"""
Patient Education Topics - Rheumatology
"""
from patient_education.models import PatientEducationTopic


RHEUMATOLOGY_TOPICS = [
        PatientEducationTopic(
            id="osteoarthritis_basics",
            title="Understanding Osteoarthritis",
            title_vn="Hiểu về Thoái hóa khớp",
            category="Disease",
            content="""
    # Hiểu về Thoái hóa khớp

    ## Thoái hóa khớp là gì?

    Thoái hóa khớp là tình trạng sụn khớp bị mòn, gây đau và cứng khớp.

    ## Triệu chứng:
    - Đau khớp (tăng khi vận động)
    - Cứng khớp (đặc biệt buổi sáng)
    - Sưng khớp
    - Giảm vận động
    - Có tiếng kêu trong khớp

    ## Khớp thường bị:
    - Gối
    - Hông
    - Cột sống
    - Ngón tay
    - Cổ tay

    ## Nguyên nhân:
    - Tuổi cao
    - Chấn thương cũ
    - Béo phì
    - Di truyền
    - Vận động quá mức

    ## Điều trị:
    - **Giảm đau:** Paracetamol, NSAID
    - **Vật lý trị liệu:** Tập thể dục, kéo giãn
    - **Giảm cân** (nếu thừa cân)
    - **Tiêm khớp** (nếu cần)
    - **Phẫu thuật** (nếu nặng)

    ## Tập thể dục:
    - **Quan trọng!** Giúp giảm đau, tăng vận động
    - Đi bộ, bơi, đạp xe
    - Tập kéo giãn
    - Tránh vận động mạnh, chấn thương

    ## Lời khuyên:
    - Tập thể dục đều đặn
    - Giảm cân nếu thừa cân
    - Dùng thuốc giảm đau khi cần
    - Tránh vận động quá mức
    - Vật lý trị liệu
    - Khám định kỳ
            """,
            related_disease="osteoarthritis",
            related_drugs=["Paracetamol", "Ibuprofen", "Diclofenac"],
            printable=True
        ),

        PatientEducationTopic(
            id="rheumatoid_arthritis_basics",
            title="Understanding Rheumatoid Arthritis",
            title_vn="Hiểu về Viêm khớp dạng thấp",
            category="Disease",
            content="""
            # Hiểu về Viêm khớp dạng thấp

            ## Viêm khớp dạng thấp là gì?

            Viêm khớp dạng thấp (Rheumatoid Arthritis - RA) là bệnh tự miễn mạn tính, gây viêm khớp đối xứng, dẫn đến đau, sưng, cứng khớp và có thể gây biến dạng khớp.

            **⚠️ Đặc điểm:**
            - Bệnh tự miễn (hệ miễn dịch tấn công khớp)
            - Mạn tính, tiến triển
            - Ảnh hưởng nhiều khớp (đối xứng)
            - Có thể ảnh hưởng các cơ quan khác
            - Nữ mắc nhiều hơn nam (2-3 lần)

            **Phân biệt với thoái hóa khớp:**
            - **RA:** Viêm, đau cả khi nghỉ, cứng khớp buổi sáng > 1 giờ, đối xứng
            - **Thoái hóa khớp:** Không viêm, đau khi vận động, cứng khớp < 30 phút, không đối xứng

            ## Triệu chứng:

            **Triệu chứng khớp:**
            - **Đau khớp:** Đau cả khi nghỉ, đau nhiều về đêm, sáng sớm
            - **Sưng khớp:** Sưng, nóng, đỏ
            - **Cứng khớp buổi sáng:** > 1 giờ (đặc trưng!)
            - **Vị trí:** Thường khớp nhỏ (bàn tay, bàn chân), đối xứng
            - **Biến dạng khớp:** Khi bệnh nặng, lâu ngày

            **Triệu chứng toàn thân:**
            - **Mệt mỏi:** Uể oải, không có sức
            - **Sốt nhẹ:** Có thể có
            - **Sụt cân:** Không rõ nguyên nhân
            - **Chán ăn**

            **Triệu chứng ngoài khớp:**
            - **Nốt thấp khớp:** Dưới da (khuỷu tay, gót chân)
            - **Viêm mạch máu:** Có thể có
            - **Viêm màng phổi, màng tim:** (Hiếm)
            - **Tổn thương mắt:** (Hiếm)

            **⚠️ Phân độ:**
            - **Độ 1:** Đau, sưng nhẹ
            - **Độ 2:** Đau, sưng vừa, hạn chế vận động
            - **Độ 3:** Đau, sưng nặng, biến dạng khớp
            - **Độ 4:** Mất chức năng khớp, dính khớp

            ## Nguyên nhân:

            **1. Nguyên nhân:**
            - **Tự miễn:** Hệ miễn dịch tấn công khớp
            - **Nguyên nhân chưa rõ:** Có thể do gen + môi trường

            **2. Yếu tố nguy cơ:**
            - **Giới tính:** Nữ (2-3 lần nam)
            - **Tuổi:** 40-60 tuổi
            - **Di truyền:** Có người thân bị RA
            - **Hút thuốc lá:** Tăng nguy cơ
            - **Béo phì:** Tăng nguy cơ
            - **Nhiễm trùng:** Một số virus, vi khuẩn có thể kích hoạt

            ## Chẩn đoán:

            **1. Khám lâm sàng:**
            - Đánh giá khớp: Đau, sưng, cứng
            - Số khớp bị ảnh hưởng
            - Đối xứng

            **2. Xét nghiệm:**
            - **RF (Rheumatoid Factor):** Dương tính (70-80%)
            - **Anti-CCP:** Chính xác hơn RF
            - **CRP, ESR:** Tăng (dấu hiệu viêm)
            - **Công thức máu:** Thiếu máu (có thể)

            **3. X-quang:**
            - Tổn thương khớp
            - Mòn xương, hẹp khe khớp

            ## Điều trị:

            **⚠️ QUAN TRỌNG:** Điều trị sớm → Giảm tổn thương khớp, biến chứng!

            **1. Thuốc giảm đau, chống viêm:**
            - **NSAID:** Ibuprofen, Naproxen, Diclofenac
              - Giảm đau, viêm nhanh
              - Dùng khi có triệu chứng
            - **Corticosteroid:** Prednisone
              - Giảm viêm mạnh
              - Dùng ngắn hạn, liều thấp

            **2. DMARDs (Disease-Modifying Antirheumatic Drugs):**
            - **Methotrexate:** Thuốc đầu tay
            - **Sulfasalazine, Hydroxychloroquine**
            - **Leflunomide**
            - **⚠️ QUAN TRỌNG:** Uống lâu dài, giúp làm chậm tiến triển bệnh

            **3. Thuốc sinh học:**
            - **TNF-alpha inhibitors:** Etanercept, Adalimumab
            - **Rituximab, Tocilizumab**
            - Dùng khi DMARDs không hiệu quả
            - Đắt, cần theo dõi sát

            **4. Phục hồi chức năng:**
            - Vật lý trị liệu
            - Hoạt động trị liệu
            - Tập thể dục

            **5. Phẫu thuật:**
            - Thay khớp (nếu tổn thương nặng)
            - Hiếm, chỉ khi cần

            ## 🍽️ CHẾ ĐỘ ĂN CHO NGƯỜI VIÊM KHỚP DẠNG THẤP:

            **1. Nguyên tắc:**
            - **Chống viêm:** Thực phẩm chống viêm
            - **Đủ dinh dưỡng:** Giúp cơ thể chống lại bệnh
            - **Giảm cân:** Nếu thừa cân (giảm áp lực khớp)
            - **Tránh thực phẩm gây viêm**

            **2. Thực phẩm NÊN ĂN (Chống viêm):**
            - **Cá béo:** Cá hồi, cá thu, cá trích (omega-3, 2-3 lần/tuần)
              - Giúp giảm viêm
            - **Rau xanh:** Nhiều (rau cải, rau muống, bông cải)
              - Chất chống oxy hóa, chống viêm
            - **Trái cây:** Tất cả (đặc biệt quả mọng, cam, bưởi)
              - Vitamin C, chất chống oxy hóa
            - **Ngũ cốc nguyên hạt:** Gạo lứt, yến mạch, bánh mì đen
            - **Đậu, đậu phụ:** Protein thực vật
            - **Dầu ô liu:** Chất béo tốt, chống viêm
            - **Các loại hạt:** Hạnh nhân, óc chó (nếu có)
            - **Gia vị:** Nghệ, gừng (chống viêm)

            **3. Thực phẩm CẦN TRÁNH (Gây viêm):**
            - **Thịt đỏ nhiều:** Thịt bò, thịt heo (ăn ít)
            - **Thực phẩm chế biến sẵn:** Đồ hộp, thức ăn nhanh
            - **Đồ chiên, nhiều dầu mỡ:** Chất béo bão hòa
            - **Đường nhiều:** Bánh kẹo, nước ngọt
            - **Rượu bia:** Làm tăng viêm
            - **Gluten:** Một số người nhạy cảm (thử kiêng xem có cải thiện không)

            **4. Thực đơn mẫu (1 ngày):**
            - **Sáng:** Cháo yến mạch + sữa ít béo + trái cây
            - **Trưa:** 1 chén cơm gạo lứt + cá hồi hấp + rau luộc + canh rau
            - **Tối:** 1 chén cơm gạo lứt + đậu phụ xào + rau xào (dầu ô liu) + canh
            - **Bữa phụ:** Trái cây, các loại hạt, sữa chua

            **5. Lưu ý:**
            - Ăn đủ chất, không kiêng khem quá mức
            - Thử loại bỏ một số thực phẩm xem có cải thiện không (mỗi người khác nhau)
            - Ghi nhật ký ăn uống và triệu chứng

            ## 🏃 TẬP THỂ DỤC:

            **⚠️ QUAN TRỌNG:** Tập thể dục giúp duy trì chức năng khớp, giảm cứng khớp!

            **1. Khi đang viêm (đau, sưng):**
            - **Nghỉ ngơi:** Không tập thể dục
            - **Vận động nhẹ:** Cử động khớp nhẹ nhàng (tránh cứng khớp)
            - **Chườm lạnh:** Giảm sưng, đau

            **2. Khi không viêm (ổn định):**
            - **Tập thể dục nhẹ nhàng:** Đi bộ, bơi, đạp xe
            - **Tập linh hoạt:** Duỗi, gập khớp
            - **Tập sức mạnh:** Nhẹ, với dây kháng lực
            - **Yoga, thái cực quyền:** Tốt cho khớp

            **3. Thời gian và tần suất:**
            - **30 phút/ngày:** Ít nhất 5 ngày/tuần
            - **Chia nhỏ:** 3 lần x 10 phút/ngày (nếu cần)
            - **Cường độ:** Vừa phải, không gắng sức

            **4. Lưu ý:**
            - Khởi động trước tập
            - Nghỉ khi đau
            - Dừng ngay nếu: Đau tăng, sưng tăng
            - Tập đều đặn, không bỏ

            **5. Lợi ích:**
            - Duy trì chức năng khớp
            - Giảm cứng khớp
            - Tăng sức mạnh cơ
            - Giảm đau
            - Cải thiện tâm trạng

            ## 💊 QUẢN LÝ THUỐC:

            **⚠️ QUAN TRỌNG:** Uống thuốc đúng giờ, đủ liều, không tự ý ngừng!

            **1. NSAID:**
            - **Khi nào dùng:** Khi có đau, viêm
            - **Uống sau ăn:** Tránh đau dạ dày
            - **Không dùng lâu dài:** Tăng nguy cơ đau dạ dày, thận

            **2. DMARDs (Methotrexate):**
            - **Uống hàng ngày/tuần:** Theo chỉ định
            - **Uống lâu dài:** Để làm chậm tiến triển
            - **Không tự ý ngừng:** Ngừng → Bệnh nặng hơn
            - **Tác dụng phụ:** Buồn nôn, rụng tóc, tổn thương gan (theo dõi định kỳ)
            - **Folic acid:** Uống kèm để giảm tác dụng phụ

            **3. Corticosteroid:**
            - **Dùng ngắn hạn:** Liều thấp
            - **Không tự ý ngừng:** Phải giảm liều từ từ
            - **Tác dụng phụ:** Tăng cân, loãng xương, tăng đường huyết

            **4. Tác dụng phụ:**
            - Báo bác sĩ nếu: Tác dụng phụ nghiêm trọng
            - Khám định kỳ: Xét nghiệm máu, chức năng gan, thận

            ## 🛡️ PHÒNG NGỪA VÀ QUẢN LÝ:

            **1. Điều trị sớm:**
            - Phát hiện sớm → Điều trị sớm → Giảm tổn thương khớp
            - "Window of opportunity": 3-6 tháng đầu

            **2. Tuân thủ điều trị:**
            - Uống thuốc đúng giờ, đủ liều
            - Không tự ý ngừng
            - Tái khám định kỳ

            **3. Lối sống:**
            - Bỏ thuốc lá (quan trọng!)
            - Giảm cân nếu thừa cân
            - Tập thể dục đều đặn
            - Quản lý stress

            **4. Bảo vệ khớp:**
            - Tránh gắng sức quá mức
            - Dùng dụng cụ hỗ trợ nếu cần
            - Nghỉ giữa các hoạt động

            **5. Khám định kỳ:**
            - Mỗi 1-3 tháng: Đánh giá điều trị
            - Xét nghiệm máu: Chức năng gan, thận
            - X-quang: Đánh giá tổn thương khớp

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Đợt cấp:**
            - Đau, sưng khớp nặng
            - Sốt cao
            - Không đáp ứng với thuốc

            **2. Biến chứng:**
            - Nhiễm trùng (do thuốc ức chế miễn dịch)
            - Tổn thương nội tạng

            **3. Tác dụng phụ thuốc:**
            - Nghiêm trọng, không chịu được

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Khi mới chẩn đoán:**
            - Đừng lo lắng quá mức
            - RA có thể kiểm soát được
            - Điều trị sớm → Kết quả tốt

            **2. Tuân thủ điều trị:**
            - Uống thuốc đúng giờ, đủ liều
            - Không tự ý ngừng
            - Tái khám định kỳ

            **3. Lối sống:**
            - Tập thể dục đều đặn
            - Chế độ ăn chống viêm
            - Bỏ thuốc lá
            - Quản lý stress

            **4. Hỗ trợ:**
            - Nói với gia đình về bệnh
            - Tham gia nhóm hỗ trợ (nếu có)
            - Tâm lý trị liệu nếu cần

            **5. Sống tích cực:**
            - RA có thể kiểm soát được
            - Tuân thủ điều trị → Sống bình thường
            - Đừng để bệnh ảnh hưởng cuộc sống
            """,
            related_disease="rheumatoid_arthritis",
            related_drugs=["Methotrexate", "Ibuprofen", "Prednisone"],
            printable=True
        ),

        PatientEducationTopic(
            id="osteoporosis_basics",
            title="Understanding Osteoporosis",
            title_vn="Hiểu về Loãng xương",
            category="Disease",
            content="""
            # Hiểu về Loãng xương

            ## Loãng xương là gì?

            Loãng xương là tình trạng giảm mật độ xương, tăng nguy cơ gãy xương, phổ biến ở phụ nữ sau mãn kinh và người cao tuổi. Bệnh thường không có triệu chứng cho đến khi gãy xương.

            **⚠️ Đặc điểm:**
            - Giảm mật độ xương
            - Tăng nguy cơ gãy xương
            - Phổ biến ở phụ nữ sau mãn kinh
            - Thường không có triệu chứng (cho đến khi gãy xương)

            **Phân loại:**
            - **Giảm mật độ xương (Osteopenia):** T-score -1.0 đến -2.5
            - **Loãng xương:** T-score ≤ -2.5

            ## Triệu chứng:

            **Giai đoạn sớm:**
            - Thường không có triệu chứng

            **Giai đoạn muộn:**
            - **Đau lưng:** Nếu gãy đốt sống
            - **Giảm chiều cao:** Do gãy đốt sống
            - **Gù lưng:** Do gãy nhiều đốt sống
            - **Gãy xương sau chấn thương nhẹ:**
              - Cổ xương đùi (nguy hiểm nhất)
              - Đốt sống
              - Cổ tay

            **⚠️ Gãy xương:**
            - Đau dữ dội
            - Biến dạng
            - Mất chức năng

            ## Nguyên nhân:

            **1. Tuổi cao:**
            - Mất xương tự nhiên theo tuổi

            **2. Mãn kinh (phụ nữ):**
            - Giảm estrogen → Mất xương nhanh

            **3. Thiếu canxi, vitamin D:**
            - Chế độ ăn thiếu
            - Ít tiếp xúc ánh nắng

            **4. Ít vận động:**
            - Xương cần tải trọng để chắc khỏe

            **5. Yếu tố khác:**
            - Hút thuốc, rượu bia
            - Thuốc: Corticosteroid
            - Bệnh: Cường giáp, suy thận

            ## Chẩn đoán:

            **Xét nghiệm:**
            - **DEXA scan:** Đo mật độ xương (chuẩn vàng)
            - **T-score:** ≤ -2.5 (loãng xương)
            - Canxi, vitamin D, PTH
            - **FRAX score:** Đánh giá nguy cơ gãy xương

            ## Điều trị:

            **1. Bổ sung:**
            - **Canxi:** 1000-1200 mg/ngày
            - **Vitamin D:** 800-1000 IU/ngày

            **2. Thuốc:**
            - **Bisphosphonate:** Alendronate, Risedronate, Zoledronic acid
            - **Denosumab:** Kháng RANKL
            - **Teriparatide:** PTH (nếu nặng)

            **3. Tập thể dục:**
            - Tăng cường cơ, xương
            - Đi bộ, chạy bộ, tập tạ nhẹ

            **4. Phòng ngã:**
            - Loại bỏ vật cản trong nhà
            - Đủ ánh sáng
            - Tay vịn cầu thang

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Thực phẩm giàu canxi:**
            - **Sữa, sữa chua, phô mai:** Nguồn tốt nhất
            - **Cá nhỏ (ăn cả xương):** Cá cơm, cá mòi
            - **Rau xanh:** Rau muống, cải xoong, bông cải xanh
            - **Đậu, hạt:** Đậu phụ, hạnh nhân

            **2. Thực phẩm giàu vitamin D:**
            - **Cá béo:** Cá hồi, cá thu
            - **Trứng:** Lòng đỏ
            - **Sữa tăng cường vitamin D**

            **3. Tránh:**
            - Rượu bia (giảm hấp thu canxi)
            - Caffeine quá nhiều (tăng thải canxi)
            - Muối quá nhiều (tăng thải canxi)

            **4. Thực đơn mẫu:**
            - **Sáng:** Sữa, trứng, bánh mì
            - **Trưa:** Cơm, cá (ăn cả xương), rau xanh, canh, sữa chua
            - **Chiều:** Cơm, thịt/cá, rau xanh, canh, sữa
            - **Bữa phụ:** Sữa, hạt, trái cây

            **5. Lưu ý:**
            - Ăn đủ protein (tạo xương)
            - Bổ sung canxi, vitamin D nếu thiếu

            ## 🏃 TẬP THỂ DỤC:

            **1. Tập tải trọng (quan trọng!):**
            - **Đi bộ:** 30 phút/ngày, 5 ngày/tuần
            - **Chạy bộ:** Nếu sức khỏe cho phép
            - **Tập tạ nhẹ:** Tăng cường cơ, xương
            - **Leo cầu thang:** Tải trọng tốt

            **2. Tập thăng bằng:**
            - Yoga, thái cực quyền
            - Giảm nguy cơ ngã

            **3. Tránh:**
            - Tập quá mệt (tăng nguy cơ ngã)
            - Tập có nguy cơ ngã cao

            **4. Lưu ý:**
            - Khởi động kỹ
            - Tăng dần cường độ
            - Nghỉ ngơi nếu mệt

            ## 💊 QUẢN LÝ THUỐC:

            **1. Bổ sung:**
            - **Canxi:** 1000-1200 mg/ngày (chia 2 lần)
            - **Vitamin D:** 800-1000 IU/ngày
            - Uống với nước, sau ăn

            **2. Bisphosphonate:**
            - **Alendronate:** 70mg/tuần (uống buổi sáng, trước ăn 30 phút, với nước lọc)
            - **Risedronate:** 35mg/tuần
            - **Quan trọng:** Uống đúng cách (tránh viêm thực quản)

            **3. Tác dụng phụ:**
            - **Bisphosphonate:** Đau cơ, xương, viêm thực quản (nếu uống sai)
            - **Denosumab:** Đau cơ, xương

            **4. Lưu ý:**
            - Uống đều đặn
            - Theo dõi định kỳ

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Gãy xương:**
            - Đau dữ dội sau chấn thương nhẹ
            - Biến dạng
            - Không vận động được

            **2. Gãy đốt sống:**
            - Đau lưng dữ dội
            - Giảm chiều cao đột ngột
            - Gù lưng

            **3. Tác dụng phụ thuốc:**
            - Đau cơ, xương nặng
            - Khó nuốt (viêm thực quản)

            ## 💡 PHÒNG NGỪA:

            **1. Chế độ ăn:**
            - Ăn đủ canxi, vitamin D từ nhỏ
            - Duy trì suốt đời

            **2. Tập thể dục:**
            - Tập tải trọng đều đặn
            - Tăng cường cơ, xương

            **3. Phòng ngã:**
            - Loại bỏ vật cản
            - Đủ ánh sáng
            - Tay vịn cầu thang
            - Mang giày chắc chắn

            **4. Khám định kỳ:**
            - DEXA scan sau 50 tuổi (phụ nữ)
            - Sau 65 tuổi (nam)
            - Mỗi 2-3 năm

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Khi bị loãng xương:**
            - Bổ sung canxi, vitamin D
            - Uống thuốc đúng cách
            - Tập thể dục đều đặn
            - Phòng ngã

            **2. Uống thuốc đúng cách:**
            - Bisphosphonate: Buổi sáng, trước ăn 30 phút, với nước lọc
            - Đứng hoặc ngồi thẳng 30 phút sau uống

            **3. Sống tích cực:**
            - Loãng xương có thể kiểm soát
            - Điều trị đúng → Giảm nguy cơ gãy xương
            - Có thể sống bình thường

            **4. Phụ nữ sau mãn kinh:**
            - Bổ sung canxi, vitamin D
            - Tập thể dục
            - Khám định kỳ
            """,
            related_disease="osteoporosis",
            related_drugs=["Alendronate", "Risedronate", "Zoledronic Acid", "Denosumab", "Calcium", "Vitamin D"],
            printable=True
        ),

        PatientEducationTopic(
            id="psoriatic_arthritis_basics",
            title="Understanding Psoriatic Arthritis",
            title_vn="Hiểu về Viêm khớp vẩy nến",
            category="Disease",
            content="""
            # Hiểu về Viêm khớp vẩy nến

            ## Viêm khớp vẩy nến là gì?

            Viêm khớp vẩy nến (Psoriatic Arthritis - PsA) là bệnh viêm khớp mạn tính, xảy ra ở khoảng 30% bệnh nhân vẩy nến. Bệnh có thể ảnh hưởng đến khớp, da, móng, và các cơ quan khác.

            **⚠️ Đặc điểm:**
            - Viêm khớp mạn tính
            - Xảy ra ở 30% bệnh nhân vẩy nến
            - Ảnh hưởng khớp, da, móng
            - Bệnh tự miễn, không chữa khỏi

            **Phân loại:**
            - **Theo vị trí:**
              - Viêm khớp ngoại biên (tay, chân)
              - Viêm cột sống (cột sống)
              - Viêm khớp hỗn hợp
            - **Theo mức độ:**
              - Nhẹ: 1-4 khớp
              - Trung bình: 5-10 khớp
              - Nặng: > 10 khớp

            ## Triệu chứng:

            **Triệu chứng khớp:**
            - **Đau khớp:** Đau khớp, sưng khớp
            - **Cứng khớp:** Cứng khớp buổi sáng (> 30 phút)
            - **Sưng ngón tay/chân:** Sưng toàn bộ ngón (ngón xúc xích)
            - **Đau gân:** Đau gân, viêm gân (Achilles, gân bàn chân)
            - **Đau lưng:** Đau lưng, cứng lưng (nếu viêm cột sống)

            **Triệu chứng da:**
            - **Vẩy nến:** Mảng đỏ, có vẩy trắng
            - **Móng:** Móng dày, rỗ, tách móng

            **Triệu chứng khác:**
            - **Mệt mỏi:** Mệt mỏi, suy nhược
            - **Viêm mắt:** Viêm mắt, đỏ mắt
            - **Viêm ruột:** Có thể có

            **⚠️ Biến chứng:**
            - **Tổn thương khớp:** Tổn thương khớp vĩnh viễn
            - **Mất chức năng:** Mất chức năng khớp
            - **Bệnh tim mạch:** Tăng nguy cơ

            ## Nguyên nhân:

            **1. Nguyên nhân chưa rõ hoàn toàn:**
            - Có nhiều yếu tố

            **2. Yếu tố:**
            - **Tự miễn:** Hệ miễn dịch tấn công khớp, da
            - **Di truyền:** Có người thân bị bệnh (tăng nguy cơ)
            - **Vẩy nến:** 30% bệnh nhân vẩy nến bị viêm khớp
            - **Nhiễm trùng:** Có thể kích hoạt bệnh

            **3. Yếu tố nguy cơ:**
            - **Vẩy nến:** Có vẩy nến
            - **Tuổi:** 30-50 tuổi (phổ biến nhất)
            - **Di truyền:** Có người thân bị bệnh
            - **Béo phì:** Tăng nguy cơ

            ## Chẩn đoán:

            **Chẩn đoán lâm sàng:**
            - Triệu chứng điển hình
            - Khám khớp, da

            **Xét nghiệm:**
            - **Xét nghiệm máu:**
              - Tăng bạch cầu, CRP (dấu hiệu viêm)
              - RF âm tính (phân biệt với viêm khớp dạng thấp)
              - Anti-CCP âm tính
            - **X-quang:** Tổn thương khớp, xương

            **⚠️ Phân biệt:**
            - Viêm khớp dạng thấp
            - Viêm khớp do gout
            - Viêm cột sống dính khớp

            ## Điều trị:

            **1. Điều trị cấp tính:**
            - **NSAID:** Ibuprofen, Naproxen (giảm đau, viêm)
            - **Corticosteroid:** Prednisolone (nếu nặng)

            **2. Điều trị duy trì:**
            - **DMARD:**
              - **Methotrexate:** Phổ biến nhất
              - **Sulfasalazine:** Nếu viêm khớp ngoại biên
              - **Leflunomide:** Thay thế Methotrexate
            - **Biological:**
              - **TNF-α inhibitors:** Etanercept, Adalimumab, Infliximab
              - **IL-17 inhibitors:** Secukinumab, Ixekizumab
              - **IL-12/23 inhibitors:** Ustekinumab

            **3. Điều trị da:**
            - **Topical:** Corticosteroid, Vitamin D
            - **Phototherapy:** UVB, PUVA
            - **Systemic:** Methotrexate, Biological

            **⚠️ Lưu ý:**
            - Bệnh không chữa khỏi, cần điều trị lâu dài
            - Điều trị sớm → Giảm tổn thương khớp
            - Điều trị cả da và khớp

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Chế độ ăn chống viêm:**
            - **Cá béo:** Cá hồi, cá thu (omega-3, chống viêm, 2-3 lần/tuần)
            - **Rau xanh:** Nhiều (rau cải, rau muống, bông cải)
            - **Trái cây:** Tất cả (cam, bưởi, táo)
            - **Ngũ cốc nguyên hạt:** Gạo lứt, yến mạch
            - **Các loại hạt:** Hạnh nhân, óc chó (nếu có)

            **2. Thực phẩm nên tránh:**
            - **Thực phẩm chế biến sẵn:** Đồ hộp, thức ăn nhanh
            - **Đồ chiên, nhiều dầu mỡ:** Chất béo bão hòa (gây viêm)
            - **Đường nhiều:** Bánh kẹo, nước ngọt (gây viêm)
            - **Rượu bia:** Có thể làm nặng

            **3. Giảm cân (Nếu thừa cân):**
            - Thừa cân → Tăng áp lực lên khớp → Đau khớp
            - Giảm cân → Giảm đau khớp

            **4. Thực đơn mẫu:**
            - **Sáng:** Cháo yến mạch + trái cây
            - **Trưa:** Cơm + cá hồi + rau xanh + canh
            - **Chiều:** Cơm + thịt nạc + rau xanh + canh
            - **Bữa phụ:** Trái cây, hạt

            ## 🏃 TẬP THỂ DỤC:

            **1. Tập thể dục:**
            - **Quan trọng!** Giúp duy trì chức năng khớp
            - **Đi bộ:** 30 phút/ngày, 5 ngày/tuần
            - **Bơi lội:** Tốt cho khớp (ít áp lực)
            - **Yoga:** Tăng linh hoạt, giảm cứng khớp
            - **Tập tạ nhẹ:** Tăng sức mạnh cơ

            **2. Tránh:**
            - Tập quá sức khi đang đợt cấp
            - Tập khi đau nặng

            **3. Lưu ý:**
            - Khởi động kỹ
            - Tăng dần cường độ
            - Nghỉ ngơi nếu đau

            ## 💊 QUẢN LÝ THUỐC:

            **1. NSAID:**
            - **Ibuprofen, Naproxen:** Giảm đau, viêm
            - **Uống với thức ăn:** Tránh kích thích dạ dày

            **2. DMARD:**
            - **Methotrexate:** Uống hoặc tiêm, 1 lần/tuần
            - **Sulfasalazine:** Uống đều đặn
            - **Leflunomide:** Uống đều đặn
            - **Tác dụng phụ:** Giảm bạch cầu, nhiễm trùng, tổn thương gan
            - **Lưu ý:** Xét nghiệm máu định kỳ

            **3. Biological:**
            - **Etanercept, Adalimumab:** Tiêm dưới da
            - **Infliximab:** Truyền tĩnh mạch
            - **Tác dụng phụ:** Nhiễm trùng, phản ứng dị ứng
            - **Lưu ý:** Theo dõi sát

            **4. Lưu ý:**
            - Uống đúng liều, đúng giờ
            - Không tự ý ngừng thuốc
            - Báo bác sĩ nếu có tác dụng phụ
            - Xét nghiệm máu định kỳ

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Đợt cấp nặng:**
            - Đau khớp dữ dội
            - Sưng khớp nhiều
            - Sốt

            **2. Tác dụng phụ:**
            - Sốt, ớn lạnh (nhiễm trùng)
            - Phát ban, ngứa (dị ứng)
            - Khó thở

            **3. Biến chứng:**
            - Mất chức năng khớp
            - Tổn thương khớp nặng

            ## 💡 PHÒNG NGỪA:

            **1. Điều trị vẩy nến:**
            - Điều trị vẩy nến sớm
            - Giảm nguy cơ viêm khớp

            **2. Chế độ ăn:**
            - Chế độ ăn chống viêm
            - Giảm cân nếu thừa cân

            **3. Tập thể dục:**
            - Tập thể dục đều đặn
            - Duy trì chức năng khớp

            **4. Tránh:**
            - Chấn thương khớp
            - Nhiễm trùng

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Khi bị viêm khớp vẩy nến:**
            - Điều trị đều đặn, lâu dài
            - Tuân thủ điều trị
            - Điều trị cả da và khớp

            **2. Sống tích cực:**
            - Bệnh không chữa khỏi nhưng có thể kiểm soát
            - Điều trị đúng → Giảm triệu chứng, tổn thương khớp
            - Có thể sống bình thường

            **3. Tập thể dục:**
            - Tập thể dục đều đặn
            - Duy trì chức năng khớp
            - Giảm cứng khớp

            **4. Lâu dài:**
            - Cần điều trị lâu dài
            - Theo dõi định kỳ
            - Tầm soát bệnh tim mạch
            """,
            related_disease="psoriatic_arthritis",
            related_drugs=["Ibuprofen", "Naproxen", "Methotrexate", "Sulfasalazine", "Etanercept", "Adalimumab", "Infliximab"],
            printable=True
        ),

]
