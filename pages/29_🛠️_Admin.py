"""
Admin tools (local-only)
- Manage App Updates (CRUD)
"""

from __future__ import annotations

import os
import json
import time
from datetime import datetime
from pathlib import Path

import streamlit as st

from utils.page_helper import setup_page, render_standard_footer
from utils.analytics_events import track_page_view, track_feature_usage
from config.user_profile import get_current_profile, get_profile_label

from components.app_updates import AppUpdate, load_updates, upsert_update, delete_update
from components.news_logic import (
    load_news_config,
    DATA_DIR,
    NEWS_CONFIG_PATH,
    RSS_SOURCES_PATH,
    fetch_news_feed_with_retry,
)


ADMIN_PASSWORD = "canh1234"


#region agent log
def _agent_debug_log(hypothesis_id: str, message: str, data: dict) -> None:
    """
    Lightweight NDJSON logger for debug-session.
    Note: do NOT log secrets (passwords, tokens, PII).
    """
    try:
        payload = {
            "sessionId": "debug-session",
            "runId": "pre-fix",
            "hypothesisId": hypothesis_id,
            "location": "pages/29_Admin.py",
            "message": message,
            "data": data,
            "timestamp": int(time.time() * 1000),
        }
        with open(r"d:\1app\medical\.cursor\debug.log", "a", encoding="utf-8") as f:
            f.write(json.dumps(payload, ensure_ascii=False) + "\n")
    except Exception:
        # Logging must never break the app
        pass
#endregion


setup_page(
    page_title="Admin",
    page_icon="🛠️",
    description="Công cụ quản trị nội bộ (local)",
    mobile_header=True,
)

track_page_view("Admin")

st.title("🛠️ Admin (Local)")
st.caption(
    f"Profile hiện tại: **{get_profile_label(get_current_profile())}** • Lưu ý: mọi thay đổi ghi vào file local `data/`."
)

# Simple login screen for Admin
if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False

#region agent log
_agent_debug_log(
    "H2_session_state",
    "Admin page load - current session_state",
    {
        "admin_logged_in": bool(st.session_state.get("admin_logged_in", False)),
    },
)
#endregion

if not st.session_state.admin_logged_in:
    st.subheader("🔒 Đăng nhập Admin")
    with st.form("admin_login_form"):
        password = st.text_input("Mật khẩu", type="password")
        submitted = st.form_submit_button("Đăng nhập")

    if submitted:
        #region agent log
        _agent_debug_log(
            "H1_password_check",
            "Admin login form submitted",
            {
                "submitted": True,
                "password_length": len(password or ""),
            },
        )
        #endregion

        if password == ADMIN_PASSWORD:
            st.session_state.admin_logged_in = True

            #region agent log
            _agent_debug_log(
                "H1_password_check",
                "Admin login success, session_state updated",
                {
                    "admin_logged_in": True,
                },
            )
            #endregion

            st.success("Đăng nhập thành công.")
            st.rerun()
        else:
            #region agent log
            _agent_debug_log(
                "H1_password_check",
                "Admin login failed - wrong password",
                {
                    "password_length": len(password or ""),
                },
            )
            #endregion

            st.error("Sai mật khẩu. Vui lòng thử lại.")

    render_standard_footer()
    st.stop()

tab_updates, tab_news = st.tabs(["🆕 Manage Updates", "📰 News / RSS Config"])

with tab_updates:
    st.markdown("### 🆕 Manage App Updates (CRUD)")

    col_left, col_right = st.columns([2, 3])

    updates = load_updates()
    update_ids = [u.id for u in updates]

    with col_left:
        st.markdown("#### Danh sách")
        selected_id = st.selectbox("Chọn update để sửa", options=["(new)"] + update_ids)

        if selected_id != "(new)":
            if st.button("🗑️ Xóa update này", type="secondary", use_container_width=True):
                delete_update(selected_id)
                track_feature_usage("admin_updates_delete")
                st.success("Đã xóa.")
                st.rerun()

    with col_right:
        st.markdown("#### Editor")

        current = None
        if selected_id != "(new)":
            for u in updates:
                if u.id == selected_id:
                    current = u
                    break

        default_id = current.id if current else f"{datetime.now().date().isoformat()}-new"
        default_date = current.date if current else datetime.now().date().isoformat()
        default_title = current.title if current else ""
        default_content = current.content if current else ""
        default_type = current.type if current else "update"

        u_id = st.text_input("ID (unique)", value=default_id)
        u_date = st.text_input("Date (YYYY-MM-DD)", value=default_date)
        u_type = st.selectbox(
            "Type",
            options=["feature", "update", "improvement", "bugfix", "announcement"],
            index=["feature", "update", "improvement", "bugfix", "announcement"].index(default_type)
            if default_type in ["feature", "update", "improvement", "bugfix", "announcement"]
            else 1,
        )
        u_title = st.text_input("Title", value=default_title)
        u_content = st.text_area("Content (markdown ok)", value=default_content, height=180)

        col_save1, col_save2 = st.columns(2)
        with col_save1:
            if st.button("💾 Lưu (Upsert)", type="primary", use_container_width=True):
                if not u_id.strip() or not u_title.strip() or not u_date.strip():
                    st.error("Cần đủ: id, date, title.")
                else:
                    upsert_update(
                        AppUpdate(
                            id=u_id.strip(),
                            date=u_date.strip(),
                            title=u_title.strip(),
                            content=u_content.strip(),
                            type=u_type,
                        )
                    )
                    track_feature_usage("admin_updates_upsert")
                    st.success("Đã lưu.")
                    st.rerun()

        with col_save2:
            if st.button("👁️ Preview", use_container_width=True):
                st.markdown("---")
                st.markdown(f"**{u_title}** • {u_date} • `{u_type}`")
                st.markdown(u_content or "_(empty)_")
                track_feature_usage("admin_updates_preview")

with tab_news:
    st.markdown("### 📰 News / RSS Configuration")

    # ---- News config (JSON) ----
    st.markdown("#### 🔧 News Config")
    config = load_news_config()

    col_nc1, col_nc2, col_nc3 = st.columns(3)
    with col_nc1:
        update_on_page_load = st.checkbox(
            "Update on page load",
            value=config.get("update_on_page_load", True),
        )
        cache_ttl_minutes = st.number_input(
            "Cache TTL (minutes)",
            min_value=1,
            max_value=120,
            value=int(config.get("cache_ttl_minutes", 5)),
            step=1,
        )
    with col_nc2:
        max_items_per_feed = st.number_input(
            "Max items per feed",
            min_value=1,
            max_value=100,
            value=int(config.get("max_items_per_feed", 10)),
            step=1,
        )
        max_total_items = st.number_input(
            "Max total items",
            min_value=10,
            max_value=500,
            value=int(config.get("max_total_items", 50)),
            step=10,
        )
    with col_nc3:
        keep_history_days = st.number_input(
            "Keep history (days)",
            min_value=1,
            max_value=365,
            value=int(config.get("keep_history_days", 30)),
            step=1,
        )
        auto_cleanup = st.checkbox(
            "Auto cleanup history", value=config.get("auto_cleanup", True)
        )

    feeds_cfg = config.get("feeds", {}) or {}
    st.markdown("##### Feeds")
    col_f1, col_f2, col_f3 = st.columns(3)
    with col_f1:
        feeds_enabled = st.checkbox(
            "Feeds enabled", value=feeds_cfg.get("enabled", True)
        )
    with col_f2:
        timeout_seconds = st.number_input(
            "Timeout (seconds)",
            min_value=2,
            max_value=60,
            value=int(feeds_cfg.get("timeout_seconds", 10)),
            step=1,
        )
    with col_f3:
        retry_attempts = st.number_input(
            "Retry attempts",
            min_value=0,
            max_value=5,
            value=int(feeds_cfg.get("retry_attempts", 2)),
            step=1,
        )

    col_save_nc1, col_save_nc2 = st.columns([1, 3])
    with col_save_nc1:
        if st.button("💾 Lưu news_config.json", use_container_width=True):
            new_cfg = {
                "update_on_page_load": update_on_page_load,
                "cache_ttl_minutes": int(cache_ttl_minutes),
                "max_items_per_feed": int(max_items_per_feed),
                "max_total_items": int(max_total_items),
                "keep_history_days": int(keep_history_days),
                "auto_cleanup": bool(auto_cleanup),
                "feeds": {
                    "enabled": bool(feeds_enabled),
                    "timeout_seconds": int(timeout_seconds),
                    "retry_attempts": int(retry_attempts),
                },
            }
            try:
                DATA_DIR.mkdir(parents=True, exist_ok=True)
                with open(NEWS_CONFIG_PATH, "w", encoding="utf-8") as f:
                    json.dump(new_cfg, f, ensure_ascii=False, indent=2)
                track_feature_usage("admin_news_config_save")
                st.success("Đã lưu news_config.json")
            except Exception as e:
                st.error(f"Lỗi khi lưu: {e}")
    with col_save_nc2:
        st.caption(f"Path: `{Path(NEWS_CONFIG_PATH).name}` (trong thư mục data)")

    st.markdown("---")

    # ---- RSS sources (list) ----
    st.markdown("#### 📡 RSS Sources")

    try:
        with open(RSS_SOURCES_PATH, "r", encoding="utf-8") as f:
            rss_sources = json.load(f)
    except Exception:
        rss_sources = []

    if not isinstance(rss_sources, list):
        rss_sources = []

    # Simple table-like editor
    st.caption("Danh sách feed hiện tại:")
    for idx, src in enumerate(rss_sources):
        with st.expander(f"{idx+1}. {src.get('name', 'Unnamed')}"):
            c1, c2, c3 = st.columns([3, 4, 2])
            with c1:
                src["name"] = st.text_input(
                    "Name", value=src.get("name", ""), key=f"rss_name_{idx}"
                )
            with c2:
                src["url"] = st.text_input(
                    "URL", value=src.get("url", ""), key=f"rss_url_{idx}"
                )
            with c3:
                src["category"] = st.text_input(
                    "Category", value=src.get("category", ""), key=f"rss_cat_{idx}"
                )
            if st.button("🗑️ Xóa feed này", key=f"rss_del_{idx}"):
                rss_sources.pop(idx)
                track_feature_usage("admin_rss_delete")
                st.rerun()

    st.markdown("##### Thêm feed mới")
    new_name = st.text_input("Tên feed mới", key="rss_new_name")
    new_url = st.text_input("URL feed mới", key="rss_new_url")
    new_cat = st.text_input("Category", key="rss_new_cat", value="Clinical")

    col_rss1, col_rss2 = st.columns([1, 3])
    with col_rss1:
        if st.button("➕ Thêm feed", use_container_width=True):
            if not new_name.strip() or not new_url.strip():
                st.error("Cần ít nhất Name và URL.")
            else:
                rss_sources.append(
                    {
                        "name": new_name.strip(),
                        "url": new_url.strip(),
                        "category": new_cat.strip() or "Clinical",
                    }
                )
                track_feature_usage("admin_rss_add")
                try:
                    DATA_DIR.mkdir(parents=True, exist_ok=True)
                    with open(RSS_SOURCES_PATH, "w", encoding="utf-8") as f:
                        json.dump(rss_sources, f, ensure_ascii=False, indent=2)
                    st.success("Đã thêm feed. (Đã lưu rss_sources.json)")
                except Exception as e:
                    st.error(f"Lỗi khi lưu rss_sources.json: {e}")
    with col_rss2:
        if st.button("💾 Lưu thay đổi RSS Sources", use_container_width=True):
            try:
                DATA_DIR.mkdir(parents=True, exist_ok=True)
                with open(RSS_SOURCES_PATH, "w", encoding="utf-8") as f:
                    json.dump(rss_sources, f, ensure_ascii=False, indent=2)
                track_feature_usage("admin_rss_save_all")
                st.success("Đã lưu rss_sources.json")
            except Exception as e:
                st.error(f"Lỗi khi lưu rss_sources.json: {e}")

    st.markdown("---")
    st.markdown("#### 🧪 Test RSS feed")
    if rss_sources:
        feed_names = [f"{i+1}. {s.get('name', 'Unnamed')}" for i, s in enumerate(rss_sources)]
        selected = st.selectbox("Chọn feed để test", options=feed_names, key="rss_test_select")
        idx = feed_names.index(selected)
        test_src = rss_sources[idx]

        if st.button("🧪 Fetch thử 3 item", use_container_width=True, key="rss_test_btn"):
            url = test_src.get("url", "")
            name = test_src.get("name", "Unknown")
            st.info(f"Đang fetch từ: **{name}**\n\n`{url}`")
            try:
                cfg = load_news_config()
                timeout = int(cfg.get("feeds", {}).get("timeout_seconds", 10))
                items = fetch_news_feed_with_retry(url, name, timeout=timeout, retry_attempts=1)
                items = [it for it in items if not it.get("error")][:3]
                if not items:
                    st.warning("Không có item hợp lệ (hoặc lỗi).")
                else:
                    for it in items:
                        st.markdown(f"**{it.get('title','(no title)')}**")
                        st.caption(f"{it.get('date','?')} • {it.get('source', name)}")
                        if it.get("summary"):
                            st.write((it.get("summary") or "")[:300] + "...")
                        st.markdown("---")
                track_feature_usage("admin_rss_test_fetch")
            except Exception as e:
                st.error(f"Lỗi khi fetch: {e}")
    else:
        st.info("Chưa có RSS source nào trong rss_sources.json.")


render_standard_footer()

