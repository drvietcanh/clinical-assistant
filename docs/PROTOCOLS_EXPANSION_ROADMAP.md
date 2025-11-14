# 📋 Lộ Trình Bổ Sung Protocols Mới - Từng Bước

**Mục tiêu:** Tìm, nghiên cứu và bổ sung các protocols điều trị mới cập nhật vào hệ thống  
**Ngày tạo:** 2025-02-04  
**Trạng thái:** 🔄 Đang tiến hành

---

## 📊 TỔNG QUAN PROTOCOLS HIỆN CÓ

### ✅ **Đã Có (11 protocols):**

#### 🚨 Emergency (6):
- ✅ Sepsis 1-Hour Bundle
- ✅ Shock Management
- ✅ Stroke Management (AHA/ASA 2021)
- ✅ GI Bleeding (Upper & Lower)
- ✅ DKA Protocol
- ✅ Electrolyte Emergency (Hyperkalemia & Hyponatremia)

#### 🫁 Respiratory (2):
- ✅ COPD Exacerbation
- ✅ Asthma Acute Attack

#### ❤️ Cardiology (2):
- ✅ ACS Management
- ✅ Heart Failure Acute

#### 🧪 Nephrology (1):
- ✅ AKI Management (KDIGO)

---

## 🎯 PROTOCOLS CẦN BỔ SUNG (Ưu Tiên)

### **PRIORITY 1: Emergency & Critical Care** 🔥🔥🔥

#### 1. **Sepsis 3-Hour Bundle** (Mở rộng từ 1-hour)
- **Guideline:** Surviving Sepsis Campaign 2021
- **File:** `protocols/emergency/sepsis_3hour.py`
- **Nội dung:**
  - 3-hour bundle checklist
  - Antibiotic selection guide
  - Source control
  - Vasopressor initiation
- **Thời gian:** 2-3 giờ

#### 2. **CAP Management** (Community Acquired Pneumonia)
- **Guideline:** IDSA/ATS 2019
- **File:** `protocols/infectious/cap.py`
- **Nội dung:**
  - CURB-65 integration
  - Outpatient vs Inpatient decision
  - Antibiotic selection (local resistance)
  - Duration of therapy
- **Thời gian:** 3-4 giờ

#### 3. **HAP/VAP Guidelines** (Hospital-Acquired Pneumonia)
- **Guideline:** IDSA/ATS 2016
- **File:** `protocols/infectious/hap_vap.py`
- **Nội dung:**
  - Risk stratification (MDR risk)
  - Empiric antibiotic selection
  - De-escalation strategy
  - Duration (7-8 days)
- **Thời gian:** 3-4 giờ

#### 4. **C. diff Treatment**
- **Guideline:** IDSA/SHEA 2021
- **File:** `protocols/infectious/cdiff.py`
- **Nội dung:**
  - Initial episode treatment
  - Recurrent C. diff management
  - Severe/complicated C. diff
  - FMT indications
- **Thời gian:** 2-3 giờ

---

### **PRIORITY 2: Endocrine Emergencies** 🔥🔥

#### 5. **Thyrotoxic Crisis**
- **Guideline:** ATA 2016
- **File:** `protocols/endocrinology/thyrotoxic_crisis.py`
- **Nội dung:**
  - Diagnostic criteria
  - Beta-blocker (propranolol)
  - Antithyroid drugs (PTU/Methimazole)
  - Iodine therapy
  - Corticosteroids
- **Thời gian:** 2-3 giờ

#### 6. **Myxedema Coma**
- **Guideline:** ATA 2014
- **File:** `protocols/endocrinology/myxedema_coma.py`
- **Nội dung:**
  - Diagnostic criteria
  - Levothyroxine loading
  - Hydrocortisone (adrenal insufficiency)
  - Supportive care
- **Thời gian:** 2 giờ

#### 7. **Adrenal Crisis**
- **Guideline:** Endocrine Society 2016
- **File:** `protocols/endocrinology/adrenal_crisis.py`
- **Nội dung:**
  - Recognition & diagnosis
  - Hydrocortisone dosing
  - Fluid resuscitation
  - Maintenance therapy
- **Thời gian:** 2 giờ

---

### **PRIORITY 3: Electrolyte Protocols (Mở Rộng)** 🔥

#### 8. **Hypomagnesemia Correction**
- **Guideline:** Various
- **File:** `protocols/emergency/electrolytes.py` (mở rộng)
- **Nội dung:**
  - Oral vs IV replacement
  - Dosing calculator
  - Monitoring
- **Thời gian:** 1-2 giờ

#### 9. **Hypophosphatemia Management**
- **Guideline:** Various
- **File:** `protocols/emergency/electrolytes.py` (mở rộng)
- **Nội dung:**
  - Replacement protocol
  - Dosing calculator
  - Monitoring
- **Thời gian:** 1-2 giờ

#### 10. **Hypocalcemia Emergency**
- **Guideline:** Various
- **File:** `protocols/emergency/electrolytes.py` (mở rộng)
- **Nội dung:**
  - Acute vs chronic
  - Calcium gluconate vs chloride
  - Dosing calculator
- **Thời gian:** 1-2 giờ

---

### **PRIORITY 4: Oncology Protocols** 🔥

#### 11. **Tumor Lysis Syndrome Prevention**
- **Guideline:** NCCN 2023
- **File:** `protocols/oncology/tls.py`
- **Nội dung:**
  - Risk stratification
  - Allopurinol vs Rasburicase
  - Hydration protocol
  - Monitoring (uric acid, K, P, Ca)
- **Thời gian:** 3-4 giờ

#### 12. **Febrile Neutropenia Management**
- **Guideline:** IDSA 2010, ASCO 2018
- **File:** `protocols/oncology/febrile_neutropenia.py`
- **Nội dung:**
  - Risk stratification (MASCC score)
  - Empiric antibiotic selection
  - Outpatient vs Inpatient
  - Duration of therapy
- **Thời gian:** 3-4 giờ

#### 13. **Hypercalcemia of Malignancy**
- **Guideline:** ASCO 2021
- **File:** `protocols/oncology/hypercalcemia.py`
- **Nội dung:**
  - Hydration
  - Bisphosphonates (zoledronate)
  - Calcitonin (severe)
  - Monitoring
- **Thời gian:** 2-3 giờ

---

## 📝 QUY TRÌNH TỪNG BƯỚC

### **BƯỚC 1: NGHIÊN CỨU & CHUẨN BỊ** (30-60 phút)

#### 1.1. Xác định Protocol Cần Bổ Sung
```bash
# Checklist:
- [ ] Protocol có guideline rõ ràng?
- [ ] Protocol có clinical value cao?
- [ ] Protocol được dùng thường xuyên?
- [ ] Có đủ thông tin để implement?
```

#### 1.2. Tìm Guidelines Mới Nhất
**Nguồn tham khảo:**
- **UpToDate** - Clinical guidelines
- **PubMed** - Latest research
- **Guideline websites:**
  - AHA/ASA (Stroke, Cardiology)
  - IDSA (Infectious Disease)
  - KDIGO (Nephrology)
  - ATA (Endocrinology)
  - NCCN (Oncology)
  - Surviving Sepsis Campaign

**Cách tìm:**
1. Google: `"[Protocol Name] guidelines [Year]"` (VD: "CAP management IDSA 2019")
2. Check guideline websites trực tiếp
3. Tìm "Clinical Practice Guidelines" trên PubMed
4. Kiểm tra UpToDate "Summary and Recommendations"

#### 1.3. Thu Thập Thông Tin
**Template thu thập:**
```markdown
## [Protocol Name]

### Guideline Source:
- Organization: [AHA/IDSA/etc]
- Year: [2021]
- Link: [URL]

### Key Points:
1. Diagnostic Criteria: [...]
2. Treatment Algorithm: [...]
3. Dosing: [...]
4. Monitoring: [...]
5. Special Populations: [...]

### References:
- Primary guideline: [...]
- Supporting evidence: [...]
```

---

### **BƯỚC 2: TẠO FILE PROTOCOL** (2-4 giờ)

#### 2.1. Tạo File Mới
```bash
# Ví dụ: protocols/infectious/cap.py
# Hoặc: protocols/endocrinology/thyrotoxic_crisis.py
```

#### 2.2. Cấu Trúc File Template
```python
"""
[Protocol Name] Protocol
[Guideline Source] [Year]
[Brief Description]
"""

import streamlit as st

def render():
    """[Protocol Name] Protocol"""
    st.subheader("[Icon] [Protocol Name] Protocol")
    st.caption("[Guideline Source] [Year] - [Brief Description]")
    
    # Overview/Info box
    st.info("""
    **Key Points:**
    - Point 1
    - Point 2
    - Point 3
    """)
    
    st.markdown("---")
    
    # Main content sections
    # 1. Diagnostic Criteria
    # 2. Treatment Algorithm
    # 3. Dosing Calculator (if applicable)
    # 4. Monitoring
    # 5. Special Populations
    # 6. References
    
    # Footer
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể.")
```

#### 2.3. Các Section Cần Có

**A. Diagnostic Criteria**
- Clear criteria
- Scoring systems (nếu có)
- Differential diagnosis

**B. Treatment Algorithm**
- Step-by-step approach
- Decision trees
- Visual flow (nếu có thể)

**C. Dosing Information**
- Drug names (generic + brand names VN nếu có)
- Dosing ranges
- Calculator (nếu phức tạp)
- Adjustments (renal, hepatic)

**D. Monitoring**
- What to monitor
- Frequency
- Warning signs

**E. Special Populations**
- Elderly
- Pediatric
- Pregnancy
- Renal/Hepatic impairment

**F. References**
- Primary guideline
- Key studies
- Links (nếu có)

---

### **BƯỚC 3: TÍCH HỢP VÀO HỆ THỐNG** (30-60 phút)

#### 3.1. Update `__init__.py` Files

**A. Update specialty `__init__.py`**
```python
# protocols/infectious/__init__.py
from .cap import render as render_cap
from .hap_vap import render as render_hap_vap
from .cdiff import render as render_cdiff

__all__ = [
    'render_cap',
    'render_hap_vap',
    'render_cdiff',
]
```

**B. Update main `protocols/__init__.py`**
```python
from .infectious import (
    render_cap,
    render_hap_vap,
    render_cdiff
)

__all__ = [
    # ... existing
    'render_cap',
    'render_hap_vap',
    'render_cdiff',
]
```

#### 3.2. Update Main Page Router

**File:** `pages/04_📋_Protocols.py`

**A. Thêm specialty vào sidebar (nếu cần)**
```python
specialty = st.selectbox(
    "Chuyên khoa:",
    [
        "🚨 Cấp Cứu (Emergency)",
        "🫁 Hô Hấp (Respiratory)",
        "❤️ Tim Mạch (Cardiology)",
        "🧪 Thận (Nephrology)",
        "🦠 Nhiễm Khuẩn (Infectious)",  # NEW
        "⚕️ Nội Tiết (Endocrinology)",  # NEW
        "🎗️ Ung Thư (Oncology)",       # NEW
    ]
)
```

**B. Thêm protocols vào radio options**
```python
elif "Nhiễm Khuẩn" in specialty:
    protocol = st.radio(
        "Phác đồ:",
        [
            "🫁 CAP Management",
            "🏥 HAP/VAP Guidelines",
            "🦠 C. diff Treatment",
        ],
        label_visibility="collapsed"
    )
```

**C. Thêm routing logic**
```python
elif "CAP" in protocol:
    render_cap()
elif "HAP" in protocol or "VAP" in protocol:
    render_hap_vap()
elif "C. diff" in protocol or "cdiff" in protocol.lower():
    render_cdiff()
```

#### 3.3. Import vào Main Page
```python
from protocols import (
    # ... existing
    render_cap,
    render_hap_vap,
    render_cdiff,
)
```

---

### **BƯỚC 4: TESTING & VALIDATION** (30-60 phút)

#### 4.1. Functional Testing
```bash
# Checklist:
- [ ] File imports successfully
- [ ] No syntax errors
- [ ] Protocol displays correctly
- [ ] All sections render properly
- [ ] Navigation works
- [ ] No broken links
```

#### 4.2. Content Validation
```bash
# Checklist:
- [ ] Information is accurate
- [ ] Dosing is correct
- [ ] References are valid
- [ ] Vietnamese translations are correct
- [ ] No typos
```

#### 4.3. UI/UX Check
```bash
# Checklist:
- [ ] Layout is clean
- [ ] Information is organized
- [ ] Easy to navigate
- [ ] Mobile-friendly
- [ ] Consistent with other protocols
```

---

### **BƯỚC 5: DOCUMENTATION** (15-30 phút)

#### 5.1. Update Documentation
- Add to `docs/PROTOCOLS_LIST.md` (nếu có)
- Update README nếu cần
- Note any special features

#### 5.2. Commit Message Template
```bash
feat(protocols): Add [Protocol Name] protocol

- Add [Protocol Name] management protocol
- Based on [Guideline Source] [Year]
- Includes: [key features]
- File: protocols/[specialty]/[filename].py

Closes #[issue] (nếu có)
```

---

## 🎯 KẾ HOẠCH THỰC HIỆN THEO PHASE

### **PHASE 1: Emergency & Infectious (Ưu tiên cao nhất)** 
**Thời gian:** 1-2 tuần

1. ✅ Sepsis 3-Hour Bundle (2-3h)
2. ✅ CAP Management (3-4h)
3. ✅ HAP/VAP Guidelines (3-4h)
4. ✅ C. diff Treatment (2-3h)

**Tổng:** ~10-14 giờ

---

### **PHASE 2: Endocrine Emergencies**
**Thời gian:** 1 tuần

5. ✅ Thyrotoxic Crisis (2-3h)
6. ✅ Myxedema Coma (2h)
7. ✅ Adrenal Crisis (2h)

**Tổng:** ~6-7 giờ

---

### **PHASE 3: Electrolyte Expansion**
**Thời gian:** 3-5 ngày

8. ✅ Hypomagnesemia (1-2h)
9. ✅ Hypophosphatemia (1-2h)
10. ✅ Hypocalcemia (1-2h)

**Tổng:** ~3-6 giờ

---

### **PHASE 4: Oncology Protocols**
**Thời gian:** 1-2 tuần

11. ✅ Tumor Lysis Syndrome (3-4h)
12. ✅ Febrile Neutropenia (3-4h)
13. ✅ Hypercalcemia of Malignancy (2-3h)

**Tổng:** ~8-11 giờ

---

## 📚 TEMPLATE FILE MẪU

### **Template: Infectious Disease Protocol**
```python
"""
[Protocol Name] Protocol
[Guideline Source] [Year]
[Brief Description]
"""

import streamlit as st

def render():
    """[Protocol Name] Protocol"""
    st.subheader("🦠 [Protocol Name] Protocol")
    st.caption("[Guideline Source] [Year] - [Brief Description]")
    
    # Overview
    st.info("""
    **Key Points:**
    - Point 1
    - Point 2
    - Point 3
    """)
    
    st.markdown("---")
    
    # Section 1: Diagnostic Criteria
    st.markdown("### 📋 Diagnostic Criteria")
    # ... criteria ...
    
    # Section 2: Risk Stratification
    st.markdown("### 📊 Risk Stratification")
    # ... risk assessment ...
    
    # Section 3: Treatment Algorithm
    st.markdown("### 💊 Treatment Algorithm")
    # ... treatment steps ...
    
    # Section 4: Antibiotic Selection
    st.markdown("### 🧪 Antibiotic Selection")
    # ... antibiotic guide ...
    
    # Section 5: Monitoring
    st.markdown("### 📈 Monitoring")
    # ... monitoring guide ...
    
    # Section 6: Special Populations
    st.markdown("### 👥 Special Populations")
    # ... special considerations ...
    
    # Section 7: References
    st.markdown("---")
    st.markdown("### 📚 References")
    st.markdown("""
    1. [Primary Guideline] - [Year]
    2. [Supporting Study] - [Year]
    """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể.")
```

---

## 🔍 CHECKLIST TRƯỚC KHI HOÀN THÀNH

### **Content Checklist:**
- [ ] Protocol name is clear
- [ ] Guideline source is cited
- [ ] Year of guideline is mentioned
- [ ] Diagnostic criteria are complete
- [ ] Treatment algorithm is step-by-step
- [ ] Dosing information is accurate
- [ ] Monitoring requirements are clear
- [ ] Special populations are addressed
- [ ] References are valid and accessible

### **Technical Checklist:**
- [ ] File is in correct directory
- [ ] `__init__.py` files are updated
- [ ] Main page router is updated
- [ ] Imports are correct
- [ ] No syntax errors
- [ ] No linting errors
- [ ] UI is consistent with other protocols

### **Quality Checklist:**
- [ ] Vietnamese translations are correct
- [ ] Medical terminology is accurate
- [ ] No typos or grammatical errors
- [ ] Formatting is consistent
- [ ] Information is up-to-date
- [ ] Clinical accuracy is verified

---

## 📝 NOTES

### **Best Practices:**
1. **Always cite sources** - Include guideline organization and year
2. **Keep it practical** - Focus on actionable steps
3. **Use calculators** - Add dosing calculators for complex protocols
4. **Visual aids** - Use tables, flowcharts when helpful
5. **Vietnamese first** - Primary language is Vietnamese
6. **Mobile-friendly** - Ensure protocols work on mobile

### **Common Pitfalls to Avoid:**
1. ❌ Don't copy-paste without understanding
2. ❌ Don't use outdated guidelines
3. ❌ Don't skip special populations
4. ❌ Don't forget monitoring requirements
5. ❌ Don't make dosing too complex without calculator

---

## 🚀 BẮT ĐẦU VỚI PROTOCOL NÀO?

**Khuyến nghị:** Bắt đầu với **CAP Management** vì:
- ✅ High clinical value
- ✅ Clear guidelines (IDSA/ATS 2019)
- ✅ Frequently used
- ✅ Good template for other infectious protocols

**Next Steps:**
1. Research CAP guidelines (IDSA/ATS 2019)
2. Create `protocols/infectious/cap.py`
3. Follow template structure
4. Integrate into system
5. Test and validate

---

**Last Updated:** 2025-02-04  
**Status:** 📋 Ready for implementation  
**Next Protocol:** CAP Management (Priority 1)

