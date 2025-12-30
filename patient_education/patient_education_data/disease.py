"""
Patient Education Topics - Disease
"""

from patient_education.models import PatientEducationTopic


DISEASE_TOPICS = [
    PatientEducationTopic(
            id="diabetes_basics",
            title="Understanding Diabetes",
            title_vn="Hiểu về Đái tháo đường",
            category="Disease",
            content="""
        # Hiểu về Đái tháo đường

        ## Đái tháo đường là gì?

        Đái tháo đường là bệnh mạn tính xảy ra khi cơ thể không thể sử dụng đường (glucose) đúng cách. Đường là nguồn năng lượng chính của cơ thể, được lấy từ thức ăn và được insulin (hormone từ tuyến tụy) giúp đưa vào tế bào để sử dụng.

        **Khi bị đái tháo đường:**
        - Đường tích tụ trong máu → Đường huyết cao
        - Tế bào thiếu năng lượng → Mệt mỏi
        - Gây tổn thương các cơ quan theo thời gian

        ## Có hai loại chính:

        **Đái tháo đường type 1 (10%):**
        - **Nguyên nhân:** Tuyến tụy không sản xuất insulin (do tự miễn)
        - **Độ tuổi:** Thường gặp ở trẻ em, thanh niên (< 30 tuổi)
        - **Triệu chứng:** Khởi phát nhanh, rõ ràng
        - **Điều trị:** Bắt buộc tiêm insulin hàng ngày
        - **Không thể phòng ngừa**

        **Đái tháo đường type 2 (90%):**
        - **Nguyên nhân:** Cơ thể kháng insulin hoặc không sản xuất đủ
        - **Độ tuổi:** Thường gặp ở người lớn (> 40 tuổi), nhưng ngày càng trẻ hóa
        - **Yếu tố nguy cơ:** Béo phì, ít vận động, di truyền, tuổi cao
        - **Triệu chứng:** Khởi phát từ từ, có thể không có triệu chứng
        - **Điều trị:** Thuốc uống, chế độ ăn, tập thể dục, có thể cần insulin
        - **Có thể phòng ngừa** bằng lối sống lành mạnh

        ## Triệu chứng:

        **Triệu chứng điển hình (thường gặp ở type 1 hoặc type 2 nặng):**
        - **Tiểu nhiều:** Đi tiểu nhiều lần, lượng nhiều (do thận cố gắng thải đường)
        - **Khát nhiều:** Uống nước liên tục nhưng vẫn khát
        - **Ăn nhiều nhưng sụt cân:** Cơ thể không sử dụng được đường, đốt mỡ và cơ
        - **Mệt mỏi:** Thiếu năng lượng, uể oải
        - **Nhìn mờ:** Đường huyết cao làm thay đổi hình dạng thủy tinh thể

        **Triệu chứng khác:**
        - Vết thương lâu lành
        - Nhiễm trùng thường xuyên (nhiễm nấm, nhiễm trùng da)
        - Tê bì, ngứa ran ở tay chân (tổn thương thần kinh)
        - Da khô, ngứa

        **⚠️ Lưu ý:** Nhiều người type 2 không có triệu chứng rõ ràng, chỉ phát hiện khi khám sức khỏe định kỳ.

        ## Chẩn đoán:

        **Xét nghiệm đường huyết:**
        - **Đường huyết đói:** ≥ 126 mg/dL (≥ 7.0 mmol/L) - 2 lần
        - **Đường huyết bất kỳ:** ≥ 200 mg/dL (≥ 11.1 mmol/L) + có triệu chứng
        - **HbA1c:** ≥ 6.5% (đường huyết trung bình 3 tháng)
        - **Nghiệm pháp dung nạp glucose:** ≥ 200 mg/dL sau 2 giờ

        ## Điều trị (3 trụ cột):

        **1. Thuốc:**
        - **Type 1:** Insulin (bắt buộc)
        - **Type 2:** 
          - Metformin (thuốc đầu tay)
          - Sulfonylurea, DPP-4 inhibitors, SGLT-2 inhibitors
          - Insulin (nếu thuốc uống không đủ)
        - **Quan trọng:** Uống đúng giờ, đúng liều, không tự ý ngừng

        **2. Chế độ ăn:**
        - Ăn đúng giờ, đều đặn
        - Chọn thực phẩm có chỉ số đường huyết thấp
        - Kiểm soát khẩu phần
        - Xem chi tiết trong topic "Chế độ ăn cho người Đái tháo đường"

        **3. Tập thể dục:**
        - **Loại:** Đi bộ, chạy bộ, bơi lội, đạp xe, yoga
        - **Thời gian:** 30 phút/ngày, ít nhất 5 ngày/tuần
        - **Cường độ:** Vừa phải (có thể nói chuyện khi tập)
        - **Thời điểm:** Sau bữa ăn 1-2 giờ (tránh hạ đường huyết)
        - **Lưu ý:** Đo đường huyết trước và sau tập, mang đường bên người

        ## 🏃 TẬP THỂ DỤC CHI TIẾT:

        **1. Đi bộ (Dễ nhất, phù hợp mọi người):**
        - **Bắt đầu:** 10-15 phút/ngày
        - **Tăng dần:** 30-45 phút/ngày
        - **Tốc độ:** 4-5 km/giờ (hơi nhanh)
        - **Tần suất:** Hàng ngày hoặc ít nhất 5 ngày/tuần
        - **Lợi ích:** Giảm đường huyết, giảm cân, tăng sức khỏe tim mạch

        **2. Chạy bộ (Nếu sức khỏe cho phép):**
        - **Bắt đầu:** 5-10 phút, xen kẽ đi bộ
        - **Tăng dần:** 20-30 phút
        - **Tần suất:** 3-4 lần/tuần
        - **Lưu ý:** Kiểm tra tim mạch trước, mang giày phù hợp

        **3. Bơi lội:**
        - **Thời gian:** 20-30 phút
        - **Tần suất:** 3-4 lần/tuần
        - **Lợi ích:** Toàn thân, ít chấn thương khớp

        **4. Đạp xe:**
        - **Thời gian:** 30-45 phút
        - **Tần suất:** 3-5 lần/tuần
        - **Lợi ích:** Tăng sức mạnh chân, tim mạch

        **5. Tập sức mạnh (Quan trọng!):**
        - **Loại:** Nâng tạ nhẹ, tập với dây kháng lực, bodyweight
        - **Thời gian:** 20-30 phút
        - **Tần suất:** 2-3 lần/tuần (không liên tiếp)
        - **Lợi ích:** Tăng cơ, giảm kháng insulin, tăng chuyển hóa

        **6. Yoga, Thái Cực Quyền:**
        - **Thời gian:** 30-60 phút
        - **Tần suất:** 3-5 lần/tuần
        - **Lợi ích:** Giảm stress, tăng linh hoạt, kiểm soát đường huyết

        **⚠️ Lưu ý khi tập thể dục:**
        - Đo đường huyết trước tập: Nếu < 100 mg/dL → Ăn nhẹ trước
        - Đo đường huyết sau tập: Nếu < 70 mg/dL → Ăn ngay
        - Mang đường bên người (kẹo, nước ngọt)
        - Uống đủ nước
        - Khởi động trước, giãn cơ sau
        - Dừng ngay nếu: Đau ngực, chóng mặt, khó thở nặng

        ## 📊 THEO DÕI VÀ QUẢN LÝ:

        **1. Đo đường huyết tại nhà:**
        - **Type 1:** Trước mỗi bữa ăn, trước khi ngủ, trước/sau tập
        - **Type 2:** Trước bữa sáng, trước bữa tối (hoặc theo chỉ định bác sĩ)
        - **Mục tiêu:**
          - Trước ăn: 80-130 mg/dL (4.4-7.2 mmol/L)
          - Sau ăn 2 giờ: < 180 mg/dL (< 10 mmol/L)
          - Trước ngủ: 100-140 mg/dL (5.6-7.8 mmol/L)

        **2. Xét nghiệm HbA1c:**
        - **Mục tiêu:** < 7% (đường huyết trung bình 3 tháng)
        - **Tần suất:** Mỗi 3-6 tháng
        - **Ý nghĩa:** Đánh giá kiểm soát đường huyết dài hạn

        **3. Khám định kỳ:**
        - **Hàng tháng:** Đo đường huyết, huyết áp, cân nặng
        - **Mỗi 3 tháng:** HbA1c, đánh giá điều trị
        - **Mỗi 6 tháng - 1 năm:**
          - Khám mắt (kiểm tra võng mạc)
          - Xét nghiệm chức năng thận (creatinine, microalbumin)
          - Khám bàn chân (kiểm tra tổn thương thần kinh)
          - Lipid máu, chức năng gan

        **4. Nhật ký quản lý:**
        - Ghi: Đường huyết, thuốc đã uống, thức ăn, tập thể dục
        - Giúp bác sĩ điều chỉnh điều trị tốt hơn

        ## ⚠️ BIẾN CHỨNG NẾU KHÔNG ĐIỀU TRỊ:

        **1. Biến chứng mạch máu nhỏ:**
        - **Mắt (Võng mạc):** Mờ mắt, mù lòa
        - **Thận:** Suy thận, cần lọc thận
        - **Thần kinh:** Tê bì, đau, loét bàn chân

        **2. Biến chứng mạch máu lớn:**
        - **Tim:** Nhồi máu cơ tim, suy tim
        - **Não:** Đột quỵ
        - **Chân:** Tắc mạch, hoại tử, có thể phải cắt cụt

        **3. Biến chứng cấp tính:**
        - **Hạ đường huyết:** Run, đổ mồ hôi, lú lẫn, hôn mê (nguy hiểm!)
        - **Tăng đường huyết cấp:** Nhiễm toan ceton, hôn mê (nguy hiểm!)

        **⚠️ QUAN TRỌNG:** Kiểm soát đường huyết tốt giúp giảm 40-60% nguy cơ biến chứng!

        ## 💡 SINH HOẠT HÀNG NGÀY:

        **1. Giấc ngủ:**
        - Ngủ đủ 7-8 giờ/đêm
        - Giờ ngủ đều đặn
        - Thiếu ngủ làm tăng đường huyết, tăng kháng insulin

        **2. Quản lý stress:**
        - Stress làm tăng đường huyết
        - Tập thư giãn: Hít thở sâu, thiền, yoga
        - Tránh căng thẳng kéo dài

        **3. Chăm sóc bàn chân:**
        - Kiểm tra bàn chân mỗi ngày (tìm vết thương, vết loét)
        - Rửa chân sạch, lau khô (đặc biệt kẽ ngón chân)
        - Mang giày dép phù hợp, không đi chân đất
        - Cắt móng chân cẩn thận
        - **⚠️ Vết thương nhỏ ở chân có thể dẫn đến nhiễm trùng nặng!**

        **4. Vệ sinh răng miệng:**
        - Đánh răng 2 lần/ngày
        - Dùng chỉ nha khoa
        - Khám răng định kỳ (đái tháo đường dễ sâu răng, viêm nướu)

        **5. Tiêm chủng:**
        - Tiêm vắc xin cúm hàng năm
        - Tiêm vắc xin phế cầu (nếu bác sĩ chỉ định)
        - Tiêm vắc xin COVID-19

        **6. Khi ốm:**
        - Tiếp tục uống thuốc (không tự ý ngừng)
        - Đo đường huyết thường xuyên hơn
        - Uống đủ nước
        - Gọi bác sĩ nếu: Đường huyết > 250 mg/dL, nôn nhiều, không ăn được

        ## 🚨 KHI NÀO CẦN CẤP CỨU:

        **Hạ đường huyết (Đường huyết < 70 mg/dL):**
        - **Triệu chứng:** Run, đổ mồ hôi, đói, chóng mặt, lú lẫn, tim đập nhanh
        - **Xử trí ngay:**
          1. Ăn/uống 15g đường (3 viên kẹo, 1/2 ly nước ngọt, 1 thìa mật ong)
          2. Đợi 15 phút, đo lại
          3. Nếu vẫn thấp → Lặp lại
          4. Sau đó ăn bữa phụ (bánh mì, sữa)
        - **Nếu hôn mê:** Gọi cấp cứu ngay, không cho uống (sặc)

        **Tăng đường huyết cấp (Đường huyết > 250 mg/dL + triệu chứng):**
        - **Triệu chứng:** Khát nhiều, tiểu nhiều, mệt mỏi, buồn nôn, thở nhanh, hơi thở có mùi trái cây
        - **Xử trí:** Gọi cấp cứu ngay, đến bệnh viện

        ## 💊 LỜI KHUYÊN QUAN TRỌNG:

        **1. Tuân thủ điều trị:**
        - Uống thuốc đúng giờ, đúng liều
        - Không tự ý ngừng thuốc
        - Không tự ý thay đổi liều
        - Báo bác sĩ nếu có tác dụng phụ

        **2. Giáo dục bản thân:**
        - Học về bệnh, cách quản lý
        - Tham gia lớp học về đái tháo đường (nếu có)
        - Đọc tài liệu từ nguồn uy tín

        **3. Hỗ trợ xã hội:**
        - Nói với gia đình, bạn bè về bệnh
        - Tham gia nhóm hỗ trợ người đái tháo đường
        - Không ngại hỏi bác sĩ khi không rõ

        **4. Tích cực, lạc quan:**
        - Đái tháo đường có thể kiểm soát được
        - Sống khỏe mạnh, bình thường nếu kiểm soát tốt
        - Đừng để bệnh chi phối cuộc sống

        **5. Phòng ngừa biến chứng:**
        - Kiểm soát đường huyết tốt
        - Kiểm soát huyết áp (< 130/80 mmHg)
        - Kiểm soát cholesterol
        - Không hút thuốc
        - Khám định kỳ đầy đủ

        ## 📞 LIÊN HỆ BÁC SĨ KHI:

        - Đường huyết cao/thấp bất thường
        - Có triệu chứng mới
        - Vết thương không lành
        - Có dấu hiệu nhiễm trùng
        - Cần điều chỉnh thuốc
        - Có thắc mắc về điều trị
            """,
            related_disease="diabetes_type2",
            related_drugs=["Metformin", "Insulin"],
            printable=True
    ),

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
    
    # === ASTHMA ===
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
    
    # === GERD ===
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
    
    # === UTI ===
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
    
    # === OSTEOARTHRITIS ===
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
    
    # === DEPRESSION ===
    PatientEducationTopic(
        id="depression_basics",
        title="Understanding Depression",
        title_vn="Hiểu về Trầm cảm",
        category="Disease",
        content="""
# Hiểu về Trầm cảm

## Trầm cảm là gì?

Trầm cảm là bệnh tâm thần gây cảm giác buồn bã, mất hứng thú kéo dài.

## Triệu chứng:
- Buồn bã, chán nản kéo dài
- Mất hứng thú với mọi thứ
- Mệt mỏi, thiếu năng lượng
- Khó tập trung
- Thay đổi giấc ngủ (mất ngủ hoặc ngủ nhiều)
- Thay đổi ăn uống
- Cảm giác vô giá trị, tội lỗi
- Ý nghĩ tự tử

## Nguyên nhân:
- Di truyền
- Mất cân bằng hóa chất não
- Stress, sang chấn tâm lý
- Bệnh mạn tính
- Một số thuốc

## Điều trị:
- **Thuốc chống trầm cảm:** Uống đúng giờ, đủ thời gian
- **Tâm lý trị liệu:** Nói chuyện với chuyên gia
- **Thay đổi lối sống:** Tập thể dục, ngủ đủ
- **Hỗ trợ:** Gia đình, bạn bè

## ⚠️ QUAN TRỌNG:
- Trầm cảm là BỆNH, không phải yếu đuối
- Cần điều trị, không tự khỏi
- Thuốc cần thời gian mới có tác dụng (2-4 tuần)
- Không tự ý ngừng thuốc

## Khi nào cần cấp cứu:
- Ý nghĩ tự tử
- Có kế hoạch tự tử
- Không thể chăm sóc bản thân
- Hoang tưởng, ảo giác

## Lời khuyên:
- Điều trị sớm
- Uống thuốc đúng giờ
- Tâm lý trị liệu
- Tập thể dục
- Ngủ đủ giấc
- Nói chuyện với người thân
- Không tự ý ngừng thuốc
        """,
        related_disease="depression",
        related_drugs=["Sertraline", "Fluoxetine", "Escitalopram"],
        printable=True
    ),
    
    # === DENGUE FEVER ===
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
    
    # === GOUT ===
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
    
    # === STROKE ===
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
    
    # === HEPATITIS B/C ===
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
    
    # === TUBERCULOSIS ===
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
    
    # === PEPTIC ULCER DISEASE ===
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
    
    # === KIDNEY STONES ===
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
    
    # === HAND FOOT MOUTH DISEASE ===
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
    
    # === INFLUENZA ===
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
    
    # === RHEUMATOID ARTHRITIS ===
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
    
    # === MYOCARDIAL INFARCTION ===
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
    
    # === GASTRITIS ===
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
    
    # === SINUSITIS ===
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
    
    # === BRONCHITIS ===
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
    
    # === ACUTE DIARRHEA ===
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
    
    # === ALLERGIC RHINITIS ===
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
    
    # === BACK PAIN ===
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
    
    # === HEPATITIS A ===
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
]
