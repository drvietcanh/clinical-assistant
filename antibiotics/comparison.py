"""
Side-by-Side Antibiotic Comparison
Compare 2-4 antibiotics side by side
"""

import streamlit as st
import pandas as pd
import html
from datetime import datetime
from .antibiotics_data import ANTIBIOTICS_DATABASE
from .mic_breakpoints import get_common_susceptibility
from .resistance_patterns import get_antibiotic_resistance_summary
from .antibiogram import (
    get_antibiogram,
    get_available_hospitals,
    get_default_hospital_id,
    set_default_hospital_id,
)


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
        <h1 style='margin: 0; color: white; font-size: 2.5em; font-weight: 700;'>📊 So sánh kháng sinh</h1>
        <p style='margin: 12px 0 0 0; color: rgba(255,255,255,0.95); font-size: 1.15em;'>
            So sánh 2-4 kháng sinh: Liều dùng, Phổ tác dụng, AWaRe, Độ nhạy, Tác dụng phụ
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Antibiotic selection
    st.markdown("### 🔍 Chọn kháng sinh để so sánh:")
    
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
    
    # Antibiogram (Phase 1) - optional context for empiric choices
    with st.expander("🧫 Antibiogram theo bệnh viện (tham khảo nhanh)", expanded=False):
        hospitals = get_available_hospitals()
        default_hospital = get_default_hospital_id(hospitals)
        hospital_id = st.selectbox(
            "Chọn bệnh viện",
            options=list(hospitals.keys()),
            format_func=lambda k: hospitals.get(k, k),
            index=list(hospitals.keys()).index(default_hospital),
            key="compare_antibiogram_hospital",
        )
        set_default_hospital_id(hospital_id)
        metric = st.radio(
            "Chỉ số hiển thị",
            options=["S (%)", "I (%)", "R (%)"],
            horizontal=True,
            key="compare_antibiogram_metric",
        )
        abg = get_antibiogram(hospital_id)
        # Build table focusing on selected antibiotics
        organisms = sorted(abg.keys())
        cols_to_show = selected_antibiotics[:4]  # limit width
        rows = []
        for org in organisms:
            row = {"Vi khuẩn": org}
            for ab in cols_to_show:
                entry = abg.get(org, {}).get(ab)
                row[ab] = entry.as_dict().get(metric) if entry else None
            rows.append(row)
        if rows and cols_to_show:
            df_abg = pd.DataFrame(rows)
            st.dataframe(df_abg, use_container_width=True, hide_index=True)
        else:
            st.caption("Chọn kháng sinh để xem độ nhạy theo antibiogram của BV.")
    
    st.markdown("---")
    
    # Comparison table
    st.markdown("### 📋 Bảng so sánh:")
    
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
            "Kháng sinh": ab_name,
            "Nhóm": ab_data.get('group', 'N/A'),
            "Đường Dùng": admin_str,
            "AWaRe": aware,
            "Liều dùng": dosage_str,
            "Chỉ định": indications_str,
            "Độ nhạy": suscept_str,
            "Tác dụng phụ": side_effects_str
        })
    
    if comparison_data:
        df_comparison = pd.DataFrame(comparison_data)
        st.dataframe(df_comparison, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # Visual comparison (if available)
    # Visual comparison (Phase 4 - Enhanced)
    try:
        from .visual_comparison import (
            render_spectrum_chart,
            render_dosing_comparison_chart,
            render_side_effects_heatmap
        )
        
        st.markdown("---")
        st.markdown("### 📊 So Sánh Trực Quan")
        
        # Prepare data for visual comparison
        visual_comparison_data = []
        for ab_name in selected_antibiotics:
            if ab_name not in ANTIBIOTICS_DATABASE:
                continue
            
            ab_data = ANTIBIOTICS_DATABASE[ab_name]
            visual_comparison_data.append({
                'name': ab_name,
                'dose': ab_data.get('dosage', {}).get('adult_standard', 'N/A') if isinstance(ab_data.get('dosage'), dict) else str(ab_data.get('dosage', 'N/A')),
                'frequency': 'N/A',  # Will be extracted if available
                'route': ' / '.join(ab_data.get('administration', [])) if ab_data.get('administration') else 'N/A',
                'spectrum': ab_data.get('spectrum', []),
                'side_effects': ab_data.get('side_effects', []),
                'notes': ab_data.get('notes', 'N/A')
            })
        
        if visual_comparison_data:
            # Create tabs for visual comparisons
            visual_tabs = st.tabs([
                "📊 Phổ Tác Dụng",
                "💉 Liều Dùng",
                "⚠️ Tác Dụng Phụ"
            ])
            
            with visual_tabs[0]:
                render_spectrum_chart(visual_comparison_data, selected_antibiotics)
            
            with visual_tabs[1]:
                render_dosing_comparison_chart(visual_comparison_data, selected_antibiotics)
            
            with visual_tabs[2]:
                render_side_effects_heatmap(visual_comparison_data, selected_antibiotics)
    except ImportError as e:
        st.info(f"💡 Tính năng so sánh trực quan sẽ được cải thiện trong phiên bản tương lai. ({e})")
    
    st.markdown("---")
    
    # Detailed comparison by category
    st.markdown("### 📊 So sánh chi tiết:")
    
    comparison_tabs = st.tabs(["💉 Liều dùng", "📋 Chỉ định", "🦠 Độ nhạy", "⚠️ Tác dụng phụ", "🫘 Điều chỉnh thận"])
    
    # Dosage comparison
    with comparison_tabs[0]:
        st.markdown("#### 💉 Liều dùng:")
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
        st.markdown("#### 📋 Chỉ định:")
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
        st.markdown("#### 🦠 Độ nhạy Thường gặp:")
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
        st.markdown("#### ⚠️ Tác dụng phụ:")
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
        st.markdown("#### 🫘 Điều chỉnh Theo Chức Năng Thận:")
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
    
    # Visual comparison charts
    st.markdown("---")
    try:
        from .visual_comparison import render_visual_comparison_tabs
        
        # Prepare comparison data for visual charts
        visual_comparison_data = []
        for ab_name in selected_antibiotics:
            if ab_name not in ANTIBIOTICS_DATABASE:
                continue
            visual_comparison_data.append(ANTIBIOTICS_DATABASE[ab_name])
        
        render_visual_comparison_tabs(visual_comparison_data, selected_antibiotics)
    except ImportError as e:
        st.info("💡 Tính năng so sánh trực quan đang được cập nhật")
    
    # Export buttons
    st.markdown("---")
    st.markdown("### 📥 Xuất Kết Quả So Sánh")
    try:
        from .export import render_export_buttons
        
        # Prepare comparison data for export
        comparison_data = []
        for ab_name in selected_antibiotics:
            if ab_name not in ANTIBIOTICS_DATABASE:
                continue
            
            ab_data = ANTIBIOTICS_DATABASE[ab_name]
            comparison_data.append({
                'name': ab_name,
                'dose': ab_data.get('dosing', {}).get('adult', 'N/A') if isinstance(ab_data.get('dosing'), dict) else str(ab_data.get('dosing', 'N/A')),
                'frequency': 'N/A',  # Will be extracted from dosing if available
                'spectrum': ', '.join(ab_data.get('spectrum', [])) if ab_data.get('spectrum') else 'N/A',
                'notes': ab_data.get('notes', 'N/A')
            })
        
        export_data = {
            'comparison_data': comparison_data,
            'drugs': selected_antibiotics
        }
        
        render_export_buttons(
            content_type='comparison',
            content_data=export_data,
            title=f"So Sánh Kháng Sinh - {', '.join(selected_antibiotics)}",
            filename=f"comparison_{'_'.join([ab.replace(' ', '_') for ab in selected_antibiotics])}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        )
    except ImportError:
        st.info("💡 Tính năng xuất sẽ được thêm trong phiên bản tương lai")
    
    # Quick actions
    st.markdown("---")
    st.markdown("### ⚡ Thao Tác Nhanh:")
    action_cols = st.columns(len(selected_antibiotics))
    
    for idx, ab_name in enumerate(selected_antibiotics):
        with action_cols[idx]:
            if st.button(f"📖 Chi tiết {ab_name}", key=f"compare_detail_{ab_name}", use_container_width=True):
                st.session_state['view_antibiotic'] = ab_name
                st.rerun()

