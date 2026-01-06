# Tài liệu Đầy đủ - Trang Scores

**Ngày tạo**: 2026-01-06  
**Version**: 1.0  
**Status**: ✅ Implementation Complete - Ready for Testing

---

## Mục lục

1. [Tổng quan](#tổng-quan)
2. [Cấu trúc Trang](#cấu-trúc-trang)
3. [Specialties & Calculators](#specialties--calculators)
4. [UI Components](#ui-components)
5. [Configuration](#configuration)
6. [Functions & Methods](#functions--methods)
7. [Integration Points](#integration-points)
8. [File Structure](#file-structure)
9. [Testing Information](#testing-information)
10. [Known Issues & Notes](#known-issues--notes)

---

## Tổng quan

### Thống kê

- **Total Specialties**: 22
- **Total Calculators**: 201
- **New Module**: Geriatrics (6 calculators)
- **View Modes**: 2 (Classic, Modern)
- **UI Components**: 5 main components
- **Documentation Files**: 10 files

### Tính năng chính

1. **Classic View**: Sidebar navigation với radio button selection
2. **Modern View**: Calculator cards grid với tabs navigation
3. **Geriatrics Module**: 6 calculators cho elderly patients
4. **Recent Tracking**: Automatic tracking và quick access
5. **Mobile Optimization**: Responsive design với touch-friendly controls

---

## Cấu trúc Trang

### Main Page: `pages/01_📊_Scores.py`

#### Layout Structure

**Classic View:**
```
┌─────────────────────────────────────┐
│  Header: View Mode Toggle            │
├──────────┬───────────────────────────┤
│ Sidebar  │ Main Content              │
│          │                           │
│ • Search │ Calculator Display        │
│ • Filters│                           │
│ • Specialty│                         │
│ • Calculator List│                    │
│ • Favorites│                         │
└──────────┴───────────────────────────┘
```

**Modern View:**
```
┌─────────────────────────────────────┐
│  Header: View Mode Toggle            │
│  Enhanced Search Bar                 │
├─────────────────────────────────────┤
│  Tabs: Groups | Quick Access | All  │
├─────────────────────────────────────┤
│  Calculator Cards Grid (3 columns)   │
│  [Card] [Card] [Card]               │
│  [Card] [Card] [Card]               │
└─────────────────────────────────────┘
```

### Key Sections

1. **View Mode Toggle**: Switch giữa Classic và Modern View
2. **Search**: Global search với autocomplete
3. **Filters**: By status, usage, category
4. **Specialty Selection**: Dropdown/selectbox
5. **Calculator Display**: Routing đến appropriate module
6. **Related Calculators**: Suggestions ở cuối
7. **References**: Evidence và citations

---

## Specialties & Calculators

### Tổng quan Specialties

**22 Specialties** được tổ chức thành **4 nhóm chính**:

#### Nhóm 1: Critical Care & Emergency (Priority 1)
- 🚨 Cấp cứu & Hồi sức (Emergency & Critical Care) - 20 calculators
- 🦴 Chấn thương & Chỉnh Hình (Trauma/Orthopedics) - 5 calculators

#### Nhóm 2: Organ Systems (Priority 2)
- ❤️ Tim mạch (Cardiology) - 22 calculators
- 🫁 Hô hấp (Respiratory) - 9 calculators
- 🧠 Thần kinh (Neurology) - 15 calculators
- 🩸 Tiêu hóa - Gan Mật (GI/Hepatology) - 12 calculators
- 🩺 Huyết học & Đông máu (Hematology) - 4 calculators
- 🧪 Thận - Điện giải (Nephrology) - 4 calculators

#### Nhóm 3: Special Populations (Priority 3)
- 👴 Lão khoa (Geriatrics) ⭐ NEW - 6 calculators
- 👶 Nhi khoa (Pediatrics) - 10 calculators
- 🤰 Sản khoa (Obstetrics) - 3 calculators

#### Nhóm 4: Specialized Fields (Priority 4)
- 💉 Nội tiết - Chuyển hóa (Endocrinology/Metabolism) - 19 calculators
- 🦠 Nhiễm khuẩn (Infectious Disease) - 5 calculators
- 🎗️ Ung thư (Oncology) - 5 calculators
- 🧠 Tâm thần - Tâm Lý (Psychiatry/Psychology) - 8 calculators
- 🦴 Thấp khớp - Miễn Dịch (Rheumatology/Immunology) - 7 calculators
- 🩹 Da liễu (Dermatology) - 5 calculators
- 👂 Tai Mũi Họng (ENT) - 2 calculators
- 👁️ Mắt (Ophthalmology) - 1 calculator
- 😣 Đánh giá đau (Pain Assessment) - 6 calculators
- 🔪 Phẫu thuật & Gây mê (Surgery/Anesthesia) - 28 calculators
- 🛏️ Chăm sóc điều dưỡng (Nursing Care) - 2 calculators

### Chi tiết từng Specialty

#### 🚨 Cấp cứu & Hồi sức (Emergency & Critical Care)
**20 calculators:**
- NEWS2, MEWS, qSOFA, SOFA, SOFA-2 (2025), APACHE II, APACHE III, APACHE IV, SAPS II, SAPS III, MODS, LODS, HOSPITAL Score, LACE Index, Alvarado Score, ROX Index, Lactate Clearance, Charlson Index, CRB-65 Score, SCORTEN Score, RDOS

#### ❤️ Tim mạch (Cardiology)
**22 calculators:**
- ASCVD Risk, NYHA, Killip, Duke, CHA2DS2-VASc, HAS-BLED, SCORE2, SCORE2-OP, HEART Score, TIMI Risk, GRACE Score, CRUSADE Score, PRECISE-DAPT, DAPT Score, ARC-HBR Criteria, PCP-HF Risk Score, Framingham, Corrected QT, HFA-ICOS Multiple Myeloma, HFA-ICOS CML TKI, HFA-ICOS RAF/MEK, HFA-ICOS VEGF, HFA-ICOS HER2, HFA-ICOS Anthracycline

#### 🫁 Hô hấp (Respiratory)
**9 calculators:**
- PERC, CURB-65, PSI/PORT, Wells PE, PESI, SMART-COP, BODE Index, ARDS Berlin, mMRC, ACT

#### 🧠 Thần kinh (Neurology)
**15 calculators:**
- GCS, NIHSS, ICH Score, Hunt & Hess, mRS, ASPECTS, ABCD2, Barthel Index, FOUR Score, Canadian CT Head, FAST-ED, ICANS Consensus Grading, Sudbury Vertigo Risk Score, MGFA Clinical Classification, MG-ADL, ICE Score

#### 🩸 Tiêu hóa - Gan Mật (GI/Hepatology)
**12 calculators:**
- BISAP, Child-Pugh, MELD, Glasgow-Blatchford, AIMS65, Rockall Score, MELD-Na, Ranson, FIB-4, Acute Pancreatitis Prediction, SAFE Score, EREFS

#### 🩺 Huyết học & Đông máu (Hematology)
**4 calculators:**
- Padua, Wells DVT, 4Ts Score, DIC Score

#### 🧪 Thận - Điện giải (Nephrology)
**4 calculators:**
- eGFR, KDIGO, RIFLE, AKIN

#### 🦴 Chấn thương & Chỉnh Hình (Trauma/Orthopedics)
**5 calculators:**
- RTS, ISS, NEXUS, Canadian C-Spine, TRISS

#### 👂 Tai Mũi Họng (ENT)
**2 calculators:**
- Epworth, STOP-BANG

#### 👶 Nhi khoa (Pediatrics)
**10 calculators:**
- Westley Croup, PEWS, APGAR, Pediatric GCS, PELOD-2, PRISM III, PIM2, Pediatric SOFA, PECARN, DHAKA Score

#### 🤰 Sản khoa (Obstetrics)
**3 calculators:**
- Preeclampsia, Bishop Score, Modified Bishop

#### 💉 Nội tiết - Chuyển hóa (Endocrinology/Metabolism)
**19 calculators:**
- CrCl, BMI/IBW/BSA, Osmolality, Anion Gap, Corrected Ca, FENa, HbA1c, Winter Formula, Free T4 Index, Osteoporosis DXA, FRAX, HOMA-IR, FINDRISC, MAP, Maintenance Fluids, Sodium Correction Hyperglycemia, Free Water Deficit, Weight-based Levothyroxine

#### 🦴 Thấp khớp - Miễn Dịch (Rheumatology/Immunology)
**7 calculators:**
- DAS28, CDAI, SDAI, ACR Criteria, SLICC, SLEDAI, Gout Diagnostic

#### 🦠 Nhiễm khuẩn (Infectious Disease)
**5 calculators:**
- SIRS, Pitt Bacteremia, MASCC, Centor, FeverPAIN

#### 🩹 Da liễu (Dermatology)
**5 calculators:**
- PASI, SCORAD, DLQI, Burn TBSA, Parkland Formula

#### 🎗️ Ung thư (Oncology)
**5 calculators:**
- ECOG, Karnofsky, Palliative Performance, CIPN Grading, MSKCC RCC Risk

#### 🧠 Tâm thần - Tâm Lý (Psychiatry/Psychology)
**8 calculators:**
- PHQ-9, GAD-7, MMSE, MoCA, CAM, CIWA-Ar, COWS, GMAWS

#### 🔪 Phẫu thuật & Gây mê (Surgery/Anesthesia)
**28 calculators:**
- ASA, P-POSSUM, RCRI, Caprini, Aldrete Score, Mallampati, Apfel PONV, Koivuranta PONV, Wilson Risk, El-Ganzouri, LEMON, Cormack-Lehane, Ramsay, RASS, Riker SAS, PADSS, ARISCAT, CAM-ICU, 4AT, Surgical Apgar, SORT, Gupta Cardiac, Goldman Cardiac, Clavien-Dindo, RHMP-30, WIFI Classification, Perioperative Anticoagulation

#### 👁️ Mắt (Ophthalmology)
**1 calculator:**
- Intraocular Pressure

#### 😣 Đánh giá đau (Pain Assessment)
**6 calculators:**
- NRS, VAS, FLACC, NIPS, Wong-Baker, DN4

#### 🛏️ Chăm sóc điều dưỡng (Nursing Care)
**2 calculators:**
- Braden, Morse

#### 👴 Lão khoa (Geriatrics) ⭐ NEW
**6 calculators:**
- CFS (Clinical Frailty Scale)
- Morse Fall Scale
- MMSE (Mini-Mental State Examination)
- MoCA (Montreal Cognitive Assessment)
- Beers Criteria
- STOPP/START Criteria

---

## UI Components

### File: `scores/ui_scores_view.py`

#### Functions

1. **`is_daily_use(info: dict) -> bool`**
   - Check if calculator is marked as daily use
   - Checks for "DÙNG HÀNG NGÀY" or "⭐" in description

2. **`render_calculator_card(score_id, score_info, specialty, key_prefix)`**
   - Render modern calculator card với:
     - Icon (specialty-specific)
     - Name và description
     - Badges (Daily Use, New, Important)
     - Status indicator
     - "Use Calculator" button
   - Mobile-optimized với responsive CSS
   - Hover effects (desktop only)
   - Recent tracking integration

3. **`render_specialty_group(group_id, group_info, specialty_grouping)`**
   - Render specialty group với expandable section
   - Display calculators trong group
   - Responsive grid (1/2/3 columns)
   - Group header với icon và count

4. **`render_quick_access_section()`**
   - Render tabs: Most Used, Recent, Favorites
   - Most Used: Daily use calculators
   - Recent: Recently viewed (from session state)
   - Favorites: Starred calculators
   - Grid layout cho cards

5. **`render_filters_sidebar()`**
   - Enhanced filters:
     - By Status (✅ 🚧 📋)
     - By Usage (⭐ Daily Use, 🆕 New, 🔥 Popular)
     - By Category (Risk, Severity, Prognostic, Diagnostic)

6. **`filter_calculators(calculators, filters) -> List[Dict]`**
   - Apply filters to calculator list
   - Status filter
   - Usage filter
   - Category filter (if implemented)

---

## Configuration

### File: `scores/config.py`

#### Structure: `SCORES_BY_SPECIALTY`

```python
SCORES_BY_SPECIALTY = {
    "Specialty Name": {
        "calculator_id": {
            "name": "Calculator Name",
            "desc": "Description",
            "status": "✅" | "🚧" | "📋"
        }
    }
}
```

#### Status Values
- ✅: Complete, ready for clinical use
- 🚧: In progress/updating
- 📋: Planned

#### Special Markers in Description
- ⭐: Daily use
- ⭐⭐: Important
- ⭐⭐⭐: Very important/New
- MỚI: Newly added
- DÙNG HÀNG NGÀY: Daily use marker

### File: `scores/specialty_groups.py`

#### Structure: `SPECIALTY_GROUPS`

```python
SPECIALTY_GROUPS = {
    "group_id": {
        "id": "group_id",
        "name": "Group Name",
        "icon": "🎯",
        "description": "Description",
        "specialties": ["Specialty 1", "Specialty 2"],
        "priority": 1-4,
        "default_expanded": True/False
    }
}
```

#### Groups
1. **critical_care_emergency** (Priority 1)
2. **organ_systems** (Priority 2)
3. **special_populations** (Priority 3)
4. **specialized_fields** (Priority 4)

---

## Functions & Methods

### Main Page: `pages/01_📊_Scores.py`

#### Helper Functions

1. **`is_daily_use(info: dict) -> bool`**
   - Check if calculator marked as daily use

2. **`global_search(query: str) -> list`**
   - Search across all specialties
   - Returns: `[(specialty, score_id, score_info), ...]`
   - Searches in: score_id, name, description

3. **`get_all_scores_flat() -> list`**
   - Get all scores as flat list
   - Returns: `[{"specialty": ..., "score_id": ..., "score_info": ...}, ...]`

4. **`render_calculator_with_related(specialty_name, score_id, render_func)`**
   - Render calculator và show related calculators
   - Track recent
   - Show references

#### Routing Logic

Calculator routing dựa trên specialty name matching:
- Emergency: "Cấp cứu"
- Cardiology: "Tim mạch"
- Respiratory: "Hô hấp"
- Neurology: "Thần kinh"
- GI: "Tiêu Hóa" or "Gan"
- Metabolism: "Nội tiết" or "Chuyển hóa"
- Hematology: "Huyết học" or "Đông máu"
- Nephrology: "Thận" or "Điện giải"
- Trauma: "Chấn Thương" or "Chỉnh Hình"
- Psychiatry: "Tâm Thần" or "Tâm Lý"
- Oncology: "Ung thư"
- Surgery: "Phẫu Thuật" or "Gây Mê"
- Pediatrics: "Nhi Khoa"
- Infectious: "Nhiễm khuẩn"
- ENT: "Tai Mũi Họng" or "ENT"
- Obstetrics: "Sản khoa" or "Obstetrics"
- Dermatology: "Da Liễu" or "Dermatology"
- Rheumatology: "Thấp Khớp" or "Miễn Dịch"
- Ophthalmology: "Mắt" or "Ophthalmology"
- Pain: "Đánh giá đau" or "Pain"
- Nursing: "Chăm sóc điều dưỡng" or "Nursing"
- **Geriatrics**: "Lão khoa" or "Geriatrics" ⭐ NEW

### Recent Tracking: `components/scores_recent.py`

#### Functions

1. **`add_to_recent(specialty, score_id, score_name)`**
   - Add calculator to recent list
   - Max 20 items
   - Stored in session state

2. **`get_recent_calculators(max_items=10) -> List[Dict]`**
   - Get recent calculators
   - Returns list of dicts with specialty, score_id, name

3. **`clear_recent()`**
   - Clear recent calculators list

4. **`render_recent_list(max_items=10)`**
   - Render recent list (legacy, use get_recent_calculators instead)

---

## Integration Points

### With Other Modules

1. **Global Search**
   - Scores results trong global search
   - Links to calculator pages

2. **Favorites System**
   - Uses `components/scores_favorites.py`
   - Star/unstar calculators
   - Display favorites trong Quick Access

3. **Dark Mode**
   - Uses `components/scores_dark_mode.py`
   - Theme toggle trong sidebar

4. **Mobile Optimizations**
   - Uses `components/scores_mobile.py`
   - Responsive CSS
   - Touch-friendly controls

5. **Related Calculators**
   - Uses `components/scores_related.py`
   - Suggestions ở cuối calculator

6. **References**
   - Uses `components/scores_references.py`
   - Display references cho calculator

### Session State

#### Keys Used
- `scores_view_mode`: 'classic' or 'modern'
- `selected_specialty`: Current specialty
- `selected_score_id`: Current calculator ID
- `modern_view_calculator_selected`: Boolean flag
- `modern_view_specialty`: Specialty for modern view
- `modern_view_score_id`: Calculator ID for modern view
- `recent_calculators`: List of recent calculators
- `favorite_scores`: List of favorite (specialty, score_id) tuples

---

## File Structure

### Main Files

```
pages/
├── 01_📊_Scores.py              # Main page (Classic + Modern View)

scores/
├── config.py                    # Calculator configuration
├── specialty_groups.py          # Specialty grouping
├── ui_scores_view.py            # UI components
├── geriatrics/                  # NEW - Geriatrics module
│   ├── __init__.py
│   ├── cfs.py
│   ├── morse_fall.py
│   ├── mmse.py
│   ├── moca.py
│   ├── beers.py
│   └── stopp_start.py
└── [other specialty modules]/   # Existing modules

components/
├── scores_recent.py             # NEW - Recent tracking
├── scores_favorites.py          # Favorites system
├── scores_dark_mode.py          # Dark mode
├── scores_autocomplete.py      # Search autocomplete
├── scores_related.py            # Related calculators
├── scores_mobile.py             # Mobile optimizations
└── scores_references.py        # References

docs/
├── SCORES_UI_UX_RESEARCH.md
├── SCORES_OPTIMIZATION_SUMMARY.md
├── GERIATRICS_MODULE_GUIDE.md
├── SCORES_IMPLEMENTATION_STATUS.md
├── SCORES_PHASE1_COMPLETE.md
├── SCORES_PHASE2_PROGRESS.md
├── SCORES_TESTING_CHECKLIST.md
├── SCORES_READY_FOR_TESTING.md
├── SCORES_QUICK_START.md
├── SCORES_FINAL_SUMMARY.md
└── SCORES_COMPLETE_DOCUMENTATION.md  # This file
```

### Specialty Modules

Mỗi specialty có module riêng trong `scores/`:
- `emergency/`, `cardiology/`, `respiratory/`, `neurology/`, etc.
- Mỗi module có `__init__.py` với `render_[specialty]_calculator(score_id)` function

---

## Testing Information

### Test Results

#### Syntax Check ✅
- `pages/01_📊_Scores.py`: ✅ No syntax errors (fixed indentation)
- `scores/ui_scores_view.py`: ✅ No syntax errors
- `components/scores_recent.py`: ✅ No syntax errors
- `scores/geriatrics/`: ✅ All files compile

#### Import Check ✅
- Geriatrics module: ✅ Import OK
- Specialty groups: ✅ Import OK
- UI components: ✅ Import OK

#### Linter Check ✅
- No linter errors found

### Testing Checklist

Xem file `docs/SCORES_TESTING_CHECKLIST.md` cho full checklist.

### Quick Test Commands

```bash
# Syntax check
python -m py_compile pages/01_📊_Scores.py
python -m py_compile scores/ui_scores_view.py
python -m py_compile components/scores_recent.py

# Import check
python -c "from scores import geriatrics; print('OK')"
python -c "from scores.specialty_groups import get_all_groups; print('OK')"
python -c "from scores.ui_scores_view import render_calculator_card; print('OK')"

# Run app
streamlit run pages/01_📊_Scores.py
```

---

## Known Issues & Notes

### Fixed Issues ✅
1. **Indentation Error** (Line 271): Fixed - Removed empty if statement

### Potential Issues to Watch

1. **Modern View Routing**
   - Calculator routing có thể cần refinement
   - Verify all specialties route correctly trong Modern View

2. **Recent Tracking**
   - Test với nhiều calculators
   - Verify session persistence
   - Check performance với large recent list

3. **Mobile Layout**
   - Test trên nhiều screen sizes
   - Verify cards stack correctly
   - Check touch targets

4. **Performance**
   - Test với large number of calculators (201+)
   - Check page load time
   - Verify search performance

### Notes

1. **Classic View**: Vẫn là default view, fully functional
2. **Modern View**: Optional, có thể toggle
3. **Geriatrics**: Fully integrated, accessible từ cả hai views
4. **Recent Tracking**: Works trong cả hai views
5. **Mobile**: Responsive design, touch-friendly

### Dependencies

#### Required Modules
- `streamlit`
- `utils.page_helper`
- `components.ui`
- All specialty modules trong `scores/`

#### Optional Modules
- `components.scores_recent` (Recent tracking)
- `scores.geriatrics` (Geriatrics module)

---

## Code Examples

### Adding New Calculator

```python
# In scores/config.py
SCORES_BY_SPECIALTY["Specialty Name"]["new_calculator_id"] = {
    "name": "New Calculator Name",
    "desc": "Description (DÙNG HÀNG NGÀY for daily use)",
    "status": "✅"
}

# In specialty module (e.g., scores/emergency/__init__.py)
def render_emergency_calculator(calculator_id):
    calculators = {
        "new_calculator_id": render_new_calculator,
        # ... other calculators
    }
    # ... routing logic
```

### Using UI Components

```python
from scores.ui_scores_view import render_calculator_card

render_calculator_card(
    score_id="NEWS2",
    score_info={"name": "NEWS2", "desc": "...", "status": "✅"},
    specialty="🚨 Cấp cứu & Hồi sức",
    key_prefix="example"
)
```

### Recent Tracking

```python
from components.scores_recent import add_to_recent, get_recent_calculators

# Add to recent
add_to_recent("Specialty", "score_id", "Calculator Name")

# Get recent
recent = get_recent_calculators(max_items=10)
```

---

## Statistics Summary

### Calculators by Status
- ✅ Complete: ~195 calculators
- 🚧 In Progress: ~5 calculators
- 📋 Planned: ~1 calculator

### Calculators by Usage
- ⭐ Daily Use: ~50+ calculators
- 🆕 New: 6 calculators (Geriatrics)
- 🔥 Important: Multiple calculators

### Specialties Distribution
- Critical Care: 2 specialties, 25 calculators
- Organ Systems: 6 specialties, 66 calculators
- Special Populations: 3 specialties, 19 calculators
- Specialized Fields: 11 specialties, 91 calculators

---

## Future Enhancements

### Planned Features
1. Usage statistics tracking
2. Calculator preview modal
3. Export/Print functionality
4. Bottom navigation cho mobile
5. Swipe gestures
6. Custom calculator sets
7. Offline support
8. Advanced search filters
9. Calculator comparison
10. Integration với protocols

### Geriatrics Phase 2
- FRAIL Scale
- Hendrich II Fall Risk
- Clock Drawing Test
- Anticholinergic Burden Scale
- GDS (Geriatric Depression Scale)
- SARC-F (Sarcopenia screening)

---

## References

### Clinical Guidelines
- AGS Beers Criteria 2023
- STOPP/START Criteria 2015
- Clinical Frailty Scale (Rockwood et al.)
- Morse Fall Scale
- MMSE (Folstein et al.)
- MoCA (Nasreddine et al.)

### UI/UX References
- MDCalc (mdcalc.com)
- UpToDate
- Medscape
- BMJ Best Practice
- QxMD Calculate

---

## Support & Maintenance

### File Locations
- Main page: `pages/01_📊_Scores.py`
- Config: `scores/config.py`
- UI Components: `scores/ui_scores_view.py`
- Specialty Groups: `scores/specialty_groups.py`
- Recent Tracking: `components/scores_recent.py`
- Geriatrics: `scores/geriatrics/`

### Documentation
- All docs trong `docs/SCORES_*.md`
- Geriatrics guide: `docs/GERIATRICS_MODULE_GUIDE.md`
- Testing: `docs/SCORES_TESTING_CHECKLIST.md`

### Contact
- Check documentation files
- Review code comments
- Test với testing checklist

---

**Last Updated**: 2026-01-06  
**Version**: 1.0  
**Status**: ✅ Complete - Ready for Testing
