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

]
