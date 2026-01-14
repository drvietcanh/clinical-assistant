# Kế Hoạch Bổ Sung Field Cho Các Thuốc Thần Kinh

## Tổng Quan

Bổ sung đầy đủ các field còn thiếu cho các thuốc thần kinh, bao gồm:
- **4 field bổ sung quan trọng**: `pediatric_dosing`, `geriatric_dosing`, `brand_names`, `cost_estimate`
- **Sửa format sai**: Tách `cost_estimate` ra khỏi `brand_names` (nếu bị đặt nhầm)
- **Bổ sung chi tiết**: Đảm bảo `pharmacokinetics` có đầy đủ `metabolism` và `clearance`

## Cấu Trúc Field Cần Bổ Sung

### 1. pediatric_dosing
```python
"pediatric_dosing": {
    "neonates": "...",
    "infants": "...",
    "children": "...",
    "adolescents": "...",
    "notes": "..."
}
```

### 2. geriatric_dosing
```python
"geriatric_dosing": {
    "considerations": "...",
    "dose_adjustment": "...",
    "monitoring": "..."
}
```

### 3. brand_names
```python
"brand_names": {
    "vietnam": ["...", "..."],
    "common": ["...", "..."]
}
```

### 4. cost_estimate
```python
"cost_estimate": {
    "unit": "VND",
    "range": "...",
    "note": "..."
}
```

## Danh Sách File Cần Bổ Sung

### File 1: anticonvulsants.py (14 thuốc)
1. Carbamazepine - **SỬA**: Tách `cost_estimate` ra khỏi `brand_names`
2. Ethosuximide - ✅ Đã có đầy đủ
3. Fosphenytoin - Cần kiểm tra và bổ sung
4. Lacosamide - Cần kiểm tra và bổ sung
5. Lamotrigine - Cần kiểm tra và bổ sung
6. Levetiracetam - Cần kiểm tra và bổ sung
7. Oxcarbazepine - **SỬA**: Tách `cost_estimate` ra khỏi `brand_names`
8. Perampanel - Cần kiểm tra và bổ sung
9. Phenobarbital - ✅ Đã có đầy đủ
10. Phenytoin - **SỬA**: Tách `cost_estimate` ra khỏi `brand_names`
11. Primidone - Cần kiểm tra và bổ sung
12. Topiramate - Cần kiểm tra và bổ sung
13. Valproate - **SỬA**: Tách `cost_estimate` ra khỏi `brand_names`
14. Zonisamide - Cần kiểm tra và bổ sung

### File 2: benzodiazepines.py (3 thuốc)
1. Clonazepam - **THIẾU HOÀN TOÀN**: `pediatric_dosing`, `geriatric_dosing`, `brand_names`, `cost_estimate`
2. Diazepam - **THIẾU HOÀN TOÀN**: `pediatric_dosing`, `geriatric_dosing`, `brand_names`, `cost_estimate`
3. Lorazepam - **THIẾU HOÀN TOÀN**: `pediatric_dosing`, `geriatric_dosing`, `brand_names`, `cost_estimate`

### File 3: antiparkinsonian.py (8 thuốc)
1. Deutetrabenazine - Cần kiểm tra và bổ sung
2. Istradefylline - Cần kiểm tra và bổ sung
3. Opicapone - Cần kiểm tra và bổ sung
4. Pimavanserin - Cần kiểm tra và bổ sung
5. Pramipexole - Cần kiểm tra và bổ sung
6. Ropinirole - Cần kiểm tra và bổ sung
7. Safinamide - Cần kiểm tra và bổ sung
8. Tetrabenazine - Cần kiểm tra và bổ sung

### File 4: Các file khác (kiểm tra sau)
- alzheimer_dementia_drugs.py
- anticonvulsant_alpha_2_delta_ligands.py
- cerebral_circulation.py
- migraine_triptans.py
- migraine_cgrp_drugs.py
- muscle_relaxants.py
- multiple_sclerosis_drugs.py
- ssri_selective_serotonin_reuptake_inhibitors.py

## Kế Hoạch Thực Hiện Theo Phiên

### PHIÊN 1: Sửa format sai trong anticonvulsants.py
**Mục tiêu**: Tách `cost_estimate` ra khỏi `brand_names` cho 4 thuốc

**Thuốc cần sửa**:
1. Carbamazepine (dòng ~167-173)
2. Oxcarbazepine (dòng ~1201-1207)
3. Phenytoin (dòng ~1806-1812)
4. Valproate (dòng ~2366-2372)

**Công việc**:
- Đọc phần `brand_names` của từng thuốc
- Tách `range` và `note` ra thành field `cost_estimate` riêng
- Đảm bảo `brand_names` chỉ chứa `vietnam` và `common`
- Đảm bảo `cost_estimate` có format: `{"unit": "VND", "range": "...", "note": "..."}`

### PHIÊN 2: Bổ sung field cho benzodiazepines.py (3 thuốc)
**Mục tiêu**: Bổ sung đầy đủ 4 field cho tất cả 3 thuốc benzodiazepine

**Thuốc**:
1. Clonazepam
2. Diazepam
3. Lorazepam

**Công việc cho mỗi thuốc**:
- Nghiên cứu từ FDA, UpToDate, Medscape, Drugs.com
- Bổ sung `pediatric_dosing` (liều cho trẻ em, đặc biệt chú ý an toàn)
- Bổ sung `geriatric_dosing` (liều cho người cao tuổi, chú ý té ngã, lú lẫn)
- Bổ sung `brand_names` (tên thương mại ở Việt Nam và quốc tế)
- Bổ sung `cost_estimate` (giá ước tính ở Việt Nam)

**Lưu ý đặc biệt**:
- Benzodiazepine có nguy cơ phụ thuộc, nghiện cao
- Nguy cơ té ngã ở người cao tuổi
- Nguy cơ suy hô hấp khi dùng với opioids/alcohol
- Cần thận trọng với trẻ em

### PHIÊN 3: Bổ sung field cho anticonvulsants.py - Nhóm 1 (4 thuốc)
**Mục tiêu**: Bổ sung đầy đủ field cho 4 thuốc đầu tiên còn thiếu

**Thuốc**:
1. Fosphenytoin
2. Lacosamide
3. Lamotrigine
4. Levetiracetam

**Công việc cho mỗi thuốc**:
- Kiểm tra các field hiện có
- Bổ sung các field còn thiếu: `pediatric_dosing`, `geriatric_dosing`, `brand_names`, `cost_estimate`
- Đảm bảo `pharmacokinetics` có đầy đủ `metabolism` và `clearance`
- Nghiên cứu từ FDA, UpToDate, Medscape, Drugs.com

### PHIÊN 4: Bổ sung field cho anticonvulsants.py - Nhóm 2 (4 thuốc)
**Mục tiêu**: Bổ sung đầy đủ field cho 4 thuốc tiếp theo

**Thuốc**:
1. Perampanel
2. Primidone
3. Topiramate
4. Zonisamide

**Công việc**: Tương tự Phiên 3

### PHIÊN 5: Bổ sung field cho antiparkinsonian.py - Nhóm 1 (4 thuốc)
**Mục tiêu**: Bổ sung đầy đủ field cho 4 thuốc đầu tiên

**Thuốc**:
1. Deutetrabenazine
2. Istradefylline
3. Opicapone
4. Pimavanserin

**Công việc cho mỗi thuốc**:
- Kiểm tra các field hiện có
- Bổ sung các field còn thiếu
- Nghiên cứu từ FDA, UpToDate, Medscape, Drugs.com
- Chú ý đặc biệt: trầm cảm, QT kéo dài, tác dụng phụ thần kinh

### PHIÊN 6: Bổ sung field cho antiparkinsonian.py - Nhóm 2 (4 thuốc)
**Mục tiêu**: Bổ sung đầy đủ field cho 4 thuốc còn lại

**Thuốc**:
1. Pramipexole
2. Ropinirole
3. Safinamide
4. Tetrabenazine

**Công việc**: Tương tự Phiên 5

### PHIÊN 7: Kiểm tra và bổ sung các file khác
**Mục tiêu**: Kiểm tra và bổ sung field cho các file còn lại

**File cần kiểm tra**:
1. alzheimer_dementia_drugs.py
2. anticonvulsant_alpha_2_delta_ligands.py
3. cerebral_circulation.py
4. migraine_triptans.py
5. migraine_cgrp_drugs.py
6. muscle_relaxants.py
7. multiple_sclerosis_drugs.py
8. ssri_selective_serotonin_reuptake_inhibitors.py

**Công việc**:
- Đếm số thuốc trong mỗi file
- Kiểm tra field hiện có
- Bổ sung các field còn thiếu
- Chia thành các phiên nhỏ nếu cần

### PHIÊN 8: Kiểm tra tổng thể và sửa lỗi
**Mục tiêu**: Kiểm tra lại tất cả các field đã bổ sung

**Công việc**:
- Kiểm tra syntax Python
- Kiểm tra format field
- Kiểm tra tính nhất quán
- Kiểm tra đầy đủ thông tin
- Sửa các lỗi phát hiện được

## Nguồn Tham Khảo

### Nguồn chính:
1. **FDA Drug Labels**: https://www.fda.gov/drugs/drug-approvals-and-databases
2. **UpToDate**: Drug information monographs
3. **Medscape**: Drug reference
4. **Drugs.com**: Drug information
5. **Lexicomp**: Drug monographs
6. **Goodman & Gilman's**: Pharmacological Basis of Therapeutics

### Nguồn bổ sung:
- Nhà sản xuất: Package inserts, official websites
- Guidelines: AAN (American Academy of Neurology), ILAE (International League Against Epilepsy)
- ISMP: High Alert Medications

## Lưu Ý Quan Trọng

### 1. An toàn thuốc
- **Benzodiazepine**: Phụ thuộc, nghiện, té ngã, suy hô hấp
- **Anticonvulsants**: Nguy cơ tự sát, dị tật bẩm sinh, độc tính gan/thận
- **Antiparkinsonian**: Trầm cảm, QT kéo dài, rối loạn vận động

### 2. Liều dùng đặc biệt
- **Trẻ em**: Cần tính theo cân nặng, theo dõi chặt chẽ
- **Người cao tuổi**: Giảm liều, tăng nguy cơ tác dụng phụ
- **Suy gan/thận**: Điều chỉnh liều theo chức năng

### 3. Tương tác thuốc
- Benzodiazepine + Opioids/Alcohol: Suy hô hấp nguy hiểm
- Anticonvulsants: Nhiều tương tác do cảm ứng/ức chế enzyme
- Antiparkinsonian: Tương tác với MAO inhibitors, thuốc kéo dài QT

### 4. Theo dõi
- Nồng độ trong máu (nếu có therapeutic range)
- Chức năng gan, thận
- Công thức máu
- ECG (nếu có nguy cơ QT kéo dài)
- Dấu hiệu tác dụng phụ nghiêm trọng

## Tiêu Chuẩn Chất Lượng

### Mỗi field phải:
1. **Đầy đủ**: Có đủ thông tin cần thiết
2. **Chính xác**: Dựa trên nguồn đáng tin cậy
3. **Nhất quán**: Format giống nhau giữa các thuốc
4. **Rõ ràng**: Dễ hiểu, không mơ hồ
5. **Cập nhật**: Thông tin mới nhất

### Format chuẩn:
- Sử dụng dấu nháy đơn `'` cho key trong dict
- Sử dụng dấu nháy kép `"` cho string trong dict
- Indent 8 spaces cho level 1, 12 spaces cho level 2
- Không có trailing comma ở field cuối cùng

## Checklist Cho Mỗi Thuốc

- [ ] `pediatric_dosing`: Đầy đủ cho neonates, infants, children, adolescents
- [ ] `geriatric_dosing`: Có considerations, dose_adjustment, monitoring
- [ ] `brand_names`: Có vietnam và common
- [ ] `cost_estimate`: Có unit, range, note
- [ ] `pharmacokinetics`: Có metabolism và clearance chi tiết
- [ ] Syntax Python: Không có lỗi
- [ ] Format: Nhất quán với các thuốc khác
- [ ] Thông tin: Chính xác, đầy đủ

## Thời Gian Ước Tính

- **Phiên 1**: 30 phút (sửa format)
- **Phiên 2**: 2-3 giờ (3 thuốc benzodiazepine)
- **Phiên 3**: 2-3 giờ (4 thuốc anticonvulsants)
- **Phiên 4**: 2-3 giờ (4 thuốc anticonvulsants)
- **Phiên 5**: 2-3 giờ (4 thuốc antiparkinsonian)
- **Phiên 6**: 2-3 giờ (4 thuốc antiparkinsonian)
- **Phiên 7**: 3-4 giờ (8 file khác, tùy số lượng thuốc)
- **Phiên 8**: 1-2 giờ (kiểm tra tổng thể)

**Tổng thời gian ước tính**: 15-22 giờ

## Ghi Chú

- Làm thủ công, cẩn thận từng field
- Nghiên cứu kỹ từ các nguồn đáng tin cậy
- Chia phiên để tránh code quá dài
- Kiểm tra lại sau mỗi phiên
- Lưu backup trước khi sửa
