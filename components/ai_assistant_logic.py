"""
AI Assistant Logic Engine
Handles user queries and generates responses based on internal database (Drugs & Protocols).
Current Implementation: Keyword-based Intent Matching (Pre-LLM)
"""

from typing import Dict, List, Any, Optional
import random

# Import Data Sources
try:
    from drugs.drug_database import DRUG_DATABASE
    from config.protocol_routing import PROTOCOL_ROUTING
    from config.protocol_lists import PROTOCOL_LISTS, SPECIALTY_LIST
except ImportError:
    DRUG_DATABASE = {}
    PROTOCOL_ROUTING = {}
    PROTOCOL_LISTS = {}
    SPECIALTY_LIST = []

def find_protocol_context(protocol_id: str, keyword: str) -> tuple[Optional[str], Optional[str]]:
    """
    Find the Specialty and Full Protocol Name for a given protocol ID/keyword.
    heuristic search in PROTOCOL_LISTS.
    """
    # 1. Try to find by keyword match in lists
    for specialty, p_list in PROTOCOL_LISTS.items():
        for p_name in p_list:
            # Check if keyword is in protocol name (flexible check)
            p_name_clean = p_name.split(' ', 1)[-1] if ' ' in p_name else p_name
            if keyword.lower() in p_name_clean.lower() or p_name_clean.lower() in keyword.lower():
                # Find the full specialty string that matches the key
                full_specialty = next((s for s in SPECIALTY_LIST if specialty in s), specialty)
                return full_specialty, p_name
                
    # 2. If not found, map some common IDs to specialties manually (Fallback)
    id_map = {
        "anaphylaxis": "🚨 Cấp cứu (Emergency)",
        "cardiac_arrest": "🚨 Cấp cứu (Emergency)",
        "sepsis": "🚨 Cấp cứu (Emergency)",
        "stemi": "❤️ Tim mạch (Cardiology)",
        "asthma": "🫁 Hô hấp (Respiratory)"
    }
    if protocol_id in id_map:
        return id_map[protocol_id], None
        
    # Default fallback
    return "🚨 Cấp cứu (Emergency)", None

def get_ai_response(query: str) -> Dict[str, Any]:
    """
    Process user query and return response
    
    Args:
        query: User input string
        
    Returns:
        Dict with keys:
        - content: Main answer text (Markdown)
        - sources: List of source items (optional)
        - type: 'text', 'drug_card', 'protocol_link'
    """
    query_lower = query.lower().strip()
    
    # 1. GREETINGS
    greetings = ['xin chào', 'hi', 'hello', 'chao', 'alo']
    if any(q == query_lower for q in greetings):
        return {
            "content": "Xin chào! Tôi là trợ lý AI y khoa. Tôi có thể giúp gì cho bạn? \n\nVí dụ: Bạn có thể hỏi về *'Liều dùng Paracetamol'* hoặc *'Phác đồ sốc phản vệ'*.",
            "type": "text"
        }

    # 2. DRUG SEARCH INTENT
    # Check if query matches any drug name
    found_drugs = []
    for drug_name, data in DRUG_DATABASE.items():
        if drug_name.lower() in query_lower:
            found_drugs.append((drug_name, data))
            
    if found_drugs:
        # Sort by length similarity to prioritize exact matches
        found_drugs.sort(key=lambda x: len(x[0]), reverse=True)
        best_match_name, best_match_data = found_drugs[0]
        
        # Determine specific question about drug
        response_content = f"### 💊 Thông tin về {best_match_name}\n\n"
        
        if "liều" in query_lower or "dose" in query_lower:
            dosing = best_match_data.get('dosing', {})
            if isinstance(dosing, dict):
                response_content += "**Liều dùng:**\n"
                for population, dose in dosing.items():
                    response_content += f"- **{population}:** {dose}\n"
            else:
                 response_content += f"**Liều dùng:** {dosing}\n"
                 
        elif "tác dụng phụ" in query_lower or "side effect" in query_lower:
             response_content += f"**Tác dụng phụ:** {best_match_data.get('side_effects', 'Chưa có dữ liệu')}\n"
             
        elif "chống chỉ định" in query_lower or "contraindication" in query_lower:
             response_content += f"**Chống chỉ định:** {best_match_data.get('contraindications', 'Chưa có dữ liệu')}\n"
             
        elif "tương tác" in query_lower or "interaction" in query_lower:
             # Basic info, refer to checker
             response_content += "⚠️ **Tương tác thuốc:**\nĐể kiểm tra tương tác chi tiết, vui lòng sử dụng công cụ *'Kiểm tra tương tác thuốc'* chuyên biệt trong phần Thuốc."
        
        else:
            # General info summary
            response_content += f"**Nhóm thuốc:** {best_match_data.get('group', 'Unknown')}\n"
            response_content += f"**Chỉ định:** {', '.join(best_match_data.get('indications', []))}\n"
            response_content += f"**Dược động học:** {best_match_data.get('pharmacokinetics', '')}\n"

        return {
            "content": response_content,
            "type": "drug_card",
            "data": best_match_data
        }

    # 3. PROTOCOL SEARCH INTENT
    # Check if query matches any protocol keyword
    found_protocols = []
    for p_id, p_config in PROTOCOL_ROUTING.items():
        keywords = p_config.get('keywords', [])
        for kw in keywords:
            if kw.lower() in query_lower:
                found_protocols.append((p_id, kw, p_config))
                break
    
    if found_protocols:
        # Pick best match (priority)
        found_protocols.sort(key=lambda x: x[2].get('priority', 0), reverse=True)
        p_id, match_kw, p_config = found_protocols[0]
        
        # Determine context for navigation
        specialty, full_p_name = find_protocol_context(p_id, match_kw)
        
        # Get protocol title for display (use full name if found, else Title case keyword)
        display_name = full_p_name.split(' ', 1)[-1] if full_p_name and ' ' in full_p_name else match_kw.title()
        
        response_content = f"### 📋 Phác đồ: {display_name}\n\n"
        response_content += f"Tôi tìm thấy phác đồ điều trị liên quan đến **'{match_kw}'** trong hệ thống.\n"
        if specialty:
            response_content += f"*Chuyên khoa: {specialty}*\n"
        
        response_content += f"\nBạn có thể xem chi tiết phác đồ này tại module Protocols."
        
        return {
            "content": response_content,
            "type": "protocol_link",
            "protocol_id": full_p_name if full_p_name else p_id, # Prefer full name for deep link
            "specialty": specialty
        }

    # 4. FALLBACK
    return {
        "content": "Xin lỗi, tôi chưa tìm thấy thông tin phù hợp trong cơ sở dữ liệu thuốc và phác đồ hiện có.\n\nHãy thử dùng từ khóa cụ thể hơn, ví dụ: *'Metformin'*, *'Sốc phản vệ'*, *'Tăng huyết áp'*.",
        "type": "text"
    }

