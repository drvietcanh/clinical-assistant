"""
Protocol Lists Configuration
Centralized protocol lists for each specialty
"""

# Specialty list
SPECIALTY_LIST = [
    "🚨 Cấp cứu (Emergency)",
    "🫁 Hô hấp (Respiratory)",
    "❤️ Tim mạch (Cardiology)",
    "🧪 Thận (Nephrology)",
    "🦠 Nhiễm khuẩn (Infectious)",
    "⚕️ Nội tiết (Endocrinology)",
    "🧠 Thần kinh (Neurology)",
    "🎗️ Ung thư (Oncology)",
    "💊 Đau (Pain Management)",
    "🩸 Huyết học (Hematology)",
    "🫀 Tiêu hóa (Gastroenterology)",
    "🏥 Hồi sức (Critical Care)",
    "🦴 Thấp khớp (Rheumatology)",
    "🤰 Sản khoa (Obstetrics)",
    "🩹 Da liễu (Dermatology)"
]

# Protocol lists by specialty
PROTOCOL_LISTS = {
    "Cấp cứu": [
        "💔 Cardiac Arrest / ACLS",
        "🫀 Tắc Nghẽn Đường Thở Trên (Upper Airway Obstruction)",
        "🧠 Chấn Thương Tủy Sống (Spinal Cord Injury)",
        "🦠 Sepsis 1-Hour Bundle",
        "🦠 Sepsis 3-Hour Bundle",
        "💔 Quản lý Sốc",
        "🧠 Stroke Management",
        "🩸 GI Bleeding",
        "🍭 DKA Protocol",
        "⚡ Electrolyte Emergency",
        "🚨 Anaphylaxis",
        "⚡ Cơn tăng huyết áp cấp cứu",
        "🧠 Trạng thái động kinh liên tục",
        "💉 Ngộ Độc Opioid / Naloxone",
        "🍺 Cai rượu cấp",
        "💊 Ngộ Độc Paracetamol",
        "💊 Ngộ Độc Salicylate (Aspirin)",
        "💨 Ngộ Độc Carbon Monoxide",
        "☣️ Ngộ Độc Organophosphate",
        "🍷 Ngộ Độc Alcohol Độc Hại (Methanol/Ethylene Glycol)",
        "❤️‍🔥 Loạn nhịp nguy hiểm (Malignant Arrhythmias)",
        "🫁 Tràn khí màng phổi (Pneumothorax)",
        "🧠 Chấn thương sọ não (Traumatic Brain Injury)",
        "🌊 Đuối nước (Drowning)",
        "🌡️ Sốc Nhiệt (Heat Stroke)",
        "❄️ Hạ thân nhiệt (Hypothermia)",
        "🐍 Rắn Lục Xanh Đuôi Đỏ Cắn",
        "🐍 Rắn Hổ Mang Cắn",
        "🐍 Rắn Cạp Nia Cắn",
        "🫁 Phù Phổi Cấp (Acute Pulmonary Edema)",
        "💊 Ngộ Độc TCA (Tricyclic Antidepressant)",
        "💊 Ngộ Độc Digoxin (Digoxin Toxicity)",
        "🍭 Hạ Đường Huyết Cấp cứu (Severe Hypoglycemia)",
        "🫁 Chấn Thương Ngực (Chest Trauma)",
        "🫀 Chấn Thương Bụng (Abdominal Trauma)",
        "🔥 Bỏng (Burn Management)"
    ],
    "Hô hấp": [
        "🫁 Suy Hô hấp Cấp (Acute Respiratory Failure)",
        "🫁 COPD Exacerbation",
        "🫁 Cơn hen cấp",
        "🫁 Viêm phổi cộng đồng (CAP)",
        "🦠 Cúm mùa nặng / Viêm phổi do cúm",
        "🫁 Lao phổi (Pulmonary TB)",
        "🫁 Lao phổi (VN Protocol)",
        "👶 Viêm tiểu phế quản (Bronchiolitis)"
    ],
    "Tim mạch": [
        "💔 ACS - Hội chứng vành cấp",
        "💔 STEMI (ST-Elevation Myocardial Infarction)",
        "💔 NSTEMI (Non-ST-Elevation Myocardial Infarction)",
        "💔 Chèn Ép Tim (Cardiac Tamponade)",
        "💔 Bóc Tách Động Mạch Chủ (Aortic Dissection)",
        "💔 Suy tim Cấp",
        "💔 Suy tim Mất Bù Cấp (ADHF)",
        "💓 Rung Nhĩ (Atrial Fibrillation)",
        "🩸 DVT/PE Management",
        "💔 Nhịp chậm (Bradycardia)",
        "💔 Nhịp nhanh (Tachycardia)"
    ],
    "Thận": [
        "🧪 AKI Management",
        "🫘 Suy thận mạn tính (CKD)",
        "🩸 Thiếu Máu Trong CKD (KDIGO 2026)",
        "📊 Quản lý Huyết Áp Trong CKD (KDIGO 2021)",
        "💊 Tăng Huyết Áp Kháng Trị Trong CKD",
        "🔬 IgA Nephropathy (KDIGO 2021)",
        "🌙 Lupus Nephritis (KDIGO 2021)",
        "🔬 ANCA Vasculitis (KDIGO 2021)",
        "❤️ Suy tim Trong CKD (KDIGO 2025)",
        "🍭 Bệnh thận do đái tháo đường",
        "📈 Bệnh thận do tăng huyết áp",
        "🚻 Nhiễm trùng tiểu / Viêm bể thận",
        "🪨 Sỏi thận / Cơn đau quặn thận",
        "🧔‍♂️ BPH & Bí tiểu cấp",
        "🔬 Viêm cầu thận mạn tính",
        "💧 Hội chứng thận hư",
        "🧪 Hội Chứng Gan Thận (Hepatorenal Syndrome)",
        "🧪 Lọc Máu Cấp cứu (Emergency Dialysis)"
    ],
    "Nhiễm khuẩn": [
        "🫁 CAP Management",
        "🏥 HAP/VAP Guidelines",
        "🦠 C. diff Treatment",
        "🧠 Meningitis / Encephalitis",
        "🦠 Viêm nội tâm mạc (Endocarditis)",
        "🦟 Sốt Xuất huyết Dengue",
        "🦟 Sốt Xuất huyết Dengue (VN Protocol)",
        "🦟 Sốt Mò (Scrub Typhus)",
        "🦟 Sốt Rét (Malaria)",
        "🪱 Nhiễm Ký sinh Trùng Giun Sán (Parasitic Worms)"
    ],
    "Nội tiết": [
        "⚡ Thyrotoxic Crisis",
        "❄️ Myxedema Coma",
        "⚡ Adrenal Crisis",
        "🍭 HHS (Hyperglycemic Hyperosmolar State)",
        "🍭 Hạ đường huyết (Hypoglycemia)"
    ],
    "Huyết học": [
        "🩸 Truyền máu (Transfusion)",
        "🩸 Đảo Ngược Chống đông (Anticoagulation Reversal)",
        "🩸 Xuất huyết Giảm Tiểu Cầu Miễn dịch (ITP)",
        "🩸 TTP/HUS (Thrombotic Thrombocytopenic Purpura)",
        "🩸 DIC (Disseminated Intravascular Coagulation)"
    ],
    "Tiêu hóa": [
        "🫀 Viêm Tụy Cấp (Acute Pancreatitis)",
        "🫀 Suy gan Cấp (Acute Liver Failure)",
        "🫀 Thiếu Máu Mạc Treo Cấp (Acute Mesenteric Ischemia)",
        "🫀 Viêm Túi Mật / Viêm Đường Mật (Cholecystitis/Cholangitis)",
        "🫀 Viêm Ruột Thừa Cấp (Acute Appendicitis)",
        "🫀 Viêm Túi Thừa Cấp (Acute Diverticulitis)",
        "🫀 Tắc Ruột Cấp (Acute Intestinal Obstruction)",
        "🫀 Viêm Gan Cấp (Non-viral) (Acute Hepatitis)",
        "🫀 Viêm Đại Tràng Cấp (Non-IBD) (Acute Colitis)",
        "🩸 IBD Exacerbation (Acute Exacerbation of IBD)",
        "🫀 Điều trị Viêm Gan B (Hepatitis B Treatment)",
        "🫀 Viêm Loét Dạ Dày HP (+) (H. pylori Gastritis/Ulcer)",
        "🫀 Điều trị Viêm Gan C (Hepatitis C Treatment)",
        "🫀 Trào Ngược Dạ Dày Thực Quản (GERD)",
        "🫀 Hội Chứng Ruột Kích Thích (IBS)",
        "🫀 Quản lý Xơ Gan (Cirrhosis Management)",
        "🫀 Bệnh Gan Nhiễm Mỡ Không Do Rượu (NAFLD/NASH)",
        "🫀 Táo Bón Mạn Tính (Chronic Constipation)",
        "🫀 Tiêu chảy Cấp (Acute Diarrhea)",
        "🩸 Xuất huyết Tiêu hóa Dưới (Lower GI Bleeding)",
        "🫀 Thủng Dạ Dày Tá Tràng (Perforated Peptic Ulcer)",
        "🫀 Tắc Mật (Biliary Obstruction)",
        "🫀 Xơ Gan Mất Bù (Decompensated Cirrhosis)"
    ],
    "Hồi sức": [
        "🧠 Quản lý Delirium (Delirium Management)",
        "💤 An thần & Giảm đau ICU (ICU Sedation & Analgesia)",
        "🫁 ARDS Management",
        "🫁 Ventilator Weaning",
        "🩸 Stress Ulcer Prophylaxis",
        "🧠 Quản lý Áp Lực Nội Sọ (ICP Management)",
        "🧪 CRRT (Continuous Renal Replacement Therapy)"
    ],
    "Ung thư": [
        "🎗️ Tumor Lysis Syndrome",
        "🌡️ Febrile Neutropenia",
        "📈 Hypercalcemia of Malignancy"
    ],
    "Đau": [
        "💊 Quản lý Đau Cấp (Acute Pain Management)"
    ],
    "Thấp khớp": [
        "🦴 Gout Cấp (Acute Gout Management)",
        "🦴 RA Flare (Acute Flare of Rheumatoid Arthritis)",
        "🦴 Viêm Khớp Thoái Hóa (Osteoarthritis)",
        "🦴 Viêm Cột Sống Dính Khớp (Ankylosing Spondylitis)",
        "🦴 Viêm Khớp Phản Ứng (Reactive Arthritis)",
        "🦴 Viêm Khớp Vảy Nến (Psoriatic Arthritis)",
        "🦴 Lupus - Viêm Khớp (SLE Arthritis)"
    ],
    "Thần kinh": [
        "🧠 Hội chứng Serotonin (Serotonin Syndrome)",
        "🧠 Hội chứng ác tính do thuốc an thần (NMS)",
        "🧠 Tăng áp lực nội sọ (Intracranial Hypertension)"
    ],
    "Sản khoa": [
        "🤰 Sản giật (Eclampsia)",
        "🩸 Xuất huyết sau sinh (Postpartum Hemorrhage)",
        "🤰 Tiền Sản Giật (Preeclampsia)",
        "🤰 HELLP Syndrome",
        "🤰 Nhiễm Trùng Ối (Chorioamnionitis)",
        "🤰 Nhau Bong Non (Placental Abruption)",
        "🤰 Vỡ Tử Cung (Uterine Rupture)"
    ],
    "Da liễu": [
        "🩹 Hội chứng Stevens-Johnson (SJS/TEN)",
        "🩹 Viêm da cơ địa (Atopic Dermatitis)",
        "🩹 Viêm da tiếp xúc (Contact Dermatitis)",
        "🩹 Mụn trứng cá (Acne Vulgaris)",
        "🩹 Nhiễm nấm da (Fungal Skin Infections)",
        "🩹 Ghẻ (Scabies)",
        "🩹 Mề đay (Urticaria)",
        "🩹 Vảy nến (Psoriasis)"
    ]
}


def get_protocol_list(specialty: str) -> list:
    """
    Get protocol list for a given specialty.
    
    Args:
        specialty: Specialty name (can be full name or partial match)
        
    Returns:
        List of protocol names for the specialty, or empty list if not found
    """
    # Try exact match first
    if specialty in PROTOCOL_LISTS:
        return PROTOCOL_LISTS[specialty]
    
    # Try partial match
    for key in PROTOCOL_LISTS:
        if key in specialty or specialty in key:
            return PROTOCOL_LISTS[key]
    
    # Try matching with English names
    specialty_mapping = {
        "Emergency": "Cấp cứu",
        "Respiratory": "Hô hấp",
        "Cardiology": "Tim mạch",
        "Nephrology": "Thận",
        "Infectious": "Nhiễm khuẩn",
        "Endocrinology": "Nội tiết",
        "Neurology": "Thần kinh",
        "Oncology": "Ung thư",
        "Pain Management": "Đau",
        "Hematology": "Huyết học",
        "Gastroenterology": "Tiêu hóa",
        "Critical Care": "Hồi sức",
        "Rheumatology": "Thấp khớp",
        "Obstetrics": "Sản khoa",
        "Dermatology": "Da liễu"
    }
    
    for eng_name, vn_name in specialty_mapping.items():
        if eng_name in specialty:
            return PROTOCOL_LISTS.get(vn_name, [])
    
    return []

