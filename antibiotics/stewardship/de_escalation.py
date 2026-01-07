"""
De-escalation Guidelines
Hướng dẫn giảm liều và đổi thuốc kháng sinh
"""

from typing import List, Dict, Optional
from dataclasses import dataclass


@dataclass
class DeEscalationGuideline:
    """Hướng dẫn de-escalation cho một loại nhiễm trùng"""
    infection_type: str
    infection_type_vi: str
    timing: str
    criteria: List[str]
    examples: List[str]
    notes: Optional[str] = None


DE_ESCALATION_GUIDELINES = [
    DeEscalationGuideline(
        infection_type="CAP",
        infection_type_vi="Viêm phổi cộng đồng",
        timing="Sau 48-72 giờ khi có kết quả cấy và đáp ứng lâm sàng tốt",
        criteria=[
            "Bệnh nhân cải thiện lâm sàng (afebrile ≥ 24h, giảm triệu chứng)",
            "Cấy máu/đờm âm tính hoặc vi khuẩn nhạy cảm với kháng sinh phổ hẹp hơn",
            "Không có nguy cơ nhiễm khuẩn đa kháng",
            "Có thể chuyển sang đường uống"
        ],
        examples=[
            "Từ Ceftriaxone + Azithromycin → Amoxicillin-clavulanate PO",
            "Từ Levofloxacin IV → Levofloxacin PO",
            "Từ Piperacillin-tazobactam → Amoxicillin-clavulanate PO (nếu không có Pseudomonas)"
        ],
        notes="De-escalation sớm giúp giảm nguy cơ kháng thuốc và chi phí điều trị"
    ),
    DeEscalationGuideline(
        infection_type="HAP/VAP",
        infection_type_vi="Viêm phổi bệnh viện/Viêm phổi liên quan thở máy",
        timing="Sau 48-72 giờ khi có kết quả cấy và đáp ứng lâm sàng",
        criteria=[
            "Bệnh nhân cải thiện lâm sàng",
            "Cấy đờm/BAL âm tính hoặc vi khuẩn nhạy cảm với kháng sinh phổ hẹp",
            "Không có nguy cơ MDR (Multi-drug resistant) pathogens",
            "Có thể chuyển từ phối hợp sang đơn trị"
        ],
        examples=[
            "Từ Piperacillin-tazobactam + Vancomycin → Piperacillin-tazobactam đơn trị (nếu không có MRSA)",
            "Từ Meropenem + Vancomycin → Ceftriaxone (nếu không có ESBL/KPC)",
            "Từ phối hợp → đơn trị khi cấy chỉ có một vi khuẩn nhạy cảm"
        ],
        notes="Đặc biệt quan trọng ở HAP/VAP để tránh kháng thuốc và nhiễm khuẩn bệnh viện"
    ),
    DeEscalationGuideline(
        infection_type="UTI",
        infection_type_vi="Nhiễm khuẩn đường tiết niệu",
        timing="Sau 24-48 giờ khi có kết quả cấy và đáp ứng lâm sàng",
        criteria=[
            "Bệnh nhân cải thiện triệu chứng",
            "Cấy nước tiểu có vi khuẩn nhạy cảm với kháng sinh phổ hẹp",
            "Có thể chuyển sang đường uống"
        ],
        examples=[
            "Từ Ceftriaxone IV → Ciprofloxacin PO hoặc Amoxicillin-clavulanate PO",
            "Từ Piperacillin-tazobactam → Ciprofloxacin PO (nếu nhạy cảm)",
            "Từ IV → PO khi bệnh nhân có thể uống được"
        ]
    ),
    DeEscalationGuideline(
        infection_type="Sepsis",
        infection_type_vi="Nhiễm trùng huyết",
        timing="Sau 48-72 giờ khi có kết quả cấy và đáp ứng lâm sàng",
        criteria=[
            "Bệnh nhân ổn định huyết động (không cần vasopressor)",
            "Cấy máu âm tính hoặc vi khuẩn nhạy cảm với kháng sinh phổ hẹp",
            "Không có nguồn nhiễm trùng còn lại",
            "Có thể chuyển sang đường uống"
        ],
        examples=[
            "Từ Meropenem + Vancomycin → Ceftriaxone (nếu không có ESBL/KPC/MRSA)",
            "Từ Piperacillin-tazobactam + Vancomycin → Amoxicillin-clavulanate PO (nếu không có MRSA)",
            "Từ phối hợp → đơn trị khi cấy chỉ có một vi khuẩn"
        ],
        notes="Cần thận trọng ở sepsis, đảm bảo bệnh nhân đã ổn định trước khi de-escalate"
    ),
    DeEscalationGuideline(
        infection_type="SSTI",
        infection_type_vi="Nhiễm khuẩn da và mô mềm",
        timing="Sau 48-72 giờ khi có kết quả cấy và đáp ứng lâm sàng",
        criteria=[
            "Vết thương cải thiện (giảm đỏ, sưng, mủ)",
            "Cấy mủ/vết thương có vi khuẩn nhạy cảm với kháng sinh phổ hẹp",
            "Có thể chuyển sang đường uống"
        ],
        examples=[
            "Từ Vancomycin IV → Clindamycin PO (nếu không có MRSA hoặc MRSA nhạy cảm clindamycin)",
            "Từ Piperacillin-tazobactam → Amoxicillin-clavulanate PO",
            "Từ phối hợp → đơn trị khi cấy chỉ có một vi khuẩn"
        ]
    ),
]


def get_de_escalation_guidelines(infection_type: Optional[str] = None) -> List[DeEscalationGuideline]:
    """Lấy hướng dẫn de-escalation"""
    if infection_type:
        return [g for g in DE_ESCALATION_GUIDELINES if g.infection_type == infection_type]
    return DE_ESCALATION_GUIDELINES


def render_de_escalation_view():
    """Render UI cho de-escalation guidelines"""
    import streamlit as st
    
    st.markdown("### 🔄 Hướng dẫn De-escalation")
    st.caption("Giảm liều và đổi thuốc kháng sinh khi có kết quả cấy và đáp ứng lâm sàng tốt")
    
    guidelines = get_de_escalation_guidelines()
    
    for guideline in guidelines:
        with st.expander(f"🦠 {guideline.infection_type_vi} ({guideline.infection_type})", expanded=False):
            st.markdown(f"**⏰ Thời điểm:** {guideline.timing}")
            
            st.markdown("**✅ Tiêu chí de-escalation:**")
            for criterion in guideline.criteria:
                st.markdown(f"- {criterion}")
            
            st.markdown("**💡 Ví dụ:**")
            for example in guideline.examples:
                st.markdown(f"- {example}")
            
            if guideline.notes:
                st.info(f"💡 **Lưu ý:** {guideline.notes}")
        
        st.markdown("---")
    
    # General principles
    st.markdown("### 📋 Nguyên tắc chung")
    st.markdown("""
    1. **Đánh giá đáp ứng lâm sàng**: Bệnh nhân phải cải thiện trước khi de-escalate
    2. **Dựa vào kết quả cấy**: Chỉ de-escalate khi có kết quả cấy và vi khuẩn nhạy cảm
    3. **Tránh de-escalate quá sớm**: Đợi ít nhất 48-72 giờ để đảm bảo đáp ứng
    4. **Xem xét nguy cơ**: Không de-escalate nếu vẫn có nguy cơ nhiễm khuẩn đa kháng
    5. **Chuyển IV → PO**: Khi có thể, chuyển sang đường uống để giảm chi phí và thời gian nằm viện
    """)
