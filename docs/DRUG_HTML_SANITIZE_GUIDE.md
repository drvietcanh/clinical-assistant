## HTML trong dữ liệu thuốc – Script và Validator

### 1. Mục tiêu

- Tránh để **mã HTML thô** (ví dụ: `<div>`, `<span>`, `<strong>`) nằm trong dữ liệu thuốc trong thư mục `drugs/drug_modules`.
- Giảm lỗi hiển thị kiểu in nguyên `<div style='...'>` trên UI (Drug Detail, Quick Facts, Dosing, Monitoring...).
- Tạo quy trình **tự động kiểm tra + tự động làm sạch** dữ liệu.

---

### 2. Script 1 – `sanitize_drug_html.py`

**Chức năng**:

- Duyệt toàn bộ file `.py` trong `drugs/drug_modules`.
- Dùng AST để tìm tất cả **string hằng**.
- Nếu string có chứa HTML tag (match `</?[a-zA-Z][^>]*>`), script sẽ:
  - Strip toàn bộ tag bằng regex `r"<[^>]+>"`.
  - Giữ lại phần text, `strip()` khoảng trắng hai đầu.
  - Ghi lại source code mới.
- Tự động tạo **file backup** với đuôi `.backup` trước khi ghi.

**Cách chạy** (từ thư mục project gốc):

```bash
cd "D:\1 medical"
python sanitize_drug_html.py
```

**Output**:

- In từng file dạng:
  - `[CLEAN] drugs/drug_modules/...` – không phát hiện HTML cần strip.
  - `[FIXED] drugs/drug_modules/...` – đã strip ít nhất một string chứa HTML.
- Phần `SUMMARY` cuối:
  - `Total files scanned`
  - `Files modified`
  - Thông báo vị trí lưu backup `.backup`.

**Khuyến cáo**:

- Nên **commit code hiện tại** trước khi chạy để dễ rollback.
- Chỉ nên chạy khi chắc chắn các file trong `drugs/drug_modules` chủ yếu chứa **data dict**, không chứa UI HTML đặc biệt cần giữ nguyên.

---

### 3. Script 2 – `check_drug_html.py`

**Chức năng**:

- Validator chỉ đọc, **không sửa**.
- Quét `drugs/drug_modules` bằng AST.
- Nếu còn bất kỳ string hằng nào chứa HTML tag:
  - In ra **file, số dòng, snippet nội dung**.
  - Trả về **exit code 1** (thất bại).
- Nếu không có: in thông báo pass và trả về **exit code 0**.

**Cách chạy**:

```bash
cd "D:\1 medical"
python check_drug_html.py
```

**Output**:

- Ví dụ khi phát hiện HTML:

```text
=== CHECK DRUG MODULES FOR EMBEDDED HTML ===

⚠️  drugs/drug_modules/.../some_drug.py:
   - Line 123: <div style='background: white; padding: 15px;'>Tăng huyết áp...</div>

=== SUMMARY ===
Total files scanned    : 120
Files with HTML issues : 1

❌ HTML tags detected in drug data. Vui lòng chạy sanitize_drug_html.py hoặc sửa tay.
```

- Khi không còn HTML:

```text
=== SUMMARY ===
Total files scanned    : 120
Files with HTML issues : 0

✅ No HTML tags detected in drug data.
```

---

### 4. Quy trình đề xuất khi chỉnh sửa/ thêm thuốc

1. **Sửa hoặc thêm thuốc** trong `drugs/drug_modules/...`.
2. Chạy validator:

```bash
python check_drug_html.py
```

3. Nếu script báo **có HTML**:
   - Chạy:

   ```bash
   python sanitize_drug_html.py
   ```

   - Hoặc mở file cụ thể, sửa tay string đang chứa HTML.
4. Chạy lại:

```bash
python check_drug_html.py
```

để xác nhận dữ liệu **sạch HTML** trước khi deploy.

---

### 5. Tích hợp vào quy trình kiểm tra hệ thống

- Có thể thêm bước:

```bash
python check_drug_html.py
```

vào script `final_system_check.py` hoặc pipeline CI:
  - Nếu exit code ≠ 0 → fail build, yêu cầu làm sạch dữ liệu trước khi merge/deploy.


