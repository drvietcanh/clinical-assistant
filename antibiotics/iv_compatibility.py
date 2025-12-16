"""
IV Compatibility Checker - Phase 5
Kiểm tra tính tương thích khi pha chế IV
"""

import streamlit as st
from typing import Dict, List, Tuple, Optional

# IV Compatibility Database
# Format: {("Drug1", "Drug2"): {"compatible": True/False, "notes": "...", "sources": [...]}}
IV_COMPATIBILITY_DB = {
    # Vancomycin
    ("Vancomycin", "Piperacillin-Tazobactam"): {
        "compatible": False,
        "notes": "Không tương thích - Tạo kết tủa. Pha riêng, truyền riêng hoặc rửa line giữa các liều.",
        "severity": "major",
        "sources": ["Trissel's IV Compatibility", "ASHP Handbook"]
    },
    ("Vancomycin", "Ceftriaxone"): {
        "compatible": False,
        "notes": "Không tương thích - Tạo kết tủa. Pha riêng, truyền riêng.",
        "severity": "major",
        "sources": ["Trissel's IV Compatibility"]
    },
    ("Vancomycin", "Aminoglycosides"): {
        "compatible": False,
        "notes": "Không tương thích - Tạo kết tủa. Pha riêng, truyền riêng. Ngoài ra, tăng nguy cơ độc thận khi phối hợp.",
        "severity": "major",
        "sources": ["Trissel's IV Compatibility", "ASHP Handbook"]
    },
    ("Vancomycin", "Amphotericin B"): {
        "compatible": False,
        "notes": "Không tương thích - Tạo kết tủa.",
        "severity": "major",
        "sources": ["Trissel's IV Compatibility"]
    },
    ("Vancomycin", "NS"): {
        "compatible": True,
        "notes": "Tương thích với Normal Saline (0.9% NaCl).",
        "severity": "info",
        "sources": ["Trissel's IV Compatibility"]
    },
    ("Vancomycin", "D5W"): {
        "compatible": True,
        "notes": "Tương thích với Dextrose 5% in Water.",
        "severity": "info",
        "sources": ["Trissel's IV Compatibility"]
    },
    
    # Piperacillin-Tazobactam
    ("Piperacillin-Tazobactam", "Vancomycin"): {
        "compatible": False,
        "notes": "Không tương thích - Tạo kết tủa. Pha riêng, truyền riêng hoặc rửa line giữa các liều.",
        "severity": "major",
        "sources": ["Trissel's IV Compatibility", "ASHP Handbook"]
    },
    ("Piperacillin-Tazobactam", "Aminoglycosides"): {
        "compatible": False,
        "notes": "Không tương thích - Tạo kết tủa. Pha riêng, truyền riêng.",
        "severity": "major",
        "sources": ["Trissel's IV Compatibility"]
    },
    ("Piperacillin-Tazobactam", "NS"): {
        "compatible": True,
        "notes": "Tương thích với Normal Saline.",
        "severity": "info",
        "sources": ["Trissel's IV Compatibility"]
    },
    
    # Ceftriaxone
    ("Ceftriaxone", "Vancomycin"): {
        "compatible": False,
        "notes": "Không tương thích - Tạo kết tủa. Pha riêng, truyền riêng.",
        "severity": "major",
        "sources": ["Trissel's IV Compatibility"]
    },
    ("Ceftriaxone", "Calcium"): {
        "compatible": False,
        "notes": "Không tương thích với calcium - Tạo kết tủa. Tránh pha chung hoặc truyền cùng lúc.",
        "severity": "major",
        "sources": ["FDA Warning", "Trissel's IV Compatibility"]
    },
    ("Ceftriaxone", "NS"): {
        "compatible": True,
        "notes": "Tương thích với Normal Saline.",
        "severity": "info",
        "sources": ["Trissel's IV Compatibility"]
    },
    
    # Meropenem
    ("Meropenem", "NS"): {
        "compatible": True,
        "notes": "Tương thích với Normal Saline.",
        "severity": "info",
        "sources": ["Trissel's IV Compatibility"]
    },
    ("Meropenem", "D5W"): {
        "compatible": True,
        "notes": "Tương thích với Dextrose 5%.",
        "severity": "info",
        "sources": ["Trissel's IV Compatibility"]
    },
    
    # Aminoglycosides
    ("Aminoglycosides", "Vancomycin"): {
        "compatible": False,
        "notes": "Không tương thích - Tạo kết tủa. Pha riêng, truyền riêng. Ngoài ra, tăng nguy cơ độc thận khi phối hợp.",
        "severity": "major",
        "sources": ["Trissel's IV Compatibility", "ASHP Handbook"]
    },
    ("Aminoglycosides", "Beta-lactams"): {
        "compatible": False,
        "notes": "Không tương thích - Tạo kết tủa. Pha riêng, truyền riêng.",
        "severity": "major",
        "sources": ["Trissel's IV Compatibility"]
    },
    
    # Common IV fluids
    ("NS", "D5W"): {
        "compatible": True,
        "notes": "Tương thích.",
        "severity": "info",
        "sources": ["Standard"]
    }
}


def normalize_drug_name(drug_name: str) -> str:
    """
    Normalize drug name for matching
    """
    # Remove common variations
    normalized = drug_name.strip()
    
    # Handle common aliases
    aliases = {
        "gentamicin": "Aminoglycosides",
        "tobramycin": "Aminoglycosides",
        "amikacin": "Aminoglycosides",
        "piperacillin/tazobactam": "Piperacillin-Tazobactam",
        "pip/taz": "Piperacillin-Tazobactam",
        "zosyn": "Piperacillin-Tazobactam"
    }
    
    normalized_lower = normalized.lower()
    for alias, standard in aliases.items():
        if alias in normalized_lower:
            return standard
    
    return normalized


def check_iv_compatibility(drug1: str, drug2: str) -> Optional[Dict]:
    """
    Check IV compatibility between two drugs
    
    Args:
        drug1: Tên thuốc 1
        drug2: Tên thuốc 2
    
    Returns:
        Dict với compatibility info hoặc None nếu không tìm thấy
    """
    drug1_norm = normalize_drug_name(drug1)
    drug2_norm = normalize_drug_name(drug2)
    
    # Check both orders
    key1 = (drug1_norm, drug2_norm)
    key2 = (drug2_norm, drug1_norm)
    
    if key1 in IV_COMPATIBILITY_DB:
        return IV_COMPATIBILITY_DB[key1]
    elif key2 in IV_COMPATIBILITY_DB:
        return IV_COMPATIBILITY_DB[key2]
    
    return None


def check_multiple_drugs(drugs: List[str]) -> List[Dict]:
    """
    Check compatibility for multiple drugs
    
    Args:
        drugs: List tên thuốc
    
    Returns:
        List of compatibility results
    """
    results = []
    
    # Check all pairs
    for i in range(len(drugs)):
        for j in range(i + 1, len(drugs)):
            compat = check_iv_compatibility(drugs[i], drugs[j])
            if compat:
                results.append({
                    "drug1": drugs[i],
                    "drug2": drugs[j],
                    **compat
                })
            else:
                # Unknown compatibility - warn
                results.append({
                    "drug1": drugs[i],
                    "drug2": drugs[j],
                    "compatible": None,
                    "notes": "Không có dữ liệu tương thích. Khuyến cáo pha riêng và truyền riêng để an toàn.",
                    "severity": "warning",
                    "sources": []
                })
    
    return results


def render_iv_compatibility_checker(antibiotic_name: str):
    """
    Render IV compatibility checker UI
    
    Args:
        antibiotic_name: Tên kháng sinh chính
    """
    st.markdown("---")
    st.markdown("### 💉 Kiểm tra tương thích IV")
    
    st.info("""
    **Kiểm tra tính tương thích khi pha chế IV:**
    - Tránh tạo kết tủa hoặc mất tác dụng
    - Đảm bảo an toàn khi truyền cùng lúc
    - Dựa trên Trissel's IV Compatibility và ASHP Handbook
    """)
    
    # Input: Other drugs
    st.markdown("#### 📋 Thuốc khác đang truyền")
    
    # Sanitize antibiotic name for keys
    from .database_display import _make_safe_session_key
    safe_ab_name = _make_safe_session_key("iv_compat", antibiotic_name)
    
    other_drugs_text = st.text_input(
        "Nhập tên thuốc (phân cách bằng dấu phẩy):",
        placeholder="Ví dụ: Piperacillin-Tazobactam, Ceftriaxone, NS",
        key=_make_safe_session_key(safe_ab_name, "drugs"),
        help="Nhập các thuốc hoặc dịch truyền khác đang dùng cùng lúc"
    )
    
    # Common IV fluids
    st.markdown("#### 💧 Dịch truyền")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        use_ns = st.checkbox("Normal Saline (NS)", key=_make_safe_session_key(safe_ab_name, "ns"))
    with col2:
        use_d5w = st.checkbox("D5W", key=_make_safe_session_key(safe_ab_name, "d5w"))
    with col3:
        use_calcium = st.checkbox("Calcium", key=_make_safe_session_key(safe_ab_name, "calcium"))
    
    # Build drug list
    drugs_to_check = [antibiotic_name]
    
    if other_drugs_text:
        other_drugs = [d.strip() for d in other_drugs_text.split(",") if d.strip()]
        drugs_to_check.extend(other_drugs)
    
    if use_ns:
        drugs_to_check.append("NS")
    if use_d5w:
        drugs_to_check.append("D5W")
    if use_calcium:
        drugs_to_check.append("Calcium")
    
    if len(drugs_to_check) < 2:
        st.warning("⚠️ Vui lòng chọn ít nhất 1 thuốc/dịch truyền khác để kiểm tra")
        return
    
    # Check button
    if st.button("🔍 Kiểm tra tương thích", type="primary", key=_make_safe_session_key(safe_ab_name, "check")):
        results = check_multiple_drugs(drugs_to_check)
        
        if not results:
            st.info("✅ Không có thông tin tương thích trong database. Khuyến cáo pha riêng và truyền riêng.")
            return
        
        st.markdown("---")
        st.markdown("### 📊 Kết quả Kiểm tra")
        
        # Group by compatibility
        compatible = []
        incompatible = []
        unknown = []
        
        for result in results:
            if result['compatible'] is True:
                compatible.append(result)
            elif result['compatible'] is False:
                incompatible.append(result)
            else:
                unknown.append(result)
        
        # Show incompatible first (most important)
        if incompatible:
            st.error("### 🚨 Không Tương Thích")
            for result in incompatible:
                st.error(f"""
                **{result['drug1']} + {result['drug2']}**
                
                {result['notes']}
                
                **Khuyến cáo:** Pha riêng, truyền riêng hoặc rửa line giữa các liều.
                """)
        
        # Show unknown
        if unknown:
            st.warning("### ⚠️ Chưa Có Dữ Liệu")
            for result in unknown:
                st.warning(f"""
                **{result['drug1']} + {result['drug2']}**
                
                {result['notes']}
                """)
        
        # Show compatible
        if compatible:
            st.success("### ✅ Tương Thích")
            for result in compatible:
                st.info(f"""
                **{result['drug1']} + {result['drug2']}**
                
                {result['notes']}
                """)
        
        # Summary
        st.markdown("---")
        if incompatible:
            st.error(f"⚠️ **Cảnh báo:** Có {len(incompatible)} cặp thuốc không tương thích. Cần pha riêng và truyền riêng!")
        elif unknown:
            st.warning(f"ℹ️ **Lưu ý:** Có {len(unknown)} cặp thuốc chưa có dữ liệu. Khuyến cáo pha riêng để an toàn.")
        else:
            st.success(f"✅ **Tất cả {len(compatible)} cặp thuốc đều tương thích!**")


def get_compatibility_summary(drug1: str, drug2: str) -> str:
    """
    Get quick compatibility summary for display
    
    Returns:
        Short summary string
    """
    compat = check_iv_compatibility(drug1, drug2)
    
    if compat is None:
        return "❓ Chưa có dữ liệu"
    elif compat['compatible']:
        return "✅ Tương thích"
    else:
        return "❌ Không tương thích"

