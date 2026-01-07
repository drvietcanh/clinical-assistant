"""
Drug Classes Data Structure
Tổ chức kháng sinh theo nhóm thuốc với spectrum, indications, dosing, resistance patterns
"""

from typing import List, Dict, Optional
from dataclasses import dataclass


@dataclass
class DrugInClass:
    """Thông tin thuốc trong một nhóm"""
    name: str
    vietnamese_name: Optional[str] = None
    spectrum: Optional[str] = None
    common_indications: Optional[List[str]] = None
    dosing_summary: Optional[str] = None
    resistance_notes: Optional[str] = None
    aware_classification: Optional[str] = None


@dataclass
class DrugClass:
    """Thông tin một nhóm thuốc"""
    class_name: str
    class_name_vi: str
    description: str
    mechanism: str
    drugs: List[DrugInClass]
    spectrum_summary: str
    common_indications: List[str]
    resistance_patterns: str
    clinical_notes: Optional[str] = None


# Beta-lactams
BETA_LACTAMS = DrugClass(
    class_name="Beta-lactams",
    class_name_vi="Beta-lactam",
    description="Nhóm kháng sinh có cấu trúc beta-lactam ring, bao gồm Penicillins, Cephalosporins, và Carbapenems",
    mechanism="Ức chế tổng hợp thành tế bào vi khuẩn (PBP - Penicillin Binding Proteins)",
    drugs=[
        DrugInClass(
            name="Penicillin G",
            vietnamese_name="Penicillin G, Bicilin",
            spectrum="Gram-positive: Streptococcus, Enterococcus, Treponema pallidum",
            common_indications=["Nhiễm khuẩn do liên cầu", "Giang mai", "Viêm màng não do phế cầu"],
            dosing_summary="2-4 triệu đơn vị IV mỗi 4-6 giờ",
            resistance_notes="Kháng penicillin ở S. pneumoniae tăng (20-30% tại VN)"
        ),
        DrugInClass(
            name="Ampicillin",
            vietnamese_name="Ampicillin, Ampicin",
            spectrum="Gram-positive và một số Gram-negative (H. influenzae, E. coli nhạy cảm)",
            common_indications=["Nhiễm khuẩn đường tiết niệu", "Nhiễm khuẩn đường hô hấp"],
            dosing_summary="1-2g IV mỗi 4-6 giờ",
            resistance_notes="Beta-lactamase production phổ biến → cần kết hợp với beta-lactamase inhibitor"
        ),
        DrugInClass(
            name="Amoxicillin-Clavulanate",
            vietnamese_name="Amoxicillin-Clavulanate, Augmentin",
            spectrum="Gram-positive và Gram-negative (bao gồm beta-lactamase producers)",
            common_indications=["Nhiễm khuẩn đường hô hấp", "Nhiễm khuẩn da và mô mềm", "Nhiễm khuẩn đường tiết niệu"],
            dosing_summary="875/125mg PO BID hoặc 1.2g IV mỗi 8 giờ",
            aware_classification="ACCESS"
        ),
        DrugInClass(
            name="Piperacillin-Tazobactam",
            vietnamese_name="Piperacillin-Tazobactam, Tazocin",
            spectrum="Phổ rộng: Gram-positive, Gram-negative (bao gồm Pseudomonas), kỵ khí",
            common_indications=["Nhiễm khuẩn bệnh viện", "Nhiễm khuẩn ổ bụng", "Nhiễm khuẩn huyết"],
            dosing_summary="4.5g IV mỗi 6-8 giờ",
            resistance_notes="ESBL-producing Enterobacteriaceae: R 30-40% tại VN"
        ),
        DrugInClass(
            name="Ceftriaxone",
            vietnamese_name="Ceftriaxone, Rocephin",
            spectrum="Gram-positive và Gram-negative (không bao gồm Pseudomonas)",
            common_indications=["Viêm phổi cộng đồng", "Nhiễm khuẩn huyết", "Viêm màng não"],
            dosing_summary="1-2g IV/IM mỗi 24 giờ",
            resistance_notes="E. coli: R 35-45% tại VN (ESBL), K. pneumoniae: R 40-50%"
        ),
        DrugInClass(
            name="Ceftazidime",
            vietnamese_name="Ceftazidime, Fortum",
            spectrum="Gram-negative (bao gồm Pseudomonas)",
            common_indications=["Nhiễm khuẩn do Pseudomonas", "Nhiễm khuẩn bệnh viện"],
            dosing_summary="2g IV mỗi 8 giờ",
            resistance_notes="Pseudomonas: R 25-35% tại VN"
        ),
        DrugInClass(
            name="Meropenem",
            vietnamese_name="Meropenem, Meronem",
            spectrum="Phổ rất rộng: Gram-positive, Gram-negative (bao gồm ESBL), Pseudomonas, kỵ khí",
            common_indications=["Nhiễm khuẩn nặng", "Nhiễm khuẩn đa kháng", "Nhiễm khuẩn ICU"],
            dosing_summary="1g IV mỗi 8 giờ (hoặc 2g mỗi 8 giờ nếu nhiễm khuẩn nặng)",
            resistance_notes="K. pneumoniae: R 15-25% tại VN (KPC, NDM carbapenemase)"
        ),
    ],
    spectrum_summary="Phổ tác dụng rộng từ Gram-positive đến Gram-negative, tùy thuộc vào từng thuốc cụ thể",
    common_indications=[
        "Nhiễm khuẩn đường hô hấp",
        "Nhiễm khuẩn đường tiết niệu",
        "Nhiễm khuẩn da và mô mềm",
        "Nhiễm khuẩn ổ bụng",
        "Nhiễm khuẩn huyết",
        "Viêm màng não"
    ],
    resistance_patterns="Beta-lactamase production (ESBL, AmpC, Carbapenemase) là cơ chế kháng thuốc chính. ESBL-producing Enterobacteriaceae phổ biến tại VN (30-40%). Carbapenemase (KPC, NDM) đang tăng.",
    clinical_notes="Dị ứng chéo giữa các beta-lactam có thể xảy ra. Cần test dị ứng trước khi dùng."
)


# Fluoroquinolones
FLUOROQUINOLONES = DrugClass(
    class_name="Fluoroquinolones",
    class_name_vi="Fluoroquinolone",
    description="Kháng sinh phổ rộng, ức chế DNA gyrase và topoisomerase IV",
    mechanism="Ức chế DNA gyrase (Gram-negative) và topoisomerase IV (Gram-positive)",
    drugs=[
        DrugInClass(
            name="Ciprofloxacin",
            vietnamese_name="Ciprofloxacin, Cipro, Cifran",
            spectrum="Gram-negative (bao gồm Pseudomonas), một số Gram-positive",
            common_indications=["Nhiễm khuẩn đường tiết niệu", "Nhiễm khuẩn đường tiêu hóa", "Nhiễm khuẩn do Pseudomonas"],
            dosing_summary="400mg IV mỗi 12 giờ hoặc 500-750mg PO BID",
            resistance_notes="E. coli: R 50-60% tại VN, K. pneumoniae: R 55-65%"
        ),
        DrugInClass(
            name="Levofloxacin",
            vietnamese_name="Levofloxacin, Levoflox, Tavanic",
            spectrum="Gram-positive và Gram-negative (không bao gồm Pseudomonas tốt như ciprofloxacin)",
            common_indications=["Viêm phổi cộng đồng", "Viêm phổi bệnh viện", "Nhiễm khuẩn đường tiết niệu"],
            dosing_summary="500-750mg IV/PO mỗi 24 giờ",
            resistance_notes="E. coli: R 45-55% tại VN"
        ),
        DrugInClass(
            name="Moxifloxacin",
            vietnamese_name="Moxifloxacin, Avelox",
            spectrum="Gram-positive (bao gồm S. pneumoniae), Gram-negative, kỵ khí",
            common_indications=["Viêm phổi cộng đồng", "Nhiễm khuẩn da và mô mềm"],
            dosing_summary="400mg IV/PO mỗi 24 giờ",
            resistance_notes="Ít kháng hơn levofloxacin nhưng vẫn có nguy cơ"
        ),
    ],
    spectrum_summary="Phổ rộng: Gram-positive và Gram-negative, một số có hoạt tính với Pseudomonas và kỵ khí",
    common_indications=[
        "Nhiễm khuẩn đường tiết niệu",
        "Nhiễm khuẩn đường hô hấp",
        "Nhiễm khuẩn đường tiêu hóa",
        "Nhiễm khuẩn da và mô mềm"
    ],
    resistance_patterns="Kháng quinolone cao tại VN do sử dụng rộng rãi. E. coli: R 50-60%, K. pneumoniae: R 55-65%. Cơ chế: đột biến DNA gyrase/topoisomerase, efflux pumps.",
    clinical_notes="⚠️ Cảnh báo: QT prolongation, đứt gân, rối loạn thần kinh trung ương. Tránh dùng ở trẻ em và phụ nữ có thai. WHO khuyến cáo hạn chế sử dụng (WATCH group)."
)


# Macrolides
MACROLIDES = DrugClass(
    class_name="Macrolides",
    class_name_vi="Macrolide",
    description="Kháng sinh ức chế tổng hợp protein vi khuẩn",
    mechanism="Ức chế tổng hợp protein tại ribosome 50S",
    drugs=[
        DrugInClass(
            name="Azithromycin",
            vietnamese_name="Azithromycin, Zithromax, Azitro",
            spectrum="Gram-positive (một số), atypical pathogens (Chlamydia, Mycoplasma, Legionella)",
            common_indications=["Viêm phổi cộng đồng", "Nhiễm Chlamydia", "Nhiễm Mycoplasma"],
            dosing_summary="500mg IV/PO ngày 1, sau đó 250mg/ngày x 4 ngày",
            resistance_notes="S. pneumoniae: R 40-50% tại VN"
        ),
        DrugInClass(
            name="Clarithromycin",
            vietnamese_name="Clarithromycin, Klacid",
            spectrum="Gram-positive, atypical pathogens",
            common_indications=["Nhiễm khuẩn đường hô hấp", "Helicobacter pylori"],
            dosing_summary="500mg PO BID",
            resistance_notes="Kháng macrolide tăng do sử dụng rộng rãi"
        ),
        DrugInClass(
            name="Erythromycin",
            vietnamese_name="Erythromycin, Erythrocin",
            spectrum="Gram-positive, atypical pathogens",
            common_indications=["Nhiễm khuẩn đường hô hấp", "Nhiễm khuẩn da và mô mềm"],
            dosing_summary="250-500mg PO QID hoặc 1g IV mỗi 6 giờ",
            resistance_notes="S. aureus: R 40-50% tại VN"
        ),
    ],
    spectrum_summary="Chủ yếu Gram-positive và atypical pathogens (Chlamydia, Mycoplasma, Legionella)",
    common_indications=[
        "Viêm phổi cộng đồng",
        "Nhiễm khuẩn đường hô hấp trên",
        "Nhiễm Chlamydia",
        "Nhiễm Mycoplasma"
    ],
    resistance_patterns="Kháng macrolide tăng do sử dụng rộng rãi. S. pneumoniae: R 40-50%, S. aureus: R 40-50%. Cơ chế: methylase (erm), efflux pumps (mef).",
    clinical_notes="QT prolongation risk, đặc biệt khi kết hợp với các thuốc khác. Azithromycin có thời gian bán thải dài (68h)."
)


# Glycopeptides
GLYCOPEPTIDES = DrugClass(
    class_name="Glycopeptides",
    class_name_vi="Glycopeptide",
    description="Kháng sinh phổ Gram-positive, đặc biệt hiệu quả với MRSA",
    mechanism="Ức chế tổng hợp thành tế bào (peptidoglycan) ở Gram-positive",
    drugs=[
        DrugInClass(
            name="Vancomycin",
            vietnamese_name="Vancomycin, Vancocin",
            spectrum="Gram-positive: MRSA, MSSA, Enterococcus, Coagulase-negative staphylococci",
            common_indications=["Nhiễm khuẩn do MRSA", "Nhiễm khuẩn huyết", "Viêm màng não", "Nhiễm khuẩn liên quan catheter"],
            dosing_summary="15-20mg/kg IV mỗi 8-12 giờ (theo dõi nồng độ)",
            resistance_notes="VRE (Vancomycin-resistant Enterococcus) đang tăng: E. faecium R 60-70% tại VN"
        ),
        DrugInClass(
            name="Teicoplanin",
            vietnamese_name="Teicoplanin, Targocid",
            spectrum="Tương tự vancomycin: Gram-positive",
            common_indications=["Nhiễm khuẩn do MRSA", "Nhiễm khuẩn huyết"],
            dosing_summary="400mg IV x 2 lần/ngày ngày 1-3, sau đó 400mg/ngày",
            resistance_notes="Ít phổ biến hơn vancomycin tại VN"
        ),
    ],
    spectrum_summary="Chỉ có hoạt tính với Gram-positive (không có tác dụng với Gram-negative)",
    common_indications=[
        "Nhiễm khuẩn do MRSA",
        "Nhiễm khuẩn huyết",
        "Viêm màng não",
        "Nhiễm khuẩn liên quan thiết bị y tế"
    ],
    resistance_patterns="VRE (Vancomycin-resistant Enterococcus) đang tăng, đặc biệt E. faecium (R 60-70% tại VN). VRSA (Vancomycin-resistant S. aureus) hiếm nhưng đáng lo ngại.",
    clinical_notes="⚠️ Cần theo dõi nồng độ (TDM) để đảm bảo hiệu quả và tránh độc tính. Nguy cơ độc tính thận và thính giác ở liều cao."
)


# Aminoglycosides
AMINOGLYCOSIDES = DrugClass(
    class_name="Aminoglycosides",
    class_name_vi="Aminoglycoside",
    description="Kháng sinh phổ Gram-negative, thường dùng kết hợp",
    mechanism="Ức chế tổng hợp protein tại ribosome 30S",
    drugs=[
        DrugInClass(
            name="Gentamicin",
            vietnamese_name="Gentamicin, Garamycin",
            spectrum="Gram-negative (bao gồm Pseudomonas), một số Gram-positive (synergy)",
            common_indications=["Nhiễm khuẩn Gram-negative", "Nhiễm khuẩn huyết", "Nhiễm khuẩn đường tiết niệu"],
            dosing_summary="5-7mg/kg IV mỗi 24 giờ (hoặc 1.5-2mg/kg mỗi 8 giờ)",
            resistance_notes="E. coli: R 20-30% tại VN, K. pneumoniae: R 25-35%"
        ),
        DrugInClass(
            name="Amikacin",
            vietnamese_name="Amikacin, Amikin",
            spectrum="Gram-negative (bao gồm một số chủng kháng gentamicin), một số Gram-positive",
            common_indications=["Nhiễm khuẩn đa kháng", "Nhiễm khuẩn do vi khuẩn kháng gentamicin"],
            dosing_summary="15-20mg/kg IV mỗi 24 giờ",
            resistance_notes="Ít kháng hơn gentamicin: E. coli R 10-15%, K. pneumoniae R 15-20%"
        ),
        DrugInClass(
            name="Tobramycin",
            vietnamese_name="Tobramycin, Nebcin",
            spectrum="Gram-negative (đặc biệt tốt với Pseudomonas)",
            common_indications=["Nhiễm khuẩn do Pseudomonas", "Nhiễm khuẩn đường hô hấp"],
            dosing_summary="5-7mg/kg IV mỗi 24 giờ",
            resistance_notes="Pseudomonas: R 15-25% tại VN"
        ),
    ],
    spectrum_summary="Chủ yếu Gram-negative (bao gồm Pseudomonas), có thể kết hợp với beta-lactam để tăng hiệu quả với Gram-positive",
    common_indications=[
        "Nhiễm khuẩn Gram-negative",
        "Nhiễm khuẩn huyết",
        "Nhiễm khuẩn do Pseudomonas",
        "Kết hợp với beta-lactam cho nhiễm khuẩn nặng"
    ],
    resistance_patterns="Kháng aminoglycoside do enzyme modification (aminoglycoside-modifying enzymes). Gentamicin: E. coli R 20-30%, K. pneumoniae R 25-35%. Amikacin ít kháng hơn.",
    clinical_notes="⚠️ Độc tính thận và thính giác. Cần theo dõi nồng độ (TDM) và chức năng thận. Tránh dùng ở suy thận nặng."
)


# Lincosamides
LINCOSAMIDES = DrugClass(
    class_name="Lincosamides",
    class_name_vi="Lincosamide",
    description="Kháng sinh phổ Gram-positive và kỵ khí",
    mechanism="Ức chế tổng hợp protein tại ribosome 50S",
    drugs=[
        DrugInClass(
            name="Clindamycin",
            vietnamese_name="Clindamycin, Dalacin, Cleocin",
            spectrum="Gram-positive (bao gồm MRSA), kỵ khí (Bacteroides)",
            common_indications=["Nhiễm khuẩn da và mô mềm", "Nhiễm khuẩn kỵ khí", "Nhiễm khuẩn do MRSA (PO)"],
            dosing_summary="600-900mg IV mỗi 8 giờ hoặc 300-450mg PO QID",
            resistance_notes="S. aureus: R 15-25% tại VN (inducible resistance)"
        ),
    ],
    spectrum_summary="Gram-positive (bao gồm MRSA) và kỵ khí (Bacteroides fragilis)",
    common_indications=[
        "Nhiễm khuẩn da và mô mềm",
        "Nhiễm khuẩn kỵ khí",
        "Nhiễm khuẩn do MRSA (đường uống)"
    ],
    resistance_patterns="Inducible resistance ở S. aureus (D-test). S. aureus: R 15-25% tại VN. Bacteroides fragilis: R 10-15%.",
    clinical_notes="Nguy cơ viêm đại tràng giả mạc (C. difficile). Cần theo dõi triệu chứng tiêu chảy."
)


# Tetracyclines
TETRACYCLINES = DrugClass(
    class_name="Tetracyclines",
    class_name_vi="Tetracycline",
    description="Kháng sinh phổ rộng, ức chế tổng hợp protein",
    mechanism="Ức chế tổng hợp protein tại ribosome 30S",
    drugs=[
        DrugInClass(
            name="Doxycycline",
            vietnamese_name="Doxycycline, Vibramycin",
            spectrum="Gram-positive, Gram-negative, atypical pathogens, rickettsia, spirochetes",
            common_indications=["Viêm phổi cộng đồng", "Nhiễm khuẩn do rickettsia", "Nhiễm khuẩn đường tiết niệu"],
            dosing_summary="100mg PO BID hoặc 200mg IV/PO mỗi 24 giờ",
            resistance_notes="Kháng tetracycline phổ biến do sử dụng rộng rãi trong quá khứ"
        ),
        DrugInClass(
            name="Tigecycline",
            vietnamese_name="Tigecycline, Tygacil",
            spectrum="Phổ rộng: Gram-positive (bao gồm MRSA, VRE), Gram-negative (bao gồm ESBL), kỵ khí",
            common_indications=["Nhiễm khuẩn đa kháng", "Nhiễm khuẩn ổ bụng", "Nhiễm khuẩn da và mô mềm"],
            dosing_summary="100mg IV ngày 1, sau đó 50mg IV mỗi 12 giờ",
            resistance_notes="Ít kháng hơn do cơ chế mới, nhưng vẫn có nguy cơ"
        ),
    ],
    spectrum_summary="Phổ rộng: Gram-positive, Gram-negative, atypical pathogens, rickettsia, spirochetes",
    common_indications=[
        "Viêm phổi cộng đồng",
        "Nhiễm khuẩn do rickettsia",
        "Nhiễm khuẩn đường tiết niệu",
        "Nhiễm khuẩn đa kháng (tigecycline)"
    ],
    resistance_patterns="Kháng tetracycline phổ biến do sử dụng rộng rãi trong quá khứ. Cơ chế: efflux pumps, ribosomal protection. Tigecycline ít kháng hơn.",
    clinical_notes="⚠️ Tránh dùng ở trẻ em < 8 tuổi và phụ nữ có thai (ảnh hưởng răng và xương). Tigecycline có nguy cơ tử vong cao hơn → chỉ dùng khi không có lựa chọn khác."
)


# Others
OTHER_ANTIBIOTICS = DrugClass(
    class_name="Others",
    class_name_vi="Khác",
    description="Các kháng sinh không thuộc các nhóm chính",
    mechanism="Nhiều cơ chế khác nhau",
    drugs=[
        DrugInClass(
            name="Metronidazole",
            vietnamese_name="Metronidazole, Flagyl",
            spectrum="Kỵ khí (Bacteroides, Clostridium), protozoa",
            common_indications=["Nhiễm khuẩn kỵ khí", "Nhiễm khuẩn ổ bụng", "Nhiễm trùng đường tiêu hóa"],
            dosing_summary="500mg IV/PO mỗi 8 giờ",
            resistance_notes="Bacteroides fragilis: R 5-10%"
        ),
        DrugInClass(
            name="Linezolid",
            vietnamese_name="Linezolid, Zyvox",
            spectrum="Gram-positive (bao gồm MRSA, VRE)",
            common_indications=["Nhiễm khuẩn do MRSA/VRE", "Viêm phổi bệnh viện", "Nhiễm khuẩn da và mô mềm"],
            dosing_summary="600mg IV/PO mỗi 12 giờ",
            resistance_notes="Rất ít kháng (< 1%)"
        ),
        DrugInClass(
            name="Colistin",
            vietnamese_name="Colistin, Polymyxin E",
            spectrum="Gram-negative (bao gồm đa kháng: KPC, NDM)",
            common_indications=["Nhiễm khuẩn đa kháng", "Nhiễm khuẩn do carbapenem-resistant Enterobacteriaceae"],
            dosing_summary="2.5-5mg/kg IV mỗi 8-12 giờ (theo colistin base activity)",
            resistance_notes="A. baumannii: R 5-10% tại VN"
        ),
    ],
    spectrum_summary="Nhiều phổ khác nhau tùy thuộc vào từng thuốc",
    common_indications=[
        "Nhiễm khuẩn kỵ khí",
        "Nhiễm khuẩn đa kháng",
        "Nhiễm khuẩn do vi khuẩn kháng thuốc"
    ],
    resistance_patterns="Tùy thuộc vào từng thuốc. Linezolid rất ít kháng. Colistin đang có nguy cơ kháng tăng.",
    clinical_notes="Metronidazole: tránh rượu. Linezolid: nguy cơ giảm tiểu cầu, serotonin syndrome. Colistin: độc tính thận và thần kinh."
)


# Tất cả các nhóm thuốc
ALL_DRUG_CLASSES = [
    BETA_LACTAMS,
    FLUOROQUINOLONES,
    MACROLIDES,
    GLYCOPEPTIDES,
    AMINOGLYCOSIDES,
    LINCOSAMIDES,
    TETRACYCLINES,
    OTHER_ANTIBIOTICS
]


def get_drug_class_by_name(class_name: str) -> Optional[DrugClass]:
    """Lấy thông tin nhóm thuốc theo tên"""
    for drug_class in ALL_DRUG_CLASSES:
        if drug_class.class_name.lower() == class_name.lower():
            return drug_class
    return None


def get_all_drug_names() -> List[str]:
    """Lấy danh sách tất cả tên thuốc trong tất cả các nhóm"""
    all_drugs = []
    for drug_class in ALL_DRUG_CLASSES:
        for drug in drug_class.drugs:
            all_drugs.append(drug.name)
    return all_drugs
