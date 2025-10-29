# Changelog - Clinical Assistant

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Planned
- SOFA score calculator
- CHA₂DS₂-VASc score
- HAS-BLED score
- Vancomycin dosing calculator
- ARDSNet ventilator calculator
- Drug interactions checker
- Offline PWA mode
- Multi-language support (Vietnamese/English)

---

## [1.0.0] - 2025-10-29

### Added
- **Core Infrastructure**
  - Single Page Application (SPA) architecture
  - Module system for easy expansion
  - Google Apps Script backend
  - Google Sheets database integration
  - Caching system for performance
  - Version control via Meta sheet

- **Module: Scores**
  - qSOFA calculator (demo implementation)
  - Framework for additional scoring systems

- **Module: Antibiotics**
  - Basic structure
  - Data schema for antibiotic dosing

- **Module: Ventilator**
  - Basic structure
  - ARDSNet data tables

- **Module: Protocols**
  - Basic structure
  - COPD exacerbation protocol data

- **UI/UX**
  - Mobile-responsive design
  - Clean, minimal interface
  - Card-based layout
  - Navigation system (hash-based routing)
  - Shared utility functions (el() helper)

- **Documentation**
  - QUICKSTART.md - 30-minute setup guide
  - ROADMAP.md - Comprehensive development roadmap
  - IMPLEMENTATION_GUIDE.md - Detailed module implementation
  - DEPLOYMENT.md - Deploy & DevOps guide
  - RESOURCES.md - Clinical & technical references
  - SIMILAR_APPS.md - Competitor analysis
  - Templates for new modules

- **Data**
  - Initial clinical data (CSV format)
    - Scores: qSOFA
    - Antibiotics: Cefepime, Pip/Tazo, Vancomycin
    - Ventilator: ARDSNet PEEP/FiO2 tables
    - Protocols: COPD exacerbation
  - Meta version control
  - Citation tracking

### Technical
- Google Apps Script V8 runtime
- ES6 JavaScript syntax
- Vanilla JS (no frameworks)
- HTML5/CSS3 responsive design
- CacheService for performance (10min TTL)
- Asia/Ho_Chi_Minh timezone

### Security
- No PHI storage
- Session-based user tracking (anonymous)
- Input validation
- Error logging without sensitive data

---

## [0.9.0] - 2025-10-28 (Internal Beta)

### Added
- Initial project structure
- Basic SPA framework
- Sample data collection
- Clinical reference gathering

### Testing
- Internal testing with 5 physicians
- Feedback collection
- Performance baseline

---

## Version Numbering

- **MAJOR** (x.0.0): Breaking changes, major rewrites
- **MINOR** (0.x.0): New features, backwards compatible
- **PATCH** (0.0.x): Bug fixes, minor improvements

---

## Future Versions

### [1.1.0] - Planned 2025-11-15
- SOFA score (complete implementation)
- CHA₂DS₂-VASc score
- Vancomycin calculator with CrCl
- PWA manifest for offline support

### [1.2.0] - Planned 2025-12-01
- ARDSNet ventilator calculator
- PBW calculation
- PEEP/FiO2 recommendation engine
- Dark mode

### [2.0.0] - Planned 2026-Q1
- Multi-language support
- User authentication
- Favorites & history sync
- Advanced analytics dashboard
- AI-powered recommendations (if feasible)

---

## Migration Notes

### Upgrading from 0.9.0 to 1.0.0
- No breaking changes
- Data structure unchanged
- Clear browser cache for best performance
- Update deployment URL if changed

---

## Contributors

### Version 1.0.0
- **Clinical Content**: Dr. Nguyen A., Dr. Tran B.
- **Development**: IT Team Lead, Clinical Informatics
- **Testing**: ICU Team, Emergency Department

---

## References Updated

Each version includes updates to clinical references. Current guidelines:
- Sepsis-3 (JAMA 2016) - qSOFA, SOFA
- GOLD 2025 - COPD management
- IDSA/ATS 2016 - HAP/VAP
- ARDSNet 2000 - Low tidal volume ventilation
- FDA Labels (2024-2025) - Antibiotic dosing

---

## Known Issues

### Version 1.0.0
- [ ] qSOFA threshold at systolic BP should be ≤100 (currently using <100) - **Fixed in 1.0.1**
- [ ] Mobile keyboard may cover inputs on some Android devices - **Investigating**
- [ ] Cache not clearing automatically after version update - **Workaround: Manual clear**

---

## Deprecation Notices

None for version 1.0.0.

---

**Maintained by:** Clinical IT Team  
**Contact:** clinical-it@hospital.com  
**Repository:** https://github.com/your-hospital/clinical-assistant

---

## Template for Future Entries

```markdown
## [X.Y.Z] - YYYY-MM-DD

### Added
- New feature 1
- New feature 2

### Changed
- Modified feature 1
- Updated data X

### Fixed
- Bug fix 1
- Issue #123

### Deprecated
- Old feature X (will be removed in vX.Y.Z)

### Removed
- Deprecated feature Y

### Security
- Security improvement 1
```

