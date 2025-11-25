# ✅ Google Analytics API Setup Checklist

## 📋 Checklist Theo Dõi Tiến Độ

Đánh dấu ✅ khi hoàn thành mỗi bước.

---

## 🔵 PHẦN 1: GOOGLE CLOUD CONSOLE

### Bước 1: Tạo Project
- [ ] Truy cập https://console.cloud.google.com/
- [ ] Đăng nhập bằng tài khoản Google
- [ ] Click "Select a project" → "NEW PROJECT"
- [ ] Đặt tên: "Clinical Assistant Analytics"
- [ ] Click "CREATE"
- [ ] Đợi vài giây → Click "SELECT"

**Ghi chú:** 
- Project ID: _________________________

### Bước 2: Enable API
- [ ] Menu trái → "APIs & Services" → "Library"
- [ ] Tìm "Google Analytics Data API"
- [ ] Click "ENABLE"
- [ ] Đợi vài giây để API được enable
- [ ] Thấy thông báo "API enabled" ✅

**Ghi chú:**
- API Status: ☐ Enabled

### Bước 3: Tạo Service Account
- [ ] Menu trái → "APIs & Services" → "Credentials"
- [ ] Click "+ CREATE CREDENTIALS" → "Service account"
- [ ] Điền thông tin:
  - Service account name: `analytics-reader`
  - Description: "Service account để đọc Google Analytics data"
- [ ] Click "CREATE AND CONTINUE"
- [ ] Bỏ qua "Grant access" → Click "DONE"

**Ghi chú:**
- Service Account Name: `analytics-reader`
- Service Account ID: _________________________

### Bước 4: Download JSON Credentials
- [ ] Click vào Service Account vừa tạo
- [ ] Tab "KEYS" → "ADD KEY" → "Create new key"
- [ ] Chọn "JSON" → Click "CREATE"
- [ ] File JSON đã được download về máy
- [ ] Lưu file vào thư mục an toàn
  - Ví dụ: `D:\1app\medical\credentials\`
  - Hoặc: `D:\1app\medical\`

**Ghi chú:**
- File JSON path: _________________________
- File name: _________________________

### Bước 5: Lấy Email Service Account
- [ ] Mở file JSON vừa download
- [ ] Tìm dòng: `"client_email"`
- [ ] Copy email (ví dụ: `analytics-reader@project-id.iam.gserviceaccount.com`)

**Ghi chú:**
- Service Account Email: _________________________
- ⚠️ **LƯU EMAIL NÀY LẠI - CẦN Ở BƯỚC TIẾP THEO!**

---

## 🟢 PHẦN 2: GOOGLE ANALYTICS

### Bước 6: Thêm Service Account vào Google Analytics
- [ ] Truy cập https://analytics.google.com/
- [ ] Đăng nhập bằng tài khoản Google (cùng tài khoản với Google Cloud)
- [ ] Click icon ⚙️ **Admin** (góc dưới trái)
- [ ] Cột "Property" → "Property access management"
- [ ] Click nút "+" hoặc "Add users"
- [ ] Paste email Service Account vào ô "Email addresses"
- [ ] Chọn quyền: **"Viewer"**
- [ ] Click "Add"
- [ ] Thấy email xuất hiện trong danh sách với quyền "Viewer" ✅

**Ghi chú:**
- Email đã thêm: _________________________
- Quyền: ☐ Viewer

### Bước 7: Lấy Property ID
- [ ] Trong Google Analytics, vẫn ở phần Admin
- [ ] Cột "Property" → "Property Settings"
- [ ] Scroll xuống, tìm phần "Property ID"
- [ ] Copy số (ví dụ: `123456789` hoặc `130433471`)

**Ghi chú:**
- Property ID (số): _________________________
- Property ID (format): `properties/_________________________`
- ⚠️ **Format đúng: properties/123456789 (có prefix "properties/")**

---

## 🟡 PHẦN 3: CẤU HÌNH VÀO APP

### Bước 8: Cấu Hình Streamlit Secrets

#### Option A: Streamlit Cloud (Khuyến nghị)
- [ ] Vào Streamlit Cloud: https://share.streamlit.io/
- [ ] Chọn app của bạn
- [ ] Settings → Secrets
- [ ] Paste nội dung sau vào editor:

```toml
[google_analytics]
service_account_json = '''
{PASTE_TOÀN_BỘ_NỘI_DUNG_JSON_FILE_VÀO_ĐÂY}
'''
property_id = "properties/YOUR_PROPERTY_ID"
```

- [ ] Thay `YOUR_PROPERTY_ID` bằng số Property ID thực tế
- [ ] Click "Save"

**Ghi chú:**
- Streamlit Cloud App: _________________________
- Secrets đã lưu: ☐ Yes

#### Option B: Local Development
- [ ] Tạo thư mục `.streamlit` (nếu chưa có)
- [ ] Copy file template: `.streamlit/secrets.toml.example` → `.streamlit/secrets.toml`
- [ ] Mở file `.streamlit/secrets.toml`
- [ ] Paste nội dung JSON vào phần `service_account_json`
- [ ] Thay `property_id` bằng Property ID thực tế (format: `properties/123456789`)
- [ ] Lưu file

**Ghi chú:**
- File path: `.streamlit/secrets.toml`
- File đã tạo: ☐ Yes

---

## 🟣 PHẦN 4: KIỂM TRA

### Bước 9: Kiểm Tra Cấu Hình
- [ ] Chạy script kiểm tra:
  ```bash
  python setup_ga_api.py auto
  ```
- [ ] Tất cả kiểm tra đều ✅ OK
- [ ] Không có lỗi

**Kết quả kiểm tra:**
- [ ] ✅ Requirements: OK
- [ ] ✅ Credentials: OK
- [ ] ✅ Property ID: OK
- [ ] ✅ API Connection: OK

### Bước 10: Kiểm Tra Trên Trang Web
- [ ] Restart ứng dụng Streamlit (nếu đang chạy local)
- [ ] Mở trang web: https://clinical-assistant-drvietcanh.streamlit.app/
- [ ] Scroll xuống phần "Thống Kê Truy Cập"
- [ ] Thấy số liệu thực tế:
  - [ ] 👥 Người Dùng (30 ngày)
  - [ ] 🔄 Sessions
  - [ ] 📄 Lượt Xem Trang
  - [ ] ⚡ Đang Online

**Ghi chú:**
- Số liệu đã hiển thị: ☐ Yes
- Ngày kiểm tra: _________________________

---

## 📝 THÔNG TIN TỔNG HỢP

Sau khi hoàn thành, điền thông tin sau để tham khảo:

- **Google Cloud Project ID:** _________________________
- **Service Account Email:** _________________________
- **Property ID:** `properties/_________________________`
- **Measurement ID:** `G-_________________________` (đã có từ trước)
- **File JSON Location:** _________________________
- **Secrets Config:** ☐ Streamlit Cloud ☐ Local

---

## 🎉 HOÀN THÀNH!

Khi tất cả các bước đều ✅, bạn đã setup thành công Google Analytics API!

**Lưu ý:**
- Số liệu có thể mất vài phút để hiển thị sau khi có lượt truy cập thực tế
- Nếu không thấy số liệu ngay, đợi vài giờ rồi kiểm tra lại

---

## 📚 TÀI LIỆU THAM KHẢO

- Hướng dẫn chi tiết: `docs/HUONG_DAN_GOOGLE_CLOUD_STEP_BY_STEP.md`
- Hướng dẫn nhanh: `docs/QUICK_SETUP_GA_API.md`
- Hướng dẫn đầy đủ: `docs/GOOGLE_ANALYTICS_API_SETUP.md`

---

## 🔧 TROUBLESHOOTING

Nếu gặp lỗi, đánh dấu và xem hướng dẫn:

- [ ] ❌ "Permission denied" → Xem Bước 6
- [ ] ❌ "API not enabled" → Xem Bước 2
- [ ] ❌ "Property not found" → Xem Bước 7
- [ ] ❌ "No data" → Đợi vài giờ sau khi có lượt truy cập

---

**Ngày bắt đầu:** _________________________  
**Ngày hoàn thành:** _________________________  
**Ghi chú thêm:**  
_________________________________________________  
_________________________________________________  
_________________________________________________

