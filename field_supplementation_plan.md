# KẾ HOẠCH BỔ SUNG CÁC FIELD CÒN THIẾU CHO THUỐC

## 📋 TỔNG QUAN

**Mục tiêu**: Bổ sung đầy đủ các field còn thiếu cho **22 thuốc mới** đã được thêm thủ công.

**Các field cần bổ sung**:
1. `brand_names` - Tên biệt dược
2. `pediatric_dosing` - Liều dùng trẻ em
3. `geriatric_dosing` - Liều dùng người cao tuổi
4. `cost_estimate` - Ước tính giá
5. `storage` - Điều kiện bảo quản (chỉ cho 4 thuốc antipsychotics)

---

## 🎯 PHƯƠNG PHÁP TÌM KIẾM THÔNG TIN

### Nguồn thông tin ưu tiên:

1. **Tên biệt dược (brand_names)**:
   - ✅ Web search: "[Tên thuốc] brand names Vietnam"
   - ✅ Web search: "[Tên thuốc] biệt dược Việt Nam"
   - ✅ Các trang: nhathuocphuongchinh.com, nhathuocminhthuy.vn, thuocbietduoc.com.vn
   - ✅ FDA Drug Labels (cho brand names quốc tế)

2. **Liều dùng trẻ em (pediatric_dosing)**:
   - ✅ UpToDate - Pediatric dosing
   - ✅ FDA Drug Labels - Pediatric section
   - ✅ Lexicomp, Micromedex
   - ✅ Web search: "[Tên thuốc] pediatric dosing"
   - ✅ WHO Essential Medicines List

3. **Liều dùng người cao tuổi (geriatric_dosing)**:
   - ✅ UpToDate - Geriatric dosing
   - ✅ FDA Drug Labels - Geriatric section
   - ✅ Beers Criteria (nếu có)
   - ✅ Web search: "[Tên thuốc] geriatric dosing elderly"

4. **Ước tính giá (cost_estimate)**:
   - ✅ Web search: "[Tên thuốc] giá Việt Nam"
   - ✅ Web search: "[Tên thuốc] giá nhà thuốc"
   - ✅ Các trang: nhathuocphuongchinh.com, nhathuocminhthuy.vn
   - ✅ Lưu ý: Giá có thể thay đổi, chỉ ước tính khoảng

5. **Điều kiện bảo quản (storage)**:
   - ✅ FDA Drug Labels - Storage section
   - ✅ Web search: "[Tên thuốc] storage conditions"
   - ✅ Thường là: "Nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng"

---

## 📝 DANH SÁCH THUỐC CẦN BỔ SUNG

### PHASE 1: SLEEP MEDICATIONS (5 thuốc)

#### 1. Zolpidem
- [ ] `brand_names` - Tìm: Stilnox, Ambien, Zolpidem STADA, Zolpidem Stella
- [ ] `pediatric_dosing` - Thường không khuyến cáo <18 tuổi
- [ ] `geriatric_dosing` - Giảm liều 5mg, tối đa 5mg/ngày
- [ ] `cost_estimate` - Tìm giá Stilnox, Zolpidem generic

**Nguồn tìm kiếm**:
- Web: "Zolpidem Stilnox giá Việt Nam"
- Web: "Zolpidem pediatric dosing"
- FDA Label: Ambien (Zolpidem)

#### 2. Zaleplon
- [ ] `brand_names` - Tìm: Sonata
- [ ] `pediatric_dosing` - Thường không khuyến cáo <18 tuổi
- [ ] `geriatric_dosing` - Giảm liều 5mg
- [ ] `cost_estimate` - Tìm giá Zaleplon

**Nguồn tìm kiếm**:
- Web: "Zaleplon Sonata giá"
- FDA Label: Sonata (Zaleplon)

#### 3. Eszopiclone
- [ ] `brand_names` - Tìm: Lunesta
- [ ] `pediatric_dosing` - Thường không khuyến cáo <18 tuổi
- [ ] `geriatric_dosing` - Giảm liều 1mg
- [ ] `cost_estimate` - Tìm giá Lunesta, Eszopiclone

**Nguồn tìm kiếm**:
- Web: "Eszopiclone Lunesta giá"
- FDA Label: Lunesta (Eszopiclone)

#### 4. Ramelteon
- [ ] `brand_names` - Tìm: Rozerem
- [ ] `pediatric_dosing` - Thường không khuyến cáo <18 tuổi
- [ ] `geriatric_dosing` - Liều tương tự, thận trọng
- [ ] `cost_estimate` - Tìm giá Rozerem, Ramelteon

**Nguồn tìm kiếm**:
- Web: "Ramelteon Rozerem giá"
- FDA Label: Rozerem (Ramelteon)

#### 5. Suvorexant
- [ ] `brand_names` - Tìm: Belsomra
- [ ] `pediatric_dosing` - Thường không khuyến cáo <18 tuổi
- [ ] `geriatric_dosing` - Giảm liều 10mg, tối đa 15mg
- [ ] `cost_estimate` - Tìm giá Belsomra, Suvorexant

**Nguồn tìm kiếm**:
- Web: "Suvorexant Belsomra giá"
- FDA Label: Belsomra (Suvorexant)

---

### PHASE 2: VESTIBULAR DRUGS (3 thuốc)

#### 6. Betahistine
- [ ] `brand_names` - Tìm: Serc, Betaserc, Betahistine STADA
- [ ] `pediatric_dosing` - Thường không khuyến cáo <18 tuổi
- [ ] `geriatric_dosing` - Liều tương tự, thận trọng
- [ ] `cost_estimate` - Tìm giá Serc, Betaserc

**Nguồn tìm kiếm**:
- Web: "Betahistine Serc giá Việt Nam"
- Web: "Betahistine biệt dược"
- Web: "Betahistine pediatric dosing"

#### 7. Dimenhydrinate
- [ ] `brand_names` - Tìm: Dramamine, Gravol
- [ ] `pediatric_dosing` - Có liều cho trẻ em (12.5-50mg tùy tuổi)
- [ ] `geriatric_dosing` - Giảm liều, thận trọng
- [ ] `cost_estimate` - Tìm giá Dramamine

**Nguồn tìm kiếm**:
- Web: "Dimenhydrinate Dramamine giá"
- Web: "Dimenhydrinate pediatric dosing"
- FDA Label: Dramamine

#### 8. Meclizine
- [ ] `brand_names` - Tìm: Antivert, Bonine
- [ ] `pediatric_dosing` - Thường không khuyến cáo <12 tuổi
- [ ] `geriatric_dosing` - Giảm liều 25mg
- [ ] `cost_estimate` - Tìm giá Antivert, Meclizine

**Nguồn tìm kiếm**:
- Web: "Meclizine Antivert giá"
- Web: "Meclizine pediatric dosing"
- FDA Label: Antivert (Meclizine)

---

### PHASE 3: NEUROLOGICAL COMBINATIONS - MỚI (7 thuốc)

#### 9. Sumatriptan/Naproxen (Treximet)
- [ ] `brand_names` - Tìm: Treximet
- [ ] `pediatric_dosing` - Thường không khuyến cáo <18 tuổi
- [ ] `geriatric_dosing` - Thận trọng, liều tương tự
- [ ] `cost_estimate` - Tìm giá Treximet

**Nguồn tìm kiếm**:
- Web: "Treximet Sumatriptan Naproxen giá"
- FDA Label: Treximet
- Web: "Treximet pediatric dosing"

#### 10. Diphenhydramine/Melatonin
- [ ] `brand_names` - Tìm: Các sản phẩm kết hợp, Sleep Aid Combination
- [ ] `pediatric_dosing` - Thận trọng ở trẻ em
- [ ] `geriatric_dosing` - Thận trọng, giảm liều
- [ ] `cost_estimate` - Tìm giá sản phẩm kết hợp

**Nguồn tìm kiếm**:
- Web: "Diphenhydramine Melatonin combination giá"
- Web: "Diphenhydramine pediatric dosing"
- Web: "Melatonin pediatric dosing"

#### 11. Betahistine/Cinnarizine
- [ ] `brand_names` - Tìm: Các sản phẩm kết hợp
- [ ] `pediatric_dosing` - Thường không khuyến cáo <18 tuổi
- [ ] `geriatric_dosing` - Thận trọng, tránh dùng kéo dài
- [ ] `cost_estimate` - Tìm giá sản phẩm kết hợp

**Nguồn tìm kiếm**:
- Web: "Betahistine Cinnarizine combination giá"
- Web: "Betahistine Cinnarizine biệt dược"

#### 12. Dihydroergotamine/Metoclopramide
- [ ] `brand_names` - Tìm: Migranal, DHE-45 (có thể kết hợp với metoclopramide)
- [ ] `pediatric_dosing` - Thường không khuyến cáo <18 tuổi
- [ ] `geriatric_dosing` - Thận trọng, CHỐNG CHỈ ĐỊNH nếu có bệnh tim mạch
- [ ] `cost_estimate` - Tìm giá Dihydroergotamine, Migranal

**Nguồn tìm kiếm**:
- Web: "Dihydroergotamine Migranal giá"
- FDA Label: Migranal (Dihydroergotamine)
- Web: "Dihydroergotamine pediatric dosing"

#### 13. Zolpidem/Melatonin
- [ ] `brand_names` - Tìm: Các sản phẩm kết hợp
- [ ] `pediatric_dosing` - CHỐNG CHỈ ĐỊNH <18 tuổi
- [ ] `geriatric_dosing` - Giảm liều zolpidem 5mg
- [ ] `cost_estimate` - Tìm giá sản phẩm kết hợp

**Nguồn tìm kiếm**:
- Web: "Zolpidem Melatonin combination giá"
- Web: "Zolpidem pediatric dosing"

#### 14. Betahistine/Piracetam
- [ ] `brand_names` - Tìm: Các sản phẩm kết hợp
- [ ] `pediatric_dosing` - Thận trọng, giảm liều piracetam
- [ ] `geriatric_dosing` - Thận trọng, giảm liều piracetam
- [ ] `cost_estimate` - Tìm giá sản phẩm kết hợp

**Nguồn tìm kiếm**:
- Web: "Betahistine Piracetam combination giá"
- Web: "Piracetam pediatric dosing"

#### 15. Sumatriptan/Metoclopramide
- [ ] `brand_names` - Tìm: Các sản phẩm kết hợp hoặc dùng riêng
- [ ] `pediatric_dosing` - Thường không khuyến cáo <18 tuổi
- [ ] `geriatric_dosing` - Thận trọng, liều tương tự
- [ ] `cost_estimate` - Tìm giá Sumatriptan + Metoclopramide

**Nguồn tìm kiếm**:
- Web: "Sumatriptan Metoclopramide combination giá"
- Web: "Sumatriptan pediatric dosing"

---

### PHASE 4: ANTIPSYCHOTICS - MỚI (4 thuốc)

#### 16. Brexpiprazole
- [ ] `storage` - Nhiệt độ phòng, tránh ẩm
- [ ] `pediatric_dosing` - Có thể dùng cho trẻ em (cần tìm liều cụ thể)
- [ ] `geriatric_dosing` - Thận trọng, liều tương tự
- [ ] `cost_estimate` - Tìm giá Rexulti, Brexpiprazole

**Nguồn tìm kiếm**:
- Web: "Brexpiprazole Rexulti giá"
- FDA Label: Rexulti (Brexpiprazole)
- Web: "Brexpiprazole pediatric dosing"
- Web: "Brexpiprazole storage conditions"

#### 17. Cariprazine
- [ ] `storage` - Nhiệt độ phòng, tránh ẩm
- [ ] `pediatric_dosing` - Thường không khuyến cáo <18 tuổi
- [ ] `geriatric_dosing` - Thận trọng, giảm liều
- [ ] `cost_estimate` - Tìm giá Vraylar, Cariprazine

**Nguồn tìm kiếm**:
- Web: "Cariprazine Vraylar giá"
- FDA Label: Vraylar (Cariprazine)
- Web: "Cariprazine pediatric dosing"
- Web: "Cariprazine storage conditions"

#### 18. Lumateperone
- [ ] `storage` - Nhiệt độ phòng, tránh ẩm
- [ ] `pediatric_dosing` - Thường không khuyến cáo <18 tuổi
- [ ] `geriatric_dosing` - Thận trọng, liều tương tự
- [ ] `cost_estimate` - Tìm giá Caplyta, Lumateperone

**Nguồn tìm kiếm**:
- Web: "Lumateperone Caplyta giá"
- FDA Label: Caplyta (Lumateperone)
- Web: "Lumateperone pediatric dosing"
- Web: "Lumateperone storage conditions"

#### 19. Pimavanserin
- [ ] `storage` - Nhiệt độ phòng, tránh ẩm
- [ ] `pediatric_dosing` - Thường không khuyến cáo <18 tuổi
- [ ] `geriatric_dosing` - Thận trọng, liều tương tự
- [ ] `cost_estimate` - Tìm giá Nuplazid, Pimavanserin

**Nguồn tìm kiếm**:
- Web: "Pimavanserin Nuplazid giá"
- FDA Label: Nuplazid (Pimavanserin)
- Web: "Pimavanserin pediatric dosing"
- Web: "Pimavanserin storage conditions"

---

### PHASE 5: CEREBRAL CIRCULATION - MỚI (3 thuốc)

#### 20. Cinnarizine
- [ ] `brand_names` - Tìm: Stugeron, Cinnarizine
- [ ] `pediatric_dosing` - Có thể dùng cho trẻ em (cần tìm liều cụ thể)
- [ ] `geriatric_dosing` - Thận trọng, tránh dùng kéo dài (nguy cơ parkinsonism)
- [ ] `cost_estimate` - Tìm giá Stugeron, Cinnarizine

**Nguồn tìm kiếm**:
- Web: "Cinnarizine Stugeron giá Việt Nam"
- Web: "Cinnarizine biệt dược"
- Web: "Cinnarizine pediatric dosing"
- Web: "Cinnarizine geriatric dosing"

#### 21. Flunarizine
- [ ] `brand_names` - Tìm: Sibelium, Flunarizine
- [ ] `pediatric_dosing` - Thường không khuyến cáo <18 tuổi
- [ ] `geriatric_dosing` - Thận trọng, tránh dùng kéo dài (nguy cơ parkinsonism)
- [ ] `cost_estimate` - Tìm giá Sibelium, Flunarizine

**Nguồn tìm kiếm**:
- Web: "Flunarizine Sibelium giá"
- Web: "Flunarizine biệt dược"
- Web: "Flunarizine pediatric dosing"
- Web: "Flunarizine geriatric dosing"

#### 22. Cilostazol
- [ ] `brand_names` - Tìm: Pletal, Cilostazol
- [ ] `pediatric_dosing` - Thường không khuyến cáo <18 tuổi
- [ ] `geriatric_dosing` - Thận trọng, liều tương tự
- [ ] `cost_estimate` - Tìm giá Pletal, Cilostazol

**Nguồn tìm kiếm**:
- Web: "Cilostazol Pletal giá"
- FDA Label: Pletal (Cilostazol)
- Web: "Cilostazol pediatric dosing"
- Web: "Cilostazol geriatric dosing"

---

## 📊 TEMPLATE ĐIỀN THÔNG TIN

### Template cho brand_names:
```python
"brand_names": {
    "common": ["Brand quốc tế 1", "Brand quốc tế 2"],
    "vietnam": ["Brand VN 1", "Brand VN 2", "Generic name"],
}
```

### Template cho pediatric_dosing:
```python
"pediatric_dosing": {
    "notes": "Không khuyến cáo cho trẻ em dưới X tuổi (dữ liệu hạn chế).",
    # HOẶC nếu có liều cụ thể:
    "children_X_Y": "Liều cụ thể",
    "adolescents_X_Y": "Liều cụ thể",
}
```

### Template cho geriatric_dosing:
```python
"geriatric_dosing": {
    "considerations": "Người cao tuổi nhạy cảm hơn với tác dụng phụ...",
    "dose_adjustment": "Bắt đầu liều thấp (Xmg) hoặc liều tương tự nhưng thận trọng hơn.",
    "monitoring": "Theo dõi sát tác dụng phụ...",
}
```

### Template cho cost_estimate:
```python
"cost_estimate": {
    "unit": "VND",
    "range": "X,000 - Y,000 VND/viên (tùy hàm lượng và thương hiệu)",
    "note": "Giá thay đổi theo thương hiệu và nhà thuốc. [Brand name] (brand) thường đắt hơn.",
}
```

### Template cho storage:
```python
"storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
```

---

## 🎯 THỨ TỰ ƯU TIÊN

### Ưu tiên cao (thuốc phổ biến):
1. ✅ Zolpidem (Stilnox) - Rất phổ biến
2. ✅ Betahistine (Serc) - Phổ biến ở VN
3. ✅ Dimenhydrinate (Dramamine) - Phổ biến
4. ✅ Sumatriptan/Naproxen (Treximet) - Phổ biến
5. ✅ Brexpiprazole, Cariprazine - Thuốc mới quan trọng

### Ưu tiên trung bình:
6. ✅ Các thuốc sleep còn lại
7. ✅ Các thuốc vestibular còn lại
8. ✅ Các thuốc combination còn lại

### Ưu tiên thấp:
9. ✅ Các thuốc cerebral circulation mới
10. ✅ Lumateperone, Pimavanserin (ít phổ biến hơn)

---

## 📝 CHECKLIST TIẾN ĐỘ

### Phase 1: Sleep Medications (5 thuốc)
- [ ] Zolpidem
- [ ] Zaleplon
- [ ] Eszopiclone
- [ ] Ramelteon
- [ ] Suvorexant

### Phase 2: Vestibular Drugs (3 thuốc)
- [ ] Betahistine
- [ ] Dimenhydrinate
- [ ] Meclizine

### Phase 3: Neurological Combinations (7 thuốc)
- [ ] Sumatriptan/Naproxen
- [ ] Diphenhydramine/Melatonin
- [ ] Betahistine/Cinnarizine
- [ ] Dihydroergotamine/Metoclopramide
- [ ] Zolpidem/Melatonin
- [ ] Betahistine/Piracetam
- [ ] Sumatriptan/Metoclopramide

### Phase 4: Antipsychotics (4 thuốc)
- [ ] Brexpiprazole
- [ ] Cariprazine
- [ ] Lumateperone
- [ ] Pimavanserin

### Phase 5: Cerebral Circulation (3 thuốc)
- [ ] Cinnarizine
- [ ] Flunarizine
- [ ] Cilostazol

**Tổng cộng: 22 thuốc**

---

## 🔍 CHIẾN LƯỢC TÌM KIẾM

### Bước 1: Tìm brand_names
1. Web search: "[Tên thuốc] brand names"
2. Web search: "[Tên thuốc] biệt dược Việt Nam"
3. Kiểm tra các trang nhà thuốc VN
4. FDA Drug Labels cho brand quốc tế

### Bước 2: Tìm pediatric_dosing
1. Web search: "[Tên thuốc] pediatric dosing"
2. UpToDate (nếu có)
3. FDA Drug Labels - Pediatric section
4. Nếu không có: Ghi "Không khuyến cáo cho trẻ em dưới X tuổi (dữ liệu hạn chế)"

### Bước 3: Tìm geriatric_dosing
1. Web search: "[Tên thuốc] geriatric dosing elderly"
2. UpToDate (nếu có)
3. FDA Drug Labels - Geriatric section
4. Beers Criteria (nếu có)
5. Thường: "Thận trọng, giảm liều hoặc liều tương tự"

### Bước 4: Tìm cost_estimate
1. Web search: "[Tên thuốc] giá Việt Nam"
2. Web search: "[Tên thuốc] giá nhà thuốc"
3. Kiểm tra các trang nhà thuốc VN
4. Lưu ý: Chỉ ước tính khoảng, giá có thể thay đổi

### Bước 5: Tìm storage (nếu cần)
1. FDA Drug Labels - Storage section
2. Web search: "[Tên thuốc] storage conditions"
3. Thường: "Nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng"

---

## ✅ KẾT QUẢ MONG ĐỢI

Sau khi hoàn thành:
- ✅ Tất cả 22 thuốc mới có đầy đủ 4-5 field
- ✅ Thông tin chính xác, có nguồn tham khảo
- ✅ Format đúng theo template
- ✅ File Python không có lỗi syntax

---

**Ngày tạo kế hoạch**: 2025-02-18
**Dự kiến hoàn thành**: Theo từng phase
**Tổng số thuốc**: 22 thuốc
**Tổng số field cần bổ sung**: ~88-90 field
