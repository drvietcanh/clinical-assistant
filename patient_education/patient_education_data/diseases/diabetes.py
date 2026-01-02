"""
Patient Education Topics - Diabetes
"""
from patient_education.models import PatientEducationTopic


DIABETES_TOPICS = [
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

]
