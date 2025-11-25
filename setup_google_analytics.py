"""
Script hỗ trợ cấu hình Google Analytics
Chạy script này để kiểm tra và cấu hình Google Analytics ID
"""

import os
import sys
from pathlib import Path

def check_google_analytics_config():
    """Kiểm tra cấu hình Google Analytics hiện tại"""
    print("=" * 60)
    print("🔍 KIỂM TRA CẤU HÌNH GOOGLE ANALYTICS")
    print("=" * 60)
    print()
    
    # Kiểm tra environment variable
    env_id = os.getenv("GOOGLE_ANALYTICS_ID")
    if env_id:
        print(f"✅ Environment Variable: {env_id}")
    else:
        print("❌ Environment Variable: Chưa được set")
    
    # Kiểm tra config file
    config_file = Path(__file__).parent / "config" / "app_config.py"
    if config_file.exists():
        with open(config_file, "r", encoding="utf-8") as f:
            content = f.read()
            if 'google_analytics_id' in content:
                # Tìm giá trị trong config
                import re
                match = re.search(r'"google_analytics_id":\s*os\.getenv\([^,]+,\s*"([^"]+)"\)', content)
                if match:
                    default_id = match.group(1)
                    print(f"📝 Config File Default: {default_id}")
                    if default_id == "G-XXXXXXXXXX":
                        print("   ⚠️  Vẫn đang dùng placeholder ID")
                    else:
                        print("   ✅ Đã có ID thực tế trong config")
    else:
        print("❌ Config file không tồn tại")
    
    print()
    print("=" * 60)
    
    # Kết luận
    if env_id and env_id != "G-XXXXXXXXXX":
        print("✅ Google Analytics đã được cấu hình qua Environment Variable")
        return True
    elif env_id is None:
        print("⚠️  Chưa cấu hình Google Analytics")
        print()
        print("📋 HƯỚNG DẪN:")
        print("1. Lấy Measurement ID từ Google Analytics (dạng G-XXXXXXXXXX)")
        print("2. Chọn một trong các cách sau:")
        print()
        print("   Cách 1: Set Environment Variable")
        print("   Windows PowerShell:")
        print('   $env:GOOGLE_ANALYTICS_ID="G-XXXXXXXXXX"')
        print()
        print("   Cách 2: Sửa config/app_config.py")
        print("   Thay 'G-XXXXXXXXXX' bằng ID thực tế của bạn")
        print()
        return False
    else:
        print("⚠️  Google Analytics ID vẫn là placeholder")
        return False


def interactive_setup():
    """Cấu hình tương tác"""
    print()
    print("=" * 60)
    print("⚙️  CẤU HÌNH GOOGLE ANALYTICS")
    print("=" * 60)
    print()
    
    print("Nhập Google Analytics Measurement ID của bạn:")
    print("(Format: G-XXXXXXXXXX, hoặc nhấn Enter để bỏ qua)")
    print()
    
    ga_id = input("Google Analytics ID: ").strip()
    
    if not ga_id:
        print("❌ Đã hủy cấu hình")
        return
    
    # Validate format
    if not ga_id.startswith("G-") or len(ga_id) != 12:
        print("⚠️  Cảnh báo: ID không đúng format (G-XXXXXXXXXX)")
        confirm = input("Bạn có chắc muốn tiếp tục? (y/n): ").strip().lower()
        if confirm != 'y':
            return
    
    # Cập nhật config file
    config_file = Path(__file__).parent / "config" / "app_config.py"
    if config_file.exists():
        with open(config_file, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Thay thế placeholder
        import re
        pattern = r'"google_analytics_id":\s*os\.getenv\([^,]+,\s*"G-XXXXXXXXXX"\)'
        replacement = f'"google_analytics_id": os.getenv("GOOGLE_ANALYTICS_ID", "{ga_id}")'
        
        new_content = re.sub(pattern, replacement, content)
        
        if new_content != content:
            with open(config_file, "w", encoding="utf-8") as f:
                f.write(new_content)
            print()
            print(f"✅ Đã cập nhật config file với ID: {ga_id}")
            print()
            print("📝 Lưu ý: Bạn cần restart ứng dụng Streamlit để áp dụng thay đổi")
        else:
            print("⚠️  Không tìm thấy placeholder để thay thế")
            print("   Vui lòng kiểm tra file config/app_config.py thủ công")
    else:
        print("❌ Không tìm thấy file config/app_config.py")


if __name__ == "__main__":
    # Kiểm tra cấu hình hiện tại
    is_configured = check_google_analytics_config()
    
    # Nếu chưa cấu hình, hỏi có muốn cấu hình không
    if not is_configured:
        print()
        try:
            choice = input("Bạn có muốn cấu hình ngay bây giờ? (y/n): ").strip().lower()
            if choice == 'y':
                interactive_setup()
            else:
                print()
                print("📚 Xem hướng dẫn chi tiết tại: docs/GOOGLE_ANALYTICS_SETUP.md")
        except (EOFError, KeyboardInterrupt):
            # Non-interactive mode hoặc bị interrupt
            print()
            print("📚 Xem hướng dẫn chi tiết tại: docs/GOOGLE_ANALYTICS_SETUP.md")
            print()
            print("💡 TIP: Chạy script này trong terminal để cấu hình tương tác")
    
    print()
    print("=" * 60)

