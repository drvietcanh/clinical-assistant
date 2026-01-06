# 📋 Tóm Tắt Chức Năng & Cải Tiến Trang Antibiotics

**Ngày cập nhật:** 2025-02-18  
**Version:** 2.0  
**Trạng thái:** ✅ Hoàn thành

---

## 📑 Mục Lục

1. [Tổng Quan](#tổng-quan)
2. [Việt Hóa Thuật Ngữ](#việt-hóa-thuật-ngữ)
3. [Cải Thiện UI/UX](#cải-thiện-uiux)
4. [Tính Năng Khoa Học](#tính-năng-khoa-học)
5. [Tối Ưu Workflow](#tối-ưu-workflow)
6. [Cấu Trúc Files](#cấu-trúc-files)
7. [Hướng Dẫn Sử Dụng](#hướng-dẫn-sử-dụng)

---

## 🎯 Tổng Quan

Trang **Antibiotics (Kháng sinh)** là module chuyên sâu về kháng sinh với các tính năng:
- Phác đồ điều trị theo guideline mới nhất (IDSA/ATS, Sanford Guide)
- So sánh kháng sinh side-by-side
- Database 100+ kháng sinh tiêm truyền
- Tính liều tích hợp
- Tích hợp với các modules khác (TDM, Critical Care, Drug Database)

---

## 🇻🇳 Việt Hóa Thuật Ngữ

### ✅ Hoàn Thành 100%

#### 1. Schema & Enums
- **InfectionSite**: CAP → "Viêm phổi cộng đồng", HAP → "Viêm phổi bệnh viện", etc.
- **Severity**: MILD → "Nhẹ", MODERATE → "Trung bình", SEVERE → "Nặng", ICU → "ICU"
- **Setting**: OPD → "Ngoại trú", WARD → "Nội trú", ICU → "ICU"
- **RegimenType**: FIRST_LINE → "Tuyến đầu", ALTERNATIVE → "Thay thế", RESCUE → "Cứu cánh", STEP_DOWN → "Giảm liều"
- **RecommendationLevel**: STRONG → "Mạnh", WEAK → "Yếu", CONDITIONAL → "Có điều kiện"

#### 2. UI Components
- Tất cả labels, headers, tooltips đã được việt hóa
- Filters sidebar: "Vị trí nhiễm trùng", "Mức độ nặng", "Môi trường điều trị"
- Buttons: "Chi tiết", "TDM", "Tìm kiếm Toàn cục", "Hồi sức", "Cơ sở dữ liệu Thuốc"
- Messages: "Tìm thấy X phác đồ", "Không tìm thấy phác đồ", etc.

#### 3. Wizard (Trợ lý Chọn Kháng Sinh)
- Form labels: "Vị trí nhiễm trùng", "Mức độ nặng", "Môi trường điều trị"
- Comorbidities: "Bệnh thận mạn", "Suy giảm miễn dịch", "Mang thai"
- Risk factors: "Nguy cơ MRSA", "Nguy cơ Pseudomonas", "Nguy cơ ESBL", "Dị ứng beta-lactam"
- Output: "Đề xuất", "Tìm thấy X đề xuất"

#### 4. Database & Display
- Headers: "Tra cứu & Dữ liệu kháng sinh"
- Tabs: "Database", "Yêu thích", "Gần đây"
- Fields: "Chỉ định", "Chống chỉ định", "Tác dụng phụ", "Tương tác"

---

## 🎨 Cải Thiện UI/UX

### 1. Visual Hierarchy & Typography

#### Header Section
- **Font size**: 2.5em → **2.8em** (H1)
- **Font weight**: 700 (bold)
- **Letter spacing**: -0.5px
- **Text shadow**: 0 2px 8px rgba(0,0,0,0.2)
- **Gradient background**: linear-gradient(135deg, #4caf50 0%, #2e7d32 100%)
- **Box shadow**: 0 8px 24px rgba(76,175,80,0.25), 0 4px 8px rgba(0,0,0,0.1)
- **Decorative elements**: Blurred circles for depth

#### Typography Scale
- **H1**: 2.8em (Hero headers)
- **H2**: 2em (Section headers)
- **H3**: 1.5em (Card titles)
- **Body**: 1em (Standard text)
- **Caption**: 0.85-0.95em (Small text)

### 2. Color Coding System

#### Severity Colors
- **Nhẹ**: Background #e8f5e9 (xanh lá nhạt), Border #4caf50
- **Trung bình**: Background #fff3e0 (cam nhạt), Border #ff9800
- **Nặng**: Background #ffebee (đỏ nhạt), Border #f44336
- **ICU**: Background #fce4ec (hồng nhạt), Border #e91e63

#### Regimen Type Badges
- **Tuyến đầu**: #4caf50 (xanh lá) 🟢
- **Thay thế**: #ff9800 (cam) 🟡
- **Cứu cánh**: #f44336 (đỏ) 🔴
- **Giảm liều**: #2196f3 (xanh dương) 💊

#### AWaRe Classification
- **ACCESS**: #4caf50 (xanh) 🟢
- **WATCH**: #ffc107 (vàng) 🟡
- **RESERVE**: #f44336 (đỏ) 🔴

#### Recommendation Levels
- **Mạnh**: #4caf50 (xanh lá)
- **Yếu**: #ff9800 (cam)
- **Có điều kiện**: #ffc107 (vàng)

### 3. Card Design Enhancement

#### Protocol Cards
- **Border-radius**: 8px → **16px**
- **Padding**: 16px → **20px**
- **Box-shadow**: 
  - Before: `0 2px 4px rgba(0,0,0,0.1)`
  - After: `0 4px 12px rgba(0,0,0,0.15), 0 2px 4px rgba(0,0,0,0.1)`
- **Background**: Subtle gradient `linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%)`
- **Transition**: `all 0.3s ease`
- **Border-left**: 4px solid với màu theo severity

#### Regimen Cards
- **Border-radius**: 16px
- **Padding**: 20px
- **Box-shadow**: Multiple layers cho depth
- **Hover effect**: Smooth transitions (prepared for future enhancement)
- **Badge styling**: Rounded corners (12px), padding 6px 14px

### 4. Mobile Optimization

#### Responsive Breakpoints
- **Mobile**: < 768px
- **Tablet**: 768-1024px
- **Desktop**: > 1024px

#### Mobile-Specific Improvements
- **Touch targets**: Minimum 44x44px cho buttons
- **Font sizes**: Responsive (smaller trên mobile)
- **Layout**: Stacked columns trên mobile
- **CSS**: Media queries cho mobile optimization
- **Buttons**: Full-width trên mobile (`use_container_width=True`)

#### CSS Media Queries
```css
@media (max-width: 768px) {
    .stButton > button {
        min-height: 44px;
        font-size: 1em;
    }
    .stExpander {
        font-size: 0.95em;
    }
}
```

### 5. Loading & Empty States

#### Skeleton Loaders
- Animated placeholders khi đang load data
- Pulse animation effect
- Placeholder cards với gray backgrounds

#### Empty States
- Icon-based empty state messages
- Helpful text: "Vui lòng thử điều chỉnh bộ lọc hoặc từ khóa tìm kiếm"
- Centered layout với large icons

### 6. Guideline Badges

#### Enhanced Design
- **Background**: Linear gradient `linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%)`
- **Color**: #1976d2 (blue)
- **Padding**: 6px 14px
- **Border-radius**: 12px
- **Box-shadow**: 0 2px 4px rgba(25,118,210,0.2)
- **Content**: Guideline source + year + last reviewed date

---

## 🔬 Tính Năng Khoa Học

### 1. MIC Breakpoints & Susceptibility

#### Tích Hợp
- Hiển thị trong regimen cards với expander "🔬 Độ nhạy cảm (Việt Nam)"
- Data từ `mic_breakpoints.py`
- Color coding:
  - **Xanh (#4caf50)**: Sensitive (S)
  - **Đỏ (#f44336)**: Resistant (R)
  - **Xám (#666)**: Other patterns

#### Hiển Thị
- Top 5 organisms phổ biến nhất
- Format: `Organism: Pattern (e.g., "S (90-95%)", "R: 35-45% tại VN")`
- Notes section nếu có

#### Ví Dụ
```
🔬 Độ nhạy cảm (Việt Nam)
E. coli: S (55-65%) - R: 35-45% tại VN
K. pneumoniae: S (50-60%) - R: 40-50% tại VN
S. pneumoniae: S (85-90%)
💡 ESBL-producing E. coli phổ biến (30-40%)
```

### 2. Resistance Patterns (Việt Nam)

#### Data Source
- `resistance_patterns.py`
- Local surveillance data từ Việt Nam
- Updated 2024

#### Coverage
- **E. coli**: Ceftriaxone (R: 35-45%), Ciprofloxacin (R: 50-60%), etc.
- **K. pneumoniae**: KPC và NDM carbapenemase phổ biến
- **Pseudomonas aeruginosa**: Kháng đa thuốc phổ biến
- **Acinetobacter baumannii**: Kháng đa thuốc rất cao
- **Staphylococcus aureus**: MRSA (30-40%)
- **Enterococcus**: VRE đang tăng
- Và nhiều organisms khác

#### Integration
- Tích hợp vào MIC breakpoints display
- Warning badges khi resistance cao
- Notes về resistance patterns đặc biệt

### 3. Evidence Levels & Guidelines

#### Recommendation Levels
- **Mạnh**: Strong recommendation (xanh lá)
- **Yếu**: Weak recommendation (cam)
- **Có điều kiện**: Conditional recommendation (vàng)

#### Guideline Sources
- **IDSA/ATS 2019**: CAP guidelines
- **IDSA/ATS 2016**: HAP/VAP guidelines
- **IDSA 2010**: UTI guidelines
- **IDSA 2014**: SSTI guidelines
- **Surviving Sepsis Campaign 2021**: Sepsis guidelines
- **Sanford Guide 2025**: Empiric therapy patterns

#### Display
- Badge với guideline source + year
- Last reviewed date (nếu có)
- Visual distinction với gradient backgrounds

---

## ⚙️ Tối Ưu Workflow

### 1. Print & Export

#### Print-Friendly CSS
```css
@media print {
    .stButton, .stSidebar, .stHeader {
        display: none !important;
    }
    .protocol-card, .regimen-card {
        page-break-inside: avoid;
        border: 1px solid #000 !important;
    }
}
```

#### Export Features
- **Export Protocols List**: Text file với danh sách protocols
- **Format**: Plain text (.txt)
- **Content**: Title, infection site, severity, guideline source
- **Download button**: "📥 Xuất danh sách"

#### Print Button
- Nút "📄 In" trong mỗi regimen card
- Triggers browser print dialog
- Print-optimized layout

### 2. Integration Improvements

#### Quick Links
- **Global Search**: Link đến trang tìm kiếm toàn cục
- **Critical Care**: Link đến phác đồ hồi sức (cho sepsis/severe infections)
- **Drug Database**: Link đến database thuốc chi tiết
- **TDM**: Auto-link khi chọn vancomycin/aminoglycoside

#### Context-Aware Links
- Critical Care link chỉ hiện khi: `infection_site == SEPSIS` hoặc `severity == ICU`
- TDM link chỉ hiện cho: vancomycin, aminoglycoside, gentamicin, tobramycin, amikacin

#### Navigation
- Breadcrumbs-ready structure
- Seamless page switching với `st.switch_page()`
- Session state management cho search queries

### 3. Search Enhancement

#### Enhanced Search Bar
- Placeholder: "Tìm theo nhiễm trùng, thuốc hoặc hướng dẫn..."
- Help text: "Tìm kiếm theo tên nhiễm trùng, tên thuốc, hoặc nguồn hướng dẫn"
- Search trong: Title, description, indication, drug names

#### Quick Search Suggestions
- **CAP**: Community-acquired pneumonia
- **UTI**: Urinary tract infection
- **Sepsis**: Sepsis/septic shock
- **MRSA**: Methicillin-resistant S. aureus
- One-click search buttons

#### Search Features
- Case-insensitive search
- Multi-field search (title, description, indication, drugs)
- Real-time filtering
- Search + filter combination

### 4. Comparison Tools

#### Side-by-Side Comparison
- Multi-drug comparison (existing feature)
- Visual comparison tables
- Color-coded differences

#### Integration
- Link từ regimen cards đến comparison tools
- Pre-filled drug selection

---

## 📁 Cấu Trúc Files

### Core Files

#### `antibiotics/protocols_schema.py`
- Schema definitions cho protocols
- Enum classes với Vietnamese labels
- Dataclasses: `DrugDose`, `Regimen`, `AntibioticProtocol`, `ProtocolCollection`

#### `antibiotics/protocols_data.py`
- Protocol data cho các infections:
  - CAP (non-severe, severe, ICU)
  - HAP/VAP
  - UTI (uncomplicated, complicated)
  - SSTI (mild, severe)
  - Sepsis/Septic shock

#### `antibiotics/ui_antibiotics_view.py`
- Main UI components
- Card rendering functions
- Filter sidebar
- Search functionality
- Integration links

#### `antibiotics/wizard.py`
- Antibiotic Wizard form
- Recommendation engine
- Comorbidity handling
- Risk factor assessment

### New Files

#### `antibiotics/vietnamese_terms.py`
- Centralized Vietnamese terminology mapping
- Functions: `get_vietnamese_label()`
- Dictionaries: `INFECTION_SITE_VI`, `SEVERITY_VI`, `SETTING_VI`, etc.

#### `antibiotics/ui_helpers.py`
- UI helper functions
- Color schemes: `SEVERITY_COLORS`, `REGIMEN_BADGE_COLORS`, etc.
- Utility functions: `render_skeleton_loader()`, `render_empty_state()`

### Supporting Files

#### `antibiotics/mic_breakpoints.py`
- MIC breakpoints data (CLSI, EUCAST)
- Functions: `get_mic_breakpoints()`, `get_common_susceptibility()`

#### `antibiotics/resistance_patterns.py`
- Vietnam resistance patterns data
- Functions: `get_resistance_pattern()`, `get_antibiotic_resistance_summary()`

#### `antibiotics/database.py`
- Main database view
- Search & filter functions
- Favorites & recent tracking

#### `antibiotics/database_display.py`
- Display components
- Compact cards
- Detail views
- Export functions

#### `pages/02_💊_Antibiotics.py`
- Main page file
- Tab navigation
- Hero section
- Sidebar

---

## 📖 Hướng Dẫn Sử Dụng

### 1. Navigation

#### Tabs
- **🦠 Theo Nhiễm Trùng**: Protocols organized by infection site
- **💊 Theo Nhóm Thuốc**: Organized by drug class (coming soon)
- **🔄 Quản lý Kháng Sinh**: Stewardship tools (coming soon)
- **🔧 Công cụ**: Legacy tools (database, comparison)

### 2. By Infection Tab

#### Wizard
1. Click "🧙 Bắt đầu Trợ lý Chọn Kháng Sinh"
2. Select:
   - Vị trí nhiễm trùng (CAP, UTI, Sepsis, etc.)
   - Mức độ nặng (Nhẹ, Trung bình, Nặng, ICU)
   - Môi trường điều trị (Ngoại trú, Nội trú, ICU)
3. Check comorbidities và risk factors
4. Click "🔍 Nhận Đề xuất"
5. Review top 3 recommendations

#### Search
- Type vào search bar để tìm protocols
- Hoặc click quick suggestions: CAP, UTI, Sepsis, MRSA
- Search trong: infection name, drug name, guideline source

#### Filters (Sidebar)
- **Vị trí nhiễm trùng**: Multi-select
- **Mức độ nặng**: Multi-select
- **Môi trường điều trị**: Multi-select
- **Nguồn hướng dẫn**: Multi-select

#### Protocol Cards
- Color-coded theo severity
- Guideline badge với source + year
- Regimen cards với badges (Tuyến đầu, Thay thế, Cứu cánh)
- Recommendation level badges (Mạnh, Yếu, Có điều kiện)
- Drug details với links đến Drug Database
- TDM links cho vancomycin/aminoglycoside
- MIC breakpoints & susceptibility data
- Step-down options (IV → PO)
- Special populations notes

### 3. Actions

#### On Each Regimen Card
- **📖 Chi tiết**: Link đến Drug Database
- **📊 TDM**: Link đến TDM module (nếu applicable)
- **🔍 Tìm kiếm**: Link đến Global Search
- **🫁 Hồi sức**: Link đến Critical Care
- **💊 Thuốc**: Link đến Drug Database
- **📄 In**: Print protocol

#### Export
- Click "📥 Xuất danh sách" để export filtered protocols
- Download as .txt file
- Format: Plain text với structured data

### 4. Database Tab (Legacy Tools)

#### Features
- Search antibiotics by name, Vietnamese name, group, indication
- Filter by: Group, Route, AWaRe classification
- Favorites system
- Recent searches
- Recent calculations
- Condition-based search

#### Actions
- **📖 Chi tiết**: View full antibiotic information
- **🧮 Tính liều**: Open dosing calculator
- **⭐ Favorite**: Add/remove from favorites

---

## 🎯 Tính Năng Nổi Bật

### 1. Vietnamese-First Design
- 100% Vietnamese terminology
- English drug names (international standard)
- Vietnamese medical terms throughout

### 2. Evidence-Based
- Guideline references với years
- Recommendation levels (Strong/Weak/Conditional)
- Last reviewed dates
- Evidence grades (A/B/C)

### 3. Clinical Workflow Integration
- Seamless links giữa modules
- Context-aware suggestions
- Quick actions toolbar
- Print/export capabilities

### 4. Scientific Accuracy
- MIC breakpoints (CLSI, EUCAST)
- Vietnam resistance patterns
- Susceptibility data
- Clinical notes và warnings

### 5. Modern UI/UX
- Card-based design
- Color coding system
- Mobile-responsive
- Loading states
- Empty states
- Print-friendly

---

## 📊 Metrics & Performance

### Success Metrics
- ✅ 100% thuật ngữ được việt hóa
- ✅ UI/UX cải thiện rõ rệt
- ✅ Mobile optimization hoàn chỉnh
- ✅ Print/Export hoạt động tốt
- ✅ Integration seamless với các modules khác

### Performance Targets
- Page load: < 2s
- Search response: < 500ms
- Calculation time: < 100ms

---

## 🔄 Future Enhancements

### Phase 5 (Planned)
1. **By Drug Class Tab**: Organize by drug class với spectrum, indications, dosing
2. **Stewardship Tab**: De-escalation guidelines, IV→PO switch, duration recommendations
3. **More Protocols**: CNS infections, IAI, Endocarditis, Osteomyelitis
4. **Advanced Features**: 
   - Local resistance pattern integration
   - Cost comparison
   - Drug interaction checker integration
   - Monitoring recommendations
   - Treatment duration calculator
   - Dosing schedule generator

---

## 📚 References

### Guidelines
- IDSA/ATS Guidelines 2019
- Sanford Guide 2025
- Surviving Sepsis Campaign 2021
- WHO AWaRe Classification 2023

### Data Sources
- CLSI MIC Breakpoints
- EUCAST Breakpoints
- Vietnam Resistance Patterns (Local surveillance)
- Clinical experience và studies

---

## ✅ Checklist Hoàn Thành

### Phase 1: Việt Hóa
- [x] Schema & Enums với Vietnamese labels
- [x] UI Components việt hóa
- [x] Database & Display việt hóa
- [x] Wizard việt hóa

### Phase 2: UI/UX
- [x] Visual hierarchy & typography
- [x] Color coding system
- [x] Card design enhancement
- [x] Mobile optimization
- [x] Loading & empty states

### Phase 3: Tính Năng Khoa Học
- [x] MIC breakpoints integration
- [x] Resistance patterns (Vietnam)
- [x] Evidence levels & guidelines

### Phase 4: Workflow
- [x] Print & export
- [x] Integration improvements
- [x] Search enhancement
- [x] Comparison tools (existing)

---

## 📝 Notes

- Tên thuốc giữ nguyên tiếng Anh (chuẩn quốc tế)
- Enum values giữ nguyên tiếng Anh (để code dễ maintain)
- Vietnamese mapping centralized trong `vietnamese_terms.py`
- UI helpers centralized trong `ui_helpers.py`
- Tất cả protocols là summaries, không copy nguyên văn từ guidelines
- Guidelines được reference với year để version tracking

---

**Tác giả:** AI Assistant  
**Ngày hoàn thành:** 2025-02-18  
**Version:** 2.0
