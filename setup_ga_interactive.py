"""
Interactive Setup Helper cho Google Analytics API
Hướng dẫn từng bước và kiểm tra tiến độ
"""

import os
import json
from pathlib import Path

def print_header(text):
    """In header đẹp"""
    print("\n" + "=" * 70)
    print(f"  {text}")
    print("=" * 70 + "\n")

def print_step(step_num, title):
    """In step header"""
    print(f"\n{'='*70}")
    print(f"  BƯỚC {step_num}: {title}")
    print(f"{'='*70}\n")

def wait_for_user():
    """Đợi user nhấn Enter"""
    input("👉 Nhấn ENTER khi bạn đã hoàn thành bước này...")

def check_json_file():
    """Kiểm tra file JSON credentials"""
    print("📁 Kiểm tra file JSON credentials...")
    
    # Tìm file JSON trong thư mục hiện tại
    current_dir = Path(".")
    json_files = list(current_dir.glob("*.json"))
    
    # Hoặc tìm trong thư mục credentials
    creds_dir = Path("credentials")
    if creds_dir.exists():
        json_files.extend(list(creds_dir.glob("*.json")))
    
    if json_files:
        print(f"\n✅ Tìm thấy {len(json_files)} file JSON:")
        for i, f in enumerate(json_files, 1):
            print(f"   {i}. {f}")
        
        try:
            choice = input("\nChọn file (số) hoặc Enter để bỏ qua: ").strip()
            if choice and choice.isdigit():
                idx = int(choice) - 1
                if 0 <= idx < len(json_files):
                    selected_file = json_files[idx]
                    return validate_json_file(selected_file)
        except:
            pass
    
    print("⚠️  Chưa tìm thấy file JSON trong thư mục hiện tại")
    print("   Bạn có thể paste đường dẫn đến file JSON:")
    file_path = input("   Đường dẫn file (hoặc Enter để bỏ qua): ").strip()
    
    if file_path:
        path = Path(file_path)
        if path.exists():
            return validate_json_file(path)
    
    return None

def validate_json_file(file_path):
    """Validate file JSON"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        required_fields = ['type', 'project_id', 'private_key', 'client_email']
        missing = [f for f in required_fields if f not in data]
        
        if missing:
            print(f"❌ File thiếu các field: {', '.join(missing)}")
            return None
        
        print(f"\n✅ File JSON hợp lệ!")
        print(f"   - Project ID: {data.get('project_id')}")
        print(f"   - Client Email: {data.get('client_email')}")
        print(f"   - Type: {data.get('type')}")
        
        return {
            'file_path': str(file_path),
            'project_id': data.get('project_id'),
            'client_email': data.get('client_email'),
            'json_content': json.dumps(data, indent=2)
        }
    except json.JSONDecodeError:
        print("❌ File không phải JSON hợp lệ")
        return None
    except Exception as e:
        print(f"❌ Lỗi đọc file: {e}")
        return None

def step_1_2_google_cloud():
    """Bước 1-2: Google Cloud Console"""
    print_step(1, "TẠO GOOGLE CLOUD PROJECT & ENABLE API")
    
    print("""
📋 HƯỚNG DẪN:

1. Mở trình duyệt, truy cập: https://console.cloud.google.com/
2. Đăng nhập bằng tài khoản Google của bạn

3. TẠO PROJECT:
   - Click dropdown "Select a project" (góc trên trái)
   - Click "NEW PROJECT"
   - Đặt tên: "Clinical Assistant Analytics"
   - Click "CREATE"
   - Đợi vài giây → Click "SELECT"

4. ENABLE API:
   - Menu trái → "APIs & Services" → "Library"
   - Tìm: "Google Analytics Data API"
   - Click "ENABLE"
   - Đợi vài giây để API được enable
    """)
    
    wait_for_user()
    
    print("\n✅ Bạn đã hoàn thành Bước 1-2!")
    return True

def step_3_service_account():
    """Bước 3: Tạo Service Account"""
    print_step(3, "TẠO SERVICE ACCOUNT")
    
    print("""
📋 HƯỚNG DẪN:

1. Trong Google Cloud Console:
   - Menu trái → "APIs & Services" → "Credentials"

2. TẠO SERVICE ACCOUNT:
   - Click "+ CREATE CREDENTIALS"
   - Chọn "Service account"

3. ĐIỀN THÔNG TIN:
   - Service account name: "analytics-reader"
   - Description (tùy chọn): "Service account để đọc Google Analytics data"
   - Click "CREATE AND CONTINUE"

4. BỎ QUA GRANT ACCESS:
   - Click "CONTINUE" hoặc "DONE"
   - (Không cần grant access)
    """)
    
    wait_for_user()
    
    print("\n✅ Bạn đã hoàn thành Bước 3!")
    return True

def step_4_download_json():
    """Bước 4: Download JSON"""
    print_step(4, "DOWNLOAD JSON CREDENTIALS")
    
    print("""
📋 HƯỚNG DẪN:

1. Trong danh sách Service Accounts:
   - Click vào Service Account vừa tạo (tên: analytics-reader)

2. VÀO TAB KEYS:
   - Click tab "KEYS" (ở trên cùng)
   - Click "ADD KEY" → "Create new key"

3. TẠO KEY:
   - Chọn "JSON"
   - Click "CREATE"
   - File JSON sẽ tự động download về máy

4. LƯU FILE:
   - Tìm file vừa download (tên: your-project-id-xxxxx.json)
   - Di chuyển vào thư mục an toàn
   - Ví dụ: D:\\1app\\medical\\credentials\\
    """)
    
    wait_for_user()
    
    # Kiểm tra file JSON
    print("\n🔍 Đang kiểm tra file JSON...")
    json_info = check_json_file()
    
    if json_info:
        print(f"\n✅ Đã tìm thấy file JSON hợp lệ!")
        print(f"   📧 Service Account Email: {json_info['client_email']}")
        print(f"   💾 Lưu email này lại - bạn sẽ cần nó ở bước tiếp theo!")
        
        # Lưu thông tin vào file tạm
        temp_file = Path(".ga_setup_temp.json")
        with open(temp_file, 'w', encoding='utf-8') as f:
            json.dump(json_info, f, indent=2)
        print(f"\n💡 Thông tin đã được lưu vào: {temp_file}")
        
        return json_info
    else:
        print("\n⚠️  Chưa tìm thấy file JSON hợp lệ")
        print("   Bạn có thể tiếp tục và quay lại bước này sau")
        return None

def step_5_get_email():
    """Bước 5: Lấy Email Service Account"""
    print_step(5, "LẤY EMAIL SERVICE ACCOUNT")
    
    # Thử load từ file tạm
    temp_file = Path(".ga_setup_temp.json")
    if temp_file.exists():
        try:
            with open(temp_file, 'r', encoding='utf-8') as f:
                json_info = json.load(f)
                email = json_info.get('client_email')
                if email:
                    print(f"✅ Đã tìm thấy email từ file trước đó:")
                    print(f"   📧 {email}")
                    print(f"\n💡 Email này sẽ được dùng ở Bước 6")
                    return email
        except:
            pass
    
    print("""
📋 HƯỚNG DẪN:

CÓ 2 CÁCH LẤY EMAIL:

CÁCH 1: Từ file JSON (Khuyến nghị)
   - Mở file JSON vừa download
   - Tìm dòng: "client_email"
   - Copy giá trị email
   - Ví dụ: analytics-reader@your-project-id.iam.gserviceaccount.com

CÁCH 2: Từ Google Cloud Console
   - Vào Service Account details
   - Email hiển thị ở phần "Service account details" → "Email"
   - Copy email này
    """)
    
    email = input("\n👉 Paste email Service Account vào đây (hoặc Enter để bỏ qua): ").strip()
    
    if email and '@' in email:
        print(f"\n✅ Đã lưu email: {email}")
        return email
    else:
        print("\n⚠️  Email không hợp lệ hoặc bạn đã bỏ qua")
        print("   Bạn có thể quay lại bước này sau")
        return None

def step_6_add_to_analytics():
    """Bước 6: Thêm vào Google Analytics"""
    print_step(6, "THÊM SERVICE ACCOUNT VÀO GOOGLE ANALYTICS")
    
    # Lấy email từ bước trước
    email = None
    temp_file = Path(".ga_setup_temp.json")
    if temp_file.exists():
        try:
            with open(temp_file, 'r', encoding='utf-8') as f:
                json_info = json.load(f)
                email = json_info.get('client_email')
        except:
            pass
    
    if email:
        print(f"📧 Service Account Email: {email}")
        print(f"   (Đã lấy từ file JSON)")
    else:
        email = input("\n👉 Nhập email Service Account: ").strip()
    
    print(f"""
📋 HƯỚNG DẪN:

1. Mở Google Analytics: https://analytics.google.com/
2. Đăng nhập bằng tài khoản Google (cùng tài khoản với Google Cloud)

3. VÀO ADMIN:
   - Click icon ⚙️ Admin (góc dưới trái)

4. VÀO PROPERTY ACCESS MANAGEMENT:
   - Cột "Property" (cột giữa)
   - Click "Property access management"
   - Hoặc: "Property Settings" → "Property Access Management"

5. THÊM USER:
   - Click nút "+" hoặc "Add users"
   - Trong ô "Email addresses", paste email:
     {email if email else '[EMAIL_SERVICE_ACCOUNT]'}

6. CHỌN QUYỀN:
   - Phần "Select roles" → Chọn "Viewer"
   - (Chỉ cần quyền Viewer, không cần Editor)

7. HOÀN THÀNH:
   - Click "Add"
   - Bạn sẽ thấy email xuất hiện trong danh sách với quyền "Viewer"
    """)
    
    wait_for_user()
    
    print("\n✅ Bạn đã hoàn thành Bước 6!")
    return True

def step_7_get_property_id():
    """Bước 7: Lấy Property ID"""
    print_step(7, "LẤY PROPERTY ID")
    
    print("""
📋 HƯỚNG DẪN:

1. Trong Google Analytics, vẫn ở phần Admin:
   - Cột "Property" → Click "Property Settings"

2. TÌM PROPERTY ID:
   - Scroll xuống, tìm phần "Property ID"
   - Bạn sẽ thấy một SỐ (ví dụ: 123456789 hoặc 130433471)
   - Copy số này!

3. FORMAT:
   - Property ID cần format: properties/123456789
   - Nếu bạn copy được số 123456789
   - Thì format đúng là: properties/123456789
    """)
    
    prop_id = input("\n👉 Nhập Property ID (số, ví dụ: 123456789): ").strip()
    
    if prop_id:
        # Loại bỏ "properties/" nếu có
        prop_id = prop_id.replace('properties/', '').strip()
        
        # Validate là số
        if prop_id.isdigit():
            formatted_id = f"properties/{prop_id}"
            print(f"\n✅ Property ID hợp lệ: {formatted_id}")
            
            # Lưu vào file tạm
            temp_file = Path(".ga_setup_temp.json")
            temp_data = {}
            if temp_file.exists():
                try:
                    with open(temp_file, 'r', encoding='utf-8') as f:
                        temp_data = json.load(f)
                except:
                    pass
            
            temp_data['property_id'] = formatted_id
            with open(temp_file, 'w', encoding='utf-8') as f:
                json.dump(temp_data, f, indent=2)
            
            return formatted_id
        else:
            print("❌ Property ID phải là số!")
            return None
    else:
        print("\n⚠️  Bạn đã bỏ qua. Có thể quay lại bước này sau.")
        return None

def step_8_configure_app():
    """Bước 8: Cấu hình vào App"""
    print_step(8, "CẤU HÌNH VÀO ỨNG DỤNG")
    
    # Load thông tin từ file tạm
    temp_file = Path(".ga_setup_temp.json")
    json_info = None
    property_id = None
    
    if temp_file.exists():
        try:
            with open(temp_file, 'r', encoding='utf-8') as f:
                temp_data = json.load(f)
                json_info = temp_data
                property_id = temp_data.get('property_id')
        except:
            pass
    
    if not json_info or not json_info.get('json_content'):
        print("⚠️  Chưa có thông tin JSON credentials")
        print("   Vui lòng quay lại Bước 4 để download file JSON")
        json_path = input("\n👉 Hoặc paste đường dẫn đến file JSON: ").strip()
        if json_path:
            json_info = validate_json_file(Path(json_path))
    
    if not property_id:
        print("⚠️  Chưa có Property ID")
        property_id = input("\n👉 Nhập Property ID (format: properties/123456789): ").strip()
    
    if json_info and property_id:
        print("\n" + "="*70)
        print("  CẤU HÌNH STREAMLIT SECRETS")
        print("="*70)
        
        print("\n📋 Chọn cách cấu hình:")
        print("1. Streamlit Cloud (Khuyến nghị cho production)")
        print("2. Local Development (.streamlit/secrets.toml)")
        print("3. Cả hai")
        
        choice = input("\n👉 Chọn (1/2/3): ").strip()
        
        secrets_content = f"""[google_analytics]
service_account_json = '''
{json_info['json_content']}
'''
property_id = "{property_id}"
"""
        
        if choice in ['1', '3']:
            print("\n" + "="*70)
            print("  STREAMLIT CLOUD SECRETS")
            print("="*70)
            print("\n📋 Hướng dẫn:")
            print("1. Vào Streamlit Cloud: https://share.streamlit.io/")
            print("2. Chọn app của bạn")
            print("3. Settings → Secrets")
            print("4. Paste nội dung sau vào editor:")
            print("\n" + "-"*70)
            print(secrets_content)
            print("-"*70)
            print("\n5. Click 'Save'")
            wait_for_user()
        
        if choice in ['2', '3']:
            print("\n" + "="*70)
            print("  LOCAL DEVELOPMENT")
            print("="*70)
            
            # Tạo thư mục .streamlit
            streamlit_dir = Path(".streamlit")
            streamlit_dir.mkdir(exist_ok=True)
            
            secrets_file = streamlit_dir / "secrets.toml"
            
            if secrets_file.exists():
                overwrite = input(f"\n⚠️  File {secrets_file} đã tồn tại. Ghi đè? (y/n): ").strip().lower()
                if overwrite != 'y':
                    print("❌ Đã hủy")
                    return False
            
            with open(secrets_file, 'w', encoding='utf-8') as f:
                f.write(secrets_content)
            
            print(f"\n✅ Đã tạo file: {secrets_file}")
            print("⚠️  LƯU Ý: File này đã được thêm vào .gitignore, sẽ không commit lên GitHub")
        
        print("\n✅ Bạn đã hoàn thành Bước 8!")
        return True
    else:
        print("\n❌ Thiếu thông tin cần thiết. Vui lòng quay lại các bước trước.")
        return False

def step_9_test():
    """Bước 9: Kiểm tra"""
    print_step(9, "KIỂM TRA")
    
    print("""
📋 KIỂM TRA CẤU HÌNH:

Đang chạy script kiểm tra tự động...
    """)
    
    # Import và chạy check
    try:
        from setup_ga_api import run_all_checks
        run_all_checks()
    except Exception as e:
        print(f"\n⚠️  Không thể chạy script kiểm tra: {e}")
        print("   Bạn có thể chạy thủ công: python setup_ga_api.py auto")
    
    print("\n" + "="*70)
    print("  HOÀN THÀNH!")
    print("="*70)
    print("""
🎉 Nếu tất cả kiểm tra đều OK, bạn đã setup thành công!

📋 BƯỚC TIẾP THEO:
1. Restart ứng dụng Streamlit (nếu đang chạy local)
2. Mở trang web
3. Scroll xuống phần "Thống Kê Truy Cập"
4. Sẽ thấy số liệu thực tế từ Google Analytics!

💡 Lưu ý: Số liệu có thể mất vài phút để hiển thị sau khi có lượt truy cập thực tế.
    """)

def main():
    """Main interactive setup"""
    print_header("🚀 GOOGLE ANALYTICS API - INTERACTIVE SETUP")
    
    print("""
Chào mừng đến với Interactive Setup Helper!

Tool này sẽ hướng dẫn bạn từng bước để cấu hình Google Analytics API.
Mỗi bước sẽ có hướng dẫn chi tiết và kiểm tra tự động.

Bắt đầu thôi! 🚀
    """)
    
    input("\n👉 Nhấn ENTER để bắt đầu...")
    
    # Chạy từng bước
    steps = [
        ("Bước 1-2", step_1_2_google_cloud),
        ("Bước 3", step_3_service_account),
        ("Bước 4", step_4_download_json),
        ("Bước 5", step_5_get_email),
        ("Bước 6", step_6_add_to_analytics),
        ("Bước 7", step_7_get_property_id),
        ("Bước 8", step_8_configure_app),
        ("Bước 9", step_9_test),
    ]
    
    for step_name, step_func in steps:
        try:
            result = step_func()
            if result is False:
                print(f"\n⚠️  {step_name} có vấn đề. Bạn có thể quay lại sau.")
                continue_choice = input("\n👉 Tiếp tục? (y/n): ").strip().lower()
                if continue_choice != 'y':
                    print("\n👋 Đã dừng. Bạn có thể chạy lại script này bất cứ lúc nào!")
                    break
        except KeyboardInterrupt:
            print("\n\n👋 Đã hủy. Bạn có thể chạy lại script này bất cứ lúc nào!")
            break
        except Exception as e:
            print(f"\n❌ Lỗi ở {step_name}: {e}")
            continue_choice = input("\n👉 Tiếp tục? (y/n): ").strip().lower()
            if continue_choice != 'y':
                break
    
    # Cleanup
    temp_file = Path(".ga_setup_temp.json")
    if temp_file.exists():
        keep = input("\n👉 Giữ file tạm .ga_setup_temp.json? (y/n): ").strip().lower()
        if keep != 'y':
            temp_file.unlink()
            print("✅ Đã xóa file tạm")
    
    print("\n" + "="*70)
    print("  CẢM ƠN BẠN ĐÃ SỬ DỤNG!")
    print("="*70 + "\n")

if __name__ == "__main__":
    main()

