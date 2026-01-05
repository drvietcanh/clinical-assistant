# Tóm tắt lỗi syntax cần sửa

## Vấn đề

Có **26 files** trong `drugs/drug_modules/` có lỗi syntax tương tự nhau liên quan đến cấu trúc `drug_interactions`.

## Pattern lỗi

Lỗi xuất hiện với pattern: `}], 'mechanism':`

Cấu trúc đúng nên là:
```python
'drug_interactions': {
    'major': [...],
    'moderate': [...],
    'minor': [...]
}
```

Nhưng hiện tại có nhiều file có cấu trúc sai:
```python
'drug_interactions': {
    'major': [...],
    'mechanism': ...  # SAI - thiếu 'moderate': [
}
```

## Danh sách files cần sửa

1. drugs/drug_modules/endocrinology_other/corticosteroids/short_intermediate_acting.py
2. drugs/drug_modules/endocrinology_other/corticosteroids/long_acting.py
3. drugs/drug_modules/supportive/vitamin_ds.py
4. drugs/drug_modules/supportive/vitamin_b12s.py
5. drugs/drug_modules/supportive/irons.py
6. drugs/drug_modules/supportive/folates.py (đang sửa, còn lỗi)
7. drugs/drug_modules/oncology/platinum_compounds.py
8. drugs/drug_modules/oncology/antimetabolite_antifolates.py
9. drugs/drug_modules/oncology/antimetabolites.py
10. drugs/drug_modules/oncology/anthracyclines.py
11. drugs/drug_modules/oncology/alkylating_agents.py
12. drugs/drug_modules/miscellaneous/xanthine_oxidase_inhibitors.py
13. drugs/drug_modules/miscellaneous/beta_2_agonist_short_actings.py
14. drugs/drug_modules/miscellaneous/analgesicantipyreticnsaid.py
15. drugs/drug_modules/miscellaneous/analgesicantipyretic.py
16. drugs/drug_modules/infectious_other/tetracyclines.py
17. drugs/drug_modules/infectious_other/nitroimidazoles.py
18. drugs/drug_modules/infectious_other/macrolides.py
19. drugs/drug_modules/infectious_other/fluoroquinolones.py
20. drugs/drug_modules/infectious_other/cephalosporins.py
21. drugs/drug_modules/infectious_other/beta_lactams.py
22. drugs/drug_modules/emergency/opioid_antagonists.py
23. drugs/drug_modules/emergency/local_anesthetic__antiarrhythmic_class_ibs.py
24. drugs/drug_modules/emergency/catecholamine_alpha__beta_agonists.py
25. drugs/drug_modules/emergency/anticholinergics.py
26. drugs/drug_modules/emergency/antiarrhythmics.py

## Files đã sửa

1. ✅ drugs/drug_modules/neurological/ssri_selective_serotonin_reuptake_inhibitors.py
2. ✅ drugs/drug_modules/neurological/anticonvulsant_alpha_2_delta_ligands.py
3. ✅ drugs/drug_modules/neurological/alzheimer_dementia_drugs.py
4. ✅ drugs/drug_modules/supportive/calciums.py
5. ⚠️ drugs/drug_modules/supportive/folates.py (đang sửa, còn lỗi brace count)

## Cách sửa

Với mỗi file:
1. Tìm pattern `}], 'mechanism':`
2. Thay bằng `}], 'moderate': [`
3. Đảm bảo các interactions sau đó được wrap trong dict format: `{'drug': ..., 'mechanism': ..., 'effect': ..., 'management': ...}`
4. Đóng 'moderate' list với `}],`
5. Kiểm tra brace count và syntax

## Script hỗ trợ

Đã tạo `fix_drug_interactions_syntax.py` nhưng cần manual review cho mỗi file.

## Khuyến nghị

Nên sửa tất cả 26 files trước khi tiếp tục với các todos khác, vì chúng đang chặn việc import DRUG_DATABASE.




