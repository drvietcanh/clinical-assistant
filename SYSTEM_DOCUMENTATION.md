# TÀI LIỆU HỆ THỐNG QUẢN LÝ THUỐC

**Phiên bản**: 1.0  
**Ngày tạo**: 2025-02-18  
**Trạng thái**: ✅ Hoàn chỉnh

---

## MỤC LỤC

1. [Tổng quan hệ thống](#tổng-quan-hệ-thống)
2. [14 Field chuẩn](#14-field-chuẩn)
3. [Cấu trúc thuốc](#cấu-trúc-thuốc)
4. [Hệ thống quản lý](#hệ-thống-quản-lý)
5. [Cách sử dụng](#cách-sử-dụng)
6. [Tiến trình làm việc](#tiến-trình-làm-việc)

---

## TỔNG QUAN HỆ THỐNG

### Mục tiêu:
- ✅ **Cấu trúc đồng bộ**: Mỗi thuốc có 14 field chuẩn, thứ tự khoa học
- ✅ **Dễ tìm kiếm**: Hệ thống tìm kiếm thông minh, nhiều cách
- ✅ **Dễ sửa chữa**: Cấu trúc rõ ràng, có thể sửa từng field
- ✅ **Khoa học**: Sắp xếp theo logic y học
- ✅ **Quản lý tập trung**: Tất cả trong một hệ thống

### Trạng thái hiện tại:
- **Tổng số thuốc**: 721
- **Thuốc có đủ 14 field**: 716 (99%)
- **Thuốc thiếu field**: 5 (1%)
- **Cấu trúc**: Đồng bộ và khoa học

---

## 14 FIELD CHUẨN

### Thứ tự khoa học:

#### 1. Core Fields (5):
1. **group** - Nhóm thuốc
   - Ví dụ: "Antibiotic - Aminoglycoside"
   - Mục đích: Phân loại thuốc theo nhóm dược lý

2. **vietnamese_name** - Tên tiếng Việt
   - Ví dụ: "Gentamicin, Garamycin"
   - Mục đích: Tên thuốc và biệt dược

3. **administration** - Đường dùng
   - Ví dụ: ["IV", "IM"]
   - Mục đích: Các đường dùng có thể

4. **indications** - Chỉ định
   - Ví dụ: ["Nhiễm khuẩn Gram-âm nặng", ...]
   - Mục đích: Các chỉ định sử dụng

5. **dosage** - Liều dùng
   - Cấu trúc: dict với adult_standard, adult_maintenance, notes
   - Mục đích: Liều dùng chi tiết

#### 2. Extended Fields (4):
6. **side_effects** - Tác dụng phụ
   - Ví dụ: ["Độc thận", "Độc thính giác", ...]
   - Mục đích: Các tác dụng phụ có thể gặp

7. **contraindications** - Chống chỉ định
   - Ví dụ: ["Dị ứng", "Suy thận nặng", ...]
   - Mục đích: Các trường hợp không được dùng

8. **interactions** - Tương tác thuốc
   - Ví dụ: ["Vancomycin: tăng độc thận", ...]
   - Mục đích: Tương tác với thuốc khác

9. **pregnancy** - Thai kỳ
   - Ví dụ: "D - Độc thai nhi"
   - Mục đích: Phân loại FDA cho thai kỳ

#### 3. Enhanced Fields (5):
10. **mechanism_of_action** - Cơ chế tác dụng
    - Ví dụ: "Gentamicin là aminoglycoside kháng sinh..."
    - Mục đích: Giải thích cách thuốc hoạt động

11. **monitoring** - Theo dõi
    - Ví dụ: ["TDM", "Chức năng thận", ...]
    - Mục đích: Các thông số cần theo dõi

12. **precautions** - Thận trọng
    - Ví dụ: ["TDM BẮT BUỘC", "Độc thận", ...]
    - Mục đích: Các lưu ý quan trọng

13. **pharmacokinetics** - Dược động học
    - Cấu trúc: dict với half_life, onset, duration, protein_binding, clearance
    - Mục đích: Thông tin dược động học

14. **storage** - Bảo quản
    - Ví dụ: "Bảo quản ở nhiệt độ phòng (20-25°C)"
    - Mục đích: Hướng dẫn bảo quản

---

## CẤU TRÚC THUỐC

### Template chuẩn:
```python
"DrugName": {
    # Core Fields (1-5)
    "group": "...",
    "vietnamese_name": "...",
    "administration": [...],
    "indications": [...],
    "dosage": {
        "adult_standard": "...",
        "adult_maintenance": "...",
        "notes": "..."
    },
    
    # Extended Fields (6-9)
    "side_effects": [...],
    "contraindications": [...],
    "interactions": [...],
    "pregnancy": "...",
    
    # Enhanced Fields (10-14)
    "mechanism_of_action": "...",
    "monitoring": [...],
    "precautions": [...],
    "pharmacokinetics": {
        "half_life": "...",
        "onset": "...",
        "duration": "...",
        "protein_binding": "...",
        "clearance": "..."
    },
    "storage": "...",
    
    # Additional Fields (tùy chọn)
    "black_box_warnings": "...",
    "drug_interactions": {...},
    "pregnancy_lactation": {...},
    "hepatic_adjustment": {...},
    "overdose_management": {...},
    "reversal_agents": {...},
    "administration_instructions": {...},
    "references": {...}
}
```

### Nguyên tắc:
1. **Thứ tự field**: Luôn theo thứ tự 14 field chuẩn trước, sau đó mới đến field bổ sung
2. **Cấu trúc đồng nhất**: Tất cả thuốc nên có cấu trúc giống nhau
3. **Đầy đủ thông tin**: Mỗi field nên có giá trị, không để rỗng nếu có thể

---

## HỆ THỐNG QUẢN LÝ

### Scripts chính:

#### 1. `comprehensive_drug_management_system.py` ⭐
**Hệ thống quản lý tổng hợp - Sử dụng chính**

Chức năng:
- Load và quản lý 721 thuốc
- Tìm kiếm thông minh
- Kiểm tra cấu trúc
- Thống kê chi tiết
- Export báo cáo

#### 2. `drug_structure_standardizer.py`
**Chuẩn hóa cấu trúc**

Chức năng:
- Phân tích cấu trúc thuốc
- Xác định thuốc thiếu field
- Tạo kế hoạch chuẩn hóa
- Lưu báo cáo phân tích

#### 3. `drug_organizer_system.py`
**Tổ chức và sắp xếp**

Chức năng:
- Tổ chức thuốc theo file
- Phân loại cấu trúc
- Thống kê phân bố
- Lưu dữ liệu tổ chức

#### 4. `ultimate_drug_management_system.py`
**Quản lý tối ưu**

Chức năng:
- Index toàn diện
- Tìm kiếm nhanh
- Sắp xếp linh hoạt
- Quản lý hiệu quả

---

## CÁCH SỬ DỤNG

### 1. Kiểm tra trạng thái hệ thống:
```bash
python comprehensive_drug_management_system.py stats
```

**Kết quả**: Hiển thị tổng số thuốc, số thuốc có đủ 14 field, thống kê field

### 2. Tìm kiếm thuốc:
```bash
python comprehensive_drug_management_system.py search gentamicin
```

**Kết quả**: Danh sách thuốc matching, kèm trạng thái có đủ 14 field

### 3. Kiểm tra cấu trúc một thuốc:
```bash
python comprehensive_drug_management_system.py check Gentamicin
```

**Kết quả**: 
- File chứa thuốc
- Có đủ 14 field hay không
- Số lượng field
- Các field thiếu (nếu có)

### 4. Phân tích cấu trúc:
```bash
python drug_structure_standardizer.py
```

**Kết quả**: 
- Báo cáo phân tích chi tiết
- Danh sách thuốc thiếu field
- Kế hoạch chuẩn hóa
- Lưu file `drug_structure_analysis.json`

### 5. Tổ chức thuốc:
```bash
python drug_organizer_system.py
```

**Kết quả**: 
- Tóm tắt tổ chức
- Phân bố theo file
- Lưu file `drug_organization_data.json`

### 6. Export báo cáo:
```bash
python comprehensive_drug_management_system.py export report.json
```

**Kết quả**: File JSON chứa toàn bộ thông tin thuốc và thống kê

---

## TIẾN TRÌNH LÀM VIỆC

### Phiên hiện tại (2025-02-18):

#### Đã hoàn thành:
1. ✅ Phân tích cấu trúc thuốc hiện tại
2. ✅ Xác định 14 field chuẩn
3. ✅ Tạo hệ thống quản lý tổng hợp
4. ✅ Tạo hệ thống chuẩn hóa
5. ✅ Tạo hệ thống tổ chức
6. ✅ Phân tích và thống kê
7. ✅ Tạo tài liệu hướng dẫn

#### Kết quả:
- **721 thuốc** được quản lý
- **716 thuốc** (99%) có đủ 14 field
- **5 thuốc** (1%) cần bổ sung field

#### Cần làm tiếp:
1. ⚠️ Bổ sung field cho 5 thuốc:
   - Ampicillin
   - Amoxicillin-clavulanate
   - Ampicillin-sulbactam
   - Nafcillin
   - Oxacillin

### Hướng dẫn cho phiên sau:

#### Bước 1: Kiểm tra trạng thái
```bash
python comprehensive_drug_management_system.py stats
```

#### Bước 2: Tìm thuốc cần sửa
```bash
python drug_structure_standardizer.py
```

#### Bước 3: Kiểm tra thuốc cụ thể
```bash
python comprehensive_drug_management_system.py check <drug_name>
```

#### Bước 4: Bổ sung field
- Sử dụng `add_missing_fields_simple.py` hoặc sửa thủ công
- Đảm bảo thêm đúng 3 field: interactions, monitoring, storage

#### Bước 5: Kiểm tra lại
```bash
python comprehensive_drug_management_system.py stats
```

---

## FILES QUAN TRỌNG

### Scripts:
- `comprehensive_drug_management_system.py` - Hệ thống chính ⭐
- `drug_structure_standardizer.py` - Chuẩn hóa cấu trúc
- `drug_organizer_system.py` - Tổ chức và sắp xếp
- `ultimate_drug_management_system.py` - Quản lý tối ưu
- `add_missing_fields_simple.py` - Bổ sung field

### Tài liệu:
- `SYSTEM_DOCUMENTATION.md` - File này (tài liệu hệ thống)
- `DRUG_MANAGEMENT_PROGRESS.md` - Tiến trình quản lý
- `ULTIMATE_SYSTEM_GUIDE.md` - Hướng dẫn hệ thống tối ưu

### Reports/Data:
- `drug_structure_analysis.json` - Báo cáo phân tích cấu trúc
- `drug_organization_data.json` - Dữ liệu tổ chức
- `comprehensive_drug_report.json` - Báo cáo tổng hợp (khi export)

---

## LƯU Ý QUAN TRỌNG

1. **14 field chuẩn**: Đây là các field bắt buộc, phải có trong mỗi thuốc
2. **Thứ tự field**: Nên sắp xếp theo thứ tự chuẩn để dễ đọc và quản lý
3. **Cấu trúc đồng bộ**: Tất cả thuốc nên có cấu trúc giống nhau
4. **Field bổ sung**: Có thể thêm nhưng không bắt buộc
5. **Kiểm tra thường xuyên**: Chạy `stats` để kiểm tra trạng thái

---

## HỖ TRỢ

Nếu có vấn đề:
1. Kiểm tra tài liệu này
2. Chạy `stats` để xem trạng thái
3. Chạy `check <drug_name>` để kiểm tra thuốc cụ thể
4. Xem các file JSON để phân tích chi tiết

---

**Cập nhật lần cuối**: 2025-02-18  
**Phiên bản**: 1.0  
**Trạng thái**: ✅ Hoàn chỉnh và sẵn sàng sử dụng

