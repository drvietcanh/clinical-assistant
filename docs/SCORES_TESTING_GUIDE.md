# 🧪 Testing Guide - Scores Page Improvements

**Ngày:** 2025-02-18  
**Mục đích:** Hướng dẫn test và checklist cho các tính năng mới

---

## 📋 MỤC LỤC

1. [Test Checklist](#test-checklist)
2. [Test Cases](#test-cases)
3. [Test Scenarios](#test-scenarios)
4. [Performance Testing](#performance-testing)
5. [Browser Compatibility](#browser-compatibility)
6. [Mobile Testing](#mobile-testing)

---

## ✅ TEST CHECKLIST

### Phase 1: Quick Wins

#### 1. 🔍 Global Search
- [ ] Search với từ khóa ngắn (2+ ký tự)
- [ ] Search với từ khóa dài
- [ ] Search với viết tắt (Wells, CHA2DS2-VASc)
- [ ] Search với tên đầy đủ
- [ ] Search không có kết quả
- [ ] Search với special characters
- [ ] Search case-insensitive
- [ ] Kết quả hiển thị đúng specialty
- [ ] Click vào kết quả chuyển đúng calculator

#### 2. 🔧 Advanced Filters
- [ ] Filter theo status ✅
- [ ] Filter theo status 🚧
- [ ] Filter theo status 📋
- [ ] Filter multiple status
- [ ] Filter daily use ⭐
- [ ] Kết hợp filter với search
- [ ] Clear filters
- [ ] Filter với empty results

#### 3. ⭐ Favorites
- [ ] Add favorite từ header button
- [ ] Remove favorite từ header button
- [ ] Add favorite từ sidebar
- [ ] Remove favorite từ sidebar
- [ ] Favorites hiển thị trong sidebar
- [ ] Click favorite mở đúng calculator
- [ ] Favorites persist trong session
- [ ] Favorites với nhiều calculators

#### 4. 🎨 Color Coding
- [ ] Risk badge hiển thị đúng màu
- [ ] Risk bar hiển thị đúng màu
- [ ] Risk table hiển thị đúng màu
- [ ] Very low (green)
- [ ] Low (light green)
- [ ] Moderate (yellow/orange)
- [ ] High (orange)
- [ ] Very high (red)
- [ ] Critical (dark red)
- [ ] Accessible colors (WCAG)

#### 5. 📊 Visual Charts
- [ ] Risk bar chart render
- [ ] Risk gauge chart render
- [ ] Risk pie chart render
- [ ] Comparison chart render
- [ ] Trend line chart render
- [ ] Charts responsive trên mobile
- [ ] Charts hiển thị đúng data
- [ ] Charts với dark mode

#### 6. 🌙 Dark Mode
- [ ] Toggle dark mode
- [ ] Toggle light mode
- [ ] Theme persist trong session
- [ ] Dark mode CSS apply đúng
- [ ] All components hiển thị đúng trong dark mode
- [ ] Charts hiển thị đúng trong dark mode

#### 7. 📤 Export/Print
- [ ] Export to TXT
- [ ] Export to CSV
- [ ] Copy to clipboard
- [ ] Print functionality
- [ ] Export format đúng
- [ ] Export include inputs
- [ ] Export include results
- [ ] Export include metadata

### Phase 2: Enhanced Features

#### 8. 🔍 Autocomplete/Suggestions
- [ ] Suggestions hiển thị khi typing
- [ ] Popular searches hiển thị
- [ ] Recent searches hiển thị
- [ ] Click suggestion chuyển đúng calculator
- [ ] Fuzzy matching hoạt động
- [ ] Relevance scoring đúng
- [ ] Recent searches được lưu
- [ ] Suggestions limit đúng

#### 9. 📋 Related Calculators
- [ ] Related calculators hiển thị
- [ ] Related từ cùng specialty
- [ ] Related từ keywords
- [ ] Relevance scoring đúng
- [ ] Click related mở đúng calculator
- [ ] Related limit đúng (5)
- [ ] Related không hiển thị chính nó

#### 10. 📱 Mobile Layout
- [ ] Responsive trên mobile (< 768px)
- [ ] Responsive trên tablet (769-1024px)
- [ ] Touch-friendly buttons (44px)
- [ ] Sidebar tối ưu mobile
- [ ] Charts responsive
- [ ] Tables scrollable
- [ ] Landscape orientation
- [ ] Dark mode mobile

---

## 🧪 TEST CASES

### TC-001: Global Search
**Mục đích:** Test tìm kiếm toàn cục

**Steps:**
1. Mở trang Scores
2. Nhập "Wells" vào global search
3. Xem kết quả

**Expected:**
- Hiển thị Wells DVT và Wells PE
- Kết quả có specialty context
- Click vào kết quả chuyển đúng calculator

**Actual:** [ ] Pass [ ] Fail

---

### TC-002: Advanced Filters
**Mục đích:** Test filters

**Steps:**
1. Mở Advanced Filters
2. Chọn status ✅
3. Check "Daily use ⭐"
4. Xem kết quả

**Expected:**
- Chỉ hiển thị calculators với status ✅
- Chỉ hiển thị daily use calculators
- Kết quả được filter đúng

**Actual:** [ ] Pass [ ] Fail

---

### TC-003: Favorites
**Mục đích:** Test favorites system

**Steps:**
1. Chọn calculator
2. Click "⭐ Đánh dấu"
3. Xem sidebar favorites
4. Click vào favorite

**Expected:**
- Favorite được thêm
- Hiển thị trong sidebar
- Click mở đúng calculator

**Actual:** [ ] Pass [ ] Fail

---

### TC-004: Color Coding
**Mục đích:** Test color coding

**Steps:**
1. Mở calculator có risk score
2. Xem risk badge
3. Xem risk bar
4. Xem risk table

**Expected:**
- Badge hiển thị đúng màu
- Bar hiển thị đúng màu
- Table hiển thị đúng màu
- Màu accessible

**Actual:** [ ] Pass [ ] Fail

---

### TC-005: Visual Charts
**Mục đích:** Test charts

**Steps:**
1. Mở calculator có charts
2. Xem gauge chart
3. Xem bar chart
4. Resize window

**Expected:**
- Charts render đúng
- Charts responsive
- Charts hiển thị đúng data

**Actual:** [ ] Pass [ ] Fail

---

### TC-006: Dark Mode
**Mục đích:** Test dark mode

**Steps:**
1. Click "🌙 Dark Mode"
2. Xem theme change
3. Refresh page
4. Xem theme persist

**Expected:**
- Theme chuyển sang dark
- CSS apply đúng
- Theme persist sau refresh

**Actual:** [ ] Pass [ ] Fail

---

### TC-007: Export
**Mục đích:** Test export functionality

**Steps:**
1. Tính toán calculator
2. Click "📤 Xuất kết quả"
3. Download TXT
4. Download CSV

**Expected:**
- TXT file download
- CSV file download
- Format đúng
- Include inputs và results

**Actual:** [ ] Pass [ ] Fail

---

### TC-008: Autocomplete
**Mục đích:** Test autocomplete

**Steps:**
1. Nhập "CHA" vào search
2. Xem suggestions
3. Click suggestion

**Expected:**
- Suggestions hiển thị
- CHA2DS2-VASc trong suggestions
- Click chuyển đúng calculator

**Actual:** [ ] Pass [ ] Fail

---

### TC-009: Related Calculators
**Mục đích:** Test related calculators

**Steps:**
1. Mở CHA2DS2-VASc calculator
2. Scroll xuống
3. Xem related calculators

**Expected:**
- Hiển thị related calculators
- HAS-BLED trong related
- Click mở đúng calculator

**Actual:** [ ] Pass [ ] Fail

---

### TC-010: Mobile Layout
**Mục đích:** Test mobile responsive

**Steps:**
1. Mở trên mobile (< 768px)
2. Test sidebar
3. Test buttons
4. Test charts
5. Test landscape

**Expected:**
- Layout responsive
- Buttons touch-friendly
- Charts responsive
- Landscape optimized

**Actual:** [ ] Pass [ ] Fail

---

## 🎭 TEST SCENARIOS

### Scenario 1: User Journey - Tìm Calculator
1. User mở trang Scores
2. User nhập "Wells" vào search
3. Xem suggestions
4. Click vào "Wells DVT Score"
5. Calculator mở
6. User thêm vào favorites
7. User xem related calculators
8. User export kết quả

**Expected:** Tất cả bước hoạt động mượt mà

---

### Scenario 2: User Journey - Filter & Browse
1. User mở Advanced Filters
2. Filter theo status ✅ và daily use ⭐
3. Browse calculators
4. Chọn calculator
5. Toggle dark mode
6. Xem charts
7. Export kết quả

**Expected:** Filter hoạt động, dark mode toggle, charts hiển thị

---

### Scenario 3: Mobile User Journey
1. User mở trên mobile
2. Search calculator
3. Chọn calculator
4. Tính toán
5. Xem kết quả
6. Export

**Expected:** Tất cả hoạt động tốt trên mobile

---

## ⚡ PERFORMANCE TESTING

### Load Time
- [ ] Page load < 2s
- [ ] Search results < 500ms
- [ ] Charts render < 1s
- [ ] Filter apply < 300ms

### Memory
- [ ] No memory leaks
- [ ] Session state manageable
- [ ] Charts cleanup properly

### Large Dataset
- [ ] Search với 300+ calculators
- [ ] Filter với 300+ calculators
- [ ] Related với 300+ calculators
- [ ] Performance acceptable

---

## 🌐 BROWSER COMPATIBILITY

### Desktop Browsers
- [ ] Chrome (latest)
- [ ] Firefox (latest)
- [ ] Safari (latest)
- [ ] Edge (latest)

### Mobile Browsers
- [ ] Chrome Mobile
- [ ] Safari iOS
- [ ] Samsung Internet

### Features
- [ ] Dark mode works
- [ ] Charts render
- [ ] Export works
- [ ] Responsive works

---

## 📱 MOBILE TESTING

### Devices
- [ ] iPhone (various sizes)
- [ ] Android (various sizes)
- [ ] Tablet (iPad, Android)

### Orientations
- [ ] Portrait
- [ ] Landscape

### Touch
- [ ] Buttons touch-friendly
- [ ] Swipe gestures (if any)
- [ ] Scroll smooth

### Performance
- [ ] Load time acceptable
- [ ] Smooth scrolling
- [ ] No lag

---

## 🐛 KNOWN ISSUES

### Current Issues
1. **Favorites persistence:** Chỉ lưu trong session, mất khi refresh
   - **Workaround:** Sử dụng localStorage (future enhancement)
   - **Priority:** Medium

2. **Global search performance:** Có thể chậm với 300+ calculators
   - **Workaround:** Limit results, optimize algorithm
   - **Priority:** Low

3. **Color coding:** Chưa tích hợp vào tất cả calculators
   - **Workaround:** Tích hợp từng calculator
   - **Priority:** Medium

### Fixed Issues
- ✅ None currently

---

## 📊 TEST RESULTS TEMPLATE

### Test Run: [Date]
**Tester:** [Name]  
**Environment:** [Desktop/Mobile/Browser]

| Test Case | Status | Notes |
|-----------|--------|-------|
| TC-001 | [ ] Pass [ ] Fail | |
| TC-002 | [ ] Pass [ ] Fail | |
| TC-003 | [ ] Pass [ ] Fail | |
| TC-004 | [ ] Pass [ ] Fail | |
| TC-005 | [ ] Pass [ ] Fail | |
| TC-006 | [ ] Pass [ ] Fail | |
| TC-007 | [ ] Pass [ ] Fail | |
| TC-008 | [ ] Pass [ ] Fail | |
| TC-009 | [ ] Pass [ ] Fail | |
| TC-010 | [ ] Pass [ ] Fail | |

**Overall:** [ ] Pass [ ] Fail  
**Issues Found:** [Count]  
**Notes:** [Any notes]

---

## ✅ ACCEPTANCE CRITERIA

### Must Have
- [ ] All Phase 1 features work
- [ ] All Phase 2 features work
- [ ] Mobile responsive
- [ ] No critical bugs
- [ ] Performance acceptable

### Should Have
- [ ] Components integrated into calculators
- [ ] All test cases pass
- [ ] Documentation complete
- [ ] User feedback positive

### Nice to Have
- [ ] Performance optimized
- [ ] All calculators integrated
- [ ] Advanced features

---

## 🔗 RELATED DOCUMENTATION

- [Integration Guide](SCORES_INTEGRATION_GUIDE.md)
- [Quick Start](SCORES_QUICK_START.md)
- [Complete Summary](SCORES_COMPLETE_SUMMARY.md)

---

**Maintainer:** Development Team  
**Last Updated:** 2025-02-18

