"""
Main Menu Styles
Centralized CSS for the Main Menu page to keep layout and styling maintainable.
Modern, responsive design with dark mode support.
"""

import streamlit as st


def inject_main_menu_styles() -> None:
    """Inject CSS styles used on the Main Menu page."""
    st.markdown(
        """
<style>
/* ===== CSS Variables for Theme Support ===== */
:root {
    --primary-color: #00897B;
    --primary-dark: #00695C;
    --secondary-color: #667eea;
    --accent-color: #764ba2;
    --success-color: #4CAF50;
    --warning-color: #FF9800;
    --error-color: #F44336;
    --text-primary: #212121;
    --text-secondary: #757575;
    --bg-primary: #FFFFFF;
    --bg-secondary: #F5F5F5;
    --border-color: #E0E0E0;
    --shadow-sm: 0 2px 4px rgba(0,0,0,0.1);
    --shadow-md: 0 4px 12px rgba(0,0,0,0.15);
    --shadow-lg: 0 8px 24px rgba(0,0,0,0.2);
    --radius-sm: 8px;
    --radius-md: 12px;
    --radius-lg: 16px;
    --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

[data-theme="dark"] {
    --text-primary: #FFFFFF;
    --text-secondary: #B0B0B0;
    --bg-primary: #1E1E1E;
    --bg-secondary: #2D2D2D;
    --border-color: #404040;
}

/* ===== Main Container ===== */
.main-menu-container {
    max-width: 1400px;
    margin: 0 auto;
    padding: 20px;
}

/* ===== Hero Section ===== */
.hero-section {
    background: linear-gradient(135deg, #00897B 0%, #00695C 100%);
    border-radius: var(--radius-lg);
    padding: 2.5rem;
    margin-bottom: 2rem;
    color: white;
    box-shadow: var(--shadow-md);
    position: relative;
    overflow: hidden;
}

.hero-section::before {
    content: '';
    position: absolute;
    top: -50%;
    right: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
    animation: pulse 8s ease-in-out infinite;
}

@keyframes pulse {
    0%, 100% { transform: scale(1); opacity: 0.5; }
    50% { transform: scale(1.1); opacity: 0.8; }
}

.hero-content {
    position: relative;
    z-index: 1;
}

.hero-greeting {
    font-size: 2.5rem;
    font-weight: 700;
    margin: 0 0 0.5rem 0;
    letter-spacing: -0.02em;
}

.hero-date {
    font-size: 0.95rem;
    opacity: 0.9;
    margin-bottom: 1.5rem;
    font-weight: 500;
}

.hero-stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 1rem;
    margin-top: 1.5rem;
}

.hero-stat-card {
    background: rgba(255,255,255,0.15);
    padding: 1.25rem;
    border-radius: var(--radius-md);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.2);
    transition: var(--transition);
}

.hero-stat-card:hover {
    background: rgba(255,255,255,0.2);
    transform: translateY(-2px);
}

.hero-stat-label {
    font-size: 0.85rem;
    opacity: 0.9;
    margin: 0 0 0.5rem 0;
}

.hero-stat-value {
    font-size: 2rem;
    font-weight: 700;
    margin: 0;
}

/* ===== Search Section ===== */
.search-section {
    margin-bottom: 2rem;
}

.search-container {
    position: relative;
    margin-bottom: 1rem;
}

.search-input-wrapper {
    position: relative;
}

.search-suggestions {
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    background: var(--bg-primary);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-md);
    box-shadow: var(--shadow-lg);
    z-index: 1000;
    max-height: 400px;
    overflow-y: auto;
    margin-top: 4px;
}

.search-suggestion-item {
    padding: 12px 16px;
    cursor: pointer;
    border-bottom: 1px solid var(--border-color);
    transition: var(--transition);
    display: flex;
    align-items: center;
    gap: 12px;
}

.search-suggestion-item:hover,
.search-suggestion-item.selected {
    background: var(--bg-secondary);
}

.search-suggestion-icon {
    font-size: 1.5rem;
}

.search-suggestion-content {
    flex: 1;
}

.search-suggestion-name {
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 2px;
}

.search-suggestion-category {
    font-size: 0.85rem;
    color: var(--text-secondary);
}

.search-history {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 12px;
}

.search-history-chip {
    background: var(--bg-secondary);
    border: 1px solid var(--border-color);
    border-radius: 20px;
    padding: 6px 12px;
    font-size: 0.85rem;
    cursor: pointer;
    transition: var(--transition);
}

.search-history-chip:hover {
    background: var(--primary-color);
    color: white;
    border-color: var(--primary-color);
}

/* ===== Stats Cards ===== */
.stats-card {
    background: linear-gradient(135deg, var(--secondary-color) 0%, var(--accent-color) 100%);
    color: white;
    padding: 24px;
    border-radius: var(--radius-md);
    margin: 10px 0;
    box-shadow: var(--shadow-sm);
    transition: var(--transition);
}

.stats-card:hover {
    box-shadow: var(--shadow-md);
    transform: translateY(-2px);
}

.stats-card h3 {
    color: white;
    margin: 0 0 8px 0;
    font-size: 1rem;
    font-weight: 600;
}

.stats-card p {
    color: rgba(255, 255, 255, 0.95);
    margin: 0;
    font-size: 1.5rem;
    font-weight: 700;
}

.stats-card-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem;
    margin: 1.5rem 0;
}

/* ===== Quick Access Grid ===== */
.quick-access-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 1rem;
    margin: 1.5rem 0;
}

@media (max-width: 768px) {
    .quick-access-grid {
        grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
        gap: 0.75rem;
    }
}

/* ===== Category Cards ===== */
.category-card {
    background: var(--bg-primary);
    border: 2px solid var(--border-color);
    border-radius: var(--radius-md);
    padding: 24px;
    text-align: center;
    cursor: pointer;
    transition: var(--transition);
    box-shadow: var(--shadow-sm);
    position: relative;
    overflow: hidden;
}

.category-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, var(--primary-color), var(--secondary-color));
    transform: scaleX(0);
    transition: var(--transition);
}

.category-card:hover {
    box-shadow: var(--shadow-md);
    transform: translateY(-4px);
    border-color: var(--primary-color);
}

.category-card:hover::before {
    transform: scaleX(1);
}

.category-card-icon {
    font-size: 3rem;
    margin-bottom: 12px;
    display: block;
}

.category-card-title {
    font-size: 1.1rem;
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 8px;
}

.category-card-desc {
    font-size: 0.85rem;
    color: var(--text-secondary);
    margin-bottom: 8px;
}

.category-card-stats {
    font-size: 0.75rem;
    color: var(--text-secondary);
    margin-top: 8px;
}

/* ===== Calculator Cards ===== */
.calculator-card {
    background: var(--bg-primary);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-md);
    padding: 16px;
    transition: var(--transition);
    box-shadow: var(--shadow-sm);
    position: relative;
}

.calculator-card:hover {
    box-shadow: var(--shadow-md);
    transform: translateY(-2px);
    border-color: var(--primary-color);
}

.calculator-card-icon {
    font-size: 2.5rem;
    margin-bottom: 8px;
}

.calculator-card-name {
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 4px;
    font-size: 1rem;
}

.calculator-card-category {
    font-size: 0.85rem;
    color: var(--text-secondary);
}

.calculator-card-actions {
    display: flex;
    gap: 8px;
    margin-top: 12px;
}

/* ===== Favorites & Recently Used ===== */
.favorites-section,
.recently-used-section {
    margin: 2rem 0;
}

.empty-state {
    text-align: center;
    padding: 3rem 1rem;
    color: var(--text-secondary);
}

.empty-state-icon {
    font-size: 4rem;
    margin-bottom: 1rem;
    opacity: 0.5;
}

.empty-state-message {
    font-size: 1.1rem;
    margin-bottom: 0.5rem;
    color: var(--text-primary);
}

.empty-state-hint {
    font-size: 0.9rem;
    color: var(--text-secondary);
}

/* ===== Quick Actions ===== */
.quick-actions-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 1rem;
    margin: 1.5rem 0;
}

.quick-action-button {
    background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-dark) 100%);
    color: white;
    border: none;
    border-radius: var(--radius-md);
    padding: 1.5rem;
    font-size: 1rem;
    font-weight: 600;
    cursor: pointer;
    transition: var(--transition);
    box-shadow: var(--shadow-sm);
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 8px;
}

.quick-action-button:hover {
    box-shadow: var(--shadow-md);
    transform: translateY(-2px);
    background: linear-gradient(135deg, var(--primary-dark) 0%, var(--primary-color) 100%);
}

.quick-action-icon {
    font-size: 2.5rem;
}

/* ===== Announcement Banner ===== */
.announcement-banner {
    background: linear-gradient(135deg, #FF9800 0%, #F57C00 100%);
    color: white;
    padding: 1rem 1.5rem;
    border-radius: var(--radius-md);
    margin-bottom: 1.5rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: var(--shadow-sm);
}

.announcement-content {
    flex: 1;
}

.announcement-close {
    background: rgba(255,255,255,0.2);
    border: none;
    color: white;
    border-radius: 50%;
    width: 32px;
    height: 32px;
    cursor: pointer;
    font-size: 1.2rem;
    transition: var(--transition);
}

.announcement-close:hover {
    background: rgba(255,255,255,0.3);
}

/* ===== Responsive Design ===== */
@media (max-width: 1200px) {
    .main-menu-container {
        padding: 16px;
    }
    
    .hero-greeting {
        font-size: 2rem;
    }
    
    .hero-stats-grid {
        grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
    }
}

@media (max-width: 768px) {
    .hero-section {
        padding: 1.5rem;
    }
    
    .hero-greeting {
        font-size: 1.75rem;
    }
    
    .hero-stat-value {
        font-size: 1.5rem;
    }
    
    .stats-card-grid {
        grid-template-columns: 1fr;
    }
    
    .quick-actions-grid {
        grid-template-columns: repeat(2, 1fr);
    }
    
    .category-card {
        padding: 16px;
    }
}

@media (max-width: 480px) {
    .hero-section {
        padding: 1rem;
    }
    
    .hero-greeting {
        font-size: 1.5rem;
    }
    
    .hero-stats-grid {
        grid-template-columns: 1fr;
    }
    
    .quick-actions-grid {
        grid-template-columns: 1fr;
    }
}

/* ===== Loading States ===== */
.skeleton-loader {
    background: linear-gradient(90deg, 
        var(--bg-secondary) 0%, 
        rgba(255,255,255,0.5) 50%, 
        var(--bg-secondary) 100%);
    background-size: 200% 100%;
    animation: loading 1.5s ease-in-out infinite;
    border-radius: var(--radius-sm);
    height: 60px;
    margin-bottom: 8px;
}

@keyframes loading {
    0% { background-position: 200% 0; }
    100% { background-position: -200% 0; }
}

/* ===== Accessibility ===== */
*:focus-visible {
    outline: 2px solid var(--primary-color);
    outline-offset: 2px;
}

.sr-only {
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    margin: -1px;
    overflow: hidden;
    clip: rect(0, 0, 0, 0);
    white-space: nowrap;
    border-width: 0;
}

/* ===== Print Styles ===== */
@media print {
    .hero-section,
    .search-section,
    .announcement-banner {
        display: none;
    }
    
    .category-card,
    .calculator-card {
        break-inside: avoid;
    }
}
</style>
        """,
        unsafe_allow_html=True,
    )

