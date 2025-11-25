"""
Antibiotic Database - Export Functions
Export antibiotic information to text files
"""

import streamlit as st
from datetime import datetime
import html

def _render_antibiotic_export(ab_name, ab_data):
    """Render export section for antibiotic information"""
    from datetime import datetime
    import html
    
    lines = []
    lines.append("=" * 70)
    lines.append(f"THÔNG TIN KHÁNG SINH - {ab_name}")
    lines.append("=" * 70)
    lines.append(f"Ngày xuất: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("-" * 70)
    
    # Basic info
    lines.append(f"\n📋 THÔNG TIN CƠ BẢN:")
    if 'vietnamese_name' in ab_data:
        lines.append(f"  Tên biệt dược: {ab_data['vietnamese_name']}")
    if 'group' in ab_data:
        lines.append(f"  Nhóm: {ab_data['group']}")
    if 'administration' in ab_data:
        lines.append(f"  Đường dùng: {', '.join(ab_data['administration'])}")
    if 'aware_classification' in ab_data:
        lines.append(f"  AWaRe: {ab_data['aware_classification']}")
    
    # Indications
    if 'indications' in ab_data:
        lines.append(f"\n📋 CHỈ ĐỊNH:")
        for ind in ab_data['indications']:
            lines.append(f"  • {ind}")
    
    # Contraindications
    if 'contraindications' in ab_data:
        lines.append(f"\n⛔ CHỐNG CHỈ ĐỊNH:")
        for contr in ab_data['contraindications']:
            lines.append(f"  • {contr}")
    
    # Dosage
    if 'dosage' in ab_data:
        lines.append(f"\n💉 LIỀU DÙNG:")
        dosage = ab_data['dosage']
        if 'adult_iv' in dosage:
            lines.append(f"  IV: {dosage['adult_iv']}")
        if 'adult_im' in dosage:
            lines.append(f"  IM: {dosage['adult_im']}")
        if 'adult_po' in dosage:
            lines.append(f"  PO: {dosage['adult_po']}")
        if 'adult_standard' in dosage:
            lines.append(f"  Liều chuẩn: {dosage['adult_standard']}")
        if 'adult_severe' in dosage:
            lines.append(f"  Nhiễm khuẩn nặng: {dosage['adult_severe']}")
        if 'pediatric_iv' in dosage:
            lines.append(f"  Trẻ em (IV): {dosage['pediatric_iv']}")
    
    # Renal adjustment
    if 'renal_adjustment' in ab_data:
        lines.append(f"\n🫘 ĐIỀU CHỈNH THEO CHỨC NĂNG THẬN:")
        renal = ab_data['renal_adjustment']
        if 'normal' in renal:
            lines.append(f"  CrCl ≥ 60: {renal['normal']}")
        if '30_60' in renal:
            lines.append(f"  CrCl 30-60: {renal['30_60']}")
        if '15_30' in renal:
            lines.append(f"  CrCl 15-30: {renal['15_30']}")
        if 'under_15' in renal:
            lines.append(f"  CrCl < 15: {renal['under_15']}")
    
    # Side effects
    if 'side_effects' in ab_data:
        lines.append(f"\n⚠️ TÁC DỤNG PHỤ:")
        for se in ab_data['side_effects']:
            lines.append(f"  • {se}")
    
    # Monitoring
    if 'monitoring' in ab_data:
        lines.append(f"\n📊 THEO DÕI: {ab_data['monitoring']}")
    
    # Interactions
    if 'interactions' in ab_data:
        lines.append(f"\n🔗 TƯƠNG TÁC THUỐC:")
        for inter in ab_data['interactions']:
            lines.append(f"  • {inter}")
    
    # Pregnancy
    if 'pregnancy' in ab_data:
        lines.append(f"\n🤰 AN TOÀN THAI KỲ: {ab_data['pregnancy']}")
    
    lines.append("\n" + "=" * 70)
    lines.append("⚠️ Lưu ý: Thông tin chỉ mang tính tham khảo")
    lines.append("   Không thay thế đánh giá lâm sàng của bác sĩ")
    lines.append("=" * 70)
    
    export_text = "\n".join(lines)
    
    with st.expander("📤 Export Thông Tin", expanded=True):
        st.markdown("**Preview:**")
        st.code(export_text, language="text")
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        with col1:
            st.code(export_text, language="text")
            st.success("✅ Chọn và copy text từ khung trên để copy vào clipboard")
        
        with col2:
            # Sanitize ab_name for filename and key
            safe_filename = str(ab_name).replace(' ', '_').replace('-', '_').replace('/', '_')
            safe_download_key = f"download_{safe_filename}"
            filename = f"antibiotic_{safe_filename}"
            st.download_button(
                label="💾 Tải TXT",
                data=export_text,
                file_name=f"{filename}.txt",
                mime="text/plain",
                use_container_width=True,
                key=safe_download_key
            )



