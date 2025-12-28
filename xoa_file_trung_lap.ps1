# Script xóa các file .md trùng lặp về bổ sung fields cho thuốc
# Ngày tạo: 2025-12-28

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "XOA CAC FILE TRUNG LAP" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Danh sách file cần xóa
$filesToDelete = @(
    "TONG_KET_FINAL_BO_SUNG_FIELDS.md",
    "KET_QUA_CUOI_CUNG_BO_SUNG_FIELDS.md",
    "BAO_CAO_CUOI_CUNG_BO_SUNG_FIELDS.md",
    "BAO_CAO_TONG_KET_BO_SUNG_FIELDS_FINAL.md",
    "BAO_CAO_TONG_KET_BO_SUNG_FIELDS.md",
    "BAO_CAO_BO_SUNG_FIELDS_THUOC.md",
    "KE_HOACH_BO_SUNG_FIELDS_THEO_PHIEN.md",
    "DANH_SACH_THUOC_CAN_BO_SUNG_2025_02_05.md",
    "KE_HOACH_KIEM_TRA_FIELDS_THUOC_CON_THIEU.md",
    "BAO_CAO_KIEM_TRA_FIELDS_TAT_CA_THUOC.md",
    "BAO_CAO_KIEM_TRA_FIELDS_THUOC_MOI.md"
)

$deletedCount = 0
$notFoundCount = 0

# Xóa từng file
foreach ($file in $filesToDelete) {
    if (Test-Path $file) {
        try {
            Remove-Item $file -Force
            Write-Host "  [✓] Đã xóa: $file" -ForegroundColor Green
            $deletedCount++
        } catch {
            Write-Host "  [✗] Lỗi khi xóa: $file - $($_.Exception.Message)" -ForegroundColor Red
        }
    } else {
        Write-Host "  [!] Không tìm thấy: $file" -ForegroundColor Yellow
        $notFoundCount++
    }
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "KET QUA:" -ForegroundColor Cyan
Write-Host "  - Đã xóa: $deletedCount file" -ForegroundColor Green
Write-Host "  - Không tìm thấy: $notFoundCount file" -ForegroundColor Yellow
Write-Host "  - Tổng cộng: $($filesToDelete.Count) file" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Hoàn thành! Các file trùng lặp đã được xóa." -ForegroundColor Green
Write-Host "File chính còn lại: BAO_CAO_TONG_KET_100_PERCENT.md" -ForegroundColor Cyan

