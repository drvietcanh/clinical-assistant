"""
Patient Education Topics - Obstetrics_Gynecology
"""
from patient_education.models import PatientEducationTopic


OBSTETRICS_GYNECOLOGY_TOPICS = [
        PatientEducationTopic(
            id="pelvic_inflammatory_disease_basics",
            title="Understanding Pelvic Inflammatory Disease",
            title_vn="Hiểu về Viêm nhiễm phụ khoa",
            category="Disease",
            content="""
            # Hiểu về Viêm nhiễm phụ khoa

            ## Viêm nhiễm phụ khoa là gì?

            Viêm nhiễm phụ khoa (PID) là tình trạng viêm nhiễm cơ quan sinh dục nữ (tử cung, vòi trứng, buồng trứng), thường do nhiễm khuẩn lây qua đường tình dục. Bệnh phổ biến ở phụ nữ trẻ, có thể gây vô sinh nếu không điều trị.

            **⚠️ Đặc điểm:**
            - Viêm nhiễm cơ quan sinh dục nữ
            - Thường do nhiễm khuẩn lây qua đường tình dục
            - Phổ biến ở phụ nữ trẻ
            - Có thể gây vô sinh

            ## Triệu chứng:

            **Triệu chứng điển hình:**
            - **Đau bụng dưới:** Đau âm ỉ, có thể dữ dội
            - **Sốt:** Sốt nhẹ đến vừa (37.5-39°C)
            - **Khí hư:** Khí hư nhiều, có mùi hôi, màu vàng/xanh
            - **Đau khi quan hệ:** Đau khi giao hợp
            - **Ra máu bất thường:** Ra máu giữa kỳ kinh, sau quan hệ
            - **Đau khi đi tiểu:** Có thể có

            **Triệu chứng khác:**
            - Buồn nôn, nôn
            - Mệt mỏi
            - Đau lưng

            **⚠️ Không có triệu chứng:**
            - Nhiều phụ nữ không có triệu chứng rõ ràng
            - Phát hiện khi khám phụ khoa

            **⚠️ Biến chứng:**
            - Vô sinh (do tắc vòi trứng)
            - Thai ngoài tử cung
            - Áp xe vùng chậu
            - Đau vùng chậu mạn tính

            ## Nguyên nhân:

            **1. Nhiễm khuẩn:**
            - **Chlamydia trachomatis:** Phổ biến nhất
            - **Neisseria gonorrhoeae:** Phổ biến
            - **Vi khuẩn khác:** Mycoplasma, Ureaplasma

            **2. Lây truyền:**
            - **Quan hệ tình dục:** Không an toàn
            - **Nhiều bạn tình:** Tăng nguy cơ
            - **Tiền sử:** Nhiễm khuẩn lây qua đường tình dục

            **3. Yếu tố nguy cơ:**
            - Quan hệ tình dục không an toàn
            - Nhiều bạn tình
            - Tuổi trẻ (< 25 tuổi)
            - Đặt dụng cụ tử cung (IUD)
            - Thụt rửa âm đạo

            ## Chẩn đoán:

            **Chẩn đoán lâm sàng:**
            - Triệu chứng điển hình
            - Khám phụ khoa: Đau khi khám, khí hư bất thường

            **Xét nghiệm:**
            - **Cấy dịch âm đạo:** Tìm vi khuẩn
            - **Xét nghiệm Chlamydia, Gonorrhea:** PCR
            - **Siêu âm:** Áp xe, dịch vùng chậu
            - **Nội soi ổ bụng:** Nếu cần (chuẩn vàng)

            ## Điều trị:

            **1. Kháng sinh (QUAN TRỌNG!):**
            - **Ceftriaxone 250mg IM + Doxycycline 100mg x 2 lần/ngày + Metronidazole 500mg x 2 lần/ngày:** 14 ngày
            - **Hoặc:** Ofloxacin 400mg x 2 lần/ngày + Metronidazole 500mg x 2 lần/ngày: 14 ngày
            - **Quan trọng:** Uống đủ liệu trình, điều trị bạn tình

            **2. Điều trị bạn tình:**
            - Điều trị đồng thời bạn tình
            - Tránh tái nhiễm

            **3. Nghỉ ngơi:**
            - Nghỉ ngơi tại giường
            - Tránh quan hệ tình dục cho đến khi khỏi

            **4. Phẫu thuật:**
            - Dẫn lưu áp xe nếu có
            - Cắt bỏ vòi trứng nếu tắc hoàn toàn

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Khi đang bệnh:**
            - Ăn đủ dinh dưỡng
            - Protein: Thịt, cá, trứng
            - Rau xanh, trái cây
            - Uống nhiều nước

            **2. Tránh:**
            - Đồ cay nóng (có thể làm đau tăng)
            - Rượu bia (khi dùng Metronidazole)

            **3. Thực đơn mẫu:**
            - **Sáng:** Cháo/cơm, thịt/cá, trái cây
            - **Trưa:** Cơm, thịt/cá, rau xanh, canh
            - **Chiều:** Cơm, thịt/cá, rau xanh, canh
            - **Bữa phụ:** Trái cây, sữa

            ## 🏃 TẬP THỂ DỤC:

            **1. Khi đang bệnh:**
            - Nghỉ ngơi tại giường
            - Tránh gắng sức

            **2. Sau khi khỏi:**
            - Tập thể dục từ từ
            - Tăng dần cường độ

            ## 💊 QUẢN LÝ THUỐC:

            **1. Kháng sinh:**
            - Uống đủ liệu trình (14 ngày)
            - Uống đúng giờ, đúng liều
            - **Quan trọng:** Không tự ý ngừng (gây tái phát, biến chứng)

            **2. Tác dụng phụ:**
            - **Metronidazole:** Buồn nôn, đắng miệng, không uống rượu
            - **Doxycycline:** Nhạy cảm ánh sáng, đau dạ dày
            - Báo bác sĩ nếu có tác dụng phụ nặng

            **3. Lưu ý:**
            - Điều trị bạn tình (quan trọng!)
            - Tránh quan hệ tình dục cho đến khi khỏi
            - Không thụt rửa âm đạo

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Triệu chứng nặng:**
            - Đau bụng dữ dội
            - Sốt cao (> 39°C)
            - Nôn nhiều

            **2. Biến chứng:**
            - Áp xe vùng chậu
            - Viêm phúc mạc
            - Sốc nhiễm khuẩn

            **3. Không đáp ứng điều trị:**
            - Triệu chứng không giảm sau 48-72 giờ
            - Tái phát

            **4. Mang thai:**
            - Nếu đang mang thai
            - Cần điều trị đặc biệt

            ## 💡 PHÒNG NGỪA:

            **1. Quan hệ tình dục an toàn:**
            - **Dùng bao cao su:** Quan trọng nhất!
            - **Một bạn tình:** Giảm nguy cơ
            - **Xét nghiệm định kỳ:** Nếu có nguy cơ

            **2. Vệ sinh:**
            - Vệ sinh vùng kín đúng cách
            - **Không thụt rửa âm đạo** (làm mất cân bằng vi khuẩn)
            - Mặc quần lót cotton, thoáng

            **3. Điều trị sớm:**
            - Điều trị nhiễm khuẩn lây qua đường tình dục sớm
            - Tránh biến chứng

            **4. Khám phụ khoa định kỳ:**
            - Khám phụ khoa định kỳ
            - Xét nghiệm Chlamydia, Gonorrhea nếu có nguy cơ

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Phòng ngừa:**
            - **Dùng bao cao su** (quan trọng nhất!)
            - Quan hệ tình dục an toàn
            - Vệ sinh vùng kín đúng cách

            **2. Khi bị viêm nhiễm phụ khoa:**
            - Điều trị sớm (quan trọng!)
            - Uống kháng sinh đủ liệu trình
            - Điều trị bạn tình
            - Tránh quan hệ tình dục cho đến khi khỏi

            **3. Sống tích cực:**
            - Viêm nhiễm phụ khoa có thể điều trị khỏi
            - Điều trị sớm → Tránh biến chứng (vô sinh)
            - Phòng ngừa tốt → Không mắc bệnh

            **4. Biến chứng:**
            - Có thể gây vô sinh nếu không điều trị
            - Cần điều trị sớm, đủ liệu trình
            - Khám phụ khoa định kỳ
            """,
            related_disease="pelvic_inflammatory_disease",
            related_drugs=["Ceftriaxone", "Doxycycline", "Metronidazole", "Ofloxacin"],
            printable=True
        ),

        PatientEducationTopic(
            id="uterine_fibroids_basics",
            title="Understanding Uterine Fibroids",
            title_vn="Hiểu về U xơ tử cung",
            category="Disease",
            content="""
            # Hiểu về U xơ tử cung

            ## U xơ tử cung là gì?

            U xơ tử cung là khối u lành tính phát triển từ cơ tử cung, rất phổ biến ở phụ nữ trong độ tuổi sinh sản. Hầu hết u xơ không gây triệu chứng, nhưng một số có thể gây ra máu nhiều, đau bụng.

            **⚠️ Đặc điểm:**
            - Khối u lành tính (không phải ung thư)
            - Phát triển từ cơ tử cung
            - Rất phổ biến (20-50% phụ nữ)
            - Hầu hết không gây triệu chứng

            **Phân loại:**
            - **Dưới thanh mạc:** Phát triển ra ngoài tử cung
            - **Trong cơ:** Phát triển trong cơ tử cung
            - **Dưới niêm mạc:** Phát triển vào trong tử cung (gây triệu chứng nhiều nhất)

            ## Triệu chứng:

            **Triệu chứng điển hình:**
            - **Ra máu nhiều:** Kinh nguyệt nhiều, kéo dài
            - **Đau bụng:** Đau bụng dưới, đau lưng
            - **Đau khi quan hệ:** Có thể có
            - **Đi tiểu nhiều:** Nếu u lớn chèn ép bàng quang
            - **Táo bón:** Nếu u lớn chèn ép trực tràng

            **Triệu chứng khác:**
            - Bụng to (nếu u lớn)
            - Thiếu máu (do ra máu nhiều)
            - Vô sinh, sảy thai (hiếm)

            **⚠️ Không có triệu chứng:**
            - Hầu hết u xơ không gây triệu chứng
            - Phát hiện khi khám phụ khoa, siêu âm

            ## Nguyên nhân:

            **1. Hormone:**
            - Estrogen, Progesterone kích thích phát triển
            - U xơ thường teo sau mãn kinh

            **2. Yếu tố nguy cơ:**
            - Tuổi: 30-50 tuổi
            - Tiền sử gia đình
            - Béo phì
            - Chủng tộc: Phụ nữ da đen có nguy cơ cao hơn
            - Chưa sinh con

            **3. Yếu tố bảo vệ:**
            - Sinh con
            - Dùng thuốc tránh thai
            - Mãn kinh

            ## Chẩn đoán:

            **Xét nghiệm:**
            - **Siêu âm:** Chuẩn vàng (thấy u xơ, kích thước, vị trí)
            - **MRI:** Nếu cần đánh giá chi tiết
            - **Nội soi tử cung:** Nếu u dưới niêm mạc
            - **Sinh thiết:** Nếu nghi ngờ ung thư (hiếm)

            ## Điều trị:

            **1. Theo dõi:**
            - Nếu không có triệu chứng, u nhỏ
            - Siêu âm định kỳ 6-12 tháng

            **2. Thuốc:**
            - **Thuốc tránh thai:** Giảm ra máu nhiều
            - **Progestin:** Giảm ra máu
            - **GnRH agonist:** Làm teo u (tạm thời)
            - **Tranexamic acid:** Giảm ra máu nhiều

            **3. Phẫu thuật:**
            - **Bóc u xơ:** Giữ lại tử cung (nếu muốn sinh con)
            - **Cắt tử cung:** Nếu u lớn, nhiều u, không muốn sinh con
            - **Nội soi tử cung:** Cắt u dưới niêm mạc

            **4. Can thiệp:**
            - **Thuyên tắc động mạch tử cung:** Làm teo u
            - **Sóng siêu âm tập trung:** Phá hủy u

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Bình thường:**
            - Ăn uống bình thường
            - Ăn đủ dinh dưỡng

            **2. Nếu thiếu máu:**
            - Bổ sung sắt: Thịt đỏ, rau xanh
            - Vitamin C: Giúp hấp thu sắt
            - Tránh trà, cà phê khi ăn (giảm hấp thu sắt)

            **3. Thực đơn mẫu:**
            - **Sáng:** Cháo/cơm, thịt/cá, trái cây
            - **Trưa:** Cơm, thịt đỏ, rau xanh, canh
            - **Chiều:** Cơm, thịt/cá, rau xanh, canh
            - **Bữa phụ:** Trái cây giàu vitamin C

            ## 🏃 TẬP THỂ DỤC:

            **1. Bình thường:**
            - Tập thể dục bình thường
            - 30 phút/ngày, 5 ngày/tuần

            **2. Lưu ý:**
            - Tránh gắng sức quá mức nếu đau bụng
            - Nghỉ ngơi nếu mệt mỏi

            ## 💊 QUẢN LÝ THUỐC:

            **1. Thuốc giảm ra máu:**
            - Thuốc tránh thai: Uống đều đặn
            - Tranexamic acid: Uống khi ra máu nhiều

            **2. Bổ sung sắt:**
            - Nếu thiếu máu
            - Uống sau ăn (giảm đau dạ dày)

            **3. Lưu ý:**
            - Uống đúng giờ, đúng liều
            - Báo bác sĩ nếu có tác dụng phụ

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Ra máu nhiều:**
            - Ra máu nhiều, không cầm được
            - Thiếu máu nặng (mệt mỏi, chóng mặt)

            **2. Đau bụng dữ dội:**
            - Đau bụng dữ dội, đột ngột
            - Có thể do xoắn u, hoại tử u

            **3. Triệu chứng nặng:**
            - Đi tiểu khó, bí tiểu
            - Táo bón nặng

            **4. Nghi ngờ ung thư:**
            - U phát triển nhanh
            - Sau mãn kinh

            ## 💡 PHÒNG NGỪA:

            **1. Không thể phòng ngừa hoàn toàn:**
            - U xơ có thể do di truyền, hormone
            - Không có cách phòng ngừa chắc chắn

            **2. Giảm nguy cơ:**
            - Duy trì cân nặng hợp lý
            - Ăn đủ dinh dưỡng
            - Tập thể dục đều đặn

            **3. Khám phụ khoa định kỳ:**
            - Khám phụ khoa định kỳ
            - Siêu âm nếu có triệu chứng

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Khi có u xơ:**
            - Hầu hết u xơ không cần điều trị
            - Theo dõi định kỳ nếu không có triệu chứng
            - Điều trị nếu có triệu chứng

            **2. Điều trị:**
            - Thuốc: Giảm triệu chứng
            - Phẫu thuật: Nếu u lớn, triệu chứng nặng
            - Có thể giữ lại tử cung (bóc u xơ)

            **3. Sống tích cực:**
            - U xơ là lành tính (không phải ung thư)
            - Hầu hết không ảnh hưởng cuộc sống
            - Điều trị đúng → Giảm triệu chứng

            **4. Phụ nữ trẻ:**
            - Có thể bóc u xơ, giữ lại tử cung
            - Vẫn có thể sinh con sau phẫu thuật
            - Cần theo dõi định kỳ
            """,
            related_disease="uterine_fibroids",
            related_drugs=["Oral Contraceptive", "Progestin", "GnRH Agonist", "Tranexamic Acid", "Iron"],
            printable=True
        ),

        PatientEducationTopic(
            id="polycystic_ovary_syndrome_basics",
            title="Understanding Polycystic Ovary Syndrome",
            title_vn="Hiểu về Hội chứng buồng trứng đa nang",
            category="Disease",
            content="""
            # Hiểu về Hội chứng buồng trứng đa nang (PCOS)

            ## PCOS là gì?

            Hội chứng buồng trứng đa nang (PCOS) là rối loạn nội tiết phổ biến ở phụ nữ, đặc trưng bởi rối loạn kinh nguyệt, tăng androgen, và buồng trứng đa nang. Bệnh ảnh hưởng đến khả năng sinh sản và sức khỏe lâu dài.

            **⚠️ Đặc điểm:**
            - Rối loạn nội tiết phổ biến (5-10% phụ nữ)
            - Rối loạn kinh nguyệt, tăng androgen
            - Buồng trứng đa nang
            - Ảnh hưởng khả năng sinh sản

            **Tiêu chuẩn chẩn đoán (Rotterdam):**
            - Rối loạn kinh nguyệt (ít kinh, vô kinh)
            - Tăng androgen (lâm sàng hoặc xét nghiệm)
            - Buồng trứng đa nang (siêu âm)
            - **Cần ≥ 2/3 tiêu chuẩn**

            ## Triệu chứng:

            **Triệu chứng điển hình:**
            - **Rối loạn kinh nguyệt:** Kinh thưa, vô kinh, không đều
            - **Rậm lông:** Lông mọc nhiều (mặt, ngực, bụng)
            - **Mụn trứng cá:** Mụn nhiều, dai dẳng
            - **Rụng tóc:** Rụng tóc kiểu nam (hói)
            - **Béo phì:** Tăng cân, khó giảm cân
            - **Vô sinh:** Khó có thai

            **Triệu chứng khác:**
            - Da sẫm màu (gáy, nách)
            - Tâm trạng thay đổi
            - Ngưng thở khi ngủ

            **⚠️ Biến chứng:**
            - Vô sinh
            - Đái tháo đường type 2
            - Tăng huyết áp
            - Rối loạn lipid máu
            - Ung thư nội mạc tử cung

            ## Nguyên nhân:

            **1. Rối loạn nội tiết:**
            - Tăng androgen (testosterone)
            - Kháng insulin
            - Rối loạn hormone sinh dục

            **2. Yếu tố nguy cơ:**
            - Tiền sử gia đình
            - Béo phì
            - Lối sống ít vận động
            - Chế độ ăn không lành mạnh

            **3. Cơ chế:**
            - Kháng insulin → Tăng insulin → Tăng androgen
            - Rối loạn hormone → Rối loạn rụng trứng

            ## Chẩn đoán:

            **Xét nghiệm:**
            - **Siêu âm:** Buồng trứng đa nang (≥ 12 nang, kích thước 2-9mm)
            - **Hormone:** Testosterone, LH, FSH, Prolactin
            - **Đường huyết:** Đường huyết đói, HbA1c
            - **Lipid máu:** Cholesterol, Triglyceride

            ## Điều trị:

            **1. Giảm cân (QUAN TRỌNG!):**
            - Giảm 5-10% cân nặng → Cải thiện triệu chứng
            - Chế độ ăn lành mạnh
            - Tập thể dục đều đặn

            **2. Thuốc:**
            - **Thuốc tránh thai:** Điều hòa kinh nguyệt, giảm androgen
            - **Metformin:** Giảm kháng insulin, giảm cân
            - **Spironolactone:** Giảm rậm lông
            - **Clomiphene:** Kích thích rụng trứng (nếu muốn có thai)

            **3. Điều trị vô sinh:**
            - Clomiphene
            - Letrozole
            - IVF nếu cần

            **4. Điều trị rậm lông:**
            - Thuốc tránh thai
            - Spironolactone
            - Điều trị tại chỗ (tẩy lông, laser)

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Chế độ ăn giảm cân:**
            - **Giảm calo:** Giảm 500-1000 calo/ngày
            - **Giảm carbohydrate:** Đặc biệt đường, tinh bột tinh chế
            - **Tăng protein:** Thịt nạc, cá, trứng
            - **Tăng chất xơ:** Rau xanh, trái cây
            - **Chất béo tốt:** Dầu ô liu, hạt, cá béo

            **2. Thực phẩm tốt:**
            - Rau xanh, trái cây
            - Ngũ cốc nguyên hạt
            - Protein nạc
            - Cá béo (omega-3)

            **3. Tránh:**
            - Đường, đồ ngọt
            - Tinh bột tinh chế (bánh mì trắng, cơm trắng)
            - Đồ chế biến sẵn
            - Nước ngọt

            **4. Thực đơn mẫu:**
            - **Sáng:** Trứng, rau, trái cây
            - **Trưa:** Cơm gạo lứt, thịt/cá, rau xanh, canh
            - **Chiều:** Cơm gạo lứt, thịt/cá, rau xanh, canh
            - **Bữa phụ:** Trái cây, hạt

            ## 🏃 TẬP THỂ DỤC:

            **1. Quan trọng!**
            - Tập thể dục đều đặn (giảm cân, giảm kháng insulin)
            - 30-60 phút/ngày, 5 ngày/tuần

            **2. Loại bài tập:**
            - **Cardio:** Đi bộ, chạy bộ, bơi lội, đạp xe
            - **Tập sức mạnh:** Tăng cơ, tăng chuyển hóa
            - **Kết hợp:** Cardio + Tập sức mạnh

            **3. Lưu ý:**
            - Bắt đầu từ từ
            - Tăng dần cường độ
            - Kiên trì (quan trọng!)

            ## 💊 QUẢN LÝ THUỐC:

            **1. Thuốc tránh thai:**
            - Uống đều đặn, đúng giờ
            - Điều hòa kinh nguyệt, giảm androgen

            **2. Metformin:**
            - Uống sau ăn (giảm đau dạ dày)
            - Bắt đầu liều thấp, tăng dần
            - Giảm kháng insulin, giảm cân

            **3. Spironolactone:**
            - Uống đều đặn
            - Giảm rậm lông

            **4. Lưu ý:**
            - Uống đúng giờ, đúng liều
            - Báo bác sĩ nếu có tác dụng phụ

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Rối loạn kinh nguyệt nặng:**
            - Vô kinh > 6 tháng
            - Ra máu nhiều, kéo dài

            **2. Vô sinh:**
            - Không có thai sau 1 năm (nếu < 35 tuổi)
            - Cần điều trị hỗ trợ sinh sản

            **3. Biến chứng:**
            - Đái tháo đường
            - Tăng huyết áp
            - Rối loạn lipid máu

            ## 💡 PHÒNG NGỪA:

            **1. Lối sống lành mạnh:**
            - Duy trì cân nặng hợp lý
            - Chế độ ăn lành mạnh
            - Tập thể dục đều đặn

            **2. Khám định kỳ:**
            - Khám phụ khoa định kỳ
            - Xét nghiệm đường huyết, lipid máu

            **3. Điều trị sớm:**
            - Điều trị sớm → Giảm biến chứng
            - Kiểm soát tốt → Cải thiện chất lượng cuộc sống

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Khi bị PCOS:**
            - **Giảm cân** (quan trọng nhất!)
            - Chế độ ăn lành mạnh
            - Tập thể dục đều đặn
            - Uống thuốc đều đặn

            **2. Giảm cân:**
            - Giảm 5-10% cân nặng → Cải thiện đáng kể
            - Kiên trì, không nản lòng
            - Kết hợp ăn uống + tập thể dục

            **3. Sống tích cực:**
            - PCOS có thể kiểm soát
            - Điều trị đúng → Cải thiện triệu chứng, khả năng sinh sản
            - Có thể có thai (với điều trị)

            **4. Lâu dài:**
            - Cần kiểm soát lâu dài
            - Theo dõi biến chứng (đái tháo đường, tăng huyết áp)
            - Khám định kỳ
            """,
            related_disease="polycystic_ovary_syndrome",
            related_drugs=["Oral Contraceptive", "Metformin", "Spironolactone", "Clomiphene", "Letrozole"],
            printable=True
        ),

        PatientEducationTopic(
            id="endometriosis_basics",
            title="Understanding Endometriosis",
            title_vn="Hiểu về Lạc nội mạc tử cung",
            category="Disease",
            content="""
            # Hiểu về Lạc nội mạc tử cung

            ## Lạc nội mạc tử cung là gì?

            Lạc nội mạc tử cung (Endometriosis) là tình trạng mô nội mạc tử cung (lớp lót bên trong tử cung) phát triển ở ngoài tử cung, gây đau, viêm, có thể dẫn đến vô sinh. Bệnh phổ biến ở phụ nữ trong độ tuổi sinh sản (10-15%).

            **⚠️ Đặc điểm:**
            - Mô nội mạc tử cung phát triển ngoài tử cung
            - Gây đau, viêm
            - Có thể dẫn đến vô sinh
            - Phổ biến ở phụ nữ 25-40 tuổi

            **Vị trí:**
            - **Buồng trứng:** Phổ biến nhất (tạo nang chocolate)
            - **Dây chằng tử cung-cùng:** Phổ biến
            - **Ổ bụng:** Phúc mạc, ruột, bàng quang
            - **Hiếm:** Phổi, não

            **Phân loại:**
            - **Độ 1 (Nhẹ):** Tổn thương nông, ít
            - **Độ 2-3 (Trung bình):** Tổn thương sâu hơn, nhiều hơn
            - **Độ 4 (Nặng):** Tổn thương sâu, nhiều, dính

            ## Triệu chứng:

            **Triệu chứng điển hình:**
            - **Đau bụng kinh:** Đau bụng kinh nặng, không giảm khi dùng thuốc giảm đau thông thường
            - **Đau khi quan hệ:** Đau khi giao hợp (dyspareunia)
            - **Đau vùng chậu mạn tính:** Đau vùng chậu không liên quan kinh nguyệt
            - **Đau khi đi tiểu, đại tiện:** Đau khi đi tiểu, đại tiện (nếu có tổn thương bàng quang, ruột)
            - **Ra máu bất thường:** Ra máu giữa kỳ kinh, sau quan hệ

            **Triệu chứng khác:**
            - Mệt mỏi
            - Buồn nôn, nôn (khi đau nặng)
            - Đầy bụng, chướng bụng
            - Tiêu chảy, táo bón (khi có tổn thương ruột)

            **⚠️ Vô sinh:**
            - 30-50% phụ nữ bị lạc nội mạc tử cung có vấn đề về khả năng sinh sản
            - Do dính, tắc vòi trứng, viêm

            **⚠️ Không có triệu chứng:**
            - Một số phụ nữ không có triệu chứng
            - Phát hiện tình cờ khi khám phụ khoa, siêu âm

            ## Nguyên nhân:

            **1. Nguyên nhân chưa rõ hoàn toàn:**
            - Có nhiều giả thuyết

            **2. Giả thuyết:**
            - **Kinh ngược dòng:** Máu kinh chảy ngược qua vòi trứng vào ổ bụng
            - **Di chuyển tế bào:** Tế bào nội mạc tử cung di chuyển qua máu, bạch huyết
            - **Chuyển hóa:** Tế bào phúc mạc chuyển hóa thành tế bào nội mạc tử cung
            - **Di truyền:** Có người thân bị lạc nội mạc tử cung

            **3. Yếu tố nguy cơ:**
            - **Tuổi:** 25-40 tuổi
            - **Chưa sinh con:** Chưa sinh con
            - **Kinh nguyệt sớm:** Bắt đầu kinh nguyệt sớm (< 11 tuổi)
            - **Kinh nguyệt dài:** Chu kỳ kinh nguyệt ngắn (< 27 ngày)
            - **Kinh nguyệt nhiều:** Ra máu nhiều, kéo dài
            - **Di truyền:** Có người thân bị lạc nội mạc tử cung

            **4. Yếu tố bảo vệ:**
            - **Mang thai:** Giảm nguy cơ
            - **Cho con bú:** Giảm nguy cơ
            - **Tập thể dục:** Giảm nguy cơ

            ## Chẩn đoán:

            **Chẩn đoán lâm sàng:**
            - Triệu chứng điển hình
            - Khám phụ khoa

            **Khám:**
            - **Khám phụ khoa:** Đau khi khám, khối u vùng chậu
            - **Siêu âm:** Phát hiện nang buồng trứng (nang chocolate)
            - **MRI:** Đánh giá tổn thương, mức độ

            **Chẩn đoán xác định:**
            - **Nội soi ổ bụng:** Quan sát trực tiếp tổn thương, sinh thiết
            - **Tiêu chuẩn vàng:** Nội soi ổ bụng + Sinh thiết

            **Xét nghiệm:**
            - **CA-125:** Tăng (không đặc hiệu, có thể tăng trong bệnh khác)
            - **Xét nghiệm máu:** Thường bình thường

            **⚠️ Phân biệt:**
            - Đau bụng kinh thông thường
            - U xơ tử cung
            - Viêm vùng chậu
            - Hội chứng ruột kích thích

            ## Điều trị:

            **1. Điều trị triệu chứng:**
            - **Thuốc giảm đau:**
              - **NSAID:** Ibuprofen, Naproxen (giảm đau, viêm)
              - **Paracetamol:** Nếu NSAID không đủ
            - **Thuốc tránh thai:**
              - **Thuốc tránh thai kết hợp:** Giảm đau, làm chậm tiến triển
              - **Dùng liên tục:** Không nghỉ (giảm đau bụng kinh)

            **2. Điều trị nội tiết:**
            - **Progestin:** Medroxyprogesterone, Dienogest (ức chế estrogen)
            - **Danazol:** Ức chế hormone (ít dùng, tác dụng phụ nhiều)
            - **GnRH agonist:** Leuprolide, Goserelin (tạo mãn kinh tạm thời)
            - **Mục tiêu:** Giảm estrogen → Teo mô lạc nội mạc tử cung

            **3. Phẫu thuật:**
            - **Nội soi ổ bụng:**
              - **Cắt bỏ tổn thương:** Cắt bỏ mô lạc nội mạc tử cung
              - **Đốt điện, laser:** Phá hủy tổn thương
            - **Cắt tử cung + Buồng trứng:**
              - Chỉ khi nặng, không đáp ứng điều trị khác
              - Tạo mãn kinh vĩnh viễn

            **4. Điều trị vô sinh:**
            - **Phẫu thuật:** Cắt bỏ tổn thương, giải phóng dính
            - **Thụ tinh nhân tạo (IUI):** Nếu nhẹ
            - **Thụ tinh trong ống nghiệm (IVF):** Nếu nặng

            **⚠️ Lưu ý:**
            - Điều trị tùy theo triệu chứng, mức độ, mong muốn có con
            - Không có cách chữa khỏi hoàn toàn
            - Có thể tái phát sau điều trị

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Thực phẩm chống viêm:**
            - **Cá béo:** Cá hồi, cá thu, cá mòi (Omega-3)
            - **Rau xanh:** Rau cải, rau bina, cải xoăn
            - **Trái cây:** Dâu, cam, bưởi (vitamin C)
            - **Quả hạch:** Hạnh nhân, óc chó
            - **Dầu oliu:** Dầu oliu nguyên chất

            **2. Thực phẩm giàu chất xơ:**
            - Rau xanh, trái cây
            - Ngũ cốc nguyên hạt
            - Đậu

            **3. Thực phẩm nên tránh:**
            - **Thịt đỏ:** Có thể tăng viêm
            - **Đồ chiên rán:** Tăng viêm
            - **Đường:** Tăng viêm
            - **Rượu bia:** Có thể làm nặng triệu chứng
            - **Caffeine:** Có thể làm nặng đau (một số người)

            **4. Thực đơn mẫu:**
            - **Sáng:** Cháo yến mạch + trái cây + sữa chua
            - **Trưa:** Cơm + canh rau + cá + rau xanh
            - **Chiều:** Cơm + canh rau + cá + rau xanh
            - **Bữa phụ:** Trái cây, quả hạch

            **5. Lưu ý:**
            - Ăn đủ dinh dưỡng
            - Tránh thực phẩm gây viêm
            - Ghi nhật ký thức ăn để tìm yếu tố kích thích

            ## 🏃 TẬP THỂ DỤC:

            **1. Tập thể dục đều đặn:**
            - **Đi bộ:** 30 phút/ngày, 5 ngày/tuần
            - **Yoga:** Kéo giãn, thư giãn (giảm đau)
            - **Bơi lội:** Tốt cho vùng chậu
            - **Giảm đau:** Tập thể dục đều đặn giảm đau

            **2. Khi đang đau:**
            - Nghỉ ngơi
            - Kéo giãn nhẹ
            - Chườm nóng (giảm đau)

            **3. Tránh:**
            - Tập quá sức khi đang đau
            - Tập khi đau bụng kinh nặng

            ## 💊 QUẢN LÝ THUỐC:

            **1. Thuốc giảm đau:**
            - **NSAID:** Ibuprofen 400-600mg, 3 lần/ngày (sau ăn)
            - **Naproxen:** 250-500mg, 2 lần/ngày
            - **Uống trước khi đau:** Uống 1-2 ngày trước khi có kinh

            **2. Thuốc tránh thai:**
            - **Thuốc tránh thai kết hợp:** Uống đều đặn
            - **Dùng liên tục:** Không nghỉ (nếu được bác sĩ chỉ định)
            - **Giảm đau:** Giảm đau bụng kinh, làm chậm tiến triển

            **3. Điều trị nội tiết:**
            - **Progestin:** Uống đều đặn, theo chỉ định
            - **GnRH agonist:** Tiêm, theo chỉ định
            - **Tác dụng phụ:** Bốc hỏa, khô âm đạo, loãng xương (GnRH)

            **4. Lưu ý:**
            - Uống đúng liều, đúng giờ
            - Báo bác sĩ nếu có tác dụng phụ
            - Không tự ý ngừng thuốc

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Đau nặng:**
            - Đau bụng dữ dội, không chịu được
            - Không đáp ứng thuốc giảm đau

            **2. Vô sinh:**
            - Không có thai sau 1 năm (nếu < 35 tuổi)
            - Cần điều trị hỗ trợ sinh sản

            **3. Triệu chứng mới:**
            - Ra máu nhiều, kéo dài
            - Đau khi đi tiểu, đại tiện nặng
            - Sốt, ớn lạnh (nhiễm trùng)

            **4. Tác dụng phụ:**
            - Tác dụng phụ nặng của thuốc
            - Bốc hỏa nặng, loãng xương (GnRH)

            ## 💡 PHÒNG NGỪA:

            **1. Không có cách phòng ngừa chắc chắn:**
            - Nguyên nhân chưa rõ hoàn toàn

            **2. Có thể giảm nguy cơ:**
            - **Tập thể dục:** Đều đặn, 30 phút/ngày
            - **Chế độ ăn:** Chế độ ăn chống viêm
            - **Tránh rượu bia:** Có thể giảm nguy cơ

            **3. Phát hiện sớm:**
            - Nhận biết triệu chứng
            - Khám phụ khoa định kỳ
            - Điều trị sớm → Giảm biến chứng

            **4. Điều trị:**
            - Điều trị sớm → Làm chậm tiến triển
            - Giảm nguy cơ vô sinh

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Khi bị lạc nội mạc tử cung:**
            - **Điều trị sớm** (quan trọng nhất!)
            - Dùng thuốc đều đặn
            - Tập thể dục đều đặn
            - Chế độ ăn chống viêm

            **2. Quản lý đau:**
            - Uống thuốc giảm đau trước khi đau
            - Chườm nóng
            - Thư giãn, yoga

            **3. Sống tích cực:**
            - Lạc nội mạc tử cung có thể kiểm soát
            - Điều trị đúng → Giảm triệu chứng
            - Có thể có thai (với điều trị)
            - Tham gia nhóm hỗ trợ

            **4. Vô sinh:**
            - Nếu muốn có con, cần điều trị sớm
            - Phẫu thuật có thể cải thiện khả năng sinh sản
            - Thụ tinh trong ống nghiệm (IVF) là lựa chọn tốt

            **5. Lâu dài:**
            - Cần điều trị lâu dài
            - Có thể tái phát
            - Theo dõi định kỳ
            """,
            related_disease="endometriosis",
            related_drugs=["Ibuprofen", "Naproxen", "Oral Contraceptive", "Medroxyprogesterone", "Leuprolide"],
            printable=True
        ),

        PatientEducationTopic(
            id="menstrual_disorders_basics",
            title="Understanding Menstrual Disorders",
            title_vn="Hiểu về Rối loạn kinh nguyệt",
            category="Disease",
            content="""
            # Hiểu về Rối loạn kinh nguyệt

            ## Rối loạn kinh nguyệt là gì?

            Rối loạn kinh nguyệt là những thay đổi bất thường về chu kỳ kinh nguyệt, lượng máu, thời gian ra máu. Rối loạn kinh nguyệt rất phổ biến, ảnh hưởng đến 30-50% phụ nữ ở một thời điểm nào đó.

            **⚠️ Đặc điểm:**
            - Thay đổi bất thường về chu kỳ, lượng máu, thời gian
            - Rất phổ biến (30-50% phụ nữ)
            - Có thể do nhiều nguyên nhân
            - Có thể điều trị

            **Phân loại:**
            - **Rối loạn chu kỳ:** Chu kỳ không đều, quá ngắn, quá dài
            - **Rối loạn lượng máu:** Ra máu nhiều, ít, không đều
            - **Rối loạn thời gian:** Ra máu kéo dài, ngắn
            - **Đau bụng kinh:** Đau bụng kinh nặng

            **Chu kỳ kinh nguyệt bình thường:**
            - **Chu kỳ:** 21-35 ngày (trung bình 28 ngày)
            - **Thời gian ra máu:** 3-7 ngày
            - **Lượng máu:** 30-80ml
            - **Đều đặn:** Chu kỳ đều đặn

            ## Triệu chứng:

            **1. Rối loạn chu kỳ:**
            - **Chu kỳ ngắn:** < 21 ngày (polymenorrhea)
            - **Chu kỳ dài:** > 35 ngày (oligomenorrhea)
            - **Chu kỳ không đều:** Chu kỳ thay đổi > 7 ngày
            - **Vô kinh:** Không có kinh > 6 tháng (amenorrhea)

            **2. Rối loạn lượng máu:**
            - **Ra máu nhiều (Menorrhagia):** Ra máu > 80ml, kéo dài > 7 ngày
            - **Ra máu ít (Hypomenorrhea):** Ra máu < 20ml
            - **Ra máu không đều:** Lượng máu thay đổi

            **3. Ra máu bất thường:**
            - **Ra máu giữa kỳ:** Ra máu giữa các kỳ kinh (metrorrhagia)
            - **Ra máu sau quan hệ:** Ra máu sau giao hợp
            - **Ra máu sau mãn kinh:** Ra máu sau mãn kinh (cần khám ngay!)

            **4. Đau bụng kinh (Dysmenorrhea):**
            - **Đau bụng kinh nguyên phát:** Đau bụng kinh không do bệnh (phổ biến ở tuổi dậy thì)
            - **Đau bụng kinh thứ phát:** Đau bụng kinh do bệnh (lạc nội mạc tử cung, u xơ tử cung)

            **Triệu chứng khác:**
            - Mệt mỏi (nếu ra máu nhiều)
            - Thiếu máu (nếu ra máu nhiều, kéo dài)
            - Đau đầu, chóng mặt
            - Thay đổi tâm trạng

            **⚠️ Dấu hiệu báo động (cần khám ngay!):**
            - Ra máu sau mãn kinh
            - Ra máu nhiều, kéo dài, không cầm
            - Đau bụng dữ dội
            - Sốt, ớn lạnh (nhiễm trùng)

            ## Nguyên nhân:

            **1. Rối loạn nội tiết:**
            - **Hội chứng buồng trứng đa nang (PCOS):** Chu kỳ không đều, vô kinh
            - **Suy giáp, cường giáp:** Rối loạn chu kỳ
            - **Rối loạn prolactin:** Tăng prolactin → Vô kinh
            - **Mãn kinh sớm:** Mãn kinh < 40 tuổi

            **2. Bệnh phụ khoa:**
            - **U xơ tử cung:** Ra máu nhiều, kéo dài
            - **Lạc nội mạc tử cung:** Đau bụng kinh nặng, ra máu bất thường
            - **Polyp tử cung:** Ra máu bất thường
            - **Ung thư tử cung, cổ tử cung:** Ra máu bất thường (hiếm)

            **3. Thuốc:**
            - **Thuốc tránh thai:** Có thể gây ra máu bất thường (ban đầu)
            - **Thuốc chống đông:** Ra máu nhiều
            - **Thuốc nội tiết:** Rối loạn chu kỳ

            **4. Yếu tố lối sống:**
            - **Stress:** Căng thẳng, lo âu
            - **Giảm cân nhanh:** Vô kinh
            - **Tập thể dục quá sức:** Vô kinh
            - **Béo phì:** Rối loạn chu kỳ

            **5. Yếu tố khác:**
            - **Tuổi:** Tuổi dậy thì, tiền mãn kinh (chu kỳ không đều)
            - **Mang thai:** Vô kinh
            - **Cho con bú:** Vô kinh (tạm thời)

            ## Chẩn đoán:

            **Chẩn đoán lâm sàng:**
            - Triệu chứng điển hình
            - Khám phụ khoa

            **Khám:**
            - **Khám phụ khoa:** Đánh giá tử cung, buồng trứng
            - **Siêu âm:** Phát hiện u xơ, polyp, nang buồng trứng
            - **Soi tử cung:** Quan sát bên trong tử cung

            **Xét nghiệm:**
            - **Xét nghiệm máu:**
              - Hormone (FSH, LH, Estrogen, Progesterone)
              - Chức năng tuyến giáp (TSH, T4)
              - Prolactin
              - Xét nghiệm máu (nếu thiếu máu)
            - **Sinh thiết:** Sinh thiết nội mạc tử cung (nếu cần)

            **⚠️ Phân biệt:**
            - Mang thai (vô kinh)
            - Bệnh khác (rối loạn đông máu)

            ## Điều trị:

            **1. Điều trị rối loạn chu kỳ:**
            - **Thuốc tránh thai:** Điều chỉnh chu kỳ
            - **Progestin:** Điều chỉnh chu kỳ
            - **Điều trị bệnh nền:** PCOS, suy giáp

            **2. Điều trị ra máu nhiều:**
            - **Thuốc tránh thai:** Giảm lượng máu
            - **Progestin:** Giảm lượng máu
            - **Tranexamic acid:** Giảm chảy máu
            - **NSAID:** Ibuprofen (giảm chảy máu, đau)
            - **Dụng cụ tử cung (IUD):** IUD chứa progestin (giảm chảy máu)

            **3. Điều trị đau bụng kinh:**
            - **NSAID:** Ibuprofen, Naproxen (giảm đau, viêm)
            - **Thuốc tránh thai:** Giảm đau
            - **Chườm nóng:** Giảm đau
            - **Tập thể dục:** Giảm đau

            **4. Phẫu thuật:**
            - **Cắt polyp:** Cắt polyp tử cung
            - **Cắt u xơ:** Cắt u xơ tử cung
            - **Cắt nội mạc tử cung:** Cắt nội mạc tử cung (nếu ra máu nhiều, không muốn có con)
            - **Cắt tử cung:** Chỉ khi cần thiết

            **5. Điều trị vô kinh:**
            - **Điều trị nguyên nhân:** PCOS, suy giáp
            - **Thuốc nội tiết:** Estrogen, Progestin
            - **Giảm cân:** Nếu do giảm cân nhanh

            **⚠️ Lưu ý:**
            - Điều trị tùy theo nguyên nhân, triệu chứng
            - Điều trị bệnh nền (nếu có)

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Thực phẩm nên ăn:**
            - **Thực phẩm giàu sắt:** Thịt đỏ, gan, rau xanh (nếu thiếu máu)
            - **Thực phẩm giàu vitamin C:** Trái cây, rau xanh (tăng hấp thu sắt)
            - **Rau xanh, trái cây:** Vitamin, khoáng chất
            - **Ngũ cốc nguyên hạt:** Chất xơ, vitamin B
            - **Cá béo:** Omega-3 (giảm viêm)

            **2. Thực phẩm nên tránh:**
            - **Đường:** Có thể làm nặng triệu chứng
            - **Caffeine:** Có thể làm nặng đau (một số người)
            - **Rượu bia:** Có thể làm nặng triệu chứng
            - **Thực phẩm chế biến:** Đồ hộp, thức ăn nhanh

            **3. Thực đơn mẫu:**
            - **Sáng:** Cháo yến mạch + trái cây + sữa chua
            - **Trưa:** Cơm + canh rau + thịt/cá + rau xanh
            - **Chiều:** Cơm + canh rau + thịt/cá + rau xanh
            - **Bữa phụ:** Trái cây, hạt

            **4. Lưu ý:**
            - Ăn đủ dinh dưỡng
            - Bổ sung sắt nếu thiếu máu
            - Duy trì cân nặng hợp lý

            ## 🏃 TẬP THỂ DỤC:

            **1. Tập thể dục đều đặn:**
            - **Đi bộ:** 30 phút/ngày, 5 ngày/tuần
            - **Yoga:** Kéo giãn, thư giãn (giảm đau bụng kinh)
            - **Bơi lội:** Tốt cho sức khỏe
            - **Giảm đau:** Tập thể dục đều đặn giảm đau bụng kinh

            **2. Khi đang đau bụng kinh:**
            - Nghỉ ngơi
            - Kéo giãn nhẹ
            - Chườm nóng (giảm đau)

            **3. Tránh:**
            - Tập quá sức (có thể gây vô kinh)
            - Tập khi đau bụng kinh nặng

            ## 💊 QUẢN LÝ THUỐC:

            **1. Thuốc giảm đau:**
            - **NSAID:** Ibuprofen 400-600mg, 3 lần/ngày (sau ăn)
            - **Naproxen:** 250-500mg, 2 lần/ngày
            - **Uống trước khi đau:** Uống 1-2 ngày trước khi có kinh

            **2. Thuốc tránh thai:**
            - **Thuốc tránh thai kết hợp:** Điều chỉnh chu kỳ, giảm lượng máu, đau
            - **Uống đều đặn:** Theo chỉ định bác sĩ

            **3. Progestin:**
            - **Medroxyprogesterone:** Điều chỉnh chu kỳ, giảm lượng máu
            - **Uống đều đặn:** Theo chỉ định bác sĩ

            **4. Tranexamic acid:**
            - **Giảm chảy máu:** Uống khi ra máu nhiều
            - **Theo chỉ định bác sĩ**

            **5. Lưu ý:**
            - Uống đúng liều, đúng giờ
            - Báo bác sĩ nếu có tác dụng phụ
            - Không tự ý ngừng thuốc

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Ra máu sau mãn kinh:**
            - **Cần khám ngay!** (Có thể ung thư)

            **2. Ra máu nhiều, không cầm:**
            - Ra máu nhiều, kéo dài, không cầm
            - Thiếu máu (mệt mỏi, xanh xao, khó thở)
            - **Cấp cứu ngay!**

            **3. Đau bụng dữ dội:**
            - Đau bụng dữ dội, không chịu được
            - Không đáp ứng thuốc giảm đau

            **4. Sốt, ớn lạnh:**
            - Sốt, ớn lạnh (nhiễm trùng)
            - **Cấp cứu ngay!**

            **5. Vô kinh:**
            - Vô kinh > 6 tháng (nếu không mang thai, cho con bú)
            - Cần khám để tìm nguyên nhân

            ## 💡 PHÒNG NGỪA:

            **1. Lối sống lành mạnh:**
            - **Duy trì cân nặng hợp lý:** Tránh béo phì, giảm cân quá nhanh
            - **Tập thể dục đều đặn:** 30 phút/ngày (không quá sức)
            - **Quản lý stress:** Thư giãn, yoga, thiền
            - **Ngủ đủ giấc:** 7-9 giờ/đêm

            **2. Chế độ ăn:**
            - Ăn đủ dinh dưỡng
            - Bổ sung sắt nếu thiếu máu
            - Tránh đường, caffeine (nếu có ảnh hưởng)

            **3. Khám định kỳ:**
            - Khám phụ khoa định kỳ (mỗi 1-2 năm)
            - Phát hiện sớm bệnh

            **4. Theo dõi:**
            - Ghi nhật ký kinh nguyệt
            - Theo dõi chu kỳ, lượng máu, triệu chứng
            - Báo bác sĩ nếu có thay đổi

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Phòng ngừa:**
            - **Lối sống lành mạnh** (quan trọng nhất!)
            - **Duy trì cân nặng hợp lý**
            - **Tập thể dục đều đặn**
            - **Quản lý stress**

            **2. Khi bị rối loạn kinh nguyệt:**
            - Khám bác sĩ để tìm nguyên nhân
            - Điều trị theo chỉ định
            - Theo dõi triệu chứng

            **3. Sống tích cực:**
            - Rối loạn kinh nguyệt rất phổ biến
            - Có thể điều trị
            - Điều trị đúng → Cải thiện triệu chứng

            **4. Ghi nhật ký:**
            - Ghi nhật ký kinh nguyệt
            - Theo dõi chu kỳ, lượng máu, triệu chứng
            - Giúp bác sĩ chẩn đoán

            **5. Đừng ngại:**
            - Rối loạn kinh nguyệt là bình thường
            - Không phải lỗi của bạn
            - Cần điều trị, không cần xấu hổ
            """,
            related_disease="menstrual_disorders",
            related_drugs=["Ibuprofen", "Naproxen", "Oral Contraceptive", "Medroxyprogesterone", "Tranexamic acid"],
            printable=True
        ),

        PatientEducationTopic(
            id="ovarian_cyst_basics",
            title="Understanding Ovarian Cyst",
            title_vn="Hiểu về U nang buồng trứng",
            category="Disease",
            content="""
            # Hiểu về U nang buồng trứng

            ## U nang buồng trứng là gì?

            U nang buồng trứng (Ovarian Cyst) là túi chứa dịch trong buồng trứng, rất phổ biến ở phụ nữ trong độ tuổi sinh sản. Hầu hết u nang là lành tính và tự khỏi, nhưng một số có thể gây biến chứng.

            **⚠️ Đặc điểm:**
            - Túi chứa dịch trong buồng trứng
            - Rất phổ biến ở phụ nữ
            - Hầu hết lành tính, tự khỏi
            - Một số có thể gây biến chứng

            **Phân loại:**
            - **U nang chức năng:** U nang do rụng trứng (phổ biến nhất, lành tính)
            - **U nang bệnh lý:** U nang do bệnh (lạc nội mạc tử cung, u nang bì, u nang ác tính)

            **U nang chức năng:**
            - **U nang nang noãn:** Nang noãn không vỡ
            - **U nang hoàng thể:** Hoàng thể không teo
            - Tự khỏi trong 1-3 tháng

            ## Triệu chứng:

            **1. Không có triệu chứng (phổ biến):**
            - Phát hiện tình cờ khi siêu âm
            - Tự khỏi

            **2. Triệu chứng nhẹ:**
            - **Đau bụng dưới:** Đau bụng dưới, một bên
            - **Đầy bụng:** Đầy bụng, chướng bụng
            - **Rối loạn kinh nguyệt:** Rối loạn kinh nguyệt

            **3. Triệu chứng nặng (biến chứng):**
            - **Vỡ nang:** Đau bụng dữ dội, đột ngột
            - **Xoắn nang:** Đau bụng dữ dội, nôn, sốt
            - **Chảy máu trong nang:** Đau bụng, thiếu máu

            **⚠️ Dấu hiệu báo động:**
            - U nang lớn (> 5cm)
            - U nang tăng kích thước
            - U nang có vách, nhú
            - U nang ở phụ nữ sau mãn kinh

            ## Nguyên nhân:

            **1. U nang chức năng:**
            - **Rụng trứng:** Nang noãn không vỡ, hoàng thể không teo
            - **Hormone:** Rối loạn hormone
            - Tự khỏi trong 1-3 tháng

            **2. U nang bệnh lý:**
            - **Lạc nội mạc tử cung:** Nang chocolate
            - **U nang bì (Dermoid):** Chứa tóc, răng, xương
            - **U nang tuyến (Cystadenoma):** Lành tính hoặc ác tính
            - **Ung thư buồng trứng:** Hiếm

            **3. Yếu tố nguy cơ:**
            - Phụ nữ trong độ tuổi sinh sản
            - Rối loạn hormone
            - Lạc nội mạc tử cung
            - Tiền sử u nang buồng trứng

            ## Chẩn đoán:

            **Chẩn đoán lâm sàng:**
            - Triệu chứng điển hình
            - Khám phụ khoa

            **Xét nghiệm:**
            - **Siêu âm:** Phát hiện u nang, kích thước, đặc điểm (quan trọng nhất!)
            - **Xét nghiệm máu:**
              - CA-125: Tăng (nếu nghi ngờ ung thư)
              - Hormone: Đánh giá rối loạn hormone

            **Hình ảnh:**
            - **CT/MRI:** Đánh giá chi tiết (nếu cần)

            **⚠️ Phân biệt:**
            - Thai ngoài tử cung
            - Viêm vùng chậu
            - U xơ tử cung

            ## Điều trị:

            **1. U nang chức năng (nhỏ, < 5cm):**
            - **Theo dõi:** Theo dõi, tự khỏi trong 1-3 tháng
            - **Siêu âm lại:** Sau 6-12 tuần
            - **Không cần điều trị:** Nếu tự khỏi

            **2. U nang lớn (> 5cm) hoặc không tự khỏi:**
            - **Phẫu thuật nội soi:** Cắt bỏ u nang (bảo tồn buồng trứng)
            - **Phẫu thuật mở:** Nếu u nang lớn, nghi ngờ ác tính

            **3. Biến chứng:**
            - **Vỡ nang:** Theo dõi, phẫu thuật nếu chảy máu nhiều
            - **Xoắn nang:** Phẫu thuật ngay (cấp cứu!)

            **4. U nang ác tính:**
            - Phẫu thuật cắt buồng trứng, tử cung
            - Hóa trị, xạ trị

            **⚠️ Lưu ý:**
            - Hầu hết u nang lành tính, tự khỏi
            - Chỉ phẫu thuật khi cần thiết
            - Bảo tồn buồng trứng (nếu có thể)

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Chế độ ăn lành mạnh:**
            - Đủ dinh dưỡng
            - Rau xanh, trái cây
            - Protein nạc
            - Uống nhiều nước

            **2. Thực phẩm nên ăn:**
            - Protein nạc (thịt, cá, đậu)
            - Rau xanh, trái cây
            - Ngũ cốc nguyên hạt
            - Cá béo (omega-3)

            **3. Thực phẩm nên tránh:**
            - Đồ chiên rán
            - Thức ăn nhiều chất béo
            - Rượu bia

            **4. Lưu ý:**
            - Ăn đủ dinh dưỡng
            - Duy trì cân nặng hợp lý

            ## 🏃 TẬP THỂ DỤC:

            **1. Tập thể dục:**
            - Bình thường, đều đặn
            - 30 phút/ngày, 5 ngày/tuần

            **2. Lưu ý:**
            - Tránh gắng sức quá mức
            - Nghỉ ngơi nếu đau bụng

            **3. Sau phẫu thuật:**
            - Nghỉ ngơi 1-2 tuần
            - Tập thể dục từ từ
            - Tăng dần cường độ

            ## 💊 QUẢN LÝ THUỐC:

            **1. Thuốc giảm đau:**
            - **Paracetamol:** Nếu đau
            - **NSAID:** Ibuprofen (nếu không chống chỉ định)

            **2. Thuốc tránh thai:**
            - Có thể giúp giảm u nang chức năng
            - Theo chỉ định bác sĩ

            **3. Lưu ý:**
            - Uống đúng liều, đúng giờ
            - Báo bác sĩ nếu đau không giảm

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Biến chứng:**
            - **Xoắn nang:** Đau bụng dữ dội, nôn, sốt
            - **Vỡ nang:** Đau bụng dữ dội, đột ngột
            - **Cấp cứu ngay!**

            **2. Triệu chứng nặng:**
            - Đau bụng dữ dội
            - Sốt, ớn lạnh
            - Tụt huyết áp

            **3. U nang lớn hoặc tăng kích thước:**
            - U nang > 5cm
            - U nang tăng kích thước
            - Cần đánh giá thêm

            ## 💡 PHÒNG NGỪA:

            **1. Không có cách phòng ngừa chắc chắn:**
            - U nang chức năng là bình thường

            **2. Khám định kỳ:**
            - Khám phụ khoa định kỳ (mỗi 1-2 năm)
            - Siêu âm nếu có triệu chứng

            **3. Phát hiện sớm:**
            - Nhận biết triệu chứng
            - Khám ngay khi có triệu chứng

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Khi có u nang buồng trứng:**
            - Hầu hết lành tính, tự khỏi
            - Theo dõi định kỳ
            - Không cần lo lắng quá

            **2. Sống tích cực:**
            - U nang buồng trứng rất phổ biến
            - Hầu hết tự khỏi
            - Chỉ phẫu thuật khi cần thiết

            **3. Theo dõi:**
            - Siêu âm lại sau 6-12 tuần
            - Báo bác sĩ nếu có triệu chứng mới
            """,
            related_disease="ovarian_cyst",
            related_drugs=["Paracetamol", "Ibuprofen", "Oral Contraceptive"],
            printable=True
        ),

        PatientEducationTopic(
            id="pelvic_inflammatory_disease_detailed_basics",
            title="Understanding Pelvic Inflammatory Disease (Detailed)",
            title_vn="Hiểu về Viêm vùng chậu",
            category="Disease",
            content="""
            # Hiểu về Viêm vùng chậu

            ## Viêm vùng chậu là gì?

            Viêm vùng chậu (Pelvic Inflammatory Disease - PID) là tình trạng viêm nhiễm cơ quan sinh dục nữ (tử cung, vòi trứng, buồng trứng), thường do nhiễm khuẩn lây qua đường tình dục. Bệnh phổ biến ở phụ nữ trẻ, có thể gây vô sinh nếu không điều trị.

            **⚠️ Đặc điểm:**
            - Viêm nhiễm cơ quan sinh dục nữ
            - Thường do nhiễm khuẩn lây qua đường tình dục
            - Phổ biến ở phụ nữ trẻ
            - Có thể gây vô sinh

            **Phân loại:**
            - **Viêm vùng chậu cấp:** Viêm đột ngột
            - **Viêm vùng chậu mạn:** Viêm tái phát, mạn tính

            ## Triệu chứng:

            **Triệu chứng điển hình:**
            - **Đau bụng dưới:** Đau bụng dưới, âm ỉ, có thể dữ dội
            - **Sốt:** Sốt nhẹ đến vừa (37.5-39°C)
            - **Khí hư:** Khí hư nhiều, có mùi hôi, màu vàng/xanh
            - **Đau khi quan hệ:** Đau khi giao hợp
            - **Ra máu bất thường:** Ra máu giữa kỳ kinh, sau quan hệ
            - **Đau khi đi tiểu:** Có thể có

            **Triệu chứng khác:**
            - Buồn nôn, nôn
            - Mệt mỏi
            - Đau lưng

            **⚠️ Không có triệu chứng:**
            - Nhiều phụ nữ không có triệu chứng rõ ràng
            - Phát hiện khi khám phụ khoa

            **⚠️ Biến chứng:**
            - **Vô sinh:** Do tắc vòi trứng (10-20%)
            - **Thai ngoài tử cung:** Tăng nguy cơ (6-10 lần)
            - **Áp xe vùng chậu:** Áp xe vùng chậu
            - **Đau vùng chậu mạn tính:** Đau vùng chậu mạn tính

            ## Nguyên nhân:

            **1. Nhiễm khuẩn lây qua đường tình dục (STI):**
            - **Chlamydia trachomatis:** Phổ biến nhất (40%)
            - **Neisseria gonorrhoeae:** Phổ biến (30%)
            - **Mycoplasma genitalium:** Phổ biến
            - **Nhiễm khuẩn hỗn hợp:** Nhiều loại vi khuẩn

            **2. Nhiễm khuẩn không do STI:**
            - **Vi khuẩn âm đạo:** Gardnerella, Bacteroides
            - **Sau thủ thuật:** Sau nạo phá thai, đặt dụng cụ tử cung

            **3. Yếu tố nguy cơ:**
            - **Quan hệ tình dục không an toàn:** Nhiều bạn tình, không dùng bao cao su
            - **Tuổi:** < 25 tuổi
            - **Tiền sử:** Viêm vùng chậu trước đó
            - **Đặt dụng cụ tử cung (IUD):** Tăng nguy cơ nhẹ (trong 3 tuần đầu)
            - **Nạo phá thai:** Sau nạo phá thai

            ## Chẩn đoán:

            **Chẩn đoán lâm sàng:**
            - Triệu chứng điển hình
            - Khám phụ khoa

            **Khám:**
            - **Khám phụ khoa:** Đau khi khám, khối u vùng chậu
            - **Siêu âm:** Phát hiện áp xe, dịch vùng chậu

            **Xét nghiệm:**
            - **Cấy khí hư:** Xác định vi khuẩn
            - **Xét nghiệm STI:** Chlamydia, Gonorrhea (PCR)
            - **Xét nghiệm máu:** Bạch cầu tăng, CRP tăng

            **⚠️ Phân biệt:**
            - Thai ngoài tử cung
            - Viêm ruột thừa
            - U nang buồng trứng xoắn

            ## Điều trị:

            **1. Kháng sinh:**
            - **Ceftriaxone + Doxycycline + Metronidazole:** Phổ biến
            - **Đường tĩnh mạch:** Nếu nặng, nhập viện
            - **Đường uống:** Nếu nhẹ, điều trị ngoại trú
            - **Thời gian:** 14 ngày

            **2. Điều trị bạn tình:**
            - Điều trị bạn tình (quan trọng!)
            - Tránh tái nhiễm

            **3. Phẫu thuật:**
            - **Chỉ định:**
              - Áp xe vùng chậu không đáp ứng kháng sinh
              - Vỡ áp xe
            - **Phương pháp:** Dẫn lưu áp xe, cắt vòi trứng (nếu cần)

            **⚠️ Lưu ý:**
            - Điều trị sớm (quan trọng!)
            - Điều trị đủ thời gian (14 ngày)
            - Điều trị bạn tình

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Khi đang điều trị:**
            - **Đủ dinh dưỡng:** Đủ calo, protein, vitamin
            - **Dễ tiêu:** Thức ăn mềm, dễ tiêu
            - **Uống nhiều nước:** Uống nhiều nước

            **2. Thực phẩm nên ăn:**
            - Protein nạc (thịt, cá, đậu)
            - Rau xanh, trái cây
            - Cháo, súp
            - Uống nhiều nước

            **3. Thực phẩm nên tránh:**
            - Đồ cay nóng
            - Rượu bia
            - Thức ăn khó tiêu

            ## 🏃 TẬP THỂ DỤC:

            **1. Khi đang điều trị:**
            - Nghỉ ngơi
            - Tránh gắng sức
            - Tránh quan hệ tình dục (cho đến khi khỏi)

            **2. Sau khi khỏi:**
            - Tập thể dục từ từ
            - Tăng dần cường độ

            ## 💊 QUẢN LÝ THUỐC:

            **1. Kháng sinh:**
            - **Ceftriaxone:** Tiêm bắp, 1 lần
            - **Doxycycline:** 100mg, 2 lần/ngày, 14 ngày
            - **Metronidazole:** 500mg, 2 lần/ngày, 14 ngày
            - **Uống đều đặn:** Theo chỉ định bác sĩ
            - **Đủ thời gian:** 14 ngày (quan trọng!)

            **2. Lưu ý:**
            - Uống đúng liều, đúng giờ
            - Không tự ý ngừng thuốc
            - Báo bác sĩ nếu có tác dụng phụ

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Triệu chứng nặng:**
            - Đau bụng dữ dội
            - Sốt cao (> 39°C)
            - Nôn, không ăn được
            - **Cấp cứu ngay!**

            **2. Biến chứng:**
            - Áp xe vùng chậu
            - Vỡ áp xe
            - **Cấp cứu ngay!**

            **3. Không đáp ứng điều trị:**
            - Điều trị > 3 ngày không cải thiện
            - Triệu chứng tăng

            ## 💡 PHÒNG NGỪA:

            **1. Quan hệ tình dục an toàn:**
            - **Dùng bao cao su:** Dùng bao cao su (quan trọng nhất!)
            - **Một bạn tình:** Một bạn tình
            - **Xét nghiệm STI:** Xét nghiệm STI định kỳ

            **2. Điều trị STI sớm:**
            - Điều trị Chlamydia, Gonorrhea sớm
            - Giảm nguy cơ viêm vùng chậu

            **3. Tránh:**
            - Quan hệ tình dục không an toàn
            - Nhiều bạn tình

            **4. Sau thủ thuật:**
            - Vệ sinh sau nạo phá thai
            - Theo dõi sau đặt IUD

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Phòng ngừa:**
            - **Quan hệ tình dục an toàn** (quan trọng nhất!)
            - Dùng bao cao su
            - Xét nghiệm STI định kỳ

            **2. Khi bị viêm vùng chậu:**
            - Điều trị sớm, đủ thời gian
            - Điều trị bạn tình
            - Tránh quan hệ tình dục cho đến khi khỏi

            **3. Sống tích cực:**
            - Viêm vùng chậu có thể điều trị khỏi
            - Điều trị sớm → Giảm biến chứng
            - Phòng ngừa tốt → Không tái phát

            **4. Lâu dài:**
            - Tăng nguy cơ vô sinh (nếu tái phát nhiều lần)
            - Cần điều trị sớm, đúng cách
            - Theo dõi định kỳ
            """,
            related_disease="pelvic_inflammatory_disease",
            related_drugs=["Ceftriaxone", "Doxycycline", "Metronidazole"],
            printable=True
        ),

]
