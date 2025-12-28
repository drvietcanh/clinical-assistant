"""
Auto Link Scores to Content
Tự động phát hiện và gắn liên kết scores cho articles và protocols
Chạy thường xuyên để cập nhật mapping
"""

import re
import json
from pathlib import Path
from typing import Dict, List, Set, Tuple
from collections import defaultdict

# Import scores config
import sys
import ast
sys.path.insert(0, str(Path(__file__).parent.parent))
from scores.config import SCORES_BY_SPECIALTY

# Parse PROTOCOL_ROUTING without importing streamlit
def parse_protocol_routing():
    """Parse PROTOCOL_ROUTING from file without importing streamlit."""
    routing_file = Path(__file__).parent.parent / "config" / "protocol_routing.py"
    content = routing_file.read_text(encoding="utf-8")
    
    # Extract protocol info using regex - improved pattern
    protocol_info = {}
    
    # Pattern to match: "protocol_id": { ... "keywords": [...] ... "render": render_func ...
    pattern = r'"([^"]+)":\s*\{[^}]*?"keywords":\s*\[([^\]]+)\][^}]*?"render":\s*(\w+)'
    matches = re.finditer(pattern, content, re.DOTALL)
    
    for match in matches:
        protocol_id = match.group(1)
        keywords_str = match.group(2)
        render_func = match.group(3)
        
        # Extract keywords - handle both single and double quotes
        keywords = re.findall(r'["\']([^"\']+)["\']', keywords_str)
        if keywords:
            protocol_info[protocol_id] = {
                "keywords": keywords,
                "render_func": render_func
            }
    
    return protocol_info

PROTOCOL_ROUTING = parse_protocol_routing()


# Keywords mapping: score keywords -> score_id, specialty
SCORE_KEYWORDS: Dict[str, List[Tuple[str, str]]] = {
    # Emergency & Critical Care
    "news2": [("NEWS2", "🚨 Cấp cứu & Hồi sức (Emergency & Critical Care)")],
    "mews": [("MEWS", "🚨 Cấp cứu & Hồi sức (Emergency & Critical Care)")],
    "qsofa": [("qSOFA", "🚨 Cấp cứu & Hồi sức (Emergency & Critical Care)")],
    "sofa": [("SOFA", "🚨 Cấp cứu & Hồi sức (Emergency & Critical Care)"), ("SOFA-2 (2025)", "🚨 Cấp cứu & Hồi sức (Emergency & Critical Care)")],
    "apache": [("APACHE II", "🚨 Cấp cứu & Hồi sức (Emergency & Critical Care)"), ("APACHE III", "🚨 Cấp cứu & Hồi sức (Emergency & Critical Care)")],
    "saps": [("SAPS II", "🚨 Cấp cứu & Hồi sức (Emergency & Critical Care)"), ("SAPS III", "🚨 Cấp cứu & Hồi sức (Emergency & Critical Care)")],
    "mods": [("MODS", "🚨 Cấp cứu & Hồi sức (Emergency & Critical Care)")],
    "lods": [("LODS", "🚨 Cấp cứu & Hồi sức (Emergency & Critical Care)")],
    "sirs": [("SIRS", "🦠 Nhiễm khuẩn (Infectious Disease)")],
    
    # Cardiology
    "heart score": [("HEART Score", "❤️ Tim mạch (Cardiology)")],
    "timi": [("TIMI Risk", "❤️ Tim mạch (Cardiology)")],
    "grace": [("GRACE Score", "❤️ Tim mạch (Cardiology)")],
    "killip": [("Killip", "❤️ Tim mạch (Cardiology)")],
    "nyha": [("NYHA", "❤️ Tim mạch (Cardiology)")],
    "cha2ds2": [("CHA2DS2-VASc", "❤️ Tim mạch (Cardiology)")],
    "has-bled": [("HAS-BLED", "❤️ Tim mạch (Cardiology)")],
    "ascvd": [("ASCVD Risk", "❤️ Tim mạch (Cardiology)")],
    "score2": [("SCORE2", "❤️ Tim mạch (Cardiology)"), ("SCORE2-OP", "❤️ Tim mạch (Cardiology)")],
    "qtc": [("Corrected QT", "❤️ Tim mạch (Cardiology)")],
    "qt interval": [("Corrected QT", "❤️ Tim mạch (Cardiology)")],
    
    # Respiratory
    "perc": [("PERC", "🫁 Hô hấp (Respiratory)")],
    "curb-65": [("CURB-65", "🫁 Hô hấp (Respiratory)")],
    "curb65": [("CURB-65", "🫁 Hô hấp (Respiratory)")],
    "psi": [("PSI/PORT", "🫁 Hô hấp (Respiratory)")],
    "port": [("PSI/PORT", "🫁 Hô hấp (Respiratory)")],
    "wells pe": [("Wells PE", "🫁 Hô hấp (Respiratory)")],
    "pesi": [("PESI", "🫁 Hô hấp (Respiratory)")],
    "smart-cop": [("SMART-COP", "🫁 Hô hấp (Respiratory)")],
    "bode": [("BODE Index", "🫁 Hô hấp (Respiratory)")],
    "ards berlin": [("ARDS Berlin", "🫁 Hô hấp (Respiratory)")],
    "ards": [("ARDS Berlin", "🫁 Hô hấp (Respiratory)")],
    
    # Neurology
    "gcs": [("GCS", "🧠 Thần kinh (Neurology)")],
    "glasgow": [("GCS", "🧠 Thần kinh (Neurology)")],
    "nihss": [("NIHSS", "🧠 Thần kinh (Neurology)")],
    "ich score": [("ICH Score", "🧠 Thần kinh (Neurology)")],
    "hunt": [("Hunt & Hess", "🧠 Thần kinh (Neurology)")],
    "mrs": [("mRS", "🧠 Thần kinh (Neurology)")],
    "modified rankin": [("mRS", "🧠 Thần kinh (Neurology)")],
    "aspects": [("ASPECTS", "🧠 Thần kinh (Neurology)")],
    "abcd2": [("ABCD2", "🧠 Thần kinh (Neurology)")],
    "barthel": [("Barthel Index", "🧠 Thần kinh (Neurology)")],
    "four score": [("FOUR Score", "🧠 Thần kinh (Neurology)")],
    
    # GI/Hepatology
    "bisap": [("BISAP", "🩸 Tiêu hóa - Gan Mật (GI/Hepatology)")],
    "child-pugh": [("Child-Pugh", "🩸 Tiêu hóa - Gan Mật (GI/Hepatology)")],
    "child pugh": [("Child-Pugh", "🩸 Tiêu hóa - Gan Mật (GI/Hepatology)")],
    "meld": [("MELD", "🩸 Tiêu hóa - Gan Mật (GI/Hepatology)"), ("MELD-Na", "🩸 Tiêu hóa - Gan Mật (GI/Hepatology)")],
    "glasgow-blatchford": [("Glasgow-Blatchford", "🩸 Tiêu hóa - Gan Mật (GI/Hepatology)")],
    "aims65": [("AIMS65", "🩸 Tiêu hóa - Gan Mật (GI/Hepatology)")],
    "rockall": [("Rockall Score", "🩸 Tiêu hóa - Gan Mật (GI/Hepatology)")],
    "ranson": [("Ranson", "🩸 Tiêu hóa - Gan Mật (GI/Hepatology)")],
    
    # Hematology
    "padua": [("Padua", "🩺 Huyết học & Đông máu (Hematology)")],
    "wells dvt": [("Wells DVT", "🩺 Huyết học & Đông máu (Hematology)")],
    "4ts": [("4Ts Score", "🩺 Huyết học & Đông máu (Hematology)")],
    "dic": [("DIC Score", "🩺 Huyết học & Đông máu (Hematology)")],
    
    # Nephrology
    "egfr": [("eGFR", "🧪 Thận - Điện giải (Nephrology)")],
    "kdigo": [("KDIGO", "🧪 Thận - Điện giải (Nephrology)")],
    "rifle": [("RIFLE", "🧪 Thận - Điện giải (Nephrology)")],
    "akin": [("AKIN", "🧪 Thận - Điện giải (Nephrology)")],
    
    # Endocrinology/Metabolism
    "crcl": [("CrCl", "💉 Nội tiết - Chuyển hóa (Endocrinology/Metabolism)")],
    "cockcroft": [("CrCl", "💉 Nội tiết - Chuyển hóa (Endocrinology/Metabolism)")],
    "bmi": [("BMI/IBW/BSA", "💉 Nội tiết - Chuyển hóa (Endocrinology/Metabolism)")],
    "osmolality": [("Osmolality", "💉 Nội tiết - Chuyển hóa (Endocrinology/Metabolism)")],
    "anion gap": [("Anion Gap", "💉 Nội tiết - Chuyển hóa (Endocrinology/Metabolism)")],
    "corrected calcium": [("Corrected Ca", "💉 Nội tiết - Chuyển hóa (Endocrinology/Metabolism)")],
    "fena": [("FENa", "💉 Nội tiết - Chuyển hóa (Endocrinology/Metabolism)")],
    "hba1c": [("HbA1c", "💉 Nội tiết - Chuyển hóa (Endocrinology/Metabolism)")],
    "winter formula": [("Winter Formula", "💉 Nội tiết - Chuyển hóa (Endocrinology/Metabolism)")],
    
    # Obstetrics
    "preeclampsia": [("Preeclampsia", "🤰 Sản khoa (Obstetrics)")],
    "bishop": [("Bishop Score", "🤰 Sản khoa (Obstetrics)"), ("Modified Bishop", "🤰 Sản khoa (Obstetrics)")],
    
    # Rheumatology
    "gout": [("Gout Diagnostic", "🦴 Thấp khớp - Miễn Dịch (Rheumatology/Immunology)")],
    "das28": [("DAS28", "🦴 Thấp khớp - Miễn Dịch (Rheumatology/Immunology)")],
    
    # Surgery/Anesthesia
    "rass": [("RASS", "🔪 Phẫu thuật & Gây mê (Surgery/Anesthesia)")],
    "asa": [("ASA", "🔪 Phẫu thuật & Gây mê (Surgery/Anesthesia)")],
}


def normalize_text(text: str) -> str:
    """Normalize text for matching."""
    return text.lower().strip()


def find_scores_in_text(text: str) -> Set[Tuple[str, str]]:
    """
    Tìm các scores có trong text dựa trên keywords.
    
    Returns:
        Set of (score_id, specialty) tuples
    """
    found_scores = set()
    text_lower = normalize_text(text)
    
    for keyword, score_list in SCORE_KEYWORDS.items():
        if keyword in text_lower:
            found_scores.update(score_list)
    
    # Also check for direct score name mentions
    for specialty, scores in SCORES_BY_SPECIALTY.items():
        for score_id, score_info in scores.items():
            score_name = normalize_text(score_info.get("name", ""))
            if score_name and score_name in text_lower:
                found_scores.add((score_id, specialty))
    
    return found_scores


def scan_articles() -> Dict[str, List[Dict[str, str]]]:
    """
    Scan tất cả articles và tìm scores liên quan.
    
    Returns:
        Dictionary: article_id -> list of score dicts
    """
    articles_dir = Path(__file__).parent.parent / "content" / "articles"
    if not articles_dir.exists():
        return {}
    
    article_scores = {}
    
    for article_file in articles_dir.glob("*.md"):
        article_id = article_file.stem
        try:
            content = article_file.read_text(encoding="utf-8")
            found_scores = find_scores_in_text(content)
            
            if found_scores:
                score_list = []
                for score_id, specialty in found_scores:
                    score_info = SCORES_BY_SPECIALTY.get(specialty, {}).get(score_id)
                    if score_info:
                        score_list.append({
                            "score_id": score_id,
                            "specialty": specialty,
                            "reason": f"Được đề cập trong bài viết"
                        })
                
                if score_list:
                    article_scores[article_id] = score_list
        
        except Exception as e:
            print(f"Error scanning {article_file}: {e}")
    
    return article_scores


def scan_protocols() -> Dict[str, List[Dict[str, str]]]:
    """
    Scan tất cả protocols và tìm scores liên quan.
    
    Returns:
        Dictionary: protocol_function -> list of score dicts
    """
    protocol_scores = {}
    
    # Get protocol keywords and names from PROTOCOL_ROUTING
    for protocol_id, config in PROTOCOL_ROUTING.items():
        render_func = config.get("render_func")
        if not render_func:
            continue
        
        # Build text from keywords and protocol name
        keywords = config.get("keywords", [])
        text = " ".join(keywords).lower()
        text += " " + protocol_id.lower()
        
        found_scores = find_scores_in_text(text)
        
        if found_scores:
            score_list = []
            for score_id, specialty in found_scores:
                score_info = SCORES_BY_SPECIALTY.get(specialty, {}).get(score_id)
                if score_info:
                    score_list.append({
                        "score_id": score_id,
                        "specialty": specialty,
                        "reason": f"Liên quan đến protocol"
                    })
            
            if score_list:
                protocol_scores[render_func] = score_list
    
    return protocol_scores


def generate_mapping_file(article_scores: Dict, protocol_scores: Dict, output_file: Path):
    """
    Generate mapping file với format Python dict.
    """
    lines = [
        '"""',
        "Mapping between Articles/Protocols and Scores for bidirectional linking.",
        "",
        "AUTO-GENERATED by scripts/auto_link_scores_to_content.py",
        "DO NOT EDIT MANUALLY - Run the script to update",
        '"""',
        "",
        "from typing import Optional, Dict, List, Tuple",
        "from scores.config import SCORES_BY_SPECIALTY",
        "",
        "",
        "# Mapping: article_id -> list of score IDs",
        "ARTICLE_TO_SCORES: Dict[str, List[Dict[str, str]]] = {",
    ]
    
    # Articles
    for article_id, scores in sorted(article_scores.items()):
        lines.append(f'    "{article_id}": [')
        for score in scores:
            lines.append(f'        {{"score_id": "{score["score_id"]}", "specialty": "{score["specialty"]}", "reason": "{score["reason"]}"}},')
        lines.append("    ],")
        lines.append("")
    
    lines.append("}")
    lines.append("")
    lines.append("")
    lines.append("# Mapping: protocol_function -> list of score IDs")
    lines.append("PROTOCOL_TO_SCORES: Dict[str, List[Dict[str, str]]] = {")
    
    # Protocols
    for protocol_func, scores in sorted(protocol_scores.items()):
        lines.append(f'    "{protocol_func}": [')
        for score in scores:
            lines.append(f'        {{"score_id": "{score["score_id"]}", "specialty": "{score["specialty"]}", "reason": "{score["reason"]}"}},')
        lines.append("    ],")
        lines.append("")
    
    lines.append("}")
    lines.append("")
    lines.append("")
    lines.append("def get_scores_for_article(article_id: str) -> List[Dict[str, str]]:")
    lines.append('    """Get list of scores for a given article ID."""')
    lines.append("    return ARTICLE_TO_SCORES.get(article_id, [])")
    lines.append("")
    lines.append("")
    lines.append("def get_scores_for_protocol(protocol_function: str) -> List[Dict[str, str]]:")
    lines.append('    """Get list of scores for a given protocol function."""')
    lines.append("    return PROTOCOL_TO_SCORES.get(protocol_function, [])")
    lines.append("")
    lines.append("")
    lines.append("def get_score_info(score_id: str, specialty: str) -> Optional[Dict[str, str]]:")
    lines.append('    """Get score information from SCORES_BY_SPECIALTY."""')
    lines.append("    specialty_scores = SCORES_BY_SPECIALTY.get(specialty, {})")
    lines.append("    return specialty_scores.get(score_id)")
    lines.append("")
    lines.append("")
    lines.append("def has_scores(article_id: str = None, protocol_function: str = None) -> bool:")
    lines.append('    """Check if an article or protocol has associated scores."""')
    lines.append("    if article_id:")
    lines.append("        return article_id in ARTICLE_TO_SCORES and len(ARTICLE_TO_SCORES[article_id]) > 0")
    lines.append("    if protocol_function:")
    lines.append("        return protocol_function in PROTOCOL_TO_SCORES and len(PROTOCOL_TO_SCORES[protocol_function]) > 0")
    lines.append("    return False")
    
    output_file.write_text("\n".join(lines), encoding="utf-8")


def main():
    """Main function to scan and generate mapping."""
    print("[SCAN] Scanning articles...")
    article_scores = scan_articles()
    print(f"[OK] Found {len(article_scores)} articles with scores")
    
    print("\n[SCAN] Scanning protocols...")
    protocol_scores = scan_protocols()
    print(f"[OK] Found {len(protocol_scores)} protocols with scores")
    
    print("\n[GEN] Generating mapping file...")
    output_file = Path(__file__).parent.parent / "config" / "article_protocol_score_mapping.py"
    generate_mapping_file(article_scores, protocol_scores, output_file)
    print(f"[OK] Generated: {output_file}")
    
    print("\n[SUMMARY]")
    print(f"   Articles: {len(article_scores)}")
    print(f"   Protocols: {len(protocol_scores)}")
    total_scores = sum(len(scores) for scores in article_scores.values()) + sum(len(scores) for scores in protocol_scores.values())
    print(f"   Total links: {total_scores}")


if __name__ == "__main__":
    main()

