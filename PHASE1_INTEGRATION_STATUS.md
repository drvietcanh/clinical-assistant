# 📊 TRẠNG THÁI TÍCH HỢP PHASE 1 VÀO CALCULATORS

**Ngày cập nhật:** 2025-02-05  
**Tổng số calculators:** ~146  
**Đã tích hợp Phase 1:** ~22 (15%)  
**Cần tích hợp:** ~124 (85%)

---

## ✅ CALCULATORS ĐÃ TÍCH HỢP PHASE 1 (22)

### Tim Mạch (Cardiology) - 5/13
- ✅ CHA2DS2-VASc
- ✅ HEART Score
- ✅ GRACE Score
- ✅ TIMI Risk Score
- ✅ HAS-BLED Score

### Hô Hấp (Respiratory) - 5/5
- ✅ Wells PE Score
- ✅ PERC Rule
- ✅ CURB-65
- ✅ PESI Score
- ✅ PSI/PORT Score

### Cấp Cứu (Emergency) - 3/12
- ✅ SOFA Score
- ✅ qSOFA
- ✅ MEWS

### Thần Kinh (Neurology) - 4/10
- ✅ GCS Score
- ✅ NIHSS
- ✅ Hunt & Hess Scale
- ✅ ICH Score

### Tiêu Hóa (GI) - 1/8
- ✅ MELD (partial - chỉ có references)

### Khác
- ✅ Child-Pugh (GI)
- ✅ NEWS2 (Emergency)

---

## ⏳ CALCULATORS CẦN TÍCH HỢP PHASE 1

### Tim Mạch (Cardiology) - 8 còn lại
- [ ] ASCVD Risk Calculator
- [ ] Framingham Risk Score
- [ ] Score2
- [ ] Score2-OP
- [ ] QTC Calculator
- [ ] Killip Class
- [ ] NYHA Class
- [ ] Duke Treadmill Score

### Cấp Cứu (Emergency) - 9 còn lại
- [ ] Apache2
- [ ] Apache3
- [ ] SAPS2
- [ ] SAPS3
- [ ] LODS
- [ ] MODS
- [ ] LACE Index
- [ ] Hospital Score
- [ ] SOFA2

### Thần Kinh (Neurology) - 6 còn lại
- [ ] ABCD2 Score
- [ ] Four Score
- [ ] Aspects Score
- [ ] Barthel Index
- [ ] MRS (Modified Rankin Scale)
- [ ] Pediatric GCS

### Tiêu Hóa (GI) - 7 còn lại
- [ ] MELD-Na
- [ ] BISAP
- [ ] AIMS65
- [ ] Glasgow-Blatchford Score
- [ ] Rockall Score
- [ ] Ranson Score
- [ ] Child-Pugh (cần kiểm tra lại)

### Nhi Khoa (Pediatrics) - 7
- [ ] PIM2
- [ ] PELOD2
- [ ] PRISM3
- [ ] PEWS
- [ ] Apgar Score
- [ ] Pediatric SOFA
- [ ] Westley Croup Score

### Phẫu Thuật (Surgery) - 20+
- [ ] Four AT
- [ ] CAM-ICU
- [ ] ARISCAT
- [ ] PADSS
- [ ] Riker SAS
- [ ] RASS
- [ ] Cormack-Lehane
- [ ] LEMON
- [ ] El-Ganzouri
- [ ] Ramsay
- [ ] Wilson Risk
- [ ] Koivuranta PONV
- [ ] Gupta Cardiac
- [ ] Goldman Cardiac
- [ ] SORT
- [ ] Surgical Apgar
- [ ] Apfel PONV
- [ ] ASA
- [ ] POSSUM
- [ ] Caprini
- [ ] RCRI
- [ ] Aldrete
- [ ] Mallampati

### Chấn Thương (Trauma) - 5
- [ ] ISS
- [ ] RTS
- [ ] TRISS
- [ ] Canadian C-Spine
- [ ] NEXUS

### Huyết Học (Hematology) - 4
- [ ] DIC Score
- [ ] Wells DVT
- [ ] Four T's (HIT)
- [ ] Padua Score

### Nhiễm Trùng (Infectious) - 5
- [ ] Pitt Bacteremia
- [ ] MASCC
- [ ] Centor Score
- [ ] SIRS
- [ ] FeverPAIN

### Chuyển Hóa (Metabolism) - 8
- [ ] Winter Formula
- [ ] Osmolality
- [ ] CrCl
- [ ] Corrected Calcium
- [ ] Anion Gap
- [ ] BMI/IBW/BSA
- [ ] FeNa Calculator
- [ ] Free T4 Index
- [ ] HbA1c to eAG

### Thận (Nephrology) - 4
- [ ] RIFLE
- [ ] KDIGO
- [ ] AKIN
- [ ] eGFR Calculators

### Tâm Thần (Psychiatry) - 7
- [ ] PHQ9
- [ ] GAD7
- [ ] CIWA
- [ ] COWS
- [ ] CAM
- [ ] MMSE
- [ ] MOCA

### Da Liễu (Dermatology) - 4
- [ ] PASI
- [ ] SCORAD
- [ ] Burn TBSA
- [ ] Parkland Formula
- [ ] DLQI

### Thấp Khớp (Rheumatology) - 5
- [ ] SDAI
- [ ] DAS28
- [ ] CDAI
- [ ] SLICC
- [ ] Gout
- [ ] ACR RA

### Ung Thư (Oncology) - 3
- [ ] ECOG
- [ ] Karnofsky
- [ ] PPS
- [ ] CIPN

### Sản Khoa (Obstetrics) - 3
- [ ] Bishop Score
- [ ] Modified Bishop
- [ ] Preeclampsia

### Điều Dưỡng (Nursing) - 2
- [ ] Braden Scale
- [ ] Morse Fall Risk

### Tai Mũi Họng (ENT) - 2
- [ ] Epworth Sleepiness
- [ ] STOP-BANG

### Đau (Pain) - 5
- [ ] DN4
- [ ] FLACC
- [ ] NIPS
- [ ] NRS
- [ ] VAS
- [ ] Wong-Baker

### Mắt (Ophthalmology) - 1
- [ ] IOP Correction

---

## 📋 HƯỚNG DẪN TÍCH HỢP PHASE 1

### Pattern chuẩn để tích hợp:

1. **Import các components Phase 1:**
```python
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
```

2. **Trong hàm `render()`:**
   - Load shared result từ URL (đầu hàm)
   - Render smart suggestions (trong sidebar hoặc column)
   - Sau khi tính toán: save to history, render share section, render history UI, render references

3. **Ví dụ code pattern:**
```python
def render():
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'calculator_id':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Input fields...
    
    with col2:
        # Smart Suggestions
        render_suggestions(
            calculator_id="calculator_id",
            calculator_name="Calculator Name",
            category="Category",
            show_related=True,
            show_category=True,
            limit=3
        )
        
        if st.button("🧮 Tính", type="primary"):
            # Calculate...
            
            # Prepare inputs_dict and results_dict
            
            # Export section
            from components.export import render_export_section
            render_export_section(...)
            
            # Save to history
            save_calculation_to_history(...)
            
            # Share section
            render_share_section(...)
            
            # History section
            from components.calculation_history import render_history_ui
            render_history_ui(...)
            
            # References section
            references = get_references("Calculator Name")
            if references:
                render_references_section(...)
    
    # Always show references at the bottom
    references = get_references("Calculator Name")
    if references:
        render_references_section(...)
```

---

## 🎯 ƯU TIÊN TÍCH HỢP

### Ưu tiên cao (Quan trọng nhất):
1. **Tim Mạch:** ASCVD, Framingham, Score2, QTC
2. **Cấp Cứu:** Apache2, Apache3, SAPS2, SAPS3
3. **Thần Kinh:** ABCD2, Four Score, Aspects
4. **Tiêu Hóa:** MELD-Na, BISAP, AIMS65, Glasgow-Blatchford
5. **Nhi Khoa:** PIM2, PELOD2, PRISM3, PEWS

### Ưu tiên trung bình:
- Chấn Thương: ISS, RTS, TRISS
- Huyết Học: DIC Score, Wells DVT
- Nhiễm Trùng: SIRS, Centor, MASCC
- Thận: KDIGO, AKIN, RIFLE

### Ưu tiên thấp:
- Phẫu Thuật (nhiều calculators)
- Tâm Thần
- Da Liễu
- Thấp Khớp
- Ung Thư

---

## 📝 NOTES

1. **Calculator ID:** Cần đảm bảo `calculator_id` khớp với tên trong `references_config.py` và `smart_suggestions.py`
2. **Category:** Cần đúng category để suggestions hoạt động tốt
3. **References:** Kiểm tra xem calculator có trong `references_config.py` chưa
4. **Export:** Đảm bảo `inputs_dict` và `results_dict` được format đúng

---

**Tiếp tục tích hợp theo thứ tự ưu tiên!**

