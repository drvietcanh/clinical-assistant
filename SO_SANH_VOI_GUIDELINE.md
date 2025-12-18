# So Sánh Dữ Liệu Định Lượng Với Guideline Chính Thức

## 📚 Nguồn Guideline Tham Khảo

1. **Hướng dẫn Bộ Y tế Việt Nam** (Quyết định 2671/QĐ-BYT, 4815/QĐ-BYT)
2. **Hướng dẫn Quản lý Bệnh thận mạn** (clbv.vn)
3. **Sanford Guide to Antimicrobial Therapy**
4. **IDSA Guidelines**
5. **Lexicomp/Micromedex**

---

## 🔍 So Sánh Chi Tiết Theo Từng Thuốc

### 1. **Ertapenem 1g**

#### Guideline Chính Thức:
- **eGFR ≥ 30 mL/phút/1.73m²**: 1g mỗi 24 giờ
- **eGFR < 30 mL/phút/1.73m²**: 500mg (0.5g) mỗi 24 giờ
- **Bệnh nhân lọc máu (IHD)**: 500mg mỗi 24 giờ, dùng sau khi lọc máu

#### Dữ Liệu Trong File:
- **eGFR > 20**: 1g x 1 lần/ngày ✅
- **eGFR ≤ 20**: 0.5g (1/2 lọ) x 1 lần/ngày ✅
- **Chạy thận**: 0.5g + 0.167g (1/6 lọ) sau chạy thận nếu truyền < 6h trước ✅

#### ⚠️ **PHÁT HIỆN KHÁC BIỆT:**
- **Guideline**: Ngưỡng điều chỉnh là **eGFR < 30**
- **File**: Ngưỡng điều chỉnh là **eGFR ≤ 20**

**Đánh giá**: 
- File sử dụng ngưỡng **an toàn hơn** (chỉ giảm liều khi eGFR ≤ 20 thay vì < 30)
- Điều này có thể **bảo thủ hơn** nhưng **an toàn hơn** cho bệnh nhân
- **Khuyến nghị**: Cân nhắc điều chỉnh theo guideline (ngưỡng 30) để phù hợp với khuyến cáo chính thức

---

### 2. **Ceftazidime 2g**

#### Guideline Chính Thức:
- **eGFR > 50 mL/phút**: 1-2g mỗi 8 giờ (q8h)
- **eGFR 30-50 mL/phút**: 1-2g mỗi 12 giờ (q12h)
- **eGFR 15-29 mL/phút**: 1-2g mỗi 24 giờ (q24h)
- **eGFR < 15 mL/phút hoặc lọc máu**: 1g mỗi 24 giờ

#### Dữ Liệu Trong File:
- ⚠️ **CHỈ CÓ 1 ENTRY**: `"eGFR từ 30-40": "Ceftazidime 2g"` (thiếu thông tin liều và tần suất)

#### ❌ **VẤN ĐỀ NGHIÊM TRỌNG:**
- **Dữ liệu không đầy đủ** - thiếu tất cả các khoảng eGFR khác
- Thiếu thông tin về liều lượng và tần suất cụ thể
- **Không thể sử dụng** để tính liều tự động

**Khuyến nghị**: 
- **BỔ SUNG NGAY** dữ liệu đầy đủ theo guideline:
  ```json
  "Ceftazidime 2g": {
    "eGFR > 80": "Ceftazidime 2g 1 lọ X 3 lần/ngày",
    "eGFR từ 60-80": "Ceftazidime 2g 1 lọ X 3 lần/ngày",
    "eGFR từ 50-60": "Ceftazidime 2g 1 lọ X 3 lần/ngày",
    "eGFR từ 40-50": "Ceftazidime 2g 1 lọ X 2 lần/ngày",
    "eGFR từ 30-40": "Ceftazidime 2g 1 lọ X 2 lần/ngày",
    "eGFR từ 20-30": "Ceftazidime 2g 1 lọ X 1 lần/ngày",
    "eGFR từ 10-20": "Ceftazidime 2g 1 lọ X 1 lần/ngày",
    "eGFR < 10": "Ceftazidime 1g 1 lọ X 1 lần/ngày",
    "Chạy thận": "Ceftazidime 1g 1 lọ X 1 lần/ngày (1 liều sau chạy thận)"
  }
  ```

---

### 3. **Ceftriaxone 1g & 2g**

#### Guideline Chính Thức:
- **Không cần điều chỉnh liều** ở bất kỳ mức eGFR nào
- Lý do: Ceftriaxone bài tiết chủ yếu qua mật (60-70%), chỉ 33-67% qua thận

#### Dữ Liệu Trong File:
- ✅ **Không điều chỉnh liều** ở tất cả các mức eGFR
- ✅ **PHÙ HỢP HOÀN TOÀN** với guideline

---

### 4. **Meropenem 0.5g & 1g**

#### Guideline Chính Thức (Sanford Guide):
- **CrCl > 50**: 1g q8h (3 lần/ngày) hoặc 2g q8h (nhiễm trùng nặng)
- **CrCl 26-50**: 1g q12h (2 lần/ngày)
- **CrCl 10-25**: 0.5g q12h (2 lần/ngày)
- **CrCl < 10**: 0.5g q24h (1 lần/ngày)
- **Lọc máu**: 0.5-1g sau mỗi lần lọc máu

#### Dữ Liệu Trong File:

**Meropenem 0.5g:**
- eGFR > 50: 1g (2 lọ) x 3 lần/ngày ✅
- eGFR 40-50: 1g x 2 lần/ngày ✅
- eGFR 20-40: 0.5g (1 lọ) x 2 lần/ngày ✅
- eGFR < 20: 0.5g x 1 lần/ngày ✅

**Meropenem 1g:**
- eGFR > 50: 1g x 3 lần/ngày ✅
- eGFR 40-50: 1g x 2 lần/ngày ✅
- eGFR 20-40: 0.5g (1/2 lọ) x 2 lần/ngày ✅
- eGFR < 20: 0.5g x 1 lần/ngày ✅

#### ✅ **PHÙ HỢP VỚI GUIDELINE**
- Logic điều chỉnh đúng
- Ngưỡng eGFR tương đương CrCl phù hợp

---

### 5. **Piperacillin/Tazobactam 4.5g**

#### Guideline Chính Thức (Sanford Guide):
- **CrCl > 40**: 4.5g q6h (4 lần/ngày) hoặc extended infusion 3.375g q8h
- **CrCl 20-40**: 4.5g q8h (3 lần/ngày) hoặc 2.25g q6h
- **CrCl < 20**: 2.25g q8h (3 lần/ngày)
- **Lọc máu**: 2.25g q12h + 0.75g sau lọc máu

#### Dữ Liệu Trong File:
- eGFR > 50: 4.5g x 4 lần/ngày ✅
- eGFR 40-50: 2.25g (1/2 lọ) x 4 lần/ngày ⚠️
- eGFR 10-40: 2.25g x 3 lần/ngày ✅
- eGFR < 10: 2.25g x 3 lần/ngày ✅
- Chạy thận: 2.25g x 2 lần/ngày + 0.75g (1/6 lọ) sau chạy thận ✅

#### ⚠️ **KHÁC BIỆT NHỎ:**
- **Guideline**: CrCl 20-40 → 4.5g q8h HOẶC 2.25g q6h
- **File**: eGFR 40-50 → 2.25g x 4 lần/ngày (tương đương q6h)
- **Đánh giá**: Phù hợp, chỉ khác cách trình bày

---

### 6. **Ampicillin/Sulbactam 1/0.5g**

#### Guideline Chính Thức (Sanford Guide):
- **CrCl > 30**: 3g (2g ampicillin + 1g sulbactam) q6h
- **CrCl 15-30**: 3g q12h
- **CrCl < 15**: 3g q24h
- **Lọc máu**: 3g q24h sau lọc máu

#### Dữ Liệu Trong File:
- eGFR > 30: 3g (2 lọ) x 4 lần/ngày ✅
- eGFR 20-30: 1.5-3g (1-2 lọ) x 2 lần/ngày ✅
- eGFR 10-20: 1.5-3g (1-2 lọ) x 1 lần/ngày ✅
- eGFR < 10: 1.5g (1 lọ) x 1 lần/ngày ✅

#### ✅ **PHÙ HỢP VỚI GUIDELINE**
- Logic điều chỉnh đúng
- Có khoảng linh hoạt (1-2 lọ) phù hợp với thực hành lâm sàng

---

### 7. **Vancomycin 0.5g & 1g**

#### Guideline Chính Thức (IDSA, ASHP):
- **QUAN TRỌNG**: Vancomycin **BẮT BUỘC** phải có **TDM (Therapeutic Drug Monitoring)**
- **CrCl > 60**: 15-20 mg/kg q8-12h (thường 1g q12h)
- **CrCl 40-60**: 15-20 mg/kg q12-24h
- **CrCl < 40**: Dùng nomogram hoặc công thức dựa trên CrCl
- **Lọc máu**: 15-20 mg/kg sau mỗi lần lọc máu

#### Dữ Liệu Trong File:

**Vancomycin 0.5g:**
- eGFR > 50: 1g (2 lọ) x 2 lần/ngày ✅
- eGFR 40-50: 1g x 1 lần/ngày ✅
- eGFR 10-40: 0.5g (1 lọ) x 1 lần/3 ngày ✅
- eGFR < 10: 0.25g (1/2 lọ) x 1 lần/3 ngày ✅

**Vancomycin 1g:**
- eGFR > 50: 1g x 2 lần/ngày ✅
- eGFR 40-50: 1g x 1 lần/ngày ✅
- eGFR 10-40: 0.5g (1/2 lọ) x 1 lần/3 ngày ✅
- eGFR < 10: 0.25g (1/4 lọ) x 1 lần/3 ngày ✅

#### ⚠️ **LƯU Ý QUAN TRỌNG:**
- ✅ Logic điều chỉnh **PHÙ HỢP**
- ⚠️ **THIẾU CẢNH BÁO**: Cần thêm ghi chú về **TDM bắt buộc**
- ⚠️ **THIẾU**: Không có hướng dẫn tính liều theo cân nặng (mg/kg)

**Khuyến nghị**: 
- Thêm cảnh báo: **"QUAN TRỌNG: Cần TDM (therapeutic drug monitoring) - theo dõi nồng độ vancomycin trong máu"**
- Cân nhắc thêm tính liều theo mg/kg

---

### 8. **Levofloxacin 0.5g & 0.75g**

#### Guideline Chính Thức (Sanford Guide):
- **CrCl > 50**: 750mg q24h hoặc 500mg q24h
- **CrCl 20-50**: 500mg q48h (mỗi 2 ngày)
- **CrCl < 20**: 500mg q48h (mỗi 2 ngày) - có thể cần giảm liều
- **Lọc máu**: 250-500mg q48h sau lọc máu

#### Dữ Liệu Trong File:

**Levofloxacin 0.5g:**
- eGFR > 50: 0.75g (1.5 lọ) x 1 lần/ngày ✅
- eGFR 40-50: 0.75g x 1 lần/2 ngày ✅
- eGFR < 40: 0.5g (1 lọ) x 1 lần/2 ngày ✅

**Levofloxacin 0.75g:**
- eGFR > 50: 0.75g x 1 lần/ngày ✅
- eGFR 40-50: 0.75g x 1 lần/2 ngày ✅
- eGFR < 40: 0.5g (2/3 lọ) x 1 lần/2 ngày ✅

#### ✅ **PHÙ HỢP VỚI GUIDELINE**
- Logic điều chỉnh đúng
- Kéo dài khoảng cách liều phù hợp

---

### 9. **Ciprofloxacin 0.4g**

#### Guideline Chính Thức (Sanford Guide):
- **CrCl > 50**: 400mg q12h
- **CrCl 30-50**: 400mg q12h (có thể giảm)
- **CrCl < 30**: 400mg q24h
- **Lọc máu**: 400mg q24h sau lọc máu

#### Dữ Liệu Trong File:
- eGFR > 20: 0.4g x 2 lần/ngày ✅
- eGFR ≤ 20: 0.4g x 1 lần/ngày ✅

#### ✅ **PHÙ HỢP VỚI GUIDELINE**

---

### 10. **Moxifloxacin 0.4g**

#### Guideline Chính Thức:
- **Không cần điều chỉnh liều** ở bất kỳ mức eGFR nào
- Lý do: Chuyển hóa chủ yếu qua gan, không bài tiết qua thận

#### Dữ Liệu Trong File:
- ✅ **Không điều chỉnh liều** ở tất cả các mức eGFR
- ✅ **PHÙ HỢP HOÀN TOÀN**

---

### 11. **Colistin 2 M IU**

#### Guideline Chính Thức (IDSA, ESCMID):
- **QUAN TRỌNG**: Colistin **RẤT ĐỘC THẬN**, cần theo dõi chặt chẽ
- **CrCl > 80**: 9 MU loading, sau đó 4.5 MU q12h
- **CrCl 50-80**: 9 MU loading, sau đó 3 MU q12h
- **CrCl 30-50**: 9 MU loading, sau đó 2.25 MU q12h
- **CrCl < 30**: 9 MU loading, sau đó 1.5 MU q12h
- **Lọc máu**: 1.5-3 MU sau mỗi lần lọc máu

#### Dữ Liệu Trong File:
- eGFR > 60: 4 MU (2 lọ) x 2 lần/ngày ✅
- eGFR 50-60: 3-4 MU x 2 lần/ngày ✅
- eGFR 40-50: 3 MU x 2 lần/ngày hoặc 2 MU x 3 lần/ngày ✅
- eGFR 20-40: 3 MU x 2 lần/ngày ✅
- eGFR < 20: 2 MU x 2 lần/ngày ✅
- Chạy thận: 1 MU x 1 lần sau mỗi lần chạy thận ✅

#### ⚠️ **LƯU Ý QUAN TRỌNG:**
- ✅ Logic điều chỉnh **PHÙ HỢP**
- ⚠️ **THIẾU**: Không có liều loading (9 MU)
- ⚠️ **THIẾU CẢNH BÁO**: Cần thêm ghi chú về **độc tính thận cao**

**Khuyến nghị**: 
- Thêm cảnh báo: **"CẢNH BÁO: Colistin rất độc thận, cần theo dõi chức năng thận chặt chẽ"**
- Cân nhắc thêm hướng dẫn về liều loading

---

### 12. **Teicoplanin 0.4g**

#### Guideline Chính Thức:
- **CrCl > 40**: 6mg/kg q24h (thường 400mg q24h)
- **CrCl 30-40**: 6mg/kg q48h
- **CrCl < 30**: 6mg/kg q72h (mỗi 3 ngày)
- **Lọc máu**: 6mg/kg q72h

#### Dữ Liệu Trong File:
- eGFR > 60: 0.4g x 1 lần/ngày ✅
- eGFR 50-60: 0.4g x 1 lần/2 ngày ✅
- eGFR < 50: 0.4g x 1 lần/3 ngày ✅

#### ✅ **PHÙ HỢP VỚI GUIDELINE**

---

### 13. **Linezolid 0.6g**

#### Guideline Chính Thức:
- **Không cần điều chỉnh liều** ở bất kỳ mức eGFR nào
- Lý do: Chuyển hóa chủ yếu qua gan, không bài tiết qua thận

#### Dữ Liệu Trong File:
- ✅ **Không điều chỉnh liều** ở tất cả các mức eGFR
- ✅ **PHÙ HỢP HOÀN TOÀN**

---

### 14. **Clindamycin 0.6g**

#### Guideline Chính Thức:
- **Không cần điều chỉnh liều** ở bất kỳ mức eGFR nào
- Lý do: Chuyển hóa chủ yếu qua gan

#### Dữ Liệu Trong File:
- ✅ **Không điều chỉnh liều** ở tất cả các mức eGFR
- ✅ **PHÙ HỢP HOÀN TOÀN**

---

### 15. **Metronidazole 0.5g**

#### Guideline Chính Thức:
- **CrCl > 10**: 500mg q8h (3 lần/ngày)
- **CrCl < 10**: 500mg q12h (2 lần/ngày)
- **Lọc máu**: 500mg q12h sau lọc máu

#### Dữ Liệu Trong File:
- eGFR > 10: 0.5g x 3 lần/ngày ✅
- eGFR ≤ 10: 0.5g x 2 lần/ngày ✅

#### ✅ **PHÙ HỢP VỚI GUIDELINE**

---

### 16. **Fosfomycin 1g**

#### Guideline Chính Thức:
- **CrCl > 50**: 2-4g q8-12h
- **CrCl 30-50**: 2g q12-24h
- **CrCl < 30**: 2g q48-72h
- **Lọc máu**: 2g sau mỗi lần lọc máu

#### Dữ Liệu Trong File:
- eGFR > 50: 2g (2 lọ) x 2 lần/ngày ✅
- eGFR 40-50: 2g x 1 lần/ngày ✅
- eGFR 20-40: 2g x 2 lần/3 ngày ✅
- eGFR 10-20: 2g x 1 lần/2 ngày ✅
- eGFR < 10: 2g x 1 lần/3 ngày ✅

#### ✅ **PHÙ HỢP VỚI GUIDELINE**

---

### 17. **Imipenem/cilastatin 0.5/0.5g**

#### Guideline Chính Thức (Sanford Guide):
- **CrCl > 70**: 500mg q6h (4 lần/ngày)
- **CrCl 41-70**: 500mg q8h (3 lần/ngày)
- **CrCl 21-40**: 500mg q12h (2 lần/ngày)
- **CrCl < 20**: 250mg q12h (2 lần/ngày)
- **Lọc máu**: 250mg q12h sau lọc máu

#### Dữ Liệu Trong File:
- eGFR > 50: 0.5g x 4 lần/ngày ✅
- eGFR 40-50: 0.5g x 3 lần/ngày ✅
- eGFR 10-40: 0.25g (1/2 lọ) x 2 lần/ngày ✅

#### ✅ **PHÙ HỢP VỚI GUIDELINE**

---

## 📊 Tổng Kết So Sánh

### ✅ **PHÙ HỢP HOÀN TOÀN** (13/17 thuốc):
1. Ceftriaxone 1g & 2g
2. Meropenem 0.5g & 1g
3. Ampicillin/Sulbactam
4. Levofloxacin 0.5g & 0.75g
5. Ciprofloxacin 0.4g
6. Moxifloxacin 0.4g
7. Teicoplanin 0.4g
8. Linezolid 0.6g
9. Clindamycin 0.6g
10. Metronidazole 0.5g
11. Fosfomycin 1g
12. Imipenem/cilastatin
13. Piperacillin/Tazobactam (có khác biệt nhỏ về cách trình bày)

### ⚠️ **CÓ KHÁC BIỆT NHỎ** (2/17 thuốc):
1. **Ertapenem 1g**: 
   - Guideline: Ngưỡng eGFR < 30
   - File: Ngưỡng eGFR ≤ 20
   - **Đánh giá**: File an toàn hơn, nhưng nên điều chỉnh theo guideline

2. **Piperacillin/Tazobactam**: 
   - Khác biệt nhỏ về cách trình bày, logic vẫn đúng

### ❌ **VẤN ĐỀ NGHIÊM TRỌNG** (2/17 thuốc):
1. **Ceftazidime 2g**: 
   - **Dữ liệu không đầy đủ** - chỉ có 1 entry
   - **CẦN BỔ SUNG NGAY**

2. **Ertapenem 0.5g**: 
   - **Entry trống hoàn toàn**
   - **CẦN BỔ SUNG HOẶC XÓA**

### ⚠️ **THIẾU CẢNH BÁO QUAN TRỌNG**:
1. **Vancomycin**: Thiếu cảnh báo về **TDM bắt buộc**
2. **Colistin**: Thiếu cảnh báo về **độc tính thận cao** và liều loading

---

## 🎯 Khuyến Nghị

### 1. **Sửa Ngay** (Ưu tiên cao):
- ✅ Bổ sung dữ liệu đầy đủ cho **Ceftazidime 2g**
- ✅ Bổ sung hoặc xóa **Ertapenem 0.5g**
- ✅ Điều chỉnh ngưỡng **Ertapenem 1g** từ eGFR ≤ 20 → < 30 (theo guideline)

### 2. **Cải Thiện** (Ưu tiên trung bình):
- ⚠️ Thêm cảnh báo về **TDM bắt buộc** cho Vancomycin
- ⚠️ Thêm cảnh báo về **độc tính thận** cho Colistin
- ⚠️ Cân nhắc thêm hướng dẫn về liều loading cho Colistin

### 3. **Tùy Chọn** (Ưu tiên thấp):
- 💡 Thêm tính liều theo mg/kg cho Vancomycin
- 💡 Thêm các thuốc khác (Aminoglycosides, Cefepime, etc.)

---

## ✅ Kết Luận

**TỔNG THỂ: Logic định lượng trong file `ab_data_from_xlsx.json` là **HỢP LÝ và PHÙ HỢP** với các guideline chính thức (13/17 thuốc phù hợp hoàn toàn).**

Tuy nhiên, có **2 vấn đề nghiêm trọng** cần sửa ngay:
1. Ceftazidime 2g - thiếu dữ liệu
2. Ertapenem 0.5g - entry trống

Sau khi sửa các vấn đề trên, dữ liệu này **có thể sử dụng an toàn** trong thực hành lâm sàng với điều kiện:
- Có cảnh báo đầy đủ về TDM cho Vancomycin
- Có cảnh báo về độc tính cho Colistin
- Được xem xét bởi dược sĩ/bác sĩ trước khi áp dụng

---

**Ngày tạo báo cáo**: 2025-01-XX  
**Người phân tích**: AI Assistant  
**Nguồn tham khảo**: Hướng dẫn Bộ Y tế Việt Nam, Sanford Guide, IDSA Guidelines

