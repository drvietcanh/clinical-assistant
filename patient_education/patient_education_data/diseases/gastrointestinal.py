"""
Patient Education Topics - Gastrointestinal
"""
from patient_education.models import PatientEducationTopic


GASTROINTESTINAL_TOPICS = [
        PatientEducationTopic(
            id="gerd_basics",
            title="Understanding GERD",
            title_vn="Hiểu về Trào ngược dạ dày thực quản",
            category="Disease",
            content="""
            # Hiểu về Trào ngược dạ dày thực quản (GERD)

            ## GERD là gì?

            GERD (Gastroesophageal Reflux Disease) xảy ra khi axit dạ dày trào ngược lên thực quản, gây viêm và tổn thương niêm mạc thực quản.

            **Cơ chế:**
            - Cơ vòng thực quản dưới (LES) yếu hoặc giãn không đúng lúc
            - Axit dạ dày trào lên thực quản
            - Gây viêm, tổn thương niêm mạc

            **⚠️ Phân biệt:**
            - **Trào ngược sinh lý:** Thỉnh thoảng, không có triệu chứng (bình thường)
            - **GERD:** Thường xuyên (> 2 lần/tuần), có triệu chứng, cần điều trị

            ## Triệu chứng:

            **Triệu chứng điển hình:**
            - **Ợ nóng (Heartburn):** Nóng rát ngực, lan lên cổ họng (sau ăn, khi nằm)
            - **Ợ chua:** Cảm giác axit trào lên miệng
            - **Đau ngực:** Đau sau xương ức, có thể nhầm với đau tim
            - **Khó nuốt:** Cảm giác thức ăn mắc ở cổ
            - **Nuốt đau:** Đau khi nuốt

            **Triệu chứng không điển hình:**
            - **Ho mạn tính:** Đặc biệt ban đêm, khi nằm
            - **Khàn giọng:** Do axit kích thích thanh quản
            - **Đau họng:** Viêm họng do axit
            - **Cảm giác vướng cổ:** Cảm giác có gì đó ở cổ
            - **Hen phế quản:** GERD có thể làm hen nặng hơn
            - **Đau răng:** Axit làm mòn men răng

            **⚠️ Lưu ý:** Đau ngực do GERD có thể giống đau tim. Nếu đau ngực dữ dội, lan ra tay, kèm khó thở → Cần loại trừ đau tim trước!

            ## Nguyên nhân:

            **1. Yếu tố cơ học:**
            - **Thoát vị hoành:** Dạ dày trượt lên ngực qua cơ hoành
            - **Cơ vòng thực quản yếu:** Do tuổi, bệnh lý
            - **Tăng áp lực ổ bụng:** Béo phì, mang thai, ho mạn tính

            **2. Yếu tố lối sống:**
            - **Ăn quá no:** Làm tăng áp lực dạ dày
            - **Nằm sau ăn:** Trọng lực không giúp giữ axit
            - **Thức ăn kích thích:** Đồ cay, chua, béo, cà phê, rượu
            - **Hút thuốc:** Làm yếu cơ vòng thực quản
            - **Stress:** Làm tăng tiết axit

            **3. Thuốc:**
            - Một số thuốc làm yếu cơ vòng: Theophylline, một số thuốc huyết áp
            - NSAID: Làm tổn thương niêm mạc dạ dày

            **4. Bệnh khác:**
            - Béo phì
            - Mang thai
            - Đái tháo đường (gây liệt dạ dày)
            - Xơ cứng bì

            ## Điều trị:

            **1. Thay đổi lối sống (QUAN TRỌNG NHẤT!):**
            - Chế độ ăn phù hợp
            - Thay đổi thói quen sinh hoạt
            - Xem chi tiết bên dưới

            **2. Thuốc:**
            - **PPI (Proton Pump Inhibitors):** Omeprazole, Pantoprazole, Esomeprazole
              - Uống trước ăn 30 phút
              - Uống lâu dài nếu cần
            - **H2 Blockers:** Ranitidine, Famotidine
            - **Antacid:** Trung hòa axit tạm thời (không dùng lâu dài)

            **3. Phẫu thuật:**
            - Hiếm, chỉ khi thuốc không hiệu quả
            - Thắt cơ vòng thực quản

            ## 🍽️ CHẾ ĐỘ ĂN CHO NGƯỜI GERD:

            **1. Nguyên tắc:**
            - **Ăn nhiều bữa nhỏ:** 5-6 bữa/ngày (thay vì 3 bữa lớn)
            - **Không ăn quá no:** Ăn vừa đủ, dừng khi no 70-80%
            - **Ăn chậm, nhai kỹ:** Giúp tiêu hóa tốt hơn
            - **Tránh thức ăn kích thích:** Xem danh sách bên dưới

            **2. Thực phẩm NÊN ĂN:**
            - **Rau xanh:** Rau cải, rau muống, bông cải, cà rốt (luộc, hấp)
            - **Trái cây ít axit:** Chuối, táo, lê, dưa hấu
            - **Protein nạc:** Thịt gà (bỏ da), cá, đậu phụ (luộc, hấp, nướng)
            - **Ngũ cốc:** Gạo, bánh mì, yến mạch
            - **Sữa ít béo:** Sữa tách béo, sữa chua (không quá chua)
            - **Chất béo tốt:** Dầu ô liu, quả bơ (ít)

            **3. Thực phẩm CẦN TRÁNH:**
            - **Đồ cay:** Ớt, tiêu, gừng (nhiều), tỏi (một số người)
            - **Đồ chua:** Chanh, cam, bưởi, dứa, cà chua (nhiều)
            - **Đồ béo:** Đồ chiên rán, thịt mỡ, bơ, phô mai béo
            - **Cà phê, trà:** Làm yếu cơ vòng thực quản, tăng axit
            - **Rượu bia:** Làm tăng trào ngược
            - **Đồ uống có ga:** Gây đầy bụng, tăng áp lực
            - **Sô cô la:** Làm yếu cơ vòng thực quản
            - **Bạc hà:** Làm giãn cơ vòng thực quản
            - **Hành, tỏi:** Một số người nhạy cảm

            **4. Cách chế biến:**
            - **Nên:** Luộc, hấp, nướng, xào ít dầu
            - **Tránh:** Chiên rán, nướng nhiều dầu mỡ

            **5. Thực đơn mẫu (1 ngày):**
            - **Sáng:** Cháo yến mạch + chuối + sữa ít béo
            - **Bữa phụ (10h):** Táo, bánh quy giòn
            - **Trưa:** 1 chén cơm + cá luộc + rau luộc + canh rau
            - **Bữa phụ (15h):** Sữa chua, bánh mì
            - **Tối:** 1 chén cơm + thịt gà luộc + rau xào (ít dầu) + canh
            - **Bữa phụ (21h - nếu cần):** Sữa ấm

            **6. Lưu ý:**
            - Ghi nhật ký ăn uống: Ghi thức ăn và triệu chứng
            - Xác định thức ăn gây triệu chứng (mỗi người khác nhau)
            - Tránh thức ăn đó

            ## 💤 THAY ĐỔI THÓI QUEN SINH HOẠT:

            **1. Sau khi ăn:**
            - **Không nằm ngay:** Chờ ít nhất 2-3 giờ sau ăn
            - **Ngồi thẳng:** Hoặc đi bộ nhẹ nhàng
            - **Tránh cúi gập:** Không cúi, gập người sau ăn

            **2. Khi ngủ:**
            - **Kê đầu cao:** Kê gối cao 15-20cm, hoặc nâng đầu giường
            - **Nằm nghiêng trái:** Giúp giảm trào ngược (dạ dày ở bên trái)
            - **Tránh nằm ngửa:** Dễ trào ngược hơn

            **3. Quần áo:**
            - **Mặc rộng rãi:** Tránh quần áo chật, thắt lưng chặt
            - **Giảm áp lực ổ bụng**

            **4. Thời gian ăn:**
            - **Bữa tối:** Ăn trước 7 giờ tối (ít nhất 3 giờ trước khi ngủ)
            - **Bữa sáng:** Ăn đúng giờ, không bỏ bữa
            - **Bữa trưa:** Ăn vừa đủ, không quá no

            **5. Uống nước:**
            - Uống giữa các bữa ăn (không uống nhiều trong bữa ăn)
            - Uống nước ấm (tốt hơn nước lạnh)
            - Tránh đồ uống có ga

            **6. Giảm cân (nếu thừa cân):**
            - Béo phì làm tăng áp lực ổ bụng
            - Giảm 5-10% cân nặng → Giảm triệu chứng đáng kể

            **7. Bỏ thuốc lá:**
            - Hút thuốc làm yếu cơ vòng thực quản
            - Tăng tiết axit
            - Bỏ thuốc → Giảm triệu chứng

            **8. Quản lý stress:**
            - Stress làm tăng tiết axit, tăng trào ngược
            - Tập thư giãn: Hít thở sâu, thiền, yoga
            - Ngủ đủ giấc

            ## 💊 QUẢN LÝ THUỐC:

            **1. PPI (Proton Pump Inhibitors):**
            - **Khi nào dùng:** Khi thay đổi lối sống không đủ
            - **Cách dùng:** Uống trước ăn 30 phút (quan trọng!)
            - **Thời gian:** Thường 4-8 tuần, có thể lâu hơn
            - **Không tự ý ngừng:** Ngừng đột ngột → Trào ngược nặng hơn

            **2. H2 Blockers:**
            - Dùng trước khi ngủ (nếu triệu chứng về đêm)
            - Hoặc khi cần giảm axit nhanh

            **3. Antacid:**
            - Dùng khi có triệu chứng (không dùng lâu dài)
            - Trung hòa axit tạm thời

            **4. Tác dụng phụ:**
            - **PPI:** Tiêu chảy, đau đầu, thiếu B12 (nếu dùng lâu)
            - **Báo bác sĩ nếu:** Tác dụng phụ nghiêm trọng

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Triệu chứng báo động:**
            - **Khó nuốt:** Cảm giác thức ăn mắc ở cổ, nuốt đau
            - **Nuốt đau:** Đau khi nuốt
            - **Nôn ra máu:** Máu đỏ hoặc nâu
            - **Phân đen:** Có thể chảy máu dạ dày
            - **Sụt cân:** Không rõ nguyên nhân
            - **Thiếu máu:** Mệt mỏi, da xanh

            **2. Triệu chứng nặng:**
            - Đau ngực dữ dội (cần loại trừ đau tim!)
            - Nôn nhiều
            - Không ăn được

            **3. Không đáp ứng điều trị:**
            - Thay đổi lối sống + thuốc không hiệu quả
            - Triệu chứng không giảm sau 4-8 tuần

            **⚠️ Lưu ý:** Các triệu chứng báo động có thể là dấu hiệu của bệnh nặng hơn (ung thư thực quản, loét dạ dày). Cần nội soi để chẩn đoán!

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Thay đổi lối sống trước:**
            - Thử thay đổi lối sống 2-4 tuần trước khi dùng thuốc
            - Nhiều người cải thiện chỉ bằng thay đổi lối sống

            **2. Nhận biết thức ăn kích thích:**
            - Ghi nhật ký: Thức ăn + triệu chứng
            - Mỗi người khác nhau
            - Tránh thức ăn gây triệu chứng

            **3. Khi đi ăn ngoài:**
            - Chọn món luộc, hấp
            - Tránh đồ chiên, cay, chua
            - Ăn vừa đủ, không quá no
            - Không nằm ngay sau ăn

            **4. Khi mang thai:**
            - GERD thường gặp khi mang thai (do hormone, tăng áp lực)
            - Thay đổi lối sống trước
            - Dùng thuốc an toàn (hỏi bác sĩ)
            - Thường tự khỏi sau sinh

            **5. Ở trẻ em:**
            - GERD thường gặp ở trẻ sơ sinh
            - Thường tự khỏi khi lớn
            - Nếu nặng: Cần điều trị

            **6. Phòng ngừa:**
            - Duy trì cân nặng hợp lý
            - Ăn đúng giờ, không bỏ bữa
            - Tránh thức ăn kích thích
            - Không nằm sau ăn
            - Bỏ thuốc lá
            - Quản lý stress

            **7. Sống tích cực:**
            - GERD có thể kiểm soát được
            - Thay đổi lối sống + thuốc → Sống bình thường
            - Đừng để GERD ảnh hưởng cuộc sống
            """,
            related_disease="gerd",
            related_drugs=["Omeprazole", "Pantoprazole", "Ranitidine"],
            printable=True
        ),

        PatientEducationTopic(
            id="peptic_ulcer_basics",
            title="Understanding Peptic Ulcer Disease",
            title_vn="Hiểu về Viêm loét dạ dày tá tràng",
            category="Disease",
            content="""
            # Hiểu về Viêm loét dạ dày tá tràng

            ## Viêm loét dạ dày tá tràng là gì?

            Viêm loét dạ dày tá tràng là tình trạng có vết loét ở niêm mạc dạ dày hoặc tá tràng (phần đầu ruột non), do axit dạ dày và pepsin làm tổn thương.

            **Vị trí:**
            - **Loét dạ dày:** Vết loét ở dạ dày
            - **Loét tá tràng:** Vết loét ở tá tràng (phổ biến hơn, 80%)

            **⚠️ Đặc điểm:**
            - Có thể gây đau, chảy máu, thủng
            - Có thể chữa khỏi hoàn toàn
            - Dễ tái phát nếu không điều trị đúng

            ## Triệu chứng:

            **Triệu chứng điển hình:**
            - **Đau bụng vùng thượng vị:**
              - Đau rát, cồn cào
              - Đau khi đói, giảm khi ăn (loét tá tràng)
              - Đau tăng khi ăn (loét dạ dày)
              - Đau về đêm
            - **Ợ hơi, ợ chua**
            - **Buồn nôn, nôn**
            - **Đầy bụng, khó tiêu**
            - **Chán ăn**

            **Triệu chứng biến chứng:**
            - **Chảy máu:** Nôn ra máu, đi ngoài phân đen
            - **Thủng:** Đau bụng dữ dội, đột ngột
            - **Hẹp môn vị:** Nôn nhiều, không ăn được

            **⚠️ Lưu ý:** Nhiều người không có triệu chứng rõ ràng!

            ## Nguyên nhân:

            **1. Nhiễm H. pylori (80%):**
            - Vi khuẩn Helicobacter pylori
            - Làm tổn thương niêm mạc dạ dày
            - Lây qua đường miệng-miệng, phân-miệng

            **2. Thuốc NSAID:**
            - Aspirin, Ibuprofen, Diclofenac
            - Làm tổn thương niêm mạc dạ dày
            - Dùng lâu dài → Tăng nguy cơ

            **3. Yếu tố khác:**
            - **Stress:** Làm tăng tiết axit
            - **Hút thuốc lá:** Làm chậm lành vết loét
            - **Rượu bia:** Kích thích dạ dày
            - **Thức ăn cay, chua:** Kích thích (không phải nguyên nhân chính)

            ## Chẩn đoán:

            **1. Nội soi dạ dày:**
            - Xem trực tiếp vết loét
            - Sinh thiết (tìm H. pylori, loại trừ ung thư)
            - Chính xác nhất

            **2. Xét nghiệm H. pylori:**
            - Test thở (Urea breath test)
            - Xét nghiệm phân
            - Xét nghiệm máu (kháng thể)

            **3. Xét nghiệm khác:**
            - Công thức máu (nếu chảy máu)
            - Test phân tìm máu ẩn

            ## Điều trị:

            **1. Điều trị H. pylori (nếu có):**
            - **Phác đồ 3 thuốc (14 ngày):**
              - PPI (Omeprazole, Pantoprazole)
              - 2 kháng sinh (Amoxicillin + Clarithromycin hoặc Metronidazole)
            - **⚠️ QUAN TRỌNG:** Uống đủ ngày, đúng giờ
            - Tỷ lệ thành công: 80-90%

            **2. Thuốc giảm axit:**
            - **PPI:** Omeprazole, Pantoprazole, Esomeprazole
              - Uống trước ăn 30 phút
              - Uống 4-8 tuần
            - **H2 Blockers:** Ranitidine, Famotidine

            **3. Thuốc bảo vệ niêm mạc:**
            - Sucralfate
            - Bismuth

            **4. ⚠️ QUAN TRỌNG:**
            - Uống thuốc đúng giờ, đủ ngày
            - Không tự ý ngừng
            - Tái khám sau điều trị

            ## 🍽️ CHẾ ĐỘ ĂN CHO NGƯỜI VIÊM LOÉT DẠ DÀY:

            **1. Nguyên tắc:**
            - **Ăn đúng giờ:** Không bỏ bữa
            - **Ăn nhiều bữa nhỏ:** 5-6 bữa/ngày
            - **Ăn chậm, nhai kỹ:** Giúp tiêu hóa tốt
            - **Tránh thức ăn kích thích:** Đồ cay, chua, nóng, lạnh

            **2. Thực phẩm NÊN ĂN:**
            - **Cháo, súp:** Dễ tiêu, ấm
              - Cháo gà, cháo thịt bằm
              - Súp rau củ
            - **Thức ăn mềm:** Luộc, hấp
            - **Rau xanh:** Luộc, hấp (rau cải, rau muống)
            - **Trái cây:** Chuối, táo (không quá chua)
            - **Sữa:** Sữa ấm, sữa chua (ít chua)
            - **Thịt nạc:** Thịt gà, cá (luộc, hấp)

            **3. Thực phẩm CẦN TRÁNH:**
            - **Đồ cay:** Ớt, tiêu, gừng (nhiều)
            - **Đồ chua:** Chanh, dấm, cam chua
            - **Đồ nóng, lạnh:** Nước đá, đồ quá nóng
            - **Đồ chiên, nhiều dầu mỡ:** Khó tiêu
            - **Rượu bia:** Kích thích dạ dày
            - **Cà phê, trà đặc:** Tăng tiết axit
            - **Đồ chế biến sẵn:** Đồ hộp, thức ăn nhanh

            **4. Thực đơn mẫu (1 ngày):**
            - **Sáng:** Cháo gà + sữa ấm
            - **Bữa phụ (10h):** Bánh mì mềm, sữa chua
            - **Trưa:** 1 chén cơm mềm + cá hấp + rau luộc + canh rau
            - **Bữa phụ (15h):** Chuối, bánh quy
            - **Tối:** 1 chén cơm mềm + thịt gà luộc + rau luộc + canh
            - **Bữa phụ (21h):** Sữa ấm

            **5. Lưu ý:**
            - Ăn chậm, nhai kỹ
            - Không ăn quá no
            - Không nằm ngay sau ăn (chờ 2-3 giờ)
            - Uống nước ấm, không uống lạnh

            ## 💊 QUẢN LÝ THUỐC:

            **1. Thuốc điều trị H. pylori:**
            - **Uống đủ 14 ngày:** Quan trọng!
            - **Uống đúng giờ:** 2 lần/ngày
            - **Không tự ý ngừng:** Ngừng → Không diệt được vi khuẩn

            **2. Thuốc PPI:**
            - **Uống trước ăn 30 phút:** Quan trọng!
            - **Uống đủ 4-8 tuần:** Để vết loét lành
            - **Không tự ý ngừng:** Ngừng sớm → Tái phát

            **3. Tránh NSAID:**
            - **Không dùng:** Aspirin, Ibuprofen, Diclofenac
            - **Nếu cần giảm đau:** Dùng Paracetamol
            - **Nếu bắt buộc dùng NSAID:** Dùng kèm PPI

            **4. Tác dụng phụ:**
            - **PPI:** Tiêu chảy, đau đầu (thường nhẹ)
            - **Kháng sinh:** Buồn nôn, tiêu chảy
            - **Báo bác sĩ nếu:** Tác dụng phụ nghiêm trọng

            ## 🛡️ PHÒNG NGỪA:

            **1. Điều trị H. pylori:**
            - Nếu có H. pylori → Điều trị triệt để
            - Giảm nguy cơ tái phát

            **2. Tránh NSAID:**
            - Không tự ý dùng lâu dài
            - Nếu cần → Dùng kèm PPI

            **3. Lối sống:**
            - **Bỏ thuốc lá:** Làm chậm lành vết loét
            - **Hạn chế rượu bia:** Kích thích dạ dày
            - **Quản lý stress:** Tập thư giãn, yoga
            - **Ăn đúng giờ:** Không bỏ bữa

            **4. Chế độ ăn:**
            - Tránh thức ăn kích thích
            - Ăn nhiều bữa nhỏ
            - Ăn chậm, nhai kỹ

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Chảy máu:**
            - Nôn ra máu (đỏ hoặc nâu)
            - Đi ngoài phân đen
            - Mệt mỏi, da xanh (thiếu máu)

            **2. Thủng:**
            - Đau bụng dữ dội, đột ngột
            - Bụng cứng như gỗ
            - **→ Cấp cứu ngay!**

            **3. Hẹp môn vị:**
            - Nôn nhiều, không ăn được
            - Sụt cân

            **4. Không cải thiện:**
            - Điều trị 4-8 tuần không đỡ
            - Triệu chứng nặng hơn

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Khi bị viêm loét:**
            - Tuân thủ điều trị
            - Uống thuốc đúng giờ, đủ ngày
            - Chế độ ăn phù hợp
            - Tái khám sau điều trị

            **2. Phòng ngừa tái phát:**
            - Điều trị H. pylori triệt để
            - Tránh NSAID
            - Bỏ thuốc lá, hạn chế rượu bia
            - Ăn đúng giờ, không bỏ bữa

            **3. Sống tích cực:**
            - Viêm loét có thể chữa khỏi
            - Tuân thủ điều trị → Khỏi bệnh
            - Đừng lo lắng quá mức
            """,
            related_disease="peptic_ulcer",
            related_drugs=["Omeprazole", "Amoxicillin", "Clarithromycin"],
            printable=True
        ),

        PatientEducationTopic(
            id="gastritis_basics",
            title="Understanding Gastritis",
            title_vn="Hiểu về Viêm dạ dày",
            category="Disease",
            content="""
            # Hiểu về Viêm dạ dày

            ## Viêm dạ dày là gì?

            Viêm dạ dày là tình trạng viêm niêm mạc dạ dày, có thể cấp tính (ngắn hạn) hoặc mạn tính (dài hạn).

            **⚠️ Đặc điểm:**
            - Có thể do nhiều nguyên nhân
            - Có thể chữa khỏi nếu điều trị đúng
            - Dễ tái phát nếu không thay đổi lối sống

            **Phân loại:**
            - **Viêm dạ dày cấp:** Khởi phát đột ngột, ngắn hạn
            - **Viêm dạ dày mạn:** Kéo dài, có thể tiến triển

            ## Triệu chứng:

            **Triệu chứng điển hình:**
            - **Đau bụng vùng thượng vị:**
              - Đau rát, cồn cào
              - Đau tăng khi đói
              - Đau giảm khi ăn
            - **Buồn nôn, nôn:** Có thể có
            - **Đầy bụng, khó tiêu:** Sau ăn
            - **Ợ hơi, ợ chua:** Có thể có
            - **Chán ăn:** Có thể có

            **Triệu chứng khác:**
            - Cảm giác no sớm
            - Đắng miệng
            - Hơi thở hôi

            **⚠️ Lưu ý:** Nhiều người không có triệu chứng rõ ràng!

            ## Nguyên nhân:

            **1. Nhiễm H. pylori:**
            - Vi khuẩn Helicobacter pylori
            - Nguyên nhân phổ biến nhất
            - Lây qua đường miệng-miệng, phân-miệng

            **2. Thuốc:**
            - **NSAID:** Aspirin, Ibuprofen, Diclofenac
            - **Corticosteroid:** Khi dùng lâu dài
            - Làm tổn thương niêm mạc dạ dày

            **3. Rượu bia:**
            - Kích thích niêm mạc dạ dày
            - Uống nhiều → Viêm cấp

            **4. Stress:**
            - Stress nặng → Viêm dạ dày cấp
            - Stress kéo dài → Viêm mạn

            **5. Yếu tố khác:**
            - Thức ăn cay, chua (không phải nguyên nhân chính)
            - Hút thuốc lá
            - Bệnh tự miễn (hiếm)

            ## Chẩn đoán:

            **1. Nội soi dạ dày:**
            - Xem trực tiếp niêm mạc dạ dày
            - Sinh thiết (tìm H. pylori, loại trừ ung thư)
            - Chính xác nhất

            **2. Xét nghiệm H. pylori:**
            - Test thở
            - Xét nghiệm phân
            - Xét nghiệm máu

            **3. Xét nghiệm khác:**
            - Công thức máu (nếu chảy máu)
            - Test phân tìm máu ẩn

            ## Điều trị:

            **1. Điều trị H. pylori (nếu có):**
            - Phác đồ 3 thuốc (14 ngày)
            - PPI + 2 kháng sinh
            - Uống đủ ngày, đúng giờ

            **2. Thuốc giảm axit:**
            - **PPI:** Omeprazole, Pantoprazole
              - Uống trước ăn 30 phút
              - Uống 4-8 tuần
            - **H2 Blockers:** Ranitidine, Famotidine

            **3. Thuốc bảo vệ niêm mạc:**
            - Sucralfate
            - Bismuth

            **4. Tránh thuốc gây tổn thương:**
            - Không dùng NSAID (nếu có thể)
            - Nếu cần → Dùng kèm PPI

            ## 🍽️ CHẾ ĐỘ ĂN CHO NGƯỜI VIÊM DẠ DÀY:

            **1. Nguyên tắc:**
            - **Ăn đúng giờ:** Không bỏ bữa
            - **Ăn nhiều bữa nhỏ:** 5-6 bữa/ngày
            - **Ăn chậm, nhai kỹ:** Giúp tiêu hóa tốt
            - **Tránh thức ăn kích thích:** Đồ cay, chua, nóng, lạnh

            **2. Thực phẩm NÊN ĂN:**
            - **Cháo, súp:** Dễ tiêu, ấm
              - Cháo gà, cháo thịt bằm
              - Súp rau củ
            - **Thức ăn mềm:** Luộc, hấp
            - **Rau xanh:** Luộc, hấp (rau cải, rau muống)
            - **Trái cây:** Chuối, táo (không quá chua)
            - **Sữa:** Sữa ấm, sữa chua (ít chua)
            - **Thịt nạc:** Thịt gà, cá (luộc, hấp)

            **3. Thực phẩm CẦN TRÁNH:**
            - **Đồ cay:** Ớt, tiêu, gừng (nhiều)
            - **Đồ chua:** Chanh, dấm, cam chua
            - **Đồ nóng, lạnh:** Nước đá, đồ quá nóng
            - **Đồ chiên, nhiều dầu mỡ:** Khó tiêu
            - **Rượu bia:** Kích thích dạ dày
            - **Cà phê, trà đặc:** Tăng tiết axit
            - **Đồ chế biến sẵn:** Đồ hộp, thức ăn nhanh

            **4. Thực đơn mẫu (1 ngày):**
            - **Sáng:** Cháo gà + sữa ấm
            - **Bữa phụ (10h):** Bánh mì mềm, sữa chua
            - **Trưa:** 1 chén cơm mềm + cá hấp + rau luộc + canh rau
            - **Bữa phụ (15h):** Chuối, bánh quy
            - **Tối:** 1 chén cơm mềm + thịt gà luộc + rau luộc + canh
            - **Bữa phụ (21h):** Sữa ấm

            **5. Lưu ý:**
            - Ăn chậm, nhai kỹ
            - Không ăn quá no
            - Không nằm ngay sau ăn (chờ 2-3 giờ)
            - Uống nước ấm, không uống lạnh

            ## 💊 QUẢN LÝ THUỐC:

            **1. Thuốc điều trị H. pylori:**
            - Uống đủ 14 ngày
            - Uống đúng giờ
            - Không tự ý ngừng

            **2. Thuốc PPI:**
            - Uống trước ăn 30 phút
            - Uống đủ 4-8 tuần
            - Không tự ý ngừng

            **3. Tránh NSAID:**
            - Không dùng Aspirin, Ibuprofen, Diclofenac
            - Nếu cần giảm đau → Dùng Paracetamol
            - Nếu bắt buộc dùng NSAID → Dùng kèm PPI

            ## 🛡️ PHÒNG NGỪA:

            **1. Điều trị H. pylori:**
            - Nếu có → Điều trị triệt để
            - Giảm nguy cơ tái phát

            **2. Tránh thuốc gây tổn thương:**
            - Không tự ý dùng NSAID lâu dài
            - Nếu cần → Dùng kèm PPI

            **3. Lối sống:**
            - **Bỏ thuốc lá:** Làm tổn thương niêm mạc
            - **Hạn chế rượu bia:** Kích thích dạ dày
            - **Quản lý stress:** Tập thư giãn, yoga
            - **Ăn đúng giờ:** Không bỏ bữa

            **4. Chế độ ăn:**
            - Tránh thức ăn kích thích
            - Ăn nhiều bữa nhỏ
            - Ăn chậm, nhai kỹ

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Chảy máu:**
            - Nôn ra máu
            - Đi ngoài phân đen
            - Mệt mỏi, da xanh (thiếu máu)

            **2. Triệu chứng nặng:**
            - Đau bụng dữ dội
            - Nôn nhiều, không ăn được
            - Sụt cân

            **3. Không cải thiện:**
            - Điều trị 4-8 tuần không đỡ
            - Triệu chứng nặng hơn

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Khi bị viêm dạ dày:**
            - Tuân thủ điều trị
            - Uống thuốc đúng giờ, đủ ngày
            - Chế độ ăn phù hợp
            - Tái khám sau điều trị

            **2. Phòng ngừa tái phát:**
            - Điều trị H. pylori triệt để
            - Tránh NSAID
            - Bỏ thuốc lá, hạn chế rượu bia
            - Ăn đúng giờ, không bỏ bữa
            - Quản lý stress

            **3. Sống tích cực:**
            - Viêm dạ dày có thể chữa khỏi
            - Tuân thủ điều trị → Khỏi bệnh
            """,
            related_disease="gastritis",
            related_drugs=["Omeprazole", "Amoxicillin", "Clarithromycin"],
            printable=True
        ),

        PatientEducationTopic(
            id="acute_diarrhea_basics",
            title="Understanding Acute Diarrhea",
            title_vn="Hiểu về Tiêu chảy cấp",
            category="Disease",
            content="""
            # Hiểu về Tiêu chảy cấp

            ## Tiêu chảy cấp là gì?

            Tiêu chảy cấp là tình trạng đi ngoài phân lỏng > 3 lần/ngày, kéo dài < 14 ngày. Có thể gây mất nước nghiêm trọng, đặc biệt nguy hiểm ở trẻ em.

            **⚠️ Đặc điểm:**
            - Rất phổ biến, đặc biệt ở trẻ em
            - Nguy hiểm nhất là mất nước
            - Hầu hết tự khỏi sau vài ngày
            - Cần bù nước đúng cách

            **Phân loại:**
            - **Tiêu chảy cấp:** < 14 ngày
            - **Tiêu chảy mạn:** > 14 ngày

            ## Triệu chứng:

            **Triệu chứng điển hình:**
            - **Đi ngoài phân lỏng:** > 3 lần/ngày
            - **Phân:** Lỏng, nước, có thể có máu, nhầy
            - **Đau bụng:** Quặn, từng cơn
            - **Buồn nôn, nôn:** Có thể có
            - **Sốt:** Có thể có (nếu nhiễm trùng)

            **Triệu chứng mất nước:**
            - **Khát nước:** Khát nhiều
            - **Tiểu ít:** Nước tiểu vàng đậm
            - **Mắt trũng:** Mắt lõm
            - **Da khô:** Da nhăn, mất đàn hồi
            - **Mệt mỏi:** Uể oải, không có sức
            - **Chóng mặt:** Khi đứng dậy

            **Triệu chứng mất nước nặng (Cần cấp cứu!):**
            - Không tiểu hoặc tiểu rất ít
            - Mắt rất trũng
            - Da rất khô, nhăn
            - Lú lẫn, buồn ngủ
            - Mạch nhanh, yếu
            - Huyết áp tụt

            ## Nguyên nhân:

            **1. Nhiễm trùng:**
            - **Virus:** Rotavirus, Norovirus (phổ biến nhất)
            - **Vi khuẩn:** E. coli, Salmonella, Shigella, Campylobacter
            - **Ký sinh trùng:** Giardia, Cryptosporidium

            **2. Thức ăn, nước uống:**
            - **Thức ăn nhiễm khuẩn:** Không nấu chín, để lâu
            - **Nước uống không sạch:** Nước chưa đun sôi
            - **Vệ sinh kém:** Tay bẩn, dụng cụ bẩn

            **3. Thuốc:**
            - Kháng sinh (tiêu chảy do kháng sinh)
            - Một số thuốc khác

            **4. Yếu tố khác:**
            - Không dung nạp thức ăn
            - Stress

            ## Chẩn đoán:

            **1. Khám lâm sàng:**
            - Đánh giá triệu chứng
            - Đánh giá mất nước
            - Khám bụng

            **2. Xét nghiệm:**
            - **Cấy phân:** Tìm vi khuẩn (nếu cần)
            - **Soi phân:** Tìm ký sinh trùng (nếu cần)
            - **Xét nghiệm máu:** Đánh giá mất nước, điện giải

            **3. Thường không cần:**
            - Hầu hết tiêu chảy cấp tự khỏi
            - Chỉ xét nghiệm khi nặng hoặc kéo dài

            ## Điều trị:

            **⚠️ QUAN TRỌNG:** Bù nước là điều trị chính!

            **1. Bù nước (QUAN TRỌNG NHẤT!):**
            - **Oresol:** Tốt nhất (bù nước và điện giải)
              - Pha đúng tỷ lệ (1 gói + 1 lít nước)
              - Uống từng ngụm nhỏ, thường xuyên
              - Uống ngay cả khi nôn
            - **Nước lọc:** Nếu không có Oresol
            - **Nước trái cây:** Pha loãng
            - **Súp, canh:** Vừa ăn vừa uống nước

            **2. Điều trị tại nhà (Nhẹ):**
            - Bù nước (Oresol)
            - Ăn nhẹ, dễ tiêu
            - Nghỉ ngơi
            - Theo dõi triệu chứng

            **3. Điều trị tại viện (Nặng):**
            - Truyền dịch (nếu mất nước nặng)
            - Kháng sinh (nếu nhiễm trùng do vi khuẩn)
            - Điều trị hỗ trợ

            **4. Thuốc:**
            - **Kháng sinh:** Chỉ khi nhiễm trùng do vi khuẩn (hiếm)
            - **Thuốc cầm tiêu chảy:** Loperamide (thận trọng, không dùng ở trẻ em)
            - **⚠️ KHÔNG tự ý dùng kháng sinh!**

            ## 🍽️ CHẾ ĐỘ ĂN KHI BỊ TIÊU CHẢY:

            **⚠️ QUAN TRỌNG:** Vẫn cần ăn để cung cấp năng lượng!

            **1. Nguyên tắc:**
            - **Bù nước:** Quan trọng nhất!
            - **Ăn nhẹ, dễ tiêu:** Tránh đồ khó tiêu
            - **Chia nhỏ bữa:** 5-6 bữa/ngày
            - **Tránh thức ăn kích thích:** Đồ cay, nhiều dầu mỡ

            **2. Uống nước (QUAN TRỌNG NHẤT!):**
            - **Oresol:** Tốt nhất
              - Pha đúng tỷ lệ
              - Uống từng ngụm nhỏ, thường xuyên
              - Uống ngay cả khi nôn (uống lại sau 10-15 phút)
            - **Nước lọc:** Nếu không có Oresol
            - **Nước trái cây:** Pha loãng (cam, chanh)
            - **Súp, canh:** Vừa ăn vừa uống nước
            - **⚠️ Tránh:** Nước ngọt có ga, rượu bia

            **3. Thực phẩm NÊN ĂN:**
            - **Cháo, súp:** Dễ tiêu, có nước
              - Cháo gạo, cháo thịt bằm
              - Súp rau củ
            - **Cơm mềm:** Ít, với thức ăn nhẹ
            - **Chuối:** Kali, dễ tiêu
            - **Táo:** Pectin (giúp cầm tiêu chảy)
            - **Bánh mì:** Mềm, không bơ
            - **Khoai tây:** Luộc, nghiền

            **4. Thực phẩm CẦN TRÁNH:**
            - **Sữa, sản phẩm sữa:** Khó tiêu (trừ sữa mẹ ở trẻ bú mẹ)
            - **Đồ chiên, nhiều dầu mỡ:** Khó tiêu
            - **Đồ cay:** Kích thích ruột
            - **Đồ ngọt nhiều:** Bánh kẹo, nước ngọt
            - **Rượu bia:** Làm mất nước
            - **Cà phê:** Làm mất nước

            **5. Thực đơn mẫu (1 ngày):**
            - **Sáng:** Cháo gạo + chuối
            - **Bữa phụ (10h):** Oresol, bánh mì mềm
            - **Trưa:** Cháo thịt bằm + táo
            - **Bữa phụ (15h):** Oresol, chuối
            - **Tối:** Cơm mềm (ít) + khoai tây luộc
            - **Uống:** Oresol, nước lọc, súp

            **6. Lưu ý:**
            - Uống nước ngay cả khi không khát
            - Uống từng ngụm nhỏ, thường xuyên
            - Nếu nôn → Uống lại sau 10-15 phút
            - Ăn chậm, nhai kỹ
            - Không bỏ ăn hoàn toàn

            ## 🛡️ PHÒNG NGỪA:

            **1. Vệ sinh cá nhân:**
            - **Rửa tay:** Thường xuyên với xà phòng
              - Trước khi ăn
              - Sau khi đi vệ sinh
              - Sau khi thay tã
              - Sau khi chơi
            - **Vệ sinh răng miệng:** Đánh răng 2 lần/ngày

            **2. Vệ sinh thực phẩm:**
            - **Nấu chín:** Thức ăn phải nấu chín kỹ
            - **Rửa sạch:** Rau, trái cây
            - **Bảo quản:** Thức ăn trong tủ lạnh
            - **Tránh:** Thức ăn để lâu, không rõ nguồn gốc

            **3. Nước uống:**
            - **Đun sôi:** Nước uống phải đun sôi
            - **Sạch:** Dùng nước sạch
            - **Tránh:** Nước chưa đun sôi, nước đá không rõ nguồn gốc

            **4. Vệ sinh môi trường:**
            - Vệ sinh nhà cửa
            - Xử lý phân đúng cách
            - Diệt ruồi, gián

            **5. Tiêm chủng:**
            - **Vắc xin Rotavirus:** Cho trẻ (phòng ngừa tiêu chảy do Rotavirus)

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Mất nước nặng:**
            - Không tiểu hoặc tiểu rất ít
            - Mắt rất trũng
            - Da rất khô, nhăn
            - Lú lẫn, buồn ngủ
            - Mạch nhanh, yếu
            - Huyết áp tụt

            **2. Triệu chứng nặng:**
            - Sốt cao > 39°C
            - Đau bụng dữ dội
            - Đi ngoài ra máu
            - Nôn nhiều, không uống được

            **3. Trẻ em:**
            - Trẻ < 6 tháng
            - Tiêu chảy > 24 giờ
            - Nôn nhiều
            - Sốt cao
            - Có dấu hiệu mất nước

            **4. Không cải thiện:**
            - Tiêu chảy > 3 ngày không đỡ
            - Triệu chứng nặng hơn

            **⚠️ QUAN TRỌNG:** Đến bệnh viện ngay khi có dấu hiệu mất nước nặng!

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Khi bị tiêu chảy:**
            - Bù nước ngay (Oresol)
            - Ăn nhẹ, dễ tiêu
            - Nghỉ ngơi
            - Theo dõi triệu chứng

            **2. Phòng ngừa:**
            - Rửa tay thường xuyên
            - Vệ sinh thực phẩm
            - Nước uống sạch
            - Tiêm vắc xin (nếu có)

            **3. Không tự ý:**
            - Dùng kháng sinh (hầu hết không cần)
            - Dùng thuốc cầm tiêu chảy ở trẻ em (nguy hiểm)

            **4. Sống tích cực:**
            - Hầu hết tiêu chảy cấp tự khỏi
            - Bù nước đúng cách → Khỏi nhanh
            """,
            related_disease="acute_diarrhea",
            related_drugs=["Oresol", "Loperamide"],
            printable=True
        ),

        PatientEducationTopic(
            id="cirrhosis_basics",
            title="Understanding Cirrhosis",
            title_vn="Hiểu về Xơ gan",
            category="Disease",
            content="""
            # Hiểu về Xơ gan

            ## Xơ gan là gì?

            Xơ gan là tình trạng thay thế mô gan bình thường bằng mô xơ, dẫn đến suy giảm chức năng gan. Bệnh rất phổ biến tại Việt Nam, thường do viêm gan B/C mạn tính hoặc rượu bia.

            **⚠️ Đặc điểm:**
            - Mô gan bị thay thế bằng mô xơ
            - Suy giảm chức năng gan
            - Không thể hồi phục (nhưng có thể làm chậm tiến triển)
            - Phổ biến ở Việt Nam

            **Nguyên nhân chính tại Việt Nam:**
            - Viêm gan B, C mạn tính (60-70%)
            - Rượu bia (20-30%)
            - Viêm gan nhiễm mỡ không do rượu (NAFLD)

            ## Triệu chứng:

            **Giai đoạn sớm (compensated):**
            - Thường không có triệu chứng
            - Mệt mỏi nhẹ
            - Có thể phát hiện khi khám sức khỏe

            **Giai đoạn muộn (decompensated):**
            - **Vàng da, vàng mắt:** Bilirubin tăng
            - **Phù chân:** Do giảm albumin
            - **Cổ trướng:** Bụng to, đầy hơi
            - **Mệt mỏi, suy nhược**
            - **Xuất huyết:** Chảy máu cam, chảy máu chân răng
            - **Lú lẫn:** Bệnh não gan
            - **Giảm cân**

            **⚠️ Biến chứng:**
            - Xuất huyết tiêu hóa (giãn tĩnh mạch thực quản)
            - Bệnh não gan (lú lẫn, hôn mê)
            - Nhiễm trùng dịch cổ trướng
            - Ung thư gan
            - Suy gan

            ## Nguyên nhân:

            **1. Viêm gan B, C mạn:**
            - Nguyên nhân #1 tại Việt Nam
            - Không điều trị → Xơ gan

            **2. Rượu bia:**
            - Uống nhiều, lâu dài
            - > 40g rượu/ngày (nam), > 20g (nữ)

            **3. Viêm gan nhiễm mỡ:**
            - Béo phì, đái tháo đường
            - Không do rượu

            **4. Yếu tố khác:**
            - Bệnh gan tự miễn
            - Thuốc
            - Di truyền

            ## Chẩn đoán:

            **Xét nghiệm:**
            - Chức năng gan: Giảm albumin, tăng bilirubin, PT kéo dài
            - Siêu âm gan: Gan nhỏ, bờ không đều
            - FibroScan: Đánh giá độ xơ hóa
            - Sinh thiết gan (nếu cần)

            ## Điều trị:

            **1. Điều trị nguyên nhân:**
            - Diệt virus (nếu viêm gan B/C)
            - **Bỏ rượu bia HOÀN TOÀN** (quan trọng!)

            **2. Điều trị biến chứng:**
            - **Cổ trướng:** Lợi tiểu (Furosemide, Spironolactone), giảm muối
            - **Bệnh não gan:** Lactulose
            - **Xuất huyết:** Beta-blocker (Propranolol), nội soi

            **3. Ghép gan:**
            - Nếu nặng, suy gan

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Protein:**
            - **Đủ protein:** 1-1.2g/kg/ngày (nếu không có bệnh não gan)
            - **Giảm protein:** 0.8g/kg/ngày (nếu có bệnh não gan)
            - Protein nạc: Thịt gà, cá, trứng, đậu

            **2. Muối:**
            - **Giảm muối:** < 2g/ngày (nếu có cổ trướng)
            - Tránh đồ mặn, chế biến sẵn

            **3. Nước:**
            - Hạn chế nước (nếu có cổ trướng): 1-1.5L/ngày

            **4. Tránh:**
            - **Rượu bia HOÀN TOÀN** (quan trọng nhất!)
            - Đồ cay, nóng
            - Thực phẩm chế biến sẵn

            **5. Thực đơn mẫu:**
            - **Sáng:** Cháo thịt, trứng
            - **Trưa:** Cơm, thịt gà/cá, rau xanh, canh (không mặn)
            - **Chiều:** Cơm, thịt/cá, rau xanh, canh
            - **Bữa phụ:** Trái cây, sữa

            ## 🏃 TẬP THỂ DỤC:

            **1. Khi ổn định:**
            - Tập nhẹ: Đi bộ 15-20 phút/ngày
            - Tránh gắng sức (mệt mỏi)

            **2. Khi có cổ trướng:**
            - Nghỉ ngơi, tránh tập thể dục

            **3. Lưu ý:**
            - Nghỉ ngơi nếu mệt
            - Không tập quá mệt

            ## 💊 QUẢN LÝ THUỐC:

            **1. Điều trị nguyên nhân:**
            - Tenofovir, Entecavir (nếu viêm gan B)
            - DAA (nếu viêm gan C)
            - **Bỏ rượu bia HOÀN TOÀN**

            **2. Lợi tiểu:**
            - Furosemide, Spironolactone (nếu cổ trướng)
            - Theo dõi cân nặng, điện giải

            **3. Lactulose:**
            - Nếu bệnh não gan
            - Uống để đi ngoài 2-3 lần/ngày

            **4. Lưu ý:**
            - Tránh thuốc gây độc gan
            - Không tự ý dùng thuốc
            - Báo bác sĩ tất cả thuốc đang dùng

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Xuất huyết:**
            - Nôn ra máu
            - Đi ngoài phân đen
            - **Cấp cứu ngay!**

            **2. Bệnh não gan:**
            - Lú lẫn, thay đổi tính tình
            - Buồn ngủ, hôn mê
            - **Cấp cứu ngay!**

            **3. Nhiễm trùng:**
            - Sốt, đau bụng
            - Cổ trướng tăng

            **4. Triệu chứng nặng:**
            - Vàng da nặng
            - Cổ trướng nhiều
            - Khó thở

            ## 💡 PHÒNG NGỪA:

            **1. Điều trị viêm gan:**
            - Điều trị viêm gan B, C sớm
            - Tiêm vắc xin viêm gan B

            **2. Bỏ rượu bia:**
            - **HOÀN TOÀN** nếu đã xơ gan
            - Hạn chế nếu chưa xơ gan

            **3. Kiểm soát cân nặng:**
            - Giảm cân nếu béo phì
            - Kiểm soát đái tháo đường

            **4. Khám định kỳ:**
            - Nếu có bệnh gan
            - Siêu âm gan, AFP (phòng ung thư gan)

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Khi bị xơ gan:**
            - **Bỏ rượu bia HOÀN TOÀN** (quan trọng nhất!)
            - Điều trị nguyên nhân
            - Chế độ ăn phù hợp
            - Khám định kỳ

            **2. Chế độ ăn:**
            - Đủ protein (nếu không có bệnh não gan)
            - Giảm muối (nếu có cổ trướng)
            - Tránh rượu bia HOÀN TOÀN

            **3. Sống tích cực:**
            - Xơ gan không thể hồi phục
            - Nhưng có thể làm chậm tiến triển
            - Điều trị đúng → Sống lâu hơn

            **4. Theo dõi:**
            - Khám định kỳ 3-6 tháng
            - Siêu âm gan, AFP (phòng ung thư gan)
            - Theo dõi biến chứng
            """,
            related_disease="cirrhosis",
            related_drugs=["Furosemide", "Spironolactone", "Lactulose", "Propranolol", "Tenofovir", "Entecavir"],
            printable=True
        ),

        PatientEducationTopic(
            id="irritable_bowel_syndrome_basics",
            title="Understanding Irritable Bowel Syndrome",
            title_vn="Hiểu về Hội chứng ruột kích thích (IBS)",
            category="Disease",
            content="""
            # Hiểu về Hội chứng ruột kích thích (IBS)

            ## Hội chứng ruột kích thích là gì?

            Hội chứng ruột kích thích (IBS) là rối loạn chức năng đường tiêu hóa mạn tính, đặc trưng bởi đau bụng và thay đổi thói quen đại tiện. Bệnh rất phổ biến tại Việt Nam, ảnh hưởng đến chất lượng cuộc sống.

            **⚠️ Đặc điểm:**
            - Rối loạn chức năng (không có tổn thương thực thể)
            - Mạn tính, tái phát
            - Rất phổ biến (10-15% dân số)
            - Ảnh hưởng chất lượng cuộc sống

            **Phân loại:**
            - **IBS-D:** Tiêu chảy (diarrhea)
            - **IBS-C:** Táo bón (constipation)
            - **IBS-M:** Hỗn hợp (mixed)

            ## Triệu chứng:

            **Triệu chứng điển hình:**
            - **Đau bụng:** Giảm sau đại tiện
            - **Thay đổi thói quen đại tiện:**
              - Tiêu chảy (IBS-D)
              - Táo bón (IBS-C)
              - Xen kẽ (IBS-M)
            - **Đầy bụng, chướng bụng**
            - **Phân có nhầy**
            - **Cảm giác đi không hết**

            **Triệu chứng khác:**
            - Mệt mỏi
            - Đau lưng
            - Triệu chứng tăng khi stress

            **⚠️ Triệu chứng báo động (cần khám ngay):**
            - Sụt cân
            - Thiếu máu
            - Chảy máu trực tràng
            - Sốt
            - Tiền sử gia đình ung thư đại tràng

            ## Nguyên nhân:

            **1. Nguyên nhân chưa rõ:**
            - Rối loạn vận động ruột
            - Tăng nhạy cảm nội tạng
            - Rối loạn hệ vi sinh đường ruột

            **2. Yếu tố kích thích:**
            - **Stress, lo âu:** Rất quan trọng
            - **Thức ăn:** FODMAP, lactose, gluten
            - **Thay đổi hormone:** Kinh nguyệt

            **3. Yếu tố nguy cơ:**
            - Nữ giới (gấp 2 lần nam)
            - Tuổi < 50
            - Tiền sử gia đình
            - Nhiễm trùng đường tiêu hóa trước đó

            ## Chẩn đoán:

            **Tiêu chuẩn Rome IV:**
            - Đau bụng ≥ 1 ngày/tuần trong 3 tháng
            - Có ≥ 2: liên quan đại tiện, thay đổi tần số, thay đổi hình dạng phân

            **Xét nghiệm:**
            - Công thức máu (loại trừ thiếu máu)
            - CRP, ESR (loại trừ viêm)
            - Test không dung nạp lactose
            - Nội soi đại tràng (nếu có triệu chứng báo động)

            ## Điều trị:

            **1. Chế độ ăn FODMAP thấp:**
            - **Tránh:** Sữa, lúa mì, hành, tỏi, đậu, trái cây có nhiều fructose
            - **Nên ăn:** Gạo, thịt, cá, trứng, rau xanh, chuối
            - Thử 2-6 tuần, sau đó thêm từng loại

            **2. Thuốc:**
            - **Antispasmodic:** Hyoscine, Mebeverine (giảm đau bụng)
            - **Loperamide:** Nếu tiêu chảy
            - **Laxative:** Nếu táo bón
            - **Chất xơ:** Psyllium (nếu táo bón)
            - **Probiotic:** Có thể giúp

            **3. Quản lý stress:**
            - Tập thể dục
            - Yoga, thiền
            - Tư vấn tâm lý (nếu cần)

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. FODMAP thấp (thử 2-6 tuần):**
            - **Tránh:**
              - Sữa, phô mai mềm
              - Lúa mì, bánh mì
              - Hành, tỏi
              - Đậu, đậu lăng
              - Táo, lê, xoài
            - **Nên ăn:**
              - Gạo, khoai tây
              - Thịt, cá, trứng
              - Rau xanh (rau muống, cải)
              - Chuối, cam

            **2. Ăn đều đặn:**
            - Không bỏ bữa
            - Ăn chậm, nhai kỹ
            - Uống đủ nước

            **3. Ghi nhật ký:**
            - Ghi thức ăn và triệu chứng
            - Tìm thức ăn gây triệu chứng

            **4. Thực đơn mẫu (FODMAP thấp):**
            - **Sáng:** Cơm, trứng, rau xanh
            - **Trưa:** Cơm, thịt/cá, rau xanh, canh
            - **Chiều:** Cơm, thịt/cá, rau xanh, canh
            - **Bữa phụ:** Chuối, cam

            ## 🏃 TẬP THỂ DỤC:

            **1. Nên tập:**
            - Tập thể dục đều đặn (giảm stress, cải thiện triệu chứng)
            - Đi bộ, chạy bộ, yoga
            - 30 phút/ngày, 5 ngày/tuần

            **2. Lưu ý:**
            - Tránh tập ngay sau ăn
            - Nghỉ ngơi nếu mệt

            ## 💊 QUẢN LÝ THUỐC:

            **1. Antispasmodic:**
            - Hyoscine, Mebeverine
            - Uống trước ăn (nếu đau bụng)

            **2. Loperamide:**
            - Nếu tiêu chảy
            - Không dùng lâu dài

            **3. Laxative:**
            - Nếu táo bón
            - Dùng ngắn hạn

            **4. Probiotic:**
            - Có thể giúp cải thiện triệu chứng
            - Thử 4-8 tuần

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Triệu chứng báo động:**
            - Sụt cân
            - Thiếu máu
            - Chảy máu trực tràng
            - Sốt
            - > 50 tuổi, triệu chứng mới

            **2. Triệu chứng nặng:**
            - Đau bụng dữ dội
            - Tiêu chảy nhiều, mất nước
            - Táo bón nặng

            ## 💡 PHÒNG NGỪA:

            **1. Chế độ ăn:**
            - Tránh thức ăn kích thích
            - Ăn đều đặn
            - Ghi nhật ký

            **2. Quản lý stress:**
            - Tập thể dục
            - Yoga, thiền
            - Ngủ đủ giấc

            **3. Tập thể dục:**
            - Đều đặn
            - Giảm stress

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Khi bị IBS:**
            - Chế độ ăn FODMAP thấp (thử)
            - Quản lý stress (quan trọng!)
            - Tập thể dục đều đặn
            - Ghi nhật ký thức ăn

            **2. Sống tích cực:**
            - IBS không nguy hiểm
            - Có thể kiểm soát
            - Điều trị đúng → Giảm triệu chứng

            **3. Hỗ trợ:**
            - Tham gia nhóm hỗ trợ
            - Tư vấn tâm lý (nếu cần)
            """,
            related_disease="irritable_bowel_syndrome",
            related_drugs=["Hyoscine", "Mebeverine", "Loperamide", "Psyllium", "Probiotic"],
            printable=True
        ),

        PatientEducationTopic(
            id="rotavirus_diarrhea_basics",
            title="Understanding Rotavirus Diarrhea",
            title_vn="Hiểu về Tiêu chảy do Rotavirus",
            category="Disease",
            content="""
            # Hiểu về Tiêu chảy do Rotavirus

            ## Tiêu chảy do Rotavirus là gì?

            Tiêu chảy do Rotavirus là bệnh nhiễm virus đường ruột do Rotavirus gây ra, đặc trưng bởi tiêu chảy nhiều nước, nôn, sốt. Bệnh rất phổ biến ở trẻ em Việt Nam, đặc biệt trẻ < 2 tuổi, là nguyên nhân hàng đầu gây tiêu chảy nặng ở trẻ em.

            **⚠️ Đặc điểm:**
            - Bệnh nhiễm virus đường ruột
            - Tiêu chảy nhiều nước, nôn, sốt
            - Rất phổ biến ở trẻ em < 2 tuổi
            - Nguyên nhân hàng đầu gây tiêu chảy nặng

            ## Triệu chứng:

            **Triệu chứng điển hình:**
            - **Tiêu chảy:** Tiêu chảy nhiều nước, không có máu, mùi chua
            - **Nôn:** Nôn nhiều, có thể nôn liên tục
            - **Sốt:** Sốt nhẹ đến vừa (37.5-39°C)
            - **Đau bụng:** Đau bụng, quấy khóc
            - **Mệt mỏi, suy nhược**

            **Triệu chứng khác:**
            - Chán ăn
            - Khát nước
            - Giảm đi tiểu

            **⚠️ Mất nước:**
            - **Nhẹ:** Khát nước, môi khô
            - **Vừa:** Mắt trũng, da nhăn, giảm đi tiểu
            - **Nặng:** Mệt mỏi nặng, lơ mơ, không uống được, sốc

            **⚠️ Biến chứng:**
            - Mất nước nặng
            - Rối loạn điện giải
            - Sốc
            - Tử vong (nếu không điều trị)

            ## Nguyên nhân:

            **1. Virus:**
            - Rotavirus
            - Có nhiều type (A, B, C...)

            **2. Lây truyền:**
            - **Phân-miệng:** Từ phân người bệnh
            - **Tiếp xúc trực tiếp:** Tay, đồ vật bị nhiễm
            - **Gián tiếp:** Đồ chơi, bề mặt bị nhiễm
            - **Nước, thức ăn:** Bị nhiễm virus

            **3. Yếu tố nguy cơ:**
            - Trẻ em < 2 tuổi
            - Chưa tiêm vắc xin
            - Vệ sinh kém
            - Sống đông đúc
            - Suy dinh dưỡng

            ## Chẩn đoán:

            **Chẩn đoán lâm sàng:**
            - Triệu chứng điển hình
            - Trẻ em < 2 tuổi

            **Xét nghiệm:**
            - **Test nhanh:** Kháng nguyên Rotavirus trong phân
            - **PCR:** Phát hiện RNA virus
            - **Cấy virus:** Ít dùng

            ## Điều trị:

            **1. Bù dịch (QUAN TRỌNG NHẤT!):**
            - **Oresol:** Uống ngay khi bắt đầu tiêu chảy
            - **Cách uống:** Uống từng ngụm nhỏ, thường xuyên
            - **Liều lượng:** 50-100ml sau mỗi lần đi ngoài (trẻ em)
            - **Truyền dịch:** Nếu mất nước nặng, không uống được

            **2. Điều trị triệu chứng:**
            - **Hạ sốt:** Paracetamol khi sốt > 38.5°C
            - **Giảm nôn:** Domperidone (nếu cần)
            - **Kẽm:** 10-20mg/ngày, 10-14 ngày (giảm tiêu chảy)

            **3. Dinh dưỡng:**
            - **Tiếp tục bú mẹ:** Nếu đang bú mẹ
            - **Tiếp tục ăn:** Ăn thức ăn mềm, dễ tiêu
            - **Tránh:** Nhịn ăn (làm bệnh nặng)

            **4. Không dùng:**
            - **Kháng sinh:** Không có tác dụng (virus)
            - **Thuốc cầm tiêu chảy:** Loperamide (nguy hiểm ở trẻ em)

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Khi đang tiêu chảy:**
            - **Tiếp tục bú mẹ:** Nếu đang bú mẹ (quan trọng!)
            - **Tiếp tục ăn:** Ăn thức ăn mềm, dễ tiêu
            - **Uống Oresol:** Uống từng ngụm nhỏ, thường xuyên
            - **Tránh:** Nhịn ăn, thức ăn khó tiêu, nhiều đường

            **2. Thức ăn phù hợp:**
            - Cháo, súp
            - Cơm mềm
            - Thịt, cá nấu chín (ít)
            - Trái cây: Chuối, táo
            - Tránh: Sữa công thức (nếu không dung nạp), nước ngọt

            **3. Sau khi khỏi:**
            - Ăn đủ dinh dưỡng
            - Bổ sung vitamin, khoáng chất
            - Tăng dần lượng thức ăn

            **4. Thực đơn mẫu (trẻ em):**
            - **Sáng:** Cháo thịt
            - **Trưa:** Cháo/cơm mềm, thịt/cá (ít), chuối
            - **Chiều:** Cháo/cơm mềm, thịt/cá (ít), chuối
            - **Bữa phụ:** Sữa mẹ, sữa công thức (nếu dung nạp)

            ## 🏃 TẬP THỂ DỤC:

            **1. Khi đang bệnh:**
            - Nghỉ ngơi tại nhà
            - Tránh gắng sức
            - Cách ly cho đến khi khỏi

            **2. Sau khi khỏi:**
            - Tập thể dục từ từ
            - Tăng dần cường độ

            ## 💊 QUẢN LÝ THUỐC:

            **1. Oresol (QUAN TRỌNG!):**
            - Uống ngay khi bắt đầu tiêu chảy
            - Uống từng ngụm nhỏ, thường xuyên
            - Pha đúng liều (theo hướng dẫn)
            - Uống 50-100ml sau mỗi lần đi ngoài (trẻ em)

            **2. Hạ sốt:**
            - Paracetamol: Khi sốt > 38.5°C
            - Không quá 4 lần/ngày (trẻ em)

            **3. Kẽm:**
            - 10-20mg/ngày, 10-14 ngày
            - Giảm tiêu chảy, tái phát

            **4. Lưu ý:**
            - **Không dùng kháng sinh** (virus)
            - **Không dùng thuốc cầm tiêu chảy** ở trẻ em
            - Báo bác sĩ nếu mất nước nặng

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Mất nước nặng:**
            - Mắt trũng, da nhăn
            - Lơ mơ, không uống được
            - Không đi tiểu > 6 giờ
            - **Cấp cứu ngay!**

            **2. Trẻ nhỏ:**
            - Trẻ < 6 tháng
            - Tiêu chảy nhiều, nôn nhiều
            - Sốt cao

            **3. Triệu chứng nặng:**
            - Tiêu chảy > 10 lần/ngày
            - Nôn liên tục, không uống được
            - Sốt > 39°C
            - Có máu trong phân

            **4. Không đáp ứng:**
            - Tiêu chảy kéo dài > 7 ngày
            - Mất nước không cải thiện

            ## 💡 PHÒNG NGỪA:

            **1. Tiêm vắc xin (QUAN TRỌNG NHẤT!):**
            - **Vắc xin Rotavirus:** 2-3 mũi (2, 4, 6 tháng tuổi)
            - **Hiệu quả:** 70-90%
            - **Bảo vệ:** Giảm tiêu chảy nặng, nhập viện
            - **Đối tượng:** Tất cả trẻ em

            **2. Vệ sinh cá nhân:**
            - **Rửa tay:** Rửa tay bằng xà phòng trước khi ăn, sau khi đi vệ sinh
            - **Vệ sinh:** Giữ vệ sinh cá nhân sạch sẽ

            **3. Vệ sinh môi trường:**
            - Vệ sinh nhà vệ sinh
            - Vệ sinh đồ chơi, bề mặt
            - Xử lý phân đúng cách

            **4. Khi có người bệnh:**
            - Cách ly người bệnh
            - Vệ sinh dụng cụ ăn uống
            - Rửa tay sau khi tiếp xúc

            **5. Nuôi con bằng sữa mẹ:**
            - Nuôi con bằng sữa mẹ (giảm nguy cơ)

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Phòng ngừa:**
            - **Tiêm vắc xin** (quan trọng nhất!)
            - Rửa tay thường xuyên
            - Vệ sinh môi trường

            **2. Khi bị tiêu chảy do Rotavirus:**
            - **Bù dịch ngay** (quan trọng nhất!)
            - Uống Oresol từng ngụm nhỏ, thường xuyên
            - Tiếp tục bú mẹ, ăn uống
            - Theo dõi dấu hiệu mất nước

            **3. Sống tích cực:**
            - Tiêu chảy do Rotavirus thường tự khỏi
            - Bù dịch đúng cách → Giảm biến chứng
            - Phòng ngừa tốt → Không mắc bệnh
            - Tiêm vắc xin → Bảo vệ 70-90%

            **4. Trẻ em:**
            - Cần chăm sóc, theo dõi sát
            - Bù dịch ngay (quan trọng!)
            - Tiếp tục bú mẹ, ăn uống
            - Theo dõi dấu hiệu mất nước
            - Đến bệnh viện nếu mất nước nặng
            """,
            related_disease="rotavirus_diarrhea",
            related_drugs=["Oresol", "Paracetamol", "Zinc", "Domperidone"],
            printable=True
        ),

]
