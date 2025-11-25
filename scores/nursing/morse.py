"""
Morse Fall Scale
Thang điểm đánh giá nguy cơ té ngã
"""

import streamlit as st


def render():
    """Morse Fall Scale Calculator"""
    st.markdown("""
    <h2 style='text-align: center; color: #0EA5E9;'>⚠️ Morse Fall Scale</h2>
    <p style='text-align: center;'><em>Thang điểm đánh giá nguy cơ té ngã</em></p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu"):
        st.markdown("""
        **Morse Fall Scale** là thang điểm tiêu chuẩn để đánh giá nguy cơ té ngã ở bệnh nhân nội trú.
        
        **Chỉ định:**
        - Tất cả bệnh nhân nội trú
        - Bệnh nhân cao tuổi
        - Bệnh nhân có tiền sử té ngã
        - Đánh giá khi vào viện và định kỳ
        
        **6 Tiêu chí (tổng điểm 0-125):**
        1. **History of Falling (Tiền sử té ngã)** - 0 hoặc 25 điểm
        2. **Secondary Diagnosis (Chẩn đoán thứ phát)** - 0 hoặc 15 điểm
        3. **Ambulatory Aid (Dụng cụ hỗ trợ đi lại)** - 0, 15, hoặc 30 điểm
        4. **IV/Heparin Lock (Truyền dịch)** - 0 hoặc 20 điểm
        5. **Gait (Dáng đi)** - 0, 10, hoặc 20 điểm
        6. **Mental Status (Tình trạng tâm thần)** - 0 hoặc 15 điểm
        
        **Nguy cơ:**
        - **0-24:** Nguy cơ thấp
        - **25-44:** Nguy cơ trung bình
        - **≥ 45:** Nguy cơ cao
        """)
    
    st.markdown("---")
    
    st.subheader("📝 Đánh Giá")
    
    # 1. History of Falling
    st.markdown("### 1️⃣ History of Falling (Tiền sử té ngã)")
    history_fall = st.radio(
        "Có tiền sử té ngã trong 3 tháng qua?",
        [
            "0 - Không",
            "25 - Có"
        ],
        key="morse_history"
    )
    history_score = int(history_fall.split(" - ")[0])
    
    # 2. Secondary Diagnosis
    st.markdown("### 2️⃣ Secondary Diagnosis (Chẩn đoán thứ phát)")
    secondary_dx = st.radio(
        "Có nhiều hơn 1 chẩn đoán?",
        [
            "0 - Không (chỉ 1 chẩn đoán)",
            "15 - Có (≥ 2 chẩn đoán)"
        ],
        key="morse_secondary"
    )
    secondary_score = int(secondary_dx.split(" - ")[0])
    
    # 3. Ambulatory Aid
    st.markdown("### 3️⃣ Ambulatory Aid (Dụng cụ hỗ trợ đi lại)")
    ambulatory = st.radio(
        "Dụng cụ hỗ trợ đi lại:",
        [
            "0 - Không cần, hoặc nằm liệt giường, hoặc đi lại với người hỗ trợ",
            "15 - Nạng, gậy, khung tập đi",
            "30 - Đi lại bằng cách vịn tường, bàn, hoặc không có dụng cụ hỗ trợ"
        ],
        key="morse_ambulatory"
    )
    ambulatory_score = int(ambulatory.split(" - ")[0])
    
    # 4. IV/Heparin Lock
    st.markdown("### 4️⃣ IV/Heparin Lock (Truyền dịch)")
    iv_lock = st.radio(
        "Có truyền dịch hoặc heparin lock?",
        [
            "0 - Không",
            "20 - Có"
        ],
        key="morse_iv"
    )
    iv_score = int(iv_lock.split(" - ")[0])
    
    # 5. Gait
    st.markdown("### 5️⃣ Gait (Dáng đi)")
    gait = st.radio(
        "Dáng đi:",
        [
            "0 - Bình thường, đi lại tốt, hoặc nằm liệt giường",
            "10 - Yếu, cần hỗ trợ",
            "20 - Rối loạn, không vững, hoặc không thể đi lại"
        ],
        key="morse_gait"
    )
    gait_score = int(gait.split(" - ")[0])
    
    # 6. Mental Status
    st.markdown("### 6️⃣ Mental Status (Tình trạng tâm thần)")
    mental = st.radio(
        "Tình trạng tâm thần:",
        [
            "0 - Tỉnh táo, định hướng tốt về bản thân và môi trường",
            "15 - Lú lẫn, quên, hoặc không hợp tác"
        ],
        key="morse_mental"
    )
    mental_score = int(mental.split(" - ")[0])
    
    st.markdown("---")
    
    if st.button("📊 Tính điểm Morse", type="primary", use_container_width=True):
        total_score = history_score + secondary_score + ambulatory_score + iv_score + gait_score + mental_score
        
        st.markdown("## 📊 Kết quả")
        
        # Interpret risk
        if total_score < 25:
            risk_level = "Nguy cơ thấp"
            color = "#10b981"
            icon = "✅"
            interpretation = "Nguy cơ té ngã thấp"
        elif total_score < 45:
            risk_level = "Nguy cơ trung bình"
            color = "#f59e0b"
            icon = "⚠️"
            interpretation = "Nguy cơ té ngã trung bình, cần theo dõi"
        else:
            risk_level = "Nguy cơ cao"
            color = "#ef4444"
            icon = "🚨"
            interpretation = "Nguy cơ té ngã cao, cần can thiệp ngay"
        
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {color}22 0%, {color}44 100%); 
                    padding: 30px; border-radius: 15px; border-left: 5px solid {color}; margin: 20px 0;'>
            <h2 style='color: {color}; margin: 0; text-align: center;'>
                {icon} Morse Fall Score = {total_score}
            </h2>
            <p style='text-align: center; font-size: 1.1em; margin-top: 10px;'>
                {risk_level}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"**Diễn giải:** {interpretation}")
        
        # Breakdown
        st.markdown("### 📋 Chi tiết điểm số:")
        st.markdown(f"""
        - **History of Falling (Tiền sử té ngã):** {history_score} điểm
        - **Secondary Diagnosis (Chẩn đoán thứ phát):** {secondary_score} điểm
        - **Ambulatory Aid (Dụng cụ hỗ trợ):** {ambulatory_score} điểm
        - **IV/Heparin Lock (Truyền dịch):** {iv_score} điểm
        - **Gait (Dáng đi):** {gait_score} điểm
        - **Mental Status (Tình trạng tâm thần):** {mental_score} điểm
        
        **Tổng:** {total_score} điểm
        """)
        
        # Prevention recommendations
        st.markdown("---")
        st.markdown("### 🛡️ Khuyến nghị phòng ngừa")
        
        if total_score < 25:
            st.success("""
            **✅ Nguy cơ thấp (Morse < 25):**
            
            **Biện pháp cơ bản:**
            - Hướng dẫn bệnh nhân về an toàn
            - Đảm bảo môi trường an toàn
            - Đánh giá lại khi có thay đổi tình trạng
            """)
        elif total_score < 45:
            st.warning("""
            **⚠️ Nguy cơ trung bình (Morse 25-44):**
            
            **Biện pháp phòng ngừa:**
            
            1. **Môi trường:**
               - Đảm bảo đủ ánh sáng
               - Loại bỏ vật cản trên sàn
               - Sử dụng thảm chống trượt
               - Đảm bảo giường ở vị trí thấp, có thanh chắn
            
            2. **Hỗ trợ:**
               - Hỗ trợ khi đi lại
               - Sử dụng dụng cụ hỗ trợ phù hợp
               - Đảm bảo giày dép phù hợp, không trơn trượt
            
            3. **Theo dõi:**
               - Đánh giá lại Morse mỗi 48 giờ
               - Theo dõi sát bệnh nhân
            """)
        else:
            st.error("""
            **🚨 Nguy cơ cao (Morse ≥ 45) - Can thiệp ngay:**
            
            **Biện pháp phòng ngừa tích cực:**
            
            1. **Môi trường:**
               - Đảm bảo đủ án sáng (đặc biệt ban đêm)
               - Loại bỏ tất cả vật cản
               - Sử dụng thảm chống trượt
               - Giường ở vị trí thấp nhất, có thanh chắn
               - Chuông gọi trong tầm với
            
            2. **Hỗ trợ:**
               - Hỗ trợ khi đi lại (không để đi một mình)
               - Sử dụng dụng cụ hỗ trợ phù hợp
               - Đảm bảo giày dép phù hợp, chống trượt
               - Cân nhắc sử dụng áo vest hoặc đai an toàn (nếu cần)
            
            3. **Theo dõi:**
               - Đánh giá lại Morse mỗi 24 giờ
               - Theo dõi sát bệnh nhân (mỗi 1-2 giờ)
               - Đặt bệnh nhân gần bàn điều dưỡng
               - Ghi nhận trên bảng theo dõi
            
            4. **Giáo dục:**
               - Hướng dẫn bệnh nhân và gia đình về nguy cơ té ngã
               - Nhắc nhở gọi nhân viên y tế khi cần đi lại
               - Hướng dẫn cách đứng dậy an toàn
            
            5. **Điều chỉnh thuốc:**
               - Đánh giá thuốc có thể gây té ngã (an thần, hạ huyết áp...)
               - Cân nhắc điều chỉnh liều hoặc thời gian dùng thuốc
            """)
        
        with st.expander("📚 Hướng Dẫn Sử Dụng"):
            st.markdown("""
            ### 🎯 Cách Đánh Giá:
            
            1. **Đánh giá khi vào viện:**
               - Tất cả bệnh nhân nội trú
               - Đặc biệt bệnh nhân cao tuổi (≥ 65 tuổi)
               - Bệnh nhân có tiền sử té ngã
            
            2. **Đánh giá định kỳ:**
               - Nguy cơ cao (≥ 45): Mỗi 24 giờ
               - Nguy cơ trung bình (25-44): Mỗi 48 giờ
               - Nguy cơ thấp (< 25): Khi có thay đổi
            
            3. **Đánh giá lại khi:**
               - Tình trạng bệnh nhân thay đổi
               - Sau phẫu thuật
               - Sau khi té ngã
               - Khi thay đổi thuốc (an thần, hạ huyết áp...)
               - Khi chuyển khoa
            
            ### 📋 Yếu tố nguy cơ té ngã:
            - Tuổi cao (≥ 65 tuổi)
            - Tiền sử té ngã
            - Rối loạn dáng đi, thăng bằng
            - Yếu cơ, giảm sức mạnh
            - Rối loạn tâm thần (lú lẫn, sa sút trí tuệ)
            - Thuốc (an thần, hạ huyết áp, lợi tiểu...)
            - Bệnh lý (đột quỵ, Parkinson, bệnh tim...)
            - Môi trường (ánh sáng kém, sàn trơn...)
            """)
        
        with st.expander("📚 Tài liệu tham khảo"):
            st.markdown("""
            1. **Morse JM, Morse RM, Tylko SJ.** Development of a scale to identify the fall-prone patient. 
               *Can J Aging.* 1989;8(4):366-377.
            
            2. **Morse JM, Black C, Oberle K, Donahue P.** A prospective study to identify the fall-prone patient. 
               *Soc Sci Med.* 1989;28(1):81-86.
            """)
    
    st.info("""
    💡 **Điểm quan trọng:**
    
    1. **Morse < 25:** Nguy cơ thấp → Phòng ngừa cơ bản
    2. **Morse 25-44:** Nguy cơ trung bình → Theo dõi và phòng ngừa
    3. **Morse ≥ 45:** Nguy cơ cao → Can thiệp ngay
    4. **Đánh giá lại:** Tùy theo mức độ nguy cơ (24-48 giờ)
    5. **Mục tiêu:** Phòng ngừa té ngã, giảm tỷ lệ té ngã trong bệnh viện
    """)

