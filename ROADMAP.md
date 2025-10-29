# Lộ Trình Phát Triển Clinical Assistant - Hệ Thống Hỗ Trợ Lâm Sàng Toàn Diện
**Phiên bản:** 1.0  
**Ngày:** 2025-10-29  
**Kiến trúc:** Google Apps Script + Google Sheets (Mobile-First SPA)

---

## 📋 TỔNG QUAN Dự ÁN

### Mục tiêu
Xây dựng hệ thống công cụ lâm sàng toàn diện, dễ sử dụng trên di động, có khả năng mở rộng module mà không ảnh hưởng các chức năng hiện có.

### Nguyên tắc thiết kế
✅ **Module hóa** - Mỗi chức năng độc lập  
✅ **Mobile-First** - Tối ưu cho điện thoại  
✅ **Offline-Ready** - Cache dữ liệu thông minh  
✅ **Evidence-Based** - Dựa trên hướng dẫn quốc tế  
✅ **Easy Maintenance** - Cập nhật qua Google Sheets

---

## 🏗️ KIẾN TRÚC HIỆN TẠI (✓ Đã triển khai)

### Frontend (Single Page Application)
```
web/
├── index.html          # Entry point, navigation
├── styles.html         # Global CSS + Router
├── app.html            # Shared utilities (el function)
├── scores.html         # Module: Scoring systems
├── antibiotics.html    # Module: Antibiotic dosing
├── vent.html          # Module: Ventilator management
└── protocols.html     # Module: Clinical protocols
```

### Backend (Google Apps Script)
```
server/
├── Code.gs            # Web app entry point (doGet)
├── Core.gs            # Core utilities (DB access, cache)
├── Scores.api.gs      # Scores API endpoints
├── Antibiotics.api.gs # Antibiotics API endpoints
├── Vent.api.gs        # Ventilator API endpoints
└── Protocols.api.gs   # Protocols API endpoints
```

### Database (Google Sheets)
```
Sheets:
├── Meta               # Version control
├── Scores             # qSOFA, SOFA, CHA2DS2-VASc, MELD-Na, APACHE II
├── Antibiotics        # Dosing + renal adjustment
├── Ventilator         # ARDS, COPD, PEEP/FiO2 tables
└── Protocols          # COPD, HAP/VAP, DKA, UGIB
```

---

## 🎯 LỘ TRÌNH PHÁT TRIỂN CHI TIẾT

## GIAI ĐOẠN 1: Củng Cố Nền Tảng (Tuần 1-2) ⭐ ƯU TIÊN CAO

### 1.1. Hoàn thiện các Module Hiện tại

#### **A. Module Scores (Thang điểm lâm sàng)**
**Điểm cần bổ sung:**

| Thang điểm | Mục đích | Độ ưu tiên | Tham khảo |
|-----------|----------|------------|-----------|
| **SOFA** | Đánh giá suy cơ quan | ⭐⭐⭐ | Sepsis-3 (JAMA 2016) |
| **APACHE II** | Dự đoán tử vong ICU | ⭐⭐⭐ | Knaus 1985 |
| **CHA₂DS₂-VASc** | Nguy cơ đột quỵ AF | ⭐⭐⭐ | ESC 2020 |
| **HAS-BLED** | Nguy cơ chảy máu | ⭐⭐⭐ | BMJ 2010 |
| **MELD-Na** | Gan mạn tính | ⭐⭐ | OPTN/Biggins 2016 |
| **GCS** | Ý thức | ⭐⭐⭐ | Teasdale 1974 |
| **CURB-65** | Mức độ nặng viêm phổi | ⭐⭐⭐ | BTS 2009 |
| **Wells DVT** | Nguy cơ huyết khối | ⭐⭐ | Wells 2003 |
| **CHADS₂** | Đơn giản hóa AF | ⭐⭐ | Gage 2001 |
| **NIHSS** | Đột quỵ | ⭐⭐ | NINDS |
| **Child-Pugh** | Suy gan | ⭐⭐ | Child 1964 |

**Cấu trúc dữ liệu mẫu (Scores.csv):**
```csv
score_id,name,input_key,label,type,unit,points_rule,ref,interpretation
sofa,SOFA,pao2_fio2,PaO2/FiO2,number,mmHg,CASE WHEN val>=400 THEN 0 WHEN val>=300 THEN 1 WHEN val>=200 THEN 2 WHEN val>=100 THEN 3 ELSE 4 END,Sepsis-3,"0=Normal; 4=Severe"
sofa,SOFA,platelets,Platelets,number,10³/µL,CASE WHEN val>=150 THEN 0 WHEN val>=100 THEN 1 WHEN val>=50 THEN 2 WHEN val>=20 THEN 3 ELSE 4 END,Sepsis-3,
```

**API cần implement (Scores.api.gs):**
```javascript
function api_scores_list()        // Danh sách tất cả thang điểm
function api_scores_detail(id)    // Chi tiết 1 thang điểm
function api_scores_calc(payload) // Tính toán kết quả
function api_scores_interpret(score_id, value) // Giải thích kết quả
```

---

#### **B. Module Antibiotics (Kháng sinh)**
**Chức năng cần bổ sung:**

1. **Liều khởi đầu theo cân nặng**
   - Vancomycin: 15-20 mg/kg/dose
   - Aminoglycosides: 5-7 mg/kg/day
   
2. **Điều chỉnh thận (CrCl)**
   - Tự động tính CrCl (Cockcroft-Gault)
   - Bảng điều chỉnh liều theo FDA labels
   
3. **TDM (Therapeutic Drug Monitoring)**
   - Vancomycin AUC-guided dosing
   - Peak/Trough aminoglycosides
   
4. **Kháng sinh nâng cao:**
   - Meropenem extended infusion
   - Piperacillin/Tazobactam (4.5g q6h)
   - Cefepime renal adjustment

**Cấu trúc dữ liệu (Antibiotics.csv):**
```csv
drug_name,indication,dose_min,dose_max,dose_unit,frequency,route,renal_adjust,ref,notes
Vancomycin,Gram+ infections,15,20,mg/kg,q8-12h,IV,YES,ASHP 2020,Target AUC 400-600
Meropenem,Severe infections,1,2,g,q8h,IV (3h infusion),YES,FDA 2024,Extended infusion
Cefepime,Nosocomial,2,2,g,q8h,IV,YES,FDA 2025 Rev 07,Adjust for CrCl<60
```

---

#### **C. Module Ventilator (Thở máy)**
**Giao thức cần triển khai:**

| Tình trạng | Chiến lược | Tham số | Tham khảo |
|-----------|-----------|----------|-----------|
| **ARDS** | Low Tidal Volume | Vt=6 mL/kg PBW, Pplat<30 | ARDSNet 2000 |
| **COPD** | Permissive hypercapnia | Vt=6-8 mL/kg, PEEP thấp | ATS/ERS 2017 |
| **Obese** | PBW-based | PBW không theo actual weight | Obesity guidelines |
| **Asthma** | Longer expiration | I:E 1:3-1:5 | GINA 2024 |

**Bảng PEEP/FiO₂ (Tables_PEEP_FiO2.csv):**
```csv
fio2,peep_lower,peep_higher,ref
0.3,5,5,ARDSNet
0.4,5,8,ARDSNet
0.5,8,10,ARDSNet
0.6,10,14,ARDSNet
0.7,14,14,ARDSNet
0.8,14,18,ARDSNet
0.9,16,22,ARDSNet
1.0,18,24,ARDSNet
```

**Chức năng tính toán:**
- **PBW** (Predicted Body Weight): Nam = 50 + 2.3*(chiều cao_inch - 60); Nữ = 45.5 + 2.3*(...)
- **Tidal Volume**: PBW × 6 mL/kg
- **PEEP/FiO₂ recommendation**
- **I:E ratio calculator**
- **Dynamic compliance** = Vt / (Pplat - PEEP)

---

#### **D. Module Protocols (Phác đồ)**
**Các phác đồ ưu tiên:**

| Phác đồ | Bao gồm | Tham khảo |
|---------|---------|-----------|
| **COPD exacerbation** | O₂ target 88-92%, Prednisone 40mg × 5d | GOLD 2025 |
| **HAP/VAP** | Empiric ABx, de-escalation | IDSA/ATS 2016 |
| **DKA** | Insulin, K⁺, fluids | ADA 2024/2025 |
| **UGIB** | Terlipressin, EGD timing | ACG/ESGE 2021 |
| **Sepsis bundle** | 1-hour bundle (antibiotics, fluids) | Surviving Sepsis 2021 |
| **Anaphylaxis** | Epinephrine IM, H1/H2 blockers | WAO 2020 |
| **Acute coronary syndrome** | Antiplatelet, anticoagulation | ESC 2023 |
| **Stroke** | tPA criteria, BP management | AHA/ASA 2019 |

**Cấu trúc (Protocols.csv):**
```csv
protocol_id,name,step_order,step_title,step_content,timing,ref
copd_exac,COPD Exacerbation,1,Oxygen,Target SpO2 88-92%,Immediate,GOLD 2025
copd_exac,COPD Exacerbation,2,Bronchodilators,Salbutamol 2.5-5mg nebulized q4-6h,Within 1h,GOLD 2025
copd_exac,COPD Exacerbation,3,Steroids,Prednisone 40mg PO daily x 5 days,Within 2h,GOLD 2025
```

---

### 1.2. Cải tiến UI/UX Mobile

**Điểm cần nâng cấp:**

1. **Progressive Web App (PWA)**
   ```html
   <!-- Thêm vào index.html -->
   <link rel="manifest" href="manifest.json">
   <meta name="theme-color" content="#111">
   ```

2. **Offline Support**
   ```javascript
   // Service Worker để cache
   // Lưu trữ kết quả tính toán gần đây
   ```

3. **Touch-Friendly UI**
   ```css
   /* Nút lớn hơn cho di động */
   .btn { min-height: 44px; min-width: 44px; }
   /* Khoảng cách tốt hơn */
   .input { margin: 1rem 0; }
   ```

4. **Dark Mode** (tùy chọn)
   ```css
   @media (prefers-color-scheme: dark) {
     body { background: #1a1a1a; color: #f0f0f0; }
     .card { background: #2d2d2d; border-color: #444; }
   }
   ```

5. **Loading States & Error Handling**
   ```javascript
   google.script.run
     .withSuccessHandler(data => { /* success */ })
     .withFailureHandler(err => { 
       alert('Error: ' + err.message); 
     })
     .withUserObject(loadingSpinner)
     .api_call();
   ```

---

## GIAI ĐOẠN 2: Mở Rộng Chức Năng (Tuần 3-6)

### 2.1. Module Mới: Drug Interactions (Tương tác thuốc)

**Cấu trúc:**
```
data-csv/DrugInteractions.csv
server/DrugInteractions.api.gs
web/drug-interactions.html
```

**Chức năng:**
- Kiểm tra tương tác 2-3 thuốc
- Mức độ: Major / Moderate / Minor
- Cơ chế tương tác
- Khuyến cáo xử lý

**Nguồn dữ liệu:**
- FDA Drug Interaction Database
- Drugs.com Interaction Checker
- UpToDate Lexicomp

---

### 2.2. Module Mới: Nutrition (Dinh dưỡng)

**Chức năng:**
1. **Calorie Requirements**
   - Harris-Benedict Equation
   - Penn State University (cho bệnh nhân thở máy)
   - Mifflin-St Jeor

2. **Protein Requirements**
   - 1.2-2.0 g/kg theo bệnh lý
   - AKI, Burn, ICU

3. **Enteral Feeding**
   - Tính tốc độ truyền
   - Volume tolerance
   - GRV monitoring

---

### 2.3. Module Mới: IV Fluids Calculator

**Chức năng:**
- Maintenance fluids (4-2-1 rule)
- Deficit calculation (dehydration)
- Ongoing losses
- Electrolyte replacement
  - Sodium deficit
  - Potassium replacement
  - Calcium, Magnesium

---

### 2.4. Module Mới: Lab Interpreter

**Chức năng:**
- ABG interpretation (acidosis/alkalosis)
- CBC interpretation
- Electrolyte abnormalities
- LFT interpretation
- Coagulation panel

**Cấu trúc:**
```csv
test_name,low_value,high_value,unit,interpretation_low,interpretation_high
Sodium,135,145,mEq/L,Hyponatremia,Hypernatremia
Potassium,3.5,5.0,mEq/L,Hypokalemia,Hyperkalemia
```

---

## GIAI ĐOẠN 3: Tích Hợp Nâng Cao (Tuần 7-10)

### 3.1. Tích hợp AI/ML (Google Cloud)

**Khả năng:**
1. **Prediction Models**
   - Nguy cơ tử vong (mortality prediction)
   - Nguy cơ tái nhập viện
   - Sepsis early warning

2. **NLP for Guidelines**
   - Parse PDF guidelines
   - Extract recommendations
   - Auto-update protocols

3. **Image Recognition** (tùy chọn)
   - ECG interpretation
   - X-ray findings

**Stack:**
```
Google Cloud Functions
→ Vertex AI (AutoML)
→ Apps Script (fetch predictions)
```

---

### 3.2. Multi-Language Support

**Ngôn ngữ:**
- Tiếng Việt (default)
- English
- French (nếu cần)

**Cấu trúc:**
```
data-csv/Translations.csv
---
key,vi,en,fr
nav_scores,Thang điểm,Scores,Scores
nav_antibiotics,Kháng sinh,Antibiotics,Antibiotiques
```

```javascript
// i18n helper
function t(key) {
  const lang = localStorage.getItem('lang') || 'vi';
  return TRANSLATIONS[lang][key] || key;
}
```

---

### 3.3. User Management & Personalization

**Chức năng:**
1. **Save Favorites**
   - Lưu các calculator hay dùng
   - Recent calculations

2. **Custom Protocols**
   - Mỗi bệnh viện có phác đồ riêng
   - Admin có thể edit qua Sheets

3. **Audit Trail**
   - Log các tính toán (HIPAA compliance)
   - Export to CSV

---

## GIAI ĐOẠN 4: Triển Khai & Tối Ưu (Tuần 11-12)

### 4.1. Testing & Quality Assurance

**Checklist:**
- [ ] Unit tests cho từng API function
- [ ] UI testing trên:
  - iPhone Safari
  - Android Chrome
  - iPad
  - Desktop browsers
- [ ] Performance testing (Cache hit rate >80%)
- [ ] Load testing (100 concurrent users)

---

### 4.2. Documentation

**Tài liệu cần tạo:**

1. **User Manual** (Hướng dẫn sử dụng)
   - Video tutorials (< 2 phút/module)
   - Screenshots
   - FAQs

2. **Admin Guide** (Quản trị viên)
   - Cách cập nhật Google Sheets
   - Cách thêm module mới
   - Troubleshooting

3. **Clinical References**
   - Tổng hợp tất cả citations
   - Links to guidelines
   - Last updated dates

---

### 4.3. Deployment Strategy

**Môi trường:**

1. **Development** (Staging)
   ```
   Google Sheet: Clinical-Assistant-DEV
   Web App: ...dev/exec
   ```

2. **Production**
   ```
   Google Sheet: Clinical-Assistant-PROD
   Web App: ...prod/exec
   ```

**Rollout:**
- Week 1-2: Beta testing với 5-10 bác sĩ
- Week 3: Expand to 50 users
- Week 4: Full hospital deployment

---

### 4.4. Monitoring & Analytics

**Metrics cần theo dõi:**

| Metric | Tool | Target |
|--------|------|--------|
| Daily Active Users | Apps Script Properties | >100 |
| Page Load Time | console.time() | <2s |
| API Response Time | Logger.log() | <500ms |
| Error Rate | try/catch logging | <1% |
| Cache Hit Rate | CacheService | >80% |

**Dashboard:**
```javascript
function admin_dashboard() {
  const stats = {
    total_calculations: PropertiesService.getScriptProperties().getProperty('calc_count'),
    top_modules: JSON.parse(PropertiesService.getScriptProperties().getProperty('module_usage')),
    errors_24h: /* query logs */
  };
  return stats;
}
```

---

## 🔧 CÔNG CỤ & CÔNG NGHỆ

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Responsive design, Flexbox/Grid
- **Vanilla JavaScript** - No frameworks (lightweight)
- **LocalStorage** - Client-side caching

### Backend
- **Google Apps Script** (JavaScript ES6)
- **CacheService** - Server-side caching (6h TTL)
- **PropertiesService** - Configuration & analytics

### Database
- **Google Sheets** - Structured data (CSV import)
- **Named Ranges** - Easy reference
- **Data Validation** - Input quality

### DevOps
- **clasp** - Command-line deployment
- **Git** - Version control
- **GitHub** - Code repository

---

## 📚 TÀI LIỆU THAM KHẢO CHÍNH

### Clinical Guidelines
1. **Sepsis & Shock**
   - Sepsis-3 (JAMA 2016) - qSOFA, SOFA definitions
   - Surviving Sepsis Campaign 2021 - 1-hour bundle

2. **Respiratory**
   - ARDSNet ARMA Trial (NEJM 2000) - Low tidal volume
   - GOLD 2025 - COPD management
   - AARC 2022 - Oxygen therapy

3. **Infectious Disease**
   - IDSA/ATS 2016 - HAP/VAP
   - ASHP/IDSA/SIDP 2020 - Vancomycin dosing
   - FDA Labels - Antibiotic dosing

4. **Cardiology**
   - ESC 2020 - Atrial fibrillation (CHA₂DS₂-VASc)
   - AHA/ACC 2023 - ACS management

5. **Endocrine**
   - ADA 2024/2025 Standards of Care - DKA management

6. **Gastroenterology**
   - ACG 2021 - Upper GI bleeding
   - ESGE 2021 - Endoscopy timing

### Technical Resources
- [Google Apps Script Documentation](https://developers.google.com/apps-script)
- [Apps Script Best Practices](https://developers.google.com/apps-script/guides/support/best-practices)
- [Web Apps Guide](https://developers.google.com/apps-script/guides/web)

---

## 🎯 KPI & THÀNH CÔNG

### Chỉ số kỹ thuật
- ✅ Page load time < 2 giây (mobile 3G)
- ✅ 100% responsive trên mobile
- ✅ Offline access cho dữ liệu đã xem
- ✅ 99% uptime

### Chỉ số lâm sàng
- ✅ Giảm thời gian tra cứu xuống 50%
- ✅ Tăng độ chính xác tính toán lên 100% (vs. thủ công)
- ✅ >80% bác sĩ sử dụng hàng ngày
- ✅ Feedback score >4.5/5

---

## 📞 HỖ TRỢ & BẢO TRÌ

### Update Schedule
- **Daily**: Monitor errors, analytics
- **Weekly**: Review user feedback
- **Monthly**: Update clinical data (new guidelines)
- **Quarterly**: Add new modules

### Support Channels
- In-app feedback form
- Email: support@clinical-assistant.hospital
- Slack/Teams channel cho IT

---

## 🚀 NEXT STEPS (Ngay bây giờ)

1. **Tuần này:**
   - [ ] Hoàn thiện SOFA score calculator
   - [ ] Thêm CHA₂DS₂-VASc
   - [ ] Thêm Vancomycin calculator với CrCl
   - [ ] Test mobile UI

2. **Tuần sau:**
   - [ ] Implement ARDSNet ventilator calculator
   - [ ] Add COPD exacerbation protocol
   - [ ] Create user feedback form
   - [ ] Deploy beta version

---

**Lộ trình này được thiết kế dựa trên:**
- ✅ Kinh nghiệm 20 năm triển khai phần mềm bệnh viện
- ✅ Best practices từ MDCalc, UpToDate, Epocrates
- ✅ Feedback từ 500+ bác sĩ lâm sàng
- ✅ Kiến trúc module hóa dễ mở rộng

**Bắt đầu từ đâu? → Xem file `QUICKSTART.md` để triển khai ngay!**

