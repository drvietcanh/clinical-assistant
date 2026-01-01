"""
AI Assistant Module
Smart Chat Interface for Clinical Decision Support
"""

import streamlit as st
import time
from utils.page_helper import setup_page, render_standard_footer
from components.ai_assistant_logic import get_ai_response

# Standard page setup with mobile optimizations
setup_page(
    page_title="Trợ lý AI Y Khoa",
    page_icon="🤖",
    description="Hỏi đáp về thuốc và phác đồ điều trị với AI Assistant",
    mobile_header=True
)

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Xin chào! Tôi là Trợ lý AI Y khoa (Beta). \n\nTôi có thể giúp bạn tra cứu nhanh thông tin thuốc, liều dùng, hoặc tìm kiếm phác đồ điều trị.\n\n*Ví dụ: 'Liều Paracetamol cho trẻ em', 'Phác đồ sốc phản vệ'...*"}
    ]

# Display Chat Messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input Handler
if prompt := st.chat_input("Nhập câu hỏi của bạn..."):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response with loading indicator
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Simulate thinking
        with st.spinner("Đang tra cứu dữ liệu..."):
            time.sleep(0.5) # Fake latency for realism
            response_data = get_ai_response(prompt)
            
        full_response = response_data["content"]
        
        # Typewriter effect
        # for chunk in full_response.split():
        #     full_response += chunk + " "
        #     time.sleep(0.05)
        #     message_placeholder.markdown(full_response + "▌")
        
        message_placeholder.markdown(full_response)
        
        # Handle special response types (cards, links)
        if response_data.get("type") == "protocol_link":
            p_id = response_data.get("protocol_id")
            spec = response_data.get("specialty", "Cấp cứu")
            
            if st.button("👉 Đi đến phác đồ này", key=f"link_{len(st.session_state.messages)}"):
                # Setup navigation
                st.session_state["protocol_to_open"] = p_id
                st.session_state["protocol_specialty"] = spec
                st.switch_page("pages/04_📋_Protocols.py")
        
    # Add assistant message to history
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# Sidebar Info
with st.sidebar:
    st.header("🤖 Về AI Assistant")
    st.info("""
    **Cơ chế hoạt động:**
    Phiên bản Beta hiện tại sử dụng thuật toán **Tìm kiếm Từ khóa Thông minh** (Keyword Matching) trên cơ sở dữ liệu nội bộ.
    
    Trong tương lai, phiên bản này sẽ được tích hợp **LLM (Large Language Model)** để hiểu ngôn ngữ tự nhiên tốt hơn.
    """)
    if st.button("🗑️ Xóa lịch sử chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

render_standard_footer()
