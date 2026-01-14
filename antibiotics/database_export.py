"""
Antibiotic Database - Export Functions
Export antibiotic information to text, HTML, and structured formats
Enhanced with better formatting (Phase 2)
"""

import streamlit as st
from datetime import datetime
import html
import json

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
    
    return export_text


def _generate_html_export(ab_name, ab_data):
    """Generate HTML export with better formatting"""
    html_lines = []
    html_lines.append("<!DOCTYPE html>")
    html_lines.append("<html lang='vi'>")
    html_lines.append("<head>")
    html_lines.append("<meta charset='UTF-8'>")
    html_lines.append("<meta name='viewport' content='width=device-width, initial-scale=1.0'>")
    html_lines.append(f"<title>Thông tin Kháng sinh - {html.escape(ab_name)}</title>")
    html_lines.append("""
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 800px;
            margin: 20px auto;
            padding: 20px;
            line-height: 1.6;
            color: #333;
        }
        h1 {
            color: #1976D2;
            border-bottom: 3px solid #1976D2;
            padding-bottom: 10px;
        }
        h2 {
            color: #0288D1;
            margin-top: 30px;
            border-left: 4px solid #0288D1;
            padding-left: 10px;
        }
        .info-box {
            background: #f5f5f5;
            padding: 15px;
            border-radius: 8px;
            margin: 10px 0;
        }
        ul {
            list-style-type: none;
            padding-left: 0;
        }
        li {
            padding: 5px 0;
            border-bottom: 1px solid #e0e0e0;
        }
        .warning {
            background: #fff3cd;
            border-left: 4px solid #ffc107;
            padding: 10px;
            margin: 20px 0;
        }
        .footer {
            margin-top: 40px;
            padding-top: 20px;
            border-top: 2px solid #e0e0e0;
            color: #666;
            font-size: 0.9em;
        }
    </style>
    """)
    html_lines.append("</head>")
    html_lines.append("<body>")
    
    html_lines.append(f"<h1>💊 {html.escape(ab_name)}</h1>")
    html_lines.append(f"<p><em>Ngày xuất: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</em></p>")
    
    # Basic info
    html_lines.append("<div class='info-box'>")
    html_lines.append("<h2>📋 Thông tin Cơ bản</h2>")
    if 'vietnamese_name' in ab_data:
        html_lines.append(f"<p><strong>Tên biệt dược:</strong> {html.escape(ab_data['vietnamese_name'])}</p>")
    if 'group' in ab_data:
        html_lines.append(f"<p><strong>Nhóm:</strong> {html.escape(ab_data['group'])}</p>")
    if 'administration' in ab_data:
        html_lines.append(f"<p><strong>Đường dùng:</strong> {', '.join(ab_data['administration'])}</p>")
    if 'aware_classification' in ab_data:
        html_lines.append(f"<p><strong>AWaRe:</strong> {html.escape(ab_data['aware_classification'])}</p>")
    html_lines.append("</div>")
    
    # Indications
    if 'indications' in ab_data:
        html_lines.append("<h2>📋 Chỉ định</h2>")
        html_lines.append("<ul>")
        for ind in ab_data['indications']:
            html_lines.append(f"<li>• {html.escape(ind)}</li>")
        html_lines.append("</ul>")
    
    # Dosage
    if 'dosage' in ab_data:
        html_lines.append("<h2>💉 Liều dùng</h2>")
        html_lines.append("<div class='info-box'>")
        dosage = ab_data['dosage']
        if 'adult_iv' in dosage:
            html_lines.append(f"<p><strong>IV:</strong> {html.escape(dosage['adult_iv'])}</p>")
        if 'adult_im' in dosage:
            html_lines.append(f"<p><strong>IM:</strong> {html.escape(dosage['adult_im'])}</p>")
        if 'adult_po' in dosage:
            html_lines.append(f"<p><strong>PO:</strong> {html.escape(dosage['adult_po'])}</p>")
        html_lines.append("</div>")
    
    # Renal adjustment
    if 'renal_adjustment' in ab_data:
        html_lines.append("<h2>🫘 Điều chỉnh theo chức năng thận</h2>")
        html_lines.append("<div class='info-box'>")
        renal = ab_data['renal_adjustment']
        if 'normal' in renal:
            html_lines.append(f"<p><strong>CrCl ≥ 60:</strong> {html.escape(renal['normal'])}</p>")
        if '30_60' in renal:
            html_lines.append(f"<p><strong>CrCl 30-60:</strong> {html.escape(renal['30_60'])}</p>")
        if '15_30' in renal:
            html_lines.append(f"<p><strong>CrCl 15-30:</strong> {html.escape(renal['15_30'])}</p>")
        if 'under_15' in renal:
            html_lines.append(f"<p><strong>CrCl < 15:</strong> {html.escape(renal['under_15'])}</p>")
        html_lines.append("</div>")
    
    # Side effects
    if 'side_effects' in ab_data:
        html_lines.append("<h2>⚠️ Tác dụng phụ</h2>")
        html_lines.append("<ul>")
        for se in ab_data['side_effects']:
            html_lines.append(f"<li>• {html.escape(se)}</li>")
        html_lines.append("</ul>")
    
    # Interactions
    if 'interactions' in ab_data:
        html_lines.append("<h2>🔗 Tương tác thuốc</h2>")
        html_lines.append("<ul>")
        for inter in ab_data['interactions']:
            html_lines.append(f"<li>• {html.escape(inter)}</li>")
        html_lines.append("</ul>")
    
    # Footer
    html_lines.append("<div class='footer'>")
    html_lines.append("<div class='warning'>")
    html_lines.append("<p><strong>⚠️ Lưu ý:</strong> Thông tin chỉ mang tính tham khảo. Không thay thế đánh giá lâm sàng của bác sĩ.</p>")
    html_lines.append("</div>")
    html_lines.append("</div>")
    
    html_lines.append("</body>")
    html_lines.append("</html>")
    
    return "\n".join(html_lines)


def _generate_json_export(ab_name, ab_data):
    """Generate JSON export with structured data"""
    export_data = {
        "antibiotic_name": ab_name,
        "export_date": datetime.now().isoformat(),
        "data": ab_data
    }
    
    return json.dumps(export_data, indent=2, ensure_ascii=False)
    
    with st.expander("📤 Export Thông tin", expanded=True):
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
            
            # Export options
            export_format = st.radio(
                "Định dạng:",
                ["📄 TXT", "🌐 HTML", "📋 JSON"],
                horizontal=True,
                key=f"export_format_{safe_filename}"
            )
            
            if export_format == "📄 TXT":
                st.download_button(
                    label="💾 Tải TXT",
                    data=export_text,
                    file_name=f"antibiotic_{safe_filename}.txt",
                    mime="text/plain",
                    use_container_width=True,
                    key=f"download_txt_{safe_filename}"
                )
            elif export_format == "🌐 HTML":
                html_content = _generate_html_export(ab_name, ab_data)
                st.download_button(
                    label="💾 Tải HTML",
                    data=html_content,
                    file_name=f"antibiotic_{safe_filename}.html",
                    mime="text/html",
                    use_container_width=True,
                    key=f"download_html_{safe_filename}"
                )
            else:  # JSON
                json_content = _generate_json_export(ab_name, ab_data)
                st.download_button(
                    label="💾 Tải JSON",
                    data=json_content,
                    file_name=f"antibiotic_{safe_filename}.json",
                    mime="application/json",
                    use_container_width=True,
                    key=f"download_json_{safe_filename}"
                )



