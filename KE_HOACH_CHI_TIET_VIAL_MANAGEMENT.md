# 📋 KẾ HOẠCH CHI TIẾT: VIAL MANAGEMENT SYSTEM
## Phase 1: Triển khai từng bước với kiểm tra và so sánh

**Ngày bắt đầu:** 2025-02-05  
**Mục tiêu:** Bổ sung hệ thống quản lý ống thuốc (vials) với kiểm tra kỹ lưỡng  
**Ưu tiên:** ⭐⭐⭐ Cao

---

## 🎯 TỔNG QUAN

### Mục tiêu
- Tạo hệ thống quản lý ống thuốc (vials) chi tiết
- Tự động tính số lượng ống cần dùng
- Hỗ trợ nhiều loại ống khác nhau
- Tính toán chính xác, tránh sai sót

### Phạm vi
- Vial database (JSON)
- Vial selection UI
- Quantity calculator
- Integration vào Drug Database và Critical Care

---

## 📚 NGHIÊN CỨU VÀ SO SÁNH

### 1. Công thức tính toán cần kiểm tra

#### 1.1. Tính số lượng ống cần dùng
```
Số lượng ống = CEIL(Tổng liều cần / Liều mỗi ống)
```

**Ví dụ:**
- Tổng liều: 150 mg
- Ống có: 100 mg
- Số lượng: CEIL(150/100) = 2 ống

**Nguồn tham khảo:**
- Medical Calculator (tkinter app)
- MDCalc (nếu có)
- HSCC.vn
- UpToDate drug dosing

#### 1.2. Tính lượng thuốc thừa (waste)
```
Lượng thừa = (Số lượng ống × Liều mỗi ống) - Tổng liều cần
```

**Ví dụ:**
- Số lượng ống: 2
- Liều mỗi ống: 100 mg
- Tổng liều cần: 150 mg
- Lượng thừa: (2 × 100) - 150 = 50 mg

#### 1.3. Tính nồng độ pha
```
Nồng độ (mg/ml) = Tổng liều (mg) / Thể tích pha (ml)
```

**Ví dụ:**
- Tổng liều: 150 mg
- Thể tích pha: 50 ml
- Nồng độ: 150 / 50 = 3 mg/ml

---

### 2. So sánh với các app khác

#### Medical Calculator (tkinter)
- ✅ Có vial management
- ✅ Tính số lượng ống
- ✅ Hỗ trợ nhiều loại ống
- ⚠️ Chưa có tính waste

#### MDCalc
- ⚠️ Không có vial management riêng
- ✅ Có tính liều thuốc
- ✅ Có unit conversion

#### HSCC.vn
- ✅ Có tính liều thuốc
- ⚠️ Chưa rõ có vial management

---

## 📝 KẾ HOẠCH CHI TIẾT TỪNG BƯỚC

### BƯỚC 1: Nghiên cứu và thiết kế (Ngày 1-2)

#### Task 1.1: Nghiên cứu cấu trúc dữ liệu
- [ ] Đọc code Medical Calculator về vial management
- [ ] Nghiên cứu cấu trúc JSON hiện tại (antibiotics_data.json)
- [ ] Thiết kế cấu trúc vial database
- [ ] So sánh với các nguồn uy tín (UpToDate, MIMS)

**Deliverable:**
- Document: `docs/vial_database_design.md`
- Schema: Vial database structure

**Checklist kiểm tra:**
- [ ] Cấu trúc dữ liệu đầy đủ (size, volume, concentration)
- [ ] Hỗ trợ nhiều loại ống cho 1 thuốc
- [ ] Dễ mở rộng và cập nhật

---

#### Task 1.2: Thiết kế UI/UX
- [ ] Thiết kế giao diện chọn ống
- [ ] Thiết kế hiển thị kết quả
- [ ] Thiết kế tích hợp vào Drug Database
- [ ] Thiết kế tích hợp vào Critical Care

**Deliverable:**
- Mockup: UI design
- Document: `docs/vial_ui_design.md`

**Checklist kiểm tra:**
- [ ] UI rõ ràng, dễ sử dụng
- [ ] Hiển thị đầy đủ thông tin
- [ ] Responsive trên mobile

---

### BƯỚC 2: Tạo Vial Database (Ngày 3-4)

#### Task 2.1: Tạo cấu trúc dữ liệu
- [ ] Tạo file `drugs/vials_database.json`
- [ ] Định nghĩa schema cho mỗi thuốc
- [ ] Thêm 5-10 thuốc mẫu để test

**Cấu trúc đề xuất:**
```json
{
  "drug_name": {
    "name": "Adrenaline",
    "vials": [
      {
        "size": "1mg/1ml",
        "volume_ml": 1,
        "concentration_mg_ml": 1.0,
        "total_mg": 1.0,
        "common": true
      },
      {
        "size": "1mg/10ml",
        "volume_ml": 10,
        "concentration_mg_ml": 0.1,
        "total_mg": 1.0,
        "common": false
      }
    ],
    "default_vial": "1mg/1ml",
    "solvent": "NaCl 0.9%",
    "notes": "..."
  }
}
```

**Checklist kiểm tra:**
- [ ] JSON hợp lệ (validate với JSON schema)
- [ ] Dữ liệu chính xác (so sánh với MIMS, UpToDate)
- [ ] Đầy đủ thông tin cần thiết
- [ ] Dễ đọc và maintain

**Validation:**
- [ ] Test với JSON validator
- [ ] So sánh với nguồn uy tín
- [ ] Review bởi dược sĩ/bác sĩ (nếu có)

---

#### Task 2.2: Thêm thuốc tim mạch vào database
- [ ] Adrenaline (Epinephrine)
- [ ] Noradrenaline (Norepinephrine)
- [ ] Dopamine
- [ ] Dobutamine
- [ ] Vasopressin
- [ ] Milrinone
- [ ] Nitroglycerin

**Checklist kiểm tra:**
- [ ] Mỗi thuốc có ít nhất 2 loại ống
- [ ] Thông tin ống chính xác (so với MIMS)
- [ ] Ghi chú rõ ràng về cách pha

**Nguồn tham khảo:**
- MIMS Vietnam
- UpToDate
- Surviving Sepsis Guidelines
- Medical Calculator (tkinter)

---

### BƯỚC 3: Implement Core Functions (Ngày 5-7)

#### Task 3.1: Tạo module `drugs/vial_manager.py`

**Functions cần implement:**

```python
def load_vial_database() -> dict:
    """Load vial database from JSON"""
    # TODO: Implement
    pass

def get_drug_vials(drug_name: str) -> list:
    """Get list of vials for a drug"""
    # TODO: Implement
    pass

def calculate_vials_needed(drug_name: str, total_dose_mg: float, 
                          selected_vial: str = None) -> dict:
    """
    Calculate number of vials needed
    
    Returns:
        {
            "vials_needed": int,
            "total_available_mg": float,
            "waste_mg": float,
            "waste_percent": float,
            "selected_vial": str
        }
    """
    # TODO: Implement
    pass

def calculate_preparation(drug_name: str, total_dose_mg: float,
                         selected_vial: str, final_volume_ml: float) -> dict:
    """
    Calculate preparation details
    
    Returns:
        {
            "vials_needed": int,
            "total_available_mg": float,
            "final_concentration_mg_ml": float,
            "waste_mg": float,
            "preparation_instructions": str
        }
    """
    # TODO: Implement
    pass
```

**Checklist kiểm tra:**
- [ ] Functions có docstring đầy đủ
- [ ] Type hints cho tất cả parameters
- [ ] Error handling (drug not found, invalid dose, etc.)
- [ ] Unit tests cho mỗi function

**Test cases:**
```python
# Test 1: Normal case
assert calculate_vials_needed("Adrenaline", 150, "1mg/1ml") == {
    "vials_needed": 150,
    "total_available_mg": 150,
    "waste_mg": 0,
    "waste_percent": 0
}

# Test 2: Need multiple vials
assert calculate_vials_needed("Adrenaline", 150, "1mg/1ml") == {
    "vials_needed": 150,  # 150 vials of 1mg each
    "total_available_mg": 150,
    "waste_mg": 0
}

# Test 3: Waste calculation
assert calculate_vials_needed("Adrenaline", 150, "100mg/10ml") == {
    "vials_needed": 2,  # 2 vials of 100mg
    "total_available_mg": 200,
    "waste_mg": 50,
    "waste_percent": 25.0
}

# Test 4: Drug not found
assert calculate_vials_needed("Unknown", 100) == None

# Test 5: Invalid dose
assert calculate_vials_needed("Adrenaline", -10) == None
```

---

#### Task 3.2: Validation và Error Handling

**Validation rules:**
- [ ] Tổng liều > 0
- [ ] Tên thuốc có trong database
- [ ] Loại ống được chọn có trong danh sách
- [ ] Thể tích pha > 0 và hợp lý

**Error messages:**
- [ ] Thông báo lỗi rõ ràng, dễ hiểu
- [ ] Hướng dẫn cách sửa lỗi
- [ ] Hiển thị bằng tiếng Việt

**Checklist kiểm tra:**
- [ ] Tất cả edge cases được xử lý
- [ ] Error messages user-friendly
- [ ] Logging cho debugging

---

### BƯỚC 4: So sánh và kiểm tra công thức (Ngày 8)

#### Task 4.1: So sánh với Medical Calculator

**Test cases so sánh:**
- [ ] Adrenaline: 0.1 mcg/kg/min, 70kg → Tính số ống
- [ ] Noradrenaline: 0.1 mcg/kg/min, 70kg → Tính số ống
- [ ] Dopamine: 5 mcg/kg/min, 70kg → Tính số ống

**Công thức cần verify:**
```python
# Formula 1: Calculate total dose from mcg/kg/min
total_dose_mcg = dose_mcg_per_kg_min * weight_kg * duration_minutes
total_dose_mg = total_dose_mcg / 1000

# Formula 2: Calculate vials needed
vials_needed = math.ceil(total_dose_mg / vial_size_mg)

# Formula 3: Calculate waste
waste_mg = (vials_needed * vial_size_mg) - total_dose_mg
waste_percent = (waste_mg / (vials_needed * vial_size_mg)) * 100
```

**Checklist kiểm tra:**
- [ ] Kết quả khớp với Medical Calculator
- [ ] Kết quả khớp với tính tay
- [ ] Edge cases được xử lý đúng

---

#### Task 4.2: So sánh với MDCalc và HSCC

**Nếu có tính năng tương tự:**
- [ ] So sánh kết quả tính toán
- [ ] So sánh cách hiển thị
- [ ] Ghi nhận điểm khác biệt

**Nếu không có:**
- [ ] Ghi chú: "MDCalc/HSCC không có tính năng này"
- [ ] Tham khảo cách tính liều của họ

---

#### Task 4.3: Verify với nguồn uy tín

**Nguồn tham khảo:**
- [ ] UpToDate - Drug dosing
- [ ] MIMS Vietnam - Vial sizes
- [ ] Surviving Sepsis Guidelines
- [ ] ACCM Guidelines

**Checklist:**
- [ ] Kích thước ống khớp với MIMS
- [ ] Cách pha khớp với hướng dẫn
- [ ] Liều dùng khớp với guidelines

---

### BƯỚC 5: Tạo UI Component (Ngày 9-10)

#### Task 5.1: Tạo Streamlit component

**File:** `components/vial_selector.py`

**Functions:**
```python
def render_vial_selector(drug_name: str, total_dose_mg: float) -> dict:
    """
    Render vial selection UI
    
    Returns:
        {
            "selected_vial": str,
            "vials_needed": int,
            "waste_mg": float,
            "preparation_instructions": str
        }
    """
    # TODO: Implement
    pass

def render_vial_results(calculation_results: dict):
    """Render calculation results"""
    # TODO: Implement
    pass
```

**UI Elements:**
- [ ] Dropdown chọn thuốc
- [ ] Input tổng liều
- [ ] Dropdown chọn loại ống
- [ ] Hiển thị kết quả (số ống, waste, hướng dẫn pha)
- [ ] Warning nếu waste > 20%

**Checklist kiểm tra:**
- [ ] UI rõ ràng, dễ sử dụng
- [ ] Responsive trên mobile
- [ ] Error handling tốt
- [ ] Loading states

---

#### Task 5.2: Tích hợp vào Drug Database

**File:** `pages/07_💊_Drug_Database.py`

**Integration:**
- [ ] Thêm tab "Vial Management"
- [ ] Hiển thị khi chọn thuốc có trong vial database
- [ ] Tự động tính khi nhập liều

**Checklist:**
- [ ] Tích hợp mượt mà
- [ ] Không ảnh hưởng tính năng hiện có
- [ ] UI nhất quán

---

#### Task 5.3: Tích hợp vào Critical Care

**File:** `pages/09_🫁_Critical_Care.py`

**Integration:**
- [ ] Thêm vào Vasopressor calculator
- [ ] Hiển thị vial info khi tính liều
- [ ] Link đến vial management

**Checklist:**
- [ ] Tích hợp tự nhiên
- [ ] Thông tin hữu ích
- [ ] Không làm rối UI

---

### BƯỚC 6: Testing và Validation (Ngày 11-12)

#### Task 6.1: Unit Tests

**File:** `tests/test_vial_manager.py`

**Test cases:**
- [ ] Test load database
- [ ] Test get drug vials
- [ ] Test calculate vials needed (normal cases)
- [ ] Test calculate vials needed (edge cases)
- [ ] Test calculate preparation
- [ ] Test error handling

**Coverage target:** > 90%

---

#### Task 6.2: Integration Tests

**Test cases:**
- [ ] Test UI component với các thuốc khác nhau
- [ ] Test tích hợp vào Drug Database
- [ ] Test tích hợp vào Critical Care
- [ ] Test với các liều khác nhau

---

#### Task 6.3: Manual Testing

**Test scenarios:**
1. **Scenario 1: Adrenaline**
   - Liều: 0.1 mcg/kg/min
   - Cân nặng: 70 kg
   - Thời gian: 24 giờ
   - Expected: Tính đúng số ống, waste

2. **Scenario 2: Noradrenaline**
   - Liều: 0.1 mcg/kg/min
   - Cân nặng: 70 kg
   - Thời gian: 24 giờ
   - Expected: Tính đúng số ống, waste

3. **Scenario 3: Edge cases**
   - Liều = 0 → Error
   - Liều rất lớn → Tính đúng
   - Thuốc không có trong DB → Error message rõ ràng

**Checklist:**
- [ ] Tất cả scenarios pass
- [ ] UI hoạt động mượt
- [ ] Kết quả chính xác
- [ ] Error handling tốt

---

#### Task 6.4: So sánh kết quả cuối cùng

**So sánh với:**
- [ ] Medical Calculator (tkinter)
- [ ] Tính tay
- [ ] MIMS Vietnam
- [ ] UpToDate

**Tolerance:**
- Số ống: Phải khớp 100%
- Waste: Cho phép sai số < 1% (do rounding)

---

### BƯỚC 7: Documentation và Cleanup (Ngày 13)

#### Task 7.1: Documentation

**Files:**
- [ ] `docs/vial_management_guide.md` - User guide
- [ ] `docs/vial_management_api.md` - API documentation
- [ ] Update `README.md`

**Content:**
- [ ] Hướng dẫn sử dụng
- [ ] Ví dụ tính toán
- [ ] FAQ
- [ ] Troubleshooting

---

#### Task 7.2: Code Review và Cleanup

**Checklist:**
- [ ] Code style consistent
- [ ] Comments đầy đủ
- [ ] Remove debug code
- [ ] Optimize performance
- [ ] Security check

---

## ✅ CHECKLIST TỔNG HỢP

### Trước khi bắt đầu
- [ ] Đã nghiên cứu Medical Calculator
- [ ] Đã so sánh với MDCalc, HSCC
- [ ] Đã thiết kế cấu trúc dữ liệu
- [ ] Đã thiết kế UI/UX

### Trong quá trình phát triển
- [ ] Mỗi function có unit test
- [ ] Mỗi bước có validation
- [ ] So sánh kết quả với nguồn uy tín
- [ ] Code review thường xuyên

### Trước khi release
- [ ] Tất cả tests pass
- [ ] Manual testing hoàn tất
- [ ] So sánh với Medical Calculator khớp
- [ ] Documentation đầy đủ
- [ ] Code cleanup hoàn tất

---

## 📊 METRICS VÀ KPI

### Success Criteria
- [ ] Vial management hoạt động cho ít nhất 7 thuốc tim mạch
- [ ] Tính toán chính xác 100% (so với Medical Calculator)
- [ ] UI/UX tốt, dễ sử dụng
- [ ] Tích hợp mượt vào app hiện tại
- [ ] Documentation đầy đủ

### Performance
- [ ] Load database < 100ms
- [ ] Calculate vials < 10ms
- [ ] UI render < 200ms

---

## 🚨 RISK MANAGEMENT

### Risks
1. **Công thức tính sai**
   - Mitigation: So sánh với nhiều nguồn, test kỹ
   
2. **Dữ liệu ống không chính xác**
   - Mitigation: Verify với MIMS, UpToDate
   
3. **UI phức tạp**
   - Mitigation: User testing sớm, iterate

4. **Tích hợp làm hỏng tính năng cũ**
   - Mitigation: Test integration kỹ, có rollback plan

---

## 📅 TIMELINE

| Bước | Ngày | Trạng thái |
|------|------|------------|
| Bước 1: Nghiên cứu | 1-2 | ⏳ Pending |
| Bước 2: Database | 3-4 | ⏳ Pending |
| Bước 3: Core Functions | 5-7 | ⏳ Pending |
| Bước 4: So sánh | 8 | ⏳ Pending |
| Bước 5: UI | 9-10 | ⏳ Pending |
| Bước 6: Testing | 11-12 | ⏳ Pending |
| Bước 7: Documentation | 13 | ⏳ Pending |

**Tổng thời gian:** 13 ngày (2.5 tuần)

---

## 📝 NOTES

- Luôn so sánh kết quả với Medical Calculator
- Verify dữ liệu với nguồn uy tín
- Test kỹ trước khi commit
- Document mọi thay đổi

---

*© 2025 - Kế hoạch chi tiết Vial Management System*

