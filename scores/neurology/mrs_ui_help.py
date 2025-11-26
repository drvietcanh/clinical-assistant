"""
mRS Calculator - Help Sections and Expanders
Handles all help content and educational expanders
"""

import streamlit as st


def render_important_notes():
    """Render important notes about mRS"""
    st.markdown("---")
    st.info(f"""
    **📌 LƯU Ý QUAN TRỌNG VỀ mRS:**
    
    **1. Thời điểm đánh giá:**
    - **3 tháng sau đột quỵ** là thời điểm chuẩn trong nghiên cứu lâm sàng
    - Cũng có thể đánh giá tại: xuất viện, 1 tháng, 6 tháng, 1 năm
    - mRS có thể thay đổi theo thời gian (thường cải thiện trong 6-12 tháng đầu)
    
    **2. mRS trong nghiên cứu đột quỵ:**
    - **Primary endpoint** trong hầu hết nghiên cứu về đột quỵ
    - **Kết cục tốt** thường định nghĩa là: mRS 0-2 (độc lập)
    - **Kết cục xấu:** mRS 3-6 (phụ thuộc hoặc tử vong)
    
    **3. Các yếu tố ảnh hưởng mRS:**
    - Mức độ nặng đột quỵ ban đầu (NIHSS)
    - Vị trí, kích thước tổn thương
    - Tuổi (càng cao càng xấu)
    - Bệnh đi kèm
    - Thời gian được điều trị (thời gian đến bệnh viện)
    - Chất lượng phục hồi chức năng
    
    **4. Hạn chế của mRS:**
    - **Chủ quan:** Phụ thuộc người đánh giá
    - **Không chi tiết:** Không phân biệt giữa các loại khuyết tật (vận động vs nhận thức)
    - **Hiệu ứng trần/sàn:** Không nhạy với thay đổi nhỏ ở hai đầu thang điểm
    - **Khó phân biệt:** Đặc biệt là giữa mRS 2 vs 3, và 3 vs 4
    
    **5. Các thang điểm bổ sung:**
    - **Barthel Index:** Đánh giá chi tiết hơn ADL
    - **FIM (Functional Independence Measure):** Phục hồi chức năng
    - **NIHSS:** Đánh giá thần kinh học
    - **MoCA/MMSE:** Đánh giá nhận thức
    
    **6. "Good outcome" (mRS 0-2):**
    - Mục tiêu của điều trị đột quỵ cấp (thrombolysis, thrombectomy)
    - **Number Needed to Treat (NNT)** thường tính dựa trên tỷ lệ đạt mRS 0-2
    
    **7. Cân nhắc văn hóa:**
    - Khái niệm "phụ thuộc" có thể khác nhau giữa các nền văn hóa
    - Tại Việt Nam: Gia đình thường hỗ trợ nhiều hơn → Cần đánh giá kỹ khả năng thực sự của bệnh nhân
    """)


def render_comparison_table():
    """Render comparison table expander"""
    with st.expander("📊 Bảng So Sánh mRS Scores"):
        st.markdown("""
        | mRS | Mô Tả | Đi Lại | Tự Chăm Sóc | Độc Lập | Kết Cục |
        |-----|-------|--------|-------------|---------|---------|
        | **0** | Không triệu chứng | ✅ Bình thường | ✅ Hoàn toàn | ✅ Hoàn toàn | 🟢 Excellent |
        | **1** | Triệu chứng nhẹ | ✅ Bình thường | ✅ Hoàn toàn | ✅ Hoàn toàn | 🟢 Excellent |
        | **2** | Khuyết tật nhẹ | ✅ Độc lập | ✅ Tự chăm sóc | ✅ Độc lập | 🟢 Good |
        | **3** | Khuyết tật trung bình | ✅ Không cần nâng | ⚠️ Cần giúp đỡ | ⚠️ Một phần | 🟡 Moderate |
        | **4** | Khuyết tật vừa nặng | ❌ Cần người đỡ | ❌ Cần giúp | ❌ Phụ thuộc | 🔴 Poor |
        | **5** | Khuyết tật nặng | ❌ Nằm giường | ❌ Cần chăm sóc 24/7 | ❌ Hoàn toàn | 🔴 Very Poor |
        | **6** | Tử vong | N/A | N/A | N/A | ⚫ Death |
        
        **Phân loại kết cục:**
        - **Good outcome:** mRS 0-2 (độc lập)
        - **Poor outcome:** mRS 3-6 (phụ thuộc hoặc tử vong)
        """)


def render_barthel_comparison():
    """Render Barthel Index comparison expander"""
    with st.expander("🔄 mRS vs Barthel Index"):
        st.markdown("""
        **Barthel Index** là thang điểm chi tiết hơn để đánh giá ADL (Activities of Daily Living).
        
        **So sánh tương đương (xấp xỉ):**
        
        | mRS | Barthel Index | Diễn giải |
        |-----|---------------|-----------|
        | 0-1 | 100 | Hoàn toàn độc lập |
        | 2 | 95 | Gần như độc lập |
        | 3 | 60-90 | Cần giúp đỡ một phần |
        | 4 | 25-55 | Phụ thuộc nặng |
        | 5 | 0-20 | Phụ thuộc hoàn toàn |
        
        **Ưu điểm của Barthel:**
        - Chi tiết hơn (10 mục ADL)
        - Nhạy hơn với thay đổi nhỏ
        - Hữu ích cho theo dõi phục hồi chức năng
        
        **Ưu điểm của mRS:**
        - Đơn giản, nhanh
        - Tiêu chuẩn trong nghiên cứu đột quỵ
        - Dễ so sánh giữa các nghiên cứu
        """)


def render_references():
    """Render references expander"""
    with st.expander("📚 Tài Liệu Tham Khảo"):
        st.markdown("""
        **Primary References:**
        - Rankin J. *Cerebral vascular accidents in patients over the age of 60. II. Prognosis.* 
          Scott Med J. 1957 May;2(5):200-15. [PMID: 13432835]
        
        - van Swieten JC, Koudstaal PJ, Visser MC, Schouten HJ, van Gijn J. 
          *Interobserver agreement for the assessment of handicap in stroke patients.* 
          Stroke. 1988 May;19(5):604-7. [PMID: 3363593]
        
        **Structured Interview:**
        - Bruno A, Akinwuntan AE, Lin C, et al. 
          *Simplified modified rankin scale questionnaire: reproducibility over the telephone and validation with quality of life.* 
          Stroke. 2011;42(8):2276-9.
        
        **In Clinical Trials:**
        - Saver JL, Filip B, Hamilton S, et al. 
          *Improving the reliability of stroke disability grading in clinical trials and clinical practice: the Rankin Focused Assessment (RFA).* 
          Stroke. 2010;41(5):992-5.
        
        **Guidelines:**
        - Powers WJ, et al. *Guidelines for the Early Management of Patients With Acute Ischemic Stroke.* 
          Stroke. 2019;50(12):e344-e418.
        
        - Quinn TJ, Dawson J, Walters MR, Lees KR. 
          *Reliability of the modified Rankin Scale: a systematic review.* 
          Stroke. 2009;40(10):3393-5.
        """)


def render_assessment_guide():
    """Render assessment guide expander"""
    with st.expander("❓ Cách Đánh Giá mRS Chính Xác"):
        st.markdown("""
        **Cách tiếp cận có cấu trúc để đánh giá mRS:**
        
        **Bước 1: Hỏi về triệu chứng**
        - "Bạn có triệu chứng gì từ cơn đột quỵ không?"
        - Nếu KHÔNG → mRS 0
        - Nếu CÓ → Tiếp bước 2
        
        **Bước 2: Hỏi về hoạt động thường ngày**
        - "Bạn có thể làm tất cả những gì bạn làm trước đột quỵ không?"
        - Nếu CÓ → mRS 1
        - Nếu KHÔNG → Tiếp bước 3
        
        **Bước 3: Hỏi về tự chăm sóc**
        - "Bạn có thể tự chăm sóc bản thân không cần ai giúp không?" (tắm, vệ sinh, ăn uống, mặc quần áo)
        - Nếu CÓ → mRS 2
        - Nếu KHÔNG → Tiếp bước 4
        
        **Bước 4: Hỏi về đi lại**
        - "Bạn có thể đi lại mà không cần ai nâng đỡ không?" (dùng gậy OK)
        - Nếu CÓ → mRS 3
        - Nếu KHÔNG → Tiếp bước 5
        
        **Bước 5: Hỏi về nằm giường và tiểu tiện**
        - "Bạn có nằm liệt giường và không tự chủ tiểu tiện không?"
        - Nếu CÓ → mRS 5
        - Nếu KHÔNG → mRS 4
        
        **Lưu ý:**
        - Đánh giá dựa trên **khả năng thực sự**, không phải **tiềm năng**
        - Đánh giá **trạng thái hiện tại**, không phải trạng thái tốt nhất
        - Nếu bệnh nhân cần giúp đỡ vì lý do khác (không phải đột quỵ), cần cân nhắc riêng
        """)


def render_clinical_decisions():
    """Render clinical decisions expander"""
    with st.expander("🎯 mRS Trong Quyết Định Lâm Sàng"):
        st.markdown("""
        **mRS được sử dụng để quyết định điều trị:**
        
        **1. Thrombolysis (Tiêu sợi huyết):**
        - Mục tiêu: Tăng tỷ lệ mRS 0-2 tại 3 tháng
        - Trong thực tế: mRS trước đột quỵ (pre-stroke mRS) quan trọng
        - Nếu pre-stroke mRS ≥2: Cân nhắc lợi ích/nguy cơ cẩn thận
        
        **2. Thrombectomy (Lấy huyết khối):**
        - Mục tiêu: mRS 0-2 tại 90 ngày
        - Tiêu chí: Pre-stroke mRS thường ≤1 (một số nghiên cứu ≤2)
        - NNT = 3-5 để có thêm 1 người đạt mRS 0-2
        
        **3. Decompressive Craniectomy (Mở hộp sọ giảm áp):**
        - Giảm tử vong nhưng có thể tăng mRS 4-5
        - Cần thảo luận với gia đình: Sống với khuyết tật nặng vs tử vong
        - Tuổi <60, GCS >8: Tiên lượng tốt hơn
        
        **4. Quyết định DNR/Comfort Care:**
        - Dự đoán mRS ≥5: Có thể cân nhắc comfort care
        - Nhưng KHÔNG nên quyết định quá sớm (đợi ít nhất 72h)
        - Cân nhắc ý muốn bệnh nhân, gia đình
        
        **5. Chỉ định phục hồi chức năng:**
        - mRS 2-4: Hưởng lợi nhiều nhất từ rehab
        - mRS 5: Rehab để phòng biến chứng
        - mRS 0-1: Có thể rehab ngoại trú
        """)


def render_common_mistakes():
    """Render common mistakes expander"""
    with st.expander("⚠️ Những Sai Lầm Thường Gặp"):
        st.markdown("""
        **1. Đánh giá dựa trên tiềm năng thay vì thực tế:**
        - ❌ SAI: "Bệnh nhân CÓ THỂ tự tắm nếu cố gắng" → mRS 2
        - ✅ ĐÚNG: "Bệnh nhân THỰC TẾ cần giúp đỡ tắm" → mRS 3 hoặc 4
        
        **2. Nhầm lẫn giữa sử dụng dụng cụ vs cần người giúp:**
        - Dùng gậy đi lại → Vẫn "đi lại độc lập" → mRS 0-3
        - Cần người nâng đỡ đi lại → "Không đi lại độc lập" → mRS 4-5
        
        **3. Đánh giá quá sớm:**
        - mRS dao động nhiều trong 1-2 tuần đầu
        - Nên đánh giá tại thời điểm ổn định (ví dụ: khi xuất viện, 3 tháng)
        
        **4. Bỏ qua pre-stroke mRS:**
        - Bệnh nhân đã mRS 3 trước đột quỵ → Sau đột quỵ vẫn mRS 3 → Không tệ đi
        - Quan trọng so sánh với baseline
        
        **5. Nhầm giữa mRS 3 và 4:**
        - **Câu hỏi then chốt:** "Đi lại có cần người nâng đỡ không?"
        - Nếu CẦN → mRS 4
        - Nếu KHÔNG CẦN (dù dùng gậy) → mRS 3
        
        **6. Đánh giá không khách quan:**
        - Cần hỏi cụ thể, quan sát thực tế
        - Nếu có thể, dùng structured interview (câu hỏi chuẩn)
        - Hỏi gia đình/người chăm sóc để xác nhận
        """)


def render_footer():
    """Render footer"""
    st.markdown("---")
    st.caption("📚 Based on: Rankin 1957, van Swieten et al. 1988")
    st.caption("⚠️ Most commonly used outcome measure in stroke trials")
    st.caption("🎯 Good outcome = mRS 0-2 (functional independence)")

