# Workflow GitHub + Streamlit Cloud - Hướng Dẫn Nhanh

## 🚀 Quy Trình Cập Nhật App trên Streamlit Cloud

### 1. Làm Việc Local

```bash
# 1. Sửa code
# ... edit files ...

# 2. Test local
streamlit run app.py

# 3. Commit và push
git add .
git commit -m "Update: Mô tả thay đổi"
git push origin main
```

### 2. Streamlit Cloud Tự Động Deploy

- Streamlit Cloud tự động detect commit mới
- Tự động pull code và rebuild
- Thường mất **1-3 phút**

### 3. Kiểm Tra Deploy

1. Vào [Streamlit Cloud Dashboard](https://share.streamlit.io/)
2. Xem tab **Activity** để theo dõi progress
3. Xem tab **Logs** nếu có lỗi

---

## 🔄 Refresh và Clear Cache trên Streamlit Cloud

### Cách 1: Hard Refresh Browser
- `Ctrl + Shift + R` (Windows/Linux)
- `Cmd + Shift + R` (Mac)

### Cách 2: Dùng URL Parameter
Thêm vào cuối URL của app:
```
?clear_cache=true
```
Ví dụ:
```
https://your-app.streamlit.app/?clear_cache=true
```

### Cách 3: Nút Clear Cache trong App
- Click nút **🗑️ Clear Cache** trong sidebar
- App sẽ tự động clear cache và rerun

### Cách 4: Restart App từ Dashboard
1. Vào [Streamlit Cloud Dashboard](https://share.streamlit.io/)
2. Click vào app của bạn
3. Click **⋮** → **Restart**

---

## 🛠️ Developer Tools (Tùy Chọn)

### Enable Developer Tools từ URL:
Thêm vào URL:
```
?dev_tools=true
```

Hoặc set trong Streamlit Cloud Secrets:
1. Vào Dashboard → App → Settings → Secrets
2. Thêm:
```toml
show_dev_tools = true
```

---

## 📋 Checklist Trước Khi Push

- [ ] Code đã test local và chạy OK
- [ ] Không có lỗi syntax
- [ ] Requirements.txt đầy đủ
- [ ] Commit message rõ ràng
- [ ] Đã push lên GitHub thành công

---

## 🔧 Troubleshooting

### App Không Cập Nhật Sau Push

**Giải pháp:**
```bash
# Force redeploy bằng empty commit
git commit --allow-empty -m "Force redeploy"
git push origin main
```

Hoặc từ Dashboard → Click **Redeploy**

### Cache Không Xóa

**Giải pháp:**
1. Hard refresh: `Ctrl + Shift + R`
2. Dùng URL: `?clear_cache=true`
3. Click nút Clear Cache trong app
4. Restart app từ Dashboard

### Lỗi Khi Deploy

**Kiểm tra:**
1. Xem **Logs** trên Dashboard
2. Kiểm tra **Requirements.txt** có đầy đủ không
3. Kiểm tra code có lỗi syntax không
4. Test lại local trước khi push

---

## 💡 Tips

1. **Auto-deploy:** Streamlit Cloud tự động deploy khi push lên GitHub
2. **Branch:** Mặc định watch branch `main` hoặc `master`
3. **Secrets:** Set từ Dashboard, không commit vào code
4. **Cache:** Streamlit Cloud tự quản lý, nhưng có thể clear thủ công
5. **Performance:** Free plan có giới hạn, nhưng đủ cho hầu hết apps

---

## 🔗 Links

- [Streamlit Cloud Dashboard](https://share.streamlit.io/)
- [Streamlit Cloud Docs](https://docs.streamlit.io/streamlit-community-cloud)
- [GitHub của bạn](https://github.com/your-username/your-repo)

---

## 📝 Quick Commands

```bash
# Push code lên GitHub
git add .
git commit -m "Update app"
git push origin main

# Force redeploy
git commit --allow-empty -m "Force redeploy"
git push origin main

# Clear cache từ URL
https://your-app.streamlit.app/?clear_cache=true
```
