"""
Side-by-Side Antibiotic Comparison
Compare 2-4 antibiotics side by side
"""

import streamlit as st
import pandas as pd
import html
from .antibiotics_data import ANTIBIOTICS_DATABASE
from .mic_breakpoints import get_common_susceptibility
from .resistance_patterns import get_antibiotic_resistance_summary


def render_comparison():
    """Render side-by-side antibiotic comparison interface"""
    
    st.markdown("""
    <div style='
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 30px 25px;
        border-radius: 20px;
        margin-bottom: 30px;
        text-align: center;
        box-shadow: 0 8px 24px rgba(102,126,234,0.25);
    '>
        <h1 style='margin: 0; color: white; font-size: 2.5em; font-weight: 700;'>📊 So Sánh Kháng Sinh</h1>
        <p style='margin: 12px 0 0 0; color: rgba(255,255,255,0.95); font-size: 1.15em;'>
            So sánh 2-4 kháng sinh: Liều dùng, Phổ tác dụng, AWaRe, Độ nhạy, Tác dụng phụ
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Antibiotic selection
    st.markdown("### 🔍 Chọn Kháng Sinh Để So Sánh:")
    
    available_antibiotics = sorted(list(ANTIBIOTICS_DATABASE.keys()))
    
    num_comparisons = st.slider(
        "Số lượng kháng sinh so sánh:",
        min_value=2,
        max_value=4,
        value=2,
        key="num_comparisons"
    )
    
    selected_antibiotics = []
    cols = st.columns(num_comparisons)
    
    for i in range(num_comparisons):
        with cols[i]:
            selected = st.selectbox(
                f"Kháng sinh {i+1}:",
                options=[""] + available_antibiotics,
                key=f"compare_ab_{i}",
                help="Chọn kháng sinh để so sánh"
            )
            if selected:
                selected_antibiotics.append(selected)
    
    if len(selected_antibiotics) < 2:
        st.info("👆 **Vui lòng chọn ít nhất 2 kháng sinh để so sánh**")
        return
    
    # Remove duplicates while preserving order
    selected_antibiotics = list(dict.fromkeys(selected_antibiotics))
    
    if len(selected_antibiotics) < 2:
        st.warning("⚠️ Vui lòng chọn ít nhất 2 kháng sinh khác nhau")
        return
    
    st.markdown("---")
    
    # Comparison table
    st.markdown("### 📋 Bảng So Sánh:")
    
    # Prepare comparison data
    comparison_data = []
    
    for ab_name in selected_antibiotics:
        if ab_name not in ANTIBIOTICS_DATABASE:
            continue
        
        ab_data = ANTIBIOTICS_DATABASE[ab_name]
        
        # Get dosage summary
        dosage = ab_data.get('dosage', {})
        dosage_summary = []
        if 'adult_standard' in dosage:
            dosage_summary.append(dosage['adult_standard'])
        elif 'adult_iv' in dosage:
            dosage_summary.append(dosage['adult_iv'])
        elif 'adult_iv_standard' in dosage:
            dosage_summary.append(dosage['adult_iv_standard'])
        dosage_str = "; ".join(dosage_summary[:2]) if dosage_summary else "Xem chi tiết"
        
        # Get indications summary
        indications = ab_data.get('indications', [])
        indications_str = ", ".join(indications[:3]) if indications else "N/A"
        if len(indications) > 3:
            indications_str += "..."
        
        # Get administration
        admin = ab_data.get('administration', [])
        admin_str = " / ".join(admin) if admin else "N/A"
        
        # Get AWaRe
        aware = ab_data.get('aware_classification', 'N/A')
        
        # Get common susceptibility
        suscept = get_common_susceptibility(ab_name)
        suscept_summary = []
        for org, pattern in list(suscept.items())[:2]:
            suscept_summary.append(f"{org}: {pattern}")
        suscept_str = "; ".join(suscept_summary) if suscept_summary else "Xem chi tiết"
        
        # Get side effects count
        side_effects = ab_data.get('side_effects', [])
        side_effects_str = f"{len(side_effects)} tác dụng phụ chính"
        
        comparison_data.append({
            "Kháng Sinh": ab_name,
            "Nhóm": ab_data.get('group', 'N/A'),
            "Đường Dùng": admin_str,
            "AWaRe": aware,
            "Liều Dùng": dosage_str,
            "Chỉ Định": indications_str,
            "Độ Nhạy": suscept_str,
            "Tác Dụng Phụ": side_effects_str
        })
    
    if comparison_data:
        df_comparison = pd.DataFrame(comparison_data)
        st.dataframe(df_comparison, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # Detailed comparison by category
    st.markdown("### 📊 So Sánh Chi Tiết:")
    
    comparison_tabs = st.tabs(["💉 Liều Dùng", "📋 Chỉ Định", "🦠 Độ Nhạy", "⚠️ Tác Dụng Phụ", "🫘 Điều Chỉnh Thận"])
    
    # Dosage comparison
    with comparison_tabs[0]:
        st.markdown("#### 💉 Liều Dùng:")
        for ab_name in selected_antibiotics:
            if ab_name not in ANTIBIOTICS_DATABASE:
                continue
            
            ab_data = ANTIBIOTICS_DATABASE[ab_name]
            dosage = ab_data.get('dosage', {})
            
            st.markdown(f"**{ab_name}:**")
            dosage_items = []
            for key in ['adult_standard', 'adult_iv', 'adult_iv_standard', 'adult_severe']:
                if key in dosage:
                    dosage_items.append(f"- {dosage[key]}")
            
            if dosage_items:
                for item in dosage_items[:3]:
                    st.markdown(item)
            else:
                st.caption("Xem chi tiết trong database")
            st.markdown("---")
    
    # Indications comparison
    with comparison_tabs[1]:
        st.markdown("#### 📋 Chỉ Định:")
        for ab_name in selected_antibiotics:
            if ab_name not in ANTIBIOTICS_DATABASE:
                continue
            
            ab_data = ANTIBIOTICS_DATABASE[ab_name]
            indications = ab_data.get('indications', [])
            
            st.markdown(f"**{ab_name}:**")
            if indications:
                for ind in indications:
                    st.markdown(f"- ✓ {ind}")
            else:
                st.caption("Không có dữ liệu")
            st.markdown("---")
    
    # Susceptibility comparison
    with comparison_tabs[2]:
        st.markdown("#### 🦠 Độ Nhạy Thường Gặp:")
        for ab_name in selected_antibiotics:
            if ab_name not in ANTIBIOTICS_DATABASE:
                continue
            
            suscept = get_common_susceptibility(ab_name)
            
            st.markdown(f"**{ab_name}:**")
            if suscept:
                for org, pattern in suscept.items():
                    # Color code
                    color = "#FF9800"  # Default
                    try:
                        if "S (" in pattern:
                            # Extract percentage from "S (XX%)" or "S (XX-YY%)"
                            s_part = pattern.split("S (")[1].split("%")[0]
                            # Handle range like "95-98" -> take first value
                            s_val = float(s_part.split("-")[0].strip())
                            if s_val >= 80:
                                color = "#4CAF50"
                        elif "R (" in pattern:
                            # Extract percentage from "R (XX%)" or "R (XX-YY%)"
                            r_part = pattern.split("R (")[1].split("%")[0]
                            # Handle range like "60-70" -> take first value
                            r_val = float(r_part.split("-")[0].strip())
                            if r_val >= 50:
                                color = "#F44336"
                    except (ValueError, IndexError, AttributeError):
                        # If parsing fails, use default color
                        color = "#FF9800"
                    
                    st.markdown(f"""
                    <div style='padding: 6px 10px; margin: 4px 0; background: rgba(25,118,210,0.05); border-left: 3px solid {color}; border-radius: 6px;'>
                        <strong>{org}:</strong> <span style='color: {color}; font-weight: 600;'>{pattern}</span>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.caption("Xem chi tiết trong database")
            st.markdown("---")
    
    # Side effects comparison
    with comparison_tabs[3]:
        st.markdown("#### ⚠️ Tác Dụng Phụ:")
        for ab_name in selected_antibiotics:
            if ab_name not in ANTIBIOTICS_DATABASE:
                continue
            
            ab_data = ANTIBIOTICS_DATABASE[ab_name]
            side_effects = ab_data.get('side_effects', [])
            
            st.markdown(f"**{ab_name}:**")
            if side_effects:
                for se in side_effects:
                    st.markdown(f"- ⚠️ {se}")
            else:
                st.caption("Không có dữ liệu")
            st.markdown("---")
    
    # Renal adjustment comparison
    with comparison_tabs[4]:
        st.markdown("#### 🫘 Điều Chỉnh Theo Chức Năng Thận:")
        for ab_name in selected_antibiotics:
            if ab_name not in ANTIBIOTICS_DATABASE:
                continue
            
            ab_data = ANTIBIOTICS_DATABASE[ab_name]
            renal = ab_data.get('renal_adjustment', {})
            
            st.markdown(f"**{ab_name}:**")
            if renal:
                renal_data = []
                if 'normal' in renal:
                    renal_data.append({"CrCl": "≥ 60", "Điều chỉnh": renal['normal']})
                if '30_60' in renal:
                    renal_data.append({"CrCl": "30-60", "Điều chỉnh": renal['30_60']})
                if '15_30' in renal:
                    renal_data.append({"CrCl": "15-30", "Điều chỉnh": renal['15_30']})
                if 'under_15' in renal:
                    renal_data.append({"CrCl": "< 15", "Điều chỉnh": renal['under_15']})
                
                if renal_data:
                    df_renal = pd.DataFrame(renal_data)
                    st.dataframe(df_renal, use_container_width=True, hide_index=True)
            else:
                st.caption("Không cần điều chỉnh hoặc không có dữ liệu")
            st.markdown("---")
    
    # Quick actions
    st.markdown("---")
    st.markdown("### ⚡ Thao Tác Nhanh:")
    action_cols = st.columns(len(selected_antibiotics))
    
    for idx, ab_name in enumerate(selected_antibiotics):
        with action_cols[idx]:
            if st.button(f"📖 Chi tiết {ab_name}", key=f"compare_detail_{ab_name}", use_container_width=True):
                st.session_state['view_antibiotic'] = ab_name
                st.rerun()

