"""
Acute Spinal Cord Injury Protocol
AANS/CNS 2013, NICE 2016
Management of acute spinal cord injury
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Acute Spinal Cord Injury Protocol"""
    st.subheader("🧠 Acute Spinal Cord Injury")
    st.caption("AANS/CNS 2013, NICE 2016 - Management of acute spinal cord injury")
    
    st.error("""
    **🚨 ACUTE SPINAL CORD INJURY = URGENT ASSESSMENT REQUIRED**
    
    **Triệu chứng:**
    - Yếu hoặc liệt tay/chân
    - Mất cảm giác dưới mức tổn thương
    - Rối loạn chức năng bàng quang/ruột
    - Khó thở (nếu tổn thương cao)
    - Hạ huyết áp, nhịp chậm (neurogenic shock)
    
    **Cần xử trí ngay - Mỗi phút đều quý giá!**
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: INITIAL MANAGEMENT ==========
    st.markdown("### ⚡ Xử Trí Ban Đầu")
    
    with st.expander("🔄 Xem quy trình xử trí ban đầu", expanded=True):
        st.markdown("""
        **1. ABC (Airway, Breathing, Circulation):**
        - **Airway:** Đảm bảo thông thoáng, cẩn thận với cột sống cổ
        - **Breathing:** Đánh giá chức năng hô hấp (đặc biệt tổn thương cao)
        - **Circulation:** Đánh giá neurogenic shock
        
        **2. Immobilization:**
        - **Cervical collar:** Cổ cứng
        - **Backboard:** Nằm trên ván cứng
        - **Log roll:** Xoay người như khúc gỗ
        - **Không di chuyển:** Tránh di chuyển không cần thiết
        
        **3. Neurological Assessment:**
        - **ASIA Impairment Scale (AIS):**
          - A: Complete (không có chức năng dưới mức tổn thương)
          - B: Sensory incomplete (có cảm giác, không vận động)
          - C: Motor incomplete (vận động yếu)
          - D: Motor incomplete (vận động gần bình thường)
          - E: Normal
        - **Motor score:** 0-5 cho mỗi nhóm cơ
        - **Sensory score:** 0-2 cho mỗi dermatome
        
        **4. Imaging:**
        - **CT spine:** Ưu tiên (nhanh, chính xác)
        - **MRI:** Đánh giá tổn thương tủy, dây chằng
        - **X-ray:** Nếu không có CT
        """)
    
    st.markdown("---")
    
    # ========== SECTION 2: NEUROGENIC SHOCK ==========
    st.markdown("### ⚡ Neurogenic Shock")
    
    with st.expander("💔 Xem quy trình xử trí neurogenic shock", expanded=False):
        st.markdown("""
        **Đặc điểm:**
        - Hạ huyết áp (SBP < 90 mmHg)
        - Nhịp chậm (HR < 60 bpm)
        - Tổn thương tủy trên T6
        - Mất tone giao cảm
        
        **Quy trình:**
        
        1. **Fluid Resuscitation:**
           - 500-1000 mL NS trong 10-15 phút
           - Theo dõi sát đáp ứng
           - Tránh quá tải dịch
        
        2. **Vasopressors:**
           - **Norepinephrine:** 0.05-0.5 mcg/kg/min
           - **Phenylephrine:** 0.1-0.5 mcg/kg/min
           - **Mục tiêu:** MAP ≥ 85-90 mmHg (cao hơn bình thường)
        
        3. **Atropine:**
           - **Liều:** 0.5-1 mg IV
           - **Chỉ định:** Nhịp chậm nặng (< 40 bpm)
        
        4. **Theo dõi:**
           - MAP ≥ 85-90 mmHg (quan trọng cho tưới máu tủy)
           - HR, CVP
           - Lượng nước tiểu
        """)
    
    st.markdown("---")
    
    # ========== SECTION 3: HIGH-DOSE METHYLPREDNISOLONE ==========
    st.markdown("### 💉 High-Dose Methylprednisolone")
    
    with st.expander("⚠️ Xem chỉ định và liều methylprednisolone", expanded=False):
        st.markdown("""
        **⚠️ CONTROVERSIAL - Cần thảo luận với chuyên khoa**
        
        **Chỉ định:**
        - Tổn thương tủy không hoàn toàn (AIS B, C, D)
        - Bắt đầu trong vòng 8 giờ sau chấn thương
        - Không có chống chỉ định
        
        **Liều (NASCIS II Protocol):**
        - **Bolus:** 30 mg/kg IV trong 15 phút
        - **Infusion:** 5.4 mg/kg/h x 23 giờ
        - **Tổng liều:** ~5.4 g trong 24 giờ
        
        **Chống chỉ định:**
        - Tổn thương hoàn toàn (AIS A)
        - > 8 giờ sau chấn thương
        - Chấn thương sọ não nặng
        - Nhiễm trùng nặng
        - Chảy máu nặng
        - Phụ nữ có thai
        
        **Biến chứng:**
        - Nhiễm trùng (pneumonia, UTI)
        - Chảy máu đường tiêu hóa
        - Tăng đường huyết
        - Loãng xương
        
        **Lưu ý:**
        - Hiệu quả còn tranh cãi
        - Nhiều guidelines không khuyến nghị
        - Cần thảo luận với chuyên khoa
        """)
    
    st.markdown("---")
    
    # ========== SECTION 4: RESPIRATORY MANAGEMENT ==========
    st.markdown("### 🫁 Respiratory Management")
    
    st.markdown("""
    **Tổn thương cao (C1-C4):**
    - Liệt cơ hô hấp hoàn toàn
    - Cần intubation ngay
    - Ventilator support lâu dài
    
    **Tổn thương trung bình (C5-C8):**
    - Yếu cơ hô hấp
    - Có thể cần NIV hoặc intubation
    - Theo dõi sát
    
    **Tổn thương thấp (T1-T12):**
    - Chức năng hô hấp thường bình thường
    - Có thể yếu cơ bụng (ảnh hưởng ho)
    
    **Quy trình:**
    - Đánh giá chức năng hô hấp sát
    - Cân nhắc intubation sớm nếu tổn thương cao
    - Chest physiotherapy
    - Phòng ngừa pneumonia
    """)
    
    st.markdown("---")
    
    # ========== SECTION 5: SURGICAL MANAGEMENT ==========
    st.markdown("### 🔪 Surgical Management")
    
    with st.expander("🏥 Xem chỉ định phẫu thuật", expanded=False):
        st.markdown("""
        **Chỉ định:**
        - **Cervical spine:**
          - Dislocation không giảm được
          - Compression tủy
          - Instability
          - Progressive neurological deficit
        - **Thoracic/Lumbar spine:**
          - Compression tủy
          - Instability
          - Progressive neurological deficit
        
        **Timing:**
        - **Early (< 24h):** Nếu có progressive deficit
        - **Delayed (24-72h):** Nếu ổn định
        
        **Procedures:**
        - **Decompression:** Laminectomy, corpectomy
        - **Stabilization:** Fusion, instrumentation
        - **Reduction:** Closed hoặc open
        """)
    
    st.markdown("---")
    
    # ========== SECTION 6: COMPLICATIONS ==========
    st.markdown("### ⚠️ Complications")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Sớm (< 48h):**
        - **Neurogenic shock:** Hạ huyết áp, nhịp chậm
        - **Respiratory failure:** Đặc biệt tổn thương cao
        - **Autonomic dysreflexia:** Tăng huyết áp đột ngột
        - **Bradycardia:** Do mất tone giao cảm
        - **Hypothermia:** Do mất điều hòa nhiệt độ
        
        **Trung bình (48h - 2 tuần):**
        - **Pneumonia:** Do liệt cơ hô hấp
        - **UTI:** Do rối loạn bàng quang
        - **Pressure ulcers:** Do bất động
        - **DVT/PE:** Do bất động
        """)
    
    with col2:
        st.markdown("""
        **Muộn (> 2 tuần):**
        - **Spasticity:** Tăng trương lực cơ
        - **Contractures:** Co cứng khớp
        - **Heterotopic ossification:** Xương hóa trong mô mềm
        - **Syringomyelia:** Nang trong tủy
        - **Chronic pain:** Đau mạn tính
        
        **Phòng ngừa:**
        - **DVT prophylaxis:** Heparin/LMWH
        - **Pressure relief:** Xoay trở thường xuyên
        - **Bladder care:** Catheter, intermittent
        - **Bowel care:** Laxatives, enemas
        """)
    
    st.markdown("---")
    
    # ========== SECTION 7: AUTONOMIC DYSREFLEXIA ==========
    st.markdown("### ⚡ Autonomic Dysreflexia")
    
    with st.expander("🚨 Xem quy trình xử trí autonomic dysreflexia", expanded=False):
        st.markdown("""
        **Đặc điểm:**
        - Tăng huyết áp đột ngột (SBP > 150 mmHg)
        - Nhức đầu, đỏ mặt
        - Đổ mồ hôi trên mức tổn thương
        - Tổn thương tủy trên T6
        
        **Nguyên nhân:**
        - Bàng quang đầy (phổ biến nhất)
        - Ruột đầy
        - Nhiễm trùng
        - Loét ép
        - Nhiệt độ thay đổi
        
        **Quy trình:**
        
        1. **Ngồi dậy:** Giảm huyết áp
        2. **Tìm nguyên nhân:**
           - Kiểm tra catheter
           - Kiểm tra ruột
           - Kiểm tra da
        3. **Điều trị nguyên nhân:**
           - Làm rỗng bàng quang
           - Làm rỗng ruột
           - Điều trị nhiễm trùng
        4. **Nếu huyết áp vẫn cao:**
           - **Nifedipine:** 10 mg SL
           - **Nitroglycerin:** 0.4 mg SL
           - **Labetalol:** 10-20 mg IV
        """)
    
    st.markdown("---")
    
    # ========== SECTION 8: SPECIAL POPULATIONS ==========
    st.markdown("### 👥 Special Populations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Trẻ em:**
        - Tổn thương cột sống cổ cao hơn
        - SCIWORA (Spinal Cord Injury Without Radiographic Abnormality)
        - Cần MRI nếu nghi ngờ
        - Liều thuốc dựa trên cân nặng
        
        **Người cao tuổi:**
        - Tỷ lệ biến chứng cao hơn
        - Phục hồi chậm hơn
        - Cần cân nhắc chất lượng cuộc sống
        """)
    
    with col2:
        st.markdown("""
        **Phụ nữ có thai:**
        - Tránh methylprednisolone
        - Cẩn thận với imaging (bảo vệ thai)
        - Cần tư vấn sản khoa
        
        **Bệnh nhân có bệnh nền:**
        - Điều chỉnh liều thuốc
        - Cẩn thận với biến chứng
        - Tư vấn chuyên khoa
        """)
    
    st.markdown("---")
    
    # ========== SECTION 9: REFERENCES ==========
    render_references_section(get_references("spinal_cord_injury"))
    
    st.markdown("---")
    
    # Footer
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")


