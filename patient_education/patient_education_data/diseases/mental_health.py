"""
Patient Education Topics - Mental_Health
"""
from patient_education.models import PatientEducationTopic


MENTAL_HEALTH_TOPICS = [
        PatientEducationTopic(
            id="depression_basics",
            title="Understanding Depression",
            title_vn="Hiểu về Trầm cảm",
            category="Disease",
            content="""
    # Hiểu về Trầm cảm

    ## Trầm cảm là gì?

    Trầm cảm là bệnh tâm thần gây cảm giác buồn bã, mất hứng thú kéo dài.

    ## Triệu chứng:
    - Buồn bã, chán nản kéo dài
    - Mất hứng thú với mọi thứ
    - Mệt mỏi, thiếu năng lượng
    - Khó tập trung
    - Thay đổi giấc ngủ (mất ngủ hoặc ngủ nhiều)
    - Thay đổi ăn uống
    - Cảm giác vô giá trị, tội lỗi
    - Ý nghĩ tự tử

    ## Nguyên nhân:
    - Di truyền
    - Mất cân bằng hóa chất não
    - Stress, sang chấn tâm lý
    - Bệnh mạn tính
    - Một số thuốc

    ## Điều trị:
    - **Thuốc chống trầm cảm:** Uống đúng giờ, đủ thời gian
    - **Tâm lý trị liệu:** Nói chuyện với chuyên gia
    - **Thay đổi lối sống:** Tập thể dục, ngủ đủ
    - **Hỗ trợ:** Gia đình, bạn bè

    ## ⚠️ QUAN TRỌNG:
    - Trầm cảm là BỆNH, không phải yếu đuối
    - Cần điều trị, không tự khỏi
    - Thuốc cần thời gian mới có tác dụng (2-4 tuần)
    - Không tự ý ngừng thuốc

    ## Khi nào cần cấp cứu:
    - Ý nghĩ tự tử
    - Có kế hoạch tự tử
    - Không thể chăm sóc bản thân
    - Hoang tưởng, ảo giác

    ## Lời khuyên:
    - Điều trị sớm
    - Uống thuốc đúng giờ
    - Tâm lý trị liệu
    - Tập thể dục
    - Ngủ đủ giấc
    - Nói chuyện với người thân
    - Không tự ý ngừng thuốc
            """,
            related_disease="depression",
            related_drugs=["Sertraline", "Fluoxetine", "Escitalopram"],
            printable=True
        ),

        PatientEducationTopic(
            id="anxiety_disorder_basics",
            title="Understanding Anxiety Disorder",
            title_vn="Hiểu về Rối loạn lo âu",
            category="Disease",
            content="""
            # Hiểu về Rối loạn lo âu

            ## Rối loạn lo âu là gì?

            Rối loạn lo âu là nhóm bệnh đặc trưng bởi lo âu, sợ hãi quá mức, ảnh hưởng đến cuộc sống hàng ngày. Bệnh rất phổ biến, có thể điều trị hiệu quả.

            **⚠️ Đặc điểm:**
            - Lo âu, sợ hãi quá mức
            - Ảnh hưởng cuộc sống hàng ngày
            - Rất phổ biến (20% dân số)
            - Có thể điều trị hiệu quả

            **Phân loại:**
            - **GAD (Generalized Anxiety Disorder):** Lo âu lan tỏa
            - **Panic Disorder:** Cơn hoảng sợ
            - **Social Anxiety:** Lo âu xã hội
            - **Phobia:** Ám ảnh sợ

            ## Triệu chứng:

            **Triệu chứng tâm thần:**
            - **Lo âu, lo lắng quá mức:** Kéo dài
            - **Bồn chồn, căng thẳng**
            - **Khó tập trung**
            - **Sợ hãi:** Sợ điều tồi tệ sẽ xảy ra

            **Triệu chứng thể chất:**
            - **Đánh trống ngực:** Tim đập nhanh
            - **Khó thở:** Cảm giác nghẹt thở
            - **Đổ mồ hôi:** Lòng bàn tay, nách
            - **Run tay**
            - **Chóng mặt**
            - **Buồn nôn**
            - **Rối loạn giấc ngủ**

            **Cơn hoảng sợ (Panic Attack):**
            - Lo âu dữ dội đột ngột
            - Đánh trống ngực, khó thở
            - Cảm giác sắp chết
            - Kéo dài 10-30 phút

            ## Nguyên nhân:

            **1. Yếu tố di truyền:**
            - Tiền sử gia đình

            **2. Yếu tố môi trường:**
            - Stress, sang chấn
            - Căng thẳng công việc, gia đình

            **3. Rối loạn chất dẫn truyền thần kinh:**
            - Serotonin, norepinephrine

            **4. Bệnh thực thể:**
            - Cường giáp
            - Rối loạn nhịp tim

            ## Chẩn đoán:

            **Tiêu chuẩn:**
            - Triệu chứng lo âu kéo dài ≥ 6 tháng
            - Ảnh hưởng chức năng hàng ngày
            - Loại trừ: do chất, bệnh thực thể

            ## Điều trị:

            **1. SSRI (thuốc đầu tay):**
            - Sertraline, Escitalopram
            - Bắt đầu liều thấp, tăng dần
            - Cần 2-4 tuần để thấy hiệu quả

            **2. Liệu pháp tâm lý:**
            - CBT (Cognitive Behavioral Therapy)
            - Rất hiệu quả

            **3. Benzodiazepine (ngắn hạn):**
            - Alprazolam, Lorazepam
            - Cơn cấp, ngắn hạn
            - **Không dùng lâu dài** (gây nghiện)

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Tránh:**
            - **Caffeine:** Cà phê, trà, nước ngọt (kích thích lo âu)
            - **Rượu bia:** Tạm thời giảm, nhưng tăng lo âu sau
            - **Đường:** Tăng và giảm đường huyết → Lo âu

            **2. Nên ăn:**
            - **Thực phẩm giàu tryptophan:** Chuối, sữa, gà tây
            - **Omega-3:** Cá béo
            - **Magnesium:** Rau xanh, hạt
            - **Ăn đều đặn:** Không bỏ bữa

            **3. Thực đơn mẫu:**
            - **Sáng:** Cháo yến mạch, sữa, trái cây
            - **Trưa:** Cơm, cá, rau xanh, canh
            - **Chiều:** Cơm, thịt/cá, rau xanh, canh
            - **Bữa phụ:** Hạt, sữa

            ## 🏃 TẬP THỂ DỤC:

            **1. Quan trọng!**
            - Tập thể dục đều đặn (giảm lo âu rất hiệu quả)
            - Giải phóng endorphin

            **2. Loại bài tập:**
            - **Đi bộ, chạy bộ:** 30 phút/ngày
            - **Yoga, thiền:** Rất tốt cho lo âu
            - **Bơi lội:** Thư giãn
            - **5 ngày/tuần**

            **3. Lưu ý:**
            - Bắt đầu nhẹ, tăng dần
            - Tập đều đặn (quan trọng!)

            ## 💊 QUẢN LÝ THUỐC:

            **1. SSRI:**
            - Sertraline, Escitalopram
            - Uống đều đặn, đúng giờ
            - Cần 2-4 tuần để thấy hiệu quả
            - **Không tự ý ngừng** (triệu chứng tái phát)

            **2. Tác dụng phụ:**
            - Buồn nôn (tạm thời)
            - Buồn ngủ hoặc mất ngủ
            - Giảm ham muốn tình dục

            **3. Lưu ý:**
            - Uống đủ thời gian (6-12 tháng)
            - Giảm dần liều khi ngừng

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Cơn hoảng sợ:**
            - Lo âu dữ dội
            - Đánh trống ngực, khó thở
            - Cảm giác sắp chết

            **2. Ý nghĩ tự tử:**
            - **Cấp cứu ngay!**

            **3. Triệu chứng nặng:**
            - Không thể làm việc
            - Không thể ra khỏi nhà

            ## 💡 PHÒNG NGỪA:

            **1. Quản lý stress:**
            - Tập thể dục
            - Yoga, thiền
            - Ngủ đủ giấc

            **2. Tránh:**
            - Caffeine
            - Rượu bia
            - Stress quá mức

            **3. Hỗ trợ:**
            - Nói chuyện với người thân
            - Tư vấn tâm lý

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Khi bị lo âu:**
            - Uống thuốc đều đặn
            - Tập thể dục (quan trọng!)
            - Tránh caffeine, rượu bia
            - Quản lý stress

            **2. Kỹ thuật thư giãn:**
            - Thở sâu (4-7-8)
            - Thiền
            - Yoga

            **3. Sống tích cực:**
            - Rối loạn lo âu có thể điều trị hiệu quả
            - Điều trị đúng → Giảm triệu chứng
            - Có thể sống bình thường

            **4. Hỗ trợ:**
            - Tham gia nhóm hỗ trợ
            - Tư vấn tâm lý
            - Nói chuyện với người thân
            """,
            related_disease="anxiety_disorder",
            related_drugs=["Sertraline", "Escitalopram", "Alprazolam", "Lorazepam", "Propranolol"],
            printable=True
        ),

]
