"""
Trang hiển thị các bài viết chuyên sâu.
Nội dung lấy từ docs/articles/*.md với metadata khai báo trong ARTICLES.
Thiết kế lại với UI/UX đẹp và khoa học hơn.
"""

from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components
from collections import Counter

from utils.page_helper import setup_page, render_standard_footer


BASE_DIR = Path(__file__).resolve().parent.parent
ARTICLES = [
    {
        "id": "hypertension",
        "title": "Điều trị tăng huyết áp người lớn",
        "specialty": "Tim mạch",
        "keywords": ["tăng huyết áp", "ESC/ESH", "ACC/AHA", "ACEi", "ARB", "CCB", "thiazide-like"],
        "path": BASE_DIR / "docs" / "articles" / "hypertension.md",
        "last_reviewed": "2025-01",
        "guidelines": ["ESC/ESH 2023/2024", "ACC/AHA 2024"],
        "summary": [
            "Phối hợp 2 thuốc sớm: RAASi + CCB hoặc RAASi + thiazide-like.",
            "Đích HA đa số <140/90; xem xét <130/80 nếu dung nạp và nguy cơ cao.",
            "Bước 3: RAASi + CCB + thiazide-like; kháng trị thêm spironolactone khi eGFR/K+ cho phép.",
            "Ưu tiên ACEi/ARB ở CKD/protein niệu, ĐTĐ; β-blocker khi có chỉ định tim mạch.",
            "Theo dõi K+, creatinine/eGFR; tránh triple whammy (RAASi + NSAID + lợi tiểu).",
        ],
        "related_calculators": ["eGFR (CKD-EPI)", "CrCl (Cockcroft-Gault)", "ASCVD 10-year", "SCORE2/SCORE2-OP", "BMI"],
        "related_protocols": ["(đề xuất) HTN management quick steps"],
    },
    {
        "id": "acid_suppression",
        "title": "Thuốc giảm tiết acid và dự phòng xuất huyết tiêu hóa do stress",
        "specialty": "Tiêu hóa / Hồi sức",
        "keywords": ["PPI", "H2RA", "stress ulcer prophylaxis", "ACG", "AGA", "ASHP", "ICU", "GERD", "PUD"],
        "path": BASE_DIR / "docs" / "articles" / "acid_suppression.md",
        "last_reviewed": "2025-01",
        "guidelines": ["ACG/AGA GERD & PUD 2022–2024", "ASHP SUP", "SSC/ICU (tham khảo)"],
        "summary": [
            "SUP chỉ định ở ICU nguy cơ cao; ngừng khi hết yếu tố nguy cơ.",
            "PPI ưu tiên nguy cơ cao; H2RA khi cần giảm nguy cơ C. difficile/ít tương tác; H2RA phải chỉnh liều thận.",
            "GERD/PUD: PPI 4–8 tuần, cân nhắc step-down; diệt H. pylori nếu dương tính.",
            "Ưu tiên pantoprazole khi dùng kèm clopidogrel; theo dõi Mg/B12 nếu dùng kéo dài.",
            "Đánh giá lại chỉ định mỗi 4–8 tuần; cảnh giác C. difficile và viêm phổi cộng đồng.",
        ],
        "related_calculators": ["CrCl (Cockcroft-Gault)", "eGFR", "BMI"],
        "related_protocols": ["(đề xuất) ICU Stress Ulcer Prophylaxis checklist"],
    },
    {
        "id": "acs_management",
        "title": "Hội chứng vành cấp (NSTEMI/STEMI): kháng kết tập, chống đông, chiến lược can thiệp",
        "specialty": "Tim mạch cấp cứu",
        "keywords": ["ACS", "NSTEMI", "STEMI", "DAPT", "heparin", "fondaparinux", "bivalirudin", "PCI"],
        "path": BASE_DIR / "docs" / "articles" / "acs_management.md",
        "last_reviewed": "2025-01",
        "guidelines": ["ESC ACS (NSTEMI/STEMI) 2023", "ACC/AHA ACS/PCI 2024–2025"],
        "summary": [
            "Phân tầng sớm (GRACE/TIMI/HEART) quyết định thời gian PCI (<2h rất cao, <24h cao).",
            "DAPT: aspirin + P2Y12 (ticagrelor/prasugrel ưu tiên; clopidogrel khi cần).",
            "Chống đông: UFH/enoxaparin; fondaparinux NSTEMI nguy cơ chảy máu (cần bolus UFH khi PCI); bivalirudin nếu nguy cơ chảy máu cao.",
            "STEMI: PCI tiên phát ưu tiên; nếu không khả dụng <120 phút → fibrinolysis rồi PCI cứu vãn.",
            "Chọn thời gian DAPT 6–12 tháng theo cân bằng thiếu máu cục bộ/chảy máu (PRECISE-DAPT).",
        ],
        "related_calculators": ["GRACE", "TIMI", "HEART", "CrCl (Cockcroft-Gault)", "BMI"],
        "related_protocols": ["ACS protocol trong app (nếu có)", "(đề xuất) DAPT/anticoag checklist"],
    },
    {
        "id": "copd_asthma_exacerbation",
        "title": "Đợt cấp COPD và Hen: xử trí, thuốc giãn phế quản, steroid, kháng sinh",
        "specialty": "Hô hấp",
        "keywords": ["COPD", "asthma", "exacerbation", "GOLD 2024", "GINA 2024", "SABA", "LABA", "LAMA", "ICS"],
        "path": BASE_DIR / "docs" / "articles" / "copd_asthma_exacerbation.md",
        "last_reviewed": "2025-01",
        "guidelines": ["GOLD 2024", "GINA 2024"],
        "summary": [
            "COPD đợt cấp: SABA ± SAMA, steroid ngắn ngày; kháng sinh khi đờm mủ/≥2 tiêu chuẩn Anthonisen hoặc cần thông khí; NIV khi toan tăng CO₂.",
            "Hen đợt cấp: SABA lặp lại, ipratropium nếu nặng, steroid sớm; MgSO₄ TM nếu không đáp ứng; adrenaline nếu phản vệ.",
            "SpO₂ mục tiêu COPD 88–92%; đánh giá ABG khi nặng.",
            "Chỉnh liều kháng sinh theo eGFR; theo dõi QTc với macrolide/quinolone.",
            "Tái đánh giá sau 1–3 giờ; cân nhắc ICU nếu thất bại NIV hoặc toan nặng.",
        ],
        "related_calculators": ["PERC/Wells", "BMI", "CrCl (Cockcroft-Gault)", "ABG interpreter"],
        "related_protocols": ["COPD exacerbation protocol", "Acute asthma protocol"],
    },
    {
        "id": "ards_ventilation",
        "title": "ARDS và thở máy: Vt bảo vệ phổi, PEEP/FiO₂, prone, cứu vãn",
        "specialty": "Hồi sức / Thở máy",
        "keywords": ["ARDS", "PEEP", "FiO2", "prone", "ECMO", "ARDSNet", "driving pressure"],
        "path": BASE_DIR / "docs" / "articles" / "ards_ventilation.md",
        "last_reviewed": "2025-01",
        "guidelines": ["ATS/ESICM/SCCM ARDS ventilation", "SSC 2021/2024 updates"],
        "summary": [
            "Vt 4–6 mL/kg PBW, Pplat ≤30; chú ý driving pressure ≤15.",
            "Dùng bảng PEEP/FiO₂; tăng PEEP theo bậc, theo dõi huyết động.",
            "Prone 12–16h/ngày cho ARDS trung bình-nặng (PaO₂/FiO₂ <150) nếu không chống chỉ định.",
            "Cân nhắc giãn cơ ngắn hạn khi dyssynchrony nặng; tránh kéo dài.",
            "Cứu vãn: ECMO VV khi thất bại tối ưu thông khí + prone + paralysis.",
        ],
        "related_calculators": ["ARDSNet tidal volume", "PEEP/FiO₂ table", "ABG interpreter", "BMI/PBW calculator"],
        "related_protocols": ["ARDSNet protocol", "ARDS prone positioning checklist"],
    },
    {
        "id": "acute_heart_failure",
        "title": "Suy tim cấp: lợi tiểu, vasodilator, inotrope, đích huyết động",
        "specialty": "Tim mạch / Hồi sức",
        "keywords": ["acute heart failure", "lợi tiểu", "vasodilator", "inotrope", "ESC HF 2023"],
        "path": BASE_DIR / "docs" / "articles" / "acute_heart_failure.md",
        "last_reviewed": "2025-01",
        "guidelines": ["ESC HF 2023", "ACC/AHA/HFSA 2022–2024"],
        "summary": [
            "Phân nhóm warm/cold, wet/dry để chọn thuốc; mục tiêu giảm sung huyết và duy trì tưới máu.",
            "Lợi tiểu quai IV nền; tăng liều/nhắc lại hoặc phối hợp thiazide-like khi kháng lợi tiểu.",
            "Vasodilator khi HA đủ; inotrope/vasopressor nếu giảm tưới máu hoặc sốc tim.",
            "Theo dõi nước tiểu, cân nặng, điện giải, creatinine; điều chỉnh nhanh mỗi 6–12h.",
            "Tối ưu điều trị nền (ARNI/ACEi/ARB, β-blocker, MRA, SGLT2i) sau ổn định.",
        ],
        "related_calculators": ["eGFR (CKD-EPI)", "CrCl (Cockcroft-Gault)", "BNP/NT-proBNP interpret"],
        "related_protocols": ["Acute Heart Failure protocol", "(đề xuất) Diuretic escalation checklist"],
    },
    {
        "id": "t2dm_inpatient_outpatient",
        "title": "Đái tháo đường típ 2: kiểm soát đường huyết nội trú và lựa chọn thuốc ngoại trú",
        "specialty": "Nội tiết / Chuyển hóa",
        "keywords": ["T2DM", "insulin", "SGLT2i", "GLP-1 RA", "ADA 2025", "basal-bolus"],
        "path": BASE_DIR / "docs" / "articles" / "t2dm_inpatient_outpatient.md",
        "last_reviewed": "2025-01",
        "guidelines": ["ADA 2025", "AACE/ACE"],
        "summary": [
            "Nội trú: ưu tiên insulin basal-bolus/correction; mục tiêu 140–180 mg/dL, thấp hơn nếu an toàn.",
            "Dừng SGLT2i khi nhập viện/phẫu thuật; thận trọng metformin ở eGFR thấp hoặc thủ thuật cản quang.",
            "Ngoại trú: ưu tiên SGLT2i/GLP-1 RA khi ASCVD/CKD/HF/béo phì; cá thể hóa HbA1c mục tiêu.",
            "Giáo dục sick-day rules, tự theo dõi, nhận diện hạ đường huyết.",
            "Chỉnh liều theo eGFR; giảm liều insulin khởi đầu ở người già/suy thận.",
        ],
        "related_calculators": ["CrCl (Cockcroft-Gault)", "eGFR", "BMI"],
        "related_protocols": ["Inpatient glycemic control protocol", "(đề xuất) Outpatient T2DM escalation pathway"],
    },
    {
        "id": "cirrhosis_complications",
        "title": "Xơ gan và biến chứng: XHTH, báng, HE, dự phòng tiên phát/thứ phát",
        "specialty": "Tiêu hóa / Gan mật",
        "keywords": ["xơ gan", "XHTH", "báng", "HE", "MELD", "Child-Pugh"],
        "path": BASE_DIR / "docs" / "articles" / "cirrhosis_complications.md",
        "last_reviewed": "2025-01",
        "guidelines": ["EASL portal hypertension/cirrhosis", "ACG variceal bleeding"],
        "summary": [
            "XHTH: resuscitation kiểm soát, kháng sinh dự phòng, octreotide/terlipressin, thắt TM trong 12h; cứu vãn TIPS nếu cần.",
            "Báng: hạn chế muối, spironolactone ± furosemide; chọc tháo lớn kèm albumin; báng kháng trị → TIPS.",
            "HE: lactulose đạt 2–3 lần phân mềm/ngày, thêm rifaximin khi tái phát; tìm và xử lý yếu tố thúc đẩy.",
            "Dự phòng tiên phát/thứ phát: NSBB hoặc thắt TM; tiếp tục NSBB nếu dung nạp.",
            "Đánh giá MELD/MELD-Na cho ghép; tiêm ngừa HBV/HAV, tránh NSAID.",
        ],
        "related_calculators": ["Child-Pugh", "MELD/MELD-Na", "eGFR", "BMI"],
        "related_protocols": ["XHTH tiêu hóa trên do vỡ giãn tĩnh mạch", "(đề xuất) HE/báng checklist"],
    },
    {
        "id": "antibiotic_stewardship",
        "title": "Kháng sinh theo tác nhân và vị trí nhiễm: Stewardship, PK/PD, TDM",
        "specialty": "Nhiễm khuẩn / Dược lâm sàng",
        "keywords": ["kháng sinh", "IDSA", "ATS", "ESCMID", "stewardship", "PK/PD", "TDM", "AUC/MIC", "fT>MIC"],
        "path": BASE_DIR / "docs" / "articles" / "antibiotic_stewardship.md",
        "last_reviewed": "2025-01",
        "guidelines": ["IDSA/ATS CAP 2019", "IDSA/ATS HAP/VAP 2016", "IDSA/SHEA Stewardship 2016"],
        "summary": [
            "Chọn kháng sinh theo vị trí nhiễm, tác nhân nghi ngờ, nguy cơ MDR; dùng guideline IDSA/ATS/ESCMID.",
            "PK/PD: β-lactam cần fT>MIC 40–70%; vancomycin AUC/MIC ≥400; aminoglycoside Cmax/MIC ≥8–10.",
            "TDM: vancomycin (trough 15–20 nếu nặng, 10–15 thông thường), aminoglycoside (peak/trough), linezolid (nếu dài hạn).",
            "Thời gian dùng: CAP 5–7 ngày; HAP/VAP 7–8 ngày; de-escalation khi có kết quả cấy.",
            "Chỉnh liều theo CrCl/eGFR; tránh dùng không cần thiết và kéo dài.",
        ],
        "related_calculators": ["CrCl (Cockcroft-Gault)", "eGFR", "Vancomycin TDM", "Aminoglycoside dosing"],
        "related_protocols": ["Sepsis 1-Hour Bundle", "(đề xuất) Antibiotic stewardship checklist"],
    },
    {
        "id": "pregnancy_hypertension_preeclampsia",
        "title": "Tăng huyết áp thai kỳ và tiền sản giật: MgSO₄, chỉ định sản khoa",
        "specialty": "Sản khoa",
        "keywords": ["tăng huyết áp thai kỳ", "tiền sản giật", "eclampsia", "MgSO4", "ACOG", "SMFM"],
        "path": BASE_DIR / "docs" / "articles" / "pregnancy_hypertension_preeclampsia.md",
        "last_reviewed": "2025-01",
        "guidelines": ["ACOG Gestational Hypertension & Preeclampsia 2020", "SMFM Preeclampsia 2023", "WHO"],
        "summary": [
            "Phân loại: tăng huyết áp thai kỳ, tiền sản giật (nhẹ/nặng), tiền sản giật trên nền tăng huyết áp mạn, HELLP, eclampsia.",
            "Tiền sản giật nặng: HA ≥160/110, đau đầu/thị lực, đau thượng vị, suy thận, giảm tiểu cầu, tăng men gan; chỉ định chấm dứt thai kỳ.",
            "MgSO₄: liều tải 4–6g TM trong 15–20 phút, duy trì 1–2g/giờ; mục tiêu nồng độ 4–7 mg/dL; theo dõi phản xạ gân xương, nhịp thở, nước tiểu.",
            "Kiểm soát HA: labetalol, nifedipine, hydralazine; tránh hạ quá nhanh; mục tiêu <160/110 (ACOG 2020).",
            "Chấm dứt thai kỳ: ≥34 tuần hoặc <34 tuần nếu nặng/không đáp ứng; dự phòng steroid nếu <34 tuần.",
        ],
        "related_calculators": ["Preeclampsia Severity", "Bishop Score", "Modified Bishop", "BMI"],
        "related_protocols": ["(đề xuất) Preeclampsia management checklist", "(đề xuất) MgSO4 dosing protocol"],
    },
    {
        "id": "sepsis_bundle",
        "title": "Sepsis và Septic Shock: 1-Hour Bundle, kháng sinh, dịch truyền, vận mạch",
        "specialty": "Hồi sức / Nhiễm khuẩn",
        "keywords": ["sepsis", "septic shock", "SSC 2021", "1-hour bundle", "lactate", "norepinephrine", "vasopressin"],
        "path": BASE_DIR / "docs" / "articles" / "sepsis_bundle.md",
        "last_reviewed": "2025-01",
        "guidelines": ["SSC 2021", "SSC 2024 Updates", "IDSA/SCCM Sepsis-3"],
        "summary": [
            "Sepsis-3: nhiễm khuẩn + rối loạn chức năng cơ quan (SOFA ≥2); septic shock = sepsis + hạ huyết áp + lactate ≥2.",
            "1-Hour Bundle: đo lactate, cấy máu trước kháng sinh, kháng sinh trong 1 giờ, dịch 30 mL/kg nếu hạ HA/lactate ≥4, norepinephrine nếu hạ HA sau dịch.",
            "Kháng sinh: phổ rộng trong 1 giờ; de-escalation sau 48–72h khi có kết quả cấy.",
            "Dịch truyền: 30 mL/kg crystalloid ban đầu; tránh quá tải dịch; đánh giá đáp ứng (lactate, HA, nước tiểu).",
            "Vận mạch: norepinephrine hàng đầu; thêm vasopressin/epinephrine nếu cần; mục tiêu MAP ≥65.",
        ],
        "related_calculators": ["SOFA", "qSOFA", "APACHE II", "SAPS II", "CrCl (Cockcroft-Gault)", "eGFR"],
        "related_protocols": ["Sepsis 1-Hour Bundle"],
    },
    {
        "id": "aki_kdigo",
        "title": "Suy thận cấp (AKI): KDIGO, phân loại, xử trí, chỉnh liều thuốc",
        "specialty": "Thận / Hồi sức",
        "keywords": ["AKI", "KDIGO", "RIFLE", "AKIN", "suy thận cấp", "lọc máu", "chỉnh liều thuốc"],
        "path": BASE_DIR / "docs" / "articles" / "aki_kdigo.md",
        "last_reviewed": "2025-01",
        "guidelines": ["KDIGO AKI 2012", "KDIGO 2024 CKD (tham khảo)"],
        "summary": [
            "KDIGO: tăng creatinine ≥0.3 mg/dL trong 48h hoặc ≥1.5× baseline trong 7 ngày, hoặc nước tiểu <0.5 mL/kg/giờ trong 6h.",
            "Phân loại: Stage 1 (creatinine 1.5–1.9× hoặc ≥0.3 tăng, nước tiểu <0.5 mL/kg/giờ 6–12h), Stage 2 (2–2.9×, nước tiểu <0.5 mL/kg/giờ ≥12h), Stage 3 (≥3× hoặc ≥4.0 mg/dL hoặc RRT, nước tiểu <0.5 mL/kg/giờ ≥24h).",
            "Nguyên nhân: prerenal (giảm tưới máu), intrinsic (tổn thương thận), postrenal (tắc nghẽn).",
            "Xử trí: điều chỉnh nguyên nhân, bù dịch nếu prerenal, tránh nephrotoxin, chỉnh liều thuốc, cân nhắc RRT khi stage 3 hoặc quá tải dịch/toan nặng.",
            "Chỉnh liều thuốc: dùng CrCl thay vì eGFR; tránh tích lũy và độc tính.",
        ],
        "related_calculators": ["KDIGO AKI", "RIFLE", "AKIN", "eGFR (CKD-EPI)", "CrCl (Cockcroft-Gault)", "FENa"],
        "related_protocols": ["(đề xuất) AKI management checklist", "(đề xuất) Drug dosing in AKI"],
    },
    {
        "id": "stroke_management",
        "title": "Đột quỵ cấp: tPA, can thiệp nội mạch, xử trí nội khoa, dự phòng thứ phát",
        "specialty": "Thần kinh / Cấp cứu",
        "keywords": ["đột quỵ", "stroke", "tPA", "thrombolysis", "thrombectomy", "AHA/ASA", "NIHSS"],
        "path": BASE_DIR / "docs" / "articles" / "stroke_management.md",
        "last_reviewed": "2025-01",
        "guidelines": ["AHA/ASA Ischemic Stroke 2019/2021", "AHA/ASA ICH 2022"],
        "summary": [
            "Đột quỵ thiếu máu: tPA IV trong 4.5h (0.9 mg/kg, tối đa 90mg); thrombectomy trong 6–24h nếu LVO; aspirin 24h sau tPA (nếu không chảy máu).",
            "Đột quỵ xuất huyết: kiểm soát HA <140 (labetalol, nicardipine); đảo ngược kháng đông nếu có; cân nhắc phẫu thuật nếu ICH lớn/tiến triển.",
            "Xử trí nội khoa: HA <220/120 nếu không tPA; hạ thân nhiệt nếu sốt; kiểm soát đường huyết 140–180; tránh hạ đường huyết.",
            "Dự phòng thứ phát: aspirin/clopidogrel (nếu không rung nhĩ); warfarin/DOAC nếu rung nhĩ; statin; kiểm soát HA/ĐTĐ.",
            "Theo dõi: NIHSS, GCS, dấu hiệu chảy máu; tái đánh giá sau 24h.",
        ],
        "related_calculators": ["NIHSS", "ICH Score", "mRS", "GCS"],
        "related_protocols": ["(đề xuất) Stroke code checklist", "(đề xuất) tPA administration protocol"],
    },
    {
        "id": "atrial_fibrillation",
        "title": "Rung nhĩ: kiểm soát nhịp/tần số, kháng đông, chuyển nhịp, catheter ablation",
        "specialty": "Tim mạch / Rối loạn nhịp",
        "keywords": ["rung nhĩ", "atrial fibrillation", "AF", "CHADS2-VASc", "HAS-BLED", "DOAC", "cardioversion"],
        "path": BASE_DIR / "docs" / "articles" / "atrial_fibrillation.md",
        "last_reviewed": "2025-01",
        "guidelines": ["ESC AF 2020/2022", "ACC/AHA/HRS AF 2019/2024"],
        "summary": [
            "Phân loại: paroxysmal (<7 ngày tự hết), persistent (≥7 ngày hoặc cần chuyển nhịp), long-standing persistent (≥12 tháng), permanent (chấp nhận).",
            "Kháng đông: CHADS₂-VASc ≥2 (nam) hoặc ≥3 (nữ) → kháng đông; DOAC ưu tiên hơn warfarin (trừ van cơ học, hẹp van 2 lá nặng).",
            "Kiểm soát tần số: β-blocker, non-DHP CCB, digoxin; mục tiêu <110 bpm lúc nghỉ.",
            "Kiểm soát nhịp: amiodarone, flecainide, propafenone, sotalol; chuyển nhịp (điện hoặc thuốc) nếu <48h hoặc TEE âm tính.",
            "Catheter ablation: cân nhắc khi kháng thuốc hoặc không dung nạp; ưu tiên ở bệnh nhân trẻ, paroxysmal AF.",
        ],
        "related_calculators": ["CHADS₂-VASc", "HAS-BLED", "QTc", "CrCl (Cockcroft-Gault)", "eGFR"],
        "related_protocols": ["(đề xuất) AF management pathway", "(đề xuất) Anticoagulation decision tree"],
    },
    {
        "id": "electrolyte_disorders",
        "title": "Rối loạn điện giải: Na, K, Ca, Mg, P - chẩn đoán, xử trí, chỉnh liều",
        "specialty": "Nội khoa / Hồi sức",
        "keywords": ["rối loạn điện giải", "natri", "kali", "canxi", "magie", "phospho", "hyponatremia", "hyperkalemia"],
        "path": BASE_DIR / "docs" / "articles" / "electrolyte_disorders.md",
        "last_reviewed": "2025-01",
        "guidelines": ["KDIGO Electrolyte Disorders (tham khảo)", "Endocrine Society Hyponatremia 2014", "AHA/ACC Hyperkalemia"],
        "summary": [
            "Hạ natri: phân loại theo thể tích (hypovolemic, euvolemic, hypervolemic); điều chỉnh chậm (<6–8 mEq/L/24h) để tránh ODS; dùng nước muối 3% nếu nặng/có triệu chứng.",
            "Tăng kali: >6.5 hoặc có triệu chứng → cấp cứu (calcium gluconate, insulin+glucose, albuterol, furosemide, kayexalate); điều chỉnh nguyên nhân.",
            "Hạ kali: bù K+ PO/IV; mục tiêu 4.0–4.5 mEq/L; theo dõi ECG nếu nặng.",
            "Hạ canxi: bù Ca gluconate IV nếu nặng/có triệu chứng; bổ sung vitamin D nếu thiếu; điều chỉnh nguyên nhân.",
            "Tăng canxi: bù dịch, furosemide, bisphosphonate, calcitonin nếu nặng; điều chỉnh nguyên nhân (PTH, malignancy).",
        ],
        "related_calculators": ["Osmolality", "Anion Gap", "Corrected Ca", "FENa", "eGFR", "CrCl"],
        "related_protocols": ["(đề xuất) Electrolyte replacement protocol", "(đề xuất) Hyperkalemia emergency protocol"],
    },
    {
        "id": "anaphylaxis",
        "title": "Phản vệ: chẩn đoán, xử trí cấp cứu, adrenaline, dự phòng",
        "specialty": "Cấp cứu / Dị ứng",
        "keywords": ["phản vệ", "anaphylaxis", "adrenaline", "epinephrine", "WAO", "AAAAI"],
        "path": BASE_DIR / "docs" / "articles" / "anaphylaxis.md",
        "last_reviewed": "2025-01",
        "guidelines": ["WAO Anaphylaxis 2020", "AAAAI Anaphylaxis 2020"],
        "summary": [
            "Chẩn đoán: phản ứng dị ứng cấp + một trong: tổn thương da/niêm mạc, hô hấp, huyết động, tiêu hóa; hoặc hạ HA sau tiếp xúc dị nguyên đã biết.",
            "Xử trí ngay: adrenaline IM 0.3–0.5 mg (0.01 mg/kg trẻ em) vào cơ đùi ngoài; lặp lại sau 5–15 phút nếu không đáp ứng.",
            "Hỗ trợ: nằm ngửa, nâng chân; oxy, truyền dịch nếu hạ HA; albuterol khí dung nếu co thắt phế quản.",
            "Theo dõi: 4–6 giờ sau phản ứng nặng; 24 giờ nếu có triệu chứng hô hấp hoặc cần >1 liều adrenaline.",
            "Dự phòng: tránh dị nguyên, epinephrine auto-injector, giáo dục bệnh nhân và người thân.",
        ],
        "related_calculators": ["BMI", "CrCl (Cockcroft-Gault)"],
        "related_protocols": ["(đề xuất) Anaphylaxis emergency protocol", "(đề xuất) Epinephrine auto-injector guide"],
    },
    {
        "id": "antiallergy_medications",
        "title": "Thuốc chống dị ứng: Antihistamine, Corticosteroid, Leukotriene Modifier, Mast Cell Stabilizer",
        "specialty": "Dị ứng / Dược lâm sàng",
        "keywords": ["antihistamine", "dị ứng", "allergy", "H1 antagonist", "corticosteroid", "leukotriene", "mast cell", "WAO", "AAAAI", "EAACI"],
        "path": BASE_DIR / "docs" / "articles" / "antiallergy_medications.md",
        "last_reviewed": "2025-01",
        "guidelines": ["WAO Guidelines 2020", "AAAAI Practice Parameters 2020", "EAACI Guidelines 2020"],
        "summary": [
            "Antihistamine H1: thế hệ 1 (diphenhydramine) gây buồn ngủ; thế hệ 2 (cetirizine, loratadine, fexofenadine) ít buồn ngủ, dùng hàng ngày.",
            "Corticosteroid: dùng tại chỗ (mũi, da) ưu tiên; uống/tiêm chỉ khi nặng, ngắn hạn.",
            "Leukotriene modifier: montelukast cho allergic rhinitis và asthma; zafirlukast cho asthma.",
            "Mast cell stabilizer: cromolyn, nedocromil dự phòng; tác dụng chậm, cần dùng trước tiếp xúc dị nguyên.",
            "Chỉnh liều theo chức năng thận/gan; tránh tương tác thuốc (CYP450, P-glycoprotein).",
        ],
        "related_calculators": ["BMI", "CrCl (Cockcroft-Gault)", "eGFR"],
        "related_protocols": ["Anaphylaxis emergency protocol", "(đề xuất) Allergic rhinitis management", "(đề xuất) Urticaria management"],
    },
    {
        "id": "pain_relief_antiinflammatory",
        "title": "Thuốc giảm đau chống viêm: Paracetamol, NSAID, Corticosteroid, Opioid",
        "specialty": "Giảm đau / Dược lâm sàng",
        "keywords": ["paracetamol", "acetaminophen", "NSAID", "ibuprofen", "naproxen", "diclofenac", "corticosteroid", "opioid", "WHO", "APS", "ESRA"],
        "path": BASE_DIR / "docs" / "articles" / "pain_relief_antiinflammatory.md",
        "last_reviewed": "2025-01",
        "guidelines": ["WHO Pain Ladder 2020", "APS Guidelines 2016", "ESRA Guidelines 2020"],
        "summary": [
            "Paracetamol: giảm đau, hạ sốt an toàn; liều tối đa 4g/ngày (người lớn), 60–75 mg/kg/ngày (trẻ em); tránh quá liều (ngộ độc gan).",
            "NSAID: giảm đau, chống viêm; ibuprofen, naproxen, diclofenac; tác dụng phụ: GI, thận, tim mạch; tránh ở suy thận, suy tim, loét dạ dày.",
            "Corticosteroid: chống viêm mạnh; prednisone, methylprednisolone; dùng ngắn hạn, tránh dài hạn (loãng xương, tăng đường huyết).",
            "Opioid: giảm đau mạnh; morphine, tramadol, oxycodone; dùng khi đau nặng không đáp ứng paracetamol/NSAID; cảnh giác lệ thuộc, suy hô hấp.",
            "Chỉnh liều theo chức năng thận/gan; tránh tương tác thuốc (warfarin, ACEi/ARB, lợi tiểu).",
        ],
        "related_calculators": ["BMI", "CrCl (Cockcroft-Gault)", "eGFR", "Paracetamol overdose nomogram"],
        "related_protocols": ["Paracetamol overdose", "(đề xuất) Acute pain management", "(đề xuất) Chronic pain management"],
    },
    {
        "id": "topical_medications",
        "title": "Thuốc dùng ngoài: Corticosteroid, Kháng sinh, Chống nấm, Retinoid, Calcineurin Inhibitor",
        "specialty": "Da liễu / Dược lâm sàng",
        "keywords": ["topical", "dùng ngoài", "corticosteroid", "kháng sinh", "chống nấm", "retinoid", "calcineurin", "dermatology", "AAD", "EADV"],
        "path": BASE_DIR / "docs" / "articles" / "topical_medications.md",
        "last_reviewed": "2025-01",
        "guidelines": ["AAD Guidelines 2020-2024", "EADV Guidelines 2020-2024", "BAD Guidelines 2020-2024"],
        "summary": [
            "Corticosteroid tại chỗ: phân loại theo độ mạnh (I-VII); dùng ngắn hạn, giảm liều dần; tránh dùng lâu dài (teo da, giãn mạch).",
            "Kháng sinh tại chỗ: mupirocin, fusidic acid cho nhiễm khuẩn; clindamycin, erythromycin cho mụn; tránh kháng sinh phổ rộng dài hạn (kháng thuốc).",
            "Chống nấm tại chỗ: azole (clotrimazole, miconazole), allylamine (terbinafine), polyene (nystatin); dùng 2-4 tuần, tiếp tục 1 tuần sau hết triệu chứng.",
            "Retinoid tại chỗ: tretinoin, adapalene, tazarotene cho mụn/vẩy nến; bắt đầu liều thấp, tránh khi có thai (teratogenic).",
            "Calcineurin inhibitor: tacrolimus, pimecrolimus cho viêm da cơ địa; an toàn hơn corticosteroid dài hạn, nhưng cảnh giác ung thư da (hiếm).",
            "Vitamin D analogues: calcipotriol, calcitriol cho vẩy nến; kết hợp với corticosteroid tăng hiệu quả.",
        ],
        "related_calculators": ["BMI", "BSA (Body Surface Area)"],
        "related_protocols": ["Psoriasis", "Atopic Dermatitis", "Acne Vulgaris", "Fungal Infections", "Contact Dermatitis"],
    },
    {
        "id": "psychotropic_medications",
        "title": "Thuốc hướng thần tâm thần kinh: Chống trầm cảm, Chống loạn thần, Ổn định khí sắc, Chống lo âu",
        "specialty": "Tâm thần / Dược lâm sàng",
        "keywords": ["psychotropic", "antidepressant", "antipsychotic", "mood stabilizer", "anxiolytic", "SSRI", "SNRI", "TCA", "benzodiazepine", "APA", "NICE", "WFSBP"],
        "path": BASE_DIR / "docs" / "articles" / "psychotropic_medications.md",
        "last_reviewed": "2025-01",
        "guidelines": ["APA Practice Guidelines 2020-2024", "NICE Guidelines 2020-2024", "WFSBP Guidelines 2020-2024"],
        "summary": [
            "SSRI: fluoxetine, sertraline, citalopram, escitalopram; khởi đầu liều thấp, tăng dần; tác dụng phụ: buồn nôn, mất ngủ, rối loạn tình dục; tránh dừng đột ngột (hội chứng cai).",
            "SNRI: venlafaxine, duloxetine; tác dụng tương tự SSRI + giảm đau; tăng huyết áp ở liều cao (venlafaxine).",
            "TCA: amitriptyline, imipramine; hiệu quả tốt nhưng nhiều tác dụng phụ (anticholinergic, tim mạch); nguy cơ quá liều cao.",
            "Chống loạn thần: typical (haloperidol) và atypical (risperidone, olanzapine, quetiapine); tác dụng phụ: ngoại tháp, tăng cân, rối loạn chuyển hóa, QTc kéo dài.",
            "Ổn định khí sắc: lithium, valproate, carbamazepine, lamotrigine; cần TDM, chỉnh liều theo chức năng thận/gan; cảnh giác độc tính.",
            "Benzodiazepine: alprazolam, lorazepam, diazepam; dùng ngắn hạn, tránh dài hạn (lệ thuộc, dung nạp); giảm liều dần khi ngừng.",
        ],
        "related_calculators": ["BMI", "CrCl (Cockcroft-Gault)", "eGFR", "QTc"],
        "related_protocols": ["(đề xuất) Depression management", "(đề xuất) Anxiety management", "(đề xuất) Bipolar disorder management"],
    },
    {
        "id": "bronchodilators_copd_asthma",
        "title": "Thuốc giãn phế quản điều trị COPD và Hen: SABA, LABA, SAMA, LAMA, ICS, Kết hợp",
        "specialty": "Hô hấp / Dược lâm sàng",
        "keywords": ["bronchodilator", "giãn phế quản", "SABA", "LABA", "SAMA", "LAMA", "ICS", "COPD", "asthma", "GOLD", "GINA", "salbutamol", "tiotropium", "salmeterol"],
        "path": BASE_DIR / "docs" / "articles" / "bronchodilators_copd_asthma.md",
        "last_reviewed": "2025-01",
        "guidelines": ["GOLD 2024", "GINA 2024", "ATS/ERS Guidelines 2020-2024"],
        "summary": [
            "SABA: salbutamol, terbutaline; tác dụng nhanh (5-15 phút), ngắn (4-6 giờ); dùng cắt cơn, trước gắng sức; tác dụng phụ: run tay, nhịp tim nhanh, hạ kali máu.",
            "LABA: salmeterol, formoterol, indacaterol; tác dụng dài (12-24 giờ); dùng duy trì, không dùng cắt cơn; tác dụng phụ: tương tự SABA nhưng ít hơn.",
            "SAMA: ipratropium; tác dụng nhanh (15-30 phút), ngắn (6-8 giờ); phối hợp với SABA trong đợt cấp; tác dụng phụ: khô miệng, bí tiểu (hiếm).",
            "LAMA: tiotropium, aclidinium, glycopyrronium, umecidinium; tác dụng dài (24 giờ); dùng duy trì COPD; tác dụng phụ: khô miệng, bí tiểu, táo bón.",
            "ICS: fluticasone, budesonide, beclomethasone; chống viêm, giảm đợt cấp; dùng duy trì hen và COPD có eosinophil cao; tác dụng phụ: nấm miệng, khàn tiếng, loãng xương (dài hạn).",
            "Kết hợp: LABA/ICS (hen, COPD), LAMA/LABA (COPD), LAMA/LABA/ICS (COPD nặng); tăng hiệu quả, giảm số lần hít.",
        ],
        "related_calculators": ["BMI", "ABG interpreter", "PERC/Wells"],
        "related_protocols": ["COPD exacerbation", "Acute asthma", "COPD management", "Asthma management"],
    },
    {
        "id": "cerebrovascular_medications",
        "title": "Thuốc tuần hoàn não: Giãn mạch, Cải thiện chuyển hóa, Chống oxy hóa, Bảo vệ thần kinh",
        "specialty": "Thần kinh / Dược lâm sàng",
        "keywords": ["tuần hoàn não", "cerebrovascular", "nimodipine", "piracetam", "vinpocetine", "ginkgo", "citicoline", "cinnarizine", "flunarizine", "AHA/ASA", "EAN"],
        "path": BASE_DIR / "docs" / "articles" / "cerebrovascular_medications.md",
        "last_reviewed": "2025-01",
        "guidelines": ["AHA/ASA Guidelines 2020-2024", "EAN Guidelines 2020-2024", "EFNS Guidelines"],
        "summary": [
            "Nimodipine: CCB chọn lọc mạch não; chỉ định SAH (60mg q4h × 21 ngày); tác dụng phụ: hạ huyết áp, nhức đầu; cần theo dõi huyết áp.",
            "Piracetam: nootropic, cải thiện chức năng nhận thức; chỉ định sa sút trí tuệ, chấn thương sọ não; tác dụng phụ: buồn nôn, mất ngủ; hiệu quả chưa rõ ràng.",
            "Vinpocetine: cải thiện lưu thông máu não, chống oxy hóa; chỉ định sa sút trí tuệ, thiếu máu não; tác dụng phụ: nhức đầu, chóng mặt; bằng chứng hạn chế.",
            "Ginkgo biloba: chống oxy hóa, cải thiện lưu thông máu não; chỉ định sa sút trí tuệ nhẹ, ù tai; tác dụng phụ: chảy máu, dị ứng; tương tác warfarin.",
            "Citicoline: bảo vệ tế bào thần kinh, cải thiện chuyển hóa; chỉ định đột quỵ thiếu máu, chấn thương sọ não; tác dụng phụ: buồn nôn, nhức đầu; bằng chứng hạn chế.",
            "Cinnarizine/Flunarizine: CCB, chống histamine; chỉ định chóng mặt, đau nửa đầu; tác dụng phụ: buồn ngủ, trầm cảm, parkinsonism (flunarizine).",
        ],
        "related_calculators": ["BMI", "CrCl (Cockcroft-Gault)", "eGFR", "NIHSS", "GCS"],
        "related_protocols": ["Stroke management", "(đề xuất) Subarachnoid hemorrhage management", "(đề xuất) Cognitive impairment management"],
    },
    {
        "id": "antibiotic_combinations",
        "title": "Kháng sinh và phối hợp: Synergy, Antagonism, Phối hợp thường dùng, Tương tác",
        "specialty": "Nhiễm khuẩn / Dược lâm sàng",
        "keywords": ["kháng sinh", "phối hợp", "combination", "synergy", "antagonism", "IDSA", "ATS", "ESCMID", "stewardship", "PK/PD"],
        "path": BASE_DIR / "docs" / "articles" / "antibiotic_combinations.md",
        "last_reviewed": "2025-01",
        "guidelines": ["IDSA/ATS Guidelines 2019-2024", "IDSA/SHEA Antimicrobial Stewardship 2016 (updates)", "ESCMID Guidelines 2020-2024"],
        "summary": [
            "Phối hợp synergy: β-lactam + aminoglycoside (viêm nội tâm mạc, nhiễm khuẩn huyết GNB nặng); vancomycin + aminoglycoside (viêm nội tâm mạc Enterococcus); β-lactam + β-lactamase inhibitor (mở rộng phổ).",
            "Phối hợp empiric: β-lactam + vancomycin (nghi MRSA); β-lactam + macrolide (CAP); β-lactam + quinolone (CAP, HAP); carbapenem + colistin (GNB kháng).",
            "Phối hợp tránh: β-lactam bacteriostatic + bacteriostatic (antagonism); chloramphenicol + penicillin (antagonism); vancomycin + aminoglycoside (độc thận, chỉ dùng khi cần).",
            "Tương tác độc tính: vancomycin + aminoglycoside (độc thận); aminoglycoside + furosemide (độc thận, độc tai); linezolid + SSRI (serotonin syndrome).",
            "De-escalation: chuyển từ phối hợp sang đơn trị khi có kết quả cấy; giảm phổ kháng sinh; rút ngắn thời gian.",
            "Sử dụng công cụ trong app: tra cứu kháng sinh, so sánh liều, phác đồ điều trị, tính liều theo thận.",
        ],
        "related_calculators": ["CrCl (Cockcroft-Gault)", "eGFR", "Vancomycin TDM", "Aminoglycoside dosing"],
        "related_protocols": ["Sepsis 1-Hour Bundle", "COPD exacerbation", "Pneumonia"],
        "related_menu_sections": [
            "💊 Tra cứu & dữ liệu kháng sinh",
            "🔬 So sánh nhiều kháng sinh",
            "📊 So sánh Side-by-Side",
            "🔄 Phác đồ điều trị",
            "🧮 Tính liều theo eGFR/CrCl"
        ],
    },
]


def load_article_content(path: Path) -> str:
    """Đọc nội dung markdown từ file; trả về chuỗi rỗng nếu thiếu."""
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""


def estimate_reading_time(content: str) -> int:
    """Ước tính thời gian đọc (phút) dựa trên số từ."""
    words = len(content.split())
    # Trung bình 200 từ/phút
    return max(1, round(words / 200))


def get_specialty_color(specialty: str) -> tuple:
    """Trả về màu gradient và border cho từng chuyên khoa."""
    colors = {
        "Tim mạch": ("linear-gradient(135deg, #667eea 0%, #764ba2 100%)", "#667eea"),
        "Tim mạch cấp cứu": ("linear-gradient(135deg, #f093fb 0%, #f5576c 100%)", "#f5576c"),
        "Tim mạch / Hồi sức": ("linear-gradient(135deg, #f093fb 0%, #f5576c 100%)", "#f5576c"),
        "Tim mạch / Rối loạn nhịp": ("linear-gradient(135deg, #667eea 0%, #764ba2 100%)", "#667eea"),
        "Tiêu hóa / Hồi sức": ("linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)", "#4facfe"),
        "Tiêu hóa / Gan mật": ("linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)", "#43e97b"),
        "Hô hấp": ("linear-gradient(135deg, #fa709a 0%, #fee140 100%)", "#fa709a"),
        "Hồi sức / Thở máy": ("linear-gradient(135deg, #30cfd0 0%, #330867 100%)", "#30cfd0"),
        "Hồi sức / Nhiễm khuẩn": ("linear-gradient(135deg, #a8edea 0%, #fed6e3 100%)", "#a8edea"),
        "Nội tiết / Chuyển hóa": ("linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%)", "#fcb69f"),
        "Nhiễm khuẩn / Dược lâm sàng": ("linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%)", "#ff9a9e"),
        "Sản khoa": ("linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%)", "#ffecd2"),
        "Thận / Hồi sức": ("linear-gradient(135deg, #a8edea 0%, #fed6e3 100%)", "#a8edea"),
        "Thần kinh / Cấp cứu": ("linear-gradient(135deg, #667eea 0%, #764ba2 100%)", "#667eea"),
        "Thần kinh / Dược lâm sàng": ("linear-gradient(135deg, #667eea 0%, #764ba2 100%)", "#667eea"),
        "Nội khoa / Hồi sức": ("linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)", "#4facfe"),
        "Cấp cứu / Dị ứng": ("linear-gradient(135deg, #f093fb 0%, #f5576c 100%)", "#f5576c"),
        "Dị ứng / Dược lâm sàng": ("linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%)", "#ff9a9e"),
        "Giảm đau / Dược lâm sàng": ("linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%)", "#ffecd2"),
        "Da liễu / Dược lâm sàng": ("linear-gradient(135deg, #fa709a 0%, #fee140 100%)", "#fa709a"),
        "Tâm thần / Dược lâm sàng": ("linear-gradient(135deg, #a8edea 0%, #fed6e3 100%)", "#a8edea"),
        "Hô hấp / Dược lâm sàng": ("linear-gradient(135deg, #fa709a 0%, #fee140 100%)", "#fa709a"),
    }
    return colors.get(specialty, ("linear-gradient(135deg, #667eea 0%, #764ba2 100%)", "#667eea"))


def render_statistics_dashboard(articles: list):
    """Hiển thị dashboard thống kê về các bài viết."""
    total_articles = len(articles)
    specialties = Counter([a["specialty"] for a in articles])
    total_guidelines = len(set([g for a in articles for g in a.get("guidelines", [])]))
    total_keywords = len(set([k for a in articles for k in a.get("keywords", [])]))
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("📚 Tổng số bài viết", total_articles)
    with col2:
        st.metric("🩺 Chuyên khoa", len(specialties))
    with col3:
        st.metric("📑 Hướng dẫn", total_guidelines)
    with col4:
        st.metric("🏷️ Từ khóa", total_keywords)


def render_article_card(article: dict, index: int):
    """Hiển thị thẻ bài viết với thiết kế đẹp và khoa học."""
    specialty = article["specialty"]
    gradient, border_color = get_specialty_color(specialty)
    
    # Tính toán reading time
    content = load_article_content(article["path"])
    reading_time = estimate_reading_time(content) if content else 0
    
    # Tạo card HTML với thiết kế đẹp
    card_id = f"article_card_{article['id']}"
    
    card_html = f"""
    <div id="{card_id}" style="
        background: white;
        border-radius: 16px;
        padding: 0;
        margin-bottom: 24px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        border-left: 4px solid {border_color};
        overflow: hidden;
    " onmouseover="
        this.style.transform='translateY(-4px)';
        this.style.boxShadow='0 8px 24px rgba(0,0,0,0.15)';
    " onmouseout="
        this.style.transform='translateY(0)';
        this.style.boxShadow='0 2px 8px rgba(0,0,0,0.1)';
    ">
        <!-- Header với gradient -->
        <div style="
            background: {gradient};
            padding: 20px 24px;
            color: white;
        ">
            <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 8px;">
                <h3 style="margin: 0; font-size: 1.3rem; font-weight: 600; color: white; line-height: 1.4;">
                    {article['title']}
                </h3>
                <span style="
                    background: rgba(255,255,255,0.2);
                    padding: 4px 12px;
                    border-radius: 12px;
                    font-size: 0.85rem;
                    white-space: nowrap;
                    margin-left: 12px;
                ">{specialty}</span>
            </div>
            <div style="display: flex; gap: 16px; flex-wrap: wrap; font-size: 0.85rem; opacity: 0.95;">
                <span>🔄 {article.get('last_reviewed', 'N/A')}</span>
                {f'<span>⏱️ {reading_time} phút đọc</span>' if reading_time > 0 else ''}
                <span>📑 {len(article.get('guidelines', []))} guideline</span>
            </div>
        </div>
        
        <!-- Body -->
        <div style="padding: 20px 24px;">
            <!-- Guidelines badges -->
            <div style="margin-bottom: 16px;">
                {" ".join([f'<span style="background: #e3f2fd; color: #1976d2; padding: 4px 10px; border-radius: 12px; font-size: 0.8rem; margin-right: 6px; margin-bottom: 6px; display: inline-block;">{g}</span>' for g in article.get('guidelines', [])[:3]])}
            </div>
            
            <!-- Summary points -->
            <div style="margin-bottom: 16px;">
                <strong style="color: #424242; font-size: 0.95rem;">💡 Điểm cần nhớ:</strong>
                <ul style="margin: 8px 0 0 0; padding-left: 20px; color: #616161; font-size: 0.9rem; line-height: 1.6;">
                    {"".join([f'<li style="margin-bottom: 6px;">{item}</li>' for item in article.get('summary', [])[:3]])}
                </ul>
            </div>
            
            <!-- Keywords tags -->
            {f'''
            <div style="margin-bottom: 16px;">
                <div style="display: flex; flex-wrap: wrap; gap: 6px;">
                    {" ".join([f'<span style="background: #f5f5f5; color: #616161; padding: 4px 10px; border-radius: 12px; font-size: 0.75rem; border: 1px solid #e0e0e0;">{k}</span>' for k in article.get('keywords', [])[:6]])}
                </div>
            </div>
            ''' if article.get('keywords') else ''}
            
            <!-- Related links -->
            <div style="
                background: #f8f9fa;
                padding: 12px 16px;
                border-radius: 8px;
                margin-top: 16px;
            ">
                <div style="font-size: 0.85rem; color: #616161;">
                    {f'<div style="margin-bottom: 8px;"><strong>📊 Calculators:</strong> {", ".join(article.get("related_calculators", [])[:3])}</div>' if article.get('related_calculators') else ''}
                    {f'<div><strong>📋 Protocols:</strong> {", ".join(article.get("related_protocols", [])[:2])}</div>' if article.get('related_protocols') else ''}
                </div>
            </div>
        </div>
    </div>
    """
    
    components.html(card_html, height=400, scrolling=False)
    
    # Streamlit expander cho nội dung đầy đủ
    with st.expander(f"📖 Đọc toàn bộ: {article['title']}", expanded=False):
        if content:
            st.markdown(content)
        else:
            st.warning(f"Không tìm thấy nội dung tại {article['path'].name}.")


def filter_articles(search: str, specialties: list, selected_keywords: list):
    """Lọc bài viết theo từ khóa, chuyên khoa và keywords."""
    search_lower = search.lower()
    filtered = []
    
    for article in ARTICLES:
        # Filter by specialty
        if specialties and article["specialty"] not in specialties:
            continue
        
        # Filter by keywords
        if selected_keywords:
            article_keywords = [k.lower() for k in article.get("keywords", [])]
            if not any(kw.lower() in article_keywords for kw in selected_keywords):
                continue
        
        # Filter by search text
        if search_lower:
            haystack = " ".join([
                article["title"],
                article["specialty"],
                " ".join(article.get("keywords", [])),
                " ".join(article.get("summary", [])),
            ]).lower()
            if search_lower not in haystack:
                continue
        
        filtered.append(article)
    
    return filtered


def main():
    setup_page(
        page_title="Bài viết chuyên sâu",
        page_icon="📚",
        description="Tổng hợp chuyên sâu theo guideline mới nhất, gắn liền calculators/protocols trong ứng dụng.",
    )
    
    # Statistics Dashboard
    render_statistics_dashboard(ARTICLES)
    
    st.markdown("---")
    
    # Sidebar filters
    with st.sidebar:
        st.header("🔎 Tìm kiếm & Lọc")
        
        search = st.text_input(
            "🔍 Tìm kiếm",
            value="",
            placeholder="VD: tăng huyết áp, PPI, ICU, sepsis...",
            help="Tìm kiếm theo tiêu đề, chuyên khoa, từ khóa hoặc nội dung"
        )
        
        st.markdown("---")
        
        st.subheader("🩺 Chuyên khoa")
        all_specialties = sorted({article["specialty"] for article in ARTICLES})
        selected_specialties = st.multiselect(
            "Chọn chuyên khoa",
            options=all_specialties,
            default=[],
            help="Chọn một hoặc nhiều chuyên khoa để lọc"
        )
        
        st.markdown("---")
        
        st.subheader("🏷️ Từ khóa phổ biến")
        all_keywords = sorted(set([k for a in ARTICLES for k in a.get("keywords", [])]))
        # Hiển thị top keywords
        keyword_counts = Counter([k for a in ARTICLES for k in a.get("keywords", [])])
        top_keywords = [k for k, _ in keyword_counts.most_common(15)]
        
        selected_keywords = st.multiselect(
            "Chọn từ khóa",
            options=top_keywords,
            default=[],
            help="Chọn từ khóa để lọc bài viết liên quan"
        )
        
        st.markdown("---")
        
        st.info("""
        **📚 Thông tin:**
        
        - Nội dung cập nhật theo guideline quốc tế mới nhất
        - ESC/ESH, ACC/AHA, ACG/AGA, ASHP, IDSA, SSC...
        - Tích hợp với calculators và protocols trong app
        - Được mở rộng và cập nhật định kỳ
        """)
        
        st.markdown("---")
        
        # Quick stats
        st.caption(f"**Tổng số bài viết:** {len(ARTICLES)}")
        st.caption(f"**Chuyên khoa:** {len(all_specialties)}")
    
    # Filter articles
    filtered = filter_articles(search, selected_specialties, selected_keywords)
    
    # Display results
    if not filtered:
        st.warning("""
        **Không tìm thấy bài viết phù hợp.**
        
        Thử:
        - Xóa bộ lọc chuyên khoa
        - Thay đổi từ khóa tìm kiếm
        - Chọn từ khóa khác
        """)
    else:
        st.success(f"Tìm thấy **{len(filtered)}** bài viết phù hợp")
        st.markdown("---")
        
        # Display articles in grid
        for idx, article in enumerate(filtered):
            render_article_card(article, idx)
    
    render_standard_footer(disclaimer=True)


if __name__ == "__main__":
    main()
