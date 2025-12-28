#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script tự động áp dụng các sửa lỗi vào enhanced_fields_overrides.py
(Cẩn thận: Script này sẽ sửa trực tiếp vào file!)
"""

import os
import shutil
from datetime import datetime

def backup_file(file_path: str) -> str:
    """Backup file"""
    if not os.path.exists(file_path):
        print(f"❌ File không tồn tại: {file_path}")
        return None
    
    backup_path = f"{file_path}.backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    shutil.copy2(file_path, backup_path)
    print(f"✅ Đã backup: {backup_path}")
    return backup_path

def check_auto_fix_code_exists() -> bool:
    """Kiểm tra file auto_fix_code_to_add.py có tồn tại không"""
    return os.path.exists('auto_fix_code_to_add.py')

def read_auto_fix_code() -> str:
    """Đọc code từ auto_fix_code_to_add.py"""
    try:
        with open('auto_fix_code_to_add.py', 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"❌ Lỗi khi đọc file: {e}")
        return None

def apply_to_file(target_file: str, code: str, dry_run: bool = False) -> bool:
    """Áp dụng code vào file"""
    if not os.path.exists(target_file):
        print(f"❌ File không tồn tại: {target_file}")
        return False
    
    if dry_run:
        print("🔍 DRY RUN - Chỉ xem preview, không sửa file")
        print(f"\nSẽ thêm vào cuối file {target_file}:")
        print("=" * 80)
        print(code)
        print("=" * 80)
        return True
    
    # Backup trước
    backup_path = backup_file(target_file)
    if not backup_path:
        return False
    
    # Đọc file hiện tại
    try:
        with open(target_file, 'r', encoding='utf-8') as f:
            current_content = f.read()
    except Exception as e:
        print(f"❌ Lỗi khi đọc file: {e}")
        return False
    
    # Kiểm tra xem code đã có chưa
    if code.strip() in current_content:
        print("⚠️  Code đã có trong file, bỏ qua")
        return True
    
    # Thêm code vào cuối
    try:
        with open(target_file, 'a', encoding='utf-8') as f:
            f.write('\n\n')
            f.write(code)
        print(f"✅ Đã thêm code vào {target_file}")
        return True
    except Exception as e:
        print(f"❌ Lỗi khi ghi file: {e}")
        # Restore backup
        if backup_path:
            shutil.copy2(backup_path, target_file)
            print(f"✅ Đã khôi phục từ backup")
        return False

def main():
    """Hàm chính"""
    import sys
    
    print("=" * 100)
    print("TỰ ĐỘNG ÁP DỤNG CÁC SỬA LỖI VÀO FILE")
    print("=" * 100)
    print()
    
    # Kiểm tra file auto_fix_code_to_add.py
    if not check_auto_fix_code_exists():
        print("❌ Không tìm thấy auto_fix_code_to_add.py")
        print("   Vui lòng chạy apply_auto_fixes_to_file.py trước")
        return
    
    # Đọc code
    print("Đang đọc code từ auto_fix_code_to_add.py...")
    code = read_auto_fix_code()
    if not code:
        return
    
    # File đích
    target_file = "drugs/enhanced_fields_overrides.py"
    
    # Kiểm tra dry run
    dry_run = '--dry-run' in sys.argv or '-n' in sys.argv
    
    if dry_run:
        print("\n🔍 CHẾ ĐỘ DRY RUN - Chỉ xem preview")
    else:
        print("\n⚠️  CẢNH BÁO: Script này sẽ sửa trực tiếp vào file!")
        print(f"   File đích: {target_file}")
        response = input("   Bạn có chắc chắn muốn tiếp tục? (yes/no): ")
        if response.lower() not in ['yes', 'y']:
            print("❌ Đã hủy")
            return
    
    # Áp dụng
    success = apply_to_file(target_file, code, dry_run=dry_run)
    
    if success:
        if not dry_run:
            print("\n✅ Hoàn thành!")
            print("\n💡 Bước tiếp theo:")
            print("   1. Kiểm tra file đã được sửa đúng chưa")
            print("   2. Chạy lại validation:")
            print("      python comprehensive_drug_validation.py")
            print("   3. Nếu mọi thứ OK, commit changes")
        else:
            print("\n💡 Để áp dụng thực sự, chạy lại không có --dry-run:")
            print("   python auto_apply_fixes.py")
    else:
        print("\n❌ Có lỗi xảy ra, vui lòng kiểm tra")

if __name__ == '__main__':
    main()

