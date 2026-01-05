"""
Script để xóa các file .md trùng lặp và không cần thiết
Giữ lại: README.md, PROJECT_STATUS_AND_ROADMAP.md, và files trong docs/, diseases/, drugs/
"""
import os
import sys
import io
from pathlib import Path
from typing import List, Set
import json
from datetime import datetime

# Fix encoding cho Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# Files cần GIỮ LẠI
FILES_TO_KEEP = {
    'README.md',
    'PROJECT_STATUS_AND_ROADMAP.md',
    # Các file quan trọng khác (nếu cần)
    # 'DRUG_REFERENCE_GUIDE.md',  # Có thể giữ lại nếu cần
    # 'MASTER_GUIDE.md',  # Có thể giữ lại nếu cần
    # 'HOW_TO_ADD_NEW_DRUG.md',  # Có thể giữ lại nếu cần
}

# Thư mục cần GIỮ LẠI (không xóa files trong các thư mục này)
DIRECTORIES_TO_KEEP = {
    'docs',
    'diseases',
    'drugs',
    # Có thể thêm 'content' nếu muốn giữ lại articles
    # 'content',
}

# Patterns để xác định files cần XÓA
DELETE_PATTERNS = [
    'PHASE*_*.md',
    'BAO_CAO_*.md',
    'SUMMARY_*.md',
    'COMPLETE_*.md',
    'FINAL_*.md',
    'TODO_*.md',
    'KE_HOACH_*.md',
    'CONG_VIEC_*.md',
    'FIELD_*.md',  # Trừ PROJECT_STATUS_AND_ROADMAP.md đã được giữ lại
    'DRUG_*.md',  # Có thể giữ lại một số, nhưng xóa các file báo cáo cũ
    'SESSION_*.md',
    'PROGRESS_*.md',
    'IMPLEMENTATION_*.md',
    'OPTIMIZATION_*.md',
    'REFACTORING_*.md',
    'ACHIEVEMENT_*.md',
    'STATUS_*.md',
    'REPORT_*.md',
    'CHECKLIST_*.md',
    'GUIDE_*.md',  # Có thể giữ lại một số, nhưng xóa các guide cũ
    'QUICK_*.md',
    'START_*.md',
    'MASTER_*.md',
    'HOW_TO_*.md',
    'SYSTEM_*.md',
    'ULTIMATE_*.md',
    'INDEX_*.md',
    'CHANGELOG_*.md',
    'CAPITALIZATION_*.md',
    'ERROR_*.md',
    'DECIMAL_*.md',
    'HTML_*.md',
    'FIX_*.md',
    'TEST_*.md',
    'ALL_*.md',
    'NEXT_*.md',
    'CONTINUE_*.md',
    'DANH_SACH_*.md',
    'DE_XUAT_*.md',
    'CAP_NHAT_*.md',
    'BO_SUNG_*.md',
    'AKI_*.md',
    'ACTION_*.md',
    'APP_*.md',
    'CHECKLIST_*.md',
    'COMMIT_*.md',
    'COMPREHENSIVE_*.md',
    'DATABASE_*.md',
    'ENHANCED_*.md',
    'FEATURE_*.md',
    'IMPROVEMENTS_*.md',
    'INTEGRATION_*.md',
    'MODULE_*.md',
    'ORGANIZATION_*.md',
    'REORGANIZATION_*.md',
    'STANDARDIZATION_*.md',
    'STRUCTURE_*.md',
    'THUAT_TOAN_*.md',
    'TIEN_TRINH_*.md',
    'UNIFIED_*.md',
    'WORKFLOW_*.md',
]

def should_keep_file(file_path: Path) -> bool:
    """
    Kiểm tra xem file có nên được giữ lại không
    """
    file_name = file_path.name
    
    # Giữ lại files trong danh sách
    if file_name in FILES_TO_KEEP:
        return True
    
    # Giữ lại files trong các thư mục được chỉ định
    for keep_dir in DIRECTORIES_TO_KEEP:
        if keep_dir in file_path.parts:
            return True
    
    return False

def matches_delete_pattern(file_name: str) -> bool:
    """
    Kiểm tra xem file có khớp với pattern cần xóa không
    """
    import fnmatch
    for pattern in DELETE_PATTERNS:
        if fnmatch.fnmatch(file_name, pattern):
            return True
    return False

def find_md_files(root_dir: Path) -> List[Path]:
    """
    Tìm tất cả file .md trong thư mục
    """
    md_files = []
    for file_path in root_dir.rglob('*.md'):
        # Bỏ qua files trong .git, __pycache__, node_modules, etc.
        if any(skip in file_path.parts for skip in ['.git', '__pycache__', 'node_modules', '.venv', 'venv']):
            continue
        md_files.append(file_path)
    return md_files

def categorize_files(md_files: List[Path]) -> tuple[List[Path], List[Path]]:
    """
    Phân loại files thành: giữ lại và xóa
    """
    files_to_keep = []
    files_to_delete = []
    
    for file_path in md_files:
        if should_keep_file(file_path):
            files_to_keep.append(file_path)
        elif matches_delete_pattern(file_path.name):
            files_to_delete.append(file_path)
        else:
            # Files không khớp pattern, giữ lại để xem xét
            files_to_keep.append(file_path)
    
    return files_to_keep, files_to_delete

def main(dry_run: bool = True):
    """
    Main function
    """
    root_dir = Path.cwd()
    
    print("=" * 70)
    print("CLEANUP DUPLICATE MD FILES")
    print("=" * 70)
    print(f"Root directory: {root_dir}")
    print(f"Mode: {'DRY-RUN' if dry_run else 'DELETE'}")
    print("=" * 70)
    
    # Tìm tất cả file .md
    print("\nĐang tìm tất cả file .md...")
    md_files = find_md_files(root_dir)
    print(f"Tìm thấy {len(md_files)} file .md")
    
    # Phân loại files
    print("\nĐang phân loại files...")
    files_to_keep, files_to_delete = categorize_files(md_files)
    
    print(f"\nFiles sẽ GIỮ LẠI: {len(files_to_keep)}")
    print(f"Files sẽ XÓA: {len(files_to_delete)}")
    
    # Hiển thị files sẽ xóa
    if files_to_delete:
        print("\n" + "=" * 70)
        print("DANH SÁCH FILES SẼ XÓA:")
        print("=" * 70)
        for i, file_path in enumerate(sorted(files_to_delete), 1):
            rel_path = file_path.relative_to(root_dir)
            print(f"{i:4d}. {rel_path}")
        
        # Tạo báo cáo JSON
        report = {
            'timestamp': datetime.now().isoformat(),
            'mode': 'dry_run' if dry_run else 'delete',
            'total_md_files': len(md_files),
            'files_to_keep': len(files_to_keep),
            'files_to_delete': len(files_to_delete),
            'files_to_keep_list': [str(f.relative_to(root_dir)) for f in files_to_keep],
            'files_to_delete_list': [str(f.relative_to(root_dir)) for f in files_to_delete],
        }
        
        report_file = f'cleanup_report_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        print(f"\nBáo cáo đã lưu: {report_file}")
        
        # Xóa files nếu không phải dry-run
        if not dry_run:
            print("\n" + "=" * 70)
            print("ĐANG XÓA FILES...")
            print("=" * 70)
            
            deleted_count = 0
            error_count = 0
            
            for file_path in files_to_delete:
                try:
                    file_path.unlink()
                    deleted_count += 1
                    rel_path = file_path.relative_to(root_dir)
                    print(f"✓ Đã xóa: {rel_path}")
                except Exception as e:
                    error_count += 1
                    rel_path = file_path.relative_to(root_dir)
                    print(f"✗ Lỗi khi xóa {rel_path}: {e}")
            
            print("\n" + "=" * 70)
            print("KẾT QUẢ:")
            print("=" * 70)
            print(f"Đã xóa: {deleted_count} files")
            print(f"Lỗi: {error_count} files")
            print("=" * 70)
        else:
            print("\n" + "=" * 70)
            print("DRY-RUN MODE - Không có file nào bị xóa")
            print("Chạy với --apply để xóa thật")
            print("=" * 70)
    else:
        print("\nKhông có file nào cần xóa!")
    
    # Hiển thị files sẽ giữ lại (top 20)
    if files_to_keep:
        print("\n" + "=" * 70)
        print("FILES SẼ GIỮ LẠI (hiển thị 20 đầu tiên):")
        print("=" * 70)
        for i, file_path in enumerate(sorted(files_to_keep)[:20], 1):
            rel_path = file_path.relative_to(root_dir)
            print(f"{i:4d}. {rel_path}")
        if len(files_to_keep) > 20:
            print(f"... và {len(files_to_keep) - 20} files khác")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Cleanup duplicate MD files')
    parser.add_argument('--apply', action='store_true', help='Thực sự xóa files (mặc định là dry-run)')
    
    args = parser.parse_args()
    
    main(dry_run=not args.apply)

