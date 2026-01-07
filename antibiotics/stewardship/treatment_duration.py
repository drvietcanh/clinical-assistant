"""
Treatment Duration Recommendations
Khuyến cáo thời gian điều trị kháng sinh
"""

from typing import List, Dict, Optional
from dataclasses import dataclass


@dataclass
class TreatmentDuration:
    """Thời gian điều trị cho một loại nhiễm trùng"""
    infection_type: str
    infection_type_vi: str
    standard_duration: str
    short_duration: Optional[str] = None
    extended_duration: Optional[str] = None
    criteria: Optional[List[str]] = None
    notes: Optional[str] = None


TREATMENT_DURATION_RECOMMENDATIONS = [
    TreatmentDuration(
        infection_type="CAP",
        infection_type_vi="Viêm phổi cộng đồng",
        standard_duration="5-7 ngày",
        short_duration="3-5 ngày (nếu đáp ứng tốt và không có biến chứng)",
        extended_duration="10-14 ngày (nếu có biến chứng, áp xe phổi, hoặc vi khuẩn đặc biệt)",
        criteria=[
            "Đáp ứng lâm sàng tốt (afebrile ≥ 48h)",
            "Không có biến chứng",
            "Cấy máu âm tính"
        ],
        notes="Rút ngắn thời gian điều trị giúp giảm nguy cơ kháng thuốc và tác dụng phụ"
    ),
    TreatmentDuration(
        infection_type="HAP/VAP",
        infection_type_vi="Viêm phổi bệnh viện/Viêm phổi liên quan thở máy",
        standard_duration="7 ngày",
        short_duration="5-7 ngày (nếu đáp ứng tốt)",
        extended_duration="10-14 ngày (nếu có biến chứng, áp xe, hoặc vi khuẩn đặc biệt)",
        criteria=[
            "Đáp ứng lâm sàng tốt",
            "Cấy đờm/BAL âm tính hoặc cải thiện",
            "Không có biến chứng"
        ],
        notes="IDSA/ATS 2016 khuyến cáo 7 ngày cho đa số trường hợp"
    ),
    TreatmentDuration(
        infection_type="UTI - Uncomplicated",
        infection_type_vi="Nhiễm khuẩn đường tiết niệu - Không biến chứng",
        standard_duration="3-5 ngày",
        short_duration="3 ngày (fluoroquinolone hoặc TMP-SMX)",
        extended_duration="7-10 ngày (nếu có nguy cơ tái phát)",
        criteria=[
            "Phụ nữ trẻ, khỏe mạnh",
            "Không có bất thường giải phẫu",
            "Không có đặt catheter"
        ]
    ),
    TreatmentDuration(
        infection_type="UTI - Complicated",
        infection_type_vi="Nhiễm khuẩn đường tiết niệu - Có biến chứng",
        standard_duration="7-14 ngày",
        extended_duration="14-21 ngày (nếu có áp xe, viêm thận-bể thận nặng)",
        criteria=[
            "Nam giới",
            "Có bất thường giải phẫu",
            "Có đặt catheter",
            "Suy giảm miễn dịch"
        ]
    ),
    TreatmentDuration(
        infection_type="SSTI",
        infection_type_vi="Nhiễm khuẩn da và mô mềm",
        standard_duration="5-10 ngày",
        short_duration="5-7 ngày (nếu nhẹ, đáp ứng tốt)",
        extended_duration="10-14 ngày (nếu nặng, có hoại tử, hoặc viêm cân mạc)",
        criteria=[
            "Mức độ nặng",
            "Có hoại tử",
            "Viêm cân mạc"
        ]
    ),
    TreatmentDuration(
        infection_type="Sepsis/Bacteremia",
        infection_type_vi="Nhiễm trùng huyết/Nhiễm khuẩn huyết",
        standard_duration="7-14 ngày",
        short_duration="7 ngày (nếu cấy máu âm tính và đáp ứng tốt)",
        extended_duration="14-21 ngày (nếu có nguồn nhiễm trùng khó điều trị, viêm nội tâm mạc)",
        criteria=[
            "Cấy máu âm tính",
            "Không có nguồn nhiễm trùng còn lại",
            "Đáp ứng lâm sàng tốt"
        ],
        notes="Thời gian điều trị phụ thuộc vào nguồn nhiễm trùng và đáp ứng lâm sàng"
    ),
    TreatmentDuration(
        infection_type="Osteomyelitis",
        infection_type_vi="Viêm tủy xương",
        standard_duration="4-6 tuần (IV) + tiếp tục PO",
        extended_duration="6-12 tuần (nếu nặng hoặc khó điều trị)",
        criteria=[
            "Mức độ lan rộng",
            "Vi khuẩn kháng thuốc",
            "Có vật liệu ghép"
        ],
        notes="Cần điều trị dài ngày, thường bắt đầu IV sau đó chuyển PO"
    ),
    TreatmentDuration(
        infection_type="Endocarditis",
        infection_type_vi="Viêm nội tâm mạc",
        standard_duration="4-6 tuần",
        extended_duration="6 tuần hoặc lâu hơn (nếu có biến chứng hoặc vi khuẩn kháng thuốc)",
        criteria=[
            "Loại van (tự nhiên vs nhân tạo)",
            "Vi khuẩn",
            "Có biến chứng"
        ],
        notes="Cần điều trị dài ngày, thường 4-6 tuần"
    ),
]


def get_treatment_duration_recommendations(infection_type: Optional[str] = None) -> List[TreatmentDuration]:
    """Lấy khuyến cáo thời gian điều trị"""
    if infection_type:
        return [d for d in TREATMENT_DURATION_RECOMMENDATIONS if d.infection_type == infection_type]
    return TREATMENT_DURATION_RECOMMENDATIONS


def render_treatment_duration_view():
    """Render UI cho treatment duration recommendations"""
    import streamlit as st
    
    st.markdown("### ⏱️ Khuyến cáo Thời gian Điều trị")
    st.caption("Thời gian điều trị kháng sinh theo từng loại nhiễm trùng")
    
    recommendations = get_treatment_duration_recommendations()
    
    for rec in recommendations:
        with st.expander(f"🦠 {rec.infection_type_vi} ({rec.infection_type})", expanded=False):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(f"**⏱️ Thời gian chuẩn:** {rec.standard_duration}")
                
                if rec.short_duration:
                    st.success(f"✅ **Rút ngắn:** {rec.short_duration}")
            
            with col2:
                if rec.extended_duration:
                    st.warning(f"⚠️ **Kéo dài:** {rec.extended_duration}")
            
            if rec.criteria:
                st.markdown("**📋 Tiêu chí:**")
                for criterion in rec.criteria:
                    st.markdown(f"- {criterion}")
            
            if rec.notes:
                st.info(f"💡 **Lưu ý:** {rec.notes}")
        
        st.markdown("---")
    
    # General principles
    st.markdown("### 📋 Nguyên tắc chung")
    st.markdown("""
    1. **Đánh giá đáp ứng lâm sàng**: Rút ngắn thời gian nếu đáp ứng tốt
    2. **Dựa vào bằng chứng**: Tuân theo guideline mới nhất (IDSA/ATS)
    3. **Tránh điều trị quá dài**: Điều trị dài không cần thiết làm tăng nguy cơ kháng thuốc
    4. **Xem xét từng trường hợp**: Điều chỉnh theo tình trạng bệnh nhân cụ thể
    5. **Theo dõi và đánh giá**: Đánh giá lại định kỳ để quyết định thời gian điều trị
    """)
    
    st.markdown("---")
    
    # Benefits of shorter duration
    st.markdown("### 💡 Lợi ích của điều trị ngắn ngày")
    st.markdown("""
    - ✅ Giảm nguy cơ kháng thuốc
    - ✅ Giảm tác dụng phụ
    - ✅ Giảm chi phí điều trị
    - ✅ Giảm nguy cơ nhiễm khuẩn bệnh viện (C. difficile)
    - ✅ Cải thiện chất lượng cuộc sống bệnh nhân
    """)
