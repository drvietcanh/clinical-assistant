## Hướng dẫn nhập liệu tương tác thuốc (full-detail)

Mục tiêu: dữ liệu thống nhất, đủ thông tin lâm sàng, dễ kiểm tra tự động.

### 1. Schema chuẩn (key ➜ mô tả)
- `severity`: `Contraindicated` | `Major` | `Moderate` | `Minor`
- `mechanism`: Mô tả ngắn (PK/PD).
- `mechanism_type`: `pharmacokinetic` | `pharmacodynamic` | `mixed` | `unknown`
- `description`/`effect`: Hậu quả lâm sàng chính.
- `onset`: `rapid` | `delayed` | `accumulation` | `unknown`
- `management`: Hướng dẫn xử trí cụ thể (tránh/giảm liều/theo dõi).
- `monitoring`: Danh sách chỉ số cần theo dõi (ECG, điện giải, INR...).
- `special_populations`: Tag bối cảnh: `ICU`, `pediatrics`, `pregnancy`, `renal_impairment`, `hepatic_impairment`.
- `evidence_level`: `high` | `moderate` | `low`.
- `references`: Danh sách nguồn (tối thiểu 1), có thể là tên guideline hoặc tài liệu.

### 2. Mức độ nghiêm trọng (cách gán)
- `Contraindicated`: chống chỉ định tuyệt đối hoặc nguy cơ tử vong cao (MAOI + SSRI, QT nặng…).
- `Major`: nguy cơ nghiêm trọng cần tránh/giảm liều lớn/giám sát chặt (warfarin + TMP/SMX, amiodarone + macrolide).
- `Moderate`: cần điều chỉnh liều hoặc theo dõi (ACEI + NSAID, ondansetron + quinolone).
- `Minor`: ít ý nghĩa lâm sàng, chủ yếu ghi chú theo dõi.

### 3. Quy trình nhập từng tương tác
1. Xác định cặp thuốc/lớp (A-B). Dùng tên chuẩn trong `DRUG_CLASS_MAPPINGS` nếu là tương tác theo lớp.
2. Điền `severity`, `mechanism`, `description`.
3. Chuyển thành `management` cụ thể: tránh/giảm liều, khoảng cách liều, cần theo dõi gì, tần suất.
4. Gắn `monitoring` (ECG, INR, K/Mg, nồng độ thuốc), `onset` và `mechanism_type`.
5. Gắn `special_populations` khi liên quan (ICU, suy tạng, sản/nhi).
6. Thêm tối thiểu 1 `reference`, ưu tiên guideline/boxed warning.

### 4. Quy tắc đặt tên & lớp
- Ưu tiên tên hoạt chất chuẩn; nếu tương tác theo lớp, dùng khóa lớp đã khai báo ở `DRUG_CLASS_MAPPINGS` (ví dụ: `ACE Inhibitor`, `ARB`, `QT Prolonging`, `Macrolide`, `Azole Antifungal`, `Opioid`, `Benzodiazepine`).
- Không viết tắt khó hiểu; tránh tên biệt dược trừ khi đó là dạng phối hợp duy nhất.

### 5. Chất lượng & kiểm tra
- Bắt buộc: `severity`, `mechanism`, `description`/`effect`, `management`, `references`.
- Chạy validator: `validate_interaction_dataset()` trong `drugs.interactions_data`.
- Tránh trùng cặp A-B và B-A; nếu là lớp-lớp, đảm bảo không trùng với thuốc-thuốc cùng nội dung.

### 6. Ưu tiên nhập (Pha 1-3)
- Pha 1 (nguy cơ cao): kéo dài QT (amiodarone + macrolide/quinolone/antipsychotic/ondansetron), kháng đông + thuốc ức chế/NSAID, ICU an thần/gây mê + ức chế CYP/thuốc ức chế hô hấp.
- Pha 2: tim mạch thường gặp (ACEI/ARB/beta-blocker/CCB/diuretic/statin), đái tháo đường, tâm thần kinh (SSRI/SNRI/antipsychotic/antiepileptic).
- Pha 3: ARV, chống lao, ung thư/ức chế miễn dịch, sản/nhi chuyên biệt.

### 7. Mẹo nhập nhanh
- Dùng template `data/templates/interaction_entry_template.json` để copy/paste.
- Luôn thêm `monitoring` và `onset` để hỗ trợ cảnh báo thời gian thực.
- Nếu nguồn mâu thuẫn: chọn nguồn mạnh nhất (guideline/boxed warning) và ghi chú trong `references`.
