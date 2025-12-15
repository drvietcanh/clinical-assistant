# Phase 1 Integration Example

Hướng dẫn tích hợp các tính năng Phase 1 vào calculator

---

## 📝 Example: CHA₂DS₂-VASc Calculator với Phase 1 Features

```python
"""
CHA₂DS₂-VASc Score Calculator
Với Phase 1 features: References, History, Share, Suggestions
"""

import streamlit as st
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions


def render():
    """CHA₂DS₂-VASc Score Calculator với Phase 1 features"""
    st.subheader("❤️ CHA₂DS₂-VASc Score")
    st.caption("Đánh giá Nguy cơ Đột Quỵ Trong Rung Nhĩ")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared:
        # Pre-fill inputs from shared result
        st.session_state['shared_inputs'] = shared['inputs']
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
    
    # Calculator inputs
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Tiêu chí Đánh giá")
        
        chf = st.checkbox("**C** - Suy tim sung huyết")
        htn = st.checkbox("**H** - Tăng huyết áp")
        age_group = st.radio("**A** - Tuổi", ["< 65", "65-74", "≥ 75"], horizontal=True)
        dm = st.checkbox("**D** - Đái tháo đường")
        stroke = st.checkbox("**S** - Tiền sử Đột quỵ / TIA")
        vasc = st.checkbox("**V** - Bệnh mạch máu")
        sex = st.radio("**Sc** - Giới tính", ["Nam", "Nữ"], horizontal=True)
    
    with col2:
        st.markdown("### 💡 Gợi ý")
        render_suggestions(
            calculator_id="cha2ds2vasc",
            calculator_name="CHA₂DS₂-VASc Score",
            category="Tim Mạch",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Calculate button
    if st.button("📊 Tính toán", type="primary"):
        # Calculate score
        score = 0
        details = []
        
        if chf:
            score += 1
            details.append("CHF: +1")
        if htn:
            score += 1
            details.append("HTN: +1")
        if age_group == "65-74":
            score += 1
            details.append("Age 65-74: +1")
        elif age_group == "≥ 75":
            score += 2
            details.append("Age ≥75: +2")
        if dm:
            score += 1
            details.append("DM: +1")
        if stroke:
            score += 2
            details.append("Stroke/TIA: +2")
        if vasc:
            score += 1
            details.append("Vascular: +1")
        if sex == "Nữ":
            score += 1
            details.append("Female: +1")
        
        # Determine risk
        if score == 0:
            risk = "THẤP (0% năm)"
        elif score == 1:
            risk = "TRUNG BÌNH (1.3% năm)"
        else:
            risk = "CAO (≥2.2% năm)"
        
        # Display results
        st.markdown("---")
        st.markdown("### 📊 Kết quả")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("CHA₂DS₂-VASc Score", f"{score} điểm")
        with col2:
            st.metric("Nguy cơ đột quỵ", risk)
        
        st.markdown("**Chi tiết:**")
        for detail in details:
            st.markdown(f"- {detail}")
        
        # Prepare data for history and share
        inputs_dict = {
            "CHF": chf,
            "HTN": htn,
            "Age Group": age_group,
            "DM": dm,
            "Stroke/TIA": stroke,
            "Vascular": vasc,
            "Sex": sex
        }
        
        results_dict = {
            "Score": score,
            "Risk": risk,
            "Details": details
        }
        
        # Save to history
        save_calculation_to_history(
            calculator_id="cha2ds2vasc",
            calculator_name="CHA₂DS₂-VASc Score",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="cha2ds2vasc",
            calculator_name="CHA₂DS₂-VASc Score",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        st.markdown("---")
        from components.calculation_history import render_history_ui
        render_history_ui(calculator_id="cha2ds2vasc", show_actions=True)
    
    # References section (always visible)
    st.markdown("---")
    references = get_references("CHA2DS2-VASc")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )
    
    st.markdown("---")
    st.caption("⚠️ Công cụ hỗ trợ lâm sàng - không thay thế đánh giá lâm sàng toàn diện")
```

---

## 🔧 Integration Checklist

### 1. References
- [ ] Import `get_references` và `render_references_section`
- [ ] Call `get_references(calculator_name)` 
- [ ] Call `render_references_section()` ở cuối calculator

### 2. History
- [ ] Import `save_calculation_to_history`
- [ ] Sau khi tính toán, call `save_calculation_to_history()` với inputs và results
- [ ] (Optional) Import và render `render_history_ui()` để hiển thị history

### 3. Share
- [ ] Import `render_share_section` và `load_shared_result_from_url`
- [ ] Call `load_shared_result_from_url()` ở đầu calculator để load shared result
- [ ] Sau khi tính toán, call `render_share_section()` với inputs và results

### 4. Suggestions
- [ ] Import `render_suggestions`
- [ ] Call `render_suggestions()` với calculator_id, name, category

---

## 📦 Quick Integration Template

```python
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions

def render():
    # Load shared result
    shared = load_shared_result_from_url()
    
    # Calculator UI
    # ... inputs ...
    
    # Suggestions (sidebar or inline)
    render_suggestions(
        calculator_id="your_calc_id",
        calculator_name="Your Calculator Name",
        category="Your Category"
    )
    
    # Calculate
    if st.button("Tính toán"):
        # ... calculation logic ...
        
        # Save to history
        save_calculation_to_history(
            calculator_id="your_calc_id",
            calculator_name="Your Calculator Name",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="your_calc_id",
            calculator_name="Your Calculator Name",
            inputs=inputs_dict,
            results=results_dict
        )
    
    # References (always at bottom)
    references = get_references("Your Calculator Name")
    if references:
        render_references_section(references=references)
```

---

## 🎯 Best Practices

1. **References:** Luôn hiển thị ở cuối calculator (even before calculation)
2. **History:** Save sau mỗi calculation thành công
3. **Share:** Hiển thị sau khi có kết quả
4. **Suggestions:** Hiển thị ở sidebar hoặc sau results

---

**Phase 1 Integration: Ready!** ✅

