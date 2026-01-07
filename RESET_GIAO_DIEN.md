# Hướng Dẫn Reset Lại Giao Diện App

## ⚠️ LƯU Ý QUAN TRỌNG
- Nếu bạn đã **push lên remote** (GitHub/GitLab), cần cẩn thận với `git reset --hard` và `git push --force`
- Nếu có người khác đang làm việc trên cùng branch, **KHÔNG NÊN** dùng `git push --force`

---

## Cách 1: Git Revert (KHUYẾN NGHỊ - An toàn nhất)

Tạo commit mới để hoàn tác các thay đổi, không làm mất lịch sử.

### Bước 1: Xem commit cần revert
```bash
git log --oneline -10
```

### Bước 2: Revert commit gần nhất (hoặc nhiều commit)
```bash
# Revert 1 commit gần nhất
git revert HEAD

# Hoặc revert nhiều commit
git revert HEAD~2..HEAD

# Hoặc revert commit cụ thể
git revert 16a9fb9
```

### Bước 3: Push lên remote
```bash
git push origin main
```

**Ưu điểm:**
- ✅ An toàn, không làm mất lịch sử
- ✅ Có thể revert nhiều commit
- ✅ Không cần force push

**Nhược điểm:**
- Tạo thêm commit mới trong lịch sử

---

## Cách 2: Git Reset + Force Push (NGUY HIỂM)

Reset về commit cũ và force push lên remote.

### ⚠️ CẢNH BÁO: Chỉ dùng nếu bạn chắc chắn và không có người khác đang làm việc trên branch!

### Bước 1: Xem commit muốn reset về
```bash
git log --oneline -10
```

### Bước 2: Reset về commit trước đó
```bash
# Reset về commit trước đó 1 bước (giữ thay đổi trong working directory)
git reset --soft HEAD~1

# Reset về commit trước đó và xóa thay đổi (NGUY HIỂM)
git reset --hard HEAD~1

# Reset về commit cụ thể
git reset --hard 584e063
```

### Bước 3: Force push (NGUY HIỂM!)
```bash
git push --force origin main
```

**Ưu điểm:**
- Xóa hoàn toàn commit khỏi lịch sử
- Lịch sử sạch sẽ hơn

**Nhược điểm:**
- ⚠️ Nguy hiểm nếu có người khác đang làm việc
- ⚠️ Có thể làm mất công việc của người khác
- ⚠️ Không thể khôi phục sau khi force push

---

## Cách 3: Chỉnh Sửa Lại và Commit Mới (KHUYẾN NGHỊ)

Chỉnh sửa lại code và commit mới, giữ nguyên lịch sử.

### Bước 1: Chỉnh sửa lại các file giao diện
```bash
# Sửa các file cần thiết
# Ví dụ: app.py, components/sidebar_navigation.py, etc.
```

### Bước 2: Commit và push
```bash
git add .
git commit -m "Revert: Khôi phục giao diện về phiên bản trước"
git push origin main
```

**Ưu điểm:**
- ✅ An toàn nhất
- ✅ Có thể chỉnh sửa chọn lọc
- ✅ Giữ nguyên lịch sử

---

## Cách 4: Tạo Branch Mới và Reset (An toàn)

Tạo branch mới từ commit cũ, sau đó merge lại.

### Bước 1: Tạo branch mới từ commit cũ
```bash
# Tạo branch mới từ commit cũ
git checkout -b revert-ui 584e063
```

### Bước 2: Merge vào main
```bash
git checkout main
git merge revert-ui
git push origin main
```

---

## So Sánh Các Cách

| Cách | An toàn | Giữ lịch sử | Độ khó | Khi nào dùng |
|------|---------|-------------|--------|--------------|
| **Revert** | ⭐⭐⭐⭐⭐ | ✅ Có | Dễ | Đã push, có người khác làm việc |
| **Reset + Force** | ⭐⭐ | ❌ Không | Trung bình | Chỉ mình bạn làm việc, chắc chắn |
| **Chỉnh sửa lại** | ⭐⭐⭐⭐⭐ | ✅ Có | Dễ | Muốn chỉnh sửa chọn lọc |
| **Branch mới** | ⭐⭐⭐⭐ | ✅ Có | Trung bình | Muốn thử nghiệm trước |

---

## Khuyến Nghị

**Nếu bạn đã push và có người khác làm việc:**
→ Dùng **Cách 1: Git Revert**

**Nếu chỉ mình bạn làm việc và chắc chắn:**
→ Có thể dùng **Cách 2: Git Reset + Force Push** (cẩn thận!)

**Nếu muốn chỉnh sửa chọn lọc:**
→ Dùng **Cách 3: Chỉnh sửa lại**

---

## Ví Dụ Cụ Thể

### Revert commit gần nhất về giao diện:
```bash
# Xem commit
git log --oneline -5

# Revert commit "Tối ưu hóa menu và giao diện"
git revert 16a9fb9

# Giải quyết conflict nếu có
git add .
git commit -m "Revert: Khôi phục giao diện về phiên bản trước"

# Push
git push origin main
```

### Reset về commit trước đó:
```bash
# Reset về commit trước đó 2 bước
git reset --hard HEAD~2

# Force push (CHỈ KHI CHẮC CHẮN!)
git push --force origin main
```

---

## Lưu Ý

1. **Luôn backup** trước khi reset: `git branch backup-before-reset`
2. **Kiểm tra** xem có người khác đang làm việc không
3. **Test** sau khi reset để đảm bảo app vẫn hoạt động
4. **Không force push** trên branch chính nếu có nhiều người làm việc
