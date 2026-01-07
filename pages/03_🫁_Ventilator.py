"""
Ventilator - Redirect to Critical Care
This page has been merged into Critical_Care.py
Keeping for backward compatibility - redirects to the unified Critical Care page
"""

import streamlit as st

# Set session state to open Ventilator tab/section
st.session_state['critical_care_open_ventilator'] = True

# Redirect to the unified Critical Care page
st.switch_page("pages/09_🫁_Critical_Care.py")
