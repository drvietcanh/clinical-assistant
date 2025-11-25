# 📖 Hướng Dẫn Sử Dụng: Kiểm Tra Tương Tác Thuốc

**Version:** 1.0  
**Last Updated:** 2025-02-05  
**Status:** ✅ Production Ready

---

## 🎯 Tổng Quan

Công cụ **Kiểm Tra Tương Tác Thuốc** giúp phát hiện và đánh giá tương tác giữa các thuốc trong danh sách điều trị của bệnh nhân. Hệ thống hỗ trợ:

- ✅ **500+ tương tác thuốc** được phân loại theo mức độ nghiêm trọng
- ✅ **Class-based matching** - Tự động nhận diện tương tác theo nhóm thuốc
- ✅ **Fuzzy matching** - Tìm thuốc ngay cả khi gõ sai chính tả
- ✅ **Autocomplete** - Gợi ý thuốc khi nhập
- ✅ **Ma trận tương tác trực quan** - Hiển thị tất cả tương tác trong một bảng

---

## 🚀 Cách Sử Dụng

### **Bước 1: Truy Cập Tính Năng**

1. Mở ứng dụng Clinical Assistant
2. Điều hướng đến **"Drugs"** → **"Drug Interactions"**
3. Hoặc tìm kiếm "tương tác thuốc" trong thanh tìm kiếm

### **Bước 2: Nhập Danh Sách Thuốc**

Có 2 cách nhập:

#### **Cách 1: Nhập Từng Thuốc**
1. Chọn **"Nhập từng thuốc"**
2. Chọn số lượng thuốc (1-20)
3. Nhập tên từng thuốc vào các ô tương ứng
4. Hệ thống sẽ tự động gợi ý khi bạn nhập (autocomplete)

#### **Cách 2: Nhập Danh Sách (Bulk)**
1. Chọn **"Nhập danh sách (mỗi dòng một thuốc)"**
2. Dán hoặc nhập danh sách thuốc, mỗi thuốc một dòng:
   ```
   Warfarin
   Aspirin
   Metformin
   Omeprazole
   ```

### **Bước 3: Kiểm Tra Tương Tác**

1. Nhấn nút **"🔍 Kiểm Tra Tương Tác"**
2. Hệ thống sẽ:
   - Tự động chuẩn hóa tên thuốc (fuzzy matching)
   - Kiểm tra tất cả các cặp thuốc
   - Phân loại theo mức độ nghiêm trọng
   - Hiển thị kết quả

---

## 📊 Hiểu Kết Quả

### **Tóm Tắt Tổng Quan**

Sau khi kiểm tra, bạn sẽ thấy:
- **Tổng số tương tác** được phát hiện
- **Phân bố theo mức độ:**
  - 🔴 **Major (Nghiêm trọng):** Cần xử trí ngay
  - 🟡 **Moderate (Trung bình):** Cần theo dõi
  - 🔵 **Minor (Nhẹ):** Ít ảnh hưởng

### **Ma Trận Tương Tác**

Ma trận hiển thị tất cả các cặp thuốc:
- ✅ **Xanh:** Không có tương tác
- 🔴 **Đỏ:** Tương tác nghiêm trọng
- 🟡 **Vàng:** Tương tác trung bình
- 🔵 **Xanh dương:** Tương tác nhẹ

### **Chi Tiết Tương Tác**

Mỗi tương tác hiển thị:
- **🔬 Cơ chế:** Cách thức tương tác xảy ra
- **📝 Mô tả:** Mô tả ngắn gọn về tương tác
- **⚕️ Ý nghĩa lâm sàng:** Tác động lâm sàng chi tiết
- **📋 Hướng xử trí:** Khuyến nghị xử trí cụ thể
- **💡 Thuốc thay thế:** Gợi ý thuốc thay thế (nếu có)
- **📚 Tài liệu tham khảo:** Nguồn tham khảo

---

## 🔍 Tính Năng Nâng Cao

### **1. Fuzzy Matching (Tìm Kiếm Thông Minh)**

Hệ thống tự động nhận diện thuốc ngay cả khi:
- Gõ sai chính tả nhẹ
- Viết hoa/thường khác nhau
- Tên tiếng Việt

**Ví dụ:**
- "warfarin" → Tự động nhận diện "Warfarin"
- "omeprazol" → Tự động nhận diện "Omeprazole"
- "aspirin" → Tự động nhận diện "Aspirin"

### **2. Class-Based Interactions (Tương Tác Theo Nhóm)**

Hệ thống tự động nhận diện nhóm thuốc và kiểm tra tương tác:

**Ví dụ:**
- Nhập "Lisinopril" → Hệ thống nhận diện là "ACE Inhibitor"
- Kiểm tra tương tác với "Potassium" → Phát hiện tương tác "ACE Inhibitor + Potassium"

**Các nhóm được hỗ trợ:**
- ACE Inhibitors (Lisinopril, Captopril, Enalapril...)
- ARBs (Losartan, Valsartan...)
- Beta-blockers (Metoprolol, Atenolol...)
- CCBs (Amlodipine, Nifedipine...)
- Statins (Atorvastatin, Simvastatin...)
- NSAIDs (Ibuprofen, Naproxen...)
- SSRIs (Fluoxetine, Sertraline...)
- PPIs (Omeprazole, Pantoprazole...)
- Và nhiều nhóm khác...

### **3. Autocomplete (Gợi Ý Tự Động)**

Khi nhập tên thuốc:
- Hệ thống tự động gợi ý các thuốc phù hợp
- Nhấn vào gợi ý để chọn nhanh
- Tìm kiếm theo tên tiếng Anh hoặc tiếng Việt

### **4. Tìm Kiếm và Lọc**

Sau khi có kết quả:
- **Tìm kiếm:** Nhập từ khóa để tìm trong danh sách tương tác
- **Lọc theo mức độ:** Chọn mức độ nghiêm trọng muốn xem

---

## 📋 Ví Dụ Sử Dụng

### **Ví Dụ 1: Bệnh Nhân Tim Mạch**

**Danh sách thuốc:**
- Warfarin
- Aspirin
- Lisinopril
- Metoprolol
- Atorvastatin

**Kết quả:**
- 🔴 **Major:** Warfarin + Aspirin (tăng nguy cơ xuất huyết)
- 🟡 **Moderate:** Lisinopril + Atorvastatin (có thể tăng tác dụng)

**Khuyến nghị:**
- Tránh dùng chung Warfarin + Aspirin nếu không cần thiết
- Theo dõi INR thường xuyên nếu phải dùng chung

### **Ví Dụ 2: Bệnh Nhân Đái Tháo Đường + Tim Mạch**

**Danh sách thuốc:**
- Metformin
- Glibenclamide
- Lisinopril
- Atorvastatin
- Omeprazole

**Kết quả:**
- 🟡 **Moderate:** Lisinopril + Atorvastatin
- ✅ Không có tương tác nghiêm trọng khác

**Khuyến nghị:**
- Theo dõi chức năng thận và kali máu

### **Ví Dụ 3: Bệnh Nhân Dùng Kháng Sinh**

**Danh sách thuốc:**
- Warfarin
- Metronidazole
- Ciprofloxacin

**Kết quả:**
- 🔴 **Major:** Warfarin + Metronidazole (tăng nguy cơ xuất huyết nặng)
- 🟡 **Moderate:** Warfarin + Ciprofloxacin

**Khuyến nghị:**
- Giảm liều Warfarin 30-50% khi dùng Metronidazole
- Theo dõi INR 2-3 lần/tuần
- Cân nhắc dùng kháng sinh khác nếu có thể

---

## ⚠️ Lưu Ý Quan Trọng

### **Giới Hạn**

1. **Database không đầy đủ:**
   - Database hiện tại bao gồm ~500 tương tác phổ biến
   - Không phải tất cả tương tác đều được bao phủ
   - Luôn tham khảo nguồn đáng tin cậy (Micromedex, Lexicomp, AHFS)

2. **Không thay thế đánh giá lâm sàng:**
   - Công cụ chỉ hỗ trợ quyết định lâm sàng
   - Bác sĩ phải tự đánh giá và quyết định
   - Xem xét từng trường hợp cụ thể

3. **Cần cập nhật thường xuyên:**
   - Database cần được cập nhật khi có thông tin mới
   - Tham khảo tài liệu mới nhất

### **Khuyến Nghị**

1. **Luôn xác minh:**
   - Kiểm tra lại với nguồn đáng tin cậy
   - Tham khảo ý kiến chuyên gia nếu cần

2. **Xem xét bối cảnh:**
   - Tình trạng bệnh nhân
   - Liều lượng thuốc
   - Thời gian dùng thuốc
   - Các yếu tố nguy cơ khác

3. **Theo dõi:**
   - Theo dõi dấu hiệu tương tác
   - Xét nghiệm cần thiết (INR, chức năng thận, kali máu...)
   - Điều chỉnh liều nếu cần

---

## 📚 Tài Liệu Tham Khảo

Database được xây dựng dựa trên:
- **Micromedex** - Drug Interactions
- **Lexicomp** - Drug Interactions
- **AHFS Drug Information** - Drug Interactions
- **Clinical Pharmacology** - Drug Interactions
- **FDA Drug Interactions** - Warnings and Precautions

---

## 🆘 Hỗ Trợ

Nếu gặp vấn đề hoặc có câu hỏi:
1. Kiểm tra lại tên thuốc đã nhập đúng chưa
2. Thử dùng tên tiếng Anh thay vì tiếng Việt
3. Kiểm tra xem thuốc có trong database chưa
4. Liên hệ đội phát triển nếu cần hỗ trợ

---

## 📊 Thống Kê Database

- **Tổng số tương tác:** ~500+
- **Số thuốc được hỗ trợ:** 200+
- **Số nhóm thuốc:** 20+
- **Phân bố mức độ:**
  - Major: ~43%
  - Moderate: ~51%
  - Minor: ~6%

---

**Version:** 1.0  
**Last Updated:** 2025-02-05  
**Status:** ✅ Production Ready

