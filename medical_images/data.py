"""
Medical Image Library Database
Metadata for medical images (X-ray, CT, MRI, Ultrasound, Clinical photos, ECG, Pathology)
"""

from typing import List, Optional
from dataclasses import dataclass, field


@dataclass
class MedicalImage:
    """Medical image information"""
    id: str
    title: str
    title_vn: str
    category: str  # Cardiology, Respiratory, Neurology, etc.
    image_type: str  # X-ray, CT, MRI, Ultrasound, Clinical, ECG, Pathology
    description: str = ""
    findings: str = ""  # What to look for in the image
    diagnosis: str = ""  # Associated diagnosis
    url: str = ""  # URL to image (placeholder for now)
    source: str = ""  # Source/attribution
    related_disease: Optional[str] = None
    related_scores: List[str] = field(default_factory=list)
    notes: str = ""


# Medical Images Database
# Metadata for medical images (actual images can be added later)
MEDICAL_IMAGES_DATABASE: List[MedicalImage] = [
    # === CHEST X-RAY ===
    MedicalImage(
        id="cxr_pneumonia",
        title="Chest X-ray: Pneumonia",
        title_vn="X-quang ngực: Viêm phổi",
        category="Respiratory",
        image_type="X-ray",
        description="X-quang ngực cho thấy thâm nhiễm phổi do viêm phổi",
        findings="Thâm nhiễm phổi một bên, có thể thấy air bronchograms, không có tràn dịch màng phổi",
        diagnosis="Pneumonia",
        url="",  # Placeholder - can add actual image URLs later
        source="Educational reference",
        related_disease="pneumonia",
        related_scores=["CURB-65", "PSI"]
    ),
    MedicalImage(
        id="cxr_copd",
        title="Chest X-ray: COPD",
        title_vn="X-quang ngực: COPD",
        category="Respiratory",
        image_type="X-ray",
        description="X-quang ngực ở bệnh nhân COPD cho thấy khí phế thũng",
        findings="Tăng sáng phổi, phẳng cơ hoành, lồng ngực hình thùng, tim dài và hẹp",
        diagnosis="COPD with emphysema",
        url="",
        source="Educational reference",
        related_disease="copd"
    ),
    MedicalImage(
        id="cxr_pneumothorax",
        title="Chest X-ray: Pneumothorax",
        title_vn="X-quang ngực: Tràn khí màng phổi",
        category="Respiratory",
        image_type="X-ray",
        description="X-quang ngực cho thấy tràn khí màng phổi",
        findings="Mất mạch máu phổi, thấy đường màng phổi tạng, phổi bị đẩy vào trong",
        diagnosis="Pneumothorax",
        url="",
        source="Educational reference",
        related_disease="pneumothorax"
    ),
    
    # === ECG ===
    MedicalImage(
        id="ecg_stemi",
        title="ECG: STEMI",
        title_vn="Điện tâm đồ: STEMI",
        category="Cardiology",
        image_type="ECG",
        description="ECG cho thấy nhồi máu cơ tim ST chênh lên (STEMI)",
        findings="ST chênh lên ở chuyển đạo trước (V1-V4), có thể có sóng Q mới, rối loạn nhịp",
        diagnosis="ST-Elevation Myocardial Infarction (STEMI)",
        url="",
        source="Educational reference",
        related_disease="myocardial_infarction",
        related_scores=["TIMI Risk Score"]
    ),
    MedicalImage(
        id="ecg_afib",
        title="ECG: Atrial Fibrillation",
        title_vn="Điện tâm đồ: Rung nhĩ",
        category="Cardiology",
        image_type="ECG",
        description="ECG cho thấy rung nhĩ",
        findings="Không có sóng P, nhịp không đều, sóng f (fibrillation waves), QRS bình thường",
        diagnosis="Atrial Fibrillation",
        url="",
        source="Educational reference",
        related_disease="atrial_fibrillation",
        related_scores=["CHA2DS2-VASc"]
    ),
    MedicalImage(
        id="ecg_svt",
        title="ECG: Supraventricular Tachycardia",
        title_vn="Điện tâm đồ: Nhịp nhanh trên thất",
        category="Cardiology",
        image_type="ECG",
        description="ECG cho thấy nhịp nhanh trên thất (SVT)",
        findings="Nhịp tim nhanh (>150 bpm), QRS hẹp, sóng P khó thấy hoặc đảo ngược",
        diagnosis="Supraventricular Tachycardia",
        url="",
        source="Educational reference"
    ),
    
    # === CT SCAN ===
    MedicalImage(
        id="ct_stroke",
        title="CT Brain: Ischemic Stroke",
        title_vn="CT não: Đột quỵ thiếu máu cục bộ",
        category="Neurology",
        image_type="CT",
        description="CT não không tiêm thuốc cản quang cho thấy đột quỵ thiếu máu cục bộ",
        findings="Vùng giảm đậm độ ở vùng tưới máu động mạch não giữa, mất ranh giới chất xám-chất trắng",
        diagnosis="Acute Ischemic Stroke",
        url="",
        source="Educational reference",
        related_disease="stroke",
        related_scores=["NIHSS"]
    ),
    MedicalImage(
        id="ct_ich",
        title="CT Brain: Intracerebral Hemorrhage",
        title_vn="CT não: Xuất huyết nội sọ",
        category="Neurology",
        image_type="CT",
        description="CT não cho thấy xuất huyết nội sọ",
        findings="Vùng tăng đậm độ (máu) trong nhu mô não, có thể có hiệu ứng khối, phù xung quanh",
        diagnosis="Intracerebral Hemorrhage",
        url="",
        source="Educational reference",
        related_disease="stroke"
    ),
    
    # === CLINICAL PHOTOS ===
    MedicalImage(
        id="clinical_jaundice",
        title="Clinical Photo: Jaundice",
        title_vn="Ảnh lâm sàng: Vàng da",
        category="GI",
        image_type="Clinical",
        description="Ảnh lâm sàng cho thấy vàng da và củng mạc",
        findings="Vàng da rõ, vàng củng mạc, có thể kèm ngứa, nước tiểu sẫm màu",
        diagnosis="Jaundice (multiple causes)",
        url="",
        source="Educational reference"
    ),
    MedicalImage(
        id="clinical_cyanosis",
        title="Clinical Photo: Cyanosis",
        title_vn="Ảnh lâm sàng: Tím tái",
        category="Cardiology",
        image_type="Clinical",
        description="Ảnh lâm sàng cho thấy tím tái",
        findings="Môi, đầu ngón tay tím, có thể kèm clubbing, thở nhanh",
        diagnosis="Cyanosis (hypoxia)",
        url="",
        source="Educational reference"
    ),
    
    # === PATHOLOGY ===
    MedicalImage(
        id="pathology_aki",
        title="Pathology: Acute Kidney Injury",
        title_vn="Giải phẫu bệnh: Tổn thương thận cấp",
        category="Nephrology",
        image_type="Pathology",
        description="Mẫu giải phẫu bệnh cho thấy tổn thương thận cấp",
        findings="Hoại tử ống thận, tế bào ống thận bong tróc, có thể thấy cast trong ống thận",
        diagnosis="Acute Tubular Necrosis (ATN)",
        url="",
        source="Educational reference",
        related_disease="aki"
    ),
]


def get_all_images() -> List[MedicalImage]:
    """Get all medical images"""
    return MEDICAL_IMAGES_DATABASE


def get_images_by_category(category: str) -> List[MedicalImage]:
    """Get images filtered by category"""
    if not category or category == "All":
        return MEDICAL_IMAGES_DATABASE
    return [img for img in MEDICAL_IMAGES_DATABASE if img.category == category]


def get_images_by_type(image_type: str) -> List[MedicalImage]:
    """Get images filtered by image type"""
    if not image_type or image_type == "All":
        return MEDICAL_IMAGES_DATABASE
    return [img for img in MEDICAL_IMAGES_DATABASE if img.image_type == image_type]


def get_category_list() -> List[str]:
    """Get list of all categories"""
    categories = set(img.category for img in MEDICAL_IMAGES_DATABASE)
    return sorted(list(categories))


def get_image_type_list() -> List[str]:
    """Get list of all image types"""
    types = set(img.image_type for img in MEDICAL_IMAGES_DATABASE)
    return sorted(list(types))

