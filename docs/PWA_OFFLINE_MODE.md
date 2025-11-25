# 📱 PWA & Offline Mode - Hướng Dẫn

**Ngày:** 2025-01-30  
**Version:** 1.0.0  
**Status:** ✅ Hoàn thành

---

## 📋 Tổng Quan

Ứng dụng đã được tích hợp **Progressive Web App (PWA)** với khả năng hoạt động offline. Người dùng có thể:

- ✅ Cài đặt ứng dụng như app native
- ✅ Hoạt động offline (một phần)
- ✅ Cache static assets và data
- ✅ Truy cập nhanh từ màn hình chính

---

## 🚀 Tính Năng

### 1. **PWA Installation**
- Cài đặt ứng dụng trên desktop/mobile
- Icon trên màn hình chính
- Launch như app native
- Standalone mode (không có browser UI)

### 2. **Offline Support**
- **Cache-first:** Static assets (CSS, JS, images)
- **Network-first:** Dynamic content (Streamlit routes)
- **Offline fallback:** Trang offline khi mất kết nối
- **Auto-update:** Service worker tự động cập nhật

### 3. **Caching Strategy**

```
Static Assets (CSS, JS, images)
  → Cache-first: Check cache → Network → Cache

Streamlit Routes (/pages/, /)
  → Network-first: Network → Cache → Offline page

API Responses
  → Stale-while-revalidate: Cache + Network
```

---

## 📁 Cấu Trúc Files

```
static/
├── manifest.json          # PWA manifest
├── service-worker.js      # Service worker logic
├── offline.html           # Offline fallback page
├── offline.js             # Offline support JS
├── icon-192.png           # PWA icon 192x192
└── icon-512.png           # PWA icon 512x512

components/
└── offline.py             # Streamlit offline component

app.py                     # Main app (injects PWA files)
```

---

## 🔧 Cài Đặt & Sử Dụng

### **Cho Người Dùng:**

#### **Desktop (Chrome/Edge):**
1. Mở ứng dụng trong browser
2. Click icon "Cài đặt" trong thanh địa chỉ (hoặc menu)
3. Click "Cài đặt" trong popup
4. Ứng dụng sẽ xuất hiện trên desktop/Start menu

#### **Mobile (iOS Safari):**
1. Mở ứng dụng trong Safari
2. Tap nút "Share" (hình vuông với mũi tên)
3. Chọn "Add to Home Screen"
4. Customize tên (nếu muốn)
5. Tap "Add"

#### **Mobile (Android Chrome):**
1. Mở ứng dụng trong Chrome
2. Tap menu (3 chấm)
3. Chọn "Install app" hoặc "Add to Home screen"
4. Tap "Install"

### **Kiểm Tra Trạng Thái:**
- Mở sidebar → "📱 PWA & Offline"
- Xem trạng thái online/offline
- Xem service worker status
- Xóa cache nếu cần

---

## 🛠️ Development

### **Tạo Icons Mới:**

```bash
python utils/create_pwa_icons.py
```

Hoặc thay thế `static/icon-192.png` và `static/icon-512.png` bằng icons tùy chỉnh.

### **Update Service Worker:**

1. Sửa `static/service-worker.js`
2. Tăng version trong `CACHE_NAME` (ví dụ: `v1` → `v2`)
3. Service worker sẽ tự động update khi user reload

### **Test Offline Mode:**

1. **Chrome DevTools:**
   - F12 → Application tab
   - Service Workers → Check "Offline"
   - Reload page

2. **Network Throttling:**
   - F12 → Network tab
   - Throttle → "Offline"
   - Test functionality

3. **Disconnect Internet:**
   - Tắt WiFi/network
   - Test offline features

---

## 📊 Caching Details

### **Cached Resources:**

#### **On Install:**
- `/static/styles.css`
- `/static/offline.html`
- `/static/manifest.json`
- `/static/offline.js`

#### **Runtime Cache:**
- Static assets (CSS, JS, images)
- Streamlit routes (visited pages)
- API responses (drug database, etc.)

### **Cache Size:**
- Default: ~5-10 MB
- Auto-cleanup: Old caches deleted on update

---

## ⚠️ Limitations

### **Streamlit-Specific:**

1. **Dynamic Routes:**
   - Streamlit routes (`/pages/`) là dynamic
   - Không thể cache toàn bộ app offline
   - Chỉ cache pages đã visit

2. **Server-Side Rendering:**
   - Streamlit render trên server
   - Offline mode chỉ hoạt động với cached content
   - Một số tính năng cần server connection

3. **Real-time Updates:**
   - Service worker cần reload để update
   - Không có auto-sync như native apps

### **Browser Support:**

| Browser | PWA Support | Offline Support |
|---------|-------------|-----------------|
| Chrome/Edge | ✅ Full | ✅ Full |
| Firefox | ✅ Full | ✅ Full |
| Safari (iOS) | ✅ Full | ✅ Full |
| Safari (macOS) | ⚠️ Limited | ✅ Full |
| Opera | ✅ Full | ✅ Full |

---

## 🔍 Troubleshooting

### **Service Worker Không Hoạt Động:**

1. **Check Console:**
   ```javascript
   // F12 → Console
   navigator.serviceWorker.getRegistrations()
   ```

2. **Clear Cache:**
   - F12 → Application → Clear storage
   - Hoặc: Sidebar → PWA & Offline → "Xóa Cache"

3. **Unregister Service Worker:**
   ```javascript
   navigator.serviceWorker.getRegistrations().then(function(registrations) {
     for(let registration of registrations) {
       registration.unregister();
     }
   });
   ```

### **Icons Không Hiển Thị:**

1. Check `static/icon-192.png` và `icon-512.png` tồn tại
2. Check `manifest.json` có đúng paths
3. Clear cache và reload

### **Offline Page Không Hiển Thị:**

1. Check `static/offline.html` tồn tại
2. Check service worker cache `OFFLINE_URL`
3. Test với DevTools → Offline mode

---

## 📈 Future Improvements

### **Priority 1:**
- [ ] Cache drug database to IndexedDB
- [ ] Cache calculator definitions
- [ ] Background sync khi online lại
- [ ] Push notifications (optional)

### **Priority 2:**
- [ ] Full offline mode cho calculators
- [ ] Offline data entry với sync
- [ ] Conflict resolution khi sync
- [ ] Advanced cache management UI

### **Priority 3:**
- [ ] Web Share API integration
- [ ] File System Access API
- [ ] Periodic background sync
- [ ] Web Push notifications

---

## 📚 References

- [MDN: Progressive Web Apps](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps)
- [MDN: Service Workers](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API)
- [Web.dev: PWA](https://web.dev/progressive-web-apps/)
- [Streamlit: Static Files](https://docs.streamlit.io/library/advanced-features/static-file-serving)

---

## ✅ Checklist Implementation

- [x] Create `manifest.json`
- [x] Create `service-worker.js`
- [x] Create `offline.html` fallback
- [x] Create `offline.js` support
- [x] Create PWA icons (192x192, 512x512)
- [x] Inject manifest và JS vào `app.py`
- [x] Create offline component (`components/offline.py`)
- [x] Add offline indicator
- [x] Add PWA info in sidebar
- [x] Test offline functionality
- [x] Documentation

---

**Last Updated:** 2025-01-30  
**Maintained by:** Clinical IT Team

