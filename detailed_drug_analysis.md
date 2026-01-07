# Báo Cáo Chi Tiết Thuốc Thiếu Fields

**Tổng số thuốc**: 722

## Thống Kê Theo Field

| Field | Số thuốc thiếu | Số module | Số file |
|-------|----------------|-----------|----------|
| `renal_adjustment` | 118 | 21 | 48 |
| `drug_interactions` | 47 | 10 | 18 |
| `contraindications_detail` | 338 | 28 | 115 |
| `reversal_agents` | 171 | 24 | 70 |

## Thuốc Ưu Tiên (Thiếu Nhiều Field)

| Thuốc | Số field thiếu | Các field | File |
|-------|----------------|-----------|------|
| Enalapril | 4 | renal_adjustment, drug_interactions, contraindications_detail, reversal_agents | ace_arb.py |
| Telmisartan | 4 | renal_adjustment, drug_interactions, contraindications_detail, reversal_agents | ace_arb.py |
| Omeprazole | 4 | renal_adjustment, drug_interactions, contraindications_detail, reversal_agents | anticoagulants.py |
| Budesonide inhaled | 4 | renal_adjustment, drug_interactions, contraindications_detail, reversal_agents | inhaled_corticosteroid_icss.py |
| Desloratadine | 4 | renal_adjustment, drug_interactions, contraindications_detail, reversal_agents | antihistamines.py |
| Fexofenadine | 4 | renal_adjustment, drug_interactions, contraindications_detail, reversal_agents | antihistamines.py |
| Loratadine | 4 | renal_adjustment, drug_interactions, contraindications_detail, reversal_agents | antihistamines.py |
| Etomidate | 4 | renal_adjustment, drug_interactions, contraindications_detail, reversal_agents | induction_agents.py |
| Ketamine | 4 | renal_adjustment, drug_interactions, contraindications_detail, reversal_agents | induction_agents.py |
| Propofol | 4 | renal_adjustment, drug_interactions, contraindications_detail, reversal_agents | induction_agents.py |
| Cisatracurium | 4 | renal_adjustment, drug_interactions, contraindications_detail, reversal_agents | neuromuscular_blockers.py |
| Succinylcholine | 4 | renal_adjustment, drug_interactions, contraindications_detail, reversal_agents | neuromuscular_blockers.py |
| Levothyroxine | 4 | renal_adjustment, drug_interactions, contraindications_detail, reversal_agents | thyroid.py |
| Methimazole | 4 | renal_adjustment, drug_interactions, contraindications_detail, reversal_agents | thyroid.py |
| Prednisone | 4 | renal_adjustment, drug_interactions, contraindications_detail, reversal_agents | corticosteroids.py |
| Hydrocortisone | 4 | renal_adjustment, drug_interactions, contraindications_detail, reversal_agents | corticosteroids.py |
| Methylprednisolone | 4 | renal_adjustment, drug_interactions, contraindications_detail, reversal_agents | corticosteroids.py |
| Dexamethasone | 4 | renal_adjustment, drug_interactions, contraindications_detail, reversal_agents | corticosteroids.py |
| Tamoxifen | 4 | renal_adjustment, drug_interactions, contraindications_detail, reversal_agents | basic_oncology.py |
| Imatinib | 4 | renal_adjustment, drug_interactions, contraindications_detail, reversal_agents | basic_oncology.py |
| Erlotinib | 4 | renal_adjustment, drug_interactions, contraindications_detail, reversal_agents | basic_oncology.py |
| Lidocaine | 4 | renal_adjustment, drug_interactions, contraindications_detail, reversal_agents | local_anesthetics.py |
| Cyclosporine | 4 | renal_adjustment, drug_interactions, contraindications_detail, reversal_agents | nsaids.py |
| Mycophenolate | 4 | renal_adjustment, drug_interactions, contraindications_detail, reversal_agents | immunosuppressants.py |
| Tacrolimus | 4 | renal_adjustment, drug_interactions, contraindications_detail, reversal_agents | immunosuppressants.py |
| Lisinopril | 3 | renal_adjustment, drug_interactions, reversal_agents | ace_arb.py |
| Losartan | 3 | renal_adjustment, drug_interactions, reversal_agents | ace_arb.py |
| Valsartan | 3 | renal_adjustment, contraindications_detail, reversal_agents | ace_arb.py |
| Atorvastatin | 3 | renal_adjustment, contraindications_detail, reversal_agents | statins.py |
| Rosuvastatin | 3 | renal_adjustment, contraindications_detail, reversal_agents | statins.py |

## Danh Sách Theo File (Top 20)

### monoclonal_antibodies.py

**Module**: miscellaneous

**Tổng số thuốc thiếu**: 26

- **contraindications_detail**: 26 thuốc - Atezolizumab, Belimumab, Brodalumab, Cemiplimab, Certolizumab pegol và 21 thuốc khác

### electrolytes.py

**Module**: emergency

**Tổng số thuốc thiếu**: 10

- **contraindications_detail**: 10 thuốc - Zoledronic acid, Calcium chloride, Calcium gluconate, Demeclocycline, Magnesium oxide và 5 thuốc khác

### antituberculars.py

**Module**: infectious_other

**Tổng số thuốc thiếu**: 9

- **renal_adjustment**: 1 thuốc - Pyridoxine (Vitamin B6)
- **contraindications_detail**: 1 thuốc - Pyridoxine (Vitamin B6)
- **reversal_agents**: 9 thuốc - Levofloxacin, Linezolid, Linezolid (lao MDR/XDR), PAS (para-aminosalicylic acid), Pyrazinamide và 4 thuốc khác

### topical_corticosteroids.py

**Module**: dermatology

**Tổng số thuốc thiếu**: 9

- **contraindications_detail**: 7 thuốc - Betamethasone topical, Betamethasone/Clotrimazole topical, Clobetasol, Fusidic acid/Betamethasone topical, Hydrocortisone topical và 2 thuốc khác
- **reversal_agents**: 5 thuốc - Betamethasone/Clotrimazole topical, Clobetasol, Fusidic acid/Betamethasone topical, Gentamicin/Betamethasone/Clotrimazole topical, Miconazole/Hydrocortisone topical

### specific_insulins.py

**Module**: diabetes

**Tổng số thuốc thiếu**: 8

- **renal_adjustment**: 8 thuốc - Insulin Aspart, Insulin Degludec, Insulin Detemir, Insulin Glargine, Insulin Glulisine và 3 thuốc khác
- **contraindications_detail**: 7 thuốc - Insulin Aspart, Insulin Degludec, Insulin Detemir, Insulin Glargine, Insulin Glulisine và 2 thuốc khác

### nsaids.py

**Module**: analgesics

**Tổng số thuốc thiếu**: 8

- **renal_adjustment**: 3 thuốc - Probenecid, Cyclosporine, Methotrexate
- **drug_interactions**: 1 thuốc - Cyclosporine
- **contraindications_detail**: 8 thuốc - Aspirin, Etoricoxib, Meloxicam, Naproxen, Nimesulide và 3 thuốc khác
- **reversal_agents**: 2 thuốc - Cyclosporine, Methotrexate

### other_cv.py

**Module**: cardiovascular

**Tổng số thuốc thiếu**: 7

- **renal_adjustment**: 1 thuốc - Atropine
- **contraindications_detail**: 4 thuốc - Clonidine, Methyldopa, Sacubitril-valsartan, Atropine
- **reversal_agents**: 4 thuốc - Finerenone, Sotagliflozin, Vericiguat, Atropine

### opioid_agonist_strongs.py

**Module**: analgesics

**Tổng số thuốc thiếu**: 7

- **contraindications_detail**: 6 thuốc - Morphine, Oxycodone, Remifentanil, Sufentanil, Alfentanil và 1 thuốc khác
- **reversal_agents**: 1 thuốc - Rifampin

### other_topical.py

**Module**: dermatology

**Tổng số thuốc thiếu**: 7

- **contraindications_detail**: 7 thuốc - Calcipotriol, Calcitriol topical, Diclofenac gel, Ivermectin cream, Ketoprofen gel và 2 thuốc khác

### anti_glaucoma.py

**Module**: ophthalmology

**Tổng số thuốc thiếu**: 7

- **contraindications_detail**: 7 thuốc - Bimatoprost, Brimonidine, Brinzolamide, Dorzolamide, Latanoprost và 2 thuốc khác

### anti_infective.py

**Module**: ophthalmology

**Tổng số thuốc thiếu**: 7

- **contraindications_detail**: 7 thuốc - Ciprofloxacin eye drops, Erythromycin eye ointment, Ganciclovir eye drops, Gentamicin eye drops, Moxifloxacin eye drops và 2 thuốc khác
- **reversal_agents**: 1 thuốc - Polymyxin B/Trimethoprim eye drops

### anticonvulsants.py

**Module**: neurological

**Tổng số thuốc thiếu**: 6

- **renal_adjustment**: 2 thuốc - Oxcarbazepine, Ethanol
- **contraindications_detail**: 6 thuốc - Ethosuximide, Oxcarbazepine, Perampanel, Primidone, Zonisamide và 1 thuốc khác
- **reversal_agents**: 1 thuốc - Ethanol

### antihistamines.py

**Module**: allergy

**Tổng số thuốc thiếu**: 6

- **renal_adjustment**: 5 thuốc - Desloratadine, Fexofenadine, Loratadine, Chlorpheniramine, Diphenhydramine
- **drug_interactions**: 6 thuốc - Cetirizine, Desloratadine, Fexofenadine, Loratadine, Chlorpheniramine và 1 thuốc khác
- **contraindications_detail**: 4 thuốc - Cetirizine, Desloratadine, Fexofenadine, Loratadine
- **reversal_agents**: 6 thuốc - Cetirizine, Desloratadine, Fexofenadine, Loratadine, Chlorpheniramine và 1 thuốc khác

### triglyceride_lowering.py

**Module**: cardiovascular

**Tổng số thuốc thiếu**: 6

- **contraindications_detail**: 6 thuốc - Evinacumab, Icosapent ethyl, Omega-3 acid ethyl esters, Pemafibrate, Plozasiran và 1 thuốc khác

### combination_inhalers.py

**Module**: respiratory

**Tổng số thuốc thiếu**: 6

- **contraindications_detail**: 6 thuốc - Budesonide/Formoterol inhaler, Fluticasone/Salmeterol inhaler, Fluticasone/Umeclidinium/Vilanterol inhaler, Ipratropium/Salbutamol inhaler, Tiotropium/Olodaterol inhaler và 1 thuốc khác

### beta_lactams.py

**Module**: antimicrobial

**Tổng số thuốc thiếu**: 6

- **contraindications_detail**: 2 thuốc - Doripenem, Meropenem
- **reversal_agents**: 4 thuốc - Ertapenem, Imipenem-cilastatin, Penicillin G, Piperacillin-tazobactam

### nrti.py

**Module**: antimicrobial

**Tổng số thuốc thiếu**: 6

- **reversal_agents**: 6 thuốc - Emtricitabine (FTC), Lamivudine (3TC), Tenofovir alafenamide (TAF), Tenofovir alafenamide/Emtricitabine (TAF/FTC), Tenofovir disoproxil fumarate (TDF) và 1 thuốc khác

### ace_arb.py

**Module**: cardiovascular

**Tổng số thuốc thiếu**: 5

- **renal_adjustment**: 5 thuốc - Enalapril, Lisinopril, Losartan, Telmisartan, Valsartan
- **drug_interactions**: 4 thuốc - Enalapril, Lisinopril, Losartan, Telmisartan
- **contraindications_detail**: 3 thuốc - Enalapril, Telmisartan, Valsartan
- **reversal_agents**: 5 thuốc - Enalapril, Lisinopril, Losartan, Telmisartan, Valsartan

### statins.py

**Module**: cardiovascular

**Tổng số thuốc thiếu**: 5

- **renal_adjustment**: 2 thuốc - Atorvastatin, Rosuvastatin
- **contraindications_detail**: 3 thuốc - Atorvastatin, Rosuvastatin, Niacin
- **reversal_agents**: 4 thuốc - Atorvastatin, Simvastatin, Rosuvastatin, Pravastatin

### dihydropyridines.py

**Module**: cardiovascular

**Tổng số thuốc thiếu**: 5

- **renal_adjustment**: 2 thuốc - Amlodipine, Lacidipine
- **contraindications_detail**: 4 thuốc - Amlodipine, Lacidipine, Nicardipine, Nisoldipine
- **reversal_agents**: 1 thuốc - Clevidipine

