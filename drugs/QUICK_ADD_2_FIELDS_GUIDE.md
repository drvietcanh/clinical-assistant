# Hướng Dẫn Nhanh Bổ Sung 2 Field Còn Thiếu

## 🎯 Mục Tiêu
Bổ sung đầy đủ 2 field còn thiếu cho 108 thuốc còn lại.

## ⚡ Cách Làm Nhanh Nhất

### Bước 1: Tìm thuốc cần bổ sung
```bash
python find_drugs_missing_2_fields.py
```

### Bước 2: Xác định pattern thiếu field
- Pattern 1: `contraindications_detail` + `renal_adjustment`
- Pattern 2: `contraindications_detail` + `reversal_agents`
- Pattern 3: `black_box_warnings` + `reversal_agents`
- Pattern 4: `black_box_warnings` + `contraindications_detail`
- Pattern 5: `drug_interactions` (nếu có `drug_interactions_detail`)

### Bước 3: Tìm file chứa thuốc
```bash
grep -r "DrugName" drugs/
```

### Bước 4: Bổ sung field theo template

#### Template 1: `contraindications_detail` (copy từ `contraindications`)
```python
"contraindications_detail": {
    "tuyệt_đối": drug_data["contraindications"]["tuyệt_đối"].copy(),
    "tương_đối": drug_data["contraindications"]["tương_đối"].copy()
},
```

#### Template 2: `renal_adjustment`
```python
"renal_adjustment": {
    "normal": "Không cần chỉnh liều",
    "30_60": "Thận trọng, có thể cần giảm liều",
    "under_30": "Thận trọng, giảm liều (thải trừ qua thận)",
    "dialysis": "Thận trọng, giảm liều. [Drug] không được lọc sạch hiệu quả qua thẩm phân máu.",
    "notes": "[Drug] thải trừ qua thận. Suy thận có thể tăng nguy cơ tích lũy."
},
```

#### Template 3: `reversal_agents`
```python
"reversal_agents": {
    "available": False,
    "agents": [],
    "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ."
},
```

#### Template 4: `black_box_warnings`
```python
"black_box_warnings": None  # Nếu không có cảnh báo đặc biệt
```

#### Template 5: `drug_interactions` (copy từ `drug_interactions_detail`)
```python
"drug_interactions": {
    "major": drug_data["drug_interactions_detail"]["major"].copy(),
    "moderate": drug_data["drug_interactions_detail"]["moderate"].copy(),
    "minor": drug_data["drug_interactions_detail"]["minor"].copy()
},
```

## 📝 Checklist Nhanh

- [ ] Tìm thuốc trong danh sách
- [ ] Xác định pattern thiếu field
- [ ] Tìm file chứa thuốc
- [ ] Copy template phù hợp
- [ ] Thay thế [Drug] bằng tên thuốc
- [ ] Kiểm tra syntax
- [ ] Chạy script kiểm tra: `python find_drugs_missing_2_fields.py`

## 🔍 Ví Dụ Thực Tế

### Ví dụ 1: Bổ sung cho Clonazepam
```python
# File: drugs/drug_modules/neurological/benzodiazepines.py
# Pattern: contraindications_detail + renal_adjustment

# Sau dòng "contraindications": {...}
"contraindications_detail": {
    "tuyệt_đối": drug_data["contraindications"]["tuyệt_đối"].copy(),
    "tương_đối": drug_data["contraindications"]["tương_đối"].copy()
},
"renal_adjustment": {
    "normal": "Không cần chỉnh liều",
    "30_60": "Thận trọng, có thể cần giảm liều",
    "under_30": "Thận trọng, giảm liều (thải trừ qua thận)",
    "dialysis": "Thận trọng, giảm liều. Clonazepam không được lọc sạch hiệu quả qua thẩm phân máu.",
    "notes": "Clonazepam thải trừ một phần qua thận. Suy thận có thể tăng nguy cơ tích lũy."
},
```

### Ví dụ 2: Bổ sung cho Amoxicillin
```python
# File: drugs/drug_modules/antimicrobial/antibiotics/penicillins.py
# Pattern: contraindications_detail + reversal_agents

# Sau dòng "contraindications": {...}
"contraindications_detail": {
    "tuyệt_đối": drug_data["contraindications"]["tuyệt_đối"].copy(),
    "tương_đối": drug_data["contraindications"]["tương_đối"].copy()
},
"reversal_agents": {
    "available": False,
    "agents": [],
    "notes": "Không có antidote đặc hiệu. Điều trị quá liều amoxicillin chủ yếu là hỗ trợ."
},
```

## ⚠️ Lưu Ý Quan Trọng

1. **Luôn copy từ field có sẵn** - Nếu có `contraindications` dict, copy sang `contraindications_detail`
2. **Kiểm tra syntax** - Đảm bảo dấu phẩy, ngoặc đúng
3. **Thay thế [Drug]** - Thay bằng tên thuốc thực tế trong notes
4. **Kiểm tra sau mỗi nhóm** - Chạy script kiểm tra thường xuyên
5. **Backup trước khi sửa** - Commit hoặc backup file trước khi sửa nhiều

## 🚀 Tối Ưu Hóa

### Làm theo nhóm file
1. Tìm tất cả thuốc trong cùng 1 file
2. Bổ sung cùng lúc cho tất cả thuốc trong file đó
3. Kiểm tra file đó
4. Chuyển sang file tiếp theo

### Làm theo pattern
1. Tìm tất cả thuốc có cùng pattern (ví dụ: tất cả SSRIs)
2. Bổ sung cùng lúc cho nhóm đó
3. Kiểm tra nhóm đó

## 📊 Tiến Độ

- **Đã hoàn thành:** 15/123 thuốc (12.2%)
- **Còn lại:** 108 thuốc
- **Mục tiêu:** Hoàn thành 100%

