"""
Toxicity Management Module
Hướng dẫn xử trí độc tính và tác dụng phụ nặng của kháng sinh
"""

import streamlit as st
from typing import Dict, List, Optional
from .antibiotics_data import ANTIBIOTICS_DATABASE


# Toxicity management guidelines
TOXICITY_MANAGEMENT = {
    "Vancomycin": {
        "nephrotoxicity": {
            "symptoms": [
                "Giảm lượng nước tiểu",
                "Tăng creatinine",
                "Phù",
                "Mệt mỏi"
            ],
            "monitoring": [
                "Theo dõi creatinine hàng ngày",
                "Theo dõi lượng nước tiểu",
                "Theo dõi nồng độ vancomycin trong máu (trough 15-20 mg/L)"
            ],
            "management": [
                "Ngừng hoặc giảm liều vancomycin",
                "Điều chỉnh liều theo CrCl",
                "Đảm bảo đủ dịch",
                "Tránh các thuốc độc thận khác (aminoglycosides, NSAIDs)",
                "Xem xét chuyển sang kháng sinh khác nếu cần"
            ],
            "prevention": [
                "Duy trì trough level < 20 mg/L",
                "Tránh phối hợp với aminoglycosides",
                "Đảm bảo đủ dịch",
                "Theo dõi chức năng thận thường xuyên"
            ]
        },
        "ototoxicity": {
            "symptoms": [
                "Ù tai",
                "Giảm thính lực",
                "Chóng mặt",
                "Mất thăng bằng"
            ],
            "monitoring": [
                "Hỏi bệnh nhân về triệu chứng",
                "Test thính lực nếu có triệu chứng",
                "Theo dõi nồng độ vancomycin"
            ],
            "management": [
                "Ngừng vancomycin ngay lập tức",
                "Đánh giá mức độ tổn thương",
                "Chuyển sang kháng sinh khác",
                "Tư vấn chuyên khoa Tai Mũi Họng"
            ],
            "prevention": [
                "Duy trì trough level < 20 mg/L",
                "Tránh phối hợp với aminoglycosides",
                "Theo dõi triệu chứng thường xuyên"
            ]
        },
        "red_man_syndrome": {
            "symptoms": [
                "Đỏ da mặt, cổ, ngực",
                "Ngứa",
                "Hạ huyết áp",
                "Nhịp tim nhanh"
            ],
            "monitoring": [
                "Theo dõi trong quá trình truyền",
                "Theo dõi huyết áp, mạch"
            ],
            "management": [
                "Ngừng truyền ngay",
                "Truyền dịch",
                "Dùng antihistamine (diphenhydramine)",
                "Giảm tốc độ truyền khi tiếp tục",
                "Pre-medicate với antihistamine cho các liều sau"
            ],
            "prevention": [
                "Truyền chậm (≥ 60 phút)",
                "Pre-medicate với antihistamine",
                "Theo dõi trong quá trình truyền"
            ]
        }
    },
    "Aminoglycosides": {
        "nephrotoxicity": {
            "symptoms": [
                "Giảm lượng nước tiểu",
                "Tăng creatinine",
                "Tăng BUN",
                "Rối loạn điện giải"
            ],
            "monitoring": [
                "Creatinine hàng ngày",
                "Lượng nước tiểu",
                "Điện giải đồ",
                "Nồng độ aminoglycoside (peak/trough)"
            ],
            "management": [
                "Ngừng aminoglycoside",
                "Điều chỉnh liều theo CrCl",
                "Đảm bảo đủ dịch",
                "Tránh các thuốc độc thận khác",
                "Xem xét chuyển sang kháng sinh khác"
            ],
            "prevention": [
                "Dùng liều một lần/ngày (ODD)",
                "Theo dõi nồng độ (peak/trough)",
                "Tránh phối hợp với vancomycin",
                "Điều chỉnh liều theo CrCl",
                "Theo dõi creatinine thường xuyên"
            ]
        },
        "ototoxicity": {
            "symptoms": [
                "Ù tai",
                "Giảm thính lực",
                "Chóng mặt",
                "Mất thăng bằng"
            ],
            "monitoring": [
                "Hỏi bệnh nhân về triệu chứng",
                "Test thính lực baseline và định kỳ",
                "Theo dõi nồng độ aminoglycoside"
            ],
            "management": [
                "Ngừng aminoglycoside ngay",
                "Đánh giá mức độ tổn thương",
                "Chuyển sang kháng sinh khác",
                "Tư vấn chuyên khoa Tai Mũi Họng",
                "⚠️ Tổn thương có thể không hồi phục"
            ],
            "prevention": [
                "Dùng liều một lần/ngày",
                "Theo dõi nồng độ",
                "Tránh phối hợp với vancomycin",
                "Test thính lực baseline ở bệnh nhân nguy cơ cao"
            ]
        }
    },
    "Fluoroquinolones": {
        "tendon_rupture": {
            "symptoms": [
                "Đau gân",
                "Sưng gân",
                "Đứt gân (đặc biệt gân Achilles)",
                "Khó đi lại"
            ],
            "monitoring": [
                "Hỏi bệnh nhân về đau gân",
                "Khám lâm sàng gân",
                "Siêu âm gân nếu nghi ngờ"
            ],
            "management": [
                "Ngừng fluoroquinolone ngay",
                "Nghỉ ngơi, không vận động",
                "Chườm lạnh",
                "Nâng cao chân",
                "Tư vấn chuyên khoa Chấn thương chỉnh hình",
                "⚠️ Nguy cơ cao ở người cao tuổi, dùng corticosteroid"
            ],
            "prevention": [
                "Tránh dùng ở người cao tuổi",
                "Tránh dùng ở người dùng corticosteroid",
                "Tránh vận động mạnh khi dùng",
                "Theo dõi triệu chứng đau gân"
            ]
        },
        "qt_prolongation": {
            "symptoms": [
                "Chóng mặt",
                "Ngất",
                "Đánh trống ngực",
                "Rối loạn nhịp tim"
            ],
            "monitoring": [
                "ECG baseline và định kỳ",
                "Theo dõi QT interval",
                "Theo dõi triệu chứng"
            ],
            "management": [
                "Ngừng fluoroquinolone",
                "ECG ngay",
                "Theo dõi tim mạch",
                "Tránh các thuốc kéo dài QT khác",
                "Xem xét chuyển sang kháng sinh khác"
            ],
            "prevention": [
                "ECG baseline ở bệnh nhân nguy cơ",
                "Tránh phối hợp với thuốc kéo dài QT",
                "Tránh dùng ở bệnh nhân có QT kéo dài",
                "Theo dõi ECG định kỳ"
            ]
        },
        "cns_toxicity": {
            "symptoms": [
                "Co giật",
                "Lo âu",
                "Hoang tưởng",
                "Mất ngủ",
                "Chóng mặt"
            ],
            "monitoring": [
                "Theo dõi triệu chứng thần kinh",
                "Hỏi bệnh nhân về thay đổi hành vi"
            ],
            "management": [
                "Ngừng fluoroquinolone",
                "Xử trí co giật nếu có",
                "Theo dõi thần kinh",
                "Chuyển sang kháng sinh khác"
            ],
            "prevention": [
                "Tránh dùng ở bệnh nhân có tiền sử co giật",
                "Giảm liều ở bệnh nhân suy thận",
                "Theo dõi triệu chứng"
            ]
        }
    },
    "Linezolid": {
        "myelosuppression": {
            "symptoms": [
                "Giảm tiểu cầu",
                "Giảm bạch cầu",
                "Thiếu máu",
                "Chảy máu",
                "Nhiễm trùng"
            ],
            "monitoring": [
                "Công thức máu hàng tuần",
                "Theo dõi triệu chứng chảy máu",
                "Theo dõi dấu hiệu nhiễm trùng"
            ],
            "management": [
                "Ngừng linezolid",
                "Truyền tiểu cầu nếu cần",
                "Theo dõi công thức máu",
                "Chuyển sang kháng sinh khác",
                "⚠️ Thường hồi phục sau khi ngừng thuốc"
            ],
            "prevention": [
                "Công thức máu baseline",
                "Theo dõi hàng tuần",
                "Tránh dùng > 14 ngày nếu có thể",
                "Theo dõi triệu chứng"
            ]
        },
        "serotonin_syndrome": {
            "symptoms": [
                "Kích động",
                "Lú lẫn",
                "Tăng thân nhiệt",
                "Co cứng cơ",
                "Run"
            ],
            "monitoring": [
                "Theo dõi triệu chứng thần kinh",
                "Theo dõi nhiệt độ",
                "Hỏi về các thuốc đang dùng"
            ],
            "management": [
                "Ngừng linezolid ngay",
                "Ngừng các thuốc tăng serotonin",
                "Hỗ trợ hô hấp nếu cần",
                "Hạ nhiệt",
                "Benzodiazepine cho kích động",
                "Cyproheptadine nếu nặng"
            ],
            "prevention": [
                "Tránh phối hợp với SSRI, SNRI, MAOI",
                "Tránh phối hợp với tramadol, meperidine",
                "Theo dõi triệu chứng",
                "Giáo dục bệnh nhân về triệu chứng"
            ]
        }
    },
    "Colistin": {
        "nephrotoxicity": {
            "symptoms": [
                "Giảm lượng nước tiểu",
                "Tăng creatinine",
                "Suy thận cấp"
            ],
            "monitoring": [
                "Creatinine hàng ngày",
                "Lượng nước tiểu",
                "Điện giải đồ"
            ],
            "management": [
                "Ngừng colistin",
                "Điều chỉnh liều theo CrCl",
                "Đảm bảo đủ dịch",
                "Xem xét lọc máu nếu cần",
                "Chuyển sang kháng sinh khác"
            ],
            "prevention": [
                "Điều chỉnh liều theo CrCl",
                "Theo dõi creatinine thường xuyên",
                "Tránh phối hợp với thuốc độc thận",
                "Dùng liều loading đúng"
            ]
        },
        "neurotoxicity": {
            "symptoms": [
                "Yếu cơ",
                "Tê bì",
                "Khó thở (liệt cơ hô hấp)",
                "Chóng mặt"
            ],
            "monitoring": [
                "Theo dõi triệu chứng thần kinh",
                "Theo dõi chức năng hô hấp",
                "Hỏi bệnh nhân về yếu cơ"
            ],
            "management": [
                "Ngừng colistin ngay",
                "Hỗ trợ hô hấp nếu cần",
                "Theo dõi thần kinh",
                "Chuyển sang kháng sinh khác"
            ],
            "prevention": [
                "Giảm liều ở bệnh nhân suy thận",
                "Theo dõi triệu chứng",
                "Tránh dùng ở bệnh nhân có bệnh thần kinh cơ"
            ]
        }
    }
}


def get_toxicity_info(antibiotic_name: str, toxicity_type: Optional[str] = None) -> Optional[Dict]:
    """Get toxicity management information"""
    if antibiotic_name not in TOXICITY_MANAGEMENT:
        return None
    
    toxicity_data = TOXICITY_MANAGEMENT[antibiotic_name]
    
    if toxicity_type:
        return toxicity_data.get(toxicity_type)
    
    return toxicity_data


def render_toxicity_management(antibiotic_name: str):
    """Render toxicity management UI for an antibiotic"""
    
    st.markdown("---")
    st.markdown("### ⚠️ Xử Trí Độc Tính")
    
    toxicity_data = get_toxicity_info(antibiotic_name)
    
    if not toxicity_data:
        st.info(f"💡 Thông tin xử trí độc tính cho {antibiotic_name} đang được cập nhật.")
        return
    
    st.markdown(f"#### {antibiotic_name} - Hướng Dẫn Xử Trí Độc Tính")
    
    # List all toxicity types
    for toxicity_type, info in toxicity_data.items():
        toxicity_name_vi = {
            "nephrotoxicity": "Độc Thận",
            "ototoxicity": "Độc Tai",
            "red_man_syndrome": "Hội Chứng Đỏ Người",
            "tendon_rupture": "Đứt Gân",
            "qt_prolongation": "QT Kéo Dài",
            "cns_toxicity": "Độc Thần Kinh",
            "myelosuppression": "Ức Chế Tủy Xương",
            "serotonin_syndrome": "Hội Chứng Serotonin",
            "neurotoxicity": "Độc Thần Kinh"
        }.get(toxicity_type, toxicity_type.title())
        
        with st.expander(f"⚠️ {toxicity_name_vi}", expanded=False):
            # Symptoms
            if "symptoms" in info:
                st.markdown("**Triệu chứng:**")
                for symptom in info["symptoms"]:
                    st.markdown(f"- {symptom}")
            
            st.markdown("---")
            
            # Monitoring
            if "monitoring" in info:
                st.markdown("**Theo dõi:**")
                for item in info["monitoring"]:
                    st.markdown(f"- {item}")
            
            st.markdown("---")
            
            # Management
            if "management" in info:
                st.markdown("**Xử trí:**")
                for item in info["management"]:
                    if item.startswith("⚠️"):
                        st.warning(item)
                    else:
                        st.markdown(f"- {item}")
            
            st.markdown("---")
            
            # Prevention
            if "prevention" in info:
                st.markdown("**Phòng ngừa:**")
                for item in info["prevention"]:
                    st.markdown(f"- {item}")


def render_toxicity_checker():
    """Render Toxicity Management Checker UI"""
    
    st.markdown("### ⚠️ Xử Trí Độc Tính Kháng Sinh")
    st.caption("Hướng dẫn xử trí độc tính và tác dụng phụ nặng")
    
    st.warning("""
    **⚠️ Cảnh báo:**
    - Đây là hướng dẫn xử trí độc tính nặng
    - Luôn ưu tiên an toàn bệnh nhân
    - Ngừng thuốc ngay khi có dấu hiệu độc tính nặng
    - Tư vấn chuyên khoa khi cần
    """)
    
    # Antibiotic selection
    antibiotic_name = st.selectbox(
        "Chọn kháng sinh:",
        options=sorted(list(ANTIBIOTICS_DATABASE.keys())),
        key="toxicity_ab"
    )
    
    if st.button("⚠️ Xem Hướng Dẫn Xử Trí", type="primary", use_container_width=True):
        render_toxicity_management(antibiotic_name)
    
    # Quick reference
    st.markdown("---")
    st.markdown("#### 📋 Tài Liệu Tham Khảo")
    st.info("""
    **Nguồn:**
    - Micromedex Toxicity Management
    - UpToDate Drug Toxicity
    - ASHP Handbook on Injectable Drugs
    - Clinical Practice Guidelines
    
    **Lưu ý:**
    - Thông tin này chỉ mang tính tham khảo
    - Luôn tuân theo protocol của bệnh viện
    - Tư vấn chuyên khoa khi cần
    """)


__all__ = [
    'get_toxicity_info',
    'render_toxicity_management',
    'render_toxicity_checker',
]
