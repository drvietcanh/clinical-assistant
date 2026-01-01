"""
Duke Criteria for Infective Endocarditis
Tiêu chuẩn chẩn đoán viêm nội tâm mạc nhiễm khuẩn
"""

import streamlit as st
from config.theme import COLORS
from components.ui.scoring import render_score_result
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section
# ======================================


def render():
    """Render Duke Criteria interface"""
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    shared_inputs = {}
    if shared and shared.get("calculator_id") == "duke":
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared.get('calculator_name', 'Duke Criteria')}")
        shared_inputs = shared.get("inputs", {})
    
    st.markdown(f"""
    <h3 style='text-align: center; color: {COLORS['success']};'>❤️ Duke Criteria</h3>
    <p style='text-align: center;'><em>Chẩn đoán Viêm Nội Tâm Mạc Nhiễm Khuẩn (IE)</em></p>
    """, unsafe_allow_html=True)
    
    render_suggestions(
        calculator_id="duke",
        calculator_name="Duke Criteria",
        category="Tim Mạch",
        show_related=True,
        show_category=True,
        limit=3
    )
    
    with st.expander("ℹ️ Giới thiệu về Duke Criteria"):
        st.markdown("""
        **Duke Criteria** là tiêu chuẩn chẩn đoán **Viêm nội tâm mạc nhiễm khuẩn (Infective Endocarditis - IE)**.
        
        **2 loại tiêu chí:**
        - **Major (chính):** Bằng chứng mạnh về IE
        - **Minor (phụ):** Bằng chứng hỗ trợ
        
        **Kết luận:**
        - **Definite IE:** 2 major HOẶC 1 major + 3 minor HOẶC 5 minor
        - **Possible IE:** 1 major + 1 minor HOẶC 3 minor
        - **Rejected:** Không đủ tiêu chí
        """)
    
    st.markdown("---")
    
    st.subheader("📝 Đánh giá bệnh nhân")
    
    major_count = 0
    minor_count = 0
    major_list = []
    minor_list = []
    
    # MAJOR CRITERIA
    st.markdown("## 🔴 MAJOR CRITERIA")
    
    st.markdown("### 1️⃣ Cấy máu dương tính:")
    
    blood_typical = st.checkbox(
        "Vi khuẩn ĐIỂN HÌNH cho IE trong ≥2 lần cấy máu riêng biệt: Streptococcus viridans, S. gallolyticus (bovis), HACEK, S. aureus, Enterococcus (không có ổ nhiễm khác)",
        value=shared_inputs.get("blood_typical", False)
    )
    
    blood_persistent = st.checkbox(
        "Vi khuẩn phù hợp IE trong cấy máu LIÊN TỤC: ≥2 lần cấy (+) cách ≥12h, HOẶC 3/3 hoặc >4/4 lần cấy (+) (cách ≥1h)",
        value=shared_inputs.get("blood_persistent", False)
    )
    
    coxiella = st.checkbox(
        "Coxiella burnetii: 1 lần cấy máu (+) HOẶC IgG anti-phase I > 1:800",
        value=shared_inputs.get("coxiella", False)
    )
    
    if blood_typical:
        major_count += 1
        major_list.append("Cấy máu: Vi khuẩn điển hình IE")
    if blood_persistent:
        major_count += 1
        major_list.append("Cấy máu: Dương tính liên tục")
    if coxiella:
        major_count += 1
        major_list.append("Coxiella burnetii (+)")
    
    st.markdown("---")
    
    st.markdown("### 2️⃣ Bằng chứng tổn thương nội tâm mạc (Echo):")
    
    vegetation = st.checkbox(
        "Mảng sùi (vegetation) trên van tim, dây chằng, hoặc vật liệu cấy ghép",
        value=shared_inputs.get("vegetation", False)
    )
    
    abscess = st.checkbox(
        "Áp xe quanh van",
        value=shared_inputs.get("abscess", False)
    )
    
    new_dehiscence = st.checkbox(
        "Suy van MỚI hoặc bong van nhân tạo",
        value=shared_inputs.get("new_dehiscence", False)
    )
    
    if vegetation:
        major_count += 1
        major_list.append("Echo: Mảng sùi")
    if abscess:
        major_count += 1
        major_list.append("Echo: Áp xe quanh van")
    if new_dehiscence:
        major_count += 1
        major_list.append("Echo: Suy van mới/bong van")
    
    st.markdown("---")
    
    # MINOR CRITERIA
    st.markdown("## 🟡 MINOR CRITERIA")
    
    predisposing = st.checkbox(
        "Yếu tố nguy cơ: Bệnh van tim từ trước HOẶC tiêm chích ma túy",
        value=shared_inputs.get("predisposing", False)
    )
    if predisposing:
        minor_count += 1
        minor_list.append("Yếu tố nguy cơ")
    
    fever = st.checkbox(
        "Sốt ≥ 38°C",
        value=shared_inputs.get("fever", False)
    )
    if fever:
        minor_count += 1
        minor_list.append("Sốt ≥38°C")
    
    st.markdown("**Hiện tượng mạch máu:**")
    vascular = st.multiselect(
        "",
        options=[
            "Tắc mạch động mạch lớn",
            "Nhồi máu phổi nhiễm trùng",
            "Phình mạch nhiễm trùng",
            "Xuất huyết nội sọ",
            "Xuất huyết kết mạc",
            "Janeway lesions (nốt đỏ không đau ở lòng bàn tay/chân)"
        ],
        default=shared_inputs.get("vascular", [])
    )
    if len(vascular) > 0:
        minor_count += 1
        minor_list.append(f"Hiện tượng mạch máu: {', '.join(vascular)}")
    
    st.markdown("**Hiện tượng miễn dịch:**")
    immunologic = st.multiselect(
        "",
        options=[
            "Osler nodes (nốt đau ở đầu ngón tay)",
            "Roth spots (xuất huyết võng mạc)",
            "Rheumatoid factor (+)",
            "Viêm cầu thận"
        ],
        default=shared_inputs.get("immunologic", [])
    )
    if len(immunologic) > 0:
        minor_count += 1
        minor_list.append(f"Hiện tượng miễn dịch: {', '.join(immunologic)}")
    
    micro_evidence = st.checkbox(
        "Bằng chứng vi sinh KHÔNG đủ major: Cấy máu (+) nhưng không đủ tiêu chí major, HOẶC huyết thanh học gợi ý nhiễm khuẩn phù hợp IE",
        value=shared_inputs.get("micro_evidence", False)
    )
    if micro_evidence:
        minor_count += 1
        minor_list.append("Bằng chứng vi sinh (không đủ major)")
    
    st.markdown("---")
    
    if st.button("📊 Đánh giá Duke Criteria", type="primary", use_container_width=True):
        # Diagnosis
        if (major_count >= 2) or (major_count >= 1 and minor_count >= 3) or (minor_count >= 5):
            diagnosis = "DEFINITE IE"
            color = COLORS["error"]
            icon = "🚨"
            recommendation = "Chẩn đoán XÁC ĐỊNH viêm nội tâm mạc nhiễm khuẩn"
        elif (major_count >= 1 and minor_count >= 1) or (minor_count >= 3):
            diagnosis = "POSSIBLE IE"
            color = COLORS["warning"]
            icon = "⚠️"
            recommendation = "NGHI NGỜ viêm nội tâm mạc - Cần theo dõi, xét nghiệm thêm"
        else:
            diagnosis = "REJECTED"
            color = COLORS["success"]
            icon = "✅"
            recommendation = "Không đủ tiêu chí chẩn đoán IE"
        
        st.markdown("## 📊 Kết quả")
        
        st.markdown(f"""
        render_score_result(
            title="Duke Criteria Results",
            score=diagnosis,
            interpretation=recommendation,
            mortality=None,
            color=color,
            icon=icon,
            size="large"
        )
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Major Criteria", f"{major_count}")
        with col2:
            st.metric("Minor Criteria", f"{minor_count}")
        
        if major_list:
            st.markdown("### 🔴 Major Criteria:")
            for item in major_list:
                st.markdown(f"- {item}")
        
        if minor_list:
            st.markdown("### 🟡 Minor Criteria:")
            for item in minor_list:
                st.markdown(f"- {item}")
        
        st.markdown("---")
        
        if diagnosis == "DEFINITE IE":
            st.error("""
            **🚨 XÁC ĐỊNH VIÊM NỘI TÂM MẠC NHIỄM KHUẨN**
            
            **Điều trị KHẨN:**
            
            1️⃣ **Nhập viện ngay - Hội chẩn tim mạch + nhiễm khuẩn:**
            
            2️⃣ **Kháng sinh NGAY (TRƯỚC khi có kết quả cấy):**
            
            **Nếu van tự nhiên:**
            - **Vancomycin** 15 mg/kg IV q12h +
            - **Gentamicin** 1 mg/kg IV q8h +
            - **Ceftriaxone** 2g IV q24h
            
            **Nếu van nhân tạo:**
            - **Vancomycin** +
            - **Gentamicin** +
            - **Rifampin** 300 mg PO q8h
            
            **Điều chỉnh khi có kháng sinh đồ:**
            - **S. viridans:** Penicillin G hoặc Ceftriaxone + Gentamicin (2-6 tuần)
            - **S. aureus:** Nafcillin/Oxacillin (MSSA) hoặc Vancomycin (MRSA) + Gentamicin (4-6 tuần)
            - **Enterococcus:** Ampicillin + Gentamicin (4-6 tuần)
            
            3️⃣ **Cấy máu:**
            - 3 bộ cấy máu (từ 3 vị trí khác nhau, cách ≥10 phút)
            - TRƯỚC khi dùng kháng sinh nếu được
            - Lặp lại mỗi 24-48h cho đến khi âm tính
            
            4️⃣ **Echo:**
            - TEE (siêu âm qua thực quản) - nhạy hơn TTE
            - Lặp lại sau 7-10 ngày
            - Theo dõi kích thước vegetation, biến chứng
            
            5️⃣ **Theo dõi biến chứng:**
            - Suy tim (40-50%)
            - Tắc mạch (20-50%)
            - Áp xe quanh van
            - Block nhĩ thất (ECG hàng ngày)
            - Suy thận
            
            6️⃣ **Chỉ định phẫu thuật:**
            
            **KHẨN CẤP (trong 24h):**
            - Suy tim cấp khó kiểm soát
            - Nhiễm khuẩn không kiểm soát (Fungus, áp xe, sốt kéo dài)
            
            **URGENT (trong vài ngày):**
            - Vegetation > 10 mm + tắc mạch
            - Vegetation rất lớn (> 15 mm)
            - Suy van nặng
            - Áp xe, giả phình, fistula
            - Bong van nhân tạo
            
            **Thời gian điều trị:** 4-6 tuần kháng sinh IV
            """)
        
        elif diagnosis == "POSSIBLE IE":
            st.warning("""
            **⚠️ NGHI NGỜ IE - Cần đánh giá thêm**
            
            **Xử trí:**
            
            1️⃣ **Nhập viện theo dõi**
            
            2️⃣ **Cấy máu lặp lại:**
            - 3 bộ cấy máu mới
            - Cấy kéo dài (cho tổ chức chậm)
            - Xét nghiệm huyết thanh học (Bartonella, Coxiella, Brucella...)
            
            3️⃣ **TEE (siêu âm qua thực quản):**
            - Nhạy hơn TTE nhiều
            - Nếu TEE (-) + nghi ngờ cao → Lặp lại sau 7-10 ngày
            
            4️⃣ **Tìm yếu tố nguy cơ/ổ nhiễm:**
            - Khám răng (S. viridans)
            - Khám da (S. aureus)
            - Khám tiết niệu sinh dục (Enterococcus)
            - Vết tiêm chích (nếu IVDU)
            
            5️⃣ **Cân nhắc kháng sinh kinh nghiệm nếu:**
            - Lâm sàng nặng
            - Nguy cơ cao (van nhân tạo)
            - Có biến chứng
            
            **Tái đánh giá Duke Criteria sau khi có thêm kết quả**
            """)
        
        else:
            st.success("""
            **✅ Không đủ tiêu chí IE**
            
            **Nhưng vẫn cần:**
            - Tìm nguyên nhân khác gây sốt
            - Nếu lâm sàng vẫn nghi ngờ cao IE → TEE
            - Theo dõi, tái đánh giá
            
            **IE có thể bị bỏ sót nếu:**
            - Đã dùng kháng sinh trước
            - Vi khuẩn khó cấy (HACEK, Bartonella, Coxiella...)
            - Vegetation nhỏ
            - IE van bên phải (khó phát hiện)
            """)
        
        with st.expander("📊 Bảng Duke Criteria chi tiết"):
            st.markdown("""
            ### MAJOR CRITERIA (2 loại):
            
            **1. Cấy máu dương tính:**
            - Vi khuẩn điển hình IE (S. viridans, S. gallolyticus, HACEK, S. aureus, Enterococcus) trong ≥2 lần cấy riêng biệt
            - Vi khuẩn phù hợp IE trong cấy máu liên tục
            - Coxiella burnetii: 1 lần cấy (+) hoặc IgG anti-phase I > 1:800
            
            **2. Bằng chứng tổn thương nội tâm mạc (Echo):**
            - Vegetation
            - Áp xe
            - Bong van nhân tạo
            - Suy van mới
            
            ---
            
            ### MINOR CRITERIA:
            
            1. Yếu tố nguy cơ (bệnh van tim, IVDU)
            2. Sốt ≥ 38°C
            3. Hiện tượng mạch máu (tắc mạch, nhồi máu phổi, phình mạch nhiễm trùng, Janeway lesions...)
            4. Hiện tượng miễn dịch (Osler nodes, Roth spots, RF+, viêm cầu thận)
            5. Bằng chứng vi sinh (không đủ major)
            
            ---
            
            ### CHẨN ĐOÁN:
            
            **DEFINITE IE (Xác định):**
            - 2 major, HOẶC
            - 1 major + 3 minor, HOẶC
            - 5 minor
            
            **POSSIBLE IE (Nghi ngờ):**
            - 1 major + 1 minor, HOẶC
            - 3 minor
            
            **REJECTED (Loại trừ):**
            - Không đủ tiêu chí Possible
            """)
        
        with st.expander("📚 Tài liệu tham khảo"):
            st.markdown("""
            1. **Durack DT, Lukes AS, Bright DK.** New criteria for diagnosis of infective endocarditis: utilization of specific echocardiographic findings. Duke Endocarditis Service. 
               *Am J Med.* 1994;96(3):200-9.
            
            2. **Li JS, Sexton DJ, Mick N, et al.** Proposed modifications to the Duke criteria for the diagnosis of infective endocarditis. 
               *Clin Infect Dis.* 2000;30(4):633-8.
            
            3. **Habib G, Lancellotti P, Antunes MJ, et al.** 2015 ESC Guidelines for the management of infective endocarditis. 
               *Eur Heart J.* 2015;36(44):3075-3128.
            
            4. **Baddour LM, Wilson WR, Bayer AS, et al.** Infective Endocarditis in Adults: Diagnosis, Antimicrobial Therapy, and Management of Complications: A Scientific Statement for Healthcare Professionals From the American Heart Association. 
               *Circulation.* 2015;132(15):1435-86.
            """)
        
        # Phase 1: save history + share + history UI + references
        inputs_dict = {
            "Major criteria": major_list or ["Không tiêu chí"],
            "Minor criteria": minor_list or ["Không tiêu chí"],
            "Major count": major_count,
            "Minor count": minor_count
        }
        results_dict = {
            "Diagnosis": diagnosis,
            "Recommendation": recommendation
        }
        
        # Export section
        render_export_section(
                title="Duke Criteria",
                inputs=inputs_dict,
                results=results_dict
        ,
                calculator_name="Duke Criteria"
            )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="duke",
            calculator_name="Duke Criteria",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="duke",
            calculator_name="Duke Criteria",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        st.markdown("---")
        render_history_ui(calculator_id="duke", show_actions=True)
        
        references = get_references("DUKE")
        if references:
            render_references_section(
                references=references,
                title="📚 Tài liệu tham khảo",
                last_updated="2024-01-15",
                show_evidence_level=True,
                show_links=True
            )
    
    st.info("""
    💡 **Điểm quan trọng:**
    
    1. **Cấy máu TRƯỚC kháng sinh** (3 bộ, từ 3 vị trí, cách ≥10 phút)
    
    2. **TEE nhạy hơn TTE** rất nhiều - Làm TEE nếu nghi ngờ cao
    
    3. **Definite IE = 2 major HOẶC 1 major + 3 minor HOẶC 5 minor**
    
    4. **Điều trị 4-6 tuần** kháng sinh IV
    
    5. **Phẫu thuật 40-50% trường hợp** (suy tim, nhiễm khuẩn không kiểm soát...)
    """)


if __name__ == "__main__":
    render()

