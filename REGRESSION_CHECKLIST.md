## Regression Checklist trước mỗi lần cập nhật lớn

Đánh dấu (✅/❌) khi đã chạy từng bước.

### 1. Kiểm tra dữ liệu & hệ thống thuốc

- [ ] Chạy `python run_drug_validation_suite.py`
- [ ] Xem lại các báo cáo trong `reports/drugs/` (nếu có)
- [ ] Không còn lỗi nghiêm trọng mới

### 2. Kiểm tra calculators & scores chính

- [ ] (Tùy chọn) Chạy `pytest tests/scores` cho các thang điểm quan trọng
- [ ] (Tùy chọn) Chạy `pytest tests/antibiotics` cho Vancomycin/Aminoglycoside

### 3. Kiểm tra runtime & UI

- [ ] Chạy `streamlit run app.py`
- [ ] Mở lần lượt: Trang chủ, Scores, Antibiotics, Drug Database, Disease Encyclopedia, Decision Support
- [ ] Không có exception mới trên console

### 4. Kiểm tra UI/UX & hiệu năng (tóm tắt)

- [ ] Cập nhật các phát hiện mới vào `UI_UX_ISSUES.md`
- [ ] Cập nhật các quan sát về hiệu năng vào `PERF_REPORT.md`

### 5. Cập nhật Master Issues

- [ ] Gom tất cả lỗi/vấn đề mới vào `MASTER_ISSUES_LIST.md` (đặt mức độ P0–P3)
- [ ] Đánh dấu trạng thái cho các lỗi đã được sửa

