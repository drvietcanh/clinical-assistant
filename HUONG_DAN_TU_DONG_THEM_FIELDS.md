# Hướng Dẫn Sử Dụng Script Tự Động Thêm Fields

## Tổng Quan

Đã tạo các script để tự động thêm các fields còn thiếu cho thuốc:

1. **`tu_dong_them_fields_nhanh.py`** - Script chính, nhanh nhất, sử dụng pattern matching
2. **`kiem_tra_fields_tat_ca_thuoc_v3.py`** - Script kiểm tra fields

## Cách Sử Dụng

### Bước 1: Kiểm tra fields thiếu
```bash
python kiem_tra_fields_tat_ca_thuoc_v3.py
```

Script này sẽ tạo:
- `BAO_CAO_KIEM_TRA_FIELDS_TAT_CA_THUOC_CHI_TIET.txt` - Báo cáo chi tiết
- `KE_HOACH_BO_SUNG_FIELDS_THEO_PHIEN.md` - Kế hoạch theo phiên

### Bước 2: Sử dụng script tự động (đang phát triển)

Script `tu_dong_them_fields_nhanh.py` có thể:
- Tìm file chứa thuốc
- Tự động thêm các fields template vào đúng vị trí
- Phát hiện loại thuốc (topical, nasal, oral, IV) để tạo template phù hợp

**Lưu ý:** Script này tạo các fields TEMPLATE, cần review và cập nhật thông tin chi tiết sau.

## Cách Thêm Fields Thủ Công (Hiện Tại - Chính Xác Nhất)

Dựa trên cách đã thực hiện với 4 thuốc trong `ent_oral_nasal_combinations.py`:

1. Đọc file chứa thuốc
2. Tìm vị trí drug dict (ví dụ: `"DrugName": {`)
3. Thêm các fields còn thiếu vào TRƯỚC dấu `},` cuối cùng của drug dict
4. Sử dụng template từ các thuốc đã có đầy đủ fields (ví dụ: Clotrimazole topical trong dermatology.py)

### Template Fields Chuẩn

Xem file `drugs/drug_modules/dermatology.py` (từ dòng 2600+) để xem template đầy đủ của:
- `pharmacokinetics`
- `storage`
- `black_box_warnings`
- `drug_interactions`
- `contraindications` (convert từ list sang dict)
- `pregnancy_lactation`
- `hepatic_adjustment`
- `renal_adjustment`
- `overdose_management`
- `reversal_agents`
- `administration_instructions`
- `references`

## Ưu Tiên

Theo `KE_HOACH_BO_SUNG_FIELDS_THEO_PHIEN.md`:
- **Phiên 1:** 4 thuốc thiếu 10 fields (đã hoàn thành ✅)
- **Phiên 2:** 9 thuốc thiếu 8 fields (ưu tiên tiếp theo)
- **Phiên 3:** 15 thuốc thiếu 7 fields
- ...và tiếp tục

## Lưu Ý

1. **Fields template:** Script tự động tạo fields template với giá trị "Cần tra cứu", cần được cập nhật thông tin chi tiết
2. **Kiểm tra syntax:** Sau khi thêm fields, chạy `read_lints` để kiểm tra lỗi
3. **Backup:** Nên backup file trước khi chỉnh sửa
4. **Review:** Luôn review lại các fields đã thêm để đảm bảo chính xác

