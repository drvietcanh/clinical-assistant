"""
Share Results Component
Generate shareable links with parameters, QR codes, and link expiration
"""

try:
    import streamlit as st
    import streamlit.components.v1 as components
except Exception:  # Fallback for test environments without Streamlit
    class _DummyStreamlit:
        def __getattr__(self, name):
            def _noop(*args, **kwargs):
                return None
            return _noop
    class _DummyComponents:
        def html(self, *args, **kwargs):
            return ""
    st = _DummyStreamlit()
    components = _DummyComponents()
from typing import Dict, Any, Optional
from datetime import datetime, timedelta
import json
import base64
import hashlib
import qrcode
from io import BytesIO
from PIL import Image


# In-memory storage for shared results (in production, use database)
SHARED_RESULTS_STORE = {}


def generate_share_id(calculator_id: str, inputs: Dict[str, Any], results: Dict[str, Any]) -> str:
    """
    Generate unique share ID from calculator and data
    
    Args:
        calculator_id: Calculator identifier
        inputs: Input values
        results: Calculation results
    
    Returns:
        Unique share ID
    """
    data_string = json.dumps({
        'calculator_id': calculator_id,
        'inputs': inputs,
        'results': results
    }, sort_keys=True)
    
    hash_object = hashlib.md5(data_string.encode())
    return hash_object.hexdigest()[:12]


def save_shared_result(
    calculator_id: str,
    calculator_name: str,
    inputs: Dict[str, Any],
    results: Dict[str, Any],
    expiration_days: int = 7
) -> str:
    """
    Save shared result and return share ID
    
    Args:
        calculator_id: Calculator identifier
        calculator_name: Calculator name
        inputs: Input values
        results: Calculation results
        expiration_days: Days until expiration (default 7)
    
    Returns:
        Share ID
    """
    share_id = generate_share_id(calculator_id, inputs, results)
    
    expiration_date = datetime.now() + timedelta(days=expiration_days)
    
    SHARED_RESULTS_STORE[share_id] = {
        'calculator_id': calculator_id,
        'calculator_name': calculator_name,
        'inputs': inputs,
        'results': results,
        'created_at': datetime.now().isoformat(),
        'expires_at': expiration_date.isoformat(),
        'expired': False
    }
    
    return share_id


def get_shared_result(share_id: str) -> Optional[Dict[str, Any]]:
    """
    Get shared result by ID
    
    Args:
        share_id: Share ID
    
    Returns:
        Shared result dict or None if not found/expired
    """
    if share_id not in SHARED_RESULTS_STORE:
        return None
    
    shared = SHARED_RESULTS_STORE[share_id]
    
    # Check expiration
    expires_at = datetime.fromisoformat(shared['expires_at'])
    if datetime.now() > expires_at:
        shared['expired'] = True
        return None
    
    return shared


def generate_share_url(share_id: str, base_url: Optional[str] = None) -> str:
    """
    Generate shareable URL
    
    Args:
        share_id: Share ID
        base_url: Base URL (defaults to current page)
    
    Returns:
        Shareable URL
    """
    if base_url is None:
        # Try to get from query params or use default
        base_url = st.get_option("server.baseUrlPath") or ""
    
    # For Streamlit, we'll use query parameters
    return f"?share={share_id}"


def generate_qr_code(data: str) -> str:
    """
    Generate QR code image as base64 string
    
    Args:
        data: Data to encode in QR code
    
    Returns:
        Base64 encoded image string
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Convert to base64
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    
    # Return data URI so clients can render directly
    return f"data:image/png;base64,{img_str}"


def render_share_section(
    calculator_id: str,
    calculator_name: str,
    inputs: Dict[str, Any],
    results: Dict[str, Any],
    show_qr: bool = True,
    expiration_days: int = 7
) -> None:
    """
    Render share results section
    
    Args:
        calculator_id: Calculator identifier
        calculator_name: Calculator name
        inputs: Input values
        results: Calculation results
        show_qr: Show QR code
        expiration_days: Days until expiration
    """
    st.markdown("---")
    st.subheader("🔗 Chia sẻ kết quả")
    
    # Save shared result
    share_id = save_shared_result(
        calculator_id=calculator_id,
        calculator_name=calculator_name,
        inputs=inputs,
        results=results,
        expiration_days=expiration_days
    )
    
    # Generate URL
    share_url = generate_share_url(share_id)
    full_url = f"{st.get_option('server.baseUrlPath') or ''}{share_url}"
    
    # Display share link
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown("**Link chia sẻ:**")
        st.code(share_url, language=None)
        
        # Copy button
        copy_button_html = f"""
        <button onclick="navigator.clipboard.writeText('{share_url}')" 
                style="
                    background: #007bff;
                    color: white;
                    border: none;
                    padding: 8px 16px;
                    border-radius: 4px;
                    cursor: pointer;
                    font-size: 14px;
                ">
            📋 Copy Link
        </button>
        """
        st.markdown(copy_button_html, unsafe_allow_html=True)
    
    with col2:
        if show_qr:
            # Generate QR code
            qr_data = share_url
            qr_image = generate_qr_code(qr_data)
            
            st.markdown("**QR Code:**")
            st.markdown(
                f'<img src="data:image/png;base64,{qr_image}" style="width: 150px; height: 150px;">',
                unsafe_allow_html=True
            )
    
    # Expiration info
    expiration_date = (datetime.now() + timedelta(days=expiration_days)).strftime('%Y-%m-%d %H:%M')
    st.info(f"⏰ Link sẽ hết hạn vào: **{expiration_date}** ({expiration_days} ngày)")
    
    # Share buttons
    st.markdown("**Chia sẻ qua:**")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Email
        email_subject = f"Kết quả {calculator_name}"
        email_body = f"Kết quả tính toán:\n\n{json.dumps(results, indent=2, ensure_ascii=False)}\n\nLink: {share_url}"
        email_link = f"mailto:?subject={email_subject}&body={email_body}"
        st.markdown(f'<a href="{email_link}" style="text-decoration: none;">📧 Email</a>', unsafe_allow_html=True)
    
    with col2:
        # WhatsApp (if on mobile)
        whatsapp_text = f"Kết quả {calculator_name}: {share_url}"
        whatsapp_link = f"https://wa.me/?text={whatsapp_text}"
        st.markdown(f'<a href="{whatsapp_link}" target="_blank" style="text-decoration: none;">💬 WhatsApp</a>', unsafe_allow_html=True)
    
    with col3:
        # Copy to clipboard (JavaScript)
        st.markdown(
            f'<button onclick="navigator.clipboard.writeText(\'{share_url}\'); alert(\'Đã copy!\');">📋 Copy</button>',
            unsafe_allow_html=True
        )


def load_shared_result_from_url() -> Optional[Dict[str, Any]]:
    """
    Load shared result from URL query parameters
    
    Returns:
        Shared result dict or None
    """
    query_params = st.query_params
    
    if 'share' in query_params:
        share_id = query_params['share']
        shared = get_shared_result(share_id)
        
        if shared:
            return shared
        else:
            st.error("⚠️ Link chia sẻ không hợp lệ hoặc đã hết hạn.")
            return None
    
    return None


def render_shared_result_view(shared: Dict[str, Any]) -> None:
    """
    Render shared result view
    
    Args:
        shared: Shared result dictionary
    """
    st.success(f"📥 Đã tải kết quả chia sẻ: **{shared['calculator_name']}**")
    
    st.markdown("### 📊 Kết quả")
    st.json(shared['results'])
    
    st.markdown("### 📋 Inputs")
    st.json(shared['inputs'])
    
    st.markdown("### ℹ️ Thông tin")
    st.info(f"**Tạo lúc:** {shared['created_at']}\n\n**Hết hạn:** {shared['expires_at']}")
    
    # Button to use this result
    if st.button("▶️ Sử dụng kết quả này", key="use_shared_result"):
        # Set inputs in session state
        st.session_state['shared_inputs'] = shared['inputs']
        st.rerun()

