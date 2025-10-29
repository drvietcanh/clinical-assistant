"""
Acute Heart Failure Protocol
Acute Decompensated Heart Failure Management
"""

import streamlit as st


def render():
    """Acute Heart Failure Protocol"""
    st.subheader("💔 Suy Tim Cấp")
    st.caption("Acute Decompensated Heart Failure - ESC/AHA Guidelines")
    
    st.info("""
    **Suy tim cấp** là khởi phát nhanh hoặc xấu đi nhanh của triệu chứng suy tim.
    """)
    
    # Assessment
    st.markdown("### 1️⃣ Đánh Giá Ban Đầu")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("#### Triệu Chứng & Dấu Hiệu")
        
        # Symptoms
        dyspnea = st.checkbox("Khó thở", key="hf_dyspnea")
        orthopnea = st.checkbox("Khó thở khi nằm (Orthopnea)", key="hf_orthopnea")
        pnd = st.checkbox("Khó thở đột ngột ban đêm (PND)", key="hf_pnd")
        fatigue = st.checkbox("Mệt mỏi", key="hf_fatigue")
        
        # Signs
        st.markdown("**Dấu hiệu khám:**")
        rales = st.checkbox("Ran ẩm phổi", key="hf_rales")
        edema = st.checkbox("Phù 2 chân", key="hf_edema")
        jvd = st.checkbox("Tĩnh mạch cổ nổi (JVD)", key="hf_jvd")
        s3_gallop = st.checkbox("S3 gallop", key="hf_s3")
        hepatomegaly = st.checkbox("Gan to", key="hf_hepato")
        
        # Severity markers
        st.markdown("**Dấu hiệu nặng:**")
        hypotension = st.checkbox("Hạ huyết áp (SBP <90 mmHg)", key="hf_hypotension")
        cold_extremities = st.checkbox("Chi lạnh, toát mồ hôi", key="hf_cold")
        altered_mental = st.checkbox("Lú lẫn", key="hf_confusion")
        oliguria = st.checkbox("Tiểu ít (<0.5 mL/kg/h)", key="hf_oliguria")
        
        # Vital signs
        sbp = st.number_input("Huyết áp tâm thu (mmHg)", 50, 250, 120, 5, key="hf_sbp")
        hr = st.number_input("Nhịp tim (/phút)", 30, 200, 80, 5, key="hf_hr")
        rr = st.number_input("Nhịp thở (/phút)", 10, 60, 20, 2, key="hf_rr")
        spo2 = st.number_input("SpO₂ (%)", 70, 100, 95, 1, key="hf_spo2")
    
    with col2:
        st.markdown("### 📊 Phân Loại")
        
        # Calculate severity
        congestion = sum([rales, edema, jvd, orthopnea, pnd])
        perfusion_issues = sum([hypotension, cold_extremities, altered_mental, oliguria])
        
        # Clinical profile (Forrester/Stevenson)
        if congestion >= 2 and perfusion_issues >= 2:
            st.error("## Profile C")
            st.error("🚨 Cold & Wet")
            profile = "C"
            st.caption("Tắc nghẽn + Tưới máu kém")
        elif congestion >= 2:
            st.warning("## Profile B")
            st.warning("⚠️ Warm & Wet")
            profile = "B"
            st.caption("Tắc nghẽn, tưới máu OK")
        elif perfusion_issues >= 2:
            st.error("## Profile L")
            st.error("❗ Cold & Dry")
            profile = "L"
            st.caption("Tưới máu kém, không tắc nghẽn")
        else:
            st.success("## Profile A")
            st.success("✅ Warm & Dry")
            profile = "A"
            st.caption("Bù trừ tốt")
        
        if hypotension or sbp < 90:
            st.error("⚠️ SHOCK TIM")
    
    st.markdown("---")
    st.markdown("### 2️⃣ Điều Trị")
    
    tabs = st.tabs(["💊 Diuretics", "🩸 Vasodilators", "💉 Inotropes", "🫁 Oxygen/NIV", "📋 GDMT"])
    
    with tabs[0]:  # Diuretics
        st.markdown("#### Lợi Tiểu")
        
        if profile in ["B", "C"]:
            st.success("""
            **Furosemide IV - Thuốc đầu tay cho tắc nghẽn:**
            
            **Liều khởi đầu:**
            - Chưa dùng furosemide: **40mg IV bolus**
            - Đã dùng ≤80mg/ngày: **40mg IV bolus**
            - Đã dùng >80mg/ngày: **Liều gấp đôi liều PO hàng ngày**
            
            **Đánh giá sau 2h:**
            - Nếu tiểu ít: Tăng gấp đôi liều
            - Nếu đáp ứng tốt: Tiếp tục liều đó mỗi 6-12h
            
            **Chiến lược:**
            - **Bolus liên tục** (mỗi 6-12h)
            - Hoặc **Continuous infusion:** 5-10mg/h (nếu đáp ứng kém)
            
            **Mục tiêu:**
            - Cân nặng giảm 0.5-1 kg/ngày
            - Tiểu ≥100-150 mL/h trong 6h đầu
            - Giảm triệu chứng tắc nghẽn
            """)
            
            if profile == "C":
                st.error("""
                **Profile C (Cold & Wet) - Tắc nghẽn + Tưới máu kém:**
                
                ⚠️ **THẬN TRỌNG với lợi tiểu!**
                - Có thể làm giảm thêm cardiac output
                - Cần cải thiện tưới máu trước (inotropes)
                - Sau đó mới lợi tiểu mạnh
                - Liều thấp hơn, tăng dần
                """)
            
            st.info("""
            **Theo dõi:**
            - Điện giải (K, Mg, Na) hàng ngày
            - Creatinine hàng ngày
            - Cân nặng hàng ngày (cùng giờ)
            - Cân bằng nước vào/ra
            
            **Bổ sung kali:**
            - Mục tiêu K >4.0 mmol/L
            - KCl PO hoặc IV nếu thiếu
            """)
        else:
            st.info("""
            **Không tắc nghẽn (Profile A hoặc L):**
            - Không cần lợi tiểu mạnh
            - Cân nhắc liều thấp để duy trì
            - Tập trung vào cải thiện tưới máu (nếu Profile L)
            """)
    
    with tabs[1]:  # Vasodilators
        st.markdown("#### Thuốc Giãn Mạch")
        
        if sbp >= 110:
            st.success("""
            **Nitrates (nếu SBP ≥110 mmHg):**
            
            **Nitroglycerin (GTN) IV:**
            - Bắt đầu: 10-20 mcg/min
            - Tăng 5-10 mcg/min mỗi 5-10 phút
            - Tối đa: 200 mcg/min
            - **Mục tiêu:** Giảm SBP 10-15% (không <90 mmHg)
            
            **Lợi ích:**
            - Giảm preload (giãn tĩnh mạch)
            - Giảm afterload (giãn động mạch)
            - Giảm đau ngực
            - Cải thiện triệu chứng nhanh
            
            **Lưu ý:**
            - Theo dõi BP mỗi 5-10 phút
            - Đau đầu là tác dụng phụ thường gặp
            - Chống chỉ định: SBP <90, sử dụng PDE5i (viagra) trong 24-48h
            """)
        else:
            st.error("""
            **SBP <110 mmHg - KHÔNG dùng vasodilators!**
            - Nguy cơ hạ huyết áp
            - Tập trung vào inotropes nếu cần
            """)
    
    with tabs[2]:  # Inotropes
        st.markdown("#### Thuốc Tăng Co Bóp")
        
        if profile in ["C", "L"] or hypotension:
            st.error("""
            **Chỉ định Inotropes:**
            - Shock tim (SBP <90 mmHg)
            - Tưới máu kém (Profile C hoặc L)
            - Triệu chứng nặng dù điều trị tối ưu
            
            **Lựa chọn:**
            
            **1. Dobutamine (ưu tiên nếu SBP >85):**
            - Liều: 2.5-10 mcg/kg/min
            - Tăng cardiac output
            - Giảm afterload nhẹ
            - **Lưu ý:** Có thể gây hạ huyết áp, tachycardia
            
            **2. Dopamine (nếu SBP <85):**
            - Liều: 5-15 mcg/kg/min
            - Tăng BP + cardiac output
            - **Nhược điểm:** Nhiều tác dụng phụ hơn
            
            **3. Milrinone:**
            - Loading: 25-50 mcg/kg trong 10-20 phút
            - Infusion: 0.375-0.75 mcg/kg/min
            - **Ưu điểm:** Tốt cho người dùng beta-blocker
            - **Nhược điểm:** Có thể gây hạ huyết áp
            
            **4. Levosimendan (nếu có):**
            - Loading: 6-12 mcg/kg trong 10 phút (bỏ qua nếu SBP thấp)
            - Infusion: 0.05-0.2 mcg/kg/min
            - Hiệu quả kéo dài 7-10 ngày
            
            **Theo dõi:**
            - Arterial line monitoring
            - Cardiac output monitoring
            - ECG liên tục (arrhythmias)
            - Electrolytes, lactate
            """)
            
            st.warning("""
            **⚠️ Lưu ý:**
            - Inotropes tăng nguy cơ arrhythmia
            - Tăng nhu cầu oxy cơ tim
            - Chỉ dùng tạm thời để ổn định
            - Không cải thiện tiên lượng dài hạn
            - Mục tiêu: Cai sớm nhất có thể
            """)
        else:
            st.info("""
            **Profile A hoặc B với BP ổn định:**
            - KHÔNG cần inotropes
            - Điều trị với diuretics ± vasodilators
            - GDMT khi ổn định
            """)
    
    with tabs[3]:  # Oxygen/NIV
        st.markdown("#### Hỗ Trợ Hô Hấp")
        
        st.success("""
        **Oxygen Therapy:**
        - **Mục tiêu:** SpO₂ >90% (>94% nếu có thể)
        - Nasal cannula: 2-6 L/min
        - Face mask: 6-10 L/min nếu cần
        - High-flow oxygen nếu suy hô hấp
        
        **Chỉ định:**
        - SpO₂ <90%
        - Khó thở nặng
        - Phù phổi cấp
        """)
        
        st.warning("""
        **NIV (Non-Invasive Ventilation):**
        
        **Chỉ định:**
        - Phù phổi cấp
        - Suy hô hấp (RR >25, SpO₂ <90%)
        - Không đáp ứng với oxygen thường
        
        **Chế độ:**
        - **CPAP:** 5-10 cmH₂O (ưu tiên cho phù phổi cấp)
        - Hoặc **BiPAP:** IPAP 10-15, EPAP 5-8 cmH₂O
        - FiO₂ điều chỉnh để SpO₂ >90%
        
        **Lợi ích:**
        - Giảm công thở
        - Cải thiện oxy hóa
        - Giảm tỷ lệ đặt nội khí quản
        - Giảm tử vong (trong phù phổi cấp)
        
        **Chống chỉ định:**
        - Ngừng thở/ngừng tim
        - Không hợp tác
        - Chảy máu đường tiêu hóa trên nặng
        - Phẫu thuật mặt gần đây
        """)
        
        st.error("""
        **Chỉ định đặt nội khí quản:**
        - Ngừng thở/ngừng tim
        - Suy hô hấp nặng không đáp ứng NIV
        - Lú lẫn nặng, hôn mê
        - Không bảo vệ được đường thở
        - Kiệt sức
        """)
    
    with tabs[4]:  # GDMT
        st.markdown("#### Guideline-Directed Medical Therapy")
        
        st.success("""
        **GDMT cho HFrEF (EF <40%):**
        
        **"Fantastic Four" (4 nhóm thuốc cốt lõi):**
        
        **1. ACE-I/ARB/ARNI:**
        - **Sacubitril-Valsartan** 24/26mg → 49/51mg → 97/103mg x 2/ngày (ưu tiên)
        - Hoặc **Ramipril** 2.5mg → 5mg → 10mg mỗi ngày
        - Hoặc **Enalapril** 2.5mg → 10mg x 2/ngày
        - Hoặc **Valsartan** nếu không dung nạp ACE-I
        
        **2. Beta-blocker:**
        - **Bisoprolol** 1.25mg → 10mg mỗi ngày
        - Hoặc **Carvedilol** 3.125mg → 25mg x 2/ngày
        - Hoặc **Metoprolol succinate** 12.5mg → 200mg mỗi ngày
        - Mục tiêu HR: 50-60 bpm
        
        **3. MRA (Mineralocorticoid Receptor Antagonist):**
        - **Spironolactone** 25mg → 50mg mỗi ngày
        - Hoặc **Eplerenone** 25mg → 50mg mỗi ngày
        - Theo dõi K, Cr
        
        **4. SGLT2 Inhibitor:**
        - **Dapagliflozin** 10mg mỗi ngày
        - Hoặc **Empagliflozin** 10mg mỗi ngày
        - Lợi ích ngay cả không ĐTĐ
        
        **Bổ sung:**
        - **Ivabradine** (nếu HR >70 dù beta-blocker tối ưu)
        - **Hydralazine + Nitrate** (nếu không dung nạp ACE-I/ARB)
        - **Digoxin** (nếu có AF hoặc triệu chứng kéo dài)
        """)
        
        st.info("""
        **HFpEF (EF ≥50%):**
        - Lợi tiểu để giảm tắc nghẽn
        - Kiểm soát THA (<130/80)
        - Kiểm soát HR nếu AF
        - SGLT2 inhibitor (Dapagliflozin, Empagliflozin)
        - Điều trị bệnh kèm theo
        
        **HFmrEF (EF 40-49%):**
        - Điều trị tương tự HFrEF
        - Evidence ít hơn nhưng có lợi ích
        """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Theo Dõi & Xuất Viện")
    
    col_mon1, col_mon2 = st.columns(2)
    
    with col_mon1:
        st.success("""
        **Monitoring:**
        - ✓ Cân nặng hàng ngày (cùng giờ)
        - ✓ Cân bằng nước vào/ra
        - ✓ Vital signs mỗi 4-6h
        - ✓ Electrolytes, Cr, BUN hàng ngày
        - ✓ BNP/NT-proBNP (baseline & discharge)
        - ✓ Echo (đánh giá EF, valves)
        - ✓ Telemetry nếu arrhythmia
        
        **Labs cần làm:**
        - CBC, electrolytes, Cr, BUN
        - BNP hoặc NT-proBNP
        - Troponin (loại trừ ACS)
        - TSH (loại trừ thyroid)
        - Lipid profile
        - HbA1c
        """)
    
    with col_mon2:
        st.info("""
        **Tiêu chuẩn xuất viện:**
        - ✅ Euvolemic (không tắc nghẽn)
        - ✅ Huyết động ổn định
        - ✅ Không cần IV meds ≥24h
        - ✅ Đã chuyển sang PO diuretics
        - ✅ Cr ổn định
        - ✅ Đã tối ưu GDMT
        - ✅ Giáo dục bệnh nhân
        - ✅ Sắp xếp theo dõi ngoại trú
        
        **Thời gian nằm viện:**
        - Trung bình: 4-7 ngày
        - Profile B: 3-5 ngày
        - Profile C: 7-14 ngày
        """)
    
    st.warning("""
    **Giáo dục bệnh nhân (BẮT BUỘC):**
    - 📊 Cân nặng hàng ngày (tăng >2kg/3 ngày → gọi bác sĩ)
    - 💧 Hạn chế nước (<1.5-2 L/ngày)
    - 🧂 Giảm muối (<2g sodium/ngày)
    - 💊 Tuân thủ uống thuốc
    - 🚭 Cai thuốc lá, hạn chế rượu
    - 🏃 Tập luyện vừa phải
    - ⚠️ Nhận biết dấu hiệu xấu đi
    
    **Theo dõi sau xuất viện:**
    - Tuần 1-2: Tái khám (điều chỉnh lợi tiểu)
    - Tháng 1: Tối ưu GDMT
    - Tháng 3: Echo kiểm tra EF
    - Mỗi 3-6 tháng: Follow-up thường quy
    """)
    
    st.markdown("---")
    
    with st.expander("📚 Tài Liệu Tham Khảo"):
        st.markdown("""
        **ESC Guidelines 2021 - Acute and Chronic Heart Failure**
        **AHA/ACC/HFSA Guidelines 2022**
        
        **Clinical Profiles (Forrester/Stevenson):**
        - **Profile A (Warm & Dry):** Well compensated - GDMT optimization
        - **Profile B (Warm & Wet):** Congestion - Diuretics ± vasodilators
        - **Profile C (Cold & Wet):** Congestion + hypoperfusion - Inotropes first, then diuretics
        - **Profile L (Cold & Dry):** Hypoperfusion - Inotropes, careful with diuretics
        
        **GDMT for HFrEF:**
        - ACE-I/ARB/ARNI (Class I)
        - Beta-blocker (Class I)
        - MRA (Class I)
        - SGLT2 inhibitor (Class I - NEW!)
        
        **Diuretic Strategy:**
        - IV loop diuretics for acute decompensation
        - Continuous infusion if inadequate response to boluses
        - Monitor electrolytes, renal function daily
        
        **References:**
        - McDonagh TA et al. Eur Heart J. 2021;42(36):3599-3726.
        - Heidenreich PA et al. Circulation. 2022;145(18):e895-e1032.
        - Felker GM et al. JAMA. 2011;305(24):2543-2550. (DOSE trial)
        
        **Links:**
        - ESC 2021: https://academic.oup.com/eurheartj/article/42/36/3599/6358045
        - AHA/ACC 2022: https://www.ahajournals.org/doi/10.1161/CIR.0000000000001063
        """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol hỗ trợ lâm sàng - cần cá thể hóa theo EF và clinical profile")

