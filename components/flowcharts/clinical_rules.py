"""
Clinical Decision Rules Flowcharts
Pre-built flowcharts for important clinical decision rules
"""

from typing import List, Tuple
from components.flowchart import FlowchartNode, FlowchartEdge, NodeType


def create_wells_pe_flowchart() -> Tuple[List[FlowchartNode], List[FlowchartEdge]]:
    """
    Create Wells PE Score flowchart
    
    Dựa trên:
    - Wells PS, et al. Derivation of a simple clinical model to categorize patients probability of pulmonary embolism (1998)
    - ESC/ERS Guidelines for Diagnosis and Management of Acute Pulmonary Embolism (2019, 2023)
    - ATS/ERS Clinical Practice Guidelines on Pulmonary Embolism
    """
    nodes = [
        FlowchartNode("start", "Nghi ngờ PE?", NodeType.START, icon="🫁"),
        FlowchartNode("wells", "Tính Wells Score", NodeType.ACTION, icon="📊"),
        FlowchartNode("low", "Wells ≤4\n(Nguy cơ thấp)", NodeType.DECISION, icon="🟢"),
        FlowchartNode("moderate", "Wells 5-6\n(Nguy cơ trung bình)", NodeType.DECISION, icon="🟡"),
        FlowchartNode("high", "Wells ≥7\n(Nguy cơ cao)", NodeType.DECISION, icon="🔴"),
        FlowchartNode("dimer_low", "D-dimer", NodeType.TEST, icon="🧪"),
        FlowchartNode("dimer_neg", "D-dimer (-)", NodeType.ACTION, color="#28a745", icon="✅"),
        FlowchartNode("dimer_pos", "D-dimer (+)", NodeType.ACTION, color="#ffc107", icon="⚠️"),
        FlowchartNode("ctpa", "CTPA", NodeType.TEST, icon="📷"),
        FlowchartNode("ctpa_pos", "CTPA (+)\nĐiều trị", NodeType.ACTION, color="#dc3545", icon="💊"),
        FlowchartNode("ctpa_neg", "CTPA (-)\nLoại trừ PE", NodeType.ACTION, color="#28a745", icon="✅"),
        FlowchartNode("no_pe", "Loại trừ PE", NodeType.END, color="#28a745", icon="🏠"),
        FlowchartNode("treat_pe", "Điều trị PE", NodeType.END, color="#dc3545", icon="💊"),
    ]
    
    edges = [
        FlowchartEdge("start", "wells", ""),
        FlowchartEdge("wells", "low", "≤4"),
        FlowchartEdge("wells", "moderate", "5-6"),
        FlowchartEdge("wells", "high", "≥7"),
        FlowchartEdge("low", "dimer_low", ""),
        FlowchartEdge("moderate", "dimer_low", ""),
        FlowchartEdge("high", "ctpa", "Bỏ qua D-dimer"),
        FlowchartEdge("dimer_low", "dimer_neg", "Âm tính"),
        FlowchartEdge("dimer_low", "dimer_pos", "Dương tính"),
        FlowchartEdge("dimer_neg", "no_pe", ""),
        FlowchartEdge("dimer_pos", "ctpa", ""),
        FlowchartEdge("ctpa", "ctpa_pos", "Có PE"),
        FlowchartEdge("ctpa", "ctpa_neg", "Không có PE"),
        FlowchartEdge("ctpa_pos", "treat_pe", ""),
        FlowchartEdge("ctpa_neg", "no_pe", ""),
    ]
    
    return nodes, edges


def create_perc_flowchart() -> Tuple[List[FlowchartNode], List[FlowchartEdge]]:
    """
    Create PERC Rule flowchart
    
    Dựa trên:
    - Kline JA, et al. Clinical criteria to prevent unnecessary diagnostic testing in emergency department patients with suspected pulmonary embolism (2004)
    - ESC/ERS Guidelines for Diagnosis and Management of Acute Pulmonary Embolism (2019, 2023)
    """
    nodes = [
        FlowchartNode("start", "Nghi ngờ PE?", NodeType.START, icon="🫁"),
        FlowchartNode("perc", "Đánh giá PERC", NodeType.ACTION, icon="📋"),
        FlowchartNode("all_neg", "Tất cả PERC (-)", NodeType.DECISION, icon="🟢"),
        FlowchartNode("any_pos", "Có PERC (+)", NodeType.DECISION, icon="🟡"),
        FlowchartNode("no_pe", "Loại trừ PE\nKhông cần test", NodeType.END, color="#28a745", icon="✅"),
        FlowchartNode("wells", "Tính Wells Score", NodeType.ACTION, icon="📊"),
        FlowchartNode("wells_low", "Wells ≤4", NodeType.DECISION, icon="🟢"),
        FlowchartNode("wells_high", "Wells >4", NodeType.DECISION, icon="🔴"),
        FlowchartNode("dimer", "D-dimer", NodeType.TEST, icon="🧪"),
        FlowchartNode("ctpa", "CTPA", NodeType.TEST, icon="📷"),
        FlowchartNode("treat", "Điều trị PE", NodeType.END, color="#dc3545", icon="💊"),
    ]
    
    edges = [
        FlowchartEdge("start", "perc", ""),
        FlowchartEdge("perc", "all_neg", "Tất cả (-)"),
        FlowchartEdge("perc", "any_pos", "Có (+)"),
        FlowchartEdge("all_neg", "no_pe", ""),
        FlowchartEdge("any_pos", "wells", ""),
        FlowchartEdge("wells", "wells_low", "≤4"),
        FlowchartEdge("wells", "wells_high", ">4"),
        FlowchartEdge("wells_low", "dimer", ""),
        FlowchartEdge("wells_high", "ctpa", ""),
        FlowchartEdge("dimer", "ctpa", "D-dimer (+)"),
        FlowchartEdge("dimer", "no_pe", "D-dimer (-)"),
        FlowchartEdge("ctpa", "treat", "CTPA (+)"),
        FlowchartEdge("ctpa", "no_pe", "CTPA (-)"),
    ]
    
    return nodes, edges


def create_cha2ds2vasc_flowchart() -> Tuple[List[FlowchartNode], List[FlowchartEdge]]:
    """
    Create CHA₂DS₂-VASc Score flowchart
    
    Dựa trên:
    - Lip GY, et al. Refining clinical risk stratification for predicting stroke and thromboembolism in atrial fibrillation (2009)
    - AHA/ACC/HRS Guideline for Management of Patients with Atrial Fibrillation (2019, 2023)
    - ESC Guidelines for Management of Atrial Fibrillation (2020, 2023)
    """
    nodes = [
        FlowchartNode("start", "Rung nhĩ?", NodeType.START, icon="❤️"),
        FlowchartNode("calc", "Tính CHA₂DS₂-VASc", NodeType.ACTION, icon="📊"),
        FlowchartNode("score0", "Score = 0\n(Nam)", NodeType.DECISION, icon="🟢"),
        FlowchartNode("score1", "Score = 1\n(Nam)", NodeType.DECISION, icon="🟡"),
        FlowchartNode("score2", "Score ≥2", NodeType.DECISION, icon="🔴"),
        FlowchartNode("no_anticoag", "Không kháng đông\n(hoặc Aspirin)", NodeType.END, color="#28a745", icon="✅"),
        FlowchartNode("consider", "Cân nhắc kháng đông", NodeType.ACTION, color="#ffc107", icon="⚠️"),
        FlowchartNode("hasbled", "Tính HAS-BLED", NodeType.ACTION, icon="📊"),
        FlowchartNode("anticoag", "KHUYẾN CÁO KHÁNG ĐÔNG\n(NOAC hoặc Warfarin)", NodeType.END, color="#dc3545", icon="💊"),
    ]
    
    edges = [
        FlowchartEdge("start", "calc", ""),
        FlowchartEdge("calc", "score0", "= 0"),
        FlowchartEdge("calc", "score1", "= 1"),
        FlowchartEdge("calc", "score2", "≥ 2"),
        FlowchartEdge("score0", "no_anticoag", ""),
        FlowchartEdge("score1", "consider", ""),
        FlowchartEdge("score2", "hasbled", ""),
        FlowchartEdge("hasbled", "anticoag", ""),
    ]
    
    return nodes, edges


def create_sepsis_flowchart() -> Tuple[List[FlowchartNode], List[FlowchartEdge]]:
    """
    Create Sepsis-3 flowchart
    
    Dựa trên:
    - Singer M, et al. The Third International Consensus Definitions for Sepsis and Septic Shock (Sepsis-3) (2016)
    - Surviving Sepsis Campaign (SSC) Guidelines 2021 - International Guidelines for Management of Sepsis and Septic Shock
    - IDSA/SCCM Guidelines
    """
    nodes = [
        FlowchartNode("start", "Nghi ngờ nhiễm trùng?", NodeType.START, icon="🦠"),
        FlowchartNode("qsofa", "Tính qSOFA", NodeType.ACTION, icon="📊"),
        FlowchartNode("qsofa_pos", "qSOFA ≥2", NodeType.DECISION, icon="🔴"),
        FlowchartNode("qsofa_neg", "qSOFA <2", NodeType.DECISION, icon="🟢"),
        FlowchartNode("sofa", "Tính SOFA", NodeType.ACTION, icon="📊"),
        FlowchartNode("sofa_pos", "SOFA ≥2", NodeType.DECISION, icon="🔴"),
        FlowchartNode("sepsis", "SEPSIS\n(SOFA ≥2)", NodeType.ACTION, color="#dc3545", icon="🚨"),
        FlowchartNode("shock", "Septic Shock?", NodeType.DECISION, icon="⚠️"),
        FlowchartNode("septic_shock", "SEPTIC SHOCK", NodeType.ACTION, color="#dc3545", icon="🚨"),
        FlowchartNode("bundle", "1-Hour Bundle", NodeType.ACTION, icon="💊"),
        FlowchartNode("monitor", "Theo dõi", NodeType.END, color="#17a2b8", icon="👁️"),
        FlowchartNode("no_sepsis", "Không phải Sepsis", NodeType.END, color="#28a745", icon="✅"),
    ]
    
    edges = [
        FlowchartEdge("start", "qsofa", ""),
        FlowchartEdge("qsofa", "qsofa_pos", "≥2"),
        FlowchartEdge("qsofa", "qsofa_neg", "<2"),
        FlowchartEdge("qsofa_pos", "sofa", ""),
        FlowchartEdge("qsofa_neg", "no_sepsis", "Nguy cơ thấp"),
        FlowchartEdge("sofa", "sofa_pos", "≥2"),
        FlowchartEdge("sofa", "no_sepsis", "<2"),
        FlowchartEdge("sofa_pos", "sepsis", ""),
        FlowchartEdge("sepsis", "shock", ""),
        FlowchartEdge("shock", "septic_shock", "MAP <65 + Lactate >2"),
        FlowchartEdge("shock", "bundle", "Không shock"),
        FlowchartEdge("septic_shock", "bundle", ""),
        FlowchartEdge("bundle", "monitor", ""),
    ]
    
    return nodes, edges


def create_stroke_flowchart() -> Tuple[List[FlowchartNode], List[FlowchartEdge]]:
    """
    Create Acute Stroke flowchart
    
    Dựa trên:
    - AHA/ASA Guidelines for Early Management of Patients with Acute Ischemic Stroke (2019, 2023)
    - AHA/ASA Guidelines for Management of Spontaneous Intracerebral Hemorrhage (2022)
    - European Stroke Organisation (ESO) Guidelines for Management of Acute Ischemic Stroke (2021)
    """
    nodes = [
        FlowchartNode("start", "Đột quỵ cấp?", NodeType.START, icon="🧠"),
        FlowchartNode("time", "Thời gian khởi phát?", NodeType.DECISION, icon="⏰"),
        FlowchartNode("within_4.5", "< 4.5 giờ", NodeType.DECISION, icon="🟢"),
        FlowchartNode("within_24", "4.5-24 giờ", NodeType.DECISION, icon="🟡"),
        FlowchartNode("over_24", "> 24 giờ", NodeType.DECISION, icon="🔴"),
        FlowchartNode("nihss", "Tính NIHSS", NodeType.ACTION, icon="📊"),
        FlowchartNode("ct", "CT não", NodeType.TEST, icon="📷"),
        FlowchartNode("no_ich", "Không ICH", NodeType.DECISION, icon="✅"),
        FlowchartNode("ich", "Có ICH", NodeType.DECISION, icon="🔴"),
        FlowchartNode("tpa", "tPA", NodeType.ACTION, color="#dc3545", icon="💊"),
        FlowchartNode("thrombectomy", "Thrombectomy", NodeType.ACTION, color="#dc3545", icon="🔧"),
        FlowchartNode("supportive", "Điều trị hỗ trợ", NodeType.ACTION, color="#17a2b8", icon="💊"),
        FlowchartNode("monitor", "Theo dõi", NodeType.END, color="#17a2b8", icon="👁️"),
    ]
    
    edges = [
        FlowchartEdge("start", "time", ""),
        FlowchartEdge("time", "within_4.5", "< 4.5h"),
        FlowchartEdge("time", "within_24", "4.5-24h"),
        FlowchartEdge("time", "over_24", "> 24h"),
        FlowchartEdge("within_4.5", "nihss", ""),
        FlowchartEdge("within_24", "nihss", ""),
        FlowchartEdge("over_24", "supportive", ""),
        FlowchartEdge("nihss", "ct", ""),
        FlowchartEdge("ct", "no_ich", "Không ICH"),
        FlowchartEdge("ct", "ich", "Có ICH"),
        FlowchartEdge("no_ich", "tpa", "Chỉ định tPA"),
        FlowchartEdge("no_ich", "thrombectomy", "Chỉ định thrombectomy"),
        FlowchartEdge("ich", "supportive", ""),
        FlowchartEdge("tpa", "monitor", ""),
        FlowchartEdge("thrombectomy", "monitor", ""),
        FlowchartEdge("supportive", "monitor", ""),
    ]
    
    return nodes, edges


def create_aki_flowchart() -> Tuple[List[FlowchartNode], List[FlowchartEdge]]:
    """
    Create AKI diagnostic flowchart
    
    Dựa trên:
    - KDIGO (Kidney Disease: Improving Global Outcomes) Clinical Practice Guideline for Acute Kidney Injury (2012, 2024)
    - AKI Network (AKIN) Criteria
    - RIFLE Criteria
    """
    nodes = [
        FlowchartNode("start", "Nghi ngờ AKI?", NodeType.START, icon="🫘"),
        FlowchartNode("stage", "Phân loại AKI\n(KDIGO)", NodeType.ACTION, icon="📊"),
        FlowchartNode("stage1", "Stage 1", NodeType.DECISION, icon="🟡"),
        FlowchartNode("stage2", "Stage 2", NodeType.DECISION, icon="🟠"),
        FlowchartNode("stage3", "Stage 3", NodeType.DECISION, icon="🔴"),
        FlowchartNode("fena", "FENa", NodeType.TEST, icon="🧪"),
        FlowchartNode("prerenal", "Prerenal\n(FENa <1%)", NodeType.ACTION, color="#17a2b8", icon="💧"),
        FlowchartNode("intrinsic", "Intrinsic\n(FENa >2%)", NodeType.ACTION, color="#ffc107", icon="⚠️"),
        FlowchartNode("postrenal", "Postrenal", NodeType.ACTION, color="#dc3545", icon="🔴"),
        FlowchartNode("treat", "Điều trị", NodeType.END, color="#28a745", icon="💊"),
    ]
    
    edges = [
        FlowchartEdge("start", "stage", ""),
        FlowchartEdge("stage", "stage1", "Stage 1"),
        FlowchartEdge("stage", "stage2", "Stage 2"),
        FlowchartEdge("stage", "stage3", "Stage 3"),
        FlowchartEdge("stage1", "fena", ""),
        FlowchartEdge("stage2", "fena", ""),
        FlowchartEdge("stage3", "fena", ""),
        FlowchartEdge("fena", "prerenal", "< 1%"),
        FlowchartEdge("fena", "intrinsic", "> 2%"),
        FlowchartEdge("fena", "postrenal", "Check obstruction"),
        FlowchartEdge("prerenal", "treat", "Volume, BP"),
        FlowchartEdge("intrinsic", "treat", "Nephrotoxins"),
        FlowchartEdge("postrenal", "treat", "Relieve obstruction"),
    ]
    
    return nodes, edges


def create_curb65_flowchart() -> Tuple[List[FlowchartNode], List[FlowchartEdge]]:
    """
    Create CURB-65 flowchart
    
    Dựa trên:
    - Lim WS, et al. Defining community acquired pneumonia severity on presentation to hospital (2003)
    - IDSA/ATS Guidelines for Community-Acquired Pneumonia (2019)
    - BTS (British Thoracic Society) Guidelines for Management of Community Acquired Pneumonia (2009, 2015)
    """
    nodes = [
        FlowchartNode("start", "Viêm phổi cộng đồng?", NodeType.START, icon="🫁"),
        FlowchartNode("curb65", "Tính CURB-65", NodeType.ACTION, icon="📊"),
        FlowchartNode("score0", "Score 0", NodeType.DECISION, icon="🟢"),
        FlowchartNode("score1_2", "Score 1-2", NodeType.DECISION, icon="🟡"),
        FlowchartNode("score3_5", "Score 3-5", NodeType.DECISION, icon="🔴"),
        FlowchartNode("outpatient", "Điều trị ngoại trú", NodeType.END, color="#28a745", icon="🏠"),
        FlowchartNode("inpatient", "Nhập viện", NodeType.END, color="#ffc107", icon="🏥"),
        FlowchartNode("icu", "ICU", NodeType.END, color="#dc3545", icon="🚨"),
    ]
    
    edges = [
        FlowchartEdge("start", "curb65", ""),
        FlowchartEdge("curb65", "score0", "0"),
        FlowchartEdge("curb65", "score1_2", "1-2"),
        FlowchartEdge("curb65", "score3_5", "3-5"),
        FlowchartEdge("score0", "outpatient", ""),
        FlowchartEdge("score1_2", "inpatient", ""),
        FlowchartEdge("score3_5", "icu", ""),
    ]
    
    return nodes, edges


def create_shock_flowchart() -> Tuple[List[FlowchartNode], List[FlowchartEdge]]:
    """
    Create shock / hypotension resuscitation flowchart (initial ED/ICU approach)
    
    Dựa trên:
    - Surviving Sepsis Campaign (SSC) Guidelines 2021
    - ACLS (Advanced Cardiac Life Support) Protocol
    - ATLS (Advanced Trauma Life Support) - Shock Management
    - ESC/ESICM Guidelines on Shock Management
    """
    nodes = [
        FlowchartNode("start", "SBP <90 mmHg\nhoặc MAP <65?", NodeType.START, icon="📉"),
        FlowchartNode("airway", "Airway & Breathing", NodeType.ACTION, icon="🫁"),
        FlowchartNode("iv_access", "2 đường IV lớn\n+ lấy xét nghiệm", NodeType.ACTION, icon="💉"),
        FlowchartNode("fluid_bolus", "Bolus dịch 30 ml/kg\nCrystalloid", NodeType.ACTION, color="#17a2b8", icon="💧"),
        FlowchartNode("responsive", "Đáp ứng với dịch?", NodeType.DECISION, icon="❓"),
        FlowchartNode("reassess", "Theo dõi & tìm nguyên nhân", NodeType.ACTION, icon="👁️"),
        FlowchartNode("no_response", "Không đáp ứng\nhoặc phù phổi", NodeType.DECISION, icon="⚠️"),
        FlowchartNode("vasopressor", "Bắt đầu Vasopressor\n(Noradrenaline)", NodeType.ACTION, color="#dc3545", icon="💊"),
        FlowchartNode("identify_shock", "Phân loại shock:\nSeptic / Cardiogenic /\nHypovolemic / Obstructive", NodeType.ACTION, icon="🧪"),
        FlowchartNode("monitor", "ICU / Theo dõi sát\nLactate, UO, MAP", NodeType.END, color="#17a2b8", icon="🏥"),
    ]
    
    edges = [
        FlowchartEdge("start", "airway", "Có"),
        FlowchartEdge("airway", "iv_access", ""),
        FlowchartEdge("iv_access", "fluid_bolus", ""),
        FlowchartEdge("fluid_bolus", "responsive", "Sau 30 ml/kg"),
        FlowchartEdge("responsive", "reassess", "Có cải thiện"),
        FlowchartEdge("responsive", "no_response", "Không cải thiện"),
        FlowchartEdge("no_response", "vasopressor", ""),
        FlowchartEdge("vasopressor", "identify_shock", ""),
        FlowchartEdge("identify_shock", "monitor", ""),
    ]
    
    return nodes, edges


def create_gi_bleed_flowchart() -> Tuple[List[FlowchartNode], List[FlowchartEdge]]:
    """
    Create upper GI bleeding initial management flowchart
    
    Dựa trên:
    - ACG (American College of Gastroenterology) Clinical Guideline: Management of Acute Upper GI Bleeding 2021
    - AASLD (American Association for the Study of Liver Diseases) Practice Guidelines
    - BSG (British Society of Gastroenterology) Guidelines for Management of Upper GI Bleeding
    - International Consensus Recommendations on Management of Upper GI Bleeding
    """
    nodes = [
        FlowchartNode("start", "Nghi ngờ XHTH trên?", NodeType.START, icon="🩸"),
        FlowchartNode("resus", "Resuscitation:\nAirway, 2 đường IV,\nBolus dịch", NodeType.ACTION, icon="🚑"),
        FlowchartNode("risk", "Đánh giá huyết động\n& nguy cơ cao", NodeType.DECISION, icon="⚠️"),
        FlowchartNode("high_risk", "Huyết động không ổn\nhoặc Hb rất thấp", NodeType.DECISION, icon="🔴"),
        FlowchartNode("transfuse", "Truyền máu PRBC\n(đích Hb ≥7-8 g/dL)", NodeType.ACTION, color="#dc3545", icon="💉"),
        FlowchartNode("ppi", "Bolus + truyền PPI\n(Esomeprazole)", NodeType.ACTION, icon="💊"),
        FlowchartNode("endoscopy", "Nội soi trong 24h\n(≤12h nếu nguy cơ cao)", NodeType.TEST, icon="📷"),
        FlowchartNode("low_risk", "Nguy cơ thấp /\nổn định", NodeType.DECISION, icon="🟢"),
        FlowchartNode("discharge", "Cân nhắc điều trị\nngoại trú / theo dõi\nngắn hạn", NodeType.END, color="#28a745", icon="🏠"),
        FlowchartNode("admit", "Nhập viện / ICU\nTheo dõi & can thiệp", NodeType.END, color="#17a2b8", icon="🏥"),
    ]
    
    edges = [
        FlowchartEdge("start", "resus", ""),
        FlowchartEdge("resus", "risk", ""),
        FlowchartEdge("risk", "high_risk", "Không ổn định"),
        FlowchartEdge("risk", "low_risk", "Ổn định"),
        FlowchartEdge("high_risk", "transfuse", ""),
        FlowchartEdge("transfuse", "ppi", ""),
        FlowchartEdge("ppi", "endoscopy", ""),
        FlowchartEdge("low_risk", "ppi", "Có viêm/loét\nnghi ngờ"),
        FlowchartEdge("endoscopy", "admit", "Tổn thương\nnguy cơ cao"),
        FlowchartEdge("endoscopy", "discharge", "Nguy cơ thấp"),
    ]
    
    return nodes, edges


def create_dka_flowchart() -> Tuple[List[FlowchartNode], List[FlowchartEdge]]:
    """
    Create DKA initial management flowchart
    
    Dựa trên:
    - ADA (American Diabetes Association) Standards of Medical Care in Diabetes 2024
    - ISPAD (International Society for Pediatric and Adolescent Diabetes) Clinical Practice Consensus Guidelines
    - Joint British Diabetes Societies (JBDS) Guidelines for Management of DKA
    - Endocrine Society Clinical Practice Guideline on Diabetic Ketoacidosis
    """
    nodes = [
        FlowchartNode("start", "Nghi ngờ DKA?", NodeType.START, icon="🍭"),
        FlowchartNode("labs", "Lấy xét nghiệm:\nGlucose, ABG/VBG,\nĐiện giải, Ketone", NodeType.TEST, icon="🧪"),
        FlowchartNode("confirm", "Glucose >250,\npH <7.3,\nHCO3- <18,\nKetone (+)", NodeType.DECISION, icon="📊"),
        FlowchartNode("no_dka", "Không DKA\nTìm chẩn đoán khác", NodeType.END, color="#28a745", icon="✅"),
        FlowchartNode("fluid", "Bolus NS 0.9%\n15-20 ml/kg (1-1.5L)", NodeType.ACTION, color="#17a2b8", icon="💧"),
        FlowchartNode("insulin", "Bắt đầu Insulin\n0.1 U/kg/h (IV)", NodeType.ACTION, color="#dc3545", icon="💉"),
        FlowchartNode("potassium", "Đánh giá K+ và\nBổ sung nếu cần", NodeType.ACTION, icon="🧂"),
        FlowchartNode("monitor", "Theo dõi:\nGlucose, K+, pH,\nAnion gap", NodeType.ACTION, icon="👁️"),
        FlowchartNode("resolve", "DKA giải quyết:\npH >7.3,\nHCO3- >18,\nAnion gap đóng", NodeType.DECISION, icon="🟢"),
        FlowchartNode("transition", "Chuyển sang SC\nInsulin & ăn uống", NodeType.END, color="#17a2b8", icon="🍽️"),
    ]
    
    edges = [
        FlowchartEdge("start", "labs", ""),
        FlowchartEdge("labs", "confirm", ""),
        FlowchartEdge("confirm", "no_dka", "Không đủ tiêu chuẩn"),
        FlowchartEdge("confirm", "fluid", "DKA xác định"),
        FlowchartEdge("fluid", "insulin", "Sau bolus đầu"),
        FlowchartEdge("insulin", "potassium", ""),
        FlowchartEdge("potassium", "monitor", ""),
        FlowchartEdge("monitor", "resolve", "Đánh giá định kỳ"),
        FlowchartEdge("resolve", "transition", "Tiêu chuẩn đạt"),
    ]
    
    return nodes, edges


def create_copd_exacerbation_flowchart() -> Tuple[List[FlowchartNode], List[FlowchartEdge]]:
    """
    Create COPD Exacerbation initial management flowchart

    Dựa trên:
    - GOLD (Global Initiative for Chronic Obstructive Lung Disease) Report 2024
    - ERS/ATS Guidelines on COPD Exacerbations
    """
    nodes = [
        FlowchartNode("start", "Nghi đợt cấp COPD?", NodeType.START, icon="🫁"),
        FlowchartNode("severity", "Đánh giá mức độ nặng:\nKhó thở, SpO₂, RR, Huyết động", NodeType.DECISION, icon="⚠️"),
        FlowchartNode("mild_mod", "Nhẹ / Trung bình", NodeType.DECISION, icon="🟡"),
        FlowchartNode("severe", "Nặng / Đe dọa suy hô hấp", NodeType.DECISION, icon="🔴"),
        FlowchartNode("bronchodilator", "Khí dung SABA ± SAMA\n(VD: Salbutamol + Ipratropium)", NodeType.ACTION, icon="🌬️"),
        FlowchartNode("steroid", "Corticosteroid toàn thân\n(VD: Prednisone 40mg x 5 ngày)", NodeType.ACTION, icon="💊"),
        FlowchartNode("antibiotic", "Cân nhắc kháng sinh nếu:\nĐờm mủ / Tăng lượng đờm / Nhiễm trùng", NodeType.ACTION, icon="🧫"),
        FlowchartNode("oxygen", "Oxy mục tiêu SpO₂ 88-92%", NodeType.ACTION, icon="🧷"),
        FlowchartNode("niv", "Cân nhắc NIPPV (BiPAP)\nNếu PaCO₂ tăng / Toan hô hấp", NodeType.ACTION, icon="💨"),
        FlowchartNode("admit", "Nhập viện / ICU\nNếu nặng", NodeType.END, color="#dc3545", icon="🏥"),
        FlowchartNode("discharge", "Điều trị ngoại trú\nTheo dõi sát", NodeType.END, color="#28a745", icon="🏠"),
    ]

    edges = [
        FlowchartEdge("start", "severity", ""),
        FlowchartEdge("severity", "mild_mod", "Nhẹ / Trung bình"),
        FlowchartEdge("severity", "severe", "Nặng / Nguy kịch"),
        FlowchartEdge("mild_mod", "bronchodilator", ""),
        FlowchartEdge("bronchodilator", "steroid", ""),
        FlowchartEdge("steroid", "antibiotic", "Có chỉ định"),
        FlowchartEdge("steroid", "discharge", "Không chỉ định KS\nỔn định"),
        FlowchartEdge("antibiotic", "discharge", "Ổn định"),
        FlowchartEdge("severe", "oxygen", ""),
        FlowchartEdge("oxygen", "niv", "PaCO₂↑ / Toan hô hấp"),
        FlowchartEdge("niv", "admit", "Cần ICU / NIPPV"),
        FlowchartEdge("oxygen", "admit", "Không đáp ứng / Bệnh nền nặng"),
    ]

    return nodes, edges


def create_asthma_exacerbation_flowchart() -> Tuple[List[FlowchartNode], List[FlowchartEdge]]:
    """
    Create Acute Asthma Exacerbation management flowchart

    Dựa trên:
    - GINA (Global Initiative for Asthma) Strategy 2024
    - ERS/ATS Guidelines on Severe Asthma Exacerbations
    """
    nodes = [
        FlowchartNode("start", "Cơn hen cấp?", NodeType.START, icon="🌬️"),
        FlowchartNode("severity", "Đánh giá mức độ:\nSpO₂, RR, Nói câu / từ", NodeType.DECISION, icon="⚠️"),
        FlowchartNode("mild", "Nhẹ / Trung bình", NodeType.DECISION, icon="🟡"),
        FlowchartNode("severe", "Nặng / Đe dọa\nngừng thở", NodeType.DECISION, icon="🔴"),
        FlowchartNode("saba", "SABA khí dung lặp lại\n(VD: Salbutamol mỗi 20 phút x 3)", NodeType.ACTION, icon="💨"),
        FlowchartNode("steroid_po", "Corticosteroid uống\n(VD: Prednisone 1-2 mg/kg)", NodeType.ACTION, icon="💊"),
        FlowchartNode("ipratropium", "Thêm Ipratropium\nnếu cơn nặng", NodeType.ACTION, icon="🧪"),
        FlowchartNode("oxygen", "Oxy mục tiêu SpO₂ ≥94%", NodeType.ACTION, icon="🧷"),
        FlowchartNode("iv_therapy", "Magnesium sulfate IV ±\nCorticosteroid IV", NodeType.ACTION, icon="💉"),
        FlowchartNode("icu", "ICU / Đặt NKQ\nNếu đe dọa ngừng thở", NodeType.END, color="#dc3545", icon="🏥"),
        FlowchartNode("discharge", "Xuất viện + Kế hoạch\nphòng ngừa lâu dài", NodeType.END, color="#28a745", icon="🏠"),
    ]

    edges = [
        FlowchartEdge("start", "severity", ""),
        FlowchartEdge("severity", "mild", "Nhẹ / Trung bình"),
        FlowchartEdge("severity", "severe", "Nặng / Nguy kịch"),
        FlowchartEdge("mild", "saba", ""),
        FlowchartEdge("saba", "steroid_po", "Đáp ứng chưa đầy đủ"),
        FlowchartEdge("steroid_po", "discharge", "Cải thiện"),
        FlowchartEdge("severe", "oxygen", ""),
        FlowchartEdge("oxygen", "ipratropium", ""),
        FlowchartEdge("ipratropium", "iv_therapy", "Không cải thiện"),
        FlowchartEdge("iv_therapy", "icu", "Xấu đi / CO₂↑"),
        FlowchartEdge("iv_therapy", "discharge", "Cải thiện rõ"),
    ]

    return nodes, edges


def create_acute_hf_flowchart() -> Tuple[List[FlowchartNode], List[FlowchartEdge]]:
    """
    Create Acute Decompensated Heart Failure / Pulmonary Edema flowchart

    Dựa trên:
    - ESC Guidelines for the Diagnosis and Treatment of Acute and Chronic Heart Failure (2021)
    - AHA/ACC/HFSA Guidelines for the Management of Heart Failure (2022)
    """
    nodes = [
        FlowchartNode("start", "Khó thở cấp / Phù phổi?", NodeType.START, icon="❤️"),
        FlowchartNode("abcs", "ABC + Oxy + Monitor", NodeType.ACTION, icon="🧷"),
        FlowchartNode("bp_check", "Đánh giá HA:\nHuyết áp cao / thấp", NodeType.DECISION, icon="⚖️"),
        FlowchartNode("htn", "HA tăng (SBP ≥140)", NodeType.DECISION, icon="🟥"),
        FlowchartNode("normotensive", "HA bình thường\n(SBP 100-140)", NodeType.DECISION, icon="🟨"),
        FlowchartNode("hypotensive", "HA thấp (SBP <100)", NodeType.DECISION, icon="🟦"),
        FlowchartNode("diuretic", "Furosemide IV\n(20-40 mg hoặc hơn nếu dùng trước đó)", NodeType.ACTION, icon="💊"),
        FlowchartNode("vasodilator", "Vasodilator IV\n(VD: Nitroglycerin)", NodeType.ACTION, icon="💉"),
        FlowchartNode("inotrope", "Inotrope ± Vasopressor\n(Noradrenaline / Dobutamine)", NodeType.ACTION, icon="💊"),
        FlowchartNode("niv", "NIV (CPAP/BiPAP)\nNếu phù phổi nặng", NodeType.ACTION, icon="💨"),
        FlowchartNode("icu", "ICU / Coronary Care Unit", NodeType.END, color="#dc3545", icon="🏥"),
        FlowchartNode("ward", "Nhập viện nội tim mạch", NodeType.END, color="#ffc107", icon="🏥"),
    ]

    edges = [
        FlowchartEdge("start", "abcs", ""),
        FlowchartEdge("abcs", "bp_check", ""),
        FlowchartEdge("bp_check", "htn", "SBP ≥140"),
        FlowchartEdge("bp_check", "normotensive", "SBP 100-140"),
        FlowchartEdge("bp_check", "hypotensive", "SBP <100"),
        FlowchartEdge("htn", "vasodilator", ""),
        FlowchartEdge("vasodilator", "diuretic", ""),
        FlowchartEdge("normotensive", "diuretic", ""),
        FlowchartEdge("hypotensive", "inotrope", ""),
        FlowchartEdge("diuretic", "niv", "Phù phổi nặng"),
        FlowchartEdge("niv", "icu", "Không cải thiện"),
        FlowchartEdge("niv", "ward", "Cải thiện"),
        FlowchartEdge("diuretic", "ward", "Ổn định"),
        FlowchartEdge("inotrope", "icu", ""),
    ]

    return nodes, edges


def create_anaphylaxis_flowchart() -> Tuple[List[FlowchartNode], List[FlowchartEdge]]:
    """
    Create Anaphylaxis emergency management flowchart

    Dựa trên:
    - WAO (World Allergy Organization) Anaphylaxis Guidelines
    - EAACI (European Academy of Allergy and Clinical Immunology) Anaphylaxis Guidelines
    - Resuscitation Council (UK) Anaphylaxis Guidelines
    """
    nodes = [
        FlowchartNode("start", "Nghi sốc phản vệ?", NodeType.START, icon="⚡"),
        FlowchartNode("abc", "ABC + Gọi hỗ trợ + Nằm ngửa\nNâng chân (trừ khó thở)", NodeType.ACTION, icon="🆘"),
        FlowchartNode("im_adrenaline", "Tiêm Adrenaline IM\n0.3-0.5 mg (1:1000) đùi ngoài", NodeType.ACTION, color="#dc3545", icon="💉"),
        FlowchartNode("oxygen", "Oxy lưu lượng cao\nMonitor SpO₂, HA, ECG", NodeType.ACTION, icon="🧷"),
        FlowchartNode("fluids", "Bolus dịch nhanh\nCrystalloid 20 ml/kg", NodeType.ACTION, icon="💧"),
        FlowchartNode("reassess", "Đánh giá lại sau mỗi\n5-10 phút", NodeType.DECISION, icon="👁️"),
        FlowchartNode("repeat_im", "Lặp lại Adrenaline IM\nmỗi 5-10 phút nếu cần", NodeType.ACTION, icon="💉"),
        FlowchartNode("adjunct", "Adjuncts:\nKháng Histamine, Corticoid", NodeType.ACTION, icon="💊"),
        FlowchartNode("observe", "Theo dõi ≥4-6 giờ\n(24h nếu nặng)", NodeType.END, color="#ffc107", icon="👁️"),
        FlowchartNode("icu", "ICU / Đặt NKQ\nNếu suy hô hấp / shock dai dẳng", NodeType.END, color="#dc3545", icon="🏥"),
    ]

    edges = [
        FlowchartEdge("start", "abc", ""),
        FlowchartEdge("abc", "im_adrenaline", ""),
        FlowchartEdge("im_adrenaline", "oxygen", ""),
        FlowchartEdge("oxygen", "fluids", ""),
        FlowchartEdge("fluids", "reassess", ""),
        FlowchartEdge("reassess", "repeat_im", "Không cải thiện"),
        FlowchartEdge("reassess", "adjunct", "Cải thiện"),
        FlowchartEdge("repeat_im", "fluids", "Vẫn không ổn"),
        FlowchartEdge("repeat_im", "icu", "Shock / Suy hô hấp"),
        FlowchartEdge("adjunct", "observe", ""),
    ]

    return nodes, edges
