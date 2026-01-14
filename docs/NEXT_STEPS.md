# Các Bước Tiếp Theo - Quick Reference

## 1. Kiểm Tra và Sửa Lỗi Syntax Còn Lại

```bash
# Tìm lỗi
python drugs/find_syntax_errors.py

# Xem kết quả
cat drugs/syntax_errors_found.json
```

Nếu còn lỗi, tạo script mới hoặc sửa thủ công.

## 2. Khôi Phục biguanides.py

1. Mở `drugs/drug_modules/diabetes/biguanides.py`
2. Sửa các lỗi syntax còn lại
3. Uncomment trong `drugs/drug_modules/diabetes/__init__.py`:
   ```python
   from .biguanides import BIGUANIDES_DRUGS
   # ...
   **BIGUANIDES_DRUGS,
   ```

## 3. Kiểm Tra DRUG_DATABASE

```bash
python -c "from drugs.drug_database import DRUG_DATABASE; print(f'✅ Loaded {len(DRUG_DATABASE)} drugs')"
```

Nếu OK, tiếp tục. Nếu lỗi, sửa các file còn lỗi syntax.

## 4. Bổ Sung Field Pregnancy (109 thuốc)

### Cách 1: Tự động (nếu có thể)
```bash
python drugs/supplement_pregnancy_auto.py
```

### Cách 2: Thủ công
```bash
python drugs/manual_supplementation_helper.py
```

Chọn option để bổ sung pregnancy field.

## 5. Bổ Sung Các Field Khác

Sử dụng `manual_supplementation_helper.py` cho:
- dosage (1 thuốc)
- side_effects (14 thuốc)
- contraindications (35 thuốc)
- interactions (57 thuốc)
- storage (62 thuốc)

## 6. Cập Nhật Tiến Trình

Sau mỗi bước, cập nhật:
- `drugs/manual_supplementation_progress.json`
- `docs/SUPPLEMENTATION_PROGRESS.md`

---

**Lưu ý:** Luôn backup trước khi sửa file!
