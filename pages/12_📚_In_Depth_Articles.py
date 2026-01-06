"""
Trang hiển thị các bài viết chuyên sâu.

Nguồn dữ liệu **1 mối**: content/articles/*.md (auto-discovery).
"""

from pathlib import Path
import html
import re
import streamlit as st
import streamlit.components.v1 as components
from collections import Counter, defaultdict

from utils.page_helper import setup_page, render_standard_footer
from components.ui import render_info_box, render_hero
from config.article_protocol_mapping import (
    get_protocol_for_article,
    has_protocol as check_has_protocol,
    get_protocol_deep_link
)


BASE_DIR = Path(__file__).resolve().parent.parent
CONTENT_ARTICLES_DIR = BASE_DIR / "content" / "articles"

# Legacy (docs/articles) registry is kept for backward compatibility/reference only.
# The app runtime now uses auto-discovery from `content/articles/`.
LEGACY_ARTICLES = [
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
            "Đích HA đa số <140/90; cân nhắc <130/80 nếu dung nạp/nguy cơ cao.",
            "Bước 3: RAASi + CCB + thiazide-like; kháng trị thêm spironolactone khi eGFR/K+ cho phép.",
            "Ưu tiên ACEi/ARB ở CKD/protein niệu, ĐTĐ; β-blocker khi có chỉ định tim mạch.",
            "Theo dõi K+, creatinine/eGFR; tránh triple whammy (RAASi + NSAID + lợi tiểu).",
        ],
        "key_points": [
            "Khởi trị đa số cần 2 thuốc: RAASi + CCB hoặc RAASi + thiazide-like.",
            "Đích HA thường <140/90; cân nhắc <130/80 nếu dung nạp và nguy cơ cao.",
            "Step 3: RAASi + CCB + thiazide-like; thêm spironolactone nếu eGFR/K+ cho phép.",
            "Tránh triple whammy (RAASi + NSAID + lợi tiểu); ưu tiên ACEi/ARB ở CKD/protein niệu/ĐTĐ.",
        ],
        "evidence_level": "High (ESC/ESH 2023/24; ACC/AHA 2024)",
        "recommendation_strength": "Strong",
        "red_flags": [
            "HA ≥180/120 kèm tổn thương cơ quan đích (HA cấp cứu): chuyển tuyến/ICU.",
            "Tăng K+ >5.5 mmol/L hoặc creatinine tăng >30% sau RAASi/MRA.",
            "eGFR <30: tránh thiazide-like; cân nhắc loop; theo dõi sát thể tích.",
            "Đau ngực, khó thở, TK khu trú: loại trừ hội chứng vành/stroke.",
        ],
        "monitoring": [
            "Đo HA tại nhà/ambulatory nếu có; tái kiểm 2–4 tuần sau khởi/đổi liều.",
            "K+, creatinine/eGFR 1–2 tuần sau RAASi/MRA hoặc tăng liều; sau đó mỗi 3–6 tháng.",
            "Điện giải (Na/K) khi dùng thiazide-like; theo dõi phù, hạ HA tư thế ở người già.",
        ],
        "special_populations": [
            "CKD/protein niệu: ưu tiên ACEi/ARB; titrate chậm, theo dõi K+/creatinine.",
            "ĐTĐ/ASCVD nguy cơ cao: cân nhắc đích <130/80 nếu dung nạp.",
            "Người già/hạ thể tích: khởi liều thấp, theo dõi hạ HA tư thế.",
        ],
        "interactions": [
            "NSAID + RAASi + lợi tiểu (triple whammy) → tăng nguy cơ AKI, tăng K+.",
            "RAASi/MRA + bổ sung K+ hoặc thuốc giữ K+ khác → tăng K+.",
            "ACEi/ARB + lithium → tăng nồng độ lithium; cần theo dõi hoặc tránh.",
        ],
        "follow_up": "Tái đánh giá sau 4 tuần (sớm hơn 1–2 tuần nếu chỉnh RAASi/MRA hoặc K+/creatinine cần theo dõi); điều chỉnh phác đồ nếu chưa đạt đích.",
        "related_calculators": ["eGFR (CKD-EPI)", "CrCl (Cockcroft-Gault)", "ASCVD 10-year", "SCORE2/SCORE2-OP", "BMI"],
        "related_protocols": ["(đề xuất) HTN management quick steps"],
        "has_protocol": True,
        "protocol_links": ["pages/04_📋_Protocols.py"],
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
        "key_points": [
            "Dùng thang điểm (GRACE/TIMI/HEART) để phân tầng nguy cơ và quyết định thời gian PCI.",
            "DAPT với aspirin + P2Y₁₂ (ticagrelor/prasugrel ưu tiên, clopidogrel khi có chống chỉ định/nguồn lực).",
            "Chống đông chọn UFH/enoxaparin; fondaparinux cho NSTEMI nguy cơ chảy máu, bivalirudin nếu nguy cơ rất cao.",
            "STEMI: ưu tiên PCI trong thời gian chuẩn (door-to-balloon); nếu không đạt, dùng fibrinolysis rồi PCI cứu vãn.",
        ],
        "evidence_level": "High (ESC 2023; ACC/AHA 2024–2025)",
        "recommendation_strength": "Strong",
        "red_flags": [
            "Đau ngực dai dẳng, huyết động không ổn, VT/VF, sốc tim → cần PCI khẩn (cửa bóng <120 phút, càng sớm càng tốt).",
            "STEMI kèm block nhánh trái mới, VT kéo dài, suy tim cấp (Killip III–IV).",
            "NSTEMI nguy cơ rất cao: đau ngực không kiểm soát, rối loạn nhịp đe dọa, suy tim tiến triển, huyết động không ổn.",
        ],
        "monitoring": [
            "ECG seri (ban đầu, 15–30 phút nếu đau còn), men tim (hs-Tn) theo protocol.",
            "HA, mạch, SpO₂, nhịp thở liên tục; theo dõi dấu hiệu suy tim/phù phổi.",
            "Theo dõi chảy máu (da, niêm, tiêu hóa, nội sọ) khi dùng DAPT/chống đông.",
            "QTc khi dùng thuốc kéo dài QT (amiodarone, sotalol) hoặc phối hợp nhiều thuốc.",
        ],
        "special_populations": [
            "Người già/suy thận: chỉnh liều enoxaparin/fondaparinux; thận trọng nguy cơ chảy máu.",
            "Phụ nữ, ĐTĐ: triệu chứng không điển hình; cần ngưỡng nghi ngờ thấp hơn và thăm dò tích cực.",
            "Bệnh nhân dùng kháng đông đường uống: chiến lược DAPT/anticoag phải cá thể hóa, ưu tiên giảm chảy máu.",
        ],
        "interactions": [
            "Clopidogrel + omeprazole (CYP2C19) có thể giảm hiệu quả; ưu tiên pantoprazole nếu cần PPI.",
            "Trùng lặp kháng đông (heparin + DOAC + kháng tiểu cầu mạnh) → tăng nguy cơ chảy máu nặng.",
            "Statin (simvastatin, lovastatin) + mạnh ức chế CYP3A4 (macrolide, azole) → tăng nguy cơ độc cơ.",
        ],
        "follow_up": "Sau giai đoạn cấp, tối ưu điều trị nền (DAPT, statin cường độ cao, ACEi/ARB/ARNI, β-blocker) và lên kế hoạch DAPT 6–12 tháng tùy nguy cơ chảy máu; tái khám tim mạch sớm.",
        "related_calculators": ["GRACE", "TIMI", "HEART", "CrCl (Cockcroft-Gault)", "BMI"],
        "related_protocols": ["ACS protocol trong app (nếu có)", "(đề xuất) DAPT/anticoag checklist"],
        "has_protocol": True,
        "protocol_links": ["pages/04_📋_Protocols.py"],
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
        "key_points": [
            "COPD đợt cấp: ưu tiên SABA ± SAMA, steroid toàn thân ngắn ngày, cân nhắc kháng sinh theo Anthonisen và nguy cơ.",
            "Hen đợt cấp: SABA lặp lại, thêm ipratropium nếu nặng, steroid sớm; MgSO₄ TM nếu đáp ứng kém.",
            "SpO₂ mục tiêu 88–92% ở COPD (tránh cho quá nhiều oxy); đánh giá ABG khi nặng hoặc nghi tăng CO₂.",
            "NIV cho COPD tăng CO₂ có toan; chuyển ICU/đặt NKQ nếu thất bại NIV hoặc toan xấu đi.",
        ],
        "evidence_level": "Moderate-High (GOLD 2024; GINA 2024)",
        "recommendation_strength": "Strong",
        "red_flags": [
            "SpO₂ <88% dù đã oxy, dấu hiệu mệt cơ hô hấp, co kéo cơ phụ, nói từng từ.",
            "Toan hô hấp pH <7.30, PaCO₂ tăng nhanh, hoặc ý thức xấu đi.",
            "Hen đợt cấp: không đáp ứng SABA nhiều liều, PEF/FEV₁ rất thấp, tiền sử ICU/đặt NKQ.",
            "Huyết động không ổn (tụt HA, loạn nhịp), nghi tràn khí màng phổi hoặc PE.",
        ],
        "monitoring": [
            "SpO₂ liên tục; mục tiêu 88–92% COPD, 94–98% hen nếu không tăng CO₂ nền.",
            "Nhịp thở, nhịp tim, huyết áp, tri giác mỗi 15–30 phút khi mới nhập/khi nặng.",
            "ABG khi SpO₂ khó kiểm soát, COPD nặng, dùng NIV, hoặc nghi tăng CO₂.",
            "Đánh giá đáp ứng mỗi 1–3 giờ; điều chỉnh thuốc giãn phế quản/steroid/kháng sinh.",
        ],
        "special_populations": [
            "Người già/béo phì: dễ suy hô hấp và quá liều an thần; thận trọng benzodiazepine/opioid.",
            "CKD/HC suy gan: chỉnh liều kháng sinh (quinolone, macrolide) và steroid; theo dõi đường huyết.",
            "Tiền sử tim mạch: thận trọng beta-agonist liều cao (nhịp nhanh, rung nhĩ, thiếu máu cơ tim).",
        ],
        "interactions": [
            "Macrolide/quinolone + thuốc kéo dài QT khác (amiodarone, TCA) → nguy cơ xoắn đỉnh.",
            "Theophylline (nếu dùng) tương tác với nhiều thuốc (macrolide, quinolone, cimetidine); dễ ngộ độc.",
            "Steroid toàn thân kéo dài + NSAID/kháng đông → tăng nguy cơ xuất huyết tiêu hóa.",
        ],
        "follow_up": "Đánh giá đáp ứng trong 1–3 giờ đầu; sau ổn định, lập kế hoạch giảm thuốc giãn phế quản, steroid và điều chỉnh điều trị nền; hẹn tái khám/chức năng hô hấp.",
        "related_calculators": ["PERC/Wells", "BMI", "CrCl (Cockcroft-Gault)", "ABG interpreter"],
        "related_protocols": ["COPD exacerbation protocol", "Acute asthma protocol"],
        "has_protocol": True,
        "protocol_links": ["pages/04_📋_Protocols.py"],
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
        "key_points": [
            "Vt 4–6 mL/kg PBW, Pplat ≤30 cmH₂O, driving pressure ≤15 cmH₂O là nền tảng bảo vệ phổi.",
            "Sử dụng bảng PEEP/FiO₂, tăng PEEP từng bước kèm theo dõi huyết động và oxy hóa.",
            "Prone 12–16h/ngày cho ARDS trung bình–nặng (PaO₂/FiO₂ <150) nếu không chống chỉ định.",
            "Giãn cơ ngắn hạn trong 24–48h có thể cân nhắc nếu dyssynchrony nặng, khó kiểm soát.",
            "ECMO VV là biện pháp cứu vãn khi thất bại tối ưu thông khí + prone + giãn cơ.",
        ],
        "evidence_level": "Moderate-High (ARDSNet, ATS/ESICM/SCCM)",
        "recommendation_strength": "Strong",
        "red_flags": [
            "PaO₂/FiO₂ <80 dù đã tối ưu PEEP/FiO₂ và prone.",
            "Pplat >30 cmH₂O hoặc driving pressure >15 cmH₂O dù đã giảm Vt tối đa cho phép.",
            "Huyết động không ổn định khi tăng PEEP (tụt HA, cần vận mạch cao).",
            "Tăng CO₂ nặng, pH <7.15 kéo dài dù đã điều chỉnh tần số/Vt trong giới hạn an toàn.",
        ],
        "monitoring": [
            "ABG định kỳ sau điều chỉnh Vt/PEEP/FiO₂; theo dõi PaO₂/FiO₂, PaCO₂, pH.",
            "Áp lực đường thở (Pplat, driving pressure) sau mỗi thay đổi cài đặt.",
            "Huyết động (HA, mạch, lactate, siêu âm tim nếu có) khi thay đổi PEEP hoặc prone.",
            "Áp lực bụng/nội sọ nếu nghi tăng áp lực khoang; theo dõi loét tỳ đè khi prone kéo dài.",
        ],
        "special_populations": [
            "Béo phì: cần tính PBW chính xác, PEEP thường cao hơn; theo dõi huyết động sát.",
            "Suy tim/suy thất phải: tăng PEEP có thể xấu đi cung lượng tim; cân bằng giữa oxy hóa và huyết động.",
            "Thai kỳ: prone khó áp dụng, cân nhắc lateral/prone modified; cần phối hợp sản khoa.",
        ],
        "interactions": [
            "Sedation + giãn cơ kéo dài → yếu cơ, ICU-acquired weakness; cần chiến lược giảm liều sớm.",
            "Thông khí áp lực cao + quá tải dịch → tăng nguy cơ barotrauma và phù phổi.",
            "ECMO + chống đông toàn thân → tăng nguy cơ xuất huyết; cần cân bằng với thủ thuật khác.",
        ],
        "follow_up": "Đánh giá lại PaO₂/FiO₂, Pplat, driving pressure sau mỗi điều chỉnh lớn; rà soát hằng ngày khả năng giảm FiO₂/PEEP, cai prone và cai máy.",
        "related_calculators": ["ARDSNet tidal volume", "PEEP/FiO₂ table", "ABG interpreter", "BMI/PBW calculator"],
        "related_protocols": ["ARDSNet protocol", "ARDS prone positioning checklist"],
        "has_protocol": True,
        "protocol_links": ["pages/04_📋_Protocols.py"],
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
        "key_points": [
            "Phân nhóm warm/cold, wet/dry để định hướng chiến lược (giảm sung huyết vs tăng tưới máu).",
            "Lợi tiểu quai IV là nền; tăng liều/nhắc lại hoặc phối hợp thiazide-like nếu kháng lợi tiểu.",
            "Vasodilator dùng khi HA đủ (thường SBP >100–110 mmHg); inotrope/vasopressor khi giảm tưới máu/sốc tim.",
            "Theo dõi sát nước tiểu, cân nặng, điện giải, creatinine và đáp ứng lâm sàng; điều chỉnh mỗi 6–12h.",
        ],
        "evidence_level": "Moderate-High (ESC HF 2023; ACC/AHA/HFSA 2022–2024)",
        "recommendation_strength": "Strong",
        "red_flags": [
            "Huyết áp tụt, lạnh đầu chi, tiểu ít, lactate tăng → nghi sốc tim, cần ICU/inotrope sớm.",
            "Khó thở khi nghỉ, phù phổi cấp, SpO₂ thấp dù đã oxy; cần thông khí hỗ trợ (NIV/NKQ).",
            "Natri rất thấp, K+ rối loạn nặng, toan chuyển hóa, suy đa cơ quan.",
            "Đau ngực gợi ý ACS, sốc tim sau MI; cần can thiệp mạch vành khẩn.",
        ],
        "monitoring": [
            "Dấu hiệu sung huyết (phù, tĩnh mạch cổ, ran phổi) và tưới máu (HA, lạnh đầu chi, lactate).",
            "Nước tiểu giờ, cân nặng hàng ngày; điện giải (Na/K), creatinine mỗi 12–24h.",
            "HA và nhịp tim liên tục nếu dùng vasodilator/inotrope/vasopressor.",
            "ECG, men tim khi nghi ACS; siêu âm tim tại giường nếu có để đánh giá chức năng và huyết động.",
        ],
        "special_populations": [
            "Người già/suy thận: giảm liều lợi tiểu/inotrope; theo dõi điện giải và creatinine sát.",
            "HATT thấp (borderline): hạn chế vasodilator, ưu tiên chỉnh thể tích và inotrope nếu giảm tưới máu.",
            "HFpEF vs HFrEF: chiến lược giảm sung huyết tương tự nhưng tối ưu điều trị nền khác nhau sau ổn định.",
        ],
        "interactions": [
            "NSAID làm giảm hiệu quả lợi tiểu và nặng thêm suy thận; nên tránh.",
            "ACEi/ARB/MRA + lợi tiểu quai có thể gây tụt HA, AKI, tăng K+; cần titrate thận trọng.",
            "Inotrope (dobutamine, milrinone) + thuốc loạn nhịp/thuốc kéo dài QT → tăng nguy cơ loạn nhịp.",
        ],
        "follow_up": "Sau ổn định đợt cấp, chuyển sang tối ưu điều trị nền (ARNI/ACEi/ARB, β-blocker, MRA, SGLT2i) và hẹn tái khám sớm (1–2 tuần) để chỉnh liều.",
        "related_calculators": ["eGFR (CKD-EPI)", "CrCl (Cockcroft-Gault)", "BNP/NT-proBNP interpret"],
        "related_protocols": ["Acute Heart Failure protocol", "(đề xuất) Diuretic escalation checklist"],
        "has_protocol": True,
        "protocol_links": ["pages/04_📋_Protocols.py"],
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
        "key_points": [
            "Nội trú: ưu tiên insulin (basal-bolus hoặc basal + correction); tránh khởi thuốc uống mới.",
            "Mục tiêu đường huyết nội trú đa số 140–180 mg/dL; mục tiêu chặt hơn chỉ nếu an toàn.",
            "Dừng SGLT2i khi nhập viện/phẫu thuật; thận trọng metformin khi eGFR thấp hoặc dùng cản quang.",
            "Ngoại trú: ưu tiên SGLT2i/GLP-1 RA nếu có ASCVD/CKD/HF/béo phì; cá thể hóa HbA1c.",
        ],
        "evidence_level": "Moderate-High (ADA 2025; AACE/ACE)",
        "recommendation_strength": "Strong",
        "red_flags": [
            "Nghi DKA/HHS: đa niệu, khát nhiều, mệt, thở Kussmaul, ketone cao, toan máu, osmolarity cao.",
            "Hạ đường huyết nặng (ý thức xấu, co giật) hoặc lặp lại nhiều lần.",
            "eGFR giảm nhanh, lactate tăng ở bệnh nhân đang dùng metformin (nghi toan lactic).",
        ],
        "monitoring": [
            "Đường huyết trước bữa và trước ngủ (4–7 lần/ngày) cho nội trú dùng insulin.",
            "HbA1c mỗi 3 tháng nếu chưa đạt mục tiêu hoặc thay đổi điều trị; mỗi 6 tháng nếu ổn.",
            "Creatinine/eGFR ít nhất 6–12 tháng/lần; thường xuyên hơn nếu CKD hoặc dùng SGLT2i/Metformin.",
        ],
        "special_populations": [
            "Người già, suy thận: giảm liều insulin khởi đầu, tránh hạ đường huyết; chỉnh liều metformin/SGLT2i theo eGFR.",
            "HF/ASCVD: ưu tiên SGLT2i/GLP-1 RA có lợi tim mạch; tránh TZD nếu HF.",
            "Béo phì: GLP-1 RA và SGLT2i hỗ trợ giảm cân; hạn chế sulfonylurea nếu có thể.",
        ],
        "interactions": [
            "β-blocker có thể che dấu triệu chứng hạ đường huyết (trừ vã mồ hôi).",
            "Steroid toàn thân làm tăng đường huyết; cần điều chỉnh liều insulin phù hợp.",
            "Thuốc lợi tiểu, ACEi/ARB + SGLT2i: tăng nguy cơ mất nước/hạ HA, nhất là người già.",
        ],
        "follow_up": "Nội trú: điều chỉnh insulin mỗi 1–2 ngày dựa trên profile đường huyết. Ngoại trú: tái khám 3 tháng đầu để tinh chỉnh phác đồ; sau đó 3–6 tháng một lần tùy kiểm soát.",
        "related_calculators": ["CrCl (Cockcroft-Gault)", "eGFR", "BMI"],
        "related_protocols": ["Inpatient glycemic control protocol", "(đề xuất) Outpatient T2DM escalation pathway"],
        "has_protocol": True,
        "protocol_links": ["pages/04_📋_Protocols.py"],
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
        "key_points": [
            "Nhận diện sớm: nhiễm khuẩn + SOFA ≥2; shock = sepsis + lactate ≥2 và cần vận mạch để MAP ≥65.",
            "Kháng sinh phổ rộng trong 1 giờ đầu; cấy máu trước kháng sinh nếu không trì hoãn.",
            "Dịch ban đầu 30 mL/kg crystalloid; đánh giá đáp ứng, tránh quá tải dịch.",
            "Norepinephrine là vận mạch đầu tay; thêm vasopressin/epinephrine nếu MAP chưa đạt.",
            "De-escalation sau 48–72h khi có kết quả cấy, rút ngắn thời gian dùng phù hợp.",
        ],
        "evidence_level": "Moderate-High (SSC 2021/2024)",
        "recommendation_strength": "Strong",
        "red_flags": [
            "MAP <65, lactate tăng hoặc không giảm sau bù dịch ban đầu.",
            "Suy hô hấp cần oxy dòng cao/NIV hoặc đặt NKQ, PaO2/FiO2 giảm nhanh.",
            "Thiểu niệu <0.5 mL/kg/h, tăng creatinine nhanh, toan chuyển hóa nặng.",
            "Giảm ý thức, dấu hiệu giảm tưới máu ngoại vi, tím đầu chi.",
        ],
        "monitoring": [
            "MAP, mạch, SpO2 liên tục; đo lactate ban đầu và lặp lại (2–4h) nếu cao.",
            "Nước tiểu giờ; cân bằng dịch; creatinine/electrolytes 6–12h.",
            "Theo dõi đáp ứng dịch: lâm sàng, lactate, siêu âm TM chủ dưới, passive leg raise nếu có.",
            "Nếu dùng vận mạch: đặt đường trung tâm/động mạch khi có thể; theo dõi ngoại vi sát.",
        ],
        "special_populations": [
            "Suy tim/CKD: bù dịch thận trọng, đánh giá quá tải; dùng vận mạch sớm hơn nếu cần.",
            "Sản phụ/già yếu: liều dịch thấp hơn, theo dõi quá tải và HA tư thế.",
            "Suy gan: chú ý lactate có thể cao nền; đánh giá tưới máu lâm sàng và nước tiểu.",
        ],
        "interactions": [
            "Aminoglycoside + loop/vancomycin: tăng nguy cơ độc thận, cần TDM và chỉnh liều theo CrCl.",
            "Linezolid + SSRI: nguy cơ serotonin syndrome; cân nhắc đổi thuốc hoặc theo dõi sát.",
            "Macrolide/quinolone: kéo dài QTc, thận trọng nếu có thuốc kéo dài QT khác.",
        ],
        "follow_up": "Đánh giá lại sau 3–6h (lactate, MAP, tưới máu), sau 24–48h xem xét de-escalation kháng sinh; rà soát nguồn nhiễm và thời gian điều trị.",
        "related_calculators": ["SOFA", "qSOFA", "APACHE II", "SAPS II", "CrCl (Cockcroft-Gault)", "eGFR"],
        "related_protocols": ["Sepsis 1-Hour Bundle"],
        "has_protocol": True,
        "protocol_links": ["pages/04_📋_Protocols.py"],
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
        "key_points": [
            "Xác định nhanh nguyên nhân (pre-/intra-/post-renal); ngừng nephrotoxin, tối ưu tưới máu.",
            "Đánh giá thể tích: bù dịch nếu prerenal; tránh quá tải; theo dõi nước tiểu, cân nặng.",
            "Chỉnh liều thuốc theo CrCl (Cockcroft-Gault); tránh tích lũy, nhất là kháng sinh/thuốc độc thận.",
            "Stage 3 hoặc quá tải dịch/toan/k tăng/refractory: cân nhắc RRT sớm; hội chẩn thận/ICU.",
        ],
        "evidence_level": "Moderate (KDIGO 2012; cập nhật 2024 tham khảo)",
        "recommendation_strength": "Moderate",
        "red_flags": [
            "Nước tiểu <0.3–0.5 mL/kg/h kéo dài >12h hoặc vô niệu.",
            "Tăng K+ >6.0 mmol/L, toan chuyển hóa pH <7.1, quá tải dịch gây giảm oxy.",
            "Creatinine tăng nhanh, triệu chứng ure huyết (lú lẫn, viêm màng ngoài tim, xuất huyết).",
            "Thiểu niệu không đáp ứng bù dịch, nghi tắc nghẽn nhưng chưa loại trừ.",
        ],
        "monitoring": [
            "Lượng nước tiểu giờ, cân nặng hàng ngày, dấu hiệu quá tải dịch.",
            "Điện giải, pH, creatinine mỗi 6–24h tùy mức độ; lactate nếu sốc.",
            "Thuốc độc thận (aminoglycoside, vancomycin, amphotericin B, NSAID, cản quang): tránh/giảm liều, TDM nếu có.",
        ],
        "special_populations": [
            "Người già/suy tim/suy gan: dễ quá tải dịch; bù dịch thận trọng, dùng siêu âm TM chủ nếu có.",
            "CKD nền: điều chỉnh liều sớm, theo dõi K+/creatinine sát; tránh kép nephrotoxin.",
            "Obese: tính CrCl theo công thức hiệu chỉnh cân nặng; thận trọng liều aminoglycoside/vancomycin.",
        ],
        "interactions": [
            "RAASi/ARB + NSAID + lợi tiểu (triple whammy) → AKI.",
            "Aminoglycoside + vancomycin/loop → tăng độc thận; cần TDM/chỉnh liều.",
            "Cản quang iod: cần đánh giá nguy cơ; bù dịch trước-sau, cân nhắc tránh nếu không bắt buộc.",
        ],
        "follow_up": "Đánh giá đáp ứng sau 6–24h (nước tiểu, K+, pH, creatinine); sau ổn định, tái khám chức năng thận 1–2 tuần và rà soát thuốc độc thận.",
        "related_calculators": ["KDIGO AKI", "RIFLE", "AKIN", "eGFR (CKD-EPI)", "CrCl (Cockcroft-Gault)", "FENa"],
        "related_protocols": ["(đề xuất) AKI management checklist", "(đề xuất) Drug dosing in AKI"],
        "has_protocol": True,
        "protocol_links": ["pages/04_📋_Protocols.py"],
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


def _extract_first_h1(markdown_text: str, fallback: str) -> str:
    for line in markdown_text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def _extract_meta_value(markdown_text: str, label: str) -> str | None:
    """
    Extract value from markdown meta lines like:
    > **Cập nhật:** Tháng 12/2025
    """
    pattern = rf"^>\s*\*\*{re.escape(label)}\*\*:\s*(.+?)\s*$"
    for line in markdown_text.splitlines():
        m = re.match(pattern, line.strip())
        if m:
            return m.group(1).strip()
    return None


def _extract_guidelines(markdown_text: str) -> list[str]:
    raw = _extract_meta_value(markdown_text, "Tài liệu tham khảo chính")
    if not raw:
        return []
    # Split on commas/semicolons while being tolerant of bracketed refs.
    parts = re.split(r"\s*[,;]\s*", raw)
    cleaned: list[str] = []
    for p in parts:
        p2 = p.strip()
        if not p2:
            continue
        cleaned.append(p2)
    return cleaned[:8]


def _extract_summary_items(markdown_text: str) -> list[str]:
    """
    Best-effort extraction:
    - Prefer first 3 bullet points under '## Tóm tắt'
    - Fallback to first 2 non-empty lines after that heading
    """
    lines = markdown_text.splitlines()
    start_idx = None
    for i, line in enumerate(lines):
        if line.strip().lower() == "## tóm tắt":
            start_idx = i + 1
            break
    if start_idx is None:
        return []

    bullets: list[str] = []
    paras: list[str] = []
    for line in lines[start_idx:]:
        s = line.strip()
        if s.startswith("## "):
            break
        if not s or s == "---":
            continue
        if s.startswith("- "):
            bullets.append(s[2:].strip())
        else:
            # Avoid meta quote lines
            if not s.startswith(">"):
                paras.append(s)

    if bullets:
        return bullets[:3]
    return paras[:2]


def _infer_specialty_from_filename_and_title(filename: str, title: str) -> str:
    hay = f"{filename} {title}".lower()
    if any(k in hay for k in ["xo-gan", "xuat-huyet-do-gian-tinh-mach", "tang-ap-luc-tinh-mach-cua", "co-truong", "sbp", "viem-gan", "gan"]):
        return "Tiêu hóa / Gan mật"
    if any(k in hay for k in ["dot-quy", "xuat-huyet-nao", "ich", "ais", "tia", "than-kinh"]):
        return "Thần kinh / Cấp cứu"
    if any(k in hay for k in ["copd", "hen", "phe-quan", "ho-hap"]):
        return "Hô hấp"
    if any(k in hay for k in ["suy-tim", "tang-huyet-ap", "acs", "nvaf", "van-tim", "tim-mach", "benh-mach-vanh", "hcm", "pericarditis", "myocarditis", "aortic"]):
        return "Tim mạch"
    if any(k in hay for k in ["aki", "suy-than", "than"]):
        return "Thận / Hồi sức"
    if any(k in hay for k in ["sepsis", "nhiem-khuan"]):
        return "Hồi sức / Nhiễm khuẩn"
    return "Nội khoa"


@st.cache_data(show_spinner=False)
def get_articles_from_content() -> list[dict]:
    """Auto-discover all markdown articles from content/articles/."""
    if not CONTENT_ARTICLES_DIR.exists():
        return []

    articles: list[dict] = []
    for path in sorted(CONTENT_ARTICLES_DIR.glob("*.md")):
        try:
            content = path.read_text(encoding="utf-8")
        except Exception:
            continue

        title = _extract_first_h1(content, fallback=path.stem)
        last_reviewed = _extract_meta_value(content, "Cập nhật") or ""
        specialty = _extract_meta_value(content, "Chuyên khoa") or _infer_specialty_from_filename_and_title(path.stem, title)
        guidelines = _extract_guidelines(content)
        summary = _extract_summary_items(content)
        
        # Check for protocol mapping
        article_id = path.stem
        protocol_info = get_protocol_for_article(article_id)
        has_protocol_mapping = protocol_info is not None
        
        # Get related protocols from metadata if exists
        related_protocols_meta = _extract_meta_value(content, "related_protocols")
        related_protocols = []
        if related_protocols_meta and isinstance(related_protocols_meta, str):
            # Parse comma-separated string
            related_protocols = [p.strip() for p in related_protocols_meta.split(",") if p.strip()]
        
        # If mapping exists, add protocol display name to related_protocols
        protocol_links = []
        if has_protocol_mapping and protocol_info:
            protocol_display = protocol_info.get("protocol_display", "")
            if protocol_display and protocol_display not in related_protocols:
                related_protocols.insert(0, protocol_display)
            # Store protocol info for deep linking
            protocol_links.append({
                "page": protocol_info.get("specialty_selector", ""),
                "protocol": protocol_info.get("protocol_display", ""),
                "function": protocol_info.get("protocol_function", "")
            })

        articles.append(
            {
                "id": article_id,
                "title": title,
                "specialty": specialty,
                "keywords": [],
                "path": path,
                "last_reviewed": last_reviewed,
                "guidelines": guidelines,
                "summary": summary,
                # Optional fields used by UI
                "key_points": [],
                "red_flags": [],
                "monitoring": [],
                "special_populations": [],
                "interactions": [],
                "follow_up": "",
                "related_calculators": [],
                "related_protocols": related_protocols,
                "has_protocol": has_protocol_mapping,
                "protocol_links": protocol_links,
                "protocol_info": protocol_info,  # Store full protocol info
            }
        )

    return articles


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


def markdown_to_safe_html(text: str) -> str:
    """
    Convert markdown syntax cơ bản thành HTML an toàn.
    Xử lý: **bold**, *italic*, \< escape sequences, và escape HTML nguy hiểm.
    """
    if not text:
        return ""
    
    # Thay thế markdown escape sequences trước (ví dụ: \< thành <)
    text = text.replace(r'\<', '<').replace(r'\>', '>')
    
    # Convert markdown syntax thành HTML TRƯỚC KHI escape
    # **bold** -> <strong>bold</strong>
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # *italic* -> <em>italic</em> (chỉ khi không phải **)
    text = re.sub(r'(?<!\*)\*([^*]+?)\*(?!\*)', r'<em>\1</em>', text)
    
    # Escape HTML để tránh XSS, nhưng giữ lại các HTML tags an toàn đã tạo
    # Bảo vệ các tags an toàn trước khi escape
    text = text.replace('<strong>', '___STRONG_OPEN___').replace('</strong>', '___STRONG_CLOSE___')
    text = text.replace('<em>', '___EM_OPEN___').replace('</em>', '___EM_CLOSE___')
    
    # Escape HTML
    text = html.escape(text)
    
    # Khôi phục các tags an toàn
    text = text.replace('___STRONG_OPEN___', '<strong>').replace('___STRONG_CLOSE___', '</strong>')
    text = text.replace('___EM_OPEN___', '<em>').replace('___EM_CLOSE___', '</em>')
    
    return text


def render_article_card(article: dict, index: int):
    """Hiển thị thẻ bài viết với thiết kế đẹp và khoa học."""
    specialty = article["specialty"]
    
    # Xử lý các text items: convert markdown thành HTML an toàn
    safe_summary_items = [markdown_to_safe_html(item) for item in article.get("summary", [])]
    safe_key_points = [markdown_to_safe_html(item) for item in article.get("key_points", [])]
    safe_red_flags = [markdown_to_safe_html(item) for item in article.get("red_flags", [])]
    safe_monitoring = [markdown_to_safe_html(item) for item in article.get("monitoring", [])]
    safe_special_pops = [markdown_to_safe_html(item) for item in article.get("special_populations", [])]
    safe_interactions = [markdown_to_safe_html(item) for item in article.get("interactions", [])]
    safe_follow_up = markdown_to_safe_html(article.get("follow_up", "") or "")
    evidence_level = article.get("evidence_level")
    recommendation_strength = article.get("recommendation_strength")
    protocol_links = article.get("protocol_links", [])
    has_protocol = article.get("has_protocol", False)

    gradient, border_color = get_specialty_color(specialty)
    
    # Tính toán reading time
    content = load_article_content(article["path"])
    reading_time = estimate_reading_time(content) if content else 0
    
    # Tạo card HTML với thiết kế đẹp - tối ưu mobile
    # Sanitize ID để đảm bảo an toàn cho HTML ID attribute
    safe_id = "".join(c if c.isalnum() or c in ('_', '-') else '_' for c in str(article['id']))
    card_id = f"article_card_{safe_id}"
    
    card_html = f"""
    <div id="{card_id}" style="max-width: 980px; margin: 0 auto 24px auto;">
      <div class="article-card" style="
          background: white;
          border-radius: 16px;
          padding: 0;
          box-shadow: 0 2px 8px rgba(0,0,0,0.06);
          transition: all 0.25s ease;
          border-left: 4px solid {border_color};
          overflow: hidden;
        "
        onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 10px 30px rgba(15,23,42,0.12)';"
        onmouseout="this.style.transform='translateY(0)';this.style.boxShadow='0 2px 8px rgba(0,0,0,0.06)';"
      >
        <!-- Header với gradient -->
        <div class="article-card-header" style="
            background: {gradient};
            padding: 18px 22px;
            color: white;
        ">
            <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 8px; width: 100%;">
                <h3 class="article-card-title" style="margin: 0; font-size: 1.3rem; font-weight: 600; color: white; line-height: 1.4; flex: 1;">
                    {html.escape(article['title'])}
                </h3>
                <span class="article-card-specialty" style="
                    background: rgba(255,255,255,0.2);
                    padding: 4px 12px;
                    border-radius: 12px;
                    font-size: 0.85rem;
                    white-space: nowrap;
                    margin-left: 12px;
                ">{html.escape(specialty)}</span>
            </div>
            <div class="article-card-meta" style="display: flex; gap: 16px; flex-wrap: wrap; font-size: 0.85rem; opacity: 0.95;">
                <span>🔄 {html.escape(str(article.get('last_reviewed', 'N/A')))}</span>
                {f'<span>⏱️ {reading_time} phút đọc</span>' if reading_time > 0 else ''}
                <span>📑 {len(article.get('guidelines', []))} guideline</span>
                {f'<span class="article-badge" style="background: rgba(255,255,255,0.2); padding: 4px 10px; border-radius: 12px;">LoE: {html.escape(evidence_level)}</span>' if evidence_level else ''}
                {f'<span class="article-badge" style="background: rgba(255,255,255,0.2); padding: 4px 10px; border-radius: 12px;">SoR: {html.escape(recommendation_strength)}</span>' if recommendation_strength else ''}
            </div>
        </div>
        
        <!-- Body -->
        <div class="article-card-body" style="padding: 18px 22px 20px 22px;">
            <!-- Key Points -->
            {""
            if not safe_key_points else
            '<div class="article-content-box" style="margin-bottom: 16px; background: #f3f6ff; border: 1px solid #dfe7ff; border-radius: 10px; padding: 12px 14px;">'
            + '<div class="article-content-box-title" style="font-weight: 600; color: #2a3f6b; margin-bottom: 8px;">⭐ Key points</div>'
            + '<ul style="margin: 0; padding-left: 18px; color: #455a64; line-height: 1.55;">'
            + "".join([f'<li style="margin-bottom: 6px;">{kp}</li>' for kp in safe_key_points[:4]])
            + '</ul>'
            + '</div>'
            }

            <!-- Guidelines badges -->
            <div style="margin-bottom: 16px;">
                {" ".join([f'<span class="article-badge" style="background: #e3f2fd; color: #1976d2; padding: 4px 10px; border-radius: 12px; font-size: 0.8rem; margin-right: 6px; margin-bottom: 6px; display: inline-block;">{html.escape(g)}</span>' for g in article.get('guidelines', [])[:3]])}
            </div>
            
            <!-- Summary points -->
            <div style="margin-bottom: 16px;">
                <strong style="color: #424242; font-size: 0.95rem;">💡 Điểm cần nhớ:</strong>
                <ul style="margin: 8px 0 0 0; padding-left: 20px; color: #616161; font-size: 0.9rem; line-height: 1.6;">
                    {"".join([f'<li style="margin-bottom: 6px;">{item}</li>' for item in safe_summary_items[:3]])}
                </ul>
            </div>

            <!-- Red flags -->
            {"" if not safe_red_flags else
            '<div class="article-content-box" style="margin-bottom: 16px; background: #fff5f5; border: 1px solid #ffcdd2; border-radius: 10px; padding: 12px 14px;">'
            + '<div class="article-content-box-title" style="font-weight: 600; color: #c62828; margin-bottom: 6px;">⚠️ Red flags / Khi cần escalation</div>'
            + '<ul style="margin: 0; padding-left: 18px; color: #b71c1c; line-height: 1.5;">'
            + "".join([f'<li style="margin-bottom: 6px;">{rf}</li>' for rf in safe_red_flags[:4]])
            + '</ul>'
            + '</div>'
            }
            
            <!-- Keywords tags -->
            {f'''
            <div style="margin-bottom: 16px;">
                <div style="display: flex; flex-wrap: wrap; gap: 6px;">
                    {" ".join([f'<span class="article-tag" style="background: #f5f5f5; color: #616161; padding: 4px 10px; border-radius: 12px; font-size: 0.75rem; border: 1px solid #e0e0e0;">{html.escape(k)}</span>' for k in article.get('keywords', [])[:6]])}
                </div>
            </div>
            ''' if article.get('keywords') else ''}

            <!-- Monitoring / Follow-up -->
            {"" if not (safe_monitoring or safe_follow_up) else
            '<div class="article-content-box" style="margin-bottom: 16px; background: #f9fbe7; border: 1px solid #e6ee9c; border-radius: 10px; padding: 12px 14px;">'
            + ('' if not safe_monitoring else '<div class="article-content-box-title" style="font-weight:600;color:#827717;margin-bottom:6px;">🩺 Monitoring</div>'
               + '<ul style="margin:0; padding-left:18px; color:#6d4c41; line-height:1.5;">'
               + "".join([f'<li style="margin-bottom:6px;">{m}</li>' for m in safe_monitoring[:4]])
               + '</ul>')
            + ('' if not safe_follow_up else f'<div style="margin-top:8px; color:#6d4c41;"><strong>📆 Follow-up:</strong> {safe_follow_up}</div>')
            + '</div>'
            }

            <!-- Special populations -->
            {"" if not safe_special_pops else
            '<div class="article-content-box" style="margin-bottom: 16px; background: #eef7ff; border: 1px solid #c5e0ff; border-radius: 10px; padding: 12px 14px;">'
            + '<div class="article-content-box-title" style="font-weight:600;color:#0d47a1;margin-bottom:6px;">👪 Đối tượng đặc biệt</div>'
            + '<ul style="margin:0; padding-left:18px; color:#37474f; line-height:1.5;">'
            + "".join([f'<li style="margin-bottom:6px;">{sp}</li>' for sp in safe_special_pops[:4]])
            + '</ul>'
            + '</div>'
            }

            <!-- Interactions -->
            {"" if not safe_interactions else
            '<div class="article-content-box" style="margin-bottom: 16px; background: #f3e5f5; border: 1px solid #e1bee7; border-radius: 10px; padding: 12px 14px;">'
            + '<div class="article-content-box-title" style="font-weight:600;color:#6a1b9a;margin-bottom:6px;">🔗 Tương tác thuốc quan trọng</div>'
            + '<ul style="margin:0; padding-left:18px; color:#4a148c; line-height:1.5;">'
            + "".join([f'<li style="margin-bottom:6px;">{it}</li>' for it in safe_interactions[:4]])
            + '</ul>'
            + '</div>'
            }
            
            <!-- Related links -->
            <div style="
                background: #f8f9fa;
                padding: 12px 16px;
                border-radius: 8px;
                margin-top: 16px;
            ">
                <div style="font-size: 0.85rem; color: #616161;">
                    {f'<div style="margin-bottom: 8px;"><strong>📊 Calculators:</strong> {html.escape(", ".join(article.get("related_calculators", [])[:3]))}</div>' if article.get('related_calculators') else ''}
                    {f'<div><strong>📋 Protocols:</strong> {html.escape(", ".join(article.get("related_protocols", [])[:2]))}</div>' if article.get('related_protocols') else ''}
                </div>
            </div>
        </div>
      </div>
    </div>
    """

    # Dùng markdown trực tiếp để card co giãn tự nhiên theo nội dung (thân thiện mobile hơn)
    st.markdown(card_html, unsafe_allow_html=True)
    
    # Protocol deep link button (Streamlit button)
    protocol_info = article.get("protocol_info")
    if protocol_info:
        col1, col2 = st.columns([1, 3])
        with col1:
            if st.button(
                "📋 Mở Protocol",
                key=f"protocol_btn_{article['id']}_{index}",
                use_container_width=True,
                help=f"Mở protocol: {html.escape(protocol_info.get('protocol_display', ''))}",
                type="primary"
            ):
                # Store protocol selection in session state for Protocols page
                st.session_state['protocol_specialty'] = protocol_info.get("specialty_selector")
                st.session_state['protocol_to_open'] = protocol_info.get("protocol_display")
                st.session_state['protocol_function'] = protocol_info.get("protocol_function")
                st.switch_page("pages/04_📋_Protocols.py")
        with col2:
            st.caption(f"💡 Có protocol tương ứng: **{html.escape(protocol_info.get('protocol_display', ''))}**")
    
    # Score links
    try:
        from components.score_links_from_content import render_score_links_from_article
        render_score_links_from_article(article['id'])
    except ImportError:
        pass
    
    # Streamlit expander cho nội dung đầy đủ - với class cho mobile optimization
    expand_key = f"article_expand_{article['id']}_{index}"
    expanded = st.session_state.get(f"expand_article_{article['id']}", False)
    with st.expander(f"📖 Đọc toàn bộ: {html.escape(article['title'])}", expanded=expanded, key=expand_key):
        st.markdown('<div class="article-expander-content">', unsafe_allow_html=True)
        if content:
            st.markdown(content)
        else:
            st.warning(f"Không tìm thấy nội dung tại {html.escape(article['path'].name)}.")


def filter_articles(articles: list[dict], search: str, specialties: list, selected_keywords: list):
    """Lọc bài viết theo từ khóa, chuyên khoa và keywords."""
    search_lower = search.lower()
    filtered = []
    
    for article in articles:
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

    # Inject mobile-optimized CSS
    st.markdown("""
    <style>
    /* Mobile-first responsive styles */
    @media (max-width: 768px) {
        /* Hero section mobile */
        .article-hero {
            padding: 1rem 1.25rem !important;
            flex-direction: column !important;
            align-items: flex-start !important;
        }
        .article-hero > div {
            max-width: 100% !important;
            min-width: 100% !important;
        }
        .article-hero h2 {
            font-size: 1.35rem !important;
            line-height: 1.3 !important;
        }
        .article-hero p {
            font-size: 0.875rem !important;
            line-height: 1.5 !important;
        }
        
        /* Card mobile optimization */
        .article-card {
            margin-bottom: 20px !important;
            border-radius: 12px !important;
        }
        .article-card-header {
            padding: 16px 18px !important;
            flex-direction: column !important;
            align-items: flex-start !important;
        }
        .article-card-title {
            font-size: 1.15rem !important;
            line-height: 1.4 !important;
            margin-bottom: 8px !important;
            width: 100% !important;
        }
        .article-card-specialty {
            margin-left: 0 !important;
            margin-top: 8px !important;
            font-size: 0.8rem !important;
            padding: 5px 10px !important;
        }
        .article-card-meta {
            flex-direction: column !important;
            gap: 8px !important;
            font-size: 0.8rem !important;
        }
        .article-card-body {
            padding: 16px 18px !important;
        }
        
        /* Typography mobile */
        .article-card-body ul,
        .article-card-body ol {
            padding-left: 20px !important;
            line-height: 1.6 !important;
        }
        .article-card-body li {
            margin-bottom: 8px !important;
            font-size: 0.9rem !important;
        }
        .article-card-body strong {
            font-size: 0.95rem !important;
        }
        
        /* Content boxes mobile */
        .article-content-box {
            padding: 10px 12px !important;
            margin-bottom: 12px !important;
            border-radius: 8px !important;
        }
        .article-content-box-title {
            font-size: 0.9rem !important;
            margin-bottom: 6px !important;
        }
        
        /* Badges and tags mobile */
        .article-badge,
        .article-tag {
            font-size: 0.75rem !important;
            padding: 5px 9px !important;
            margin-right: 4px !important;
            margin-bottom: 6px !important;
        }
        
        /* Filter chips mobile */
        .filter-chip {
            font-size: 0.8rem !important;
            padding: 6px 10px !important;
            margin-right: 6px !important;
            margin-bottom: 6px !important;
        }
        
        /* Reading content mobile */
        .article-expander-content {
            font-size: 1rem !important;
            line-height: 1.7 !important;
        }
        .article-expander-content p {
            margin-bottom: 1rem !important;
        }
        .article-expander-content h1,
        .article-expander-content h2,
        .article-expander-content h3 {
            font-size: 1.25rem !important;
            line-height: 1.4 !important;
            margin-top: 1.5rem !important;
            margin-bottom: 0.75rem !important;
        }
        
        /* Touch targets - minimum 44x44px */
        button[data-testid*="protocol_btn"],
        button[data-testid*="stButton"] {
            min-height: 44px !important;
            padding: 10px 16px !important;
        }
        
        /* Statistics dashboard mobile */
        .stMetric {
            padding: 0.75rem !important;
        }
    }
    
    /* Tablet optimization (768px - 1024px) */
    @media (min-width: 769px) and (max-width: 1024px) {
        .article-card {
            max-width: 95% !important;
        }
        .article-card-header {
            padding: 18px 20px !important;
        }
        .article-card-body {
            padding: 18px 20px !important;
        }
    }
    
    /* Ensure good reading experience on all devices */
    .article-expander-content {
        max-width: 100%;
        word-wrap: break-word;
        overflow-wrap: break-word;
    }
    </style>
    """, unsafe_allow_html=True)

    # Hero section giống các trang kiến thức y khoa hiện đại - với class cho CSS
    st.markdown(
        """
        <div class="article-hero" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    padding: 1.5rem 2rem;
                    border-radius: 16px;
                    margin-bottom: 1.5rem;
                    color: white;
                    display: flex;
                    flex-wrap: wrap;
                    justify-content: space-between;
                    align-items: center;">
            <div style="max-width: 60%; min-width: 260px;">
                <div style="font-size: 0.9rem; opacity: 0.9; margin-bottom: 0.25rem;">📚 Chuyên sâu theo guideline</div>
                <h2 style="margin: 0 0 0.5rem 0; font-size: 1.6rem; font-weight: 600;">Kiến thức chuyên sâu, bám sát thực hành lâm sàng</h2>
                <p style="margin: 0; font-size: 0.9rem; opacity: 0.95;">
                    Tổng hợp các chủ đề tim mạch, hồi sức, hô hấp, nội tiết, gan mật, nhiễm khuẩn...
                    kèm điểm cần nhớ, guideline gốc và liên kết trực tiếp tới calculators/protocols trong ứng dụng.
                </p>
            </div>
            <div style="min-width: 200px; margin-top: 1rem;">
                <div style="display: flex; flex-direction: column; gap: 6px; font-size: 0.85rem;">
                    <span style="background: rgba(255,255,255,0.12); padding: 6px 10px; border-radius: 999px;">
                        🔍 Tìm nhanh theo <strong>chuyên khoa</strong> và <strong>từ khóa</strong> ở sidebar
                    </span>
                    <span style="background: rgba(255,255,255,0.12); padding: 6px 10px; border-radius: 999px;">
                        📊 Mỗi bài gắn với <strong>calculators</strong> và <strong>protocols</strong> liên quan
                    </span>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    articles = get_articles_from_content()
    if not articles:
        st.warning(
            f"Chưa tìm thấy bài viết trong `{CONTENT_ARTICLES_DIR}`. "
            "Hãy đảm bảo các bài markdown nằm trong `content/articles/`."
        )

    # Statistics Dashboard
    render_statistics_dashboard(articles)
    
    st.markdown("---")
    
    # Sidebar filters
    with st.sidebar:
        st.header("📚 Bài viết chuyên sâu")
        st.caption("Sub-module **Bài viết chuyên sâu** – thuộc nhóm *🩺 Chẩn đoán & Bài viết*.")
        
        with st.expander("Liên kết trong nhóm Chẩn đoán & Bài viết", expanded=False):
            col1, col2 = st.columns(2)
            with col1:
                if st.button("🩺 Chẩn đoán phân biệt", use_container_width=True, key="sidebar_btn_diagnosis"):
                    st.switch_page("pages/06_🩺_Diagnosis.py")
            with col2:
                if st.button("📊 Thang điểm & Scores", use_container_width=True, key="sidebar_btn_scores"):
                    st.switch_page("pages/01_📊_Scores.py")
        
        st.markdown("---")
        st.header("🔎 Tìm kiếm & Lọc")
        
        search = st.text_input(
            "🔍 Tìm kiếm",
            value="",
            placeholder="VD: tăng huyết áp, PPI, ICU, sepsis...",
            help="Tìm kiếm theo tiêu đề, chuyên khoa, từ khóa hoặc nội dung"
        )
        
        st.markdown("---")
        
        st.subheader("🩺 Chuyên khoa")
        all_specialties = sorted({article["specialty"] for article in articles})
        selected_specialties = st.multiselect(
            "Chọn chuyên khoa",
            options=all_specialties,
            default=[],
            help="Chọn một hoặc nhiều chuyên khoa để lọc"
        )
        
        st.markdown("---")
        
        st.subheader("🏷️ Từ khóa phổ biến")
        all_keywords = sorted(set([k for a in articles for k in a.get("keywords", [])]))
        # Hiển thị top keywords
        keyword_counts = Counter([k for a in articles for k in a.get("keywords", [])])
        top_keywords = [k for k, _ in keyword_counts.most_common(15)]
        
        selected_keywords = st.multiselect(
            "Chọn từ khóa",
            options=top_keywords,
            default=[],
            help="Chọn từ khóa để lọc bài viết liên quan"
        )
        
        st.markdown("---")
        
        render_info_box(
            """
            **📚 Thông tin:**
            
            - Nội dung cập nhật theo guideline quốc tế mới nhất
            - ESC/ESH, ACC/AHA, ACG/AGA, ASHP, IDSA, SSC...
            - Tích hợp với calculators và protocols trong app
            - Được mở rộng và cập nhật định kỳ
            """,
            type="info",
            title="Thông tin Module"
        )
        
        st.markdown("---")
        
        # Quick stats
        st.caption(f"**Tổng số bài viết:** {len(articles)}")
        st.caption(f"**Chuyên khoa:** {len(all_specialties)}")
    
    # Check for deep link from Protocols page
    article_to_open = st.session_state.get('article_to_open')
    if article_to_open:
        # Find and highlight the article
        target_article = next((a for a in articles if a['id'] == article_to_open), None)
        if target_article:
            render_info_box(
                f"**Đang hiển thị bài viết:** {html.escape(target_article['title'])}",
                type="success",
                title="📚 Bài viết",
                icon="📚"
            )
            st.caption("💡 Bài viết sẽ tự động mở rộng bên dưới")
            # Auto-expand the article
            st.session_state[f"expand_article_{article_to_open}"] = True
        else:
            render_info_box(
                f"Không tìm thấy bài viết với ID: `{html.escape(article_to_open)}`",
                type="warning"
            )
        # Clear deep link state
        if 'article_to_open' in st.session_state:
            del st.session_state['article_to_open']
    
    # Filter articles
    filtered = filter_articles(articles, search, selected_specialties, selected_keywords)
    
    # Display results
    if not filtered:
        render_info_box(
            """
            **Không tìm thấy bài viết phù hợp.**
            
            Thử:
            - Xóa bộ lọc chuyên khoa
            - Thay đổi từ khóa tìm kiếm
            - Chọn từ khóa khác
            """,
            type="warning"
        )
    else:
        # Tóm tắt nhanh bộ lọc đang dùng giống thanh "active filters" trên các trang y khoa hiện đại
        active_filters = []
        if search:
            active_filters.append(f"🔍 \"{search}\"")
        if selected_specialties:
            active_filters.append("🩺 " + ", ".join(selected_specialties))
        if selected_keywords:
            active_filters.append("🏷️ " + ", ".join(selected_keywords))

        render_info_box(
            f"Tìm thấy **{len(filtered)}** bài viết phù hợp",
            type="success",
            title="Kết quả tìm kiếm"
        )
        if active_filters:
            chips = " ".join(
                f"<span class='filter-chip' style='background:#eef2ff;color:#3730a3;padding:4px 10px;border-radius:999px;font-size:0.8rem;margin-right:6px;margin-bottom:4px;display:inline-block;'>{html.escape(f)}</span>"
                for f in active_filters
            )
            st.markdown(
                f"<div style='margin-top:0.35rem;margin-bottom:0.75rem;'>{chips}</div>",
                unsafe_allow_html=True,
            )
        st.markdown("---")

        # Tabs để xem theo chuyên ngành hoặc danh sách phẳng
        tab_overview, tab_list = st.tabs(["🩺 Theo chuyên ngành", "📄 Danh sách đầy đủ"])

        # Nhóm bài viết theo chuyên ngành
        grouped_by_specialty = defaultdict(list)
        for article in filtered:
            grouped_by_specialty[article["specialty"]].append(article)
        specs = sorted(grouped_by_specialty.keys())

        with tab_overview:
            # Tóm tắt chuyên ngành đang có trong kết quả
            st.markdown("### 🩺 Chuyên ngành trong kết quả")
            spec_badges = " ".join(
                f"<span style='background:#e3f2fd;color:#1976d2;padding:4px 10px;border-radius:12px;font-size:0.8rem;margin-right:6px;margin-bottom:6px;display:inline-block;'>{html.escape(spec)} ({len(grouped_by_specialty[spec])})</span>"
                for spec in specs
            )
            st.markdown(spec_badges, unsafe_allow_html=True)
            st.markdown("---")

            # Hiển thị lần lượt từng chuyên ngành
            for spec in specs:
                st.markdown(f"### 🩺 {html.escape(spec)}")
                st.caption(f"{len(grouped_by_specialty[spec])} bài viết chuyên sâu")

                for idx, article in enumerate(grouped_by_specialty[spec]):
                    render_article_card(article, idx)

                st.markdown("---")

        with tab_list:
            st.markdown("### 📄 Tất cả bài viết (theo bộ lọc hiện tại)")
            st.caption("Danh sách phẳng, sắp xếp theo thứ tự trong cấu hình ARTICLES.")
            for idx, article in enumerate(filtered):
                render_article_card(article, idx)
                st.markdown("---")
    
    render_standard_footer(disclaimer=True)


if __name__ == "__main__":
    main()
