"""
Performance Optimization for Antibiotics Module
Lazy loading, virtual scrolling, and performance enhancements
"""

import streamlit as st
from typing import List, Optional
from .protocols_schema import AntibioticProtocol


def inject_lazy_loading():
    """
    Inject lazy loading for protocol cards
    Cards load as user scrolls (intersection observer)
    """
    
    st.markdown("""
    <style>
    @media (max-width: 768px) {
        .lazy-load-card {
            opacity: 0;
            transform: translateY(20px);
            transition: opacity 0.3s ease, transform 0.3s ease;
        }
        
        .lazy-load-card.loaded {
            opacity: 1;
            transform: translateY(0);
        }
        
        .lazy-load-placeholder {
            min-height: 200px;
            background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
            background-size: 200% 100%;
            animation: loading 1.5s infinite;
            border-radius: 12px;
            margin-bottom: 16px;
        }
        
        @keyframes loading {
            0% { background-position: 200% 0; }
            100% { background-position: -200% 0; }
        }
    }
    </style>
    
    <script>
    (function() {
        'use strict';
        
        // Lazy load cards using Intersection Observer
        const lazyCards = document.querySelectorAll('.lazy-load-card');
        
        if ('IntersectionObserver' in window) {
            const cardObserver = new IntersectionObserver(function(entries, observer) {
                entries.forEach(function(entry) {
                    if (entry.isIntersecting) {
                        const card = entry.target;
                        card.classList.add('loaded');
                        observer.unobserve(card);
                    }
                });
            }, {
                rootMargin: '50px' // Start loading 50px before card enters viewport
            });
            
            lazyCards.forEach(function(card) {
                cardObserver.observe(card);
            });
        } else {
            // Fallback: Load all cards immediately
            lazyCards.forEach(function(card) {
                card.classList.add('loaded');
            });
        }
        
        // Re-observe when new content is added
        const observer = new MutationObserver(function(mutations) {
            mutations.forEach(function(mutation) {
                mutation.addedNodes.forEach(function(node) {
                    if (node.nodeType === 1) {
                        const newCards = node.querySelectorAll ? node.querySelectorAll('.lazy-load-card') : [];
                        newCards.forEach(function(card) {
                            if ('IntersectionObserver' in window) {
                                cardObserver.observe(card);
                            } else {
                                card.classList.add('loaded');
                            }
                        });
                    }
                });
            });
        });
        
        observer.observe(document.body, {
            childList: true,
            subtree: true
        });
    })();
    </script>
    """, unsafe_allow_html=True)


def inject_virtual_scrolling(container_id: str = "protocols-container"):
    """
    Inject virtual scrolling for long lists
    Only renders visible items + buffer
    
    Args:
        container_id: ID of container element
    """
    
    st.markdown(f"""
    <style>
    @media (max-width: 768px) {{
        #{container_id} {{
            height: 100vh;
            overflow-y: auto;
            -webkit-overflow-scrolling: touch;
        }}
        
        .virtual-scroll-item {{
            min-height: 200px;
            margin-bottom: 16px;
        }}
    }}
    </style>
    
    <script>
    (function() {{
        'use strict';
        
        const container = document.getElementById('{container_id}');
        if (!container) return;
        
        const items = container.querySelectorAll('.virtual-scroll-item');
        const itemHeight = 216; // Approximate height per item (200px + 16px margin)
        const buffer = 3; // Number of items to render outside viewport
        
        function updateVisibleItems() {{
            const scrollTop = container.scrollTop;
            const containerHeight = container.clientHeight;
            const startIndex = Math.max(0, Math.floor(scrollTop / itemHeight) - buffer);
            const endIndex = Math.min(items.length, Math.ceil((scrollTop + containerHeight) / itemHeight) + buffer);
            
            items.forEach(function(item, index) {{
                if (index >= startIndex && index < endIndex) {{
                    item.style.display = 'block';
                }} else {{
                    item.style.display = 'none';
                }}
            }});
        }}
        
        // Initial render
        updateVisibleItems();
        
        // Update on scroll
        let scrollTimeout;
        container.addEventListener('scroll', function() {{
            clearTimeout(scrollTimeout);
            scrollTimeout = setTimeout(updateVisibleItems, 10);
        }}, {{ passive: true }});
        
        // Update on resize
        window.addEventListener('resize', function() {{
            updateVisibleItems();
        }}, {{ passive: true }});
    }})();
    </script>
    """, unsafe_allow_html=True)


def inject_image_lazy_loading():
    """
    Inject lazy loading for images
    Images load when they enter viewport
    """
    
    st.markdown("""
    <script>
    (function() {
        'use strict';
        
        if ('IntersectionObserver' in window) {
            const imageObserver = new IntersectionObserver(function(entries, observer) {
                entries.forEach(function(entry) {
                    if (entry.isIntersecting) {
                        const img = entry.target;
                        if (img.dataset.src) {
                            img.src = img.dataset.src;
                            img.removeAttribute('data-src');
                            img.classList.add('loaded');
                            observer.unobserve(img);
                        }
                    }
                });
            }, {
                rootMargin: '50px'
            });
            
            // Observe all images with data-src
            const lazyImages = document.querySelectorAll('img[data-src]');
            lazyImages.forEach(function(img) {
                imageObserver.observe(img);
            });
            
            // Re-observe new images
            const observer = new MutationObserver(function(mutations) {
                mutations.forEach(function(mutation) {
                    mutation.addedNodes.forEach(function(node) {
                        if (node.nodeType === 1) {
                            const newImages = node.querySelectorAll ? node.querySelectorAll('img[data-src]') : [];
                            newImages.forEach(function(img) {
                                imageObserver.observe(img);
                            });
                        }
                    });
                });
            });
            
            observer.observe(document.body, {
                childList: true,
                subtree: true
            });
        }
    })();
    </script>
    
    <style>
    img[data-src] {
        opacity: 0;
        transition: opacity 0.3s ease;
    }
    
    img[data-src].loaded {
        opacity: 1;
    }
    </style>
    """, unsafe_allow_html=True)


def inject_performance_monitoring():
    """
    Inject performance monitoring
    Track load times, render times, etc.
    """
    
    st.markdown("""
    <script>
    (function() {
        'use strict';
        
        // Performance monitoring (only in development)
        if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
            window.addEventListener('load', function() {
                if (window.performance && window.performance.timing) {
                    const perfData = window.performance.timing;
                    const pageLoadTime = perfData.loadEventEnd - perfData.navigationStart;
                    const domReadyTime = perfData.domContentLoadedEventEnd - perfData.navigationStart;
                    const connectTime = perfData.responseEnd - perfData.requestStart;
                    
                    console.log('Performance Metrics:');
                    console.log('Page Load Time:', pageLoadTime + 'ms');
                    console.log('DOM Ready Time:', domReadyTime + 'ms');
                    console.log('Connect Time:', connectTime + 'ms');
                }
            });
            
            // Monitor long tasks
            if ('PerformanceObserver' in window) {
                try {
                    const observer = new PerformanceObserver(function(list) {
                        list.getEntries().forEach(function(entry) {
                            if (entry.duration > 50) {
                                console.warn('Long task detected:', entry.duration + 'ms');
                            }
                        });
                    });
                    observer.observe({ entryTypes: ['longtask'] });
                } catch (e) {
                    // Long task API not supported
                }
            }
        }
    })();
    </script>
    """, unsafe_allow_html=True)


def paginate_protocols(protocols: List[AntibioticProtocol], page_size: int = 10) -> tuple:
    """
    Paginate protocols for better performance
    
    Args:
        protocols: List of protocols
        page_size: Number of protocols per page
    
    Returns:
        Tuple of (current_page_protocols, total_pages, current_page)
    """
    
    if 'protocol_page' not in st.session_state:
        st.session_state.protocol_page = 1
    
    total_protocols = len(protocols)
    total_pages = (total_protocols + page_size - 1) // page_size
    current_page = st.session_state.protocol_page
    
    start_idx = (current_page - 1) * page_size
    end_idx = min(start_idx + page_size, total_protocols)
    
    current_protocols = protocols[start_idx:end_idx]
    
    return current_protocols, total_pages, current_page


def render_pagination_controls(total_pages: int, current_page: int, key_prefix: str = ""):
    """
    Render pagination controls
    
    Args:
        total_pages: Total number of pages
        current_page: Current page number
        key_prefix: Prefix for keys
    """
    
    if total_pages <= 1:
        return
    
    col_prev, col_info, col_next = st.columns([1, 2, 1])
    
    with col_prev:
        if st.button("← Trước", key=f"{key_prefix}_prev_page", disabled=(current_page == 1), use_container_width=True):
            st.session_state.protocol_page = max(1, current_page - 1)
            st.rerun()
    
    with col_info:
        st.markdown(f"<div style='text-align: center; padding: 12px;'>Trang {current_page} / {total_pages}</div>", unsafe_allow_html=True)
    
    with col_next:
        if st.button("Sau →", key=f"{key_prefix}_next_page", disabled=(current_page >= total_pages), use_container_width=True):
            st.session_state.protocol_page = min(total_pages, current_page + 1)
            st.rerun()
