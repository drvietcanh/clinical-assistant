# Hướng Dẫn Bổ Sung Thủ Công Dữ Liệu Thuốc

**Ngày tạo:** 2026-01-13  
**Mục đích:** Hướng dẫn chi tiết quy trình bổ sung thủ công các field thiếu cho dữ liệu thuốc

---

## Mục Lục

1. [Tổng Quan](#tổng-quan)
2. [Chuẩn Bị](#chuẩn-bị)
3. [Quy Trình Bổ Sung](#quy-trình-bổ-sung)
4. [Hướng Dẫn Theo Field](#hướng-dẫn-theo-field)
5. [Nguồn Tham Khảo](#nguồn-tham-khảo)
6. [Lưu Ý Quan Trọng](#lưu-ý-quan-trọng)
7. [Troubleshooting](#troubleshooting)

---

## Tổng Quan

Hệ thống hiện có **714 thuốc**, trong đó:

- **109 thuốc** thiếu field `pregnancy` (bắt buộc) - **ƯU TIÊN CAO NHẤT**
- **1 thuốc** thiếu field `dosage` (bắt buộc)
- **14 thuốc** thiếu field `side_effects` (bắt buộc)
- **35 thuốc** thiếu field `contraindications` (bắt buộc)
- **57 thuốc** thiếu field `interactions` (bắt buộc)
- **62 thuốc** có field `storage` rỗng (bắt buộc)
- Nhiều thuốc có field khuyến nghị rỗng (có thể bỏ qua)

### Nguyên Tắc

1. **Làm chậm, kiểm tra kỹ**: Không vội vàng, kiểm tra từng thuốc cẩn thận
2. **Tránh thông tin giả**: Chỉ bổ sung khi có nguồn đáng tin cậy
3. **Bỏ qua khi cần**: Nếu không tìm thấy thông tin đáng tin cậy → đánh dấu bỏ qua
4. **Ghi chú nguồn**: Luôn ghi chú nguồn tham khảo vào field `references`

---

## Chuẩn Bị

### Bước 1: Chạy Script Phân Tích

```bash
cd D:\1app\medical
python drugs/manual_supplementation_analyzer.py
```

**Kết quả:**
- `drugs/manual_supplementation_priority.json` - Danh sách ưu tiên
- `drugs/manual_supplementation_report.md` - Báo cáo phân tích

### Bước 2: Tạo Template

```bash
python drugs/create_manual_supplementation_template.py
```

**Kết quả:**
- `drugs/manual_supplementation_workbook.json` - Workbook tổng hợp
- `drugs/manual_supplementation_templates/` - Template riêng cho từng thuốc

### Bước 3: Khởi Động Helper

```bash
python drugs/manual_supplementation_helper.py
```

---

## Quy Trình Bổ Sung

### Workflow Cho Mỗi Thuốc

1. **Chọn thuốc cần bổ sung**
   - Ưu tiên P0 trước (pregnancy, dosage)
   - Sau đó P1 (side_effects, contraindications, interactions)
   - Cuối cùng P2, P3

2. **Xem thông tin thuốc**
   - Đọc template trong `manual_supplementation_templates/`
   - Xem field nào cần bổ sung
   - Xem hướng dẫn cho từng field

3. **Tìm kiếm thông tin**
   - Sử dụng nguồn đáng tin cậy (xem phần [Nguồn Tham Khảo](#nguồn-tham-khảo))
   - So sánh từ ít nhất 2 nguồn
   - Ưu tiên nguồn chính thức (FDA, EMA, nhà sản xuất)

4. **Bổ sung dữ liệu**
   - Sử dụng `manual_supplementation_helper.py`
   - Nhập dữ liệu theo format đúng
   - Ghi chú nguồn tham khảo

5. **Kiểm tra và lưu**
   - Validate dữ liệu trước khi lưu
   - Tạo backup file module trước khi cập nhật
   - Cập nhật file nguồn trong `drug_modules/`

---

## Hướng Dẫn Theo Field

### Field `pregnancy` (109 thuốc thiếu) - **ƯU TIÊN CAO NHẤT**

**Format:** `string`  
**Ví dụ:** `"D - Chống chỉ định trong thai kỳ"` hoặc `"D"`

**FDA Categories:**
- **A**: Không có nguy cơ trong các nghiên cứu có đối chứng
- **B**: Không có bằng chứng về nguy cơ ở người
- **C**: Nguy cơ không thể loại trừ
- **D**: Có bằng chứng về nguy cơ nhưng lợi ích có thể lớn hơn
- **X**: Chống chỉ định trong thai kỳ

**Nguồn tham khảo:**
1. FDA Pregnancy Categories Database
2. UpToDate Pregnancy Safety
3. Package insert (nhà sản xuất)
4. Dược thư Quốc gia Việt Nam

**Quy tắc:**
- Ưu tiên FDA category
- Nếu không tìm thấy → đánh dấu "BỎ QUA" và ghi chú lý do
- Nếu có nhiều nguồn khác nhau → ưu tiên FDA, sau đó là nhà sản xuất

**Ví dụ:**
```json
"pregnancy": "D - Chống chỉ định trong thai kỳ do nguy cơ gây hại cho thai nhi"
```

---

### Field `dosage` (1 thuốc thiếu: Budesonide inhaled)

**Format:** `dict`  
**Cấu trúc:**
```json
{
  "adult": "200-800mcg x 2 lần/ngày",
  "adult_initial": "200mcg x 2 lần/ngày",
  "pediatric": "100-400mcg x 2 lần/ngày (trẻ em >6 tuổi)",
  "notes": "Điều chỉnh liều theo đáp ứng"
}
```

**Nguồn tham khảo:**
1. Package insert (nhà sản xuất)
2. UpToDate Dosing
3. FDA Labeling
4. Hướng dẫn sử dụng thuốc Việt Nam

**Quy tắc:**
- Bổ sung đầy đủ liều cho các trường hợp (adult, pediatric)
- Ghi chú đặc biệt nếu có
- Kiểm tra đơn vị đo (mg, mcg, IU, etc.)

---

### Field `side_effects` (14 thuốc thiếu)

**Format:** `list of strings`  
**Ví dụ:** `["Ho khan", "Tăng kali máu", "Hạ huyết áp"]`

**Nguồn tham khảo:**
1. Package insert
2. UpToDate Adverse Effects
3. FDA Labeling
4. Micromedex

**Quy tắc:**
- Bổ sung ít nhất 3-5 tác dụng phụ phổ biến nhất
- Ưu tiên tác dụng phụ nghiêm trọng
- Nếu không tìm thấy → có thể bổ sung dựa trên nhóm thuốc tương tự

**Ví dụ:**
```json
"side_effects": [
  "Ho khan",
  "Tăng kali máu",
  "Hạ huyết áp",
  "Phù mạch",
  "Suy thận cấp"
]
```

---

### Field `contraindications` (35 thuốc thiếu)

**Format:** `list of strings` hoặc `dict`  
**Ví dụ 1 (list):** `["Dị ứng", "Có thai", "Hẹp động mạch thận 2 bên"]`  
**Ví dụ 2 (dict):**
```json
{
  "tuyệt_đối": ["Dị ứng thuốc", "Có thai"],
  "tương_đối": ["Suy thận trung bình", "Tăng kali máu"]
}
```

**Nguồn tham khảo:**
1. Package insert
2. FDA Labeling
3. UpToDate Contraindications
4. Dược thư Quốc gia

**Quy tắc:**
- Bổ sung chống chỉ định tuyệt đối trước
- Nếu không tìm thấy → có thể bổ sung dựa trên nhóm thuốc
- Phân biệt tuyệt đối và tương đối nếu có thể

---

### Field `interactions` (57 thuốc thiếu)

**Format:** `list of strings`  
**Ví dụ:** `["Kali bổ sung: tăng nguy cơ tăng kali máu", "NSAID: giảm hiệu quả hạ huyết áp"]`

**Nguồn tham khảo:**
1. Drug interactions database (Drugs.com, Medscape)
2. UpToDate Drug Interactions
3. Package insert
4. Micromedex

**Quy tắc:**
- Bổ sung tương tác quan trọng nhất (major interactions)
- Format: "Thuốc A: mô tả tương tác"
- Nếu không tìm thấy → có thể bỏ qua hoặc bổ sung dựa trên nhóm thuốc

---

### Field `storage` (62 thuốc rỗng)

**Format:** `string`  
**Ví dụ:** `"Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng"`

**Nguồn tham khảo:**
1. Package insert
2. FDA Labeling
3. Hướng dẫn bảo quản thuốc

**Quy tắc:**
- Nếu không tìm thấy → có thể dùng giá trị mặc định theo nhóm thuốc
- Hoặc đánh dấu "BỎ QUA" nếu không quan trọng
- Một số nhóm thuốc có storage tương tự nhau

**Giá trị mặc định theo nhóm:**
- **Thuốc uống thông thường**: "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm"
- **Thuốc tiêm**: "Bảo quản ở nhiệt độ phòng (15-30°C), tránh đông lạnh"
- **Thuốc nhạy cảm nhiệt độ**: "Bảo quản ở 2-8°C, tránh đông lạnh"

---

## Nguồn Tham Khảo

### Nguồn Chính Thức (Ưu Tiên Cao)

1. **FDA (Food and Drug Administration)**
   - Website: https://www.fda.gov/
   - FDA Labeling Database
   - Pregnancy Categories Database

2. **EMA (European Medicines Agency)**
   - Website: https://www.ema.europa.eu/
   - EPAR (European Public Assessment Report)

3. **WHO (World Health Organization)**
   - WHO Model Formulary
   - Essential Medicines List

4. **Nhà Sản Xuất**
   - Package insert (tờ hướng dẫn sử dụng)
   - Official website của nhà sản xuất

### Nguồn Y Khoa Uy Tín

1. **UpToDate**
   - Database y khoa chuyên sâu
   - Có thông tin về dosing, pregnancy, interactions

2. **Medscape**
   - Drug Reference
   - Drug Interactions Checker

3. **Micromedex**
   - Drug Information Database
   - Drug Interactions

4. **Drugs.com**
   - Drug Information
   - Drug Interactions Checker

### Nguồn Việt Nam

1. **Dược Thư Quốc Gia Việt Nam**
   - Thông tin thuốc chính thức của Việt Nam

2. **Hướng Dẫn Sử Dụng Thuốc**
   - Các tài liệu hướng dẫn của Bộ Y Tế

3. **Các App Y Tế Việt Nam**
   - Medscape Vietnam
   - Các app tra cứu thuốc uy tín

---

## Lưu Ý Quan Trọng

### 1. Tránh Thông Tin Giả

- **KHÔNG** bịa đặt thông tin
- **KHÔNG** copy từ nguồn không đáng tin cậy
- **KHÔNG** đoán mò dữ liệu
- **CHỈ** bổ sung khi có nguồn đáng tin cậy

### 2. Kiểm Tra Kỹ

- So sánh từ ít nhất 2 nguồn
- Ưu tiên nguồn chính thức
- Kiểm tra ngày cập nhật của nguồn
- Xác minh thông tin trước khi lưu

### 3. Bỏ Qua Khi Cần

- Nếu không tìm thấy thông tin đáng tin cậy → **BỎ QUA**
- Ghi chú lý do bỏ qua
- Không để field rỗng với giá trị giả

### 4. Ghi Chú Nguồn

- Luôn ghi chú nguồn vào field `references`
- Format: `{"primary_sources": ["UpToDate", "FDA Labeling"], "last_updated": "2026-01-13"}`

### 5. Backup và Validation

- Luôn tạo backup trước khi cập nhật file nguồn
- Validate dữ liệu sau khi bổ sung
- Kiểm tra format đúng với field_validator

---

## Troubleshooting

### Vấn Đề: Không tìm thấy thông tin

**Giải pháp:**
1. Thử nhiều nguồn khác nhau
2. Tìm kiếm bằng tên thuốc khác (generic name, brand name)
3. Tìm kiếm bằng nhóm thuốc tương tự
4. Nếu vẫn không tìm thấy → đánh dấu "BỎ QUA"

### Vấn Đề: Thông tin mâu thuẫn giữa các nguồn

**Giải pháp:**
1. Ưu tiên nguồn chính thức (FDA, EMA, nhà sản xuất)
2. Kiểm tra ngày cập nhật của nguồn
3. Sử dụng nguồn mới nhất
4. Ghi chú trong field `references` về sự mâu thuẫn

### Vấn Đề: Format không đúng

**Giải pháp:**
1. Kiểm tra `field_validator.py` để biết format chính xác
2. Xem ví dụ trong `DRUG_FIELD_STRUCTURE.md`
3. Sử dụng script validation để kiểm tra

### Vấn Đề: Không biết bắt đầu từ đâu

**Giải pháp:**
1. Bắt đầu với P0 (pregnancy, dosage)
2. Làm từng thuốc một, không vội vàng
3. Sử dụng `manual_supplementation_helper.py` để hướng dẫn

---

## Kết Luận

Quy trình bổ sung thủ công cần:
- ✅ Kiên nhẫn và cẩn thận
- ✅ Kiểm tra kỹ từng thuốc
- ✅ Sử dụng nguồn đáng tin cậy
- ✅ Ghi chú đầy đủ
- ✅ Backup và validation

**Nhớ:** Chất lượng quan trọng hơn số lượng. Tốt hơn là bỏ qua một field thay vì điền thông tin giả.

---

**Tài liệu liên quan:**
- `docs/DRUG_FIELD_STRUCTURE.md` - Cấu trúc field chuẩn
- `docs/DRUG_DATA_FIX_PROGRESS_DETAILED.md` - Tiến trình sửa lỗi
- `drugs/field_validator.py` - Validation rules
