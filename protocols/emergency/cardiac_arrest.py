"""
Cardiac Arrest / ACLS Protocol
AHA 2020, ERC 2021
Advanced Cardiac Life Support for cardiac arrest management
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Cardiac Arrest / ACLS Protocol"""
    st.subheader("💔 Cardiac Arrest / ACLS Protocol")
    st.caption("AHA 2020, ERC 2021 - Advanced Cardiac Life Support")
    
    st.error("""
    **🚨 CARDIAC ARREST = IMMEDIATE LIFE-THREATENING EMERGENCY**
    
    **Triệu chứng:**
    - Mất ý thức
    - Không có mạch
    - Ngừng thở hoặc thở ngáp cá
    - Không phản ứng với kích thích
    
    **Bắt đầu CPR ngay lập tức - Mỗi giây đều quý giá!**
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: BLS ==========
    st.markdown("### ⚡ BLS (Basic Life Support)")
    
    with st.expander("🔄 Xem quy trình BLS", expanded=True):
        # Dùng HTML với font chuẩn để tránh lỗi hiển thị dấu tiếng Việt
        st.markdown(
            """
            <div style="font-family: 'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif; font-size: 0.95rem; line-height: 1.6;">
              <ol style="margin: 0; padding-left: 20px;">
                <li><strong>Kiểm tra an toàn:</strong>
                  <ul style="margin-top: 4px;">
                    <li>Đảm bảo môi trường an toàn cho người cứu hộ và bệnh nhân</li>
                  </ul>
                </li>
                <li><strong>Kiểm tra phản ứng:</strong>
                  <ul style="margin-top: 4px;">
                    <li>Lay người, gọi to: "Bạn có ổn không?"</li>
                    <li>Nếu không phản ứng → Gọi cấp cứu (115) và lấy AED</li>
                  </ul>
                </li>
                <li><strong>Kiểm tra thở:</strong>
                  <ul style="margin-top: 4px;">
                    <li>Mở đường thở (head-tilt chin-lift hoặc jaw-thrust nếu chấn thương)</li>
                    <li>Nhìn, nghe, cảm nhận thở (5-10 giây)</li>
                    <li>Nếu không thở bình thường → Bắt đầu CPR</li>
                  </ul>
                </li>
                <li><strong>CPR (Cardiopulmonary Resuscitation):</strong>
                  <ul style="margin-top: 4px;">
                    <li><strong>Tần số:</strong> 100-120 lần/phút</li>
                    <li><strong>Độ sâu:</strong> 5-6 cm (Người lớn), 1/3 chiều sâu ngực (Trẻ em)</li>
                    <li><strong>Tỷ lệ:</strong> 30 ép : 2 thổi (1 người), 15 ép : 2 thổi (2 người)</li>
                    <li><strong>Vị trí:</strong> Giữa ngực, trên xương ức</li>
                    <li><strong>Cho phép nở ngực hoàn toàn</strong> giữa các lần ép</li>
                  </ul>
                </li>
                <li><strong>AED (Automated External Defibrillator):</strong>
                  <ul style="margin-top: 4px;">
                    <li>Bật AED ngay khi có</li>
                    <li>Dán pad theo hướng dẫn</li>
                    <li>Để AED phân tích nhịp</li>
                    <li>Sốc nếu được khuyến nghị</li>
                    <li>Tiếp tục CPR sau sốc</li>
                  </ul>
                </li>
              </ol>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    st.markdown("---")
    
    # ========== SECTION 2: ACLS ALGORITHM ==========
    st.markdown("### 🔌 ACLS Algorithm")
    
    rhythm_type = st.radio(
        "**Loại nhịp tim:**",
        ["VF/VT (Shockable)", "PEA/Asystole (Non-shockable)", "Post-ROSC Care"],
        key="acls_rhythm"
    )
    
    st.markdown("---")
    
    if rhythm_type == "VF/VT (Shockable)":
        render_shockable_protocol()
    elif rhythm_type == "PEA/Asystole (Non-shockable)":
        render_nonshockable_protocol()
    else:
        render_post_rosc_care()
    
    st.markdown("---")
    
    # ========== SECTION 3: ACLS DRUGS ==========
    st.markdown("### 💉 ACLS Medications")
    
    with st.expander("📋 Xem liều thuốc ACLS", expanded=False):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **Epinephrine:**
            - **Liều:** 1 mg IV/IO
            - **Lặp lại:** q3-5 phút
            - **Đường dùng:** IV, IO, ET (2-2.5 mg)
            - **Ghi chú:** Thuốc đầu tay cho tất cả loại nhịp
            
            **Amiodarone:**
            - **Liều đầu:** 300 mg IV/IO bolus
            - **Liều thứ 2:** 150 mg IV/IO (nếu VF/VT tái phát)
            - **Truyền tĩnh mạch:** 1 mg/min x 6h, sau đó 0.5 mg/min
            - **Ghi chú:** Cho VF/VT kháng sốc
            
            **Lidocaine:**
            - **Liều đầu:** 1-1.5 mg/kg IV/IO
            - **Liều lặp:** 0.5-0.75 mg/kg q5-10 phút (max 3 mg/kg)
            - **Truyền tĩnh mạch:** 1-4 mg/min
            - **Ghi chú:** Thay thế Amiodarone nếu không có
            """)
        
        with col2:
            st.markdown("""
            **Atropine:**
            - **Liều:** 1 mg IV/IO
            - **Lặp lại:** q3-5 phút (max 3 mg)
            - **Ghi chú:** Chỉ cho bradycardia, không dùng cho PEA/Asystole
            
            **Vasopressin:**
            - **Liều:** 40 units IV/IO
            - **Lặp lại:** 1 lần (thay thế liều Epinephrine đầu tiên hoặc thứ hai)
            - **Ghi chú:** Không còn khuyến nghị trong AHA 2020
            
            **Magnesium:**
            - **Liều:** 1-2 g IV/IO (nếu hypomagnesemia hoặc torsades)
            - **Ghi chú:** Chỉ cho torsades de pointes hoặc hypomagnesemia
            """)
    
    st.markdown("---")
    
    # ========== SECTION 4: SPECIAL CIRCUMSTANCES ==========
    st.markdown("### 🎯 Special Circumstances")
    
    special_circumstance = st.selectbox(
        "**Tình huống đặc biệt:**",
        [
            "Chọn tình huống...",
            "Hypothermia",
            "Drowning",
            "Anaphylaxis",
            "Opioid Overdose",
            "Pregnancy",
            "Trauma",
            "Electrocution"
        ],
        key="special_circumstance"
    )
    
    if special_circumstance != "Chọn tình huống...":
        render_special_circumstance(special_circumstance)
    
    st.markdown("---")
    
    # ========== SECTION 5: TARGETED TEMPERATURE MANAGEMENT ==========
    st.markdown("### 🌡️ Targeted Temperature Management (TTM)")
    
    with st.expander("❄️ Xem quy trình TTM", expanded=False):
        st.markdown("""
        **Chỉ định:**
        - Bệnh nhân sau ROSC, vẫn hôn mê
        - Nhịp ban đầu: VF/VT hoặc shockable rhythm
        
        **Quy trình:**
        1. **Làm mát sớm:** Bắt đầu trong vòng 2-6 giờ sau ROSC
        2. **Nhiệt độ mục tiêu:** 32-36°C (thường 33-34°C)
        3. **Thời gian:** 24 giờ
        4. **Làm ấm lại:** 0.25-0.5°C/giờ (từ từ)
        5. **Theo dõi:** Nhiệt độ liên tục, shivering, điện giải
        
        **Phương pháp:**
        - Surface cooling (ice packs, cooling blankets)
        - Intravascular cooling
        - IV cold saline
        
        **Chống chỉ định:**
        - Chảy máu nặng
        - Shock nặng
        - Nhiễm trùng nặng
        - Phụ nữ có thai
        """)
    
    st.markdown("---")
    
    # ========== SECTION 6: POST-ROSC MONITORING ==========
    st.markdown("### 📈 Post-ROSC Monitoring")
    
    st.markdown("""
    **Theo dõi sát:**
    - **Huyết động:** BP, HR, CVP, ScvO2
    - **Hô hấp:** SpO2, ABG, X-ray ngực
    - **Thần kinh:** GCS, pupil, EEG (nếu có)
    - **Chuyển hóa:** Lactate, glucose, điện giải
    - **Tim mạch:** ECG, troponin, echo
    
    **Mục tiêu:**
    - **MAP:** ≥65 mmHg (hoặc SBP ≥90 mmHg)
    - **SpO2:** 94-98%
    - **Glucose:** 140-180 mg/dL
    - **Nhiệt độ:** Tránh sốt (>37.5°C)
    - **PaCO2:** 35-45 mmHg (normocapnia)
    """)
    
    st.markdown("---")
    
    # ========== SECTION 7: PROGNOSIS ==========
    st.markdown("### 📊 Prognosis & Decision Making")
    
    with st.expander("🔮 Xem tiên lượng", expanded=False):
        st.markdown("""
        **Yếu tố tiên lượng tốt:**
        - ROSC sớm (<20 phút)
        - Nhịp ban đầu: VF/VT
        - Tuổi trẻ
        - Không có bệnh nền nặng
        - Phản ứng thần kinh sớm
        
        **Yếu tố tiên lượng xấu:**
        - Thời gian CPR kéo dài (>30 phút)
        - Nhịp ban đầu: PEA/Asystole
        - Tuổi cao
        - Bệnh nền nặng
        - Không có phản ứng thần kinh sau 72 giờ
        
        **Quyết định ngừng điều trị:**
        - Thảo luận với gia đình
        - Đánh giá thần kinh sau 72 giờ
        - Xem xét các yếu tố tiên lượng
        - Tuân theo guidelines địa phương
        """)
    
    st.markdown("---")
    
    # ========== SECTION 8: SPECIAL POPULATIONS ==========
    st.markdown("### 👥 Special Populations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Trẻ em:**
        - **CPR:** 15 ép : 2 thổi (2 người)
        - **Epinephrine:** 0.01 mg/kg IV/IO (0.1 mg/kg ET)
        - **Amiodarone:** 5 mg/kg IV/IO
        - **Lidocaine:** 1 mg/kg IV/IO
        - **Defibrillation:** 2-4 J/kg
        
        **Phụ nữ có thai:**
        - **CPR:** Đặt nghiêng trái 15-30° (manual left uterine displacement)
        - **Defibrillation:** An toàn, không cần thay đổi liều
        - **ROSC:** Cân nhắc mổ lấy thai nếu >20 tuần và không ROSC sau 4 phút
        """)
    
    with col2:
        st.markdown("""
        **Người cao tuổi:**
        - Tỷ lệ thành công thấp hơn
        - Cần xem xét chất lượng cuộc sống
        - Thảo luận với gia đình về mục tiêu điều trị
        
        **Bệnh nhân có bệnh nền:**
        - Điều chỉnh theo bệnh nền
        - Cân nhắc ngừng điều trị nếu tiên lượng rất xấu
        """)
    
    st.markdown("---")
    
    # ========== SECTION 9: REFERENCES ==========
    render_references_section(get_references("cardiac_arrest"))
    
    st.markdown("---")
    
    # Footer
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Tuân theo guidelines địa phương và điều chỉnh theo tình huống lâm sàng cụ thể.")


def render_shockable_protocol():
    """VF/VT (Shockable) Protocol"""
    st.error("## ⚡ VF/VT (SHOCKABLE) PROTOCOL")
    
    st.markdown("""
    **Quy trình:**
    
    1. **Tiếp tục CPR** trong khi chuẩn bị defibrillator
    
    2. **Defibrillation:**
       - **Liều:** 120-200 J (biphasic) hoặc 360 J (monophasic)
       - **Lặp lại:** Tăng liều nếu cần
       - **Sau sốc:** Tiếp tục CPR ngay, không kiểm tra mạch
    
    3. **Sau 2 phút CPR:**
       - Kiểm tra nhịp
       - Nếu vẫn VF/VT:
         - Sốc lại
         - **Epinephrine:** 1 mg IV/IO
         - Tiếp tục CPR 2 phút
    
    4. **Sau 2 phút CPR tiếp:**
       - Kiểm tra nhịp
       - Nếu vẫn VF/VT:
         - Sốc lại
         - **Amiodarone:** 300 mg IV/IO (hoặc Lidocaine 1-1.5 mg/kg)
         - Tiếp tục CPR 2 phút
    
    5. **Lặp lại chu kỳ:**
       - Sốc → CPR 2 phút → Kiểm tra nhịp
       - **Epinephrine:** q3-5 phút
       - **Amiodarone liều 2:** 150 mg (nếu cần)
    
    **Lưu ý:**
    - Không ngừng CPR để kiểm tra mạch trừ khi có ROSC rõ ràng
    - Tối đa hóa thời gian ép ngực (minimize interruptions)
    - Xoay người ép ngực mỗi 2 phút
    """)
    
    st.info("""
    **💡 Mẹo quan trọng:**
    - Chất lượng CPR quan trọng hơn thuốc
    - Minimize "no-flow time" (thời gian không ép ngực)
    - Đảm bảo đường thở và thông khí tốt
    - Theo dõi ETCO2 (mục tiêu >10 mmHg)
    """)


def render_nonshockable_protocol():
    """PEA/Asystole (Non-shockable) Protocol"""
    st.warning("## ⚠️ PEA/ASYSTOLE (NON-SHOCKABLE) PROTOCOL")
    
    st.markdown("""
    **Quy trình:**
    
    1. **Tiếp tục CPR chất lượng cao**
    
    2. **Epinephrine:** 1 mg IV/IO q3-5 phút
    
    3. **Sau 2 phút CPR:**
       - Kiểm tra nhịp
       - Nếu vẫn PEA/Asystole:
         - Tiếp tục CPR
         - **Epinephrine:** 1 mg IV/IO
         - Tìm và điều trị nguyên nhân (H's và T's)
    
    4. **Điều trị nguyên nhân (H's và T's):**
       - **Hypovolemia:** Truyền dịch
       - **Hypoxia:** Đảm bảo thông khí
       - **Hydrogen ion (acidosis):** Sodium bicarbonate (cân nhắc)
       - **Hypo/Hyperkalemia:** Điều chỉnh K+
       - **Hypothermia:** Làm ấm
       - **Tension pneumothorax:** Giải áp ngay
       - **Tamponade:** Chọc dò màng tim
       - **Toxins:** Antidote nếu có
       - **Thrombosis (PE):** Thrombolytics (cân nhắc)
       - **Thrombosis (ACS):** PCI nếu có
    
    5. **Lặp lại chu kỳ:**
       - CPR 2 phút → Kiểm tra nhịp
       - **Epinephrine:** q3-5 phút
       - Tiếp tục điều trị nguyên nhân
    
    **Lưu ý:**
    - PEA/Asystole có tiên lượng xấu hơn VF/VT
    - Tập trung vào tìm và điều trị nguyên nhân
    - Cân nhắc ngừng điều trị nếu không có tiến triển sau 20-30 phút
    """)
    
    st.info("""
    **💡 Mẹo quan trọng:**
    - Tìm nguyên nhân có thể đảo ngược (H's và T's)
    - PEA có thể có hoạt động điện nhưng không có mạch
    - Asystole có thể là fine VF - cân nhắc sốc thử
    - Theo dõi ETCO2 (nếu tăng có thể là dấu hiệu ROSC)
    """)


def render_post_rosc_care():
    """Post-ROSC Care Protocol"""
    st.success("## ✅ POST-ROSC CARE PROTOCOL")
    
    st.markdown("""
    **1. Đảm bảo ABC:**
       - **Airway:** Đặt nội khí quản nếu cần
       - **Breathing:** Thông khí, SpO2 94-98%
       - **Circulation:** Đảm bảo MAP ≥65 mmHg
    
    2. **Huyết động:**
       - **Mục tiêu MAP:** ≥65 mmHg (hoặc SBP ≥90 mmHg)
       - **Vasopressors:** Norepinephrine (ưu tiên) hoặc Epinephrine
       - **Fluid:** Truyền dịch nếu hypovolemic
       - **Inotropes:** Dobutamine nếu cần
    
    3. **Thông khí:**
       - **SpO2:** 94-98% (tránh hyperoxia)
       - **PaCO2:** 35-45 mmHg (normocapnia)
       - **PEEP:** 5-10 cmH2O
    
    4. **Targeted Temperature Management (TTM):**
       - Làm mát đến 32-36°C (thường 33-34°C)
       - Duy trì 24 giờ
       - Làm ấm lại từ từ (0.25-0.5°C/giờ)
    
    5. **Thần kinh:**
       - Đánh giá GCS
       - Theo dõi pupil
       - Cân nhắc EEG nếu có
    
    6. **Chuyển hóa:**
       - **Glucose:** 140-180 mg/dL
       - **Điện giải:** Bình thường hóa
       - **Lactate:** Theo dõi, mục tiêu giảm
    
    7. **Tim mạch:**
       - **ECG:** 12-lead ngay
       - **Troponin:** Xét nghiệm
       - **Echo:** Đánh giá chức năng tim
       - **PCI:** Cân nhắc nếu STEMI hoặc nghi ngờ ACS
    
    8. **Theo dõi:**
       - ICU monitoring
       - Theo dõi sát các thông số
       - Đánh giá thần kinh định kỳ
    """)
    
    st.info("""
    **💡 Mẹo quan trọng:**
    - ROSC chỉ là bước đầu - cần chăm sóc sau ROSC tốt
    - Tránh hyperoxia và hypercapnia
    - TTM cải thiện kết quả thần kinh
    - Cân nhắc PCI sớm nếu nghi ngờ ACS
    """)


def render_special_circumstance(circumstance: str):
    """Render special circumstance protocol"""
    
    if circumstance == "Hypothermia":
        st.markdown("""
        **Hypothermia Cardiac Arrest:**
        - **CPR:** Tiếp tục cho đến khi làm ấm đến 32-35°C
        - **Defibrillation:** Chỉ sốc khi nhiệt độ >30°C
        - **Thuốc:** Giảm liều hoặc trì hoãn cho đến khi làm ấm
        - **Làm ấm:** Active rewarming (warm IV fluids, warm humidified O2, extracorporeal)
        - **Nguyên tắc:** "Not dead until warm and dead"
        """)
    
    elif circumstance == "Drowning":
        st.markdown("""
        **Drowning Cardiac Arrest:**
        - **CPR:** Bắt đầu ngay, không cố gắng "drain water"
        - **Ventilation:** Quan trọng (thường do hypoxia)
        - **Defibrillation:** Nếu VF/VT
        - **Làm ấm:** Nếu hypothermia
        - **Corticosteroids:** Không khuyến nghị thường quy
        - **Antibiotics:** Chỉ nếu nhiễm trùng rõ ràng
        """)
    
    elif circumstance == "Anaphylaxis":
        st.markdown("""
        **Anaphylaxis Cardiac Arrest:**
        - **Epinephrine:** 1 mg IV/IO (ACLS dose)
        - **CPR:** Tiếp tục
        - **Fluid:** Truyền dịch tích cực (hypovolemia do leaky vessels)
        - **Antihistamines:** Sau ROSC
        - **Corticosteroids:** Sau ROSC
        """)
    
    elif circumstance == "Opioid Overdose":
        st.markdown("""
        **Opioid Overdose Cardiac Arrest:**
        - **Naloxone:** 2 mg IV/IO/IM/IN (có thể lặp lại)
        - **CPR:** Tiếp tục
        - **Ventilation:** Quan trọng (thường do respiratory depression)
        - **Nếu ROSC:** Theo dõi sát (có thể tái ngộ độc)
        """)
    
    elif circumstance == "Pregnancy":
        st.markdown("""
        **Pregnancy Cardiac Arrest:**
        - **CPR:** Đặt nghiêng trái 15-30° (manual left uterine displacement)
        - **Defibrillation:** An toàn, không cần thay đổi liều
        - **Thuốc:** Không cần thay đổi liều
        - **ROSC:** Cân nhắc mổ lấy thai nếu >20 tuần và không ROSC sau 4 phút
        - **Perimortem C-section:** Nếu >20 tuần, không ROSC sau 4 phút CPR
        """)
    
    elif circumstance == "Trauma":
        st.markdown("""
        **Trauma Cardiac Arrest:**
        - **CPR:** Tiếp tục
        - **Tension pneumothorax:** Giải áp ngay (needle decompression)
        - **Tamponade:** Chọc dò màng tim
        - **Hypovolemia:** Truyền dịch, cân nhắc blood products
        - **Surgery:** Cân nhắc thoracotomy nếu nghi ngờ chảy máu trong
        """)
    
    elif circumstance == "Electrocution":
        st.markdown("""
        **Electrocution Cardiac Arrest:**
        - **An toàn:** Đảm bảo nguồn điện đã tắt
        - **CPR:** Bắt đầu ngay
        - **Defibrillation:** Nếu VF/VT
        - **Burns:** Điều trị sau ROSC
        - **Rhabdomyolysis:** Theo dõi CK, myoglobinuria
        """)

