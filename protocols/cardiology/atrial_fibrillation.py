"""
Atrial Fibrillation Management Protocol
AHA/ACC/HRS 2019, ESC 2020
Acute and chronic atrial fibrillation management
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Atrial Fibrillation Management Protocol"""
    st.subheader("💓 Rung Nhĩ (Atrial Fibrillation)")
    st.caption("ESC 2020 / ACC/AHA/ACCP/HRS 2023 - Early Rhythm Control Priority")
    
    st.info("""
    **Cập nhật quan trọng (2024):**
    - **ABC Pathway:** Anticoagulation (Chống đông), Better symptom control (Kiểm soát triệu chứng), Comorbidities (Bệnh đồng mắc).
    - **Early Rhythm Control:** Ưu tiên khôi phục nhịp sớm (Ablation/Antiarrhythmic) cho bệnh nhân mới chẩn đoán (<1 năm) để cải thiện tiên lượng.
    - **Catheter Ablation:** First-line cho một số nhóm bệnh nhân (suy tim HFrEF).
    """)
    
    st.info("""
    **Rung nhĩ (AF) là gì:**
    - Rối loạn nhịp tim phổ biến nhất
    - Tần suất: ~1% dân số, tăng theo tuổi
    - Nguy cơ: Đột quỵ, suy tim, tử vong
    
    **Phân loại:**
    - **Paroxysmal:** Tự hết <7 ngày
    - **Persistent:** >7 ngày hoặc cần cardioversion
    - **Long-standing persistent:** >12 tháng
    - **Permanent:** Quyết định không điều trị
    """)
    
    st.markdown("---")
    
    st.markdown("### 📋 Chẩn đoán")
    
    with st.expander("🔍 Tiêu chuẩn chẩn đoán", expanded=True):
        st.markdown("""
        **ECG:**
        - Không có sóng P
        - Sóng f (fibrillation waves)
        - RR interval không đều
        - Tần số thất: 100-180 bpm (không điều trị)
        
        **Triệu chứng:**
        - Hồi hộp, đánh trống ngực
        - Khó thở, mệt mỏi
        - Đau ngực, chóng mặt
        - Có thể không có triệu chứng
        """)
    
    st.markdown("---")
    
    st.markdown("### 🎯 Chiến Lược Điều trị (ABC Pathway)")
    
    strategy = st.radio(
        "**Chiến lược điều trị:**",
        [
            "A - Anticoagulation (Tránh đột quỵ)",
            "B - Better Symptom Control (Rate/Rhythm)",
            "C - Comorbidities (Quản lý bệnh nền)",
            "Rung nhĩ cấp với RVR (Cấp cứu)"
        ],
        key="af_strategy"
    )
    
    st.markdown("---")
    
    if "Anticoagulation" in strategy:
        render_anticoagulation()
    elif "Better Symptom" in strategy:
        control_type = st.radio("Chọn phương pháp:", ["Kiểm soát Nhịp (Rhythm Control - Ưu tiên)", "Kiểm soát Tần số (Rate Control)"], horizontal=True)
        if "Rhythm" in control_type:
            render_rhythm_control()
        else:
            render_rate_control()
    elif "Comorbidities" in strategy:
        render_comorbidities()
    elif "RVR" in strategy or "cấp" in strategy:
        render_acute_af_rvr()
    
    st.markdown("---")
    
    st.markdown("### 📊 Đánh giá nguy cơ")
    
    st.info("""
    **CHADS₂-VASc Score (Nguy cơ đột quỵ):**
    - **C:** Congestive heart failure (1 điểm)
    - **H:** Hypertension (1 điểm)
    - **A:** Age ≥75 (2 điểm), 65-74 (1 điểm)
    - **D:** Diabetes (1 điểm)
    - **S₂:** Stroke/TIA (2 điểm)
    - **V:** Vascular disease (1 điểm)
    - **Sc:** Sex (Female) (1 điểm)
    
    **Điểm số:**
    - **0:** Nguy cơ thấp - Aspirin hoặc không điều trị
    - **1:** Nguy cơ thấp-trung bình - DOAC hoặc warfarin
    - **≥2:** Nguy cơ cao - DOAC hoặc warfarin (ưu tiên DOAC)
    
    **HAS-BLED Score (Nguy cơ chảy máu):**
    - **H:** Hypertension (1 điểm)
    - **A:** Abnormal renal/liver (1 điểm mỗi)
    - **S:** Stroke (1 điểm)
    - **B:** Bleeding history (1 điểm)
    - **L:** Labile INR (1 điểm)
    - **E:** Elderly >65 (1 điểm)
    - **D:** Drugs/alcohol (1 điểm mỗi)
    
    **Điểm ≥3:** Nguy cơ chảy máu cao - Cần cân nhắc cẩn thận
    """)
    
    st.markdown("---")
    
    st.markdown("### 💊 Thuốc Kiểm soát Tần Số")
    
    st.warning("""
    **Mục tiêu:** Tần số thất 60-100 bpm (nghỉ ngơi), <110 bpm (vận động nhẹ)
    
    **1. Beta Blockers (Ưu tiên):**
    - **Metoprolol:** 25-100 mg PO bid
    - **Atenolol:** 25-100 mg PO qd
    - **Propranolol:** 10-40 mg PO tid
    
    **2. Non-DHP Calcium Channel Blockers:**
    - **Diltiazem:** 120-360 mg PO qd (ER)
    - **Verapamil:** 120-360 mg PO qd (ER)
    
    **3. Digoxin:**
    - **Liều:** 0.125-0.25 mg PO qd
    - **Dùng khi:** Suy tim, không vận động nhiều
    - **Theo dõi:** Nồng độ digoxin, chức năng thận
    
    **4. Amiodarone:**
    - **Liều:** 200-400 mg PO qd
    - **Dùng khi:** Các thuốc khác không hiệu quả
    - **Cảnh báo:** Nhiều tác dụng phụ
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚡ Khôi Phục Nhịp (Cardioversion)")
    
    st.info("""
    **Chỉ định:**
    - Rung nhĩ mới (<48 giờ) có triệu chứng
    - Rung nhĩ persistent có triệu chứng
    - Suy tim do rung nhĩ
    
    **Chống chỉ định:**
    - Rung nhĩ >48 giờ không chống đông đủ
    - Huyết khối nhĩ trái (cần TEE)
    - Digoxin toxicity
    
    **Phương pháp:**
    1. **Điện (Electrical Cardioversion):**
       - Năng lượng: 100-200 J (biphasic)
       - Tỷ lệ thành công: 70-90%
       - Cần gây mê ngắn
    
    2. **Thuốc (Chemical Cardioversion):**
       - **Flecainide:** 200-300 mg PO (pill-in-pocket)
       - **Propafenone:** 600 mg PO
       - **Amiodarone:** 400-800 mg PO qd x 2 tuần
       - **Ibutilide:** 1 mg IV (cần theo dõi 4 giờ)
    """)
    
    st.markdown("---")
    
    st.markdown("### 🩸 Chống đông")
    
    st.error("""
    **DOACs (Ưu tiên):**
    - **Apixaban:** 5 mg PO bid (2.5 mg nếu ≥2 trong: tuổi ≥80, cân nặng ≤60 kg, Cr ≥1.5)
    - **Rivaroxaban:** 20 mg PO qd (15 mg nếu CrCl 15-50)
    - **Edoxaban:** 60 mg PO qd (30 mg nếu CrCl 15-50 hoặc ≤60 kg)
    - **Dabigatran:** 150 mg PO bid (110 mg nếu nguy cơ chảy máu cao)
    
    **Warfarin:**
    - **Liều:** 2-10 mg PO qd (điều chỉnh theo INR)
    - **Mục tiêu INR:** 2.0-3.0
    - **Theo dõi:** INR hàng tuần đến ổn định
    
    **Aspirin:**
    - Chỉ dùng khi CHADS₂-VASc = 0
    - Không khuyến nghị trong hầu hết trường hợp
    """)
    
    st.markdown("---")
    
    st.markdown("### 📋 Danh sách kiểm tra điều trị")
    
    checklist_items = [
        "✅ ECG xác nhận rung nhĩ",
        "✅ Đánh giá CHADS₂-VASc và HAS-BLED",
        "✅ Quyết định rate vs rhythm control",
        "✅ Chống đông nếu CHADS₂-VASc ≥1",
        "✅ Kiểm soát tần số nếu rate control",
        "✅ Cardioversion nếu rhythm control",
        "✅ Điều trị nguyên nhân (suy tim, cường giáp, v.v.)",
        "✅ Theo dõi triệu chứng, ECG"
    ]
    
    for item in checklist_items:
        st.markdown(f"- {item}")
    
    st.markdown("---")
    
    st.markdown("### 👥 Nhóm bệnh nhân đặc biệt")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Người cao tuổi:**
        - Bắt đầu với liều thấp
        - Cẩn thận với chống đông (nguy cơ té ngã)
        - Ưu tiên rate control
        
        **Suy tim:**
        - Digoxin có thể hữu ích
        - Tránh verapamil, diltiazem nếu EF thấp
        - Rhythm control có thể cải thiện triệu chứng
        """)
    
    with col2:
        st.markdown("""
        **Có thai:**
        - Beta blocker an toàn (metoprolol)
        - Tránh warfarin (teratogenic)
        - DOAC không khuyến nghị
        - Heparin/LMWH nếu cần chống đông
        
        **Suy thận:**
        - Điều chỉnh liều DOAC theo CrCl
        - Warfarin không cần điều chỉnh
        - Tránh dabigatran nếu CrCl <30
        """)
    
    st.markdown("---")
    
    # References section
    references = get_references("Atrial Fibrillation")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")


def render_rate_control():
    """Rate control strategy"""
    st.success("## 🟢 Kiểm soát Tần Số")
    
    st.markdown("""
    **Chỉ định:**
    - Rung nhĩ không triệu chứng
    - Người cao tuổi
    - Rung nhĩ lâu năm
    - Không thể duy trì nhịp xoang
    
    **Mục tiêu:**
    - Tần số thất: 60-100 bpm (nghỉ ngơi)
    - <110 bpm (vận động nhẹ)
    
    **Thuốc:**
    1. **Beta blocker:** Metoprolol 25-100 mg bid
    2. **Diltiazem:** 120-360 mg qd (ER)
    3. **Digoxin:** 0.125-0.25 mg qd (nếu suy tim)
    
    **Theo dõi:** ECG, triệu chứng, chức năng thận
    """)


def render_rhythm_control():
    """Rhythm control strategy"""
    st.success("## 🟡 Khôi Phục Nhịp (Rhythm Control)")
    st.caption("Ưu tiên cho: Mới chẩn đoán (<1 năm), Trẻ tuổi, Suy tim, Có triệu chứng")
    
    st.markdown("""
    **Chiến lược sớm (Early Rhythm Control):**
    - Giảm biến cố tim mạch và đột quỵ ở bệnh nhân rung nhĩ mới chẩn đoán.
    
    **Phương pháp:**
    1. **Catheter Ablation (Triệt đốt qua catheter):**
       - **Class I:** Suy tim HFrEF (cải thiện tử vong), Rung nhĩ paroxysmal có triệu chứng (thất bại thuốc).
       - **Class IIa:** First-line cho Rung nhĩ paroxysmal.
    
    2. **Cardioversion (Sốc điện/Thuốc):**
       - Điện: 100-200 J (đồng bộ)
       - Thuốc: Flecainide, Amiodarone, Propafenone (Pill-in-pocket)
       - **Lưu ý:** Cần loại trừ huyết khối tiểu nhĩ trái (TEE) nếu >48h.
    
    3. **Thuốc chống loạn nhịp (Antiarrhythmic Drugs - AAD):**
       - **Không bệnh tim cấu trúc:** Flecainide, Propafenone
       - **Có suy tim/CAD:** Amiodarone
       - **Sotalol:** Cần theo dõi QT
    """)


def render_anticoagulation():
    """Anticoagulation strategy"""
    st.error("## 🔴 Chống đông")
    
    st.markdown("""
    **CHADS₂-VASc ≥1:** Cần chống đông
    
    **DOACs (Ưu tiên):**
    - Apixaban 5 mg bid
    - Rivaroxaban 20 mg qd
    - Edoxaban 60 mg qd
    - Dabigatran 150 mg bid
    
    **Warfarin:**
    - Mục tiêu INR: 2.0-3.0
    - Dùng khi: Van cơ học, hẹp van 2 lá
    
    **Theo dõi:**
    - Chức năng thận (DOAC)
    - INR (warfarin)
    - Dấu hiệu chảy máu
    """)


def render_acute_af_rvr():
    """Acute AF with rapid ventricular response"""
    st.error("## 🔴 Rung Nhĩ Cấp Với RVR - Cấp cứu")
    
    st.markdown("""
    **Triệu chứng:**
    - Tần số thất >150 bpm
    - Hạ huyết áp, suy tim
    - Đau ngực, khó thở
    
    **Điều trị ngay:**
    1. **Nếu không ổn định huyết động:**
       - Cardioversion ngay (100-200 J)
    
    2. **Nếu ổn định:**
       - **Diltiazem:** 0.25 mg/kg IV bolus, sau đó 5-15 mg/h
       - **Hoặc:** Metoprolol 5 mg IV q5min x 3
       - **Hoặc:** Esmolol 500 mcg/kg bolus, sau đó 50-300 mcg/kg/min
    
    3. **Digoxin:** 0.25-0.5 mg IV (nếu suy tim)
    
    4. **Amiodarone:** 150 mg IV bolus, sau đó 1 mg/min x 6h
    
    **Mục tiêu:** Tần số thất <100 bpm
    
    **Theo dõi:** ECG liên tục, huyết áp
    """)

def render_comorbidities():
    """Manage comorbidities (C in ABC pathway)"""
    st.info("## 🔵 Quản lý Bệnh Đồng Mắc (Comorbidities)")
    st.markdown("""
    **Tối ưu hóa điều trị các yếu tố nguy cơ:**
    - **Hypertension:** Kiểm soát HA tốt.
    - **Heart Failure:** Điều trị nội khoa tối ưu (GDMT).
    - **Diabetes:** Kiểm soát đường huyết.
    - **Obesity:** Giảm cân (giảm >10% cân nặng giúp giảm gánh nặng rung nhĩ).
    - **Sleep Apnea:** Tầm soát và điều trị CPAP.
    - **Alcohol:** Hạn chế hoặc ngừng rượu bia.
    """)

