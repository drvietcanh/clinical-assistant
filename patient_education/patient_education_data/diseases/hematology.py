"""
Patient Education Topics - Hematology
"""
from patient_education.models import PatientEducationTopic


HEMATOLOGY_TOPICS = [
        PatientEducationTopic(
            id="iron_deficiency_anemia_basics",
            title="Understanding Iron Deficiency Anemia",
            title_vn="Hiểu về Thiếu máu thiếu sắt",
            category="Disease",
            content="""
            # Hiểu về Thiếu máu thiếu sắt

            ## Thiếu máu thiếu sắt là gì?

            Thiếu máu thiếu sắt là tình trạng giảm hemoglobin do thiếu sắt, nguyên nhân phổ biến nhất của thiếu máu tại Việt Nam. Bệnh ảnh hưởng đến mọi lứa tuổi, đặc biệt phụ nữ và trẻ em.

            **⚠️ Đặc điểm:**
            - Giảm hemoglobin do thiếu sắt
            - Nguyên nhân thiếu máu #1 tại Việt Nam
            - Có thể điều trị khỏi
            - Cần tìm và điều trị nguyên nhân

            **Phân loại:**
            - **Thiếu sắt không thiếu máu:** Ferritin giảm, Hb bình thường
            - **Thiếu máu thiếu sắt:** Ferritin giảm, Hb giảm

            ## Triệu chứng:

            **Triệu chứng thiếu máu:**
            - **Mệt mỏi, suy nhược:** Uể oải, không có sức
            - **Da xanh, niêm mạc nhợt:** Môi, lưỡi, kết mạc nhợt
            - **Khó thở khi gắng sức:** Leo cầu thang, đi bộ
            - **Đánh trống ngực:** Tim đập nhanh
            - **Đau đầu, chóng mặt:** Đặc biệt khi đứng dậy
            - **Tóc rụng, móng tay dễ gãy:** Móng tay lõm (koilonychia)

            **Triệu chứng thiếu sắt:**
            - **Viêm lưỡi:** Lưỡi đỏ, đau
            - **Khó nuốt:** Plummer-Vinson syndrome (hiếm)
            - **Thèm ăn lạ:** Pica (thèm đất, đá, đá lạnh)

            **⚠️ Thiếu máu nặng:**
            - Khó thở ngay cả khi nghỉ
            - Đau ngực
            - Suy tim (nếu kéo dài)

            ## Nguyên nhân:

            **1. Mất máu mạn tính (nguyên nhân chính):**
            - **Xuất huyết tiêu hóa:** Loét dạ dày, ung thư đại tràng, trĩ
            - **Kinh nguyệt nhiều:** Phụ nữ
            - **Giun móc:** Vùng nông thôn
            - **Xuất huyết tiết niệu:** Ung thư bàng quang, thận

            **2. Thiếu cung cấp:**
            - Chế độ ăn thiếu sắt
            - Ăn chay
            - Kém hấp thu

            **3. Tăng nhu cầu:**
            - Mang thai
            - Trẻ em đang lớn
            - Cho con bú

            **4. Rối loạn hấp thu:**
            - Bệnh celiac
            - Cắt dạ dày
            - Viêm ruột

            ## Chẩn đoán:

            **Xét nghiệm:**
            - **Hemoglobin giảm:** Nam < 13 g/dL, nữ < 12 g/dL
            - **MCV giảm:** < 80 fL (microcytic anemia)
            - **Ferritin giảm:** < 15 ng/mL (tiêu chuẩn vàng)
            - **Sắt huyết thanh giảm**
            - **TIBC tăng**
            - **Transferrin saturation < 15%**

            **Tìm nguyên nhân:**
            - Nội soi dạ dày tá tràng (nếu nghi ngờ xuất huyết tiêu hóa)
            - Xét nghiệm phân (tìm máu ẩn, giun móc)
            - Nội soi đại tràng (nếu cần)

            ## Điều trị:

            **1. Điều trị nguyên nhân:**
            - Cầm máu (nếu xuất huyết)
            - Tẩy giun (nếu giun móc)
            - Điều trị bệnh tiêu hóa

            **2. Bổ sung sắt:**
            - **Sắt uống:** Ferrous sulfate 325mg x 1-2 lần/ngày
            - **Uống sau ăn:** Giảm tác dụng phụ
            - **Với vitamin C:** Tăng hấp thu (nước cam, viên C)
            - **Thời gian:** 3-6 tháng (đến khi ferritin bình thường)

            **3. Sắt tiêm tĩnh mạch:**
            - Nếu không dung nạp sắt uống
            - Nếu cần tăng nhanh
            - Nếu kém hấp thu

            **4. Truyền máu:**
            - Nếu thiếu máu nặng, có triệu chứng
            - Hb < 7 g/dL hoặc có triệu chứng nặng

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Thực phẩm giàu sắt:**
            - **Sắt heme (hấp thu tốt):** Thịt đỏ, gan, thịt gà, cá, hải sản
            - **Sắt non-heme:** Rau xanh (rau muống, cải xoong), đậu, hạt, ngũ cốc

            **2. Tăng hấp thu sắt:**
            - **Vitamin C:** Nước cam, ớt chuông, cà chua, bông cải xanh
            - **Thịt, cá:** Ăn cùng rau xanh (tăng hấp thu sắt non-heme)

            **3. Giảm hấp thu sắt (tránh):**
            - **Trà, cà phê:** Uống cách xa bữa ăn 1-2 giờ
            - **Canxi:** Uống cách xa bữa ăn
            - **Phytate:** Ngũ cốc nguyên hạt (ngâm, nấu chín giảm tác dụng)

            **4. Thực đơn mẫu:**
            - **Sáng:** Cháo thịt bằm, trứng, nước cam
            - **Trưa:** Cơm, thịt bò/cá, rau muống xào, canh chua, trái cây
            - **Chiều:** Cơm, gan xào, rau xanh, canh, trái cây
            - **Bữa phụ:** Hạt, sữa

            **5. Lưu ý:**
            - Ăn đủ protein (tạo hemoglobin)
            - Bổ sung acid folic, B12 (nếu thiếu)

            ## 🏃 TẬP THỂ DỤC:

            **1. Khi thiếu máu nặng:**
            - Nghỉ ngơi, tránh gắng sức
            - Tập nhẹ: Đi bộ 10-15 phút/ngày

            **2. Khi đã cải thiện:**
            - Tập bình thường
            - Đi bộ, chạy bộ, bơi lội
            - 30 phút/ngày, 5 ngày/tuần
            - **Lợi ích:** Tăng sức khỏe, cải thiện tuần hoàn

            **3. Lưu ý:**
            - Nghỉ ngơi nếu mệt
            - Uống đủ nước
            - Tăng dần cường độ

            ## 💊 QUẢN LÝ THUỐC:

            **1. Sắt uống:**
            - **Ferrous sulfate:** 325mg x 1-2 lần/ngày
            - **Uống sau ăn:** Giảm tác dụng phụ
            - **Với vitamin C:** Tăng hấp thu
            - **Không uống với:** Trà, cà phê, canxi, sữa

            **2. Tác dụng phụ:**
            - **Táo bón:** Uống nhiều nước, ăn nhiều chất xơ
            - **Buồn nôn:** Uống sau ăn, giảm liều
            - **Phân đen:** Bình thường (không phải xuất huyết)
            - **Đau bụng:** Uống sau ăn, giảm liều

            **3. Theo dõi:**
            - Hb, ferritin sau 4-6 tuần
            - Tiếp tục đến khi ferritin bình thường (3-6 tháng)

            **4. Lưu ý:**
            - Không tự ý ngừng (thiếu máu tái phát)
            - Uống đều đặn

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Thiếu máu nặng:**
            - Khó thở ngay cả khi nghỉ
            - Đau ngực
            - Ngất xỉu
            - **Cần truyền máu**

            **2. Xuất huyết:**
            - Nôn ra máu
            - Đi ngoài phân đen
            - Chảy máu nhiều

            **3. Không cải thiện:**
            - Sau 4-6 tuần điều trị
            - Cần tìm nguyên nhân khác

            ## 💡 PHÒNG NGỪA:

            **1. Chế độ ăn:**
            - Ăn đủ thực phẩm giàu sắt
            - Bổ sung vitamin C
            - Tránh trà, cà phê trong bữa ăn

            **2. Phụ nữ:**
            - Bổ sung sắt khi mang thai
            - Điều trị kinh nguyệt nhiều

            **3. Trẻ em:**
            - Ăn đủ thực phẩm giàu sắt
            - Tẩy giun định kỳ

            **4. Tìm nguyên nhân:**
            - Khám định kỳ
            - Xét nghiệm phân (tìm giun móc)
            - Nội soi (nếu nghi ngờ xuất huyết tiêu hóa)

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Khi bị thiếu máu:**
            - Uống sắt đều đặn
            - Ăn đủ thực phẩm giàu sắt
            - Tìm và điều trị nguyên nhân

            **2. Uống sắt đúng cách:**
            - Sau ăn, với vitamin C
            - Không với trà, cà phê, canxi
            - Uống đều đặn, đủ thời gian

            **3. Sống tích cực:**
            - Thiếu máu thiếu sắt có thể chữa khỏi
            - Điều trị đúng → Hb, ferritin bình thường
            - Có thể sống bình thường

            **4. Mang thai:**
            - Bổ sung sắt (30-60mg/ngày)
            - Bổ sung acid folic
            - Theo dõi Hb định kỳ
            """,
            related_disease="iron_deficiency_anemia",
            related_drugs=["Ferrous Sulfate", "Iron IV"],
            printable=True
        ),

        PatientEducationTopic(
            id="thrombocytopenia_basics",
            title="Understanding Thrombocytopenia",
            title_vn="Hiểu về Giảm tiểu cầu",
            category="Disease",
            content="""
            # Hiểu về Giảm tiểu cầu

            ## Giảm tiểu cầu là gì?

            Giảm tiểu cầu là tình trạng số lượng tiểu cầu trong máu thấp (< 150,000/μL), có thể gây chảy máu. Bệnh có thể do nhiều nguyên nhân, từ nhẹ đến nặng.

            **⚠️ Đặc điểm:**
            - Số lượng tiểu cầu thấp
            - Có thể gây chảy máu
            - Nhiều nguyên nhân
            - Từ nhẹ đến nặng

            **Phân loại:**
            - **Nhẹ:** 100,000-150,000/μL (thường không có triệu chứng)
            - **Vừa:** 50,000-100,000/μL (có thể chảy máu khi chấn thương)
            - **Nặng:** < 50,000/μL (chảy máu tự phát)
            - **Rất nặng:** < 20,000/μL (chảy máu nặng)

            ## Triệu chứng:

            **Triệu chứng điển hình:**
            - **Chảy máu:** Chảy máu cam, chảy máu lợi
            - **Xuất huyết da:** Nốt xuất huyết, ban xuất huyết, bầm tím
            - **Xuất huyết tiêu hóa:** Nôn ra máu, đi ngoài phân đen
            - **Xuất huyết tiết niệu:** Đi tiểu ra máu
            - **Kinh nguyệt nhiều:** Ở phụ nữ

            **⚠️ Chảy máu nặng:**
            - Xuất huyết não (nguy hiểm!)
            - Xuất huyết tiêu hóa nặng
            - **Cấp cứu ngay!**

            **⚠️ Không có triệu chứng:**
            - Nhiều người không có triệu chứng
            - Phát hiện khi xét nghiệm máu

            ## Nguyên nhân:

            **1. Giảm sản xuất:**
            - **Bệnh tủy xương:** Ung thư máu, suy tủy
            - **Thuốc:** Hóa trị, một số thuốc
            - **Nhiễm virus:** HIV, viêm gan C
            - **Thiếu vitamin:** B12, Folate

            **2. Tăng phá hủy:**
            - **ITP (Giảm tiểu cầu miễn dịch):** Tự miễn
            - **Heparin:** Gây giảm tiểu cầu do heparin
            - **Nhiễm khuẩn:** Nhiễm khuẩn huyết
            - **DIC:** Đông máu rải rác trong lòng mạch

            **3. Tăng tiêu thụ:**
            - **Lách to:** Giữ tiểu cầu
            - **Huyết khối:** Tiêu thụ tiểu cầu

            **4. Yếu tố nguy cơ:**
            - Nhiễm virus
            - Thuốc
            - Bệnh tự miễn
            - Ung thư

            ## Chẩn đoán:

            **Xét nghiệm:**
            - **Công thức máu:** Số lượng tiểu cầu
            - **Kính phết máu:** Đánh giá hình dạng tiểu cầu
            - **Tủy đồ:** Nếu nghi ngờ bệnh tủy xương
            - **Xét nghiệm đông máu:** PT, PTT, Fibrinogen
            - **Kháng thể:** Nếu nghi ngờ ITP

            ## Điều trị:

            **1. Điều trị nguyên nhân:**
            - Điều trị bệnh nền
            - Ngừng thuốc gây giảm tiểu cầu
            - Điều trị nhiễm khuẩn

            **2. ITP (Giảm tiểu cầu miễn dịch):**
            - **Corticosteroid:** Prednisone (tăng tiểu cầu)
            - **IVIG:** Immunoglobulin tĩnh mạch (nếu nặng)
            - **Rituximab:** Nếu kháng Corticosteroid
            - **Cắt lách:** Nếu kháng thuốc

            **3. Truyền tiểu cầu:**
            - Nếu chảy máu nặng
            - Trước phẫu thuật nếu tiểu cầu thấp

            **4. Điều trị hỗ trợ:**
            - Tránh chấn thương
            - Tránh thuốc chống đông, Aspirin

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Bình thường:**
            - Ăn uống bình thường
            - Ăn đủ dinh dưỡng

            **2. Nếu thiếu vitamin:**
            - Bổ sung B12, Folate (nếu thiếu)
            - Thịt, cá, trứng, rau xanh

            **3. Tránh:**
            - Rượu bia (ảnh hưởng tủy xương)
            - Thức ăn cứng (nếu chảy máu lợi)

            **4. Thực đơn mẫu:**
            - **Sáng:** Cháo/cơm, thịt/cá, trái cây
            - **Trưa:** Cơm, thịt/cá, rau xanh, canh
            - **Chiều:** Cơm, thịt/cá, rau xanh, canh
            - **Bữa phụ:** Trái cây, sữa

            ## 🏃 TẬP THỂ DỤC:

            **1. Khi tiểu cầu thấp:**
            - Tránh thể thao va chạm
            - Tránh gắng sức quá mức
            - Tập thể dục nhẹ nhàng

            **2. Khi tiểu cầu bình thường:**
            - Tập thể dục bình thường
            - 30 phút/ngày, 5 ngày/tuần

            ## 💊 QUẢN LÝ THUỐC:

            **1. Corticosteroid:**
            - Prednisone: Uống đều đặn
            - Giảm liều từ từ (tránh tái phát)
            - Theo dõi tác dụng phụ

            **2. Tránh:**
            - **Aspirin:** Làm tăng chảy máu
            - **Thuốc chống đông:** Nếu không có chỉ định
            - **NSAID:** Ibuprofen, Naproxen

            **3. Lưu ý:**
            - Uống đúng giờ, đúng liều
            - Báo bác sĩ nếu chảy máu
            - Không tự ý ngừng thuốc

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Chảy máu nặng:**
            - Chảy máu không cầm được
            - Nôn ra máu, đi ngoài phân đen
            - Đi tiểu ra máu
            - **Cấp cứu ngay!**

            **2. Xuất huyết não:**
            - Đau đầu dữ dội
            - Yếu liệt, rối loạn ý thức
            - **Cấp cứu ngay!**

            **3. Tiểu cầu rất thấp:**
            - < 20,000/μL
            - Có nguy cơ chảy máu nặng

            **4. Triệu chứng mới:**
            - Xuất huyết da mới
            - Chảy máu mới

            ## 💡 PHÒNG NGỪA:

            **1. Tránh chấn thương:**
            - Tránh thể thao va chạm
            - Cẩn thận khi vận động
            - Mang bảo vệ nếu cần

            **2. Tránh thuốc:**
            - Tránh Aspirin, NSAID
            - Báo bác sĩ tất cả thuốc đang dùng

            **3. Điều trị nguyên nhân:**
            - Điều trị bệnh nền
            - Ngừng thuốc gây giảm tiểu cầu

            **4. Khám định kỳ:**
            - Xét nghiệm máu định kỳ
            - Theo dõi số lượng tiểu cầu

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Khi bị giảm tiểu cầu:**
            - Tránh chấn thương (quan trọng!)
            - Tránh Aspirin, NSAID
            - Uống thuốc đều đặn
            - Theo dõi dấu hiệu chảy máu

            **2. Chảy máu:**
            - Báo bác sĩ ngay nếu chảy máu
            - Đến bệnh viện nếu chảy máu nặng
            - Tránh gãi, va chạm

            **3. Sống tích cực:**
            - Giảm tiểu cầu có thể điều trị
            - Điều trị đúng → Tăng tiểu cầu, giảm chảy máu
            - Có thể sống bình thường

            **4. Theo dõi:**
            - Xét nghiệm máu định kỳ
            - Theo dõi triệu chứng
            - Khám định kỳ
            """,
            related_disease="thrombocytopenia",
            related_drugs=["Prednisone", "IVIG", "Rituximab", "Platelet Transfusion"],
            printable=True
        ),

]
