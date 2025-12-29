"""
Patient Education Content Database
Educational materials for patients in simple, easy-to-understand language
"""

from typing import List, Optional
from dataclasses import dataclass, field


@dataclass
class PatientEducationTopic:
    """Patient education topic information"""
    id: str
    title: str
    title_vn: str
    category: str  # Disease, Medication, Lifestyle, etc.
    content: str  # Main content in simple language
    related_disease: Optional[str] = None  # Link to disease
    related_drugs: List[str] = field(default_factory=list)  # Link to drugs
    printable: bool = True
    language: str = "vi"  # Vietnamese


# Patient Education Database
# Starting with 20-30 common topics
PATIENT_EDUCATION_DATABASE: List[PatientEducationTopic] = [
    # === DIABETES ===
    PatientEducationTopic(
        id="diabetes_basics",
        title="Understanding Diabetes",
        title_vn="Hiểu về Đái tháo đường",
        category="Disease",
        content="""
# Hiểu về Đái tháo đường

## Đái tháo đường là gì?

Đái tháo đường là bệnh mạn tính xảy ra khi cơ thể không thể sử dụng đường (glucose) đúng cách. Đường là nguồn năng lượng chính của cơ thể.

## Có hai loại chính:

**Đái tháo đường type 1:**
- Cơ thể không sản xuất insulin
- Thường gặp ở trẻ em và thanh niên
- Cần tiêm insulin hàng ngày

**Đái tháo đường type 2:**
- Cơ thể không sử dụng insulin đúng cách
- Thường gặp ở người lớn
- Có thể kiểm soát bằng thuốc, chế độ ăn, và tập thể dục

## Triệu chứng:
- Tiểu nhiều
- Khát nhiều
- Ăn nhiều nhưng sụt cân
- Mệt mỏi
- Nhìn mờ

## Điều trị:
- Uống thuốc đúng giờ
- Chế độ ăn lành mạnh
- Tập thể dục đều đặn
- Theo dõi đường huyết

## Biến chứng nếu không điều trị:
- Bệnh tim mạch
- Bệnh thận
- Tổn thương mắt
- Tổn thương thần kinh
- Vết thương lâu lành

## Lời khuyên:
- Tuân thủ điều trị
- Kiểm tra đường huyết thường xuyên
- Khám định kỳ
- Giữ chế độ ăn và tập thể dục
        """,
        related_disease="diabetes_type2",
        related_drugs=["Metformin", "Insulin"],
        printable=True
    ),
    
    PatientEducationTopic(
        id="diabetes_diet",
        title="Diet for Diabetes",
        title_vn="Chế độ ăn cho người Đái tháo đường",
        category="Lifestyle",
        content="""
# Chế độ ăn cho người Đái tháo đường

## Nguyên tắc chính:

**1. Ăn đúng giờ:**
- Ăn 3 bữa chính và 2-3 bữa phụ
- Không bỏ bữa
- Ăn đều đặn mỗi ngày

**2. Chọn thực phẩm phù hợp:**
- **Nên ăn:** Rau xanh, trái cây ít ngọt, thịt nạc, cá, đậu
- **Hạn chế:** Đường, bánh kẹo, nước ngọt, đồ chiên rán
- **Tránh:** Đồ ngọt, rượu bia

**3. Kiểm soát khẩu phần:**
- Ăn vừa đủ, không quá no
- Chia nhỏ bữa ăn
- Đọc nhãn thực phẩm

**4. Uống đủ nước:**
- Uống 1.5-2 lít nước/ngày
- Tránh nước ngọt, nước có đường

## Thực phẩm nên ăn:
- Rau xanh (rau cải, rau muống, bông cải)
- Trái cây ít ngọt (táo, lê, cam)
- Thịt nạc, cá, đậu
- Gạo lứt, bánh mì đen
- Sữa không đường

## Thực phẩm nên tránh:
- Đường, mật ong
- Bánh kẹo, nước ngọt
- Đồ chiên rán nhiều dầu mỡ
- Rượu bia
- Trái cây quá ngọt (sầu riêng, mít, nhãn)

## Lời khuyên:
- Ăn chậm, nhai kỹ
- Không ăn quá no
- Theo dõi đường huyết sau ăn
- Tham khảo bác sĩ dinh dưỡng
        """,
        related_disease="diabetes_type2",
        printable=True
    ),
    
    # === HYPERTENSION ===
    PatientEducationTopic(
        id="hypertension_basics",
        title="Understanding High Blood Pressure",
        title_vn="Hiểu về Tăng huyết áp",
        category="Disease",
        content="""
# Hiểu về Tăng huyết áp

## Tăng huyết áp là gì?

Tăng huyết áp (cao huyết áp) là khi huyết áp cao hơn bình thường trong thời gian dài.

**Huyết áp bình thường:** Dưới 120/80 mmHg
**Tăng huyết áp:** Từ 140/90 mmHg trở lên

## Nguyên nhân:
- Tuổi cao
- Di truyền
- Béo phì
- Ăn mặn
- Ít vận động
- Hút thuốc, uống rượu
- Stress

## Triệu chứng:
- Thường không có triệu chứng
- Đau đầu
- Chóng mặt
- Mệt mỏi
- Nhìn mờ

## Điều trị:
- Uống thuốc đúng giờ
- Chế độ ăn ít muối
- Tập thể dục
- Giảm cân (nếu thừa cân)
- Bỏ thuốc lá, hạn chế rượu

## Biến chứng nếu không điều trị:
- Đột quỵ
- Nhồi máu cơ tim
- Suy thận
- Tổn thương mắt

## Lời khuyên:
- Đo huyết áp thường xuyên
- Uống thuốc đúng giờ
- Ăn ít muối (< 5g/ngày)
- Tập thể dục 30 phút/ngày
- Giữ cân nặng hợp lý
        """,
        related_disease="hypertension",
        related_drugs=["Amlodipine", "Enalapril", "Losartan"],
        printable=True
    ),
    
    # === PNEUMONIA ===
    PatientEducationTopic(
        id="pneumonia_basics",
        title="Understanding Pneumonia",
        title_vn="Hiểu về Viêm phổi",
        category="Disease",
        content="""
# Hiểu về Viêm phổi

## Viêm phổi là gì?

Viêm phổi là tình trạng nhiễm trùng phổi, gây viêm các túi khí trong phổi.

## Nguyên nhân:
- Vi khuẩn (phổ biến nhất)
- Virus (cúm, COVID-19)
- Nấm (hiếm)

## Triệu chứng:
- Sốt, ớn lạnh
- Ho có đờm (vàng/xanh)
- Khó thở
- Đau ngực
- Mệt mỏi

## Điều trị:
- Uống kháng sinh đúng liều, đủ ngày
- Nghỉ ngơi
- Uống nhiều nước
- Hạ sốt (Paracetamol)
- Oxy nếu khó thở nặng

## Khi nào cần đến bệnh viện:
- Khó thở nặng
- Sốt cao không hạ
- Đau ngực nhiều
- Lú lẫn
- Môi tím

## Phòng ngừa:
- Tiêm vắc xin phế cầu
- Tiêm vắc xin cúm hàng năm
- Rửa tay thường xuyên
- Bỏ thuốc lá
- Giữ sức khỏe tốt

## Lời khuyên:
- Uống đủ nước
- Nghỉ ngơi đầy đủ
- Uống thuốc đúng giờ
- Tái khám nếu không cải thiện
        """,
        related_disease="pneumonia",
        related_drugs=["Amoxicillin", "Azithromycin", "Levofloxacin"],
        printable=True
    ),
    
    # === MEDICATION SAFETY ===
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
    
    # === ANTIBIOTIC USE ===
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
    
    # === HEART FAILURE ===
    PatientEducationTopic(
        id="heart_failure_basics",
        title="Understanding Heart Failure",
        title_vn="Hiểu về Suy tim",
        category="Disease",
        content="""
# Hiểu về Suy tim

## Suy tim là gì?

Suy tim là khi tim không bơm đủ máu để đáp ứng nhu cầu của cơ thể.

## Triệu chứng:
- Khó thở (khi gắng sức, khi nằm)
- Mệt mỏi
- Phù chân, mắt cá chân
- Ho khan
- Tăng cân (do ứ dịch)

## Điều trị:
- Uống thuốc đúng giờ
- Chế độ ăn ít muối
- Hạn chế uống nước (nếu bác sĩ yêu cầu)
- Tập thể dục nhẹ nhàng
- Theo dõi cân nặng hàng ngày

## Chế độ ăn:
- **Ít muối:** < 2g/ngày
- **Hạn chế nước:** Nếu bác sĩ yêu cầu
- **Tránh:** Đồ mặn, đồ hộp, thức ăn nhanh

## Theo dõi:
- Cân nặng mỗi sáng
- Huyết áp
- Triệu chứng

## Khi nào cần đến bệnh viện:
- Khó thở nặng
- Phù nhiều
- Tăng cân nhanh (> 2kg/tuần)
- Đau ngực
- Tim đập nhanh, không đều

## Lời khuyên:
- Uống thuốc đúng giờ
- Theo dõi cân nặng
- Ăn ít muối
- Tập thể dục nhẹ nhàng
- Khám định kỳ
        """,
        related_disease="heart_failure",
        related_drugs=["ACE Inhibitor", "Beta-blocker", "Furosemide"],
        printable=True
    ),
    
    # === COPD ===
    PatientEducationTopic(
        id="copd_basics",
        title="Understanding COPD",
        title_vn="Hiểu về COPD",
        category="Disease",
        content="""
# Hiểu về COPD

## COPD là gì?

COPD (Bệnh phổi tắc nghẽn mạn tính) là bệnh phổi mạn tính gây khó thở.

## Nguyên nhân chính:
- **Hút thuốc lá** (nguyên nhân chính)
- Khói thuốc
- Ô nhiễm không khí
- Khói, bụi nghề nghiệp

## Triệu chứng:
- Ho mạn tính
- Khạc đờm
- Khó thở khi gắng sức
- Thở khò khè
- Tức ngực

## Điều trị:
- **Bỏ thuốc lá** (quan trọng nhất!)
- Dùng thuốc hít đúng cách
- Tập thể dục, phục hồi chức năng phổi
- Oxy nếu cần
- Tiêm vắc xin cúm, phế cầu

## Phòng ngừa đợt cấp:
- Bỏ thuốc lá
- Tránh khói, bụi
- Tiêm vắc xin
- Uống thuốc đúng giờ
- Tập thể dục

## Khi nào cần đến bệnh viện:
- Khó thở nặng hơn
- Ho nhiều, đờm vàng/xanh
- Sốt
- Không đáp ứng với thuốc

## Lời khuyên:
- **Bỏ thuốc lá ngay lập tức**
- Dùng thuốc hít đúng cách
- Tập thể dục đều đặn
- Tránh khói, bụi
- Khám định kỳ
        """,
        related_disease="copd",
        related_drugs=["Salbutamol", "Tiotropium", "Budesonide"],
        printable=True
    ),
]


def get_all_topics() -> List[PatientEducationTopic]:
    """Get all patient education topics"""
    return PATIENT_EDUCATION_DATABASE


def get_topics_by_category(category: str) -> List[PatientEducationTopic]:
    """Get topics filtered by category"""
    if not category or category == "All":
        return PATIENT_EDUCATION_DATABASE
    return [t for t in PATIENT_EDUCATION_DATABASE if t.category == category]


def get_category_list() -> List[str]:
    """Get list of all categories"""
    categories = set(t.category for t in PATIENT_EDUCATION_DATABASE)
    return sorted(list(categories))

