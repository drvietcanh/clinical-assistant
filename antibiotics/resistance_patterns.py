"""
Antibiotic Resistance Patterns - Vietnam Data
Based on local surveillance data and studies
"""

RESISTANCE_PATTERNS_VN = {
    "region": "Vietnam",
    "year": "2024",
    "source": "Local surveillance data, studies, and clinical experience",
    "data": {
        "E. coli": {
            "Ceftriaxone": {"resistant": "35-45%", "intermediate": "5-10%", "sensitive": "50-60%"},
            "Ciprofloxacin": {"resistant": "50-60%", "intermediate": "5-10%", "sensitive": "35-45%"},
            "Levofloxacin": {"resistant": "45-55%", "intermediate": "5-10%", "sensitive": "40-50%"},
            "Piperacillin-Tazobactam": {"resistant": "30-40%", "intermediate": "5-10%", "sensitive": "60-70%"},
            "Meropenem": {"resistant": "5-10%", "intermediate": "2-5%", "sensitive": "90-95%"},
            "Amikacin": {"resistant": "10-15%", "intermediate": "3-5%", "sensitive": "85-90%"},
            "Gentamicin": {"resistant": "20-30%", "intermediate": "5-10%", "sensitive": "70-80%"},
            "notes": "ESBL-producing E. coli phổ biến (30-40%). Kháng quinolone cao."
        },
        "Klebsiella pneumoniae": {
            "Ceftriaxone": {"resistant": "40-50%", "intermediate": "5-10%", "sensitive": "50-60%"},
            "Ciprofloxacin": {"resistant": "55-65%", "intermediate": "5-10%", "sensitive": "30-40%"},
            "Piperacillin-Tazobactam": {"resistant": "35-45%", "intermediate": "5-10%", "sensitive": "55-65%"},
            "Meropenem": {"resistant": "15-25%", "intermediate": "3-5%", "sensitive": "75-85%"},
            "Amikacin": {"resistant": "15-20%", "intermediate": "3-5%", "sensitive": "80-85%"},
            "Gentamicin": {"resistant": "25-35%", "intermediate": "5-10%", "sensitive": "65-75%"},
            "notes": "KPC và NDM carbapenemase phổ biến. Kháng đa thuốc cao."
        },
        "Pseudomonas aeruginosa": {
            "Ceftazidime": {"resistant": "25-35%", "intermediate": "5-10%", "sensitive": "60-70%"},
            "Ciprofloxacin": {"resistant": "30-40%", "intermediate": "5-10%", "sensitive": "60-70%"},
            "Piperacillin-Tazobactam": {"resistant": "20-30%", "intermediate": "5-10%", "sensitive": "70-80%"},
            "Meropenem": {"resistant": "20-30%", "intermediate": "5-10%", "sensitive": "70-80%"},
            "Amikacin": {"resistant": "15-20%", "intermediate": "3-5%", "sensitive": "80-85%"},
            "Gentamicin": {"resistant": "15-25%", "intermediate": "5-10%", "sensitive": "75-85%"},
            "notes": "Kháng đa thuốc phổ biến. Cần test độ nhạy trước khi điều trị."
        },
        "Acinetobacter baumannii": {
            "Ceftazidime": {"resistant": "70-80%", "intermediate": "5-10%", "sensitive": "15-25%"},
            "Meropenem": {"resistant": "50-60%", "intermediate": "5-10%", "sensitive": "40-50%"},
            "Imipenem": {"resistant": "50-60%", "intermediate": "5-10%", "sensitive": "40-50%"},
            "Amikacin": {"resistant": "30-40%", "intermediate": "5-10%", "sensitive": "60-70%"},
            "Colistin": {"resistant": "5-10%", "intermediate": "2-5%", "sensitive": "90-95%"},
            "notes": "Kháng đa thuốc rất cao. Colistin thường là lựa chọn cuối cùng."
        },
        "Staphylococcus aureus": {
            "Oxacillin (MSSA)": {"resistant": "0-5%", "sensitive": "95-100%"},
            "Oxacillin (MRSA)": {"resistant": "30-40%", "sensitive": "60-70%"},
            "Vancomycin": {"resistant": "< 1%", "intermediate": "< 1%", "sensitive": "> 99%"},
            "Clindamycin": {"resistant": "15-25%", "sensitive": "75-85%"},
            "Erythromycin": {"resistant": "40-50%", "sensitive": "50-60%"},
            "notes": "MRSA phổ biến (30-40%). Vancomycin vẫn hiệu quả cao."
        },
        "Enterococcus faecalis": {
            "Ampicillin": {"resistant": "5-10%", "sensitive": "90-95%"},
            "Vancomycin": {"resistant": "5-10%", "sensitive": "85-90%"},
            "Linezolid": {"resistant": "< 1%", "sensitive": "> 99%"},
            "notes": "VRE (Vancomycin-resistant) đang tăng."
        },
        "Streptococcus pneumoniae": {
            "Penicillin": {"resistant": "20-30%", "intermediate": "10-15%", "sensitive": "60-70%"},
            "Ceftriaxone": {"resistant": "5-10%", "intermediate": "5-10%", "sensitive": "85-90%"},
            "Levofloxacin": {"resistant": "5-10%", "sensitive": "90-95%"},
            "Azithromycin": {"resistant": "40-50%", "sensitive": "50-60%"},
            "notes": "Kháng penicillin và macrolide tăng. Ceftriaxone vẫn hiệu quả."
        },
        "Enterococcus faecium": {
            "Ampicillin": {"resistant": "85-95%", "sensitive": "5-15%"},
            "Vancomycin": {"resistant": "60-70%", "sensitive": "30-40%"},
            "Linezolid": {"resistant": "< 1%", "sensitive": "> 99%"},
            "Daptomycin": {"resistant": "5-10%", "sensitive": "90-95%"},
            "notes": "VRE (Vancomycin-resistant) rất phổ biến. Linezolid là lựa chọn tốt."
        },
        "Haemophilus influenzae": {
            "Ampicillin": {"resistant": "30-40%", "sensitive": "60-70%"},
            "Ceftriaxone": {"resistant": "< 1%", "sensitive": "> 99%"},
            "Azithromycin": {"resistant": "5-10%", "sensitive": "90-95%"},
            "Levofloxacin": {"resistant": "< 1%", "sensitive": "> 99%"},
            "notes": "Beta-lactamase production phổ biến. Ceftriaxone vẫn hiệu quả cao."
        },
        "Streptococcus pyogenes": {
            "Penicillin": {"resistant": "< 1%", "sensitive": "> 99%"},
            "Ceftriaxone": {"resistant": "< 1%", "sensitive": "> 99%"},
            "Clindamycin": {"resistant": "5-10%", "sensitive": "90-95%"},
            "Azithromycin": {"resistant": "10-15%", "sensitive": "85-90%"},
            "Erythromycin": {"resistant": "15-25%", "sensitive": "75-85%"},
            "notes": "Penicillin vẫn là lựa chọn đầu tay. Kháng macrolide tăng."
        },
        "Bacteroides fragilis": {
            "Metronidazole": {"resistant": "5-10%", "sensitive": "90-95%"},
            "Clindamycin": {"resistant": "10-15%", "sensitive": "85-90%"},
            "Piperacillin-Tazobactam": {"resistant": "5-10%", "sensitive": "90-95%"},
            "Meropenem": {"resistant": "2-5%", "sensitive": "95-98%"},
            "Ertapenem": {"resistant": "2-5%", "sensitive": "95-98%"},
            "notes": "Kỵ khí quan trọng nhất. Metronidazole và carbapenem hiệu quả cao."
        },
        "Neisseria meningitidis": {
            "Penicillin": {"resistant": "5-10%", "intermediate": "10-15%", "sensitive": "75-85%"},
            "Ceftriaxone": {"resistant": "< 1%", "sensitive": "> 99%"},
            "Ciprofloxacin": {"resistant": "< 1%", "sensitive": "> 99%"},
            "notes": "Ceftriaxone là lựa chọn đầu tay cho viêm màng não."
        }
    }
}


def get_resistance_pattern(organism, antibiotic):
    """Get resistance pattern for a specific organism-antibiotic combination"""
    data = RESISTANCE_PATTERNS_VN.get("data", {})
    if organism in data and antibiotic in data[organism]:
        return data[organism][antibiotic]
    return None


def get_organism_resistance(organism):
    """Get all resistance patterns for an organism"""
    data = RESISTANCE_PATTERNS_VN.get("data", {})
    return data.get(organism, {})


def get_antibiotic_resistance_summary(antibiotic):
    """Get resistance summary across organisms for an antibiotic"""
    data = RESISTANCE_PATTERNS_VN.get("data", {})
    summary = {}
    
    for organism, patterns in data.items():
        if antibiotic in patterns:
            summary[organism] = patterns[antibiotic]
    
    return summary

