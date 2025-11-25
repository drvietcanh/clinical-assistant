"""
Tự động tạo file secrets.toml từ file JSON
"""

import json
from pathlib import Path

# Đọc file JSON
json_file = Path("ordinal-tower-479306-f0-4a63b90a1b41.json")
with open(json_file, 'r', encoding='utf-8') as f:
    json_data = json.load(f)

# Tạo thư mục .streamlit
streamlit_dir = Path(".streamlit")
streamlit_dir.mkdir(exist_ok=True)

# Tạo nội dung secrets
secrets_content = f"""[google_analytics]
service_account_json = '''
{json.dumps(json_data, indent=2)}
'''
property_id = "properties/YOUR_PROPERTY_ID"
"""

# Ghi file
secrets_file = streamlit_dir / "secrets.toml"
with open(secrets_file, 'w', encoding='utf-8') as f:
    f.write(secrets_content)

print("✅ Đã tạo file: .streamlit/secrets.toml")
print(f"\n📧 Service Account Email: {json_data['client_email']}")
print("\n⚠️  BẠN CẦN:")
print("   1. Thêm email này vào Google Analytics Property")
print("   2. Lấy Property ID và thay 'YOUR_PROPERTY_ID' trong file secrets.toml")
print("\n📋 Xem hướng dẫn: HUONG_DAN_DON_GIAN.md")

