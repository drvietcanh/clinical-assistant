"""
Antibiotic Stewardship Principles
Nguyên tắc quản lý kháng sinh
"""

from typing import List, Dict, Optional
from dataclasses import dataclass


@dataclass
class StewardshipPrinciple:
    """Nguyên tắc quản lý kháng sinh"""
    title: str
    title_vi: str
    description: str
    key_points: List[str]
    examples: Optional[List[str]] = None


STEWARDSHIP_PRINCIPLES = [
    StewardshipPrinciple(
        title="Right Drug",
        title_vi="Chọn đúng thuốc",
        description="Chọn kháng sinh phù hợp dựa trên vi khuẩn gây bệnh, phổ tác dụng, và kháng thuốc tại địa phương",
        key_points=[
            "Dựa vào kết quả cấy và độ nhạy cảm khi có",
            "Xem xét phổ tác dụng phù hợp (không quá rộng, không quá hẹp)",
            "Chọn kháng sinh theo AWaRe classification (ACCESS > WATCH > RESERVE)",
            "Xem xét kháng thuốc tại địa phương",
            "Tránh dùng kháng sinh phổ rộng không cần thiết"
        ],
        examples=[
            "CAP không biến chứng: Amoxicillin hoặc Amoxicillin-clavulanate (không cần carbapenem)",
            "UTI đơn giản: Nitrofurantoin hoặc TMP-SMX (không cần fluoroquinolone)",
            "Nhiễm khuẩn do MRSA: Vancomycin hoặc Clindamycin (không cần linezolid nếu không cần)"
        ]
    ),
    StewardshipPrinciple(
        title="Right Dose",
        title_vi="Liều đúng",
        description="Sử dụng liều kháng sinh phù hợp để đảm bảo hiệu quả và tránh độc tính",
        key_points=[
            "Điều chỉnh liều theo chức năng thận (CrCl/eGFR)",
            "Điều chỉnh liều theo cân nặng (đặc biệt ở béo phì)",
            "Xem xét tuổi tác và bệnh kèm theo",
            "Theo dõi nồng độ (TDM) khi cần (vancomycin, aminoglycoside)",
            "Sử dụng liều tối ưu để đạt hiệu quả điều trị"
        ],
        examples=[
            "Vancomycin: 15-20mg/kg mỗi 8-12 giờ + TDM để đạt trough 15-20 mg/L",
            "Gentamicin: 5-7mg/kg mỗi 24 giờ + TDM",
            "Điều chỉnh liều ở suy thận: Giảm liều hoặc tăng khoảng cách liều"
        ]
    ),
    StewardshipPrinciple(
        title="Right Duration",
        title_vi="Thời gian đúng",
        description="Điều trị đủ thời gian nhưng không quá dài",
        key_points=[
            "Tuân theo guideline về thời gian điều trị",
            "Rút ngắn thời gian khi có thể (nếu đáp ứng tốt)",
            "Tránh điều trị quá dài không cần thiết",
            "Đánh giá lại định kỳ để quyết định thời gian điều trị",
            "Xem xét chuyển IV → PO sớm"
        ],
        examples=[
            "CAP: 5-7 ngày (không cần 10-14 ngày)",
            "HAP/VAP: 7 ngày (không cần 14 ngày)",
            "UTI không biến chứng: 3-5 ngày"
        ]
    ),
    StewardshipPrinciple(
        title="Right Route",
        title_vi="Đường dùng đúng",
        description="Chọn đường dùng phù hợp: IV khi cần, PO khi có thể",
        key_points=[
            "Bắt đầu IV khi bệnh nhân nặng hoặc không thể uống",
            "Chuyển sang PO sớm khi có thể (sau 48-72 giờ)",
            "Xem xét độ hấp thu của thuốc đường uống",
            "Giảm chi phí và thời gian nằm viện bằng cách chuyển PO sớm"
        ],
        examples=[
            "Levofloxacin: Có thể chuyển IV → PO trực tiếp (bioavailability 99%)",
            "Amoxicillin-clavulanate: Có thể chuyển IV → PO (bioavailability 75-85%)",
            "Vancomycin: Không thể chuyển PO (chỉ dùng PO cho C. difficile)"
        ]
    ),
    StewardshipPrinciple(
        title="De-escalation",
        title_vi="Giảm liều",
        description="Giảm phổ kháng sinh và đổi thuốc khi có kết quả cấy",
        key_points=[
            "Đánh giá sau 48-72 giờ khi có kết quả cấy",
            "Chuyển từ phối hợp sang đơn trị khi có thể",
            "Chuyển từ kháng sinh phổ rộng sang phổ hẹp hơn",
            "Dựa vào kết quả cấy và độ nhạy cảm",
            "Đảm bảo bệnh nhân đã đáp ứng lâm sàng"
        ],
        examples=[
            "Từ Meropenem + Vancomycin → Ceftriaxone (nếu không có ESBL/KPC/MRSA)",
            "Từ Piperacillin-tazobactam + Vancomycin → Piperacillin-tazobactam đơn trị (nếu không có MRSA)"
        ]
    ),
    StewardshipPrinciple(
        title="Monitoring and Assessment",
        title_vi="Theo dõi và đánh giá",
        description="Theo dõi đáp ứng lâm sàng và đánh giá lại định kỳ",
        key_points=[
            "Đánh giá đáp ứng lâm sàng sau 48-72 giờ",
            "Theo dõi các dấu hiệu cải thiện (sốt, triệu chứng)",
            "Xem xét kết quả cấy và độ nhạy cảm",
            "Đánh giá lại định kỳ để quyết định tiếp tục, đổi, hoặc ngừng kháng sinh",
            "Theo dõi tác dụng phụ và độc tính"
        ],
        examples=[
            "Đánh giá sau 48-72 giờ: Bệnh nhân có cải thiện không?",
            "Nếu không cải thiện: Xem xét đổi kháng sinh hoặc tìm nguồn nhiễm trùng khác",
            "Nếu cải thiện tốt: Xem xét de-escalation hoặc chuyển PO"
        ]
    ),
    StewardshipPrinciple(
        title="Prevention of Resistance",
        title_vi="Phòng ngừa kháng thuốc",
        description="Áp dụng các biện pháp để phòng ngừa kháng thuốc",
        key_points=[
            "Sử dụng kháng sinh hợp lý (không lạm dụng)",
            "Tránh điều trị dự phòng không cần thiết",
            "Tuân theo guideline về thời gian điều trị",
            "Giáo dục bệnh nhân về sử dụng kháng sinh đúng cách",
            "Theo dõi và báo cáo kháng thuốc tại địa phương"
        ],
        examples=[
            "Không dùng kháng sinh cho cảm cúm (virus)",
            "Không dùng kháng sinh dự phòng không cần thiết",
            "Hoàn thành đủ liều kháng sinh theo chỉ định"
        ]
    ),
]


def get_stewardship_principles() -> List[StewardshipPrinciple]:
    """Lấy các nguyên tắc quản lý kháng sinh"""
    return STEWARDSHIP_PRINCIPLES


def render_principles_view():
    """Render UI cho stewardship principles"""
    import streamlit as st
    
    st.markdown("### 📋 Nguyên tắc Quản lý Kháng Sinh")
    st.caption("Các nguyên tắc cơ bản để sử dụng kháng sinh hiệu quả và an toàn")
    
    principles = get_stewardship_principles()
    
    for principle in principles:
        st.markdown(f"#### {principle.title_vi} ({principle.title})")
        st.markdown(f"**{principle.description}**")
        
        st.markdown("**Điểm chính:**")
        for point in principle.key_points:
            st.markdown(f"- ✓ {point}")
        
        if principle.examples:
            st.markdown("**Ví dụ:**")
            for example in principle.examples:
                st.markdown(f"- 💡 {example}")
        
        st.markdown("---")
    
    # Summary
    st.markdown("### 📊 Tóm tắt")
    st.markdown("""
    Quản lý kháng sinh hiệu quả dựa trên 7 nguyên tắc chính:
    1. **Chọn đúng thuốc** - Phù hợp với vi khuẩn và kháng thuốc tại địa phương
    2. **Liều đúng** - Đảm bảo hiệu quả và tránh độc tính
    3. **Thời gian đúng** - Đủ nhưng không quá dài
    4. **Đường dùng đúng** - IV khi cần, PO khi có thể
    5. **De-escalation** - Giảm phổ khi có kết quả cấy
    6. **Theo dõi và đánh giá** - Đánh giá lại định kỳ
    7. **Phòng ngừa kháng thuốc** - Sử dụng hợp lý để bảo vệ hiệu quả lâu dài
    """)
