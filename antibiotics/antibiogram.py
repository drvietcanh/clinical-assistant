"""
Hospital Antibiogram (Vietnam) - Phase 1

Mục tiêu:
- Cung cấp antibiogram theo bệnh viện (S/I/R %) để hỗ trợ chọn empiric therapy.
- Tích hợp được vào UI (Tools tab) và dùng lại cho comparison/protocols.

Lưu ý:
- Dữ liệu dưới đây là dữ liệu mẫu (demo) để khởi động tính năng.
- Khi có dữ liệu chính thức từ từng BV, có thể thay thế/ghi đè theo năm.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Optional, Tuple, List, Any

import streamlit as st
import pandas as pd
from config.user_profile import get_current_profile


@dataclass(frozen=True)
class AntibiogramEntry:
    susceptible: float  # %
    intermediate: float  # %
    resistant: float  # %
    n: Optional[int] = None  # sample size
    notes: Optional[str] = None

    def as_dict(self) -> Dict[str, Any]:
        return {
            "S (%)": self.susceptible,
            "I (%)": self.intermediate,
            "R (%)": self.resistant,
            "N": self.n,
            "Ghi chú": self.notes or "",
        }


# Hospitals
VIETNAM_HOSPITALS = {
    "BACH_MAI": "Bệnh viện Bạch Mai",
    "CHO_RAY": "Bệnh viện Chợ Rẫy",
    "108": "Bệnh viện 108",
    "NHI_DONG": "Bệnh viện Nhi Đồng",
    "Y_DUOC_HCM": "Bệnh viện Đại học Y Dược TP.HCM",
    "GENERAL": "Bệnh viện đa khoa tỉnh/thành phố",
}


def _mk(s: float, i: float, r: float, n: Optional[int] = None, notes: Optional[str] = None) -> AntibiogramEntry:
    # Light validation to avoid silly values
    for v in (s, i, r):
        if v < 0 or v > 100:
            raise ValueError("Antibiogram % must be 0..100")
    return AntibiogramEntry(susceptible=s, intermediate=i, resistant=r, n=n, notes=notes)


# Demo antibiogram: organisms -> antibiotics -> entry
HOSPITAL_ANTIBIOGRAM_2025: Dict[str, Dict[str, Dict[str, AntibiogramEntry]]] = {
    "BACH_MAI": {
        "E. coli": {
            "Ceftriaxone": _mk(55, 8, 37, 620, "ESBL cao"),
            "Piperacillin-Tazobactam": _mk(68, 6, 26, 610),
            "Meropenem": _mk(93, 3, 4, 600),
            "Amikacin": _mk(88, 4, 8, 580),
            "Ciprofloxacin": _mk(40, 8, 52, 590),
        },
        "K. pneumoniae": {
            "Ceftriaxone": _mk(52, 7, 41, 510, "KPC/NDM rải rác"),
            "Piperacillin-Tazobactam": _mk(60, 6, 34, 500),
            "Meropenem": _mk(80, 4, 16, 480),
            "Amikacin": _mk(83, 4, 13, 470),
        },
        "P. aeruginosa": {
            "Ceftazidime": _mk(68, 7, 25, 220),
            "Piperacillin-Tazobactam": _mk(78, 6, 16, 230),
            "Meropenem": _mk(75, 6, 19, 210),
            "Amikacin": _mk(84, 4, 12, 200),
        },
        "A. baumannii": {
            "Meropenem": _mk(45, 8, 47, 190, "MDR phổ biến"),
            "Colistin": _mk(92, 3, 5, 160),
        },
        "S. aureus (MRSA)": {
            "Vancomycin": _mk(99, 0.5, 0.5, 140),
            "Linezolid": _mk(99.5, 0.3, 0.2, 120),
        },
    },
    "CHO_RAY": {
        "E. coli": {
            "Ceftriaxone": _mk(58, 7, 35, 700),
            "Piperacillin-Tazobactam": _mk(70, 6, 24, 690),
            "Meropenem": _mk(92, 3, 5, 680),
            "Amikacin": _mk(86, 5, 9, 640),
            "Ciprofloxacin": _mk(42, 8, 50, 670),
        },
        "K. pneumoniae": {
            "Ceftriaxone": _mk(50, 7, 43, 560),
            "Meropenem": _mk(78, 5, 17, 520),
            "Amikacin": _mk(82, 5, 13, 500),
        },
        "P. aeruginosa": {
            "Ceftazidime": _mk(66, 8, 26, 240),
            "Piperacillin-Tazobactam": _mk(76, 7, 17, 250),
            "Meropenem": _mk(73, 7, 20, 230),
        },
    },
    "108": {
        "E. coli": {
            "Ceftriaxone": _mk(57, 8, 35, 420),
            "Piperacillin-Tazobactam": _mk(69, 6, 25, 410),
            "Meropenem": _mk(93, 3, 4, 400),
            "Amikacin": _mk(87, 4, 9, 390),
            "Ciprofloxacin": _mk(42, 8, 50, 400),
        },
        "K. pneumoniae": {
            "Ceftriaxone": _mk(52, 7, 41, 360),
            "Piperacillin-Tazobactam": _mk(62, 6, 32, 350),
            "Meropenem": _mk(82, 4, 14, 340),
            "Amikacin": _mk(84, 4, 12, 330),
        },
        "P. aeruginosa": {
            "Ceftazidime": _mk(67, 7, 26, 160),
            "Piperacillin-Tazobactam": _mk(77, 6, 17, 170),
            "Meropenem": _mk(75, 7, 18, 165),
            "Amikacin": _mk(85, 4, 11, 150),
        },
    },
    "NHI_DONG": {
        "E. coli": {
            "Ceftriaxone": _mk(60, 8, 32, 300, "Dữ liệu pedi nội trú"),
            "Piperacillin-Tazobactam": _mk(72, 6, 22, 290),
            "Meropenem": _mk(95, 3, 2, 280),
            "Amikacin": _mk(90, 4, 6, 270),
            "Ciprofloxacin": _mk(45, 8, 47, 260),
        },
        "K. pneumoniae": {
            "Ceftriaxone": _mk(55, 7, 38, 220),
            "Meropenem": _mk(85, 4, 11, 210),
            "Amikacin": _mk(86, 4, 10, 205),
        },
        "P. aeruginosa": {
            "Ceftazidime": _mk(70, 7, 23, 120),
            "Piperacillin-Tazobactam": _mk(80, 6, 14, 118),
            "Meropenem": _mk(78, 7, 15, 115),
        },
    },
    "Y_DUOC_HCM": {
        "E. coli": {
            "Ceftriaxone": _mk(56, 8, 36, 380),
            "Piperacillin-Tazobactam": _mk(68, 6, 26, 370),
            "Meropenem": _mk(93, 3, 4, 360),
            "Amikacin": _mk(88, 4, 8, 350),
            "Ciprofloxacin": _mk(41, 8, 51, 355),
        },
        "K. pneumoniae": {
            "Ceftriaxone": _mk(53, 7, 40, 300),
            "Piperacillin-Tazobactam": _mk(63, 6, 31, 295),
            "Meropenem": _mk(81, 4, 15, 290),
            "Amikacin": _mk(84, 4, 12, 288),
        },
        "P. aeruginosa": {
            "Ceftazidime": _mk(67, 7, 26, 150),
            "Piperacillin-Tazobactam": _mk(78, 6, 16, 148),
            "Meropenem": _mk(75, 7, 18, 146),
            "Amikacin": _mk(85, 4, 11, 140),
        },
        "S. aureus (MRSA)": {
            "Vancomycin": _mk(99, 0.5, 0.5, 110),
            "Linezolid": _mk(99.5, 0.3, 0.2, 105),
        },
    },
    # Defaults for other hospitals fall back to “GENERAL” or VN baseline
    "GENERAL": {
        "E. coli": {
            "Ceftriaxone": _mk(58, 7, 35, None, "Ước tính theo dữ liệu VN"),
            "Piperacillin-Tazobactam": _mk(65, 7, 28),
            "Meropenem": _mk(92, 3, 5),
            "Amikacin": _mk(87, 4, 9),
            "Ciprofloxacin": _mk(40, 8, 52),
        },
        "K. pneumoniae": {
            "Ceftriaxone": _mk(55, 7, 38),
            "Meropenem": _mk(82, 4, 14),
            "Amikacin": _mk(83, 4, 13),
        },
        "P. aeruginosa": {
            "Ceftazidime": _mk(65, 8, 27),
            "Piperacillin-Tazobactam": _mk(75, 7, 18),
            "Meropenem": _mk(72, 8, 20),
        },
    },
}


def get_available_hospitals() -> Dict[str, str]:
    return dict(VIETNAM_HOSPITALS)


def _get_default_hospital_key() -> str:
    """Session-state key for default hospital, scoped by user profile."""
    profile = get_current_profile()
    return f"default_hospital_{profile}"


def get_default_hospital_id(hospitals: Dict[str, str]) -> str:
    """
    Get default hospital id for current user/profile.
    Falls back to GENERAL or first entry.
    """
    key = _get_default_hospital_key()
    stored = st.session_state.get(key)
    if isinstance(stored, str) and stored in hospitals:
        return stored
    if "GENERAL" in hospitals:
        return "GENERAL"
    # Fallback to first key
    return next(iter(hospitals.keys()))


def set_default_hospital_id(hospital_id: str) -> None:
    """Persist default hospital id in session_state for current profile."""
    if not hospital_id:
        return
    key = _get_default_hospital_key()
    st.session_state[key] = hospital_id


def _normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Normalize column names for CSV import."""
    col_map = {
        "hospital": "hospital",
        "bv": "hospital",
        "facility": "hospital",
        "organism": "organism",
        "vi_khuan": "organism",
        "pathogen": "organism",
        "antibiotic": "antibiotic",
        "thuoc": "antibiotic",
        "drug": "antibiotic",
        "s": "s",
        "i": "i",
        "r": "r",
        "n": "n",
        "sample": "n",
        "notes": "notes",
        "ghi_chu": "notes",
    }
    norm_cols = []
    for c in df.columns:
        key = c.strip().lower()
        norm_cols.append(col_map.get(key, key))
    df.columns = norm_cols
    return df


def parse_antibiogram_df(df: pd.DataFrame) -> Dict[str, Dict[str, Dict[str, AntibiogramEntry]]]:
    """
    Parse a DataFrame with columns: hospital, organism, antibiotic, s, i, r, [n], [notes].
    Returns nested dict hospital -> organism -> antibiotic -> AntibiogramEntry
    """
    if df is None or df.empty:
        return {}
    df = _normalize_columns(df)
    required = {"hospital", "organism", "antibiotic", "s", "r"}
    if not required.issubset(set(df.columns)):
        return {}
    result: Dict[str, Dict[str, Dict[str, AntibiogramEntry]]] = {}
    for _, row in df.iterrows():
        try:
            hospital = str(row.get("hospital", "")).strip()
            organism = str(row.get("organism", "")).strip()
            antibiotic = str(row.get("antibiotic", "")).strip()
            if not hospital or not organism or not antibiotic:
                continue
            s_val = float(row.get("s", 0) or 0)
            i_val = float(row.get("i", 0) or 0)
            r_val = float(row.get("r", 0) or 0)
            n_val = row.get("n", None)
            try:
                n_val = int(n_val) if pd.notna(n_val) else None
            except Exception:
                n_val = None
            notes_val = str(row.get("notes", "")).strip() if pd.notna(row.get("notes", "")) else None
            entry = _mk(s_val, i_val, r_val, n_val, notes_val)
            result.setdefault(hospital, {}).setdefault(organism, {})[antibiotic] = entry
        except Exception:
            # Skip malformed rows
            continue
    return result


def get_antibiogram(
    hospital_id: str,
    year: str = "2025",
) -> Dict[str, Dict[str, AntibiogramEntry]]:
    # For now we only ship 2025 demo dataset; year kept for forward compatibility.
    _ = year
    data = HOSPITAL_ANTIBIOGRAM_2025.get(hospital_id)
    if data:
        return data
    return HOSPITAL_ANTIBIOGRAM_2025["GENERAL"]


def _to_wide_table(
    antibiogram: Dict[str, Dict[str, AntibiogramEntry]],
    metric: str = "S (%)",
) -> pd.DataFrame:
    """
    Wide table: rows=organisms, cols=antibiotics, values=metric (S/I/R)
    """
    organisms = sorted(antibiogram.keys())
    antibiotics: List[str] = sorted({ab for org in antibiogram.values() for ab in org.keys()})
    rows = []
    for org in organisms:
        row = {"Vi khuẩn": org}
        for ab in antibiotics:
            entry = antibiogram.get(org, {}).get(ab)
            if not entry:
                row[ab] = None
            else:
                row[ab] = entry.as_dict().get(metric)
        rows.append(row)
    return pd.DataFrame(rows)


def render_antibiogram_view() -> None:
    st.markdown("### 🧫 Antibiogram theo bệnh viện")
    st.caption("Dữ liệu kháng thuốc theo từng bệnh viện (demo), hỗ trợ chọn kháng sinh kinh nghiệm.")

    # Optional CSV upload (user data)
    with st.expander("📥 Tải antibiogram từ CSV/Excel (tùy chọn)", expanded=False):
        uploaded = st.file_uploader("Chọn file CSV/Excel (cột: hospital, organism, antibiotic, s, i, r, [n], [notes])", type=["csv", "xlsx"], key="abx_antibiogram_upload")
        if uploaded:
            try:
                if uploaded.name.lower().endswith(".csv"):
                    df_u = pd.read_csv(uploaded)
                else:
                    df_u = pd.read_excel(uploaded)
                parsed = parse_antibiogram_df(df_u)
                if parsed:
                    st.session_state["abx_custom_antibiogram"] = parsed
                    st.success(f"Đã nạp {len(parsed)} bệnh viện từ file.")
                else:
                    st.warning("Không đọc được dữ liệu hợp lệ. Kiểm tra tên cột.")
            except Exception as exc:
                st.error(f"Lỗi đọc file: {exc}")

    hospitals = get_available_hospitals()
    if "abx_custom_antibiogram" in st.session_state:
        hospitals = {"CUSTOM_UPLOAD": "📂 Dữ liệu tải lên"} | hospitals

    # Personalization: default hospital per user/profile
    default_hospital = get_default_hospital_id(hospitals)
    if "CUSTOM_UPLOAD" in hospitals and "abx_custom_antibiogram" in st.session_state:
        default_hospital = "CUSTOM_UPLOAD"

    default_idx = list(hospitals.keys()).index(default_hospital)

    hospital_id = st.selectbox(
        "Chọn bệnh viện",
        options=list(hospitals.keys()),
        format_func=lambda k: hospitals.get(k, k),
        index=default_idx,
        key="abx_antibiogram_hospital",
    )

    # Update default preference (ignore CUSTOM_UPLOAD to avoid surprises)
    if hospital_id != "CUSTOM_UPLOAD":
        set_default_hospital_id(hospital_id)

    year = st.selectbox("Năm", options=["2025"], index=0, key="abx_antibiogram_year")
    if hospital_id == "CUSTOM_UPLOAD" and "abx_custom_antibiogram" in st.session_state:
        antibiogram = st.session_state["abx_custom_antibiogram"]
    else:
        antibiogram = get_antibiogram(hospital_id, year=year)

    # Filters
    organisms = sorted(antibiogram.keys())
    selected_orgs = st.multiselect(
        "Lọc vi khuẩn (tùy chọn)",
        options=organisms,
        default=organisms[: min(5, len(organisms))],
        key="abx_antibiogram_orgs",
    )
    filtered = {o: antibiogram[o] for o in selected_orgs} if selected_orgs else antibiogram

    metric = st.radio(
        "Hiển thị chỉ số",
        options=["S (%)", "I (%)", "R (%)"],
        horizontal=True,
        index=0,
        key="abx_antibiogram_metric",
    )

    df = _to_wide_table(filtered, metric=metric)
    st.dataframe(df, use_container_width=True, hide_index=True)

    with st.expander("Ghi chú & cảnh báo", expanded=False):
        st.markdown(
            "- Đây là **dữ liệu mẫu** để khởi động tính năng. Khi có antibiogram chính thức từng BV, hãy cập nhật theo năm.\n"
            "- Luôn kết hợp **lâm sàng + vị trí nhiễm + tiền sử kháng** và **kết quả cấy/KSĐ** để quyết định.\n"
            "- Nếu cần, có thể thêm view theo **khoa** (ICU/ngoại/nội) và theo **mẫu bệnh phẩm**."
        )

