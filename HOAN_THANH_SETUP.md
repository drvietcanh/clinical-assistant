# ✅ Hoàn Thành Setup Google Analytics API

## 🎉 BẠN ĐÃ LÀM ĐƯỢC:

- ✅ Download file JSON credentials
- ✅ Tạo file cấu hình `.streamlit/secrets.toml`
- ✅ Lấy Property ID: `514243692`
- ✅ Cập nhật Property ID vào file cấu hình

---

## 📋 THÔNG TIN ĐÃ CẤU HÌNH:

- **Project ID:** `ordinal-tower-479306-f0`
- **Service Account Email:** `analytics-reader@ordinal-tower-479306-f0.iam.gserviceaccount.com`
- **Property ID:** `properties/514243692`
- **File Config:** `.streamlit/secrets.toml` ✅

---

## ⚠️ BƯỚC CUỐI CÙNG: THÊM EMAIL VÀO GOOGLE ANALYTICS

Bạn cần thêm Service Account email vào Google Analytics Property:

### **Cách làm:**

1. **Vào Google Analytics:** https://analytics.google.com/

2. **Click Admin** (icon ⚙️ góc dưới trái)

3. **Ở cột giữa (Property):**
   - Tìm **"Quản lý quyền truy cập và..."** hoặc **"Property access management"**
   - **Click vào đó**

4. **Thêm email:**
   - Click nút **"+"** hoặc **"Thêm người dùng"** / **"Add users"**
   - Paste email này: `analytics-reader@ordinal-tower-479306-f0.iam.gserviceaccount.com`
   - Chọn quyền: **"Viewer"** (Người xem)
   - Click **"Thêm"** hoặc **"Add"**

5. **Xong!** Email sẽ xuất hiện trong danh sách

---

## ✅ SAU KHI THÊM EMAIL XONG

### **1. Đợi vài phút** (để permissions được cập nhật)

### **2. Kiểm tra lại:**
```bash
python setup_ga_api.py auto
```

Nếu thấy:
- ✅ Requirements: OK
- ✅ Credentials: OK
- ✅ Property ID: OK
- ✅ API Connection: OK

→ **Thành công!** 🎉

### **3. Kiểm tra trên trang web:**
1. Restart ứng dụng Streamlit (nếu đang chạy local)
2. Mở trang web: https://clinical-assistant-drvietcanh.streamlit.app/
3. Scroll xuống phần **"Thống Kê Truy Cập"**
4. Sẽ thấy số liệu thực tế:
   - 👥 Người Dùng (30 ngày)
   - 🔄 Sessions
   - 📄 Lượt Xem Trang
   - ⚡ Đang Online

---

## 🔧 NẾU VẪN CHƯA THẤY SỐ LIỆU

### **Nguyên nhân có thể:**

1. **Service Account chưa được thêm vào Google Analytics**
   - → Làm lại bước "Thêm email vào Google Analytics" ở trên

2. **Permissions chưa được cập nhật**
   - → Đợi 5-10 phút rồi thử lại

3. **Chưa có dữ liệu trong Google Analytics**
   - → Đợi vài giờ sau khi có lượt truy cập thực tế
   - → Hoặc tự truy cập trang web để tạo dữ liệu

4. **Google Analytics Data API chưa được enable**
   - → Vào Google Cloud Console
   - → APIs & Services → Library
   - → Tìm "Google Analytics Data API" → Enable

---

## 📝 TÓM TẮT

**Bạn đã hoàn thành:**
- ✅ File JSON credentials
- ✅ File cấu hình secrets.toml
- ✅ Property ID: 514243692

**Còn lại:**
- ⏳ Thêm email vào Google Analytics Property (bước trên)
- ⏳ Đợi vài phút để permissions cập nhật
- ⏳ Kiểm tra lại

---

## 🎯 BƯỚC TIẾP THEO

1. **Thêm email vào Google Analytics** (xem hướng dẫn ở trên)
2. **Đợi 5-10 phút**
3. **Chạy kiểm tra:** `python setup_ga_api.py auto`
4. **Xem kết quả trên trang web**

---

**Chúc bạn thành công!** 🚀

Nếu gặp vấn đề, cho tôi biết bạn đang ở bước nào!

