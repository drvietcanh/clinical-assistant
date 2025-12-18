# Phân Tích Dữ Liệu Định Lượng Thuốc Theo eGFR

## 📋 Tổng Quan

File `ab_data_from_xlsx.json` chứa dữ liệu về định lượng các kháng sinh dựa trên eGFR (estimated Glomerular Filtration Rate - Mức lọc cầu thận ước tính). Đây là dữ liệu quan trọng để điều chỉnh liều thuốc cho bệnh nhân suy thận.

## 🔍 Cấu Trúc Dữ Liệu

### Các Khoảng eGFR Được Sử Dụng:
- `eGFR > 80`: Chức năng thận bình thường
- `eGFR từ 60-80`: Suy thận nhẹ (CKD G2)
- `eGFR từ 50-60`: Suy thận nhẹ-trung bình
- `eGFR từ 40-50`: Suy thận trung bình (CKD G3a)
- `eGFR từ 30-40`: Suy thận trung bình-nặng (CKD G3b)
- `eGFR từ 20-30`: Suy thận nặng (CKD G4)
- `eGFR từ 10-20`: Suy thận rất nặng (CKD G5)
- `eGRF < 10`: Suy thận giai đoạn cuối (CKD G5)
- `Chạy thận`: Bệnh nhân đang lọc máu

## ✅ Phân Tích Logic Theo Từng Nhóm Thuốc

### 1. **Cephalosporins (Ceftriaxone, Ceftazidime)**

#### Ceftriaxone 1g & 2g
- **Logic**: Không điều chỉnh liều ở tất cả các mức eGFR
- **Đánh giá**: ✅ **HỢP LÝ**
- **Lý do**: Ceftriaxone chủ yếu bài tiết qua mật (60-70%), chỉ 33-67% bài tiết qua thận. Do đó không cần điều chỉnh liều ở suy thận.

#### Ceftazidime 2g
- **Vấn đề**: ⚠️ **DỮ LIỆU KHÔNG ĐẦY ĐỦ** - chỉ có 1 khoảng eGFR (30-40)
- **Khuyến nghị**: Cần bổ sung đầy đủ các khoảng eGFR

### 2. **Beta-lactam/Beta-lactamase Inhibitor Combinations**

#### Ampicillin/Sulbactam 1/0,5g
- **Logic**: 
  - eGFR > 30: 2 lọ x 4 lần/ngày
  - eGFR 20-30: 1-2 lọ x 2 lần/ngày
  - eGFR 10-20: 1-2 lọ x 1 lần/ngày
  - eGFR < 10: 1 lọ x 1 lần/ngày
- **Đánh giá**: ✅ **HỢP LÝ**
- **Lý do**: Cả ampicillin và sulbactam đều bài tiết chủ yếu qua thận, cần giảm tần suất khi eGFR giảm.

#### Cefoperazone/Sulbactam 0.5/0.5g
- **Logic**: 
  - eGFR > 20: 2 lọ x 2 lần/ngày
  - eGFR ≤ 20: 1 lọ x 2 lần/ngày
- **Đánh giá**: ✅ **HỢP LÝ**
- **Lý do**: Cefoperazone bài tiết qua mật và thận, sulbactam qua thận. Cần giảm liều ở suy thận nặng.

#### Piperacillin/Tazobactam 4.5g
- **Logic**: 
  - eGFR > 50: 4.5g x 4 lần/ngày
  - eGFR 40-50: 2.25g (1/2 lọ) x 4 lần/ngày
  - eGFR 10-40: 2.25g x 3 lần/ngày
  - eGFR < 10: 2.25g x 3 lần/ngày
  - Chạy thận: 2.25g x 2 lần/ngày + 0.75g sau chạy thận
- **Đánh giá**: ✅ **HỢP LÝ**
- **Lý do**: Cả piperacillin và tazobactam đều bài tiết chủ yếu qua thận. Cần giảm liều và tần suất.

### 3. **Carbapenems**

#### Meropenem 0.5g
- **Logic**: 
  - eGFR > 50: 1g (2 lọ) x 3 lần/ngày
  - eGFR 40-50: 1g x 2 lần/ngày
  - eGFR 20-40: 0.5g (1 lọ) x 2 lần/ngày
  - eGFR < 20: 0.5g x 1 lần/ngày
- **Đánh giá**: ✅ **HỢP LÝ**
- **Lý do**: Meropenem bài tiết chủ yếu qua thận, cần điều chỉnh cả liều và tần suất.

#### Meropenem 1g
- **Logic**: 
  - eGFR > 50: 1g x 3 lần/ngày
  - eGFR 40-50: 1g x 2 lần/ngày
  - eGFR 20-40: 0.5g (1/2 lọ) x 2 lần/ngày
  - eGFR < 20: 0.5g x 1 lần/ngày
- **Đánh giá**: ✅ **HỢP LÝ**

#### Ertapenem 1g
- **Logic**: 
  - eGFR > 20: 1g x 1 lần/ngày
  - eGFR ≤ 20: 0.5g (1/2 lọ) x 1 lần/ngày
  - Chạy thận: 0.5g + 0.167g (1/6 lọ) sau chạy thận nếu truyền < 6h trước
- **Đánh giá**: ✅ **HỢP LÝ**
- **Lưu ý**: Ertapenem 0.5g có entry nhưng trống - cần bổ sung

#### Imipenem/cilastatin 0.5/0.5g
- **Logic**: 
  - eGFR > 50: 0.5g x 4 lần/ngày
  - eGFR 40-50: 0.5g x 3 lần/ngày
  - eGFR 10-40: 0.25g (1/2 lọ) x 2 lần/ngày
- **Đánh giá**: ✅ **HỢP LÝ**
- **Lưu ý**: Có typo "Imipenem 0.5/0.5g" thay vì "Imipenem/cilastatin 0.5/0.5g" ở một số dòng

### 4. **Fluoroquinolones**

#### Ciprofloxacin 0.4g
- **Logic**: 
  - eGFR > 20: 0.4g x 2 lần/ngày
  - eGFR ≤ 20: 0.4g x 1 lần/ngày
- **Đánh giá**: ✅ **HỢP LÝ**
- **Lý do**: Ciprofloxacin bài tiết qua thận và gan, cần giảm tần suất ở suy thận nặng.

#### Levofloxacin 0.5g
- **Logic**: 
  - eGFR > 50: 0.75g (1.5 lọ) x 1 lần/ngày
  - eGFR 40-50: 0.75g x 1 lần/2 ngày
  - eGFR < 40: 0.5g (1 lọ) x 1 lần/2 ngày
- **Đánh giá**: ✅ **HỢP LÝ**
- **Lý do**: Levofloxacin bài tiết chủ yếu qua thận (80-90%), cần kéo dài khoảng cách liều.

#### Levofloxacin 0.75g
- **Logic**: 
  - eGFR > 50: 0.75g x 1 lần/ngày
  - eGFR 40-50: 0.75g x 1 lần/2 ngày
  - eGFR < 40: 0.5g (2/3 lọ) x 1 lần/2 ngày
- **Đánh giá**: ✅ **HỢP LÝ**

#### Moxifloxacin 0.4g
- **Logic**: Không điều chỉnh liều ở tất cả các mức eGFR
- **Đánh giá**: ✅ **HỢP LÝ**
- **Lý do**: Moxifloxacin chủ yếu chuyển hóa qua gan, không cần điều chỉnh ở suy thận.

### 5. **Glycopeptides**

#### Vancomycin 0.5g
- **Logic**: 
  - eGFR > 50: 1g (2 lọ) x 2 lần/ngày
  - eGFR 40-50: 1g x 1 lần/ngày
  - eGFR 10-40: 0.5g (1 lọ) x 1 lần/3 ngày
  - eGFR < 10: 0.25g (1/2 lọ) x 1 lần/3 ngày
- **Đánh giá**: ✅ **HỢP LÝ**
- **Lý do**: Vancomycin bài tiết chủ yếu qua thận, cần điều chỉnh đáng kể. **QUAN TRỌNG**: Cần TDM (therapeutic drug monitoring).

#### Vancomycin 1g
- **Logic**: 
  - eGFR > 50: 1g x 2 lần/ngày
  - eGFR 40-50: 1g x 1 lần/ngày
  - eGFR 10-40: 0.5g (1/2 lọ) x 1 lần/3 ngày
  - eGFR < 10: 0.25g (1/4 lọ) x 1 lần/3 ngày
- **Đánh giá**: ✅ **HỢP LÝ**

#### Teicoplanin 0.4g
- **Logic**: 
  - eGFR > 60: 0.4g x 1 lần/ngày
  - eGFR 50-60: 0.4g x 1 lần/2 ngày
  - eGFR < 50: 0.4g x 1 lần/3 ngày
- **Đánh giá**: ✅ **HỢP LÝ**
- **Lý do**: Teicoplanin có thời gian bán thải rất dài, cần kéo dài khoảng cách liều ở suy thận.

### 6. **Polymyxins**

#### Colistin 2 M IU
- **Logic**: 
  - eGFR > 60: 4 M IU (2 lọ) x 2 lần/ngày
  - eGFR 50-60: 3-4 M IU x 2 lần/ngày
  - eGFR 40-50: 3 M IU x 2 lần/ngày hoặc 2 M IU x 3 lần/ngày
  - eGFR 20-40: 3 M IU x 2 lần/ngày
  - eGFR < 20: 2 M IU x 2 lần/ngày
  - Chạy thận: 1 M IU x 1 lần sau mỗi lần chạy thận
- **Đánh giá**: ✅ **HỢP LÝ**
- **Lý do**: Colistin rất độc thận, cần điều chỉnh cẩn thận. **QUAN TRỌNG**: Theo dõi chức năng thận chặt chẽ.

### 7. **Oxazolidinones**

#### Linezolid 0.6g
- **Logic**: Không điều chỉnh liều ở tất cả các mức eGFR
- **Đánh giá**: ✅ **HỢP LÝ**
- **Lý do**: Linezolid chuyển hóa qua gan, không cần điều chỉnh ở suy thận.

### 8. **Lincosamides**

#### Clindamycin 0.6g
- **Logic**: Không điều chỉnh liều ở tất cả các mức eGFR
- **Đánh giá**: ✅ **HỢP LÝ**
- **Lý do**: Clindamycin chuyển hóa qua gan, không cần điều chỉnh ở suy thận.

### 9. **Nitroimidazoles**

#### Metronidazole 0.5g
- **Logic**: 
  - eGFR > 10: 0.5g x 3 lần/ngày
  - eGFR ≤ 10: 0.5g x 2 lần/ngày
- **Đánh giá**: ✅ **HỢP LÝ**
- **Lý do**: Metronidazole chuyển hóa qua gan nhưng có metabolite hoạt động bài tiết qua thận, cần giảm nhẹ ở suy thận nặng.

### 10. **Phosphonic Acids**

#### Fosfomycin 1g
- **Logic**: 
  - eGFR > 50: 2g (2 lọ) x 2 lần/ngày
  - eGFR 40-50: 2g x 1 lần/ngày
  - eGFR 20-40: 2g x 2 lần/3 ngày
  - eGFR 10-20: 2g x 1 lần/2 ngày
  - eGFR < 10: 2g x 1 lần/3 ngày
- **Đánh giá**: ✅ **HỢP LÝ**
- **Lưu ý**: Có typo "Fosmycin" thay vì "Fosfomycin"

## ⚠️ Các Vấn Đề Phát Hiện

### 1. **Lỗi Chính Tả**
- ❌ `"eGRF < 10"` → ✅ Nên là `"eGFR < 10"` (chữ F viết hoa)
- ❌ `"Fosmycin"` → ✅ Nên là `"Fosfomycin"`
- ❌ `"Imipenem 0.5/0.5g"` (thiếu "/cilastatin") ở một số dòng

### 2. **Dữ Liệu Không Đầy Đủ**
- ⚠️ **Ceftazidime 2g**: Chỉ có 1 khoảng eGFR (30-40), thiếu các khoảng khác
- ⚠️ **Ertapenem 0.5g**: Entry trống hoàn toàn

### 3. **Inconsistencies trong Formatting**
- Một số dùng `"x"` (chữ thường), một số dùng `"X"` (chữ hoa)
- Một số có khoảng trắng thừa: `"x 2 lần/ ngày"` vs `"x 2 lần/ngày"`
- Một số dùng dấu phẩy: `"0,5g"`, một số dùng dấu chấm: `"0.5g"`

## 📊 Đánh Giá Tổng Thể

### ✅ **Điểm Mạnh:**
1. Logic điều chỉnh liều phù hợp với nguyên tắc dược động học
2. Phân loại eGFR rõ ràng theo các giai đoạn CKD
3. Có xử lý riêng cho bệnh nhân chạy thận
4. Bao phủ nhiều nhóm kháng sinh quan trọng

### ⚠️ **Cần Cải Thiện:**
1. Sửa lỗi chính tả (eGRF → eGFR)
2. Bổ sung dữ liệu thiếu (Ceftazidime, Ertapenem 0.5g)
3. Chuẩn hóa formatting (thống nhất dấu, chữ hoa/thường)
4. Có thể thêm các thuốc khác: Amikacin, Gentamicin, Tobramycin (aminoglycosides)

## 🔧 Khuyến Nghị

### 1. **Sửa Lỗi Ngay Lập Tức:**
```json
// Thay tất cả "eGRF" thành "eGFR"
"eGFR < 10": "..."
```

### 2. **Bổ Sung Dữ Liệu Thiếu:**
- Hoàn thiện Ceftazidime 2g với tất cả các khoảng eGFR
- Bổ sung Ertapenem 0.5g hoặc xóa entry nếu không dùng

### 3. **Chuẩn Hóa Format:**
- Thống nhất: `"X"` (chữ hoa) cho dấu nhân
- Thống nhất: `"0.5g"` (dấu chấm) cho số thập phân
- Loại bỏ khoảng trắng thừa

### 4. **Mở Rộng Dữ Liệu:**
- Thêm aminoglycosides (Amikacin, Gentamicin, Tobramycin)
- Thêm các cephalosporin khác (Cefepime, Ceftolozane/tazobactam)
- Thêm các thuốc mới (Ceftazidime/avibactam, Meropenem/vaborbactam)

## 📚 Tài Liệu Tham Khảo

1. **Sanford Guide to Antimicrobial Therapy** - Renal dosing adjustments
2. **IDSA Guidelines** - Antimicrobial stewardship in renal impairment
3. **Lexicomp** - Drug dosing in renal impairment
4. **Micromedex** - Renal dosing adjustments

## ✅ Kết Luận

**Logic định lượng trong file `ab_data_from_xlsx.json` về cơ bản là HỢP LÝ và phù hợp với các nguyên tắc dược động học và hướng dẫn lâm sàng.** 

Tuy nhiên, cần:
1. ✅ Sửa các lỗi chính tả và formatting
2. ✅ Bổ sung dữ liệu thiếu
3. ✅ Chuẩn hóa cấu trúc dữ liệu
4. ✅ Có thể tích hợp vào hệ thống tính liều tự động

Sau khi sửa các vấn đề trên, dữ liệu này có thể được sử dụng để:
- Tích hợp vào hệ thống tính liều tự động
- Tạo bảng tra cứu nhanh cho bác sĩ
- Phát triển ứng dụng hỗ trợ quyết định lâm sàng

