"""
Test kết nối Google Analytics API với thông báo lỗi chi tiết
"""

import streamlit as st
from components.google_analytics_api import (
    get_ga_credentials,
    get_ga_property_id,
    get_analytics_data,
    GA_API_AVAILABLE
)

print("=" * 70)
print("  TEST KẾT NỐI GOOGLE ANALYTICS API")
print("=" * 70)

if not GA_API_AVAILABLE:
    print("❌ Google Analytics Data API chưa được cài đặt")
    print("   Chạy: pip install google-analytics-data")
    exit(1)

print("\n1. Đang lấy credentials...")
credentials = get_ga_credentials()
if not credentials:
    print("❌ Không tìm thấy credentials")
    print("   Kiểm tra file .streamlit/secrets.toml")
    exit(1)
print("✅ Credentials: OK")

print("\n2. Đang lấy Property ID...")
property_id = get_ga_property_id()
if not property_id:
    print("❌ Không tìm thấy Property ID")
    print("   Kiểm tra file .streamlit/secrets.toml")
    exit(1)
print(f"✅ Property ID: {property_id}")

print("\n3. Đang test kết nối API...")
try:
    data = get_analytics_data(property_id, credentials, days=7)
    if data:
        print("\n✅ KẾT NỐI THÀNH CÔNG!")
        print(f"   - Users (7 ngày): {data['total_users']:,}")
        print(f"   - Sessions: {data['total_sessions']:,}")
        print(f"   - Pageviews: {data['total_pageviews']:,}")
        print(f"   - Realtime Users: {data['realtime_users']}")
    else:
        print("❌ Không thể lấy dữ liệu")
        print("\n💡 Có thể do:")
        print("   1. Permissions chưa được cập nhật (đợi 5-10 phút)")
        print("   2. Chưa có dữ liệu trong Google Analytics")
        print("   3. Service Account chưa được thêm đúng cách")
except Exception as e:
    print(f"\n❌ LỖI: {e}")
    print(f"\n💡 Kiểm tra:")
    print("   1. Service Account đã được thêm vào Google Analytics Property?")
    print("   2. Quyền đã được set là 'Viewer'?")
    print("   3. Google Analytics Data API đã được enable trong Google Cloud?")
    print("   4. Đợi 5-10 phút sau khi thêm email để permissions cập nhật")

print("\n" + "=" * 70)

