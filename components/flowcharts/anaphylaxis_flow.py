"""
Interactive Flowchart Data for Anaphylaxis (Sốc phản vệ)
Based on Vietnamese Ministry of Health Guidelines (Circular 51/2017/TT-BYT)
"""

ANAPHYLAXIS_FLOW = {
    "title": "Phác đồ cấp cứu Phản vệ (Thông tư 51/2017/TT-BYT)",
    "start_node_id": "assessment_start",
    "nodes": {
        "assessment_start": {
            "type": "question",
            "title": "Đánh giá ban đầu",
            "content": """
            **Bệnh nhân có xuất hiện đột ngột các triệu chứng:**
            - Mề đay, phù mạch, ngứa?
            - Khó thở, tức ngực, thở rít?
            - Tụt huyết áp, ngất?
            - Đau bụng, nôn?
            
            *Ngay sau khi tiếp xúc dị nguyên?*
            """,
            "options": [
                {"label": "Có, nghi ngờ phản vệ", "next": "grade_assessment"},
                {"label": "Không rõ/Không", "next": "monitor_other"}
            ]
        },
        "monitor_other": {
             "type": "result",
             "title": "Theo dõi nguyên nhân khác",
             "content": "Tiếp tục theo dõi, đánh giá các nguyên nhân khác (Ngất xỉu, Hạ đường huyết, Nhồi máu cơ tim...).",
             "next": None
        },
        "grade_assessment": {
            "type": "question",
            "title": "Phân độ phản vệ",
            "content": """
            **Chọn mức độ nặng nhất bệnh nhân đang gặp phải:**
            
            1. **Độ I (Nhẹ):** Chỉ có biểu hiện da/niêm mạc (ngứa, mề đay).
            2. **Độ II (Nặng):** Có từ 2 biểu hiện trở lên (Da + Hô hấp/Tuần hoàn/Tiêu hóa).
            3. **Độ III (Nguy kịch):** Tụt HA, ngất, rít thanh quản, tím tái.
            4. **Độ IV (Ngừng tuần hoàn):** Ngừng hô hấp, ngừng tuần hoàn.
            """,
            "options": [
                {"label": "Độ I (Chỉ triệu chứng da)", "next": "treat_grade_1"},
                {"label": "Độ II (Nặng)", "next": "treat_adrenaline_im"},
                {"label": "Độ III (Nguy kịch)", "next": "treat_adrenaline_im"},
                {"label": "Độ IV (Ngừng tuần hoàn)", "next": "cpr_protocol"}
            ]
        },
        "treat_grade_1": {
            "type": "action",
            "title": "Xử trí Độ I",
            "content": """
            - Sử dụng **Diphenhydramin** hoặc **Methylprednisolon** (uống hoặc tiêm).
            - Theo dõi sát ít nhất 24 giờ.
            """,
            "warning": "Nếu diễn biến nặng lên (khó thở, tụt HA) -> Chuyển sang xử trí như Độ II ngay!",
            "next": None
        },
        "treat_adrenaline_im": {
            "type": "action",
            "title": "TIÊM ADRENALINE NGAY LẬP TỨC!",
            "content": """
            **Adrenaline 1mg/1ml (1 ống)**
            
            **Tiêm bắp (IM)** (mặt trước bên đùi):
            - Người lớn (>30kg): **1/2 - 1 ống**
            - Trẻ em (6-12 tuổi): **1/2 ống**
            - Trẻ nhỏ (<6 tuổi): **1/5 - 1/4 ống**
            
            *Nhắc lại liều sau mỗi 3-5 phút nếu chưa ổn định.*
            """,
            "warning": "Adrenaline là thuốc quan trọng nhất, tiêm càng sớm càng tốt!",
            "next": "post_adrenaline_monitoring"
        },
        "cpr_protocol": {
            "type": "action",
            "title": "Cấp cứu ngừng tuần hoàn (CPR)",
            "content": """
            - Ép tim ngoài lồng ngực + Thông khí ngay.
            - **Tiêm Adrenaline tĩnh mạch (IV)** hoặc tiêm qua màng nhẫn giáp nếu không có đường truyền.
            - Gọi hỗ trợ cấp cứu ngay lập tức!
            """,
             "next": "post_adrenaline_monitoring"
        },
        "post_adrenaline_monitoring": {
            "type": "question",
            "title": "Đánh giá đáp ứng sau tiêm Adrenaline",
            "content": "Sau 3-5 phút, tình trạng bệnh nhân thế nào? \n(Huyết áp lên? Hết khó thở?)",
            "options": [
                {"label": "Tốt lên (HA ổn định, hết khó thở)", "next": "maintenance"},
                {"label": "Không cải thiện / Xấu đi", "next": "escalate_treatment"}
            ]
        },
        "escalate_treatment": {
             "type": "action",
             "title": "Tăng cường xử trí",
             "content": """
             - Tiếp tục tiêm bắp Adrenaline nhắc lại.
             - Thiết lập đường truyền tĩnh mạch.
             - Truyền dịch Nhanh.
             - Chuẩn bị truyền tĩnh mạch Adrenaline liên tục (Duy trì).
             - Hỗ trợ hô hấp (Thở oxy, Đặt NKQ nếu cần).
             """,
             "next": "post_adrenaline_monitoring"
        },
        "maintenance": {
             "type": "result",
             "title": "Duy trì và Theo dõi",
             "content": """
             - Truyền dịch duy trì.
             - Có thể dùng thêm Corticoid, Kháng Histamin (sau khi đã ổn định HA).
             - Theo dõi tại viện ít nhất 24 giờ để phòng phản vệ pha 2.
             """,
             "next": None
        }
    }
}
