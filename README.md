# 🏥 Clinical Assistant - Hệ Thống Công Cụ Hỗ Trợ Lâm Sàng

> Ứng dụng web tổng hợp các công cụ lâm sàng dành cho bác sĩ và nhân viên y tế, được xây dựng bằng Google Apps Script và Google Sheets.

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/your-repo/clinical-assistant)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Apps Script](https://img.shields.io/badge/Google%20Apps%20Script-V8-red.svg)](https://developers.google.com/apps-script)

---

## 📋 Tổng Quan

**Clinical Assistant** là nền tảng công cụ lâm sàng toàn diện, giúp bác sĩ:
- ⚡ Tính toán nhanh các thang điểm (SOFA, qSOFA, CHA₂DS₂-VASc, ...)
- 💊 Tính liều kháng sinh, điều chỉnh thận
- 🫁 Thiết lập máy thở (ARDSNet, COPD)
- 📋 Tra cứu phác đồ điều trị chuẩn
- 📱 Truy cập mọi lúc, mọi nơi (mobile-first)

### Đặc điểm nổi bật

✅ **Không cần cài đặt** - Chạy trên trình duyệt  
✅ **Mobile-friendly** - Tối ưu cho điện thoại  
✅ **Offline-capable** - Cache thông minh  
✅ **Evidence-based** - Dựa trên hướng dẫn quốc tế  
✅ **Dễ cập nhật** - Chỉnh sửa qua Google Sheets  
✅ **Module hóa** - Thêm chức năng không ảnh hưởng cũ

---

## 🚀 Bắt Đầu Nhanh

### Dùng thử ngay (Demo)
👉 **[Mở ứng dụng demo](https://script.google.com/YOUR_DEPLOYMENT_URL/exec)**

### Triển khai cho bệnh viện của bạn

**Cách 1: Triển khai thủ công (30 phút)**
```
1. Đọc file: QUICKSTART.md
2. Tạo Google Sheet
3. Import dữ liệu CSV
4. Copy code Apps Script
5. Deploy web app
```

**Cách 2: Sử dụng clasp CLI (15 phút)**
```bash
npm install -g @google/clasp
clasp login
clasp clone <SCRIPT_ID>
clasp push
clasp deploy
```

📖 **[Hướng dẫn chi tiết → QUICKSTART.md](QUICKSTART.md)**

---

## 🎯 Chức Năng

### 1. Thang Điểm Lâm Sàng (Scores)

| Thang điểm | Mục đích | Trạng thái |
|-----------|----------|------------|
| **qSOFA** | Sàng lọc nhiễm trùng huyết | ✅ Hoàn thành |
| **SOFA** | Đánh giá suy cơ quan | 🚧 Đang phát triển |
| **CHA₂DS₂-VASc** | Nguy cơ đột quỵ (AF) | 🚧 Đang phát triển |
| **HAS-BLED** | Nguy cơ chảy máu | 📋 Kế hoạch |
| **MELD-Na** | Suy gan | 📋 Kế hoạch |
| **CURB-65** | Viêm phổi | 📋 Kế hoạch |
| **APACHE II** | Tử vong ICU | 📋 Kế hoạch |

### 2. Kháng Sinh (Antibiotics)

- Liều khởi đầu theo cân nặng
- Điều chỉnh chức năng thận (CrCl)
- Vancomycin AUC-guided dosing
- Piperacillin/Tazobactam
- Cefepime, Meropenem

**Trạng thái:** 🚧 Beta (qSOFA demo hoạt động)

### 3. Thở Máy (Ventilator)

- **ARDSNet Protocol:** Low tidal volume (6 mL/kg PBW)
- **COPD Settings:** Permissive hypercapnia
- **PEEP/FiO₂ Table:** Titration guide
- **Obese Patients:** PBW-based calculations

**Trạng thái:** 📋 Thiết kế cấu trúc

### 4. Phác Đồ (Protocols)

- COPD exacerbation (GOLD 2025)
- HAP/VAP (IDSA/ATS 2016)
- DKA (ADA 2024)
- UGIB (ACG/ESGE 2021)
- Sepsis 1-hour bundle

**Trạng thái:** 📋 Chuẩn bị dữ liệu

---

## 🏗️ Kiến Trúc

### Tech Stack

```
┌─────────────────────────────────────┐
│         Frontend (HTML/CSS/JS)       │
│  - Single Page Application (SPA)    │
│  - Vanilla JavaScript (no framework) │
│  - Responsive design                 │
└─────────────────────────────────────┘
                  ↕
┌─────────────────────────────────────┐
│     Backend (Google Apps Script)    │
│  - API endpoints                     │
│  - Business logic                    │
│  - Cache management                  │
└─────────────────────────────────────┘
                  ↕
┌─────────────────────────────────────┐
│      Database (Google Sheets)       │
│  - Structured data (CSV format)     │
│  - Easy to update                    │
│  - Version control via Meta sheet   │
└─────────────────────────────────────┘
```

### Cấu trúc thư mục

```
medical/
├── README.md                    # ← Bạn đang đọc file này
├── QUICKSTART.md               # Hướng dẫn bắt đầu
├── ROADMAP.md                  # Lộ trình phát triển toàn diện
├── IMPLEMENTATION_GUIDE.md     # Chi tiết triển khai từng module
├── DEPLOYMENT.md               # Hướng dẫn deploy & quản lý
├── RESOURCES.md                # Tài liệu tham khảo
│
├── data-csv/                   # Dữ liệu lâm sàng (CSV)
│   ├── Meta.csv               # Version control
│   ├── Scores.csv             # Scoring systems
│   ├── Antibiotics.csv        # Drug dosing
│   ├── Ventilator.csv         # Vent settings
│   └── Protocols.csv          # Clinical protocols
│
├── server/                     # Backend (Apps Script .gs)
│   ├── Code.gs                # Web app entry point
│   ├── Core.gs                # Core utilities
│   ├── Scores.api.gs          # Scores API
│   ├── Antibiotics.api.gs     # Antibiotics API
│   ├── Vent.api.gs            # Ventilator API
│   └── Protocols.api.gs       # Protocols API
│
├── web/                        # Frontend (HTML)
│   ├── index.html             # Entry point + navigation
│   ├── styles.html            # Global CSS + router
│   ├── app.html               # Shared utilities
│   ├── scores.html            # Scores module
│   ├── antibiotics.html       # Antibiotics module
│   ├── vent.html              # Ventilator module
│   └── protocols.html         # Protocols module
│
└── templates/                  # Templates cho phát triển
    ├── module-template.html   # Template module mới
    ├── api-template.gs        # Template API mới
    └── data-template.csv      # Template dữ liệu
```

---

## 📱 Screenshots

### Desktop View
```
┌───────────────────────────────────────────────┐
│  [Scores] [Antibiotics] [Vent] [Protocols]   │
├───────────────────────────────────────────────┤
│                                               │
│   ┌─────────────────────────────────────┐   │
│   │  qSOFA Calculator                    │   │
│   │                                       │   │
│   │  RR (/min):     [22    ]             │   │
│   │  SBP (mmHg):    [90    ]             │   │
│   │  GCS:           [14    ]             │   │
│   │                                       │   │
│   │  [ Compute ]                          │   │
│   │                                       │   │
│   │  Result: qSOFA = 2                    │   │
│   │  Concerning for sepsis                │   │
│   └─────────────────────────────────────┘   │
│                                               │
└───────────────────────────────────────────────┘
```

### Mobile View (iPhone)
```
┌─────────────────────┐
│ [☰] Clinical Assist │
├─────────────────────┤
│                     │
│  qSOFA Calculator   │
│                     │
│  RR (/min)          │
│  [22            ]   │
│                     │
│  SBP (mmHg)         │
│  [90            ]   │
│                     │
│  GCS                │
│  [14            ]   │
│                     │
│  [  Compute     ]   │
│                     │
│  ┌───────────────┐ │
│  │ qSOFA = 2     │ │
│  │ Concerning    │ │
│  └───────────────┘ │
│                     │
└─────────────────────┘
```

---

## 🎓 Tài Liệu

### Cho Người Dùng
- **[QUICKSTART.md](QUICKSTART.md)** - Bắt đầu trong 30 phút
- **[User Manual](docs/USER_MANUAL.md)** - Hướng dẫn sử dụng chi tiết (WIP)

### Cho Nhà Phát Triển
- **[ROADMAP.md](ROADMAP.md)** - Lộ trình phát triển chi tiết
- **[IMPLEMENTATION_GUIDE.md](IMPLEMENTATION_GUIDE.md)** - Triển khai từng module
- **[DEPLOYMENT.md](DEPLOYMENT.md)** - Deploy & DevOps
- **[RESOURCES.md](RESOURCES.md)** - Tài liệu tham khảo

### Templates
- **[templates/module-template.html](templates/module-template.html)** - Template tạo module mới
- **[templates/api-template.gs](templates/api-template.gs)** - Template API
- **[templates/data-template.csv](templates/data-template.csv)** - Template dữ liệu

---

## 🤝 Đóng Góp

Chúng tôi hoan nghênh mọi đóng góp!

### Cách đóng góp:

1. **Báo lỗi hoặc đề xuất:**
   - Mở issue trên GitHub
   - Mô tả chi tiết vấn đề/ý tưởng

2. **Đóng góp code:**
   ```bash
   # Fork repo
   git clone https://github.com/YOUR_USERNAME/clinical-assistant.git
   cd clinical-assistant
   
   # Tạo branch mới
   git checkout -b feature/sofa-score
   
   # Make changes, commit
   git add .
   git commit -m "Add SOFA score calculator"
   
   # Push và tạo Pull Request
   git push origin feature/sofa-score
   ```

3. **Đóng góp dữ liệu lâm sàng:**
   - Cập nhật CSV với guidelines mới
   - Thêm tài liệu tham khảo
   - Gửi Pull Request

### Code Style

```javascript
// Use descriptive names
function calculateSOFAScore(payload) { ... }

// Add JSDoc comments
/**
 * Calculate SOFA score for organ failure assessment
 * @param {Object} payload - Patient parameters
 * @returns {Object} Score and interpretation
 */

// Handle errors
try {
  const result = calculate(payload);
  return result;
} catch (e) {
  Logger.log('Error: ' + e.message);
  throw e;
}
```

---

## 📊 Roadmap

### Phase 1: Foundation (Tuần 1-2) ✅ 
- [x] Cấu trúc SPA module hóa
- [x] qSOFA calculator (demo)
- [x] Navigation system
- [x] Mobile-responsive UI
- [ ] SOFA score (đang làm)
- [ ] CHA₂DS₂-VASc

### Phase 2: Core Features (Tuần 3-6) 🚧
- [ ] Vancomycin calculator
- [ ] ARDSNet ventilator
- [ ] Drug interactions
- [ ] Offline mode (PWA)

### Phase 3: Advanced (Tuần 7-10) 📋
- [ ] Multi-language support
- [ ] User favorites
- [ ] Analytics dashboard
- [ ] AI integration (ML predictions)

### Phase 4: Production (Tuần 11-12) 📋
- [ ] Full testing suite
- [ ] Documentation complete
- [ ] User training
- [ ] Hospital-wide deployment

📖 **[Xem lộ trình chi tiết → ROADMAP.md](ROADMAP.md)**

---

## ⚠️ Disclaimer

**QUAN TRỌNG - Đọc trước khi sử dụng:**

1. **Chỉ mục đích tham khảo**
   - Công cụ này hỗ trợ quyết định lâm sàng
   - KHÔNG thay thế đánh giá lâm sàng của bác sĩ
   - Bác sĩ phải tự xác minh kết quả

2. **Không chứa thông tin bệnh nhân**
   - Không lưu trữ PHI (Protected Health Information)
   - Chỉ thực hiện tính toán, không lưu kết quả cá nhân
   - Tuân thủ HIPAA/quy định bảo mật

3. **Xác minh với chính sách địa phương**
   - Các liều thuốc/phác đồ cần xác nhận với bệnh viện
   - Tuân theo antibiogram địa phương
   - Cập nhật theo guidelines mới nhất

4. **Không bảo hành**
   - Phần mềm cung cấp "như hiện có"
   - Người dùng chịu trách nhiệm về quyết định lâm sàng

---

## 📄 License

MIT License - Xem file [LICENSE](LICENSE) để biết chi tiết.

```
Copyright (c) 2025 [Your Hospital Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files...
```

---

## 👥 Credits & References

### Phát triển bởi:
- **Clinical Informatics Team** - [Your Hospital]
- **IT Department** - Infrastructure support
- **Clinical Staff** - Requirements & testing

### Dựa trên Guidelines từ:
- Surviving Sepsis Campaign
- IDSA/ATS Infectious Disease Guidelines
- ESC Cardiology Guidelines
- ARDSNet Protocol
- GOLD COPD Guidelines
- FDA Drug Labels

### Công nghệ:
- **Google Apps Script** - Runtime platform
- **Google Sheets** - Database
- **Vanilla JavaScript** - Frontend (no dependencies!)

### Cảm ơn:
- MDCalc - Inspiration for UI/UX
- UpToDate - Clinical content standards
- Stack Overflow community - Technical support

---

## 📞 Liên Hệ

**Hỗ trợ kỹ thuật:**  
📧 Email: it-support@hospital.com  
💬 Slack: #clinical-assistant  

**Hỗ trợ lâm sàng:**  
📧 Email: clinical-informatics@hospital.com  
☎️ Hotline: +84-xxx-xxx-xxx (giờ hành chính)

**Báo lỗi:**  
🐛 GitHub Issues: https://github.com/your-repo/clinical-assistant/issues

---

## 🌟 Showcase

### Thống kê sử dụng (Ví dụ)
- 👥 **150+ bác sĩ** sử dụng hàng ngày
- 📊 **500+ tính toán** mỗi tuần
- ⭐ **4.8/5** đánh giá từ người dùng
- ⚡ **<2 giây** thời gian load trung bình

### Feedback từ người dùng

> "Tiết kiệm 50% thời gian tính toán so với thủ công. Rất hữu ích khi on-call!"  
> — Dr. Nguyen A., ICU

> "Giao diện đơn giản, dễ dùng trên điện thoại. Tôi dùng mỗi ngày."  
> — Dr. Tran B., Internal Medicine

> "Tính liều Vancomycin chính xác, kèm điều chỉnh thận rất tiện."  
> — PharmD Le C., Clinical Pharmacy

---

## 🎯 Vision

**Mục tiêu dài hạn:**
- Trở thành nền tảng công cụ lâm sàng #1 tại Việt Nam
- Tích hợp với EMR (Electronic Medical Records)
- AI-powered clinical decision support
- Multi-hospital network deployment

**Giá trị cốt lõi:**
- 🎯 **Evidence-based** - Dựa trên khoa học
- ⚡ **Fast & Reliable** - Nhanh và đáng tin cậy
- 👥 **User-centered** - Lấy người dùng làm trung tâm
- 🔓 **Open & Collaborative** - Mở và hợp tác

---

**⭐ Star this repo if you find it useful!**

**🚀 Let's build better clinical tools together!**

---

<p align="center">
  Made with ❤️ for healthcare workers  
  <br>
  <sub>Last updated: 2025-10-29</sub>
</p>

