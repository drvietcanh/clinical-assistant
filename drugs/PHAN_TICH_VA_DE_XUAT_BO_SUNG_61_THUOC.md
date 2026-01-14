# 📋 Phân tích Yêu Cầu & Đề Xuất Bổ sung 61 Thuốc

**Ngày:** 2025-02-05  
**Kiến trúc sư:** Phân tích từ góc độ 30 năm kinh nghiệm  
**Mục tiêu:** Từ 239 thuốc → 300+ thuốc (cần thêm 61+ thuốc)

---

## 1. 📊 PHÂN TÍCH HIỆN TRẠNG

### 1.1. Số Lượng Thuốc Hiện Tại

| Nhóm Thuốc | Số Lượng | Tỷ lệ | Ghi Chú |
|------------|----------|-------|---------|
| Cardiovascular | 30 | 12.6% | Đã khá đầy đủ |
| Diabetes | 9 | 3.8% | Cần bổ sung |
| Gastrointestinal | 10 | 4.2% | Cần bổ sung |
| Oncology | 10 | 4.2% | Cần bổ sung |
| Emergency | 7 | 2.9% | **Cần bổ sung gấp** |
| Antibiotics | 9 | 3.8% | **Cần bổ sung gấp** |
| Pediatric | 6 | 2.5% | Cần bổ sung |
| Analgesics | 8 | 3.3% | Cần bổ sung |
| Respiratory | 7 | 2.9% | Cần bổ sung |
| Neurology/Psychiatry | 13 | 5.4% | Cần bổ sung |
| Allergy | 5 | 2.1% | Cần bổ sung |
| Vitamins/Supplements | 5 | 2.1% | Đủ |
| Anti-infectives | 7 | 2.9% | Cần bổ sung |
| Endocrinology | 4 | 1.7% | **Cần bổ sung gấp** |
| Other | 2 | 0.8% | Cần bổ sung |
| **TỔNG** | **239** | **100%** | **Cần thêm 61+** |

### 1.2. Phân tích Gaps (Khoảng Trống)

#### 🔴 **Nhóm Thiếu Nhiều Nhất (Ưu tiên cao):**
1. **Emergency (7 → 15):** Thiếu 8 thuốc cấp cứu quan trọng
2. **Antibiotics (9 → 30):** Thiếu 21 thuốc kháng sinh phổ biến
3. **Endocrinology (4 → 15):** Thiếu 11 thuốc nội tiết
4. **Hematology (1 → 10):** Thiếu 9 thuốc huyết học (chưa có trong DRUG_GROUPS nhưng có module)

#### 🟡 **Nhóm Thiếu Trung Bình (Ưu tiên trung bình):**
5. **Neurology/Psychiatry (13 → 20):** Thiếu 7 thuốc
6. **Gastrointestinal (10 → 20):** Thiếu 10 thuốc
7. **Oncology (10 → 20):** Thiếu 10 thuốc
8. **Respiratory (7 → 15):** Thiếu 8 thuốc
9. **Analgesics (8 → 15):** Thiếu 7 thuốc
10. **Diabetes (9 → 15):** Thiếu 6 thuốc

#### 🟢 **Nhóm Thiếu Ít (Ưu tiên thấp):**
11. **Allergy (5 → 10):** Thiếu 5 thuốc
12. **Pediatric (6 → 10):** Thiếu 4 thuốc
13. **Other (2 → 10):** Thiếu 8 thuốc

---

## 2. 🏗️ CẤU TRÚC THUỐC HIỆN TẠI

### 2.1. Cấu Trúc Dictionary Cơ Bản

```python
"Tên Thuốc": {
    # === CÁC TRƯỜNG CƠ BẢN ===
    'group': 'Nhóm thuốc chính',
    'vietnamese_name': 'Tên tiếng Việt, tên chung, biệt dược',
    'administration': ['PO', 'IV', 'IM', 'SC', 'Inhaled', 'Topical'],
    
    # === CHỈ ĐỊNH & CHỐNG CHỈ ĐỊNH ===
    'indications': [
        'Chỉ định 1',
        'Chỉ định 2',
        'Chỉ định 3'
    ],
    'contraindications': [
        'Chống chỉ định 1',
        'Chống chỉ định 2'
    ],
    
    # === LIỀU DÙNG ===
    'dosage': {
        'adult_po': 'Liều uống người lớn',
        'adult_iv': 'Liều tiêm tĩnh mạch người lớn',
        'adult_im': 'Liều tiêm bắp người lớn',
        'pediatric_po': 'Liều uống trẻ em',
        'pediatric_iv': 'Liều tiêm tĩnh mạch trẻ em',
        'notes': 'Ghi chú đặc biệt về liều dùng'
    },
    
    # === ĐIỀU CHỈNH THEO CHỨC NĂNG THẬN ===
    'renal_adjustment': {
        'normal': 'Liều bình thường',
        '30_60': 'Điều chỉnh CrCl 30-60',
        'under_30': 'Điều chỉnh CrCl <30',
        'dialysis': 'Điều chỉnh khi lọc máu'
    },
    
    # === TÁC DỤNG PHỤ ===
    'side_effects': [
        'Tác dụng phụ 1',
        'Tác dụng phụ 2',
        'Tác dụng phụ nghiêm trọng'
    ],
    
    # === TƯƠNG TÁC THUỐC ===
    'interactions': [
        'Tương tác 1',
        'Tương tác 2'
    ],
    
    # === THAI KỲ ===
    'pregnancy': 'FDA Category (A/B/C/D/X)',
    
    # === ENHANCED FIELDS (6 FIELDS CƠ BẢN) ===
    'mechanism_of_action': {
        'primary': 'Cơ chế tác dụng chính (1-2 câu)',
        'detailed': 'Cơ chế tác dụng chi tiết (3-5 câu)',
        'target': 'Đích tác dụng (receptor, enzyme, channel)'
    },
    
    'monitoring': {
        'labs': [
            'Xét nghiệm cần theo dõi 1',
            'Xét nghiệm cần theo dõi 2'
        ],
        'vital_signs': [
            'Dấu hiệu sinh tồn cần theo dõi'
        ],
        'clinical': [
            'Dấu hiệu lâm sàng cần theo dõi'
        ],
        'frequency': 'Tần suất theo dõi'
    },
    
    'precautions': [
        'Lưu ý quan trọng 1',
        'Lưu ý quan trọng 2',
        'Cảnh báo đặc biệt'
    ],
    
    'pharmacokinetics': {
        'half_life': 'Thời gian bán hủy',
        'onset': 'Thời gian bắt đầu tác dụng',
        'duration': 'Thời gian tác dụng',
        'protein_binding': 'Tỷ lệ gắn protein',
        'clearance': 'Thanh thải (gan/thận)',
        'bioavailability': 'Sinh khả dụng',
        'metabolism': 'Chuyển hóa (enzyme)',
        'excretion': 'Bài tiết'
    },
    
    'storage': 'Hướng dẫn bảo quản chi tiết',
    
    'black_box_warnings': [
        'Cảnh báo đen 1',
        'Cảnh báo đen 2'
    ],
    
    # === ENHANCED FIELDS (8 FIELDS TÙY CHỌN) ===
    'drug_interactions': {
        'major': [
            {
                'drug': 'Tên thuốc tương tác',
                'mechanism': 'Cơ chế tương tác',
                'effect': 'Hậu quả',
                'management': 'Cách xử lý'
            }
        ],
        'moderate': [...],
        'minor': [...]
    },
    
    'contraindications': {
        'tuyệt_đối': [
            'Chống chỉ định tuyệt đối 1',
            'Chống chỉ định tuyệt đối 2'
        ],
        'tương_đối': [
            'Chống chỉ định tương đối 1',
            'Chống chỉ định tương đối 2'
        ]
    },
    
    'pregnancy_lactation': {
        'fda_category': 'A/B/C/D/X',
        'pregnancy_details': 'Chi tiết về thai kỳ',
        'lactation': {
            'safety': 'Compatible/Incompatible',
            'details': 'Chi tiết',
            'recommendation': 'Khuyến cáo'
        }
    },
    
    'hepatic_adjustment': {
        'mild': 'Điều chỉnh suy gan nhẹ',
        'moderate': 'Điều chỉnh suy gan trung bình',
        'severe': 'Điều chỉnh suy gan nặng',
        'notes': 'Ghi chú'
    },
    
    'overdose_management': {
        'symptoms': [
            'Triệu chứng quá liều 1',
            'Triệu chứng quá liều 2'
        ],
        'antidote': 'Thuốc giải độc',
        'treatment': [
            'Bước điều trị 1',
            'Bước điều trị 2'
        ],
        'monitoring': 'Theo dõi sau quá liều'
    },
    
    'reversal_agents': [
        {
            'name': 'Tên thuốc giải độc',
            'indication': 'Chỉ định',
            'dose': 'Liều dùng',
            'mechanism': 'Cơ chế',
            'notes': 'Ghi chú'
        }
    ],
    
    'administration_instructions': {
        'oral': {
            'with_food': 'Uống với thức ăn hay không',
            'timing': 'Thời điểm uống'
        },
        'iv': {
            'reconstitution': 'Cách pha',
            'infusion_rate': 'Tốc độ truyền',
            'compatibility': ['D5W', 'NS', 'LR'],
            'incompatibility': ['Không pha với...'],
            'notes': 'Ghi chú'
        }
    },
    
    'pediatric_dosing': {
        'neonates': 'Liều trẻ sơ sinh',
        'infants': 'Liều trẻ nhũ nhi',
        'children': 'Liều trẻ em',
        'adolescents': 'Liều thanh thiếu niên',
        'notes': 'Ghi chú'
    },
    
    'references': [
        'Nguồn tham khảo 1',
        'Nguồn tham khảo 2'
    ]
}
```

### 2.2. Cấu Trúc Module

Mỗi nhóm thuốc được tổ chức trong module riêng:

```
drugs/drug_modules/
├── [nhóm_chính]/
│   ├── __init__.py          # Import và merge tất cả sub-modules
│   ├── [sub_category_1].py  # Sub-category 1
│   ├── [sub_category_2].py  # Sub-category 2
│   └── ...
```

**Ví dụ:**
```
drugs/drug_modules/cardiovascular/
├── __init__.py
├── ace_inhibitors.py
├── arbs.py
├── beta_blockers/
│   ├── __init__.py
│   ├── non_selective.py
│   └── selective.py
├── statins.py
└── ...
```

### 2.3. Quy Tắc Đặt Tên

1. **Tên thuốc:** Tên chung (generic name) bằng tiếng Anh, viết hoa chữ cái đầu
2. **Key trong dictionary:** Tên chung chính xác
3. **Module file:** Tên file theo snake_case, mô tả nhóm thuốc
4. **Constant:** Tên constant UPPER_SNAKE_CASE, kết thúc bằng `_DRUGS`

---

## 3. 📝 ĐỀ XUẤT 61 THUỐC CẦN BỔ SUNG

### 3.1. Nhóm Emergency (8 thuốc) - 🔥🔥🔥 ƯU TIÊN CAO NHẤT

| STT | Tên Thuốc | Nhóm Phụ | Lý Do | File Module |
|-----|-----------|----------|-------|-------------|
| 1 | **Epinephrine** | Catecholamine | Cấp cứu sốc phản vệ, ngừng tim | `emergency/catecholamine_alpha__beta_agonists.py` |
| 2 | **Norepinephrine** | Catecholamine | Cấp cứu sốc, tăng huyết áp | `emergency/catecholamine_alpha__beta_agonists.py` |
| 3 | **Dopamine** | Catecholamine | Cấp cứu sốc, tăng co bóp tim | `emergency/catecholamine_alpha__beta_agonists.py` |
| 4 | **Dobutamine** | Catecholamine | Cấp cứu suy tim, tăng co bóp | `emergency/catecholamine_alpha__beta_agonists.py` |
| 5 | **Lidocaine** | Antiarrhythmic | Cấp cứu rối loạn nhịp thất | `emergency/local_anesthetic__antiarrhythmic_class_ibs.py` |
| 6 | **Atropine** | Anticholinergic | Cấp cứu nhịp chậm, ngộ độc | `emergency/anticholinergics.py` |
| 7 | **Naloxone** | Opioid antagonist | Cấp cứu quá liều opioid | `emergency/opioid_antagonists.py` |
| 8 | **Flumazenil** | Benzodiazepine antagonist | Cấp cứu quá liều benzodiazepine | `emergency/benzodiazepine_antagonists.py` |

### 3.2. Nhóm Antibiotics (21 thuốc) - 🔥🔥🔥 ƯU TIÊN CAO NHẤT

| STT | Tên Thuốc | Nhóm Phụ | Lý Do | File Module |
|-----|-----------|----------|-------|-------------|
| 9 | **Azithromycin** | Macrolide | Kháng sinh phổ biến, viêm phổi | `infectious_other/macrolides.py` |
| 10 | **Clarithromycin** | Macrolide | Kháng sinh phổ biến, H. pylori | `infectious_other/macrolides.py` |
| 11 | **Amoxicillin-clavulanate** | Beta-lactam/BLI | Kháng sinh phổ biến nhất | `infectious_other/beta_lactams.py` |
| 12 | **Ampicillin-sulbactam** | Beta-lactam/BLI | Kháng sinh phổ biến | `infectious_other/beta_lactams.py` |
| 13 | **Cefazolin** | Cephalosporin 1st gen | Phẫu thuật, nhiễm trùng da | `infectious_other/cephalosporins.py` |
| 14 | **Cefuroxime** | Cephalosporin 2nd gen | Nhiễm trùng hô hấp | `infectious_other/cephalosporins.py` |
| 15 | **Ceftazidime** | Cephalosporin 3rd gen | Nhiễm trùng Pseudomonas | `infectious_other/cephalosporins.py` |
| 16 | **Cefepime** | Cephalosporin 4th gen | Nhiễm trùng nặng | `infectious_other/cephalosporins.py` |
| 17 | **Vancomycin** | Glycopeptide | MRSA, nhiễm trùng nặng | `antimicrobial/antibiotics.py` |
| 18 | **Linezolid** | Oxazolidinone | MRSA, VRE | `antimicrobial/antibiotics.py` |
| 19 | **Clindamycin** | Lincosamide | Nhiễm trùng kỵ khí, da | `antimicrobial/antibiotics.py` |
| 20 | **Metronidazole** | Nitroimidazole | Nhiễm trùng kỵ khí, ký sinh trùng | `infectious_other/nitroimidazoles.py` |
| 21 | **Doxycycline** | Tetracycline | Nhiễm trùng đặc biệt, sốt rét | `infectious_other/tetracyclines.py` |
| 22 | **Minocycline** | Tetracycline | Mụn trứng cá, nhiễm trùng | `infectious_other/tetracyclines.py` |
| 23 | **Gentamicin** | Aminoglycoside | Nhiễm trùng Gram âm nặng | `antimicrobial/antibiotics.py` |
| 24 | **Amikacin** | Aminoglycoside | Nhiễm trùng kháng thuốc | `antimicrobial/antibiotics.py` |
| 25 | **Tobramycin** | Aminoglycoside | Nhiễm trùng Pseudomonas | `antimicrobial/antibiotics.py` |
| 26 | **Meropenem** | Carbapenem | Nhiễm trùng nặng, đa kháng | `antimicrobial/antibiotics.py` |
| 27 | **Imipenem-cilastatin** | Carbapenem | Nhiễm trùng nặng | `antimicrobial/antibiotics.py` |
| 28 | **Ertapenem** | Carbapenem | Nhiễm trùng nặng (không Pseudomonas) | `antimicrobial/antibiotics.py` |
| 29 | **Trimethoprim-sulfamethoxazole** | Sulfonamide | Nhiễm trùng đặc biệt | `antimicrobial/antibiotics.py` |

### 3.3. Nhóm Endocrinology (11 thuốc) - 🔥🔥 ƯU TIÊN CAO

| STT | Tên Thuốc | Nhóm Phụ | Lý Do | File Module |
|-----|-----------|----------|-------|-------------|
| 30 | **Levothyroxine** | Thyroid hormone | Suy giáp, rất phổ biến | `metabolic/thyroid_hormones.py` |
| 31 | **Methimazole** | Antithyroid | Cường giáp | `metabolic/antithyroid.py` |
| 32 | **Propylthiouracil** | Antithyroid | Cường giáp (thai kỳ) | `metabolic/antithyroid.py` |
| 33 | **Prednisone** | Corticosteroid | Viêm, dị ứng, rất phổ biến | `endocrinology_other/corticosteroids/short_intermediate_acting.py` |
| 34 | **Prednisolone** | Corticosteroid | Viêm, dị ứng | `endocrinology_other/corticosteroids/short_intermediate_acting.py` |
| 35 | **Methylprednisolone** | Corticosteroid | Viêm nặng, cấp cứu | `endocrinology_other/corticosteroids/short_intermediate_acting.py` |
| 36 | **Hydrocortisone** | Corticosteroid | Suy thượng thận, cấp cứu | `endocrinology_other/corticosteroids/short_intermediate_acting.py` |
| 37 | **Dexamethasone** | Corticosteroid | Viêm, phù não | `endocrinology_other/corticosteroids/long_acting.py` |
| 38 | **Budesonide** | Corticosteroid | Viêm ruột, hô hấp | `endocrinology_other/corticosteroids/short_intermediate_acting.py` |
| 39 | **Fludrocortisone** | Mineralocorticoid | Suy thượng thận | `endocrinology_other/corticosteroids/short_intermediate_acting.py` |
| 40 | **Testosterone** | Androgen | Suy sinh dục nam | `metabolic/corticosteroids.py` (hoặc tạo mới) |

### 3.4. Nhóm Neurology/Psychiatry (7 thuốc) - 🔥🔥 ƯU TIÊN CAO

| STT | Tên Thuốc | Nhóm Phụ | Lý Do | File Module |
|-----|-----------|----------|-------|-------------|
| 41 | **Phenytoin** | Anticonvulsant | Động kinh, rất phổ biến | `neurological/anticonvulsants.py` |
| 42 | **Levetiracetam** | Anticonvulsant | Động kinh, an toàn | `neurological/anticonvulsants.py` |
| 43 | **Topiramate** | Anticonvulsant | Động kinh, đau nửa đầu | `neurological/anticonvulsants.py` |
| 44 | **Donepezil** | Cholinesterase inhibitor | Alzheimer | `neurological/alzheimer_dementia_drugs.py` |
| 45 | **Rivastigmine** | Cholinesterase inhibitor | Alzheimer | `neurological/alzheimer_dementia_drugs.py` |
| 46 | **Memantine** | NMDA antagonist | Alzheimer | `neurological/alzheimer_dementia_drugs.py` |
| 47 | **Sumatriptan** | Antimigraine | Đau nửa đầu | `analgesics/antimigraine_5_ht1_receptor_agonists.py` |

### 3.5. Nhóm Gastrointestinal (10 thuốc) - 🔥 ƯU TIÊN TRUNG BÌNH

| STT | Tên Thuốc | Nhóm Phụ | Lý Do | File Module |
|-----|-----------|----------|-------|-------------|
| 48 | **Lansoprazole** | PPI | Loét dạ dày, rất phổ biến | `gastrointestinal/proton_pump_inhibitor_ppis.py` |
| 49 | **Esomeprazole** | PPI | Loét dạ dày | `gastrointestinal/proton_pump_inhibitor_ppis.py` |
| 50 | **Rabeprazole** | PPI | Loét dạ dày | `gastrointestinal/proton_pump_inhibitor_ppis.py` |
| 51 | **Ranitidine** | H2 blocker | Loét dạ dày | `gastrointestinal/h2_receptor_antagonists.py` |
| 52 | **Famotidine** | H2 blocker | Loét dạ dày | `gastrointestinal/h2_receptor_antagonists.py` |
| 53 | **Domperidone** | Prokinetic | Buồn nôn, nôn | `gastrointestinal/prokinetic_antiemetics.py` |
| 54 | **Metoclopramide** | Prokinetic | Buồn nôn, nôn | `gastrointestinal/prokinetic_antiemetics.py` |
| 55 | **Loperamide** | Antidiarrheal | Tiêu chảy | `gastrointestinal/antidiarrheals.py` |
| 56 | **Bismuth subsalicylate** | Antidiarrheal | Tiêu chảy, H. pylori | `gastrointestinal/antidiarrheals.py` |
| 57 | **Sucralfate** | Mucosal protectant | Loét dạ dày | `gastrointestinal/mucosal_protectants.py` |

### 3.6. Nhóm Respiratory (8 thuốc) - 🔥 ƯU TIÊN TRUNG BÌNH

| STT | Tên Thuốc | Nhóm Phụ | Lý Do | File Module |
|-----|-----------|----------|-------|-------------|
| 58 | **Salmeterol** | LABA | Hen suyễn, COPD | `respiratory/long_acting_beta_2_agonist_labas.py` |
| 59 | **Formoterol** | LABA | Hen suyễn, COPD | `respiratory/long_acting_beta_2_agonist_labas.py` |
| 60 | **Ipratropium** | SAMA | COPD, hen suyễn | `respiratory/anticholinergic_short_actings.py` |
| 61 | **Tiotropium** | LAMA | COPD | `respiratory/anticholinergic_long_actings.py` |
| 62 | **Montelukast** | Leukotriene antagonist | Hen suyễn, dị ứng | `respiratory/leukotriene_receptor_antagonists.py` |
| 63 | **Budesonide inhaled** | ICS | Hen suyễn, COPD | `respiratory/inhaled_corticosteroid_icss.py` |
| 64 | **Fluticasone inhaled** | ICS | Hen suyễn, COPD | `respiratory/inhaled_corticosteroid_icss.py` |
| 65 | **Beclomethasone inhaled** | ICS | Hen suyễn | `respiratory/inhaled_corticosteroid_icss.py` |

### 3.7. Nhóm Oncology (10 thuốc) - 🔥 ƯU TIÊN TRUNG BÌNH

| STT | Tên Thuốc | Nhóm Phụ | Lý Do | File Module |
|-----|-----------|----------|-------|-------------|
| 66 | **Oxaliplatin** | Platinum | Ung thư đại trực tràng | `oncology/platinum_compounds.py` |
| 67 | **5-Fluorouracil** | Antimetabolite | Ung thư đại trực tràng | `oncology/antimetabolites.py` |
| 68 | **Ifosfamide** | Alkylating | Ung thư, sarcoma | `oncology/alkylating_agents.py` |
| 69 | **Doxorubicin** | Anthracycline | Ung thư vú, lymphoma | `oncology/anthracyclines.py` |
| 70 | **Paclitaxel** | Taxane | Ung thư vú, phổi | `oncology/taxanes.py` |
| 71 | **Docetaxel** | Taxane | Ung thư vú, phổi | `oncology/taxanes.py` |
| 72 | **Gemcitabine** | Antimetabolite | Ung thư tụy, phổi | `oncology/antimetabolites.py` |
| 73 | **Irinotecan** | Topoisomerase inhibitor | Ung thư đại trực tràng | `oncology/topoisomerase_inhibitors.py` |
| 74 | **Granisetron** | 5-HT3 antagonist | Chống nôn (hóa trị) | `oncology/anti_emetic_5_ht3_antagonists.py` |
| 75 | **Palonosetron** | 5-HT3 antagonist | Chống nôn (hóa trị) | `oncology/anti_emetic_5_ht3_antagonists.py` |

### 3.8. Nhóm Analgesics (7 thuốc) - 🔥 ƯU TIÊN TRUNG BÌNH

| STT | Tên Thuốc | Nhóm Phụ | Lý Do | File Module |
|-----|-----------|----------|-------|-------------|
| 76 | **Naproxen** | NSAID | Đau, viêm | `analgesics/nsaids.py` |
| 77 | **Diclofenac** | NSAID | Đau, viêm | `analgesics/nsaids.py` |
| 78 | **Ketorolac** | NSAID | Đau nặng (IV) | `analgesics/nsaids.py` |
| 79 | **Morphine** | Opioid strong | Đau nặng | `analgesics/opioid_agonist_strongs.py` |
| 80 | **Fentanyl** | Opioid strong | Đau nặng (IV/patch) | `analgesics/opioid_agonist_strongs.py` |
| 81 | **Codeine** | Opioid weak | Đau nhẹ đến trung bình | `analgesics/opioid_agonist_weaks.py` |
| 82 | **Tramadol** | Opioid weak | Đau nhẹ đến trung bình | `analgesics/opioid_agonist_weaks.py` |

### 3.9. Nhóm Diabetes (6 thuốc) - ⚡ ƯU TIÊN THẤP

| STT | Tên Thuốc | Nhóm Phụ | Lý Do | File Module |
|-----|-----------|----------|-------|-------------|
| 83 | **Empagliflozin** | SGLT2 inhibitor | Đái tháo đường, suy tim | `diabetes/sglt2_inhibitors.py` |
| 84 | **Dapagliflozin** | SGLT2 inhibitor | Đái tháo đường, suy tim | `diabetes/sglt2_inhibitors.py` |
| 85 | **Sitagliptin** | DPP-4 inhibitor | Đái tháo đường | `diabetes/dpp_4_inhibitors.py` |
| 86 | **Vildagliptin** | DPP-4 inhibitor | Đái tháo đường | `diabetes/dpp_4_inhibitors.py` |
| 87 | **Pioglitazone** | TZD | Đái tháo đường | `diabetes/thiazolidinedione_tzds.py` |
| 88 | **Acarbose** | Alpha-glucosidase inhibitor | Đái tháo đường | `diabetes/alpha_glucosidase_inhibitors.py` |

### 3.10. Nhóm Allergy (5 thuốc) - ⚡ ƯU TIÊN THẤP

| STT | Tên Thuốc | Nhóm Phụ | Lý Do | File Module |
|-----|-----------|----------|-------|-------------|
| 89 | **Loratadine** | Antihistamine 2nd gen | Dị ứng | `supportive/antihistamine_h1_antagonist_2nd_generations.py` |
| 90 | **Cetirizine** | Antihistamine 2nd gen | Dị ứng | `supportive/antihistamine_h1_antagonist_2nd_generations.py` |
| 91 | **Fexofenadine** | Antihistamine 2nd gen | Dị ứng | `supportive/antihistamine_h1_antagonist_2nd_generations.py` |
| 92 | **Desloratadine** | Antihistamine 2nd gen | Dị ứng | `supportive/antihistamine_h1_antagonist_2nd_generations.py` |
| 93 | **Levocetirizine** | Antihistamine 2nd gen | Dị ứng | `supportive/antihistamine_h1_antagonist_2nd_generations.py` |

### 3.11. Nhóm Hematology (9 thuốc) - ⚡ ƯU TIÊN THẤP

| STT | Tên Thuốc | Nhóm Phụ | Lý Do | File Module |
|-----|-----------|----------|-------|-------------|
| 94 | **Warfarin** | Anticoagulant | Chống đông, rất phổ biến | `cardiovascular/anticoagulants.py` |
| 95 | **Aspirin** | Antiplatelet | Chống đông, rất phổ biến | `cardiovascular_other/antiplatelets.py` |
| 96 | **Clopidogrel** | Antiplatelet | Chống đông | `cardiovascular_other/antiplatelets.py` |
| 97 | **Ticagrelor** | Antiplatelet | Chống đông | `cardiovascular_other/antiplatelets.py` |
| 98 | **Prasugrel** | Antiplatelet | Chống đông | `cardiovascular_other/antiplatelets.py` |
| 99 | **Enoxaparin** | LMWH | Chống đông | `cardiovascular/anticoagulants.py` |
| 100 | **Heparin** | Anticoagulant | Chống đông | `cardiovascular/anticoagulants.py` |
| 101 | **Fondaparinux** | Factor Xa inhibitor | Chống đông | `cardiovascular/anticoagulants.py` |
| 102 | **Rivaroxaban** | DOAC | Chống đông | `cardiovascular/anticoagulants.py` |

### 3.12. Nhóm Other/Miscellaneous (8 thuốc) - ⚡ ƯU TIÊN THẤP

| STT | Tên Thuốc | Nhóm Phụ | Lý Do | File Module |
|-----|-----------|----------|-------|-------------|
| 103 | **Allopurinol** | Xanthine oxidase inhibitor | Gout | `miscellaneous/xanthine_oxidase_inhibitors.py` |
| 104 | **Colchicine** | Antigout | Gout | `miscellaneous/gout_medications.py` |
| 105 | **Probenecid** | Uricosuric | Gout | `miscellaneous/gout_medications.py` |
| 106 | **Methotrexate** | Antimetabolite | Viêm khớp, ung thư | `oncology/antimetabolite_antifolates.py` |
| 107 | **Cyclosporine** | Immunosuppressant | Ghép tạng, tự miễn | `other.py` (hoặc tạo mới) |
| 108 | **Tacrolimus** | Immunosuppressant | Ghép tạng, tự miễn | `other.py` (hoặc tạo mới) |
| 109 | **Mycophenolate** | Immunosuppressant | Ghép tạng, tự miễn | `other.py` (hoặc tạo mới) |
| 110 | **Azathioprine** | Immunosuppressant | Ghép tạng, tự miễn | `other.py` (hoặc tạo mới) |

**TỔNG CỘNG: 102 thuốc được đề xuất** (vượt mục tiêu 61 thuốc để có buffer)

---

## 4. 🎯 THỨ TỰ TRIỂN KHAI ĐỀ XUẤT

### 4.1. Nguyên tắc Ưu tiên

1. **Ưu tiên theo mức độ quan trọng lâm sàng:**
   - 🔥🔥🔥 Cấp cứu, thường dùng, nguy cơ cao
   - 🔥🔥 Thường dùng, có nguy cơ
   - 🔥 Thường dùng
   - ⚡ Ít dùng hơn

2. **Ưu tiên theo nhóm:**
   - Emergency → Antibiotics → Endocrinology → Neurology/Psychiatry
   - Sau đó: Gastrointestinal → Respiratory → Oncology → Analgesics
   - Cuối cùng: Diabetes → Allergy → Hematology → Other

3. **Ưu tiên theo module:**
   - Bổ sung vào module đã có trước
   - Tạo module mới sau (nếu cần)

### 4.2. Kế Hoạch Triển Khai Chi tiết

#### **GIAI ĐOẠN 1: Emergency & Antibiotics (29 thuốc) - 🔥🔥🔥**

**Thời gian ước tính:** 2-3 tuần  
**Mục tiêu:** Hoàn thành các thuốc cấp cứu và kháng sinh cơ bản

**Bước 1.1: Emergency (8 thuốc)**
- Ưu tiên: Epinephrine, Norepinephrine, Dopamine, Dobutamine
- Tiếp theo: Lidocaine, Atropine, Naloxone, Flumazenil
- **File:** `drugs/drug_modules/emergency/`
- **Thời gian:** 1 tuần

**Bước 1.2: Antibiotics - Beta-lactams & Macrolides (8 thuốc)**
- Amoxicillin-clavulanate, Ampicillin-sulbactam
- Cefazolin, Cefuroxime, Ceftazidime, Cefepime
- Azithromycin, Clarithromycin
- **File:** `drugs/drug_modules/infectious_other/`, `antimicrobial/`
- **Thời gian:** 1 tuần

**Bước 1.3: Antibiotics - Các nhóm khác (13 thuốc)**
- Vancomycin, Linezolid, Clindamycin
- Metronidazole, Doxycycline, Minocycline
- Gentamicin, Amikacin, Tobramycin
- Meropenem, Imipenem-cilastatin, Ertapenem
- Trimethoprim-sulfamethoxazole
- **File:** `drugs/drug_modules/antimicrobial/`, `infectious_other/`
- **Thời gian:** 1 tuần

#### **GIAI ĐOẠN 2: Endocrinology & Neurology (18 thuốc) - 🔥🔥**

**Thời gian ước tính:** 2 tuần  
**Mục tiêu:** Hoàn thành các thuốc nội tiết và thần kinh quan trọng

**Bước 2.1: Endocrinology (11 thuốc)**
- Ưu tiên: Levothyroxine, Methimazole, Propylthiouracil
- Tiếp theo: Prednisone, Prednisolone, Methylprednisolone, Hydrocortisone
- Sau đó: Dexamethasone, Budesonide, Fludrocortisone, Testosterone
- **File:** `drugs/drug_modules/metabolic/`, `endocrinology_other/`
- **Thời gian:** 1.5 tuần

**Bước 2.2: Neurology/Psychiatry (7 thuốc)**
- Phenytoin, Levetiracetam, Topiramate
- Donepezil, Rivastigmine, Memantine
- Sumatriptan
- **File:** `drugs/drug_modules/neurological/`, `analgesics/`
- **Thời gian:** 0.5 tuần

#### **GIAI ĐOẠN 3: Gastrointestinal & Respiratory (18 thuốc) - 🔥**

**Thời gian ước tính:** 1.5 tuần  
**Mục tiêu:** Hoàn thành các thuốc tiêu hóa và hô hấp

**Bước 3.1: Gastrointestinal (10 thuốc)**
- PPI: Lansoprazole, Esomeprazole, Rabeprazole
- H2 blockers: Ranitidine, Famotidine
- Prokinetics: Domperidone, Metoclopramide
- Antidiarrheals: Loperamide, Bismuth subsalicylate
- Mucosal protectant: Sucralfate
- **File:** `drugs/drug_modules/gastrointestinal/`
- **Thời gian:** 1 tuần

**Bước 3.2: Respiratory (8 thuốc)**
- LABA: Salmeterol, Formoterol
- Anticholinergics: Ipratropium, Tiotropium
- Leukotriene: Montelukast
- ICS: Budesonide inhaled, Fluticasone inhaled, Beclomethasone inhaled
- **File:** `drugs/drug_modules/respiratory/`
- **Thời gian:** 0.5 tuần

#### **GIAI ĐOẠN 4: Oncology & Analgesics (17 thuốc) - 🔥**

**Thời gian ước tính:** 1.5 tuần  
**Mục tiêu:** Hoàn thành các thuốc ung thư và giảm đau

**Bước 4.1: Oncology (10 thuốc)**
- Platinum: Oxaliplatin
- Antimetabolites: 5-FU, Gemcitabine
- Alkylating: Ifosfamide
- Anthracyclines: Doxorubicin
- Taxanes: Paclitaxel, Docetaxel
- Topoisomerase: Irinotecan
- Antiemetics: Granisetron, Palonosetron
- **File:** `drugs/drug_modules/oncology/`
- **Thời gian:** 1 tuần

**Bước 4.2: Analgesics (7 thuốc)**
- NSAIDs: Naproxen, Diclofenac, Ketorolac
- Opioid strong: Morphine, Fentanyl
- Opioid weak: Codeine, Tramadol
- **File:** `drugs/drug_modules/analgesics/`
- **Thời gian:** 0.5 tuần

#### **GIAI ĐOẠN 5: Các Nhóm Còn Lại (20 thuốc) - ⚡**

**Thời gian ước tính:** 1 tuần  
**Mục tiêu:** Hoàn thành các nhóm còn lại

**Bước 5.1: Diabetes (6 thuốc)**
- SGLT2: Empagliflozin, Dapagliflozin
- DPP-4: Sitagliptin, Vildagliptin
- TZD: Pioglitazone
- Alpha-glucosidase: Acarbose
- **File:** `drugs/drug_modules/diabetes/`
- **Thời gian:** 0.3 tuần

**Bước 5.2: Allergy (5 thuốc)**
- Loratadine, Cetirizine, Fexofenadine, Desloratadine, Levocetirizine
- **File:** `drugs/drug_modules/supportive/`
- **Thời gian:** 0.2 tuần

**Bước 5.3: Hematology (9 thuốc)**
- Warfarin, Aspirin, Clopidogrel, Ticagrelor, Prasugrel
- Enoxaparin, Heparin, Fondaparinux, Rivaroxaban
- **File:** `drugs/drug_modules/cardiovascular/`, `cardiovascular_other/`
- **Thời gian:** 0.3 tuần

**Bước 5.4: Other/Miscellaneous (8 thuốc)**
- Allopurinol, Colchicine, Probenecid
- Methotrexate, Cyclosporine, Tacrolimus, Mycophenolate, Azathioprine
- **File:** `drugs/drug_modules/miscellaneous/`, `other.py`
- **Thời gian:** 0.2 tuần

### 4.3. Tổng Kết Thời Gian

| Giai Đoạn | Số Thuốc | Thời Gian Ước Tính | Ưu tiên |
|-----------|----------|-------------------|---------|
| Giai đoạn 1 | 29 | 2-3 tuần | 🔥🔥🔥 |
| Giai đoạn 2 | 18 | 2 tuần | 🔥🔥 |
| Giai đoạn 3 | 18 | 1.5 tuần | 🔥 |
| Giai đoạn 4 | 17 | 1.5 tuần | 🔥 |
| Giai đoạn 5 | 20 | 1 tuần | ⚡ |
| **TỔNG** | **102** | **8-9 tuần** | |

---

## 5. 📋 CHECKLIST TRIỂN KHAI

### 5.1. Checklist Cho Mỗi Thuốc

- [ ] Thu thập đầy đủ thông tin từ nguồn đáng tin cậy
- [ ] Xác định file module đúng
- [ ] Tạo dictionary entry với đầy đủ các trường cơ bản
- [ ] Thêm enhanced_fields (6 fields cơ bản bắt buộc)
- [ ] Thêm enhanced_fields (8 fields tùy chọn nếu có thông tin)
- [ ] Kiểm tra format đúng với cấu trúc hiện tại
- [ ] Cập nhật DRUG_GROUPS trong `drug_utils/groups.py`
- [ ] Validate không có lỗi syntax
- [ ] Test import module
- [ ] Test search functionality
- [ ] Test display drug info

### 5.2. Checklist Cho Mỗi Nhóm

- [ ] Hoàn thành tất cả thuốc trong nhóm
- [ ] Validate tất cả thuốc trong nhóm
- [ ] Test tất cả thuốc trong nhóm
- [ ] Cập nhật documentation
- [ ] Commit changes với message rõ ràng

### 5.3. Checklist Tổng Thể

- [ ] Hoàn thành tất cả 5 giai đoạn
- [ ] Tổng số thuốc đạt 300+
- [ ] Tất cả thuốc có enhanced_fields đầy đủ
- [ ] DRUG_GROUPS được cập nhật đầy đủ
- [ ] Test toàn bộ hệ thống
- [ ] Cập nhật tài liệu tổng thể
- [ ] Review code quality
- [ ] Deploy và test production

---

## 6. 📚 NGUỒN THAM KHẢO ĐỀ XUẤT

### 6.1. Nguồn Chính Thức

1. **FDA Drug Labels** - https://www.fda.gov/drugs
2. **UpToDate** - Clinical drug information
3. **Medscape** - Drug reference
4. **Goodman & Gilman's** - Pharmacology textbook
5. **Katzung & Trevor's** - Pharmacology textbook

### 6.2. Nguồn Tiếng Việt

1. **Dược thư Quốc gia Việt Nam**
2. **Hướng dẫn sử dụng thuốc Bộ Y tế**
3. **Các tài liệu lâm sàng tại Việt Nam**

### 6.3. Nguồn Bổ sung

1. **Micromedex** - Drug information
2. **Lexicomp** - Drug information
3. **Clinical guidelines** - Từ các hiệp hội y khoa

---

## 7. ⚠️ LƯU Ý QUAN TRỌNG

### 7.1. Chất Lượng Hơn Số Lượng

- **Ưu tiên chất lượng:** Mỗi thuốc phải có thông tin chính xác, đầy đủ
- **Không vội vàng:** Tốt hơn là làm chậm nhưng đúng
- **Review kỹ:** Mỗi thuốc nên được review trước khi commit

### 7.2. Tính Nhất Quán

- **Format nhất quán:** Tất cả thuốc phải theo cùng một format
- **Thuật ngữ nhất quán:** Sử dụng thuật ngữ y khoa chuẩn
- **Cấu trúc nhất quán:** Tuân thủ cấu trúc module hiện tại

### 7.3. Tính Bảo Trì

- **Code sạch:** Code dễ đọc, dễ hiểu
- **Comment đầy đủ:** Comment rõ ràng cho các phần phức tạp
- **Documentation:** Cập nhật documentation khi thêm thuốc mới

### 7.4. Tính Mở Rộng

- **Dễ mở rộng:** Cấu trúc phải dễ thêm thuốc mới sau này
- **Không hardcode:** Tránh hardcode các giá trị
- **Module hóa:** Tổ chức theo module để dễ quản lý

---

## 8. 📊 KẾT QUẢ MONG ĐỢI

### 8.1. Số Lượng

- **Trước:** 239 thuốc
- **Sau:** 300+ thuốc (ít nhất 341 thuốc với 102 thuốc mới)
- **Tăng:** +42.7% (ít nhất)

### 8.2. Chất Lượng

- **100% thuốc có enhanced_fields (6 fields cơ bản)**
- **≥80% thuốc có enhanced_fields đầy đủ (14 fields)**
- **Tất cả thuốc có thông tin chính xác, đầy đủ**

### 8.3. Phân Bố

- **Cân bằng hơn:** Các nhóm được bổ sung đều
- **Đầy đủ hơn:** Các nhóm thiếu được bổ sung
- **Phù hợp hơn:** Phù hợp với nhu cầu lâm sàng tại Việt Nam

---

## 9. ✅ KẾT LUẬN

### 9.1. Tóm Tắt

1. **Hiện trạng:** 239 thuốc, cần thêm 61+ thuốc để đạt 300+
2. **Đề xuất:** 102 thuốc được đề xuất (vượt mục tiêu để có buffer)
3. **Cấu trúc:** Tuân thủ cấu trúc hiện tại với enhanced_fields đầy đủ
4. **Thứ tự:** Ưu tiên Emergency → Antibiotics → Endocrinology → Các nhóm khác

### 9.2. Bước Tiếp Theo

1. **Review và phê duyệt** đề xuất này
2. **Bắt đầu Giai đoạn 1:** Emergency & Antibiotics
3. **Theo dõi tiến độ** theo từng giai đoạn
4. **Validate và test** sau mỗi giai đoạn
5. **Hoàn thành** tất cả 5 giai đoạn

---

**Ngày tạo:** 2025-02-05  
**Phiên bản:** 1.0  
**Trạng thái:** 📋 Sẵn sàng triển khai  
**Bước tiếp theo:** Review và phê duyệt, sau đó bắt đầu Giai đoạn 1
