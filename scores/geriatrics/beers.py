"""
Beers Criteria
Potentially Inappropriate Medications in Older Adults
AGS Beers Criteria 2023
"""

import streamlit as st

def render_beers(score_id: str = "Beers Criteria"):
    """Render Beers Criteria checker"""
    
    st.markdown("### Beers Criteria")
    st.markdown("**Potentially Inappropriate Medications in Older Adults**")
    st.info("""
    **AGS Beers Criteria 2023** liệt kê các thuốc có thể không phù hợp với bệnh nhân cao tuổi (≥65 tuổi).
    
    **Mục đích:** Giảm nguy cơ adverse drug reactions và cải thiện an toàn thuốc ở elderly.
    """)
    
    st.markdown("---")
    
    # Common PIMs
    st.markdown("#### Các thuốc thường gặp trong Beers Criteria")
    
    beers_categories = {
        "Anticholinergics": {
            "drugs": ["Diphenhydramine", "Chlorpheniramine", "Promethazine", "Hydroxyzine"],
            "concern": "Cognitive impairment, delirium, constipation, urinary retention",
            "severity": "High"
        },
        "Benzodiazepines": {
            "drugs": ["Diazepam", "Lorazepam", "Alprazolam", "Clonazepam", "Temazepam"],
            "concern": "Delirium, falls, fractures, motor vehicle accidents",
            "severity": "High"
        },
        "NSAIDs (Non-COX-2 selective)": {
            "drugs": ["Ibuprofen", "Naproxen", "Diclofenac", "Ketorolac"],
            "concern": "GI bleeding, peptic ulcer, AKI, hypertension",
            "severity": "High"
        },
        "Sulfonylureas (long-acting)": {
            "drugs": ["Chlorpropamide", "Glyburide (glibenclamide)"],
            "concern": "Prolonged hypoglycemia",
            "severity": "High"
        },
        "Antipsychotics": {
            "drugs": ["Haloperidol", "Risperidone", "Olanzapine", "Quetiapine"],
            "concern": "Delirium, falls, stroke risk (in dementia)",
            "severity": "High"
        },
        "Antiplatelet (dipyridamole)": {
            "drugs": ["Dipyridamole"],
            "concern": "Syncope, orthostatic hypotension",
            "severity": "Moderate"
        },
        "Alpha-1 blockers": {
            "drugs": ["Prazosin", "Doxazosin", "Terazosin"],
            "concern": "Orthostatic hypotension, syncope",
            "severity": "High"
        },
        "Tricyclic antidepressants": {
            "drugs": ["Amitriptyline", "Imipramine", "Doxepin (>6mg/day)"],
            "concern": "Anticholinergic effects, orthostatic hypotension",
            "severity": "High"
        }
    }
    
    # Drug search
    st.markdown("#### Tìm kiếm thuốc")
    drug_search = st.text_input(
        "Nhập tên thuốc để kiểm tra:",
        placeholder="Ví dụ: Diphenhydramine, Lorazepam...",
        key="beers_search"
    )
    
    if drug_search:
        drug_search_lower = drug_search.lower()
        found_drugs = []
        
        for category, info in beers_categories.items():
            for drug in info["drugs"]:
                if drug_search_lower in drug.lower():
                    found_drugs.append({
                        "drug": drug,
                        "category": category,
                        "concern": info["concern"],
                        "severity": info["severity"]
                    })
        
        if found_drugs:
            st.warning(f"⚠️ Tìm thấy {len(found_drugs)} thuốc trong Beers Criteria:")
            for item in found_drugs:
                with st.expander(f"❌ {item['drug']} - {item['category']}", expanded=True):
                    st.markdown(f"**Mức độ:** {item['severity']}")
                    st.markdown(f"**Mối quan tâm:** {item['concern']}")
                    st.markdown("**Khuyến nghị:** Tránh hoặc sử dụng thận trọng, cân nhắc thuốc thay thế")
        else:
            st.info("Không tìm thấy trong danh sách PIMs phổ biến. Vui lòng kiểm tra Beers Criteria đầy đủ.")
    
    st.markdown("---")
    
    # Display categories
    st.markdown("#### Các nhóm thuốc trong Beers Criteria")
    
    for category, info in beers_categories.items():
        with st.expander(f"⚠️ {category} ({info['severity']} risk)", expanded=False):
            st.markdown(f"**Thuốc:** {', '.join(info['drugs'])}")
            st.markdown(f"**Mối quan tâm:** {info['concern']}")
            st.markdown(f"**Mức độ rủi ro:** {info['severity']}")
    
    st.markdown("---")
    
    # Key principles
    st.markdown("#### Nguyên tắc chính")
    st.markdown("""
    1. **Tránh** các thuốc trong Beers Criteria khi có thể
    2. **Thay thế** bằng thuốc an toàn hơn
    3. **Điều chỉnh liều** nếu phải dùng
    4. **Theo dõi** adverse effects
    5. **Xem xét** ngưng thuốc không cần thiết (deprescribing)
    
    **Lưu ý:** Beers Criteria là hướng dẫn, không phải tuyệt đối. 
    Cần cân nhắc từng trường hợp cụ thể và goals of care.
    """)
    
    st.markdown("---")
    
    # References
    st.markdown("#### References")
    st.markdown("""
    - American Geriatrics Society 2023 updated AGS Beers Criteria for Potentially Inappropriate Medication Use in Older Adults. J Am Geriatr Soc. 2023;71(7):2052-2081.
    - 2023 AGS Beers Criteria. https://www.americangeriatrics.org
    """)
