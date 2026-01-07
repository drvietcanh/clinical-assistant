# Hướng Dẫn Refresh và Xóa Cache trên Streamlit Cloud

## 🌐 Streamlit Cloud - Cách Refresh và Xóa Cache

### 1. Refresh Giao Diện trên Streamlit Cloud

**Trong Browser:**
- `Ctrl + R` hoặc `F5` - Refresh trang
- `Ctrl + Shift + R` hoặc `Ctrl + F5` - Hard refresh (xóa cache browser)
- Click vào menu **☰** → **Rerun** - Chạy lại app từ đầu

**Từ URL:**
- Thêm `?clear_cache=true` vào cuối URL:
  ```
  https://your-app.streamlit.app/?clear_cache=true
  ```

### 2. Xóa Cache Từ Code (Trong App)

Thêm nút Clear Cache vào app (đã có trong app.py):

```python
import streamlit as st

if st.button("🗑️ Clear Cache"):
    st.cache_data.clear()
    st.cache_resource.clear()
    st.success("✅ Cache cleared!")
    st.rerun()
```

### 3. Xóa Cache Bằng URL Parameter

Streamlit Cloud hỗ trợ URL parameters để clear cache:

```
https://your-app.streamlit.app/?clear_cache=true
```

Hoặc trong code, có thể check parameter:

```python
import streamlit as st

# Check nếu có parameter clear_cache
if st.query_params.get("clear_cache") == "true":
    st.cache_data.clear()
    st.cache_resource.clear()
    st.query_params.clear()
    st.rerun()
```

---

## 🚀 Deploy và Cập Nhật App trên Streamlit Cloud

### Bước 1: Push Code Lên GitHub

```bash
# Kiểm tra status
git status

# Add các file thay đổi
git add .

# Commit
git commit -m "Update: Thêm tính năng clear cache"

# Push lên GitHub
git push origin main
```

### Bước 2: Streamlit Cloud Tự Động Deploy

Streamlit Cloud sẽ tự động:
1. Detect khi có commit mới trên GitHub
2. Pull code mới
3. Rebuild và redeploy app
4. Clear cache cũ

**Thời gian:** Thường mất 1-3 phút để deploy xong.

### Bước 3: Kiểm Tra Deploy Status

1. Vào [Streamlit Cloud Dashboard](https://share.streamlit.io/)
2. Click vào app của bạn
3. Xem tab **Activity** để theo dõi deploy progress
4. Xem tab **Logs** nếu có lỗi

---

## 🔄 Cách Force Redeploy trên Streamlit Cloud

### Cách 1: Tạo Empty Commit

```bash
git commit --allow-empty -m "Force redeploy"
git push origin main
```

### Cách 2: Từ Streamlit Cloud Dashboard

1. Vào [Streamlit Cloud Dashboard](https://share.streamlit.io/)
2. Click vào app của bạn
3. Click **⋮** (menu) → **Redeploy**
4. Hoặc click **Settings** → **Redeploy**

### Cách 3: Thay Đổi File Requirements

Thêm comment vào `requirements.txt` để trigger rebuild:

```txt
# Updated: 2025-01-07
streamlit>=1.28.0
pandas>=2.0.0
```

Sau đó commit và push.

---

## 🗑️ Xóa Cache trên Streamlit Cloud

### Cách 1: Từ Code (Đã Implement)

App đã có nút Clear Cache trong sidebar (Developer Tools).

### Cách 2: URL Parameter

Thêm `?clear_cache=true` vào URL:
```
https://your-app.streamlit.app/?clear_cache=true
```

### Cách 3: Từ Streamlit Cloud Dashboard

1. Vào Dashboard → App của bạn
2. Click **Settings**
3. Click **Clear cache** (nếu có)

### Cách 4: Restart App

1. Vào Dashboard → App của bạn
2. Click **⋮** → **Restart**
3. Hoặc **Settings** → **Restart**

---

## 📝 Cấu Hình Streamlit Cloud

### File `.streamlit/config.toml` (nếu cần)

```toml
[server]
# Tự động clear cache khi rerun
clearCacheOnRerun = false

# Headless mode (không cần)
headless = true

# Port (mặc định)
port = 8501
```

### File `.streamlit/secrets.toml` (cho secrets)

```toml
# Secrets cho Streamlit Cloud
# Được set từ Dashboard → Settings → Secrets

# Ví dụ:
show_dev_tools = true
google_analytics_id = "G-XXXXXXXXXX"
```

**Lưu ý:** File `secrets.toml` KHÔNG được commit lên GitHub. Set secrets từ Dashboard.

---

## 🔧 Troubleshooting trên Streamlit Cloud

### App Không Cập Nhật Sau Khi Push

1. **Kiểm tra GitHub:** Đảm bảo code đã push thành công
2. **Kiểm tra Branch:** Đảm bảo Streamlit Cloud đang watch đúng branch (thường là `main`)
3. **Kiểm tra Logs:** Vào Dashboard → Logs để xem lỗi
4. **Force Redeploy:** Tạo empty commit hoặc click Redeploy

### Cache Không Xóa

1. **Hard Refresh Browser:** `Ctrl + Shift + R`
2. **Dùng URL Parameter:** `?clear_cache=true`
3. **Restart App:** Từ Dashboard
4. **Clear từ Code:** Click nút Clear Cache trong app

### App Chạy Chậm

1. **Kiểm tra Cache:** Có thể cache quá nhiều, cần clear
2. **Kiểm tra Logs:** Xem có lỗi nào không
3. **Optimize Code:** Giảm số lượng cache, optimize queries
4. **Upgrade Plan:** Nếu cần (Streamlit Cloud có free và paid plans)

---

## 📋 Checklist Deploy

- [ ] Code đã được commit và push lên GitHub
- [ ] Branch đúng (main/master)
- [ ] Requirements.txt đầy đủ
- [ ] Không có lỗi syntax trong code
- [ ] Test local trước khi push
- [ ] Kiểm tra logs trên Streamlit Cloud
- [ ] Test app sau khi deploy

---

## 🎯 Quick Commands

### Push Code Lên GitHub:
```bash
git add .
git commit -m "Update app"
git push origin main
```

### Force Redeploy:
```bash
git commit --allow-empty -m "Force redeploy"
git push origin main
```

### Clear Cache từ URL:
```
https://your-app.streamlit.app/?clear_cache=true
```

---

## 💡 Tips cho Streamlit Cloud

1. **Auto-deploy:** Streamlit Cloud tự động deploy khi có commit mới
2. **Branch:** Mặc định watch branch `main` hoặc `master`
3. **Secrets:** Set từ Dashboard, không commit vào code
4. **Logs:** Luôn check logs nếu có vấn đề
5. **Cache:** Streamlit Cloud tự động quản lý cache, nhưng có thể clear thủ công
6. **Performance:** Free plan có giới hạn, paid plan tốt hơn

---

## 🔗 Links Hữu Ích

- [Streamlit Cloud Dashboard](https://share.streamlit.io/)
- [Streamlit Cloud Docs](https://docs.streamlit.io/streamlit-community-cloud)
- [GitHub Integration](https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app/connect-to-github)

---

## 📞 Support

Nếu gặp vấn đề:
1. Check [Streamlit Community Forum](https://discuss.streamlit.io/)
2. Check [GitHub Issues](https://github.com/streamlit/streamlit/issues)
3. Xem logs trên Streamlit Cloud Dashboard
