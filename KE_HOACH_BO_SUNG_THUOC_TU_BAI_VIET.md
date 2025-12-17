# 📋 Kế Hoạch Bổ Sung Thuốc Từ Các Bài Viết Chuyên Sâu

**Ngày tạo:** 2025-02-05  
**Cơ sở:** Phân tích các bài viết chuyên sâu trong `docs/articles/`  
**Mục tiêu:** Bổ sung các thuốc quan trọng được đề cập trong bài viết nhưng chưa có trong database

---

## 📊 TỔNG QUAN

### **Trạng thái hiện tại:**
- ✅ **Đã có:** 300 thuốc
- ⏳ **Cần bổ sung:** ~50-70 thuốc từ các bài viết
- 📚 **Nguồn tham khảo:** 21 bài viết chuyên sâu

### **Phương pháp:**
1. Rà soát từng bài viết để liệt kê thuốc được đề cập
2. So sánh với database hiện tại
3. Ưu tiên hóa theo mức độ quan trọng và tần suất sử dụng
4. Lập kế hoạch bổ sung theo từng nhóm

---

## 🔍 PHÂN TÍCH THEO BÀI VIẾT

### **1. Bronchodilators COPD/Asthma** (`bronchodilators_copd_asthma.md`)

#### **Thuốc đã có:**
- ✅ Salbutamol (Albuterol)
- ✅ Formoterol
- ✅ Tiotropium
- ✅ Ipratropium
- ✅ Fluticasone
- ✅ Budesonide
- ✅ Beclomethasone
- ✅ Theophylline

#### **Thuốc cần bổ sung:**

| STT | Tên Thuốc | Nhóm | File Module | Ưu Tiên | Ghi Chú |
|-----|-----------|------|-------------|---------|---------|
| 1 | **Terbutaline** | SABA | `respiratory/short_acting_beta_2_agonist_sabas.py` | 🔥🔥 | Thay thế salbutamol, dùng SC trong cấp cứu |
| 2 | **Salmeterol** | LABA | `respiratory/long_acting_beta_2_agonist_labas.py` | 🔥🔥🔥 | Kết hợp với fluticasone, rất phổ biến |
| 3 | **Indacaterol** | LABA | `respiratory/long_acting_beta_2_agonist_labas.py` | 🔥🔥 | Dùng 1 lần/ngày, thuận tiện |
| 4 | **Olodaterol** | LABA | `respiratory/long_acting_beta_2_agonist_labas.py` | 🔥 | Kết hợp với tiotropium |
| 5 | **Vilanterol** | LABA | `respiratory/long_acting_beta_2_agonist_labas.py` | 🔥 | Kết hợp với umeclidinium/fluticasone |
| 6 | **Aclidinium** | LAMA | `respiratory/anticholinergic_long_actings.py` | 🔥🔥 | Kết hợp với formoterol |
| 7 | **Glycopyrronium (Glycopyrrolate)** | LAMA | `respiratory/anticholinergic_long_actings.py` | 🔥🔥 | Kết hợp với indacaterol |
| 8 | **Umeclidinium** | LAMA | `respiratory/anticholinergic_long_actings.py` | 🔥🔥 | Kết hợp với vilanterol |
| 9 | **Ciclesonide** | ICS | `respiratory/inhaled_corticosteroids.py` | 🔥 | Ít tác dụng phụ hơn, prodrug |

**Tổng:** 9 thuốc

---

### **2. Psychotropic Medications** (`psychotropic_medications.md`)

#### **Thuốc đã có:**
- ✅ Fluoxetine, Sertraline, Citalopram, Escitalopram, Paroxetine (SSRI)
- ✅ Venlafaxine, Duloxetine (SNRI)
- ✅ Amitriptyline, Imipramine, Nortriptyline (TCA)
- ✅ Haloperidol, Risperidone, Olanzapine, Quetiapine, Aripiprazole (Antipsychotics)
- ✅ Lithium, Valproate, Carbamazepine, Lamotrigine (Mood stabilizers)
- ✅ Alprazolam, Lorazepam, Diazepam, Clonazepam (Benzodiazepines)
- ✅ Pregabalin, Gabapentin

#### **Thuốc cần bổ sung:**

| STT | Tên Thuốc | Nhóm | File Module | Ưu Tiên | Ghi Chú |
|-----|-----------|------|-------------|---------|---------|
| 1 | **Fluvoxamine** | SSRI | `psychiatry_other/antidepressants.py` | 🔥🔥 | Dùng cho OCD, nhiều tương tác CYP450 |
| 2 | **Desvenlafaxine** | SNRI | `psychiatry_other/antidepressants.py` | 🔥 | Metabolite của venlafaxine |
| 3 | **Clomipramine** | TCA | `psychiatry_other/antidepressants.py` | 🔥🔥 | Dùng cho OCD |
| 4 | **Bupropion** | NDRI | `psychiatry_other/antidepressants.py` | 🔥🔥🔥 | Cai thuốc lá, không gây rối loạn tình dục |
| 5 | **Mirtazapine** | Tetracyclic | `psychiatry_other/antidepressants.py` | 🔥🔥🔥 | Tăng cân, an thần, dùng buổi tối |
| 6 | **Trazodone** | SARI | `psychiatry_other/antidepressants.py` | 🔥🔥 | Mất ngủ, cảnh giác priapism |
| 7 | **Phenelzine** | MAOI | `psychiatry_other/antidepressants.py` | 🔥 | Trầm cảm kháng trị, chế độ ăn tyramine |
| 8 | **Tranylcypromine** | MAOI | `psychiatry_other/antidepressants.py` | 🔥 | Trầm cảm kháng trị |
| 9 | **Chlorpromazine** | Typical Antipsychotic | `psychiatry_other/antipsychotics.py` | 🔥🔥 | Thuốc cổ điển, dùng cho nôn mửa |
| 10 | **Fluphenazine** | Typical Antipsychotic | `psychiatry_other/antipsychotics.py` | 🔥 | Ít dùng hơn |
| 11 | **Ziprasidone** | Atypical Antipsychotic | `psychiatry_other/antipsychotics.py` | 🔥🔥 | QTc kéo dài, cần theo dõi ECG |
| 12 | **Clozapine** | Atypical Antipsychotic | `psychiatry_other/antipsychotics.py` | 🔥🔥🔥 | Kháng trị, cần theo dõi công thức máu |
| 13 | **Lurasidone** | Atypical Antipsychotic | `psychiatry_other/antipsychotics.py` | 🔥 | Ít tăng cân |
| 14 | **Buspirone** | Anxiolytic | `psychiatry_other/anxiolytics.py` | 🔥🔥 | Không gây lệ thuộc, an toàn hơn BZD |
| 15 | **Methylphenidate** | ADHD | `psychiatry_other/adhd_medications.py` | 🔥🔥 | ADHD, narcolepsy |
| 16 | **Dextroamphetamine** | ADHD | `psychiatry_other/adhd_medications.py` | 🔥 | ADHD, narcolepsy |
| 17 | **Lisdexamfetamine** | ADHD | `psychiatry_other/adhd_medications.py` | 🔥 | Prodrug, ít lệ thuộc hơn |
| 18 | **Atomoxetine** | ADHD | `psychiatry_other/adhd_medications.py` | 🔥🔥 | Không gây lệ thuộc, không phải chất kiểm soát |
| 19 | **Donepezil** | Dementia | `psychiatry_other/dementia_medications.py` | 🔥🔥🔥 | Alzheimer, rất phổ biến |
| 20 | **Rivastigmine** | Dementia | `psychiatry_other/dementia_medications.py` | 🔥🔥 | Alzheimer, Parkinson dementia, có patch |
| 21 | **Memantine** | Dementia | `psychiatry_other/dementia_medications.py` | 🔥🔥 | Alzheimer trung bình-nặng |

**Tổng:** 21 thuốc

---

### **3. Pain Relief & Anti-inflammatory** (`pain_relief_antiinflammatory.md`)

#### **Thuốc đã có:**
- ✅ Paracetamol
- ✅ Ibuprofen, Naproxen, Diclofenac
- ✅ Ketorolac
- ✅ Morphine, Tramadol, Fentanyl, Oxycodone, Hydromorphone
- ✅ Prednisone, Methylprednisolone

#### **Thuốc cần bổ sung:**

| STT | Tên Thuốc | Nhóm | File Module | Ưu Tiên | Ghi Chú |
|-----|-----------|------|-------------|---------|---------|
| 1 | **Celecoxib** | COX-2 Selective NSAID | `analgesics/nsaids.py` | 🔥🔥 | Ít tác dụng phụ GI, nhưng tăng nguy cơ tim mạch |
| 2 | **Etoricoxib** | COX-2 Selective NSAID | `analgesics/nsaids.py` | 🔥 | Tương tự celecoxib |
| 3 | **Codeine** | Opioid Weak | `analgesics/opioid_agonist_weaks.py` | 🔥🔥 | WHO bước 2, ho |
| 4 | **Hydrocodone** | Opioid Strong | `analgesics/opioid_agonist_strongs.py` | 🔥 | Kết hợp với paracetamol |

**Tổng:** 4 thuốc

---

### **4. Antiallergy Medications** (`antiallergy_medications.md`)

#### **Thuốc đã có:**
- ✅ Cetirizine, Loratadine, Fexofenadine
- ✅ Prednisone, Methylprednisolone
- ✅ Montelukast

#### **Thuốc cần bổ sung:**

| STT | Tên Thuốc | Nhóm | File Module | Ưu Tiên | Ghi Chú |
|-----|-----------|------|-------------|---------|---------|
| 1 | **Diphenhydramine** | H1 Antihistamine Gen 1 | `miscellaneous/antihistamines.py` | 🔥🔥🔥 | Phản vệ, mất ngủ, rất phổ biến |
| 2 | **Chlorpheniramine** | H1 Antihistamine Gen 1 | `miscellaneous/antihistamines.py` | 🔥🔥 | Dị ứng nhẹ-trung bình |
| 3 | **Hydroxyzine** | H1 Antihistamine Gen 1 | `miscellaneous/antihistamines.py` | 🔥🔥 | Urticaria, lo âu, mất ngủ |
| 4 | **Desloratadine** | H1 Antihistamine Gen 2 | `miscellaneous/antihistamines.py` | 🔥 | Metabolite của loratadine |
| 5 | **Levocetirizine** | H1 Antihistamine Gen 2 | `miscellaneous/antihistamines.py` | 🔥 | Enantiomer của cetirizine |
| 6 | **Zafirlukast** | Leukotriene Modifier | `respiratory/leukotriene_modifiers.py` | 🔥 | Asthma, tương tác warfarin |
| 7 | **Cromolyn Sodium** | Mast Cell Stabilizer | `respiratory/mast_cell_stabilizers.py` | 🔥 | Dự phòng, mũi/mắt/hít |
| 8 | **Nedocromil** | Mast Cell Stabilizer | `respiratory/mast_cell_stabilizers.py` | 🔥 | Mắt, dự phòng |
| 9 | **Ranitidine** | H2 Antagonist | `gastrointestinal/h2_blockers.py` | 🔥🔥 | Phản vệ hỗ trợ (mặc dù ít dùng cho GERD) |
| 10 | **Famotidine** | H2 Antagonist | `gastrointestinal/h2_blockers.py` | 🔥🔥 | Phản vệ hỗ trợ |

**Tổng:** 10 thuốc

---

### **5. Atrial Fibrillation** (`atrial_fibrillation.md`)

#### **Thuốc đã có:**
- ✅ Apixaban, Rivaroxaban, Dabigatran, Edoxaban (DOAC)
- ✅ Warfarin
- ✅ Metoprolol, Bisoprolol, Atenolol
- ✅ Diltiazem, Verapamil
- ✅ Digoxin
- ✅ Amiodarone

#### **Thuốc cần bổ sung:**

| STT | Tên Thuốc | Nhóm | File Module | Ưu Tiên | Ghi Chú |
|-----|-----------|------|-------------|---------|---------|
| 1 | **Flecainide** | Antiarrhythmic Class IC | `cardiovascular/antiarrhythmics.py` | 🔥🔥🔥 | Chuyển nhịp, duy trì nhịp xoang, không có bệnh tim cấu trúc |
| 2 | **Propafenone** | Antiarrhythmic Class IC | `cardiovascular/antiarrhythmics.py` | 🔥🔥 | Tương tự flecainide |
| 3 | **Sotalol** | Antiarrhythmic Class III | `cardiovascular/antiarrhythmics.py` | 🔥🔥 | Duy trì nhịp xoang, theo dõi QTc |
| 4 | **Dronedarone** | Antiarrhythmic Class III | `cardiovascular/antiarrhythmics.py` | 🔥 | Tránh nếu suy tim nặng, CrCl <30 |
| 5 | **Ibutilide** | Antiarrhythmic Class III | `cardiovascular/antiarrhythmics.py` | 🔥 | Chuyển nhịp IV, không có QT kéo dài |
| 6 | **Procainamide** | Antiarrhythmic Class IA | `cardiovascular/antiarrhythmics.py` | 🔥 | AF với WPW |

**Tổng:** 6 thuốc

---

### **6. Hypertension** (`hypertension.md`)

#### **Thuốc đã có:**
- ✅ ACE inhibitors (Lisinopril, Enalapril, Captopril, Ramipril, Perindopril)
- ✅ ARBs (Losartan, Valsartan, Irbesartan, Telmisartan, Olmesartan)
- ✅ CCB (Amlodipine, Nifedipine, Verapamil, Diltiazem)
- ✅ Thiazide (Hydrochlorothiazide)
- ✅ Beta-blockers (Metoprolol, Bisoprolol, Atenolol, Propranolol)
- ✅ Spironolactone

#### **Thuốc cần bổ sung:**

| STT | Tên Thuốc | Nhóm | File Module | Ưu Tiên | Ghi Chú |
|-----|-----------|------|-------------|---------|---------|
| 1 | **Chlorthalidone** | Thiazide-like | `cardiovascular/diuretics.py` | 🔥🔥🔥 | Ưu tiên hơn HCTZ theo ESC/ESH 2023 |
| 2 | **Indapamide** | Thiazide-like | `cardiovascular/diuretics.py` | 🔥🔥🔥 | Ưu tiên hơn HCTZ, ít hạ kali hơn |
| 3 | **Lacidipine** | CCB Dihydropyridine | `cardiovascular/calcium_blockers/dihydropyridines.py` | 🔥 | Được đề cập trong bài viết |
| 4 | **Eplerenone** | MRA | `cardiovascular/diuretics.py` | 🔥🔥 | Thay thế spironolactone nếu không dung nạp |

**Tổng:** 4 thuốc

---

### **7. Acid Suppression** (`acid_suppression.md`)

#### **Thuốc đã có:**
- ✅ Omeprazole, Pantoprazole, Esomeprazole, Lansoprazole, Rabeprazole
- ✅ Ranitidine, Famotidine

#### **Thuốc cần bổ sung:**
- ✅ Tất cả đã có đầy đủ

**Tổng:** 0 thuốc

---

### **8. Topical Medications** (`topical_medications.md`)

#### **Thuốc cần bổ sung (rất nhiều):**

| STT | Tên Thuốc | Nhóm | File Module | Ưu Tiên | Ghi Chú |
|-----|-----------|------|-------------|---------|---------|
| 1 | **Mupirocin** | Topical Antibiotic | `miscellaneous/topical_medications.py` | 🔥🔥🔥 | Nhiễm khuẩn da, rất phổ biến |
| 2 | **Fusidic Acid** | Topical Antibiotic | `miscellaneous/topical_medications.py` | 🔥🔥 | Nhiễm khuẩn da, đặc biệt S. aureus |
| 3 | **Clindamycin (topical)** | Topical Antibiotic | `miscellaneous/topical_medications.py` | 🔥🔥 | Mụn trứng cá |
| 4 | **Erythromycin (topical)** | Topical Antibiotic | `miscellaneous/topical_medications.py` | 🔥 | Mụn trứng cá, kháng thuốc cao |
| 5 | **Metronidazole (topical)** | Topical Antibiotic | `miscellaneous/topical_medications.py` | 🔥🔥 | Rosacea |
| 6 | **Clotrimazole (topical)** | Topical Antifungal | `miscellaneous/topical_medications.py` | 🔥🔥🔥 | Nấm da, rất phổ biến |
| 7 | **Miconazole (topical)** | Topical Antifungal | `miscellaneous/topical_medications.py` | 🔥🔥 | Nấm da, candida |
| 8 | **Ketoconazole (topical)** | Topical Antifungal | `miscellaneous/topical_medications.py` | 🔥🔥 | Nấm da, viêm da tiết bã, có shampoo |
| 9 | **Econazole (topical)** | Topical Antifungal | `miscellaneous/topical_medications.py` | 🔥 | Nấm da |
| 10 | **Terbinafine (topical)** | Topical Antifungal | `miscellaneous/topical_medications.py` | 🔥🔥🔥 | Nấm da, hiệu quả cao |
| 11 | **Nystatin (topical)** | Topical Antifungal | `miscellaneous/topical_medications.py` | 🔥🔥🔥 | Nấm candida, rất phổ biến |
| 12 | **Tretinoin (topical)** | Topical Retinoid | `miscellaneous/topical_medications.py` | 🔥🔥🔥 | Mụn trứng cá, lão hóa da |
| 13 | **Adapalene (topical)** | Topical Retinoid | `miscellaneous/topical_medications.py` | 🔥🔥 | Mụn trứng cá, ít kích ứng hơn tretinoin |
| 14 | **Tazarotene (topical)** | Topical Retinoid | `miscellaneous/topical_medications.py` | 🔥 | Vẩy nến, mụn trứng cá |
| 15 | **Tacrolimus (topical)** | Topical Calcineurin Inhibitor | `miscellaneous/topical_medications.py` | 🔥🔥🔥 | Viêm da cơ địa, an toàn hơn corticosteroid dài hạn |
| 16 | **Pimecrolimus (topical)** | Topical Calcineurin Inhibitor | `miscellaneous/topical_medications.py` | 🔥🔥 | Viêm da cơ địa nhẹ |
| 17 | **Calcipotriol (topical)** | Topical Vitamin D Analogue | `miscellaneous/topical_medications.py` | 🔥🔥 | Vẩy nến |
| 18 | **Calcitriol (topical)** | Topical Vitamin D Analogue | `miscellaneous/topical_medications.py` | 🔥 | Vẩy nến |
| 19 | **Benzoyl Peroxide (topical)** | Topical Acne Treatment | `miscellaneous/topical_medications.py` | 🔥🔥🔥 | Mụn trứng cá, rất phổ biến |
| 20 | **Azelaic Acid (topical)** | Topical Acne Treatment | `miscellaneous/topical_medications.py` | 🔥🔥 | Mụn trứng cá, rosacea, melasma |
| 21 | **Salicylic Acid (topical)** | Topical Keratolytic | `miscellaneous/topical_medications.py` | 🔥🔥 | Mụn trứng cá, vẩy nến, mụn cóc |
| 22 | **Diclofenac (topical gel)** | Topical NSAID | `miscellaneous/topical_medications.py` | 🔥🔥 | Đau cơ xương khớp |
| 23 | **Ketoprofen (topical gel)** | Topical NSAID | `miscellaneous/topical_medications.py` | 🔥 | Đau cơ xương khớp |
| 24 | **Hydrocortisone (topical)** | Topical Corticosteroid | `miscellaneous/topical_medications.py` | 🔥🔥🔥 | Eczema nhẹ, rất phổ biến |
| 25 | **Triamcinolone (topical)** | Topical Corticosteroid | `miscellaneous/topical_medications.py` | 🔥🔥 | Eczema, viêm da tiếp xúc |
| 26 | **Betamethasone (topical)** | Topical Corticosteroid | `miscellaneous/topical_medications.py` | 🔥🔥 | Eczema, vẩy nến |
| 27 | **Mometasone (topical)** | Topical Corticosteroid | `miscellaneous/topical_medications.py` | 🔥🔥 | Eczema, vẩy nến |
| 28 | **Clobetasol (topical)** | Topical Corticosteroid | `miscellaneous/topical_medications.py` | 🔥🔥 | Vẩy nến nặng, lichen planus |
| 29 | **Permethrin (topical)** | Topical Antiparasitic | `miscellaneous/topical_medications.py` | 🔥🔥🔥 | Ghẻ, chấy, rất phổ biến |
| 30 | **Ivermectin (topical cream)** | Topical Antiparasitic | `miscellaneous/topical_medications.py` | 🔥 | Rosacea |

**Tổng:** 30 thuốc (có thể tách thành các nhóm nhỏ hơn)

---

### **9. Electrolyte Disorders** (`electrolyte_disorders.md`)

#### **Thuốc cần bổ sung:**

| STT | Tên Thuốc | Nhóm | File Module | Ưu Tiên | Ghi Chú |
|-----|-----------|------|-------------|---------|---------|
| 1 | **Calcium Gluconate** | Electrolyte Replacement | `emergency/electrolyte_replacements.py` | 🔥🔥🔥 | Tăng kali cấp cứu, hạ canxi, rất quan trọng |
| 2 | **Calcium Chloride** | Electrolyte Replacement | `emergency/electrolyte_replacements.py` | 🔥🔥 | Tăng kali cấp cứu (nếu không có đường ngoại vi tốt) |
| 3 | **Sodium Bicarbonate** | Electrolyte Replacement | `emergency/electrolyte_replacements.py` | 🔥🔥🔥 | Tăng kali (nếu toan chuyển hóa), rất quan trọng |
| 4 | **Sodium Polystyrene Sulfonate (Kayexalate)** | Potassium Binder | `emergency/electrolyte_replacements.py` | 🔥🔥 | Tăng kali, tăng thải K+ |
| 5 | **Sodium Phosphate** | Electrolyte Replacement | `emergency/electrolyte_replacements.py` | 🔥 | Hạ phospho |
| 6 | **Potassium Phosphate** | Electrolyte Replacement | `emergency/electrolyte_replacements.py` | 🔥 | Hạ phospho, hạ kali |
| 7 | **Magnesium Sulfate** | Electrolyte Replacement | `emergency/electrolyte_replacements.py` | 🔥🔥🔥 | Hạ magie, tiền sản giật, rất quan trọng |
| 8 | **Magnesium Oxide** | Electrolyte Replacement | `emergency/electrolyte_replacements.py` | 🔥 | Hạ magie PO |
| 9 | **Demeclocycline** | SIADH Treatment | `miscellaneous/siadh_treatment.py` | 🔥 | SIADH, hạ natri euvolemic |
| 10 | **Zoledronic Acid** | Hypercalcemia Treatment | `miscellaneous/hypercalcemia_treatment.py` | 🔥🔥 | Tăng canxi, bisphosphonate |
| 11 | **Pamidronate** | Hypercalcemia Treatment | `miscellaneous/hypercalcemia_treatment.py` | 🔥 | Tăng canxi, bisphosphonate |
| 12 | **Calcitonin** | Hypercalcemia Treatment | `miscellaneous/hypercalcemia_treatment.py` | 🔥 | Tăng canxi, tác dụng nhanh |

**Tổng:** 12 thuốc

---

### **10. Sepsis Bundle** (`sepsis_bundle.md`)

#### **Thuốc đã có:**
- ✅ Piperacillin-Tazobactam
- ✅ Cefepime
- ✅ Vancomycin
- ✅ Meropenem
- ✅ Metronidazole
- ✅ Norepinephrine
- ✅ Epinephrine
- ✅ Hydrocortisone

#### **Thuốc cần bổ sung:**

| STT | Tên Thuốc | Nhóm | File Module | Ưu Tiên | Ghi Chú |
|-----|-----------|------|-------------|---------|---------|
| 1 | **Vasopressin** | Vasopressor | `emergency/vasopressors.py` | 🔥🔥🔥 | Septic shock, thêm vào norepinephrine, rất quan trọng |
| 2 | **Linezolid** | Antibiotic (Oxazolidinone) | `antimicrobial/antibiotics/other_antibiotics.py` | 🔥🔥 | MRSA, viêm phổi, thay thế vancomycin |

**Tổng:** 2 thuốc

---

## 📊 TỔNG KẾT

### **Tổng số thuốc cần bổ sung:** ~98 thuốc

#### **Phân bổ theo ưu tiên:**

**🔥🔥🔥 Ưu tiên cao (30 thuốc):**
- Salmeterol, Terbutaline (Respiratory)
- Bupropion, Mirtazapine, Trazodone, Donepezil, Rivastigmine, Memantine (Psychiatry)
- Diphenhydramine, Chlorpheniramine, Hydroxyzine (Antihistamines)
- Flecainide, Propafenone (Antiarrhythmics)
- Chlorthalidone, Indapamide (Diuretics)
- Mupirocin, Terbinafine, Nystatin, Tretinoin, Tacrolimus, Benzoyl Peroxide, Permethrin (Topical)
- Calcium Gluconate, Sodium Bicarbonate, Magnesium Sulfate (Electrolytes)
- Vasopressin (Vasopressor)

**🔥🔥 Ưu tiên trung bình (35 thuốc):**
- Indacaterol, Aclidinium, Glycopyrronium, Umeclidinium (Respiratory)
- Fluvoxamine, Clomipramine, Chlorpromazine, Ziprasidone, Clozapine, Buspirone, Methylphenidate, Atomoxetine (Psychiatry)
- Celecoxib, Codeine (Analgesics)
- Desloratadine, Levocetirizine, Zafirlukast, Cromolyn, Ranitidine, Famotidine (Antiallergy)
- Sotalol, Ibutilide (Antiarrhythmics)
- Eplerenone (Diuretics)
- Clindamycin, Fusidic Acid, Metronidazole, Clotrimazole, Miconazole, Ketoconazole, Adapalene, Pimecrolimus, Calcipotriol, Diclofenac gel, Hydrocortisone, Triamcinolone, Betamethasone, Mometasone, Clobetasol (Topical)
- Calcium Chloride, Kayexalate, Zoledronic Acid (Electrolytes)
- Linezolid (Antibiotic)

**🔥 Ưu tiên thấp (33 thuốc):**
- Olodaterol, Vilanterol, Ciclesonide (Respiratory)
- Desvenlafaxine, Phenelzine, Tranylcypromine, Fluphenazine, Lurasidone, Dextroamphetamine, Lisdexamfetamine (Psychiatry)
- Etoricoxib, Hydrocodone (Analgesics)
- Nedocromil (Antiallergy)
- Dronedarone, Procainamide (Antiarrhythmics)
- Lacidipine (CCB)
- Erythromycin, Econazole, Tazarotene, Calcitriol, Azelaic Acid, Salicylic Acid, Ketoprofen gel, Ivermectin cream (Topical)
- Sodium Phosphate, Potassium Phosphate, Magnesium Oxide, Demeclocycline, Pamidronate, Calcitonin (Electrolytes)

---

## 🎯 KẾ HOẠCH THỰC HIỆN

### **Phase 1: Ưu tiên cao (30 thuốc) - Tuần 1-2**

**Nhóm 1: Respiratory (2 thuốc)**
- Salmeterol
- Terbutaline

**Nhóm 2: Psychiatry (6 thuốc)**
- Bupropion
- Mirtazapine
- Trazodone
- Donepezil
- Rivastigmine
- Memantine

**Nhóm 3: Antihistamines (3 thuốc)**
- Diphenhydramine
- Chlorpheniramine
- Hydroxyzine

**Nhóm 4: Antiarrhythmics (2 thuốc)**
- Flecainide
- Propafenone

**Nhóm 5: Diuretics (2 thuốc)**
- Chlorthalidone
- Indapamide

**Nhóm 6: Topical (7 thuốc)**
- Mupirocin
- Terbinafine
- Nystatin
- Tretinoin
- Tacrolimus
- Benzoyl Peroxide
- Permethrin

**Nhóm 7: Electrolytes (3 thuốc)**
- Calcium Gluconate
- Sodium Bicarbonate
- Magnesium Sulfate

**Nhóm 8: Emergency (1 thuốc)**
- Vasopressin

---

### **Phase 2: Ưu tiên trung bình (35 thuốc) - Tuần 3-4**

**Nhóm 1: Respiratory (4 thuốc)**
- Indacaterol
- Aclidinium
- Glycopyrronium
- Umeclidinium

**Nhóm 2: Psychiatry (8 thuốc)**
- Fluvoxamine
- Clomipramine
- Chlorpromazine
- Ziprasidone
- Clozapine
- Buspirone
- Methylphenidate
- Atomoxetine

**Nhóm 3: Analgesics (2 thuốc)**
- Celecoxib
- Codeine

**Nhóm 4: Antiallergy (6 thuốc)**
- Desloratadine
- Levocetirizine
- Zafirlukast
- Cromolyn
- Ranitidine (nếu chưa có)
- Famotidine (nếu chưa có)

**Nhóm 5: Antiarrhythmics (2 thuốc)**
- Sotalol
- Ibutilide

**Nhóm 6: Diuretics (1 thuốc)**
- Eplerenone

**Nhóm 7: Topical (10 thuốc)**
- Clindamycin
- Fusidic Acid
- Metronidazole
- Clotrimazole
- Miconazole
- Ketoconazole
- Adapalene
- Pimecrolimus
- Calcipotriol
- Diclofenac gel

**Nhóm 8: Topical Corticosteroids (4 thuốc)**
- Hydrocortisone
- Triamcinolone
- Betamethasone
- Mometasone
- Clobetasol

**Nhóm 9: Electrolytes (3 thuốc)**
- Calcium Chloride
- Kayexalate
- Zoledronic Acid

**Nhóm 10: Antibiotics (1 thuốc)**
- Linezolid

---

### **Phase 3: Ưu tiên thấp (33 thuốc) - Tuần 5-6**

Bổ sung các thuốc còn lại theo danh sách trên.

---

## 📝 HƯỚNG DẪN BỔ SUNG

### **Bước 1: Xác định file module**
- Xem cột "File Module" trong bảng trên
- Mở file tương ứng trong `drugs/drug_modules/`

### **Bước 2: Thêm thuốc vào dictionary**
- Copy format từ thuốc tương tự trong cùng file
- Đảm bảo có đầy đủ enhanced_fields:
  - `mechanism_of_action`
  - `pharmacokinetics`
  - `monitoring`
  - `precautions`
  - `storage`
  - `black_box_warnings` (nếu có)
  - `drug_interactions` (optional)
  - `contraindications` (optional)
  - `pregnancy_lactation` (optional)
  - `hepatic_adjustment` (optional)
  - `renal_adjustment` (optional)
  - `overdose_management` (optional)
  - `reversal_agents` (optional)
  - `administration_instructions` (optional)
  - `references` (optional)

### **Bước 3: Validate**
```bash
python -c "from drugs.drug_database import TOTAL_DRUGS; print(f'Total: {TOTAL_DRUGS}')"
```

### **Bước 4: Cập nhật checklist**
- Đánh dấu ✅ khi hoàn thành
- Cập nhật số thuốc hiện tại

---

## ✅ CHECKLIST TIẾN ĐỘ

### **Phase 1: Ưu tiên cao (30 thuốc)**
- [ ] Salmeterol
- [ ] Terbutaline
- [ ] Bupropion
- [ ] Mirtazapine
- [ ] Trazodone
- [ ] Donepezil
- [ ] Rivastigmine
- [ ] Memantine
- [ ] Diphenhydramine
- [ ] Chlorpheniramine
- [ ] Hydroxyzine
- [ ] Flecainide
- [ ] Propafenone
- [ ] Chlorthalidone
- [ ] Indapamide
- [ ] Mupirocin
- [ ] Terbinafine
- [ ] Nystatin
- [ ] Tretinoin
- [ ] Tacrolimus (topical)
- [ ] Benzoyl Peroxide
- [ ] Permethrin
- [ ] Calcium Gluconate
- [ ] Sodium Bicarbonate
- [ ] Magnesium Sulfate
- [ ] Vasopressin

### **Phase 2: Ưu tiên trung bình (35 thuốc)**
- [ ] Indacaterol
- [ ] Aclidinium
- [ ] Glycopyrronium
- [ ] Umeclidinium
- [ ] Fluvoxamine
- [ ] Clomipramine
- [ ] Chlorpromazine
- [ ] Ziprasidone
- [ ] Clozapine
- [ ] Buspirone
- [ ] Methylphenidate
- [ ] Atomoxetine
- [ ] Celecoxib
- [ ] Codeine
- [ ] Desloratadine
- [ ] Levocetirizine
- [ ] Zafirlukast
- [ ] Cromolyn
- [ ] Sotalol
- [ ] Ibutilide
- [ ] Eplerenone
- [ ] Clindamycin (topical)
- [ ] Fusidic Acid
- [ ] Metronidazole (topical)
- [ ] Clotrimazole (topical)
- [ ] Miconazole (topical)
- [ ] Ketoconazole (topical)
- [ ] Adapalene
- [ ] Pimecrolimus
- [ ] Calcipotriol
- [ ] Diclofenac gel
- [ ] Hydrocortisone (topical)
- [ ] Triamcinolone (topical)
- [ ] Betamethasone (topical)
- [ ] Mometasone (topical)
- [ ] Clobetasol (topical)
- [ ] Calcium Chloride
- [ ] Kayexalate
- [ ] Zoledronic Acid
- [ ] Linezolid

### **Phase 3: Ưu tiên thấp (33 thuốc)**
- [ ] Olodaterol
- [ ] Vilanterol
- [ ] Ciclesonide
- [ ] Desvenlafaxine
- [ ] Phenelzine
- [ ] Tranylcypromine
- [ ] Fluphenazine
- [ ] Lurasidone
- [ ] Dextroamphetamine
- [ ] Lisdexamfetamine
- [ ] Etoricoxib
- [ ] Hydrocodone
- [ ] Nedocromil
- [ ] Dronedarone
- [ ] Procainamide
- [ ] Lacidipine
- [ ] Erythromycin (topical)
- [ ] Econazole (topical)
- [ ] Tazarotene
- [ ] Calcitriol (topical)
- [ ] Azelaic Acid
- [ ] Salicylic Acid
- [ ] Ketoprofen gel
- [ ] Ivermectin cream
- [ ] Sodium Phosphate
- [ ] Potassium Phosphate
- [ ] Magnesium Oxide
- [ ] Demeclocycline
- [ ] Pamidronate
- [ ] Calcitonin

---

## 📚 TÀI LIỆU THAM KHẢO

- `docs/articles/bronchodilators_copd_asthma.md`
- `docs/articles/psychotropic_medications.md`
- `docs/articles/pain_relief_antiinflammatory.md`
- `docs/articles/antiallergy_medications.md`
- `docs/articles/atrial_fibrillation.md`
- `docs/articles/hypertension.md`
- `docs/articles/acid_suppression.md`
- `docs/articles/topical_medications.md`
- `docs/articles/electrolyte_disorders.md`
- `docs/articles/sepsis_bundle.md`
- `DANH_SACH_THUOC_CAN_BO_SUNG_2025_02_05.md`
- `drugs/DRUG_EXPANSION_PLAN.md`

---

**Cập nhật lần cuối:** 2025-02-05  
**Trạng thái:** 📋 Kế hoạch đã được lập  
**Tiếp theo:** Bắt đầu Phase 1 - Ưu tiên cao

