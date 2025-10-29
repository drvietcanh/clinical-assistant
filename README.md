# 🩺 Clinical Assistant - Streamlit Edition

**Công cụ hỗ trợ lâm sàng toàn diện dành cho nhân viên y tế**

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

---

## 🌟 Tính Năng Chính

### 📊 **Thang Điểm Lâm Sàng (100+ Calculators)**
- **Tim Mạch:** CHA₂DS₂-VASc, HAS-BLED, SCORE2, SCORE2-OP, HEART, TIMI, GRACE
- **Cấp Cứu & Hồi Sức:** qSOFA, SOFA, APACHE II, SAPS II
- **Hô Hấp:** CURB-65, PSI/PORT, Wells PE, BODE Index
- **Thần Kinh:** GCS, NIHSS, ICH Score, Hunt & Hess, mRS
- **Tiêu Hóa:** MELD, MELD-Na, Child-Pugh, Rockall, Glasgow-Blatchford
- **Thận:** RIFLE, AKIN, KDIGO
- **Và nhiều chuyên khoa khác...**

### 💊 **Kháng Sinh - Tính Liều & TDM**
- Tính CrCl (Cockcroft-Gault) với chuyển đổi đơn vị
- Vancomycin dosing & TDM
- Aminoglycoside dosing
- Tra cứu cơ sở dữ liệu kháng sinh

### 🫁 **Thở Máy - Hỗ Trợ Hô Hấp**
- ARDSNet Tidal Volume Calculator
- Bảng PEEP/FiO2 (ARDSNet Protocol)
- Cài đặt ban đầu theo bệnh lý

### 📋 **Phác Đồ Điều Trị**
- Sepsis 1-Hour Bundle (SSC 2021)
- COPD Exacerbation
- Acute Asthma
- ACS Protocol
- Acute Heart Failure

---

## 🚀 Quick Start

### Cài Đặt

```bash
# Clone repository
git clone https://github.com/drvietcanh/clinical-assistant.git
cd clinical-assistant

# Tạo virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# hoặc
venv\Scripts\activate  # Windows

# Cài đặt dependencies
pip install -r requirements.txt

# Chạy ứng dụng
streamlit run app.py
```

### Deploy lên Streamlit Cloud

1. Push code lên GitHub
2. Truy cập https://streamlit.io/cloud
3. Connect GitHub repository
4. Deploy!

**→ Xem hướng dẫn chi tiết:** [QUICKSTART_STREAMLIT.md](QUICKSTART_STREAMLIT.md)

---

## 📂 Cấu Trúc Project

```
medical/
├── app.py                      # Main entry point
├── pages/                      # Streamlit pages (routers)
│   ├── 01_📊_Scores.py
│   ├── 02_💊_Antibiotics.py
│   ├── 03_🫁_Ventilator.py
│   └── 04_📋_Protocols.py
│
├── scores/                     # Scores module (modular)
│   ├── config.py
│   ├── cardiology.py
│   ├── emergency.py
│   ├── respiratory.py
│   └── neurology.py
│
├── antibiotics/                # Antibiotics module
│   ├── calculators.py
│   └── database.py
│
├── ventilator/                 # Ventilator module
│   ├── calculators.py
│   └── tables.py
│
└── protocols/                  # Protocols module
    ├── emergency.py
    ├── respiratory.py
    └── cardiology.py
```

**→ Xem chi tiết:** [ARCHITECTURE.md](ARCHITECTURE.md)

---

## 💡 Ưu Điểm

### ✅ **Modular Architecture**
- Mỗi calculator là 1 function độc lập
- Dễ bảo trì, dễ mở rộng
- Nhiều người có thể làm song song

### ✅ **Unit Conversion**
- Creatinine: mg/dL ↔ µmol/L
- Cholesterol: mg/dL ↔ mmol/L
- Urea: mg/dL ↔ mmol/L

### ✅ **Evidence-Based**
- Dựa trên hướng dẫn quốc tế
- ESC, AHA/ACC, IDSA, SSC...
- Cập nhật thường xuyên

### ✅ **Mobile-Friendly**
- Giao diện responsive
- Tối ưu cho điện thoại/tablet
- Truy cập mọi lúc, mọi nơi

### ✅ **Vietnamese Localization**
- Giao diện tiếng Việt
- Dễ sử dụng cho bác sĩ Việt Nam

---

## 📊 Tính Năng Nổi Bật

### 🎯 **Đã Hoàn Thành (12 Calculators)**

1. **qSOFA** - Sàng lọc sepsis ✅
2. **CHA₂DS₂-VASc** - Nguy cơ đột quỵ (Rung nhĩ) ✅
3. **HAS-BLED** - Nguy cơ chảy máu ✅
4. **SCORE2** - Nguy cơ tim mạch 10 năm (40-69 tuổi) ✅
5. **SCORE2-OP** - Nguy cơ tim mạch (≥70 tuổi) ✅
6. **CURB-65** - Mức độ nặng viêm phổi ✅
7. **GCS** - Mức độ ý thức ✅
8. **CrCl** - Độ lọc cầu thận (với unit conversion) ✅
9. **ARDSNet** - Tidal volume calculator ✅
10. **PEEP/FiO2 Table** - ARDSNet protocol ✅
11. **Sepsis Bundle** - Sepsis 1-hour bundle ✅

### 🚧 **Đang Phát Triển (8 Calculators)**

- HEART Score, TIMI, GRACE, Framingham
- Vancomycin, Aminoglycoside dosing
- COPD, Asthma protocols
- ACS, Heart Failure protocols

### 📋 **Kế Hoạch (80+ Calculators)**

- Tất cả các specialty còn lại
- Antibiotic database
- Nhiều protocols hơn

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit 1.28+
- **Backend:** Python 3.9+
- **Data:** Pandas, NumPy
- **Deployment:** Streamlit Cloud
- **Version Control:** Git/GitHub

---

## 📚 Tài Liệu

- [QUICKSTART_STREAMLIT.md](QUICKSTART_STREAMLIT.md) - Hướng dẫn bắt đầu nhanh
- [ARCHITECTURE.md](ARCHITECTURE.md) - Kiến trúc chi tiết
- [DEPLOYMENT.md](DEPLOYMENT.md) - Hướng dẫn triển khai

---

## 🤝 Đóng Góp

### Cách đóng góp:

1. Fork repository
2. Tạo branch mới (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Tạo Pull Request

### Thêm Calculator Mới:

```python
# Thêm vào file specialty tương ứng (vd: scores/cardiology.py)
def render_new_calculator():
    """New Calculator Description"""
    st.subheader("🔥 New Calculator")
    # Implementation here
    ...

# Thêm vào router
def render_cardiology_calculator(calculator_id):
    calculators = {
        ...
        "New Calculator": render_new_calculator,
    }
```

**→ Xem chi tiết:** [ARCHITECTURE.md](ARCHITECTURE.md#-cách-thêm-tính-năng-mới)

---

## ⚠️ Disclaimer

**Clinical Assistant** là công cụ hỗ trợ lâm sàng, **KHÔNG PHẢI** để thay thế đánh giá và quyết định lâm sàng của bác sĩ.

- Chỉ mục đích tham khảo
- Luôn xác minh với hướng dẫn địa phương
- Luôn sử dụng clinical judgment
- Luôn cá thể hóa theo bệnh nhân

---

## 📧 Liên Hệ

- **Developer:** DRVIETCANH
- **GitHub:** [@drvietcanh](https://github.com/drvietcanh)
- **Repository:** [clinical-assistant](https://github.com/drvietcanh/clinical-assistant)

---

## 📄 License

MIT License - Xem [LICENSE](LICENSE) để biết thêm chi tiết.

---

## 🙏 Acknowledgments

- **Streamlit Team** - Amazing framework
- **Clinical Guidelines Organizations** - ESC, AHA/ACC, IDSA, SSC
- **Medical Community** - Feedback và contributions

---

## 📈 Stats

![GitHub stars](https://img.shields.io/github/stars/drvietcanh/clinical-assistant?style=social)
![GitHub forks](https://img.shields.io/github/forks/drvietcanh/clinical-assistant?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/drvietcanh/clinical-assistant?style=social)

---

**Made with ❤️ for healthcare professionals**

**Last Updated:** 2025-10-29
