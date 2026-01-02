"""
Patient Education Topics - Ophthalmology
"""
from patient_education.models import PatientEducationTopic


OPHTHALMOLOGY_TOPICS = [
        PatientEducationTopic(
            id="cataract_basics",
            title="Understanding Cataract",
            title_vn="Hiểu về Đục thủy tinh thể",
            category="Disease",
            content="""
            # Hiểu về Đục thủy tinh thể

            ## Đục thủy tinh thể là gì?

            Đục thủy tinh thể là tình trạng thủy tinh thể bị đục, gây giảm thị lực, rất phổ biến ở người cao tuổi tại Việt Nam. Phẫu thuật là phương pháp điều trị duy nhất.

            **⚠️ Đặc điểm:**
            - Thủy tinh thể bị đục
            - Gây giảm thị lực
            - Rất phổ biến ở người cao tuổi
            - Phẫu thuật có thể phục hồi thị lực

            **Phân loại:**
            - **Theo tuổi:** Tuổi già (phổ biến nhất)
            - **Theo nguyên nhân:** Đái tháo đường, chấn thương, thuốc

            ## Triệu chứng:

            **Triệu chứng điển hình:**
            - **Giảm thị lực từ từ:** Mờ mắt dần
            - **Nhìn mờ:** Như có màng che
            - **Nhìn đôi:** Nếu một mắt
            - **Nhạy cảm với ánh sáng:** Chói mắt
            - **Nhìn màu kém:** Màu sắc nhạt
            - **Thay đổi độ kính thường xuyên**

            **Triệu chứng khác:**
            - Nhìn thấy hào quang quanh đèn
            - Khó nhìn ban đêm
            - Đọc sách khó

            **⚠️ Giai đoạn muộn:**
            - Thị lực giảm nhiều
            - Ảnh hưởng sinh hoạt hàng ngày
            - Có thể dẫn đến mù

            ## Nguyên nhân:

            **1. Tuổi già:**
            - Nguyên nhân chính
            - Thủy tinh thể đục tự nhiên theo tuổi

            **2. Đái tháo đường:**
            - Tăng nguy cơ
            - Đục sớm hơn

            **3. Chấn thương mắt:**
            - Chấn thương trực tiếp
            - Tia cực tím

            **4. Thuốc:**
            - Corticosteroid (uống, nhỏ mắt)

            **5. Yếu tố khác:**
            - Hút thuốc
            - Rượu bia
            - Di truyền

            ## Chẩn đoán:

            **Khám:**
            - Đo thị lực
            - Khám mắt bằng đèn khe: Thủy tinh thể đục
            - Soi đáy mắt: Giảm ánh đồng tử đỏ

            ## Điều trị:

            **1. Phẫu thuật:**
            - **Phương pháp duy nhất**
            - **Phacoemulsification:** Phẫu thuật nội soi
            - **Đặt thủy tinh thể nhân tạo (IOL)**
            - Phẫu thuật ngoại trú, phục hồi nhanh

            **2. Khi nào phẫu thuật:**
            - Thị lực giảm ảnh hưởng sinh hoạt
            - Thường khi thị lực < 20/40

            **3. Kính mắt:**
            - Tạm thời, nếu nhẹ
            - Không điều trị được

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Chống oxy hóa:**
            - **Rau xanh:** Rau bina, cải xoong
            - **Trái cây:** Cam, dâu tây
            - **Cá béo:** Omega-3

            **2. Vitamin:**
            - Vitamin C, E
            - Lutein, Zeaxanthin

            **3. Tránh:**
            - Rượu bia (tăng nguy cơ)
            - Đồ chế biến sẵn

            **4. Thực đơn mẫu:**
            - **Sáng:** Trứng, rau xanh, trái cây
            - **Trưa:** Cơm, cá, rau xanh, canh
            - **Chiều:** Cơm, thịt/cá, rau xanh, canh
            - **Bữa phụ:** Trái cây, hạt

            ## 🏃 TẬP THỂ DỤC:

            **1. Nên tập:**
            - Tập thể dục bình thường
            - Đi bộ, chạy bộ
            - 30 phút/ngày, 5 ngày/tuần

            **2. Lưu ý:**
            - Đeo kính râm khi ra nắng (bảo vệ mắt)
            - Tránh chấn thương mắt

            ## 💊 QUẢN LÝ THUỐC:

            **1. Không có thuốc điều trị:**
            - Chỉ có phẫu thuật

            **2. Sau phẫu thuật:**
            - Kháng sinh nhỏ mắt
            - Corticosteroid nhỏ mắt
            - Theo dõi định kỳ

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Thị lực giảm nhanh:**
            - Giảm đột ngột
            - Ảnh hưởng sinh hoạt

            **2. Sau phẫu thuật:**
            - Đau mắt nhiều
            - Giảm thị lực
            - Đỏ mắt nhiều

            **3. Biến chứng:**
            - Tăng nhãn áp
            - Viêm màng bồ đào

            ## 💡 PHÒNG NGỪA:

            **1. Đeo kính râm:**
            - Bảo vệ khỏi tia UV
            - Khi ra nắng

            **2. Kiểm soát đái tháo đường:**
            - Đường huyết ổn định
            - Giảm nguy cơ

            **3. Bỏ thuốc lá:**
            - Giảm nguy cơ

            **4. Khám mắt định kỳ:**
            - Sau 40 tuổi
            - Mỗi 1-2 năm

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Khi bị đục thủy tinh thể:**
            - Khám mắt định kỳ
            - Đeo kính (nếu cần)
            - Phẫu thuật khi có chỉ định

            **2. Sau phẫu thuật:**
            - Nhỏ thuốc đúng cách
            - Tránh dụi mắt
            - Khám lại định kỳ

            **3. Sống tích cực:**
            - Phẫu thuật an toàn, hiệu quả
            - Phục hồi thị lực tốt
            - Có thể sống bình thường

            **4. Phòng ngừa:**
            - Đeo kính râm
            - Kiểm soát đái tháo đường
            - Bỏ thuốc lá
            - Khám mắt định kỳ
            """,
            related_disease="cataract",
            related_drugs=[],
            printable=True
        ),

]
