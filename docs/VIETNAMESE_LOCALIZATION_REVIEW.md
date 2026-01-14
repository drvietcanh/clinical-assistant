# Báo cáo Kiểm tra Việt hóa và Thuật ngữ Y khoa

**Ngày tạo:** 2025-01-30  
**Phạm vi:** Toàn bộ ứng dụng Trợ lý Lâm sàng

## Tóm tắt

### Thống kê tổng quan
- **Số file đã kiểm tra:** 2,686 files
- **Tổng số chuỗi tiếng Việt:** 879,889 strings
- **Vấn đề phát hiện:**
  - Chuỗi hardcoded (nên dùng i18n): 203
  - Thiếu chú thích thuật ngữ: 115,282
  - Thuật ngữ không nhất quán: 19
  - Thuật ngữ y khoa cần thêm vào từ điển: 264,878

### Đánh giá tổng thể
✅ **Điểm mạnh:**
- Hệ thống có nhiều file dịch tập trung (`utils/i18n.py`, `antibiotics/vietnamese_terms.py`, `diagnosis/vietnamese_translations.py`)
- Thuật ngữ y khoa cơ bản đã được dịch chính xác
- Cấu trúc code cho phép mở rộng dễ dàng

⚠️ **Vấn đề cần cải thiện:**
- Nhiều chuỗi tiếng Việt vẫn hardcoded trong code thay vì dùng i18n
- Thiếu chú thích cho các viết tắt y khoa phổ biến
- Một số thuật ngữ không nhất quán giữa các module
- Cần bổ sung nhiều thuật ngữ vào từ điển

## Chi tiết các vấn đề

### 1. Chuỗi Hardcoded (Nên dùng i18n)

**Vấn đề:** Nhiều chuỗi tiếng Việt được hardcode trực tiếp trong code thay vì sử dụng hệ thống i18n.

**Ví dụ phát hiện:**
- `components/batch_calculator.py:166` - 'Bệnh nhân' → nên dùng `t('patient')`
- `components/breadcrumbs_enhanced.py:32` - 'Trang chủ' → nên dùng `t('home')`
- `components/calculator_enhancements.py:216` - 'Bệnh nhân' → nên dùng `t('patient')`
- `components/cds_alerts.py:155` - 'Chống chỉ định' → nên dùng `t('contraindication')`
- `components/drug_cards.py:131` - 'Chỉ định' → nên dùng `t('indication')`

**Đề xuất:**
1. Thay thế tất cả hardcoded strings bằng i18n keys
2. Sử dụng helper function `t()` từ `utils/i18n.py`
3. Tạo script tự động để tìm và thay thế

**Ưu tiên:** Cao

### 2. Thiếu Chú thích Thuật ngữ Y khoa

**Vấn đề:** Nhiều viết tắt y khoa được sử dụng mà không có chú thích giải thích.

**Ví dụ phát hiện:**
- `components/ai_assistant_logic.py:86` - 'BE' (Base Excess)
- `components/cardiovascular_calculator.py:30` - 'PE' (Thuyên tắc phổi)
- `components/cds_alerts.py:104` - 'MI' (Nhồi máu cơ tim)
- `components/cds_decision_trees.py:101` - 'SEPSIS' (Nhiễm trùng huyết)
- `components/cds_decision_trees.py:219` - 'NIHSS' (Thang điểm đột quỵ)

**Đề xuất:**
1. Sử dụng `utils/term_annotations.py` để tự động thêm chú thích
2. Áp dụng cho các viết tắt trong:
   - UI components
   - Calculator results
   - Protocol descriptions
   - Drug information displays

**Ưu tiên:** Trung bình-Cao

### 3. Thuật ngữ Không Nhất quán

**Vấn đề:** Một số thuật ngữ được sử dụng khác nhau ở các nơi khác nhau.

**Ví dụ:**
- 'ICU' vs 'Đơn vị hồi sức tích cực' vs 'Hồi sức'
- 'TDM' vs 'Theo dõi nồng độ thuốc'
- 'eGFR' vs 'Độ lọc cầu thận ước tính'

**Đề xuất:**
1. Sử dụng viết tắt chuẩn (ICU, TDM, eGFR) theo từ điển thuật ngữ
2. Thêm chú thích khi cần thiết
3. Cập nhật tất cả các file để nhất quán

**Ưu tiên:** Trung bình

### 4. Thuật ngữ Y khoa Cần Thêm vào Từ điển

**Vấn đề:** Nhiều thuật ngữ y khoa được sử dụng nhưng chưa có trong từ điển hoặc hệ thống chú thích.

**Đề xuất:**
1. Bổ sung vào `docs/medical_terms_glossary.md`
2. Thêm vào `utils/term_annotations.py` nếu cần chú thích
3. Ưu tiên các thuật ngữ xuất hiện nhiều nhất

**Ưu tiên:** Thấp-Trung bình

## Đánh giá theo Module

### 1. Components (`components/`)

#### Analytics (`components/analytics.py`)
**Trạng thái:** ⚠️ Cần cải thiện

**Vấn đề:**
- Sử dụng hardcoded strings: "Bảng điều khiển thống kê sử dụng", "Insights và thống kê"
- Thuật ngữ chuyên khoa đã đúng nhưng có thể rút gọn một số cụm từ

**Đề xuất:**
- "Bảng điều khiển thống kê sử dụng" → "Bảng điều khiển thống kê" (ngắn gọn hơn)
- "Insights và thống kê" → Giữ nguyên hoặc thêm chú thích cho "Insights"
- Sử dụng i18n keys thay vì hardcoded

**Ví dụ cải thiện:**
```python
# Trước
st.markdown("### 📊 Thống kê của bạn")

# Sau
from utils.i18n import t
st.markdown(f"### 📊 {t('statistics')}")
```

#### Navigation (`config/navigation_config.py`)
**Trạng thái:** ✅ Tốt

**Nhận xét:**
- Tên module nhất quán
- Icon và mô tả phù hợp
- Sử dụng tiếng Việt rõ ràng

**Đề xuất nhỏ:**
- Có thể thêm tooltip giải thích cho một số module phức tạp

### 2. Drugs Module (`drugs/`)

#### Vietnamese Terms (`antibiotics/vietnamese_terms.py`)
**Trạng thái:** ✅ Tốt, có thể cải thiện

**Điểm mạnh:**
- Có hệ thống mapping rõ ràng
- Thuật ngữ chính xác
- Tổ chức tốt theo enum

**Đề xuất cải thiện:**
1. **Thêm chú thích cho viết tắt:**
   ```python
   # Hiện tại
   "CAP": "Viêm phổi cộng đồng",
   
   # Đề xuất (sử dụng term_annotations)
   from utils.term_annotations import get_term_with_annotation
   "CAP": get_term_with_annotation("CAP", format_type='inline')
   # → "Viêm phổi cộng đồng (CAP: Community-Acquired Pneumonia)"
   ```

2. **Bổ sung thuật ngữ còn thiếu:**
   - Thêm các nhóm thuốc khác (không chỉ kháng sinh)
   - Thêm thuật ngữ về tương tác thuốc
   - Thêm thuật ngữ về điều chỉnh liều

**Ví dụ cải thiện:**
```python
# Thêm vào COMMON_TERMS_VI
"Drug Interaction": "Tương tác thuốc",
"Major Interaction": "Tương tác nghiêm trọng",
"Moderate Interaction": "Tương tác trung bình",
"Minor Interaction": "Tương tác nhẹ",
"Contraindicated": "Chống chỉ định",
"Use with Caution": "Thận trọng khi sử dụng",
```

### 3. Protocols (`protocols/`)

**Trạng thái:** ⚠️ Cần kiểm tra chi tiết

**Vấn đề:**
- Tên phác đồ có thể không nhất quán
- Thuật ngữ trong nội dung phác đồ cần được kiểm tra
- Một số viết tắt có thể thiếu chú thích

**Đề xuất:**
1. Tạo danh sách tên phác đồ chuẩn
2. Kiểm tra từng phác đồ để đảm bảo nhất quán
3. Thêm chú thích cho các viết tắt trong nội dung

**Ví dụ:**
- "STEMI" → "Nhồi máu cơ tim ST chênh lên (STEMI)"
- "NSTEMI" → "Nhồi máu cơ tim ST không chênh lên (NSTEMI)"

### 4. Diagnosis (`diagnosis/`)

**Trạng thái:** ✅ Tốt

**Nhận xét:**
- File `vietnamese_translations.py` tổ chức tốt
- Thuật ngữ triệu chứng và yếu tố nguy cơ chính xác
- Có hàm helper để dịch

**Đề xuất nhỏ:**
- Có thể thêm nhiều triệu chứng hơn nữa
- Bổ sung các thuật ngữ chẩn đoán phân biệt

## Kế hoạch Cải thiện

### Giai đoạn 1: Ưu tiên Cao (Tuần 1-2)
1. ✅ Tạo từ điển thuật ngữ y khoa (`docs/medical_terms_glossary.md`)
2. ✅ Tạo hệ thống chú thích (`utils/term_annotations.py`)
3. ✅ Mở rộng hệ thống i18n (`utils/i18n.py`)
4. ✅ Tạo script kiểm tra tự động (`scripts/check_vietnamese_localization.py`)
5. ⏳ Thay thế hardcoded strings bằng i18n keys (top 50)
6. ⏳ Thêm chú thích cho các viết tắt y khoa phổ biến nhất

### Giai đoạn 2: Ưu tiên Trung bình (Tuần 3-4)
1. ⏳ Rà soát và cập nhật tất cả components
2. ⏳ Cải thiện `antibiotics/vietnamese_terms.py` với chú thích
3. ⏳ Kiểm tra và chuẩn hóa tên phác đồ
4. ⏳ Bổ sung thuật ngữ còn thiếu vào từ điển

### Giai đoạn 3: Ưu tiên Thấp (Tuần 5+)
1. ⏳ Tối ưu hóa và làm sạch code
2. ⏳ Tạo documentation cho developers
3. ⏳ Thiết lập CI/CD checks cho việt hóa

## Checklist Cải thiện

### Thuật ngữ Y khoa
- [x] Tạo từ điển thuật ngữ y khoa
- [x] Tạo hệ thống chú thích tự động
- [ ] Kiểm tra tính chính xác của tất cả thuật ngữ
- [ ] Đảm bảo nhất quán trong toàn bộ ứng dụng
- [ ] Thêm chú thích cho các viết tắt quan trọng

### Hệ thống i18n
- [x] Mở rộng `utils/i18n.py` với các key mới
- [x] Nhóm keys theo module/chức năng
- [ ] Thay thế hardcoded strings bằng i18n keys
- [ ] Tạo helper functions để sử dụng dễ dàng
- [ ] Document cách sử dụng i18n system

### Components
- [ ] Analytics: Cải thiện việt hóa
- [ ] Navigation: Đã tốt, chỉ cần review nhỏ
- [ ] Search: Kiểm tra và cải thiện
- [ ] Calculators: Thêm chú thích cho các score
- [ ] Drug Cards: Sử dụng i18n keys

### Modules
- [ ] Drugs: Cải thiện `vietnamese_terms.py`
- [ ] Protocols: Chuẩn hóa tên và thuật ngữ
- [ ] Diagnosis: Bổ sung thuật ngữ
- [ ] Critical Care: Kiểm tra thuật ngữ chuyên môn

## Công cụ và Tài nguyên

### Scripts đã tạo
1. **`scripts/scan_vietnamese_text.py`**
   - Quét toàn bộ codebase để tìm chuỗi tiếng Việt
   - Phân loại theo loại (medical term, UI text, etc.)
   - Tạo báo cáo chi tiết

2. **`scripts/check_vietnamese_localization.py`**
   - Kiểm tra các vấn đề việt hóa
   - Phát hiện hardcoded strings
   - Tìm thiếu chú thích
   - Báo cáo thuật ngữ không nhất quán

### Files đã tạo
1. **`docs/medical_terms_glossary.md`**
   - Từ điển đầy đủ các thuật ngữ y khoa
   - Quy tắc dịch thuật
   - Ví dụ sử dụng đúng/sai

2. **`utils/term_annotations.py`**
   - Hệ thống chú thích tự động
   - Helper functions để thêm chú thích
   - Dictionary các thuật ngữ cần chú thích

3. **`utils/i18n.py`** (đã mở rộng)
   - Hệ thống i18n với nhiều keys hơn
   - Nhóm theo module
   - Hỗ trợ tiếng Việt và tiếng Anh

## Khuyến nghị

### Ngắn hạn (1-2 tuần)
1. **Ưu tiên cao:** Thay thế 50 hardcoded strings phổ biến nhất bằng i18n keys
2. **Ưu tiên cao:** Thêm chú thích cho top 20 viết tắt y khoa phổ biến nhất
3. **Ưu tiên trung bình:** Cập nhật Analytics component để sử dụng i18n

### Trung hạn (1 tháng)
1. Hoàn thành việc thay thế tất cả hardcoded strings
2. Thêm chú thích cho tất cả viết tắt y khoa quan trọng
3. Chuẩn hóa thuật ngữ trong toàn bộ ứng dụng

### Dài hạn (3+ tháng)
1. Thiết lập quy trình review cho việt hóa mới
2. Tạo documentation cho developers
3. Tích hợp checks vào CI/CD pipeline

## Kết luận

Hệ thống việt hóa của ứng dụng đã có nền tảng tốt với các file dịch tập trung và thuật ngữ chính xác. Tuy nhiên, vẫn còn nhiều cơ hội cải thiện:

1. **Tăng cường sử dụng i18n:** Thay thế hardcoded strings bằng i18n keys sẽ giúp dễ dàng bảo trì và cập nhật.

2. **Thêm chú thích:** Các viết tắt y khoa nên có chú thích để người dùng không chuyên cũng hiểu được.

3. **Nhất quán:** Đảm bảo cùng một thuật ngữ được sử dụng nhất quán trong toàn bộ ứng dụng.

4. **Mở rộng từ điển:** Tiếp tục bổ sung thuật ngữ mới vào từ điển khi phát hiện.

Với các công cụ và tài liệu đã tạo, việc cải thiện việt hóa sẽ trở nên dễ dàng và có hệ thống hơn.

---

**Tài liệu liên quan:**
- `docs/medical_terms_glossary.md` - Từ điển thuật ngữ y khoa
- `utils/term_annotations.py` - Hệ thống chú thích
- `utils/i18n.py` - Hệ thống i18n
- `scripts/check_vietnamese_localization.py` - Script kiểm tra

**Người phụ trách:** Development Team  
**Cập nhật lần cuối:** 2025-01-30
