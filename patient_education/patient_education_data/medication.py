"""
Patient Education Topics - Medication
"""

from patient_education.models import PatientEducationTopic


MEDICATION_TOPICS = [
    PatientEducationTopic(
            id="medication_safety",
            title="Medication Safety",
            title_vn="An toàn khi dùng thuốc",
            category="Medication",
            content="""
        # An toàn khi dùng thuốc

        ## Nguyên tắc quan trọng:

        **1. Uống thuốc đúng giờ:**
        - Tuân thủ lịch uống thuốc
        - Không bỏ liều
        - Không tự ý tăng/giảm liều

        **2. Đọc kỹ hướng dẫn:**
        - Đọc nhãn thuốc
        - Hiểu cách dùng
        - Biết tác dụng phụ

        **3. Không dùng chung thuốc:**
        - Mỗi người có đơn thuốc riêng
        - Không cho người khác dùng thuốc của mình

        **4. Bảo quản thuốc đúng cách:**
        - Để nơi khô ráo, tránh ánh sáng
        - Tránh xa tầm tay trẻ em
        - Kiểm tra hạn sử dụng

        **5. Báo cho bác sĩ:**
        - Tất cả thuốc đang dùng
        - Dị ứng thuốc
        - Tác dụng phụ

        ## Tác dụng phụ thường gặp:
        - Buồn nôn, nôn
        - Chóng mặt
        - Phát ban
        - Mệt mỏi

        ## Khi nào cần gọi bác sĩ:
        - Tác dụng phụ nghiêm trọng
        - Dị ứng (phát ban, khó thở)
        - Không cải thiện sau vài ngày
        - Quên uống thuốc nhiều lần

        ## Lời khuyên:
        - Mang danh sách thuốc khi khám
        - Hỏi bác sĩ nếu không rõ
        - Không tự ý ngừng thuốc
        - Báo ngay nếu có vấn đề
            """,
            printable=True
    ),

    PatientEducationTopic(
            id="antibiotic_use",
            title="Proper Antibiotic Use",
            title_vn="Sử dụng Kháng sinh đúng cách",
            category="Medication",
            content="""
        # Sử dụng Kháng sinh đúng cách

        ## Kháng sinh là gì?

        Kháng sinh là thuốc dùng để điều trị nhiễm trùng do vi khuẩn.

        ## ⚠️ QUAN TRỌNG:

        **Kháng sinh KHÔNG điều trị:**
        - Cảm lạnh (do virus)
        - Cúm (do virus)
        - Ho do virus
        - Sốt do virus

        ## Nguyên tắc sử dụng:

        **1. Uống đủ liều, đủ ngày:**
        - Uống đúng liều bác sĩ kê
        - Uống đủ số ngày (thường 5-7 ngày)
        - KHÔNG tự ý ngừng khi thấy đỡ

        **2. Uống đúng giờ:**
        - Cách đều nhau trong ngày
        - Trước hoặc sau ăn theo hướng dẫn

        **3. Không dùng lại thuốc cũ:**
        - Mỗi lần nhiễm trùng cần đơn mới
        - Không dùng thuốc thừa

        **4. Không chia sẻ thuốc:**
        - Mỗi người có đơn riêng
        - Không cho người khác dùng

        ## Tác dụng phụ:
        - Buồn nôn, nôn
        - Tiêu chảy
        - Phát ban
        - Dị ứng

        ## Kháng kháng sinh:
        - Dùng kháng sinh không đúng → vi khuẩn kháng thuốc
        - Lần sau sẽ khó điều trị hơn
        - Có thể nguy hiểm tính mạng

        ## Lời khuyên:
        - Chỉ dùng khi bác sĩ kê
        - Uống đủ liều, đủ ngày
        - Không tự ý mua kháng sinh
        - Báo bác sĩ nếu có tác dụng phụ
            """,
            related_drugs=["Amoxicillin", "Azithromycin", "Ceftriaxone"],
            printable=True
    ),
    
    # === PAIN RELIEVERS ===
    PatientEducationTopic(
        id="pain_relievers",
        title="Using Pain Relievers Safely",
        title_vn="Sử dụng Thuốc giảm đau an toàn",
        category="Medication",
        content="""
# Sử dụng Thuốc giảm đau an toàn

## Các loại thuốc giảm đau:

**1. Paracetamol (Acetaminophen):**
- Giảm đau nhẹ đến trung bình
- Hạ sốt
- An toàn nếu dùng đúng liều
- **Liều tối đa:** 4g/ngày (người lớn)

**2. NSAID (Ibuprofen, Diclofenac, Naproxen):**
- Giảm đau, viêm
- Hạ sốt
- **Tác dụng phụ:** Đau dạ dày, tăng huyết áp
- **Tránh dùng:** Nếu có bệnh dạ dày, thận, tim

**3. Opioids (Codeine, Tramadol):**
- Giảm đau mạnh
- Chỉ dùng khi bác sĩ kê
- **Nguy cơ:** Nghiện, táo bón, buồn ngủ

## Nguyên tắc sử dụng:

**1. Dùng đúng liều:**
- Đọc nhãn thuốc
- Không vượt quá liều tối đa
- Không dùng quá 3-5 ngày không có chỉ định

**2. Paracetamol:**
- An toàn nếu dùng đúng
- **Nguy hiểm:** Quá liều gây tổn thương gan
- Không uống rượu khi dùng

**3. NSAID:**
- Uống sau ăn để giảm đau dạ dày
- Không dùng lâu dài không có chỉ định
- Báo bác sĩ nếu đau dạ dày

**4. Opioids:**
- Chỉ dùng khi bác sĩ kê
- Không lái xe khi dùng
- Báo bác sĩ nếu nghiện

## Khi nào cần gọi bác sĩ:
- Đau không giảm sau vài ngày
- Tác dụng phụ nghiêm trọng
- Cần dùng thuốc lâu dài
- Quá liều

## Lời khuyên:
- Dùng đúng liều
- Không tự ý tăng liều
- Báo bác sĩ tất cả thuốc đang dùng
- Tránh dùng nhiều loại cùng lúc
- Đọc nhãn thuốc cẩn thận
        """,
        related_drugs=["Paracetamol", "Ibuprofen", "Diclofenac", "Codeine"],
        printable=True
    ),
    
    # === STATINS ===
    PatientEducationTopic(
        id="statins_use",
        title="Understanding Statins",
        title_vn="Hiểu về Thuốc Statin",
        category="Medication",
        content="""
# Hiểu về Thuốc Statin

## Statin là gì?

Statin là thuốc giảm cholesterol, giúp phòng ngừa bệnh tim mạch.

## Tác dụng:
- Giảm cholesterol xấu (LDL)
- Tăng cholesterol tốt (HDL)
- Giảm nguy cơ đột quỵ, nhồi máu cơ tim
- Ổn định mảng xơ vữa

## Khi nào cần dùng:
- Cholesterol cao
- Đã có bệnh tim mạch
- Đái tháo đường + yếu tố nguy cơ
- Nguy cơ tim mạch cao

## Cách dùng:
- Uống buổi tối (hiệu quả hơn)
- Uống đúng giờ mỗi ngày
- Uống lâu dài (thường suốt đời)
- Không tự ý ngừng

## Tác dụng phụ:
- **Đau cơ:** Thường gặp, thường nhẹ
- **Tổn thương gan:** Hiếm, cần xét nghiệm
- **Đái tháo đường:** Tăng nguy cơ nhẹ
- **Rối loạn trí nhớ:** Hiếm

## Khi nào cần báo bác sĩ:
- Đau cơ nhiều
- Nước tiểu sẫm màu (có thể tổn thương cơ)
- Mệt mỏi bất thường
- Vàng da

## Tương tác thuốc:
- Một số thuốc kháng nấm
- Một số kháng sinh
- Nước ép bưởi (tăng tác dụng phụ)
- **Báo bác sĩ tất cả thuốc đang dùng**

## Lời khuyên:
- Uống đúng giờ
- Không tự ý ngừng
- Xét nghiệm máu định kỳ
- Báo bác sĩ nếu đau cơ
- Kết hợp với chế độ ăn, tập thể dục
- Không uống nước ép bưởi
        """,
        related_drugs=["Atorvastatin", "Simvastatin", "Rosuvastatin"],
        printable=True
    ),
    
    # === ANTICOAGULANTS ===
    PatientEducationTopic(
        id="anticoagulants_use",
        title="Understanding Anticoagulants",
        title_vn="Hiểu về Thuốc chống đông máu",
        category="Medication",
        content="""
# Hiểu về Thuốc chống đông máu

## Thuốc chống đông máu là gì?

Thuốc chống đông máu giúp ngăn ngừa hình thành cục máu đông.

## Khi nào cần dùng:
- Rung nhĩ
- Sau phẫu thuật tim
- Huyết khối tĩnh mạch sâu (DVT)
- Nhồi máu cơ tim
- Đột quỵ do cục máu đông

## Các loại thuốc:
- **Warfarin:** Uống hàng ngày, cần xét nghiệm máu
- **DOACs** (Dabigatran, Rivaroxaban, Apixaban): Uống hàng ngày, không cần xét nghiệm thường xuyên

## ⚠️ QUAN TRỌNG:

**Nguy cơ chảy máu:**
- Dễ chảy máu hơn bình thường
- Vết thương lâu cầm máu
- Dễ bầm tím
- Chảy máu cam, chảy máu nướu

**Khi nào cần cấp cứu:**
- Chảy máu không cầm được
- Nôn ra máu
- Phân đen hoặc có máu
- Đau đầu dữ dội
- Ngã, chấn thương đầu
- Chảy máu nhiều từ vết thương

## Tương tác thuốc:
- Nhiều thuốc tương tác
- **Báo bác sĩ TẤT CẢ thuốc đang dùng**
- Một số thực phẩm (Warfarin)

## Chế độ ăn (Warfarin):
- **Vitamin K:** Ảnh hưởng tác dụng
- Ăn đều đặn, không thay đổi đột ngột
- Rau xanh (rau cải, rau muống) có nhiều vitamin K

## Lời khuyên:
- Uống đúng giờ mỗi ngày
- Không tự ý ngừng
- Xét nghiệm máu định kỳ (Warfarin)
- Mang thẻ y tế ghi rõ đang dùng thuốc chống đông
- Báo bác sĩ trước phẫu thuật, nhổ răng
- Tránh chấn thương
- Báo ngay nếu chảy máu bất thường
        """,
        related_drugs=["Warfarin", "Dabigatran", "Rivaroxaban", "Apixaban"],
        printable=True
    ),
    
    # === INSULIN INJECTION ===
    PatientEducationTopic(
        id="insulin_injection",
        title="How to Inject Insulin",
        title_vn="Cách tiêm Insulin",
        category="Medication",
        content="""
# Cách tiêm Insulin

## Chuẩn bị:

**1. Rửa tay sạch**

**2. Kiểm tra insulin:**
- Kiểm tra tên, hạn sử dụng
- Kiểm tra màu sắc (phải trong suốt)
- Không dùng nếu đổi màu, có hạt

**3. Chuẩn bị bơm tiêm:**
- Lấy bơm tiêm và kim tiêm mới
- Lấy đúng loại insulin
- Lấy đúng liều

## Cách tiêm:

**1. Chọn vị trí:**
- Bụng (cách rốn 5cm)
- Đùi (mặt trước, mặt ngoài)
- Cánh tay (mặt sau)
- Mông
- **Luân phiên vị trí** (không tiêm cùng chỗ)

**2. Kỹ thuật:**
- Sát trùng da bằng cồn
- Kẹp da bằng ngón tay
- Đâm kim vuông góc (90 độ)
- Bơm insulin từ từ
- Đếm 10 giây
- Rút kim
- Ấn nhẹ (không xoa)

**3. Bảo quản:**
- **Đang dùng:** Để ở nhiệt độ phòng (< 30°C)
- **Chưa dùng:** Để trong tủ lạnh (2-8°C)
- Không để đông lạnh
- Không để ngoài nắng

## Lưu ý:
- Dùng kim tiêm mới mỗi lần
- Không dùng lại kim tiêm
- Vứt kim tiêm đúng cách (hộp cứng)
- Không chia sẻ bơm tiêm

## Tác dụng phụ:
- Hạ đường huyết (nguy hiểm!)
- Bầm tím, đau tại chỗ tiêm
- Dị ứng (hiếm)

## Hạ đường huyết:
- **Triệu chứng:** Run, đổ mồ hôi, đói, chóng mặt, lú lẫn
- **Xử trí:** Ăn/uống đường ngay (kẹo, nước ngọt)
- **Phòng ngừa:** Ăn đúng giờ, kiểm tra đường huyết

## Lời khuyên:
- Học kỹ thuật từ bác sĩ/y tá
- Tiêm đúng giờ
- Luân phiên vị trí
- Kiểm tra đường huyết
- Mang đường bên người
- Báo bác sĩ nếu có vấn đề
        """,
        related_drugs=["Insulin"],
        printable=True
    ),

]
