# Kế Hoạch Các Phiên Làm Việc

**Tổng số phiên**: 253
**Tổng số thuốc cần xử lý**: 674

## Thống Kê

### Theo Field

- `contraindications_detail`: 117 phiên
- `drug_interactions`: 18 phiên
- `renal_adjustment`: 48 phiên
- `reversal_agents`: 70 phiên

### Theo Priority

- **high**: 64 phiên
- **low**: 155 phiên
- **medium**: 34 phiên

### Theo Module (Top 10)

- `cardiovascular`: 35 phiên
- `antimicrobial`: 20 phiên
- `miscellaneous`: 19 phiên
- `diabetes`: 15 phiên
- `gastrointestinal`: 14 phiên
- `infectious_other`: 14 phiên
- `respiratory`: 13 phiên
- `anesthesia`: 12 phiên
- `neurological`: 11 phiên
- `endocrinology`: 11 phiên

## Danh Sách Phiên Làm Việc

### renal_adjustment (48 phiên)

#### Module: allergy (1 phiên)

**Phiên 104** [low]: 5 thuốc trong `antihistamines.py`
- Danh sách: Desloratadine, Fexofenadine, Loratadine, Chlorpheniramine, Diphenhydramine

#### Module: analgesics (2 phiên)

**Phiên 99** [low]: 2 thuốc trong `antimigraine_5_ht1_receptor_agonists.py`
- Danh sách: Rizatriptan, Sumatriptan

**Phiên 114** [low]: 3 thuốc trong `nsaids.py`
- Danh sách: Probenecid, Cyclosporine, Methotrexate

#### Module: anesthesia (3 phiên)

**Phiên 68** [medium]: 3 thuốc trong `induction_agents.py`
- Danh sách: Etomidate, Ketamine, Propofol

**Phiên 69** [medium]: 3 thuốc trong `neuromuscular_blockers.py`
- Danh sách: Cisatracurium, Rocuronium, Succinylcholine

**Phiên 72** [medium]: 3 thuốc trong `local_anesthetics.py`
- Danh sách: Lidocaine, Bupivacaine, Levobupivacaine

#### Module: cardiovascular (9 phiên)

**Phiên 1** [high]: 5 thuốc trong `ace_arb.py`
- Danh sách: Enalapril, Lisinopril, Losartan, Telmisartan, Valsartan

**Phiên 2** [high]: 2 thuốc trong `statins.py`
- Danh sách: Atorvastatin, Rosuvastatin

**Phiên 3** [high]: 2 thuốc trong `dihydropyridines.py`
- Danh sách: Amlodipine, Lacidipine

**Phiên 4** [high]: 2 thuốc trong `diuretics.py`
- Danh sách: Hydrochlorothiazide, Indapamide

**Phiên 5** [high]: 3 thuốc trong `pcsk9_inhibitors.py`
- Danh sách: Alirocumab, Evolocumab, Inclisiran

**Phiên 6** [high]: 2 thuốc trong `antiarrhythmics.py`
- Danh sách: Dipyridamole, Carbamazepine

**Phiên 12** [high]: 1 thuốc trong `anticoagulants.py`
- Danh sách: Omeprazole

**Phiên 15** [high]: 1 thuốc trong `other_cv.py`
- Danh sách: Atropine

**Phiên 16** [high]: 1 thuốc trong `ace_inhibitors.py`
- Danh sách: Allopurinol

#### Module: diabetes (3 phiên)

**Phiên 7** [high]: 8 thuốc trong `specific_insulins.py`
- Danh sách: Insulin Aspart, Insulin Degludec, Insulin Detemir, Insulin Glargine, Insulin Glulisine và 3 thuốc khác

**Phiên 8** [high]: 3 thuốc trong `sglt2_inhibitors.py`
- Danh sách: Empagliflozin, Dapagliflozin, Canagliflozin

**Phiên 9** [high]: 4 thuốc trong `glp1_agonists.py`
- Danh sách: Liraglutide, Semaglutide, Dulaglutide, Exenatide

#### Module: emergency (2 phiên)

**Phiên 110** [low]: 2 thuốc trong `uterotonics.py`
- Danh sách: Carboprost, Dinoprostone

**Phiên 111** [low]: 4 thuốc trong `fluids.py`
- Danh sách: Sodium Chloride 0.9%, Ringer Lactate, Albumin (Human), HES 130/0.4

#### Module: endocrinology (2 phiên)

**Phiên 70** [medium]: 3 thuốc trong `thyroid.py`
- Danh sách: Levothyroxine, Methimazole, Propylthiouracil

**Phiên 71** [medium]: 5 thuốc trong `corticosteroids.py`
- Danh sách: Prednisone, Hydrocortisone, Methylprednisolone, Prednisolone, Dexamethasone

#### Module: endocrinology_other (2 phiên)

**Phiên 107** [low]: 1 thuốc trong `long_acting.py`
- Danh sách: Betamethasone

**Phiên 108** [low]: 1 thuốc trong `osteoporosis_bisphosphonates.py`
- Danh sách: Alendronate

#### Module: gastrointestinal (4 phiên)

**Phiên 10** [high]: 1 thuốc trong `h2_receptor_antagonists.py`
- Danh sách: Ranitidine

**Phiên 11** [high]: 3 thuốc trong `ppis.py`
- Danh sách: Esomeprazole, Lansoprazole, Pantoprazole

**Phiên 13** [high]: 2 thuốc trong `pcab.py`
- Danh sách: Tegoprazan, Vonoprazan

**Phiên 14** [high]: 1 thuốc trong `ibd_5asa.py`
- Danh sách: Sulfasalazine

#### Module: hematology (2 phiên)

**Phiên 102** [low]: 1 thuốc trong `growth_factors.py`
- Danh sách: Epoetin alfa

**Phiên 103** [low]: 2 thuốc trong `thrombolytics.py`
- Danh sách: Alteplase, Tenecteplase

#### Module: immunology (1 phiên)

**Phiên 115** [low]: 2 thuốc trong `immunosuppressants.py`
- Danh sách: Mycophenolate, Tacrolimus

#### Module: infectious_other (2 phiên)

**Phiên 106** [low]: 1 thuốc trong `antimalarials.py`
- Danh sách: Hydroxychloroquine

**Phiên 122** [low]: 1 thuốc trong `antituberculars.py`
- Danh sách: Pyridoxine (Vitamin B6)

#### Module: miscellaneous (4 phiên)

**Phiên 112** [low]: 4 thuốc trong `vitamins.py`
- Danh sách: Folic Acid, Vitamin C, Vitamin D3 (Cholecalciferol), Vitamin E

**Phiên 113** [low]: 2 thuốc trong `gout_medications.py`
- Danh sách: Colchicine, Febuxostat

**Phiên 116** [low]: 1 thuốc trong `dmards_rheumatology.py`
- Danh sách: Leflunomide

**Phiên 119** [low]: 1 thuốc trong `analgesicantipyretic.py`
- Danh sách: Acetylcysteine

#### Module: neurological (3 phiên)

**Phiên 65** [medium]: 2 thuốc trong `anticonvulsants.py`
- Danh sách: Oxcarbazepine, Ethanol

**Phiên 66** [medium]: 2 thuốc trong `muscle_relaxants.py`
- Danh sách: Metaxalone, Methocarbamol

**Phiên 67** [medium]: 1 thuốc trong `migraine_triptans.py`
- Danh sách: Zolmitriptan

#### Module: nutrition (1 phiên)

**Phiên 121** [low]: 3 thuốc trong `vitamins.py`
- Danh sách: Thiamine (Vitamin B1), Cyanocobalamin (Vitamin B12), Vitamin C (Ascorbic Acid)

#### Module: oncology (1 phiên)

**Phiên 109** [low]: 4 thuốc trong `basic_oncology.py`
- Danh sách: Tamoxifen, Anastrozole, Imatinib, Erlotinib

#### Module: psychiatry_other (1 phiên)

**Phiên 101** [low]: 3 thuốc trong `snris.py`
- Danh sách: Desvenlafaxine, Duloxetine, Venlafaxine

#### Module: respiratory (1 phiên)

**Phiên 100** [low]: 1 thuốc trong `inhaled_corticosteroid_icss.py`
- Danh sách: Budesonide inhaled

#### Module: supportive (1 phiên)

**Phiên 105** [low]: 1 thuốc trong `antihistamine_h1_antagonist_1st_generations.py`
- Danh sách: Hydroxyzine

#### Module: toxicology (1 phiên)

**Phiên 120** [low]: 2 thuốc trong `antidotes.py`
- Danh sách: Pralidoxime, Vitamin K1

#### Module: vaccines (2 phiên)

**Phiên 117** [low]: 4 thuốc trong `standard_vaccines.py`
- Danh sách: VAT (Tetanus Vaccine), Verorab (Rabies Vaccine), Influenza Vaccine, Hepatitis B Vaccine

**Phiên 118** [low]: 4 thuốc trong `antisera.py`
- Danh sách: SAT (Tetanus Antitoxin), SAR (Rabies Antiserum), Snake Antivenom (Luc Tre), Snake Antivenom (Ho Dat)

### drug_interactions (18 phiên)

#### Module: allergy (1 phiên)

**Phiên 124** [low]: 6 thuốc trong `antihistamines.py`
- Danh sách: Cetirizine, Desloratadine, Fexofenadine, Loratadine, Chlorpheniramine và 1 thuốc khác

#### Module: analgesics (1 phiên)

**Phiên 126** [low]: 1 thuốc trong `nsaids.py`
- Danh sách: Cyclosporine

#### Module: anesthesia (3 phiên)

**Phiên 73** [medium]: 3 thuốc trong `induction_agents.py`
- Danh sách: Etomidate, Ketamine, Propofol

**Phiên 74** [medium]: 3 thuốc trong `neuromuscular_blockers.py`
- Danh sách: Cisatracurium, Rocuronium, Succinylcholine

**Phiên 77** [medium]: 1 thuốc trong `local_anesthetics.py`
- Danh sách: Lidocaine

#### Module: cardiovascular (3 phiên)

**Phiên 17** [high]: 4 thuốc trong `ace_arb.py`
- Danh sách: Enalapril, Lisinopril, Losartan, Telmisartan

**Phiên 20** [high]: 1 thuốc trong `anticoagulants.py`
- Danh sách: Omeprazole

**Phiên 21** [high]: 2 thuốc trong `non_dihydropyridines.py`
- Danh sách: Diltiazem, Verapamil

#### Module: endocrinology (3 phiên)

**Phiên 75** [medium]: 3 thuốc trong `thyroid.py`
- Danh sách: Levothyroxine, Methimazole, Propylthiouracil

**Phiên 76** [medium]: 4 thuốc trong `corticosteroids.py`
- Danh sách: Prednisone, Hydrocortisone, Methylprednisolone, Dexamethasone

**Phiên 78** [medium]: 1 thuốc trong `antidiuretic_hormone.py`
- Danh sách: Desmopressin

#### Module: gastrointestinal (2 phiên)

**Phiên 18** [high]: 1 thuốc trong `h2_receptor_antagonists.py`
- Danh sách: Ranitidine

**Phiên 19** [high]: 3 thuốc trong `ppis.py`
- Danh sách: Esomeprazole, Lansoprazole, Pantoprazole

#### Module: immunology (1 phiên)

**Phiên 127** [low]: 4 thuốc trong `immunosuppressants.py`
- Danh sách: Mycophenolate, Tacrolimus, Sirolimus, Everolimus

#### Module: infectious_other (1 phiên)

**Phiên 129** [low]: 4 thuốc trong `tetracyclines.py`
- Danh sách: Doxycycline, Minocycline, Tetracycline, Tigecycline

#### Module: oncology (1 phiên)

**Phiên 125** [low]: 4 thuốc trong `basic_oncology.py`
- Danh sách: Tamoxifen, Anastrozole, Imatinib, Erlotinib

#### Module: respiratory (2 phiên)

**Phiên 123** [low]: 1 thuốc trong `inhaled_corticosteroid_icss.py`
- Danh sách: Budesonide inhaled

**Phiên 128** [low]: 1 thuốc trong `anticholinergic_short_actings.py`
- Danh sách: Ipratropium

### contraindications_detail (117 phiên)

#### Module: allergy (1 phiên)

**Phiên 135** [low]: 4 thuốc trong `antihistamines.py`
- Danh sách: Cetirizine, Desloratadine, Fexofenadine, Loratadine

#### Module: analgesics (5 phiên)

**Phiên 130** [low]: 2 thuốc trong `antimigraine_5_ht1_receptor_agonists.py`
- Danh sách: Rizatriptan, Sumatriptan

**Phiên 143** [low]: 8 thuốc trong `nsaids.py`
- Danh sách: Aspirin, Etoricoxib, Meloxicam, Naproxen, Nimesulide và 3 thuốc khác

**Phiên 155** [low]: 1 thuốc trong `opioid_agonists.py`
- Danh sách: Tapentadol

**Phiên 156** [low]: 6 thuốc trong `opioid_agonist_strongs.py`
- Danh sách: Morphine, Oxycodone, Remifentanil, Sufentanil, Alfentanil và 1 thuốc khác

**Phiên 157** [low]: 5 thuốc trong `pain_muscle_relaxant_combinations.py`
- Danh sách: Aspirin/Carisoprodol, Paracetamol/Carisoprodol, Paracetamol/Chlorzoxazone, Paracetamol/Methocarbamol, Paracetamol/Orphenadrine

#### Module: anesthesia (3 phiên)

**Phiên 82** [medium]: 3 thuốc trong `induction_agents.py`
- Danh sách: Etomidate, Ketamine, Propofol

**Phiên 83** [medium]: 3 thuốc trong `neuromuscular_blockers.py`
- Danh sách: Cisatracurium, Rocuronium, Succinylcholine

**Phiên 86** [medium]: 3 thuốc trong `local_anesthetics.py`
- Danh sách: Lidocaine, Bupivacaine, Levobupivacaine

#### Module: antimicrobial (9 phiên)

**Phiên 171** [low]: 2 thuốc trong `beta_lactams.py`
- Danh sách: Doripenem, Meropenem

**Phiên 173** [low]: 1 thuốc trong `cephalosporins.py`
- Danh sách: Cephalexin

**Phiên 174** [low]: 1 thuốc trong `aminoglycosides.py`
- Danh sách: Plazomicin

**Phiên 175** [low]: 2 thuốc trong `glycopeptides.py`
- Danh sách: Daptomycin, Teicoplanin

**Phiên 176** [low]: 1 thuốc trong `polymyxins.py`
- Danh sách: Polymyxin B

**Phiên 177** [low]: 3 thuốc trong `others.py`
- Danh sách: Lefamulin, Nitrofurantoin, Omadacycline

**Phiên 178** [low]: 2 thuốc trong `influenza.py`
- Danh sách: Remdesivir, Zanamivir

**Phiên 179** [low]: 1 thuốc trong `azoles.py`
- Danh sách: Isavuconazole

**Phiên 180** [low]: 1 thuốc trong `echinocandins.py`
- Danh sách: Micafungin

#### Module: cardiovascular (13 phiên)

**Phiên 22** [high]: 3 thuốc trong `ace_arb.py`
- Danh sách: Enalapril, Telmisartan, Valsartan

**Phiên 23** [high]: 3 thuốc trong `statins.py`
- Danh sách: Atorvastatin, Rosuvastatin, Niacin

**Phiên 24** [high]: 4 thuốc trong `dihydropyridines.py`
- Danh sách: Amlodipine, Lacidipine, Nicardipine, Nisoldipine

**Phiên 25** [high]: 1 thuốc trong `diuretics.py`
- Danh sách: Spironolactone

**Phiên 26** [high]: 3 thuốc trong `pcsk9_inhibitors.py`
- Danh sách: Alirocumab, Evolocumab, Inclisiran

**Phiên 27** [high]: 4 thuốc trong `antiarrhythmics.py`
- Danh sách: Quinidine, Sotalol, Carbamazepine, Magnesium sulfate

**Phiên 30** [high]: 1 thuốc trong `anticoagulants.py`
- Danh sách: Omeprazole

**Phiên 33** [high]: 4 thuốc trong `other_cv.py`
- Danh sách: Clonidine, Methyldopa, Sacubitril-valsartan, Atropine

**Phiên 34** [high]: 1 thuốc trong `ace_inhibitors.py`
- Danh sách: Allopurinol

**Phiên 35** [high]: 2 thuốc trong `arbs.py`
- Danh sách: Azilsartan medoxomil, Olmesartan

*... và 3 phiên khác*

#### Module: cardiovascular_other (1 phiên)

**Phiên 154** [low]: 1 thuốc trong `ace_inhibitors_iv.py`
- Danh sách: Enalaprilat

#### Module: dermatology (6 phiên)

**Phiên 189** [low]: 7 thuốc trong `other_topical.py`
- Danh sách: Calcipotriol, Calcitriol topical, Diclofenac gel, Ivermectin cream, Ketoprofen gel và 2 thuốc khác

**Phiên 190** [low]: 1 thuốc trong `topical_antiacne.py`
- Danh sách: Azelaic Acid

**Phiên 191** [low]: 5 thuốc trong `topical_antibiotics.py`
- Danh sách: Clindamycin topical, Erythromycin topical, Fusidic Acid, Metronidazole topical, Mupirocin topical

**Phiên 192** [low]: 5 thuốc trong `topical_antifungals.py`
- Danh sách: Clotrimazole topical, Econazole topical, Ketoconazole topical, Miconazole topical, Terbinafine topical

**Phiên 193** [low]: 7 thuốc trong `topical_corticosteroids.py`
- Danh sách: Betamethasone topical, Betamethasone/Clotrimazole topical, Clobetasol, Fusidic acid/Betamethasone topical, Hydrocortisone topical và 2 thuốc khác

**Phiên 194** [low]: 2 thuốc trong `topical_retinoids.py`
- Danh sách: Adapalene, Tazarotene

#### Module: diabetes (9 phiên)

**Phiên 28** [high]: 7 thuốc trong `specific_insulins.py`
- Danh sách: Insulin Aspart, Insulin Degludec, Insulin Detemir, Insulin Glargine, Insulin Glulisine và 2 thuốc khác

**Phiên 29** [high]: 4 thuốc trong `glp1_agonists.py`
- Danh sách: Liraglutide, Semaglutide, Dulaglutide, Exenatide

**Phiên 39** [high]: 1 thuốc trong `biguanides.py`
- Danh sách: Metformin

**Phiên 40** [high]: 1 thuốc trong `dpp_4_inhibitors.py`
- Danh sách: Vildagliptin

**Phiên 41** [high]: 2 thuốc trong `thiazolidinedione_tzds.py`
- Danh sách: Pioglitazone, Rosiglitazone

**Phiên 42** [high]: 1 thuốc trong `meglitinides.py`
- Danh sách: Nateglinide

**Phiên 43** [high]: 2 thuốc trong `fixed_dose_combinations.py`
- Danh sách: Metformin/Glibenclamide, Metformin/Pioglitazone

**Phiên 44** [high]: 1 thuốc trong `t1dm_prevention.py`
- Danh sách: Teplizumab

**Phiên 45** [high]: 2 thuốc trong `other_antidiabetics.py`
- Danh sách: Bromocriptine, Colesevelam

#### Module: emergency (6 phiên)

**Phiên 139** [low]: 3 thuốc trong `uterotonics.py`
- Danh sách: Carboprost, Dinoprostone, Methylergonovine

**Phiên 140** [low]: 4 thuốc trong `fluids.py`
- Danh sách: Sodium Chloride 0.9%, Ringer Lactate, Albumin (Human), HES 130/0.4

**Phiên 170** [low]: 1 thuốc trong `neuromuscular_blockers.py`
- Danh sách: Vecuronium

**Phiên 184** [low]: 10 thuốc trong `electrolytes.py`
- Danh sách: Zoledronic acid, Calcium chloride, Calcium gluconate, Demeclocycline, Magnesium oxide và 5 thuốc khác

**Phiên 185** [low]: 1 thuốc trong `opioid_antagonists.py`
- Danh sách: Naltrexone

**Phiên 186** [low]: 2 thuốc trong `catecholamine_alpha__beta_agonists.py`
- Danh sách: Epinephrine, Vasopressin

#### Module: endocrinology (3 phiên)

**Phiên 84** [medium]: 2 thuốc trong `thyroid.py`
- Danh sách: Levothyroxine, Methimazole

**Phiên 85** [medium]: 5 thuốc trong `corticosteroids.py`
- Danh sách: Prednisone, Hydrocortisone, Methylprednisolone, Prednisolone, Dexamethasone

**Phiên 87** [medium]: 1 thuốc trong `antidiuretic_hormone.py`
- Danh sách: Desmopressin

#### Module: endocrinology_other (2 phiên)

**Phiên 137** [low]: 1 thuốc trong `osteoporosis_bisphosphonates.py`
- Danh sách: Alendronate

**Phiên 183** [low]: 1 thuốc trong `sex_hormones.py`
- Danh sách: Testosterone

#### Module: ent_oral_nasal_combinations.py (1 phiên)

**Phiên 200** [low]: 4 thuốc trong `ent_oral_nasal_combinations.py`
- Danh sách: Azelastine/Fluticasone nasal spray, Cetirizine/Pseudoephedrine, Fexofenadine/Pseudoephedrine, Loratadine/Pseudoephedrine

#### Module: gastrointestinal (4 phiên)

**Phiên 31** [high]: 2 thuốc trong `pcab.py`
- Danh sách: Tegoprazan, Vonoprazan

**Phiên 32** [high]: 1 thuốc trong `ibd_5asa.py`
- Danh sách: Sulfasalazine

**Phiên 46** [high]: 1 thuốc trong `mucosal_protectants.py`
- Danh sách: Misoprostol

**Phiên 47** [high]: 1 thuốc trong `proton_pump_inhibitors.py`
- Danh sách: Rabeprazole

#### Module: hematology (2 phiên)

**Phiên 133** [low]: 2 thuốc trong `growth_factors.py`
- Danh sách: Epoetin alfa, Filgrastim

**Phiên 134** [low]: 1 thuốc trong `thrombolytics.py`
- Danh sách: Alteplase

#### Module: immunology (1 phiên)

**Phiên 144** [low]: 4 thuốc trong `immunosuppressants.py`
- Danh sách: Mycophenolate, Tacrolimus, Sirolimus, Everolimus

#### Module: infectious_other (7 phiên)

**Phiên 136** [low]: 2 thuốc trong `antimalarials.py`
- Danh sách: Hydroxychloroquine, Primaquine

**Phiên 151** [low]: 1 thuốc trong `antituberculars.py`
- Danh sách: Pyridoxine (Vitamin B6)

**Phiên 153** [low]: 4 thuốc trong `tetracyclines.py`
- Danh sách: Doxycycline, Minocycline, Tetracycline, Tigecycline

**Phiên 166** [low]: 2 thuốc trong `anthelmintics.py`
- Danh sách: Clozapine, Mebendazole

**Phiên 172** [low]: 3 thuốc trong `beta_lactams.py`
- Danh sách: Nafcillin, Oxacillin, Dicloxacillin

**Phiên 181** [low]: 3 thuốc trong `cephalosporins.py`
- Danh sách: Cefaclor, Cefdinir, Cefixime

**Phiên 182** [low]: 4 thuốc trong `fluoroquinolones.py`
- Danh sách: Gemifloxacin, Norfloxacin, Ofloxacin, Sparfloxacin

#### Module: miscellaneous (11 phiên)

**Phiên 141** [low]: 3 thuốc trong `vitamins.py`
- Danh sách: Vitamin C, Vitamin D3 (Cholecalciferol), Vitamin E

**Phiên 142** [low]: 2 thuốc trong `gout_medications.py`
- Danh sách: Colchicine, Febuxostat

**Phiên 145** [low]: 1 thuốc trong `dmards_rheumatology.py`
- Danh sách: Leflunomide

**Phiên 148** [low]: 1 thuốc trong `analgesicantipyretic.py`
- Danh sách: Acetylcysteine

**Phiên 159** [low]: 2 thuốc trong `beta_2_agonist_short_actings.py`
- Danh sách: Formoterol, Salmeterol

**Phiên 201** [low]: 1 thuốc trong `immunosuppressants.py`
- Danh sách: Azathioprine

**Phiên 202** [low]: 1 thuốc trong `fusion_proteins.py`
- Danh sách: Etanercept

**Phiên 203** [low]: 12 thuốc trong `monoclonal_antibodies.py`
- Danh sách: Atezolizumab, Belimumab, Brodalumab, Cemiplimab, Certolizumab pegol và 7 thuốc khác

**Phiên 204** [low]: 12 thuốc trong `monoclonal_antibodies.py`
- Danh sách: Lanadelumab, Natalizumab, Nivolumab, Ocrelizumab, Pembrolizumab và 7 thuốc khác

**Phiên 205** [low]: 2 thuốc trong `monoclonal_antibodies.py`
- Danh sách: Ustekinumab, Vedolizumab

*... và 1 phiên khác*

#### Module: neurological (5 phiên)

**Phiên 79** [medium]: 6 thuốc trong `anticonvulsants.py`
- Danh sách: Ethosuximide, Oxcarbazepine, Perampanel, Primidone, Zonisamide và 1 thuốc khác

**Phiên 80** [medium]: 2 thuốc trong `muscle_relaxants.py`
- Danh sách: Metaxalone, Methocarbamol

**Phiên 81** [medium]: 1 thuốc trong `migraine_triptans.py`
- Danh sách: Zolmitriptan

**Phiên 88** [medium]: 5 thuốc trong `antiparkinsonian.py`
- Danh sách: Deutetrabenazine, Pimavanserin, Pramipexole, Safinamide, Tetrabenazine

**Phiên 89** [medium]: 4 thuốc trong `neurological_combinations.py`
- Danh sách: Citicoline/Piracetam, Ginkgo biloba/Vinpocetine, Olanzapine/Fluoxetine, Piracetam/Vinpocetine

#### Module: nutrition (1 phiên)

**Phiên 150** [low]: 3 thuốc trong `vitamins.py`
- Danh sách: Thiamine (Vitamin B1), Cyanocobalamin (Vitamin B12), Vitamin C (Ascorbic Acid)

#### Module: obstetrics_gynecology (1 phiên)

**Phiên 199** [low]: 1 thuốc trong `contraceptives.py`
- Danh sách: Levonorgestrel

#### Module: oncology (3 phiên)

**Phiên 138** [low]: 3 thuốc trong `basic_oncology.py`
- Danh sách: Tamoxifen, Imatinib, Erlotinib

**Phiên 206** [low]: 1 thuốc trong `monoclonal_antibodies_adcs.py`
- Danh sách: Bevacizumab

**Phiên 207** [low]: 1 thuốc trong `anthracyclines.py`
- Danh sách: Trastuzumab

#### Module: ophthalmology (4 phiên)

**Phiên 195** [low]: 7 thuốc trong `anti_glaucoma.py`
- Danh sách: Bimatoprost, Brimonidine, Brinzolamide, Dorzolamide, Latanoprost và 2 thuốc khác

**Phiên 196** [low]: 7 thuốc trong `anti_infective.py`
- Danh sách: Ciprofloxacin eye drops, Erythromycin eye ointment, Ganciclovir eye drops, Gentamicin eye drops, Moxifloxacin eye drops và 2 thuốc khác

**Phiên 197** [low]: 2 thuốc trong `antihistamines.py`
- Danh sách: Ketotifen eye drops, Olopatadine eye drops

**Phiên 198** [low]: 4 thuốc trong `mydriatics.py`
- Danh sách: Atropine eye drops, Cyclopentolate eye drops, Phenylephrine eye drops, Tropicamide eye drops

#### Module: psychiatry_other (5 phiên)

**Phiên 132** [low]: 3 thuốc trong `snris.py`
- Danh sách: Desvenlafaxine, Duloxetine, Venlafaxine

**Phiên 165** [low]: 1 thuốc trong `tcas.py`
- Danh sách: Clomipramine

**Phiên 167** [low]: 2 thuốc trong `antipsychotics.py`
- Danh sách: Pimozide, Ziprasidone

**Phiên 168** [low]: 4 thuốc trong `antidepressants.py`
- Danh sách: Mirtazapine, Phenelzine, Tranylcypromine, Trazodone

**Phiên 169** [low]: 5 thuốc trong `adhd_anxiolytics.py`
- Danh sách: Atomoxetine, Buspirone, Dextroamphetamine, Lisdexamfetamine, Methylphenidate

#### Module: respiratory (8 phiên)

**Phiên 131** [low]: 2 thuốc trong `inhaled_corticosteroid_icss.py`
- Danh sách: Budesonide inhaled, Fluticasone inhaled

**Phiên 152** [low]: 1 thuốc trong `anticholinergic_short_actings.py`
- Danh sách: Ipratropium

**Phiên 158** [low]: 2 thuốc trong `leukotriene_receptor_antagonists.py`
- Danh sách: Cromolyn, Zafirlukast

**Phiên 160** [low]: 3 thuốc trong `long_acting_beta_2_agonist_labas.py`
- Danh sách: Indacaterol, Olodaterol, Vilanterol

**Phiên 161** [low]: 4 thuốc trong `anticholinergic_long_actings.py`
- Danh sách: Aclidinium, Glycopyrronium, Tiotropium, Umeclidinium

**Phiên 162** [low]: 5 thuốc trong `respiratory_biologics.py`
- Danh sách: Benralizumab, Dupilumab, Mepolizumab, Omalizumab, Tezepelumab

**Phiên 163** [low]: 1 thuốc trong `pde4_inhibitors.py`
- Danh sách: Roflumilast

**Phiên 164** [low]: 6 thuốc trong `combination_inhalers.py`
- Danh sách: Budesonide/Formoterol inhaler, Fluticasone/Salmeterol inhaler, Fluticasone/Umeclidinium/Vilanterol inhaler, Ipratropium/Salbutamol inhaler, Tiotropium/Olodaterol inhaler và 1 thuốc khác

#### Module: rheumatology (1 phiên)

**Phiên 209** [low]: 1 thuốc trong `osteoporosis.py`
- Danh sách: Zoledronic Acid

#### Module: toxicology (1 phiên)

**Phiên 149** [low]: 2 thuốc trong `antidotes.py`
- Danh sách: Pralidoxime, Vitamin K1

#### Module: urology (2 phiên)

**Phiên 187** [low]: 2 thuốc trong `bph_alpha_blockers.py`
- Danh sách: Silodosin, Tamsulosin

**Phiên 188** [low]: 1 thuốc trong `overactive_bladder.py`
- Danh sách: Fesoterodine

#### Module: vaccines (2 phiên)

**Phiên 146** [low]: 4 thuốc trong `standard_vaccines.py`
- Danh sách: VAT (Tetanus Vaccine), Verorab (Rabies Vaccine), Influenza Vaccine, Hepatitis B Vaccine

**Phiên 147** [low]: 4 thuốc trong `antisera.py`
- Danh sách: SAT (Tetanus Antitoxin), SAR (Rabies Antiserum), Snake Antivenom (Luc Tre), Snake Antivenom (Ho Dat)

### reversal_agents (70 phiên)

#### Module: allergy (1 phiên)

**Phiên 212** [low]: 6 thuốc trong `antihistamines.py`
- Danh sách: Cetirizine, Desloratadine, Fexofenadine, Loratadine, Chlorpheniramine và 1 thuốc khác

#### Module: analgesics (3 phiên)

**Phiên 210** [low]: 2 thuốc trong `antimigraine_5_ht1_receptor_agonists.py`
- Danh sách: Rizatriptan, Sumatriptan

**Phiên 221** [low]: 2 thuốc trong `nsaids.py`
- Danh sách: Cyclosporine, Methotrexate

**Phiên 232** [low]: 1 thuốc trong `opioid_agonist_strongs.py`
- Danh sách: Rifampin

#### Module: anesthesia (3 phiên)

**Phiên 92** [medium]: 3 thuốc trong `induction_agents.py`
- Danh sách: Etomidate, Ketamine, Propofol

**Phiên 93** [medium]: 2 thuốc trong `neuromuscular_blockers.py`
- Danh sách: Cisatracurium, Succinylcholine

**Phiên 96** [medium]: 3 thuốc trong `local_anesthetics.py`
- Danh sách: Lidocaine, Bupivacaine, Levobupivacaine

#### Module: antimicrobial (11 phiên)

**Phiên 233** [low]: 4 thuốc trong `beta_lactams.py`
- Danh sách: Ertapenem, Imipenem-cilastatin, Penicillin G, Piperacillin-tazobactam

**Phiên 234** [low]: 1 thuốc trong `cephalosporins.py`
- Danh sách: Cephalexin

**Phiên 235** [low]: 3 thuốc trong `aminoglycosides.py`
- Danh sách: Amikacin, Gentamicin, Tobramycin

**Phiên 236** [low]: 1 thuốc trong `azoles.py`
- Danh sách: Isavuconazole

**Phiên 237** [low]: 1 thuốc trong `echinocandins.py`
- Danh sách: Anidulafungin

**Phiên 247** [low]: 2 thuốc trong `herpes.py`
- Danh sách: Acyclovir, Valacyclovir

**Phiên 248** [low]: 5 thuốc trong `hepatitis.py`
- Danh sách: Entecavir, Ledipasvir, Sofosbuvir, Sofosbuvir/Velpatasvir, Tenofovir

**Phiên 249** [low]: 1 thuốc trong `integrase_inhibitors.py`
- Danh sách: Bictegravir/Emtricitabine/Tenofovir alafenamide (BIC/FTC/TAF)

**Phiên 250** [low]: 1 thuốc trong `nnrti.py`
- Danh sách: Efavirenz/Tenofovir disoproxil fumarate/Emtricitabine (EFV/TDF/FTC)

**Phiên 251** [low]: 6 thuốc trong `nrti.py`
- Danh sách: Emtricitabine (FTC), Lamivudine (3TC), Tenofovir alafenamide (TAF), Tenofovir alafenamide/Emtricitabine (TAF/FTC), Tenofovir disoproxil fumarate (TDF) và 1 thuốc khác

*... và 1 phiên khác*

#### Module: cardiovascular (10 phiên)

**Phiên 48** [high]: 5 thuốc trong `ace_arb.py`
- Danh sách: Enalapril, Lisinopril, Losartan, Telmisartan, Valsartan

**Phiên 49** [high]: 4 thuốc trong `statins.py`
- Danh sách: Atorvastatin, Simvastatin, Rosuvastatin, Pravastatin

**Phiên 50** [high]: 1 thuốc trong `dihydropyridines.py`
- Danh sách: Clevidipine

**Phiên 55** [high]: 1 thuốc trong `anticoagulants.py`
- Danh sách: Omeprazole

**Phiên 57** [high]: 4 thuốc trong `other_cv.py`
- Danh sách: Finerenone, Sotagliflozin, Vericiguat, Atropine

**Phiên 58** [high]: 1 thuốc trong `ace_inhibitors.py`
- Danh sách: Allopurinol

**Phiên 59** [high]: 2 thuốc trong `non_dihydropyridines.py`
- Danh sách: Diltiazem, Verapamil

**Phiên 61** [high]: 1 thuốc trong `vasodilators.py`
- Danh sách: Nesiritide

**Phiên 62** [high]: 1 thuốc trong `cholesterol_absorption_inhibitors.py`
- Danh sách: Bempedoic acid

**Phiên 63** [high]: 4 thuốc trong `fixed_dose_combinations.py`
- Danh sách: Amlodipine/Olmesartan, Amlodipine/Valsartan, Lisinopril/Hydrochlorothiazide, Losartan/Hydrochlorothiazide

#### Module: dermatology (3 phiên)

**Phiên 241** [low]: 2 thuốc trong `topical_antiacne.py`
- Danh sách: Azelaic acid topical, Benzoyl peroxide topical

**Phiên 242** [low]: 1 thuốc trong `topical_antibiotics.py`
- Danh sách: Mupirocin topical

**Phiên 243** [low]: 5 thuốc trong `topical_corticosteroids.py`
- Danh sách: Betamethasone/Clotrimazole topical, Clobetasol, Fusidic acid/Betamethasone topical, Gentamicin/Betamethasone/Clotrimazole topical, Miconazole/Hydrocortisone topical

#### Module: diabetes (3 phiên)

**Phiên 51** [high]: 3 thuốc trong `sglt2_inhibitors.py`
- Danh sách: Empagliflozin, Dapagliflozin, Canagliflozin

**Phiên 52** [high]: 4 thuốc trong `glp1_agonists.py`
- Danh sách: Liraglutide, Semaglutide, Dulaglutide, Exenatide

**Phiên 60** [high]: 3 thuốc trong `fixed_dose_combinations.py`
- Danh sách: Metformin/Dapagliflozin, Metformin/Empagliflozin, Metformin/Sitagliptin

#### Module: emergency (3 phiên)

**Phiên 217** [low]: 3 thuốc trong `uterotonics.py`
- Danh sách: Carboprost, Dinoprostone, Methylergonovine

**Phiên 218** [low]: 4 thuốc trong `fluids.py`
- Danh sách: Sodium Chloride 0.9%, Ringer Lactate, Albumin (Human), HES 130/0.4

**Phiên 239** [low]: 4 thuốc trong `catecholamine_alpha__beta_agonists.py`
- Danh sách: Dobutamine, Dopamine, Norepinephrine, Vasopressin

#### Module: endocrinology (3 phiên)

**Phiên 94** [medium]: 3 thuốc trong `thyroid.py`
- Danh sách: Levothyroxine, Methimazole, Propylthiouracil

**Phiên 95** [medium]: 5 thuốc trong `corticosteroids.py`
- Danh sách: Prednisone, Hydrocortisone, Methylprednisolone, Prednisolone, Dexamethasone

**Phiên 97** [medium]: 1 thuốc trong `antidiuretic_hormone.py`
- Danh sách: Desmopressin

#### Module: endocrinology_other (3 phiên)

**Phiên 214** [low]: 1 thuốc trong `long_acting.py`
- Danh sách: Betamethasone

**Phiên 215** [low]: 3 thuốc trong `osteoporosis_bisphosphonates.py`
- Danh sách: Alendronate, Ibandronate, Risedronate

**Phiên 253** [low]: 5 thuốc trong `osteoporosis_other.py`
- Danh sách: Abaloparatide, Denosumab, Raloxifene, Romosozumab, Teriparatide

#### Module: gastrointestinal (4 phiên)

**Phiên 53** [high]: 1 thuốc trong `h2_receptor_antagonists.py`
- Danh sách: Ranitidine

**Phiên 54** [high]: 1 thuốc trong `ppis.py`
- Danh sách: Pantoprazole

**Phiên 56** [high]: 1 thuốc trong `ibd_5asa.py`
- Danh sách: Sulfasalazine

**Phiên 64** [high]: 2 thuốc trong `proton_pump_inhibitor_ppis.py`
- Danh sách: Dexlansoprazole, Ilaprazole

#### Module: hematology (1 phiên)

**Phiên 246** [low]: 1 thuốc trong `reversal_agents.py`
- Danh sách: Andexanet alfa

#### Module: immunology (1 phiên)

**Phiên 222** [low]: 4 thuốc trong `immunosuppressants.py`
- Danh sách: Mycophenolate, Tacrolimus, Sirolimus, Everolimus

#### Module: infectious_other (4 phiên)

**Phiên 213** [low]: 1 thuốc trong `antimalarials.py`
- Danh sách: Hydroxychloroquine

**Phiên 229** [low]: 9 thuốc trong `antituberculars.py`
- Danh sách: Levofloxacin, Linezolid, Linezolid (lao MDR/XDR), PAS (para-aminosalicylic acid), Pyrazinamide và 4 thuốc khác

**Phiên 231** [low]: 3 thuốc trong `tetracyclines.py`
- Danh sách: Doxycycline, Minocycline, Tetracycline

**Phiên 238** [low]: 2 thuốc trong `cephalosporins.py`
- Danh sách: Vancomycin, Cefpirome

#### Module: miscellaneous (4 phiên)

**Phiên 219** [low]: 1 thuốc trong `vitamins.py`
- Danh sách: Vitamin D3 (Cholecalciferol)

**Phiên 220** [low]: 2 thuốc trong `gout_medications.py`
- Danh sách: Colchicine, Febuxostat

**Phiên 223** [low]: 1 thuốc trong `dmards_rheumatology.py`
- Danh sách: Leflunomide

**Phiên 226** [low]: 1 thuốc trong `analgesicantipyretic.py`
- Danh sách: Acetylcysteine

#### Module: neurological (3 phiên)

**Phiên 90** [medium]: 1 thuốc trong `anticonvulsants.py`
- Danh sách: Ethanol

**Phiên 91** [medium]: 1 thuốc trong `migraine_triptans.py`
- Danh sách: Zolmitriptan

**Phiên 98** [medium]: 1 thuốc trong `anticonvulsant_alpha_2_delta_ligands.py`
- Danh sách: Gabapentin

#### Module: nutrition (1 phiên)

**Phiên 228** [low]: 3 thuốc trong `vitamins.py`
- Danh sách: Thiamine (Vitamin B1), Cyanocobalamin (Vitamin B12), Vitamin C (Ascorbic Acid)

#### Module: oncology (1 phiên)

**Phiên 216** [low]: 4 thuốc trong `basic_oncology.py`
- Danh sách: Tamoxifen, Anastrozole, Imatinib, Erlotinib

#### Module: ophthalmology (1 phiên)

**Phiên 244** [low]: 1 thuốc trong `anti_infective.py`
- Danh sách: Polymyxin B/Trimethoprim eye drops

#### Module: respiratory (2 phiên)

**Phiên 211** [low]: 1 thuốc trong `inhaled_corticosteroid_icss.py`
- Danh sách: Budesonide inhaled

**Phiên 230** [low]: 1 thuốc trong `anticholinergic_short_actings.py`
- Danh sách: Ipratropium

#### Module: rheumatology (1 phiên)

**Phiên 245** [low]: 1 thuốc trong `osteoporosis.py`
- Danh sách: Zoledronic Acid

#### Module: toxicology (1 phiên)

**Phiên 227** [low]: 2 thuốc trong `antidotes.py`
- Danh sách: Pralidoxime, Vitamin K1

#### Module: urology (1 phiên)

**Phiên 240** [low]: 1 thuốc trong `overactive_bladder.py`
- Danh sách: Fesoterodine

#### Module: vaccines (2 phiên)

**Phiên 224** [low]: 4 thuốc trong `standard_vaccines.py`
- Danh sách: VAT (Tetanus Vaccine), Verorab (Rabies Vaccine), Influenza Vaccine, Hepatitis B Vaccine

**Phiên 225** [low]: 4 thuốc trong `antisera.py`
- Danh sách: SAT (Tetanus Antitoxin), SAR (Rabies Antiserum), Snake Antivenom (Luc Tre), Snake Antivenom (Ho Dat)

