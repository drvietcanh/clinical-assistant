"""
Stress Ulcer Prophylaxis Protocol
SCCM Guidelines, ASHP Guidelines
Prevention of Stress-Related Mucosal Disease
"""

import streamlit as st


def render():
    """Stress Ulcer Prophylaxis Protocol"""
    st.subheader("🩸 Stress Ulcer Prophylaxis Protocol")
    st.caption("SCCM Guidelines - Prevention of Stress-Related Mucosal Disease")
    
    st.info("""
    **Stress Ulcer Prophylaxis (SUP) là phòng ngừa xuất huyết tiêu hóa do stress ở bệnh nhân ICU.**
    - **Incidence:** 1-5% ở ICU patients
    - **Mortality:** 30-50% nếu có bleeding
    - **Prevention:** Quan trọng ở bệnh nhân nguy cơ cao
    """)
    
    st.markdown("---")
    
    # Risk stratification
    st.markdown("### 1️⃣ Risk Stratification - Đánh giá Nguy cơ")
    
    st.markdown("#### 📋 Chỉ định SUP (High Risk)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**High Risk Factors (Cần SUP):**")
        mechanical_vent = st.checkbox("**Mechanical ventilation >48h**", key="sup_vent")
        coagulopathy = st.checkbox("**Coagulopathy (INR >1.5, Platelet <50k)**", key="sup_coag")
        gi_bleed_hx = st.checkbox("**Tiền sử GI bleeding**", key="sup_hx")
        shock = st.checkbox("**Shock (vasopressors >4h)**", key="sup_shock")
        burn = st.checkbox("**Burns >35% BSA**", key="sup_burn")
        head_injury = st.checkbox("**Head injury (GCS <10)**", key="sup_head")
    
    with col2:
        st.markdown("**Moderate Risk Factors (Cân nhắc SUP):**")
        sepsis = st.checkbox("**Sepsis**", key="sup_sepsis")
        multiple_trauma = st.checkbox("**Multiple trauma**", key="sup_trauma")
        renal_failure = st.checkbox("**Renal failure (Cr >2 mg/dL)**", key="sup_renal")
        liver_failure = st.checkbox("**Liver failure**", key="sup_liver")
        steroids = st.checkbox("**High-dose steroids**", key="sup_steroids")
        anticoagulation = st.checkbox("**Anticoagulation**", key="sup_anticoag")
    
    # Calculate risk
    high_risk_count = sum([mechanical_vent, coagulopathy, gi_bleed_hx, shock, burn, head_injury])
    moderate_risk_count = sum([sepsis, multiple_trauma, renal_failure, liver_failure, steroids, anticoagulation])
    
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        if high_risk_count >= 1:
            st.error("### 🚨 **NGUY CƠ CAO - CẦN SUP**")
            st.error(f"Có {high_risk_count} yếu tố nguy cơ cao - Bắt đầu SUP ngay")
            need_sup = True
            risk_level = "High"
        elif moderate_risk_count >= 2:
            st.warning("### ⚠️ **NGUY CƠ TRUNG BÌNH - CÂN NHẮC SUP**")
            st.warning(f"Có {moderate_risk_count} yếu tố nguy cơ trung bình - Cân nhắc SUP")
            need_sup = True
            risk_level = "Moderate"
        else:
            st.success("### ✅ **NGUY CƠ THẤP - KHÔNG CẦN SUP**")
            st.success("Không có yếu tố nguy cơ cao - Không cần SUP routine")
            need_sup = False
            risk_level = "Low"
    
    with col2:
        st.metric("**High Risk:**", f"{high_risk_count}/6")
        st.metric("**Moderate Risk:**", f"{moderate_risk_count}/6")
    
    st.markdown("---")
    st.markdown("### 2️⃣ SUP Agents - Thuốc Phòng Ngừa")
    
    if need_sup:
        agent = st.radio(
            "**Chọn thuốc SUP:**",
            ["PPI (Proton Pump Inhibitor) - Ưu tiên", "H2 Receptor Antagonist", "Sucralfate"],
            key="sup_agent"
        )
        
        st.markdown("---")
        
        if "PPI" in agent:
            render_ppi_sup()
        elif "H2" in agent:
            render_h2_sup()
        else:
            render_sucralfate_sup()
    else:
        st.info("""
        **Không cần SUP routine:**
        - Chỉ dùng SUP nếu có indication mới
        - Reassess nếu tình trạng thay đổi
        """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Duration & Discontinuation")
    
    st.warning("""
    **Khi nào dừng SUP:**
    
    **Discontinue nếu:**
    - Không còn mechanical ventilation (và không có yếu tố nguy cơ khác)
    - Hemodynamically stable (không cần vasopressors)
    - Coagulopathy đã cải thiện
    - Đã chuyển sang PO diet
    
    **Lưu ý:**
    - Không cần SUP sau khi xuất viện (trừ trường hợp đặc biệt)
    - Reassess mỗi 24-48h
    - Dừng sớm khi có thể (giảm nguy cơ C. difficile, pneumonia)
    """)
    
    st.markdown("---")
    st.markdown("### 4️⃣ Monitoring")
    
    st.info("""
    **Theo dõi dấu hiệu GI bleeding:**
    - **Hematemesis:** Nôn máu
    - **Melena:** Phân đen
    - **Hematochezia:** Phân máu đỏ
    - **Gastric aspirate:** Coffee ground hoặc máu
    - **Hgb drop:** >2 g/dL trong 24h
    - **Hemodynamic instability:** Tụt HA, shock
    
    **Nếu có bleeding:**
    - Dừng SUP (không hiệu quả)
    - GI consult
    - Endoscopy
    - Điều trị theo GI bleeding protocol
    """)
    
    st.markdown("---")
    st.markdown("### 5️⃣ Complications")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.warning("""
        **PPI/H2 Blockers:**
        - Tăng nguy cơ C. difficile colitis
        - Tăng nguy cơ viêm phổi (HAP/VAP)
        - Tăng nguy cơ gãy xương (dùng kéo dài)
        - Giảm hấp thu vitamin B12, Mg²⁺
        """)
    
    with col2:
        st.info("""
        **Sucralfate:**
        - Tăng nguy cơ bezoar
        - Tương tác với một số thuốc (giảm hấp thu)
        - Ít nguy cơ C. difficile, pneumonia hơn PPI/H2
        """)
    
    st.markdown("---")
    st.markdown("### 📚 Tài liệu tham khảo")
    
    st.markdown("""
    1. **SCCM Guidelines** - Stress Ulcer Prophylaxis 2016
    2. **ASHP Guidelines** - Stress Ulcer Prophylaxis 1999
    3. **UpToDate:** Stress Ulcer Prophylaxis in ICU - Last updated 2024
    """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể.")


def render_ppi_sup():
    """PPI for SUP"""
    st.success("## 💊 PPI (Proton Pump Inhibitor) - Ưu Tiên")
    
    st.info("""
    **PPI là lựa chọn ưu tiên cho SUP:**
    - Hiệu quả tốt hơn H2 blockers
    - Giảm nguy cơ GI bleeding
    - Dễ dùng (IV hoặc PO)
    """)
    
    ppi_type = st.selectbox(
        "**Loại PPI:**",
        ["Pantoprazole", "Omeprazole", "Esomeprazole", "Lansoprazole"],
        key="sup_ppi_type"
    )
    
    route = st.radio(
        "**Đường dùng:**",
        ["IV (Ưu tiên nếu NPO)", "PO (nếu có thể uống)"],
        key="sup_ppi_route"
    )
    
    if route == "IV":
        st.success(f"""
        **{ppi_type} IV Protocol:**
        
        **Liều:**
        - **Pantoprazole:** 40mg IV q12h hoặc 40mg IV q24h
        - **Omeprazole:** 40mg IV q12h hoặc 40mg IV q24h
        - **Esomeprazole:** 40mg IV q12h hoặc 40mg IV q24h
        
        **Cách pha:**
        - Pha trong 100ml NS
        - Truyền trong 15-30 phút
        
        **Duration:** Cho đến khi không còn indication
        """)
    else:
        st.info(f"""
        **{ppi_type} PO Protocol:**
        
        **Liều:**
        - **Pantoprazole:** 40mg PO q12h hoặc 40mg PO q24h
        - **Omeprazole:** 40mg PO q12h hoặc 40mg PO q24h
        - **Esomeprazole:** 40mg PO q12h hoặc 40mg PO q24h
        
        **Lưu ý:** Uống 30-60 phút trước bữa ăn (nếu có thể)
        """)


def render_h2_sup():
    """H2 Blockers for SUP"""
    st.warning("## 💊 H2 Receptor Antagonists")
    
    st.info("""
    **H2 Blockers (Alternative to PPI):**
    - Hiệu quả tốt nhưng kém hơn PPI một chút
    - Có thể dùng nếu không có PPI
    """)
    
    h2_type = st.selectbox(
        "**Loại H2 Blocker:**",
        ["Famotidine", "Ranitidine", "Cimetidine"],
        key="sup_h2_type"
    )
    
    route = st.radio(
        "**Đường dùng:**",
        ["IV", "PO"],
        key="sup_h2_route"
    )
    
    if route == "IV":
        st.success(f"""
        **{h2_type} IV Protocol:**
        
        **Liều:**
        - **Famotidine:** 20mg IV q12h
        - **Ranitidine:** 50mg IV q8h hoặc 150mg IV q12h
        - **Cimetidine:** 300mg IV q6-8h
        
        **Duration:** Cho đến khi không còn indication
        """)
    else:
        st.info(f"""
        **{h2_type} PO Protocol:**
        
        **Liều:**
        - **Famotidine:** 20mg PO q12h hoặc 40mg PO q24h
        - **Ranitidine:** 150mg PO q12h
        - **Cimetidine:** 300mg PO q6h hoặc 400mg PO q12h
        """)


def render_sucralfate_sup():
    """Sucralfate for SUP"""
    st.info("## 💊 Sucralfate")
    
    st.warning("""
    **Sucralfate:**
    - Ít hiệu quả hơn PPI/H2
    - Ưu điểm: Ít nguy cơ C. difficile, pneumonia
    - Nhược điểm: Tăng nguy cơ bezoar, tương tác thuốc
    - **Chỉ dùng nếu:** Không thể dùng PPI/H2 (allergy, etc.)
    """)
    
    st.success("""
    **Sucralfate Protocol:**
    
    **Liều:**
    - **1g PO q6h** (4 lần/ngày)
    - Hoặc **1g PO q8h** (3 lần/ngày)
    
    **Lưu ý:**
    - Uống 1 giờ trước hoặc 2 giờ sau các thuốc khác
    - Không dùng nếu có bezoar risk
    - Có thể gây constipation
    """)

