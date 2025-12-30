"""
CSS Fix Utility for Scores Pages
Uses JavaScript + CSS to fix text overlap issues dynamically
"""

import streamlit as st


def inject_text_overlap_fix():
    """
    Inject CSS + JavaScript to fix text overlap issues in input fields and headers.
    Uses MutationObserver to fix elements after Streamlit renders them dynamically.
    Call this at the beginning of any score page render function.
    """
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
        // Function to fix text input overlap
        function fixTextInputOverlap() {
            // Find all text inputs
            const textInputs = document.querySelectorAll('div[data-testid="stTextInput"]');
            
            textInputs.forEach(function(inputContainer) {
                // Find the actual input element
                const input = inputContainer.querySelector('input[type="text"]');
                if (!input) return;
                
                // Find and hide help icon to prevent overlap
                const helpIcon = inputContainer.querySelector('[data-testid="stTooltipIcon"]');
                const allHelpIcons = inputContainer.querySelectorAll('[class*="help"], [class*="icon"], [data-baseweb="popover"]');
                
                // Hide all help icons
                if (helpIcon) {
                    helpIcon.style.display = 'none';
                    helpIcon.style.visibility = 'hidden';
                    helpIcon.style.opacity = '0';
                    helpIcon.style.width = '0';
                    helpIcon.style.height = '0';
                    helpIcon.style.position = 'absolute';
                    helpIcon.style.left = '-9999px';
                    helpIcon.style.pointerEvents = 'none';
                }
                
                allHelpIcons.forEach(function(icon) {
                    icon.style.display = 'none';
                    icon.style.visibility = 'hidden';
                    icon.style.opacity = '0';
                    icon.style.pointerEvents = 'none';
                });
                
                // Ensure input has proper padding (no need for extra padding since icon is hidden)
                if (input) {
                    input.style.paddingRight = '16px';
                    input.style.width = '100%';
                    input.style.maxWidth = '100%';
                    input.style.boxSizing = 'border-box';
                }
                
                // Remove any pseudo-elements
                const style = document.createElement('style');
                style.textContent = `
                    div[data-testid="stTextInput"] *::before,
                    div[data-testid="stTextInput"] *::after {
                        content: none !important;
                        display: none !important;
                    }
                `;
                document.head.appendChild(style);
            });
        }
        
        // Fix immediately
        fixTextInputOverlap();
        
        // Fix after DOM changes (Streamlit renders dynamically)
        const observer = new MutationObserver(function(mutations) {
            let shouldFix = false;
            mutations.forEach(function(mutation) {
                if (mutation.addedNodes.length > 0) {
                    mutation.addedNodes.forEach(function(node) {
                        if (node.nodeType === 1 && (
                            node.querySelector && node.querySelector('div[data-testid="stTextInput"]') ||
                            node.matches && node.matches('div[data-testid="stTextInput"]')
                        )) {
                            shouldFix = true;
                        }
                    });
                }
            });
            if (shouldFix) {
                setTimeout(fixTextInputOverlap, 100);
            }
        });
        
        // Start observing
        observer.observe(document.body, {
            childList: true,
            subtree: true
        });
        
        // Also fix on window load
        window.addEventListener('load', fixTextInputOverlap);
        
        // Fix periodically as fallback
        setInterval(fixTextInputOverlap, 1000);
    })();
    </script>
    """, unsafe_allow_html=True)

