#!/bin/bash
# Script để kiểm tra và sửa số thập phân dư không có ý nghĩa lâm sàng

echo "========================================"
echo "KIỂM TRA SỐ THẬP PHÂN DƯ"
echo "========================================"
echo ""

# Kiểm tra xem có tham số không
MODE=${1:-check}

case "$MODE" in
    check)
        echo "[MODE: CHECK] Chỉ kiểm tra và tạo báo cáo..."
        python utils/fix_decimal_precision.py --check --report DECIMAL_PRECISION_REPORT.md
        ;;
    fix)
        echo "[MODE: FIX] Tự động sửa các lỗi..."
        python utils/fix_decimal_precision.py --fix --report DECIMAL_PRECISION_REPORT.md
        ;;
    dry-run)
        echo "[MODE: DRY-RUN] Xem sẽ sửa gì nhưng không sửa thật..."
        python utils/fix_decimal_precision.py --fix --dry-run --report DECIMAL_PRECISION_REPORT.md
        ;;
    *)
        echo "Usage:"
        echo "  ./fix_decimal_precision.sh check    - Chỉ kiểm tra và báo cáo"
        echo "  ./fix_decimal_precision.sh fix      - Tự động sửa"
        echo "  ./fix_decimal_precision.sh dry-run  - Xem sẽ sửa gì nhưng không sửa thật"
        exit 1
        ;;
esac

echo ""
echo "========================================"
echo "HOÀN THÀNH"
echo "========================================"

