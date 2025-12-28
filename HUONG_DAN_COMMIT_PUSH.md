# 📝 HƯỚNG DẪN COMMIT VÀ PUSH (RẤT ĐƠN GIẢN)

## Cách 1: Dùng Cursor/VS Code (DỄ NHẤT - CHỈ 4 BƯỚC)

### Bước 1: Mở Source Control
- Nhấn phím **`Ctrl + Shift + G`** (hoặc click icon Source Control ở sidebar bên trái)

### Bước 2: Stage tất cả files
- Ở phần "Changes", bạn sẽ thấy danh sách files đã thay đổi
- Click vào dấu **`+`** bên cạnh chữ "Changes" (hoặc click chuột phải vào "Changes" → chọn "Stage All Changes")
- Tất cả files sẽ chuyển sang phần "Staged Changes"

### Bước 3: Viết commit message
- Ở ô "Message" phía trên, copy và paste đoạn này:

```
Add auto-link scores system: components, scripts, and auto-generated mapping

- Add score_links.py component for linking to existing scores
- Add score_links_from_content.py for articles/protocols
- Add auto_link_scores_to_content.py script for auto-detection
- Auto-generate article_protocol_score_mapping.py (301 links: 74 articles, 9 protocols)
- Integrate score links into Articles and Protocols pages
- Update protocol_routing.py to support score links
- Add update_score_links.bat for quick updates
- Add documentation for score links system
```

### Bước 4: Commit và Push
- Click nút **"Commit"** (hoặc nhấn `Ctrl + Enter`)
- Sau khi commit xong, click nút **"Push"** (hoặc nhấn `Ctrl + Shift + P` → gõ "push" → chọn "Git: Push")

**XONG!** 🎉

---

## Cách 2: Cài Git và dùng Command Line

### Bước 1: Cài Git
1. Vào: https://git-scm.com/download/win
2. Download và cài đặt
3. Trong quá trình cài, chọn "Add Git to PATH"

### Bước 2: Mở Git Bash
- Click chuột phải vào thư mục dự án → chọn "Git Bash Here"

### Bước 3: Chạy lệnh
Copy và paste từng dòng này:

```bash
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

**XONG!** 🎉

---

## ⚠️ LƯU Ý

- Nếu lần đầu push, có thể cần nhập username/password
- Nếu có lỗi, hãy chụp màn hình và gửi lại

---

## 📸 HÌNH ẢNH MÔ TẢ

### Trong Cursor/VS Code:
```
┌─────────────────────────────────────┐
│ Source Control (Ctrl+Shift+G)      │
├─────────────────────────────────────┤
│ Message: [Paste commit message]    │
│                                     │
│ Changes (click + để stage)         │
│  ✏️ file1.py                       │
│  ✏️ file2.py                       │
│                                     │
│ [Commit] [Push]                    │
└─────────────────────────────────────┘
```

---

**KHUYẾN NGHỊ: Dùng Cách 1 (Cursor/VS Code) - Dễ nhất!**

