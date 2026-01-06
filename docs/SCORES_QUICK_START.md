# Quick Start Guide - Trang Scores

## Bắt đầu nhanh

### 1. Khởi động ứng dụng
```bash
streamlit run pages/01_📊_Scores.py
```

### 2. Test Classic View
1. Mở trang Scores
2. Sidebar bên trái hiển thị:
   - Search bar
   - Filters
   - Specialty selection
   - Calculator list
3. Chọn specialty → Chọn calculator → Calculator hiển thị

### 3. Test Modern View
1. Click toggle "Modern View" ở đầu trang
2. Modern View hiển thị với:
   - Prominent search bar
   - 3 tabs: By Specialty Groups, Quick Access, All Calculators
3. Click calculator card để mở calculator

### 4. Test Geriatrics Module
1. Trong Modern View → Tab "By Specialty Groups"
2. Expand "👥 Special Populations"
3. Click "👴 Lão khoa (Geriatrics)"
4. Test các calculators:
   - Clinical Frailty Scale (CFS)
   - Morse Fall Scale
   - MMSE
   - MoCA
   - Beers Criteria
   - STOPP/START Criteria

### 5. Test Recent Tracking
1. Sử dụng một số calculators (bất kỳ)
2. Vào Modern View → Tab "Quick Access" → Tab "🕐 Recent"
3. Verify recent calculators hiển thị

## Tính năng chính

### Classic View
- Sidebar navigation
- Radio button selection
- Traditional layout

### Modern View
- Calculator cards grid
- Specialty groups
- Quick Access tabs
- Enhanced search

### Geriatrics Module
- 6 calculators cho elderly patients
- Frailty assessment
- Fall risk
- Cognitive screening
- Medication safety

### Recent Tracking
- Automatic tracking
- Quick Access integration
- Session persistence

## Troubleshooting

### Page không load
- Check console errors
- Verify imports
- Check file paths

### Calculator không hiển thị
- Check specialty routing
- Verify calculator ID
- Check module imports

### Modern View không hoạt động
- Check UI components import
- Verify specialty_groups.py
- Check session state

### Recent không track
- Check scores_recent.py import
- Verify session state
- Check button clicks

## Files quan trọng

- `pages/01_📊_Scores.py` - Main page
- `scores/ui_scores_view.py` - UI components
- `scores/geriatrics/` - Geriatrics module
- `components/scores_recent.py` - Recent tracking

## Documentation

- `docs/SCORES_TESTING_CHECKLIST.md` - Full testing guide
- `docs/SCORES_FINAL_SUMMARY.md` - Project summary
- `docs/GERIATRICS_MODULE_GUIDE.md` - Geriatrics guide
