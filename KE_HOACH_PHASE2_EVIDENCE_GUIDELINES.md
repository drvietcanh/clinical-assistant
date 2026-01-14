# Kế Hoạch Phase 2: Evidence & Guidelines

**Mục tiêu:** Implement Evidence Grading System và tích hợp Guidelines phù hợp Việt Nam

**Thời gian:** 2-3 tháng

**Trạng thái:** 🚀 Bắt đầu

---

## Tổng Quan

Phase 2 tập trung vào:
1. **Evidence Grading System** - Thêm level of evidence (A/B/C) và strength of recommendation
2. **Guidelines VN** - Tích hợp Bộ Y tế và Hội chuyên khoa VN
3. **Local Protocols** - Bổ sung protocols phù hợp điều kiện VN
4. **Drug Formulary VN** - Tích hợp danh mục thuốc VN

---

## Task 1: Implement Evidence Grading System

### 1.1 Tạo Evidence Grading Schema

**File:** `config/evidence_grading.py`

**Nội dung:**
```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class EvidenceLevel:
    """Level of evidence (A/B/C)"""
    level: str  # "A", "B", "C"
    description: str
    color: str
    icon: str

EVIDENCE_LEVELS = {
    "A": EvidenceLevel(
        level="A",
        description="High-quality evidence",
        color="#28a745",  # Green
        icon="🟢"
    ),
    "B": EvidenceLevel(
        level="B",
        description="Moderate-quality evidence",
        color="#ffc107",  # Yellow
        icon="🟡"
    ),
    "C": EvidenceLevel(
        level="C",
        description="Low-quality evidence",
        color="#dc3545",  # Red
        icon="🔴"
    )
}

@dataclass
class RecommendationStrength:
    """Strength of recommendation (Strong/Weak)"""
    strength: str  # "Strong", "Weak"
    description: str
    color: str
    icon: str

RECOMMENDATION_STRENGTHS = {
    "Strong": RecommendationStrength(
        strength="Strong",
        description="Strong recommendation",
        color="#007bff",  # Blue
        icon="💪"
    ),
    "Weak": RecommendationStrength(
        strength="Weak",
        description="Weak recommendation",
        color="#6c757d",  # Gray
        icon="🤏"
    )
}

@dataclass
class EvidenceGrade:
    """Complete evidence grade"""
    level: str  # "A", "B", "C"
    strength: str  # "Strong", "Weak"
    source: Optional[str] = None  # Guideline source
    year: Optional[int] = None  # Publication year
```

### 1.2 Tạo Evidence Badge Component

**File:** `components/evidence_badge.py`

**Chức năng:**
- Hiển thị badge với màu sắc phân biệt
- Tooltip với mô tả chi tiết
- Responsive design

### 1.3 Áp dụng cho Protocols

**File:** `protocols/` (các file protocol)

**Công việc:**
- Thêm `evidence_grade` parameter cho mỗi recommendation
- Hiển thị badge trong protocol rendering
- Thêm section "Evidence Summary" ở đầu protocol

### 1.4 Áp dụng cho Guidelines Tracker

**File:** `guidelines/data.py`, `pages/15_📋_Guidelines_Tracker.py`

**Công việc:**
- Thêm `evidence_level` field cho guidelines
- Hiển thị badge trong guideline cards
- Filter theo evidence level

### 1.5 Áp dụng cho Drug Recommendations

**File:** `drugs/drug_database.py`, `pages/07_💊_Drug_Database.py`

**Công việc:**
- Thêm `evidence_grade` cho dosing recommendations
- Hiển thị trong drug detail view
- Áp dụng cho renal/hepatic adjustments

---

## Task 2: Tích Hợp Bộ Y Tế Guidelines

### 2.1 Thu Thập Guidelines

**Nguồn:**
- Bộ Y tế VN website
- Các quyết định, thông tư về điều trị
- Hướng dẫn chẩn đoán và điều trị

### 2.2 Cấu Trúc Dữ Liệu

**File:** `guidelines/data_vn.py`

**Fields:**
- `id`: Unique identifier
- `title_vn`: Tiêu đề tiếng Việt
- `title_en`: Tiêu đề tiếng Anh (nếu có)
- `organization`: "Bộ Y tế VN"
- `category`: Chuyên khoa
- `year`: Năm ban hành
- `last_updated`: Cập nhật lần cuối
- `evidence_level`: Level of evidence
- `link`: Link đến tài liệu chính thức
- `summary`: Tóm tắt
- `key_recommendations`: Các khuyến nghị chính

### 2.3 Tích Hợp vào Guidelines Tracker

**File:** `guidelines/tracker.py`, `pages/15_📋_Guidelines_Tracker.py`

**Công việc:**
- Import guidelines từ `data_vn.py`
- Hiển thị với badge "Bộ Y tế VN"
- Filter theo organization
- Search hỗ trợ tiếng Việt

---

## Task 3: Bổ Sung Local Protocols

### 3.1 Xác Định Protocols Cần Bổ Sung

**Ưu tiên:**
- Protocols phù hợp điều kiện VN
- Protocols cho bệnh phổ biến tại VN
- Protocols với thuốc có sẵn tại VN

### 3.2 Tạo Protocols Mới

**File:** `protocols/` (thêm các file mới)

**Ví dụ:**
- `render_dengue_fever_vn.py` - Sốt xuất huyết (VN protocol)
- `render_tuberculosis_vn.py` - Lao (VN protocol)
- `render_hypertension_vn.py` - Tăng huyết áp (VN protocol)

### 3.3 Tag "VN Protocol"

**Công việc:**
- Thêm tag "VN Protocol" cho protocols phù hợp VN
- Hiển thị badge trong protocol list
- Filter theo tag

---

## Task 4: Drug Formulary VN

### 4.1 Thu Thập Dữ Liệu Formulary

**Nguồn:**
- Danh mục thuốc được phép lưu hành tại VN
- Danh mục thuốc BHYT chi trả
- Formulary các bệnh viện lớn

### 4.2 Cấu Trúc Dữ Liệu

**File:** `drugs/formulary_vn.py`

**Fields:**
- `drug_id`: Link đến drug database
- `vn_approved`: Được phép tại VN (True/False)
- `bhyt_coverage`: BHYT chi trả (True/False)
- `bhyt_percentage`: Tỷ lệ chi trả (%)
- `bhyt_conditions`: Điều kiện chi trả
- `hospital_formulary`: Danh sách bệnh viện có thuốc
- `generic_available`: Có generic (True/False)
- `generic_names`: Tên generic

### 4.3 Tích Hợp vào Drug Database

**File:** `drugs/drug_database.py`, `pages/07_💊_Drug_Database.py`

**Công việc:**
- Import formulary data
- Hiển thị trong drug detail view:
  - Badge "BHYT" nếu được chi trả
  - Tỷ lệ chi trả
  - Điều kiện chi trả
  - Generic alternatives
- Filter theo BHYT coverage
- Filter theo VN approved

---

## Deliverables

1. ✅ Evidence Grading System hoàn chỉnh
2. ✅ Evidence badges hiển thị trong Protocols, Guidelines, Drugs
3. ✅ Bộ Y tế Guidelines trong Guidelines Tracker
4. ✅ Local Protocols phù hợp VN
5. ✅ Drug Formulary VN tích hợp vào Drug Database

---

## Success Criteria

- ✅ Tất cả recommendations có evidence grade
- ✅ Evidence badges hiển thị rõ ràng
- ✅ Guidelines VN có thể search và filter
- ✅ Protocols VN được tag và filter được
- ✅ Drug Formulary VN hiển thị đầy đủ trong drug detail

---

## Timeline

**Week 1-2:** Evidence Grading System
- Tạo schema và components
- Áp dụng cho Protocols

**Week 3-4:** Guidelines VN
- Thu thập và cấu trúc dữ liệu
- Tích hợp vào Guidelines Tracker

**Week 5-6:** Local Protocols
- Xác định và tạo protocols mới
- Tag và filter

**Week 7-8:** Drug Formulary VN
- Thu thập và cấu trúc dữ liệu
- Tích hợp vào Drug Database

---

**Bắt đầu:** 2025-01-30  
**Dự kiến hoàn thành:** 2025-03-30
