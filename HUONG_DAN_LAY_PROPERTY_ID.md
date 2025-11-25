# 🆔 Hướng Dẫn Lấy Property ID - Chi Tiết

## 📍 BẠN ĐANG Ở ĐÂU?

Bạn đang ở phần **Admin** của Google Analytics, đã thấy menu bên trái với:
- "Quản trị" (Admin) - đang được chọn
- "Cài đặt tài sản" (Property settings) - đang mở
- "Tài sản" (Property) - đang mở

---

## 🎯 CÁCH LẤY PROPERTY ID

### **Cách 1: Từ Menu Bên Trái (Dễ nhất)**

1. **Nhìn vào menu bên trái**, trong phần "Tài sản" (Property)
2. Tìm dòng: **"Thông tin về tài sản"** (Property information)
   - Có icon giống tờ giấy 📄
3. **Click vào "Thông tin về tài sản"**

### **Cách 2: Từ Card Bên Phải**

1. **Nhìn sang bên phải**, tìm card có tiêu đề **"CÀI ĐẶT TÀI SẢN"** (PROPERTY SETTINGS)
2. Trong card đó, tìm phần **"Tài sản"** (Property)
3. Tìm dòng: **"Thông tin về tài sản"** (Property information)
   - Có icon giống tờ giấy 📄
4. **Click vào đó**

---

## 📋 SAU KHI CLICK "THÔNG TIN VỀ TÀI SẢN"

Bạn sẽ thấy một trang mới với thông tin về Property:

1. **Scroll xuống** trang này
2. Tìm phần **"Property ID"** hoặc **"Mã tài sản"**
3. Bạn sẽ thấy một **SỐ** (ví dụ: `130433471` hoặc `123456789`)
4. **Copy số đó!**

**Ví dụ bạn sẽ thấy:**
```
Property ID: 130433471
```
hoặc
```
Mã tài sản: 130433471
```

---

## ✅ SAU KHI CÓ PROPERTY ID

1. **Copy số đó** (ví dụ: `130433471`)

2. **Mở file:** `.streamlit/secrets.toml`
   - File này ở trong thư mục: `D:\1app\medical\.streamlit\secrets.toml`

3. **Tìm dòng:**
   ```toml
   property_id = "properties/YOUR_PROPERTY_ID"
   ```

4. **Thay `YOUR_PROPERTY_ID` bằng số bạn vừa copy:**
   ```toml
   property_id = "properties/130433471"
   ```
   (Thay `130433471` bằng số thực tế của bạn)

5. **Lưu file**

---

## 🔍 HÌNH ẢNH MÔ TẢ

Trong menu bên trái, bạn sẽ thấy:
```
📁 Cài đặt tài sản (Property settings) [đang mở]
  └─ 📁 Tài sản (Property) [đang mở]
      ├─ 📄 Thông tin về tài sản ← CLICK VÀO ĐÂY!
      ├─ 👥 Quản lý quyền truy cập và...
      ├─ 🕐 Nhật ký thay đổi của tài sản
      └─ ...
```

---

## 💡 LƯU Ý QUAN TRỌNG

- ✅ Property ID là một **SỐ** (ví dụ: `130433471`)
- ❌ **KHÔNG phải** Measurement ID (dạng `G-XXXXXXXXXX`)
- ✅ Format đúng: `properties/130433471` (có chữ `properties/` ở trước)
- ✅ Không có khoảng trắng

---

## 🎯 TÓM TẮT NHANH

1. Click **"Thông tin về tài sản"** (Property information)
2. Scroll xuống tìm **"Property ID"** hoặc **"Mã tài sản"**
3. Copy **SỐ** đó
4. Mở file `.streamlit/secrets.toml`
5. Thay `YOUR_PROPERTY_ID` bằng số bạn vừa copy
6. Lưu file

---

## ✅ SAU KHI XONG

Chạy lệnh để kiểm tra:
```bash
python setup_ga_api.py auto
```

Nếu tất cả đều ✅ → **Hoàn thành!** 🎉

---

**Bạn đã tìm thấy Property ID chưa?** Nếu gặp khó khăn, cho tôi biết bạn đang thấy gì trên màn hình! 😊

