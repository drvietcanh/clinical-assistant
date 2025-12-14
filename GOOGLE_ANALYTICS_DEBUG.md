# 🔍 Hướng Dẫn Debug Google Analytics

## ✅ Đã Sửa

1. **Google Analytics ID**: Đã cập nhật từ `G-JRP0GQLG70` (số 0) thành `G-JRPOGQLG70` (chữ O)
2. **Retry Logic**: Thêm retry logic với tối đa 5 lần thử khi load gtag.js
3. **Error Handling**: Thêm try-catch để bắt lỗi khi track
4. **Periodic Check**: Thêm interval check mỗi 2 giây để đảm bảo không miss navigation
5. **Improved Timing**: Tăng delay để đảm bảo gtag đã load trước khi track

## 🔧 Cách Kiểm Tra

### 1. Kiểm Tra Trong Browser Console

Mở Developer Tools (F12) và kiểm tra:

```javascript
// Kiểm tra gtag có tồn tại không
typeof gtag
// Kết quả: "function"

// Kiểm tra dataLayer
window.dataLayer
// Kết quả: Array với các events

// Kiểm tra GA script đã load chưa
document.querySelector('script[src*="googletagmanager.com/gtag/js"]')
// Kết quả: <script> element
```

### 2. Kiểm Tra Network Requests

1. Mở Developer Tools → Network tab
2. Filter: `collect` hoặc `google-analytics`
3. Reload trang
4. Tìm requests đến `google-analytics.com` hoặc `googletagmanager.com`
5. Kiểm tra status code: phải là 200

### 3. Kiểm Tra Google Analytics Real-Time

1. Vào Google Analytics → Realtime → Overview
2. Mở app trong tab mới
3. Trong vòng 30 giây, bạn sẽ thấy:
   - Active users: +1
   - Page views: +1
   - Current page: URL của app

### 4. Kiểm Tra Browser Extensions

Một số extensions có thể block Google Analytics:
- AdBlock
- uBlock Origin
- Privacy Badger
- Ghostery

Tắt các extensions này và test lại.

## 🐛 Các Vấn Đề Thường Gặp

### Vấn đề 1: Script không load

**Triệu chứng**: Không thấy request đến `googletagmanager.com`

**Nguyên nhân**:
- Streamlit block script injection
- Network issue
- CORS issue

**Giải pháp**:
- Kiểm tra console có lỗi không
- Kiểm tra Network tab
- Thử tăng retry delay

### Vấn đề 2: gtag undefined

**Triệu chứng**: `typeof gtag === 'undefined'`

**Nguyên nhân**:
- Script chưa load xong
- Script bị block
- Timing issue

**Giải pháp**:
- Code đã có retry logic
- Tăng timeout trong `initTracking()`
- Kiểm tra script có trong DOM không

### Vấn đề 3: Events không được gửi

**Triệu chứng**: Có request nhưng không thấy trong GA

**Nguyên nhân**:
- Measurement ID sai
- Filter trong GA
- Data processing delay (24-48 giờ)

**Giải pháp**:
- Kiểm tra Measurement ID đúng: `G-JRPOGQLG70`
- Kiểm tra Real-time report (không có delay)
- Đợi 24-48 giờ cho standard reports

## 📊 Code Changes

### File: `config/app_config.py`
```python
"google_analytics_id": os.getenv("GOOGLE_ANALYTICS_ID", "G-JRPOGQLG70"),
```

### File: `app.py`
- Thêm retry logic với `onload` và `onerror` handlers
- Thêm error handling với try-catch
- Thêm periodic check mỗi 2 giây
- Tăng delay để đảm bảo gtag load xong

## 🧪 Test Script

Tạo file `test_ga.html` để test GA tracking:

```html
<!DOCTYPE html>
<html>
<head>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-JRPOGQLG70"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', 'G-JRPOGQLG70');
    </script>
</head>
<body>
    <h1>Test Google Analytics</h1>
    <button onclick="gtag('event', 'button_click', {'event_category': 'test'}); alert('Event sent!');">
        Send Test Event
    </button>
</body>
</html>
```

Mở file này trong browser và kiểm tra Real-time report trong GA.

## 📝 Checklist

- [ ] Measurement ID đúng: `G-JRPOGQLG70`
- [ ] Script được inject vào `<head>`
- [ ] gtag.js load thành công (check Network tab)
- [ ] `gtag` function tồn tại (check Console)
- [ ] Events được gửi (check Network tab, filter `collect`)
- [ ] Real-time report hiển thị data
- [ ] Không có lỗi trong Console
- [ ] Không có ad blockers active

## 🚀 Next Steps

1. Deploy code mới lên Streamlit Cloud
2. Đợi 5-10 phút để GA process data
3. Kiểm tra Real-time report
4. Nếu vẫn không thấy data, kiểm tra:
   - Streamlit Cloud có block script không
   - Có CSP (Content Security Policy) nào block không
   - Có service worker nào intercept requests không

## 📞 Support

Nếu vẫn không hoạt động sau khi thử tất cả các bước trên:
1. Check Streamlit Cloud logs
2. Check browser console errors
3. Check Network tab requests
4. Verify Measurement ID trong GA dashboard

