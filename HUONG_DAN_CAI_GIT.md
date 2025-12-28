# 🔧 HƯỚNG DẪN CÀI GIT VÀ COMMIT

## ⚡ CÁCH NHANH NHẤT: Dùng Cursor/VS Code (KHÔNG CẦN CÀI GIT)

Cursor/VS Code đã có Git tích hợp sẵn!

1. **Nhấn `Ctrl + Shift + G`** (mở Source Control)
2. **Click dấu `+`** bên cạnh "Changes" (stage tất cả)
3. **Copy commit message** từ `COMMIT_NHANH.txt` và paste vào ô "Message"
4. **Click "Commit"** → **Click "Push"**

**XONG!** Không cần cài Git! 🎉

---

## 🔧 CÁCH 2: Cài Git (nếu muốn dùng command line)

### Bước 1: Tải Git
- Vào: https://git-scm.com/download/win
- Download file `.exe`

### Bước 2: Cài đặt
1. Chạy file installer
2. **QUAN TRỌNG**: Trong quá trình cài, chọn **"Add Git to PATH"**
3. Cài đặt với các tùy chọn mặc định

### Bước 3: Commit và Push
Sau khi cài xong, mở Git Bash hoặc PowerShell và chạy:

```bash
cd "d:/1 medical"
git add .
git commit -m "Add auto-link scores system: components, scripts, and auto-generated mapping

- Add score_links.py component for linking to existing scores
- Add score_links_from_content.py for articles/protocols
- Add auto_link_scores_to_content.py script for auto-detection
- Auto-generate article_protocol_score_mapping.py (301 links: 74 articles, 9 protocols)
- Integrate score links into Articles and Protocols pages
- Update protocol_routing.py to support score links
- Add update_score_links.bat for quick updates
- Add documentation for score links system"
git push
```

---

## 🚀 CÁCH 3: Tự động cài Git (cần quyền Admin)

1. **Right-click** vào PowerShell → **"Run as Administrator"**
2. Chạy:
```powershell
cd "d:\1 medical"
powershell -ExecutionPolicy Bypass -File "scripts\install_git_and_commit.ps1"
```

Script sẽ tự động:
- Tải và cài Git
- Thêm vào PATH
- Commit và push

---

## 💡 KHUYẾN NGHỊ

**Dùng Cách 1 (Cursor/VS Code)** - Dễ nhất, không cần cài gì thêm!

