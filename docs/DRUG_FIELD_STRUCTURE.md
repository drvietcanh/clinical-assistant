# Cấu Trúc Field Chuẩn Cho Thuốc

## Tổng Quan

Tài liệu này mô tả chi tiết cấu trúc field chuẩn cho tất cả thuốc trong hệ thống. Tất cả thuốc phải tuân theo cấu trúc này để đảm bảo tính nhất quán.

## Thứ Tự Field Chuẩn

### STANDARD_14_FIELDS (Bắt buộc)

Các field này là bắt buộc và phải có theo thứ tự sau:

1. `group` (string)
2. `vietnamese_name` (string)
3. `administration` (list)
4. `indications` (list)
5. `dosage` (dict)
6. `side_effects` (list)
7. `contraindications` (list hoặc dict)
8. `interactions` (list)
9. `pregnancy` (string)
10. `mechanism_of_action` (string)
11. `monitoring` (list)
12. `precautions` (list)
13. `pharmacokinetics` (dict)
14. `storage` (string)

### ADDITIONAL_8_FIELDS (Bổ sung)

Các field này được khuyến nghị và đặt sau STANDARD fields:

15. `black_box_warnings` (string hoặc None)
16. `drug_interactions` (dict)
17. `pregnancy_lactation` (dict)
18. `hepatic_adjustment` (dict)
19. `overdose_management` (dict)
20. `reversal_agents` (dict hoặc None)
21. `administration_instructions` (dict)
22. `references` (dict)

### ADDITIONAL_COMMON_FIELDS (Thường dùng)

23. `renal_adjustment` (dict)
24. `contraindications_detail` (dict)

## Chi Tiết Từng Field

### 1. group
- **Type:** string
- **Required:** Yes
- **Description:** Nhóm thuốc
- **Example:** `"Cardiovascular - ACE Inhibitor"`

### 2. vietnamese_name
- **Type:** string
- **Required:** Yes
- **Description:** Tên tiếng Việt và tên thương mại
- **Example:** `"Benazepril, Lotensin"`

### 3. administration
- **Type:** list of strings
- **Required:** Yes
- **Description:** Đường dùng thuốc
- **Valid values:** `["PO"]`, `["IV", "IM"]`, `["SC"]`, `["Inhalation"]`, `["Topical"]`, etc.
- **Example:** `["PO"]`

### 4. indications
- **Type:** list of strings
- **Required:** Yes
- **Description:** Danh sách chỉ định
- **Example:** `["Tăng huyết áp", "Suy tim"]`

### 5. dosage
- **Type:** dict
- **Required:** Yes
- **Description:** Liều dùng cho các trường hợp khác nhau
- **Structure:**
  ```python
  {
      "adult": "10-40mg x 1-2 lần/ngày",
      "adult_initial": "10mg x 1 lần/ngày",
      "pediatric": "...",
      "notes": "..."
  }
  ```

### 6. side_effects
- **Type:** list of strings
- **Required:** Yes
- **Description:** Danh sách tác dụng phụ
- **Example:** `["Ho khan", "Tăng kali máu", "Hạ huyết áp"]`

### 7. contraindications
- **Type:** list of strings hoặc dict
- **Required:** Yes
- **Description:** Chống chỉ định
- **Format 1 (list):** `["Dị ứng", "Có thai"]`
- **Format 2 (dict):** 
  ```python
  {
      "tuyệt_đối": ["..."],
      "tương_đối": ["..."]
  }
  ```

### 8. interactions
- **Type:** list of strings
- **Required:** Yes
- **Description:** Tương tác thuốc dạng text
- **Example:** `["Kali bổ sung: tăng nguy cơ tăng kali máu"]`

### 9. pregnancy
- **Type:** string
- **Required:** Yes
- **Description:** FDA pregnancy category
- **Format:** `"D - Chống chỉ định trong thai kỳ"` hoặc `"D"`
- **Valid categories:** A, B, C, D, X

### 10. mechanism_of_action
- **Type:** string
- **Required:** Yes
- **Description:** Cơ chế tác dụng chi tiết
- **Example:** `"Ức chế men chuyển angiotensin (ACE)..."`

### 11. monitoring
- **Type:** list of strings
- **Required:** Yes
- **Description:** Các chỉ số cần theo dõi
- **Example:** `["Huyết áp", "Creatinine", "Kali máu"]`

### 12. precautions
- **Type:** list of strings
- **Required:** Yes
- **Description:** Các lưu ý thận trọng
- **Example:** `["Khởi đầu liều thấp ở bệnh nhân suy tim"]`

### 13. pharmacokinetics
- **Type:** dict
- **Required:** Yes
- **Description:** Dược động học
- **Structure:**
  ```python
  {
      "half_life": "10-12 giờ",
      "onset": "1 giờ",
      "duration": "24 giờ",
      "protein_binding": "~96%",
      "clearance": "Thận"
  }
  ```

### 14. storage
- **Type:** string
- **Required:** Yes
- **Description:** Điều kiện bảo quản
- **Example:** `"Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm"`

### 15. black_box_warnings
- **Type:** string hoặc None
- **Required:** No (khuyến nghị)
- **Description:** Cảnh báo đen từ FDA
- **Example:** `"CHỐNG CHỈ ĐỊNH trong thai kỳ..."` hoặc `None`

### 16. drug_interactions
- **Type:** dict
- **Required:** No (khuyến nghị)
- **Description:** Tương tác thuốc chi tiết
- **Structure:**
  ```python
  {
      "major": [
          {
              "drug": "Tên thuốc",
              "mechanism": "Cơ chế tương tác",
              "effect": "Tác dụng",
              "management": "Xử trí"
          }
      ],
      "moderate": [...],
      "minor": [...]
  }
  ```

### 17. pregnancy_lactation
- **Type:** dict
- **Required:** No (khuyến nghị)
- **Description:** Thông tin chi tiết về thai kỳ và cho con bú
- **Structure:**
  ```python
  {
      "fda_category": "D",
      "pregnancy_details": "Chi tiết về thai kỳ...",
      "lactation": {
          "safety": "Caution",
          "details": "Chi tiết về cho con bú...",
          "recommendation": "Khuyến nghị..."
      }
  }
  ```

### 18. hepatic_adjustment
- **Type:** dict
- **Required:** No (khuyến nghị)
- **Description:** Điều chỉnh liều suy gan
- **Structure:**
  ```python
  {
      "mild": "Thận trọng",
      "moderate": "Giảm liều",
      "severe": "CHỐNG CHỈ ĐỊNH",
      "notes": "Ghi chú thêm..."
  }
  ```

### 19. overdose_management
- **Type:** dict
- **Required:** No (khuyến nghị)
- **Description:** Xử trí quá liều
- **Structure:**
  ```python
  {
      "symptoms": ["Triệu chứng 1", "Triệu chứng 2"],
      "antidote": "Thuốc giải độc (nếu có)",
      "treatment": ["Điều trị 1", "Điều trị 2"],
      "monitoring": "Theo dõi..."
  }
  ```

### 20. reversal_agents
- **Type:** dict hoặc None
- **Required:** No (khuyến nghị)
- **Description:** Thuốc giải độc
- **Structure:**
  ```python
  {
      "available": True/False,
      "agents": ["Tên thuốc giải độc"],
      "notes": "Ghi chú..."
  }
  ```
- **Note:** Có thể là `None` nếu không có thuốc giải độc

### 21. administration_instructions
- **Type:** dict
- **Required:** No (khuyến nghị)
- **Description:** Hướng dẫn dùng thuốc chi tiết
- **Structure:**
  ```python
  {
      "oral": {
          "with_food": "Uống với thức ăn",
          "timing": "Trước bữa ăn"
      },
      "iv": {
          "rate": "Tốc độ truyền",
          "dilution": "Pha loãng"
      }
  }
  ```

### 22. references
- **Type:** dict
- **Required:** No (khuyến nghị)
- **Description:** Tài liệu tham khảo
- **Structure:**
  ```python
  {
      "primary_sources": ["UpToDate", "FDA Labeling"],
      "last_updated": "2026-01-13",
      "evidence_level": "A"
  }
  ```

### 23. renal_adjustment
- **Type:** dict
- **Required:** No (thường dùng)
- **Description:** Điều chỉnh liều suy thận
- **Structure:**
  ```python
  {
      "normal": "Không đổi",
      "30_60": "Giảm liều",
      "under_30": "CHỐNG CHỈ ĐỊNH",
      "dialysis": "Liều sau lọc máu",
      "notes": "Ghi chú..."
  }
  ```

### 24. contraindications_detail
- **Type:** dict
- **Required:** No (thường dùng)
- **Description:** Chống chỉ định chi tiết
- **Structure:**
  ```python
  {
      "tuyệt_đối": [
          "Dị ứng thuốc",
          "Có thai"
      ],
      "tương_đối": [
          "Suy thận trung bình",
          "Tăng kali máu"
      ]
  }
  ```

## Ví Dụ Hoàn Chỉnh

```python
"Benazepril": {
    "group": "Cardiovascular - ACE Inhibitor",
    "vietnamese_name": "Benazepril, Lotensin",
    "administration": ["PO"],
    "indications": [
        "Tăng huyết áp (đơn trị hoặc phối hợp)",
        "Suy tim (off-label)"
    ],
    "dosage": {
        "adult_htn": "10-40mg x 1-2 lần/ngày",
        "adult_htn_initial": "10mg x 1 lần/ngày",
        "notes": "Điều chỉnh liều theo đáp ứng"
    },
    "side_effects": [
        "Ho khan",
        "Tăng kali máu",
        "Hạ huyết áp"
    ],
    "contraindications": [
        "Dị ứng ACE inhibitor",
        "Có thai",
        "Hẹp động mạch thận 2 bên"
    ],
    "interactions": [
        "Kali bổ sung: tăng nguy cơ tăng kali máu",
        "NSAID: giảm hiệu quả hạ huyết áp"
    ],
    "pregnancy": "D - Chống chỉ định trong thai kỳ",
    "mechanism_of_action": "Ức chế men chuyển angiotensin (ACE)...",
    "monitoring": [
        "Huyết áp",
        "Creatinine",
        "Kali máu"
    ],
    "precautions": [
        "Khởi đầu liều thấp ở bệnh nhân suy tim"
    ],
    "pharmacokinetics": {
        "half_life": "10-12 giờ",
        "onset": "1 giờ",
        "duration": "24 giờ",
        "protein_binding": "~96%",
        "clearance": "Thận"
    },
    "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
    "black_box_warnings": "CHỐNG CHỈ ĐỊNH trong thai kỳ...",
    "drug_interactions": {
        "major": [
            {
                "drug": "Kali bổ sung",
                "mechanism": "Giảm thải trừ kali",
                "effect": "Tăng kali máu nặng",
                "management": "Tránh phối hợp"
            }
        ],
        "moderate": [],
        "minor": []
    },
    "pregnancy_lactation": {
        "fda_category": "D",
        "pregnancy_details": "CHỐNG CHỈ ĐỊNH tuyệt đối...",
        "lactation": {
            "safety": "Caution",
            "details": "Bài tiết vào sữa mẹ...",
            "recommendation": "Thận trọng khi cho con bú"
        }
    },
    "hepatic_adjustment": {
        "mild": "Thường không cần chỉnh liều",
        "moderate": "Thận trọng",
        "severe": "Thận trọng",
        "notes": "..."
    },
    "overdose_management": {
        "symptoms": ["Hạ huyết áp nặng", "Chóng mặt"],
        "antidote": "Không có antidote đặc hiệu",
        "treatment": ["Truyền dịch", "Vasopressor"],
        "monitoring": "Huyết áp, nhịp tim"
    },
    "reversal_agents": {
        "available": False,
        "agents": [],
        "notes": "Không có thuốc giải độc đặc hiệu"
    },
    "administration_instructions": {
        "oral": {
            "with_food": "Có thể uống với hoặc không có thức ăn",
            "timing": "1-2 lần/ngày"
        }
    },
    "references": {
        "primary_sources": ["UpToDate", "FDA Labeling"],
        "last_updated": "2026-01-13",
        "evidence_level": "A"
    },
    "renal_adjustment": {
        "normal": "Không đổi",
        "30_60": "Liều khởi đầu 5mg/ngày",
        "under_30": "Liều khởi đầu 2.5-5mg/ngày",
        "dialysis": "Theo dõi sát",
        "notes": "..."
    },
    "contraindications_detail": {
        "tuyệt_đối": [
            "Dị ứng ACE inhibitor",
            "Có thai"
        ],
        "tương_đối": [
            "Suy thận trung bình",
            "Tăng kali máu"
        ]
    }
}
```

## Quy Tắc Quan Trọng

1. **Thứ tự field phải đúng** - STANDARD fields trước, ADDITIONAL fields sau
2. **Không được thiếu STANDARD fields** - Tất cả 14 field là bắt buộc
3. **Format phải đúng** - List phải là list, dict phải là dict
4. **Không được rỗng** - Field không được là empty string, empty list, hoặc empty dict (trừ khi None được phép)
5. **Nội dung thực tế** - Không được điền "Đang cập nhật" hoặc placeholder

## Validation

Sử dụng `validate_all_drugs.py` để kiểm tra tính hợp lệ:

```bash
python drugs/validate_all_drugs.py
```

Script sẽ kiểm tra:
- Field có tồn tại không
- Field có đúng type không
- Field có rỗng không
- Field có đúng thứ tự không
- Format có đúng không
