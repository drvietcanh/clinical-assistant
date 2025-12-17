"""
Protocols Module - Clinical Treatment Protocols
Main Router - Imports from protocols module
"""

import streamlit as st
from utils.page_helper import setup_page, render_standard_footer

from protocols import (
    render_sepsis,
    render_sepsis_3hour,
    render_shock,
    render_stroke,
    render_gi_bleeding,
    render_dka,
    render_electrolytes,
    render_anaphylaxis,
    render_hypertensive_emergency,
    render_status_epilepticus,
    render_opioid_overdose,
    render_alcohol_withdrawal,
    render_paracetamol_overdose,
    render_salicylate_overdose,
    render_carbon_monoxide_poisoning,
    render_organophosphate_poisoning,
    render_toxic_alcohol_poisoning,
    render_malignant_arrhythmias,
    render_pneumothorax,
    render_traumatic_brain_injury,
    render_drowning,
    render_heat_stroke,
    render_hypothermia,
    render_cardiac_arrest,
    render_upper_airway_obstruction,
    render_spinal_cord_injury,
    render_green_pit_viper_bite,
    render_cobra_bite,
    render_krait_bite,
    render_acute_pain,
    render_copd,
    render_asthma,
    render_acute_respiratory_failure,
    render_pulmonary_tb,
    render_severe_influenza,
    render_bronchiolitis,
    render_acs,
    render_hf,
    render_acute_decompensated_hf,
    render_atrial_fibrillation,
    render_dvt_pe,
    render_bradycardia,
    render_tachycardia,
    render_aki,
    render_uti_pyelonephritis,
    render_nephrolithiasis,
    render_bph_urinary_retention,
    render_cap,
    render_hap_vap,
    render_cdiff,
    render_meningitis,
    render_endocarditis,
    render_parasitic_worms,
    render_dengue_fever,
    render_scrub_typhus,
    render_malaria,
    render_thyrotoxic_crisis,
    render_myxedema_coma,
    render_adrenal_crisis,
    render_hhs,
    render_hypoglycemia,
    render_acute_pancreatitis,
    render_acute_liver_failure,
    render_acute_mesenteric_ischemia,
    render_cholecystitis_cholangitis,
    render_acute_appendicitis,
    render_acute_diverticulitis,
    render_acute_intestinal_obstruction,
    render_acute_hepatitis,
    render_acute_colitis,
    render_hepatitis_b,
    render_h_pylori_gastritis,
    render_hepatitis_c,
    render_gerd,
    render_ibs,
    render_cirrhosis,
    render_nafld,
    render_chronic_constipation,
    render_acute_diarrhea,
    render_transfusion,
    render_anticoagulation_reversal,
    render_delirium,
    render_sedation,
    render_ards,
    render_ventilator_weaning,
    render_stress_ulcer,
    render_tls,
    render_febrile_neutropenia,
    render_hypercalcemia,
    render_ibd_exacerbation
)
from protocols.rheumatology import render_acute_gout, render_ra_flare
from protocols.neurology import render_serotonin_syndrome, render_neuroleptic_malignant_syndrome, render_intracranial_hypertension
from protocols.obstetrics import render_eclampsia, render_postpartum_hemorrhage
from protocols.dermatology import render_stevens_johnson_syndrome

# Standard page setup
setup_page(
    page_title="Phác đồ điều trị",
    page_icon="📋",
    description="Các phác đồ điều trị chuẩn theo hướng dẫn quốc tế"
)

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("📂 Chọn chuyên khoa")
    
    specialty = st.selectbox(
        "Chuyên khoa:",
        [
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
    )
    
    st.markdown("---")
    
    # Display protocols based on specialty
    if "Cấp cứu" in specialty:
        protocol = st.radio(
            "Phác đồ:",
            [
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
                "🐍 Rắn Cạp Nia Cắn"
            ],
            label_visibility="collapsed"
        )
    elif "Hô hấp" in specialty:
        protocol = st.radio(
            "Phác đồ:",
            [
                "🫁 Suy Hô Hấp Cấp (Acute Respiratory Failure)",
                "🫁 COPD Exacerbation",
                "🫁 Cơn hen cấp",
                "🫁 Viêm phổi cộng đồng (CAP)",
                "🦠 Cúm mùa nặng / Viêm phổi do cúm",
                "🫁 Lao phổi (Pulmonary TB)",
                "👶 Viêm tiểu phế quản (Bronchiolitis)"
            ],
            label_visibility="collapsed"
        )
    elif "Tim mạch" in specialty:
        protocol = st.radio(
            "Phác đồ:",
            [
                "💔 ACS - Hội chứng vành cấp",
                "💔 Suy tim Cấp",
                "💔 Suy tim Mất Bù Cấp (ADHF)",
                "💓 Rung Nhĩ (Atrial Fibrillation)",
                "🩸 DVT/PE Management",
                "💔 Nhịp chậm (Bradycardia)",
                "💔 Nhịp nhanh (Tachycardia)"
            ],
            label_visibility="collapsed"
        )
    elif "Thận" in specialty:
        protocol = st.radio(
            "Phác đồ:",
            [
                "🧪 AKI Management",
                "🚻 Nhiễm trùng tiểu / Viêm bể thận",
                "🪨 Sỏi thận / Cơn đau quặn thận",
                "🧔‍♂️ BPH & Bí tiểu cấp"
            ],
            label_visibility="collapsed"
        )
    elif "Nhiễm khuẩn" in specialty:
        protocol = st.radio(
            "Phác đồ:",
            [
                "🫁 CAP Management",
                "🏥 HAP/VAP Guidelines",
                "🦠 C. diff Treatment",
                "🧠 Meningitis / Encephalitis",
                "🦠 Viêm nội tâm mạc (Endocarditis)",
                "🦟 Sốt Xuất Huyết Dengue",
                "🦟 Sốt Mò (Scrub Typhus)",
                "🦟 Sốt Rét (Malaria)",
                "🪱 Nhiễm Ký sinh Trùng Giun Sán (Parasitic Worms)"
            ],
            label_visibility="collapsed"
        )
    elif "Nội tiết" in specialty:
        protocol = st.radio(
            "Phác đồ:",
            [
                "⚡ Thyrotoxic Crisis",
                "❄️ Myxedema Coma",
                "⚡ Adrenal Crisis",
                "🍭 HHS (Hyperglycemic Hyperosmolar State)",
                "🍭 Hạ đường huyết (Hypoglycemia)"
            ],
            label_visibility="collapsed"
        )
    elif "Huyết học" in specialty or "Hematology" in specialty:
        protocol = st.radio(
            "Phác đồ:",
            [
                "🩸 Truyền máu (Transfusion)",
                "🩸 Đảo Ngược Chống đông (Anticoagulation Reversal)"
            ],
            label_visibility="collapsed"
        )
    elif "Tiêu hóa" in specialty or "Gastroenterology" in specialty:
        protocol = st.radio(
            "Phác đồ:",
            [
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
                "🫀 Điều Trị Viêm Gan B (Hepatitis B Treatment)",
                "🫀 Viêm Loét Dạ Dày HP (+) (H. pylori Gastritis/Ulcer)",
                "🫀 Điều Trị Viêm Gan C (Hepatitis C Treatment)",
                "🫀 Trào Ngược Dạ Dày Thực Quản (GERD)",
                "🫀 Hội Chứng Ruột Kích Thích (IBS)",
                "🫀 Quản Lý Xơ Gan (Cirrhosis Management)",
                "🫀 Bệnh Gan Nhiễm Mỡ Không Do Rượu (NAFLD/NASH)",
                "🫀 Táo Bón Mạn Tính (Chronic Constipation)",
                "🫀 Tiêu Chảy Cấp (Acute Diarrhea)"
            ],
            label_visibility="collapsed"
        )
    elif "Hồi sức" in specialty or "Critical Care" in specialty:
        protocol = st.radio(
            "Phác đồ:",
            [
                "🧠 Quản lý Delirium (Delirium Management)",
                "💤 An thần & Giảm đau ICU (ICU Sedation & Analgesia)",
                "🫁 ARDS Management",
                "🫁 Ventilator Weaning",
                "🩸 Stress Ulcer Prophylaxis"
            ],
            label_visibility="collapsed"
        )
    elif "Ung thư" in specialty or "Oncology" in specialty:
        protocol = st.radio(
            "Phác đồ:",
            [
                "🎗️ Tumor Lysis Syndrome",
                "🌡️ Febrile Neutropenia",
                "📈 Hypercalcemia of Malignancy"
            ],
            label_visibility="collapsed"
        )
    elif "Đau" in specialty or "Pain" in specialty:
        protocol = st.radio(
            "Phác đồ:",
            [
                "💊 Quản lý Đau Cấp (Acute Pain Management)"
            ],
            label_visibility="collapsed"
        )
    elif "Thấp khớp" in specialty or "Rheumatology" in specialty:
        protocol = st.radio(
            "Phác đồ:",
            [
                "🦴 Gout Cấp (Acute Gout Management)",
                "🦴 RA Flare (Acute Flare of Rheumatoid Arthritis)"
            ],
            label_visibility="collapsed"
        )
    elif "Thần kinh" in specialty or "Neurology" in specialty:
        protocol = st.radio(
            "Phác đồ:",
            [
                "🧠 Hội chứng Serotonin (Serotonin Syndrome)",
                "🧠 Hội chứng ác tính do thuốc an thần (NMS)",
                "🧠 Tăng áp lực nội sọ (Intracranial Hypertension)"
            ],
            label_visibility="collapsed"
        )
    elif "Sản khoa" in specialty or "Obstetrics" in specialty:
        protocol = st.radio(
            "Phác đồ:",
            [
                "🤰 Sản giật (Eclampsia)",
                "🩸 Xuất huyết sau sinh (Postpartum Hemorrhage)"
            ],
            label_visibility="collapsed"
        )
    elif "Da liễu" in specialty or "Dermatology" in specialty:
        protocol = st.radio(
            "Phác đồ:",
            [
                "🩹 Hội chứng Stevens-Johnson (SJS/TEN)"
            ],
            label_visibility="collapsed"
        )
    
    st.markdown("---")
    st.info("""
    **📚 Căn cứ:**
    - International Guidelines
    - Evidence-based protocols
    - Updated regularly
    """)

# ========== MAIN CONTENT ==========

st.info(f"""
**Chuyên khoa:** {specialty}

**Phác đồ đang xem:** {protocol.split(' ', 1)[1] if ' ' in protocol else protocol}
""")

st.markdown("---")

# Route to appropriate protocol
if "Cardiac Arrest" in protocol or "ACLS" in protocol or "cardiac arrest" in protocol.lower() or "acls" in protocol.lower():
    render_cardiac_arrest()

elif "Upper Airway" in protocol or "Tắc Nghẽn Đường Thở" in protocol or "upper airway" in protocol.lower() or "airway obstruction" in protocol.lower():
    render_upper_airway_obstruction()

elif "Spinal Cord" in protocol or "Chấn Thương Tủy" in protocol or "spinal cord" in protocol.lower() or "tủy sống" in protocol.lower():
    render_spinal_cord_injury()

elif "Sepsis 1-Hour" in protocol:
    render_sepsis()
elif "Sepsis 3-Hour" in protocol:
    render_sepsis_3hour()
elif "Sepsis" in protocol:
    render_sepsis()  # Fallback

elif "Sốc" in protocol:
    render_shock()

elif "Respiratory Failure" in protocol or "Suy Hô Hấp" in protocol or "respiratory failure" in protocol.lower():
    render_acute_respiratory_failure()

elif "COPD" in protocol:
    render_copd()

elif "Hen" in protocol:
    render_asthma()

elif "Viêm phổi cộng đồng" in protocol or "CAP" in protocol:
    render_cap()

elif "Cúm" in protocol or "influenza" in protocol.lower():
    render_severe_influenza()

elif "Lao phổi" in protocol or "tuberculosis" in protocol.lower():
    render_pulmonary_tb()

elif "Tiểu phế quản" in protocol or "bronchiolitis" in protocol.lower():
    render_bronchiolitis()

elif "ACS" in protocol:
    render_acs()

elif "Suy tim" in protocol and "Mất Bù" not in protocol and "ADHF" not in protocol:
    render_hf()

elif "ADHF" in protocol or "Mất Bù" in protocol or "acute decompensated" in protocol.lower():
    render_acute_decompensated_hf()

elif "Stroke" in protocol:
    render_stroke()

elif "GI Bleeding" in protocol or "GI" in protocol:
    render_gi_bleeding()

elif "DKA" in protocol:
    render_dka()

elif "Electrolyte" in protocol:
    render_electrolytes()

elif "Anaphylaxis" in protocol or "anaphylaxis" in protocol.lower():
    render_anaphylaxis()

elif "Tăng Huyết áp" in protocol or "Hypertensive" in protocol or "hypertensive" in protocol.lower():
    render_hypertensive_emergency()

elif "Status Epilepticus" in protocol or "status epilepticus" in protocol.lower() or "Epilepticus" in protocol or "Trạng thái động kinh" in protocol:
    render_status_epilepticus()

elif "Opioid" in protocol or "opioid" in protocol.lower() or "Naloxone" in protocol or "naloxone" in protocol.lower():
    render_opioid_overdose()

elif "Alcohol" in protocol or "alcohol" in protocol.lower() or "Cai rượu" in protocol or "cai rượu" in protocol.lower() or "Rượu" in protocol:
    render_alcohol_withdrawal()

elif "Rung Nhĩ" in protocol or "Atrial Fibrillation" in protocol or "atrial fibrillation" in protocol.lower() or "AF" in protocol:
    render_atrial_fibrillation()

elif "DVT" in protocol or "PE" in protocol or "dvt" in protocol.lower() or "pe" in protocol.lower() or "Huyết Khối" in protocol or "Thuyên Tắc" in protocol:
    render_dvt_pe()

elif "AKI" in protocol:
    render_aki()
elif "Nhiễm trùng tiểu" in protocol or "bể thận" in protocol or "UTI" in protocol:
    render_uti_pyelonephritis()
elif "Sỏi thận" in protocol or "quặn thận" in protocol or "renal colic" in protocol.lower():
    render_nephrolithiasis()
elif "BPH" in protocol or "Bí tiểu" in protocol or "bph" in protocol.lower():
    render_bph_urinary_retention()

elif "CAP" in protocol:
    render_cap()

elif "HAP" in protocol or "VAP" in protocol:
    render_hap_vap()

elif "C. diff" in protocol or "cdiff" in protocol.lower():
    render_cdiff()

elif "Meningitis" in protocol or "meningitis" in protocol.lower() or "Encephalitis" in protocol or "encephalitis" in protocol.lower():
    render_meningitis()

elif "Thyrotoxic" in protocol or "thyrotoxic" in protocol.lower():
    render_thyrotoxic_crisis()

elif "Myxedema" in protocol or "myxedema" in protocol.lower():
    render_myxedema_coma()

elif "Adrenal" in protocol or "adrenal" in protocol.lower():
    render_adrenal_crisis()

elif "HHS" in protocol or "Hyperosmolar" in protocol or "hyperosmolar" in protocol.lower():
    render_hhs()

elif "Pancreatitis" in protocol or "pancreatitis" in protocol.lower() or "Tụy" in protocol:
    render_acute_pancreatitis()

elif "Liver Failure" in protocol or "liver failure" in protocol.lower() or "Suy gan" in protocol:
    render_acute_liver_failure()

elif "Mesenteric Ischemia" in protocol or "Thiếu Máu Mạc Treo" in protocol or "mesenteric ischemia" in protocol.lower() or "mạc treo" in protocol.lower():
    render_acute_mesenteric_ischemia()

elif "Cholecystitis" in protocol or "Cholangitis" in protocol or "Túi Mật" in protocol or "Đường Mật" in protocol or "cholecystitis" in protocol.lower() or "cholangitis" in protocol.lower():
    render_cholecystitis_cholangitis()

elif "Appendicitis" in protocol or "Ruột Thừa" in protocol or "appendicitis" in protocol.lower() or "ruột thừa" in protocol.lower():
    render_acute_appendicitis()

elif "Diverticulitis" in protocol or "Túi Thừa" in protocol or "diverticulitis" in protocol.lower() or "túi thừa" in protocol.lower():
    render_acute_diverticulitis()

elif "Intestinal Obstruction" in protocol or "Tắc Ruột" in protocol or "intestinal obstruction" in protocol.lower() or "tắc ruột" in protocol.lower():
    render_acute_intestinal_obstruction()

elif "Hepatitis" in protocol and "Non-viral" in protocol or "Viêm Gan Cấp" in protocol or "hepatitis" in protocol.lower() and "non-viral" in protocol.lower():
    render_acute_hepatitis()

elif "Colitis" in protocol and "Non-IBD" in protocol or "Viêm Đại Tràng Cấp" in protocol or "colitis" in protocol.lower() and "non-ibd" in protocol.lower():
    render_acute_colitis()

elif "IBD" in protocol or "ibd" in protocol.lower() or "Crohn" in protocol or "Colitis" in protocol:
    render_ibd_exacerbation()

elif "Hepatitis B" in protocol or "Viêm Gan B" in protocol or "hepatitis b" in protocol.lower() or "viêm gan b" in protocol.lower():
    render_hepatitis_b()

elif "H. pylori" in protocol or "pylori" in protocol.lower() or "HP (+)" in protocol or "HP dương" in protocol.lower() or "Viêm Loét Dạ Dày HP" in protocol:
    render_h_pylori_gastritis()

elif "Hepatitis C" in protocol or "Viêm Gan C" in protocol or "hepatitis c" in protocol.lower() or "viêm gan c" in protocol.lower():
    render_hepatitis_c()

elif "GERD" in protocol or "Trào Ngược" in protocol or "gerd" in protocol.lower() or "trào ngược" in protocol.lower() or "Gastroesophageal Reflux" in protocol:
    render_gerd()

elif "IBS" in protocol or "Ruột Kích Thích" in protocol or "ibs" in protocol.lower() or "ruột kích thích" in protocol.lower() or "Irritable Bowel" in protocol:
    render_ibs()

elif "Cirrhosis" in protocol or "Xơ Gan" in protocol or "cirrhosis" in protocol.lower() or "xơ gan" in protocol.lower():
    render_cirrhosis()

elif "NAFLD" in protocol or "NASH" in protocol or "Gan Nhiễm Mỡ" in protocol or "nafld" in protocol.lower() or "nash" in protocol.lower() or "gan nhiễm mỡ" in protocol.lower():
    render_nafld()

elif "Táo Bón" in protocol or "Constipation" in protocol or "táo bón" in protocol.lower() or "constipation" in protocol.lower():
    render_chronic_constipation()

elif "Tiêu Chảy" in protocol or "Diarrhea" in protocol or "tiêu chảy" in protocol.lower() or "diarrhea" in protocol.lower():
    render_acute_diarrhea()

elif "Delirium" in protocol or "delirium" in protocol.lower() or "Quản lý Delirium" in protocol:
    render_delirium()

elif "Sedation" in protocol or "sedation" in protocol.lower() or "An thần" in protocol or "Giảm đau ICU" in protocol:
    render_sedation()

elif "Transfusion" in protocol or "transfusion" in protocol.lower() or "Truyền Máu" in protocol:
    render_transfusion()

elif "Anticoagulation" in protocol or "anticoagulation" in protocol.lower() or "Đảo Ngược" in protocol or "Chống Đông" in protocol:
    render_anticoagulation_reversal()

elif "Tumor Lysis" in protocol or "TLS" in protocol or "tls" in protocol.lower():
    render_tls()

elif "Febrile Neutropenia" in protocol or "neutropenia" in protocol.lower():
    render_febrile_neutropenia()

elif "Hypercalcemia" in protocol or "hypercalcemia" in protocol.lower():
    render_hypercalcemia()

elif "Đau" in protocol or "Pain" in protocol or "pain" in protocol.lower():
    render_acute_pain()

elif "Gout" in protocol or "gout" in protocol.lower():
    render_acute_gout()

elif "ARDS" in protocol or "ards" in protocol.lower():
    render_ards()

elif "Ventilator Weaning" in protocol or "weaning" in protocol.lower() or "Cai Máy" in protocol:
    render_ventilator_weaning()

elif "Stress Ulcer" in protocol or "stress ulcer" in protocol.lower() or "SUP" in protocol:
    render_stress_ulcer()

elif "RA Flare" in protocol or "rheumatoid arthritis" in protocol.lower() or "RA" in protocol:
    render_ra_flare()

elif "IBD" in protocol or "ibd" in protocol.lower() or "Crohn" in protocol or "Colitis" in protocol:
    render_ibd_exacerbation()

elif "Bradycardia" in protocol or "bradycardia" in protocol.lower() or "Nhịp chậm" in protocol:
    render_bradycardia()

elif "Tachycardia" in protocol or "tachycardia" in protocol.lower() or "Nhịp nhanh" in protocol:
    render_tachycardia()

elif "Endocarditis" in protocol or "endocarditis" in protocol.lower() or "Viêm nội tâm mạc" in protocol:
    render_endocarditis()

elif "Sốt Mò" in protocol or "Scrub Typhus" in protocol or "scrub typhus" in protocol.lower() or "sốt mò" in protocol.lower():
    render_scrub_typhus()

elif "Sốt Rét" in protocol or "Malaria" in protocol or "malaria" in protocol.lower() or "sốt rét" in protocol.lower():
    render_malaria()

elif "Ký sinh Trùng" in protocol or "Parasitic" in protocol or "parasitic" in protocol.lower() or "Giun Sán" in protocol or "giun sán" in protocol.lower():
    render_parasitic_worms()

elif "Hypoglycemia" in protocol or "hypoglycemia" in protocol.lower() or "Hạ đường huyết" in protocol:
    render_hypoglycemia()

elif "Serotonin" in protocol or "serotonin" in protocol.lower():
    render_serotonin_syndrome()

elif "Neuroleptic" in protocol or "neuroleptic" in protocol.lower() or "NMS" in protocol or "ác tính do thuốc an thần" in protocol:
    render_neuroleptic_malignant_syndrome()

elif "Intracranial" in protocol or "intracranial" in protocol.lower() or "Tăng áp lực nội sọ" in protocol:
    render_intracranial_hypertension()

elif "Eclampsia" in protocol or "eclampsia" in protocol.lower() or "Sản giật" in protocol:
    render_eclampsia()

elif "Postpartum" in protocol or "postpartum" in protocol.lower() or "Xuất huyết sau sinh" in protocol:
    render_postpartum_hemorrhage()

elif "Stevens" in protocol or "stevens" in protocol.lower() or "SJS" in protocol or "TEN" in protocol:
    render_stevens_johnson_syndrome()

elif "Paracetamol" in protocol or "paracetamol" in protocol.lower() or "Acetaminophen" in protocol or "acetaminophen" in protocol.lower():
    render_paracetamol_overdose()

elif "Salicylate" in protocol or "salicylate" in protocol.lower() or "Aspirin" in protocol or "aspirin" in protocol.lower():
    render_salicylate_overdose()

elif "Carbon Monoxide" in protocol or "carbon monoxide" in protocol.lower() or "CO" in protocol or "Carbon" in protocol:
    render_carbon_monoxide_poisoning()

elif "Organophosphate" in protocol or "organophosphate" in protocol.lower():
    render_organophosphate_poisoning()

elif "Alcohol Độc Hại" in protocol or "Methanol" in protocol or "Ethylene Glycol" in protocol or "alcohol" in protocol.lower():
    render_toxic_alcohol_poisoning()

elif "Malignant Arrhythmias" in protocol or "loạn nhịp" in protocol.lower() or "VF" in protocol or "VT" in protocol:
    render_malignant_arrhythmias()

elif "Pneumothorax" in protocol or "pneumothorax" in protocol.lower() or "Tràn khí màng phổi" in protocol:
    render_pneumothorax()

elif "Traumatic Brain Injury" in protocol or "Chấn thương sọ não" in protocol or "traumatic brain injury" in protocol.lower() or "TBI" in protocol:
    render_traumatic_brain_injury()

elif "Drowning" in protocol or "drowning" in protocol.lower() or "Đuối nước" in protocol:
    render_drowning()

elif "Heat Stroke" in protocol or "heat stroke" in protocol.lower() or "Sốc Nhiệt" in protocol or "sốc nhiệt" in protocol.lower():
    render_heat_stroke()

elif "Hypothermia" in protocol or "hypothermia" in protocol.lower() or "Hạ thân nhiệt" in protocol or "hạ thân nhiệt" in protocol.lower():
    render_hypothermia()

elif "Rắn Lục Xanh" in protocol or "green pit viper" in protocol.lower() or "lục xanh đuôi đỏ" in protocol.lower():
    render_green_pit_viper_bite()

elif "Rắn Hổ Mang" in protocol or "cobra" in protocol.lower() or "hổ mang" in protocol.lower():
    render_cobra_bite()

elif "Rắn Cạp Nia" in protocol or "krait" in protocol.lower() or "cạp nia" in protocol.lower():
    render_krait_bite()

elif "Dengue" in protocol or "dengue" in protocol.lower() or "Sốt Xuất Huyết" in protocol or "sốt xuất huyết" in protocol.lower():
    render_dengue_fever()

# ========== FOOTER ==========
render_standard_footer(disclaimer=False)
