"""
ICU Drug Compatibility Checker
Y-site compatibility and drug interactions in ICU setting
"""

import streamlit as st
from components.ui.alerts import render_info_alert, render_warning_alert, render_error_alert


# Y-site compatibility database
Y_SITE_COMPATIBILITY = {
    "Norepinephrine": {
        "compatible": ["Dopamine", "Epinephrine", "Vasopressin", "Dobutamine", "Fentanyl", "Morphine", "Propofol", "Midazolam"],
        "incompatible": ["Sodium Bicarbonate", "Alkaline solutions"],
        "notes": "Pha loãng trong D5W hoặc NS. Tránh pha với alkaline solutions."
    },
    "Epinephrine": {
        "compatible": ["Norepinephrine", "Dopamine", "Vasopressin", "Dobutamine"],
        "incompatible": ["Sodium Bicarbonate", "Alkaline solutions"],
        "notes": "Pha loãng trong D5W hoặc NS."
    },
    "Vasopressin": {
        "compatible": ["Norepinephrine", "Epinephrine", "Dopamine", "Dobutamine"],
        "incompatible": ["Sodium Bicarbonate"],
        "notes": "Có thể dùng chung Y-site với các vasopressor khác."
    },
    "Dopamine": {
        "compatible": ["Norepinephrine", "Epinephrine", "Vasopressin", "Dobutamine"],
        "incompatible": ["Sodium Bicarbonate", "Alkaline solutions"],
        "notes": "Pha loãng trong D5W hoặc NS."
    },
    "Dobutamine": {
        "compatible": ["Norepinephrine", "Epinephrine", "Dopamine", "Vasopressin", "Fentanyl", "Morphine"],
        "incompatible": ["Sodium Bicarbonate", "Alkaline solutions"],
        "notes": "Pha loãng trong D5W hoặc NS."
    },
    "Propofol": {
        "compatible": ["Norepinephrine", "Fentanyl", "Morphine", "Midazolam"],
        "incompatible": ["Dopamine", "Epinephrine", "Dobutamine", "Vasopressin"],
        "notes": "Không trộn với các thuốc khác. Dùng đường truyền riêng."
    },
    "Midazolam": {
        "compatible": ["Propofol", "Fentanyl", "Morphine", "Norepinephrine"],
        "incompatible": ["Sodium Bicarbonate"],
        "notes": "Có thể dùng chung với propofol và opioids."
    },
    "Fentanyl": {
        "compatible": ["Norepinephrine", "Dobutamine", "Propofol", "Midazolam", "Morphine"],
        "incompatible": [],
        "notes": "Tương đối tương thích với nhiều thuốc."
    },
    "Morphine": {
        "compatible": ["Norepinephrine", "Dobutamine", "Propofol", "Midazolam", "Fentanyl"],
        "incompatible": [],
        "notes": "Có thể giải phóng histamine."
    },
    "Dexmedetomidine": {
        "compatible": ["Fentanyl", "Morphine"],
        "incompatible": ["Propofol", "Midazolam", "Vasopressors"],
        "notes": "Dùng đường truyền riêng. Không trộn với propofol hoặc benzodiazepines."
    },
    "Vancomycin": {
        "compatible": ["Piperacillin/Tazobactam", "Meropenem", "Ceftriaxone"],
        "incompatible": ["Aminoglycosides", "Amphotericin B"],
        "notes": "Có thể gây phản ứng Red Man nếu truyền quá nhanh."
    },
    "Piperacillin/Tazobactam": {
        "compatible": ["Vancomycin", "Meropenem"],
        "incompatible": ["Aminoglycosides"],
        "notes": "Có thể gây giảm K+ khi dùng liều cao."
    },
    "Meropenem": {
        "compatible": ["Vancomycin", "Piperacillin/Tazobactam"],
        "incompatible": ["Aminoglycosides"],
        "notes": "Tương đối an toàn khi dùng chung."
    },
    "Sodium Bicarbonate": {
        "compatible": [],
        "incompatible": ["Norepinephrine", "Epinephrine", "Dopamine", "Dobutamine", "Vasopressin", "Calcium", "Midazolam"],
        "notes": "Không tương thích với nhiều thuốc. Dùng đường truyền riêng."
    },
    "Calcium": {
        "compatible": [],
        "incompatible": ["Sodium Bicarbonate", "Phosphate"],
        "notes": "Có thể kết tủa với bicarbonate và phosphate."
    }
}


# Drug interactions in ICU
ICU_DRUG_INTERACTIONS = {
    "Sedation + Vasopressor": {
        "drugs": ["Propofol/Midazolam + Norepinephrine/Epinephrine"],
        "interaction": "An thần có thể gây hạ huyết áp, cần tăng liều vasopressor",
        "severity": "Moderate",
        "management": "Theo dõi MAP sát, điều chỉnh liều phù hợp"
    },
    "Antibiotic + Sedation": {
        "drugs": ["Vancomycin/Piperacillin + Propofol"],
        "interaction": "Không có tương tác dược lý trực tiếp, nhưng cần theo dõi chức năng thận",
        "severity": "Low",
        "management": "Theo dõi creatinine, điều chỉnh liều nếu suy thận"
    },
    "Vasopressor + Inotrope": {
        "drugs": ["Norepinephrine + Dobutamine"],
        "interaction": "Có thể dùng cùng để hỗ trợ cả MAP và CO",
        "severity": "None",
        "management": "Theo dõi MAP, CO, HR"
    },
    "Opioid + Benzodiazepine": {
        "drugs": ["Fentanyl/Morphine + Midazolam"],
        "interaction": "Tăng tác dụng an thần, giảm thông khí",
        "severity": "High",
        "management": "Giảm liều từng thuốc, theo dõi RR, SpO2"
    },
    "Propofol + Opioid": {
        "drugs": ["Propofol + Fentanyl/Morphine"],
        "interaction": "Tăng tác dụng an thần",
        "severity": "Moderate",
        "management": "Theo dõi RASS, điều chỉnh liều"
    }
}


def check_y_site_compatibility(drug1: str, drug2: str) -> dict:
    """Check Y-site compatibility between two drugs"""
    if drug1 not in Y_SITE_COMPATIBILITY or drug2 not in Y_SITE_COMPATIBILITY:
        return {
            "compatible": None,
            "message": "Một hoặc cả hai thuốc không có trong database",
            "notes": "Vui lòng tham khảo tài liệu hoặc dược sĩ"
        }
    
    drug1_info = Y_SITE_COMPATIBILITY[drug1]
    drug2_info = Y_SITE_COMPATIBILITY[drug2]
    
    # Check if compatible
    if drug2 in drug1_info.get("compatible", []):
        return {
            "compatible": True,
            "message": f"✅ {drug1} và {drug2} TƯƠNG THÍCH qua Y-site",
            "notes": f"{drug1_info.get('notes', '')} {drug2_info.get('notes', '')}"
        }
    
    # Check if incompatible
    if drug2 in drug1_info.get("incompatible", []) or drug1 in drug2_info.get("incompatible", []):
        return {
            "compatible": False,
            "message": f"❌ {drug1} và {drug2} KHÔNG TƯƠNG THÍCH qua Y-site",
            "notes": "Không được trộn hoặc dùng chung Y-site. Dùng đường truyền riêng."
        }
    
    # Unknown compatibility
    return {
        "compatible": None,
        "message": f"⚠️ Chưa có dữ liệu về tính tương thích giữa {drug1} và {drug2}",
        "notes": "Khuyến nghị: Dùng đường truyền riêng để an toàn"
    }


def check_drug_interactions(drugs: list) -> list:
    """Check for drug interactions in ICU setting"""
    interactions = []
    
    # Check known interactions
    for interaction_type, info in ICU_DRUG_INTERACTIONS.items():
        # Simple check - in real implementation would be more sophisticated
        for drug_pair in info["drugs"]:
            if any(drug in drug_pair for drug in drugs):
                interactions.append({
                    "type": interaction_type,
                    "drugs": info["drugs"],
                    "interaction": info["interaction"],
                    "severity": info["severity"],
                    "management": info["management"]
                })
    
    return interactions


def render_y_site_checker():
    """Render Y-site compatibility checker"""
    st.subheader("💉 Kiểm tra tương thích Y-site")
    st.caption("Kiểm tra xem hai thuốc có thể dùng chung Y-site không")
    
    st.markdown("""
    **Y-site compatibility** là khả năng hai thuốc có thể truyền qua cùng một Y-site 
    mà không gây kết tủa, mất tác dụng, hoặc phản ứng bất lợi.
    """)
    
    st.markdown("---")
    
    # Drug selection
    available_drugs = sorted(list(Y_SITE_COMPATIBILITY.keys()))
    
    col1, col2 = st.columns(2)
    
    with col1:
        drug1 = st.selectbox("Thuốc 1:", available_drugs, key="compat_drug1")
    
    with col2:
        drug2 = st.selectbox("Thuốc 2:", available_drugs, key="compat_drug2")
    
    if drug1 == drug2:
        st.warning("⚠️ Vui lòng chọn hai thuốc khác nhau")
    else:
        # Check compatibility
        result = check_y_site_compatibility(drug1, drug2)
        
        st.markdown("---")
        
        # Display result
        if result["compatible"] is True:
            st.success(result["message"])
        elif result["compatible"] is False:
            st.error(result["message"])
        else:
            st.warning(result["message"])
        
        if result.get("notes"):
            st.info(f"**Ghi chú:** {result['notes']}")
        
        # Display drug information
        st.markdown("---")
        st.markdown("### 📋 Thông tin thuốc")
        
        col1, col2 = st.columns(2)
        
        with col1:
            drug1_info = Y_SITE_COMPATIBILITY[drug1]
            st.markdown(f"#### {drug1}")
            st.markdown(f"**Tương thích với:** {', '.join(drug1_info.get('compatible', [])) or 'Không có'}")
            st.markdown(f"**Không tương thích với:** {', '.join(drug1_info.get('incompatible', [])) or 'Không có'}")
            if drug1_info.get('notes'):
                st.caption(drug1_info['notes'])
        
        with col2:
            drug2_info = Y_SITE_COMPATIBILITY[drug2]
            st.markdown(f"#### {drug2}")
            st.markdown(f"**Tương thích với:** {', '.join(drug2_info.get('compatible', [])) or 'Không có'}")
            st.markdown(f"**Không tương thích với:** {', '.join(drug2_info.get('incompatible', [])) or 'Không có'}")
            if drug2_info.get('notes'):
                st.caption(drug2_info['notes'])


def render_compatibility_matrix():
    """Render compatibility matrix"""
    st.subheader("📊 Bảng tương thích")
    st.caption("Xem tất cả các thuốc tương thích và không tương thích")
    
    # Create matrix
    drugs = sorted(list(Y_SITE_COMPATIBILITY.keys()))
    
    # Display as expandable sections
    for drug in drugs:
        with st.expander(drug):
            drug_info = Y_SITE_COMPATIBILITY[drug]
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**✅ Tương thích:**")
                if drug_info.get('compatible'):
                    for compat_drug in drug_info['compatible']:
                        st.markdown(f"- {compat_drug}")
                else:
                    st.markdown("*Không có*")
            
            with col2:
                st.markdown("**❌ Không tương thích:**")
                if drug_info.get('incompatible'):
                    for incompat_drug in drug_info['incompatible']:
                        st.markdown(f"- {incompat_drug}")
                else:
                    st.markdown("*Không có*")
            
            if drug_info.get('notes'):
                st.info(f"**Ghi chú:** {drug_info['notes']}")


def render_drug_interactions():
    """Render drug interactions checker"""
    st.subheader("🔗 Kiểm tra tương tác thuốc")
    st.caption("Kiểm tra tương tác thuốc trong ICU")
    
    st.markdown("---")
    
    # Drug selection (multiple)
    available_drugs = []
    for interaction_info in ICU_DRUG_INTERACTIONS.values():
        for drug_pair in interaction_info["drugs"]:
            # Extract drug names (simplified)
            drugs_in_pair = drug_pair.split(" + ")
            available_drugs.extend(drugs_in_pair)
    
    available_drugs = sorted(list(set(available_drugs)))
    
    selected_drugs = st.multiselect(
        "Chọn thuốc đang dùng:",
        available_drugs,
        key="interaction_drugs"
    )
    
    if selected_drugs:
        # Check interactions
        interactions = check_drug_interactions(selected_drugs)
        
        if interactions:
            st.markdown("### 🚨 Tương tác thuốc phát hiện")
            
            for interaction in interactions:
                severity_color = {
                    "High": "error",
                    "Moderate": "warning",
                    "Low": "info",
                    "None": "success"
                }.get(interaction["severity"], "info")
                
                if interaction["severity"] == "High":
                    render_error_alert(
                        f"**{interaction['type']}:** {interaction['interaction']}",
                        f"**Quản lý:** {interaction['management']}"
                    )
                elif interaction["severity"] == "Moderate":
                    render_warning_alert(
                        f"**{interaction['type']}:** {interaction['interaction']}",
                        f"**Quản lý:** {interaction['management']}"
                    )
                else:
                    render_info_alert(
                        f"**{interaction['type']}:** {interaction['interaction']}",
                        f"**Quản lý:** {interaction['management']}"
                    )
        else:
            st.success("✅ Không phát hiện tương tác thuốc đáng kể")
    
    st.markdown("---")
    
    # Display known interactions
    st.markdown("### 📋 Tương tác thuốc thường gặp trong ICU")
    
    for interaction_type, info in ICU_DRUG_INTERACTIONS.items():
        with st.expander(interaction_type):
            st.markdown(f"**Thuốc:** {', '.join(info['drugs'])}")
            st.markdown(f"**Tương tác:** {info['interaction']}")
            st.markdown(f"**Mức độ:** {info['severity']}")
            st.markdown(f"**Quản lý:** {info['management']}")


def render_drug_compatibility():
    """Main function to render drug compatibility checker"""
    st.header("💉 Kiểm tra tương thích thuốc")
    st.caption("Y-site compatibility và tương tác thuốc trong ICU")
    
    tabs = st.tabs([
        "💉 Y-site Compatibility",
        "📊 Bảng tương thích",
        "🔗 Tương tác thuốc"
    ])
    
    with tabs[0]:
        render_y_site_checker()
    
    with tabs[1]:
        render_compatibility_matrix()
    
    with tabs[2]:
        render_drug_interactions()
