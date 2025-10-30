# 🩺 Clinical Assistant - Streamlit Edition

**Công cụ hỗ trợ lâm sàng toàn diện dành cho nhân viên y tế**

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

---

## 🌟 Tính Năng Chính

### 📊 **Thang Điểm Lâm Sàng (50+ Calculators)**
- **Tim Mạch (8):** CHA₂DS₂-VASc, HAS-BLED, SCORE2, SCORE2-OP, HEART, TIMI, GRACE, Framingham ✅
- **Cấp Cứu & Hồi Sức (5):** qSOFA, SOFA, APACHE II, SAPS II, MODS ✅ ⭐ **MỚI HOÀN THÀNH**
- **Hô Hấp (4):** CURB-65, PSI/PORT, Wells PE, SMART-COP ✅
- **Thần Kinh (5):** GCS, NIHSS, ICH Score, Hunt & Hess, mRS ✅
- **Tiêu Hóa - Gan Mật (4):** Child-Pugh, MELD, Glasgow-Blatchford, Rockall ✅
- **Huyết Học (3):** Wells DVT, 4Ts Score (HIT), DIC Score (ISTH) ✅
- **Thận (3):** KDIGO, RIFLE, AKIN (AKI staging) ✅
- **Chấn Thương (2):** RTS, ISS ✅
- **Chuyển Hóa (3):** Anion Gap, Corrected Calcium, FENa ✅
- **Và nhiều chuyên khoa khác...**

### 💊 **Kháng Sinh - Tính Liều & TDM**
- Tính CrCl (Cockcroft-Gault) với chuyển đổi đơn vị (µmol/L ↔ mg/dL)
- Vancomycin dosing & TDM
- Aminoglycoside dosing
- Tra cứu cơ sở dữ liệu kháng sinh

### 🔬 **Labs - Xét Nghiệm & Giải Thích** ⭐ NEW
- **CBC** - Complete Blood Count
- **BMP/CMP** - Metabolic Panels
- **LFT** - Liver Function Tests
- **Lipid Panel** - Cholesterol, Triglycerides
- **Cardiac Markers** - Troponin, BNP, CK-MB
- **Coagulation** - PT/INR, aPTT
- **Thyroid** - TSH, T3, T4
- **ABG** - Arterial Blood Gas Interpreter

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

### 🪟 Windows - Siêu Nhanh (Khuyến Nghị)

**Cách 1: Double-click file .bat** ⚡
```bash
1. Double-click: quick-start.bat
   → Chạy trực tiếp, nhanh nhất!

2. Hoặc: run.bat
   → Tự động kiểm tra & cài đặt dependencies

3. Lần đầu tiên: setup.bat
   → Tạo virtual environment & cài đặt
```

**Cách 2: Command Line**
```bash
# Clone repository
git clone https://github.com/drvietcanh/clinical-assistant.git
cd clinical-assistant

# Chạy nhanh
quick-start.bat

# Hoặc với kiểm tra dependencies
run.bat
```

### 🐧 Linux/Mac

```bash
# Clone repository
git clone https://github.com/drvietcanh/clinical-assistant.git
cd clinical-assistant

# Tạo virtual environment
python -m venv venv
source venv/bin/activate

# Cài đặt dependencies
pip install -r requirements.txt

# Chạy ứng dụng
python -m streamlit run app.py
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
├── 📄 Core Files
│   ├── app.py                      # Main entry point
│   ├── requirements.txt            # Dependencies
│   ├── quick-start.bat             # Quick launch (Windows) ⚡
│   ├── run.bat                     # Run with checks (Windows)
│   └── setup.bat                   # First-time setup (Windows)
│
├── 📁 Pages (Routers)
│   ├── 01_📊_Scores.py
│   ├── 02_💊_Antibiotics.py
│   ├── 03_🫁_Ventilator.py
│   ├── 04_📋_Protocols.py
│   └── 05_🔬_Labs.py               # NEW! ⭐
│
├── 📁 Scores Module (Modular by Specialty)
│   ├── config.py                   # Central config
│   ├── cardiology/                 # 8 calculators
│   │   ├── cha2ds2vasc.py
│   │   ├── hasbled.py
│   │   ├── score2.py, score2_op.py
│   │   ├── heart.py, timi.py, grace.py
│   │   └── framingham.py
│   ├── emergency/                  # 5 calculators
│   │   ├── qsofa.py, sofa.py
│   │   ├── apache2.py, saps2.py
│   │   └── mods.py
│   ├── respiratory/                # Respiratory scores
│   │   └── curb65.py
│   └── neurology/                  # Neurology scores
│       └── gcs.py
│
├── 📁 Antibiotics Module
│   ├── crcl.py                     # CrCl calculator
│   ├── vancomycin.py               # Vancomycin dosing
│   ├── aminoglycoside.py           # Aminoglycoside dosing
│   └── database.py                 # Antibiotic lookup
│
├── 📁 Labs Module ⭐ NEW
│   ├── cbc.py                      # Complete Blood Count
│   ├── bmp.py, cmp.py              # Metabolic panels
│   ├── lft.py                      # Liver Function Tests
│   ├── lipid.py                    # Lipid panel
│   ├── cardiac.py                  # Cardiac markers
│   ├── coag.py                     # Coagulation
│   ├── thyroid.py                  # Thyroid function
│   ├── abg.py                      # ABG interpreter
│   ├── converter.py                # Unit conversions
│   └── normal_ranges.py            # Reference ranges
│
├── 📁 Ventilator Module
│   ├── calculators.py              # ARDSNet, PBW
│   └── tables.py                   # PEEP/FiO2
│
├── 📁 Protocols Module
│   ├── emergency/
│   │   └── sepsis.py
│   ├── respiratory/
│   │   ├── copd.py
│   │   └── asthma.py
│   └── cardiology/
│       ├── acs.py
│       └── heart_failure.py
│
├── 📁 Data
│   ├── Antibiotics.csv
│   ├── Scores.csv
│   ├── Ventilator.csv
│   ├── Protocols.csv
│   └── Meta.csv
│
└── 📚 Documentation
    ├── README.md                   # This file
    ├── ARCHITECTURE.md             # Technical docs
    └── QUICKSTART_STREAMLIT.md     # Quick start guide
```

**Tổng:** 
- **5 modules chính** (Scores, Antibiotics, Labs ⭐, Ventilator, Protocols)
- **30+ calculators** implemented
- **100% modular** - Easy to maintain & extend
- **3 .bat files** cho Windows - Double-click to run! ⚡

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

### 🎯 **Đã Hoàn Thành (50+ Tools)**

**Scores (50+ calculators):** ⭐ **CẬP NHẬT MỚI**

**Cardiology (8/8):** CHA₂DS₂-VASc, HAS-BLED, SCORE2 ⭐, SCORE2-OP ⭐, HEART, TIMI, GRACE, Framingham ✅

**Emergency & Critical Care (5/5):** qSOFA, SOFA ⭐, APACHE II ⭐, SAPS II ⭐, MODS ⭐ ✅ **HOÀN THIỆN 100%**

**Respiratory (4/4):** CURB-65, PSI/PORT, Wells PE, SMART-COP ✅

**Neurology (5/5):** GCS, NIHSS, ICH Score, Hunt & Hess, mRS ✅

**GI/Hepatology (4/6):** Child-Pugh, MELD, Glasgow-Blatchford, Rockall ✅

**Hematology (3/3):** Wells DVT, 4Ts Score (HIT), DIC Score (ISTH) ✅

**Nephrology (3/3):** KDIGO, RIFLE, AKIN (AKI staging systems) ✅

**Trauma (2/4):** RTS (Revised Trauma Score), ISS (Injury Severity Score) ✅

**Metabolism (3/7):** Anion Gap, Corrected Calcium, FENa ✅

**Labs (9 panels):** ⭐ NEW
- CBC, BMP, CMP, LFT, Lipid
- Cardiac markers, Coagulation
- Thyroid, ABG interpreter ✅

**Antibiotics:**
- CrCl calculator (with unit conversion) ✅
- Vancomycin dosing ✅
- Aminoglycoside dosing ✅

**Ventilator:**
- ARDSNet calculator ✅
- PEEP/FiO2 tables ✅

**Protocols:**
- Sepsis bundle, COPD, Asthma ✅
- ACS, Heart Failure ✅

### 📋 **Kế Hoạch Phát Triển (60+ Calculators)**

**Scores cần bổ sung:**
- **Pediatrics:** PEWS, APGAR, Pediatric GCS
- **Obstetrics:** Bishop Score, Modified Bishop
- **Rheumatology:** DAS28, CDAI, SDAI, ACR Criteria, SLEDAI
- **Psychiatry:** PHQ-9, GAD-7, MMSE, MoCA, CAM, CIWA-Ar, COWS
- **Surgery:** ASA, P-POSSUM, RCRI, Caprini, Aldrete, Mallampati
- **Infectious Disease:** SIRS, Pitt Bacteremia, MASCC, Centor, FeverPAIN
- **Dermatology:** PASI, SCORAD, DLQI, Burn TBSA, Parkland
- **Oncology:** ECOG, Karnofsky, Palliative Performance, CIPN
- **ENT:** Epworth, STOP-BANG
- **Và nhiều specialty khác...**

**Tính năng khác:**
- Unit tests cho các công thức
- Antibiotic database mở rộng
- Drug interaction checker
- Clinical pathways
- Export/Print results

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
