"""
Clinical Case Studies
Real-world clinical scenarios for learning
"""

import streamlit as st
from typing import List, Dict, Optional

# Case studies database
CASE_STUDIES = [
    {
        "id": 1,
        "title": "CAP ở Bệnh nhân Cao tuổi",
        "category": "Pneumonia",
        "difficulty": "Intermediate",
        "case": """
        **Bệnh nhân:** Nam, 75 tuổi
        
        **Bệnh sử:**
        - Ho, sốt 39°C, khó thở 3 ngày
        - Đau ngực bên trái
        - Tiền sử: COPD, ĐTĐ type 2
        
        **Khám lâm sàng:**
        - T: 39.2°C, BP: 130/80, HR: 110, RR: 24, SpO2: 92% room air
        - Ran nổ bên trái dưới
        - XQ ngực: Đông đặc thùy dưới trái
        
        **Xét nghiệm:**
        - WBC: 15,000/μL (neutrophils 85%)
        - Cr: 1.2 mg/dL, eGFR: 55 mL/min/1.73m²
        - Cấy đờm: Đang chờ kết quả
        
        **Câu hỏi:** Chọn phác đồ kháng sinh phù hợp?
        """,
        "options": [
            "Amoxicillin 1g PO TID",
            "Ceftriaxone 2g IV q24h + Azithromycin 500mg IV q24h",
            "Piperacillin-Tazobactam 4.5g IV q6h + Vancomycin",
            "Levofloxacin 750mg PO q24h"
        ],
        "correct": 1,
        "explanation": """
        **Đáp án đúng: Ceftriaxone + Azithromycin**
        
        **Lý do:**
        - CAP nặng (sốt cao, khó thở, XQ đông đặc) → cần IV
        - Bệnh nhân cao tuổi, có COPD → nguy cơ cao
        - Ceftriaxone: Covers S. pneumoniae, H. influenzae
        - Azithromycin: Covers atypical (Mycoplasma, Chlamydia, Legionella)
        - eGFR 55 → không cần điều chỉnh liều Ceftriaxone
        
        **Các lựa chọn khác:**
        - Amoxicillin PO: Không đủ cho CAP nặng
        - Piperacillin-Tazobactam + Vancomycin: Quá rộng, không cần MRSA coverage
        - Levofloxacin đơn độc: Có thể dùng nhưng không phải lựa chọn đầu tay
        """,
        "learning_points": [
            "CAP nặng cần IV antibiotics",
            "Dual therapy (beta-lactam + macrolide) cho CAP",
            "Cân nhắc điều chỉnh liều theo eGFR",
            "De-escalate sau 48-72h khi có kết quả cấy"
        ]
    },
    {
        "id": 2,
        "title": "UTI Complicated với Suy thận",
        "category": "UTI",
        "difficulty": "Advanced",
        "case": """
        **Bệnh nhân:** Nữ, 68 tuổi
        
        **Bệnh sử:**
        - Sốt, ớn lạnh, đau hông lưng 2 ngày
        - Tiểu buốt, tiểu máu
        - Tiền sử: ĐTĐ, CKD stage 3
        
        **Khám lâm sàng:**
        - T: 38.5°C, BP: 140/90
        - Đau điểm góc sườn thắt lưng (P)
        - Không có dấu hiệu sốc
        
        **Xét nghiệm:**
        - Urine: WBC >100/HPF, nitrite (+), bacteria (+)
        - Cấy nước tiểu: E. coli >10⁵ CFU/mL (đang chờ AST)
        - Cr: 2.1 mg/dL, eGFR: 28 mL/min/1.73m²
        - HbA1c: 8.5%
        
        **Câu hỏi:** Chọn kháng sinh và liều phù hợp?
        """,
        "options": [
            "Ceftriaxone 2g IV q24h (không đổi liều)",
            "Ceftriaxone 2g IV q24h (giảm liều)",
            "Ciprofloxacin 400mg IV q12h",
            "Piperacillin-Tazobactam 4.5g IV q6h"
        ],
        "correct": 0,
        "explanation": """
        **Đáp án đúng: Ceftriaxone 2g IV q24h (không đổi liều)**
        
        **Lý do:**
        - UTI complicated (sốt, đau hông lưng) → cần IV
        - E. coli là tác nhân phổ biến nhất
        - Ceftriaxone thải chủ yếu qua gan (60%) → không cần giảm liều khi eGFR 28
        - Liều chuẩn 2g q24h vẫn an toàn
        
        **Các lựa chọn khác:**
        - Giảm liều Ceftriaxone: Không cần vì thải qua gan
        - Ciprofloxacin: Có thể dùng nhưng kháng thuốc cao tại VN (50-60%)
        - Piperacillin-Tazobactam: Quá rộng cho UTI đơn giản, cần điều chỉnh liều khi eGFR < 30
        """,
        "learning_points": [
            "Ceftriaxone không cần điều chỉnh liều khi suy thận (thải qua gan)",
            "UTI complicated cần IV antibiotics",
            "Cân nhắc kháng thuốc tại địa phương",
            "Theo dõi đáp ứng và de-escalate khi có kết quả AST"
        ]
    },
    {
        "id": 3,
        "title": "Sepsis với Sốc nhiễm khuẩn",
        "category": "Sepsis",
        "difficulty": "Advanced",
        "case": """
        **Bệnh nhân:** Nam, 55 tuổi
        
        **Bệnh sử:**
        - Sốt cao, ớn lạnh, lơ mơ 12 giờ
        - Tiền sử: Không có
        
        **Khám lâm sàng:**
        - T: 39.8°C, BP: 85/50 (sốc), HR: 130, RR: 28
        - SpO2: 88% room air → cần O2
        - Da lạnh, ẩm, CRT >3 giây
        - Không rõ nguồn nhiễm trùng
        
        **Xét nghiệm:**
        - WBC: 22,000/μL, Platelets: 80,000/μL
        - Lactate: 4.5 mmol/L
        - Cr: 1.0 mg/dL, Albumin: 2.8 g/dL
        - Cấy máu: Đang chờ (đã lấy trước khi dùng kháng sinh)
        
        **Câu hỏi:** Chọn phác đồ kháng sinh empiric?
        """,
        "options": [
            "Ceftriaxone 2g IV q24h",
            "Piperacillin-Tazobactam 4.5g IV q6h + Vancomycin 15-20 mg/kg IV q12h",
            "Meropenem 2g IV q8h",
            "Levofloxacin 750mg IV q24h"
        ],
        "correct": 1,
        "explanation": """
        **Đáp án đúng: Piperacillin-Tazobactam + Vancomycin**
        
        **Lý do:**
        - Sepsis với sốc → cần kháng sinh phổ rộng NGAY
        - Nguồn nhiễm trùng không rõ → cần coverage rộng
        - Piperacillin-Tazobactam: Covers Gram-negative, anaerobes, Pseudomonas
        - Vancomycin: Covers MRSA, Gram-positive
        - Albumin thấp (2.8) → có thể cần tăng liều (nhưng ưu tiên bắt đầu điều trị)
        
        **Các lựa chọn khác:**
        - Ceftriaxone đơn độc: Không đủ phổ, không cover MRSA/Pseudomonas
        - Meropenem: Có thể dùng nhưng không cover MRSA
        - Levofloxacin: Không đủ phổ, không phải lựa chọn đầu tay cho sepsis
        
        **Lưu ý:**
        - Bắt đầu kháng sinh trong vòng 1 giờ
        - De-escalate sau 48-72h khi có kết quả cấy
        - Monitor đáp ứng lâm sàng
        """,
        "learning_points": [
            "Sepsis cần kháng sinh phổ rộng ngay lập tức",
            "Empiric therapy: Beta-lactam + Vancomycin cho sepsis không rõ nguồn",
            "De-escalate sau 48-72h",
            "Theo dõi đáp ứng và điều chỉnh"
        ]
    },
]


def get_case_studies(category: Optional[str] = None, difficulty: Optional[str] = None) -> List[Dict]:
    """Get case studies, optionally filtered"""
    cases = CASE_STUDIES.copy()
    
    if category:
        cases = [c for c in cases if c["category"].lower() == category.lower()]
    
    if difficulty:
        cases = [c for c in cases if c["difficulty"].lower() == difficulty.lower()]
    
    return cases


def render_case_studies():
    """Render Case Studies UI"""
    
    st.markdown("### 📚 Tình Huống Lâm Sàng (Case Studies)")
    st.caption("Học từ các tình huống lâm sàng thực tế về sử dụng kháng sinh")
    
    # Filter options
    col1, col2 = st.columns(2)
    
    with col1:
        categories = sorted(list(set([c["category"] for c in CASE_STUDIES])))
        selected_category = st.selectbox(
            "Chọn chủ đề:",
            options=["Tất cả"] + categories,
            key="case_category"
        )
    
    with col2:
        difficulties = sorted(list(set([c["difficulty"] for c in CASE_STUDIES])))
        selected_difficulty = st.selectbox(
            "Độ khó:",
            options=["Tất cả"] + difficulties,
            key="case_difficulty"
        )
    
    # Get filtered cases
    category = None if selected_category == "Tất cả" else selected_category
    difficulty = None if selected_difficulty == "Tất cả" else selected_difficulty
    cases = get_case_studies(category, difficulty)
    
    if not cases:
        st.info("Không có case study nào phù hợp")
        return
    
    # Display cases
    for case in cases:
        with st.expander(f"📋 {case['title']} ({case['category']} - {case['difficulty']})", expanded=False):
            st.markdown("#### 📖 Tình huống")
            st.markdown(case["case"])
            
            st.markdown("---")
            st.markdown("#### ❓ Câu hỏi")
            st.markdown("Chọn đáp án đúng:")
            
            # Answer options
            selected_answer = st.radio(
                "Chọn đáp án:",
                options=case["options"],
                key=f"case_answer_{case['id']}",
                label_visibility="collapsed"
            )
            
            # Show answer button
            if st.button(f"✅ Xem đáp án", key=f"show_answer_{case['id']}"):
                st.markdown("---")
                st.markdown("#### ✅ Đáp án và Giải thích")
                
                # Highlight correct answer
                correct_option = case["options"][case["correct"]]
                user_selected = selected_answer
                is_correct = user_selected == correct_option
                
                if is_correct:
                    st.success(f"🎉 Đúng! Đáp án: {correct_option}")
                else:
                    st.error(f"❌ Sai. Đáp án đúng: {correct_option}")
                    st.info(f"Bạn chọn: {user_selected}")
                
                st.markdown(case["explanation"])
                
                # Learning points
                st.markdown("---")
                st.markdown("#### 📚 Điểm Học Tập")
                for point in case["learning_points"]:
                    st.markdown(f"- {point}")
            
            st.markdown("---")
