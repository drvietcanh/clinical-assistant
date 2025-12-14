# 📝 Hướng Dẫn Sửa Lỗi Viết Hoa Tiếng Việt

## 📋 Tổng Quan

File `vietnamese_capitalization_fixes.py` chứa danh sách đầy đủ các lỗi viết hoa tiếng Việt cần sửa trong toàn bộ codebase.

## 🔧 Cách Sử Dụng

### 1. Quét và Kiểm Tra (Dry Run)

Chạy script để quét và báo cáo các lỗi mà không sửa file:

```bash
python fix_vietnamese_caps_comprehensive_scan.py
```

### 2. Áp Dụng Sửa Lỗi

Để thực sự sửa các file, chạy với flag `--apply`:

```bash
python fix_vietnamese_caps_comprehensive_scan.py --apply
```

## 📊 Danh Sách Các Pattern Đã Được Tổng Hợp

File `vietnamese_capitalization_fixes.py` chứa **150+ pattern** cần sửa, được phân loại thành các nhóm:

### 1. Thuật Ngữ Y Khoa
- Giới Tính → Giới tính
- Suy Tim → Suy tim
- Bệnh Phổi Mạn → Bệnh phổi mạn
- Tần Số Thở → Tần số thở
- ... và nhiều hơn

### 2. Lab & Clinical Terms
- Huyết Học → Huyết học
- Bilirubin Toàn Phần → Bilirubin toàn phần
- Lâm Sàng → Lâm sàng
- Nước Tiểu → Nước tiểu
- Cân Nặng → Cân nặng
- ... và nhiều hơn

### 3. Prognosis & Scoring
- Tiên Lượng → Tiên lượng
- Tiêu chí → Tiêu chí (đã đúng)
- So sánh Tổng Hợp → So sánh tổng hợp
- ... và nhiều hơn

### 4. Treatment & Strategy
- Xử Trí → Xử trí
- Chiến Lược → Chiến lược
- ... và nhiều hơn

### 5. Patient Demographics
- Người Cao Tuổi → Người cao tuổi
- Phụ Nữ Có Thai → Phụ nữ có thai
- Trẻ Em → Trẻ em
- ... và nhiều hơn

### 6. Hematology
- Mức Độ Giảm Tiểu Cầu → Mức độ giảm tiểu cầu
- Nguyên Nhân → Nguyên nhân
- ... và nhiều hơn

### 7. Trauma & Emergency
- Quy Tắc → Quy tắc
- Rối Loạn Ý Thức → Rối loạn ý thức
- ... và nhiều hơn

### 8. Assessment & Evaluation
- Kết quả Đánh giá → Kết quả đánh giá
- Độ Chính Xác → Độ chính xác
- Tình Huống → Tình huống
- ... và nhiều hơn

## 🎯 Quy Tắc Viết Hoa Tiếng Việt

### ✅ ĐÚNG:
- Chỉ viết hoa chữ cái đầu của câu
- Tên riêng (người, địa danh)
- Tên các tổ chức, cơ quan
- Tên các thuật ngữ khoa học khi là tên riêng (nhưng không phải mô tả)

### ❌ SAI:
- Viết hoa tất cả các từ trong cụm danh từ
- Viết hoa các từ mô tả thông thường
- Viết hoa các tính từ, động từ trong cụm danh từ

### Ví Dụ:
- ❌ "Người Cao Tuổi" → ✅ "Người cao tuổi"
- ❌ "Xử Trí Ngay Lập Tức" → ✅ "Xử trí ngay lập tức"
- ❌ "Kết quả Đánh giá" → ✅ "Kết quả đánh giá"

## 📁 Files Được Quét

Script sẽ quét các thư mục sau:
- `protocols/**/*.py`
- `pages/**/*.py`
- `scores/**/*.py`
- `labs/**/*.py`
- `critical_care/**/*.py`
- `antibiotics/**/*.py`
- `drugs/**/*.py`

## ⚠️ Lưu Ý

1. **Luôn chạy dry run trước** để xem các thay đổi sẽ được áp dụng
2. **Kiểm tra kỹ** các thay đổi trước khi commit
3. **Backup code** trước khi chạy với `--apply`
4. Một số pattern có thể cần điều chỉnh thủ công nếu context đặc biệt

## 🔄 Cập Nhật Danh Sách

Khi phát hiện lỗi viết hoa mới, thêm vào `vietnamese_capitalization_fixes.py`:

```python
VIETNAMESE_CAPITALIZATION_FIXES = {
    # ... existing patterns ...
    "Lỗi Mới": "Lỗi mới",  # Thêm vào đây
}
```

## 📈 Thống Kê

- **Tổng số pattern:** 150+
- **Files đã quét:** 455+
- **Files đã sửa:** 100+

## 🎉 Kết Quả

Sau khi chạy script, tất cả các lỗi viết hoa tiếng Việt sẽ được sửa tự động và nhất quán trong toàn bộ codebase.

