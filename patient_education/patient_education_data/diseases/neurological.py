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

        PatientEducationTopic(
            id="sciatica_basics",
            title="Understanding Sciatica",
            title_vn="Hiểu về Đau thần kinh tọa",
            category="Disease",
            content="""
            # Hiểu về Đau thần kinh tọa

            ## Đau thần kinh tọa là gì?

            Đau thần kinh tọa (Sciatica) là tình trạng đau dọc theo đường đi của dây thần kinh tọa (từ lưng dưới xuống chân), do chèn ép hoặc kích thích dây thần kinh. Bệnh rất phổ biến, ảnh hưởng đến 10-40% dân số ở một thời điểm nào đó.

            **⚠️ Đặc điểm:**
            - Đau dọc theo dây thần kinh tọa
            - Từ lưng dưới xuống mông, đùi sau, cẳng chân, bàn chân
            - Thường một bên
            - Rất phổ biến (10-40% dân số)

            **Dây thần kinh tọa:**
            - Dây thần kinh lớn nhất, dài nhất cơ thể
            - Từ cột sống thắt lưng (L4-S3) → Mông → Đùi sau → Cẳng chân → Bàn chân
            - Chi phối cảm giác, vận động chân

            **Phân loại:**
            - **Cấp tính:** < 6 tuần
            - **Bán cấp:** 6-12 tuần
            - **Mạn tính:** > 12 tuần

            ## Triệu chứng:

            **Triệu chứng điển hình:**
            - **Đau:** Đau dọc theo dây thần kinh tọa
              - Từ lưng dưới → Mông → Đùi sau → Cẳng chân → Bàn chân
              - Đau nhói, như điện giật, nóng rát
              - Thường một bên
            - **Tê, ngứa ran:** Dọc theo đường đi dây thần kinh
            - **Yếu cơ:** Yếu cơ chân (nếu nặng)
            - **Đau tăng:** Khi ngồi, ho, hắt hơi, rặn

            **Vị trí đau:**
            - **Lưng dưới:** Đau lưng dưới (có thể)
            - **Mông:** Đau mông, hông
            - **Đùi sau:** Đau đùi sau
            - **Cẳng chân:** Đau cẳng chân (trong hoặc ngoài)
            - **Bàn chân:** Đau bàn chân, ngón chân

            **Triệu chứng khác:**
            - Co cứng cơ lưng
            - Khó đứng, đi
            - Đau tăng khi ngồi lâu

            **⚠️ Dấu hiệu báo động (cần cấp cứu ngay!):**
            - **Hội chứng đuôi ngựa (Cauda Equina):**
              - Mất kiểm soát tiểu tiện, đại tiện
              - Tê vùng yên ngựa (vùng giữa hai chân)
              - Yếu chân nặng, liệt
              - **Cấp cứu ngay!**
            - **Yếu chân nặng:** Không đi được
            - **Mất cảm giác:** Mất cảm giác chân

            ## Nguyên nhân:

            **1. Thoát vị đĩa đệm (Phổ biến nhất, 90%):**
            - Đĩa đệm cột sống thắt lưng thoát vị
            - Chèn ép rễ thần kinh tọa
            - Thường L4-L5, L5-S1

            **2. Hẹp ống sống (Spinal Stenosis):**
            - Ống sống hẹp do thoái hóa
            - Chèn ép dây thần kinh
            - Thường người cao tuổi

            **3. Thoái hóa cột sống:**
            - Gai xương, thoái hóa đĩa đệm
            - Chèn ép rễ thần kinh

            **4. Trượt đốt sống (Spondylolisthesis):**
            - Đốt sống trượt ra trước
            - Chèn ép rễ thần kinh

            **5. Hội chứng cơ hình lê (Piriformis Syndrome):**
            - Cơ hình lê co thắt, chèn ép dây thần kinh tọa
            - Đau mông, lan xuống chân

            **6. Yếu tố nguy cơ:**
            - **Tuổi:** 30-50 tuổi
            - **Nghề nghiệp:** Ngồi lâu, khuân vác nặng
            - **Béo phì:** Tăng áp lực cột sống
            - **Ít vận động:** Yếu cơ lưng, bụng
            - **Mang giày cao gót:** Thay đổi tư thế
            - **Hút thuốc lá:** Làm chậm lành

            ## Chẩn đoán:

            **Chẩn đoán lâm sàng:**
            - Triệu chứng điển hình
            - Khám thần kinh

            **Khám:**
            - **Test Straight Leg Raise (SLR):** Nâng chân thẳng, đau tăng → Dương tính
            - **Khám cảm giác:** Tê, giảm cảm giác
            - **Khám vận động:** Yếu cơ
            - **Phản xạ:** Giảm phản xạ gân Achilles (S1)

            **Xét nghiệm:**
            - **X-quang:** Đánh giá cột sống
            - **MRI:** Phát hiện thoát vị đĩa đệm, hẹp ống sống (quan trọng!)
            - **CT:** Nếu không thể chụp MRI
            - **EMG:** Đánh giá chức năng dây thần kinh

            ## Điều trị:

            **1. Điều trị không phẫu thuật (90% cải thiện):**
            - **Nghỉ ngơi:** Nghỉ ngơi ngắn (1-2 ngày), không nằm lâu
            - **Thuốc giảm đau:**
              - **Paracetamol:** 500-1000mg, 3-4 lần/ngày
              - **NSAID:** Ibuprofen, Naproxen (giảm đau, viêm)
            - **Thuốc giãn cơ:** Cyclobenzaprine, Methocarbamol
            - **Thuốc giảm đau thần kinh:**
              - **Gabapentin, Pregabalin:** Giảm đau thần kinh
              - **Amitriptyline:** Giảm đau mạn tính
            - **Corticosteroid:** Prednisolone (ngắn hạn, nếu viêm nặng)
            - **Tiêm corticosteroid:** Tiêm ngoài màng cứng (giảm đau nhanh)

            **2. Vật lý trị liệu:**
            - **Kéo giãn:** Kéo giãn cơ lưng, mông, đùi sau
            - **Tăng cường cơ:** Tăng cường cơ lưng, bụng
            - **Tư thế:** Tư thế đúng
            - **Massage:** Massage cơ lưng, mông
            - **Nhiệt/Lạnh:** Chườm nóng/lạnh

            **3. Phẫu thuật (Chỉ khi cần):**
            - **Chỉ định:**
                - Hội chứng đuôi ngựa (cấp cứu!)
                - Yếu chân nặng, liệt
                - Không đáp ứng điều trị > 6 tháng
                - Đau nặng, không chịu được
            - **Phương pháp:**
                - **Cắt đĩa đệm (Discectomy):** Cắt đĩa đệm thoát vị
                - **Laminectomy:** Mở rộng ống sống
                - **Hợp nhất cột sống (Fusion):** Nếu trượt đốt sống

            **⚠️ Lưu ý:**
            - 90% cải thiện không cần phẫu thuật
            - Phẫu thuật chỉ khi cần thiết
            - Vật lý trị liệu quan trọng

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Thực phẩm chống viêm:**
            - **Cá béo:** Cá hồi, cá thu, cá mòi (Omega-3)
            - **Rau xanh:** Rau cải, rau bina, cải xoăn
            - **Trái cây:** Dâu, cam, bưởi (vitamin C)
            - **Quả hạch:** Hạnh nhân, óc chó
            - **Dầu oliu:** Dầu oliu nguyên chất

            **2. Thực phẩm giàu canxi, vitamin D:**
            - **Sữa, sữa chua:** Canxi
            - **Cá nhỏ:** Cá cơm, cá mòi (ăn cả xương)
            - **Rau xanh:** Cải xoăn, bông cải xanh
            - **Phơi nắng:** Vitamin D

            **3. Thực phẩm nên tránh:**
            - **Đồ chiên rán:** Tăng viêm
            - **Đường:** Tăng viêm
            - **Thực phẩm chế biến:** Thịt nguội, xúc xích
            - **Rượu bia:** Tăng viêm, làm chậm lành

            **4. Thực đơn mẫu:**
            - **Sáng:** Cháo yến mạch + sữa chua + trái cây
            - **Trưa:** Cơm + canh rau + cá + rau xanh
            - **Chiều:** Cơm + canh rau + cá + rau xanh
            - **Bữa phụ:** Quả hạch, trái cây

            **5. Lưu ý:**
            - Ăn đủ dinh dưỡng
            - Duy trì cân nặng hợp lý (giảm áp lực cột sống)
            - Uống nhiều nước

            ## 🏃 TẬP THỂ DỤC:

            **1. Khi đang đau:**
            - **Nghỉ ngơi ngắn:** 1-2 ngày, không nằm lâu
            - **Đi bộ nhẹ:** 10-15 phút, 2-3 lần/ngày
            - **Kéo giãn nhẹ:** Kéo giãn cơ lưng, mông, đùi sau
            - **Tránh:** Ngồi lâu, đứng lâu, khuân vác

            **2. Khi đã cải thiện:**
            - **Kéo giãn:** Kéo giãn cơ lưng, mông, đùi sau (quan trọng!)
            - **Tăng cường cơ lưng, bụng:**
              - Plank, bridge
              - Tăng cường cơ core
            - **Đi bộ:** 30 phút/ngày
            - **Bơi lội:** Tốt cho cột sống
            - **Yoga:** Tư thế kéo giãn, tăng cường

            **3. Bài tập kéo giãn:**
            - **Knee-to-chest:** Nằm ngửa, kéo gối lên ngực
            - **Piriformis stretch:** Kéo giãn cơ hình lê
            - **Hamstring stretch:** Kéo giãn cơ đùi sau
            - **Cat-cow:** Tư thế mèo-bò

            **4. Tránh:**
            - Ngồi lâu, đứng lâu
            - Khuân vác nặng
            - Tập quá sức
            - Tư thế sai

            ## 💊 QUẢN LÝ THUỐC:

            **1. Thuốc giảm đau:**
            - **Paracetamol:** 500-1000mg, 3-4 lần/ngày
            - **NSAID:** Ibuprofen 400-600mg, 3 lần/ngày (sau ăn)
            - **Lưu ý:** Không dùng quá 7-10 ngày (tránh tác dụng phụ)

            **2. Thuốc giảm đau thần kinh:**
            - **Gabapentin:** 300-600mg, 3 lần/ngày
            - **Pregabalin:** 75-150mg, 2 lần/ngày
            - **Tác dụng phụ:** Chóng mặt, buồn ngủ (ban đầu)
            - **Lưu ý:** Tăng liều từ từ

            **3. Thuốc giãn cơ:**
            - **Cyclobenzaprine:** 5-10mg, 3 lần/ngày
            - **Tác dụng phụ:** Buồn ngủ
            - **Lưu ý:** Dùng ngắn hạn (1-2 tuần)

            **4. Tiêm corticosteroid:**
            - Tiêm ngoài màng cứng
            - Giảm đau nhanh
            - Có thể lặp lại (nếu cần)

            **5. Lưu ý:**
            - Uống đúng liều, đúng giờ
            - Báo bác sĩ nếu có tác dụng phụ
            - Không tự ý tăng liều

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Hội chứng đuôi ngựa (CẤP CỨU NGAY!):**
            - Mất kiểm soát tiểu tiện, đại tiện
            - Tê vùng yên ngựa
            - Yếu chân nặng, liệt
            - **Cấp cứu ngay!**

            **2. Yếu chân nặng:**
            - Không đi được
            - Liệt chân
            - **Cấp cứu ngay!**

            **3. Đau nặng:**
            - Đau không chịu được
            - Không đáp ứng thuốc giảm đau

            **4. Không đáp ứng điều trị:**
            - Điều trị > 6 tuần không cải thiện
            - Đau tăng

            **5. Tái phát:**
            - Tái phát nhiều lần
            - Cần đánh giá thêm

            ## 💡 PHÒNG NGỪA:

            **1. Tư thế đúng:**
            - **Ngồi:** Ngồi thẳng lưng, chân chạm đất
            - **Đứng:** Đứng thẳng, trọng lượng đều hai chân
            - **Nâng vật:** Gập gối, không gập lưng
            - **Ngủ:** Nệm cứng vừa, gối phù hợp

            **2. Tập thể dục:**
            - **Tăng cường cơ lưng, bụng:** Quan trọng!
            - **Kéo giãn:** Kéo giãn cơ lưng, mông, đùi sau
            - **Đều đặn:** 30 phút/ngày

            **3. Tránh:**
            - Ngồi lâu, đứng lâu
            - Khuân vác nặng
            - Tư thế sai
            - Béo phì (tăng áp lực cột sống)

            **4. Lối sống:**
            - Duy trì cân nặng hợp lý
            - Bỏ thuốc lá
            - Quản lý stress

            **5. Nghề nghiệp:**
            - Đứng dậy mỗi 30-60 phút nếu ngồi lâu
            - Tư thế đúng khi khuân vác
            - Mang giày phù hợp

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Phòng ngừa:**
            - **Tư thế đúng** (quan trọng nhất!)
            - **Tăng cường cơ lưng, bụng**
            - **Tập thể dục đều đặn**

            **2. Khi bị đau thần kinh tọa:**
            - Nghỉ ngơi ngắn (1-2 ngày)
            - Dùng thuốc giảm đau
            - Vật lý trị liệu
            - Kéo giãn, tăng cường cơ

            **3. Sống tích cực:**
            - 90% cải thiện không cần phẫu thuật
            - Điều trị đúng → Cải thiện
            - Phòng ngừa tốt → Không tái phát

            **4. Kiên nhẫn:**
            - Điều trị cần thời gian (4-12 tuần)
            - Không nản lòng
            - Kết hợp nhiều biện pháp
            """,
            related_disease="sciatica",
            related_drugs=["Paracetamol", "Ibuprofen", "Gabapentin", "Pregabalin", "Cyclobenzaprine", "Prednisolone"],
            printable=True
        ),

        PatientEducationTopic(
            id="tension_headache_basics",
            title="Understanding Tension Headache",
            title_vn="Hiểu về Đau đầu căng thẳng",
            category="Disease",
            content="""
            # Hiểu về Đau đầu căng thẳng

            ## Đau đầu căng thẳng là gì?

            Đau đầu căng thẳng (Tension Headache) là loại đau đầu phổ biến nhất, đặc trưng bởi đau như bị bóp, căng ở cả hai bên đầu. Bệnh rất phổ biến, ảnh hưởng đến 70-80% dân số ở một thời điểm nào đó.

            **⚠️ Đặc điểm:**
            - Đau như bị bóp, căng
            - Cả hai bên đầu
            - Đau nhẹ đến vừa
            - Rất phổ biến (70-80% dân số)

            **Phân loại:**
            - **Đau đầu căng thẳng không thường xuyên:** < 1 ngày/tháng
            - **Đau đầu căng thẳng thường xuyên:** 1-14 ngày/tháng
            - **Đau đầu căng thẳng mạn tính:** ≥ 15 ngày/tháng, > 3 tháng

            ## Triệu chứng:

            **Triệu chứng điển hình:**
            - **Đau:** Đau như bị bóp, căng, đè ép
            - **Vị trí:** Cả hai bên đầu, trán, thái dương, sau gáy
            - **Cường độ:** Đau nhẹ đến vừa (không nặng như migraine)
            - **Đặc điểm:** Đau liên tục, không nhói
            - **Thời gian:** 30 phút đến vài ngày

            **Triệu chứng khác:**
            - Căng cứng cơ cổ, vai
            - Nhạy cảm ánh sáng, tiếng động (nhẹ, không như migraine)
            - Mệt mỏi
            - Khó tập trung

            **⚠️ Không có:**
            - Buồn nôn, nôn (có thể có nhẹ)
            - Nhạy cảm ánh sáng, tiếng động nặng (như migraine)
            - Đau tăng khi vận động (như migraine)

            **⚠️ Phân biệt với Migraine:**
            - **Đau đầu căng thẳng:** Đau cả hai bên, nhẹ-vừa, không nhói
            - **Migraine:** Đau một bên, nặng, nhói, kèm buồn nôn, nhạy cảm ánh sáng/tiếng động

            ## Nguyên nhân:

            **1. Căng cơ:**
            - **Cơ cổ, vai:** Căng cứng cơ cổ, vai
            - **Cơ đầu:** Cơ thái dương, cơ trán
            - **Tư thế sai:** Ngồi, đứng sai tư thế

            **2. Stress:**
            - **Căng thẳng:** Công việc, học tập, gia đình
            - **Lo âu:** Lo âu, sợ hãi
            - **Trầm cảm:** Trầm cảm

            **3. Yếu tố kích thích:**
            - **Thiếu ngủ:** Ngủ không đủ, mất ngủ
            - **Mệt mỏi:** Mệt mỏi, kiệt sức
            - **Đói:** Bỏ bữa, nhịn ăn
            - **Mất nước:** Uống ít nước
            - **Ánh sáng:** Ánh sáng chói, màn hình máy tính
            - **Tiếng ồn:** Tiếng ồn lớn
            - **Thời tiết:** Thay đổi thời tiết

            **4. Yếu tố nguy cơ:**
            - **Tuổi:** 20-50 tuổi
            - **Giới tính:** Phụ nữ (gấp 2 lần nam)
            - **Nghề nghiệp:** Công việc căng thẳng, ngồi lâu
            - **Tiền sử gia đình:** Có người thân bị đau đầu

            **5. Thuốc:**
            - Lạm dụng thuốc giảm đau (đau đầu do thuốc)

            ## Chẩn đoán:

            **Chẩn đoán lâm sàng:**
            - Triệu chứng điển hình
            - Không có dấu hiệu báo động

            **Tiêu chuẩn (ICHD-3):**
            - Đau đầu đáp ứng ít nhất 2 tiêu chuẩn:
              - Đau cả hai bên
              - Đau như bóp, căng (không nhói)
              - Đau nhẹ đến vừa
              - Không tăng khi vận động
            - Có thể kèm: Nhạy cảm ánh sáng/tiếng động (nhẹ), buồn nôn (nhẹ)
            - Không do bệnh khác

            **Khám:**
            - Khám thần kinh bình thường
            - Căng cứng cơ cổ, vai

            **Xét nghiệm:**
            - Thường không cần
            - CT/MRI nếu có dấu hiệu báo động

            **⚠️ Dấu hiệu báo động (cần khám ngay):**
            - Đau đầu đột ngột, dữ dội (thunderclap headache)
            - Đau đầu mới xuất hiện sau 50 tuổi
            - Đau đầu tăng dần
            - Đau đầu kèm sốt, cứng gáy
            - Đau đầu kèm yếu tay chân, rối loạn thị giác
            - Đau đầu sau chấn thương

            ## Điều trị:

            **1. Điều trị cấp tính:**
            - **Paracetamol:** 500-1000mg, có thể lặp lại sau 4-6 giờ
            - **NSAID:** Ibuprofen 400-600mg, Naproxen 250-500mg
            - **Aspirin:** 300-600mg (nếu không chống chỉ định)
            - **Kết hợp:** Paracetamol + Caffeine (tăng hiệu quả)

            **2. Điều trị phòng ngừa (Nếu đau thường xuyên, mạn tính):**
            - **Amitriptyline:** 10-75mg/ngày, tối
            - **Propranolol:** 40-160mg/ngày
            - **Topiramate:** 25-100mg/ngày
            - **Venlafaxine:** 37.5-150mg/ngày

            **3. Điều trị không dùng thuốc:**
            - **Vật lý trị liệu:** Massage, kéo giãn cơ cổ, vai
            - **Châm cứu:** Có thể giúp
            - **Thư giãn:** Thở sâu, thiền, yoga
            - **Biofeedback:** Phản hồi sinh học
            - **Tư vấn tâm lý:** Nếu stress, lo âu, trầm cảm

            **4. Thay đổi lối sống:**
            - Quản lý stress
            - Ngủ đủ giấc
            - Tập thể dục đều đặn
            - Tư thế đúng

            **⚠️ Lưu ý:**
            - Tránh lạm dụng thuốc giảm đau (đau đầu do thuốc)
            - Không dùng thuốc giảm đau > 10 ngày/tháng
            - Điều trị phòng ngừa nếu đau thường xuyên

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Thực phẩm nên ăn:**
            - **Rau xanh, trái cây:** Vitamin, chất chống oxy hóa
            - **Ngũ cốc nguyên hạt:** Ổn định đường huyết
            - **Protein nạc:** Thịt, cá, đậu
            - **Cá béo:** Omega-3 (giảm viêm)
            - **Nước:** Uống nhiều nước (2-3 lít/ngày)

            **2. Thực phẩm nên tránh:**
            - **Caffeine:** Cà phê, trà, nước ngọt (có thể gây đau đầu nếu lạm dụng)
            - **Rượu bia:** Có thể gây đau đầu
            - **Đường:** Đường, bánh kẹo (thay đổi đường huyết)
            - **Thực phẩm chế biến:** Thịt nguội, xúc xích (có thể chứa nitrite)
            - **Bỏ bữa:** Nhịn ăn, bỏ bữa (gây đau đầu)

            **3. Thực đơn mẫu:**
            - **Sáng:** Cháo yến mạch + trái cây + sữa chua
            - **Trưa:** Cơm + canh rau + thịt/cá + rau xanh
            - **Chiều:** Cơm + canh rau + thịt/cá + rau xanh
            - **Bữa phụ:** Trái cây, hạt
            - **Uống:** 2-3 lít nước/ngày

            **4. Lưu ý:**
            - Ăn đều đặn, không bỏ bữa
            - Uống nhiều nước
            - Tránh caffeine nếu có ảnh hưởng

            ## 🏃 TẬP THỂ DỤC:

            **1. Tập thể dục đều đặn:**
            - **Đi bộ:** 30 phút/ngày, 5 ngày/tuần
            - **Chạy bộ:** 20-30 phút/ngày
            - **Bơi lội:** Tốt cho cơ cổ, vai
            - **Yoga:** Kéo giãn, thư giãn
            - **Giảm đau đầu:** Tập thể dục đều đặn giảm tần suất đau đầu

            **2. Kéo giãn cơ cổ, vai:**
            - **Xoay cổ:** Xoay cổ nhẹ nhàng
            - **Kéo giãn cổ:** Nghiêng đầu sang hai bên
            - **Kéo giãn vai:** Nâng vai, thả lỏng
            - **5-10 phút, 2-3 lần/ngày**

            **3. Thư giãn:**
            - **Thở sâu:** Thở sâu, chậm
            - **Thiền:** 10-15 phút/ngày
            - **Yoga:** Tư thế thư giãn

            **4. Tránh:**
            - Tập quá sức (có thể gây đau đầu)
            - Tập khi đang đau đầu nặng

            ## 💊 QUẢN LÝ THUỐC:

            **1. Thuốc giảm đau cấp tính:**
            - **Paracetamol:** 500-1000mg, có thể lặp lại sau 4-6 giờ
            - **Ibuprofen:** 400-600mg, 3 lần/ngày (sau ăn)
            - **Naproxen:** 250-500mg, 2 lần/ngày
            - **Lưu ý:** Không dùng quá 10 ngày/tháng (tránh đau đầu do thuốc)

            **2. Thuốc phòng ngừa:**
            - **Amitriptyline:** 10-75mg/ngày, tối (bắt đầu 10mg, tăng dần)
            - **Propranolol:** 40-160mg/ngày
            - **Topiramate:** 25-100mg/ngày
            - **Uống đều đặn:** Theo chỉ định bác sĩ
            - **Thời gian:** 3-6 tháng

            **3. Tác dụng phụ:**
            - **Amitriptyline:** Buồn ngủ, khô miệng (ban đầu)
            - **Propranolol:** Mệt mỏi, chóng mặt
            - **Topiramate:** Chóng mặt, tê tay chân

            **4. Lưu ý:**
            - Tránh lạm dụng thuốc giảm đau
            - Điều trị phòng ngừa nếu đau thường xuyên
            - Báo bác sĩ nếu có tác dụng phụ

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Dấu hiệu báo động:**
            - Đau đầu đột ngột, dữ dội (thunderclap headache)
            - Đau đầu mới xuất hiện sau 50 tuổi
            - Đau đầu tăng dần
            - Đau đầu kèm sốt, cứng gáy
            - Đau đầu kèm yếu tay chân, rối loạn thị giác
            - Đau đầu sau chấn thương

            **2. Đau đầu nặng:**
            - Đau đầu không chịu được
            - Không đáp ứng thuốc giảm đau

            **3. Đau đầu thường xuyên:**
            - Đau đầu ≥ 15 ngày/tháng
            - Ảnh hưởng cuộc sống
            - Cần điều trị phòng ngừa

            **4. Đau đầu do thuốc:**
            - Lạm dụng thuốc giảm đau
            - Đau đầu tăng khi dùng thuốc
            - Cần cai thuốc

            ## 💡 PHÒNG NGỪA:

            **1. Quản lý stress:**
            - **Thư giãn:** Thở sâu, thiền, yoga
            - **Tư vấn:** Tư vấn tâm lý nếu cần
            - **Nghỉ ngơi:** Nghỉ ngơi đầy đủ

            **2. Ngủ đủ giấc:**
            - **7-9 giờ/đêm:** Ngủ đủ giấc
            - **Thói quen:** Đi ngủ, thức dậy cùng giờ
            - **Môi trường:** Phòng ngủ tối, yên tĩnh

            **3. Tập thể dục:**
            - Đều đặn, 30 phút/ngày
            - Giảm tần suất đau đầu

            **4. Tư thế:**
            - Ngồi, đứng đúng tư thế
            - Kéo giãn cơ cổ, vai thường xuyên

            **5. Tránh:**
            - Bỏ bữa, nhịn ăn
            - Mất nước
            - Lạm dụng caffeine, rượu bia
            - Lạm dụng thuốc giảm đau

            **6. Môi trường:**
            - Tránh ánh sáng chói
            - Tránh tiếng ồn lớn
            - Nghỉ giải lao khi làm việc với màn hình

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Phòng ngừa:**
            - **Quản lý stress** (quan trọng nhất!)
            - **Ngủ đủ giấc**
            - **Tập thể dục đều đặn**
            - **Tư thế đúng**

            **2. Khi bị đau đầu:**
            - Nghỉ ngơi, thư giãn
            - Dùng thuốc giảm đau (nếu cần)
            - Chườm lạnh/ấm
            - Massage cổ, vai

            **3. Sống tích cực:**
            - Đau đầu căng thẳng rất phổ biến
            - Có thể điều trị và phòng ngừa
            - Điều trị đúng → Giảm tần suất, cường độ

            **4. Ghi nhật ký:**
            - Ghi nhật ký đau đầu
            - Tìm yếu tố kích thích
            - Tránh yếu tố kích thích

            **5. Tránh lạm dụng thuốc:**
            - Không dùng thuốc giảm đau > 10 ngày/tháng
            - Điều trị phòng ngừa nếu đau thường xuyên
            """,
            related_disease="tension_headache",
            related_drugs=["Paracetamol", "Ibuprofen", "Amitriptyline", "Propranolol", "Topiramate"],
            printable=True
        ),

        PatientEducationTopic(
            id="meningitis_basics",
            title="Understanding Meningitis",
            title_vn="Hiểu về Viêm màng não",
            category="Disease",
            content="""
            # Hiểu về Viêm màng não

            ## Viêm màng não là gì?

            Viêm màng não (Meningitis) là tình trạng viêm của màng não (màng bao quanh não và tủy sống), thường do nhiễm trùng. Đây là cấp cứu thần kinh, cần điều trị ngay để tránh tử vong và di chứng.

            **⚠️ Đặc điểm:**
            - Viêm màng não
            - Thường do nhiễm trùng
            - Cấp cứu thần kinh
            - Cần điều trị ngay

            **Phân loại:**
            - **Viêm màng não do vi khuẩn:** Nặng, nguy hiểm tính mạng
            - **Viêm màng não do virus:** Thường nhẹ hơn, tự khỏi
            - **Viêm màng não do nấm:** Hiếm, thường ở người suy giảm miễn dịch
            - **Viêm màng não do lao:** Phổ biến ở vùng lưu hành lao

            ## Triệu chứng:

            **Triệu chứng điển hình:**
            - **Sốt:** Sốt cao, ớn lạnh
            - **Đau đầu:** Đau đầu dữ dội
            - **Cứng gáy:** Cứng gáy, không cúi được đầu
            - **Buồn nôn, nôn:** Buồn nôn, nôn (kiểu vọt)
            - **Nhạy cảm ánh sáng:** Nhạy cảm ánh sáng (photophobia)
            - **Lú lẫn:** Lú lẫn, rối loạn ý thức
            - **Phát ban:** Phát ban (một số loại vi khuẩn)

            **Triệu chứng ở trẻ em:**
            - Sốt cao
            - Quấy khóc, bỏ bú
            - Thóp phồng (trẻ nhỏ)
            - Co giật

            **⚠️ Dấu hiệu nặng:**
            - Hôn mê
            - Co giật
            - Sốc
            - **Cấp cứu ngay!**

            ## Nguyên nhân:

            **1. Vi khuẩn:**
            - **Neisseria meningitidis (Meningococcus):** Phổ biến, có thể gây dịch
            - **Streptococcus pneumoniae (Pneumococcus):** Phổ biến
            - **Haemophilus influenzae type B:** Phổ biến (trước khi có vắc xin)
            - **Listeria:** Ở trẻ sơ sinh, người cao tuổi, suy giảm miễn dịch

            **2. Virus:**
            - **Enterovirus:** Phổ biến nhất
            - **Herpes simplex:** Hiếm nhưng nặng
            - **Varicella zoster:** Thủy đậu
            - **Mumps:** Quai bị

            **3. Nấm:**
            - **Cryptococcus:** Ở người suy giảm miễn dịch
            - **Candida:** Hiếm

            **4. Lao:**
            - **Mycobacterium tuberculosis:** Phổ biến ở vùng lưu hành lao

            **5. Yếu tố nguy cơ:**
            - Trẻ em, người cao tuổi
            - Suy giảm miễn dịch
            - Chưa tiêm vắc xin
            - Tiếp xúc người bệnh

            ## Chẩn đoán:

            **Chẩn đoán lâm sàng:**
            - Triệu chứng điển hình
            - Khám thần kinh

            **Xét nghiệm:**
            - **Chọc dò tủy sống (LP):** Quan trọng nhất!
              - Dịch não tủy: Tăng bạch cầu, protein, giảm glucose
              - Cấy dịch não tủy: Xác định vi khuẩn
            - **Xét nghiệm máu:**
              - Bạch cầu tăng
              - CRP tăng
              - Cấy máu
            - **PCR:** Phát hiện virus, vi khuẩn

            **Hình ảnh:**
            - **CT não:** Trước khi chọc dò tủy sống (nếu có dấu hiệu tăng áp lực nội sọ)

            **⚠️ Phân biệt:**
            - Viêm não
            - Áp xe não
            - Xuất huyết dưới nhện

            ## Điều trị:

            **1. Viêm màng não do vi khuẩn:**
            - **Kháng sinh đường tĩnh mạch:** Ngay lập tức!
              - **Ceftriaxone + Vancomycin:** Phổ biến
              - **Penicillin G:** Nếu Meningococcus
              - **Ampicillin:** Nếu Listeria
            - **Corticosteroid:** Dexamethasone (giảm biến chứng)
            - **Thời gian:** 7-14 ngày

            **2. Viêm màng não do virus:**
            - **Hỗ trợ:** Không có thuốc đặc hiệu (hầu hết)
            - **Acyclovir:** Nếu Herpes simplex
            - **Nghỉ ngơi:** Tự khỏi

            **3. Viêm màng não do lao:**
            - **Điều trị lao:** 4 thuốc (Isoniazid, Rifampicin, Pyrazinamide, Ethambutol)
            - **Thời gian:** 6-12 tháng

            **4. Điều trị hỗ trợ:**
            - **Truyền dịch:** Truyền dịch đường tĩnh mạch
            - **Oxy:** Nếu khó thở
            - **Chống co giật:** Nếu co giật

            **⚠️ Lưu ý:**
            - Điều trị ngay lập tức (quan trọng!)
            - Không trì hoãn (nguy cơ tử vong, di chứng)
            - Viêm màng não do vi khuẩn: Nguy hiểm tính mạng

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Khi đang điều trị:**
            - **Nuôi ăn:** Nuôi ăn qua ống hoặc tĩnh mạch (nếu hôn mê)
            - **Khi đã tỉnh:** Ăn lỏng → Mềm → Bình thường

            **2. Thực phẩm nên ăn:**
            - Cháo, súp
            - Thức ăn mềm, dễ tiêu
            - Uống nhiều nước

            **3. Thực phẩm nên tránh:**
            - Đồ cay nóng
            - Thức ăn khó tiêu

            ## 🏃 TẬP THỂ DỤC:

            **1. Khi đang điều trị:**
            - Nghỉ ngơi hoàn toàn
            - Tránh gắng sức

            **2. Sau khi khỏi:**
            - Tập thể dục từ từ
            - Vật lý trị liệu (nếu có di chứng)
            - Tăng dần cường độ

            ## 💊 QUẢN LÝ THUỐC:

            **1. Kháng sinh:**
            - **Đường tĩnh mạch:** Ngay lập tức
            - **Uống đều đặn:** Theo chỉ định bác sĩ
            - **Đủ thời gian:** 7-14 ngày (vi khuẩn)

            **2. Corticosteroid:**
            - **Dexamethasone:** Giảm biến chứng
            - **Theo chỉ định bác sĩ**

            **3. Lưu ý:**
            - Uống đúng liều, đúng giờ
            - Không tự ý ngừng thuốc
            - Báo bác sĩ nếu có tác dụng phụ

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Triệu chứng viêm màng não:**
            - Sốt cao + Đau đầu dữ dội + Cứng gáy
            - **Cấp cứu ngay!**

            **2. Dấu hiệu nặng:**
            - Hôn mê
            - Co giật
            - Sốc
            - **Cấp cứu ngay!**

            **3. Trẻ em:**
            - Sốt cao + Quấy khóc + Bỏ bú
            - **Cấp cứu ngay!**

            ## 💡 PHÒNG NGỪA:

            **1. Tiêm vắc xin (QUAN TRỌNG NHẤT!):**
            - **Vắc xin Meningococcus:** Bảo vệ viêm màng não do Meningococcus
            - **Vắc xin Pneumococcus:** Bảo vệ viêm màng não do Pneumococcus
            - **Vắc xin Hib:** Bảo vệ viêm màng não do Hib
            - **Tiêm đầy đủ:** Theo lịch tiêm chủng

            **2. Tránh tiếp xúc:**
            - Tránh tiếp xúc người bệnh
            - Đeo khẩu trang
            - Rửa tay thường xuyên

            **3. Điều trị nhiễm trùng:**
            - Điều trị nhiễm trùng đúng cách
            - Giảm nguy cơ

            **4. Kháng sinh dự phòng:**
            - Nếu tiếp xúc người bệnh (Meningococcus)
            - Rifampicin, Ciprofloxacin

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Phòng ngừa:**
            - **Tiêm vắc xin** (quan trọng nhất!)
            - Tránh tiếp xúc người bệnh
            - Rửa tay thường xuyên

            **2. Khi có triệu chứng:**
            - **Đến bệnh viện ngay!** (quan trọng nhất!)
            - Không trì hoãn
            - Điều trị sớm → Giảm tử vong, di chứng

            **3. Sống tích cực:**
            - Viêm màng não do vi khuẩn: Nguy hiểm nhưng có thể điều trị
            - Điều trị sớm → Khỏi, không di chứng
            - Viêm màng não do virus: Thường tự khỏi

            **4. Di chứng:**
            - Một số trường hợp có thể có di chứng (điếc, liệt, chậm phát triển)
            - Cần vật lý trị liệu, phục hồi chức năng
            """,
            related_disease="meningitis",
            related_drugs=["Ceftriaxone", "Vancomycin", "Penicillin G", "Ampicillin", "Dexamethasone", "Acyclovir"],
            printable=True
        ),

        PatientEducationTopic(
            id="alzheimer_disease_basics",
            title="Understanding Alzheimer's Disease",
            title_vn="Hiểu về Bệnh Alzheimer",
            category="Disease",
            content="""
            # Hiểu về Bệnh Alzheimer

            ## Bệnh Alzheimer là gì?

            Bệnh Alzheimer là bệnh thoái hóa thần kinh mạn tính, gây mất trí nhớ, suy giảm nhận thức, ảnh hưởng đến cuộc sống hàng ngày. Đây là nguyên nhân phổ biến nhất của sa sút trí tuệ ở người cao tuổi.

            **⚠️ Đặc điểm:**
            - Bệnh thoái hóa thần kinh mạn tính
            - Gây mất trí nhớ, suy giảm nhận thức
            - Nguyên nhân phổ biến nhất của sa sút trí tuệ
            - Không chữa khỏi, tiến triển dần

            **Phân loại:**
            - **Alzheimer khởi phát sớm:** < 65 tuổi (hiếm, 5%)
            - **Alzheimer khởi phát muộn:** > 65 tuổi (phổ biến, 95%)

            **Giai đoạn:**
            - **Giai đoạn nhẹ:** Mất trí nhớ nhẹ, vẫn sống độc lập
            - **Giai đoạn trung bình:** Mất trí nhớ nặng, cần hỗ trợ
            - **Giai đoạn nặng:** Mất trí nhớ nặng, cần chăm sóc toàn thời gian

            ## Triệu chứng:

            **Giai đoạn nhẹ:**
            - **Mất trí nhớ:** Quên những việc vừa xảy ra, lặp lại câu hỏi
            - **Khó nhớ tên:** Khó nhớ tên người, đồ vật
            - **Mất phương hướng:** Mất phương hướng ở nơi quen thuộc
            - **Khó lập kế hoạch:** Khó lập kế hoạch, giải quyết vấn đề
            - **Thay đổi tâm trạng:** Thay đổi tâm trạng, tính cách

            **Giai đoạn trung bình:**
            - **Mất trí nhớ nặng:** Quên tên người thân, sự kiện quan trọng
            - **Lú lẫn:** Lú lẫn về thời gian, địa điểm
            - **Khó giao tiếp:** Khó giao tiếp, tìm từ
            - **Thay đổi hành vi:** Kích động, lo âu, trầm cảm
            - **Mất kỹ năng:** Mất kỹ năng sống hàng ngày

            **Giai đoạn nặng:**
            - **Mất trí nhớ hoàn toàn:** Không nhớ gì
            - **Mất khả năng giao tiếp:** Không nói được
            - **Mất khả năng vận động:** Không đi được, nằm liệt giường
            - **Mất khả năng tự chăm sóc:** Cần chăm sóc toàn thời gian
            - **Nhiễm trùng:** Nhiễm trùng (viêm phổi, nhiễm trùng đường tiểu)

            **⚠️ Phân biệt với quên bình thường:**
            - **Quên bình thường:** Quên tạm thời, nhớ lại sau
            - **Alzheimer:** Quên vĩnh viễn, không nhớ lại

            ## Nguyên nhân:

            **1. Nguyên nhân chưa rõ hoàn toàn:**
            - Có nhiều yếu tố

            **2. Yếu tố:**
            - **Tích tụ protein:** Beta-amyloid, Tau protein
            - **Mất tế bào thần kinh:** Mất tế bào thần kinh
            - **Viêm:** Viêm mạn tính trong não

            **3. Yếu tố nguy cơ:**
            - **Tuổi:** > 65 tuổi (tăng nguy cơ theo tuổi)
            - **Di truyền:** Có người thân bị Alzheimer (tăng nguy cơ)
            - **Gen APOE4:** Tăng nguy cơ
            - **Bệnh tim mạch:** Tăng huyết áp, đái tháo đường
            - **Chấn thương đầu:** Chấn thương đầu nặng
            - **Ít hoạt động trí não:** Ít học, ít đọc

            **4. Yếu tố bảo vệ:**
            - **Hoạt động trí não:** Đọc, học, chơi game
            - **Tập thể dục:** Tập thể dục đều đặn
            - **Chế độ ăn:** Chế độ ăn lành mạnh
            - **Giao tiếp xã hội:** Giao tiếp xã hội

            ## Chẩn đoán:

            **Chẩn đoán lâm sàng:**
            - Triệu chứng điển hình
            - Khám thần kinh, tâm thần

            **Xét nghiệm:**
            - **Test nhận thức:** MMSE, MoCA (đánh giá nhận thức)
            - **Xét nghiệm máu:** Loại trừ nguyên nhân khác
            - **Chọc dò tủy sống:** Beta-amyloid, Tau (nếu cần)

            **Hình ảnh:**
            - **CT/MRI não:** Loại trừ nguyên nhân khác (khối u, đột quỵ)
            - **PET scan:** Phát hiện tích tụ beta-amyloid (nếu có)

            **⚠️ Phân biệt:**
            - Sa sút trí tuệ do mạch máu
            - Sa sút trí tuệ do Parkinson
            - Trầm cảm (giả sa sút trí tuệ)

            ## Điều trị:

            **1. Thuốc điều trị triệu chứng:**
            - **Cholinesterase inhibitor:**
              - **Donepezil:** 5-10mg/ngày
              - **Rivastigmine:** 1.5-6mg, 2 lần/ngày
              - **Galantamine:** 8-24mg, 2 lần/ngày
              - Cải thiện nhận thức, chức năng
            - **Memantine:** 10-20mg, 2 lần/ngày (giai đoạn trung bình-nặng)
            - **Hiệu quả:** Cải thiện nhẹ, không chữa khỏi

            **2. Điều trị hành vi:**
            - **Thuốc chống trầm cảm:** Nếu trầm cảm
            - **Thuốc an thần:** Nếu kích động (thận trọng)

            **3. Điều trị không dùng thuốc:**
            - **Hoạt động trí não:** Đọc, học, chơi game
            - **Tập thể dục:** Tập thể dục đều đặn
            - **Giao tiếp xã hội:** Giao tiếp xã hội
            - **Vật lý trị liệu:** Duy trì vận động
            - **Tư vấn:** Tư vấn cho bệnh nhân, gia đình

            **⚠️ Lưu ý:**
            - Không có cách chữa khỏi
            - Điều trị chỉ làm chậm tiến triển
            - Chăm sóc hỗ trợ quan trọng

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Chế độ ăn lành mạnh:**
            - **Chế độ ăn Địa Trung Hải:** Cá, rau xanh, dầu oliu
            - **Chế độ ăn DASH:** Giảm muối, tăng rau xanh
            - **Chất chống oxy hóa:** Rau xanh, trái cây

            **2. Thực phẩm nên ăn:**
            - Cá béo (omega-3)
            - Rau xanh, trái cây
            - Ngũ cốc nguyên hạt
            - Dầu oliu
            - Quả hạch

            **3. Thực phẩm nên tránh:**
            - Thịt đỏ, mỡ động vật
            - Đồ chiên rán
            - Đường, đồ ngọt
            - Rượu bia

            **4. Lưu ý:**
            - Ăn đủ dinh dưỡng
            - Tránh quên ăn
            - Hỗ trợ ăn uống (nếu cần)

            ## 🏃 TẬP THỂ DỤC:

            **1. Tập thể dục đều đặn:**
            - **Đi bộ:** 30 phút/ngày, 5 ngày/tuần
            - **Tập sức mạnh:** Tập sức mạnh nhẹ
            - **Giảm tiến triển:** Tập thể dục làm chậm tiến triển

            **2. Hoạt động trí não:**
            - **Đọc sách:** Đọc sách, báo
            - **Chơi game:** Chơi game trí tuệ
            - **Học:** Học điều mới
            - **Giao tiếp:** Giao tiếp xã hội

            **3. Lưu ý:**
            - Tập thể dục an toàn
            - Tránh ngã
            - Có người giám sát (nếu cần)

            ## 💊 QUẢN LÝ THUỐC:

            **1. Cholinesterase inhibitor:**
            - **Donepezil:** Uống buổi tối
            - **Rivastigmine:** Uống 2 lần/ngày (sáng, tối)
            - **Galantamine:** Uống 2 lần/ngày (sáng, tối)
            - **Tác dụng phụ:** Buồn nôn, tiêu chảy (ban đầu)

            **2. Memantine:**
            - **Uống 2 lần/ngày:** Sáng, tối
            - **Tác dụng phụ:** Chóng mặt, đau đầu (hiếm)

            **3. Lưu ý:**
            - Uống đúng liều, đúng giờ
            - Có người giám sát (nếu cần)
            - Báo bác sĩ nếu có tác dụng phụ

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Thay đổi đột ngột:**
            - Thay đổi đột ngột về nhận thức, hành vi
            - Cần đánh giá

            **2. Biến chứng:**
            - Nhiễm trùng (viêm phổi, nhiễm trùng đường tiểu)
            - Ngã, chấn thương
            - Suy dinh dưỡng

            **3. Hành vi nguy hiểm:**
            - Kích động, bạo lực
            - Tự làm hại

            ## 💡 PHÒNG NGỪA:

            **1. Hoạt động trí não:**
            - **Đọc sách:** Đọc sách, báo thường xuyên
            - **Học:** Học điều mới
            - **Chơi game:** Chơi game trí tuệ
            - **Giao tiếp:** Giao tiếp xã hội

            **2. Tập thể dục:**
            - Tập thể dục đều đặn, 30 phút/ngày
            - Giảm nguy cơ

            **3. Chế độ ăn:**
            - Chế độ ăn lành mạnh
            - Cá béo, rau xanh

            **4. Kiểm soát yếu tố nguy cơ:**
            - Kiểm soát huyết áp
            - Kiểm soát đái tháo đường
            - Bỏ thuốc lá

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Phòng ngừa:**
            - **Hoạt động trí não** (quan trọng nhất!)
            - Tập thể dục đều đặn
            - Chế độ ăn lành mạnh

            **2. Khi bị Alzheimer:**
            - Điều trị sớm (quan trọng!)
            - Uống thuốc đều đặn
            - Hoạt động trí não, tập thể dục
            - Hỗ trợ gia đình

            **3. Chăm sóc:**
            - Cần chăm sóc hỗ trợ
            - An toàn (tránh ngã, lạc)
            - Dinh dưỡng đủ
            - Giao tiếp, yêu thương

            **4. Sống tích cực:**
            - Alzheimer không chữa khỏi nhưng có thể làm chậm tiến triển
            - Điều trị đúng → Cải thiện chất lượng cuộc sống
            - Hỗ trợ gia đình → Giảm gánh nặng

            **5. Gia đình:**
            - Cần hỗ trợ, giáo dục
            - Tham gia nhóm hỗ trợ
            - Tư vấn tâm lý (nếu cần)
            """,
            related_disease="alzheimer_disease",
            related_drugs=["Donepezil", "Rivastigmine", "Galantamine", "Memantine"],
            printable=True
        ),

]
