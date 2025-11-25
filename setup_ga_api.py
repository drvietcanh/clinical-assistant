"""
Script hỗ trợ cấu hình Google Analytics API
Hướng dẫn từng bước và kiểm tra cấu hình
"""

import os
import json
from pathlib import Path

def print_header(text):
    """In header đẹp"""
    print("\n" + "=" * 70)
    print(f"  {text}")
    print("=" * 70 + "\n")

def check_requirements():
    """Kiểm tra các package cần thiết"""
    print_header("🔍 KIỂM TRA REQUIREMENTS")
    
    try:
        import google.analytics.data_v1beta
        print("✅ google-analytics-data: Đã cài đặt")
        return True
    except ImportError:
        print("❌ google-analytics-data: Chưa cài đặt")
        print("\n📦 Cài đặt bằng lệnh:")
        print("   pip install google-analytics-data google-auth google-auth-oauthlib google-auth-httplib2")
        return False

def check_credentials():
    """Kiểm tra credentials"""
    print_header("🔑 KIỂM TRA CREDENTIALS")
    
    # Kiểm tra environment variable
    creds_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
    if creds_path and os.path.exists(creds_path):
        print(f"✅ Environment Variable: {creds_path}")
        try:
            with open(creds_path, 'r') as f:
                creds = json.load(f)
                print(f"   - Project ID: {creds.get('project_id', 'N/A')}")
                print(f"   - Client Email: {creds.get('client_email', 'N/A')}")
                return True
        except Exception as e:
            print(f"   ❌ Lỗi đọc file: {e}")
            return False
    else:
        print("❌ Environment Variable: Chưa được set")
        print("   Set bằng: $env:GOOGLE_APPLICATION_CREDENTIALS='path/to/file.json'")
    
    # Kiểm tra Streamlit secrets
    try:
        import streamlit as st
        if hasattr(st, 'secrets') and 'google_analytics' in st.secrets:
            ga_secrets = st.secrets['google_analytics']
            if 'service_account_json' in ga_secrets:
                print("✅ Streamlit Secrets: Đã có service_account_json")
                try:
                    creds = json.loads(ga_secrets['service_account_json'])
                    print(f"   - Project ID: {creds.get('project_id', 'N/A')}")
                    print(f"   - Client Email: {creds.get('client_email', 'N/A')}")
                    return True
                except:
                    print("   ❌ Lỗi parse JSON")
            elif 'service_account_path' in ga_secrets:
                path = ga_secrets['service_account_path']
                if os.path.exists(path):
                    print(f"✅ Streamlit Secrets: Đã có service_account_path: {path}")
                    return True
                else:
                    print(f"❌ Streamlit Secrets: File không tồn tại: {path}")
        else:
            print("❌ Streamlit Secrets: Chưa có google_analytics config")
    except:
        print("⚠️  Không thể kiểm tra Streamlit secrets (chạy trong Streamlit app)")
    
    return False

def check_property_id():
    """Kiểm tra Property ID"""
    print_header("🆔 KIỂM TRA PROPERTY ID")
    
    # Kiểm tra environment variable
    prop_id = os.getenv('GOOGLE_ANALYTICS_PROPERTY_ID')
    if prop_id:
        print(f"✅ Environment Variable: {prop_id}")
        if not prop_id.startswith('properties/'):
            print(f"   ⚠️  Format nên là: properties/{prop_id}")
        return True
    
    # Kiểm tra Streamlit secrets
    try:
        import streamlit as st
        if hasattr(st, 'secrets') and 'google_analytics' in st.secrets:
            ga_secrets = st.secrets['google_analytics']
            if 'property_id' in ga_secrets:
                prop_id = ga_secrets['property_id']
                print(f"✅ Streamlit Secrets: {prop_id}")
                if not prop_id.startswith('properties/'):
                    print(f"   ⚠️  Format nên là: properties/{prop_id}")
                return True
    except:
        pass
    
    print("❌ Property ID: Chưa được cấu hình")
    print("\n📋 Cách lấy Property ID:")
    print("   1. Vào Google Analytics: https://analytics.google.com/")
    print("   2. Admin → Property Settings")
    print("   3. Copy Property ID (dạng số, ví dụ: 123456789)")
    print("   4. Format: properties/123456789")
    
    return False

def test_api_connection():
    """Test kết nối API"""
    print_header("🧪 TEST KẾT NỐI API")
    
    if not check_requirements():
        print("❌ Không thể test - thiếu package")
        return False
    
    try:
        from components.google_analytics_api import (
            get_ga_credentials,
            get_ga_property_id,
            get_analytics_data
        )
        
        credentials = get_ga_credentials()
        property_id = get_ga_property_id()
        
        if not credentials:
            print("❌ Không tìm thấy credentials")
            return False
        
        if not property_id:
            print("❌ Không tìm thấy Property ID")
            return False
        
        print(f"✅ Credentials: OK")
        print(f"✅ Property ID: {property_id}")
        print("\n🔄 Đang test kết nối...")
        
        data = get_analytics_data(property_id, credentials, days=7)
        
        if data:
            print("\n✅ KẾT NỐI THÀNH CÔNG!")
            print(f"   - Users (7 ngày): {data['total_users']:,}")
            print(f"   - Sessions: {data['total_sessions']:,}")
            print(f"   - Pageviews: {data['total_pageviews']:,}")
            print(f"   - Realtime Users: {data['realtime_users']}")
            return True
        else:
            print("❌ Không thể lấy dữ liệu")
            print("   Kiểm tra:")
            print("   1. Service Account đã được thêm vào Google Analytics Property chưa?")
            print("   2. Property ID có đúng không?")
            print("   3. Google Analytics Data API đã được enable chưa?")
            return False
            
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        return False

def create_secrets_template():
    """Tạo template cho Streamlit secrets"""
    print_header("📝 TẠO TEMPLATE STREAMLIT SECRETS")
    
    template = """# Streamlit Secrets Template
# Copy nội dung này vào .streamlit/secrets.toml (local) hoặc Streamlit Cloud Secrets

[google_analytics]
# Option 1: Paste toàn bộ nội dung JSON file vào đây (khuyến nghị)
service_account_json = '''
{
  "type": "service_account",
  "project_id": "your-project-id",
  "private_key_id": "...",
  "private_key": "-----BEGIN PRIVATE KEY-----\\n...\\n-----END PRIVATE KEY-----\\n",
  "client_email": "analytics-reader@your-project-id.iam.gserviceaccount.com",
  "client_id": "...",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "..."
}
'''

# Option 2: Hoặc chỉ định path đến file JSON (chỉ dùng cho local)
# service_account_path = "path/to/ga-service-account.json"

# Property ID (format: properties/123456789)
property_id = "properties/123456789"
"""
    
    secrets_file = Path(".streamlit") / "secrets.toml.example"
    secrets_file.parent.mkdir(exist_ok=True)
    
    with open(secrets_file, "w", encoding="utf-8") as f:
        f.write(template)
    
    print(f"✅ Đã tạo template tại: {secrets_file}")
    print("\n📋 Hướng dẫn:")
    print("   1. Copy file này thành .streamlit/secrets.toml")
    print("   2. Điền thông tin credentials và property_id")
    print("   3. KHÔNG commit file secrets.toml lên GitHub!")

def print_setup_guide():
    """In hướng dẫn setup"""
    print_header("📚 HƯỚNG DẪN SETUP")
    
    print("""
🔧 CÁC BƯỚC SETUP GOOGLE ANALYTICS API:

1️⃣  TẠO GOOGLE CLOUD PROJECT
   - Truy cập: https://console.cloud.google.com/
   - Tạo project mới hoặc chọn project hiện có

2️⃣  ENABLE GOOGLE ANALYTICS DATA API
   - APIs & Services → Library
   - Tìm "Google Analytics Data API" → Enable

3️⃣  TẠO SERVICE ACCOUNT
   - APIs & Services → Credentials
   - Create Credentials → Service Account
   - Đặt tên: "analytics-reader"
   - Create and Continue → Done

4️⃣  DOWNLOAD JSON CREDENTIALS
   - Click vào Service Account vừa tạo
   - Tab Keys → Add Key → Create new key → JSON
   - Download file JSON về máy

5️⃣  THÊM SERVICE ACCOUNT VÀO GOOGLE ANALYTICS
   - Vào Google Analytics: https://analytics.google.com/
   - Admin → Property Access Management
   - Add users → Nhập email Service Account (từ file JSON)
   - Quyền: Viewer → Add

6️⃣  LẤY PROPERTY ID
   - Admin → Property Settings
   - Copy Property ID (dạng số, ví dụ: 123456789)
   - Format: properties/123456789

7️⃣  CẤU HÌNH VÀO ỨNG DỤNG
   - Xem hướng dẫn trong: docs/GOOGLE_ANALYTICS_API_SETUP.md
   - Hoặc dùng template: .streamlit/secrets.toml.example

📖 Xem hướng dẫn chi tiết: docs/GOOGLE_ANALYTICS_API_SETUP.md
    """)

def run_all_checks():
    """Chạy tất cả kiểm tra tự động"""
    print("\n" + "="*70)
    print("  CHẠY TẤT CẢ KIỂM TRA")
    print("="*70 + "\n")
    
    results = {
        'requirements': check_requirements(),
        'credentials': check_credentials(),
        'property_id': check_property_id(),
    }
    
    if all(results.values()):
        print("\n" + "="*70)
        print("  TẤT CẢ KIỂM TRA ĐỀU OK - ĐANG TEST API...")
        print("="*70 + "\n")
        results['api'] = test_api_connection()
    else:
        print("\n⚠️  Một số kiểm tra chưa pass. Vui lòng cấu hình trước khi test API.")
        results['api'] = False
    
    # Tổng kết
    print("\n" + "="*70)
    print("  TỔNG KẾT")
    print("="*70)
    print(f"✅ Requirements: {'OK' if results['requirements'] else '❌ Cần cài đặt'}")
    print(f"✅ Credentials: {'OK' if results['credentials'] else '❌ Cần cấu hình'}")
    print(f"✅ Property ID: {'OK' if results['property_id'] else '❌ Cần cấu hình'}")
    if 'api' in results:
        print(f"✅ API Connection: {'OK' if results['api'] else '❌ Cần kiểm tra'}")
    print("="*70 + "\n")
    
    if all(results.values()):
        print("🎉 TẤT CẢ ĐÃ SẴN SÀNG! Google Analytics API đã được cấu hình thành công!")
    else:
        print("📚 Xem hướng dẫn setup: docs/GOOGLE_ANALYTICS_API_SETUP.md")
        print("📋 Hoặc chạy: python setup_ga_api.py (chọn option 6)")

def main():
    """Main function"""
    import sys
    
    # Nếu có argument "auto", chạy tự động
    if len(sys.argv) > 1 and sys.argv[1] == "auto":
        create_secrets_template()
        run_all_checks()
        return
    
    print_header("🚀 GOOGLE ANALYTICS API SETUP HELPER")
    
    print("Chọn hành động:")
    print("1. Kiểm tra requirements")
    print("2. Kiểm tra credentials")
    print("3. Kiểm tra Property ID")
    print("4. Test kết nối API")
    print("5. Tạo template secrets")
    print("6. Xem hướng dẫn setup")
    print("7. Chạy tất cả kiểm tra")
    print("0. Thoát")
    
    try:
        choice = input("\nNhập lựa chọn (0-7): ").strip()
        
        if choice == "1":
            check_requirements()
        elif choice == "2":
            check_credentials()
        elif choice == "3":
            check_property_id()
        elif choice == "4":
            test_api_connection()
        elif choice == "5":
            create_secrets_template()
        elif choice == "6":
            print_setup_guide()
        elif choice == "7":
            run_all_checks()
        elif choice == "0":
            print("👋 Tạm biệt!")
        else:
            print("❌ Lựa chọn không hợp lệ")
    except (KeyboardInterrupt, EOFError):
        print("\n\n👋 Không có input. Chạy tự động...")
        create_secrets_template()
        run_all_checks()
    except Exception as e:
        print(f"\n❌ Lỗi: {e}")

if __name__ == "__main__":
    main()

