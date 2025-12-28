# Tóm tắt Script Kiểm tra Guideline

## 📋 Tổng quan

Đã tạo bộ script Python để tự động kiểm tra và cập nhật guideline trong các bài viết y khoa.

## 🚀 Scripts có sẵn

### 1. `check_guideline_updates.py` - Script chính
**Chức năng:**
- Quét tất cả file markdown trong `content/articles/`
- Trích xuất thông tin guideline từ metadata và nội dung
- Đánh giá guideline cần kiểm tra dựa trên chu kỳ cập nhật
- Tạo báo cáo chi tiết
- Tự động cập nhật ngày review (tùy chọn)

**Sử dụng:**
```bash
python scripts/check_guideline_updates.py --report-only
```

### 2. `check_guideline_summary.py` - Báo cáo tổng hợp
**Chức năng:**
- Hiển thị báo cáo tổng quan ngắn gọn trên terminal
- Top guideline cần kiểm tra
- Guideline mới nhất và cũ nhất
- File cần ưu tiên kiểm tra

**Sử dụng:**
```bash
python scripts/check_guideline_summary.py
```

### 3. `update_guideline_dates.py` - Cập nhật ngày
**Chức năng:**
- Chỉ cập nhật ngày review
- Đơn giản, nhanh

**Sử dụng:**
```bash
# Dry-run
python scripts/update_guideline_dates.py --dry-run

# Thực sự cập nhật
python scripts/update_guideline_dates.py
```

## 📊 Kết quả test

Đã test thành công:
- ✅ Quét được 82 file markdown
- ✅ Tìm thấy 44 file cần kiểm tra guideline
- ✅ Tạo báo cáo chi tiết
- ✅ Script summary hoạt động tốt

## 📅 Lịch trình khuyến nghị

### Hàng tuần
```bash
python scripts/check_guideline_summary.py
```
→ Xem tổng quan nhanh

### Hàng tháng
```bash
python scripts/check_guideline_updates.py --report-only
```
→ Tạo báo cáo chi tiết và kiểm tra

### Mỗi 6 tháng
```bash
python scripts/update_guideline_dates.py
```
→ Cập nhật ngày review cho tất cả file

## 📁 Tài liệu

- `scripts/README.md` - Tổng quan
- `scripts/README_GUIDELINE_CHECKER.md` - Hướng dẫn chi tiết
- `scripts/QUICK_START_GUIDELINE_CHECKER.md` - Hướng dẫn nhanh
- `scripts/USAGE_EXAMPLES.md` - Ví dụ sử dụng
- `HUONG_DAN_SU_DUNG_SCRIPT_GUIDELINE.md` - Hướng dẫn đầy đủ (tiếng Việt)

## ⚠️ Lưu ý quan trọng

1. **Script chỉ kiểm tra, không tự động cập nhật guideline mới:** Cần kiểm tra thủ công trên website chính thức
2. **Chu kỳ cập nhật là ước tính:** Các guideline có thể không tuân theo chu kỳ chính xác
3. **Commit trước khi cập nhật:** Luôn commit code trước khi chạy `--force`
4. **Xác nhận thủ công:** Sau khi có báo cáo, nên kiểm tra lại guideline quan trọng

## 🎯 Kết luận

Hệ thống script đã sẵn sàng sử dụng. Có thể chạy định kỳ để đảm bảo các bài viết luôn được kiểm tra guideline mới nhất một cách tự động và hiệu quả.

