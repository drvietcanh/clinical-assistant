# Guideline Checker Scripts - Index

## 🚀 Quick Start

**Xem tổng quan nhanh:**
```bash
python scripts/check_guideline_summary.py
# Hoặc Windows:
check_guidelines.bat summary
```

**Tạo báo cáo chi tiết:**
```bash
python scripts/check_guideline_updates.py --report-only
# Hoặc Windows:
check_guidelines.bat report
```

**Cập nhật ngày review:**
```bash
python scripts/update_guideline_dates.py --dry-run  # Xem trước
python scripts/update_guideline_dates.py            # Thực sự cập nhật
```

---

## 📁 Danh sách Scripts

### Core Scripts

| Script | Mô tả | Kích thước |
|--------|-------|------------|
| `check_guideline_updates.py` | Script chính - kiểm tra và tạo báo cáo | 433 dòng |
| `check_guideline_summary.py` | Báo cáo tổng hợp ngắn gọn | 120 dòng |
| `update_guideline_dates.py` | Cập nhật ngày review | 85 dòng |

### Advanced Scripts

| Script | Mô tả | Kích thước |
|--------|-------|------------|
| `export_guideline_report.py` | Xuất báo cáo ra JSON/CSV | 110 dòng |
| `compare_guideline_reports.py` | So sánh 2 báo cáo | 150 dòng |
| `create_guideline_dashboard.py` | Tạo HTML dashboard | 250 dòng |
| `validate_article_format.py` | Kiểm tra format file | 150 dòng |
| `check_guidelines.bat` | Batch script cho Windows | 50 dòng |

**Tổng:** 8 scripts, ~1,348 dòng code

---

## 📚 Tài liệu

### Hướng dẫn cơ bản
- **`README.md`** - Tổng quan chính
- **`QUICK_START_GUIDELINE_CHECKER.md`** - Hướng dẫn nhanh (5 phút)

### Hướng dẫn chi tiết
- **`README_GUIDELINE_CHECKER.md`** - Hướng dẫn đầy đủ
- **`HUONG_DAN_SU_DUNG_SCRIPT_GUIDELINE.md`** - Hướng dẫn tiếng Việt

### Nâng cao
- **`README_ADVANCED.md`** - Tính năng nâng cao
- **`USAGE_EXAMPLES.md`** - Ví dụ sử dụng và workflow

### Tổng kết
- **`TOM_TAT_SCRIPT_GUIDELINE.md`** - Tóm tắt nhanh
- **`TOM_TAT_HOAN_THANH_SCRIPT_GUIDELINE.md`** - Tổng kết hoàn thành

---

## 🎯 Use Cases

### 1. Kiểm tra nhanh (hàng tuần)
→ Dùng: `check_guideline_summary.py`

### 2. Kiểm tra đầy đủ (hàng tháng)
→ Dùng: `check_guideline_updates.py --report-only`

### 3. Cập nhật ngày review (mỗi 6 tháng)
→ Dùng: `update_guideline_dates.py`

### 4. Export và phân tích
→ Dùng: `export_guideline_report.py --format json`

### 5. Theo dõi thay đổi
→ Dùng: `compare_guideline_reports.py`

### 6. Tích hợp hệ thống
→ Dùng: `export_guideline_report.py` + JSON output

---

## 🔗 Liên kết nhanh

- [README chính](README.md)
- [Hướng dẫn nhanh](QUICK_START_GUIDELINE_CHECKER.md)
- [Tính năng nâng cao](README_ADVANCED.md)
- [Ví dụ sử dụng](USAGE_EXAMPLES.md)

---

## 📊 Thống kê

- **Tổng số scripts:** 8
- **Tổng số dòng code:** ~1,348
- **Tổng số tài liệu:** 8 files
- **File được quét:** 82 file markdown
- **Test thành công:** 100%

