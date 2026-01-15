"""
Vietnamese-Specific Protocols and Guidelines
Local guidelines, drug availability, and regional considerations
"""

import streamlit as st
from components.ui.alerts import render_info_alert, render_warning_alert


# Common drugs available in Vietnam
VIETNAM_DRUG_AVAILABILITY = {
    "Vasopressors": {
        "Norepinephrine": {
            "available": True,
            "brands": ["Levophed", "Generic"],
            "notes": "Có sẵn tại hầu hết bệnh viện"
        },
        "Epinephrine": {
            "available": True,
            "brands": ["Adrenaline", "Generic"],
            "notes": "Có sẵn, dùng trong cấp cứu"
        },
        "Dopamine": {
            "available": True,
            "brands": ["Dopamine", "Generic"],
            "notes": "Có sẵn, ít dùng hơn norepinephrine"
        },
        "Vasopressin": {
            "available": False,
            "brands": [],
            "notes": "Không có sẵn tại nhiều bệnh viện. Thay thế: Norepinephrine + Dobutamine"
        }
    },
    "Sedation": {
        "Propofol": {
            "available": True,
            "brands": ["Diprivan", "Propofol", "Generic"],
            "notes": "Có sẵn, giá cao"
        },
        "Midazolam": {
            "available": True,
            "brands": ["Dormicum", "Midazolam", "Generic"],
            "notes": "Có sẵn, giá hợp lý"
        },
        "Dexmedetomidine": {
            "available": False,
            "brands": [],
            "notes": "Không có sẵn tại nhiều bệnh viện. Thay thế: Midazolam + Fentanyl"
        }
    },
    "Analgesia": {
        "Fentanyl": {
            "available": True,
            "brands": ["Fentanyl", "Generic"],
            "notes": "Có sẵn"
        },
        "Morphine": {
            "available": True,
            "brands": ["Morphine", "Generic"],
            "notes": "Có sẵn, giá rẻ"
        },
        "Remifentanil": {
            "available": False,
            "brands": [],
            "notes": "Không có sẵn. Thay thế: Fentanyl"
        }
    },
    "Antibiotics": {
        "Vancomycin": {
            "available": True,
            "brands": ["Vancomycin", "Generic"],
            "notes": "Có sẵn, cần theo dõi nồng độ"
        },
        "Piperacillin/Tazobactam": {
            "available": True,
            "brands": ["Tazocin", "Generic"],
            "notes": "Có sẵn"
        },
        "Meropenem": {
            "available": True,
            "brands": ["Meronem", "Generic"],
            "notes": "Có sẵn, giá cao"
        },
        "Linezolid": {
            "available": False,
            "brands": [],
            "notes": "Không có sẵn. Thay thế: Vancomycin"
        }
    }
}


# Drug alternatives when unavailable
DRUG_ALTERNATIVES = {
    "Vasopressin": {
        "alternatives": [
            "Norepinephrine (tăng liều)",
            "Norepinephrine + Dobutamine",
            "Epinephrine (nếu sốc nặng)"
        ],
        "notes": "Vasopressin không có sẵn, dùng norepinephrine là lựa chọn đầu tiên"
    },
    "Dexmedetomidine": {
        "alternatives": [
            "Midazolam + Fentanyl (để đạt mục tiêu RASS tương tự)",
            "Propofol (nếu ngắn hạn)",
            "Midazolam đơn thuần"
        ],
        "notes": "Dexmedetomidine không có sẵn, dùng midazolam + fentanyl"
    },
    "Remifentanil": {
        "alternatives": [
            "Fentanyl (liều tương đương)",
            "Morphine (nếu không có fentanyl)"
        ],
        "notes": "Remifentanil không có sẵn, dùng fentanyl"
    },
    "Linezolid": {
        "alternatives": [
            "Vancomycin (cho MRSA)",
            "Teicoplanin (nếu có)",
            "Daptomycin (nếu có)"
        ],
        "notes": "Linezolid không có sẵn, dùng vancomycin"
    }
}


def render_drug_availability():
    """Render drug availability checker"""
    st.subheader("💊 Kiểm tra thuốc có sẵn tại Việt Nam")
    st.caption("Thông tin về thuốc có sẵn và thay thế khi thiếu")
    
    st.markdown("---")
    
    # Category selection
    category = st.selectbox(
        "Chọn nhóm thuốc:",
        list(VIETNAM_DRUG_AVAILABILITY.keys()),
        key="viet_drug_category"
    )
    
    if category:
        st.markdown(f"### {category}")
        
        for drug, info in VIETNAM_DRUG_AVAILABILITY[category].items():
            with st.expander(drug):
                if info["available"]:
                    st.success(f"✅ **Có sẵn**")
                    st.markdown(f"**Nhãn hiệu:** {', '.join(info['brands'])}")
                else:
                    st.error(f"❌ **Không có sẵn**")
                    
                    # Show alternatives
                    if drug in DRUG_ALTERNATIVES:
                        st.markdown("**Thay thế:**")
                        for alt in DRUG_ALTERNATIVES[drug]["alternatives"]:
                            st.markdown(f"- {alt}")
                        st.info(f"**Ghi chú:** {DRUG_ALTERNATIVES[drug]['notes']}")
                
                if info.get("notes"):
                    st.caption(info["notes"])


def render_cost_considerations():
    """Render cost considerations"""
    st.subheader("💰 Cân nhắc chi phí")
    st.caption("Hướng dẫn lựa chọn thuốc dựa trên chi phí")
    
    st.markdown("""
    **Nguyên tắc:**
    - Ưu tiên hiệu quả và an toàn
    - Cân nhắc chi phí khi có nhiều lựa chọn tương đương
    - Thảo luận với gia đình về chi phí khi cần
    """)
    
    st.markdown("---")
    
    cost_categories = {
        "Sedation": {
            "High cost": ["Propofol", "Dexmedetomidine (nếu có)"],
            "Medium cost": ["Midazolam"],
            "Low cost": ["Morphine"]
        },
        "Vasopressors": {
            "High cost": ["Vasopressin (nếu có)"],
            "Medium cost": ["Norepinephrine", "Epinephrine"],
            "Low cost": ["Dopamine"]
        },
        "Antibiotics": {
            "High cost": ["Meropenem", "Linezolid (nếu có)"],
            "Medium cost": ["Piperacillin/Tazobactam", "Vancomycin"],
            "Low cost": ["Ceftriaxone", "Cefepime"]
        }
    }
    
    for category, costs in cost_categories.items():
        st.markdown(f"#### {category}")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("**💰 Chi phí cao:**")
            for drug in costs["High cost"]:
                st.markdown(f"- {drug}")
        
        with col2:
            st.markdown("**💰💰 Chi phí trung bình:**")
            for drug in costs["Medium cost"]:
                st.markdown(f"- {drug}")
        
        with col3:
            st.markdown("**💰💰💰 Chi phí thấp:**")
            for drug in costs["Low cost"]:
                st.markdown(f"- {drug}")
        
        st.markdown("---")


def render_local_guidelines():
    """Render local guidelines placeholder"""
    st.subheader("📋 Hướng dẫn địa phương")
    st.caption("Hướng dẫn từ Bộ Y tế Việt Nam và bệnh viện")
    
    st.info("""
    **Tính năng đang phát triển:**
    - Tích hợp hướng dẫn từ Bộ Y tế Việt Nam
    - Protocol từ các bệnh viện lớn
    - Regional variations
    - Customizable hospital-specific protocols
    """)
    
    st.markdown("---")
    
    st.markdown("### 📚 Tài liệu tham khảo")
    
    references = [
        "Bộ Y tế Việt Nam - Hướng dẫn điều trị (nếu có)",
        "Bệnh viện Bạch Mai - Protocol ICU",
        "Bệnh viện Chợ Rẫy - Protocol ICU",
        "Bệnh viện 108 - Protocol ICU",
        "Hội Hồi sức Cấp cứu và Chống độc Việt Nam"
    ]
    
    for ref in references:
        st.markdown(f"- {ref}")


def render_bilingual_glossary():
    """Render bilingual medical terminology glossary"""
    st.subheader("📖 Từ điển thuật ngữ y khoa")
    st.caption("Thuật ngữ tiếng Việt và tiếng Anh")
    
    st.markdown("---")
    
    glossary = {
        "Hô hấp": {
            "Ventilator": "Máy thở",
            "Tidal Volume": "Thể tích khí lưu thông",
            "PEEP": "Áp lực dương cuối thì thở ra",
            "FiO2": "Nồng độ oxy trong khí thở vào",
            "Plateau Pressure": "Áp lực cao nguyên",
            "Driving Pressure": "Áp lực đẩy",
            "Compliance": "Độ giãn nở",
            "ARDS": "Hội chứng suy hô hấp cấp"
        },
        "Huyết động": {
            "MAP": "Huyết áp trung bình",
            "CVP": "Áp lực tĩnh mạch trung tâm",
            "Cardiac Output": "Cung lượng tim",
            "Cardiac Index": "Chỉ số tim",
            "SVR": "Sức cản mạch hệ thống",
            "SVV": "Biến thiên thể tích nhát bóp",
            "PPV": "Biến thiên áp lực mạch"
        },
        "An thần": {
            "RASS": "Thang đánh giá kích động-an thần Richmond",
            "CAM-ICU": "Phương pháp đánh giá mê sảng trong ICU",
            "Sedation": "An thần",
            "Analgesia": "Giảm đau",
            "Delirium": "Mê sảng"
        },
        "Đánh giá": {
            "APACHE": "Hệ thống đánh giá sinh lý bệnh cấp tính và bệnh mạn tính",
            "SOFA": "Đánh giá suy cơ quan tuần tự",
            "SAPS": "Hệ thống đánh giá sinh lý đơn giản",
            "GCS": "Thang điểm hôn mê Glasgow",
            "AKI": "Suy thận cấp"
        }
    }
    
    category = st.selectbox(
        "Chọn chủ đề:",
        list(glossary.keys()),
        key="glossary_category"
    )
    
    if category:
        st.markdown(f"### {category}")
        
        for eng_term, viet_term in glossary[category].items():
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"**{eng_term}**")
            with col2:
                st.markdown(f"{viet_term}")


def render_vietnamese_protocols():
    """Main function to render Vietnamese-specific protocols"""
    st.header("🇻🇳 Hướng dẫn đặc thù Việt Nam")
    st.caption("Thuốc có sẵn, thay thế, và hướng dẫn địa phương")
    
    tabs = st.tabs([
        "💊 Thuốc có sẵn",
        "💰 Chi phí",
        "📋 Hướng dẫn địa phương",
        "📖 Từ điển"
    ])
    
    with tabs[0]:
        render_drug_availability()
    
    with tabs[1]:
        render_cost_considerations()
    
    with tabs[2]:
        render_local_guidelines()
    
    with tabs[3]:
        render_bilingual_glossary()
