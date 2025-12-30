# Danh sách đầy đủ các bệnh trong hệ thống

**Tổng số:** 72 bệnh  
**Cập nhật:** 2025-01-30

---

## 📋 Danh sách theo chuyên khoa

### 1. Cardiology (Tim mạch) - 9 bệnh
1. `heart_failure` - Suy tim
2. `myocardial_infarction` - Nhồi máu cơ tim cấp
3. `hypertension` - Tăng huyết áp
4. `atrial_fibrillation` - Rung nhĩ
5. `coronary_artery_disease` - Bệnh mạch vành
6. `valvular_heart_disease` - Bệnh van tim
7. `myocarditis` - Viêm cơ tim
8. `pericarditis` - Viêm màng ngoài tim
9. `dilated_cardiomyopathy` - Bệnh cơ tim giãn

### 2. Infectious (Nhiễm khuẩn) - 6 bệnh
10. `pneumonia` - Viêm phổi
11. `sepsis` - Nhiễm khuẩn huyết / Sepsis
12. `tuberculosis` - Lao phổi
13. `dengue_fever` - Sốt xuất huyết Dengue
14. `malaria` - Sốt rét
15. `japanese_encephalitis` - Viêm não Nhật Bản

### 3. Gastroenterology (Tiêu hóa) - 5 bệnh
16. `peptic_ulcer_disease` - Loét dạ dày tá tràng
17. `gastroesophageal_reflux` - Trào ngược dạ dày thực quản (GERD)
18. `hepatitis_b` - Viêm gan B
19. `cirrhosis` - Xơ gan
20. `irritable_bowel_syndrome` - Hội chứng ruột kích thích (IBS)

### 4. Neurology (Thần kinh) - 4 bệnh
21. `stroke` - Đột quỵ thiếu máu cục bộ cấp
22. `epilepsy` - Động kinh
23. `migraine` - Đau nửa đầu (Migraine)
24. `parkinson_disease` - Bệnh Parkinson

### 5. ENT (Tai Mũi Họng) - 3 bệnh
25. `acute_pharyngitis` - Viêm họng cấp
26. `sinusitis` - Viêm xoang
27. `otitis_media` - Viêm tai giữa

### 6. Orthopedics (Cơ xương khớp) - 3 bệnh
28. `osteoarthritis` - Thoái hóa khớp
29. `rheumatoid_arthritis` - Viêm khớp dạng thấp
30. `osteoporosis` - Loãng xương

### 7. Obstetrics/Gynecology (Sản phụ khoa) - 3 bệnh
31. `pelvic_inflammatory_disease` - Viêm nhiễm phụ khoa
32. `uterine_fibroids` - U xơ tử cung
33. `polycystic_ovary_syndrome` - Hội chứng buồng trứng đa nang (PCOS)

### 8. Oncology (Ung bướu) - 3 bệnh
34. `lung_cancer` - Ung thư phổi
35. `hepatocellular_carcinoma` - Ung thư gan
36. `breast_cancer` - Ung thư vú

### 9. Endocrinology (Nội tiết) - 3 bệnh
37. `diabetes_type2` - Đái tháo đường type 2
38. `hyperthyroidism` - Cường giáp
39. `hypothyroidism` - Suy giáp

### 10. Emergency (Cấp cứu) - 2 bệnh
40. `anaphylaxis` - Phản vệ
41. `acute_poisoning` - Ngộ độc cấp

### 11. Hematology (Huyết học) - 2 bệnh
42. `iron_deficiency_anemia` - Thiếu máu thiếu sắt
43. `thrombocytopenia` - Giảm tiểu cầu

### 12. Dermatology (Da liễu) - 2 bệnh
44. `atopic_dermatitis` - Viêm da cơ địa
45. `psoriasis` - Vẩy nến

### 13. Psychiatry (Tâm thần) - 2 bệnh
46. `major_depression` - Trầm cảm
47. `anxiety_disorder` - Rối loạn lo âu

### 14. Respiratory (Hô hấp) - 2 bệnh
48. `copd` - Bệnh phổi tắc nghẽn mạn tính (COPD)
49. `asthma` - Hen phế quản

### 15. Nephrology (Thận) - 2 bệnh
50. `aki` - Tổn thương thận cấp (AKI)
51. `chronic_kidney_disease` - Suy thận mạn tính (CKD)

### 16. Urology (Tiết niệu) - 2 bệnh
52. `urinary_tract_infection` - Nhiễm trùng đường tiết niệu
53. `kidney_stones` - Sỏi thận

### 17. Pediatrics (Nhi khoa) - 2 bệnh
54. `malnutrition` - Suy dinh dưỡng
55. `hand_foot_mouth_disease` - Bệnh tay chân miệng

### 18. Ophthalmology (Mắt) - 2 bệnh
56. `cataract` - Đục thủy tinh thể
57. `conjunctivitis` - Viêm kết mạc

### 19. Allergy/Immunology (Dị ứng miễn dịch) - 2 bệnh
58. `food_allergy` - Dị ứng thực phẩm
59. `contact_dermatitis` - Viêm da tiếp xúc

### 20. Rheumatology (Khớp) - 1 bệnh
60. `gout` - Bệnh gút

### 21. Critical Care (Hồi sức) - 4 bệnh
61. `ards` - Hội chứng suy hô hấp cấp (ARDS)
62. `septic_shock` - Sốc nhiễm khuẩn
63. `cardiogenic_shock` - Sốc tim
64. `mods` - Hội chứng suy đa tạng (MODS)

---

## 📊 Thống kê

- **Tổng số bệnh:** 72
- **Số chuyên khoa có dữ liệu:** 21/21 ✅
- **Trạng thái:** Tất cả modules đã có dữ liệu!

---

## 🔍 Tìm kiếm bệnh

### Theo ID:
```python
from diseases import get_disease_info
disease = get_disease_info("pneumonia")
```

### Theo tên:
```python
from diseases import search_diseases
results = search_diseases("viêm phổi")
```

### Theo chuyên khoa:
```python
from diseases import get_diseases_by_category
cardio = get_diseases_by_category("Cardiology")
```

### Theo ICD-10:
```python
from diseases.management import get_diseases_by_icd10
results = get_diseases_by_icd10("J18.9")
```

### Theo thuốc:
```python
from diseases.management import get_diseases_by_drug
results = get_diseases_by_drug("Metformin")
```

---

## 📝 Ghi chú

- Tất cả bệnh đều có đầy đủ thông tin: định nghĩa, nguyên nhân, triệu chứng, chẩn đoán, điều trị, phòng ngừa, biến chứng
- Mỗi bệnh có ICD-10 codes, related scores, related drugs, related protocols
- Hệ thống tự động tổng hợp và tạo category mapping

