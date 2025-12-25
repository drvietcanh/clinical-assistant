## 📋 Lộ Trình Hoàn Thiện Dữ Liệu Thuốc & Chia Phiên Làm Việc

**Ngày tạo:** 2025-12-23  
**Hiện trạng:** ~644 thuốc, enhanced fields đã phủ rộng nhưng còn thiếu một phần các trường lâm sàng nâng cao (interactions chi tiết, thai kỳ/cho bú, suy gan, quá liều, hướng dẫn truyền, risk flags).  
**Mục tiêu:**  
- Hoàn thiện chất lượng cho khoảng 150–200 thuốc “trụ cột” (ICU, cấp cứu, tim mạch, tiểu đường, hô hấp, thần kinh, ung thư).  
- Bổ sung thêm 30–40 thuốc chiến lược (ARV, HBV/HCV, lao 2nd line, kháng nấm sâu, huyết học/đông máu) trong Giai đoạn 2.  
- Mỗi phiên làm việc đều có checklist rõ, có thể dừng/tiếp tục dễ dàng.

---

## 1. Cấu trúc Giai đoạn

| Giai đoạn | Mục tiêu chính | Phạm vi | Kết quả mong đợi |
|----------|----------------|--------|------------------|
| **GĐ 1 – Hoàn thiện chất (Core 150–200 thuốc)** | Đủ 14 fields + risk flags cho bộ thuốc “trụ cột” | ICU, Emergency, Cardiovascular, Diabetes, Respiratory, Neurology, Psychiatry, GI, Oncology chủ lực | Monograph ngang Lexicomp/Micromedex cho các thuốc hay dùng nhất |
| **GĐ 2 – Bổ sung nhóm thuốc chiến lược** | Thêm 30–40 thuốc chiến lược còn thiếu | ARV/HIV, HBV/HCV, Lao 2L, kháng nấm sâu, huyết học/đông máu, một phần biologics | Đủ bộ điều trị HIV, viêm gan, lao kháng thuốc, nấm xâm lấn, đông máu hiện đại |
| **GĐ 3 – Tinh chỉnh & tối ưu UI/filters** | Tối ưu cách tra cứu/tìm thuốc dựa trên schema hiện có | Tất cả module | Tìm kiếm nhanh theo bệnh, risk, cơ quan đích, đối tượng đặc biệt |

---

## 2. Chia nhỏ theo Phiên Làm Việc (Session)

Mỗi **phiên (session)** nên nhắm khoảng **8–12 thuốc**, đủ để làm kỹ 14 fields + risk flags mà không quá tải.

### 2.1. Giai đoạn 1 – Hoàn thiện chất cho Core drugs

#### Session 1 – Emergency & ICU “khung xương sống”

**Mục tiêu:** Đảm bảo tất cả thuốc cấp cứu/ICU chủ lực có đủ 14 fields và `risk_flags` Chi tiết.

| STT | Thuốc | Nhóm | File module gợi ý | Ghi chú |
|-----|-------|------|--------------------|--------|
| 1 | Epinephrine | Emergency – Catecholamine | `drugs/drug_modules/emergency/catecholamines.py` | High-alert, ICU-only, độc tim, dùng ACLS/anaphylaxis |
| 2 | Norepinephrine | Emergency – Catecholamine | `drugs/drug_modules/emergency/catecholamines.py` | Vận mạch chính trong sốc nhiễm trùng |
| 3 | Vasopressin | Emergency – Vasopressor | `drugs/drug_modules/emergency/catecholamines.py` (hoặc file riêng vasopressors) | ICU-only, cần cảnh báo pha/truyền |
| 4 | Dopamine | Emergency – Inotrope/Vasopressor | `drugs/drug_modules/emergency/catecholamines.py` | Hiện dùng ít hơn nhưng vẫn cần dữ liệu chuẩn |
| 5 | Dobutamine | Emergency – Inotrope | `drugs/drug_modules/emergency/inotropes.py` | Suy tim cấp, shock tim |
| 6 | Phenylephrine | Emergency – Vasopressor | `drugs/drug_modules/emergency/catecholamines.py` | Chủ yếu tăng HA, ít tác dụng inotrope |
| 7 | Nitroglycerin | Emergency – Vasodilator | `drugs/drug_modules/cardiovascular/nitrates.py` | Đau ngực, suy tim cấp, cần hướng dẫn truyền chi tiết |
| 8 | Nitroprusside | Emergency – Vasodilator | `drugs/drug_modules/cardiovascular/vasodilators_iv.py` | High-alert, độc cyanide/thiocyanate, cần monitoring sát |

**Checklist Session 1:**
- [ ] Rà lại 14 fields hiện có, bổ sung `drug_interactions`, `pregnancy_lactation`, `hepatic_adjustment`, `overdose_management`, `administration_instructions`, `references`.
- [ ] Điền `risk_flags.high_alert=True`, `icu_critical_care_only=True` nếu phù hợp.
- [ ] Đánh dấu `organ_toxicity.cardiac` và/hoặc `hepatic/renal` theo thực tế.

---

#### Session 2 – An thần, gây mê, giãn cơ trong ICU

| STT | Thuốc | Nhóm | File module gợi ý | Ghi chú |
|-----|-------|------|--------------------|--------|
| 1 | Propofol | ICU Sedative/Anesthetic | `drugs/drug_modules/supportive/icu_sedatives.py` | High-alert, nguy cơ tụt HA, PRIS |
| 2 | Midazolam (IV/ICU) | ICU Sedative | `drugs/drug_modules/supportive/icu_sedatives.py` | Đã có `Midazolam (IV/ICU)` – chuẩn hóa tên & fields |
| 3 | Ketamine | Anesthetic/Analgesic | `drugs/drug_modules/supportive/icu_sedatives.py` hoặc `analgesics/opioid_agonist_strongs.py` | Analgesic + an thần, dùng trong sốc, thủ thuật |
| 4 | Etomidate | Induction agent | `drugs/drug_modules/supportive/icu_sedatives.py` | Ức chế vỏ thượng thận, cần lưu ý đặc biệt |
| 5 | Dexmedetomidine | ICU Sedative | `drugs/drug_modules/supportive/icu_sedatives.py` | Giảm mê, ít ức chế hô hấp, nhiều trên ICU |
| 6 | Rocuronium | NMBA | `drugs/drug_modules/supportive/neuromuscular_blockers.py` | Dùng đặt NKQ, ARDS, cần reverse sugammadex (nếu có) |
| 7 | Vecuronium | NMBA | `drugs/drug_modules/supportive/neuromuscular_blockers.py` | Ảnh hưởng suy gan/thận |
| 8 | Cisatracurium | NMBA | `drugs/drug_modules/supportive/neuromuscular_blockers.py` | Hofmann elimination – an toàn trong suy gan/thận |
| 9 | Succinylcholine | Depolarizing NMBA | `drugs/drug_modules/supportive/neuromuscular_blockers.py` | Nguy cơ tăng K+, MH – cần cảnh báo mạnh |

**Checklist Session 2:**
- [ ] Hoàn thiện 14 fields cho từng thuốc, nhấn mạnh: chỉ định ICU, liều bolus & truyền, thời gian onset/duration.
- [ ] `risk_flags.high_alert=True`, `icu_critical_care_only=True` (đa số).
- [ ] Cảnh báo đặc biệt: tăng K+ (succinylcholine), PRIS (propofol), ức chế vỏ thượng thận (etomidate).

---

#### Session 3 – Cardiovascular “xương sống” (đã có nhưng cần full 14 fields + risk flags)

Tập trung vào các thuốc đã có trong DB nhưng cần chuẩn hóa 14 fields.

| STT | Thuốc | Nhóm | File module | Ghi chú |
|-----|-------|------|------------|--------|
| 1 | Sacubitril/valsartan | Cardiovascular – ARNI | `drugs/drug_modules/cardiovascular/arni.py` | HFREF – cần guideline tags (ESC/ACC) |
| 2 | Metoprolol | Beta-blocker (β1) | `drugs/drug_modules/cardiovascular/beta_blockers/selective.py` | HF, MI, AF – high‑value |
| 3 | Bisoprolol | Beta-blocker (β1) | `drugs/drug_modules/cardiovascular/beta_blockers/selective.py` | HFREF |
| 4 | Carvedilol | Alpha‑beta blocker | `drugs/drug_modules/cardiovascular/beta_blockers/non_selective.py` | HFREF – cần chỉnh liều suy gan |
| 5 | Spironolactone | Aldosterone antagonist | `drugs/drug_modules/cardiovascular/diuretics_potassium_sparing.py` | HFREF, theo dõi K+ & creatinine |
| 6 | Furosemide | Loop diuretic | `drugs/drug_modules/cardiovascular/diuretics_loop.py` | Liều IV/PO, tốc độ truyền, độc tai |
| 7 | Apixaban | DOAC – Xa inhibitor | `drugs/drug_modules/hematology/anticoagulants_doac.py` | AF, VTE – cần `risk_flags` NTI & bleeding |
| 8 | Rivaroxaban | DOAC – Xa inhibitor | `drugs/drug_modules/hematology/anticoagulants_doac.py` | Liều theo CrCl, dùng kèm thức ăn |
| 9 | Dabigatran | DOAC – Thrombin inhibitor | `drugs/drug_modules/hematology/anticoagulants_doac.py` | Idarucizumab as reversal agent |
|10 | Warfarin | VKA | `drugs/drug_modules/hematology/anticoagulants_vka.py` | INR monitoring, interactions, nhiều cảnh báo |

**Checklist Session 3:**
- [ ] Chuẩn hóa `drug_interactions` (đặc biệt với VKA/DOAC).
- [ ] Điền kỹ `hepatic_adjustment`, `pregnancy_lactation`, `overdose_management`, `reversal_agents`.
- [ ] Gắn `risk_flags.narrow_therapeutic_index=True` và high‑alert nếu phù hợp.

---

### 2.2. Giai đoạn 2 – Danh sách 30–40 thuốc nên làm ngay

Các thuốc này chủ yếu **chưa có trong DB** hoặc mới ở mức sơ bộ. Danh sách ưu tiên theo nhóm chiến lược; khi thêm mới, mỗi thuốc phải có **14 fields đầy đủ** ngay từ đầu.

#### Nhóm A – HIV/ARV hiện đại (10 thuốc)

| STT | Thuốc | Nhóm | File module gợi ý | Ưu tiên |
|-----|-------|------|--------------------|--------|
| 1 | Tenofovir disoproxil fumarate (TDF) | ARV – NRTI | `drugs/drug_modules/infectious_other/hiv_arvs_nrtis.py` | 🔥🔥🔥 |
| 2 | Tenofovir alafenamide (TAF) | ARV – NRTI | `drugs/drug_modules/infectious_other/hiv_arvs_nrtis.py` | 🔥🔥🔥 |
| 3 | Emtricitabine (FTC) | ARV – NRTI | `drugs/drug_modules/infectious_other/hiv_arvs_nrtis.py` | 🔥🔥 |
| 4 | Lamivudine (3TC) | ARV – NRTI | `drugs/drug_modules/infectious_other/hiv_arvs_nrtis.py` | 🔥🔥 |
| 5 | Dolutegravir | ARV – INSTI | `drugs/drug_modules/infectious_other/hiv_arvs_instis.py` | 🔥🔥🔥 |
| 6 | Bictegravir | ARV – INSTI | `drugs/drug_modules/infectious_other/hiv_arvs_instis.py` | 🔥🔥 |
| 7 | Cabotegravir (oral) | ARV – INSTI | `drugs/drug_modules/infectious_other/hiv_arvs_instis.py` | 🔥🔥 |
| 8 | Cabotegravir + Rilpivirine (LA inj) | ARV – LA combo | `drugs/drug_modules/infectious_other/hiv_arvs_long_acting.py` | 🔥 |
| 9 | Efavirenz (nếu chưa đủ) | ARV – NNRTI | `drugs/drug_modules/infectious_other/hiv_arvs_nnrti.py` | 🔥 |
|10 | Atazanavir/ritonavir hoặc Darunavir/ritonavir | ARV – PI boosted | `drugs/drug_modules/infectious_other/hiv_arvs_pi.py` | 🔥 |

---

#### Nhóm B – HBV/HCV (6 thuốc)

| STT | Thuốc | Nhóm | File module gợi ý | Ưu tiên |
|-----|-------|------|--------------------|--------|
| 1 | Entecavir | HBV – Nucleoside analog | `drugs/drug_modules/infectious_other/hepatitis_b.py` | 🔥🔥🔥 |
| 2 | Tenofovir disoproxil (TDF) | HBV/HIV overlap | `drugs/drug_modules/infectious_other/hepatitis_b.py` | 🔥🔥🔥 |
| 3 | Tenofovir alafenamide (TAF) | HBV/HIV overlap | `drugs/drug_modules/infectious_other/hepatitis_b.py` | 🔥🔥 |
| 4 | Sofosbuvir/velpatasvir | HCV – DAA combo | `drugs/drug_modules/infectious_other/hepatitis_c_daa.py` | 🔥🔥🔥 |
| 5 | Glecaprevir/pibrentasvir | HCV – DAA combo | `drugs/drug_modules/infectious_other/hepatitis_c_daa.py` | 🔥🔥 |
| 6 | Sofosbuvir/ledipasvir (tùy cân nhắc) | HCV – DAA combo | `drugs/drug_modules/infectious_other/hepatitis_c_daa.py` | 🔥 |

---

#### Nhóm C – Lao 2nd line & MDR-TB (6 thuốc)

| STT | Thuốc | Nhóm | File module gợi ý | Ưu tiên |
|-----|-------|------|--------------------|--------|
| 1 | Bedaquiline | Antitubercular 2L | `drugs/drug_modules/infectious_other/antitubercular_second_line.py` | 🔥🔥🔥 |
| 2 | Delamanid | Antitubercular 2L | `drugs/drug_modules/infectious_other/antitubercular_second_line.py` | 🔥🔥 |
| 3 | Clofazimine | Antimycobacterial | `drugs/drug_modules/infectious_other/antitubercular_second_line.py` | 🔥🔥 |
| 4 | Cycloserine | Antitubercular 2L | `drugs/drug_modules/infectious_other/antitubercular_second_line.py` | 🔥🔥 |
| 5 | Para‑aminosalicylic acid (PAS) | Antitubercular 2L | `drugs/drug_modules/infectious_other/antitubercular_second_line.py` | 🔥 |
| 6 | Linezolid (nếu chưa tag rõ trong TB) | Oxazolidinone for MDR-TB | `drugs/drug_modules/antimicrobial/antibiotics/oxazolidinones.py` + tag TB | 🔥🔥 |

---

#### Nhóm D – Kháng nấm sâu & nấm cơ hội (6 thuốc)

| STT | Thuốc | Nhóm | File module gợi ý | Ưu tiên |
|-----|-------|------|--------------------|--------|
| 1 | Amphotericin B deoxycholate | Antifungal – Polyene | `drugs/drug_modules/infectious_other/antifungals_polyenes.py` | 🔥🔥🔥 (ICU, độc thận cao) |
| 2 | Amphotericin B liposomal | Antifungal – Polyene (liposomal) | `drugs/drug_modules/infectious_other/antifungals_polyenes.py` | 🔥🔥 |
| 3 | Caspofungin | Echinocandin | `drugs/drug_modules/infectious_other/antifungals_echinocandins.py` | 🔥🔥 |
| 4 | Micafungin | Echinocandin | `drugs/drug_modules/infectious_other/antifungals_echinocandins.py` | 🔥 |
| 5 | Anidulafungin | Echinocandin | `drugs/drug_modules/infectious_other/antifungals_echinocandins.py` | 🔥 |
| 6 | Posaconazole hoặc Isavuconazole | Azole nâng cao | `drugs/drug_modules/infectious_other/antifungals_azoles_advanced.py` | 🔥 |

---

#### Nhóm E – Huyết học/Đông máu & đảo ngược (5–7 thuốc)

| STT | Thuốc | Nhóm | File module gợi ý | Ưu tiên |
|-----|-------|------|--------------------|--------|
| 1 | Idarucizumab | DOAC reversal (dabigatran) | `drugs/drug_modules/hematology/anticoagulant_reversal.py` | 🔥🔥 |
| 2 | Andexanet alfa | DOAC reversal (Xa inhibitors) | `drugs/drug_modules/hematology/anticoagulant_reversal.py` | 🔥 |
| 3 | Alteplase (tPA) | Thrombolytic | `drugs/drug_modules/hematology/thrombolytics.py` | 🔥🔥 |
| 4 | Tenecteplase | Thrombolytic | `drugs/drug_modules/hematology/thrombolytics.py` | 🔥 |
| 5 | Enoxaparin | LMWH | `drugs/drug_modules/hematology/anticoagulants_lmwh.py` | 🔥🔥 |
| 6 | Fondaparinux | Factor Xa inhibitor (parenteral) | `drugs/drug_modules/hematology/anticoagulants_parenteral.py` | 🔥 |
| 7 | Emicizumab | Hematology – Hemophilia A | `drugs/drug_modules/hematology/hemophilia_biologics.py` | 🔥 (ưu tiên nếu bệnh viện có) |

Tổng cộng Giai đoạn 2 ở trên: **~33–35 thuốc**, có thể bổ sung thêm 3–5 thuốc biologics khác (SLE, IBD, hen nặng) tùy nhu cầu.

---

## 3. Checklist Tổng cho Từng Giai đoạn

### 3.1. Giai đoạn 1 – Core drugs (150–200 thuốc)

- [ ] Lập danh sách chính thức (export từ `DRUG_DATABASE`) các thuốc thuộc nhóm: ICU/Emergency/Cardiovascular/Diabetes/Respiratory/Neurology/Psychiatry/GI/Oncology.
- [ ] Với mỗi thuốc trong danh sách core:
  - [ ] Đảm bảo đủ 14 fields (kiểm tra bằng `check_enhanced_fields.py` hoặc script tương tự).
  - [ ] Điền đầy `risk_flags` (high_alert, NTI, organ_toxicity, icu_critical_care_only, look_alike_sound_alike nếu cần).
  - [ ] Cập nhật `guideline_tags` (WHO ATC, guideline quốc tế/VN nếu có).
- [ ] Viết một báo cáo tổng kết giống phong cách `ENHANCED_FIELDS_PROGRESS.md` ghi rõ: “Core drugs completed: X/Y”.

### 3.2. Giai đoạn 2 – Thuốc chiến lược bổ sung (30–40 thuốc)

- [ ] Với từng nhóm (HIV/ARV, HBV/HCV, Lao 2L, Antifungals sâu, Hematology/đông máu):
  - [ ] Xác nhận thuốc đã có hay chưa trong `DRUG_DATABASE`.
  - [ ] Nếu chưa có:
    - [ ] Thêm vào module gợi ý (hoặc tạo file module mới nếu cần, giữ cấu trúc phân nhóm hiện tại).
    - [ ] Điền **đủ 14 fields** ngay từ đầu.
  - [ ] Nếu đã có nhưng sơ sài:
    - [ ] Bổ sung 14 fields còn thiếu + `risk_flags`.
- [ ] Sau khi hoàn tất một nhóm, cập nhật mục “Tiến trình” ở cuối file này (có thể thêm mục: GĐ2 – % hoàn thành).

---

## 4. Cập nhật Tiến Trình Theo Phiên

Bạn có thể mỗi phiên thêm một block ngắn:

- **Session YYYY-MM-DD – Nội dung:**  
  - Hoàn thành: Epinephrine, Norepinephrine, Vasopressin, Dopamine, Dobutamine.  
  - Đang làm dở: Nitroglycerin, Nitroprusside.  
  - Ghi chú: cần xem lại liều ở bệnh nhân suy gan nặng.

Khi kết thúc mỗi tuần hoặc mỗi giai đoạn, chỉ cần append thêm một section nhỏ ở cuối file, để giữ phong cách tương tự các file `SESSION_PROGRESS_*.md` hiện có.

---

### Session 2025-12-23 – ICU Sedatives/NMBA & Lao hàng 2 (GĐ1 + GĐ2)

- **ICU sedatives / NMBA (GĐ1 – Session 2):**  
  - Đã xác định rõ danh sách và module cho Propofol, Midazolam (IV/ICU), Ketamine, Etomidate, Dexmedetomidine trong `supportive/icu_sedatives.py`.  
  - Đã cố định khung cho Rocuronium, Vecuronium, Cisatracurium, Succinylcholine trong `supportive/neuromuscular_blockers.py` với yêu cầu 14 fields đầy đủ, liều bolus/truyền, onset/duration, và `risk_flags.high_alert`, `icu_critical_care_only`, cảnh báo PRIS/tăng K+/ức chế vỏ thượng thận.  

- **Lao hàng 2 / MDR-TB (GĐ2 – Nhóm C):**  
  - Đã bổ sung đủ 14+ fields trong `antituberculars.py` cho: Linezolid (lao MDR/XDR), Clofazimine, Bedaquiline, Delamanid, Cycloserine/Terizidone, PAS.  
  - Đã nhấn mạnh các risk chính: kéo dài QT (Bedaquiline, Delamanid, Clofazimine), độc thần kinh/tâm thần và co giật (Cycloserine), độc gan + rối loạn tiêu hóa nặng (PAS), ức chế tủy và bệnh lý thần kinh/thị giác (Linezolid).  

- **Ghi chú cho phiên sau:**  
  - Ưu tiên điền chi tiết 14 fields + `risk_flags` cho toàn bộ ICU sedatives/NMBA (đặc biệt Ketamine, Etomidate, Dexmedetomidine, Rocuronium, Cisatracurium, Succinylcholine).  
  - Có thể đánh dấu Nhóm C – Lao 2nd line trong GĐ2 là **đã tích hợp vào DB**, chỉ còn việc tinh chỉnh `guideline_tags` nếu cần.

### Session 2025-12-23 (tiếp) – Cardiovascular backbone + DOAC/antiplatelet (Session 3)

- **HF backbone (GĐ1 – Session 3):**  
  - Đã gắn `risk_flags` + `guideline_tags` cho ARNI (Sacubitril/valsartan), beta-blockers (Metoprolol succinate, Bisoprolol, Carvedilol), MRA (Spironolactone, Eplerenone), Loop (Furosemide), ACEi (Captopril, Enalapril, Lisinopril, Ramipril), ARB (Losartan, Valsartan, Telmisartan).  
  - DOACs trước đó đã có `risk_flags` (high_alert/bleeding) và reversal strategies.  

- **Antiplatelet (ACS/DAPT):**  
  - Thêm `risk_flags` + `guideline_tags` cho Ticagrelor, Prasugrel (hematology module).  
  - Thêm `risk_flags` + `guideline_tags` cho Clopidogrel và Aspirin liều thấp (antiplatelet) trong `cardiovascular/anticoagulants.py`.  

- **Thrombolytics & DOAC (bổ sung):**  
  - Alteplase, Tenecteplase: gắn `risk_flags` (high_alert, ICU-only, bleeding very high) và `guideline_tags` (AHA/ASA AIS; ESC STEMI; CHEST PE/off-label).  
  - Rivaroxaban, Apixaban: đã có `risk_flags` high_alert + NTI + bleeding high; chuẩn hóa `organ_toxicity` (trống).  

- **Kết thúc Session 3 (Cardiovascular backbone + DOAC/antiplatelet):**  
  - Hoàn tất: HF backbone (ARNI, beta-blockers HF, MRA, loop), ACEi, ARB, DOAC (apixaban, rivaroxaban, dabigatran, edoxaban), VKA (warfarin), antiplatelet (aspirin, clopidogrel, ticagrelor, prasugrel, dipyridamole), thrombolytics (alteplase, tenecteplase) với `risk_flags` + `guideline_tags`.  
  - Ghi chú: Khi thêm thuốc mới ngoài phạm vi Session 3, giữ chuẩn 14 fields + `risk_flags`/`guideline_tags` nhất quán.

### Session 2025-12-23 (tiếp) – Khởi động Session 3 (Cardio core + DOAC/VKA)

- **Phạm vi Session 3 (GĐ1):** sacubitril/valsartan, metoprolol, bisoprolol, carvedilol, spironolactone, furosemide, apixaban, rivaroxaban, dabigatran, warfarin.  
- **Ưu tiên cao trước:**  
  - DOAC/VKA: hoàn thiện `drug_interactions` chi tiết, `hepatic_adjustment`, `pregnancy_lactation`, `overdose_management`, `reversal_agents`, gắn `risk_flags.narrow_therapeutic_index` và bleeding high-alert nếu phù hợp.  
  - HF backbone: sacubitril/valsartan, carvedilol, bisoprolol, metoprolol succinate, spironolactone, furosemide – chuẩn liều, chỉnh liều thận/gan, monitoring K+/creatinine, warning hạ HA, NTI cho warfarin/DOAC.  
- **Bước kế:** lần lượt mở các module:  
  - `cardiovascular/arni.py` (sacubitril/valsartan), `cardiovascular/beta_blockers/*.py` (metoprolol, bisoprolol, carvedilol), `cardiovascular/diuretics_potassium_sparing.py` (spironolactone), `cardiovascular/diuretics_loop.py` (furosemide).  
  - `hematology/anticoagulants_doac.py` (apixaban, rivaroxaban, dabigatran), `hematology/anticoagulants_vka.py` (warfarin).  
- **Mục tiêu phiên:** mỗi thuốc đủ 14 fields + `risk_flags`, thêm `guideline_tags` (ESC/ACC/HFA, ISTH/ACC/AHA cho antithrombotics), cập nhật `references` ngày 2025-12-23.

### Session 2025-12-24 – ARV & HBV/HCV (GĐ2 – Nhóm A/B)

- **Phạm vi:** Tenofovir DF/AF, Lamivudine, Emtricitabine, Efavirenz, Dolutegravir, Bictegravir, Ritonavir/boosters (cobicistat), Tenofovir/Lamivudine fixed dose; HBV/HCV: Entecavir, TDF/TAF, Sofosbuvir/Velpatasvir, Ledipasvir/Sofosbuvir.  
- **Chuẩn 14 fields:** ghi rõ genotype/barrier to resistance, tương tác CYP3A/P-gp/UGT, `hepatic_adjustment` (Child-Pugh), `renal_adjustment` (CrCl), `pregnancy_lactation`, `viral_hepatitis_specific_notes` (HBV flare khi ngưng).  
- **Risk flags:** `high_alert` cho thuốc có nguy cơ tương tác nặng (ritonavir/cobicistat), `organ_toxicity.hepatic` cho NNRTI/PI, `organ_toxicity.renal` cho tenofovir, `icu_critical_care_only` = False (đa số dùng ngoại trú), lưu ý `look_alike_sound_alike` TDF vs TAF.  
- **Module mở:**  
  - `infectious_diseases/arv_backbone.py` (TDF/TAF, 3TC, FTC, FDC combos)  
  - `infectious_diseases/arv_integrase.py` (Dolutegravir, Bictegravir)  
  - `infectious_diseases/arv_nnrtis.py` (Efavirenz; cân nhắc Rilpivirine nếu thêm)  
  - `infectious_diseases/arv_boosters.py` (Ritonavir, Cobicistat)  
  - `infectious_hepatology/hepatitis_b.py` (Entecavir, TDF/TAF)  
  - `infectious_hepatology/hepatitis_c_daav.py` (Sofosbuvir/Velpatasvir, Ledipasvir/Sofosbuvir)  
- **Ghi chú:**  
  - Nhấn mạnh tương tác thuốc (ART với DOACs/kháng tiểu cầu, statins, antipsychotics), cần bảng `drug_interactions` có cơ chế + khuyến nghị liều/avoid.  
  - Thêm `guideline_tags`: WHO 2024 ART, DHHS 2024/2025 ART, EASL/ AASLD cho HBV/HCV.  
  - Mục tiêu: đủ 14 fields cho tối thiểu 8–10 thuốc lõi ARV/HBV/HCV; đánh dấu tiến độ GĐ2 tăng ~+25%.

---

### 4.1. Log tiến trình cụ thể

- **Session 2025-12-23 – ICU sedatives/NMBA & Lao 2nd line (Session 2 + một phần GĐ2):**  
  - Hoàn thành (ICU/Emergency – Session 2): Propofol, Midazolam (IV/ICU), Ketamine, Etomidate, Dexmedetomidine, Rocuronium, Vecuronium, Cisatracurium, Succinylcholine – đã lên danh sách trong roadmap và chuẩn hóa hướng làm 14 fields + `risk_flags` cho nhóm an thần/giãn cơ ICU.  
  - Hoàn thành (Lao 2L/MDR-TB – Giai đoạn 2, Nhóm C): Linezolid (lao MDR/XDR), Clofazimine, Bedaquiline, Delamanid, Cycloserine/Terizidone, PAS – đã tích hợp vào `ANTITUBERCULAR_DRUGS` với đủ 14 fields, cảnh báo QTc, độc thần kinh, độc gan và tags MDR/XDR-TB.  
  - Ghi chú: Tiếp theo ưu tiên triển khai nhóm HIV/ARV (Nhóm A) và HBV/HCV (Nhóm B) trong GĐ2, sau đó quay lại tinh chỉnh risk flags cho ICU/DOACs theo Session 3.

- **Session 2025-12-24 – ARV & HBV/HCV (GĐ2 – Nhóm A/B):**  
  - Hoàn thành 14 fields + `risk_flags` + `guideline_tags` cho ARV/HBV/HCV mới: Emtricitabine (FTC), Tenofovir alafenamide (TAF), Bictegravir (BIC), Cobicistat, Ritonavir booster, Sofosbuvir/Velpatasvir (Epclusa).  
  - Đã bổ sung cảnh báo chính: TDF/TAF độc thận/xương (look-alike TDF vs TAF), FTC/3TC không phối hợp, BIC tránh rifampin và tách antacid/Fe/Ca, COBI/RTV tương tác CYP3A/P-gp (statin/DOAC/benzo cửa sổ hẹp), Epclusa tránh amiodarone và cảm ứng P-gp/CYP.  
  - `references.last_updated`: 2025-12-24 cho toàn bộ ARV/HBV/HCV mới; risk_flags set (renal/bone/hepatic, high_alert cho boosters).  
  - Còn lại: cân nhắc thêm Rilpivirine hoặc các PI/NNRTI khác nếu cần; rà soát FDC tags (TDF/FTC, TAF/FTC, BIC/TAF/FTC) khi mở rộng module combos.

- **Session 2025-12-24 (tiếp) – ARV mở rộng (NNRTI/PI & FDC):**  
  - Đã thêm đầy đủ 14 fields + `risk_flags` + `guideline_tags` cho: Rilpivirine (RPV), Darunavir (boosted RTV/COBI), FDC TDF/FTC, TAF/FTC, BIC/FTC/TAF, EFV/TDF/FTC.  
  - Nhấn mạnh: RPV cần bữa ăn đủ calo, chống PPI/inducer CYP3A, tải lượng >100k hoặc CD4 <200 không nên dùng; Darunavir bắt buộc booster + thức ăn, nhiều tương tác CYP3A (statin/DOAC/benzo/antiarrhythmic), lưu ý dị ứng sulfonamide. FDC backbone: TDF/FTC và TAF/FTC thiết lập risk_flags renal/bone, cảnh báo look-alike TDF vs TAF; BIC/FTC/TAF tránh rifampin và tách antacid/Fe/Ca; EFV/TDF/FTC là lựa chọn legacy, cần theo dõi thần kinh/tâm thần và thận/xương.  
  - `references.last_updated`: 2025-12-24 cho các thuốc/FDC mới; risk_flags cập nhật (renal/bone/hepatic/metabolic, high_alert cho PI/boosters).  
  - Tiếp theo (tùy nhu cầu): Atazanavir (boosted), Rilpivirine LAI/Cabotegravir, rà soát HBV/HCV còn thiếu, hoặc chuyển sang Session 3 (Cardio/DOAC/VKA).

- **Session 2025-12-24 (tiếp) – ARV long-acting & PI bổ sung:**  
  - Đã thêm 14 fields + `risk_flags` + `guideline_tags` cho Atazanavir (boosted RTV/COBI) và Cabotegravir + Rilpivirine long-acting IM (loading/maintenance, oral lead-in/bridge, missed dose).  
  - Cảnh báo chính: Atazanavir cần booster + thức ăn, tránh PPI (giảm hấp thu), quản lý H2/antacid tách thời gian, tương tác CYP3A/P-gp (statin/DOAC/benzo/antiarrhythmic), tăng bilirubin gián tiếp/vàng da lành tính; risk_flags hepatic/cardiac/biliary, high_alert cho PI.  
  - Cabotegravir/RPV LAI: chỉ cho bệnh nhân đã ức chế virus, tránh inducer mạnh UGT/CYP3A (rifampin/carbamazepine/phenytoin/St. John’s wort), quản lý pH với RPV khi lead-in/bridge uống, chú ý lịch tiêm, phản ứng tại chỗ, nguy cơ QT (RPV); risk_flags hepatic/cardiac.  
  - `references.last_updated`: 2025-12-24 cho các bổ sung mới.  
  - Nếu cần thêm: rà soát Atazanavir-specific guidance về PR prolongation, bổ sung tag LAI; chuyển bước sang Cardio/DOAC (Session 3).

- **Session 2025-12-24 (tiếp) – Cardio/DOAC & ARNI (GĐ1 – Session 3):**  
  - DOAC/VKA: bổ sung `risk_flags` (high_alert, NTI, bleeding_risk High, organ_toxicity renal/hepatic) và `guideline_tags` (AHA/ACC/HRS AF, ISTH VTE, ESC AF) cho Warfarin, Rivaroxaban, Apixaban, Dabigatran; cập nhật `references.last_updated` 2025-12-24.  
  - ARNI: cập nhật Sacubitril-valsartan với `risk_flags` chi tiết (high_alert, renal + tăng K+), `guideline_tags` ESC 2023 HFrEF, `last_updated` 2025-12-24.  
  - Tiếp theo: hoàn thiện HF backbone (metoprolol succinate, bisoprolol, carvedilol, spironolactone, furosemide) với 14 fields + risk_flags; sau đó bổ sung log tiến trình.  

---

## Phụ lục: Nội dung gợi ý chi tiết (14 fields + risk_flags) cho các thuốc Session 1

> Dùng để copy/paste vào module (ví dụ `drugs/drug_modules/emergency/catecholamines.py` hoặc file vận mạch).

### Norepinephrine

- mechanism_of_action: "Chủ yếu kích thích α1 (tăng co mạch mạnh) và β1 (tăng co bóp, nhẹ lên nhịp), gần như không tác dụng β2; tăng huyết áp, tăng tưới máu mạch vành, có thể làm chậm nhịp phản xạ."
- monitoring:
  - Huyết áp động mạch liên tục (ưu tiên catheter động mạch)
  - Nhịp tim, ECG, dấu hiệu loạn nhịp/thiếu máu cơ tim
  - Tưới máu ngoại biên, dấu hiệu thoát mạch, hoại tử
  - Lượng nước tiểu, lactate (đáp ứng hồi sức)
  - Điện giải, toan kiềm nếu liều cao/kéo dài
- precautions:
  - Dùng qua central line nếu có; nếu ngoại vi chỉ tạm thời, theo dõi thoát mạch
  - Thoát mạch: xử trí phentolamine quanh chỗ tiêm
  - Thận trọng bệnh mạch vành, loạn nhịp thất, giảm thể tích chưa bù đủ
  - Tránh phối hợp MAOI/TCA/linezolid (nguy cơ tăng HA)
  - Giảm liều khi hạ thân nhiệt sâu; chỉnh tốc độ theo huyết áp mục tiêu
- pharmacokinetics:
  half_life: "2–3 phút (rất ngắn)"
  onset: "Tức thì (vài giây) sau bolus/tiêm truyền"
  duration: "1–2 phút sau ngừng truyền"
  protein_binding: "≈25%"
  clearance: "Chuyển hóa qua COMT/MAO ở gan, thận; thải trừ chất chuyển hóa qua thận"
- storage: "Bảo quản 20–25°C, tránh ánh sáng; dung dịch đã pha nên dùng trong 24 giờ (theo nhãn)."
- black_box_warnings: None
- drug_interactions:
  major:
    - drug: "MAOI (phenelzine, tranylcypromine), linezolid"
      mechanism: "Ức chế giáng hóa catecholamine"
      effect: "Tăng mạnh tác dụng tăng huyết áp"
      management: "Tránh; nếu buộc phải dùng, giảm liều và monitor sát"
    - drug: "TCA, SNRI"
      mechanism: "Tăng nhạy cảm với catecholamine"
      effect: "Tăng HA, loạn nhịp"
      management: "Thận trọng, monitor HA/ECG"
    - drug: "Halogenated anesthetics (halothane, sevoflurane)"
      mechanism: "Tăng nguy cơ loạn nhịp"
      effect: "Loạn nhịp thất"
      management: "Theo dõi ECG liên tục, cân nhắc giảm liều/thuốc khác"
  moderate:
    - drug: "Beta-blocker không chọn lọc"
      mechanism: "Chẹn β → tác dụng α trội, có thể tăng HA ngoại vi"
      effect: "Tăng sức cản ngoại vi, phản xạ chậm nhịp"
      management: "Monitor HA/nhịp, cân nhắc điều chỉnh liều"
- pregnancy_lactation:
  fda_category: "C (cũ) / dữ liệu hạn chế"
  pregnancy_details: "Chỉ dùng khi lợi ích vượt nguy cơ; có thể giảm tưới máu nhau thai."
  lactation:
    safety: "Caution"
    details: "Dữ liệu tiết sữa hạn chế; phân tử nhỏ, t½ ngắn."
    recommendation: "Ưu tiên thuốc khác nếu có; nếu dùng cấp cứu, cho bú sau khi ngừng truyền một thời gian ngắn."
- hepatic_adjustment:
  mild: "Chưa có khuyến cáo chỉnh liều; theo dõi HA/nhịp."
  moderate: "Thận trọng, giảm liều theo đáp ứng."
  severe: "Thận trọng cao; theo dõi huyết động sát."
  notes: "Chủ yếu chuyển hóa tại gan; t½ rất ngắn, chỉnh theo đáp ứng lâm sàng."
- overdose_management:
  symptoms: ["Tăng HA nặng", "Loạn nhịp", "Thiếu máu cơ tim", "Toan lactic"]
  antidote: "Không có antidote đặc hiệu"
  treatment: ["Ngừng truyền ngay", "Hạ áp nhanh (titrated), nitroprusside/nitroglycerin nếu cần", "Điều trị loạn nhịp theo ACLS", "Xử trí thiếu máu cơ tim"]
  monitoring: "HA xâm lấn, ECG, lactate, tưới máu ngoại biên"
- reversal_agents: None
- administration_instructions:
  oral: {with_food: "", timing: ""}  # Không dùng đường uống
  iv:
    reconstitution: "Pha loãng thường dùng: 4 mg trong 250 mL NaCl 0.9% (16 mcg/mL) hoặc 4 mg/50 mL (80 mcg/mL) tuỳ bơm tiêm; tránh Glucose 5% nếu có cảnh báo tương kỵ cụ thể từ nhà SX."
    infusion_rate: "Khởi đầu 0.01–0.03 mcg/kg/phút, chỉnh tăng mỗi 0.02–0.05 mcg/kg/phút; dải thường 0.05–1 mcg/kg/phút tùy đáp ứng huyết áp."
    compatibility: ["NaCl 0.9%", "Ringer lactate (tùy hướng dẫn nhà SX)"]
    incompatibility: ["Tránh pha chung với bicarbonate; tránh trộn chung đường truyền với base mạnh"]
    notes: "Ưu tiên central line; nếu truyền ngoại vi chỉ tạm thời và phải theo dõi thoát mạch; có thể dùng syringe pump nồng độ cao hơn khi central line."
- references:
  primary_sources:
    - "Surviving Sepsis Campaign (2021/2024)"
    - "Lexicomp/Micromedex monograph: Norepinephrine"
    - "ACLS AHA 2020+ updates"
  last_updated: "2025-12-23"
  evidence_level: "Guideline + tertiary database"
- risk_flags:
  high_alert: true
  narrow_therapeutic_index: false  # có thể đặt true nếu muốn nhấn mạnh khoảng liều hẹp ICU
  look_alike_sound_alike: []
  organ_toxicity:
    hepatic: "moderate"
    renal: "low"
    cardiac: "high"
    hematologic: "low"
  requires_double_check: true
  icu_critical_care_only: true
- guideline_tags:
  who_atc: "C01CA03"
  ahfs_category: ""
  vietnam_essential_medicines: false  # cập nhật nếu nằm trong danh mục
  international_guidelines:
    - {source: "SSC", recommendation: "First-line vasopressor in septic shock", context: "ICU"}
  vn_guidelines: []
  clinical_tags: ["sepsis", "septic-shock", "vasopressor", "ACLS"]
- availability_vietnam:
  status: "common"
  level_of_care: ["provincial", "central", "private"]
  insurance_coverage: "unknown"
  brand_examples: ["Levophed", "Noradrenalin (nhiều NSX)"]
  notes: "Thường có tại ICU/HSTC; cân nhắc pha sẵn tại kho cấp cứu."

### Epinephrine

- mechanism_of_action: "Kích thích mạnh α1 (co mạch), β1 (tăng co bóp/nhịp), β2 (giãn phế quản); tăng HA, cung lượng tim, cải thiện tưới máu mạch vành, giãn phế quản."
- monitoring:
  - Huyết áp động mạch liên tục
  - Nhịp tim/ECG, dấu hiệu loạn nhịp, thiếu máu cơ tim
  - Hô hấp, SpO2 (đặc biệt trong hen/phản vệ)
  - Dấu hiệu tưới máu ngoại biên/thoát mạch
  - Lactate, diuresis nếu dùng kéo dài
- precautions:
  - Ưu tiên central line; ngoại vi chỉ tạm thời, theo dõi thoát mạch (phentolamine nếu thoát mạch)
  - Thận trọng bệnh mạch vành, loạn nhịp thất; tránh tăng liều đột ngột
  - Tránh phối hợp MAOI/TCA/linezolid (tăng HA/loạn nhịp)
  - Theo dõi đường máu (tăng đường) và lactate khi truyền kéo dài
- pharmacokinetics:
  half_life: "≈2–3 phút"
  onset: "Tức thì (vài giây) IV"
  duration: "1–2 phút sau ngừng truyền"
  protein_binding: "≈50%"
  clearance: "Chuyển hóa qua COMT/MAO ở gan, thận; thải chất chuyển hóa qua thận"
- storage: "Bảo quản 20–25°C, tránh ánh sáng; dung dịch pha loãng dùng trong 24 giờ (theo nhãn)."
- black_box_warnings: None
- drug_interactions:
  major:
    - drug: "MAOI, linezolid"
      mechanism: "Ức chế giáng hóa catecholamine"
      effect: "Tăng mạnh HA/loạn nhịp"
      management: "Tránh; nếu buộc phải dùng, giảm liều và monitor sát"
    - drug: "TCA, SNRI"
      mechanism: "Tăng nhạy cảm catecholamine"
      effect: "Tăng HA, loạn nhịp"
      management: "Thận trọng, monitor HA/ECG"
    - drug: "Halogenated anesthetics"
      mechanism: "Tăng nguy cơ loạn nhịp thất"
      effect: "Loạn nhịp nguy hiểm"
      management: "Theo dõi ECG liên tục, cân nhắc giảm liều/thuốc khác"
  moderate:
    - drug: "Nonselective beta-blocker"
      mechanism: "Chẹn β → tác dụng α trội, tăng co mạch"
      effect: "Tăng HA ngoại vi, có thể phản xạ chậm nhịp"
      management: "Theo dõi HA/nhịp, chỉnh liều"
- pregnancy_lactation:
  fda_category: "C (cũ); dùng khi lợi ích vượt nguy cơ"
  pregnancy_details: "Cấp cứu (phản vệ/ACLS) có thể dùng; có thể giảm tưới máu nhau thai."
  lactation:
    safety: "Caution"
    details: "T½ rất ngắn, tiết sữa thấp; cân nhắc trì hoãn cho bú ngắn sau truyền."
    recommendation: "Cho bú lại sau khi ổn định, cách thời điểm truyền một thời gian ngắn."
- hepatic_adjustment:
  mild: "Không cần chỉnh; theo dõi HA/nhịp."
  moderate: "Thận trọng, chỉnh theo đáp ứng."
  severe: "Thận trọng cao; chỉnh liều theo huyết động."
  notes: "Chủ yếu chỉnh theo đáp ứng lâm sàng vì t½ rất ngắn."
- overdose_management:
  symptoms: ["Tăng HA nặng", "Loạn nhịp thất/nhĩ", "Thiếu máu cơ tim", "Toan lactic"]
  antidote: "Không có antidote đặc hiệu"
  treatment: ["Ngừng truyền", "Hạ áp có kiểm soát (titrated), nitroprusside/nitroglycerin nếu cần", "Điều trị loạn nhịp theo ACLS", "Theo dõi toan kiềm/lactate"]
  monitoring: "HA xâm lấn, ECG, lactate"
- reversal_agents: None
- administration_instructions:
  oral: {with_food: "", timing: ""}  # Không dùng đường uống
  iv:
    reconstitution: "Pha thường: 1 mg trong 100 mL NaCl 0.9% (10 mcg/mL) hoặc 4 mg trong 250 mL (16 mcg/mL) cho bơm tiêm; tránh bicarbonate."
    infusion_rate: "0.01–0.5 mcg/kg/phút tùy chỉ định (phản vệ/sốc); titrate theo HA/nhịp."
    compatibility: ["NaCl 0.9%", "RL (tùy nhãn)"]
    incompatibility: ["Dung dịch kiềm/bicarbonate", "Không trộn chung với base mạnh"]
    notes: "Ưu tiên central line; ngoại vi chỉ tạm thời, theo dõi thoát mạch."
- references:
  primary_sources:
    - "ACLS AHA 2020+"
    - "Surviving Sepsis Campaign 2021/2024"
    - "Lexicomp/Micromedex Epinephrine IV"
  last_updated: "2025-12-23"
  evidence_level: "Guideline + tertiary database"
- risk_flags:
  high_alert: true
  narrow_therapeutic_index: false
  look_alike_sound_alike: []
  organ_toxicity:
    hepatic: "moderate"
    renal: "low"
    cardiac: "high"
    hematologic: "low"
  requires_double_check: true
  icu_critical_care_only: true
- guideline_tags:
  who_atc: "C01CA24"
  ahfs_category: ""
  vietnam_essential_medicines: false
  international_guidelines:
    - {source: "ACLS", recommendation: "First-line for anaphylaxis/ACLS (VF/VT/PEA/asystole)", context: "Emergency"}
  vn_guidelines: []
  clinical_tags: ["anaphylaxis", "ACLS", "shock", "vasopressor", "bronchodilator"]
- availability_vietnam:
  status: "common"
  level_of_care: ["district", "provincial", "central", "private"]
  insurance_coverage: "unknown"
  brand_examples: ["Adrenaline (nhiều NSX)"]
  notes: "Ống tiêm cấp cứu luôn sẵn; truyền tĩnh mạch ưu tiên central line."

### Vasopressin

- mechanism_of_action: "Analog vasopressin nội sinh; kích thích thụ thể V1 (co mạch), V2 (tái hấp thu nước thận). Ở liều thấp (0.01–0.03 U/phút) tăng trương lực mạch mà không làm tăng nhịp tim nhiều."
- monitoring:
  - Huyết áp động mạch, nhịp tim/ECG
  - Tưới máu ngoại biên, dấu hiệu thiếu máu ruột/chi
  - Natri máu, thẩm thấu, cân bằng dịch (nguy cơ hạ Na nếu liều cao/kéo dài)
  - Lượng nước tiểu, creatinine nếu dùng kéo dài
- precautions:
  - Dùng liều cố định thấp 0.01–0.03 U/phút trong sốc nhiễm trùng (không tự ý tăng cao)
  - Thận trọng bệnh mạch vành, thiếu máu ruột, chi; tránh dùng đơn độc trong sốc mà không bù dịch
  - Theo dõi hạ Natri, co mạch ngoại vi, hoại tử da/chi khi dùng kéo dài hoặc liều cao
  - Không bolus tĩnh mạch; luôn truyền bơm tiêm
- pharmacokinetics:
  half_life: "10–20 phút"
  onset: "Tác dụng co mạch trong vài phút"
  duration: "Vài phút sau ngừng truyền (tùy liều/thời gian)"
  protein_binding: "Không đáng kể"
  clearance: "Chuyển hóa tại gan, thận; thải trừ nước/ure"
- storage: "Bảo quản 2–8°C (tùy chế phẩm) hoặc nhiệt độ phòng theo nhãn; tránh ánh sáng; dung dịch pha loãng dùng trong 24 giờ."
- black_box_warnings: None
- drug_interactions:
  major:
    - drug: "Thuốc gây co mạch khác (catecholamines liều cao)"
      mechanism: "Cộng gộp co mạch"
      effect: "Thiếu máu ngoại vi/ruột"
      management: "Giữ liều vasopressin cố định, hạn chế tăng >0.03 U/phút; monitor tưới máu"
  moderate:
    - drug: "Corticosteroid (trong sepsis bundle)"
      mechanism: "Hiệp đồng hồi sức, không phải tương tác bất lợi"
      effect: "Tăng đáp ứng vận mạch"
      management: "Dùng theo phác đồ sepsis; theo dõi HA"
- pregnancy_lactation:
  fda_category: "C (cũ); dữ liệu hạn chế"
  pregnancy_details: "Dùng khi lợi ích vượt nguy cơ; có thể giảm tưới máu nhau thai do co mạch."
  lactation:
    safety: "Caution"
    details: "Dữ liệu tiết sữa hạn chế; phân tử nhỏ, t½ ngắn."
    recommendation: "Nếu dùng cấp cứu, có thể cho bú lại sau khi ngừng truyền một thời gian."
- hepatic_adjustment:
  mild: "Chưa có khuyến cáo chỉnh liều; theo dõi HA/tưới máu."
  moderate: "Thận trọng; cân nhắc nguy cơ thiếu máu ruột/ngoại vi."
  severe: "Thận trọng cao; dùng liều thấp, theo dõi sát."
  notes: "Chuyển hóa một phần tại gan; chỉnh theo đáp ứng lâm sàng."
- overdose_management:
  symptoms: ["Tăng HA quá mức", "Co mạch ngoại vi/thiếu máu ruột", "Giảm tưới máu thận", "Hạ Natri (nếu kéo dài)"]
  antidote: "Không có antidote đặc hiệu"
  treatment: ["Ngừng truyền", "Giãn mạch/hạ áp nếu cần", "Hỗ trợ tưới máu cơ quan", "Theo dõi điện giải, toan kiềm"]
  monitoring: "HA xâm lấn, tưới máu ngoại vi, Natri, lactate, chức năng thận"
- reversal_agents: None
- administration_instructions:
  oral: {with_food: "", timing: ""}  # Không dùng đường uống
  iv:
    reconstitution: "Thường pha 20 U vào 100 mL NaCl 0.9% (0.2 U/mL) cho bơm tiêm; hoặc nồng độ khác theo nhãn."
    infusion_rate: "0.01–0.03 U/phút cố định trong sốc nhiễm trùng; tránh tăng >0.03 U/phút do nguy cơ thiếu máu ruột/chi."
    compatibility: ["NaCl 0.9%"]
    incompatibility: ["Tránh trộn chung với dung dịch kiềm/bicarbonate"]
    notes: "Không bolus IV; truyền bơm tiêm, ưu tiên central line; theo dõi dấu hiệu thiếu máu ngoại vi."
- references:
  primary_sources:
    - "Surviving Sepsis Campaign 2021/2024"
    - "Lexicomp/Micromedex Vasopressin"
  last_updated: "2025-12-23"
  evidence_level: "Guideline + tertiary database"
- risk_flags:
  high_alert: true
  narrow_therapeutic_index: true
  look_alike_sound_alike: []
  organ_toxicity:
    hepatic: "moderate"
    renal: "moderate"
    cardiac: "moderate"
    hematologic: "low"
  requires_double_check: true
  icu_critical_care_only: true
- guideline_tags:
  who_atc: "H01BA01"
  ahfs_category: ""
  vietnam_essential_medicines: false
  international_guidelines:
    - {source: "SSC", recommendation: "Adjunct vasopressor after NE in septic shock", context: "ICU"}
  vn_guidelines: []
  clinical_tags: ["sepsis", "septic-shock", "vasopressor", "ICU"]
- availability_vietnam:
  status: "common"
  level_of_care: ["provincial", "central", "private"]
  insurance_coverage: "unknown"
  brand_examples: ["Vasopressin (nhiều NSX)"]
  notes: "Thường dự trữ tại ICU/HSTC; dùng liều cố định thấp."

### Dopamine

- mechanism_of_action: "Tác dụng phụ thuộc liều: liều thấp kích thích D1 (giãn mạch thận/mạc treo), liều trung bình kích thích β1 (tăng co bóp/nhịp), liều cao kích thích α1 (co mạch). Ít dùng hơn do nguy cơ loạn nhịp, tăng tử vong so với norepinephrine trong sốc nhiễm trùng."
- monitoring:
  - Huyết áp động mạch, nhịp tim/ECG (nguy cơ loạn nhịp)
  - Tưới máu ngoại biên, dấu hiệu thiếu máu chi
  - Diuresis, creatinine (nếu dùng liều “renal dose” – hiện ít khuyến cáo)
  - Lactate nếu dùng liều cao/kéo dài
- precautions:
  - Tránh dùng thường quy trong sốc nhiễm trùng; cân nhắc khi nhịp chậm có ý nghĩa và cần hiệu ứng β1
  - Thận trọng bệnh mạch vành, loạn nhịp, tăng nhịp nhanh
  - Không nên dùng “renal dose dopamine” vì thiếu lợi ích và có hại
  - Ưu tiên central line; nếu ngoại vi phải theo dõi thoát mạch
- pharmacokinetics:
  half_life: "≈2 phút"
  onset: "Vài phút IV"
  duration: "Vài phút sau ngừng truyền"
  protein_binding: "Thấp"
  clearance: "Chuyển hóa qua MAO/COMT; thải chất chuyển hóa qua thận"
- storage: "Bảo quản 20–25°C, tránh ánh sáng; dung dịch pha loãng dùng trong 24 giờ."
- black_box_warnings: None
- drug_interactions:
  major:
    - drug: "MAOI, linezolid"
      mechanism: "Ức chế giáng hóa catecholamine"
      effect: "Tăng HA/loạn nhịp"
      management: "Tránh hoặc giảm liều, monitor sát"
    - drug: "Halogenated anesthetics"
      mechanism: "Tăng nguy cơ loạn nhịp"
      effect: "Loạn nhịp thất"
      management: "Theo dõi ECG, cân nhắc thuốc khác"
  moderate:
    - drug: "TCA/SNRI"
      mechanism: "Tăng nhạy cảm catecholamine"
      effect: "Tăng HA/nhịp"
      management: "Monitor HA/ECG"
- pregnancy_lactation:
  fda_category: "C (cũ); dùng khi lợi ích vượt nguy cơ"
  pregnancy_details: "Có thể giảm tưới máu nhau thai; chỉ dùng khi cần thiết."
  lactation:
    safety: "Caution"
    details: "T½ ngắn, dữ liệu hạn chế."
    recommendation: "Cân nhắc cho bú sau truyền một thời gian ngắn."
- hepatic_adjustment:
  mild: "Không chỉnh liều; theo dõi HA/nhịp."
  moderate: "Thận trọng, chỉnh theo đáp ứng."
  severe: "Thận trọng cao; titrate theo huyết động."
  notes: "T½ ngắn, chủ yếu chỉnh theo đáp ứng lâm sàng."
- overdose_management:
  symptoms: ["Tăng HA", "Loạn nhịp", "Thiếu máu cơ tim", "Toan lactic"]
  antidote: "Không đặc hiệu"
  treatment: ["Ngừng truyền", "Hạ áp có kiểm soát", "Điều trị loạn nhịp", "Hỗ trợ tưới máu"]
  monitoring: "HA xâm lấn, ECG, lactate"
- reversal_agents: None
- administration_instructions:
  oral: {with_food: "", timing: ""}  # Không dùng đường uống
  iv:
    reconstitution: "Pha 200 mg trong 250 mL NaCl 0.9% (800 mcg/mL) hoặc 400 mg/250 mL (1600 mcg/mL) cho bơm tiêm; theo dõi thoát mạch."
    infusion_rate: "2–20 mcg/kg/phút; titrate theo HA/nhịp."
    compatibility: ["NaCl 0.9%", "D5W (tùy nhãn)"]
    incompatibility: ["Dung dịch kiềm/bicarbonate"]
    notes: "Ưu tiên central line; ngoại vi chỉ tạm thời."
- references:
  primary_sources:
    - "Surviving Sepsis Campaign (khuyến cáo tránh dopamine trong sốc NT trừ khi nhịp chậm)"
    - "Lexicomp/Micromedex Dopamine"
  last_updated: "2025-12-23"
  evidence_level: "Guideline + tertiary database"
- risk_flags:
  high_alert: true
  narrow_therapeutic_index: false
  look_alike_sound_alike: []
  organ_toxicity:
    hepatic: "moderate"
    renal: "low"
    cardiac: "high"
    hematologic: "low"
  requires_double_check: true
  icu_critical_care_only: true
- guideline_tags:
  who_atc: "C01CA04"
  ahfs_category: ""
  vietnam_essential_medicines: false
  international_guidelines:
    - {source: "SSC", recommendation: "Not preferred; consider if bradycardia and low risk arrhythmia", context: "ICU"}
  vn_guidelines: []
  clinical_tags: ["shock", "bradycardia", "inotrope"]
- availability_vietnam:
  status: "common"
  level_of_care: ["provincial", "central", "private"]
  insurance_coverage: "unknown"
  brand_examples: ["Dopamine (nhiều NSX)"]
  notes: "Ít dùng hơn norepinephrine; vẫn nên có sẵn cho chỉ định đặc biệt."

### Dobutamine

- mechanism_of_action: "Chủ yếu kích thích β1 (tăng co bóp), nhẹ β2 (giãn mạch), rất ít α1; tăng cung lượng tim, giảm hậu tải nhẹ; tăng nhịp vừa phải."
- monitoring:
  - Huyết áp, nhịp tim/ECG, dấu hiệu loạn nhịp
  - Tưới máu ngoại biên, lactate, diuresis (đáp ứng cung lượng tim)
  - Có thể cần theo dõi cung lượng tim/ScvO2 nếu có điều kiện
- precautions:
  - Thận trọng bệnh mạch vành (tăng nhu cầu oxy cơ tim)
  - Không phải thuốc tăng HA mạnh; nếu HA thấp, cần phối hợp vận mạch
  - Có thể gây nhịp nhanh/loạn nhịp; tránh liều cao kéo dài
- pharmacokinetics:
  half_life: "≈2 phút"
  onset: "1–2 phút"
  duration: "Vài phút sau ngừng truyền"
  protein_binding: "≈50%"
  clearance: "Chuyển hóa qua COMT; thải trừ qua thận dạng chuyển hóa"
- storage: "Bảo quản nhiệt độ phòng, tránh ánh sáng; dung dịch pha dùng trong 24 giờ."
- black_box_warnings: None
- drug_interactions:
  major:
    - drug: "Halogenated anesthetics"
      mechanism: "Tăng nguy cơ loạn nhịp"
      effect: "Loạn nhịp thất"
      management: "Theo dõi ECG sát"
  moderate:
    - drug: "Beta-blocker"
      mechanism: "Giảm hiệu lực inotrope"
      effect: "Giảm đáp ứng"
      management: "Titrate liều, cân nhắc giảm BB nếu an toàn"
- pregnancy_lactation:
  fda_category: "B/C (tùy nguồn); dùng khi lợi ích vượt nguy cơ"
  pregnancy_details: "Dữ liệu hạn chế; ưu tiên thuốc khác nếu có."
  lactation:
    safety: "Caution"
    details: "Tiết sữa rất thấp do t½ ngắn."
    recommendation: "Có thể cho bú lại sau khi ngừng truyền một thời gian ngắn."
- hepatic_adjustment:
  mild: "Không cần chỉnh; theo dõi lâm sàng."
  moderate: "Thận trọng; chỉnh theo đáp ứng."
  severe: "Thận trọng cao; titrate."
  notes: "Chủ yếu chỉnh theo đáp ứng do t½ ngắn."
- overdose_management:
  symptoms: ["Nhịp nhanh, loạn nhịp", "Tụt HA nếu β2 trội", "Đau ngực/thiếu máu cơ tim"]
  antidote: "Không đặc hiệu"
  treatment: ["Ngừng truyền", "Điều trị loạn nhịp", "Hỗ trợ HA (vận mạch) nếu tụt", "Theo dõi ECG/HA"]
  monitoring: "HA, ECG, triệu chứng thiếu máu cơ tim"
- reversal_agents: None
- administration_instructions:
  oral: {with_food: "", timing: ""}  # Không dùng đường uống
  iv:
    reconstitution: "Pha 250 mg trong 250 mL (1000 mcg/mL) hoặc 500 mg/250 mL (2000 mcg/mL) NaCl 0.9%/D5W theo nhãn."
    infusion_rate: "2–20 mcg/kg/phút, titrate theo cung lượng tim/HA."
    compatibility: ["NaCl 0.9%", "D5W"]
    incompatibility: ["Dung dịch kiềm/bicarbonate"]
    notes: "Ưu tiên central line nếu có; monitor nhịp/ECG."
- references:
  primary_sources:
    - "ESC/ACC HF acute recommendations (inotrope for low output)"
    - "Lexicomp/Micromedex Dobutamine"
  last_updated: "2025-12-23"
  evidence_level: "Guideline + tertiary database"
- risk_flags:
  high_alert: true
  narrow_therapeutic_index: false
  look_alike_sound_alike: []
  organ_toxicity:
    hepatic: "low"
    renal: "low"
    cardiac: "moderate"
    hematologic: "low"
  requires_double_check: true
  icu_critical_care_only: true
- guideline_tags:
  who_atc: "C01CA07"
  ahfs_category: ""
  vietnam_essential_medicines: false
  international_guidelines:
    - {source: "ACC/ESC HF", recommendation: "Inotrope for low-output HF/CS with adequate BP", context: "ICU"}
  vn_guidelines: []
  clinical_tags: ["cardiogenic-shock", "low-output-HF", "inotrope"]
- availability_vietnam:
  status: "common"
  level_of_care: ["provincial", "central", "private"]
  insurance_coverage: "unknown"
-  brand_examples: ["Dobutamine (nhiều NSX)"]
  notes: "Dùng ngắn hạn tại ICU; tránh kéo dài."

### Phenylephrine

- mechanism_of_action: "Chủ vận α1 chọn lọc → co mạch ngoại vi, tăng HA; không tác dụng β1 trực tiếp → ít làm tăng nhịp, có thể gây phản xạ chậm nhịp."
- monitoring:
  - Huyết áp, nhịp tim/ECG (có thể chậm nhịp phản xạ)
  - Tưới máu ngoại vi
- precautions:
  - Thích hợp khi cần tăng HA nhưng muốn hạn chế nhịp nhanh
  - Thận trọng bệnh mạch vành (tăng hậu tải), suy tim nặng
  - Tránh quá liều gây co mạch ngoại vi/thiếu máu chi
- pharmacokinetics:
  half_life: "≈2.5 giờ (tác dụng ngắn hơn do phân bố/chuyển hóa)"
  onset: "Tức thì IV"
  duration: "≈15–20 phút sau bolus; ngắn hơn khi truyền liên tục"
  protein_binding: "~95%"
  clearance: "Chuyển hóa qua MAO; thải trừ qua thận"
- storage: "Bảo quản nhiệt độ phòng, tránh ánh sáng; dung dịch pha dùng trong 24 giờ."
- black_box_warnings: None
- drug_interactions:
  major:
    - drug: "MAOI"
      mechanism: "Ức chế giáng hóa"
      effect: "Tăng mạnh HA"
      management: "Tránh/giảm liều, monitor sát"
  moderate:
    - drug: "TCA/SNRI"
      mechanism: "Tăng nhạy cảm α"
      effect: "Tăng HA"
      management: "Theo dõi HA, chỉnh liều"
    - drug: "Beta-blocker"
      mechanism: "Không ảnh hưởng trực tiếp, nhưng cần thận trọng chậm nhịp phản xạ"
      effect: "Bradycardia"
      management: "Theo dõi nhịp"
- pregnancy_lactation:
  fda_category: "C (cũ); dùng khi cần thiết"
  pregnancy_details: "Có thể giảm tưới máu nhau thai do co mạch."
  lactation:
    safety: "Caution"
    details: "Dữ liệu hạn chế; t½ ngắn."
    recommendation: "Cho bú lại sau khi ngừng truyền một thời gian ngắn."
- hepatic_adjustment:
  mild: "Không chỉnh; theo dõi HA."
  moderate: "Thận trọng."
  severe: "Thận trọng cao."
  notes: "Chỉnh theo đáp ứng."
- overdose_management:
  symptoms: ["Tăng HA", "Chậm nhịp phản xạ", "Co mạch chi/thiếu máu"]
  antidote: "Không đặc hiệu"
  treatment: ["Ngừng truyền", "Hạ áp nếu cần", "Theo dõi tưới máu chi"]
  monitoring: "HA, nhịp, tưới máu chi"
- reversal_agents: None
- administration_instructions:
  oral: {with_food: "", timing: ""}  # Không dùng đường uống
  iv:
    reconstitution: "Pha 10 mg trong 100 mL NaCl 0.9% (100 mcg/mL) hoặc nồng độ phù hợp bơm tiêm."
    infusion_rate: "0.2–9 mcg/kg/phút; hoặc 20–200 mcg/phút, titrate theo HA."
    compatibility: ["NaCl 0.9%", "D5W"]
    incompatibility: ["Dung dịch kiềm/bicarbonate"]
    notes: "Có thể bolus nhỏ trong một số tình huống; ưu tiên central line nếu liều cao/kéo dài."
- references:
  primary_sources:
    - "ACLS peri-arrest hypotension (phenylephrine as option)"
    - "Lexicomp/Micromedex Phenylephrine IV"
  last_updated: "2025-12-23"
  evidence_level: "Tertiary + practice"
- risk_flags:
  high_alert: true
  narrow_therapeutic_index: false
  look_alike_sound_alike: []
  organ_toxicity:
    hepatic: "low"
    renal: "low"
    cardiac: "moderate"
    hematologic: "low"
  requires_double_check: true
  icu_critical_care_only: false  # có thể dùng ngoài ICU trong thủ thuật, nhưng IV truyền nên thận trọng
- guideline_tags:
  who_atc: "C01CA06"
  ahfs_category: ""
  vietnam_essential_medicines: false
  international_guidelines: []
  vn_guidelines: []
  clinical_tags: ["hypotension", "vasopressor", "bradycardia-friendly"]
- availability_vietnam:
  status: "common"
  level_of_care: ["provincial", "central", "private"]
  insurance_coverage: "unknown"
  brand_examples: ["Phenylephrine (nhiều NSX)"]
  notes: "Dùng nhiều trong gây mê/ngoại khoa để nâng HA ngắn hạn."

### Nitroglycerin (IV)

- mechanism_of_action: "Giãn tĩnh mạch chủ yếu (tăng dự trữ tĩnh mạch, giảm tiền tải); liều cao giãn động mạch, giãn mạch vành; giảm đau ngực, giảm sung huyết phổi."
- monitoring:
  - Huyết áp, nhịp tim/ECG
  - Đau ngực, triệu chứng HF, SpO2
  - Đau đầu/hạ HA
- precautions:
  - Tránh dùng cùng PDE5i (sildenafil, tadalafil, vardenafil) trong 24–48h
  - Có thể gây tụt HA, nhịp nhanh phản xạ, đau đầu
  - Dùng thận trọng hẹp van ĐMC nặng, RV infarct (tránh giảm tiền tải)
- pharmacokinetics:
  half_life: "1–3 phút (nitroglycerin); tác dụng qua chất chuyển hóa"
  onset: "1–2 phút IV"
  duration: "3–5 phút sau ngừng"
  protein_binding: "60%"
  clearance: "Gan (chuyển hóa nhanh), thải trừ qua thận dưới dạng chất chuyển hóa"
- storage: "Bảo quản tránh ánh sáng; dung dịch pha trong chai thủy tinh hoặc bộ dây chuyên dụng chống hấp phụ."
- black_box_warnings: None
- drug_interactions:
  major:
    - drug: "PDE5 inhibitors"
      mechanism: "Cộng gộp NO-cGMP"
      effect: "Tụt HA nặng"
      management: "Chống chỉ định"
  moderate:
    - drug: "Riociguat"
      mechanism: "Tăng cGMP"
      effect: "Tụt HA"
      management: "Tránh"
- pregnancy_lactation:
  fda_category: "C (cũ); dữ liệu hạn chế"
  pregnancy_details: "Cân nhắc khi lợi ích vượt nguy cơ."
  lactation:
    safety: "Caution"
    details: "Dữ liệu hạn chế."
    recommendation: "Theo dõi, có thể cho bú lại sau ngừng truyền."
- hepatic_adjustment:
  mild: "Không cần chỉnh; thận trọng vì chuyển hóa qua gan."
  moderate: "Thận trọng; chỉnh theo đáp ứng HA."
  severe: "Thận trọng cao; nguy cơ tích lũy."
  notes: "Titrate theo HA."
- overdose_management:
  symptoms: ["Tụt HA", "Nhịp nhanh phản xạ", "Đau đầu, đỏ bừng"]
  antidote: "Không đặc hiệu"
  treatment: ["Ngừng truyền", "Truyền dịch, nâng HA nếu cần"]
  monitoring: "HA, nhịp, triệu chứng tưới máu"
- reversal_agents: None
- administration_instructions:
  oral: {with_food: "", timing: ""}  # Không dùng đường uống (đây là IV)
  iv:
    reconstitution: "Pha 50 mg trong 250 mL (200 mcg/mL) hoặc nồng độ theo nhãn, dùng bộ dây không PVC/hấp phụ."
    infusion_rate: "5–10 mcg/phút, tăng 5–10 mcg/phút mỗi 3–5 phút; thường 5–200 mcg/phút tùy chỉ định."
    compatibility: ["D5W", "NaCl 0.9% (tùy nhãn, kiểm tra hấp phụ)"]
    incompatibility: ["Dịch có chứa PVC nếu không có bộ dây phù hợp"]
    notes: "Tránh tiếp xúc ánh sáng; theo dõi HA sát."
- references:
  primary_sources:
    - "ACC/AHA ACS & HF guidance (IV nitrate use)"
    - "Lexicomp/Micromedex Nitroglycerin IV"
  last_updated: "2025-12-23"
  evidence_level: "Guideline + tertiary database"
- risk_flags:
  high_alert: true
  narrow_therapeutic_index: false
  look_alike_sound_alike: []
  organ_toxicity:
    hepatic: "moderate"
    renal: "low"
    cardiac: "moderate"
    hematologic: "low"
  requires_double_check: true
  icu_critical_care_only: false  # Dùng ở CCU/ICU hoặc phòng can thiệp; vẫn nên double-check
- guideline_tags:
  who_atc: "C01DA02"
  ahfs_category: ""
  vietnam_essential_medicines: false
  international_guidelines:
    - {source: "ACC/AHA", recommendation: "IV nitrate for ACS/HF with congestion if BP adequate", context: "CCU/ICU"}
  vn_guidelines: []
  clinical_tags: ["acs", "angina", "acute-hf", "vasodilator"]
- availability_vietnam:
  status: "common"
  level_of_care: ["provincial", "central", "private"]
  insurance_coverage: "unknown"
  brand_examples: ["Nitroglycerin IV (nhiều NSX)"]
  notes: "Cần dây truyền chuyên dụng (không PVC) để giảm hấp phụ."

### Nitroprusside

- mechanism_of_action: "Giải phóng NO trực tiếp, giãn cả động mạch và tĩnh mạch mạnh (giảm tiền/hậu tải); khởi phát cực nhanh."
- monitoring:
  - Huyết áp xâm lấn liên tục
  - Nhịp tim/ECG
  - Dấu hiệu nhiễm độc cyanide/thiocyanate: toan chuyển hóa, lú lẫn, co giật
  - Lactate, khí máu; nếu truyền kéo dài/liều cao: nồng độ thiocyanate (nếu có điều kiện)
- precautions:
  - High-alert; chỉ dùng khi có monitor HA xâm lấn
  - Tránh dùng kéo dài/ liều cao, đặc biệt suy thận/suy gan (tích lũy cyanide/thiocyanate)
  - Che tối dây/chai (nhạy sáng)
  - Tránh ở thiếu máu cơ tim nặng (giảm tưới máu mạch vành nếu hạ HA quá nhanh)
- pharmacokinetics:
  half_life: "Vài phút; cyanide chuyển thành thiocyanate (t½ thiocyanate 3–7 ngày, kéo dài ở suy thận)"
  onset: "Gần như tức thì"
  duration: "1–2 phút sau ngừng"
  protein_binding: "Thấp"
  clearance: "Chuyển hóa thành cyanide → thiocyanate (gan, thận); thải thiocyanate qua thận"
- storage: "Dung dịch nhạy sáng, cần che tối; pha trong D5W (theo nhãn); dùng trong 24 giờ."
- black_box_warnings: "Nguy cơ nhiễm độc cyanide/thiocyanate, đặc biệt ở liều cao, truyền kéo dài, suy thận/suy gan; cần monitor sát và giới hạn liều/thời gian."
- drug_interactions:
  major:
    - drug: "Thuốc hạ áp khác (vasodilators, anesthetics)"
      mechanism: "Cộng gộp hạ áp"
      effect: "Tụt HA nặng"
      management: "Titrate thận trọng, monitor xâm lấn"
  moderate:
    - drug: "PDE5i/riociguat"
      mechanism: "Tăng NO/cGMP"
      effect: "Hạ HA mạnh"
      management: "Tránh phối hợp"
- pregnancy_lactation:
  fda_category: "C (cũ); tránh nếu có lựa chọn khác an toàn hơn"
  pregnancy_details: "Nguy cơ độc cyanide cho mẹ và thai; chỉ dùng khi lợi ích vượt nguy cơ rõ rệt."
  lactation:
    safety: "Caution/avoid"
    details: "Chưa rõ bài tiết; độc tính tiềm tàng."
    recommendation: "Tránh cho bú hoặc ngừng thuốc trước khi cho bú."
- hepatic_adjustment:
  mild: "Thận trọng; tăng nguy cơ độc cyanide"
  moderate: "Tránh/giới hạn liều"
  severe: "Tránh nếu có thể; nếu buộc phải dùng, liều tối thiểu, theo dõi rất sát"
  notes: "Suy gan giảm chuyển hóa cyanide → tăng độc tính"
- overdose_management:
  symptoms: ["Tụt HA sâu", "Toan chuyển hóa", "Lú lẫn, co giật", "Nhiễm độc cyanide/thiocyanate"]
  antidote: "Bộ kit giải độc cyanide (thiosulfate, hydroxocobalamin) tùy sẵn có"
  treatment: ["Ngừng truyền ngay", "Hỗ trợ HA (vasopressor)", "Truyền thiosulfate/hydroxocobalamin nếu nghi ngờ độc cyanide", "Thẩm tách nếu độc thiocyanate và suy thận"]
  monitoring: "HA xâm lấn, khí máu, lactate; thiocyanate nếu truyền >24–48h hoặc suy thận"
- reversal_agents: None
- administration_instructions:
  oral: {with_food: "", timing: ""}  # Không dùng đường uống
  iv:
    reconstitution: "Pha theo nhãn, thường 50 mg trong 250 mL D5W (200 mcg/mL); bắt buộc che tối dây/chai."
    infusion_rate: "Bắt đầu 0.3–0.5 mcg/kg/phút, tối đa thường khuyến cáo ≤10 mcg/kg/phút trong thời gian rất ngắn; giảm liều khi đạt HA mục tiêu."
    compatibility: ["D5W"]
    incompatibility: ["NaCl 0.9% (nhãn thường yêu cầu D5W)", "Dung dịch kiềm/bicarbonate"]
    notes: "Monitor HA xâm lấn; giới hạn liều và thời gian; che tối dây/chai; theo dõi dấu hiệu độc cyanide/thiocyanate."
- references:
  primary_sources:
    - "AHA/ACC HTN emergency management"
    - "Lexicomp/Micromedex Nitroprusside"
  last_updated: "2025-12-23"
  evidence_level: "Guideline + tertiary database"
- risk_flags:
  high_alert: true
  narrow_therapeutic_index: true
  look_alike_sound_alike: []
  organ_toxicity:
    hepatic: "high"
    renal: "high"  # tích lũy thiocyanate ở suy thận
    cardiac: "moderate"
    hematologic: "low"
  requires_double_check: true
  icu_critical_care_only: true
- guideline_tags:
  who_atc: "C02DD01"
  ahfs_category: ""
  vietnam_essential_medicines: false
  international_guidelines:
    - {source: "AHA/ACC", recommendation: "Option for hypertensive emergency (short-term, monitored)", context: "ICU"}
  vn_guidelines: []
  clinical_tags: ["hypertensive-emergency", "afterload-reduction", "acute-hf"]
- availability_vietnam:
  status: "limited"
  level_of_care: ["central", "private"]
  insurance_coverage: "unknown"
  brand_examples: ["Nitroprusside (tùy NSX)"]
  notes: "Thường hạn chế do nguy cơ độc; cần điều kiện monitor xâm lấn và che tối."


