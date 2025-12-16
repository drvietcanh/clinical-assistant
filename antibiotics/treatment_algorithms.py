"""
Treatment Algorithms - Decision Trees and Flowcharts
Clinical decision support for antibiotic selection
"""

import streamlit as st


ALGORITHMS = {
    "Sepsis": {
        "title": "Sepsis / Nhiễm khuẩn huyết",
        "description": "Phác đồ điều trị empiric cho sepsis",
        "steps": [
            {
                "step": 1,
                "question": "Bệnh nhân có sốc nhiễm khuẩn?",
                "options": {
                    "Có": {
                        "action": "Điều trị ngay lập tức",
                        "next": "severe_sepsis"
                    },
                    "Không": {
                        "action": "Đánh giá mức độ nặng",
                        "next": "moderate_sepsis"
                    }
                }
            },
            {
                "step": 2,
                "id": "severe_sepsis",
                "question": "Nguồn nhiễm khuẩn nghi ngờ?",
                "options": {
                    "Không rõ / Đa ổ": {
                        "recommendation": "Piperacillin-Tazobactam 4.5g IV mỗi 6 giờ + Vancomycin 15-20mg/kg IV mỗi 8-12 giờ",
                        "rationale": "Phổ rộng nhất, bao phủ Gram âm, Gram dương, kỵ khí, MRSA"
                    },
                    "Nghi ngờ ESBL": {
                        "recommendation": "Meropenem 1-2g IV mỗi 8 giờ + Vancomycin (nếu nghi ngờ MRSA)",
                        "rationale": "Meropenem hiệu quả với ESBL-producing Enterobacteriaceae"
                    },
                    "Nghi ngờ MRSA": {
                        "recommendation": "Vancomycin 15-20mg/kg IV (loading 25-30mg/kg) + Piperacillin-Tazobactam",
                        "rationale": "Vancomycin là lựa chọn đầu tay cho MRSA"
                    },
                    "Nghi ngờ Pseudomonas": {
                        "recommendation": "Piperacillin-Tazobactam 4.5g IV mỗi 6 giờ hoặc Meropenem 2g IV mỗi 8 giờ",
                        "rationale": "Cả hai đều hiệu quả với P. aeruginosa"
                    }
                }
            },
            {
                "step": 2,
                "id": "moderate_sepsis",
                "question": "Nguồn nhiễm khuẩn nghi ngờ?",
                "options": {
                    "Không rõ": {
                        "recommendation": "Ceftriaxone 2g IV x 1/ngày + Vancomycin (nếu nghi ngờ MRSA)",
                        "rationale": "Phác đồ chuẩn cho sepsis cộng đồng"
                    },
                    "UTI": {
                        "recommendation": "Ceftriaxone 1-2g IV x 1/ngày hoặc Piperacillin-Tazobactam",
                        "rationale": "E. coli là tác nhân phổ biến nhất"
                    },
                    "Pneumonia": {
                        "recommendation": "Ceftriaxone 2g IV x 1/ngày + Azithromycin 500mg IV/PO x 1/ngày",
                        "rationale": "Bao phủ typical và atypical pathogens"
                    }
                }
            },
            {
                "step": 3,
                "question": "Đánh giá sau 48-72 giờ",
                "options": {
                    "Cải thiện": {
                        "action": "De-escalate: Giảm phổ kháng sinh, chuyển IV → PO nếu có thể",
                        "next": "de_escalate"
                    },
                    "Không cải thiện": {
                        "action": "Đánh giá lại: Cấy máu, điều chỉnh kháng sinh theo kết quả",
                        "next": "reassess"
                    }
                }
            }
        ],
        "notes": [
            "Bắt đầu kháng sinh trong vòng 1 giờ sau chẩn đoán",
            "Lấy cấy máu TRƯỚC khi dùng kháng sinh",
            "Điều chỉnh theo kết quả cấy máu và độ nhạy",
            "Thời gian điều trị: 7-14 ngày (tùy đáp ứng)"
        ]
    },
    "Pneumonia": {
        "title": "Viêm Phổi",
        "description": "Phác đồ điều trị viêm phổi cộng đồng (CAP) và bệnh viện (HAP)",
        "steps": [
            {
                "step": 1,
                "question": "Loại viêm phổi?",
                "options": {
                    "CAP (Cộng đồng)": {
                        "next": "cap"
                    },
                    "HAP (Bệnh viện)": {
                        "next": "hap"
                    }
                }
            },
            {
                "step": 2,
                "id": "cap",
                "question": "Mức độ nặng?",
                "options": {
                    "Nhẹ - Trung bình (outpatient)": {
                        "recommendation": "Azithromycin 500mg PO ngày 1, sau đó 250mg/ngày x 4 ngày HOẶC Levofloxacin 500-750mg PO x 1/ngày",
                        "rationale": "Monotherapy đủ cho CAP nhẹ"
                    },
                    "Nặng (inpatient)": {
                        "recommendation": "Ceftriaxone 1-2g IV x 1/ngày + Azithromycin 500mg IV/PO x 1/ngày",
                        "rationale": "Phác đồ chuẩn cho CAP nặng, bao phủ S. pneumoniae và atypical"
                    },
                    "Rất nặng (ICU)": {
                        "recommendation": "Ceftriaxone 2g IV x 1/ngày + Azithromycin + Vancomycin (nếu nghi ngờ MRSA)",
                        "rationale": "Phác đồ mở rộng cho CAP rất nặng"
                    }
                }
            },
            {
                "step": 2,
                "id": "hap",
                "question": "Yếu tố nguy cơ?",
                "options": {
                    "Không có yếu tố nguy cơ đặc biệt": {
                        "recommendation": "Piperacillin-Tazobactam 4.5g IV mỗi 6 giờ",
                        "rationale": "Bao phủ Gram âm và kỵ khí"
                    },
                    "Nghi ngờ ESBL": {
                        "recommendation": "Meropenem 1-2g IV mỗi 8 giờ",
                        "rationale": "Hiệu quả với ESBL-producing Enterobacteriaceae"
                    },
                    "Nghi ngờ MRSA": {
                        "recommendation": "Vancomycin 15-20mg/kg IV mỗi 8-12 giờ + Piperacillin-Tazobactam",
                        "rationale": "Bổ sung coverage cho MRSA"
                    },
                    "VAP (Ventilator-associated)": {
                        "recommendation": "Meropenem 2g IV mỗi 8 giờ + Vancomycin (nếu nghi ngờ MRSA)",
                        "rationale": "VAP thường do đa kháng thuốc"
                    }
                }
            },
            {
                "step": 3,
                "question": "Đánh giá sau 48-72 giờ",
                "options": {
                    "Cải thiện (afebrile, giảm triệu chứng)": {
                        "action": "Chuyển IV → PO, tiếp tục 5-7 ngày",
                        "next": "switch_po"
                    },
                    "Không cải thiện": {
                        "action": "Đánh giá lại: Cấy đờm, X-quang, điều chỉnh kháng sinh",
                        "next": "reassess"
                    }
                }
            }
        ],
        "notes": [
            "CAP: Thời gian điều trị 5-7 ngày (nếu đáp ứng tốt)",
            "HAP: Thời gian điều trị 7-14 ngày",
            "Chuyển IV → PO khi: Afebrile 24-48h, ăn uống được, không nôn",
            "Điều chỉnh theo kết quả cấy đờm và độ nhạy"
        ]
    },
    "UTI": {
        "title": "Nhiễm Khuẩn Đường Tiết Niệu",
        "description": "Phác đồ điều trị UTI đơn giản và phức tạp",
        "steps": [
            {
                "step": 1,
                "question": "Loại UTI?",
                "options": {
                    "UTI đơn giản (Cystitis)": {
                        "next": "simple_uti"
                    },
                    "UTI phức tạp / Pyelonephritis": {
                        "next": "complex_uti"
                    }
                }
            },
            {
                "step": 2,
                "id": "simple_uti",
                "question": "Mức độ nặng?",
                "options": {
                    "Nhẹ (outpatient)": {
                        "recommendation": "Ciprofloxacin 500mg PO x 2 lần/ngày x 3 ngày HOẶC Levofloxacin 500mg PO x 1/ngày x 3 ngày",
                        "rationale": "Quinolone hiệu quả nhưng kháng thuốc cao tại VN. Cân nhắc dùng nếu nhạy cảm."
                    },
                    "Không dùng quinolone": {
                        "recommendation": "Ceftriaxone 1g IM x 1 liều HOẶC Cefuroxime 500mg PO x 2 lần/ngày x 3 ngày",
                        "rationale": "Alternative nếu kháng quinolone hoặc không dùng được"
                    }
                }
            },
            {
                "step": 2,
                "id": "complex_uti",
                "question": "Mức độ nặng?",
                "options": {
                    "Trung bình (inpatient)": {
                        "recommendation": "Ceftriaxone 1-2g IV x 1/ngày",
                        "rationale": "Phổ rộng, hiệu quả với E. coli, K. pneumoniae"
                    },
                    "Nặng / Nghi ngờ ESBL": {
                        "recommendation": "Meropenem 1g IV mỗi 8 giờ HOẶC Piperacillin-Tazobactam 4.5g IV mỗi 8 giờ",
                        "rationale": "Cho UTI phức tạp, nhiễm khuẩn bệnh viện, nghi ngờ ESBL"
                    },
                    "Nghi ngờ Pseudomonas": {
                        "recommendation": "Piperacillin-Tazobactam 4.5g IV mỗi 6 giờ HOẶC Cefepime 2g IV mỗi 8 giờ",
                        "rationale": "Bao phủ P. aeruginosa"
                    }
                }
            },
            {
                "step": 3,
                "question": "Đánh giá sau 48-72 giờ",
                "options": {
                    "Cải thiện": {
                        "action": "Chuyển IV → PO, tiếp tục 7-10 ngày (pyelonephritis) hoặc 3-5 ngày (cystitis)",
                        "next": "switch_po"
                    },
                    "Không cải thiện": {
                        "action": "Đánh giá lại: Cấy nước tiểu, siêu âm thận, điều chỉnh kháng sinh",
                        "next": "reassess"
                    }
                }
            }
        ],
        "notes": [
            "UTI đơn giản: 3-5 ngày",
            "Pyelonephritis: 7-14 ngày",
            "E. coli là tác nhân phổ biến nhất (80-90%)",
            "Kháng quinolone cao tại VN (50-60%), cân nhắc test độ nhạy",
            "Chuyển IV → PO khi: Afebrile 24h, ăn uống được"
        ]
    },
    "Meningitis": {
        "title": "Viêm Màng Não",
        "description": "Phác đồ điều trị viêm màng não cộng đồng",
        "steps": [
            {
                "step": 1,
                "question": "Tuổi bệnh nhân?",
                "options": {
                    "Trẻ em (< 3 tháng)": {
                        "recommendation": "Ampicillin + Cefotaxime HOẶC Ampicillin + Gentamicin",
                        "rationale": "Bao phủ Group B Strep, E. coli, Listeria"
                    },
                    "Trẻ em (3 tháng - 18 tuổi)": {
                        "recommendation": "Ceftriaxone 50-100mg/kg IV mỗi 12 giờ (max 2g) + Vancomycin",
                        "rationale": "Bao phủ S. pneumoniae, N. meningitidis, H. influenzae"
                    },
                    "Người lớn (18-50 tuổi)": {
                        "recommendation": "Ceftriaxone 2g IV mỗi 12 giờ + Vancomycin 15-20mg/kg IV mỗi 8-12 giờ",
                        "rationale": "Phác đồ chuẩn cho viêm màng não cộng đồng"
                    },
                    "Người lớn (> 50 tuổi)": {
                        "recommendation": "Ceftriaxone 2g IV mỗi 12 giờ + Vancomycin + Ampicillin 2g IV mỗi 4 giờ",
                        "rationale": "Thêm Ampicillin để bao phủ Listeria"
                    }
                }
            },
            {
                "step": 2,
                "question": "Nghi ngờ tác nhân?",
                "options": {
                    "S. pneumoniae": {
                        "recommendation": "Ceftriaxone 2g IV mỗi 12 giờ + Vancomycin (trough 15-20 mg/L)",
                        "rationale": "S. pneumoniae có thể kháng penicillin, cần Vancomycin"
                    },
                    "N. meningitidis": {
                        "recommendation": "Ceftriaxone 2g IV mỗi 12 giờ",
                        "rationale": "Ceftriaxone hiệu quả cao với N. meningitidis"
                    },
                    "Gram âm (E. coli, K. pneumoniae)": {
                        "recommendation": "Meropenem 2g IV mỗi 8 giờ",
                        "rationale": "Meropenem thấm tốt vào dịch não tủy, hiệu quả với Gram âm"
                    }
                }
            },
            {
                "step": 3,
                "question": "Đánh giá sau 48-72 giờ",
                "options": {
                    "Cải thiện": {
                        "action": "Tiếp tục điều trị 10-14 ngày (S. pneumoniae) hoặc 7 ngày (N. meningitidis)",
                        "next": "continue"
                    },
                    "Không cải thiện": {
                        "action": "Đánh giá lại: CSF culture, điều chỉnh kháng sinh",
                        "next": "reassess"
                    }
                }
            }
        ],
        "notes": [
            "Bắt đầu kháng sinh NGAY LẬP TỨC (trong vòng 30 phút)",
            "Lấy CSF TRƯỚC khi dùng kháng sinh",
            "Liều cao để đảm bảo thấm vào dịch não tủy",
            "Ceftriaxone: 2g mỗi 12 giờ (Người lớn)",
            "Vancomycin: Trough target 15-20 mg/L",
            "Thời gian điều trị: 7-21 ngày tùy tác nhân"
        ]
    },
    "Osteomyelitis": {
        "title": "Viêm Xương Tủy",
        "description": "Phác đồ điều trị viêm xương tủy",
        "steps": [
            {
                "step": 1,
                "question": "Loại viêm xương tủy?",
                "options": {
                    "Cộng đồng (hematogenous)": {
                        "next": "community"
                    },
                    "Sau chấn thương/phẫu thuật": {
                        "next": "post_trauma"
                    },
                    "Bàn chân ĐTĐ": {
                        "next": "diabetic_foot"
                    }
                }
            },
            {
                "step": 2,
                "id": "community",
                "question": "Tác nhân nghi ngờ?",
                "options": {
                    "S. aureus (phổ biến nhất)": {
                        "recommendation": "Vancomycin 15-20mg/kg IV mỗi 8-12 giờ + Ceftriaxone 2g IV x 1/ngày",
                        "rationale": "Bao phủ S. aureus (kể cả MRSA) và Gram âm"
                    },
                    "S. pyogenes": {
                        "recommendation": "Penicillin G 2-4 triệu đơn vị IV mỗi 4-6 giờ hoặc Ceftriaxone",
                        "rationale": "Penicillin là lựa chọn đầu tay cho S. pyogenes"
                    }
                }
            },
            {
                "step": 2,
                "id": "post_trauma",
                "question": "Nhiễm khuẩn?",
                "options": {
                    "Đa vi khuẩn": {
                        "recommendation": "Vancomycin + Piperacillin-Tazobactam hoặc Vancomycin + Ceftriaxone + Metronidazole",
                        "rationale": "Bao phủ Gram dương, Gram âm, và kỵ khí"
                    },
                    "Nghi ngờ MRSA": {
                        "recommendation": "Vancomycin 15-20mg/kg IV mỗi 8-12 giờ",
                        "rationale": "MRSA phổ biến trong viêm xương tủy sau chấn thương"
                    }
                }
            },
            {
                "step": 2,
                "id": "diabetic_foot",
                "question": "Mức độ nặng?",
                "options": {
                    "Nhẹ - Trung bình": {
                        "recommendation": "Piperacillin-Tazobactam 4.5g IV mỗi 6 giờ",
                        "rationale": "Bao phủ đa vi khuẩn (Gram dương, Gram âm, kỵ khí)"
                    },
                    "Nặng / Nghi ngờ MDR": {
                        "recommendation": "Meropenem 1g IV mỗi 8 giờ + Vancomycin (nếu nghi ngờ MRSA)",
                        "rationale": "Cho nhiễm khuẩn nặng, nghi ngờ ESBL hoặc MDR"
                    }
                }
            },
            {
                "step": 3,
                "question": "Đánh giá sau 2-4 tuần",
                "options": {
                    "Cải thiện": {
                        "action": "Chuyển IV → PO, tiếp tục 4-6 tuần tổng cộng",
                        "next": "switch_po"
                    },
                    "Không cải thiện": {
                        "action": "Đánh giá lại: Cấy mô xương, X-quang, điều chỉnh kháng sinh",
                        "next": "reassess"
                    }
                }
            }
        ],
        "notes": [
            "Thời gian điều trị: 4-6 tuần (cộng đồng) hoặc 6-12 tuần (sau chấn thương)",
            "Có thể chuyển IV → PO sau 2 tuần nếu cải thiện",
            "Cần debridement phẫu thuật nếu có hoại tử",
            "Monitor X-quang để đánh giá đáp ứng"
        ]
    },
    "Endocarditis": {
        "title": "Viêm Nội Tâm Mạc",
        "description": "Phác đồ điều trị viêm nội tâm mạc",
        "steps": [
            {
                "step": 1,
                "question": "Loại van tim?",
                "options": {
                    "Van tự nhiên": {
                        "next": "native_valve"
                    },
                    "Van nhân tạo": {
                        "next": "prosthetic_valve"
                    }
                }
            },
            {
                "step": 2,
                "id": "native_valve",
                "question": "Tác nhân nghi ngờ?",
                "options": {
                    "S. viridans / S. bovis": {
                        "recommendation": "Penicillin G 18-24 triệu đơn vị/ngày chia 4-6 lần + Gentamicin 1mg/kg IV mỗi 8 giờ",
                        "rationale": "Phác đồ chuẩn cho S. viridans nhạy cảm penicillin"
                    },
                    "S. aureus (MSSA)": {
                        "recommendation": "Nafcillin 2g IV mỗi 4 giờ + Gentamicin 1mg/kg IV mỗi 8 giờ (3-5 ngày đầu)",
                        "rationale": "Nafcillin hiệu quả hơn vancomycin cho MSSA"
                    },
                    "S. aureus (MRSA)": {
                        "recommendation": "Vancomycin 15-20mg/kg IV mỗi 8-12 giờ (trough 15-20 mg/L)",
                        "rationale": "Vancomycin là lựa chọn cho MRSA"
                    },
                    "Enterococcus": {
                        "recommendation": "Ampicillin 2g IV mỗi 4 giờ + Gentamicin 1mg/kg IV mỗi 8 giờ",
                        "rationale": "Synergy giữa ampicillin và gentamicin"
                    }
                }
            },
            {
                "step": 2,
                "id": "prosthetic_valve",
                "question": "Thời gian sau phẫu thuật?",
                "options": {
                    "< 1 năm": {
                        "recommendation": "Vancomycin + Gentamicin + Rifampin",
                        "rationale": "Thường do S. epidermidis, S. aureus. Cần phác đồ mạnh."
                    },
                    "> 1 năm": {
                        "recommendation": "Theo tác nhân (tương tự van tự nhiên)",
                        "rationale": "Tương tự viêm nội tâm mạc van tự nhiên"
                    }
                }
            },
            {
                "step": 3,
                "question": "Đánh giá sau 48-72 giờ",
                "options": {
                    "Cải thiện": {
                        "action": "Tiếp tục điều trị 4-6 tuần, monitor nồng độ kháng sinh",
                        "next": "continue"
                    },
                    "Không cải thiện": {
                        "action": "Đánh giá lại: Echo tim, cấy máu, xem xét phẫu thuật",
                        "next": "reassess"
                    }
                }
            }
        ],
        "notes": [
            "Thời gian điều trị: 4-6 tuần (van tự nhiên) hoặc 6 tuần (van nhân tạo)",
            "Monitor nồng độ kháng sinh: Vancomycin trough 15-20 mg/L, Gentamicin peak/trough",
            "Echo tim để đánh giá biến chứng",
            "Xem xét phẫu thuật nếu: Suy tim, áp xe, tắc mạch lớn"
        ]
    }
}


def render_algorithm(algorithm_name):
    """Render a treatment algorithm as interactive flowchart"""
    
    if algorithm_name not in ALGORITHMS:
        st.error(f"Không tìm thấy algorithm: {algorithm_name}")
        return
    
    algo = ALGORITHMS[algorithm_name]
    
    # Header
    st.markdown(f"""
    <div style='
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 25px;
        border-radius: 16px;
        margin-bottom: 25px;
    '>
        <h2 style='margin: 0; color: white; font-size: 2em; font-weight: 700;'>{algo['title']}</h2>
        <p style='margin: 10px 0 0 0; color: rgba(255,255,255,0.9); font-size: 1.1em;'>{algo['description']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Render steps
    current_step = 0
    selected_path = {}
    
    for step_data in algo['steps']:
        step_num = step_data.get('step', current_step + 1)
        step_id = step_data.get('id', f"step_{step_num}")
        
        # Check if this step should be shown based on previous selections
        if 'id' in step_data:
            # This is a conditional step, check if we should show it
            show_step = True
            # Simple logic: show if no previous conditional steps or if path matches
            if selected_path and step_id not in selected_path.values():
                # Check if this is the right branch
                continue
        else:
            show_step = True
        
        if not show_step:
            continue
        
        st.markdown(f"### Bước {step_num}: {step_data['question']}")
        
        options = step_data.get('options', {})
        
        # Create selection interface
        option_keys = list(options.keys())
        selected_option = st.radio(
            f"Lựa chọn:",
            options=option_keys,
            key=f"{algorithm_name}_step_{step_num}_{step_id}",
            label_visibility="collapsed"
        )
        
        selected_path[step_id] = selected_option
        option_data = options[selected_option]
        
        # Display recommendation or next step
        if 'recommendation' in option_data:
            st.markdown("---")
            st.markdown(f"""
            <div style='
                background: linear-gradient(135deg, rgba(76,175,80,0.1) 0%, rgba(76,175,80,0.05) 100%);
                padding: 20px;
                border-radius: 12px;
                border-left: 4px solid #4CAF50;
                margin: 15px 0;
            '>
                <h4 style='color: #2e7d32; margin-bottom: 10px;'>💊 Khuyến cáo:</h4>
                <p style='font-size: 1.1em; font-weight: 600; color: #1976D2; margin: 10px 0;'>{option_data['recommendation']}</p>
                <p style='color: #666; margin-top: 10px;'><strong>💡 Lý do:</strong> {option_data.get('rationale', '')}</p>
            </div>
            """, unsafe_allow_html=True)
        
        if 'action' in option_data:
            st.info(f"**Hành động:** {option_data['action']}")
        
        if 'next' in option_data:
            next_step_id = option_data['next']
            # Continue to next conditional step if exists
            continue
        
        st.markdown("---")
        current_step = step_num
    
    # Notes section
    if 'notes' in algo:
        st.markdown("### 📝 Lưu ý quan trọng:")
        for note in algo['notes']:
            st.markdown(f"• {note}")


def render_algorithms_page():
    """Render main algorithms page with algorithm selection"""
    
    st.markdown("""
    <div style='
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 30px 25px;
        border-radius: 20px;
        margin-bottom: 30px;
        text-align: center;
        box-shadow: 0 8px 24px rgba(102,126,234,0.25);
    '>
        <h1 style='margin: 0; color: white; font-size: 2.5em; font-weight: 700;'>🔄 Phác Đồ Điều trị</h1>
        <p style='margin: 12px 0 0 0; color: rgba(255,255,255,0.95); font-size: 1.15em;'>
            Decision trees và flowcharts hỗ trợ quyết định lâm sàng
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Algorithm selection
    algorithm_names = list(ALGORITHMS.keys())
    algorithm_display = {
        "Sepsis": "Sepsis / Nhiễm khuẩn huyết",
        "Pneumonia": "Viêm Phổi (CAP/HAP)",
        "UTI": "Nhiễm Khuẩn Đường Tiết Niệu",
        "Meningitis": "Viêm Màng Não",
        "Osteomyelitis": "Viêm Xương Tủy",
        "Endocarditis": "Viêm Nội Tâm Mạc"
    }
    
    selected_algo = st.selectbox(
        "Chọn phác đồ điều trị:",
        options=algorithm_names,
        format_func=lambda x: algorithm_display.get(x, x),
        key="algorithm_select"
    )
    
    st.markdown("---")
    
    # Render selected algorithm
    if selected_algo:
        render_algorithm(selected_algo)

