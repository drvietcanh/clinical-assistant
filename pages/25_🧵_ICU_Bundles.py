"""
ICU & Nội Bundles
Curated workflows for common scenarios: Sepsis/Shock, Acute Dyspnea
"""

import streamlit as st
from utils.page_helper import setup_page, render_standard_footer
from components.ui import render_hero
from config.user_profile import get_current_profile, get_profile_label
from utils.analytics_events import track_page_view, track_feature_usage


setup_page(
    page_title="ICU & Nội Bundles",
    page_icon="🧵",
    description="Các workflow gộp sẵn cho Sepsis/Shock và Khó thở cấp",
)

profile = get_current_profile()

# Track page view
try:
    track_page_view("ICU_Bundles")
except Exception:
    pass

render_hero(
    title="🧵 ICU & Nội Bundles",
    subtitle=f"Workflow gộp sẵn cho {get_profile_label(profile)}",
    description=(
        "Tập trung các thang điểm, phác đồ và công cụ liên quan vào một nơi cho từng tình huống lâm sàng."
    ),
    icon="🧵",
    gradient=("#ff9a9e", "#fad0c4"),
)

tab_sepsis, tab_dyspnea = st.tabs(["🩸 Sepsis / Shock", "😮‍💨 Khó thở cấp"])


with tab_sepsis:
    st.markdown("### 🩸 Sepsis / Septic Shock Bundle")
    st.markdown(
        """
**Mục tiêu:** nhận diện sớm, resuscitation trong 1 giờ đầu, và theo dõi đáp ứng điều trị.
"""
    )

    col_scores, col_protocols, col_antibiotics = st.columns(3)

    with col_scores:
        st.markdown("#### 📊 Scores & Monitoring")
        st.caption("SOFA, qSOFA, NEWS2, Lactate, MAP, Urine output…")
        if st.button("Mở Scores (ICU)", use_container_width=True, key="bundle_sepsis_scores"):
            try:
                track_feature_usage("bundle_sepsis_scores")
            except Exception:
                pass
            st.switch_page("pages/01_📊_Scores.py")
        if st.button("Labs & Lactate", use_container_width=True, key="bundle_sepsis_labs"):
            try:
                track_feature_usage("bundle_sepsis_labs")
            except Exception:
                pass
            st.switch_page("pages/05_🔬_Labs_and_Calculators.py")

    with col_protocols:
        st.markdown("#### 📋 Sepsis 1-hour bundle")
        st.caption("Theo dõi guideline SSC: dịch, vận mạch, kháng sinh, lactate.")
        if st.button("Mở Sepsis Protocol", use_container_width=True, key="bundle_sepsis_protocol"):
            try:
                track_feature_usage("bundle_sepsis_protocol")
            except Exception:
                pass
            st.switch_page("pages/04_📋_Protocols.py")
        if st.button("Hồi sức / Critical Care", use_container_width=True, key="bundle_sepsis_critical"):
            try:
                track_feature_usage("bundle_sepsis_critical")
            except Exception:
                pass
            st.switch_page("pages/09_🫁_Critical_Care.py")

    with col_antibiotics:
        st.markdown("#### 💊 Kháng sinh & TDM")
        st.caption("Chọn kháng sinh theo nguồn nhiễm, điều chỉnh liều, TDM.")
        if st.button("Kháng sinh chi tiết", use_container_width=True, key="bundle_sepsis_abx"):
            try:
                track_feature_usage("bundle_sepsis_abx")
            except Exception:
                pass
            st.switch_page("pages/02_💊_Antibiotics.py")
        if st.button("Drug Database", use_container_width=True, key="bundle_sepsis_drugdb"):
            try:
                track_feature_usage("bundle_sepsis_drugdb")
            except Exception:
                pass
            st.switch_page("pages/07_💊_Drug_Database.py")
        if st.button("TDM - Nồng độ thuốc", use_container_width=True, key="bundle_sepsis_tdm"):
            try:
                track_feature_usage("bundle_sepsis_tdm")
            except Exception:
                pass
            st.switch_page("pages/08_📊_TDM.py")


with tab_dyspnea:
    st.markdown("### 😮‍💨 Acute Dyspnea / Khó thở cấp")
    st.markdown(
        """
**Mục tiêu:** phân biệt nhanh nguyên nhân tim mạch / hô hấp và hỗ trợ quyết định ICU.
"""
    )

    col_assess, col_icu, col_ddx = st.columns(3)

    with col_assess:
        st.markdown("#### 📊 Đánh giá ban đầu")
        st.caption("CURB-65, PSI, HEART/ACS, SpO₂, ABG…")
        if st.button("Mở Scores Hô hấp/Tim mạch", use_container_width=True, key="bundle_dyspnea_scores"):
            try:
                track_feature_usage("bundle_dyspnea_scores")
            except Exception:
                pass
            st.switch_page("pages/01_📊_Scores.py")
        if st.button("ABG & Labs", use_container_width=True, key="bundle_dyspnea_labs"):
            try:
                track_feature_usage("bundle_dyspnea_labs")
            except Exception:
                pass
            st.switch_page("pages/05_🔬_Labs_and_Calculators.py")

    with col_icu:
        st.markdown("#### 🫁 ICU / Thở máy")
        st.caption("Oxy liệu pháp, NIV/CPAP, thở máy xâm lấn.")
        if st.button("Critical Care / Ventilator", use_container_width=True, key="bundle_dyspnea_icu"):
            try:
                track_feature_usage("bundle_dyspnea_icu")
            except Exception:
                pass
            st.switch_page("pages/09_🫁_Critical_Care.py")

    with col_ddx:
        st.markdown("#### 🩺 Chẩn đoán phân biệt")
        st.caption("Khó thở do tim, COPD/asthma, PE, viêm phổi, ARDS…")
        if st.button("DDx Khó thở", use_container_width=True, key="bundle_dyspnea_ddx"):
            try:
                track_feature_usage("bundle_dyspnea_ddx")
            except Exception:
                pass
            st.switch_page("pages/06_🩺_Diagnosis.py")
        if st.button("Bách khoa bệnh lý", use_container_width=True, key="bundle_dyspnea_disease_ency"):
            try:
                track_feature_usage("bundle_dyspnea_disease_ency")
            except Exception:
                pass
            st.switch_page("pages/16_📖_Disease_Encyclopedia.py")

st.markdown("---")
render_standard_footer(disclaimer=False)

