"""
Visual Drug Comparison
Side-by-side comparison of multiple drugs with visual charts
Enhanced version for general drugs (beyond antibiotics)
"""

import streamlit as st
import pandas as pd
from .drug_database import DRUG_DATABASE
from .search import search_drugs


def render_visual_comparison():
    """Render visual drug comparison interface"""
    
    st.markdown("""
    <div style='
        background: linear-gradient(135deg, #9C27B0 0%, #7B1FA2 100%);
        color: white;
        padding: 25px;
        border-radius: 15px;
        margin-bottom: 25px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    '>
        <h1 style='margin: 0; color: white; font-size: 2.2em;'>📊 So sánh Thuốc Trực Quan</h1>
        <p style='margin: 10px 0 0 0; color: rgba(255,255,255,0.9); font-size: 1.1em;'>
            So sánh nhiều thuốc trong bảng/grid • Visual charts • Side-by-side comparison
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("""
    **Công cụ này giúp:**
    - ✅ So sánh nhiều thuốc cùng lúc trong bảng
    - ✅ So sánh chỉ định, tác dụng phụ, tương tác
    - ✅ So sánh đường dùng và liều dùng
    - ✅ Chọn thuốc phù hợp nhất
    """)
    
    st.markdown("---")
    
    # Drug selection
    st.markdown("### 💊 Chọn Thuốc Để So sánh")
    
    all_drugs = sorted(list(DRUG_DATABASE.keys()))
    
    selected_drugs = st.multiselect(
        "Chọn thuốc (có thể chọn nhiều):",
        all_drugs,
        default=[],
        key="visual_selected_drugs",
        help="Chọn từ 2-5 thuốc để so sánh"
    )
    
    if len(selected_drugs) < 2:
        st.info("👆 Chọn ít nhất 2 thuốc để bắt đầu so sánh")
        
        st.markdown("### 💡 Gợi ý các phối hợp thường dùng:")
        suggestions = {
            "ACE Inhibitors": ["Captopril", "Enalapril", "Lisinopril"],
            "Beta-blockers": ["Metoprolol", "Propranolol"],
            "PPIs": ["Omeprazole", "Pantoprazole"],
            "Analgesics": ["Paracetamol", "Ibuprofen", "Tramadol"],
            "Statins": ["Atorvastatin", "Simvastatin"]
        }
        
        for combo_name, combo_drugs in suggestions.items():
            if st.button(f"📋 {combo_name}: {', '.join(combo_drugs)}", key=f"visual_suggest_{combo_name}", use_container_width=True):
                st.session_state['visual_selected_drugs'] = combo_drugs
                st.rerun()
        return
    
    if len(selected_drugs) > 5:
        st.warning("⚠️ Chọn quá nhiều thuốc (max 5). Sẽ chỉ hiển thị 5 thuốc đầu tiên.")
        selected_drugs = selected_drugs[:5]
    
    st.markdown("---")
    
    # Comparison table
    if st.button("📊 So sánh", type="primary", use_container_width=True):
        comparison_data = []
        
        for drug_name in selected_drugs:
            if drug_name not in DRUG_DATABASE:
                continue
            
            drug_data = DRUG_DATABASE[drug_name]
            
            # Get key information
            group = drug_data.get('group', 'Unknown')
            vn_name = drug_data.get('vietnamese_name', '')
            admin = ", ".join(drug_data.get('administration', []))
            indications = ", ".join(drug_data.get('indications', [])[:3])  # First 3
            contraindications = ", ".join(drug_data.get('contraindications', [])[:2])  # First 2
            side_effects_count = len(drug_data.get('side_effects', []))
            interactions_count = len(drug_data.get('interactions', []))
            pregnancy = drug_data.get('pregnancy', 'N/A')
            
            # Get dosage summary
            dosage_summary = "N/A"
            if 'dosage' in drug_data:
                dosage = drug_data['dosage']
                if 'adult_standard' in dosage:
                    dosage_summary = dosage['adult_standard']
                elif 'adult_po' in dosage:
                    dosage_summary = dosage['adult_po']
                elif 'adult_htn' in dosage:
                    dosage_summary = dosage['adult_htn']
                elif len(dosage) > 0:
                    # Get first dosage entry
                    first_key = list(dosage.keys())[0]
                    dosage_summary = dosage[first_key]
            
            comparison_data.append({
                "Thuốc": drug_name,
                "Tên biệt dược": vn_name[:30] + "..." if len(vn_name) > 30 else vn_name,
                "Nhóm": group.split(" - ")[-1] if " - " in group else group,
                "Đường dùng": admin,
                "Liều dùng": dosage_summary[:50] + "..." if len(str(dosage_summary)) > 50 else str(dosage_summary),
                "Chỉ định": indications[:50] + "..." if len(indications) > 50 else indications,
                "Tác dụng phụ": f"{side_effects_count} items",
                "Tương tác": f"{interactions_count} items",
                "Thai kỳ": pregnancy
            })
        
        # Display comparison table
        st.markdown("### 📊 Bảng so sánh")
        df = pd.DataFrame(comparison_data)
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        st.markdown("---")
        
        # Side-by-side detailed comparison
        st.markdown("### 📋 So sánh chi tiết từng thuốc:")
        
        cols = st.columns(min(len(selected_drugs), 3))
        
        for idx, drug_name in enumerate(selected_drugs):
            col_idx = idx % 3
            with cols[col_idx]:
                drug_data = DRUG_DATABASE[drug_name]
                
                # Card header
                group = drug_data.get('group', 'Unknown')
                group_color = "#1976D2"
                if "Cardiovascular" in group:
                    group_color = "#E91E63"
                elif "Diabetes" in group:
                    group_color = "#9C27B0"
                elif "Gastrointestinal" in group:
                    group_color = "#FF9800"
                elif "Analgesic" in group:
                    group_color = "#F44336"
                
                st.markdown(f"""
                <div style='background: linear-gradient(135deg, {group_color} 0%, {group_color}dd 100%); color: white; padding: 15px; border-radius: 10px; margin: 10px 0;'>
                    <h3 style='margin: 0; color: white; font-size: 1.2em;'>💊 {drug_name}</h3>
                    <p style='margin: 5px 0 0 0; font-size: 0.9em; opacity: 0.9;'>{group.split(' - ')[-1] if ' - ' in group else group}</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Key info
                if 'vietnamese_name' in drug_data:
                    st.caption(f"**Tên biệt dược:** {drug_data['vietnamese_name']}")
                
                if 'administration' in drug_data:
                    st.caption(f"**Đường dùng:** {', '.join(drug_data['administration'])}")
                
                # Dosage
                if 'dosage' in drug_data:
                    dosage = drug_data['dosage']
                    dosage_keys = list(dosage.keys())
                    if dosage_keys:
                        first_dose_key = dosage_keys[0]
                        st.info(f"**Liều:** {dosage[first_dose_key]}")
                
                # Indications (first 2)
                if 'indications' in drug_data:
                    inds = drug_data['indications'][:2]
                    st.write("**Chỉ định:**")
                    for ind in inds:
                        st.write(f"- {ind}")
                
                # Side effects count
                if 'side_effects' in drug_data:
                    st.warning(f"⚠️ {len(drug_data['side_effects'])} tác dụng phụ")
                
                # Pregnancy
                if 'pregnancy' in drug_data:
                    preg = drug_data['pregnancy']
                    preg_icons = {"A": "🟢", "B": "🟡", "C": "🟠", "D": "🔴", "X": "⚫"}
                    st.write(f"**Thai kỳ:** {preg_icons.get(preg, '')} {preg}")
        
        st.markdown("---")
        
        # Comparison by category
        st.markdown("### 📈 So sánh Theo Tiêu chí:")
        
        # Side effects comparison
        side_effects_data = {
            "Thuốc": selected_drugs,
            "Số tác dụng phụ": [len(DRUG_DATABASE[d].get('side_effects', [])) for d in selected_drugs]
        }
        df_se = pd.DataFrame(side_effects_data)
        st.bar_chart(df_se.set_index("Thuốc"))
        
        # Interactions comparison
        interactions_data = {
            "Thuốc": selected_drugs,
            "Số tương tác": [len(DRUG_DATABASE[d].get('interactions', [])) for d in selected_drugs]
        }
        df_int = pd.DataFrame(interactions_data)
        st.bar_chart(df_int.set_index("Thuốc"))
        
        # Summary recommendations
        st.markdown("---")
        st.markdown("### 💡 Tóm tắt & khuyến cáo:")
        
        # Find safest (fewest side effects)
        side_effect_counts = {d: len(DRUG_DATABASE[d].get('side_effects', [])) for d in selected_drugs}
        safest = min(side_effect_counts.items(), key=lambda x: x[1])
        st.success(f"✅ **Ít tác dụng phụ nhất:** {safest[0]} ({safest[1]} tác dụng phụ)")
        
        # Find most interactions
        interaction_counts = {d: len(DRUG_DATABASE[d].get('interactions', [])) for d in selected_drugs}
        most_interactions = max(interaction_counts.items(), key=lambda x: x[1])
        st.warning(f"⚠️ **Nhiều tương tác nhất:** {most_interactions[0]} ({most_interactions[1]} tương tác)")

