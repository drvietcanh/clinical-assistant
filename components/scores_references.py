
import streamlit as st

def render_references(score_info: dict):
    """
    Render references for a calculator if available.
    """
    if not score_info:
        return

    reference = score_info.get("reference")
    if reference:
        st.markdown("---")
        with st.expander("📚 Tài liệu tham khảo & Nguồn chứng cứ"):
            st.markdown(f"""
            **Nguồn chính:**
            {reference}
            
            *(Dữ liệu được trích dẫn từ các hướng dẫn lâm sàng uy tín)*
            """)
