"""
Voice Search Component
Voice search capability for mobile devices
"""

import streamlit as st
from typing import Optional, Callable


def render_voice_search_button(
    on_result: Optional[Callable[[str], None]] = None,
    button_text: str = "🎤 Tìm kiếm bằng giọng nói",
    language: str = "vi-VN"
) -> None:
    """
    Render voice search button (mobile/web)
    
    Args:
        on_result: Callback function when voice result is received
        button_text: Button text
        language: Language code for speech recognition
    """
    button_key = "voice_search_btn"
    
    # Check if browser supports speech recognition
    st.markdown("""
    <script>
    // Check for speech recognition support
    if (!('webkitSpeechRecognition' in window) && !('SpeechRecognition' in window)) {
        console.log('Speech recognition not supported');
    }
    </script>
    """, unsafe_allow_html=True)
    
    if st.button(button_text, key=button_key, use_container_width=True):
        st.markdown("""
        <div id="voice-search-status" style="text-align: center; padding: 10px;">
            <p>🎤 Đang nghe... Nói vào microphone</p>
        </div>
        <script>
        (function() {
            const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
            
            if (!SpeechRecognition) {
                document.getElementById('voice-search-status').innerHTML = 
                    '<p style="color: red;">❌ Trình duyệt không hỗ trợ nhận diện giọng nói</p>';
                return;
            }
            
            const recognition = new SpeechRecognition();
            recognition.lang = 'vi-VN';
            recognition.continuous = false;
            recognition.interimResults = false;
            
            recognition.onstart = function() {
                document.getElementById('voice-search-status').innerHTML = 
                    '<p style="color: blue;">🎤 Đang nghe...</p>';
            };
            
            recognition.onresult = function(event) {
                const transcript = event.results[0][0].transcript;
                document.getElementById('voice-search-status').innerHTML = 
                    '<p style="color: green;">✅ Đã nhận: ' + transcript + '</p>';
                
                // Store in session storage for Streamlit to pick up
                sessionStorage.setItem('voice_search_result', transcript);
                
                // Trigger Streamlit rerun
                window.parent.postMessage({type: 'streamlit:setComponentValue', value: transcript}, '*');
            };
            
            recognition.onerror = function(event) {
                document.getElementById('voice-search-status').innerHTML = 
                    '<p style="color: red;">❌ Lỗi: ' + event.error + '</p>';
            };
            
            recognition.onend = function() {
                document.getElementById('voice-search-status').innerHTML = 
                    '<p>Đã dừng nghe</p>';
            };
            
            recognition.start();
        })();
        </script>
        """, unsafe_allow_html=True)
        
        # Check for result in session state
        if 'voice_search_result' in st.session_state:
            result = st.session_state['voice_search_result']
            if on_result:
                on_result(result)
            else:
                st.session_state['search_query'] = result
                st.rerun()


def render_voice_search_integrated(
    search_callback: Callable[[str], None],
    placeholder: str = "Nhấn nút để tìm kiếm bằng giọng nói"
) -> None:
    """
    Render integrated voice search with text input fallback
    
    Args:
        search_callback: Function to call with search query
        placeholder: Placeholder text
    """
    col1, col2 = st.columns([4, 1])
    
    with col1:
        text_query = st.text_input(
            "🔍 Tìm kiếm",
            placeholder=placeholder,
            key="search_input"
        )
    
    with col2:
        render_voice_search_button(
            on_result=lambda result: search_callback(result),
            button_text="🎤"
        )
    
    if text_query:
        search_callback(text_query)


__all__ = [
    'render_voice_search_button',
    'render_voice_search_integrated',
]

