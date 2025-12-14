"""
Westley Croup Score
Đánh giá mức độ nặng của viêm후두khí quản cấp (croup) ở trẻ em
"""

import streamlit as st


def render():
    """Render Westley Croup Score interface"""
    
    st.markdown("""
    <h2 style='text-align: center; color: #0EA5E9;'>👶 Westley Croup Score</h2>
    <p style='text-align: center;'><em>Đánh giá mức độ nặng của Croup ở trẻ em</em></p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về Croup và Westley Score"):
        st.markdown("""
        **Croup (Viêm후두khí quản cấp)** là nhiễm virus đường hô hấp trên ở trẻ em, 
        đặc trưng bởi **ho khàn giọng (barking cough)**, **khàn tiếng**, và **khó thở**.
        
        **Westley Croup Score** đánh giá mức độ nặng để quyết định điều trị.
        
        **5 tiêu chí (tối đa 17 điểm):**
        - Tình trạng ý thức
        - Tím tái
        - Rút lõm lồng ngực
        - Thở rít (stridor)
        - Thông khí (air entry)
        
        **Phân loại:**
        - **< 3:** Croup nhẹ
        - **3-7:** Croup trung bình
        - **≥ 8:** Croup nặng
        """)
    
    st.markdown("---")
    
    st.subheader("📝 Đánh giá trẻ")
    
    score = 0
    
    # Level of consciousness
    st.markdown("### 1️⃣ Tình trạng ý thức:")
    consciousness = st.radio(
        "",
        options=[0, 5],
        format_func=lambda x: "Bình thường (tỉnh táo, chơi bình thường)" if x == 0 else "Bất thường (lơ mơ, kích thích, lo lắng)",
        horizontal=False
    )
    score += consciousness
    
    st.markdown("---")
    
    # Cyanosis
    st.markdown("### 2️⃣ Tím tái:")
    cyanosis = st.radio(
        "",
        options=[0, 4, 5],
        format_func=lambda x: {
            0: "Không",
            4: "Tím khi kích động",
            5: "Tím khi nghỉ ngơi"
        }[x]
    )
    score += cyanosis
    
    st.markdown("---")
    
    # Stridor
    st.markdown("### 3️⃣ Thở rít (Stridor):")
    stridor = st.radio(
        "",
        options=[0, 1, 2],
        format_func=lambda x: {
            0: "Không",
            1: "Có khi kích động",
            2: "Có khi nghỉ ngơi"
        }[x]
    )
    score += stridor
    
    st.markdown("---")
    
    # Air entry
    st.markdown("### 4️⃣ Thông khí:")
    air_entry = st.radio(
        "",
        options=[0, 1, 2],
        format_func=lambda x: {
            0: "Bình thường",
            1: "Giảm nhẹ",
            2: "Giảm rõ rệt"
        }[x]
    )
    score += air_entry
    
    st.markdown("---")
    
    # Retractions
    st.markdown("### 5️⃣ Rút lõm lồng ngực:")
    retractions = st.radio(
        "",
        options=[0, 1, 2, 3],
        format_func=lambda x: {
            0: "Không",
            1: "Nhẹ",
            2: "Trung bình",
            3: "Nặng"
        }[x]
    )
    score += retractions
    
    st.markdown("---")
    
    if st.button("📊 Tính Westley Croup Score", type="primary", use_container_width=True):
        # Severity
        if score < 3:
            severity = "Nhẹ"
            color = "#28a745"
            icon = "✅"
        elif score <= 7:
            severity = "Trung bình"
            color = "#ffc107"
            icon = "⚠️"
        else:
            severity = "Nặng"
            color = "#dc3545"
            icon = "🚨"
        
        st.markdown("## 📊 Kết quả")
        
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {color}22 0%, {color}44 100%); 
                    padding: 40px; border-radius: 15px; border-left: 5px solid {color}; margin: 20px 0;'>
            <h1 style='color: {color}; margin: 0; text-align: center; font-size: 3em;'>
                {icon} Westley Score = {score}
            </h1>
            <p style='text-align: center; font-size: 1.3em; margin-top: 15px; font-weight: bold;'>
                Croup {severity}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 💊 Khuyến cáo điều trị:")
        
        if score < 3:
            st.success("""
            **✅ CROUP NHẸ - Điều trị ngoại trú**
            
            **Điều trị:**
            - **Dexamethasone** 0.6 mg/kg PO/IM/IV (tối đa 10 mg) - LIỀU DUY NHẤT
            - Hoặc **Prednisolone** 1 mg/kg PO
            - Hơi nước ấm (không chứng minh hiệu quả nhưng vô hại)
            
            **Hướng dẫn về nhà:**
            - Giữ trẻ bình tĩnh (ẵm bồng)
            - Uống nước đầy đủ
            - Hạ sốt nếu cần (Paracetamol)
            - Quan sát tại viện 2-4h sau dexamethasone
            - Về nhà nếu ổn định
            
            **Tái khám/Cấp cứu nếu:**
            - Khó thở tăng
            - Thở rít khi nghỉ
            - Tím tái
            - Bú kém/không uống được
            - Lơ mơ
            """)
        elif score <= 7:
            st.warning("""
            **⚠️ CROUP TRUNG BÌNH - Cần nhập viện**
            
            **Điều trị:**
            1. **Dexamethasone** 0.6 mg/kg IV/IM/PO (liều duy nhất)
            
            2. **Epinephrine nebulized (nếu có stridor khi nghỉ):**
               - Epinephrine 1:1000: 0.5 mL/kg (tối đa 5 mL) + NaCl 0.9% thành 5 mL
               - Xông khí dung
               - Hiệu quả trong 10-30 phút
               - Tác dụng kéo dài 2h
               - Có thể lặp lại q20-30min nếu cần
            
            3. **Oxy** nếu SpO₂ < 92%
            
            **Theo dõi:**
            - Quan sát ít nhất 4h (vì epinephrine có rebound)
            - Monitor SpO₂, RR, HR
            - Tái đánh giá Westley Score
            
            **Nhập viện nếu:**
            - Cần > 2 liều epinephrine
            - Không cải thiện sau điều trị
            - Điều kiện nhà không đảm bảo
            """)
        else:
            st.error("""
            **🚨 CROUP NẶNG - CẤP CỨU!**
            
            **Nhập viện NGAY - ICU:**
            
            1. **Dexamethasone** 0.6 mg/kg IV ngay
            
            2. **Epinephrine nebulized:**
               - 1:1000: 0.5 mL/kg (max 5 mL) pha NaCl 0.9%
               - Lặp lại q20-30min nếu cần
               - Hoặc infusion liên tục nếu cần nhiều liều
            
            3. **Oxy liệu pháp:**
               - Oxy qua mask/nasal cannula
               - Mục tiêu SpO₂ > 92%
            
            4. **Theo dõi sát:**
               - ICU/PICU
               - Monitor liên tục
               - Sẵn sàng đặt nội khí quản
            
            **Cân nhắc đặt nội khí quản nếu:**
            - Suy hô hấp tiến triển
            - Tím tái kéo dài
            - Lơ mơ, kiệt sức
            - Không đáp ứng epinephrine
            - PaCO₂ tăng
            
            **Lưu ý:**
            - ⚠️ Đặt NKQ khó (phù thanh quản)
            - Dùng ống nhỏ hơn bình thường 0.5-1 size
            - Sẵn sàng cricothyrotomy
            
            **Hội chẩn ENT nếu:**
            - Nghi ngờ epiglottitis
            - Nghi ngờ dị vật
            - Không đáp ứng điều trị
            """)
        
        with st.expander("📊 Bảng Westley Croup Score"):
            st.markdown("""
            | Tiêu chí | 0 | 1 | 2 | 3 | 4 | 5 |
            |:---------|:--|:--|:--|:--|:--|:--|
            | **Ý thức** | Bình thường | - | - | - | - | Bất thường |
            | **Tím tái** | Không | - | - | - | Khi kích động | Khi nghỉ |
            | **Stridor** | Không | Khi kích động | Khi nghỉ | - | - | - |
            | **Thông khí** | Bình thường | Giảm nhẹ | Giảm rõ | - | - | - |
            | **Rút lõm** | Không | Nhẹ | Trung bình | Nặng | - | - |
            
            **Tổng điểm:** 0-17
            
            **Phân loại:**
            - **< 3:** Nhẹ - Ngoại trú
            - **3-7:** Trung bình - Nhập viện
            - **≥ 8:** Nặng - ICU
            """)
        
        with st.expander("ℹ️ Phân biệt Croup vs các bệnh khác"):
            st.markdown("""
            | Đặc điểm | Croup | Epiglottitis | Tracheitis | Dị vật |
            |:---------|:------|:-------------|:-----------|:-------|
            | **Tuổi** | 6m-3y | 2-7y | Bất kỳ | Bất kỳ |
            | **Khởi phát** | Từ từ | Cấp tính | Từ từ | Đột ngột |
            | **Sốt** | Nhẹ | Cao | Cao | Không |
            | **Ho** | Barking | Ít | Có | Có |
            | **Khàn** | Có | Không | Có | Có thể |
            | **Nuốt** | Bình thường | Đau, chảy nước dãi | Bình thường | Có thể khó |
            | **Tư thế** | Bình thường | Ngồi tripod | Bình thường | Khác nhau |
            | **X-quang** | Steeple sign | Thumb sign | Bất thường | Có thể thấy dị vật |
            | **Điều trị** | Dexamethasone | Ceftriaxone + ICU | Kháng sinh | Lấy dị vật |
            
            **🚨 Epiglottitis - CẤP CỨU:**
            - Sốt cao, toxic
            - Ngồi nghiêng về trước, chảy nước dãi
            - KHÔNG khám họng (gây co thắt)
            - Gọi ENT + anesthesia NGAY
            - Ceftriaxone + Vancomycin
            """)
        
        with st.expander("📚 Tài liệu tham khảo"):
            st.markdown("""
            1. **Westley CR, Cotton EK, Brooks JG.** Nebulized racemic epinephrine by IPPB for the treatment of croup: a double-blind study. 
               *Am J Dis Child.* 1978;132(5):484-7.
            
            2. **Bjornson CL, Johnson DW.** Croup. *Lancet.* 2008;371(9609):329-39.
            
            3. **Gates A, Gates M, Vandermeer B, et al.** Glucocorticoids for croup in children. 
               *Cochrane Database Syst Rev.* 2018;8(8):CD001955.
            """)
    
    st.info("""
    💡 **Điểm quan trọng:**
    
    1. **Dexamethasone 0.6 mg/kg** - LUÔN cho, kể cả croup nhẹ
    
    2. **Epinephrine nebulized** - Nếu stridor khi nghỉ
    
    3. **Quan sát 4h** sau epinephrine (rebound effect)
    
    4. **Westley ≥ 8** - Cần ICU
    
    5. **Không khám họng** nếu nghi epiglottitis!
    """)


if __name__ == "__main__":
    render()

