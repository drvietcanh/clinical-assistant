# 🎯 BẮT ĐẦU TẠI ĐÂY - Clinical Assistant Streamlit

> **Tôi mới vào dự án, nên đọc file nào trước?**

---

## 🚀 QUICK START (Chọn theo mục đích)

### 1️⃣ Tôi Muốn Deploy App Ngay (15 phút)

```
👉 Đọc: QUICKSTART_STREAMLIT.md
   ↓
   Làm theo 4 bước:
   1. Push code lên GitHub
   2. Sign up Streamlit Cloud
   3. Deploy app
   4. Nhận URL → Share với đồng nghiệp
   
   ✅ DONE! App live sau 15 phút
```

### 2️⃣ Tôi Muốn Hiểu Tổng Quan Dự Án

```
👉 Đọc: README_STREAMLIT.md (10 phút)
   
   Hiểu được:
   - Clinical Assistant làm gì?
   - Tại sao chọn Streamlit?
   - Có những tính năng gì?
   - Roadmap phát triển
```

### 3️⃣ Tôi Muốn Code Calculator Mới

```
👉 Đọc theo thứ tự:
   1. README_STREAMLIT.md - Hiểu cấu trúc (10 min)
   2. Xem file: pages/01_📊_Scores.py - Ví dụ qSOFA (15 min)
   3. Copy template → Modify → Test (30 min)
   
   ✅ Calculator đầu tiên sau 1 giờ
```

### 4️⃣ Tôi Là Bác Sĩ, Muốn Kiểm Tra Nội Dung Lâm Sàng

```
👉 Xem file:
   - data-csv/Scores.csv - Data thang điểm
   - data-csv/Antibiotics.csv - Data kháng sinh
   - RESOURCES.md - Tất cả guidelines references
   
   Verify công thức, citations → Feedback qua GitHub Issues
```

### 5️⃣ Tôi Muốn Chạy Local Để Test

```bash
# 3 lệnh:
pip install -r requirements.txt
streamlit run app.py
# → Mở http://localhost:8501
```

---

## 📂 CẤU TRÚC FILES (Đọc cái nào?)

### 🌟 FILES QUAN TRỌNG (Đọc trước)

| File | Dành cho | Thời gian | Nội dung |
|------|----------|-----------|----------|
| **QUICKSTART_STREAMLIT.md** | Everyone | 5 min | Deploy trong 15 phút |
| **README_STREAMLIT.md** | Everyone | 10 min | Tổng quan dự án |
| **app.py** | Developers | 10 min | Code chính, hiểu flow |
| **pages/01_📊_Scores.py** | Developers | 15 min | Ví dụ calculator hoàn chỉnh |

### 📄 FILES HỖ TRỢ (Đọc khi cần)

| File | Khi nào đọc? |
|------|--------------|
| **requirements.txt** | Khi add thư viện mới |
| **.streamlit/config.toml** | Khi đổi theme/màu sắc |
| **data-csv/*.csv** | Khi cập nhật dữ liệu lâm sàng |
| **RESOURCES.md** | Khi cần citation/guideline |
| **SIMILAR_APPS.md** | Khi nghiên cứu competitors |

### 🗂️ FILES LEGACY (Google Apps Script - Tham khảo)

| File | Note |
|------|------|
| **server/*.gs** | Apps Script code (legacy) |
| **web/*.html** | Apps Script HTML (legacy) |
| **QUICKSTART.md** | Apps Script deployment (outdated) |

**⚠️ Chú ý:** Dự án đã chuyển sang **Streamlit**, các files Apps Script chỉ để tham khảo.

---

## 🎯 ROADMAP HỌC TẬP

### Path 1: User (Bác sĩ sử dụng)

```
Day 1: README_STREAMLIT.md (10 min)
       → Hiểu app làm gì
       
Day 1: Truy cập live URL (hoặc local)
       → Test thử calculators
       
Week 1: Feedback clinical content
        → Report issues nếu thấy sai
        
Week 2: Request new calculators
        → Suggest features
```

### Path 2: Developer (Lập trình viên)

```
Hour 1: README_STREAMLIT.md
        → Hiểu kiến trúc Streamlit
        
Hour 2: QUICKSTART_STREAMLIT.md
        → Deploy local, test
        
Hour 3: Read app.py + pages/01_📊_Scores.py
        → Hiểu code pattern
        
Hour 4-8: Code calculator đầu tiên
          → Copy template → Modify → Test
          
Day 2+: Add more calculators
        → Follow roadmap in README
```

### Path 3: DevOps/Admin

```
Hour 1: QUICKSTART_STREAMLIT.md
        → Deploy to Streamlit Cloud
        
Hour 2: Setup monitoring
        → Check Streamlit dashboard
        
Week 1: Setup GitHub Actions (optional)
        → Auto-testing
        
Week 2: Custom domain (optional)
        → clinical-assistant.hospital.com
```

---

## 🧩 CÁC MODULE HIỆN CÓ

### ✅ Hoàn Thành (Có thể dùng ngay)

1. **qSOFA Calculator** - `pages/01_📊_Scores.py`
   - Input: RR, SBP, GCS
   - Output: qSOFA score + interpretation
   - Reference: Sepsis-3

2. **CrCl Calculator** - `pages/02_💊_Antibiotics.py`
   - Input: Age, Weight, SCr, Sex
   - Output: CrCl + CKD staging
   - Reference: Cockcroft-Gault

3. **ARDSNet Ventilator** - `pages/03_🫁_Ventilator.py`
   - Input: Height, Sex, FiO₂
   - Output: Vt, PEEP, settings
   - Reference: ARDSNet 2000

4. **COPD Exacerbation Protocol** - `pages/04_📋_Protocols.py`
   - Step-by-step bundle
   - Reference: GOLD 2025

5. **Sepsis Bundle** - `pages/04_📋_Protocols.py`
   - 1-hour bundle checklist
   - Reference: Surviving Sepsis 2021

### 🚧 Đang Phát Triển (Week 2-4)

- SOFA score
- CHA₂DS₂-VASc
- Vancomycin dosing
- DKA protocol
- UGIB protocol

---

## ❓ FAQ

### Q: Tôi không biết Python, có code được không?

**A:** Streamlit rất dễ! Ví dụ tạo input:

```python
age = st.number_input("Age", min_value=0, max_value=120, value=65)
```

Xem `pages/01_📊_Scores.py` để học pattern.

### Q: Deploy có mất phí không?

**A:** **MIỄN PHÍ** với Streamlit Community Cloud!
- Unlimited public apps
- Auto-deploy từ GitHub
- 1GB RAM, đủ cho app này

### Q: Làm sao update clinical data?

**A:** 
1. Edit file CSV trong `data-csv/`
2. `git commit` → `git push`
3. Streamlit tự động reload data

### Q: Tôi muốn thêm calculator mới, bắt đầu từ đâu?

**A:**
1. Copy `pages/01_📊_Scores.py`
2. Rename → `pages/05_YourModule.py`
3. Sửa code bên trong
4. Test local: `streamlit run app.py`
5. Push → Auto-deploy!

### Q: App có lưu thông tin bệnh nhân không?

**A:** **KHÔNG!** App này:
- ❌ Không có database
- ❌ Không lưu inputs
- ❌ Không track users
- ✅ Chỉ tính toán realtime

### Q: Tôi muốn chạy offline (nội mạng bệnh viện)?

**A:** Xem phần "Offline Mode" trong `QUICKSTART_STREAMLIT.md`

---

## 🎬 VIDEO TUTORIAL (Coming Soon)

- [ ] Video 1: Deploy trong 5 phút
- [ ] Video 2: Tạo calculator đầu tiên
- [ ] Video 3: Update clinical data
- [ ] Video 4: Customize theme

---

## 🚦 STATUS DỰ ÁN

**Version:** 1.0.0 (Streamlit)  
**Last Updated:** 2025-10-29  
**Status:** 🟢 Active Development

**Current Focus:**
- ✅ Core infrastructure complete
- 🚧 Adding more calculators (Week 2-4)
- 📋 Planning AI integration (Month 2-3)

---

## 📞 CẦN GIÚP ĐỠ?

### Technical Issues:
- 💬 GitHub Issues: [Report here](https://github.com/YOUR_REPO/issues)
- 📧 Email: clinical-it@hospital.com

### Clinical Content:
- 📧 Email: clinical-informatics@hospital.com

### Streamlit Help:
- 📚 Docs: https://docs.streamlit.io/
- 💬 Forum: https://discuss.streamlit.io/
- 🎥 Tutorials: https://streamlit.io/gallery

---

## ✅ CHECKLIST BẮT ĐẦU

### Ngày 1:
- [ ] Đọc README_STREAMLIT.md
- [ ] Clone repo
- [ ] Chạy local: `streamlit run app.py`
- [ ] Test các calculators

### Ngày 2:
- [ ] Đọc QUICKSTART_STREAMLIT.md
- [ ] Deploy lên Streamlit Cloud
- [ ] Share URL với 2-3 đồng nghiệp

### Tuần 1:
- [ ] Học code từ `pages/01_📊_Scores.py`
- [ ] Thử modify một calculator
- [ ] Test và deploy

### Tuần 2:
- [ ] Code calculator mới
- [ ] Add clinical data
- [ ] Contribute back (Pull Request)

---

## 🎉 BẮT ĐẦU NGAY!

**3 bước đơn giản:**

```bash
# 1. Clone
git clone https://github.com/YOUR_USERNAME/clinical-assistant.git

# 2. Install
pip install -r requirements.txt

# 3. Run
streamlit run app.py
```

**→ Mở http://localhost:8501**

**🎊 Chúc bạn thành công!**

---

<p align="center">
  <strong>Clinical Assistant - Streamlit Version</strong>
  <br>
  <sub>Nếu còn thắc mắc, hãy mở GitHub Issue!</sub>
</p>

