# ⚡ Quick Setup Google Analytics API

## 🎯 Mục Tiêu
Cấu hình Google Analytics API trong **5 phút** để hiển thị số liệu thực tế trên trang web.

---

## 🚀 Cách Nhanh Nhất

### **Bước 1: Chạy Script Helper**
```bash
# Windows
setup-ga-api.bat

# Hoặc Python
python setup_ga_api.py
```

Script sẽ:
- ✅ Kiểm tra requirements
- ✅ Kiểm tra credentials
- ✅ Kiểm tra Property ID
- ✅ Test kết nối API
- ✅ Tạo template secrets

---

## 📋 Checklist Nhanh

### **1. Google Cloud Console** (2 phút)
- [ ] Tạo/Chọn project
- [ ] Enable "Google Analytics Data API"
- [ ] Tạo Service Account
- [ ] Download JSON credentials

### **2. Google Analytics** (1 phút)
- [ ] Thêm Service Account email vào Property
- [ ] Quyền: **Viewer**
- [ ] Copy Property ID

### **3. Cấu Hình App** (2 phút)

#### **Option A: Streamlit Cloud (Khuyến nghị)**
1. Vào **Settings** → **Secrets**
2. Paste:
```toml
[google_analytics]
service_account_json = '''
{PASTE_TOÀN_BỘ_NỘI_DUNG_JSON_FILE}
'''
property_id = "properties/123456789"
```

#### **Option B: Local Development**
1. Tạo file `.streamlit/secrets.toml`
2. Copy từ `.streamlit/secrets.toml.example`
3. Điền thông tin

---

## ✅ Kiểm Tra

Chạy script:
```bash
python setup_ga_api.py
# Chọn option 7: Chạy tất cả kiểm tra
```

Nếu thấy:
- ✅ Tất cả đều OK → **Thành công!**
- ❌ Có lỗi → Xem troubleshooting bên dưới

---

## 🔧 Troubleshooting Nhanh

### ❌ "Permission denied"
→ Service Account chưa được thêm vào Google Analytics Property

### ❌ "API not enabled"
→ Enable "Google Analytics Data API" trong Google Cloud Console

### ❌ "Property not found"
→ Kiểm tra Property ID format: `properties/123456789` (có prefix `properties/`)

### ❌ "No data"
→ Đợi vài giờ sau khi có lượt truy cập thực tế

---

## 📚 Tài Liệu Đầy Đủ

Xem hướng dẫn chi tiết: [GOOGLE_ANALYTICS_API_SETUP.md](./GOOGLE_ANALYTICS_API_SETUP.md)

---

## 💡 Tips

1. **Service Account Email**: Tìm trong file JSON, field `client_email`
2. **Property ID**: Không phải Measurement ID (G-XXX), mà là số (123456789)
3. **Format Property ID**: Phải có prefix `properties/`
4. **Permissions**: Chỉ cần quyền "Viewer", không cần "Editor"

---

## 🎉 Hoàn Thành!

Sau khi setup xong, refresh trang web và scroll xuống phần "Thống Kê Truy Cập" → Sẽ thấy số liệu thực tế! 🚀

