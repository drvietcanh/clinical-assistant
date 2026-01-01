"""
Free T4 Index (FTI) Calculator
Chỉ số T4 tự do - ước tính T4 tự do từ T4 toàn phần và T3 uptake
"""

import streamlit as st
from scores.utils.validation import (
    validate_range,
    validate_lab_value
)
from components.ui.validation import render_validation_errors
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section
# =====================================


def _format_num(value: float, decimals: int = 1) -> str:
    """Format số, loại bỏ số 0 thừa"""
    rounded = round(value, decimals)
    if rounded == int(rounded):
        return str(int(rounded))
    return f"{rounded:.{decimals}f}".rstrip('0').rstrip('.')


def calculate_fti(total_t4, t3_uptake):
    """
    Tính Free T4 Index
    
    FTI = Total T4 × (T3 uptake / 100)
    
    Parameters:
    - total_t4: T4 toàn phần (µg/dL)
    - t3_uptake: T3 uptake (%)
    
    Returns:
    - dict với fti, interpretation
    """
    fti = total_t4 * (t3_uptake / 100)
    
    # Phân loại
    if fti < 1.0:
        status = "Suy giáp (Hypothyroidism)"
        interpretation = "FTI thấp → Giảm hormone giáp"
        color = "blue"
        recommendation = "Xem xét suy giáp, cần TSH để xác nhận"
    elif fti <= 4.0:
        status = "Bình thường (Euthyroid)"
        interpretation = "FTI trong giới hạn bình thường"
        color = "green"
        recommendation = "Chức năng giáp bình thường"
    else:
        status = "Cường giáp (Hyperthyroidism)"
        interpretation = "FTI cao → Tăng hormone giáp"
        color = "red"
        recommendation = "Xem xét cường giáp, cần TSH và xét nghiệm bổ sung"
    
    return {
        "fti": fti,
        "status": status,
        "interpretation": interpretation,
        "color": color,
        "recommendation": recommendation
    }


def render():
    """Render Free T4 Index calculator interface"""
    
    st.markdown("""
    <h2 style='text-align: center; color: #8B5CF6;'>🦋 Free T4 Index (FTI)</h2>
    <p style='text-align: center;'><em>Chỉ số T4 tự do - Ước tính T4 tự do</em></p>
    """, unsafe_allow_html=True)
    shared = load_shared_result_from_url()
    if shared and shared.get("calculator_id") == "free_t4_index":
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared.get('calculator_name', 'Free T4 Index')}")
    
    # Thông tin về FTI
    with st.expander("ℹ️ Giới thiệu về Free T4 Index"):
        st.markdown("""
        **Free T4 Index (FTI)** là phương pháp tính toán để ước tính nồng độ T4 tự do 
        từ T4 toàn phần và T3 resin uptake (T3RU).
        
        **Nguyên lý:**
        - T4 toàn phần = T4 tự do + T4 gắn protein
        - Khi protein gắn hormone thay đổi → T4 toàn phần thay đổi nhưng T4 tự do có thể bình thường
        - FTI điều chỉnh cho sự thay đổi protein gắn hormone
        
        **Mục đích:**
        - Ước tính T4 tự do khi không có xét nghiệm Free T4 trực tiếp
        - Loại trừ ảnh hưởng của thay đổi protein gắn hormone
        - Hữu ích khi có thay đổi TBG (Thyroxine Binding Globulin)
        
        **Khi nào sử dụng:**
        - Thai kỳ (TBG tăng)
        - Dùng estrogen, thuốc tránh thai
        - Bệnh gan (thay đổi protein)
        - Khi nghi ngờ rối loạn protein gắn hormone
        
        **Giới hạn:**
        - Hiện nay đo Free T4 trực tiếp chính xác hơn và phổ biến hơn
        - FTI chỉ là ước tính, không chính xác bằng Free T4
        - Ít được sử dụng trong thực hành hiện đại
        
        **Lưu ý:**
        - FTI là xét nghiệm cũ, hiện nay đo Free T4 trực tiếp
        - Vẫn hữu ích khi không có Free T4
        - Luôn kết hợp với TSH để đánh giá đầy đủ
        """)
    
    st.markdown("---")
    
    # Input form
    st.subheader("📝 Nhập kết quả xét nghiệm")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 1️⃣ Total T4 (T4 toàn phần)")
        
        total_t4_unit = st.radio(
            "Chọn đơn vị:",
            options=["µg/dL", "nmol/L"],
            horizontal=True,
            help="Đơn vị phổ biến nhất là µg/dL"
        )
        
        if total_t4_unit == "µg/dL":
            total_t4_ugdl = st.number_input(
                "Total T4 (µg/dL)",
                min_value=0.0,
                max_value=30.0,
                value=8.0,
                step=0.1,
                help="Bình thường: 5-12 µg/dL"
            )
            total_t4 = total_t4_ugdl
            st.info(f"💡 Giá trị bình thường: **5-12 µg/dL**")
        else:
            total_t4_nmol = st.number_input(
                "Total T4 (nmol/L)",
                min_value=0.0,
                max_value=400.0,
                value=100.0,
                step=1.0,
                help="Bình thường: 64-154 nmol/L"
            )
            # Convert nmol/L to µg/dL (1 nmol/L = 0.0777 µg/dL)
            total_t4 = total_t4_nmol * 0.0777
            st.info(f"💡 Giá trị bình thường: **64-154 nmol/L**")
            st.caption(f"= {_format_num(total_t4, 1)} µg/dL")
    
    with col2:
        st.markdown("### 2️⃣ T3 Resin Uptake (T3RU)")
        
        t3_uptake = st.number_input(
            "T3 Uptake (%)",
            min_value=0.0,
            max_value=100.0,
            value=30.0,
            step=0.5,
            help="Bình thường: 25-35% (tùy lab)"
        )
        
        st.info("""
        💡 **T3 Resin Uptake:**
        - Bình thường: **25-35%** (có thể khác tùy lab)
        - Đo gián tiếp khả năng gắn hormone của protein
        - **T3RU cao** → Ít TBG hoặc nhiều T4 tự do
        - **T3RU thấp** → Nhiều TBG hoặc ít T4 tự do
        """)
        
        # Normal range input
        with st.expander("⚙️ Tùy chỉnh giá trị bình thường của Lab"):
            st.caption("Mỗi phòng lab có thể có khoảng tham chiếu khác nhau")
            
            col_t3a, col_t3b = st.columns(2)
            with col_t3a:
                t3_normal_min = st.number_input(
                    "T3RU min (%)",
                    value=25.0,
                    step=1.0
                )
            with col_t3b:
                t3_normal_max = st.number_input(
                    "T3RU max (%)",
                    value=35.0,
                    step=1.0
                )
            
            if t3_normal_min <= t3_uptake <= t3_normal_max:
                st.success(f"✅ T3RU trong khoảng bình thường ({t3_normal_min}-{t3_normal_max}%)")
            elif t3_uptake < t3_normal_min:
                st.warning(f"⬇️ T3RU thấp (< {t3_normal_min}%)")
            else:
                st.warning(f"⬆️ T3RU cao (> {t3_normal_max}%)")
    
    st.markdown("---")
    
    # Optional TSH for complete assessment
    with st.expander("🔬 Nhập TSH để đánh giá toàn diện (tùy chọn)"):
        include_tsh = st.checkbox("Tôi có kết quả TSH", value=False)
        
        if include_tsh:
            tsh_unit = st.radio(
                "Đơn vị TSH:",
                options=["mIU/L", "µIU/mL"],
                horizontal=True,
                help="mIU/L = µIU/mL"
            )
            
            tsh_value = st.number_input(
                f"TSH ({tsh_unit})",
                min_value=0.0,
                max_value=100.0,
                value=2.5,
                step=0.1,
                help="Bình thường: 0.4-4.0 mIU/L"
            )
            
            if 0.4 <= tsh_value <= 4.0:
                tsh_status = "Bình thường"
                tsh_color = "green"
            elif tsh_value < 0.4:
                tsh_status = "Thấp (nghi ngờ cường giáp)"
                tsh_color = "red"
            else:
                tsh_status = "Cao (nghi ngờ suy giáp)"
                tsh_color = "blue"
            
            st.info(f"💡 TSH: {tsh_value} {tsh_unit} - **{tsh_status}**")
    
    st.markdown("---")
    
    # Calculate button
    if st.button("🔬 Tính Free T4 Index", type="primary", use_container_width=True):
        # Validate inputs
        validation_errors = []
        
        # Total T4 validation (depends on unit)
        if total_t4_unit == "µg/dL":
            is_valid_t4, t4_error = validate_lab_value(total_t4_ugdl, "Total T4", 0.0, 30.0)
            if not is_valid_t4:
                validation_errors.append(f"Total T4 (µg/dL): {t4_error}")
        else:  # nmol/L
            is_valid_t4, t4_error = validate_lab_value(total_t4_nmol, "Total T4", 0.0, 400.0)
            if not is_valid_t4:
                validation_errors.append(f"Total T4 (nmol/L): {t4_error}")
        
        # T3 Uptake validation
        is_valid_t3, t3_error = validate_range(t3_uptake, 0.0, 100.0, "T3 Uptake")
        if not is_valid_t3:
            validation_errors.append(f"T3 Uptake: {t3_error}")
        
        # TSH validation (if provided)
        if include_tsh:
            is_valid_tsh, tsh_error = validate_lab_value(tsh_value, "TSH", 0.0, 100.0)
            if not is_valid_tsh:
                validation_errors.append(f"TSH: {tsh_error}")
        
        if validation_errors:
            render_validation_errors(validation_errors)
            return
        
        result = calculate_fti(total_t4, t3_uptake)
        
        # Display result
        st.markdown("## 📊 Kết quả")
        
        # FTI display
        score_color_map = {
            "green": COLORS["success"],
            "blue": COLORS["info"],
            "red": COLORS["error"]
        }
        score_color = score_color_map[result["color"]]
        
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {score_color}22 0%, {score_color}44 100%); 
                    padding: 30px; border-radius: 15px; border-left: 5px solid {score_color}; margin: 20px 0;'>
            <h2 style='color: {score_color}; margin: 0; text-align: center;'>
                Free T4 Index: {_format_num(result['fti'], 2)}
            </h2>
        </div>
        """, unsafe_allow_html=True)
        
        # Component breakdown
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("T4 toàn phần", f"{_format_num(total_t4, 1)} µg/dL")
        
        with col2:
            st.metric("T3 Uptake", f"{_format_num(t3_uptake, 1)}%")
        
        with col3:
            st.metric("FTI", _format_num(result['fti'], 2))
        
        st.markdown("---")
        
        inputs_dict = {
            "Total T4 (ug/dL)": round(total_t4, 2),
            "T3 Uptake (%)": t3_uptake,
            "TSH": tsh_value if include_tsh else None
        }
        results_dict = {
            "FTI": round(result["fti"], 2),
            "Status": result["status"]
        }
        
        # Export section
        render_export_section(
                title="Free T4 Index",
                inputs=inputs_dict,
                results=results_dict
        ,
                calculator_name="Free T4 Index"
            )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="free_t4_index",
            calculator_name="Free T4 Index",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="free_t4_index",
            calculator_name="Free T4 Index",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        render_suggestions(
            calculator_id="free_t4_index",
            calculator_name="Free T4 Index",
            category="Nội Tiết",
            show_related=True,
            show_category=True,
            limit=3
        )
        
        # History section
        st.markdown("---")
        render_history_ui(calculator_id="free_t4_index", show_actions=True)
        
        # Status
        st.markdown(f"""
        <div style='background-color: {score_color}22; padding: 20px; border-radius: 10px; border: 2px solid {score_color};'>
            <h3 style='color: {score_color}; margin-top: 0;'>🎯 Trạng thái: {result['status']}</h3>
            <p style='font-size: 1.1em; margin: 10px 0;'>{result['interpretation']}</p>
            <p style='font-size: 1.2em; color: {score_color}; font-weight: bold; margin: 10px 0;'>
                {result['recommendation']}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Integrated assessment with TSH
        if include_tsh:
            st.markdown("---")
            st.markdown("### 🔬 Đánh giá tổng hợp với TSH")
            
            # Combined interpretation
            if 1.0 <= result["fti"] <= 4.0 and 0.4 <= tsh_value <= 4.0:
                st.success(f"""
                ✅ **Chức năng giáp bình thường (Euthyroid)**
                - FTI: {_format_num(result['fti'], 2)} (bình thường)
                - TSH: {_format_num(tsh_value, 1)} {tsh_unit} (bình thường)
                - Không cần can thiệp
                """)
            
            elif result["fti"] > 4.0 and tsh_value < 0.4:
                st.error(f"""
                🔴 **Cường giáp (Hyperthyroidism)**
                - FTI: {_format_num(result['fti'], 2)} (cao)
                - TSH: {_format_num(tsh_value, 1)} {tsh_unit} (thấp)
                - Kết quả phù hợp với cường giáp
                
                **Cần làm thêm:**
                - Free T3
                - Kháng thể anti-TPO, anti-TG
                - Siêu âm giáp
                - Xét nghiệm TSH receptor antibody nếu nghi Graves
                """)
            
            elif result["fti"] < 1.0 and tsh_value > 4.0:
                st.info(f"""
                🔵 **Suy giáp (Hypothyroidism)**
                - FTI: {_format_num(result['fti'], 2)} (thấp)
                - TSH: {_format_num(tsh_value, 1)} {tsh_unit} (cao)
                - Kết quả phù hợp với suy giáp tiên phát
                
                **Cần làm thêm:**
                - Kháng thể anti-TPO (Hashimoto?)
                - Xét nghiệm lại sau 2-3 tháng nếu suy giáp cận lâm sàng
                - Xem xét điều trị levothyroxine
                """)
            
            else:
                st.warning(f"""
                ⚠️ **Kết quả không phù hợp / Cần đánh giá thêm**
                - FTI: {_format_num(result['fti'], 2)}
                - TSH: {_format_num(tsh_value, 1)} {tsh_unit}
                
                **Các khả năng:**
                1. Suy giáp cận lâm sàng (TSH cao, FTI bình thường)
                2. Cường giáp cận lâm sàng (TSH thấp, FTI bình thường)
                3. Bệnh không liên quan đến giáp (sick euthyroid syndrome)
                4. Rối loạn protein gắn hormone
                5. Thuốc ảnh hưởng (amiodarone, steroid, dopamine...)
                
                **Khuyến cáo:**
                - Đo Free T4 và Free T3 trực tiếp
                - Đánh giá lâm sàng kỹ
                - Xem xét lịch sử dùng thuốc
                - Xét nghiệm lại sau 4-6 tuần
                """)
        
        # Interpretation guide
        with st.expander("📊 Hướng dẫn giải thích kết quả"):
            st.markdown("""
            ### Free T4 Index (FTI)
            
            **Công thức:**
            ```
            FTI = Total T4 × (T3 Uptake / 100)
            ```
            
            **Khoảng tham chiếu:**
            - Bình thường: **1.0 - 4.0** (có thể thay đổi tùy lab)
            - Suy giáp: < 1.0
            - Cường giáp: > 4.0
            
            **Ý nghĩa:**
            
            | Total T4 | T3RU | FTI | Giải thích |
            |:---------|:-----|:----|:-----------|
            | ↑ | ↑ | ↑↑ | Cường giáp |
            | ↓ | ↓ | ↓↓ | Suy giáp |
            | ↑ | ↓ | Bình thường | TBG tăng (thai kỳ, estrogen) |
            | ↓ | ↑ | Bình thường | TBG giảm (nephrotic, gan) |
            
            **Nguyên tắc:**
            - FTI cùng chiều với T4 tự do thực sự
            - Điều chỉnh cho thay đổi protein gắn hormone
            - T3RU ngược chiều với TBG
            """)
        
        # Factors affecting results
        with st.expander("⚠️ Các yếu tố ảnh hưởng kết quả"):
            st.markdown("""
            ### Làm TBG tăng (↑ Total T4, ↓ T3RU, FTI bình thường):
            - **Thai kỳ**
            - Estrogen, thuốc tránh thai
            - Hepatitis cấp
            - Porphyria
            - Thuốc: Tamoxifen, Methadone, Heroin
            - Bệnh di truyền tăng TBG
            
            ### Làm TBG giảm (↓ Total T4, ↑ T3RU, FTI bình thường):
            - Hội chứng thận hư
            - Xơ gan, suy dinh dưỡng
            - Androgen, steroid đồng hóa
            - Glucocorticoid liều cao
            - Acromegaly
            - Bệnh nặng (sick euthyroid)
            
            ### Thuốc ảnh hưởng trực tiếp:
            - **Amiodarone:** Tăng T4, giảm T3
            - **Lithium:** Có thể gây suy giáp
            - **Interferon:** Rối loạn chức năng giáp
            - **Dopamine, Glucocorticoid:** Giảm TSH
            - **Biotin liều cao:** Làm sai kết quả xét nghiệm
            
            ### Bệnh không giáp (Non-thyroidal illness):
            - Bệnh cấp nặng
            - Phẫu thuật lớn
            - Nhịn đói kéo dài
            - → T4, T3 giảm nhưng không phải suy giáp
            - → Thường không cần điều trị hormone giáp
            """)
        
        # Modern approach
        with st.expander("🔬 Tiếp cận hiện đại"):
            st.markdown("""
            ### Xét nghiệm chức năng giáp hiện nay:
            
            **Sàng lọc ban đầu:**
            1. **TSH** - Xét nghiệm quan trọng nhất
               - Nhạy nhất với thay đổi chức năng giáp
               - Bình thường: 0.4-4.0 mIU/L
            
            **Khi TSH bất thường:**
            2. **Free T4** (T4 tự do)
               - Đo trực tiếp, chính xác hơn FTI
               - Không bị ảnh hưởng bởi protein gắn hormone
            
            3. **Free T3** (nếu cần)
               - Đặc biệt trong cường giáp T3
               - Theo dõi điều trị cường giáp
            
            **Xét nghiệm bổ sung:**
            - Anti-TPO, Anti-TG: Viêm giáp tự miễn (Hashimoto)
            - TSH receptor antibody: Graves' disease
            - Thyroglobulin: Theo dõi ung thư giáp
            
            **FTI còn được dùng khi:**
            - Không có Free T4
            - So sánh với kết quả cũ
            - Nghiên cứu lịch sử
            - Chi phí là vấn đề (ở một số nơi)
            
            **Xu hướng:**
            - FTI ngày càng ít dùng
            - Free T4, Free T3 trực tiếp là tiêu chuẩn
            - TSH vẫn là xét nghiệm sàng lọc tốt nhất
            """)
        
        # Clinical scenarios
        with st.expander("📋 Các tình huống lâm sàng"):
            st.markdown("""
            ### 1. Thai kỳ:
            - TBG tăng → T4 toàn phần tăng
            - Nhưng T4 tự do (FTI) bình thường
            - TSH: Có thể giảm nhẹ tam cá nguyệt 1 (bình thường)
            - **Lưu ý:** Khoảng tham chiếu TSH khác ở thai phụ
            
            ### 2. Dùng thuốc tránh thai/Estrogen:
            - Tương tự thai kỳ
            - TBG tăng → T4 toàn phần tăng
            - FTI và TSH bình thường → Không cần điều trị
            
            ### 3. Bệnh nhân ICU/Bệnh nặng:
            - Sick euthyroid syndrome
            - T4, T3 thấp, TSH bình thường hoặc hơi thấp
            - Cơ chế bảo vệ, không phải suy giáp
            - **Không** điều trị hormone giáp
            
            ### 4. Suy dinh dưỡng:
            - TBG giảm → T4 toàn phần thấp
            - FTI có thể bình thường
            - T3 thường thấp (chuyển hóa giảm)
            - Điều trị nguyên nhân, không phải hormone
            
            ### 5. Amiodarone:
            - Ức chế chuyển T4 → T3
            - T4 tăng, T3 giảm, rT3 tăng
            - TSH ban đầu tăng, sau đó bình thường
            - Theo dõi TSH 3-6 tháng/lần
            - Có thể gây cường hoặc suy giáp
            """)
        
        # References
        with st.expander("📚 Tài liệu tham khảo"):
            st.markdown("""
            1. **Ross DS.** Serum thyroid-stimulating hormone measurement for assessment of thyroid function and disease. 
               Endocrinol Metab Clin North Am. 2001;30(2):245-64.
            
            2. **Garber JR, Cobin RH, Gharib H, et al.** Clinical practice guidelines for hypothyroidism in adults: 
               cosponsored by the American Association of Clinical Endocrinologists and the American Thyroid Association. 
               Thyroid. 2012;22(12):1200-35.
            
            3. **Jonklaas J, Bianco AC, Bauer AJ, et al.** Guidelines for the treatment of hypothyroidism: 
               prepared by the american thyroid association task force on thyroid hormone replacement. 
               Thyroid. 2014;24(12):1670-751.
            
            4. **Wartofsky L, Dickey RA.** The evidence for a narrower thyrotropin reference range is compelling. 
               J Clin Endocrinol Metab. 2005;90(9):5483-8.
            
            5. **Lee RH, Spencer CA, Mestman JH, et al.** Free T4 immunoassays are flawed during pregnancy. 
               Am J Obstet Gynecol. 2009;200(3):260.e1-6.
            
            **Lưu ý:** FTI là xét nghiệm cũ, các hướng dẫn hiện đại khuyến cáo dùng Free T4 trực tiếp.
            """)
    
    # Quick guide
    st.markdown("---")
    references = get_references("Free T4 Index")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            show_evidence_level=True,
            show_links=True
        )
    
    st.info("""
    💡 **Điểm quan trọng:**
    
    1. **FTI là xét nghiệm cũ** - Hiện nay đo Free T4 trực tiếp chính xác hơn
    
    2. **TSH là quan trọng nhất** - Luôn làm TSH trước để sàng lọc
    
    3. **Khi nào dùng FTI:**
       - Không có Free T4
       - So sánh với kết quả cũ đã có FTI
       - Nghi ngờ rối loạn protein gắn hormone
    
    4. **Luôn kết hợp lâm sàng:**
       - Triệu chứng cường/suy giáp
       - Thuốc đang dùng
       - Bệnh kèm theo
    
    5. **Không điều trị chỉ dựa vào một lần xét nghiệm** - Cần xét nghiệm lại và đánh giá lâm sàng đầy đủ
    """)


if __name__ == "__main__":
    render()

