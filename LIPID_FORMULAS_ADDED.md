# Bổ Sung Các Công Thức Tính Lipid Chuyên Sâu

## Tóm Tắt
Đã bổ sung đầy đủ các công thức tính lipid chuyên sâu vào bảng chỉ số Lipid, bao gồm:
- Công thức tính LDL khi triglyceride quá cao (≥400 mg/dL)
- Các tỉ lệ lipid chuyên sâu
- Các chỉ số đánh giá nguy cơ tim mạch

## Các Công Thức Đã Bổ Sung

### 1. Tính LDL Cholesterol

#### a) Công thức Friedewald (1972) - Mặc định
- **Công thức:** LDL = Total Chol - HDL - (TG / 5) [mg/dL]
- **Công thức:** LDL = Total Chol - HDL - (TG / 2.2) [mmol/L]
- **Áp dụng:** Khi TG < 400 mg/dL (< 4.5 mmol/L)
- **Hạn chế:** Không chính xác khi TG ≥ 400 mg/dL

#### b) Công thức Sampson (2020) - Cho TG cao
- **Công thức:** LDL = Total Chol - HDL - TG/5 - (non-HDL - TG/5) × (TG/150) × 0.45
- **Áp dụng:** Khi TG ≥ 400 mg/dL
- **Ưu điểm:** Chính xác hơn Friedewald khi TG cao
- **Khuyến nghị:** AHA/ACC 2022

#### c) Công thức Martin/Hopkins (2013) - Alternative
- **Công thức:** Sử dụng hệ số động thay vì hệ số cố định 5
- **Hệ số:** Tăng từ 5 (TG < 150) đến 9 (TG > 400)
- **Áp dụng:** Khi TG ≥ 400 mg/dL (alternative method)

### 2. Non-HDL Cholesterol
- **Công thức:** Non-HDL = Total Chol - HDL
- **Ý nghĩa:** Bao gồm tất cả cholesterol gây xơ vữa (LDL + VLDL + IDL)
- **Mục tiêu:**
  - Very high risk: <100 mg/dL
  - High risk: <130 mg/dL
  - Moderate risk: <160 mg/dL
  - Low risk: <190 mg/dL

### 3. Remnant Cholesterol
- **Công thức:** Remnant = Total Chol - LDL - HDL
- **Ý nghĩa:** VLDL + IDL (nguy cơ tim mạch độc lập)
- **Lưu ý:** Quan trọng trong đánh giá nguy cơ tim mạch

### 4. Các Tỉ Lệ Lipid

#### a) Total Chol/HDL Ratio (Castelli Risk Index I)
- **Công thức:** Total Chol / HDL
- **Ý nghĩa:** Đánh giá nguy cơ tim mạch
- **Phân loại:**
  - <3.5: Low risk
  - 3.5-5.0: Average risk
  - >5.0: High risk

#### b) LDL/HDL Ratio (Castelli Risk Index II)
- **Công thức:** LDL / HDL
- **Ý nghĩa:** Đánh giá nguy cơ tim mạch
- **Phân loại:**
  - <2.0: Low risk
  - 2.0-3.0: Average risk
  - >3.0: High risk

#### c) TG/HDL Ratio
- **Công thức:** TG / HDL
- **Ý nghĩa:** Đánh giá kháng insulin và nguy cơ tim mạch
- **Phân loại (mmol/L):**
  - <0.87: Lý tưởng
  - 0.87-1.74: Bình thường
  - 1.74-2.62: Cao
  - >2.62: Quá cao
- **Phân loại (mg/dL):**
  - <2.0: Lý tưởng
  - 2.0-4.0: Bình thường
  - 4.0-6.0: Cao
  - >6.0: Quá cao

#### d) Non-HDL/HDL Ratio
- **Công thức:** Non-HDL / HDL
- **Ý nghĩa:** Đánh giá nguy cơ tim mạch
- **Phân loại:**
  - <3.0: Low risk
  - 3.0-3.6: Average risk
  - >3.6: High risk

### 5. Atherogenic Index of Plasma (AIP)
- **Công thức:** AIP = log₁₀(TG / HDL)
- **Ý nghĩa:** Đánh giá nguy cơ xơ vữa động mạch và kháng insulin
- **Phân loại:**
  - <-0.3: Low risk
  - -0.3 to 0.1: Average risk
  - >0.1: High risk
- **Lưu ý:** AIP > 0.1: Tăng nguy cơ xơ vữa động mạch và kháng insulin

### 6. Atherogenic Coefficient
- **Công thức:** (Total Chol - HDL) / HDL
- **Ý nghĩa:** Đánh giá nguy cơ tim mạch
- **Phân loại:**
  - <3.0: Low risk
  - 3.0-4.0: Average risk
  - >4.0: High risk

## Xử Lý Trường Hợp Triglyceride Quá Cao

### Khi TG < 400 mg/dL (< 4.5 mmol/L)
- ✅ Sử dụng công thức **Friedewald** (chính xác)
- Hiển thị kết quả với nhãn "Friedewald"

### Khi TG ≥ 400 mg/dL (≥ 4.5 mmol/L)
- ⚠️ Công thức Friedewald **KHÔNG chính xác**
- ✅ Sử dụng công thức **Sampson (2020)** (mặc định)
- ✅ Hiển thị thêm kết quả **Martin/Hopkins (2013)** (alternative)
- Cảnh báo người dùng về độ chính xác

## Tính Năng Mới

1. **Chế độ nhập linh hoạt:**
   - Tự động tính LDL từ công thức (mặc định)
   - Nhập LDL trực tiếp (nếu đã đo)

2. **Hiển thị đầy đủ:**
   - Tất cả các chỉ số lipid chuyên sâu
   - Interpretation cho từng chỉ số
   - Phân loại nguy cơ

3. **Cảnh báo thông minh:**
   - Cảnh báo khi TG ≥ 400 mg/dL
   - Gợi ý sử dụng công thức phù hợp
   - Hiển thị cả hai kết quả (Sampson và Martin/Hopkins) khi TG cao

## File Đã Cập Nhật

**labs/lipid.py**
- Thêm 3 hàm tính LDL: `calculate_ldl_friedewald()`, `calculate_ldl_sampson()`, `calculate_ldl_martin_hopkins()`
- Bổ sung tính toán và hiển thị:
  - Non-HDL cholesterol
  - Remnant cholesterol
  - 4 tỉ lệ lipid (Total Chol/HDL, LDL/HDL, TG/HDL, Non-HDL/HDL)
  - Atherogenic Index of Plasma (AIP)
  - Castelli Risk Index I & II
  - Atherogenic Coefficient
- Xử lý tự động khi TG ≥ 400 mg/dL
- Thêm expander với thông tin về các công thức

## Kết Quả

- ✅ **3 công thức tính LDL** (Friedewald, Sampson, Martin/Hopkins)
- ✅ **6 chỉ số lipid chuyên sâu** (Non-HDL, Remnant, 4 tỉ lệ)
- ✅ **2 chỉ số đánh giá nguy cơ** (AIP, Atherogenic Coefficient)
- ✅ **Xử lý tự động** khi TG ≥ 400 mg/dL
- ✅ **Interpretation đầy đủ** cho tất cả chỉ số
- ✅ Không có lỗi linter

## Ngày Cập Nhật
2025-02-05

