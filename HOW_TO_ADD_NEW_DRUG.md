# HƯỚNG DẪN THÊM THUỐC MỚI

**📌 FILE CHÍNH CẦN ĐỌC**: `DRUG_REFERENCE_GUIDE.md`

---

## 🎯 BẮT ĐẦU NHANH

### File cần đọc:
→ **`DRUG_REFERENCE_GUIDE.md`** - File này chứa TẤT CẢ thông tin cần thiết

### Nội dung trong file:
1. ✅ Cấu trúc 14 field chuẩn
2. ✅ Template thuốc mẫu (copy và sửa)
3. ✅ Danh sách thuốc theo nhóm (để chọn nhóm phù hợp)
4. ✅ Danh sách thuốc theo file (để chọn file phù hợp)
5. ✅ Danh sách tất cả thuốc (để tránh trùng lặp)
6. ✅ Hướng dẫn thêm thuốc mới (5 bước chi tiết)

---

## 📋 QUY TRÌNH THÊM THUỐC MỚI

### Bước 1: Mở file tham chiếu
```bash
# Mở file
DRUG_REFERENCE_GUIDE.md
```

### Bước 2: Xem template
- Xem phần **"2. TEMPLATE THUỐC MẪU"**
- Copy template và sửa

### Bước 3: Chọn nhóm thuốc
- Xem phần **"3. DANH SÁCH THUỐC THEO NHÓM"**
- Chọn nhóm phù hợp hoặc tạo nhóm mới

### Bước 4: Chọn file chứa
- Xem phần **"4. DANH SÁCH THUỐC THEO FILE"**
- Chọn file phù hợp hoặc tạo file mới

### Bước 5: Kiểm tra trùng lặp
- Xem phần **"5. DANH SÁCH TẤT CẢ THUỐC"**
- Đảm bảo tên thuốc không trùng

### Bước 6: Thêm thuốc
- Copy template
- Điền đầy đủ 14 field
- Thêm vào file đã chọn

### Bước 7: Kiểm tra
```bash
# Kiểm tra thuốc mới
python comprehensive_drug_management_system.py check <TênThuốc>

# Kiểm tra trạng thái
python comprehensive_drug_management_system.py stats

# Cập nhật danh sách
python create_drug_lists.py
```

### Bước 8: Cập nhật file tham chiếu
```bash
# Cập nhật file tham chiếu
python create_drug_reference.py
```

---

## ⚠️ LƯU Ý QUAN TRỌNG

1. **Bắt buộc có đủ 14 field chuẩn** - Không được thiếu field nào
2. **Thứ tự field** - Nên theo thứ tự chuẩn
3. **Tên thuốc** - Phải chính xác, không trùng lặp
4. **Nhóm thuốc** - Phải nhất quán với các thuốc cùng loại
5. **File chứa** - Nên đặt trong file phù hợp với nhóm

---

## 📚 TÀI LIỆU HỖ TRỢ

### File chính:
- **`DRUG_REFERENCE_GUIDE.md`** ⭐ - File tham chiếu đầy đủ

### File hỗ trợ:
- `MASTER_GUIDE.md` - Hướng dẫn tổng quan
- `SYSTEM_DOCUMENTATION.md` - Tài liệu hệ thống chi tiết

---

## 🔍 TÌM KIẾM NHANH

### Tìm nhóm thuốc:
- Mở `DRUG_REFERENCE_GUIDE.md`
- Ctrl+F: "DANH SÁCH THUỐC THEO NHÓM"
- Tìm nhóm phù hợp

### Tìm file chứa:
- Mở `DRUG_REFERENCE_GUIDE.md`
- Ctrl+F: "DANH SÁCH THUỐC THEO FILE"
- Tìm file phù hợp

### Kiểm tra trùng lặp:
- Mở `DRUG_REFERENCE_GUIDE.md`
- Ctrl+F: "DANH SÁCH TẤT CẢ THUỐC"
- Tìm tên thuốc

---

## ✅ CHECKLIST

Khi thêm thuốc mới:

- [ ] Đã đọc `DRUG_REFERENCE_GUIDE.md`
- [ ] Đã xem template thuốc mẫu
- [ ] Đã chọn nhóm thuốc phù hợp
- [ ] Đã chọn file chứa phù hợp
- [ ] Đã kiểm tra không trùng tên
- [ ] Đã điền đủ 14 field chuẩn
- [ ] Đã kiểm tra bằng script
- [ ] Đã cập nhật danh sách
- [ ] Đã cập nhật file tham chiếu

---

**Tóm tắt**: Chỉ cần đọc **`DRUG_REFERENCE_GUIDE.md`** là đủ!

