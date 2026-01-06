# 📋 Quy Tắc Lưu Trữ File Tiến Trình

## 🎯 Mục Đích

Tài liệu này quy định cách tổ chức và lưu trữ các file tiến trình, kế hoạch và tổng hợp công việc trong dự án.

## 📂 Cấu Trúc Thư Mục

```
docs/progress/
├── plans/          # Kế hoạch công việc
│   ├── KE_HOACH_TIEP_THEO_2026-01-XX.md
│   ├── KE_HOACH_BO_SUNG_FIELDS_*.md
│   └── ...
├── tracking/       # Theo dõi tiến trình
│   ├── TIEN_TRINH_TONG_HOP_2026-01-XX.md
│   ├── TIEN_TRINH_UPDATE_*.md
│   └── ...
├── summaries/      # Tổng hợp công việc
│   ├── TONG_HOP_CONG_VIEC_2026-01-XX.md
│   ├── TONG_HOP_CONG_VIEC_DANG_LAM_DO.md
│   └── ...
└── README.md       # Hướng dẫn chung
```

## 📝 Quy Tắc Đặt Tên

### 1. Kế Hoạch (Plans) - `plans/`
- **Format**: `KE_HOACH_[TEN_MO_TA]_YYYY-MM-DD.md`
- **Ví dụ**: 
  - `KE_HOACH_TIEP_THEO_2026-01-XX.md`
  - `KE_HOACH_BO_SUNG_FIELDS_2026-01-15.md`
  - `KE_HOACH_PHASE_6_7_8.md`

### 2. Tiến Trình (Tracking) - `tracking/`
- **Format**: `TIEN_TRINH_[TEN_MO_TA]_YYYY-MM-DD.md`
- **Ví dụ**:
  - `TIEN_TRINH_TONG_HOP_2026-01-XX.md`
  - `TIEN_TRINH_UPDATE_2026-01-15.md`
  - `TIEN_TRINH_SESSION_2026-01-15.md`

### 3. Tổng Hợp (Summaries) - `summaries/`
- **Format**: `TONG_HOP_[TEN_MO_TA]_YYYY-MM-DD.md`
- **Ví dụ**:
  - `TONG_HOP_CONG_VIEC_2026-01-XX.md`
  - `TONG_HOP_CONG_VIEC_DANG_LAM_DO.md`
  - `TONG_HOP_TIEN_TRINH_2026-01-15.md`

## 🔄 Quy Trình Lưu Trữ

### Khi Tạo File Mới:
1. **Xác định loại file**: Kế hoạch, Tiến trình, hay Tổng hợp?
2. **Chọn thư mục phù hợp**: `plans/`, `tracking/`, hoặc `summaries/`
3. **Đặt tên theo quy tắc**: Sử dụng format chuẩn
4. **Cập nhật ngày tháng**: Trong tên file và nội dung file

### Khi Cập Nhật File:
1. **Giữ nguyên tên file** nếu là cập nhật cùng ngày
2. **Tạo file mới** nếu là cập nhật ngày khác (thêm ngày mới)
3. **Cập nhật metadata** trong file (ngày cập nhật, phiên bản)

## 📌 Lưu Ý Quan Trọng

### ✅ Nên Làm:
- Luôn lưu file vào đúng thư mục con
- Sử dụng format ngày tháng nhất quán (YYYY-MM-DD)
- Cập nhật README.md khi có thay đổi cấu trúc
- Giữ file cũ khi tạo file mới (không xóa)

### ❌ Không Nên:
- Lưu file trực tiếp vào `docs/progress/` (phải có thư mục con)
- Đặt tên file không theo quy tắc
- Xóa file cũ khi cập nhật
- Lưu file ở thư mục gốc dự án

## 🔍 Tìm Kiếm File

### Tìm theo loại:
- **Kế hoạch**: `docs/progress/plans/KE_HOACH_*.md`
- **Tiến trình**: `docs/progress/tracking/TIEN_TRINH_*.md`
- **Tổng hợp**: `docs/progress/summaries/TONG_HOP_*.md`

### Tìm theo ngày:
- `docs/progress/**/*2026-01-*.md` (tất cả file tháng 1/2026)

## 📚 Ví Dụ Thực Tế

### Tạo Kế Hoạch Mới:
```
File: docs/progress/plans/KE_HOACH_BO_SUNG_THUOC_2026-01-20.md
Nội dung: Kế hoạch bổ sung thuốc mới vào database
```

### Cập Nhật Tiến Trình:
```
File: docs/progress/tracking/TIEN_TRINH_SESSION_2026-01-20.md
Nội dung: Tiến trình phiên làm việc ngày 20/01/2026
```

### Tổng Hợp Công Việc:
```
File: docs/progress/summaries/TONG_HOP_CONG_VIEC_2026-01-20.md
Nội dung: Tổng hợp công việc đã làm và đang làm dở
```

## 🔗 Liên Kết

- [README.md](./README.md) - Hướng dẫn chung về thư mục progress
- [../README.md](../README.md) - Tài liệu chính của docs

---

**Cập nhật lần cuối**: 2026-01-06  
**Phiên bản**: 1.0
