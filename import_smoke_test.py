"""
Import smoke test for core modules.

Goal:
- Phát hiện nhanh lỗi SyntaxError / ImportError ở các module chính
- Ghi kết quả ra file log để xem lại

Chạy:
    python import_smoke_test.py
"""

import importlib
import pkgutil
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent
REPORTS_DIR = ROOT_DIR / "reports"
REPORTS_DIR.mkdir(exist_ok=True)


MODULE_PACKAGES = [
    "scores",
    "antibiotics",
    "drugs",
    "diseases",
    "critical_care",
    "diagnosis",
    "components",
    "config",
]


def iter_modules_in_package(package_name: str):
    """Yield full module names for all .py modules in a package (recursive)."""
    try:
        pkg = importlib.import_module(package_name)
    except Exception as exc:  # noqa: BLE001
        yield package_name, exc
        return

    if not hasattr(pkg, "__path__"):
        # Single module, not a package
        return

    for finder, name, ispkg in pkgutil.walk_packages(pkg.__path__, pkg.__name__ + "."):
        full_name = name
        yield full_name, None


def run_import_smoke_test():
    failures = []
    success_count = 0

    for package in MODULE_PACKAGES:
        for module_name, initial_error in iter_modules_in_package(package):
            if initial_error is not None:
                failures.append((module_name, initial_error))
                continue

            try:
                importlib.import_module(module_name)
                success_count += 1
            except Exception as exc:  # noqa: BLE001
                failures.append((module_name, exc))

    log_file = REPORTS_DIR / "import_smoke_errors.log"
    with log_file.open("w", encoding="utf-8") as f:
        f.write(f"=== Import Smoke Test ===\n")
        f.write(f"Total successful imports: {success_count}\n")
        f.write(f"Total failures: {len(failures)}\n\n")

        for module_name, exc in failures:
            f.write(f"[FAIL] {module_name}: {type(exc).__name__}: {exc}\n")

    print(f"[import_smoke_test] Completed. Success: {success_count}, Failures: {len(failures)}")
    print(f"[import_smoke_test] Log written to: {log_file}")


if __name__ == "__main__":
    run_import_smoke_test()

