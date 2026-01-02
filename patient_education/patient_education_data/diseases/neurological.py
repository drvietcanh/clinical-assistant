"""
Patient Education Topics - Neurological
"""
from patient_education.models import PatientEducationTopic


NEUROLOGICAL_TOPICS = [
        PatientEducationTopic(
            id="epilepsy_basics",
            title="Understanding Epilepsy",
            title_vn="Hiểu về Động kinh",
            category="Disease",
            content="""
            # Hiểu về Động kinh

            ## Động kinh là gì?

            Động kinh là rối loạn thần kinh đặc trưng bởi các cơn co giật tái phát do hoạt động điện bất thường của não. Bệnh có thể ảnh hưởng đến mọi lứa tuổi.

            **⚠️ Đặc điểm:**
            - Cơn co giật tái phát
            - Do hoạt động điện bất thường của não
            - Có thể kiểm soát bằng thuốc
            - Cần điều trị lâu dài

            **Phân loại:**
            - **Focal (cục bộ):** Bắt đầu từ một vùng não
            - **Generalized (toàn thể):** Ảnh hưởng toàn bộ não
            - **Unknown:** Không xác định được

            ## Triệu chứng:

            **Cơn co giật toàn thể (Generalized):**
            - **Co cứng-co giật:** Co cứng → Co giật toàn thân
            - **Mất ý thức:** Không nhớ gì sau cơn
            - **Cắn lưỡi:** Có thể xảy ra
            - **Tiểu không tự chủ:** Có thể xảy ra
            - **Sau cơn:** Mệt mỏi, lú lẫn, đau đầu

            **Cơn co giật cục bộ (Focal):**
            - **Có ý thức:** Vẫn tỉnh táo
            - **Triệu chứng:** Phụ thuộc vùng não
              - Vận động: Co giật một bên
              - Cảm giác: Tê, ngứa ran
              - Thị giác: Nhìn thấy ánh sáng, hình ảnh
              - Tâm thần: Sợ hãi, déjà vu

            **Cơn vắng (Absence):**
            - Nhìn chằm chằm, mất ý thức ngắn (5-10 giây)
            - Thường gặp ở trẻ em
            - Không có co giật

            **⚠️ Status epilepticus:**
            - Cơn co giật kéo dài > 5 phút
            - Hoặc nhiều cơn liên tiếp không hồi phục
            - **Cấp cứu ngay!**

            ## Nguyên nhân:

            **1. Vô căn (không rõ nguyên nhân):**
            - 50-60% trường hợp
            - Có thể do di truyền

            **2. Thứ phát:**
            - Sau chấn thương đầu
            - Sau đột quỵ
            - U não
            - Nhiễm trùng não (viêm màng não, viêm não)
            - Rối loạn chuyển hóa
            - Sốt cao (trẻ em)

            **3. Yếu tố kích thích:**
            - Thiếu ngủ
            - Rượu bia
            - Stress
            - Ánh sáng nhấp nháy
            - Quên uống thuốc

            ## Chẩn đoán:

            **Xét nghiệm:**
            - **EEG (Điện não đồ):** Phát hiện sóng bất thường
            - **MRI não:** Tìm nguyên nhân
            - **CT não:** Nếu không có MRI
            - **Xét nghiệm máu:** Điện giải, đường huyết, chức năng gan

            ## Điều trị:

            **1. Thuốc chống động kinh (AED):**
            - **Carbamazepine:** Focal seizures
            - **Valproate:** Generalized seizures
            - **Lamotrigine:** Focal và generalized
            - **Levetiracetam:** Focal và generalized
            - **Topiramate:** Focal và generalized
            - **Bắt đầu một thuốc, tăng dần liều**
            - **Kết hợp 2-3 thuốc nếu cần**

            **2. Phẫu thuật:**
            - Nếu kháng thuốc
            - Có tổn thương rõ trên MRI

            **3. Kích thích dây thần kinh phế vị (VNS):**
            - Nếu kháng thuốc, không phẫu thuật được

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Nên ăn:**
            - **Chế độ ăn bình thường, đủ dinh dưỡng**
            - Protein: Thịt, cá, trứng, đậu
            - Carbohydrate: Cơm, bánh mì, mì
            - Rau xanh, trái cây
            - Uống đủ nước

            **2. Ketogenic diet (nếu có chỉ định):**
            - Chế độ ăn nhiều chất béo, ít carbohydrate
            - Chỉ dùng khi có chỉ định bác sĩ
            - Cần theo dõi sát

            **3. Tránh:**
            - Rượu bia (kích thích cơn)
            - Caffeine quá nhiều (có thể kích thích)
            - Bỏ bữa (hạ đường huyết → cơn)

            **4. Thực đơn mẫu:**
            - **Sáng:** Cháo/cơm, thịt/cá, rau
            - **Trưa:** Cơm, thịt/cá, rau xanh, canh
            - **Chiều:** Cơm, thịt/cá, rau xanh, canh
            - **Bữa phụ:** Trái cây, sữa

            ## 🏃 TẬP THỂ DỤC:

            **1. Nên tập:**
            - Tập thể dục bình thường (nếu cơn đã kiểm soát)
            - Đi bộ, chạy bộ, bơi lội
            - 30 phút/ngày, 5 ngày/tuần
            - **Lợi ích:** Giảm stress, cải thiện giấc ngủ

            **2. Tránh:**
            - Bơi một mình (cần người giám sát)
            - Leo núi, nhảy dù (nguy hiểm nếu có cơn)
            - Tập quá mệt (thiếu ngủ → cơn)

            **3. Lưu ý:**
            - Ngủ đủ giấc (quan trọng!)
            - Uống đủ nước khi tập
            - Mang theo thông tin y tế

            ## 💊 QUẢN LÝ THUỐC:

            **1. Uống đúng cách:**
            - **Uống đều đặn, đúng giờ** (quan trọng nhất!)
            - Không tự ý ngừng thuốc
            - Không tự ý đổi liều
            - Uống với nước, sau ăn

            **2. Tác dụng phụ:**
            - **Carbamazepine:** Chóng mặt, buồn nôn, phát ban
            - **Valproate:** Tăng cân, rụng tóc, tổn thương gan
            - **Lamotrigine:** Phát ban (nguy hiểm nếu nặng)
            - **Levetiracetam:** Buồn ngủ, cáu gắt
            - **Topiramate:** Sỏi thận, giảm cân

            **3. Theo dõi:**
            - Nồng độ thuốc trong máu (nếu cần)
            - Chức năng gan, thận định kỳ
            - Đếm số cơn co giật

            **4. Lưu ý:**
            - Báo bác sĩ nếu có tác dụng phụ
            - Không ngừng thuốc đột ngột (nguy hiểm!)

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Status epilepticus:**
            - Cơn co giật > 5 phút
            - Nhiều cơn liên tiếp
            - **Cấp cứu ngay!**

            **2. Chấn thương do cơn:**
            - Ngã, đập đầu
            - Gãy xương
            - Chảy máu

            **3. Tác dụng phụ nặng:**
            - Phát ban nặng (Lamotrigine)
            - Vàng da (tổn thương gan)
            - Rối loạn tâm thần

            **4. Cơn mới:**
            - Cơn đầu tiên
            - Cơn thay đổi tính chất

            ## 💡 PHÒNG NGỪA:

            **1. Tránh yếu tố kích thích:**
            - **Ngủ đủ giấc** (quan trọng nhất!)
            - Tránh rượu bia
            - Quản lý stress
            - Tránh ánh sáng nhấp nháy (nếu nhạy cảm)

            **2. Uống thuốc đều đặn:**
            - Không quên uống thuốc
            - Đặt báo thức nhắc uống thuốc
            - Mang thuốc khi đi xa

            **3. An toàn:**
            - Đeo vòng cảnh báo y tế
            - Thông báo cho người xung quanh
            - Tránh hoạt động nguy hiểm

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Khi có cơn co giật:**
            - **KHÔNG:** Đưa vật vào miệng, giữ chặt, đổ nước
            - **NÊN:** Đặt nằm nghiêng, bảo vệ đầu, gọi cấp cứu nếu > 5 phút

            **2. Sống tích cực:**
            - Động kinh có thể kiểm soát bằng thuốc
            - 70% bệnh nhân không còn cơn với điều trị đúng
            - Có thể sống bình thường, làm việc, học tập

            **3. Hỗ trợ:**
            - Tham gia nhóm hỗ trợ
            - Giáo dục gia đình, bạn bè
            - Tư vấn tâm lý (nếu cần)

            **4. Mang thai:**
            - Cần điều chỉnh thuốc (một số thuốc ảnh hưởng thai nhi)
            - Bổ sung acid folic
            - Theo dõi sát
            """,
            related_disease="epilepsy",
            related_drugs=["Carbamazepine", "Valproate", "Lamotrigine", "Levetiracetam", "Topiramate"],
            printable=True
        ),

        PatientEducationTopic(
            id="migraine_basics",
            title="Understanding Migraine",
            title_vn="Hiểu về Đau nửa đầu (Migraine)",
            category="Disease",
            content="""
            # Hiểu về Đau nửa đầu (Migraine)

            ## Migraine là gì?

            Migraine là bệnh đau đầu nguyên phát, đặc trưng bởi cơn đau đầu một bên, đau nhói, kèm buồn nôn, nhạy cảm ánh sáng/tiếng động. Bệnh rất phổ biến, ảnh hưởng đến chất lượng cuộc sống.

            **⚠️ Đặc điểm:**
            - Đau đầu một bên (có thể hai bên)
            - Đau nhói, đau vừa đến nặng
            - Kèm buồn nôn, nhạy cảm ánh sáng/tiếng động
            - Tăng khi vận động
            - Kéo dài 4-72 giờ

            **Phân loại:**
            - **Migraine không aura:** 80% (không có dấu hiệu báo trước)
            - **Migraine có aura:** 20% (có dấu hiệu báo trước: rối loạn thị giác, cảm giác)

            ## Triệu chứng:

            **Giai đoạn tiền triệu (Prodrome):** 1-2 ngày trước cơn
            - Thay đổi tâm trạng
            - Cổ cứng
            - Thèm ăn
            - Táo bón hoặc tiêu chảy

            **Giai đoạn aura (nếu có):** 5-60 phút trước cơn
            - **Rối loạn thị giác:** Nhìn thấy ánh sáng, đường zigzag, mất thị trường
            - **Rối loạn cảm giác:** Tê, ngứa ran một bên
            - **Rối loạn ngôn ngữ:** Nói khó

            **Giai đoạn đau đầu:**
            - **Đau một bên:** Có thể hai bên
            - **Đau nhói:** Như đập, đau vừa đến nặng
            - **Tăng khi vận động:** Đi lại, cúi xuống
            - **Kéo dài:** 4-72 giờ (không điều trị)
            - **Buồn nôn, nôn**
            - **Nhạy cảm ánh sáng (photophobia)**
            - **Nhạy cảm tiếng động (phonophobia)**

            **Giai đoạn hồi phục (Postdrome):** Sau cơn
            - Mệt mỏi
            - Lú lẫn
            - Có thể kéo dài 1-2 ngày

            ## Nguyên nhân:

            **1. Yếu tố di truyền:**
            - Có tiền sử gia đình

            **2. Yếu tố kích thích:**
            - **Thức ăn:** Rượu (đặc biệt rượu vang đỏ), phô mai, chocolate, thực phẩm chế biến
            - **Hormone:** Kinh nguyệt, mãn kinh, thuốc tránh thai
            - **Stress:** Căng thẳng, lo âu
            - **Thiếu ngủ hoặc ngủ quá nhiều**
            - **Thay đổi thời tiết**
            - **Mùi hương mạnh**
            - **Ánh sáng chói**

            **3. Yếu tố nguy cơ:**
            - Nữ giới (gấp 3 lần nam)
            - Tuổi 30-40
            - Tiền sử gia đình

            ## Chẩn đoán:

            **Tiêu chuẩn ICHD-3:**
            - ≥ 5 cơn đau đầu với đặc điểm migraine
            - Đau đầu kéo dài 4-72 giờ
            - Có ≥ 2: một bên, nhói, vừa-nặng, tăng khi vận động
            - Có ≥ 1: buồn nôn/vom, nhạy cảm ánh sáng/tiếng động

            **Xét nghiệm:**
            - Không cần xét nghiệm đặc biệt
            - CT/MRI não (nếu có triệu chứng báo động)

            ## Điều trị:

            **1. Cắt cơn:**
            - **Triptan:** Sumatriptan, Rizatriptan (nếu đau vừa-nặng)
            - **NSAID:** Ibuprofen, Naproxen (nếu đau nhẹ-vừa)
            - **Paracetamol:** Nếu đau nhẹ
            - **Uống sớm:** Khi mới bắt đầu đau (hiệu quả hơn)

            **2. Chống nôn:**
            - Metoclopramide, Ondansetron

            **3. Phòng ngừa (nếu ≥ 4 cơn/tháng):**
            - **Beta-blocker:** Propranolol
            - **Topiramate**
            - **Amitriptyline**
            - **CGRP antagonist:** Erenumab (nếu nặng)

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Tránh yếu tố kích thích:**
            - **Rượu:** Đặc biệt rượu vang đỏ
            - **Phô mai già:** Cheddar, Swiss
            - **Chocolate**
            - **Thực phẩm chế biến:** Thịt xông khói, xúc xích
            - **Mùi hương mạnh:** Hành, tỏi (một số người)

            **2. Nên ăn:**
            - **Ăn đều đặn:** Không bỏ bữa (hạ đường huyết → cơn)
            - **Thực phẩm tươi:** Rau xanh, trái cây
            - **Protein nạc:** Thịt, cá
            - **Uống đủ nước**

            **3. Thực đơn mẫu:**
            - **Sáng:** Cháo/cơm, trứng, sữa
            - **Trưa:** Cơm, thịt/cá, rau xanh, canh
            - **Chiều:** Cơm, thịt/cá, rau xanh, canh
            - **Bữa phụ:** Trái cây, hạt

            **4. Lưu ý:**
            - Ghi nhật ký đau đầu (tìm yếu tố kích thích)
            - Tránh thức ăn gây cơn

            ## 🏃 TẬP THỂ DỤC:

            **1. Nên tập:**
            - Tập thể dục đều đặn (giảm tần suất cơn)
            - Đi bộ, chạy bộ, bơi lội, yoga
            - 30 phút/ngày, 5 ngày/tuần
            - **Lợi ích:** Giảm stress, cải thiện giấc ngủ

            **2. Tránh:**
            - Tập quá mệt (có thể kích thích cơn)
            - Tập khi đang đau đầu

            **3. Lưu ý:**
            - Khởi động kỹ
            - Uống đủ nước
            - Nghỉ ngơi nếu mệt

            ## 💊 QUẢN LÝ THUỐC:

            **1. Cắt cơn:**
            - **Uống sớm:** Khi mới bắt đầu đau
            - Triptan: Không dùng quá 2-3 lần/tuần (tránh lạm dụng)
            - NSAID: Uống sau ăn (tránh đau dạ dày)

            **2. Phòng ngừa:**
            - Uống đều đặn, đúng giờ
            - Cần 2-3 tháng để thấy hiệu quả
            - Không tự ý ngừng

            **3. Tác dụng phụ:**
            - **Triptan:** Đau ngực, chóng mặt (hiếm)
            - **Propranolol:** Mệt mỏi, chóng mặt
            - **Topiramate:** Tê tay chân, giảm cân

            **4. Lưu ý:**
            - Tránh lạm dụng thuốc (có thể gây đau đầu do thuốc)
            - Báo bác sĩ nếu có tác dụng phụ

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Đau đầu báo động:**
            - Đau đầu đột ngột, dữ dội ("thunderclap")
            - Đau đầu kèm sốt, cổ cứng
            - Đau đầu sau chấn thương
            - Đau đầu kèm yếu liệt, rối loạn thị giác mới
            - Đau đầu ở người > 50 tuổi lần đầu

            **2. Migraine nặng:**
            - Đau > 72 giờ (status migrainosus)
            - Nôn nhiều, mất nước
            - Không đáp ứng điều trị

            **3. Tác dụng phụ thuốc:**
            - Đau ngực (Triptan)
            - Tác dụng phụ nặng

            ## 💡 PHÒNG NGỪA:

            **1. Tránh yếu tố kích thích:**
            - Ghi nhật ký đau đầu (tìm yếu tố kích thích)
            - Tránh thức ăn, mùi hương gây cơn
            - Quản lý stress

            **2. Lối sống:**
            - **Ngủ đủ giấc** (quan trọng!)
            - Ăn đều đặn, không bỏ bữa
            - Tập thể dục đều đặn
            - Uống đủ nước

            **3. Thuốc phòng ngừa:**
            - Nếu ≥ 4 cơn/tháng
            - Nếu cơn ảnh hưởng nhiều đến cuộc sống

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Khi có cơn đau:**
            - Nghỉ ngơi trong phòng tối, yên tĩnh
            - Uống thuốc sớm
            - Chườm lạnh trán
            - Ngủ (nếu có thể)

            **2. Sống tích cực:**
            - Migraine có thể kiểm soát
            - Điều trị đúng → Giảm tần suất, mức độ
            - Có thể sống bình thường

            **3. Hỗ trợ:**
            - Ghi nhật ký đau đầu
            - Tham gia nhóm hỗ trợ
            - Tư vấn tâm lý (nếu cần)

            **4. Mang thai:**
            - Một số thuốc không dùng được
            - Paracetamol an toàn
            - Triptan: Cần thận trọng
            - Tư vấn bác sĩ
            """,
            related_disease="migraine",
            related_drugs=["Sumatriptan", "Rizatriptan", "Ibuprofen", "Naproxen", "Propranolol", "Topiramate"],
            printable=True
        ),

        PatientEducationTopic(
            id="parkinson_disease_basics",
            title="Understanding Parkinson's Disease",
            title_vn="Hiểu về Bệnh Parkinson",
            category="Disease",
            content="""
            # Hiểu về Bệnh Parkinson

            ## Bệnh Parkinson là gì?

            Bệnh Parkinson là rối loạn thoái hóa thần kinh, đặc trưng bởi run, cứng cơ, chậm vận động, mất thăng bằng. Bệnh phổ biến ở người cao tuổi, ảnh hưởng đến vận động và chất lượng cuộc sống.

            **⚠️ Đặc điểm:**
            - Thoái hóa tế bào thần kinh sản xuất dopamine
            - Tiến triển từ từ
            - Phổ biến ở người cao tuổi (> 60 tuổi)
            - Không thể chữa khỏi, nhưng có thể kiểm soát

            **Triệu chứng chính (4 triệu chứng):**
            - Run (tremor)
            - Cứng cơ (rigidity)
            - Chậm vận động (bradykinesia)
            - Mất thăng bằng (postural instability)

            ## Triệu chứng:

            **Triệu chứng vận động:**
            - **Run:** Khi nghỉ, giảm khi vận động, thường bắt đầu một bên
            - **Cứng cơ:** Cứng khớp, đau cơ
            - **Chậm vận động:** Cử động chậm, khó khăn
            - **Mất thăng bằng:** Dễ ngã
            - **Dáng đi:** Bước nhỏ, không vung tay, khó quay đầu

            **Triệu chứng khác:**
            - Giảm biểu cảm mặt (mặt nạ)
            - Rối loạn giọng nói (nói nhỏ, đơn điệu)
            - Rối loạn nuốt
            - Rối loạn viết (chữ nhỏ)
            - Táo bón
            - Rối loạn giấc ngủ
            - Trầm cảm

            **⚠️ Giai đoạn muộn:**
            - Tàn tật
            - Suy giảm nhận thức
            - Rối loạn nuốt, viêm phổi hít

            ## Nguyên nhân:

            **1. Thoái hóa tế bào thần kinh:**
            - Tế bào sản xuất dopamine bị chết
            - Nguyên nhân chưa rõ

            **2. Yếu tố nguy cơ:**
            - Tuổi cao (> 60 tuổi)
            - Nam giới (tỷ lệ cao hơn nữ)
            - Tiền sử gia đình
            - Tiếp xúc thuốc trừ sâu, kim loại nặng

            ## Chẩn đoán:

            **Khám:**
            - Triệu chứng lâm sàng: ≥ 2 trong 4 triệu chứng chính
            - Đáp ứng với Levodopa
            - MRI não (loại trừ bệnh khác)

            ## Điều trị:

            **1. Levodopa/Carbidopa:**
            - Thuốc đầu tay
            - Bổ sung dopamine
            - Uống 3-4 lần/ngày

            **2. Dopamine agonist:**
            - Pramipexole, Ropinirole
            - Dùng sớm, trẻ tuổi

            **3. MAO-B inhibitor:**
            - Selegiline, Rasagiline
            - Làm chậm tiến triển

            **4. Vật lý trị liệu:**
            - Tập vận động
            - Tăng cường cơ
            - Cải thiện thăng bằng

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Protein:**
            - **Lưu ý:** Protein có thể giảm hấp thu Levodopa
            - Ăn protein cách xa uống thuốc 1 giờ
            - Hoặc ăn protein vào bữa tối

            **2. Chất xơ:**
            - Rau xanh, trái cây (phòng táo bón)
            - Uống nhiều nước

            **3. Tránh:**
            - Rượu bia (ảnh hưởng thuốc)
            - Caffeine quá nhiều (ảnh hưởng giấc ngủ)

            **4. Thực đơn mẫu:**
            - **Sáng:** Cháo/cơm, trứng (sau uống thuốc 1 giờ)
            - **Trưa:** Cơm, thịt/cá, rau xanh, canh
            - **Chiều:** Cơm, thịt/cá, rau xanh, canh
            - **Bữa phụ:** Trái cây, sữa

            ## 🏃 TẬP THỂ DỤC:

            **1. Quan trọng!**
            - Tập thể dục đều đặn (làm chậm tiến triển)
            - Tăng cường cơ, cải thiện thăng bằng

            **2. Loại bài tập:**
            - **Đi bộ:** 30 phút/ngày
            - **Tập tăng cường cơ:** Tạ nhẹ
            - **Tập thăng bằng:** Yoga, thái cực quyền
            - **Vật lý trị liệu:** Có hướng dẫn

            **3. Lưu ý:**
            - Tránh ngã (quan trọng!)
            - Tập nhẹ nhàng, tăng dần
            - Nghỉ ngơi nếu mệt

            ## 💊 QUẢN LÝ THUỐC:

            **1. Levodopa/Carbidopa:**
            - Uống 3-4 lần/ngày
            - Uống trước ăn 30 phút (hấp thu tốt hơn)
            - **Không uống với protein** (giảm hấp thu)

            **2. Tác dụng phụ:**
            - Buồn nôn (uống sau ăn nếu cần)
            - Rối loạn vận động (dyskinesia) - nếu dùng lâu
            - Ảo giác (hiếm)

            **3. Lưu ý:**
            - Uống đều đặn, đúng giờ
            - Không tự ý ngừng (nguy hiểm!)
            - Báo bác sĩ nếu có tác dụng phụ

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Ngã:**
            - Ngã, chấn thương
            - Gãy xương

            **2. Rối loạn nuốt:**
            - Khó nuốt, sặc
            - Viêm phổi hít

            **3. Tác dụng phụ nặng:**
            - Ảo giác
            - Rối loạn vận động nặng

            ## 💡 PHÒNG NGỪA:

            **1. Không có cách phòng ngừa:**
            - Nguyên nhân chưa rõ

            **2. Có thể giảm nguy cơ:**
            - Tránh tiếp xúc thuốc trừ sâu
            - Tập thể dục đều đặn
            - Ăn đủ dinh dưỡng

            **3. Phát hiện sớm:**
            - Khám khi có triệu chứng
            - Điều trị sớm → Tốt hơn

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Khi bị Parkinson:**
            - Uống thuốc đều đặn, đúng cách
            - Tập thể dục đều đặn (quan trọng!)
            - Vật lý trị liệu
            - Hỗ trợ gia đình

            **2. An toàn:**
            - Loại bỏ vật cản trong nhà
            - Tay vịn cầu thang, phòng tắm
            - Mang giày chắc chắn
            - Tránh ngã

            **3. Sống tích cực:**
            - Parkinson có thể kiểm soát
            - Điều trị đúng → Cải thiện triệu chứng
            - Có thể sống lâu, chất lượng cuộc sống tốt

            **4. Hỗ trợ:**
            - Tham gia nhóm hỗ trợ
            - Giáo dục gia đình
            - Tư vấn tâm lý (nếu cần)
            """,
            related_disease="parkinson_disease",
            related_drugs=["Levodopa", "Carbidopa", "Pramipexole", "Ropinirole", "Selegiline"],
            printable=True
        ),

]
