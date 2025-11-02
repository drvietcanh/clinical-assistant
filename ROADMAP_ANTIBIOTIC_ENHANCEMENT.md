# 🗺️ LỘ TRÌNH CHI TIẾT: CẢI THIỆN TÍNH NĂNG KHÁNG SINH

**Ngày bắt đầu:** 2025-01-30  
**Mục tiêu:** Tích hợp tra cứu + tính liều nhiều trường hợp, bổ sung tính năng từ các app hàng đầu

---

## 📊 TỔNG QUAN LỘ TRÌNH

| Phase | Tên | Thời gian | Ưu tiên | Status |
|-------|-----|-----------|---------|--------|
| **Phase 1** | Multi-Scenario Calculator | 1-2 tuần | 🔴 P0 | ⏳ Chưa bắt đầu |
| **Phase 2** | Drug Interaction Checker | 1-2 tuần | 🔴 P0 | ⏳ Chưa bắt đầu |
| **Phase 3** | Visual Charts & Export | 1 tuần | 🟡 P1 | ⏳ Chưa bắt đầu |
| **Phase 4** | Integration & UX | 1 tuần | 🟡 P1 | ⏳ Chưa bắt đầu |
| **Phase 5** | Advanced Features | 2-3 tuần | 🟢 P2 | ⏳ Chưa bắt đầu |

---

## 🔴 PHASE 1: MULTI-SCENARIO CALCULATOR

**Mục tiêu:** Tạo calculator tính liều cho nhiều scenarios (CrCl khác nhau) trong 1 lần, tích hợp vào trang tra cứu

**Thời gian ước tính:** 1-2 tuần  
**Ưu tiên:** P0 (Critical)

### ✅ Task 1.1: Tạo Component `scenario_dosing_calculator.py`

**File:** `antibiotics/scenario_dosing_calculator.py`

**Chức năng:**
- Input: Thông số bệnh nhân (cân nặng, chiều cao, tuổi, giới tính)
- Input: Chọn scenarios (CrCl categories: Normal, Mild, Moderate, Severe)
- Input: Chọn chỉ định (Standard, Severe, Meningitis)
- Tính liều cho tất cả combinations
- Trả về DataFrame với kết quả

**Tasks:**
- [ ] Tạo file `scenario_dosing_calculator.py`
- [ ] Import các functions cần thiết từ `dosing_calculator.py`
- [ ] Viết function `calculate_scenarios()` nhận:
  - `antibiotic_name`
  - `weight`, `height`, `age`, `sex`
  - `scenarios_list` (list of CrCl values)
  - `indications_list` (list of indications)
- [ ] Return: List of dicts với kết quả
- [ ] Test với 1 kháng sinh

**Estimate:** 2-3 giờ

---

### ✅ Task 1.2: Tích Hợp Vào `database.py`

**File:** `antibiotics/database.py`

**Chức năng:**
- Trong `display_antibiotic_info()`, thêm expander "🧮 Tính Liều Cho Nhiều Trường Hợp"
- Gọi `render_scenario_dosing_calculator()` từ expander
- Pass `ab_name` vào function

**Tasks:**
- [ ] Import `render_scenario_dosing_calculator` trong `database.py`
- [ ] Thêm expander sau phần hiển thị thông tin kháng sinh
- [ ] Test với một vài kháng sinh khác nhau

**Estimate:** 1-2 giờ

---

### ✅ Task 1.3: Tạo UI Component cho Multi-Scenario

**File:** `antibiotics/scenario_dosing_calculator.py` (update)

**Chức năng:**
- Form nhập thông số bệnh nhân (columns layout)
- Checkboxes để chọn CrCl scenarios:
  - [x] CrCl ≥ 60 (Normal) - mặc định checked
  - [x] CrCl 30-59 (Mild) - mặc định checked
  - [x] CrCl 15-29 (Moderate) - mặc định checked
  - [x] CrCl < 15 (Severe) - mặc định checked
- Multiselect cho chỉ định
- Button "🧮 Tính Liều Cho Tất Cả Scenarios"

**Tasks:**
- [ ] Design form layout (columns)
- [ ] Input fields: weight, height, age, sex
- [ ] Checkboxes cho CrCl scenarios với giá trị mặc định
- [ ] Multiselect cho indications
- [ ] Button trigger calculation
- [ ] Test UI layout

**Estimate:** 2-3 giờ

---

### ✅ Task 1.4: Hiển Thị Kết Quả Dạng Bảng

**File:** `antibiotics/scenario_dosing_calculator.py` (update)

**Chức năng:**
- Hiển thị DataFrame với pandas
- Columns: Scenario, CrCl, Indication, Dose (mg), Interval (hours), Renal Adjustment
- Color coding rows (green/yellow/orange/red)
- Sortable columns

**Tasks:**
- [ ] Import pandas
- [ ] Tạo DataFrame từ kết quả calculations
- [ ] Format columns đẹp
- [ ] Thêm color coding dựa trên CrCl category
- [ ] Hiển thị bằng `st.dataframe()` với styling
- [ ] Test với nhiều scenarios

**Estimate:** 2-3 giờ

---

### ✅ Task 1.5: Bổ Sung Tính Năng Import CrCl/eGFR

**File:** `antibiotics/scenario_dosing_calculator.py` (update)

**Chức năng:**
- Checkbox "Sử dụng CrCl/eGFR đã tính từ eGFR Calculator"
- Nếu checked → Lấy từ `st.session_state['patient_crcl']`, `st.session_state['patient_egfr']`
- Tự động fill vào form hoặc thêm vào scenarios list

**Tasks:**
- [ ] Checkbox "Import từ eGFR Calculator"
- [ ] Kiểm tra session state
- [ ] Auto-fill hoặc highlight giá trị đã import
- [ ] Test integration với eGFR calculator

**Estimate:** 1 giờ

---

### ✅ Task 1.6: Testing & Bug Fixes

**Tasks:**
- [ ] Test với tất cả các kháng sinh trong database
- [ ] Test edge cases (giá trị biên)
- [ ] Test với nhiều scenarios (16 combinations)
- [ ] Fix bugs nếu có
- [ ] Optimize performance nếu chậm

**Estimate:** 2-3 giờ

---

**Tổng thời gian Phase 1:** ~10-15 giờ (1.5-2 ngày làm việc)

---

## 🔴 PHASE 2: DRUG INTERACTION CHECKER

**Mục tiêu:** Tạo hệ thống kiểm tra tương tác thuốc, đặc biệt cho phối hợp nhiều kháng sinh

**Thời gian ước tính:** 1-2 tuần  
**Ưu tiên:** P0 (Critical)

### ✅ Task 2.1: Tạo Database Tương Tác Thuốc

**File:** `antibiotics/drug_interactions.py` (new)

**Chức năng:**
- Dictionary chứa các tương tác phổ biến
- Format: `{("Drug1", "Drug2"): {"severity": "major/minor", "description": "...", "recommendation": "..."}}`
- Bao gồm:
  - Vancomycin + Aminoglycoside (nephrotoxicity)
  - Piperacillin-Tazobactam + Vancomycin (acute kidney injury)
  - Các tương tác phổ biến khác

**Tasks:**
- [ ] Tạo file `drug_interactions.py`
- [ ] Research và list các tương tác phổ biến
- [ ] Tạo dictionary structure
- [ ] Thêm ít nhất 10-15 tương tác phổ biến nhất
- [ ] Document sources

**Estimate:** 3-4 giờ

---

### ✅ Task 2.2: Tạo Function `check_interactions()`

**File:** `antibiotics/drug_interactions.py` (update)

**Chức năng:**
- Nhận list các kháng sinh đang dùng
- Check từng cặp (nC2 combinations)
- Return list các interactions found
- Sort theo severity (major trước)

**Tasks:**
- [ ] Function `check_interactions(drug_list)`
- [ ] Logic check từng cặp
- [ ] Return structured data (severity, description, recommendation)
- [ ] Handle case-insensitive matching
- [ ] Test với nhiều combinations

**Estimate:** 2-3 giờ

---

### ✅ Task 2.3: Tích Hợp Vào Multi-Comparison Page

**File:** `antibiotics/multi_dosing_comparison.py` (update)

**Chức năng:**
- Import `check_interactions` từ `drug_interactions.py`
- Sau khi user chọn nhiều kháng sinh, tự động check interactions
- Hiển thị cảnh báo với color coding:
  - 🔴 Major interactions (st.error)
  - 🟡 Minor interactions (st.warning)
  - ℹ️ Info interactions (st.info)

**Tasks:**
- [ ] Import function
- [ ] Gọi function khi user chọn kháng sinh
- [ ] Display warnings section
- [ ] Color coding theo severity
- [ ] Test với nhiều combinations

**Estimate:** 1-2 giờ

---

### ✅ Task 2.4: Tích Hợp Vào Dosing Calculator

**File:** `antibiotics/dosing_calculator.py` (update)

**Chức năng:**
- Input field "Thuốc khác đang dùng" (text input hoặc multiselect)
- Check interactions với kháng sinh đang tính liều
- Hiển thị warnings trong section "Cảnh Báo"

**Tasks:**
- [ ] Thêm input field cho "Other drugs"
- [ ] Import `check_interactions`
- [ ] Check khi calculate dose
- [ ] Display trong warnings section
- [ ] Test

**Estimate:** 1-2 giờ

---

### ✅ Task 2.5: Expand Database Interactions

**File:** `antibiotics/drug_interactions.py` (update)

**Chức năng:**
- Bổ sung thêm interactions từ research
- Thêm interactions với thuốc không phải kháng sinh:
  - Warfarin
  - Oral contraceptives
  - Methotrexate
  - v.v.

**Tasks:**
- [ ] Research thêm interactions
- [ ] Thêm vào database (ít nhất 30-40 interactions)
- [ ] Categorize (drug-drug, drug-food, etc.)
- [ ] Document sources

**Estimate:** 4-5 giờ

---

**Tổng thời gian Phase 2:** ~11-16 giờ (1.5-2 ngày làm việc)

---

## 🟡 PHASE 3: VISUAL CHARTS & EXPORT

**Mục tiêu:** Thêm biểu đồ trực quan và khả năng export/print

**Thời gian ước tính:** 1 tuần  
**Ưu tiên:** P1 (High)

### ✅ Task 3.1: Visual Dosing Chart (Bar Chart)

**File:** `antibiotics/scenario_dosing_calculator.py` (update)

**Chức năng:**
- Dùng `plotly` hoặc `matplotlib` để vẽ bar chart
- X-axis: Scenarios (Normal, Mild, Moderate, Severe)
- Y-axis: Dose (mg)
- Multiple bars cho các indications khác nhau
- Color coding theo CrCl category

**Tasks:**
- [ ] Install/check plotly dependency
- [ ] Create bar chart function
- [ ] Integrate vào scenario calculator
- [ ] Test với nhiều scenarios

**Estimate:** 2-3 giờ

---

### ✅ Task 3.2: Interval Comparison Chart

**File:** `antibiotics/scenario_dosing_calculator.py` (update)

**Chức năng:**
- Line chart hoặc bar chart cho dosing intervals
- Show frequency changes across scenarios
- Visual representation dễ hiểu

**Tasks:**
- [ ] Create interval chart
- [ ] Integrate
- [ ] Test

**Estimate:** 1-2 giờ

---

### ✅ Task 3.3: Export to CSV

**File:** `antibiotics/scenario_dosing_calculator.py` (update)

**Chức năng:**
- Button "📥 Export to CSV"
- Download DataFrame dưới dạng CSV
- Include patient info, scenarios, results

**Tasks:**
- [ ] Add export button
- [ ] Convert DataFrame to CSV
- [ ] Use `st.download_button()` để download
- [ ] Test download

**Estimate:** 1 giờ

---

### ✅ Task 3.4: Print-Friendly View

**File:** `antibiotics/scenario_dosing_calculator.py` (update)

**Chức năng:**
- Print-friendly CSS
- Hide sidebar, buttons khi print
- Format table đẹp cho print
- Include timestamp, patient info

**Tasks:**
- [ ] Add print CSS
- [ ] Create print view
- [ ] Test print preview

**Estimate:** 1-2 giờ

---

**Tổng thời gian Phase 3:** ~5-8 giờ (1 ngày làm việc)

---

## 🟡 PHASE 4: INTEGRATION & UX IMPROVEMENTS

**Mục tiêu:** Tích hợp tất cả tính năng và cải thiện UX

**Thời gian ước tính:** 1 tuần  
**Ưu tiên:** P1 (High)

### ✅ Task 4.1: Quick Access Recent Calculations

**File:** `antibiotics/database.py` (update)

**Chức năng:**
- Lưu recent calculations vào `st.session_state`
- Hiển thị trong sidebar
- Quick click để load lại

**Tasks:**
- [ ] Save calculations to session state
- [ ] Display recent list
- [ ] Quick access functionality
- [ ] Limit to 5-10 most recent

**Estimate:** 2 giờ

---

### ✅ Task 4.2: Favorite Antibiotics

**File:** `antibiotics/database.py` (update)

**Chức năng:**
- Star/Bookmark icon cho mỗi kháng sinh
- Lưu favorites vào session state
- Quick access từ sidebar hoặc dashboard

**Tasks:**
- [ ] Add favorite button
- [ ] Save to session state
- [ ] Display favorites section
- [ ] Quick access functionality

**Estimate:** 2 giờ

---

### ✅ Task 4.3: Smart Search Enhancement

**File:** `antibiotics/database.py` (update)

**Chức năng:**
- Filter theo nhóm kháng sinh
- Filter theo đường dùng
- Filter theo AWaRe classification
- Auto-complete suggestions

**Tasks:**
- [ ] Add filter UI (columns)
- [ ] Implement filter logic
- [ ] Auto-complete (optional)
- [ ] Test filtering

**Estimate:** 2-3 giờ

---

### ✅ Task 4.4: UI/UX Polish

**Tasks:**
- [ ] Color consistency
- [ ] Spacing improvements
- [ ] Mobile responsiveness check
- [ ] Loading states
- [ ] Error handling messages

**Estimate:** 2-3 giờ

---

**Tổng thời gian Phase 4:** ~8-10 giờ (1-1.5 ngày làm việc)

---

## 🟢 PHASE 5: ADVANCED FEATURES

**Mục tiêu:** Tính năng nâng cao (TDM, Pediatric, etc.)

**Thời gian ước tính:** 2-3 tuần  
**Ưu tiên:** P2 (Medium)

### ✅ Task 5.1: TDM Integration (Vancomycin)

**File:** `antibiotics/tdm_calculator.py` (new)

**Chức năng:**
- Tính liều dựa trên nồng độ máu Vancomycin
- Dự đoán nồng độ đạt được
- Điều chỉnh liều theo TDM results

**Tasks:**
- [ ] Research Vancomycin TDM protocols
- [ ] Create TDM calculator
- [ ] Integrate vào dosing calculator
- [ ] Test

**Estimate:** 4-5 giờ

---

### ✅ Task 5.2: Pediatric Dosing Templates

**File:** `antibiotics/dosing_calculator.py` (update)

**Chức năng:**
- Template sẵn cho pediatric
- Age-based adjustments
- Weight-based calculations tự động

**Tasks:**
- [ ] Add pediatric templates
- [ ] Age-based logic
- [ ] UI improvements
- [ ] Test với các độ tuổi khác nhau

**Estimate:** 3-4 giờ

---

### ✅ Task 5.3: IV Compatibility Checker

**File:** `antibiotics/iv_compatibility.py` (new)

**Chức năng:**
- Check tính tương thích khi pha chế IV
- Warning khi không tương thích

**Tasks:**
- [ ] Research IV compatibility data
- [ ] Create compatibility database
- [ ] Create checker function
- [ ] Integrate vào calculator

**Estimate:** 3-4 giờ

---

**Tổng thời gian Phase 5:** ~10-13 giờ (1.5-2 ngày làm việc)

---

## 📋 TỔNG KẾT

### Thời Gian Tổng Thể:
- **Phase 1:** 10-15 giờ (1.5-2 ngày)
- **Phase 2:** 11-16 giờ (1.5-2 ngày)
- **Phase 3:** 5-8 giờ (1 ngày)
- **Phase 4:** 8-10 giờ (1-1.5 ngày)
- **Phase 5:** 10-13 giờ (1.5-2 ngày)

**Tổng cộng:** ~44-62 giờ (~6-8 ngày làm việc)

### Kế Hoạch Thực Hiện:

**Tuần 1-2:**
- ✅ Phase 1: Multi-Scenario Calculator
- ✅ Phase 2: Drug Interaction Checker

**Tuần 3:**
- ✅ Phase 3: Visual Charts & Export
- ✅ Phase 4: Integration & UX

**Tuần 4-5 (Optional):**
- ✅ Phase 5: Advanced Features

---

## ✅ CHECKLIST TỔNG QUAN

### Phase 1: Multi-Scenario Calculator
- [ ] Task 1.1: Tạo Component
- [ ] Task 1.2: Tích hợp vào database.py
- [ ] Task 1.3: Tạo UI Component
- [ ] Task 1.4: Hiển thị kết quả bảng
- [ ] Task 1.5: Import CrCl/eGFR
- [ ] Task 1.6: Testing & Bug Fixes

### Phase 2: Drug Interaction Checker
- [ ] Task 2.1: Tạo Database
- [ ] Task 2.2: Tạo Function check_interactions()
- [ ] Task 2.3: Tích hợp Multi-Comparison
- [ ] Task 2.4: Tích hợp Dosing Calculator
- [ ] Task 2.5: Expand Database

### Phase 3: Visual Charts & Export
- [ ] Task 3.1: Bar Chart
- [ ] Task 3.2: Interval Chart
- [ ] Task 3.3: Export CSV
- [ ] Task 3.4: Print View

### Phase 4: Integration & UX
- [ ] Task 4.1: Recent Calculations
- [ ] Task 4.2: Favorite Antibiotics
- [ ] Task 4.3: Smart Search
- [ ] Task 4.4: UI/UX Polish

### Phase 5: Advanced Features
- [ ] Task 5.1: TDM Integration
- [ ] Task 5.2: Pediatric Templates
- [ ] Task 5.3: IV Compatibility

---

## 📝 NOTES

- **Commit sau mỗi phase:** Commit và push sau khi hoàn thành mỗi phase
- **Testing:** Test kỹ sau mỗi task
- **Documentation:** Update documentation khi thêm tính năng mới
- **Flexibility:** Có thể điều chỉnh thứ tự ưu tiên nếu cần

---

**Last Updated:** 2025-01-30  
**Status:** 📋 Ready to Start

