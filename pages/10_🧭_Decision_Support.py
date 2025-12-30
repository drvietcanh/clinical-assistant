"""
Hỗ trợ quyết định (Decision Support)
- Flowcharts quyết định lâm sàng
- An toàn thai kỳ & cho con bú
- Tính liều Nhi khoa
"""

import streamlit as st
from utils.page_helper import setup_page, render_standard_footer
from components.ui import render_info_box, render_hero

# Phase 2 imports
from components.flowchart import render_flowchart, create_chest_pain_algorithm
from components.flowcharts.clinical_rules import (
    create_wells_pe_flowchart,
    create_perc_flowchart,
    create_cha2ds2vasc_flowchart,
    create_sepsis_flowchart,
    create_stroke_flowchart,
    create_aki_flowchart,
    create_curb65_flowchart,
    create_shock_flowchart,
    create_gi_bleed_flowchart,
    create_dka_flowchart,
    create_copd_exacerbation_flowchart,
    create_asthma_exacerbation_flowchart,
    create_acute_hf_flowchart,
    create_anaphylaxis_flowchart,
    create_dvt_flowchart,
    create_hyponatremia_flowchart,
    create_tbi_flowchart,
    create_meningitis_flowchart,
    create_febrile_neutropenia_flowchart,
    create_acute_pancreatitis_flowchart,
)
from components.pregnancy_lactation_display import render_pregnancy_lactation_section
from scores.pediatrics.pediatric_dosing import render_pediatric_dosing_calculator

# Standard page setup
setup_page(
    page_title="Hỗ trợ quyết định",
    page_icon="🧭",
    description="Flowcharts, thai kỳ/cho bú, liều Nhi khoa"
)

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("🧭 Hỗ trợ quyết định")
    
    feature_options = [
        "🔄 Flowcharts quyết định lâm sàng",
        "🤰 Thai kỳ & cho con bú",
        "👶 Liều Nhi khoa"
    ]
    
    last_feature = st.session_state.get("phase2_feature_selector", feature_options[0])
    default_index = feature_options.index(last_feature) if last_feature in feature_options else 0
    
    selected_feature = st.selectbox(
        "Tính năng:",
        feature_options,
        index=default_index,
        key="phase2_feature_selector"
    )
    
    st.markdown("---")
    render_info_box(
        """
        <div>
            <p><strong>📚 Nhóm 🧭 Hỗ trợ quyết định:</strong></p>
            <p><strong>🔄 Flowcharts quyết định lâm sàng</strong><br>
            - Quy trình ra quyết định từng bước, dựa trên clinical rules (Wells, PERC, CHA₂DS₂-VASc, Sepsis-3, CURB-65...)</p>
            <p><strong>🤰 Thai kỳ & cho con bú</strong><br>
            - Thông tin an toàn thuốc theo từng giai đoạn thai kỳ và cho con bú (tóm tắt thực hành)</p>
            <p><strong>👶 Liều Nhi khoa</strong><br>
            - Tính liều theo cân nặng/BSA, gợi ý liều thường dùng cho Nhi khoa</p>
        </div>
        """,
        type="info",
        title="Thông tin Module"
    )

# ========== MAIN CONTENT ==========

if selected_feature == feature_options[0]:
    st.header("🔄 Flowcharts quyết định lâm sàng")
    st.caption("Flowcharts tương tác cho các clinical decision rules quan trọng")
    
    # Algorithm selector
    algorithms = {
        "Wells PE Score": create_wells_pe_flowchart,
        "PERC Rule": create_perc_flowchart,
        "CHA₂DS₂-VASc Score": create_cha2ds2vasc_flowchart,
        "Sepsis-3 Protocol": create_sepsis_flowchart,
        "Acute Stroke": create_stroke_flowchart,
        "AKI Diagnostic": create_aki_flowchart,
        "CURB-65": create_curb65_flowchart,
        # Bệnh cấp cứu / bệnh nặng phổ biến
        "Acute Chest Pain / ACS": create_chest_pain_algorithm,
        "Shock / Hypotension": create_shock_flowchart,
        "Upper GI Bleeding": create_gi_bleed_flowchart,
        "DKA Initial Management": create_dka_flowchart,
        "COPD Exacerbation": create_copd_exacerbation_flowchart,
        "Acute Asthma Exacerbation": create_asthma_exacerbation_flowchart,
        "Acute Heart Failure / Pulmonary Edema": create_acute_hf_flowchart,
        "Anaphylaxis": create_anaphylaxis_flowchart,
        "DVT (Lower Limb) / Wells DVT": create_dvt_flowchart,
        "Hyponatremia": create_hyponatremia_flowchart,
        "Traumatic Brain Injury (TBI)": create_tbi_flowchart,
        "Acute Bacterial Meningitis": create_meningitis_flowchart,
        "Febrile Neutropenia": create_febrile_neutropenia_flowchart,
        "Acute Pancreatitis": create_acute_pancreatitis_flowchart,
    }
    
    selected_algorithm = st.selectbox(
        "Chọn flowchart:",
        list(algorithms.keys()),
        key="algorithm_selector"
    )
    
    st.markdown("---")
    
    # Render flowchart
    if selected_algorithm in algorithms:
        nodes, edges = algorithms[selected_algorithm]()
        
        # Adjust size based on algorithm
        size_map = {
            "Wells PE Score": (900, 700),
            "PERC Rule": (900, 600),
            "CHA₂DS₂-VASc Score": (800, 500),
            "Sepsis-3 Protocol": (900, 700),
            "Acute Stroke": (900, 700),
            "AKI Diagnostic": (800, 600),
            "CURB-65": (800, 500),
            "Acute Chest Pain / ACS": (900, 600),
            "Shock / Hypotension": (900, 600),
            "Upper GI Bleeding": (900, 650),
            "DKA Initial Management": (900, 650),
            "COPD Exacerbation": (900, 650),
            "Acute Asthma Exacerbation": (900, 650),
            "Acute Heart Failure / Pulmonary Edema": (900, 650),
            "Anaphylaxis": (900, 600),
            "DVT (Lower Limb) / Wells DVT": (900, 650),
            "Hyponatremia": (900, 700),
            "Traumatic Brain Injury (TBI)": (900, 650),
            "Acute Bacterial Meningitis": (900, 650),
            "Febrile Neutropenia": (900, 650),
            "Acute Pancreatitis": (900, 650),
        }
        
        width, height = size_map.get(selected_algorithm, (800, 600))
        
        render_flowchart(
            nodes=nodes,
            edges=edges,
            title=f"{selected_algorithm} - Clinical Algorithm",
            width=width,
            height=height,
            interactive=True
        )
        
        # Algorithm description
        st.markdown("---")
        with st.expander("ℹ️ Giải thích Algorithm"):
            if selected_algorithm == "Wells PE Score":
                st.markdown("""
                **Wells PE Score Algorithm:**
                
                1. Tính Wells Score dựa trên các tiêu chí lâm sàng
                2. Phân loại nguy cơ: Thấp (≤4), Trung bình (5-6), Cao (≥7)
                3. Nguy cơ thấp/trung bình → D-dimer
                4. Nguy cơ cao → CTPA trực tiếp
                5. D-dimer (+) → CTPA
                6. D-dimer (-) → Loại trừ PE
                7. CTPA (+) → Điều trị PE
                8. CTPA (-) → Loại trừ PE
                
                **📚 Dựa trên:**
                - Wells PS, et al. Derivation of a simple clinical model to categorize patients probability of pulmonary embolism (1998)
                - ESC/ERS Guidelines for Diagnosis and Management of Acute Pulmonary Embolism (2019, 2023)
                - ATS/ERS Clinical Practice Guidelines on Pulmonary Embolism
                """)
            elif selected_algorithm == "PERC Rule":
                st.markdown("""
                **PERC Rule Algorithm:**
                
                1. Đánh giá 8 tiêu chí PERC
                2. PERC = 0 (tất cả âm) → Loại trừ PE, không cần test
                3. PERC ≥ 1 → Tính Wells Score
                4. Wells ≤ 4 → D-dimer
                5. Wells > 4 → CTPA
                6. D-dimer (+) → CTPA
                7. D-dimer (-) → Loại trừ PE
                
                **📚 Dựa trên:**
                - Kline JA, et al. Clinical criteria to prevent unnecessary diagnostic testing in emergency department patients with suspected pulmonary embolism (2004)
                - ESC/ERS Guidelines for Diagnosis and Management of Acute Pulmonary Embolism (2019, 2023)
                """)
            elif selected_algorithm == "CHA₂DS₂-VASc Score":
                st.markdown("""
                **CHA₂DS₂-VASc Score Algorithm:**
                
                1. Tính CHA₂DS₂-VASc Score
                2. Score = 0 (Nam) → Không kháng đông
                3. Score = 1 (Nam) → Cân nhắc kháng đông
                4. Score ≥ 2 → Tính HAS-BLED → Khuyến cáo kháng đông
                
                **📚 Dựa trên:**
                - Lip GY, et al. Refining clinical risk stratification for predicting stroke and thromboembolism in atrial fibrillation (2009)
                - AHA/ACC/HRS Guideline for Management of Patients with Atrial Fibrillation (2019, 2023)
                - ESC Guidelines for Management of Atrial Fibrillation (2020, 2023)
                """)
            elif selected_algorithm == "Sepsis-3 Protocol":
                st.markdown("""
                **Sepsis-3 Protocol:**
                
                1. Nghi ngờ nhiễm trùng
                2. Tính qSOFA (screening)
                3. qSOFA ≥ 2 → Tính SOFA
                4. qSOFA < 2 → Nguy cơ thấp
                5. SOFA ≥ 2 → SEPSIS
                6. Septic Shock? → 1-Hour Bundle
                7. Theo dõi
                
                **📚 Dựa trên:**
                - Singer M, et al. The Third International Consensus Definitions for Sepsis and Septic Shock (Sepsis-3) (2016)
                - **Surviving Sepsis Campaign (SSC) Guidelines 2021** - International Guidelines for Management of Sepsis and Septic Shock
                - IDSA/SCCM Guidelines
                """)
            elif selected_algorithm == "Acute Stroke":
                st.markdown("""
                **Acute Stroke Algorithm:**
                
                1. Đột quỵ cấp
                2. Thời gian khởi phát?
                3. < 4.5h → tPA
                4. 4.5-24h → Thrombectomy
                5. > 24h → Điều trị hỗ trợ
                6. CT não → ICH?
                7. Không ICH → tPA/Thrombectomy
                8. Có ICH → Điều trị hỗ trợ
                
                **📚 Dựa trên:**
                - AHA/ASA Guidelines for Early Management of Patients with Acute Ischemic Stroke (2019, 2023)
                - AHA/ASA Guidelines for Management of Spontaneous Intracerebral Hemorrhage (2022)
                - European Stroke Organisation (ESO) Guidelines for Management of Acute Ischemic Stroke (2021)
                """)
            elif selected_algorithm == "AKI Diagnostic":
                st.markdown("""
                **AKI Diagnostic Algorithm:**
                
                1. Nghi ngờ AKI
                2. Phân loại AKI (KDIGO Stage 1, 2, 3)
                3. Tính FENa
                4. FENa < 1% → Prerenal
                5. FENa > 2% → Intrinsic Renal
                6. Check obstruction → Postrenal
                7. Điều trị theo nguyên nhân
                
                **📚 Dựa trên:**
                - **KDIGO (Kidney Disease: Improving Global Outcomes)** Clinical Practice Guideline for Acute Kidney Injury (2012, 2024)
                - AKI Network (AKIN) Criteria
                - RIFLE Criteria
                """)
            elif selected_algorithm == "CURB-65":
                st.markdown("""
                **CURB-65 Algorithm:**
                
                1. Viêm phổi cộng đồng
                2. Tính CURB-65 Score
                3. Score 0 → Điều trị ngoại trú
                4. Score 1-2 → Nhập viện
                5. Score 3-5 → ICU
                
                **📚 Dựa trên:**
                - Lim WS, et al. Defining community acquired pneumonia severity on presentation to hospital (2003)
                - IDSA/ATS Guidelines for Community-Acquired Pneumonia (2019)
                - BTS (British Thoracic Society) Guidelines for Management of Community Acquired Pneumonia (2009, 2015)
                """)
            elif selected_algorithm == "COPD Exacerbation":
                st.markdown("""
                **COPD Exacerbation Algorithm:**

                1. Nghi đợt cấp COPD
                2. Đánh giá mức độ nặng (khó thở, SpO₂, RR, huyết động)
                3. Nhẹ / Trung bình → SABA ± SAMA, Corticosteroid uống, Cân nhắc kháng sinh nếu có chỉ định
                4. Nặng / Nguy kịch → Oxy 88-92%, NIPPV (BiPAP), Nhập viện / ICU

                **📚 Dựa trên:**
                - GOLD (Global Initiative for Chronic Obstructive Lung Disease) Report 2024
                - ERS/ATS Guidelines on COPD Exacerbations
                """)
            elif selected_algorithm == "Acute Asthma Exacerbation":
                st.markdown("""
                **Acute Asthma Exacerbation Algorithm:**

                1. Cơn hen cấp
                2. Đánh giá mức độ (SpO₂, RR, nói câu/từ)
                3. Nhẹ/Trung bình → SABA khí dung lặp lại, Corticosteroid uống
                4. Nặng/Nguy kịch → Oxy, SABA + Ipratropium, Corticosteroid IV, Magnesium sulfate IV, ICU nếu đe dọa ngừng thở

                **📚 Dựa trên:**
                - GINA (Global Initiative for Asthma) Strategy 2024
                - ERS/ATS Guidelines on Severe Asthma Exacerbations
                """)
            elif selected_algorithm == "Acute Heart Failure / Pulmonary Edema":
                st.markdown("""
                **Acute Heart Failure / Pulmonary Edema Algorithm:**

                1. Khó thở cấp / phù phổi
                2. ABC + Oxy + Monitor
                3. Phân tầng theo huyết áp (HA cao / bình thường / thấp)
                4. HA cao → Vasodilator IV + Furosemide
                5. HA bình thường → Furosemide ± Vasodilator
                6. HA thấp → Inotrope ± Vasopressor, ICU
                7. Cân nhắc NIV (CPAP/BiPAP) nếu phù phổi nặng

                **📚 Dựa trên:**
                - ESC Guidelines for the Diagnosis and Treatment of Acute and Chronic Heart Failure (2021)
                - AHA/ACC/HFSA Guidelines for the Management of Heart Failure (2022)
                """)
            elif selected_algorithm == "Anaphylaxis":
                st.markdown("""
                **Anaphylaxis Emergency Management Algorithm:**

                1. Nghi sốc phản vệ
                2. ABC + gọi hỗ trợ + nằm ngửa, nâng chân
                3. Tiêm Adrenaline IM 0.3-0.5 mg (1:1000) mặt ngoài đùi, lặp lại mỗi 5-10 phút nếu cần
                4. Oxy lưu lượng cao, Monitor SpO₂, HA, ECG
                5. Bolus dịch nhanh Crystalloid 20 ml/kg
                6. Adjuncts: Kháng Histamine, Corticoid
                7. Theo dõi ≥4-6 giờ (24h nếu nặng), ICU nếu suy hô hấp/shock dai dẳng

                **📚 Dựa trên:**
                - WAO (World Allergy Organization) Anaphylaxis Guidelines
                - EAACI (European Academy of Allergy and Clinical Immunology) Anaphylaxis Guidelines
                - Resuscitation Council (UK) Anaphylaxis Guidelines
                """)
            elif selected_algorithm == "DVT (Lower Limb) / Wells DVT":
                st.markdown("""
                **DVT (Lower Limb) / Wells DVT Algorithm:**

                1. Nghi ngờ DVT chi dưới
                2. Tính Wells DVT Score → phân tầng nguy cơ (thấp / trung bình / cao)
                3. Nguy cơ thấp/trung bình → D-dimer
                4. Nguy cơ cao → Siêu âm doppler TM chi dưới (có thể bỏ qua D-dimer)
                5. D-dimer (-) → Loại trừ DVT
                6. D-dimer (+) hoặc nguy cơ cao → Siêu âm
                7. Siêu âm (+) → Điều trị DVT; Siêu âm (-) → Loại trừ DVT

                **📚 Dựa trên:**
                - Wells DVT score derivation and validation studies
                - ACCP Guidelines on Venous Thromboembolism
                - ESC Guidelines on Diagnosis and Management of Acute Pulmonary Embolism (mục DVT)
                """)
            elif selected_algorithm == "Hyponatremia":
                st.markdown("""
                **Hyponatremia Algorithm:**

                1. Na+ <135 mmol/L → đánh giá triệu chứng (co giật, lơ mơ, hôn mê)
                2. Nếu triệu chứng nặng → Bolus NaCl 3% 1.5–2 ml/kg (hoặc 100 mL x3), theo dõi Na+ sát
                3. Nếu không nặng → đánh giá độ thẩm thấu (hypo/iso/hypertonic)
                4. Hyponatremia giảm thẩm thấu → đánh giá thể tích (giảm / bình thường / tăng)
                5. Giảm thể tích → NaCl 0.9% + ngưng lợi tiểu
                6. Thể tích bình thường (SIADH...) → hạn chế nước, điều trị nguyên nhân
                7. Tăng thể tích (suy tim, xơ gan...) → hạn chế nước + lợi tiểu
                8. Luôn giới hạn tốc độ tăng Na+ ≤8–10 mmol/L/24h

                **📚 Dựa trên:**
                - European Clinical Practice Guidelines on Diagnosis and Treatment of Hyponatraemia (2014, updates)
                - US expert consensus on hyponatremia management
                """)
            elif selected_algorithm == "Traumatic Brain Injury (TBI)":
                st.markdown("""
                **Traumatic Brain Injury (TBI) Algorithm:**

                1. Chấn thương sọ não → ABC + cố định cột sống cổ
                2. Đánh giá GCS (13–15 nhẹ, 9–12 trung bình, ≤8 nặng)
                3. GCS nhẹ: xem xét CT nếu có yếu tố nguy cơ (ngất, nôn, dùng kháng đông...) hoặc theo dõi/xuất viện có dặn dò
                4. GCS trung bình: CT não khẩn, thường nhập viện theo dõi
                5. GCS nặng: ABC ưu tiên, sau đó CT khi ổn định, tham vấn Ngoại TK, ICU theo dõi ICP

                **📚 Dựa trên:**
                - Brain Trauma Foundation Guidelines for Management of Severe TBI
                - ATLS Head Injury Protocol
                """)
            elif selected_algorithm == "Acute Bacterial Meningitis":
                st.markdown("""
                **Acute Bacterial Meningitis Algorithm (Người lớn):**

                1. Nghi viêm màng não (sốt, cổ cứng, đau đầu, thay đổi ý thức)
                2. Đánh giá dấu hiệu tăng ALNS/chèn ép (khuyết thần kinh khu trú, co giật mới, GCS ↓ nặng)
                3. Không dấu chèn ép rõ → cấy máu + KS TM sớm + Dexamethasone → chọc dò DNT sớm
                4. Có dấu chèn ép → CT não, nhưng **KHÔNG trì hoãn** KS TM nếu nghi mạnh
                5. Điều chỉnh KS theo kết quả DNT/cấy, theo dõi sát tại khoa phù hợp/ICU

                **📚 Dựa trên:**
                - IDSA Guidelines for Management of Bacterial Meningitis
                - ESCMID Guidelines on Acute Bacterial Meningitis
                """)
            elif selected_algorithm == "Febrile Neutropenia":
                st.markdown("""
                **Febrile Neutropenia Algorithm:**

                1. Sốt + ANC <500/µL (hoặc dự kiến <500) ở bệnh nhân ung thư/HST
                2. Đánh giá nguy cơ (MASCC/Risk Index → thấp / cao)
                3. Nguy cơ cao → cấy máu/xét nghiệm → KS TM phổ rộng ngay (Pip-Tazo, Cefepime, Meropenem...), nhập viện, ICU nếu shock
                4. Nguy cơ thấp → cấy máu/xét nghiệm → có thể KS uống chọn lọc + theo dõi sát, chỉ ngoại trú khi rất thấp nguy cơ

                **📚 Dựa trên:**
                - IDSA Clinical Practice Guideline for Use of Antimicrobial Agents in Neutropenic Patients with Cancer
                - ASCO/ESMO Guidelines on Management of Febrile Neutropenia
                """)
            elif selected_algorithm == "Acute Pancreatitis":
                st.markdown("""
                **Acute Pancreatitis Algorithm:**

                1. Nghi viêm tụy cấp: đau thượng vị điển hình, amylase/lipase >3x, hình ảnh phù hợp (≥2/3 tiêu chuẩn)
                2. Xác định chẩn đoán → bù dịch tích cực, giảm đau, nhịn ăn sớm
                3. Phân loại mức độ: nhẹ (không suy tạng), trung bình (suy tạng thoáng qua/biến chứng nhẹ), nặng (suy tạng kéo dài >48h)
                4. Tìm và điều trị nguyên nhân (sỏi mật, rượu, tăng TG, thuốc...)
                5. Nhập khoa tiêu hóa/nội tổng quát hoặc ICU nếu suy tạng/huyết động không ổn

                **📚 Dựa trên:**
                - IAP/APA Guidelines for Management of Acute Pancreatitis
                - ACG Clinical Guideline: Management of Acute Pancreatitis
                """)
            elif selected_algorithm == "Acute Chest Pain / ACS":
                st.markdown("""
                **Acute Chest Pain / ACS Algorithm:**
                
                1. Đau ngực cấp
                2. ECG ngay lập tức
                3. STEMI → Cath Lab (PCI)
                4. Không STEMI → Troponin
                5. Troponin (+) → Monitor & Reassess
                6. Troponin (-) → Cân nhắc xuất viện
                
                **📚 Dựa trên:**
                - AHA/ACC Guidelines for Management of Patients with STEMI (2023)
                - ESC Guidelines for Management of Acute Coronary Syndromes (2023)
                - AHA/ACC/ASE/CHEST/SAEM/SCCT/SCMR Guideline for Evaluation and Diagnosis of Chest Pain (2021)
                """)
            elif selected_algorithm == "Shock / Hypotension":
                st.markdown("""
                **Shock / Hypotension Resuscitation Algorithm:**
                
                1. SBP <90 hoặc MAP <65
                2. Airway & Breathing
                3. 2 đường IV lớn + lấy xét nghiệm
                4. Bolus dịch 30 ml/kg Crystalloid
                5. Đáp ứng với dịch?
                   - Có → Theo dõi & tìm nguyên nhân
                   - Không / Phù phổi → Bắt đầu Vasopressor (Noradrenaline)
                6. Phân loại shock: Septic / Cardiogenic / Hypovolemic / Obstructive
                7. ICU / Theo dõi sát (MAP, Lactate, UO)
                
                **📚 Dựa trên:**
                - **Surviving Sepsis Campaign (SSC) Guidelines 2021** - International Guidelines for Management of Sepsis and Septic Shock
                - **ACLS (Advanced Cardiac Life Support) Protocol** - AHA Guidelines
                - **ATLS (Advanced Trauma Life Support)** - Shock Management Module
                - **ESC/ESICM Guidelines** on Shock Management
                - **SCCM (Society of Critical Care Medicine)** Guidelines
                """)
            elif selected_algorithm == "Upper GI Bleeding":
                st.markdown("""
                **Upper GI Bleeding Initial Management Algorithm:**
                
                1. Nghi ngờ XHTH trên
                2. Resuscitation: Airway, 2 đường IV, Bolus dịch
                3. Đánh giá huyết động & nguy cơ cao
                4. **Nguy cơ cao:**
                   - Truyền máu PRBC (đích Hb ≥7-8 g/dL)
                   - Bolus + truyền PPI (Esomeprazole)
                   - Nội soi trong 12-24h
                5. **Nguy cơ thấp:**
                   - PPI đơn thuần
                   - Nội soi theo hẹn
                6. Nhập viện/ICU hoặc điều trị ngoại trú
                
                **📚 Dựa trên:**
                - **ACG (American College of Gastroenterology) Clinical Guideline: Management of Acute Upper GI Bleeding 2021**
                - **AASLD (American Association for the Study of Liver Diseases)** Practice Guidelines on Management of Variceal Bleeding
                - **BSG (British Society of Gastroenterology)** Guidelines for Management of Upper GI Bleeding (2021)
                - **International Consensus Recommendations** on Management of Upper GI Bleeding
                - **ESGE (European Society of Gastrointestinal Endoscopy)** Guidelines
                """)
            elif selected_algorithm == "DKA Initial Management":
                st.markdown("""
                **DKA Initial Management Algorithm:**
                
                1. Nghi ngờ DKA
                2. Lấy xét nghiệm: Glucose, ABG/VBG, Điện giải, Ketone
                3. Chẩn đoán DKA: Glucose >250, pH <7.3, HCO₃⁻ <18, Ketone (+)
                4. Bolus NS 0.9% 15-20 ml/kg (1-1.5L)
                5. Bắt đầu Insulin IV 0.1 U/kg/h
                6. Đánh giá K⁺ và bổ sung nếu cần
                7. Theo dõi: Glucose, K⁺, pH, Anion gap
                8. DKA giải quyết (pH >7.3, HCO₃⁻ >18, Anion gap đóng) → Chuyển sang SC Insulin + ăn uống
                
                **📚 Dựa trên:**
                - **ADA (American Diabetes Association) Standards of Medical Care in Diabetes 2024**
                - **ISPAD (International Society for Pediatric and Adolescent Diabetes)** Clinical Practice Consensus Guidelines 2022
                - **Joint British Diabetes Societies (JBDS)** Guidelines for Management of DKA (2021)
                - **Endocrine Society Clinical Practice Guideline** on Diabetic Ketoacidosis and Hyperosmolar Hyperglycemic State
                - **AACE/ACE Consensus Statement** on Type 1 Diabetes Management
                """)

elif selected_feature == feature_options[1]:
    st.header("🤰 An toàn thai kỳ & cho con bú")
    st.caption("Thông tin an toàn thai kỳ và cho con bú cho thuốc")
    
    # Drug search
    from drugs.pregnancy_lactation_safety import PREGNANCY_SAFETY, LACTATION_SAFETY
    
    all_drugs = sorted(set(list(PREGNANCY_SAFETY.keys()) + list(LACTATION_SAFETY.keys())))
    
    selected_drug = st.selectbox(
        "Chọn thuốc:",
        all_drugs,
        key="pregnancy_drug_selector"
    )
    
    if selected_drug:
        render_pregnancy_lactation_section(selected_drug)
    
    # Add new drug form
    st.markdown("---")
    with st.expander("➕ Thêm thuốc mới (Admin)"):
        st.info("💡 Tính năng này sẽ được mở rộng để thêm thuốc mới vào database.")

elif selected_feature == feature_options[2]:
    render_pediatric_dosing_calculator()

# Footer
render_standard_footer()

