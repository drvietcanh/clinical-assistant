"""
Patient Education Topics - Cardiovascular
"""
from patient_education.models import PatientEducationTopic


CARDIOVASCULAR_TOPICS = [
        PatientEducationTopic(
                id="hypertension_basics",
                title="Understanding High Blood Pressure",
                title_vn="Hiểu về Tăng huyết áp",
                category="Disease",
                content="""
            # Hiểu về Tăng huyết áp

            ## Tăng huyết áp là gì?

            Tăng huyết áp (cao huyết áp) là khi huyết áp cao hơn bình thường trong thời gian dài. Huyết áp là áp lực của máu lên thành động mạch khi tim bơm máu.

            **Huyết áp gồm 2 số:**
            - **Số trên (Tâm thu):** Áp lực khi tim co bóp
            - **Số dưới (Tâm trương):** Áp lực khi tim giãn

            ## Phân loại huyết áp:

            **Bình thường:** < 120/80 mmHg
            **Tăng huyết áp độ 1:** 130-139/80-89 mmHg
            **Tăng huyết áp độ 2:** ≥ 140/90 mmHg
            **Tăng huyết áp cấp cứu:** ≥ 180/120 mmHg (cần cấp cứu ngay!)

            **⚠️ Lưu ý:** Huyết áp thay đổi theo thời gian trong ngày, cần đo nhiều lần để chẩn đoán.

            ## Nguyên nhân:

            **1. Nguyên nhân không thay đổi được:**
            - **Tuổi cao:** Mạch máu cứng dần theo tuổi
            - **Di truyền:** Có người thân bị tăng huyết áp
            - **Giới tính:** Nam > 55 tuổi, Nữ > 65 tuổi dễ mắc hơn

            **2. Nguyên nhân có thể thay đổi:**
            - **Béo phì:** Tăng cân → Tăng huyết áp
            - **Ăn mặn:** Muối giữ nước → Tăng thể tích máu → Tăng huyết áp
            - **Ít vận động:** Tim phải làm việc nhiều hơn
            - **Hút thuốc lá:** Làm hẹp mạch máu
            - **Uống rượu bia:** Làm tăng huyết áp
            - **Stress:** Làm tăng hormone gây tăng huyết áp
            - **Thiếu ngủ:** Rối loạn hormone
            - **Bệnh khác:** Đái tháo đường, bệnh thận, bệnh tuyến giáp

            ## Triệu chứng:

            **⚠️ QUAN TRỌNG:** Hầu hết người tăng huyết áp KHÔNG có triệu chứng!

            **Triệu chứng có thể gặp (khi huyết áp rất cao):**
            - Đau đầu (thường sau gáy, buổi sáng)
            - Chóng mặt, choáng váng
            - Mệt mỏi, uể oải
            - Nhìn mờ
            - Đau ngực
            - Khó thở
            - Tim đập nhanh, không đều

            **⚠️ Lưu ý:** Không nên dựa vào triệu chứng để biết huyết áp cao. Cần đo huyết áp thường xuyên!

            ## Điều trị:

            **1. Thay đổi lối sống (Quan trọng nhất!):**
            - Chế độ ăn ít muối
            - Tập thể dục đều đặn
            - Giảm cân (nếu thừa cân)
            - Bỏ thuốc lá
            - Hạn chế rượu bia
            - Quản lý stress
            - Ngủ đủ giấc

            **2. Thuốc:**
            - **ACE inhibitors:** Enalapril, Lisinopril
            - **ARB:** Losartan, Valsartan
            - **Calcium channel blockers:** Amlodipine, Nifedipine
            - **Diuretics:** Hydrochlorothiazide, Furosemide
            - **Beta-blockers:** Metoprolol, Atenolol
            - **Quan trọng:** Uống đúng giờ, đúng liều, không tự ý ngừng

            **3. Theo dõi:**
            - Đo huyết áp tại nhà
            - Khám định kỳ
            - Điều chỉnh thuốc nếu cần

            ## 🍽️ CHẾ ĐỘ ĂN CHO NGƯỜI TĂNG HUYẾT ÁP:

            **1. Giảm muối (QUAN TRỌNG NHẤT!):**
            - **Mục tiêu:** < 5g muối/ngày (< 2g natri/ngày)
            - **1 thìa cà phê muối = 5g muối**
            - **Cách giảm muối:**
              - Không thêm muối khi nấu (hoặc giảm 1/2)
              - Không chấm muối, nước mắm khi ăn
              - Tránh đồ mặn: Dưa muối, cà muối, đồ hộp
              - Tránh thức ăn nhanh, đồ chế biến sẵn
              - Đọc nhãn: Chọn thực phẩm < 120mg natri/100g
              - Dùng gia vị thay thế: Chanh, tỏi, gừng, rau thơm

            **2. Tăng Kali (Giúp giảm huyết áp):**
            - **Thực phẩm giàu kali:**
              - Chuối, cam, bơ
              - Khoai tây, khoai lang
              - Rau xanh: Rau muống, rau cải, rau ngót
              - Đậu, đậu phụ
              - Cá, sữa
            - **Lưu ý:** Nếu dùng thuốc lợi tiểu giữ kali → Hỏi bác sĩ

            **3. Chế độ ăn DASH (Dietary Approaches to Stop Hypertension):**
            - **Nhiều rau xanh, trái cây:** 4-5 phần/ngày
            - **Ngũ cốc nguyên hạt:** 6-8 phần/ngày
            - **Sữa ít béo:** 2-3 phần/ngày
            - **Protein nạc:** 2 phần/ngày (cá, thịt nạc, đậu)
            - **Chất béo tốt:** 2-3 thìa cà phê dầu/ngày
            - **Hạn chế:** Đường, đồ ngọt (< 5 phần/tuần)

            **4. Thực phẩm nên ăn:**
            - Rau xanh (nhiều): Rau cải, rau muống, rau ngót, bông cải
            - Trái cây: Chuối, cam, bưởi, táo
            - Cá: Cá hồi, cá thu (2-3 lần/tuần)
            - Thịt nạc: Thịt gà (bỏ da), thịt bò nạc
            - Đậu, đậu phụ
            - Sữa ít béo, sữa chua
            - Ngũ cốc nguyên hạt: Gạo lứt, yến mạch

            **5. Thực phẩm cần tránh:**
            - **Đồ mặn:** Dưa muối, cà muối, đồ hộp
            - **Thức ăn nhanh:** Hamburger, pizza, gà rán
            - **Đồ chế biến sẵn:** Xúc xích, thịt nguội, giò chả
            - **Đồ khô:** Cá khô, tôm khô, mắm
            - **Nước mắm, nước tương:** Dùng ít, pha loãng
            - **Bánh mì, bánh quy:** Có nhiều muối ẩn

            **6. Thực đơn mẫu (1 ngày):**
            - **Sáng:** Cháo yến mạch + 1 quả chuối + sữa ít béo
            - **Trưa:** 1 chén cơm + cá kho (ít muối) + rau luộc + canh rau
            - **Tối:** 1 chén cơm + thịt gà luộc + rau xào + canh
            - **Bữa phụ:** Trái cây, sữa chua

            ## 🏃 TẬP THỂ DỤC:

            **1. Loại bài tập:**
            - **Aerobic:** Đi bộ, chạy bộ, bơi, đạp xe, khiêu vũ
            - **Sức mạnh:** Nâng tạ nhẹ, tập với dây kháng lực (2-3 lần/tuần)
            - **Kéo giãn:** Yoga, thái cực quyền

            **2. Thời gian và tần suất:**
            - **Tối thiểu:** 30 phút/ngày, 5 ngày/tuần
            - **Lý tưởng:** 45-60 phút/ngày
            - **Có thể chia nhỏ:** 3 lần x 10 phút/ngày

            **3. Cường độ:**
            - **Vừa phải:** Có thể nói chuyện khi tập, hơi thở gấp
            - **Tránh:** Tập quá sức, gắng sức đột ngột

            **4. Lưu ý:**
            - Khởi động 5-10 phút trước
            - Giãn cơ 5-10 phút sau
            - Đo huyết áp trước và sau tập
            - Dừng ngay nếu: Đau ngực, chóng mặt, khó thở nặng
            - Uống đủ nước

            **5. Lợi ích:**
            - Giảm huyết áp 5-10 mmHg
            - Giảm cân
            - Tăng sức khỏe tim mạch
            - Giảm stress

            ## 💊 QUẢN LÝ THUỐC:

            **1. Uống đúng giờ:**
            - Một số thuốc uống buổi sáng
            - Một số thuốc uống buổi tối (giúp giảm huyết áp ban đêm)
            - Tuân thủ theo chỉ định bác sĩ

            **2. Không tự ý ngừng:**
            - Tăng huyết áp cần điều trị lâu dài
            - Ngừng thuốc đột ngột → Huyết áp tăng cao nguy hiểm
            - Chỉ ngừng khi bác sĩ chỉ định

            **3. Tác dụng phụ:**
            - Chóng mặt, mệt mỏi (thường gặp khi mới uống)
            - Ho khan (ACE inhibitors)
            - Phù chân (một số thuốc)
            - **Báo bác sĩ nếu:** Tác dụng phụ nghiêm trọng, không chịu được

            **4. Tương tác thuốc:**
            - Báo bác sĩ TẤT CẢ thuốc đang dùng
            - Một số thuốc làm tăng huyết áp: Thuốc cảm, thuốc giảm đau NSAID

            ## 📊 THEO DÕI HUYẾT ÁP:

            **1. Đo tại nhà:**
            - **Thời điểm:** Buổi sáng (sau khi thức dậy, trước uống thuốc), buổi tối
            - **Tần suất:** Hàng ngày hoặc ít nhất 3-4 lần/tuần
            - **Cách đo:** Xem topic "Cách đo Huyết áp tại nhà"

            **2. Ghi nhật ký:**
            - Ghi: Ngày, giờ, số đo, thuốc đã uống, hoạt động
            - Mang khi khám bác sĩ

            **3. Khám định kỳ:**
            - **Hàng tháng:** Đo huyết áp, đánh giá điều trị
            - **Mỗi 3-6 tháng:** Xét nghiệm máu, đánh giá biến chứng
            - **Mỗi năm:** Khám mắt, đánh giá tổng thể

            ## ⚠️ BIẾN CHỨNG NẾU KHÔNG ĐIỀU TRỊ:

            **1. Tim mạch:**
            - **Nhồi máu cơ tim:** Huyết áp cao làm tổn thương mạch vành
            - **Suy tim:** Tim phải làm việc quá sức
            - **Rối loạn nhịp tim**

            **2. Não:**
            - **Đột quỵ:** Vỡ hoặc tắc mạch máu não
            - **Suy giảm trí nhớ:** Tổn thương mạch máu não

            **3. Thận:**
            - **Suy thận:** Tổn thương mạch máu thận
            - **Có thể cần lọc thận**

            **4. Mắt:**
            - **Tổn thương võng mạc:** Mờ mắt, mù lòa

            **5. Mạch máu:**
            - **Phình động mạch chủ:** Nguy hiểm, có thể vỡ
            - **Bệnh động mạch ngoại vi:** Đau chân khi đi

            **⚠️ QUAN TRỌNG:** Kiểm soát huyết áp tốt giúp giảm 40-50% nguy cơ đột quỵ và nhồi máu cơ tim!

            ## 🚨 TĂNG HUYẾT ÁP CẤP CỨU:

            **Khi nào cần cấp cứu:**
            - Huyết áp ≥ 180/120 mmHg
            - Có triệu chứng: Đau đầu dữ dội, đau ngực, khó thở, nhìn mờ, lú lẫn

            **Xử trí:**
            - Gọi cấp cứu ngay (115)
            - Ngồi nghỉ, thư giãn
            - Uống thuốc hạ huyết áp (nếu bác sĩ đã kê sẵn)
            - Không tự ý uống thuốc mới

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Giảm cân:**
            - Giảm 5-10% cân nặng → Giảm 5-10 mmHg huyết áp
            - Mục tiêu: BMI 18.5-24.9

            **2. Quản lý stress:**
            - Tập thư giãn: Hít thở sâu, thiền, yoga
            - Ngủ đủ 7-8 giờ/đêm
            - Tránh căng thẳng kéo dài
            - Tìm sở thích, giải trí

            **3. Bỏ thuốc lá:**
            - Hút thuốc làm tăng huyết áp ngay lập tức
            - Bỏ thuốc → Giảm nguy cơ tim mạch đáng kể

            **4. Hạn chế rượu bia:**
            - **Nam:** Tối đa 2 ly/ngày
            - **Nữ:** Tối đa 1 ly/ngày
            - 1 ly = 1 lon bia, 1 ly rượu vang, 1 shot rượu mạnh

            **5. Ngủ đủ giấc:**
            - Thiếu ngủ → Tăng huyết áp
            - Ngủ 7-8 giờ/đêm
            - Điều trị ngưng thở khi ngủ nếu có

            **6. Tránh caffeine quá mức:**
            - Cà phê, trà có thể làm tăng huyết áp tạm thời
            - Hạn chế: 1-2 ly/ngày
            - Đo huyết áp trước và sau uống cà phê để xem ảnh hưởng

            **7. Kiểm tra huyết áp thường xuyên:**
            - Đo tại nhà hàng ngày
            - Mang máy đo khi khám bác sĩ
            - Ghi nhật ký

            **8. Tuân thủ điều trị:**
            - Uống thuốc đúng giờ, đúng liều
            - Không tự ý ngừng hoặc thay đổi liều
            - Báo bác sĩ nếu có vấn đề
                """,
                related_disease="hypertension",
                related_drugs=["Amlodipine", "Enalapril", "Losartan"],
                printable=True
        ),

        PatientEducationTopic(
                id="heart_failure_basics",
                title="Understanding Heart Failure",
                title_vn="Hiểu về Suy tim",
                category="Disease",
                content="""
            # Hiểu về Suy tim

            ## Suy tim là gì?

            Suy tim là khi tim không bơm đủ máu để đáp ứng nhu cầu của cơ thể. Tim yếu hoặc cứng, không thể bơm máu hiệu quả, dẫn đến máu ứ lại ở phổi và các cơ quan khác.

            **Có 2 loại:**
            - **Suy tim tâm thu:** Tim co bóp yếu (EF < 40%)
            - **Suy tim tâm trương:** Tim cứng, không giãn được (EF bình thường)

            ## Nguyên nhân:

            - **Bệnh mạch vành:** Nhồi máu cơ tim, thiếu máu cơ tim
            - **Tăng huyết áp:** Tim phải làm việc quá sức
            - **Bệnh van tim:** Hẹp/hở van tim
            - **Bệnh cơ tim:** Viêm cơ tim, cơ tim giãn
            - **Rối loạn nhịp tim:** Rung nhĩ, nhịp nhanh
            - **Đái tháo đường:** Tổn thương mạch máu
            - **Bệnh phổi mạn tính:** COPD
            - **Bệnh tuyến giáp**

            ## Triệu chứng:

            **Triệu chứng chính:**
            - **Khó thở:**
              - Khi gắng sức (đi bộ, leo cầu thang)
              - Khi nằm (phải kê gối cao)
              - Khó thở về đêm (thức giấc vì khó thở)
            - **Mệt mỏi:** Dễ mệt, không làm được việc nặng
            - **Phù:** Chân, mắt cá chân, bụng (cổ trướng)
            - **Ho khan:** Đặc biệt khi nằm
            - **Tăng cân:** Do ứ dịch (> 2kg/tuần)

            **Triệu chứng khác:**
            - Tim đập nhanh, không đều
            - Đau ngực
            - Chán ăn, buồn nôn
            - Tiểu ít
            - Lú lẫn (ở người già)

            **⚠️ Phân độ suy tim (NYHA):**
            - **Độ I:** Không có triệu chứng khi hoạt động bình thường
            - **Độ II:** Triệu chứng khi gắng sức vừa
            - **Độ III:** Triệu chứng khi gắng sức nhẹ
            - **Độ IV:** Triệu chứng cả khi nghỉ

            ## Điều trị:

            **1. Thuốc (QUAN TRỌNG!):**
            - **ACE inhibitors/ARB:** Giảm gánh tim, bảo vệ tim
            - **Beta-blockers:** Giảm nhịp tim, tăng sức co bóp
            - **Lợi tiểu:** Giảm ứ dịch (Furosemide, Spironolactone)
            - **Digoxin:** Tăng sức co bóp tim (nếu cần)
            - **Quan trọng:** Uống đúng giờ, đúng liều, không tự ý ngừng

            **2. Chế độ ăn:**
            - Ít muối (< 2g/ngày)
            - Hạn chế nước (nếu bác sĩ yêu cầu)
            - Xem chi tiết bên dưới

            **3. Tập thể dục:**
            - Tập nhẹ nhàng, phù hợp
            - Phục hồi chức năng tim
            - Xem chi tiết bên dưới

            **4. Theo dõi:**
            - Cân nặng hàng ngày
            - Huyết áp, nhịp tim
            - Triệu chứng

            ## 🍽️ CHẾ ĐỘ ĂN CHO NGƯỜI SUY TIM:

            **1. Giảm muối (RẤT QUAN TRỌNG!):**
            - **Mục tiêu:** < 2g muối/ngày (rất ít!)
            - **1 thìa cà phê muối = 5g muối**
            - **Cách giảm muối:**
              - Không thêm muối khi nấu
              - Không chấm muối, nước mắm
              - Tránh hoàn toàn: Dưa muối, cà muối, đồ hộp
              - Tránh thức ăn nhanh, đồ chế biến sẵn
              - Dùng gia vị thay thế: Chanh, tỏi, gừng, rau thơm
              - Đọc nhãn: Chọn thực phẩm < 100mg natri/100g

            **2. Hạn chế nước (Nếu bác sĩ yêu cầu):**
            - **Mục tiêu:** 1.5-2 lít/ngày (bao gồm cả nước, canh, sữa, trái cây)
            - **Cách hạn chế:**
              - Uống từng ngụm nhỏ
              - Dùng cốc nhỏ
              - Tránh đồ uống có đường (gây khát)
              - Ngậm đá viên nếu khát
              - Tránh đồ mặn (gây khát)

            **3. Thực phẩm nên ăn:**
            - **Rau xanh:** Nhiều (luộc, hấp, không muối)
            - **Trái cây:** Táo, lê, cam (ăn tươi, không ép)
            - **Protein nạc:** Cá, thịt gà (luộc, hấp, không muối)
            - **Ngũ cốc:** Gạo, bánh mì (ít)
            - **Sữa ít béo:** 1-2 ly/ngày

            **4. Thực phẩm cần tránh:**
            - **Đồ mặn:** Dưa muối, cà muối, đồ hộp, thức ăn nhanh
            - **Đồ nhiều nước:** Canh, súp, chè (nếu hạn chế nước)
            - **Rượu bia:** Làm suy tim nặng hơn
            - **Caffeine:** Có thể làm tim đập nhanh

            **5. Thực đơn mẫu (1 ngày):**
            - **Sáng:** Cháo yến mạch (không muối) + 1 quả trứng luộc
            - **Trưa:** 1/2 chén cơm + cá luộc (không muối) + rau luộc
            - **Tối:** 1/2 chén cơm + thịt gà luộc + rau xào (ít dầu, không muối)
            - **Bữa phụ:** Trái cây tươi

            **6. Lưu ý:**
            - Ăn nhạt hoàn toàn (sẽ quen sau vài tuần)
            - Chia nhỏ bữa ăn (5-6 bữa/ngày)
            - Ăn chậm, nhai kỹ
            - Tránh ăn quá no (gây khó thở)

            ## 🏃 TẬP THỂ DỤC:

            **⚠️ QUAN TRỌNG:** Tập thể dục giúp cải thiện suy tim, nhưng phải có chỉ định và hướng dẫn của bác sĩ!

            **1. Loại bài tập:**
            - **Đi bộ:** Dễ nhất, an toàn nhất
            - **Đạp xe tại chỗ:** Ít gắng sức
            - **Tập tay:** Với tạ nhẹ, dây kháng lực
            - **Yoga, thái cực quyền:** Nhẹ nhàng, thư giãn

            **2. Thời gian và tần suất:**
            - **Bắt đầu:** 5-10 phút/ngày
            - **Tăng dần:** 20-30 phút/ngày
            - **Tần suất:** 3-5 lần/tuần
            - **Cường độ:** Nhẹ, vừa phải (có thể nói chuyện)

            **3. Lưu ý khi tập:**
            - Khởi động 5-10 phút
            - Dừng ngay nếu: Khó thở nặng, đau ngực, chóng mặt, mệt mỏi
            - Nghỉ giữa các bài tập
            - Giãn cơ sau tập
            - Đo huyết áp, nhịp tim trước và sau

            **4. Tránh:**
            - Tập quá sức
            - Tập khi mệt, khó thở
            - Tập khi thời tiết quá nóng/lạnh
            - Tập ngay sau ăn

            **5. Lợi ích:**
            - Tăng sức khỏe tim
            - Giảm triệu chứng
            - Tăng khả năng hoạt động
            - Cải thiện chất lượng sống

            ## 📊 THEO DÕI:

            **1. Cân nặng (QUAN TRỌNG NHẤT!):**
            - **Đo mỗi sáng:** Sau khi đi vệ sinh, trước khi ăn, không mặc quần áo
            - **Ghi nhật ký:** Ngày, cân nặng, triệu chứng
            - **⚠️ Dấu hiệu báo động:**
              - Tăng > 1.5kg trong 1 ngày
              - Tăng > 2kg trong 1 tuần
              - → Có thể ứ dịch, cần gọi bác sĩ

            **2. Huyết áp và nhịp tim:**
            - Đo hàng ngày
            - Ghi nhật ký
            - Mục tiêu: Theo chỉ định bác sĩ

            **3. Triệu chứng:**
            - Khó thở: Mức độ, khi nào
            - Phù: Vị trí, mức độ
            - Mệt mỏi: Mức độ
            - Ho: Khi nào, có đờm không

            **4. Khám định kỳ:**
            - **Hàng tháng:** Đo huyết áp, cân nặng, đánh giá triệu chứng
            - **Mỗi 3 tháng:** Xét nghiệm máu, đánh giá điều trị
            - **Mỗi 6 tháng - 1 năm:** Siêu âm tim, đánh giá tổng thể

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN NGAY:

            **1. Khó thở nặng:**
            - Khó thở khi nghỉ
            - Không nằm được (phải ngồi)
            - Thở nhanh, gấp

            **2. Phù nhiều:**
            - Phù toàn thân
            - Phù bụng (cổ trướng)
            - Phù không giảm

            **3. Tăng cân nhanh:**
            - Tăng > 2kg trong 1 tuần
            - Tăng > 1.5kg trong 1 ngày

            **4. Triệu chứng khác:**
            - Đau ngực
            - Tim đập nhanh, không đều
            - Lú lẫn, mệt mỏi cực độ
            - Ho ra máu
            - Không đi tiểu được

            **5. Không đáp ứng với thuốc:**
            - Uống thuốc nhưng triệu chứng không giảm
            - Phải tăng liều thuốc lợi tiểu

            ## 💊 QUẢN LÝ THUỐC:

            **1. Uống đúng giờ:**
            - Một số thuốc uống buổi sáng
            - Một số thuốc uống buổi tối
            - Lợi tiểu thường uống buổi sáng (tránh đi tiểu đêm)

            **2. Không tự ý ngừng:**
            - Suy tim cần điều trị suốt đời
            - Ngừng thuốc → Suy tim nặng hơn, có thể nguy hiểm
            - Chỉ ngừng khi bác sĩ chỉ định

            **3. Tác dụng phụ:**
            - **Lợi tiểu:** Đi tiểu nhiều, mất kali (có thể chuột rút)
            - **ACE inhibitors:** Ho khan, chóng mặt
            - **Beta-blockers:** Mệt mỏi, chậm nhịp tim
            - **Báo bác sĩ nếu:** Tác dụng phụ nghiêm trọng

            **4. Tương tác thuốc:**
            - Báo bác sĩ TẤT CẢ thuốc đang dùng
            - Một số thuốc làm suy tim nặng: NSAID, một số thuốc cảm

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Nghỉ ngơi:**
            - Ngủ đủ 7-8 giờ/đêm
            - Kê gối cao khi ngủ (giảm khó thở)
            - Nghỉ giữa các hoạt động
            - Tránh gắng sức

            **2. Quản lý stress:**
            - Stress làm suy tim nặng hơn
            - Tập thư giãn: Hít thở sâu, thiền
            - Tránh căng thẳng

            **3. Tiêm chủng:**
            - Tiêm vắc xin cúm hàng năm
            - Tiêm vắc xin phế cầu (nếu bác sĩ chỉ định)
            - Tiêm vắc xin COVID-19

            **4. Chăm sóc bản thân:**
            - Không hút thuốc
            - Hạn chế rượu bia
            - Giữ ấm (tránh nhiễm trùng)
            - Vệ sinh răng miệng tốt

            **5. Khi ốm:**
            - Tiếp tục uống thuốc
            - Theo dõi cân nặng, triệu chứng
            - Gọi bác sĩ nếu: Khó thở tăng, tăng cân, không ăn được

            **6. Hỗ trợ:**
            - Nói với gia đình về bệnh
            - Tham gia nhóm hỗ trợ (nếu có)
            - Hỏi bác sĩ khi không rõ

            **7. Sống tích cực:**
            - Suy tim có thể kiểm soát được
            - Tuân thủ điều trị → Sống khỏe mạnh
            - Đừng để bệnh chi phối cuộc sống
                """,
                related_disease="heart_failure",
                related_drugs=["ACE Inhibitor", "Beta-blocker", "Furosemide"],
                printable=True
        ),

        PatientEducationTopic(
            id="stroke_basics",
            title="Understanding Stroke",
            title_vn="Hiểu về Đột quỵ",
            category="Disease",
            content="""
            # Hiểu về Đột quỵ

            ## Đột quỵ là gì?

            Đột quỵ (Tai biến mạch máu não) xảy ra khi mạch máu não bị tắc nghẽn hoặc vỡ, làm gián đoạn lưu thông máu đến não, gây tổn thương não.

            **⚠️ Đặc điểm:**
            - Cấp cứu y tế! Thời gian = Não
            - Có thể gây tử vong hoặc tàn tật vĩnh viễn
            - Phát hiện và điều trị sớm → Giảm tổn thương

            **Có 2 loại:**
            - **Đột quỵ thiếu máu cục bộ (80%):** Tắc mạch máu não
            - **Đột quỵ xuất huyết (20%):** Vỡ mạch máu não

            ## Triệu chứng (FAST):

            **⚠️ QUAN TRỌNG:** Nhận biết sớm triệu chứng → Cứu sống!

            **F - Face (Mặt):**
            - Mặt lệch một bên
            - Miệng méo
            - Không cười được đều

            **A - Arms (Tay):**
            - Yếu hoặc tê liệt một bên tay/chân
            - Không giơ được tay lên
            - Rơi đồ vật

            **S - Speech (Lời nói):**
            - Nói khó, nói ngọng
            - Không hiểu lời nói
            - Nói lắp, nói không rõ

            **T - Time (Thời gian):**
            - **Gọi cấp cứu ngay!** (115)
            - Thời gian = Não
            - Điều trị trong 4.5 giờ đầu → Hiệu quả tốt nhất

            **Triệu chứng khác:**
            - Mất thị lực một hoặc cả hai mắt
            - Chóng mặt, mất thăng bằng
            - Đau đầu dữ dội, đột ngột
            - Lú lẫn, mất trí nhớ
            - Khó nuốt

            ## Nguyên nhân:

            **1. Đột quỵ thiếu máu cục bộ:**
            - **Cục máu đông:** Hình thành trong mạch máu não
            - **Cục máu đông từ nơi khác:** Tim, động mạch cảnh → Di chuyển lên não
            - **Hẹp mạch máu:** Xơ vữa động mạch

            **2. Đột quỵ xuất huyết:**
            - **Tăng huyết áp:** Vỡ mạch máu nhỏ
            - **Dị dạng mạch máu:** Phình mạch, dị dạng động-tĩnh mạch
            - **Chấn thương**

            **3. Yếu tố nguy cơ:**
            - **Tăng huyết áp:** Nguy cơ cao nhất
            - **Đái tháo đường**
            - **Rối loạn mỡ máu:** Cholesterol cao
            - **Hút thuốc lá**
            - **Rượu bia:** Uống nhiều
            - **Béo phì, ít vận động**
            - **Rung nhĩ:** Tạo cục máu đông
            - **Tuổi cao:** > 55 tuổi
            - **Tiền sử gia đình**

            ## Chẩn đoán:

            **1. Khám lâm sàng:**
            - Đánh giá triệu chứng
            - Kiểm tra thần kinh
            - Đo huyết áp, nhịp tim

            **2. Chụp CT/MRI não:**
            - Xác định loại đột quỵ
            - Vị trí tổn thương
            - Mức độ tổn thương

            **3. Xét nghiệm:**
            - Công thức máu
            - Đường huyết
            - Chức năng đông máu
            - Lipid máu

            **4. Siêu âm:**
            - Siêu âm động mạch cảnh
            - Siêu âm tim (tìm cục máu đông)

            ## Điều trị:

            **1. Cấp cứu (Trong 4.5 giờ đầu):**
            - **Thuốc tiêu sợi huyết (tPA):** Cho đột quỵ thiếu máu
              - Phải trong 4.5 giờ đầu
              - Phá vỡ cục máu đông
              - **⚠️ QUAN TRỌNG:** Càng sớm càng tốt!
            - **Lấy huyết khối cơ học:** Dùng ống thông lấy cục máu đông
            - **Phẫu thuật:** Nếu xuất huyết nặng

            **2. Điều trị hỗ trợ:**
            - Kiểm soát huyết áp
            - Kiểm soát đường huyết
            - Chống phù não
            - Phòng ngừa biến chứng

            **3. Phục hồi chức năng:**
            - Vật lý trị liệu
            - Ngôn ngữ trị liệu
            - Hoạt động trị liệu
            - Bắt đầu sớm (sau 24-48 giờ)

            ## 🍽️ CHẾ ĐỘ ĂN SAU ĐỘT QUỴ:

            **1. Nguyên tắc:**
            - **Phòng ngừa tái phát:** Quan trọng nhất!
            - **Giảm muối:** < 5g/ngày
            - **Giảm chất béo bão hòa:** Giảm cholesterol
            - **Tăng rau xanh, trái cây:** Chất xơ, vitamin
            - **Đủ protein:** Giúp phục hồi

            **2. Thực phẩm NÊN ĂN:**
            - **Rau xanh:** Nhiều (rau cải, rau muống, bông cải)
            - **Trái cây:** Tất cả (cam, bưởi, táo, chuối)
            - **Cá:** Cá hồi, cá thu (omega-3, 2-3 lần/tuần)
            - **Thịt nạc:** Thịt gà (bỏ da), thịt bò nạc
            - **Ngũ cốc nguyên hạt:** Gạo lứt, yến mạch, bánh mì đen
            - **Đậu, đậu phụ:** Protein thực vật
            - **Sữa ít béo:** Sữa tách béo, sữa chua
            - **Dầu thực vật:** Dầu ô liu, dầu hạt cải

            **3. Thực phẩm CẦN TRÁNH:**
            - **Muối nhiều:** Dưa muối, cà muối, đồ hộp, thức ăn nhanh
            - **Chất béo bão hòa:** Mỡ động vật, thịt mỡ, bơ
            - **Thực phẩm chế biến sẵn:** Xúc xích, thịt nguội, đồ hộp
            - **Đồ chiên rán:** Nhiều dầu mỡ
            - **Rượu bia:** Hạn chế tối đa
            - **Đường nhiều:** Bánh kẹo, nước ngọt

            **4. Thực đơn mẫu (1 ngày):**
            - **Sáng:** Cháo yến mạch + 1 quả trứng luộc + sữa ít béo
            - **Trưa:** 1 chén cơm gạo lứt + cá hấp + rau luộc + canh rau
            - **Tối:** 1 chén cơm gạo lứt + thịt gà luộc (bỏ da) + rau xào (ít dầu) + canh
            - **Bữa phụ:** Trái cây, sữa chua

            **5. Lưu ý khi ăn (Nếu có khó nuốt):**
            - Ăn thức ăn mềm, dễ nuốt
            - Ăn chậm, nhai kỹ
            - Ngồi thẳng khi ăn
            - Nghỉ giữa các miếng ăn
            - Uống nước sau ăn (tránh sặc)

            ## 🏃 TẬP THỂ DỤC SAU ĐỘT QUỴ:

            **⚠️ QUAN TRỌNG:** Phục hồi chức năng bắt đầu sớm (sau 24-48 giờ)!

            **1. Vật lý trị liệu:**
            - **Bắt đầu:** Sau 24-48 giờ (nếu ổn định)
            - **Tần suất:** Hàng ngày, có hướng dẫn
            - **Mục tiêu:** Phục hồi vận động, thăng bằng

            **2. Tập vận động:**
            - **Tập tay/chân yếu:** Cử động thụ động → Chủ động
            - **Tập đi:** Với nạng, khung tập đi
            - **Tập thăng bằng:** Ngồi, đứng
            - **Tập phối hợp:** Tay-mắt, tay-chân

            **3. Tập tại nhà:**
            - **Đi bộ:** Bắt đầu 5-10 phút, tăng dần
            - **Tập tay:** Nâng tạ nhẹ, tập với dây kháng lực
            - **Tập thăng bằng:** Đứng một chân, đi trên đường thẳng
            - **Yoga, thái cực quyền:** Nhẹ nhàng, thư giãn

            **4. Lưu ý:**
            - Tập vừa sức, không gắng sức
            - Nghỉ khi mệt
            - Có người hỗ trợ khi cần
            - Dừng ngay nếu: Đau ngực, chóng mặt, khó thở

            **5. Lợi ích:**
            - Phục hồi chức năng vận động
            - Giảm co cứng cơ
            - Tăng sức mạnh
            - Cải thiện thăng bằng
            - Phòng ngừa tái phát

            ## 🛡️ PHÒNG NGỪA TÁI PHÁT:

            **1. Kiểm soát huyết áp:**
            - **Mục tiêu:** < 130/80 mmHg
            - Đo huyết áp hàng ngày
            - Uống thuốc đúng giờ
            - Chế độ ăn ít muối

            **2. Kiểm soát đường huyết:**
            - Nếu có đái tháo đường
            - HbA1c < 7%
            - Chế độ ăn phù hợp

            **3. Kiểm soát cholesterol:**
            - LDL < 100 mg/dL (hoặc < 70 nếu nguy cơ cao)
            - Chế độ ăn ít chất béo bão hòa
            - Uống thuốc statin (nếu cần)

            **4. Bỏ thuốc lá:**
            - Hút thuốc → Tăng nguy cơ đột quỵ 2-4 lần
            - Bỏ thuốc → Giảm nguy cơ đáng kể

            **5. Hạn chế rượu bia:**
            - **Nam:** Tối đa 2 ly/ngày
            - **Nữ:** Tối đa 1 ly/ngày
            - Hoặc bỏ hoàn toàn (tốt nhất)

            **6. Tập thể dục:**
            - 30 phút/ngày, ít nhất 5 ngày/tuần
            - Đi bộ, bơi, đạp xe
            - Vừa phải, không gắng sức

            **7. Giảm cân:**
            - Nếu thừa cân
            - BMI 18.5-24.9
            - Giảm từ từ

            **8. Uống thuốc đúng giờ:**
            - **Aspirin:** Phòng ngừa (nếu bác sĩ chỉ định)
            - **Thuốc huyết áp:** Hàng ngày
            - **Statin:** Giảm cholesterol
            - **Không tự ý ngừng!**

            ## 🚨 KHI NÀO CẦN CẤP CỨU:

            **Dấu hiệu đột quỵ (FAST):**
            - **F - Face:** Mặt lệch
            - **A - Arms:** Tay yếu
            - **S - Speech:** Nói khó
            - **T - Time:** Gọi cấp cứu ngay!

            **Triệu chứng khác:**
            - Mất thị lực đột ngột
            - Chóng mặt, mất thăng bằng
            - Đau đầu dữ dội, đột ngột
            - Lú lẫn, mất trí nhớ

            **⚠️ QUAN TRỌNG:**
            - **Gọi cấp cứu ngay:** 115
            - **Không tự lái xe:** Nguy hiểm!
            - **Ghi nhớ thời gian:** Khi nào bắt đầu triệu chứng
            - **Thời gian = Não:** Càng sớm càng tốt!

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Phòng ngừa:**
            - Kiểm soát các yếu tố nguy cơ
            - Chế độ ăn lành mạnh
            - Tập thể dục đều đặn
            - Không hút thuốc
            - Khám sức khỏe định kỳ

            **2. Sau đột quỵ:**
            - Tuân thủ điều trị
            - Phục hồi chức năng tích cực
            - Phòng ngừa tái phát
            - Hỗ trợ từ gia đình

            **3. Hỗ trợ:**
            - Nói với gia đình về bệnh
            - Tham gia nhóm hỗ trợ (nếu có)
            - Tâm lý trị liệu nếu cần

            **4. Sống tích cực:**
            - Đột quỵ có thể phục hồi
            - Phục hồi chức năng tích cực → Cải thiện đáng kể
            - Đừng từ bỏ hy vọng
            """,
            related_disease="stroke",
            related_drugs=["Aspirin", "tPA", "Atorvastatin"],
            printable=True
        ),

        PatientEducationTopic(
            id="myocardial_infarction_basics",
            title="Understanding Myocardial Infarction",
            title_vn="Hiểu về Nhồi máu cơ tim",
            category="Disease",
            content="""
            # Hiểu về Nhồi máu cơ tim

            ## Nhồi máu cơ tim là gì?

            Nhồi máu cơ tim (Heart Attack) xảy ra khi động mạch vành (mạch máu nuôi tim) bị tắc nghẽn hoàn toàn, làm một phần cơ tim bị chết do thiếu máu.

            **⚠️ Đặc điểm:**
            - Cấp cứu y tế! Thời gian = Cơ tim
            - Có thể gây tử vong nếu không điều trị kịp thời
            - Phát hiện và điều trị sớm → Giảm tổn thương cơ tim

            **Cơ chế:**
            - Mảng xơ vữa vỡ → Hình thành cục máu đông
            - Cục máu đông tắc động mạch vành
            - Cơ tim thiếu máu → Chết

            ## Triệu chứng:

            **⚠️ QUAN TRỌNG:** Nhận biết sớm triệu chứng → Cứu sống!

            **Triệu chứng điển hình:**
            - **Đau ngực:**
              - Đau sau xương ức, đau dữ dội
              - Cảm giác bóp nghẹt, đè ép
              - Đau lan ra tay trái, cổ, hàm, lưng
              - Đau kéo dài > 20 phút
              - Không giảm khi nghỉ
            - **Khó thở:** Thở nhanh, nông
            - **Vã mồ hôi:** Mồ hôi lạnh
            - **Buồn nôn, nôn:** Có thể có
            - **Chóng mặt, choáng váng**

            **Triệu chứng không điển hình (Ở nữ, người già, đái tháo đường):**
            - Đau ngực nhẹ hoặc không đau
            - Mệt mỏi cực độ
            - Khó thở
            - Đau bụng trên
            - Lú lẫn

            **⚠️ Lưu ý:** Không phải ai cũng có triệu chứng điển hình! Đặc biệt ở nữ và người đái tháo đường.

            ## Nguyên nhân:

            **1. Nguyên nhân chính:**
            - **Xơ vữa động mạch vành:**
              - Mảng xơ vữa tích tụ trong động mạch vành
              - Mảng xơ vữa vỡ → Hình thành cục máu đông
              - Cục máu đông tắc động mạch

            **2. Yếu tố nguy cơ:**
            - **Tăng huyết áp:** Tổn thương mạch máu
            - **Đái tháo đường:** Tổn thương mạch máu
            - **Rối loạn mỡ máu:** Cholesterol cao
            - **Hút thuốc lá:** Tổn thương mạch máu, tăng đông máu
            - **Béo phì, ít vận động**
            - **Tuổi cao:** > 55 tuổi (nam), > 65 tuổi (nữ)
            - **Tiền sử gia đình:** Có người thân bị nhồi máu cơ tim
            - **Stress:** Làm tăng nguy cơ

            ## Chẩn đoán:

            **1. Điện tâm đồ (ECG):**
            - Thay đổi sóng ST-T
            - Phát hiện nhồi máu
            - Xác định vị trí

            **2. Xét nghiệm máu:**
            - **Troponin:** Tăng (dấu hiệu tổn thương cơ tim)
            - **CK-MB:** Tăng
            - **BNP:** Đánh giá suy tim

            **3. Siêu âm tim:**
            - Đánh giá chức năng tim
            - Vùng cơ tim bị tổn thương

            **4. Chụp động mạch vành:**
            - Xem vị trí tắc nghẽn
            - Có thể can thiệp ngay

            ## Điều trị:

            **⚠️ CẤP CỨU:** Điều trị càng sớm càng tốt!

            **1. Điều trị cấp cứu (Trong bệnh viện):**
            - **Thông mạch vành:**
              - **Nong mạch + đặt stent:** Mở động mạch bị tắc
              - **Tốt nhất:** Trong 90 phút đầu (golden hour)
            - **Thuốc tiêu sợi huyết:** Nếu không có can thiệp
            - **Thuốc chống đông:** Aspirin, Clopidogrel
            - **Thuốc giảm đau:** Morphine
            - **Oxy:** Nếu thiếu oxy

            **2. Điều trị sau nhồi máu:**
            - **Thuốc:**
              - **Aspirin:** Phòng ngừa tái phát
              - **Clopidogrel:** Chống đông
              - **Statin:** Giảm cholesterol
              - **ACE inhibitors:** Bảo vệ tim
              - **Beta-blockers:** Giảm nhịp tim, bảo vệ tim
            - **⚠️ QUAN TRỌNG:** Uống đúng giờ, đủ liều, không tự ý ngừng!

            **3. Phục hồi chức năng tim:**
            - Bắt đầu sớm (sau 1-2 ngày)
            - Tập thể dục có hướng dẫn
            - Giáo dục về bệnh
            - Tư vấn dinh dưỡng

            ## 🍽️ CHẾ ĐỘ ĂN SAU NHỒI MÁU CƠ TIM:

            **⚠️ QUAN TRỌNG:** Chế độ ăn giúp phòng ngừa tái phát!

            **1. Nguyên tắc:**
            - **Giảm chất béo bão hòa:** Giảm cholesterol
            - **Giảm muối:** < 5g/ngày (kiểm soát huyết áp)
            - **Tăng chất xơ:** Rau xanh, trái cây
            - **Chất béo tốt:** Omega-3
            - **Đủ protein:** Thịt nạc, cá

            **2. Thực phẩm NÊN ĂN:**
            - **Cá béo:** Cá hồi, cá thu, cá trích (omega-3, 2-3 lần/tuần)
            - **Rau xanh:** Nhiều (rau cải, rau muống, bông cải)
            - **Trái cây:** Tất cả (cam, bưởi, táo, chuối)
            - **Ngũ cốc nguyên hạt:** Gạo lứt, yến mạch, bánh mì đen
            - **Thịt nạc:** Thịt gà (bỏ da), thịt bò nạc (ít)
            - **Đậu, đậu phụ:** Protein thực vật
            - **Sữa ít béo:** Sữa tách béo, sữa chua
            - **Dầu thực vật:** Dầu ô liu, dầu hạt cải
            - **Các loại hạt:** Hạnh nhân, óc chó (nếu có)

            **3. Thực phẩm CẦN TRÁNH:**
            - **Chất béo bão hòa:** Mỡ động vật, thịt mỡ, bơ
            - **Chất béo trans:** Đồ chiên rán, bánh kẹo công nghiệp
            - **Muối nhiều:** Dưa muối, đồ hộp, thức ăn nhanh
            - **Thực phẩm chế biến sẵn:** Xúc xích, thịt nguội
            - **Đường nhiều:** Bánh kẹo, nước ngọt
            - **Rượu bia:** Hạn chế tối đa

            **4. Thực đơn mẫu (1 ngày):**
            - **Sáng:** Cháo yến mạch + 1 quả trứng luộc + sữa ít béo
            - **Trưa:** 1 chén cơm gạo lứt + cá hồi hấp + rau luộc + canh rau
            - **Tối:** 1 chén cơm gạo lứt + thịt gà luộc (bỏ da) + rau xào (dầu ô liu) + canh
            - **Bữa phụ:** Trái cây, các loại hạt, sữa chua

            ## 🏃 TẬP THỂ DỤC SAU NHỒI MÁU CƠ TIM:

            **⚠️ QUAN TRỌNG:** Phục hồi chức năng tim bắt đầu sớm (sau 1-2 ngày)!

            **1. Phục hồi chức năng tim:**
            - **Bắt đầu:** Sau 1-2 ngày (nếu ổn định)
            - **Có hướng dẫn:** Nhân viên y tế
            - **Tăng dần:** Từ nhẹ đến vừa phải

            **2. Tập thể dục:**
            - **Đi bộ:** Bắt đầu 5-10 phút, tăng dần đến 30-45 phút
            - **Đạp xe:** Tại chỗ hoặc ngoài trời
            - **Bơi lội:** (Nếu được phép)
            - **Tần suất:** Hàng ngày hoặc ít nhất 5 ngày/tuần
            - **Cường độ:** Vừa phải (có thể nói chuyện)

            **3. Lưu ý:**
            - Khởi động 5-10 phút
            - Dừng ngay nếu: Đau ngực, khó thở, chóng mặt
            - Nghỉ giữa các bài tập
            - Giãn cơ sau tập
            - Đo huyết áp, nhịp tim trước và sau

            **4. Tránh:**
            - Tập quá sức
            - Tập khi mệt, đau ngực
            - Tập khi thời tiết quá nóng/lạnh
            - Tập ngay sau ăn

            **5. Lợi ích:**
            - Phục hồi chức năng tim
            - Giảm nguy cơ tái phát
            - Tăng sức khỏe tim mạch
            - Cải thiện chất lượng sống

            ## 🛡️ PHÒNG NGỪA TÁI PHÁT:

            **1. Kiểm soát các yếu tố nguy cơ:**
            - **Huyết áp:** < 130/80 mmHg
            - **Đường huyết:** HbA1c < 7% (nếu có đái tháo đường)
            - **Cholesterol:** LDL < 70 mg/dL (hoặc < 100)
            - **Cân nặng:** BMI 18.5-24.9

            **2. Bỏ thuốc lá:**
            - Hút thuốc → Tăng nguy cơ tái phát 2-3 lần
            - Bỏ thuốc → Giảm nguy cơ đáng kể

            **3. Tập thể dục:**
            - 30 phút/ngày, ít nhất 5 ngày/tuần
            - Đi bộ, bơi, đạp xe
            - Vừa phải, không gắng sức

            **4. Chế độ ăn:**
            - Giảm chất béo bão hòa
            - Giảm muối
            - Tăng rau xanh, trái cây
            - Cá béo 2-3 lần/tuần

            **5. Uống thuốc đúng giờ:**
            - **Aspirin:** Hàng ngày (phòng ngừa)
            - **Statin:** Giảm cholesterol
            - **ACE inhibitors:** Bảo vệ tim
            - **Beta-blockers:** Bảo vệ tim
            - **⚠️ KHÔNG tự ý ngừng!**

            **6. Quản lý stress:**
            - Stress làm tăng nguy cơ
            - Tập thư giãn: Hít thở sâu, thiền, yoga
            - Ngủ đủ giấc

            **7. Khám định kỳ:**
            - Mỗi 1-3 tháng: Đo huyết áp, đánh giá
            - Mỗi 6 tháng - 1 năm: Xét nghiệm máu, siêu âm tim

            ## 🚨 KHI NÀO CẦN CẤP CỨU:

            **Dấu hiệu nhồi máu cơ tim:**
            - **Đau ngực:** Đau dữ dội, sau xương ức, lan ra tay, cổ, hàm
            - **Khó thở:** Thở nhanh, nông
            - **Vã mồ hôi:** Mồ hôi lạnh
            - **Buồn nôn, nôn**
            - **Chóng mặt, choáng váng**

            **⚠️ QUAN TRỌNG:**
            - **Gọi cấp cứu ngay:** 115
            - **Không tự lái xe:** Nguy hiểm!
            - **Ghi nhớ thời gian:** Khi nào bắt đầu đau
            - **Thời gian = Cơ tim:** Càng sớm càng tốt!

            **⚠️ Lưu ý:** Không phải ai cũng có triệu chứng điển hình! Đặc biệt ở nữ và người đái tháo đường.

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Phòng ngừa:**
            - Kiểm soát các yếu tố nguy cơ
            - Chế độ ăn lành mạnh
            - Tập thể dục đều đặn
            - Không hút thuốc
            - Khám sức khỏe định kỳ

            **2. Sau nhồi máu cơ tim:**
            - Tuân thủ điều trị nghiêm ngặt
            - Phục hồi chức năng tích cực
            - Phòng ngừa tái phát
            - Hỗ trợ từ gia đình

            **3. Nhận biết sớm:**
            - Biết triệu chứng
            - Gọi cấp cứu ngay khi có dấu hiệu
            - Không chờ đợi

            **4. Sống tích cực:**
            - Nhồi máu cơ tim có thể phục hồi
            - Tuân thủ điều trị → Sống khỏe mạnh
            - Đừng để bệnh ảnh hưởng cuộc sống
            """,
            related_disease="myocardial_infarction",
            related_drugs=["Aspirin", "Atorvastatin", "Metoprolol"],
            printable=True
        ),

        PatientEducationTopic(
            id="atrial_fibrillation_basics",
            title="Understanding Atrial Fibrillation",
            title_vn="Hiểu về Rung nhĩ",
            category="Disease",
            content="""
            # Hiểu về Rung nhĩ

            ## Rung nhĩ là gì?

            Rung nhĩ là rối loạn nhịp tim phổ biến nhất, đặc trưng bởi nhịp tim không đều, nhanh. Bệnh tăng nguy cơ đột quỵ và suy tim, rất phổ biến ở người cao tuổi.

            **⚠️ Đặc điểm:**
            - Rối loạn nhịp tim phổ biến nhất
            - Nhịp tim không đều, nhanh
            - Tăng nguy cơ đột quỵ (5 lần)
            - Phổ biến ở người cao tuổi (> 65 tuổi)

            **Phân loại:**
            - **Paroxysmal:** Tự hết trong 7 ngày
            - **Persistent:** Kéo dài > 7 ngày
            - **Permanent:** Không thể chuyển nhịp

            ## Triệu chứng:

            **Triệu chứng điển hình:**
            - **Đánh trống ngực:** Cảm giác tim đập nhanh, không đều
            - **Khó thở:** Khi gắng sức
            - **Mệt mỏi, suy nhược**
            - **Chóng mặt, choáng váng**
            - **Đau ngực:** Có thể có

            **Triệu chứng khác:**
            - Ngất xỉu (hiếm)
            - Đi tiểu nhiều (do tăng ANP)

            **⚠️ Không có triệu chứng:**
            - Nhiều người không có triệu chứng
            - Phát hiện khi khám sức khỏe

            **⚠️ Biến chứng:**
            - Đột quỵ (nguy hiểm nhất!)
            - Suy tim
            - Rối loạn nhịp tim khác

            ## Nguyên nhân:

            **1. Bệnh tim:**
            - Bệnh mạch vành
            - Suy tim
            - Bệnh van tim

            **2. Tăng huyết áp:**
            - Nguyên nhân phổ biến

            **3. Yếu tố khác:**
            - Cường giáp
            - Bệnh phổi mạn tính
            - Rượu bia
            - Tuổi cao

            ## Chẩn đoán:

            **Xét nghiệm:**
            - **ECG:** Nhịp không đều, không có sóng P
            - **Holter ECG:** Ghi 24-48 giờ
            - Siêu âm tim
            - Xét nghiệm chức năng tuyến giáp

            ## Điều trị:

            **1. Chống đông (quan trọng!):**
            - **Warfarin hoặc DOAC:** Phòng ngừa đột quỵ
            - **CHADS2-VASc score:** Đánh giá nguy cơ đột quỵ
            - **Quan trọng:** Uống đều đặn, theo dõi INR (nếu Warfarin)

            **2. Kiểm soát nhịp tim:**
            - **Beta-blocker:** Metoprolol, Bisoprolol
            - **Calcium channel blocker:** Diltiazem, Verapamil
            - **Digoxin:** Nếu suy tim

            **3. Chuyển nhịp:**
            - **Thuốc:** Amiodarone, Flecainide
            - **Sốc điện:** Nếu cấp cứu
            - **Ablation:** Nếu kháng thuốc

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Nên ăn:**
            - Chế độ ăn bình thường, đủ dinh dưỡng
            - Protein: Thịt, cá, trứng
            - Rau xanh, trái cây
            - Uống đủ nước

            **2. Tránh:**
            - **Rượu bia:** Kích thích rung nhĩ
            - **Caffeine quá nhiều:** Có thể kích thích
            - **Đồ mặn:** Nếu tăng huyết áp

            **3. Lưu ý với Warfarin:**
            - **Vitamin K:** Tránh thay đổi đột ngột (rau xanh, gan)
            - Ăn đều đặn, không thay đổi chế độ ăn đột ngột

            **4. Thực đơn mẫu:**
            - **Sáng:** Cháo/cơm, thịt/cá, rau
            - **Trưa:** Cơm, thịt/cá, rau xanh, canh
            - **Chiều:** Cơm, thịt/cá, rau xanh, canh
            - **Bữa phụ:** Trái cây, sữa

            ## 🏃 TẬP THỂ DỤC:

            **1. Nên tập:**
            - Tập thể dục đều đặn (cải thiện sức khỏe tim)
            - Đi bộ, chạy bộ, bơi lội
            - 30 phút/ngày, 5 ngày/tuần

            **2. Lưu ý:**
            - Tránh gắng sức quá mức (có thể kích thích rung nhĩ)
            - Nghỉ ngơi nếu đánh trống ngực
            - Theo dõi nhịp tim khi tập

            ## 💊 QUẢN LÝ THUỐC:

            **1. Chống đông:**
            - **Warfarin:** Uống đều đặn, theo dõi INR mỗi 2-4 tuần
            - **DOAC (Dabigatran, Rivaroxaban, Apixaban):** Uống đều đặn, không cần theo dõi INR
            - **Quan trọng:** Uống đều đặn, không tự ý ngừng

            **2. Kiểm soát nhịp tim:**
            - Beta-blocker: Uống đều đặn
            - Không ngừng đột ngột

            **3. Tác dụng phụ:**
            - **Warfarin:** Chảy máu (nếu INR cao)
            - **Beta-blocker:** Mệt mỏi, chóng mặt

            **4. Lưu ý:**
            - Báo bác sĩ tất cả thuốc đang dùng
            - Tránh thuốc tương tác

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Đột quỵ:**
            - Yếu liệt một bên
            - Nói khó
            - **Cấp cứu ngay!**

            **2. Rung nhĩ nhanh:**
            - Nhịp tim > 150 lần/phút
            - Khó thở nặng
            - Đau ngực

            **3. Chảy máu:**
            - Chảy máu nhiều (nếu dùng chống đông)
            - Nôn ra máu, đi ngoài phân đen

            ## 💡 PHÒNG NGỪA:

            **1. Kiểm soát yếu tố nguy cơ:**
            - Kiểm soát huyết áp
            - Kiểm soát đái tháo đường
            - Điều trị bệnh tim

            **2. Lối sống:**
            - Hạn chế rượu bia
            - Tập thể dục đều đặn
            - Giảm cân nếu béo phì

            **3. Khám định kỳ:**
            - Nếu có yếu tố nguy cơ
            - ECG định kỳ

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Khi bị rung nhĩ:**
            - Uống thuốc chống đông đều đặn (quan trọng!)
            - Kiểm soát nhịp tim
            - Khám định kỳ

            **2. Chống đông:**
            - Uống đều đặn, đúng giờ
            - Theo dõi INR (nếu Warfarin)
            - Báo bác sĩ nếu chảy máu

            **3. Sống tích cực:**
            - Rung nhĩ có thể kiểm soát
            - Điều trị đúng → Giảm nguy cơ đột quỵ
            - Có thể sống bình thường

            **4. Theo dõi:**
            - Khám định kỳ 3-6 tháng
            - Theo dõi INR (nếu Warfarin)
            - Siêu âm tim định kỳ
            """,
            related_disease="atrial_fibrillation",
            related_drugs=["Warfarin", "Dabigatran", "Rivaroxaban", "Apixaban", "Metoprolol", "Bisoprolol", "Amiodarone"],
            printable=True
        ),

        PatientEducationTopic(
            id="coronary_artery_disease_basics",
            title="Understanding Coronary Artery Disease",
            title_vn="Hiểu về Bệnh mạch vành",
            category="Disease",
            content="""
            # Hiểu về Bệnh mạch vành

            ## Bệnh mạch vành là gì?

            Bệnh mạch vành là tình trạng hẹp hoặc tắc nghẽn động mạch vành do xơ vữa động mạch, dẫn đến thiếu máu cơ tim. Bệnh rất phổ biến, là nguyên nhân tử vong hàng đầu.

            **⚠️ Đặc điểm:**
            - Hẹp/tắc động mạch vành
            - Thiếu máu cơ tim
            - Nguyên nhân tử vong hàng đầu
            - Rất phổ biến (đặc biệt nam > 45 tuổi)

            **Phân loại:**
            - **Đau thắt ngực ổn định:** Đau khi gắng sức, giảm khi nghỉ
            - **Hội chứng vành cấp:** Đau ngực không ổn định, nhồi máu cơ tim

            ## Triệu chứng:

            **Đau thắt ngực ổn định:**
            - **Đau ngực:** Đau thắt, đè ép, sau xương ức
            - **Lan ra:** Cánh tay trái, hàm, lưng
            - **Khi gắng sức:** Leo cầu thang, đi bộ nhanh
            - **Giảm khi nghỉ:** Hoặc dùng Nitrate
            - **Kéo dài:** 2-10 phút

            **Triệu chứng khác:**
            - Khó thở khi gắng sức
            - Mệt mỏi
            - Đổ mồ hôi
            - Buồn nôn

            **⚠️ Hội chứng vành cấp:**
            - Đau ngực dữ dội, kéo dài
            - Không giảm khi nghỉ
            - **Cấp cứu ngay!**

            **⚠️ Thiếu máu cơ tim thầm lặng:**
            - Không có triệu chứng
            - Phát hiện khi khám sức khỏe

            ## Nguyên nhân:

            **1. Xơ vữa động mạch:**
            - Mảng xơ vữa tích tụ trong động mạch vành
            - Hẹp dần → Thiếu máu cơ tim

            **2. Yếu tố nguy cơ:**
            - **Không thay đổi được:** Tuổi cao, nam giới, tiền sử gia đình
            - **Thay đổi được:**
              - Tăng huyết áp
              - Đái tháo đường
              - Rối loạn lipid máu
              - Hút thuốc
              - Béo phì
              - Ít vận động

            ## Chẩn đoán:

            **Xét nghiệm:**
            - **ECG:** ST chênh xuống khi gắng sức
            - **Test gắng sức:** Dương tính
            - **Chụp mạch vành:** Chuẩn vàng (hẹp ≥ 50%)
            - **CT mạch vành:** Nếu phù hợp

            ## Điều trị:

            **1. Thuốc:**
            - **Aspirin:** 75-100mg/ngày (phòng ngừa huyết khối)
            - **Statin:** Atorvastatin 40-80mg (giảm cholesterol)
            - **Beta-blocker:** Giảm nhịp tim, giảm nhu cầu oxy
            - **ACE inhibitor:** Nếu có suy tim, đái tháo đường
            - **Nitrate:** Giảm đau ngực

            **2. Can thiệp:**
            - **PCI (đặt stent):** Nếu hẹp nặng
            - **CABG (bắc cầu):** Nếu nhiều nhánh hẹp

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Chế độ ăn tim mạch:**
            - **Giảm chất béo bão hòa:** Thịt đỏ, mỡ động vật
            - **Tăng chất béo không bão hòa:** Cá béo, dầu ô liu, hạt
            - **Giảm muối:** < 5g/ngày
            - **Tăng chất xơ:** Rau xanh, trái cây, ngũ cốc nguyên hạt

            **2. Thực phẩm tốt:**
            - **Cá béo:** Cá hồi, cá thu (omega-3)
            - **Rau xanh, trái cây:** Chống oxy hóa
            - **Ngũ cốc nguyên hạt:** Yến mạch, gạo lứt
            - **Hạt:** Hạnh nhân, óc chó

            **3. Tránh:**
            - Thịt đỏ, mỡ động vật
            - Đồ chế biến sẵn
            - Đồ ngọt, nước ngọt
            - Rượu bia (hạn chế)

            **4. Thực đơn mẫu:**
            - **Sáng:** Cháo yến mạch, trứng, trái cây
            - **Trưa:** Cơm, cá, rau xanh, canh (không mặn)
            - **Chiều:** Cơm, thịt gà/cá, rau xanh, canh
            - **Bữa phụ:** Trái cây, hạt

            ## 🏃 TẬP THỂ DỤC:

            **1. Quan trọng!**
            - Tập thể dục đều đặn (cải thiện sức khỏe tim)
            - Tăng cường mạch máu phụ
            - Giảm nguy cơ biến cố

            **2. Loại bài tập:**
            - **Đi bộ:** 30 phút/ngày, 5 ngày/tuần
            - **Chạy bộ:** Nếu sức khỏe cho phép
            - **Bơi lội:** Tốt cho tim
            - **Đạp xe:** Tăng cường tim

            **3. Lưu ý:**
            - Khởi động kỹ
            - Tránh gắng sức quá mức (gây đau ngực)
            - Nghỉ ngơi nếu đau ngực
            - Mang Nitrate khi tập (nếu có chỉ định)

            ## 💊 QUẢN LÝ THUỐC:

            **1. Aspirin:**
            - 75-100mg/ngày
            - Uống sau ăn (tránh đau dạ dày)
            - **Quan trọng:** Uống đều đặn

            **2. Statin:**
            - Atorvastatin 40-80mg
            - Uống buổi tối
            - Theo dõi chức năng gan, cơ

            **3. Beta-blocker:**
            - Uống đều đặn
            - Không ngừng đột ngột

            **4. Nitrate:**
            - Dùng khi đau ngực
            - Ngậm dưới lưỡi (nhanh)
            - Hoặc uống (tác dụng kéo dài)

            **5. Lưu ý:**
            - Uống đều đặn, đúng giờ
            - Không tự ý ngừng
            - Báo bác sĩ nếu có tác dụng phụ

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Đau ngực không ổn định:**
            - Đau ngực dữ dội, kéo dài
            - Không giảm khi nghỉ hoặc dùng Nitrate
            - **Cấp cứu ngay!**

            **2. Nhồi máu cơ tim:**
            - Đau ngực dữ dội
            - Vã mồ hôi
            - Khó thở
            - **Gọi 115 ngay!**

            **3. Tác dụng phụ thuốc:**
            - Đau cơ (Statin)
            - Chảy máu (Aspirin)
            - Chóng mặt nặng (Beta-blocker)

            ## 💡 PHÒNG NGỪA:

            **1. Kiểm soát yếu tố nguy cơ:**
            - Kiểm soát huyết áp (< 130/80 mmHg)
            - Kiểm soát đái tháo đường (HbA1c < 7%)
            - Kiểm soát cholesterol (LDL < 100 mg/dL)
            - **Bỏ thuốc lá** (quan trọng!)

            **2. Chế độ ăn:**
            - Chế độ ăn tim mạch
            - Giảm muối, chất béo bão hòa
            - Tăng cá béo, rau xanh

            **3. Tập thể dục:**
            - Đều đặn, 30 phút/ngày
            - 5 ngày/tuần

            **4. Thuốc:**
            - Aspirin (nếu có chỉ định)
            - Statin (nếu có nguy cơ)

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Khi bị bệnh mạch vành:**
            - Uống thuốc đều đặn (quan trọng!)
            - Chế độ ăn tim mạch
            - Tập thể dục đều đặn
            - Kiểm soát yếu tố nguy cơ

            **2. Khi đau ngực:**
            - Nghỉ ngơi ngay
            - Dùng Nitrate (nếu có)
            - Gọi cấp cứu nếu không giảm

            **3. Sống tích cực:**
            - Bệnh mạch vành có thể kiểm soát
            - Điều trị đúng → Giảm triệu chứng, biến cố
            - Có thể sống lâu, chất lượng cuộc sống tốt

            **4. Theo dõi:**
            - Khám định kỳ 3-6 tháng
            - Theo dõi cholesterol, huyết áp
            - Test gắng sức định kỳ
            """,
            related_disease="coronary_artery_disease",
            related_drugs=["Aspirin", "Atorvastatin", "Clopidogrel", "ACE Inhibitor", "Beta-blocker", "Nitrate"],
            printable=True
        ),

        PatientEducationTopic(
            id="valvular_heart_disease_basics",
            title="Understanding Valvular Heart Disease",
            title_vn="Hiểu về Bệnh van tim",
            category="Disease",
            content="""
            # Hiểu về Bệnh van tim

            ## Bệnh van tim là gì?

            Bệnh van tim là tình trạng van tim không hoạt động đúng cách, gây hẹp hoặc hở van, ảnh hưởng đến lưu thông máu. Bệnh phổ biến ở Việt Nam, đặc biệt do thấp tim.

            **⚠️ Đặc điểm:**
            - Van tim không hoạt động đúng
            - Hẹp hoặc hở van
            - Ảnh hưởng lưu thông máu
            - Phổ biến do thấp tim ở Việt Nam

            **Phân loại:**
            - **Hẹp van:** Van không mở đủ
            - **Hở van:** Van không đóng kín
            - **Van tim:** Van 2 lá, van 3 lá, van động mạch chủ, van động mạch phổi

            ## Triệu chứng:

            **Triệu chứng điển hình:**
            - **Khó thở:** Khi gắng sức, nặng hơn khi nằm
            - **Mệt mỏi:** Mệt mỏi khi gắng sức
            - **Đau ngực:** Có thể có
            - **Đánh trống ngực:** Nhịp tim không đều
            - **Phù:** Phù chân, mắt cá chân
            - **Ho:** Ho khan, đặc biệt ban đêm

            **Triệu chứng khác:**
            - Chóng mặt, ngất xỉu
            - Đau đầu
            - Tím tái (nếu nặng)

            **⚠️ Biến chứng:**
            - Suy tim
            - Rối loạn nhịp tim
            - Đột quỵ (huyết khối)
            - Viêm nội tâm mạc

            ## Nguyên nhân:

            **1. Thấp tim (phổ biến ở Việt Nam):**
            - Biến chứng của viêm họng do liên cầu khuẩn
            - Gây hẹp/hở van 2 lá, van động mạch chủ

            **2. Nguyên nhân khác:**
            - **Thoái hóa:** Tuổi cao
            - **Bẩm sinh:** Dị tật van tim
            - **Viêm nội tâm mạc:** Nhiễm khuẩn van tim
            - **Nhồi máu cơ tim:** Tổn thương cơ nhú
            - **Bệnh mạch vành:** Thiếu máu cơ tim

            **3. Yếu tố nguy cơ:**
            - Tiền sử thấp tim
            - Tuổi cao
            - Bệnh tim mạch
            - Nhiễm khuẩn

            ## Chẩn đoán:

            **Xét nghiệm:**
            - **Siêu âm tim:** Chuẩn vàng (đánh giá van tim)
            - **ECG:** Rối loạn nhịp tim
            - **X-quang ngực:** Tim to, phù phổi
            - **Chụp mạch vành:** Nếu cần phẫu thuật

            ## Điều trị:

            **1. Thuốc:**
            - **Lợi tiểu:** Furosemide (giảm phù, khó thở)
            - **ACE inhibitor:** Nếu suy tim
            - **Beta-blocker:** Giảm nhịp tim
            - **Chống đông:** Warfarin (nếu rung nhĩ, van cơ học)
            - **Kháng sinh dự phòng:** Nếu có chỉ định

            **2. Phẫu thuật:**
            - **Sửa van:** Nếu có thể
            - **Thay van:** Van cơ học hoặc sinh học
            - **Chỉ định:** Khi triệu chứng nặng, suy tim

            **3. Can thiệp:**
            - **Nong van:** Nếu hẹp van 2 lá
            - **TAVI:** Thay van động mạch chủ qua da

            ## 🍽️ CHẾ ĐỘ ĂN:

            **1. Chế độ ăn tim mạch:**
            - **Giảm muối:** < 5g/ngày (giảm phù)
            - **Giảm chất béo bão hòa:** Thịt đỏ, mỡ động vật
            - **Tăng chất xơ:** Rau xanh, trái cây
            - **Uống đủ nước:** Nhưng không quá nhiều (nếu phù)

            **2. Thực phẩm tốt:**
            - Cá béo (omega-3)
            - Rau xanh, trái cây
            - Ngũ cốc nguyên hạt
            - Hạt

            **3. Tránh:**
            - Đồ mặn
            - Thịt đỏ, mỡ động vật
            - Rượu bia (hạn chế)

            **4. Thực đơn mẫu:**
            - **Sáng:** Cháo/cơm, trứng, trái cây
            - **Trưa:** Cơm, cá, rau xanh, canh (không mặn)
            - **Chiều:** Cơm, thịt gà/cá, rau xanh, canh
            - **Bữa phụ:** Trái cây, hạt

            ## 🏃 TẬP THỂ DỤC:

            **1. Nên tập:**
            - Tập thể dục đều đặn (cải thiện sức khỏe tim)
            - Đi bộ, chạy bộ nhẹ
            - 30 phút/ngày, 5 ngày/tuần

            **2. Lưu ý:**
            - Tránh gắng sức quá mức (gây khó thở)
            - Nghỉ ngơi nếu khó thở, mệt mỏi
            - Theo dõi nhịp tim khi tập

            ## 💊 QUẢN LÝ THUỐC:

            **1. Lợi tiểu:**
            - Furosemide: Uống buổi sáng
            - Theo dõi cân nặng (giảm phù)

            **2. Chống đông:**
            - Warfarin: Uống đều đặn, theo dõi INR
            - DOAC: Nếu có chỉ định

            **3. ACE inhibitor:**
            - Uống đều đặn
            - Theo dõi huyết áp, chức năng thận

            **4. Lưu ý:**
            - Uống đều đặn, đúng giờ
            - Không tự ý ngừng
            - Báo bác sĩ nếu có tác dụng phụ

            ## 🚨 KHI NÀO CẦN ĐẾN BỆNH VIỆN:

            **1. Suy tim nặng:**
            - Khó thở nặng
            - Phù nhiều
            - Không nằm được

            **2. Rối loạn nhịp tim:**
            - Đánh trống ngực nhiều
            - Ngất xỉu

            **3. Đột quỵ:**
            - Yếu liệt một bên
            - Nói khó
            - **Cấp cứu ngay!**

            ## 💡 PHÒNG NGỪA:

            **1. Phòng ngừa thấp tim:**
            - **Điều trị viêm họng do liên cầu:** Kháng sinh đủ liệu trình
            - **Dự phòng thấp tim:** Penicillin dài hạn (nếu có chỉ định)
            - **Vệ sinh:** Giữ vệ sinh cá nhân

            **2. Kiểm soát yếu tố nguy cơ:**
            - Kiểm soát huyết áp
            - Kiểm soát đái tháo đường
            - Điều trị bệnh tim mạch

            **3. Khám định kỳ:**
            - Siêu âm tim định kỳ
            - Theo dõi triệu chứng

            **4. Phòng ngừa viêm nội tâm mạc:**
            - Kháng sinh dự phòng (nếu có chỉ định)
            - Vệ sinh răng miệng

            ## 💡 LỜI KHUYÊN THỰC TẾ:

            **1. Phòng ngừa:**
            - **Điều trị viêm họng do liên cầu** (quan trọng!)
            - Dự phòng thấp tim
            - Vệ sinh cá nhân

            **2. Khi bị bệnh van tim:**
            - Uống thuốc đều đặn
            - Chế độ ăn ít muối
            - Tập thể dục đều đặn
            - Khám định kỳ

            **3. Sống tích cực:**
            - Bệnh van tim có thể kiểm soát
            - Điều trị đúng → Giảm triệu chứng
            - Phẫu thuật → Cải thiện chất lượng cuộc sống

            **4. Theo dõi:**
            - Khám định kỳ 3-6 tháng
            - Siêu âm tim định kỳ
            - Theo dõi triệu chứng
            """,
            related_disease="valvular_heart_disease",
            related_drugs=["Furosemide", "ACE Inhibitor", "Beta-blocker", "Warfarin", "Penicillin"],
            printable=True
        ),

]
