# Tiến độ bổ sung field đầy đủ cho các thuốc (2022-2026)

## Tổng quan

- **Tổng số thuốc**: 186
- **Đã hoàn thành**: 11
- **Còn lại**: 175

## Thuốc đã hoàn thành

### ✅ Amvuttra (vutrisiran)
- **Module**: `miscellaneous/other.py`
- **Năm phê duyệt**: 2022
- **Trạng thái**: ✅ Hoàn thành tất cả các field

### ✅ Relyvrio (sodium phenylbutyrate/taurursodiol)
- **Module**: `miscellaneous/other.py`
- **Năm phê duyệt**: 2022
- **Trạng thái**: ✅ Hoàn thành tất cả các field

### ✅ Journavx (suzetrigine)
- **Module**: `analgesics/opioid_agonist_weaks.py`
- **Năm phê duyệt**: 2025
- **Trạng thái**: ✅ Hoàn thành tất cả các field
- **Các field đã bổ sung**:
  - ✅ side_effects (9 tác dụng phụ)
  - ✅ interactions (3 tương tác)
  - ✅ mechanism_of_action (chi tiết về siRNA và RNAi)
  - ✅ precautions (7 cảnh báo)
  - ✅ pharmacokinetics (đầy đủ 6 subfield)
  - ✅ black_box_warnings (cảnh báo về giảm vitamin A)
  - ✅ monitoring (6 mục theo dõi)
  - ✅ pregnancy_lactation (chi tiết)
  - ✅ hepatic_adjustment (chi tiết)
  - ✅ overdose_management (chi tiết)
  - ✅ administration_instructions (subcutaneous)

### ✅ Enjaymo (sutimlimab-jome)
- **Module**: `antimicrobial/antibiotics/beta_lactams.py`
- **Năm phê duyệt**: 2022
- **Trạng thái**: ✅ Hoàn thành tất cả các field
- **Các field đã bổ sung**:
  - ✅ side_effects (10 tác dụng phụ)
  - ✅ interactions (3 tương tác)
  - ✅ mechanism_of_action (chi tiết về monoclonal antibody ức chế C1s)
  - ✅ precautions (7 cảnh báo)
  - ✅ pharmacokinetics (đầy đủ 6 subfield)
  - ✅ black_box_warnings (không có, nhưng có cảnh báo về nhiễm trùng)
  - ✅ monitoring (7 mục theo dõi)
  - ✅ pregnancy_lactation (chi tiết)
  - ✅ hepatic_adjustment (chi tiết)
  - ✅ overdose_management (chi tiết)
  - ✅ administration_instructions (IV infusion)
  - ✅ Đã sửa route: từ PO → IV

### ✅ Alhemo (concizumab-mtci)
- **Module**: `antimicrobial/antibiotics/beta_lactams.py`
- **Năm phê duyệt**: 2024
- **Trạng thái**: ✅ Hoàn thành tất cả các field
- **Các field đã bổ sung**:
  - ✅ side_effects (8 tác dụng phụ)
  - ✅ interactions (3 tương tác)
  - ✅ mechanism_of_action (chi tiết về monoclonal antibody ức chế TFPI)
  - ✅ precautions (8 cảnh báo)
  - ✅ pharmacokinetics (đầy đủ 6 subfield)
  - ✅ black_box_warnings (không có, nhưng có cảnh báo về huyết khối)
  - ✅ monitoring (7 mục theo dõi)
  - ✅ pregnancy_lactation (chi tiết)
  - ✅ hepatic_adjustment (chi tiết)
  - ✅ overdose_management (chi tiết)
  - ✅ administration_instructions (SC injection)
  - ✅ Đã sửa route: từ PO → SC

### ✅ Exblifep (cefepime/enmetazobactam)
- **Module**: `antimicrobial/antibiotics/beta_lactams.py`
- **Năm phê duyệt**: 2024
- **Trạng thái**: ✅ Hoàn thành tất cả các field
- **Các field đã bổ sung**:
  - ✅ side_effects (9 tác dụng phụ)
  - ✅ interactions (4 tương tác)
  - ✅ mechanism_of_action (chi tiết về cefepime và enmetazobactam)
  - ✅ precautions (8 cảnh báo)
  - ✅ pharmacokinetics (đầy đủ 6 subfield)
  - ✅ black_box_warnings (không có, nhưng có cảnh báo về C. difficile và co giật)
  - ✅ monitoring (7 mục theo dõi)
  - ✅ pregnancy_lactation (chi tiết, Category B)
  - ✅ hepatic_adjustment (chi tiết)
  - ✅ overdose_management (chi tiết)
  - ✅ administration_instructions (IV infusion)
  - ✅ Đã sửa route: từ PO → IV
  - ✅ Đã cập nhật renal_adjustment với liều cụ thể

### ✅ Orlynvah (sulopenem etzadroxil/probenecid)
- **Module**: `antimicrobial/antibiotics/beta_lactams.py`
- **Năm phê duyệt**: 2024
- **Trạng thái**: ✅ Hoàn thành tất cả các field
- **Các field đã bổ sung**:
  - ✅ side_effects (9 tác dụng phụ)
  - ✅ interactions (5 tương tác)
  - ✅ mechanism_of_action (chi tiết về sulopenem và probenecid)
  - ✅ precautions (8 cảnh báo)
  - ✅ pharmacokinetics (đầy đủ 6 subfield)
  - ✅ black_box_warnings (không có, nhưng có cảnh báo về C. difficile)
  - ✅ monitoring (7 mục theo dõi)
  - ✅ pregnancy_lactation (chi tiết, Category C)
  - ✅ hepatic_adjustment (chi tiết)
  - ✅ overdose_management (chi tiết)
  - ✅ administration_instructions (oral với thức ăn)
  - ✅ Đã cập nhật dosage với liều cụ thể (500mg x 2 lần/ngày x 5 ngày)
  - ✅ Đã cập nhật vietnamese_name để bao gồm cả probenecid

### ✅ Blujepa (gepotidacin)
- **Module**: `antimicrobial/antibiotics/beta_lactams.py`
- **Năm phê duyệt**: 2025
- **Trạng thái**: ✅ Hoàn thành tất cả các field
- **Các field đã bổ sung**:
  - ✅ side_effects (9 tác dụng phụ)
  - ✅ interactions (3 tương tác)
  - ✅ mechanism_of_action (chi tiết về triazaacenaphthylene, ức chế DNA gyrase và topoisomerase IV)
  - ✅ precautions (7 cảnh báo)
  - ✅ pharmacokinetics (đầy đủ 6 subfield)
  - ✅ black_box_warnings (không có, nhưng có cảnh báo về C. difficile)
  - ✅ monitoring (6 mục theo dõi)
  - ✅ pregnancy_lactation (chi tiết, Category C)
  - ✅ hepatic_adjustment (chi tiết)
  - ✅ overdose_management (chi tiết)
  - ✅ administration_instructions (oral, có thể với hoặc không có thức ăn)
  - ✅ Đã cập nhật dosage với liều cụ thể (1500mg x 2 lần/ngày x 5 ngày)

### ✅ Defencath (taurolidine/heparin)
- **Module**: `antimicrobial/antibiotics/others.py`
- **Năm phê duyệt**: 2023
- **Trạng thái**: ✅ Hoàn thành tất cả các field
- **Các field đã bổ sung**:
  - ✅ side_effects (5 tác dụng phụ)
  - ✅ interactions (3 tương tác)
  - ✅ mechanism_of_action (chi tiết về taurolidine và heparin)
  - ✅ precautions (7 cảnh báo)
  - ✅ pharmacokinetics (đầy đủ 6 subfield)
  - ✅ black_box_warnings (không có, nhưng có cảnh báo về chảy máu và HIT)
  - ✅ monitoring (6 mục theo dõi)
  - ✅ pregnancy_lactation (chi tiết, Category C)
  - ✅ hepatic_adjustment (chi tiết)
  - ✅ overdose_management (chi tiết, có antidote: protamine sulfate)
  - ✅ administration_instructions (IV lock solution)
  - ✅ Đã cập nhật dosage và vietnamese_name để bao gồm cả heparin
  - ✅ Đã sửa administration: chỉ IV (lock solution)

### ✅ Xolremdi (mavorixafor)
- **Module**: `antimicrobial/antibiotics/others.py`
- **Năm phê duyệt**: 2024
- **Trạng thái**: ✅ Hoàn thành tất cả các field
- **Các field đã bổ sung**:
  - ✅ side_effects (9 tác dụng phụ)
  - ✅ interactions (3 tương tác)
  - ✅ mechanism_of_action (chi tiết về CXCR4 antagonist cho WHIM syndrome)
  - ✅ precautions (6 cảnh báo)
  - ✅ pharmacokinetics (đầy đủ 6 subfield)
  - ✅ black_box_warnings (không có)
  - ✅ monitoring (6 mục theo dõi)
  - ✅ pregnancy_lactation (chi tiết, Category C)
  - ✅ hepatic_adjustment (chi tiết)
  - ✅ overdose_management (chi tiết)
  - ✅ administration_instructions (oral với thức ăn)
  - ✅ Đã cập nhật dosage với liều cụ thể (400mg x 2 lần/ngày)

### ✅ Nuzolvence (zoliflodacin)
- **Module**: `antimicrobial/antibiotics/others.py`
- **Năm phê duyệt**: 2025
- **Trạng thái**: ✅ Hoàn thành tất cả các field
- **Các field đã bổ sung**:
  - ✅ side_effects (9 tác dụng phụ)
  - ✅ interactions (3 tương tác)
  - ✅ mechanism_of_action (chi tiết về spiropyrimidinetrione, ức chế DNA gyrase)
  - ✅ precautions (8 cảnh báo)
  - ✅ pharmacokinetics (đầy đủ 6 subfield)
  - ✅ black_box_warnings (không có, nhưng có cảnh báo về C. difficile)
  - ✅ monitoring (6 mục theo dõi)
  - ✅ pregnancy_lactation (chi tiết, Category C)
  - ✅ hepatic_adjustment (chi tiết)
  - ✅ overdose_management (chi tiết)
  - ✅ administration_instructions (oral, liều duy nhất)
  - ✅ Đã cập nhật dosage với liều cụ thể (3g PO liều duy nhất)

## Thuốc tiếp theo cần bổ sung

Theo thứ tự trong `MANUAL_UPDATE_TEMPLATE.md`:

1. ⏳ **Vivjoa** (oteseconazole) - `antimicrobial/antifungals/azoles.py` - 2022
2. ⏳ **Bimzelx** (bimekizumab) - `antimicrobial/antifungals/azoles.py` - 2023
3. ⏳ **Povtay** (posaconazole) - `antimicrobial/antifungals/azoles.py` - 2024

## Hướng dẫn tiếp tục

1. Chọn thuốc tiếp theo từ danh sách
2. Tìm thông tin từ FDA Drug Labels hoặc DrugBank
3. Cập nhật các field còn thiếu
4. Kiểm tra syntax
5. Cập nhật file này với tiến độ

## Ghi chú

- Tất cả thuốc đã có ghi chú năm phê duyệt trong field `group`
- Ưu tiên bổ sung các thuốc thường dùng trong lâm sàng trước
- Sử dụng `update_drug_fields.py` để hỗ trợ cập nhật
