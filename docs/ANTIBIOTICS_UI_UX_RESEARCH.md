# Nghiên cứu UI/UX cho Trang Antibiotics

## Tổng quan
Tài liệu này tổng hợp các pattern UI/UX tốt từ các ứng dụng và website y học hàng đầu để áp dụng vào trang Antibiotics của Clinical Assistant.

## 1. UpToDate - Pattern Navigation chính

### Layout Structure
- **Top Navigation**: Tabs theo workflow (Treatment, Diagnosis, Pathophysiology)
- **Sidebar Left**: Table of Contents với expandable sections
- **Main Content**: Structured content với:
  - Quick summary box ở đầu
  - Evidence-based recommendations với grade levels
  - Tables cho dosing regimens
  - Decision trees cho complex cases

### Key Features
- **Search bar prominent** ở top
- **Color coding**: Green (recommended), Yellow (alternative), Red (avoid)
- **Badges**: "Strong recommendation", "Weak recommendation", "Evidence level"
- **Quick links** đến related topics

### Áp dụng cho Antibiotics
- Tabs: "By Infection Site", "By Drug Class", "Stewardship"
- Sidebar filter: Infection type, Severity, Setting (OPD/IPD/ICU)
- Color-coded cards: First-line (green), Alternative (yellow), Rescue (red)

## 2. Sanford Guide (Web/App) - Pattern Empiric Selection

### Layout Structure
- **Main View**: Infection site-based navigation
- **Quick Access**: Most common infections ở top
- **Regimen Display**: 
  - Drug name + dose + frequency + duration
  - Indication (empiric vs targeted)
  - Notes về resistance patterns

### Key Features
- **Local resistance patterns** được highlight
- **Empiric vs Targeted** therapy clearly separated
- **Dosing adjustments** (renal, hepatic) inline
- **Step-down therapy** options highlighted

### Áp dụng cho Antibiotics
- Infection site accordion: CAP, HAP/VAP, UTI, SSTI, CNS, IAI
- Each infection có sub-sections: Non-severe, Severe, ICU
- Regimen cards với badges: "Empiric", "Targeted", "Step-down"

## 3. IDSA Guidelines Website - Pattern Evidence-based

### Layout Structure
- **Guideline Navigation**: By topic (Pneumonia, UTI, SSTI, etc.)
- **Content Structure**:
  - Executive Summary
  - Recommendations với strength (Strong/Weak) và quality (High/Moderate/Low)
  - Evidence tables
  - Implementation considerations

### Key Features
- **Recommendation grading**: Strong/Weak, High/Moderate/Low evidence
- **Special populations**: Pregnancy, Pediatrics, Immunocompromised
- **Resistance considerations**: MRSA, ESBL, CRE risk factors
- **Duration of therapy** clearly stated

### Áp dụng cho Antibiotics
- Badge system: "IDSA 2019", "ATS/IDSA 2019", "Sanford 2025"
- Recommendation levels: "Strong", "Weak", "Conditional"
- Special situations: Accordion cho Pregnancy, Pediatrics, Renal failure

## 4. Medscape - Pattern Quick Reference

### Layout Structure
- **Quick Reference Cards**: Condensed information
- **Drug Monographs**: Detailed với tabs (Overview, Dosing, Interactions)
- **Clinical Calculators**: Integrated dosing tools

### Key Features
- **Mobile-optimized**: Cards stack vertically
- **Quick facts** sidebar: Spectrum, PK/PD, Cost
- **Drug interactions** checker integrated
- **Dosing calculator** inline

### Áp dụng cho Antibiotics
- Mobile-first design: Stacked layout trên mobile
- Quick facts panel: Spectrum coverage, PK/PD properties
- Integration với Drug Interactions và TDM modules

## 5. BMJ Best Practice - Pattern Decision Support

### Layout Structure
- **Step-by-step approach**: Diagnosis → Treatment → Monitoring
- **Decision trees**: Visual flowcharts
- **Risk calculators**: Integrated tools

### Key Features
- **Wizard-style** interface cho complex decisions
- **Risk stratification** tools
- **Monitoring recommendations** post-treatment
- **Follow-up** guidance

### Áp dụng cho Antibiotics
- Antibiotic Wizard: Form-based selection
  - Site of infection
  - Severity
  - Comorbidities
  - Allergy status
- Output: 1-3 recommended regimens với rationale

## Pattern Tổng hợp để Áp dụng

### 1. Navigation Structure
```
Top Tabs (3):
├── By Infection Site
│   ├── CAP (non-severe / severe / ICU)
│   ├── HAP/VAP
│   ├── UTI (uncomplicated / complicated)
│   ├── SSTI (mild / moderate / severe)
│   ├── CNS (meningitis / encephalitis)
│   └── IAI / Bacteremia / Sepsis
├── By Drug Class
│   ├── Beta-lactams
│   ├── Fluoroquinolones
│   ├── Macrolides
│   ├── Glycopeptides
│   └── Carbapenems
└── Stewardship & Dosing
    ├── De-escalation
    ├── IV → PO switch
    └── Renal dosing summary
```

### 2. UI Components

#### Cards với Color Coding
- **Green**: First-line recommendations
- **Yellow**: Alternative options
- **Red**: Rescue therapy / ICU
- **Blue**: Step-down / Oral options

#### Badges
- "First-line", "Alternative", "Rescue"
- "IDSA 2019", "ATS/IDSA 2019", "Sanford 2025"
- "Empiric", "Targeted", "Step-down"
- "Strong", "Weak", "Conditional"

#### Filters (Sidebar)
- Infection site (multi-select)
- Severity (mild / moderate / severe)
- Setting (OPD / Ward / ICU)
- Guideline source (IDSA / ATS / Sanford)
- Special situations (Pregnancy / Pediatrics / Renal)

#### Search
- In-page search bar
- Filter by: Infection name, Organism, Antibiotic name
- Autocomplete suggestions

### 3. Regimen Display Format

```
┌─────────────────────────────────────────┐
│ First-line Regimen                      │
│ ─────────────────────────────────────── │
│ Drug: Ceftriaxone 2g IV                 │
│ Frequency: Once daily                   │
│ Duration: 7-10 days                     │
│                                         │
│ Indication: CAP non-severe             │
│ Guideline: IDSA/ATS 2019               │
│ Evidence: Strong recommendation        │
│                                         │
│ ⚠️ Renal adjustment: CrCl <10 → reduce │
│ 💊 Step-down: Cefuroxime 500mg PO BID  │
└─────────────────────────────────────────┘
```

### 4. Mobile Optimization
- **Stacked layout**: Filters → Content → Quick facts
- **Touch-friendly**: Buttons min 48px height
- **Collapsible sections**: Accordion cho mỗi infection
- **Quick action button**: "Start Antibiotic Wizard" prominent

### 5. Integration Points
- **Drug Detail**: Link từ mỗi regimen
- **TDM**: Auto-link khi chọn vancomycin/aminoglycoside
- **Critical Care**: Link cho sepsis/severe infections
- **Drug Interactions**: Checker khi chọn multiple drugs

## Implementation Priority

### Phase 1 (High Priority)
1. ✅ Navigation tabs (By Infection / By Drug Class / Stewardship)
2. ✅ Sidebar filters
3. ✅ Color-coded regimen cards
4. ✅ Badge system
5. ✅ Mobile-responsive layout

### Phase 2 (Medium Priority)
1. In-page search
2. Antibiotic Wizard (basic version)
3. Integration với Drug Detail
4. Quick facts panel

### Phase 3 (Lower Priority)
1. Stewardship dashboard
2. Advanced filters (resistance patterns)
3. Local resistance data integration

## References
- UpToDate: https://www.uptodate.com
- Sanford Guide: https://www.sanfordguide.com
- IDSA Guidelines: https://www.idsociety.org/practice-guideline/
- Medscape: https://www.medscape.com
- BMJ Best Practice: https://bestpractice.bmj.com
