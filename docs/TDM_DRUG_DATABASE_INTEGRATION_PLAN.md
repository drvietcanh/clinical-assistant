# 📊 KẾ HOẠCH TÍCH HỢP TDM VÀO DRUG DATABASE

**Ngày:** 2025-02-03  
**Mục tiêu:** Phân tích và đề xuất cách tích hợp thông tin TDM vào trang Drug Database  
**Dựa trên:** Nghiên cứu các app y học phổ biến (Epocrates, Micromedex, Medscape, UpToDate, Drugs.com)

---

## 🔍 PHÂN TÍCH CÁC APP Y HỌC PHỔ BIẾN

### **1. Epocrates ⭐⭐⭐⭐⭐**

**Giao diện:**
- Drug monograph có tabs: Overview, Dosing, Safety, Interactions, Pricing
- **TDM section** nằm trong tab "Dosing" hoặc "Safety"
- Hiển thị: Therapeutic range, Sampling time, Clinical significance
- Link đến TDM calculator (nếu có)

**Tính năng:**
- ✅ TDM info tích hợp trong drug detail
- ✅ Quick reference: Therapeutic range ngay trong overview
- ✅ Link đến tools/calculators
- ✅ Color-coded warnings (subtherapeutic, therapeutic, toxic)

---

### **2. Micromedex ⭐⭐⭐⭐⭐**

**Giao diện:**
- Drug monograph rất chi tiết
- **TDM section** là một phần riêng trong "Dosing & Administration"
- Hiển thị: Target ranges, Timing, Interpretation guide
- Có link đến TDM calculator tools

**Tính năng:**
- ✅ TDM là standard section trong drug monograph
- ✅ Detailed interpretation guidelines
- ✅ Integration với dosing calculators
- ✅ Clinical pearls và warnings

---

### **3. Medscape ⭐⭐⭐⭐**

**Giao diện:**
- Drug reference với sections: Overview, Dosing, Interactions, Monitoring
- **TDM info** trong section "Monitoring"
- Hiển thị: Therapeutic levels, Toxic levels, Monitoring parameters

**Tính năng:**
- ✅ TDM trong monitoring section
- ✅ Quick access từ drug detail
- ✅ Link đến related tools

---

### **4. UpToDate ⭐⭐⭐⭐**

**Giao diện:**
- Clinical topic format (không phải drug monograph)
- TDM info trong "Dosing and administration" section
- Reference đến TDM guidelines

**Tính năng:**
- ✅ TDM info trong dosing section
- ✅ Evidence-based recommendations
- ✅ Clinical context

---

### **5. Drugs.com ⭐⭐⭐**

**Giao diện:**
- Drug information với tabs
- TDM info trong "Professional" tab
- Hiển thị: Therapeutic range, Monitoring recommendations

**Tính năng:**
- ✅ TDM info có sẵn
- ✅ User-friendly interface

---

## 📋 KẾT LUẬN TỪ NGHIÊN CỨU

### **Xu hướng chung:**

1. **✅ TDM Info trong Drug Detail:**
   - Tất cả app đều có TDM info trong drug monograph/detail
   - Thường nằm trong section "Dosing", "Monitoring", hoặc "Safety"
   - Hiển thị: Therapeutic range, Sampling time, Interpretation

2. **✅ TDM Calculator riêng:**
   - Calculator tools thường là separate tools/modules
   - Link từ drug detail đến calculator
   - Calculator có tính năng phức tạp (tính toán, dose adjustment)

3. **✅ Integration Pattern:**
   - **Info** (therapeutic range, timing) → Trong drug detail
   - **Calculator** (dose adjustment, interpretation) → Separate module/tool
   - **Link** từ drug detail đến calculator

---

## 🎯 ĐỀ XUẤT CHO ỨNG DỤNG HIỆN TẠI

### **Hiện trạng:**

✅ **Đã có:**
- Module TDM riêng (`pages/08_📊_TDM.py`) - ✅ ĐÚNG
- TDM calculators đầy đủ (Digoxin, Phenytoin, Lithium, Theophylline, Tacrolimus/Cyclosporine, Vancomycin, Aminoglycosides, Carbamazepine, Valproic Acid)
- TDM config (`drugs/tdm/tdm_config.py`) với đầy đủ thông tin
- Drug Database với drug detail page (`drugs/drug_info.py`)
- Section "Monitoring" trong drug detail (dòng 237-242)

❌ **Thiếu:**
- TDM info section trong drug detail (cho các thuốc có TDM)
- Link từ drug detail đến TDM calculator
- Mapping giữa drug database và TDM config
- Hiển thị therapeutic range trong drug detail

---

## 💡 KẾ HOẠCH TÍCH HỢP

### **Phương án: Hybrid Approach** ⭐⭐⭐⭐⭐

**Giữ nguyên:**
- ✅ TDM Calculator module riêng (`pages/08_📊_TDM.py`)
- ✅ TDM calculators đầy đủ tính năng

**Thêm mới:**
- ✅ TDM Info section trong drug detail (cho thuốc có TDM)
- ✅ Link đến TDM calculator từ drug detail
- ✅ Mapping function giữa drug database và TDM config

---

## 📝 IMPLEMENTATION PLAN

### **Bước 1: Tạo TDM Mapping Function**

**File:** `drugs/drug_utils/tdm_mapping.py` (mới)

```python
"""
TDM Mapping Utilities
Map drug names from database to TDM config
"""

from drugs.tdm.tdm_config import TDM_DRUGS

# Mapping từ drug database names → TDM config keys
DRUG_TO_TDM_MAP = {
    # Exact matches
    "Digoxin": "digoxin",
    "Phenytoin": "phenytoin",
    "Lithium": "lithium",
    "Theophylline": "theophylline",
    "Tacrolimus": "tacrolimus",
    "Cyclosporine": "cyclosporine",
    "Vancomycin": "vancomycin",
    "Carbamazepine": "carbamazepine",
    "Valproic Acid": "valproic_acid",
    "Valproate": "valproic_acid",
    
    # Aminoglycosides
    "Amikacin": "amikacin",
    "Gentamicin": "gentamicin",
    "Tobramycin": "tobramycin",
    "Netilmicin": "netilmicin",
    
    # Case-insensitive matching
    # ... more mappings
}

def get_tdm_info(drug_name: str) -> dict:
    """
    Get TDM info for a drug
    Returns None if drug doesn't have TDM
    """
    # Try exact match
    drug_lower = drug_name.lower().strip()
    
    # Check direct mapping
    if drug_name in DRUG_TO_TDM_MAP:
        tdm_key = DRUG_TO_TDM_MAP[drug_name]
        if tdm_key in TDM_DRUGS:
            return TDM_DRUGS[tdm_key]
    
    # Try case-insensitive match in TDM_DRUGS
    for tdm_key, tdm_info in TDM_DRUGS.items():
        if tdm_info['name'].lower() == drug_lower:
            return tdm_info
    
    # Try partial match
    for tdm_key, tdm_info in TDM_DRUGS.items():
        if drug_lower in tdm_info['name'].lower() or tdm_info['name'].lower() in drug_lower:
            return tdm_info
    
    return None

def has_tdm(drug_name: str) -> bool:
    """Check if drug has TDM"""
    return get_tdm_info(drug_name) is not None
```

---

### **Bước 2: Thêm TDM Section vào Drug Detail**

**File:** `drugs/drug_info.py`

**Vị trí:** Sau section "Monitoring" (dòng 242), trước section "Precautions"

**Code:**

```python
# TDM Section (nếu thuốc có TDM)
from drugs.drug_utils.tdm_mapping import get_tdm_info, has_tdm

if has_tdm(drug_name):
    tdm_info = get_tdm_info(drug_name)
    
    st.markdown("---")
    st.markdown("### 📊 Theo Dõi Nồng Độ Thuốc (TDM)")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.info(f"""
        **Khoảng điều trị:** {tdm_info['therapeutic_range']}
        
        **Thời điểm lấy mẫu:** {tdm_info['sampling_time']}
        
        **Half-life:** {tdm_info.get('half_life_hours', 'N/A')} giờ
        
        **Đơn vị:** {tdm_info['unit']}
        """)
    
    with col2:
        # Button to open TDM calculator
        safe_tdm_key = f"tdm_calc_{str(drug_name).replace(' ', '_').replace('-', '_').replace('/', '_')}"
        if st.button("📊 Mở TDM Calculator", key=safe_tdm_key, use_container_width=True, type="primary"):
            # Set session state to switch to TDM module with preset
            st.session_state['preset_tdm_drug'] = drug_name
            st.session_state['switch_to_tdm'] = True
            st.rerun()
    
    st.caption("💡 Click nút trên để mở TDM calculator với thuốc này đã được chọn sẵn")
```

---

### **Bước 3: Cập nhật TDM Module để nhận preset**

**File:** `pages/08_📊_TDM.py`

**Thêm vào đầu sidebar:**

```python
# Check if should switch to TDM from drug detail view
if st.session_state.get('switch_to_tdm', False):
    st.session_state['switch_to_tdm'] = False
    preset_drug = st.session_state.get('preset_tdm_drug', None)
    if preset_drug:
        # Auto-select drug in dropdown
        # Find matching option
        for option in all_options:
            if preset_drug.lower() in option.lower():
                st.session_state['tdm_drug_selector'] = option
                break
        # Clear preset
        if 'preset_tdm_drug' in st.session_state:
            del st.session_state['preset_tdm_drug']
```

---

### **Bước 4: Thêm TDM Info vào Drug Database (nếu chưa có)**

**File:** `drugs/drug_modules/` (các file drug modules)

**Thêm field `tdm_info` vào các thuốc có TDM:**

```python
"Digoxin": {
    # ... existing fields ...
    "tdm_info": {
        "has_tdm": True,
        "therapeutic_range": "0.5-0.9 ng/mL (HF), 0.5-1.0 ng/mL (AF)",
        "sampling_time": "Trough (≥ 6-8 hours post-dose)",
        "unit": "ng/mL"
    }
}
```

**Hoặc:** Sử dụng mapping function (không cần thêm field, tự động detect từ TDM config)

---

## 🎨 UI/UX DESIGN

### **TDM Section trong Drug Detail:**

```
┌─────────────────────────────────────────┐
│ 📊 Theo Dõi Nồng Độ Thuốc (TDM)        │
├─────────────────────────────────────────┤
│                                         │
│  Khoảng điều trị: 0.5-0.9 ng/mL        │
│  Thời điểm lấy mẫu: Trough (≥ 6-8h)    │
│  Half-life: 36 giờ                      │
│  Đơn vị: ng/mL                          │
│                                         │
│  [📊 Mở TDM Calculator]                 │
│                                         │
└─────────────────────────────────────────┘
```

### **Color Coding:**
- **Therapeutic range:** Green badge
- **Toxic threshold:** Red warning
- **Button:** Primary color (blue)

---

## ✅ CHECKLIST IMPLEMENTATION

### **Phase 1: Core Integration**
- [ ] Tạo `drugs/drug_utils/tdm_mapping.py`
- [ ] Thêm TDM section vào `drugs/drug_info.py`
- [ ] Test với các thuốc có TDM (Digoxin, Phenytoin, Lithium, Theophylline, Tacrolimus/Cyclosporine)

### **Phase 2: Enhanced Features**
- [ ] Cập nhật TDM module để nhận preset từ drug detail
- [ ] Thêm TDM info cho tất cả thuốc trong TDM config
- [ ] Test navigation flow: Drug Detail → TDM Calculator

### **Phase 3: UI/UX Polish**
- [ ] Color coding cho therapeutic ranges
- [ ] Icons và visual indicators
- [ ] Tooltips và help text

---

## 📊 SO SÁNH CÁC PHƯƠNG ÁN

| Tiêu chí | Phương án 1<br/>(Tách hoàn toàn) | Phương án 2<br/>(Tích hợp đầy đủ) | Phương án 3<br/>(Hybrid) ⭐ |
|----------|----------------------------------|----------------------------------|----------------------------|
| **TDM Calculator** | Module riêng ✅ | Trong Drug DB ❌ | Module riêng ✅ |
| **TDM Info** | Không có ❌ | Trong Drug DB ✅ | Trong Drug DB ✅ |
| **Link Integration** | Không có ❌ | Có ✅ | Có ✅ |
| **User Experience** | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Architecture** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Maintainability** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Tổng điểm** | **⭐⭐⭐** | **⭐⭐⭐⭐** | **⭐⭐⭐⭐⭐** |

---

## 🎯 KẾT LUẬN

### **Đề xuất: Phương án 3 - Hybrid Approach** ⭐⭐⭐⭐⭐

**Lý do:**

1. **✅ Best of both worlds:**
   - TDM Calculator giữ module riêng (phù hợp với tính năng phức tạp)
   - TDM Info tích hợp vào drug detail (theo chuẩn các app y học)

2. **✅ User Experience:**
   - Người dùng tra cứu thuốc → Thấy TDM info ngay
   - Click button → Mở TDM calculator với thuốc đã chọn
   - Workflow tự nhiên, giống Epocrates/Micromedex

3. **✅ Architecture:**
   - Separation of concerns: Info vs Calculator
   - Reusable mapping function
   - Dễ maintain và mở rộng

4. **✅ Consistency:**
   - Giống pattern hiện tại (Dosing Calculator link từ drug detail)
   - Consistent với các app y học phổ biến

---

## 📝 NEXT STEPS

1. **Review và approve** kế hoạch này
2. **Implement Phase 1** (Core Integration)
3. **Test** với các thuốc có TDM
4. **Gather feedback** từ người dùng
5. **Iterate** và cải thiện

---

**Người phân tích:** AI Code Review Assistant  
**Ngày:** 2025-02-03  
**Status:** ✅ Ready for Implementation

