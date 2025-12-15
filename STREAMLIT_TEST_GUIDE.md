# 🧪 HƯỚNG DẪN TEST STREAMLIT APP - PHASE 1 & PHASE 2

**Ngày:** 2025-02-05  
**Mục đích:** Test các tính năng Phase 1 & Phase 2 trong Streamlit app

---

## 🚀 BƯỚC 1: KHỞI ĐỘNG APP

```bash
cd D:\1app\medical
streamlit run app.py
```

App sẽ mở tại: `http://localhost:8501`

---

## 📋 CHECKLIST TEST

### ✅ PHASE 1: QUICK WINS

#### 1. References Component
**Vị trí:** Trong các calculators (CHA2DS2-VASc, SOFA, GCS)

**Test:**
- [ ] Mở calculator CHA2DS2-VASc
- [ ] Nhập thông tin và tính toán
- [ ] Kiểm tra phần "References" xuất hiện ở cuối
- [ ] Kiểm tra có:
  - [ ] Evidence level badges (màu sắc)
  - [ ] APA citations
  - [ ] PubMed links (clickable)
  - [ ] DOI links (nếu có)

**Expected:** References section hiển thị với đầy đủ thông tin

---

#### 2. Calculation History
**Vị trí:** Trong các calculators đã tích hợp

**Test:**
- [ ] Tính toán một vài lần trong CHA2DS2-VASc
- [ ] Kiểm tra history được lưu
- [ ] Tìm phần "Calculation History" hoặc "Lịch sử tính toán"
- [ ] Kiểm tra có thể:
  - [ ] Xem lịch sử
  - [ ] Search trong history
  - [ ] Export history (JSON/CSV)
  - [ ] Xóa entries

**Expected:** History được lưu và hiển thị đúng

---

#### 3. Share Results
**Vị trí:** Trong các calculators đã tích hợp

**Test:**
- [ ] Tính toán trong một calculator
- [ ] Tìm phần "Share Results" hoặc "Chia sẻ kết quả"
- [ ] Kiểm tra có thể:
  - [ ] Generate shareable link
  - [ ] Generate QR code (hiển thị image)
  - [ ] Copy link
  - [ ] Set expiration time

**Expected:** 
- Link được tạo thành công
- QR code hiển thị (image)
- Link có thể copy được

---

#### 4. Smart Suggestions
**Vị trí:** Trong các calculators đã tích hợp

**Test:**
- [ ] Tính toán trong CHA2DS2-VASc
- [ ] Tìm phần "Related Calculators" hoặc "Gợi ý"
- [ ] Kiểm tra hiển thị:
  - [ ] Related calculators (cùng category)
  - [ ] Popular calculators
  - [ ] Links đến các calculators khác

**Expected:** Suggestions hiển thị và clickable

---

### ✅ PHASE 2: CORE FEATURES

#### 5. Clinical Decision Rules với Flowcharts
**Vị trí:** Page "Phase 2 Features" → "Clinical Decision Rules"

**Test:**
- [ ] Navigate đến page "Phase 2 Features"
- [ ] Chọn "Clinical Decision Rules (Flowcharts)"
- [ ] Test từng algorithm:
  - [ ] **Wells PE Score:**
    - [ ] Flowchart hiển thị
    - [ ] Nodes có màu sắc đúng
    - [ ] Edges (arrows) hiển thị
    - [ ] Hover effects hoạt động
  - [ ] **PERC Rule:**
    - [ ] Flowchart hiển thị đúng
  - [ ] **CHA₂DS₂-VASc Score:**
    - [ ] Flowchart hiển thị đúng
  - [ ] **Sepsis-3 Protocol:**
    - [ ] Flowchart hiển thị đúng
  - [ ] **Acute Stroke:**
    - [ ] Flowchart hiển thị đúng
  - [ ] **AKI Diagnostic:**
    - [ ] Flowchart hiển thị đúng
  - [ ] **CURB-65:**
    - [ ] Flowchart hiển thị đúng

**Expected:** 
- Flowcharts hiển thị đẹp
- Interactive (hover effects)
- Legend hiển thị
- Algorithm descriptions có thể expand

---

#### 6. Pregnancy & Lactation Safety
**Vị trí:** Page "Phase 2 Features" → "Pregnancy & Lactation Safety"

**Test:**
- [ ] Navigate đến "Pregnancy & Lactation Safety"
- [ ] Chọn một số thuốc:
  - [ ] **Paracetamol:**
    - [ ] Pregnancy safety hiển thị
    - [ ] FDA Category hiển thị (màu sắc)
    - [ ] Risk level hiển thị
    - [ ] Trimester-specific info hiển thị
    - [ ] Lactation safety hiển thị
    - [ ] Briggs Category hiển thị
  - [ ] **Ibuprofen:**
    - [ ] Kiểm tra warning về 3rd trimester
  - [ ] **Doxycycline:**
    - [ ] Kiểm tra contraindicated warning
  - [ ] **Metformin:**
    - [ ] Kiểm tra safe in pregnancy

**Expected:**
- Color-coded risk levels
- Trimester-specific information
- References section
- Warning messages

---

#### 7. Pediatric Dosing Calculator
**Vị trí:** Page "Phase 2 Features" → "Pediatric Dosing Calculator"

**Test:**
- [ ] Navigate đến "Pediatric Dosing Calculator"
- [ ] Test **Weight-based dosing:**
  - [ ] Nhập weight: 20 kg
  - [ ] Nhập dose: 10 mg/kg
  - [ ] Set max dose: 200 mg
  - [ ] Click "Tính liều"
  - [ ] Kiểm tra kết quả: 200 mg (max)
  - [ ] Test với min dose
- [ ] Test **BSA-based dosing:**
  - [ ] Nhập weight: 20 kg
  - [ ] Nhập height: 100 cm
  - [ ] Nhập dose: 100 mg/m²
  - [ ] Click "Tính liều"
  - [ ] Kiểm tra BSA và dose được tính
- [ ] Test **Drug-specific Guidelines:**
  - [ ] Chọn "Paracetamol"
  - [ ] Kiểm tra guidelines hiển thị
  - [ ] Nhập weight và tính liều
  - [ ] Test với các thuốc khác:
    - [ ] Ibuprofen
    - [ ] Amoxicillin
    - [ ] Azithromycin

**Expected:**
- Calculations chính xác
- Min/max constraints hoạt động
- Guidelines hiển thị đúng
- Warning messages hiển thị

---

## 🐛 COMMON ISSUES & FIXES

### Issue 1: QR Code không hiển thị
**Symptom:** QR code section trống hoặc lỗi  
**Fix:** 
```bash
pip install qrcode Pillow
```

### Issue 2: Flowcharts không hiển thị
**Symptom:** Flowchart section trống  
**Check:**
- Browser console có lỗi không?
- HTML rendering có vấn đề không?

### Issue 3: Pregnancy Safety không có data
**Symptom:** "Chưa có thông tin"  
**Check:**
- Drug name có đúng không? (case-sensitive)
- Database có drug đó không?

### Issue 4: Pediatric Dosing calculation sai
**Symptom:** Kết quả không đúng  
**Check:**
- Units có đúng không? (mg/kg vs mcg/kg)
- Min/max constraints có áp dụng không?

---

## 📊 TEST RESULTS TEMPLATE

### Phase 1 Tests:
- [ ] References: ✅ / ❌
- [ ] History: ✅ / ❌
- [ ] Share Results: ✅ / ❌
- [ ] Smart Suggestions: ✅ / ❌

### Phase 2 Tests:
- [ ] Flowcharts: ✅ / ❌
- [ ] Pregnancy Safety: ✅ / ❌
- [ ] Pediatric Dosing: ✅ / ❌

### Issues Found:
1. 
2. 
3. 

---

## ✅ SUCCESS CRITERIA

**App được coi là PASS nếu:**
- ✅ Tất cả Phase 1 features hoạt động trong calculators
- ✅ Tất cả Phase 2 features hoạt động trong Phase 2 page
- ✅ Không có lỗi console
- ✅ UI hiển thị đẹp và responsive
- ✅ Tất cả links và buttons hoạt động

---

## 📝 NOTES

- Test trên nhiều browsers (Chrome, Firefox, Edge)
- Test trên mobile (responsive)
- Test với dark mode (nếu có)
- Test với slow network (offline mode)

---

**Happy Testing!** 🎉

