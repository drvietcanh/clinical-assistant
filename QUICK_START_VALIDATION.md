# ⚡ Quick Start - Kiểm Tra Dữ Liệu Thuốc

## 🚀 Chạy Nhanh

### Windows
```bash
# Kiểm tra đầy đủ (khuyến nghị)
validate_drugs.bat

# Hoặc kiểm tra nhanh
quick_check.bat
```

### Linux/Mac
```bash
# Kiểm tra đầy đủ
python comprehensive_drug_validation.py
python export_validation_issues.py
python generate_html_report.py

# Hoặc kiểm tra nhanh
python quick_validation_check.py
```

---

## 📊 Kết Quả

Sau khi chạy, bạn sẽ có:

1. **`drug_validation_report.html`** ⭐ - Mở trong trình duyệt để xem báo cáo đẹp
2. **`drug_validation_report.json`** - Báo cáo chi tiết dạng JSON
3. **`drug_validation_report.txt`** - Báo cáo dạng text
4. **`validation_errors.csv`** - Import vào Excel để theo dõi
5. **`auto_fix_suggestions.txt`** - Gợi ý sửa lỗi tự động

---

## 🔧 Tự Động Sửa Lỗi

```bash
# Chạy validation trước
python comprehensive_drug_validation.py

# Sau đó tự động sửa
python auto_fix_common_errors.py
```

**Lưu ý:** Các thay đổi chỉ áp dụng trong bộ nhớ. Bạn cần cập nhật thủ công vào file module hoặc `enhanced_fields_overrides.py`.

---

## 📋 Các Script Chính

| Script | Mô Tả | Khi Nào Dùng |
|--------|-------|--------------|
| `comprehensive_drug_validation.py` | Kiểm tra đầy đủ | Sau khi thêm/sửa thuốc |
| `quick_validation_check.py` | Kiểm tra nhanh | Trước khi commit |
| `export_validation_issues.py` | Export vấn đề | Khi cần danh sách sửa |
| `auto_fix_common_errors.py` | Tự động sửa | Sau khi validation |
| `generate_html_report.py` | Tạo báo cáo HTML | Để xem báo cáo đẹp |

---

## 📈 Kết Quả Hiện Tại

- **Tổng số thuốc:** 666
- **Thuốc hoàn chỉnh:** 160 (24%)
- **Lỗi:** 0 (sau auto fix)
- **Cảnh báo:** 971

### Top 3 Field Cần Bổ Sung

1. `contraindications_detail` - thiếu 346 thuốc (52%)
2. `reversal_agents` - thiếu 175 thuốc (26%)
3. `black_box_warnings` - thiếu 138 thuốc (21%)

---

## 💡 Tips

- Chạy `quick_check.bat` hàng ngày
- Chạy `validate_drugs.bat` định kỳ (tuần/tháng)
- Xem `drug_validation_report.html` để có cái nhìn tổng quan
- Sử dụng `validation_errors.csv` để theo dõi tiến độ trong Excel

---

## 📖 Tài Liệu Đầy Đủ

- `README_DRUG_VALIDATION.md` - Hướng dẫn chi tiết
- `VALIDATION_TOOLS_SUMMARY.md` - Tổng hợp công cụ
- `FINAL_VALIDATION_SUMMARY.md` - Tổng kết cuối cùng

---

**Cần giúp đỡ?** Xem `README_DRUG_VALIDATION.md` hoặc các file báo cáo đã tạo.

