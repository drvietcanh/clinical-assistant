# Kế Hoạch Triển Khai Chi Tiết: Module Máy Thở

## 📋 Tổng Quan

Tài liệu này mô tả chi tiết cách triển khai từng phiên phát triển module máy thở, bao gồm cấu trúc code, API, và các bước cụ thể.

---

## PHIÊN 1: Nền Tảng & Tích Hợp ABG

### 1.1. Cấu Trúc Files Mới

```
ventilator/
├── __init__.py (sửa)
├── calculators.py (sửa)
├── tables.py (giữ nguyên)
├── abg_integration.py (mới) ⭐
└── comprehensive_calculator.py (mới) ⭐
```

### 1.2. File: `ventilator/abg_integration.py`

```python
"""
ABG Integration for Ventilator Module
Tích hợp ABG vào ventilator calculator
"""

import streamlit as st
from labs.abg import calculate_pf_ratio, analyze_acid_base

def render_abg_panel():
    """Panel nhập ABG trong ventilator page"""
    st.markdown("### 💨 Thông Số Khí Máu (ABG)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        ph = st.number_input("pH", 6.8, 7.8, 7.40, 0.01, key="vent_abg_ph")
        pco2 = st.number_input("PaCO₂ (mmHg)", 10.0, 100.0, 40.0, 0.1, 
                               format="%.1f", key="vent_abg_pco2")
        po2 = st.number_input("PaO₂ (mmHg)", 30.0, 600.0, 95.0, 1.0, 
                             key="vent_abg_po2")
    
    with col2:
        hco3 = st.number_input("HCO₃ (mEq/L)", 5.0, 50.0, 24.0, 0.1, 
                               format="%.1f", key="vent_abg_hco3")
        fio2 = st.number_input("FiO₂ (%)", 21.0, 100.0, 21.0, 1.0, 
                              key="vent_abg_fio2")
        sao2 = st.number_input("SaO₂ (%)", 70.0, 100.0, 98.0, 0.1, 
                              format="%.1f", key="vent_abg_sao2")
    
    return {
        "ph": ph,
        "pco2": pco2,
        "po2": po2,
        "hco3": hco3,
        "fio2": fio2,
        "sao2": sao2
    }

def calculate_pf_ratio(po2, fio2):
    """Tính P/F ratio"""
    if fio2 == 0:
        return None
    return po2 / (fio2 / 100)

def classify_ards(pf_ratio):
    """Phân loại ARDS dựa trên P/F ratio"""
    if pf_ratio is None:
        return None, None
    
    if pf_ratio >= 400:
        return "Bình thường", "success"
    elif pf_ratio >= 300:
        return "Thiếu oxy nhẹ", "info"
    elif pf_ratio >= 200:
        return "ARDS nhẹ", "warning"
    elif pf_ratio >= 100:
        return "ARDS trung bình", "error"
    else:
        return "ARDS nặng", "error"

def display_abg_summary(abg_data):
    """Hiển thị tóm tắt ABG với màu sắc cảnh báo"""
    pf_ratio = calculate_pf_ratio(abg_data["po2"], abg_data["fio2"])
    ards_class, color = classify_ards(pf_ratio)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # pH
        if 7.35 <= abg_data["ph"] <= 7.45:
            st.success(f"**pH:** {abg_data['ph']:.2f} ✓")
        else:
            st.error(f"**pH:** {abg_data['ph']:.2f} ⚠️")
    
    with col2:
        # P/F Ratio
        if pf_ratio:
            if color == "success":
                st.success(f"**P/F:** {pf_ratio:.0f} ✓")
            elif color == "warning":
                st.warning(f"**P/F:** {pf_ratio:.0f} ⚠️")
            else:
                st.error(f"**P/F:** {pf_ratio:.0f} ⚠️")
            st.caption(f"{ards_class}")
    
    with col3:
        # PaCO2
        if 35 <= abg_data["pco2"] <= 45:
            st.success(f"**PaCO₂:** {abg_data['pco2']:.1f} ✓")
        else:
            st.warning(f"**PaCO₂:** {abg_data['pco2']:.1f} ⚠️")
    
    return pf_ratio, ards_class
```

### 1.3. File: `ventilator/comprehensive_calculator.py`

```python
"""
Comprehensive Ventilator Calculator
Tính toán tổng hợp với tất cả thông số
"""

import streamlit as st
from ventilator.abg_integration import render_abg_panel, calculate_pf_ratio, classify_ards

def render_comprehensive_calculator():
    """Comprehensive Ventilator Calculator"""
    st.subheader("🫁 Máy Thở - Tính Toán Tổng Hợp")
    st.caption("Nhập đầy đủ thông số để có khuyến nghị chính xác")
    
    # Layout: 3 cột
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        st.markdown("### 📋 Thông Tin Bệnh Nhân")
        sex = st.radio("Giới tính", ["Nam", "Nữ"], horizontal=True, 
                      key="comp_sex")
        height = st.number_input("Chiều cao (cm)", 100, 220, 170, 1, 
                                key="comp_height")
        
        # Calculate PBW
        if sex == "Nam":
            pbw = 50 + 0.91 * (height - 152.4)
        else:
            pbw = 45.5 + 0.91 * (height - 152.4)
        pbw = round(pbw, 1)
        
        st.metric("PBW", f"{pbw} kg")
    
    with col2:
        st.markdown("### ⚙️ Thông Số Máy Thở")
        mode = st.selectbox("Mode", 
                           ["AC/VC", "SIMV", "PSV", "CPAP", "BiPAP"],
                           key="comp_mode")
        vt = st.number_input("Vt (mL)", 0, 1000, 0, 10, key="comp_vt")
        rr = st.number_input("RR (lần/phút)", 0, 50, 0, 1, key="comp_rr")
        peep = st.number_input("PEEP (cmH2O)", 0, 30, 0, 1, key="comp_peep")
        fio2 = st.number_input("FiO₂ (%)", 21, 100, 21, 1, key="comp_fio2")
        plateau = st.number_input("Plateau Pressure (cmH2O)", 0, 60, 0, 1, 
                                  key="comp_plateau")
    
    with col3:
        st.markdown("### 💨 ABG")
        abg_data = render_abg_panel()
    
    # Calculate
    if st.button("🧮 Tính Toán & Phân Tích", type="primary"):
        # Calculate P/F ratio
        pf_ratio = calculate_pf_ratio(abg_data["po2"], abg_data["fio2"])
        ards_class, _ = classify_ards(pf_ratio)
        
        # Calculate driving pressure
        driving_pressure = None
        if plateau > 0 and peep >= 0:
            driving_pressure = plateau - peep
        
        # Calculate compliance
        compliance = None
        if driving_pressure and driving_pressure > 0 and vt > 0:
            compliance = vt / driving_pressure
        
        # Display results
        st.markdown("---")
        st.markdown("### 📊 Kết Quả Tính Toán")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            if pf_ratio:
                st.metric("P/F Ratio", f"{pf_ratio:.0f}")
                st.caption(ards_class)
        
        with col2:
            if driving_pressure is not None:
                if driving_pressure <= 15:
                    st.success(f"**Driving P:** {driving_pressure:.1f} cmH2O ✓")
                else:
                    st.error(f"**Driving P:** {driving_pressure:.1f} cmH2O ⚠️")
            else:
                st.info("Cần nhập Plateau & PEEP")
        
        with col3:
            if compliance:
                if 30 <= compliance <= 50:
                    st.success(f"**Compliance:** {compliance:.1f} mL/cmH2O ✓")
                elif compliance < 30:
                    st.error(f"**Compliance:** {compliance:.1f} mL/cmH2O ⚠️")
                else:
                    st.warning(f"**Compliance:** {compliance:.1f} mL/cmH2O")
            else:
                st.info("Cần đủ thông số")
        
        with col4:
            if vt > 0 and pbw > 0:
                vt_per_kg = vt / pbw
                if vt_per_kg <= 6:
                    st.success(f"**Vt/kg:** {vt_per_kg:.1f} mL/kg ✓")
                elif vt_per_kg <= 8:
                    st.warning(f"**Vt/kg:** {vt_per_kg:.1f} mL/kg")
                else:
                    st.error(f"**Vt/kg:** {vt_per_kg:.1f} mL/kg ⚠️")
        
        # Alerts
        st.markdown("---")
        st.markdown("### ⚠️ Cảnh Báo & Khuyến Nghị")
        
        alerts = []
        
        if pf_ratio and pf_ratio < 200:
            alerts.append(("error", f"⚠️ P/F ratio thấp ({pf_ratio:.0f}) - ARDS nặng"))
        
        if driving_pressure and driving_pressure > 15:
            alerts.append(("error", f"⚠️ Driving pressure cao ({driving_pressure:.1f} cmH2O) - Cần giảm Vt hoặc tăng PEEP"))
        
        if plateau > 30:
            alerts.append(("error", f"⚠️ Plateau pressure cao ({plateau} cmH2O) - Cần giảm Vt"))
        
        if vt > 0 and pbw > 0:
            vt_per_kg = vt / pbw
            if vt_per_kg > 8:
                alerts.append(("error", f"⚠️ Vt/kg cao ({vt_per_kg:.1f} mL/kg) - Không lung-protective"))
        
        if compliance and compliance < 30:
            alerts.append(("warning", f"⚠️ Compliance thấp ({compliance:.1f} mL/cmH2O) - Phổi cứng"))
        
        if alerts:
            for alert_type, message in alerts:
                if alert_type == "error":
                    st.error(message)
                else:
                    st.warning(message)
        else:
            st.success("✅ Tất cả thông số trong giới hạn an toàn")
```

### 1.4. Sửa File: `ventilator/__init__.py`

```python
"""
Ventilator Module - Mechanical Ventilation Tools
Modular structure for easy maintenance
"""

from .calculators import render_ardsnet, render_initial_settings
from .tables import render_peep_fio2_table
from .comprehensive_calculator import render_comprehensive_calculator  # ⭐ Mới

__all__ = [
    'render_ardsnet',
    'render_initial_settings',
    'render_peep_fio2_table',
    'render_comprehensive_calculator',  # ⭐ Mới
]
```

### 1.5. Sửa File: `pages/03_🫁_Ventilator.py`

```python
# ... existing code ...

from ventilator import (
    render_ardsnet,
    render_initial_settings,
    render_peep_fio2_table,
    render_comprehensive_calculator  # ⭐ Mới
)

# ... existing code ...

function_type = st.selectbox(
    "Công cụ:",
    [
        "🫁 Tính Toán Tổng Hợp",  # ⭐ Mới - đặt đầu tiên
        "🫁 ARDSNet - Tidal Volume",
        "⚙️ Cài Đặt Ban Đầu",
        "📊 Bảng PEEP/FiO2",
        "💧 Tính Toán Dịch Truyền",
        "💉 Hướng Dẫn Vasopressor"
    ]
)

# ... existing code ...

# Route to appropriate function
if "Tính Toán Tổng Hợp" in function_type:  # ⭐ Mới
    render_comprehensive_calculator()

elif "ARDSNet" in function_type:
    render_ardsnet()

# ... existing code ...
```

---

## PHIÊN 2: Tư Vấn Thông Minh & Cảnh Báo

### 2.1. File: `ventilator/abg_advisor.py`

```python
"""
ABG-based Ventilator Adjustment Advisor
Tư vấn điều chỉnh máy thở dựa trên ABG
"""

import streamlit as st

def analyze_abg_for_ventilator(abg_data):
    """Phân tích ABG và đề xuất điều chỉnh máy thở"""
    recommendations = []
    
    # Acid-base analysis
    ph = abg_data["ph"]
    pco2 = abg_data["pco2"]
    hco3 = abg_data["hco3"]
    
    # Respiratory acidosis
    if ph < 7.35 and pco2 > 45:
        recommendations.append({
            "type": "error",
            "title": "Toan Hô Hấp",
            "message": "PaCO₂ cao, pH thấp",
            "actions": [
                "Tăng RR để tăng thông khí",
                "Kiểm tra Vt có đủ không",
                "Kiểm tra auto-PEEP",
                "Cân nhắc tăng flow rate"
            ]
        })
    
    # Respiratory alkalosis
    elif ph > 7.45 and pco2 < 35:
        recommendations.append({
            "type": "warning",
            "title": "Kiềm Hô Hấp",
            "message": "PaCO₂ thấp, pH cao",
            "actions": [
                "Giảm RR nếu quá cao",
                "Kiểm tra Vt có quá lớn không"
            ]
        })
    
    # Metabolic acidosis
    if ph < 7.35 and hco3 < 22:
        recommendations.append({
            "type": "warning",
            "title": "Toan Chuyển Hóa",
            "message": "HCO₃ thấp",
            "actions": [
                "Điều trị nguyên nhân (sepsis, shock, etc.)",
                "Có thể tăng RR nhẹ để bù",
                "Cân nhắc NaHCO₃ nếu nặng"
            ]
        })
    
    return recommendations

def recommend_ventilator_adjustments(abg_data, vent_settings):
    """Đề xuất điều chỉnh thông số máy thở"""
    recommendations = []
    
    pf_ratio = abg_data["po2"] / (abg_data["fio2"] / 100)
    
    # Hypoxemia
    if pf_ratio < 200:
        if vent_settings["peep"] < 10:
            recommendations.append({
                "parameter": "PEEP",
                "current": vent_settings["peep"],
                "suggested": min(vent_settings["peep"] + 2, 24),
                "reason": f"P/F ratio thấp ({pf_ratio:.0f}) - Cần tăng PEEP"
            })
        
        if abg_data["fio2"] < 60:
            recommendations.append({
                "parameter": "FiO₂",
                "current": abg_data["fio2"],
                "suggested": min(abg_data["fio2"] + 10, 100),
                "reason": "Oxy hóa kém - Cần tăng FiO₂"
            })
    
    # Hypercapnia
    if abg_data["pco2"] > 45:
        if vent_settings["rr"] < 25:
            recommendations.append({
                "parameter": "RR",
                "current": vent_settings["rr"],
                "suggested": min(vent_settings["rr"] + 2, 35),
                "reason": "PaCO₂ cao - Cần tăng thông khí"
            })
    
    # Hypocapnia
    elif abg_data["pco2"] < 35:
        if vent_settings["rr"] > 12:
            recommendations.append({
                "parameter": "RR",
                "current": vent_settings["rr"],
                "suggested": max(vent_settings["rr"] - 2, 8),
                "reason": "PaCO₂ thấp - Có thể giảm RR"
            })
    
    return recommendations

def display_recommendations(recommendations):
    """Hiển thị khuyến nghị"""
    if not recommendations:
        st.success("✅ Không có khuyến nghị điều chỉnh")
        return
    
    st.markdown("### 💡 Khuyến Nghị Điều Chỉnh")
    
    for rec in recommendations:
        if rec["type"] == "error":
            st.error(f"**{rec['title']}:** {rec['message']}")
        else:
            st.warning(f"**{rec['title']}:** {rec['message']}")
        
        st.markdown("**Hành động đề xuất:**")
        for i, action in enumerate(rec["actions"], 1):
            st.markdown(f"{i}. {action}")
        
        st.markdown("---")
```

### 2.2. File: `ventilator/alerts.py`

```python
"""
Ventilator Alerts System
Hệ thống cảnh báo thông minh
"""

import streamlit as st

def check_ventilator_alerts(vent_settings, abg_data, calculations):
    """Kiểm tra và tạo cảnh báo"""
    alerts = []
    
    # Plateau pressure
    if vent_settings.get("plateau", 0) > 30:
        alerts.append({
            "level": "critical",
            "title": "Plateau Pressure Cao",
            "message": f"Plateau pressure ({vent_settings['plateau']} cmH2O) > 30 cmH2O",
            "action": "Giảm Vt ngay lập tức"
        })
    
    # Driving pressure
    if calculations.get("driving_pressure", 0) > 15:
        alerts.append({
            "level": "critical",
            "title": "Driving Pressure Cao",
            "message": f"Driving pressure ({calculations['driving_pressure']:.1f} cmH2O) > 15 cmH2O",
            "action": "Giảm Vt hoặc tăng PEEP"
        })
    
    # P/F ratio
    if calculations.get("pf_ratio", 0) < 200:
        alerts.append({
            "level": "warning",
            "title": "P/F Ratio Thấp",
            "message": f"P/F ratio ({calculations['pf_ratio']:.0f}) < 200 - ARDS nặng",
            "action": "Tăng PEEP và/hoặc FiO₂"
        })
    
    # Vt/kg
    if calculations.get("vt_per_kg", 0) > 8:
        alerts.append({
            "level": "warning",
            "title": "Vt/kg Cao",
            "message": f"Vt/kg ({calculations['vt_per_kg']:.1f} mL/kg) > 8 mL/kg",
            "action": "Giảm Vt để lung-protective"
        })
    
    # Compliance
    if calculations.get("compliance", 100) < 30:
        alerts.append({
            "level": "info",
            "title": "Compliance Thấp",
            "message": f"Compliance ({calculations['compliance']:.1f} mL/cmH2O) < 30",
            "action": "Phổi cứng - Cần điều chỉnh thông số"
        })
    
    return alerts

def display_alerts(alerts):
    """Hiển thị cảnh báo"""
    if not alerts:
        return
    
    st.markdown("### ⚠️ Cảnh Báo")
    
    for alert in alerts:
        if alert["level"] == "critical":
            st.error(f"**🔴 {alert['title']}**\n\n{alert['message']}\n\n**Hành động:** {alert['action']}")
        elif alert["level"] == "warning":
            st.warning(f"**🟡 {alert['title']}**\n\n{alert['message']}\n\n**Hành động:** {alert['action']}")
        else:
            st.info(f"**🔵 {alert['title']}**\n\n{alert['message']}\n\n**Hành động:** {alert['action']}")
        
        st.markdown("---")
```

### 2.3. File: `ventilator/protocols.py`

```python
"""
Ventilator Protocol Recommendations
Khuyến nghị dựa trên protocol chuẩn
"""

import streamlit as st

def get_ardsnet_recommendations(pbw, pf_ratio):
    """Khuyến nghị theo ARDSNet protocol"""
    recommendations = []
    
    # Target Vt
    target_vt = pbw * 6
    recommendations.append({
        "parameter": "Vt",
        "target": f"{target_vt:.0f} mL (6 mL/kg PBW)",
        "reason": "ARDSNet protocol - Lung-protective ventilation"
    })
    
    # PEEP/FiO2 based on P/F ratio
    if pf_ratio < 100:
        recommendations.append({
            "parameter": "PEEP/FiO₂",
            "target": "PEEP 18-24, FiO₂ 0.8-1.0",
            "reason": "ARDS nặng - P/F <100"
        })
    elif pf_ratio < 200:
        recommendations.append({
            "parameter": "PEEP/FiO₂",
            "target": "PEEP 14-18, FiO₂ 0.6-0.8",
            "reason": "ARDS trung bình - P/F 100-200"
        })
    else:
        recommendations.append({
            "parameter": "PEEP/FiO₂",
            "target": "PEEP 8-12, FiO₂ 0.4-0.6",
            "reason": "ARDS nhẹ - P/F 200-300"
        })
    
    return recommendations

def get_sepsis_guidelines_recommendations():
    """Khuyến nghị theo Surviving Sepsis Campaign"""
    return [
        {
            "title": "Lung-Protective Ventilation",
            "recommendations": [
                "Vt ≤6-8 mL/kg PBW",
                "Plateau pressure ≤30 cmH2O",
                "PEEP ≥5 cmH2O"
            ]
        },
        {
            "title": "Permissive Hypercapnia",
            "recommendations": [
                "Cho phép pH ≥7.15",
                "Không cần điều chỉnh nếu pH >7.15"
            ]
        }
    ]

def display_protocol_recommendations(protocol_type, **kwargs):
    """Hiển thị khuyến nghị theo protocol"""
    if protocol_type == "ARDSNet":
        recommendations = get_ardsnet_recommendations(
            kwargs.get("pbw", 70),
            kwargs.get("pf_ratio", 200)
        )
        
        st.markdown("### 📋 ARDSNet Protocol Recommendations")
        for rec in recommendations:
            st.info(f"**{rec['parameter']}:** {rec['target']}\n\n*{rec['reason']}*")
    
    elif protocol_type == "Sepsis":
        recommendations = get_sepsis_guidelines_recommendations()
        
        st.markdown("### 📋 Surviving Sepsis Campaign Guidelines")
        for rec in recommendations:
            st.markdown(f"**{rec['title']}:**")
            for item in rec['recommendations']:
                st.markdown(f"- {item}")
```

---

## PHIÊN 3-6: (Tương tự, tạo files riêng)

### Cấu Trúc Files Hoàn Chỉnh

```
ventilator/
├── __init__.py
├── calculators.py
├── tables.py
├── abg_integration.py          # PHIÊN 1
├── comprehensive_calculator.py  # PHIÊN 1
├── abg_advisor.py              # PHIÊN 2
├── alerts.py                   # PHIÊN 2
├── protocols.py                # PHIÊN 2
├── compliance.py               # PHIÊN 3
├── auto_peep.py                # PHIÊN 3
├── weaning.py                  # PHIÊN 4
├── history.py                  # PHIÊN 5
├── trends.py                   # PHIÊN 5
└── export.py                   # PHIÊN 5
```

---

## 📝 Checklist Triển Khai

### PHIÊN 1
- [ ] Tạo `abg_integration.py`
- [ ] Tạo `comprehensive_calculator.py`
- [ ] Sửa `__init__.py`
- [ ] Sửa `pages/03_🫁_Ventilator.py`
- [ ] Test tích hợp ABG
- [ ] Test comprehensive calculator
- [ ] Test responsive design

### PHIÊN 2
- [ ] Tạo `abg_advisor.py`
- [ ] Tạo `alerts.py`
- [ ] Tạo `protocols.py`
- [ ] Tích hợp vào comprehensive calculator
- [ ] Test tư vấn
- [ ] Test cảnh báo
- [ ] Test protocol recommendations

### PHIÊN 3-6
- [ ] Tạo các files tương ứng
- [ ] Tích hợp vào main page
- [ ] Test từng tính năng
- [ ] Test integration

---

**Tài Liệu Này Được Tạo Bởi:** AI Assistant  
**Ngày:** 2025-02-04  
**Phiên Bản:** 1.0

