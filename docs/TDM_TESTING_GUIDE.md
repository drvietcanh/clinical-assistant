# 🧪 HƯỚNG DẪN TEST TDM INTEGRATION

**Ngày:** 2025-02-03  
**Mục đích:** Hướng dẫn test tích hợp TDM vào Drug Database

---

## ✅ TEST CASES

### **Test Case 1: Digoxin - Có TDM trong DB**

**Steps:**
1. Vào module "💊 Drug Database"
2. Search "Digoxin"
3. Click "Xem chi tiết"
4. Scroll xuống đến section "📊 Theo Dõi Nồng Độ Thuốc (TDM)"

**Expected Results:**
- ✅ TDM section hiển thị
- ✅ Thông tin hiển thị:
  - Khoảng điều trị: 0.5-0.9 ng/mL (HF), 0.5-1.0 ng/mL (AF)
  - Thời điểm lấy mẫu: Trough (≥ 6-8 hours post-dose)
  - Half-life: 36 giờ
  - Đơn vị: ng/mL
- ✅ Button "📊 Mở TDM Calculator" hiển thị

**Test Navigation:**
5. Click "📊 Mở TDM Calculator"
6. Verify chuyển đến module "📊 TDM"
7. Verify "💚 TDM - Digoxin (Tim Mạch)" được chọn trong dropdown
8. Verify notification "✅ Đã chọn: **Digoxin** từ Drug Database"

---

### **Test Case 2: Phenytoin - Có TDM trong DB**

**Steps:**
1. Vào module "💊 Drug Database"
2. Search "Phenytoin"
3. Click "Xem chi tiết"
4. Scroll xuống đến section "📊 Theo Dõi Nồng Độ Thuốc (TDM)"

**Expected Results:**
- ✅ TDM section hiển thị
- ✅ Thông tin hiển thị:
  - Khoảng điều trị: 10-20 mg/L (total), 1-2 mg/L (free)
  - Thời điểm lấy mẫu: Trough (pre-dose)
  - Half-life: 22 giờ
  - Đơn vị: mg/L
- ✅ Button "📊 Mở TDM Calculator" hiển thị

**Test Navigation:**
5. Click "📊 Mở TDM Calculator"
6. Verify chuyển đến module "📊 TDM"
7. Verify "🧠 TDM - Phenytoin (Thần Kinh)" được chọn trong dropdown

---

### **Test Case 3: Carbamazepine - Có TDM trong DB**

**Steps:**
1. Vào module "💊 Drug Database"
2. Search "Carbamazepine"
3. Click "Xem chi tiết"
4. Scroll xuống đến section "📊 Theo Dõi Nồng Độ Thuốc (TDM)"

**Expected Results:**
- ✅ TDM section hiển thị
- ✅ Thông tin hiển thị:
  - Khoảng điều trị: 4-12 mg/L
  - Thời điểm lấy mẫu: Trough (pre-dose)
  - Half-life: 12 giờ
  - Đơn vị: mg/L
- ✅ Button "📊 Mở TDM Calculator" hiển thị

---

### **Test Case 4: Valproate - Có TDM trong DB**

**Steps:**
1. Vào module "💊 Drug Database"
2. Search "Valproate" hoặc "Valproic Acid"
3. Click "Xem chi tiết"
4. Scroll xuống đến section "📊 Theo Dõi Nồng Độ Thuốc (TDM)"

**Expected Results:**
- ✅ TDM section hiển thị
- ✅ Thông tin hiển thị:
  - Khoảng điều trị: 50-100 mg/L
  - Thời điểm lấy mẫu: Trough (pre-dose)
  - Half-life: 12 giờ
  - Đơn vị: mg/L
- ✅ Button "📊 Mở TDM Calculator" hiển thị

---

### **Test Case 5: Metformin - Không có TDM**

**Steps:**
1. Vào module "💊 Drug Database"
2. Search "Metformin"
3. Click "Xem chi tiết"
4. Scroll xuống xem tất cả sections

**Expected Results:**
- ✅ KHÔNG thấy section "📊 Theo Dõi Nồng Độ Thuốc (TDM)"
- ✅ Chỉ thấy các sections thông thường (Monitoring, Precautions, etc.)

---

### **Test Case 6: Omeprazole - Không có TDM**

**Steps:**
1. Vào module "💊 Drug Database"
2. Search "Omeprazole"
3. Click "Xem chi tiết"
4. Scroll xuống xem tất cả sections

**Expected Results:**
- ✅ KHÔNG thấy section "📊 Theo Dõi Nồng Độ Thuốc (TDM)"

---

## 🔍 EDGE CASES

### **Test Case 7: Tên thuốc có biến thể**

**Steps:**
1. Search "Valproic Acid" (thay vì "Valproate")
2. Verify TDM section vẫn hiển thị

**Expected Results:**
- ✅ TDM mapping function xử lý được biến thể tên
- ✅ TDM section hiển thị đúng

---

### **Test Case 8: Thuốc có trong TDM config nhưng chưa có trong DB**

**Steps:**
1. Search "Lithium" hoặc "Theophylline"
2. Verify behavior

**Expected Results:**
- ⚠️ Nếu thuốc không có trong DB → Không thể test
- ⚠️ Nếu thuốc có trong DB nhưng chưa có TDM section → Cần thêm vào DB

---

## 📊 VERIFICATION CHECKLIST

### **Functional Testing:**
- [ ] TDM section hiển thị cho thuốc có TDM
- [ ] TDM section KHÔNG hiển thị cho thuốc không có TDM
- [ ] Thông tin TDM hiển thị đúng (therapeutic range, sampling time, half-life, unit)
- [ ] Button "Mở TDM Calculator" hoạt động
- [ ] Navigation từ Drug Detail → TDM module hoạt động
- [ ] Preset drug trong TDM module hoạt động
- [ ] Notification hiển thị khi preset được sử dụng

### **UI/UX Testing:**
- [ ] TDM section có layout đẹp
- [ ] Info box hiển thị rõ ràng
- [ ] Button có style phù hợp (primary)
- [ ] Caption hướng dẫn rõ ràng
- [ ] Visual hierarchy hợp lý

### **Error Handling:**
- [ ] Không crash khi TDM mapping fail
- [ ] Graceful degradation khi không tìm thấy TDM info
- [ ] Error messages (nếu có) rõ ràng

---

## 🐛 KNOWN ISSUES / TODO

### **Thuốc chưa có trong DB:**
- [ ] Lithium - Cần thêm vào DB
- [ ] Theophylline - Cần thêm vào DB
- [ ] Tacrolimus/Cyclosporine - Cần kiểm tra và thêm nếu chưa có
- [ ] Vancomycin - Cần kiểm tra và thêm nếu chưa có
- [ ] Aminoglycosides - Cần kiểm tra và thêm nếu chưa có

### **Enhancements:**
- [ ] Thêm TDM info cho các thuốc còn thiếu
- [ ] Improve error messages
- [ ] Add visual indicators (color coding)
- [ ] Add tooltips

---

## 📝 TEST RESULTS TEMPLATE

```
Test Date: ___________
Tester: ___________

Test Case 1: Digoxin
- [ ] Pass
- [ ] Fail
- Notes: ___________

Test Case 2: Phenytoin
- [ ] Pass
- [ ] Fail
- Notes: ___________

Test Case 3: Carbamazepine
- [ ] Pass
- [ ] Fail
- Notes: ___________

Test Case 4: Valproate
- [ ] Pass
- [ ] Fail
- Notes: ___________

Test Case 5: Metformin (No TDM)
- [ ] Pass
- [ ] Fail
- Notes: ___________

Test Case 6: Omeprazole (No TDM)
- [ ] Pass
- [ ] Fail
- Notes: ___________

Overall Status: [ ] All Pass | [ ] Some Fail | [ ] All Fail
```

---

**Người tạo:** AI Code Assistant  
**Ngày:** 2025-02-03

