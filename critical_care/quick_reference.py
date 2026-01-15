"""
Quick Reference Guides for Critical Care
Nursing and physician quick reference guides
"""

import streamlit as st
from components.ui.alerts import render_info_alert, render_warning_alert


# Normal ranges
NORMAL_RANGES = {
    "Vital Signs": {
        "HR": "60-100 /min",
        "BP": "90-140/60-90 mmHg",
        "MAP": "70-100 mmHg",
        "RR": "12-20 /min",
        "SpO2": ">95%",
        "Temp": "36.5-37.5°C"
    },
    "ABG": {
        "pH": "7.35-7.45",
        "PaCO2": "35-45 mmHg",
        "PaO2": "80-100 mmHg",
        "HCO3": "22-26 mEq/L",
        "BE": "-2 to +2 mEq/L",
        "SaO2": ">95%"
    },
    "Ventilator": {
        "Vt": "6-8 mL/kg IBW",
        "RR": "12-20 /min",
        "PEEP": "5-10 cmH2O",
        "FiO2": "21-100%",
        "Plateau": "≤30 cmH2O",
        "Driving P": "≤15 cmH2O",
        "I:E": "1:2"
    },
    "Hemodynamics": {
        "CVP": "2-8 mmHg",
        "PAWP": "8-12 mmHg",
        "CO": "4-8 L/min",
        "CI": "2.5-4 L/min/m²",
        "SVR": "800-1200 dynes·s/cm⁵",
        "PVR": "100-250 dynes·s/cm⁵"
    },
    "Labs": {
        "Na": "135-145 mEq/L",
        "K": "3.5-5.0 mEq/L",
        "Cl": "98-107 mEq/L",
        "HCO3": "22-26 mEq/L",
        "BUN": "7-20 mg/dL",
        "Cr": "0.6-1.2 mg/dL",
        "Glucose": "70-100 mg/dL",
        "Lactate": "<2 mmol/L",
        "Hb": "12-16 g/dL (F), 14-18 g/dL (M)",
        "Hct": "36-48% (F), 42-52% (M)",
        "Platelets": "150-400 K/μL",
        "PT": "11-13 sec",
        "PTT": "25-35 sec",
        "INR": "0.9-1.1"
    }
}


# Common ICU drug infusions
COMMON_ICU_DRUGS = {
    "Vasopressors": {
        "Norepinephrine": {
            "dose": "0.05-2 mcg/kg/min",
            "concentration": "4 mg/250 mL (16 mcg/mL)",
            "rate_mlh": "0.5-20 mL/h (70 kg)",
            "indication": "Sốc, hạ huyết áp",
            "monitor": "MAP, HR, lactate"
        },
        "Epinephrine": {
            "dose": "0.05-2 mcg/kg/min",
            "concentration": "1 mg/250 mL (4 mcg/mL)",
            "rate_mlh": "0.5-20 mL/h (70 kg)",
            "indication": "Sốc nặng, ngừng tim",
            "monitor": "MAP, HR, arrhythmias"
        },
        "Vasopressin": {
            "dose": "0.01-0.04 units/min",
            "concentration": "20 units/100 mL (0.2 units/mL)",
            "rate_mlh": "3-12 mL/h",
            "indication": "Sốc kháng catecholamine",
            "monitor": "MAP, Na+"
        },
        "Dopamine": {
            "dose": "2-20 mcg/kg/min",
            "concentration": "400 mg/250 mL (1.6 mg/mL)",
            "rate_mlh": "1-10 mL/h (70 kg)",
            "indication": "Sốc, nhịp chậm",
            "monitor": "MAP, HR, arrhythmias"
        }
    },
    "Inotropes": {
        "Dobutamine": {
            "dose": "2-20 mcg/kg/min",
            "concentration": "250 mg/250 mL (1 mg/mL)",
            "rate_mlh": "1-10 mL/h (70 kg)",
            "indication": "Suy tim, sốc tim",
            "monitor": "CO, MAP, HR"
        },
        "Milrinone": {
            "dose": "0.375-0.75 mcg/kg/min",
            "concentration": "20 mg/100 mL (200 mcg/mL)",
            "rate_mlh": "0.1-0.2 mL/h (70 kg)",
            "indication": "Suy tim, tăng áp phổi",
            "monitor": "CO, MAP, HR"
        }
    },
    "Sedation": {
        "Propofol": {
            "dose": "5-50 mcg/kg/min",
            "concentration": "1000 mg/100 mL (10 mg/mL)",
            "rate_mlh": "2-20 mL/h (70 kg)",
            "indication": "An thần ngắn hạn",
            "monitor": "RASS, MAP, triglycerides"
        },
        "Midazolam": {
            "dose": "0.02-0.1 mg/kg/h",
            "concentration": "50 mg/50 mL (1 mg/mL)",
            "rate_mlh": "1-5 mL/h (70 kg)",
            "indication": "An thần dài hạn",
            "monitor": "RASS, accumulation"
        },
        "Dexmedetomidine": {
            "dose": "0.2-1.5 mcg/kg/h",
            "concentration": "200 mcg/50 mL (4 mcg/mL)",
            "rate_mlh": "0.2-1.5 mL/h (70 kg)",
            "indication": "An thần nhẹ, cai máy thở",
            "monitor": "RASS, HR, BP"
        }
    },
    "Analgesia": {
        "Fentanyl": {
            "dose": "0.5-5 mcg/kg/h",
            "concentration": "1000 mcg/100 mL (10 mcg/mL)",
            "rate_mlh": "0.5-5 mL/h (70 kg)",
            "indication": "Giảm đau",
            "monitor": "Pain score, RR"
        },
        "Morphine": {
            "dose": "0.05-0.2 mg/kg/h",
            "concentration": "50 mg/50 mL (1 mg/mL)",
            "rate_mlh": "0.5-2 mL/h (70 kg)",
            "indication": "Giảm đau",
            "monitor": "Pain score, RR, histamine"
        }
    }
}


# Ventilator alarm troubleshooting
VENTILATOR_ALARMS = {
    "High Pressure": {
        "causes": [
            "Tắc ống NKQ (đờm, uốn cong)",
            "Bệnh nhân ho, gồng",
            "Compliance giảm (ARDS, phù phổi)",
            "PEEP cao",
            "Vt quá lớn"
        ],
        "actions": [
            "Kiểm tra ống NKQ - hút đờm",
            "Đánh giá bệnh nhân - an thần?",
            "Kiểm tra compliance",
            "Giảm Vt hoặc PEEP",
            "Xem xét giảm RR"
        ]
    },
    "Low Pressure": {
        "causes": [
            "Rò rỉ hệ thống",
            "Ống NKQ bị tuột",
            "Bóng chèn không đủ",
            "Disconnect"
        ],
        "actions": [
            "Kiểm tra tất cả kết nối",
            "Kiểm tra vị trí ống NKQ",
            "Kiểm tra bóng chèn",
            "Test leak"
        ]
    },
    "Low Minute Ventilation": {
        "causes": [
            "Rò rỉ",
            "Bệnh nhân tự thở yếu",
            "Apnea",
            "Disconnect"
        ],
        "actions": [
            "Kiểm tra rò rỉ",
            "Đánh giá bệnh nhân",
            "Tăng backup rate",
            "Kiểm tra kết nối"
        ]
    },
    "High FiO2": {
        "causes": [
            "SpO2 thấp",
            "PEEP thấp",
            "ARDS",
            "Shunt"
        ],
        "actions": [
            "Tăng PEEP",
            "Đánh giá ABG",
            "Xem xét ARDS protocol",
            "Kiểm tra vị trí ống NKQ"
        ]
    },
    "Apnea": {
        "causes": [
            "Bệnh nhân ngừng thở",
            "An thần quá sâu",
            "Disconnect",
            "Apnea time quá ngắn"
        ],
        "actions": [
            "Đánh giá bệnh nhân ngay",
            "Kiểm tra kết nối",
            "Tăng backup rate",
            "Giảm an thần nếu quá sâu"
        ]
    }
}


def render_nursing_guide():
    """Render nursing quick reference guide"""
    st.header("👩‍⚕️ Hướng dẫn nhanh cho điều dưỡng")
    
    tabs = st.tabs([
        "📊 Giá trị bình thường",
        "💉 Thuốc truyền thường dùng",
        "🚨 Xử lý báo động máy thở",
        "📋 Checklist hàng ngày"
    ])
    
    # Tab 1: Normal Ranges
    with tabs[0]:
        st.markdown("### 📊 Giá trị bình thường")
        
        for category, values in NORMAL_RANGES.items():
            with st.expander(category):
                for param, range_val in values.items():
                    st.markdown(f"**{param}:** {range_val}")
    
    # Tab 2: Common Drugs
    with tabs[1]:
        st.markdown("### 💉 Thuốc truyền thường dùng trong ICU")
        
        for category, drugs in COMMON_ICU_DRUGS.items():
            st.markdown(f"#### {category}")
            
            for drug, info in drugs.items():
                with st.expander(drug):
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.markdown(f"""
                        **Liều:** {info['dose']}  
                        **Nồng độ:** {info['concentration']}  
                        **Tốc độ:** {info['rate_mlh']}
                        """)
                    
                    with col2:
                        st.markdown(f"""
                        **Chỉ định:** {info['indication']}  
                        **Theo dõi:** {info['monitor']}
                        """)
            
            st.markdown("---")
    
    # Tab 3: Ventilator Alarms
    with tabs[2]:
        st.markdown("### 🚨 Xử lý báo động máy thở")
        
        for alarm, details in VENTILATOR_ALARMS.items():
            with st.expander(f"🚨 {alarm}"):
                st.markdown("**Nguyên nhân có thể:**")
                for cause in details['causes']:
                    st.markdown(f"- {cause}")
                
                st.markdown("**Hành động:**")
                for action in details['actions']:
                    st.markdown(f"1. {action}")
    
    # Tab 4: Daily Checklist
    with tabs[3]:
        st.markdown("### 📋 Checklist hàng ngày ICU")
        
        checklist_categories = {
            "Ventilator": [
                "Kiểm tra vị trí ống NKQ (độ sâu)",
                "Kiểm tra bóng chèn",
                "Đánh giá compliance",
                "Kiểm tra ABG (nếu có)",
                "Đánh giá sẵn sàng cai máy thở"
            ],
            "Sedation": [
                "Đánh giá RASS",
                "CAM-ICU (nếu RASS ≥ -3)",
                "Đánh giá mức độ đau",
                "Cân nhắc giảm an thần (SAT)"
            ],
            "Fluid & Hemodynamics": [
                "Tính cân bằng dịch 24h",
                "Đánh giá lượng nước tiểu",
                "Đánh giá MAP, CVP",
                "Kiểm tra dấu hiệu quá tải dịch"
            ],
            "Labs & Monitoring": [
                "Xem kết quả xét nghiệm",
                "Đánh giá điện giải",
                "Đánh giá chức năng thận",
                "Đánh giá chức năng gan",
                "Lactate (nếu sepsis)"
            ],
            "General": [
                "Đánh giá vị trí nằm (prone?)",
                "Kiểm tra vết loét tì đè",
                "Đánh giá dinh dưỡng",
                "Kiểm tra đường truyền",
                "Đánh giá nhiễm trùng"
            ]
        }
        
        for category, items in checklist_categories.items():
            st.markdown(f"#### {category}")
            for item in items:
                st.checkbox(item, key=f"nurse_check_{category}_{item}")
            st.markdown("---")


def render_physician_guide():
    """Render physician quick reference guide"""
    st.header("👨‍⚕️ Hướng dẫn nhanh cho bác sĩ")
    
    tabs = st.tabs([
        "🫁 Cài đặt máy thở ban đầu",
        "💉 Liều thuốc thường dùng",
        "📊 Scoring systems",
        "🔄 Workflow lâm sàng"
    ])
    
    # Tab 1: Initial Ventilator Settings
    with tabs[0]:
        st.markdown("### 🫁 Cài đặt máy thở ban đầu theo tình trạng")
        
        conditions = {
            "ARDS": {
                "mode": "AC hoặc VC",
                "vt": "6 mL/kg IBW",
                "rr": "12-20 /min",
                "peep": "8-12 cmH2O (theo PEEP/FiO2 table)",
                "fio2": "100% → giảm dần",
                "targets": "Plateau ≤30, Driving ≤15, P/F >200"
            },
            "COPD": {
                "mode": "AC hoặc PSV",
                "vt": "6-8 mL/kg IBW",
                "rr": "10-14 /min (cho phép tăng CO2)",
                "peep": "5-8 cmH2O (cẩn thận auto-PEEP)",
                "fio2": "Đủ để SpO2 >88%",
                "targets": "Cho phép hypercapnia nhẹ, tránh auto-PEEP"
            },
            "Asthma": {
                "mode": "AC",
                "vt": "6-8 mL/kg IBW",
                "rr": "10-14 /min",
                "peep": "5 cmH2O (tránh auto-PEEP)",
                "fio2": "Đủ để SpO2 >90%",
                "targets": "Tránh hyperinflation, cho phép hypercapnia"
            },
            "Post-op": {
                "mode": "AC hoặc SIMV",
                "vt": "8-10 mL/kg IBW",
                "rr": "12-16 /min",
                "peep": "5-8 cmH2O",
                "fio2": "40-60%",
                "targets": "Cai máy thở sớm nếu có thể"
            },
            "Sepsis/Shock": {
                "mode": "AC",
                "vt": "6-8 mL/kg IBW",
                "rr": "16-20 /min",
                "peep": "8-10 cmH2O",
                "fio2": "Đủ để SpO2 >94%",
                "targets": "Hỗ trợ huyết động, tránh barotrauma"
            }
        }
        
        condition = st.selectbox("Tình trạng:", list(conditions.keys()), key="vent_condition")
        
        if condition:
            settings = conditions[condition]
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(f"""
                **Mode:** {settings['mode']}  
                **Tidal Volume:** {settings['vt']}  
                **Respiratory Rate:** {settings['rr']}
                """)
            
            with col2:
                st.markdown(f"""
                **PEEP:** {settings['peep']}  
                **FiO2:** {settings['fio2']}
                """)
            
            st.info(f"**Mục tiêu:** {settings['targets']}")
    
    # Tab 2: Common Drug Doses
    with tabs[1]:
        st.markdown("### 💉 Liều thuốc thường dùng")
        
        drug_categories = {
            "Vasopressors": {
                "Norepinephrine": "0.05-2 mcg/kg/min (bắt đầu 0.1)",
                "Epinephrine": "0.05-2 mcg/kg/min",
                "Vasopressin": "0.01-0.04 units/min",
                "Dopamine": "2-20 mcg/kg/min"
            },
            "Sedation": {
                "Propofol": "5-50 mcg/kg/min (target RASS -1 to -2)",
                "Midazolam": "0.02-0.1 mg/kg/h",
                "Dexmedetomidine": "0.2-1.5 mcg/kg/h"
            },
            "Analgesia": {
                "Fentanyl": "0.5-5 mcg/kg/h",
                "Morphine": "0.05-0.2 mg/kg/h"
            },
            "Antibiotics (Loading)": {
                "Vancomycin": "15-20 mg/kg IV",
                "Piperacillin/Tazobactam": "4.5 g IV",
                "Meropenem": "1-2 g IV",
                "Ceftriaxone": "1-2 g IV"
            }
        }
        
        for category, drugs in drug_categories.items():
            st.markdown(f"#### {category}")
            for drug, dose in drugs.items():
                st.markdown(f"**{drug}:** {dose}")
            st.markdown("---")
    
    # Tab 3: Scoring Systems
    with tabs[2]:
        st.markdown("### 📊 Scoring Systems - Khi nào dùng")
        
        scoring_guide = {
            "APACHE II": {
                "when": "Vào ICU 24h đầu, tiên lượng tử vong",
                "frequency": "Một lần (24h đầu)",
                "link": "📊 Scoring Systems"
            },
            "SOFA": {
                "when": "Sepsis, đánh giá suy cơ quan, theo dõi tiến triển",
                "frequency": "Hàng ngày",
                "link": "📊 Scoring Systems"
            },
            "SAPS II": {
                "when": "Tiên lượng tử vong ICU (alternative to APACHE)",
                "frequency": "Một lần (24h đầu)",
                "link": "📊 Scoring Systems"
            },
            "GCS": {
                "when": "Chấn thương, đột quỵ, hôn mê",
                "frequency": "Thường xuyên (mỗi 1-4h)",
                "link": "📊 Scoring Systems"
            },
            "RASS": {
                "when": "Đánh giá mức độ an thần, mục tiêu RASS -1 to -2",
                "frequency": "Mỗi 4-8h, trước khi điều chỉnh an thần",
                "link": "📊 Scoring Systems"
            },
            "CAM-ICU": {
                "when": "Sàng lọc mê sảng ở ICU (khi RASS ≥ -3)",
                "frequency": "Hàng ngày, hoặc khi nghi ngờ",
                "link": "📊 Scoring Systems"
            }
        }
        
        for score, info in scoring_guide.items():
            with st.expander(score):
                st.markdown(f"**Khi nào dùng:** {info['when']}")
                st.markdown(f"**Tần suất:** {info['frequency']}")
                if st.button(f"Mở {score}", key=f"phys_score_{score}"):
                    st.session_state['critical_care_tool_selection'] = info['link']
                    st.rerun()
    
    # Tab 4: Clinical Workflow
    with tabs[3]:
        st.markdown("### 🔄 Workflow lâm sàng thường gặp")
        
        workflows = {
            "Bệnh nhân mới vào ICU": [
                "1. Đánh giá ABC (Airway, Breathing, Circulation)",
                "2. Đánh giá mức độ ý thức (GCS)",
                "3. Tính APACHE II / SOFA",
                "4. Đánh giá đường thở (cần NKQ?)",
                "5. Đánh giá huyết động (sốc?)",
                "6. Xét nghiệm cơ bản (ABG, lactate, CBC, BMP)",
                "7. Cài đặt máy thở (nếu cần)",
                "8. An thần (target RASS -1 to -2)",
                "9. Bù dịch / Vasopressor (nếu cần)"
            ],
            "Đánh giá hàng ngày": [
                "1. SOFA score",
                "2. RASS, CAM-ICU",
                "3. Cân bằng dịch 24h",
                "4. Đánh giá sẵn sàng cai máy thở",
                "5. Xem xét giảm an thần (SAT)",
                "6. Đánh giá nhiễm trùng",
                "7. Đánh giá dinh dưỡng",
                "8. Đánh giá vết loét tì đè"
            ],
            "Sepsis Protocol": [
                "1. Nhận diện (SIRS, qSOFA, SOFA)",
                "2. Lấy máu cấy, kháng sinh trong 1 giờ",
                "3. Bù dịch 30 mL/kg",
                "4. Vasopressor nếu MAP <65",
                "5. Đo lactate, theo dõi clearance",
                "6. Source control",
                "7. Đánh giá ARDS (nếu có)"
            ],
            "Cai máy thở": [
                "1. Đánh giá sẵn sàng (RSBI, GCS, strength)",
                "2. Spontaneous breathing trial (SBT)",
                "3. Đánh giá sau SBT (ABG, RR, HR, BP)",
                "4. Nếu đạt: Extubation",
                "5. Nếu không đạt: Tiếp tục thở máy, đánh giá lại sau 24h"
            ]
        }
        
        workflow = st.selectbox("Chọn workflow:", list(workflows.keys()), key="phys_workflow")
        
        if workflow:
            st.markdown(f"#### {workflow}")
            for step in workflows[workflow]:
                st.markdown(step)


def render_quick_reference():
    """Main function to render quick reference guides"""
    tabs = st.tabs([
        "👩‍⚕️ Điều dưỡng",
        "👨‍⚕️ Bác sĩ"
    ])
    
    with tabs[0]:
        render_nursing_guide()
    
    with tabs[1]:
        render_physician_guide()
