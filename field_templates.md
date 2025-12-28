# 📋 Templates Cho Enhanced Fields

File này chứa templates để bổ sung các enhanced fields thiếu.

---

## contraindications_detail

**Thiếu:** 346 thuốc (52.0%)

**Template:**
```python
"contraindications_detail": {
    "tuyệt_đối": [
        "Dị ứng thuốc",
        "Chống chỉ định cụ thể"
    ],
    "tương_đối": [
        "Thận trọng trong trường hợp",
        "Cần điều chỉnh liều"
    ]
}
```

**Ví dụ thuốc cần bổ sung (10 đầu tiên):**
- Digoxin
- Clonidine
- Methyldopa
- Labetalol
- Ivabradine
- Sacubitril-valsartan
- Doxazosin
- Isosorbide mononitrate
- Hydralazine
- Nesiritide

---

## reversal_agents

**Thiếu:** 175 thuốc (26.3%)

**Template:**
```python
"reversal_agents": {
    "available": True,  # hoặc False nếu không có
    "agents": [
        {
            "name": "Tên thuốc giải độc",
            "dose": "Liều dùng",
            "route": "Đường dùng",
            "notes": "Ghi chú"
        }
    ]
}
```

**Ví dụ thuốc cần bổ sung (10 đầu tiên):**
- Vericiguat
- Sotagliflozin
- Finerenone
- Nesiritide
- Simvastatin
- Bempedoic acid
- Clevidipine
- Bumetanide
- Torsemide
- Lisinopril/Hydrochlorothiazide

---

## black_box_warnings

**Thiếu:** 138 thuốc (20.7%)

**Template:**
```python
"black_box_warnings": "Cảnh báo đặc biệt quan trọng về an toàn. Mô tả chi tiết các nguy cơ nghiêm trọng."
```

**Ví dụ thuốc cần bổ sung (10 đầu tiên):**
- Nesiritide
- Nebivolol
- Ezetimibe
- Adenosine
- Lacidipine
- Clevidipine
- Hydrochlorothiazide
- Indapamide
- Sitagliptin
- Linagliptin

---

## renal_adjustment

**Thiếu:** 43 thuốc (6.5%)

**Template:**
```python
"renal_adjustment": {
    "normal": "Không đổi",
    "30_60": "Giảm liều X%",
    "under_30": "Giảm liều X% hoặc không dùng",
    "notes": "Ghi chú thêm"
}
```

**Ví dụ thuốc cần bổ sung (10 đầu tiên):**
- Lacidipine
- Hydrochlorothiazide
- Indapamide
- Insulin Lispro
- Insulin Aspart
- Insulin Glulisine
- Insulin Regular
- Insulin NPH
- Insulin Glargine
- Insulin Detemir

---

## hepatic_adjustment

**Thiếu:** 33 thuốc (5.0%)

**Template:**
```python
"hepatic_adjustment": {
    "mild": "Không đổi hoặc giảm liều X%",
    "moderate": "Giảm liều X%",
    "severe": "Không dùng hoặc giảm liều X%",
    "notes": "Ghi chú thêm"
}
```

**Ví dụ thuốc cần bổ sung (10 đầu tiên):**
- Valsartan
- Simvastatin
- Bumetanide
- Torsemide
- Insulin Lispro
- Insulin Aspart
- Insulin Glulisine
- Insulin Regular
- Insulin NPH
- Insulin Glargine

---

## drug_interactions

**Thiếu:** 32 thuốc (4.8%)

**Template:**
```python
"drug_interactions": {
    "major": [
        {
            "drug": "Tên thuốc",
            "mechanism": "Cơ chế tương tác",
            "effect": "Tác dụng",
            "management": "Cách xử lý"
        }
    ],
    "moderate": [],
    "minor": []
}
```

**Ví dụ thuốc cần bổ sung (10 đầu tiên):**
- Valsartan
- Bumetanide
- Torsemide
- Insulin Lispro
- Insulin Aspart
- Insulin Glulisine
- Insulin Regular
- Insulin NPH
- Insulin Glargine
- Insulin Detemir

---

## pregnancy_lactation

**Thiếu:** 29 thuốc (4.4%)

**Template:**
```python
"pregnancy_lactation": {
    "fda_category": "X",  # A, B, C, D, hoặc X
    "pregnancy_details": "Chi tiết về sử dụng trong thai kỳ",
    "lactation": {
        "safety": "Compatible/Incompatible/Unknown",
        "details": "Chi tiết về sử dụng khi cho con bú",
        "recommendation": "Khuyến nghị"
    }
}
```

**Ví dụ thuốc cần bổ sung (10 đầu tiên):**
- Valsartan
- Simvastatin
- Bumetanide
- Torsemide
- Insulin Lispro
- Insulin Aspart
- Insulin Glulisine
- Insulin Regular
- Insulin NPH
- Insulin Glargine

---

## overdose_management

**Thiếu:** 29 thuốc (4.4%)

**Template:**
```python
"overdose_management": {
    "symptoms": [
        "Triệu chứng 1",
        "Triệu chứng 2"
    ],
    "antidote": "Tên antidote hoặc 'Không có antidote đặc hiệu'",
    "treatment": [
        "Bước điều trị 1",
        "Bước điều trị 2"
    ],
    "monitoring": "Theo dõi các dấu hiệu sinh tồn và triệu chứng"
}
```

**Ví dụ thuốc cần bổ sung (10 đầu tiên):**
- Valsartan
- Simvastatin
- Bumetanide
- Torsemide
- Insulin Lispro
- Insulin Aspart
- Insulin Glulisine
- Insulin Regular
- Insulin NPH
- Insulin Glargine

---

## administration_instructions

**Thiếu:** 29 thuốc (4.4%)

**Template:**
```python
"administration_instructions": {
    "oral": {
        "with_food": "Uống với thức ăn hoặc không",
        "timing": "Thời điểm uống"
    },
    "iv": {
        "reconstitution": "Cách pha",
        "infusion_rate": "Tốc độ truyền",
        "compatibility": ["Thuốc tương thích"],
        "incompatibility": ["Thuốc không tương thích"],
        "notes": "Ghi chú thêm"
    }
}
```

**Ví dụ thuốc cần bổ sung (10 đầu tiên):**
- Valsartan
- Simvastatin
- Bumetanide
- Torsemide
- Insulin Lispro
- Insulin Aspart
- Insulin Glulisine
- Insulin Regular
- Insulin NPH
- Insulin Glargine

---
