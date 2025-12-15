"""
Corrected Calcium Calculator
Điều chỉnh Calcium theo Albumin

Formula:
Corrected Ca = Measured Ca + 0.8 × (4.0 - Albumin)

Why? 40% of calcium is bound to albumin.
Low albumin → Low measured Ca but normal ionized Ca

Reference:
Payne RB, et al. Interpretation of serum calcium in patients with abnormal serum proteins.
Br Med J. 1973;4(5893):643-6.
"""

import streamlit as st
from scores.utils.validation import validate_lab_value
from components.ui.validation import render_validation_errors
from components.ui.results import render_result_box
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
# =====================================


def _format_num(value: float, decimals: int = 1) -> str:
    """Format số, loại bỏ số 0 thừa"""
    rounded = round(value, decimals)
    if rounded == int(rounded):
        return str(int(rounded))
    return f"{rounded:.{decimals}f}".rstrip('0').rstrip('.')


def render():
    """Render Corrected Calcium Calculator"""
    
    st.subheader("🦴 Corrected Calcium")
    st.caption("Calcium Điều Chỉnh Theo Albumin")
    shared = load_shared_result_from_url()
    if shared and shared.get("calculator_id") == "corrected_calcium":
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared.get('calculator_name', 'Corrected Calcium')}")
    
    st.markdown("""
    **Corrected Calcium** điều chỉnh calcium toàn phần theo nồng độ albumin.
    
    **Tại sao cần điều chỉnh?**
    - 40% calcium gắn với albumin
    - Albumin thấp → Ca đo thấp giả tạo
    - Nhưng Ca ion hóa (Ca²⁺) vẫn bình thường
    
    **Công thức:** Ca corrected = Ca measured + 0.8 × (4.0 - Albumin)
    """)
    
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 🔬 Xét nghiệm")
        
        # Calcium
        st.markdown("#### 1. Calcium toàn phần")
        
        ca_unit = st.radio(
            "Đơn vị:",
            ["mg/dL", "mmol/L (SI)"],
            horizontal=True,
            key="ca_unit"
        )
        
        if "mg/dL" in ca_unit:
            ca = st.number_input(
                "Calcium (mg/dL):",
                min_value=4.0,
                max_value=16.0,
                value=8.5,
                step=0.1,
                format="%.1f",
                help="Bình thường: 8.5-10.5 mg/dL"
            )
            ca_mgdl = ca
            ca_mmol = round(ca / 4, 2)
            st.caption(f"≈ {ca_mmol if ca_mmol != int(ca_mmol) else int(ca_mmol)} mmol/L")
        else:
            ca = st.number_input(
                "Calcium (mmol/L):",
                min_value=1.0,
                max_value=4.0,
                value=2.2,
                step=0.05,
                format="%.1f",
                help="Bình thường: 2.12-2.62 mmol/L"
            )
            ca_mgdl = ca * 4
            st.caption(f"≈ {_format_num(ca_mgdl, 1)} mg/dL")
        
        # Albumin
        st.markdown("#### 2. Albumin")
        albumin = st.number_input(
            "Albumin (g/dL):",
            min_value=1.0,
            max_value=6.0,
            value=4.0,
            step=0.1,
            format="%.1f",
            help="Bình thường: 3.5-5.5 g/dL"
        )
        st.caption(f"≈ {round(albumin * 10)} g/L")
        
        st.markdown("---")
        
        if st.button("🧮 Tính Corrected Calcium", type="primary", use_container_width=True):
            # Validate inputs
            validation_errors = []
            
            # Validate calcium
            if "mg/dL" in ca_unit:
                is_valid_ca, ca_error = validate_lab_value(ca, "Calcium (mg/dL)", 4.0, 16.0)
            else:
                is_valid_ca, ca_error = validate_lab_value(ca, "Calcium (mmol/L)", 1.0, 4.0)
            if not is_valid_ca:
                validation_errors.append(ca_error)
            
            # Validate albumin
            is_valid_alb, alb_error = validate_lab_value(albumin, "Albumin (g/dL)", 1.0, 6.0)
            if not is_valid_alb:
                validation_errors.append(alb_error)
            
            if validation_errors:
                render_validation_errors(validation_errors)
            
            # Calculate corrected calcium
            ca_corrected_mgdl = ca_mgdl + 0.8 * (4.0 - albumin)
            ca_corrected_mmol = ca_corrected_mgdl / 4
            
            # Determine if correction needed
            if abs(ca_corrected_mgdl - ca_mgdl) < 0.3:
                correction_needed = False
            else:
                correction_needed = True
            
            # Interpret corrected calcium
            if ca_corrected_mgdl < 8.5:
                interpretation = "THẤP (Hypocalcemia)"
                color = "error"
            elif ca_corrected_mgdl <= 10.5:
                interpretation = "BÌNH THƯỜNG"
                color = "success"
            else:
                interpretation = "CAO (Hypercalcemia)"
                color = "warning"
            
            st.markdown("---")
            st.markdown("## 📊 Kết quả")
            
            # Display measured calcium
            render_result_box(
                title="Calcium Đo Được",
                value=f"{ca_mgdl:.1f} mg/dL",
                subtitle=f"{ca_mgdl/4:.2f} mmol/L",
                color="info",
                icon="🔬",
                size="medium"
            )
            
            # Display corrected calcium with interpretation
            render_result_box(
                title="Calcium Điều Chỉnh",
                value=f"{ca_corrected_mgdl:.1f} mg/dL",
                subtitle=f"{interpretation} ({ca_corrected_mmol:.2f} mmol/L)",
                color=color,
                icon="🦴" if color == "success" else "⚠️" if color == "warning" else "🚨",
                size="large"
            )
            
            st.caption("Bình thường: 8.5-10.5 mg/dL")
            
            # Phase 1: history + share + suggestions
            inputs_dict = {
                "Calcium Input": ca_mgdl,
                "Albumin (g/dL)": albumin,
                "Unit": ca_unit
            }
            results_dict = {
                "Corrected Calcium (mg/dL)": round(ca_corrected_mgdl, 1),
                "Corrected Calcium (mmol/L)": round(ca_corrected_mmol, 2),
                "Interpretation": interpretation
            }
            
            save_calculation_to_history(
                calculator_id="corrected_calcium",
                calculator_name="Corrected Calcium",
                inputs=inputs_dict,
                results=results_dict
            )
            
            render_share_section(
                calculator_id="corrected_calcium",
                calculator_name="Corrected Calcium",
                inputs=inputs_dict,
                results=results_dict,
                show_qr=True
            )
            
            render_suggestions(
                calculator_id="corrected_calcium",
                calculator_name="Corrected Calcium",
                category="Nội Tiết",
                show_related=True,
                show_category=True,
                limit=3
            )
            
            st.markdown("---")
            
            if correction_needed:
                if albumin < 4.0:
                    st.warning(f"""
                    ⚠️ **CẦN ĐIỀU CHỈNH**
                    
                    Albumin thấp ({albumin:.1f} g/dL) → Ca đo thấp giả tạo
                    
                    - Ca đo được: {ca_mgdl:.1f} mg/dL
                    - **Ca điều chỉnh: {ca_corrected_mgdl:.1f} mg/dL** ← Sử dụng giá trị này
                    - Chênh lệch: +{ca_corrected_mgdl - ca_mgdl:.1f} mg/dL
                    """)
                else:
                    st.info(f"""
                    ℹ️ Albumin cao ({albumin:.1f} g/dL)
                    
                    - Ca đo được: {ca_mgdl:.1f} mg/dL
                    - **Ca điều chỉnh: {ca_corrected_mgdl:.1f} mg/dL**
                    - Chênh lệch: {ca_corrected_mgdl - ca_mgdl:.1f} mg/dL
                    """)
            else:
                st.success(f"""
                ✅ **KHÔNG CẦN ĐIỀU CHỈNH**
                
                Albumin gần bình thường ({albumin:.1f} g/dL)
                
                Ca đo được ≈ Ca điều chỉnh: {ca_mgdl:.1f} mg/dL
                """)
            
            st.markdown("---")
            st.markdown("### 💡 GIẢI THÍCH & XỬ TRÍ")
            
            if ca_corrected_mgdl < 8.5:
                st.error(f"""
                **🔴 HYPOCALCEMIA (Ca < 8.5 mg/dL)**
                
                **Ca điều chỉnh: {ca_corrected_mgdl:.1f} mg/dL**
                
                **Mức độ:**
                - Nhẹ: 7.5-8.5 mg/dL
                - Trung bình: 6.5-7.5 mg/dL
                - Nặng: <6.5 mg/dL (nguy kịch)
                
                **Ca của bạn: {ca_corrected_mgdl:.1f} mg/dL** = {"Nhẹ" if ca_corrected_mgdl > 7.5 else "Trung bình" if ca_corrected_mgdl > 6.5 else "NẶNG"}
                
                **Triệu chứng:**
                
                **Nhẹ-Trung bình:**
                - Tê bì chung quanh miệng, tay chân
                - Chuột rút cơ
                - Paresthesia
                - Chvostek's sign (+)
                - Trousseau's sign (+)
                
                **Nặng (Ca < 7.0):**
                - **Tetany** (co cứng cơ)
                - **Laryngospasm** (co thắt thanh quản)
                - **Seizures** (động kinh)
                - **QT prolongation** → Arrhythmia
                - **Heart failure**
                - Bronchospasm
                
                **Nguyên Nhân:**
                
                1. **Suy tuyến cận giáp:**
                   - Sau phẫu thuật tuyến giáp
                   - Autoimmune
                   - Check PTH
                
                2. **Thiếu Vitamin D:**
                   - Không tiếp xúc ánh sáng mặt trời
                   - Suy dinh dưỡng
                   - Malabsorption
                   - CKD (không chuyển hóa Vit D)
                
                3. **Hypomagnesemia:**
                   - Mg thấp → PTH không tiết được
                   - Check & correct Mg trước
                
                4. **CKD/Suy thận:**
                   - Giảm hấp thu Ca
                   - Giảm Vitamin D hoạt tính
                   - Tăng Phosphate
                
                5. **Acute pancreatitis:**
                   - Ca lắng đọng trong mô hoại tử
                   - Chỉ điểm tiên lượng xấu
                
                6. **Thuốc:**
                   - Bisphosphonate
                   - Calcitonin
                   - Loop diuretics
                   - Phenytoin
                
                7. **Massive blood transfusion:**
                   - Citrate trong máu trữ gắn Ca
                
                **XỬ TRÍ:**
                
                **Cấp cứu (triệu chứng hoặc Ca < 7.0):**
                1. **Calcium gluconate 10% IV:**
                   - 1-2 ampule (10-20ml) trong 100ml D5W
                   - Chạy trong 10-20 phút
                   - **Không bolus nhanh** (nguy cơ arrhythmia)
                   - Monitor ECG
                
                2. **Sau đó Maintenance:**
                   - Ca gluconate 10% 10 ampule (100ml) trong 1L NS
                   - Chạy 50-100ml/h (0.5-2mg Ca element/kg/h)
                   - Mục tiêu: Ca 8-9 mg/dL
                
                3. **Check & correct Mg:**
                   - Nếu Mg < 2.0 mg/dL:
                   - MgSO4 2g IV trong 15-60 phút
                   - Sau đó 1-2g/h maintenance
                
                **Không cấp cứu (Ca 7-8.5, không triệu chứng):**
                1. **Calcium carbonate** 1-2g Ca element/ngày PO (chia 2-3 lần)
                   - Tums 500mg = 200mg Ca element
                   - Uống với bữa ăn
                
                2. **Vitamin D:**
                   - Vitamin D3 1000-2000 IU/ngày
                   - Nếu thiếu nặng: 50,000 IU/tuần × 8 tuần
                
                3. **Điều trị nguyên nhân**
                
                **Theo dõi:**
                - Ca, Albumin, Mg, Phosphate
                - PTH, Vitamin D (25-OH-D)
                - ECG (QTc interval)
                
                **CẢNH BÁO:**
                - ⚠️ Ca < 6.5 mg/dL = nguy kịch → ICU
                - ⚠️ QTc prolongation → nguy cơ Torsades de Pointes
                - ⚠️ Laryngospasm → nguy cơ ngạt thở
                """)
            
            elif ca_corrected_mgdl <= 10.5:
                st.success(f"""
                **🟢 CALCIUM BÌNH THƯỜNG (8.5-10.5 mg/dL)**
                
                **Ca điều chỉnh: {ca_corrected_mgdl:.1f} mg/dL**
                
                **Đánh giá:** Calcium trong giới hạn bình thường.
                
                **Lưu ý:**
                - Giá trị Ca điều chỉnh chỉ là ước tính
                - Nếu nghi ngờ lâm sàng, check **Ionized Calcium** (Ca²⁺)
                - Ca²⁺ là gold standard (bình thường: 1.16-1.32 mmol/L)
                
                **Khi nào cần check Ca ion hóa:**
                - Acid-base disorder (ảnh hưởng Ca ion hóa)
                - Rối loạn protein nặng
                - Triệu chứng không khớp với Ca toàn phần
                - ICU, bệnh nhân nặng
                
                **Duy trì Ca bình thường:**
                - Ăn đủ Ca: 1000-1200mg/ngày
                - Vitamin D đủ: 600-800 IU/ngày
                - Vận động đều đặn
                - Tránh thuốc ảnh hưởng Ca
                """)
            
            else:  # Hypercalcemia
                st.warning(f"""
                **🟡 HYPERCALCEMIA (Ca > 10.5 mg/dL)**
                
                **Ca điều chỉnh: {ca_corrected_mgdl:.1f} mg/dL**
                
                **Mức độ:**
                - Nhẹ: 10.5-12.0 mg/dL
                - Trung bình: 12.0-14.0 mg/dL
                - Nặng: >14.0 mg/dL (hypercalcemic crisis)
                
                **Ca của bạn: {ca_corrected_mgdl:.1f} mg/dL** = {"Nhẹ" if ca_corrected_mgdl < 12 else "Trung bình" if ca_corrected_mgdl < 14 else "NẶNG"}
                
                **Triệu chứng - "Stones, Bones, Groans, Thrones, Psychiatric overtones":**
                
                **Nhẹ-Trung bình:**
                - **Stones:** Sỏi thận, đau hông
                - **Bones:** Đau xương, osteoporosis
                - **Groans:** Đau bụng, táo bón, nôn
                - **Thrones:** Polyuria (đái nhiều)
                - **Psychiatric:** Trầm cảm, lú lẫn, mệt mỏi
                
                **Nặng (Ca > 14):**
                - **Cardiac:** QT shortening, arrhythmia, HTN
                - **Neurologic:** Confusion, lethargy, coma
                - **GI:** Pancreatitis
                - **Renal:** AKI, nephrogenic DI
                
                **Nguyên nhân (90% = PTH-mediated hoặc Malignancy):**
                
                **1. Hyperparathyroidism (PTH cao):**
                - **Primary:** Adenoma tuyến cận giáp (phổ biến nhất ngoại trú)
                - PTH tăng, Phosphate thấp
                - Sỏi thận, osteoporosis
                - Điều trị: Phẫu thuật
                
                **2. Malignancy (30-40% - phổ biến nhất nội trú):**
                - **PTHrP (Parathyroid hormone-related peptide):**
                  * Lung, kidney, breast cancer
                  * PTH thấp, PTHrP cao
                - **Osteolytic metastasis:**
                  * Multiple myeloma, breast cancer
                  * Local bone destruction
                - **Lymphoma:**
                  * Tăng Vitamin D (calcitriol)
                
                **3. Granulomatous disease:**
                - Sarcoidosis, TB
                - Tăng Vitamin D
                - PTH thấp
                
                **4. Thuốc:**
                - **Thiazide diuretics** (giảm thải Ca qua nước tiểu)
                - **Lithium** (tăng PTH)
                - **Vitamin D intoxication**
                - **Calcium supplements** quá liều
                - **Vitamin A** quá liều
                
                **5. Bất động lâu ngày:**
                - Tăng hủy xương
                
                **6. Hyperthyroidism:**
                - Tăng chuyển hóa xương
                
                **7. Milk-alkali syndrome:**
                - Uống quá nhiều Ca + antacid
                
                **XỬ TRÍ:**
                
                **Nhẹ (Ca 10.5-12, không triệu chứng):**
                1. **Hydration:** Uống nhiều nước (2-3L/ngày)
                2. **Tránh:**
                   - Thiazide diuretics
                   - Vitamin D, Ca supplements
                   - Bất động
                3. **Điều trị nguyên nhân:**
                   - Phẫu thuật nếu hyperparathyroidism
                   - Điều trị ung thư nếu có
                
                **Trung bình (Ca 12-14) hoặc Có triệu chứng:**
                1. **IV Saline tích cực:**
                   - NS 200-300ml/h (4-6L trong 24h)
                   - Mục tiêu: UO 100-150ml/h
                   - Monitor volume status (CVP, I/O)
                
                2. **Loop diuretics (SAU khi đã hydrate đủ):**
                   - Furosemide 20-40mg IV q6-12h
                   - Tăng thải Ca qua thận
                   - **Không dùng nếu còn mất nước!**
                
                3. **Bisphosphonate:**
                   - **Zoledronic acid** 4mg IV trong 15 phút
                   - Hoặc Pamidronate 60-90mg IV
                   - Hiệu quả sau 2-4 ngày, kéo dài 2-4 tuần
                   - Dùng nếu malignancy hoặc không đáp ứng hydration
                
                **Nặng (Ca > 14) - KHẨN CẤP:**
                1. **ICU monitoring**
                
                2. **Aggressive hydration:**
                   - NS 250-500ml/h
                   - +/- Furosemide
                
                3. **Calcitonin:**
                   - 4 IU/kg SC/IM q12h
                   - Hiệu quả nhanh (4-6h) nhưng tachyphylaxis
                   - Dùng trong khi chờ bisphosphonate có hiệu quả
                
                4. **Bisphosphonate:**
                   - Zoledronic acid 4mg IV
                
                5. **Nếu không đáp ứng:**
                   - **Hemodialysis** (zero-calcium dialysate)
                   - **Denosumab** 120mg SC
                   - **Steroid** (nếu lymphoma, granuloma, Vit D intoxication)
                
                6. **Điều trị nguyên nhân khẩn cấp**
                
                **Workup:**
                - PTH (phân biệt PTH-mediated vs non-PTH)
                - Phosphate
                - Vitamin D (25-OH-D, 1,25-OH-D)
                - PTHrP (nếu nghi malignancy)
                - Imaging: Neck ultrasound, CT chest/abdomen/pelvis
                
                **CẢNH BÁO:**
                - ⚠️ Ca > 14 mg/dL = hypercalcemic crisis → ICU
                - ⚠️ Nguy cơ arrhythmia, cardiac arrest
                - ⚠️ AKI do calcium nephropathy
                """)
            
            # Additional info
            st.markdown("---")
            with st.expander("🧮 Chi tiết tính toán"):
                st.markdown(f"""
                **Công thức Payne:**
                ```
                Corrected Ca (mg/dL) = Measured Ca + 0.8 × (4.0 - Albumin)
                ```
                
                **Giá trị của bạn:**
                - Ca đo được = {ca_mgdl:.1f} mg/dL
                - Albumin = {albumin:.1f} g/dL
                - Correction = 0.8 × (4.0 - {albumin:.1f}) = {0.8 * (4.0 - albumin):.1f}
                - **Ca điều chỉnh = {ca_mgdl:.1f} + {0.8 * (4.0 - albumin):.1f} = {ca_corrected_mgdl:.1f} mg/dL**
                
                **Chuyển đổi đơn vị:**
                - mg/dL ÷ 4 = mmol/L
                - {ca_corrected_mgdl:.1f} mg/dL = {ca_corrected_mmol:.2f} mmol/L
                """)
            
            with st.expander("📚 Tài liệu tham khảo"):
                st.markdown("""
                **Primary Reference:**
                - Payne RB, Little AJ, Williams RB, Milner JR. 
                  *Interpretation of serum calcium in patients with abnormal serum proteins.* 
                  Br Med J. 1973 Dec 15;4(5893):643-6. [PMID: 4758544]
                
                **Guidelines:**
                - Bilezikian JP, et al. *Guidelines for the management of asymptomatic primary hyperparathyroidism.* 
                  J Clin Endocrinol Metab. 2014;99(10):3561-9.
                
                - Cooper MS, Gittoes NJ. *Diagnosis and management of hypercalcaemia.* 
                  BMJ. 2008 May 24;336(7655):1177-80.
                
                - Shane E, Berenson JR. *Treatment of hypercalcemia.* 
                  UpToDate. 2023.
                """)
    
    # Educational content
    st.markdown("---")
    st.markdown("### 📖 THÔNG TIN THÊM")
    
    with st.expander("❓ Tại sao cần điều chỉnh calcium?"):
        st.markdown("""
        **Calcium trong máu có 3 dạng:**
        
        1. **Ionized (Ca²⁺) - 50%:**
           - Dạng hoạt tính sinh học
           - Quan trọng cho: Co cơ, dẫn truyền thần kinh, đông máu
           - **Đây là giá trị thực sự quan trọng!**
        
        2. **Protein-bound - 40%:**
           - 90% gắn với **Albumin**
           - 10% gắn với globulin
           - Không hoạt tính sinh học
        
        3. **Complexed - 10%:**
           - Gắn với anion (citrate, phosphate, sulfate)
           - Không hoạt tính sinh học
        
        **Vấn đề:**
        - Lab thường đo **Ca toàn phần** (cả 3 dạng)
        - Albumin thấp → Ca protein-bound giảm → Ca toàn phần giảm
        - **NHƯNG Ca²⁺ (ion hóa) vẫn bình thường!**
        - → Không cần điều trị
        
        **Giải pháp:**
        - Điều chỉnh Ca theo Albumin
        - Hoặc đo trực tiếp **Ca ion hóa** (gold standard)
        """)
    
    with st.expander("⚖️ Calcium vs Phosphate"):
        st.markdown("""
        **Calcium và Phosphate có mối quan hệ nghịch:**
        
        **Điều hòa bởi PTH và Vitamin D:**
        - **PTH:**
          * Tăng Ca máu (↑ hấp thu xương, ↑ hấp thu thận, ↑ Vit D)
          * Giảm Phosphate máu (↑ thải qua thận)
        
        - **Vitamin D:**
          * Tăng cả Ca và Phosphate (↑ hấp thu ruột)
        
        **Ca × PO₄ product:**
        - Ca (mg/dL) × PO₄ (mg/dL) < 55
        - Nếu > 55: Nguy cơ lắng đọng calcium phosphate vào mô mềm
        
        **Pattern nhận biết:**
        
        | Tình trạng | Ca | PO₄ | PTH |
        |------------|-----|-----|-----|
        | **Primary hyperparathyroidism** | ↑ | ↓ | ↑↑ |
        | **Malignancy** | ↑↑ | ↓ | ↓ |
        | **Hypoparathyroidism** | ↓ | ↑ | ↓↓ |
        | **CKD** | ↓ | ↑↑ | ↑↑ |
        | **Vitamin D deficiency** | ↓ | ↓ | ↑ |
        | **Vitamin D intoxication** | ↑ | ↑ | ↓ |
        """)
    
    # Footer
    st.markdown("---")
    references = get_references("Corrected Ca")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            show_evidence_level=True,
            show_links=True
        )
    
    st.caption("📚 Essential correction for accurate calcium interpretation")
    st.caption("⚠️ Always consider albumin when interpreting calcium levels")
    st.caption("🏥 When in doubt, measure ionized calcium directly")

