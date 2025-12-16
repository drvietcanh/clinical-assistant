# 🔧 Quick Fix Vietnamese Capitalization

Script nhanh để quét và sửa lỗi viết hoa tiếng Việt triệt để trong toàn bộ codebase.

## 📋 Quy Tắc Viết Hoa Tiếng Việt

**ĐÚNG:** Chỉ viết hoa chữ cái đầu của từ đầu tiên trong cụm danh từ
- ✅ "Điều trị"
- ✅ "Theo dõi"
- ✅ "Phân loại"
- ✅ "Nguyên nhân"

**SAI:** Viết hoa tất cả các từ trong cụm danh từ
- ❌ "Điều Trị"
- ❌ "Theo Dõi"
- ❌ "Phân Loại"
- ❌ "Nguyên Nhân"

## 🚀 Cách Sử Dụng

### 1. Kiểm tra (Dry Run) - Không sửa file

```bash
python quick_fix_vietnamese_caps.py
```

Script sẽ quét và báo cáo tất cả các lỗi viết hoa mà không sửa file.

### 2. Áp dụng sửa lỗi

```bash
python quick_fix_vietnamese_caps.py --apply
```

Script sẽ tự động sửa tất cả các lỗi viết hoa trong codebase.

## 📊 Kết Quả

- **Tổng số file đã quét:** 686 files
- **Tổng số file có lỗi:** 132 files
- **Tổng số thay đổi:** 290 thay đổi

## 📁 Thư Mục Được Quét

- `protocols/`
- `pages/`
- `scores/`
- `labs/`
- `critical_care/`
- `antibiotics/`
- `drugs/`
- `components/`
- `ventilator/`
- `diagnosis/`

## ⚠️ Lưu Ý

1. **Luôn chạy dry run trước** để xem các thay đổi sẽ được áp dụng
2. **Kiểm tra kỹ** các thay đổi trước khi commit
3. **Backup code** trước khi chạy với `--apply`
4. Script tự động bỏ qua các file test, check, fix để tránh sửa nhầm

## 🔍 Các Pattern Được Sửa

Script sửa hơn 200+ pattern phổ biến như:
- Điều Trị → Điều trị
- Chẩn Đoán → Chẩn đoán
- Theo Dõi → Theo dõi
- Phân Loại → Phân loại
- Nguyên Nhân → Nguyên nhân
- ... và nhiều hơn

## ✅ Sau Khi Chạy

Sau khi chạy script với `--apply`, tất cả các lỗi viết hoa tiếng Việt sẽ được sửa tự động và nhất quán trong toàn bộ codebase.

