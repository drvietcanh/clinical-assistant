"""
Condition-Based Search - Find antibiotics by clinical condition
Maps clinical conditions to recommended antibiotics
"""

CONDITION_ANTIBIOTICS = {
    "Sepsis": {
        "description": "Nhiễm khuẩn huyết / Sepsis",
        "empiric_therapy": [
            {
                "antibiotic": "Piperacillin-Tazobactam",
                "rationale": "Phổ rộng, bao phủ Gram âm, Gram dương, kỵ khí",
                "dosing": "4.5g IV mỗi 6-8 giờ",
                "priority": "First-line"
            },
            {
                "antibiotic": "Meropenem",
                "rationale": "Phổ rộng nhất, cho nhiễm khuẩn nặng, nghi ngờ ESBL",
                "dosing": "1g IV mỗi 8 giờ (nặng: 2g mỗi 8 giờ)",
                "priority": "First-line (nghi ngờ ESBL)"
            },
            {
                "antibiotic": "Vancomycin",
                "rationale": "Nếu nghi ngờ MRSA hoặc nhiễm khuẩn Gram dương",
                "dosing": "15-20mg/kg IV mỗi 8-12 giờ (loading 25-30mg/kg)",
                "priority": "Add-on (nghi ngờ MRSA)"
            },
            {
                "antibiotic": "Ceftriaxone + Vancomycin",
                "rationale": "Phác đồ kết hợp cho sepsis cộng đồng",
                "dosing": "Ceftriaxone 2g IV x 1/ngày + Vancomycin",
                "priority": "Alternative"
            }
        ],
        "notes": "Điều trị empiric phải bao phủ Gram âm và Gram dương. Điều chỉnh theo kết quả cấy máu."
    },
    "UTI": {
        "description": "Nhiễm khuẩn đường tiết niệu",
        "empiric_therapy": [
            {
                "antibiotic": "Ceftriaxone",
                "rationale": "Phổ rộng, hiệu quả với E. coli, K. pneumoniae",
                "dosing": "1-2g IV x 1 lần/ngày",
                "priority": "First-line (nặng)"
            },
            {
                "antibiotic": "Ciprofloxacin",
                "rationale": "Hiệu quả với E. coli, nhưng kháng thuốc cao tại VN",
                "dosing": "400mg IV mỗi 12 giờ hoặc 500mg PO x 2 lần/ngày",
                "priority": "Alternative (nếu nhạy cảm)"
            },
            {
                "antibiotic": "Levofloxacin",
                "rationale": "Tương tự ciprofloxacin, phổ rộng hơn",
                "dosing": "500-750mg IV/PO x 1 lần/ngày",
                "priority": "Alternative"
            },
            {
                "antibiotic": "Piperacillin-Tazobactam",
                "rationale": "Cho UTI phức tạp, nhiễm khuẩn bệnh viện",
                "dosing": "4.5g IV mỗi 8 giờ",
                "priority": "Complex UTI"
            }
        ],
        "notes": "E. coli là tác nhân phổ biến nhất. Kháng quinolone cao tại VN (50-60%)."
    },
    "Pneumonia": {
        "description": "Viêm phổi",
        "empiric_therapy": [
            {
                "antibiotic": "Ceftriaxone + Azithromycin",
                "rationale": "Phác đồ chuẩn cho viêm phổi cộng đồng",
                "dosing": "Ceftriaxone 1-2g IV x 1/ngày + Azithromycin 500mg IV/PO x 1/ngày",
                "priority": "First-line (CAP)"
            },
            {
                "antibiotic": "Levofloxacin",
                "rationale": "Monotherapy cho CAP, bao phủ cả typical và atypical",
                "dosing": "500-750mg IV/PO x 1 lần/ngày",
                "priority": "Alternative (CAP)"
            },
            {
                "antibiotic": "Piperacillin-Tazobactam",
                "rationale": "Cho viêm phổi bệnh viện (HAP), nghi ngờ Gram âm",
                "dosing": "4.5g IV mỗi 6 giờ",
                "priority": "First-line (HAP)"
            },
            {
                "antibiotic": "Meropenem",
                "rationale": "Cho HAP nặng, nghi ngờ ESBL, VAP",
                "dosing": "1-2g IV mỗi 8 giờ",
                "priority": "Severe HAP/VAP"
            },
            {
                "antibiotic": "Vancomycin",
                "rationale": "Nếu nghi ngờ MRSA",
                "dosing": "15-20mg/kg IV mỗi 8-12 giờ",
                "priority": "Add-on (MRSA)"
            }
        ],
        "notes": "CAP: Ceftriaxone + Azithromycin. HAP: Piperacillin-Tazobactam hoặc Meropenem."
    },
    "Meningitis": {
        "description": "Viêm màng não",
        "empiric_therapy": [
            {
                "antibiotic": "Ceftriaxone + Vancomycin",
                "rationale": "Phác đồ chuẩn cho viêm màng não cộng đồng",
                "dosing": "Ceftriaxone 2g IV mỗi 12 giờ + Vancomycin 15-20mg/kg IV mỗi 8-12 giờ",
                "priority": "First-line"
            },
            {
                "antibiotic": "Meropenem",
                "rationale": "Cho viêm màng não do Gram âm, nghi ngờ kháng Ceftriaxone",
                "dosing": "2g IV mỗi 8 giờ",
                "priority": "Alternative (Gram negative)"
            },
            {
                "antibiotic": "Vancomycin",
                "rationale": "Cho viêm màng não do S. pneumoniae kháng penicillin",
                "dosing": "15-20mg/kg IV mỗi 8-12 giờ (trough 15-20 mg/L)",
                "priority": "Penicillin-resistant"
            }
        ],
        "notes": "Phải dùng liều cao, thấm tốt vào dịch não tủy. Ceftriaxone 2g mỗi 12h."
    },
    "Intra-abdominal": {
        "description": "Nhiễm khuẩn ổ bụng",
        "empiric_therapy": [
            {
                "antibiotic": "Piperacillin-Tazobactam",
                "rationale": "Bao phủ Gram âm, kỵ khí (Bacteroides)",
                "dosing": "4.5g IV mỗi 6-8 giờ",
                "priority": "First-line"
            },
            {
                "antibiotic": "Meropenem",
                "rationale": "Cho nhiễm khuẩn nặng, nghi ngờ ESBL",
                "dosing": "1g IV mỗi 8 giờ",
                "priority": "Severe/ESBL"
            },
            {
                "antibiotic": "Ceftriaxone + Metronidazole",
                "rationale": "Phác đồ kết hợp cho nhiễm khuẩn ổ bụng",
                "dosing": "Ceftriaxone 2g IV x 1/ngày + Metronidazole 500mg IV mỗi 8 giờ",
                "priority": "Alternative"
            }
        ],
        "notes": "Phải bao phủ kỵ khí (Bacteroides fragilis). Piperacillin-Tazobactam là lựa chọn tốt."
    },
    "Skin_Soft_Tissue": {
        "description": "Nhiễm khuẩn da và mô mềm",
        "empiric_therapy": [
            {
                "antibiotic": "Ceftriaxone",
                "rationale": "Cho nhiễm khuẩn da do Gram dương và Gram âm",
                "dosing": "1-2g IV x 1 lần/ngày",
                "priority": "First-line"
            },
            {
                "antibiotic": "Vancomycin",
                "rationale": "Nếu nghi ngờ MRSA",
                "dosing": "15-20mg/kg IV mỗi 8-12 giờ",
                "priority": "MRSA"
            },
            {
                "antibiotic": "Clindamycin",
                "rationale": "Cho nhiễm khuẩn da do S. aureus, S. pyogenes",
                "dosing": "600-900mg IV mỗi 8 giờ",
                "priority": "Alternative"
            },
            {
                "antibiotic": "Piperacillin-Tazobactam",
                "rationale": "Cho nhiễm khuẩn da phức tạp, nhiễm khuẩn bệnh viện",
                "dosing": "4.5g IV mỗi 6-8 giờ",
                "priority": "Complex/Hospital"
            }
        ],
        "notes": "MRSA phổ biến. Cần test độ nhạy. Vancomycin cho MRSA."
    },
    "Osteomyelitis": {
        "description": "Viêm Xương Tủy",
        "empiric_therapy": [
            {
                "antibiotic": "Vancomycin + Ceftriaxone",
                "rationale": "Phác đồ chuẩn cho viêm xương tủy cộng đồng",
                "dosing": "Vancomycin 15-20mg/kg IV mỗi 8-12 giờ + Ceftriaxone 2g IV x 1/ngày",
                "priority": "First-line"
            },
            {
                "antibiotic": "Vancomycin + Ciprofloxacin",
                "rationale": "Alternative, đặc biệt nếu nghi ngờ Gram âm",
                "dosing": "Vancomycin + Ciprofloxacin 400mg IV mỗi 12 giờ",
                "priority": "Alternative"
            },
            {
                "antibiotic": "Clindamycin",
                "rationale": "Cho viêm xương tủy do S. aureus, có thể chuyển PO",
                "dosing": "600-900mg IV mỗi 8 giờ, sau đó 300-450mg PO x 4 lần/ngày",
                "priority": "Step-down"
            }
        ],
        "notes": "Thời gian điều trị dài (4-6 tuần). Có thể chuyển IV → PO sau 2 tuần nếu cải thiện."
    },
    "Endocarditis": {
        "description": "Viêm Nội Tâm Mạc",
        "empiric_therapy": [
            {
                "antibiotic": "Vancomycin + Gentamicin",
                "rationale": "Phác đồ chuẩn cho viêm nội tâm mạc nghi ngờ MRSA hoặc Enterococcus",
                "dosing": "Vancomycin 15-20mg/kg IV mỗi 8-12 giờ + Gentamicin 1mg/kg IV mỗi 8 giờ",
                "priority": "First-line (MRSA/Enterococcus)"
            },
            {
                "antibiotic": "Ceftriaxone + Gentamicin",
                "rationale": "Cho viêm nội tâm mạc do S. viridans, Enterococcus nhạy cảm",
                "dosing": "Ceftriaxone 2g IV x 1/ngày + Gentamicin 1mg/kg IV mỗi 8 giờ",
                "priority": "First-line (S. viridans)"
            },
            {
                "antibiotic": "Ampicillin + Gentamicin",
                "rationale": "Cho Enterococcus faecalis nhạy cảm ampicillin",
                "dosing": "Ampicillin 2g IV mỗi 4 giờ + Gentamicin 1mg/kg IV mỗi 8 giờ",
                "priority": "First-line (E. faecalis)"
            }
        ],
        "notes": "Thời gian điều trị dài (4-6 tuần). Cần test độ nhạy. Monitor nồng độ kháng sinh."
    },
    "Cellulitis": {
        "description": "Viêm Mô Tế Bào",
        "empiric_therapy": [
            {
                "antibiotic": "Ceftriaxone",
                "rationale": "Cho viêm mô tế bào không phức tạp, bao phủ S. pyogenes và S. aureus",
                "dosing": "1-2g IV x 1 lần/ngày",
                "priority": "First-line"
            },
            {
                "antibiotic": "Clindamycin",
                "rationale": "Cho viêm mô tế bào do S. pyogenes, có thể chuyển PO",
                "dosing": "600-900mg IV mỗi 8 giờ, sau đó 300-450mg PO x 4 lần/ngày",
                "priority": "Alternative"
            },
            {
                "antibiotic": "Vancomycin",
                "rationale": "Nếu nghi ngờ MRSA hoặc viêm mô tế bào nặng",
                "dosing": "15-20mg/kg IV mỗi 8-12 giờ",
                "priority": "MRSA"
            },
            {
                "antibiotic": "Piperacillin-Tazobactam",
                "rationale": "Cho viêm mô tế bào phức tạp, nhiễm khuẩn bệnh viện",
                "dosing": "4.5g IV mỗi 6-8 giờ",
                "priority": "Complex/Hospital"
            }
        ],
        "notes": "S. pyogenes và S. aureus là tác nhân phổ biến. MRSA cần được xem xét."
    },
    "Diabetic_Foot": {
        "description": "Nhiễm Khuẩn Bàn Chân Đái Tháo Đường",
        "empiric_therapy": [
            {
                "antibiotic": "Piperacillin-Tazobactam",
                "rationale": "Bao phủ Gram âm, Gram dương, kỵ khí (phổ biến trong nhiễm khuẩn bàn chân ĐTĐ)",
                "dosing": "4.5g IV mỗi 6 giờ",
                "priority": "First-line"
            },
            {
                "antibiotic": "Meropenem",
                "rationale": "Cho nhiễm khuẩn nặng, nghi ngờ ESBL, nhiễm khuẩn đa kháng",
                "dosing": "1g IV mỗi 8 giờ",
                "priority": "Severe/ESBL"
            },
            {
                "antibiotic": "Vancomycin + Piperacillin-Tazobactam",
                "rationale": "Nếu nghi ngờ MRSA kết hợp với Gram âm",
                "dosing": "Vancomycin 15-20mg/kg IV mỗi 8-12 giờ + Piperacillin-Tazobactam",
                "priority": "MRSA + Gram negative"
            },
            {
                "antibiotic": "Ceftriaxone + Metronidazole",
                "rationale": "Alternative, bao phủ Gram âm và kỵ khí",
                "dosing": "Ceftriaxone 2g IV x 1/ngày + Metronidazole 500mg IV mỗi 8 giờ",
                "priority": "Alternative"
            }
        ],
        "notes": "Thường đa vi khuẩn (Gram dương, Gram âm, kỵ khí). Cần đánh giá tưới máu và debridement."
    },
    "Prostatitis": {
        "description": "Viêm Tuyến Tiền Liệt",
        "empiric_therapy": [
            {
                "antibiotic": "Ciprofloxacin",
                "rationale": "Thấm tốt vào tuyến tiền liệt, hiệu quả với E. coli",
                "dosing": "400mg IV mỗi 12 giờ hoặc 500mg PO x 2 lần/ngày",
                "priority": "First-line (nếu nhạy cảm)"
            },
            {
                "antibiotic": "Levofloxacin",
                "rationale": "Tương tự ciprofloxacin, phổ rộng hơn",
                "dosing": "500-750mg IV/PO x 1 lần/ngày",
                "priority": "Alternative"
            },
            {
                "antibiotic": "Ceftriaxone",
                "rationale": "Cho viêm tuyến tiền liệt cấp nặng",
                "dosing": "1-2g IV x 1 lần/ngày",
                "priority": "Severe"
            },
            {
                "antibiotic": "Trimethoprim-Sulfamethoxazole",
                "rationale": "Cho viêm tuyến tiền liệt mạn, thấm tốt vào tuyến tiền liệt",
                "dosing": "160/800mg PO x 2 lần/ngày",
                "priority": "Chronic"
            }
        ],
        "notes": "E. coli là tác nhân phổ biến nhất. Quinolone thấm tốt vào tuyến tiền liệt. Thời gian điều trị: 4-6 tuần (mạn)."
    }
}


def search_by_condition(condition):
    """Search antibiotics by clinical condition"""
    condition_lower = condition.lower()
    
    # Map common search terms to conditions
    condition_map = {
        "sepsis": "Sepsis",
        "nhiễm khuẩn huyết": "Sepsis",
        "uti": "UTI",
        "nhiễm khuẩn tiết niệu": "UTI",
        "pneumonia": "Pneumonia",
        "viêm phổi": "Pneumonia",
        "meningitis": "Meningitis",
        "viêm màng não": "Meningitis",
        "intra-abdominal": "Intra-abdominal",
        "nhiễm khuẩn ổ bụng": "Intra-abdominal",
        "skin": "Skin_Soft_Tissue",
        "da": "Skin_Soft_Tissue",
        "nhiễm khuẩn da": "Skin_Soft_Tissue",
        "osteomyelitis": "Osteomyelitis",
        "viêm xương tủy": "Osteomyelitis",
        "endocarditis": "Endocarditis",
        "viêm nội tâm mạc": "Endocarditis",
        "cellulitis": "Cellulitis",
        "viêm mô tế bào": "Cellulitis",
        "diabetic foot": "Diabetic_Foot",
        "bàn chân đái tháo đường": "Diabetic_Foot",
        "prostatitis": "Prostatitis",
        "viêm tuyến tiền liệt": "Prostatitis"
    }
    
    # Find matching condition
    for key, value in condition_map.items():
        if key in condition_lower:
            return CONDITION_ANTIBIOTICS.get(value, None)
    
    # Direct match
    return CONDITION_ANTIBIOTICS.get(condition, None)


def get_all_conditions():
    """Get list of all available conditions"""
    return list(CONDITION_ANTIBIOTICS.keys())


def get_condition_antibiotics(condition):
    """Get recommended antibiotics for a condition"""
    return CONDITION_ANTIBIOTICS.get(condition, {})

