"""
Guideline Viewer - Redirect to Guidelines Tracker
This page has been merged into Guidelines_Tracker.py with tabs
Keeping for backward compatibility - redirects to the unified page with Viewer tab
"""

import streamlit as st

# Set session state to open Viewer tab
st.session_state['guidelines_open_viewer_tab'] = True

# Redirect to the unified Guidelines Tracker page
st.switch_page("pages/15_📋_Guidelines_Tracker.py")
