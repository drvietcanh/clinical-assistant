# Cấu Trúc Field Thuốc

## Tổng Quan

Mỗi thuốc trong hệ thống có cấu trúc field chuẩn gồm:
- **14 field chuẩn** (bắt buộc)
- **8 field bổ sung** (khuyến nghị)

## 14 Field Chuẩn

### 1. group
**Type:** `str`  
**Mô tả:** Nhóm thuốc  
**Ví dụ:** `"Cardiovascular - ACE Inhibitor"`

### 2. vietnamese_name
**Type:** `str`  
**Mô tả:** Tên thuốc tiếng Việt (có thể kèm tên thương mại)  
**Ví dụ:** `"Metformin (Glucophage, Glumetza)"`

### 3. administration
**Type:** `list[str]`  
**Mô tả:** Đường dùng  
**Ví dụ:** `["PO", "IV"]`  
**Giá trị hợp lệ:** `PO`, `IV`, `IM`, `SC`, `Inhalation`, `Topical`, `Vaginal`, `Rectal`, `Transdermal`

### 4. indications
**Type:** `list[str]`  
**Mô tả:** Chỉ định  
**Ví dụ:** `["Type 2 diabetes", "Polycystic ovary syndrome"]`

### 5. dosage
**Type:** `dict`  
**Mô tả:** Liều dùng  
**Ví dụ:**
```python
{
    "adult": "500-2000mg PO x 2 lần/ngày",
    "pediatric": "10-15mg/kg PO x 2 lần/ngày",
    "notes": "Uống với thức ăn"
}
```

### 6. side_effects
**Type:** `list[str]`  
**Mô tả:** Tác dụng phụ  
**Ví dụ:** `["Buồn nôn", "Tiêu chảy", "Đau bụng"]`

### 7. contraindications
**Type:** `list[str]` hoặc `dict`  
**Mô tả:** Chống chỉ định  
**Ví dụ (list):**
```python
["Suy thận nặng", "Nhiễm toan lactic"]
```

**Ví dụ (dict):**
```python
{
    "tuyệt_đối": ["Suy thận nặng"],
    "tương_đối": ["Suy thận nhẹ - thận trọng"]
}
```

### 8. interactions
**Type:** `list[str]` hoặc `dict`  
**Mô tả:** Tương tác thuốc  
**Ví dụ (list):**
```python
["Tăng nguy cơ nhiễm toan lactic với contrast"]
```

**Ví dụ (dict):**
```python
{
    "giảm_hiệu_quả": ["Thuốc cảm ứng CYP3A4"],
    "tăng_nguy_cơ": ["Thuốc ức chế CYP3A4"]
}
```

### 9. pregnancy
**Type:** `str`  
**Mô tả:** Phân loại thai kỳ (FDA category)  
**Ví dụ:** `"B - An toàn trong thai kỳ"`  
**Giá trị hợp lệ:** `A`, `B`, `C`, `D`, `X`

### 10. mechanism_of_action
**Type:** `str` hoặc `tuple`  
**Mô tả:** Cơ chế tác dụng  
**Ví dụ:** `"Ức chế tổng hợp glucose ở gan, tăng nhạy cảm insulin"`

### 11. monitoring
**Type:** `list[str]`  
**Mô tả:** Theo dõi  
**Ví dụ:** `["Đường huyết", "Chức năng thận", "Nhiễm toan lactic"]`

### 12. precautions
**Type:** `list[str]` hoặc `dict`  
**Mô tả:** Thận trọng  
**Ví dụ (list):**
```python
["Thận trọng ở suy thận", "Tránh dùng contrast"]
```

**Ví dụ (dict):**
```python
{
    "quan_trọng": ["CHỐNG CHỈ ĐỊNH ở suy thận nặng"],
    "khác": ["Thận trọng ở suy thận nhẹ"]
}
```

### 13. pharmacokinetics
**Type:** `dict`  
**Mô tả:** Dược động học  
**Ví dụ:**
```python
{
    "half_life": "6 giờ",
    "onset": "2-3 giờ",
    "duration": "12-24 giờ",
    "protein_binding": "Minimal",
    "metabolism": "Gan",
    "clearance": "Thận"
}
```

### 14. storage
**Type:** `str`  
**Mô tả:** Bảo quản  
**Ví dụ:** `"Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm"`

## 8 Field Bổ Sung

### 15. black_box_warnings
**Type:** `str` hoặc `None`  
**Mô tả:** Cảnh báo đen (black box warnings)  
**Ví dụ:** `"Nguy cơ nhiễm toan lactic - NGUY HIỂM"`

### 16. drug_interactions
**Type:** `dict`  
**Mô tả:** Tương tác thuốc chi tiết  
**Ví dụ:**
```python
{
    "major": [
        {
            "drug": "Contrast media",
            "mechanism": "Tăng nguy cơ nhiễm toan lactic",
            "effect": "NGUY HIỂM",
            "management": "Ngừng metformin 48h trước và sau contrast"
        }
    ],
    "moderate": [],
    "minor": []
}
```

### 17. pregnancy_lactation
**Type:** `dict`  
**Mô tả:** Thông tin thai kỳ và cho con bú chi tiết  
**Ví dụ:**
```python
{
    "fda_category": "B",
    "pregnancy_details": "An toàn trong thai kỳ",
    "lactation": {
        "safety": "Compatible",
        "details": "Bài tiết vào sữa mẹ ở nồng độ thấp",
        "recommendation": "Có thể dùng khi cho con bú"
    }
}
```

### 18. hepatic_adjustment
**Type:** `dict`  
**Mô tả:** Điều chỉnh liều ở bệnh nhân suy gan  
**Ví dụ:**
```python
{
    "mild": "Không cần điều chỉnh",
    "moderate": "Thận trọng",
    "severe": "CHỐNG CHỈ ĐỊNH",
    "notes": "Chuyển hóa qua gan"
}
```

### 19. overdose_management
**Type:** `dict`  
**Mô tả:** Xử trí quá liều  
**Ví dụ:**
```python
{
    "symptoms": ["Buồn nôn", "Nôn", "Nhiễm toan lactic"],
    "antidote": "Không có antidote đặc hiệu",
    "treatment": [
        "Ngừng ngay metformin",
        "Điều trị hỗ trợ",
        "Lọc máu nếu cần"
    ],
    "monitoring": "Theo dõi nhiễm toan lactic"
}
```

### 20. reversal_agents
**Type:** `dict` hoặc `None`  
**Mô tả:** Thuốc giải độc  
**Ví dụ:**
```python
{
    "available": False,
    "agents": [],
    "notes": "Không có antidote đặc hiệu"
}
```

### 21. administration_instructions
**Type:** `dict`  
**Mô tả:** Hướng dẫn dùng thuốc chi tiết  
**Ví dụ:**
```python
{
    "oral": {
        "with_food": "Uống với thức ăn",
        "timing": "500-2000mg PO x 2 lần/ngày",
        "notes": "Uống đều đặn"
    }
}
```

### 22. references
**Type:** `dict`  
**Mô tả:** Tài liệu tham khảo  
**Ví dụ:**
```python
{
    "primary_sources": [
        "FDA Drug Label - Metformin",
        "ADA Guidelines - Type 2 Diabetes"
    ],
    "last_updated": "2025-02-18",
    "evidence_level": "A - Dựa trên FDA và guidelines"
}
```

## Thứ Tự Field Chuẩn

Field phải được sắp xếp theo thứ tự sau:

1. group
2. vietnamese_name
3. administration
4. indications
5. dosage
6. side_effects
7. contraindications
8. interactions
9. pregnancy
10. mechanism_of_action
11. monitoring
12. precautions
13. pharmacokinetics
14. storage
15. black_box_warnings
16. drug_interactions
17. pregnancy_lactation
18. hepatic_adjustment
19. overdose_management
20. reversal_agents
21. administration_instructions
22. references

## Field Khác (Tùy Chọn)

Các field khác có thể có:
- `risk_flags` - Cờ cảnh báo rủi ro
- `organ_toxicity` - Độc tính cơ quan
- `pediatric_dosing` - Liều trẻ em
- `geriatric_dosing` - Liều người già
- `brand_names` - Tên thương mại
- `cost_estimate` - Ước tính chi phí
- `contraindications_detail` - Chi tiết chống chỉ định
- `renal_adjustment` - Điều chỉnh liều ở suy thận
- `last_updated` - Ngày cập nhật
- `evidence_level` - Mức độ bằng chứng

## Validation

Sử dụng `FieldValidator` để kiểm tra:
- Field có tồn tại không
- Kiểu dữ liệu đúng không
- Field không rỗng
- Thứ tự field đúng không
- Format field đúng không

## Standardization

Sử dụng `FieldStandardizer` để:
- Sắp xếp lại thứ tự field
- Bổ sung field thiếu
- Sửa format field không đúng

## Ví Dụ Đầy Đủ

Xem các file trong `drugs/drug_modules/` để tham khảo cấu trúc đầy đủ của thuốc.

