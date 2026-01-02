"""
Patient Education Topics - Infectious
"""
from patient_education.models import PatientEducationTopic


INFECTIOUS_TOPICS = [
        PatientEducationTopic(
            id="uti_basics",
            title="Understanding Urinary Tract Infection",
            title_vn="Hiểu về Nhiễm trùng đường tiểu",
            category="Disease",
            content="""
    # Hiểu về Nhiễm trùng đường tiểu (UTI)

    ## Nhiễm trùng đường tiểu là gì?

    UTI là nhiễm trùng ở bàng quang, niệu đạo, hoặc thận.

    ## Triệu chứng:
    - Tiểu buốt, tiểu rắt
    - Tiểu nhiều lần
    - Nước tiểu đục, có mùi
    - Đau bụng dưới
    - Sốt (nếu nhiễm thận)
    - Đau lưng (nếu nhiễm thận)

    ## Nguyên nhân:
    - Vi khuẩn từ đường tiêu hóa
    - Phụ nữ dễ mắc hơn (niệu đạo ngắn)
    - Quan hệ tình dục
    - Vệ sinh không đúng cách

    ## Điều trị:
    - Uống kháng sinh đủ liều, đủ ngày
    - Uống nhiều nước
    - Nghỉ ngơi
    - Giảm đau nếu cần

    ## Phòng ngừa:
    - Uống đủ nước (1.5-2 lít/ngày)
    - Đi tiểu thường xuyên, không nhịn
    - Vệ sinh đúng cách (lau từ trước ra sau)
    - Đi tiểu sau quan hệ
    - Mặc quần lót cotton, rộng rãi

    ## Khi nào cần đến bệnh viện:
    - Sốt cao
    - Đau lưng dữ dội
    - Nôn, không uống được
    - Không cải thiện sau 2-3 ngày

    ## Lời khuyên:
    - Uống nhiều nước
    - Uống kháng sinh đủ ngày
    - Vệ sinh đúng cách
    - Đi tiểu thường xuyên
    - Tái khám nếu không đỡ
            """,
            related_disease="uti",
            related_drugs=["Ciprofloxacin", "Trimethoprim", "Nitrofurantoin"],
            printable=True
        ),

        PatientEducationTopic(
            id="dengue_fever_basics",
            title="Understanding Dengue Fever",
            title_vn="Hiểu về Sốt xuất huyết Dengue",
            category="Disease",
            content="""
            # Hiểu về Sốt xuất huyết Dengue

            ## Sốt xuất huyết Dengue là gì?

            Sốt xuất huyết Dengue là bệnh truyền nhiễm do virus Dengue, lây truyền qua muỗi vằn (Aedes aegypti). Bệnh phổ biến ở vùng nhiệt đới, đặc biệt là Việt Nam.

            **⚠️ Đặc điểm:**
            - Bệnh theo mùa (mùa mưa, nóng ẩm)
            - Có thể nặng, gây sốt xuất huyết Dengue nặng (DSS)
            - Chưa có thuốc đặc trị, chủ yếu điều trị triệu chứng

            ## Triệu chứng:

            **Giai đoạn sốt (1-3 ngày đầu):**
            - **Sốt cao đột ngột:** 39-40°C, liên tục
            - **Đau đầu:** Đau dữ dội, đặc biệt vùng trán
            - **Đau mắt:** Đau sau hốc mắt
            - **Đau cơ, đau khớp:** Đau toàn thân
            - **Mệt mỏi:** Uể oải, không có sức
            - **Buồn nôn, nôn**
            - **Phát ban:** Ban đỏ trên da (có thể có)

            **Giai đoạn nguy hiểm (Ngày 4-7):**
            - **Sốt giảm:** Có thể hạ sốt (nhưng đây là giai đoạn nguy hiểm!)
            - **Xuất huyết:**
              - Chấm xuất huyết dưới da
              - Chảy máu cam, chảy máu chân răng
              - Nôn ra máu, đi ngoài phân đen
              - Kinh nguyệt kéo dài (ở nữ)
            - **Dấu hiệu cảnh báo:**
              - Đau bụng, nôn nhiều
              - Vật vã, lú lẫn
              - Chảy máu niêm mạc
              - Tiểu ít
              - **→ Cần đến bệnh viện ngay!**

            **Giai đoạn hồi phục (Sau ngày 7):**
            - Sốt giảm
            - Ăn uống tốt hơn
            - Phát ban, ngứa da (có thể)

            ## 🚨 DẤU HIỆU CẢNH BÁO (Cần nhập viện ngay!):

            **1. Dấu hiệu sốc:**
            - Vật vã, lú lẫn
            - Tay chân lạnh, ẩm
            - Mạch nhanh, yếu
            - Huyết áp tụt
            - Tiểu ít hoặc không tiểu

            **2. Xuất huyết nặng:**
            - Nôn ra máu
            - Đi ngoài phân đen
            - Chảy máu cam nhiều
            - Chảy máu không cầm được

            **3. Đau bụng:**
            - Đau bụng dữ dội
            - Nôn nhiều

            **4. Dấu hiệu khác:**
            - Khó thở
            - Co giật
            - Hôn mê

            **⚠️ QUAN TRỌNG:** Giai đoạn nguy hiểm thường xảy ra khi sốt giảm (ngày 4-7). Đừng chủ quan khi hạ sốt!

            ## Điều trị:

            **1. Điều trị tại nhà (Sốt xuất huyết nhẹ):**
            - **Hạ sốt:** Paracetamol 10-15mg/kg/lần, cách 4-6 giờ
            - **⚠️ KHÔNG dùng:** Aspirin, Ibuprofen (gây xuất huyết nặng!)
            - **Uống nhiều nước:** Nước lọc, oresol, nước trái cây
            - **Nghỉ ngơi:** Nghỉ hoàn toàn
            - **Theo dõi:** Đo nhiệt độ, theo dõi triệu chứng

            **2. Điều trị tại viện (Sốt xuất huyết nặng):**
            - Truyền dịch
            - Theo dõi tiểu cầu, hematocrit
            - Điều trị xuất huyết
            - Điều trị sốc nếu có

            **3. Không có thuốc đặc trị:**
            - Chủ yếu điều trị triệu chứng
            - Hỗ trợ, theo dõi

            ## 🍽️ CHẾ ĐỘ ĂN KHI BỊ SỐT XUẤT HUYẾT:

            **1. Nguyên tắc:**
            - **Uống nhiều nước:** Quan trọng nhất! (2-3 lít/ngày)
            - **Ăn nhẹ, dễ tiêu:** Tránh đồ khó tiêu
            - **Chia nhỏ bữa:** 5-6 bữa/ngày
            - **Đủ dinh dưỡng:** Giúp cơ thể chống lại bệnh

            **2. Uống nước (QUAN TRỌNG!):**
            - **Oresol:** Tốt nhất (bù nước và điện giải)
              - Pha đúng tỷ lệ (1 gói + 1 lít nước)
              - Uống từng ngụm nhỏ, thường xuyên
            - **Nước lọc:** Uống nhiều
            - **Nước trái cây:** Cam, chanh, dừa (vitamin C, kali)
            - **Súp, canh:** Vừa ăn vừa uống nước
            - **⚠️ Tránh:** Nước ngọt có ga, đồ uống có cồn

            **3. Thực phẩm nên ăn:**
            - **Cháo, súp:** Dễ nuốt, dễ tiêu, có nước
              - Cháo gà, cháo thịt bằm
              - Súp rau củ
            - **Trái cây:** Cam, chanh, bưởi (vitamin C), chuối (kali)
            - **Rau xanh:** Luộc, hấp (vitamin, chất xơ)
            - **Protein:** Thịt nạc, cá (luộc, hấp)
            - **Sữa:** Sữa ấm, sữa chua

            **4. Thực phẩm cần tránh:**
            - **Thực phẩm màu đỏ, nâu:** Dưa hấu, củ dền, cà phê, coca
              - **Lý do:** Khó phân biệt với máu khi nôn/đi ngoài
            - **Đồ chiên, nhiều dầu mỡ:** Khó tiêu
            - **Đồ cay:** Kích thích dạ dày
            - **Đồ lạnh:** Có thể làm sốt nặng hơn
            - **Rượu bia:** Làm mất nước, giảm miễn dịch

            **5. Thực đơn mẫu (1 ngày):**
            - **Sáng:** Cháo gà + nước cam
            - **Bữa phụ (10h):** Oresol, chuối
            - **Trưa:** Cháo thịt bằm + canh rau
            - **Bữa phụ (15h):** Nước dừa, sữa chua
            - **Tối:** Súp rau củ + nước trái cây
            - **Bữa phụ (21h):** Sữa ấm, oresol

            **6. Lưu ý:**
            - Uống nước ngay cả khi không khát
            - Uống từng ngụm nhỏ, thường xuyên
            - Nếu nôn → Uống lại sau 10-15 phút
            - Ăn chậm, nhai kỹ
            - Nếu không ăn được → Uống sữa, nước trái cây

            ## 💤 CHĂM SÓC TẠI NHÀ:

            **1. Nghỉ ngơi:**
            - Nghỉ hoàn toàn, không làm việc
            - Ngủ đủ giấc
            - Tránh gắng sức

            **2. Hạ sốt:**
            - **Paracetamol:** 10-15mg/kg/lần, cách 4-6 giờ
            - **Lau người:** Nước ấm (không dùng nước lạnh)
            - **Mặc quần áo thoáng:** Không đắp chăn quá dày
            - **⚠️ KHÔNG dùng:** Aspirin, Ibuprofen, Diclofenac

            **3. Theo dõi:**
            - **Nhiệt độ:** Đo 3-4 lần/ngày
            - **Triệu chứng:** Ghi nhật ký
            - **Dấu hiệu cảnh báo:** Kiểm tra thường xuyên
            - **Tiểu:** Theo dõi số lần, lượng nước tiểu

            **4. Vệ sinh:**
            - Rửa tay thường xuyên
            - Vệ sinh răng miệng (nhẹ nhàng, tránh chảy máu)
            - Tắm nhanh bằng nước ấm (nếu sốt không quá cao)

            **5. Phòng ngừa lây lan:**
            - Nằm màn (tránh muỗi đốt, lây cho người khác)
            - Diệt muỗi, lăng quăng trong nhà
            - Không để nước đọng

            ## 🛡️ PHÒNG NGỪA:

            **1. Diệt muỗi, lăng quăng:**
            - **Loại bỏ nước đọng:**
              - Đậy kín lu, vại, bể chứa nước
              - Thả cá vào bể nước
              - Thay nước bình hoa, chậu cây thường xuyên
              - Lật úp các vật chứa nước không dùng
            - **Diệt lăng quăng:** Dùng hóa chất, cá
            - **Phun thuốc diệt muỗi:** Khi có dịch

            **2. Tránh muỗi đốt:**
            - **Nằm màn:** Khi ngủ (ngày và đêm)
            - **Mặc quần áo dài:** Khi ra ngoài
            - **Dùng kem chống muỗi:** DEET, Picaridin
            - **Dùng nhang muỗi, vợt muỗi**

            **3. Vệ sinh môi trường:**
            - Dọn dẹp nhà cửa sạch sẽ
            - Không để rác, nước đọng
            - Thông thoáng nhà cửa

            **4. Tiêm chủng:**
            - Vắc xin Dengue đã có (Dengvaxia)
            - Chỉ dùng cho người đã từng bị sốt xuất huyết
            - Tham khảo bác sĩ

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN NGAY:

            **1. Dấu hiệu cảnh báo:**
            - Vật vã, lú lẫn
            - Đau bụng dữ dội
            - Nôn nhiều
            - Chảy máu (cam, chân răng, dưới da)
            - Tay chân lạnh, ẩm
            - Tiểu ít hoặc không tiểu

            **2. Sốt xuất huyết nặng:**
            - Sốc (tụt huyết áp, mạch nhanh)
            - Xuất huyết nặng
            - Suy tạng

            **3. Không cải thiện:**
            - Sốt > 3 ngày không giảm
            - Triệu chứng nặng hơn
            - Không uống được nước

            **⚠️ QUAN TRỌNG:** Đến bệnh viện ngay khi có dấu hiệu cảnh báo! Sốt xuất huyết có thể diễn biến nhanh, nguy hiểm.

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Khi bị sốt xuất huyết:**
            - Nghỉ ngơi hoàn toàn
            - Uống nhiều nước (quan trọng nhất!)
            - Hạ sốt đúng cách (chỉ dùng Paracetamol)
            - Theo dõi dấu hiệu cảnh báo
            - Đến bệnh viện khi cần

            **2. Không tự ý:**
            - Dùng Aspirin, Ibuprofen
            - Truyền dịch tại nhà (nguy hiểm!)
            - Dùng thuốc không rõ nguồn gốc

            **3. Phòng ngừa:**
            - Diệt muỗi, lăng quăng
            - Nằm màn
            - Vệ sinh môi trường

            **4. Mùa dịch:**
            - Mùa mưa (tháng 6-11) là mùa sốt xuất huyết
            - Cần phòng ngừa tích cực
            - Khi có dịch → Tránh nơi có nhiều muỗi
            """,
            related_disease="dengue_fever",
            related_drugs=["Paracetamol", "Oresol"],
            printable=True
        ),

        PatientEducationTopic(
            id="hepatitis_bc_basics",
            title="Understanding Hepatitis B and C",
            title_vn="Hiểu về Viêm gan B và C",
            category="Disease",
            content="""
            # Hiểu về Viêm gan B và C

            ## Viêm gan B và C là gì?

            Viêm gan B và C là bệnh nhiễm trùng gan do virus, có thể gây viêm gan cấp hoặc mạn tính, dẫn đến xơ gan, ung thư gan.

            **Viêm gan B (HBV):**
            - Có vắc xin phòng ngừa
            - Có thể chữa khỏi hoặc kiểm soát
            - Lây qua máu, quan hệ tình dục, từ mẹ sang con

            **Viêm gan C (HCV):**
            - Chưa có vắc xin
            - Có thể chữa khỏi hoàn toàn (90-95%)
            - Lây chủ yếu qua máu

            **⚠️ Đặc điểm:**
            - Nhiều người không có triệu chứng
            - Có thể tiến triển thành xơ gan, ung thư gan
            - Phát hiện sớm → Điều trị hiệu quả

            ## Triệu chứng:

            **Viêm gan cấp:**
            - **Mệt mỏi:** Uể oải, không có sức
            - **Chán ăn:** Không muốn ăn
            - **Vàng da, vàng mắt:** Dấu hiệu điển hình
            - **Nước tiểu sẫm màu:** Như nước trà đặc
            - **Phân nhạt màu:** Trắng, xám
            - **Đau bụng:** Vùng gan (bên phải)
            - **Buồn nôn, nôn**
            - **Sốt nhẹ**

            **Viêm gan mạn:**
            - **Thường không có triệu chứng** (nguy hiểm!)
            - Mệt mỏi nhẹ
            - Đau tức vùng gan
            - Có thể tiến triển thành xơ gan, ung thư gan

            **⚠️ Lưu ý:** Nhiều người không biết mình bị viêm gan cho đến khi có biến chứng!

            ## Nguyên nhân và đường lây:

            **1. Viêm gan B:**
            - **Máu:** Dùng chung kim tiêm, dao cạo, bàn chải đánh răng
            - **Quan hệ tình dục:** Không an toàn
            - **Từ mẹ sang con:** Khi sinh
            - **Vết thương:** Tiếp xúc với máu người bệnh
            - **Dụng cụ y tế:** Không vô trùng

            **2. Viêm gan C:**
            - **Máu:** Chủ yếu (dùng chung kim tiêm)
            - **Quan hệ tình dục:** Ít hơn (nhưng vẫn có)
            - **Từ mẹ sang con:** Hiếm
            - **Dụng cụ y tế:** Không vô trùng

            **3. KHÔNG lây qua:**
            - Ôm, hôn
            - Dùng chung bát đĩa
            - Ho, hắt hơi
            - Muỗi đốt
            - Cho con bú (nếu núm vú không chảy máu)

            ## Chẩn đoán:

            **1. Xét nghiệm máu:**
            - **Viêm gan B:**
              - HBsAg: Kháng nguyên bề mặt
              - Anti-HBc: Kháng thể lõi
              - HBV DNA: Tải lượng virus
            - **Viêm gan C:**
              - Anti-HCV: Kháng thể
              - HCV RNA: Tải lượng virus

            **2. Đánh giá chức năng gan:**
            - AST, ALT: Men gan
            - Bilirubin: Vàng da
            - Albumin: Chức năng gan
            - PT/INR: Đông máu

            **3. Đánh giá tổn thương gan:**
            - **Siêu âm gan:** Xem cấu trúc gan
            - **FibroScan:** Đo độ xơ hóa gan
            - **Sinh thiết gan:** (nếu cần)

            ## Điều trị:

            **1. Viêm gan B:**
            - **Thuốc kháng virus:**
              - Tenofovir
              - Entecavir
              - Lamivudine
            - **Mục tiêu:** Ức chế virus, giảm tổn thương gan
            - **Thời gian:** Thường uống lâu dài
            - **⚠️ QUAN TRỌNG:** Uống đúng giờ, không tự ý ngừng

            **2. Viêm gan C:**
            - **Thuốc kháng virus trực tiếp (DAA):**
              - Sofosbuvir + Velpatasvir
              - Glecaprevir + Pibrentasvir
            - **Thời gian:** 8-12 tuần
            - **Tỷ lệ chữa khỏi:** 90-95%
            - **⚠️ QUAN TRỌNG:** Uống đúng giờ, đủ ngày

            **3. Điều trị hỗ trợ:**
            - Nghỉ ngơi
            - Chế độ ăn phù hợp
            - Tránh rượu bia, thuốc lá

            ## 🍽️ CHẾ ĐỘ ĂN CHO NGƯỜI VIÊM GAN:

            **1. Nguyên tắc:**
            - **Bảo vệ gan:** Tránh gánh nặng cho gan
            - **Đủ dinh dưỡng:** Giúp gan phục hồi
            - **Dễ tiêu:** Tránh đồ khó tiêu
            - **Tránh rượu bia:** Hoàn toàn!

            **2. Thực phẩm NÊN ĂN:**
            - **Protein nạc:** Thịt gà (bỏ da), cá, đậu phụ
              - Giúp phục hồi tế bào gan
              - 1-1.5g/kg cân nặng/ngày
            - **Rau xanh:** Nhiều (rau cải, rau muống, bông cải)
              - Vitamin, chất xơ
              - Chống oxy hóa
            - **Trái cây:** Tất cả (cam, bưởi, táo)
              - Vitamin C
            - **Ngũ cốc:** Gạo, bánh mì, yến mạch
              - Năng lượng
            - **Sữa ít béo:** Sữa tách béo, sữa chua
            - **Dầu thực vật:** Dầu ô liu, dầu hạt cải (ít)

            **3. Thực phẩm CẦN TRÁNH:**
            - **Rượu bia:** HOÀN TOÀN! (làm tổn thương gan nặng hơn)
            - **Thực phẩm nhiều chất béo:** Đồ chiên rán, mỡ động vật
            - **Thực phẩm chế biến sẵn:** Đồ hộp, thức ăn nhanh
            - **Thực phẩm sống:** Gỏi, sushi (nguy cơ nhiễm khuẩn)
            - **Muối nhiều:** Nếu có xơ gan, cổ trướng
            - **Đường nhiều:** Bánh kẹo, nước ngọt

            **4. Thực đơn mẫu (1 ngày):**
            - **Sáng:** Cháo yến mạch + 1 quả trứng luộc + sữa ít béo
            - **Trưa:** 1 chén cơm + cá hấp + rau luộc + canh rau
            - **Tối:** 1 chén cơm + thịt gà luộc (bỏ da) + rau xào (ít dầu) + canh
            - **Bữa phụ:** Trái cây, sữa chua

            **5. Lưu ý:**
            - Ăn đều đặn, không bỏ bữa
            - Ăn chậm, nhai kỹ
            - Chia nhỏ bữa nếu chán ăn
            - Uống đủ nước (1.5-2 lít/ngày)

            ## 🏃 TẬP THỂ DỤC:

            **1. Khi viêm gan cấp:**
            - **Nghỉ ngơi:** Không tập thể dục
            - Nghỉ hoàn toàn cho đến khi hồi phục

            **2. Khi viêm gan mạn (ổn định):**
            - **Tập thể dục nhẹ nhàng:** Đi bộ, yoga, thái cực quyền
            - **Thời gian:** 20-30 phút/ngày
            - **Tần suất:** 3-5 lần/tuần
            - **Tránh:** Tập quá sức, gắng sức

            **3. Lợi ích:**
            - Tăng sức khỏe
            - Giảm mệt mỏi
            - Cải thiện tâm trạng

            ## 🛡️ PHÒNG NGỪA:

            **1. Viêm gan B:**
            - **Tiêm vắc xin:** Quan trọng nhất!
              - Trẻ sơ sinh: Tiêm ngay sau sinh
              - Người lớn: 3 mũi (0, 1, 6 tháng)
              - Hiệu quả > 95%
            - **Kiểm tra:** Xét nghiệm trước khi tiêm

            **2. Viêm gan C:**
            - **Chưa có vắc xin**
            - Phòng ngừa bằng cách tránh lây nhiễm

            **3. Tránh lây nhiễm:**
            - **Không dùng chung:** Kim tiêm, dao cạo, bàn chải đánh răng
            - **Quan hệ tình dục an toàn:** Dùng bao cao su
            - **Dụng cụ y tế:** Đảm bảo vô trùng
            - **Kiểm tra máu:** Trước khi truyền

            **4. Nếu đã bị viêm gan:**
            - **Không cho máu**
            - **Báo cho người thân:** Để phòng ngừa
            - **Không dùng chung:** Đồ dùng cá nhân
            - **Bảo vệ người khác:** Tránh lây lan

            ## 💊 QUẢN LÝ THUỐC:

            **1. Viêm gan B:**
            - **Uống đúng giờ:** Hàng ngày
            - **Không tự ý ngừng:** Ngừng → Virus tái hoạt động
            - **Theo dõi:** Xét nghiệm định kỳ (3-6 tháng)
            - **Tác dụng phụ:** Ít, nhưng báo bác sĩ nếu có

            **2. Viêm gan C:**
            - **Uống đúng giờ:** Hàng ngày
            - **Uống đủ ngày:** 8-12 tuần (quan trọng!)
            - **Không tự ý ngừng:** Ngừng → Không chữa khỏi
            - **Tác dụng phụ:** Mệt mỏi, đau đầu (thường nhẹ)

            **3. Tương tác thuốc:**
            - Báo bác sĩ TẤT CẢ thuốc đang dùng
            - Một số thuốc tương tác với thuốc viêm gan

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Viêm gan cấp nặng:**
            - Vàng da nặng
            - Nôn nhiều, không ăn được
            - Lú lẫn, buồn ngủ
            - Chảy máu

            **2. Biến chứng:**
            - Xơ gan: Phù chân, cổ trướng
            - Ung thư gan: Đau bụng, sụt cân

            **3. Tác dụng phụ thuốc:**
            - Nghiêm trọng, không chịu được

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Nếu chưa bị:**
            - Tiêm vắc xin viêm gan B
            - Tránh lây nhiễm
            - Khám sức khỏe định kỳ

            **2. Nếu đã bị:**
            - Tuân thủ điều trị
            - Không uống rượu bia
            - Chế độ ăn lành mạnh
            - Khám định kỳ
            - Bảo vệ người khác

            **3. Sống tích cực:**
            - Viêm gan có thể kiểm soát/chữa khỏi
            - Tuân thủ điều trị → Sống khỏe mạnh
            - Đừng để bệnh ảnh hưởng cuộc sống
            """,
            related_disease="hepatitis_bc",
            related_drugs=["Tenofovir", "Entecavir", "Sofosbuvir"],
            printable=True
        ),

        PatientEducationTopic(
            id="tuberculosis_basics",
            title="Understanding Tuberculosis",
            title_vn="Hiểu về Lao phổi",
            category="Disease",
            content="""
            # Hiểu về Lao phổi

            ## Lao phổi là gì?

            Lao phổi là bệnh truyền nhiễm do vi khuẩn Mycobacterium tuberculosis gây ra, chủ yếu ảnh hưởng đến phổi nhưng có thể ảnh hưởng đến các cơ quan khác.

            **⚠️ Đặc điểm:**
            - Bệnh truyền nhiễm, lây qua đường hô hấp
            - Có thể chữa khỏi hoàn toàn nếu điều trị đúng
            - Không điều trị → Nguy hiểm, có thể tử vong
            - Điều trị lâu dài (ít nhất 6 tháng)

            **Phân loại:**
            - **Lao phổi:** Ảnh hưởng phổi (phổ biến nhất)
            - **Lao ngoài phổi:** Ảnh hưởng cơ quan khác (lao màng phổi, lao xương, lao màng não)

            ## Triệu chứng:

            **Triệu chứng điển hình:**
            - **Ho kéo dài:** > 2 tuần (dấu hiệu quan trọng nhất!)
            - **Ho ra máu:** Có thể có
            - **Sốt nhẹ về chiều:** 37.5-38°C
            - **Ra mồ hôi đêm:** Ướt đẫm
            - **Sụt cân:** Không rõ nguyên nhân
            - **Mệt mỏi:** Uể oải, không có sức
            - **Chán ăn**
            - **Đau ngực:** Có thể có
            - **Khó thở:** Khi bệnh nặng

            **⚠️ Lưu ý:**
            - Ho > 2 tuần → Cần nghĩ đến lao
            - Nhiều người không có triệu chứng rõ ràng
            - Cần xét nghiệm để chẩn đoán

            ## Nguyên nhân và đường lây:

            **1. Nguyên nhân:**
            - Vi khuẩn Mycobacterium tuberculosis
            - Lây qua đường hô hấp

            **2. Đường lây:**
            - **Ho, hắt hơi:** Người bệnh ho → Giọt bắn chứa vi khuẩn
            - **Nói chuyện:** Gần, lâu
            - **Hít phải:** Vi khuẩn vào phổi

            **3. Yếu tố nguy cơ:**
            - **Tiếp xúc gần:** Sống chung, làm việc chung với người lao
            - **Suy giảm miễn dịch:** HIV, đái tháo đường, dùng thuốc ức chế miễn dịch
            - **Điều kiện sống:** Chật chội, thiếu ánh sáng, thiếu thông khí
            - **Suy dinh dưỡng**
            - **Hút thuốc lá**

            **4. KHÔNG lây qua:**
            - Ôm, hôn
            - Dùng chung bát đĩa
            - Muỗi đốt
            - Quần áo

            ## Chẩn đoán:

            **1. Xét nghiệm đờm:**
            - **AFB (Acid Fast Bacilli):** Tìm vi khuẩn lao trong đờm
              - Lấy đờm 3 lần (sáng sớm, trước ăn)
              - Kết quả trong 1-2 ngày
            - **Xpert MTB/RIF:** Xét nghiệm nhanh, chính xác
              - Phát hiện vi khuẩn lao và kháng rifampicin
              - Kết quả trong vài giờ

            **2. Chụp X-quang phổi:**
            - Tìm tổn thương phổi
            - Đánh giá mức độ bệnh

            **3. Test Mantoux (Tuberculin skin test):**
            - Kiểm tra phản ứng với lao
            - Dương tính → Có thể đã tiếp xúc với lao

            **4. Xét nghiệm máu (IGRA):**
            - Phát hiện lao tiềm ẩn

            ## Điều trị:

            **⚠️ QUAN TRỌNG:** Lao phải điều trị đúng, đủ thời gian!

            **1. Phác đồ điều trị chuẩn:**
            - **Giai đoạn tấn công (2 tháng đầu):**
              - Isoniazid (H)
              - Rifampicin (R)
              - Pyrazinamide (Z)
              - Ethambutol (E)
            - **Giai đoạn duy trì (4 tháng tiếp):**
              - Isoniazid (H)
              - Rifampicin (R)
            - **Tổng thời gian:** 6 tháng (ít nhất)

            **2. Điều trị dưới sự giám sát (DOT):**
            - Uống thuốc dưới sự giám sát của nhân viên y tế
            - Đảm bảo uống đúng, đủ
            - Phòng ngừa kháng thuốc

            **3. ⚠️ QUAN TRỌNG:**
            - **Uống đúng giờ:** Hàng ngày
            - **Uống đủ thời gian:** 6 tháng (ít nhất)
            - **Không tự ý ngừng:** Ngừng → Kháng thuốc, bệnh nặng hơn
            - **Uống khi đói:** Trước ăn 1 giờ hoặc sau ăn 2 giờ

            **4. Điều trị lao kháng thuốc:**
            - Nếu kháng thuốc → Phác đồ đặc biệt
            - Thời gian điều trị lâu hơn (18-24 tháng)
            - Thuốc khác, nhiều tác dụng phụ hơn

            ## 🍽️ CHẾ ĐỘ ĂN CHO NGƯỜI BỊ LAO:

            **1. Nguyên tắc:**
            - **Đủ dinh dưỡng:** Giúp cơ thể chống lại bệnh
            - **Tăng calo:** Bù lại sụt cân
            - **Đủ protein:** Phục hồi tế bào
            - **Vitamin, khoáng chất:** Tăng miễn dịch

            **2. Thực phẩm NÊN ĂN:**
            - **Protein:** Thịt nạc, cá, trứng, đậu, sữa
              - Giúp phục hồi, tăng miễn dịch
              - 1.5-2g/kg cân nặng/ngày
            - **Carbohydrate:** Gạo, bánh mì, khoai
              - Năng lượng
            - **Rau xanh:** Nhiều (rau cải, rau muống, bông cải)
              - Vitamin, chất xơ
            - **Trái cây:** Tất cả (cam, bưởi, ổi)
              - Vitamin C (tăng miễn dịch)
            - **Sữa, sữa chua:** Protein, canxi
            - **Các loại hạt:** Hạnh nhân, óc chó (nếu có)

            **3. Thực phẩm CẦN TRÁNH:**
            - **Rượu bia:** Làm giảm miễn dịch, tăng tác dụng phụ thuốc
            - **Thuốc lá:** Làm tổn thương phổi nặng hơn
            - **Thực phẩm chế biến sẵn:** Ít dinh dưỡng
            - **Đồ chiên, nhiều dầu mỡ:** Khó tiêu

            **4. Thực đơn mẫu (1 ngày):**
            - **Sáng:** Cháo thịt bằm + 1 quả trứng luộc + sữa
            - **Bữa phụ (10h):** Sữa chua, trái cây
            - **Trưa:** 1.5 chén cơm + thịt gà kho + rau luộc + canh thịt
            - **Bữa phụ (15h):** Sữa, bánh mì
            - **Tối:** 1.5 chén cơm + cá kho + rau xào + canh
            - **Bữa phụ (21h):** Sữa ấm

            **5. Lưu ý:**
            - Ăn nhiều bữa nhỏ (5-6 bữa/ngày) nếu chán ăn
            - Ăn đủ chất, không kiêng khem
            - Uống đủ nước (2-3 lít/ngày)

            ## 🏃 TẬP THỂ DỤC:

            **1. Khi đang điều trị:**
            - **Nghỉ ngơi:** Nghỉ nhiều, không gắng sức
            - **Tập nhẹ nhàng:** Đi bộ nhẹ, 10-15 phút/ngày
            - **Tránh:** Tập quá sức, gắng sức

            **2. Sau khi khỏi:**
            - **Tập thể dục dần:** Tăng dần cường độ
            - **Đi bộ:** 20-30 phút/ngày
            - **Tập thở:** Phục hồi chức năng phổi
            - **Mục tiêu:** Tăng sức khỏe, phục hồi

            ## 🛡️ PHÒNG NGỪA:

            **1. Tiêm vắc xin BCG:**
            - Tiêm cho trẻ sơ sinh
            - Phòng ngừa lao nặng ở trẻ em
            - Không phòng ngừa lao phổi ở người lớn

            **2. Phát hiện và điều trị sớm:**
            - Phát hiện sớm → Điều trị sớm → Giảm lây lan
            - Nếu ho > 2 tuần → Đi khám, xét nghiệm đờm

            **3. Điều trị lao tiềm ẩn:**
            - Nếu tiếp xúc với người lao → Xét nghiệm
            - Nếu có lao tiềm ẩn → Điều trị dự phòng

            **4. Tránh lây nhiễm:**
            - **Người bệnh:**
              - Đeo khẩu trang khi ra ngoài
              - Che miệng khi ho, hắt hơi
              - Ở phòng riêng, thông thoáng
              - Không khạc nhổ bừa bãi
            - **Người khỏe:**
              - Đeo khẩu trang khi tiếp xúc người lao
              - Tránh nơi đông người, thiếu thông khí
              - Giữ vệ sinh môi trường

            **5. Cải thiện điều kiện sống:**
            - Thông thoáng, có ánh sáng
            - Không chật chội
            - Vệ sinh môi trường

            ## 💊 QUẢN LÝ THUỐC:

            **⚠️ QUAN TRỌNG:** Uống thuốc đúng, đủ thời gian!

            **1. Uống đúng giờ:**
            - Hàng ngày, cùng một giờ
            - Uống khi đói (trước ăn 1 giờ hoặc sau ăn 2 giờ)
            - Đặt báo thức nhắc nhở

            **2. Uống đủ thời gian:**
            - 6 tháng (ít nhất)
            - Không tự ý ngừng
            - Ngừng sớm → Kháng thuốc, bệnh nặng hơn

            **3. Tác dụng phụ:**
            - **Isoniazid:** Tổn thương thần kinh (dùng thêm vitamin B6)
            - **Rifampicin:** Nước tiểu đỏ (bình thường), đau dạ dày
            - **Pyrazinamide:** Đau khớp, tăng acid uric
            - **Ethambutol:** Tổn thương mắt (kiểm tra mắt định kỳ)
            - **Báo bác sĩ nếu:** Tác dụng phụ nghiêm trọng

            **4. Tương tác thuốc:**
            - Báo bác sĩ TẤT CẢ thuốc đang dùng
            - Một số thuốc tương tác với thuốc lao

            **5. Điều trị dưới sự giám sát (DOT):**
            - Uống thuốc trước mặt nhân viên y tế
            - Đảm bảo uống đúng, đủ
            - Phòng ngừa kháng thuốc

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Triệu chứng nặng:**
            - Ho ra máu nhiều
            - Khó thở nặng
            - Sốt cao, không hạ
            - Đau ngực dữ dội

            **2. Tác dụng phụ thuốc:**
            - Nghiêm trọng, không chịu được
            - Tổn thương mắt (nhìn mờ)
            - Vàng da, vàng mắt

            **3. Không cải thiện:**
            - Sau 2-3 tháng điều trị
            - Triệu chứng không giảm

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Khi bị lao:**
            - Tuân thủ điều trị nghiêm ngặt
            - Uống thuốc đúng, đủ thời gian
            - Chế độ ăn đủ chất
            - Nghỉ ngơi nhiều
            - Bảo vệ người khác (đeo khẩu trang, không khạc nhổ bừa bãi)

            **2. Phòng ngừa:**
            - Tiêm BCG cho trẻ
            - Phát hiện sớm (ho > 2 tuần → Khám)
            - Tránh tiếp xúc với người lao
            - Cải thiện điều kiện sống

            **3. Sống tích cực:**
            - Lao có thể chữa khỏi hoàn toàn
            - Tuân thủ điều trị → Khỏi bệnh
            - Đừng lo lắng quá mức
            - Hỗ trợ từ gia đình, xã hội

            **4. Không kỳ thị:**
            - Lao là bệnh có thể chữa khỏi
            - Người bệnh cần được hỗ trợ, không kỳ thị
            - Điều trị đúng → Không còn lây sau 2-3 tuần
            """,
            related_disease="tuberculosis",
            related_drugs=["Isoniazid", "Rifampicin", "Pyrazinamide", "Ethambutol"],
            printable=True
        ),

        PatientEducationTopic(
            id="hand_foot_mouth_basics",
            title="Understanding Hand Foot Mouth Disease",
            title_vn="Hiểu về Bệnh Tay chân miệng",
            category="Disease",
            content="""
            # Hiểu về Bệnh Tay chân miệng

            ## Tay chân miệng là gì?

            Tay chân miệng là bệnh truyền nhiễm do virus (chủ yếu Coxsackie A16, Enterovirus 71) gây ra, thường gặp ở trẻ em dưới 5 tuổi, đặc biệt trẻ dưới 3 tuổi.

            **⚠️ Đặc điểm:**
            - Bệnh theo mùa (tháng 3-5, 9-11)
            - Thường nhẹ, tự khỏi
            - Có thể nặng, gây biến chứng (hiếm)
            - Chưa có vắc xin, thuốc đặc trị

            **Triệu chứng điển hình:**
            - Sốt
            - Loét miệng
            - Phát ban ở tay, chân

            ## Triệu chứng:

            **Giai đoạn ủ bệnh (3-7 ngày):**
            - Không có triệu chứng

            **Giai đoạn khởi phát (1-2 ngày):**
            - **Sốt:** 38-39°C
            - **Mệt mỏi:** Trẻ quấy khóc
            - **Chán ăn:** Do đau miệng
            - **Đau họng**

            **Giai đoạn toàn phát (3-10 ngày):**
            - **Loét miệng:**
              - Vết loét ở lưỡi, lợi, má trong
              - Đau, khó ăn, khó uống
              - Trẻ chảy nước dãi nhiều
            - **Phát ban:**
              - **Tay:** Lòng bàn tay, ngón tay
              - **Chân:** Lòng bàn chân, ngón chân
              - **Mông, đầu gối:** Có thể có
              - Ban đỏ, có thể có bọng nước
              - Không ngứa
            - **Sốt:** Có thể sốt cao

            **Giai đoạn hồi phục:**
            - Sốt giảm
            - Vết loét lành
            - Phát ban biến mất
            - Tự khỏi sau 7-10 ngày

            **⚠️ Dấu hiệu cảnh báo (Cần nhập viện):**
            - Sốt cao > 39°C, không hạ
            - Giật mình, run tay chân
            - Quấy khóc liên tục
            - Khó thở
            - Da xanh, môi tím
            - Nôn nhiều
            - Lú lẫn, hôn mê

            ## Nguyên nhân và đường lây:

            **1. Nguyên nhân:**
            - Virus Coxsackie A16 (thường nhẹ)
            - Enterovirus 71 (có thể nặng, biến chứng)

            **2. Đường lây:**
            - **Tiếp xúc trực tiếp:** Dịch mũi, họng, nước bọt
            - **Phân:** Virus trong phân (lây qua tay bẩn)
            - **Đồ dùng:** Dùng chung đồ chơi, bát đĩa
            - **Giọt bắn:** Ho, hắt hơi

            **3. Yếu tố nguy cơ:**
            - Trẻ < 5 tuổi (đặc biệt < 3 tuổi)
            - Mùa dịch (tháng 3-5, 9-11)
            - Nơi đông người: Nhà trẻ, mẫu giáo

            ## Chẩn đoán:

            **1. Chẩn đoán lâm sàng:**
            - Dựa vào triệu chứng: Sốt + loét miệng + phát ban tay chân
            - Không cần xét nghiệm (thường)

            **2. Xét nghiệm (nếu cần):**
            - PCR: Tìm virus trong dịch họng, phân
            - Thường chỉ làm khi có biến chứng

            ## Điều trị:

            **⚠️ QUAN TRỌNG:** Không có thuốc đặc trị! Chủ yếu điều trị triệu chứng.

            **1. Hạ sốt:**
            - **Paracetamol:** 10-15mg/kg/lần, cách 4-6 giờ
            - **Ibuprofen:** Nếu Paracetamol không đủ (hỏi bác sĩ)
            - **Lau người:** Nước ấm

            **2. Giảm đau miệng:**
            - **Gel bôi miệng:** Lidocaine (theo chỉ định bác sĩ)
            - **Súc miệng:** Nước muối (nếu trẻ lớn)
            - **Tránh:** Thức ăn cay, nóng, chua

            **3. Hỗ trợ:**
            - **Uống nhiều nước:** Tránh mất nước
            - **Nghỉ ngơi:** Nghỉ ở nhà, không đi học
            - **Theo dõi:** Dấu hiệu cảnh báo

            **4. Không dùng:**
            - Kháng sinh (không hiệu quả với virus)
    - Aspirin (nguy hiểm ở trẻ em)

            ## 🍽️ CHẾ ĐỘ ĂN CHO TRẺ BỊ TAY CHÂN MIỆNG:

            **⚠️ QUAN TRỌNG:** Trẻ đau miệng → Khó ăn → Cần thức ăn mềm, dễ nuốt!

            **1. Nguyên tắc:**
            - **Thức ăn mềm, lỏng:** Dễ nuốt, không đau
            - **Mát, không nóng:** Tránh kích thích vết loét
            - **Không cay, chua:** Tránh đau
            - **Chia nhỏ bữa:** 5-6 bữa/ngày
            - **Uống nhiều nước:** Tránh mất nước

            **2. Thực phẩm NÊN ĂN:**
            - **Cháo, súp:** Mềm, dễ nuốt
              - Cháo gà, cháo thịt bằm
              - Súp rau củ
            - **Sữa:** Sữa mát, sữa chua
            - **Trái cây mềm:** Chuối, đu đủ, xoài chín (xay nhuyễn)
            - **Kem, sữa chua:** Mát, giảm đau miệng
            - **Nước trái cây:** Cam, chanh (pha loãng, không quá chua)

            **3. Thực phẩm CẦN TRÁNH:**
            - **Thức ăn cứng:** Bánh quy, bánh mì cứng
            - **Thức ăn cay:** Ớt, tiêu
            - **Thức ăn chua:** Chanh, dấm, cam chua
            - **Thức ăn nóng:** Nóng → Đau vết loét
            - **Thức ăn mặn:** Kích thích vết loét

            **4. Cách cho trẻ ăn:**
            - **Cho ăn bằng thìa:** Nhỏ, mềm
            - **Cho uống bằng ống hút:** Nếu đau miệng nhiều
            - **Cho ăn chậm:** Không ép
            - **Nghỉ giữa các miếng:** Để trẻ đỡ đau

            **5. Uống nước:**
            - **Nước lọc:** Mát
            - **Nước trái cây:** Pha loãng
            - **Sữa:** Mát
            - **Oresol:** Nếu sốt cao, mất nước
            - **⚠️ Quan trọng:** Uống nhiều để tránh mất nước!

            **6. Thực đơn mẫu (1 ngày):**
            - **Sáng:** Cháo gà mát + sữa
            - **Bữa phụ (10h):** Sữa chua, chuối xay
            - **Trưa:** Súp rau củ mát
            - **Bữa phụ (15h):** Kem, nước trái cây
            - **Tối:** Cháo thịt bằm mát + sữa
            - **Bữa phụ (21h):** Sữa ấm

            ## 💤 CHĂM SÓC TẠI NHÀ:

            **1. Nghỉ ngơi:**
            - Nghỉ ở nhà, không đi học
            - Nghỉ ít nhất 7-10 ngày
            - Tránh tiếp xúc với trẻ khác

            **2. Hạ sốt:**
            - Paracetamol đúng liều
            - Lau người bằng nước ấm
            - Mặc quần áo thoáng

            **3. Vệ sinh:**
            - **Rửa tay:** Thường xuyên (người chăm sóc và trẻ)
            - **Vệ sinh răng miệng:** Nhẹ nhàng, không làm đau vết loét
            - **Tắm:** Tắm nhanh, nhẹ nhàng
            - **Quần áo:** Sạch, thoáng

            **4. Theo dõi:**
            - Đo nhiệt độ 3-4 lần/ngày
            - Theo dõi dấu hiệu cảnh báo
            - Ghi nhật ký triệu chứng

            **5. Phòng ngừa lây lan:**
            - Cách ly trẻ (không đi học)
            - Không dùng chung đồ dùng
            - Vệ sinh đồ chơi, bát đĩa
            - Rửa tay thường xuyên

            ## 🛡️ PHÒNG NGỪA:

            **1. Vệ sinh cá nhân:**
            - **Rửa tay:** Thường xuyên với xà phòng
              - Trước khi ăn
              - Sau khi đi vệ sinh
              - Sau khi thay tã
              - Sau khi chơi
            - **Vệ sinh răng miệng:** Đánh răng 2 lần/ngày

            **2. Vệ sinh môi trường:**
            - **Lau sạch:** Bề mặt, đồ chơi, bàn ghế
            - **Khử trùng:** Dùng dung dịch khử trùng
            - **Thông thoáng:** Phòng ốc, nhà cửa

            **3. Tránh tiếp xúc:**
            - Tránh người bệnh
            - Không dùng chung đồ dùng
            - Không đến nơi đông người khi có dịch

            **4. Khi có dịch:**
            - Đóng cửa nhà trẻ, mẫu giáo (nếu cần)
            - Tăng cường vệ sinh
            - Phát hiện sớm, cách ly

            **5. Chưa có vắc xin:**
            - Vắc xin đang nghiên cứu
            - Phòng ngừa chủ yếu bằng vệ sinh

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Dấu hiệu cảnh báo:**
            - Sốt cao > 39°C, không hạ
            - Giật mình, run tay chân
            - Quấy khóc liên tục
            - Khó thở
            - Da xanh, môi tím
            - Nôn nhiều
            - Lú lẫn, hôn mê

            **2. Mất nước:**
            - Không uống được nước
            - Tiểu ít hoặc không tiểu
            - Mắt trũng, da khô
            - Mệt mỏi cực độ

            **3. Biến chứng:**
            - Viêm não, viêm màng não
            - Viêm cơ tim
            - Suy hô hấp

            **⚠️ QUAN TRỌNG:** Đến bệnh viện ngay khi có dấu hiệu cảnh báo!

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Khi trẻ bị tay chân miệng:**
            - Nghỉ ở nhà, không đi học
            - Chế độ ăn mềm, mát
            - Uống nhiều nước
            - Hạ sốt, giảm đau
            - Theo dõi dấu hiệu cảnh báo

            **2. Phòng ngừa:**
            - Rửa tay thường xuyên
            - Vệ sinh môi trường
            - Tránh tiếp xúc người bệnh

            **3. Không lo lắng quá:**
            - Hầu hết trẻ tự khỏi sau 7-10 ngày
            - Chỉ một số ít có biến chứng
            - Theo dõi sát, đến viện khi cần
            """,
            related_disease="hand_foot_mouth",
            related_drugs=["Paracetamol", "Ibuprofen"],
            printable=True
        ),

        PatientEducationTopic(
            id="influenza_basics",
            title="Understanding Influenza",
            title_vn="Hiểu về Cúm",
            category="Disease",
            content="""
            # Hiểu về Cúm

            ## Cúm là gì?

            Cúm (Influenza) là bệnh nhiễm trùng đường hô hấp do virus cúm gây ra, khác với cảm lạnh thông thường. Cúm thường nặng hơn và có thể gây biến chứng.

            **⚠️ Đặc điểm:**
            - Bệnh theo mùa (mùa đông, xuân)
            - Lây lan nhanh, dễ thành dịch
            - Có thể gây biến chứng nặng (viêm phổi, suy hô hấp)
            - Có vắc xin phòng ngừa

            **Phân loại:**
            - **Cúm A:** Phổ biến, có thể gây đại dịch
            - **Cúm B:** Ít phổ biến hơn
            - **Cúm C:** Nhẹ, ít gặp

            ## Triệu chứng:

            **Triệu chứng điển hình:**
            - **Sốt:** 38-40°C, đột ngột
            - **Ớn lạnh, run:** Kèm sốt
            - **Đau đầu:** Đau dữ dội
            - **Đau cơ, đau khớp:** Toàn thân
            - **Mệt mỏi:** Uể oải, không có sức
            - **Ho:** Ho khan hoặc có đờm
            - **Đau họng:** Có thể có
            - **Nghẹt mũi, chảy nước mũi:** Có thể có

            **Triệu chứng khác:**
            - Buồn nôn, nôn (thường ở trẻ em)
            - Tiêu chảy (thường ở trẻ em)
            - Chán ăn

            **⚠️ Phân biệt với cảm lạnh:**
            - **Cúm:** Sốt cao, đau cơ nhiều, mệt mỏi nặng, khởi phát đột ngột
            - **Cảm lạnh:** Sốt nhẹ hoặc không sốt, ít đau cơ, mệt mỏi nhẹ, khởi phát từ từ

            **Triệu chứng biến chứng:**
            - Khó thở, thở nhanh
            - Đau ngực
            - Sốt cao không hạ
            - Lú lẫn
            - Môi tím

            ## Nguyên nhân và đường lây:

            **1. Nguyên nhân:**
            - Virus cúm (Influenza virus)
            - Thay đổi kháng nguyên → Dịch mới mỗi năm

            **2. Đường lây:**
            - **Giọt bắn:** Ho, hắt hơi, nói chuyện
            - **Tiếp xúc:** Tay chạm vào bề mặt có virus → Chạm mắt, mũi, miệng
            - **Không khí:** Virus có thể tồn tại trong không khí

            **3. Yếu tố nguy cơ:**
            - **Tuổi:** Trẻ < 5 tuổi, người > 65 tuổi
            - **Bệnh mạn tính:** COPD, đái tháo đường, suy tim
            - **Suy giảm miễn dịch:** HIV, dùng thuốc ức chế miễn dịch
            - **Mang thai**
            - **Béo phì**

            ## Chẩn đoán:

            **1. Chẩn đoán lâm sàng:**
            - Dựa vào triệu chứng và mùa dịch
            - Thường không cần xét nghiệm

            **2. Xét nghiệm (nếu cần):**
            - **Test nhanh:** Phết mũi, họng (kết quả trong 15 phút)
            - **PCR:** Chính xác hơn
            - Thường chỉ làm khi có biến chứng hoặc cần xác định

            ## Điều trị:

            **⚠️ QUAN TRỌNG:** Không có thuốc đặc trị! Chủ yếu điều trị triệu chứng.

            **1. Điều trị tại nhà (Cúm nhẹ):**
            - **Hạ sốt:** Paracetamol 500-1000mg mỗi 4-6 giờ
            - **Nghỉ ngơi:** Nghỉ hoàn toàn
            - **Uống nhiều nước:** 2-3 lít/ngày
            - **Theo dõi:** Triệu chứng

            **2. Thuốc kháng virus (Nếu cần):**
            - **Oseltamivir (Tamiflu):** Uống trong 48 giờ đầu
            - **Zanamivir:** Hít
            - Chỉ dùng khi có chỉ định bác sĩ
            - Giúp giảm triệu chứng, rút ngắn thời gian bệnh

            **3. Điều trị tại viện (Nếu nặng):**
            - Kháng virus
            - Hỗ trợ hô hấp (nếu cần)
            - Điều trị biến chứng

            **4. Không dùng:**
            - Kháng sinh (không hiệu quả với virus)
            - Aspirin ở trẻ em (nguy hiểm - hội chứng Reye)

            ## 🍽️ CHẾ ĐỘ ĂN KHI BỊ CÚM:

            **1. Nguyên tắc:**
            - **Ăn nhẹ, dễ tiêu:** Tránh đồ khó tiêu
            - **Uống nhiều nước:** Quan trọng!
            - **Đủ dinh dưỡng:** Giúp cơ thể chống lại bệnh
            - **Chia nhỏ bữa:** 5-6 bữa/ngày (nếu chán ăn)

            **2. Uống nước (QUAN TRỌNG!):**
            - **Nước lọc:** Tốt nhất
            - **Nước trái cây:** Cam, chanh (vitamin C)
            - **Súp, canh:** Vừa ăn vừa uống nước
            - **Trà gừng ấm:** Giảm ho, ấm cổ họng
            - **Oresol:** Nếu sốt cao, mất nước
            - **⚠️ Tránh:** Rượu bia, cà phê (làm mất nước)

            **3. Thực phẩm NÊN ĂN:**
            - **Súp, cháo:** Dễ nuốt, dễ tiêu, có nước
              - Cháo gà (tốt cho cảm cúm!)
              - Súp rau củ
              - Canh nóng
            - **Trái cây:** Cam, chanh, bưởi (vitamin C)
            - **Rau xanh:** Luộc, hấp (vitamin, chất xơ)
            - **Protein:** Thịt nạc, cá (luộc, hấp)
            - **Sữa ấm:** Dễ uống, có protein

            **4. Thực phẩm CẦN TRÁNH:**
            - **Đồ chiên, nhiều dầu mỡ:** Khó tiêu
            - **Đồ lạnh:** Làm ho nhiều hơn
            - **Đồ cay:** Kích thích ho
            - **Rượu bia:** Làm mất nước, giảm miễn dịch
            - **Đồ ngọt nhiều:** Bánh kẹo (giảm miễn dịch)

            **5. Thực đơn mẫu (1 ngày):**
            - **Sáng:** Cháo gà + nước cam
            - **Bữa phụ (10h):** Súp rau củ, nước chanh ấm
            - **Trưa:** Cháo thịt bằm + canh rau
            - **Bữa phụ (15h):** Sữa ấm, trái cây
            - **Tối:** Súp rau củ + nước trái cây
            - **Bữa phụ (21h):** Trà gừng ấm, sữa ấm

            **6. Lưu ý:**
            - Uống nước ngay cả khi không khát
            - Ăn chậm, nhai kỹ
            - Nếu không ăn được → Uống sữa, nước trái cây

            ## 💤 CHĂM SÓC TẠI NHÀ:

            **1. Nghỉ ngơi:**
            - Nghỉ hoàn toàn, không làm việc
            - Ngủ đủ giấc (8-10 giờ/đêm)
            - Tránh gắng sức

            **2. Hạ sốt:**
            - Paracetamol đúng liều
            - Lau người bằng nước ấm
            - Mặc quần áo thoáng
            - **⚠️ KHÔNG dùng Aspirin ở trẻ em!**

            **3. Giảm ho:**
            - Uống nước ấm
            - Xông hơi (nước nóng, thêm gừng)
            - Súc miệng nước muối
            - Kê gối cao khi ngủ

            **4. Vệ sinh:**
            - Rửa tay thường xuyên
            - Che miệng khi ho, hắt hơi (khăn giấy, khuỷu tay)
            - Vệ sinh răng miệng

            **5. Phòng ngừa lây lan:**
            - Ở nhà, không đi làm/đi học
            - Đeo khẩu trang khi ra ngoài
            - Không dùng chung đồ dùng
            - Vệ sinh bề mặt thường xuyên

            **6. Theo dõi:**
            - Đo nhiệt độ 3-4 lần/ngày
            - Theo dõi triệu chứng
            - Ghi nhật ký

            ## 🛡️ PHÒNG NGỪA:

            **1. Tiêm vắc xin cúm (QUAN TRỌNG NHẤT!):**
            - **Tiêm hàng năm:** Vì virus thay đổi mỗi năm
            - **Thời điểm:** Trước mùa cúm (tháng 9-11)
            - **Đối tượng:**
              - Trẻ > 6 tháng tuổi
              - Người > 65 tuổi
              - Người có bệnh mạn tính
              - Phụ nữ mang thai
              - Nhân viên y tế
            - **Hiệu quả:** 40-60% (giảm nguy cơ mắc, giảm mức độ nặng)

            **2. Vệ sinh cá nhân:**
            - **Rửa tay:** Thường xuyên với xà phòng, ít nhất 20 giây
            - **Che miệng:** Khi ho, hắt hơi
            - **Không chạm:** Mắt, mũi, miệng bằng tay bẩn

            **3. Tránh tiếp xúc:**
            - Tránh người bị cúm
            - Tránh nơi đông người khi có dịch
            - Đeo khẩu trang khi cần

            **4. Vệ sinh môi trường:**
            - Lau sạch bề mặt (bàn, tay nắm cửa)
            - Thông thoáng phòng ốc
            - Dùng dung dịch khử trùng

            **5. Tăng cường miễn dịch:**
            - Ăn đủ chất
            - Ngủ đủ giấc
            - Tập thể dục đều đặn
            - Quản lý stress

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Triệu chứng nặng:**
            - Khó thở, thở nhanh
            - Đau ngực
            - Sốt cao không hạ (> 39°C)
            - Lú lẫn
            - Môi tím

            **2. Yếu tố nguy cơ cao:**
            - Trẻ < 5 tuổi
            - Người > 65 tuổi
            - Có bệnh mạn tính nặng
            - Mang thai

            **3. Biến chứng:**
            - Viêm phổi
            - Suy hô hấp
            - Nhiễm trùng nặng

            **4. Không cải thiện:**
            - Sốt > 3 ngày không giảm
            - Triệu chứng nặng hơn

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Khi bị cúm:**
            - Nghỉ ngơi hoàn toàn
            - Uống nhiều nước
            - Hạ sốt đúng cách
            - Ăn nhẹ, dễ tiêu
            - Ở nhà, không đi làm/đi học

            **2. Phòng ngừa:**
            - Tiêm vắc xin cúm hàng năm (quan trọng nhất!)
            - Rửa tay thường xuyên
            - Tránh tiếp xúc người bệnh
            - Tăng cường miễn dịch

            **3. Mùa dịch:**
            - Mùa đông, xuân là mùa cúm
            - Cần phòng ngừa tích cực
            - Tiêm vắc xin trước mùa dịch

            **4. Không tự ý:**
            - Dùng kháng sinh (không hiệu quả)
            - Dùng Aspirin ở trẻ em (nguy hiểm)
            """,
            related_disease="influenza",
            related_drugs=["Paracetamol", "Oseltamivir"],
            printable=True
        ),

        PatientEducationTopic(
            id="hepatitis_a_basics",
            title="Understanding Hepatitis A",
            title_vn="Hiểu về Viêm gan A",
            category="Disease",
            content="""
            # Hiểu về Viêm gan A

            ## Viêm gan A là gì?

            Viêm gan A là bệnh nhiễm trùng gan do virus viêm gan A (HAV) gây ra, lây truyền qua đường tiêu hóa (phân-miệng). Khác với viêm gan B/C, viêm gan A thường tự khỏi và không gây viêm gan mạn.

            **⚠️ Đặc điểm:**
            - Lây qua đường tiêu hóa (phân-miệng)
            - Thường tự khỏi, không gây mạn tính
            - Có vắc xin phòng ngừa
            - Phổ biến ở nơi vệ sinh kém

            **So sánh với viêm gan B/C:**
            - **Viêm gan A:** Lây qua đường tiêu hóa, tự khỏi, có vắc xin
            - **Viêm gan B/C:** Lây qua máu, có thể mạn tính, B có vắc xin, C chưa có

            ## Triệu chứng:

            **Giai đoạn ủ bệnh (15-50 ngày):**
            - Không có triệu chứng

            **Giai đoạn tiền vàng da (1-2 tuần):**
            - **Mệt mỏi:** Uể oải, không có sức
            - **Chán ăn:** Không muốn ăn
            - **Buồn nôn, nôn:** Có thể có
            - **Sốt nhẹ:** Có thể có
            - **Đau bụng:** Vùng gan (bên phải)
            - **Đau cơ, đau khớp:** Có thể có

            **Giai đoạn vàng da (1-2 tuần):**
            - **Vàng da, vàng mắt:** Dấu hiệu điển hình
            - **Nước tiểu sẫm màu:** Như nước trà đặc
            - **Phân nhạt màu:** Trắng, xám
            - **Triệu chứng giảm:** Mệt mỏi, chán ăn giảm

            **Giai đoạn hồi phục (2-4 tuần):**
            - Vàng da giảm
            - Ăn uống tốt hơn
            - Tự khỏi hoàn toàn

            **⚠️ Lưu ý:** Nhiều người (đặc biệt trẻ em) không có triệu chứng hoặc triệu chứng nhẹ!

            ## Nguyên nhân và đường lây:

            **1. Nguyên nhân:**
            - Virus viêm gan A (HAV)
            - Lây qua đường tiêu hóa

            **2. Đường lây:**
            - **Phân-miệng:** Phân người bệnh → Nước, thức ăn → Vào miệng
            - **Thức ăn, nước uống:** Nhiễm virus (không nấu chín, không đun sôi)
            - **Tay bẩn:** Tay dính phân → Chạm miệng
            - **Tiếp xúc gần:** Sống chung, chăm sóc người bệnh

            **3. Yếu tố nguy cơ:**
            - Vệ sinh kém
            - Nước uống không sạch
            - Thức ăn không nấu chín
            - Sống chung với người bệnh
            - Đi du lịch vùng có dịch

            **4. KHÔNG lây qua:**
            - Ôm, hôn
            - Ho, hắt hơi
            - Dùng chung bát đĩa (nếu rửa sạch)
            - Muỗi đốt

            ## Chẩn đoán:

            **1. Xét nghiệm máu:**
            - **Anti-HAV IgM:** Dương tính (viêm gan A cấp)
            - **Anti-HAV IgG:** Dương tính (đã từng bị hoặc đã tiêm vắc xin)

            **2. Xét nghiệm chức năng gan:**
            - AST, ALT: Tăng (men gan)
            - Bilirubin: Tăng (vàng da)

            **3. Thường không cần:**
            - Hầu hết chẩn đoán dựa vào triệu chứng và xét nghiệm

            ## Điều trị:

            **⚠️ QUAN TRỌNG:** Không có thuốc đặc trị! Chủ yếu điều trị hỗ trợ.

            **1. Điều trị hỗ trợ:**
            - **Nghỉ ngơi:** Nghỉ hoàn toàn, không làm việc
            - **Uống nhiều nước:** 2-3 lít/ngày
            - **Chế độ ăn:** Nhẹ, dễ tiêu, đủ dinh dưỡng
            - **Tránh rượu bia:** Hoàn toàn! (làm tổn thương gan nặng hơn)

            **2. Thuốc:**
            - **Hạ sốt, giảm đau:** Paracetamol (thận trọng, liều thấp)
            - **Chống nôn:** Nếu nôn nhiều
            - **⚠️ KHÔNG dùng:** Thuốc không cần thiết (tăng gánh nặng cho gan)

            **3. Theo dõi:**
            - Xét nghiệm chức năng gan định kỳ
            - Theo dõi triệu chứng
            - Phát hiện biến chứng (hiếm)

            **4. Tự khỏi:**
            - Hầu hết tự khỏi sau 2-4 tuần
            - Không gây viêm gan mạn
            - Không cần điều trị đặc biệt

            ## 🍽️ CHẾ ĐỘ ĂN KHI BỊ VIÊM GAN A:

            **1. Nguyên tắc:**
            - **Bảo vệ gan:** Tránh gánh nặng cho gan
            - **Đủ dinh dưỡng:** Giúp gan phục hồi
            - **Dễ tiêu:** Tránh đồ khó tiêu
            - **Tránh rượu bia:** Hoàn toàn!

            **2. Uống nước:**
            - **Nước lọc:** Tốt nhất
            - **Nước trái cây:** Cam, chanh (vitamin C)
            - **Súp, canh:** Vừa ăn vừa uống nước
            - **⚠️ Tránh:** Rượu bia, cà phê (làm mất nước)

            **3. Thực phẩm NÊN ĂN:**
            - **Cháo, súp:** Dễ tiêu, có nước
              - Cháo gà, cháo thịt bằm
              - Súp rau củ
            - **Protein nạc:** Thịt gà (bỏ da), cá, đậu phụ (luộc, hấp)
              - Giúp phục hồi tế bào gan
            - **Rau xanh:** Luộc, hấp (rau cải, rau muống, bông cải)
              - Vitamin, chất xơ
            - **Trái cây:** Cam, bưởi, táo (vitamin C)
            - **Sữa ít béo:** Sữa tách béo, sữa chua
            - **Ngũ cốc:** Gạo, bánh mì, yến mạch

            **4. Thực phẩm CẦN TRÁNH:**
            - **Rượu bia:** HOÀN TOÀN! (làm tổn thương gan nặng hơn)
            - **Thực phẩm nhiều chất béo:** Đồ chiên rán, mỡ động vật
            - **Thực phẩm chế biến sẵn:** Đồ hộp, thức ăn nhanh
            - **Thực phẩm sống:** Gỏi, sushi (nguy cơ nhiễm khuẩn)
            - **Đồ cay:** Kích thích dạ dày

            **5. Thực đơn mẫu (1 ngày):**
            - **Sáng:** Cháo gà + sữa ít béo
            - **Trưa:** 1 chén cơm + cá hấp + rau luộc + canh rau
            - **Tối:** 1 chén cơm + thịt gà luộc (bỏ da) + rau luộc + canh
            - **Bữa phụ:** Trái cây, sữa chua

            **6. Lưu ý:**
            - Ăn đều đặn, không bỏ bữa
            - Ăn chậm, nhai kỹ
            - Chia nhỏ bữa nếu chán ăn
            - Uống đủ nước (2-3 lít/ngày)

            ## 🏃 TẬP THỂ DỤC:

            **1. Khi đang viêm gan A:**
            - **Nghỉ ngơi:** Không tập thể dục
            - Nghỉ hoàn toàn cho đến khi hồi phục

            **2. Sau khi khỏi:**
            - **Tập thể dục dần:** Tăng dần cường độ
            - **Đi bộ:** 20-30 phút/ngày
            - **Tập nhẹ nhàng:** Không gắng sức
            - **Mục tiêu:** Tăng sức khỏe, phục hồi

            ## 🛡️ PHÒNG NGỪA:

            **1. Vệ sinh cá nhân:**
            - **Rửa tay:** Thường xuyên với xà phòng
              - Trước khi ăn
              - Sau khi đi vệ sinh
              - Sau khi thay tã
              - Sau khi chăm sóc người bệnh
            - **Vệ sinh răng miệng:** Đánh răng 2 lần/ngày

            **2. Vệ sinh thực phẩm:**
            - **Nấu chín:** Thức ăn phải nấu chín kỹ
            - **Rửa sạch:** Rau, trái cây
            - **Tránh:** Thức ăn sống, không rõ nguồn gốc

            **3. Nước uống:**
            - **Đun sôi:** Nước uống phải đun sôi
            - **Sạch:** Dùng nước sạch
            - **Tránh:** Nước chưa đun sôi, nước đá không rõ nguồn gốc

            **4. Vệ sinh môi trường:**
            - Vệ sinh nhà cửa
            - Xử lý phân đúng cách
            - Diệt ruồi, gián

            **5. Tiêm vắc xin (QUAN TRỌNG!):**
            - **Vắc xin viêm gan A:** 2 mũi (0, 6-12 tháng)
            - **Đối tượng:**
              - Trẻ em (từ 1 tuổi)
              - Người đi du lịch vùng có dịch
              - Người có bệnh gan mạn
              - Nhân viên y tế
            - **Hiệu quả:** > 95%
            - **Bảo vệ:** 20-25 năm (có thể suốt đời)

            **6. Khi có người bệnh:**
            - Cách ly (không dùng chung đồ dùng)
            - Vệ sinh tay thường xuyên
            - Vệ sinh bề mặt, dụng cụ
            - Rửa tay sau khi chăm sóc

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Viêm gan A nặng:**
            - Vàng da nặng
            - Nôn nhiều, không ăn được
            - Lú lẫn, buồn ngủ
            - Chảy máu

            **2. Biến chứng (Hiếm):**
            - Suy gan cấp
            - Viêm gan tối cấp

            **3. Không cải thiện:**
            - Triệu chứng kéo dài > 4 tuần
            - Triệu chứng nặng hơn

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Khi bị viêm gan A:**
            - Nghỉ ngơi hoàn toàn
            - Uống nhiều nước
            - Chế độ ăn lành mạnh
            - Tránh rượu bia hoàn toàn
            - Vệ sinh tay thường xuyên (tránh lây cho người khác)

            **2. Phòng ngừa:**
            - Tiêm vắc xin viêm gan A (quan trọng!)
            - Rửa tay thường xuyên
            - Vệ sinh thực phẩm
            - Nước uống sạch

            **3. Sống tích cực:**
            - Viêm gan A thường tự khỏi
            - Không gây viêm gan mạn
            - Phục hồi hoàn toàn sau 2-4 tuần
            """,
            related_disease="hepatitis_a",
            related_drugs=["Paracetamol"],
            printable=True
        ),

        PatientEducationTopic(
            id="malaria_basics",
            title="Understanding Malaria",
            title_vn="Hiểu về Sốt rét",
            category="Disease",
            content="""
            # Hiểu về Sốt rét

            ## Sốt rét là gì?

            Sốt rét là bệnh nhiễm ký sinh trùng do muỗi Anopheles truyền, vẫn còn lưu hành tại một số vùng miền núi Việt Nam. Bệnh có thể nặng và nguy hiểm nếu không điều trị kịp thời.

            **⚠️ Đặc điểm:**
            - Lây qua muỗi Anopheles đốt
            - Có thể gây sốt rét nặng (P. falciparum)
            - Phổ biến ở vùng miền núi, rừng
            - Có thể tái phát (P. vivax)

            **Các loại ký sinh trùng:**
            - **P. falciparum:** Nguy hiểm nhất, có thể gây sốt rét nặng
            - **P. vivax:** Có thể tái phát (thể ngủ trong gan)
            - **P. malariae:** Ít gặp
            - **P. ovale:** Rất hiếm

            ## Triệu chứng:

            **Sốt rét điển hình:**
            - **Sốt cao đột ngột:** 39-40°C
            - **Ớn lạnh, rét run:** Dữ dội, kéo dài 15-60 phút
            - **Vã mồ hôi:** Sau sốt, kéo dài 2-4 giờ
            - **Chu kỳ sốt:** 
              - P. falciparum: Không đều (mỗi ngày)
              - P. vivax: 48 giờ (cách ngày)
              - P. malariae: 72 giờ (cách 2 ngày)

            **Triệu chứng khác:**
            - Đau đầu dữ dội
            - Đau cơ, đau khớp
            - Mệt mỏi, suy nhược
            - Buồn nôn, nôn
            - Thiếu máu (nếu kéo dài)
            - Lách to (nếu mạn tính)

            **⚠️ Sốt rét nặng (P. falciparum):**
            - Rối loạn ý thức, hôn mê
            - Co giật
            - Suy thận cấp
            - Sốc
            - Thiếu máu nặng
            - Suy hô hấp
            - **Cần cấp cứu ngay!**

            ## Nguyên nhân và đường lây:

            **1. Nguyên nhân:**
            - Ký sinh trùng Plasmodium
            - Muỗi Anopheles truyền

            **2. Đường lây:**
            - Muỗi Anopheles đốt người bệnh → Hút ký sinh trùng → Đốt người lành → Lây bệnh
            - **KHÔNG lây:** Qua tiếp xúc, hô hấp, nước bọt

            **3. Yếu tố nguy cơ:**
            - Sống/đi du lịch vùng lưu hành sốt rét
            - Không có biện pháp phòng ngừa
            - Làm việc trong rừng, ban đêm

            ## Chẩn đoán:

            **Xét nghiệm:**
            - **Thick/thin smear (phết máu):** Tìm ký sinh trùng - chuẩn vàng
            - **Test nhanh (RDT):** Phát hiện kháng nguyên
            - **PCR:** Xác định loài (nếu cần)
            - **Công thức máu:** Thiếu máu, giảm tiểu cầu

            **⚠️ Quan trọng:**
            - Nếu có sốt + tiền sử vùng lưu hành → Nghĩ đến sốt rét
            - Xét nghiệm ngay để chẩn đoán sớm

            ## Điều trị:

            **1. Sốt rét thường (P. falciparum):**
            - **Artesunate + Mefloquine** (3 ngày)
            - Hoặc **Artemether-Lumefantrine** (3 ngày)
            - **Quan trọng:** Uống đủ liều, đúng giờ

            **2. Sốt rét thường (P. vivax):**
            - **Chloroquine** (3 ngày) + **Primaquine** (14 ngày)
            - Primaquine: Diệt thể ngủ trong gan (tránh tái phát)
            - **⚠️ Lưu ý:** Kiểm tra G6PD trước khi dùng Primaquine

            **3. Sốt rét nặng:**
            - **Artesunate IV** (tại bệnh viện)
            - Theo dõi sát, điều trị biến chứng

            **4. Phòng ngừa tái phát (P. vivax):**
            - Primaquine 14 ngày (nếu G6PD bình thường)

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Khi sốt:**
            - Uống nhiều nước (quan trọng!)
            - Ăn nhẹ, dễ tiêu
            - Súp, cháo
            - Trái cây, nước trái cây

            **2. Khi hết sốt:**
            - Ăn đủ dinh dưỡng
            - Bổ sung sắt (nếu thiếu máu)
            - Thịt nạc, cá, trứng
            - Rau xanh, trái cây

            **3. Thực đơn mẫu (khi hết sốt):**
            - **Sáng:** Cháo thịt, trứng
            - **Trưa:** Cơm, thịt/cá, rau xanh, canh
            - **Chiều:** Cơm, thịt/cá, rau xanh, canh
            - **Bữa phụ:** Sữa, trái cây

            **4. Tránh:**
            - Rượu bia (khi đang điều trị)
            - Đồ cay, nóng (khi sốt)

            ## 🏃 TẬP THỂ DỤC:

            **1. Khi đang sốt:**
            - Nghỉ ngơi hoàn toàn
            - Không tập thể dục

            **2. Sau khi hết sốt:**
            - Nghỉ ngơi thêm 1-2 tuần
            - Tập nhẹ: Đi bộ 10-15 phút/ngày
            - Tăng dần khi sức khỏe tốt hơn

            **3. Khi đã khỏi:**
            - Tập thể dục bình thường
            - Đi bộ, chạy bộ, bơi lội
            - 30 phút/ngày, 5 ngày/tuần

            ## 💊 QUẢN LÝ THUỐC:

            **1. Uống đúng cách:**
            - Uống đủ liều, đúng giờ
            - Không tự ý ngừng thuốc
            - Uống với nước, sau ăn

            **2. Thuốc phòng ngừa (nếu đi vùng lưu hành):**
            - **Doxycycline:** 100mg/ngày (bắt đầu 1-2 ngày trước, tiếp tục 4 tuần sau khi rời)
            - **Mefloquine:** 250mg/tuần (bắt đầu 1-2 tuần trước, tiếp tục 4 tuần sau)
            - **Atovaquone-Proguanil:** 1 viên/ngày (bắt đầu 1-2 ngày trước, tiếp tục 1 tuần sau)

            **3. Tác dụng phụ:**
            - **Mefloquine:** Chóng mặt, buồn nôn, rối loạn tâm thần (hiếm)
            - **Primaquine:** Thiếu máu tan máu (nếu thiếu G6PD)
            - **Artesunate:** Ít tác dụng phụ

            **4. Lưu ý:**
            - Báo bác sĩ nếu có tác dụng phụ
            - Không tự ý đổi thuốc

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Sốt rét nặng:**
            - Sốt cao + rối loạn ý thức
            - Co giật
            - Khó thở
            - Nôn nhiều, không uống được
            - Vàng da
            - Tiểu ít hoặc không tiểu

            **2. Sốt rét thường nhưng:**
            - Sốt cao kéo dài > 3 ngày
            - Không đáp ứng điều trị
            - Thiếu máu nặng
            - Có biến chứng

            **3. Tái phát:**
            - Sốt lại sau khi đã điều trị
            - Cần điều trị lại

            ## 💡 PHÒNG NGỪA:

            **1. Tránh muỗi đốt:**
            - Ngủ màn (quan trọng nhất!)
            - Mặc quần áo dài tay, dài chân
            - Dùng thuốc chống muỗi (DEET 20-30%)
            - Tránh ra ngoài ban đêm, sáng sớm

            **2. Diệt muỗi:**
            - Phun thuốc diệt muỗi
            - Diệt lăng quăng
            - Vệ sinh môi trường

            **3. Thuốc phòng ngừa:**
            - Nếu đi vùng lưu hành: Uống thuốc phòng
            - Bắt đầu trước khi đi, tiếp tục sau khi về

            **4. Phát hiện sớm:**
            - Nếu sốt sau khi đi vùng lưu hành → Nghĩ đến sốt rét
            - Đến cơ sở y tế ngay

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Khi bị sốt rét:**
            - Nghỉ ngơi hoàn toàn
            - Uống nhiều nước
            - Uống thuốc đúng, đủ liều
            - Theo dõi triệu chứng

            **2. Phòng ngừa:**
            - Ngủ màn (quan trọng nhất!)
            - Dùng thuốc phòng nếu đi vùng lưu hành
            - Vệ sinh môi trường

            **3. Sau khi khỏi:**
            - Tiếp tục phòng ngừa (có thể tái nhiễm)
            - Theo dõi tái phát (P. vivax)

            **4. Sống tích cực:**
            - Sốt rét có thể chữa khỏi
            - Điều trị sớm, đúng cách → Khỏi hoàn toàn
            - Phòng ngừa tốt → Không mắc bệnh
            """,
            related_disease="malaria",
            related_drugs=["Artesunate", "Mefloquine", "Chloroquine", "Primaquine", "Doxycycline"],
            printable=True
        ),

        PatientEducationTopic(
            id="acute_pharyngitis_basics",
            title="Understanding Acute Pharyngitis",
            title_vn="Hiểu về Viêm họng cấp",
            category="Disease",
            content="""
            # Hiểu về Viêm họng cấp

            ## Viêm họng cấp là gì?

            Viêm họng cấp là tình trạng viêm nhiễm cấp tính vùng họng, rất phổ biến tại Việt Nam, đặc biệt khi thay đổi thời tiết. Hầu hết do virus, tự khỏi.

            **⚠️ Đặc điểm:**
            - Viêm nhiễm cấp tính vùng họng
            - Rất phổ biến (đặc biệt trẻ em)
            - 80-90% do virus (tự khỏi)
            - 10-20% do vi khuẩn (cần kháng sinh)

            ## Triệu chứng:

            **Triệu chứng chung:**
            - Đau họng, rát họng (đặc biệt khi nuốt)
            - Khó nuốt
            - Sốt (nhẹ nếu virus, cao nếu vi khuẩn)
            - Ho, sổ mũi (nếu virus)
            - Sưng hạch cổ

            **Triệu chứng vi khuẩn (Strep):**
            - Sốt cao (> 38.5°C)
            - Họng đỏ, có mủ
            - Không ho, không sổ mũi

            ## Điều trị:

            **1. Virus (hầu hết):**
            - Điều trị triệu chứng: Paracetamol, Ibuprofen
            - Súc họng nước muối
            - Tự khỏi 3-7 ngày

            **2. Vi khuẩn (Strep):**
            - Kháng sinh: Amoxicillin 10 ngày
            - Uống đủ 10 ngày (quan trọng!)

            ## 🍽️ CHẾ ĐỘ ĂN:

            **Khi đau họng:**
            - Ăn mềm, lỏng: Cháo, súp, sữa
            - Uống nhiều nước ấm
            - Tránh đồ cay, nóng, cứng

            ## 💊 QUẢN LÝ THUỐC:

            - Paracetamol: Hạ sốt, giảm đau
            - Amoxicillin: Nếu vi khuẩn, uống đủ 10 ngày

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            - Khó thở, khó nuốt
            - Sốt cao > 39°C
            - Đau họng > 7 ngày
            - Áp xe quanh amidan

            ## 💡 PHÒNG NGỪA:

            - Rửa tay thường xuyên
            - Tránh tiếp xúc người bệnh
            - Tiêm vắc xin cúm
            """,
            related_disease="acute_pharyngitis",
            related_drugs=["Amoxicillin", "Penicillin V", "Azithromycin", "Paracetamol", "Ibuprofen"],
            printable=True
        ),

        PatientEducationTopic(
            id="otitis_media_basics",
            title="Understanding Otitis Media",
            title_vn="Hiểu về Viêm tai giữa",
            category="Disease",
            content="""
            # Hiểu về Viêm tai giữa

            ## Viêm tai giữa là gì?

            Viêm tai giữa là tình trạng viêm nhiễm tai giữa, rất phổ biến ở trẻ em tại Việt Nam. Bệnh có thể cấp tính hoặc mạn tính, ảnh hưởng đến thính lực nếu không điều trị đúng.

            **⚠️ Đặc điểm:**
            - Viêm nhiễm tai giữa
            - Rất phổ biến ở trẻ em (80% trẻ < 3 tuổi)
            - Có thể ảnh hưởng thính lực
            - Cần điều trị đúng để tránh biến chứng

            **Phân loại:**
            - **Viêm tai giữa cấp (AOM):** Nhiễm trùng cấp tính
            - **Viêm tai giữa có tràn dịch (OME):** Dịch trong tai giữa, không nhiễm trùng

            ## Triệu chứng:

            **Trẻ em:**
            - **Quấy khóc:** Đặc biệt ban đêm
            - **Kéo tai:** Dấu hiệu điển hình
            - **Sốt:** Có thể cao
            - **Chảy dịch tai:** Nếu thủng màng nhĩ
            - **Giảm thính lực:** Có thể có
            - **Mệt mỏi, chán ăn**

            **Người lớn:**
            - **Đau tai:** Đau nhói, đau vừa đến nặng
            - **Sốt**
            - **Chảy dịch tai:** Nếu thủng màng nhĩ
            - **Giảm thính lực**
            - **Ù tai**

            **⚠️ Biến chứng:**
            - Thủng màng nhĩ
            - Viêm xương chũm
            - Giảm thính lực vĩnh viễn
            - Viêm màng não (hiếm)

            ## Nguyên nhân:

            **1. Vi khuẩn:**
            - Streptococcus pneumoniae
            - Haemophilus influenzae
            - Moraxella catarrhalis

            **2. Virus:**
            - RSV, Rhinovirus

            **3. Yếu tố nguy cơ:**
            - Trẻ em (vòi nhĩ ngắn, nằm ngang)
            - Viêm đường hô hấp trên
            - Hút thuốc thụ động
            - Bú bình nằm
            - Đi nhà trẻ

            ## Chẩn đoán:

            **Khám:**
            - Soi tai: Màng nhĩ đỏ, phồng, có dịch
            - Đo nhĩ lượng (nếu có)

            ## Điều trị:

            **1. Trẻ > 2 tuổi, nhẹ:**
            - Có thể theo dõi 48-72 giờ
            - Điều trị triệu chứng: Paracetamol, Ibuprofen

            **2. Trẻ < 2 tuổi hoặc nặng:**
            - **Kháng sinh:** Amoxicillin (80-90 mg/kg/ngày)
            - **Nếu dị ứng Penicillin:** Azithromycin, Cefdinir
            - **Nếu kháng Amoxicillin:** Amoxicillin-clavulanate
            - **Thời gian:** 7-10 ngày

            **3. Điều trị triệu chứng:**
            - Paracetamol, Ibuprofen (giảm đau, hạ sốt)
            - Nhỏ tai (nếu thủng màng nhĩ, có chỉ định)

            **4. Phẫu thuật:**
            - Đặt ống thông khí (nếu tái phát nhiều lần)
            - Chọc màng nhĩ (nếu áp lực cao)

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Khi đang bệnh:**
            - Ăn bình thường, đủ dinh dưỡng
            - Uống nhiều nước
            - Tránh đồ cay, nóng (có thể làm đau họng → đau tai)

            **2. Trẻ em:**
            - Cho bú mẹ (nếu có thể)
            - Tránh bú bình nằm (tăng nguy cơ)

            **3. Thực đơn mẫu:**
            - **Sáng:** Cháo/cơm, thịt/cá, rau
            - **Trưa:** Cơm, thịt/cá, rau xanh, canh
            - **Chiều:** Cơm, thịt/cá, rau xanh, canh
            - **Bữa phụ:** Trái cây, sữa

            ## 🏃 TẬP THỂ DỤC:

            **1. Khi đang bệnh:**
            - Nghỉ ngơi, tránh tập thể dục
            - Tránh bơi lội (nước vào tai)

            **2. Khi đã khỏi:**
            - Tập bình thường
            - Đi bộ, chạy bộ
            - 30 phút/ngày, 5 ngày/tuần

            **3. Lưu ý:**
            - Tránh bơi lội nếu có thủng màng nhĩ
            - Đeo nút tai khi bơi (nếu cần)

            ## 💊 QUẢN LÝ THUỐC:

            **1. Kháng sinh:**
            - **Amoxicillin:** 80-90 mg/kg/ngày (trẻ em)
            - **Uống đủ 7-10 ngày** (quan trọng!)
            - Uống sau ăn

            **2. Giảm đau, hạ sốt:**
            - **Paracetamol:** 10-15 mg/kg x 3-4 lần/ngày
            - **Ibuprofen:** 10 mg/kg x 3 lần/ngày (sau ăn)

            **3. Tác dụng phụ:**
            - **Amoxicillin:** Tiêu chảy, phát ban (dị ứng)
            - **Ibuprofen:** Đau dạ dày (uống sau ăn)

            **4. Lưu ý:**
            - Uống đủ liều, đủ thời gian
            - Không tự ý ngừng

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Triệu chứng nặng:**
            - Đau tai dữ dội
            - Sốt cao > 39°C
            - Chảy dịch tai nhiều
            - Giảm thính lực rõ rệt

            **2. Biến chứng:**
            - Viêm xương chũm (đau sau tai, sưng)
            - Viêm màng não (sốt cao, cổ cứng, lú lẫn)
            - Thủng màng nhĩ không lành

            **3. Tái phát nhiều lần:**
            - ≥ 3 lần trong 6 tháng
            - Cần đánh giá đặt ống thông khí

            **4. Trẻ em:**
            - < 6 tháng tuổi
            - Sốt cao, không uống được
            - Quấy khóc nhiều

            ## 💡 PHÒNG NGỪA:

            **1. Tiêm chủng:**
            - Vắc xin phế cầu (PCV)
            - Vắc xin Hib
            - Vắc xin cúm

            **2. Cho con bú:**
            - Bú mẹ (giảm nguy cơ)
            - Tránh bú bình nằm

            **3. Môi trường:**
            - Tránh hút thuốc thụ động
            - Vệ sinh tay
            - Điều trị viêm đường hô hấp trên sớm

            **4. Trẻ em:**
            - Tránh đi nhà trẻ quá sớm (nếu có thể)
            - Vệ sinh mũi họng

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Khi bị viêm tai giữa:**
            - Nghỉ ngơi, uống nhiều nước
            - Dùng thuốc giảm đau, hạ sốt
            - Uống kháng sinh đủ liều, đủ thời gian
            - Không nhỏ bất kỳ gì vào tai (trừ khi có chỉ định)

            **2. Trẻ em:**
            - Theo dõi sát
            - Giảm đau (quan trọng!)
            - Không tự ý nhỏ thuốc vào tai

            **3. Sống tích cực:**
            - Hầu hết khỏi hoàn toàn
            - Điều trị đúng → Khỏi nhanh
            - Phòng ngừa tốt → Ít tái phát

            **4. Theo dõi:**
            - Khám lại sau 2-3 tuần (kiểm tra màng nhĩ)
            - Đo thính lực nếu tái phát nhiều lần
            """,
            related_disease="otitis_media",
            related_drugs=["Amoxicillin", "Amoxicillin-clavulanate", "Azithromycin", "Cefdinir", "Paracetamol", "Ibuprofen"],
            printable=True
        ),

        PatientEducationTopic(
            id="japanese_encephalitis_basics",
            title="Understanding Japanese Encephalitis",
            title_vn="Hiểu về Viêm não Nhật Bản",
            category="Disease",
            content="""
            # Hiểu về Viêm não Nhật Bản

            ## Viêm não Nhật Bản là gì?

            Viêm não Nhật Bản là bệnh nhiễm virus do muỗi Culex truyền, nguy hiểm, có thể gây tử vong hoặc di chứng thần kinh. Bệnh phổ biến tại Việt Nam, đặc biệt vùng nông thôn.

            **⚠️ Đặc điểm:**
            - Nhiễm virus do muỗi Culex truyền
            - Nguy hiểm, có thể tử vong (20-30%)
            - Di chứng thần kinh nặng
            - Phổ biến ở vùng nông thôn Việt Nam
            - Có vắc xin phòng ngừa

            **Đường lây:**
            - Muỗi Culex đốt lợn/chim nhiễm virus → Đốt người → Lây bệnh
            - **KHÔNG lây:** Qua tiếp xúc, hô hấp

            ## Triệu chứng:

            **Giai đoạn ủ bệnh (5-15 ngày):**
            - Không có triệu chứng

            **Giai đoạn cấp:**
            - **Sốt cao đột ngột:** 39-40°C
            - **Đau đầu dữ dội**
            - **Nôn, buồn nôn**
            - **Rối loạn ý thức:** Lú lẫn, hôn mê
            - **Co giật:** Có thể có
            - **Cứng gáy:** Dấu hiệu viêm màng não
            - **Liệt:** Có thể có

            **⚠️ Giai đoạn nặng:**
            - Hôn mê
            - Suy hô hấp
            - Sốc
            - Tử vong (20-30%)

            **⚠️ Lưu ý:**
            - Hầu hết nhiễm không có triệu chứng (99%)
            - Chỉ 1% có triệu chứng, nhưng rất nặng

            ## Nguyên nhân:

            **1. Virus:**
            - Japanese Encephalitis Virus (JEV)
            - Muỗi Culex truyền

            **2. Yếu tố nguy cơ:**
            - Sống vùng nông thôn
            - Mùa mưa (tăng muỗi)
            - Chưa tiêm vắc xin
            - Trẻ em (dễ mắc hơn)

            ## Chẩn đoán:

            **Xét nghiệm:**
            - **IgM JEV:** Dương tính (CSF hoặc máu)
            - **PCR:** Nếu có
            - **CT/MRI não:** Tổn thương thùy thái dương, nhân xám

            ## Điều trị:

            **1. Điều trị hỗ trợ:**
            - **Không có thuốc kháng virus đặc hiệu**
            - Hạ sốt: Paracetamol
            - Chống co giật: Phenobarbital, Phenytoin
            - Hỗ trợ hô hấp: Thở máy nếu cần
            - Hỗ trợ tuần hoàn: Truyền dịch, vận mạch

            **2. Corticosteroid:**
            - Có thể giúp giảm viêm
            - Dùng ngắn hạn

            **3. Vật lý trị liệu:**
            - Sau khi ổn định
            - Phục hồi chức năng

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Khi đang bệnh:**
            - Nếu hôn mê: Nuôi ăn qua ống
            - Nếu tỉnh: Ăn mềm, lỏng
            - Uống đủ nước

            **2. Sau khi khỏi:**
            - Ăn đủ dinh dưỡng
            - Protein: Thịt, cá, trứng
            - Rau xanh, trái cây
            - Bổ sung vitamin, khoáng chất

            **3. Thực đơn mẫu (sau khi khỏi):**
            - **Sáng:** Cháo thịt, trứng, sữa
            - **Trưa:** Cơm, thịt/cá, rau xanh, canh
            - **Chiều:** Cơm, thịt/cá, rau xanh, canh
            - **Bữa phụ:** Trái cây, sữa

            ## 🏃 TẬP THỂ DỤC:

            **1. Khi đang bệnh:**
            - Nghỉ ngơi hoàn toàn
            - Vật lý trị liệu (nếu có liệt)

            **2. Sau khi khỏi:**
            - Vật lý trị liệu (quan trọng!)
            - Phục hồi chức năng
            - Tập vận động từ từ

            **3. Lưu ý:**
            - Có thể có di chứng
            - Cần kiên nhẫn, tập luyện lâu dài

            ## 💊 QUẢN LÝ THUỐC:

            **1. Điều trị hỗ trợ:**
            - Paracetamol: Hạ sốt
            - Chống co giật: Phenobarbital, Phenytoin
            - Corticosteroid: Giảm viêm

            **2. Lưu ý:**
            - Điều trị tại bệnh viện
            - Theo dõi sát
            - Không có thuốc đặc hiệu

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Triệu chứng nặng:**
            - Sốt cao + đau đầu dữ dội
            - Rối loạn ý thức
            - Co giật
            - Cứng gáy
            - **Cấp cứu ngay!**

            **2. Di chứng:**
            - Liệt
            - Co giật
            - Chậm phát triển
            - Cần vật lý trị liệu

            ## 💡 PHÒNG NGỪA:

            **1. Tiêm vắc xin (QUAN TRỌNG NHẤT!):**
            - **Vắc xin JEV:** 2 mũi (0, 28 ngày), nhắc lại sau 1 năm
            - **Đối tượng:**
              - Trẻ em (từ 1 tuổi)
              - Người sống vùng lưu hành
              - Người đi du lịch vùng lưu hành
            - **Hiệu quả:** > 95%
            - **Bảo vệ:** 3-5 năm (cần nhắc lại)

            **2. Tránh muỗi đốt:**
            - Ngủ màn (quan trọng!)
            - Mặc quần áo dài tay, dài chân
            - Dùng thuốc chống muỗi (DEET 20-30%)
            - Tránh ra ngoài ban đêm, sáng sớm

            **3. Diệt muỗi:**
            - Phun thuốc diệt muỗi
            - Diệt lăng quăng
            - Vệ sinh môi trường

            **4. Môi trường:**
            - Tránh vùng có nhiều lợn, chim
            - Vệ sinh chuồng trại

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Phòng ngừa:**
            - **Tiêm vắc xin JEV** (quan trọng nhất!)
            - Ngủ màn
            - Tránh muỗi đốt

            **2. Khi bị viêm não Nhật Bản:**
            - Điều trị tại bệnh viện
            - Hỗ trợ hô hấp, tuần hoàn
            - Vật lý trị liệu sau khi khỏi

            **3. Di chứng:**
            - Có thể có di chứng thần kinh
            - Cần vật lý trị liệu lâu dài
            - Hỗ trợ gia đình

            **4. Sống tích cực:**
            - Phòng ngừa tốt → Không mắc bệnh
            - Tiêm vắc xin → Bảo vệ > 95%
            - Điều trị sớm → Giảm tử vong, di chứng

            **5. Trẻ em:**
            - Tiêm vắc xin từ 1 tuổi
            - Ngủ màn
            - Tránh muỗi đốt
            """,
            related_disease="japanese_encephalitis",
            related_drugs=["Paracetamol", "Phenobarbital", "Phenytoin", "Corticosteroid"],
            printable=True
        ),

        PatientEducationTopic(
            id="typhoid_fever_basics",
            title="Understanding Typhoid Fever",
            title_vn="Hiểu về Sốt thương hàn",
            category="Disease",
            content="""
            # Hiểu về Sốt thương hàn

            ## Sốt thương hàn là gì?

            Sốt thương hàn là bệnh nhiễm khuẩn do vi khuẩn Salmonella Typhi gây ra, lây qua đường tiêu hóa. Bệnh rất phổ biến ở Việt Nam, đặc biệt ở vùng nông thôn, nơi điều kiện vệ sinh kém.

            **⚠️ Đặc điểm:**
            - Bệnh nhiễm khuẩn đường tiêu hóa
            - Lây qua thức ăn, nước uống bị nhiễm khuẩn
            - Rất phổ biến ở Việt Nam
            - Có thể gây biến chứng nặng nếu không điều trị

            ## Triệu chứng:

            **Triệu chứng điển hình (tuần 1-2):**
            - **Sốt:** Sốt cao liên tục (39-40°C), tăng dần
            - **Đau đầu:** Đau đầu dữ dội
            - **Mệt mỏi, suy nhược**
            - **Đau bụng:** Đau bụng, đầy bụng
            - **Táo bón hoặc tiêu chảy:** Thường táo bón ở người lớn, tiêu chảy ở trẻ em
            - **Chán ăn**

            **Triệu chứng tuần 2-3:**
            - Sốt cao liên tục
            - **Ban đỏ:** Ban hồng (rose spots) trên ngực, bụng
            - **Lách to:** Có thể sờ thấy
            - **Nhịp tim chậm:** So với sốt cao (dấu hiệu đặc trưng)
            - **Lưỡi bẩn:** Lưỡi có lớp phủ trắng, viền đỏ

            **⚠️ Biến chứng:**
            - Xuất huyết tiêu hóa
            - Thủng ruột
            - Viêm màng não
            - Viêm xương
            - Tử vong (nếu không điều trị)

            ## Nguyên nhân:

            **1. Vi khuẩn:**
            - Salmonella Typhi
            - Lây qua đường tiêu hóa

            **2. Nguồn lây:**
            - Người bệnh hoặc người lành mang trùng
            - Phân, nước tiểu người bệnh
            - Thức ăn, nước uống bị nhiễm khuẩn
            - Rau sống, nước đá, hải sản

            **3. Yếu tố nguy cơ:**
            - Vệ sinh kém
            - Nước uống không sạch
            - Thức ăn không nấu chín
            - Vùng nông thôn, vùng lũ lụt

            ## Chẩn đoán:

            **Xét nghiệm:**
            - **Cấy máu:** Dương tính tuần 1-2
            - **Cấy phân:** Dương tính tuần 2-3
            - **Cấy tủy xương:** Rất nhạy
            - **Widal test:** Kháng thể (ít chính xác)
            - **Xét nghiệm nhanh:** PCR, kháng nguyên

            ## Điều trị:

            **1. Kháng sinh:**
            - **Ceftriaxone:** 2g/ngày, 7-14 ngày (thuốc đầu tay)
            - **Azithromycin:** 1g/ngày, 5-7 ngày
            - **Ciprofloxacin:** 500mg x 2 lần/ngày, 7-14 ngày (nếu nhạy cảm)
            - **Quan trọng:** Uống đủ liệu trình, không tự ý ngừng

            **2. Hạ sốt:**
            - Paracetamol: 500-1000mg mỗi 6 giờ
            - Chườm mát

            **3. Bù dịch:**
            - Uống nhiều nước
            - Oresol nếu tiêu chảy
            - Truyền dịch nếu nặng

            **4. Nghỉ ngơi:**
            - Nghỉ ngơi tại giường
            - Tránh gắng sức

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Khi đang sốt:**
            - Ăn mềm, lỏng: Cháo, súp
            - Uống nhiều nước: Nước lọc, nước trái cây
            - Oresol nếu tiêu chảy
            - Tránh thức ăn khó tiêu

            **2. Khi hết sốt:**
            - Ăn đủ dinh dưỡng
            - Protein: Thịt, cá, trứng (nấu chín)
            - Rau xanh (nấu chín)
            - Trái cây
            - Tránh rau sống, thức ăn tái

            **3. Thực đơn mẫu:**
            - **Sáng:** Cháo thịt, trứng
            - **Trưa:** Cơm, thịt/cá nấu chín, rau xanh nấu chín, canh
            - **Chiều:** Cơm, thịt/cá nấu chín, rau xanh nấu chín, canh
            - **Bữa phụ:** Trái cây, sữa

            **4. Lưu ý:**
            - **Nấu chín kỹ:** Tất cả thức ăn phải nấu chín
            - **Nước sạch:** Chỉ uống nước đun sôi
            - **Rửa tay:** Rửa tay trước khi ăn, sau khi đi vệ sinh

            ## 🏃 TẬP THỂ DỤC:

            **1. Khi đang bệnh:**
            - Nghỉ ngơi hoàn toàn
            - Tránh gắng sức
            - Nghỉ tại giường

            **2. Sau khi khỏi:**
            - Tập thể dục từ từ
            - Đi bộ nhẹ nhàng
            - Tăng dần cường độ

            ## 💊 QUẢN LÝ THUỐC:

            **1. Kháng sinh:**
            - Uống đủ liệu trình (7-14 ngày)
            - Uống đúng giờ, đúng liều
            - **Quan trọng:** Không tự ý ngừng (gây kháng thuốc, tái phát)

            **2. Hạ sốt:**
            - Paracetamol: Khi sốt > 38.5°C
            - Không quá 4g/ngày

            **3. Tác dụng phụ:**
            - Kháng sinh: Tiêu chảy, buồn nôn
            - Báo bác sĩ nếu có tác dụng phụ nặng

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Sốt cao liên tục:**
            - Sốt > 39°C, không giảm
            - Sốt kéo dài > 5 ngày

            **2. Biến chứng:**
            - Đau bụng dữ dội (thủng ruột)
            - Nôn ra máu, đi ngoài phân đen (xuất huyết)
            - Rối loạn ý thức (viêm màng não)

            **3. Mất nước:**
            - Không uống được
            - Tiêu chảy nhiều
            - Mệt mỏi nặng

            ## 💡 PHÒNG NGỪA:

            **1. Vệ sinh cá nhân:**
            - **Rửa tay:** Rửa tay bằng xà phòng trước khi ăn, sau khi đi vệ sinh
            - **Vệ sinh:** Giữ vệ sinh cá nhân sạch sẽ

            **2. Thức ăn, nước uống:**
            - **Nước sạch:** Chỉ uống nước đun sôi, nước đóng chai
            - **Nấu chín:** Tất cả thức ăn phải nấu chín kỹ
            - **Tránh:** Rau sống, thức ăn tái, nước đá không đảm bảo
            - **Rửa sạch:** Rửa sạch rau, trái cây trước khi ăn

            **3. Vệ sinh môi trường:**
            - Xử lý phân đúng cách
            - Vệ sinh nhà vệ sinh
            - Diệt ruồi, gián

            **4. Tiêm vắc xin:**
            - **Vắc xin Typhoid:** Có thể tiêm cho người đi du lịch vùng lưu hành
            - Hiệu quả: 50-80%
            - Bảo vệ: 2-3 năm

            **5. Khi có người bệnh:**
            - Cách ly người bệnh
            - Vệ sinh dụng cụ ăn uống
            - Rửa tay sau khi tiếp xúc

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Phòng ngừa:**
            - **Rửa tay** (quan trọng nhất!)
            - Uống nước sạch
            - Ăn thức ăn nấu chín
            - Tránh rau sống, nước đá không đảm bảo

            **2. Khi bị sốt thương hàn:**
            - Điều trị sớm (quan trọng!)
            - Uống kháng sinh đủ liệu trình
            - Nghỉ ngơi, uống nhiều nước
            - Ăn thức ăn nấu chín

            **3. Sống tích cực:**
            - Phòng ngừa tốt → Không mắc bệnh
            - Điều trị sớm → Khỏi hoàn toàn
            - Uống đủ kháng sinh → Tránh tái phát, kháng thuốc

            **4. Vùng nông thôn:**
            - Đặc biệt chú ý vệ sinh
            - Nước uống phải đun sôi
            - Thức ăn phải nấu chín
            - Rửa tay thường xuyên
            """,
            related_disease="typhoid_fever",
            related_drugs=["Ceftriaxone", "Azithromycin", "Ciprofloxacin", "Paracetamol", "Oresol"],
            printable=True
        ),

        PatientEducationTopic(
            id="giardiasis_basics",
            title="Understanding Giardiasis",
            title_vn="Hiểu về Nhiễm Giardia",
            category="Disease",
            content="""
            # Hiểu về Nhiễm Giardia

            ## Nhiễm Giardia là gì?

            Nhiễm Giardia là bệnh ký sinh trùng đường ruột do Giardia lamblia gây ra, đặc trưng bởi tiêu chảy, đau bụng, đầy hơi. Bệnh rất phổ biến ở Việt Nam, lây qua thức ăn, nước uống bị nhiễm ký sinh trùng.

            **⚠️ Đặc điểm:**
            - Bệnh ký sinh trùng đường ruột
            - Tiêu chảy, đau bụng, đầy hơi
            - Rất phổ biến ở Việt Nam
            - Lây qua thức ăn, nước uống

            ## Triệu chứng:

            **Triệu chứng điển hình:**
            - **Tiêu chảy:** Tiêu chảy nhiều nước, có mùi hôi, phân mỡ (steatorrhea)
            - **Đau bụng:** Đau bụng âm ỉ, đầy bụng
            - **Đầy hơi, chướng bụng:** Nhiều hơi
            - **Buồn nôn, nôn:** Có thể có
            - **Mệt mỏi, suy nhược**
            - **Sụt cân:** Do kém hấp thu

            **Triệu chứng khác:**
            - Sốt nhẹ (hiếm)
            - Đau đầu
            - Chán ăn

            **⚠️ Nhiễm mạn tính:**
            - Tiêu chảy tái phát
            - Kém hấp thu
            - Sụt cân
            - Thiếu vitamin, khoáng chất

            **⚠️ Không có triệu chứng:**
            - Nhiều người nhiễm không có triệu chứng
            - Vẫn có thể lây cho người khác

            ## Nguyên nhân:

            **1. Ký sinh trùng:**
            - Giardia lamblia
            - Sống ở ruột non

            **2. Lây truyền:**
            - **Thức ăn, nước uống:** Bị nhiễm ký sinh trùng
            - **Phân- miệng:** Từ người bệnh hoặc người lành mang trùng
            - **Nước:** Nước không được xử lý, nước giếng
            - **Thức ăn:** Rau sống, thức ăn không nấu chín

            **3. Yếu tố nguy cơ:**
            - Vệ sinh kém
            - Nước uống không sạch
            - Rau sống, thức ăn không nấu chín
            - Vùng nông thôn
            - Trẻ em, người suy giảm miễn dịch

            ## Chẩn đoán:

            **Xét nghiệm:**
            - **Soi phân:** Tìm kén Giardia (cần soi nhiều lần)
            - **Test nhanh:** Kháng nguyên trong phân
            - **PCR:** Phát hiện DNA

            ## Điều trị:

            **1. Thuốc:**
            - **Metronidazole:** 250mg x 3 lần/ngày, 5-7 ngày (thuốc đầu tay)
            - **Tinidazole:** 2g, uống 1 lần (hiệu quả cao)
            - **Nitazoxanide:** 500mg x 2 lần/ngày, 3 ngày
            - **Albendazole:** 400mg/ngày, 5 ngày

            **2. Bù dịch:**
            - Uống nhiều nước
            - Oresol nếu tiêu chảy nhiều
            - Truyền dịch nếu mất nước nặng

            **3. Dinh dưỡng:**
            - Ăn đủ dinh dưỡng
            - Bổ sung vitamin, khoáng chất nếu kém hấp thu

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Khi đang tiêu chảy:**
            - Ăn mềm, lỏng: Cháo, súp
            - Uống nhiều nước: Nước lọc, nước trái cây
            - Oresol nếu tiêu chảy nhiều
            - Tránh thức ăn khó tiêu, nhiều mỡ

            **2. Sau khi khỏi:**
            - Ăn đủ dinh dưỡng
            - Protein: Thịt, cá, trứng (nấu chín)
            - Rau xanh (nấu chín)
            - Trái cây
            - Tránh rau sống, thức ăn tái

            **3. Thực đơn mẫu:**
            - **Sáng:** Cháo thịt, trứng
            - **Trưa:** Cơm, thịt/cá nấu chín, rau xanh nấu chín, canh
            - **Chiều:** Cơm, thịt/cá nấu chín, rau xanh nấu chín, canh
            - **Bữa phụ:** Trái cây, sữa

            **4. Lưu ý:**
            - **Nấu chín kỹ:** Tất cả thức ăn phải nấu chín
            - **Nước sạch:** Chỉ uống nước đun sôi
            - **Rửa tay:** Rửa tay trước khi ăn, sau khi đi vệ sinh
            - **Tránh:** Rau sống, thức ăn tái, nước đá không đảm bảo

            ## 🏃 TẬP THỂ DỤC:

            **1. Khi đang bệnh:**
            - Nghỉ ngơi nếu mệt mỏi
            - Tránh gắng sức

            **2. Sau khi khỏi:**
            - Tập thể dục bình thường
            - Tăng dần cường độ

            ## 💊 QUẢN LÝ THUỐC:

            **1. Thuốc điều trị:**
            - Uống đủ liệu trình (5-7 ngày)
            - Uống đúng giờ, đúng liều
            - **Quan trọng:** Không tự ý ngừng (gây tái phát, kháng thuốc)

            **2. Tác dụng phụ:**
            - **Metronidazole:** Buồn nôn, đắng miệng, không uống rượu
            - Báo bác sĩ nếu có tác dụng phụ nặng

            **3. Lưu ý:**
            - Không uống rượu khi dùng Metronidazole (gây phản ứng)
            - Uống sau ăn (giảm buồn nôn)

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Tiêu chảy nặng:**
            - Tiêu chảy nhiều, không giảm
            - Mất nước nặng
            - Không uống được

            **2. Kém hấp thu:**
            - Sụt cân nhiều
            - Thiếu vitamin, khoáng chất nặng

            **3. Không đáp ứng điều trị:**
            - Tiêu chảy kéo dài sau điều trị
            - Tái phát nhiều lần

            ## 💡 PHÒNG NGỪA:

            **1. Vệ sinh cá nhân:**
            - **Rửa tay:** Rửa tay bằng xà phòng trước khi ăn, sau khi đi vệ sinh
            - **Vệ sinh:** Giữ vệ sinh cá nhân sạch sẽ

            **2. Thức ăn, nước uống:**
            - **Nước sạch:** Chỉ uống nước đun sôi, nước đóng chai
            - **Nấu chín:** Tất cả thức ăn phải nấu chín kỹ
            - **Tránh:** Rau sống, thức ăn tái, nước đá không đảm bảo
            - **Rửa sạch:** Rửa sạch rau, trái cây trước khi ăn

            **3. Vệ sinh môi trường:**
            - Xử lý phân đúng cách
            - Vệ sinh nhà vệ sinh
            - Vệ sinh nguồn nước

            **4. Khi có người bệnh:**
            - Điều trị người bệnh
            - Vệ sinh dụng cụ ăn uống
            - Rửa tay sau khi tiếp xúc

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Phòng ngừa:**
            - **Rửa tay** (quan trọng nhất!)
            - Uống nước sạch
            - Ăn thức ăn nấu chín
            - Tránh rau sống, nước đá không đảm bảo

            **2. Khi bị nhiễm Giardia:**
            - Điều trị sớm (quan trọng!)
            - Uống thuốc đủ liệu trình
            - Uống nhiều nước nếu tiêu chảy
            - Ăn thức ăn nấu chín

            **3. Sống tích cực:**
            - Phòng ngừa tốt → Không mắc bệnh
            - Điều trị sớm → Khỏi hoàn toàn
            - Uống đủ thuốc → Tránh tái phát

            **4. Vùng nông thôn:**
            - Đặc biệt chú ý vệ sinh
            - Nước uống phải đun sôi
            - Thức ăn phải nấu chín
            - Rửa tay thường xuyên
            """,
            related_disease="giardiasis",
            related_drugs=["Metronidazole", "Tinidazole", "Nitazoxanide", "Albendazole", "Oresol"],
            printable=True
        ),

        PatientEducationTopic(
            id="leptospirosis_basics",
            title="Understanding Leptospirosis",
            title_vn="Hiểu về Sốt vàng da xuất huyết",
            category="Disease",
            content="""
            # Hiểu về Sốt vàng da xuất huyết

            ## Sốt vàng da xuất huyết là gì?

            Sốt vàng da xuất huyết (Leptospirosis) là bệnh nhiễm khuẩn do xoắn khuẩn Leptospira gây ra, lây từ động vật sang người qua nước, đất bị nhiễm nước tiểu động vật. Bệnh phổ biến ở Việt Nam, đặc biệt vùng nông thôn, mùa mưa lũ.

            **⚠️ Đặc điểm:**
            - Bệnh nhiễm khuẩn từ động vật
            - Sốt, vàng da, xuất huyết
            - Phổ biến ở vùng nông thôn, mùa mưa lũ
            - Có thể gây biến chứng nặng

            ## Triệu chứng:

            **Giai đoạn 1 (tuần 1):**
            - **Sốt:** Sốt cao đột ngột (39-40°C)
            - **Đau đầu:** Đau đầu dữ dội
            - **Đau cơ:** Đau cơ toàn thân, đặc biệt bắp chân
            - **Đau mắt:** Đau mắt, sợ ánh sáng
            - **Mệt mỏi, suy nhược**
            - **Buồn nôn, nôn**
            - **Đỏ mắt:** Kết mạc đỏ

            **Giai đoạn 2 (tuần 2):**
            - **Vàng da:** Vàng da, vàng mắt
            - **Xuất huyết:** Chảy máu cam, xuất huyết da, xuất huyết tiêu hóa
            - **Suy thận:** Thiểu niệu, vô niệu
            - **Suy gan:** Men gan tăng
            - **Viêm màng não:** Đau đầu, cứng gáy

            **⚠️ Biến chứng nặng:**
            - Suy thận cấp
            - Suy gan
            - Xuất huyết phổi
            - Viêm màng não
            - Tử vong (nếu không điều trị)

            ## Nguyên nhân:

            **1. Vi khuẩn:**
            - Leptospira
            - Lây từ động vật sang người

            **2. Nguồn lây:**
            - **Động vật:** Chuột, chó, lợn, bò (nước tiểu)
            - **Nước, đất:** Bị nhiễm nước tiểu động vật
            - **Tiếp xúc:** Qua da, niêm mạc bị tổn thương
            - **Nuốt phải:** Nước bị nhiễm

            **3. Yếu tố nguy cơ:**
            - Làm ruộng, chăn nuôi
            - Tiếp xúc nước, đất bẩn
            - Mùa mưa lũ
            - Vùng nông thôn
            - Bơi lội ở ao, hồ, sông

            ## Chẩn đoán:

            **Xét nghiệm:**
            - **Cấy máu:** Dương tính tuần 1
            - **Cấy nước tiểu:** Dương tính tuần 2
            - **MAT (Microscopic Agglutination Test):** Kháng thể
            - **PCR:** Phát hiện DNA
            - **Xét nghiệm nhanh:** Kháng thể IgM

            ## Điều trị:

            **1. Kháng sinh:**
            - **Penicillin G:** 1.5 triệu đơn vị x 4 lần/ngày, 7 ngày (thuốc đầu tay)
            - **Doxycycline:** 100mg x 2 lần/ngày, 7 ngày
            - **Ceftriaxone:** 1g/ngày, 7 ngày
            - **Azithromycin:** 500mg/ngày, 3 ngày
            - **Quan trọng:** Điều trị sớm (trong 5 ngày đầu)

            **2. Điều trị hỗ trợ:**
            - Hạ sốt: Paracetamol
            - Bù dịch: Truyền dịch
            - Điều trị suy thận: Lọc máu nếu cần
            - Điều trị xuất huyết: Truyền máu, tiểu cầu nếu cần

            **3. Nghỉ ngơi:**
            - Nghỉ ngơi tại giường
            - Tránh gắng sức

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Khi đang sốt:**
            - Ăn mềm, lỏng: Cháo, súp
            - Uống nhiều nước: Nước lọc, nước trái cây
            - Tránh thức ăn khó tiêu

            **2. Khi có suy gan, suy thận:**
            - Hạn chế protein nếu suy thận nặng
            - Hạn chế muối nếu phù
            - Theo chỉ định bác sĩ

            **3. Sau khi khỏi:**
            - Ăn đủ dinh dưỡng
            - Protein: Thịt, cá, trứng (nấu chín)
            - Rau xanh, trái cây
            - Bổ sung vitamin, khoáng chất

            **4. Thực đơn mẫu:**
            - **Sáng:** Cháo thịt, trứng
            - **Trưa:** Cơm, thịt/cá nấu chín, rau xanh, canh
            - **Chiều:** Cơm, thịt/cá nấu chín, rau xanh, canh
            - **Bữa phụ:** Trái cây, sữa

            ## 🏃 TẬP THỂ DỤC:

            **1. Khi đang bệnh:**
            - Nghỉ ngơi hoàn toàn
            - Tránh gắng sức
            - Nghỉ tại giường

            **2. Sau khi khỏi:**
            - Tập thể dục từ từ
            - Đi bộ nhẹ nhàng
            - Tăng dần cường độ

            ## 💊 QUẢN LÝ THUỐC:

            **1. Kháng sinh:**
            - Uống đủ liệu trình (7 ngày)
            - Uống đúng giờ, đúng liều
            - **Quan trọng:** Điều trị sớm (trong 5 ngày đầu)

            **2. Hạ sốt:**
            - Paracetamol: Khi sốt > 38.5°C
            - Không quá 4g/ngày

            **3. Tác dụng phụ:**
            - **Penicillin:** Dị ứng (cần test trước)
            - **Doxycycline:** Nhạy cảm ánh sáng, đau dạ dày
            - Báo bác sĩ nếu có tác dụng phụ nặng

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Sốt cao:**
            - Sốt > 39°C, không giảm
            - Sốt kéo dài > 5 ngày

            **2. Biến chứng:**
            - Vàng da, vàng mắt
            - Xuất huyết
            - Thiểu niệu, vô niệu (suy thận)
            - Rối loạn ý thức (viêm màng não)

            **3. Mất nước:**
            - Không uống được
            - Mệt mỏi nặng

            ## 💡 PHÒNG NGỪA:

            **1. Tránh tiếp xúc:**
            - Tránh tiếp xúc nước, đất bẩn
            - Mang ủng, găng tay khi làm ruộng
            - Tránh bơi lội ở ao, hồ, sông (đặc biệt mùa mưa)

            **2. Vệ sinh:**
            - Rửa tay sau khi tiếp xúc đất, nước
            - Rửa sạch vết thương
            - Vệ sinh môi trường

            **3. Diệt chuột:**
            - Diệt chuột (nguồn lây chính)
            - Vệ sinh chuồng trại
            - Bảo quản thức ăn

            **4. Dự phòng:**
            - **Doxycycline:** 200mg/tuần (cho người có nguy cơ cao)
            - Tiêm vắc xin cho động vật

            **5. Mùa mưa lũ:**
            - Đặc biệt chú ý
            - Tránh tiếp xúc nước lũ
            - Mang ủng, găng tay

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Phòng ngừa:**
            - **Tránh tiếp xúc nước, đất bẩn** (quan trọng nhất!)
            - Mang ủng, găng tay khi làm ruộng
            - Diệt chuột
            - Tránh bơi lội ở ao, hồ, sông

            **2. Khi bị sốt vàng da xuất huyết:**
            - Điều trị sớm (quan trọng!)
            - Uống kháng sinh đủ liệu trình
            - Nghỉ ngơi, uống nhiều nước
            - Theo dõi biến chứng

            **3. Sống tích cực:**
            - Phòng ngừa tốt → Không mắc bệnh
            - Điều trị sớm → Giảm biến chứng, tử vong
            - Uống đủ kháng sinh → Khỏi hoàn toàn

            **4. Vùng nông thôn, mùa mưa:**
            - Đặc biệt chú ý phòng ngừa
            - Tránh tiếp xúc nước, đất bẩn
            - Mang ủng, găng tay
            - Diệt chuột
            """,
            related_disease="leptospirosis",
            related_drugs=["Penicillin G", "Doxycycline", "Ceftriaxone", "Azithromycin", "Paracetamol"],
            printable=True
        ),

        PatientEducationTopic(
            id="chickenpox_basics",
            title="Understanding Chickenpox",
            title_vn="Hiểu về Thủy đậu",
            category="Disease",
            content="""
            # Hiểu về Thủy đậu

            ## Thủy đậu là gì?

            Thủy đậu là bệnh nhiễm virus do Varicella-zoster virus (VZV) gây ra, đặc trưng bởi sốt và phát ban mụn nước toàn thân. Bệnh rất phổ biến ở trẻ em Việt Nam, lây qua đường hô hấp và tiếp xúc trực tiếp.

            **⚠️ Đặc điểm:**
            - Bệnh nhiễm virus
            - Sốt, phát ban mụn nước
            - Rất phổ biến ở trẻ em
            - Lây qua đường hô hấp

            ## Triệu chứng:

            **Triệu chứng điển hình:**
            - **Sốt:** Sốt nhẹ đến vừa (37.5-39°C)
            - **Phát ban:** Ban đỏ, sau đó thành mụn nước
            - **Mụn nước:** Mụn nước trong, sau đó đục, vỡ, đóng vảy
            - **Ngứa:** Ngứa nhiều
            - **Mệt mỏi, chán ăn**

            **Đặc điểm phát ban:**
            - **Giai đoạn 1:** Ban đỏ (1-2 ngày)
            - **Giai đoạn 2:** Mụn nước trong (2-3 ngày)
            - **Giai đoạn 3:** Mụn nước đục, vỡ (3-4 ngày)
            - **Giai đoạn 4:** Đóng vảy (5-7 ngày)
            - **Nhiều đợt:** Có thể có nhiều đợt phát ban (2-4 ngày)
            - **Toàn thân:** Mặt, thân, tay chân, cả niêm mạc

            **⚠️ Biến chứng:**
            - Nhiễm khuẩn da (do gãi)
            - Viêm phổi (người lớn)
            - Viêm não
            - Nhiễm khuẩn huyết
            - Để lại sẹo

            **⚠️ Người lớn:**
            - Bệnh nặng hơn trẻ em
            - Nguy cơ biến chứng cao hơn

            ## Nguyên nhân:

            **1. Virus:**
            - Varicella-zoster virus (VZV)
            - Cùng họ với virus gây zona

            **2. Lây truyền:**
            - **Đường hô hấp:** Ho, hắt hơi, nói chuyện
            - **Tiếp xúc trực tiếp:** Dịch mụn nước
            - **Gián tiếp:** Đồ vật bị nhiễm

            **3. Yếu tố nguy cơ:**
            - Chưa tiêm vắc xin
            - Chưa từng mắc bệnh
            - Tiếp xúc với người bệnh
            - Suy giảm miễn dịch

            ## Chẩn đoán:

            **Chẩn đoán lâm sàng:**
            - Triệu chứng điển hình
            - Phát ban đặc trưng

            **Xét nghiệm:**
            - **PCR:** Phát hiện DNA virus
            - **Kháng thể:** IgM, IgG
            - **Cấy virus:** Ít dùng

            ## Điều trị:

            **1. Điều trị triệu chứng:**
            - **Hạ sốt:** Paracetamol (không dùng Aspirin ở trẻ em!)
            - **Giảm ngứa:** Antihistamine, Calamine lotion
            - **Chăm sóc da:** Tắm nước ấm, giữ da sạch

            **2. Thuốc kháng virus:**
            - **Acyclovir:** 20mg/kg x 4 lần/ngày, 5 ngày (nếu trong 24 giờ đầu)
            - Dùng cho người lớn, trẻ em có nguy cơ biến chứng
            - Giảm mức độ bệnh, biến chứng

            **3. Điều trị nhiễm khuẩn:**
            - Kháng sinh bôi hoặc uống nếu nhiễm khuẩn da

            **4. Nghỉ ngơi:**
            - Nghỉ ngơi tại nhà
            - Cách ly cho đến khi khỏi

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Khi đang sốt:**
            - Ăn mềm, lỏng: Cháo, súp
            - Uống nhiều nước: Nước lọc, nước trái cây
            - Tránh thức ăn cay nóng (có thể làm ngứa tăng)

            **2. Sau khi hết sốt:**
            - Ăn đủ dinh dưỡng
            - Protein: Thịt, cá, trứng
            - Rau xanh, trái cây
            - Tránh thức ăn gây dị ứng (nếu có)

            **3. Thực đơn mẫu:**
            - **Sáng:** Cháo, trứng
            - **Trưa:** Cơm, thịt/cá, rau xanh, canh
            - **Chiều:** Cơm, thịt/cá, rau xanh, canh
            - **Bữa phụ:** Trái cây, sữa

            ## 🏃 TẬP THỂ DỤC:

            **1. Khi đang bệnh:**
            - Nghỉ ngơi tại nhà
            - Tránh gắng sức
            - Cách ly cho đến khi khỏi

            **2. Sau khi khỏi:**
            - Tập thể dục bình thường
            - Tăng dần cường độ

            ## 💊 QUẢN LÝ THUỐC:

            **1. Hạ sốt:**
            - **Paracetamol:** Khi sốt > 38.5°C
            - **Không dùng Aspirin** ở trẻ em (gây hội chứng Reye)
            - Không quá 4g/ngày (người lớn)

            **2. Giảm ngứa:**
            - **Antihistamine:** Cetirizine, Loratadine
            - **Calamine lotion:** Bôi lên mụn nước
            - Tránh gãi (gây nhiễm khuẩn, sẹo)

            **3. Kháng virus:**
            - Acyclovir: Nếu có chỉ định
            - Uống đủ liệu trình

            **4. Lưu ý:**
            - Không tự ý dùng Corticosteroid (làm bệnh nặng)
            - Báo bác sĩ nếu có tác dụng phụ

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Biến chứng:**
            - Sốt cao, kéo dài
            - Khó thở (viêm phổi)
            - Rối loạn ý thức (viêm não)
            - Nhiễm khuẩn da nặng

            **2. Người có nguy cơ:**
            - Trẻ sơ sinh
            - Người lớn
            - Phụ nữ mang thai
            - Suy giảm miễn dịch

            **3. Triệu chứng nặng:**
            - Sốt > 40°C
            - Mụn nước nhiều, lan rộng
            - Mệt mỏi nặng

            ## 💡 PHÒNG NGỪA:

            **1. Tiêm vắc xin (QUAN TRỌNG NHẤT!):**
            - **Vắc xin Varicella:** 2 mũi (12-15 tháng, 4-6 tuổi)
            - **Hiệu quả:** > 90%
            - **Bảo vệ:** Lâu dài
            - **Đối tượng:** Trẻ em, người chưa mắc bệnh

            **2. Cách ly:**
            - Cách ly người bệnh cho đến khi khỏi
            - Tránh tiếp xúc với người chưa mắc bệnh
            - Trẻ em không đi học cho đến khi khỏi

            **3. Vệ sinh:**
            - Rửa tay thường xuyên
            - Vệ sinh đồ vật
            - Che miệng khi ho, hắt hơi

            **4. Phụ nữ mang thai:**
            - Tránh tiếp xúc với người bệnh
            - Tiêm vắc xin trước khi mang thai (nếu chưa mắc)

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Phòng ngừa:**
            - **Tiêm vắc xin** (quan trọng nhất!)
            - Cách ly người bệnh
            - Vệ sinh cá nhân

            **2. Khi bị thủy đậu:**
            - Nghỉ ngơi tại nhà
            - Hạ sốt, giảm ngứa
            - Tránh gãi (gây nhiễm khuẩn, sẹo)
            - Tắm nước ấm, giữ da sạch

            **3. Sống tích cực:**
            - Thủy đậu thường tự khỏi
            - Điều trị triệu chứng → Giảm khó chịu
            - Phòng ngừa tốt → Không mắc bệnh
            - Tiêm vắc xin → Bảo vệ > 90%

            **4. Trẻ em:**
            - Thường nhẹ hơn người lớn
            - Cần chăm sóc, theo dõi
            - Tránh gãi (quan trọng!)
            - Không đi học cho đến khi khỏi
            """,
            related_disease="chickenpox",
            related_drugs=["Paracetamol", "Acyclovir", "Cetirizine", "Loratadine", "Calamine"],
            printable=True
        ),

        PatientEducationTopic(
            id="measles_basics",
            title="Understanding Measles",
            title_vn="Hiểu về Sởi",
            category="Disease",
            content="""
            # Hiểu về Sởi

            ## Sởi là gì?

            Sởi là bệnh nhiễm virus do Measles virus gây ra, đặc trưng bởi sốt, ho, sổ mũi, đỏ mắt và phát ban. Bệnh rất phổ biến ở trẻ em Việt Nam, lây qua đường hô hấp, có thể gây biến chứng nặng.

            **⚠️ Đặc điểm:**
            - Bệnh nhiễm virus
            - Sốt, ho, sổ mũi, phát ban
            - Rất phổ biến ở trẻ em
            - Có thể gây biến chứng nặng

            ## Triệu chứng:

            **Giai đoạn 1 (ủ bệnh):** 10-14 ngày
            - Không có triệu chứng

            **Giai đoạn 2 (tiền triệu):** 2-4 ngày
            - **Sốt:** Sốt cao (38-40°C)
            - **Ho:** Ho khan
            - **Sổ mũi:** Chảy nước mũi
            - **Đỏ mắt:** Viêm kết mạc, sợ ánh sáng
            - **Đốm Koplik:** Đốm trắng nhỏ trong miệng (dấu hiệu đặc trưng)

            **Giai đoạn 3 (phát ban):** 3-5 ngày
            - **Phát ban:** Ban đỏ, bắt đầu từ sau tai, lan ra mặt, thân, tay chân
            - **Ban dạng dát sẩn:** Ban đỏ, nổi gờ, có thể hợp lại
            - **Sốt cao:** Sốt cao khi phát ban
            - **Mệt mỏi nặng**

            **Giai đoạn 4 (hồi phục):** 1-2 tuần
            - Ban nhạt dần, bong vảy
            - Sốt giảm
            - Ho có thể kéo dài

            **⚠️ Biến chứng:**
            - **Viêm phổi:** Nguy hiểm nhất, có thể tử vong
            - **Viêm não:** Hiếm nhưng nguy hiểm
            - **Viêm tai giữa:** Phổ biến
            - **Tiêu chảy:** Phổ biến
            - **Suy dinh dưỡng:** Do kém ăn
            - **Mù:** Do thiếu vitamin A

            ## Nguyên nhân:

            **1. Virus:**
            - Measles virus
            - Rất dễ lây

            **2. Lây truyền:**
            - **Đường hô hấp:** Ho, hắt hơi, nói chuyện
            - **Tiếp xúc trực tiếp:** Dịch mũi, họng
            - **Gián tiếp:** Đồ vật bị nhiễm (ít gặp)

            **3. Yếu tố nguy cơ:**
            - Chưa tiêm vắc xin
            - Chưa từng mắc bệnh
            - Tiếp xúc với người bệnh
            - Suy dinh dưỡng
            - Thiếu vitamin A
            - Suy giảm miễn dịch

            ## Chẩn đoán:

            **Chẩn đoán lâm sàng:**
            - Triệu chứng điển hình
            - Đốm Koplik
            - Phát ban đặc trưng

            **Xét nghiệm:**
            - **Kháng thể IgM:** Dương tính
            - **PCR:** Phát hiện RNA virus
            - **Cấy virus:** Ít dùng

            ## Điều trị:

            **1. Điều trị triệu chứng:**
            - **Hạ sốt:** Paracetamol (không dùng Aspirin ở trẻ em!)
            - **Giảm ho:** Thuốc ho, mật ong
            - **Nhỏ mũi:** Nước muối sinh lý
            - **Nhỏ mắt:** Nước muối sinh lý

            **2. Bổ sung vitamin A:**
            - **Vitamin A:** 200,000 IU (trẻ > 12 tháng), 100,000 IU (trẻ 6-12 tháng), 50,000 IU (trẻ < 6 tháng)
            - Uống 2 lần (cách 24 giờ)
            - Giảm nguy cơ mù, tử vong

            **3. Điều trị biến chứng:**
            - **Viêm phổi:** Kháng sinh
            - **Viêm tai giữa:** Kháng sinh
            - **Tiêu chảy:** Bù dịch, Oresol

            **4. Nghỉ ngơi:**
            - Nghỉ ngơi tại nhà
            - Cách ly cho đến khi khỏi

            **5. Dinh dưỡng:**
            - Ăn đủ dinh dưỡng
            - Uống nhiều nước
            - Bổ sung vitamin, khoáng chất

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Khi đang sốt:**
            - Ăn mềm, lỏng: Cháo, súp
            - Uống nhiều nước: Nước lọc, nước trái cây
            - Tránh thức ăn khó tiêu

            **2. Sau khi hết sốt:**
            - Ăn đủ dinh dưỡng
            - Protein: Thịt, cá, trứng
            - Rau xanh, trái cây (bổ sung vitamin A)
            - Sữa, sữa chua

            **3. Thực đơn mẫu:**
            - **Sáng:** Cháo thịt, trứng
            - **Trưa:** Cơm, thịt/cá, rau xanh, canh
            - **Chiều:** Cơm, thịt/cá, rau xanh, canh
            - **Bữa phụ:** Trái cây, sữa

            **4. Lưu ý:**
            - Bổ sung vitamin A (quan trọng!)
            - Ăn đủ dinh dưỡng (tránh suy dinh dưỡng)

            ## 🏃 TẬP THỂ DỤC:

            **1. Khi đang bệnh:**
            - Nghỉ ngơi tại nhà
            - Tránh gắng sức
            - Cách ly cho đến khi khỏi

            **2. Sau khi khỏi:**
            - Tập thể dục từ từ
            - Tăng dần cường độ

            ## 💊 QUẢN LÝ THUỐC:

            **1. Hạ sốt:**
            - **Paracetamol:** Khi sốt > 38.5°C
            - **Không dùng Aspirin** ở trẻ em (gây hội chứng Reye)
            - Không quá 4g/ngày (người lớn)

            **2. Vitamin A:**
            - Uống đúng liều, đúng thời điểm
            - Quan trọng để giảm biến chứng

            **3. Điều trị biến chứng:**
            - Kháng sinh nếu có nhiễm khuẩn
            - Oresol nếu tiêu chảy

            **4. Lưu ý:**
            - Không tự ý dùng Corticosteroid
            - Báo bác sĩ nếu có biến chứng

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Biến chứng:**
            - Sốt cao, kéo dài
            - Khó thở (viêm phổi)
            - Rối loạn ý thức (viêm não)
            - Co giật
            - Mất nước nặng

            **2. Trẻ nhỏ:**
            - Trẻ < 12 tháng
            - Suy dinh dưỡng
            - Thiếu vitamin A

            **3. Triệu chứng nặng:**
            - Sốt > 40°C
            - Ho nhiều, khó thở
            - Mệt mỏi nặng
            - Không ăn uống được

            ## 💡 PHÒNG NGỪA:

            **1. Tiêm vắc xin (QUAN TRỌNG NHẤT!):**
            - **Vắc xin MMR (Sởi-Quai bị-Rubella):** 2 mũi (12-15 tháng, 4-6 tuổi)
            - **Hiệu quả:** > 95%
            - **Bảo vệ:** Lâu dài
            - **Đối tượng:** Tất cả trẻ em

            **2. Cách ly:**
            - Cách ly người bệnh cho đến khi khỏi
            - Tránh tiếp xúc với người chưa tiêm vắc xin
            - Trẻ em không đi học cho đến khi khỏi

            **3. Vệ sinh:**
            - Rửa tay thường xuyên
            - Che miệng khi ho, hắt hơi
            - Vệ sinh đồ vật

            **4. Bổ sung vitamin A:**
            - Bổ sung vitamin A định kỳ cho trẻ em
            - Đặc biệt quan trọng khi mắc sởi

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Phòng ngừa:**
            - **Tiêm vắc xin** (quan trọng nhất!)
            - Cách ly người bệnh
            - Vệ sinh cá nhân

            **2. Khi bị sởi:**
            - Nghỉ ngơi tại nhà
            - Hạ sốt, giảm ho
            - Bổ sung vitamin A (quan trọng!)
            - Ăn đủ dinh dưỡng
            - Theo dõi biến chứng

            **3. Sống tích cực:**
            - Sởi có thể gây biến chứng nặng
            - Điều trị triệu chứng, bổ sung vitamin A → Giảm biến chứng
            - Phòng ngừa tốt → Không mắc bệnh
            - Tiêm vắc xin → Bảo vệ > 95%

            **4. Trẻ em:**
            - Cần chăm sóc, theo dõi sát
            - Bổ sung vitamin A (quan trọng!)
            - Ăn đủ dinh dưỡng
            - Không đi học cho đến khi khỏi
            - Theo dõi biến chứng (viêm phổi, viêm não)
            """,
            related_disease="measles",
            related_drugs=["Paracetamol", "Vitamin A", "Oresol", "Antibiotic"],
            printable=True
        ),

        PatientEducationTopic(
            id="sepsis_basics",
            title="Understanding Sepsis",
            title_vn="Hiểu về Nhiễm khuẩn huyết",
            category="Disease",
            content="""
            # Hiểu về Nhiễm khuẩn huyết

            ## Nhiễm khuẩn huyết là gì?

            Nhiễm khuẩn huyết (Sepsis) là tình trạng đe dọa tính mạng do phản ứng của cơ thể với nhiễm khuẩn, gây tổn thương các cơ quan. Bệnh rất nguy hiểm, cần điều trị cấp cứu ngay lập tức.

            **⚠️ Đặc điểm:**
            - Tình trạng đe dọa tính mạng
            - Phản ứng của cơ thể với nhiễm khuẩn
            - Gây tổn thương các cơ quan
            - Tử vong cao nếu không điều trị sớm

            ## Triệu chứng:

            **Triệu chứng điển hình:**
            - **Sốt:** Sốt cao (> 38°C) hoặc hạ thân nhiệt (< 36°C)
            - **Nhịp tim nhanh:** > 90 lần/phút
            - **Thở nhanh:** > 20 lần/phút
            - **Rối loạn ý thức:** Lơ mơ, kích thích, hôn mê
            - **Huyết áp thấp:** Sốc nhiễm khuẩn

            **Triệu chứng khác:**
            - Da lạnh, ẩm
            - Vã mồ hôi
            - Giảm đi tiểu
            - Đau cơ, khớp
            - Buồn nôn, nôn

            **⚠️ Sốc nhiễm khuẩn:**
            - Huyết áp tụt
            - Thiểu niệu
            - Rối loạn ý thức
            - **Cấp cứu ngay!**

            ## Nguyên nhân:

            **1. Nhiễm khuẩn:**
            - Vi khuẩn (phổ biến nhất)
            - Virus, nấm (ít gặp hơn)

            **2. Nguồn nhiễm khuẩn:**
            - **Viêm phổi:** Phổ biến nhất
            - **Nhiễm khuẩn tiết niệu**
            - **Nhiễm khuẩn da, mô mềm**
            - **Nhiễm khuẩn ổ bụng**
            - **Nhiễm khuẩn huyết từ catheter**

            **3. Yếu tố nguy cơ:**
            - Tuổi cao (> 65 tuổi)
            - Trẻ sơ sinh
            - Suy giảm miễn dịch
            - Bệnh mạn tính (đái tháo đường, suy thận)
            - Phẫu thuật gần đây
            - Đặt catheter, ống thông

            ## Chẩn đoán:

            **Tiêu chuẩn chẩn đoán (SOFA score):**
            - Nhiễm khuẩn + Rối loạn chức năng cơ quan
            - **SOFA ≥ 2:** Sepsis
            - **Sốc:** Sepsis + Huyết áp thấp

            **Xét nghiệm:**
            - **Cấy máu:** Tìm vi khuẩn
            - **Cấy nước tiểu, đờm:** Tìm nguồn nhiễm
            - **Công thức máu:** Bạch cầu tăng/giảm
            - **Procalcitonin:** Tăng cao
            - **Lactate:** Tăng (thiếu oxy mô)

            ## Điều trị:

            **1. Kháng sinh (QUAN TRỌNG!):**
            - **Bắt đầu ngay:** Trong 1 giờ đầu
            - **Phổ rộng:** Ceftriaxone + Vancomycin, hoặc Piperacillin-Tazobactam
            - **Điều chỉnh:** Theo kết quả cấy và kháng sinh đồ
            - **Liệu trình:** 7-14 ngày

            **2. Bù dịch:**
            - **Truyền dịch:** 30ml/kg trong 3 giờ đầu
            - **Dịch tinh thể:** Nước muối sinh lý, Ringer lactate
            - **Theo dõi:** Đáp ứng dịch

            **3. Vận mạch:**
            - **Norepinephrine:** Nếu huyết áp thấp sau bù dịch
            - **Dopamine, Epinephrine:** Nếu cần

            **4. Điều trị hỗ trợ:**
            - **Thở máy:** Nếu suy hô hấp
            - **Lọc máu:** Nếu suy thận
            - **Hạ sốt:** Paracetamol
            - **Điều chỉnh đường huyết:** Insulin nếu cần

            **5. Điều trị nguồn nhiễm:**
            - Dẫn lưu ổ áp xe
            - Loại bỏ catheter nhiễm khuẩn
            - Phẫu thuật nếu cần

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Khi đang bệnh nặng:**
            - Nuôi ăn qua ống (nếu hôn mê)
            - Nuôi ăn tĩnh mạch (nếu không ăn được)
            - Theo chỉ định bác sĩ

            **2. Khi ổn định:**
            - Ăn đủ dinh dưỡng
            - Protein: Thịt, cá, trứng
            - Rau xanh, trái cây
            - Uống nhiều nước

            **3. Thực đơn mẫu:**
            - **Sáng:** Cháo thịt, trứng
            - **Trưa:** Cơm, thịt/cá, rau xanh, canh
            - **Chiều:** Cơm, thịt/cá, rau xanh, canh
            - **Bữa phụ:** Trái cây, sữa

            ## 🏃 TẬP THỂ DỤC:

            **1. Khi đang bệnh:**
            - Nghỉ ngơi hoàn toàn
            - Vật lý trị liệu (nếu có chỉ định)

            **2. Sau khi khỏi:**
            - Tập thể dục từ từ
            - Phục hồi chức năng
            - Tăng dần cường độ

            ## 💊 QUẢN LÝ THUỐC:

            **1. Kháng sinh:**
            - Uống đủ liệu trình (7-14 ngày)
            - Uống đúng giờ, đúng liều
            - **Quan trọng:** Không tự ý ngừng

            **2. Điều trị hỗ trợ:**
            - Paracetamol: Hạ sốt
            - Insulin: Điều chỉnh đường huyết (nếu cần)

            **3. Lưu ý:**
            - Điều trị tại bệnh viện
            - Theo dõi sát
            - Báo bác sĩ nếu có tác dụng phụ

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Triệu chứng nặng:**
            - Sốt cao + nhịp tim nhanh + thở nhanh
            - Rối loạn ý thức
            - Huyết áp thấp
            - **Cấp cứu ngay!**

            **2. Nhiễm khuẩn + triệu chứng:**
            - Nhiễm khuẩn + sốt cao
            - Nhiễm khuẩn + mệt mỏi nặng
            - Nhiễm khuẩn + rối loạn ý thức

            **3. Yếu tố nguy cơ:**
            - Tuổi cao
            - Suy giảm miễn dịch
            - Bệnh mạn tính

            ## 💡 PHÒNG NGỪA:

            **1. Phòng ngừa nhiễm khuẩn:**
            - **Rửa tay:** Rửa tay thường xuyên
            - **Vệ sinh:** Giữ vệ sinh cá nhân sạch sẽ
            - **Vết thương:** Chăm sóc vết thương đúng cách
            - **Tiêm vắc xin:** Cúm, phế cầu (nếu có chỉ định)

            **2. Điều trị nhiễm khuẩn sớm:**
            - Điều trị nhiễm khuẩn ngay khi có triệu chứng
            - Uống kháng sinh đủ liệu trình
            - Không tự ý ngừng kháng sinh

            **3. Yếu tố nguy cơ:**
            - Kiểm soát bệnh mạn tính
            - Tăng cường miễn dịch
            - Tránh tiếp xúc với người bệnh

            **4. Chăm sóc y tế:**
            - Vệ sinh catheter, ống thông
            - Phòng ngừa nhiễm khuẩn bệnh viện

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Phòng ngừa:**
            - **Rửa tay** (quan trọng nhất!)
            - Điều trị nhiễm khuẩn sớm
            - Vệ sinh cá nhân

            **2. Khi có triệu chứng:**
            - **Đến bệnh viện ngay** (quan trọng nhất!)
            - Điều trị sớm → Giảm tử vong
            - Không tự điều trị tại nhà

            **3. Sống tích cực:**
            - Nhiễm khuẩn huyết rất nguy hiểm
            - Điều trị sớm → Tỷ lệ sống cao
            - Phòng ngừa tốt → Không mắc bệnh

            **4. Sau khi khỏi:**
            - Có thể có di chứng
            - Cần phục hồi chức năng
            - Theo dõi định kỳ
            """,
            related_disease="sepsis",
            related_drugs=["Ceftriaxone", "Vancomycin", "Piperacillin-Tazobactam", "Norepinephrine", "Paracetamol"],
            printable=True
        ),

]
