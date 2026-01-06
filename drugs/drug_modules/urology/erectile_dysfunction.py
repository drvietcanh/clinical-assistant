"""
Urology Drugs - Erectile Dysfunction
"""
from typing import Dict, Any


ERECTILE_DYSFUNCTION_DRUGS: Dict[str, Dict[str, Any]] = {
        "Avanafil": {
            "group": "Urology - PDE-5 Inhibitor (Erectile Dysfunction)",
            "vietnamese_name": "Avanafil, Stendra",
            "administration": ["PO"],
            "indications": [
                "Rối loạn cương dương (erectile dysfunction - ED)",
                "Cải thiện khả năng đạt và duy trì cương dương"
            ],
            "contraindications": [
                "Dị ứng avanafil",
                "Dùng nitrate (nitroglycerin, isosorbide) - CHỐNG CHỈ ĐỊNH tuyệt đối",
                "Dùng riociguat - CHỐNG CHỈ ĐỊNH tuyệt đối",
                "Bệnh tim nặng không ổn định",
                "Đột quỵ hoặc nhồi máu cơ tim gần đây (<6 tháng)",
                "Hạ huyết áp nặng (<90/50 mmHg)",
                "Mất thị lực một mắt do NAION (Non-Arteritic Anterior Ischemic Optic Neuropathy)"
            ],
            "dosage": {
                "adult_ed": "100mg PO x 1 lần/ngày (30 phút trước hoạt động tình dục)",
                "adult_ed_max": "200mg PO x 1 lần/ngày nếu cần",
                "adult_ed_min": "50mg PO x 1 lần/ngày nếu không dung nạp",
                "max_frequency": "Tối đa 1 lần/ngày",
                "notes": "Avanafil là PDE-5 inhibitor mới nhất, tác dụng nhanh (15-30 phút), thời gian bán thải ngắn (3-5 giờ). Ít tác dụng phụ hơn sildenafil và tadalafil. CHỐNG CHỈ ĐỊNH tuyệt đối với nitrate."
            },
            "renal_adjustment": {
                "normal": "Không đổi",
                "30_60": "Thận trọng, giảm liều 50mg",
                "under_30": "Thận trọng, giảm liều 50mg"
            },
            "side_effects": [
                "Đau đầu - phổ biến",
                "Đỏ bừng mặt (flushing) - phổ biến",
                "Nghẹt mũi - phổ biến",
                "Rối loạn tiêu hóa (buồn nôn, khó tiêu)",
                "Chóng mặt",
                "Đau lưng, đau cơ - ít hơn tadalafil",
                "Rối loạn thị giác (nhìn mờ, thay đổi màu sắc) - hiếm",
                "Mất thị lực đột ngột (NAION) - hiếm nhưng nguy hiểm",
                "Mất thính lực đột ngột - hiếm nhưng nguy hiểm"
            ],
            "interactions": [
                "Nitrate (nitroglycerin, isosorbide): CHỐNG CHỈ ĐỊNH tuyệt đối - nguy cơ hạ huyết áp nặng, tử vong",
                "Riociguat: CHỐNG CHỈ ĐỊNH tuyệt đối - nguy cơ hạ huyết áp nặng",
                "Alpha-blockers (tamsulosin, doxazosin): tăng nguy cơ hạ huyết áp",
                "CYP3A4 inhibitors (ketoconazole, clarithromycin): tăng nồng độ avanafil",
                "Ritonavir, saquinavir: tăng nồng độ avanafil",
                "Erythromycin, clarithromycin: tăng nồng độ avanafil"
            ],
            "pregnancy": "Không áp dụng (chỉ dùng cho nam giới)",
            "mechanism_of_action": "Avanafil là phosphodiesterase-5 (PDE-5) inhibitor. Ức chế enzyme PDE-5, làm tăng nồng độ cGMP (cyclic guanosine monophosphate) trong cơ trơn mạch máu dương vật. cGMP gây giãn mạch, tăng lưu lượng máu đến dương vật, và gây cương dương. Avanafil KHÔNG gây cương dương tự phát, cần kích thích tình dục để có tác dụng. Avanafil là PDE-5 inhibitor mới nhất, tác dụng nhanh (15-30 phút), thời gian bán thải ngắn (3-5 giờ), ít tác dụng phụ hơn sildenafil và tadalafil. ĐẶC ĐIỂM: (1) Tác dụng nhanh (15-30 phút), thời gian bán thải ngắn (3-5 giờ), (2) Ít tác dụng phụ hơn sildenafil và tadalafil, (3) CHỐNG CHỈ ĐỊNH tuyệt đối với nitrate (nguy cơ hạ huyết áp nặng, tử vong), (4) Nguy cơ rối loạn thị giác và mất thị lực (NAION), (5) Tương tác với nhiều thuốc (alpha-blockers, protease inhibitors, macrolides).",
            "monitoring": [
                "Đáp ứng lâm sàng (khả năng đạt và duy trì cương dương)",
                "Huyết áp - QUAN TRỌNG (đặc biệt khi dùng với thuốc hạ huyết áp)",
                "Dấu hiệu mất thị lực đột ngột (NAION) - NGỪNG NGAY nếu có",
                "Dấu hiệu mất thính lực đột ngột - NGỪNG NGAY nếu có",
                "Dấu hiệu rối loạn thị giác (nhìn mờ, thay đổi màu sắc)"
            ],
            "precautions": [
                "CHỐNG CHỈ ĐỊNH tuyệt đối với nitrate (nitroglycerin, isosorbide) - nguy cơ hạ huyết áp nặng, tử vong",
                "CHỐNG CHỈ ĐỊNH tuyệt đối với riociguat - nguy cơ hạ huyết áp nặng",
                "NGỪNG NGAY nếu có mất thị lực hoặc mất thính lực đột ngột",
                "Thận trọng ở bệnh nhân bệnh tim nặng không ổn định",
                "Thận trọng khi dùng với alpha-blockers (tăng nguy cơ hạ huyết áp)",
                "Thận trọng khi dùng với thuốc hạ huyết áp khác",
                "Thận trọng ở bệnh nhân có tiền sử NAION (nguy cơ tái phát)",
                "Thận trọng ở bệnh nhân có tiền sử mất thính lực đột ngột",
                "Không dùng quá 1 lần/ngày",
                "Cần kích thích tình dục để có tác dụng (không gây cương dương tự phát)"
            ],
            "pharmacokinetics": {
                "half_life": "3-5 giờ (ngắn hơn sildenafil và tadalafil)",
                "onset": "15-30 phút (nhanh hơn sildenafil)",
                "duration": "4-6 giờ",
                "protein_binding": "99%",
                "metabolism": "Gan (CYP3A4)",
                "clearance": "Gan, thận (bài tiết qua nước tiểu và phân)"
            },
            "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
            "black_box_warnings": "CHỐNG CHỈ ĐỊNH tuyệt đối với nitrate (nitroglycerin, isosorbide) và riociguat. Nguy cơ hạ huyết áp nặng, tử vong. Nguy cơ mất thị lực đột ngột (NAION) và mất thính lực đột ngột.",
            "drug_interactions": {
                "major": [
                    {
                        "drug": "Nitrate (Nitroglycerin, Isosorbide Mononitrate, Isosorbide Dinitrate)",
                        "mechanism": "Cả hai đều gây giãn mạch, tác dụng cộng dồn",
                        "effect": "Hạ huyết áp nặng, ngất, đột quỵ, nhồi máu cơ tim, tử vong",
                        "management": "CHỐNG CHỈ ĐỊNH tuyệt đối. KHÔNG được dùng đồng thời. Cách xa ít nhất 24 giờ."
                    },
                    {
                        "drug": "Riociguat",
                        "mechanism": "Cả hai đều gây giãn mạch, tác dụng cộng dồn",
                        "effect": "Hạ huyết áp nặng, ngất, đột quỵ, nhồi máu cơ tim, tử vong",
                        "management": "CHỐNG CHỈ ĐỊNH tuyệt đối. KHÔNG được dùng đồng thời."
                    },
                    {
                        "drug": "Alpha-blockers (Tamsulosin, Doxazosin, Terazosin)",
                        "mechanism": "Cả hai đều gây giãn mạch, tác dụng cộng dồn",
                        "effect": "Tăng nguy cơ hạ huyết áp nặng, ngất",
                        "management": "TRÁNH DÙNG CHUNG. Nếu bắt buộc, dùng liều thấp nhất và theo dõi huyết áp sát. Cách xa ít nhất 4-6 giờ."
                    }
                ],
                "moderate": [
                    {
                        "drug": "CYP3A4 Inhibitors (Ketoconazole, Clarithromycin, Itraconazole, Ritonavir, Saquinavir)",
                        "mechanism": "Ức chế CYP3A4, tăng nồng độ avanafil",
                        "effect": "Tăng nồng độ avanafil, tăng nguy cơ tác dụng phụ",
                        "management": "Giảm liều avanafil 50mg. Theo dõi tác dụng phụ."
                    },
                    {
                        "drug": "Macrolides (Erythromycin, Clarithromycin)",
                        "mechanism": "Ức chế CYP3A4, tăng nồng độ avanafil",
                        "effect": "Tăng nồng độ avanafil, tăng nguy cơ tác dụng phụ",
                        "management": "Thận trọng. Có thể cần giảm liều avanafil."
                    }
                ],
                "minor": []
            },
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng avanafil",
                    "Dùng nitrate (nitroglycerin, isosorbide) - CHỐNG CHỈ ĐỊNH tuyệt đối",
                    "Dùng riociguat - CHỐNG CHỈ ĐỊNH tuyệt đối",
                    "Bệnh tim nặng không ổn định - CHỐNG CHỈ ĐỊNH",
                    "Đột quỵ hoặc nhồi máu cơ tim gần đây (<6 tháng) - CHỐNG CHỈ ĐỊNH",
                    "Hạ huyết áp nặng (<90/50 mmHg) - CHỐNG CHỈ ĐỊNH",
                    "Mất thị lực một mắt do NAION - CHỐNG CHỈ ĐỊNH"
                ],
                "tương_đối": [
                    "Bệnh tim ổn định - thận trọng",
                    "Tăng huyết áp - thận trọng",
                    "Suy gan trung bình đến nặng - giảm liều",
                    "Suy thận trung bình đến nặng - giảm liều",
                    "Dùng với alpha-blockers - tăng nguy cơ hạ huyết áp"
                ]
            },
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng avanafil",
                    "Dùng nitrate (nitroglycerin, isosorbide) - CHỐNG CHỈ ĐỊNH tuyệt đối",
                    "Dùng riociguat - CHỐNG CHỈ ĐỊNH tuyệt đối",
                    "Bệnh tim nặng không ổn định - CHỐNG CHỈ ĐỊNH",
                    "Đột quỵ hoặc nhồi máu cơ tim gần đây (<6 tháng) - CHỐNG CHỈ ĐỊNH",
                    "Hạ huyết áp nặng (<90/50 mmHg) - CHỐNG CHỈ ĐỊNH",
                    "Mất thị lực một mắt do NAION - CHỐNG CHỈ ĐỊNH"
                ],
                "tương_đối": [
                    "Bệnh tim ổn định - thận trọng",
                    "Tăng huyết áp - thận trọng",
                    "Suy gan trung bình đến nặng - giảm liều",
                    "Suy thận trung bình đến nặng - giảm liều",
                    "Dùng với alpha-blockers - tăng nguy cơ hạ huyết áp"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "Không áp dụng",
                "pregnancy_details": "Avanafil chỉ dùng cho nam giới. Không áp dụng cho phụ nữ có thai.",
                "lactation": {
                    "safety": "Not Applicable",
                    "details": "Avanafil chỉ dùng cho nam giới. Không áp dụng cho phụ nữ cho con bú.",
                    "recommendation": "Không áp dụng."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh liều",
                "moderate": "Thận trọng. Chuyển hóa qua gan có thể giảm, tăng nồng độ avanafil. Giảm liều 50mg.",
                "severe": "Giảm liều 50mg. Chuyển hóa qua gan giảm đáng kể, tăng nồng độ avanafil và nguy cơ tác dụng phụ.",
                "notes": "Avanafil chuyển hóa qua gan (CYP3A4). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và nguy cơ tác dụng phụ. Cần giảm liều ở suy gan trung bình đến nặng."
            },
            "overdose_management": {
                "symptoms": [
                    "Hạ huyết áp nặng",
                    "Ngất (syncope)",
                    "Đau đầu nặng",
                    "Đỏ bừng mặt nặng",
                    "Rối loạn thị giác nặng"
                ],
                "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
                "treatment": [
                    "Ngừng ngay avanafil",
                    "Nếu hạ huyết áp nặng:",
                    "  - Nằm ngửa, nâng chân",
                    "  - Truyền dịch nếu cần",
                    "  - Theo dõi huyết áp liên tục",
                    "  - Có thể cần thuốc tăng huyết áp (phenylephrine, norepinephrine) nếu nặng",
                    "Theo dõi: Huyết áp, nhịp tim, dấu hiệu sinh tồn, thị giác, thính giác"
                ],
                "monitoring": "Theo dõi huyết áp, nhịp tim, dấu hiệu sinh tồn, thị giác, thính giác cho đến khi hồi phục."
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ. Nếu hạ huyết áp nặng: nằm ngửa, nâng chân, truyền dịch, thuốc tăng huyết áp (phenylephrine, norepinephrine) nếu cần. Half-life 3-5 giờ nên tác dụng sẽ giảm sau vài giờ."
            },
            "administration_instructions": {
                "oral": {
                    "with_food": "Uống với hoặc không thức ăn. Có thể uống không thức ăn.",
                    "timing": "100mg PO x 1 lần/ngày (30 phút trước hoạt động tình dục). Tối đa 1 lần/ngày.",
                    "notes": "QUAN TRỌNG: 1) CHỐNG CHỈ ĐỊNH tuyệt đối với nitrate và riociguat, 2) Tác dụng nhanh (15-30 phút), 3) NGỪNG NGAY nếu có mất thị lực hoặc mất thính lực đột ngột, 4) Cần kích thích tình dục để có tác dụng, 5) Không dùng quá 1 lần/ngày."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Avanafil (Stendra)",
                    "AUA Guidelines - Management of Erectile Dysfunction",
                    "UpToDate - Avanafil: Drug Information",
                    "Medscape - Avanafil Drug Reference"
                ],
                "last_updated": "2025-02-18",
                "evidence_level": "A - Dựa trên FDA drug labels, AUA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
            },
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": [],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Blood pressure - CRITICAL (contraindicated with nitrates)", "Signs of vision/hearing loss (NAION, sudden hearing loss)", "Cardiovascular status"]
            },
            "guideline_tags": [
                "AUA Guidelines - Erectile Dysfunction",
                "EAU Guidelines - Erectile Dysfunction",
                "FDA Black Box Warning - PDE-5 Inhibitors and Nitrates",
                "FDA Drug Safety Communication - PDE-5 Inhibitors and Vision Loss"
            ]
        },

        "Sildenafil": {
            "group": "Urology - PDE-5 Inhibitor (Erectile Dysfunction)",
            "vietnamese_name": "Sildenafil, Viagra",
            "administration": ["PO"],
            "indications": [
                "Rối loạn cương dương (erectile dysfunction - ED)",
                "Tăng áp động mạch phổi (pulmonary arterial hypertension - PAH) - liều khác"
            ],
            "contraindications": [
                "Dị ứng sildenafil",
                "Dùng với nitrate (nitroglycerin, isosorbide) - CHỐNG CHỈ ĐỊNH (nguy cơ hạ huyết áp nặng, tử vong)",
                "Dùng với riociguat - CHỐNG CHỈ ĐỊNH",
                "Bệnh tim nặng không ổn định (nhồi máu cơ tim gần đây, đau thắt ngực không ổn định)",
                "Hạ huyết áp nặng",
                "Đột quỵ gần đây",
                "Mất thị lực một mắt do NAION (Non-Arteritic Anterior Ischemic Optic Neuropathy)"
            ],
            "dosage": {
                "adult_ed": "50mg PO 30-60 phút trước hoạt động tình dục (tối đa 100mg, tối thiểu 25mg)",
                "adult_ed_daily": "25mg PO x 1 lần/ngày (dùng liên tục)",
                "adult_pah": "20mg PO x 3 lần/ngày (chỉ cho PAH)",
                "notes": "Tác dụng kéo dài 4-6 giờ. Không dùng quá 1 lần/ngày. TRÁNH DÙNG với nitrate (cách xa ít nhất 24 giờ)."
            },
            "renal_adjustment": {
                "normal": "Không đổi",
                "30_60": "Không cần điều chỉnh đáng kể",
                "under_30": "Giảm liều 25mg (ED), thận trọng (PAH)"
            },
            "side_effects": [
                "Đau đầu (phổ biến)",
                "Đỏ mặt (flushing)",
                "Nghẹt mũi",
                "Rối loạn tiêu hóa (khó tiêu, buồn nôn)",
                "Chóng mặt",
                "Rối loạn thị giác (nhìn mờ, nhìn xanh/vàng, nhạy cảm ánh sáng)",
                "Mất thị lực đột ngột (NAION) - hiếm nhưng nguy hiểm",
                "Mất thính lực đột ngột - hiếm",
                "Hạ huyết áp",
                "Đau cơ, đau lưng"
            ],
            "interactions": [
                "Nitrate: hạ huyết áp nguy hiểm - CHỐNG CHỈ ĐỊNH",
                "Alpha-blockers: tăng nguy cơ hạ huyết áp",
                "Ritonavir, saquinavir: tăng nồng độ sildenafil",
                "Erythromycin, clarithromycin: tăng nồng độ sildenafil"
            ],
            "pregnancy": "Không áp dụng (chỉ dùng cho nam giới)",
            "mechanism_of_action": "Sildenafil là phosphodiesterase-5 (PDE-5) inhibitor. Ức chế enzyme PDE-5, làm tăng nồng độ cGMP (cyclic guanosine monophosphate) trong cơ trơn mạch máu dương vật. cGMP gây giãn mạch, tăng lưu lượng máu đến dương vật, và gây cương dương. Sildenafil KHÔNG gây cương dương tự phát, cần kích thích tình dục để có tác dụng. ĐẶC ĐIỂM: (1) Tác dụng nhanh (30-60 phút), kéo dài 4-6 giờ, (2) CHỐNG CHỈ ĐỊNH với nitrate (nguy cơ hạ huyết áp nặng, tử vong), (3) Nguy cơ rối loạn thị giác và mất thị lực (NAION), (4) Tương tác với nhiều thuốc (alpha-blockers, protease inhibitors, macrolides).",
            "monitoring": [
                "Dấu hiệu hạ huyết áp (chóng mặt, ngất)",
                "Dấu hiệu rối loạn thị giác (nhìn mờ, nhìn xanh/vàng)",
                "Dấu hiệu mất thị lực đột ngột (NAION) - NGỪNG NGAY nếu có",
                "Dấu hiệu mất thính lực đột ngột - NGỪNG NGAY nếu có",
                "Dấu hiệu đau ngực, khó thở (bệnh tim)"
            ],
            "precautions": [
                "CHỐNG CHỈ ĐỊNH với nitrate (nitroglycerin, isosorbide) - nguy cơ hạ huyết áp nặng, tử vong",
                "Cách xa nitrate ít nhất 24 giờ",
                "CHỐNG CHỈ ĐỊNH với riociguat",
                "Thận trọng ở bệnh nhân bệnh tim (nhồi máu cơ tim gần đây, đau thắt ngực không ổn định)",
                "Thận trọng khi dùng với alpha-blockers (tăng nguy cơ hạ huyết áp)",
                "NGỪNG NGAY nếu có mất thị lực đột ngột (NAION) hoặc mất thính lực đột ngột",
                "Không dùng quá 1 lần/ngày",
                "Tác dụng kéo dài 4-6 giờ - không dùng lại trong thời gian này"
            ],
            "pharmacokinetics": {
                "half_life": "3-5 giờ",
                "onset": "30-60 phút",
                "duration": "4-6 giờ",
                "protein_binding": "96%",
                "metabolism": "Gan (CYP3A4, CYP2C9)",
                "clearance": "Gan, thận (bài tiết qua nước tiểu và phân)"
            },
            "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
            "black_box_warnings": "CHỐNG CHỈ ĐỊNH với nitrate (nitroglycerin, isosorbide) - nguy cơ hạ huyết áp nặng, có thể tử vong. Cách xa nitrate ít nhất 24 giờ. Nguy cơ mất thị lực đột ngột (NAION) và mất thính lực đột ngột. NGỪNG NGAY nếu có.",
            "drug_interactions": {
                "major": [
                    {
                        "drug": "Nitrate (Nitroglycerin, Isosorbide mononitrate, Isosorbide dinitrate)",
                        "mechanism": "Cả hai đều tăng cGMP, tác dụng cộng dồn giãn mạch",
                        "effect": "Hạ huyết áp nặng, có thể tử vong",
                        "management": "CHỐNG CHỈ ĐỊNH tuyệt đối. KHÔNG được dùng đồng thời. Cách xa ít nhất 24 giờ."
                    },
                    {
                        "drug": "Riociguat",
                        "mechanism": "Cả hai đều tăng cGMP, tác dụng cộng dồn",
                        "effect": "Hạ huyết áp nặng, có thể tử vong",
                        "management": "CHỐNG CHỈ ĐỊNH tuyệt đối. KHÔNG được dùng đồng thời."
                    },
                    {
                        "drug": "Alpha-blockers (Tamsulosin, Doxazosin, Terazosin)",
                        "mechanism": "Cả hai đều gây giãn mạch, tác dụng cộng dồn",
                        "effect": "Tăng nguy cơ hạ huyết áp nặng, ngất",
                        "management": "TRÁNH DÙNG CHUNG. Nếu bắt buộc, dùng liều thấp nhất và theo dõi huyết áp sát. Cách xa ít nhất 4-6 giờ."
                    }
                ],
                "moderate": [
                    {
                        "drug": "Protease Inhibitors (Ritonavir, Saquinavir, Indinavir)",
                        "mechanism": "Ức chế CYP3A4, tăng nồng độ sildenafil",
                        "effect": "Tăng nồng độ sildenafil, tăng nguy cơ tác dụng phụ",
                        "management": "Giảm liều sildenafil 25mg mỗi 48 giờ (với ritonavir). Theo dõi tác dụng phụ."
                    },
                    {
                        "drug": "Macrolides (Erythromycin, Clarithromycin)",
                        "mechanism": "Ức chế CYP3A4, tăng nồng độ sildenafil",
                        "effect": "Tăng nồng độ sildenafil, tăng nguy cơ tác dụng phụ",
                        "management": "Thận trọng. Có thể cần giảm liều sildenafil."
                    }
                ],
                "minor": []
            },
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng sildenafil",
                    "Dùng với nitrate (nitroglycerin, isosorbide) - CHỐNG CHỈ ĐỊNH (nguy cơ hạ huyết áp nặng, tử vong)",
                    "Dùng với riociguat - CHỐNG CHỈ ĐỊNH",
                    "Bệnh tim nặng không ổn định (nhồi máu cơ tim gần đây, đau thắt ngực không ổn định) - CHỐNG CHỈ ĐỊNH",
                    "Hạ huyết áp nặng - CHỐNG CHỈ ĐỊNH"
                ],
                "tương_đối": [
                    "Bệnh tim ổn định - thận trọng, đánh giá nguy cơ tim mạch trước khi dùng",
                    "Đột quỵ gần đây - thận trọng",
                    "Mất thị lực một mắt do NAION - thận trọng (nguy cơ mất thị lực mắt còn lại)",
                    "Dùng với alpha-blockers - tăng nguy cơ hạ huyết áp",
                    "Suy gan/thận nặng - giảm liều"
                ]
            },
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng sildenafil",
                    "Dùng với nitrate (nitroglycerin, isosorbide) - CHỐNG CHỈ ĐỊNH (nguy cơ hạ huyết áp nặng, tử vong)",
                    "Dùng với riociguat - CHỐNG CHỈ ĐỊNH",
                    "Bệnh tim nặng không ổn định (nhồi máu cơ tim gần đây, đau thắt ngực không ổn định) - CHỐNG CHỈ ĐỊNH",
                    "Hạ huyết áp nặng - CHỐNG CHỈ ĐỊNH"
                ],
                "tương_đối": [
                    "Bệnh tim ổn định - thận trọng, đánh giá nguy cơ tim mạch trước khi dùng",
                    "Đột quỵ gần đây - thận trọng",
                    "Mất thị lực một mắt do NAION - thận trọng (nguy cơ mất thị lực mắt còn lại)",
                    "Dùng với alpha-blockers - tăng nguy cơ hạ huyết áp",
                    "Suy gan/thận nặng - giảm liều"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "Không áp dụng",
                "pregnancy_details": "Sildenafil chỉ dùng cho nam giới. Không áp dụng cho phụ nữ có thai.",
                "lactation": {
                    "safety": "Không áp dụng",
                    "details": "Sildenafil chỉ dùng cho nam giới. Không áp dụng cho phụ nữ cho con bú.",
                    "recommendation": "Không áp dụng."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh liều",
                "moderate": "Thận trọng. Chuyển hóa qua gan có thể giảm, tăng nồng độ sildenafil. Giảm liều 25mg.",
                "severe": "Giảm liều 25mg. Chuyển hóa qua gan giảm đáng kể, tăng nồng độ sildenafil và nguy cơ tác dụng phụ.",
                "notes": "Sildenafil chuyển hóa qua gan (CYP3A4, CYP2C9). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và nguy cơ tác dụng phụ. Cần giảm liều ở suy gan trung bình đến nặng."
            },
            "overdose_management": {
                "symptoms": [
                    "Hạ huyết áp nặng, ngất",
                    "Đau đầu nặng",
                    "Rối loạn thị giác nặng",
                    "Đau ngực",
                    "Nhịp tim nhanh"
                ],
                "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
                "treatment": [
                    "Nếu hạ huyết áp nặng:",
                    "  - Nằm đầu thấp, nâng chân",
                    "  - Truyền dịch (NS, LR) nếu cần",
                    "  - Thuốc vận mạch (norepinephrine, phenylephrine) nếu cần",
                    "Theo dõi: Huyết áp, nhịp tim, ECG liên tục",
                    "Hỗ trợ hô hấp nếu cần"
                ],
                "monitoring": "Theo dõi huyết áp, nhịp tim, ECG liên tục cho đến khi hồi phục."
            },
            "reversal_agents": None,
            "administration_instructions": {
                "oral": {
                    "with_food": "Uống với hoặc không thức ăn. Có thể uống không thức ăn nếu cần.",
                    "timing": "50mg PO 30-60 phút trước hoạt động tình dục (tối đa 100mg, tối thiểu 25mg). Hoặc 25mg PO x 1 lần/ngày (dùng liên tục). Không dùng quá 1 lần/ngày.",
                    "notes": "QUAN TRỌNG: 1) CHỐNG CHỈ ĐỊNH với nitrate (cách xa ít nhất 24 giờ), 2) Tác dụng kéo dài 4-6 giờ, 3) NGỪNG NGAY nếu có mất thị lực hoặc mất thính lực đột ngột, 4) Thận trọng khi dùng với alpha-blockers."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Sildenafil (Viagra)",
                    "AUA Guidelines - Erectile Dysfunction",
                    "UpToDate - Sildenafil: Drug Information",
                    "Medscape - Sildenafil Drug Reference"
                ],
                "last_updated": "2025-02-18",
                "evidence_level": "A - Dựa trên FDA drug labels, AUA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
            },
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["Sudden vision loss (NAION) - CRITICAL", "Sudden hearing loss - CRITICAL", "Hypotension (especially with nitrates) - CRITICAL"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Signs of hypotension (dizziness, syncope) - CRITICAL", "Signs of vision changes (blurred vision, color vision changes)", "Signs of sudden vision loss (NAION) - CRITICAL (STOP immediately)", "Signs of sudden hearing loss - CRITICAL (STOP immediately)", "Signs of chest pain, dyspnea (cardiac disease)"]
            },
            "guideline_tags": [
                "AUA Guidelines - Erectile Dysfunction",
                "FDA Black Box Warning - Sildenafil and Nitrates (Contraindicated)",
                "FDA Black Box Warning - Sildenafil and Vision Loss (NAION)",
                "FDA Black Box Warning - Sildenafil and Hearing Loss"
            ],
            "reversal_agents": {
                "available": False,
                "agents": [],
            },
        },

        "Tadalafil": {
            "group": "Urology - PDE-5 Inhibitor (Erectile Dysfunction/BPH)",
            "vietnamese_name": "Tadalafil, Cialis",
            "administration": ["PO"],
            "indications": [
                "Rối loạn cương dương (erectile dysfunction - ED)",
                "Phì đại tuyến tiền liệt lành tính (BPH) - giảm triệu chứng",
                "ED + BPH (kết hợp)"
            ],
            "contraindications": [
                "Dị ứng tadalafil",
                "Dùng với nitrate (nitroglycerin, isosorbide) - CHỐNG CHỈ ĐỊNH (nguy cơ hạ huyết áp nặng, tử vong)",
                "Dùng với riociguat - CHỐNG CHỈ ĐỊNH",
                "Bệnh tim nặng không ổn định (nhồi máu cơ tim gần đây, đau thắt ngực không ổn định)",
                "Hạ huyết áp nặng",
                "Đột quỵ gần đây",
                "Mất thị lực một mắt do NAION"
            ],
            "dosage": {
                "adult_ed": "10mg PO 30 phút trước hoạt động tình dục (tối đa 20mg, tối thiểu 5mg)",
                "adult_ed_daily": "2.5-5mg PO x 1 lần/ngày (dùng liên tục)",
                "adult_bph": "5mg PO x 1 lần/ngày",
                "adult_ed_bph": "5mg PO x 1 lần/ngày (kết hợp ED + BPH)",
                "notes": "Tác dụng kéo dài 36 giờ (dài hơn sildenafil). Không dùng quá 1 lần/ngày. TRÁNH DÙNG với nitrate (cách xa ít nhất 48 giờ)."
            },
            "renal_adjustment": {
                "normal": "Không đổi",
                "30_60": "Giảm liều 5mg (ED), 2.5mg (BPH)",
                "under_30": "CHỐNG CHỈ ĐỊNH hoặc dùng rất thận trọng, giảm liều đáng kể"
            },
            "side_effects": [
                "Đau đầu (phổ biến)",
                "Đỏ mặt (flushing)",
                "Nghẹt mũi",
                "Rối loạn tiêu hóa (khó tiêu, buồn nôn)",
                "Chóng mặt",
                "Đau lưng, đau cơ (phổ biến với tadalafil)",
                "Rối loạn thị giác (nhìn mờ, nhìn xanh/vàng)",
                "Mất thị lực đột ngột (NAION) - hiếm nhưng nguy hiểm",
                "Mất thính lực đột ngột - hiếm",
                "Hạ huyết áp"
            ],
            "interactions": [
                "Nitrate: hạ huyết áp nguy hiểm - CHỐNG CHỈ ĐỊNH",
                "Alpha-blockers: tăng nguy cơ hạ huyết áp",
                "Ritonavir, saquinavir: tăng nồng độ tadalafil",
                "Erythromycin, clarithromycin: tăng nồng độ tadalafil"
            ],
            "pregnancy": "Không áp dụng (chỉ dùng cho nam giới)",
            "mechanism_of_action": "Tadalafil là phosphodiesterase-5 (PDE-5) inhibitor. Ức chế enzyme PDE-5, làm tăng nồng độ cGMP trong cơ trơn mạch máu dương vật và tuyến tiền liệt. cGMP gây giãn mạch, tăng lưu lượng máu đến dương vật (gây cương dương) và giảm sức cản đường tiểu (cải thiện triệu chứng BPH). Tadalafil KHÔNG gây cương dương tự phát, cần kích thích tình dục để có tác dụng. ĐẶC ĐIỂM: (1) Tác dụng dài hơn sildenafil (36 giờ vs 4-6 giờ), (2) Có thể dùng cho cả ED và BPH, (3) CHỐNG CHỈ ĐỊNH với nitrate (nguy cơ hạ huyết áp nặng, tử vong), (4) Nguy cơ rối loạn thị giác và mất thị lực (NAION), (5) Đau lưng, đau cơ phổ biến hơn sildenafil.",
            "monitoring": [
                "Dấu hiệu hạ huyết áp (chóng mặt, ngất)",
                "Dấu hiệu rối loạn thị giác (nhìn mờ, nhìn xanh/vàng)",
                "Dấu hiệu mất thị lực đột ngột (NAION) - NGỪNG NGAY nếu có",
                "Dấu hiệu mất thính lực đột ngột - NGỪNG NGAY nếu có",
                "Triệu chứng BPH (nếu dùng cho BPH)",
                "Dấu hiệu đau ngực, khó thở (bệnh tim)"
            ],
            "precautions": [
                "CHỐNG CHỈ ĐỊNH với nitrate (nitroglycerin, isosorbide) - nguy cơ hạ huyết áp nặng, tử vong",
                "Cách xa nitrate ít nhất 48 giờ (dài hơn sildenafil do thời gian bán thải dài)",
                "CHỐNG CHỈ ĐỊNH với riociguat",
                "Thận trọng ở bệnh nhân bệnh tim (nhồi máu cơ tim gần đây, đau thắt ngực không ổn định)",
                "Thận trọng khi dùng với alpha-blockers (tăng nguy cơ hạ huyết áp)",
                "NGỪNG NGAY nếu có mất thị lực đột ngột (NAION) hoặc mất thính lực đột ngột",
                "Không dùng quá 1 lần/ngày",
                "Tác dụng kéo dài 36 giờ - không dùng lại trong thời gian này",
                "Đau lưng, đau cơ - phổ biến, thường tự khỏi"
            ],
            "pharmacokinetics": {
                "half_life": "17.5 giờ (rất dài)",
                "onset": "30 phút",
                "duration": "36 giờ (dài hơn sildenafil)",
                "protein_binding": "94%",
                "metabolism": "Gan (CYP3A4)",
                "clearance": "Gan, thận (bài tiết qua nước tiểu và phân)"
            },
            "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
            "black_box_warnings": "CHỐNG CHỈ ĐỊNH với nitrate (nitroglycerin, isosorbide) - nguy cơ hạ huyết áp nặng, có thể tử vong. Cách xa nitrate ít nhất 48 giờ. Nguy cơ mất thị lực đột ngột (NAION) và mất thính lực đột ngột. NGỪNG NGAY nếu có.",
            "drug_interactions": {
                "major": [
                    {
                        "drug": "Nitrate (Nitroglycerin, Isosorbide mononitrate, Isosorbide dinitrate)",
                        "mechanism": "Cả hai đều tăng cGMP, tác dụng cộng dồn giãn mạch",
                        "effect": "Hạ huyết áp nặng, có thể tử vong",
                        "management": "CHỐNG CHỈ ĐỊNH tuyệt đối. KHÔNG được dùng đồng thời. Cách xa ít nhất 48 giờ (dài hơn sildenafil do thời gian bán thải dài)."
                    },
                    {
                        "drug": "Riociguat",
                        "mechanism": "Cả hai đều tăng cGMP, tác dụng cộng dồn",
                        "effect": "Hạ huyết áp nặng, có thể tử vong",
                        "management": "CHỐNG CHỈ ĐỊNH tuyệt đối. KHÔNG được dùng đồng thời."
                    },
                    {
                        "drug": "Alpha-blockers (Tamsulosin, Doxazosin, Terazosin)",
                        "mechanism": "Cả hai đều gây giãn mạch, tác dụng cộng dồn",
                        "effect": "Tăng nguy cơ hạ huyết áp nặng, ngất",
                        "management": "TRÁNH DÙNG CHUNG. Nếu bắt buộc, dùng liều thấp nhất và theo dõi huyết áp sát. Cách xa ít nhất 4-6 giờ."
                    }
                ],
                "moderate": [
                    {
                        "drug": "Protease Inhibitors (Ritonavir, Saquinavir, Indinavir)",
                        "mechanism": "Ức chế CYP3A4, tăng nồng độ tadalafil",
                        "effect": "Tăng nồng độ tadalafil, tăng nguy cơ tác dụng phụ",
                        "management": "Giảm liều tadalafil 10mg mỗi 72 giờ (với ritonavir). Theo dõi tác dụng phụ."
                    },
                    {
                        "drug": "Macrolides (Erythromycin, Clarithromycin)",
                        "mechanism": "Ức chế CYP3A4, tăng nồng độ tadalafil",
                        "effect": "Tăng nồng độ tadalafil, tăng nguy cơ tác dụng phụ",
                        "management": "Thận trọng. Có thể cần giảm liều tadalafil."
                    }
                ],
                "minor": []
            },
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng tadalafil",
                    "Dùng với nitrate (nitroglycerin, isosorbide) - CHỐNG CHỈ ĐỊNH (nguy cơ hạ huyết áp nặng, tử vong)",
                    "Dùng với riociguat - CHỐNG CHỈ ĐỊNH",
                    "Bệnh tim nặng không ổn định (nhồi máu cơ tim gần đây, đau thắt ngực không ổn định) - CHỐNG CHỈ ĐỊNH",
                    "Hạ huyết áp nặng - CHỐNG CHỈ ĐỊNH",
                    "Suy thận nặng (CrCl <30) - CHỐNG CHỈ ĐỊNH hoặc dùng rất thận trọng"
                ],
                "tương_đối": [
                    "Bệnh tim ổn định - thận trọng, đánh giá nguy cơ tim mạch trước khi dùng",
                    "Đột quỵ gần đây - thận trọng",
                    "Mất thị lực một mắt do NAION - thận trọng (nguy cơ mất thị lực mắt còn lại)",
                    "Dùng với alpha-blockers - tăng nguy cơ hạ huyết áp",
                    "Suy gan/thận (CrCl 30-60) - giảm liều"
                ]
            },
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng tadalafil",
                    "Dùng với nitrate (nitroglycerin, isosorbide) - CHỐNG CHỈ ĐỊNH (nguy cơ hạ huyết áp nặng, tử vong)",
                    "Dùng với riociguat - CHỐNG CHỈ ĐỊNH",
                    "Bệnh tim nặng không ổn định (nhồi máu cơ tim gần đây, đau thắt ngực không ổn định) - CHỐNG CHỈ ĐỊNH",
                    "Hạ huyết áp nặng - CHỐNG CHỈ ĐỊNH",
                    "Suy thận nặng (CrCl <30) - CHỐNG CHỈ ĐỊNH hoặc dùng rất thận trọng"
                ],
                "tương_đối": [
                    "Bệnh tim ổn định - thận trọng, đánh giá nguy cơ tim mạch trước khi dùng",
                    "Đột quỵ gần đây - thận trọng",
                    "Mất thị lực một mắt do NAION - thận trọng (nguy cơ mất thị lực mắt còn lại)",
                    "Dùng với alpha-blockers - tăng nguy cơ hạ huyết áp",
                    "Suy gan/thận (CrCl 30-60) - giảm liều"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "Không áp dụng",
                "pregnancy_details": "Tadalafil chỉ dùng cho nam giới. Không áp dụng cho phụ nữ có thai.",
                "lactation": {
                    "safety": "Không áp dụng",
                    "details": "Tadalafil chỉ dùng cho nam giới. Không áp dụng cho phụ nữ cho con bú.",
                    "recommendation": "Không áp dụng."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh liều",
                "moderate": "Thận trọng. Chuyển hóa qua gan có thể giảm, tăng nồng độ tadalafil. Giảm liều 5mg.",
                "severe": "Giảm liều 5mg. Chuyển hóa qua gan giảm đáng kể, tăng nồng độ tadalafil và nguy cơ tác dụng phụ.",
                "notes": "Tadalafil chuyển hóa qua gan (CYP3A4). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và nguy cơ tác dụng phụ. Cần giảm liều ở suy gan trung bình đến nặng."
            },
            "overdose_management": {
                "symptoms": [
                    "Hạ huyết áp nặng, ngất",
                    "Đau đầu nặng",
                    "Rối loạn thị giác nặng",
                    "Đau ngực",
                    "Nhịp tim nhanh",
                    "Đau lưng, đau cơ nặng"
                ],
                "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
                "treatment": [
                    "Nếu hạ huyết áp nặng:",
                    "  - Nằm đầu thấp, nâng chân",
                    "  - Truyền dịch (NS, LR) nếu cần",
                    "  - Thuốc vận mạch (norepinephrine, phenylephrine) nếu cần",
                    "Theo dõi: Huyết áp, nhịp tim, ECG liên tục",
                    "Hỗ trợ hô hấp nếu cần"
                ],
                "monitoring": "Theo dõi huyết áp, nhịp tim, ECG liên tục cho đến khi hồi phục. Thời gian bán thải dài (17.5 giờ), cần theo dõi lâu hơn."
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ. Nếu hạ huyết áp nặng: nằm đầu thấp, truyền dịch, thuốc vận mạch (norepinephrine, phenylephrine) nếu cần. Half-life dài (17.5 giờ) nên tác dụng sẽ kéo dài."
            },
            "administration_instructions": {
                "oral": {
                    "with_food": "Uống với hoặc không thức ăn. Có thể uống không thức ăn nếu cần.",
                    "timing": "ED: 10mg PO 30 phút trước hoạt động tình dục (tối đa 20mg, tối thiểu 5mg). Hoặc 2.5-5mg PO x 1 lần/ngày (dùng liên tục). BPH: 5mg PO x 1 lần/ngày. ED+BPH: 5mg PO x 1 lần/ngày. Không dùng quá 1 lần/ngày.",
                    "notes": "QUAN TRỌNG: 1) CHỐNG CHỈ ĐỊNH với nitrate (cách xa ít nhất 48 giờ), 2) Tác dụng kéo dài 36 giờ (dài hơn sildenafil), 3) NGỪNG NGAY nếu có mất thị lực hoặc mất thính lực đột ngột, 4) Thận trọng khi dùng với alpha-blockers, 5) Đau lưng, đau cơ phổ biến."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Tadalafil (Cialis)",
                    "AUA Guidelines - Erectile Dysfunction and Benign Prostatic Hyperplasia",
                    "UpToDate - Tadalafil: Drug Information",
                    "Medscape - Tadalafil Drug Reference"
                ],
                "last_updated": "2025-02-18",
                "evidence_level": "A - Dựa trên FDA drug labels, AUA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
            },
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["Sudden vision loss (NAION) - CRITICAL", "Sudden hearing loss - CRITICAL", "Hypotension (especially with nitrates) - CRITICAL"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Signs of hypotension (dizziness, syncope) - CRITICAL", "Signs of vision changes (blurred vision, color vision changes)", "Signs of sudden vision loss (NAION) - CRITICAL (STOP immediately)", "Signs of sudden hearing loss - CRITICAL (STOP immediately)", "BPH symptoms (if used for BPH)", "Signs of chest pain, dyspnea (cardiac disease)"]
            },
            "guideline_tags": [
                "AUA Guidelines - Erectile Dysfunction",
                "AUA Guidelines - Benign Prostatic Hyperplasia",
                "FDA Black Box Warning - Tadalafil and Nitrates (Contraindicated)",
                "FDA Black Box Warning - Tadalafil and Vision Loss (NAION)",
                "FDA Black Box Warning - Tadalafil and Hearing Loss"
            ]
        },

        "Vardenafil": {
            "group": "Urology - PDE-5 Inhibitor (Erectile Dysfunction)",
            "vietnamese_name": "Vardenafil, Levitra",
            "administration": ["PO"],
            "indications": [
                "Rối loạn cương dương (erectile dysfunction - ED)"
            ],
            "contraindications": [
                "Dị ứng vardenafil",
                "Dùng với nitrate (nitroglycerin, isosorbide) - CHỐNG CHỈ ĐỊNH (nguy cơ hạ huyết áp nặng, tử vong)",
                "Dùng với riociguat - CHỐNG CHỈ ĐỊNH",
                "Bệnh tim nặng không ổn định (nhồi máu cơ tim gần đây, đau thắt ngực không ổn định)",
                "Hạ huyết áp nặng",
                "Đột quỵ gần đây",
                "Mất thị lực một mắt do NAION"
            ],
            "dosage": {
                "adult_ed": "10mg PO 30-60 phút trước hoạt động tình dục (tối đa 20mg, tối thiểu 5mg)",
                "notes": "Tác dụng kéo dài 4-5 giờ. Không dùng quá 1 lần/ngày. TRÁNH DÙNG với nitrate (cách xa ít nhất 24 giờ)."
            },
            "renal_adjustment": {
                "normal": "Không đổi",
                "30_60": "Không cần điều chỉnh đáng kể",
                "under_30": "Giảm liều 5mg"
            },
            "side_effects": [
                "Đau đầu (phổ biến)",
                "Đỏ mặt (flushing)",
                "Nghẹt mũi",
                "Rối loạn tiêu hóa (khó tiêu, buồn nôn)",
                "Chóng mặt",
                "Rối loạn thị giác (nhìn mờ, nhìn xanh/vàng, nhạy cảm ánh sáng)",
                "Mất thị lực đột ngột (NAION) - hiếm nhưng nguy hiểm",
                "Mất thính lực đột ngột - hiếm",
                "Hạ huyết áp"
            ],
            "interactions": [
                "Nitrate: hạ huyết áp nguy hiểm - CHỐNG CHỈ ĐỊNH",
                "Alpha-blockers: tăng nguy cơ hạ huyết áp",
                "Ritonavir, saquinavir: tăng nồng độ vardenafil",
                "Erythromycin, clarithromycin: tăng nồng độ vardenafil"
            ],
            "pregnancy": "Không áp dụng (chỉ dùng cho nam giới)",
            "mechanism_of_action": "Vardenafil là phosphodiesterase-5 (PDE-5) inhibitor. Ức chế enzyme PDE-5, làm tăng nồng độ cGMP (cyclic guanosine monophosphate) trong cơ trơn mạch máu dương vật. cGMP gây giãn mạch, tăng lưu lượng máu đến dương vật, và gây cương dương. Vardenafil KHÔNG gây cương dương tự phát, cần kích thích tình dục để có tác dụng. ĐẶC ĐIỂM: (1) Tác dụng nhanh (30-60 phút), kéo dài 4-5 giờ, (2) CHỐNG CHỈ ĐỊNH với nitrate (nguy cơ hạ huyết áp nặng, tử vong), (3) Nguy cơ rối loạn thị giác và mất thị lực (NAION), (4) Tương tác với nhiều thuốc (alpha-blockers, protease inhibitors, macrolides), (5) Tương tự sildenafil nhưng có thể hiệu quả hơn ở một số bệnh nhân.",
            "monitoring": [
                "Dấu hiệu hạ huyết áp (chóng mặt, ngất)",
                "Dấu hiệu rối loạn thị giác (nhìn mờ, nhìn xanh/vàng)",
                "Dấu hiệu mất thị lực đột ngột (NAION) - NGỪNG NGAY nếu có",
                "Dấu hiệu mất thính lực đột ngột - NGỪNG NGAY nếu có",
                "Dấu hiệu đau ngực, khó thở (bệnh tim)"
            ],
            "precautions": [
                "CHỐNG CHỈ ĐỊNH với nitrate (nitroglycerin, isosorbide) - nguy cơ hạ huyết áp nặng, tử vong",
                "Cách xa nitrate ít nhất 24 giờ",
                "CHỐNG CHỈ ĐỊNH với riociguat",
                "Thận trọng ở bệnh nhân bệnh tim (nhồi máu cơ tim gần đây, đau thắt ngực không ổn định)",
                "Thận trọng khi dùng với alpha-blockers (tăng nguy cơ hạ huyết áp)",
                "NGỪNG NGAY nếu có mất thị lực đột ngột (NAION) hoặc mất thính lực đột ngột",
                "Không dùng quá 1 lần/ngày",
                "Tác dụng kéo dài 4-5 giờ - không dùng lại trong thời gian này"
            ],
            "pharmacokinetics": {
                "half_life": "4-5 giờ",
                "onset": "30-60 phút",
                "duration": "4-5 giờ",
                "protein_binding": "94%",
                "metabolism": "Gan (CYP3A4, CYP3A5, CYP2C9)",
                "clearance": "Gan, thận (bài tiết qua nước tiểu và phân)"
            },
            "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
            "black_box_warnings": "CHỐNG CHỈ ĐỊNH với nitrate (nitroglycerin, isosorbide) - nguy cơ hạ huyết áp nặng, có thể tử vong. Cách xa nitrate ít nhất 24 giờ. Nguy cơ mất thị lực đột ngột (NAION) và mất thính lực đột ngột. NGỪNG NGAY nếu có.",
            "drug_interactions": {
                "major": [
                    {
                        "drug": "Nitrate (Nitroglycerin, Isosorbide mononitrate, Isosorbide dinitrate)",
                        "mechanism": "Cả hai đều tăng cGMP, tác dụng cộng dồn giãn mạch",
                        "effect": "Hạ huyết áp nặng, có thể tử vong",
                        "management": "CHỐNG CHỈ ĐỊNH tuyệt đối. KHÔNG được dùng đồng thời. Cách xa ít nhất 24 giờ."
                    },
                    {
                        "drug": "Riociguat",
                        "mechanism": "Cả hai đều tăng cGMP, tác dụng cộng dồn",
                        "effect": "Hạ huyết áp nặng, có thể tử vong",
                        "management": "CHỐNG CHỈ ĐỊNH tuyệt đối. KHÔNG được dùng đồng thời."
                    },
                    {
                        "drug": "Alpha-blockers (Tamsulosin, Doxazosin, Terazosin)",
                        "mechanism": "Cả hai đều gây giãn mạch, tác dụng cộng dồn",
                        "effect": "Tăng nguy cơ hạ huyết áp nặng, ngất",
                        "management": "TRÁNH DÙNG CHUNG. Nếu bắt buộc, dùng liều thấp nhất và theo dõi huyết áp sát. Cách xa ít nhất 4-6 giờ."
                    }
                ],
                "moderate": [
                    {
                        "drug": "Protease Inhibitors (Ritonavir, Saquinavir, Indinavir)",
                        "mechanism": "Ức chế CYP3A4, tăng nồng độ vardenafil",
                        "effect": "Tăng nồng độ vardenafil, tăng nguy cơ tác dụng phụ",
                        "management": "Giảm liều vardenafil 2.5mg mỗi 72 giờ (với ritonavir). Theo dõi tác dụng phụ."
                    },
                    {
                        "drug": "Macrolides (Erythromycin, Clarithromycin)",
                        "mechanism": "Ức chế CYP3A4, tăng nồng độ vardenafil",
                        "effect": "Tăng nồng độ vardenafil, tăng nguy cơ tác dụng phụ",
                        "management": "Thận trọng. Có thể cần giảm liều vardenafil."
                    }
                ],
                "minor": []
            },
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng vardenafil",
                    "Dùng với nitrate (nitroglycerin, isosorbide) - CHỐNG CHỈ ĐỊNH (nguy cơ hạ huyết áp nặng, tử vong)",
                    "Dùng với riociguat - CHỐNG CHỈ ĐỊNH",
                    "Bệnh tim nặng không ổn định (nhồi máu cơ tim gần đây, đau thắt ngực không ổn định) - CHỐNG CHỈ ĐỊNH",
                    "Hạ huyết áp nặng - CHỐNG CHỈ ĐỊNH"
                ],
                "tương_đối": [
                    "Bệnh tim ổn định - thận trọng, đánh giá nguy cơ tim mạch trước khi dùng",
                    "Đột quỵ gần đây - thận trọng",
                    "Mất thị lực một mắt do NAION - thận trọng (nguy cơ mất thị lực mắt còn lại)",
                    "Dùng với alpha-blockers - tăng nguy cơ hạ huyết áp",
                    "Suy gan/thận nặng - giảm liều"
                ]
            },
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng vardenafil",
                    "Dùng với nitrate (nitroglycerin, isosorbide) - CHỐNG CHỈ ĐỊNH (nguy cơ hạ huyết áp nặng, tử vong)",
                    "Dùng với riociguat - CHỐNG CHỈ ĐỊNH",
                    "Bệnh tim nặng không ổn định (nhồi máu cơ tim gần đây, đau thắt ngực không ổn định) - CHỐNG CHỈ ĐỊNH",
                    "Hạ huyết áp nặng - CHỐNG CHỈ ĐỊNH"
                ],
                "tương_đối": [
                    "Bệnh tim ổn định - thận trọng, đánh giá nguy cơ tim mạch trước khi dùng",
                    "Đột quỵ gần đây - thận trọng",
                    "Mất thị lực một mắt do NAION - thận trọng (nguy cơ mất thị lực mắt còn lại)",
                    "Dùng với alpha-blockers - tăng nguy cơ hạ huyết áp",
                    "Suy gan/thận nặng - giảm liều"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "Không áp dụng",
                "pregnancy_details": "Vardenafil chỉ dùng cho nam giới. Không áp dụng cho phụ nữ có thai.",
                "lactation": {
                    "safety": "Không áp dụng",
                    "details": "Vardenafil chỉ dùng cho nam giới. Không áp dụng cho phụ nữ cho con bú.",
                    "recommendation": "Không áp dụng."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh liều",
                "moderate": "Thận trọng. Chuyển hóa qua gan có thể giảm, tăng nồng độ vardenafil. Giảm liều 5mg.",
                "severe": "Giảm liều 5mg. Chuyển hóa qua gan giảm đáng kể, tăng nồng độ vardenafil và nguy cơ tác dụng phụ.",
                "notes": "Vardenafil chuyển hóa qua gan (CYP3A4, CYP3A5, CYP2C9). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và nguy cơ tác dụng phụ. Cần giảm liều ở suy gan trung bình đến nặng."
            },
            "overdose_management": {
                "symptoms": [
                    "Hạ huyết áp nặng, ngất",
                    "Đau đầu nặng",
                    "Rối loạn thị giác nặng",
                    "Đau ngực",
                    "Nhịp tim nhanh"
                ],
                "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
                "treatment": [
                    "Nếu hạ huyết áp nặng:",
                    "  - Nằm đầu thấp, nâng chân",
                    "  - Truyền dịch (NS, LR) nếu cần",
                    "  - Thuốc vận mạch (norepinephrine, phenylephrine) nếu cần",
                    "Theo dõi: Huyết áp, nhịp tim, ECG liên tục",
                    "Hỗ trợ hô hấp nếu cần"
                ],
                "monitoring": "Theo dõi huyết áp, nhịp tim, ECG liên tục cho đến khi hồi phục."
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ. Nếu hạ huyết áp nặng: nằm đầu thấp, truyền dịch, thuốc vận mạch (norepinephrine, phenylephrine) nếu cần. Half-life 4-5 giờ nên tác dụng sẽ giảm sau vài giờ."
            },
            "administration_instructions": {
                "oral": {
                    "with_food": "Uống với hoặc không thức ăn. Có thể uống không thức ăn nếu cần.",
                    "timing": "10mg PO 30-60 phút trước hoạt động tình dục (tối đa 20mg, tối thiểu 5mg). Không dùng quá 1 lần/ngày.",
                    "notes": "QUAN TRỌNG: 1) CHỐNG CHỈ ĐỊNH với nitrate (cách xa ít nhất 24 giờ), 2) Tác dụng kéo dài 4-5 giờ, 3) NGỪNG NGAY nếu có mất thị lực hoặc mất thính lực đột ngột, 4) Thận trọng khi dùng với alpha-blockers."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Vardenafil (Levitra)",
                    "AUA Guidelines - Erectile Dysfunction",
                    "UpToDate - Vardenafil: Drug Information",
                    "Medscape - Vardenafil Drug Reference"
                ],
                "last_updated": "2025-02-18",
                "evidence_level": "A - Dựa trên FDA drug labels, AUA guidelines"
            },
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["ophthalmic", "cardiac"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Blood pressure", "Visual changes", "Hearing changes"]
            },
            "guideline_tags": [
                "FDA Drug Information",
                "UpToDate Drug Information",
                "AUA Guidelines - Erectile Dysfunction",
                "FDA Black Box Warning - Nitrate Contraindication"
            ]
        },

}

__all__ = ['ERECTILE_DYSFUNCTION_DRUGS']
