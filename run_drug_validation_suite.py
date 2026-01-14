"""
Drug Validation Suite - Chạy gộp các kiểm tra dữ liệu thuốc quan trọng.

Mục tiêu:
- Dễ dàng chạy lại toàn bộ kiểm tra chính cho hệ thống thuốc bằng 1 lệnh.

Chạy:
    python run_drug_validation_suite.py
"""

from pathlib import Path
import importlib
import sys


ROOT = Path(__file__).resolve().parent
REPORTS_DIR = ROOT / "reports" / "drugs"
REPORTS_DIR.mkdir(parents=True, exist_ok=True)


def _run_module_entry_point(module_name: str, func_name: str = "main") -> None:
    """Import module và gọi hàm main/entry nếu có."""
    print(f"\n=== Running {module_name}.{func_name}() ===")
    try:
        module = importlib.import_module(module_name)
        func = getattr(module, func_name, None)
        if callable(func):
            func()
        else:
            print(f"[INFO] Module {module_name} không có hàm {func_name}(), bỏ qua.")
    except Exception as exc:  # noqa: BLE001
        print(f"[ERROR] Lỗi khi chạy {module_name}: {exc}")


def main() -> None:
    print("\n" + "=" * 80)
    print("CHAY GỌP CAC KIEM TRA DU LIEU THUOC CHINH".center(80))
    print("=" * 80 + "\n")

    # Đảm bảo project root có trong sys.path
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))

    # 1. Kiểm tra cấu trúc & syntax tổng thể (nếu có)
    for module, entry in [
        ("drugs.validate_all_drugs", "main"),
        ("drugs.comprehensive_drug_audit", "main"),
        ("drugs.data_integrity_checker", "main"),
        ("drugs.field_validator", "main"),
        ("drugs.data_quality_manager", "main"),
    ]:
        _run_module_entry_point(module, entry)

    print("\n" + "=" * 80)
    print("HOAN TAT DRUG VALIDATION SUITE".center(80))
    print("=" * 80 + "\n")
    print("Vui lòng xem thêm các báo cáo JSON/TXT do từng script xuất ra trong thư mục:")
    print(f"  - {REPORTS_DIR}")


if __name__ == "__main__":
    main()

