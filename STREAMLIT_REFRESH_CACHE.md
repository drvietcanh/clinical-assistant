# Hướng Dẫn Refresh Giao Diện và Xóa Cache Streamlit

## 🔄 Cách Refresh Giao Diện Streamlit

### 1. Refresh Trong Browser (Cách Đơn Giản Nhất)

**Windows/Linux:**
- `Ctrl + R` - Refresh trang
- `Ctrl + Shift + R` hoặc `Ctrl + F5` - Hard refresh (xóa cache browser)
- `F5` - Refresh

**Mac:**
- `Cmd + R` - Refresh trang
- `Cmd + Shift + R` - Hard refresh

### 2. Sử Dụng Menu Streamlit

Trong giao diện Streamlit, click vào menu **☰** (góc trên bên phải) và chọn:
- **Rerun** - Chạy lại app từ đầu
- **Clear cache** - Xóa cache của Streamlit
- **Settings** → **Clear cache** - Xóa cache

### 3. Dùng Nút Rerun Trong Code

Thêm nút rerun vào code:
```python
import streamlit as st

if st.button("🔄 Refresh App"):
    st.cache_data.clear()
    st.rerun()
```

---

## 🗑️ Cách Xóa Cache Streamlit

### Cách 1: Xóa Cache Từ Code (Trong App)

#### Xóa tất cả cache:
```python
import streamlit as st

# Xóa tất cả cache
st.cache_data.clear()
st.cache_resource.clear()

# Sau đó rerun
st.rerun()
```

#### Xóa cache của một function cụ thể:
```python
import streamlit as st

@st.cache_data
def my_cached_function():
    return "data"

# Xóa cache của function này
my_cached_function.clear()

# Hoặc xóa cache khi có tham số cụ thể
my_cached_function.clear(key="specific_key")
```

### Cách 2: Xóa Cache Từ Terminal/Command Line

#### Windows PowerShell:
```powershell
# Xóa cache Streamlit
Remove-Item -Recurse -Force "$env:USERPROFILE\.streamlit\cache"

# Hoặc xóa cache trong thư mục project
Remove-Item -Recurse -Force ".streamlit\cache"
```

#### Windows CMD:
```cmd
rmdir /s /q "%USERPROFILE%\.streamlit\cache"
```

#### Linux/Mac:
```bash
# Xóa cache Streamlit
rm -rf ~/.streamlit/cache

# Hoặc xóa cache trong thư mục project
rm -rf .streamlit/cache
```

### Cách 3: Xóa Cache Khi Chạy Streamlit

Thêm flag `--server.clearCacheOnRerun` khi chạy:
```bash
streamlit run app.py --server.clearCacheOnRerun=true
```

Hoặc trong file `.streamlit/config.toml`:
```toml
[server]
clearCacheOnRerun = true
```

---

## 🛠️ Tạo Script Xóa Cache

### Script Python để xóa cache:

```python
# clear_streamlit_cache.py
import shutil
import os
from pathlib import Path

def clear_streamlit_cache():
    """Xóa cache Streamlit"""
    cache_paths = [
        Path.home() / ".streamlit" / "cache",
        Path(".streamlit") / "cache",
        Path("__pycache__"),
    ]
    
    for cache_path in cache_paths:
        if cache_path.exists():
            try:
                shutil.rmtree(cache_path)
                print(f"✅ Đã xóa: {cache_path}")
            except Exception as e:
                print(f"❌ Lỗi khi xóa {cache_path}: {e}")
        else:
            print(f"ℹ️  Không tìm thấy: {cache_path}")

if __name__ == "__main__":
    clear_streamlit_cache()
    print("\n✨ Hoàn tất! Khởi động lại Streamlit để áp dụng.")
```

### Script Batch (Windows):

```batch
@echo off
echo Xoa cache Streamlit...

rmdir /s /q "%USERPROFILE%\.streamlit\cache" 2>nul
rmdir /s /q ".streamlit\cache" 2>nul
rmdir /s /q "__pycache__" 2>nul

echo Hoan tat!
pause
```

### Script Shell (Linux/Mac):

```bash
#!/bin/bash
echo "Xóa cache Streamlit..."

rm -rf ~/.streamlit/cache
rm -rf .streamlit/cache
rm -rf __pycache__

echo "Hoàn tất!"
```

---

## 🔧 Xóa Cache Cụ Thể Trong App

### Xóa cache của các function trong app:

```python
import streamlit as st
from utils.cache_helpers import (
    get_module_list_for_navigation_cached,
    get_popular_calculators,
    compute_usage_stats_snapshot
)

# Xóa cache của các function cụ thể
if st.sidebar.button("🗑️ Clear All Cache"):
    get_module_list_for_navigation_cached.clear()
    get_popular_calculators.clear()
    compute_usage_stats_snapshot.clear()
    st.cache_data.clear()
    st.cache_resource.clear()
    st.success("✅ Đã xóa tất cả cache!")
    st.rerun()
```

---

## 🎯 Xóa Session State

Nếu muốn reset toàn bộ state của app:

```python
import streamlit as st

if st.button("🔄 Reset App"):
    # Xóa tất cả session state
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    
    # Xóa cache
    st.cache_data.clear()
    st.cache_resource.clear()
    
    # Rerun
    st.rerun()
```

---

## 📝 Thêm Nút Clear Cache Vào App

Thêm vào sidebar hoặc settings:

```python
import streamlit as st

with st.sidebar:
    st.markdown("---")
    st.subheader("⚙️ Developer Tools")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🔄 Rerun"):
            st.rerun()
    
    with col2:
        if st.button("🗑️ Clear Cache"):
            st.cache_data.clear()
            st.cache_resource.clear()
            st.success("Cache cleared!")
            st.rerun()
```

---

## 🚀 Các Cách Khác Để Refresh

### 1. Restart Streamlit Server

Dừng server (Ctrl+C) và chạy lại:
```bash
streamlit run app.py
```

### 2. Xóa File .pyc

```bash
# Windows PowerShell
Get-ChildItem -Path . -Recurse -Filter *.pyc | Remove-Item

# Linux/Mac
find . -type f -name "*.pyc" -delete
```

### 3. Xóa __pycache__

```bash
# Windows PowerShell
Get-ChildItem -Path . -Recurse -Directory -Filter __pycache__ | Remove-Item -Recurse

# Linux/Mac
find . -type d -name __pycache__ -exec rm -r {} +
```

---

## ⚙️ Cấu Hình Cache Trong config.toml

Tạo file `.streamlit/config.toml`:

```toml
[server]
# Tự động xóa cache khi rerun
clearCacheOnRerun = false

# Port và các cấu hình khác
port = 8501
```

---

## 🔍 Kiểm Tra Cache Đang Dùng

Xem cache đang được sử dụng:

```python
import streamlit as st

# Hiển thị thông tin cache
st.write("Cache info:", st.cache_data.get_stats())
```

---

## 💡 Tips

1. **Hard Refresh Browser**: `Ctrl + Shift + R` (Windows) hoặc `Cmd + Shift + R` (Mac)
2. **Xóa cache khi code thay đổi**: Thêm `st.cache_data.clear()` vào đầu file
3. **Disable cache tạm thời**: Comment decorator `@st.cache_data` khi debug
4. **Xóa cache theo điều kiện**: Chỉ xóa khi có thay đổi cụ thể

---

## 🎬 Quick Commands

### Windows:
```powershell
# Xóa cache và restart
Remove-Item -Recurse -Force "$env:USERPROFILE\.streamlit\cache"; streamlit run app.py
```

### Linux/Mac:
```bash
# Xóa cache và restart
rm -rf ~/.streamlit/cache && streamlit run app.py
```

---

## 📌 Tóm Tắt

| Mục đích | Cách làm |
|----------|----------|
| **Refresh trang** | `Ctrl + R` hoặc `F5` |
| **Hard refresh** | `Ctrl + Shift + R` |
| **Xóa cache từ code** | `st.cache_data.clear()` |
| **Xóa cache từ terminal** | Xóa thư mục `.streamlit/cache` |
| **Reset app hoàn toàn** | Xóa cache + xóa session state + rerun |
| **Restart server** | `Ctrl + C` rồi chạy lại `streamlit run app.py` |
