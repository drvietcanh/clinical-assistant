"""
Patient Education Topics - Metabolic
"""
from patient_education.models import PatientEducationTopic


METABOLIC_TOPICS = [
        PatientEducationTopic(
            id="gout_basics",
            title="Understanding Gout",
            title_vn="Hiểu về Bệnh Gout",
            category="Disease",
            content="""
            # Hiểu về Bệnh Gout

            ## Bệnh Gout là gì?

            Bệnh Gout là bệnh viêm khớp do tăng acid uric trong máu, tạo thành tinh thể urat lắng đọng ở khớp, gây viêm đau dữ dội.

            **Cơ chế:**
            - Tăng acid uric máu (do sản xuất nhiều hoặc đào thải ít)
            - Tinh thể urat lắng đọng ở khớp
            - Gây viêm, sưng, đau dữ dội

            **⚠️ Đặc điểm:**
            - Đau khớp đột ngột, dữ dội
            - Thường gặp ở nam > 40 tuổi
            - Có thể tái phát nếu không điều trị

            ## Triệu chứng:

            **Cơn Gout cấp:**
            - **Đau khớp dữ dội:** Đột ngột, thường về đêm
            - **Sưng, nóng, đỏ:** Khớp sưng to, đỏ, nóng
            - **Vị trí:** Thường khớp ngón chân cái (50%), khớp cổ chân, gối, khuỷu tay
            - **Đau tăng:** Khi chạm vào, cử động
            - **Sốt:** Có thể có sốt nhẹ
            - **Tự khỏi:** Sau 3-10 ngày (nhưng sẽ tái phát)

            **Gout mạn tính:**
            - Đau khớp tái phát nhiều lần
            - Hạt tophi (tinh thể urat dưới da): Ở vành tai, khuỷu tay, ngón tay
            - Tổn thương khớp vĩnh viễn
            - Sỏi thận (do acid uric)

            ## Nguyên nhân:

            **1. Tăng acid uric:**
            - **Sản xuất nhiều:** Do gen, bệnh máu
            - **Đào thải ít:** Do thận, thuốc

            **2. Yếu tố nguy cơ:**
            - **Nam giới:** > 40 tuổi
            - **Béo phì:** Tăng sản xuất acid uric
            - **Ăn nhiều purin:** Thịt đỏ, hải sản, nội tạng
            - **Uống nhiều rượu bia:** Đặc biệt bia
            - **Thuốc:** Lợi tiểu, Aspirin liều thấp
            - **Bệnh khác:** Đái tháo đường, tăng huyết áp, suy thận

            ## Điều trị:

            **1. Điều trị cơn Gout cấp:**
            - **Colchicine:** Thuốc đặc trị (uống sớm, trong 24 giờ đầu)
            - **NSAID:** Ibuprofen, Naproxen (giảm đau, viêm)
            - **Corticosteroid:** Nếu không dùng được NSAID
            - **Nghỉ ngơi:** Nâng cao chân, chườm lạnh

            **2. Điều trị dự phòng:**
            - **Allopurinol:** Giảm sản xuất acid uric
            - **Probenecid:** Tăng đào thải acid uric
            - **Uống lâu dài:** Để phòng ngừa cơn tái phát

            **3. Mục tiêu điều trị:**
            - Acid uric máu < 6 mg/dL (360 μmol/L)
            - Giảm cơn tái phát
            - Phòng ngừa biến chứng

            ## 🍽️ CHẾ ĐỘ ĂN CHO NGƯỜI BỊ GOUT:

            **⚠️ QUAN TRỌNG:** Chế độ ăn rất quan trọng trong điều trị Gout!

            **1. Nguyên tắc:**
            - **Giảm purin:** Thực phẩm giàu purin → Tăng acid uric
            - **Uống nhiều nước:** Giúp đào thải acid uric
            - **Giảm rượu bia:** Đặc biệt bia
            - **Giảm cân:** Nếu thừa cân

            **2. Thực phẩm CẦN TRÁNH (Giàu purin):**
            - **Nội tạng:** Gan, thận, tim, lòng (rất nhiều purin)
            - **Thịt đỏ:** Thịt bò, thịt heo, thịt dê (nhiều)
            - **Hải sản:** Tôm, cua, cá mòi, cá trích, cá cơm (nhiều)
            - **Đồ uống có cồn:** 
              - **Bia:** Rất nhiều purin (tránh hoàn toàn!)
              - Rượu (hạn chế)
            - **Nước ngọt có đường:** Fructose → Tăng acid uric
            - **Thịt chế biến sẵn:** Xúc xích, thịt nguội

            **3. Thực phẩm HẠN CHẾ (Trung bình purin):**
            - **Thịt trắng:** Thịt gà, thịt vịt (ăn ít, 100-150g/ngày)
            - **Cá:** Cá nước ngọt (ăn ít)
            - **Đậu:** Đậu phụ, đậu nành (ăn ít)
            - **Rau:** Măng tây, nấm, rau chân vịt (ăn ít)

            **4. Thực phẩm NÊN ĂN (Ít purin):**
            - **Rau xanh:** Hầu hết rau (trừ măng tây, nấm, rau chân vịt)
              - Rau cải, rau muống, bông cải, cà rốt
            - **Trái cây:** Tất cả (đặc biệt cherry - giúp giảm acid uric)
            - **Ngũ cốc:** Gạo, bánh mì, yến mạch
            - **Sữa ít béo:** Sữa tách béo, sữa chua (giúp giảm acid uric)
            - **Trứng:** 3-4 quả/tuần
            - **Dầu thực vật:** Dầu ô liu, dầu hạt cải

            **5. Uống nước:**
            - **Mục tiêu:** 2-3 lít/ngày
            - **Nước lọc:** Tốt nhất
            - **Cà phê:** Có thể uống (giúp giảm acid uric)
            - **Trà:** Có thể uống
            - **⚠️ Tránh:** Bia, rượu, nước ngọt có đường

            **6. Thực đơn mẫu (1 ngày):**
            - **Sáng:** Cháo yến mạch + trứng luộc + sữa ít béo
            - **Trưa:** 1 chén cơm + đậu phụ luộc + rau luộc + canh rau
            - **Tối:** 1 chén cơm + cá nước ngọt (ít) + rau xào + canh
            - **Bữa phụ:** Trái cây (cherry nếu có), sữa chua

            **7. Lưu ý:**
            - Ghi nhật ký ăn uống: Ghi thức ăn và cơn Gout
            - Xác định thức ăn gây cơn (mỗi người khác nhau)
            - Tránh thức ăn đó
            - Ăn đều đặn, không bỏ bữa

            ## 🏃 TẬP THỂ DỤC:

            **1. Khi có cơn Gout cấp:**
            - **Nghỉ ngơi:** Không tập thể dục
            - **Nâng cao chân:** Giảm sưng
            - **Chườm lạnh:** Giảm đau, sưng

            **2. Khi không có cơn:**
            - **Tập thể dục nhẹ nhàng:** Đi bộ, bơi, đạp xe
            - **Tránh:** Chạy, nhảy (gây áp lực khớp)
            - **Mục tiêu:** Giảm cân, tăng sức khỏe

            **3. Lưu ý:**
            - Tập vừa sức
            - Uống đủ nước
            - Nghỉ nếu đau khớp

            ## 💊 QUẢN LÝ THUỐC:

            **1. Khi có cơn cấp:**
            - **Dùng thuốc sớm:** Trong 24 giờ đầu (hiệu quả tốt nhất)
            - **Colchicine:** Uống theo chỉ định (không tự ý tăng liều)
            - **NSAID:** Uống sau ăn (tránh đau dạ dày)

            **2. Thuốc dự phòng:**
            - **Uống hàng ngày:** Đúng giờ
            - **Không tự ý ngừng:** Ngừng → Cơn tái phát
            - **Theo dõi:** Acid uric máu định kỳ

            **3. Tác dụng phụ:**
            - **Colchicine:** Tiêu chảy, buồn nôn
            - **Allopurinol:** Phát ban (báo bác sĩ ngay!)
            - **Báo bác sĩ nếu:** Tác dụng phụ nghiêm trọng

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Cơn Gout cấp:**
            - Đau dữ dội, không chịu được
            - Thuốc không hiệu quả
            - Sốt cao

            **2. Biến chứng:**
            - Hạt tophi vỡ, nhiễm trùng
            - Sỏi thận (đau lưng, tiểu máu)
            - Tổn thương khớp nặng

            **3. Tác dụng phụ thuốc:**
            - Phát ban (có thể dị ứng Allopurinol)
            - Đau dạ dày nặng

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Phòng ngừa cơn:**
            - Tránh thức ăn giàu purin
            - Không uống bia, rượu
            - Uống nhiều nước
            - Uống thuốc dự phòng đúng giờ

            **2. Khi có cơn:**
            - Nghỉ ngơi, nâng cao chân
            - Dùng thuốc sớm
            - Chườm lạnh
            - Đến bệnh viện nếu nặng

            **3. Giảm cân:**
            - Nếu thừa cân → Giảm cân từ từ
            - Giảm cân nhanh → Tăng acid uric → Cơn Gout

            **4. Sống tích cực:**
            - Gout có thể kiểm soát được
            - Tuân thủ điều trị → Không còn cơn
            - Đừng để Gout ảnh hưởng cuộc sống
            """,
            related_disease="gout",
            related_drugs=["Colchicine", "Allopurinol", "Ibuprofen"],
            printable=True
        ),

        PatientEducationTopic(
            id="kidney_stones_basics",
            title="Understanding Kidney Stones",
            title_vn="Hiểu về Sỏi thận",
            category="Disease",
            content="""
            # Hiểu về Sỏi thận

            ## Sỏi thận là gì?

            Sỏi thận là những tinh thể cứng hình thành trong thận từ các chất trong nước tiểu, có thể di chuyển xuống niệu quản, bàng quang, gây đau và tắc nghẽn.

            **⚠️ Đặc điểm:**
            - Rất đau (cơn đau quặn thận)
            - Có thể tái phát
            - Có thể phòng ngừa bằng chế độ ăn

            **Vị trí:**
            - Thận
            - Niệu quản
            - Bàng quang
            - Niệu đạo

            ## Triệu chứng:

            **Cơn đau quặn thận:**
            - **Đau dữ dội:** Đột ngột, ở vùng thắt lưng
            - **Đau lan:** Xuống bụng dưới, háng, bộ phận sinh dục
            - **Đau từng cơn:** Đau dữ dội rồi giảm, lặp lại
            - **Không nằm yên được:** Vật vã, lăn lộn
            - **Buồn nôn, nôn**

            **Triệu chứng khác:**
            - **Tiểu máu:** Nước tiểu đỏ hoặc hồng
            - **Tiểu buốt, tiểu rắt:** Khi sỏi ở bàng quang
            - **Sốt, ớn lạnh:** Nếu có nhiễm trùng
            - **Tiểu ít hoặc không tiểu:** Nếu tắc nghẽn nặng

            **⚠️ Lưu ý:** Một số người có sỏi nhưng không có triệu chứng (sỏi im lặng).

            ## Nguyên nhân:

            **1. Uống ít nước:**
            - Nước tiểu đậm đặc
            - Tinh thể dễ kết tinh

            **2. Chế độ ăn:**
            - **Muối nhiều:** Tăng canxi trong nước tiểu
            - **Protein nhiều:** Tăng acid uric, oxalate
            - **Oxalate nhiều:** Rau chân vịt, đậu phộng, sô cô la

            **3. Yếu tố khác:**
            - **Di truyền:** Có người thân bị sỏi
            - **Bệnh khác:** Cường cận giáp, nhiễm trùng tiểu
            - **Thuốc:** Một số thuốc tăng nguy cơ
            - **Ít vận động:** Tăng canxi trong nước tiểu

            ## Chẩn đoán:

            **1. Siêu âm:**
            - Phát hiện sỏi
            - Đánh giá kích thước, vị trí
            - Xem có ứ nước không

            **2. CT scan:**
            - Chính xác hơn siêu âm
            - Xem rõ kích thước, vị trí

            **3. Xét nghiệm:**
            - Nước tiểu: Tìm tinh thể, máu
            - Máu: Chức năng thận, canxi, acid uric

            **4. Phân tích sỏi:**
            - Sau khi lấy sỏi ra
            - Xác định loại sỏi → Điều chỉnh chế độ ăn

            ## Điều trị:

            **1. Sỏi nhỏ (< 5mm):**
            - **Uống nhiều nước:** 2-3 lít/ngày
            - **Thuốc giảm đau:** NSAID, Paracetamol
            - **Thuốc giãn niệu quản:** Tamsulosin
            - **Tập thể dục:** Đi bộ, nhảy
            - **Thường tự ra:** 80-90% trong 4-6 tuần

            **2. Sỏi vừa (5-10mm):**
            - **Tán sỏi ngoài cơ thể (ESWL):** Dùng sóng xung kích
            - **Nội soi niệu quản:** Lấy sỏi qua ống soi
            - **Tán sỏi laser:** Qua nội soi

            **3. Sỏi lớn (> 10mm):**
            - **Tán sỏi qua da (PCNL):** Rạch nhỏ, đưa ống vào thận
            - **Phẫu thuật mở:** (Hiếm)

            **4. Điều trị cơn đau:**
            - **NSAID:** Ibuprofen, Diclofenac (tiêm hoặc uống)
            - **Paracetamol:** Nếu không dùng được NSAID
            - **Thuốc giảm co thắt:** Buscopan

            ## 🍽️ CHẾ ĐỘ ĂN CHO NGƯỜI SỎI THẬN:

            **⚠️ QUAN TRỌNG:** Chế độ ăn rất quan trọng trong phòng ngừa sỏi!

            **1. Nguyên tắc:**
            - **Uống nhiều nước:** Quan trọng nhất!
            - **Giảm muối:** < 5g/ngày
            - **Giảm protein động vật:** Thịt đỏ
            - **Giảm oxalate:** (Nếu sỏi oxalate)

            **2. Uống nước (QUAN TRỌNG NHẤT!):**
            - **Mục tiêu:** 2.5-3 lít/ngày
            - **Nước lọc:** Tốt nhất
            - **Nước chanh:** Citrate giúp ngăn sỏi
            - **Tránh:** Nước ngọt có đường, nước có nhiều oxalate

            **3. Giảm muối:**
            - **Mục tiêu:** < 5g muối/ngày
            - **Tránh:** Dưa muối, cà muối, đồ hộp, thức ăn nhanh
            - **Đọc nhãn:** Chọn thực phẩm ít natri

            **4. Giảm protein động vật:**
            - **Hạn chế:** Thịt đỏ (thịt bò, thịt heo)
            - **Nên ăn:** Thịt trắng (thịt gà, cá) - 100-150g/ngày
            - **Protein thực vật:** Đậu, đậu phụ (tốt hơn)

            **5. Giảm oxalate (Nếu sỏi oxalate):**
            - **Hạn chế:** Rau chân vịt, đậu phộng, sô cô la, trà đặc
            - **Có thể ăn:** Rau xanh khác, trái cây

            **6. Canxi:**
            - **Có thể ăn:** Sữa, sữa chua (1-2 phần/ngày)
            - **Không kiêng hoàn toàn:** Canxi từ thức ăn không tăng nguy cơ
            - **Tránh:** Viên bổ sung canxi (nếu không cần)

            **7. Thực phẩm NÊN ĂN:**
            - **Rau xanh:** Rau cải, rau muống, bông cải (trừ rau chân vịt nếu sỏi oxalate)
            - **Trái cây:** Tất cả (đặc biệt cam, chanh - citrate)
            - **Ngũ cốc:** Gạo, bánh mì
            - **Thịt trắng:** Thịt gà, cá (ít)
            - **Đậu, đậu phụ:** Protein thực vật
            - **Sữa ít béo:** 1-2 ly/ngày

            **8. Thực phẩm CẦN TRÁNH:**
            - **Muối nhiều:** Dưa muối, đồ hộp, thức ăn nhanh
            - **Thịt đỏ nhiều:** Thịt bò, thịt heo (ăn ít)
            - **Oxalate (nếu sỏi oxalate):** Rau chân vịt, đậu phộng, sô cô la
            - **Nước ngọt có đường:** Tăng nguy cơ

            **9. Thực đơn mẫu (1 ngày):**
            - **Sáng:** Cháo yến mạch + sữa ít béo + nước chanh
            - **Trưa:** 1 chén cơm + cá hấp + rau luộc + canh rau
            - **Tối:** 1 chén cơm + thịt gà luộc + rau xào + canh
            - **Uống nước:** 2.5-3 lít/ngày (nước lọc, nước chanh)

            ## 🏃 TẬP THỂ DỤC:

            **1. Khi có sỏi nhỏ:**
            - **Đi bộ, nhảy:** Giúp sỏi di chuyển, ra ngoài
            - **Tập thể dục nhẹ nhàng:** 30 phút/ngày

            **2. Phòng ngừa:**
            - **Tập thể dục đều đặn:** 30 phút/ngày
            - **Đi bộ, bơi, đạp xe**
            - **Tránh:** Ngồi lâu, ít vận động

            ## 🛡️ PHÒNG NGỪA TÁI PHÁT:

            **1. Uống nhiều nước:**
            - **2.5-3 lít/ngày:** Quan trọng nhất!
            - **Nước tiểu trong:** Dấu hiệu uống đủ
            - **Uống đều trong ngày:** Không uống dồn

            **2. Chế độ ăn:**
            - Giảm muối
            - Giảm protein động vật
            - Giảm oxalate (nếu sỏi oxalate)

            **3. Tập thể dục:**
            - Đều đặn, không ngồi lâu

            **4. Khám định kỳ:**
            - Siêu âm thận 6-12 tháng/lần
            - Phát hiện sớm sỏi mới

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Cơn đau quặn thận:**
            - Đau dữ dội, không chịu được
            - Thuốc giảm đau không hiệu quả

            **2. Tắc nghẽn:**
            - Tiểu ít hoặc không tiểu
            - Sốt, ớn lạnh (nhiễm trùng)

            **3. Chảy máu:**
            - Tiểu máu nhiều

            **4. Sỏi lớn:**
            - Sỏi > 10mm → Cần can thiệp

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Khi có sỏi:**
            - Uống nhiều nước
            - Thuốc giảm đau
            - Tập thể dục (nếu sỏi nhỏ)
            - Theo dõi, tái khám

            **2. Phòng ngừa:**
            - Uống nhiều nước (quan trọng nhất!)
            - Chế độ ăn phù hợp
            - Tập thể dục đều đặn
            - Khám định kỳ

            **3. Sống tích cực:**
            - Sỏi thận có thể phòng ngừa
            - Tuân thủ chế độ ăn → Giảm tái phát
            """,
            related_disease="kidney_stones",
            related_drugs=["Tamsulosin", "Ibuprofen", "Paracetamol"],
            printable=True
        ),

        PatientEducationTopic(
            id="hyperthyroidism_basics",
            title="Understanding Hyperthyroidism",
            title_vn="Hiểu về Cường giáp",
            category="Disease",
            content="""
            # Hiểu về Cường giáp

            ## Cường giáp là gì?

            Cường giáp là tình trạng tuyến giáp sản xuất quá nhiều hormone tuyến giáp (T3, T4), dẫn đến tăng chuyển hóa. Bệnh phổ biến ở phụ nữ, đặc biệt độ tuổi 20-40.

            **⚠️ Đặc điểm:**
            - Tuyến giáp hoạt động quá mức
            - Tăng chuyển hóa toàn thân
            - Phổ biến ở phụ nữ (gấp 5-10 lần nam)
            - Có thể điều trị khỏi

            **Nguyên nhân chính:**
            - **Basedow (Graves' disease):** 70-80% (bệnh tự miễn)
            - Bướu giáp đa nhân độc
            - Viêm giáp (thyroiditis)
            - U tuyến giáp độc
            - Quá liều hormone tuyến giáp

            ## Triệu chứng:

            **Triệu chứng điển hình:**
            - **Nhịp tim nhanh:** > 100 lần/phút, đánh trống ngực
            - **Sụt cân:** Dù ăn nhiều
            - **Ra mồ hôi nhiều:** Không do nóng
            - **Run tay:** Rõ ràng, không kiểm soát được
            - **Mệt mỏi, yếu cơ:** Đặc biệt cơ đùi
            - **Khó ngủ:** Mất ngủ, ngủ không sâu
            - **Tiêu chảy:** Tăng nhu động ruột
            - **Tính tình thay đổi:** Dễ cáu, lo âu, bồn chồn

            **Triệu chứng Basedow:**
            - **Mắt lồi:** Nhìn chằm chằm, mắt to
            - **Phù quanh mắt:** Sưng mí mắt
            - **Bướu giáp:** Tuyến giáp to, có thể thấy, sờ được

            **Triệu chứng khác:**
            - Rụng tóc
            - Da ẩm, nóng
            - Kinh nguyệt không đều (nữ)
            - Giảm ham muốn tình dục

            **⚠️ Cơn cường giáp cấp (Thyroid storm):**
            - Sốt cao > 38.5°C
            - Nhịp tim rất nhanh > 140 lần/phút
            - Rối loạn ý thức, lú lẫn
            - **Cần cấp cứu ngay!**

            ## Nguyên nhân:

            **1. Basedow (Graves' disease):**
            - Bệnh tự miễn
            - Cơ thể tạo kháng thể kích thích tuyến giáp
            - Có yếu tố di truyền

            **2. Bướu giáp đa nhân độc:**
            - Nhiều nhân trong tuyến giáp tự sản xuất hormone

            **3. Viêm giáp:**
            - Viêm tuyến giáp → Giải phóng hormone

            **4. Yếu tố nguy cơ:**
            - Nữ giới
            - Tuổi 20-40
            - Tiền sử gia đình
            - Stress
            - Hút thuốc (tăng nguy cơ mắt lồi)

            ## Chẩn đoán:

            **Xét nghiệm:**
            - **TSH giảm:** < 0.1 mIU/L
            - **T3, T4 tăng:** Tăng rõ ràng
            - **TRAb (Thyroid Receptor Antibody):** Dương tính nếu Basedow
            - **Anti-TPO, Anti-Tg:** Có thể dương tính

            **Khám:**
            - Siêu âm tuyến giáp
            - Xạ hình tuyến giáp (nếu cần)

            ## Điều trị:

            **1. Thuốc kháng giáp:**
            - **Methimazole:** Thuốc đầu tay (10-40mg/ngày)
            - **Propylthiouracil (PTU):** Nếu mang thai 3 tháng đầu
            - **Thời gian:** 12-18 tháng
            - **Theo dõi:** Chức năng gan, bạch cầu

            **2. Beta-blocker:**
            - **Propranolol:** Giảm nhịp tim, run tay (20-40mg x 3-4 lần/ngày)
            - Dùng ngắn hạn, giảm triệu chứng

            **3. I-131 (Radioactive Iodine):**
            - Điều trị dứt điểm
            - Uống 1 lần
            - **⚠️ Lưu ý:** Không dùng khi mang thai, cho con bú

            **4. Phẫu thuật:**
            - Cắt một phần hoặc toàn bộ tuyến giáp
            - Nếu bướu to, kháng thuốc

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Nên ăn:**
            - **Thực phẩm giàu canxi:** Sữa, phô mai, cá nhỏ (ăn cả xương), rau xanh
            - **Thực phẩm giàu vitamin D:** Cá béo, trứng, sữa
            - **Protein nạc:** Thịt gà, cá, đậu
            - **Rau xanh, trái cây:** Đủ vitamin, khoáng chất
            - **Uống nhiều nước:** Bù mồ hôi

            **2. Hạn chế:**
            - **I-ốt:** Không bổ sung quá nhiều (rong biển, muối i-ốt quá nhiều)
            - **Caffeine:** Có thể làm tăng nhịp tim
            - **Đồ cay, nóng:** Có thể làm tăng mồ hôi

            **3. Tránh:**
            - Rượu bia (ảnh hưởng thuốc)
            - Thuốc lá (tăng nguy cơ mắt lồi)

            **4. Thực đơn mẫu:**
            - **Sáng:** Cháo yến mạch, sữa, trứng
            - **Trưa:** Cơm, thịt gà/cá, rau xanh, canh, sữa chua
            - **Chiều:** Cơm, thịt/cá, rau xanh, canh, trái cây
            - **Bữa phụ:** Sữa, trái cây, hạt

            ## 🏃 TẬP THỂ DỤC:

            **1. Khi chưa điều trị ổn:**
            - Tránh tập gắng sức (nhịp tim đã nhanh)
            - Tập nhẹ: Đi bộ 15-20 phút/ngày
            - Yoga, thiền (giảm stress)

            **2. Khi đã điều trị ổn:**
            - Tập bình thường
            - Đi bộ, chạy bộ, bơi lội
            - 30 phút/ngày, 5 ngày/tuần
            - Tăng cường cơ (phòng loãng xương)

            **3. Lưu ý:**
            - Theo dõi nhịp tim khi tập
            - Nghỉ ngơi nếu mệt
            - Uống đủ nước

            ## 💊 QUẢN LÝ THUỐC:

            **1. Methimazole:**
            - Uống sau ăn
            - Uống đều đặn, đúng giờ
            - Không tự ý ngừng
            - **Tác dụng phụ:** Phát ban, giảm bạch cầu, tổn thương gan (hiếm)

            **2. Propranolol:**
            - Uống với nước
            - Có thể gây mệt mỏi, chóng mặt
            - Không ngừng đột ngột

            **3. Theo dõi:**
            - Xét nghiệm TSH, T3, T4 mỗi 4-6 tuần
            - Chức năng gan, bạch cầu mỗi 3 tháng
            - Điều chỉnh liều theo kết quả

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Cơn cường giáp cấp:**
            - Sốt cao > 38.5°C
            - Nhịp tim > 140 lần/phút
            - Rối loạn ý thức
            - **Cấp cứu ngay!**

            **2. Tác dụng phụ thuốc:**
            - Sốt, đau họng (giảm bạch cầu)
            - Vàng da (tổn thương gan)
            - Phát ban nặng

            **3. Triệu chứng nặng:**
            - Khó thở
            - Đau ngực
            - Rối loạn nhịp tim

            ## 💡 PHÒNG NGỪA:

            **1. Không thể phòng ngừa hoàn toàn:**
            - Basedow là bệnh tự miễn
            - Có yếu tố di truyền

            **2. Có thể giảm nguy cơ:**
            - Bỏ thuốc lá (giảm mắt lồi)
            - Quản lý stress
            - Khám định kỳ nếu có tiền sử gia đình

            **3. Phát hiện sớm:**
            - Khám khi có triệu chứng
            - Xét nghiệm TSH định kỳ (nếu có nguy cơ)

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Khi bị cường giáp:**
            - Uống thuốc đều đặn
            - Theo dõi triệu chứng
            - Khám định kỳ
            - Nghỉ ngơi đủ

            **2. Chăm sóc mắt (nếu Basedow):**
            - Đeo kính râm (nhạy cảm ánh sáng)
            - Nhỏ mắt nhân tạo (khô mắt)
            - Nằm cao đầu khi ngủ (giảm phù)
            - Bỏ thuốc lá (quan trọng!)

            **3. Sống tích cực:**
            - Cường giáp có thể điều trị khỏi
            - Điều trị đúng → Bình thường hóa hormone
            - Có thể sống bình thường

            **4. Mang thai:**
            - Cần điều trị (ảnh hưởng thai nhi)
            - Dùng PTU 3 tháng đầu
            - Theo dõi sát
            """,
            related_disease="hyperthyroidism",
            related_drugs=["Methimazole", "Propylthiouracil", "Propranolol", "I-131"],
            printable=True
        ),

        PatientEducationTopic(
            id="hypothyroidism_basics",
            title="Understanding Hypothyroidism",
            title_vn="Hiểu về Suy giáp",
            category="Disease",
            content="""
            # Hiểu về Suy giáp

            ## Suy giáp là gì?

            Suy giáp là tình trạng tuyến giáp sản xuất không đủ hormone tuyến giáp (T3, T4), dẫn đến giảm chuyển hóa. Bệnh phổ biến ở phụ nữ, đặc biệt sau 50 tuổi.

            **⚠️ Đặc điểm:**
            - Tuyến giáp hoạt động kém
            - Giảm chuyển hóa toàn thân
            - Phổ biến ở phụ nữ (gấp 5-10 lần nam)
            - Cần điều trị suốt đời

            **Nguyên nhân chính:**
            - **Hashimoto (viêm giáp tự miễn):** 90% (nguyên nhân #1)
            - Sau phẫu thuật cắt tuyến giáp
            - Sau điều trị I-131
            - Thiếu i-ốt (hiếm ở Việt Nam)
            - Thuốc: Lithium, Amiodarone

            ## Triệu chứng:

            **Triệu chứng điển hình:**
            - **Mệt mỏi, suy nhược:** Uể oải, không có sức
            - **Tăng cân:** Dù ăn ít
            - **Lạnh:** Không chịu được lạnh
            - **Da khô, tóc rụng:** Da thô, tóc dễ gãy
            - **Táo bón:** Giảm nhu động ruột
            - **Trầm cảm:** Buồn, chán nản
            - **Nhịp tim chậm:** < 60 lần/phút
            - **Phù niêm:** Mặt phù, mí mắt sưng

            **Triệu chứng khác:**
            - Giọng khàn
            - Khó tập trung, trí nhớ kém
            - Đau cơ, cứng khớp
            - Kinh nguyệt nhiều (nữ)
            - Giảm ham muốn tình dục

            **⚠️ Hôn mê phù niêm (Myxedema coma):**
            - Hạ thân nhiệt < 35°C
            - Hôn mê
            - Suy hô hấp
            - **Cấp cứu ngay!**

            ## Nguyên nhân:

            **1. Hashimoto:**
            - Bệnh tự miễn
            - Cơ thể tấn công tuyến giáp
            - Có yếu tố di truyền

            **2. Sau phẫu thuật/điều trị:**
            - Cắt tuyến giáp
            - Điều trị I-131 (cường giáp)

            **3. Yếu tố nguy cơ:**
            - Nữ giới
            - Tuổi > 50
            - Tiền sử gia đình
            - Bệnh tự miễn khác

            ## Chẩn đoán:

            **Xét nghiệm:**
            - **TSH tăng:** > 4.5 mIU/L
            - **T4 giảm:** < 0.8 ng/dL
            - **Anti-TPO, Anti-Tg:** Dương tính nếu Hashimoto

            **Khám:**
            - Siêu âm tuyến giáp

            ## Điều trị:

            **1. Levothyroxine (T4):**
            - Thuốc đầu tay
            - Bắt đầu liều thấp: 25-50 mcg/ngày
            - Tăng dần mỗi 4-6 tuần
            - **Dùng suốt đời**

            **2. Liều duy trì:**
            - 1.6-1.8 mcg/kg/ngày
            - Uống buổi sáng, trước ăn 30-60 phút
            - Không uống với sữa, canxi, sắt

            **3. Theo dõi:**
            - Xét nghiệm TSH sau 4-6 tuần
            - Điều chỉnh liều theo TSH
            - Mục tiêu: TSH 0.5-2.5 mIU/L

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Nên ăn:**
            - **I-ốt (vừa phải):** Muối i-ốt, cá biển, rong biển (không quá nhiều)
            - **Selen:** Cá, trứng, hạt (giúp chuyển đổi T4 → T3)
            - **Kẽm:** Thịt, hải sản, hạt
            - **Protein nạc:** Thịt, cá, đậu
            - **Rau xanh, trái cây:** Đủ vitamin

            **2. Hạn chế:**
            - **Goitrogens (nếu thiếu i-ốt):** Bắp cải, súp lơ (nấu chín giảm tác dụng)
            - **Đồ chế biến sẵn:** Ít dinh dưỡng

            **3. Lưu ý:**
            - **Canxi, sắt:** Uống cách xa Levothyroxine 4 giờ
            - **Cà phê:** Uống cách xa Levothyroxine 1 giờ

            **4. Thực đơn mẫu:**
            - **Sáng:** Cháo yến mạch, trứng, sữa (sau khi uống thuốc 1 giờ)
            - **Trưa:** Cơm, thịt/cá, rau xanh, canh
            - **Chiều:** Cơm, thịt/cá, rau xanh, canh
            - **Bữa phụ:** Trái cây, hạt

            ## 🏃 TẬP THỂ DỤC:

            **1. Khi chưa điều trị ổn:**
            - Tập nhẹ: Đi bộ 15-20 phút/ngày
            - Tránh gắng sức (mệt mỏi, nhịp tim chậm)

            **2. Khi đã điều trị ổn:**
            - Tập bình thường
            - Đi bộ, chạy bộ, bơi lội
            - 30 phút/ngày, 5 ngày/tuần
            - Tăng cường cơ (phòng loãng xương)

            **3. Lưu ý:**
            - Khởi động kỹ (nhịp tim chậm)
            - Nghỉ ngơi nếu mệt
            - Uống đủ nước

            ## 💊 QUẢN LÝ THUỐC:

            **1. Levothyroxine:**
            - **Uống buổi sáng, trước ăn 30-60 phút**
            - Uống với nước lọc
            - **Không uống với:** Sữa, canxi, sắt, cà phê
            - Uống đều đặn, đúng giờ
            - **Dùng suốt đời**

            **2. Tác dụng phụ:**
            - Quá liều: Nhịp tim nhanh, mất ngủ, run tay (như cường giáp)
            - Thiếu liều: Triệu chứng suy giáp

            **3. Theo dõi:**
            - TSH mỗi 4-6 tuần (khi điều chỉnh liều)
            - TSH mỗi 6-12 tháng (khi ổn định)
            - Mục tiêu: TSH 0.5-2.5 mIU/L

            **4. Lưu ý:**
            - Không tự ý ngừng thuốc
            - Không tự ý đổi liều
            - Báo bác sĩ nếu có triệu chứng bất thường

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Hôn mê phù niêm:**
            - Hạ thân nhiệt < 35°C
            - Hôn mê
            - Khó thở
            - **Cấp cứu ngay!**

            **2. Triệu chứng nặng:**
            - Mệt mỏi quá mức
            - Khó thở
            - Đau ngực
            - Rối loạn nhịp tim

            **3. Quá liều thuốc:**
            - Nhịp tim nhanh
            - Mất ngủ
            - Run tay

            ## 💡 PHÒNG NGỪA:

            **1. Không thể phòng ngừa hoàn toàn:**
            - Hashimoto là bệnh tự miễn
            - Có yếu tố di truyền

            **2. Có thể giảm nguy cơ:**
            - Bổ sung i-ốt đủ (nếu thiếu)
            - Khám định kỳ nếu có nguy cơ

            **3. Phát hiện sớm:**
            - Khám khi có triệu chứng
            - Xét nghiệm TSH định kỳ (nếu có nguy cơ)

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Khi bị suy giáp:**
            - Uống thuốc đều đặn, đúng cách
            - Theo dõi triệu chứng
            - Khám định kỳ
            - Kiên nhẫn (cải thiện từ từ)

            **2. Uống thuốc đúng cách:**
            - Buổi sáng, trước ăn 30-60 phút
            - Không uống với sữa, canxi, sắt
            - Uống đều đặn, không quên

            **3. Sống tích cực:**
            - Suy giáp có thể kiểm soát tốt
            - Điều trị đúng → Bình thường hóa hormone
            - Có thể sống bình thường

            **4. Mang thai:**
            - Cần tăng liều (nhu cầu tăng)
            - Theo dõi sát TSH
            - Quan trọng cho sự phát triển thai nhi
            """,
            related_disease="hypothyroidism",
            related_drugs=["Levothyroxine"],
            printable=True
        ),

        PatientEducationTopic(
            id="chronic_kidney_disease_basics",
            title="Understanding Chronic Kidney Disease",
            title_vn="Hiểu về Suy thận mạn tính (CKD)",
            category="Disease",
            content="""
            # Hiểu về Suy thận mạn tính (CKD)

            ## Suy thận mạn tính là gì?

            Suy thận mạn tính là tình trạng suy giảm chức năng thận mạn tính, kéo dài ≥ 3 tháng. Bệnh rất phổ biến tại Việt Nam, thường do đái tháo đường và tăng huyết áp.

            **⚠️ Đặc điểm:**
            - Suy giảm chức năng thận mạn tính
            - Tiến triển từ từ
            - Phổ biến tại Việt Nam
            - Có thể dẫn đến lọc máu/ghép thận

            **Phân loại theo KDIGO:**
            - **G1-G2:** eGFR ≥ 60 (tổn thương thận, chức năng bình thường)
            - **G3a-G3b:** eGFR 30-59 (suy thận nhẹ-trung bình)
            - **G4:** eGFR 15-29 (suy thận nặng)
            - **G5:** eGFR < 15 (suy thận giai đoạn cuối - cần lọc máu)

            ## Triệu chứng:

            **Giai đoạn sớm (G1-G3):**
            - Thường không có triệu chứng
            - Có thể phát hiện khi khám sức khỏe

            **Giai đoạn muộn (G4-G5):**
            - **Mệt mỏi, suy nhược:** Do thiếu máu
            - **Phù:** Chân, mặt
            - **Buồn nôn, nôn:** Do ure cao
            - **Ngứa:** Do tích tụ độc tố
            - **Thiếu máu:** Da xanh, mệt mỏi
            - **Tăng huyết áp**
            - **Xương yếu:** Do rối loạn canxi, phospho

            **⚠️ Giai đoạn cuối (ESRD):**
            - Cần lọc máu hoặc ghép thận
            - Nhiều biến chứng

            ## Nguyên nhân:

            **1. Đái tháo đường:**
            - Nguyên nhân #1 tại Việt Nam
            - Bệnh thận đái tháo đường

            **2. Tăng huyết áp:**
            - Nguyên nhân #2
            - Bệnh thận do tăng huyết áp

            **3. Viêm cầu thận:**
            - Viêm cầu thận mạn

            **4. Yếu tố khác:**
            - Bệnh thận đa nang
            - Thuốc độc thận (NSAID, kháng sinh)
            - Tắc nghẽn đường tiết niệu

            ## Chẩn đoán:

            **Xét nghiệm:**
            - **Creatinine, eGFR:** Đánh giá chức năng thận
            - **Albumin niệu (UACR):** Đánh giá tổn thương thận
            - Công thức máu (thiếu máu)
            - Điện giải, canxi, phospho

            ## Điều trị:

            **1. Làm chậm tiến triển:**
            - **ACE inhibitor hoặc ARB:** Nếu có protein niệu
            - **Kiểm soát huyết áp:** < 130/80 mmHg
            - **Kiểm soát đường huyết:** Nếu đái tháo đường
            - **Statin:** Giảm cholesterol

            **2. Điều trị biến chứng:**
            - **Thiếu máu:** Erythropoietin, sắt
            - **Rối loạn canxi, phospho:** Bổ sung canxi, hạn chế phospho
            - **Toan máu:** Bicarbonate

            **3. Lọc máu:**
            - Nếu CKD giai đoạn 5 (eGFR < 15)
            - Thẩm phân phúc mạc hoặc chạy thận nhân tạo

            **4. Ghép thận:**
            - Nếu phù hợp

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Protein:**
            - **Giai đoạn sớm (G1-G3):** Bình thường (0.8-1g/kg/ngày)
            - **Giai đoạn muộn (G4-G5):** Giảm (0.6-0.8g/kg/ngày)
            - Protein chất lượng cao: Thịt, cá, trứng, sữa

            **2. Muối:**
            - **Giảm muối:** < 2g/ngày (nếu tăng huyết áp, phù)
            - Tránh đồ mặn, chế biến sẵn

            **3. Phospho:**
            - **Hạn chế:** Nếu phospho cao (G4-G5)
            - Tránh: Sữa, phô mai, đậu, hạt, đồ uống có ga

            **4. Kali:**
            - **Hạn chế:** Nếu kali cao (G4-G5)
            - Tránh: Chuối, cam, khoai tây, cà chua

            **5. Nước:**
            - Uống đủ nước (nếu không phù)
            - Hạn chế nếu có phù

            **6. Thực đơn mẫu (G1-G3):**
            - **Sáng:** Cháo thịt, trứng
            - **Trưa:** Cơm, thịt/cá, rau xanh, canh (không mặn)
            - **Chiều:** Cơm, thịt/cá, rau xanh, canh
            - **Bữa phụ:** Trái cây (tránh chuối, cam nếu G4-G5)

            ## 🏃 TẬP THỂ DỤC:

            **1. Nên tập:**
            - Tập thể dục đều đặn (cải thiện chức năng thận)
            - Đi bộ, chạy bộ, bơi lội
            - 30 phút/ngày, 5 ngày/tuần

            **2. Lưu ý:**
            - Tránh gắng sức quá mức
            - Nghỉ ngơi nếu mệt
            - Uống đủ nước

            ## 💊 QUẢN LÝ THUỐC:

            **1. ACE inhibitor/ARB:**
            - Làm chậm tiến triển (nếu có protein niệu)
            - Theo dõi chức năng thận, kali

            **2. Kiểm soát huyết áp:**
            - < 130/80 mmHg
            - Dùng thuốc đều đặn

            **3. Tránh thuốc độc thận:**
            - NSAID (Ibuprofen, Naproxen)
            - Một số kháng sinh
            - Báo bác sĩ tất cả thuốc đang dùng

            **4. Lưu ý:**
            - Không tự ý dùng thuốc
            - Theo dõi chức năng thận định kỳ

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Suy thận nặng:**
            - eGFR < 15
            - Cần lọc máu

            **2. Biến chứng:**
            - Phù phổi (khó thở)
            - Rối loạn điện giải nặng
            - Toan máu nặng

            **3. Triệu chứng nặng:**
            - Buồn nôn, nôn nhiều
            - Lú lẫn
            - Co giật

            ## 💡 PHÒNG NGỪA:

            **1. Kiểm soát đái tháo đường:**
            - Đường huyết ổn định
            - HbA1c < 7%

            **2. Kiểm soát huyết áp:**
            - Huyết áp < 130/80 mmHg
            - Dùng thuốc đều đặn

            **3. Tránh thuốc độc thận:**
            - Không tự ý dùng NSAID
            - Báo bác sĩ tất cả thuốc

            **4. Khám định kỳ:**
            - Nếu có đái tháo đường, tăng huyết áp
            - Xét nghiệm chức năng thận mỗi 3-6 tháng

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Khi bị suy thận mạn:**
            - Kiểm soát đái tháo đường, huyết áp (quan trọng!)
            - Chế độ ăn phù hợp
            - Tránh thuốc độc thận
            - Khám định kỳ

            **2. Chế độ ăn:**
            - Giảm muối, protein (nếu cần)
            - Hạn chế phospho, kali (nếu G4-G5)
            - Uống đủ nước

            **3. Sống tích cực:**
            - Suy thận mạn có thể làm chậm tiến triển
            - Điều trị đúng → Làm chậm tiến triển
            - Có thể sống lâu, chất lượng cuộc sống tốt

            **4. Chuẩn bị lọc máu:**
            - Nếu CKD giai đoạn 4-5
            - Tạo cầu nối AV fistula sớm
            - Giáo dục về lọc máu
            """,
            related_disease="chronic_kidney_disease",
            related_drugs=["ACE Inhibitor", "ARB", "Erythropoietin", "Furosemide"],
            printable=True
        ),

]
