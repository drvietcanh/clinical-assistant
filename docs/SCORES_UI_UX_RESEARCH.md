# Nghiên cứu UI/UX cho Trang Scores/Calculators

## Tổng quan
Tài liệu này tổng hợp các pattern UI/UX tốt từ các ứng dụng và website y học hàng đầu để áp dụng vào trang Scores/Calculators của Clinical Assistant.

## 1. MDCalc (mdcalc.com) - Gold Standard

### Layout Structure
- **Top Navigation Bar**: 
  - Categories dropdown (Cardiology, Emergency, Neurology, etc.)
  - Search bar prominent ở center
  - Mobile menu (hamburger)
- **Main Content**:
  - Specialty landing pages với calculator grid
  - Calculator cards: Icon + Name + Brief description
  - Usage frequency indicators
  - Quick access buttons
- **Calculator Detail Page**:
  - Clean, focused input form
  - Results prominent
  - References và interpretation

### Key Features
- **Search**: Real-time autocomplete, searches name và description
- **Categories**: Organized by specialty, có "Most Used" section
- **Calculator Cards**: 
  - Large icons
  - One-line description
  - "Use Calculator" button
  - Star icon for favorites
- **Mobile**: Bottom navigation bar với quick access

### Áp dụng cho Scores
- Grid layout cho calculator cards (3-4 columns desktop)
- Prominent search bar với autocomplete
- Category-based navigation với expandable sections
- Mobile bottom navigation cho quick access

## 2. UpToDate - Evidence-based Pattern

### Layout Structure
- **Sidebar Navigation**: 
  - Expandable specialty tree
  - Table of contents cho mỗi calculator
- **Main Content**:
  - Structured sections
  - Evidence level badges (Strong, Weak recommendation)
  - Inline references
  - Related calculators suggestions

### Key Features
- **Evidence Level**: Visual badges cho recommendation strength
- **References**: Inline citations, expandable references section
- **Related Content**: Suggestions ở cuối mỗi calculator
- **Print/Export**: Options để export calculator results

### Áp dụng cho Scores
- Evidence level badges trên calculator cards
- References section trong calculator detail
- Related calculators suggestions
- Export/print functionality

## 3. Medscape - Quick Reference Pattern

### Layout Structure
- **Quick Categories**: Most used calculators ở top
- **Alphabetical Index**: Cho advanced users
- **Category Grid**: Icons với specialty names
- **Search**: Quick search với filters

### Key Features
- **Most Used**: Prominent display của popular calculators
- **Favorites**: Star system với favorites page
- **Recent**: Recently viewed calculators
- **Filters**: By specialty, by category, by evidence level

### Áp dụng cho Scores
- Quick access section: Most used, Recent, Favorites
- Alphabetical index cho advanced search
- Enhanced filters trong sidebar
- Favorites với star system

## 4. BMJ Best Practice - Decision Support Pattern

### Layout Structure
- **Step-by-step**: Guided workflow
- **Decision Trees**: Visual flowcharts
- **Risk Calculators**: Integrated tools
- **Monitoring**: Follow-up recommendations

### Key Features
- **Wizard-style**: Step-by-step calculation process
- **Context-aware**: Suggestions based on inputs
- **Integration**: Links to related guidelines
- **Mobile-first**: Optimized for mobile use

### Áp dụng cho Scores
- Wizard mode cho complex calculators
- Context-aware suggestions
- Integration với protocols và guidelines
- Mobile-first design

## 5. QxMD Calculate - Mobile App Pattern

### Layout Structure
- **Bottom Navigation**: Quick access to categories
- **Card-based**: Large touch-friendly cards
- **Swipe Gestures**: Navigate between calculators
- **Offline Support**: Cached calculators

### Key Features
- **Bottom Navigation**: Fixed bar với categories
- **Large Cards**: Touch-friendly, icon + name
- **Swipe**: Swipe left/right between calculators
- **Offline**: Cache frequently used calculators
- **History**: Calculation history tracking

### Áp dụng cho Scores
- Bottom navigation cho mobile
- Large touch-friendly calculator cards
- Swipe gestures
- Offline caching
- Calculation history

## Pattern Tổng hợp để Áp dụng

### 1. Navigation Structure

#### Desktop
```
Top: Search Bar (Prominent)
├── Sidebar (Left)
│   ├── Quick Access
│   │   ├── Most Used
│   │   ├── Recent
│   │   └── Favorites
│   ├── Main Groups (Collapsible)
│   │   ├── Critical Care & Emergency
│   │   ├── Organ Systems
│   │   ├── Special Populations
│   │   └── Specialized Fields
│   └── Filters
│       ├── By Status
│       ├── By Usage
│       └── By Category
└── Main Content
    ├── Specialty Tabs (if needed)
    └── Calculator Grid/Cards
```

#### Mobile
```
Top: Search Bar
├── Quick Access Tabs (Most Used, Recent, Favorites)
├── Specialty Accordion
│   ├── ▼ Critical Care
│   │   ├── Emergency
│   │   └── ICU Scores
│   ├── ▼ Organ Systems
│   │   ├── Cardiology
│   │   └── ...
│   └── ▶ Special Populations
└── Calculator Cards (Stacked)
    └── Bottom Navigation (Fixed)
```

### 2. Calculator Card Design

```
┌─────────────────────────────────┐
│ [Icon] Calculator Name          │
│                                 │
│ Brief description (1-2 lines)   │
│                                 │
│ [⭐ Daily Use] [✅] [🔥 Popular] │
│                                 │
│ [Use Calculator] Button         │
└─────────────────────────────────┘
```

**Card Elements**:
- **Icon**: Specialty-specific, large (48px+)
- **Name**: Bold, clear
- **Description**: 1-2 lines, concise
- **Badges**: Daily Use ⭐, New 🆕, Popular 🔥
- **Status**: ✅ Complete, 🚧 In Progress, 📋 Planned
- **Button**: Primary action "Use Calculator"

### 3. Search Enhancement

- **Position**: Top, prominent, full-width
- **Features**:
  - Autocomplete với suggestions (real-time)
  - Search history dropdown
  - Quick filters: "Most Used", "By Specialty", "Daily Use"
  - Keyboard shortcut: Ctrl+K (focus search)
  - Fuzzy search: Tìm gần đúng
- **Results**: 
  - Highlight matched terms
  - Group by specialty
  - Show context (description snippet)

### 4. Specialty Grouping

#### Group 1: Critical Care & Emergency (High Priority)
- Emergency & Critical Care
- Trauma & Surgery

#### Group 2: Organ Systems
- Cardiovascular (Tim mạch)
- Respiratory (Hô hấp)
- Neurology (Thần kinh)
- Gastroenterology & Hepatology
- Nephrology (Thận)
- Hematology (Huyết học)

#### Group 3: Special Populations
- **Geriatrics** ⭐ NEW
- Pediatrics (Nhi khoa)
- Obstetrics (Sản khoa)

#### Group 4: Specialized Fields
- Metabolism & Endocrinology
- Infectious Diseases
- Oncology
- Psychiatry
- Rheumatology
- Dermatology
- ENT
- Ophthalmology
- Pain Management
- Nursing

### 5. Filters & Sorting

#### By Status
- ✅ Complete
- 🚧 In Progress
- 📋 Planned

#### By Usage
- ⭐ Daily Use
- 🔥 Popular (most accessed)
- 🆕 New (recently added)

#### By Category
- Risk Scores
- Severity Scores
- Prognostic Scores
- Diagnostic Scores
- Functional Assessment

#### By Evidence Level
- Strong Evidence
- Moderate Evidence
- Weak Evidence

#### Sorting Options
- Alphabetical
- Most Used
- Recently Added
- By Specialty

### 6. Quick Access Features

#### Most Used
- Top 10 calculators by usage
- Tracked via analytics
- Display as cards grid

#### Recent
- Last 10 calculators viewed
- Stored in session/localStorage
- Quick access list

#### Favorites
- Star system
- User can favorite any calculator
- Favorites page/ section

#### By Workflow
- Emergency workflow: NEWS2 → SOFA → qSOFA
- Cardiology: ASCVD → CHA2DS2-VASc → HAS-BLED
- Pre-op: RCRI → P-POSSUM → ARISCAT

### 7. Mobile Optimization

#### Bottom Navigation
- Fixed at bottom
- Icons: Home, Search, Favorites, Categories, More
- Touch-friendly (48px+)

#### Swipe Gestures
- Swipe left/right: Navigate between calculators in same specialty
- Swipe up: Show details
- Swipe down: Hide keyboard

#### Touch Targets
- Minimum 44px height/width
- Adequate spacing between elements
- Large calculator cards

#### Responsive Grid
- Desktop: 3-4 columns
- Tablet: 2-3 columns
- Mobile: 1-2 columns

### 8. Calculator Display Improvements

#### Quick Preview
- Modal hoặc expandable preview
- Show key inputs và outputs
- "Open Full Calculator" button

#### Enhanced Results
- Visual results (charts, graphs if applicable)
- Clear interpretation
- Next steps/recommendations
- References inline

#### Related Calculators
- Suggested at bottom of calculator
- Based on specialty, category, workflow
- "People also used" pattern

### 9. Integration Points

#### With Protocols
- Link to relevant protocols từ calculator results
- Example: SOFA → Sepsis Protocol

#### With Drug Database
- Link to drug dosing calculators
- Example: CrCl → Drug dosing adjustment

#### With Critical Care
- Link to ICU protocols
- Example: APACHE → Critical Care protocols

#### With Global Search
- Integrated search across all modules
- Calculator results trong global search

## Implementation Priority

### Phase 1 (High Priority)
1. ✅ Enhanced search với autocomplete
2. ✅ Calculator cards với badges
3. ✅ Specialty grouping với collapsible sections
4. ✅ Mobile-responsive grid
5. ✅ Quick Access (Most Used, Recent, Favorites)

### Phase 2 (Medium Priority)
1. Bottom navigation cho mobile
2. Swipe gestures
3. Calculator preview
4. Enhanced filters
5. Evidence level badges

### Phase 3 (Lower Priority)
1. Export/Print functionality
2. Calculation history
3. Calculator comparison
4. Custom calculator sets
5. Offline support

## References
- MDCalc: https://www.mdcalc.com
- UpToDate: https://www.uptodate.com
- Medscape: https://www.medscape.com
- BMJ Best Practice: https://bestpractice.bmj.com
- QxMD Calculate: Mobile app

## Key Takeaways

1. **Search is critical**: Make it prominent, fast, với autocomplete
2. **Cards over lists**: Visual cards easier to scan
3. **Group logically**: Organize by workflow và specialty
4. **Mobile-first**: Bottom nav, large touch targets, swipe gestures
5. **Quick access matters**: Most used, recent, favorites
6. **Visual hierarchy**: Clear icons, badges, status indicators
7. **Integration**: Link related content (protocols, drugs, guidelines)
