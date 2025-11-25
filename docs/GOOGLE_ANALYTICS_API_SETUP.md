# 📊 Hướng Dẫn Setup Google Analytics API

## 🎯 Mục Đích
Cấu hình Google Analytics Data API để lấy số liệu thực tế (users, sessions, pageviews) và hiển thị trên trang web.

---

## 📖 HƯỚNG DẪN CHI TIẾT TỪNG BƯỚC

👉 **Xem hướng dẫn chi tiết với hình ảnh mô tả:** [HUONG_DAN_GOOGLE_CLOUD_STEP_BY_STEP.md](./HUONG_DAN_GOOGLE_CLOUD_STEP_BY_STEP.md)

---

## 📝 Bước 1: Tạo Google Cloud Project

1. Truy cập: https://console.cloud.google.com/
2. Đăng nhập bằng tài khoản Google của bạn
3. Tạo project mới hoặc chọn project hiện có:
   - Click **"Select a project"** → **"New Project"**
   - Đặt tên: "Clinical Assistant Analytics" (hoặc tên bạn muốn)
   - Click **"Create"**

---

## 🔧 Bước 2: Enable Google Analytics Data API

1. Trong Google Cloud Console, vào **"APIs & Services"** → **"Library"**
2. Tìm **"Google Analytics Data API"**
3. Click **"Enable"**

---

## 🔑 Bước 3: Tạo Service Account

1. Vào **"APIs & Services"** → **"Credentials"**
2. Click **"Create Credentials"** → **"Service Account"**
3. Điền thông tin:
   - **Service account name**: "analytics-reader" (hoặc tên bạn muốn)
   - **Service account ID**: Sẽ tự động tạo
   - **Description**: "Service account để đọc Google Analytics data"
4. Click **"Create and Continue"**
5. Bỏ qua phần "Grant this service account access to project" (không cần)
6. Click **"Done"**

---

## 📥 Bước 4: Download JSON Credentials

1. Trong danh sách Service Accounts, click vào service account vừa tạo
2. Vào tab **"Keys"**
3. Click **"Add Key"** → **"Create new key"**
4. Chọn **"JSON"**
5. Click **"Create"** → File JSON sẽ được download về máy
6. **Lưu file này an toàn!** (ví dụ: `ga-service-account.json`)

---

## 🔐 Bước 5: Thêm Service Account vào Google Analytics

1. Vào Google Analytics: https://analytics.google.com/
2. Vào **Admin** (biểu tượng bánh răng)
3. Chọn **Property** của bạn
4. Vào **"Property access management"** (hoặc **"Property Settings"** → **"Property Access Management"**)
5. Click **"+"** → **"Add users"**
6. Nhập **Email của Service Account** (tìm trong file JSON vừa download, field `client_email`)
   - Format: `analytics-reader@your-project-id.iam.gserviceaccount.com`
7. Chọn quyền: **"Viewer"** (chỉ đọc)
8. Click **"Add"**

---

## 🆔 Bước 6: Lấy Property ID

1. Trong Google Analytics, vào **Admin**
2. Chọn **Property** của bạn
3. Vào **"Property Settings"**
4. Tìm **"Property ID"** (dạng số, ví dụ: `123456789`)
5. **Copy Property ID này!**

---

## ⚙️ Bước 7: Cấu Hình vào Ứng Dụng

### **Cách 1: Sử dụng Streamlit Secrets (Khuyến nghị cho Streamlit Cloud)**

1. Mở file JSON credentials đã download
2. Copy toàn bộ nội dung JSON
3. Trong Streamlit Cloud:
   - Vào **Settings** → **Secrets**
   - Thêm:
   ```toml
   [google_analytics]
   service_account_json = '''
   {
     "type": "service_account",
     "project_id": "your-project-id",
     "private_key_id": "...",
     "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n",
     "client_email": "analytics-reader@your-project-id.iam.gserviceaccount.com",
     "client_id": "...",
     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
     "token_uri": "https://oauth2.googleapis.com/token",
     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
     "client_x509_cert_url": "..."
   }
   '''
   property_id = "properties/123456789"
   ```
   - **Lưu ý:** Thay `properties/123456789` bằng Property ID thực tế của bạn (thêm prefix `properties/`)

### **Cách 2: Sử dụng Environment Variable (Cho local development)**

#### Trên Windows (PowerShell):
```powershell
# Set path đến file JSON
$env:GOOGLE_APPLICATION_CREDENTIALS="D:\path\to\ga-service-account.json"

# Set Property ID
$env:GOOGLE_ANALYTICS_PROPERTY_ID="properties/123456789"
```

#### Trên Linux/Mac:
```bash
# Thêm vào ~/.bashrc hoặc ~/.zshrc
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/ga-service-account.json"
export GOOGLE_ANALYTICS_PROPERTY_ID="properties/123456789"
```

### **Cách 3: Sửa trực tiếp trong code (Không khuyến nghị)**

Nếu muốn hardcode (không an toàn), có thể sửa trong `components/google_analytics_api.py`:
```python
# Thêm vào get_ga_property_id()
return "properties/123456789"  # Thay bằng Property ID thực tế
```

---

## ✅ Bước 8: Kiểm Tra

1. Restart ứng dụng Streamlit
2. Mở trang web
3. Scroll xuống phần "Thống Kê Truy Cập"
4. Nếu thấy số liệu thực tế (users, sessions, pageviews) → **Thành công!** ✅
5. Nếu thấy hướng dẫn setup → Kiểm tra lại các bước trên

---

## 🔍 Troubleshooting

### ❌ Lỗi: "Permission denied" hoặc "403 Forbidden"

**Nguyên nhân:** Service Account chưa được thêm vào Google Analytics Property

**Giải pháp:**
1. Kiểm tra lại Bước 5
2. Đảm bảo email Service Account đã được thêm với quyền "Viewer"
3. Đợi vài phút để permissions được cập nhật

### ❌ Lỗi: "API not enabled"

**Nguyên nhân:** Google Analytics Data API chưa được enable

**Giải pháp:**
1. Kiểm tra lại Bước 2
2. Vào Google Cloud Console → APIs & Services → Library
3. Tìm "Google Analytics Data API" → Enable

### ❌ Lỗi: "Property not found"

**Nguyên nhân:** Property ID sai hoặc format sai

**Giải pháp:**
1. Kiểm tra Property ID trong Google Analytics
2. Đảm bảo format: `properties/123456789` (có prefix `properties/`)
3. Không dùng Measurement ID (G-XXXXXXXXXX), phải dùng Property ID (số)

### ❌ Không thấy số liệu

**Nguyên nhân có thể:**
1. Chưa có dữ liệu trong Google Analytics (trang web mới tạo)
2. Credentials chưa đúng
3. Property ID sai

**Giải pháp:**
1. Đợi vài giờ sau khi có lượt truy cập thực tế
2. Kiểm tra Google Analytics Dashboard xem có dữ liệu không
3. Kiểm tra lại credentials và Property ID

---

## 📚 Tài Liệu Tham Khảo

- [Google Analytics Data API Documentation](https://developers.google.com/analytics/devguides/reporting/data/v1)
- [Service Account Authentication](https://cloud.google.com/iam/docs/service-accounts)
- [Streamlit Secrets Management](https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app/secrets-management)

---

## ⚠️ Lưu Ý Quan Trọng

1. **Bảo mật:** 
   - KHÔNG commit file JSON credentials lên GitHub
   - File JSON đã được thêm vào `.gitignore`
   - Sử dụng Streamlit Secrets cho production

2. **Permissions:**
   - Chỉ cần quyền "Viewer" cho Service Account
   - Không cần quyền "Editor" hoặc "Admin"

3. **Rate Limits:**
   - Google Analytics Data API có rate limits
   - Component đã có cache 5 phút để tránh quá tải

4. **Costs:**
   - Google Analytics Data API miễn phí cho usage hợp lý
   - Không có chi phí phát sinh

---

## 🎉 Hoàn Thành!

Sau khi cấu hình xong, bạn sẽ thấy:
- ✅ Số người dùng trong 30 ngày qua
- ✅ Tổng số sessions
- ✅ Tổng số lượt xem trang
- ✅ Số người dùng đang online (realtime)

**Chúc bạn thành công!** 🚀

