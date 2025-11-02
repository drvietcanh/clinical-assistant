# 💡 Đề Xuất Tích Hợp: Tra Cứu Kháng Sinh + Tính Liều Nhiều Trường Hợp

## 🎯 Mục Tiêu
Tạo workflow liền mạch: **Tra cứu kháng sinh → Tính liều cho nhiều trường hợp sử dụng**

## 📊 Phân Tích Hiện Trạng

### Workflow Hiện Tại:
1. **Tra Cứu** (database.py):
   - Tìm kháng sinh
   - Xem thông tin chi tiết
   - Quick calculator (chỉ khi có CrCl từ session state)
   - Link đến universal calculator

2. **Tính Liều** (dosing_calculator.py):
   - Nhập thông số bệnh nhân
   - Chọn kháng sinh
   - Tính liều cho 1 trường hợp

3. **So Sánh** (multi_dosing_comparison.py):
   - So sánh nhiều kháng sinh
   - Tính liều cho cùng 1 bệnh nhân

### Vấn Đề:
- ❌ Phải chuyển qua lại giữa các trang
- ❌ Không thể tính liều cho nhiều scenarios cùng lúc
- ❌ Quick calculator quá đơn giản

---

## 🚀 Phương Án Đề Xuất

### **Phương Án 1: Enhanced Quick Calculator trong Tra Cứu** ⭐ (Khuyến nghị)

**Ưu điểm:**
- Workflow liền mạch (không cần chuyển trang)
- Tính liều ngay khi tra cứu
- Hỗ trợ nhiều scenarios

**Cách thực hiện:**

1. **Trong trang Tra Cứu (database.py):**
   - Khi chọn/xem kháng sinh → Hiện expander "🧮 Tính Liều Cho Nhiều Trường Hợp"
   - Trong expander:
     - Form nhập thông số bệnh nhân cơ bản (tuổi, cân nặng, chiều cao, giới tính)
     - Form nhập CrCl (có thể nhập nhiều giá trị: 90, 60, 30, 15)
     - Chọn chỉ định (standard, severe, meningitis)
     - Button "Tính liều cho tất cả scenarios"
     - Hiển thị bảng so sánh kết quả

2. **Tính năng:**
   - Tính liều cho nhiều CrCl (normal, 30-60, 15-30, <15)
   - Tính liều cho nhiều chỉ định
   - Bảng so sánh với color coding
   - Export kết quả

**Workflow:**
```
Tra cứu "Ceftriaxone" 
  ↓
Xem thông tin chi tiết
  ↓
Mở "Tính Liều Cho Nhiều Trường Hợp"
  ↓
Nhập: 70kg, 170cm, Nam, CrCl = [90, 50, 25, 10]
  ↓
Tính liều cho 4 scenarios
  ↓
Bảng so sánh kết quả
```

---

### **Phương Án 2: Tích Hợp Session State**

**Cách thực hiện:**
- Từ tra cứu → Button "Tính liều chi tiết"
- Set `st.session_state['selected_antibiotic']` = kháng sinh đã chọn
- Redirect sang trang "Tính Liều" với kháng sinh đã pre-selected
- Trong calculator, cho phép chọn "Nhiều scenarios"

**Workflow:**
```
Tra cứu → Chọn kháng sinh
  ↓
Click "Tính liều chi tiết"
  ↓
Chuyển sang calculator (kháng sinh đã chọn)
  ↓
Mode "Nhiều scenarios"
  ↓
Nhập nhiều CrCl/chỉ định
  ↓
Bảng so sánh
```

---

### **Phương Án 3: Tab-Based Integration** (Phức tạp hơn)

**Cách thực hiện:**
- Trong trang Antibiotics, dùng tabs:
  - Tab 1: Tra Cứu
  - Tab 2: Tính Liều (single scenario)
  - Tab 3: Tính Liều (multi scenarios)
  - Tab 4: So Sánh Nhiều Kháng Sinh

- Từ Tab 1 → Click kháng sinh → Auto fill vào Tab 2/3

---

## ✅ Đề Xuất Chi Tiết - Phương Án 1

### **Component Mới: `scenario_dosing_calculator()`**

```python
def render_scenario_dosing_calculator(antibiotic_name):
    """
    Tính liều cho nhiều scenarios (CrCl, chỉ định)
    """
    st.markdown("### 🧮 Tính Liều Cho Nhiều Trường Hợp")
    
    # Input: Thông số bệnh nhân
    col1, col2 = st.columns(2)
    with col1:
        weight = st.number_input("Cân nặng (kg)", ...)
        height = st.number_input("Chiều cao (cm)", ...)
    
    with col2:
        age = st.number_input("Tuổi", ...)
        sex = st.radio("Giới tính", ...)
    
    # Scenarios
    st.markdown("#### 📋 Chọn Scenarios:")
    
    # CrCl scenarios (checkboxes)
    crcl_scenarios = []
    if st.checkbox("CrCl ≥ 60 (Normal)", True):
        crcl_scenarios.append(("Normal", 90))
    if st.checkbox("CrCl 30-59 (Mild)", True):
        crcl_scenarios.append(("30-59", 45))
    if st.checkbox("CrCl 15-29 (Moderate)", True):
        crcl_scenarios.append(("15-29", 22))
    if st.checkbox("CrCl < 15 (Severe)", True):
        crcl_scenarios.append(("< 15", 10))
    
    # Indications
    indications = st.multiselect(
        "Chỉ định:",
        ["Standard", "Severe", "Meningitis"],
        default=["Standard"]
    )
    
    # Calculate button
    if st.button("🧮 Tính Liều Cho Tất Cả Scenarios"):
        results = []
        for crcl_name, crcl_value in crcl_scenarios:
            for indication in indications:
                # Calculate dose
                detailed = calculate_detailed_dose(...)
                results.append({
                    'crcl_category': crcl_name,
                    'crcl_value': crcl_value,
                    'indication': indication,
                    'dose': detailed['calculated_dose_mg'],
                    'interval': detailed['interval_hours'],
                    ...
                })
        
        # Display comparison table
        df = pd.DataFrame(results)
        st.dataframe(df, use_container_width=True)
        
        # Visual comparison
        st.markdown("#### 📊 So Sánh Trực Quan:")
        # Charts, color coding, etc.
```

### **Tích Hợp Vào database.py:**

```python
# Trong display_antibiotic_info() hoặc sau khi hiển thị info
with st.expander("🧮 Tính Liều Cho Nhiều Trường Hợp", expanded=False):
    render_scenario_dosing_calculator(ab_name)
```

---

## 🎨 UI/UX Improvements

1. **Color Coding:**
   - Normal CrCl: 🟢 Green
   - Mild: 🟡 Yellow
   - Moderate: 🟠 Orange
   - Severe: 🔴 Red

2. **Comparison Table:**
   - Sortable columns
   - Highlight recommended dose
   - Warning badges

3. **Export Options:**
   - Copy to clipboard
   - Download CSV
   - Print-friendly view

---

## 📝 Implementation Plan

### Phase 1: Core Functionality
1. ✅ Tạo `render_scenario_dosing_calculator()`
2. ✅ Tích hợp vào `display_antibiotic_info()`
3. ✅ Support multiple CrCl scenarios
4. ✅ Basic comparison table

### Phase 2: Enhancements
1. ⏳ Support multiple indications
2. ⏳ Visual charts (bar chart cho liều, line chart cho intervals)
3. ⏳ Export functionality
4. ⏳ Save scenarios to session state

### Phase 3: Advanced Features
1. ⏳ Compare multiple antibiotics side-by-side
2. ⏳ ICU adjustments integration
3. ⏳ Pediatric dosing scenarios

---

## 🤔 Lựa Chọn

**Phương Án 1** được khuyến nghị vì:
- ✅ Workflow tự nhiên nhất
- ✅ Không cần chuyển trang
- ✅ Dễ implement
- ✅ Đáp ứng đúng nhu cầu user

**Bước tiếp theo:** Implement Phương Án 1?

