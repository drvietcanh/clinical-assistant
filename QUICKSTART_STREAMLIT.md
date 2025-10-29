# 🚀 Hướng Dẫn Triển Khai Nhanh - Clinical Assistant với Streamlit

**Thời gian:** 15 phút  
**Platform:** Streamlit Community Cloud (Free)  
**Auto-deploy:** ✅ Tự động từ GitHub

---

## 📋 TỔNG QUAN

### Ưu điểm Streamlit so với Apps Script:
- ✅ **Giao diện đẹp hơn** - Modern, professional
- ✅ **Dễ customize** - Python thuần, không giới hạn
- ✅ **Auto-deploy từ GitHub** - Push code là tự động update
- ✅ **Responsive tốt hơn** - Mobile, tablet, desktop
- ✅ **Dashboard capabilities** - Charts, metrics, expanders
- ✅ **AI integration** - Dễ tích hợp Gemini, GPT-4

---

## BƯỚC 1: Chuẩn Bị GitHub Repository (5 phút)

### 1.1. Tạo Repository Mới

```bash
# Tại thư mục medical/
git init
git add .
git commit -m "Initial commit - Clinical Assistant Streamlit"

# Tạo repo trên GitHub
# https://github.com/new
# Tên repo: clinical-assistant

# Link local với GitHub
git remote add origin https://github.com/YOUR_USERNAME/clinical-assistant.git
git branch -M main
git push -u origin main
```

### 1.2. Cấu Trúc Thư Mục Đã Sẵn Sàng

```
medical/
├── app.py                      # ← File chính Streamlit
├── pages/                      # ← Multi-page app
│   ├── 01_📊_Scores.py
│   ├── 02_💊_Antibiotics.py
│   ├── 03_🫁_Ventilator.py
│   └── 04_📋_Protocols.py
├── data/                       # ← Data CSV (đã có)
│   ├── Meta.csv
│   ├── Scores.csv
│   ├── Antibiotics.csv
│   ├── Ventilator.csv
│   └── Protocols.csv
├── utils/                      # ← Helper functions
│   ├── __init__.py
│   ├── calculators.py
│   └── data_loader.py
├── requirements.txt            # ← Dependencies
├── .streamlit/
│   └── config.toml            # ← Theme config
└── README_STREAMLIT.md
```

Tất cả đã được tạo tự động trong thư mục này!

---

## BƯỚC 2: Deploy lên Streamlit Cloud (5 phút)

### 2.1. Tạo Tài Khoản Streamlit

1. Truy cập: **https://streamlit.io/cloud**
2. Click **"Sign up"**
3. Chọn **"Continue with GitHub"**
4. Authorize Streamlit truy cập GitHub của bạn

### 2.2. Deploy App

1. **Click "New app"**

2. **Điền thông tin:**
   ```
   Repository: YOUR_USERNAME/clinical-assistant
   Branch: main
   Main file path: app.py
   ```

3. **Advanced settings (Optional):**
   ```
   Python version: 3.9
   App URL: clinical-assistant (hoặc tên bạn muốn)
   ```

4. **Click "Deploy!"**

5. **Đợi 2-3 phút** - Streamlit sẽ:
   - Clone repo của bạn
   - Cài đặt dependencies từ `requirements.txt`
   - Chạy `streamlit run app.py`
   - Tạo URL: `https://clinical-assistant-yourname.streamlit.app`

### 2.3. Nhận URL và Chia Sẻ

```
🎉 App của bạn đã live tại:
https://clinical-assistant-yourname.streamlit.app

- Mở trên điện thoại: Scan QR code
- Bookmark: Add to home screen (PWA-like)
- Share: Gửi link cho đồng nghiệp
```

---

## BƯỚC 3: Test Trên Mobile (2 phút)

### iPhone/iPad:
1. Mở Safari, truy cập URL
2. Tap Share button (⬆️)
3. Chọn "Add to Home Screen"
4. Icon xuất hiện như native app

### Android:
1. Mở Chrome, truy cập URL
2. Menu (⋮) → "Add to Home screen"
3. Icon xuất hiện

---

## BƯỚC 4: Cập Nhật App (Auto-Deploy)

### Thay Đổi Code Local:

```bash
# Sửa file bất kỳ, ví dụ app.py
nano app.py

# Commit và push
git add .
git commit -m "Update: Add SOFA calculator"
git push origin main
```

### Streamlit Cloud Tự Động:
- ✅ Detect thay đổi từ GitHub
- ✅ Rebuild app (1-2 phút)
- ✅ Deploy version mới
- ✅ Người dùng tự động thấy update (refresh page)

**Không cần làm gì thêm!** 🎉

---

## 📱 SỬ DỤNG APP

### Giao Diện Chính

```
┌─────────────────────────────────────────┐
│  🩺 Clinical Assistant                  │
│  ════════════════════════                │
│                                          │
│  📊 Scores                               │ ← Click vào module
│  💊 Antibiotics                          │
│  🫁 Ventilator                           │
│  📋 Protocols                            │
│                                          │
│  ─────────────────────────────────────  │
│                                          │
│  [Nội dung module hiển thị ở đây]       │
│                                          │
└─────────────────────────────────────────┘
```

### Module Scores - Ví dụ qSOFA

```
📊 Scores > qSOFA Calculator

Respiratory Rate (/min)
[22                    ] ← Input

Systolic BP (mmHg)
[90                    ]

GCS
[14                    ]

[Calculate qSOFA]  ← Button

─────────────────────────
📈 Result: qSOFA = 2
⚠️ Concerning for sepsis
📚 Reference: Sepsis-3 (JAMA 2016)
```

---

## 🎨 CUSTOMIZATION

### Thay Đổi Theme (Màu Sắc)

Edit `.streamlit/config.toml`:

```toml
[theme]
primaryColor="#0066cc"        # Màu chính (buttons, links)
backgroundColor="#ffffff"      # Background
secondaryBackgroundColor="#f0f2f6"  # Sidebar, boxes
textColor="#262730"           # Text color
font="sans serif"             # Font family
```

**Màu theo bệnh viện:**
```toml
# Ví dụ: Màu xanh bệnh viện
primaryColor="#1976d2"
secondaryBackgroundColor="#e3f2fd"
```

### Thêm Logo Bệnh Viện

Edit `app.py`:

```python
import streamlit as st

# Thêm logo
st.image("assets/hospital_logo.png", width=200)
st.title("🩺 Clinical Assistant - [Tên Bệnh Viện]")
```

Upload logo vào thư mục `assets/`.

---

## 🔧 TROUBLESHOOTING

### App không chạy sau deploy

**Kiểm tra logs:**
1. Vào Streamlit Cloud dashboard
2. Click vào app
3. Xem "Logs" tab
4. Tìm lỗi (thường là import hoặc file not found)

**Lỗi thường gặp:**

```python
# ❌ Lỗi: ModuleNotFoundError: No module named 'pandas'
# ✅ Fix: Thêm 'pandas' vào requirements.txt

# ❌ Lỗi: FileNotFoundError: data/Scores.csv
# ✅ Fix: Kiểm tra đường dẫn, đảm bảo file trong repo

# ❌ Lỗi: Invalid syntax
# ✅ Fix: Kiểm tra Python version (dùng 3.9+)
```

### App chạy chậm

**Tối ưu với @st.cache_data:**

```python
import streamlit as st
import pandas as pd

@st.cache_data  # ← Cache data, không load lại
def load_data(file):
    return pd.read_csv(file)

df = load_data("data/Scores.csv")
```

### Update không tự động

**Force rebuild:**
1. Streamlit Cloud → App settings
2. Click "Reboot app"
3. Hoặc: Push một commit nhỏ để trigger

---

## 📊 MONITORING & ANALYTICS

### Xem Thống Kê Sử Dụng

**Streamlit Cloud Dashboard:**
- 📈 Viewers (realtime)
- 📊 Resource usage (CPU, RAM)
- 🕐 Uptime

**Thêm Google Analytics (Optional):**

```python
# app.py
import streamlit.components.v1 as components

# Inject GA code
ga_code = """
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
"""
components.html(ga_code, height=0)
```

---

## 🔐 BẢO MẬT

### Public vs. Private App

**Free tier Streamlit Cloud:**
- ✅ App luôn public (có URL thì ai cũng truy cập được)
- ❌ Không có authentication built-in

**Nếu cần riêng tư:**

**Option 1: Private GitHub Repo (cần Streamlit Teams - $250/month)**

**Option 2: Tự code authentication:**

```python
import streamlit as st

def check_password():
    def password_entered():
        if st.session_state["password"] == "hospital2024":
            st.session_state["password_correct"] = True
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.text_input("Password", type="password", 
                      on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        st.text_input("Password", type="password", 
                      on_change=password_entered, key="password")
        st.error("😕 Password incorrect")
        return False
    else:
        return True

if check_password():
    st.write("Main app here")
```

**Option 3: Deploy riêng trên server bệnh viện** (xem DEPLOYMENT_STREAMLIT.md)

---

## 📦 OFFLINE MODE (Nội Mạng Bệnh Viện)

### Deploy Streamlit Trên Server Riêng

```bash
# Trên server Ubuntu/Windows
pip install streamlit
git clone https://github.com/YOUR_USERNAME/clinical-assistant.git
cd clinical-assistant
pip install -r requirements.txt

# Chạy app
streamlit run app.py --server.port 8501 --server.address 0.0.0.0

# Truy cập:
# http://SERVER_IP:8501
```

**Chạy như service (luôn bật):**

```bash
# Tạo systemd service
sudo nano /etc/systemd/system/clinical-assistant.service
```

```ini
[Unit]
Description=Clinical Assistant Streamlit
After=network.target

[Service]
User=www-data
WorkingDirectory=/opt/clinical-assistant
ExecStart=/usr/bin/streamlit run app.py --server.port 8501
Restart=always

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl enable clinical-assistant
sudo systemctl start clinical-assistant
```

---

## 🎯 NEXT STEPS

### Sau khi deploy thành công:

1. **Test trên nhiều devices:**
   - [ ] Desktop Chrome
   - [ ] Desktop Firefox
   - [ ] iPhone Safari
   - [ ] Android Chrome
   - [ ] iPad

2. **Chia sẻ với beta testers (5-10 người):**
   - [ ] Gửi link
   - [ ] Thu thập feedback
   - [ ] Fix bugs

3. **Thêm chức năng:**
   - [ ] SOFA calculator (xem IMPLEMENTATION_STREAMLIT.md)
   - [ ] Vancomycin calculator
   - [ ] ARDSNet ventilator
   - [ ] Charts & visualizations

4. **Tối ưu:**
   - [ ] Add caching
   - [ ] Optimize load time
   - [ ] Add error handling
   - [ ] Create user guide

---

## 📚 TÀI LIỆU THAM KHẢO

- **[Streamlit Documentation](https://docs.streamlit.io/)**
- **[Streamlit Gallery](https://streamlit.io/gallery)** - Ví dụ apps
- **[Streamlit Components](https://streamlit.io/components)** - Mở rộng chức năng
- **[IMPLEMENTATION_STREAMLIT.md](IMPLEMENTATION_STREAMLIT.md)** - Code chi tiết
- **[DEPLOYMENT_STREAMLIT.md](DEPLOYMENT_STREAMLIT.md)** - Deploy nâng cao

---

## ✅ CHECKLIST HOÀN THÀNH

- [ ] GitHub repo tạo xong
- [ ] Code push lên GitHub
- [ ] Streamlit Cloud account đã tạo
- [ ] App deployed thành công
- [ ] URL app hoạt động
- [ ] Test trên mobile OK
- [ ] Logo/branding đã thêm (optional)
- [ ] Share link với 3-5 người để test

---

## 🆘 HỖ TRỢ

**Streamlit Community:**
- Forum: https://discuss.streamlit.io/
- GitHub: https://github.com/streamlit/streamlit
- Discord: https://discord.gg/streamlit

**Clinical Assistant Support:**
- GitHub Issues: [YOUR_REPO]/issues
- Email: clinical-it@hospital.com

---

**🎉 Chúc mừng! App của bạn đã live tại:**  
**`https://clinical-assistant-yourname.streamlit.app`**

**Next: Đọc [IMPLEMENTATION_STREAMLIT.md](IMPLEMENTATION_STREAMLIT.md) để thêm calculators!**

