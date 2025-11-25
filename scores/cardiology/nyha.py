"""
NYHA Functional Classification
Phân loại chức năng suy tim theo New York Heart Association
"""

import streamlit as st


def render():
    """Render NYHA Classification interface"""
    
    st.markdown("""
    <h2 style='text-align: center; color: #0EA5E9;'>❤️ NYHA Functional Classification</h2>
    <p style='text-align: center;'><em>Phân loại chức năng suy tim - New York Heart Association</em></p>
    """, unsafe_allow_html=True)
    
    # Thông tin về NYHA
    with st.expander("ℹ️ Giới thiệu về NYHA Classification"):
        st.markdown("""
        **NYHA (New York Heart Association) Functional Classification** là hệ thống phân loại 
        mức độ nặng của suy tim dựa trên **triệu chứng** và **hoạt động thể lực**.
        
        **Đặc điểm:**
        - Đơn giản, dễ sử dụng
        - Dựa hoàn toàn trên lâm sàng (không cần xét nghiệm)
        - Sử dụng rộng rãi trong thực hành lâm sàng
        - Hướng dẫn điều trị và tiên lượng
        
        **Lưu ý quan trọng:**
        - NYHA đánh giá **TRIỆU CHỨNG**, không phải chức năng tim
        - EF thấp có thể không triệu chứng (NYHA I)
        - EF bảo tồn có thể nặng (NYHA III-IV)
        - Phân loại có thể thay đổi theo điều trị
        
        **Phân biệt:**
        - **NYHA Class:** Triệu chứng hiện tại (có thể thay đổi)
        - **ACC/AHA Stage:** Tiến triển bệnh (không thay đổi)
        """)
    
    st.markdown("---")
    
    # Interactive classification
    st.subheader("📝 Đánh giá bệnh nhân")
    
    st.markdown("""
    Hãy chọn mức độ hoạt động gây ra triệu chứng cho bệnh nhân:
    """)
    
    # Classification questions
    st.markdown("### 🏃 Hoạt động thể lực và triệu chứng:")
    
    option = st.radio(
        "Bệnh nhân có triệu chứng (khó thở, mệt, tim đập nhanh) khi:",
        options=[
            "class1",
            "class2", 
            "class3",
            "class4"
        ],
        format_func=lambda x: {
            "class1": "❌ KHÔNG có triệu chứng với hoạt động thể lực bình thường",
            "class2": "⚠️ Có triệu chứng với hoạt động VỪNG (leo cầu thang, đi nhanh, mang vác)",
            "class3": "🔶 Có triệu chứng với hoạt động NHẸ (đi bộ bình thường, tắm rửa, thay quần áo)",
            "class4": "🚨 Có triệu chứng KHI NGHỈ hoặc với BẤT KỲ hoạt động nào"
        }[x],
        help="Chọn mức độ hoạt động thấp nhất gây ra triệu chứng"
    )
    
    st.markdown("---")
    
    # Specific symptom check
    st.markdown("### 💭 Triệu chứng cụ thể:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        dyspnea = st.checkbox("Khó thở khi gắng sức", value=True)
        fatigue = st.checkbox("Mệt mỏi, suy nhược", value=True)
    
    with col2:
        palpitations = st.checkbox("Hồi hộp, tim đập nhanh")
        orthopnea = st.checkbox("Khó thở khi nằm (orthopnea)")
    
    # Additional assessment
    functional_capacity = st.slider(
        "Khả năng sinh hoạt hàng ngày (%)",
        min_value=0,
        max_value=100,
        value=50,
        step=10,
        help="Đánh giá tổng quát khả năng sinh hoạt so với bình thường"
    )
    
    st.markdown("---")
    
    # Display results
    if st.button("📋 Xác định NYHA Class", type="primary", use_container_width=True):
        # Determine class
        classifications = {
            "class1": {
                "class": "Class I",
                "roman": "I",
                "description": "Không hạn chế hoạt động thể lực",
                "details": """
                - Hoạt động thể lực bình thường KHÔNG gây mệt, hồi hộp hoặc khó thở
                - Không có triệu chứng với hoạt động hàng ngày
                - Có thể leo cầu thang nhiều tầng không khó thở
                - Có thể chơi thể thao nhẹ
                """,
                "color": "#28a745",
                "icon": "✅",
                "prognosis": "Tiên lượng tốt",
                "mortality": "Tỷ lệ tử vong 1 năm: ~5%"
            },
            "class2": {
                "class": "Class II",
                "roman": "II",
                "description": "Hạn chế nhẹ hoạt động thể lực",
                "details": """
                - Thoải mái khi nghỉ
                - Hoạt động thể lực bình thường gây mệt, hồi hộp hoặc khó thở
                - Khó thở khi leo cầu thang, đi nhanh, mang vác
                - Có thể làm việc nhà nhẹ nhàng
                - Có thể đi bộ khoảng cách vừa phải
                """,
                "color": "#ffc107",
                "icon": "⚠️",
                "prognosis": "Tiên lượng tương đối tốt",
                "mortality": "Tỷ lệ tử vong 1 năm: ~10-15%"
            },
            "class3": {
                "class": "Class III",
                "roman": "III",
                "description": "Hạn chế rõ rệt hoạt động thể lực",
                "details": """
                - Thoải mái khi nghỉ
                - Hoạt động thể lực NHẸ HƠN bình thường gây triệu chứng
                - Khó thở khi đi bộ bình thường, tắm rửa, thay quần áo
                - Chỉ có thể làm việc nhà rất nhẹ
                - Khó đi bộ quãng đường ngắn
                """,
                "color": "#fd7e14",
                "icon": "🔶",
                "prognosis": "Tiên lượng kém hơn",
                "mortality": "Tỷ lệ tử vong 1 năm: ~20-30%"
            },
            "class4": {
                "class": "Class IV",
                "roman": "IV",
                "description": "Không thể hoạt động thể lực không khó chịu",
                "details": """
                - Triệu chứng khi NGHỈ
                - Khó chịu tăng lên với BẤT KỲ hoạt động nào
                - Khó thở ngay cả khi nằm hoặc ngồi
                - Cần nằm đầu cao
                - Không thể tự chăm sóc bản thân
                - Phụ thuộc hoàn toàn vào người khác
                """,
                "color": "#dc3545",
                "icon": "🚨",
                "prognosis": "Tiên lượng xấu",
                "mortality": "Tỷ lệ tử vong 1 năm: ~40-60%"
            }
        }
        
        result = classifications[option]
        
        # Main result
        st.markdown("## 📊 Kết quả")
        
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {result['color']}22 0%, {result['color']}44 100%); 
                    padding: 40px; border-radius: 15px; border-left: 5px solid {result['color']}; margin: 20px 0;'>
            <h1 style='color: {result['color']}; margin: 0; text-align: center; font-size: 3em;'>
                {result['icon']} NYHA {result['class']}
            </h1>
            <p style='text-align: center; font-size: 1.3em; margin-top: 15px; font-weight: bold;'>
                {result['description']}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Details
        st.markdown(f"""
        <div style='background-color: {result['color']}22; padding: 20px; border-radius: 10px; border: 2px solid {result['color']};'>
            <h3 style='color: {result['color']};'>📋 Đặc điểm lâm sàng:</h3>
            <div style='font-size: 1.1em; line-height: 1.8;'>
                {result['details']}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Prognosis
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric(
                "Tiên lượng",
                result['prognosis'],
                help="Tiên lượng tổng quát dựa trên NYHA class"
            )
        
        with col2:
            st.metric(
                "Tỷ lệ tử vong",
                result['mortality'],
                help="Ước tính tỷ lệ tử vong 1 năm"
            )
        
        # Management recommendations
        st.markdown("---")
        st.markdown("### 💊 Khuyến cáo điều trị")
        
        if option == "class1":
            st.success("""
            **NYHA Class I - Điều trị dự phòng**
            
            **Mục Tiêu:** Ngăn tiến triển, kiểm soát yếu tố nguy cơ
            
            **Thuốc nền:**
            - **ACEi/ARB hoặc ARNI** (nếu EF giảm)
            - **Beta-blocker** (nếu EF giảm hoặc post-MI)
            - **MRA** (nếu EF < 35%)
            
            **Lối sống:**
            - ✅ Tập thể dục đều đặn
            - ✅ Kiểm soát cân nặng
            - ✅ Hạn chế muối (< 2-3 g/ngày)
            - ✅ Kiểm soát ĐTĐ, THA, lipid
            - ❌ Ngừng hút thuốc, hạn chế rượu
            
            **Theo Dõi:**
            - Khám lại 3-6 tháng
            - Siêu âm tim hàng năm
            - Monitor EF, BNP
            """)
        
        elif option == "class2":
            st.warning("""
            **NYHA Class II - Điều trị tối ưu**
            
            **Mục Tiêu:** Giảm triệu chứng, ngăn tiến triển
            
            **Thuốc nền (GDMT):**
            - **ACEi/ARB hoặc ARNI** 
            - **Beta-blocker**
            - **MRA** (nếu EF < 35%)
            - **SGLT2i** (Dapagliflozin, Empagliflozin)
            
            **Thuốc triệu chứng:**
            - **Lợi tiểu quai** (Furosemide) nếu tắc nghẽn
            - Digoxin (nếu AF hoặc triệu chứng dai dẳng)
            
            **Lối sống:**
            - ⚠️ Hạn chế gắng sức nặng
            - ✅ Tập thể dục vừa phải (cardiac rehab)
            - ✅ Hạn chế muối < 2g/ngày
            - ✅ Hạn chế dịch < 1.5-2L/ngày
            - ✅ Cân nặng hàng ngày
            
            **Theo Dõi:**
            - Khám lại 2-3 tháng
            - Siêu âm tim 6-12 tháng
            - Đánh giá ICD nếu EF < 35%
            """)
        
        elif option == "class3":
            st.error("""
            **NYHA Class III - Điều trị tích cực**
            
            **Mục Tiêu:** Giảm triệu chứng, cải thiện chất lượng sống, giảm nhập viện
            
            **Thuốc nền (GDMT) - LIỀU TỐI ĐA:**
            - **ARNI** (Sacubitril/Valsartan) thay ACEi
            - **Beta-blocker** (tăng liều từ từ)
            - **MRA** (Spironolactone/Eplerenone)
            - **SGLT2i** (Dapagliflozin/Empagliflozin)
            
            **Thuốc triệu chứng:**
            - **Lợi tiểu quai liều cao** ± Thiazide
            - Digoxin
            - Hydralazine + Nitrate (nếu không dung nạp ACEi/ARB)
            
            **Can thiệp:**
            - ⚡ **ICD** nếu EF ≤ 35% (phòng đột tử)
            - ⚡ **CRT** nếu QRS ≥ 130ms + LBBB
            - 🫀 Đánh giá **ghép tim**
            - 🫀 Đánh giá **LVAD** (heart pump)
            
            **Lối sống:**
            - 🚫 Hạn chế hoạt động nặng
            - ✅ Vật lý trị liệu giám sát
            - ✅ Muối < 2g/ngày, dịch < 1.5L/ngày
            - ✅ Cân nặng HÀNG NGÀY
            
            **Theo Dõi:**
            - Khám 1-2 tháng
            - Siêu âm tim 3-6 tháng
            - ⚠️ Hội chẩn chuyên khoa tim
            """)
        
        else:  # class4
            st.error("""
            **NYHA Class IV - Điều trị cấp cứu/giai đoạn cuối**
            
            **🚨 CẦN NHẬP VIỆN NGAY**
            
            **Điều trị nội trú:**
            - **Lợi tiểu IV** (Furosemide bolus hoặc infusion)
            - **Inotropes** nếu huyết động kém:
              - Dobutamine
              - Milrinone
              - Levosimendan
            - **Vasodilators IV** (Nitroglycerin, Nitroprusside)
            - Siêu lọc (ultrafiltration) nếu kháng lợi tiểu
            
            **Can thiệp khẩn:**
            - 🫀 **Đánh giá ghép tim KHẨN**
            - 🫀 **LVAD** (mechanical circulatory support)
            - ⚡ **Intra-aortic balloon pump (IABP)**
            - 🏥 **ICU monitoring**
            
            **Nếu không phù hợp ghép tim:**
            - 💊 **Thuốc vận mạch liên tục** (inotrope dependence)
            - 💊 **Inotropes tại nhà** (palliative)
            - 🕊️ **Chăm sóc giảm nhẹ** (palliative care)
            - ☮️ Thảo luận mục tiêu chăm sóc
            
            **Lưu ý:**
            - ❌ KHÔNG ra viện cho đến khi ổn định
            - ✅ Cân mỗi ngày
            - ✅ Hạn chế dịch NGHIÊM NGẶT < 1-1.5L/ngày
            - ✅ Muối < 2g/ngày
            - 🚫 Tuyệt đối nghỉ ngơi
            
            **Tiên lượng:**
            - Tỷ lệ tử vong rất cao nếu không can thiệp
            - Cần bàn về Advanced Care Planning
            """)
        
        # Comparison with ACC/AHA staging
        with st.expander("🔄 So sánh NYHA vs ACC/AHA Stage"):
            st.markdown("""
            ### NYHA Class (Triệu chứng - CÓ THỂ THAY ĐỔI):
            - **Class I:** Không triệu chứng
            - **Class II:** Triệu chứng với gắng sức bình thường
            - **Class III:** Triệu chứng với gắng sức nhẹ
            - **Class IV:** Triệu chứng khi nghỉ
            
            ---
            
            ### ACC/AHA Stage (Tiến triển bệnh - KHÔNG THỂ LÙI):
            - **Stage A:** Nguy cơ cao (ĐTĐ, THA) nhưng chưa bệnh tim
            - **Stage B:** Bệnh tim cấu trúc (EF thấp) nhưng chưa triệu chứng
            - **Stage C:** Bệnh tim cấu trúc + Triệu chứng
            - **Stage D:** Suy tim kháng trị
            
            ---
            
            ### Ví dụ:
            - **Stage B, NYHA I:** EF 30% nhưng không triệu chứng
            - **Stage C, NYHA II:** EF 35%, khó thở khi leo cầu thang
            - **Stage C, NYHA IV:** EF 20%, khó thở khi nghỉ
            - **Stage D:** Cần ghép tim/LVAD bất kể NYHA class
            
            **Lưu ý:** 
            - Cùng 1 bệnh nhân có thể cải thiện từ NYHA IV → II sau điều trị
            - Nhưng vẫn mãi mãi là Stage C (không thể lùi về B)
            """)
        
        # Exercise recommendations
        with st.expander("🏃 Khuyến cáo vận động theo NYHA"):
            st.markdown("""
            ### NYHA Class I:
            ✅ **Được phép:**
            - Tập thể dục đều đặn (150 phút/tuần)
            - Chạy bộ, bơi lội, đạp xe
            - Tập gym với tạ nhẹ
            - Hầu hết các thể thao
            
            ⚠️ **Tránh:** Thể thao thi đấu cạnh tranh nếu EF < 35%
            
            ---
            
            ### NYHA Class II:
            ✅ **Được phép:**
            - Đi bộ 30 phút/ngày
            - Đạp xe địa hình bằng phẳng
            - Bơi lội nhẹ nhàng
            - Vật lý trị liệu tim mạch (cardiac rehab)
            
            ⚠️ **Tránh:** Gắng sức quá mức, tập nặng, thể thao cạnh tranh
            
            ---
            
            ### NYHA Class III:
            ✅ **Được phép:**
            - Đi bộ chậm trong nhà
            - Vật lý trị liệu GIÁM SÁT
            - Tập thở, yoga nhẹ
            
            ⚠️ **Tránh:** Hoạt động ngoài trời không giám sát, tập nặng
            
            ---
            
            ### NYHA Class IV:
            🚫 **Nghỉ ngơi tuyệt đối hoặc hoạt động tối thiểu**
            - Chỉ làm các hoạt động cần thiết
            - Cần hỗ trợ sinh hoạt hàng ngày
            - Vật lý trị liệu rất nhẹ tại giường nếu được phép
            """)
        
        # When to seek emergency care
        with st.expander("🚨 Khi nào cần cấp cứu?"):
            st.markdown("""
            **ĐI CẤP CỨU NGAY NẾU:**
            
            🚨 **Triệu chứng cấp tính:**
            - Khó thở nghiêm trọng khi nghỉ
            - Đau ngực
            - Ngất hoặc gần ngất
            - Tim đập nhanh bất thường
            
            🚨 **Dấu hiệu xấu:**
            - Tăng cân đột ngột > 2kg trong 2-3 ngày
            - Phù chi tăng nhanh
            - Tăng khó thở rõ rệt
            - Ho nhiều đờm hồng, bọt
            
            🚨 **Kém đáp ứng điều trị:**
            - Tăng liều lợi tiểu mà không đỡ
            - Giảm lượng nước tiểu
            - Lú lẫn, mệt lả
            """)
        
        # References
        with st.expander("📚 Tài liệu tham khảo"):
            st.markdown("""
            1. **The Criteria Committee of the New York Heart Association.** 
               Nomenclature and Criteria for Diagnosis of Diseases of the Heart and Great Vessels. 
               9th ed. Boston: Little, Brown & Co; 1994:253-256.
            
            2. **Heidenreich PA, Bozkurt B, Aguilar D, et al.** 2022 AHA/ACC/HFSA Guideline for the 
               Management of Heart Failure. Circulation. 2022;145(18):e895-e1032.
            
            3. **McDonagh TA, Metra M, Adamo M, et al.** 2021 ESC Guidelines for the diagnosis and 
               treatment of acute and chronic heart failure. Eur Heart J. 2021;42(36):3599-3726.
            
            4. **Yancy CW, Jessup M, Bozkurt B, et al.** 2013 ACCF/AHA guideline for the management 
               of heart failure: a report of the American College of Cardiology Foundation/
               American Heart Association Task Force on Practice Guidelines. 
               J Am Coll Cardiol. 2013;62(16):e147-239.
            """)
    
    # Quick reference table
    st.markdown("---")
    st.markdown("### 📊 Bảng tổng hợp NYHA Classification:")
    
    st.markdown("""
    | Class | Hoạt động thể lực | Triệu chứng | Tử vong 1 năm |
    |:-----:|:------------------|:------------|:--------------|
    | **I** | Không hạn chế | Không triệu chứng với hoạt động bình thường | ~5% |
    | **II** | Hạn chế nhẹ | Triệu chứng với hoạt động bình thường (leo cầu thang, đi nhanh) | ~10-15% |
    | **III** | Hạn chế rõ | Triệu chứng với hoạt động nhẹ (đi bộ, tắm rửa) | ~20-30% |
    | **IV** | Không thể hoạt động | Triệu chứng khi nghỉ | ~40-60% |
    """)
    
    st.info("""
    💡 **Điểm quan trọng:**
    
    1. **NYHA đánh giá TRIỆU CHỨNG**, không phải chức năng tim
    
    2. **Có thể thay đổi** theo điều trị (khác với ACC/AHA Stage)
    
    3. **Hướng dẫn điều trị:**
       - Class I-II: GDMT tối ưu
       - Class III: Cân nhắc ICD/CRT
       - Class IV: Đánh giá ghép tim/LVAD
    
    4. **Không thay thế** cho đánh giá chức năng tim (EF, BNP, siêu âm)
    
    5. **Kết hợp** với ACC/AHA Stage để đánh giá toàn diện
    """)


if __name__ == "__main__":
    render()

