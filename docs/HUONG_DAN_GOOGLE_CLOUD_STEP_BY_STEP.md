# 📘 Hướng Dẫn Chi Tiết: Setup Google Analytics API

## 🎯 Mục Tiêu
Cấu hình Google Analytics API để lấy số liệu thực tế hiển thị trên trang web.

---

## 📋 BƯỚC 1: TẠO GOOGLE CLOUD PROJECT

### 1.1. Truy cập Google Cloud Console
1. Mở trình duyệt, truy cập: **https://console.cloud.google.com/**
2. Đăng nhập bằng tài khoản Google của bạn (cùng tài khoản với Google Analytics)

### 1.2. Tạo Project Mới
1. Ở góc trên cùng bên trái, click vào **dropdown "Select a project"** (hiển thị tên project hiện tại hoặc "Select a project")
2. Click **"NEW PROJECT"** (hoặc "Create Project")
3. Điền thông tin:
   - **Project name**: `Clinical Assistant Analytics` (hoặc tên bạn muốn)
   - **Location**: Chọn "No organization" hoặc organization của bạn
4. Click **"CREATE"**
5. Đợi vài giây để project được tạo
6. Click **"SELECT"** để chọn project vừa tạo

---

## 📋 BƯỚC 2: ENABLE GOOGLE ANALYTICS DATA API

### 2.1. Vào APIs & Services
1. Trong menu bên trái, tìm **"APIs & Services"** (hoặc **"APIs & Services"** → **"Library"**)
2. Click vào **"Library"**

### 2.2. Tìm và Enable API
1. Trong ô tìm kiếm, gõ: **"Google Analytics Data API"**
2. Click vào kết quả **"Google Analytics Data API"**
3. Click nút **"ENABLE"** (màu xanh)
4. Đợi vài giây để API được enable
5. Bạn sẽ thấy thông báo **"API enabled"** hoặc icon checkmark ✅

---

## 📋 BƯỚC 3: TẠO SERVICE ACCOUNT

### 3.1. Vào Credentials
1. Trong menu bên trái, click **"APIs & Services"** → **"Credentials"**
2. Hoặc click vào **"Credentials"** trực tiếp từ menu

### 3.2. Tạo Service Account
1. Ở phía trên trang, click **"+ CREATE CREDENTIALS"**
2. Chọn **"Service account"** từ dropdown menu

### 3.3. Điền Thông Tin Service Account
1. **Service account name**: `analytics-reader` (hoặc tên bạn muốn)
   - Tên này sẽ tự động tạo Service account ID
2. **Service account ID**: Sẽ tự động tạo (ví dụ: `analytics-reader@your-project-id.iam.gserviceaccount.com`)
3. **Description** (tùy chọn): `Service account để đọc Google Analytics data`
4. Click **"CREATE AND CONTINUE"**

### 3.4. Bỏ Qua Grant Access (Không Cần)
1. Ở bước **"Grant this service account access to project"**, bạn có thể **BỎ QUA** (không cần grant)
2. Click **"CONTINUE"** hoặc **"DONE"**

### 3.5. Hoàn Thành
- Service Account đã được tạo thành công
- Bạn sẽ thấy Service Account trong danh sách

---

## 📋 BƯỚC 4: DOWNLOAD JSON CREDENTIALS

### 4.1. Mở Service Account
1. Trong danh sách Service Accounts, click vào Service Account vừa tạo (tên: `analytics-reader`)

### 4.2. Vào Tab Keys
1. Ở trên cùng, click tab **"KEYS"**
2. Click **"ADD KEY"** → **"Create new key"**

### 4.3. Tạo Key JSON
1. Chọn **"JSON"** làm key type
2. Click **"CREATE"**
3. File JSON sẽ **tự động download** về máy của bạn
4. **LƯU FILE NÀY AN TOÀN!** 
   - Tên file thường: `your-project-id-xxxxx.json`
   - Lưu vào thư mục an toàn (ví dụ: `D:\1app\medical\credentials\`)

### 4.4. Lưu Ý Quan Trọng
- ⚠️ **KHÔNG chia sẻ file này với ai**
- ⚠️ **KHÔNG commit lên GitHub** (đã có trong .gitignore)
- ⚠️ File này chứa private key, cần bảo mật

---

## 📋 BƯỚC 5: LẤY EMAIL SERVICE ACCOUNT

### 5.1. Xem Email trong File JSON
1. Mở file JSON vừa download bằng Notepad hoặc text editor
2. Tìm dòng: `"client_email":`
3. Copy giá trị email (ví dụ: `analytics-reader@your-project-id.iam.gserviceaccount.com`)
4. **Lưu email này lại** - bạn sẽ cần nó ở bước tiếp theo

### 5.2. Hoặc Xem trong Google Cloud Console
1. Trong trang Service Account details
2. Email hiển thị ở phần **"Service account details"** → **"Email"**
3. Copy email này

---

## 📋 BƯỚC 6: THÊM SERVICE ACCOUNT VÀO GOOGLE ANALYTICS

### 6.1. Truy Cập Google Analytics
1. Mở tab mới, truy cập: **https://analytics.google.com/**
2. Đăng nhập bằng tài khoản Google (cùng tài khoản với Google Cloud)

### 6.2. Vào Admin
1. Ở góc dưới bên trái, click icon **⚙️ Admin** (hoặc chữ "Admin")

### 6.3. Vào Property Access Management
1. Trong cột **"Property"** (cột giữa), tìm **"Property access management"**
2. Click vào **"Property access management"**
   - Hoặc: **"Property Settings"** → **"Property Access Management"**

### 6.4. Thêm User
1. Click nút **"+"** (hoặc **"Add users"**)
2. Trong ô **"Email addresses"**, paste email Service Account đã copy ở Bước 5
   - Ví dụ: `analytics-reader@your-project-id.iam.gserviceaccount.com`

### 6.5. Chọn Quyền
1. Ở phần **"Select roles"**, chọn **"Viewer"**
   - ✅ Chỉ cần quyền **"Viewer"** (chỉ đọc)
   - ❌ Không cần "Editor" hoặc "Administrator"

### 6.6. Hoàn Thành
1. Click **"Add"** (hoặc **"Add users"**)
2. Bạn sẽ thấy Service Account email xuất hiện trong danh sách với quyền "Viewer"
3. ✅ **Hoàn thành!**

---

## 📋 BƯỚC 7: LẤY PROPERTY ID

### 7.1. Vào Property Settings
1. Trong Google Analytics, vẫn ở phần **Admin**
2. Trong cột **"Property"**, click **"Property Settings"**

### 7.2. Tìm Property ID
1. Scroll xuống, tìm phần **"Property ID"**
2. Bạn sẽ thấy một **số** (ví dụ: `123456789` hoặc `130433471`)
3. **Copy số này!**

### 7.3. Format Property ID
- Property ID cần format: `properties/123456789`
- Nếu bạn copy được số `123456789`, thì format đúng là: `properties/123456789`
- **Lưu lại** để dùng ở bước tiếp theo

---

## 📋 BƯỚC 8: CẤU HÌNH VÀO ỨNG DỤNG

### 8.1. Mở File JSON Credentials
1. Mở file JSON đã download ở Bước 4
2. Copy **TOÀN BỘ** nội dung file (Ctrl+A, Ctrl+C)

### 8.2. Cấu Hình Streamlit Secrets

#### **Option A: Streamlit Cloud (Khuyến nghị)**
1. Vào Streamlit Cloud: https://share.streamlit.io/
2. Chọn app của bạn
3. Click **"Settings"** → **"Secrets"**
4. Paste vào ô editor:
```toml
[google_analytics]
service_account_json = '''
{PASTE_TOÀN_BỘ_NỘI_DUNG_JSON_FILE_VÀO_ĐÂY}
'''
property_id = "properties/123456789"
```
5. Thay `123456789` bằng Property ID thực tế của bạn
6. Click **"Save"**

#### **Option B: Local Development**
1. Tạo thư mục `.streamlit` (nếu chưa có):
   ```bash
   mkdir .streamlit
   ```
2. Copy file template:
   ```bash
   copy .streamlit\secrets.toml.example .streamlit\secrets.toml
   ```
3. Mở file `.streamlit/secrets.toml`
4. Paste nội dung JSON vào phần `service_account_json`
5. Thay `property_id` bằng Property ID thực tế
6. Lưu file

---

## ✅ BƯỚC 9: KIỂM TRA

### 9.1. Chạy Script Kiểm Tra
```bash
# Windows
setup-ga-api.bat

# Hoặc
python setup_ga_api.py auto
```

### 9.2. Kiểm Tra Kết Quả
Script sẽ hiển thị:
- ✅ Requirements: OK
- ✅ Credentials: OK
- ✅ Property ID: OK
- ✅ API Connection: OK

Nếu tất cả đều ✅ → **Thành công!**

### 9.3. Kiểm Tra Trên Trang Web
1. Restart ứng dụng Streamlit (nếu đang chạy local)
2. Mở trang web
3. Scroll xuống phần **"Thống Kê Truy Cập"**
4. Nếu thấy số liệu thực tế (Users, Sessions, Pageviews) → **Hoàn thành!** 🎉

---

## 🔧 TROUBLESHOOTING

### ❌ Lỗi: "Permission denied" hoặc "403 Forbidden"
**Nguyên nhân:** Service Account chưa được thêm vào Google Analytics Property

**Giải pháp:**
1. Kiểm tra lại Bước 6
2. Đảm bảo email Service Account đã được thêm với quyền "Viewer"
3. Đợi vài phút để permissions được cập nhật
4. Thử lại

### ❌ Lỗi: "API not enabled"
**Nguyên nhân:** Google Analytics Data API chưa được enable

**Giải pháp:**
1. Kiểm tra lại Bước 2
2. Vào Google Cloud Console → APIs & Services → Library
3. Tìm "Google Analytics Data API" → Kiểm tra đã enable chưa
4. Nếu chưa, click "ENABLE"

### ❌ Lỗi: "Property not found"
**Nguyên nhân:** Property ID sai hoặc format sai

**Giải pháp:**
1. Kiểm tra Property ID trong Google Analytics (Bước 7)
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

## 📚 TÀI LIỆU THAM KHẢO

- [Google Analytics Data API Documentation](https://developers.google.com/analytics/devguides/reporting/data/v1)
- [Service Account Authentication](https://cloud.google.com/iam/docs/service-accounts)
- [Streamlit Secrets Management](https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app/secrets-management)

---

## ⚠️ LƯU Ý QUAN TRỌNG

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

## 🎉 HOÀN THÀNH!

Sau khi hoàn thành tất cả các bước, bạn sẽ có:
- ✅ Service Account đã được tạo
- ✅ JSON credentials đã được download
- ✅ Google Analytics Data API đã được enable
- ✅ Service Account đã được thêm vào Google Analytics
- ✅ Property ID đã được lấy
- ✅ Đã cấu hình vào ứng dụng
- ✅ Số liệu thực tế đang hiển thị trên trang web

**Chúc bạn thành công!** 🚀

