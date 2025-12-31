# Phase 1 Implementation Guide - Tối Ưu App Y Học

## 📋 Tổng Quan Phase 1

Phase 1 tập trung vào 4 mục tiêu chính:
1. **Evidence-Based Content Enhancement** - Thêm evidence levels và references
2. **Enhanced Calculator Features** - Nâng cao chất lượng calculators
3. **Images & Visual Aids** - Thêm hình ảnh minh họa
4. **Offline Mode Enhancement** - Nâng cấp offline mode

---

## 🎯 1. Evidence-Based Content Enhancement

### Mục tiêu
Thêm evidence levels (A, B, C) và full citations vào tất cả protocols.

### Components đã tạo
- `components/phase1_protocol_enhancer.py` - Helper functions để thêm evidence vào protocols
- `components/protocol_version.py` - Version tracking (đã có)
- `components/evidence_badge.py` - Evidence badges (đã có)
- `components/references.py` - References display (đã có)
- `protocols/references_config.py` - References database (đã có)

### Cách sử dụng

#### Trong Protocol File:

```python
from components.phase1_protocol_enhancer import (
    render_protocol_header,
    render_recommendation_with_evidence,
    render_protocol_footer,
    add_evidence_to_recommendation
)

def render():
    """Your Protocol"""
    st.subheader("🦠 Protocol Name")
    
    # Header với version và evidence summary
    render_protocol_header(
        protocol_name="Protocol Name",
        guideline_source="AHA/ACC 2023",
        show_version=True,
        show_evidence_summary=True
    )
    
    st.markdown("---")
    
    # Recommendations với evidence levels
    st.markdown("### 💊 Treatment Recommendations")
    
    render_recommendation_with_evidence(
        "Kháng sinh phổ rộng trong vòng 1 giờ",
        evidence_level="A",
        citation_indices=[1, 2]
    )
    
    render_recommendation_with_evidence(
        "Truyền dịch 30 mL/kg",
        evidence_level="B",
        citation_indices=[3]
    )
    
    # Footer với references
    render_protocol_footer("Protocol Name")
```

### Checklist triển khai
- [ ] Import `phase1_protocol_enhancer` vào tất cả protocol files
- [ ] Thêm `render_protocol_header()` vào đầu mỗi protocol
- [ ] Thêm evidence levels (A/B/C) vào các recommendations
- [ ] Thêm `render_protocol_footer()` vào cuối mỗi protocol
- [ ] Cập nhật `protocols/references_config.py` với references đầy đủ
- [ ] Cập nhật `components/protocol_version.py` với version info cho tất cả protocols

---

## 🧮 2. Enhanced Calculator Features

### Mục tiêu
Thêm educational explanations, evidence citations, visual aids vào calculators.

### Components đã tạo
- `components/phase1_calculator_metadata.py` - Calculator metadata system
- `components/calculator_enhancements.py` - Enhancement components (đã có)

### Cách sử dụng

#### Trong Calculator File:

```python
from components.phase1_calculator_metadata import (
    render_calculator_education,
    render_calculator_result_with_interpretation
)
from components.calculator_enhancements import (
    render_visual_aid_chart,
    render_comparison_tool
)

def calculate_qsofa(...):
    """qSOFA Calculator"""
    
    # Educational content
    render_calculator_education("qsofa")
    
    st.markdown("---")
    
    # Calculator inputs
    # ... your calculator logic ...
    
    # Results với interpretation
    if result:
        render_calculator_result_with_interpretation(
            calculator_id="qsofa",
            result=f"qSOFA Score: {score}",
            result_value=score
        )
    
    # Visual aids (optional)
    if show_chart:
        render_visual_aid_chart(
            chart_type="bar",
            data={"x": [...], "y": [...]},
            title="qSOFA Score Distribution"
        )
```

### Calculator Metadata

Đã có metadata cho:
- ✅ qSOFA
- ✅ SOFA
- ✅ CHA₂DS₂-VASc
- ✅ CURB-65

**Cần thêm metadata cho:**
- [ ] ASCVD
- [ ] NEWS2
- [ ] GCS
- [ ] NIHSS
- [ ] MELD
- [ ] Child-Pugh
- [ ] Và các calculators quan trọng khác

### Checklist triển khai
- [ ] Thêm metadata vào `CALCULATOR_METADATA` trong `phase1_calculator_metadata.py`
- [ ] Import và sử dụng `render_calculator_education()` trong calculator files
- [ ] Thêm `render_calculator_result_with_interpretation()` cho results
- [ ] Thêm visual aids (charts, graphs) cho calculators phù hợp
- [ ] Thêm comparison tools cho calculators có thể so sánh nhiều patients

---

## 🖼️ 3. Images & Visual Aids

### Mục tiêu
Thêm hình ảnh minh họa vào protocols (flowcharts, diagrams, ECG examples).

### Components đã tạo
- `components/phase1_image_support.py` - Image support system

### Cách sử dụng

#### Trong Protocol File:

```python
from components.phase1_image_support import (
    render_flowchart_image,
    render_anatomy_diagram,
    render_ecg_example,
    render_infographic
)

def render():
    """Your Protocol"""
    
    # Flowchart
    render_flowchart_image(
        flowchart_path="protocols/sepsis_flowchart.png",
        title="Sepsis Management Flowchart",
        description="Sơ đồ quản lý sepsis theo Surviving Sepsis Campaign 2021"
    )
    
    # Anatomy diagram
    render_anatomy_diagram(
        diagram_path="anatomy/heart.png",
        labels=["Right atrium", "Left ventricle", "Aorta"],
        caption="Giải phẫu tim"
    )
    
    # ECG example
    render_ecg_example(
        ecg_path="ecg/stemi.png",
        diagnosis="STEMI - Anterior Wall",
        findings=["ST elevation V2-V4", "Q waves", "T wave inversion"]
    )
```

### Cấu trúc thư mục images

```
static/
  images/
    protocols/
      sepsis_flowchart.png
      stroke_pathway.png
      acls_algorithm.png
    anatomy/
      heart.png
      lung.png
      kidney.png
    ecg/
      normal.png
      atrial_fibrillation.png
      stemi.png
    infographics/
      patient_education_*.png
```

### Checklist triển khai
- [ ] Tạo thư mục `static/images/` với các subdirectories
- [ ] Thêm hình ảnh flowcharts cho protocols quan trọng
- [ ] Thêm anatomy diagrams cho protocols liên quan
- [ ] Thêm ECG examples cho cardiac protocols
- [ ] Thêm infographics cho patient education
- [ ] Cập nhật `IMAGE_REGISTRY` trong `phase1_image_support.py`
- [ ] Import và sử dụng image components trong protocols

---

## 📱 4. Offline Mode Enhancement

### Mục tiêu
Cache calculators, protocols, và drug database để hoạt động offline hoàn chỉnh.

### Files cần cập nhật
- `static/service-worker.js` - Service worker để cache
- `static/offline.js` - Offline support script (đã có)
- `static/manifest.json` - PWA manifest (đã có)

### Cách nâng cấp Service Worker

Cần thêm vào `service-worker.js`:

```javascript
// Cache calculator definitions
const CALCULATOR_CACHE = 'calculator-cache-v1';
const PROTOCOL_CACHE = 'protocol-cache-v1';

// Cache calculators khi install
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CALCULATOR_CACHE).then((cache) => {
      return cache.addAll([
        '/config/calculators.py',
        '/components/calculator_enhancements.py',
        '/components/phase1_calculator_metadata.py'
      ]);
    })
  );
  
  event.waitUntil(
    caches.open(PROTOCOL_CACHE).then((cache) => {
      return cache.addAll([
        '/config/protocol_lists.py',
        '/config/protocol_routing.py',
        '/protocols/references_config.py'
      ]);
    })
  );
});

// Serve từ cache khi offline
self.addEventListener('fetch', (event) => {
  // Calculator requests
  if (event.request.url.includes('/Scores')) {
    event.respondWith(
      caches.match(event.request).then((response) => {
        return response || fetch(event.request);
      })
    );
  }
  
  // Protocol requests
  if (event.request.url.includes('/Protocols')) {
    event.respondWith(
      caches.match(event.request).then((response) => {
        return response || fetch(event.request);
      })
    );
  }
});
```

### Checklist triển nhật
- [ ] Cập nhật `service-worker.js` để cache calculators
- [ ] Cập nhật `service-worker.js` để cache protocols
- [ ] Cập nhật `service-worker.js` để cache drug database (đã có)
- [ ] Test offline mode với calculators
- [ ] Test offline mode với protocols
- [ ] Test sync khi online lại
- [ ] Thêm offline indicator improvements

---

## 📊 Tiến Độ Triển Khai

### ✅ Đã hoàn thành
- [x] Tạo `phase1_protocol_enhancer.py` component
- [x] Tạo `phase1_calculator_metadata.py` component
- [x] Tạo `phase1_image_support.py` component
- [x] Tạo implementation guide

### 🔄 Đang triển khai
- [ ] Tích hợp evidence levels vào protocols
- [ ] Thêm calculator metadata cho các calculators quan trọng
- [ ] Thêm hình ảnh vào protocols
- [ ] Nâng cấp offline mode

### 📝 Cần làm tiếp
- [ ] Test tất cả components
- [ ] Update documentation
- [ ] Create example implementations
- [ ] Performance optimization

---

## 🚀 Bước Tiếp Theo

1. **Bắt đầu với Evidence Enhancement:**
   - Chọn 5-10 protocols quan trọng nhất
   - Thêm evidence levels và references
   - Test và refine

2. **Calculator Enhancements:**
   - Thêm metadata cho top 20 calculators
   - Test educational content
   - Add visual aids

3. **Images:**
   - Tạo/collect hình ảnh cho protocols
   - Implement image components
   - Test display

4. **Offline Mode:**
   - Update service worker
   - Test caching
   - Test sync

---

## 📚 Tài Liệu Tham Khảo

- `DANH_SACH_DE_XUAT_TOI_UU_APP.md` - Original optimization list
- `components/phase1_protocol_enhancer.py` - Protocol enhancement helpers
- `components/phase1_calculator_metadata.py` - Calculator metadata
- `components/phase1_image_support.py` - Image support system
- `components/evidence_badge.py` - Evidence badge component
- `components/references.py` - References component

---

*Document created: 2025-02-18*
*Phase 1 Implementation Guide v1.0*

