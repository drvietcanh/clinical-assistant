# Hướng dẫn Module Lão khoa (Geriatrics)

## Tổng quan
Module Geriatrics cung cấp các clinical calculators đặc biệt cho bệnh nhân cao tuổi (≥65 tuổi), bao gồm:
- Đánh giá frailty
- Đánh giá nguy cơ té ngã
- Screening cognitive function
- An toàn thuốc (medication safety)

## Cấu trúc Module

```
scores/geriatrics/
├── __init__.py          # Main router
├── cfs.py               # Clinical Frailty Scale
├── morse_fall.py        # Morse Fall Scale
├── mmse.py              # Mini-Mental State Examination
├── moca.py              # Montreal Cognitive Assessment
├── beers.py             # Beers Criteria
└── stopp_start.py       # STOPP/START Criteria
```

## Cách sử dụng

### 1. Truy cập Module
- Vào trang **Scores**
- Chọn specialty: **👴 Lão khoa (Geriatrics)**
- Chọn calculator từ danh sách

### 2. Clinical Frailty Scale (CFS)

**Mục đích**: Đánh giá mức độ frailty (1-9)

**Khi dùng**:
- Tiên lượng bệnh nhân
- Quyết định điều trị
- Lập kế hoạch chăm sóc

**Interpretation**:
- 1-3: Fit to Managing Well
- 4-5: Vulnerable to Mildly Frail
- 6-7: Moderately to Severely Frail
- 8-9: Very Severely Frail to Terminally Ill

**Reference**: Rockwood K, et al. CMAJ. 2005

### 3. Morse Fall Scale

**Mục đích**: Đánh giá nguy cơ té ngã ở bệnh nhân nội trú

**Khi dùng**: Hàng ngày trong bệnh viện

**6 yếu tố đánh giá**:
1. History of falling
2. Secondary diagnosis
3. Ambulatory aid
4. IV/Heparin lock
5. Gait
6. Mental status

**Risk levels**:
- Low: 0-24 points
- Medium: 25-44 points
- High: ≥45 points

**Reference**: Morse JM, et al. Soc Sci Med. 1989

### 4. MMSE (Mini-Mental State Examination)

**Mục đích**: Screening cognitive impairment

**Khi dùng**:
- Screening ban đầu
- Theo dõi diễn biến

**Components** (11 items):
- Orientation (10 points)
- Registration (3 points)
- Attention & Calculation (5 points)
- Recall (3 points)
- Language (8 points)
- Construction (1 point)

**Score**: 0-30
- Normal: 24-30
- Mild impairment: 18-23
- Moderate: 10-17
- Severe: 0-9

**Reference**: Folstein MF, et al. J Psychiatr Res. 1975

### 5. MoCA (Montreal Cognitive Assessment)

**Mục đích**: Screening MCI và dementia (nhạy hơn MMSE)

**Khi dùng**:
- Screening MCI (mild cognitive impairment)
- Early dementia detection
- Bệnh nhân có trình độ học vấn thấp

**Components**:
- Visuospatial/Executive (5 points)
- Naming (3 points)
- Memory (not scored)
- Attention (6 points)
- Language (3 points)
- Abstraction (2 points)
- Delayed Recall (5 points)
- Orientation (6 points)

**Score**: 0-30 (with education adjustment)
- Normal: 26-30
- MCI: 18-25
- Dementia: 0-17

**Reference**: Nasreddine ZS, et al. J Am Geriatr Soc. 2005

### 6. Beers Criteria

**Mục đích**: Xác định potentially inappropriate medications (PIMs)

**Khi dùng**:
- Medication review
- Khi kê đơn mới cho elderly
- Kiểm tra an toàn thuốc

**Common PIMs**:
- Anticholinergics
- Benzodiazepines
- NSAIDs (non-COX-2 selective)
- Long-acting sulfonylureas
- Antipsychotics (in dementia)

**Reference**: AGS Beers Criteria 2023

### 7. STOPP/START Criteria

**Mục đích**: 
- **STOPP**: Medications to stop (potentially inappropriate)
- **START**: Medications to start (omitted but indicated)

**Khi dùng**:
- Comprehensive medication review
- Đảm bảo không thiếu thuốc cần thiết
- Đảm bảo không dùng thuốc không phù hợp

**Systems covered**:
- Cardiovascular
- CNS
- Gastrointestinal
- Pain & Inflammation
- Endocrine
- Respiratory
- Musculoskeletal

**Reference**: O'Mahony D, et al. Age Ageing. 2015

## Workflow Integration

### Medication Review Workflow
1. **Beers Criteria**: Kiểm tra PIMs
2. **STOPP/START**: Comprehensive review
3. **Deprescribing**: Xem xét ngưng thuốc không cần thiết

### Fall Risk Assessment Workflow
1. **Morse Fall Scale**: Đánh giá nguy cơ
2. **Interventions**: Theo risk level
3. **Monitoring**: Đánh giá lại thường xuyên

### Cognitive Assessment Workflow
1. **Screening**: MoCA hoặc MMSE
2. **Interpretation**: Phân loại severity
3. **Follow-up**: Neuropsychological testing nếu cần

### Frailty Assessment Workflow
1. **CFS**: Đánh giá frailty
2. **Goals of Care**: Thảo luận với bệnh nhân/người nhà
3. **Care Planning**: Điều chỉnh treatment goals

## Best Practices

### 1. Comprehensive Geriatric Assessment
- Combine multiple tools
- Consider all domains: physical, cognitive, functional, social
- Multidisciplinary approach

### 2. Medication Safety
- Regular medication reviews
- Use both Beers và STOPP/START
- Consider drug interactions
- Monitor adverse effects

### 3. Fall Prevention
- Screen all hospitalized elderly
- Implement interventions based on risk
- Reassess regularly

### 4. Cognitive Screening
- Screen if concerns raised
- Use MoCA for better MCI detection
- Consider education level
- Follow up with detailed assessment if needed

## Future Enhancements

### Phase 2 Calculators
- FRAIL Scale (quick frailty screening)
- Hendrich II Fall Risk Model
- Clock Drawing Test
- Anticholinergic Burden Scale

### Phase 3 Calculators
- GDS (Geriatric Depression Scale)
- SARC-F (Sarcopenia screening)
- eCART Score (Elderly)
- ISAR Score

## References
- Beers Criteria 2023: https://www.americangeriatrics.org
- MoCA Test: https://www.mocatest.org
- Clinical Frailty Scale: Dalhousie University
