"""
MELD Score (Model for End-Stage Liver Disease)
Dự đoán tử vong 3 tháng ở bệnh nhân xơ gan

Formula:
MELD = 3.78×ln[bilirubin(mg/dL)] + 11.2×ln[INR] + 9.57×ln[creatinine(mg/dL)] + 6.43

Score range: 6-40
- Higher score = Higher 3-month mortality
- Used for liver transplant prioritization

Reference:
Kamath PS, et al. A model to predict survival in patients with end-stage liver disease.
Hepatology. 2001;33(2):464-70.
"""

import streamlit as st
import math


def calculate_meld(bilirubin, inr, creatinine, dialysis=False):
    """
    Calculate MELD Score
    
    Args:
        bilirubin: Total bilirubin in mg/dL
        inr: INR value
        creatinine: Serum creatinine in mg/dL
        dialysis: Whether patient had dialysis twice in past week
    
    Returns:
        MELD score (6-40)
    """
    # Apply minimums
    bili = max(bilirubin, 1.0)
    inr_val = max(inr, 1.0)
    cr = max(creatinine, 1.0)
    
    # If on dialysis or Cr > 4, cap creatinine at 4
    if dialysis or cr > 4.0:
        cr = 4.0
    
    # MELD formula
    meld = (
        3.78 * math.log(bili) +
        11.2 * math.log(inr_val) +
        9.57 * math.log(cr) +
        6.43
    )
    
    # Round to nearest integer
    meld = round(meld)
    
    # Cap between 6 and 40
    meld = max(6, min(40, meld))
    
    return meld


def render():
    """Render MELD Score Calculator"""
    
    st.subheader("🩸 MELD Score")
    st.caption("Model for End-Stage Liver Disease - Tiên lượng xơ gan & ưu tiên ghép gan")
    
    st.markdown("""
    **MELD Score** dự đoán tỷ lệ tử vong 3 tháng ở bệnh nhân xơ gan mất bù.
    
    **Ứng dụng:**
    - **Ưu tiên ghép gan** (MELD càng cao càng ưu tiên)
    - Dự đoán tử vong ngắn hạn
    - Quyết định điều trị (TIPS, phẫu thuật)
    """)
    
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 🔬 Xét Nghiệm")
        
        # 1. Bilirubin
        st.markdown("#### 1. Bilirubin Toàn Phần")
        
        bili_unit = st.radio(
            "Đơn vị:",
            ["mg/dL", "µmol/L (SI)"],
            horizontal=True,
            key="bili_meld"
        )
        
        if "mg/dL" in bili_unit:
            bili = st.number_input(
                "Bilirubin (mg/dL):",
                min_value=0.1,
                max_value=30.0,
                value=1.0,
                step=0.1,
                help="Bình thường: 0.3-1.2 mg/dL"
            )
            bili_mgdl = bili
            st.caption(f"≈ {bili * 17.1:.0f} µmol/L")
        else:
            bili = st.number_input(
                "Bilirubin (µmol/L):",
                min_value=0.0,
                max_value=500.0,
                value=17.0,
                step=1.0,
                help="Bình thường: 5-21 µmol/L"
            )
            bili_mgdl = bili / 17.1
            st.caption(f"≈ {bili_mgdl:.1f} mg/dL")
        
        # 2. INR
        st.markdown("#### 2. INR")
        inr = st.number_input(
            "INR (International Normalized Ratio):",
            min_value=0.8,
            max_value=10.0,
            value=1.0,
            step=0.1,
            help="Bình thường: 0.9-1.1"
        )
        
        # 3. Creatinine
        st.markdown("#### 3. Creatinine")
        
        cr_unit = st.radio(
            "Đơn vị:",
            ["µmol/L (SI)", "mg/dL"],
            horizontal=True,
            index=0,
            key="cr_meld"
        )
        
        if "µmol/L" in cr_unit:
            cr = st.number_input(
                "Creatinine (µmol/L):",
                min_value=0.0,
                max_value=1500.0,
                value=88.0,
                step=5.0,
                help="Bình thường: 62-115 µmol/L"
            )
            cr_mgdl = cr / 88.4
            st.caption(f"≈ {cr_mgdl:.1f} mg/dL")
        else:  # mg/dL
            cr = st.number_input(
                "Creatinine (mg/dL):",
                min_value=0.1,
                max_value=15.0,
                value=1.0,
                step=0.1,
                help="Bình thường: 0.7-1.3 mg/dL"
            )
            cr_mgdl = cr
            st.caption(f"≈ {cr * 88.4:.0f} µmol/L")
        
        # 4. Dialysis
        st.markdown("#### 4. Lọc Máu")
        dialysis = st.checkbox(
            "Đã lọc máu ≥2 lần trong 7 ngày qua HOẶC CRRT 24h",
            help="Nếu có, Cr sẽ được tính là 4.0 mg/dL"
        )
        
        if dialysis:
            st.warning("⚠️ Có lọc máu → Creatinine được tính = 4.0 mg/dL")
        
        st.markdown("---")
        
        if st.button("🧮 Tính MELD Score", type="primary", use_container_width=True):
            # Calculate MELD
            meld_score = calculate_meld(bili_mgdl, inr, cr_mgdl, dialysis)
            
            # Determine mortality risk
            if meld_score < 10:
                mortality_3m = "1.9%"
                mortality_1yr = "5-10%"
                severity = "XƠ GAN NHẸ"
                color = "green"
                transplant_priority = "Thấp"
            elif meld_score < 20:
                mortality_3m = "6.0%"
                mortality_1yr = "15-25%"
                severity = "XƠ GAN TRUNG BÌNH"
                color = "orange"
                transplant_priority = "Trung bình"
            elif meld_score < 30:
                mortality_3m = "19.6%"
                mortality_1yr = "40-60%"
                severity = "XƠ GAN NẶNG"
                color = "red"
                transplant_priority = "Cao"
            else:
                mortality_3m = "52.6%"
                mortality_1yr = ">70%"
                severity = "XƠ GAN RẤT NẶNG"
                color = "darkred"
                transplant_priority = "Rất cao (khẩn cấp)"
            
            with col2:
                st.markdown("### 📊 Kết Quả")
                
                st.markdown(f"""
                <div style="background-color: {color}; padding: 20px; border-radius: 10px; text-align: center;">
                    <h1 style="color: white; margin: 0;">MELD = {meld_score}</h1>
                    <p style="color: white; margin: 0; font-size: 1.2rem;">Điểm 6-40</p>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("<br>", unsafe_allow_html=True)
                
                st.metric("Tử vong 3 tháng", mortality_3m)
                st.metric("Ưu tiên ghép gan", transplant_priority)
            
            st.markdown("---")
            st.markdown("### 📋 ĐÁNH GIÁ & KHUYẾN NGHỊ")
            
            # Display interpretation
            if meld_score < 10:
                st.success(f"""
                **🟢 MELD = {meld_score} - {severity}**
                
                **Tỷ lệ tử vong:**
                - 3 tháng: {mortality_3m}
                - 1 năm: {mortality_1yr}
                
                **Đánh giá:** Xơ gan còn bù trừ tốt hoặc bệnh gan nhẹ.
                
                **Khuyến nghị:**
                
                1. **Theo dõi định kỳ:**
                   - Khám gan mỗi 3-6 tháng
                   - MELD score mỗi 3 tháng
                   - Siêu âm + AFP mỗi 6 tháng (sàng lọc HCC)
                
                2. **Điều trị nguyên nhân:**
                   - Viêm gan B/C: Kháng virus
                   - Rượu: Cai hoàn toàn
                   - NASH: Giảm cân, kiểm soát ĐTĐ
                
                3. **Ghép gan:**
                   - **CHƯA có chỉ định** ghép gan
                   - Tiếp tục điều trị bảo tồn
                   - Theo dõi MELD định kỳ
                
                4. **Chỉ định phẫu thuật:**
                   - ✅ Có thể phẫu thuật nếu cần
                   - Nguy cơ phẫu thuật chấp nhận được
                
                **Tiên lượng:** Tốt với điều trị thích hợp.
                """)
            
            elif meld_score < 15:
                st.info(f"""
                **🟡 MELD = {meld_score} - {severity}**
                
                **Tỷ lệ tử vong:**
                - 3 tháng: {mortality_3m}
                - 1 năm: {mortality_1yr}
                
                **Đánh giá:** Bệnh gan tiến triển, cần theo dõi sát.
                
                **Khuyến nghị:**
                
                1. **Theo dõi chặt chẽ:**
                   - Khám gan mỗi 2-3 tháng
                   - MELD score mỗi 1-2 tháng
                   - Siêu âm + AFP mỗi 3-6 tháng
                
                2. **Điều trị tích cực:**
                   - Điều trị nguyên nhân mạnh mẽ
                   - Kiểm soát biến chứng (ascites, varices)
                   - Phòng ngừa SBP, HE
                
                3. **Đánh giá ghép gan:**
                   - **MELD ≥15: Cân nhắc đánh giá ghép gan**
                   - Liên hệ trung tâm ghép gan
                   - Đánh giá tiêu chí ghép gan
                   - Tìm người cho nếu có thể (living donor)
                
                4. **Phẫu thuật:**
                   - ⚠️ Nguy cơ phẫu thuật tăng
                   - Cân nhắc lợi ích/nguy cơ cẩn thận
                   - Tối ưu hóa trước phẫu thuật
                
                **Tiên lượng:** Trung bình. Cần chuẩn bị ghép gan nếu MELD tăng.
                """)
            
            elif meld_score < 20:
                st.warning(f"""
                **🟠 MELD = {meld_score} - {severity}**
                
                **Tỷ lệ tử vong:**
                - 3 tháng: {mortality_3m}
                - 1 năm: {mortality_1yr}
                
                **Đánh giá:** Xơ gan nặng, nguy cơ cao, CẦN ghép gan.
                
                **Khuyến nghị:**
                
                1. **ĐÁNH GIÁ GHÉP GAN KHẨN CẤP:**
                   - ✅ **Chỉ định ghép gan rõ ràng**
                   - Liên hệ trung tâm ghép gan NGAY
                   - Đăng ký danh sách chờ ghép
                   - MELD {meld_score} = Ưu tiên trung bình-cao
                
                2. **Theo dõi sát:**
                   - Khám mỗi 1-2 tháng
                   - MELD mỗi 2-4 tuần
                   - Theo dõi biến chứng liên tục
                
                3. **Điều trị biến chứng tích cực:**
                   - Ascites: Lợi tiểu, paracentesis
                   - HE: Lactulose, rifaximin
                   - Varices: Beta-blocker, nội soi
                   - SBP prophylaxis
                
                4. **Cân nhắc TIPS:**
                   - Nếu ascites khó trị
                   - Nếu varices chảy máu tái phát
                   - Cầu nối đến ghép gan
                
                5. **Phẫu thuật:**
                   - ❌ **Tránh phẫu thuật không cần thiết**
                   - Nguy cơ tử vong cao
                   - Chỉ phẫu thuật khi cấp cứu
                
                6. **Chuẩn bị ghép gan:**
                   - Đánh giá toàn diện
                   - Xử lý các vấn đề y tế khác
                   - Hỗ trợ tâm lý, tài chính
                   - Living donor nếu có thể
                
                **Tiên lượng:** Xấu nếu không ghép gan. Cần ghép gan sớm.
                """)
            
            else:  # MELD >= 20
                st.error(f"""
                **🔴 MELD = {meld_score} - {severity}** 🚨
                
                **Tỷ lệ tử vong:**
                - 3 tháng: {mortality_3m}
                - 1 năm: {mortality_1yr}
                
                **Đánh giá:** Xơ gan giai đoạn cuối, nguy cơ tử vong rất cao, CẦN ghép gan KHẨN CẤP.
                
                **Khuyến nghị:**
                
                1. **GHÉP GAN KHẨN CẤP:**
                   - 🚨 **Chỉ định ghép gan ưu tiên cao**
                   - MELD {meld_score} = Status cao trên danh sách chờ
                   - Liên hệ trung tâm ghép gan NGAY nếu chưa
                   - Xem xét **Living donor transplant** (nhanh hơn)
                   - Xem xét **Status 1** nếu có suy gan cấp
                
                2. **Nhập viện/Theo dõi ICU:**
                   - Cân nhắc nhập viện nếu không ổn định
                   - ICU nếu biến chứng nặng
                   - Monitoring sát các biến chứng
                
                3. **Điều trị hỗ trợ tích cực:**
                   
                   **Suy thận (HRS):**
                   - Terlipressin + Albumin
                   - Midodrine + Octreotide + Albumin
                   - Dialysis nếu cần (bridge to transplant)
                   
                   **Bệnh não gan:**
                   - Lactulose tối đa
                   - Rifaximin
                   - Tìm và điều trị yếu tố kích phát
                   
                   **Cổ chướng:**
                   - Paracentesis thường xuyên + Albumin
                   - TIPS nếu khó trị (bridge to transplant)
                   
                   **Nhiễm trùng:**
                   - SBP prophylaxis
                   - Điều trị nhiễm trùng tích cực
                   - Kháng sinh broad-spectrum sớm
                
                4. **Phẫu thuật:**
                   - ❌ **CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI**
                   - Nguy cơ tử vong cực cao (>50%)
                   - Chỉ phẫu thuật khi tính mạng nguy cấp
                
                5. **Chuẩn bị ghép gan:**
                   - Đánh giá phẫu thuật tim phổi
                   - Đánh giá tâm lý, xã hội
                   - Giáo dục bệnh nhân/gia đình
                   - Sẵn sàng 24/7 khi có gan
                
                6. **Chăm sóc hỗ trợ:**
                   - Dinh dưỡng: BCAA, protein cao
                   - Hỗ trợ tâm lý
                   - Palliative care tham vấn
                   - Advance directives
                
                7. **Thảo luận với gia đình:**
                   - Tiên lượng rất xấu
                   - Tầm quan trọng của ghép gan
                   - Nguy cơ tử vong cao nếu không ghép
                   - Goals of care
                
                **Tiên lượng:** Rất xấu. Ghép gan là phương pháp duy nhất cứu sống. 
                Tỷ lệ tử vong rất cao ({mortality_3m} trong 3 tháng) nếu không ghép gan.
                
                **MELD ≥30-35:** Cân nhắc **Status 1** (ưu tiên cao nhất) nếu có suy gan cấp trên nền mạn.
                """)
            
            # Detailed info
            st.markdown("---")
            with st.expander("🧮 Công Thức Tính MELD"):
                st.markdown(f"""
                **MELD = 3.78×ln[Bili] + 11.2×ln[INR] + 9.57×ln[Cr] + 6.43**
                
                **Giá trị đầu vào:**
                - Bilirubin: {bili_mgdl:.2f} mg/dL
                - INR: {inr:.2f}
                - Creatinine: {cr_mgdl:.2f} mg/dL {"(capped at 4.0)" if (dialysis or cr_mgdl > 4) else ""}
                - Dialysis: {"Có" if dialysis else "Không"}
                
                **Lưu ý:**
                - Giá trị tối thiểu: 1.0 (để tránh log âm)
                - Nếu dialysis hoặc Cr >4: Cr = 4.0
                - Kết quả làm tròn đến số nguyên
                - Giới hạn: 6-40 điểm
                
                **Kết quả:** MELD = **{meld_score}**
                """)
            
            with st.expander("📊 Bảng Tỷ Lệ Tử Vong Theo MELD"):
                st.markdown("""
                | MELD Score | Tử vong 3 tháng | Tử vong 1 năm | Mức Độ | Ưu tiên ghép |
                |------------|-----------------|---------------|---------|--------------|
                | <10 | 1.9% | 5-10% | 🟢 Nhẹ | Thấp |
                | 10-14 | 6.0% | 15-25% | 🟡 Trung bình | Trung bình |
                | 15-19 | 10-15% | 25-40% | 🟠 Nặng | Cao |
                | 20-24 | 19.6% | 40-55% | 🔴 Rất nặng | Rất cao |
                | 25-29 | 30-40% | 55-70% | 🔴 Cực nặng | Cực cao |
                | 30-34 | 52.6% | >70% | ⚫ Giai đoạn cuối | Khẩn cấp |
                | ≥35 | >60% | >80% | ⚫ Status 1 | Ưu tiên tối đa |
                
                **Nguồn:** UNOS (United Network for Organ Sharing) data
                """)
            
            with st.expander("🏥 MELD và Ưu Tiên Ghép Gan"):
                st.markdown("""
                **Hệ thống MELD dùng để phân bổ gan ghép:**
                
                **Nguyên tắc:**
                - MELD càng cao → Ưu tiên càng cao
                - Phản ánh nguy cơ tử vong trong 3 tháng
                - Công bằng dựa trên mức độ bệnh nặng
                
                **Cutoffs quan trọng:**
                - **MELD <15:** Chưa cần ghép, theo dõi
                - **MELD 15-24:** Có chỉ định, đưa vào danh sách chờ
                - **MELD 25-29:** Ưu tiên cao, cần ghép sớm
                - **MELD ≥30:** Ưu tiên rất cao, cần ghép khẩn
                - **Status 1 (Acute liver failure):** Ưu tiên tuyệt đối
                
                **MELD exceptions (điểm cộng):**
                - **HCC:** MELD exception points (thường lên 22-28 tùy giai đoạn)
                - **Hepatopulmonary syndrome**
                - **Portopulmonary hypertension**
                - **Primary hyperoxaluria**
                - **Các tình trạng đặc biệt khác**
                
                **Thời gian chờ trung bình:**
                - MELD <15: Có thể chờ lâu (>1 năm)
                - MELD 15-24: Vài tháng đến 1 năm
                - MELD 25-29: Vài tuần đến vài tháng
                - MELD ≥30: Vài ngày đến vài tuần
                - Status 1: Vài giờ đến vài ngày
                
                **Cập nhật MELD:**
                - MELD 25-30: Cập nhật mỗi tuần
                - MELD 19-24: Cập nhật mỗi tháng
                - MELD 11-18: Cập nhật mỗi 3 tháng
                - MELD <11: Có thể đánh giá lại chỉ định
                """)
            
            with st.expander("🔄 MELD vs Child-Pugh"):
                st.markdown("""
                **So sánh hai thang điểm chính:**
                
                | Đặc điểm | MELD | Child-Pugh |
                |----------|------|------------|
                | **Tham số** | 3 (chỉ xét nghiệm) | 5 (2 lâm sàng + 3 XN) |
                | **Khách quan** | ✅ Hoàn toàn | ❌ Chủ quan (ascites, HE) |
                | **Liên tục** | ✅ 6-40 | ❌ 3 class (A,B,C) |
                | **Ưu tiên ghép gan** | ✅ Sử dụng | ❌ Không dùng |
                | **Tiên lượng ngắn hạn** | ✅ Rất tốt (3 tháng) | ✅ Tốt |
                | **Phân loại phẫu thuật** | ❌ Ít dùng | ✅ Thường dùng |
                | **Đơn giản** | ✅ Đơn giản | ⚠️ Tương đối đơn giản |
                
                **Khi nào dùng gì?**
                - **MELD:** Ghép gan, tiên lượng ngắn hạn, nghiên cứu
                - **Child-Pugh:** Phẫu thuật, điều trị, đánh giá tổng quát
                
                **Khuyến nghị:** Sử dụng CẢ HAI để đánh giá toàn diện!
                
                **Tương quan gần đúng:**
                - MELD <10 ≈ Child A
                - MELD 10-19 ≈ Child B
                - MELD ≥20 ≈ Child C
                (Nhưng không hoàn toàn tương ứng)
                """)
            
            with st.expander("📚 Tài Liệu Tham Khảo"):
                st.markdown("""
                **Primary Reference:**
                - Kamath PS, Wiesner RH, Malinchoc M, et al. 
                  *A model to predict survival in patients with end-stage liver disease.* 
                  Hepatology. 2001 Feb;33(2):464-70. [PMID: 11172350]
                
                **MELD for Transplant Allocation:**
                - Wiesner R, Edwards E, Freeman R, et al. 
                  *Model for end-stage liver disease (MELD) and allocation of donor livers.* 
                  Gastroenterology. 2003 Jan;124(1):91-6.
                
                - Kamath PS, Kim WR; Advanced Liver Disease Study Group. 
                  *The model for end-stage liver disease (MELD).* 
                  Hepatology. 2007 Mar;45(3):797-805.
                
                **MELD-Na (Updated formula):**
                - Biggins SW, et al. 
                  *Serum sodium predicts mortality in patients listed for liver transplantation.* 
                  Hepatology. 2005 Jul;42(1):79-88.
                
                - Kim WR, et al. 
                  *Hyponatremia and mortality among patients on the liver-transplant waiting list.* 
                  N Engl J Med. 2008 Sep 4;359(10):1018-26.
                
                **Guidelines:**
                - Martin P, DiMartini A, Feng S, Brown R Jr, Fallon M. 
                  *Evaluation for liver transplantation in adults: 2013 practice guideline by AASLD and AST.* 
                  Hepatology. 2014 Mar;59(3):1144-65.
                
                - EASL Clinical Practice Guidelines: Liver transplantation. 
                  J Hepatol. 2016 Feb;64(2):433-85.
                """)
    
    # Educational content
    st.markdown("---")
    st.markdown("### 📖 THÔNG TIN THÊM")
    
    with st.expander("❓ MELD Score là gì?"):
        st.markdown("""
        **MELD (Model for End-Stage Liver Disease)** là công thức toán học 
        dự đoán tỷ lệ tử vong 3 tháng ở bệnh nhân xơ gan.
        
        **Lịch sử:**
        - 2000: Mayo Clinic phát triển cho bệnh nhân TIPS
        - 2002: UNOS chấp nhận dùng cho phân bổ gan ghép
        - 2016: MELD-Na (bổ sung sodium)
        
        **Ưu điểm:**
        - Hoàn toàn khách quan (3 xét nghiệm)
        - Liên tục (6-40 điểm)
        - Dự đoán chính xác tử vong ngắn hạn
        - Công bằng trong phân bổ gan ghép
        - Validated rộng rãi
        
        **Hạn chế:**
        - Không tính biến chứng (ascites, HE, varices)
        - Kém chính xác ở MELD thấp (<10)
        - Một số tình trạng cần MELD exception
        - Không dự đoán HCC
        """)
    
    with st.expander("🆕 MELD-Na (MELD 3.0)"):
        st.markdown("""
        **MELD-Na** là phiên bản cải tiến, bổ sung **Sodium**.
        
        **Lý do:**
        - Hyponatremia là yếu tố tiên lượng độc lập
        - Phổ biến ở xơ gan mất bù (20-50%)
        - Cải thiện dự đoán tử vong
        
        **Công thức MELD-Na:**
        ```
        MELD-Na = MELD + 1.32×(137-Na) - [0.033×MELD×(137-Na)]
        ```
        
        - Na giới hạn: 125-137 mEq/L
        - MELD-Na thường cao hơn MELD 1-10 điểm
        
        **Khi nào dùng MELD-Na:**
        - **UNOS đã chuyển sang MELD-Na từ 2016**
        - Dùng cho phân bổ gan ghép tại Mỹ
        - Một số nước châu Âu vẫn dùng MELD
        
        **Ở Việt Nam:** Hiện tại chủ yếu dùng MELD, 
        nhưng MELD-Na đang được áp dụng dần.
        """)
    
    with st.expander("⚠️ Hạn Chế Của MELD"):
        st.markdown("""
        **MELD có một số hạn chế:**
        
        1. **Không phản ánh biến chứng:**
           - Không tính ascites
           - Không tính hepatic encephalopathy
           - Không tính variceal bleeding
           - → Bệnh nhân có thể MELD thấp nhưng rất sick
        
        2. **MELD thấp (<15) kém chính xác:**
           - Dự đoán tử vong kém ở MELD <10
           - Nhiều bệnh nhân Child B có MELD <15
        
        3. **Không dự đoán HCC:**
           - HCC cần MELD exception points
           - Tiêu chí Milan để được exception
        
        4. **Biến động xét nghiệm:**
           - Creatinine dao động (hydration, thuốc)
           - INR có thể bị ảnh hưởng bởi vitamin K
           - Bilirubin có thể tăng tạm thời
        
        5. **Một số tình trạng đặc biệt:**
           - Hepatopulmonary syndrome
           - Portopulmonary hypertension
           - Pruritis không kiểm soát
           - Recurrent cholangitis
           → Cần MELD exception
        
        6. **Không phù hợp:**
           - Suy gan cấp (dùng King's College Criteria)
           - Xơ gan còn bù tốt (MELD <10)
           - Một số bệnh gan cholestatic
        """)
    
    with st.expander("💊 Yếu Tố Ảnh Hưởng MELD"):
        st.markdown("""
        **Các yếu tố có thể làm tăng/giảm MELD:**
        
        **Tăng MELD (không phản ánh bệnh gan nặng hơn):**
        - **Suy thận cấp** (AKI, HRS type 1)
        - **Thuốc độc thận:** NSAIDs, aminoglycosides, contrast
        - **Mất nước:** Lợi tiểu quá mức, paracentesis không albumin
        - **Sepsis**
        - **Kháng đông quá mức:** Warfarin
        
        **Giảm MELD (không phản ánh bệnh gan tốt hơn):**
        - **Vitamin K:** Cải thiện INR tạm thời
        - **Thuốc:** Steroid (giảm bili), FFP/albumin
        - **Hydration:** Cải thiện Cr tạm thời
        - **Dialysis:** Giảm Cr nhưng MELD cap at 40
        
        **Khuyến nghị:**
        - Đánh giá MELD khi bệnh nhân ổn định
        - Tránh tác nhân nhiễu (thuốc, dehydration)
        - Lặp lại MELD định kỳ để theo dõi xu hướng
        - Xem xét bối cảnh lâm sàng, không chỉ dựa vào số
        """)
    
    # Footer
    st.markdown("---")
    st.caption("📚 Based on: Kamath PS, et al. Hepatology. 2001;33(2):464-70")
    st.caption("⚠️ Standard score for liver transplant prioritization (UNOS)")
    st.caption("🏥 Predicts 3-month mortality in cirrhosis patients")

