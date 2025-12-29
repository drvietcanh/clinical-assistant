"""
Protocol Export Component
Print and PDF export functionality
"""

import streamlit as st
from typing import Optional
from datetime import datetime


def render_print_button():
    """
    Render print button that triggers browser print dialog.
    """
    st.markdown("""
    <script>
    function printProtocol() {
        window.print();
    }
    </script>
    """, unsafe_allow_html=True)
    
    if st.button("🖨️ In Protocol", use_container_width=True, type="secondary"):
        st.markdown("""
        <script>
        window.print();
        </script>
        """, unsafe_allow_html=True)
        st.info("💡 Sử dụng Ctrl+P (Windows) hoặc Cmd+P (Mac) để in. CSS print styles đã được tối ưu.")


def render_export_section(protocol_name: str):
    """
    Render export section with print and PDF options.
    
    Args:
        protocol_name: Name of the protocol
    """
    with st.expander("📥 Xuất / In Protocol", expanded=False):
        col1, col2 = st.columns(2)
        
        with col1:
            # Print button
            if st.button("🖨️ In", use_container_width=True, type="secondary"):
                st.markdown("""
                <script>
                window.print();
                </script>
                """, unsafe_allow_html=True)
                st.success("💡 Đang mở hộp thoại in. Sử dụng Ctrl+P nếu không tự động mở.")
        
        with col2:
            # PDF export (placeholder - would need weasyprint or similar)
            if st.button("📄 Tải PDF", use_container_width=True, type="primary"):
                st.info("""
                ⚠️ **Tính năng PDF đang được phát triển**
                
                Hiện tại bạn có thể:
                1. Sử dụng nút "In" và chọn "Save as PDF" trong hộp thoại in
                2. Hoặc sử dụng trình duyệt: Ctrl+P → Save as PDF
                
                CSS print styles đã được tối ưu cho PDF export.
                """)
        
        st.markdown("---")
        
        # Print tips
        st.markdown("""
        **💡 Mẹo in:**
        - Sidebar sẽ tự động ẩn khi in
        - Chỉ nội dung protocol được in
        - Format tối ưu cho A4
        - Có thể chọn "Save as PDF" trong hộp thoại in
        """)


def generate_print_friendly_html(protocol_content: str, protocol_name: str) -> str:
    """
    Generate print-friendly HTML version of protocol.
    
    Args:
        protocol_content: Protocol content
        protocol_name: Protocol name
        
    Returns:
        HTML string optimized for printing
    """
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>{protocol_name}</title>
        <style>
            @media print {{
                body {{
                    font-family: 'Times New Roman', serif;
                    font-size: 12pt;
                    line-height: 1.6;
                    color: #000;
                    background: #fff;
                }}
                .no-print {{
                    display: none !important;
                }}
                h1, h2, h3 {{
                    color: #000;
                    page-break-after: avoid;
                }}
                .protocol-section {{
                    page-break-inside: avoid;
                    margin-bottom: 1rem;
                }}
                @page {{
                    margin: 2cm;
                }}
            }}
        </style>
    </head>
    <body>
        <h1>{protocol_name}</h1>
        {protocol_content}
    </body>
    </html>
    """
    return html


def render_share_link(protocol_name: str, specialty: str):
    """
    Render share link generation (for future implementation).
    
    Args:
        protocol_name: Name of protocol
        specialty: Specialty name
    """
    with st.expander("🔗 Chia Sẻ Protocol", expanded=False):
        st.info("""
        **Tính năng chia sẻ đang được phát triển**
        
        Trong tương lai bạn sẽ có thể:
        - Tạo link chia sẻ protocol
        - Gửi qua email
        - Share với team
        """)
        
        # Placeholder for share link
        protocol_id = f"{specialty}_{protocol_name}".replace(" ", "_").lower()
        st.code(f"Protocol ID: {protocol_id}", language=None)

