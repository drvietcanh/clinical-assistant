"""
Allergy Cross-Reactivity Checker
Kiểm tra phản ứng chéo giữa các beta-lactam và kháng sinh khác
Dựa trên dữ liệu từ IDSA, ASHP, và các nghiên cứu lâm sàng
"""

import streamlit as st
from typing import List, Dict, Optional, Tuple

# Beta-lactam cross-reactivity database
# Based on IDSA guidelines and clinical studies
BETA_LACTAM_CROSS_REACTIVITY = {
    "Penicillin": {
        "cross_reactive": {
            "Ampicillin": {"risk": "high", "rate": "5-10%", "notes": "Cùng nhóm aminopenicillin"},
            "Amoxicillin": {"risk": "high", "rate": "5-10%", "notes": "Cùng nhóm aminopenicillin"},
            "Amoxicillin-Clavulanate": {"risk": "high", "rate": "5-10%", "notes": "Cùng nhóm aminopenicillin"},
            "Piperacillin": {"risk": "high", "rate": "5-10%", "notes": "Cùng nhóm penicillin"},
            "Piperacillin-Tazobactam": {"risk": "high", "rate": "5-10%", "notes": "Cùng nhóm penicillin"},
            "Penicillin G": {"risk": "very_high", "rate": ">90%", "notes": "Cùng phân tử"},
            "Penicillin V": {"risk": "very_high", "rate": ">90%", "notes": "Cùng phân tử"},
        },
        "low_risk": {
            "Cephalosporin 1st gen": {"risk": "low", "rate": "1-2%", "notes": "Cephalosporin thế hệ 1 có nguy cơ thấp"},
            "Cephalosporin 2nd gen": {"risk": "low", "rate": "0.5-1%", "notes": "Cephalosporin thế hệ 2 có nguy cơ rất thấp"},
            "Cephalosporin 3rd gen": {"risk": "low", "rate": "0.5-1%", "notes": "Cephalosporin thế hệ 3 có nguy cơ rất thấp"},
            "Cephalosporin 4th gen": {"risk": "low", "rate": "0.5-1%", "notes": "Cephalosporin thế hệ 4 có nguy cơ rất thấp"},
            "Cephalosporin 5th gen": {"risk": "low", "rate": "0.5-1%", "notes": "Cephalosporin thế hệ 5 có nguy cơ rất thấp"},
            "Carbapenem": {"risk": "low", "rate": "1-2%", "notes": "Carbapenem có nguy cơ thấp"},
            "Monobactam": {"risk": "very_low", "rate": "<0.5%", "notes": "Aztreonam (monobactam) không có phản ứng chéo"},
        },
        "safe_alternatives": [
            "Aztreonam",
            "Vancomycin",
            "Clindamycin",
            "Daptomycin",
            "Linezolid",
            "Quinolone (Ciprofloxacin, Levofloxacin)",
            "Macrolide (Azithromycin, Clarithromycin)",
            "Tetracycline (Doxycycline)",
        ]
    },
    "Ampicillin": {
        "cross_reactive": {
            "Penicillin": {"risk": "high", "rate": "5-10%", "notes": "Cùng nhóm beta-lactam"},
            "Amoxicillin": {"risk": "very_high", "rate": ">90%", "notes": "Cùng phân tử aminopenicillin"},
            "Amoxicillin-Clavulanate": {"risk": "very_high", "rate": ">90%", "notes": "Cùng phân tử aminopenicillin"},
        },
        "low_risk": {
            "Cephalosporin": {"risk": "low", "rate": "1-2%", "notes": "Cephalosporin có nguy cơ thấp"},
            "Carbapenem": {"risk": "low", "rate": "1-2%", "notes": "Carbapenem có nguy cơ thấp"},
        },
        "safe_alternatives": [
            "Aztreonam",
            "Vancomycin",
            "Cephalosporin (thận trọng)",
            "Carbapenem (thận trọng)",
        ]
    },
    "Cephalosporin": {
        "cross_reactive": {
            "Penicillin": {"risk": "low", "rate": "1-2%", "notes": "Nguy cơ thấp nhưng vẫn có thể xảy ra"},
            "Ampicillin": {"risk": "low", "rate": "1-2%", "notes": "Nguy cơ thấp"},
            "Amoxicillin": {"risk": "low", "rate": "1-2%", "notes": "Nguy cơ thấp"},
            "Other Cephalosporin": {"risk": "variable", "rate": "1-5%", "notes": "Phụ thuộc vào thế hệ và cấu trúc"},
        },
        "low_risk": {
            "Carbapenem": {"risk": "low", "rate": "1-2%", "notes": "Carbapenem có nguy cơ thấp"},
            "Monobactam": {"risk": "very_low", "rate": "<0.5%", "notes": "Aztreonam an toàn"},
        },
        "safe_alternatives": [
            "Aztreonam",
            "Vancomycin",
            "Carbapenem (thận trọng)",
        ]
    },
    "Carbapenem": {
        "cross_reactive": {
            "Penicillin": {"risk": "low", "rate": "1-2%", "notes": "Nguy cơ thấp nhưng vẫn có thể xảy ra"},
            "Cephalosporin": {"risk": "low", "rate": "1-2%", "notes": "Nguy cơ thấp"},
        },
        "low_risk": {
            "Monobactam": {"risk": "very_low", "rate": "<0.5%", "notes": "Aztreonam an toàn"},
        },
        "safe_alternatives": [
            "Aztreonam",
            "Vancomycin",
            "Quinolone",
            "Macrolide",
        ]
    },
}

# Specific drug to class mapping
DRUG_TO_CLASS = {
    # Penicillins
    "Penicillin G": "Penicillin",
    "Penicillin V": "Penicillin",
    "Ampicillin": "Ampicillin",
    "Amoxicillin": "Ampicillin",
    "Amoxicillin-Clavulanate": "Ampicillin",
    "Piperacillin": "Penicillin",
    "Piperacillin-Tazobactam": "Penicillin",
    "Nafcillin": "Penicillin",
    "Oxacillin": "Penicillin",
    "Dicloxacillin": "Penicillin",
    
    # Cephalosporins
    "Cefazolin": "Cephalosporin",
    "Cephalexin": "Cephalosporin",
    "Cefuroxime": "Cephalosporin",
    "Cefotetan": "Cephalosporin",
    "Ceftriaxone": "Cephalosporin",
    "Cefotaxime": "Cephalosporin",
    "Ceftazidime": "Cephalosporin",
    "Cefepime": "Cephalosporin",
    "Ceftaroline": "Cephalosporin",
    
    # Carbapenems
    "Imipenem-Cilastatin": "Carbapenem",
    "Meropenem": "Carbapenem",
    "Ertapenem": "Carbapenem",
    "Doripenem": "Carbapenem",
    
    # Monobactam
    "Aztreonam": "Monobactam",
}

# Allergy severity levels
ALLERGY_SEVERITY = {
    "anaphylaxis": "Nghiêm trọng (Sốc phản vệ)",
    "severe": "Nặng (Phản ứng nặng)",
    "moderate": "Trung bình (Phát ban, ngứa)",
    "mild": "Nhẹ (Phản ứng nhẹ)",
    "unknown": "Không rõ",
}


def get_drug_class(drug_name: str) -> Optional[str]:
    """Get beta-lactam class for a drug"""
    return DRUG_TO_CLASS.get(drug_name)


def check_cross_reactivity(allergic_drug: str, proposed_drug: str) -> Dict:
    """
    Check cross-reactivity between allergic drug and proposed drug
    
    Args:
        allergic_drug: Drug that patient is allergic to
        proposed_drug: Drug being considered for use
    
    Returns:
        dict with cross-reactivity information
    """
    allergic_class = get_drug_class(allergic_drug)
    proposed_class = get_drug_class(proposed_drug)
    
    # If same drug
    if allergic_drug == proposed_drug:
        return {
            "cross_reactive": True,
            "risk": "very_high",
            "rate": ">90%",
            "recommendation": "CHỐNG CHỈ ĐỊNH: Cùng một thuốc",
            "severity": "contraindicated"
        }
    
    # If not beta-lactams, assume safe (but check other interactions separately)
    if not allergic_class or not proposed_class:
        return {
            "cross_reactive": False,
            "risk": "unknown",
            "rate": "N/A",
            "recommendation": "Không phải beta-lactam, kiểm tra tương tác thuốc khác",
            "severity": "safe"
        }
    
    # Get cross-reactivity data
    if allergic_class in BETA_LACTAM_CROSS_REACTIVITY:
        class_data = BETA_LACTAM_CROSS_REACTIVITY[allergic_class]
        
        # Check direct cross-reactivity
        if proposed_drug in class_data.get("cross_reactive", {}):
            react_data = class_data["cross_reactive"][proposed_drug]
            risk = react_data["risk"]
            rate = react_data["rate"]
            notes = react_data.get("notes", "")
            
            if risk == "very_high":
                recommendation = f"🚨 CHỐNG CHỈ ĐỊNH: Nguy cơ phản ứng chéo rất cao ({rate})"
                severity = "contraindicated"
            elif risk == "high":
                recommendation = f"⚠️ THẬN TRỌNG: Nguy cơ phản ứng chéo cao ({rate}). {notes}"
                severity = "high_risk"
            else:
                recommendation = f"⚠️ Thận trọng: Nguy cơ phản ứng chéo ({rate})"
                severity = "moderate_risk"
            
            return {
                "cross_reactive": True,
                "risk": risk,
                "rate": rate,
                "notes": notes,
                "recommendation": recommendation,
                "severity": severity
            }
        
        # Check if in low-risk category
        for category, react_data in class_data.get("low_risk", {}).items():
            if proposed_class in category or proposed_drug in category:
                return {
                    "cross_reactive": False,
                    "risk": react_data["risk"],
                    "rate": react_data["rate"],
                    "notes": react_data["notes"],
                    "recommendation": f"✅ Nguy cơ thấp ({react_data['rate']}): {react_data['notes']}. Có thể dùng thận trọng.",
                    "severity": "low_risk"
                }
    
    # If same class but not in database, assume moderate risk
    if allergic_class == proposed_class:
        return {
            "cross_reactive": True,
            "risk": "moderate",
            "rate": "Unknown",
            "recommendation": "⚠️ Cùng nhóm beta-lactam. Thận trọng, cân nhắc test da hoặc desensitization.",
            "severity": "moderate_risk"
        }
    
    # Different classes - low risk
    return {
        "cross_reactive": False,
        "risk": "low",
        "rate": "1-2%",
        "recommendation": "✅ Khác nhóm beta-lactam. Nguy cơ thấp, có thể dùng thận trọng.",
        "severity": "low_risk"
    }


def get_safe_alternatives(allergic_drug: str) -> List[str]:
    """Get list of safe alternative antibiotics"""
    allergic_class = get_drug_class(allergic_drug)
    
    if allergic_class and allergic_class in BETA_LACTAM_CROSS_REACTIVITY:
        return BETA_LACTAM_CROSS_REACTIVITY[allergic_class].get("safe_alternatives", [])
    
    # Default safe alternatives if class not found
    return [
        "Vancomycin",
        "Clindamycin",
        "Daptomycin",
        "Linezolid",
        "Quinolone (Ciprofloxacin, Levofloxacin)",
        "Macrolide (Azithromycin, Clarithromycin)",
        "Tetracycline (Doxycycline)",
        "Aztreonam (nếu cần Gram-negative coverage)",
    ]


def render_allergy_checker():
    """Render the Allergy Cross-Reactivity Checker UI"""
    
    st.markdown("### 🔍 Kiểm tra Phản ứng Chéo (Allergy Cross-Reactivity)")
    st.caption("Kiểm tra nguy cơ phản ứng chéo giữa các beta-lactam và kháng sinh khác")
    
    st.info("""
    **💡 Lưu ý:**
    - Phản ứng chéo giữa beta-lactam phụ thuộc vào cấu trúc phân tử và loại phản ứng dị ứng
    - Phản ứng tức thì (anaphylaxis) có nguy cơ cao hơn phản ứng chậm (phát ban)
    - Luôn tham khảo ý kiến chuyên gia dị ứng khi có nghi ngờ
    - Có thể cân nhắc test da hoặc desensitization trong trường hợp cần thiết
    """)
    
    # Input section
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🚫 Thuốc Dị Ứng")
        allergic_drug = st.text_input(
            "Nhập tên thuốc bệnh nhân dị ứng:",
            placeholder="Ví dụ: Penicillin, Ampicillin, Ceftriaxone...",
            key="allergic_drug_input"
        )
        
        # Show autocomplete suggestions
        if allergic_drug:
            matching_drugs = [drug for drug in DRUG_TO_CLASS.keys() 
                            if allergic_drug.lower() in drug.lower()]
            if matching_drugs:
                st.caption("💡 Gợi ý:")
                for drug in matching_drugs[:5]:
                    if st.button(f"📌 {drug}", key=f"suggest_allergic_{drug}"):
                        st.session_state.allergic_drug_input = drug
                        st.rerun()
        
        allergy_severity = st.selectbox(
            "Mức độ phản ứng dị ứng:",
            options=list(ALLERGY_SEVERITY.keys()),
            format_func=lambda x: ALLERGY_SEVERITY[x],
            key="allergy_severity"
        )
    
    with col2:
        st.markdown("#### 💊 Thuốc Đề Xuất")
        proposed_drug = st.text_input(
            "Nhập tên thuốc muốn sử dụng:",
            placeholder="Ví dụ: Ceftriaxone, Meropenem, Vancomycin...",
            key="proposed_drug_input"
        )
        
        # Show autocomplete suggestions
        if proposed_drug:
            matching_drugs = [drug for drug in DRUG_TO_CLASS.keys() 
                            if proposed_drug.lower() in drug.lower()]
            if matching_drugs:
                st.caption("💡 Gợi ý:")
                for drug in matching_drugs[:5]:
                    if st.button(f"📌 {drug}", key=f"suggest_proposed_{drug}"):
                        st.session_state.proposed_drug_input = drug
                        st.rerun()
    
    st.markdown("---")
    
    # Check button
    if st.button("🔍 Kiểm tra Phản ứng Chéo", type="primary", use_container_width=True):
        if not allergic_drug or not proposed_drug:
            st.warning("⚠️ Vui lòng nhập đầy đủ thông tin")
            return
        
        # Perform check
        result = check_cross_reactivity(allergic_drug, proposed_drug)
        
        # Display results
        st.markdown("### 📊 Kết quả Kiểm tra")
        
        # Risk level display
        risk_colors = {
            "contraindicated": "#f44336",
            "high_risk": "#ff9800",
            "moderate_risk": "#ffc107",
            "low_risk": "#4caf50",
            "safe": "#4caf50"
        }
        
        risk_color = risk_colors.get(result["severity"], "#757575")
        
        st.markdown(f"""
        <div style='
            background: {risk_color};
            color: white;
            padding: 20px;
            border-radius: 12px;
            margin-bottom: 20px;
        '>
            <h3 style='margin: 0 0 10px 0; color: white;'>{result["recommendation"]}</h3>
            <p style='margin: 5px 0;'><strong>Tỷ lệ phản ứng chéo:</strong> {result["rate"]}</p>
            {f'<p style="margin: 5px 0;"><strong>Ghi chú:</strong> {result.get("notes", "")}</p>' if result.get("notes") else ""}
        </div>
        """, unsafe_allow_html=True)
        
        # Additional information based on allergy severity
        if allergy_severity == "anaphylaxis":
            st.error("""
            🚨 **Phản ứng tức thì (Anaphylaxis):**
            - Nguy cơ phản ứng chéo cao hơn phản ứng chậm
            - Cần thận trọng với TẤT CẢ beta-lactam
            - Cân nhắc test da trước khi dùng
            - Có thể cần desensitization nếu không có lựa chọn khác
            """)
        elif allergy_severity == "severe":
            st.warning("""
            ⚠️ **Phản ứng nặng:**
            - Thận trọng với beta-lactam cùng nhóm
            - Có thể cân nhắc beta-lactam khác nhóm (nguy cơ thấp)
            - Tham khảo ý kiến chuyên gia dị ứng
            """)
        
        # Show safe alternatives
        st.markdown("---")
        st.markdown("### ✅ Thuốc Thay Thế An Toàn")
        
        safe_alternatives = get_safe_alternatives(allergic_drug)
        
        if safe_alternatives:
            for alt in safe_alternatives:
                st.markdown(f"- **{alt}**")
        else:
            st.info("💡 Tham khảo ý kiến chuyên gia để chọn thuốc thay thế phù hợp")
        
        # Clinical recommendations
        st.markdown("---")
        st.markdown("### 📋 Khuyến Cáo Lâm Sàng")
        
        if result["severity"] == "contraindicated":
            st.error("""
            **CHỐNG CHỈ ĐỊNH:**
            - Không sử dụng thuốc này
            - Chọn thuốc thay thế từ danh sách an toàn
            - Nếu bắt buộc phải dùng, cần desensitization dưới sự giám sát chuyên khoa
            """)
        elif result["severity"] == "high_risk":
            st.warning("""
            **THẬN TRỌNG:**
            - Nguy cơ phản ứng chéo cao
            - Ưu tiên chọn thuốc thay thế an toàn hơn
            - Nếu phải dùng: test da trước, có sẵn epinephrine, monitor sát
            """)
        elif result["severity"] == "moderate_risk":
            st.info("""
            **CẦN ĐÁNH GIÁ:**
            - Nguy cơ trung bình
            - Có thể cân nhắc dùng nếu không có lựa chọn khác
            - Monitor sát các dấu hiệu dị ứng
            """)
        else:
            st.success("""
            **AN TOÀN:**
            - Nguy cơ phản ứng chéo thấp
            - Có thể sử dụng với sự theo dõi thông thường
            - Vẫn cần monitor các dấu hiệu dị ứng
            """)
    
    # Information section
    with st.expander("📚 Thông tin về Phản ứng Chéo Beta-Lactam", expanded=False):
        st.markdown("""
        **Cơ chế phản ứng chéo:**
        - Beta-lactam có cấu trúc vòng beta-lactam chung
        - Phản ứng dị ứng phụ thuộc vào:
          - Cấu trúc vòng beta-lactam (chung cho tất cả)
          - Cấu trúc side chain (khác nhau giữa các thuốc)
        
        **Nguy cơ phản ứng chéo:**
        - **Rất cao (>90%):** Cùng phân tử (ví dụ: Penicillin G và Penicillin V)
        - **Cao (5-10%):** Cùng nhóm (ví dụ: Penicillin và Ampicillin)
        - **Thấp (1-2%):** Khác nhóm (ví dụ: Penicillin và Cephalosporin)
        - **Rất thấp (<0.5%):** Monobactam (Aztreonam) - không có phản ứng chéo
        
        **Nguồn tham khảo:**
        - IDSA Clinical Practice Guidelines
        - ASHP Guidelines
        - Campagna JD, et al. Cross-reactivity between penicillins and cephalosporins. J Allergy Clin Immunol. 2019
        """)
