# 📊 Báo Cáo Các Module Dài và Phức Tạp

**Ngày:** 2025-01-30  
**Mục đích:** Phân tích độ phức tạp và độ dài của các module trong Clinical Assistant

---

## 🔍 Tổng Quan

Dựa trên phân tích codebase, các file sau được xác định là **dài và phức tạp nhất**:

---

## 🏆 TOP 5 FILE PHỨC TẠP NHẤT

### 1. 📄 `scores/emergency/apache2.py` - **614 dòng** ⚠️ PHỨC TẠP NHẤT

**Độ phức tạp:** 🔴🔴🔴🔴🔴 (5/5)

**Đặc điểm:**
- **12 helper functions** riêng biệt cho từng biến số APACHE II
- **Logic phức tạp:** Tính A-a gradient, xử lý nhiều điều kiện
- **Nhiều điều kiện nested:** Nhiều if/elif cho từng biến số
- **UI phức tạp:** Nhiều input fields, validation, unit conversion
- **Calculation logic:** Toán học phức tạp (logit function cho mortality)

**Các hàm chính:**
- `get_temp_score()` - 18 dòng
- `get_map_score()` - 14 dòng  
- `get_hr_score()` - 16 dòng
- `get_rr_score()` - 19 dòng
- `get_oxygenation_score()` - 24 dòng (logic phức tạp nhất)
- `get_ph_score()` - 16 dòng
- `get_na_score()` - 18 dòng
- `get_k_score()` - 16 dòng
- `get_cr_score()` - 16 dòng (có điều kiện nhân đôi)
- `get_hct_score()` - 14 dòng
- `get_wbc_score()` - 14 dòng
- `get_gcs_score()` - 3 dòng
- `get_age_score()` - 11 dòng
- `get_chronic_health_score()` - 13 dòng
- `calculate_apache2()` - 115 dòng (hàm tính toán chính)
- `render()` - 230 dòng (UI chính)

**Đề xuất tối ưu:**
- ✅ Code đã rất tốt, modular
- ⚠️ Có thể tách `render()` thành các sections nhỏ hơn
- ⚠️ Có thể tạo lookup tables thay vì nhiều if/elif

---

### 2. 📄 `app.py` - **530 dòng** ⚠️ RẤT PHỨC TẠP

**Độ phức tạp:** 🔴🔴🔴🔴🟡 (4.5/5)

**Đặc điểm:**
- **File chính của ứng dụng** - Entry point
- **Nhiều tính năng:** Search, Favorites, Recently Used, Stats
- **State management:** Quản lý nhiều session state variables
- **UI phức tạp:** Nhiều columns, containers, dynamic rendering
- **Large dictionary:** `ALL_CALCULATORS` với 37+ entries

**Các sections:**
- Session state initialization (8 dòng)
- Calculator registry (91 dòng) - **Dictionary lớn**
- Helper functions (25 dòng)
- Custom CSS (45 dòng)
- Header (12 dòng)
- Sidebar (23 dòng)
- Search functionality (47 dòng)
- Favorites system (29 dòng)
- Recently Used (31 dòng)
- Quick Access Modules (64 dòng)
- Stats & Updates (58 dòng)
- Tips & Footer (37 dòng)

**Đề xuất tối ưu:**
- ✅ Code tốt, organized
- ⚠️ Có thể tách `ALL_CALCULATORS` ra file riêng (`config.py`)
- ⚠️ Có thể tách Search/Favorites/Recently Used thành modules riêng
- ⚠️ Custom CSS có thể đưa vào file CSS riêng

---

### 3. 📄 `scores/respiratory/psi_port.py` - **476 dòng** ⚠️ PHỨC TẠP

**Độ phức tạp:** 🔴🔴🔴🔴🟡 (4/5)

**Đặc điểm:**
- **20+ input fields** - Nhiều biến số
- **Unit conversion logic:** BUN (mmol/L ↔ mg/dL), Glucose, PaO2 (mmHg ↔ kPa)
- **Phức tạp tính điểm:** Nhiều điều kiện, nested logic
- **Dynamic UI:** Conditional rendering dựa trên input
- **Risk stratification:** 5 risk classes với mortality rates

**Các sections:**
- Patient demographics (30 dòng)
- Comorbidities (25 dòng)
- Clinical symptoms (45 dòng)
- Lab values với unit conversion (120 dòng) - **Phức tạp nhất**
- Score calculation (75 dòng)
- Risk stratification (50 dòng)
- Treatment recommendations (45 dòng)
- References (35 dòng)

**Đề xuất tối ưu:**
- ⚠️ Unit conversion có thể tách thành helper functions riêng
- ⚠️ Calculation logic có thể tách ra function riêng
- ✅ UI tốt, dễ đọc

---

### 4. 📄 `labs/normal_ranges.py` - **472 dòng** ⚠️ DATA-HEAVY

**Độ phức tạp:** 🔴🔴🔴🟡🟡 (3/5) - Không phức tạp logic, nhưng **rất dài**

**Đặc điểm:**
- **100% data structure** - Không có logic phức tạp
- **8 dictionaries lớn:** CBC_RANGES, BMP_RANGES, LFT_RANGES, LIPID_RANGES, CARDIAC_RANGES, COAG_RANGES, THYROID_RANGES, ADDITIONAL_RANGES
- **Mỗi entry có nhiều fields:** name, unit, normal ranges, critical values, SI conversion
- **Helper functions:** Đơn giản, chỉ lookup và validation

**Cấu trúc:**
- CBC_RANGES - 69 dòng (9 tests)
- BMP_RANGES - 74 dòng (8 tests)
- LFT_RANGES - 56 dòng (7 tests)
- LIPID_RANGES - 47 dòng (4 tests)
- CARDIAC_RANGES - 36 dòng (5 tests)
- COAG_RANGES - 36 dòng (5 tests)
- THYROID_RANGES - 24 dòng (3 tests)
- ADDITIONAL_RANGES - 35 dòng (4 tests)
- ALL_RANGES merge - 9 dòng
- Helper functions - 60 dòng

**Đề xuất tối ưu:**
- ✅ Code rất clean và organized
- ⚠️ Có thể chuyển sang JSON/YAML file để dễ maintain
- ⚠️ Có thể tách thành nhiều files theo specialty
- ✅ Helper functions tốt

---

### 5. 📄 `antibiotics/vancomycin.py` - **286 dòng** ⚠️ PHỨC TẠP VỀ LOGIC

**Độ phức tạp:** 🔴🔴🔴🟡🟡 (3.5/5)

**Đặc điểm:**
- **Phức tạp về clinical logic:** Dosing rules dựa trên CrCl, indication, weight
- **Multiple calculations:** IBW, ABW, CrCl, loading dose, maintenance dose
- **Conditional logic:** Nhiều điều kiện cho different scenarios
- **TDM guidance:** Phức tạp về AUC monitoring

**Các sections:**
- Patient info & IBW/ABW calculation (50 dòng)
- Creatinine với unit conversion (25 dòng)
- CrCl calculation (10 dòng)
- Indication selection (15 dòng)
- Dosing calculation logic (60 dòng) - **Phức tạp nhất**
- TDM guidance (50 dòng)
- Safety notes (20 dòng)
- Infusion instructions (20 dòng)
- References (26 dòng)

**Đề xuất tối ưu:**
- ⚠️ Dosing logic có thể tách thành functions riêng
- ⚠️ TDM guidance có thể là module riêng
- ✅ Code tốt, clinical accurate

---

## 📊 SO SÁNH ĐỘ PHỨC TẠP

| File | Dòng Code | Số Functions | Độ Phức Tạp | Vấn Đề Chính |
|------|-----------|--------------|-------------|--------------|
| `apache2.py` | 614 | 17 | 🔴🔴🔴🔴🔴 | Nhiều helper functions, logic phức tạp |
| `app.py` | 530 | 4 | 🔴🔴🔴🔴🟡 | File chính, nhiều features, state management |
| `psi_port.py` | 476 | 1 | 🔴🔴🔴🔴🟡 | 20+ inputs, unit conversion, complex calculation |
| `normal_ranges.py` | 472 | 3 | 🔴🔴🔴🟡🟡 | Data-heavy, 8 large dictionaries |
| `vancomycin.py` | 286 | 1 | 🔴🔴🔴🟡🟡 | Complex dosing logic, multiple calculations |

---

## 🔧 ĐỀ XUẤT TỐI ƯU HÓA

### **Priority 1 - Tách File Lớn:**

1. **`app.py`** → Tách thành:
   - `app.py` (main entry - 100 dòng)
   - `config/calculators.py` (ALL_CALCULATORS - 50 dòng)
   - `components/search.py` (search functionality - 50 dòng)
   - `components/favorites.py` (favorites system - 40 dòng)
   - `components/recently_used.py` (recently used - 40 dòng)
   - `components/stats.py` (stats & updates - 60 dòng)
   - `static/styles.css` (CSS - 50 dòng)

2. **`normal_ranges.py`** → Tách thành:
   - `labs/data/cbc_ranges.py`
   - `labs/data/bmp_ranges.py`
   - `labs/data/lft_ranges.py`
   - `labs/data/lipid_ranges.py`
   - `labs/data/cardiac_ranges.py`
   - `labs/data/coag_ranges.py`
   - `labs/data/thyroid_ranges.py`
   - `labs/normal_ranges.py` (combine & helpers)

### **Priority 2 - Tối Ưu Logic:**

3. **`apache2.py`**:
   - Tạo lookup tables cho scoring ranges
   - Tách `render()` thành sections nhỏ hơn

4. **`psi_port.py`**:
   - Tạo unit conversion helper module (`utils/converter.py`)
   - Tách calculation logic ra function riêng

5. **`vancomycin.py`**:
   - Tách dosing calculation thành `dosing_calculator.py`
   - Tách TDM guidance thành `tdm_guide.py`

---

## ✅ CÁC FILE ĐÃ TỐT (KHÔNG CẦN TỐI ƯU)

- `pages/01_📊_Scores.py` - Router đơn giản (185 dòng)
- `pages/02_💊_Antibiotics.py` - Router đơn giản (75 dòng)
- `pages/04_📋_Protocols.py` - Router đơn giản (115 dòng)
- `pages/05_🔬_Labs.py` - Router đơn giản (123 dòng)
- `scores/cardiology/__init__.py` - Router đơn giản (64 dòng)
- `scores/config.py` - Config file rõ ràng (165 dòng)

---

## 📈 METRICS TỔNG QUAN

**Tổng số file Python:** ~156 files  
**Average lines/file:** ~150 dòng  
**Files >300 dòng:** 5 files (3.2%)  
**Files >400 dòng:** 4 files (2.6%)  
**Files >500 dòng:** 2 files (1.3%)  
**Files >600 dòng:** 1 file (0.6%)

**Kết luận:** Codebase **rất tốt**, chỉ có vài file lớn cần tối ưu.

---

## 🎯 KHUYẾN NGHỊ

### **Ngắn hạn (1-2 tuần):**
1. Tách `app.py` thành modules nhỏ hơn
2. Chuyển `normal_ranges.py` data sang JSON/YAML

### **Trung hạn (1 tháng):**
3. Tối ưu `apache2.py` với lookup tables
4. Tạo unit conversion helper module

### **Dài hạn (2-3 tháng):**
5. Refactor complex calculations thành reusable functions
6. Tạo testing suite cho các file phức tạp

---

**Báo cáo này giúp định hướng refactoring và maintenance roadmap.**

