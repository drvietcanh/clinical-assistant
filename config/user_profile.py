"""
User profile / specialty configuration
Currently supports two profiles: 'noi' (Internal Medicine) and 'icu' (Intensive Care).
"""

from typing import Literal

import streamlit as st

ProfileType = Literal["noi", "icu"]


def get_current_profile() -> ProfileType:
    """
    Get current user profile (specialty).
    Defaults to 'noi' if not set.
    """
    if "user_profile" not in st.session_state:
        st.session_state.user_profile = "noi"
    profile = st.session_state.user_profile
    # Defensive: fall back to 'noi' on unexpected value
    if profile not in ("noi", "icu"):
        profile = "noi"
        st.session_state.user_profile = profile
    return profile  # type: ignore[return-value]


def set_current_profile(profile: ProfileType) -> None:
    """Set current user profile."""
    st.session_state.user_profile = profile


def get_profile_label(profile: ProfileType | None = None) -> str:
    """Get human-readable label for a profile."""
    if profile is None:
        profile = get_current_profile()
    return "Nội" if profile == "noi" else "ICU"


__all__ = ["ProfileType", "get_current_profile", "set_current_profile", "get_profile_label"]

