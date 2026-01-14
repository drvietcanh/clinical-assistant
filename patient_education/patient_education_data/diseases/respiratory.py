"""
Patient Education Topics - Respiratory
"""
from patient_education.models import PatientEducationTopic


RESPIRATORY_TOPICS = [
        PatientEducationTopic(
                id="pneumonia_basics",
                title="Understanding Pneumonia",
                title_vn="Hiểu về Viêm phổi",
                category="Disease",
                content="""
            # Hiểu về Viêm phổi

            ## Viêm phổi là gì?

            Viêm phổi là tình trạng nhiễm trùng phổi, gây viêm các túi khí (phế nang) trong phổi. Phế nang bị đầy dịch hoặc mủ, làm khó trao đổi oxy.

            **⚠️ Nguy hiểm:** Viêm phổi có thể nặng, đặc biệt ở trẻ em, người già, người có bệnh mạn tính.

            ## Nguyên nhân:

            **1. Vi khuẩn (Phổ biến nhất):**
            - **Streptococcus pneumoniae (Phế cầu):** Phổ biến nhất
            - **Haemophilus influenzae**
            - **Mycoplasma pneumoniae:** Viêm phổi không điển hình
            - **Legionella:** Từ nước, điều hòa không khí
            - **Điều trị:** Kháng sinh

            **2. Virus:**
            - **Cúm (Influenza):** Phổ biến
            - **COVID-19:** SARS-CoV-2
            - **RSV:** Ở trẻ em
            - **Điều trị:** Hỗ trợ, một số có thuốc kháng virus

            **3. Nấm (Hiếm):**
            - Thường ở người suy giảm miễn dịch
            - **Điều trị:** Thuốc kháng nấm

            **4. Yếu tố nguy cơ:**
            - Tuổi: Trẻ < 2 tuổi, người > 65 tuổi
            - Hút thuốc lá
            - Bệnh mạn tính: COPD, đái tháo đường, suy tim
            - Suy giảm miễn dịch
            - Nằm viện, nằm liệt giường

            ## Triệu chứng:

            **Triệu chứng điển hình (Viêm phổi do vi khuẩn):**
            - **Sốt:** 38-40°C, có thể kèm ớn lạnh, run
            - **Ho:** Ho có đờm vàng/xanh, đặc
            - **Khó thở:** Thở nhanh, nông
            - **Đau ngực:** Đau nhói, tăng khi ho, hít sâu
            - **Mệt mỏi:** Uể oải, không có sức

            **Triệu chứng viêm phổi do virus:**
            - Sốt, ớn lạnh
            - Ho khan hoặc ít đờm
            - Đau cơ, đau đầu
            - Mệt mỏi

            **Triệu chứng ở người già:**
            - Có thể không sốt
            - Lú lẫn, mê sảng
            - Mệt mỏi, yếu
            - Ăn kém

            **Triệu chứng ở trẻ em:**
            - Sốt, ho
            - Thở nhanh, rút lõm lồng ngực
            - Bỏ ăn, quấy khóc
            - Môi tím (nặng)

            ## Điều trị:

            **1. Kháng sinh (Nếu do vi khuẩn):**
            - **Nhẹ (Điều trị tại nhà):**
              - Amoxicillin, Amoxicillin-Clavulanate
              - Azithromycin, Clarithromycin
            - **Nặng (Điều trị tại viện):**
              - Ceftriaxone, Levofloxacin
              - Có thể cần tiêm tĩnh mạch
            - **⚠️ QUAN TRỌNG:**
              - Uống đủ liều, đủ ngày (thường 7-14 ngày)
              - Không tự ý ngừng khi thấy đỡ
              - Uống đúng giờ

            **2. Hỗ trợ:**
            - **Nghỉ ngơi:** Nghỉ hoàn toàn, không làm việc
            - **Uống nhiều nước:** 2-3 lít/ngày (trừ khi bác sĩ hạn chế)
            - **Hạ sốt:** Paracetamol 500-1000mg mỗi 4-6 giờ (nếu sốt > 38.5°C)
            - **Giảm ho:** Nếu ho quá nhiều, dùng thuốc giảm ho (hỏi bác sĩ)
            - **Oxy:** Nếu khó thở nặng, SpO2 < 90%

            **3. Điều trị tại nhà:**
            - Nghỉ ngơi trên giường
            - Uống đủ nước (nước lọc, nước cam, súp)
            - Ăn nhẹ, dễ tiêu
            - Theo dõi triệu chứng
            - Tái khám sau 2-3 ngày

            **4. Điều trị tại viện (Nếu nặng):**
            - Kháng sinh tiêm tĩnh mạch
            - Oxy liệu pháp
            - Truyền dịch
            - Theo dõi sát

            ## 🍽️ CHẾ ĐỘ ĂN KHI BỊ VIÊM PHỔI:

            **1. Nguyên tắc:**
            - **Ăn nhẹ, dễ tiêu:** Tránh đồ chiên, nhiều dầu mỡ
            - **Đủ dinh dưỡng:** Giúp cơ thể chống lại nhiễm trùng
            - **Nhiều bữa nhỏ:** 5-6 bữa/ngày (dễ ăn hơn)
            - **Uống nhiều nước:** Giúp loãng đờm, dễ khạc

            **2. Thực phẩm nên ăn:**
            - **Súp, cháo:** Dễ nuốt, dễ tiêu, có nước
              - Cháo gà, cháo thịt bằm
              - Súp rau củ
              - Canh nóng
            - **Trái cây:** Cam, bưởi (vitamin C), chuối (dễ ăn)
            - **Rau xanh:** Luộc, hấp (vitamin, chất xơ)
            - **Protein:** Thịt nạc, cá, trứng (luộc, hấp)
            - **Sữa ấm:** Dễ uống, có protein

            **3. Thực phẩm nên tránh:**
            - **Đồ chiên, nhiều dầu mỡ:** Khó tiêu
            - **Đồ lạnh:** Làm ho nhiều hơn
            - **Đồ cay:** Kích thích ho
            - **Rượu bia:** Làm giảm miễn dịch
            - **Đồ ngọt:** Làm tăng đờm

            **4. Uống nước:**
            - **Nước lọc:** Tốt nhất
            - **Nước cam, chanh:** Vitamin C
            - **Trà gừng ấm:** Giảm ho, ấm cổ họng
            - **Súp, canh:** Vừa ăn vừa uống nước
            - **Mục tiêu:** 2-3 lít/ngày (nếu không hạn chế)

            **5. Lưu ý:**
            - Ăn chậm, nhai kỹ
            - Nghỉ giữa các bữa
            - Nếu không ăn được → Uống sữa, nước trái cây
            - Không bỏ bữa (cơ thể cần năng lượng)

            ## 🏥 CHĂM SÓC TẠI NHÀ:

            **1. Nghỉ ngơi:**
            - Nghỉ hoàn toàn, không làm việc
            - Ngủ đủ giấc (8-10 giờ/đêm)
            - Tránh gắng sức
            - Nghỉ ít nhất 1 tuần

            **2. Vệ sinh:**
            - Rửa tay thường xuyên (tránh lây)
            - Che miệng khi ho, hắt hơi
            - Dùng khăn giấy, vứt ngay
            - Không dùng chung đồ dùng

            **3. Theo dõi triệu chứng:**
            - Đo nhiệt độ 2-3 lần/ngày
            - Theo dõi ho, đờm
            - Theo dõi khó thở
            - Ghi nhật ký

            **4. Giảm ho:**
            - Uống nước ấm
            - Xông hơi (nước nóng, thêm gừng)
            - Súc miệng nước muối
            - Kê gối cao khi ngủ

            **5. Giảm đau ngực:**
            - Nằm nghiêng bên đau (nếu được)
            - Tránh ho mạnh (uống thuốc giảm ho)
            - Chườm ấm

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN NGAY:

            **1. Khó thở nặng:**
            - Thở nhanh (> 25 lần/phút ở người lớn)
            - Khó thở khi nghỉ
            - Môi, móng tay tím
            - Không nói được câu dài

            **2. Sốt cao:**
            - Sốt > 39°C không hạ sau dùng Paracetamol
            - Sốt kéo dài > 3 ngày
            - Ớn lạnh, run nhiều

            **3. Triệu chứng nặng:**
            - Đau ngực dữ dội
            - Lú lẫn, mê sảng
            - Mệt mỏi cực độ, không ăn được
            - Nôn nhiều, không uống được

            **4. Không cải thiện:**
            - Sau 2-3 ngày điều trị tại nhà
            - Triệu chứng nặng hơn
            - Đờm có máu

            **5. Yếu tố nguy cơ cao:**
            - Trẻ < 2 tuổi
            - Người > 65 tuổi
            - Có bệnh mạn tính nặng
            - Suy giảm miễn dịch

            ## 💊 UỐNG KHÁNG SINH ĐÚNG CÁCH:

            **⚠️ QUAN TRỌNG:** Uống kháng sinh đúng cách để điều trị hiệu quả và tránh kháng kháng sinh!

            **1. Uống đủ liều, đủ ngày:**
            - Uống đúng liều bác sĩ kê
            - Uống đủ số ngày (thường 7-14 ngày)
            - **KHÔNG tự ý ngừng khi thấy đỡ!**
            - Ngừng sớm → Vi khuẩn chưa chết hết → Tái phát, kháng thuốc

            **2. Uống đúng giờ:**
            - Cách đều nhau trong ngày
            - Ví dụ: 3 lần/ngày → Cách 8 giờ (8h, 16h, 24h)
            - Đặt báo thức nhắc nhở

            **3. Uống đúng cách:**
            - **Trước/sau ăn:** Theo hướng dẫn bác sĩ
              - Một số uống trước ăn (hấp thu tốt hơn)
              - Một số uống sau ăn (tránh đau dạ dày)
            - Uống với nước lọc (không dùng sữa, nước trái cây - trừ khi bác sĩ nói)
            - Không nghiền viên thuốc (trừ khi bác sĩ nói)

            **4. Tác dụng phụ:**
            - **Buồn nôn, nôn:** Uống sau ăn, chia nhỏ liều
            - **Tiêu chảy:** Uống nhiều nước, ăn sữa chua (probiotic)
            - **Phát ban:** Báo bác sĩ ngay (có thể dị ứng)
            - **Đau dạ dày:** Uống sau ăn

            **5. Tương tác:**
            - Báo bác sĩ TẤT CẢ thuốc đang dùng
            - Một số kháng sinh tương tác với thuốc khác

            ## 🛡️ PHÒNG NGỪA:

            **1. Tiêm chủng (QUAN TRỌNG!):**
            - **Vắc xin phế cầu:**
              - Người > 65 tuổi
              - Người có bệnh mạn tính
              - Tiêm 1 lần hoặc nhắc lại (hỏi bác sĩ)
            - **Vắc xin cúm hàng năm:**
              - Tất cả mọi người
              - Đặc biệt quan trọng với người có nguy cơ cao
            - **Vắc xin COVID-19:** Theo khuyến cáo

            **2. Vệ sinh:**
            - **Rửa tay:** Thường xuyên với xà phòng, ít nhất 20 giây
            - **Che miệng:** Khi ho, hắt hơi (khăn giấy, khuỷu tay)
            - **Không dùng chung:** Đồ dùng, khăn, cốc
            - **Vệ sinh bề mặt:** Lau sạch bàn, tay nắm cửa

            **3. Lối sống:**
            - **Bỏ thuốc lá:** Hút thuốc làm tăng nguy cơ viêm phổi
            - **Giữ sức khỏe:** Ăn uống đủ chất, tập thể dục
            - **Ngủ đủ:** 7-8 giờ/đêm
            - **Quản lý stress:** Stress làm giảm miễn dịch

            **4. Tránh yếu tố nguy cơ:**
            - Tránh người ốm (nếu có thể)
            - Tránh nơi đông người khi có dịch
            - Đeo khẩu trang khi cần
            - Giữ ấm khi trời lạnh

            **5. Điều trị bệnh mạn tính:**
            - Kiểm soát tốt đái tháo đường, COPD, suy tim
            - Giảm nguy cơ viêm phổi

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Khi bắt đầu điều trị:**
            - Nghỉ ngơi hoàn toàn
            - Uống thuốc đúng giờ
            - Uống nhiều nước
            - Ăn nhẹ, dễ tiêu
            - Theo dõi triệu chứng

            **2. Theo dõi tiến triển:**
            - Triệu chứng nên cải thiện sau 2-3 ngày
            - Sốt giảm dần
            - Ho, đờm giảm
            - Khó thở giảm
            - **Nếu không cải thiện → Tái khám ngay**

            **3. Tái khám:**
            - Sau 2-3 ngày điều trị tại nhà
            - Hoặc ngay nếu triệu chứng nặng hơn
            - Bác sĩ sẽ đánh giá lại, có thể đổi kháng sinh

            **4. Phòng ngừa tái phát:**
            - Tiêm chủng đầy đủ
            - Bỏ thuốc lá
            - Giữ sức khỏe tốt
            - Rửa tay thường xuyên

            **5. Hỗ trợ:**
            - Nghỉ ngơi đầy đủ
            - Uống đủ nước
            - Ăn đủ chất
            - Nhờ người thân giúp đỡ khi cần
                """,
                related_disease="pneumonia",
                related_drugs=["Amoxicillin", "Azithromycin", "Levofloxacin"],
                printable=True
        ),

        PatientEducationTopic(
                id="copd_basics",
                title="Understanding COPD",
                title_vn="Hiểu về COPD",
                category="Disease",
                content="""
            # Hiểu về COPD

            ## COPD là gì?

            COPD (Bệnh phổi tắc nghẽn mạn tính) là bệnh phổi mạn tính gây khó thở do đường thở bị hẹp và phá hủy. Không khí khó vào và ra khỏi phổi.

            **Bao gồm 2 bệnh:**
            - **Viêm phế quản mạn tính:** Ho, khạc đờm kéo dài
            - **Khí phế thũng:** Phá hủy phế nang, mất tính đàn hồi phổi

            **⚠️ Đặc điểm:** Bệnh tiến triển, không hồi phục hoàn toàn, nhưng có thể kiểm soát.

            ## Nguyên nhân:

            **1. Hút thuốc lá (80-90%):**
            - Nguyên nhân chính nhất
            - Hút càng lâu, càng nhiều → Nguy cơ càng cao
            - Hút thuốc thụ động cũng nguy hiểm

            **2. Ô nhiễm không khí:**
            - Khói bụi từ giao thông, nhà máy
            - Khói từ đốt than, củi
            - Bụi mịn PM2.5

            **3. Khói, bụi nghề nghiệp:**
            - Công nhân xây dựng, khai thác mỏ
            - Tiếp xúc hóa chất, bụi vải, bụi gỗ

            **4. Yếu tố khác:**
            - Nhiễm trùng phổi tái phát khi nhỏ
            - Thiếu alpha-1 antitrypsin (hiếm, di truyền)
            - Tuổi cao

            ## Triệu chứng:

            **Triệu chứng chính:**
            - **Ho mạn tính:** Ho kéo dài, đặc biệt buổi sáng
            - **Khạc đờm:** Đờm trắng, vàng, xanh (khi có nhiễm trùng)
            - **Khó thở:**
              - Khi gắng sức (đi bộ, leo cầu thang)
              - Tiến triển: Khó thở cả khi nghỉ
              - Nặng: Khó thở khi nói, ăn, mặc quần áo
            - **Thở khò khè:** Tiếng rít khi thở
            - **Tức ngực:** Cảm giác nặng ngực

            **Triệu chứng khác:**
            - Mệt mỏi
            - Sụt cân (do khó thở khi ăn)
            - Phù chân (khi có suy tim phải)
            - Đau đầu buổi sáng (do thiếu oxy)

            **⚠️ Phân độ COPD (GOLD):**
            - **Độ 1 (Nhẹ):** FEV1 ≥ 80% bình thường
            - **Độ 2 (Trung bình):** FEV1 50-79%
            - **Độ 3 (Nặng):** FEV1 30-49%
            - **Độ 4 (Rất nặng):** FEV1 < 30% hoặc có suy hô hấp

            ## Điều trị:

            **1. Bỏ thuốc lá (QUAN TRỌNG NHẤT!):**
            - Bỏ thuốc → Làm chậm tiến triển bệnh
            - Không bao giờ quá muộn để bỏ
            - Xem topic "Bỏ Thuốc lá" để biết cách

            **2. Thuốc:**
            - **Thuốc giãn phế quản:**
              - Tác dụng ngắn: Salbutamol (cắt cơn)
              - Tác dụng dài: Tiotropium, Salmeterol (dự phòng)
            - **Corticosteroid hít:** Budesonide, Fluticasone (giảm viêm)
            - **Kháng sinh:** Khi có nhiễm trùng
            - **Quan trọng:** Dùng thuốc hít đúng cách (xem hướng dẫn)

            **3. Oxy liệu pháp:**
            - Khi thiếu oxy nặng (SpO2 < 88%)
            - Dùng ít nhất 15 giờ/ngày
            - Giúp sống lâu hơn, chất lượng sống tốt hơn

            **4. Phục hồi chức năng phổi:**
            - Tập thể dục có hướng dẫn
            - Tập thở
            - Giáo dục về bệnh
            - Tư vấn dinh dưỡng

            **5. Tiêm chủng:**
            - Vắc xin cúm hàng năm
            - Vắc xin phế cầu (1 lần hoặc nhắc lại)

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Nguyên tắc:**
            - **Ăn nhiều bữa nhỏ:** 5-6 bữa/ngày (khó thở khi ăn no)
            - **Thực phẩm dễ tiêu:** Tránh đồ chiên, nhiều dầu mỡ
            - **Đủ calo:** Tránh sụt cân
            - **Đủ protein:** Giúp cơ hô hấp khỏe

            **2. Thực phẩm nên ăn:**
            - **Protein:** Thịt nạc, cá, đậu, trứng, sữa
            - **Carbohydrate phức tạp:** Gạo, bánh mì, khoai (năng lượng)
            - **Rau xanh:** Nhiều vitamin, chất xơ
            - **Trái cây:** Vitamin C (cam, bưởi, ổi)
            - **Chất béo tốt:** Dầu ô liu, quả bơ, các loại hạt

            **3. Thực phẩm cần tránh:**
            - **Đồ chiên, nhiều dầu mỡ:** Khó tiêu, gây đầy bụng → Khó thở
            - **Đồ uống có ga:** Gây đầy bụng
            - **Muối nhiều:** Giữ nước → Khó thở (nếu có suy tim)
            - **Rượu bia:** Làm giảm chức năng hô hấp

            **4. Lưu ý khi ăn:**
            - Ăn chậm, nhai kỹ
            - Nghỉ giữa các miếng ăn
            - Ngồi thẳng khi ăn
            - Uống nước sau ăn (tránh đầy bụng)
            - Dùng ống hút nếu cần

            **5. Nếu sụt cân:**
            - Tăng calo: Thêm dầu, bơ vào thức ăn
            - Uống sữa bổ sung dinh dưỡng
            - Ăn nhiều bữa nhỏ
            - Tham khảo bác sĩ dinh dưỡng

            ## 🏃 TẬP THỂ DỤC VÀ PHỤC HỒI CHỨC NĂNG:

            **⚠️ QUAN TRỌNG:** Tập thể dục giúp cải thiện khó thở, tăng khả năng hoạt động!

            **1. Tập thở (Quan trọng!):**

            **Thở môi mím:**
            - Hít vào bằng mũi (2 giây)
            - Mím môi, thở ra chậm bằng miệng (4 giây)
            - Lặp lại 10-15 lần, 3-4 lần/ngày
            - **Lợi ích:** Giảm khó thở, thở hiệu quả hơn

            **Thở bụng (Cơ hoành):**
            - Đặt tay lên bụng
            - Hít vào: Bụng phình ra
            - Thở ra: Bụng xẹp vào
            - Tập 10-15 phút/ngày
            - **Lợi ích:** Tăng sức mạnh cơ hoành

            **2. Tập thể dục:**

            **Đi bộ:**
            - Bắt đầu: 5-10 phút/ngày
            - Tăng dần: 20-30 phút/ngày
            - Tần suất: Hàng ngày
            - **Lưu ý:** Đi chậm, nghỉ khi mệt, dùng thở môi mím

            **Đạp xe tại chỗ:**
            - 15-20 phút/ngày
            - Tần suất: 3-5 lần/tuần
            - **Lợi ích:** Tăng sức mạnh chân, tim mạch

            **Tập tay:**
            - Nâng tạ nhẹ, dây kháng lực
            - 10-15 phút/ngày
            - **Lợi ích:** Tăng sức mạnh cơ hô hấp phụ

            **3. Lưu ý khi tập:**
            - Khởi động 5-10 phút
            - Tập vừa sức (có thể nói được câu ngắn)
            - Nghỉ khi mệt
            - Dùng thở môi mím khi khó thở
            - Dừng ngay nếu: Đau ngực, chóng mặt, khó thở nặng

            **4. Lợi ích:**
            - Giảm khó thở
            - Tăng khả năng hoạt động
            - Giảm số đợt cấp
            - Cải thiện chất lượng sống

            ## 💨 DÙNG THUỐC HÍT ĐÚNG CÁCH:

            **⚠️ QUAN TRỌNG:** Dùng sai → Thuốc không vào phổi → Không hiệu quả!

            **1. Chuẩn bị:**
            - Lắc bình xịt (nếu dùng bình xịt)
            - Tháo nắp
            - Kiểm tra còn thuốc không

            **2. Kỹ thuật:**
            - **Thở ra:** Thở hết không khí
            - **Hít vào:** Đưa ống hít vào miệng, bấm và hít sâu, chậm
            - **Giữ hơi:** 10 giây (nếu được)
            - **Thở ra:** Chậm, bằng miệng

            **3. Lưu ý:**
            - Rửa miệng sau dùng corticosteroid hít (tránh nấm miệng)
            - Vệ sinh dụng cụ hít thường xuyên
            - Kiểm tra còn thuốc (đếm số lần dùng)
            - Mang thuốc cắt cơn bên người

            **4. Khi nào dùng:**
            - **Thuốc cắt cơn:** Khi có triệu chứng (khó thở, ho)
            - **Thuốc dự phòng:** Hàng ngày, đúng giờ

            ## 🚨 PHÒNG NGỪA ĐỢT CẤP:

            **Đợt cấp COPD:** Triệu chứng nặng lên đột ngột (khó thở tăng, ho nhiều, đờm vàng/xanh)

            **1. Bỏ thuốc lá:**
            - Quan trọng nhất!
            - Hút thuốc → Tăng nguy cơ đợt cấp

            **2. Tránh yếu tố kích thích:**
            - **Không khí lạnh:** Đeo khẩu trang, quàng khăn
            - **Khói, bụi:** Tránh nơi có khói, bụi
            - **Thời tiết xấu:** Ở trong nhà khi ô nhiễm cao
            - **Nhiễm trùng:** Tránh người ốm, rửa tay thường xuyên

            **3. Tiêm chủng:**
            - Vắc xin cúm hàng năm (quan trọng!)
            - Vắc xin phế cầu

            **4. Uống thuốc đúng giờ:**
            - Thuốc dự phòng giúp giảm đợt cấp
            - Không tự ý ngừng

            **5. Tập thể dục:**
            - Tăng sức khỏe phổi
            - Giảm nguy cơ đợt cấp

            **6. Theo dõi triệu chứng:**
            - Nhận biết sớm dấu hiệu đợt cấp
            - Điều trị sớm

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Khó thở nặng:**
            - Khó thở khi nghỉ
            - Không nói được câu dài
            - Phải ngồi, không nằm được

            **2. Triệu chứng đợt cấp:**
            - Ho nhiều hơn bình thường
            - Đờm vàng/xanh, đặc
            - Đờm có máu
            - Sốt

            **3. Triệu chứng khác:**
            - Môi, móng tay tím
            - Lú lẫn, buồn ngủ
            - Tim đập nhanh
            - Không đáp ứng với thuốc cắt cơn

            **4. Dấu hiệu suy hô hấp:**
            - Thở nhanh (> 25 lần/phút)
            - Không thể hoạt động bình thường
            - Mệt mỏi cực độ

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Bỏ thuốc lá:**
            - **QUAN TRỌNG NHẤT!**
            - Bỏ thuốc → Làm chậm tiến triển bệnh
            - Không bao giờ quá muộn
            - Tìm hỗ trợ: Bác sĩ, nhóm bỏ thuốc, thuốc hỗ trợ

            **2. Tránh khói, bụi:**
            - Ở trong nhà khi ô nhiễm cao
            - Đeo khẩu trang khi ra ngoài
            - Dùng máy lọc không khí trong nhà
            - Tránh nơi có khói thuốc

            **3. Giữ ấm:**
            - Mặc ấm khi trời lạnh
            - Đeo khẩu trang, quàng khăn (làm ấm không khí)
            - Tránh thay đổi nhiệt độ đột ngột

            **4. Tiết kiệm năng lượng:**
            - Làm việc từ từ, nghỉ giữa chừng
            - Ngồi khi làm việc (nấu ăn, tắm)
            - Dùng dụng cụ hỗ trợ nếu cần
            - Sắp xếp công việc hợp lý

            **5. Ngủ đủ giấc:**
            - Ngủ 7-8 giờ/đêm
            - Kê gối cao (giảm khó thở)
            - Điều trị ngưng thở khi ngủ nếu có

            **6. Quản lý stress:**
            - Stress làm khó thở nặng hơn
            - Tập thư giãn: Hít thở sâu, thiền
            - Tránh căng thẳng

            **7. Khi ốm:**
            - Nghỉ ngơi nhiều
            - Uống đủ nước
            - Dùng thuốc cắt cơn nhiều hơn (nếu cần)
            - Gọi bác sĩ nếu: Sốt, đờm vàng/xanh, khó thở tăng

            **8. Hỗ trợ:**
            - Nói với gia đình về bệnh
            - Tham gia nhóm hỗ trợ COPD (nếu có)
            - Hỏi bác sĩ khi không rõ

            **9. Sống tích cực:**
            - COPD có thể kiểm soát được
            - Tuân thủ điều trị → Sống khỏe mạnh
            - Đừng để bệnh chi phối cuộc sống
                """,
                related_disease="copd",
                related_drugs=["Salbutamol", "Tiotropium", "Budesonide"],
                printable=True
        ),

        PatientEducationTopic(
            id="asthma_basics",
            title="Understanding Asthma",
            title_vn="Hiểu về Hen phế quản",
            category="Disease",
            content="""
    # Hiểu về Hen phế quản

    ## Hen phế quản là gì?

    Hen phế quản (Asthma) là bệnh mạn tính gây viêm và hẹp đường thở, dẫn đến khó thở. Đường thở bị sưng, tiết nhiều dịch nhầy, và co thắt cơ trơn phế quản.

    **⚠️ Đặc điểm:**
    - Bệnh mạn tính, không chữa khỏi hoàn toàn
    - Có thể kiểm soát tốt bằng thuốc và lối sống
    - Triệu chứng có thể thay đổi theo thời gian
    - Có thể có cơn hen (triệu chứng nặng lên đột ngột)

    ## Nguyên nhân và cơ chế:

    **Nguyên nhân:**
    - **Di truyền:** Có người thân bị hen, dị ứng
    - **Dị ứng:** Cơ địa dị ứng (atopy)
    - **Tiếp xúc sớm:** Khói thuốc, ô nhiễm khi nhỏ

    **Cơ chế:**
    - Đường thở nhạy cảm quá mức
    - Khi gặp yếu tố kích thích → Viêm, co thắt → Khó thở

    ## Triệu chứng:

    **Triệu chứng điển hình:**
    - **Thở khò khè:** Tiếng rít khi thở ra (đặc trưng)
    - **Ho:** Đặc biệt ban đêm, sáng sớm, khi gắng sức
    - **Khó thở:** Cảm giác thiếu không khí, thở nhanh, nông
    - **Tức ngực:** Cảm giác bó chặt, nặng ngực
    - **Cơn hen:** Triệu chứng nặng lên đột ngột

    **Triệu chứng khác:**
    - Mệt mỏi (do khó thở)
    - Khó ngủ (do ho, khó thở về đêm)
    - Giảm khả năng hoạt động

    **⚠️ Mức độ nặng:**
    - **Nhẹ:** Triệu chứng < 2 lần/tuần
    - **Trung bình:** Triệu chứng hàng ngày
    - **Nặng:** Triệu chứng liên tục, hạn chế hoạt động

    ## Yếu tố kích thích (Trigger):

    **1. Dị ứng:**
    - **Phấn hoa:** Mùa xuân, mùa thu
    - **Bụi:** Bụi nhà, mạt bụi
    - **Lông thú:** Chó, mèo, chim
    - **Nấm mốc:** Nơi ẩm ướt
    - **Gián:** Phân, nước bọt gián

    **2. Nhiễm trùng:**
    - Cảm lạnh, cúm
    - Viêm phế quản
    - Viêm xoang

    **3. Môi trường:**
    - **Khói thuốc:** Hút thuốc, khói thuốc thụ động
    - **Ô nhiễm không khí:** Khói bụi, PM2.5
    - **Không khí lạnh:** Thời tiết lạnh, điều hòa
    - **Thay đổi thời tiết:** Nóng lạnh đột ngột

    **4. Hoạt động:**
    - **Tập thể dục:** Hen do gắng sức (EIA)
    - **Gắng sức:** Chạy, leo cầu thang

    **5. Yếu tố khác:**
    - **Stress, cảm xúc:** Lo âu, cười to, khóc
    - **Thuốc:** Aspirin, NSAID (một số người)
    - **Thức ăn:** Sulfite (rượu vang, trái cây khô), một số người dị ứng thực phẩm
    - **Trào ngược dạ dày (GERD):** Axit kích thích đường thở

    ## Điều trị:

    **1. Thuốc cắt cơn (Reliever):**
    - **Khi nào dùng:** Khi có triệu chứng (khó thở, ho, thở khò khè)
    - **Thuốc:** Salbutamol, Terbutaline
    - **Tác dụng:** Giãn phế quản nhanh (5-15 phút)
    - **⚠️ QUAN TRỌNG:** Mang bên người mọi lúc!

    **2. Thuốc dự phòng (Controller):**
    - **Khi nào dùng:** Hàng ngày, đúng giờ (ngay cả khi không có triệu chứng)
    - **Thuốc:**
      - **Corticosteroid hít:** Budesonide, Fluticasone (giảm viêm)
      - **Thuốc giãn phế quản tác dụng dài:** Salmeterol, Formoterol
      - **Thuốc uống:** Montelukast (kháng leukotriene)
    - **Tác dụng:** Giảm viêm, phòng ngừa cơn hen
    - **⚠️ QUAN TRỌNG:** Không tự ý ngừng!

    **3. Dùng thuốc hít đúng cách:**
    - Xem hướng dẫn chi tiết bên dưới
    - Dùng sai → Thuốc không vào phổi → Không hiệu quả

    **4. Kế hoạch hành động (Action Plan):**
    - Bác sĩ sẽ hướng dẫn kế hoạch cụ thể
    - Biết khi nào dùng thuốc cắt cơn
    - Biết khi nào cần đến bệnh viện

    ## 💨 DÙNG THUỐC HÍT ĐÚNG CÁCH:

            **⚠️ QUAN TRỌNG:** Dùng sai → Thuốc không vào phổi → Không hiệu quả!

            **1. Bình xịt định liều (MDI):**

            **Kỹ thuật:**
            1. Lắc bình xịt 5-10 lần
            2. Tháo nắp
            3. Thở ra hết (không thở vào bình)
            4. Đưa bình vào miệng, ngậm chặt
            5. Bắt đầu hít vào chậm, sâu
            6. Đồng thời bấm bình xịt
            7. Tiếp tục hít sâu, chậm (3-5 giây)
            8. Giữ hơi 10 giây (nếu được)
            9. Thở ra chậm bằng miệng
            10. Nghỉ 30-60 giây trước lần xịt tiếp (nếu cần)

            **Lưu ý:**
            - Dùng buồng đệm (spacer) nếu có → Dễ dùng hơn, hiệu quả hơn
            - Rửa miệng sau dùng corticosteroid hít (tránh nấm miệng)

            **2. Bột khô (DPI):**

            **Kỹ thuật:**
            1. Nạp liều thuốc (theo hướng dẫn)
            2. Thở ra hết (không thở vào dụng cụ)
            3. Ngậm ống hít, hít mạnh, sâu, nhanh
            4. Giữ hơi 10 giây
            5. Thở ra chậm

            **Lưu ý:**
            - Không thở ra vào dụng cụ (làm ướt bột)
            - Hít mạnh, nhanh (khác với MDI)

            **3. Phun sương (Nebulizer):**

            **Kỹ thuật:**
            1. Đổ thuốc vào cốc
            2. Bật máy
            3. Đeo mặt nạ hoặc ngậm ống ngậm
            4. Hít thở bình thường, sâu (10-15 phút)
            5. Cho đến khi hết thuốc

            **4. Lưu ý chung:**
            - Đọc kỹ hướng dẫn sử dụng
            - Kiểm tra còn thuốc (đếm số lần dùng)
            - Vệ sinh dụng cụ thường xuyên
            - Bảo quản đúng cách (tránh ẩm, nắng)
            - Rửa miệng sau dùng corticosteroid hít

            **5. Khi nào dùng:**
            - **Thuốc cắt cơn:** Khi có triệu chứng, trước tập thể dục (nếu cần)
            - **Thuốc dự phòng:** Hàng ngày, đúng giờ

    ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Nguyên tắc:**
            - Ăn đủ chất, cân bằng
            - Tránh thực phẩm gây dị ứng (nếu có)
            - Tránh thực phẩm có sulfite (nếu nhạy cảm)

            **2. Thực phẩm nên ăn:**
            - **Rau xanh:** Nhiều (chống viêm)
            - **Trái cây:** Cam, bưởi, táo (vitamin C, chống oxy hóa)
            - **Cá béo:** Cá hồi, cá thu (omega-3, chống viêm)
            - **Ngũ cốc nguyên hạt:** Gạo lứt, yến mạch
            - **Protein nạc:** Thịt gà, đậu

            **3. Thực phẩm cần tránh (nếu dị ứng/nhạy cảm):**
            - **Sulfite:** Rượu vang, trái cây khô, đồ chế biến
            - **Thực phẩm gây dị ứng:** Tùy từng người (sữa, trứng, đậu phộng, hải sản)
            - **Đồ lạnh:** Có thể kích thích ho
            - **Đồ chiên, nhiều dầu mỡ:** Khó tiêu, có thể làm nặng triệu chứng

            **4. Lưu ý:**
            - Ăn chậm, nhai kỹ (tránh nuốt không khí)
            - Tránh ăn quá no (gây khó thở)
            - Uống đủ nước (giúp loãng đờm)

    ## 🏃 TẬP THỂ DỤC:

            **⚠️ QUAN TRỌNG:** Tập thể dục tốt cho hen, nhưng cần chuẩn bị!

            **1. Hen do gắng sức (EIA):**
            - Một số người hen có triệu chứng khi tập thể dục
            - Không có nghĩa là không được tập
            - Cần chuẩn bị và quản lý đúng cách

            **2. Chuẩn bị trước tập:**
            - **Khởi động:** 10-15 phút (làm ấm cơ thể)
            - **Dùng thuốc cắt cơn:** 15-30 phút trước tập (nếu bác sĩ chỉ định)
            - **Kiểm tra triệu chứng:** Nếu có triệu chứng → Không tập

            **3. Loại bài tập phù hợp:**
            - **Đi bộ:** Dễ nhất, ít gây hen
            - **Bơi lội:** Tốt (không khí ấm, ẩm)
            - **Đạp xe:** Vừa phải
            - **Yoga, thái cực quyền:** Nhẹ nhàng, thư giãn
            - **Tránh:** Chạy nhanh, tập nặng đột ngột

            **4. Khi tập:**
            - Tập vừa sức
            - Nghỉ khi mệt
            - Dừng ngay nếu: Khó thở, ho, thở khò khè
            - Dùng thuốc cắt cơn nếu cần

            **5. Sau tập:**
            - Giãn cơ 10-15 phút
            - Theo dõi triệu chứng
            - Dùng thuốc cắt cơn nếu có triệu chứng

            **6. Lợi ích:**
            - Tăng sức khỏe phổi
            - Giảm triệu chứng
            - Tăng khả năng hoạt động
            - Giảm cần dùng thuốc cắt cơn

    ## 🛡️ TRÁNH YẾU TỐ KÍCH THÍCH:

            **1. Dị ứng:**
            - **Bụi nhà, mạt bụi:**
              - Dọn dẹp thường xuyên
              - Dùng máy hút bụi có HEPA filter
              - Giặt ga gối thường xuyên (nước nóng > 60°C)
              - Dùng bao gối, chăn chống mạt bụi
              - Tránh thảm, rèm cửa (nếu có thể)
            - **Lông thú:**
              - Không nuôi thú trong nhà (tốt nhất)
              - Nếu nuôi: Không cho vào phòng ngủ, tắm thú thường xuyên
            - **Phấn hoa:**
              - Ở trong nhà khi phấn hoa nhiều
              - Đóng cửa sổ
              - Đeo khẩu trang khi ra ngoài
              - Tắm, thay quần áo sau khi ra ngoài
            - **Nấm mốc:**
              - Giữ nhà khô ráo
              - Sửa chỗ rò rỉ nước
              - Dùng máy hút ẩm
              - Lau sạch nấm mốc

            **2. Nhiễm trùng:**
            - Rửa tay thường xuyên
            - Tránh người ốm
            - Tiêm vắc xin cúm hàng năm
            - Điều trị viêm xoang, cảm lạnh sớm

            **3. Môi trường:**
            - **Không hút thuốc:** Bỏ thuốc, tránh khói thuốc
            - **Ô nhiễm không khí:**
              - Ở trong nhà khi ô nhiễm cao
              - Đeo khẩu trang khi ra ngoài
              - Dùng máy lọc không khí trong nhà
            - **Không khí lạnh:**
              - Đeo khẩu trang, quàng khăn (làm ấm không khí)
              - Tránh tập thể dục ngoài trời khi lạnh
              - Tập trong nhà khi trời lạnh

            **4. Stress:**
            - Tập thư giãn: Hít thở sâu, thiền, yoga
            - Ngủ đủ giấc
            - Tránh căng thẳng

    ## 📊 THEO DÕI VÀ QUẢN LÝ:

            **1. Peak Flow Meter (Đo lưu lượng đỉnh):**
            - Dụng cụ đo chức năng phổi tại nhà
            - Đo hàng ngày, ghi nhật ký
            - Giúp phát hiện sớm cơn hen
            - **Cách dùng:**
              1. Đứng thẳng
              2. Hít vào sâu
              3. Ngậm ống, thổi mạnh, nhanh
              4. Ghi số đo
              5. Làm 3 lần, lấy số cao nhất

            **2. Phân vùng (Zone System):**
            - **Vùng xanh (80-100%):** Ổn định, tiếp tục điều trị
            - **Vùng vàng (50-80%):** Cảnh báo, tăng thuốc dự phòng
            - **Vùng đỏ (< 50%):** Nguy hiểm, dùng thuốc cắt cơn, gọi bác sĩ

            **3. Nhật ký hen:**
            - Ghi: Triệu chứng, thuốc đã dùng, yếu tố kích thích
            - Giúp bác sĩ điều chỉnh điều trị tốt hơn

            **4. Khám định kỳ:**
            - **Mỗi 1-3 tháng:** Đánh giá điều trị, điều chỉnh thuốc
            - **Mỗi 6 tháng - 1 năm:** Đo chức năng phổi (spirometry)

            **5. Đánh giá kiểm soát:**
            - **Kiểm soát tốt:**
              - Triệu chứng < 2 lần/tuần
              - Không thức giấc vì hen
              - Không cần thuốc cắt cơn
              - Hoạt động bình thường
            - **Chưa kiểm soát tốt:** Cần điều chỉnh điều trị

    ## 🚨 KẾ HOẠCH HÀNH ĐỘNG KHI LÊN CƠN:

            **⚠️ QUAN TRỌNG:** Mỗi người cần có kế hoạch hành động riêng với bác sĩ!

            **1. Vùng xanh (Ổn định):**
            - Tiếp tục thuốc dự phòng hàng ngày
            - Tránh yếu tố kích thích
            - Tập thể dục bình thường

            **2. Vùng vàng (Cảnh báo):**
            - **Triệu chứng:** Ho, thở khò khè, khó thở nhẹ
            - **Hành động:**
              1. Dùng thuốc cắt cơn (1-2 lần xịt)
              2. Đợi 15-20 phút
              3. Nếu cải thiện → Tiếp tục theo dõi
              4. Nếu không cải thiện → Dùng thêm thuốc cắt cơn, gọi bác sĩ
              5. Có thể tăng thuốc dự phòng (theo chỉ định bác sĩ)

            **3. Vùng đỏ (Nguy hiểm):**
            - **Triệu chứng:** Khó thở nặng, không nói được câu dài, môi tím
            - **Hành động:**
              1. Dùng thuốc cắt cơn ngay (2-4 lần xịt)
              2. Đợi 15-20 phút
              3. Nếu không cải thiện → Dùng lại, gọi cấp cứu ngay
              4. Đến bệnh viện ngay

            **4. Dấu hiệu cần cấp cứu:**
            - Khó thở nặng, không nói được
            - Môi, móng tay tím
            - Thuốc cắt cơn không hiệu quả
            - Tim đập nhanh, loạn nhịp
            - Lú lẫn, buồn ngủ
            - **→ Gọi cấp cứu ngay (115), đến bệnh viện ngay!**

    ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Luôn mang thuốc cắt cơn:**
            - Mang bên người mọi lúc
            - Để ở nhà, nơi làm việc, trong xe
            - Kiểm tra còn thuốc, hạn sử dụng

            **2. Nhận biết sớm triệu chứng:**
            - Ho, thở khò khè nhẹ
            - Khó thở khi gắng sức
            - Tức ngực
            - **→ Dùng thuốc cắt cơn sớm, tránh cơn nặng**

            **3. Tránh yếu tố kích thích:**
            - Biết yếu tố kích thích của mình
            - Tránh tối đa
            - Chuẩn bị trước (ví dụ: Dùng thuốc trước tập thể dục)

            **4. Uống thuốc dự phòng đúng giờ:**
            - Không tự ý ngừng
            - Ngay cả khi không có triệu chứng
            - Giúp kiểm soát hen tốt hơn

            **5. Khi ốm:**
            - Cảm lạnh, cúm có thể làm hen nặng hơn
            - Dùng thuốc cắt cơn nhiều hơn nếu cần
            - Gọi bác sĩ nếu: Triệu chứng nặng, không cải thiện

            **6. Khi mang thai:**
            - Hen không kiểm soát → Nguy hiểm cho mẹ và con
            - Tiếp tục dùng thuốc (hỏi bác sĩ loại an toàn)
            - Khám thường xuyên hơn

            **7. Ở trẻ em:**
            - Dùng thuốc hít với buồng đệm
            - Giáo dục trẻ về bệnh (tùy độ tuổi)
            - Thông báo cho giáo viên, nhà trường
            - Có kế hoạch hành động ở trường

            **8. Sống tích cực:**
            - Hen có thể kiểm soát được
            - Tuân thủ điều trị → Sống bình thường
            - Không để hen hạn chế cuộc sống
            - Tập thể dục, hoạt động bình thường (với chuẩn bị)
            """,
            related_disease="asthma",
            related_drugs=["Salbutamol", "Budesonide", "Montelukast"],
            printable=True
        ),

        PatientEducationTopic(
            id="sinusitis_basics",
            title="Understanding Sinusitis",
            title_vn="Hiểu về Viêm xoang",
            category="Disease",
            content="""
            # Hiểu về Viêm xoang

            ## Viêm xoang là gì?

            Viêm xoang là tình trạng viêm các xoang (khoang rỗng trong xương mặt), thường do nhiễm trùng, dị ứng hoặc các yếu tố khác.

            **⚠️ Đặc điểm:**
            - Rất phổ biến ở Việt Nam (khí hậu nóng ẩm)
            - Có thể cấp tính (< 4 tuần) hoặc mạn tính (> 12 tuần)
            - Có thể tái phát

            **Vị trí xoang:**
            - Xoang hàm (2 bên má)
            - Xoang trán (trán)
            - Xoang sàng (giữa 2 mắt)
            - Xoang bướm (sau mũi)

            ## Triệu chứng:

            **Triệu chứng điển hình:**
            - **Nghẹt mũi:** Một hoặc cả hai bên
            - **Chảy nước mũi:**
              - Dịch vàng/xanh (nhiễm trùng)
              - Dịch trong (dị ứng)
              - Chảy xuống họng (chảy mũi sau)
            - **Đau mặt:**
              - Đau vùng má (xoang hàm)
              - Đau trán (xoang trán)
              - Đau giữa 2 mắt (xoang sàng)
              - Đau tăng khi cúi đầu
            - **Đau đầu:** Có thể có
            - **Giảm khứu giác:** Không ngửi được mùi
            - **Ho:** Do chảy mũi sau

            **Triệu chứng khác:**
            - Sốt (nếu nhiễm trùng)
            - Mệt mỏi
            - Hơi thở hôi
            - Đau răng (xoang hàm)

            **⚠️ Phân loại:**
            - **Viêm xoang cấp:** < 4 tuần, thường do nhiễm trùng
            - **Viêm xoang mạn:** > 12 tuần, tái phát nhiều lần

            ## Nguyên nhân:

            **1. Nhiễm trùng:**
            - **Virus:** Cảm lạnh, cúm → Viêm xoang cấp
            - **Vi khuẩn:** Nhiễm trùng thứ phát
            - **Nấm:** (Hiếm)

            **2. Dị ứng:**
            - Phấn hoa, bụi, lông thú
            - Gây viêm xoang mạn

            **3. Yếu tố khác:**
            - **Polyp mũi:** Khối u lành tính trong mũi
            - **Lệch vách ngăn mũi:** Bẩm sinh hoặc chấn thương
            - **Khí hậu:** Nóng ẩm, thay đổi thời tiết
            - **Hút thuốc lá:** Kích thích niêm mạc
            - **Bơi lội:** Nước vào xoang

            ## Chẩn đoán:

            **1. Khám lâm sàng:**
            - Khám mũi, họng
            - Ấn vùng xoang (đau)
            - Đánh giá triệu chứng

            **2. Nội soi mũi:**
            - Xem niêm mạc mũi, xoang
            - Phát hiện polyp, dịch

            **3. Chụp CT xoang:**
            - Xem rõ xoang
            - Phát hiện tổn thương
            - Thường chỉ làm khi mạn tính hoặc có biến chứng

            **4. Xét nghiệm:**
            - Cấy dịch mũi (nếu nhiễm trùng)
            - Test dị ứng (nếu nghi ngờ dị ứng)

            ## Điều trị:

            **1. Điều trị viêm xoang cấp:**
            - **Rửa mũi:** Nước muối sinh lý
              - Rửa 2-3 lần/ngày
              - Giúp làm sạch dịch, giảm nghẹt
            - **Thuốc thông mũi:** Xylometazoline, Oxymetazoline
              - Dùng ngắn hạn (3-5 ngày)
              - Không dùng lâu → Phản ứng dội
            - **Kháng sinh:** Nếu nhiễm trùng do vi khuẩn
              - Amoxicillin, Amoxicillin-Clavulanate
              - Uống đủ ngày (7-10 ngày)
            - **Corticosteroid xịt mũi:** Giảm viêm
            - **Hạ sốt, giảm đau:** Paracetamol, Ibuprofen

            **2. Điều trị viêm xoang mạn:**
            - **Rửa mũi:** Hàng ngày
            - **Corticosteroid xịt mũi:** Lâu dài
            - **Kháng sinh:** Khi có đợt cấp
            - **Điều trị dị ứng:** Nếu có
            - **Phẫu thuật:** Nếu không đáp ứng thuốc

            **3. Điều trị hỗ trợ:**
            - Xông hơi (nước nóng)
            - Chườm ấm vùng xoang
            - Nghỉ ngơi

            ## 🍽️ CHẾ ĐỘ ĂN CHO NGƯỜI VIÊM XOANG:

            **1. Nguyên tắc:**
            - **Tăng cường miễn dịch:** Giúp chống lại nhiễm trùng
            - **Chống viêm:** Thực phẩm chống viêm
            - **Tránh thực phẩm gây dị ứng:** Nếu có dị ứng

            **2. Thực phẩm NÊN ĂN:**
            - **Rau xanh:** Nhiều (rau cải, rau muống, bông cải)
              - Vitamin, chất chống oxy hóa
            - **Trái cây:** Cam, bưởi, ổi (vitamin C)
              - Tăng cường miễn dịch
            - **Tỏi, gừng:** Chống viêm, kháng khuẩn
            - **Cá béo:** Cá hồi, cá thu (omega-3, chống viêm)
            - **Nước ấm:** Uống nhiều (giúp loãng dịch)
            - **Súp, canh nóng:** Giúp thông mũi

            **3. Thực phẩm CẦN TRÁNH:**
            - **Sữa, sản phẩm sữa:** Một số người nhạy cảm (tăng dịch nhầy)
            - **Đồ lạnh:** Nước đá, kem (kích thích xoang)
            - **Đồ cay:** Ớt, tiêu (có thể kích thích)
            - **Rượu bia:** Làm khô niêm mạc
            - **Thực phẩm gây dị ứng:** Nếu có dị ứng (tùy từng người)

            **4. Thực đơn mẫu (1 ngày):**
            - **Sáng:** Cháo gà nóng + nước chanh ấm
            - **Trưa:** 1 chén cơm + cá hấp + rau luộc + canh nóng
            - **Tối:** 1 chén cơm + thịt gà luộc + rau xào + canh nóng
            - **Uống:** Nước ấm, trà gừng, súp nóng

            **5. Lưu ý:**
            - Uống nhiều nước ấm (giúp loãng dịch)
            - Ăn thức ăn nóng (giúp thông mũi)
            - Tránh đồ lạnh
            - Thử kiêng sữa xem có cải thiện không

            ## 💊 QUẢN LÝ THUỐC:

            **1. Rửa mũi:**
            - **Nước muối sinh lý:** Rửa 2-3 lần/ngày
            - **Cách rửa:**
              1. Nghiêng đầu sang một bên
              2. Đổ nước muối vào lỗ mũi trên
              3. Nước chảy ra lỗ mũi dưới
              4. Làm ngược lại bên kia
            - **Lợi ích:** Làm sạch dịch, giảm nghẹt

            **2. Thuốc thông mũi:**
            - **Xylometazoline, Oxymetazoline:** Xịt mũi
            - **Dùng ngắn hạn:** 3-5 ngày
            - **⚠️ KHÔNG dùng lâu:** > 7 ngày → Phản ứng dội (nghẹt nặng hơn)

            **3. Corticosteroid xịt mũi:**
            - **Budesonide, Fluticasone:** Xịt mũi
            - **Dùng lâu dài:** Nếu viêm xoang mạn
            - **An toàn:** Ít tác dụng phụ toàn thân

            **4. Kháng sinh:**
            - Chỉ dùng khi nhiễm trùng do vi khuẩn
            - Uống đủ ngày (7-10 ngày)
            - Không tự ý ngừng

            ## 🛡️ PHÒNG NGỪA:

            **1. Vệ sinh mũi:**
            - Rửa mũi bằng nước muối hàng ngày
            - Đặc biệt khi có cảm lạnh, cúm

            **2. Tránh dị ứng:**
            - Tránh phấn hoa, bụi, lông thú (nếu dị ứng)
            - Đeo khẩu trang khi cần
            - Vệ sinh môi trường

            **3. Lối sống:**
            - **Bỏ thuốc lá:** Kích thích niêm mạc
            - **Tránh khói, bụi:** Ô nhiễm không khí
            - **Giữ ấm:** Khi trời lạnh
            - **Tránh thay đổi nhiệt độ đột ngột**

            **4. Điều trị cảm lạnh, cúm sớm:**
            - Cảm lạnh, cúm → Viêm xoang
            - Điều trị sớm → Giảm nguy cơ viêm xoang

            **5. Tăng cường miễn dịch:**
            - Ăn đủ chất
            - Ngủ đủ giấc
            - Tập thể dục đều đặn

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Triệu chứng nặng:**
            - Sốt cao > 39°C
            - Đau đầu dữ dội
            - Sưng mặt, mắt

            **2. Biến chứng:**
            - **Viêm màng não:** Đau đầu dữ dội, cứng cổ, sốt cao
            - **Viêm ổ mắt:** Sưng mắt, đau mắt, nhìn mờ
            - **Áp xe:** Sưng, đau, sốt

            **3. Không cải thiện:**
            - Điều trị 7-10 ngày không đỡ
            - Triệu chứng nặng hơn

            **4. Viêm xoang mạn:**
            - Tái phát nhiều lần
            - Không đáp ứng với thuốc
            - Cần đánh giá phẫu thuật

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Khi bị viêm xoang:**
            - Rửa mũi thường xuyên
            - Uống nhiều nước ấm
            - Dùng thuốc đúng cách
            - Nghỉ ngơi

            **2. Phòng ngừa:**
            - Rửa mũi hàng ngày
            - Tránh dị ứng
            - Điều trị cảm lạnh, cúm sớm
            - Bỏ thuốc lá

            **3. Không tự ý:**
            - Dùng thuốc thông mũi lâu dài (phản ứng dội)
            - Dùng kháng sinh không cần thiết

            **4. Sống tích cực:**
            - Viêm xoang có thể kiểm soát được
            - Tuân thủ điều trị → Cải thiện
            """,
            related_disease="sinusitis",
            related_drugs=["Amoxicillin", "Budesonide", "Xylometazoline"],
            printable=True
        ),

        PatientEducationTopic(
            id="bronchitis_basics",
            title="Understanding Bronchitis",
            title_vn="Hiểu về Viêm phế quản",
            category="Disease",
            content="""
            # Hiểu về Viêm phế quản

            ## Viêm phế quản là gì?

            Viêm phế quản là tình trạng viêm đường thở (phế quản), gây ho, khạc đờm. Có thể cấp tính (ngắn hạn) hoặc mạn tính (dài hạn).

            **⚠️ Đặc điểm:**
            - Rất phổ biến, đặc biệt mùa lạnh
            - Viêm phế quản cấp thường tự khỏi
            - Viêm phế quản mạn cần điều trị lâu dài

            **Phân loại:**
            - **Viêm phế quản cấp:** < 3 tuần, thường do nhiễm trùng
            - **Viêm phế quản mạn:** Ho, khạc đờm > 3 tháng/năm, > 2 năm liên tiếp

            ## Triệu chứng:

            **Viêm phế quản cấp:**
            - **Ho:** Ho khan hoặc có đờm
            - **Khạc đờm:** Đờm trong, vàng, xanh
            - **Sốt:** Có thể có (nếu nhiễm trùng)
            - **Mệt mỏi:** Uể oải
            - **Đau ngực:** Khi ho nhiều
            - **Nghẹt mũi, chảy nước mũi:** Có thể có

            **Viêm phế quản mạn:**
            - **Ho mạn tính:** Ho kéo dài, đặc biệt buổi sáng
            - **Khạc đờm:** Đờm nhiều, thường xuyên
            - **Khó thở:** Khi gắng sức, tiến triển
            - **Thở khò khè:** Có thể có
            - **Mệt mỏi:** Uể oải

            **⚠️ Phân biệt với COPD:**
            - Viêm phế quản mạn là một phần của COPD
            - COPD có thêm khí phế thũng

            ## Nguyên nhân:

            **1. Viêm phế quản cấp:**
            - **Virus:** Cảm lạnh, cúm (90%)
            - **Vi khuẩn:** (10%)
            - **Kích thích:** Khói, bụi, hóa chất

            **2. Viêm phế quản mạn:**
            - **Hút thuốc lá:** Nguyên nhân chính (80-90%)
            - **Ô nhiễm không khí:** Khói, bụi
            - **Nhiễm trùng tái phát:** Làm tổn thương phế quản
            - **Yếu tố nghề nghiệp:** Bụi, hóa chất

            ## Chẩn đoán:

            **1. Khám lâm sàng:**
            - Nghe phổi (ran rít, ran ẩm)
            - Đánh giá triệu chứng

            **2. X-quang phổi:**
            - Loại trừ viêm phổi
            - Đánh giá tổn thương

            **3. Xét nghiệm:**
            - Cấy đờm (nếu nhiễm trùng)
            - Công thức máu

            **4. Đo chức năng phổi:**
            - Nếu viêm phế quản mạn
            - Đánh giá mức độ tắc nghẽn

            ## Điều trị:

            **1. Viêm phế quản cấp:**
            - **Nghỉ ngơi:** Nghỉ hoàn toàn
            - **Uống nhiều nước:** 2-3 lít/ngày
            - **Hạ sốt, giảm đau:** Paracetamol, Ibuprofen
            - **Thuốc ho:** Nếu ho nhiều, khó chịu
            - **Kháng sinh:** Chỉ khi nhiễm trùng do vi khuẩn (hiếm)
            - **⚠️ KHÔNG dùng kháng sinh cho virus!**

            **2. Viêm phế quản mạn:**
            - **Bỏ thuốc lá:** Quan trọng nhất!
            - **Thuốc giãn phế quản:** Salbutamol, Ipratropium
            - **Corticosteroid hít:** Nếu viêm nặng
            - **Kháng sinh:** Khi có đợt cấp
            - **Oxy:** Nếu thiếu oxy

            **3. Điều trị hỗ trợ:**
            - Vật lý trị liệu hô hấp
            - Tập thở
            - Tiêm vắc xin cúm, phế cầu

            ## 🍽️ CHẾ ĐỘ ĂN CHO NGƯỜI VIÊM PHẾ QUẢN:

            **1. Nguyên tắc:**
            - **Uống nhiều nước:** Quan trọng! (giúp loãng đờm)
            - **Ăn nhẹ, dễ tiêu:** Khi ốm
            - **Đủ dinh dưỡng:** Giúp cơ thể chống lại bệnh
            - **Chống viêm:** Thực phẩm chống viêm

            **2. Uống nước (QUAN TRỌNG!):**
            - **Nước lọc:** Tốt nhất
            - **Nước ấm:** Giúp loãng đờm
            - **Trà gừng ấm:** Giảm ho, ấm cổ họng
            - **Súp, canh nóng:** Vừa ăn vừa uống nước
            - **⚠️ Tránh:** Rượu bia, cà phê (làm mất nước)

            **3. Thực phẩm NÊN ĂN:**
            - **Súp, cháo:** Dễ nuốt, có nước
              - Cháo gà (tốt cho cảm cúm, viêm phế quản!)
              - Súp rau củ
            - **Rau xanh:** Nhiều (rau cải, rau muống, bông cải)
              - Vitamin, chất chống oxy hóa
            - **Trái cây:** Cam, bưởi, ổi (vitamin C)
              - Tăng cường miễn dịch
            - **Tỏi, gừng:** Chống viêm, kháng khuẩn
            - **Mật ong:** Giảm ho (nếu không có đái tháo đường)
            - **Protein:** Thịt nạc, cá (luộc, hấp)

            **4. Thực phẩm CẦN TRÁNH:**
            - **Đồ lạnh:** Nước đá, kem (làm ho nhiều hơn)
            - **Đồ chiên, nhiều dầu mỡ:** Khó tiêu
            - **Sữa, sản phẩm sữa:** Một số người nhạy cảm (tăng đờm)
            - **Rượu bia:** Làm mất nước, giảm miễn dịch
            - **Đồ ngọt nhiều:** Bánh kẹo (giảm miễn dịch)

            **5. Thực đơn mẫu (1 ngày):**
            - **Sáng:** Cháo gà nóng + nước chanh ấm
            - **Trưa:** Súp rau củ nóng + trái cây
            - **Tối:** Cháo thịt bằm nóng + nước trái cây
            - **Uống:** Nước ấm, trà gừng, súp nóng

            ## 🏃 TẬP THỂ DỤC:

            **1. Khi viêm phế quản cấp:**
            - **Nghỉ ngơi:** Không tập thể dục
            - Nghỉ hoàn toàn cho đến khi khỏi

            **2. Khi viêm phế quản mạn (ổn định):**
            - **Tập thể dục nhẹ nhàng:** Đi bộ, đạp xe
            - **Tập thở:** Thở môi mím, thở bụng
            - **Vật lý trị liệu hô hấp:** Có hướng dẫn
            - **Thời gian:** 20-30 phút/ngày
            - **Tránh:** Tập quá sức, gắng sức

            **3. Lợi ích:**
            - Tăng sức khỏe phổi
            - Giảm triệu chứng
            - Tăng khả năng hoạt động

            ## 🛡️ PHÒNG NGỪA:

            **1. Bỏ thuốc lá (QUAN TRỌNG NHẤT!):**
            - Hút thuốc → Nguyên nhân chính viêm phế quản mạn
            - Bỏ thuốc → Giảm triệu chứng, làm chậm tiến triển

            **2. Tránh kích thích:**
            - **Không hút thuốc:** Bỏ thuốc, tránh khói thuốc
            - **Tránh ô nhiễm:** Khói, bụi
            - **Đeo khẩu trang:** Khi ra ngoài, khi cần

            **3. Vệ sinh:**
            - Rửa tay thường xuyên
            - Tránh người ốm
            - Che miệng khi ho, hắt hơi

            **4. Tiêm chủng:**
            - **Vắc xin cúm:** Hàng năm
            - **Vắc xin phế cầu:** (Nếu bác sĩ chỉ định)

            **5. Điều trị cảm lạnh, cúm sớm:**
            - Cảm lạnh, cúm → Viêm phế quản
            - Điều trị sớm → Giảm nguy cơ

            **6. Tăng cường miễn dịch:**
            - Ăn đủ chất
            - Ngủ đủ giấc
            - Tập thể dục đều đặn

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Triệu chứng nặng:**
            - Sốt cao > 39°C
            - Khó thở nặng
            - Đau ngực dữ dội
            - Ho ra máu

            **2. Không cải thiện:**
            - Ho > 3 tuần không đỡ
            - Triệu chứng nặng hơn

            **3. Viêm phế quản mạn:**
            - Đợt cấp nặng
            - Khó thở tăng
            - Không đáp ứng với thuốc

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Khi bị viêm phế quản cấp:**
            - Nghỉ ngơi hoàn toàn
            - Uống nhiều nước ấm
            - Hạ sốt, giảm đau
            - Ăn nhẹ, dễ tiêu
            - Không tự ý dùng kháng sinh

            **2. Khi viêm phế quản mạn:**
            - Bỏ thuốc lá (quan trọng nhất!)
            - Uống thuốc đúng giờ
            - Tập thể dục nhẹ nhàng
            - Tránh kích thích

            **3. Phòng ngừa:**
            - Bỏ thuốc lá
            - Tránh ô nhiễm
            - Tiêm vắc xin
            - Điều trị cảm lạnh, cúm sớm

            **4. Sống tích cực:**
            - Viêm phế quản có thể kiểm soát được
            - Bỏ thuốc lá → Cải thiện đáng kể
            """,
            related_disease="bronchitis",
            related_drugs=["Salbutamol", "Amoxicillin", "Paracetamol"],
            printable=True
        ),

        PatientEducationTopic(
            id="allergic_rhinitis_basics",
            title="Understanding Allergic Rhinitis",
            title_vn="Hiểu về Viêm mũi dị ứng",
            category="Disease",
            content="""
            # Hiểu về Viêm mũi dị ứng

            ## Viêm mũi dị ứng là gì?

            Viêm mũi dị ứng là phản ứng dị ứng của niêm mạc mũi với các chất gây dị ứng (dị nguyên), gây nghẹt mũi, chảy nước mũi, hắt hơi.

            **⚠️ Đặc điểm:**
            - Rất phổ biến (20-30% dân số)
            - Có thể theo mùa hoặc quanh năm
            - Không nguy hiểm nhưng ảnh hưởng chất lượng sống
            - Có thể kiểm soát được

            **Phân loại:**
            - **Viêm mũi dị ứng theo mùa:** Phấn hoa (mùa xuân, thu)
            - **Viêm mũi dị ứng quanh năm:** Bụi, lông thú, nấm mốc

            ## Triệu chứng:

            **Triệu chứng điển hình:**
            - **Hắt hơi:** Từng tràng, nhiều lần
            - **Chảy nước mũi:** Dịch trong, nhiều
            - **Nghẹt mũi:** Một hoặc cả hai bên
            - **Ngứa mũi:** Ngứa trong mũi
            - **Ngứa mắt:** Có thể có
            - **Chảy nước mắt:** Có thể có

            **Triệu chứng khác:**
            - Đau đầu (do nghẹt mũi)
            - Giảm khứu giác
            - Ho (do chảy mũi sau)
            - Mệt mỏi (do ngủ kém)

            **⚠️ Phân biệt với cảm lạnh:**
            - **Viêm mũi dị ứng:** Dịch trong, kéo dài, không sốt
            - **Cảm lạnh:** Dịch vàng/xanh, 7-10 ngày, có thể sốt

            ## Nguyên nhân:

            **1. Dị nguyên (Chất gây dị ứng):**
            - **Phấn hoa:** Cây, cỏ, hoa (theo mùa)
            - **Bụi nhà, mạt bụi:** Quanh năm
            - **Lông thú:** Chó, mèo, chim
            - **Nấm mốc:** Nơi ẩm ướt
            - **Gián:** Phân, nước bọt gián

            **2. Yếu tố nguy cơ:**
            - **Di truyền:** Có người thân bị dị ứng
            - **Cơ địa dị ứng:** Dễ dị ứng
            - **Môi trường:** Ô nhiễm, khói thuốc
            - **Tuổi:** Trẻ em, thanh thiếu niên

            ## Chẩn đoán:

            **1. Khám lâm sàng:**
            - Đánh giá triệu chứng
            - Khám mũi (niêm mạc phù nề, nhợt)
            - Khám mắt (đỏ, sưng)

            **2. Test dị ứng:**
            - **Test da:** Chích da với dị nguyên
            - **Xét nghiệm máu:** IgE đặc hiệu
            - Xác định dị nguyên gây dị ứng

            **3. Thường không cần:**
            - Hầu hết chẩn đoán dựa vào triệu chứng

            ## Điều trị:

            **1. Tránh dị nguyên (QUAN TRỌNG NHẤT!):**
            - Xác định dị nguyên gây dị ứng
            - Tránh tối đa
            - Xem chi tiết phần phòng ngừa

            **2. Thuốc:**
            - **Corticosteroid xịt mũi:** Fluticasone, Budesonide
              - Hiệu quả nhất
              - Dùng lâu dài nếu cần
            - **Antihistamine:** Cetirizine, Loratadine
              - Giảm hắt hơi, ngứa
              - Uống khi có triệu chứng
            - **Thuốc thông mũi:** Xylometazoline (ngắn hạn)
            - **Thuốc nhỏ mắt:** Nếu ngứa mắt

            **3. Miễn dịch trị liệu:**
            - Tiêm hoặc ngậm dị nguyên
            - Giảm phản ứng dị ứng
            - Thời gian dài (3-5 năm)

            ## 🍽️ CHẾ ĐỘ ĂN CHO NGƯỜI VIÊM MŨI DỊ ỨNG:

            **1. Nguyên tắc:**
            - **Chống viêm:** Thực phẩm chống viêm
            - **Tăng cường miễn dịch:** Giúp giảm phản ứng dị ứng
            - **Tránh thực phẩm gây dị ứng:** Nếu có dị ứng thực phẩm

            **2. Thực phẩm NÊN ĂN:**
            - **Cá béo:** Cá hồi, cá thu (omega-3, chống viêm, 2-3 lần/tuần)
            - **Rau xanh:** Nhiều (rau cải, rau muống, bông cải)
              - Chất chống oxy hóa, chống viêm
            - **Trái cây:** Cam, bưởi, táo (vitamin C)
              - Tăng cường miễn dịch
            - **Tỏi, gừng:** Chống viêm
            - **Mật ong:** Có thể giúp giảm dị ứng (nếu không dị ứng mật ong)
            - **Ngũ cốc nguyên hạt:** Gạo lứt, yến mạch
            - **Các loại hạt:** Hạnh nhân, óc chó (nếu không dị ứng)

            **3. Thực phẩm CẦN TRÁNH:**
            - **Thực phẩm gây dị ứng:** Nếu có dị ứng (tùy từng người)
              - Hải sản, đậu phộng, trứng, sữa (nếu dị ứng)
            - **Thực phẩm chế biến sẵn:** Đồ hộp, thức ăn nhanh
            - **Đồ ngọt nhiều:** Bánh kẹo, nước ngọt (có thể làm nặng triệu chứng)
            - **Rượu bia:** Có thể làm nặng triệu chứng

            **4. Thực đơn mẫu (1 ngày):**
            - **Sáng:** Cháo yến mạch + sữa ít béo + trái cây
            - **Trưa:** 1 chén cơm gạo lứt + cá hồi hấp + rau luộc + canh rau
            - **Tối:** 1 chén cơm gạo lứt + thịt gà luộc + rau xào + canh
            - **Bữa phụ:** Trái cây, các loại hạt

            **5. Lưu ý:**
            - Ghi nhật ký ăn uống: Ghi thức ăn và triệu chứng
            - Xác định thức ăn gây dị ứng (nếu có)
            - Tránh thức ăn đó

            ## 🏃 TẬP THỂ DỤC:

            **1. Khi có triệu chứng:**
            - **Tránh tập ngoài trời:** Khi phấn hoa nhiều
            - **Tập trong nhà:** Nếu cần
            - **Đeo khẩu trang:** Khi tập ngoài trời

            **2. Khi không có triệu chứng:**
            - **Tập thể dục đều đặn:** 30 phút/ngày
            - **Đi bộ, bơi, đạp xe:** Tốt cho sức khỏe
            - **Yoga, thái cực quyền:** Thư giãn, giảm stress

            **3. Lợi ích:**
            - Tăng sức khỏe
            - Giảm stress (stress có thể làm nặng dị ứng)
            - Tăng miễn dịch

            ## 🛡️ PHÒNG NGỪA:

            **⚠️ QUAN TRỌNG:** Tránh dị nguyên là cách tốt nhất!

            **1. Phấn hoa (Nếu dị ứng):**
            - **Ở trong nhà:** Khi phấn hoa nhiều (sáng sớm, chiều tối)
            - **Đóng cửa sổ:** Khi phấn hoa nhiều
            - **Đeo khẩu trang:** Khi ra ngoài
            - **Tắm, thay quần áo:** Sau khi ra ngoài
            - **Kiểm tra mức độ phấn hoa:** Trước khi ra ngoài

            **2. Bụi nhà, mạt bụi:**
            - **Dọn dẹp thường xuyên:** Lau bụi, hút bụi
            - **Dùng máy hút bụi có HEPA filter**
            - **Giặt ga gối:** Thường xuyên (nước nóng > 60°C)
            - **Dùng bao gối, chăn chống mạt bụi**
            - **Tránh thảm, rèm cửa:** (Nếu có thể)
            - **Giữ độ ẩm < 50%:** Dùng máy hút ẩm

            **3. Lông thú:**
            - **Không nuôi thú trong nhà:** (Tốt nhất)
            - **Nếu nuôi:** Không cho vào phòng ngủ, tắm thú thường xuyên
            - **Rửa tay:** Sau khi chơi với thú

            **4. Nấm mốc:**
            - **Giữ nhà khô ráo:** Sửa chỗ rò rỉ nước
            - **Dùng máy hút ẩm:** Giữ độ ẩm < 50%
            - **Lau sạch nấm mốc:** Dùng dung dịch tẩy
            - **Thông thoáng:** Phòng ốc

            **5. Gián:**
            - **Vệ sinh nhà cửa:** Sạch sẽ
            - **Đậy kín thức ăn:** Không để thức ăn thừa
            - **Diệt gián:** Dùng thuốc diệt gián

            **6. Vệ sinh môi trường:**
            - Dọn dẹp nhà cửa sạch sẽ
            - Thông thoáng, có ánh sáng
            - Tránh ẩm ướt

            **7. Lối sống:**
            - **Bỏ thuốc lá:** Khói thuốc làm nặng triệu chứng
            - **Tránh khói, bụi:** Ô nhiễm không khí
            - **Quản lý stress:** Stress có thể làm nặng dị ứng

            ## 💊 QUẢN LÝ THUỐC:

            **1. Corticosteroid xịt mũi:**
            - **Hiệu quả nhất:** Giảm viêm, nghẹt mũi
            - **Dùng lâu dài:** Nếu cần (an toàn)
            - **Cách dùng:** Xịt vào mũi, hít nhẹ
            - **Rửa miệng:** Sau khi dùng (tránh nấm miệng)

            **2. Antihistamine:**
            - **Khi nào dùng:** Khi có triệu chứng
            - **Tác dụng:** Giảm hắt hơi, ngứa
            - **Tác dụng phụ:** Buồn ngủ (một số loại)

            **3. Thuốc thông mũi:**
            - **Dùng ngắn hạn:** 3-5 ngày
            - **⚠️ KHÔNG dùng lâu:** > 7 ngày → Phản ứng dội

            **4. Miễn dịch trị liệu:**
            - Tiêm hoặc ngậm dị nguyên
            - Thời gian dài (3-5 năm)
            - Hiệu quả lâu dài

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Triệu chứng nặng:**
            - Nghẹt mũi nặng, không thở được
            - Ảnh hưởng giấc ngủ, công việc
            - Không đáp ứng với thuốc

            **2. Biến chứng:**
            - **Viêm xoang:** Đau mặt, sốt
            - **Viêm tai giữa:** Đau tai
            - **Hen phế quản:** Khó thở, thở khò khè

            **3. Cần test dị ứng:**
            - Xác định dị nguyên
            - Điều trị miễn dịch

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Khi bị viêm mũi dị ứng:**
            - Tránh dị nguyên (quan trọng nhất!)
            - Dùng thuốc đúng cách
            - Rửa mũi bằng nước muối

            **2. Phòng ngừa:**
            - Xác định dị nguyên gây dị ứng
            - Tránh tối đa
            - Vệ sinh môi trường

            **3. Sống tích cực:**
            - Viêm mũi dị ứng có thể kiểm soát được
            - Tránh dị nguyên + thuốc → Sống bình thường
            - Đừng để dị ứng ảnh hưởng cuộc sống
            """,
            related_disease="allergic_rhinitis",
            related_drugs=["Fluticasone", "Cetirizine", "Loratadine"],
            printable=True
        ),

        PatientEducationTopic(
            id="laryngitis_basics",
            title="Understanding Laryngitis",
            title_vn="Hiểu về Viêm thanh quản",
            category="Disease",
            content="""
            # Hiểu về Viêm thanh quản

            ## Viêm thanh quản là gì?

            Viêm thanh quản (Laryngitis) là tình trạng viêm của thanh quản (dây thanh âm), gây khàn giọng, mất giọng. Bệnh rất phổ biến, đặc biệt khi thay đổi thời tiết, thường tự khỏi trong vài ngày đến 1 tuần.

            **⚠️ Đặc điểm:**
            - Viêm thanh quản (dây thanh âm)
            - Khàn giọng, mất giọng
            - Rất phổ biến
            - Thường tự khỏi

            **Phân loại:**
            - **Viêm thanh quản cấp:** Viêm đột ngột, < 3 tuần
            - **Viêm thanh quản mạn:** Viêm kéo dài, > 3 tuần

            **Thanh quản:**
            - Cơ quan ở cổ, chứa dây thanh âm
            - Chức năng: Phát âm, bảo vệ đường thở

            ## Triệu chứng:

            **Triệu chứng điển hình:**
            - **Khàn giọng:** Giọng khàn, yếu
            - **Mất giọng:** Mất giọng hoàn toàn (nếu nặng)
            - **Đau họng:** Đau họng, khó chịu
            - **Ho khan:** Ho khan, có thể ho nhiều
            - **Cảm giác vướng:** Cảm giác có gì đó ở cổ họng

            **Triệu chứng khác:**
            - Sốt nhẹ (nếu do nhiễm trùng)
            - Mệt mỏi
            - Khó nuốt (nếu nặng)

            **⚠️ Dấu hiệu báo động (cần khám ngay!):**
            - Khó thở (có thể tắc nghẽn đường thở)
            - Nuốt đau nặng
            - Ho ra máu
            - Khàn giọng > 3 tuần (cần loại trừ ung thư)

            ## Nguyên nhân:

            **Viêm thanh quản cấp:**
            - **Nhiễm virus:** Cảm lạnh, cúm (phổ biến nhất)
            - **Nhiễm vi khuẩn:** Hiếm
            - **Lạm dụng giọng:** Nói nhiều, hát, la hét
            - **Hút thuốc lá:** Kích thích thanh quản
            - **Rượu bia:** Kích thích thanh quản

            **Viêm thanh quản mạn:**
            - **Hút thuốc lá:** Phổ biến nhất
            - **Lạm dụng giọng:** Nói nhiều, nghề nghiệp
            - **Trào ngược dạ dày (GERD):** Axit kích thích thanh quản
            - **Dị ứng:** Dị ứng
            - **Nhiễm trùng mạn:** Nhiễm trùng mạn tính

            **Yếu tố nguy cơ:**
            - Hút thuốc lá
            - Uống rượu bia
            - Nghề nghiệp (giáo viên, ca sĩ, MC)
            - Nhiễm trùng đường hô hấp trên
            - Thay đổi thời tiết

            ## Chẩn đoán:

            **Chẩn đoán lâm sàng:**
            - Triệu chứng điển hình
            - Khám họng

            **Khám:**
            - **Soi thanh quản:** Quan sát dây thanh âm (đỏ, sưng)
            - **Khám họng:** Đỏ, sưng

            **Xét nghiệm:**
            - Thường không cần
            - Cấy dịch (nếu nghi ngờ vi khuẩn)

            **⚠️ Phân biệt:**
            - Ung thư thanh quản (nếu khàn giọng > 3 tuần)
            - Liệt dây thanh âm
            - Polyp, u dây thanh âm

            ## Điều trị:

            **Viêm thanh quản cấp:**

            **1. Điều trị hỗ trợ:**
            - **Nghỉ giọng:** Nghỉ nói, không nói (quan trọng nhất!)
            - **Uống nhiều nước:** Uống nhiều nước ấm
            - **Súc miệng:** Súc miệng bằng nước muối
            - **Xông hơi:** Xông hơi nước ấm
            - **Tránh:** Hút thuốc lá, rượu bia, đồ lạnh

            **2. Thuốc:**
            - **Giảm đau:** Paracetamol (nếu đau)
            - **Kháng sinh:** Chỉ dùng nếu do vi khuẩn (hiếm)

            **Viêm thanh quản mạn:**

            **1. Điều trị nguyên nhân:**
            - **Bỏ thuốc lá:** Bỏ thuốc lá HOÀN TOÀN
            - **Điều trị GERD:** Nếu có trào ngược
            - **Nghỉ giọng:** Nghỉ nói, giảm nói

            **2. Thuốc:**
            - **Corticosteroid:** Xịt hoặc uống (ngắn hạn)
            - **Điều trị GERD:** PPI, H2 blocker

            **3. Vật lý trị liệu:**
            - Tập luyện giọng nói
            - Kỹ thuật nói đúng

            **⚠️ Lưu ý:**
            - Viêm thanh quản cấp: Thường tự khỏi
            - Viêm thanh quản mạn: Cần điều trị nguyên nhân

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Thực phẩm nên ăn:**
            - **Thức ăn mềm, lỏng:** Cháo, súp (khi đau họng)
            - **Thức ăn ấm:** Thức ăn ấm (không nóng)
            - **Uống nhiều nước:** Nước ấm, trà ấm
            - **Mật ong:** Mật ong + chanh (giảm đau họng)

            **2. Thực phẩm nên tránh:**
            - **Đồ cay nóng:** Kích thích thanh quản
            - **Đồ lạnh:** Đồ lạnh, kem
            - **Rượu bia:** Kích thích thanh quản
            - **Caffeine:** Có thể làm khô

            **3. Thực đơn mẫu:**
            - **Sáng:** Cháo ấm + trái cây
            - **Trưa:** Súp ấm + thức ăn mềm
            - **Chiều:** Súp ấm + thức ăn mềm
            - **Uống:** Nước ấm, trà ấm

            ## 🏃 TẬP THỂ DỤC:

            **1. Khi đang viêm:**
            - Nghỉ ngơi
            - Tránh gắng sức
            - Tránh nói nhiều

            **2. Khi đã khỏi:**
            - Tập thể dục bình thường
            - Tập luyện giọng nói (nếu nghề nghiệp)

            ## 💊 QUẢN LÝ THUỐC:

            **1. Thuốc giảm đau:**
            - **Paracetamol:** 500-1000mg, 3-4 lần/ngày

            **2. Corticosteroid:**
            - **Xịt hoặc uống:** Ngắn hạn (nếu cần)
            - **Theo chỉ định bác sĩ**

            **3. Lưu ý:**
            - Không tự ý dùng kháng sinh
            - Nghỉ giọng quan trọng hơn thuốc

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Dấu hiệu báo động:**
            - Khó thở (có thể tắc nghẽn đường thở)
            - Nuốt đau nặng
            - Ho ra máu
            - **Cấp cứu ngay!**

            **2. Khàn giọng > 3 tuần:**
            - Cần khám để loại trừ ung thư
            - Soi thanh quản

            **3. Không đáp ứng điều trị:**
            - Điều trị > 1 tuần không cải thiện
            - Tái phát nhiều lần

            ## 💡 PHÒNG NGỪA:

            **1. Bỏ thuốc lá:**
            - **Bỏ thuốc lá HOÀN TOÀN** (quan trọng nhất!)
            - Giảm nguy cơ viêm thanh quản mạn

            **2. Tránh lạm dụng giọng:**
            - Nghỉ nói khi mệt
            - Không la hét, nói to
            - Uống nước khi nói nhiều

            **3. Điều trị GERD:**
            - Điều trị trào ngược dạ dày
            - Giảm kích thích thanh quản

            **4. Tránh:**
            - Rượu bia
            - Đồ lạnh
            - Môi trường khô, bụi

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Phòng ngừa:**
            - **Bỏ thuốc lá** (quan trọng nhất!)
            - Tránh lạm dụng giọng
            - Điều trị GERD

            **2. Khi bị viêm thanh quản:**
            - **Nghỉ giọng** (quan trọng nhất!)
            - Uống nhiều nước ấm
            - Tránh hút thuốc lá, rượu bia

            **3. Sống tích cực:**
            - Viêm thanh quản cấp thường tự khỏi
            - Điều trị đúng → Khỏi nhanh
            - Phòng ngừa tốt → Không tái phát
            """,
            related_disease="laryngitis",
            related_drugs=["Paracetamol", "Prednisolone"],
            printable=True
        ),

        PatientEducationTopic(
            id="lung_abscess_basics",
            title="Understanding Lung Abscess",
            title_vn="Hiểu về Áp xe phổi",
            category="Disease",
            content="""
            # Hiểu về Áp xe phổi

            ## Áp xe phổi là gì?

            Áp xe phổi (Lung Abscess) là tình trạng hình thành ổ mủ trong phổi, thường do nhiễm trùng. Áp xe phổi có thể là biến chứng của viêm phổi hoặc do nhiễm trùng trực tiếp.

            **⚠️ Đặc điểm:**
            - Ổ mủ trong phổi
            - Thường do nhiễm trùng
            - Có thể là biến chứng viêm phổi
            - Cần điều trị kháng sinh lâu dài

            **Phân loại:**
            - **Áp xe phổi nguyên phát:** Nhiễm trùng trực tiếp phổi
            - **Áp xe phổi thứ phát:** Biến chứng viêm phổi, tắc nghẽn

            ## Triệu chứng:

            **Triệu chứng điển hình:**
            - **Sốt:** Sốt cao, ớn lạnh
            - **Ho:** Ho có đờm, đờm mủ, có thể có mùi hôi
            - **Ho ra máu:** Có thể ho ra máu
            - **Đau ngực:** Đau ngực, tăng khi ho
            - **Khó thở:** Khó thở, đặc biệt khi gắng sức
            - **Mệt mỏi:** Mệt mỏi, suy nhược
            - **Sụt cân:** Sụt cân

            **Triệu chứng khác:**
            - Đổ mồ hôi đêm
            - Chán ăn
            - Hơi thở hôi

            **⚠️ Biến chứng:**
            - Vỡ vào màng phổi (tràn mủ màng phổi)
            - Nhiễm trùng huyết
            - Suy hô hấp
            - Tử vong (nếu không điều trị)

            ## Nguyên nhân:

            **1. Nhiễm trùng:**
            - **Vi khuẩn:** Staphylococcus, Klebsiella, Pseudomonas
            - **Kỵ khí:** Bacteroides, Peptostreptococcus (phổ biến)
            - **Nấm:** Aspergillus, Candida (hiếm)

            **2. Yếu tố nguy cơ:**
            - **Viêm phổi:** Biến chứng viêm phổi
            - **Hút thuốc lá:** Tăng nguy cơ
            - **Rượu bia:** Tăng nguy cơ
            - **Suy giảm miễn dịch:** HIV, thuốc ức chế miễn dịch
            - **Tắc nghẽn đường thở:** Khối u, dị vật
            - **Nằm liệt giường:** Tăng nguy cơ

            **3. Đường lây:**
            - Hít phải vi khuẩn từ miệng, họng
            - Nhiễm trùng từ nơi khác (hiếm)

            ## Chẩn đoán:

            **Chẩn đoán lâm sàng:**
            - Triệu chứng điển hình
            - Khám phổi

            **Xét nghiệm:**
            - **Xét nghiệm máu:**
              - Bạch cầu tăng
              - CRP tăng
              - Cấy máu (nếu sốt cao)
            - **Cấy đờm:** Xác định vi khuẩn
            - **Cấy dịch mủ:** Nếu có

            **Hình ảnh:**
            - **X-quang ngực:** Phát hiện ổ mủ (hình tròn, có mức nước-khí)
            - **CT ngực:** Đánh giá chính xác, kích thước, vị trí

            **⚠️ Phân biệt:**
            - Viêm phổi
            - Ung thư phổi (hoại tử)
            - Lao phổi

            ## Điều trị:

            **1. Kháng sinh:**
            - **Kháng sinh phổ rộng:** Clindamycin, Amoxicillin-Clavulanate
            - **Kháng sinh kỵ khí:** Metronidazole (nếu nghi ngờ kỵ khí)
            - **Đường tĩnh mạch:** Ban đầu (1-2 tuần)
            - **Đường uống:** Sau khi ổn định (4-8 tuần)
            - **Thời gian:** 4-8 tuần (quan trọng!)

            **2. Dẫn lưu:**
            - **Dẫn lưu qua da:** Nếu áp xe lớn, không đáp ứng kháng sinh
            - **Nội soi phế quản:** Dẫn lưu qua nội soi

            **3. Phẫu thuật:**
            - **Chỉ định:**
              - Áp xe lớn (> 6cm)
              - Không đáp ứng điều trị > 6 tuần
              - Biến chứng (vỡ, tràn mủ màng phổi)
            - **Phương pháp:** Cắt thùy phổi, cắt phân thùy

            **4. Điều trị hỗ trợ:**
            - **Vật lý trị liệu:** Vỗ rung, dẫn lưu tư thế (giúp đờm ra)
            - **Oxy:** Nếu khó thở
            - **Dinh dưỡng:** Đủ dinh dưỡng

            **⚠️ Lưu ý:**
            - Điều trị kháng sinh lâu dài (4-8 tuần)
            - Không tự ý ngừng kháng sinh
            - Theo dõi sát

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Khi đang điều trị:**
            - **Đủ dinh dưỡng:** Đủ calo, protein, vitamin
            - **Dễ tiêu:** Thức ăn mềm, dễ tiêu
            - **Uống nhiều nước:** Uống nhiều nước (giúp đờm loãng)

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
            - Vật lý trị liệu (vỗ rung, dẫn lưu tư thế)
            - Tập thở (nếu có thể)

            **2. Sau khi khỏi:**
            - Tập thể dục từ từ
            - Tăng dần cường độ

            ## 💊 QUẢN LÝ THUỐC:

            **1. Kháng sinh:**
            - **Uống đều đặn:** Theo chỉ định bác sĩ
            - **Đủ thời gian:** 4-8 tuần (quan trọng!)
            - **Không tự ý ngừng:** Nguy cơ tái phát

            **2. Thuốc giảm đau:**
            - **Paracetamol:** Nếu đau, sốt

            **3. Lưu ý:**
            - Uống đúng liều, đúng giờ
            - Báo bác sĩ nếu có tác dụng phụ
            - Xét nghiệm máu định kỳ (nếu cần)

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Triệu chứng nặng:**
            - Sốt cao, ớn lạnh
            - Khó thở nặng
            - Ho ra máu nhiều
            - **Cấp cứu ngay!**

            **2. Biến chứng:**
            - Tràn mủ màng phổi
            - Nhiễm trùng huyết
            - Suy hô hấp

            **3. Không đáp ứng điều trị:**
            - Điều trị > 6 tuần không cải thiện
            - Sốt tái phát

            ## 💡 PHÒNG NGỪA:

            **1. Điều trị viêm phổi:**
            - Điều trị viêm phổi đúng cách
            - Giảm nguy cơ biến chứng

            **2. Bỏ thuốc lá:**
            - **Bỏ thuốc lá HOÀN TOÀN**
            - Giảm nguy cơ

            **3. Vệ sinh răng miệng:**
            - Vệ sinh răng miệng sạch sẽ
            - Giảm vi khuẩn trong miệng

            **4. Tránh:**
            - Rượu bia
            - Suy giảm miễn dịch

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Phòng ngừa:**
            - Điều trị viêm phổi đúng cách
            - Bỏ thuốc lá
            - Vệ sinh răng miệng

            **2. Khi bị áp xe phổi:**
            - Điều trị kháng sinh lâu dài (4-8 tuần)
            - Tuân thủ điều trị
            - Vật lý trị liệu

            **3. Sống tích cực:**
            - Áp xe phổi có thể điều trị khỏi
            - Điều trị đúng → Khỏi
            - Phòng ngừa tốt → Không tái phát
            """,
            related_disease="lung_abscess",
            related_drugs=["Clindamycin", "Amoxicillin-Clavulanate", "Metronidazole", "Paracetamol"],
            printable=True
        ),

        PatientEducationTopic(
            id="pneumothorax_basics",
            title="Understanding Pneumothorax",
            title_vn="Hiểu về Tràn khí màng phổi",
            category="Disease",
            content="""
            # Hiểu về Tràn khí màng phổi

            ## Tràn khí màng phổi là gì?

            Tràn khí màng phổi (Pneumothorax) là tình trạng khí tích tụ trong khoang màng phổi (giữa phổi và thành ngực), gây xẹp phổi, khó thở. Đây là cấp cứu hô hấp, cần điều trị ngay.

            **⚠️ Đặc điểm:**
            - Khí tích tụ trong khoang màng phổi
            - Gây xẹp phổi
            - Cấp cứu hô hấp
            - Cần điều trị ngay

            **Phân loại:**
            - **Tràn khí màng phổi tự phát nguyên phát:** Không có bệnh nền (phổ biến ở nam trẻ, cao, gầy)
            - **Tràn khí màng phổi tự phát thứ phát:** Có bệnh nền (COPD, hen, lao)
            - **Tràn khí màng phổi do chấn thương:** Chấn thương ngực
            - **Tràn khí màng phổi áp lực:** Khí tích tụ, tăng áp lực (cấp cứu!)

            ## Triệu chứng:

            **Triệu chứng điển hình:**
            - **Đau ngực:** Đau ngực đột ngột, dữ dội, một bên, tăng khi thở, ho
            - **Khó thở:** Khó thở, tăng khi gắng sức
            - **Ho:** Ho khan
            - **Mạch nhanh:** Mạch nhanh
            - **Huyết áp tụt:** Huyết áp tụt (nếu nặng)

            **Triệu chứng khác:**
            - Da xanh, tím (nếu nặng)
            - Mệt mỏi
            - Lo âu

            **⚠️ Tràn khí màng phổi áp lực (CẤP CỨU!):**
            - Khó thở nặng
            - Tụt huyết áp
            - Mạch nhanh
            - Tím tái
            - **Cấp cứu ngay!**

            ## Nguyên nhân:

            **1. Tràn khí màng phổi tự phát nguyên phát:**
            - **Vỡ bóng khí (Bleb):** Vỡ bóng khí nhỏ trên phổi
            - **Nam trẻ, cao, gầy:** Yếu tố nguy cơ
            - **Hút thuốc lá:** Tăng nguy cơ

            **2. Tràn khí màng phổi tự phát thứ phát:**
            - **COPD:** Bệnh phổi tắc nghẽn mạn tính
            - **Hen phế quản:** Hen phế quản
            - **Lao phổi:** Lao phổi
            - **Xơ phổi:** Xơ phổi
            - **Ung thư phổi:** Ung thư phổi

            **3. Tràn khí màng phổi do chấn thương:**
            - **Chấn thương ngực:** Gãy xương sườn, đâm thủng
            - **Sau phẫu thuật:** Sau phẫu thuật ngực
            - **Thủ thuật:** Chọc dò màng phổi, đặt catheter

            **4. Yếu tố nguy cơ:**
            - Nam, trẻ (20-40 tuổi)
            - Cao, gầy
            - Hút thuốc lá
            - Có bệnh phổi

            ## Chẩn đoán:

            **Chẩn đoán lâm sàng:**
            - Triệu chứng điển hình
            - Khám phổi (giảm rì rào phế nang, gõ vang)

            **Xét nghiệm:**
            - **X-quang ngực:** Phát hiện tràn khí (phổi xẹp, không có mạch máu phổi)
            - **CT ngực:** Đánh giá chính xác, tìm nguyên nhân

            **⚠️ Phân biệt:**
            - Nhồi máu phổi
            - Viêm màng phổi
            - Đau ngực do tim

            ## Điều trị:

            **1. Tràn khí màng phổi nhỏ (< 20%):**
            - **Theo dõi:** Theo dõi, tự hấp thu
            - **Oxy:** Thở oxy (tăng tốc độ hấp thu)
            - **Nghỉ ngơi:** Nghỉ ngơi

            **2. Tràn khí màng phổi vừa-nặng (> 20%):**
            - **Chọc hút khí:** Chọc hút khí bằng kim
            - **Dẫn lưu màng phổi:** Đặt ống dẫn lưu màng phổi
            - **Theo dõi:** Theo dõi sát

            **3. Tràn khí màng phổi áp lực (CẤP CỨU!):**
            - **Chọc kim giải áp:** Chọc kim giải áp ngay
            - **Dẫn lưu màng phổi:** Đặt ống dẫn lưu
            - **Cấp cứu ngay!**

            **4. Phẫu thuật:**
            - **Chỉ định:**
              - Tái phát nhiều lần (> 2 lần)
              - Không đáp ứng dẫn lưu
              - Tràn khí màng phổi hai bên
            - **Phương pháp:**
              - Nội soi lồng ngực (VATS)
              - Cắt bóng khí, dính màng phổi

            **⚠️ Lưu ý:**
            - Tràn khí màng phổi áp lực: Cấp cứu ngay!
            - Tái phát: Cần phẫu thuật

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Khi đang điều trị:**
            - **Đủ dinh dưỡng:** Đủ calo, protein
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
            - Tập thở nhẹ (nếu có thể)

            **2. Sau khi khỏi:**
            - Tập thể dục từ từ
            - Tăng dần cường độ
            - Tránh lặn, bay (nếu có nguy cơ tái phát)

            ## 💊 QUẢN LÝ THUỐC:

            **1. Thuốc giảm đau:**
            - **Paracetamol:** Nếu đau
            - **NSAID:** Ibuprofen (nếu không chống chỉ định)

            **2. Oxy:**
            - Thở oxy (nếu khó thở)

            **3. Lưu ý:**
            - Uống đúng liều, đúng giờ
            - Báo bác sĩ nếu đau không giảm

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Tràn khí màng phổi áp lực:**
            - Khó thở nặng
            - Tụt huyết áp
            - Tím tái
            - **Cấp cứu ngay!**

            **2. Triệu chứng nặng:**
            - Đau ngực dữ dội
            - Khó thở nặng
            - **Cấp cứu ngay!**

            **3. Tái phát:**
            - Tái phát nhiều lần
            - Cần phẫu thuật

            ## 💡 PHÒNG NGỪA:

            **1. Bỏ thuốc lá:**
            - **Bỏ thuốc lá HOÀN TOÀN**
            - Giảm nguy cơ

            **2. Điều trị bệnh phổi:**
            - Điều trị COPD, hen
            - Giảm nguy cơ

            **3. Tránh:**
            - Lặn (nếu có nguy cơ tái phát)
            - Bay (nếu có nguy cơ tái phát)
            - Gắng sức quá mức

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Phòng ngừa:**
            - Bỏ thuốc lá
            - Điều trị bệnh phổi

            **2. Khi bị tràn khí màng phổi:**
            - Đến bệnh viện ngay
            - Tuân thủ điều trị
            - Nghỉ ngơi

            **3. Sống tích cực:**
            - Tràn khí màng phổi có thể điều trị khỏi
            - Điều trị đúng → Khỏi
            - Phẫu thuật → Giảm nguy cơ tái phát

            **4. Lâu dài:**
            - Nếu tái phát nhiều lần → Cần phẫu thuật
            - Tránh lặn, bay (nếu có nguy cơ)
            """,
            related_disease="pneumothorax",
            related_drugs=["Paracetamol", "Ibuprofen"],
            printable=True
        ),

]
