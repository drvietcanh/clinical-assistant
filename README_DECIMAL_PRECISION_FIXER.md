# 🔧 Công Cụ Tự Động Kiểm Tra và Sửa Số Thập Phân Dư

Script tự động để kiểm tra và sửa các giá trị lâm sàng hiển thị với quá nhiều chữ số thập phân không có ý nghĩa.

## 📋 Mục Đích

Trong lâm sàng, việc hiển thị quá nhiều chữ số thập phân không có ý nghĩa và có thể gây nhầm lẫn. Script này giúp:
- ✅ Tự động phát hiện các giá trị lâm sàng có độ chính xác quá cao (≥3 chữ số thập phân)
- ✅ Đề xuất độ chính xác phù hợp dựa trên loại giá trị
- ✅ Tự động sửa hoặc tạo báo cáo để review

## 🚀 Cách Sử Dụng

### Windows (PowerShell/CMD)

```bash
# Chỉ kiểm tra và tạo báo cáo
fix_decimal_precision.bat check

# Tự động sửa các lỗi
fix_decimal_precision.bat fix

# Xem sẽ sửa gì nhưng không sửa thật (dry-run)
fix_decimal_precision.bat dry-run
```

### Linux/Mac

```bash
# Cấp quyền thực thi (chỉ cần làm 1 lần)
chmod +x fix_decimal_precision.sh

# Chỉ kiểm tra và tạo báo cáo
./fix_decimal_precision.sh check

# Tự động sửa các lỗi
./fix_decimal_precision.sh fix

# Xem sẽ sửa gì nhưng không sửa thật (dry-run)
./fix_decimal_precision.sh dry-run
```

### Python Trực Tiếp

```bash
# Chỉ kiểm tra
python utils/fix_decimal_precision.py --check

# Tự động sửa
python utils/fix_decimal_precision.py --fix

# Dry-run
python utils/fix_decimal_precision.py --fix --dry-run

# Tùy chỉnh file báo cáo
python utils/fix_decimal_precision.py --check --report MY_REPORT.md

# Quét thư mục khác
python utils/fix_decimal_precision.py --check --root ./scores
```

## 📊 Các Tùy Chọn

| Tùy chọn | Mô tả |
|----------|-------|
| `--check` | Chỉ kiểm tra và tạo báo cáo, không sửa |
| `--fix` | Tự động sửa các lỗi tìm thấy |
| `--dry-run` | Xem sẽ sửa gì nhưng không sửa thật (chỉ dùng với `--fix`) |
| `--report FILE` | File để lưu báo cáo (mặc định: `DECIMAL_PRECISION_REPORT.md`) |
| `--root DIR` | Thư mục gốc để quét (mặc định: thư mục hiện tại) |

## 🎯 Nguyên Tắc Làm Tròn

Script tự động xác định độ chính xác phù hợp dựa trên loại giá trị:

| Loại Giá Trị | Độ Chính Xác | Ví Dụ |
|--------------|---------------|-------|
| **Vital signs** (huyết áp, nhịp tim) | 0 chữ số | `120 mmHg`, `80 bpm` |
| **Nhiệt độ** | 1 chữ số | `37.1°C` |
| **Cân nặng, chiều cao** | 1 chữ số | `70.5 kg`, `175.0 cm` |
| **Lab values** | 1-2 chữ số | `7.2 mg/dL`, `140.5 mmol/L` |
| **Liều thuốc** | 1-2 chữ số | `2.5 mg/kg`, `10.0 mg/h` |
| **Thể tích** | 1-2 chữ số | `500.0 mL`, `2.5 L` |
| **Scores** | 1-2 chữ số | `15.5 điểm`, `8.0` |
| **Phần trăm** | 1 chữ số | `95.5%` |
| **Thời gian** | 2 chữ số | `1.25 giờ`, `30.50 giây` |
| **Áp lực** | 1 chữ số | `15.5 cmH2O` |
| **BSA, tỷ lệ** | 2 chữ số | `1.73 m²` |

## 🔍 Các File Được Bỏ Qua

Script tự động bỏ qua các file không phải giá trị lâm sàng:
- ✅ File test (`test_*.py`, `*_test.py`)
- ✅ File logging/debug (`utils/performance_monitor.py`, `utils/logger*.py`)
- ✅ File cache (`__pycache__`, `*.pyc`)

## 📝 Ví Dụ Output

### Khi chạy `--check`:

```
🔍 Đang quét codebase để tìm số thập phân dư...

📊 Tìm thấy 5 lỗi số thập phân dư

📋 Tóm tắt:
  - scores/cardiology/qtc.py: 2 lỗi
  - critical_care/sedation.py: 1 lỗi
  - labs/lipid.py: 1 lỗi
  - scores/nephrology/egfr_ui_results.py: 1 lỗi

📄 Báo cáo chi tiết đã được tạo: DECIMAL_PRECISION_REPORT.md
```

### Khi chạy `--fix`:

```
🔍 Đang quét codebase để tìm số thập phân dư...

📊 Tìm thấy 5 lỗi số thập phân dư

🔧 Đang sửa các lỗi...
  ✅ Đã sửa: scores/cardiology/qtc.py:277
  ✅ Đã sửa: scores/cardiology/qtc.py:434
  ✅ Đã sửa: critical_care/sedation.py:408
  ✅ Đã sửa: labs/lipid.py:351
  ✅ Đã sửa: scores/nephrology/egfr_ui_results.py:96

✅ Đã sửa 5/5 lỗi
```

## 🔄 Tích Hợp vào Workflow

### Trước khi commit:

```bash
# Kiểm tra và sửa tự động
./fix_decimal_precision.sh fix

# Review các thay đổi
git diff

# Commit nếu OK
git add .
git commit -m "Fix decimal precision issues"
```

### Trong CI/CD:

```yaml
# .github/workflows/check_decimal_precision.yml
- name: Check decimal precision
  run: |
    python utils/fix_decimal_precision.py --check
    if [ -s DECIMAL_PRECISION_REPORT.md ]; then
      echo "Found decimal precision issues!"
      cat DECIMAL_PRECISION_REPORT.md
      exit 1
    fi
```

## 🛠️ Tùy Chỉnh

Nếu cần thay đổi logic, chỉnh sửa file `utils/fix_decimal_precision.py`:

1. **Thêm pattern mới:** Thêm vào `CLINICAL_PATTERNS` dictionary
2. **Thay đổi độ chính xác:** Sửa `PrecisionLevel` enum
3. **Bỏ qua file khác:** Thêm vào `IGNORE_PATTERNS` list

## 📚 Ví Dụ Cụ Thể

### Trước khi sửa:
```python
st.metric("RR Interval", f"{rr_interval:.3f} s")  # ❌ 3 chữ số không cần thiết
st.info(f"**AIP:** {aip:.3f}")  # ❌ 3 chữ số không cần thiết
```

### Sau khi sửa:
```python
st.metric("RR Interval", f"{rr_interval:.2f} s")  # ✅ 2 chữ số phù hợp
st.info(f"**AIP:** {aip:.2f}")  # ✅ 2 chữ số phù hợp
```

## ⚠️ Lưu Ý

1. **Luôn review trước khi commit:** Chạy `--dry-run` trước để xem sẽ sửa gì
2. **Backup code:** Script sẽ sửa trực tiếp file, nên commit hoặc backup trước
3. **Test sau khi sửa:** Đảm bảo ứng dụng vẫn hoạt động đúng sau khi sửa

## 🐛 Báo Lỗi

Nếu script không hoạt động đúng hoặc phát hiện sai, vui lòng:
1. Chạy với `--dry-run` để xem sẽ sửa gì
2. Kiểm tra file báo cáo chi tiết
3. Tạo issue với thông tin chi tiết

## 📄 License

Script này là một phần của dự án Clinical Assistant và tuân theo cùng license.

