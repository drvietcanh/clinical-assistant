# Quick Start Guide - Tiếp tục phát triển Disease Encyclopedia

## 📌 Trạng thái hiện tại

- ✅ **Tổng số bệnh:** 72
- ✅ **Số chuyên khoa có dữ liệu:** 21/21
- ✅ **Trạng thái:** Tất cả modules đã có dữ liệu!

## 🎯 Công việc tiếp theo

### 1. Mở rộng các module hiện có (Ưu tiên cao)

**Gợi ý bổ sung:**
- **Infectious:** COVID-19, Influenza, Giun sán
- **Gastroenterology:** Viêm dạ dày, Viêm đại tràng, Viêm tụy cấp
- **Cardiology:** Rối loạn lipid máu, Bệnh động mạch ngoại vi
- **Urology:** BPH, Ung thư tuyến tiền liệt
- **Pediatrics:** Viêm phổi trẻ em, Nhiễm khuẩn hô hấp trên
- **Ophthalmology:** Glaucoma, Tật khúc xạ

## 🚀 Cách thêm bệnh mới

### Bước 1: Mở file module
```bash
# Ví dụ: thêm vào Critical Care
diseases/modules/critical_care.py
```

### Bước 2: Thêm Disease object
```python
Disease(
    id="ards",
    name="ARDS",
    name_vn="Hội chứng suy hô hấp cấp",
    category="Critical Care",
    definition="...",
    causes=[...],
    symptoms=[...],
    diagnosis={...},
    treatment={...},
    prevention=[...],
    complications=[...],
    related_scores=[...],
    related_drugs=[...],
    related_protocols=[...],
    icd10_codes=[...]
)
```

### Bước 3: Kiểm tra
```bash
python -c "from diseases.data import DISEASES_DATABASE; print(f'Total: {len(DISEASES_DATABASE)}')"
```

## 📚 Tài liệu tham khảo

- **PROGRESS.md** - Tiến trình chi tiết, hướng dẫn đầy đủ
- **DISEASES_LIST.md** - Danh sách tất cả 60 bệnh hiện có
- **README.md** - Hướng dẫn sử dụng hệ thống

## 🔍 Kiểm tra hệ thống

### Xem tổng số bệnh:
```python
from diseases.data import DISEASES_DATABASE
print(f"Total: {len(DISEASES_DATABASE)} diseases")
```

### Xem thống kê theo chuyên khoa:
```python
from diseases.management import get_specialty_statistics
stats = get_specialty_statistics()
for category, info in stats.items():
    print(f"{category}: {info['total_diseases']} diseases")
```

### Tìm kiếm bệnh:
```python
from diseases import search_diseases
results = search_diseases("viêm phổi")
```

## ⚠️ Lưu ý quan trọng

1. **ID phải duy nhất** - Không trùng với bệnh khác
2. **Category phải khớp** - Phải khớp với tên module
3. **Cập nhật PROGRESS.md** - Ghi lại bệnh mới đã thêm
4. **Chạy linter** - Kiểm tra lỗi sau khi sửa

## 📝 Template bệnh mới

Copy template này khi thêm bệnh mới:

```python
Disease(
    id="disease_id",
    name="Disease Name",
    name_vn="Tên bệnh tiếng Việt",
    category="Specialty Name",
    definition="Định nghĩa ngắn gọn về bệnh...",
    causes=[
        "Nguyên nhân 1",
        "Nguyên nhân 2",
    ],
    symptoms=[
        "Triệu chứng 1",
        "Triệu chứng 2",
    ],
    diagnosis={
        "criteria": [
            "Tiêu chí chẩn đoán 1",
            "Tiêu chí chẩn đoán 2",
        ],
        "tests": [
            "Xét nghiệm 1",
            "Xét nghiệm 2",
        ],
        "imaging": [
            "Hình ảnh học 1",
        ]
    },
    treatment={
        "general": "Nguyên tắc điều trị chung...",
        "medications": [
            "Thuốc 1",
            "Thuốc 2",
        ],
        "procedures": [
            "Thủ thuật 1",
        ]
    },
    prevention=[
        "Biện pháp phòng ngừa 1",
    ],
    complications=[
        "Biến chứng 1",
    ],
    related_scores=["Score 1"],
    related_drugs=["Drug 1"],
    related_protocols=["Protocol 1"],
    icd10_codes=["ICD10.1"]
),
```

---

**Cập nhật lần cuối:** 2025-01-30  
**Tổng số bệnh:** 64

