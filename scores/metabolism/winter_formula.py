"""
Winter Formula - Expected PCO2 in Metabolic Acidosis
Công thức Winter - PCO2 dự đoán trong toan chuyển hóa
"""

import streamlit as st


def calculate_expected_pco2(hco3):
    """
    Calculate expected PCO2 using Winter's Formula
    Expected PCO2 = 1.5 × [HCO3] + 8 (± 2)
    
    Args:
        hco3: Serum bicarbonate in mmol/L or mEq/L
    
    Returns:
        tuple: (expected_pco2, lower_limit, upper_limit)
    """
    expected_pco2 = 1.5 * hco3 + 8
    lower_limit = expected_pco2 - 2
    upper_limit = expected_pco2 + 2
    
    return expected_pco2, lower_limit, upper_limit


def interpret_compensation(actual_pco2, expected_pco2, lower_limit, upper_limit):
    """
    Interpret respiratory compensation status
    
    Args:
        actual_pco2: Actual measured PCO2
        expected_pco2: Expected PCO2 from Winter's formula
        lower_limit: Lower limit of expected range
        upper_limit: Upper limit of expected range
    
    Returns:
        dict: Interpretation results
    """
    if lower_limit <= actual_pco2 <= upper_limit:
        return {
            "status": "Bù thường thích hợp",
            "color": "🟢",
            "interpretation": "Bù thường hô hấp đầy đủ cho toan chuyển hóa",
            "clinical": "Chỉ có rối loạn acid-base đơn thuần (Toan chuyển hóa)",
            "action": "Điều trị nguyên nhân gây toan chuyển hóa"
        }
    elif actual_pco2 < lower_limit:
        deviation = lower_limit - actual_pco2
        return {
            "status": "Bù thường quá mức",
            "color": "🔵",
            "interpretation": f"PCO2 thấp hơn dự đoán {deviation:.1f} mmHg",
            "clinical": "Rối loạn acid-base hỗn hợp: Toan chuyển hóa + Kiềm hô hấp",
            "action": "Tìm nguyên nhân tăng thông khí (lo âu, đau, nhiễm trùng phổi, v.v.)"
        }
    else:  # actual_pco2 > upper_limit
        deviation = actual_pco2 - upper_limit
        return {
            "status": "Bù thường không đầy đủ",
            "color": "🟠",
            "interpretation": f"PCO2 cao hơn dự đoán {deviation:.1f} mmHg",
            "clinical": "Rối loạn acid-base hỗn hợp: Toan chuyển hóa + Toan hô hấp",
            "action": "Đánh giá chức năng hô hấp, xem xét hỗ trợ thông khí"
        }


def get_metabolic_acidosis_causes(anion_gap):
    """
    Get common causes based on anion gap
    
    Args:
        anion_gap: Calculated anion gap
    
    Returns:
        dict: Causes categorized by anion gap
    """
    if anion_gap > 12:
        return {
            "type": "Toan chuyển hóa Anion Gap cao",
            "mnemonic": "MUDPILES / GOLDMARK",
            "causes": [
                "**M**ethanol",
                "**U**remia (suy thận)",
                "**D**KA (nhiễm toan do đái tháo đường)",
                "**P**araldehyde / **P**ropylene glycol",
                "**I**soniazid / **I**ron",
                "**L**actic acidosis (nhiễm toan lactic)",
                "**E**thylene glycol",
                "**S**alicylates (aspirin)"
            ]
        }
    else:
        return {
            "type": "Toan chuyển hóa Anion Gap bình thường",
            "mnemonic": "HARDUPS",
            "causes": [
                "**H**yperalimentation",
                "**A**cetazolamide / **A**ddison's disease",
                "**R**TA (Renal Tubular Acidosis)",
                "**D**iarrhea (tiêu chảy)",
                "**U**reteral diversions",
                "**P**ancreatic fistula",
                "**S**aline excess"
            ]
        }


def render():
    """Render the Winter Formula calculator"""
    
    st.title("🧪 Winter Formula")
    st.markdown("""
    ### PCO2 Dự Đoán trong Toan Chuyển Hóa
    
    **Winter's Formula:**
    - Dự đoán mức PCO2 bù thường thích hợp trong toan chuyển hóa
    - Giúp nhận diện rối loạn acid-base hỗn hợp
    - **Expected PCO2 = 1.5 × [HCO₃⁻] + 8 (± 2)**
    
    **Ý nghĩa lâm sàng:**
    - Nếu PCO2 thực tế = PCO2 dự đoán → Bù thường thích hợp (rối loạn đơn thuần)
    - Nếu PCO2 < PCO2 dự đoán → Bù thường quá mức (thêm kiềm hô hấp)
    - Nếu PCO2 > PCO2 dự đoán → Bù thường không đủ (thêm toan hô hấp)
    
    **Lưu ý:** Chỉ áp dụng cho toan chuyển hóa (HCO₃⁻ < 22 mmol/L)
    """)
    
    st.markdown("---")
    
    # Input section
    st.subheader("📊 Nhập thông số khí máu động mạch")
    
    col1, col2 = st.columns(2)
    
    with col1:
        ph = st.number_input(
            "**pH**",
            min_value=6.8,
            max_value=7.8,
            value=7.25,
            step=0.01,
            format="%.2f",
            help="pH máu động mạch (bình thường: 7.35-7.45)"
        )
        
        hco3 = st.number_input(
            "**HCO₃⁻ (mmol/L)**",
            min_value=1.0,
            max_value=50.0,
            value=12.0,
            step=0.5,
            format="%.1f",
            help="Bicarbonate (bình thường: 22-28 mmol/L)"
        )
    
    with col2:
        actual_pco2 = st.number_input(
            "**PCO₂ thực tế (mmHg)**",
            min_value=10.0,
            max_value=100.0,
            value=28.0,
            step=0.5,
            format="%.1f",
            help="PCO2 đo được từ khí máu (bình thường: 35-45 mmHg)"
        )
        
        # Optional anion gap for additional interpretation
        calculate_ag = st.checkbox("Có giá trị Anion Gap?")
        
        if calculate_ag:
            anion_gap = st.number_input(
                "**Anion Gap (mmol/L)**",
                min_value=0.0,
                max_value=50.0,
                value=20.0,
                step=1.0,
                help="AG = Na - (Cl + HCO3) (bình thường: 8-12)"
            )
        else:
            anion_gap = None
    
    # Check if it's metabolic acidosis
    if hco3 >= 22:
        st.warning("⚠️ **Lưu ý:** Winter's Formula chỉ áp dụng cho toan chuyển hóa (HCO₃⁻ < 22 mmol/L)")
    
    if st.button("🔬 Tính Toán & Phân tích", type="primary", use_container_width=True):
        # Calculate expected PCO2
        expected_pco2, lower_limit, upper_limit = calculate_expected_pco2(hco3)
        
        # Interpret compensation
        result = interpret_compensation(actual_pco2, expected_pco2, lower_limit, upper_limit)
        
        st.markdown("---")
        st.subheader("📈 Kết quả Phân tích")
        
        # Display ABG values
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                "pH",
                f"{ph:.2f}",
                delta="Toan" if ph < 7.35 else "Kiềm" if ph > 7.45 else "Bình thường",
                delta_color="inverse"
            )
        
        with col2:
            st.metric(
                "HCO₃⁻",
                f"{hco3:.1f} mmol/L",
                delta="Thấp" if hco3 < 22 else "Cao" if hco3 > 28 else "Bình thường",
                delta_color="inverse"
            )
        
        with col3:
            st.metric(
                "PCO₂ thực tế",
                f"{actual_pco2:.1f} mmHg",
                delta="Thấp" if actual_pco2 < 35 else "Cao" if actual_pco2 > 45 else "Bình thường",
                delta_color="inverse"
            )
        
        st.markdown("---")
        
        # Winter's Formula Results
        st.subheader("🔬 Winter's Formula - PCO₂ Dự Đoán")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.info(f"""
            **Công thức:**  
            PCO₂ dự đoán = 1.5 × [{hco3:.1f}] + 8 (± 2)
            
            **Kết quả:**
            - PCO₂ dự đoán: **{expected_pco2:.1f} mmHg**
            - Khoảng chấp nhận: **{lower_limit:.1f} - {upper_limit:.1f} mmHg**
            - PCO₂ thực tế: **{actual_pco2:.1f} mmHg**
            """)
        
        with col2:
            # Compensation status
            st.success(f"""
            {result['color']} **{result['status']}**
            
            **Giải thích:**  
            {result['interpretation']}
            """)
        
        st.markdown("---")
        
        # Clinical interpretation
        st.subheader("🎯 Phân tích Lâm Sàng")
        
        if result['color'] == "🟢":
            st.success(f"""
            ✅ **{result['clinical']}**
            
            Bệnh nhân có toan chuyển hóa đơn thuần với bù thường hô hấp thích hợp.
            
            **Khuyến nghị:**
            - {result['action']}
            - Xác định và điều trị nguyên nhân toan chuyển hóa
            - Theo dõi điện giải đồ và chức năng thận
            """)
        else:
            st.warning(f"""
            ⚠️ **{result['clinical']}**
            
            Bệnh nhân có rối loạn acid-base hỗn hợp cần đánh giá kỹ hơn.
            
            **Khuyến nghị:**
            - {result['action']}
            - Xem xét các nguyên nhân gây rối loạn acid-base đồng thời
            - Cân nhắc hội chẩn chuyên khoa
            """)
        
        # Causes based on anion gap
        if anion_gap is not None:
            st.markdown("---")
            st.subheader("🔍 Nguyên Nhân Toan Chuyển Hóa")
            
            causes_info = get_metabolic_acidosis_causes(anion_gap)
            
            st.info(f"""
            **Anion Gap = {anion_gap:.1f} mmol/L**
            
            **Loại:** {causes_info['type']}
            
            **Gợi nhớ ({causes_info['mnemonic']}):**
            """)
            
            for cause in causes_info['causes']:
                st.markdown(f"- {cause}")
    
    # Educational content
    st.markdown("---")
    st.subheader("📚 Kiến Thức Bổ Sung")
    
    with st.expander("🎯 Cơ Chế Bù Thường"):
        st.markdown("""
        ### Bù thường hô hấp trong toan chuyển hóa:
        
        **1. Cơ chế:**
        - HCO₃⁻ giảm → pH giảm
        - Kích thích trung tâm hô hấp
        - Tăng thông khí → Thải CO₂
        - PCO₂ giảm → pH tăng trở lại
        
        **2. Thời gian:**
        - Bắt đầu: Ngay lập tức (phút)
        - Tối đa: 12-24 giờ
        - Hoàn tất: 2-3 ngày
        
        **3. Giới hạn:**
        - PCO₂ thấp nhất có thể: ~10-12 mmHg
        - Không bao giờ bù thường hoàn toàn (pH không về 7.40)
        - Nếu pH bình thường → Có thêm rối loạn kiềm
        
        **4. Ý nghĩa Winter's Formula:**
        - Dự đoán PCO₂ "mục tiêu" khi bù thường đầy đủ
        - Phát hiện rối loạn acid-base hỗn hợp
        - Hướng dẫn điều trị thích hợp
        """)
    
    with st.expander("📊 Cách đánh giá khí máu động mạch"):
        st.markdown("""
        ### Tiếp cận có hệ thống:
        
        **Bước 1: Đánh giá pH**
        - pH < 7.35 → Toan
        - pH > 7.45 → Kiềm
        - pH 7.35-7.45 → Bình thường (hoặc bù thường hoàn toàn)
        
        **Bước 2: Xác định rối loạn chính**
        - Toan + HCO₃⁻ thấp → Toan chuyển hóa
        - Toan + PCO₂ cao → Toan hô hấp
        - Kiềm + HCO₃⁻ cao → Kiềm chuyển hóa
        - Kiềm + PCO₂ thấp → Kiềm hô hấp
        
        **Bước 3: Đánh giá bù thường**
        - Toan chuyển hóa → Dùng Winter's Formula
        - Kiềm chuyển hóa → PCO₂ tăng 0.7 mmHg/1 mmol/L HCO₃⁻
        - Toan hô hấp:
          + Cấp: HCO₃⁻ tăng 1 mmol/L mỗi 10 mmHg PCO₂
          + Mạn: HCO₃⁻ tăng 4 mmol/L mỗi 10 mmHg PCO₂
        - Kiềm hô hấp:
          + Cấp: HCO₃⁻ giảm 2 mmol/L mỗi 10 mmHg PCO₂
          + Mạn: HCO₃⁻ giảm 5 mmol/L mỗi 10 mmHg PCO₂
        
        **Bước 4: Tính Anion Gap**
        - AG = Na⁺ - (Cl⁻ + HCO₃⁻)
        - Bình thường: 8-12 mmol/L
        - Phân loại nguyên nhân toan chuyển hóa
        
        **Bước 5: Delta Ratio (nếu AG cao)**
        - Δ Ratio = (AG - 12) / (24 - HCO₃⁻)
        - Ratio 1-2: Toan chuyển hóa AG cao đơn thuần
        - Ratio < 1: Thêm toan AG bình thường
        - Ratio > 2: Thêm kiềm chuyển hóa
        """)
    
    with st.expander("⚠️ Rối Loạn Acid-Base Hỗn Hợp"):
        st.markdown("""
        ### Các tình huống thường gặp:
        
        **1. Toan chuyển hóa + Toan hô hấp:**
        - Ngừng tim, sốc nặng
        - PCO₂ cao hơn dự đoán theo Winter
        - pH rất thấp, tiên lượng xấu
        
        **2. Toan chuyển hóa + Kiềm hô hấp:**
        - Nhiễm trùng huyết + suy gan
        - Ngộ độc salicylate
        - PCO₂ thấp hơn dự đoán theo Winter
        - pH có thể gần bình thường
        
        **3. Toan chuyển hóa + Kiềm chuyển hóa:**
        - Suy thận + nôn nhiều
        - DKA + thuốc lợi tiểu
        - AG cao nhưng HCO₃⁻ gần bình thường
        - Dùng Delta Ratio để phát hiện
        
        **4. Triple disorder:**
        - DKA + nôn + ngộ độc aspirin
        - Suy tim + suy gan + suy thận
        - Rất phức tạp, cần hội chẩn
        """)
    
    with st.expander("🔢 Công Thức Khác Liên Quan"):
        st.markdown("""
        ### Các công thức bù thường khác:
        
        **1. Kiềm chuyển hóa:**
        ```
        Expected PCO₂ = 0.7 × (HCO₃⁻ - 24) + 40
        Hoặc: PCO₂ tăng 0.7 mmHg/1 mmol/L HCO₃⁻
        ```
        
        **2. Toan hô hấp:**
        ```
        Cấp: HCO₃⁻ tăng 1 mmol/L mỗi 10 mmHg PCO₂
        Mạn: HCO₃⁻ tăng 4 mmol/L mỗi 10 mmHg PCO₂
        ```
        
        **3. Kiềm hô hấp:**
        ```
        Cấp: HCO₃⁻ giảm 2 mmol/L mỗi 10 mmHg PCO₂
        Mạn: HCO₃⁻ giảm 5 mmol/L mỗi 10 mmHg PCO₂
        ```
        
        **4. Anion Gap điều chỉnh theo Albumin:**
        ```
        AG corrected = AG measured + 2.5 × (4.0 - Albumin)
        ```
        
        **5. Delta Ratio:**
        ```
        Δ Ratio = (AG - 12) / (24 - HCO₃⁻)
        ```
        """)
    
    # References
    st.markdown("---")
    st.caption("""
    **Tài liệu tham khảo:**
    - Winter SD. A simple formula for the base excess of blood. J Appl Physiol. 1971
    - Albert MS, et al. Quantitative displacement of acid-base equilibrium. Ann Intern Med. 1967
    - Berend K, et al. Physiological approach to assessment of acid-base disturbances. NEJM. 2014
    - Rose BD, Post TW. Clinical Physiology of Acid-Base and Electrolyte Disorders. 5th ed. 2001
    """)


if __name__ == "__main__":
    render()

