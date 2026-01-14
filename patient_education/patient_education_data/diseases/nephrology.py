"""
Patient Education Topics - Nephrology (VN common conditions)
"""
from patient_education.models import PatientEducationTopic


NEPHROLOGY_TOPICS = [
    PatientEducationTopic(
        id="nephrotic_syndrome_basics_vn",
        title="Understanding Nephrotic Syndrome",
        title_vn="Hội chứng thận hư: Điều bệnh nhân cần biết",
        category="Disease",
        content="""
# Hội chứng thận hư là gì?
- Thận bị rò rỉ nhiều đạm qua nước tiểu → phù toàn thân, tăng cân nhanh, nước tiểu có bọt.
- Gặp ở cả trẻ em và người lớn; ở trẻ thường tiên lượng tốt, nhưng cần theo dõi chặt.

## 🩺 Triệu chứng thường gặp
- Phù mí mắt, phù chân, bụng trướng nhẹ; tăng cân nhanh.
- Nước tiểu sủi bọt, tiểu ít.
- Mệt, chán ăn; có thể tăng huyết áp nhẹ.

## ⚠️ Khi nào cần đi khám ngay / nhập viện?
- Phù nhiều, khó thở, đau ngực, không đi tiểu/tiểu rất ít.
- Sốt, đau đầu nhiều, nôn, co giật.
- Tăng cân > 1–2 kg trong 1–2 ngày.

## 💊 Điều trị & thuốc (tóm tắt)
- **Corticoid** (theo toa): không tự ý ngừng/giảm liều đột ngột.
- **Thuốc lợi tiểu**: uống đúng giờ; theo dõi lượng nước tiểu, cân nặng.
- **Thuốc bảo vệ thận/huyết áp** (ACEi/ARB) nếu bác sĩ kê.
- **Tránh tự mua NSAID/thuốc nam**: dễ làm thận nặng hơn.

## 🍚 Ăn uống & sinh hoạt
- **Giảm muối**: hạn chế nước mắm, đồ kho mặn, đồ khô/mắm; nếm nhạt vừa.
- **Nước**: theo hướng dẫn bác sĩ (không tự uống quá nhiều nếu đang suy thận/phù nhiều).
- **Đạm**: đủ nhưng không “bồi bổ” quá mức; ưu tiên cá, thịt nạc; tránh nội tạng.
- Tránh rượu bia; bỏ thuốc lá.

## 📌 Lời khuyên cho bệnh nhân & gia đình
- Cân nặng hằng ngày; ghi nhật ký nước tiểu, cân nặng, thuốc đã uống.
- Khám đúng hẹn; mang sổ theo dõi.
- Giữ vệ sinh, tiêm phòng đầy đủ (cúm, phế cầu nếu bác sĩ khuyên).

## 📎 Lưu ý riêng cho Việt Nam
- Không tự dùng thuốc nam/lá, không tự mua kháng sinh/lợi tiểu.
- Đọc kỹ nhãn thuốc tránh NSAID (đau nhức) khi không được bác sĩ cho phép.

____ Bác sĩ có thể ghi thêm lời dặn riêng tại đây ____ 
""",
        related_disease="nephrotic_syndrome",
        related_drugs=["Prednisolone", "Furosemide", "Losartan"],
        printable=True,
    ),
    PatientEducationTopic(
        id="ckd_basics_vn",
        title="Understanding Chronic Kidney Disease",
        title_vn="Suy thận mạn: Cách theo dõi và chuẩn bị",
        category="Disease",
        content="""
# Suy thận mạn là gì?
- Thận mất dần chức năng lọc → tích tụ độc tố, có thể phải lọc máu khi muộn.
- Giai đoạn 3–5 cần theo dõi sát, chuẩn bị điều trị thay thế thận khi cần.

## 🩺 Triệu chứng thường gặp
- Giai đoạn sớm: ít triệu chứng; có thể mệt, chán ăn, phù nhẹ, tiểu đêm.
- Giai đoạn muộn: phù nhiều, buồn nôn, ngứa, khó thở, tăng huyết áp.

## ⚠️ Khi nào cần đi viện ngay?
- Khó thở, phù phổi; không đi tiểu/tiểu rất ít.
- Lú lẫn, co giật; buồn nôn/nôn nhiều.
- Kali máu cao (bác sĩ báo) hoặc loạn nhịp.

## 💊 Thuốc và nguyên tắc an toàn
- Thuốc huyết áp (ACEi/ARB/beta-blocker): uống đều, không tự ngưng.
- Lợi tiểu (nếu kê): theo dõi cân nặng, lượng nước tiểu.
- Thuốc gắn phosphat, vitamin D, EPO (nếu bác sĩ kê).
- **Tránh NSAID/thuốc giảm đau tự mua**; tránh thuốc cỏ cây không rõ nguồn.

## 🍚 Ăn uống & sinh hoạt (tùy giai đoạn, nghe theo bác sĩ/dinh dưỡng)
- Hạn chế muối; ăn nhạt.
- Đạm vừa phải, chọn đạm tốt (cá, thịt nạc); không “bồi bổ” quá mức.
- Nước: theo chỉ định (không tự uống quá nhiều nếu phù/suy tim).
- Hạn chế phosphate (nội tạng, phủ tạng, nước ngọt có phosphat), hạn chế kali nếu được dặn (chuối, cam…).
- Bỏ thuốc lá, hạn chế rượu bia.

## Chuẩn bị lọc máu (khi gần giai đoạn cuối)
- Khám tư vấn sớm: chạy thận nhân tạo / thẩm phân phúc mạc.
- Tạo cầu tay (fistula) sớm nếu chọn chạy thận.
- Tiêm ngừa viêm gan B (nếu chưa đủ).

## Theo dõi
- Cân nặng, huyết áp tại nhà; xét nghiệm định kỳ theo hẹn.
- Mang danh sách thuốc khi khám.

____ Bác sĩ có thể ghi thêm lời dặn riêng tại đây ____ 
""",
        related_disease="chronic_kidney_disease",
        related_drugs=["Losartan", "Furosemide", "Erythropoietin"],
        printable=True,
    ),
    PatientEducationTopic(
        id="recurrent_uti_basics_vn",
        title="Understanding Recurrent UTIs",
        title_vn="Nhiễm trùng tiểu tái phát: Phòng và xử trí",
        category="Disease",
        content="""
# Nhiễm trùng tiểu tái phát là gì?
- Viêm đường tiểu lặp lại (thường ≥ 2 lần/6 tháng hoặc ≥ 3 lần/năm), phổ biến ở nữ.
- Thường do vi khuẩn từ vùng sinh dục – hậu môn đi ngược lên bàng quang.

## 🩺 Triệu chứng
- Tiểu buốt, rát, tiểu lắt nhắt; có thể tiểu đục/hôi.
- Đau bụng dưới, khó chịu vùng hạ vị.
- Có thể không sốt hoặc sốt nhẹ; nếu sốt cao/rét run nghĩ viêm thận bể thận.

## ⚠️ Khi nào cần đi viện ngay?
- Sốt cao, rét run, đau lưng hông; buồn nôn/nôn; đang mang thai; tiểu máu nhiều; bí tiểu.

## 💊 Điều trị & lưu ý
- Dùng kháng sinh **đủ liều, đủ ngày theo toa**; không tự mua/đổi thuốc.
- Uống nhiều nước (nếu không bị giới hạn bởi bệnh thận/tim).
- Giảm đau (paracetamol) nếu cần, tránh tự dùng NSAID nếu có bệnh thận.

## 🍚 Phòng ngừa tái phát
- Uống đủ nước; đi tiểu sớm khi buồn tiểu, sau giao hợp.
- Vệ sinh vùng kín đúng cách (lau từ trước ra sau).
- Không nhịn tiểu kéo dài; không dùng dung dịch vệ sinh gây kích ứng.
- Hạn chế đồ uống quá ngọt/rượu bia; tránh táo bón.

## Phụ nữ
- Không thụt rửa sâu; tránh sản phẩm gây kích ứng.
- Nếu tái phát nhiều, trao đổi bác sĩ về dự phòng kháng sinh liều thấp hoặc biện pháp khác.

____ Bác sĩ có thể ghi thêm lời dặn riêng tại đây ____ 
""",
        related_disease="urinary_tract_infection",
        related_drugs=["Nitrofurantoin", "Cefuroxime", "Paracetamol"],
        printable=True,
    ),
    PatientEducationTopic(
        id="kidney_stone_basics_vn",
        title="Understanding Kidney and Ureteral Stones",
        title_vn="Sỏi thận / niệu quản: Nhận biết và phòng ngừa",
        category="Disease",
        content="""
# Sỏi thận / niệu quản là gì?
- Tinh thể khoáng chất kết tụ trong thận/niệu quản, gây đau quặn thận, tiểu máu.

## 🩺 Triệu chứng
- Đau quặn lưng – hông lan xuống bụng dưới/bẹn, từng cơn.
- Tiểu máu hồng/đỏ; tiểu buốt rát nhẹ.
- Có thể buồn nôn, nôn; ra sỏi nhỏ khi tiểu.

## ⚠️ Khi nào cần đi viện ngay?
- Sốt, rét run (nguy cơ nhiễm trùng niệu tắc nghẽn).
- Bí tiểu, không tiểu được; đau dữ dội không giảm.
- Đau kèm buồn nôn/nôn nhiều, mất nước.

## 💊 Điều trị & chăm sóc
- Uống nhiều nước (2–3 lít/ngày nếu không chống chỉ định).
- Thuốc giảm đau theo toa; thuốc giãn cơ trơn/giãn niệu quản nếu bác sĩ kê.
- Một số sỏi nhỏ có thể tự ra; sỏi lớn có thể cần tán sỏi/phẫu thuật.
- Không tự dùng kháng sinh/thuốc nam không rõ nguồn.

## 🍚 Ăn uống & phòng ngừa tái phát
- Uống đủ nước đều trong ngày.
- Giảm muối, hạn chế thức ăn quá nhiều oxalat (rau bina, trà đặc, socola) nếu bác sĩ dặn.
- Đủ canxi từ thực phẩm (không lạm dụng viên bổ sung khi không chỉ định).
- Hạn chế nước ngọt có gas, rượu bia; kiểm soát đạm động vật vừa phải.

## Theo dõi
- Giữ lại viên sỏi (nếu ra) để xét nghiệm thành phần.
- Tái khám, siêu âm/CT theo hẹn; xét nghiệm nước tiểu, máu.

____ Bác sĩ có thể ghi thêm lời dặn riêng tại đây ____ 
""",
        related_disease="kidney_stones",
        related_drugs=["Paracetamol", "Tamsulosin"],
        printable=True,
    ),
]
