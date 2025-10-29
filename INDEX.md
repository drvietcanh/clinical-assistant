# 📚 Clinical Assistant - Navigation Index

> **Hướng dẫn nhanh:** Tìm đúng tài liệu cho nhu cầu của bạn

---

## 🎯 BẠN MUỐN LÀM GÌ?

### 🚀 "Tôi muốn bắt đầu ngay!"
→ **[QUICKSTART.md](QUICKSTART.md)** - 30 phút có ứng dụng chạy

### 📖 "Tôi muốn hiểu tổng quan dự án"
→ **[README.md](README.md)** - Giới thiệu đầy đủ về Clinical Assistant

### 🗺️ "Tôi muốn xem lộ trình phát triển"
→ **[ROADMAP.md](ROADMAP.md)** - Kế hoạch chi tiết 12 tuần

### 💻 "Tôi muốn code một module mới"
→ **[IMPLEMENTATION_GUIDE.md](IMPLEMENTATION_GUIDE.md)** - Hướng dẫn code từng bước

### ⚙️ "Tôi muốn deploy lên production"
→ **[DEPLOYMENT.md](DEPLOYMENT.md)** - Deploy & DevOps guide

### 📚 "Tôi cần tài liệu tham khảo lâm sàng"
→ **[RESOURCES.md](RESOURCES.md)** - Guidelines, citations, links

### 🔍 "Tôi muốn xem các app tương tự"
→ **[SIMILAR_APPS.md](SIMILAR_APPS.md)** - Phân tích MDCalc, UpToDate, etc.

### 📊 "Tôi muốn xem tóm tắt nhanh"
→ **[SUMMARY.md](SUMMARY.md)** - Executive summary 1 trang

### 📝 "Tôi muốn biết có gì thay đổi"
→ **[CHANGELOG.md](CHANGELOG.md)** - Lịch sử versions

---

## 📂 TÀI LIỆU THEO VAI TRÒ

### 👨‍⚕️ Bác sĩ / Người dùng cuối
```
1. README.md         - Hiểu ứng dụng làm gì
2. QUICKSTART.md     - Cách truy cập và sử dụng
3. RESOURCES.md      - Tài liệu lâm sàng tham khảo
```

### 👨‍💻 Lập trình viên
```
1. README.md              - Technical overview
2. QUICKSTART.md          - Setup development environment
3. IMPLEMENTATION_GUIDE.md - Code chi tiết
4. templates/             - Code templates
5. DEPLOYMENT.md          - CI/CD workflow
```

### 👨‍💼 Quản lý dự án
```
1. SUMMARY.md        - Executive summary
2. ROADMAP.md        - Timeline & milestones
3. CHANGELOG.md      - Version history
4. SIMILAR_APPS.md   - Market analysis
```

### 🏥 Quản trị viên hệ thống
```
1. QUICKSTART.md     - Deployment instructions
2. DEPLOYMENT.md     - Operations & monitoring
3. RESOURCES.md      - Support resources
```

### 🎓 Nhà nghiên cứu / Học viên
```
1. README.md         - Project overview
2. ROADMAP.md        - Development methodology
3. SIMILAR_APPS.md   - Literature review
4. RESOURCES.md      - Academic references
```

---

## 📁 CẤU TRÚC THƯ MỤC

### 📖 Documentation (10 files)
```
├── INDEX.md              ⭐ BẠN ĐANG Ở ĐÂY
├── README.md             → Tổng quan dự án
├── QUICKSTART.md         → Bắt đầu nhanh (30 phút)
├── SUMMARY.md            → Tóm tắt 1 trang
├── ROADMAP.md            → Lộ trình phát triển (40+ trang)
├── IMPLEMENTATION_GUIDE.md → Hướng dẫn code chi tiết
├── DEPLOYMENT.md         → Deploy & DevOps
├── RESOURCES.md          → Tài liệu tham khảo
├── SIMILAR_APPS.md       → Phân tích đối thủ
└── CHANGELOG.md          → Lịch sử versions
```

### 💾 Data (data-csv/)
```
├── Meta.csv              → Version control
├── Scores.csv            → Scoring systems data
├── Antibiotics.csv       → Drug dosing data
├── Ventilator.csv        → Ventilator settings
└── Protocols.csv         → Clinical protocols
```

### 🖥️ Backend (server/)
```
├── Code.gs               → Web app entry (doGet)
├── Core.gs               → Core utilities
├── Scores.api.gs         → Scores API
├── Antibiotics.api.gs    → Antibiotics API
├── Vent.api.gs          → Ventilator API
└── Protocols.api.gs     → Protocols API
```

### 🎨 Frontend (web/)
```
├── index.html           → Entry + navigation
├── styles.html          → Global CSS + router
├── app.html             → Shared utilities
├── scores.html          → Scores module
├── antibiotics.html     → Antibiotics module
├── vent.html           → Ventilator module
└── protocols.html      → Protocols module
```

### 📝 Templates (templates/)
```
├── module-template.html → Template cho module mới
├── api-template.gs      → Template API backend
└── data-template.csv    → Template dữ liệu
```

### ⚙️ Config
```
├── .claspignore         → Clasp ignore file
├── .gitignore           → Git ignore
└── appsscript.json      → Apps Script config
```

---

## 🔍 TÌM THEO CHỦ ĐỀ

### Clinical Content
- **Scoring systems** → IMPLEMENTATION_GUIDE.md > Phần 1
- **Antibiotics** → IMPLEMENTATION_GUIDE.md > Phần 2
- **Ventilator** → IMPLEMENTATION_GUIDE.md > Phần 3
- **Protocols** → IMPLEMENTATION_GUIDE.md > Phần 4
- **Guidelines** → RESOURCES.md

### Technical
- **Architecture** → README.md > "Kiến trúc"
- **API design** → templates/api-template.gs
- **Frontend patterns** → templates/module-template.html
- **Deployment** → DEPLOYMENT.md
- **Performance** → DEPLOYMENT.md > "Monitoring"

### Project Management
- **Timeline** → ROADMAP.md
- **Budget** → SUMMARY.md > "Cost estimate"
- **Team** → SUMMARY.md > "Team & Roles"
- **Risks** → SUMMARY.md > "Risks & Mitigation"
- **Success metrics** → SUMMARY.md > "Success metrics"

### Competitive Analysis
- **MDCalc** → SIMILAR_APPS.md > "#1"
- **UpToDate** → SIMILAR_APPS.md > "#3"
- **Epocrates** → SIMILAR_APPS.md > "#4"
- **Feature comparison** → SIMILAR_APPS.md > "Comparison table"

---

## 🎓 LEARNING PATHS

### Path 1: Complete Beginner
```
Day 1: README.md (1h)
       ↓
Day 2: QUICKSTART.md → Deploy (2h)
       ↓
Day 3: Test ứng dụng, đọc RESOURCES.md (2h)
       ↓
Week 2: IMPLEMENTATION_GUIDE.md → Thêm module đầu tiên (10h)
```

### Path 2: Experienced Developer
```
Hour 1: SUMMARY.md (quick overview)
        ↓
Hour 2: Code review (server/ + web/)
        ↓
Hour 3: DEPLOYMENT.md → Setup clasp → Deploy
        ↓
Day 2+: IMPLEMENTATION_GUIDE.md → Build features
```

### Path 3: Clinical Informaticist
```
Day 1: README.md + ROADMAP.md (hiểu scope)
       ↓
Day 2: RESOURCES.md (verify clinical content)
       ↓
Day 3: SIMILAR_APPS.md (benchmark)
       ↓
Week 2: Review data-csv/ → Validate formulas
```

### Path 4: Project Manager
```
Meeting 1: SUMMARY.md (present to stakeholders)
           ↓
Meeting 2: ROADMAP.md (discuss timeline)
           ↓
Week 1: CHANGELOG.md (track progress)
        ↓
Monthly: DEPLOYMENT.md > Analytics (review KPIs)
```

---

## 🔗 EXTERNAL LINKS

### Official Documentation
- [Google Apps Script](https://developers.google.com/apps-script)
- [Google Sheets API](https://developers.google.com/sheets/api)
- [clasp CLI](https://github.com/google/clasp)

### Clinical Guidelines
- [MDCalc](https://www.mdcalc.com/) - Calculator reference
- [UpToDate](https://www.uptodate.com/) - Clinical content
- [IDSA Guidelines](https://www.idsociety.org/practice-guidelines/)

### Community
- [Stack Overflow - Apps Script](https://stackoverflow.com/questions/tagged/google-apps-script)
- [GitHub - Medical Calculators](https://github.com/topics/medical-calculator)

---

## 🆘 TROUBLESHOOTING

### "Tôi không biết bắt đầu từ đâu"
→ Đọc [QUICKSTART.md](QUICKSTART.md) từ đầu đến cuối, follow từng bước

### "Code bị lỗi, không chạy"
→ Check [DEPLOYMENT.md > Troubleshooting](DEPLOYMENT.md#troubleshooting)

### "Tôi muốn thêm calculator mới"
→ Dùng [templates/module-template.html](templates/module-template.html)  
→ Đọc [IMPLEMENTATION_GUIDE.md](IMPLEMENTATION_GUIDE.md) phần tương ứng

### "Công thức tính toán sai"
→ Check [RESOURCES.md](RESOURCES.md) để verify với guideline gốc  
→ Report issue với clinical team

### "App chạy chậm"
→ Check [DEPLOYMENT.md > Performance](DEPLOYMENT.md#monitoring--maintenance)

---

## 📊 DOCUMENT STATUS

| File | Status | Last Updated | Pages |
|------|--------|--------------|-------|
| INDEX.md | ✅ Complete | 2025-10-29 | 1 |
| README.md | ✅ Complete | 2025-10-29 | 3 |
| QUICKSTART.md | ✅ Complete | 2025-10-29 | 4 |
| SUMMARY.md | ✅ Complete | 2025-10-29 | 5 |
| ROADMAP.md | ✅ Complete | 2025-10-29 | 42 |
| IMPLEMENTATION_GUIDE.md | ✅ Complete | 2025-10-29 | 30 |
| DEPLOYMENT.md | ✅ Complete | 2025-10-29 | 20 |
| RESOURCES.md | ✅ Complete | 2025-10-29 | 12 |
| SIMILAR_APPS.md | ✅ Complete | 2025-10-29 | 18 |
| CHANGELOG.md | ✅ Complete | 2025-10-29 | 2 |

**Total:** 137 pages of documentation

---

## ✅ QUICK CHECKLIST

### Đọc trước khi code
- [ ] README.md
- [ ] QUICKSTART.md
- [ ] IMPLEMENTATION_GUIDE.md (phần liên quan)
- [ ] templates/ (choose template)

### Đọc trước khi deploy
- [ ] DEPLOYMENT.md
- [ ] CHANGELOG.md (update version)
- [ ] Test checklist in DEPLOYMENT.md

### Đọc định kỳ
- [ ] RESOURCES.md (monthly - check for new guidelines)
- [ ] CHANGELOG.md (after each deploy)
- [ ] SIMILAR_APPS.md (quarterly - competitive analysis)

---

## 🎯 RECOMMENDED READING ORDER

### For First-Time Users
```
1. README.md              (15 min) - Hiểu dự án
2. QUICKSTART.md          (30 min) - Deploy & test
3. SUMMARY.md             (10 min) - Big picture
```
**Total: ~1 hour to get started**

### For Developers
```
1. README.md              (15 min)
2. SUMMARY.md             (10 min)
3. IMPLEMENTATION_GUIDE.md (2 hours)
4. templates/             (30 min)
5. DEPLOYMENT.md          (1 hour)
```
**Total: ~4 hours to full proficiency**

### For Project Stakeholders
```
1. SUMMARY.md             (10 min)
2. ROADMAP.md             (30 min)
3. SIMILAR_APPS.md        (30 min)
```
**Total: ~1 hour for decision-making**

---

## 📞 NEED HELP?

### Internal Support
- 📧 Email: clinical-it@hospital.com
- 💬 Slack: #clinical-assistant
- 📞 Phone: ext. 1234

### Report Issues
- 🐛 Bug: [GitHub Issues](https://github.com/your-repo/issues)
- 💡 Feature request: Same as above
- 📖 Doc improvement: Pull request

---

## 🌟 QUICK LINKS

| What | Where |
|------|-------|
| **Start coding now** | [QUICKSTART.md](QUICKSTART.md) |
| **See full roadmap** | [ROADMAP.md](ROADMAP.md) |
| **Copy-paste templates** | [templates/](templates/) |
| **Clinical references** | [RESOURCES.md](RESOURCES.md) |
| **Deploy to production** | [DEPLOYMENT.md](DEPLOYMENT.md) |
| **Version history** | [CHANGELOG.md](CHANGELOG.md) |

---

## 📅 UPDATE SCHEDULE

This index will be updated:
- **After each major version** - Add new files, restructure
- **Monthly** - Update links, status
- **As needed** - Fix broken links, add FAQs

**Last comprehensive review:** 2025-10-29

---

**🎉 Happy coding! Chúc bạn thành công với Clinical Assistant!**

---

<p align="center">
  <sub>INDEX.md - Navigation hub for Clinical Assistant project</sub>
  <br>
  <sub>Created with ❤️ for healthcare professionals</sub>
</p>

