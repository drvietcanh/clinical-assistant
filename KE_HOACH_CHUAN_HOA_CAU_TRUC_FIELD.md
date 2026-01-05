# Kế Hoạch Chuẩn Hóa Cấu Trúc Field Cho Tất Cả Thuốc

**Ngày tạo:** 2026-01-03  
**Mục tiêu:** Chuẩn hóa cấu trúc của tất cả các field trong hệ thống thuốc để dễ dàng sắp xếp, tìm kiếm và sửa chữa

## Mục Tiêu

Chuẩn hóa cấu trúc của tất cả các field trong hệ thống thuốc để:
- Dễ dàng sắp xếp, tìm kiếm và sửa chữa
- Validator có thể nhận ra và validate chính xác
- Đảm bảo tính nhất quán trong toàn bộ hệ thống
- Hỗ trợ tốt hơn cho các công cụ quản lý và tìm kiếm

## Phân Tích Hiện Trạng

Dựa trên báo cáo `DRUG_FIELDS_REPORT.json` và phân tích chi tiết (`field_structure_detailed_analysis.json`), các field có nhiều cấu trúc khác nhau:

### 1. pregnancy_lactation (6 cấu trúc khác nhau - 649 thuốc có field này)

- **618 thuốc (83.5%)**: Cấu trúc chuẩn `{"fda_category", "lactation": {"safety", "details", "recommendation"}, "pregnancy_details"}`
- **15 thuốc (2.0%)**: `{"fda_category", "lactation_details": "", "pregnancy_details"}` - cần chuyển `lactation_details` thành `lactation` dict
- **5 thuốc (0.7%)**: `{"lactation", "pregnancy_category", "pregnancy_notes"}` - cần chuẩn hóa keys (`pregnancy_category` → `fda_category`, `pregnancy_notes` → `pregnancy_details`)
- **1 thuốc**: `{"fda_category", "pregnancy_details"}` - thiếu `lactation`
- **1 thuốc**: `{"lactation", "pregnancy_details"}` - thiếu `fda_category`
- **9 thuốc (1.2%)**: String - cần chuyển thành dict

**Tổng cần sửa:** ~31 thuốc

### 2. hepatic_adjustment (3 cấu trúc khác nhau - 646 thuốc có field này)

- **600 thuốc (81.1%)**: Cấu trúc chuẩn `{"mild", "moderate", "severe", "notes"}`
- **40 thuốc (5.4%)**: `{"mild", "moderate", "severe"}` - thiếu `notes`
- **6 thuốc (0.8%)**: `{"adjustment"}` - cần chuyển đổi hoàn toàn

**Tổng cần sửa:** ~46 thuốc

### 3. overdose_management (4 cấu trúc khác nhau - 642 thuốc có field này)

- **619 thuốc (83.6%)**: Cấu trúc chuẩn `{"symptoms": [], "antidote": "", "treatment": [], "monitoring": ""}`
- **17 thuốc (2.3%)**: `{"symptoms": [], "antidote": "", "treatment": ""}` - thiếu `monitoring`, `treatment` là string thay vì list
- **5 thuốc (0.7%)**: String - cần chuyển thành dict
- **1 thuốc**: `{"symptoms": [], "treatment": ""}` - thiếu `antidote` và `monitoring`

**Tổng cần sửa:** ~23 thuốc

### 4. contraindications (5 cấu trúc khác nhau - 740 thuốc có field này)

- **661 thuốc (89.3%)**: List `["item1", "item2"]` - có thể giữ nguyên hoặc chuyển thành dict
- **435 thuốc (58.8%)**: Dict `{"tuyệt_đối": [], "tương_đối": []}` (chuẩn)
- **10 thuốc (1.4%)**: Dict `{"absolute": []}` - cần chuyển key thành `tuyệt_đối`
- **3 thuốc (0.4%)**: Dict `{"absolute": [], "relative": []}` - cần chuyển keys (`absolute` → `tuyệt_đối`, `relative` → `tương_đối`)
- **1 thuốc**: Dict với keys khác

**Lưu ý**: Số lượng > 740 vì một số thuốc có cả list và dict (có thể do lỗi hoặc cần kiểm tra)

**Tổng cần sửa:** ~14 thuốc (nếu chỉ chuẩn hóa dict, giữ nguyên list)

### 5. drug_interactions (6 cấu trúc khác nhau - 642 thuốc có field này)

- **579 thuốc (78.2%)**: Cấu trúc chuẩn `{"major": [], "moderate": [], "minor": []}`
- **46 thuốc (6.2%)**: `{"major": [], "moderate": []}` - thiếu `minor`
- **9 thuốc (1.2%)**: `{"major": []}` - thiếu `moderate` và `minor`
- **4 thuốc (0.5%)**: `{"moderate": []}` - thiếu `major` và `minor`
- **3 thuốc (0.4%)**: `{"minor": []}` - thiếu `major` và `moderate`
- **1 thuốc**: `{"minor": [], "moderate": []}` - thiếu `major`

**Tổng cần sửa:** ~63 thuốc

### 6. administration_instructions (44 cấu trúc khác nhau - 737 thuốc có field này)

- **234 thuốc (31.6%)**: `{"iv": {}, "oral": {}}` - chuẩn
- **151 thuốc (20.4%)**: `{"oral": {}}` - chuẩn
- **68 thuốc (9.2%)**: `{}` - rỗng, có thể giữ nguyên
- **15 thuốc (2.0%)**: `{"preparation": "", "administration": "", "monitoring": []}` - cấu trúc cũ, cần chuyển đổi
- **5 thuốc (0.7%)**: String - cần chuyển thành dict
- **Còn lại**: Nhiều cấu trúc khác nhau dựa trên đường dùng - có thể giữ nguyên nếu là dict với keys là đường dùng

**Tổng cần sửa:** ~20 thuốc (chỉ những cấu trúc không chuẩn)

### 7. references (7 cấu trúc khác nhau - 640 thuốc có field này)

- **633 thuốc (85.5%)**: Cấu trúc chuẩn `{"primary_sources": [], "last_updated": "", "evidence_level": ""}`
- **3 thuốc (0.4%)**: Có thêm keys không chuẩn (có thể giữ nguyên nếu không ảnh hưởng)
- **5 thuốc (0.7%)**: String - cần chuyển thành dict
- **1 thuốc**: `{"guidelines": [], "other": [], "primary": []}` - cần chuẩn hóa keys

**Tổng cần sửa:** ~6 thuốc

## Cấu Trúc Chuẩn Đề Xuất

### pregnancy_lactation
```python
{
    "fda_category": str,  # "A", "B", "C", "D", "X" hoặc ""
    "pregnancy_details": str,  # Chi tiết về sử dụng trong thai kỳ
    "lactation": {
        "safety": str,  # "Compatible", "Unknown", "Use with caution", etc.
        "details": str,  # Chi tiết về bài tiết vào sữa mẹ
        "recommendation": str  # Khuyến nghị sử dụng
    }
}
```

### hepatic_adjustment
```python
{
    "mild": str,  # Điều chỉnh liều cho suy gan nhẹ
    "moderate": str,  # Điều chỉnh liều cho suy gan trung bình
    "severe": str,  # Điều chỉnh liều cho suy gan nặng
    "notes": str  # Ghi chú thêm (có thể rỗng)
}
```

### overdose_management
```python
{
    "symptoms": list[str],  # Danh sách triệu chứng
    "antidote": str,  # Thuốc giải độc (có thể rỗng hoặc "Không có")
    "treatment": list[str],  # Danh sách các bước điều trị
    "monitoring": str  # Theo dõi sau quá liều
}
```

### contraindications
**Chuẩn hóa thành dict** (giữ lại list nếu cần tương thích ngược):
```python
{
    "tuyệt_đối": list[str],  # Chống chỉ định tuyệt đối
    "tương_đối": list[str]  # Chống chỉ định tương đối (có thể rỗng)
}
```

**Hoặc giữ cả hai cấu trúc** (list và dict) để tương thích ngược.

### drug_interactions
```python
{
    "major": list[dict],  # Tương tác nghiêm trọng
    "moderate": list[dict],  # Tương tác trung bình
    "minor": list[dict]  # Tương tác nhẹ (có thể rỗng)
}
```

### administration_instructions
**Giữ nguyên cấu trúc dựa trên đường dùng**, nhưng đảm bảo:
- Tất cả đều là dict
- Keys là tên đường dùng (lowercase): `"oral"`, `"iv"`, `"im"`, `"sc"`, etc.
- Values là dict với các hướng dẫn chi tiết

### references
```python
{
    "primary_sources": list[str],  # Nguồn tham khảo chính
    "last_updated": str,  # Ngày cập nhật (format: "YYYY-MM-DD")
    "evidence_level": str  # Mức độ bằng chứng (A, B, C, etc.)
}
```

## Kế Hoạch Thực Hiện

### Phase 1: Phân Tích và Chuẩn Bị (1-2 giờ)

#### Task 1.1: Tạo script phân tích chi tiết
- **File**: `analyze_field_structure_for_standardization.py`
- **Mục đích**: Phân tích tất cả các biến thể và tạo báo cáo chi tiết với danh sách thuốc cần sửa
- **Output**: 
  - `field_standardization_analysis.json` - Dữ liệu chi tiết
  - `field_standardization_analysis.md` - Báo cáo dễ đọc
- **Chức năng**:
  - Quét tất cả file thuốc
  - Phân loại từng field theo cấu trúc
  - Liệt kê tất cả thuốc cần sửa cho từng field
  - Tính toán số lượng thuốc cần sửa

#### Task 1.2: Xác định mapping rules
- **File**: `field_structure_mapping_rules.py`
- **Mục đích**: Định nghĩa các quy tắc chuyển đổi từ cấu trúc cũ sang cấu trúc mới
- **Nội dung**:
  - Các hàm chuyển đổi cho từng field
  - Mapping tables cho keys cần đổi tên
  - Template cho cấu trúc chuẩn
  - Validation rules

#### Task 1.3: Cập nhật field_standardizer.py
- **File**: `drugs/field_standardizer.py`
- **Mục đích**: Thêm các hàm chuẩn hóa cấu trúc
- **Hàm mới**:
  - `standardize_pregnancy_lactation_structure(drug_data: Dict) -> Dict`
  - `standardize_hepatic_adjustment_structure(drug_data: Dict) -> Dict`
  - `standardize_overdose_management_structure(drug_data: Dict) -> Dict`
  - `standardize_contraindications_structure(drug_data: Dict) -> Dict`
  - `standardize_drug_interactions_structure(drug_data: Dict) -> Dict`
  - `standardize_administration_instructions_structure(drug_data: Dict) -> Dict`
  - `standardize_references_structure(drug_data: Dict) -> Dict`
  - `standardize_all_field_structures(drug_data: Dict) -> Dict` - Áp dụng tất cả

### Phase 2: Tạo Script Chuẩn Hóa (2-3 giờ)

#### Task 2.1: Tạo script chuẩn hóa chính
- **File**: `standardize_all_field_structures.py`
- **Chức năng**:
  - Quét tất cả các file thuốc
  - Load từng thuốc
  - Áp dụng các quy tắc chuẩn hóa
  - Tạo backup trước khi sửa
  - Preview thay đổi (dry-run mode)
  - Áp dụng thay đổi với rollback nếu có lỗi
  - Progress bar và logging
- **Tính năng**:
  - Dry-run mode để xem trước
  - Batch processing với progress tracking
  - Backup tự động
  - Rollback nếu có lỗi
  - Báo cáo chi tiết về thay đổi

#### Task 2.2: Tạo script validation sau chuẩn hóa
- **File**: `validate_standardized_fields.py`
- **Mục đích**: Kiểm tra tất cả field sau khi chuẩn hóa
- **Chức năng**:
  - Validate tất cả field bằng `FieldValidator`
  - Kiểm tra không mất dữ liệu
  - So sánh trước và sau chuẩn hóa
  - Báo cáo các vấn đề nếu có
  - Đảm bảo import vẫn hoạt động

### Phase 3: Chuẩn Hóa Từng Field (3-4 giờ)

#### Task 3.1: Chuẩn hóa pregnancy_lactation (~31 thuốc)
- Chuyển `lactation_details` thành `lactation` dict với cấu trúc `{"safety": "", "details": <old_value>, "recommendation": ""}`
- Chuẩn hóa keys: `pregnancy_category` → `fda_category`, `pregnancy_notes` → `pregnancy_details`
- Thêm `lactation` dict nếu thiếu
- Thêm `fda_category` nếu thiếu
- Chuyển string thành dict với cấu trúc chuẩn

#### Task 3.2: Chuẩn hóa hepatic_adjustment (~46 thuốc)
- Thêm `notes: ""` cho 40 thuốc thiếu
- Chuyển đổi 6 thuốc có cấu trúc `{"adjustment": "..."}` thành cấu trúc chuẩn:
  - Nếu `adjustment` chứa thông tin về các mức độ, phân tích và chuyển đổi
  - Nếu không, đặt vào `notes`

#### Task 3.3: Chuẩn hóa overdose_management (~23 thuốc)
- Thêm `monitoring: ""` cho 17 thuốc thiếu
- Chuyển `treatment` từ string sang list (split by newline hoặc comma)
- Thêm `antidote: ""` nếu thiếu
- Chuyển string thành dict với cấu trúc chuẩn

#### Task 3.4: Chuẩn hóa contraindications (~14 thuốc)
- Chuyển keys: `absolute` → `tuyệt_đối`, `relative` → `tương_đối`
- Quyết định: Giữ cả list và dict để tương thích ngược, hoặc chỉ chuẩn hóa dict
- Nếu chọn chỉ chuẩn hóa dict: Chuyển list thành dict `{"tuyệt_đối": <list>, "tương_đối": []}`

#### Task 3.5: Chuẩn hóa drug_interactions (~63 thuốc)
- Thêm `minor: []` cho 46 thuốc thiếu
- Thêm `moderate: []` và `minor: []` cho 9 thuốc chỉ có `major`
- Thêm `major: []` và `minor: []` cho 4 thuốc chỉ có `moderate`
- Thêm `major: []` và `moderate: []` cho 3 thuốc chỉ có `minor`
- Thêm `major: []` cho 1 thuốc có `minor` và `moderate`

#### Task 3.6: Chuẩn hóa administration_instructions (~20 thuốc)
- Chuyển string thành dict `{"oral": {"instructions": <old_value>}}`
- Chuyển cấu trúc cũ `{"preparation", "administration", "monitoring"}` thành cấu trúc mới dựa trên đường dùng
- Đảm bảo tất cả đều là dict

#### Task 3.7: Chuẩn hóa references (~6 thuốc)
- Chuyển string thành dict với cấu trúc chuẩn
- Chuẩn hóa keys: `guidelines` → `primary_sources`, `other` → có thể thêm vào `primary_sources`, `primary` → `primary_sources`
- Đảm bảo format `last_updated` đúng (YYYY-MM-DD)

### Phase 4: Validation và Testing (1-2 giờ)

#### Task 4.1: Chạy validation toàn bộ
- Sử dụng `drugs/field_validator.py` để kiểm tra tất cả thuốc
- Đảm bảo không có lỗi validation
- Kiểm tra import vẫn hoạt động: `from drugs.drug_modules import ...`

#### Task 4.2: Kiểm tra không mất dữ liệu
- So sánh trước và sau chuẩn hóa
- Đảm bảo tất cả dữ liệu được giữ nguyên hoặc chuyển đổi đúng
- Tạo báo cáo so sánh: `field_standardization_comparison_report.json`

#### Task 4.3: Test các công cụ
- Test `drugs/drug_cli.py` vẫn hoạt động
- Test `drugs/drug_index_system.py` vẫn hoạt động
- Test search và filter
- Test `drugs/drug_manager_tool.py`

### Phase 5: Cập Nhật Tài Liệu (1 giờ)

#### Task 5.1: Cập nhật FIELD_STRUCTURE.md
- Thêm mô tả chi tiết về cấu trúc chuẩn cho từng field
- Thêm ví dụ cho từng field
- Thêm hướng dẫn migration
- Thêm mô tả về các biến thể không chuẩn và cách xử lý

#### Task 5.2: Cập nhật field_validator.py
- Thêm validation cho cấu trúc nested dict
- Đảm bảo validator nhận ra tất cả các cấu trúc chuẩn
- Thêm validation cho keys trong nested dict

#### Task 5.3: Tạo migration guide
- **File**: `FIELD_STRUCTURE_MIGRATION_GUIDE.md`
- **Nội dung**:
  - Hướng dẫn cách chuẩn hóa field mới
  - Ví dụ các trường hợp edge case
  - Best practices
  - Troubleshooting

## Rủi Ro và Giảm Thiểu

### 1. Mất dữ liệu trong quá trình chuyển đổi
- **Rủi ro**: Dữ liệu có thể bị mất hoặc sai trong quá trình chuyển đổi
- **Giảm thiểu**: 
  - Tạo backup đầy đủ trước khi sửa
  - Preview trước khi apply
  - Rollback nếu có lỗi
  - Validation sau mỗi batch

### 2. Lỗi syntax trong file Python
- **Rủi ro**: Sửa file có thể gây lỗi syntax
- **Giảm thiểu**: 
  - Validate AST sau khi sửa
  - Test import sau mỗi file
  - Sử dụng AST manipulation thay vì regex

### 3. Phá vỡ tương thích ngược
- **Rủi ro**: Code khác có thể phụ thuộc vào cấu trúc cũ
- **Giảm thiểu**: 
  - Giữ lại cấu trúc cũ nếu cần (ví dụ: contraindications có thể giữ cả list và dict)
  - Test tất cả các công cụ sau khi chuẩn hóa
  - Cập nhật tài liệu về breaking changes

### 4. Thời gian xử lý lâu
- **Rủi ro**: Xử lý 740 thuốc có thể mất nhiều thời gian
- **Giảm thiểu**: 
  - Xử lý theo batch
  - Có progress bar
  - Cho phép resume nếu bị gián đoạn

## Kết Quả Mong Đợi

- **100% thuốc có cấu trúc field chuẩn** cho các field quan trọng (pregnancy_lactation, hepatic_adjustment, overdose_management, drug_interactions, references)
- **Validator nhận ra và validate chính xác** tất cả các field
- **Dễ dàng sắp xếp, tìm kiếm và sửa chữa** nhờ cấu trúc thống nhất
- **Tài liệu đầy đủ** về cấu trúc chuẩn và cách migration
- **Không mất dữ liệu** trong quá trình chuẩn hóa
- **Tất cả công cụ vẫn hoạt động** sau khi chuẩn hóa

## Timeline Ước Tính

- **Phase 1**: 1-2 giờ
- **Phase 2**: 2-3 giờ
- **Phase 3**: 3-4 giờ
- **Phase 4**: 1-2 giờ
- **Phase 5**: 1 giờ

**Tổng cộng**: 8-12 giờ

## Files Sẽ Được Tạo/Sửa

### Files Mới
- `analyze_field_structure_for_standardization.py` - Script phân tích
- `field_structure_mapping_rules.py` - Mapping rules
- `standardize_all_field_structures.py` - Script chuẩn hóa chính
- `validate_standardized_fields.py` - Script validation
- `FIELD_STRUCTURE_MIGRATION_GUIDE.md` - Hướng dẫn migration
- `field_standardization_analysis.json` - Báo cáo phân tích
- `field_standardization_analysis.md` - Báo cáo phân tích (markdown)
- `field_standardization_comparison_report.json` - Báo cáo so sánh

### Files Sửa
- `drugs/field_standardizer.py` - Thêm các hàm chuẩn hóa cấu trúc
- `drugs/field_validator.py` - Cập nhật validation cho cấu trúc mới
- `drugs/FIELD_STRUCTURE.md` - Cập nhật tài liệu
- Tất cả các file trong `drugs/drug_modules/` - Chuẩn hóa cấu trúc field (ước tính ~200 file)

## Lưu Ý Quan Trọng

1. **Backup**: Luôn tạo backup trước khi sửa
2. **Dry-run**: Luôn chạy dry-run trước khi apply
3. **Validation**: Validate sau mỗi batch
4. **Testing**: Test tất cả công cụ sau khi hoàn thành
5. **Documentation**: Cập nhật tài liệu song song với implementation

## Quyết Định Cần Xác Nhận

1. **contraindications**: Giữ cả list và dict, hay chỉ chuẩn hóa thành dict?
   - **Đề xuất**: Giữ cả hai để tương thích ngược, nhưng ưu tiên dict cho thuốc mới

2. **administration_instructions**: Có cần chuẩn hóa tất cả các cấu trúc khác nhau thành một cấu trúc duy nhất không?
   - **Đề xuất**: Chỉ chuẩn hóa những cấu trúc không chuẩn (string, cấu trúc cũ), giữ nguyên các cấu trúc dựa trên đường dùng

3. **Thứ tự ưu tiên**: Field nào nên chuẩn hóa trước?
   - **Đề xuất**: pregnancy_lactation → hepatic_adjustment → overdose_management → drug_interactions → references → administration_instructions → contraindications

