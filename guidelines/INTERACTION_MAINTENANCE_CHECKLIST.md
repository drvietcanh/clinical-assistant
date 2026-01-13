## Checklist bảo trì dữ liệu tương tác thuốc

1) Kiểm tra tính toàn vẹn dữ liệu
- Chạy `validate_interaction_dataset()` (trong `drugs.interactions_data`) để rà soát thiếu trường, giá trị không hợp lệ.
- Kiểm tra trùng cặp A-B và B-A; ưu tiên lưu một chiều (A, B).

2) Chu kỳ cập nhật (3–6 tháng hoặc khi có cảnh báo mới)
- Thuốc mới thêm vào `DRUG_DATABASE`.
- Cảnh báo an toàn/boxed warning mới (FDA/EMA/MHRA).
- Guideline mới (ACC/AHA/ESC/IDSA/KDIGO/ADA…) liên quan tương tác.

3) Ưu tiên rà soát
- Thuốc kéo dài QT, kháng đông/kháng kết tập, thuốc ICU/gây mê/an thần.
- Thuốc PK nặng (CYP3A4/2C9/2D6/P-gp inhibitor/inducer).
- Bệnh nhân đặc biệt: ICU, suy thận/gan, sản/nhi.

4) Quy trình cập nhật
- Thu thập nguồn: Lexicomp/Micromedex/UpToDate + guideline quốc tế; bổ sung hướng dẫn Bộ Y tế khi có.
- Điền theo template `data/templates/interaction_entry_template.json`.
- Chạy validator, cập nhật `monitoring`/`onset`/`special_populations`.
- Smoke-test trên UI: nhập 3–5 ca điển hình (warfarin + TMP/SMX, amiodarone + levofloxacin, propofol + fentanyl).

5) Ghi nhận thay đổi
- Lưu ý `evidence_level` (high/moderate/low) để ưu tiên cảnh báo.
- Nếu thay đổi quản lý liều, thêm ghi chú ngắn trong `management`.
