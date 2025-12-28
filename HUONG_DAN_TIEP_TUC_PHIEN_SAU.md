# Hướng Dẫn Tiếp Tục Phiên Sau

## 🎯 Mục Tiêu

Tiếp tục triển khai **31 thang điểm còn lại** từ danh sách 49 thang điểm mới.

---

## 📋 Bước Đầu Tiên

1. **Đọc file tiến trình:**
   - `TIEN_TRINH_BO_SUNG_THANG_DIEM_MOI.md` - Tổng quan tiến trình
   - `DANH_SACH_THANG_DIEM_MOI_TU_HINH_ANH.md` - Danh sách chi tiết
   - `DANH_SACH_THANG_DIEM_DA_TRIEN_KHAI.md` - Danh sách đã hoàn thành

2. **Kiểm tra trạng thái:**
   - Đã triển khai: 18/49 thang điểm (36.7%)
   - Còn lại: 31 thang điểm

---

## 🚀 Ưu Tiên Triển Khai

### Phase 1: Ưu tiên RẤT CAO (7 thang điểm)

**6 thang điểm HFA-ICOS Cardio-Oncology (MỚI NHẤT 2024-2025):**
1. HFA-ICOS Baseline Cardio-Oncology Risk Assessment for Multiple Myeloma Therapies
2. HFA-ICOS Baseline Cardio-Oncology Risk Assessment for Multi-Targeted Kinase Inhibitors for CML
3. HFA-ICOS Baseline Cardio-Oncology Risk Assessment for Combination RAF and MEK Inhibitors
4. HFA-ICOS Baseline Cardio-Oncology Risk Assessment for VEGF Inhibitors
5. HFA-ICOS Baseline Cardio-Oncology Risk Assessment for HER2-Targeted Therapies
6. HFA-ICOS Baseline Cardio-Oncology Risk Assessment for Anthracycline Chemotherapy

**1 thang điểm khác:**
7. Perioperative Anticoagulation Management Algorithm

**Gợi ý:** Tạo thư mục `scores/cardiology/cardio_oncology/` để tổ chức 6 thang điểm HFA-ICOS.

### Phase 2: Ưu tiên CAO (8 thang điểm)
- Mutation-Adjusted Risk Score (MARS)
- MSKCC Risk of Recurrence
- Assure RCC Prognosis
- 2018 Leibovich Model for RCC
- ICE Score
- Và các thang điểm khác...

### Phase 3: Ưu tiên TRUNG BÌNH/THẤP (16 thang điểm)
- Các thang điểm còn lại

---

## 📝 Quy Trình Triển Khai

### Bước 1: Tạo file Python mới
```python
# scores/[specialty]/[score_name].py
"""
[Score Name] Calculator
=======================
[Description]
"""

import streamlit as st
from scores.utils.validation import ...
from components.ui.validation import render_validation_errors
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section
# ======================================

def calculate_[score_name](...):
    """Calculate [Score Name]"""
    # Logic here
    return result

def render():
    """Render [Score Name] interface"""
    # UI here
```

### Bước 2: Cập nhật __init__.py
```python
from .[score_name] import render as render_[score_name]

calculators = {
    ...
    "[Score Name]": render_[score_name],
}
```

### Bước 3: Cập nhật config.py
```python
"[Score Name]": {
    "name": "[Score Name] ⭐", 
    "desc": "[Description]", 
    "status": "✅"
},
```

### Bước 4: Kiểm tra
- Chạy linter: `read_lints`
- Test tính toán
- Kiểm tra UI

---

## 🔍 Tài Liệu Tham Khảo Cần Tìm

### HFA-ICOS Guidelines
- Tìm tài liệu gốc từ HFA-ICOS (2024-2025)
- Các yếu tố nguy cơ cho từng loại điều trị ung thư
- Ngưỡng nguy cơ và khuyến nghị

### Các thang điểm khác
- Tìm tài liệu gốc cho từng thang điểm
- Xác nhận công thức tính toán
- Ngưỡng và diễn giải

---

## ✅ Checklist Mỗi Thang Điểm

- [ ] Tạo file Python mới
- [ ] Implement hàm tính toán
- [ ] Implement hàm render UI
- [ ] Thêm validation
- [ ] Thêm lịch sử tính toán
- [ ] Thêm chia sẻ kết quả
- [ ] Thêm xuất dữ liệu
- [ ] Thêm khuyến nghị lâm sàng
- [ ] Cập nhật __init__.py
- [ ] Cập nhật config.py
- [ ] Kiểm tra lỗi linter
- [ ] Test tính toán
- [ ] Test UI

---

## 📊 Tiến Độ Hiện Tại

- **Đã hoàn thành:** 18/49 (36.7%)
- **Còn lại:** 31/49 (63.3%)
- **Tổng trong hệ thống:** ~168+ thang điểm

---

**Chúc bạn thành công trong phiên tiếp theo!** 🚀

