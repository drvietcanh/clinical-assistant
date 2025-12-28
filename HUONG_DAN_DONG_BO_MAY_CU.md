# 🔄 HƯỚNG DẪN ĐỒNG BỘ MÁY CŨ TRƯỚC KHI LÀM VIỆC TRÊN MÁY MỚI

## ⚠️ QUAN TRỌNG: Làm trên máy cũ TRƯỚC

### Bước 1: Kiểm tra thay đổi trên máy cũ
```bash
cd "d:\1 medical"  # hoặc thư mục của bạn
git status
```

### Bước 2: Commit tất cả thay đổi trên máy cũ
```bash
git add .
git commit -m "Lưu thay đổi từ máy cũ trước khi chuyển sang máy mới"
```

### Bước 3: Push lên GitHub
```bash
git push
```

**✅ XONG! Bây giờ mới chuyển sang máy mới**

---

## 🖥️ TRÊN MÁY MỚI

### Bước 1: Clone hoặc Pull
**Nếu chưa có repository:**
```bash
git clone https://github.com/drvietcanh/clinical-assistant.git
cd clinical-assistant
```

**Nếu đã có repository:**
```bash
cd "d:\1 medical"  # hoặc thư mục của bạn
git pull
```

### Bước 2: Kiểm tra đã đồng bộ
```bash
git status
git log --oneline -5
```

**Phải thấy commit mới nhất từ máy cũ!**

---

## ⚠️ XỬ LÝ XUNG ĐỘT (Nếu có)

### Nếu có lỗi "divergent branches":
```bash
# Xem thay đổi
git fetch
git log --oneline --graph --all

# Merge thay đổi từ máy cũ
git pull --rebase

# Hoặc nếu muốn giữ thay đổi máy mới
git pull --no-rebase
```

### Nếu có conflict (xung đột file):
1. Git sẽ báo file nào bị conflict
2. Mở file đó, tìm dòng có `<<<<<<<`, `=======`, `>>>>>>>`
3. Chọn phần code đúng (hoặc kết hợp cả 2)
4. Xóa các dòng marker (`<<<<<<<`, `=======`, `>>>>>>>`)
5. Lưu file
6. Chạy:
```bash
git add <tên_file>
git commit -m "Resolve conflict"
git push
```

---

## ✅ CHECKLIST AN TOÀN

### Trước khi chuyển máy:
- [ ] Commit tất cả thay đổi trên máy cũ
- [ ] Push lên GitHub
- [ ] Kiểm tra `git status` = "nothing to commit"

### Trên máy mới:
- [ ] Pull code mới nhất
- [ ] Kiểm tra `git status` = "up to date"
- [ ] Test chạy app để đảm bảo không lỗi

---

## 💡 MẸO

1. **Luôn pull trước khi làm việc:**
   ```bash
   git pull
   # Làm việc...
   git add .
   git commit -m "..."
   git push
   ```

2. **Kiểm tra trạng thái thường xuyên:**
   ```bash
   git status
   ```

3. **Xem lịch sử:**
   ```bash
   git log --oneline -10
   ```

---

**Lưu ý:** Nếu máy cũ không có internet hoặc không thể push, hãy copy thư mục `.git` cùng với code sang máy mới, sau đó push từ máy mới.

