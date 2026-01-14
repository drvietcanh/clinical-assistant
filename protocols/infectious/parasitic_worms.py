"""
Parasitic Worm Infections Protocol
WHO, CDC Guidelines
Common parasitic worm infections in Vietnam
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Parasitic Worm Infections Protocol"""
    st.subheader("🪱 Protocol Điều trị Nhiễm Ký sinh Trùng Giun Sán")
    st.caption("WHO, CDC Guidelines - Common Parasitic Worm Infections in Vietnam")
    
    st.info("""
    **Các bệnh ký sinh trùng giun sán phổ biến ở Việt Nam:**
    - Giun đũa (Ascaris lumbricoides)
    - Giun tóc (Trichuris trichiura)
    - Giun móc (Hookworm - Ancylostoma/Necator)
    - Giun lươn (Strongyloidiasis - Strongyloides stercoralis)
    - Sán lá gan (Liver fluke - Clonorchis/Opisthorchis)
    - Sán lá phổi (Paragonimiasis - Paragonimus)
    - Giun kim (Enterobius vermicularis)
    - Sán dây (Tapeworm - Taenia/Taeniasis)
    - Amip (Amoebiasis - Entamoeba histolytica)
    - Giardia (Giardiasis - Giardia lamblia)
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: TYPE SELECTION ==========
    st.markdown("### 🦠 Chọn Loại Nhiễm Ký sinh Trùng")
    
    infection_type = st.radio(
        "**Loại nhiễm ký sinh trùng:**",
        [
            "Giun đũa (Ascaris)",
            "Giun tóc (Trichuris)",
            "Giun móc (Hookworm)",
            "Giun lươn (Strongyloidiasis)",
            "Sán lá gan (Liver fluke)",
            "Sán lá phổi (Paragonimiasis)",
            "Giun kim (Enterobius)",
            "Sán dây (Tapeworm)",
            "Amip (Amoebiasis)",
            "Giardia (Giardiasis)",
            "Nhiễm phối hợp (Mixed infection)"
        ],
        key="parasite_type"
    )
    
    st.markdown("---")
    
    # Route to appropriate protocol
    if "Giun đũa" in infection_type or "Ascaris" in infection_type:
        render_ascariasis()
    elif "Giun tóc" in infection_type or "Trichuris" in infection_type:
        render_trichuriasis()
    elif "Giun móc" in infection_type or "Hookworm" in infection_type:
        render_hookworm()
    elif "Giun lươn" in infection_type or "Strongyloidiasis" in infection_type or "Strongyloides" in infection_type:
        render_strongyloidiasis()
    elif "Sán lá gan" in infection_type or "Liver fluke" in infection_type:
        render_liver_fluke()
    elif "Sán lá phổi" in infection_type or "Paragonimiasis" in infection_type or "Paragonimus" in infection_type:
        render_paragonimiasis()
    elif "Giun kim" in infection_type or "Enterobius" in infection_type:
        render_enterobiasis()
    elif "Sán dây" in infection_type or "Tapeworm" in infection_type:
        render_taeniasis()
    elif "Amip" in infection_type or "Amoebiasis" in infection_type or "Entamoeba" in infection_type:
        render_amoebiasis()
    elif "Giardia" in infection_type or "Giardiasis" in infection_type:
        render_giardiasis()
    else:
        render_mixed_infection()


def render_ascariasis():
    """Ascaris lumbricoides (Giun đũa) Protocol"""
    
    st.success("## 🪱 GIUN ĐŨA (Ascaris lumbricoides)")
    
    st.markdown("### 📋 Chẩn đoán")
    
    with st.expander("🔍 Tiêu chuẩn chẩn đoán", expanded=True):
        st.markdown("""
        **Triệu chứng:**
        - Thường không có triệu chứng (light infection)
        - Đau bụng, buồn nôn, nôn
        - Ho, khó thở (khi ấu trùng di chuyển qua phổi)
        - Tắc ruột (heavy infection)
        - Giun chui ống mật (biliary ascariasis)
        
        **Xét nghiệm:**
        - Soi phân tìm trứng giun (ova)
        - X-quang bụng: thấy giun trong ruột
        - Siêu âm: thấy giun trong đường mật
        """)
    
    st.markdown("---")
    
    # ========== TREATMENT ==========
    st.markdown("### 💊 Điều trị")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **Điều trị Không Biến chứng:**
        
        **Lựa chọn 1 (Ưu tiên):**
        - **Albendazole** 400mg PO x 1 liều
        - Hiệu quả: 95-100%
        - An toàn cho trẻ em >1 tuổi
        
        **Lựa chọn 2:**
        - **Mebendazole** 100mg PO BID x 3 ngày
        - Hoặc 500mg PO x 1 liều
        
        **Lựa chọn 3:**
        - **Pyrantel pamoate** 11mg/kg PO x 1 liều (tối đa 1g)
        - An toàn cho trẻ em >2 tuổi
        """)
    
    with col2:
        st.warning("""
        **Điều trị Có Biến chứng:**
        
        **Tắc ruột:**
        - Piperazine citrate 75mg/kg PO (tối đa 3.5g) x 1 liều
        - Hoặc Albendazole 400mg PO x 1 liều
        - Theo dõi sát, có thể cần phẫu thuật
        
        **Giun chui ống mật:**
        - Albendazole 400mg PO BID x 3 ngày
        - Hoặc Mebendazole 100mg PO BID x 3 ngày
        - Có thể cần nội soi mật tụy ngược dòng (ERCP)
        
        **Nhiễm phổi (Löffler syndrome):**
        - Điều trị triệu chứng (corticosteroid nếu cần)
        - Sau đó điều trị giun khi ấu trùng về ruột
        """)
    
    st.markdown("---")
    
    # ========== DOSING ==========
    st.markdown("### 💉 Liều Thuốc Chi tiết")
    
    import pandas as pd
    dosing_data = {
        "Thuốc": [
            "Albendazole",
            "Mebendazole",
            "Pyrantel pamoate",
            "Piperazine citrate"
        ],
        "Liều Người lớn": [
            "400mg PO x 1",
            "100mg PO BID x 3 ngày",
            "11mg/kg PO x 1 (max 1g)",
            "75mg/kg PO x 1 (max 3.5g)"
        ],
        "Liều Trẻ em": [
            "400mg PO x 1 (>1 tuổi)",
            "100mg PO BID x 3 ngày (>2 tuổi)",
            "11mg/kg PO x 1 (>2 tuổi)",
            "75mg/kg PO x 1"
        ],
        "Ghi chú": [
            "Không dùng khi có thai",
            "Không dùng khi có thai",
            "An toàn, ít tác dụng phụ",
            "Dùng khi tắc ruột"
        ]
    }
    
    st.dataframe(pd.DataFrame(dosing_data), use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # ========== MONITORING ==========
    st.markdown("### 📈 Theo dõi")
    
    st.markdown("""
    **Sau điều trị:**
    - Soi phân lại sau 2-3 tuần để đánh giá hiệu quả
    - Nếu vẫn còn trứng, điều trị lại sau 2-4 tuần
    
    **Dấu hiệu cảnh báo:**
    - Đau bụng dữ dội (tắc ruột)
    - Vàng da, đau hạ sườn phải (giun chui ống mật)
    - Sốt, viêm phúc mạc
    """)
    
    st.markdown("---")
    
    # ========== PREVENTION ==========
    st.markdown("### 🛡️ Phòng ngừa")
    
    st.info("""
    - Rửa tay trước khi ăn
    - Rửa sạch rau quả trước khi ăn
    - Nấu chín thức ăn
    - Điều trị định kỳ cho cộng đồng (mass deworming)
    - Cải thiện vệ sinh môi trường
    """)


def render_trichuriasis():
    """Trichuris trichiura (Giun tóc) Protocol"""
    
    st.success("## 🪱 GIUN TÓC (Trichuris trichiura)")
    
    st.markdown("### 📋 Chẩn đoán")
    
    with st.expander("🔍 Tiêu chuẩn chẩn đoán", expanded=True):
        st.markdown("""
        **Triệu chứng:**
        - Thường không có triệu chứng (light infection)
        - Đau bụng, tiêu chảy
        - Thiếu máu (heavy infection)
        - Trực tràng sa (rectal prolapse) ở trẻ em
        - Chậm phát triển ở trẻ em
        
        **Xét nghiệm:**
        - Soi phân tìm trứng giun (ova) - hình thoi, có nắp
        - Thiếu máu thiếu sắt (heavy infection)
        """)
    
    st.markdown("---")
    
    # ========== TREATMENT ==========
    st.markdown("### 💊 Điều trị")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **Điều trị Không Biến chứng:**
        
        **Lựa chọn 1 (Ưu tiên):**
        - **Albendazole** 400mg PO QD x 3 ngày
        - Hiệu quả: 70-90%
        
        **Lựa chọn 2:**
        - **Mebendazole** 100mg PO BID x 3 ngày
        - Hoặc 500mg PO x 1 liều
        
        **Lựa chọn 3:**
        - **Ivermectin** 200mcg/kg PO QD x 3 ngày
        """)
    
    with col2:
        st.warning("""
        **Điều trị Nhiễm Nặng:**
        
        **Heavy infection:**
        - Albendazole 400mg PO BID x 3 ngày
        - Hoặc Mebendazole 100mg PO BID x 5 ngày
        
        **Có thiếu máu:**
        - Bổ sung sắt
        - Điều trị giun trước, sau đó bổ sung sắt
        
        **Trực tràng sa:**
        - Điều trị giun
        - Phẫu thuật nếu cần
        """)
    
    st.markdown("---")
    
    # ========== DOSING ==========
    st.markdown("### 💉 Liều Thuốc Chi tiết")
    
    import pandas as pd
    dosing_data = {
        "Thuốc": [
            "Albendazole",
            "Mebendazole",
            "Ivermectin"
        ],
        "Liều Người lớn": [
            "400mg PO QD x 3 ngày",
            "100mg PO BID x 3 ngày",
            "200mcg/kg PO QD x 3 ngày"
        ],
        "Liều Trẻ em": [
            "400mg PO QD x 3 ngày (>1 tuổi)",
            "100mg PO BID x 3 ngày (>2 tuổi)",
            "200mcg/kg PO QD x 3 ngày (>15kg)"
        ],
        "Ghi chú": [
            "Cần điều trị 3 ngày",
            "Có thể dùng 1 liều 500mg",
            "Ít tác dụng phụ"
        ]
    }
    
    st.dataframe(pd.DataFrame(dosing_data), use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # ========== MONITORING ==========
    st.markdown("### 📈 Theo dõi")
    
    st.markdown("""
    **Sau điều trị:**
    - Soi phân lại sau 2-3 tuần
    - Đánh giá tình trạng thiếu máu
    - Theo dõi tăng trưởng ở trẻ em
    """)
    
    st.markdown("---")
    
    # ========== PREVENTION ==========
    st.markdown("### 🛡️ Phòng ngừa")
    
    st.info("""
    - Rửa tay trước khi ăn
    - Rửa sạch rau quả
    - Cải thiện vệ sinh môi trường
    - Điều trị định kỳ cho cộng đồng
    """)


def render_hookworm():
    """Hookworm (Giun móc) Protocol"""
    
    st.success("## 🪱 GIUN MÓC (Hookworm - Ancylostoma/Necator)")
    
    st.markdown("### 📋 Chẩn đoán")
    
    with st.expander("🔍 Tiêu chuẩn chẩn đoán", expanded=True):
        st.markdown("""
        **Triệu chứng:**
        - Ngứa, phát ban tại vị trí xâm nhập (ground itch)
        - Ho, khó thở (khi ấu trùng qua phổi)
        - Đau bụng, tiêu chảy
        - Thiếu máu thiếu sắt (đặc trưng)
        - Mệt mỏi, yếu sức
        - Chậm phát triển ở trẻ em
        
        **Xét nghiệm:**
        - Soi phân tìm trứng giun (ova)
        - Thiếu máu thiếu sắt
        - Eosinophilia
        """)
    
    st.markdown("---")
    
    # ========== TREATMENT ==========
    st.markdown("### 💊 Điều trị")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **Điều trị Không Biến chứng:**
        
        **Lựa chọn 1 (Ưu tiên):**
        - **Albendazole** 400mg PO x 1 liều
        - Hiệu quả: 70-95%
        - An toàn cho trẻ em >1 tuổi
        
        **Lựa chọn 2:**
        - **Mebendazole** 100mg PO BID x 3 ngày
        - Hoặc 500mg PO x 1 liều
        
        **Lựa chọn 3:**
        - **Pyrantel pamoate** 11mg/kg PO QD x 3 ngày (max 1g/ngày)
        """)
    
    with col2:
        st.warning("""
        **Điều trị Có Thiếu Máu:**
        
        **Thiếu máu nhẹ-trung bình:**
        - Điều trị giun trước
        - Sau đó bổ sung sắt: Ferrous sulfate 325mg PO BID-TID
        - Theo dõi Hb sau 2-4 tuần
        
        **Thiếu máu nặng (Hb <7g/dL):**
        - Truyền máu nếu cần
        - Bổ sung sắt
        - Điều trị giun sau khi ổn định
        
        **Nhiễm nặng:**
        - Albendazole 400mg PO BID x 3 ngày
        """)
    
    st.markdown("---")
    
    # ========== DOSING ==========
    st.markdown("### 💉 Liều Thuốc Chi tiết")
    
    import pandas as pd
    dosing_data = {
        "Thuốc": [
            "Albendazole",
            "Mebendazole",
            "Pyrantel pamoate"
        ],
        "Liều Người lớn": [
            "400mg PO x 1",
            "100mg PO BID x 3 ngày",
            "11mg/kg PO QD x 3 ngày (max 1g/ngày)"
        ],
        "Liều Trẻ em": [
            "400mg PO x 1 (>1 tuổi)",
            "100mg PO BID x 3 ngày (>2 tuổi)",
            "11mg/kg PO QD x 3 ngày (>2 tuổi)"
        ],
        "Ghi chú": [
            "Hiệu quả cao",
            "Có thể dùng 1 liều 500mg",
            "An toàn cho trẻ em"
        ]
    }
    
    st.dataframe(pd.DataFrame(dosing_data), use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # ========== MONITORING ==========
    st.markdown("### 📈 Theo dõi")
    
    st.markdown("""
    **Sau điều trị:**
    - Soi phân lại sau 2-3 tuần
    - Đánh giá tình trạng thiếu máu (Hb, ferritin)
    - Theo dõi đáp ứng với bổ sung sắt
    
    **Dấu hiệu cảnh báo:**
    - Thiếu máu nặng không cải thiện
    - Nhiễm trùng tái phát
    """)
    
    st.markdown("---")
    
    # ========== PREVENTION ==========
    st.markdown("### 🛡️ Phòng ngừa")
    
    st.info("""
    - Đi giày dép khi đi trên đất
    - Tránh tiếp xúc trực tiếp với đất ẩm
    - Cải thiện vệ sinh môi trường
    - Điều trị định kỳ cho cộng đồng
    - Bổ sung sắt cho phụ nữ có thai và trẻ em
    """)


def render_strongyloidiasis():
    """Strongyloidiasis (Giun lươn) Protocol"""
    
    st.success("## 🪱 GIUN LƯƠN (Strongyloidiasis - Strongyloides stercoralis)")
    
    st.error("""
    **⚠️ QUAN TRỌNG: Giun lươn có thể gây nhiễm lan tỏa (disseminated) nguy hiểm!**
    - Đặc biệt nguy hiểm ở người suy giảm miễn dịch
    - Tỷ lệ tử vong: 50-85% nếu nhiễm lan tỏa
    """)
    
    st.markdown("### 📋 Chẩn đoán")
    
    with st.expander("🔍 Tiêu chuẩn chẩn đoán", expanded=True):
        st.markdown("""
        **Triệu chứng:**
        - Thường không có triệu chứng (light infection)
        - Đau bụng, tiêu chảy
        - Ngứa da (larva currens - đặc trưng)
        - Ho, khó thở (khi ấu trùng qua phổi)
        - Phát ban mẩn đỏ (urticaria)
        - Thiếu máu (heavy infection)
        
        **Nhiễm lan tỏa (Disseminated - nguy hiểm):**
        - Sốt, nhiễm khuẩn huyết
        - Viêm màng não
        - Suy đa tạng
        - Tỷ lệ tử vong cao
        
        **Xét nghiệm:**
        - Soi phân tìm ấu trùng (larvae) - khó phát hiện
        - Nuôi cấy phân (Baermann technique)
        - Hút dịch tá tràng (duodenal aspirate)
        - Huyết thanh học (ELISA, IFA)
        - Eosinophilia (thường có)
        """)
    
    st.markdown("---")
    
    # ========== TREATMENT ==========
    st.markdown("### 💊 Điều trị")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **Điều trị Không Biến chứng:**
        
        **Lựa chọn 1 (Ưu tiên):**
        - **Ivermectin** 200mcg/kg PO QD x 2 ngày
        - Hiệu quả: 85-95%
        - An toàn, ít tác dụng phụ
        
        **Lựa chọn 2:**
        - **Albendazole** 400mg PO BID x 7 ngày
        - Hiệu quả: 60-80%
        - Dùng khi không có ivermectin
        
        **Lựa chọn 3:**
        - **Thiabendazole** 25mg/kg PO BID x 2-3 ngày
        - Hiệu quả: 70-90%
        - Nhiều tác dụng phụ
        """)
    
    with col2:
        st.error("""
        **Điều trị Nhiễm Lan Tỏa (Disseminated):**
        
        **CẤP CỨU - ICU:**
        - **Ivermectin** 200mcg/kg PO QD x 7-14 ngày
        - Hoặc **Ivermectin** 200mcg/kg NG/OG nếu không uống được
        - Có thể cần dùng lâu hơn
        
        **Kết hợp:**
        - **Albendazole** 400mg PO BID x 7-14 ngày
        - Điều trị song song với ivermectin
        
        **Điều trị hỗ trợ:**
        - Kháng sinh nếu có nhiễm khuẩn
        - Điều trị suy đa tạng
        - ICU monitoring
        """)
    
    st.markdown("---")
    
    # ========== DOSING ==========
    st.markdown("### 💉 Liều Thuốc Chi tiết")
    
    import pandas as pd
    dosing_data = {
        "Thuốc": [
            "Ivermectin",
            "Albendazole",
            "Thiabendazole"
        ],
        "Liều Người lớn": [
            "200mcg/kg PO QD x 2 ngày",
            "400mg PO BID x 7 ngày",
            "25mg/kg PO BID x 2-3 ngày"
        ],
        "Liều Trẻ em": [
            "200mcg/kg PO QD x 2 ngày (>15kg)",
            "400mg PO BID x 7 ngày (>1 tuổi)",
            "25mg/kg PO BID x 2-3 ngày"
        ],
        "Ghi chú": [
            "Lựa chọn 1, an toàn, hiệu quả cao",
            "Dùng khi không có ivermectin",
            "Nhiều tác dụng phụ"
        ]
    }
    
    st.dataframe(pd.DataFrame(dosing_data), use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # ========== MONITORING ==========
    st.markdown("### 📈 Theo dõi")
    
    st.markdown("""
    **Sau điều trị:**
    - Soi phân lại sau 2-4 tuần (3 mẫu phân liên tiếp)
    - Hút dịch tá tràng lại nếu cần
    - Đánh giá triệu chứng
    - Đánh giá eosinophilia
    
    **Dấu hiệu cảnh báo:**
    - Triệu chứng không cải thiện
    - Vẫn còn ấu trùng trong phân
    - Dấu hiệu nhiễm lan tỏa
    - Cần điều trị lại
    """)
    
    st.markdown("---")
    
    # ========== SPECIAL POPULATIONS ==========
    st.markdown("### 👥 Nhóm Bệnh Nhân Đặc Biệt")
    
    st.warning("""
    **Người suy giảm miễn dịch (QUAN TRỌNG):**
    - Tăng nguy cơ nhiễm lan tỏa
    - Cần điều trị sớm và đầy đủ
    - Có thể cần điều trị dự phòng (prophylaxis)
    - Theo dõi sát
    
    **Trước khi dùng thuốc ức chế miễn dịch:**
    - **PHẢI** kiểm tra và điều trị giun lươn trước
    - Nếu có nhiễm, điều trị trước khi dùng steroid/immunosuppressant
    
    **Phụ nữ có thai:**
    - Ivermectin: Category C (cân nhắc)
    - Albendazole: Tránh trong 3 tháng đầu
    - Cân nhắc lợi ích/nguy cơ
    """)
    
    st.markdown("---")
    
    # ========== PREVENTION ==========
    st.markdown("### 🛡️ Phòng ngừa")
    
    st.info("""
    - Đi giày dép khi đi trên đất
    - Tránh tiếp xúc trực tiếp với đất ẩm
    - Cải thiện vệ sinh môi trường
    - Điều trị người nhiễm để ngăn lây lan
    - **QUAN TRỌNG:** Kiểm tra và điều trị trước khi dùng thuốc ức chế miễn dịch
    """)


def render_liver_fluke():
    """Liver Fluke (Sán lá gan) Protocol"""
    
    st.success("## 🪱 SÁN LÁ GAN (Liver Fluke - Clonorchis/Opisthorchis)")
    
    st.markdown("### 📋 Chẩn đoán")
    
    with st.expander("🔍 Tiêu chuẩn chẩn đoán", expanded=True):
        st.markdown("""
        **Triệu chứng:**
        - Thường không có triệu chứng (light infection)
        - Đau hạ sườn phải
        - Vàng da (nếu tắc mật)
        - Sốt, đau bụng (viêm đường mật)
        - Gan to
        - Mệt mỏi, chán ăn
        
        **Xét nghiệm:**
        - Soi phân tìm trứng sán
        - Siêu âm bụng: giãn đường mật, sỏi mật
        - CT/MRI: thấy sán trong đường mật
        - Eosinophilia
        - Tăng ALP, GGT
        """)
    
    st.markdown("---")
    
    # ========== TREATMENT ==========
    st.markdown("### 💊 Điều trị")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **Điều trị Không Biến chứng:**
        
        **Lựa chọn 1 (Ưu tiên):**
        - **Praziquantel** 25mg/kg PO TID x 2 ngày
        - Tổng liều: 150mg/kg
        - Hiệu quả: 85-95%
        
        **Lựa chọn 2:**
        - **Triclabendazole** 10mg/kg PO x 1-2 liều
        - Hiệu quả cao với sán lá gan lớn (Fasciola)
        """)
    
    with col2:
        st.warning("""
        **Điều trị Có Biến chứng:**
        
        **Viêm đường mật:**
        - Kháng sinh (nếu có nhiễm khuẩn)
        - Praziquantel sau khi ổn định
        
        **Tắc mật:**
        - ERCP để lấy sán, sỏi
        - Praziquantel sau ERCP
        
        **Ung thư đường mật:**
        - Điều trị theo ung thư
        - Praziquantel để diệt sán còn lại
        """)
    
    st.markdown("---")
    
    # ========== DOSING ==========
    st.markdown("### 💉 Liều Thuốc Chi tiết")
    
    import pandas as pd
    dosing_data = {
        "Thuốc": [
            "Praziquantel",
            "Triclabendazole"
        ],
        "Liều Người lớn": [
            "25mg/kg PO TID x 2 ngày",
            "10mg/kg PO x 1-2 liều"
        ],
        "Liều Trẻ em": [
            "25mg/kg PO TID x 2 ngày (>4 tuổi)",
            "10mg/kg PO x 1-2 liều"
        ],
        "Ghi chú": [
            "Tổng liều 150mg/kg, uống sau ăn",
            "Dùng cho Fasciola"
        ]
    }
    
    st.dataframe(pd.DataFrame(dosing_data), use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # ========== MONITORING ==========
    st.markdown("### 📈 Theo dõi")
    
    st.markdown("""
    **Sau điều trị:**
    - Soi phân lại sau 1-3 tháng
    - Siêu âm bụng để đánh giá đường mật
    - Theo dõi chức năng gan (ALT, AST, ALP, GGT)
    
    **Dấu hiệu cảnh báo:**
    - Vàng da tăng
    - Đau bụng dữ dội
    - Sốt, viêm đường mật
    """)
    
    st.markdown("---")
    
    # ========== PREVENTION ==========
    st.markdown("### 🛡️ Phòng ngừa")
    
    st.info("""
    - **KHÔNG ăn cá sống, gỏi cá**
    - Nấu chín cá trước khi ăn (>60°C trong 5 phút)
    - Ướp muối, phơi khô cá đúng cách
    - Tránh ăn cá nước ngọt sống
    - Cải thiện vệ sinh môi trường
    """)


def render_enterobiasis():
    """Enterobius vermicularis (Giun kim) Protocol"""
    
    st.success("## 🪱 GIUN KIM (Enterobius vermicularis)")
    
    st.markdown("### 📋 Chẩn đoán")
    
    with st.expander("🔍 Tiêu chuẩn chẩn đoán", expanded=True):
        st.markdown("""
        **Triệu chứng:**
        - Ngứa hậu môn (đặc trưng, thường về đêm)
        - Rối loạn giấc ngủ
        - Đau bụng nhẹ
        - Nhiễm đường tiết niệu (ở trẻ em gái)
        - Viêm âm đạo (vulvovaginitis)
        
        **Xét nghiệm:**
        - Scotch tape test: dán băng dính vào hậu môn buổi sáng
        - Soi phân ít có giá trị (giun không đẻ trứng trong phân)
        - Có thể thấy giun trưởng thành quanh hậu môn
        """)
    
    st.markdown("---")
    
    # ========== TREATMENT ==========
    st.markdown("### 💊 Điều trị")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **Điều trị Người Bệnh:**
        
        **Lựa chọn 1 (Ưu tiên):**
        - **Albendazole** 400mg PO x 1 liều
        - Lặp lại sau 2 tuần
        
        **Lựa chọn 2:**
        - **Mebendazole** 100mg PO x 1 liều
        - Lặp lại sau 2 tuần
        
        **Lựa chọn 3:**
        - **Pyrantel pamoate** 11mg/kg PO x 1 liều (max 1g)
        - Lặp lại sau 2 tuần
        """)
    
    with col2:
        st.warning("""
        **Điều trị Gia Đình:**
        
        **Quan trọng:**
        - Điều trị tất cả thành viên trong gia đình cùng lúc
        - Ngăn ngừa tái nhiễm
        
        **Vệ sinh:**
        - Rửa tay thường xuyên
        - Cắt móng tay ngắn
        - Thay quần áo, ga gối hàng ngày
        - Giặt nóng quần áo, ga gối
        """)
    
    st.markdown("---")
    
    # ========== DOSING ==========
    st.markdown("### 💉 Liều Thuốc Chi tiết")
    
    import pandas as pd
    dosing_data = {
        "Thuốc": [
            "Albendazole",
            "Mebendazole",
            "Pyrantel pamoate"
        ],
        "Liều Người lớn": [
            "400mg PO x 1, lặp lại sau 2 tuần",
            "100mg PO x 1, lặp lại sau 2 tuần",
            "11mg/kg PO x 1 (max 1g), lặp lại sau 2 tuần"
        ],
        "Liều Trẻ em": [
            "400mg PO x 1 (>1 tuổi), lặp lại sau 2 tuần",
            "100mg PO x 1 (>2 tuổi), lặp lại sau 2 tuần",
            "11mg/kg PO x 1 (>2 tuổi), lặp lại sau 2 tuần"
        ],
        "Ghi chú": [
            "Cần lặp lại sau 2 tuần",
            "Cần lặp lại sau 2 tuần",
            "An toàn cho trẻ em"
        ]
    }
    
    st.dataframe(pd.DataFrame(dosing_data), use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # ========== MONITORING ==========
    st.markdown("### 📈 Theo dõi")
    
    st.markdown("""
    **Sau điều trị:**
    - Đánh giá triệu chứng ngứa hậu môn
    - Scotch tape test lại sau 2-4 tuần
    - Nếu vẫn còn, điều trị lại
    
    **Dấu hiệu tái nhiễm:**
    - Ngứa hậu môn tái phát
    - Cần điều trị lại và tăng cường vệ sinh
    """)
    
    st.markdown("---")
    
    # ========== PREVENTION ==========
    st.markdown("### 🛡️ Phòng ngừa")
    
    st.info("""
    - Rửa tay thường xuyên, đặc biệt sau khi đi vệ sinh
    - Cắt móng tay ngắn
    - Tắm rửa hàng ngày, đặc biệt buổi sáng
    - Thay quần áo, ga gối thường xuyên
    - Giặt nóng quần áo, ga gối
    - Điều trị tất cả thành viên trong gia đình
    """)


def render_taeniasis():
    """Tapeworm (Sán dây) Protocol"""
    
    st.success("## 🪱 SÁN DÂY (Tapeworm - Taenia/Taeniasis)")
    
    st.markdown("### 📋 Chẩn đoán")
    
    with st.expander("🔍 Tiêu chuẩn chẩn đoán", expanded=True):
        st.markdown("""
        **Triệu chứng:**
        - Thường không có triệu chứng
        - Đau bụng nhẹ
        - Buồn nôn, chán ăn
        - Sụt cân
        - Thấy đốt sán trong phân (proglottids)
        - Ngứa hậu môn
        
        **Xét nghiệm:**
        - Soi phân tìm trứng sán
        - Thấy đốt sán trong phân
        - PCR phân (nếu có)
        
        **Phân biệt:**
        - Taenia saginata (bò): không gây cysticercosis
        - Taenia solium (lợn): có thể gây cysticercosis
        """)
    
    st.markdown("---")
    
    # ========== TREATMENT ==========
    st.markdown("### 💊 Điều trị")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **Điều trị Taeniasis:**
        
        **Lựa chọn 1 (Ưu tiên):**
        - **Praziquantel** 5-10mg/kg PO x 1 liều
        - Hiệu quả: 95-100%
        
        **Lựa chọn 2:**
        - **Niclosamide** 2g PO x 1 liều (người lớn)
        - 1g PO x 1 liều (trẻ em 11-34kg)
        - 1.5g PO x 1 liều (trẻ em >34kg)
        - Uống lúc đói, nhai kỹ
        
        **Lựa chọn 3:**
        - **Albendazole** 400mg PO BID x 3 ngày
        """)
    
    with col2:
        st.warning("""
        **Lưu Ý Quan Trọng:**
        
        **Nếu nghi Taenia solium:**
        - Cần điều trị cẩn thận
        - Praziquantel có thể gây viêm do chết sán
        - Cân nhắc dùng Niclosamide hoặc Albendazole
        
        **Sau điều trị:**
        - Theo dõi đốt sán trong phân
        - Soi phân lại sau 1-3 tháng
        
        **Phòng ngừa cysticercosis:**
        - Rửa tay sau khi đi vệ sinh
        - Nấu chín thịt lợn
        - Tránh tự nhiễm
        """)
    
    st.markdown("---")
    
    # ========== DOSING ==========
    st.markdown("### 💉 Liều Thuốc Chi tiết")
    
    import pandas as pd
    dosing_data = {
        "Thuốc": [
            "Praziquantel",
            "Niclosamide",
            "Albendazole"
        ],
        "Liều Người lớn": [
            "5-10mg/kg PO x 1",
            "2g PO x 1 (nhai kỹ, lúc đói)",
            "400mg PO BID x 3 ngày"
        ],
        "Liều Trẻ em": [
            "5-10mg/kg PO x 1 (>4 tuổi)",
            "1-1.5g PO x 1 (theo cân nặng)",
            "400mg PO BID x 3 ngày (>1 tuổi)"
        ],
        "Ghi chú": [
            "Hiệu quả cao",
            "Uống lúc đói, nhai kỹ",
            "Dùng khi nghi T. solium"
        ]
    }
    
    st.dataframe(pd.DataFrame(dosing_data), use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # ========== MONITORING ==========
    st.markdown("### 📈 Theo dõi")
    
    st.markdown("""
    **Sau điều trị:**
    - Theo dõi đốt sán trong phân
    - Soi phân lại sau 1-3 tháng
    - Đánh giá triệu chứng
    
    **Dấu hiệu cảnh báo:**
    - Vẫn thấy đốt sán sau điều trị
    - Triệu chứng thần kinh (nghi cysticercosis)
    """)
    
    st.markdown("---")
    
    # ========== PREVENTION ==========
    st.markdown("### 🛡️ Phòng ngừa")
    
    st.info("""
    - **Nấu chín thịt** (nhiệt độ >60°C)
    - Kiểm tra thịt trước khi ăn
    - Rửa tay sau khi đi vệ sinh
    - Tránh tự nhiễm (auto-infection)
    - Cải thiện vệ sinh môi trường
    - Điều trị người nhiễm để ngăn lây lan
    """)


def render_paragonimiasis():
    """Paragonimiasis (Sán lá phổi) Protocol"""
    
    st.success("## 🪱 SÁN LÁ PHỔI (Paragonimiasis - Paragonimus)")
    
    st.markdown("### 📋 Chẩn đoán")
    
    with st.expander("🔍 Tiêu chuẩn chẩn đoán", expanded=True):
        st.markdown("""
        **Triệu chứng:**
        - Ho mạn tính, ho ra máu (hemoptysis)
        - Đau ngực
        - Khó thở
        - Sốt, mệt mỏi
        - Triệu chứng giống lao phổi
        - Có thể có tràn dịch màng phổi
        
        **Xét nghiệm:**
        - Soi đờm tìm trứng sán
        - Soi phân tìm trứng sán
        - X-quang ngực: thâm nhiễm, hang, tràn dịch
        - CT ngực: nốt, hang
        - Huyết thanh học (ELISA)
        - Eosinophilia
        """)
    
    st.markdown("---")
    
    # ========== TREATMENT ==========
    st.markdown("### 💊 Điều trị")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **Điều trị Không Biến chứng:**
        
        **Lựa chọn 1 (Ưu tiên):**
        - **Praziquantel** 25mg/kg PO TID x 2 ngày
        - Tổng liều: 150mg/kg
        - Hiệu quả: 90-95%
        
        **Lựa chọn 2:**
        - **Triclabendazole** 10mg/kg PO BID x 1 ngày
        - Hoặc 20mg/kg PO x 1 liều
        - Hiệu quả cao
        """)
    
    with col2:
        st.warning("""
        **Điều trị Có Biến chứng:**
        
        **Tràn dịch màng phổi:**
        - Điều trị sán
        - Chọc hút dịch nếu cần
        
        **Nhiễm nặng:**
        - Praziquantel 25mg/kg PO TID x 3 ngày
        - Hoặc Triclabendazole 10mg/kg PO BID x 2 ngày
        
        **Nhiễm não (hiếm):**
        - Praziquantel 25mg/kg PO TID x 3 ngày
        - Corticosteroid nếu có phù não
        """)
    
    st.markdown("---")
    
    # ========== DOSING ==========
    st.markdown("### 💉 Liều Thuốc Chi tiết")
    
    import pandas as pd
    dosing_data = {
        "Thuốc": [
            "Praziquantel",
            "Triclabendazole"
        ],
        "Liều Người lớn": [
            "25mg/kg PO TID x 2 ngày",
            "10mg/kg PO BID x 1 ngày"
        ],
        "Liều Trẻ em": [
            "25mg/kg PO TID x 2 ngày (>4 tuổi)",
            "10mg/kg PO BID x 1 ngày"
        ],
        "Ghi chú": [
            "Tổng liều 150mg/kg, uống sau ăn",
            "Hiệu quả cao, ít tác dụng phụ"
        ]
    }
    
    st.dataframe(pd.DataFrame(dosing_data), use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # ========== MONITORING ==========
    st.markdown("### 📈 Theo dõi")
    
    st.markdown("""
    **Sau điều trị:**
    - Soi đờm, phân lại sau 1-3 tháng
    - X-quang ngực để đánh giá
    - Theo dõi triệu chứng hô hấp
    
    **Dấu hiệu cảnh báo:**
    - Ho ra máu tăng
    - Khó thở tăng
    - Sốt kéo dài
    """)
    
    st.markdown("---")
    
    # ========== PREVENTION ==========
    st.markdown("### 🛡️ Phòng ngừa")
    
    st.info("""
    - **KHÔNG ăn cua, tôm càng sống hoặc chưa nấu chín**
    - Nấu chín cua, tôm càng (>60°C trong 5 phút)
    - Ướp muối, phơi khô đúng cách
    - Tránh ăn gỏi cua, tôm càng
    - Cải thiện vệ sinh môi trường
    """)


def render_amoebiasis():
    """Amoebiasis (Amip) Protocol"""
    
    st.success("## 🦠 AMIP (Amoebiasis - Entamoeba histolytica)")
    
    st.markdown("### 📋 Chẩn đoán")
    
    with st.expander("🔍 Tiêu chuẩn chẩn đoán", expanded=True):
        st.markdown("""
        **Triệu chứng:**
        - Tiêu chảy nhẹ đến nặng
        - Đau bụng, đau quặn
        - Phân có máu, nhầy (giống lỵ)
        - Sốt (có thể có)
        - Mệt mỏi, sụt cân
        - Áp xe gan (nếu nhiễm ngoài ruột)
        
        **Xét nghiệm:**
        - Soi phân tìm kén/hoạt động thể (trophozoite)
        - Test nhanh kháng nguyên (antigen test)
        - PCR phân
        - Siêu âm bụng (nếu nghi áp xe gan)
        - CT/MRI (nếu nghi áp xe gan)
        """)
    
    st.markdown("---")
    
    # ========== TREATMENT ==========
    st.markdown("### 💊 Điều trị")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **Điều trị Nhiễm Ruột:**
        
        **Lựa chọn 1 (Ưu tiên):**
        - **Metronidazole** 750mg PO TID x 10 ngày
        - Hoặc 500mg PO TID x 10 ngày
        - Sau đó: **Paromomycin** 25-30mg/kg/ngày PO chia 3 lần x 5-10 ngày
        
        **Lựa chọn 2:**
        - **Tinidazole** 2g PO QD x 3 ngày
        - Sau đó: **Paromomycin** 25-30mg/kg/ngày PO chia 3 lần x 5-10 ngày
        
        **Lựa chọn 3:**
        - **Nitazoxanide** 500mg PO BID x 3 ngày (người lớn)
        """)
    
    with col2:
        st.warning("""
        **Điều trị Áp Xe Gan:**
        
        **Lựa chọn 1:**
        - **Metronidazole** 750mg PO TID x 10 ngày
        - Hoặc **Tinidazole** 2g PO QD x 5 ngày
        - Sau đó: **Paromomycin** để diệt kén trong ruột
        
        **Lựa chọn 2 (nặng):**
        - **Metronidazole** 500mg IV q8h x 10 ngày
        - Chuyển sang PO khi có thể
        - Sau đó: **Paromomycin**
        
        **Chọc hút áp xe:**
        - Nếu áp xe lớn (>5cm) hoặc có nguy cơ vỡ
        - Kết hợp với điều trị thuốc
        """)
    
    st.markdown("---")
    
    # ========== DOSING ==========
    st.markdown("### 💉 Liều Thuốc Chi tiết")
    
    import pandas as pd
    dosing_data = {
        "Thuốc": [
            "Metronidazole",
            "Tinidazole",
            "Paromomycin",
            "Nitazoxanide"
        ],
        "Liều Người lớn": [
            "750mg PO TID x 10 ngày",
            "2g PO QD x 3-5 ngày",
            "25-30mg/kg/ngày PO chia 3 lần x 5-10 ngày",
            "500mg PO BID x 3 ngày"
        ],
        "Liều Trẻ em": [
            "35-50mg/kg/ngày PO chia 3 lần x 10 ngày",
            "50mg/kg/ngày PO (max 2g) x 3-5 ngày",
            "25-30mg/kg/ngày PO chia 3 lần x 5-10 ngày",
            "100mg PO BID x 3 ngày (1-3 tuổi)"
        ],
        "Ghi chú": [
            "Tránh rượu khi dùng",
            "Ít tác dụng phụ hơn metronidazole",
            "Diệt kén trong ruột",
            "Dùng cho nhiễm ruột nhẹ"
        ]
    }
    
    st.dataframe(pd.DataFrame(dosing_data), use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # ========== MONITORING ==========
    st.markdown("### 📈 Theo dõi")
    
    st.markdown("""
    **Sau điều trị:**
    - Soi phân lại sau 1-2 tuần
    - Đánh giá triệu chứng
    - Siêu âm bụng (nếu có áp xe gan)
    
    **Dấu hiệu cảnh báo:**
    - Tiêu chảy không cải thiện
    - Đau bụng tăng
    - Sốt, áp xe gan
    """)
    
    st.markdown("---")
    
    # ========== PREVENTION ==========
    st.markdown("### 🛡️ Phòng ngừa")
    
    st.info("""
    - Rửa tay sau khi đi vệ sinh
    - Rửa sạch rau quả
    - Uống nước sạch, đun sôi
    - Tránh ăn thức ăn đường phố không đảm bảo
    - Cải thiện vệ sinh môi trường
    """)


def render_giardiasis():
    """Giardiasis (Giardia) Protocol"""
    
    st.success("## 🦠 GIARDIA (Giardiasis - Giardia lamblia)")
    
    st.markdown("### 📋 Chẩn đoán")
    
    with st.expander("🔍 Tiêu chuẩn chẩn đoán", expanded=True):
        st.markdown("""
        **Triệu chứng:**
        - Tiêu chảy (thường không có máu)
        - Phân nhiều nước, có mùi hôi
        - Đầy hơi, chướng bụng
        - Buồn nôn, nôn
        - Sụt cân
        - Mệt mỏi
        - Có thể không có triệu chứng
        
        **Xét nghiệm:**
        - Soi phân tìm kén/hoạt động thể (trophozoite)
        - Test nhanh kháng nguyên (antigen test) - nhạy cảm cao
        - PCR phân
        - Hút dịch tá tràng (nếu cần)
        """)
    
    st.markdown("---")
    
    # ========== TREATMENT ==========
    st.markdown("### 💊 Điều trị")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **Điều trị Không Biến chứng:**
        
        **Lựa chọn 1 (Ưu tiên):**
        - **Metronidazole** 250mg PO TID x 5-7 ngày
        - Hoặc 500mg PO BID x 5-7 ngày
        - Hiệu quả: 80-95%
        
        **Lựa chọn 2:**
        - **Tinidazole** 2g PO x 1 liều
        - Hiệu quả: 90-100%
        - Thuận tiện (1 liều)
        
        **Lựa chọn 3:**
        - **Nitazoxanide** 500mg PO BID x 3 ngày (người lớn)
        - Hiệu quả: 85-90%
        """)
    
    with col2:
        st.warning("""
        **Điều trị Thất Bại/Tái phát:**
        
        **Lần 1 thất bại:**
        - Thử **Tinidazole** 2g PO x 1 liều
        - Hoặc **Nitazoxanide** 500mg PO BID x 3 ngày
        
        **Tái phát:**
        - **Metronidazole** 750mg PO TID x 10 ngày
        - Hoặc **Quinacrine** 100mg PO TID x 5-7 ngày (nếu có)
        
        **Kháng thuốc:**
        - **Albendazole** 400mg PO BID x 5-7 ngày
        - Hoặc **Furazolidone** 100mg PO QID x 7-10 ngày
        """)
    
    st.markdown("---")
    
    # ========== DOSING ==========
    st.markdown("### 💉 Liều Thuốc Chi tiết")
    
    import pandas as pd
    dosing_data = {
        "Thuốc": [
            "Metronidazole",
            "Tinidazole",
            "Nitazoxanide",
            "Albendazole"
        ],
        "Liều Người lớn": [
            "250mg PO TID x 5-7 ngày",
            "2g PO x 1 liều",
            "500mg PO BID x 3 ngày",
            "400mg PO BID x 5-7 ngày"
        ],
        "Liều Trẻ em": [
            "15mg/kg/ngày PO chia 3 lần x 5-7 ngày",
            "50mg/kg PO x 1 liều (max 2g)",
            "100-200mg PO BID x 3 ngày (tùy tuổi)",
            "10-15mg/kg/ngày PO chia 2 lần x 5-7 ngày"
        ],
        "Ghi chú": [
            "Tránh rượu khi dùng",
            "1 liều, hiệu quả cao",
            "An toàn cho trẻ em",
            "Dùng khi kháng metronidazole"
        ]
    }
    
    st.dataframe(pd.DataFrame(dosing_data), use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # ========== MONITORING ==========
    st.markdown("### 📈 Theo dõi")
    
    st.markdown("""
    **Sau điều trị:**
    - Soi phân lại sau 1-2 tuần
    - Đánh giá triệu chứng
    - Test kháng nguyên lại (nếu có)
    
    **Dấu hiệu cảnh báo:**
    - Tiêu chảy không cải thiện
    - Tái phát sau điều trị
    - Sụt cân, mất nước
    """)
    
    st.markdown("---")
    
    # ========== PREVENTION ==========
    st.markdown("### 🛡️ Phòng ngừa")
    
    st.info("""
    - Rửa tay sau khi đi vệ sinh
    - Uống nước sạch, đun sôi hoặc lọc
    - Tránh uống nước từ suối, sông không xử lý
    - Rửa sạch rau quả
    - Tránh bơi ở nước bị ô nhiễm
    - Cải thiện vệ sinh môi trường
    - Điều trị người nhiễm để ngăn lây lan
    """)


def render_mixed_infection():
    """Mixed Parasitic Infection Protocol"""
    
    st.warning("## 🪱 NHIỄM PHỐI HỢP (Mixed Parasitic Infection)")
    
    st.markdown("### 📋 Chẩn đoán")
    
    st.info("""
    **Nhiễm phối hợp giun sán rất phổ biến ở Việt Nam:**
    - Thường gặp: Giun đũa + Giun tóc + Giun móc
    - Có thể kết hợp với sán lá gan
    - Cần xét nghiệm phân đầy đủ để xác định tất cả loại
    """)
    
    st.markdown("---")
    
    # ========== TREATMENT ==========
    st.markdown("### 💊 Điều trị")
    
    st.success("""
    **Điều trị Nhiễm Phối Hợp:**
    
    **Lựa chọn 1 (Ưu tiên - Phổ rộng):**
    - **Albendazole** 400mg PO x 1 liều
    - Hiệu quả với: Giun đũa, Giun tóc, Giun móc, Giun kim
    - Lặp lại sau 2-4 tuần nếu cần
    
    **Lựa chọn 2:**
    - **Mebendazole** 100mg PO BID x 3 ngày
    - Hiệu quả với: Giun đũa, Giun tóc, Giun móc
    
    **Nếu có Sán lá gan:**
    - Thêm **Praziquantel** 25mg/kg PO TID x 2 ngày
    - Điều trị sau khi đã điều trị giun
    """)
    
    st.markdown("---")
    
    # ========== DOSING SCHEDULE ==========
    st.markdown("### 📅 Lịch Điều trị")
    
    st.markdown("""
    **Ngày 1-3:**
    - Albendazole 400mg PO x 1 (cho giun đũa, giun tóc, giun móc)
    - Hoặc Mebendazole 100mg PO BID x 3 ngày
    
    **Ngày 4-5 (nếu có sán lá gan):**
    - Praziquantel 25mg/kg PO TID x 2 ngày
    
    **Sau 2-4 tuần:**
    - Soi phân lại
    - Điều trị lại nếu cần
    """)
    
    st.markdown("---")
    
    # ========== MONITORING ==========
    st.markdown("### 📈 Theo dõi")
    
    st.markdown("""
    **Sau điều trị:**
    - Soi phân lại sau 2-4 tuần
    - Đánh giá tất cả loại ký sinh trùng
    - Đánh giá triệu chứng
    - Đánh giá tình trạng thiếu máu (nếu có giun móc)
    
    **Dấu hiệu cảnh báo:**
    - Vẫn còn trứng trong phân
    - Triệu chứng không cải thiện
    - Thiếu máu không cải thiện
    """)
    
    st.markdown("---")
    
    # ========== PREVENTION ==========
    st.markdown("### 🛡️ Phòng ngừa")
    
    st.info("""
    - Rửa tay trước khi ăn
    - Rửa sạch rau quả
    - Nấu chín thức ăn (đặc biệt cá, thịt)
    - Đi giày dép khi đi trên đất
    - Cải thiện vệ sinh môi trường
    - Điều trị định kỳ cho cộng đồng (mass deworming)
    - Bổ sung sắt cho phụ nữ có thai và trẻ em
    """)
    
    st.markdown("---")
    
    # ========== SPECIAL POPULATIONS ==========
    st.markdown("### 👥 Nhóm Bệnh Nhân Đặc Biệt")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Trẻ em:**
        - Nhiễm phối hợp rất phổ biến
        - Cần điều trị đầy đủ
        - Theo dõi tăng trưởng
        - Bổ sung sắt nếu thiếu máu
        
        **Phụ nữ có thai:**
        - Tránh Albendazole, Mebendazole trong 3 tháng đầu
        - Có thể dùng Pyrantel pamoate
        - Bổ sung sắt, acid folic
        """)
    
    with col2:
        st.markdown("""
        **Người cao tuổi:**
        - Theo dõi tác dụng phụ thuốc
        - Đánh giá tương tác thuốc
        - Điều chỉnh liều nếu suy thận
        
        **Suy thận:**
        - Điều chỉnh liều theo CrCl
        - Theo dõi chức năng thận
        """)
    
    st.markdown("---")
    
    # ========== REFERENCES ==========
    references = get_references("Parasitic Infections")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )
    
    st.markdown("---")
    
    # Footer
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể, xét nghiệm phân, và guidelines mới nhất.")

