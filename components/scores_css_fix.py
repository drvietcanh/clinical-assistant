"""
CSS Fix Utility for Scores Pages
Uses JavaScript + CSS to fix text overlap issues dynamically
"""

import streamlit as st


def inject_text_overlap_fix():
    """
    Inject CSS + JavaScript to fix text overlap issues in input fields and headers.
    Uses MutationObserver to fix elements after Streamlit renders them dynamically.
    Only injects once per session to avoid duplicate injection.
    Call this at the beginning of any score page render function.
    """
    # Check if already injected in this session
    if st.session_state.get('_text_overlap_fix_injected', False):
        return
    
    # Mark as injected
    st.session_state['_text_overlap_fix_injected'] = True
    
    # Inject at the very beginning with highest priority
    st.markdown("""
    <style id="scores-text-overlap-fix">
    /* ========== FIX TEXT OVERLAP IN INPUT FIELDS ========== */
    /* High specificity selectors to override all other CSS */
    body div[data-testid="stTextInput"],
    body .stTextInput,
    body div[data-testid="stTextInput"] > div,
    body .stTextInput > div {
        position: relative !important;
        width: 100% !important;
        isolation: isolate !important;
        box-sizing: border-box !important;
    }
    
    body div[data-testid="stTextInput"] > div > div,
    body .stTextInput > div > div {
        position: relative !important;
        width: 100% !important;
        isolation: isolate !important;
        box-sizing: border-box !important;
    }
    
    body div[data-testid="stTextInput"] label,
    body .stTextInput label {
        position: relative !important;
        display: block !important;
        width: 100% !important;
        margin-bottom: 8px !important;
        z-index: 0 !important;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 
                     'Noto Sans', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans',
                     'Helvetica Neue', sans-serif !important;
        font-size: 14px !important;
        font-weight: 500 !important;
        line-height: 1.4 !important;
        color: rgb(49, 51, 63) !important;
        box-sizing: border-box !important;
    }
    
    body div[data-testid="stTextInput"] > div > div > div,
    body .stTextInput > div > div > div {
        position: relative !important;
        width: 100% !important;
        isolation: isolate !important;
        box-sizing: border-box !important;
    }
    
    /* Override ALL input styles with highest specificity */
    body div[data-testid="stTextInput"] input[type="text"],
    body .stTextInput input[type="text"],
    body div[data-testid="stTextInput"] > div > div > input,
    body .stTextInput > div > div > input,
    body div[data-testid="stTextInput"] input,
    body .stTextInput input {
        position: relative !important;
        z-index: 1 !important;
        width: 100% !important;
        max-width: 100% !important;
        min-width: 0 !important;
        padding: 12px 16px 12px 16px !important;
        padding-right: 16px !important;
        box-sizing: border-box !important;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 
                     'Noto Sans', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans',
                     'Helvetica Neue', sans-serif !important;
        font-size: 16px !important;
        line-height: 1.5 !important;
        color: rgb(49, 51, 63) !important;
        background: white !important;
        border: 1px solid rgb(230, 234, 241) !important;
        border-radius: 8px !important;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
    }
    
    /* Hide help icon completely to prevent overlap */
    body div[data-testid="stTextInput"] [data-testid="stTooltipIcon"],
    body .stTextInput [data-testid="stTooltipIcon"],
    body div[data-testid="stTextInput"] [class*="help"],
    body .stTextInput [class*="help"],
    body div[data-testid="stTextInput"] [class*="icon"],
    body .stTextInput [class*="icon"],
    body div[data-testid="stTextInput"] [data-baseweb="popover"],
    body .stTextInput [data-baseweb="popover"] {
        display: none !important;
        visibility: hidden !important;
        opacity: 0 !important;
        width: 0 !important;
        height: 0 !important;
        margin: 0 !important;
        padding: 0 !important;
        position: absolute !important;
        left: -9999px !important;
        pointer-events: none !important;
    }
    
    /* Remove any pseudo-elements that might cause overlap */
    body div[data-testid="stTextInput"] *::before,
    body .stTextInput *::before,
    body div[data-testid="stTextInput"] *::after,
    body .stTextInput *::after {
        content: none !important;
        display: none !important;
    }
    
    /* Fix BaseWeb input wrapper - highest specificity */
    body div[data-testid="stTextInput"] [data-baseweb="input"],
    body .stTextInput [data-baseweb="input"],
    body div[data-testid="stTextInput"] [data-baseweb="base-input"],
    body .stTextInput [data-baseweb="base-input"] {
        position: relative !important;
        width: 100% !important;
        isolation: isolate !important;
        box-sizing: border-box !important;
    }
    
    body div[data-testid="stTextInput"] [data-baseweb="input"] > div,
    body .stTextInput [data-baseweb="input"] > div,
    body div[data-testid="stTextInput"] [data-baseweb="base-input"] > div,
    body .stTextInput [data-baseweb="base-input"] > div {
        position: relative !important;
        width: 100% !important;
        isolation: isolate !important;
        box-sizing: border-box !important;
    }
    
    body div[data-testid="stTextInput"] [data-baseweb="input"] input,
    body .stTextInput [data-baseweb="input"] input,
    body div[data-testid="stTextInput"] [data-baseweb="base-input"] input,
    body .stTextInput [data-baseweb="base-input"] input {
        width: 100% !important;
        max-width: 100% !important;
        min-width: 0 !important;
        padding-right: 16px !important;
        box-sizing: border-box !important;
    }
    
    /* ========== FIX TEXT OVERLAP IN HEADERS ========== */
    h1, h2, h3, h4, h5, h6 {
        word-wrap: break-word !important;
        overflow-wrap: break-word !important;
        line-height: 1.3 !important;
        position: relative !important;
        z-index: 1 !important;
        max-width: 100% !important;
    }
    
    .stMarkdown h1,
    .stMarkdown h2,
    .stMarkdown h3,
    .stMarkdown h4,
    .stMarkdown h5,
    .stMarkdown h6 {
        word-wrap: break-word !important;
        overflow-wrap: break-word !important;
        line-height: 1.3 !important;
        position: relative !important;
        z-index: 1 !important;
        margin-bottom: 0.5rem !important;
        max-width: 100% !important;
    }
    
    /* Fix subtitle text */
    .stMarkdown p strong,
    .stMarkdown p {
        word-wrap: break-word !important;
        overflow-wrap: break-word !important;
        line-height: 1.5 !important;
        max-width: 100% !important;
    }
    </style>
    
    <script>
    (function() {
        // Aggressive function to fix text input overlap
        function fixTextInputOverlap() {
            // Find all text inputs using multiple selectors
            const textInputs = document.querySelectorAll('div[data-testid="stTextInput"], .stTextInput');
            
            textInputs.forEach(function(inputContainer) {
                // Find the actual input element - try multiple ways
                let input = inputContainer.querySelector('input[type="text"]');
                if (!input) {
                    input = inputContainer.querySelector('input');
                }
                if (!input) return;
                
                // Find ALL possible overlapping elements
                const helpIcon = inputContainer.querySelector('[data-testid="stTooltipIcon"]');
                const allIcons = inputContainer.querySelectorAll('svg, [class*="icon"], [class*="help"], [data-baseweb="popover"], button[aria-label*="help"], button[aria-label*="tooltip"]');
                const allOverlays = inputContainer.querySelectorAll('[style*="absolute"], [style*="fixed"], [class*="overlay"], [class*="tooltip"]');
                
                // Aggressively hide/remove ALL overlapping elements
                function hideElement(el) {
                    if (!el) return;
                    el.style.display = 'none';
                    el.style.visibility = 'hidden';
                    el.style.opacity = '0';
                    el.style.width = '0';
                    el.style.height = '0';
                    el.style.position = 'absolute';
                    el.style.left = '-9999px';
                    el.style.top = '-9999px';
                    el.style.pointerEvents = 'none';
                    el.style.zIndex = '-1';
                    if (el.parentNode) {
                        el.parentNode.style.position = 'relative';
                    }
                }
                
                if (helpIcon) hideElement(helpIcon);
                allIcons.forEach(hideElement);
                allOverlays.forEach(hideElement);
                
                // Force input styles directly - override everything
                const inputWrapper = input.closest('[data-baseweb="input"]') || input.parentElement;
                if (inputWrapper) {
                    inputWrapper.style.position = 'relative';
                    inputWrapper.style.width = '100%';
                    inputWrapper.style.overflow = 'visible';
                }
                
                // Find and remove ALL sibling elements that might overlap (including BaseWeb elements)
                const inputParent = input.parentElement;
                if (inputParent) {
                    const siblings = Array.from(inputParent.children);
                    siblings.forEach(function(sibling) {
                        if (sibling !== input && sibling.tagName !== 'LABEL') {
                            // Check if it's an icon or overlay element
                            if (sibling.querySelector && (
                                sibling.querySelector('svg') || 
                                sibling.querySelector('[class*="icon"]') ||
                                sibling.querySelector('[data-testid="stTooltipIcon"]')
                            )) {
                                hideElement(sibling);
                            }
                        }
                    });
                }
                
                // Force input element styles - use setProperty for better compatibility
                const inputStyles = {
                    'position': 'relative',
                    'z-index': '1',
                    'width': '100%',
                    'max-width': '100%',
                    'min-width': '0',
                    'padding': '12px 16px',
                    'padding-right': '16px',
                    'box-sizing': 'border-box',
                    'font-family': 'Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Noto Sans", Ubuntu, Cantarell, "Fira Sans", "Droid Sans", "Helvetica Neue", sans-serif',
                    'font-size': '16px',
                    'line-height': '1.5',
                    'color': 'rgb(49, 51, 63)',
                    'background': 'white',
                    'border': '1px solid rgb(230, 234, 241)',
                    'border-radius': '8px',
                    'white-space': 'nowrap',
                    'overflow': 'hidden',
                    'text-overflow': 'ellipsis'
                };
                
                Object.keys(inputStyles).forEach(function(prop) {
                    input.style.setProperty(prop, inputStyles[prop], 'important');
                });
                
                // Ensure container doesn't have overflow hidden
                inputContainer.style.setProperty('overflow', 'visible', 'important');
                inputContainer.style.setProperty('position', 'relative', 'important');
                
                // Remove any absolutely positioned elements inside the input container
                const absoluteElements = inputContainer.querySelectorAll('[style*="absolute"], [style*="fixed"]');
                absoluteElements.forEach(function(el) {
                    if (el !== input && !el.contains(input)) {
                        hideElement(el);
                    }
                });
            });
        }
        
        // Run immediately
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', fixTextInputOverlap);
        } else {
            fixTextInputOverlap();
        }
        
        // Aggressive MutationObserver - check more frequently
        const observer = new MutationObserver(function() {
            fixTextInputOverlap();
        });
        
        // Start observing immediately
        if (document.body) {
            observer.observe(document.body, {
                childList: true,
                subtree: true,
                attributes: true,
                attributeFilter: ['style', 'class']
            });
        } else {
            document.addEventListener('DOMContentLoaded', function() {
                observer.observe(document.body, {
                    childList: true,
                    subtree: true,
                    attributes: true,
                    attributeFilter: ['style', 'class']
                });
            });
        }
        
        // Multiple event listeners
        window.addEventListener('load', fixTextInputOverlap);
        window.addEventListener('resize', fixTextInputOverlap);
        
        // More frequent interval check
        setInterval(fixTextInputOverlap, 200);
    })();
    </script>
    """, unsafe_allow_html=True)

