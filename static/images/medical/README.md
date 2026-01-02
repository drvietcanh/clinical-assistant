# Medical Images Directory

## 📁 Structure

This directory is for storing medical images used in the application.

### Recommended Structure:

```
medical/
├── anatomy/
│   ├── cardiovascular/
│   ├── respiratory/
│   ├── nervous/
│   └── ...
├── ecg/
│   ├── normal/
│   ├── abnormal/
│   └── examples/
├── flowcharts/
│   ├── protocols/
│   └── algorithms/
├── illustrations/
│   ├── procedures/
│   └── conditions/
└── infographics/
    ├── patient_education/
    └── clinical/
```

## 🖼️ Image Types

### Anatomy Diagrams
- Cardiovascular system
- Respiratory system
- Nervous system
- Other organ systems

### ECG Examples
- Normal ECG patterns
- Abnormal rhythms
- Case examples

### Flowcharts
- Protocol flowcharts
- Algorithm diagrams
- Decision trees

### Clinical Illustrations
- Procedures
- Conditions
- Pathophysiology

### Infographics
- Patient education materials
- Clinical summaries
- Drug mechanisms

## 📝 Usage

Images can be referenced in components using:

```python
from components.image_library import get_medical_image

image_path = get_medical_image("anatomy/cardiovascular/heart.png")
```

## ⚠️ Notes

- All images should be properly licensed
- Patient photos require consent
- Images should be optimized for web (compressed)
- Use appropriate formats (PNG for diagrams, JPG for photos)

---

*Directory created: 2025-01-30*

