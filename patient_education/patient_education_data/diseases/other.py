"""
Patient Education Topics - Other
"""
from patient_education.models import PatientEducationTopic


OTHER_TOPICS = [
        PatientEducationTopic(
            id="back_pain_basics",
            title="Understanding Back Pain",
            title_vn="Hiểu về Đau lưng",
            category="Disease",
            content="""
            # Hiểu về Đau lưng

            ## Đau lưng là gì?

            Đau lưng là triệu chứng rất phổ biến, có thể do nhiều nguyên nhân khác nhau, từ căng cơ đơn giản đến các bệnh lý nghiêm trọng.

            **⚠️ Đặc điểm:**
            - Rất phổ biến (80% người từng bị đau lưng)
            - Hầu hết tự khỏi sau vài ngày đến vài tuần
            - Một số trường hợp cần điều trị
            - Phòng ngừa quan trọng

            **Phân loại:**
            - **Đau lưng cấp:** < 6 tuần
            - **Đau lưng bán cấp:** 6-12 tuần
            - **Đau lưng mạn:** > 12 tuần

            **Vị trí:**
            - Đau lưng dưới (thắt lưng) - Phổ biến nhất
            - Đau lưng giữa
            - Đau lưng trên (cổ)

            ## Triệu chứng:

            **Triệu chứng điển hình:**
            - **Đau lưng:** Đau âm ỉ hoặc đau nhói
            - **Đau tăng:** Khi vận động, cúi, xoay
            - **Đau giảm:** Khi nghỉ ngơi
            - **Cứng lưng:** Khó cử động
            - **Co cứng cơ:** Cơ lưng co cứng

            **Triệu chứng khác:**
            - Đau lan xuống chân (nếu có chèn ép thần kinh)
            - Tê bì chân (nếu có chèn ép thần kinh)
            - Yếu chân (nếu có chèn ép thần kinh)

            **⚠️ Dấu hiệu cảnh báo (Cần đến bệnh viện ngay!):**
            - Đau sau chấn thương (ngã, tai nạn)
            - Đau kèm sốt
            - Đau kèm tiểu không tự chủ, tê vùng sinh dục
            - Đau kèm sụt cân không rõ nguyên nhân
            - Đau kèm yếu chân, tê bì

            ## Nguyên nhân:

            **1. Căng cơ, dây chằng:**
            - Nâng vật nặng sai tư thế
            - Vận động đột ngột
            - Ngồi lâu, sai tư thế
            - Nguyên nhân phổ biến nhất (80%)

            **2. Thoái hóa cột sống:**
            - Tuổi cao
            - Thoái hóa đĩa đệm
            - Thoái hóa khớp cột sống

            **3. Thoát vị đĩa đệm:**
            - Đĩa đệm lồi ra, chèn ép thần kinh
            - Gây đau, tê bì chân

            **4. Yếu tố khác:**
            - **Béo phì:** Tăng áp lực lên cột sống
            - **Ít vận động:** Yếu cơ lưng
            - **Hút thuốc lá:** Làm chậm lành
            - **Stress:** Tăng căng cơ
            - **Mang thai:** Tăng áp lực lên cột sống

            ## Chẩn đoán:

            **1. Khám lâm sàng:**
            - Đánh giá triệu chứng
            - Khám cột sống, cơ
            - Test thần kinh (nếu có tê bì)

            **2. X-quang:**
            - Xem cấu trúc xương
            - Thường không cần (trừ khi có dấu hiệu cảnh báo)

            **3. CT/MRI:**
            - Chỉ khi có dấu hiệu cảnh báo
            - Hoặc đau kéo dài, không đáp ứng điều trị

            ## Điều trị:

            **1. Điều trị tại nhà (Đau lưng cấp nhẹ):**
            - **Nghỉ ngơi:** 1-2 ngày (không quá lâu!)
            - **Chườm lạnh:** 48 giờ đầu (giảm sưng, đau)
            - **Chườm ấm:** Sau 48 giờ (giảm căng cơ)
            - **Thuốc giảm đau:** Paracetamol, Ibuprofen
            - **Vận động nhẹ:** Đi bộ nhẹ (sau 1-2 ngày)

            **2. Điều trị tại viện (Nếu nặng):**
            - Vật lý trị liệu
            - Thuốc giảm đau mạnh hơn
            - Tiêm corticosteroid (nếu cần)
            - Phẫu thuật (hiếm, chỉ khi cần)

            **3. ⚠️ QUAN TRỌNG:**
            - **Không nghỉ quá lâu:** > 2-3 ngày → Yếu cơ, cứng khớp
            - **Vận động sớm:** Đi bộ nhẹ sau 1-2 ngày
            - **Tư thế đúng:** Khi ngồi, đứng, nâng vật

            ## 🍽️ CHẾ ĐỘ ĂN CHO NGƯỜI ĐAU LƯNG:

            **1. Nguyên tắc:**
            - **Chống viêm:** Thực phẩm chống viêm
            - **Giảm cân:** Nếu thừa cân (giảm áp lực lên cột sống)
            - **Đủ canxi, vitamin D:** Tốt cho xương

            **2. Thực phẩm NÊN ĂN:**
            - **Cá béo:** Cá hồi, cá thu (omega-3, chống viêm, 2-3 lần/tuần)
            - **Rau xanh:** Nhiều (rau cải, rau muống, bông cải)
              - Chất chống oxy hóa, chống viêm
            - **Trái cây:** Tất cả (cam, bưởi, táo)
              - Vitamin C, chất chống oxy hóa
            - **Sữa, sữa chua:** Canxi, vitamin D (tốt cho xương)
            - **Các loại hạt:** Hạnh nhân, óc chó (nếu có)
            - **Ngũ cốc nguyên hạt:** Gạo lứt, yến mạch

            **3. Thực phẩm CẦN TRÁNH:**
            - **Thực phẩm chế biến sẵn:** Đồ hộp, thức ăn nhanh
            - **Đồ chiên, nhiều dầu mỡ:** Chất béo bão hòa (gây viêm)
            - **Đường nhiều:** Bánh kẹo, nước ngọt (gây viêm)
            - **Rượu bia:** Có thể làm nặng đau

            **4. Giảm cân (Nếu thừa cân):**
            - Thừa cân → Tăng áp lực lên cột sống → Đau lưng
            - Giảm cân → Giảm đau lưng
            - Chế độ ăn giảm calo, tăng vận động

            ## 🏃 TẬP THỂ DỤC VÀ PHÒNG NGỪA:

            **⚠️ QUAN TRỌNG:** Tập thể dục giúp phòng ngừa và điều trị đau lưng!

            **1. Khi đang đau lưng cấp:**
            - **Nghỉ ngơi:** 1-2 ngày
            - **Vận động nhẹ:** Đi bộ nhẹ sau 1-2 ngày
            - **Tránh:** Ngồi lâu, nằm lâu

            **2. Khi không đau (Phòng ngừa):**
            - **Tập cơ lưng:** Tăng sức mạnh cơ lưng
              - Tư thế siêu nhân (nằm sấp, nâng tay chân)
              - Tư thế cây cầu (nằm ngửa, nâng hông)
            - **Tập cơ bụng:** Tăng sức mạnh cơ bụng (hỗ trợ lưng)
              - Gập bụng, plank
            - **Tập linh hoạt:** Duỗi, gập lưng
            - **Yoga, pilates:** Tốt cho lưng
            - **Bơi lội:** Tốt cho lưng (ít áp lực)

            **3. Tư thế đúng:**
            - **Khi ngồi:**
              - Ngồi thẳng, lưng tựa ghế
              - Chân chạm đất
              - Màn hình ngang tầm mắt
              - Nghỉ 30 phút/lần, đứng dậy đi lại
            - **Khi đứng:**
              - Đứng thẳng, cân bằng trọng lượng 2 chân
              - Tránh đứng lâu một chỗ
            - **Khi nâng vật:**
              - Gập đầu gối, không gập lưng
              - Giữ vật gần người
              - Không xoay khi nâng
              - Nhờ người khác nếu vật quá nặng

            **4. Tần suất:**
            - **Tập cơ lưng, bụng:** 2-3 lần/tuần
            - **Tập linh hoạt:** Hàng ngày
            - **Đi bộ, bơi:** 3-5 lần/tuần, 30 phút/lần

            **5. Lợi ích:**
            - Tăng sức mạnh cơ lưng, bụng
            - Giảm nguy cơ đau lưng
            - Cải thiện tư thế
            - Tăng linh hoạt

            ## 🛡️ PHÒNG NGỪA:

            **1. Tư thế đúng:**
            - Ngồi, đứng, nâng vật đúng tư thế
            - Tránh ngồi lâu, đứng lâu

            **2. Tập thể dục:**
            - Tập cơ lưng, bụng
            - Tập linh hoạt
            - Đi bộ, bơi

            **3. Giảm cân:**
            - Nếu thừa cân
            - Giảm áp lực lên cột sống

            **4. Lối sống:**
            - **Bỏ thuốc lá:** Làm chậm lành
            - **Quản lý stress:** Stress tăng căng cơ
            - **Ngủ đủ giấc:** Nệm phù hợp, không quá mềm

            **5. Nâng vật đúng cách:**
            - Gập đầu gối, không gập lưng
            - Giữ vật gần người
            - Không xoay khi nâng
            - Nhờ người khác nếu quá nặng

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Dấu hiệu cảnh báo:**
            - Đau sau chấn thương (ngã, tai nạn)
            - Đau kèm sốt
            - Đau kèm tiểu không tự chủ, tê vùng sinh dục
            - Đau kèm sụt cân không rõ nguyên nhân
            - Đau kèm yếu chân, tê bì

            **2. Đau nặng:**
            - Đau dữ dội, không chịu được
            - Thuốc giảm đau không hiệu quả

            **3. Không cải thiện:**
            - Đau > 6 tuần không đỡ
            - Triệu chứng nặng hơn

            **4. Có dấu hiệu chèn ép thần kinh:**
            - Tê bì chân
            - Yếu chân
            - Tiểu không tự chủ

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Khi bị đau lưng:**
            - Nghỉ ngơi 1-2 ngày (không quá lâu!)
            - Chườm lạnh/ấm
            - Thuốc giảm đau
            - Vận động nhẹ sau 1-2 ngày

            **2. Phòng ngừa:**
            - Tư thế đúng
            - Tập thể dục đều đặn
            - Giảm cân nếu thừa cân
            - Nâng vật đúng cách

            **3. Không lo lắng quá:**
            - Hầu hết đau lưng tự khỏi
            - Chỉ một số ít cần điều trị đặc biệt
            - Tập thể dục → Phòng ngừa hiệu quả

            **4. Sống tích cực:**
            - Đau lưng có thể phòng ngừa
            - Tư thế đúng + Tập thể dục → Giảm nguy cơ
            """,
            related_disease="back_pain",
            related_drugs=["Paracetamol", "Ibuprofen", "Diclofenac"],
            printable=True
        ),

        PatientEducationTopic(
            id="malnutrition_basics",
            title="Understanding Malnutrition",
            title_vn="Hiểu về Suy dinh dưỡng",
            category="Disease",
            content="""
            # Hiểu về Suy dinh dưỡng

            ## Suy dinh dưỡng là gì?

            Suy dinh dưỡng là tình trạng thiếu hụt dinh dưỡng, rất phổ biến ở trẻ em vùng nông thôn Việt Nam. Bệnh ảnh hưởng đến phát triển thể chất và trí tuệ của trẻ.

            **⚠️ Đặc điểm:**
            - Thiếu hụt dinh dưỡng
            - Rất phổ biến ở trẻ em Việt Nam
            - Ảnh hưởng phát triển thể chất và trí tuệ
            - Có thể phòng ngừa và điều trị

            **Phân loại:**
            - **Thấp còi (Stunting):** Chiều cao thấp so với tuổi
            - **Gầy mòn (Wasting):** Cân nặng thấp so với chiều cao
            - **Thiếu cân (Underweight):** Cân nặng thấp so với tuổi
            - **Thiếu vi chất:** Thiếu sắt, kẽm, vitamin A, D

            ## Triệu chứng:

            **Triệu chứng thể chất:**
            - **Sụt cân, chậm tăng cân:** Không tăng cân đều
            - **Thấp còi:** Chiều cao thấp so với tuổi
            - **Gầy mòn:** Cân nặng thấp so với chiều cao
            - **Da khô, tóc khô, dễ rụng**
            - **Mệt mỏi, kém hoạt động**

            **Triệu chứng nặng:**
            - **Phù:** Nếu thiếu protein nặng (kwashiorkor)
            - **Teo cơ:** Cơ bắp yếu
            - **Chậm phát triển tâm thần vận động**

            **Triệu chứng thiếu vi chất:**
            - **Thiếu sắt:** Thiếu máu, mệt mỏi
            - **Thiếu kẽm:** Chậm tăng trưởng, nhiễm trùng
            - **Thiếu vitamin A:** Khô mắt, giảm thị lực
            - **Thiếu vitamin D:** Còi xương

            ## Nguyên nhân:

            **1. Thiếu cung cấp:**
            - Nghèo đói, thiếu thức ăn
            - Chế độ ăn không đủ, không đa dạng
            - Thiếu kiến thức dinh dưỡng

            **2. Kém hấp thu:**
            - Bệnh tiêu hóa
            - Nhiễm ký sinh trùng (giun)
            - Tiêu chảy mạn tính

            **3. Tăng nhu cầu:**
            - Bệnh mạn tính
            - Nhiễm trùng
            - Trẻ em đang lớn

            **4. Yếu tố xã hội:**
            - Vệ sinh kém
            - Nước sạch không đủ

            ## Chẩn đoán:

            **Đánh giá nhân trắc:**
            - Đo cân nặng, chiều cao
            - Tính Z-score (WHO growth charts)
            - **Z-score < -2 SD:** Suy dinh dưỡng

            **Phân loại:**
            - **Nhẹ:** -2 đến -3 SD
            - **Trung bình:** -3 đến -4 SD
            - **Nặng:** < -4 SD

            ## Điều trị:

            **1. Bổ sung dinh dưỡng:**
            - **Sữa công thức đặc biệt:** Nếu trẻ nhỏ
            - **Thức ăn bổ sung:** Đủ protein, calo
            - **Tăng dần:** Từ ít đến nhiều

            **2. Bổ sung vi chất:**
            - **Sắt:** Nếu thiếu máu
            - **Kẽm:** Tăng trưởng, miễn dịch
            - **Vitamin A:** Mắt, miễn dịch
            - **Vitamin D:** Xương

            **3. Điều trị nguyên nhân:**
            - Điều trị bệnh tiêu hóa
            - Tẩy giun
            - Điều trị nhiễm trùng

            **4. Giáo dục gia đình:**
            - Chế độ ăn đúng
            - Vệ sinh
            - Theo dõi tăng trưởng

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Trẻ < 6 tháng:**
            - **Bú mẹ hoàn toàn** (quan trọng nhất!)
            - Không cho ăn dặm sớm

            **2. Trẻ 6-24 tháng:**
            - **Tiếp tục bú mẹ** + Ăn dặm
            - **Ăn dặm đúng cách:**
              - Bắt đầu từ 6 tháng
              - Đủ 4 nhóm: Tinh bột, protein, chất béo, rau xanh
              - Ăn đa dạng, đủ lượng

            **3. Trẻ > 2 tuổi:**
            - **Ăn đủ 3 bữa chính + 2-3 bữa phụ**
            - **Đủ 4 nhóm thực phẩm:**
              - Tinh bột: Cơm, bánh mì, mì
              - Protein: Thịt, cá, trứng, đậu
              - Chất béo: Dầu, mỡ
              - Rau xanh, trái cây

            **4. Thực đơn mẫu (trẻ 2-5 tuổi):**
            - **Sáng:** Cháo thịt/cá, trứng, rau
            - **Bữa phụ:** Sữa, trái cây
            - **Trưa:** Cơm, thịt/cá, rau xanh, canh, dầu ăn
            - **Bữa phụ:** Sữa, bánh
            - **Chiều:** Cơm, thịt/cá, rau xanh, canh, dầu ăn
            - **Bữa phụ:** Sữa, trái cây

            **5. Lưu ý:**
            - Ăn đủ lượng, đủ chất
            - Đa dạng thực phẩm
            - Thêm dầu ăn (tăng calo)

            ## 🏃 TẬP THỂ DỤC:

            **1. Trẻ em:**
            - Vận động, chơi đùa bình thường
            - Không hạn chế vận động

            **2. Lưu ý:**
            - Tránh gắng sức quá mức (nếu suy dinh dưỡng nặng)
            - Tăng dần khi đã cải thiện

            ## 💊 QUẢN LÝ THUỐC:

            **1. Bổ sung vi chất:**
            - **Sắt:** Nếu thiếu máu (theo chỉ định)
            - **Kẽm:** Tăng trưởng, miễn dịch
            - **Vitamin A:** Mắt, miễn dịch
            - **Vitamin D:** Xương

            **2. Tẩy giun:**
            - Định kỳ 6 tháng/lần (nếu > 2 tuổi)
            - Albendazole, Mebendazole

            **3. Lưu ý:**
            - Theo chỉ định bác sĩ
            - Không tự ý dùng

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Suy dinh dưỡng nặng:**
            - Z-score < -4 SD
            - Phù (kwashiorkor)
            - Không ăn được

            **2. Biến chứng:**
            - Nhiễm trùng nặng
            - Thiếu máu nặng
            - Mất nước

            **3. Không cải thiện:**
            - Sau 2-3 tháng điều trị
            - Cần đánh giá lại

            ## 💡 PHÒNG NGỪA:

            **1. Nuôi con bằng sữa mẹ:**
            - Bú mẹ hoàn toàn 6 tháng đầu
            - Tiếp tục bú mẹ đến 2 tuổi

            **2. Chế độ ăn:**
            - Ăn dặm đúng cách từ 6 tháng
            - Đủ 4 nhóm thực phẩm
            - Ăn đa dạng, đủ lượng

            **3. Vệ sinh:**
            - Rửa tay thường xuyên
            - Nước sạch
            - Vệ sinh thực phẩm

            **4. Tẩy giun:**
            - Định kỳ 6 tháng/lần (trẻ > 2 tuổi)

            **5. Theo dõi:**
            - Đo cân nặng, chiều cao định kỳ
            - Phát hiện sớm

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Khi trẻ bị suy dinh dưỡng:**
            - Bổ sung dinh dưỡng đúng cách
            - Điều trị nguyên nhân
            - Theo dõi tăng trưởng
            - Giáo dục gia đình

            **2. Chế độ ăn:**
            - Bú mẹ (nếu có thể)
            - Ăn đủ 4 nhóm thực phẩm
            - Ăn đa dạng, đủ lượng
            - Thêm dầu ăn (tăng calo)

            **3. Sống tích cực:**
            - Suy dinh dưỡng có thể điều trị
            - Điều trị đúng → Trẻ tăng trưởng tốt
            - Phòng ngừa tốt → Trẻ phát triển bình thường

            **4. Gia đình:**
            - Giáo dục dinh dưỡng
            - Hỗ trợ xã hội (nếu nghèo)
            - Theo dõi tăng trưởng định kỳ
            """,
            related_disease="malnutrition",
            related_drugs=["Iron", "Zinc", "Vitamin A", "Vitamin D", "Albendazole"],
            printable=True
        ),

        PatientEducationTopic(
            id="food_allergy_basics",
            title="Understanding Food Allergy",
            title_vn="Hiểu về Dị ứng thực phẩm",
            category="Disease",
            content="""
            # Hiểu về Dị ứng thực phẩm

            ## Dị ứng thực phẩm là gì?

            Dị ứng thực phẩm là phản ứng miễn dịch bất thường với thực phẩm, có thể gây phản ứng từ nhẹ đến nặng, đe dọa tính mạng. Bệnh rất phổ biến, đặc biệt ở trẻ em.

            **⚠️ Đặc điểm:**
            - Phản ứng miễn dịch bất thường với thực phẩm
            - Có thể gây phản vệ (nguy hiểm!)
            - Rất phổ biến (5-8% trẻ em, 2-4% người lớn)
            - Cần tránh thực phẩm gây dị ứng

            **Thực phẩm gây dị ứng phổ biến:**
            - **Trẻ em:** Trứng, sữa, đậu phộng, hải sản, lúa mì, đậu nành
            - **Người lớn:** Hải sản (tôm, cua), đậu phộng, cá

            ## Triệu chứng:

            **Triệu chứng da:**
            - **Mề đay:** Nổi mẩn đỏ, ngứa
            - **Phù mạch:** Sưng môi, mí mắt, mặt
            - **Ngứa:** Toàn thân hoặc cục bộ

            **Triệu chứng tiêu hóa:**
            - Buồn nôn, nôn
            - Tiêu chảy
            - Đau bụng

            **Triệu chứng hô hấp:**
            - Khó thở
            - Thở khò khè
            - Nghẹt mũi

            **⚠️ Phản vệ (Anaphylaxis):**
            - Khó thở nặng
            - Hạ huyết áp, sốc
            - Mất ý thức
            - **Cấp cứu ngay!**

            **Thời gian:**
            - Thường xuất hiện trong vài phút đến 2 giờ sau ăn
            - Có thể chậm hơn (4-6 giờ) nếu không phải IgE-mediated

            ## Nguyên nhân:

            **1. Thực phẩm phổ biến:**
            - **Trẻ em:** Trứng, sữa, đậu phộng, hải sản, lúa mì, đậu nành
            - **Người lớn:** Hải sản (tôm, cua), đậu phộng, cá, hạt cây

            **2. Yếu tố nguy cơ:**
            - Tiền sử gia đình dị ứng
            - Trẻ em (dễ dị ứng hơn)
            - Có bệnh dị ứng khác (hen, viêm mũi dị ứng)

            **3. Cơ chế:**
            - IgE-mediated (phản ứng nhanh, có thể phản vệ)
            - Non-IgE (phản ứng chậm, thường tiêu hóa)

            ## Chẩn đoán:

            **Xét nghiệm:**
            - **Test da (skin prick test):** Nhanh, dễ làm
            - **IgE đặc hiệu (RAST, ImmunoCAP):** Xét nghiệm máu
            - **Test thử thách (oral food challenge):** Chuẩn vàng (cần bác sĩ)

            ## Điều trị:

            **1. Tránh thực phẩm gây dị ứng:**
            - **Quan trọng nhất!**
            - Đọc nhãn thực phẩm
            - Hỏi thành phần khi ăn ngoài
            - Tránh chéo (cross-contamination)

            **2. Phản ứng nhẹ:**
            - Antihistamine (Cetirizine, Loratadine)
            - Corticosteroid (nếu cần)

            **3. Phản vệ:**
            - **Epinephrine auto-injector:** Tiêm ngay!
            - Gọi cấp cứu
            - Nằm xuống, nâng chân

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Tránh thực phẩm gây dị ứng:**
            - **Hoàn toàn** (quan trọng!)
            - Đọc nhãn thực phẩm
            - Hỏi thành phần khi ăn ngoài

            **2. Thực phẩm thay thế:**
            - **Dị ứng sữa:** Sữa đậu nành, sữa dê (nếu không dị ứng)
            - **Dị ứng trứng:** Thay thế trong nấu ăn
            - **Dị ứng đậu phộng:** Tránh tất cả hạt cây

            **3. Đọc nhãn:**
            - Kiểm tra thành phần
            - Cảnh báo "có thể chứa" (may contain)

            **4. Thực đơn mẫu (nếu dị ứng đậu phộng, hải sản):**
            - **Sáng:** Cháo thịt, trứng, rau
            - **Trưa:** Cơm, thịt gà/bò, rau xanh, canh
            - **Chiều:** Cơm, thịt, rau xanh, canh
            - **Bữa phụ:** Trái cây, sữa (nếu không dị ứng sữa)

            **5. Lưu ý:**
            - Tránh chéo (dùng chung dụng cụ, bề mặt)
            - Vệ sinh tay, dụng cụ sau khi chế biến

            ## 🏃 TẬP THỂ DỤC:

            **1. Nên tập:**
            - Tập thể dục bình thường
            - Đi bộ, chạy bộ, bơi lội
            - 30 phút/ngày, 5 ngày/tuần

            **2. Lưu ý:**
            - Mang epinephrine auto-injector khi tập
            - Tránh tập ngay sau ăn (nếu có nguy cơ phản vệ do gắng sức)

            ## 💊 QUẢN LÝ THUỐC:

            **1. Epinephrine auto-injector:**
            - **Mang theo mọi lúc** (nếu có nguy cơ phản vệ)
            - Biết cách sử dụng
            - Kiểm tra hạn sử dụng

            **2. Antihistamine:**
            - Dùng khi phản ứng nhẹ
            - Cetirizine, Loratadine

            **3. Lưu ý:**
            - Luôn mang epinephrine nếu có nguy cơ phản vệ
            - Đeo vòng cảnh báo y tế

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Phản vệ:**
            - Khó thở nặng
            - Hạ huyết áp, sốc
            - Mất ý thức
            - **Tiêm epinephrine ngay, gọi cấp cứu!**

            **2. Phản ứng nặng:**
            - Phù mạch nặng (sưng mặt, cổ họng)
            - Khó thở
            - Nôn nhiều

            **3. Phản ứng lan rộng:**
            - Mề đay toàn thân
            - Triệu chứng nặng hơn

            ## 💡 PHÒNG NGỪA:

            **1. Tránh thực phẩm gây dị ứng:**
            - **Hoàn toàn** (quan trọng nhất!)
            - Đọc nhãn thực phẩm
            - Hỏi thành phần

            **2. Giáo dục:**
            - Giáo dục bệnh nhân và gia đình
            - Nhận biết triệu chứng
            - Cách sử dụng epinephrine

            **3. Chuẩn bị:**
            - Mang epinephrine auto-injector
            - Đeo vòng cảnh báo y tế
            - Thông báo cho người xung quanh

            **4. Trẻ em:**
            - Giáo dục trẻ (nếu đủ tuổi)
            - Thông báo cho nhà trường
            - Hướng dẫn giáo viên

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Khi bị dị ứng thực phẩm:**
            - Tránh thực phẩm gây dị ứng hoàn toàn
            - Đọc nhãn thực phẩm
            - Mang epinephrine nếu có nguy cơ phản vệ
            - Đeo vòng cảnh báo y tế

            **2. Khi ăn ngoài:**
            - Hỏi thành phần
            - Thông báo dị ứng
            - Cẩn thận với đồ ăn chế biến sẵn

            **3. Sống tích cực:**
            - Dị ứng thực phẩm có thể kiểm soát
            - Tránh tốt → Không có phản ứng
            - Có thể sống bình thường

            **4. Trẻ em:**
            - Giáo dục trẻ (nếu đủ tuổi)
            - Thông báo cho nhà trường
            - Hướng dẫn cách xử lý phản ứng
            """,
            related_disease="food_allergy",
            related_drugs=["Epinephrine", "Antihistamine", "Corticosteroid"],
            printable=True
        ),

        PatientEducationTopic(
            id="anaphylaxis_basics",
            title="Understanding Anaphylaxis",
            title_vn="Hiểu về Phản vệ",
            category="Disease",
            content="""
            # Hiểu về Phản vệ

            ## Phản vệ là gì?

            Phản vệ là phản ứng dị ứng nghiêm trọng, đe dọa tính mạng, xảy ra nhanh chóng sau khi tiếp xúc với chất gây dị ứng. Bệnh cần điều trị cấp cứu ngay lập tức.

            **⚠️ Đặc điểm:**
            - Phản ứng dị ứng nghiêm trọng
            - Đe dọa tính mạng
            - Xảy ra nhanh chóng (vài phút đến vài giờ)
            - Cần điều trị cấp cứu ngay

            **⚠️ Nguy hiểm:**
            - Có thể tử vong nếu không điều trị
            - Cần tiêm Adrenaline ngay
            - Gọi cấp cứu 115

            ## Triệu chứng:

            **Triệu chứng điển hình:**
            - **Phù:** Phù mặt, môi, lưỡi, họng
            - **Khó thở:** Thở khò khè, khó nuốt
            - **Phát ban:** Nổi mề đay, ngứa
            - **Huyết áp tụt:** Chóng mặt, ngất xỉu
            - **Nhịp tim nhanh:** Đánh trống ngực
            - **Buồn nôn, nôn:** Có thể có
            - **Đau bụng:** Có thể có

            **⚠️ Dấu hiệu nguy hiểm:**
            - Khó thở nặng
            - Phù họng, lưỡi
            - Huyết áp tụt
            - Sốc
            - **Cấp cứu ngay!**

            **⚠️ Phản vệ 2 pha:**
            - Triệu chứng tái phát sau 4-12 giờ
            - Cần theo dõi 24 giờ

            ## Nguyên nhân:

            **1. Thực phẩm:**
            - **Đậu phộng:** Phổ biến nhất
            - **Hải sản:** Tôm, cua, cá
            - **Sữa, trứng**
            - **Hạt:** Hạnh nhân, óc chó

            **2. Thuốc:**
            - **Penicillin:** Phổ biến
            - **NSAID:** Aspirin, Ibuprofen
            - **Thuốc cản quang**
            - **Vắc xin:** Hiếm

            **3. Côn trùng đốt:**
            - Ong, ong bắp cày
            - Kiến lửa

            **4. Latex:**
            - Găng tay, bao cao su

            **5. Yếu tố nguy cơ:**
            - Tiền sử dị ứng
            - Hen phế quản
            - Bệnh tim mạch

            ## Chẩn đoán:

            **Chẩn đoán lâm sàng:**
            - Triệu chứng điển hình
            - Tiếp xúc với chất gây dị ứng
            - Xảy ra nhanh chóng

            **Xét nghiệm:**
            - **Tryptase:** Tăng trong phản vệ
            - **Test dị ứng:** Tìm chất gây dị ứng

            ## Điều trị:

            **1. Adrenaline (QUAN TRỌNG NHẤT!):**
            - **Tiêm bắp:** 0.3-0.5mg (người lớn), 0.01mg/kg (trẻ em)
            - **Lặp lại:** Sau 5-15 phút nếu cần
            - **Tự tiêm:** EpiPen, Auvi-Q (nếu có)

            **2. Gọi cấp cứu:**
            - **Gọi 115 ngay!**
            - Đưa đến bệnh viện
            - Theo dõi 24 giờ

            **3. Điều trị hỗ trợ:**
            - **Oxy:** Nếu khó thở
            - **Truyền dịch:** Nếu huyết áp tụt
            - **Antihistamine:** Cetirizine, Diphenhydramine
            - **Corticosteroid:** Prednisone (giảm phản vệ 2 pha)

            **4. Tư thế:**
            - Nằm ngửa, nâng chân
            - Nếu khó thở: Ngồi dậy

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Tránh chất gây dị ứng:**
            - **Tránh hoàn toàn** chất gây dị ứng đã biết
            - Đọc nhãn thực phẩm
            - Hỏi thành phần khi ăn ngoài

            **2. Thực phẩm an toàn:**
            - Ăn thực phẩm đã biết an toàn
            - Tránh thực phẩm nghi ngờ

            **3. Lưu ý:**
            - Mang EpiPen khi đi ăn ngoài
            - Báo nhà hàng về dị ứng

            ## 🏃 TẬP THỂ DỤC:

            **1. Bình thường:**
            - Tập thể dục bình thường
            - Tránh tập sau khi ăn (nếu dị ứng thực phẩm)

            **2. Lưu ý:**
            - Mang EpiPen khi tập
            - Tránh tập một mình

            ## 💊 QUẢN LÝ THUỐC:

            **1. EpiPen (QUAN TRỌNG!):**
            - **Mang theo mọi lúc**
            - Biết cách sử dụng
            - Kiểm tra hạn sử dụng
            - Thay mới khi hết hạn

            **2. Antihistamine:**
            - Mang theo (Cetirizine)
            - Dùng sau khi tiêm Adrenaline

            **3. Corticosteroid:**
            - Prednisone: Nếu có chỉ định
            - Giảm phản vệ 2 pha

            **4. Lưu ý:**
            - **Mang EpiPen mọi lúc** (quan trọng nhất!)
            - Báo người xung quanh về dị ứng
            - Đeo vòng cảnh báo y tế

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Phản vệ:**
            - **Tiêm Adrenaline ngay**
            - **Gọi 115 ngay**
            - Đưa đến bệnh viện

            **2. Triệu chứng nặng:**
            - Khó thở nặng
            - Phù họng, lưỡi
            - Huyết áp tụt
            - Sốc

            **3. Sau phản vệ:**
            - Theo dõi 24 giờ (phản vệ 2 pha)
            - Tái khám nếu cần

            ## 💡 PHÒNG NGỪA:

            **1. Tránh chất gây dị ứng:**
            - **Tránh hoàn toàn** chất gây dị ứng đã biết
            - Đọc nhãn thực phẩm
            - Hỏi thành phần khi ăn ngoài

            **2. Mang EpiPen:**
            - **Mang theo mọi lúc**
            - Biết cách sử dụng
            - Kiểm tra hạn sử dụng

            **3. Báo người xung quanh:**
            - Báo gia đình, bạn bè về dị ứng
            - Đeo vòng cảnh báo y tế
            - Báo nhà hàng, trường học

            **4. Test dị ứng:**
            - Xác định chất gây dị ứng
            - Tránh tiếp xúc

            **5. Miễn dịch trị liệu:**
            - Có thể điều trị một số dị ứng (đậu phộng, ong đốt)
            - Giảm nguy cơ phản vệ

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Phòng ngừa:**
            - **Tránh chất gây dị ứng** (quan trọng nhất!)
            - **Mang EpiPen mọi lúc**
            - Đọc nhãn thực phẩm

            **2. Khi bị phản vệ:**
            - **Tiêm Adrenaline ngay** (quan trọng nhất!)
            - **Gọi 115 ngay**
            - Đưa đến bệnh viện
            - Theo dõi 24 giờ

            **3. Sống tích cực:**
            - Phản vệ có thể phòng ngừa
            - Tránh chất gây dị ứng → Không mắc bệnh
            - Mang EpiPen → Cứu sống khi phản vệ

            **4. Chuẩn bị:**
            - **Mang EpiPen mọi lúc**
            - Biết cách sử dụng
            - Báo người xung quanh
            - Đeo vòng cảnh báo y tế
            - Có kế hoạch hành động khi phản vệ
            """,
            related_disease="anaphylaxis",
            related_drugs=["Adrenaline", "Epinephrine", "Cetirizine", "Diphenhydramine", "Prednisone"],
            printable=True
        ),

]
