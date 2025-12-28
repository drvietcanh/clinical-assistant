"""
Script tổng hợp để sửa tất cả lỗi viết hoa tiếng Việt
Chạy cả quick_fix và deep_scan để đảm bảo không bỏ sót lỗi nào
"""

import subprocess
import sys

def run_script(script_name, apply=False):
    """Chạy một script và hiển thị kết quả"""
    print(f"\n{'='*70}")
    print(f"🔧 Chạy: {script_name}")
    print(f"{'='*70}\n")
    
    cmd = [sys.executable, script_name]
    if apply:
        cmd.append("--apply")
    
    result = subprocess.run(cmd, capture_output=False, text=True)
    return result.returncode == 0

def main():
    """Main function"""
    import sys
    
    apply = False
    if len(sys.argv) > 1 and sys.argv[1] == "--apply":
        apply = True
        print("⚠️  CHẾ ĐỘ SỬA FILE - Các thay đổi sẽ được lưu!\n")
    else:
        print("🔍 CHẾ ĐỘ DRY RUN - Chỉ báo cáo, không sửa file\n")
        print("💡 Để áp dụng thay đổi, chạy: python fix_all_vietnamese_caps.py --apply\n")
    
    print("=" * 70)
    print("🔧 SỬA TẤT CẢ LỖI VIẾT HOA TIẾNG VIỆT - TỔNG HỢP")
    print("=" * 70)
    print()
    
    # Chạy quick fix trước
    print("📌 Bước 1: Quét nhanh các pattern phổ biến...")
    success1 = run_script("quick_fix_vietnamese_caps.py", apply)
    
    if not success1:
        print("❌ Lỗi khi chạy quick_fix_vietnamese_caps.py")
        return
    
    # Chạy deep scan sau
    print("\n📌 Bước 2: Quét sâu các pattern còn sót lại...")
    success2 = run_script("deep_scan_vietnamese_caps.py", apply)
    
    if not success2:
        print("❌ Lỗi khi chạy deep_scan_vietnamese_caps.py")
        return
    
    # Chạy ultra deep scan cuối cùng
    print("\n📌 Bước 3: Quét cực kỳ chi tiết các pattern còn sót...")
    success3 = run_script("ultra_deep_scan_vietnamese_caps.py", apply)
    
    if not success3:
        print("❌ Lỗi khi chạy ultra_deep_scan_vietnamese_caps.py")
        return
    
    # Chạy comprehensive scan để đảm bảo không bỏ sót
    print("\n📌 Bước 4: Quét toàn diện các context đặc biệt...")
    success4 = run_script("comprehensive_scan_vietnamese_caps.py", apply)
    
    if not success4:
        print("❌ Lỗi khi chạy comprehensive_scan_vietnamese_caps.py")
        return
    
    # Tóm tắt
    print("\n" + "=" * 70)
    print("✅ HOÀN THÀNH!")
    print("=" * 70)
    print()
    print("Đã chạy cả bốn script:")
    print("  1. quick_fix_vietnamese_caps.py - Sửa các pattern phổ biến")
    print("  2. deep_scan_vietnamese_caps.py - Quét sâu các pattern còn sót")
    print("  3. ultra_deep_scan_vietnamese_caps.py - Quét cực kỳ chi tiết")
    print("  4. comprehensive_scan_vietnamese_caps.py - Quét toàn diện")
    print()
    
    if apply:
        print("✅ Tất cả các lỗi viết hoa đã được sửa!")
    else:
        print("💡 Chạy với --apply để áp dụng các thay đổi")
    print()

if __name__ == "__main__":
    main()

