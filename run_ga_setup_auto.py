"""
Auto-run Google Analytics Setup - Chạy các bước tự động có thể
"""

import os
import json
from pathlib import Path

def print_header(text):
    print("\n" + "=" * 70)
    print(f"  {text}")
    print("=" * 70 + "\n")

def check_and_setup():
    """Kiểm tra và setup tự động những gì có thể"""
    
    print_header("🚀 GOOGLE ANALYTICS API - AUTO SETUP")
    
    print("Đang kiểm tra và thực hiện các bước tự động...\n")
    
    # Bước 1: Kiểm tra requirements
    print("=" * 70)
    print("  BƯỚC 1: KIỂM TRA REQUIREMENTS")
    print("=" * 70)
    
    try:
        import google.analytics.data_v1beta
        print("✅ google-analytics-data: Đã cài đặt")
        requirements_ok = True
    except ImportError:
        print("❌ google-analytics-data: Chưa cài đặt")
        print("\n📦 Cài đặt bằng lệnh:")
        print("   pip install google-analytics-data google-auth google-auth-oauthlib google-auth-httplib2")
        requirements_ok = False
    
    # Bước 2: Tìm file JSON
    print("\n" + "=" * 70)
    print("  BƯỚC 2: TÌM FILE JSON CREDENTIALS")
    print("=" * 70)
    
    json_info = None
    current_dir = Path(".")
    json_files = list(current_dir.glob("*.json"))
    
    # Tìm trong thư mục credentials
    creds_dir = Path("credentials")
    if creds_dir.exists():
        json_files.extend(list(creds_dir.glob("*.json")))
    
    if json_files:
        print(f"✅ Tìm thấy {len(json_files)} file JSON:")
        for f in json_files:
            print(f"   - {f}")
        
        # Thử validate file đầu tiên
        for json_file in json_files:
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                if 'type' in data and data['type'] == 'service_account':
                    print(f"\n✅ File hợp lệ: {json_file}")
                    print(f"   - Project ID: {data.get('project_id', 'N/A')}")
                    print(f"   - Client Email: {data.get('client_email', 'N/A')}")
                    
                    json_info = {
                        'file_path': str(json_file),
                        'project_id': data.get('project_id'),
                        'client_email': data.get('client_email'),
                        'json_content': json.dumps(data, indent=2)
                    }
                    break
            except:
                continue
    else:
        print("⚠️  Chưa tìm thấy file JSON credentials")
        print("   Bạn cần download file JSON từ Google Cloud Console")
    
    # Bước 3: Kiểm tra secrets
    print("\n" + "=" * 70)
    print("  BƯỚC 3: KIỂM TRA STREAMLIT SECRETS")
    print("=" * 70)
    
    secrets_file = Path(".streamlit/secrets.toml")
    if secrets_file.exists():
        print(f"✅ Đã có file: {secrets_file}")
        try:
            import tomllib
            with open(secrets_file, 'rb') as f:
                secrets = tomllib.load(f)
            if 'google_analytics' in secrets:
                print("   ✅ Đã có cấu hình google_analytics")
                if 'service_account_json' in secrets['google_analytics']:
                    print("   ✅ Đã có service_account_json")
                if 'property_id' in secrets['google_analytics']:
                    print(f"   ✅ Đã có property_id: {secrets['google_analytics']['property_id']}")
        except:
            try:
                import tomli as tomllib
                with open(secrets_file, 'rb') as f:
                    secrets = tomllib.load(f)
                if 'google_analytics' in secrets:
                    print("   ✅ Đã có cấu hình google_analytics")
            except:
                print("   ⚠️  Không thể đọc file secrets (cần tomllib hoặc tomli)")
    else:
        print("⚠️  Chưa có file secrets.toml")
        
        # Nếu có JSON info, tạo file secrets
        if json_info:
            print("\n💡 Có thể tạo file secrets.toml tự động")
            print("   (Cần Property ID để hoàn thành)")
    
    # Bước 4: Tạo template nếu chưa có
    print("\n" + "=" * 70)
    print("  BƯỚC 4: TẠO TEMPLATE SECRETS")
    print("=" * 70)
    
    template_file = Path(".streamlit/secrets.toml.example")
    if not template_file.exists():
        print("⚠️  Chưa có template")
    else:
        print("✅ Đã có template: .streamlit/secrets.toml.example")
    
    # Tổng kết
    print("\n" + "=" * 70)
    print("  TỔNG KẾT & HƯỚNG DẪN")
    print("=" * 70)
    
    print("\n📋 CÁC BƯỚC BẠN CẦN LÀM THỦ CÔNG:")
    print("\n1️⃣  GOOGLE CLOUD CONSOLE:")
    print("   - Truy cập: https://console.cloud.google.com/")
    print("   - Tạo Project mới")
    print("   - Enable 'Google Analytics Data API'")
    print("   - Tạo Service Account")
    print("   - Download JSON credentials file")
    
    print("\n2️⃣  GOOGLE ANALYTICS:")
    print("   - Truy cập: https://analytics.google.com/")
    print("   - Admin → Property Access Management")
    print("   - Thêm Service Account email với quyền 'Viewer'")
    print("   - Lấy Property ID (số, không phải G-XXX)")
    
    print("\n3️⃣  CẤU HÌNH VÀO APP:")
    if json_info:
        print(f"   ✅ Đã có file JSON: {json_info['file_path']}")
        print(f"   📧 Service Account Email: {json_info['client_email']}")
        print("\n   Bạn cần:")
        print("   - Thêm email này vào Google Analytics Property")
        print("   - Lấy Property ID")
        print("   - Tạo file .streamlit/secrets.toml với nội dung:")
        print("\n" + "-" * 70)
        print(f"""[google_analytics]
service_account_json = '''
{json_info['json_content']}
'''
property_id = "properties/YOUR_PROPERTY_ID"
""")
        print("-" * 70)
    else:
        print("   ⚠️  Chưa có file JSON")
        print("   - Download file JSON từ Google Cloud Console")
        print("   - Đặt vào thư mục hiện tại hoặc thư mục credentials/")
        print("   - Chạy lại script này")
    
    print("\n" + "=" * 70)
    print("  HƯỚNG DẪN CHI TIẾT")
    print("=" * 70)
    print("\n📚 Xem hướng dẫn chi tiết:")
    print("   - docs/HUONG_DAN_GOOGLE_CLOUD_STEP_BY_STEP.md")
    print("   - docs/GOOGLE_ANALYTICS_API_SETUP.md")
    
    print("\n💡 Hoặc chạy interactive setup:")
    print("   python setup_ga_interactive.py")
    print("   (Cần chạy trong terminal có thể nhận input)")
    
    print("\n" + "=" * 70)
    print("  KIỂM TRA SAU KHI SETUP")
    print("=" * 70)
    print("\nSau khi hoàn thành các bước trên, chạy:")
    print("   python setup_ga_api.py auto")
    print("\nĐể kiểm tra cấu hình có đúng không.\n")

if __name__ == "__main__":
    check_and_setup()

