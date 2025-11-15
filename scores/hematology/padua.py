"""
Padua Prediction Score
Nguy cơ VTE ở bệnh nhân nội khoa - Chỉ định thromboprophylaxis
"""

import streamlit as st


def render():
    """Render Padua Score interface"""
    
    st.markdown("""
    <h2 style='text-align: center; color: #0EA5E9;'>🩺 Padua Prediction Score</h2>
    <p style='text-align: center;'><em>Nguy cơ VTE ở bệnh nhân nội khoa nhập viện</em></p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về Padua Score"):
        st.markdown("""
        **Padua Prediction Score** đánh giá **nguy cơ huyết khối tĩnh mạch (VTE)** ở bệnh nhân 
        **nội khoa nhập viện** để quyết định **dự phòng chống đông**.
        
        **Mục đích:**
        - Xác định bệnh nhân cần thromboprophylaxis
        - Cân bằng lợi ích/nguy cơ chống đông dự phòng
        
        **Khi nào dùng:**
        - Bệnh nhân nội khoa nhập viện
        - Dự kiến nằm viện ≥ 3 ngày
        - Không có chỉ định chống đông điều trị
        
        **Phân loại:**
        - **Padua < 4:** Nguy cơ thấp - KHÔNG cần dự phòng thường quy
        - **Padua ≥ 4:** Nguy cơ cao - NÊN dự phòng (trừ khi chống chỉ định)
        """)
    
    st.markdown("---")
    
    st.subheader("📝 Đánh giá nguy cơ VTE")
    
    score = 0
    components = []
    
    # Active cancer
    cancer = st.checkbox("Ung thư đang hoạt động", help="Metastasis hoặc đang hóa trị/xạ trị trong 6 tháng")
    if cancer:
        score += 3
        components.append("Ung thư hoạt động (+3)")
    
    # Previous VTE
    prev_vte = st.checkbox("Tiền sử VTE (trừ thrombophlebitis nông)", help="PE hoặc DVT trước đây")
    if prev_vte:
        score += 3
        components.append("Tiền sử VTE (+3)")
    
    # Reduced mobility
    mobility = st.checkbox("Giảm vận động", help="Nằm liệt giường (trừ đi toilet) ≥ 3 ngày")
    if mobility:
        score += 3
        components.append("Giảm vận động (+3)")
    
    # Thrombophilic condition
    thrombophilia = st.checkbox("Rối loạn đông máu di truyền", help="Factor V Leiden, Prothrombin G20210A, deficiency AT/PC/PS")
    if thrombophilia:
        score += 3
        components.append("Thrombophilia (+3)")
    
    # Recent trauma/surgery
    trauma = st.checkbox("Chấn thương và/hoặc phẫu thuật ≤ 1 tháng")
    if trauma:
        score += 2
        components.append("Chấn thương/PT gần đây (+2)")
    
    # Age >= 70
    age = st.number_input("Tuổi", 18, 120, 60, 1, format="%d")
    age_70 = age >= 70
    if age_70:
        score += 1
        components.append("Tuổi ≥ 70 (+1)")
    
    # Heart/respiratory failure
    hf_rf = st.checkbox("Suy tim và/hoặc suy hô hấp")
    if hf_rf:
        score += 1
        components.append("Suy tim/hô hấp (+1)")
    
    # AMI/stroke
    ami_stroke = st.checkbox("Nhồi máu cơ tim cấp và/hoặc đột quỵ thiếu máu não")
    if ami_stroke:
        score += 1
        components.append("AMI/Đột quỵ (+1)")
    
    # Acute infection/rheumatologic
    infection = st.checkbox("Nhiễm khuẩn cấp và/hoặc bệnh thấp khớp")
    if infection:
        score += 1
        components.append("Nhiễm khuẩn/Thấp khớp (+1)")
    
    # Obesity
    bmi = st.number_input("BMI (kg/m²)", 10.0, 60.0, 25.0, 0.5, format="%.1f")
    obesity = bmi >= 30
    if obesity:
        score += 1
        components.append(f"Béo phì BMI {bmi:.1f} (+1)")
    
    # Hormone therapy
    hormone = st.checkbox("Đang điều trị hormone (estrogen, HRT, tamoxifen...)")
    if hormone:
        score += 1
        components.append("Điều trị hormone (+1)")
    
    st.markdown("---")
    
    if st.button("📊 Tính Padua Score", type="primary", use_container_width=True):
        # Risk level
        if score >= 4:
            risk = "CAO"
            color = "#dc3545"
            icon = "🚨"
            vte_risk = "~11%"
            recommendation = "NÊN DỰ PHÒNG"
        else:
            risk = "THẤP"
            color = "#28a745"
            icon = "✅"
            vte_risk = "~0.3%"
            recommendation = "KHÔNG cần dự phòng thường quy"
        
        st.markdown("## 📊 Kết quả")
        
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {color}22 0%, {color}44 100%); 
                    padding: 40px; border-radius: 15px; border-left: 5px solid {color}; margin: 20px 0;'>
            <h1 style='color: {color}; margin: 0; text-align: center; font-size: 3em;'>
                {icon} Padua Score = {score}
            </h1>
            <p style='text-align: center; font-size: 1.3em; margin-top: 15px; font-weight: bold;'>
                Nguy cơ VTE: {risk}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        if components:
            st.markdown("### 📋 Thành phần điểm:")
            for comp in components:
                st.markdown(f"- {comp}")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Nguy cơ VTE", vte_risk, help="Nguy cơ VTE trong 90 ngày")
        with col2:
            st.metric("Khuyến cáo", recommendation)
        
        st.markdown("---")
        st.markdown("### 💊 Khuyến cáo dự phòng:")
        
        if score >= 4:
            st.error("""
            **🚨 NGUY CƠ CAO - NÊN DỰ PHÒNG CHỐNG ĐÔNG**
            
            **Kiểm tra chống chỉ định:**
            - Chảy máu đang hoạt động
            - Tiểu cầu < 50,000
            - Rối loạn đông máu nặng
            - Chấn thương sọ não gần đây
            - Chọc dò thắt lưng trong 12h
            - Phẫu thuật thần kinh/nhãn khoa/cột sống gần đây
            
            **Nếu KHÔNG có chống chỉ định:**
            
            1️⃣ **Dự phòng dược lý (lựa chọn ưu tiên):**
            - **Enoxaparin** 40 mg SC mỗi ngày
            - **Dalteparin** 5,000 units SC mỗi ngày
            - **Heparin** 5,000 units SC q8-12h
            - **Fondaparinux** 2.5 mg SC mỗi ngày (nếu suy thận)
            
            **Điều chỉnh liều nếu:**
            - CrCl < 30: Giảm liều enoxaparin hoặc dùng UFH
            - Béo phì nặng (BMI > 40): Tăng liều enoxaparin 30 mg/12h
            
            2️⃣ **Dự phòng cơ học (nếu chống chỉ định dược lý):**
            - Tất áp lực tốc độ (GCS)
            - Thiết bị nén khí động (IPC)
            
            **Thời gian:**
            - Tiếp tục cho đến khi xuất viện HOẶC vận động tốt
            - Không cần kéo dài sau xuất viện (trừ ung thư)
            """)
        else:
            st.success("""
            **✅ NGUY CƠ THẤP - KHÔNG cần dự phòng thường quy**
            
            **Khuyến cáo:**
            - KHÔNG dùng thuốc chống đông dự phòng
            - Khuyến khích vận động sớm
            - Hydrat hóa đầy đủ
            
            **Tái đánh giá nếu:**
            - Tình trạng xấu đi
            - Cần nằm liệt giường kéo dài
            - Xuất hiện yếu tố nguy cơ mới
            
            **Có thể cân nhắc dự phòng cơ học:**
            - GCS (tất áp lực)
            - IPC (thiết bị nén khí động)
            """)
        
        with st.expander("📊 Chi tiết Padua Score"):
            st.markdown("""
            | Yếu tố nguy cơ | Điểm |
            |:---------------|:----:|
            | **Ung thư đang hoạt động** | 3 |
            | **Tiền sử VTE** | 3 |
            | **Giảm vận động** | 3 |
            | **Thrombophilia di truyền** | 3 |
            | **Chấn thương/PT ≤ 1 tháng** | 2 |
            | **Tuổi ≥ 70** | 1 |
            | **Suy tim/hô hấp** | 1 |
            | **AMI/Đột quỵ** | 1 |
            | **Nhiễm khuẩn/Thấp khớp cấp** | 1 |
            | **Béo phì (BMI ≥ 30)** | 1 |
            | **Điều trị hormone** | 1 |
            
            **Phân loại:**
            - **< 4 điểm:** Nguy cơ thấp (~0.3% VTE) - KHÔNG dự phòng
            - **≥ 4 điểm:** Nguy cơ cao (~11% VTE) - NÊN dự phòng
            """)
        
        with st.expander("⚖️ Cân nhắc nguy cơ chảy máu"):
            st.markdown("""
            **TRƯỚC KHI dự phòng, đánh giá nguy cơ chảy máu:**
            
            **Nguy cơ chảy máu CAO (cân nhắc KHÔNG dùng thuốc):**
            - Chảy máu đang hoạt động
            - Tiểu cầu < 50,000
            - Rối loạn đông máu (Hemophilia, VWD...)
            - Suy gan nặng (INR > 1.5)
            - Loét dạ dày tá tràng đang hoạt động
            - Đột quỵ xuất huyết gần đây (< 3 tháng)
            - Phẫu thuật thần kinh/nhãn/cột sống gần đây
            - Chọc dò thắt lưng trong 12h
            
            **Nguy cơ chảy máu TRUNG BÌNH (cân nhắc liều thấp hoặc cơ học):**
            - Tiểu cầu 50-100,000
            - Suy thận nặng (CrCl < 30)
            - Loét dạ dày tá tràng không hoạt động
            - Tuổi > 85
            
            **Nếu nguy cơ chảy máu cao:**
            - Dùng dự phòng CƠ HỌC thay vì thuốc:
              - GCS (tất áp lực)
              - IPC (thiết bị nén)
            """)
        
        with st.expander("📚 Tài liệu tham khảo"):
            st.markdown("""
            1. **Barbar S, Noventa F, Rossetto V, et al.** A risk assessment model for the identification of hospitalized medical patients at risk for venous thromboembolism: the Padua Prediction Score. 
               *J Thromb Haemost.* 2010;8(11):2450-7.
            
            2. **Kahn SR, Lim W, Dunn AS, et al.** Prevention of VTE in nonsurgical patients: Antithrombotic Therapy and Prevention of Thrombosis, 9th ed: American College of Chest Physicians Evidence-Based Clinical Practice Guidelines. 
               *Chest.* 2012;141(2 Suppl):e195S-e226S.
            
            3. **Schünemann HJ, Cushman M, Burnett AE, et al.** American Society of Hematology 2018 guidelines for management of venous thromboembolism: prophylaxis for hospitalized and nonhospitalized medical patients. 
               *Blood Adv.* 2018;2(22):3198-3225.
            """)
    
    st.info("""
    💡 **Điểm quan trọng:**
    
    1. **Padua ≥ 4:** Dự phòng chống đông (trừ khi chống chỉ định)
    
    2. **Enoxaparin 40 mg SC/ngày** - Thuốc ưu tiên
    
    3. **Luôn kiểm tra** nguy cơ chảy máu trước khi dự phòng
    
    4. **Dự phòng cơ học** nếu chống chỉ định thuốc
    
    5. **Tiếp tục** cho đến xuất viện hoặc vận động tốt
    """)


if __name__ == "__main__":
    render()

