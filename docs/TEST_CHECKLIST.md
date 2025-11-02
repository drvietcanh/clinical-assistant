# 🧪 TEST CHECKLIST - Version 2.0.0

## ✅ Bugs Fixed Today:
1. **scores/config.py** - Updated status của PSI/PORT, Wells PE, NIHSS từ 📋 → ✅
2. **app.py** - Bổ sung PSI/PORT, Wells PE, NIHSS vào `ALL_CALCULATORS` dictionary

---

## 📋 TESTING GUIDE

### 1️⃣ **Main Menu Tests** (app.py)

#### Global Search:
- [ ] Gõ "NIHSS" → Xem có kết quả không
- [ ] Gõ "Wells" → Xem có hiện Wells PE không
- [ ] Gõ "PSI" → Xem có hiện PSI/PORT không
- [ ] Click nút "⭐ Yêu Thích" → Xem có add được không
- [ ] Click nút "➡️ Mở" → Xem có chuyển đúng trang không

#### Favorites System:
- [ ] Add 2-3 calculators vào Favorites
- [ ] Check section "⭐ Yêu Thích" hiển thị đúng
- [ ] Click nút "❌" để remove → Xem có xóa được không
- [ ] Refresh page → Xem favorites có giữ nguyên không

#### Recently Used:
- [ ] Mở 3-4 calculators khác nhau
- [ ] Check section "🕐 Sử Dụng Gần Đây" có update không
- [ ] Xem có đúng thứ tự không (mới nhất lên đầu)

#### Quick Access Cards:
- [ ] Click "📊 Scores" → Xem có chuyển đúng trang không
- [ ] Click "💊 Drugs" → Xem có chuyển đúng trang không
- [ ] Click "🔬 Labs" → Xem có chuyển đúng trang không
- [ ] Click "🫁 Ventilator" → Xem có chuyển đúng trang không
- [ ] Click "📋 Protocols" → Xem có chuyển đúng trang không

#### System Stats:
- [ ] Check "Tổng Calculators" = 37
- [ ] Check "Favorites" update khi add/remove
- [ ] Check "Recently Used" update khi mở calculator mới

---

### 2️⃣ **Scores Module Tests** (pages/01_📊_Scores.py)

#### Respiratory (Hô Hấp):
- [ ] Chọn chuyên khoa "🫁 Hô Hấp"
- [ ] Xem có 5 scores: CURB-65, PSI/PORT, Wells PE, SMART-COP, BODE
- [ ] Click "✅ CURB-65" → Xem calculator hoạt động không
- [ ] Click "✅ PSI/PORT" → **TEST TOÀN BỘ**:
  - [ ] Nhập tuổi 65
  - [ ] Chọn Nam, Viện dưỡng lão = Không
  - [ ] Nhập các thông số (temp, HR, RR, BP, glucose, pH, BUN, Na, Hct)
  - [ ] Click "Tính Toán PSI/PORT"
  - [ ] Xem có hiển thị kết quả Risk Class không
  - [ ] Xem có khuyến nghị điều trị không
- [ ] Click "✅ Wells PE" → **TEST TOÀN BỘ**:
  - [ ] Chọn các tiêu chí (DVT signs, PE most likely, HR>100, etc.)
  - [ ] Click "Tính Wells PE Score"
  - [ ] Xem có hiển thị probability không
  - [ ] Xem có khuyến nghị D-dimer/CTPA không
- [ ] Click "📋 SMART-COP" → Xem có hiển thị placeholder "🚧 Đang phát triển" không
- [ ] Click "📋 BODE Index" → Xem có hiển thị placeholder không

#### Neurology (Thần Kinh):
- [ ] Chọn chuyên khoa "🧠 Thần Kinh"
- [ ] Xem có 5 scores: GCS, NIHSS, ICH, Hunt & Hess, mRS
- [ ] Click "✅ GCS" → Xem calculator hoạt động không
- [ ] Click "✅ NIHSS" → **TEST TOÀN BỘ**:
  - [ ] **1a. Mức Độ Ý Thức**: Chọn "Tỉnh táo" (0 điểm)
  - [ ] **1b. Câu Hỏi LOC**: Chọn "Đáp ứng cả 2" (0 điểm)
  - [ ] **1c. Lệnh LOC**: Chọn "Thực hiện cả 2" (0 điểm)
  - [ ] **2. Nhìn**: Chọn "Bình thường" (0 điểm)
  - [ ] **3. Thị Trường**: Chọ "Không thiếu hụt" (0 điểm)
  - [ ] **4. Liệt Mặt**: Chọn "Bình thường" (0 điểm)
  - [ ] **5. Vận Động Tay Trái**: Chọn "Không rơi" (0 điểm)
  - [ ] **6. Vận Động Tay Phải**: Chọn "Không rơi" (0 điểm)
  - [ ] **7. Vận Động Chân Trái**: Chọn "Không rơi" (0 điểm)
  - [ ] **8. Vận Động Chân Phải**: Chọn "Không rơi" (0 điểm)
  - [ ] **9. Mất Điều Hòa**: Chọn "Không có" (0 điểm)
  - [ ] **10. Cảm Giác**: Chọn "Bình thường" (0 điểm)
  - [ ] **11. Ngôn Ngữ**: Chọn "Bình thường" (0 điểm)
  - [ ] **12. Lời Nói**: Chọn "Bình thường" (0 điểm)
  - [ ] **13. Inattention**: Chọn "Không có" (0 điểm)
  - [ ] Click "Tính NIHSS Score"
  - [ ] Xem kết quả = 0 (Không có triệu chứng đột quỵ)
  - [ ] **TEST SCORE CAO**: Chọn các giá trị cao (ví dụ: LOC=3, Gaze=2, Visual=3, Facial=3, Motor Arm L/R=4, Motor Leg L/R=4, Limb Ataxia=2, Sensory=2, Language=3, Dysarthria=2, Extinction=2)
  - [ ] Click "Tính NIHSS Score"
  - [ ] Xem có hiển thị SEVERE STROKE (>15) không
  - [ ] Xem có khuyến nghị thrombolysis/thrombectomy không
- [ ] Click "📋 ICH Score" → Xem placeholder
- [ ] Click "📋 Hunt & Hess" → Xem placeholder
- [ ] Click "📋 mRS" → Xem placeholder

#### Cardiology (Tim Mạch):
- [ ] Chọn chuyên khoa "❤️ Tim Mạch"
- [ ] Xem có 8 scores với status ✅
- [ ] Test random 2-3 scores để verify hoạt động tốt

#### Emergency (Cấp Cứu):
- [ ] Chọn chuyên khoa "🚨 Cấp Cứu"
- [ ] Xem có 5 scores
- [ ] Test qSOFA

---

### 3️⃣ **Unit Conversion Tests**

#### Labs Module:
- [ ] Mở "🔬 Labs" → "Lipid Panel"
- [ ] Kiểm tra default = **mmol/L** ✅
- [ ] Nhập Total Chol = 5.2 mmol/L
- [ ] Xem có hiển thị "≈ 201 mg/dL" không
- [ ] Switch sang mg/dL → Nhập 200 mg/dL
- [ ] Xem có hiển thị "≈ 5.17 mmol/L" không

- [ ] Mở "🔬 Labs" → "BMP"
- [ ] Kiểm tra Creatinine default = **µmol/L** ✅
- [ ] Nhập 88 µmol/L
- [ ] Xem có hiển thị "≈ 1.0 mg/dL" không

#### Scores Module (Cardiology):
- [ ] Mở "📊 Scores" → "SCORE2"
- [ ] Kiểm tra Cholesterol default = **mmol/L** ✅
- [ ] Test unit conversion

---

### 4️⃣ **Vietnamese Localization Tests**

- [ ] Check tất cả menu items = tiếng Việt
- [ ] Check tất cả button labels = tiếng Việt
- [ ] Check tất cả interpretations/recommendations = tiếng Việt
- [ ] Check tooltips/help text = tiếng Việt

---

### 5️⃣ **Mobile Responsive Tests**

- [ ] Resize browser window xuống 375px (iPhone size)
- [ ] Xem sidebar có collapse không
- [ ] Xem các cards có stack vertically không
- [ ] Xem các inputs có responsive không

---

### 6️⃣ **Performance Tests**

- [ ] Page load time < 2 seconds
- [ ] Calculator response time < 0.5 seconds
- [ ] No console errors in browser DevTools
- [ ] No Python errors in terminal

---

## 🐛 Known Issues (If Any):

_Record any bugs found during testing here:_

1. 
2. 
3. 

---

## 📊 Test Results Summary:

- **Date Tested:** ___________
- **Tested By:** ___________
- **Pass Rate:** _____ / _____
- **Critical Bugs:** _____
- **Minor Bugs:** _____

---

## ✅ Sign-off:

- [ ] All critical features working
- [ ] No breaking bugs
- [ ] Ready for deployment to Streamlit Cloud

**Tester:** _______________  
**Date:** _______________

