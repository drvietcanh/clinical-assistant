"""
Emergency Protocols for Critical Care
Rapid Sequence Intubation (RSI), Code Blue/CPR, Difficult Airway Management
"""

import streamlit as st
from components.ui.results import render_result_box, render_result_card
from components.ui.alerts import render_info_alert, render_warning_alert, render_error_alert
from typing import Dict, List


# RSI Drug Dosing
RSI_DRUGS = {
    "Induction": {
        "Etomidate": {
            "dose": "0.3 mg/kg IV",
            "range": "0.2-0.4 mg/kg",
            "notes": "An toàn cho huyết động không ổn định, có thể gây ức chế thượng thận"
        },
        "Propofol": {
            "dose": "1.5-2.5 mg/kg IV",
            "range": "1-3 mg/kg",
            "notes": "Gây hạ huyết áp, tránh dùng khi sốc"
        },
        "Ketamine": {
            "dose": "1-2 mg/kg IV",
            "range": "0.5-2 mg/kg",
            "notes": "Tốt cho sốc, tăng huyết áp, có thể gây ảo giác"
        },
        "Midazolam": {
            "dose": "0.1-0.2 mg/kg IV",
            "range": "0.05-0.3 mg/kg",
            "notes": "Tác dụng kéo dài, tránh dùng khi suy thận"
        }
    },
    "Paralytic": {
        "Succinylcholine": {
            "dose": "1-1.5 mg/kg IV",
            "range": "1-2 mg/kg",
            "notes": "Tác dụng nhanh (30-60s), ngắn (5-10 phút), chống chỉ định: tăng K+, MH, bỏng >48h"
        },
        "Rocuronium": {
            "dose": "0.6-1.2 mg/kg IV",
            "range": "0.6-1.2 mg/kg",
            "notes": "Tác dụng nhanh (60-90s), kéo dài (30-60 phút), an toàn hơn succinylcholine"
        },
        "Vecuronium": {
            "dose": "0.1 mg/kg IV",
            "range": "0.08-0.1 mg/kg",
            "notes": "Tác dụng chậm hơn, kéo dài (30-60 phút)"
        }
    },
    "Premedication": {
        "Lidocaine": {
            "dose": "1.5 mg/kg IV",
            "range": "1-2 mg/kg",
            "notes": "Giảm phản ứng huyết động, dùng trước 2-3 phút"
        },
        "Fentanyl": {
            "dose": "2-3 mcg/kg IV",
            "range": "1-5 mcg/kg",
            "notes": "Giảm phản ứng huyết động, dùng trước 2-3 phút"
        },
        "Atropine": {
            "dose": "0.01-0.02 mg/kg IV",
            "range": "0.01-0.02 mg/kg",
            "notes": "Chỉ dùng cho trẻ em <10 tuổi để tránh nhịp chậm"
        }
    }
}


# Code Blue Drugs
CODE_BLUE_DRUGS = {
    "Epinephrine": {
        "dose_vfib_vt": "1 mg IV/IO mỗi 3-5 phút",
        "dose_alternative": "0.1 mg/kg IV/IO (nếu không đáp ứng)",
        "dose_peds": "0.01 mg/kg (0.1 mL/kg 1:10,000) IV/IO",
        "notes": "Thuốc đầu tiên trong VF/VT, có thể dùng qua nội khí quản (2-2.5 mg pha loãng)"
    },
    "Amiodarone": {
        "dose_first": "300 mg IV/IO bolus",
        "dose_repeat": "150 mg IV/IO (nếu cần)",
        "dose_peds": "5 mg/kg IV/IO",
        "notes": "Dùng sau epinephrine trong VF/VT kháng trị"
    },
    "Lidocaine": {
        "dose": "1-1.5 mg/kg IV/IO",
        "dose_repeat": "0.5-0.75 mg/kg mỗi 5-10 phút",
        "dose_peds": "1 mg/kg IV/IO",
        "notes": "Thay thế amiodarone nếu không có sẵn"
    },
    "Atropine": {
        "dose": "1 mg IV/IO",
        "dose_repeat": "1 mg (tối đa 3 mg)",
        "dose_peds": "0.02 mg/kg IV/IO",
        "notes": "Dùng cho nhịp chậm, PEA, asystole"
    },
    "Calcium": {
        "dose": "1 g (10 mL 10% CaCl2) hoặc 3 g (10 mL 10% CaGluconate) IV",
        "notes": "Chỉ dùng khi có tăng K+, hạ Ca++, hoặc quá liều Ca++ channel blocker"
    },
    "Magnesium": {
        "dose": "1-2 g IV (pha loãng trong 10 mL D5W)",
        "notes": "Dùng cho torsades de pointes hoặc hạ Mg++"
    },
    "Sodium Bicarbonate": {
        "dose": "1 mEq/kg IV",
        "notes": "Chỉ dùng khi có nhiễm toan nặng đã biết, tăng K+, hoặc quá liều TCA"
    }
}


def calculate_rsi_dose(weight_kg: float, drug: str, category: str) -> Dict:
    """Calculate RSI drug dose based on weight"""
    if category not in RSI_DRUGS or drug not in RSI_DRUGS[category]:
        return None
    
    drug_info = RSI_DRUGS[category][drug]
    dose_str = drug_info["dose"]
    
    # Extract dose per kg
    if "mg/kg" in dose_str:
        dose_per_kg = float(dose_str.split()[0])
        total_dose = dose_per_kg * weight_kg
        return {
            "drug": drug,
            "dose_per_kg": dose_per_kg,
            "total_dose": total_dose,
            "unit": "mg",
            "range": drug_info["range"],
            "notes": drug_info["notes"]
        }
    elif "mcg/kg" in dose_str:
        dose_per_kg = float(dose_str.split()[0])
        total_dose = dose_per_kg * weight_kg
        return {
            "drug": drug,
            "dose_per_kg": dose_per_kg,
            "total_dose": total_dose,
            "unit": "mcg",
            "range": drug_info["range"],
            "notes": drug_info["notes"]
        }
    
    return None


def render_rsi_protocol():
    """Render Rapid Sequence Intubation protocol"""
    st.header("🚨 Rapid Sequence Intubation (RSI)")
    st.caption("Protocol đặt nội khí quản nhanh cho bệnh nhân cấp cứu")
    
    st.markdown("""
    **RSI** là kỹ thuật đặt nội khí quản với mục tiêu:
    - Đảm bảo an toàn đường thở
    - Giảm thiểu nguy cơ hít sặc
    - Tối ưu hóa điều kiện đặt nội khí quản
    """)
    
    st.markdown("---")
    
    # Patient information
    st.markdown("### 📋 Thông tin bệnh nhân")
    col1, col2 = st.columns(2)
    
    with col1:
        weight = st.number_input("Cân nặng (kg):", min_value=0.0, value=70.0, key="rsi_weight")
        age = st.number_input("Tuổi:", min_value=0, max_value=150, value=50, key="rsi_age")
    
    with col2:
        indication = st.selectbox(
            "Chỉ định:",
            ["Bảo vệ đường thở", "Suy hô hấp", "Sốc", "Chấn thương", "Khác"],
            key="rsi_indication"
        )
        difficult_airway = st.checkbox("Đường thở khó (LEMON dương tính)", key="rsi_difficult")
    
    st.markdown("---")
    
    # Pre-intubation checklist
    st.markdown("### ✅ Checklist trước RSI")
    
    checklist_items = [
        ("Đánh giá đường thở (LEMON)", "difficult_airway"),
        ("Chuẩn bị thiết bị (lưỡi đè, ống NKQ, máy hút)", "equipment"),
        ("Kiểm tra monitor (SpO2, ECG, NIBP)", "monitor"),
        ("Thiết lập đường truyền tĩnh mạch", "iv_access"),
        ("Chuẩn bị thuốc (induction, paralytic)", "drugs"),
        ("Chuẩn bị thiết bị dự phòng (LMA, bougie)", "backup"),
        ("Pre-oxygenation (100% O2, 3-5 phút)", "preoxygen"),
        ("Đặt tư thế (sniffing position)", "position")
    ]
    
    checklist_state = {}
    cols = st.columns(4)
    for idx, (item, key) in enumerate(checklist_items):
        with cols[idx % 4]:
            checklist_state[key] = st.checkbox(item, key=f"rsi_check_{key}")
    
    if all(checklist_state.values()):
        st.success("✅ Tất cả checklist đã hoàn thành. Sẵn sàng cho RSI.")
    else:
        missing = [item for item, key in checklist_items if not checklist_state.get(key)]
        st.warning(f"⚠️ Còn thiếu: {', '.join(missing)}")
    
    st.markdown("---")
    
    # Drug selection and dosing
    st.markdown("### 💉 Thuốc RSI")
    
    drug_tabs = st.tabs(["Induction", "Paralytic", "Premedication"])
    
    # Tab 1: Induction
    with drug_tabs[0]:
        st.markdown("**Thuốc gây mê:**")
        induction_drug = st.selectbox(
            "Chọn thuốc:",
            list(RSI_DRUGS["Induction"].keys()),
            key="rsi_induction"
        )
        
        if induction_drug:
            drug_info = RSI_DRUGS["Induction"][induction_drug]
            dose_calc = calculate_rsi_dose(weight, induction_drug, "Induction")
            
            if dose_calc:
                col1, col2 = st.columns(2)
                with col1:
                    render_result_card(
                        title=f"{induction_drug}",
                        value=f"{dose_calc['total_dose']:.1f}",
                        unit=dose_calc['unit'],
                        color="info",
                        subtitle=f"Liều: {dose_calc['dose_per_kg']:.2f} {dose_calc['unit']}/kg"
                    )
                
                with col2:
                    st.markdown(f"""
                    **Khoảng liều:** {drug_info['range']}  
                    **Ghi chú:** {drug_info['notes']}
                    """)
    
    # Tab 2: Paralytic
    with drug_tabs[1]:
        st.markdown("**Thuốc giãn cơ:**")
        paralytic_drug = st.selectbox(
            "Chọn thuốc:",
            list(RSI_DRUGS["Paralytic"].keys()),
            key="rsi_paralytic"
        )
        
        if paralytic_drug:
            drug_info = RSI_DRUGS["Paralytic"][paralytic_drug]
            dose_calc = calculate_rsi_dose(weight, paralytic_drug, "Paralytic")
            
            if dose_calc:
                col1, col2 = st.columns(2)
                with col1:
                    render_result_card(
                        title=f"{paralytic_drug}",
                        value=f"{dose_calc['total_dose']:.1f}",
                        unit=dose_calc['unit'],
                        color="warning",
                        subtitle=f"Liều: {dose_calc['dose_per_kg']:.2f} {dose_calc['unit']}/kg"
                    )
                
                with col2:
                    st.markdown(f"""
                    **Khoảng liều:** {drug_info['range']}  
                    **Ghi chú:** {drug_info['notes']}
                    """)
                    
                    if paralytic_drug == "Succinylcholine":
                        st.warning("""
                        **Chống chỉ định:**
                        - Tăng K+ (>5.5 mEq/L)
                        - Malignant hyperthermia
                        - Bỏng >48 giờ
                        - Chấn thương cơ lớn
                        - Bệnh thần kinh cơ
                        """)
    
    # Tab 3: Premedication
    with drug_tabs[2]:
        st.markdown("**Thuốc tiền xử lý (tùy chọn):**")
        
        use_lidocaine = st.checkbox("Lidocaine (giảm phản ứng huyết động)", key="rsi_lido")
        use_fentanyl = st.checkbox("Fentanyl (giảm phản ứng huyết động)", key="rsi_fent")
        use_atropine = st.checkbox("Atropine (chỉ trẻ em <10 tuổi)", key="rsi_atro")
        
        if use_lidocaine:
            dose_calc = calculate_rsi_dose(weight, "Lidocaine", "Premedication")
            if dose_calc:
                st.info(f"**Lidocaine:** {dose_calc['total_dose']:.1f} {dose_calc['unit']} IV (dùng trước 2-3 phút)")
        
        if use_fentanyl:
            dose_calc = calculate_rsi_dose(weight, "Fentanyl", "Premedication")
            if dose_calc:
                st.info(f"**Fentanyl:** {dose_calc['total_dose']:.1f} {dose_calc['unit']} IV (dùng trước 2-3 phút)")
        
        if use_atropine and age < 10:
            dose_calc = calculate_rsi_dose(weight, "Atropine", "Premedication")
            if dose_calc:
                st.info(f"**Atropine:** {dose_calc['total_dose']:.1f} {dose_calc['unit']} IV")
        elif use_atropine and age >= 10:
            st.warning("Atropine chỉ dùng cho trẻ em <10 tuổi")
    
    st.markdown("---")
    
    # RSI Sequence
    st.markdown("### 📋 Trình tự RSI")
    
    rsi_steps = [
        ("1. Pre-oxygenation", "100% O2, 3-5 phút, hoặc 8 nhịp thở sâu"),
        ("2. Premedication (nếu cần)", "Lidocaine, Fentanyl (2-3 phút trước)"),
        ("3. Induction", f"{induction_drug if 'induction_drug' in locals() else 'Chọn thuốc'} - Tiêm nhanh"),
        ("4. Cricoid pressure", "Áp lực nhẹ (10N), bỏ khi khó đặt"),
        ("5. Paralytic", f"{paralytic_drug if 'paralytic_drug' in locals() else 'Chọn thuốc'} - Tiêm nhanh"),
        ("6. Đợi giãn cơ", "30-60 giây (succinylcholine) hoặc 60-90 giây (rocuronium)"),
        ("7. Đặt nội khí quản", "Laryngoscope, xác nhận vị trí"),
        ("8. Xác nhận", "Nghe phổi, capnography, CXR"),
        ("9. Cố định", "Cố định ống NKQ, ghi chú độ sâu"),
        ("10. Post-intubation", "Cài đặt máy thở, an thần tiếp tục")
    ]
    
    for step, description in rsi_steps:
        st.markdown(f"**{step}:** {description}")
    
    st.markdown("---")
    
    # Post-intubation ventilator settings
    st.markdown("### 🫁 Cài đặt máy thở sau RSI")
    
    st.info("""
    **Cài đặt ban đầu:**
    - Mode: AC hoặc VC
    - Tidal Volume: 6-8 mL/kg IBW
    - RR: 12-16 /min
    - PEEP: 5-10 cmH2O
    - FiO2: 100% → giảm dần theo SpO2
    - I:E: 1:2
    
    **Đánh giá sau 30 phút:**
    - ABG
    - Compliance
    - Plateau pressure
    - Điều chỉnh theo kết quả
    """)
    
    if st.button("🫁 Mở Ventilator Calculator", use_container_width=True):
        st.session_state['critical_care_tool_selection'] = "🫁 Ventilator Management"
        st.rerun()


def render_code_blue_protocol():
    """Render Code Blue / CPR protocol"""
    st.header("🚨 Code Blue / CPR Protocol")
    st.caption("Protocol hồi sức tim phổi theo ACLS Guidelines")
    
    st.markdown("""
    **Mục tiêu CPR:**
    - Duy trì tuần hoàn và oxy hóa
    - Xác định và điều trị nguyên nhân có thể đảo ngược
    - Phục hồi nhịp tim hiệu quả
    """)
    
    st.markdown("---")
    
    # Rhythm identification
    st.markdown("### 📊 Nhận diện nhịp")
    
    rhythm = st.selectbox(
        "Nhịp tim:",
        ["VF/VT (Rung thất/Nhịp nhanh thất)", "PEA (Hoạt động điện không mạch)", "Asystole (Vô tâm thu)", "Nhịp chậm"],
        key="code_rhythm"
    )
    
    st.markdown("---")
    
    # CPR Algorithm
    st.markdown("### 🔄 Algorithm CPR")
    
    if "VF/VT" in rhythm:
        st.markdown("""
        **VF/VT Protocol:**
        1. **Bắt đầu CPR** - 30:2 (hoặc continuous nếu có advanced airway)
        2. **Sốc điện** - 200J (monophasic) hoặc 120J (biphasic)
        3. **Epinephrine** - 1 mg IV/IO mỗi 3-5 phút
        4. **Sốc điện lại** - Sau mỗi 2 phút
        5. **Amiodarone** - 300 mg IV/IO (sau epinephrine đầu tiên)
        6. **Tiếp tục** - CPR → Sốc → Thuốc → Lặp lại
        """)
        
        st.error("⚡ **Ưu tiên:** Sốc điện ngay lập tức nếu có máy sốc điện sẵn sàng!")
    
    elif "PEA" in rhythm or "Asystole" in rhythm:
        st.markdown("""
        **PEA/Asystole Protocol:**
        1. **Bắt đầu CPR** - 30:2 (hoặc continuous)
        2. **Epinephrine** - 1 mg IV/IO mỗi 3-5 phút
        3. **Đánh giá nhịp** - Mỗi 2 phút
        4. **Tìm nguyên nhân** - H's và T's
        5. **Tiếp tục CPR** - Cho đến khi có nhịp hiệu quả hoặc ngừng hồi sức
        """)
        
        st.warning("⚠️ **Không sốc điện** cho PEA/Asystole!")
    
    elif "Nhịp chậm" in rhythm:
        st.markdown("""
        **Nhịp chậm Protocol:**
        1. **Đánh giá** - Có triệu chứng? (hạ huyết áp, ALOC, đau ngực)
        2. **Atropine** - 1 mg IV (lặp lại nếu cần, tối đa 3 mg)
        3. **Pacing** - Transcutaneous hoặc transvenous
        4. **Epinephrine** - 2-10 mcg/min IV infusion
        5. **Dopamine** - 2-10 mcg/kg/min IV infusion
        """)
    
    st.markdown("---")
    
    # H's and T's
    st.markdown("### 🔍 Nguyên nhân có thể đảo ngược (H's và T's)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **H's:**
        - **Hypovolemia** - Thiếu dịch
        - **Hypoxia** - Thiếu oxy
        - **Hydrogen ion (Acidosis)** - Nhiễm toan
        - **Hypo/Hyperkalemia** - Rối loạn K+
        - **Hypothermia** - Hạ thân nhiệt
        """)
    
    with col2:
        st.markdown("""
        **T's:**
        - **Tension pneumothorax** - Tràn khí màng phổi
        - **Tamponade** - Chèn ép tim
        - **Toxins** - Ngộ độc
        - **Thrombosis (PE)** - Thuyên tắc phổi
        - **Thrombosis (MI)** - Nhồi máu cơ tim
        """)
    
    st.markdown("---")
    
    # Drug dosing
    st.markdown("### 💉 Liều thuốc Code Blue")
    
    weight = st.number_input("Cân nặng (kg):", min_value=0.0, value=70.0, key="code_weight")
    is_pediatric = st.checkbox("Bệnh nhân nhi", key="code_peds")
    
    drug_tabs = st.tabs(["Epinephrine", "Amiodarone", "Lidocaine", "Khác"])
    
    with drug_tabs[0]:
        st.markdown("**Epinephrine:**")
        if is_pediatric:
            dose = 0.01 * weight  # 0.01 mg/kg
            st.info(f"**Liều nhi:** {dose:.2f} mg IV/IO (0.1 mL/kg 1:10,000)")
        else:
            st.info("**Liều người lớn:** 1 mg IV/IO mỗi 3-5 phút")
            st.info("**Liều thay thế:** 0.1 mg/kg IV/IO (nếu không đáp ứng)")
        
        st.markdown(f"**Ghi chú:** {CODE_BLUE_DRUGS['Epinephrine']['notes']}")
    
    with drug_tabs[1]:
        st.markdown("**Amiodarone:**")
        if is_pediatric:
            dose = 5 * weight  # 5 mg/kg
            st.info(f"**Liều nhi:** {dose:.1f} mg IV/IO")
        else:
            st.info("**Liều đầu:** 300 mg IV/IO bolus")
            st.info("**Liều lặp lại:** 150 mg IV/IO (nếu cần)")
        
        st.markdown(f"**Ghi chú:** {CODE_BLUE_DRUGS['Amiodarone']['notes']}")
    
    with drug_tabs[2]:
        st.markdown("**Lidocaine:**")
        if is_pediatric:
            dose = 1 * weight  # 1 mg/kg
            st.info(f"**Liều nhi:** {dose:.1f} mg IV/IO")
        else:
            dose = 1.5 * weight  # 1-1.5 mg/kg
            st.info(f"**Liều người lớn:** {dose:.1f} mg IV/IO")
            st.info("**Liều lặp lại:** 0.5-0.75 mg/kg mỗi 5-10 phút")
        
        st.markdown(f"**Ghi chú:** {CODE_BLUE_DRUGS['Lidocaine']['notes']}")
    
    with drug_tabs[3]:
        st.markdown("**Các thuốc khác:**")
        
        for drug, info in [("Atropine", CODE_BLUE_DRUGS["Atropine"]), 
                          ("Calcium", CODE_BLUE_DRUGS["Calcium"]),
                          ("Magnesium", CODE_BLUE_DRUGS["Magnesium"]),
                          ("Sodium Bicarbonate", CODE_BLUE_DRUGS["Sodium Bicarbonate"])]:
            with st.expander(drug):
                st.markdown(f"**Liều:** {info.get('dose', info.get('dose_vfib_vt', 'N/A'))}")
                if 'dose_peds' in info:
                    st.markdown(f"**Liều nhi:** {info['dose_peds']}")
                st.markdown(f"**Ghi chú:** {info.get('notes', '')}")
    
    st.markdown("---")
    
    # Timing checklist
    st.markdown("### ⏱️ Timing Checklist")
    
    timing_items = [
        ("0 phút", "Nhận diện ngừng tim, bắt đầu CPR"),
        ("2 phút", "Đánh giá nhịp, sốc điện (nếu VF/VT), Epinephrine"),
        ("4 phút", "Đánh giá nhịp, sốc điện (nếu VF/VT), Amiodarone (nếu cần)"),
        ("6 phút", "Đánh giá nhịp, sốc điện (nếu VF/VT), Epinephrine"),
        ("Mỗi 2 phút", "Lặp lại: Đánh giá nhịp → Sốc (nếu VF/VT) → Thuốc")
    ]
    
    for time, action in timing_items:
        st.markdown(f"**{time}:** {action}")


def render_difficult_airway():
    """Render Difficult Airway Management protocol"""
    st.header("🚨 Quản lý đường thở khó")
    st.caption("LEMON assessment và chiến lược quản lý đường thở khó")
    
    st.markdown("---")
    
    # LEMON Assessment
    st.markdown("### 🔍 Đánh giá LEMON")
    st.markdown("""
    **LEMON** là công cụ đánh giá đường thở khó:
    - **L**ook externally
    - **E**valuate 3-3-2 rule
    - **M**allampati
    - **O**bstruction
    - **N**eck mobility
    """)
    
    lemon_scores = {}
    
    st.markdown("#### L - Look Externally")
    lemon_scores['look'] = st.selectbox(
        "Đặc điểm bên ngoài:",
        ["Bình thường", "Râu dài", "Răng giả", "Béo phì", "Ngắn cổ", "Chấn thương mặt"],
        key="lemon_look"
    )
    
    st.markdown("#### E - Evaluate 3-3-2 Rule")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        mouth_open = st.number_input("Mở miệng (ngón tay):", min_value=0, max_value=5, value=3, key="lemon_mouth")
        lemon_scores['mouth'] = "Đạt" if mouth_open >= 3 else "Không đạt"
    
    with col2:
        mentum_hyoid = st.number_input("Cằm - xương móng (ngón tay):", min_value=0, max_value=5, value=3, key="lemon_mentum")
        lemon_scores['mentum'] = "Đạt" if mentum_hyoid >= 3 else "Không đạt"
    
    with col3:
        thyroid_notch = st.number_input("Xương móng - hõm ức (ngón tay):", min_value=0, max_value=5, value=2, key="lemon_thyroid")
        lemon_scores['thyroid'] = "Đạt" if thyroid_notch >= 2 else "Không đạt"
    
    st.markdown("#### M - Mallampati")
    lemon_scores['mallampati'] = st.selectbox(
        "Phân loại Mallampati:",
        ["Class I - Thấy toàn bộ", "Class II - Thấy một phần", "Class III - Chỉ thấy mềm vòm", "Class IV - Không thấy gì"],
        key="lemon_mallampati"
    )
    
    st.markdown("#### O - Obstruction")
    lemon_scores['obstruction'] = st.selectbox(
        "Tắc nghẽn:",
        ["Không", "Nhẹ", "Trung bình", "Nặng"],
        key="lemon_obstruction"
    )
    
    st.markdown("#### N - Neck Mobility")
    lemon_scores['neck'] = st.selectbox(
        "Cử động cổ:",
        ["Bình thường", "Hạn chế nhẹ", "Hạn chế trung bình", "Cố định"],
        key="lemon_neck"
    )
    
    # Calculate LEMON score
    lemon_score = 0
    if "Không đạt" in lemon_scores.get('mouth', '') or "Không đạt" in lemon_scores.get('mentum', '') or "Không đạt" in lemon_scores.get('thyroid', ''):
        lemon_score += 1
    if "Class III" in lemon_scores.get('mallampati', '') or "Class IV" in lemon_scores.get('mallampati', ''):
        lemon_score += 1
    if lemon_scores.get('obstruction', '') != "Không":
        lemon_score += 1
    if "Hạn chế" in lemon_scores.get('neck', '') or "Cố định" in lemon_scores.get('neck', ''):
        lemon_score += 1
    if lemon_scores.get('look', '') != "Bình thường":
        lemon_score += 1
    
    st.markdown("---")
    
    # LEMON Score Interpretation
    st.markdown("### 📊 Kết quả LEMON")
    
    if lemon_score == 0:
        render_result_card(
            title="LEMON Score",
            value="0",
            unit="",
            color="success",
            subtitle="Đường thở dễ - Có thể đặt NKQ thông thường"
        )
    elif lemon_score <= 2:
        render_result_card(
            title="LEMON Score",
            value=str(lemon_score),
            unit="",
            color="warning",
            subtitle="Đường thở khó vừa - Chuẩn bị thiết bị dự phòng"
        )
    else:
        render_result_card(
            title="LEMON Score",
            value=str(lemon_score),
            unit="",
            color="error",
            subtitle="Đường thở khó nặng - Cần chiến lược đặc biệt"
        )
    
    st.markdown("---")
    
    # Difficult Airway Strategy
    st.markdown("### 🎯 Chiến lược đường thở khó")
    
    if lemon_score >= 3:
        st.error("""
        **Đường thở khó nặng - Khuyến nghị:**
        1. **Gọi hỗ trợ** - Bác sĩ gây mê, ENT
        2. **Chuẩn bị thiết bị:**
           - Video laryngoscope
           - Bougie
           - LMA / i-gel
           - Cricothyrotomy kit
        3. **Xem xét:**
           - Awake fiberoptic intubation
           - Surgical airway (nếu cần)
           - Không thử đặt NKQ nhiều lần
        """)
    elif lemon_score >= 1:
        st.warning("""
        **Đường thở khó vừa - Khuyến nghị:**
        1. **Chuẩn bị thiết bị dự phòng:**
           - Video laryngoscope
           - Bougie
           - LMA
        2. **Kỹ thuật:**
           - Positioning tốt
           - External laryngeal manipulation
           - Back-up plan rõ ràng
        """)
    else:
        st.success("""
        **Đường thở dễ - Có thể đặt NKQ thông thường:**
        - Chuẩn bị thiết bị chuẩn
        - Có back-up plan cơ bản
        """)
    
    st.markdown("---")
    
    # Backup plans
    st.markdown("### 🔄 Kế hoạch dự phòng")
    
    backup_options = [
        ("LMA / i-gel", "Đặt LMA nếu không đặt được NKQ, có thể thông khí qua LMA"),
        ("Bougie", "Dùng bougie để hỗ trợ đặt NKQ khó"),
        ("Video laryngoscope", "Cải thiện tầm nhìn, dễ đặt hơn"),
        ("Fiberoptic", "Đặt NKQ qua ống soi phế quản (cần bệnh nhân tỉnh hoặc an thần nhẹ)"),
        ("Surgical airway", "Cricothyrotomy hoặc tracheostomy (cuối cùng)")
    ]
    
    for option, description in backup_options:
        st.markdown(f"**{option}:** {description}")


def render_emergency_protocols():
    """Main function to render emergency protocols"""
    tabs = st.tabs([
        "🚨 RSI",
        "🚨 Code Blue",
        "🚨 Đường thở khó"
    ])
    
    with tabs[0]:
        render_rsi_protocol()
    
    with tabs[1]:
        render_code_blue_protocol()
    
    with tabs[2]:
        render_difficult_airway()
