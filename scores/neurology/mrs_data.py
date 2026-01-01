"""
mRS - Modified Rankin Scale Data
Contains all mRS grade definitions and descriptions
"""

from config.theme import COLORS

MRS_GRADES = {
    0: {
        "name": "mRS 0 - Không có triệu chứng",
        "desc": """
        **Hoàn toàn không có triệu chứng**
        
        **Đặc điểm:**
        - Không có bất kỳ triệu chứng nào
        - Hoàn toàn bình thường
        - Có thể thực hiện tất cả các hoạt động như trước
        
        **Ví dụ:**
        - Người bệnh đã hồi phục hoàn toàn sau TIA hoặc đột quỵ nhẹ
        - Không có dấu hiệu suy giảm thần kinh
        """,
        "color": COLORS["success"],
        "icon": "✅",
        "outcome": "Excellent",
        "independence": "Hoàn toàn độc lập"
    },
    1: {
        "name": "mRS 1 - Không khuyết tật đáng kể",
        "desc": """
        **Không khuyết tật đáng kể mặc dù có triệu chứng**
        
        **Đặc điểm:**
        - Có thể thực hiện tất cả nhiệm vụ và hoạt động thường ngày như trước
        - Có thể có triệu chứng nhẹ (ví dụ: yếu nhẹ, rối loạn cảm giác nhẹ)
        - Triệu chứng không ảnh hưởng đến khả năng tự chăm sóc bản thân
        
        **Ví dụ:**
        - Yếu tay/chân nhẹ nhưng vẫn làm việc bình thường
        - Tê bì nhẹ nhưng không ảnh hưởng sinh hoạt
        - Nói khó nhẹ nhưng vẫn giao tiếp tốt
        """,
        "color": COLORS["success"],
        "icon": "✅",
        "outcome": "Excellent",
        "independence": "Hoàn toàn độc lập"
    },
    2: {
        "name": "mRS 2 - Khuyết tật nhẹ",
        "desc": """
        **Khuyết tật nhẹ: Không thể thực hiện tất cả hoạt động như trước, nhưng tự chăm sóc được**
        
        **Đặc điểm:**
        - Không thể thực hiện một số hoạt động như trước đột quỵ
        - Có thể tự chăm sóc bản thân KHÔNG CẦN trợ giúp
        - Có thể đi lại độc lập
        - Có thể cần thay đổi công việc hoặc giảm giờ làm
        
        **Ví dụ:**
        - Không thể chạy bộ nhưng đi bộ bình thường
        - Không thể làm việc cũ (nặng) nhưng làm việc nhẹ được
        - Tự nấu ăn, tắm rửa, ăn uống được
        - Yếu tay/chân vừa phải nhưng không cần người hỗ trợ
        """,
        "color": COLORS["success"],
        "icon": "🟢",
        "outcome": "Good",
        "independence": "Độc lập"
    },
    3: {
        "name": "mRS 3 - Khuyết tật trung bình",
        "desc": """
        **Khuyết tật trung bình: Cần một ít trợ giúp, nhưng đi lại không cần hỗ trợ**
        
        **Đặc điểm:**
        - Cần một ít trợ giúp trong sinh hoạt
        - **Có thể đi lại KHÔNG CẦN hỗ trợ** (không cần người nâng đỡ, có thể dùng gậy)
        - Cần giúp đỡ một số hoạt động: nấu ăn, giặt giũ, quản lý tiền bạc
        
        **Ví dụ:**
        - Tự đi lại được (có thể dùng gậy) nhưng cần người giúp nấu ăn
        - Tự tắm rửa, ăn uống nhưng cần giúp mặc quần áo
        - Đi lại trong nhà tốt, ra ngoài cần có người đi cùng
        - Cần giúp quản lý thuốc, tài chính
        """,
        "color": COLORS["warning"],
        "icon": "🟡",
        "outcome": "Moderate",
        "independence": "Phụ thuộc nhẹ"
    },
    4: {
        "name": "mRS 4 - Khuyết tật vừa nặng",
        "desc": """
        **Khuyết tật vừa nặng: Không thể đi lại độc lập và không tự chăm sóc được**
        
        **Đặc điểm:**
        - **KHÔNG thể đi lại mà không có hỗ trợ** (cần người nâng đỡ)
        - **KHÔNG thể tự chăm sóc nhu cầu cơ thể** (tắm, vệ sinh, ăn uống)
        - Cần người chăm sóc thường xuyên trong ngày
        
        **Ví dụ:**
        - Cần người đỡ để đi từ giường sang ghế
        - Cần giúp tắm, vệ sinh, mặc quần áo
        - Có thể cần giúp ăn uống
        - Liệt nặng, chỉ ngồi được trên xe lăn hoặc nằm giường
        - Có thể tự ngồi nhưng không tự đi được
        """,
        "color": COLORS["error"],
        "icon": "🔴",
        "outcome": "Poor",
        "independence": "Phụ thuộc nặng"
    },
    5: {
        "name": "mRS 5 - Khuyết tật nặng",
        "desc": """
        **Khuyết tật nặng: Nằm liệt giường, tiểu tiện không tự chủ, cần chăm sóc liên tục**
        
        **Đặc điểm:**
        - **Nằm liệt giường** (bedridden)
        - **Tiểu tiện không tự chủ** (incontinence)
        - **Cần chăm sóc y tế liên tục 24/7**
        - Không thể tự thực hiện bất kỳ hoạt động nào
        
        **Ví dụ:**
        - Nằm liệt giường hoàn toàn
        - Không thể tự thay đổi tư thế
        - Cần đặt thông tiểu hoặc tã người lớn
        - Cần cho ăn qua ống hoặc nuôi bằng thìa
        - Cần chăm sóc toàn bộ: vệ sinh, thay đổi tư thế, phòng loét
        - Có thể ở trạng thái thực vật (vegetative state)
        """,
        "color": COLORS["error"],
        "icon": "⚫",
        "outcome": "Very Poor",
        "independence": "Phụ thuộc hoàn toàn"
    },
    6: {
        "name": "mRS 6 - Tử vong",
        "desc": """
        **Tử vong**
        
        **Đặc điểm:**
        - Bệnh nhân đã tử vong
        """,
        "color": COLORS["neutral_dark"],
        "icon": "💀",
        "outcome": "Death",
        "independence": "N/A"
    }
}

