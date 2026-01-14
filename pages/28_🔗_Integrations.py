"""
Integrations (File-based)

MVP: export small artifacts (guidelines list / updates) for external sharing.
"""

import json
import streamlit as st
from datetime import datetime

from utils.page_helper import setup_page, render_standard_footer
from utils.analytics_events import track_page_view, track_feature_usage

from components.app_updates import load_updates
from guidelines.data import GUIDELINES_DATABASE


setup_page(
    page_title="Integrations",
    page_icon="🔗",
    description="Export dữ liệu ra file để tích hợp ngoài (MVP)",
    mobile_header=True,
)

track_page_view("Integrations")
track_feature_usage("integrations_page_open")

st.title("🔗 Integrations (File-based)")
st.caption("Xuất dữ liệu ra file JSON để dùng ngoài ứng dụng (chưa có API server).")

tab1, tab2 = st.tabs(["🆕 Export Updates", "📋 Export Guidelines"])

with tab1:
    st.markdown("### 🆕 Export App Updates")
    updates = load_updates()
    payload = {
        "schema": "clinical-assistant.app-updates",
        "exported_at": datetime.now().isoformat(),
        "updates": [u.__dict__ for u in updates],
    }
    st.download_button(
        "⬇️ Tải app-updates.json",
        data=json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8"),
        file_name="app-updates.json",
        mime="application/json",
        use_container_width=True,
        on_click=lambda: track_feature_usage("integrations_export_updates"),
    )

with tab2:
    st.markdown("### 📋 Export Guidelines (metadata)")
    payload = {
        "schema": "clinical-assistant.guidelines",
        "exported_at": datetime.now().isoformat(),
        "count": len(GUIDELINES_DATABASE),
        "guidelines": [
            {
                "id": g.id,
                "title": g.title,
                "title_vn": g.title_vn,
                "organization": g.organization,
                "year": g.year,
                "category": g.category,
                "version": g.version,
                "last_updated": g.last_updated,
                "url": g.url,
                "related_protocol": g.related_protocol,
                "evidence_level": getattr(g, "evidence_level", "moderate"),
                "is_high_impact": g.is_high_impact,
            }
            for g in GUIDELINES_DATABASE
        ],
    }
    st.download_button(
        "⬇️ Tải guidelines.json",
        data=json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8"),
        file_name="guidelines.json",
        mime="application/json",
        use_container_width=True,
        on_click=lambda: track_feature_usage("integrations_export_guidelines"),
    )

render_standard_footer()

