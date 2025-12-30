"""
Patient Education Topics - Procedure
"""

from patient_education.models import PatientEducationTopic


PROCEDURE_TOPICS = [
    # === WOUND CARE ===
    PatientEducationTopic(
        id="wound_care",
        title="Proper Wound Care",
        title_vn="Chăm sóc Vết thương đúng cách",
        category="Procedure",
        content="""
# Chăm sóc Vết thương đúng cách

## Nguyên tắc cơ bản:

**1. Rửa tay:**
- Rửa tay sạch trước khi chạm vết thương
- Dùng xà phòng và nước
- Hoặc dùng cồn sát trùng

**2. Làm sạch vết thương:**
- Rửa bằng nước sạch
- Dùng xà phòng nhẹ (nếu cần)
- Loại bỏ bụi bẩn, mảnh vụn
- Không dùng cồn, oxy già trực tiếp lên vết thương (làm chậm lành)

**3. Băng bó:**
- Dùng băng sạch, khô
- Thay băng hàng ngày hoặc khi ướt
- Giữ vết thương khô ráo

## Các loại vết thương:

**1. Vết cắt nhỏ:**
- Rửa sạch
- Băng lại
- Thường tự lành trong vài ngày

**2. Vết trầy xước:**
- Rửa sạch
- Băng nhẹ
- Để hở nếu có thể

**3. Vết thương sâu:**
- Cầm máu (ấn trực tiếp)
- Rửa sạch
- Băng lại
- **Đến bệnh viện nếu:** Chảy máu nhiều, sâu, có dị vật

## Dấu hiệu nhiễm trùng:

- **Đỏ:** Vùng xung quanh đỏ, sưng
- **Nóng:** Vết thương nóng khi chạm
- **Đau:** Đau tăng lên
- **Mủ:** Có mủ vàng/xanh
- **Sốt:** Sốt > 38°C
- **Mùi hôi:** Vết thương có mùi

**⚠️ Đến bệnh viện ngay nếu có dấu hiệu nhiễm trùng!**

## Khi nào cần đến bệnh viện:

- Chảy máu không cầm được
- Vết thương sâu (> 1cm)
- Có dị vật trong vết thương
- Vết thương do động vật cắn
- Vết thương bẩn (đất, phân)
- Dấu hiệu nhiễm trùng
- Chưa tiêm uốn ván trong 5 năm
- Vết thương ở mặt, khớp

## Chăm sóc tại nhà:

**1. Giữ sạch:**
- Rửa nhẹ nhàng hàng ngày
- Dùng nước sạch
- Lau khô nhẹ nhàng

**2. Băng bó:**
- Thay băng hàng ngày
- Giữ khô ráo
- Không băng quá chặt

**3. Theo dõi:**
- Kiểm tra dấu hiệu nhiễm trùng
- Theo dõi tiến triển
- Ghi nhận thay đổi

## Phòng ngừa:

- Rửa tay thường xuyên
- Giữ vết thương sạch
- Thay băng đúng cách
- Không gãi, cậy vết thương
- Ăn uống đủ chất (giúp lành nhanh)

## Lời khuyên:

- Rửa tay trước khi chạm vết thương
- Làm sạch vết thương đúng cách
- Băng bó phù hợp
- Theo dõi dấu hiệu nhiễm trùng
- Đến bệnh viện khi cần
- Tiêm uốn ván nếu cần
- Giữ vết thương khô ráo
        """,
        printable=True
    ),
    
    # === BLOOD PRESSURE MONITORING ===
    PatientEducationTopic(
        id="bp_monitoring",
        title="How to Monitor Blood Pressure at Home",
        title_vn="Cách đo Huyết áp tại nhà",
        category="Procedure",
        content="""
# Cách đo Huyết áp tại nhà

## Tại sao cần đo tại nhà?

- Theo dõi huyết áp thường xuyên
- Đánh giá hiệu quả thuốc
- Phát hiện sớm vấn đề
- Giảm "hội chứng áo choàng trắng"

## Chuẩn bị:

**1. Máy đo:**
- Chọn máy đo tự động (tốt hơn)
- Kiểm tra độ chính xác định kỳ
- Đọc hướng dẫn sử dụng

**2. Trước khi đo:**
- Nghỉ ngơi 5 phút
- Không uống cà phê, hút thuốc 30 phút trước
- Đi tiểu trước (nếu cần)
- Ngồi yên, thư giãn

## Cách đo:

**1. Tư thế:**
- Ngồi thẳng lưng
- Chân đặt phẳng trên sàn
- Cánh tay để ngang tim
- Không nói chuyện

**2. Đặt băng quấn:**
- Quấn vừa khít (không quá chặt)
- Băng quấn cách khuỷu tay 2-3cm
- Ống nghe đặt trên động mạch

**3. Đo:**
- Bơm băng quấn
- Thả từ từ
- Ghi nhận số đo
- Nghỉ 1-2 phút, đo lại lần 2

## Ghi nhận kết quả:

- Ghi ngày, giờ
- Ghi số đo (tâm thu/tâm trương)
- Ghi nhịp tim (nếu có)
- Ghi hoạt động trước đó (nếu bất thường)

## Giá trị bình thường:

- **Bình thường:** < 120/80 mmHg
- **Tăng huyết áp độ 1:** 130-139/80-89 mmHg
- **Tăng huyết áp độ 2:** ≥ 140/90 mmHg
- **Tăng huyết áp cấp cứu:** ≥ 180/120 mmHg

## Khi nào cần gọi bác sĩ:

- Huyết áp cao liên tục (> 140/90)
- Huyết áp rất cao (> 180/120)
- Có triệu chứng (đau đầu, chóng mặt)
- Thay đổi đột ngột

## Lưu ý:

- Đo cùng giờ mỗi ngày
- Đo 2 lần, lấy trung bình
- Không đo ngay sau ăn, tập thể dục
- Không đo khi căng thẳng
- Mang máy đo khi khám bác sĩ

## Lời khuyên:

- Đo đều đặn
- Ghi nhận kết quả
- Mang sổ ghi khi khám
- Báo bác sĩ nếu bất thường
- Tuân thủ điều trị
- Thay đổi lối sống
        """,
        printable=True
    ),
    
    # === BLOOD SUGAR MONITORING ===
    PatientEducationTopic(
        id="blood_sugar_monitoring",
        title="How to Monitor Blood Sugar at Home",
        title_vn="Cách đo Đường huyết tại nhà",
        category="Procedure",
        content="""
# Cách đo Đường huyết tại nhà

## Tại sao cần đo tại nhà?

- Theo dõi đường huyết thường xuyên
- Điều chỉnh thuốc, chế độ ăn
- Phòng ngừa biến chứng
- Phát hiện hạ/tăng đường huyết

## Chuẩn bị:

**1. Máy đo:**
- Chọn máy đo phù hợp
- Kiểm tra độ chính xác
- Đọc hướng dẫn sử dụng

**2. Que thử:**
- Bảo quản đúng cách
- Kiểm tra hạn sử dụng
- Không dùng que thử cũ

**3. Kim lấy máu:**
- Dùng kim mới mỗi lần
- Điều chỉnh độ sâu phù hợp

## Cách đo:

**1. Rửa tay:**
- Rửa tay sạch bằng xà phòng
- Lau khô hoàn toàn
- Không dùng cồn (có thể sai số)

**2. Lấy máu:**
- Chọn ngón tay (thường ngón giữa, áp út)
- Xoay ngón tay để tăng lưu lượng máu
- Đâm kim vào bên cạnh đầu ngón tay (ít đau hơn)
- Nặn nhẹ để có giọt máu

**3. Đo:**
- Đưa que thử vào máu
- Chờ kết quả (thường 5-10 giây)
- Ghi nhận kết quả

## Khi nào cần đo:

**Đái tháo đường type 1:**
- Trước mỗi bữa ăn
- Trước khi ngủ
- Trước và sau tập thể dục
- Khi có triệu chứng hạ đường huyết

**Đái tháo đường type 2:**
- Trước bữa sáng (quan trọng nhất)
- Trước bữa tối
- Trước khi ngủ (nếu dùng insulin)
- Theo chỉ định bác sĩ

## Giá trị mục tiêu:

**Trước ăn:**
- 80-130 mg/dL (4.4-7.2 mmol/L)

**Sau ăn 2 giờ:**
- < 180 mg/dL (< 10 mmol/L)

**Trước khi ngủ:**
- 100-140 mg/dL (5.6-7.8 mmol/L)

**HbA1c:**
- < 7% (mục tiêu chung)

*Lưu ý: Mục tiêu có thể khác tùy từng người, hỏi bác sĩ*

## Hạ đường huyết:

**Triệu chứng:**
- Run, đổ mồ hôi
- Đói, chóng mặt
- Lú lẫn, khó tập trung
- Tim đập nhanh

**Xử trí:**
- Ăn/uống đường ngay (15g đường)
- Đo lại sau 15 phút
- Lặp lại nếu cần
- Ăn bữa phụ sau đó

**Phòng ngừa:**
- Ăn đúng giờ
- Không bỏ bữa
- Mang đường bên người
- Đo đường huyết thường xuyên

## Tăng đường huyết:

**Triệu chứng:**
- Khát nhiều
- Tiểu nhiều
- Mệt mỏi
- Nhìn mờ

**Xử trí:**
- Uống nhiều nước
- Kiểm tra ketone (nếu cần)
- Gọi bác sĩ nếu cao kéo dài

## Ghi nhận kết quả:

- Ghi ngày, giờ
- Ghi số đo
- Ghi thời điểm (trước/sau ăn)
- Ghi hoạt động, thuốc
- Ghi triệu chứng (nếu có)

## Lời khuyên:

- Đo đều đặn
- Ghi nhận tất cả kết quả
- Mang sổ ghi khi khám
- Báo bác sĩ nếu bất thường
- Tuân thủ điều trị
- Ăn uống đúng giờ
- Tập thể dục đều đặn
        """,
        printable=True
    ),

]
