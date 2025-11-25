# 📊 Hướng Dẫn Cấu Hình Google Analytics

## 🎯 Mục Đích
Thêm Google Analytics để theo dõi lượt truy cập, hành vi người dùng và thống kê trang web.

---

## 📝 Bước 1: Tạo Google Analytics Account

1. Truy cập: https://analytics.google.com/
2. Đăng nhập bằng tài khoản Google của bạn
3. Nếu chưa có tài khoản, nhấn **"Start measuring"** hoặc **"Create Account"**

---

## 🔧 Bước 2: Tạo Property Mới

1. Vào **Admin** (biểu tượng bánh răng ở góc dưới bên trái)
2. Chọn **"Create Property"**
3. Điền thông tin:
   - **Property name**: "Clinical Assistant" (hoặc tên bạn muốn)
   - **Reporting time zone**: Chọn múi giờ của bạn
   - **Currency**: VND hoặc USD
4. Nhấn **"Next"**

---

## 🌐 Bước 3: Tạo Data Stream (Web)

1. Chọn **"Web"** làm platform
2. Điền thông tin:
   - **Website URL**: URL của trang web bạn (ví dụ: `https://your-app.streamlit.app`)
   - **Stream name**: "Clinical Assistant Web" (hoặc tên bạn muốn)
3. Nhấn **"Create stream"**

---

## 🔑 Bước 4: Lấy Measurement ID

Sau khi tạo stream, bạn sẽ thấy:
- **Measurement ID**: Dạng `G-XXXXXXXXXX` (ví dụ: `G-ABC123XYZ`)

**Copy ID này!**

---

## ⚙️ Bước 5: Cấu Hình vào Ứng Dụng

### **Cách 1: Sử dụng Environment Variable (Khuyến nghị)**

#### Trên Windows (PowerShell):
```powershell
# Tạm thời (chỉ cho session hiện tại)
$env:GOOGLE_ANALYTICS_ID="G-XXXXXXXXXX"

# Vĩnh viễn (cho user)
[System.Environment]::SetEnvironmentVariable("GOOGLE_ANALYTICS_ID", "G-XXXXXXXXXX", "User")
```

#### Trên Linux/Mac:
```bash
# Thêm vào ~/.bashrc hoặc ~/.zshrc
export GOOGLE_ANALYTICS_ID="G-XXXXXXXXXX"
```

#### Trong Streamlit Cloud:
1. Vào **Settings** → **Secrets**
2. Thêm:
```toml
GOOGLE_ANALYTICS_ID = "G-XXXXXXXXXX"
```

### **Cách 2: Sửa trực tiếp trong config file**

Mở file `config/app_config.py` và tìm dòng:
```python
"google_analytics_id": os.getenv("GOOGLE_ANALYTICS_ID", "G-XXXXXXXXXX"),
```

Thay `"G-XXXXXXXXXX"` bằng Measurement ID thực tế của bạn:
```python
"google_analytics_id": os.getenv("GOOGLE_ANALYTICS_ID", "G-ABC123XYZ"),
```

---

## ✅ Bước 6: Kiểm Tra

1. Chạy lại ứng dụng Streamlit
2. Mở trang web trong trình duyệt
3. Mở **Developer Tools** (F12) → Tab **Network**
4. Tìm request đến `googletagmanager.com` → Nếu thấy là đã hoạt động!
5. Hoặc vào Google Analytics → **Reports** → **Realtime** → Sẽ thấy lượt truy cập

---

## 🔍 Xác Minh Hoạt Động

### Cách 1: Google Analytics Realtime
1. Vào Google Analytics
2. Chọn **Reports** → **Realtime**
3. Mở trang web của bạn trong tab khác
4. Quay lại Realtime → Sẽ thấy 1 user đang online

### Cách 2: Browser Developer Tools
1. Mở trang web
2. Nhấn **F12** (Developer Tools)
3. Tab **Network** → Tìm `gtag/js` → Status 200 = OK ✅

---

## 🛠️ Troubleshooting

### ❌ Không thấy dữ liệu trong Analytics?

1. **Kiểm tra Measurement ID đúng chưa?**
   - Format: `G-` + 10 ký tự
   - Không có khoảng trắng

2. **Kiểm tra code đã được inject chưa?**
   - View page source (Ctrl+U)
   - Tìm `googletagmanager.com`
   - Nếu không thấy → Kiểm tra lại config

3. **Ad blocker?**
   - Tắt ad blocker để test
   - Một số trình duyệt chặn Google Analytics

4. **CORS/Privacy?**
   - Một số trình duyệt chặn tracking
   - Thử trình duyệt khác

---

## 📚 Tài Liệu Tham Khảo

- [Google Analytics 4 Documentation](https://developers.google.com/analytics/devguides/collection/ga4)
- [Streamlit Components - HTML Injection](https://docs.streamlit.io/library/advanced-features/html)

---

## ⚠️ Lưu Ý Quan Trọng

1. **Privacy Policy**: Nếu trang web của bạn có người dùng thật, cần thông báo về việc sử dụng Google Analytics (GDPR, CCPA)

2. **Performance**: Google Analytics không ảnh hưởng đáng kể đến performance, nhưng nên test trên production

3. **Testing**: Luôn test trên môi trường development trước khi deploy

---

## 🎉 Hoàn Thành!

Sau khi cấu hình xong, Google Analytics sẽ tự động:
- ✅ Theo dõi page views
- ✅ Theo dõi user sessions
- ✅ Thu thập thông tin device, browser, location
- ✅ Tạo reports tự động

**Chúc bạn thành công!** 🚀

