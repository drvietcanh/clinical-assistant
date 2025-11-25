"""
Diagnosis Module - Differential Diagnosis Generator
Main Router - Imports from diagnosis module
"""

import streamlit as st
from utils.page_helper import setup_page, render_standard_footer

from diagnosis import render_ddx_interface

# Standard page setup
setup_page(
    page_title="Chẩn đoán phân biệt",
    page_icon="🩺",
    description="Công cụ hỗ trợ tạo danh sách chẩn đoán phân biệt"
)

# ========== MAIN CONTENT ==========

# Render DDx interface
render_ddx_interface()

# ========== FOOTER ==========
render_standard_footer(disclaimer=True)

