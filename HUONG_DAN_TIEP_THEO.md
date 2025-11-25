# 🎯 Hướng Dẫn Tiếp Theo - Google Analytics API Setup

## ✅ BƯỚC 1 ĐÃ HOÀN THÀNH!

Bạn đã:
- ✅ Truy cập Google Cloud Console
- ✅ Đang ở project: **My First Project**
- ✅ Project ID: `ordinal-tower-479306-f0`
- ✅ Project Number: `497365919716`

---

## 📋 BƯỚC 2: ENABLE GOOGLE ANALYTICS DATA API

### Cách 1: Từ Quick Access (Nhanh nhất)
1. Trong màn hình hiện tại, tìm phần **"Quick access"**
2. Click vào card **"APIs & Services"** (card đầu tiên)
3. Bạn sẽ vào trang APIs & Services

### Cách 2: Từ Menu
1. Click icon **☰ Menu** (góc trên trái, 3 đường ngang)
2. Tìm **"APIs & Services"** → Click **"Library"**

### Tiếp tục:
3. Trong ô **tìm kiếm** (có placeholder "Search for APIs..."), gõ: **"Google Analytics Data API"**
4. Click vào kết quả **"Google Analytics Data API"**
5. Click nút **"ENABLE"** (màu xanh, ở trên cùng)
6. Đợi vài giây để API được enable
7. Bạn sẽ thấy thông báo **"API enabled"** hoặc icon ✅

**✅ Đánh dấu trong checklist khi hoàn thành!**

---

## 📋 BƯỚC 3: TẠO SERVICE ACCOUNT

Sau khi enable API xong:

1. Ở trang APIs & Services, click **"Credentials"** (menu bên trái hoặc tab trên cùng)
2. Click **"+ CREATE CREDENTIALS"** (nút màu xanh, ở trên cùng)
3. Chọn **"Service account"** từ dropdown menu
4. Điền thông tin:
   - **Service account name**: `analytics-reader`
   - **Description** (tùy chọn): `Service account để đọc Google Analytics data`
5. Click **"CREATE AND CONTINUE"**
6. Ở bước "Grant this service account access to project":
   - **BỎ QUA** (không cần grant)
   - Click **"CONTINUE"** hoặc **"DONE"**

**✅ Đánh dấu trong checklist khi hoàn thành!**

---

## 📋 BƯỚC 4: DOWNLOAD JSON CREDENTIALS

1. Trong danh sách **Service Accounts**, click vào service account vừa tạo (tên: `analytics-reader`)
2. Ở trên cùng, click tab **"KEYS"**
3. Click **"ADD KEY"** → **"Create new key"**
4. Chọn **"JSON"** làm key type
5. Click **"CREATE"**
6. File JSON sẽ **tự động download** về máy
7. **Lưu file này an toàn!**
   - Tên file thường: `ordinal-tower-479306-f0-xxxxx.json`
   - Lưu vào: `D:\1app\medical\` hoặc `D:\1app\medical\credentials\`

**✅ Đánh dấu trong checklist khi hoàn thành!**

---

## 💡 LƯU Ý

- File JSON chứa thông tin bảo mật, **KHÔNG chia sẻ** với ai
- File đã được thêm vào `.gitignore`, sẽ không commit lên GitHub
- Giữ file này an toàn để dùng cho các bước tiếp theo

---

## 🎯 BƯỚC TIẾP THEO

Sau khi download file JSON xong:
1. Mở file JSON để lấy **Service Account Email** (field `client_email`)
2. Tiếp tục với **Bước 5-6** trong checklist: Thêm vào Google Analytics

---

**Chúc bạn thành công!** 🚀

