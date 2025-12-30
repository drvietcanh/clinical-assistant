"""
Clinical Decision Rules Flowcharts
Pre-built flowcharts for important clinical decision rules
"""

from typing import List, Tuple
from components.flowchart import FlowchartNode, FlowchartEdge, NodeType


def create_wells_pe_flowchart() -> Tuple[List[FlowchartNode], List[FlowchartEdge]]:
    """
    Create Wells PE Score flowchart
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
