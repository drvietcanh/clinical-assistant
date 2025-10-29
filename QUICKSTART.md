# 🚀 Hướng Dẫn Bắt Đầu Nhanh - Clinical Assistant

**Thời gian triển khai:** 30 phút  
**Yêu cầu:** Tài khoản Google Workspace

---

## BƯỚC 1: Chuẩn Bị Google Sheets (5 phút)

### 1.1. Tạo Google Sheet mới
```
1. Truy cập: https://sheets.google.com
2. Tạo mới → Đặt tên: "Clinical Assistant Database"
3. Lưu URL để sử dụng sau
```

### 1.2. Import các file CSV hiện có

**Cách 1: Import thủ công**
```
Với mỗi file CSV trong thư mục data-csv/:
1. Tạo sheet mới (nút "+" ở dưới cùng)
2. File → Import → Upload → Chọn file CSV
3. Import location: "Replace current sheet"
4. Separator type: "Comma"
5. Đổi tên sheet giống tên file (ví dụ: "Scores", "Antibiotics")
```

**Cách 2: Script tự động (Khuyến nghị)**
```javascript
// Chạy script này 1 lần để import tất cả CSV
function importAllCSV() {
  const files = [
    {name: 'Meta', url: 'https://raw.githubusercontent.com/.../Meta.csv'},
    {name: 'Scores', url: 'https://raw.githubusercontent.com/.../Scores.csv'},
    {name: 'Antibiotics', url: 'https://raw.githubusercontent.com/.../Antibiotics.csv'},
    {name: 'Ventilator', url: 'https://raw.githubusercontent.com/.../Ventilator.csv'},
    {name: 'Protocols', url: 'https://raw.githubusercontent.com/.../Protocols.csv'}
  ];
  
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  files.forEach(f => {
    const response = UrlFetchApp.fetch(f.url);
    const csv = Utilities.parseCsv(response.getContentText());
    let sheet = ss.getSheetByName(f.name);
    if (!sheet) sheet = ss.insertSheet(f.name);
    sheet.clear();
    sheet.getRange(1, 1, csv.length, csv[0].length).setValues(csv);
  });
}
```

### 1.3. Kiểm tra cấu trúc
Đảm bảo có các sheets:
- ✅ Meta
- ✅ Scores  
- ✅ Antibiotics
- ✅ Ventilator
- ✅ Protocols

---

## BƯỚC 2: Deploy Apps Script (10 phút)

### 2.1. Mở Apps Script Editor
```
1. Trong Google Sheet → Extensions → Apps Script
2. Xóa code mặc định trong Code.gs
```

### 2.2. Tạo các file script

**File 1: Code.gs**
```javascript
// Code.gs — Web app entry point
function doGet(e) {
  return HtmlService.createTemplateFromFile('index')
                    .evaluate()
                    .setTitle('Clinical Assistant')
                    .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL)
                    .addMetaTag('viewport', 'width=device-width, initial-scale=1');
}

function include(filename) {
  return HtmlService.createHtmlOutputFromFile(filename).getContent();
}
```

**File 2: Core.gs**
```javascript
// Copy toàn bộ từ server/Core.gs trong repo
```

**File 3: Scores.api.gs**
```javascript
// Copy từ server/Scores.api.gs
```

**File 4-6: Tương tự cho Antibiotics, Vent, Protocols**

### 2.3. Tạo HTML files

Click **File → New → HTML file**, tạo các file:
- index.html
- styles.html
- app.html
- scores.html
- antibiotics.html
- vent.html
- protocols.html

Copy nội dung từ thư mục `web/` tương ứng.

### 2.4. Deploy Web App

```
1. Click "Deploy" → "New deployment"
2. Type: "Web app"
3. Description: "Clinical Assistant v1.0"
4. Execute as: "Me"
5. Who has access: "Anyone" (hoặc "Anyone within organization")
6. Click "Deploy"
7. Copy "Web app URL" → Đây là link ứng dụng của bạn!
```

**URL sẽ dạng:**
```
https://script.google.com/macros/s/AKfycbx.../exec
```

---

## BƯỚC 3: Test & Verify (5 phút)

### 3.1. Mở trên Mobile
```
1. Mở URL trên điện thoại
2. Test navigation: Scores, Antibiotics, Vent, Protocols
3. Thử tính qSOFA:
   - RR: 22
   - SBP: 90
   - GCS: 14
   → Kết quả: qSOFA = 2
```

### 3.2. Add to Home Screen (PWA)
**iOS Safari:**
```
1. Nhấn Share button
2. Chọn "Add to Home Screen"
3. Icon xuất hiện như native app
```

**Android Chrome:**
```
1. Menu (⋮) → "Add to Home screen"
2. Chấp nhận
```

---

## BƯỚC 4: Tùy Chỉnh (10 phút)

### 4.1. Thêm Logo Bệnh Viện

Chỉnh file `web/index.html`:
```html
<header class="nav">
  <img src="YOUR_HOSPITAL_LOGO_URL" alt="Logo" style="height:32px">
  <a href="#/scores">Scores</a>
  <!-- ... -->
</header>
```

### 4.2. Đổi Theme Colors

Chỉnh file `web/styles.html`:
```css
:root {
  --primary-color: #0066cc;    /* Màu chính bệnh viện */
  --secondary-color: #f0f0f0;
  --text-color: #111;
}

.btn { background: var(--primary-color); }
.nav { background: var(--secondary-color); }
```

### 4.3. Thêm Disclaimer

Thêm vào `web/index.html` (trước `</body>`):
```html
<footer style="text-align:center; padding:1rem; font-size:0.8rem; color:#666;">
  ⚠️ Chỉ mục đích tham khảo. Không thay thế đánh giá lâm sàng.
  <br>© 2025 [Tên Bệnh Viện] - v1.0
</footer>
```

---

## BƯỚC 5: Nâng Cao (Tùy chọn)

### 5.1. Enable Offline Mode

Thêm Service Worker (file `sw.js`):
```javascript
// Cache các tài nguyên tĩnh
const CACHE_NAME = 'clinical-assistant-v1';
const urlsToCache = [
  '/',
  '/styles.css',
  '/app.js'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(urlsToCache))
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => response || fetch(event.request))
  );
});
```

Register trong `index.html`:
```html
<script>
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('sw.js');
}
</script>
```

### 5.2. Analytics Tracking

Thêm vào `Code.gs`:
```javascript
function logUsage(module, action) {
  const props = PropertiesService.getScriptProperties();
  const key = module + '_' + action + '_' + new Date().toDateString();
  const current = Number(props.getProperty(key)) || 0;
  props.setProperty(key, String(current + 1));
}

// Gọi trong mỗi API function
function api_scores_calc(payload) {
  logUsage('scores', 'calculate');
  // ... existing code
}
```

View analytics:
```javascript
function viewAnalytics() {
  const props = PropertiesService.getScriptProperties();
  const all = props.getProperties();
  Logger.log(all); // View trong Execution log
}
```

### 5.3. User Feedback Form

Thêm module mới `web/feedback.html`:
```html
<script>
registerModule({
  id: 'feedback',
  title: 'Góp ý',
  mount: function(root) {
    const form = el('div', {class:'card'},
      el('h3', {}, 'Gửi góp ý'),
      el('textarea', {id:'feedbackText', rows:5, style:'width:100%'}),
      el('button', {class:'btn', onclick: ()=>{
        google.script.run
          .withSuccessHandler(()=>alert('Cảm ơn góp ý!'))
          .submitFeedback(feedbackText.value);
        feedbackText.value = '';
      }}, 'Gửi')
    );
    root.append(form);
  }
});
</script>
```

Backend (`Code.gs`):
```javascript
function submitFeedback(text) {
  const sheet = SpreadsheetApp.getActiveSpreadsheet()
                  .getSheetByName('Feedback') || 
                  SpreadsheetApp.getActiveSpreadsheet().insertSheet('Feedback');
  sheet.appendRow([new Date(), text, Session.getActiveUser().getEmail()]);
}
```

---

## 🎯 CHECKLIST Hoàn Thành

- [ ] Google Sheet có đủ 5 sheets (Meta, Scores, Antibiotics, Ventilator, Protocols)
- [ ] Apps Script có đủ files (.gs và .html)
- [ ] Web app đã deploy thành công
- [ ] Test trên mobile: qSOFA calculator hoạt động
- [ ] Đã add to home screen
- [ ] Đã thêm logo/branding bệnh viện
- [ ] Đã thêm disclaimer
- [ ] Đã share link cho 5 đồng nghiệp để beta test

---

## ❓ Troubleshooting

### Lỗi: "Script function not found"
**Nguyên nhân:** Tên file HTML không khớp với `include()` call  
**Giải pháp:** Kiểm tra tên file chính xác (case-sensitive)

### Lỗi: "Missing Sheet"
**Nguyên nhân:** Tên sheet không đúng hoặc chưa import CSV  
**Giải pháp:** Đảm bảo sheet tên chính xác: "Scores" (không phải "Score")

### Web app không load trên mobile
**Nguyên nhân:** Cache cũ  
**Giải pháp:** 
1. Hard refresh: Ctrl+Shift+R (desktop)
2. Deploy → "New deployment" (tạo version mới)

### Tính toán sai
**Nguyên nhân:** Dữ liệu CSV không đúng format  
**Giải pháp:** Kiểm tra CSV không có ký tự đặc biệt, encoding UTF-8

---

## 📞 Hỗ Trợ

**Có vấn đề?**
1. Check log: Apps Script Editor → "Executions" tab
2. Test API trực tiếp: Chạy function trong editor (ví dụ: `api_scores_list()`)
3. Review dữ liệu: Mở Google Sheet, check format

**Cần thêm chức năng?**
→ Xem `ROADMAP.md` để biết lộ trình đầy đủ

---

**🎉 Chúc mừng! Bạn đã có Clinical Assistant hoạt động!**

**Next steps:**
1. Share với đồng nghiệp để thu thập feedback
2. Bắt đầu implement các module trong ROADMAP
3. Tùy chỉnh theo nhu cầu bệnh viện

