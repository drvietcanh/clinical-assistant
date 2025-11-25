# 🎯 Hướng Dẫn Đơn Giản - Bằng Tiếng Việt

## ✅ BẠN ĐÃ LÀM ĐƯỢC:
- ✅ Download file JSON về máy rồi

---

## 📁 BƯỚC 1: TÌM FILE JSON

File JSON bạn vừa download thường ở:
- **Thư mục Downloads** (Tải xuống)
- Hoặc thư mục bạn chọn khi download

**Tên file thường là:** `ordinal-tower-479306-f0-xxxxx.json`

**Làm gì:**
1. Tìm file JSON trong máy
2. Copy file này vào thư mục: `D:\1app\medical\`
3. Hoặc để nguyên ở thư mục Downloads cũng được

---

## 📧 BƯỚC 2: LẤY EMAIL TỪ FILE JSON

1. **Mở file JSON** bằng Notepad (chuột phải → Mở bằng → Notepad)
2. Tìm dòng có chữ: `"client_email"`
3. Copy email đó (ví dụ: `analytics-reader@ordinal-tower-479306-f0.iam.gserviceaccount.com`)
4. **Lưu email này lại** - bạn sẽ cần nó ở bước sau

**Ví dụ trong file JSON:**
```json
{
  "type": "service_account",
  "project_id": "ordinal-tower-479306-f0",
  "client_email": "analytics-reader@ordinal-tower-479306-f0.iam.gserviceaccount.com",
  ...
}
```
→ Email cần copy: `analytics-reader@ordinal-tower-479306-f0.iam.gserviceaccount.com`

---

## 🌐 BƯỚC 3: VÀO GOOGLE ANALYTICS

1. Mở trình duyệt
2. Vào: **https://analytics.google.com/**
3. Đăng nhập bằng tài khoản Google (cùng tài khoản với Google Cloud)

---

## ⚙️ BƯỚC 4: VÀO PHẦN ADMIN

Trong Google Analytics:

1. Nhìn xuống **góc dưới bên trái**
2. Tìm icon **⚙️** (bánh răng) - có chữ **"Quản trị"** hoặc **"Admin"**
3. **Click vào đó**

---

## 👥 BƯỚC 5: THÊM EMAIL VÀO GOOGLE ANALYTICS

Sau khi click Admin, bạn sẽ thấy 3 cột:

1. **Cột giữa** (có chữ "Tài sản" hoặc "Property"):
   - Tìm chữ **"Quản lý quyền truy cập và..."** hoặc **"Property access management"**
   - **Click vào đó**

2. Bạn sẽ thấy danh sách người dùng
   - Tìm nút **"+"** hoặc **"Thêm người dùng"** hoặc **"Add users"**
   - **Click vào đó**

3. Một cửa sổ mới hiện ra:
   - Ô **"Email addresses"** hoặc **"Địa chỉ email"**: Paste email bạn đã copy ở Bước 2
   - Phần **"Quyền"** hoặc **"Roles"**: Chọn **"Viewer"** (Người xem)
   - Click **"Thêm"** hoặc **"Add"**

4. Xong! Email sẽ xuất hiện trong danh sách

---

## 🆔 BƯỚC 6: LẤY PROPERTY ID

Vẫn trong phần Admin:

1. Ở **cột giữa** (Property), tìm **"Cài đặt tài sản"** hoặc **"Property Settings"**
2. **Click vào đó**
3. Scroll xuống, tìm **"Property ID"** hoặc **"Mã tài sản"**
4. Bạn sẽ thấy một **SỐ** (ví dụ: `130433471` hoặc `123456789`)
5. **Copy số đó!**

**Lưu ý:** 
- Đây là SỐ, không phải chữ G-XXX
- Format đúng: `properties/130433471` (có chữ "properties/" ở trước)

---

## ⚙️ BƯỚC 7: CẤU HÌNH VÀO APP

Bây giờ bạn cần tạo file cấu hình:

### Cách 1: Tự Động (Dễ nhất)

1. Đảm bảo file JSON đã ở trong thư mục `D:\1app\medical\`
2. Chạy lệnh:
   ```bash
   python run_ga_setup_auto.py
   ```
3. Script sẽ tự động tìm file JSON và tạo file cấu hình

### Cách 2: Thủ Công

1. Tạo thư mục `.streamlit` (nếu chưa có):
   - Trong thư mục `D:\1app\medical\`
   - Tạo thư mục mới tên: `.streamlit`

2. Tạo file `secrets.toml` trong thư mục `.streamlit`

3. Mở file `secrets.toml` bằng Notepad, paste nội dung sau:

```toml
[google_analytics]
service_account_json = '''
{PASTE_TOÀN_BỘ_NỘI_DUNG_FILE_JSON_VÀO_ĐÂY}
'''
property_id = "properties/130433471"
```

4. Thay thế:
   - `{PASTE_TOÀN_BỘ_NỘI_DUNG_FILE_JSON_VÀO_ĐÂY}` → Copy toàn bộ nội dung file JSON
   - `130433471` → Thay bằng Property ID thực tế của bạn

5. Lưu file

---

## ✅ BƯỚC 8: KIỂM TRA

Sau khi tạo file cấu hình xong:

1. Chạy lệnh:
   ```bash
   python setup_ga_api.py auto
   ```

2. Nếu thấy tất cả đều ✅ → **Thành công!**

3. Restart ứng dụng Streamlit (nếu đang chạy)

4. Mở trang web, scroll xuống phần "Thống Kê Truy Cập"

5. Sẽ thấy số liệu thực tế! 🎉

---

## 💡 TÓM TẮT NHANH

1. ✅ File JSON đã download → Tìm và copy vào `D:\1app\medical\`
2. 📧 Mở file JSON → Copy email (field `client_email`)
3. 🌐 Vào Google Analytics → Admin → Property access management
4. ➕ Thêm email với quyền Viewer
5. 🆔 Lấy Property ID (số) từ Property Settings
6. ⚙️ Tạo file `.streamlit/secrets.toml` với JSON và Property ID
7. ✅ Kiểm tra bằng `python setup_ga_api.py auto`

---

## ❓ CẦN GIÚP ĐỠ?

Nếu gặp khó khăn ở bước nào, cho tôi biết:
- Bạn đang ở bước nào?
- Gặp lỗi gì?
- Không tìm thấy phần nào?

Tôi sẽ hướng dẫn chi tiết hơn! 😊

