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

        PatientEducationTopic(
            id="hemorrhoids_basics",
            title="Understanding Hemorrhoids",
            title_vn="Hiểu về Trĩ",
            category="Disease",
            content="""
            # Hiểu về Trĩ

            ## Trĩ là gì?

            Trĩ là tình trạng giãn tĩnh mạch ở vùng hậu môn-trực tràng, gây đau, chảy máu, khó chịu. Trĩ rất phổ biến ở Việt Nam, ảnh hưởng đến 50-70% dân số ở một thời điểm nào đó.

            **⚠️ Đặc điểm:**
            - Giãn tĩnh mạch vùng hậu môn-trực tràng
            - Rất phổ biến (50-70% dân số)
            - Có thể điều trị và phòng ngừa
            - Không nguy hiểm nhưng gây khó chịu

            **Phân loại:**
            - **Trĩ nội:** Bên trong hậu môn, không nhìn thấy
            - **Trĩ ngoại:** Bên ngoài hậu môn, có thể nhìn thấy, sờ thấy
            - **Trĩ hỗn hợp:** Cả trĩ nội và ngoại

            **Độ trĩ nội:**
            - **Độ 1:** Chỉ chảy máu, không sa
            - **Độ 2:** Sa khi rặn, tự co lên
            - **Độ 3:** Sa khi rặn, phải đẩy lên
            - **Độ 4:** Sa thường xuyên, không đẩy lên được

            ## Triệu chứng:

            **Triệu chứng điển hình:**
            - **Chảy máu:** Máu đỏ tươi khi đi cầu, dính trên giấy vệ sinh, nhỏ giọt hoặc phun thành tia
            - **Sa búi trĩ:** Búi trĩ sa ra ngoài khi đi cầu, rặn
            - **Đau:** Đau khi đi cầu, ngồi (đặc biệt trĩ ngoại)
            - **Ngứa, khó chịu:** Vùng hậu môn ngứa, ẩm ướt
            - **Cảm giác nặng:** Cảm giác nặng, tức ở hậu môn

            **Triệu chứng khác:**
            - Tiết dịch nhầy
            - Khó chịu khi ngồi
            - Cảm giác đi cầu không hết

            **⚠️ Biến chứng:**
            - **Nghẹt búi trĩ:** Búi trĩ sa, không đẩy lên được, sưng đau
            - **Tắc mạch:** Cục máu đông trong búi trĩ, đau dữ dội
            - **Thiếu máu:** Chảy máu nhiều, kéo dài

            ## Nguyên nhân:

            **1. Tăng áp lực vùng chậu:**
            - **Táo bón:** Rặn nhiều, lâu
            - **Tiêu chảy mạn tính:** Đi cầu nhiều lần
            - **Ngồi lâu:** Ngồi toilet lâu, đọc sách khi đi cầu
            - **Mang thai:** Tăng áp lực ổ bụng
            - **Sinh đẻ:** Rặn khi sinh

            **2. Yếu tố nguy cơ:**
            - **Tuổi:** Tăng theo tuổi (mạch máu yếu)
            - **Di truyền:** Có người thân bị trĩ
            - **Béo phì:** Tăng áp lực ổ bụng
            - **Ít vận động:** Ngồi nhiều
            - **Chế độ ăn:** Ít chất xơ, uống ít nước
            - **Lao động nặng:** Khuân vác, đứng lâu

            **3. Bệnh khác:**
            - Tăng áp lực tĩnh mạch cửa (xơ gan)
            - Khối u vùng chậu

            ## Chẩn đoán:

            **Chẩn đoán lâm sàng:**
            - Triệu chứng điển hình
            - Khám hậu môn-trực tràng

            **Khám:**
            - **Nhìn:** Quan sát vùng hậu môn (trĩ ngoại)
            - **Thăm trực tràng:** Phát hiện trĩ nội
            - **Soi hậu môn:** Đánh giá độ trĩ, loại trừ bệnh khác

            **Xét nghiệm:**
            - **Soi đại tràng sigma:** Nếu chảy máu nhiều, tuổi > 50
            - **Xét nghiệm máu:** Nếu thiếu máu

            ## Điều trị:

            **1. Điều trị không phẫu thuật (Trĩ độ 1-2):**
            - **Thay đổi lối sống:** Quan trọng nhất!
              - Tăng chất xơ, uống nhiều nước
              - Tránh rặn, ngồi lâu
              - Tập thể dục đều đặn
            - **Thuốc:**
              - **Bôi tại chỗ:** Kem, mỡ chứa hydrocortisone, lidocaine (giảm đau, ngứa)
              - **Đặt hậu môn:** Viên đạn chứa thuốc
              - **Thuốc uống:** Daflon, Rutin (tăng sức bền mạch máu)

            **2. Thủ thuật (Trĩ độ 2-3):**
            - **Thắt búi trĩ:** Dùng vòng cao su thắt búi trĩ, búi trĩ teo và rụng
            - **Tiêm xơ:** Tiêm thuốc làm xơ hóa búi trĩ
            - **Quang đông hồng ngoại:** Dùng nhiệt làm teo búi trĩ
            - **Đông máu bằng laser:** Dùng laser đông máu

            **3. Phẫu thuật (Trĩ độ 3-4, không đáp ứng điều trị khác):**
            - **Cắt trĩ:** Cắt bỏ búi trĩ
            - **Khâu treo búi trĩ (PPH):** Khâu treo niêm mạc, giảm lưu lượng máu
            - **Cắt trĩ bằng sóng radio (RFA):** Dùng sóng radio cắt búi trĩ

            **⚠️ Lưu ý:**
            - Điều trị tùy theo độ trĩ, triệu chứng
            - Thay đổi lối sống là quan trọng nhất
            - Phẫu thuật chỉ khi cần thiết

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Tăng chất xơ (QUAN TRỌNG NHẤT!):**
            - **Rau xanh:** Rau muống, rau lang, rau cải, rau dền
            - **Trái cây:** Chuối, táo, lê, cam, bưởi
            - **Ngũ cốc nguyên hạt:** Gạo lứt, yến mạch, bánh mì đen
            - **Đậu:** Đậu xanh, đậu đỏ, đậu đen
            - **Mục tiêu:** 25-30g chất xơ/ngày

            **2. Uống nhiều nước:**
            - **Lượng nước:** 2-3 lít/ngày (8-12 cốc)
            - **Nước lọc:** Tốt nhất
            - **Nước trái cây:** Nước ép trái cây tươi
            - **Tránh:** Rượu bia, cà phê (có thể gây táo bón)

            **3. Thực phẩm nên ăn:**
            - Rau xanh, trái cây
            - Ngũ cốc nguyên hạt
            - Đậu, hạt
            - Sữa chua (probiotic)
            - Cá, thịt nạc

            **4. Thực phẩm nên tránh:**
            - **Đồ cay nóng:** Ớt, tiêu, gừng (kích thích hậu môn)
            - **Rượu bia:** Làm giãn mạch máu
            - **Đồ chiên rán:** Khó tiêu
            - **Thức ăn nhanh:** Ít chất xơ
            - **Thực phẩm chế biến:** Thịt nguội, xúc xích

            **5. Thực đơn mẫu 1 ngày:**
            - **Sáng:** Cháo yến mạch + chuối + sữa chua
            - **Trưa:** Cơm gạo lứt + canh rau muống + thịt/cá + rau xanh
            - **Chiều:** Cơm gạo lứt + canh rau cải + thịt/cá + rau xanh
            - **Bữa phụ:** Trái cây (táo, lê, cam)
            - **Uống:** 2-3 lít nước/ngày

            **6. Lưu ý:**
            - Ăn đều đặn, không bỏ bữa
            - Nhai kỹ, ăn chậm
            - Tăng chất xơ từ từ (tránh đầy hơi)

            ## 🏃 TẬP THỂ DỤC:

            **1. Tập thể dục đều đặn:**
            - **Đi bộ:** 30 phút/ngày, 5 ngày/tuần
            - **Bơi lội:** Tốt cho tuần hoàn
            - **Yoga:** Tư thế giúp giảm áp lực vùng chậu
            - **Tập Kegel:** Tăng cường cơ sàn chậu

            **2. Tránh:**
            - Ngồi lâu (đứng dậy mỗi 30-60 phút)
            - Đứng lâu
            - Khuân vác nặng
            - Tập quá sức

            **3. Tư thế đúng:**
            - Ngồi thẳng lưng
            - Không ngồi xổm lâu
            - Đi cầu đúng tư thế (chân kê cao)

            ## 💊 QUẢN LÝ THUỐC:

            **1. Thuốc bôi tại chỗ:**
            - **Kem, mỡ:** Bôi sau khi rửa sạch hậu môn
            - **Thành phần:** Hydrocortisone (giảm viêm), Lidocaine (giảm đau)
            - **Cách dùng:** Bôi 2-3 lần/ngày, sau khi đi cầu
            - **Lưu ý:** Không dùng quá 7 ngày (tránh teo da)

            **2. Viên đạn đặt hậu môn:**
            - **Thành phần:** Thuốc giảm đau, chống viêm
            - **Cách dùng:** Đặt vào hậu môn, tốt nhất trước khi ngủ
            - **Lưu ý:** Rửa tay trước và sau

            **3. Thuốc uống:**
            - **Daflon, Rutin:** Tăng sức bền mạch máu
            - **Uống đều đặn:** Theo chỉ định bác sĩ
            - **Thời gian:** 2-4 tuần

            **4. Lưu ý:**
            - Không tự ý dùng thuốc lâu dài
            - Báo bác sĩ nếu không cải thiện
            - Tránh thuốc nhuận tràng (có thể gây phụ thuộc)

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Chảy máu nhiều:**
            - Chảy máu thành tia, nhiều
            - Chảy máu kéo dài, không cầm
            - Thiếu máu (mệt mỏi, xanh xao, khó thở)

            **2. Nghẹt búi trĩ:**
            - Búi trĩ sa, không đẩy lên được
            - Sưng đau dữ dội
            - **Cấp cứu ngay!**

            **3. Tắc mạch:**
            - Đau dữ dội vùng hậu môn
            - Búi trĩ sưng, cứng
            - **Cấp cứu ngay!**

            **4. Triệu chứng nặng:**
            - Đau không chịu được
            - Sốt, ớn lạnh (nhiễm trùng)
            - Không đi cầu được

            **5. Không đáp ứng điều trị:**
            - Điều trị > 1 tuần không cải thiện
            - Tái phát nhiều lần

            ## 💡 PHÒNG NGỪA:

            **1. Chế độ ăn:**
            - **Tăng chất xơ:** 25-30g/ngày
            - **Uống nhiều nước:** 2-3 lít/ngày
            - **Tránh:** Đồ cay nóng, rượu bia

            **2. Thói quen đi cầu:**
            - **Đi cầu đều đặn:** Mỗi ngày, cùng giờ
            - **Không rặn:** Đi cầu tự nhiên, không gắng sức
            - **Không ngồi lâu:** < 5 phút
            - **Không đọc sách:** Khi đi cầu
            - **Vệ sinh sạch:** Rửa bằng nước, lau nhẹ

            **3. Tập thể dục:**
            - Đều đặn, 30 phút/ngày
            - Tránh ngồi lâu, đứng lâu

            **4. Tư thế:**
            - Ngồi thẳng lưng
            - Chân kê cao khi đi cầu (góc 35°)
            - Đứng dậy mỗi 30-60 phút nếu ngồi lâu

            **5. Tránh:**
            - Táo bón (quan trọng nhất!)
            - Tiêu chảy mạn tính
            - Khuân vác nặng
            - Mang thai (cần chăm sóc đặc biệt)

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Phòng ngừa:**
            - **Chế độ ăn giàu chất xơ** (quan trọng nhất!)
            - **Uống nhiều nước**
            - **Tập thể dục đều đặn**
            - **Thói quen đi cầu đúng**

            **2. Khi bị trĩ:**
            - Thay đổi lối sống ngay
            - Dùng thuốc theo chỉ định
            - Tránh rặn, ngồi lâu
            - Vệ sinh sạch sẽ

            **3. Sống tích cực:**
            - Trĩ rất phổ biến, không nguy hiểm
            - Điều trị đúng → Cải thiện triệu chứng
            - Phòng ngừa tốt → Không tái phát
            - Có thể sống bình thường

            **4. Tư vấn:**
            - Khám bác sĩ nếu triệu chứng nặng
            - Không tự ý dùng thuốc lâu dài
            - Theo dõi định kỳ nếu cần
            """,
            related_disease="hemorrhoids",
            related_drugs=["Hydrocortisone", "Lidocaine", "Daflon", "Rutin"],
            printable=True
        ),

        PatientEducationTopic(
            id="chronic_constipation_basics",
            title="Understanding Chronic Constipation",
            title_vn="Hiểu về Táo bón mạn tính",
            category="Disease",
            content="""
            # Hiểu về Táo bón mạn tính

            ## Táo bón mạn tính là gì?

            Táo bón mạn tính là tình trạng đi cầu khó khăn, ít hơn 3 lần/tuần, kéo dài > 3 tháng. Táo bón rất phổ biến, ảnh hưởng đến 15-20% dân số, đặc biệt phụ nữ và người cao tuổi.

            **⚠️ Đặc điểm:**
            - Đi cầu < 3 lần/tuần
            - Phân cứng, khó đi
            - Kéo dài > 3 tháng
            - Rất phổ biến (15-20% dân số)

            **Phân loại:**
            - **Táo bón chức năng:** Không có nguyên nhân rõ ràng (90%)
            - **Táo bón thứ phát:** Do bệnh khác, thuốc (10%)

            **Tiêu chuẩn chẩn đoán (Rome IV):**
            - Đi cầu < 3 lần/tuần
            - Phân cứng > 25% thời gian
            - Rặn > 25% thời gian
            - Cảm giác tắc nghẽn > 25% thời gian
            - Phải dùng tay hỗ trợ > 25% thời gian
            - Cảm giác đi không hết > 25% thời gian
            - Ít nhất 2 tiêu chuẩn, kéo dài > 3 tháng

            ## Triệu chứng:

            **Triệu chứng điển hình:**
            - **Đi cầu ít:** < 3 lần/tuần
            - **Phân cứng:** Phân khô, cứng, nhỏ
            - **Khó đi:** Phải rặn nhiều, lâu
            - **Cảm giác tắc nghẽn:** Cảm giác phân bị tắc
            - **Cảm giác đi không hết:** Sau khi đi cầu vẫn cảm thấy chưa hết
            - **Phải dùng tay hỗ trợ:** Phải đẩy vùng hậu môn, bụng

            **Triệu chứng khác:**
            - Đau bụng, đầy hơi
            - Chán ăn
            - Mệt mỏi
            - Đau đầu
            - Khó chịu, cáu gắt

            **⚠️ Dấu hiệu báo động (cần khám ngay):**
            - Sụt cân không rõ nguyên nhân
            - Chảy máu trực tràng
            - Thiếu máu
            - Tiền sử gia đình ung thư đại tràng
            - Tuổi > 50, táo bón mới xuất hiện

            ## Nguyên nhân:

            **1. Chế độ ăn:**
            - **Ít chất xơ:** Ăn ít rau, trái cây
            - **Uống ít nước:** < 1.5 lít/ngày
            - **Ăn nhiều thịt, đồ chế biến:** Ít chất xơ

            **2. Lối sống:**
            - **Ít vận động:** Ngồi nhiều, ít tập thể dục
            - **Nhịn đi cầu:** Không đi khi có nhu cầu
            - **Thay đổi thói quen:** Du lịch, thay đổi môi trường
            - **Stress:** Căng thẳng, lo âu

            **3. Thuốc:**
            - **Thuốc giảm đau:** Opioid (morphine, codeine)
            - **Thuốc kháng acid:** Chứa nhôm, canxi
            - **Thuốc chống trầm cảm:** Tricyclic, SSRI
            - **Thuốc hạ huyết áp:** Chẹn canxi
            - **Bổ sung sắt, canxi**
            - **Thuốc kháng cholinergic**

            **4. Bệnh khác:**
            - **Bệnh nội tiết:** Đái tháo đường, suy giáp, cường giáp
            - **Bệnh thần kinh:** Parkinson, đột quỵ, tổn thương tủy sống
            - **Bệnh ruột:** Hội chứng ruột kích thích, bệnh viêm ruột
            - **Bệnh chuyển hóa:** Tăng canxi máu, giảm kali máu

            **5. Yếu tố nguy cơ:**
            - **Tuổi:** Người cao tuổi (nhu động ruột chậm)
            - **Giới tính:** Phụ nữ (hormone, mang thai)
            - **Mang thai:** Tăng progesterone, tử cung chèn ép
            - **Sau phẫu thuật:** Phẫu thuật ổ bụng
            - **Nằm liệt giường**

            ## Chẩn đoán:

            **Chẩn đoán lâm sàng:**
            - Triệu chứng điển hình
            - Tiêu chuẩn Rome IV

            **Khám:**
            - **Khám bụng:** Sờ thấy phân cứng
            - **Thăm trực tràng:** Phân cứng, búi trĩ
            - **Đánh giá cơ thắt hậu môn**

            **Xét nghiệm:**
            - **Xét nghiệm máu:** Chức năng tuyến giáp, canxi, đường huyết
            - **Chụp X-quang bụng:** Phân ứ đọng
            - **Đo thời gian vận chuyển ruột:** Đánh dấu phóng xạ
            - **Đo áp lực hậu môn-trực tràng:** Đánh giá chức năng

            **Soi đại tràng:**
            - Nếu có dấu hiệu báo động
            - Tuổi > 50, táo bón mới xuất hiện

            ## Điều trị:

            **1. Thay đổi lối sống (QUAN TRỌNG NHẤT!):**
            - **Tăng chất xơ:** 25-30g/ngày
            - **Uống nhiều nước:** 2-3 lít/ngày
            - **Tập thể dục:** 30 phút/ngày
            - **Thói quen đi cầu:** Đi đều đặn, cùng giờ

            **2. Thuốc nhuận tràng:**
            - **Chất xơ (Psyllium, Methylcellulose):** Tăng khối lượng phân
            - **Osmotic (Lactulose, Polyethylene glycol):** Giữ nước trong ruột
            - **Kích thích (Bisacodyl, Senna):** Kích thích nhu động ruột (dùng ngắn hạn)
            - **Làm mềm phân (Docusate):** Làm mềm phân

            **3. Thuốc khác:**
            - **Lubiprostone:** Tăng tiết dịch ruột
            - **Linaclotide, Plecanatide:** Kích thích nhu động ruột
            - **Prucalopride:** Kích thích thụ thể serotonin

            **4. Điều trị nguyên nhân:**
            - Điều trị bệnh nền (đái tháo đường, suy giáp)
            - Thay đổi thuốc (nếu có thể)

            **5. Vật lý trị liệu:**
            - Tập cơ sàn chậu
            - Biofeedback (phản hồi sinh học)

            **⚠️ Lưu ý:**
            - Bắt đầu với thay đổi lối sống
            - Thuốc nhuận tràng chỉ hỗ trợ
            - Tránh lạm dụng thuốc kích thích

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Tăng chất xơ (QUAN TRỌNG NHẤT!):**
            - **Rau xanh:** Rau muống, rau lang, rau cải, rau dền, rau mồng tơi
            - **Trái cây:** Chuối, táo, lê, cam, bưởi, đu đủ, thanh long
            - **Ngũ cốc nguyên hạt:** Gạo lứt, yến mạch, bánh mì đen
            - **Đậu:** Đậu xanh, đậu đỏ, đậu đen, đậu nành
            - **Hạt:** Hạt chia, hạt lanh
            - **Mục tiêu:** 25-30g chất xơ/ngày

            **2. Uống nhiều nước:**
            - **Lượng nước:** 2-3 lít/ngày (8-12 cốc)
            - **Nước lọc:** Tốt nhất
            - **Nước trái cây:** Nước ép trái cây tươi (đu đủ, thanh long)
            - **Tránh:** Rượu bia, cà phê (có thể gây mất nước)

            **3. Thực phẩm nên ăn:**
            - Rau xanh, trái cây
            - Ngũ cốc nguyên hạt
            - Đậu, hạt
            - Sữa chua (probiotic)
            - Cá, thịt nạc
            - Dầu thực vật (dầu oliu, dầu dừa)

            **4. Thực phẩm nên tránh:**
            - **Thức ăn chế biến:** Thịt nguội, xúc xích, đồ hộp
            - **Thức ăn nhanh:** Hamburger, pizza
            - **Đồ chiên rán:** Khó tiêu
            - **Sữa (nếu không dung nạp):** Có thể gây táo bón
            - **Thức ăn ít chất xơ:** Bánh mì trắng, gạo trắng

            **5. Thực đơn mẫu 1 ngày:**
            - **Sáng:** Cháo yến mạch + chuối + sữa chua + hạt chia
            - **Trưa:** Cơm gạo lứt + canh rau muống + thịt/cá + rau xanh + đu đủ
            - **Chiều:** Cơm gạo lứt + canh rau cải + thịt/cá + rau xanh + thanh long
            - **Bữa phụ:** Trái cây (táo, lê, cam), sữa chua
            - **Uống:** 2-3 lít nước/ngày

            **6. Lưu ý:**
            - Tăng chất xơ từ từ (tránh đầy hơi)
            - Uống nhiều nước khi tăng chất xơ
            - Ăn đều đặn, không bỏ bữa
            - Nhai kỹ, ăn chậm

            ## 🏃 TẬP THỂ DỤC:

            **1. Tập thể dục đều đặn:**
            - **Đi bộ:** 30 phút/ngày, 5 ngày/tuần (kích thích nhu động ruột)
            - **Chạy bộ:** 20-30 phút/ngày
            - **Bơi lội:** Tốt cho tuần hoàn
            - **Yoga:** Tư thế xoắn, gập người (kích thích ruột)
            - **Tập bụng:** Tăng cường cơ bụng

            **2. Tập cơ sàn chậu:**
            - Tập Kegel (co thắt cơ sàn chậu)
            - 10-15 lần, 3 lần/ngày

            **3. Massage bụng:**
            - Massage bụng theo chiều kim đồng hồ
            - 5-10 phút, 2 lần/ngày

            **4. Tránh:**
            - Ngồi lâu, ít vận động
            - Tập quá sức

            ## 💊 QUẢN LÝ THUỐC:

            **1. Thuốc nhuận tràng chất xơ:**
            - **Psyllium, Methylcellulose:** 1-2 muỗng/ngày, uống với nhiều nước
            - **Uống trước bữa ăn:** 30 phút
            - **Tăng dần liều:** Từ 1 muỗng → 2 muỗng
            - **Lưu ý:** Uống nhiều nước (quan trọng!)

            **2. Thuốc nhuận tràng thẩm thấu:**
            - **Lactulose:** 15-30ml/ngày
            - **Polyethylene glycol:** 1-2 gói/ngày
            - **Uống với nhiều nước**
            - **Tác dụng phụ:** Đầy hơi, chướng bụng

            **3. Thuốc nhuận tràng kích thích:**
            - **Bisacodyl, Senna:** Dùng ngắn hạn (3-7 ngày)
            - **Tránh dùng lâu dài:** Có thể gây phụ thuộc
            - **Dùng khi cần:** Táo bón nặng, cấp tính

            **4. Lưu ý:**
            - Bắt đầu với thay đổi lối sống
            - Thuốc chỉ hỗ trợ
            - Không lạm dụng thuốc kích thích
            - Báo bác sĩ nếu không cải thiện

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Dấu hiệu báo động:**
            - Sụt cân không rõ nguyên nhân
            - Chảy máu trực tràng
            - Thiếu máu
            - Tuổi > 50, táo bón mới xuất hiện

            **2. Táo bón nặng:**
            - Không đi cầu > 7 ngày
            - Đau bụng dữ dội
            - Nôn, buồn nôn
            - Sốt

            **3. Phân cứng gây tắc:**
            - Không đi cầu được
            - Đau bụng, chướng bụng
            - Cần thụt tháo, lấy phân

            **4. Biến chứng:**
            - Trĩ (do rặn nhiều)
            - Nứt hậu môn
            - Sa trực tràng

            **5. Không đáp ứng điều trị:**
            - Điều trị > 1 tháng không cải thiện
            - Cần đánh giá thêm

            ## 💡 PHÒNG NGỪA:

            **1. Chế độ ăn:**
            - **Tăng chất xơ:** 25-30g/ngày
            - **Uống nhiều nước:** 2-3 lít/ngày
            - **Ăn đều đặn:** Không bỏ bữa

            **2. Tập thể dục:**
            - Đều đặn, 30 phút/ngày
            - Kích thích nhu động ruột

            **3. Thói quen đi cầu:**
            - **Đi đều đặn:** Mỗi ngày, cùng giờ (sau bữa sáng)
            - **Không nhịn:** Đi ngay khi có nhu cầu
            - **Không rặn:** Đi cầu tự nhiên
            - **Tư thế đúng:** Chân kê cao (góc 35°)

            **4. Tránh:**
            - Thuốc gây táo bón (nếu có thể)
            - Stress, căng thẳng
            - Thay đổi thói quen đột ngột

            **5. Khám định kỳ:**
            - Khám nếu táo bón kéo dài
            - Điều trị bệnh nền (nếu có)

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Phòng ngừa:**
            - **Chế độ ăn giàu chất xơ** (quan trọng nhất!)
            - **Uống nhiều nước**
            - **Tập thể dục đều đặn**
            - **Thói quen đi cầu đúng**

            **2. Khi bị táo bón:**
            - Thay đổi lối sống ngay
            - Tăng chất xơ từ từ
            - Uống nhiều nước
            - Dùng thuốc nhuận tràng (nếu cần)

            **3. Sống tích cực:**
            - Táo bón rất phổ biến
            - Điều trị đúng → Cải thiện
            - Phòng ngừa tốt → Không tái phát
            - Có thể sống bình thường

            **4. Kiên nhẫn:**
            - Điều trị cần thời gian (2-4 tuần)
            - Không nản lòng
            - Kết hợp nhiều biện pháp
            """,
            related_disease="chronic_constipation",
            related_drugs=["Psyllium", "Lactulose", "Polyethylene glycol", "Bisacodyl", "Senna", "Linaclotide"],
            printable=True
        ),

        PatientEducationTopic(
            id="appendicitis_basics",
            title="Understanding Appendicitis",
            title_vn="Hiểu về Viêm ruột thừa",
            category="Disease",
            content="""
            # Hiểu về Viêm ruột thừa

            ## Viêm ruột thừa là gì?

            Viêm ruột thừa (Appendicitis) là tình trạng viêm cấp tính của ruột thừa, một cơ quan nhỏ ở đầu manh tràng. Đây là cấp cứu ngoại khoa phổ biến nhất, cần phẫu thuật ngay để tránh biến chứng nguy hiểm.

            **⚠️ Đặc điểm:**
            - Viêm cấp tính ruột thừa
            - Cấp cứu ngoại khoa phổ biến nhất
            - Cần phẫu thuật ngay
            - Có thể vỡ → Viêm phúc mạc → Nguy hiểm tính mạng

            **Ruột thừa:**
            - Cơ quan nhỏ, hình ống, dài 5-10cm
            - Ở đầu manh tràng (góc hồi-manh tràng)
            - Chức năng: Chưa rõ (có thể miễn dịch)

            **Phân loại:**
            - **Viêm ruột thừa cấp:** Viêm cấp tính, cần phẫu thuật ngay
            - **Viêm ruột thừa mạn:** Viêm tái phát, ít gặp

            ## Triệu chứng:

            **Triệu chứng điển hình:**
            - **Đau bụng:**
              - Bắt đầu quanh rốn, sau đó di chuyển xuống hố chậu phải
              - Đau liên tục, tăng dần
              - Đau tăng khi ho, hắt hơi, di chuyển
            - **Sốt:** Sốt nhẹ đến vừa (37.5-38.5°C)
            - **Buồn nôn, nôn:** Thường có
            - **Chán ăn:** Chán ăn, không muốn ăn
            - **Rối loạn tiêu hóa:** Có thể táo bón hoặc tiêu chảy

            **Triệu chứng khác:**
            - Đau tăng khi ấn hố chậu phải
            - Phản ứng thành bụng (co cứng)
            - Dấu hiệu Blumberg (đau tăng khi thả tay)

            **⚠️ Triệu chứng khi vỡ:**
            - Đau bụng dữ dội, lan toàn bụng
            - Sốt cao
            - Mạch nhanh
            - Tụt huyết áp
            - **Cấp cứu ngay!**

            **⚠️ Lưu ý:**
            - Trẻ em, người cao tuổi có thể không có triệu chứng điển hình
            - Phụ nữ mang thai: Đau có thể ở vị trí khác

            ## Nguyên nhân:

            **1. Tắc nghẽn lòng ruột thừa:**
            - **Phân cứng (Fecalith):** Phân cứng tắc lòng ruột thừa (phổ biến nhất)
            - **Sỏi phân:** Sỏi phân
            - **Phì đại nang bạch huyết:** Nang bạch huyết phì đại
            - **Khối u:** Khối u ruột thừa, manh tràng
            - **Ký sinh trùng:** Giun đũa, giun kim

            **2. Nhiễm trùng:**
            - **Vi khuẩn:** E. coli, Bacteroides, Streptococcus
            - Nhiễm trùng từ đường tiêu hóa

            **3. Yếu tố nguy cơ:**
            - **Tuổi:** 10-30 tuổi (phổ biến nhất)
            - **Giới tính:** Nam > Nữ (nhẹ)
            - **Tiền sử gia đình:** Có người thân bị viêm ruột thừa
            - **Chế độ ăn:** Ít chất xơ (có thể)

            ## Chẩn đoán:

            **Chẩn đoán lâm sàng:**
            - Triệu chứng điển hình
            - Khám bụng

            **Khám:**
            - **Đau hố chậu phải:** Đau khi ấn
            - **Phản ứng thành bụng:** Co cứng thành bụng
            - **Dấu hiệu Blumberg:** Đau tăng khi thả tay
            - **Dấu hiệu Rovsing:** Đau hố chậu phải khi ấn hố chậu trái

            **Xét nghiệm:**
            - **Xét nghiệm máu:**
              - Bạch cầu tăng (10-20.000/μL)
              - CRP tăng (dấu hiệu viêm)
            - **Siêu âm bụng:** Phát hiện ruột thừa viêm, dày thành
            - **CT bụng:** Chẩn đoán chính xác (95-98%)
            - **X-quang bụng:** Ít dùng, có thể thấy sỏi phân

            **⚠️ Phân biệt:**
            - Viêm dạ dày-ruột
            - Viêm túi thừa
            - Sỏi thận
            - Viêm vùng chậu (phụ nữ)
            - Thai ngoài tử cung (phụ nữ)

            ## Điều trị:

            **1. Phẫu thuật (Điều trị chính):**
            - **Cắt ruột thừa (Appendectomy):**
              - **Mổ mở:** Mổ mở bụng (truyền thống)
              - **Mổ nội soi:** Mổ nội soi (ưu tiên, ít xâm lấn)
            - **Thời gian:** Càng sớm càng tốt (trong 24-48 giờ)
            - **Trước phẫu thuật:** Kháng sinh đường tĩnh mạch

            **2. Kháng sinh:**
            - **Trước phẫu thuật:** Kháng sinh phổ rộng (Cefazolin, Metronidazole)
            - **Sau phẫu thuật:** Tiếp tục 24-48 giờ
            - **Nếu vỡ:** Kháng sinh 5-7 ngày

            **3. Điều trị không phẫu thuật (Hiếm, chỉ khi chống chỉ định phẫu thuật):**
            - Kháng sinh đường tĩnh mạch
            - Theo dõi sát
            - Có thể tái phát

            **⚠️ Lưu ý:**
            - Phẫu thuật là điều trị chính
            - Không được trì hoãn (nguy cơ vỡ)
            - Vỡ ruột thừa → Viêm phúc mạc → Nguy hiểm tính mạng

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Trước phẫu thuật:**
            - **Nhịn ăn:** Nhịn ăn, uống (chuẩn bị phẫu thuật)
            - **Truyền dịch:** Truyền dịch đường tĩnh mạch

            **2. Sau phẫu thuật:**
            - **Ngày 1:** Uống nước, nước đường (nếu không nôn)
            - **Ngày 2-3:** Ăn lỏng (cháo, súp)
            - **Ngày 4-5:** Ăn mềm (cơm mềm, thịt/cá nấu chín)
            - **Sau 1 tuần:** Ăn bình thường

            **3. Thực phẩm nên ăn:**
            - Cháo, súp (sau phẫu thuật)
            - Thức ăn mềm, dễ tiêu
            - Rau xanh, trái cây (khi đã ổn)
            - Uống nhiều nước

            **4. Thực phẩm nên tránh:**
            - Đồ cay nóng (sau phẫu thuật)
            - Đồ chiên rán (khó tiêu)
            - Thức ăn cứng

            **5. Lưu ý:**
            - Ăn từ từ, tăng dần
            - Theo chỉ định bác sĩ
            - Báo nếu đau bụng, nôn

            ## 🏃 TẬP THỂ DỤC:

            **1. Sau phẫu thuật:**
            - **Ngày 1:** Nghỉ ngơi tại giường, đi lại nhẹ
            - **Ngày 2-3:** Đi lại trong phòng
            - **Ngày 4-5:** Đi lại bình thường
            - **Sau 1 tuần:** Tập thể dục nhẹ
            - **Sau 2-4 tuần:** Tập thể dục bình thường

            **2. Tránh:**
            - Gắng sức trong 2-4 tuần đầu
            - Khuân vác nặng
            - Tập thể dục mạnh

            **3. Lưu ý:**
            - Theo chỉ định bác sĩ
            - Báo nếu đau, khó chịu

            ## 💊 QUẢN LÝ THUỐC:

            **1. Kháng sinh:**
            - **Trước phẫu thuật:** Kháng sinh đường tĩnh mạch
            - **Sau phẫu thuật:** Tiếp tục 24-48 giờ
            - **Nếu vỡ:** Kháng sinh 5-7 ngày

            **2. Thuốc giảm đau:**
            - **Paracetamol:** 500-1000mg, 3-4 lần/ngày
            - **NSAID:** Ibuprofen (nếu không chống chỉ định)
            - **Opioid:** Morphine (nếu đau nặng, ngắn hạn)

            **3. Lưu ý:**
            - Uống đúng liều, đúng giờ
            - Báo bác sĩ nếu đau không giảm
            - Không tự ý ngừng kháng sinh

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Triệu chứng viêm ruột thừa:**
            - Đau bụng quanh rốn → Hố chậu phải
            - Sốt, buồn nôn, nôn
            - **Đến bệnh viện ngay!**

            **2. Đau bụng dữ dội:**
            - Đau bụng dữ dội, lan toàn bụng
            - Sốt cao
            - **Cấp cứu ngay!** (Có thể vỡ)

            **3. Sau phẫu thuật:**
            - Sốt cao
            - Đau bụng tăng
            - Vết mổ sưng, đỏ, chảy mủ
            - Nôn, không đi cầu được

            **4. Biến chứng:**
            - Viêm phúc mạc
            - Áp xe ổ bụng
            - Tắc ruột

            ## 💡 PHÒNG NGỪA:

            **1. Không có cách phòng ngừa chắc chắn:**
            - Nguyên nhân chưa rõ hoàn toàn

            **2. Có thể giảm nguy cơ:**
            - **Chế độ ăn giàu chất xơ:** Có thể giảm nguy cơ
            - **Uống nhiều nước:** Tránh táo bón
            - **Tập thể dục:** Tăng nhu động ruột

            **3. Phát hiện sớm:**
            - Nhận biết triệu chứng
            - Đến bệnh viện ngay khi có triệu chứng
            - Không tự ý dùng thuốc giảm đau (che dấu triệu chứng)

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Nhận biết triệu chứng:**
            - Đau bụng quanh rốn → Hố chậu phải
            - Sốt, buồn nôn, nôn
            - **Đến bệnh viện ngay!**

            **2. Không trì hoãn:**
            - Viêm ruột thừa cần phẫu thuật ngay
            - Trì hoãn → Vỡ → Nguy hiểm tính mạng
            - Không tự ý dùng thuốc giảm đau

            **3. Sau phẫu thuật:**
            - Nghỉ ngơi, ăn uống theo chỉ định
            - Theo dõi vết mổ
            - Báo bác sĩ nếu có bất thường

            **4. Sống tích cực:**
            - Phẫu thuật cắt ruột thừa an toàn
            - Hồi phục nhanh (1-2 tuần)
            - Không ảnh hưởng chức năng tiêu hóa
            """,
            related_disease="appendicitis",
            related_drugs=["Cefazolin", "Metronidazole", "Paracetamol", "Ibuprofen"],
            printable=True
        ),

        PatientEducationTopic(
            id="gallstones_basics",
            title="Understanding Gallstones",
            title_vn="Hiểu về Sỏi mật",
            category="Disease",
            content="""
            # Hiểu về Sỏi mật

            ## Sỏi mật là gì?

            Sỏi mật (Gallstones) là những viên sỏi hình thành trong túi mật hoặc ống mật, do kết tinh của các thành phần trong dịch mật. Sỏi mật rất phổ biến, ảnh hưởng đến 10-15% dân số, đặc biệt phụ nữ, người cao tuổi.

            **⚠️ Đặc điểm:**
            - Sỏi hình thành trong túi mật hoặc ống mật
            - Rất phổ biến (10-15% dân số)
            - Nhiều người không có triệu chứng
            - Có thể gây viêm túi mật, tắc ống mật

            **Phân loại:**
            - **Sỏi cholesterol:** Sỏi cholesterol (80% ở phương Tây)
            - **Sỏi sắc tố:** Sỏi bilirubin (phổ biến ở châu Á)
            - **Sỏi hỗn hợp:** Cả cholesterol và sắc tố

            **Vị trí:**
            - **Túi mật:** Phổ biến nhất
            - **Ống mật chủ:** Tắc ống mật
            - **Ống gan:** Tắc ống gan

            ## Triệu chứng:

            **1. Không có triệu chứng (80%):**
            - Phát hiện tình cờ khi siêu âm
            - Không cần điều trị

            **2. Cơn đau quặn mật (Biliary Colic):**
            - **Đau bụng:** Đau vùng hạ sườn phải, lan ra sau lưng, vai phải
            - **Đặc điểm:** Đau quặn, dữ dội, đau từng cơn
            - **Thời gian:** 30 phút đến vài giờ
            - **Kích thích:** Sau ăn nhiều chất béo
            - **Triệu chứng khác:** Buồn nôn, nôn, đầy bụng

            **3. Viêm túi mật cấp:**
            - **Đau bụng:** Đau vùng hạ sườn phải, liên tục, tăng dần
            - **Sốt:** Sốt 38-39°C
            - **Buồn nôn, nôn**
            - **Đau tăng:** Khi ấn vùng hạ sườn phải
            - **Dấu hiệu Murphy:** Đau khi ấn vùng túi mật, hít sâu

            **4. Tắc ống mật:**
            - **Vàng da:** Vàng da, vàng mắt
            - **Phân bạc màu:** Phân màu trắng, xám
            - **Nước tiểu sẫm:** Nước tiểu màu vàng đậm
            - **Sốt, ớn lạnh:** Nhiễm trùng đường mật
            - **Đau bụng:** Đau vùng hạ sườn phải

            **5. Viêm tụy cấp:**
            - Đau bụng trên, lan ra sau lưng
            - Buồn nôn, nôn
            - Sốt

            **⚠️ Biến chứng:**
            - Viêm túi mật cấp
            - Tắc ống mật
            - Viêm tụy cấp
            - Viêm phúc mạc mật (hiếm, nguy hiểm)

            ## Nguyên nhân:

            **1. Sỏi cholesterol:**
            - **Dịch mật bão hòa cholesterol:** Quá nhiều cholesterol trong dịch mật
            - **Giảm muối mật:** Giảm muối mật (không đủ để hòa tan cholesterol)
            - **Ứ đọng dịch mật:** Túi mật không co bóp tốt

            **2. Sỏi sắc tố:**
            - **Tăng bilirubin:** Tăng bilirubin trong dịch mật
            - **Nhiễm trùng:** Nhiễm trùng đường mật
            - **Thiếu máu tan máu:** Tan máu → Tăng bilirubin

            **3. Yếu tố nguy cơ:**
            - **Tuổi:** > 40 tuổi
            - **Giới tính:** Phụ nữ (gấp 2-3 lần nam)
            - **Mang thai:** Tăng nguy cơ
            - **Béo phì:** Tăng cholesterol
            - **Giảm cân nhanh:** Giảm cân > 1.5kg/tuần
            - **Chế độ ăn:** Ăn nhiều chất béo, ít chất xơ
            - **Di truyền:** Có người thân bị sỏi mật
            - **Bệnh khác:** Đái tháo đường, xơ gan, bệnh Crohn

            **4. Yếu tố bảo vệ:**
            - **Cà phê:** Uống cà phê (giảm nguy cơ)
            - **Chế độ ăn giàu chất xơ:** Giảm nguy cơ

            ## Chẩn đoán:

            **Chẩn đoán lâm sàng:**
            - Triệu chứng điển hình
            - Khám bụng

            **Xét nghiệm:**
            - **Siêu âm bụng:** Phát hiện sỏi mật (độ nhạy 95%)
            - **Xét nghiệm máu:**
              - Bilirubin tăng (nếu tắc ống mật)
              - Men gan tăng (ALT, AST)
              - Bạch cầu tăng (nếu viêm)
            - **CT bụng:** Đánh giá biến chứng
            - **MRCP:** Đánh giá ống mật (nếu cần)

            **⚠️ Phân biệt:**
            - Viêm dạ dày
            - Loét dạ dày-tá tràng
            - Viêm tụy
            - Sỏi thận

            ## Điều trị:

            **1. Sỏi mật không có triệu chứng:**
            - **Theo dõi:** Không cần điều trị
            - **Chỉ điều trị nếu:**
              - Sỏi lớn (> 2cm) → Nguy cơ ung thư túi mật
              - Túi mật vôi hóa → Nguy cơ ung thư
              - Bệnh nhân đái tháo đường → Nguy cơ biến chứng

            **2. Cơn đau quặn mật:**
            - **Thuốc giảm đau:** NSAID (Ibuprofen, Diclofenac)
            - **Thuốc giãn cơ:** Hyoscine
            - **Theo dõi:** Nếu tái phát → Cân nhắc phẫu thuật

            **3. Viêm túi mật cấp:**
            - **Kháng sinh:** Kháng sinh đường tĩnh mạch
            - **Phẫu thuật:** Cắt túi mật (trong 24-72 giờ)
            - **Nếu không phẫu thuật:** Cắt túi mật sau khi ổn định

            **4. Phẫu thuật:**
            - **Cắt túi mật:**
              - **Mổ nội soi:** Ưu tiên (ít xâm lấn, hồi phục nhanh)
              - **Mổ mở:** Nếu mổ nội soi không được
            - **Lấy sỏi ống mật:** Nội soi mật-tụy ngược dòng (ERCP)

            **5. Điều trị không phẫu thuật (Hiếm dùng):**
            - **Tán sỏi bằng sóng:** Tán sỏi bằng sóng siêu âm
            - **Hòa tan sỏi:** Ursodeoxycholic acid (chỉ sỏi cholesterol nhỏ)
            - **Hiệu quả thấp, tái phát cao**

            **⚠️ Lưu ý:**
            - Phẫu thuật là điều trị chính
            - Cắt túi mật không ảnh hưởng chức năng tiêu hóa (mật vẫn tiết từ gan)

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Khi có sỏi mật:**
            - **Giảm chất béo:** Giảm chất béo bão hòa, cholesterol
            - **Tăng chất xơ:** Rau xanh, trái cây
            - **Tránh:** Đồ chiên rán, thức ăn nhiều chất béo
            - **Ăn nhiều bữa nhỏ:** Thay vì 3 bữa lớn

            **2. Thực phẩm nên ăn:**
            - Rau xanh, trái cây
            - Ngũ cốc nguyên hạt
            - Protein nạc (thịt, cá, đậu)
            - Cá béo (Omega-3)
            - Dầu thực vật (dầu oliu, dầu hướng dương)

            **3. Thực phẩm nên tránh:**
            - **Đồ chiên rán:** Gà rán, khoai tây chiên
            - **Thức ăn nhiều chất béo:** Thịt mỡ, nội tạng
            - **Thức ăn nhanh:** Hamburger, pizza
            - **Rượu bia:** Có thể kích thích túi mật

            **4. Thực đơn mẫu:**
            - **Sáng:** Cháo yến mạch + trái cây
            - **Trưa:** Cơm + canh rau + cá/thịt nạc + rau xanh
            - **Chiều:** Cơm + canh rau + cá/thịt nạc + rau xanh
            - **Bữa phụ:** Trái cây, hạt

            **5. Lưu ý:**
            - Ăn nhiều bữa nhỏ (giảm kích thích túi mật)
            - Tránh ăn quá no
            - Uống nhiều nước

            ## 🏃 TẬP THỂ DỤC:

            **1. Tập thể dục:**
            - Bình thường, đều đặn
            - Giảm cân (nếu béo phì) → Giảm nguy cơ

            **2. Sau phẫu thuật:**
            - Nghỉ ngơi 1-2 tuần
            - Tập thể dục nhẹ sau 2 tuần
            - Tập thể dục bình thường sau 4-6 tuần

            **3. Lưu ý:**
            - Tránh gắng sức sau phẫu thuật
            - Theo chỉ định bác sĩ

            ## 💊 QUẢN LÝ THUỐC:

            **1. Thuốc giảm đau:**
            - **NSAID:** Ibuprofen, Diclofenac (cơn đau quặn mật)
            - **Opioid:** Morphine (nếu đau nặng, ngắn hạn)

            **2. Kháng sinh:**
            - **Viêm túi mật:** Kháng sinh đường tĩnh mạch
            - **Nhiễm trùng đường mật:** Kháng sinh phổ rộng

            **3. Thuốc giãn cơ:**
            - **Hyoscine:** Giảm co thắt túi mật

            **4. Lưu ý:**
            - Uống đúng liều, đúng giờ
            - Báo bác sĩ nếu đau không giảm
            - Không tự ý ngừng kháng sinh

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Cơn đau quặn mật:**
            - Đau bụng dữ dội vùng hạ sườn phải
            - Không giảm sau 1-2 giờ
            - **Đến bệnh viện ngay!**

            **2. Viêm túi mật cấp:**
            - Đau bụng + Sốt
            - **Cấp cứu ngay!**

            **3. Tắc ống mật:**
            - Vàng da, vàng mắt
            - Sốt, ớn lạnh
            - **Cấp cứu ngay!**

            **4. Sau phẫu thuật:**
            - Sốt cao
            - Đau bụng tăng
            - Vết mổ sưng, đỏ, chảy mủ
            - Vàng da

            ## 💡 PHÒNG NGỪA:

            **1. Chế độ ăn:**
            - **Giảm chất béo:** Giảm chất béo bão hòa, cholesterol
            - **Tăng chất xơ:** Rau xanh, trái cây
            - **Uống cà phê:** Có thể giảm nguy cơ

            **2. Duy trì cân nặng:**
            - Duy trì cân nặng hợp lý
            - Tránh béo phì
            - Giảm cân từ từ (không quá 1.5kg/tuần)

            **3. Tập thể dục:**
            - Đều đặn, 30 phút/ngày
            - Giảm nguy cơ

            **4. Tránh:**
            - Giảm cân quá nhanh
            - Ăn nhiều chất béo
            - Bỏ bữa

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Phòng ngừa:**
            - **Chế độ ăn lành mạnh** (quan trọng nhất!)
            - **Duy trì cân nặng hợp lý**
            - **Tập thể dục đều đặn**

            **2. Khi có sỏi mật:**
            - Nếu không có triệu chứng → Theo dõi
            - Nếu có triệu chứng → Cân nhắc phẫu thuật
            - Tránh ăn nhiều chất béo

            **3. Sống tích cực:**
            - Sỏi mật rất phổ biến
            - Nhiều người không có triệu chứng
            - Phẫu thuật an toàn, hiệu quả
            - Cắt túi mật không ảnh hưởng chức năng tiêu hóa

            **4. Sau phẫu thuật:**
            - Hồi phục nhanh (1-2 tuần)
            - Có thể sống bình thường
            - Ăn uống bình thường (có thể giảm chất béo ban đầu)
            """,
            related_disease="gallstones",
            related_drugs=["Ibuprofen", "Diclofenac", "Hyoscine", "Ursodeoxycholic acid"],
            printable=True
        ),

        PatientEducationTopic(
            id="pancreatitis_basics",
            title="Understanding Pancreatitis",
            title_vn="Hiểu về Viêm tụy",
            category="Disease",
            content="""
            # Hiểu về Viêm tụy

            ## Viêm tụy là gì?

            Viêm tụy (Pancreatitis) là tình trạng viêm của tuyến tụy, gây đau bụng dữ dội, có thể dẫn đến biến chứng nặng. Viêm tụy có thể cấp tính (đột ngột) hoặc mạn tính (kéo dài, tái phát).

            **⚠️ Đặc điểm:**
            - Viêm tuyến tụy
            - Đau bụng dữ dội
            - Có thể cấp tính hoặc mạn tính
            - Có thể dẫn đến biến chứng nặng

            **Phân loại:**
            - **Viêm tụy cấp:** Viêm đột ngột, thường tự khỏi
            - **Viêm tụy mạn:** Viêm kéo dài, tái phát, tổn thương vĩnh viễn

            **Tuyến tụy:**
            - Tuyến nằm sau dạ dày
            - Chức năng: Tiết enzyme tiêu hóa, insulin

            ## Triệu chứng:

            **Viêm tụy cấp:**
            - **Đau bụng:** Đau bụng trên, lan ra sau lưng, đau dữ dội, liên tục
            - **Buồn nôn, nôn:** Nôn nhiều, không giảm đau
            - **Sốt:** Sốt nhẹ đến vừa
            - **Đầy bụng, chướng bụng**
            - **Đau tăng:** Khi nằm ngửa, giảm khi ngồi, cúi người

            **Viêm tụy mạn:**
            - **Đau bụng:** Đau bụng trên, tái phát, có thể mạn tính
            - **Sụt cân:** Sụt cân do kém hấp thu
            - **Tiêu chảy mỡ:** Phân mỡ, nổi trên nước (kém hấp thu chất béo)
            - **Đái tháo đường:** Do tổn thương tế bào beta (tiết insulin)

            **⚠️ Biến chứng viêm tụy cấp:**
            - **Hoại tử tụy:** Tụy bị hoại tử
            - **Áp xe tụy:** Áp xe trong tụy
            - **Giả nang tụy:** Nang giả sau viêm
            - **Suy đa tạng:** Suy thận, phổi, tim
            - **Tử vong:** 5-10% (nếu nặng)

            ## Nguyên nhân:

            **Viêm tụy cấp:**
            - **Sỏi mật (40%):** Sỏi mật tắc ống tụy
            - **Rượu bia (30%):** Uống nhiều rượu bia
            - **Nguyên nhân khác (30%):**
              - Tăng triglyceride máu
              - Thuốc (Azathioprine, Thiazide, Furosemide)
              - Nhiễm trùng (virus, vi khuẩn)
              - Chấn thương
              - Sau ERCP
              - Tự phát (không rõ nguyên nhân)

            **Viêm tụy mạn:**
            - **Rượu bia (70%):** Uống nhiều rượu bia lâu dài
            - **Sỏi mật:** Tái phát nhiều lần
            - **Tăng canxi máu:** Tăng canxi máu
            - **Tự miễn:** Viêm tụy tự miễn
            - **Di truyền:** Đột biến gen (hiếm)

            **Yếu tố nguy cơ:**
            - Uống nhiều rượu bia
            - Sỏi mật
            - Tăng triglyceride máu
            - Béo phì
            - Đái tháo đường

            ## Chẩn đoán:

            **Chẩn đoán lâm sàng:**
            - Triệu chứng điển hình
            - Khám bụng

            **Xét nghiệm:**
            - **Amylase máu:** Tăng > 3 lần bình thường (độ nhạy 85%)
            - **Lipase máu:** Tăng > 3 lần bình thường (độ nhạy 95%, đặc hiệu hơn)
            - **Xét nghiệm máu khác:**
              - Bạch cầu tăng
              - Glucose tăng
              - Canxi giảm (nếu nặng)
              - Bilirubin tăng (nếu tắc ống mật)

            **Hình ảnh:**
            - **CT bụng:** Đánh giá mức độ, biến chứng (tiêu chuẩn vàng)
            - **Siêu âm bụng:** Phát hiện sỏi mật, dịch ổ bụng
            - **MRI/MRCP:** Đánh giá ống tụy, ống mật

            **⚠️ Phân biệt:**
            - Loét dạ dày-tá tràng thủng
            - Viêm túi mật cấp
            - Tắc ruột
            - Nhồi máu cơ tim

            ## Điều trị:

            **Viêm tụy cấp:**

            **1. Điều trị hỗ trợ:**
            - **Nhịn ăn:** Nhịn ăn, uống (giảm kích thích tụy)
            - **Truyền dịch:** Truyền dịch đường tĩnh mạch (quan trọng!)
            - **Giảm đau:** Morphine, Fentanyl (giảm đau dữ dội)
            - **Nuôi ăn:** Nuôi ăn qua ống mũi-dạ dày hoặc tĩnh mạch (nếu nặng)

            **2. Điều trị nguyên nhân:**
            - **Sỏi mật:** ERCP lấy sỏi (nếu tắc ống mật)
            - **Rượu bia:** Bỏ rượu bia HOÀN TOÀN
            - **Tăng triglyceride:** Giảm triglyceride

            **3. Kháng sinh:**
            - Chỉ dùng nếu có nhiễm trùng, hoại tử

            **4. Phẫu thuật:**
            - Chỉ khi có biến chứng (hoại tử nhiễm trùng, áp xe)

            **Viêm tụy mạn:**

            **1. Điều trị đau:**
            - **Thuốc giảm đau:** NSAID, Opioid (nếu cần)
            - **Phẫu thuật:** Cắt dây thần kinh, cắt tụy (nếu đau nặng)

            **2. Điều trị kém hấp thu:**
            - **Enzyme tụy:** Pancreatin (bổ sung enzyme)
            - **Vitamin:** Bổ sung vitamin tan trong dầu (A, D, E, K)

            **3. Điều trị đái tháo đường:**
            - Insulin, thuốc hạ đường huyết

            **4. Bỏ rượu bia:**
            - Bỏ rượu bia HOÀN TOÀN (quan trọng nhất!)

            **⚠️ Lưu ý:**
            - Viêm tụy cấp: Điều trị hỗ trợ, tự khỏi (nhẹ)
            - Viêm tụy mạn: Điều trị lâu dài, không chữa khỏi

            ## 🍽️ CHẾ ĐỘ ĂN:

            **Viêm tụy cấp:**
            - **Nhịn ăn:** Nhịn ăn, uống (1-3 ngày đầu)
            - **Truyền dịch:** Truyền dịch đường tĩnh mạch
            - **Khi đã ổn:** Ăn lỏng → Mềm → Bình thường (từ từ)

            **Viêm tụy mạn:**
            - **Giảm chất béo:** Giảm chất béo (kém hấp thu)
            - **Tăng protein:** Tăng protein nạc
            - **Chia nhỏ bữa:** Ăn nhiều bữa nhỏ
            - **Bổ sung enzyme:** Uống enzyme tụy trước bữa ăn

            **Thực phẩm nên ăn:**
            - Protein nạc (thịt, cá, đậu)
            - Rau xanh, trái cây
            - Ngũ cốc nguyên hạt
            - Uống nhiều nước

            **Thực phẩm nên tránh:**
            - **Rượu bia:** HOÀN TOÀN (quan trọng nhất!)
            - **Đồ chiên rán:** Nhiều chất béo
            - **Thức ăn nhiều chất béo:** Thịt mỡ, nội tạng
            - **Đồ cay nóng:** Kích thích

            **Thực đơn mẫu:**
            - **Sáng:** Cháo yến mạch + trái cây
            - **Trưa:** Cơm + canh rau + cá/thịt nạc + rau xanh
            - **Chiều:** Cơm + canh rau + cá/thịt nạc + rau xanh
            - **Bữa phụ:** Trái cây, sữa chua

            ## 🏃 TẬP THỂ DỤC:

            **Viêm tụy cấp:**
            - Nghỉ ngơi hoàn toàn
            - Tập thể dục sau khi khỏi

            **Viêm tụy mạn:**
            - Tập thể dục nhẹ, đều đặn
            - Tránh gắng sức
            - Giảm cân (nếu béo phì)

            ## 💊 QUẢN LÝ THUỐC:

            **1. Thuốc giảm đau:**
            - **Morphine, Fentanyl:** Viêm tụy cấp (đau dữ dội)
            - **NSAID:** Viêm tụy mạn (đau nhẹ-vừa)

            **2. Enzyme tụy:**
            - **Pancreatin:** Uống trước bữa ăn (viêm tụy mạn)
            - **Liều:** Theo chỉ định bác sĩ

            **3. Vitamin:**
            - **Vitamin A, D, E, K:** Bổ sung (nếu kém hấp thu)

            **4. Insulin:**
            - Nếu có đái tháo đường

            **5. Lưu ý:**
            - Uống đúng liều, đúng giờ
            - Báo bác sĩ nếu có tác dụng phụ
            - Không tự ý ngừng thuốc

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Viêm tụy cấp:**
            - Đau bụng dữ dội, lan ra sau lưng
            - Buồn nôn, nôn nhiều
            - Sốt
            - **Cấp cứu ngay!**

            **2. Biến chứng:**
            - Sốt cao, ớn lạnh (nhiễm trùng)
            - Khó thở (suy phổi)
            - Vàng da (tắc ống mật)
            - Lú lẫn (suy đa tạng)

            **3. Viêm tụy mạn:**
            - Đau nặng, không chịu được
            - Sụt cân nhiều
            - Tiêu chảy mỡ nặng

            ## 💡 PHÒNG NGỪA:

            **1. Bỏ rượu bia:**
            - **Bỏ rượu bia HOÀN TOÀN** (quan trọng nhất!)
            - Giảm nguy cơ viêm tụy cấp, mạn

            **2. Điều trị sỏi mật:**
            - Điều trị sỏi mật (nếu có)
            - Giảm nguy cơ viêm tụy cấp

            **3. Chế độ ăn:**
            - Giảm chất béo
            - Ăn đủ dinh dưỡng
            - Duy trì cân nặng hợp lý

            **4. Kiểm soát bệnh:**
            - Kiểm soát triglyceride máu
            - Kiểm soát đái tháo đường

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Phòng ngừa:**
            - **Bỏ rượu bia HOÀN TOÀN** (quan trọng nhất!)
            - Điều trị sỏi mật
            - Chế độ ăn lành mạnh

            **2. Khi bị viêm tụy:**
            - Đến bệnh viện ngay
            - Tuân thủ điều trị
            - Bỏ rượu bia HOÀN TOÀN

            **3. Sống tích cực:**
            - Viêm tụy cấp: Thường tự khỏi (nhẹ)
            - Viêm tụy mạn: Cần điều trị lâu dài
            - Bỏ rượu bia → Giảm nguy cơ tái phát

            **4. Lâu dài:**
            - Cần điều trị lâu dài (viêm tụy mạn)
            - Bổ sung enzyme, vitamin
            - Theo dõi định kỳ
            """,
            related_disease="pancreatitis",
            related_drugs=["Morphine", "Fentanyl", "Ibuprofen", "Pancreatin", "Insulin"],
            printable=True
        ),

        PatientEducationTopic(
            id="cholecystitis_basics",
            title="Understanding Cholecystitis",
            title_vn="Hiểu về Viêm túi mật",
            category="Disease",
            content="""
            # Hiểu về Viêm túi mật

            ## Viêm túi mật là gì?

            Viêm túi mật (Cholecystitis) là tình trạng viêm của túi mật, thường do sỏi mật tắc ống túi mật. Đây là cấp cứu ngoại khoa phổ biến, cần điều trị ngay để tránh biến chứng.

            **⚠️ Đặc điểm:**
            - Viêm túi mật
            - Thường do sỏi mật
            - Cấp cứu ngoại khoa
            - Cần điều trị ngay

            **Phân loại:**
            - **Viêm túi mật cấp:** Viêm đột ngột, do sỏi mật (90%)
            - **Viêm túi mật mạn:** Viêm tái phát, do sỏi mật
            - **Viêm túi mật không do sỏi:** Không có sỏi mật (10%, thường nặng hơn)

            **Túi mật:**
            - Cơ quan nhỏ, hình quả lê, dưới gan
            - Chức năng: Dự trữ, cô đặc dịch mật

            ## Triệu chứng:

            **Triệu chứng điển hình:**
            - **Đau bụng:** Đau vùng hạ sườn phải, lan ra sau lưng, vai phải, đau liên tục, tăng dần
            - **Sốt:** Sốt 38-39°C
            - **Buồn nôn, nôn:** Thường có
            - **Đau tăng:** Khi ấn vùng hạ sườn phải
            - **Dấu hiệu Murphy:** Đau khi ấn vùng túi mật, hít sâu (đặc trưng)

            **Triệu chứng khác:**
            - Đầy bụng, chướng bụng
            - Chán ăn
            - Vàng da (nếu tắc ống mật)

            **⚠️ Biến chứng:**
            - **Hoại tử túi mật:** Túi mật bị hoại tử
            - **Thủng túi mật:** Túi mật bị thủng
            - **Viêm phúc mạc mật:** Dịch mật rò vào ổ bụng
            - **Áp xe túi mật:** Áp xe trong túi mật
            - **Nhiễm trùng huyết:** Nhiễm trùng toàn thân

            ## Nguyên nhân:

            **1. Sỏi mật (90%):**
            - Sỏi mật tắc ống túi mật
            - Dịch mật ứ đọng → Viêm
            - Nhiễm trùng thứ phát

            **2. Viêm túi mật không do sỏi (10%):**
            - **Nhiễm trùng:** Nhiễm trùng trực tiếp
            - **Chấn thương:** Chấn thương bụng
            - **Sau phẫu thuật:** Sau phẫu thuật lớn
            - **Nuôi ăn tĩnh mạch:** Nuôi ăn tĩnh mạch lâu dài
            - **Bệnh khác:** Đái tháo đường, xơ gan

            **3. Yếu tố nguy cơ:**
            - Sỏi mật
            - Phụ nữ, > 40 tuổi
            - Béo phì
            - Giảm cân nhanh
            - Mang thai

            ## Chẩn đoán:

            **Chẩn đoán lâm sàng:**
            - Triệu chứng điển hình
            - Dấu hiệu Murphy
            - Khám bụng

            **Xét nghiệm:**
            - **Xét nghiệm máu:**
              - Bạch cầu tăng (10-15.000/μL)
              - Bilirubin tăng (nếu tắc ống mật)
              - Men gan tăng (ALT, AST)
              - Amylase, Lipase (nếu viêm tụy)
            - **Siêu âm bụng:** Phát hiện sỏi mật, túi mật dày thành, dịch quanh túi mật (tiêu chuẩn vàng)
            - **CT bụng:** Đánh giá biến chứng
            - **HIDA scan:** Đánh giá chức năng túi mật

            **⚠️ Phân biệt:**
            - Viêm tụy cấp
            - Loét dạ dày-tá tràng thủng
            - Viêm gan
            - Sỏi thận

            ## Điều trị:

            **1. Điều trị cấp cứu:**
            - **Nhịn ăn:** Nhịn ăn, uống (giảm kích thích túi mật)
            - **Truyền dịch:** Truyền dịch đường tĩnh mạch
            - **Kháng sinh:** Kháng sinh đường tĩnh mạch (Cefazolin + Metronidazole)
            - **Giảm đau:** Morphine, NSAID

            **2. Phẫu thuật:**
            - **Cắt túi mật:**
              - **Mổ nội soi:** Ưu tiên (trong 24-72 giờ)
              - **Mổ mở:** Nếu mổ nội soi không được
            - **Thời gian:** Càng sớm càng tốt (trong 24-72 giờ)
            - **Nếu không phẫu thuật:** Cắt túi mật sau khi ổn định (4-6 tuần)

            **3. Điều trị không phẫu thuật (Hiếm, chỉ khi chống chỉ định):**
            - Kháng sinh
            - Dẫn lưu túi mật qua da (nếu có áp xe)
            - Cắt túi mật sau khi ổn định

            **⚠️ Lưu ý:**
            - Phẫu thuật là điều trị chính
            - Cắt túi mật không ảnh hưởng chức năng tiêu hóa (mật vẫn tiết từ gan)

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Trước phẫu thuật:**
            - **Nhịn ăn:** Nhịn ăn, uống (chuẩn bị phẫu thuật)
            - **Truyền dịch:** Truyền dịch đường tĩnh mạch

            **2. Sau phẫu thuật:**
            - **Ngày 1:** Uống nước, nước đường (nếu không nôn)
            - **Ngày 2-3:** Ăn lỏng (cháo, súp)
            - **Ngày 4-5:** Ăn mềm (cơm mềm, thịt/cá nấu chín)
            - **Sau 1 tuần:** Ăn bình thường

            **3. Thực phẩm nên ăn:**
            - Cháo, súp (sau phẫu thuật)
            - Thức ăn mềm, dễ tiêu
            - Rau xanh, trái cây (khi đã ổn)
            - Uống nhiều nước

            **4. Thực phẩm nên tránh:**
            - **Đồ chiên rán:** Nhiều chất béo (trước và sau phẫu thuật)
            - **Thức ăn nhiều chất béo:** Thịt mỡ, nội tạng
            - **Rượu bia:** Có thể kích thích

            **5. Lưu ý:**
            - Ăn từ từ, tăng dần
            - Theo chỉ định bác sĩ
            - Báo nếu đau bụng, nôn

            ## 🏃 TẬP THỂ DỤC:

            **1. Sau phẫu thuật:**
            - **Ngày 1:** Nghỉ ngơi tại giường, đi lại nhẹ
            - **Ngày 2-3:** Đi lại trong phòng
            - **Ngày 4-5:** Đi lại bình thường
            - **Sau 1 tuần:** Tập thể dục nhẹ
            - **Sau 2-4 tuần:** Tập thể dục bình thường

            **2. Tránh:**
            - Gắng sức trong 2-4 tuần đầu
            - Khuân vác nặng
            - Tập thể dục mạnh

            **3. Lưu ý:**
            - Theo chỉ định bác sĩ
            - Báo nếu đau, khó chịu

            ## 💊 QUẢN LÝ THUỐC:

            **1. Kháng sinh:**
            - **Cefazolin + Metronidazole:** Đường tĩnh mạch
            - **Thời gian:** 3-5 ngày (nếu nhẹ), 7-10 ngày (nếu nặng)

            **2. Thuốc giảm đau:**
            - **Morphine:** Nếu đau nặng
            - **NSAID:** Ibuprofen, Diclofenac (nếu đau nhẹ-vừa)

            **3. Lưu ý:**
            - Uống đúng liều, đúng giờ
            - Báo bác sĩ nếu đau không giảm
            - Không tự ý ngừng kháng sinh

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Triệu chứng viêm túi mật:**
            - Đau bụng vùng hạ sườn phải
            - Sốt, buồn nôn, nôn
            - **Cấp cứu ngay!**

            **2. Biến chứng:**
            - Sốt cao, ớn lạnh (nhiễm trùng nặng)
            - Đau bụng dữ dội, lan toàn bụng (thủng)
            - Vàng da (tắc ống mật)
            - Tụt huyết áp (sốc)

            **3. Sau phẫu thuật:**
            - Sốt cao
            - Đau bụng tăng
            - Vết mổ sưng, đỏ, chảy mủ
            - Vàng da

            ## 💡 PHÒNG NGỪA:

            **1. Điều trị sỏi mật:**
            - Điều trị sỏi mật (nếu có)
            - Giảm nguy cơ viêm túi mật

            **2. Chế độ ăn:**
            - Giảm chất béo
            - Tăng chất xơ
            - Duy trì cân nặng hợp lý

            **3. Tránh:**
            - Giảm cân quá nhanh
            - Ăn nhiều chất béo

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Nhận biết triệu chứng:**
            - Đau bụng vùng hạ sườn phải
            - Sốt, buồn nôn, nôn
            - **Cấp cứu ngay!**

            **2. Không trì hoãn:**
            - Viêm túi mật cần điều trị ngay
            - Trì hoãn → Biến chứng → Nguy hiểm

            **3. Sau phẫu thuật:**
            - Hồi phục nhanh (1-2 tuần)
            - Có thể sống bình thường
            - Cắt túi mật không ảnh hưởng chức năng tiêu hóa

            **4. Sống tích cực:**
            - Phẫu thuật an toàn, hiệu quả
            - Phòng ngừa tốt → Không tái phát
            """,
            related_disease="cholecystitis",
            related_drugs=["Cefazolin", "Metronidazole", "Morphine", "Ibuprofen", "Diclofenac"],
            printable=True
        ),

        PatientEducationTopic(
            id="crohn_disease_basics",
            title="Understanding Crohn's Disease",
            title_vn="Hiểu về Bệnh Crohn",
            category="Disease",
            content="""
            # Hiểu về Bệnh Crohn

            ## Bệnh Crohn là gì?

            Bệnh Crohn là bệnh viêm ruột mạn tính, có thể ảnh hưởng đến bất kỳ phần nào của đường tiêu hóa (từ miệng đến hậu môn), đặc trưng bởi viêm từng đoạn, có thể dẫn đến biến chứng nặng.

            **⚠️ Đặc điểm:**
            - Viêm ruột mạn tính
            - Có thể ảnh hưởng toàn bộ đường tiêu hóa
            - Viêm từng đoạn (không liên tục)
            - Bệnh tự miễn, không chữa khỏi

            **Phân loại:**
            - **Theo vị trí:**
              - Crohn hồi tràng (30%): Chỉ ảnh hưởng hồi tràng
              - Crohn đại tràng (20%): Chỉ ảnh hưởng đại tràng
              - Crohn hồi-đại tràng (50%): Ảnh hưởng cả hồi tràng và đại tràng
            - **Theo mức độ:**
              - Nhẹ: Triệu chứng nhẹ, không ảnh hưởng cuộc sống
              - Trung bình: Triệu chứng vừa, ảnh hưởng cuộc sống
              - Nặng: Triệu chứng nặng, biến chứng

            ## Triệu chứng:

            **Triệu chứng đường tiêu hóa:**
            - **Đau bụng:** Đau bụng, thường vùng hố chậu phải (hồi tràng)
            - **Tiêu chảy:** Tiêu chảy mạn tính, có thể có máu
            - **Sụt cân:** Sụt cân do kém hấp thu, chán ăn
            - **Mệt mỏi:** Mệt mỏi, suy nhược
            - **Sốt:** Sốt nhẹ (khi đang viêm)

            **Triệu chứng khác:**
            - **Loét miệng:** Loét miệng tái phát
            - **Đau khớp:** Đau khớp, viêm khớp
            - **Tổn thương da:** Nốt đỏ, loét da
            - **Viêm mắt:** Viêm mắt, đỏ mắt
            - **Thiếu máu:** Thiếu máu do mất máu, kém hấp thu

            **⚠️ Biến chứng:**
            - **Hẹp ruột:** Hẹp ruột do sẹo
            - **Rò ruột:** Rò ruột (fistula)
            - **Áp xe:** Áp xe ổ bụng
            - **Ung thư đại tràng:** Tăng nguy cơ (nếu viêm đại tràng lâu dài)
            - **Suy dinh dưỡng:** Suy dinh dưỡng nặng

            ## Nguyên nhân:

            **1. Nguyên nhân chưa rõ hoàn toàn:**
            - Có nhiều yếu tố

            **2. Yếu tố:**
            - **Tự miễn:** Hệ miễn dịch tấn công ruột
            - **Di truyền:** Có người thân bị bệnh (tăng nguy cơ 10-20 lần)
            - **Môi trường:** Chế độ ăn, nhiễm trùng, stress
            - **Hút thuốc lá:** Tăng nguy cơ, làm nặng bệnh

            **3. Yếu tố nguy cơ:**
            - **Tuổi:** 15-35 tuổi (phổ biến nhất)
            - **Di truyền:** Có người thân bị bệnh
            - **Hút thuốc lá:** Tăng nguy cơ 2-3 lần
            - **Chế độ ăn:** Chế độ ăn nhiều chất béo, ít chất xơ
            - **Dùng NSAID:** Có thể làm nặng bệnh

            ## Chẩn đoán:

            **Chẩn đoán lâm sàng:**
            - Triệu chứng điển hình
            - Khám bụng

            **Xét nghiệm:**
            - **Xét nghiệm máu:**
              - Thiếu máu
              - Tăng bạch cầu, CRP (dấu hiệu viêm)
              - Giảm albumin (suy dinh dưỡng)
            - **Xét nghiệm phân:** Tìm máu, vi khuẩn, ký sinh trùng
            - **Calprotectin phân:** Tăng (dấu hiệu viêm ruột)

            **Hình ảnh:**
            - **Nội soi đại tràng:** Quan sát tổn thương, sinh thiết (tiêu chuẩn vàng)
            - **Nội soi ruột non:** Quan sát ruột non
            - **CT/MRI:** Đánh giá biến chứng (hẹp, rò)
            - **X-quang:** Ít dùng

            **⚠️ Phân biệt:**
            - Viêm loét đại tràng (UC)
            - Hội chứng ruột kích thích
            - Nhiễm trùng đường ruột

            ## Điều trị:

            **1. Điều trị cấp tính (Đợt cấp):**
            - **Corticosteroid:** Prednisolone (giảm viêm nhanh)
            - **Kháng sinh:** Metronidazole, Ciprofloxacin (nếu có nhiễm trùng)
            - **Nuôi ăn:** Nuôi ăn tĩnh mạch (nếu nặng)

            **2. Điều trị duy trì:**
            - **5-ASA:** Mesalamine (nhẹ)
            - **Immunosuppressant:**
              - **Azathioprine, 6-MP:** Ức chế miễn dịch
              - **Methotrexate:** Ức chế miễn dịch
            - **Biological:**
              - **Infliximab, Adalimumab:** Kháng TNF-α
              - **Vedolizumab:** Kháng integrin
            - **Ustekinumab:** Kháng IL-12/23

            **3. Điều trị triệu chứng:**
            - **Thuốc chống tiêu chảy:** Loperamide (thận trọng)
            - **Thuốc giảm đau:** Paracetamol (tránh NSAID)
            - **Bổ sung sắt:** Nếu thiếu máu
            - **Bổ sung vitamin:** Vitamin B12, D, canxi

            **4. Phẫu thuật:**
            - **Chỉ định:**
              - Hẹp ruột, tắc ruột
              - Rò ruột không đáp ứng điều trị
              - Áp xe
              - Ung thư
            - **Phương pháp:**
              - Cắt đoạn ruột bị bệnh
              - Nối ruột

            **⚠️ Lưu ý:**
            - Bệnh không chữa khỏi, cần điều trị lâu dài
            - Điều trị tùy theo mức độ, vị trí
            - Bỏ thuốc lá (quan trọng!)

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Khi đang đợt cấp:**
            - **Nhịn ăn:** Nhịn ăn, uống (nếu nặng)
            - **Nuôi ăn:** Nuôi ăn tĩnh mạch hoặc qua ống
            - **Khi đã ổn:** Ăn lỏng → Mềm → Bình thường (từ từ)

            **2. Khi ổn định:**
            - **Chế độ ăn đủ dinh dưỡng:** Đủ calo, protein, vitamin
            - **Chia nhỏ bữa:** Ăn nhiều bữa nhỏ
            - **Tránh:** Thức ăn gây kích thích

            **3. Thực phẩm nên ăn:**
            - Protein nạc (thịt, cá, đậu)
            - Rau xanh, trái cây (nếu dung nạp)
            - Ngũ cốc nguyên hạt (nếu dung nạp)
            - Sữa chua (probiotic)
            - Uống nhiều nước

            **4. Thực phẩm nên tránh:**
            - **Thức ăn nhiều chất xơ:** Nếu không dung nạp
            - **Đồ cay nóng:** Kích thích ruột
            - **Đồ chiên rán:** Khó tiêu
            - **Sữa:** Nếu không dung nạp lactose
            - **Rượu bia:** Có thể làm nặng

            **5. Thực đơn mẫu:**
            - **Sáng:** Cháo yến mạch + trái cây
            - **Trưa:** Cơm + canh rau + cá/thịt nạc + rau xanh
            - **Chiều:** Cơm + canh rau + cá/thịt nạc + rau xanh
            - **Bữa phụ:** Trái cây, sữa chua

            **6. Lưu ý:**
            - Ghi nhật ký thức ăn để tìm yếu tố kích thích
            - Tránh thức ăn gây triệu chứng
            - Bổ sung vitamin, khoáng chất

            ## 🏃 TẬP THỂ DỤC:

            **1. Khi đang đợt cấp:**
            - Nghỉ ngơi
            - Tập thể dục nhẹ (nếu có thể)

            **2. Khi ổn định:**
            - Tập thể dục đều đặn, 30 phút/ngày
            - Giảm stress (có thể làm nặng bệnh)
            - Yoga, thiền (thư giãn)

            **3. Tránh:**
            - Tập quá sức khi đang đợt cấp
            - Tập khi mệt mỏi

            ## 💊 QUẢN LÝ THUỐC:

            **1. Corticosteroid:**
            - **Prednisolone:** Uống đều đặn, giảm liều từ từ
            - **Tác dụng phụ:** Tăng cân, loãng xương, tăng huyết áp
            - **Lưu ý:** Không tự ý ngừng (nguy hiểm!)

            **2. Immunosuppressant:**
            - **Azathioprine, 6-MP:** Uống đều đặn
            - **Tác dụng phụ:** Giảm bạch cầu, nhiễm trùng
            - **Lưu ý:** Xét nghiệm máu định kỳ

            **3. Biological:**
            - **Infliximab, Adalimumab:** Tiêm, theo chỉ định
            - **Tác dụng phụ:** Nhiễm trùng, phản ứng dị ứng
            - **Lưu ý:** Theo dõi sát

            **4. Lưu ý:**
            - Uống đúng liều, đúng giờ
            - Không tự ý ngừng thuốc
            - Báo bác sĩ nếu có tác dụng phụ
            - Xét nghiệm máu định kỳ

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Đợt cấp nặng:**
            - Tiêu chảy nhiều, có máu
            - Đau bụng dữ dội
            - Sốt cao
            - **Cấp cứu ngay!**

            **2. Biến chứng:**
            - Tắc ruột (đau bụng, nôn, không đi cầu)
            - Rò ruột (dịch chảy ra ngoài)
            - Áp xe (sốt, đau bụng)
            - **Cấp cứu ngay!**

            **3. Tác dụng phụ:**
            - Sốt, ớn lạnh (nhiễm trùng)
            - Phát ban, ngứa (dị ứng)
            - Khó thở

            ## 💡 PHÒNG NGỪA:

            **1. Bỏ thuốc lá:**
            - **Bỏ thuốc lá HOÀN TOÀN** (quan trọng nhất!)
            - Giảm nguy cơ, làm nặng bệnh

            **2. Chế độ ăn:**
            - Ăn đủ dinh dưỡng
            - Tránh thức ăn gây kích thích
            - Ghi nhật ký thức ăn

            **3. Quản lý stress:**
            - Stress có thể làm nặng bệnh
            - Thư giãn, yoga, thiền

            **4. Tránh:**
            - NSAID (có thể làm nặng)
            - Nhiễm trùng

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Phòng ngừa:**
            - **Bỏ thuốc lá HOÀN TOÀN** (quan trọng nhất!)
            - Chế độ ăn lành mạnh
            - Quản lý stress

            **2. Khi bị Crohn:**
            - Điều trị đều đặn, lâu dài
            - Tuân thủ điều trị
            - Theo dõi định kỳ

            **3. Sống tích cực:**
            - Bệnh không chữa khỏi nhưng có thể kiểm soát
            - Điều trị đúng → Giảm triệu chứng, biến chứng
            - Có thể sống bình thường

            **4. Hỗ trợ:**
            - Tham gia nhóm hỗ trợ
            - Giáo dục gia đình
            - Tư vấn tâm lý (nếu cần)

            **5. Lâu dài:**
            - Cần điều trị lâu dài
            - Theo dõi định kỳ
            - Tầm soát ung thư đại tràng (nếu viêm đại tràng lâu dài)
            """,
            related_disease="crohn_disease",
            related_drugs=["Prednisolone", "Mesalamine", "Azathioprine", "Infliximab", "Adalimumab", "Metronidazole"],
            printable=True
        ),

        PatientEducationTopic(
            id="ulcerative_colitis_basics",
            title="Understanding Ulcerative Colitis",
            title_vn="Hiểu về Viêm loét đại tràng",
            category="Disease",
            content="""
            # Hiểu về Viêm loét đại tràng

            ## Viêm loét đại tràng là gì?

            Viêm loét đại tràng (Ulcerative Colitis - UC) là bệnh viêm ruột mạn tính, chỉ ảnh hưởng đến đại tràng và trực tràng, đặc trưng bởi viêm liên tục từ trực tràng lên trên. Bệnh tự miễn, không chữa khỏi, nhưng có thể kiểm soát.

            **⚠️ Đặc điểm:**
            - Viêm ruột mạn tính
            - Chỉ ảnh hưởng đại tràng và trực tràng
            - Viêm liên tục (từ trực tràng lên)
            - Bệnh tự miễn, không chữa khỏi

            **Phân loại:**
            - **Theo mức độ:**
              - Nhẹ: < 4 lần đi cầu/ngày, không có triệu chứng toàn thân
              - Trung bình: 4-6 lần đi cầu/ngày, có triệu chứng toàn thân nhẹ
              - Nặng: > 6 lần đi cầu/ngày, có triệu chứng toàn thân nặng
            - **Theo vị trí:**
              - Proctitis: Chỉ trực tràng
              - Left-sided: Đến góc lách
              - Extensive: Toàn bộ đại tràng

            ## Triệu chứng:

            **Triệu chứng đường tiêu hóa:**
            - **Tiêu chảy:** Tiêu chảy mạn tính, có máu, mủ
            - **Đau bụng:** Đau bụng dưới, quặn bụng
            - **Mót rặn:** Mót rặn, đi cầu nhiều lần
            - **Phân nhầy máu:** Phân có máu, mủ, nhầy
            - **Táo bón:** Có thể có (nếu chỉ viêm trực tràng)

            **Triệu chứng toàn thân:**
            - **Sụt cân:** Sụt cân do kém hấp thu, chán ăn
            - **Mệt mỏi:** Mệt mỏi, suy nhược
            - **Sốt:** Sốt nhẹ (khi đang đợt cấp)
            - **Thiếu máu:** Thiếu máu do mất máu

            **Triệu chứng ngoài ruột:**
            - **Đau khớp:** Đau khớp, viêm khớp
            - **Tổn thương da:** Nốt đỏ, loét da
            - **Viêm mắt:** Viêm mắt, đỏ mắt
            - **Viêm gan:** Viêm gan, xơ gan mật

            **⚠️ Biến chứng:**
            - **Megacolon độc:** Đại tràng giãn, nguy hiểm
            - **Thủng đại tràng:** Thủng đại tràng
            - **Ung thư đại tràng:** Tăng nguy cơ (nếu viêm lâu dài)
            - **Xuất huyết nặng:** Mất máu nhiều

            ## Nguyên nhân:

            **1. Nguyên nhân chưa rõ hoàn toàn:**
            - Có nhiều yếu tố

            **2. Yếu tố:**
            - **Tự miễn:** Hệ miễn dịch tấn công đại tràng
            - **Di truyền:** Có người thân bị bệnh (tăng nguy cơ 10-20 lần)
            - **Môi trường:** Chế độ ăn, nhiễm trùng, stress
            - **Hút thuốc lá:** Giảm nguy cơ (khác với Crohn)

            **3. Yếu tố nguy cơ:**
            - **Tuổi:** 15-35 tuổi (phổ biến nhất)
            - **Di truyền:** Có người thân bị bệnh
            - **Chế độ ăn:** Chế độ ăn nhiều chất béo, ít chất xơ
            - **Dùng NSAID:** Có thể làm nặng bệnh

            ## Chẩn đoán:

            **Chẩn đoán lâm sàng:**
            - Triệu chứng điển hình
            - Khám bụng

            **Xét nghiệm:**
            - **Xét nghiệm máu:**
              - Thiếu máu
              - Tăng bạch cầu, CRP (dấu hiệu viêm)
              - Giảm albumin (suy dinh dưỡng)
            - **Xét nghiệm phân:** Tìm máu, vi khuẩn, ký sinh trùng
            - **Calprotectin phân:** Tăng (dấu hiệu viêm ruột)

            **Hình ảnh:**
            - **Nội soi đại tràng:** Quan sát tổn thương, sinh thiết (tiêu chuẩn vàng)
            - **CT/MRI:** Đánh giá biến chứng

            **⚠️ Phân biệt:**
            - Bệnh Crohn
            - Hội chứng ruột kích thích
            - Nhiễm trùng đường ruột

            ## Điều trị:

            **1. Điều trị cấp tính (Đợt cấp):**
            - **Corticosteroid:** Prednisolone (giảm viêm nhanh)
            - **5-ASA:** Mesalamine (nhẹ-trung bình)
            - **Nuôi ăn:** Nuôi ăn tĩnh mạch (nếu nặng)

            **2. Điều trị duy trì:**
            - **5-ASA:** Mesalamine (uống, đặt hậu môn)
            - **Immunosuppressant:**
              - **Azathioprine, 6-MP:** Ức chế miễn dịch
            - **Biological:**
              - **Infliximab, Adalimumab:** Kháng TNF-α
              - **Vedolizumab:** Kháng integrin
            - **Ustekinumab:** Kháng IL-12/23

            **3. Điều trị triệu chứng:**
            - **Thuốc chống tiêu chảy:** Loperamide (thận trọng)
            - **Thuốc giảm đau:** Paracetamol (tránh NSAID)
            - **Bổ sung sắt:** Nếu thiếu máu
            - **Bổ sung vitamin:** Vitamin B12, D, canxi

            **4. Phẫu thuật:**
            - **Chỉ định:**
              - Megacolon độc
              - Thủng đại tràng
              - Xuất huyết nặng
              - Ung thư
              - Không đáp ứng điều trị
            - **Phương pháp:**
              - Cắt toàn bộ đại tràng, trực tràng
              - Tạo hậu môn nhân tạo (ileostomy)
              - Hoặc nối hồi tràng-hậu môn (ileoanal pouch)

            **⚠️ Lưu ý:**
            - Bệnh không chữa khỏi, cần điều trị lâu dài
            - Điều trị tùy theo mức độ, vị trí
            - Phẫu thuật có thể chữa khỏi (khác với Crohn)

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Khi đang đợt cấp:**
            - **Nhịn ăn:** Nhịn ăn, uống (nếu nặng)
            - **Nuôi ăn:** Nuôi ăn tĩnh mạch hoặc qua ống
            - **Khi đã ổn:** Ăn lỏng → Mềm → Bình thường (từ từ)

            **2. Khi ổn định:**
            - **Chế độ ăn đủ dinh dưỡng:** Đủ calo, protein, vitamin
            - **Chia nhỏ bữa:** Ăn nhiều bữa nhỏ
            - **Tránh:** Thức ăn gây kích thích

            **3. Thực phẩm nên ăn:**
            - Protein nạc (thịt, cá, đậu)
            - Rau xanh, trái cây (nếu dung nạp)
            - Ngũ cốc nguyên hạt (nếu dung nạp)
            - Sữa chua (probiotic)
            - Uống nhiều nước

            **4. Thực phẩm nên tránh:**
            - **Thức ăn nhiều chất xơ:** Nếu không dung nạp
            - **Đồ cay nóng:** Kích thích ruột
            - **Đồ chiên rán:** Khó tiêu
            - **Sữa:** Nếu không dung nạp lactose
            - **Rượu bia:** Có thể làm nặng

            **5. Thực đơn mẫu:**
            - **Sáng:** Cháo yến mạch + trái cây
            - **Trưa:** Cơm + canh rau + cá/thịt nạc + rau xanh
            - **Chiều:** Cơm + canh rau + cá/thịt nạc + rau xanh
            - **Bữa phụ:** Trái cây, sữa chua

            **6. Lưu ý:**
            - Ghi nhật ký thức ăn để tìm yếu tố kích thích
            - Tránh thức ăn gây triệu chứng
            - Bổ sung vitamin, khoáng chất

            ## 🏃 TẬP THỂ DỤC:

            **1. Khi đang đợt cấp:**
            - Nghỉ ngơi
            - Tập thể dục nhẹ (nếu có thể)

            **2. Khi ổn định:**
            - Tập thể dục đều đặn, 30 phút/ngày
            - Giảm stress (có thể làm nặng bệnh)
            - Yoga, thiền (thư giãn)

            **3. Tránh:**
            - Tập quá sức khi đang đợt cấp
            - Tập khi mệt mỏi

            ## 💊 QUẢN LÝ THUỐC:

            **1. Corticosteroid:**
            - **Prednisolone:** Uống đều đặn, giảm liều từ từ
            - **Tác dụng phụ:** Tăng cân, loãng xương, tăng huyết áp
            - **Lưu ý:** Không tự ý ngừng (nguy hiểm!)

            **2. 5-ASA:**
            - **Mesalamine:** Uống, đặt hậu môn
            - **Uống đều đặn:** Theo chỉ định bác sĩ

            **3. Immunosuppressant:**
            - **Azathioprine, 6-MP:** Uống đều đặn
            - **Tác dụng phụ:** Giảm bạch cầu, nhiễm trùng
            - **Lưu ý:** Xét nghiệm máu định kỳ

            **4. Biological:**
            - **Infliximab, Adalimumab:** Tiêm, theo chỉ định
            - **Tác dụng phụ:** Nhiễm trùng, phản ứng dị ứng
            - **Lưu ý:** Theo dõi sát

            **5. Lưu ý:**
            - Uống đúng liều, đúng giờ
            - Không tự ý ngừng thuốc
            - Báo bác sĩ nếu có tác dụng phụ
            - Xét nghiệm máu định kỳ

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Đợt cấp nặng:**
            - Tiêu chảy nhiều, có máu
            - Đau bụng dữ dội
            - Sốt cao
            - **Cấp cứu ngay!**

            **2. Biến chứng:**
            - Megacolon độc (đau bụng dữ dội, sốt, chướng bụng)
            - Thủng đại tràng (đau bụng dữ dội, sốt)
            - Xuất huyết nặng (mất máu nhiều)
            - **Cấp cứu ngay!**

            **3. Tác dụng phụ:**
            - Sốt, ớn lạnh (nhiễm trùng)
            - Phát ban, ngứa (dị ứng)
            - Khó thở

            ## 💡 PHÒNG NGỪA:

            **1. Chế độ ăn:**
            - Ăn đủ dinh dưỡng
            - Tránh thức ăn gây kích thích
            - Ghi nhật ký thức ăn

            **2. Quản lý stress:**
            - Stress có thể làm nặng bệnh
            - Thư giãn, yoga, thiền

            **3. Tránh:**
            - NSAID (có thể làm nặng)
            - Nhiễm trùng

            **4. Theo dõi:**
            - Nội soi định kỳ (tầm soát ung thư)
            - Xét nghiệm máu định kỳ

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Khi bị viêm loét đại tràng:**
            - Điều trị đều đặn, lâu dài
            - Tuân thủ điều trị
            - Theo dõi định kỳ

            **2. Sống tích cực:**
            - Bệnh không chữa khỏi nhưng có thể kiểm soát
            - Điều trị đúng → Giảm triệu chứng, biến chứng
            - Có thể sống bình thường
            - Phẫu thuật có thể chữa khỏi (nếu cần)

            **3. Hỗ trợ:**
            - Tham gia nhóm hỗ trợ
            - Giáo dục gia đình
            - Tư vấn tâm lý (nếu cần)

            **4. Lâu dài:**
            - Cần điều trị lâu dài
            - Theo dõi định kỳ
            - Tầm soát ung thư đại tràng (nếu viêm lâu dài)
            """,
            related_disease="ulcerative_colitis",
            related_drugs=["Prednisolone", "Mesalamine", "Azathioprine", "Infliximab", "Adalimumab"],
            printable=True
        ),

        # ===== GAN NHIỄM MỠ KHÔNG DO RƯỢU (NAFLD) – tờ rơi ngắn cho bệnh nhân =====
        PatientEducationTopic(
            id="nafld_basics_vn",
            title="Understanding Fatty Liver (NAFLD)",
            title_vn="Gan nhiễm mỡ không do rượu: Điều bệnh nhân cần biết",
            category="Gastrointestinal",
            content="""
# Gan nhiễm mỡ không do rượu (NAFLD) là gì?
- Mỡ tích tụ quá nhiều trong gan (≥ 5% tế bào gan) ở người không uống rượu hoặc uống rất ít.
- Thường gặp ở người thừa cân/béo phì, đái tháo đường típ 2, rối loạn mỡ máu.
- Đa số nhẹ, nhưng một số có thể tiến triển viêm gan nhiễm mỡ (NASH), xơ gan.

## Triệu chứng
- Thường **không có triệu chứng**.
- Đôi khi mệt, nặng tức hạ sườn phải nhẹ.
- Phát hiện qua siêu âm hoặc xét nghiệm men gan.

## Khi nào cần đi khám ngay?
- Vàng da, vàng mắt; bụng to nhanh; phù chân; nôn ra máu/đi ngoài phân đen; mệt nhiều → **đi khám/cấp cứu**.

## Điều trị: 3 trụ cột
1) **Giảm cân** (quan trọng nhất): mục tiêu giảm 7–10% cân nặng.
2) **Chế độ ăn lành mạnh cho gan:**
   - Giảm tinh bột tinh chế, đồ ngọt, nước ngọt/trà sữa.
   - Giảm mỡ động vật, nội tạng; hạn chế chiên/rán.
   - Tăng rau, trái cây tươi, ngũ cốc nguyên hạt; cá 2–3 lần/tuần; dùng dầu thực vật.
   - Hạn chế rượu bia (tốt nhất tránh).
3) **Tập luyện**: ≥ 150 phút/tuần aerobic (đi bộ nhanh, đạp xe, bơi) + 2–3 buổi sức mạnh/tuần.

## Thuốc
- Chưa có thuốc đặc hiệu bắt buộc cho NAFLD nhẹ; bác sĩ có thể kê nếu có bệnh kèm (ĐTĐ, mỡ máu...).
- Kiểm soát tốt đường huyết, mỡ máu, huyết áp giúp gan hồi phục.

## Lưu ý riêng cho Việt Nam
- Hạn chế thức uống nhiều đường (trà sữa, nước ngọt), bữa tối muộn, ăn vặt nhiều tinh bột.
- Ưu tiên khẩu phần “đĩa 1/2 rau, 1/4 đạm nạc, 1/4 tinh bột”.
- Theo dõi cân nặng, vòng bụng; mục tiêu giảm từ từ.

## Theo dõi & tái khám
- Kiểm tra men gan, siêu âm định kỳ (theo bác sĩ, thường 6–12 tháng).
- Nếu men gan cao kéo dài hoặc có xơ hoá → theo dõi sát chuyên khoa.
""",
            related_disease="nafld",
            related_drugs=[],
            printable=True,
        ),

]
