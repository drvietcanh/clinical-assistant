# HƯỚNG DẪN THAM CHIẾU - THÊM THUỐC MỚI

**Ngày tạo**: 2025-02-18
**Tổng số thuốc**: 721

---

## 📋 MỤC LỤC

1. [Cấu trúc 14 field chuẩn](#cấu-trúc-14-field-chuẩn)
2. [Template thuốc mẫu](#template-thuốc-mẫu)
3. [Danh sách thuốc theo nhóm](#danh-sách-thuốc-theo-nhóm)
4. [Danh sách thuốc theo file](#danh-sách-thuốc-theo-file)
5. [Danh sách tất cả thuốc](#danh-sách-tất-cả-thuốc)
6. [Hướng dẫn thêm thuốc mới](#hướng-dẫn-thêm-thuốc-mới)

---

## 1. CẤU TRÚC 14 FIELD CHUẨN

### Thứ tự khoa học (BẮT BUỘC):

1. **group**
2. **vietnamese_name**
3. **administration**
4. **indications**
5. **dosage**
6. **side_effects**
7. **contraindications**
8. **interactions**
9. **pregnancy**
10. **mechanism_of_action**
11. **monitoring**
12. **precautions**
13. **pharmacokinetics**
14. **storage**

### Mô tả từng field:

- **group**: Nhóm thuốc (ví dụ: 'Antibiotic - Aminoglycoside')
- **vietnamese_name**: Tên tiếng Việt và biệt dược (ví dụ: 'Gentamicin, Garamycin')
- **administration**: Đường dùng (list, ví dụ: ['IV', 'IM'])
- **indications**: Chỉ định (list, ví dụ: ['Nhiễm khuẩn Gram-âm nặng', ...])
- **dosage**: Liều dùng (dict với adult_standard, adult_maintenance, notes)
- **side_effects**: Tác dụng phụ (list)
- **contraindications**: Chống chỉ định (list)
- **interactions**: Tương tác thuốc (list)
- **pregnancy**: Phân loại thai kỳ (string, ví dụ: 'D - Độc thai nhi')
- **mechanism_of_action**: Cơ chế tác dụng (string, mô tả chi tiết)
- **monitoring**: Theo dõi (list)
- **precautions**: Thận trọng (list)
- **pharmacokinetics**: Dược động học (dict với half_life, onset, duration, protein_binding, clearance)
- **storage**: Bảo quản (string)

---

## 2. TEMPLATE THUỐC MẪU

```python
"DrugName": {
    # Core Fields (1-5)
    "group": "Antibiotic - Category",
    "vietnamese_name": "DrugName, BrandName",
    "administration": ["IV", "PO"],
    "indications": [
        "Chỉ định 1",
        "Chỉ định 2"
    ],
    "dosage": {
        "adult_standard": "Liều chuẩn",
        "adult_maintenance": "Liều duy trì",
        "notes": "Ghi chú"
    },
    
    # Extended Fields (6-9)
    "side_effects": [
        "Tác dụng phụ 1",
        "Tác dụng phụ 2"
    ],
    "contraindications": [
        "Chống chỉ định 1",
        "Chống chỉ định 2"
    ],
    "interactions": [
        "Tương tác 1",
        "Tương tác 2"
    ],
    "pregnancy": "Category - Mô tả",
    
    # Enhanced Fields (10-14)
    "mechanism_of_action": "Mô tả cơ chế tác dụng chi tiết...",
    "monitoring": [
        "Theo dõi 1",
        "Theo dõi 2"
    ],
    "precautions": [
        "Thận trọng 1",
        "Thận trọng 2"
    ],
    "pharmacokinetics": {
        "half_life": "...",
        "onset": "...",
        "duration": "...",
        "protein_binding": "...",
        "clearance": "..."
    },
    "storage": "Hướng dẫn bảo quản"
}
```

---

## 3. DANH SÁCH THUỐC THEO NHÓM

**Tổng số nhóm**: 444

### Neurology - Anticonvulsant
**Số lượng**: 13 thuốc

Danh sách:
  1. Carbamazepine (drug_modules\neurological\anticonvulsants.py)
  2. Ethosuximide (drug_modules\neurological\anticonvulsants.py)
  3. Lacosamide (drug_modules\neurological\anticonvulsants.py)
  4. Lamotrigine (drug_modules\neurological\anticonvulsants.py)
  5. Levetiracetam (drug_modules\neurological\anticonvulsants.py)
  6. Oxcarbazepine (drug_modules\neurological\anticonvulsants.py)
  7. Perampanel (drug_modules\neurological\anticonvulsants.py)
  8. Phenobarbital (drug_modules\neurological\anticonvulsants.py)
  9. Phenytoin (drug_modules\neurological\anticonvulsants.py)
 10. Primidone (drug_modules\neurological\anticonvulsants.py)
 11. Topiramate (drug_modules\neurological\anticonvulsants.py)
 12. Valproate (drug_modules\neurological\anticonvulsants.py)
 13. Zonisamide (drug_modules\neurological\anticonvulsants.py)

### Analgesic - NSAID
**Số lượng**: 8 thuốc

Danh sách:
  1. Diclofenac (drug_modules\analgesics\nsaids.py)
  2. Ibuprofen (drug_modules\analgesics\nsaids.py)
  3. Indomethacin (drug_modules\analgesics\nsaids.py)
  4. Ketoprofen (drug_modules\analgesics\nsaids.py)
  5. Ketorolac (drug_modules\analgesics\nsaids.py)
  6. Meloxicam (drug_modules\analgesics\nsaids.py)
  7. Naproxen (drug_modules\analgesics\nsaids.py)
  8. Piroxicam (drug_modules\analgesics\nsaids.py)

### Cardiovascular - ARB (Angiotensin Receptor Blocker)
**Số lượng**: 7 thuốc

Danh sách:
  1. Azilsartan medoxomil (drug_modules\cardiovascular\arbs.py)
  2. Candesartan (drug_modules\cardiovascular\arbs.py)
  3. Irbesartan (drug_modules\cardiovascular\arbs.py)
  4. Losartan (drug_modules\cardiovascular\arbs.py)
  5. Olmesartan (drug_modules\cardiovascular\arbs.py)
  6. Telmisartan (drug_modules\cardiovascular\arbs.py)
  7. Valsartan (drug_modules\cardiovascular\arbs.py)

### Cardiovascular - Calcium Channel Blocker (Dihydropyridine)
**Số lượng**: 7 thuốc

Danh sách:
  1. Amlodipine (drug_modules\cardiovascular\calcium_blockers\dihydropyridines.py)
  2. Felodipine (drug_modules\cardiovascular\calcium_blockers\dihydropyridines.py)
  3. Isradipine (drug_modules\cardiovascular\calcium_blockers\dihydropyridines.py)
  4. Lacidipine (drug_modules\cardiovascular\calcium_blockers\dihydropyridines.py)
  5. Nicardipine (drug_modules\cardiovascular\calcium_blockers\dihydropyridines.py)
  6. Nifedipine (drug_modules\cardiovascular\calcium_blockers\dihydropyridines.py)
  7. Nisoldipine (drug_modules\cardiovascular\calcium_blockers\dihydropyridines.py)

### Analgesic - Opioid Agonist (Strong)
**Số lượng**: 6 thuốc

Danh sách:
  1. Fentanyl (drug_modules\analgesics\opioid_agonist_strongs.py)
  2. Hydromorphone (drug_modules\analgesics\opioid_agonist_strongs.py)
  3. Meperidine (drug_modules\analgesics\opioid_agonist_strongs.py)
  4. Methadone (drug_modules\analgesics\opioid_agonist_strongs.py)
  5. Morphine (drug_modules\analgesics\opioid_agonist_strongs.py)
  6. Oxycodone (drug_modules\analgesics\opioid_agonist_strongs.py)

### Antibiotic - Fluoroquinolone
**Số lượng**: 6 thuốc

Danh sách:
  1. Ciprofloxacin (drug_modules\antimicrobial\antibiotics\fluoroquinolones.py)
  2. Gemifloxacin (drug_modules\infectious_other\fluoroquinolones.py)
  3. Levofloxacin (drug_modules\antimicrobial\antibiotics\fluoroquinolones.py)
  4. Norfloxacin (drug_modules\antimicrobial\antibiotics\fluoroquinolones.py)
  5. Ofloxacin (drug_modules\antimicrobial\antibiotics\fluoroquinolones.py)
  6. Sparfloxacin (drug_modules\infectious_other\fluoroquinolones.py)

### Cardiovascular - ACE Inhibitor
**Số lượng**: 6 thuốc

Danh sách:
  1. Benazepril (drug_modules\cardiovascular\ace_inhibitors.py)
  2. Captopril (drug_modules\cardiovascular\ace_inhibitors.py)
  3. Enalapril (drug_modules\cardiovascular\ace_inhibitors.py)
  4. Lisinopril (drug_modules\cardiovascular\ace_inhibitors.py)
  5. Perindopril (drug_modules\cardiovascular\ace_inhibitors.py)
  6. Ramipril (drug_modules\cardiovascular\ace_inhibitors.py)

### Cardiovascular - Statin (HMG-CoA Reductase Inhibitor)
**Số lượng**: 6 thuốc

Danh sách:
  1. Atorvastatin (drug_modules\cardiovascular\statins.py)
  2. Fluvastatin (drug_modules\cardiovascular\statins.py)
  3. Lovastatin (drug_modules\cardiovascular\statins.py)
  4. Pitavastatin (drug_modules\cardiovascular\statins.py)
  5. Pravastatin (drug_modules\cardiovascular\statins.py)
  6. Rosuvastatin (drug_modules\cardiovascular\statins.py)

### Psychiatry - Antipsychotic (Atypical)
**Số lượng**: 6 thuốc

Danh sách:
  1. Clozapine (drug_modules\psychiatry_other\antipsychotics.py)
  2. Lurasidone (drug_modules\psychiatry_other\antipsychotics.py)
  3. Olanzapine (drug_modules\psychiatry_other\antipsychotics.py)
  4. Quetiapine (drug_modules\psychiatry_other\antipsychotics.py)
  5. Risperidone (drug_modules\psychiatry_other\antipsychotics.py)
  6. Ziprasidone (drug_modules\psychiatry_other\antipsychotics.py)

### Cardiovascular - Antiarrhythmic (Class III)
**Số lượng**: 5 thuốc

Danh sách:
  1. Amiodarone (drug_modules\cardiovascular\antiarrhythmics.py)
  2. Dofetilide (drug_modules\cardiovascular\antiarrhythmics.py)
  3. Dronedarone (drug_modules\cardiovascular\antiarrhythmics.py)
  4. Ibutilide (drug_modules\cardiovascular\antiarrhythmics.py)
  5. Sotalol (drug_modules\cardiovascular\antiarrhythmics.py)

### Dermatology - Topical Antifungal
**Số lượng**: 5 thuốc

Danh sách:
  1. Clotrimazole topical (drug_modules\dermatology.py)
  2. Econazole topical (drug_modules\dermatology.py)
  3. Ketoconazole topical (drug_modules\dermatology.py)
  4. Miconazole topical (drug_modules\dermatology.py)
  5. Terbinafine topical (drug_modules\dermatology.py)

### Diabetes - DPP-4 Inhibitor
**Số lượng**: 5 thuốc

Danh sách:
  1. Alogliptin (drug_modules\diabetes\dpp_4_inhibitors.py)
  2. Linagliptin (drug_modules\diabetes\dpp_4_inhibitors.py)
  3. Saxagliptin (drug_modules\diabetes\dpp_4_inhibitors.py)
  4. Sitagliptin (drug_modules\diabetes\dpp_4_inhibitors.py)
  5. Vildagliptin (drug_modules\diabetes\dpp_4_inhibitors.py)

### Endocrinology - Corticosteroid
**Số lượng**: 5 thuốc

Danh sách:
  1. Betamethasone (drug_modules\endocrinology_other\corticosteroids\long_acting.py)
  2. Dexamethasone (drug_modules\endocrinology_other\corticosteroids\long_acting.py)
  3. Hydrocortisone (drug_modules\endocrinology_other\corticosteroids\short_intermediate_acting.py)
  4. Methylprednisolone (drug_modules\endocrinology_other\corticosteroids\short_intermediate_acting.py)
  5. Prednisolone (drug_modules\endocrinology_other\corticosteroids\short_intermediate_acting.py)

### Infectious Disease - Anthelmintic
**Số lượng**: 5 thuốc

Danh sách:
  1. Albendazole (drug_modules\infectious_other\anthelmintics.py)
  2. Ivermectin (drug_modules\infectious_other\anthelmintics.py)
  3. Levamisole (drug_modules\infectious_other\anthelmintics.py)
  4. Mebendazole (drug_modules\infectious_other\anthelmintics.py)
  5. Praziquantel (drug_modules\infectious_other\anthelmintics.py)

### Respiratory - Long-acting Beta-2 Agonist (LABA)
**Số lượng**: 5 thuốc

Danh sách:
  1. Formoterol (drug_modules\respiratory\long_acting_beta_2_agonist_labas.py)
  2. Indacaterol (drug_modules\respiratory\long_acting_beta_2_agonist_labas.py)
  3. Olodaterol (drug_modules\respiratory\long_acting_beta_2_agonist_labas.py)
  4. Salmeterol (drug_modules\respiratory\long_acting_beta_2_agonist_labas.py)
  5. Vilanterol (drug_modules\respiratory\long_acting_beta_2_agonist_labas.py)

### Allergy - Antihistamine (H1 Antagonist, 2nd generation)
**Số lượng**: 5 thuốc

Danh sách:
  1. Cetirizine (drug_modules\supportive\antihistamine_h1_antagonist_2nd_generations.py)
  2. Desloratadine (drug_modules\supportive\antihistamine_h1_antagonist_2nd_generations.py)
  3. Fexofenadine (drug_modules\supportive\antihistamine_h1_antagonist_2nd_generations.py)
  4. Levocetirizine (drug_modules\supportive\antihistamine_h1_antagonist_2nd_generations.py)
  5. Loratadine (drug_modules\supportive\antihistamine_h1_antagonist_2nd_generations.py)

### Analgesic - Combination (Paracetamol + Muscle Relaxant)
**Số lượng**: 4 thuốc

Danh sách:
  1. Paracetamol/Carisoprodol (drug_modules\analgesics\pain_muscle_relaxant_combinations.py)
  2. Paracetamol/Chlorzoxazone (drug_modules\analgesics\pain_muscle_relaxant_combinations.py)
  3. Paracetamol/Methocarbamol (drug_modules\analgesics\pain_muscle_relaxant_combinations.py)
  4. Paracetamol/Orphenadrine (drug_modules\analgesics\pain_muscle_relaxant_combinations.py)

### Antibiotic - Carbapenem
**Số lượng**: 4 thuốc

Danh sách:
  1. Doripenem (drug_modules\antimicrobial\antibiotics\beta_lactams.py)
  2. Ertapenem (drug_modules\antimicrobial\antibiotics\beta_lactams.py)
  3. Imipenem-cilastatin (drug_modules\antimicrobial\antibiotics\beta_lactams.py)
  4. Meropenem (drug_modules\antimicrobial\antibiotics\beta_lactams.py)

### Antibiotic - Cephalosporin (3rd Generation)
**Số lượng**: 4 thuốc

Danh sách:
  1. Cefoperazone (drug_modules\infectious_other\cephalosporins.py)
  2. Cefotaxime (drug_modules\infectious_other\cephalosporins.py)
  3. Ceftazidime (drug_modules\infectious_other\cephalosporins.py)
  4. Ceftriaxone (drug_modules\antimicrobial\antibiotics\cephalosporins.py)

### Infectious Disease - Antiviral
**Số lượng**: 4 thuốc

Danh sách:
  1. Acyclovir (drug_modules\antimicrobial\antivirals\herpes.py)
  2. Ganciclovir (drug_modules\antimicrobial\antivirals\cmv.py)
  3. Ribavirin (drug_modules\antimicrobial\antivirals\hepatitis.py)
  4. Valacyclovir (drug_modules\antimicrobial\antivirals\herpes.py)

### Dermatology - Topical Antibiotic
**Số lượng**: 4 thuốc

Danh sách:
  1. Clindamycin topical (drug_modules\dermatology.py)
  2. Erythromycin topical (drug_modules\dermatology.py)
  3. Fusidic Acid (drug_modules\dermatology.py)
  4. Mupirocin topical (drug_modules\dermatology.py)

### Diabetes - GLP-1 Receptor Agonist
**Số lượng**: 4 thuốc

Danh sách:
  1. Dulaglutide (drug_modules\diabetes\glp1_agonists.py)
  2. Exenatide (drug_modules\diabetes\glp1_agonists.py)
  3. Liraglutide (drug_modules\diabetes\glp1_agonists.py)
  4. Semaglutide (drug_modules\diabetes\glp1_agonists.py)

### Diabetes - SGLT2 Inhibitor
**Số lượng**: 4 thuốc

Danh sách:
  1. Canagliflozin (drug_modules\diabetes\sglt2_inhibitors.py)
  2. Dapagliflozin (drug_modules\diabetes\sglt2_inhibitors.py)
  3. Empagliflozin (drug_modules\diabetes\sglt2_inhibitors.py)
  4. Ertugliflozin (drug_modules\diabetes\sglt2_inhibitors.py)

### Emergency - Catecholamine (Alpha & Beta Agonist)
**Số lượng**: 4 thuốc

Danh sách:
  1. Dobutamine (drug_modules\emergency\catecholamine_alpha__beta_agonists.py)
  2. Dopamine (drug_modules\emergency\catecholamine_alpha__beta_agonists.py)
  3. Epinephrine (drug_modules\emergency\catecholamine_alpha__beta_agonists.py)
  4. Norepinephrine (drug_modules\emergency\catecholamine_alpha__beta_agonists.py)

### Emergency - Electrolyte
**Số lượng**: 4 thuốc

Danh sách:
  1. Calcium chloride (drug_modules\emergency\electrolytes.py)
  2. Calcium gluconate (drug_modules\emergency\electrolytes.py)
  3. Magnesium sulfate (drug_modules\emergency\electrolytes.py)
  4. Sodium bicarbonate (drug_modules\emergency\electrolytes.py)

### Gastrointestinal - Proton Pump Inhibitor (PPI)
**Số lượng**: 4 thuốc

Danh sách:
  1. Esomeprazole (drug_modules\gastrointestinal\proton_pump_inhibitor_ppis.py)
  2. Ilaprazole (drug_modules\gastrointestinal\proton_pump_inhibitor_ppis.py)
  3. Lansoprazole (drug_modules\gastrointestinal\proton_pump_inhibitor_ppis.py)
  4. Omeprazole (drug_modules\gastrointestinal\proton_pump_inhibitor_ppis.py)

### Biological - Monoclonal Antibody (anti-PD-1)
**Số lượng**: 4 thuốc

Danh sách:
  1. Cemiplimab (drug_modules\miscellaneous\biological_drugs.py)
  2. Dostarlimab (drug_modules\miscellaneous\biological_drugs.py)
  3. Nivolumab (drug_modules\miscellaneous\biological_drugs.py)
  4. Pembrolizumab (drug_modules\miscellaneous\biological_drugs.py)

### Neurology - Muscle Relaxant (Skeletal)
**Số lượng**: 4 thuốc

Danh sách:
  1. Carisoprodol (drug_modules\neurological\muscle_relaxants.py)
  2. Cyclobenzaprine (drug_modules\neurological\muscle_relaxants.py)
  3. Metaxalone (drug_modules\neurological\muscle_relaxants.py)
  4. Methocarbamol (drug_modules\neurological\muscle_relaxants.py)

### Psychiatry - SSRI (Selective Serotonin Reuptake Inhibitor)
**Số lượng**: 4 thuốc

Danh sách:
  1. Fluoxetine (drug_modules\neurological\ssri_selective_serotonin_reuptake_inhibitors.py)
  2. Fluvoxamine (drug_modules\psychiatry_other\ssris.py)
  3. Paroxetine (drug_modules\psychiatry_other\ssris.py)
  4. Sertraline (drug_modules\psychiatry_other\ssris.py)

### Respiratory - Anticholinergic (Long-acting)
**Số lượng**: 4 thuốc

Danh sách:
  1. Aclidinium (drug_modules\respiratory\anticholinergic_long_actings.py)
  2. Glycopyrronium (drug_modules\respiratory\anticholinergic_long_actings.py)
  3. Tiotropium (drug_modules\respiratory\anticholinergic_long_actings.py)
  4. Umeclidinium (drug_modules\respiratory\anticholinergic_long_actings.py)

### Respiratory - Inhaled Corticosteroid (ICS)
**Số lượng**: 4 thuốc

Danh sách:
  1. Beclomethasone inhaled (drug_modules\respiratory\inhaled_corticosteroid_icss.py)
  2. Budesonide inhaled (drug_modules\respiratory\inhaled_corticosteroid_icss.py)
  3. Ciclesonide (drug_modules\respiratory\inhaled_corticosteroid_icss.py)
  4. Fluticasone inhaled (drug_modules\respiratory\inhaled_corticosteroid_icss.py)

### Urology - Anticholinergic (Overactive Bladder)
**Số lượng**: 4 thuốc

Danh sách:
  1. Fesoterodine (drug_modules\urology.py)
  2. Oxybutynin (drug_modules\urology.py)
  3. Solifenacin (drug_modules\urology.py)
  4. Tolterodine (drug_modules\urology.py)

### Antibiotic - Aminoglycoside
**Số lượng**: 3 thuốc

Danh sách:
  1. Amikacin (drug_modules\antimicrobial\antibiotics\aminoglycosides.py)
  2. Gentamicin (drug_modules\antimicrobial\antibiotics\aminoglycosides.py)
  3. Tobramycin (drug_modules\antimicrobial\antibiotics\aminoglycosides.py)

### Antibiotic - Penicillin/Beta-lactamase Inhibitor
**Số lượng**: 3 thuốc

Danh sách:
  1. Amoxicillin-clavulanate (drug_modules\antimicrobial\antibiotics\penicillins.py)
  2. Ampicillin-sulbactam (drug_modules\antimicrobial\antibiotics\penicillins.py)
  3. Piperacillin-tazobactam (drug_modules\antimicrobial\antibiotics\beta_lactams.py)

### Antibiotic - Tetracycline
**Số lượng**: 3 thuốc

Danh sách:
  1. Doxycycline (drug_modules\antimicrobial\antibiotics\tetracyclines.py)
  2. Minocycline (drug_modules\antimicrobial\antibiotics\tetracyclines.py)
  3. Tetracycline (drug_modules\antimicrobial\antibiotics\tetracyclines.py)

### Infectious Disease - Antifungal (Echinocandin)
**Số lượng**: 3 thuốc

Danh sách:
  1. Anidulafungin (drug_modules\antimicrobial\antifungals\echinocandins.py)
  2. Caspofungin (drug_modules\antimicrobial\antifungals\echinocandins.py)
  3. Micafungin (drug_modules\antimicrobial\antifungals\echinocandins.py)

### Cardiovascular - Antiarrhythmic (Class IA)
**Số lượng**: 3 thuốc

Danh sách:
  1. Disopyramide (drug_modules\cardiovascular\antiarrhythmics.py)
  2. Procainamide (drug_modules\cardiovascular\antiarrhythmics.py)
  3. Quinidine (drug_modules\cardiovascular\antiarrhythmics.py)

### Cardiovascular - Antiplatelet (P2Y12 Inhibitor)
**Số lượng**: 3 thuốc

Danh sách:
  1. Clopidogrel (drug_modules\cardiovascular\anticoagulants.py)
  2. Prasugrel (drug_modules\cardiovascular\anticoagulants.py)
  3. Ticagrelor (drug_modules\cardiovascular\anticoagulants.py)

### Cardiovascular - Anticoagulant (Direct Factor Xa Inhibitor - DOAC)
**Số lượng**: 3 thuốc

Danh sách:
  1. Apixaban (drug_modules\cardiovascular\anticoagulants.py)
  2. Edoxaban (drug_modules\cardiovascular\anticoagulants.py)
  3. Rivaroxaban (drug_modules\cardiovascular\anticoagulants.py)

### Cardiovascular - Beta-blocker (non-selective)
**Số lượng**: 3 thuốc

Danh sách:
  1. Nadolol (drug_modules\cardiovascular\beta_blockers\non_selective.py)
  2. Propranolol (drug_modules\cardiovascular\beta_blockers\non_selective.py)
  3. Timolol (drug_modules\cardiovascular\beta_blockers\non_selective.py)

### Cardiovascular - Loop Diuretic
**Số lượng**: 3 thuốc

Danh sách:
  1. Bumetanide (drug_modules\cardiovascular\diuretics.py)
  2. Furosemide (drug_modules\cardiovascular\diuretics.py)
  3. Torsemide (drug_modules\cardiovascular\diuretics.py)

### Diabetes - Rapid-Acting Insulin
**Số lượng**: 3 thuốc

Danh sách:
  1. Insulin Aspart (drug_modules\diabetes\specific_insulins.py)
  2. Insulin Glulisine (drug_modules\diabetes\specific_insulins.py)
  3. Insulin Lispro (drug_modules\diabetes\specific_insulins.py)

### Endocrinology - Bisphosphonate (Osteoporosis)
**Số lượng**: 3 thuốc

Danh sách:
  1. Alendronate (drug_modules\endocrinology_other\osteoporosis_bisphosphonates.py)
  2. Ibandronate (drug_modules\endocrinology_other\osteoporosis_bisphosphonates.py)
  3. Risedronate (drug_modules\endocrinology_other\osteoporosis_bisphosphonates.py)

### ENT - Combination (Oral Antihistamine + Decongestant)
**Số lượng**: 3 thuốc

Danh sách:
  1. Cetirizine/Pseudoephedrine (drug_modules\ent_oral_nasal_combinations.py)
  2. Fexofenadine/Pseudoephedrine (drug_modules\ent_oral_nasal_combinations.py)
  3. Loratadine/Pseudoephedrine (drug_modules\ent_oral_nasal_combinations.py)

### Gastrointestinal - H2 Receptor Antagonist
**Số lượng**: 3 thuốc

Danh sách:
  1. Cimetidine (drug_modules\gastrointestinal\h2_receptor_antagonists.py)
  2. Famotidine (drug_modules\gastrointestinal\h2_receptor_antagonists.py)
  3. Ranitidine (drug_modules\gastrointestinal\h2_receptor_antagonists.py)

### Infectious Disease - Antitubercular (First-line)
**Số lượng**: 3 thuốc

Danh sách:
  1. Ethambutol (drug_modules\infectious_other\antituberculars.py)
  2. Isoniazid (drug_modules\infectious_other\antituberculars.py)
  3. Pyrazinamide (drug_modules\infectious_other\antituberculars.py)

### Biological - Monoclonal Antibody (anti-TNF-α)
**Số lượng**: 3 thuốc

Danh sách:
  1. Adalimumab (drug_modules\miscellaneous\biological_drugs.py)
  2. Golimumab (drug_modules\miscellaneous\biological_drugs.py)
  3. Infliximab (drug_modules\miscellaneous\biological_drugs.py)

### Neurology - Anti-amyloid Monoclonal Antibody
**Số lượng**: 3 thuốc

Danh sách:
  1. Aducanumab (drug_modules\neurological\alzheimer_dementia_drugs.py)
  2. Donanemab (drug_modules\neurological\alzheimer_dementia_drugs.py)
  3. Lecanemab (drug_modules\neurological\alzheimer_dementia_drugs.py)

### Neurology - Benzodiazepine
**Số lượng**: 3 thuốc

Danh sách:
  1. Clonazepam (drug_modules\neurological\benzodiazepines.py)
  2. Diazepam (drug_modules\neurological\benzodiazepines.py)
  3. Lorazepam (drug_modules\neurological\benzodiazepines.py)

### Neurology - Anti-CGRP Monoclonal Antibody
**Số lượng**: 3 thuốc

Danh sách:
  1. Eptinezumab (drug_modules\neurological\migraine_cgrp_drugs.py)
  2. Fremanezumab (drug_modules\neurological\migraine_cgrp_drugs.py)
  3. Galcanezumab (drug_modules\neurological\migraine_cgrp_drugs.py)

### Oncology - Antimetabolite
**Số lượng**: 3 thuốc

Danh sách:
  1. 5-Fluorouracil (drug_modules\oncology\antimetabolites.py)
  2. Capecitabine (drug_modules\oncology\antimetabolites.py)
  3. Gemcitabine (drug_modules\oncology\antimetabolites.py)

### Oncology - Antibody-Drug Conjugate (ADC)
**Số lượng**: 3 thuốc

Danh sách:
  1. Brentuximab vedotin (drug_modules\oncology\monoclonal_antibodies_adcs.py)
  2. Sacituzumab govitecan (drug_modules\oncology\monoclonal_antibodies_adcs.py)
  3. Trastuzumab deruxtecan (drug_modules\oncology\monoclonal_antibodies_adcs.py)

### Oncology - Platinum Compound
**Số lượng**: 3 thuốc

Danh sách:
  1. Carboplatin (drug_modules\oncology\platinum_compounds.py)
  2. Cisplatin (drug_modules\oncology\platinum_compounds.py)
  3. Oxaliplatin (drug_modules\oncology\platinum_compounds.py)

### Ophthalmology - Prostaglandin Analog (Glaucoma)
**Số lượng**: 3 thuốc

Danh sách:
  1. Bimatoprost (drug_modules\ophthalmology.py)
  2. Latanoprost (drug_modules\ophthalmology.py)
  3. Travoprost (drug_modules\ophthalmology.py)

### Psychiatry - Antipsychotic (Typical)
**Số lượng**: 3 thuốc

Danh sách:
  1. Fluphenazine (drug_modules\psychiatry_other\antipsychotics.py)
  2. Haloperidol (drug_modules\psychiatry_other\antipsychotics.py)
  3. Pimozide (drug_modules\psychiatry_other\antipsychotics.py)

### Psychiatry - SNRI (Serotonin-Norepinephrine Reuptake Inhibitor)
**Số lượng**: 3 thuốc

Danh sách:
  1. Desvenlafaxine (drug_modules\psychiatry_other\snris.py)
  2. Duloxetine (drug_modules\psychiatry_other\snris.py)
  3. Venlafaxine (drug_modules\psychiatry_other\snris.py)

### Allergy - Antihistamine (H1 Antagonist, 1st generation)
**Số lượng**: 3 thuốc

Danh sách:
  1. Chlorpheniramine (drug_modules\supportive\antihistamine_h1_antagonist_1st_generations.py)
  2. Diphenhydramine (drug_modules\supportive\antihistamine_h1_antagonist_1st_generations.py)
  3. Hydroxyzine (drug_modules\supportive\antihistamine_h1_antagonist_1st_generations.py)

### Urology - PDE-5 Inhibitor (Erectile Dysfunction)
**Số lượng**: 3 thuốc

Danh sách:
  1. Avanafil (drug_modules\urology.py)
  2. Sildenafil (drug_modules\urology.py)
  3. Vardenafil (drug_modules\urology.py)

### Analgesic - Antimigraine (5-HT1 Receptor Agonist)
**Số lượng**: 2 thuốc

Danh sách:
  1. Rizatriptan (drug_modules\analgesics\antimigraine_5_ht1_receptor_agonists.py)
  2. Sumatriptan (drug_modules\analgesics\antimigraine_5_ht1_receptor_agonists.py)

### Analgesic - NSAID (COX-2 Selective)
**Số lượng**: 2 thuốc

Danh sách:
  1. Celecoxib (drug_modules\analgesics\nsaids.py)
  2. Etoricoxib (drug_modules\analgesics\nsaids.py)

### Analgesic - Opioid Agonist
**Số lượng**: 2 thuốc

Danh sách:
  1. Hydrocodone (drug_modules\analgesics\opioid_agonists.py)
  2. Tramadol (drug_modules\analgesics\opioid_agonists.py)

### Antibiotic - Cephalosporin (1st Generation)
**Số lượng**: 2 thuốc

Danh sách:
  1. Cefazolin (drug_modules\antimicrobial\antibiotics\cephalosporins.py)
  2. Cephalexin (drug_modules\antimicrobial\antibiotics\cephalosporins.py)

### Antibiotic - Cephalosporin (4th Generation)
**Số lượng**: 2 thuốc

Danh sách:
  1. Cefepime (drug_modules\antimicrobial\antibiotics\cephalosporins.py)
  2. Cefpirome (drug_modules\infectious_other\cephalosporins.py)

### Antibiotic - Glycopeptide
**Số lượng**: 2 thuốc

Danh sách:
  1. Teicoplanin (drug_modules\antimicrobial\antibiotics\glycopeptides.py)
  2. Vancomycin (drug_modules\antimicrobial\antibiotics\glycopeptides.py)

### Antibiotic - Macrolide
**Số lượng**: 2 thuốc

Danh sách:
  1. Clarithromycin (drug_modules\antimicrobial\antibiotics\macrolides.py)
  2. Erythromycin (drug_modules\antimicrobial\antibiotics\macrolides.py)

### Antibiotic - Tetracycline (Next Generation)
**Số lượng**: 2 thuốc

Danh sách:
  1. Eravacycline (drug_modules\antimicrobial\antibiotics\others.py)
  2. Omadacycline (drug_modules\antimicrobial\antibiotics\others.py)

### Antibiotic - Penicillin (Aminopenicillin)
**Số lượng**: 2 thuốc

Danh sách:
  1. Amoxicillin (drug_modules\antimicrobial\antibiotics\penicillins.py)
  2. Ampicillin (drug_modules\antimicrobial\antibiotics\penicillins.py)

### Antibiotic - Penicillin (Anti-staphylococcal)
**Số lượng**: 2 thuốc

Danh sách:
  1. Nafcillin (drug_modules\antimicrobial\antibiotics\penicillins.py)
  2. Oxacillin (drug_modules\antimicrobial\antibiotics\penicillins.py)

### Antibiotic - Polymyxin
**Số lượng**: 2 thuốc

Danh sách:
  1. Colistin (drug_modules\antimicrobial\antibiotics\polymyxins.py)
  2. Polymyxin B (drug_modules\antimicrobial\antibiotics\polymyxins.py)

### Infectious Disease - Antifungal (Azole)
**Số lượng**: 2 thuốc

Danh sách:
  1. Fluconazole (drug_modules\antimicrobial\antifungals\azoles.py)
  2. Itraconazole (drug_modules\antimicrobial\antifungals\azoles.py)

### Infectious Disease - Antifungal (Polyene)
**Số lượng**: 2 thuốc

Danh sách:
  1. Amphotericin B (drug_modules\antimicrobial\antifungals\polyenes.py)
  2. Nystatin (drug_modules\antimicrobial\antifungals\polyenes.py)

### Antiviral - Nucleotide reverse transcriptase inhibitor (NRTI)
**Số lượng**: 2 thuốc

Danh sách:
  1. Tenofovir alafenamide (TAF) (drug_modules\antimicrobial\antivirals\hiv_arvs.py)
  2. Tenofovir disoproxil fumarate (TDF) (drug_modules\antimicrobial\antivirals\hiv_arvs.py)

### Antiviral - Nucleoside reverse transcriptase inhibitor (NRTI)
**Số lượng**: 2 thuốc

Danh sách:
  1. Emtricitabine (FTC) (drug_modules\antimicrobial\antivirals\hiv_arvs.py)
  2. Lamivudine (3TC) (drug_modules\antimicrobial\antivirals\hiv_arvs.py)

### Antiviral - Integrase strand transfer inhibitor (INSTI)
**Số lượng**: 2 thuốc

Danh sách:
  1. Bictegravir (BIC) (drug_modules\antimicrobial\antivirals\hiv_arvs.py)
  2. Dolutegravir (DTG) (drug_modules\antimicrobial\antivirals\hiv_arvs.py)

### Antiviral - Non-nucleoside reverse transcriptase inhibitor (NNRTI)
**Số lượng**: 2 thuốc

Danh sách:
  1. Efavirenz (EFV) (drug_modules\antimicrobial\antivirals\hiv_arvs.py)
  2. Rilpivirine (RPV) (drug_modules\antimicrobial\antivirals\hiv_arvs.py)

### Antiviral - NRTI fixed-dose combination
**Số lượng**: 2 thuốc

Danh sách:
  1. Tenofovir alafenamide/Emtricitabine (TAF/FTC) (drug_modules\antimicrobial\antivirals\hiv_arvs.py)
  2. Tenofovir disoproxil fumarate/Emtricitabine (TDF/FTC) (drug_modules\antimicrobial\antivirals\hiv_arvs.py)

### Antiviral - Protease inhibitor (boosted)
**Số lượng**: 2 thuốc

Danh sách:
  1. Atazanavir (boosted with ritonavir/cobicistat) (drug_modules\antimicrobial\antivirals\hiv_arvs.py)
  2. Darunavir (boosted with ritonavir/cobicistat) (drug_modules\antimicrobial\antivirals\hiv_arvs.py)

### Infectious Disease - Antiviral (Neuraminidase Inhibitor)
**Số lượng**: 2 thuốc

Danh sách:
  1. Oseltamivir (drug_modules\antimicrobial\antivirals\influenza.py)
  2. Zanamivir (drug_modules\antimicrobial\antivirals\influenza.py)

### Cardiovascular - Antiarrhythmic (Class IC)
**Số lượng**: 2 thuốc

Danh sách:
  1. Flecainide (drug_modules\cardiovascular\antiarrhythmics.py)
  2. Propafenone (drug_modules\cardiovascular\antiarrhythmics.py)

### Cardiovascular - Beta-blocker (Selective)
**Số lượng**: 2 thuốc

Danh sách:
  1. Atenolol (drug_modules\cardiovascular\beta_blockers\selective.py)
  2. Bisoprolol (drug_modules\cardiovascular\beta_blockers\selective.py)

### Cardiovascular - Beta-blocker (selective)
**Số lượng**: 2 thuốc

Danh sách:
  1. Acebutolol (drug_modules\cardiovascular\beta_blockers\selective.py)
  2. Betaxolol (drug_modules\cardiovascular\beta_blockers\selective.py)

### Cardiovascular - Calcium Channel Blocker (Non-dihydropyridine)
**Số lượng**: 2 thuốc

Danh sách:
  1. Diltiazem (drug_modules\cardiovascular\calcium_blockers\non_dihydropyridines.py)
  2. Verapamil (drug_modules\cardiovascular\calcium_blockers\non_dihydropyridines.py)

### Cardiovascular - Aldosterone Antagonist (Potassium-sparing Diuretic)
**Số lượng**: 2 thuốc

Danh sách:
  1. Eplerenone (drug_modules\cardiovascular\diuretics.py)
  2. Spironolactone (drug_modules\cardiovascular\diuretics.py)

### Cardiovascular - Thiazide-like Diuretic
**Số lượng**: 2 thuốc

Danh sách:
  1. Chlorthalidone (drug_modules\cardiovascular\diuretics.py)
  2. Indapamide (drug_modules\cardiovascular\diuretics.py)

### Cardiovascular - CCB + ARB (Fixed-Dose Combination)
**Số lượng**: 2 thuốc

Danh sách:
  1. Amlodipine/Olmesartan (drug_modules\cardiovascular\fixed_dose_combinations.py)
  2. Amlodipine/Valsartan (drug_modules\cardiovascular\fixed_dose_combinations.py)

### Cardiovascular - Central Alpha-2 Agonist
**Số lượng**: 2 thuốc

Danh sách:
  1. Clonidine (drug_modules\cardiovascular\other_cv.py)
  2. Methyldopa (drug_modules\cardiovascular\other_cv.py)

### Cardiovascular - PCSK9 Inhibitor
**Số lượng**: 2 thuốc

Danh sách:
  1. Alirocumab (drug_modules\cardiovascular\pcsk9_inhibitors.py)
  2. Evolocumab (drug_modules\cardiovascular\pcsk9_inhibitors.py)

### Cardiovascular - Fibrate (PPAR-alpha Agonist)
**Số lượng**: 2 thuốc

Danh sách:
  1. Fenofibrate (drug_modules\cardiovascular\triglyceride_lowering.py)
  2. Gemfibrozil (drug_modules\cardiovascular\triglyceride_lowering.py)

### Cardiovascular - Nitrate
**Số lượng**: 2 thuốc

Danh sách:
  1. Isosorbide mononitrate (drug_modules\cardiovascular\vasodilators.py)
  2. Nitroglycerin (drug_modules\cardiovascular\vasodilators.py)

### Cardiovascular - Antiplatelet
**Số lượng**: 2 thuốc

Danh sách:
  1. Dipyridamole (drug_modules\cardiovascular_other\antiplatelets.py)
  2. Ticlopidine (drug_modules\cardiovascular_other\antiplatelets.py)

### Dermatology - Topical Calcineurin Inhibitor
**Số lượng**: 2 thuốc

Danh sách:
  1. Pimecrolimus (drug_modules\dermatology.py)
  2. Tacrolimus topical (drug_modules\dermatology.py)

### Dermatology - Topical Antiacne/Anti-inflammatory
**Số lượng**: 2 thuốc

Danh sách:
  1. Azelaic Acid (drug_modules\dermatology.py)
  2. Azelaic acid topical (drug_modules\dermatology.py)

### Dermatology - Topical Antiparasitic
**Số lượng**: 2 thuốc

Danh sách:
  1. Ivermectin cream (drug_modules\dermatology.py)
  2. Permethrin topical (drug_modules\dermatology.py)

### Dermatology - Topical Retinoid
**Số lượng**: 2 thuốc

Danh sách:
  1. Adapalene (drug_modules\dermatology.py)
  2. Tazarotene (drug_modules\dermatology.py)

### Dermatology - Topical Vitamin D Analog
**Số lượng**: 2 thuốc

Danh sách:
  1. Calcipotriol (drug_modules\dermatology.py)
  2. Calcitriol topical (drug_modules\dermatology.py)

### Dermatology - Topical NSAID
**Số lượng**: 2 thuốc

Danh sách:
  1. Diclofenac gel (drug_modules\dermatology.py)
  2. Ketoprofen gel (drug_modules\dermatology.py)

### Dermatology - Topical Corticosteroid (High Potency)
**Số lượng**: 2 thuốc

Danh sách:
  1. Betamethasone topical (drug_modules\dermatology.py)
  2. Mometasone topical (drug_modules\dermatology.py)

### Diabetes - Alpha-Glucosidase Inhibitor
**Số lượng**: 2 thuốc

Danh sách:
  1. Acarbose (drug_modules\diabetes\alpha_glucosidase_inhibitors.py)
  2. Miglitol (drug_modules\diabetes\alpha_glucosidase_inhibitors.py)

### Diabetes - Biguanide + SGLT2 Inhibitor (Fixed-Dose Combination)
**Số lượng**: 2 thuốc

Danh sách:
  1. Metformin/Dapagliflozin (drug_modules\diabetes\fixed_dose_combinations.py)
  2. Metformin/Empagliflozin (drug_modules\diabetes\fixed_dose_combinations.py)

### Diabetes - Meglitinide (Glinide)
**Số lượng**: 2 thuốc

Danh sách:
  1. Nateglinide (drug_modules\diabetes\meglitinides.py)
  2. Repaglinide (drug_modules\diabetes\meglitinides.py)

### Diabetes - Long-Acting Insulin
**Số lượng**: 2 thuốc

Danh sách:
  1. Insulin Detemir (drug_modules\diabetes\specific_insulins.py)
  2. Insulin Glargine (drug_modules\diabetes\specific_insulins.py)

### Diabetes - Sulfonylurea
**Số lượng**: 2 thuốc

Danh sách:
  1. Glibenclamide (drug_modules\diabetes\sulfonylureas.py)
  2. Gliclazide (drug_modules\diabetes\sulfonylureas.py)

### Diabetes - Thiazolidinedione (TZD)
**Số lượng**: 2 thuốc

Danh sách:
  1. Pioglitazone (drug_modules\diabetes\thiazolidinedione_tzds.py)
  2. Rosiglitazone (drug_modules\diabetes\thiazolidinedione_tzds.py)

### Emergency - Electrolyte (Bisphosphonate)
**Số lượng**: 2 thuốc

Danh sách:
  1. Pamidronate (drug_modules\emergency\electrolytes.py)
  2. Zoledronic acid (drug_modules\emergency\electrolytes.py)

### Emergency - Electrolyte (Phosphate Supplement)
**Số lượng**: 2 thuốc

Danh sách:
  1. Potassium phosphate (drug_modules\emergency\electrolytes.py)
  2. Sodium phosphate (drug_modules\emergency\electrolytes.py)

### Emergency - Non-depolarizing Neuromuscular Blocker (Aminosteroid)
**Số lượng**: 2 thuốc

Danh sách:
  1. Rocuronium (drug_modules\emergency\neuromuscular_blockers.py)
  2. Vecuronium (drug_modules\emergency\neuromuscular_blockers.py)

### Emergency - Opioid Antagonist
**Số lượng**: 2 thuốc

Danh sách:
  1. Naloxone (drug_modules\emergency\opioid_antagonists.py)
  2. Naltrexone (drug_modules\emergency\opioid_antagonists.py)

### Gastrointestinal - Antidiarrheal
**Số lượng**: 2 thuốc

Danh sách:
  1. Bismuth subsalicylate (drug_modules\gastrointestinal\antidiarrheals.py)
  2. Loperamide (drug_modules\gastrointestinal\antidiarrheals.py)

### Gastrointestinal - JAK Inhibitor
**Số lượng**: 2 thuốc

Danh sách:
  1. Tofacitinib (drug_modules\gastrointestinal\jak_inhibitors.py)
  2. Upadacitinib (drug_modules\gastrointestinal\jak_inhibitors.py)

### Gastrointestinal - Potassium-Competitive Acid Blocker (PCAB)
**Số lượng**: 2 thuốc

Danh sách:
  1. Tegoprazan (drug_modules\gastrointestinal\pcab.py)
  2. Vonoprazan (drug_modules\gastrointestinal\pcab.py)

### Gastrointestinal - Prokinetic, Antiemetic
**Số lượng**: 2 thuốc

Danh sách:
  1. Domperidone (drug_modules\gastrointestinal\prokinetic_antiemetics.py)
  2. Metoclopramide (drug_modules\gastrointestinal\prokinetic_antiemetics.py)

### Gastrointestinal - Proton Pump Inhibitor
**Số lượng**: 2 thuốc

Danh sách:
  1. Pantoprazole (drug_modules\gastrointestinal\proton_pump_inhibitors.py)
  2. Rabeprazole (drug_modules\gastrointestinal\proton_pump_inhibitors.py)

### Antibiotic - Cephalosporin (3rd Generation, Oral)
**Số lượng**: 2 thuốc

Danh sách:
  1. Cefdinir (drug_modules\infectious_other\cephalosporins.py)
  2. Cefixime (drug_modules\infectious_other\cephalosporins.py)

### Antibiotic - Cephalosporin (2nd Generation, Cephamycin)
**Số lượng**: 2 thuốc

Danh sách:
  1. Cefotetan (drug_modules\infectious_other\cephalosporins.py)
  2. Cefoxitin (drug_modules\infectious_other\cephalosporins.py)

### Endocrinology - Antithyroid (Thionamide)
**Số lượng**: 2 thuốc

Danh sách:
  1. Methimazole (drug_modules\metabolic\antithyroid.py)
  2. Propylthiouracil (drug_modules\metabolic\antithyroid.py)

### Biological - Monoclonal Antibody (anti-CD20)
**Số lượng**: 2 thuốc

Danh sách:
  1. Ocrelizumab (drug_modules\miscellaneous\biological_drugs.py)
  2. Rituximab (drug_modules\miscellaneous\biological_drugs.py)

### Biological - Monoclonal Antibody (anti-PD-L1)
**Số lượng**: 2 thuốc

Danh sách:
  1. Atezolizumab (drug_modules\miscellaneous\biological_drugs.py)
  2. Durvalumab (drug_modules\miscellaneous\biological_drugs.py)

### Biological - Monoclonal Antibody (anti-IL-17A)
**Số lượng**: 2 thuốc

Danh sách:
  1. Ixekizumab (drug_modules\miscellaneous\biological_drugs.py)
  2. Secukinumab (drug_modules\miscellaneous\biological_drugs.py)

### Biological - Monoclonal Antibody (anti-IL-23)
**Số lượng**: 2 thuốc

Danh sách:
  1. Guselkumab (drug_modules\miscellaneous\biological_drugs.py)
  2. Risankizumab (drug_modules\miscellaneous\biological_drugs.py)

### Biological - Monoclonal Antibody (anti-IL-6R)
**Số lượng**: 2 thuốc

Danh sách:
  1. Sarilumab (drug_modules\miscellaneous\biological_drugs.py)
  2. Tocilizumab (drug_modules\miscellaneous\biological_drugs.py)

### Immunosuppressant - Calcineurin Inhibitor
**Số lượng**: 2 thuốc

Danh sách:
  1. Cyclosporine (drug_modules\miscellaneous\immunosuppressants.py)
  2. Tacrolimus (drug_modules\miscellaneous\immunosuppressants.py)

### Immunosuppressant - Antimetabolite
**Số lượng**: 2 thuốc

Danh sách:
  1. Azathioprine (drug_modules\miscellaneous\immunosuppressants.py)
  2. Mycophenolate (drug_modules\miscellaneous\immunosuppressants.py)

### Vitamins/Supplements - Vitamin D
**Số lượng**: 2 thuốc

Danh sách:
  1. Vitamin D (drug_modules\supportive\vitamin_ds.py)
  2. Vitamin D3 (Cholecalciferol) (drug_modules\miscellaneous\vitamins.py)

### Vitamins/Supplements - Calcium
**Số lượng**: 2 thuốc

Danh sách:
  1. Calcium (drug_modules\supportive\calciums.py)
  2. Calcium (elemental) (drug_modules\miscellaneous\vitamins.py)

### Neurology - Cholinesterase Inhibitor
**Số lượng**: 2 thuốc

Danh sách:
  1. Donepezil (drug_modules\neurological\alzheimer_dementia_drugs.py)
  2. Rivastigmine (drug_modules\neurological\alzheimer_dementia_drugs.py)

### Neurology - Anticonvulsant (Alpha-2-delta ligand)
**Số lượng**: 2 thuốc

Danh sách:
  1. Gabapentin (drug_modules\neurological\anticonvulsant_alpha_2_delta_ligands.py)
  2. Pregabalin (drug_modules\neurological\anticonvulsant_alpha_2_delta_ligands.py)

### Neurology - Antiparkinsonian (Dopamine Agonist)
**Số lượng**: 2 thuốc

Danh sách:
  1. Pramipexole (drug_modules\neurological\antiparkinsonian.py)
  2. Ropinirole (drug_modules\neurological\antiparkinsonian.py)

### Neurology - Movement Disorders (VMAT2 Inhibitor)
**Số lượng**: 2 thuốc

Danh sách:
  1. Deutetrabenazine (drug_modules\neurological\antiparkinsonian.py)
  2. Tetrabenazine (drug_modules\neurological\antiparkinsonian.py)

### Neurology - Anti-CGRP Receptor Antagonist (Gepant)
**Số lượng**: 2 thuốc

Danh sách:
  1. Rimegepant (drug_modules\neurological\migraine_cgrp_drugs.py)
  2. Ubrogepant (drug_modules\neurological\migraine_cgrp_drugs.py)

### Obstetrics/Gynecology - Antifungal (Vulvovaginal Candidiasis)
**Số lượng**: 2 thuốc

Danh sách:
  1. Clotrimazole (vaginal) (drug_modules\obstetrics_gynecology.py)
  2. Miconazole (vaginal) (drug_modules\obstetrics_gynecology.py)

### Oncology - Alkylating Agent
**Số lượng**: 2 thuốc

Danh sách:
  1. Cyclophosphamide (drug_modules\oncology\alkylating_agents.py)
  2. Ifosfamide (drug_modules\oncology\alkylating_agents.py)

### Oncology - Anti-emetic (5-HT3 Antagonist)
**Số lượng**: 2 thuốc

Danh sách:
  1. Granisetron (drug_modules\oncology\anti_emetic_5_ht3_antagonists.py)
  2. Palonosetron (drug_modules\oncology\anti_emetic_5_ht3_antagonists.py)

### Oncology - EGFR Tyrosine Kinase Inhibitor
**Số lượng**: 2 thuốc

Danh sách:
  1. Erlotinib (drug_modules\oncology\targeted_therapy_tkis.py)
  2. Gefitinib (drug_modules\oncology\targeted_therapy_tkis.py)

### Oncology - Taxane
**Số lượng**: 2 thuốc

Danh sách:
  1. Docetaxel (drug_modules\oncology\taxanes.py)
  2. Paclitaxel (drug_modules\oncology\taxanes.py)

### Oncology - Topoisomerase Inhibitor
**Số lượng**: 2 thuốc

Danh sách:
  1. Irinotecan (drug_modules\oncology\topoisomerase_inhibitors.py)
  2. Topotecan (drug_modules\oncology\topoisomerase_inhibitors.py)

### Ophthalmology - Carbonic Anhydrase Inhibitor (Glaucoma)
**Số lượng**: 2 thuốc

Danh sách:
  1. Brinzolamide (drug_modules\ophthalmology.py)
  2. Dorzolamide (drug_modules\ophthalmology.py)

### Ophthalmology - Corticosteroid (Anti-inflammatory)
**Số lượng**: 2 thuốc

Danh sách:
  1. Dexamethasone eye drops (drug_modules\ophthalmology.py)
  2. Prednisolone eye drops (drug_modules\ophthalmology.py)

### Ophthalmology - Antihistamine/Mast Cell Stabilizer (Allergic Conjunctivitis)
**Số lượng**: 2 thuốc

Danh sách:
  1. Ketotifen eye drops (drug_modules\ophthalmology.py)
  2. Olopatadine eye drops (drug_modules\ophthalmology.py)

### Ophthalmology - Antibiotic (Aminoglycoside)
**Số lượng**: 2 thuốc

Danh sách:
  1. Gentamicin eye drops (drug_modules\ophthalmology.py)
  2. Tobramycin eye drops (drug_modules\ophthalmology.py)

### Ophthalmology - NSAID (Anti-inflammatory)
**Số lượng**: 2 thuốc

Danh sách:
  1. Diclofenac eye drops (drug_modules\ophthalmology.py)
  2. Ketorolac eye drops (drug_modules\ophthalmology.py)

### Psychiatry - ADHD Medication (Stimulant)
**Số lượng**: 2 thuốc

Danh sách:
  1. Dextroamphetamine (drug_modules\psychiatry_other\adhd_anxiolytics.py)
  2. Methylphenidate (drug_modules\psychiatry_other\adhd_anxiolytics.py)

### Psychiatry - MAO Inhibitor (MAOI)
**Số lượng**: 2 thuốc

Danh sách:
  1. Phenelzine (drug_modules\psychiatry_other\antidepressants.py)
  2. Tranylcypromine (drug_modules\psychiatry_other\antidepressants.py)

### Psychiatry - SSRI
**Số lượng**: 2 thuốc

Danh sách:
  1. Citalopram (drug_modules\psychiatry_other\ssris.py)
  2. Escitalopram (drug_modules\psychiatry_other\ssris.py)

### Psychiatry - Tricyclic Antidepressant (TCA)
**Số lượng**: 2 thuốc

Danh sách:
  1. Amitriptyline (drug_modules\psychiatry_other\tcas.py)
  2. Clomipramine (drug_modules\psychiatry_other\tcas.py)

### Respiratory - Fixed-dose Combination (ICS/LABA)
**Số lượng**: 2 thuốc

Danh sách:
  1. Budesonide/Formoterol inhaler (drug_modules\respiratory\combination_inhalers.py)
  2. Fluticasone/Salmeterol inhaler (drug_modules\respiratory\combination_inhalers.py)

### Respiratory - Fixed-dose Combination (LAMA/LABA)
**Số lượng**: 2 thuốc

Danh sách:
  1. Tiotropium/Olodaterol inhaler (drug_modules\respiratory\combination_inhalers.py)
  2. Umeclidinium/Vilanterol inhaler (drug_modules\respiratory\combination_inhalers.py)

### Respiratory - Leukotriene Receptor Antagonist
**Số lượng**: 2 thuốc

Danh sách:
  1. Montelukast (drug_modules\respiratory\leukotriene_receptor_antagonists.py)
  2. Zafirlukast (drug_modules\respiratory\leukotriene_receptor_antagonists.py)

### Respiratory - Mast Cell Stabilizer
**Số lượng**: 2 thuốc

Danh sách:
  1. Cromolyn (drug_modules\respiratory\leukotriene_receptor_antagonists.py)
  2. Nedocromil (drug_modules\respiratory\leukotriene_receptor_antagonists.py)

### Respiratory - Methylxanthine (Bronchodilator)
**Số lượng**: 2 thuốc

Danh sách:
  1. Aminophylline (drug_modules\respiratory\methylxanthines.py)
  2. Theophylline (drug_modules\respiratory\methylxanthines.py)

### Urology - Alpha-1 Adrenergic Blocker (BPH)
**Số lượng**: 2 thuốc

Danh sách:
  1. Alfuzosin (drug_modules\urology.py)
  2. Tamsulosin (drug_modules\urology.py)

### Urology - 5-alpha Reductase Inhibitor (BPH)
**Số lượng**: 2 thuốc

Danh sách:
  1. Dutasteride (drug_modules\urology.py)
  2. Finasteride (drug_modules\urology.py)

### Analgesic/Antipyretic
**Số lượng**: 1 thuốc

Danh sách:
  1. Paracetamol (drug_modules\analgesics\analgesic_antipyretic.py)

### Analgesic - Antimigraine (5-HT1F Receptor Agonist)
**Số lượng**: 1 thuốc

Danh sách:
  1. Lasmiditan (drug_modules\analgesics\antimigraine_5_ht1_receptor_agonists.py)

### Analgesic - NSAID/Antiplatelet
**Số lượng**: 1 thuốc

Danh sách:
  1. Aspirin (drug_modules\analgesics\nsaids.py)

### Analgesic - NSAID (COX-2 Preferential)
**Số lượng**: 1 thuốc

Danh sách:
  1. Nimesulide (drug_modules\analgesics\nsaids.py)

### Analgesic - Opioid Agonist (Weak)
**Số lượng**: 1 thuốc

Danh sách:
  1. Codeine (drug_modules\analgesics\opioid_agonist_weaks.py)

### Analgesic - Opioid Partial Agonist
**Số lượng**: 1 thuốc

Danh sách:
  1. Buprenorphine (drug_modules\analgesics\opioid_agonists.py)

### Analgesic - Opioid Agonist (Dual Mechanism)
**Số lượng**: 1 thuốc

Danh sách:
  1. Tapentadol (drug_modules\analgesics\opioid_agonists.py)

### Analgesic - Combination (NSAID + Muscle Relaxant)
**Số lượng**: 1 thuốc

Danh sách:
  1. Aspirin/Carisoprodol (drug_modules\analgesics\pain_muscle_relaxant_combinations.py)

### Antibiotic - Aminoglycoside (Next Generation)
**Số lượng**: 1 thuốc

Danh sách:
  1. Plazomicin (drug_modules\antimicrobial\antibiotics\aminoglycosides.py)

### Antibiotic - Penicillin (Natural)
**Số lượng**: 1 thuốc

Danh sách:
  1. Penicillin G (drug_modules\antimicrobial\antibiotics\beta_lactams.py)

### Antibiotic - Monobactam
**Số lượng**: 1 thuốc

Danh sách:
  1. Aztreonam (drug_modules\antimicrobial\antibiotics\beta_lactams.py)

### Antibiotic - Siderophore Cephalosporin
**Số lượng**: 1 thuốc

Danh sách:
  1. Cefiderocol (drug_modules\antimicrobial\antibiotics\beta_lactams.py)

### Antibiotic - Fluoroquinolone (4th Generation)
**Số lượng**: 1 thuốc

Danh sách:
  1. Moxifloxacin (drug_modules\antimicrobial\antibiotics\fluoroquinolones.py)

### Antibiotic - Lipopeptide
**Số lượng**: 1 thuốc

Danh sách:
  1. Daptomycin (drug_modules\antimicrobial\antibiotics\glycopeptides.py)

### Antibiotic - Lincosamide
**Số lượng**: 1 thuốc

Danh sách:
  1. Clindamycin (drug_modules\antimicrobial\antibiotics\lincosamides.py)

### Antibiotic - Macrolide (Azalide)
**Số lượng**: 1 thuốc

Danh sách:
  1. Azithromycin (drug_modules\antimicrobial\antibiotics\macrolides.py)

### Antibiotic - Phosphonic Acid
**Số lượng**: 1 thuốc

Danh sách:
  1. Fosfomycin (drug_modules\antimicrobial\antibiotics\others.py)

### Antibiotic - Nitrofuran
**Số lượng**: 1 thuốc

Danh sách:
  1. Nitrofurantoin (drug_modules\antimicrobial\antibiotics\others.py)

### Antibiotic - Macrocyclic
**Số lượng**: 1 thuốc

Danh sách:
  1. Fidaxomicin (drug_modules\antimicrobial\antibiotics\others.py)

### Antibiotic - Pleuromutilin
**Số lượng**: 1 thuốc

Danh sách:
  1. Lefamulin (drug_modules\antimicrobial\antibiotics\others.py)

### Antibiotic - Oxazolidinone
**Số lượng**: 1 thuốc

Danh sách:
  1. Linezolid (drug_modules\antimicrobial\antibiotics\oxazolidinones.py)

### Antibiotic - Sulfonamide
**Số lượng**: 1 thuốc

Danh sách:
  1. Trimethoprim-sulfamethoxazole (drug_modules\antimicrobial\antibiotics\sulfonamides.py)

### Infectious Disease - Antifungal (Azole, 2nd generation)
**Số lượng**: 1 thuốc

Danh sách:
  1. Voriconazole (drug_modules\antimicrobial\antifungals\azoles.py)

### Infectious Disease - Antifungal (Azole - Triazole)
**Số lượng**: 1 thuốc

Danh sách:
  1. Posaconazole (drug_modules\antimicrobial\antifungals\azoles.py)

### Infectious Disease - Antifungal (Azole - Triazole, prodrug)
**Số lượng**: 1 thuốc

Danh sách:
  1. Isavuconazole (drug_modules\antimicrobial\antifungals\azoles.py)

### Infectious Disease - Antiviral (HBV)
**Số lượng**: 1 thuốc

Danh sách:
  1. Entecavir (drug_modules\antimicrobial\antivirals\hepatitis.py)

### Infectious Disease - Antiviral (HBV, HIV)
**Số lượng**: 1 thuốc

Danh sách:
  1. Tenofovir (drug_modules\antimicrobial\antivirals\hepatitis.py)

### Infectious Disease - Antiviral (HCV NS5B inhibitor)
**Số lượng**: 1 thuốc

Danh sách:
  1. Sofosbuvir (drug_modules\antimicrobial\antivirals\hepatitis.py)

### Infectious Disease - Antiviral (HCV NS5A inhibitor)
**Số lượng**: 1 thuốc

Danh sách:
  1. Ledipasvir (drug_modules\antimicrobial\antivirals\hepatitis.py)

### Infectious Disease - Antiviral (HCV NS5B + NS5A inhibitor FDC)
**Số lượng**: 1 thuốc

Danh sách:
  1. Sofosbuvir/Velpatasvir (drug_modules\antimicrobial\antivirals\hepatitis.py)

### Pharmacokinetic booster (CYP3A inhibitor)
**Số lượng**: 1 thuốc

Danh sách:
  1. Cobicistat (COBI) (drug_modules\antimicrobial\antivirals\hiv_arvs.py)

### Pharmacokinetic booster (CYP3A inhibitor; PI at high dose)
**Số lượng**: 1 thuốc

Danh sách:
  1. Ritonavir (low-dose booster) (drug_modules\antimicrobial\antivirals\hiv_arvs.py)

### Antiviral - Single tablet regimen (INSTI + NRTI backbone)
**Số lượng**: 1 thuốc

Danh sách:
  1. Bictegravir/Emtricitabine/Tenofovir alafenamide (BIC/FTC/TAF) (drug_modules\antimicrobial\antivirals\hiv_arvs.py)

### Antiviral - Single tablet regimen (NNRTI + NRTI backbone)
**Số lượng**: 1 thuốc

Danh sách:
  1. Efavirenz/Tenofovir disoproxil fumarate/Emtricitabine (EFV/TDF/FTC) (drug_modules\antimicrobial\antivirals\hiv_arvs.py)

### Antiviral - Long-acting INSTI + NNRTI (injectable)
**Số lượng**: 1 thuốc

Danh sách:
  1. Cabotegravir + Rilpivirine (Long-acting IM) (drug_modules\antimicrobial\antivirals\hiv_arvs.py)

### Infectious Disease - Antiviral (RNA Polymerase Inhibitor)
**Số lượng**: 1 thuốc

Danh sách:
  1. Remdesivir (drug_modules\antimicrobial\antivirals\influenza.py)

### Infectious Disease - Antiviral (RNA polymerase inhibitor)
**Số lượng**: 1 thuốc

Danh sách:
  1. Favipiravir (drug_modules\antimicrobial\antivirals\influenza.py)

### Cardiovascular - Antiarrhythmic (Class V - Purinergic Agonist)
**Số lượng**: 1 thuốc

Danh sách:
  1. Adenosine (drug_modules\cardiovascular\antiarrhythmics.py)

### Cardiovascular - Anticoagulant (Vitamin K Antagonist)
**Số lượng**: 1 thuốc

Danh sách:
  1. Warfarin (drug_modules\cardiovascular\anticoagulants.py)

### Cardiovascular - Anticoagulant (Factor Xa Inhibitor)
**Số lượng**: 1 thuốc

Danh sách:
  1. Fondaparinux (drug_modules\cardiovascular\anticoagulants.py)

### Cardiovascular - Anticoagulant (Low Molecular Weight Heparin)
**Số lượng**: 1 thuốc

Danh sách:
  1. Enoxaparin (drug_modules\cardiovascular\anticoagulants.py)

### Cardiovascular - Anticoagulant (Direct Thrombin Inhibitor - DOAC)
**Số lượng**: 1 thuốc

Danh sách:
  1. Dabigatran (drug_modules\cardiovascular\anticoagulants.py)

### Cardiovascular - Beta-blocker (Non-selective with Alpha-blocking)
**Số lượng**: 1 thuốc

Danh sách:
  1. Carvedilol (drug_modules\cardiovascular\beta_blockers\non_selective.py)

### Cardiovascular - Beta-blocker
**Số lượng**: 1 thuốc

Danh sách:
  1. Metoprolol (drug_modules\cardiovascular\beta_blockers\selective.py)

### Cardiovascular - Beta-blocker (Selective - Beta-1)
**Số lượng**: 1 thuốc

Danh sách:
  1. Nebivolol (drug_modules\cardiovascular\beta_blockers\selective.py)

### Cardiovascular - Calcium Channel Blocker (Dihydropyridine, IV)
**Số lượng**: 1 thuốc

Danh sách:
  1. Clevidipine (drug_modules\cardiovascular\calcium_blockers\dihydropyridines.py)

### Cardiovascular - Cholesterol Absorption Inhibitor
**Số lượng**: 1 thuốc

Danh sách:
  1. Ezetimibe (drug_modules\cardiovascular\cholesterol_absorption_inhibitors.py)

### Cardiovascular - ATP-Citrate Lyase Inhibitor
**Số lượng**: 1 thuốc

Danh sách:
  1. Bempedoic acid (drug_modules\cardiovascular\cholesterol_absorption_inhibitors.py)

### Cardiovascular - Thiazide Diuretic
**Số lượng**: 1 thuốc

Danh sách:
  1. Hydrochlorothiazide (drug_modules\cardiovascular\diuretics.py)

### Cardiovascular - ACE Inhibitor + Diuretic (Fixed-Dose Combination)
**Số lượng**: 1 thuốc

Danh sách:
  1. Lisinopril/Hydrochlorothiazide (drug_modules\cardiovascular\fixed_dose_combinations.py)

### Cardiovascular - ARB + Diuretic (Fixed-Dose Combination)
**Số lượng**: 1 thuốc

Danh sách:
  1. Losartan/Hydrochlorothiazide (drug_modules\cardiovascular\fixed_dose_combinations.py)

### Cardiovascular - Cardiac Glycoside
**Số lượng**: 1 thuốc

Danh sách:
  1. Digoxin (drug_modules\cardiovascular\other_cv.py)

### Cardiovascular - Alpha-Beta Blocker
**Số lượng**: 1 thuốc

Danh sách:
  1. Labetalol (drug_modules\cardiovascular\other_cv.py)

### Cardiovascular - If Channel Inhibitor
**Số lượng**: 1 thuốc

Danh sách:
  1. Ivabradine (drug_modules\cardiovascular\other_cv.py)

### Cardiovascular - ARNI (Angiotensin Receptor-Neprilysin Inhibitor)
**Số lượng**: 1 thuốc

Danh sách:
  1. Sacubitril-valsartan (drug_modules\cardiovascular\other_cv.py)

### Cardiovascular - Soluble Guanylate Cyclase (sGC) Stimulator
**Số lượng**: 1 thuốc

Danh sách:
  1. Vericiguat (drug_modules\cardiovascular\other_cv.py)

### Cardiovascular/Diabetes - Dual SGLT1/2 Inhibitor
**Số lượng**: 1 thuốc

Danh sách:
  1. Sotagliflozin (drug_modules\cardiovascular\other_cv.py)

### Cardiovascular/Metabolic - Nonsteroidal MRA
**Số lượng**: 1 thuốc

Danh sách:
  1. Finerenone (drug_modules\cardiovascular\other_cv.py)

### Cardiovascular - Alpha-1 Blocker
**Số lượng**: 1 thuốc

Danh sách:
  1. Doxazosin (drug_modules\cardiovascular\other_cv.py)

### Cardiovascular - PCSK9 Inhibitor (siRNA)
**Số lượng**: 1 thuốc

Danh sách:
  1. Inclisiran (drug_modules\cardiovascular\pcsk9_inhibitors.py)

### Cardiovascular - Statin
**Số lượng**: 1 thuốc

Danh sách:
  1. Simvastatin (drug_modules\cardiovascular\statins.py)

### Cardiovascular - Omega-3 Fatty Acid (EPA Ethyl Ester)
**Số lượng**: 1 thuốc

Danh sách:
  1. Icosapent ethyl (drug_modules\cardiovascular\triglyceride_lowering.py)

### Cardiovascular - Selective PPAR-alpha Modulator (Fibrate)
**Số lượng**: 1 thuốc

Danh sách:
  1. Pemafibrate (drug_modules\cardiovascular\triglyceride_lowering.py)

### Cardiovascular - Omega-3 Fatty Acids (EPA/DHA)
**Số lượng**: 1 thuốc

Danh sách:
  1. Omega-3 acid ethyl esters (drug_modules\cardiovascular\triglyceride_lowering.py)

### Cardiovascular - Vitamin B3 / Lipid-lowering Agent
**Số lượng**: 1 thuốc

Danh sách:
  1. Niacin (drug_modules\cardiovascular\triglyceride_lowering.py)

### Cardiovascular - ANGPTL3 Inhibitor (Monoclonal Antibody)
**Số lượng**: 1 thuốc

Danh sách:
  1. Evinacumab (drug_modules\cardiovascular\triglyceride_lowering.py)

### Cardiovascular - Apo C-III Inhibitor (RNA Interference)
**Số lượng**: 1 thuốc

Danh sách:
  1. Plozasiran (drug_modules\cardiovascular\triglyceride_lowering.py)

### Cardiovascular - Direct Vasodilator
**Số lượng**: 1 thuốc

Danh sách:
  1. Hydralazine (drug_modules\cardiovascular\vasodilators.py)

### Cardiovascular - Natriuretic Peptide (Vasodilator)
**Số lượng**: 1 thuốc

Danh sách:
  1. Nesiritide (drug_modules\cardiovascular\vasodilators.py)

### Cardiovascular - Vasodilator (Hypertensive Emergency)
**Số lượng**: 1 thuốc

Danh sách:
  1. Nitroprusside (drug_modules\cardiovascular\vasodilators.py)

### Cardiovascular - ACE Inhibitor (IV)
**Số lượng**: 1 thuốc

Danh sách:
  1. Enalaprilat (drug_modules\cardiovascular_other\ace_inhibitors_iv.py)

### Cardiovascular - Statin (high-intensity, secondary prevention stroke/TIA)
**Số lượng**: 1 thuốc

Danh sách:
  1. High-intensity statin (đột quỵ/TIA) (drug_modules\cardiovascular_other\statins.py)

### Dermatology - Topical Corticosteroid (Ultra-high Potency)
**Số lượng**: 1 thuốc

Danh sách:
  1. Clobetasol (drug_modules\dermatology.py)

### Dermatology - Topical Corticosteroid (Low Potency)
**Số lượng**: 1 thuốc

Danh sách:
  1. Hydrocortisone topical (drug_modules\dermatology.py)

### Dermatology - Topical Combination (Corticosteroid + Antifungal)
**Số lượng**: 1 thuốc

Danh sách:
  1. Betamethasone/Clotrimazole topical (drug_modules\dermatology.py)

### Dermatology - Topical Combination (Antibiotic + Corticosteroid)
**Số lượng**: 1 thuốc

Danh sách:
  1. Fusidic acid/Betamethasone topical (drug_modules\dermatology.py)

### Dermatology - Topical Combination (Antifungal + Low-potency Corticosteroid)
**Số lượng**: 1 thuốc

Danh sách:
  1. Miconazole/Hydrocortisone topical (drug_modules\dermatology.py)

### Dermatology - Topical Combination (Antibiotic + Corticosteroid + Antifungal)
**Số lượng**: 1 thuốc

Danh sách:
  1. Gentamicin/Betamethasone/Clotrimazole topical (drug_modules\dermatology.py)

### Dermatology - Topical Retinoid (Acne)
**Số lượng**: 1 thuốc

Danh sách:
  1. Tretinoin topical (drug_modules\dermatology.py)

### Dermatology - Topical Antiseptic (Acne)
**Số lượng**: 1 thuốc

Danh sách:
  1. Benzoyl peroxide topical (drug_modules\dermatology.py)

### Dermatology - Topical Corticosteroid (Medium Potency)
**Số lượng**: 1 thuốc

Danh sách:
  1. Triamcinolone topical (drug_modules\dermatology.py)

### Dermatology - Topical Antibiotic (Rosacea)
**Số lượng**: 1 thuốc

Danh sách:
  1. Metronidazole topical (drug_modules\dermatology.py)

### Dermatology - Topical Keratolytic
**Số lượng**: 1 thuốc

Danh sách:
  1. Salicylic Acid (drug_modules\dermatology.py)

### Diabetes - Biguanide
**Số lượng**: 1 thuốc

Danh sách:
  1. Metformin (drug_modules\diabetes\biguanides.py)

### Diabetes - Biguanide + DPP-4 Inhibitor (Fixed-Dose Combination)
**Số lượng**: 1 thuốc

Danh sách:
  1. Metformin/Sitagliptin (drug_modules\diabetes\fixed_dose_combinations.py)

### Diabetes - Biguanide + Sulfonylurea (Fixed-Dose Combination)
**Số lượng**: 1 thuốc

Danh sách:
  1. Metformin/Glibenclamide (drug_modules\diabetes\fixed_dose_combinations.py)

### Diabetes - Biguanide + Thiazolidinedione (Fixed-Dose Combination)
**Số lượng**: 1 thuốc

Danh sách:
  1. Metformin/Pioglitazone (drug_modules\diabetes\fixed_dose_combinations.py)

### Diabetes - GIP/GLP-1 Dual Agonist
**Số lượng**: 1 thuốc

Danh sách:
  1. Tirzepatide (drug_modules\diabetes\glp1_agonists.py)

### Diabetes - Insulin
**Số lượng**: 1 thuốc

Danh sách:
  1. Insulin (drug_modules\diabetes\insulins.py)

### Diabetes - Dopamine Agonist
**Số lượng**: 1 thuốc

Danh sách:
  1. Bromocriptine (drug_modules\diabetes\other_antidiabetics.py)

### Diabetes - Bile Acid Sequestrant
**Số lượng**: 1 thuốc

Danh sách:
  1. Colesevelam (drug_modules\diabetes\other_antidiabetics.py)

### Diabetes - Short-Acting Insulin
**Số lượng**: 1 thuốc

Danh sách:
  1. Insulin Regular (drug_modules\diabetes\specific_insulins.py)

### Diabetes - Intermediate-Acting Insulin
**Số lượng**: 1 thuốc

Danh sách:
  1. Insulin NPH (drug_modules\diabetes\specific_insulins.py)

### Diabetes - Ultra-Long-Acting Insulin
**Số lượng**: 1 thuốc

Danh sách:
  1. Insulin Degludec (drug_modules\diabetes\specific_insulins.py)

### Diabetes - Sulfonylurea (3rd Generation)
**Số lượng**: 1 thuốc

Danh sách:
  1. Glimepiride (drug_modules\diabetes\sulfonylureas.py)

### Diabetes - T1DM Prevention (anti-CD3 Monoclonal Antibody)
**Số lượng**: 1 thuốc

Danh sách:
  1. Teplizumab (drug_modules\diabetes\t1dm_prevention.py)

### Emergency - Anticholinergic
**Số lượng**: 1 thuốc

Danh sách:
  1. Atropine (drug_modules\emergency\anticholinergics.py)

### Emergency - Benzodiazepine Antagonist
**Số lượng**: 1 thuốc

Danh sách:
  1. Flumazenil (drug_modules\emergency\benzodiazepine_antagonists.py)

### Emergency - Vasopressor (Non-catecholamine)
**Số lượng**: 1 thuốc

Danh sách:
  1. Vasopressin (drug_modules\emergency\catecholamine_alpha__beta_agonists.py)

### Emergency - Alpha-1 Adrenergic Agonist (Pure)
**Số lượng**: 1 thuốc

Danh sách:
  1. Phenylephrine (drug_modules\emergency\catecholamine_alpha__beta_agonists.py)

### Emergency - Phosphodiesterase-3 Inhibitor (Inotrope)
**Số lượng**: 1 thuốc

Danh sách:
  1. Milrinone (drug_modules\emergency\catecholamine_alpha__beta_agonists.py)

### Emergency - Electrolyte (Potassium Binder)
**Số lượng**: 1 thuốc

Danh sách:
  1. Sodium polystyrene sulfonate (drug_modules\emergency\electrolytes.py)

### Emergency - Electrolyte (Magnesium Supplement)
**Số lượng**: 1 thuốc

Danh sách:
  1. Magnesium oxide (drug_modules\emergency\electrolytes.py)

### Emergency - Electrolyte (Tetracycline Antibiotic)
**Số lượng**: 1 thuốc

Danh sách:
  1. Demeclocycline (drug_modules\emergency\electrolytes.py)

### Emergency - Local Anesthetic / Antiarrhythmic (Class IB)
**Số lượng**: 1 thuốc

Danh sách:
  1. Lidocaine (drug_modules\emergency\local_anesthetic__antiarrhythmic_class_ibs.py)

### Emergency - Depolarizing Neuromuscular Blocker
**Số lượng**: 1 thuốc

Danh sách:
  1. Succinylcholine (drug_modules\emergency\neuromuscular_blockers.py)

### Emergency - Non-depolarizing Neuromuscular Blocker (Benzylisoquinolinium)
**Số lượng**: 1 thuốc

Danh sách:
  1. Cisatracurium (drug_modules\emergency\neuromuscular_blockers.py)

### Emergency - Obstetric uterotonic (PPH prevention/treatment)
**Số lượng**: 1 thuốc

Danh sách:
  1. Oxytocin (drug_modules\emergency\uterotonics.py)

### Emergency - Obstetric uterotonic (Ergot alkaloid)
**Số lượng**: 1 thuốc

Danh sách:
  1. Methylergonovine (drug_modules\emergency\uterotonics.py)

### Emergency - Obstetric uterotonic (Prostaglandin F2-alpha)
**Số lượng**: 1 thuốc

Danh sách:
  1. Carboprost (drug_modules\emergency\uterotonics.py)

### Emergency - Obstetric (Prostaglandin E2, Cervical ripening)
**Số lượng**: 1 thuốc

Danh sách:
  1. Dinoprostone (drug_modules\emergency\uterotonics.py)

### Endocrinology - Mineralocorticoid
**Số lượng**: 1 thuốc

Danh sách:
  1. Fludrocortisone (drug_modules\endocrinology_other\corticosteroids\short_intermediate_acting.py)

### Endocrinology - RANKL Inhibitor (Osteoporosis)
**Số lượng**: 1 thuốc

Danh sách:
  1. Denosumab (drug_modules\endocrinology_other\osteoporosis_other.py)

### Endocrinology - PTH Analog (Osteoporosis - Anabolic)
**Số lượng**: 1 thuốc

Danh sách:
  1. Teriparatide (drug_modules\endocrinology_other\osteoporosis_other.py)

### Endocrinology - PTHrP Analog (Osteoporosis - Anabolic)
**Số lượng**: 1 thuốc

Danh sách:
  1. Abaloparatide (drug_modules\endocrinology_other\osteoporosis_other.py)

### Endocrinology - Sclerostin Inhibitor (Osteoporosis - Anabolic)
**Số lượng**: 1 thuốc

Danh sách:
  1. Romosozumab (drug_modules\endocrinology_other\osteoporosis_other.py)

### Endocrinology - SERM (Selective Estrogen Receptor Modulator)
**Số lượng**: 1 thuốc

Danh sách:
  1. Raloxifene (drug_modules\endocrinology_other\osteoporosis_other.py)

### Endocrinology - Calcitonin (Osteoporosis, Hypercalcemia)
**Số lượng**: 1 thuốc

Danh sách:
  1. Calcitonin (drug_modules\endocrinology_other\osteoporosis_other.py)

### Endocrinology - Androgen (Sex Hormone)
**Số lượng**: 1 thuốc

Danh sách:
  1. Testosterone (drug_modules\endocrinology_other\sex_hormones.py)

### ENT - Combination (Intranasal Antihistamine + Corticosteroid)
**Số lượng**: 1 thuốc

Danh sách:
  1. Azelastine/Fluticasone nasal spray (drug_modules\ent_oral_nasal_combinations.py)

### Gastrointestinal - Antacid (Aluminum/Magnesium hydroxide combination)
**Số lượng**: 1 thuốc

Danh sách:
  1. Aluminum hydroxide/Magnesium hydroxide (drug_modules\gastrointestinal\antacids.py)

### Gastrointestinal - Antacid (Calcium carbonate)
**Số lượng**: 1 thuốc

Danh sách:
  1. Calcium carbonate (drug_modules\gastrointestinal\antacids.py)

### Gastrointestinal - Antiemetic (5-HT3 Antagonist)
**Số lượng**: 1 thuốc

Danh sách:
  1. Ondansetron (drug_modules\gastrointestinal\antiemetic_5_ht3_antagonists.py)

### Gastrointestinal - Antiflatulent (Chống đầy hơi, chống sủi bọt)
**Số lượng**: 1 thuốc

Danh sách:
  1. Simethicone (drug_modules\gastrointestinal\antiflatulents.py)

### Gastrointestinal - Antispasmodic (Direct smooth muscle relaxant)
**Số lượng**: 1 thuốc

Danh sách:
  1. Mebeverine (drug_modules\gastrointestinal\antispasmodics.py)

### Gastrointestinal - Antispasmodic & Motility Modulator
**Số lượng**: 1 thuốc

Danh sách:
  1. Trimebutine (drug_modules\gastrointestinal\antispasmodics.py)

### Gastrointestinal - Antispasmodic (Anticholinergic)
**Số lượng**: 1 thuốc

Danh sách:
  1. Hyoscine butylbromide (drug_modules\gastrointestinal\antispasmodics.py)

### Gastrointestinal - 5-ASA (Aminosalicylate)
**Số lượng**: 1 thuốc

Danh sách:
  1. Mesalazine (drug_modules\gastrointestinal\ibd_5asa.py)

### Gastrointestinal - 5-ASA (Aminosalicylate prodrug) + Sulfonamide
**Số lượng**: 1 thuốc

Danh sách:
  1. Sulfasalazine (drug_modules\gastrointestinal\ibd_5asa.py)

### Rheumatology/Gastrointestinal - JAK Inhibitor (JAK1/JAK2)
**Số lượng**: 1 thuốc

Danh sách:
  1. Baricitinib (drug_modules\gastrointestinal\jak_inhibitors.py)

### Gastrointestinal - Osmotic Laxative (Disaccharide)
**Số lượng**: 1 thuốc

Danh sách:
  1. Lactulose (drug_modules\gastrointestinal\laxatives.py)

### Gastrointestinal - Osmotic Laxative (PEG 3350)
**Số lượng**: 1 thuốc

Danh sách:
  1. Polyethylene glycol 3350 (drug_modules\gastrointestinal\laxatives.py)

### Gastrointestinal - Stimulant Laxative (Diphenylmethane)
**Số lượng**: 1 thuốc

Danh sách:
  1. Bisacodyl (drug_modules\gastrointestinal\laxatives.py)

### Gastrointestinal - Stimulant Laxative (Anthraquinone)
**Số lượng**: 1 thuốc

Danh sách:
  1. Senna (sennosides) (drug_modules\gastrointestinal\laxatives.py)

### Gastrointestinal - Mucosal Protectant
**Số lượng**: 1 thuốc

Danh sách:
  1. Sucralfate (drug_modules\gastrointestinal\mucosal_protectants.py)

### Gastrointestinal - Prostaglandin E1 Analog
**Số lượng**: 1 thuốc

Danh sách:
  1. Misoprostol (drug_modules\gastrointestinal\mucosal_protectants.py)

### Gastrointestinal - Proton Pump Inhibitor (PPI) - Dual delayed release
**Số lượng**: 1 thuốc

Danh sách:
  1. Dexlansoprazole (drug_modules\gastrointestinal\proton_pump_inhibitor_ppis.py)

### Hematology - Anticoagulant (Unfractionated Heparin)
**Số lượng**: 1 thuốc

Danh sách:
  1. Heparin (drug_modules\hematology.py)

### Hematology - Anticoagulant Reversal Agent
**Số lượng**: 1 thuốc

Danh sách:
  1. Protamine (drug_modules\hematology.py)

### Hematology - Anticoagulant Reversal Agent / Vitamin
**Số lượng**: 1 thuốc

Danh sách:
  1. Vitamin K (drug_modules\hematology.py)

### Hematology - Antifibrinolytic Agent
**Số lượng**: 1 thuốc

Danh sách:
  1. Tranexamic acid (drug_modules\hematology.py)

### Hematology - Thrombolytic (tPA)
**Số lượng**: 1 thuốc

Danh sách:
  1. Alteplase (drug_modules\hematology.py)

### Hematology - Fibrin-specific thrombolytic (tPA variant)
**Số lượng**: 1 thuốc

Danh sách:
  1. Tenecteplase (drug_modules\hematology.py)

### Hematology - Erythropoiesis-Stimulating Agent (ESA)
**Số lượng**: 1 thuốc

Danh sách:
  1. Epoetin alfa (drug_modules\hematology.py)

### Hematology - G-CSF (Granulocyte Colony-Stimulating Factor)
**Số lượng**: 1 thuốc

Danh sách:
  1. Filgrastim (drug_modules\hematology.py)

### Hematology - Bispecific Monoclonal Antibody
**Số lượng**: 1 thuốc

Danh sách:
  1. Emicizumab (drug_modules\hematology.py)

### Hematology - TPO Receptor Agonist
**Số lượng**: 1 thuốc

Danh sách:
  1. Eltrombopag (drug_modules\hematology.py)

### Hematology - TPO Mimetic
**Số lượng**: 1 thuốc

Danh sách:
  1. Romiplostim (drug_modules\hematology.py)

### Hematology - DOAC Reversal Agent (Dabigatran)
**Số lượng**: 1 thuốc

Danh sách:
  1. Idarucizumab (drug_modules\hematology.py)

### Hematology - DOAC Reversal Agent (Factor Xa Inhibitors)
**Số lượng**: 1 thuốc

Danh sách:
  1. Andexanet alfa (drug_modules\hematology.py)

### Infectious Disease - Antimalarial
**Số lượng**: 1 thuốc

Danh sách:
  1. Chloroquine (drug_modules\infectious_other\antimalarials.py)

### Infectious Disease - Antimalarial (Artemisinin)
**Số lượng**: 1 thuốc

Danh sách:
  1. Artesunate (drug_modules\infectious_other\antimalarials.py)

### Infectious Disease - Antimalarial (ACT)
**Số lượng**: 1 thuốc

Danh sách:
  1. Artemether-lumefantrine (drug_modules\infectious_other\antimalarials.py)

### Infectious Disease - Antimalarial/Antirheumatic
**Số lượng**: 1 thuốc

Danh sách:
  1. Hydroxychloroquine (drug_modules\infectious_other\antimalarials.py)

### Infectious Disease - Antimalarial (8-aminoquinoline)
**Số lượng**: 1 thuốc

Danh sách:
  1. Primaquine (drug_modules\infectious_other\antimalarials.py)

### Infectious Disease - Antitubercular (First-line, Rifamycin)
**Số lượng**: 1 thuốc

Danh sách:
  1. Rifampin (drug_modules\infectious_other\antituberculars.py)

### Infectious Disease - Antitubercular (Injectable aminoglycoside, second-line in many regimens)
**Số lượng**: 1 thuốc

Danh sách:
  1. Streptomycin (drug_modules\infectious_other\antituberculars.py)

### Infectious Disease - Antitubercular (Rifamycin, dùng trong HIV/TB và các phác đồ đặc biệt)
**Số lượng**: 1 thuốc

Danh sách:
  1. Rifabutin (drug_modules\infectious_other\antituberculars.py)

### Infectious Disease - Antitubercular (Long-acting rifamycin)
**Số lượng**: 1 thuốc

Danh sách:
  1. Rifapentine (drug_modules\infectious_other\antituberculars.py)

### Infectious Disease - Oxazolidinone (Second-line antitubercular, MDR/XDR-TB)
**Số lượng**: 1 thuốc

Danh sách:
  1. Linezolid (lao MDR/XDR) (drug_modules\infectious_other\antituberculars.py)

### Infectious Disease - Riminophenazine dye (Second-line antitubercular, MDR-TB; leprosy drug)
**Số lượng**: 1 thuốc

Danh sách:
  1. Clofazimine (drug_modules\infectious_other\antituberculars.py)

### Infectious Disease - Diarylquinoline (Group A second-line antitubercular for MDR/XDR-TB)
**Số lượng**: 1 thuốc

Danh sách:
  1. Bedaquiline (drug_modules\infectious_other\antituberculars.py)

### Infectious Disease - Nitroimidazole (Group C second-line antitubercular for MDR/XDR-TB)
**Số lượng**: 1 thuốc

Danh sách:
  1. Delamanid (drug_modules\infectious_other\antituberculars.py)

### Infectious Disease - Second-line antitubercular (D-alanine analog, MDR-TB)
**Số lượng**: 1 thuốc

Danh sách:
  1. Cycloserine / Terizidone (drug_modules\infectious_other\antituberculars.py)

### Infectious Disease - Second-line antitubercular (folate antagonist, MDR-TB)
**Số lượng**: 1 thuốc

Danh sách:
  1. PAS (para-aminosalicylic acid) (drug_modules\infectious_other\antituberculars.py)

### Antibiotic - Beta-lactam (Penicillin)
**Số lượng**: 1 thuốc

Danh sách:
  1. Amoxicillin suspension (drug_modules\infectious_other\beta_lactams.py)

### Antibiotic - Beta-lactam (Penicillin, Oral)
**Số lượng**: 1 thuốc

Danh sách:
  1. Penicillin V (drug_modules\infectious_other\beta_lactams.py)

### Antibiotic - Beta-lactam (Penicillinase-resistant Penicillin)
**Số lượng**: 1 thuốc

Danh sách:
  1. Dicloxacillin (drug_modules\infectious_other\beta_lactams.py)

### Antibiotic - Cephalosporin (2nd Generation)
**Số lượng**: 1 thuốc

Danh sách:
  1. Cefuroxime (drug_modules\infectious_other\cephalosporins.py)

### Antibiotic - Cephalosporin (2nd Generation, Oral)
**Số lượng**: 1 thuốc

Danh sách:
  1. Cefaclor (drug_modules\infectious_other\cephalosporins.py)

### Antibiotic - Cephalosporin (1st Generation, Oral)
**Số lượng**: 1 thuốc

Danh sách:
  1. Cefadroxil (drug_modules\infectious_other\cephalosporins.py)

### Infectious Disease - Nitroimidazole Antibiotic
**Số lượng**: 1 thuốc

Danh sách:
  1. Metronidazole (drug_modules\infectious_other\nitroimidazoles.py)

### Antibiotic - Glycylcycline (Tetracycline derivative)
**Số lượng**: 1 thuốc

Danh sách:
  1. Tigecycline (drug_modules\infectious_other\tetracyclines.py)

### Endocrinology - Corticosteroid (Glucocorticoid)
**Số lượng**: 1 thuốc

Danh sách:
  1. Prednisone (drug_modules\metabolic\corticosteroids.py)

### Endocrinology - Thyroid Hormone
**Số lượng**: 1 thuốc

Danh sách:
  1. Levothyroxine (drug_modules\metabolic\thyroid_hormones.py)

### Respiratory - Beta-2 Agonist (Short-acting)
**Số lượng**: 1 thuốc

Danh sách:
  1. Salbutamol (drug_modules\miscellaneous\beta_2_agonist_short_actings.py)

### Biological - Monoclonal Antibody (anti-HER2)
**Số lượng**: 1 thuốc

Danh sách:
  1. Trastuzumab (drug_modules\miscellaneous\biological_drugs.py)

### Biological - Monoclonal Antibody (anti-VEGF)
**Số lượng**: 1 thuốc

Danh sách:
  1. Bevacizumab (drug_modules\miscellaneous\biological_drugs.py)

### Biological - Fusion Protein (TNF receptor)
**Số lượng**: 1 thuốc

Danh sách:
  1. Etanercept (drug_modules\miscellaneous\biological_drugs.py)

### Biological - Monoclonal Antibody (anti-TNF-α, pegylated)
**Số lượng**: 1 thuốc

Danh sách:
  1. Certolizumab pegol (drug_modules\miscellaneous\biological_drugs.py)

### Biological - Monoclonal Antibody (anti-IL-12/23)
**Số lượng**: 1 thuốc

Danh sách:
  1. Ustekinumab (drug_modules\miscellaneous\biological_drugs.py)

### Biological - Monoclonal Antibody (anti-IL-17RA)
**Số lượng**: 1 thuốc

Danh sách:
  1. Brodalumab (drug_modules\miscellaneous\biological_drugs.py)

### Biological - Monoclonal Antibody (anti-C5)
**Số lượng**: 1 thuốc

Danh sách:
  1. Eculizumab (drug_modules\miscellaneous\biological_drugs.py)

### Biological - Monoclonal Antibody (anti-integrin α4β7)
**Số lượng**: 1 thuốc

Danh sách:
  1. Vedolizumab (drug_modules\miscellaneous\biological_drugs.py)

### Biological - Monoclonal Antibody (anti-integrin α4)
**Số lượng**: 1 thuốc

Danh sách:
  1. Natalizumab (drug_modules\miscellaneous\biological_drugs.py)

### Biological - Monoclonal Antibody (anti-CD52)
**Số lượng**: 1 thuốc

Danh sách:
  1. Alemtuzumab (drug_modules\miscellaneous\biological_drugs.py)

### Biological - Monoclonal Antibody (anti-BAFF)
**Số lượng**: 1 thuốc

Danh sách:
  1. Belimumab (drug_modules\miscellaneous\biological_drugs.py)

### Biological - Monoclonal Antibody (anti-IFN-α receptor)
**Số lượng**: 1 thuốc

Danh sách:
  1. Anifrolumab (drug_modules\miscellaneous\biological_drugs.py)

### Biological - Monoclonal Antibody (anti-TSLP)
**Số lượng**: 1 thuốc

Danh sách:
  1. Tezepelumab (drug_modules\miscellaneous\biological_drugs.py)

### Biological - Monoclonal Antibody (anti-IL-5)
**Số lượng**: 1 thuốc

Danh sách:
  1. Reslizumab (drug_modules\miscellaneous\biological_drugs.py)

### Biological - FcRn Blocker (anti-FcRn)
**Số lượng**: 1 thuốc

Danh sách:
  1. Efgartigimod (drug_modules\miscellaneous\biological_drugs.py)

### Biological - Monoclonal Antibody (anti-C5 Complement)
**Số lượng**: 1 thuốc

Danh sách:
  1. Ravulizumab (drug_modules\miscellaneous\biological_drugs.py)

### Biological - Nanobody (anti-vWF)
**Số lượng**: 1 thuốc

Danh sách:
  1. Caplacizumab (drug_modules\miscellaneous\biological_drugs.py)

### Biological - Monoclonal Antibody (anti-plasma kallikrein)
**Số lượng**: 1 thuốc

Danh sách:
  1. Lanadelumab (drug_modules\miscellaneous\biological_drugs.py)

### Respiratory - Corticosteroid (Inhaled)
**Số lượng**: 1 thuốc

Danh sách:
  1. Budesonide (drug_modules\miscellaneous\corticosteroid_inhaleds.py)

### Rheumatology - Conventional DMARD (Antimetabolite, Folic Acid Antagonist)
**Số lượng**: 1 thuốc

Danh sách:
  1. Methotrexate (drug_modules\miscellaneous\dmards_rheumatology.py)

### Rheumatology - Conventional DMARD (Pyrimidine Synthesis Inhibitor)
**Số lượng**: 1 thuốc

Danh sách:
  1. Leflunomide (drug_modules\miscellaneous\dmards_rheumatology.py)

### Metabolism - Gout Medication (Anti-inflammatory)
**Số lượng**: 1 thuốc

Danh sách:
  1. Colchicine (drug_modules\miscellaneous\gout_medications.py)

### Metabolism - Gout Medication (Uricosuric Agent)
**Số lượng**: 1 thuốc

Danh sách:
  1. Probenecid (drug_modules\miscellaneous\gout_medications.py)

### Metabolism - Gout Medication (Xanthine Oxidase Inhibitor)
**Số lượng**: 1 thuốc

Danh sách:
  1. Febuxostat (drug_modules\miscellaneous\gout_medications.py)

### Hematology - Vitamin
**Số lượng**: 1 thuốc

Danh sách:
  1. Folic Acid (drug_modules\miscellaneous\vitamins.py)

### Vitamins/Supplements - Vitamin C
**Số lượng**: 1 thuốc

Danh sách:
  1. Vitamin C (drug_modules\miscellaneous\vitamins.py)

### Vitamins/Supplements - Vitamin E
**Số lượng**: 1 thuốc

Danh sách:
  1. Vitamin E (drug_modules\miscellaneous\vitamins.py)

### Metabolism - Xanthine Oxidase Inhibitor
**Số lượng**: 1 thuốc

Danh sách:
  1. Allopurinol (drug_modules\miscellaneous\xanthine_oxidase_inhibitors.py)

### Neurology - NMDA Receptor Antagonist
**Số lượng**: 1 thuốc

Danh sách:
  1. Memantine (drug_modules\neurological\alzheimer_dementia_drugs.py)

### Neurology - Anticonvulsant (Phenytoin Prodrug)
**Số lượng**: 1 thuốc

Danh sách:
  1. Fosphenytoin (drug_modules\neurological\anticonvulsants.py)

### Neurology - Antiparkinsonian (Dopamine Precursor + DOPA Decarboxylase Inhibitor)
**Số lượng**: 1 thuốc

Danh sách:
  1. Levodopa/Carbidopa (drug_modules\neurological\antiparkinsonian.py)

### Neurology - Antiparkinsonian (5-HT2A Inverse Agonist)
**Số lượng**: 1 thuốc

Danh sách:
  1. Pimavanserin (drug_modules\neurological\antiparkinsonian.py)

### Neurology - Antiparkinsonian (MAO-B Inhibitor + Glutamate Release Inhibitor)
**Số lượng**: 1 thuốc

Danh sách:
  1. Safinamide (drug_modules\neurological\antiparkinsonian.py)

### Neurology - Antiparkinsonian (COMT Inhibitor)
**Số lượng**: 1 thuốc

Danh sách:
  1. Opicapone (drug_modules\neurological\antiparkinsonian.py)

### Neurology - Antiparkinsonian (Adenosine A2A Receptor Antagonist)
**Số lượng**: 1 thuốc

Danh sách:
  1. Istradefylline (drug_modules\neurological\antiparkinsonian.py)

### Neurology - Nootropic / Cerebral circulation enhancer
**Số lượng**: 1 thuốc

Danh sách:
  1. Piracetam (drug_modules\neurological\cerebral_circulation.py)

### Neurology - Neuroprotective / Nootropic
**Số lượng**: 1 thuốc

Danh sách:
  1. Citicoline (drug_modules\neurological\cerebral_circulation.py)

### Neurology - Cerebral vasodilator (controversial evidence)
**Số lượng**: 1 thuốc

Danh sách:
  1. Vinpocetine (drug_modules\neurological\cerebral_circulation.py)

### Neurology - Herbal cerebral vasomodulator (Ginkgo biloba)
**Số lượng**: 1 thuốc

Danh sách:
  1. Ginkgo biloba extract (drug_modules\neurological\cerebral_circulation.py)

### Neurology - Neuropeptide preparation (Stroke adjunct / Neurorecovery, controversial evidence)
**Số lượng**: 1 thuốc

Danh sách:
  1. Cerebrolysin (drug_modules\neurological\cerebral_circulation.py)

### Neurology - Ergot-derived cerebral vasodilator
**Số lượng**: 1 thuốc

Danh sách:
  1. Nicergoline (drug_modules\neurological\cerebral_circulation.py)

### Neurology - Free-radical scavenger (AIS adjunct, Japan guideline)
**Số lượng**: 1 thuốc

Danh sách:
  1. Edaravone (drug_modules\neurological\cerebral_circulation.py)

### Neurology - Neuropeptide/cerebroprotein hydrolysate (adjunct, evidence limited)
**Số lượng**: 1 thuốc

Danh sách:
  1. Cerebroprotein hydrolysate (khác) (drug_modules\neurological\cerebral_circulation.py)

### Neurology - Calcium channel blocker (cerebral vasospasm prophylaxis)
**Số lượng**: 1 thuốc

Danh sách:
  1. Nimodipine (drug_modules\neurological\cerebral_circulation.py)

### Neurology - Anti-CGRP Receptor Monoclonal Antibody
**Số lượng**: 1 thuốc

Danh sách:
  1. Erenumab (drug_modules\neurological\migraine_cgrp_drugs.py)

### Neurology - Anti-CD20 Monoclonal Antibody for MS
**Số lượng**: 1 thuốc

Danh sách:
  1. Ofatumumab (drug_modules\neurological\multiple_sclerosis_drugs.py)

### Neurology - S1P Receptor Modulator for MS
**Số lượng**: 1 thuốc

Danh sách:
  1. Fingolimod (drug_modules\neurological\multiple_sclerosis_drugs.py)

### Neurology - Fumaric Acid Ester for MS
**Số lượng**: 1 thuốc

Danh sách:
  1. Dimethyl fumarate (drug_modules\neurological\multiple_sclerosis_drugs.py)

### Neurology - Muscle Relaxant (GABA-B Agonist)
**Số lượng**: 1 thuốc

Danh sách:
  1. Baclofen (drug_modules\neurological\muscle_relaxants.py)

### Neurology - Muscle Relaxant (Alpha-2 Adrenergic Agonist)
**Số lượng**: 1 thuốc

Danh sách:
  1. Tizanidine (drug_modules\neurological\muscle_relaxants.py)

### Neurology - Combination (Nootropic + Cerebral vasodilator)
**Số lượng**: 1 thuốc

Danh sách:
  1. Piracetam/Vinpocetine (drug_modules\neurological\neurological_combinations.py)

### Neurology - Combination (Neuroprotective + Nootropic)
**Số lượng**: 1 thuốc

Danh sách:
  1. Citicoline/Piracetam (drug_modules\neurological\neurological_combinations.py)

### Neurology - Combination (Herbal vasomodulator + Cerebral vasodilator)
**Số lượng**: 1 thuốc

Danh sách:
  1. Ginkgo biloba/Vinpocetine (drug_modules\neurological\neurological_combinations.py)

### Psychiatry - Combination (Atypical antipsychotic + SSRI)
**Số lượng**: 1 thuốc

Danh sách:
  1. Olanzapine/Fluoxetine (drug_modules\neurological\neurological_combinations.py)

### Obstetrics/Gynecology - Emergency Contraception
**Số lượng**: 1 thuốc

Danh sách:
  1. Levonorgestrel (drug_modules\obstetrics_gynecology.py)

### Obstetrics/Gynecology - Combined Oral Contraceptive
**Số lượng**: 1 thuốc

Danh sách:
  1. Ethinyl estradiol + Levonorgestrel (drug_modules\obstetrics_gynecology.py)

### Obstetrics/Gynecology - Progestin Contraception (Injectable)
**Số lượng**: 1 thuốc

Danh sách:
  1. Medroxyprogesterone (drug_modules\obstetrics_gynecology.py)

### Obstetrics/Gynecology - Estrogen Replacement Therapy
**Số lượng**: 1 thuốc

Danh sách:
  1. Estradiol (drug_modules\obstetrics_gynecology.py)

### Obstetrics/Gynecology - Progestin Replacement Therapy
**Số lượng**: 1 thuốc

Danh sách:
  1. Progesterone (drug_modules\obstetrics_gynecology.py)

### Obstetrics/Gynecology - Nitroimidazole (Bacterial Vaginosis)
**Số lượng**: 1 thuốc

Danh sách:
  1. Metronidazole (vaginal gel) (drug_modules\obstetrics_gynecology.py)

### Oncology - Anthracycline
**Số lượng**: 1 thuốc

Danh sách:
  1. Doxorubicin (drug_modules\oncology\anthracyclines.py)

### Oncology - Selective Estrogen Receptor Modulator (SERM)
**Số lượng**: 1 thuốc

Danh sách:
  1. Tamoxifen (drug_modules\oncology\hormone_therapy.py)

### Oncology - Aromatase Inhibitor
**Số lượng**: 1 thuốc

Danh sách:
  1. Anastrozole (drug_modules\oncology\hormone_therapy.py)

### Oncology - CYP17 Inhibitor (Androgen Synthesis Inhibitor)
**Số lượng**: 1 thuốc

Danh sách:
  1. Abiraterone (drug_modules\oncology\hormone_therapy.py)

### Oncology - Androgen Receptor Antagonist
**Số lượng**: 1 thuốc

Danh sách:
  1. Enzalutamide (drug_modules\oncology\hormone_therapy.py)

### Oncology - Anti-CD38 Monoclonal Antibody
**Số lượng**: 1 thuốc

Danh sách:
  1. Daratumumab (drug_modules\oncology\monoclonal_antibodies_adcs.py)

### Oncology - Anti-IGF-1R Monoclonal Antibody
**Số lượng**: 1 thuốc

Danh sách:
  1. Teprotumumab (drug_modules\oncology\monoclonal_antibodies_adcs.py)

### Oncology - Anti-EGFR Monoclonal Antibody
**Số lượng**: 1 thuốc

Danh sách:
  1. Cetuximab (drug_modules\oncology\monoclonal_antibodies_adcs.py)

### Oncology - BCR-ABL Tyrosine Kinase Inhibitor
**Số lượng**: 1 thuốc

Danh sách:
  1. Imatinib (drug_modules\oncology\targeted_therapy_tkis.py)

### Oncology - Topoisomerase II Inhibitor
**Số lượng**: 1 thuốc

Danh sách:
  1. Etoposide (drug_modules\oncology\topoisomerase_inhibitors.py)

### Oncology - Vinca Alkaloid
**Số lượng**: 1 thuốc

Danh sách:
  1. Vincristine (drug_modules\oncology\vinca_alkaloids.py)

### Ophthalmology - Beta-blocker (Glaucoma)
**Số lượng**: 1 thuốc

Danh sách:
  1. Timolol eye drops (drug_modules\ophthalmology.py)

### Ophthalmology - Antibiotic (Fluoroquinolone)
**Số lượng**: 1 thuốc

Danh sách:
  1. Ciprofloxacin eye drops (drug_modules\ophthalmology.py)

### Ophthalmology - Lubricant (Dry Eye)
**Số lượng**: 1 thuốc

Danh sách:
  1. Artificial tears (Carboxymethylcellulose) (drug_modules\ophthalmology.py)

### Ophthalmology - Mydriatic (Pupil Dilation)
**Số lượng**: 1 thuốc

Danh sách:
  1. Tropicamide eye drops (drug_modules\ophthalmology.py)

### Ophthalmology - Miotic (Pupil Constriction, Glaucoma)
**Số lượng**: 1 thuốc

Danh sách:
  1. Pilocarpine eye drops (drug_modules\ophthalmology.py)

### Ophthalmology - Fluoroquinolone Antibiotic
**Số lượng**: 1 thuốc

Danh sách:
  1. Moxifloxacin eye drops (drug_modules\ophthalmology.py)

### Ophthalmology - Antiviral (Herpes)
**Số lượng**: 1 thuốc

Danh sách:
  1. Acyclovir eye ointment (drug_modules\ophthalmology.py)

### Ophthalmology - Antiviral
**Số lượng**: 1 thuốc

Danh sách:
  1. Acyclovir eye drops (drug_modules\ophthalmology.py)

### Ophthalmology - Antiviral (CMV)
**Số lượng**: 1 thuốc

Danh sách:
  1. Ganciclovir eye drops (drug_modules\ophthalmology.py)

### Ophthalmology - Alpha-2 Adrenergic Agonist (Glaucoma)
**Số lượng**: 1 thuốc

Danh sách:
  1. Brimonidine (drug_modules\ophthalmology.py)

### Ophthalmology - Cycloplegic/Mydriatic (Long-acting)
**Số lượng**: 1 thuốc

Danh sách:
  1. Atropine eye drops (drug_modules\ophthalmology.py)

### Ophthalmology - Cycloplegic/Mydriatic (Short-acting)
**Số lượng**: 1 thuốc

Danh sách:
  1. Cyclopentolate eye drops (drug_modules\ophthalmology.py)

### Ophthalmology - Alpha-1 Adrenergic Agonist (Mydriatic)
**Số lượng**: 1 thuốc

Danh sách:
  1. Phenylephrine eye drops (drug_modules\ophthalmology.py)

### Ophthalmology - Antibiotic (Macrolide)
**Số lượng**: 1 thuốc

Danh sách:
  1. Erythromycin eye ointment (drug_modules\ophthalmology.py)

### Ophthalmology - Antihistamine (Allergic Conjunctivitis)
**Số lượng**: 1 thuốc

Danh sách:
  1. Azelastine eye drops (drug_modules\ophthalmology.py)

### Ophthalmology - NSAID Prodrug (Anti-inflammatory)
**Số lượng**: 1 thuốc

Danh sách:
  1. Nepafenac eye drops (drug_modules\ophthalmology.py)

### Ophthalmology - Combination Antibiotic
**Số lượng**: 1 thuốc

Danh sách:
  1. Polymyxin B/Trimethoprim eye drops (drug_modules\ophthalmology.py)

### Psychiatry - Anxiolytic (5-HT1A Partial Agonist)
**Số lượng**: 1 thuốc

Danh sách:
  1. Buspirone (drug_modules\psychiatry_other\adhd_anxiolytics.py)

### Psychiatry - ADHD Medication (Non-stimulant)
**Số lượng**: 1 thuốc

Danh sách:
  1. Atomoxetine (drug_modules\psychiatry_other\adhd_anxiolytics.py)

### Psychiatry - ADHD Medication (Stimulant - Prodrug)
**Số lượng**: 1 thuốc

Danh sách:
  1. Lisdexamfetamine (drug_modules\psychiatry_other\adhd_anxiolytics.py)

### Psychiatry - Tetracyclic Antidepressant
**Số lượng**: 1 thuốc

Danh sách:
  1. Mirtazapine (drug_modules\psychiatry_other\antidepressants.py)

### Psychiatry - NDRI (Norepinephrine-Dopamine Reuptake Inhibitor)
**Số lượng**: 1 thuốc

Danh sách:
  1. Bupropion (drug_modules\psychiatry_other\antidepressants.py)

### Psychiatry - Serotonin Antagonist/Reuptake Inhibitor (SARI)
**Số lượng**: 1 thuốc

Danh sách:
  1. Trazodone (drug_modules\psychiatry_other\antidepressants.py)

### Psychiatry - Antipsychotic (Atypical, Partial Agonist)
**Số lượng**: 1 thuốc

Danh sách:
  1. Aripiprazole (drug_modules\psychiatry_other\antipsychotics.py)

### Psychiatry - Antipsychotic (Typical, Phenothiazine)
**Số lượng**: 1 thuốc

Danh sách:
  1. Chlorpromazine (drug_modules\psychiatry_other\antipsychotics.py)

### Respiratory - Anticholinergic (Short-acting)
**Số lượng**: 1 thuốc

Danh sách:
  1. Ipratropium (drug_modules\respiratory\anticholinergic_short_actings.py)

### Respiratory - Fixed-dose Combination (SAMA/SABA)
**Số lượng**: 1 thuốc

Danh sách:
  1. Ipratropium/Salbutamol inhaler (drug_modules\respiratory\combination_inhalers.py)

### Respiratory - Fixed-dose Combination (ICS/LAMA/LABA)
**Số lượng**: 1 thuốc

Danh sách:
  1. Fluticasone/Umeclidinium/Vilanterol inhaler (drug_modules\respiratory\combination_inhalers.py)

### Respiratory - PDE-4 Inhibitor (Anti-inflammatory)
**Số lượng**: 1 thuốc

Danh sách:
  1. Roflumilast (drug_modules\respiratory\pde4_inhibitors.py)

### Respiratory - Biologics (anti-IgE)
**Số lượng**: 1 thuốc

Danh sách:
  1. Omalizumab (drug_modules\respiratory\respiratory_biologics.py)

### Respiratory - Biologics (anti-IL-5)
**Số lượng**: 1 thuốc

Danh sách:
  1. Mepolizumab (drug_modules\respiratory\respiratory_biologics.py)

### Respiratory - Biologics (anti-IL-5Rα)
**Số lượng**: 1 thuốc

Danh sách:
  1. Benralizumab (drug_modules\respiratory\respiratory_biologics.py)

### Respiratory - Biologics (anti-IL-4Rα)
**Số lượng**: 1 thuốc

Danh sách:
  1. Dupilumab (drug_modules\respiratory\respiratory_biologics.py)

### Respiratory - Short-acting Beta-2 Agonist (SABA)
**Số lượng**: 1 thuốc

Danh sách:
  1. Terbutaline (drug_modules\respiratory\short_acting_beta_2_agonist_sabas.py)

### Vitamins/Supplements - Folate
**Số lượng**: 1 thuốc

Danh sách:
  1. Folic acid (drug_modules\supportive\folates.py)

### Vitamins/Supplements - Iron
**Số lượng**: 1 thuốc

Danh sách:
  1. Iron (drug_modules\supportive\irons.py)

### Supportive - Sedative/Anesthetic (ICU)
**Số lượng**: 1 thuốc

Danh sách:
  1. Propofol (drug_modules\supportive\sedatives_anesthetics_icu.py)

### Supportive - Benzodiazepine (IV Sedation/ICU)
**Số lượng**: 1 thuốc

Danh sách:
  1. Midazolam (IV/ICU) (drug_modules\supportive\sedatives_anesthetics_icu.py)

### Supportive - Dissociative anesthetic/analgesic (ICU/Procedural)
**Số lượng**: 1 thuốc

Danh sách:
  1. Ketamine (drug_modules\supportive\sedatives_anesthetics_icu.py)

### Supportive - Alpha-2 agonist sedative (ICU/Procedural)
**Số lượng**: 1 thuốc

Danh sách:
  1. Dexmedetomidine (drug_modules\supportive\sedatives_anesthetics_icu.py)

### Supportive - IV anesthetic for induction (hemodynamic stability)
**Số lượng**: 1 thuốc

Danh sách:
  1. Etomidate (drug_modules\supportive\sedatives_anesthetics_icu.py)

### Supportive - Barbiturate Anesthetic (ICU)
**Số lượng**: 1 thuốc

Danh sách:
  1. Thiopental (drug_modules\supportive\sedatives_anesthetics_icu.py)

### Vitamins/Supplements - Vitamin B12
**Số lượng**: 1 thuốc

Danh sách:
  1. Vitamin B12 (drug_modules\supportive\vitamin_b12s.py)

### Urology - PDE-5 Inhibitor (Erectile Dysfunction/BPH)
**Số lượng**: 1 thuốc

Danh sách:
  1. Tadalafil (drug_modules\urology.py)

### Urology - Beta-3 Adrenergic Agonist (Overactive Bladder)
**Số lượng**: 1 thuốc

Danh sách:
  1. Mirabegron (drug_modules\urology.py)

### Urology - Alpha-1 Adrenergic Blocker (BPH, Selective)
**Số lượng**: 1 thuốc

Danh sách:
  1. Silodosin (drug_modules\urology.py)

---

## 4. DANH SÁCH THUỐC THEO FILE

**Tổng số file**: 158

### drug_modules\miscellaneous\biological_drugs.py
**Số lượng**: 35 thuốc

  1. Adalimumab
  2. Alemtuzumab
  3. Anifrolumab
  4. Atezolizumab
  5. Belimumab
  6. Bevacizumab
  7. Brodalumab
  8. Caplacizumab
  9. Cemiplimab
 10. Certolizumab pegol
 11. Dostarlimab
 12. Durvalumab
 13. Eculizumab
 14. Efgartigimod
 15. Etanercept
 16. Golimumab
 17. Guselkumab
 18. Infliximab
 19. Ixekizumab
 20. Lanadelumab
 21. Natalizumab
 22. Nivolumab
 23. Ocrelizumab
 24. Pembrolizumab
 25. Ravulizumab
 26. Reslizumab
 27. Risankizumab
 28. Rituximab
 29. Sarilumab
 30. Secukinumab
 31. Tezepelumab
 32. Tocilizumab
 33. Trastuzumab
 34. Ustekinumab
 35. Vedolizumab

### drug_modules\dermatology.py
**Số lượng**: 34 thuốc

  1. Adapalene
  2. Azelaic Acid
  3. Azelaic acid topical
  4. Benzoyl peroxide topical
  5. Betamethasone topical
  6. Betamethasone/Clotrimazole topical
  7. Calcipotriol
  8. Calcitriol topical
  9. Clindamycin topical
 10. Clobetasol
 11. Clotrimazole topical
 12. Diclofenac gel
 13. Econazole topical
 14. Erythromycin topical
 15. Fusidic Acid
 16. Fusidic acid/Betamethasone topical
 17. Gentamicin/Betamethasone/Clotrimazole topical
 18. Hydrocortisone topical
 19. Ivermectin cream
 20. Ketoconazole topical
 21. Ketoprofen gel
 22. Metronidazole topical
 23. Miconazole topical
 24. Miconazole/Hydrocortisone topical
 25. Mometasone topical
 26. Mupirocin topical
 27. Permethrin topical
 28. Pimecrolimus
 29. Salicylic Acid
 30. Tacrolimus topical
 31. Tazarotene
 32. Terbinafine topical
 33. Tretinoin topical
 34. Triamcinolone topical

### drug_modules\ophthalmology.py
**Số lượng**: 30 thuốc

  1. Acyclovir eye drops
  2. Acyclovir eye ointment
  3. Artificial tears (Carboxymethylcellulose)
  4. Atropine eye drops
  5. Azelastine eye drops
  6. Bimatoprost
  7. Brimonidine
  8. Brinzolamide
  9. Ciprofloxacin eye drops
 10. Cyclopentolate eye drops
 11. Dexamethasone eye drops
 12. Diclofenac eye drops
 13. Dorzolamide
 14. Erythromycin eye ointment
 15. Ganciclovir eye drops
 16. Gentamicin eye drops
 17. Ketorolac eye drops
 18. Ketotifen eye drops
 19. Latanoprost
 20. Moxifloxacin eye drops
 21. Nepafenac eye drops
 22. Olopatadine eye drops
 23. Phenylephrine eye drops
 24. Pilocarpine eye drops
 25. Polymyxin B/Trimethoprim eye drops
 26. Prednisolone eye drops
 27. Timolol eye drops
 28. Tobramycin eye drops
 29. Travoprost
 30. Tropicamide eye drops

### drug_modules\antimicrobial\antivirals\hiv_arvs.py
**Số lượng**: 17 thuốc

  1. Atazanavir (boosted with ritonavir/cobicistat)
  2. Bictegravir (BIC)
  3. Bictegravir/Emtricitabine/Tenofovir alafenamide (BIC/FTC/TAF)
  4. Cabotegravir + Rilpivirine (Long-acting IM)
  5. Cobicistat (COBI)
  6. Darunavir (boosted with ritonavir/cobicistat)
  7. Dolutegravir (DTG)
  8. Efavirenz (EFV)
  9. Efavirenz/Tenofovir disoproxil fumarate/Emtricitabine (EFV/TDF/FTC)
 10. Emtricitabine (FTC)
 11. Lamivudine (3TC)
 12. Rilpivirine (RPV)
 13. Ritonavir (low-dose booster)
 14. Tenofovir alafenamide (TAF)
 15. Tenofovir alafenamide/Emtricitabine (TAF/FTC)
 16. Tenofovir disoproxil fumarate (TDF)
 17. Tenofovir disoproxil fumarate/Emtricitabine (TDF/FTC)

### drug_modules\neurological\anticonvulsants.py
**Số lượng**: 14 thuốc

  1. Carbamazepine
  2. Ethosuximide
  3. Fosphenytoin
  4. Lacosamide
  5. Lamotrigine
  6. Levetiracetam
  7. Oxcarbazepine
  8. Perampanel
  9. Phenobarbital
 10. Phenytoin
 11. Primidone
 12. Topiramate
 13. Valproate
 14. Zonisamide

### drug_modules\urology.py
**Số lượng**: 14 thuốc

  1. Alfuzosin
  2. Avanafil
  3. Dutasteride
  4. Fesoterodine
  5. Finasteride
  6. Mirabegron
  7. Oxybutynin
  8. Sildenafil
  9. Silodosin
 10. Solifenacin
 11. Tadalafil
 12. Tamsulosin
 13. Tolterodine
 14. Vardenafil

### drug_modules\hematology.py
**Số lượng**: 13 thuốc

  1. Alteplase
  2. Andexanet alfa
  3. Eltrombopag
  4. Emicizumab
  5. Epoetin alfa
  6. Filgrastim
  7. Heparin
  8. Idarucizumab
  9. Protamine
 10. Romiplostim
 11. Tenecteplase
 12. Tranexamic acid
 13. Vitamin K

### drug_modules\infectious_other\antituberculars.py
**Số lượng**: 13 thuốc

  1. Bedaquiline
  2. Clofazimine
  3. Cycloserine / Terizidone
  4. Delamanid
  5. Ethambutol
  6. Isoniazid
  7. Linezolid (lao MDR/XDR)
  8. PAS (para-aminosalicylic acid)
  9. Pyrazinamide
 10. Rifabutin
 11. Rifampin
 12. Rifapentine
 13. Streptomycin

### drug_modules\analgesics\nsaids.py
**Số lượng**: 12 thuốc

  1. Aspirin
  2. Celecoxib
  3. Diclofenac
  4. Etoricoxib
  5. Ibuprofen
  6. Indomethacin
  7. Ketoprofen
  8. Ketorolac
  9. Meloxicam
 10. Naproxen
 11. Nimesulide
 12. Piroxicam

### drug_modules\cardiovascular\antiarrhythmics.py
**Số lượng**: 11 thuốc

  1. Adenosine
  2. Amiodarone
  3. Disopyramide
  4. Dofetilide
  5. Dronedarone
  6. Flecainide
  7. Ibutilide
  8. Procainamide
  9. Propafenone
 10. Quinidine
 11. Sotalol

### drug_modules\emergency\electrolytes.py
**Số lượng**: 11 thuốc

  1. Calcium chloride
  2. Calcium gluconate
  3. Demeclocycline
  4. Magnesium oxide
  5. Magnesium sulfate
  6. Pamidronate
  7. Potassium phosphate
  8. Sodium bicarbonate
  9. Sodium phosphate
 10. Sodium polystyrene sulfonate
 11. Zoledronic acid

### drug_modules\infectious_other\cephalosporins.py
**Số lượng**: 11 thuốc

  1. Cefaclor
  2. Cefadroxil
  3. Cefdinir
  4. Cefixime
  5. Cefoperazone
  6. Cefotaxime
  7. Cefotetan
  8. Cefoxitin
  9. Cefpirome
 10. Ceftazidime
 11. Cefuroxime

### drug_modules\psychiatry_other\antipsychotics.py
**Số lượng**: 11 thuốc

  1. Aripiprazole
  2. Chlorpromazine
  3. Clozapine
  4. Fluphenazine
  5. Haloperidol
  6. Lurasidone
  7. Olanzapine
  8. Pimozide
  9. Quetiapine
 10. Risperidone
 11. Ziprasidone

### drug_modules\cardiovascular\anticoagulants.py
**Số lượng**: 10 thuốc

  1. Apixaban
  2. Clopidogrel
  3. Dabigatran
  4. Edoxaban
  5. Enoxaparin
  6. Fondaparinux
  7. Prasugrel
  8. Rivaroxaban
  9. Ticagrelor
 10. Warfarin

### drug_modules\cardiovascular\other_cv.py
**Số lượng**: 10 thuốc

  1. Clonidine
  2. Digoxin
  3. Doxazosin
  4. Finerenone
  5. Ivabradine
  6. Labetalol
  7. Methyldopa
  8. Sacubitril-valsartan
  9. Sotagliflozin
 10. Vericiguat

### drug_modules\neurological\antiparkinsonian.py
**Số lượng**: 9 thuốc

  1. Deutetrabenazine
  2. Istradefylline
  3. Levodopa/Carbidopa
  4. Opicapone
  5. Pimavanserin
  6. Pramipexole
  7. Ropinirole
  8. Safinamide
  9. Tetrabenazine

### drug_modules\neurological\cerebral_circulation.py
**Số lượng**: 9 thuốc

  1. Cerebrolysin
  2. Cerebroprotein hydrolysate (khác)
  3. Citicoline
  4. Edaravone
  5. Ginkgo biloba extract
  6. Nicergoline
  7. Nimodipine
  8. Piracetam
  9. Vinpocetine

### drug_modules\antimicrobial\antibiotics\beta_lactams.py
**Số lượng**: 8 thuốc

  1. Aztreonam
  2. Cefiderocol
  3. Doripenem
  4. Ertapenem
  5. Imipenem-cilastatin
  6. Meropenem
  7. Penicillin G
  8. Piperacillin-tazobactam

### drug_modules\cardiovascular\calcium_blockers\dihydropyridines.py
**Số lượng**: 8 thuốc

  1. Amlodipine
  2. Clevidipine
  3. Felodipine
  4. Isradipine
  5. Lacidipine
  6. Nicardipine
  7. Nifedipine
  8. Nisoldipine

### drug_modules\cardiovascular\diuretics.py
**Số lượng**: 8 thuốc

  1. Bumetanide
  2. Chlorthalidone
  3. Eplerenone
  4. Furosemide
  5. Hydrochlorothiazide
  6. Indapamide
  7. Spironolactone
  8. Torsemide

### drug_modules\cardiovascular\triglyceride_lowering.py
**Số lượng**: 8 thuốc

  1. Evinacumab
  2. Fenofibrate
  3. Gemfibrozil
  4. Icosapent ethyl
  5. Niacin
  6. Omega-3 acid ethyl esters
  7. Pemafibrate
  8. Plozasiran

### drug_modules\diabetes\specific_insulins.py
**Số lượng**: 8 thuốc

  1. Insulin Aspart
  2. Insulin Degludec
  3. Insulin Detemir
  4. Insulin Glargine
  5. Insulin Glulisine
  6. Insulin Lispro
  7. Insulin NPH
  8. Insulin Regular

### drug_modules\obstetrics_gynecology.py
**Số lượng**: 8 thuốc

  1. Clotrimazole (vaginal)
  2. Estradiol
  3. Ethinyl estradiol + Levonorgestrel
  4. Levonorgestrel
  5. Medroxyprogesterone
  6. Metronidazole (vaginal gel)
  7. Miconazole (vaginal)
  8. Progesterone

### drug_modules\cardiovascular\arbs.py
**Số lượng**: 7 thuốc

  1. Azilsartan medoxomil
  2. Candesartan
  3. Irbesartan
  4. Losartan
  5. Olmesartan
  6. Telmisartan
  7. Valsartan

### drug_modules\cardiovascular\statins.py
**Số lượng**: 7 thuốc

  1. Atorvastatin
  2. Fluvastatin
  3. Lovastatin
  4. Pitavastatin
  5. Pravastatin
  6. Rosuvastatin
  7. Simvastatin

### drug_modules\emergency\catecholamine_alpha__beta_agonists.py
**Số lượng**: 7 thuốc

  1. Dobutamine
  2. Dopamine
  3. Epinephrine
  4. Milrinone
  5. Norepinephrine
  6. Phenylephrine
  7. Vasopressin

### drug_modules\analgesics\opioid_agonist_strongs.py
**Số lượng**: 6 thuốc

  1. Fentanyl
  2. Hydromorphone
  3. Meperidine
  4. Methadone
  5. Morphine
  6. Oxycodone

### drug_modules\antimicrobial\antibiotics\others.py
**Số lượng**: 6 thuốc

  1. Eravacycline
  2. Fidaxomicin
  3. Fosfomycin
  4. Lefamulin
  5. Nitrofurantoin
  6. Omadacycline

### drug_modules\antimicrobial\antibiotics\penicillins.py
**Số lượng**: 6 thuốc

  1. Amoxicillin
  2. Amoxicillin-clavulanate
  3. Ampicillin
  4. Ampicillin-sulbactam
  5. Nafcillin
  6. Oxacillin

### drug_modules\antimicrobial\antivirals\hepatitis.py
**Số lượng**: 6 thuốc

  1. Entecavir
  2. Ledipasvir
  3. Ribavirin
  4. Sofosbuvir
  5. Sofosbuvir/Velpatasvir
  6. Tenofovir

### drug_modules\cardiovascular\ace_inhibitors.py
**Số lượng**: 6 thuốc

  1. Benazepril
  2. Captopril
  3. Enalapril
  4. Lisinopril
  5. Perindopril
  6. Ramipril

### drug_modules\cardiovascular\beta_blockers\selective.py
**Số lượng**: 6 thuốc

  1. Acebutolol
  2. Atenolol
  3. Betaxolol
  4. Bisoprolol
  5. Metoprolol
  6. Nebivolol

### drug_modules\endocrinology_other\osteoporosis_other.py
**Số lượng**: 6 thuốc

  1. Abaloparatide
  2. Calcitonin
  3. Denosumab
  4. Raloxifene
  5. Romosozumab
  6. Teriparatide

### drug_modules\neurological\alzheimer_dementia_drugs.py
**Số lượng**: 6 thuốc

  1. Aducanumab
  2. Donanemab
  3. Donepezil
  4. Lecanemab
  5. Memantine
  6. Rivastigmine

### drug_modules\neurological\migraine_cgrp_drugs.py
**Số lượng**: 6 thuốc

  1. Eptinezumab
  2. Erenumab
  3. Fremanezumab
  4. Galcanezumab
  5. Rimegepant
  6. Ubrogepant

### drug_modules\neurological\muscle_relaxants.py
**Số lượng**: 6 thuốc

  1. Baclofen
  2. Carisoprodol
  3. Cyclobenzaprine
  4. Metaxalone
  5. Methocarbamol
  6. Tizanidine

### drug_modules\oncology\monoclonal_antibodies_adcs.py
**Số lượng**: 6 thuốc

  1. Brentuximab vedotin
  2. Cetuximab
  3. Daratumumab
  4. Sacituzumab govitecan
  5. Teprotumumab
  6. Trastuzumab deruxtecan

### drug_modules\respiratory\combination_inhalers.py
**Số lượng**: 6 thuốc

  1. Budesonide/Formoterol inhaler
  2. Fluticasone/Salmeterol inhaler
  3. Fluticasone/Umeclidinium/Vilanterol inhaler
  4. Ipratropium/Salbutamol inhaler
  5. Tiotropium/Olodaterol inhaler
  6. Umeclidinium/Vilanterol inhaler

### drug_modules\supportive\sedatives_anesthetics_icu.py
**Số lượng**: 6 thuốc

  1. Dexmedetomidine
  2. Etomidate
  3. Ketamine
  4. Midazolam (IV/ICU)
  5. Propofol
  6. Thiopental

### drug_modules\analgesics\pain_muscle_relaxant_combinations.py
**Số lượng**: 5 thuốc

  1. Aspirin/Carisoprodol
  2. Paracetamol/Carisoprodol
  3. Paracetamol/Chlorzoxazone
  4. Paracetamol/Methocarbamol
  5. Paracetamol/Orphenadrine

### drug_modules\antimicrobial\antibiotics\fluoroquinolones.py
**Số lượng**: 5 thuốc

  1. Ciprofloxacin
  2. Levofloxacin
  3. Moxifloxacin
  4. Norfloxacin
  5. Ofloxacin

### drug_modules\antimicrobial\antifungals\azoles.py
**Số lượng**: 5 thuốc

  1. Fluconazole
  2. Isavuconazole
  3. Itraconazole
  4. Posaconazole
  5. Voriconazole

### drug_modules\cardiovascular\vasodilators.py
**Số lượng**: 5 thuốc

  1. Hydralazine
  2. Isosorbide mononitrate
  3. Nesiritide
  4. Nitroglycerin
  5. Nitroprusside

### drug_modules\diabetes\dpp_4_inhibitors.py
**Số lượng**: 5 thuốc

  1. Alogliptin
  2. Linagliptin
  3. Saxagliptin
  4. Sitagliptin
  5. Vildagliptin

### drug_modules\diabetes\fixed_dose_combinations.py
**Số lượng**: 5 thuốc

  1. Metformin/Dapagliflozin
  2. Metformin/Empagliflozin
  3. Metformin/Glibenclamide
  4. Metformin/Pioglitazone
  5. Metformin/Sitagliptin

### drug_modules\diabetes\glp1_agonists.py
**Số lượng**: 5 thuốc

  1. Dulaglutide
  2. Exenatide
  3. Liraglutide
  4. Semaglutide
  5. Tirzepatide

### drug_modules\gastrointestinal\proton_pump_inhibitor_ppis.py
**Số lượng**: 5 thuốc

  1. Dexlansoprazole
  2. Esomeprazole
  3. Ilaprazole
  4. Lansoprazole
  5. Omeprazole

### drug_modules\infectious_other\anthelmintics.py
**Số lượng**: 5 thuốc

  1. Albendazole
  2. Ivermectin
  3. Levamisole
  4. Mebendazole
  5. Praziquantel

### drug_modules\infectious_other\antimalarials.py
**Số lượng**: 5 thuốc

  1. Artemether-lumefantrine
  2. Artesunate
  3. Chloroquine
  4. Hydroxychloroquine
  5. Primaquine

### drug_modules\miscellaneous\vitamins.py
**Số lượng**: 5 thuốc

  1. Calcium (elemental)
  2. Folic Acid
  3. Vitamin C
  4. Vitamin D3 (Cholecalciferol)
  5. Vitamin E

### drug_modules\psychiatry_other\adhd_anxiolytics.py
**Số lượng**: 5 thuốc

  1. Atomoxetine
  2. Buspirone
  3. Dextroamphetamine
  4. Lisdexamfetamine
  5. Methylphenidate

### drug_modules\psychiatry_other\antidepressants.py
**Số lượng**: 5 thuốc

  1. Bupropion
  2. Mirtazapine
  3. Phenelzine
  4. Tranylcypromine
  5. Trazodone

### drug_modules\psychiatry_other\ssris.py
**Số lượng**: 5 thuốc

  1. Citalopram
  2. Escitalopram
  3. Fluvoxamine
  4. Paroxetine
  5. Sertraline

### drug_modules\respiratory\long_acting_beta_2_agonist_labas.py
**Số lượng**: 5 thuốc

  1. Formoterol
  2. Indacaterol
  3. Olodaterol
  4. Salmeterol
  5. Vilanterol

### drug_modules\supportive\antihistamine_h1_antagonist_2nd_generations.py
**Số lượng**: 5 thuốc

  1. Cetirizine
  2. Desloratadine
  3. Fexofenadine
  4. Levocetirizine
  5. Loratadine

### drug_modules\analgesics\opioid_agonists.py
**Số lượng**: 4 thuốc

  1. Buprenorphine
  2. Hydrocodone
  3. Tapentadol
  4. Tramadol

### drug_modules\antimicrobial\antibiotics\aminoglycosides.py
**Số lượng**: 4 thuốc

  1. Amikacin
  2. Gentamicin
  3. Plazomicin
  4. Tobramycin

### drug_modules\antimicrobial\antibiotics\cephalosporins.py
**Số lượng**: 4 thuốc

  1. Cefazolin
  2. Cefepime
  3. Ceftriaxone
  4. Cephalexin

### drug_modules\antimicrobial\antivirals\influenza.py
**Số lượng**: 4 thuốc

  1. Favipiravir
  2. Oseltamivir
  3. Remdesivir
  4. Zanamivir

### drug_modules\cardiovascular\beta_blockers\non_selective.py
**Số lượng**: 4 thuốc

  1. Carvedilol
  2. Nadolol
  3. Propranolol
  4. Timolol

### drug_modules\cardiovascular\fixed_dose_combinations.py
**Số lượng**: 4 thuốc

  1. Amlodipine/Olmesartan
  2. Amlodipine/Valsartan
  3. Lisinopril/Hydrochlorothiazide
  4. Losartan/Hydrochlorothiazide

### drug_modules\diabetes\sglt2_inhibitors.py
**Số lượng**: 4 thuốc

  1. Canagliflozin
  2. Dapagliflozin
  3. Empagliflozin
  4. Ertugliflozin

### drug_modules\emergency\neuromuscular_blockers.py
**Số lượng**: 4 thuốc

  1. Cisatracurium
  2. Rocuronium
  3. Succinylcholine
  4. Vecuronium

### drug_modules\emergency\uterotonics.py
**Số lượng**: 4 thuốc

  1. Carboprost
  2. Dinoprostone
  3. Methylergonovine
  4. Oxytocin

### drug_modules\endocrinology_other\corticosteroids\short_intermediate_acting.py
**Số lượng**: 4 thuốc

  1. Fludrocortisone
  2. Hydrocortisone
  3. Methylprednisolone
  4. Prednisolone

### drug_modules\ent_oral_nasal_combinations.py
**Số lượng**: 4 thuốc

  1. Azelastine/Fluticasone nasal spray
  2. Cetirizine/Pseudoephedrine
  3. Fexofenadine/Pseudoephedrine
  4. Loratadine/Pseudoephedrine

### drug_modules\gastrointestinal\laxatives.py
**Số lượng**: 4 thuốc

  1. Bisacodyl
  2. Lactulose
  3. Polyethylene glycol 3350
  4. Senna (sennosides)

### drug_modules\miscellaneous\immunosuppressants.py
**Số lượng**: 4 thuốc

  1. Azathioprine
  2. Cyclosporine
  3. Mycophenolate
  4. Tacrolimus

### drug_modules\neurological\neurological_combinations.py
**Số lượng**: 4 thuốc

  1. Citicoline/Piracetam
  2. Ginkgo biloba/Vinpocetine
  3. Olanzapine/Fluoxetine
  4. Piracetam/Vinpocetine

### drug_modules\oncology\hormone_therapy.py
**Số lượng**: 4 thuốc

  1. Abiraterone
  2. Anastrozole
  3. Enzalutamide
  4. Tamoxifen

### drug_modules\respiratory\anticholinergic_long_actings.py
**Số lượng**: 4 thuốc

  1. Aclidinium
  2. Glycopyrronium
  3. Tiotropium
  4. Umeclidinium

### drug_modules\respiratory\inhaled_corticosteroid_icss.py
**Số lượng**: 4 thuốc

  1. Beclomethasone inhaled
  2. Budesonide inhaled
  3. Ciclesonide
  4. Fluticasone inhaled

### drug_modules\respiratory\leukotriene_receptor_antagonists.py
**Số lượng**: 4 thuốc

  1. Cromolyn
  2. Montelukast
  3. Nedocromil
  4. Zafirlukast

### drug_modules\respiratory\respiratory_biologics.py
**Số lượng**: 4 thuốc

  1. Benralizumab
  2. Dupilumab
  3. Mepolizumab
  4. Omalizumab

### drug_modules\analgesics\antimigraine_5_ht1_receptor_agonists.py
**Số lượng**: 3 thuốc

  1. Lasmiditan
  2. Rizatriptan
  3. Sumatriptan

### drug_modules\antimicrobial\antibiotics\glycopeptides.py
**Số lượng**: 3 thuốc

  1. Daptomycin
  2. Teicoplanin
  3. Vancomycin

### drug_modules\antimicrobial\antibiotics\macrolides.py
**Số lượng**: 3 thuốc

  1. Azithromycin
  2. Clarithromycin
  3. Erythromycin

### drug_modules\antimicrobial\antibiotics\tetracyclines.py
**Số lượng**: 3 thuốc

  1. Doxycycline
  2. Minocycline
  3. Tetracycline

### drug_modules\antimicrobial\antifungals\echinocandins.py
**Số lượng**: 3 thuốc

  1. Anidulafungin
  2. Caspofungin
  3. Micafungin

### drug_modules\cardiovascular\pcsk9_inhibitors.py
**Số lượng**: 3 thuốc

  1. Alirocumab
  2. Evolocumab
  3. Inclisiran

### drug_modules\diabetes\sulfonylureas.py
**Số lượng**: 3 thuốc

  1. Glibenclamide
  2. Gliclazide
  3. Glimepiride

### drug_modules\endocrinology_other\osteoporosis_bisphosphonates.py
**Số lượng**: 3 thuốc

  1. Alendronate
  2. Ibandronate
  3. Risedronate

### drug_modules\gastrointestinal\antispasmodics.py
**Số lượng**: 3 thuốc

  1. Hyoscine butylbromide
  2. Mebeverine
  3. Trimebutine

### drug_modules\gastrointestinal\h2_receptor_antagonists.py
**Số lượng**: 3 thuốc

  1. Cimetidine
  2. Famotidine
  3. Ranitidine

### drug_modules\gastrointestinal\jak_inhibitors.py
**Số lượng**: 3 thuốc

  1. Baricitinib
  2. Tofacitinib
  3. Upadacitinib

### drug_modules\infectious_other\beta_lactams.py
**Số lượng**: 3 thuốc

  1. Amoxicillin suspension
  2. Dicloxacillin
  3. Penicillin V

### drug_modules\miscellaneous\gout_medications.py
**Số lượng**: 3 thuốc

  1. Colchicine
  2. Febuxostat
  3. Probenecid

### drug_modules\neurological\benzodiazepines.py
**Số lượng**: 3 thuốc

  1. Clonazepam
  2. Diazepam
  3. Lorazepam

### drug_modules\neurological\multiple_sclerosis_drugs.py
**Số lượng**: 3 thuốc

  1. Dimethyl fumarate
  2. Fingolimod
  3. Ofatumumab

### drug_modules\oncology\antimetabolites.py
**Số lượng**: 3 thuốc

  1. 5-Fluorouracil
  2. Capecitabine
  3. Gemcitabine

### drug_modules\oncology\platinum_compounds.py
**Số lượng**: 3 thuốc

  1. Carboplatin
  2. Cisplatin
  3. Oxaliplatin

### drug_modules\oncology\targeted_therapy_tkis.py
**Số lượng**: 3 thuốc

  1. Erlotinib
  2. Gefitinib
  3. Imatinib

### drug_modules\oncology\topoisomerase_inhibitors.py
**Số lượng**: 3 thuốc

  1. Etoposide
  2. Irinotecan
  3. Topotecan

### drug_modules\psychiatry_other\snris.py
**Số lượng**: 3 thuốc

  1. Desvenlafaxine
  2. Duloxetine
  3. Venlafaxine

### drug_modules\supportive\antihistamine_h1_antagonist_1st_generations.py
**Số lượng**: 3 thuốc

  1. Chlorpheniramine
  2. Diphenhydramine
  3. Hydroxyzine

### drug_modules\antimicrobial\antibiotics\polymyxins.py
**Số lượng**: 2 thuốc

  1. Colistin
  2. Polymyxin B

### drug_modules\antimicrobial\antifungals\polyenes.py
**Số lượng**: 2 thuốc

  1. Amphotericin B
  2. Nystatin

### drug_modules\antimicrobial\antivirals\herpes.py
**Số lượng**: 2 thuốc

  1. Acyclovir
  2. Valacyclovir

### drug_modules\cardiovascular\calcium_blockers\non_dihydropyridines.py
**Số lượng**: 2 thuốc

  1. Diltiazem
  2. Verapamil

### drug_modules\cardiovascular\cholesterol_absorption_inhibitors.py
**Số lượng**: 2 thuốc

  1. Bempedoic acid
  2. Ezetimibe

### drug_modules\cardiovascular_other\antiplatelets.py
**Số lượng**: 2 thuốc

  1. Dipyridamole
  2. Ticlopidine

### drug_modules\diabetes\alpha_glucosidase_inhibitors.py
**Số lượng**: 2 thuốc

  1. Acarbose
  2. Miglitol

### drug_modules\diabetes\meglitinides.py
**Số lượng**: 2 thuốc

  1. Nateglinide
  2. Repaglinide

### drug_modules\diabetes\other_antidiabetics.py
**Số lượng**: 2 thuốc

  1. Bromocriptine
  2. Colesevelam

### drug_modules\diabetes\thiazolidinedione_tzds.py
**Số lượng**: 2 thuốc

  1. Pioglitazone
  2. Rosiglitazone

### drug_modules\emergency\opioid_antagonists.py
**Số lượng**: 2 thuốc

  1. Naloxone
  2. Naltrexone

### drug_modules\endocrinology_other\corticosteroids\long_acting.py
**Số lượng**: 2 thuốc

  1. Betamethasone
  2. Dexamethasone

### drug_modules\gastrointestinal\antacids.py
**Số lượng**: 2 thuốc

  1. Aluminum hydroxide/Magnesium hydroxide
  2. Calcium carbonate

### drug_modules\gastrointestinal\antidiarrheals.py
**Số lượng**: 2 thuốc

  1. Bismuth subsalicylate
  2. Loperamide

### drug_modules\gastrointestinal\ibd_5asa.py
**Số lượng**: 2 thuốc

  1. Mesalazine
  2. Sulfasalazine

### drug_modules\gastrointestinal\mucosal_protectants.py
**Số lượng**: 2 thuốc

  1. Misoprostol
  2. Sucralfate

### drug_modules\gastrointestinal\pcab.py
**Số lượng**: 2 thuốc

  1. Tegoprazan
  2. Vonoprazan

### drug_modules\gastrointestinal\prokinetic_antiemetics.py
**Số lượng**: 2 thuốc

  1. Domperidone
  2. Metoclopramide

### drug_modules\gastrointestinal\proton_pump_inhibitors.py
**Số lượng**: 2 thuốc

  1. Pantoprazole
  2. Rabeprazole

### drug_modules\infectious_other\fluoroquinolones.py
**Số lượng**: 2 thuốc

  1. Gemifloxacin
  2. Sparfloxacin

### drug_modules\metabolic\antithyroid.py
**Số lượng**: 2 thuốc

  1. Methimazole
  2. Propylthiouracil

### drug_modules\miscellaneous\dmards_rheumatology.py
**Số lượng**: 2 thuốc

  1. Leflunomide
  2. Methotrexate

### drug_modules\neurological\anticonvulsant_alpha_2_delta_ligands.py
**Số lượng**: 2 thuốc

  1. Gabapentin
  2. Pregabalin

### drug_modules\oncology\alkylating_agents.py
**Số lượng**: 2 thuốc

  1. Cyclophosphamide
  2. Ifosfamide

### drug_modules\oncology\anti_emetic_5_ht3_antagonists.py
**Số lượng**: 2 thuốc

  1. Granisetron
  2. Palonosetron

### drug_modules\oncology\taxanes.py
**Số lượng**: 2 thuốc

  1. Docetaxel
  2. Paclitaxel

### drug_modules\psychiatry_other\tcas.py
**Số lượng**: 2 thuốc

  1. Amitriptyline
  2. Clomipramine

### drug_modules\respiratory\methylxanthines.py
**Số lượng**: 2 thuốc

  1. Aminophylline
  2. Theophylline

### drug_modules\analgesics\analgesic_antipyretic.py
**Số lượng**: 1 thuốc

  1. Paracetamol

### drug_modules\analgesics\opioid_agonist_weaks.py
**Số lượng**: 1 thuốc

  1. Codeine

### drug_modules\antimicrobial\antibiotics\lincosamides.py
**Số lượng**: 1 thuốc

  1. Clindamycin

### drug_modules\antimicrobial\antibiotics\oxazolidinones.py
**Số lượng**: 1 thuốc

  1. Linezolid

### drug_modules\antimicrobial\antibiotics\sulfonamides.py
**Số lượng**: 1 thuốc

  1. Trimethoprim-sulfamethoxazole

### drug_modules\antimicrobial\antivirals\cmv.py
**Số lượng**: 1 thuốc

  1. Ganciclovir

### drug_modules\cardiovascular_other\ace_inhibitors_iv.py
**Số lượng**: 1 thuốc

  1. Enalaprilat

### drug_modules\cardiovascular_other\statins.py
**Số lượng**: 1 thuốc

  1. High-intensity statin (đột quỵ/TIA)

### drug_modules\diabetes\biguanides.py
**Số lượng**: 1 thuốc

  1. Metformin

### drug_modules\diabetes\insulins.py
**Số lượng**: 1 thuốc

  1. Insulin

### drug_modules\diabetes\t1dm_prevention.py
**Số lượng**: 1 thuốc

  1. Teplizumab

### drug_modules\emergency\anticholinergics.py
**Số lượng**: 1 thuốc

  1. Atropine

### drug_modules\emergency\benzodiazepine_antagonists.py
**Số lượng**: 1 thuốc

  1. Flumazenil

### drug_modules\emergency\local_anesthetic__antiarrhythmic_class_ibs.py
**Số lượng**: 1 thuốc

  1. Lidocaine

### drug_modules\endocrinology_other\sex_hormones.py
**Số lượng**: 1 thuốc

  1. Testosterone

### drug_modules\gastrointestinal\antiemetic_5_ht3_antagonists.py
**Số lượng**: 1 thuốc

  1. Ondansetron

### drug_modules\gastrointestinal\antiflatulents.py
**Số lượng**: 1 thuốc

  1. Simethicone

### drug_modules\infectious_other\nitroimidazoles.py
**Số lượng**: 1 thuốc

  1. Metronidazole

### drug_modules\infectious_other\tetracyclines.py
**Số lượng**: 1 thuốc

  1. Tigecycline

### drug_modules\metabolic\corticosteroids.py
**Số lượng**: 1 thuốc

  1. Prednisone

### drug_modules\metabolic\thyroid_hormones.py
**Số lượng**: 1 thuốc

  1. Levothyroxine

### drug_modules\miscellaneous\beta_2_agonist_short_actings.py
**Số lượng**: 1 thuốc

  1. Salbutamol

### drug_modules\miscellaneous\corticosteroid_inhaleds.py
**Số lượng**: 1 thuốc

  1. Budesonide

### drug_modules\miscellaneous\xanthine_oxidase_inhibitors.py
**Số lượng**: 1 thuốc

  1. Allopurinol

### drug_modules\neurological\ssri_selective_serotonin_reuptake_inhibitors.py
**Số lượng**: 1 thuốc

  1. Fluoxetine

### drug_modules\oncology\anthracyclines.py
**Số lượng**: 1 thuốc

  1. Doxorubicin

### drug_modules\oncology\vinca_alkaloids.py
**Số lượng**: 1 thuốc

  1. Vincristine

### drug_modules\respiratory\anticholinergic_short_actings.py
**Số lượng**: 1 thuốc

  1. Ipratropium

### drug_modules\respiratory\pde4_inhibitors.py
**Số lượng**: 1 thuốc

  1. Roflumilast

### drug_modules\respiratory\short_acting_beta_2_agonist_sabas.py
**Số lượng**: 1 thuốc

  1. Terbutaline

### drug_modules\supportive\calciums.py
**Số lượng**: 1 thuốc

  1. Calcium

### drug_modules\supportive\folates.py
**Số lượng**: 1 thuốc

  1. Folic acid

### drug_modules\supportive\irons.py
**Số lượng**: 1 thuốc

  1. Iron

### drug_modules\supportive\vitamin_b12s.py
**Số lượng**: 1 thuốc

  1. Vitamin B12

### drug_modules\supportive\vitamin_ds.py
**Số lượng**: 1 thuốc

  1. Vitamin D

---

## 5. DANH SÁCH TẤT CẢ THUỐC

**Tổng số**: 721 thuốc

  1. **5-Fluorouracil**
    - Nhóm: Oncology - Antimetabolite
    - File: drug_modules\oncology\antimetabolites.py
    - Fields: 23

  2. **Abaloparatide**
    - Nhóm: Endocrinology - PTHrP Analog (Osteoporosis - Anabolic)
    - File: drug_modules\endocrinology_other\osteoporosis_other.py
    - Fields: 24

  3. **Abiraterone**
    - Nhóm: Oncology - CYP17 Inhibitor (Androgen Synthesis Inhibitor)
    - File: drug_modules\oncology\hormone_therapy.py
    - Fields: 23

  4. **Acarbose**
    - Nhóm: Diabetes - Alpha-Glucosidase Inhibitor
    - File: drug_modules\diabetes\alpha_glucosidase_inhibitors.py
    - Fields: 23

  5. **Acebutolol**
    - Nhóm: Cardiovascular - Beta-blocker (selective)
    - File: drug_modules\cardiovascular\beta_blockers\selective.py
    - Fields: 23

  6. **Aclidinium**
    - Nhóm: Respiratory - Anticholinergic (Long-acting)
    - File: drug_modules\respiratory\anticholinergic_long_actings.py
    - Fields: 23

  7. **Acyclovir**
    - Nhóm: Infectious Disease - Antiviral
    - File: drug_modules\antimicrobial\antivirals\herpes.py
    - Fields: 25

  8. **Acyclovir eye drops**
    - Nhóm: Ophthalmology - Antiviral
    - File: drug_modules\ophthalmology.py
    - Fields: 25

  9. **Acyclovir eye ointment**
    - Nhóm: Ophthalmology - Antiviral (Herpes)
    - File: drug_modules\ophthalmology.py
    - Fields: 25

 10. **Adalimumab**
    - Nhóm: Biological - Monoclonal Antibody (anti-TNF-α)
    - File: drug_modules\miscellaneous\biological_drugs.py
    - Fields: 25

 11. **Adapalene**
    - Nhóm: Dermatology - Topical Retinoid
    - File: drug_modules\dermatology.py
    - Fields: 23

 12. **Adenosine**
    - Nhóm: Cardiovascular - Antiarrhythmic (Class V - Purinergic Agonist)
    - File: drug_modules\cardiovascular\antiarrhythmics.py
    - Fields: 22

 13. **Aducanumab**
    - Nhóm: Neurology - Anti-amyloid Monoclonal Antibody
    - File: drug_modules\neurological\alzheimer_dementia_drugs.py
    - Fields: 24

 14. **Albendazole**
    - Nhóm: Infectious Disease - Anthelmintic
    - File: drug_modules\infectious_other\anthelmintics.py
    - Fields: 25

 15. **Alemtuzumab**
    - Nhóm: Biological - Monoclonal Antibody (anti-CD52)
    - File: drug_modules\miscellaneous\biological_drugs.py
    - Fields: 25

 16. **Alendronate**
    - Nhóm: Endocrinology - Bisphosphonate (Osteoporosis)
    - File: drug_modules\endocrinology_other\osteoporosis_bisphosphonates.py
    - Fields: 24

 17. **Alfuzosin**
    - Nhóm: Urology - Alpha-1 Adrenergic Blocker (BPH)
    - File: drug_modules\urology.py
    - Fields: 25

 18. **Alirocumab**
    - Nhóm: Cardiovascular - PCSK9 Inhibitor
    - File: drug_modules\cardiovascular\pcsk9_inhibitors.py
    - Fields: 22

 19. **Allopurinol**
    - Nhóm: Metabolism - Xanthine Oxidase Inhibitor
    - File: drug_modules\miscellaneous\xanthine_oxidase_inhibitors.py
    - Fields: 26

 20. **Alogliptin**
    - Nhóm: Diabetes - DPP-4 Inhibitor
    - File: drug_modules\diabetes\dpp_4_inhibitors.py
    - Fields: 25

 21. **Alteplase**
    - Nhóm: Hematology - Thrombolytic (tPA)
    - File: drug_modules\hematology.py
    - Fields: 24

 22. **Aluminum hydroxide/Magnesium hydroxide**
    - Nhóm: Gastrointestinal - Antacid (Aluminum/Magnesium hydroxide combination)
    - File: drug_modules\gastrointestinal\antacids.py
    - Fields: 24

 23. **Amikacin**
    - Nhóm: Antibiotic - Aminoglycoside
    - File: drug_modules\antimicrobial\antibiotics\aminoglycosides.py
    - Fields: 27

 24. **Aminophylline**
    - Nhóm: Respiratory - Methylxanthine (Bronchodilator)
    - File: drug_modules\respiratory\methylxanthines.py
    - Fields: 24

 25. **Amiodarone**
    - Nhóm: Cardiovascular - Antiarrhythmic (Class III)
    - File: drug_modules\cardiovascular\antiarrhythmics.py
    - Fields: 22

 26. **Amitriptyline**
    - Nhóm: Psychiatry - Tricyclic Antidepressant (TCA)
    - File: drug_modules\psychiatry_other\tcas.py
    - Fields: 24

 27. **Amlodipine**
    - Nhóm: Cardiovascular - Calcium Channel Blocker (Dihydropyridine)
    - File: drug_modules\cardiovascular\calcium_blockers\dihydropyridines.py
    - Fields: 29

 28. **Amlodipine/Olmesartan**
    - Nhóm: Cardiovascular - CCB + ARB (Fixed-Dose Combination)
    - File: drug_modules\cardiovascular\fixed_dose_combinations.py
    - Fields: 24

 29. **Amlodipine/Valsartan**
    - Nhóm: Cardiovascular - CCB + ARB (Fixed-Dose Combination)
    - File: drug_modules\cardiovascular\fixed_dose_combinations.py
    - Fields: 24

 30. **Amoxicillin**
    - Nhóm: Antibiotic - Penicillin (Aminopenicillin)
    - File: drug_modules\antimicrobial\antibiotics\penicillins.py
    - Fields: 21

 31. **Amoxicillin suspension**
    - Nhóm: Antibiotic - Beta-lactam (Penicillin)
    - File: drug_modules\infectious_other\beta_lactams.py
    - Fields: 24

 32. **Amoxicillin-clavulanate**
    - Nhóm: Antibiotic - Penicillin/Beta-lactamase Inhibitor
    - File: drug_modules\antimicrobial\antibiotics\penicillins.py
    - Fields: 21

 33. **Amphotericin B**
    - Nhóm: Infectious Disease - Antifungal (Polyene)
    - File: drug_modules\antimicrobial\antifungals\polyenes.py
    - Fields: 26

 34. **Ampicillin**
    - Nhóm: Antibiotic - Penicillin (Aminopenicillin)
    - File: drug_modules\antimicrobial\antibiotics\penicillins.py
    - Fields: 21

 35. **Ampicillin-sulbactam**
    - Nhóm: Antibiotic - Penicillin/Beta-lactamase Inhibitor
    - File: drug_modules\antimicrobial\antibiotics\penicillins.py
    - Fields: 21

 36. **Anastrozole**
    - Nhóm: Oncology - Aromatase Inhibitor
    - File: drug_modules\oncology\hormone_therapy.py
    - Fields: 23

 37. **Andexanet alfa**
    - Nhóm: Hematology - DOAC Reversal Agent (Factor Xa Inhibitors)
    - File: drug_modules\hematology.py
    - Fields: 26

 38. **Anidulafungin**
    - Nhóm: Infectious Disease - Antifungal (Echinocandin)
    - File: drug_modules\antimicrobial\antifungals\echinocandins.py
    - Fields: 25

 39. **Anifrolumab**
    - Nhóm: Biological - Monoclonal Antibody (anti-IFN-α receptor)
    - File: drug_modules\miscellaneous\biological_drugs.py
    - Fields: 25

 40. **Apixaban**
    - Nhóm: Cardiovascular - Anticoagulant (Direct Factor Xa Inhibitor - DOAC)
    - File: drug_modules\cardiovascular\anticoagulants.py
    - Fields: 26

 41. **Aripiprazole**
    - Nhóm: Psychiatry - Antipsychotic (Atypical, Partial Agonist)
    - File: drug_modules\psychiatry_other\antipsychotics.py
    - Fields: 23

 42. **Artemether-lumefantrine**
    - Nhóm: Infectious Disease - Antimalarial (ACT)
    - File: drug_modules\infectious_other\antimalarials.py
    - Fields: 25

 43. **Artesunate**
    - Nhóm: Infectious Disease - Antimalarial (Artemisinin)
    - File: drug_modules\infectious_other\antimalarials.py
    - Fields: 25

 44. **Artificial tears (Carboxymethylcellulose)**
    - Nhóm: Ophthalmology - Lubricant (Dry Eye)
    - File: drug_modules\ophthalmology.py
    - Fields: 25

 45. **Aspirin**
    - Nhóm: Analgesic - NSAID/Antiplatelet
    - File: drug_modules\analgesics\nsaids.py
    - Fields: 23

 46. **Aspirin/Carisoprodol**
    - Nhóm: Analgesic - Combination (NSAID + Muscle Relaxant)
    - File: drug_modules\analgesics\pain_muscle_relaxant_combinations.py
    - Fields: 23

 47. **Atazanavir (boosted with ritonavir/cobicistat)**
    - Nhóm: Antiviral - Protease inhibitor (boosted)
    - File: drug_modules\antimicrobial\antivirals\hiv_arvs.py
    - Fields: 26

 48. **Atenolol**
    - Nhóm: Cardiovascular - Beta-blocker (Selective)
    - File: drug_modules\cardiovascular\beta_blockers\selective.py
    - Fields: 30

 49. **Atezolizumab**
    - Nhóm: Biological - Monoclonal Antibody (anti-PD-L1)
    - File: drug_modules\miscellaneous\biological_drugs.py
    - Fields: 25

 50. **Atomoxetine**
    - Nhóm: Psychiatry - ADHD Medication (Non-stimulant)
    - File: drug_modules\psychiatry_other\adhd_anxiolytics.py
    - Fields: 23

 51. **Atorvastatin**
    - Nhóm: Cardiovascular - Statin (HMG-CoA Reductase Inhibitor)
    - File: drug_modules\cardiovascular\statins.py
    - Fields: 29

 52. **Atropine**
    - Nhóm: Emergency - Anticholinergic
    - File: drug_modules\emergency\anticholinergics.py
    - Fields: 24

 53. **Atropine eye drops**
    - Nhóm: Ophthalmology - Cycloplegic/Mydriatic (Long-acting)
    - File: drug_modules\ophthalmology.py
    - Fields: 25

 54. **Avanafil**
    - Nhóm: Urology - PDE-5 Inhibitor (Erectile Dysfunction)
    - File: drug_modules\urology.py
    - Fields: 26

 55. **Azathioprine**
    - Nhóm: Immunosuppressant - Antimetabolite
    - File: drug_modules\miscellaneous\immunosuppressants.py
    - Fields: 25

 56. **Azelaic Acid**
    - Nhóm: Dermatology - Topical Antiacne/Anti-inflammatory
    - File: drug_modules\dermatology.py
    - Fields: 23

 57. **Azelaic acid topical**
    - Nhóm: Dermatology - Topical Antiacne/Anti-inflammatory
    - File: drug_modules\dermatology.py
    - Fields: 25

 58. **Azelastine eye drops**
    - Nhóm: Ophthalmology - Antihistamine (Allergic Conjunctivitis)
    - File: drug_modules\ophthalmology.py
    - Fields: 25

 59. **Azelastine/Fluticasone nasal spray**
    - Nhóm: ENT - Combination (Intranasal Antihistamine + Corticosteroid)
    - File: drug_modules\ent_oral_nasal_combinations.py
    - Fields: 23

 60. **Azilsartan medoxomil**
    - Nhóm: Cardiovascular - ARB (Angiotensin Receptor Blocker)
    - File: drug_modules\cardiovascular\arbs.py
    - Fields: 26

 61. **Azithromycin**
    - Nhóm: Antibiotic - Macrolide (Azalide)
    - File: drug_modules\antimicrobial\antibiotics\macrolides.py
    - Fields: 27

 62. **Aztreonam**
    - Nhóm: Antibiotic - Monobactam
    - File: drug_modules\antimicrobial\antibiotics\beta_lactams.py
    - Fields: 24

 63. **Baclofen**
    - Nhóm: Neurology - Muscle Relaxant (GABA-B Agonist)
    - File: drug_modules\neurological\muscle_relaxants.py
    - Fields: 23

 64. **Baricitinib**
    - Nhóm: Rheumatology/Gastrointestinal - JAK Inhibitor (JAK1/JAK2)
    - File: drug_modules\gastrointestinal\jak_inhibitors.py
    - Fields: 25

 65. **Beclomethasone inhaled**
    - Nhóm: Respiratory - Inhaled Corticosteroid (ICS)
    - File: drug_modules\respiratory\inhaled_corticosteroid_icss.py
    - Fields: 24

 66. **Bedaquiline**
    - Nhóm: Infectious Disease - Diarylquinoline (Group A second-line antitubercular for MDR/XDR-TB)
    - File: drug_modules\infectious_other\antituberculars.py
    - Fields: 26

 67. **Belimumab**
    - Nhóm: Biological - Monoclonal Antibody (anti-BAFF)
    - File: drug_modules\miscellaneous\biological_drugs.py
    - Fields: 25

 68. **Bempedoic acid**
    - Nhóm: Cardiovascular - ATP-Citrate Lyase Inhibitor
    - File: drug_modules\cardiovascular\cholesterol_absorption_inhibitors.py
    - Fields: 24

 69. **Benazepril**
    - Nhóm: Cardiovascular - ACE Inhibitor
    - File: drug_modules\cardiovascular\ace_inhibitors.py
    - Fields: 26

 70. **Benralizumab**
    - Nhóm: Respiratory - Biologics (anti-IL-5Rα)
    - File: drug_modules\respiratory\respiratory_biologics.py
    - Fields: 23

 71. **Benzoyl peroxide topical**
    - Nhóm: Dermatology - Topical Antiseptic (Acne)
    - File: drug_modules\dermatology.py
    - Fields: 25

 72. **Betamethasone**
    - Nhóm: Endocrinology - Corticosteroid
    - File: drug_modules\endocrinology_other\corticosteroids\long_acting.py
    - Fields: 22

 73. **Betamethasone topical**
    - Nhóm: Dermatology - Topical Corticosteroid (High Potency)
    - File: drug_modules\dermatology.py
    - Fields: 23

 74. **Betamethasone/Clotrimazole topical**
    - Nhóm: Dermatology - Topical Combination (Corticosteroid + Antifungal)
    - File: drug_modules\dermatology.py
    - Fields: 25

 75. **Betaxolol**
    - Nhóm: Cardiovascular - Beta-blocker (selective)
    - File: drug_modules\cardiovascular\beta_blockers\selective.py
    - Fields: 23

 76. **Bevacizumab**
    - Nhóm: Biological - Monoclonal Antibody (anti-VEGF)
    - File: drug_modules\miscellaneous\biological_drugs.py
    - Fields: 25

 77. **Bictegravir (BIC)**
    - Nhóm: Antiviral - Integrase strand transfer inhibitor (INSTI)
    - File: drug_modules\antimicrobial\antivirals\hiv_arvs.py
    - Fields: 26

 78. **Bictegravir/Emtricitabine/Tenofovir alafenamide (BIC/FTC/TAF)**
    - Nhóm: Antiviral - Single tablet regimen (INSTI + NRTI backbone)
    - File: drug_modules\antimicrobial\antivirals\hiv_arvs.py
    - Fields: 26

 79. **Bimatoprost**
    - Nhóm: Ophthalmology - Prostaglandin Analog (Glaucoma)
    - File: drug_modules\ophthalmology.py
    - Fields: 25

 80. **Bisacodyl**
    - Nhóm: Gastrointestinal - Stimulant Laxative (Diphenylmethane)
    - File: drug_modules\gastrointestinal\laxatives.py
    - Fields: 25

 81. **Bismuth subsalicylate**
    - Nhóm: Gastrointestinal - Antidiarrheal
    - File: drug_modules\gastrointestinal\antidiarrheals.py
    - Fields: 23

 82. **Bisoprolol**
    - Nhóm: Cardiovascular - Beta-blocker (Selective)
    - File: drug_modules\cardiovascular\beta_blockers\selective.py
    - Fields: 30

 83. **Brentuximab vedotin**
    - Nhóm: Oncology - Antibody-Drug Conjugate (ADC)
    - File: drug_modules\oncology\monoclonal_antibodies_adcs.py
    - Fields: 24

 84. **Brimonidine**
    - Nhóm: Ophthalmology - Alpha-2 Adrenergic Agonist (Glaucoma)
    - File: drug_modules\ophthalmology.py
    - Fields: 25

 85. **Brinzolamide**
    - Nhóm: Ophthalmology - Carbonic Anhydrase Inhibitor (Glaucoma)
    - File: drug_modules\ophthalmology.py
    - Fields: 25

 86. **Brodalumab**
    - Nhóm: Biological - Monoclonal Antibody (anti-IL-17RA)
    - File: drug_modules\miscellaneous\biological_drugs.py
    - Fields: 23

 87. **Bromocriptine**
    - Nhóm: Diabetes - Dopamine Agonist
    - File: drug_modules\diabetes\other_antidiabetics.py
    - Fields: 25

 88. **Budesonide**
    - Nhóm: Respiratory - Corticosteroid (Inhaled)
    - File: drug_modules\miscellaneous\corticosteroid_inhaleds.py
    - Fields: 23

 89. **Budesonide inhaled**
    - Nhóm: Respiratory - Inhaled Corticosteroid (ICS)
    - File: drug_modules\respiratory\inhaled_corticosteroid_icss.py
    - Fields: 24

 90. **Budesonide/Formoterol inhaler**
    - Nhóm: Respiratory - Fixed-dose Combination (ICS/LABA)
    - File: drug_modules\respiratory\combination_inhalers.py
    - Fields: 25

 91. **Bumetanide**
    - Nhóm: Cardiovascular - Loop Diuretic
    - File: drug_modules\cardiovascular\diuretics.py
    - Fields: 16

 92. **Buprenorphine**
    - Nhóm: Analgesic - Opioid Partial Agonist
    - File: drug_modules\analgesics\opioid_agonists.py
    - Fields: 23

 93. **Bupropion**
    - Nhóm: Psychiatry - NDRI (Norepinephrine-Dopamine Reuptake Inhibitor)
    - File: drug_modules\psychiatry_other\antidepressants.py
    - Fields: 23

 94. **Buspirone**
    - Nhóm: Psychiatry - Anxiolytic (5-HT1A Partial Agonist)
    - File: drug_modules\psychiatry_other\adhd_anxiolytics.py
    - Fields: 23

 95. **Cabotegravir + Rilpivirine (Long-acting IM)**
    - Nhóm: Antiviral - Long-acting INSTI + NNRTI (injectable)
    - File: drug_modules\antimicrobial\antivirals\hiv_arvs.py
    - Fields: 26

 96. **Calcipotriol**
    - Nhóm: Dermatology - Topical Vitamin D Analog
    - File: drug_modules\dermatology.py
    - Fields: 23

 97. **Calcitonin**
    - Nhóm: Endocrinology - Calcitonin (Osteoporosis, Hypercalcemia)
    - File: drug_modules\endocrinology_other\osteoporosis_other.py
    - Fields: 24

 98. **Calcitriol topical**
    - Nhóm: Dermatology - Topical Vitamin D Analog
    - File: drug_modules\dermatology.py
    - Fields: 23

 99. **Calcium**
    - Nhóm: Vitamins/Supplements - Calcium
    - File: drug_modules\supportive\calciums.py
    - Fields: 24

100. **Calcium (elemental)**
    - Nhóm: Vitamins/Supplements - Calcium
    - File: drug_modules\miscellaneous\vitamins.py
    - Fields: 24

101. **Calcium carbonate**
    - Nhóm: Gastrointestinal - Antacid (Calcium carbonate)
    - File: drug_modules\gastrointestinal\antacids.py
    - Fields: 24

102. **Calcium chloride**
    - Nhóm: Emergency - Electrolyte
    - File: drug_modules\emergency\electrolytes.py
    - Fields: 23

103. **Calcium gluconate**
    - Nhóm: Emergency - Electrolyte
    - File: drug_modules\emergency\electrolytes.py
    - Fields: 23

104. **Canagliflozin**
    - Nhóm: Diabetes - SGLT2 Inhibitor
    - File: drug_modules\diabetes\sglt2_inhibitors.py
    - Fields: 25

105. **Candesartan**
    - Nhóm: Cardiovascular - ARB (Angiotensin Receptor Blocker)
    - File: drug_modules\cardiovascular\arbs.py
    - Fields: 26

106. **Capecitabine**
    - Nhóm: Oncology - Antimetabolite
    - File: drug_modules\oncology\antimetabolites.py
    - Fields: 23

107. **Caplacizumab**
    - Nhóm: Biological - Nanobody (anti-vWF)
    - File: drug_modules\miscellaneous\biological_drugs.py
    - Fields: 23

108. **Captopril**
    - Nhóm: Cardiovascular - ACE Inhibitor
    - File: drug_modules\cardiovascular\ace_inhibitors.py
    - Fields: 30

109. **Carbamazepine**
    - Nhóm: Neurology - Anticonvulsant
    - File: drug_modules\neurological\anticonvulsants.py
    - Fields: 26

110. **Carboplatin**
    - Nhóm: Oncology - Platinum Compound
    - File: drug_modules\oncology\platinum_compounds.py
    - Fields: 23

111. **Carboprost**
    - Nhóm: Emergency - Obstetric uterotonic (Prostaglandin F2-alpha)
    - File: drug_modules\emergency\uterotonics.py
    - Fields: 23

112. **Carisoprodol**
    - Nhóm: Neurology - Muscle Relaxant (Skeletal)
    - File: drug_modules\neurological\muscle_relaxants.py
    - Fields: 24

113. **Carvedilol**
    - Nhóm: Cardiovascular - Beta-blocker (Non-selective with Alpha-blocking)
    - File: drug_modules\cardiovascular\beta_blockers\non_selective.py
    - Fields: 29

114. **Caspofungin**
    - Nhóm: Infectious Disease - Antifungal (Echinocandin)
    - File: drug_modules\antimicrobial\antifungals\echinocandins.py
    - Fields: 25

115. **Cefaclor**
    - Nhóm: Antibiotic - Cephalosporin (2nd Generation, Oral)
    - File: drug_modules\infectious_other\cephalosporins.py
    - Fields: 23

116. **Cefadroxil**
    - Nhóm: Antibiotic - Cephalosporin (1st Generation, Oral)
    - File: drug_modules\infectious_other\cephalosporins.py
    - Fields: 24

117. **Cefazolin**
    - Nhóm: Antibiotic - Cephalosporin (1st Generation)
    - File: drug_modules\antimicrobial\antibiotics\cephalosporins.py
    - Fields: 26

118. **Cefdinir**
    - Nhóm: Antibiotic - Cephalosporin (3rd Generation, Oral)
    - File: drug_modules\infectious_other\cephalosporins.py
    - Fields: 23

119. **Cefepime**
    - Nhóm: Antibiotic - Cephalosporin (4th Generation)
    - File: drug_modules\antimicrobial\antibiotics\cephalosporins.py
    - Fields: 26

120. **Cefiderocol**
    - Nhóm: Antibiotic - Siderophore Cephalosporin
    - File: drug_modules\antimicrobial\antibiotics\beta_lactams.py
    - Fields: 24

121. **Cefixime**
    - Nhóm: Antibiotic - Cephalosporin (3rd Generation, Oral)
    - File: drug_modules\infectious_other\cephalosporins.py
    - Fields: 23

122. **Cefoperazone**
    - Nhóm: Antibiotic - Cephalosporin (3rd Generation)
    - File: drug_modules\infectious_other\cephalosporins.py
    - Fields: 24

123. **Cefotaxime**
    - Nhóm: Antibiotic - Cephalosporin (3rd Generation)
    - File: drug_modules\infectious_other\cephalosporins.py
    - Fields: 23

124. **Cefotetan**
    - Nhóm: Antibiotic - Cephalosporin (2nd Generation, Cephamycin)
    - File: drug_modules\infectious_other\cephalosporins.py
    - Fields: 24

125. **Cefoxitin**
    - Nhóm: Antibiotic - Cephalosporin (2nd Generation, Cephamycin)
    - File: drug_modules\infectious_other\cephalosporins.py
    - Fields: 24

126. **Cefpirome**
    - Nhóm: Antibiotic - Cephalosporin (4th Generation)
    - File: drug_modules\infectious_other\cephalosporins.py
    - Fields: 24

127. **Ceftazidime**
    - Nhóm: Antibiotic - Cephalosporin (3rd Generation)
    - File: drug_modules\infectious_other\cephalosporins.py
    - Fields: 23

128. **Ceftriaxone**
    - Nhóm: Antibiotic - Cephalosporin (3rd Generation)
    - File: drug_modules\antimicrobial\antibiotics\cephalosporins.py
    - Fields: 27

129. **Cefuroxime**
    - Nhóm: Antibiotic - Cephalosporin (2nd Generation)
    - File: drug_modules\infectious_other\cephalosporins.py
    - Fields: 23

130. **Celecoxib**
    - Nhóm: Analgesic - NSAID (COX-2 Selective)
    - File: drug_modules\analgesics\nsaids.py
    - Fields: 23

131. **Cemiplimab**
    - Nhóm: Biological - Monoclonal Antibody (anti-PD-1)
    - File: drug_modules\miscellaneous\biological_drugs.py
    - Fields: 23

132. **Cephalexin**
    - Nhóm: Antibiotic - Cephalosporin (1st Generation)
    - File: drug_modules\antimicrobial\antibiotics\cephalosporins.py
    - Fields: 23

133. **Cerebrolysin**
    - Nhóm: Neurology - Neuropeptide preparation (Stroke adjunct / Neurorecovery, controversial evidence)
    - File: drug_modules\neurological\cerebral_circulation.py
    - Fields: 25

134. **Cerebroprotein hydrolysate (khác)**
    - Nhóm: Neurology - Neuropeptide/cerebroprotein hydrolysate (adjunct, evidence limited)
    - File: drug_modules\neurological\cerebral_circulation.py
    - Fields: 24

135. **Certolizumab pegol**
    - Nhóm: Biological - Monoclonal Antibody (anti-TNF-α, pegylated)
    - File: drug_modules\miscellaneous\biological_drugs.py
    - Fields: 23

136. **Cetirizine**
    - Nhóm: Allergy - Antihistamine (H1 Antagonist, 2nd generation)
    - File: drug_modules\supportive\antihistamine_h1_antagonist_2nd_generations.py
    - Fields: 26

137. **Cetirizine/Pseudoephedrine**
    - Nhóm: ENT - Combination (Oral Antihistamine + Decongestant)
    - File: drug_modules\ent_oral_nasal_combinations.py
    - Fields: 23

138. **Cetuximab**
    - Nhóm: Oncology - Anti-EGFR Monoclonal Antibody
    - File: drug_modules\oncology\monoclonal_antibodies_adcs.py
    - Fields: 23

139. **Chloroquine**
    - Nhóm: Infectious Disease - Antimalarial
    - File: drug_modules\infectious_other\antimalarials.py
    - Fields: 23

140. **Chlorpheniramine**
    - Nhóm: Allergy - Antihistamine (H1 Antagonist, 1st generation)
    - File: drug_modules\supportive\antihistamine_h1_antagonist_1st_generations.py
    - Fields: 24

141. **Chlorpromazine**
    - Nhóm: Psychiatry - Antipsychotic (Typical, Phenothiazine)
    - File: drug_modules\psychiatry_other\antipsychotics.py
    - Fields: 23

142. **Chlorthalidone**
    - Nhóm: Cardiovascular - Thiazide-like Diuretic
    - File: drug_modules\cardiovascular\diuretics.py
    - Fields: 22

143. **Ciclesonide**
    - Nhóm: Respiratory - Inhaled Corticosteroid (ICS)
    - File: drug_modules\respiratory\inhaled_corticosteroid_icss.py
    - Fields: 24

144. **Cimetidine**
    - Nhóm: Gastrointestinal - H2 Receptor Antagonist
    - File: drug_modules\gastrointestinal\h2_receptor_antagonists.py
    - Fields: 23

145. **Ciprofloxacin**
    - Nhóm: Antibiotic - Fluoroquinolone
    - File: drug_modules\antimicrobial\antibiotics\fluoroquinolones.py
    - Fields: 21

146. **Ciprofloxacin eye drops**
    - Nhóm: Ophthalmology - Antibiotic (Fluoroquinolone)
    - File: drug_modules\ophthalmology.py
    - Fields: 23

147. **Cisatracurium**
    - Nhóm: Emergency - Non-depolarizing Neuromuscular Blocker (Benzylisoquinolinium)
    - File: drug_modules\emergency\neuromuscular_blockers.py
    - Fields: 25

148. **Cisplatin**
    - Nhóm: Oncology - Platinum Compound
    - File: drug_modules\oncology\platinum_compounds.py
    - Fields: 23

149. **Citalopram**
    - Nhóm: Psychiatry - SSRI
    - File: drug_modules\psychiatry_other\ssris.py
    - Fields: 24

150. **Citicoline**
    - Nhóm: Neurology - Neuroprotective / Nootropic
    - File: drug_modules\neurological\cerebral_circulation.py
    - Fields: 24

151. **Citicoline/Piracetam**
    - Nhóm: Neurology - Combination (Neuroprotective + Nootropic)
    - File: drug_modules\neurological\neurological_combinations.py
    - Fields: 25

152. **Clarithromycin**
    - Nhóm: Antibiotic - Macrolide
    - File: drug_modules\antimicrobial\antibiotics\macrolides.py
    - Fields: 27

153. **Clevidipine**
    - Nhóm: Cardiovascular - Calcium Channel Blocker (Dihydropyridine, IV)
    - File: drug_modules\cardiovascular\calcium_blockers\dihydropyridines.py
    - Fields: 23

154. **Clindamycin**
    - Nhóm: Antibiotic - Lincosamide
    - File: drug_modules\antimicrobial\antibiotics\lincosamides.py
    - Fields: 27

155. **Clindamycin topical**
    - Nhóm: Dermatology - Topical Antibiotic
    - File: drug_modules\dermatology.py
    - Fields: 23

156. **Clobetasol**
    - Nhóm: Dermatology - Topical Corticosteroid (Ultra-high Potency)
    - File: drug_modules\dermatology.py
    - Fields: 23

157. **Clofazimine**
    - Nhóm: Infectious Disease - Riminophenazine dye (Second-line antitubercular, MDR-TB; leprosy drug)
    - File: drug_modules\infectious_other\antituberculars.py
    - Fields: 26

158. **Clomipramine**
    - Nhóm: Psychiatry - Tricyclic Antidepressant (TCA)
    - File: drug_modules\psychiatry_other\tcas.py
    - Fields: 23

159. **Clonazepam**
    - Nhóm: Neurology - Benzodiazepine
    - File: drug_modules\neurological\benzodiazepines.py
    - Fields: 24

160. **Clonidine**
    - Nhóm: Cardiovascular - Central Alpha-2 Agonist
    - File: drug_modules\cardiovascular\other_cv.py
    - Fields: 23

161. **Clopidogrel**
    - Nhóm: Cardiovascular - Antiplatelet (P2Y12 Inhibitor)
    - File: drug_modules\cardiovascular\anticoagulants.py
    - Fields: 24

162. **Clotrimazole (vaginal)**
    - Nhóm: Obstetrics/Gynecology - Antifungal (Vulvovaginal Candidiasis)
    - File: drug_modules\obstetrics_gynecology.py
    - Fields: 24

163. **Clotrimazole topical**
    - Nhóm: Dermatology - Topical Antifungal
    - File: drug_modules\dermatology.py
    - Fields: 23

164. **Clozapine**
    - Nhóm: Psychiatry - Antipsychotic (Atypical)
    - File: drug_modules\psychiatry_other\antipsychotics.py
    - Fields: 23

165. **Cobicistat (COBI)**
    - Nhóm: Pharmacokinetic booster (CYP3A inhibitor)
    - File: drug_modules\antimicrobial\antivirals\hiv_arvs.py
    - Fields: 26

166. **Codeine**
    - Nhóm: Analgesic - Opioid Agonist (Weak)
    - File: drug_modules\analgesics\opioid_agonist_weaks.py
    - Fields: 23

167. **Colchicine**
    - Nhóm: Metabolism - Gout Medication (Anti-inflammatory)
    - File: drug_modules\miscellaneous\gout_medications.py
    - Fields: 24

168. **Colesevelam**
    - Nhóm: Diabetes - Bile Acid Sequestrant
    - File: drug_modules\diabetes\other_antidiabetics.py
    - Fields: 25

169. **Colistin**
    - Nhóm: Antibiotic - Polymyxin
    - File: drug_modules\antimicrobial\antibiotics\polymyxins.py
    - Fields: 27

170. **Cromolyn**
    - Nhóm: Respiratory - Mast Cell Stabilizer
    - File: drug_modules\respiratory\leukotriene_receptor_antagonists.py
    - Fields: 23

171. **Cyclobenzaprine**
    - Nhóm: Neurology - Muscle Relaxant (Skeletal)
    - File: drug_modules\neurological\muscle_relaxants.py
    - Fields: 24

172. **Cyclopentolate eye drops**
    - Nhóm: Ophthalmology - Cycloplegic/Mydriatic (Short-acting)
    - File: drug_modules\ophthalmology.py
    - Fields: 23

173. **Cyclophosphamide**
    - Nhóm: Oncology - Alkylating Agent
    - File: drug_modules\oncology\alkylating_agents.py
    - Fields: 23

174. **Cycloserine / Terizidone**
    - Nhóm: Infectious Disease - Second-line antitubercular (D-alanine analog, MDR-TB)
    - File: drug_modules\infectious_other\antituberculars.py
    - Fields: 26

175. **Cyclosporine**
    - Nhóm: Immunosuppressant - Calcineurin Inhibitor
    - File: drug_modules\miscellaneous\immunosuppressants.py
    - Fields: 23

176. **Dabigatran**
    - Nhóm: Cardiovascular - Anticoagulant (Direct Thrombin Inhibitor - DOAC)
    - File: drug_modules\cardiovascular\anticoagulants.py
    - Fields: 26

177. **Dapagliflozin**
    - Nhóm: Diabetes - SGLT2 Inhibitor
    - File: drug_modules\diabetes\sglt2_inhibitors.py
    - Fields: 25

178. **Daptomycin**
    - Nhóm: Antibiotic - Lipopeptide
    - File: drug_modules\antimicrobial\antibiotics\glycopeptides.py
    - Fields: 26

179. **Daratumumab**
    - Nhóm: Oncology - Anti-CD38 Monoclonal Antibody
    - File: drug_modules\oncology\monoclonal_antibodies_adcs.py
    - Fields: 24

180. **Darunavir (boosted with ritonavir/cobicistat)**
    - Nhóm: Antiviral - Protease inhibitor (boosted)
    - File: drug_modules\antimicrobial\antivirals\hiv_arvs.py
    - Fields: 26

181. **Delamanid**
    - Nhóm: Infectious Disease - Nitroimidazole (Group C second-line antitubercular for MDR/XDR-TB)
    - File: drug_modules\infectious_other\antituberculars.py
    - Fields: 26

182. **Demeclocycline**
    - Nhóm: Emergency - Electrolyte (Tetracycline Antibiotic)
    - File: drug_modules\emergency\electrolytes.py
    - Fields: 23

183. **Denosumab**
    - Nhóm: Endocrinology - RANKL Inhibitor (Osteoporosis)
    - File: drug_modules\endocrinology_other\osteoporosis_other.py
    - Fields: 24

184. **Desloratadine**
    - Nhóm: Allergy - Antihistamine (H1 Antagonist, 2nd generation)
    - File: drug_modules\supportive\antihistamine_h1_antagonist_2nd_generations.py
    - Fields: 22

185. **Desvenlafaxine**
    - Nhóm: Psychiatry - SNRI (Serotonin-Norepinephrine Reuptake Inhibitor)
    - File: drug_modules\psychiatry_other\snris.py
    - Fields: 22

186. **Deutetrabenazine**
    - Nhóm: Neurology - Movement Disorders (VMAT2 Inhibitor)
    - File: drug_modules\neurological\antiparkinsonian.py
    - Fields: 23

187. **Dexamethasone**
    - Nhóm: Endocrinology - Corticosteroid
    - File: drug_modules\endocrinology_other\corticosteroids\long_acting.py
    - Fields: 22

188. **Dexamethasone eye drops**
    - Nhóm: Ophthalmology - Corticosteroid (Anti-inflammatory)
    - File: drug_modules\ophthalmology.py
    - Fields: 24

189. **Dexlansoprazole**
    - Nhóm: Gastrointestinal - Proton Pump Inhibitor (PPI) - Dual delayed release
    - File: drug_modules\gastrointestinal\proton_pump_inhibitor_ppis.py
    - Fields: 24

190. **Dexmedetomidine**
    - Nhóm: Supportive - Alpha-2 agonist sedative (ICU/Procedural)
    - File: drug_modules\supportive\sedatives_anesthetics_icu.py
    - Fields: 26

191. **Dextroamphetamine**
    - Nhóm: Psychiatry - ADHD Medication (Stimulant)
    - File: drug_modules\psychiatry_other\adhd_anxiolytics.py
    - Fields: 23

192. **Diazepam**
    - Nhóm: Neurology - Benzodiazepine
    - File: drug_modules\neurological\benzodiazepines.py
    - Fields: 24

193. **Diclofenac**
    - Nhóm: Analgesic - NSAID
    - File: drug_modules\analgesics\nsaids.py
    - Fields: 25

194. **Diclofenac eye drops**
    - Nhóm: Ophthalmology - NSAID (Anti-inflammatory)
    - File: drug_modules\ophthalmology.py
    - Fields: 24

195. **Diclofenac gel**
    - Nhóm: Dermatology - Topical NSAID
    - File: drug_modules\dermatology.py
    - Fields: 23

196. **Dicloxacillin**
    - Nhóm: Antibiotic - Beta-lactam (Penicillinase-resistant Penicillin)
    - File: drug_modules\infectious_other\beta_lactams.py
    - Fields: 23

197. **Digoxin**
    - Nhóm: Cardiovascular - Cardiac Glycoside
    - File: drug_modules\cardiovascular\other_cv.py
    - Fields: 27

198. **Diltiazem**
    - Nhóm: Cardiovascular - Calcium Channel Blocker (Non-dihydropyridine)
    - File: drug_modules\cardiovascular\calcium_blockers\non_dihydropyridines.py
    - Fields: 23

199. **Dimethyl fumarate**
    - Nhóm: Neurology - Fumaric Acid Ester for MS
    - File: drug_modules\neurological\multiple_sclerosis_drugs.py
    - Fields: 24

200. **Dinoprostone**
    - Nhóm: Emergency - Obstetric (Prostaglandin E2, Cervical ripening)
    - File: drug_modules\emergency\uterotonics.py
    - Fields: 23

201. **Diphenhydramine**
    - Nhóm: Allergy - Antihistamine (H1 Antagonist, 1st generation)
    - File: drug_modules\supportive\antihistamine_h1_antagonist_1st_generations.py
    - Fields: 22

202. **Dipyridamole**
    - Nhóm: Cardiovascular - Antiplatelet
    - File: drug_modules\cardiovascular_other\antiplatelets.py
    - Fields: 26

203. **Disopyramide**
    - Nhóm: Cardiovascular - Antiarrhythmic (Class IA)
    - File: drug_modules\cardiovascular\antiarrhythmics.py
    - Fields: 23

204. **Dobutamine**
    - Nhóm: Emergency - Catecholamine (Alpha & Beta Agonist)
    - File: drug_modules\emergency\catecholamine_alpha__beta_agonists.py
    - Fields: 21

205. **Docetaxel**
    - Nhóm: Oncology - Taxane
    - File: drug_modules\oncology\taxanes.py
    - Fields: 23

206. **Dofetilide**
    - Nhóm: Cardiovascular - Antiarrhythmic (Class III)
    - File: drug_modules\cardiovascular\antiarrhythmics.py
    - Fields: 23

207. **Dolutegravir (DTG)**
    - Nhóm: Antiviral - Integrase strand transfer inhibitor (INSTI)
    - File: drug_modules\antimicrobial\antivirals\hiv_arvs.py
    - Fields: 26

208. **Domperidone**
    - Nhóm: Gastrointestinal - Prokinetic, Antiemetic
    - File: drug_modules\gastrointestinal\prokinetic_antiemetics.py
    - Fields: 23

209. **Donanemab**
    - Nhóm: Neurology - Anti-amyloid Monoclonal Antibody
    - File: drug_modules\neurological\alzheimer_dementia_drugs.py
    - Fields: 24

210. **Donepezil**
    - Nhóm: Neurology - Cholinesterase Inhibitor
    - File: drug_modules\neurological\alzheimer_dementia_drugs.py
    - Fields: 24

211. **Dopamine**
    - Nhóm: Emergency - Catecholamine (Alpha & Beta Agonist)
    - File: drug_modules\emergency\catecholamine_alpha__beta_agonists.py
    - Fields: 21

212. **Doripenem**
    - Nhóm: Antibiotic - Carbapenem
    - File: drug_modules\antimicrobial\antibiotics\beta_lactams.py
    - Fields: 23

213. **Dorzolamide**
    - Nhóm: Ophthalmology - Carbonic Anhydrase Inhibitor (Glaucoma)
    - File: drug_modules\ophthalmology.py
    - Fields: 23

214. **Dostarlimab**
    - Nhóm: Biological - Monoclonal Antibody (anti-PD-1)
    - File: drug_modules\miscellaneous\biological_drugs.py
    - Fields: 23

215. **Doxazosin**
    - Nhóm: Cardiovascular - Alpha-1 Blocker
    - File: drug_modules\cardiovascular\other_cv.py
    - Fields: 23

216. **Doxorubicin**
    - Nhóm: Oncology - Anthracycline
    - File: drug_modules\oncology\anthracyclines.py
    - Fields: 24

217. **Doxycycline**
    - Nhóm: Antibiotic - Tetracycline
    - File: drug_modules\antimicrobial\antibiotics\tetracyclines.py
    - Fields: 27

218. **Dronedarone**
    - Nhóm: Cardiovascular - Antiarrhythmic (Class III)
    - File: drug_modules\cardiovascular\antiarrhythmics.py
    - Fields: 22

219. **Dulaglutide**
    - Nhóm: Diabetes - GLP-1 Receptor Agonist
    - File: drug_modules\diabetes\glp1_agonists.py
    - Fields: 26

220. **Duloxetine**
    - Nhóm: Psychiatry - SNRI (Serotonin-Norepinephrine Reuptake Inhibitor)
    - File: drug_modules\psychiatry_other\snris.py
    - Fields: 22

221. **Dupilumab**
    - Nhóm: Respiratory - Biologics (anti-IL-4Rα)
    - File: drug_modules\respiratory\respiratory_biologics.py
    - Fields: 23

222. **Durvalumab**
    - Nhóm: Biological - Monoclonal Antibody (anti-PD-L1)
    - File: drug_modules\miscellaneous\biological_drugs.py
    - Fields: 23

223. **Dutasteride**
    - Nhóm: Urology - 5-alpha Reductase Inhibitor (BPH)
    - File: drug_modules\urology.py
    - Fields: 24

224. **Econazole topical**
    - Nhóm: Dermatology - Topical Antifungal
    - File: drug_modules\dermatology.py
    - Fields: 23

225. **Eculizumab**
    - Nhóm: Biological - Monoclonal Antibody (anti-C5)
    - File: drug_modules\miscellaneous\biological_drugs.py
    - Fields: 23

226. **Edaravone**
    - Nhóm: Neurology - Free-radical scavenger (AIS adjunct, Japan guideline)
    - File: drug_modules\neurological\cerebral_circulation.py
    - Fields: 24

227. **Edoxaban**
    - Nhóm: Cardiovascular - Anticoagulant (Direct Factor Xa Inhibitor - DOAC)
    - File: drug_modules\cardiovascular\anticoagulants.py
    - Fields: 26

228. **Efavirenz (EFV)**
    - Nhóm: Antiviral - Non-nucleoside reverse transcriptase inhibitor (NNRTI)
    - File: drug_modules\antimicrobial\antivirals\hiv_arvs.py
    - Fields: 26

229. **Efavirenz/Tenofovir disoproxil fumarate/Emtricitabine (EFV/TDF/FTC)**
    - Nhóm: Antiviral - Single tablet regimen (NNRTI + NRTI backbone)
    - File: drug_modules\antimicrobial\antivirals\hiv_arvs.py
    - Fields: 26

230. **Efgartigimod**
    - Nhóm: Biological - FcRn Blocker (anti-FcRn)
    - File: drug_modules\miscellaneous\biological_drugs.py
    - Fields: 23

231. **Eltrombopag**
    - Nhóm: Hematology - TPO Receptor Agonist
    - File: drug_modules\hematology.py
    - Fields: 24

232. **Emicizumab**
    - Nhóm: Hematology - Bispecific Monoclonal Antibody
    - File: drug_modules\hematology.py
    - Fields: 24

233. **Empagliflozin**
    - Nhóm: Diabetes - SGLT2 Inhibitor
    - File: drug_modules\diabetes\sglt2_inhibitors.py
    - Fields: 25

234. **Emtricitabine (FTC)**
    - Nhóm: Antiviral - Nucleoside reverse transcriptase inhibitor (NRTI)
    - File: drug_modules\antimicrobial\antivirals\hiv_arvs.py
    - Fields: 26

235. **Enalapril**
    - Nhóm: Cardiovascular - ACE Inhibitor
    - File: drug_modules\cardiovascular\ace_inhibitors.py
    - Fields: 30

236. **Enalaprilat**
    - Nhóm: Cardiovascular - ACE Inhibitor (IV)
    - File: drug_modules\cardiovascular_other\ace_inhibitors_iv.py
    - Fields: 23

237. **Enoxaparin**
    - Nhóm: Cardiovascular - Anticoagulant (Low Molecular Weight Heparin)
    - File: drug_modules\cardiovascular\anticoagulants.py
    - Fields: 23

238. **Entecavir**
    - Nhóm: Infectious Disease - Antiviral (HBV)
    - File: drug_modules\antimicrobial\antivirals\hepatitis.py
    - Fields: 26

239. **Enzalutamide**
    - Nhóm: Oncology - Androgen Receptor Antagonist
    - File: drug_modules\oncology\hormone_therapy.py
    - Fields: 23

240. **Epinephrine**
    - Nhóm: Emergency - Catecholamine (Alpha & Beta Agonist)
    - File: drug_modules\emergency\catecholamine_alpha__beta_agonists.py
    - Fields: 25

241. **Eplerenone**
    - Nhóm: Cardiovascular - Aldosterone Antagonist (Potassium-sparing Diuretic)
    - File: drug_modules\cardiovascular\diuretics.py
    - Fields: 25

242. **Epoetin alfa**
    - Nhóm: Hematology - Erythropoiesis-Stimulating Agent (ESA)
    - File: drug_modules\hematology.py
    - Fields: 24

243. **Eptinezumab**
    - Nhóm: Neurology - Anti-CGRP Monoclonal Antibody
    - File: drug_modules\neurological\migraine_cgrp_drugs.py
    - Fields: 24

244. **Eravacycline**
    - Nhóm: Antibiotic - Tetracycline (Next Generation)
    - File: drug_modules\antimicrobial\antibiotics\others.py
    - Fields: 24

245. **Erenumab**
    - Nhóm: Neurology - Anti-CGRP Receptor Monoclonal Antibody
    - File: drug_modules\neurological\migraine_cgrp_drugs.py
    - Fields: 24

246. **Erlotinib**
    - Nhóm: Oncology - EGFR Tyrosine Kinase Inhibitor
    - File: drug_modules\oncology\targeted_therapy_tkis.py
    - Fields: 23

247. **Ertapenem**
    - Nhóm: Antibiotic - Carbapenem
    - File: drug_modules\antimicrobial\antibiotics\beta_lactams.py
    - Fields: 28

248. **Ertugliflozin**
    - Nhóm: Diabetes - SGLT2 Inhibitor
    - File: drug_modules\diabetes\sglt2_inhibitors.py
    - Fields: 26

249. **Erythromycin**
    - Nhóm: Antibiotic - Macrolide
    - File: drug_modules\antimicrobial\antibiotics\macrolides.py
    - Fields: 27

250. **Erythromycin eye ointment**
    - Nhóm: Ophthalmology - Antibiotic (Macrolide)
    - File: drug_modules\ophthalmology.py
    - Fields: 23

251. **Erythromycin topical**
    - Nhóm: Dermatology - Topical Antibiotic
    - File: drug_modules\dermatology.py
    - Fields: 23

252. **Escitalopram**
    - Nhóm: Psychiatry - SSRI
    - File: drug_modules\psychiatry_other\ssris.py
    - Fields: 24

253. **Esomeprazole**
    - Nhóm: Gastrointestinal - Proton Pump Inhibitor (PPI)
    - File: drug_modules\gastrointestinal\proton_pump_inhibitor_ppis.py
    - Fields: 23

254. **Estradiol**
    - Nhóm: Obstetrics/Gynecology - Estrogen Replacement Therapy
    - File: drug_modules\obstetrics_gynecology.py
    - Fields: 24

255. **Etanercept**
    - Nhóm: Biological - Fusion Protein (TNF receptor)
    - File: drug_modules\miscellaneous\biological_drugs.py
    - Fields: 25

256. **Ethambutol**
    - Nhóm: Infectious Disease - Antitubercular (First-line)
    - File: drug_modules\infectious_other\antituberculars.py
    - Fields: 26

257. **Ethinyl estradiol + Levonorgestrel**
    - Nhóm: Obstetrics/Gynecology - Combined Oral Contraceptive
    - File: drug_modules\obstetrics_gynecology.py
    - Fields: 24

258. **Ethosuximide**
    - Nhóm: Neurology - Anticonvulsant
    - File: drug_modules\neurological\anticonvulsants.py
    - Fields: 27

259. **Etomidate**
    - Nhóm: Supportive - IV anesthetic for induction (hemodynamic stability)
    - File: drug_modules\supportive\sedatives_anesthetics_icu.py
    - Fields: 26

260. **Etoposide**
    - Nhóm: Oncology - Topoisomerase II Inhibitor
    - File: drug_modules\oncology\topoisomerase_inhibitors.py
    - Fields: 23

261. **Etoricoxib**
    - Nhóm: Analgesic - NSAID (COX-2 Selective)
    - File: drug_modules\analgesics\nsaids.py
    - Fields: 23

262. **Evinacumab**
    - Nhóm: Cardiovascular - ANGPTL3 Inhibitor (Monoclonal Antibody)
    - File: drug_modules\cardiovascular\triglyceride_lowering.py
    - Fields: 23

263. **Evolocumab**
    - Nhóm: Cardiovascular - PCSK9 Inhibitor
    - File: drug_modules\cardiovascular\pcsk9_inhibitors.py
    - Fields: 22

264. **Exenatide**
    - Nhóm: Diabetes - GLP-1 Receptor Agonist
    - File: drug_modules\diabetes\glp1_agonists.py
    - Fields: 26

265. **Ezetimibe**
    - Nhóm: Cardiovascular - Cholesterol Absorption Inhibitor
    - File: drug_modules\cardiovascular\cholesterol_absorption_inhibitors.py
    - Fields: 23

266. **Famotidine**
    - Nhóm: Gastrointestinal - H2 Receptor Antagonist
    - File: drug_modules\gastrointestinal\h2_receptor_antagonists.py
    - Fields: 23

267. **Favipiravir**
    - Nhóm: Infectious Disease - Antiviral (RNA polymerase inhibitor)
    - File: drug_modules\antimicrobial\antivirals\influenza.py
    - Fields: 26

268. **Febuxostat**
    - Nhóm: Metabolism - Gout Medication (Xanthine Oxidase Inhibitor)
    - File: drug_modules\miscellaneous\gout_medications.py
    - Fields: 26

269. **Felodipine**
    - Nhóm: Cardiovascular - Calcium Channel Blocker (Dihydropyridine)
    - File: drug_modules\cardiovascular\calcium_blockers\dihydropyridines.py
    - Fields: 27

270. **Fenofibrate**
    - Nhóm: Cardiovascular - Fibrate (PPAR-alpha Agonist)
    - File: drug_modules\cardiovascular\triglyceride_lowering.py
    - Fields: 23

271. **Fentanyl**
    - Nhóm: Analgesic - Opioid Agonist (Strong)
    - File: drug_modules\analgesics\opioid_agonist_strongs.py
    - Fields: 25

272. **Fesoterodine**
    - Nhóm: Urology - Anticholinergic (Overactive Bladder)
    - File: drug_modules\urology.py
    - Fields: 25

273. **Fexofenadine**
    - Nhóm: Allergy - Antihistamine (H1 Antagonist, 2nd generation)
    - File: drug_modules\supportive\antihistamine_h1_antagonist_2nd_generations.py
    - Fields: 24

274. **Fexofenadine/Pseudoephedrine**
    - Nhóm: ENT - Combination (Oral Antihistamine + Decongestant)
    - File: drug_modules\ent_oral_nasal_combinations.py
    - Fields: 23

275. **Fidaxomicin**
    - Nhóm: Antibiotic - Macrocyclic
    - File: drug_modules\antimicrobial\antibiotics\others.py
    - Fields: 27

276. **Filgrastim**
    - Nhóm: Hematology - G-CSF (Granulocyte Colony-Stimulating Factor)
    - File: drug_modules\hematology.py
    - Fields: 25

277. **Finasteride**
    - Nhóm: Urology - 5-alpha Reductase Inhibitor (BPH)
    - File: drug_modules\urology.py
    - Fields: 26

278. **Finerenone**
    - Nhóm: Cardiovascular/Metabolic - Nonsteroidal MRA
    - File: drug_modules\cardiovascular\other_cv.py
    - Fields: 24

279. **Fingolimod**
    - Nhóm: Neurology - S1P Receptor Modulator for MS
    - File: drug_modules\neurological\multiple_sclerosis_drugs.py
    - Fields: 24

280. **Flecainide**
    - Nhóm: Cardiovascular - Antiarrhythmic (Class IC)
    - File: drug_modules\cardiovascular\antiarrhythmics.py
    - Fields: 22

281. **Fluconazole**
    - Nhóm: Infectious Disease - Antifungal (Azole)
    - File: drug_modules\antimicrobial\antifungals\azoles.py
    - Fields: 26

282. **Fludrocortisone**
    - Nhóm: Endocrinology - Mineralocorticoid
    - File: drug_modules\endocrinology_other\corticosteroids\short_intermediate_acting.py
    - Fields: 23

283. **Flumazenil**
    - Nhóm: Emergency - Benzodiazepine Antagonist
    - File: drug_modules\emergency\benzodiazepine_antagonists.py
    - Fields: 23

284. **Fluoxetine**
    - Nhóm: Psychiatry - SSRI (Selective Serotonin Reuptake Inhibitor)
    - File: drug_modules\neurological\ssri_selective_serotonin_reuptake_inhibitors.py
    - Fields: 24

285. **Fluphenazine**
    - Nhóm: Psychiatry - Antipsychotic (Typical)
    - File: drug_modules\psychiatry_other\antipsychotics.py
    - Fields: 24

286. **Fluticasone inhaled**
    - Nhóm: Respiratory - Inhaled Corticosteroid (ICS)
    - File: drug_modules\respiratory\inhaled_corticosteroid_icss.py
    - Fields: 23

287. **Fluticasone/Salmeterol inhaler**
    - Nhóm: Respiratory - Fixed-dose Combination (ICS/LABA)
    - File: drug_modules\respiratory\combination_inhalers.py
    - Fields: 25

288. **Fluticasone/Umeclidinium/Vilanterol inhaler**
    - Nhóm: Respiratory - Fixed-dose Combination (ICS/LAMA/LABA)
    - File: drug_modules\respiratory\combination_inhalers.py
    - Fields: 25

289. **Fluvastatin**
    - Nhóm: Cardiovascular - Statin (HMG-CoA Reductase Inhibitor)
    - File: drug_modules\cardiovascular\statins.py
    - Fields: 26

290. **Fluvoxamine**
    - Nhóm: Psychiatry - SSRI (Selective Serotonin Reuptake Inhibitor)
    - File: drug_modules\psychiatry_other\ssris.py
    - Fields: 24

291. **Folic Acid**
    - Nhóm: Hematology - Vitamin
    - File: drug_modules\miscellaneous\vitamins.py
    - Fields: 24

292. **Folic acid**
    - Nhóm: Vitamins/Supplements - Folate
    - File: drug_modules\supportive\folates.py
    - Fields: 26

293. **Fondaparinux**
    - Nhóm: Cardiovascular - Anticoagulant (Factor Xa Inhibitor)
    - File: drug_modules\cardiovascular\anticoagulants.py
    - Fields: 23

294. **Formoterol**
    - Nhóm: Respiratory - Long-acting Beta-2 Agonist (LABA)
    - File: drug_modules\respiratory\long_acting_beta_2_agonist_labas.py
    - Fields: 23

295. **Fosfomycin**
    - Nhóm: Antibiotic - Phosphonic Acid
    - File: drug_modules\antimicrobial\antibiotics\others.py
    - Fields: 27

296. **Fosphenytoin**
    - Nhóm: Neurology - Anticonvulsant (Phenytoin Prodrug)
    - File: drug_modules\neurological\anticonvulsants.py
    - Fields: 23

297. **Fremanezumab**
    - Nhóm: Neurology - Anti-CGRP Monoclonal Antibody
    - File: drug_modules\neurological\migraine_cgrp_drugs.py
    - Fields: 24

298. **Furosemide**
    - Nhóm: Cardiovascular - Loop Diuretic
    - File: drug_modules\cardiovascular\diuretics.py
    - Fields: 25

299. **Fusidic Acid**
    - Nhóm: Dermatology - Topical Antibiotic
    - File: drug_modules\dermatology.py
    - Fields: 23

300. **Fusidic acid/Betamethasone topical**
    - Nhóm: Dermatology - Topical Combination (Antibiotic + Corticosteroid)
    - File: drug_modules\dermatology.py
    - Fields: 23

301. **Gabapentin**
    - Nhóm: Neurology - Anticonvulsant (Alpha-2-delta ligand)
    - File: drug_modules\neurological\anticonvulsant_alpha_2_delta_ligands.py
    - Fields: 24

302. **Galcanezumab**
    - Nhóm: Neurology - Anti-CGRP Monoclonal Antibody
    - File: drug_modules\neurological\migraine_cgrp_drugs.py
    - Fields: 24

303. **Ganciclovir**
    - Nhóm: Infectious Disease - Antiviral
    - File: drug_modules\antimicrobial\antivirals\cmv.py
    - Fields: 25

304. **Ganciclovir eye drops**
    - Nhóm: Ophthalmology - Antiviral (CMV)
    - File: drug_modules\ophthalmology.py
    - Fields: 25

305. **Gefitinib**
    - Nhóm: Oncology - EGFR Tyrosine Kinase Inhibitor
    - File: drug_modules\oncology\targeted_therapy_tkis.py
    - Fields: 23

306. **Gemcitabine**
    - Nhóm: Oncology - Antimetabolite
    - File: drug_modules\oncology\antimetabolites.py
    - Fields: 23

307. **Gemfibrozil**
    - Nhóm: Cardiovascular - Fibrate (PPAR-alpha Agonist)
    - File: drug_modules\cardiovascular\triglyceride_lowering.py
    - Fields: 23

308. **Gemifloxacin**
    - Nhóm: Antibiotic - Fluoroquinolone
    - File: drug_modules\infectious_other\fluoroquinolones.py
    - Fields: 23

309. **Gentamicin**
    - Nhóm: Antibiotic - Aminoglycoside
    - File: drug_modules\antimicrobial\antibiotics\aminoglycosides.py
    - Fields: 26

310. **Gentamicin eye drops**
    - Nhóm: Ophthalmology - Antibiotic (Aminoglycoside)
    - File: drug_modules\ophthalmology.py
    - Fields: 23

311. **Gentamicin/Betamethasone/Clotrimazole topical**
    - Nhóm: Dermatology - Topical Combination (Antibiotic + Corticosteroid + Antifungal)
    - File: drug_modules\dermatology.py
    - Fields: 26

312. **Ginkgo biloba extract**
    - Nhóm: Neurology - Herbal cerebral vasomodulator (Ginkgo biloba)
    - File: drug_modules\neurological\cerebral_circulation.py
    - Fields: 24

313. **Ginkgo biloba/Vinpocetine**
    - Nhóm: Neurology - Combination (Herbal vasomodulator + Cerebral vasodilator)
    - File: drug_modules\neurological\neurological_combinations.py
    - Fields: 25

314. **Glibenclamide**
    - Nhóm: Diabetes - Sulfonylurea
    - File: drug_modules\diabetes\sulfonylureas.py
    - Fields: 29

315. **Gliclazide**
    - Nhóm: Diabetes - Sulfonylurea
    - File: drug_modules\diabetes\sulfonylureas.py
    - Fields: 29

316. **Glimepiride**
    - Nhóm: Diabetes - Sulfonylurea (3rd Generation)
    - File: drug_modules\diabetes\sulfonylureas.py
    - Fields: 25

317. **Glycopyrronium**
    - Nhóm: Respiratory - Anticholinergic (Long-acting)
    - File: drug_modules\respiratory\anticholinergic_long_actings.py
    - Fields: 23

318. **Golimumab**
    - Nhóm: Biological - Monoclonal Antibody (anti-TNF-α)
    - File: drug_modules\miscellaneous\biological_drugs.py
    - Fields: 25

319. **Granisetron**
    - Nhóm: Oncology - Anti-emetic (5-HT3 Antagonist)
    - File: drug_modules\oncology\anti_emetic_5_ht3_antagonists.py
    - Fields: 23

320. **Guselkumab**
    - Nhóm: Biological - Monoclonal Antibody (anti-IL-23)
    - File: drug_modules\miscellaneous\biological_drugs.py
    - Fields: 25

321. **Haloperidol**
    - Nhóm: Psychiatry - Antipsychotic (Typical)
    - File: drug_modules\psychiatry_other\antipsychotics.py
    - Fields: 24

322. **Heparin**
    - Nhóm: Hematology - Anticoagulant (Unfractionated Heparin)
    - File: drug_modules\hematology.py
    - Fields: 24

323. **High-intensity statin (đột quỵ/TIA)**
    - Nhóm: Cardiovascular - Statin (high-intensity, secondary prevention stroke/TIA)
    - File: drug_modules\cardiovascular_other\statins.py
    - Fields: 24

324. **Hydralazine**
    - Nhóm: Cardiovascular - Direct Vasodilator
    - File: drug_modules\cardiovascular\vasodilators.py
    - Fields: 23

325. **Hydrochlorothiazide**
    - Nhóm: Cardiovascular - Thiazide Diuretic
    - File: drug_modules\cardiovascular\diuretics.py
    - Fields: 25

326. **Hydrocodone**
    - Nhóm: Analgesic - Opioid Agonist
    - File: drug_modules\analgesics\opioid_agonists.py
    - Fields: 23

327. **Hydrocortisone**
    - Nhóm: Endocrinology - Corticosteroid
    - File: drug_modules\endocrinology_other\corticosteroids\short_intermediate_acting.py
    - Fields: 22

328. **Hydrocortisone topical**
    - Nhóm: Dermatology - Topical Corticosteroid (Low Potency)
    - File: drug_modules\dermatology.py
    - Fields: 25

329. **Hydromorphone**
    - Nhóm: Analgesic - Opioid Agonist (Strong)
    - File: drug_modules\analgesics\opioid_agonist_strongs.py
    - Fields: 25

330. **Hydroxychloroquine**
    - Nhóm: Infectious Disease - Antimalarial/Antirheumatic
    - File: drug_modules\infectious_other\antimalarials.py
    - Fields: 23

331. **Hydroxyzine**
    - Nhóm: Allergy - Antihistamine (H1 Antagonist, 1st generation)
    - File: drug_modules\supportive\antihistamine_h1_antagonist_1st_generations.py
    - Fields: 24

332. **Hyoscine butylbromide**
    - Nhóm: Gastrointestinal - Antispasmodic (Anticholinergic)
    - File: drug_modules\gastrointestinal\antispasmodics.py
    - Fields: 25

333. **Ibandronate**
    - Nhóm: Endocrinology - Bisphosphonate (Osteoporosis)
    - File: drug_modules\endocrinology_other\osteoporosis_bisphosphonates.py
    - Fields: 24

334. **Ibuprofen**
    - Nhóm: Analgesic - NSAID
    - File: drug_modules\analgesics\nsaids.py
    - Fields: 29

335. **Ibutilide**
    - Nhóm: Cardiovascular - Antiarrhythmic (Class III)
    - File: drug_modules\cardiovascular\antiarrhythmics.py
    - Fields: 22

336. **Icosapent ethyl**
    - Nhóm: Cardiovascular - Omega-3 Fatty Acid (EPA Ethyl Ester)
    - File: drug_modules\cardiovascular\triglyceride_lowering.py
    - Fields: 23

337. **Idarucizumab**
    - Nhóm: Hematology - DOAC Reversal Agent (Dabigatran)
    - File: drug_modules\hematology.py
    - Fields: 26

338. **Ifosfamide**
    - Nhóm: Oncology - Alkylating Agent
    - File: drug_modules\oncology\alkylating_agents.py
    - Fields: 23

339. **Ilaprazole**
    - Nhóm: Gastrointestinal - Proton Pump Inhibitor (PPI)
    - File: drug_modules\gastrointestinal\proton_pump_inhibitor_ppis.py
    - Fields: 24

340. **Imatinib**
    - Nhóm: Oncology - BCR-ABL Tyrosine Kinase Inhibitor
    - File: drug_modules\oncology\targeted_therapy_tkis.py
    - Fields: 23

341. **Imipenem-cilastatin**
    - Nhóm: Antibiotic - Carbapenem
    - File: drug_modules\antimicrobial\antibiotics\beta_lactams.py
    - Fields: 31

342. **Inclisiran**
    - Nhóm: Cardiovascular - PCSK9 Inhibitor (siRNA)
    - File: drug_modules\cardiovascular\pcsk9_inhibitors.py
    - Fields: 22

343. **Indacaterol**
    - Nhóm: Respiratory - Long-acting Beta-2 Agonist (LABA)
    - File: drug_modules\respiratory\long_acting_beta_2_agonist_labas.py
    - Fields: 23

344. **Indapamide**
    - Nhóm: Cardiovascular - Thiazide-like Diuretic
    - File: drug_modules\cardiovascular\diuretics.py
    - Fields: 22

345. **Indomethacin**
    - Nhóm: Analgesic - NSAID
    - File: drug_modules\analgesics\nsaids.py
    - Fields: 23

346. **Infliximab**
    - Nhóm: Biological - Monoclonal Antibody (anti-TNF-α)
    - File: drug_modules\miscellaneous\biological_drugs.py
    - Fields: 25

347. **Insulin**
    - Nhóm: Diabetes - Insulin
    - File: drug_modules\diabetes\insulins.py
    - Fields: 26

348. **Insulin Aspart**
    - Nhóm: Diabetes - Rapid-Acting Insulin
    - File: drug_modules\diabetes\specific_insulins.py
    - Fields: 24

349. **Insulin Degludec**
    - Nhóm: Diabetes - Ultra-Long-Acting Insulin
    - File: drug_modules\diabetes\specific_insulins.py
    - Fields: 24

350. **Insulin Detemir**
    - Nhóm: Diabetes - Long-Acting Insulin
    - File: drug_modules\diabetes\specific_insulins.py
    - Fields: 24

351. **Insulin Glargine**
    - Nhóm: Diabetes - Long-Acting Insulin
    - File: drug_modules\diabetes\specific_insulins.py
    - Fields: 24

352. **Insulin Glulisine**
    - Nhóm: Diabetes - Rapid-Acting Insulin
    - File: drug_modules\diabetes\specific_insulins.py
    - Fields: 24

353. **Insulin Lispro**
    - Nhóm: Diabetes - Rapid-Acting Insulin
    - File: drug_modules\diabetes\specific_insulins.py
    - Fields: 24

354. **Insulin NPH**
    - Nhóm: Diabetes - Intermediate-Acting Insulin
    - File: drug_modules\diabetes\specific_insulins.py
    - Fields: 24

355. **Insulin Regular**
    - Nhóm: Diabetes - Short-Acting Insulin
    - File: drug_modules\diabetes\specific_insulins.py
    - Fields: 24

356. **Ipratropium**
    - Nhóm: Respiratory - Anticholinergic (Short-acting)
    - File: drug_modules\respiratory\anticholinergic_short_actings.py
    - Fields: 23

357. **Ipratropium/Salbutamol inhaler**
    - Nhóm: Respiratory - Fixed-dose Combination (SAMA/SABA)
    - File: drug_modules\respiratory\combination_inhalers.py
    - Fields: 25

358. **Irbesartan**
    - Nhóm: Cardiovascular - ARB (Angiotensin Receptor Blocker)
    - File: drug_modules\cardiovascular\arbs.py
    - Fields: 26

359. **Irinotecan**
    - Nhóm: Oncology - Topoisomerase Inhibitor
    - File: drug_modules\oncology\topoisomerase_inhibitors.py
    - Fields: 23

360. **Iron**
    - Nhóm: Vitamins/Supplements - Iron
    - File: drug_modules\supportive\irons.py
    - Fields: 25

361. **Isavuconazole**
    - Nhóm: Infectious Disease - Antifungal (Azole - Triazole, prodrug)
    - File: drug_modules\antimicrobial\antifungals\azoles.py
    - Fields: 25

362. **Isoniazid**
    - Nhóm: Infectious Disease - Antitubercular (First-line)
    - File: drug_modules\infectious_other\antituberculars.py
    - Fields: 26

363. **Isosorbide mononitrate**
    - Nhóm: Cardiovascular - Nitrate
    - File: drug_modules\cardiovascular\vasodilators.py
    - Fields: 23

364. **Isradipine**
    - Nhóm: Cardiovascular - Calcium Channel Blocker (Dihydropyridine)
    - File: drug_modules\cardiovascular\calcium_blockers\dihydropyridines.py
    - Fields: 27

365. **Istradefylline**
    - Nhóm: Neurology - Antiparkinsonian (Adenosine A2A Receptor Antagonist)
    - File: drug_modules\neurological\antiparkinsonian.py
    - Fields: 23

366. **Itraconazole**
    - Nhóm: Infectious Disease - Antifungal (Azole)
    - File: drug_modules\antimicrobial\antifungals\azoles.py
    - Fields: 26

367. **Ivabradine**
    - Nhóm: Cardiovascular - If Channel Inhibitor
    - File: drug_modules\cardiovascular\other_cv.py
    - Fields: 27

368. **Ivermectin**
    - Nhóm: Infectious Disease - Anthelmintic
    - File: drug_modules\infectious_other\anthelmintics.py
    - Fields: 26

369. **Ivermectin cream**
    - Nhóm: Dermatology - Topical Antiparasitic
    - File: drug_modules\dermatology.py
    - Fields: 23

370. **Ixekizumab**
    - Nhóm: Biological - Monoclonal Antibody (anti-IL-17A)
    - File: drug_modules\miscellaneous\biological_drugs.py
    - Fields: 25

371. **Ketamine**
    - Nhóm: Supportive - Dissociative anesthetic/analgesic (ICU/Procedural)
    - File: drug_modules\supportive\sedatives_anesthetics_icu.py
    - Fields: 26

372. **Ketoconazole topical**
    - Nhóm: Dermatology - Topical Antifungal
    - File: drug_modules\dermatology.py
    - Fields: 23

373. **Ketoprofen**
    - Nhóm: Analgesic - NSAID
    - File: drug_modules\analgesics\nsaids.py
    - Fields: 23

374. **Ketoprofen gel**
    - Nhóm: Dermatology - Topical NSAID
    - File: drug_modules\dermatology.py
    - Fields: 23

375. **Ketorolac**
    - Nhóm: Analgesic - NSAID
    - File: drug_modules\analgesics\nsaids.py
    - Fields: 25

376. **Ketorolac eye drops**
    - Nhóm: Ophthalmology - NSAID (Anti-inflammatory)
    - File: drug_modules\ophthalmology.py
    - Fields: 24

377. **Ketotifen eye drops**
    - Nhóm: Ophthalmology - Antihistamine/Mast Cell Stabilizer (Allergic Conjunctivitis)
    - File: drug_modules\ophthalmology.py
    - Fields: 23

378. **Labetalol**
    - Nhóm: Cardiovascular - Alpha-Beta Blocker
    - File: drug_modules\cardiovascular\other_cv.py
    - Fields: 27

379. **Lacidipine**
    - Nhóm: Cardiovascular - Calcium Channel Blocker (Dihydropyridine)
    - File: drug_modules\cardiovascular\calcium_blockers\dihydropyridines.py
    - Fields: 22

380. **Lacosamide**
    - Nhóm: Neurology - Anticonvulsant
    - File: drug_modules\neurological\anticonvulsants.py
    - Fields: 23

381. **Lactulose**
    - Nhóm: Gastrointestinal - Osmotic Laxative (Disaccharide)
    - File: drug_modules\gastrointestinal\laxatives.py
    - Fields: 25

382. **Lamivudine (3TC)**
    - Nhóm: Antiviral - Nucleoside reverse transcriptase inhibitor (NRTI)
    - File: drug_modules\antimicrobial\antivirals\hiv_arvs.py
    - Fields: 26

383. **Lamotrigine**
    - Nhóm: Neurology - Anticonvulsant
    - File: drug_modules\neurological\anticonvulsants.py
    - Fields: 22

384. **Lanadelumab**
    - Nhóm: Biological - Monoclonal Antibody (anti-plasma kallikrein)
    - File: drug_modules\miscellaneous\biological_drugs.py
    - Fields: 23

385. **Lansoprazole**
    - Nhóm: Gastrointestinal - Proton Pump Inhibitor (PPI)
    - File: drug_modules\gastrointestinal\proton_pump_inhibitor_ppis.py
    - Fields: 23

386. **Lasmiditan**
    - Nhóm: Analgesic - Antimigraine (5-HT1F Receptor Agonist)
    - File: drug_modules\analgesics\antimigraine_5_ht1_receptor_agonists.py
    - Fields: 24

387. **Latanoprost**
    - Nhóm: Ophthalmology - Prostaglandin Analog (Glaucoma)
    - File: drug_modules\ophthalmology.py
    - Fields: 23

388. **Lecanemab**
    - Nhóm: Neurology - Anti-amyloid Monoclonal Antibody
    - File: drug_modules\neurological\alzheimer_dementia_drugs.py
    - Fields: 24

389. **Ledipasvir**
    - Nhóm: Infectious Disease - Antiviral (HCV NS5A inhibitor)
    - File: drug_modules\antimicrobial\antivirals\hepatitis.py
    - Fields: 26

390. **Lefamulin**
    - Nhóm: Antibiotic - Pleuromutilin
    - File: drug_modules\antimicrobial\antibiotics\others.py
    - Fields: 23

391. **Leflunomide**
    - Nhóm: Rheumatology - Conventional DMARD (Pyrimidine Synthesis Inhibitor)
    - File: drug_modules\miscellaneous\dmards_rheumatology.py
    - Fields: 24

392. **Levamisole**
    - Nhóm: Infectious Disease - Anthelmintic
    - File: drug_modules\infectious_other\anthelmintics.py
    - Fields: 24

393. **Levetiracetam**
    - Nhóm: Neurology - Anticonvulsant
    - File: drug_modules\neurological\anticonvulsants.py
    - Fields: 23

394. **Levocetirizine**
    - Nhóm: Allergy - Antihistamine (H1 Antagonist, 2nd generation)
    - File: drug_modules\supportive\antihistamine_h1_antagonist_2nd_generations.py
    - Fields: 24

395. **Levodopa/Carbidopa**
    - Nhóm: Neurology - Antiparkinsonian (Dopamine Precursor + DOPA Decarboxylase Inhibitor)
    - File: drug_modules\neurological\antiparkinsonian.py
    - Fields: 22

396. **Levofloxacin**
    - Nhóm: Antibiotic - Fluoroquinolone
    - File: drug_modules\antimicrobial\antibiotics\fluoroquinolones.py
    - Fields: 34

397. **Levonorgestrel**
    - Nhóm: Obstetrics/Gynecology - Emergency Contraception
    - File: drug_modules\obstetrics_gynecology.py
    - Fields: 23

398. **Levothyroxine**
    - Nhóm: Endocrinology - Thyroid Hormone
    - File: drug_modules\metabolic\thyroid_hormones.py
    - Fields: 23

399. **Lidocaine**
    - Nhóm: Emergency - Local Anesthetic / Antiarrhythmic (Class IB)
    - File: drug_modules\emergency\local_anesthetic__antiarrhythmic_class_ibs.py
    - Fields: 23

400. **Linagliptin**
    - Nhóm: Diabetes - DPP-4 Inhibitor
    - File: drug_modules\diabetes\dpp_4_inhibitors.py
    - Fields: 25

401. **Linezolid**
    - Nhóm: Antibiotic - Oxazolidinone
    - File: drug_modules\antimicrobial\antibiotics\oxazolidinones.py
    - Fields: 31

402. **Linezolid (lao MDR/XDR)**
    - Nhóm: Infectious Disease - Oxazolidinone (Second-line antitubercular, MDR/XDR-TB)
    - File: drug_modules\infectious_other\antituberculars.py
    - Fields: 24

403. **Liraglutide**
    - Nhóm: Diabetes - GLP-1 Receptor Agonist
    - File: drug_modules\diabetes\glp1_agonists.py
    - Fields: 26

404. **Lisdexamfetamine**
    - Nhóm: Psychiatry - ADHD Medication (Stimulant - Prodrug)
    - File: drug_modules\psychiatry_other\adhd_anxiolytics.py
    - Fields: 23

405. **Lisinopril**
    - Nhóm: Cardiovascular - ACE Inhibitor
    - File: drug_modules\cardiovascular\ace_inhibitors.py
    - Fields: 30

406. **Lisinopril/Hydrochlorothiazide**
    - Nhóm: Cardiovascular - ACE Inhibitor + Diuretic (Fixed-Dose Combination)
    - File: drug_modules\cardiovascular\fixed_dose_combinations.py
    - Fields: 24

407. **Loperamide**
    - Nhóm: Gastrointestinal - Antidiarrheal
    - File: drug_modules\gastrointestinal\antidiarrheals.py
    - Fields: 23

408. **Loratadine**
    - Nhóm: Allergy - Antihistamine (H1 Antagonist, 2nd generation)
    - File: drug_modules\supportive\antihistamine_h1_antagonist_2nd_generations.py
    - Fields: 22

409. **Loratadine/Pseudoephedrine**
    - Nhóm: ENT - Combination (Oral Antihistamine + Decongestant)
    - File: drug_modules\ent_oral_nasal_combinations.py
    - Fields: 23

410. **Lorazepam**
    - Nhóm: Neurology - Benzodiazepine
    - File: drug_modules\neurological\benzodiazepines.py
    - Fields: 23

411. **Losartan**
    - Nhóm: Cardiovascular - ARB (Angiotensin Receptor Blocker)
    - File: drug_modules\cardiovascular\arbs.py
    - Fields: 30

412. **Losartan/Hydrochlorothiazide**
    - Nhóm: Cardiovascular - ARB + Diuretic (Fixed-Dose Combination)
    - File: drug_modules\cardiovascular\fixed_dose_combinations.py
    - Fields: 24

413. **Lovastatin**
    - Nhóm: Cardiovascular - Statin (HMG-CoA Reductase Inhibitor)
    - File: drug_modules\cardiovascular\statins.py
    - Fields: 26

414. **Lurasidone**
    - Nhóm: Psychiatry - Antipsychotic (Atypical)
    - File: drug_modules\psychiatry_other\antipsychotics.py
    - Fields: 24

415. **Magnesium oxide**
    - Nhóm: Emergency - Electrolyte (Magnesium Supplement)
    - File: drug_modules\emergency\electrolytes.py
    - Fields: 23

416. **Magnesium sulfate**
    - Nhóm: Emergency - Electrolyte
    - File: drug_modules\emergency\electrolytes.py
    - Fields: 23

417. **Mebendazole**
    - Nhóm: Infectious Disease - Anthelmintic
    - File: drug_modules\infectious_other\anthelmintics.py
    - Fields: 23

418. **Mebeverine**
    - Nhóm: Gastrointestinal - Antispasmodic (Direct smooth muscle relaxant)
    - File: drug_modules\gastrointestinal\antispasmodics.py
    - Fields: 25

419. **Medroxyprogesterone**
    - Nhóm: Obstetrics/Gynecology - Progestin Contraception (Injectable)
    - File: drug_modules\obstetrics_gynecology.py
    - Fields: 24

420. **Meloxicam**
    - Nhóm: Analgesic - NSAID
    - File: drug_modules\analgesics\nsaids.py
    - Fields: 25

421. **Memantine**
    - Nhóm: Neurology - NMDA Receptor Antagonist
    - File: drug_modules\neurological\alzheimer_dementia_drugs.py
    - Fields: 23

422. **Meperidine**
    - Nhóm: Analgesic - Opioid Agonist (Strong)
    - File: drug_modules\analgesics\opioid_agonist_strongs.py
    - Fields: 24

423. **Mepolizumab**
    - Nhóm: Respiratory - Biologics (anti-IL-5)
    - File: drug_modules\respiratory\respiratory_biologics.py
    - Fields: 23

424. **Meropenem**
    - Nhóm: Antibiotic - Carbapenem
    - File: drug_modules\antimicrobial\antibiotics\beta_lactams.py
    - Fields: 26

425. **Mesalazine**
    - Nhóm: Gastrointestinal - 5-ASA (Aminosalicylate)
    - File: drug_modules\gastrointestinal\ibd_5asa.py
    - Fields: 24

426. **Metaxalone**
    - Nhóm: Neurology - Muscle Relaxant (Skeletal)
    - File: drug_modules\neurological\muscle_relaxants.py
    - Fields: 22

427. **Metformin**
    - Nhóm: Diabetes - Biguanide
    - File: drug_modules\diabetes\biguanides.py
    - Fields: 29

428. **Metformin/Dapagliflozin**
    - Nhóm: Diabetes - Biguanide + SGLT2 Inhibitor (Fixed-Dose Combination)
    - File: drug_modules\diabetes\fixed_dose_combinations.py
    - Fields: 24

429. **Metformin/Empagliflozin**
    - Nhóm: Diabetes - Biguanide + SGLT2 Inhibitor (Fixed-Dose Combination)
    - File: drug_modules\diabetes\fixed_dose_combinations.py
    - Fields: 24

430. **Metformin/Glibenclamide**
    - Nhóm: Diabetes - Biguanide + Sulfonylurea (Fixed-Dose Combination)
    - File: drug_modules\diabetes\fixed_dose_combinations.py
    - Fields: 23

431. **Metformin/Pioglitazone**
    - Nhóm: Diabetes - Biguanide + Thiazolidinedione (Fixed-Dose Combination)
    - File: drug_modules\diabetes\fixed_dose_combinations.py
    - Fields: 23

432. **Metformin/Sitagliptin**
    - Nhóm: Diabetes - Biguanide + DPP-4 Inhibitor (Fixed-Dose Combination)
    - File: drug_modules\diabetes\fixed_dose_combinations.py
    - Fields: 24

433. **Methadone**
    - Nhóm: Analgesic - Opioid Agonist (Strong)
    - File: drug_modules\analgesics\opioid_agonist_strongs.py
    - Fields: 24

434. **Methimazole**
    - Nhóm: Endocrinology - Antithyroid (Thionamide)
    - File: drug_modules\metabolic\antithyroid.py
    - Fields: 23

435. **Methocarbamol**
    - Nhóm: Neurology - Muscle Relaxant (Skeletal)
    - File: drug_modules\neurological\muscle_relaxants.py
    - Fields: 22

436. **Methotrexate**
    - Nhóm: Rheumatology - Conventional DMARD (Antimetabolite, Folic Acid Antagonist)
    - File: drug_modules\miscellaneous\dmards_rheumatology.py
    - Fields: 24

437. **Methyldopa**
    - Nhóm: Cardiovascular - Central Alpha-2 Agonist
    - File: drug_modules\cardiovascular\other_cv.py
    - Fields: 23

438. **Methylergonovine**
    - Nhóm: Emergency - Obstetric uterotonic (Ergot alkaloid)
    - File: drug_modules\emergency\uterotonics.py
    - Fields: 23

439. **Methylphenidate**
    - Nhóm: Psychiatry - ADHD Medication (Stimulant)
    - File: drug_modules\psychiatry_other\adhd_anxiolytics.py
    - Fields: 23

440. **Methylprednisolone**
    - Nhóm: Endocrinology - Corticosteroid
    - File: drug_modules\endocrinology_other\corticosteroids\short_intermediate_acting.py
    - Fields: 22

441. **Metoclopramide**
    - Nhóm: Gastrointestinal - Prokinetic, Antiemetic
    - File: drug_modules\gastrointestinal\prokinetic_antiemetics.py
    - Fields: 23

442. **Metoprolol**
    - Nhóm: Cardiovascular - Beta-blocker
    - File: drug_modules\cardiovascular\beta_blockers\selective.py
    - Fields: 29

443. **Metronidazole**
    - Nhóm: Infectious Disease - Nitroimidazole Antibiotic
    - File: drug_modules\infectious_other\nitroimidazoles.py
    - Fields: 24

444. **Metronidazole (vaginal gel)**
    - Nhóm: Obstetrics/Gynecology - Nitroimidazole (Bacterial Vaginosis)
    - File: drug_modules\obstetrics_gynecology.py
    - Fields: 24

445. **Metronidazole topical**
    - Nhóm: Dermatology - Topical Antibiotic (Rosacea)
    - File: drug_modules\dermatology.py
    - Fields: 23

446. **Micafungin**
    - Nhóm: Infectious Disease - Antifungal (Echinocandin)
    - File: drug_modules\antimicrobial\antifungals\echinocandins.py
    - Fields: 25

447. **Miconazole (vaginal)**
    - Nhóm: Obstetrics/Gynecology - Antifungal (Vulvovaginal Candidiasis)
    - File: drug_modules\obstetrics_gynecology.py
    - Fields: 24

448. **Miconazole topical**
    - Nhóm: Dermatology - Topical Antifungal
    - File: drug_modules\dermatology.py
    - Fields: 23

449. **Miconazole/Hydrocortisone topical**
    - Nhóm: Dermatology - Topical Combination (Antifungal + Low-potency Corticosteroid)
    - File: drug_modules\dermatology.py
    - Fields: 24

450. **Midazolam (IV/ICU)**
    - Nhóm: Supportive - Benzodiazepine (IV Sedation/ICU)
    - File: drug_modules\supportive\sedatives_anesthetics_icu.py
    - Fields: 26

451. **Miglitol**
    - Nhóm: Diabetes - Alpha-Glucosidase Inhibitor
    - File: drug_modules\diabetes\alpha_glucosidase_inhibitors.py
    - Fields: 23

452. **Milrinone**
    - Nhóm: Emergency - Phosphodiesterase-3 Inhibitor (Inotrope)
    - File: drug_modules\emergency\catecholamine_alpha__beta_agonists.py
    - Fields: 25

453. **Minocycline**
    - Nhóm: Antibiotic - Tetracycline
    - File: drug_modules\antimicrobial\antibiotics\tetracyclines.py
    - Fields: 27

454. **Mirabegron**
    - Nhóm: Urology - Beta-3 Adrenergic Agonist (Overactive Bladder)
    - File: drug_modules\urology.py
    - Fields: 24

455. **Mirtazapine**
    - Nhóm: Psychiatry - Tetracyclic Antidepressant
    - File: drug_modules\psychiatry_other\antidepressants.py
    - Fields: 23

456. **Misoprostol**
    - Nhóm: Gastrointestinal - Prostaglandin E1 Analog
    - File: drug_modules\gastrointestinal\mucosal_protectants.py
    - Fields: 23

457. **Mometasone topical**
    - Nhóm: Dermatology - Topical Corticosteroid (High Potency)
    - File: drug_modules\dermatology.py
    - Fields: 23

458. **Montelukast**
    - Nhóm: Respiratory - Leukotriene Receptor Antagonist
    - File: drug_modules\respiratory\leukotriene_receptor_antagonists.py
    - Fields: 24

459. **Morphine**
    - Nhóm: Analgesic - Opioid Agonist (Strong)
    - File: drug_modules\analgesics\opioid_agonist_strongs.py
    - Fields: 25

460. **Moxifloxacin**
    - Nhóm: Antibiotic - Fluoroquinolone (4th Generation)
    - File: drug_modules\antimicrobial\antibiotics\fluoroquinolones.py
    - Fields: 31

461. **Moxifloxacin eye drops**
    - Nhóm: Ophthalmology - Fluoroquinolone Antibiotic
    - File: drug_modules\ophthalmology.py
    - Fields: 23

462. **Mupirocin topical**
    - Nhóm: Dermatology - Topical Antibiotic
    - File: drug_modules\dermatology.py
    - Fields: 23

463. **Mycophenolate**
    - Nhóm: Immunosuppressant - Antimetabolite
    - File: drug_modules\miscellaneous\immunosuppressants.py
    - Fields: 23

464. **Nadolol**
    - Nhóm: Cardiovascular - Beta-blocker (non-selective)
    - File: drug_modules\cardiovascular\beta_blockers\non_selective.py
    - Fields: 23

465. **Nafcillin**
    - Nhóm: Antibiotic - Penicillin (Anti-staphylococcal)
    - File: drug_modules\antimicrobial\antibiotics\penicillins.py
    - Fields: 19

466. **Naloxone**
    - Nhóm: Emergency - Opioid Antagonist
    - File: drug_modules\emergency\opioid_antagonists.py
    - Fields: 23

467. **Naltrexone**
    - Nhóm: Emergency - Opioid Antagonist
    - File: drug_modules\emergency\opioid_antagonists.py
    - Fields: 23

468. **Naproxen**
    - Nhóm: Analgesic - NSAID
    - File: drug_modules\analgesics\nsaids.py
    - Fields: 25

469. **Natalizumab**
    - Nhóm: Biological - Monoclonal Antibody (anti-integrin α4)
    - File: drug_modules\miscellaneous\biological_drugs.py
    - Fields: 23

470. **Nateglinide**
    - Nhóm: Diabetes - Meglitinide (Glinide)
    - File: drug_modules\diabetes\meglitinides.py
    - Fields: 23

471. **Nebivolol**
    - Nhóm: Cardiovascular - Beta-blocker (Selective - Beta-1)
    - File: drug_modules\cardiovascular\beta_blockers\selective.py
    - Fields: 26

472. **Nedocromil**
    - Nhóm: Respiratory - Mast Cell Stabilizer
    - File: drug_modules\respiratory\leukotriene_receptor_antagonists.py
    - Fields: 24

473. **Nepafenac eye drops**
    - Nhóm: Ophthalmology - NSAID Prodrug (Anti-inflammatory)
    - File: drug_modules\ophthalmology.py
    - Fields: 24

474. **Nesiritide**
    - Nhóm: Cardiovascular - Natriuretic Peptide (Vasodilator)
    - File: drug_modules\cardiovascular\vasodilators.py
    - Fields: 23

475. **Niacin**
    - Nhóm: Cardiovascular - Vitamin B3 / Lipid-lowering Agent
    - File: drug_modules\cardiovascular\triglyceride_lowering.py
    - Fields: 23

476. **Nicardipine**
    - Nhóm: Cardiovascular - Calcium Channel Blocker (Dihydropyridine)
    - File: drug_modules\cardiovascular\calcium_blockers\dihydropyridines.py
    - Fields: 23

477. **Nicergoline**
    - Nhóm: Neurology - Ergot-derived cerebral vasodilator
    - File: drug_modules\neurological\cerebral_circulation.py
    - Fields: 25

478. **Nifedipine**
    - Nhóm: Cardiovascular - Calcium Channel Blocker (Dihydropyridine)
    - File: drug_modules\cardiovascular\calcium_blockers\dihydropyridines.py
    - Fields: 26

479. **Nimesulide**
    - Nhóm: Analgesic - NSAID (COX-2 Preferential)
    - File: drug_modules\analgesics\nsaids.py
    - Fields: 23

480. **Nimodipine**
    - Nhóm: Neurology - Calcium channel blocker (cerebral vasospasm prophylaxis)
    - File: drug_modules\neurological\cerebral_circulation.py
    - Fields: 25

481. **Nisoldipine**
    - Nhóm: Cardiovascular - Calcium Channel Blocker (Dihydropyridine)
    - File: drug_modules\cardiovascular\calcium_blockers\dihydropyridines.py
    - Fields: 23

482. **Nitrofurantoin**
    - Nhóm: Antibiotic - Nitrofuran
    - File: drug_modules\antimicrobial\antibiotics\others.py
    - Fields: 26

483. **Nitroglycerin**
    - Nhóm: Cardiovascular - Nitrate
    - File: drug_modules\cardiovascular\vasodilators.py
    - Fields: 23

484. **Nitroprusside**
    - Nhóm: Cardiovascular - Vasodilator (Hypertensive Emergency)
    - File: drug_modules\cardiovascular\vasodilators.py
    - Fields: 23

485. **Nivolumab**
    - Nhóm: Biological - Monoclonal Antibody (anti-PD-1)
    - File: drug_modules\miscellaneous\biological_drugs.py
    - Fields: 23

486. **Norepinephrine**
    - Nhóm: Emergency - Catecholamine (Alpha & Beta Agonist)
    - File: drug_modules\emergency\catecholamine_alpha__beta_agonists.py
    - Fields: 21

487. **Norfloxacin**
    - Nhóm: Antibiotic - Fluoroquinolone
    - File: drug_modules\antimicrobial\antibiotics\fluoroquinolones.py
    - Fields: 16

488. **Nystatin**
    - Nhóm: Infectious Disease - Antifungal (Polyene)
    - File: drug_modules\antimicrobial\antifungals\polyenes.py
    - Fields: 23

489. **Ocrelizumab**
    - Nhóm: Biological - Monoclonal Antibody (anti-CD20)
    - File: drug_modules\miscellaneous\biological_drugs.py
    - Fields: 23

490. **Ofatumumab**
    - Nhóm: Neurology - Anti-CD20 Monoclonal Antibody for MS
    - File: drug_modules\neurological\multiple_sclerosis_drugs.py
    - Fields: 24

491. **Ofloxacin**
    - Nhóm: Antibiotic - Fluoroquinolone
    - File: drug_modules\antimicrobial\antibiotics\fluoroquinolones.py
    - Fields: 16

492. **Olanzapine**
    - Nhóm: Psychiatry - Antipsychotic (Atypical)
    - File: drug_modules\psychiatry_other\antipsychotics.py
    - Fields: 24

493. **Olanzapine/Fluoxetine**
    - Nhóm: Psychiatry - Combination (Atypical antipsychotic + SSRI)
    - File: drug_modules\neurological\neurological_combinations.py
    - Fields: 25

494. **Olmesartan**
    - Nhóm: Cardiovascular - ARB (Angiotensin Receptor Blocker)
    - File: drug_modules\cardiovascular\arbs.py
    - Fields: 26

495. **Olodaterol**
    - Nhóm: Respiratory - Long-acting Beta-2 Agonist (LABA)
    - File: drug_modules\respiratory\long_acting_beta_2_agonist_labas.py
    - Fields: 23

496. **Olopatadine eye drops**
    - Nhóm: Ophthalmology - Antihistamine/Mast Cell Stabilizer (Allergic Conjunctivitis)
    - File: drug_modules\ophthalmology.py
    - Fields: 23

497. **Omadacycline**
    - Nhóm: Antibiotic - Tetracycline (Next Generation)
    - File: drug_modules\antimicrobial\antibiotics\others.py
    - Fields: 23

498. **Omalizumab**
    - Nhóm: Respiratory - Biologics (anti-IgE)
    - File: drug_modules\respiratory\respiratory_biologics.py
    - Fields: 23

499. **Omega-3 acid ethyl esters**
    - Nhóm: Cardiovascular - Omega-3 Fatty Acids (EPA/DHA)
    - File: drug_modules\cardiovascular\triglyceride_lowering.py
    - Fields: 23

500. **Omeprazole**
    - Nhóm: Gastrointestinal - Proton Pump Inhibitor (PPI)
    - File: drug_modules\gastrointestinal\proton_pump_inhibitor_ppis.py
    - Fields: 26

501. **Ondansetron**
    - Nhóm: Gastrointestinal - Antiemetic (5-HT3 Antagonist)
    - File: drug_modules\gastrointestinal\antiemetic_5_ht3_antagonists.py
    - Fields: 23

502. **Opicapone**
    - Nhóm: Neurology - Antiparkinsonian (COMT Inhibitor)
    - File: drug_modules\neurological\antiparkinsonian.py
    - Fields: 23

503. **Oseltamivir**
    - Nhóm: Infectious Disease - Antiviral (Neuraminidase Inhibitor)
    - File: drug_modules\antimicrobial\antivirals\influenza.py
    - Fields: 24

504. **Oxacillin**
    - Nhóm: Antibiotic - Penicillin (Anti-staphylococcal)
    - File: drug_modules\antimicrobial\antibiotics\penicillins.py
    - Fields: 19

505. **Oxaliplatin**
    - Nhóm: Oncology - Platinum Compound
    - File: drug_modules\oncology\platinum_compounds.py
    - Fields: 24

506. **Oxcarbazepine**
    - Nhóm: Neurology - Anticonvulsant
    - File: drug_modules\neurological\anticonvulsants.py
    - Fields: 26

507. **Oxybutynin**
    - Nhóm: Urology - Anticholinergic (Overactive Bladder)
    - File: drug_modules\urology.py
    - Fields: 24

508. **Oxycodone**
    - Nhóm: Analgesic - Opioid Agonist (Strong)
    - File: drug_modules\analgesics\opioid_agonist_strongs.py
    - Fields: 23

509. **Oxytocin**
    - Nhóm: Emergency - Obstetric uterotonic (PPH prevention/treatment)
    - File: drug_modules\emergency\uterotonics.py
    - Fields: 24

510. **PAS (para-aminosalicylic acid)**
    - Nhóm: Infectious Disease - Second-line antitubercular (folate antagonist, MDR-TB)
    - File: drug_modules\infectious_other\antituberculars.py
    - Fields: 26

511. **Paclitaxel**
    - Nhóm: Oncology - Taxane
    - File: drug_modules\oncology\taxanes.py
    - Fields: 23

512. **Palonosetron**
    - Nhóm: Oncology - Anti-emetic (5-HT3 Antagonist)
    - File: drug_modules\oncology\anti_emetic_5_ht3_antagonists.py
    - Fields: 23

513. **Pamidronate**
    - Nhóm: Emergency - Electrolyte (Bisphosphonate)
    - File: drug_modules\emergency\electrolytes.py
    - Fields: 23

514. **Pantoprazole**
    - Nhóm: Gastrointestinal - Proton Pump Inhibitor
    - File: drug_modules\gastrointestinal\proton_pump_inhibitors.py
    - Fields: 26

515. **Paracetamol**
    - Nhóm: Analgesic/Antipyretic
    - File: drug_modules\analgesics\analgesic_antipyretic.py
    - Fields: 27

516. **Paracetamol/Carisoprodol**
    - Nhóm: Analgesic - Combination (Paracetamol + Muscle Relaxant)
    - File: drug_modules\analgesics\pain_muscle_relaxant_combinations.py
    - Fields: 23

517. **Paracetamol/Chlorzoxazone**
    - Nhóm: Analgesic - Combination (Paracetamol + Muscle Relaxant)
    - File: drug_modules\analgesics\pain_muscle_relaxant_combinations.py
    - Fields: 23

518. **Paracetamol/Methocarbamol**
    - Nhóm: Analgesic - Combination (Paracetamol + Muscle Relaxant)
    - File: drug_modules\analgesics\pain_muscle_relaxant_combinations.py
    - Fields: 23

519. **Paracetamol/Orphenadrine**
    - Nhóm: Analgesic - Combination (Paracetamol + Muscle Relaxant)
    - File: drug_modules\analgesics\pain_muscle_relaxant_combinations.py
    - Fields: 23

520. **Paroxetine**
    - Nhóm: Psychiatry - SSRI (Selective Serotonin Reuptake Inhibitor)
    - File: drug_modules\psychiatry_other\ssris.py
    - Fields: 24

521. **Pemafibrate**
    - Nhóm: Cardiovascular - Selective PPAR-alpha Modulator (Fibrate)
    - File: drug_modules\cardiovascular\triglyceride_lowering.py
    - Fields: 23

522. **Pembrolizumab**
    - Nhóm: Biological - Monoclonal Antibody (anti-PD-1)
    - File: drug_modules\miscellaneous\biological_drugs.py
    - Fields: 23

523. **Penicillin G**
    - Nhóm: Antibiotic - Penicillin (Natural)
    - File: drug_modules\antimicrobial\antibiotics\beta_lactams.py
    - Fields: 27

524. **Penicillin V**
    - Nhóm: Antibiotic - Beta-lactam (Penicillin, Oral)
    - File: drug_modules\infectious_other\beta_lactams.py
    - Fields: 24

525. **Perampanel**
    - Nhóm: Neurology - Anticonvulsant
    - File: drug_modules\neurological\anticonvulsants.py
    - Fields: 23

526. **Perindopril**
    - Nhóm: Cardiovascular - ACE Inhibitor
    - File: drug_modules\cardiovascular\ace_inhibitors.py
    - Fields: 26

527. **Permethrin topical**
    - Nhóm: Dermatology - Topical Antiparasitic
    - File: drug_modules\dermatology.py
    - Fields: 23

528. **Phenelzine**
    - Nhóm: Psychiatry - MAO Inhibitor (MAOI)
    - File: drug_modules\psychiatry_other\antidepressants.py
    - Fields: 23

529. **Phenobarbital**
    - Nhóm: Neurology - Anticonvulsant
    - File: drug_modules\neurological\anticonvulsants.py
    - Fields: 27

530. **Phenylephrine**
    - Nhóm: Emergency - Alpha-1 Adrenergic Agonist (Pure)
    - File: drug_modules\emergency\catecholamine_alpha__beta_agonists.py
    - Fields: 25

531. **Phenylephrine eye drops**
    - Nhóm: Ophthalmology - Alpha-1 Adrenergic Agonist (Mydriatic)
    - File: drug_modules\ophthalmology.py
    - Fields: 23

532. **Phenytoin**
    - Nhóm: Neurology - Anticonvulsant
    - File: drug_modules\neurological\anticonvulsants.py
    - Fields: 27

533. **Pilocarpine eye drops**
    - Nhóm: Ophthalmology - Miotic (Pupil Constriction, Glaucoma)
    - File: drug_modules\ophthalmology.py
    - Fields: 24

534. **Pimavanserin**
    - Nhóm: Neurology - Antiparkinsonian (5-HT2A Inverse Agonist)
    - File: drug_modules\neurological\antiparkinsonian.py
    - Fields: 23

535. **Pimecrolimus**
    - Nhóm: Dermatology - Topical Calcineurin Inhibitor
    - File: drug_modules\dermatology.py
    - Fields: 24

536. **Pimozide**
    - Nhóm: Psychiatry - Antipsychotic (Typical)
    - File: drug_modules\psychiatry_other\antipsychotics.py
    - Fields: 23

537. **Pioglitazone**
    - Nhóm: Diabetes - Thiazolidinedione (TZD)
    - File: drug_modules\diabetes\thiazolidinedione_tzds.py
    - Fields: 23

538. **Piperacillin-tazobactam**
    - Nhóm: Antibiotic - Penicillin/Beta-lactamase Inhibitor
    - File: drug_modules\antimicrobial\antibiotics\beta_lactams.py
    - Fields: 27

539. **Piracetam**
    - Nhóm: Neurology - Nootropic / Cerebral circulation enhancer
    - File: drug_modules\neurological\cerebral_circulation.py
    - Fields: 24

540. **Piracetam/Vinpocetine**
    - Nhóm: Neurology - Combination (Nootropic + Cerebral vasodilator)
    - File: drug_modules\neurological\neurological_combinations.py
    - Fields: 25

541. **Piroxicam**
    - Nhóm: Analgesic - NSAID
    - File: drug_modules\analgesics\nsaids.py
    - Fields: 23

542. **Pitavastatin**
    - Nhóm: Cardiovascular - Statin (HMG-CoA Reductase Inhibitor)
    - File: drug_modules\cardiovascular\statins.py
    - Fields: 26

543. **Plazomicin**
    - Nhóm: Antibiotic - Aminoglycoside (Next Generation)
    - File: drug_modules\antimicrobial\antibiotics\aminoglycosides.py
    - Fields: 23

544. **Plozasiran**
    - Nhóm: Cardiovascular - Apo C-III Inhibitor (RNA Interference)
    - File: drug_modules\cardiovascular\triglyceride_lowering.py
    - Fields: 23

545. **Polyethylene glycol 3350**
    - Nhóm: Gastrointestinal - Osmotic Laxative (PEG 3350)
    - File: drug_modules\gastrointestinal\laxatives.py
    - Fields: 25

546. **Polymyxin B**
    - Nhóm: Antibiotic - Polymyxin
    - File: drug_modules\antimicrobial\antibiotics\polymyxins.py
    - Fields: 26

547. **Polymyxin B/Trimethoprim eye drops**
    - Nhóm: Ophthalmology - Combination Antibiotic
    - File: drug_modules\ophthalmology.py
    - Fields: 23

548. **Posaconazole**
    - Nhóm: Infectious Disease - Antifungal (Azole - Triazole)
    - File: drug_modules\antimicrobial\antifungals\azoles.py
    - Fields: 26

549. **Potassium phosphate**
    - Nhóm: Emergency - Electrolyte (Phosphate Supplement)
    - File: drug_modules\emergency\electrolytes.py
    - Fields: 23

550. **Pramipexole**
    - Nhóm: Neurology - Antiparkinsonian (Dopamine Agonist)
    - File: drug_modules\neurological\antiparkinsonian.py
    - Fields: 23

551. **Prasugrel**
    - Nhóm: Cardiovascular - Antiplatelet (P2Y12 Inhibitor)
    - File: drug_modules\cardiovascular\anticoagulants.py
    - Fields: 27

552. **Pravastatin**
    - Nhóm: Cardiovascular - Statin (HMG-CoA Reductase Inhibitor)
    - File: drug_modules\cardiovascular\statins.py
    - Fields: 29

553. **Praziquantel**
    - Nhóm: Infectious Disease - Anthelmintic
    - File: drug_modules\infectious_other\anthelmintics.py
    - Fields: 24

554. **Prednisolone**
    - Nhóm: Endocrinology - Corticosteroid
    - File: drug_modules\endocrinology_other\corticosteroids\short_intermediate_acting.py
    - Fields: 22

555. **Prednisolone eye drops**
    - Nhóm: Ophthalmology - Corticosteroid (Anti-inflammatory)
    - File: drug_modules\ophthalmology.py
    - Fields: 26

556. **Prednisone**
    - Nhóm: Endocrinology - Corticosteroid (Glucocorticoid)
    - File: drug_modules\metabolic\corticosteroids.py
    - Fields: 24

557. **Pregabalin**
    - Nhóm: Neurology - Anticonvulsant (Alpha-2-delta ligand)
    - File: drug_modules\neurological\anticonvulsant_alpha_2_delta_ligands.py
    - Fields: 23

558. **Primaquine**
    - Nhóm: Infectious Disease - Antimalarial (8-aminoquinoline)
    - File: drug_modules\infectious_other\antimalarials.py
    - Fields: 25

559. **Primidone**
    - Nhóm: Neurology - Anticonvulsant
    - File: drug_modules\neurological\anticonvulsants.py
    - Fields: 23

560. **Probenecid**
    - Nhóm: Metabolism - Gout Medication (Uricosuric Agent)
    - File: drug_modules\miscellaneous\gout_medications.py
    - Fields: 24

561. **Procainamide**
    - Nhóm: Cardiovascular - Antiarrhythmic (Class IA)
    - File: drug_modules\cardiovascular\antiarrhythmics.py
    - Fields: 22

562. **Progesterone**
    - Nhóm: Obstetrics/Gynecology - Progestin Replacement Therapy
    - File: drug_modules\obstetrics_gynecology.py
    - Fields: 24

563. **Propafenone**
    - Nhóm: Cardiovascular - Antiarrhythmic (Class IC)
    - File: drug_modules\cardiovascular\antiarrhythmics.py
    - Fields: 22

564. **Propofol**
    - Nhóm: Supportive - Sedative/Anesthetic (ICU)
    - File: drug_modules\supportive\sedatives_anesthetics_icu.py
    - Fields: 26

565. **Propranolol**
    - Nhóm: Cardiovascular - Beta-blocker (non-selective)
    - File: drug_modules\cardiovascular\beta_blockers\non_selective.py
    - Fields: 26

566. **Propylthiouracil**
    - Nhóm: Endocrinology - Antithyroid (Thionamide)
    - File: drug_modules\metabolic\antithyroid.py
    - Fields: 23

567. **Protamine**
    - Nhóm: Hematology - Anticoagulant Reversal Agent
    - File: drug_modules\hematology.py
    - Fields: 26

568. **Pyrazinamide**
    - Nhóm: Infectious Disease - Antitubercular (First-line)
    - File: drug_modules\infectious_other\antituberculars.py
    - Fields: 26

569. **Quetiapine**
    - Nhóm: Psychiatry - Antipsychotic (Atypical)
    - File: drug_modules\psychiatry_other\antipsychotics.py
    - Fields: 24

570. **Quinidine**
    - Nhóm: Cardiovascular - Antiarrhythmic (Class IA)
    - File: drug_modules\cardiovascular\antiarrhythmics.py
    - Fields: 23

571. **Rabeprazole**
    - Nhóm: Gastrointestinal - Proton Pump Inhibitor
    - File: drug_modules\gastrointestinal\proton_pump_inhibitors.py
    - Fields: 23

572. **Raloxifene**
    - Nhóm: Endocrinology - SERM (Selective Estrogen Receptor Modulator)
    - File: drug_modules\endocrinology_other\osteoporosis_other.py
    - Fields: 24

573. **Ramipril**
    - Nhóm: Cardiovascular - ACE Inhibitor
    - File: drug_modules\cardiovascular\ace_inhibitors.py
    - Fields: 26

574. **Ranitidine**
    - Nhóm: Gastrointestinal - H2 Receptor Antagonist
    - File: drug_modules\gastrointestinal\h2_receptor_antagonists.py
    - Fields: 22

575. **Ravulizumab**
    - Nhóm: Biological - Monoclonal Antibody (anti-C5 Complement)
    - File: drug_modules\miscellaneous\biological_drugs.py
    - Fields: 25

576. **Remdesivir**
    - Nhóm: Infectious Disease - Antiviral (RNA Polymerase Inhibitor)
    - File: drug_modules\antimicrobial\antivirals\influenza.py
    - Fields: 29

577. **Repaglinide**
    - Nhóm: Diabetes - Meglitinide (Glinide)
    - File: drug_modules\diabetes\meglitinides.py
    - Fields: 23

578. **Reslizumab**
    - Nhóm: Biological - Monoclonal Antibody (anti-IL-5)
    - File: drug_modules\miscellaneous\biological_drugs.py
    - Fields: 25

579. **Ribavirin**
    - Nhóm: Infectious Disease - Antiviral
    - File: drug_modules\antimicrobial\antivirals\hepatitis.py
    - Fields: 26

580. **Rifabutin**
    - Nhóm: Infectious Disease - Antitubercular (Rifamycin, dùng trong HIV/TB và các phác đồ đặc biệt)
    - File: drug_modules\infectious_other\antituberculars.py
    - Fields: 26

581. **Rifampin**
    - Nhóm: Infectious Disease - Antitubercular (First-line, Rifamycin)
    - File: drug_modules\infectious_other\antituberculars.py
    - Fields: 26

582. **Rifapentine**
    - Nhóm: Infectious Disease - Antitubercular (Long-acting rifamycin)
    - File: drug_modules\infectious_other\antituberculars.py
    - Fields: 26

583. **Rilpivirine (RPV)**
    - Nhóm: Antiviral - Non-nucleoside reverse transcriptase inhibitor (NNRTI)
    - File: drug_modules\antimicrobial\antivirals\hiv_arvs.py
    - Fields: 26

584. **Rimegepant**
    - Nhóm: Neurology - Anti-CGRP Receptor Antagonist (Gepant)
    - File: drug_modules\neurological\migraine_cgrp_drugs.py
    - Fields: 23

585. **Risankizumab**
    - Nhóm: Biological - Monoclonal Antibody (anti-IL-23)
    - File: drug_modules\miscellaneous\biological_drugs.py
    - Fields: 25

586. **Risedronate**
    - Nhóm: Endocrinology - Bisphosphonate (Osteoporosis)
    - File: drug_modules\endocrinology_other\osteoporosis_bisphosphonates.py
    - Fields: 24

587. **Risperidone**
    - Nhóm: Psychiatry - Antipsychotic (Atypical)
    - File: drug_modules\psychiatry_other\antipsychotics.py
    - Fields: 24

588. **Ritonavir (low-dose booster)**
    - Nhóm: Pharmacokinetic booster (CYP3A inhibitor; PI at high dose)
    - File: drug_modules\antimicrobial\antivirals\hiv_arvs.py
    - Fields: 26

589. **Rituximab**
    - Nhóm: Biological - Monoclonal Antibody (anti-CD20)
    - File: drug_modules\miscellaneous\biological_drugs.py
    - Fields: 25

590. **Rivaroxaban**
    - Nhóm: Cardiovascular - Anticoagulant (Direct Factor Xa Inhibitor - DOAC)
    - File: drug_modules\cardiovascular\anticoagulants.py
    - Fields: 26

591. **Rivastigmine**
    - Nhóm: Neurology - Cholinesterase Inhibitor
    - File: drug_modules\neurological\alzheimer_dementia_drugs.py
    - Fields: 23

592. **Rizatriptan**
    - Nhóm: Analgesic - Antimigraine (5-HT1 Receptor Agonist)
    - File: drug_modules\analgesics\antimigraine_5_ht1_receptor_agonists.py
    - Fields: 23

593. **Rocuronium**
    - Nhóm: Emergency - Non-depolarizing Neuromuscular Blocker (Aminosteroid)
    - File: drug_modules\emergency\neuromuscular_blockers.py
    - Fields: 25

594. **Roflumilast**
    - Nhóm: Respiratory - PDE-4 Inhibitor (Anti-inflammatory)
    - File: drug_modules\respiratory\pde4_inhibitors.py
    - Fields: 23

595. **Romiplostim**
    - Nhóm: Hematology - TPO Mimetic
    - File: drug_modules\hematology.py
    - Fields: 26

596. **Romosozumab**
    - Nhóm: Endocrinology - Sclerostin Inhibitor (Osteoporosis - Anabolic)
    - File: drug_modules\endocrinology_other\osteoporosis_other.py
    - Fields: 24

597. **Ropinirole**
    - Nhóm: Neurology - Antiparkinsonian (Dopamine Agonist)
    - File: drug_modules\neurological\antiparkinsonian.py
    - Fields: 22

598. **Rosiglitazone**
    - Nhóm: Diabetes - Thiazolidinedione (TZD)
    - File: drug_modules\diabetes\thiazolidinedione_tzds.py
    - Fields: 23

599. **Rosuvastatin**
    - Nhóm: Cardiovascular - Statin (HMG-CoA Reductase Inhibitor)
    - File: drug_modules\cardiovascular\statins.py
    - Fields: 29

600. **Sacituzumab govitecan**
    - Nhóm: Oncology - Antibody-Drug Conjugate (ADC)
    - File: drug_modules\oncology\monoclonal_antibodies_adcs.py
    - Fields: 24

601. **Sacubitril-valsartan**
    - Nhóm: Cardiovascular - ARNI (Angiotensin Receptor-Neprilysin Inhibitor)
    - File: drug_modules\cardiovascular\other_cv.py
    - Fields: 29

602. **Safinamide**
    - Nhóm: Neurology - Antiparkinsonian (MAO-B Inhibitor + Glutamate Release Inhibitor)
    - File: drug_modules\neurological\antiparkinsonian.py
    - Fields: 23

603. **Salbutamol**
    - Nhóm: Respiratory - Beta-2 Agonist (Short-acting)
    - File: drug_modules\miscellaneous\beta_2_agonist_short_actings.py
    - Fields: 23

604. **Salicylic Acid**
    - Nhóm: Dermatology - Topical Keratolytic
    - File: drug_modules\dermatology.py
    - Fields: 23

605. **Salmeterol**
    - Nhóm: Respiratory - Long-acting Beta-2 Agonist (LABA)
    - File: drug_modules\respiratory\long_acting_beta_2_agonist_labas.py
    - Fields: 23

606. **Sarilumab**
    - Nhóm: Biological - Monoclonal Antibody (anti-IL-6R)
    - File: drug_modules\miscellaneous\biological_drugs.py
    - Fields: 25

607. **Saxagliptin**
    - Nhóm: Diabetes - DPP-4 Inhibitor
    - File: drug_modules\diabetes\dpp_4_inhibitors.py
    - Fields: 25

608. **Secukinumab**
    - Nhóm: Biological - Monoclonal Antibody (anti-IL-17A)
    - File: drug_modules\miscellaneous\biological_drugs.py
    - Fields: 25

609. **Semaglutide**
    - Nhóm: Diabetes - GLP-1 Receptor Agonist
    - File: drug_modules\diabetes\glp1_agonists.py
    - Fields: 26

610. **Senna (sennosides)**
    - Nhóm: Gastrointestinal - Stimulant Laxative (Anthraquinone)
    - File: drug_modules\gastrointestinal\laxatives.py
    - Fields: 25

611. **Sertraline**
    - Nhóm: Psychiatry - SSRI (Selective Serotonin Reuptake Inhibitor)
    - File: drug_modules\psychiatry_other\ssris.py
    - Fields: 24

612. **Sildenafil**
    - Nhóm: Urology - PDE-5 Inhibitor (Erectile Dysfunction)
    - File: drug_modules\urology.py
    - Fields: 26

613. **Silodosin**
    - Nhóm: Urology - Alpha-1 Adrenergic Blocker (BPH, Selective)
    - File: drug_modules\urology.py
    - Fields: 25

614. **Simethicone**
    - Nhóm: Gastrointestinal - Antiflatulent (Chống đầy hơi, chống sủi bọt)
    - File: drug_modules\gastrointestinal\antiflatulents.py
    - Fields: 24

615. **Simvastatin**
    - Nhóm: Cardiovascular - Statin
    - File: drug_modules\cardiovascular\statins.py
    - Fields: 26

616. **Sitagliptin**
    - Nhóm: Diabetes - DPP-4 Inhibitor
    - File: drug_modules\diabetes\dpp_4_inhibitors.py
    - Fields: 29

617. **Sodium bicarbonate**
    - Nhóm: Emergency - Electrolyte
    - File: drug_modules\emergency\electrolytes.py
    - Fields: 23

618. **Sodium phosphate**
    - Nhóm: Emergency - Electrolyte (Phosphate Supplement)
    - File: drug_modules\emergency\electrolytes.py
    - Fields: 23

619. **Sodium polystyrene sulfonate**
    - Nhóm: Emergency - Electrolyte (Potassium Binder)
    - File: drug_modules\emergency\electrolytes.py
    - Fields: 23

620. **Sofosbuvir**
    - Nhóm: Infectious Disease - Antiviral (HCV NS5B inhibitor)
    - File: drug_modules\antimicrobial\antivirals\hepatitis.py
    - Fields: 26

621. **Sofosbuvir/Velpatasvir**
    - Nhóm: Infectious Disease - Antiviral (HCV NS5B + NS5A inhibitor FDC)
    - File: drug_modules\antimicrobial\antivirals\hepatitis.py
    - Fields: 26

622. **Solifenacin**
    - Nhóm: Urology - Anticholinergic (Overactive Bladder)
    - File: drug_modules\urology.py
    - Fields: 26

623. **Sotagliflozin**
    - Nhóm: Cardiovascular/Diabetes - Dual SGLT1/2 Inhibitor
    - File: drug_modules\cardiovascular\other_cv.py
    - Fields: 24

624. **Sotalol**
    - Nhóm: Cardiovascular - Antiarrhythmic (Class III)
    - File: drug_modules\cardiovascular\antiarrhythmics.py
    - Fields: 23

625. **Sparfloxacin**
    - Nhóm: Antibiotic - Fluoroquinolone
    - File: drug_modules\infectious_other\fluoroquinolones.py
    - Fields: 23

626. **Spironolactone**
    - Nhóm: Cardiovascular - Aldosterone Antagonist (Potassium-sparing Diuretic)
    - File: drug_modules\cardiovascular\diuretics.py
    - Fields: 30

627. **Streptomycin**
    - Nhóm: Infectious Disease - Antitubercular (Injectable aminoglycoside, second-line in many regimens)
    - File: drug_modules\infectious_other\antituberculars.py
    - Fields: 26

628. **Succinylcholine**
    - Nhóm: Emergency - Depolarizing Neuromuscular Blocker
    - File: drug_modules\emergency\neuromuscular_blockers.py
    - Fields: 25

629. **Sucralfate**
    - Nhóm: Gastrointestinal - Mucosal Protectant
    - File: drug_modules\gastrointestinal\mucosal_protectants.py
    - Fields: 23

630. **Sulfasalazine**
    - Nhóm: Gastrointestinal - 5-ASA (Aminosalicylate prodrug) + Sulfonamide
    - File: drug_modules\gastrointestinal\ibd_5asa.py
    - Fields: 24

631. **Sumatriptan**
    - Nhóm: Analgesic - Antimigraine (5-HT1 Receptor Agonist)
    - File: drug_modules\analgesics\antimigraine_5_ht1_receptor_agonists.py
    - Fields: 23

632. **Tacrolimus**
    - Nhóm: Immunosuppressant - Calcineurin Inhibitor
    - File: drug_modules\miscellaneous\immunosuppressants.py
    - Fields: 25

633. **Tacrolimus topical**
    - Nhóm: Dermatology - Topical Calcineurin Inhibitor
    - File: drug_modules\dermatology.py
    - Fields: 26

634. **Tadalafil**
    - Nhóm: Urology - PDE-5 Inhibitor (Erectile Dysfunction/BPH)
    - File: drug_modules\urology.py
    - Fields: 26

635. **Tamoxifen**
    - Nhóm: Oncology - Selective Estrogen Receptor Modulator (SERM)
    - File: drug_modules\oncology\hormone_therapy.py
    - Fields: 23

636. **Tamsulosin**
    - Nhóm: Urology - Alpha-1 Adrenergic Blocker (BPH)
    - File: drug_modules\urology.py
    - Fields: 25

637. **Tapentadol**
    - Nhóm: Analgesic - Opioid Agonist (Dual Mechanism)
    - File: drug_modules\analgesics\opioid_agonists.py
    - Fields: 23

638. **Tazarotene**
    - Nhóm: Dermatology - Topical Retinoid
    - File: drug_modules\dermatology.py
    - Fields: 23

639. **Tegoprazan**
    - Nhóm: Gastrointestinal - Potassium-Competitive Acid Blocker (PCAB)
    - File: drug_modules\gastrointestinal\pcab.py
    - Fields: 22

640. **Teicoplanin**
    - Nhóm: Antibiotic - Glycopeptide
    - File: drug_modules\antimicrobial\antibiotics\glycopeptides.py
    - Fields: 26

641. **Telmisartan**
    - Nhóm: Cardiovascular - ARB (Angiotensin Receptor Blocker)
    - File: drug_modules\cardiovascular\arbs.py
    - Fields: 30

642. **Tenecteplase**
    - Nhóm: Hematology - Fibrin-specific thrombolytic (tPA variant)
    - File: drug_modules\hematology.py
    - Fields: 25

643. **Tenofovir**
    - Nhóm: Infectious Disease - Antiviral (HBV, HIV)
    - File: drug_modules\antimicrobial\antivirals\hepatitis.py
    - Fields: 26

644. **Tenofovir alafenamide (TAF)**
    - Nhóm: Antiviral - Nucleotide reverse transcriptase inhibitor (NRTI)
    - File: drug_modules\antimicrobial\antivirals\hiv_arvs.py
    - Fields: 26

645. **Tenofovir alafenamide/Emtricitabine (TAF/FTC)**
    - Nhóm: Antiviral - NRTI fixed-dose combination
    - File: drug_modules\antimicrobial\antivirals\hiv_arvs.py
    - Fields: 26

646. **Tenofovir disoproxil fumarate (TDF)**
    - Nhóm: Antiviral - Nucleotide reverse transcriptase inhibitor (NRTI)
    - File: drug_modules\antimicrobial\antivirals\hiv_arvs.py
    - Fields: 26

647. **Tenofovir disoproxil fumarate/Emtricitabine (TDF/FTC)**
    - Nhóm: Antiviral - NRTI fixed-dose combination
    - File: drug_modules\antimicrobial\antivirals\hiv_arvs.py
    - Fields: 26

648. **Teplizumab**
    - Nhóm: Diabetes - T1DM Prevention (anti-CD3 Monoclonal Antibody)
    - File: drug_modules\diabetes\t1dm_prevention.py
    - Fields: 23

649. **Teprotumumab**
    - Nhóm: Oncology - Anti-IGF-1R Monoclonal Antibody
    - File: drug_modules\oncology\monoclonal_antibodies_adcs.py
    - Fields: 24

650. **Terbinafine topical**
    - Nhóm: Dermatology - Topical Antifungal
    - File: drug_modules\dermatology.py
    - Fields: 23

651. **Terbutaline**
    - Nhóm: Respiratory - Short-acting Beta-2 Agonist (SABA)
    - File: drug_modules\respiratory\short_acting_beta_2_agonist_sabas.py
    - Fields: 22

652. **Teriparatide**
    - Nhóm: Endocrinology - PTH Analog (Osteoporosis - Anabolic)
    - File: drug_modules\endocrinology_other\osteoporosis_other.py
    - Fields: 24

653. **Testosterone**
    - Nhóm: Endocrinology - Androgen (Sex Hormone)
    - File: drug_modules\endocrinology_other\sex_hormones.py
    - Fields: 23

654. **Tetrabenazine**
    - Nhóm: Neurology - Movement Disorders (VMAT2 Inhibitor)
    - File: drug_modules\neurological\antiparkinsonian.py
    - Fields: 23

655. **Tetracycline**
    - Nhóm: Antibiotic - Tetracycline
    - File: drug_modules\antimicrobial\antibiotics\tetracyclines.py
    - Fields: 27

656. **Tezepelumab**
    - Nhóm: Biological - Monoclonal Antibody (anti-TSLP)
    - File: drug_modules\miscellaneous\biological_drugs.py
    - Fields: 25

657. **Theophylline**
    - Nhóm: Respiratory - Methylxanthine (Bronchodilator)
    - File: drug_modules\respiratory\methylxanthines.py
    - Fields: 24

658. **Thiopental**
    - Nhóm: Supportive - Barbiturate Anesthetic (ICU)
    - File: drug_modules\supportive\sedatives_anesthetics_icu.py
    - Fields: 25

659. **Ticagrelor**
    - Nhóm: Cardiovascular - Antiplatelet (P2Y12 Inhibitor)
    - File: drug_modules\cardiovascular\anticoagulants.py
    - Fields: 27

660. **Ticlopidine**
    - Nhóm: Cardiovascular - Antiplatelet
    - File: drug_modules\cardiovascular_other\antiplatelets.py
    - Fields: 27

661. **Tigecycline**
    - Nhóm: Antibiotic - Glycylcycline (Tetracycline derivative)
    - File: drug_modules\infectious_other\tetracyclines.py
    - Fields: 23

662. **Timolol**
    - Nhóm: Cardiovascular - Beta-blocker (non-selective)
    - File: drug_modules\cardiovascular\beta_blockers\non_selective.py
    - Fields: 23

663. **Timolol eye drops**
    - Nhóm: Ophthalmology - Beta-blocker (Glaucoma)
    - File: drug_modules\ophthalmology.py
    - Fields: 23

664. **Tiotropium**
    - Nhóm: Respiratory - Anticholinergic (Long-acting)
    - File: drug_modules\respiratory\anticholinergic_long_actings.py
    - Fields: 23

665. **Tiotropium/Olodaterol inhaler**
    - Nhóm: Respiratory - Fixed-dose Combination (LAMA/LABA)
    - File: drug_modules\respiratory\combination_inhalers.py
    - Fields: 25

666. **Tirzepatide**
    - Nhóm: Diabetes - GIP/GLP-1 Dual Agonist
    - File: drug_modules\diabetes\glp1_agonists.py
    - Fields: 26

667. **Tizanidine**
    - Nhóm: Neurology - Muscle Relaxant (Alpha-2 Adrenergic Agonist)
    - File: drug_modules\neurological\muscle_relaxants.py
    - Fields: 22

668. **Tobramycin**
    - Nhóm: Antibiotic - Aminoglycoside
    - File: drug_modules\antimicrobial\antibiotics\aminoglycosides.py
    - Fields: 27

669. **Tobramycin eye drops**
    - Nhóm: Ophthalmology - Antibiotic (Aminoglycoside)
    - File: drug_modules\ophthalmology.py
    - Fields: 23

670. **Tocilizumab**
    - Nhóm: Biological - Monoclonal Antibody (anti-IL-6R)
    - File: drug_modules\miscellaneous\biological_drugs.py
    - Fields: 23

671. **Tofacitinib**
    - Nhóm: Gastrointestinal - JAK Inhibitor
    - File: drug_modules\gastrointestinal\jak_inhibitors.py
    - Fields: 24

672. **Tolterodine**
    - Nhóm: Urology - Anticholinergic (Overactive Bladder)
    - File: drug_modules\urology.py
    - Fields: 24

673. **Topiramate**
    - Nhóm: Neurology - Anticonvulsant
    - File: drug_modules\neurological\anticonvulsants.py
    - Fields: 22

674. **Topotecan**
    - Nhóm: Oncology - Topoisomerase Inhibitor
    - File: drug_modules\oncology\topoisomerase_inhibitors.py
    - Fields: 23

675. **Torsemide**
    - Nhóm: Cardiovascular - Loop Diuretic
    - File: drug_modules\cardiovascular\diuretics.py
    - Fields: 16

676. **Tramadol**
    - Nhóm: Analgesic - Opioid Agonist
    - File: drug_modules\analgesics\opioid_agonists.py
    - Fields: 24

677. **Tranexamic acid**
    - Nhóm: Hematology - Antifibrinolytic Agent
    - File: drug_modules\hematology.py
    - Fields: 24

678. **Tranylcypromine**
    - Nhóm: Psychiatry - MAO Inhibitor (MAOI)
    - File: drug_modules\psychiatry_other\antidepressants.py
    - Fields: 23

679. **Trastuzumab**
    - Nhóm: Biological - Monoclonal Antibody (anti-HER2)
    - File: drug_modules\miscellaneous\biological_drugs.py
    - Fields: 23

680. **Trastuzumab deruxtecan**
    - Nhóm: Oncology - Antibody-Drug Conjugate (ADC)
    - File: drug_modules\oncology\monoclonal_antibodies_adcs.py
    - Fields: 24

681. **Travoprost**
    - Nhóm: Ophthalmology - Prostaglandin Analog (Glaucoma)
    - File: drug_modules\ophthalmology.py
    - Fields: 23

682. **Trazodone**
    - Nhóm: Psychiatry - Serotonin Antagonist/Reuptake Inhibitor (SARI)
    - File: drug_modules\psychiatry_other\antidepressants.py
    - Fields: 23

683. **Tretinoin topical**
    - Nhóm: Dermatology - Topical Retinoid (Acne)
    - File: drug_modules\dermatology.py
    - Fields: 24

684. **Triamcinolone topical**
    - Nhóm: Dermatology - Topical Corticosteroid (Medium Potency)
    - File: drug_modules\dermatology.py
    - Fields: 23

685. **Trimebutine**
    - Nhóm: Gastrointestinal - Antispasmodic & Motility Modulator
    - File: drug_modules\gastrointestinal\antispasmodics.py
    - Fields: 25

686. **Trimethoprim-sulfamethoxazole**
    - Nhóm: Antibiotic - Sulfonamide
    - File: drug_modules\antimicrobial\antibiotics\sulfonamides.py
    - Fields: 27

687. **Tropicamide eye drops**
    - Nhóm: Ophthalmology - Mydriatic (Pupil Dilation)
    - File: drug_modules\ophthalmology.py
    - Fields: 23

688. **Ubrogepant**
    - Nhóm: Neurology - Anti-CGRP Receptor Antagonist (Gepant)
    - File: drug_modules\neurological\migraine_cgrp_drugs.py
    - Fields: 23

689. **Umeclidinium**
    - Nhóm: Respiratory - Anticholinergic (Long-acting)
    - File: drug_modules\respiratory\anticholinergic_long_actings.py
    - Fields: 23

690. **Umeclidinium/Vilanterol inhaler**
    - Nhóm: Respiratory - Fixed-dose Combination (LAMA/LABA)
    - File: drug_modules\respiratory\combination_inhalers.py
    - Fields: 25

691. **Upadacitinib**
    - Nhóm: Gastrointestinal - JAK Inhibitor
    - File: drug_modules\gastrointestinal\jak_inhibitors.py
    - Fields: 24

692. **Ustekinumab**
    - Nhóm: Biological - Monoclonal Antibody (anti-IL-12/23)
    - File: drug_modules\miscellaneous\biological_drugs.py
    - Fields: 23

693. **Valacyclovir**
    - Nhóm: Infectious Disease - Antiviral
    - File: drug_modules\antimicrobial\antivirals\herpes.py
    - Fields: 23

694. **Valproate**
    - Nhóm: Neurology - Anticonvulsant
    - File: drug_modules\neurological\anticonvulsants.py
    - Fields: 26

695. **Valsartan**
    - Nhóm: Cardiovascular - ARB (Angiotensin Receptor Blocker)
    - File: drug_modules\cardiovascular\arbs.py
    - Fields: 26

696. **Vancomycin**
    - Nhóm: Antibiotic - Glycopeptide
    - File: drug_modules\antimicrobial\antibiotics\glycopeptides.py
    - Fields: 27

697. **Vardenafil**
    - Nhóm: Urology - PDE-5 Inhibitor (Erectile Dysfunction)
    - File: drug_modules\urology.py
    - Fields: 24

698. **Vasopressin**
    - Nhóm: Emergency - Vasopressor (Non-catecholamine)
    - File: drug_modules\emergency\catecholamine_alpha__beta_agonists.py
    - Fields: 25

699. **Vecuronium**
    - Nhóm: Emergency - Non-depolarizing Neuromuscular Blocker (Aminosteroid)
    - File: drug_modules\emergency\neuromuscular_blockers.py
    - Fields: 25

700. **Vedolizumab**
    - Nhóm: Biological - Monoclonal Antibody (anti-integrin α4β7)
    - File: drug_modules\miscellaneous\biological_drugs.py
    - Fields: 23

701. **Venlafaxine**
    - Nhóm: Psychiatry - SNRI (Serotonin-Norepinephrine Reuptake Inhibitor)
    - File: drug_modules\psychiatry_other\snris.py
    - Fields: 22

702. **Verapamil**
    - Nhóm: Cardiovascular - Calcium Channel Blocker (Non-dihydropyridine)
    - File: drug_modules\cardiovascular\calcium_blockers\non_dihydropyridines.py
    - Fields: 23

703. **Vericiguat**
    - Nhóm: Cardiovascular - Soluble Guanylate Cyclase (sGC) Stimulator
    - File: drug_modules\cardiovascular\other_cv.py
    - Fields: 24

704. **Vilanterol**
    - Nhóm: Respiratory - Long-acting Beta-2 Agonist (LABA)
    - File: drug_modules\respiratory\long_acting_beta_2_agonist_labas.py
    - Fields: 23

705. **Vildagliptin**
    - Nhóm: Diabetes - DPP-4 Inhibitor
    - File: drug_modules\diabetes\dpp_4_inhibitors.py
    - Fields: 25

706. **Vincristine**
    - Nhóm: Oncology - Vinca Alkaloid
    - File: drug_modules\oncology\vinca_alkaloids.py
    - Fields: 23

707. **Vinpocetine**
    - Nhóm: Neurology - Cerebral vasodilator (controversial evidence)
    - File: drug_modules\neurological\cerebral_circulation.py
    - Fields: 24

708. **Vitamin B12**
    - Nhóm: Vitamins/Supplements - Vitamin B12
    - File: drug_modules\supportive\vitamin_b12s.py
    - Fields: 24

709. **Vitamin C**
    - Nhóm: Vitamins/Supplements - Vitamin C
    - File: drug_modules\miscellaneous\vitamins.py
    - Fields: 22

710. **Vitamin D**
    - Nhóm: Vitamins/Supplements - Vitamin D
    - File: drug_modules\supportive\vitamin_ds.py
    - Fields: 24

711. **Vitamin D3 (Cholecalciferol)**
    - Nhóm: Vitamins/Supplements - Vitamin D
    - File: drug_modules\miscellaneous\vitamins.py
    - Fields: 24

712. **Vitamin E**
    - Nhóm: Vitamins/Supplements - Vitamin E
    - File: drug_modules\miscellaneous\vitamins.py
    - Fields: 22

713. **Vitamin K**
    - Nhóm: Hematology - Anticoagulant Reversal Agent / Vitamin
    - File: drug_modules\hematology.py
    - Fields: 24

714. **Vonoprazan**
    - Nhóm: Gastrointestinal - Potassium-Competitive Acid Blocker (PCAB)
    - File: drug_modules\gastrointestinal\pcab.py
    - Fields: 22

715. **Voriconazole**
    - Nhóm: Infectious Disease - Antifungal (Azole, 2nd generation)
    - File: drug_modules\antimicrobial\antifungals\azoles.py
    - Fields: 24

716. **Warfarin**
    - Nhóm: Cardiovascular - Anticoagulant (Vitamin K Antagonist)
    - File: drug_modules\cardiovascular\anticoagulants.py
    - Fields: 24

717. **Zafirlukast**
    - Nhóm: Respiratory - Leukotriene Receptor Antagonist
    - File: drug_modules\respiratory\leukotriene_receptor_antagonists.py
    - Fields: 23

718. **Zanamivir**
    - Nhóm: Infectious Disease - Antiviral (Neuraminidase Inhibitor)
    - File: drug_modules\antimicrobial\antivirals\influenza.py
    - Fields: 27

719. **Ziprasidone**
    - Nhóm: Psychiatry - Antipsychotic (Atypical)
    - File: drug_modules\psychiatry_other\antipsychotics.py
    - Fields: 23

720. **Zoledronic acid**
    - Nhóm: Emergency - Electrolyte (Bisphosphonate)
    - File: drug_modules\emergency\electrolytes.py
    - Fields: 23

721. **Zonisamide**
    - Nhóm: Neurology - Anticonvulsant
    - File: drug_modules\neurological\anticonvulsants.py
    - Fields: 23

---

## 6. HƯỚNG DẪN THÊM THUỐC MỚI

### Bước 1: Xác định nhóm thuốc

Xem danh sách nhóm ở trên để xác định nhóm phù hợp.
Nếu không có nhóm phù hợp, tạo nhóm mới theo format: `'Category - Subcategory'`

### Bước 2: Xác định file chứa

Xem danh sách file ở trên để xác định file phù hợp.
Nếu không có file phù hợp, tạo file mới trong thư mục tương ứng.

### Bước 3: Sử dụng template

Copy template ở trên và điền thông tin:
1. Thay `DrugName` bằng tên thuốc
2. Điền đầy đủ 14 field chuẩn theo thứ tự
3. Đảm bảo tất cả field đều có giá trị (không để rỗng)

### Bước 4: Kiểm tra

```bash
# Kiểm tra thuốc mới
python comprehensive_drug_management_system.py check <DrugName>

# Kiểm tra trạng thái
python comprehensive_drug_management_system.py stats

# Cập nhật danh sách
python create_drug_lists.py
```

### Bước 5: Cập nhật file tham chiếu

Sau khi thêm thuốc mới, chạy lại script này để cập nhật file tham chiếu:
```bash
python create_drug_reference.py
```

---

## ⚠️ LƯU Ý QUAN TRỌNG

1. **Bắt buộc có đủ 14 field chuẩn** - Không được thiếu field nào
2. **Thứ tự field** - Nên theo thứ tự chuẩn (có thể linh hoạt nhưng nên tuân thủ)
3. **Tên thuốc** - Phải là tên chính xác, không trùng lặp
4. **Nhóm thuốc** - Phải nhất quán với các thuốc cùng loại
5. **File chứa** - Nên đặt trong file phù hợp với nhóm

---

**Cập nhật lần cuối**: 2025-02-18
**Tổng số thuốc**: 721
