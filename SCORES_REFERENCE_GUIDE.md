# HƯỚNG DẪN THAM KHẢO HỆ THỐNG SCORES

## 📋 Mục lục
1. [Cấu trúc hệ thống](#cấu-trúc-hệ-thống)
2. [Danh sách scores theo chuyên khoa](#danh-sách-scores-theo-chuyên-khoa)
3. [Cách thêm score mới](#cách-thêm-score-mới)
4. [Quy ước đặt tên](#quy-ước-đặt-tên)
5. [Kiểm tra và debug](#kiểm-tra-và-debug)

---

## 🏗️ Cấu trúc hệ thống

### Cấu trúc thư mục
```
scores/
├── config.py                    # File cấu hình chính - Đăng ký tất cả scores
├── __init__.py                  # Router chính
├── emergency/                   # Cấp cứu & Hồi sức
│   ├── __init__.py              # Router cho emergency
│   ├── shock_index.py           # File implementation
│   └── ...
├── cardiology/                  # Tim mạch
├── respiratory/                  # Hô hấp
├── neurology/                    # Thần kinh
├── gi/                          # Tiêu hóa - Gan Mật
├── hematology/                  # Huyết học & Đông máu
├── psychiatry/                  # Tâm thần - Tâm Lý
├── geriatrics/                  # Lão khoa
└── ...
```

### File quan trọng

1. **`scores/config.py`**
   - Đăng ký tất cả scores trong hệ thống
   - Cấu trúc: `SCORES_BY_SPECIALTY` dictionary
   - Mỗi score có: `name`, `desc`, `status`

2. **`scores/{specialty}/__init__.py`**
   - Router cho từng chuyên khoa
   - Import các render functions
   - Mapping score ID → render function

3. **`scores/{specialty}/{score_name}.py`**
   - File implementation của score
   - Chứa function `render()` và logic tính toán

---

## 📊 Danh sách scores theo chuyên khoa

### 🚨 Cấp cứu & Hồi sức (Emergency & Critical Care)
**Thư mục:** `scores/emergency/`

1. NEWS2 - National Early Warning Score 2
2. MEWS - Modified Early Warning Score
3. qSOFA - Quick SOFA
4. SOFA - Sequential Organ Failure Assessment
5. SOFA-2 (2025) ⭐
6. APACHE II
7. APACHE III
8. APACHE IV ⭐
9. SAPS II
10. SAPS III
11. MODS - Multiple Organ Dysfunction Score
12. LODS - Logistic Organ Dysfunction Score
13. HOSPITAL Score
14. LACE Index
15. Alvarado Score ⭐
16. ROX Index ⭐
17. Lactate Clearance ⭐
18. Charlson Index ⭐
19. CRB-65 Score ⭐
20. SCORTEN Score ⭐
21. RDOS ⭐
22. CPIS ⭐⭐
23. San Francisco Syncope Rule ⭐⭐
24. Shock Index ⭐ (MỚI)
25. Marshall Score ⭐⭐ (MỚI)

**Còn thiếu:**
- GCS-Pupils Score

---

### ❤️ Tim mạch (Cardiology)
**Thư mục:** `scores/cardiology/`

1. ASCVD Risk Calculator ⭐
2. NYHA Classification
3. Killip Classification
4. Duke Criteria
5. CHA₂DS₂-VASc
6. HAS-BLED
7. SCORE2
8. SCORE2-OP
9. HEART Score
10. TIMI Risk Score
11. GRACE Score
12. CRUSADE Score ⭐
13. PRECISE-DAPT Score ⭐
14. DAPT Score ⭐
15. ARC-HBR Criteria ⭐⭐
16. PCP-HF Risk Score ⭐
17. Framingham Risk Score
18. Corrected QT (QTc)
19. EuroSCORE II ⭐⭐⭐
20. ATRIA Bleeding Risk ⭐⭐
21. ORBIT Bleeding Risk ⭐⭐
22. SAMe-TT₂R₂ Score ⭐⭐
23. Duke Treadmill Score ⭐⭐
24. BARC Classification ⭐⭐ (MỚI)
25. SYNTAX Score ⭐⭐ (MỚI)
26. HFA-ICOS Multiple Myeloma ⭐⭐⭐
27. HFA-ICOS CML TKI ⭐⭐⭐
28. HFA-ICOS RAF/MEK ⭐⭐⭐
29. HFA-ICOS VEGF ⭐⭐⭐
30. HFA-ICOS HER2 ⭐⭐⭐
31. HFA-ICOS Anthracycline ⭐⭐⭐

**Còn thiếu:**
- SYNTAX Score II

---

### 🫁 Hô hấp (Respiratory)
**Thư mục:** `scores/respiratory/`

1. PERC Rule
2. CURB-65
3. PSI/PORT Score
4. Wells PE Score
5. PESI - Pulmonary Embolism Severity Index
6. SMART-COP
7. BODE Index
8. ARDS Berlin Definition
9. mMRC Dyspnea Scale ⭐
10. ACT - Asthma Control Test ⭐
11. Murray Lung Injury Score ⭐⭐
12. GOLD Criteria ⭐⭐
13. sPESI ⭐⭐
14. Hestia Score ⭐⭐
15. MuLBSTA Score ⭐⭐ (MỚI)
16. HACOR Score ⭐⭐ (MỚI)

---

### 🧠 Thần kinh (Neurology)
**Thư mục:** `scores/neurology/`

1. GCS - Glasgow Coma Scale
2. NIHSS - NIH Stroke Scale
3. ICH Score
4. Hunt & Hess Scale
5. mRS - Modified Rankin Scale
6. ASPECTS - Alberta Stroke Program Early CT Score
7. ABCD2 Score
8. Barthel Index
9. FOUR Score
10. Canadian CT Head Rule ⭐
11. FAST-ED Score ⭐⭐
12. ICANS Consensus Grading ⭐⭐⭐
13. HINTS Exam ⭐⭐
14. Canadian Stroke Scale ⭐ (MỚI)
15. DRAGON Score ⭐⭐ (MỚI)
16. THRIVE Score ⭐⭐ (MỚI)
17. SEDAN Score ⭐⭐ (MỚI)

---

### 🩸 Tiêu hóa - Gan Mật (GI/Hepatology)
**Thư mục:** `scores/gi/`

1. Child-Pugh Score
2. MELD Score
3. MELD 3.0 ⭐⭐⭐ (MỚI)
4. APRI Score ⭐⭐
5. GAHS ⭐⭐
6. Lactulose Calculator ⭐ (MỚI)
7. ALBI Score ⭐⭐ (MỚI)
8. NAFLD Fibrosis Score ⭐⭐ (MỚI)

---

### 🩺 Huyết học & Đông máu (Hematology)
**Thư mục:** `scores/hematology/`

1. Wells DVT Score
2. Four T's Score
3. DIC Score
4. Padua Score
5. Warfarin Dosing ⭐ (MỚI)
6. INR Target ⭐ (MỚI)
7. Bleeding Risk ⭐ (MỚI)

**Còn thiếu:**
- HEP Score
- PLASMIC Score

---

### 🧠 Tâm thần - Tâm Lý (Psychiatry/Psychology)
**Thư mục:** `scores/psychiatry/`

1. PHQ-9 - Patient Health Questionnaire
2. GAD-7 - Generalized Anxiety Disorder
3. MMSE - Mini Mental State Exam
4. MoCA - Montreal Cognitive Assessment
5. CAM - Confusion Assessment Method
6. CIWA-Ar
7. COWS - Clinical Opiate Withdrawal
8. GMAWS ⭐
9. DASS-21 ⭐⭐ (MỚI)
10. GAF - Global Assessment of Functioning ⭐⭐ (MỚI)

**Còn thiếu:**
- MADRS
- HAM-D

---

### 👴 Lão khoa (Geriatrics)
**Thư mục:** `scores/geriatrics/`

1. CFS - Clinical Frailty Scale
2. Morse Fall Scale
3. MMSE Geriatrics (đã đổi tên để tránh trùng)
4. MoCA Geriatrics (đã đổi tên để tránh trùng)
5. Beers Criteria
6. STOPP/START

**Còn thiếu:**
- FRAIL Scale
- Edmonton Frail Scale
- SPMSQ

---

### 🧪 Thận - Điện giải (Nephrology)
**Thư mục:** `scores/nephrology/`

1. RIFLE/AKI Criteria
2. KDIGO AKI Staging
3. eGFR Calculator
4. FENa Calculator
5. ... (xem chi tiết trong config.py)

---

### Các chuyên khoa khác
- 🦴 Chấn thương & Chỉnh Hình (Trauma/Orthopedics)
- 👂 Tai Mũi Họng (ENT)
- 👶 Nhi khoa (Pediatrics)
- 🤰 Sản khoa (Obstetrics)
- 💉 Nội tiết - Chuyển hóa (Endocrinology/Metabolism)
- 🦴 Thấp khớp - Miễn Dịch (Rheumatology/Immunology)
- 🦠 Nhiễm khuẩn (Infectious Disease)
- 🩹 Da liễu (Dermatology)
- 🎗️ Ung thư (Oncology)
- 🔪 Phẫu thuật & Gây mê (Surgery/Anesthesia)
- 👁️ Mắt (Ophthalmology)
- 😣 Đánh giá đau (Pain Assessment)
- 🛏️ Chăm sóc điều dưỡng (Nursing Care)

---

## ➕ Cách thêm score mới

### Bước 1: Tạo file implementation
Tạo file mới trong thư mục chuyên khoa tương ứng:
```python
# scores/{specialty}/{score_name}.py

"""
{Score Name}
============

Description of the score.

Reference:
- Author, et al. Title. Journal. Year;Volume:Pages.

Clinical Utility:
- Use case 1
- Use case 2
"""

import streamlit as st
from config.theme import COLORS
# ... imports ...

def calculate_{score_name}(...):
    """Calculate score"""
    # Logic here
    return {
        "score": score,
        "risk_level": risk_level,
        "interpretation": "...",
        ...
    }

def render():
    """{Score Name} Calculator"""
    # UI implementation
    # Use standard components:
    # - render_score_result()
    # - render_score_breakdown()
    # - save_calculation_to_history()
    # - render_share_section()
    # - render_scores_export()
    # - render_history_ui()
    # - render_references_section()
    pass
```

### Bước 2: Đăng ký trong module __init__.py
Thêm vào `scores/{specialty}/__init__.py`:

```python
from .{score_name} import render as render_{score_name}

def render_{specialty}_calculator(calculator_id):
    calculators = {
        # ... existing ...
        "{Score ID}": render_{score_name},
    }
    # ...
```

### Bước 3: Đăng ký trong config.py
Thêm vào `scores/config.py` trong `SCORES_BY_SPECIALTY`:

```python
"{Specialty Name}": {
    # ... existing scores ...
    "{Score ID}": {
        "name": "{Score Name} ⭐⭐",
        "desc": "Mô tả ngắn gọn về score",
        "status": "✅"
    },
}
```

### Bước 4: Kiểm tra
1. Kiểm tra linting: `read_lints`
2. Kiểm tra routing: Đảm bảo score ID khớp
3. Kiểm tra trùng lặp: Đảm bảo không có score ID trùng
4. Test trong ứng dụng

---

## 📝 Quy ước đặt tên

### Score ID
- Sử dụng tên chính thức của score
- Viết hoa chữ cái đầu mỗi từ
- Ví dụ: "Shock Index", "MELD 3.0", "DASS-21"

### File name
- Chuyển sang snake_case
- Ví dụ: `shock_index.py`, `meld3.py`, `dass21.py`

### Function name
- Render function: `render_{score_name}`
- Calculate function: `calculate_{score_name}`

### Import name
```python
from .{file_name} import render as render_{score_name}
```

---

## 🔍 Kiểm tra và debug

### Kiểm tra trùng lặp
```python
# Tạo script check_duplicates.py
import re
from collections import Counter

with open('scores/config.py', 'r') as f:
    content = f.read()
    
# Extract score IDs
pattern = r'"([^"]+)":\s*\{'
matches = re.findall(pattern, content)
counter = Counter(matches)
duplicates = {k: v for k, v in counter.items() if v > 1}
print(duplicates)
```

### Kiểm tra routing
```bash
# Grep để tìm score ID trong __init__.py
grep -r "Score ID" scores/{specialty}/__init__.py
```

### Kiểm tra linting
```python
read_lints(['scores/{specialty}/{score_name}.py'])
```

---

## 📚 Tài liệu tham khảo

### Components có sẵn
- `components.ui.scoring`: render_score_result, render_score_breakdown
- `components.calculation_history`: save_calculation_to_history, render_history_ui
- `components.share_results`: render_share_section, load_shared_result_from_url
- `components.smart_suggestions`: render_suggestions
- `components.risk_color_coding`: render_risk_badge, get_risk_level
- `components.score_charts`: render_risk_gauge_chart, render_risk_bar_chart
- `components.scores_export`: render_export_section
- `components.references`: render_references_section

### Theme colors
```python
from config.theme import COLORS
# COLORS['success'], COLORS['warning'], COLORS['danger'], COLORS['info']
```

### Validation
```python
from scores.utils.validation import (
    validate_age,
    validate_lab_value,
    ...
)
```

---

## ✅ Checklist khi thêm score mới

- [ ] Tạo file implementation với đầy đủ docstring
- [ ] Implement calculate function
- [ ] Implement render function với UI đầy đủ
- [ ] Thêm import vào `__init__.py`
- [ ] Thêm routing vào `__init__.py`
- [ ] Đăng ký trong `config.py`
- [ ] Kiểm tra không trùng lặp score ID
- [ ] Kiểm tra linting
- [ ] Test trong ứng dụng
- [ ] Thêm references nếu có

---

## 🎯 Scores còn thiếu (theo kế hoạch)

### Emergency
- GCS-Pupils Score

### Cardiology
- SYNTAX Score II

### Psychiatry
- MADRS
- HAM-D

### Geriatrics
- FRAIL Scale
- Edmonton Frail Scale
- SPMSQ

### Hematology
- HEP Score
- PLASMIC Score

---

**Cập nhật lần cuối:** 2025-01-XX
**Tổng số scores:** ~270+ scores
**Scores mới đã thêm:** 24 scores
