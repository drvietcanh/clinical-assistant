# Testing Checklist - Trang Scores Optimization

## Desktop Testing

### Classic View
- [ ] Page loads correctly
- [ ] Sidebar navigation works
- [ ] Specialty selection works
- [ ] Calculator selection (radio buttons) works
- [ ] Search functionality works
- [ ] Filters work (status, daily use)
- [ ] Calculator rendering works for all specialties
- [ ] Favorites system works
- [ ] Theme toggle works
- [ ] Related calculators display
- [ ] References display

### Modern View
- [ ] Toggle between Classic/Modern works
- [ ] Modern View loads correctly
- [ ] Search bar prominent and functional
- [ ] Tabs work: By Specialty Groups, Quick Access, All Calculators
- [ ] Specialty groups expand/collapse correctly
- [ ] Calculator cards render correctly
- [ ] Calculator cards grid responsive (3 columns desktop)
- [ ] Click calculator card opens calculator
- [ ] Quick Access tabs work:
  - [ ] Most Used displays daily use calculators
  - [ ] Recent displays recently viewed
  - [ ] Favorites displays starred calculators
- [ ] Filters in "All Calculators" tab work
- [ ] Calculator routing works for all specialties
- [ ] Geriatrics calculators work in Modern View

### Search & Navigation
- [ ] Global search finds calculators
- [ ] Search autocomplete works
- [ ] Search results clickable
- [ ] Local search within specialty works
- [ ] Search history tracking (if implemented)

### Recent Tracking
- [ ] Recent calculators tracked when selected
- [ ] Recent list displays in Quick Access
- [ ] Recent list limited to 20 items
- [ ] Recent persists in session
- [ ] Recent works in both Classic and Modern View

## Mobile Testing

### Responsive Design
- [ ] Page loads on mobile (iPhone, Android)
- [ ] Sidebar accessible on mobile
- [ ] Calculator cards stack vertically on mobile (1 column)
- [ ] Calculator cards display correctly on tablet (2 columns)
- [ ] Touch targets adequate size (≥44px)
- [ ] Text readable without zooming
- [ ] Buttons touch-friendly
- [ ] Search input doesn't cause zoom on iOS
- [ ] Filters accessible on mobile
- [ ] Tabs work on mobile

### Classic View Mobile
- [ ] Sidebar navigation works
- [ ] Specialty selection works
- [ ] Calculator radio buttons touch-friendly
- [ ] Calculator rendering works
- [ ] Scrollable content

### Modern View Mobile
- [ ] Toggle works on mobile
- [ ] Search bar prominent
- [ ] Tabs accessible
- [ ] Calculator cards stack correctly
- [ ] Cards readable on small screens
- [ ] Button text appropriate length
- [ ] Quick Access tabs work
- [ ] Filters work on mobile

### Mobile-Specific Features
- [ ] Bottom navigation (if implemented)
- [ ] Swipe gestures (if implemented)
- [ ] Landscape orientation support
- [ ] Dark mode on mobile

## Cross-Browser Testing

- [ ] Chrome (desktop & mobile)
- [ ] Firefox (desktop & mobile)
- [ ] Safari (desktop & mobile)
- [ ] Edge (desktop & mobile)

## Performance Testing

- [ ] Page load time < 3 seconds
- [ ] Calculator cards render quickly
- [ ] Search responsive (no lag)
- [ ] Large specialty groups load efficiently
- [ ] No memory leaks with multiple calculator views
- [ ] Smooth scrolling
- [ ] Smooth transitions

## Functionality Testing

### All Specialties
- [ ] Emergency & Critical Care calculators work
- [ ] Cardiology calculators work
- [ ] Respiratory calculators work
- [ ] Neurology calculators work
- [ ] GI/Hepatology calculators work
- [ ] Hematology calculators work
- [ ] Nephrology calculators work
- [ ] Trauma calculators work
- [ ] Psychiatry calculators work
- [ ] Oncology calculators work
- [ ] Surgery calculators work
- [ ] Pediatrics calculators work
- [ ] Infectious Disease calculators work
- [ ] ENT calculators work
- [ ] Obstetrics calculators work
- [ ] Dermatology calculators work
- [ ] Rheumatology calculators work
- [ ] Ophthalmology calculators work
- [ ] Pain Assessment calculators work
- [ ] Nursing Care calculators work
- [ ] **Geriatrics calculators work** ⭐ NEW

### Geriatrics Module (Phase 1)
- [ ] Clinical Frailty Scale (CFS) works
- [ ] Morse Fall Scale works
- [ ] MMSE works
- [ ] MoCA works
- [ ] Beers Criteria works
- [ ] STOPP/START Criteria works

## Edge Cases

- [ ] Empty search results handled
- [ ] No calculators in specialty handled
- [ ] Invalid calculator ID handled
- [ ] Missing specialty handled
- [ ] Session state persistence
- [ ] Multiple rapid clicks handled
- [ ] Very long calculator names display correctly
- [ ] Very long descriptions truncate correctly

## Accessibility Testing

- [ ] Keyboard navigation works
- [ ] Screen reader compatible (if applicable)
- [ ] Color contrast adequate
- [ ] Focus indicators visible
- [ ] ARIA labels (if applicable)

## Integration Testing

- [ ] Works with Global Search
- [ ] Works with Favorites system
- [ ] Works with Dark Mode
- [ ] Works with Mobile optimizations
- [ ] Works with Related Calculators
- [ ] Works with References

## User Experience Testing

- [ ] Intuitive navigation
- [ ] Clear visual hierarchy
- [ ] Easy to find calculators
- [ ] Quick access to frequently used
- [ ] Smooth transitions
- [ ] Helpful error messages
- [ ] Clear status indicators

## Regression Testing

- [ ] Existing functionality still works
- [ ] No broken links
- [ ] No console errors
- [ ] No broken imports
- [ ] All modules load correctly

## Documentation Testing

- [ ] Documentation accurate
- [ ] Examples work
- [ ] Code snippets correct
- [ ] Links work

## Test Results Template

```
Date: ___________
Tester: ___________
Browser: ___________
Device: ___________

### Passed Tests
- 

### Failed Tests
- 

### Issues Found
1. 
2. 
3. 

### Notes
- 

### Recommendations
- 
```

## Priority Issues to Fix

### Critical (Must Fix)
- [ ] Calculator routing broken
- [ ] Page doesn't load
- [ ] Mobile unusable
- [ ] Data loss

### High Priority (Should Fix)
- [ ] Performance issues
- [ ] UI glitches
- [ ] Missing functionality
- [ ] Poor mobile experience

### Medium Priority (Nice to Have)
- [ ] UI improvements
- [ ] Additional features
- [ ] Better error messages
- [ ] Enhanced accessibility

### Low Priority (Future)
- [ ] Nice-to-have features
- [ ] Advanced optimizations
- [ ] Additional integrations
