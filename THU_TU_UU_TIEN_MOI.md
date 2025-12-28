# 🔄 CẬP NHẬT THỨ TỰ ƯU TIÊN MỚI

**Ngày cập nhật:** 2025-02-05  
**Thứ tự mới:** 2 → 3 → 1 → 4

---

## 📋 THỨ TỰ MỚI

### 1. Phase 2: Cardiovascular Drugs Calculator ⭐⭐⭐
**Ưu tiên:** CAO NHẤT - Bắt đầu đầu tiên

**Lý do:**
- Tính năng quan trọng nhất, được yêu cầu nhiều
- Có thể làm độc lập với Vial Management (hardcode vial info tạm thời)
- Tích hợp Vial Management đầy đủ sau khi Phase 1 hoàn thành

**Thời gian:** 12 ngày

---

### 2. Phase 3: Enhanced Infusion Calculator ⭐⭐
**Ưu tiên:** CAO - Làm tiếp theo

**Lý do:**
- Bổ sung tính năng quan trọng (giọt/phút, thời gian truyền)
- Có thể làm song song hoặc ngay sau Phase 2
- Độc lập với các phase khác

**Thời gian:** 10 ngày

---

### 3. Phase 1: Vial Management System ⭐⭐⭐
**Ưu tiên:** TRUNG BÌNH - Làm sau Phase 2, 3

**Lý do:**
- Quan trọng nhưng có thể làm sau
- Phase 2 đã có thể hoạt động với vial info hardcode
- Sẽ tích hợp đầy đủ vào Phase 2 sau khi hoàn thành

**Thời gian:** 13 ngày

---

### 4. Phase 4: Unit Conversion Enhancement ⭐⭐
**Ưu tiên:** THẤP - Làm cuối cùng

**Lý do:**
- Tính năng bổ sung, không cấp thiết
- Có thể làm sau khi các tính năng chính hoàn thành

**Thời gian:** 7 ngày

---

## 🔄 ĐIỀU CHỈNH CẦN THIẾT

### Phase 2: Cardiovascular Drugs

**Thay đổi:**
- Có thể hardcode vial information tạm thời
- Tạo database cardiovascular drugs đầy đủ
- Implement tính liều và tốc độ truyền
- Vial Management sẽ tích hợp sau (Phase 1)

**Ví dụ hardcode tạm thời:**
```python
# Tạm thời hardcode trong Phase 2
ADRENALINE_VIALS = [
    {"size": "1mg/1ml", "volume_ml": 1, "concentration_mg_ml": 1.0}
]

# Sau khi Phase 1 hoàn thành, sẽ load từ vial database
```

---

## 📅 TIMELINE MỚI

```
Tuần 1-2:   Phase 2 - Cardiovascular Drugs Calculator
Tuần 3:     Phase 3 - Enhanced Infusion Calculator  
Tuần 4-5:   Phase 1 - Vial Management System (tích hợp vào Phase 2)
Tuần 6:     Phase 4 - Unit Conversion Enhancement
```

**Tổng:** ~6 tuần (42 ngày)

---

## ✅ CHECKLIST BẮT ĐẦU

### Trước khi bắt đầu Phase 2:
- [x] Đã cập nhật thứ tự ưu tiên
- [ ] Đọc KE_HOACH_CHI_TIET_CARDIOVASCULAR_DRUGS.md
- [ ] Đọc SO_SANH_CONG_THUC_TINH_TOAN.md
- [ ] Nghiên cứu vasopressor guide hiện có
- [ ] Nghiên cứu DIRC calculator hiện có
- [ ] So sánh với Medical Calculator

---

## 📝 LƯU Ý

1. **Phase 2 có thể làm độc lập:**
   - Hardcode vial info tạm thời
   - Tập trung vào tính liều và tốc độ truyền
   - Vial Management sẽ tích hợp sau

2. **Tích hợp Phase 1 vào Phase 2:**
   - Sau khi Phase 1 hoàn thành
   - Thay thế hardcode bằng Vial Management System
   - Test lại toàn bộ

3. **Phase 3 độc lập:**
   - Có thể làm song song hoặc sau Phase 2
   - Không phụ thuộc vào Phase 1, 2

---

*© 2025 - Cập nhật thứ tự ưu tiên*

