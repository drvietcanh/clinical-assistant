#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script để xóa cache Streamlit
Sử dụng: python clear_streamlit_cache.py
"""

import shutil
import os
from pathlib import Path

def clear_streamlit_cache():
    """Xóa cache Streamlit và các file cache khác"""
    print("=" * 70)
    print("XÓA CACHE STREAMLIT")
    print("=" * 70)
    print()
    
    cache_paths = [
        # Cache Streamlit global
        Path.home() / ".streamlit" / "cache",
        # Cache trong project
        Path(".streamlit") / "cache",
        # Python cache
        Path("__pycache__"),
        # Cache trong các thư mục con
        Path("drugs") / "__pycache__",
        Path("pages") / "__pycache__",
        Path("components") / "__pycache__",
        Path("utils") / "__pycache__",
        Path("config") / "__pycache__",
    ]
    
    deleted_count = 0
    not_found_count = 0
    error_count = 0
    
    for cache_path in cache_paths:
        if cache_path.exists():
            try:
                shutil.rmtree(cache_path)
                print(f"✅ Đã xóa: {cache_path}")
                deleted_count += 1
            except Exception as e:
                print(f"❌ Lỗi khi xóa {cache_path}: {e}")
                error_count += 1
        else:
            print(f"ℹ️  Không tìm thấy: {cache_path}")
            not_found_count += 1
    
    print()
    print("=" * 70)
    print("TỔNG HỢP")
    print("=" * 70)
    print(f"✅ Đã xóa: {deleted_count} thư mục")
    print(f"ℹ️  Không tìm thấy: {not_found_count} thư mục")
    if error_count > 0:
        print(f"❌ Lỗi: {error_count} thư mục")
    
    print()
    print("✨ Hoàn tất! Khởi động lại Streamlit để áp dụng.")
    print("   Chạy: streamlit run app.py")
    print("=" * 70)

if __name__ == "__main__":
    clear_streamlit_cache()
