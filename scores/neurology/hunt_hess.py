"""
Hunt & Hess Scale - Classification of Subarachnoid Hemorrhage (SAH)
Predicts mortality and outcome in patients with aneurysmal subarachnoid hemorrhage

Grades 1-5 based on clinical features
- Higher grade = Higher mortality risk

Reference:
Hunt WE, Hess RM. Surgical risk as related to time of intervention in the repair of intracranial aneurysms.
J Neurosurg. 1968;28(1):14-20.
"""

import streamlit as st


def render():
    """Render Hunt & Hess Scale Calculator"""
    
    st.subheader("🧠 Hunt & Hess Scale - Xuất Huyết Dưới Nhện")
    st.caption("Phân loại mức độ nghiêm trọng của xuất huyết dưới màng nhện")
    
    st.markdown("""
    **Hunt & Hess Scale** là thang điểm lâm sàng dùng để phân loại mức độ nghiêm trọng 
    của xuất huyết dưới màng nhện do vỡ phình mạch (Subarachnoid Hemorrhage - SAH).
    """)
    
    st.markdown("---")
    
    # Selection
    st.markdown("### 🩺 Chọn Mức Độ Lâm Sàng")
    
    st.info("""
    **Hướng dẫn:** Chọn mức độ phù hợp nhất với tình trạng lâm sàng của bệnh nhân.
    Nếu có thêm biến chứng toàn thân nghiêm trọng (tăng huyết áp nặng, đái tháo đường, 
    xơ vữa mạch nặng, COPD, vasospasm trên DSA), cần **cộng thêm 1 grade**.
    """)
    
    grade_descriptions = {
        "Grade 1": {
            "name": "Grade 1 - Không triệu chứng hoặc đau đầu nhẹ",
            "desc": """
            **Triệu chứng:**
            - Không có triệu chứng hoặc
            - Đau đầu nhẹ và
            - Cứng gáy nhẹ
            - Không có liệt thần kinh sọ (trừ CN III, IV, VI)
            
            **Tình trạng ý thức:** Tỉnh táo, giao tiếp bình thường
            """,
            "mortality": "0-5%",
            "outcome": "Rất tốt",
            "color": "green"
        },
        "Grade 2": {
            "name": "Grade 2 - Đau đầu vừa đến nặng, cứng gáy",
            "desc": """
            **Triệu chứng:**
            - Đau đầu vừa phải đến nặng
            - Cứng gáy rõ
            - Có thể có liệt thần kinh sọ (đặc biệt CN III, IV, VI)
            - Không có thiếu sót thần kinh nặng
            
            **Tình trạng ý thức:** Tỉnh táo, có thể giao tiếp
            """,
            "mortality": "5-10%",
            "outcome": "Tốt",
            "color": "green"
        },
        "Grade 3": {
            "name": "Grade 3 - Buồn ngủ, lú lẫn, thiếu sót thần kinh nhẹ",
            "desc": """
            **Triệu chứng:**
            - Buồn ngủ (drowsiness)
            - Lú lẫn (confusion)
            - Thiếu sót thần kinh khu trú nhẹ
            
            **Tình trạng ý thức:** Giảm nhẹ, còn phản ứng với kích thích
            """,
            "mortality": "10-15%",
            "outcome": "Trung bình",
            "color": "orange"
        },
        "Grade 4": {
            "name": "Grade 4 - Hôn mê, liệt nửa người, cứng co sớm",
            "desc": """
            **Triệu chứng:**
            - Hôn mê (stupor - GCS 6-8)
            - Liệt nửa người vừa đến nặng
            - Cứng co tư thế sớm (early decerebrate rigidity)
            - Rối loạn thần kinh thực vật
            
            **Tình trạng ý thức:** Giảm nặng, chỉ phản ứng với kích thích đau
            """,
            "mortality": "60-70%",
            "outcome": "Xấu",
            "color": "red"
        },
        "Grade 5": {
            "name": "Grade 5 - Hôn mê sâu, cứng co tư thế, hấp hối",
            "desc": """
            **Triệu chứng:**
            - Hôn mê sâu (deep coma - GCS 3-5)
            - Cứng co tư thế (decerebrate rigidity)
            - Tình trạng hấp hối (moribund appearance)
            - Ngừng thở hoặc cần thở máy
            
            **Tình trạng ý thức:** Không có phản ứng hoặc phản ứng tối thiểu
            """,
            "mortality": "70-90%",
            "outcome": "Rất xấu",
            "color": "red"
        }
    }
    
    selected_grade = st.radio(
        "Chọn Hunt & Hess Grade:",
        list(grade_descriptions.keys()),
        format_func=lambda x: grade_descriptions[x]["name"],
        help="Chọn grade phù hợp nhất với tình trạng lâm sàng"
    )
    
    # Display selected grade details
    grade_info = grade_descriptions[selected_grade]
    
    with st.expander(f"📖 Chi Tiết {selected_grade}", expanded=True):
        st.markdown(grade_info["desc"])
    
    # Serious systemic disease modifier
    st.markdown("---")
    st.markdown("### ⚠️ Bệnh Toàn Thân Nghiêm Trọng")
    
    serious_disease = st.checkbox(
        "Có biến chứng toàn thân nghiêm trọng (tăng huyết áp nặng, đái tháo đường, xơ vữa mạch nặng, COPD nặng, vasospasm trên DSA)",
        help="Nếu có, cộng thêm 1 grade vào điểm cuối cùng"
    )
    
    # Calculate final grade
    grade_number = int(selected_grade.split()[1])
    if serious_disease:
        final_grade = min(grade_number + 1, 5)  # Max grade 5
        st.warning(f"**Điều chỉnh:** {selected_grade} + 1 (biến chứng toàn thân) = **Grade {final_grade}**")
    else:
        final_grade = grade_number
    
    # Calculate button
    st.markdown("---")
    if st.button("🧮 Đánh Giá Hunt & Hess", type="primary", use_container_width=True):
        st.session_state.total_calculations = st.session_state.get('total_calculations', 0) + 1
        
        # Get final grade info
        final_grade_key = f"Grade {final_grade}"
        final_info = grade_descriptions[final_grade_key]
        
        # Display result
        st.markdown("---")
        st.markdown("## 📊 KẾT QUẢ")
        
        # Grade badge
        st.markdown(f"""
        <div style="background-color: {final_info['color']}; padding: 20px; border-radius: 10px; text-align: center;">
            <h1 style="color: white; margin: 0;">Hunt & Hess Grade {final_grade}</h1>
            <p style="color: white; margin: 0; font-size: 1.2rem;">{final_info['mortality']} tỷ lệ tử vong</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Metrics
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Hunt & Hess Grade", f"Grade {final_grade}/5")
        
        with col2:
            st.metric("Tỷ Lệ Tử Vong", final_info["mortality"])
        
        with col3:
            st.metric("Tiên Lượng", final_info["outcome"])
        
        st.markdown("---")
        
        # Detailed interpretation and recommendations
        st.markdown("### 📋 ĐÁNH GIÁ & KHUYẾN NGHỊ")
        
        if final_grade == 1:
            st.success(f"""
            **🟢 HUNT & HESS GRADE 1** - Tiên lượng rất tốt
            
            **Tỷ lệ tử vong:** 0-5%  
            **Tỷ lệ kết cục tốt:** >90%
            
            **Đặc điểm lâm sàng:**
            - Bệnh nhân tỉnh táo, giao tiếp tốt
            - Không có triệu chứng hoặc đau đầu nhẹ
            - Cứng gáy nhẹ
            - Không có thiếu sót thần kinh nặng
            
            **Khuyến nghị xử trí:**
            
            1. **Nhập viện ngay:**
               - Khoa Thần kinh hoặc Stroke Unit
               - Theo dõi sát (mỗi 2-4 giờ): GCS, pupils, dấu hiệu thần kinh khu trú
            
            2. **Chẩn đoán hình ảnh:**
               - **CT angiography (CTA)** hoặc **DSA (Digital Subtraction Angiography)** để xác định vị trí phình mạch
               - CT scan não không thuốc để baseline
            
            3. **Kiểm soát huyết áp:**
               - Mục tiêu: **SBP <160 mmHg** (trước khi xử lý phình mạch)
               - Sau xử lý phình mạch: SBP <140 mmHg
               - Thuốc: Nicardipine, Labetalol IV
            
            4. **Phòng ngừa tái xuất huyết:**
               - **Xử lý phình mạch SỚM** (trong 24-72h):
                 * **Coiling nội mạch** (ưu tiên nếu phình mạch phù hợp)
                 * **Phẫu thuật clipping** (nếu không thể coiling hoặc phình mạch phức tạp)
               - Tránh gắng sức, Valsalva
               - Làm mềm phân (stool softener)
            
            5. **Phòng ngừa vasospasm:**
               - **Nimodipine 60mg PO q4h × 21 ngày** (BẮT BUỘC)
               - Duy trì euvolemia (tránh giảm thể tích)
               - Theo dõi vasospasm: TCD (Transcranial Doppler) hàng ngày từ ngày 3-14
            
            6. **Kiểm soát triệu chứng:**
               - Giảm đau: Acetaminophen, opioids nhẹ nếu cần
               - Chống nôn: Ondansetron
               - Tránh aspirin, NSAIDs (tăng nguy cơ chảy máu)
            
            7. **Theo dõi:**
               - Neurological checks q2-4h
               - CT scan lặp lại nếu có diễn biến xấu
               - DSA sau xử lý để confirm occlusion phình mạch
            
            **Tiên lượng:** Rất tốt nếu xử lý sớm và phòng ngừa vasospasm hiệu quả.
            """)
        
        elif final_grade == 2:
            st.success(f"""
            **🟢 HUNT & HESS GRADE 2** - Tiên lượng tốt
            
            **Tỷ lệ tử vong:** 5-10%  
            **Tỷ lệ kết cục tốt:** 80-90%
            
            **Đặc điểm lâm sàng:**
            - Tỉnh táo, giao tiếu tốt
            - Đau đầu vừa đến nặng
            - Cứng gáy rõ
            - Có thể có liệt thần kinh sọ (CN III, IV, VI)
            
            **Khuyến nghị xử trí:**
            
            1. **Nhập viện ICU hoặc Stroke Unit:**
               - Theo dõi sát mỗi 1-2 giờ
               - Cardiac monitoring
            
            2. **Chẩn đoán hình ảnh KHẨN CẤP:**
               - CT scan não
               - **CTA hoặc DSA** để xác định phình mạch
               - CT perfusion nếu nghi vasospasm
            
            3. **Xử lý phình mạch SỚM** (trong 24h nếu có thể):
               - **Coiling nội mạch** (first-line cho phần lớn trường hợp)
               - **Surgical clipping** (nếu không thể coiling)
               - Hội chẩn Stroke Team + Neurosurgery + Interventional Radiology
            
            4. **Kiểm soát huyết áp:**
               - **SBP <160 mmHg** trước xử lý phình mạch
               - SBP <140 mmHg sau xử lý
               - IV nicardipine hoặc labetalol
            
            5. **Phòng ngừa vasospasm (QUAN TRỌNG):**
               - **Nimodipine 60mg PO q4h × 21 ngày**
               - Maintain euvolemia (CVP 8-10 mmHg)
               - TCD hàng ngày từ ngày 3
               - Nếu có vasospasm: **3H therapy** (Hypertension, Hypervolemia, Hemodilution)
            
            6. **Kiểm soát triệu chứng:**
               - Giảm đau mạnh: Morphine, Fentanyl
               - Chống nôn
               - Làm mềm phân
            
            7. **Phòng ngừa biến chứng:**
               - DVT prophylaxis: Pneumatic compression (tránh heparin giai đoạn sớm)
               - Stress ulcer prophylaxis
               - Seizure prophylaxis (không routine, chỉ nếu có cơn động kinh)
            
            **Tiên lượng:** Tốt nếu xử lý phình mạch sớm và không có vasospasm.
            """)
        
        elif final_grade == 3:
            st.warning(f"""
            **🟠 HUNT & HESS GRADE 3** - Tiên lượng trung bình
            
            **Tỷ lệ tử vong:** 10-15%  
            **Tỷ lệ kết cục tốt:** 50-70%
            
            **Đặc điểm lâm sàng:**
            - Buồn ngủ, lú lẫn
            - Thiếu sót thần kinh khu trú nhẹ
            - Mức độ ý thức giảm nhẹ
            
            **Khuyến nghị xử trị:**
            
            1. **ICU chuyên sâu - Theo dõi sát:**
               - Neurological checks q1h
               - Cardiac monitoring, ICP monitoring nếu GCS <8
            
            2. **Bảo vệ đường thở:**
               - Đánh giá khả năng bảo vệ đường thở
               - Cân nhắc **đặt nội khí quản** nếu:
                 * GCS <8
                 * Giảm ý thức tiến triển
                 * Nguy cơ sặc
            
            3. **Hội chẩn đa chuyên khoa KHẨN CẤP:**
               - Neurology + Neurosurgery + Interventional Radiology + ICU
               - Quyết định thời điểm xử lý phình mạch
            
            4. **Thời điểm xử lý phình mạch:**
               - **Nếu tình trạng ổn định:** Xử lý trong 24h
               - **Nếu tiến triển xấu:** Cân nhắc trì hoãn đến khi ổn định
               - **Coiling** ưu tiên (ít xâm lấn hơn clipping)
            
            5. **Kiểm soát huyết áp:**
               - SBP <160 mmHg (trước xử lý phình mạch)
               - Cân bằng giữa giảm nguy cơ tái xuất huyết và duy trì tưới máu não
            
            6. **Phòng ngừa và điều trị vasospasm:**
               - **Nimodipine 60mg q4h** (qua ống ng nếu không nuốt được)
               - TCD hàng ngày
               - Nếu có vasospasm:
                 * **3H therapy**
                 * Cân nhắc **angioplasty** nội mạch nếu không đáp ứng
            
            7. **Kiểm soát áp lực nội sọ:**
               - Nâng đầu giường 30°
               - Cân nhắc ICP monitor
               - Thẩm thấu liệu nếu có tăng ICP
            
            8. **Dự phòng biến chứng:**
               - DVT prophylaxis
               - Stress ulcer prophylaxis
               - Nutrition: Enteral feeding qua ống ng
            
            **Tiên lượng:** Trung bình. Phụ thuộc vào khả năng xử lý vasospasm và biến chứng.
            """)
        
        elif final_grade == 4:
            st.error(f"""
            **🔴 HUNT & HESS GRADE 4** - Tiên lượng xấu
            
            **Tỷ lệ tử vong:** 60-70%  
            **Tỷ lệ kết cục tốt:** 10-30%
            
            **Đặc điểm lâm sàng:**
            - Hôn mê (GCS 6-8)
            - Liệt nửa người vừa đến nặng
            - Cứng co tư thế sớm
            
            **Khuyến nghị xử trí:**
            
            1. **KHẨN CẤP - ICU hồi sức chuyên sâu:**
               - Monitoring liên tục
               - **ICP monitor** (cân nhắc mạnh)
            
            2. **Bảo vệ đường thở - Đặt nội khí quản:**
               - **Rapid sequence intubation**
               - Mechanical ventilation
               - Mục tiêu: PaCO2 35-40 mmHg (tránh hyperventilation quá mức)
            
            3. **Kiểm soát áp lực nội sọ:**
               - Đặt **ICP monitor/EVD (External Ventricular Drain)**
               - Mục tiêu: ICP <20 mmHg, CPP 60-70 mmHg
               - Điều trị:
                 * Nâng đầu 30°
                 * Sedation (propofol, midazolam)
                 * Thẩm thấu liệu: Mannitol hoặc Hypertonic saline
                 * Cân nhắc **decompressive craniectomy** nếu ICP không kiểm soát được
            
            4. **Thời điểm xử lý phình mạch:**
               - **TRANH CÃI:** Có ý kiến trì hoãn đến khi ổn định
               - **Xu hướng hiện nay:** Xử lý sớm (24-72h) nếu tình trạng cho phép
               - Hội chẩn đa chuyên khoa để quyết định
               - **Coiling** ưu tiên (ít stress hơn surgery)
            
            5. **Thảo luận với gia đình về tiên lượng:**
               - Tỷ lệ tử vong cao (60-70%)
               - Ngay cả sống sót, khả năng phục hồi chức năng hạn chế
               - Thảo luận **goals of care** sớm
            
            6. **Điều trị hỗ trợ tích cực:**
               - Kiểm soát huyết áp
               - Nimodipine (qua ống ng)
               - Dự phòng vasospasm
               - DVT prophylaxis
               - Stress ulcer prophylaxis
               - Nutrition
               - Kiểm soát đường huyết, nhiệt độ
            
            7. **Theo dõi vasospasm:**
               - TCD hàng ngày (nếu làm được)
               - CT perfusion nếu nghi vasospasm
               - 3H therapy nếu có vasospasm
            
            **Tiên lượng:** Xấu. Tỷ lệ tử vong cao và khả năng phục hồi chức năng kém.
            """)
        
        else:  # Grade 5
            st.error(f"""
            **🔴 HUNT & HESS GRADE 5** - Tiên lượng rất xấu
            
            **Tỷ lệ tử vong:** 70-90%  
            **Tỷ lệ kết cục tốt:** <5%
            
            **Đặc điểm lâm sàng:**
            - Hôn mê sâu (GCS 3-5)
            - Cứng co tư thế
            - Tình trạng hấp hối
            
            **Khuyến nghị xử trí:**
            
            1. **Thảo luận NGHIÊM TÚC với gia đình:**
               - **Tiên lượng cực kỳ xấu:** Tỷ lệ tử vong 70-90%
               - Ngay cả sống sót, hầu như không phục hồi chức năng (vegetative state)
               - **Thảo luận goals of care:**
                 * Full code vs DNR/DNI
                 * Comfort care measures
                 * End-of-life care planning
            
            2. **Nếu gia đình chọn điều trị tích cực:**
               - ICU hồi sức chuyên sâu
               - Đặt nội khí quản, thở máy
               - ICP monitor/EVD
               - Kiểm soát ICP tích cực
               - Sedation, analgesia
            
            3. **Xử lý phình mạch:**
               - **TRANH CÃI LỚN:** Nhiều trung tâm không xử lý ở grade 5
               - Tỷ lệ thành công rất thấp
               - Nếu làm: **Coiling** (ít xâm lấn hơn)
               - Cân nhắc lợi ích/nguy cơ cẩn thận
            
            4. **Hoặc Chăm sóc giảm nhẹ (Palliative Care):**
               - **Comfort measures only**
               - Pain management
               - Symptom control
               - Spiritual support
               - Family support
               - End-of-life care
            
            5. **Cân nhắc hiến tạng:**
               - Nếu phù hợp và gia đình đồng ý
               - Tham vấn Organ Procurement Organization
            
            **Khuyến nghị:** Trong hầu hết trường hợp Grade 5, **Palliative Care/Comfort Care** 
            là lựa chọn hợp lý hơn điều trị tích cực.
            
            **Tôn trọng:** Ý muốn của bệnh nhân (advance directive nếu có) và quyết định của gia đình.
            """)
        
        # Additional important notes
        st.markdown("---")
        st.info(f"""
        **📌 LƯU Ý QUAN TRỌNG VỀ XUẤT HUYẾT DƯỚI NHỆN:**
        
        **1. Vasospasm - Biến chứng nghiêm trọng nhất:**
        - Xảy ra ở ~70% bệnh nhân SAH
        - Thời gian: Ngày 3-14 sau SAH (đỉnh ngày 7-10)
        - Nguyên nhân chính gây thiếu máu não muộn
        - **Phòng ngừa bắt buộc:** Nimodipine 60mg q4h × 21 ngày
        - **Điều trị:** 3H therapy (Hypertension, Hypervolemia, Hemodilution)
        
        **2. Tái xuất huyết - Nguy hiểm nhất:**
        - Nguy cơ cao nhất trong 24h đầu (~4%)
        - Tỷ lệ tử vong nếu tái xuất huyết: 70-80%
        - **Phòng ngừa:** Xử lý phình mạch SỚM (<24-72h)
        
        **3. Hydrocephalus:**
        - Cấp tính: Ngay sau SAH (cần EVD)
        - Muộn: Sau vài tuần (có thể cần VP shunt)
        
        **4. Các biến chứng khác:**
        - Động kinh (10-26%)
        - Rối loạn điện giải (hyponatremia từ SIADH hoặc CSW)
        - Suy tim do stress (Takotsubo cardiomyopathy)
        - Phù phổi thần kinh
        
        **5. Về Hunt & Hess Scale:**
        - Scale cổ điển, đã dùng từ 1968
        - Hạn chế: Chủ quan, phụ thuộc người đánh giá
        - Có thể dùng thêm: **World Federation of Neurological Surgeons (WFNS) Scale**, 
          **Fisher Scale** (dựa vào CT scan)
        """)
        
        # Comparison table
        with st.expander("📊 So Sánh Hunt & Hess Grades"):
            st.markdown("""
            | Grade | Triệu Chứng Chính | GCS | Tử Vong | Tiên Lượng |
            |-------|-------------------|-----|---------|------------|
            | **1** | Không triệu chứng/Đau đầu nhẹ | 15 | 0-5% | 🟢 Rất tốt |
            | **2** | Đau đầu nặng, cứng gáy | 14-15 | 5-10% | 🟢 Tốt |
            | **3** | Buồn ngủ, lú lẫn | 13-14 | 10-15% | 🟠 Trung bình |
            | **4** | Hôn mê, liệt nửa người | 6-8 | 60-70% | 🔴 Xấu |
            | **5** | Hôn mê sâu, hấp hối | 3-5 | 70-90% | 🔴 Rất xấu |
            """)
        
        # References
        with st.expander("📚 Tài Liệu Tham Khảo"):
            st.markdown("""
            **Primary Reference:**
            - Hunt WE, Hess RM. *Surgical risk as related to time of intervention in the repair of intracranial aneurysms.* 
              J Neurosurg. 1968 Jan;28(1):14-20. [PMID: 5635959]
            
            **Validation and Comparison Studies:**
            - Rosen DS, Macdonald RL. *Subarachnoid hemorrhage grading scales: a systematic review.* 
              Neurocrit Care. 2005;2(2):110-8.
            
            - Report of World Federation of Neurological Surgeons Committee on a Universal Subarachnoid Hemorrhage Grading Scale. 
              *J Neurosurg. 1988;68(6):985-6.*
            
            **Guidelines:**
            - Connolly ES Jr, et al. *Guidelines for the management of aneurysmal subarachnoid hemorrhage.* 
              Stroke. 2012;43(6):1711-37.
            
            - Steiner T, et al. *European Stroke Organization guidelines for the management of intracranial aneurysms and subarachnoid haemorrhage.* 
              Cerebrovasc Dis. 2013;35(2):93-112.
            
            - Diringer MN, et al. *Critical care management of patients following aneurysmal subarachnoid hemorrhage.* 
              Neurocrit Care. 2011;15(2):211-40.
            """)
    
    # Educational content
    st.markdown("---")
    st.markdown("### 📖 THÔNG TIN THÊM")
    
    with st.expander("❓ Xuất Huyết Dưới Nhện (SAH) là gì?"):
        st.markdown("""
        **Xuất huyết dưới màng nhện (Subarachnoid Hemorrhage - SAH)** là tình trạng 
        xuất huyết vào khoang dưới màng nhện (giữa màng nhện và màng mềm não).
        
        **Nguyên nhân chính:**
        1. **Vỡ phình mạch não** (~85%) - Nguyên nhân phổ biến nhất
        2. **Chấn thương** (~15%)
        3. Dị dạng mạch máu (AVM)
        4. Rối loạn đông máu
        
        **Triệu chứng điển hình:**
        - **"Thunderclap headache"** - Đau đầu dữ dội đột ngột (như bị đập vào đầu)
        - Cứng gáy
        - Buồn nôn, nôn
        - Sợ ánh sáng (photophobia)
        - Có thể mất ý thức
        
        **Chẩn đoán:**
        - **CT scan não** (độ nhạy ~95% trong 6h đầu)
        - **Chọc dò tủy sống** nếu CT âm tính nhưng nghi ngờ cao
        - **CTA hoặc DSA** để tìm phình mạch
        
        **Tỷ lệ mắc:** ~10/100,000 người/năm
        **Tuổi hay gặp:** 50-60 tuổi
        **Tỷ lệ tử vong tổng thể:** ~50%
        """)
    
    with st.expander("🆚 Hunt & Hess vs WFNS Scale"):
        st.markdown("""
        Có hai thang điểm chính để phân loại SAH:
        
        **1. Hunt & Hess Scale (1968):**
        - Dựa vào triệu chứng lâm sàng
        - Chủ quan hơn
        - Đã được sử dụng rộng rãi trong nhiều thập kỷ
        
        **2. WFNS Scale (World Federation of Neurological Surgeons - 1988):**
        - Dựa vào GCS và thiếu sót vận động
        - Khách quan hơn
        - Ít phụ thuộc người đánh giá
        
        | WFNS Grade | GCS | Motor Deficit | ~ Hunt & Hess |
        |------------|-----|---------------|---------------|
        | I | 15 | Absent | Grade 1-2 |
        | II | 13-14 | Absent | Grade 2 |
        | III | 13-14 | Present | Grade 3 |
        | IV | 7-12 | Present/Absent | Grade 4 |
        | V | 3-6 | Present/Absent | Grade 5 |
        
        **3. Fisher Scale:**
        - Dựa vào lượng máu trên CT scan
        - Dự đoán nguy cơ vasospasm
        
        **Khuyến nghị:** Sử dụng cả Hunt & Hess và WFNS để đánh giá toàn diện.
        """)
    
    with st.expander("⚠️ Khi Nào Nghi Ngờ SAH?"):
        st.markdown("""
        **LUÔN nghi ngờ SAH khi bệnh nhân có:**
        
        1. **"Thunderclap headache"** - Đau đầu dữ dội đột ngột
           - Đau đến mức "tồi tệ nhất trong đời"
           - Đau đột ngột, đạt cực độ trong vài giây đến phút
        
        2. **Đau đầu + Cứng gáy**
        
        3. **Đau đầu + Giảm ý thức**
        
        4. **Đau đầu + Động kinh lần đầu**
        
        5. **Đau đầu + Thiếu sót thần kinh khu trú**
           - Đặc biệt: Liệt CN III (suy đo phình mạch động mạch thông sau)
        
        **CẤM:** Không bỏ qua chẩn đoán SAH!
        - Tỷ lệ chẩn đoán nhầm: 12-25%
        - Nếu bỏ sót → Tái xuất huyết → Tử vong rất cao
        
        **Xử trí ban đầu:**
        1. **CT scan não NGAY** (trong 6h nếu có thể)
        2. Nếu CT âm tính nhưng nghi ngờ cao: **Chọc dò tủy sống**
        3. Nếu xác định SAH: **CTA hoặc DSA** để tìm phình mạch
        4. Nhập viện ICU/Stroke Unit ngay
        """)
    
    # Footer
    st.markdown("---")
    st.caption("📚 Based on: Hunt WE, Hess RM. J Neurosurg. 1968;28(1):14-20")
    st.caption("⚠️ For aneurysmal subarachnoid hemorrhage only (not traumatic SAH)")
    st.caption("🏥 Combine with WFNS Scale and Fisher Scale for complete assessment")

