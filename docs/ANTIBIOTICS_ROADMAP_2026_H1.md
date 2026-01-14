# Roadmap Trang Kháng Sinh 2026 - H1 (3-6 Tháng)

**Ngày tạo:** 2026-01-XX  
**Phiên bản hiện tại:** 2.0  
**Mục tiêu:** Cải thiện trang Kháng sinh dựa trên phân tích so sánh và gap analysis

---

## Mục Lục

1. [Tổng Quan Roadmap](#tổng-quan-roadmap)
2. [Phương Pháp Ưu Tiên Hóa](#phương-pháp-ưu-tiên-hóa)
3. [Roadmap Chi Tiết](#roadmap-chi-tiết)
4. [KPI & Metrics](#kpi--metrics)
5. [Rủi Ro & Giảm Thiểu](#rủi-ro--giảm-thiểu)
6. [Timeline & Milestones](#timeline--milestones)

---

## Tổng Quan Roadmap

### Mục Tiêu Tổng Thể

Nâng cao trang Kháng sinh từ **64% hoàn thiện** lên **80%+ hoàn thiện** trong 6 tháng, tập trung vào:

1. **Mở rộng coverage** - Tăng database và tính năng
2. **Cải thiện data quality** - Antibiogram, updates, versioning
3. **Nâng cao UX** - Personalization, drug images, wizard
4. **Tăng adoption** - Analytics, notifications, onboarding

### Phạm Vi

- **Thời gian:** 3-6 tháng (H1 2026)
- **Ngân sách:** Nội bộ (không có ngân sách riêng)
- **Team:** 1-2 developers + clinical advisors
- **Users:** Bác sĩ Nội/ICU, Dược sĩ lâm sàng, Điều dưỡng

---

## Phương Pháp Ưu Tiên Hóa

### Impact/Effort/Risk Matrix

Mỗi feature được đánh giá theo:
- **Impact:** 1-5 (1=thấp, 5=cao)
- **Effort:** 1-5 (1=ít, 5=nhiều)
- **Risk:** 1-5 (1=thấp, 5=cao)
- **Fit VN:** 1-5 (1=không phù hợp, 5=rất phù hợp)

**Priority Score = (Impact × Fit VN) / (Effort × Risk)**

### Tiêu Chí "Fit Bệnh Viện Việt Nam"

1. **Offline/D mobile** - Có thể dùng offline, không phụ thuộc subscription
2. **Print/Export** - Dễ in/đính kèm hồ sơ, copy nội dung
3. **Formulary theo BV** - Thuốc hạn chế, chi phí VNĐ
4. **Local resistance** - Dữ liệu kháng thuốc nội viện/khu vực
5. **Vietnamese UI** - Giao diện tiếng Việt hoàn toàn

---

## Roadmap Chi Tiết

### Phase 1: Mở Rộng Coverage (Tháng 1-2)

#### 1.1 Mở Rộng Database Kháng Sinh

**Mục tiêu lâm sàng:**
- Tăng coverage từ 100+ lên 200+ kháng sinh
- Bao phủ các kháng sinh ít dùng nhưng quan trọng
- Thêm các kháng sinh mới được phê duyệt tại VN

**User Story:**
> Là bác sĩ ICU, tôi muốn tra cứu các kháng sinh ít dùng như Colistin, Tigecycline để có đầy đủ thông tin khi cần.

**Phạm vi dữ liệu:**
- Thêm 100+ kháng sinh:
  - Các carbapenem: Imipenem, Meropenem, Ertapenem, Doripenem
  - Các cephalosporin thế hệ 4-5: Cefepime, Ceftaroline, Ceftolozane-Tazobactam
  - Các kháng sinh mới: Ceftazidime-Avibactam, Meropenem-Vaborbactam
  - Các kháng sinh ít dùng: Daptomycin, Linezolid, Tedizolid, Quinupristin-Dalfopristin
  - Các kháng sinh VN: Thuốc nội địa, generic brands

**KPI:**
- Số lượng kháng sinh: 100+ → 200+
- Coverage rate: 60% → 85%
- User satisfaction: >4.5/5

**Rủi ro & giảm thiểu:**
- **Rủi ro:** Dữ liệu không đầy đủ cho một số kháng sinh ít dùng
- **Giảm thiểu:** Ưu tiên kháng sinh có guideline rõ ràng, ghi rõ "Limited data"

**Effort:** 3/5  
**Impact:** 5/5  
**Risk:** 2/5  
**Fit VN:** 5/5  
**Priority Score:** 4.17

---

#### 1.2 Tích Hợp Antibiogram Nội Viện

**Mục tiêu lâm sàng:**
- Hiển thị resistance patterns thực tế từ các bệnh viện VN
- Hỗ trợ quyết định empiric therapy dựa trên local data
- Tích hợp với treatment protocols

**User Story:**
> Là bác sĩ Nội, tôi muốn biết tỷ lệ kháng của E. coli với Ceftriaxone tại BV của tôi để chọn kháng sinh phù hợp.

**Phạm vi dữ liệu:**
- Antibiogram từ 6 bệnh viện lớn:
  - Bạch Mai, Chợ Rẫy, 108, Nhi Đồng, Y Dược HCM, General
- Dữ liệu theo năm (2023, 2024, 2025)
- Organisms: E. coli, K. pneumoniae, P. aeruginosa, S. aureus, MRSA, Enterococcus
- Antibiotics: Các kháng sinh phổ biến

**KPI:**
- Số bệnh viện tích hợp: 0 → 6
- Số organisms: 0 → 10+
- User adoption rate: >60% cho empiric therapy selection

**Rủi ro & giảm thiểu:**
- **Rủi ro:** Dữ liệu không cập nhật, không có sẵn từ các BV
- **Giảm thiểu:** 
  - Bắt đầu với dữ liệu công khai từ các nghiên cứu VN
  - Liên hệ với các BV để hợp tác
  - Ghi rõ "Data source" và "Last updated"

**Effort:** 4/5  
**Impact:** 5/5  
**Risk:** 3/5  
**Fit VN:** 5/5  
**Priority Score:** 3.33

---

#### 1.3 Cải Thiện PK/PD Calculators (CRRT/ECMO)

**Mục tiêu lâm sàng:**
- Tính toán liều cho bệnh nhân CRRT/ECMO
- Tối ưu điều trị cho ICU patients
- Giảm nguy cơ under/over-dosing

**User Story:**
> Là bác sĩ ICU, tôi muốn tính liều Vancomycin cho bệnh nhân CRRT để đảm bảo nồng độ đủ.

**Phạm vi dữ liệu:**
- CRRT dosing cho:
  - Vancomycin, Piperacillin-Tazobactam, Meropenem, Ceftazidime
  - Aminoglycosides, Fluconazole, Voriconazole
- ECMO dosing adjustments
- PK/PD parameters cho CRRT/ECMO

**KPI:**
- Số kháng sinh hỗ trợ CRRT: 0 → 10+
- User adoption rate: >40% cho ICU users
- Accuracy: >95% so với manual calculation

**Rủi ro & giảm thiểu:**
- **Rủi ro:** PK/PD data cho CRRT/ECMO phức tạp, có thể không chính xác
- **Giảm thiểu:**
  - Dựa trên guidelines và literature
  - Ghi rõ assumptions và limitations
  - Cần clinical validation

**Effort:** 4/5  
**Impact:** 4/5  
**Risk:** 3/5  
**Fit VN:** 4/5  
**Priority Score:** 2.67

---

### Phase 2: Cải Thiện Data Quality (Tháng 3-4)

#### 2.1 Update Notification System

**Mục tiêu lâm sàng:**
- Thông báo khi có guideline updates
- Theo dõi version changes
- Đảm bảo users luôn có thông tin mới nhất

**User Story:**
> Là bác sĩ, tôi muốn được thông báo khi có guideline mới về CAP để cập nhật kiến thức.

**Phạm vi dữ liệu:**
- Version tracking cho mỗi protocol
- Changelog với mô tả thay đổi
- Notification preferences (email, in-app)

**KPI:**
- Update notification rate: 0% → 80%
- User engagement với notifications: >50%
- Time to update: <7 days sau khi guideline mới ra

**Rủi ro & giảm thiểu:**
- **Rủi ro:** Spam notifications, users tắt notifications
- **Giảm thiểu:**
  - Cho phép users customize preferences
  - Chỉ notify về major updates
  - Group notifications theo ngày/tuần

**Effort:** 3/5  
**Impact:** 3/5  
**Risk:** 2/5  
**Fit VN:** 3/5  
**Priority Score:** 2.25

---

#### 2.2 Version Tracking & Audit Trail

**Mục tiêu lâm sàng:**
- Theo dõi thay đổi trong protocols
- Đảm bảo traceability
- Hỗ trợ quality assurance

**User Story:**
> Là dược sĩ lâm sàng, tôi muốn biết khi nào protocol được cập nhật và ai đã thay đổi để audit.

**Phạm vi dữ liệu:**
- Version history cho mỗi protocol
- Changelog với author, date, reason
- Diff view để so sánh versions

**KPI:**
- Version tracking coverage: 0% → 100%
- Audit trail completeness: >95%
- User access to history: >30%

**Rủi ro & giảm thiểu:**
- **Rủi ro:** Phức tạp implementation, performance impact
- **Giảm thiểu:**
  - Sử dụng lightweight versioning
  - Chỉ track major changes
  - Optimize database queries

**Effort:** 3/5  
**Impact:** 2/5  
**Risk:** 2/5  
**Fit VN:** 2/5  
**Priority Score:** 1.50

---

### Phase 3: Nâng Cao UX (Tháng 5-6)

#### 3.1 Drug Images & Pill Identifier

**Mục tiêu lâm sàng:**
- Nhận diện thuốc qua hình ảnh
- Hỗ trợ điều dưỡng và bác sĩ
- Giảm lỗi medication

**User Story:**
> Là điều dưỡng, tôi muốn xem hình ảnh thuốc để đảm bảo đúng thuốc khi chuẩn bị.

**Phạm vi dữ liệu:**
- Hình ảnh cho 100+ kháng sinh phổ biến:
  - Viên nén, viên nang
  - Lọ tiêm, ống tiêm
  - Dung dịch truyền
- Pill identifier:
  - Màu sắc, hình dạng, ký hiệu
  - Brand name lookup

**KPI:**
- Số kháng sinh có hình ảnh: 0 → 100+
- Pill identifier accuracy: >90%
- User adoption rate: >50% cho điều dưỡng

**Rủi ro & giảm thiểu:**
- **Rủi ro:** Bản quyền hình ảnh, chi phí thu thập hình ảnh
- **Giảm thiểu:**
  - Sử dụng hình ảnh công khai hoặc tự chụp
  - Bắt đầu với kháng sinh phổ biến nhất
  - User-generated content (future)

**Effort:** 4/5  
**Impact:** 3/5  
**Risk:** 2/5  
**Fit VN:** 3/5  
**Priority Score:** 2.25

---

#### 3.2 Personalization Features

**Mục tiêu lâm sàng:**
- Favorites và recent drugs
- User preferences
- Customizable dashboard
- Tăng tốc độ truy cập

**User Story:**
> Là bác sĩ ICU, tôi muốn lưu các kháng sinh thường dùng để truy cập nhanh.

**Phạm vi dữ liệu:**
- Favorites list (per user)
- Recent drugs (last 10)
- User preferences:
  - Default hospital
  - Default units (mg vs g)
  - Theme (light/dark)
- Customizable dashboard layout

**KPI:**
- User adoption rate: >60%
- Average favorites per user: >5
- Time saved per search: >30%

**Rủi ro & giảm thiểu:**
- **Rủi ro:** Privacy concerns, storage costs
- **Giảm thiểu:**
  - Local storage (browser)
  - Optional account creation
  - Clear privacy policy

**Effort:** 2/5  
**Impact:** 3/5  
**Risk:** 1/5  
**Fit VN:** 4/5  
**Priority Score:** 6.00

---

#### 3.3 Interactive Treatment Wizard

**Mục tiêu lâm sàng:**
- Hướng dẫn step-by-step chọn kháng sinh
- Phù hợp cho người mới
- Giảm lỗi chọn sai protocol

**User Story:**
> Là bác sĩ mới, tôi muốn có wizard hướng dẫn tôi chọn protocol phù hợp cho bệnh nhân CAP.

**Phạm vi dữ liệu:**
- Wizard flow cho các infection sites:
  - CAP, HAP, UTI, SSTI, Sepsis
- Questions:
  - Infection site
  - Severity
  - Setting (OPD/Ward/ICU)
  - Risk factors (MRSA, Pseudomonas)
  - Allergies
- Recommendations với rationale

**KPI:**
- Wizard completion rate: >70%
- Accuracy: >90% match với manual selection
- User satisfaction: >4.5/5

**Rủi ro & giảm thiểu:**
- **Rủi ro:** Phức tạp implementation, có thể không cover hết cases
- **Giảm thiểu:**
  - Bắt đầu với CAP và UTI (đơn giản nhất)
  - Có "Skip wizard" option
  - User feedback để cải thiện

**Effort:** 4/5  
**Impact:** 4/5  
**Risk:** 3/5  
**Fit VN:** 4/5  
**Priority Score:** 2.67

---

### Phase 4: Tăng Adoption (Tháng 6)

#### 4.1 Analytics Dashboard

**Mục tiêu lâm sàng:**
- Theo dõi usage patterns
- Đánh giá hiệu quả
- Identify popular features
- Data-driven improvements

**User Story:**
> Là admin, tôi muốn biết tính năng nào được dùng nhiều nhất để ưu tiên cải thiện.

**Phạm vi dữ liệu:**
- Usage statistics:
  - Số users, sessions, page views
  - Popular drugs, protocols, calculators
  - Search patterns
  - Feature usage
- User feedback:
  - Ratings, comments
  - Feature requests

**KPI:**
- Dashboard coverage: 0% → 100%
- Data accuracy: >95%
- Actionable insights: >5 per month

**Rủi ro & giảm thiểu:**
- **Rủi ro:** Privacy concerns, data storage costs
- **Giảm thiểu:**
  - Anonymize data
  - Aggregate data only
  - Clear privacy policy
  - Opt-out option

**Effort:** 3/5  
**Impact:** 2/5  
**Risk:** 2/5  
**Fit VN:** 2/5  
**Priority Score:** 1.33

---

#### 4.2 Onboarding & Tutorial

**Mục tiêu lâm sàng:**
- Hướng dẫn người dùng mới
- Tăng adoption rate
- Giảm learning curve

**User Story:**
> Là bác sĩ mới, tôi muốn có tutorial hướng dẫn cách sử dụng trang để nhanh chóng làm quen.

**Phạm vi dữ liệu:**
- Interactive tutorial:
  - Overview của trang
  - Các tính năng chính
  - Tips & tricks
- Video tutorials (optional)
- FAQ section

**KPI:**
- Tutorial completion rate: >60%
- Time to proficiency: <15 minutes
- User satisfaction: >4.5/5

**Rủi ro & giảm thiểu:**
- **Rủi ro:** Users skip tutorial, outdated content
- **Giảm thiểu:**
  - Optional but recommended
  - Short and engaging
  - Regular updates

**Effort:** 2/5  
**Impact:** 3/5  
**Risk:** 1/5  
**Fit VN:** 4/5  
**Priority Score:** 6.00

---

## KPI & Metrics

### Overall KPIs

| Metric | Baseline | Target (6 tháng) |
|--------|----------|------------------|
| **Feature Completeness** | 64% | 80%+ |
| **Database Size** | 100+ | 200+ |
| **User Satisfaction** | 4.2/5 | 4.5/5 |
| **Daily Active Users** | 500 | 1000+ |
| **Feature Adoption Rate** | 40% | 60%+ |
| **Update Frequency** | Manual | Weekly |

### Phase-Specific KPIs

**Phase 1 (Tháng 1-2):**
- Database expansion: 100+ → 200+ kháng sinh
- Antibiogram integration: 0 → 6 bệnh viện
- CRRT/ECMO calculators: 0 → 10+ kháng sinh

**Phase 2 (Tháng 3-4):**
- Update notifications: 0% → 80% coverage
- Version tracking: 0% → 100% coverage
- Data quality score: 70% → 85%

**Phase 3 (Tháng 5-6):**
- Drug images: 0 → 100+ kháng sinh
- Personalization adoption: 0% → 60%
- Wizard completion: 0% → 70%

**Phase 4 (Tháng 6):**
- Analytics dashboard: 0% → 100% coverage
- Tutorial completion: 0% → 60%
- User onboarding time: >30 min → <15 min

---

## Rủi Ro & Giảm Thiểu

### Rủi Ro Tổng Thể

1. **Resource Constraints**
   - **Rủi ro:** Thiếu developers, time constraints
   - **Giảm thiểu:** Ưu tiên features có impact cao, phân chia work

2. **Data Quality**
   - **Rủi ro:** Dữ liệu không chính xác, lỗi thời
   - **Giảm thiểu:** Validation process, regular reviews, clinical advisors

3. **User Adoption**
   - **Rủi ro:** Users không sử dụng features mới
   - **Giảm thiểu:** User testing, feedback, marketing, tutorials

4. **Technical Debt**
   - **Rủi ro:** Code quality giảm khi rush features
   - **Giảm thiểu:** Code reviews, testing, refactoring time

5. **Legal/Compliance**
   - **Rủi ro:** Bản quyền dữ liệu, medical liability
   - **Giảm thiểu:** Legal review, disclaimers, source attribution

---

## Timeline & Milestones

### Tháng 1-2: Mở Rộng Coverage

**Milestones:**
- ✅ Week 1-2: Database expansion planning & data collection
- ✅ Week 3-4: Implement 50+ new antibiotics
- ✅ Week 5-6: Antibiogram integration (3 bệnh viện)
- ✅ Week 7-8: CRRT/ECMO calculators (5 kháng sinh)

**Deliverables:**
- Database với 150+ kháng sinh
- Antibiogram cho 3 bệnh viện
- CRRT calculators cho 5 kháng sinh

---

### Tháng 3-4: Cải Thiện Data Quality

**Milestones:**
- ✅ Week 9-10: Update notification system
- ✅ Week 11-12: Version tracking implementation
- ✅ Week 13-14: Testing & validation
- ✅ Week 15-16: Rollout & monitoring

**Deliverables:**
- Update notification system
- Version tracking cho tất cả protocols
- Changelog và audit trail

---

### Tháng 5-6: Nâng Cao UX

**Milestones:**
- ✅ Week 17-18: Drug images collection & upload
- ✅ Week 19-20: Personalization features
- ✅ Week 21-22: Treatment wizard (CAP, UTI)
- ✅ Week 23-24: Analytics dashboard & onboarding

**Deliverables:**
- Drug images cho 100+ kháng sinh
- Personalization features (favorites, recent)
- Treatment wizard cho CAP và UTI
- Analytics dashboard và tutorial

---

## Kết Luận

Roadmap này tập trung vào **4 phases chính** trong 6 tháng:

1. **Mở rộng coverage** - Database, antibiogram, CRRT/ECMO
2. **Cải thiện data quality** - Updates, versioning, tracking
3. **Nâng cao UX** - Images, personalization, wizard
4. **Tăng adoption** - Analytics, onboarding, tutorials

**Mục tiêu:** Nâng cao từ **64% → 80%+ hoàn thiện**, tập trung vào tính phù hợp với bệnh viện Việt Nam.

**Success Criteria:**
- ✅ 200+ kháng sinh trong database
- ✅ Antibiogram từ 6 bệnh viện
- ✅ User satisfaction >4.5/5
- ✅ Daily active users >1000
- ✅ Feature adoption rate >60%

---

**Tác giả:** AI Assistant  
**Ngày:** 2026-01-XX  
**Version:** 1.0
