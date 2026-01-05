"""
Urology Drugs - Overactive Bladder
"""
from typing import Dict, Any


OVERACTIVE_BLADDER_DRUGS: Dict[str, Dict[str, Any]] = {
        "Fesoterodine": {
            "group": "Urology - Anticholinergic (Overactive Bladder)",
            "vietnamese_name": "Fesoterodine, Toviaz",
            "administration": ["PO"],
            "indications": [
                "Bàng quang tăng hoạt (overactive bladder - OAB)",
                "Tiểu không kiểm soát (urinary incontinence)",
                "Tiểu gấp, tiểu nhiều lần (urgency, frequency)",
                "Tiểu đêm (nocturia)"
            ],
            "contraindications": [
                "Dị ứng fesoterodine hoặc tolterodine",
                "Bí tiểu (urinary retention)",
                "Bệnh nhược cơ (myasthenia gravis)",
                "Tắc nghẽn đường tiểu (bladder outlet obstruction)",
                "Bệnh đường tiêu hóa nặng (tắc nghẽn, giảm nhu động)",
                "Glaucoma góc đóng (narrow-angle glaucoma)",
                "Suy gan nặng"
            ],
            "dosage": {
                "adult_po": "4mg PO x 1 lần/ngày",
                "adult_po_max": "8mg PO x 1 lần/ngày nếu cần",
                "notes": "Fesoterodine là prodrug của tolterodine, chuyển hóa thành tolterodine trong cơ thể. Tác dụng tương tự tolterodine nhưng hấp thu tốt hơn, ít biến đổi giữa các cá nhân. Bắt đầu với 4mg, tăng lên 8mg nếu cần và dung nạp tốt."
            },
            "renal_adjustment": {
                "normal": "Không đổi",
                "30_60": "Thận trọng, không vượt quá 4mg/ngày",
                "under_30": "CHỐNG CHỈ ĐỊNH"
            },
            "side_effects": [
                "Khô miệng - phổ biến (tăng theo liều)",
                "Táo bón - phổ biến",
                "Khô mắt, mờ mắt",
                "Rối loạn nhận thức (confusion, memory impairment) - đặc biệt ở người cao tuổi",
                "Buồn nôn",
                "Đau đầu",
                "Chóng mặt",
                "Bí tiểu (urinary retention) - hiếm nhưng nguy hiểm",
                "Nhịp tim nhanh (tachycardia)"
            ],
            "interactions": [
                "CYP3A4 inhibitors (ketoconazole, clarithromycin, itraconazole): tăng nồng độ fesoterodine - CHỐNG CHỈ ĐỊNH",
                "CYP2D6 inhibitors: tăng nồng độ fesoterodine",
                "Thuốc kháng cholinergic khác: tăng nguy cơ tác dụng phụ",
                "Thuốc gây QT kéo dài: tăng nguy cơ rối loạn nhịp tim"
            ],
            "pregnancy": "C - Thận trọng",
            "mechanism_of_action": "Fesoterodine là anticholinergic (muscarinic receptor antagonist). Fesoterodine là prodrug, chuyển hóa thành tolterodine (active metabolite) trong cơ thể bởi esterase. Tolterodine ức chế muscarinic receptors (M2, M3) trên cơ trơn bàng quang, gây giãn cơ bàng quang, tăng dung tích bàng quang, và giảm tần suất co bóp bàng quang. Dẫn đến: giảm tiểu gấp, giảm tiểu nhiều lần, giảm tiểu không kiểm soát. Fesoterodine hấp thu tốt hơn tolterodine, ít biến đổi giữa các cá nhân. ĐẶC ĐIỂM: (1) Prodrug của tolterodine, hấp thu tốt hơn, (2) Tác dụng tương tự tolterodine, (3) Nguy cơ khô miệng, táo bón, khô mắt, (4) Nguy cơ rối loạn nhận thức ở người cao tuổi, (5) CHỐNG CHỈ ĐỊNH với CYP3A4 inhibitors mạnh, (6) CHỐNG CHỈ ĐỊNH ở suy thận nặng.",
            "monitoring": [
                "Triệu chứng OAB (tiểu gấp, tiểu nhiều lần, tiểu không kiểm soát)",
                "Dấu hiệu khô miệng, táo bón, khô mắt",
                "Dấu hiệu rối loạn nhận thức (confusion, memory impairment) - đặc biệt ở người cao tuổi",
                "Dấu hiệu bí tiểu (urinary retention) - NGUY HIỂM",
                "Nhịp tim, ECG (nếu có tiền sử rối loạn nhịp tim)"
            ],
            "precautions": [
                "CHỐNG CHỈ ĐỊNH với CYP3A4 inhibitors mạnh (ketoconazole, clarithromycin, itraconazole)",
                "CHỐNG CHỈ ĐỊNH ở suy thận nặng (CrCl <30 mL/min)",
                "CHỐNG CHỈ ĐỊNH ở bí tiểu hoặc tắc nghẽn đường tiểu",
                "CHỐNG CHỈ ĐỊNH ở glaucoma góc đóng",
                "Nguy cơ rối loạn nhận thức ở người cao tuổi - cần theo dõi sát",
                "Khô miệng, táo bón - phổ biến, tăng theo liều",
                "Thận trọng ở bệnh nhân suy gan nặng",
                "Thận trọng ở bệnh nhân có tiền sử rối loạn nhịp tim",
                "Bắt đầu với liều thấp (4mg), tăng lên 8mg nếu cần và dung nạp tốt"
            ],
            "pharmacokinetics": {
                "half_life": "7 giờ (tolterodine active metabolite)",
                "onset": "1-2 tuần",
                "duration": "Dài (cần dùng liên tục)",
                "protein_binding": "Không đáng kể (fesoterodine), 96% (tolterodine)",
                "metabolism": "Esterase (fesoterodine → tolterodine), sau đó gan (CYP2D6, CYP3A4)",
                "clearance": "Gan, thận (bài tiết qua nước tiểu)"
            },
            "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
            "black_box_warnings": None,
            "drug_interactions": {
                "major": [
                    {
                        "drug": "CYP3A4 Inhibitors mạnh (Ketoconazole, Clarithromycin, Itraconazole, Ritonavir)",
                        "mechanism": "Ức chế CYP3A4, tăng nồng độ fesoterodine (tolterodine active metabolite)",
                        "effect": "Tăng nồng độ fesoterodine, tăng nguy cơ tác dụng phụ nặng (khô miệng, táo bón, bí tiểu, rối loạn nhận thức)",
                        "management": "CHỐNG CHỈ ĐỊNH. KHÔNG được dùng đồng thời."
                    }
                ],
                "moderate": [
                    {
                        "drug": "CYP2D6 Inhibitors (Paroxetine, Fluoxetine, Quinidine)",
                        "mechanism": "Ức chế CYP2D6, tăng nồng độ fesoterodine (tolterodine active metabolite)",
                        "effect": "Tăng nồng độ fesoterodine, tăng nguy cơ tác dụng phụ",
                        "management": "Thận trọng. Có thể cần giảm liều fesoterodine."
                    },
                    {
                        "drug": "Thuốc kháng cholinergic khác (Oxybutynin, Tolterodine, Solifenacin)",
                        "mechanism": "Tác dụng kháng cholinergic cộng dồn",
                        "effect": "Tăng nguy cơ tác dụng phụ (khô miệng, táo bón, bí tiểu, rối loạn nhận thức)",
                        "management": "TRÁNH DÙNG CHUNG. Nếu bắt buộc, theo dõi tác dụng phụ sát."
                    }
                ],
                "minor": []
            },
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng fesoterodine hoặc tolterodine",
                    "Bí tiểu (urinary retention) - CHỐNG CHỈ ĐỊNH",
                    "Tắc nghẽn đường tiểu (bladder outlet obstruction) - CHỐNG CHỈ ĐỊNH",
                    "Glaucoma góc đóng (narrow-angle glaucoma) - CHỐNG CHỈ ĐỊNH",
                    "Bệnh nhược cơ (myasthenia gravis) - CHỐNG CHỈ ĐỊNH",
                    "Bệnh đường tiêu hóa nặng (tắc nghẽn, giảm nhu động) - CHỐNG CHỈ ĐỊNH",
                    "Suy thận nặng (CrCl <30 mL/min) - CHỐNG CHỈ ĐỊNH",
                    "Dùng với CYP3A4 inhibitors mạnh - CHỐNG CHỈ ĐỊNH"
                ],
                "tương_đối": [
                    "Suy gan nặng - thận trọng (chuyển hóa qua gan)",
                    "Suy thận trung bình (CrCl 30-60 mL/min) - thận trọng, không vượt quá 4mg/ngày",
                    "Người cao tuổi - tăng nguy cơ rối loạn nhận thức",
                    "Bệnh tim - thận trọng (nguy cơ nhịp tim nhanh)"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Fesoterodine là thuốc phân loại C. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Fesoterodine có thể qua nhau thai. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt khi không có lựa chọn khác.",
                "lactation": {
                    "safety": "Compatible with Caution",
                    "details": "Fesoterodine (tolterodine active metabolite) bài tiết vào sữa mẹ ở nồng độ thấp. Tuy nhiên, nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ.",
                    "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng. Theo dõi trẻ bú mẹ về dấu hiệu khô miệng, táo bón."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh liều",
                "moderate": "Thận trọng. Chuyển hóa qua gan có thể giảm, tăng nồng độ fesoterodine. Giảm liều 4mg.",
                "severe": "CHỐNG CHỈ ĐỊNH. Chuyển hóa qua gan giảm đáng kể, tăng nồng độ fesoterodine và nguy cơ tác dụng phụ nặng.",
                "notes": "Fesoterodine chuyển hóa qua gan (CYP2D6, CYP3A4). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và nguy cơ tác dụng phụ. Cần thận trọng và giảm liều ở suy gan trung bình, CHỐNG CHỈ ĐỊNH ở suy gan nặng."
            },
            "overdose_management": {
                "symptoms": [
                    "Khô miệng nặng",
                    "Táo bón nặng",
                    "Bí tiểu (urinary retention) - NGUY HIỂM",
                    "Rối loạn nhận thức nặng (confusion, delirium)",
                    "Nhịp tim nhanh",
                    "Mờ mắt nặng"
                ],
                "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
                "treatment": [
                    "Ngừng ngay fesoterodine",
                    "Nếu bí tiểu:",
                    "  - Đặt ống thông tiểu nếu cần",
                    "  - Theo dõi lượng nước tiểu",
                    "Nếu rối loạn nhận thức nặng:",
                    "  - Theo dõi sát, hỗ trợ",
                    "  - Có thể cần thuốc an thần nếu kích động",
                    "Nếu nhịp tim nhanh:",
                    "  - Theo dõi ECG",
                    "  - Điều trị theo protocol nếu cần",
                    "Theo dõi: Dấu hiệu sinh tồn, lượng nước tiểu, tình trạng tinh thần"
                ],
                "monitoring": "Theo dõi dấu hiệu sinh tồn, lượng nước tiểu, tình trạng tinh thần cho đến khi hồi phục."
            },
            "reversal_agents": None,
            "administration_instructions": {
                "oral": {
                    "with_food": "Uống với hoặc không thức ăn. Có thể uống không thức ăn.",
                    "timing": "4mg PO x 1 lần/ngày. Tăng lên 8mg nếu cần và dung nạp tốt.",
                    "notes": "QUAN TRỌNG: 1) CHỐNG CHỈ ĐỊNH với CYP3A4 inhibitors mạnh, 2) CHỐNG CHỈ ĐỊNH ở suy thận nặng, 3) Bắt đầu với 4mg, tăng lên 8mg nếu cần, 4) Nguy cơ rối loạn nhận thức ở người cao tuổi, 5) Theo dõi dấu hiệu bí tiểu."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Fesoterodine (Toviaz)",
                    "AUA Guidelines - Management of Overactive Bladder",
                    "UpToDate - Fesoterodine: Drug Information",
                    "Medscape - Fesoterodine Drug Reference"
                ],
                "last_updated": "2025-02-18",
                "evidence_level": "A - Dựa trên FDA drug labels, AUA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
            },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["Urinary retention", "Cognitive impairment (especially in elderly)"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["OAB symptoms (urgency, frequency, incontinence)", "Signs of urinary retention - CRITICAL", "Cognitive function (especially in elderly)", "Dry mouth, constipation", "Heart rate (if history of arrhythmias)"]
            },
            "guideline_tags": [
                "AUA Guidelines - Management of Overactive Bladder",
                "FDA Drug Information - Fesoterodine",
                "UpToDate - Overactive Bladder Treatment"
            ]
        },

        "Mirabegron": {
            "group": "Urology - Beta-3 Adrenergic Agonist (Overactive Bladder)",
            "vietnamese_name": "Mirabegron, Myrbetriq",
            "administration": ["PO"],
            "indications": [
                "Bàng quang tăng hoạt (overactive bladder - OAB)",
                "Tiểu không kiểm soát (urinary incontinence)",
                "Tiểu gấp, tiểu nhiều lần (urgency, frequency)",
                "Tiểu đêm (nocturia)"
            ],
            "contraindications": [
                "Dị ứng mirabegron",
                "Tăng huyết áp không kiểm soát",
                "Bệnh tim nặng không ổn định"
            ],
            "dosage": {
                "adult_po": "25mg PO x 1 lần/ngày",
                "adult_po_max": "50mg PO x 1 lần/ngày nếu cần",
                "notes": "Mirabegron là beta-3 agonist, cơ chế khác với anticholinergic, ít tác dụng phụ hơn (không gây khô miệng, táo bón, rối loạn nhận thức)."
            },
            "renal_adjustment": {
                "normal": "Không đổi",
                "30_60": "Thận trọng, không vượt quá 25mg/ngày",
                "under_30": "Thận trọng, không vượt quá 25mg/ngày"
            },
            "side_effects": [
                "Tăng huyết áp - phổ biến (tăng nhẹ 2-4 mmHg)",
                "Nhịp tim nhanh",
                "Nhiễm trùng đường tiết niệu",
                "Đau đầu",
                "Táo bón (ít hơn anticholinergic)",
                "Chóng mặt"
            ],
            "interactions": [
                "Digoxin: tăng nồng độ digoxin - theo dõi nồng độ digoxin",
                "CYP2D6 substrates (metoprolol, desipramine): tăng nồng độ các thuốc này"
            ],
            "pregnancy": "C",
            "mechanism_of_action": "Mirabegron là beta-3 adrenergic receptor agonist. Kích thích beta-3 receptors trên cơ trơn bàng quang, gây giãn cơ bàng quang, tăng dung tích bàng quang, và giảm tần suất tiểu tiện. Khác với anticholinergic (oxybutynin, tolterodine, solifenacin), mirabegron không ức chế muscarinic receptors, do đó không gây khô miệng, táo bón, mờ mắt, hoặc rối loạn nhận thức. ĐẶC ĐIỂM: (1) Cơ chế khác với anticholinergic (beta-3 agonist), (2) Ít tác dụng phụ hơn anticholinergic (không khô miệng, không táo bón, không rối loạn nhận thức), (3) Tăng huyết áp nhẹ (2-4 mmHg) - cần theo dõi, (4) Có thể dùng kết hợp với anticholinergic để tăng hiệu quả, (5) Tương tác với digoxin và CYP2D6 substrates.",
            "monitoring": [
                "Triệu chứng OAB (tiểu gấp, tiểu nhiều lần, tiểu không kiểm soát)",
                "Huyết áp - QUAN TRỌNG (tăng nhẹ 2-4 mmHg)",
                "Nhịp tim",
                "Nồng độ digoxin nếu dùng với digoxin",
                "Dấu hiệu nhiễm trùng đường tiết niệu"
            ],
            "precautions": [
                "TĂNG HUYẾT ÁP - tăng nhẹ 2-4 mmHg, cần theo dõi",
                "CHỐNG CHỈ ĐỊNH ở tăng huyết áp không kiểm soát",
                "Thận trọng ở bệnh nhân bệnh tim (nhịp tim nhanh)",
                "Thận trọng ở bệnh nhân suy gan/thận (không vượt quá 25mg/ngày)",
                "Theo dõi nồng độ digoxin nếu dùng với digoxin",
                "Có thể dùng kết hợp với anticholinergic để tăng hiệu quả",
                "Ít tác dụng phụ hơn anticholinergic (không khô miệng, không táo bón, không rối loạn nhận thức)"
            ],
            "pharmacokinetics": {
                "half_life": "50 giờ (rất dài)",
                "onset": "1-2 tuần",
                "duration": "Rất dài (do half-life dài)",
                "protein_binding": "71%",
                "metabolism": "Gan (CYP3A4, CYP2D6, dealkylation, oxidation)",
                "clearance": "Gan, thận (bài tiết qua nước tiểu và phân)"
            },
            "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
            "black_box_warnings": None,
            "drug_interactions": {
                "major": [
                    {
                        "drug": "Digoxin",
                        "mechanism": "Mirabegron ức chế P-glycoprotein, tăng nồng độ digoxin",
                        "effect": "Tăng nồng độ digoxin, tăng nguy cơ độc tính digoxin (buồn nôn, nôn, rối loạn nhịp tim)",
                        "management": "Theo dõi nồng độ digoxin khi bắt đầu mirabegron. Có thể cần giảm liều digoxin."
                    }
                ],
                "moderate": [
                    {
                        "drug": "CYP2D6 Substrates (Metoprolol, Desipramine, Flecainide)",
                        "mechanism": "Mirabegron ức chế CYP2D6, tăng nồng độ các thuốc này",
                        "effect": "Tăng nồng độ các thuốc, tăng nguy cơ tác dụng phụ",
                        "management": "Thận trọng. Theo dõi tác dụng phụ. Có thể cần giảm liều các thuốc này."
                    }
                ],
                "minor": []
            },
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng mirabegron",
                    "Tăng huyết áp không kiểm soát - CHỐNG CHỈ ĐỊNH",
                    "Bệnh tim nặng không ổn định - CHỐNG CHỈ ĐỊNH"
                ],
                "tương_đối": [
                    "Tăng huyết áp ổn định - thận trọng, theo dõi huyết áp",
                    "Bệnh tim ổn định - thận trọng (nhịp tim nhanh)",
                    "Suy gan/thận nặng - không vượt quá 25mg/ngày",
                    "Dùng với digoxin - theo dõi nồng độ digoxin"
                ]
            },
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng mirabegron",
                    "Tăng huyết áp không kiểm soát - CHỐNG CHỈ ĐỊNH",
                    "Bệnh tim nặng không ổn định - CHỐNG CHỈ ĐỊNH"
                ],
                "tương_đối": [
                    "Tăng huyết áp ổn định - thận trọng, theo dõi huyết áp",
                    "Bệnh tim ổn định - thận trọng (nhịp tim nhanh)",
                    "Suy gan/thận nặng - không vượt quá 25mg/ngày",
                    "Dùng với digoxin - theo dõi nồng độ digoxin"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Mirabegron phân loại C - thận trọng trong thai kỳ. Không có dữ liệu đầy đủ trên phụ nữ có thai. Không khuyến cáo dùng trong thai kỳ trừ khi lợi ích vượt trội nguy cơ.",
                "lactation": {
                    "safety": "Unknown",
                    "details": "Không biết mirabegron có bài tiết vào sữa mẹ hay không. Không khuyến cáo dùng khi cho con bú.",
                    "recommendation": "Tránh dùng khi cho con bú. Nếu cần, ngừng cho con bú hoặc ngừng thuốc."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh liều",
                "moderate": "Thận trọng. Chuyển hóa qua gan có thể giảm, tăng nồng độ mirabegron. Không vượt quá 25mg/ngày.",
                "severe": "Thận trọng. Chuyển hóa qua gan giảm đáng kể, tăng nồng độ mirabegron và nguy cơ tác dụng phụ. Không vượt quá 25mg/ngày.",
                "notes": "Mirabegron chuyển hóa qua gan (CYP3A4, CYP2D6). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và nguy cơ tác dụng phụ. Không vượt quá 25mg/ngày ở suy gan/thận trung bình đến nặng."
            },
            "overdose_management": {
                "symptoms": [
                    "Tăng huyết áp nặng",
                    "Nhịp tim nhanh",
                    "Đau ngực",
                    "Khó thở",
                    "Chóng mặt"
                ],
                "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
                "treatment": [
                    "Ngừng ngay mirabegron",
                    "Rửa dạ dày nếu mới uống <1 giờ",
                    "Than hoạt tính",
                    "Nếu tăng huyết áp nặng: Thuốc hạ huyết áp (labetalol, esmolol) nếu cần",
                    "Nếu nhịp tim nhanh: Beta-blocker (metoprolol, esmolol) nếu cần",
                    "Theo dõi: Huyết áp, nhịp tim, ECG liên tục",
                    "Lưu ý: Half-life rất dài (50 giờ), tác dụng có thể kéo dài"
                ],
                "monitoring": "Theo dõi huyết áp, nhịp tim, ECG liên tục cho đến khi hồi phục. Half-life rất dài, cần theo dõi lâu hơn."
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ. Nếu tăng huyết áp nặng: thuốc hạ huyết áp (labetalol, esmolol). Nếu nhịp tim nhanh: beta-blocker (metoprolol, esmolol). Half-life rất dài (50 giờ) nên tác dụng sẽ kéo dài."
            },
            "administration_instructions": {
                "oral": {
                    "with_food": "Uống với hoặc không thức ăn. Có thể uống với thức ăn để giảm tác dụng phụ tiêu hóa.",
                    "timing": "25mg PO x 1 lần/ngày. Có thể tăng đến 50mg/ngày nếu cần. Không vượt quá 25mg/ngày ở suy gan/thận trung bình đến nặng.",
                    "notes": "QUAN TRỌNG: 1) Beta-3 agonist, cơ chế khác với anticholinergic, 2) Ít tác dụng phụ hơn anticholinergic (không khô miệng, không táo bón, không rối loạn nhận thức), 3) Tăng huyết áp nhẹ (2-4 mmHg) - cần theo dõi, 4) Half-life rất dài (50 giờ), 5) Theo dõi nồng độ digoxin nếu dùng với digoxin."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Mirabegron (Myrbetriq)",
                    "AUA Guidelines - Overactive Bladder",
                    "UpToDate - Mirabegron: Drug Information",
                    "Medscape - Mirabegron Drug Reference"
                ],
                "last_updated": "2025-02-18",
                "evidence_level": "A - Dựa trên FDA drug labels, AUA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
            },
            "black_box_warnings": "Cần xem xét black box warnings",
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": [],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [],
            },
            "guideline_tags": [
                "FDA Drug Information",
                "UpToDate Drug Information",
            ]
        },

        "Oxybutynin": {
            "group": "Urology - Anticholinergic (Overactive Bladder)",
            "vietnamese_name": "Oxybutynin, Ditropan",
            "administration": ["PO", "TD", "Topical"],
            "indications": [
                "Bàng quang tăng hoạt (overactive bladder - OAB)",
                "Tiểu không kiểm soát (urinary incontinence)",
                "Tiểu gấp, tiểu nhiều lần (urgency, frequency)",
                "Tiểu đêm (nocturia)"
            ],
            "contraindications": [
                "Dị ứng oxybutynin",
                "Bí tiểu (urinary retention)",
                "Tăng nhãn áp góc đóng (narrow-angle glaucoma)",
                "Bệnh nhược cơ (myasthenia gravis)",
                "Tắc nghẽn đường tiêu hóa (GI obstruction)",
                "Megacolon độc tính (toxic megacolon)"
            ],
            "dosage": {
                "adult_po": "5mg PO x 2-3 lần/ngày (tối đa 5mg x 4 lần/ngày)",
                "adult_po_er": "5-10mg PO x 1 lần/ngày (extended-release)",
                "adult_td": "3.9mg/ngày (transdermal patch, thay mỗi 3-4 ngày)",
                "adult_topical": "10% gel, 1g x 1 lần/ngày (áp dụng lên da)",
                "notes": "Bắt đầu với liều thấp và tăng dần. Extended-release và transdermal ít tác dụng phụ hơn immediate-release."
            },
            "renal_adjustment": {
                "normal": "Không đổi",
                "30_60": "Thận trọng, có thể giảm liều",
                "under_30": "Thận trọng, giảm liều"
            },
            "side_effects": [
                "Khô miệng - RẤT PHỔ BIẾN",
                "Táo bón",
                "Mờ mắt, khô mắt",
                "Buồn ngủ, chóng mặt",
                "Rối loạn nhận thức (đặc biệt ở người cao tuổi) - NGUY HIỂM",
                "Bí tiểu (urinary retention)",
                "Nhịp tim nhanh",
                "Đỏ da, kích ứng da (với transdermal/topical)"
            ],
            "interactions": [
                "Thuốc anticholinergic khác: tăng tác dụng phụ",
                "Thuốc ức chế CYP3A4: tăng nồng độ oxybutynin",
                "Thuốc kích thích CYP3A4: giảm nồng độ oxybutynin"
            ],
            "pregnancy": "B",
            "mechanism_of_action": "Oxybutynin là anticholinergic (muscarinic receptor antagonist). Ức chế muscarinic receptors (M1, M2, M3) trên cơ trơn bàng quang, giảm co thắt bàng quang không tự chủ, tăng dung tích bàng quang, và giảm tần suất tiểu tiện. Oxybutynin cũng có tác dụng gây tê cục bộ và giãn cơ trơn. ĐẶC ĐIỂM: (1) Anticholinergic không chọn lọc (ảnh hưởng nhiều cơ quan), (2) Tác dụng phụ phổ biến: khô miệng, táo bón, mờ mắt, (3) Nguy cơ rối loạn nhận thức ở người cao tuổi, (4) Extended-release và transdermal ít tác dụng phụ hơn immediate-release, (5) CHỐNG CHỈ ĐỊNH ở bí tiểu và tăng nhãn áp góc đóng.",
            "monitoring": [
                "Triệu chứng OAB (tiểu gấp, tiểu nhiều lần, tiểu không kiểm soát)",
                "Dấu hiệu bí tiểu (khó tiểu, đau bụng dưới)",
                "Dấu hiệu tăng nhãn áp (đau mắt, mờ mắt)",
                "Dấu hiệu rối loạn nhận thức (đặc biệt ở người cao tuổi)",
                "Dấu hiệu táo bón",
                "Dấu hiệu khô miệng (có thể nghiêm trọng)"
            ],
            "precautions": [
                "KHÔ MIỆNG - RẤT PHỔ BIẾN, có thể nghiêm trọng",
                "RỐI LOẠN NHẬN THỨC - đặc biệt ở người cao tuổi, NGUY HIỂM",
                "CHỐNG CHỈ ĐỊNH ở bí tiểu và tăng nhãn áp góc đóng",
                "Thận trọng ở người cao tuổi (tăng nguy cơ rối loạn nhận thức)",
                "Thận trọng ở bệnh nhân suy gan/thận",
                "Extended-release và transdermal ít tác dụng phụ hơn immediate-release",
                "Bắt đầu với liều thấp và tăng dần",
                "Theo dõi dấu hiệu bí tiểu và tăng nhãn áp"
            ],
            "pharmacokinetics": {
                "half_life": "2-3 giờ (immediate-release), 13 giờ (extended-release)",
                "onset": "1-2 tuần",
                "duration": "Ngắn (immediate-release), dài (extended-release)",
                "protein_binding": "83%",
                "metabolism": "Gan (CYP3A4)",
                "clearance": "Gan, thận (bài tiết qua nước tiểu và phân)"
            },
            "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Transdermal patch: bảo quản trong túi kín.",
            "black_box_warnings": None,
            "drug_interactions": {
                "major": [
                    {
                        "drug": "Thuốc anticholinergic khác (Benztropine, Trihexyphenidyl, Scopolamine)",
                        "mechanism": "Tác dụng anticholinergic cộng dồn",
                        "effect": "Tăng tác dụng phụ: khô miệng, táo bón, mờ mắt, rối loạn nhận thức, bí tiểu",
                        "management": "Thận trọng. Theo dõi tác dụng phụ. Có thể cần giảm liều."
                    }
                ],
                "moderate": [
                    {
                        "drug": "CYP3A4 Inhibitors (Ketoconazole, Itraconazole, Ritonavir)",
                        "mechanism": "Ức chế CYP3A4, tăng nồng độ oxybutynin",
                        "effect": "Tăng nồng độ oxybutynin, tăng nguy cơ tác dụng phụ",
                        "management": "Thận trọng. Có thể cần giảm liều oxybutynin."
                    },
                    {
                        "drug": "CYP3A4 Inducers (Rifampin, Carbamazepine, Phenytoin)",
                        "mechanism": "Kích thích CYP3A4, giảm nồng độ oxybutynin",
                        "effect": "Giảm nồng độ oxybutynin, giảm hiệu quả",
                        "management": "Thận trọng. Có thể cần tăng liều oxybutynin."
                    }
                ],
                "minor": []
            },
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng oxybutynin",
                    "Bí tiểu (urinary retention) - CHỐNG CHỈ ĐỊNH",
                    "Tăng nhãn áp góc đóng (narrow-angle glaucoma) - CHỐNG CHỈ ĐỊNH",
                    "Bệnh nhược cơ (myasthenia gravis) - CHỐNG CHỈ ĐỊNH",
                    "Tắc nghẽn đường tiêu hóa (GI obstruction) - CHỐNG CHỈ ĐỊNH",
                    "Megacolon độc tính (toxic megacolon) - CHỐNG CHỈ ĐỊNH"
                ],
                "tương_đối": [
                    "Người cao tuổi - tăng nguy cơ rối loạn nhận thức",
                    "Suy gan/thận nặng - thận trọng, giảm liều",
                    "Bệnh tim - thận trọng (nhịp tim nhanh)"
                ]
            },
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng oxybutynin",
                    "Bí tiểu (urinary retention) - CHỐNG CHỈ ĐỊNH",
                    "Tăng nhãn áp góc đóng (narrow-angle glaucoma) - CHỐNG CHỈ ĐỊNH",
                    "Bệnh nhược cơ (myasthenia gravis) - CHỐNG CHỈ ĐỊNH",
                    "Tắc nghẽn đường tiêu hóa (GI obstruction) - CHỐNG CHỈ ĐỊNH",
                    "Megacolon độc tính (toxic megacolon) - CHỐNG CHỈ ĐỊNH"
                ],
                "tương_đối": [
                    "Người cao tuổi - tăng nguy cơ rối loạn nhận thức",
                    "Suy gan/thận nặng - thận trọng, giảm liều",
                    "Bệnh tim - thận trọng (nhịp tim nhanh)"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "B",
                "pregnancy_details": "Oxybutynin phân loại B - thận trọng trong thai kỳ. Không có dữ liệu đầy đủ trên phụ nữ có thai. Không khuyến cáo dùng trong thai kỳ trừ khi lợi ích vượt trội nguy cơ.",
                "lactation": {
                    "safety": "Unknown",
                    "details": "Không biết oxybutynin có bài tiết vào sữa mẹ hay không. Không khuyến cáo dùng khi cho con bú.",
                    "recommendation": "Tránh dùng khi cho con bú. Nếu cần, ngừng cho con bú hoặc ngừng thuốc."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh liều",
                "moderate": "Thận trọng. Chuyển hóa qua gan có thể giảm, tăng nồng độ oxybutynin. Giảm liều.",
                "severe": "Giảm liều. Chuyển hóa qua gan giảm đáng kể, tăng nồng độ oxybutynin và nguy cơ tác dụng phụ.",
                "notes": "Oxybutynin chuyển hóa qua gan (CYP3A4). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và nguy cơ tác dụng phụ. Cần giảm liều ở suy gan trung bình đến nặng."
            },
            "overdose_management": {
                "symptoms": [
                    "Rối loạn nhận thức nặng, mê sảng",
                    "Bí tiểu nặng",
                    "Táo bón nặng",
                    "Mờ mắt nặng",
                    "Nhịp tim nhanh",
                    "Khô miệng nặng"
                ],
                "antidote": "Physostigmine (anticholinesterase) - có thể dùng trong trường hợp nặng",
                "treatment": [
                    "Ngừng ngay oxybutynin",
                    "Rửa dạ dày nếu mới uống <1 giờ",
                    "Than hoạt tính",
                    "Nếu rối loạn nhận thức nặng: Physostigmine 1-2mg IV (thận trọng)",
                    "Điều trị bí tiểu: Đặt ống thông tiểu nếu cần",
                    "Điều trị táo bón: Thuốc nhuận tràng, thụt tháo nếu cần",
                    "Theo dõi: Dấu hiệu sinh tồn, dấu hiệu rối loạn nhận thức"
                ],
                "monitoring": "Theo dõi dấu hiệu sinh tồn, dấu hiệu rối loạn nhận thức, bí tiểu, táo bón cho đến khi hồi phục."
            },
            "reversal_agents": {
                "available": True,
                "agents": ["Physostigmine (anticholinesterase) - có thể dùng trong trường hợp nặng"]
            },
            "administration_instructions": {
                "oral": {
                    "with_food": "Uống với hoặc không thức ăn. Có thể uống với thức ăn để giảm tác dụng phụ tiêu hóa.",
                    "timing": "Immediate-release: 5mg PO x 2-3 lần/ngày (tối đa 5mg x 4 lần/ngày). Extended-release: 5-10mg PO x 1 lần/ngày. Bắt đầu với liều thấp và tăng dần.",
                    "notes": "QUAN TRỌNG: 1) Bắt đầu với liều thấp và tăng dần, 2) Extended-release ít tác dụng phụ hơn immediate-release, 3) Theo dõi rối loạn nhận thức (đặc biệt ở người cao tuổi), 4) CHỐNG CHỈ ĐỊNH ở bí tiểu và tăng nhãn áp góc đóng, 5) Khô miệng rất phổ biến."
                },
                "transdermal": {
                    "application": "Áp dụng patch lên da sạch, khô (bụng, hông, mông). Thay patch mỗi 3-4 ngày. Thay đổi vị trí mỗi lần.",
                    "notes": "Transdermal patch ít tác dụng phụ hơn oral. Có thể gây kích ứng da."
                },
                "topical": {
                    "application": "Áp dụng gel lên da sạch, khô (bụng, đùi, cánh tay, vai). Thay đổi vị trí mỗi lần.",
                    "notes": "Topical gel ít tác dụng phụ hơn oral. Có thể gây kích ứng da."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Oxybutynin (Ditropan)",
                    "AUA Guidelines - Overactive Bladder",
                    "UpToDate - Oxybutynin: Drug Information",
                    "Medscape - Oxybutynin Drug Reference"
                ],
                "last_updated": "2025-02-18",
                "evidence_level": "A - Dựa trên FDA drug labels, AUA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
            },
            "black_box_warnings": "Cần xem xét black box warnings",
        },

        "Solifenacin": {
            "group": "Urology - Anticholinergic (Overactive Bladder)",
            "vietnamese_name": "Solifenacin, Vesicare",
            "administration": ["PO"],
            "indications": [
                "Bàng quang tăng hoạt (overactive bladder - OAB)",
                "Tiểu không kiểm soát (urinary incontinence)",
                "Tiểu gấp, tiểu nhiều lần (urgency, frequency)",
                "Tiểu đêm (nocturia)"
            ],
            "contraindications": [
                "Dị ứng solifenacin",
                "Bí tiểu (urinary retention)",
                "Tăng nhãn áp góc đóng (narrow-angle glaucoma)",
                "Bệnh nhược cơ (myasthenia gravis)",
                "Tắc nghẽn đường tiêu hóa (GI obstruction)",
                "Suy gan nặng",
                "Suy thận nặng (CrCl <30)"
            ],
            "dosage": {
                "adult_po": "5mg PO x 1 lần/ngày",
                "adult_po_max": "10mg PO x 1 lần/ngày nếu cần",
                "notes": "Solifenacin chọn lọc M3 receptors (chọn lọc nhất trong các anticholinergic), ít tác dụng phụ hơn oxybutynin và tolterodine."
            },
            "renal_adjustment": {
                "normal": "Không đổi",
                "30_60": "Thận trọng, không vượt quá 5mg/ngày",
                "under_30": "CHỐNG CHỈ ĐỊNH (CrCl <30)"
            },
            "side_effects": [
                "Khô miệng - phổ biến (ít hơn oxybutynin và tolterodine)",
                "Táo bón",
                "Mờ mắt, khô mắt",
                "Buồn ngủ, chóng mặt",
                "Rối loạn nhận thức (ít hơn oxybutynin và tolterodine)",
                "Bí tiểu (urinary retention)",
                "Nhịp tim nhanh"
            ],
            "interactions": [
                "Thuốc anticholinergic khác: tăng tác dụng phụ",
                "CYP3A4 inhibitors (ketoconazole, itraconazole, ritonavir): tăng nồng độ solifenacin - không vượt quá 5mg/ngày"
            ],
            "pregnancy": "C",
            "mechanism_of_action": "Solifenacin là anticholinergic (muscarinic receptor antagonist) chọn lọc M3 receptors. M3 receptors là thụ thể chính trên cơ trơn bàng quang. Ức chế M3 receptors, giảm co thắt bàng quang không tự chủ, tăng dung tích bàng quang, và giảm tần suất tiểu tiện. Solifenacin chọn lọc M3 hơn oxybutynin và tolterodine, do đó ít ảnh hưởng đến các cơ quan khác (ít khô miệng, ít rối loạn nhận thức hơn). ĐẶC ĐIỂM: (1) Chọn lọc M3 receptors (chọn lọc nhất), (2) Tác dụng phụ: khô miệng, táo bón (ít hơn oxybutynin và tolterodine), (3) Nguy cơ rối loạn nhận thức ít hơn oxybutynin và tolterodine, (4) CHỐNG CHỈ ĐỊNH ở bí tiểu, tăng nhãn áp góc đóng, và suy thận nặng (CrCl <30).",
            "monitoring": [
                "Triệu chứng OAB (tiểu gấp, tiểu nhiều lần, tiểu không kiểm soát)",
                "Dấu hiệu bí tiểu (khó tiểu, đau bụng dưới)",
                "Dấu hiệu tăng nhãn áp (đau mắt, mờ mắt)",
                "Dấu hiệu rối loạn nhận thức (đặc biệt ở người cao tuổi)",
                "Dấu hiệu táo bón",
                "Dấu hiệu khô miệng",
                "Chức năng thận (creatinine, eGFR) - CHỐNG CHỈ ĐỊNH ở CrCl <30"
            ],
            "precautions": [
                "KHÔ MIỆNG - phổ biến (ít hơn oxybutynin và tolterodine)",
                "RỐI LOẠN NHẬN THỨC - ít hơn oxybutynin và tolterodine, nhưng vẫn có nguy cơ",
                "CHỐNG CHỈ ĐỊNH ở bí tiểu, tăng nhãn áp góc đóng, và suy thận nặng (CrCl <30)",
                "Thận trọng ở người cao tuổi (tăng nguy cơ rối loạn nhận thức)",
                "Thận trọng ở bệnh nhân suy gan/thận (CrCl 30-60: không vượt quá 5mg/ngày)",
                "Không vượt quá 5mg/ngày khi dùng với CYP3A4 inhibitors",
                "Bắt đầu với liều thấp (5mg) và tăng dần nếu cần",
                "Theo dõi dấu hiệu bí tiểu và tăng nhãn áp"
            ],
            "pharmacokinetics": {
                "half_life": "45-68 giờ (rất dài)",
                "onset": "1-2 tuần",
                "duration": "Rất dài (do half-life dài)",
                "protein_binding": "98%",
                "metabolism": "Gan (CYP3A4)",
                "clearance": "Gan, thận (bài tiết qua nước tiểu và phân)"
            },
            "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
            "black_box_warnings": None,
            "drug_interactions": {
                "major": [
                    {
                        "drug": "CYP3A4 Inhibitors mạnh (Ketoconazole, Itraconazole, Ritonavir)",
                        "mechanism": "Ức chế CYP3A4, tăng nồng độ solifenacin",
                        "effect": "Tăng nồng độ solifenacin đáng kể, tăng nguy cơ tác dụng phụ",
                        "management": "Không vượt quá 5mg/ngày khi dùng với CYP3A4 inhibitors. Theo dõi tác dụng phụ."
                    },
                    {
                        "drug": "Thuốc anticholinergic khác",
                        "mechanism": "Tác dụng anticholinergic cộng dồn",
                        "effect": "Tăng tác dụng phụ: khô miệng, táo bón, mờ mắt, rối loạn nhận thức",
                        "management": "Thận trọng. Theo dõi tác dụng phụ. Có thể cần giảm liều."
                    }
                ],
                "moderate": [],
                "minor": []
            },
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng solifenacin",
                    "Bí tiểu (urinary retention) - CHỐNG CHỈ ĐỊNH",
                    "Tăng nhãn áp góc đóng (narrow-angle glaucoma) - CHỐNG CHỈ ĐỊNH",
                    "Bệnh nhược cơ (myasthenia gravis) - CHỐNG CHỈ ĐỊNH",
                    "Tắc nghẽn đường tiêu hóa (GI obstruction) - CHỐNG CHỈ ĐỊNH",
                    "Suy gan nặng - CHỐNG CHỈ ĐỊNH",
                    "Suy thận nặng (CrCl <30) - CHỐNG CHỈ ĐỊNH"
                ],
                "tương_đối": [
                    "Người cao tuổi - tăng nguy cơ rối loạn nhận thức",
                    "Suy gan/thận trung bình (CrCl 30-60) - không vượt quá 5mg/ngày",
                    "Dùng với CYP3A4 inhibitors - không vượt quá 5mg/ngày"
                ]
            },
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng solifenacin",
                    "Bí tiểu (urinary retention) - CHỐNG CHỈ ĐỊNH",
                    "Tăng nhãn áp góc đóng (narrow-angle glaucoma) - CHỐNG CHỈ ĐỊNH",
                    "Bệnh nhược cơ (myasthenia gravis) - CHỐNG CHỈ ĐỊNH",
                    "Tắc nghẽn đường tiêu hóa (GI obstruction) - CHỐNG CHỈ ĐỊNH",
                    "Suy gan nặng - CHỐNG CHỈ ĐỊNH",
                    "Suy thận nặng (CrCl <30) - CHỐNG CHỈ ĐỊNH"
                ],
                "tương_đối": [
                    "Người cao tuổi - tăng nguy cơ rối loạn nhận thức",
                    "Suy gan/thận trung bình (CrCl 30-60) - không vượt quá 5mg/ngày",
                    "Dùng với CYP3A4 inhibitors - không vượt quá 5mg/ngày"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Solifenacin phân loại C - thận trọng trong thai kỳ. Không có dữ liệu đầy đủ trên phụ nữ có thai. Không khuyến cáo dùng trong thai kỳ trừ khi lợi ích vượt trội nguy cơ.",
                "lactation": {
                    "safety": "Unknown",
                    "details": "Không biết solifenacin có bài tiết vào sữa mẹ hay không. Không khuyến cáo dùng khi cho con bú.",
                    "recommendation": "Tránh dùng khi cho con bú. Nếu cần, ngừng cho con bú hoặc ngừng thuốc."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh liều",
                "moderate": "Thận trọng. Chuyển hóa qua gan có thể giảm, tăng nồng độ solifenacin. Giảm liều.",
                "severe": "CHỐNG CHỈ ĐỊNH. Chuyển hóa qua gan giảm đáng kể, tăng nồng độ solifenacin và nguy cơ tác dụng phụ.",
                "notes": "Solifenacin chuyển hóa qua gan (CYP3A4). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và nguy cơ tác dụng phụ. CHỐNG CHỈ ĐỊNH ở suy gan nặng."
            },
            "overdose_management": {
                "symptoms": [
                    "Rối loạn nhận thức nặng, mê sảng",
                    "Bí tiểu nặng",
                    "Táo bón nặng",
                    "Mờ mắt nặng",
                    "Nhịp tim nhanh",
                    "Khô miệng nặng"
                ],
                "antidote": "Physostigmine (anticholinesterase) - có thể dùng trong trường hợp nặng",
                "treatment": [
                    "Ngừng ngay solifenacin",
                    "Rửa dạ dày nếu mới uống <1 giờ",
                    "Than hoạt tính",
                    "Nếu rối loạn nhận thức nặng: Physostigmine 1-2mg IV (thận trọng)",
                    "Điều trị bí tiểu: Đặt ống thông tiểu nếu cần",
                    "Điều trị táo bón: Thuốc nhuận tràng, thụt tháo nếu cần",
                    "Theo dõi: Dấu hiệu sinh tồn, dấu hiệu rối loạn nhận thức",
                    "Lưu ý: Half-life rất dài (45-68 giờ), tác dụng có thể kéo dài"
                ],
                "monitoring": "Theo dõi dấu hiệu sinh tồn, dấu hiệu rối loạn nhận thức, bí tiểu, táo bón cho đến khi hồi phục. Half-life rất dài, cần theo dõi lâu hơn."
            },
            "reversal_agents": {
                "available": True,
                "agents": ["Physostigmine (anticholinesterase) - có thể dùng trong trường hợp nặng"]
            },
            "administration_instructions": {
                "oral": {
                    "with_food": "Uống với hoặc không thức ăn. Có thể uống với thức ăn để giảm tác dụng phụ tiêu hóa.",
                    "timing": "5mg PO x 1 lần/ngày. Có thể tăng đến 10mg/ngày nếu cần. Không vượt quá 5mg/ngày khi dùng với CYP3A4 inhibitors.",
                    "notes": "QUAN TRỌNG: 1) Chọn lọc M3 receptors (chọn lọc nhất), ít tác dụng phụ hơn oxybutynin và tolterodine, 2) Half-life rất dài (45-68 giờ), 3) Theo dõi rối loạn nhận thức (ít hơn các thuốc khác), 4) CHỐNG CHỈ ĐỊNH ở bí tiểu, tăng nhãn áp góc đóng, và suy thận nặng (CrCl <30), 5) Không vượt quá 5mg/ngày khi dùng với CYP3A4 inhibitors."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Solifenacin (Vesicare)",
                    "AUA Guidelines - Overactive Bladder",
                    "UpToDate - Solifenacin: Drug Information",
                    "Medscape - Solifenacin Drug Reference"
                ],
                "last_updated": "2025-02-18",
                "evidence_level": "A - Dựa trên FDA drug labels, AUA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
            },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["Urinary retention (contraindicated)", "Narrow-angle glaucoma (contraindicated)", "Cognitive impairment (less than oxybutynin/tolterodine)"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["OAB symptoms (urgency, frequency, incontinence, nocturia)", "Signs of urinary retention (difficulty urinating, lower abdominal pain) - CRITICAL", "Signs of narrow-angle glaucoma (eye pain, blurred vision) - CRITICAL", "Signs of cognitive impairment (especially in elderly)", "Constipation", "Dry mouth", "Renal function (creatinine, eGFR) - CONTRAINDICATED if CrCl <30"]
            },
            "guideline_tags": [
                "AUA Guidelines - Overactive Bladder",
                "FDA Drug Information - Solifenacin"
            ],
            "black_box_warnings": "Cần xem xét black box warnings",
        },

        "Tolterodine": {
            "group": "Urology - Anticholinergic (Overactive Bladder)",
            "vietnamese_name": "Tolterodine, Detrol",
            "administration": ["PO"],
            "indications": [
                "Bàng quang tăng hoạt (overactive bladder - OAB)",
                "Tiểu không kiểm soát (urinary incontinence)",
                "Tiểu gấp, tiểu nhiều lần (urgency, frequency)",
                "Tiểu đêm (nocturia)"
            ],
            "contraindications": [
                "Dị ứng tolterodine",
                "Bí tiểu (urinary retention)",
                "Tăng nhãn áp góc đóng (narrow-angle glaucoma)",
                "Bệnh nhược cơ (myasthenia gravis)",
                "Tắc nghẽn đường tiêu hóa (GI obstruction)",
                "Suy gan nặng"
            ],
            "dosage": {
                "adult_po": "2mg PO x 2 lần/ngày",
                "adult_po_er": "4mg PO x 1 lần/ngày (extended-release)",
                "adult_reduced": "1mg PO x 2 lần/ngày (nếu dùng với CYP3A4 inhibitors)",
                "notes": "Tolterodine chọn lọc hơn oxybutynin, ít tác dụng phụ hơn. Extended-release ít tác dụng phụ hơn immediate-release."
            },
            "renal_adjustment": {
                "normal": "Không đổi",
                "30_60": "Không cần điều chỉnh đáng kể",
                "under_30": "Thận trọng, có thể giảm liều"
            },
            "side_effects": [
                "Khô miệng - phổ biến (ít hơn oxybutynin)",
                "Táo bón",
                "Mờ mắt, khô mắt",
                "Buồn ngủ, chóng mặt",
                "Rối loạn nhận thức (ít hơn oxybutynin, nhưng vẫn có nguy cơ)",
                "Bí tiểu (urinary retention)",
                "Nhịp tim nhanh"
            ],
            "interactions": [
                "Thuốc anticholinergic khác: tăng tác dụng phụ",
                "CYP3A4 inhibitors (ketoconazole, itraconazole, ritonavir): tăng nồng độ tolterodine - giảm liều",
                "CYP2D6 inhibitors (fluoxetine, paroxetine): tăng nồng độ tolterodine"
            ],
            "pregnancy": "C",
            "mechanism_of_action": "Tolterodine là anticholinergic (muscarinic receptor antagonist) chọn lọc hơn oxybutynin. Ức chế muscarinic receptors trên cơ trơn bàng quang, giảm co thắt bàng quang không tự chủ, tăng dung tích bàng quang, và giảm tần suất tiểu tiện. Tolterodine chọn lọc hơn oxybutynin, ít ảnh hưởng đến các cơ quan khác (ít khô miệng, ít rối loạn nhận thức hơn). ĐẶC ĐIỂM: (1) Chọn lọc hơn oxybutynin (ít tác dụng phụ hơn), (2) Tác dụng phụ: khô miệng, táo bón (ít hơn oxybutynin), (3) Nguy cơ rối loạn nhận thức ít hơn oxybutynin, (4) Extended-release ít tác dụng phụ hơn immediate-release, (5) CHỐNG CHỈ ĐỊNH ở bí tiểu và tăng nhãn áp góc đóng.",
            "monitoring": [
                "Triệu chứng OAB (tiểu gấp, tiểu nhiều lần, tiểu không kiểm soát)",
                "Dấu hiệu bí tiểu (khó tiểu, đau bụng dưới)",
                "Dấu hiệu tăng nhãn áp (đau mắt, mờ mắt)",
                "Dấu hiệu rối loạn nhận thức (đặc biệt ở người cao tuổi)",
                "Dấu hiệu táo bón",
                "Dấu hiệu khô miệng"
            ],
            "precautions": [
                "KHÔ MIỆNG - phổ biến (ít hơn oxybutynin)",
                "RỐI LOẠN NHẬN THỨC - ít hơn oxybutynin, nhưng vẫn có nguy cơ, đặc biệt ở người cao tuổi",
                "CHỐNG CHỈ ĐỊNH ở bí tiểu và tăng nhãn áp góc đóng",
                "Thận trọng ở người cao tuổi (tăng nguy cơ rối loạn nhận thức)",
                "Thận trọng ở bệnh nhân suy gan/thận",
                "Giảm liều khi dùng với CYP3A4 inhibitors",
                "Extended-release ít tác dụng phụ hơn immediate-release",
                "Bắt đầu với liều thấp và tăng dần",
                "Theo dõi dấu hiệu bí tiểu và tăng nhãn áp"
            ],
            "pharmacokinetics": {
                "half_life": "2-3 giờ (immediate-release), 7-8 giờ (extended-release)",
                "onset": "1-2 tuần",
                "duration": "Ngắn (immediate-release), dài (extended-release)",
                "protein_binding": "96%",
                "metabolism": "Gan (CYP3A4, CYP2D6)",
                "clearance": "Gan, thận (bài tiết qua nước tiểu và phân)"
            },
            "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
            "black_box_warnings": None,
            "drug_interactions": {
                "major": [
                    {
                        "drug": "CYP3A4 Inhibitors mạnh (Ketoconazole, Itraconazole, Ritonavir)",
                        "mechanism": "Ức chế CYP3A4, tăng nồng độ tolterodine",
                        "effect": "Tăng nồng độ tolterodine đáng kể, tăng nguy cơ tác dụng phụ",
                        "management": "Giảm liều tolterodine xuống 1mg x 2 lần/ngày. Theo dõi tác dụng phụ."
                    },
                    {
                        "drug": "Thuốc anticholinergic khác",
                        "mechanism": "Tác dụng anticholinergic cộng dồn",
                        "effect": "Tăng tác dụng phụ: khô miệng, táo bón, mờ mắt, rối loạn nhận thức",
                        "management": "Thận trọng. Theo dõi tác dụng phụ. Có thể cần giảm liều."
                    }
                ],
                "moderate": [
                    {
                        "drug": "CYP2D6 Inhibitors (Fluoxetine, Paroxetine, Quinidine)",
                        "mechanism": "Ức chế CYP2D6, tăng nồng độ tolterodine",
                        "effect": "Tăng nồng độ tolterodine, tăng nguy cơ tác dụng phụ",
                        "management": "Thận trọng. Có thể cần giảm liều tolterodine."
                    }
                ],
                "minor": []
            },
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng tolterodine",
                    "Bí tiểu (urinary retention) - CHỐNG CHỈ ĐỊNH",
                    "Tăng nhãn áp góc đóng (narrow-angle glaucoma) - CHỐNG CHỈ ĐỊNH",
                    "Bệnh nhược cơ (myasthenia gravis) - CHỐNG CHỈ ĐỊNH",
                    "Tắc nghẽn đường tiêu hóa (GI obstruction) - CHỐNG CHỈ ĐỊNH",
                    "Suy gan nặng - CHỐNG CHỈ ĐỊNH"
                ],
                "tương_đối": [
                    "Người cao tuổi - tăng nguy cơ rối loạn nhận thức",
                    "Suy gan/thận trung bình - thận trọng, giảm liều",
                    "Dùng với CYP3A4 inhibitors - giảm liều"
                ]
            },
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng tolterodine",
                    "Bí tiểu (urinary retention) - CHỐNG CHỈ ĐỊNH",
                    "Tăng nhãn áp góc đóng (narrow-angle glaucoma) - CHỐNG CHỈ ĐỊNH",
                    "Bệnh nhược cơ (myasthenia gravis) - CHỐNG CHỈ ĐỊNH",
                    "Tắc nghẽn đường tiêu hóa (GI obstruction) - CHỐNG CHỈ ĐỊNH",
                    "Suy gan nặng - CHỐNG CHỈ ĐỊNH"
                ],
                "tương_đối": [
                    "Người cao tuổi - tăng nguy cơ rối loạn nhận thức",
                    "Suy gan/thận trung bình - thận trọng, giảm liều",
                    "Dùng với CYP3A4 inhibitors - giảm liều"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Tolterodine phân loại C - thận trọng trong thai kỳ. Không có dữ liệu đầy đủ trên phụ nữ có thai. Không khuyến cáo dùng trong thai kỳ trừ khi lợi ích vượt trội nguy cơ.",
                "lactation": {
                    "safety": "Unknown",
                    "details": "Không biết tolterodine có bài tiết vào sữa mẹ hay không. Không khuyến cáo dùng khi cho con bú.",
                    "recommendation": "Tránh dùng khi cho con bú. Nếu cần, ngừng cho con bú hoặc ngừng thuốc."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh liều",
                "moderate": "Thận trọng. Chuyển hóa qua gan có thể giảm, tăng nồng độ tolterodine. Giảm liều.",
                "severe": "CHỐNG CHỈ ĐỊNH. Chuyển hóa qua gan giảm đáng kể, tăng nồng độ tolterodine và nguy cơ tác dụng phụ.",
                "notes": "Tolterodine chuyển hóa qua gan (CYP3A4, CYP2D6). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và nguy cơ tác dụng phụ. CHỐNG CHỈ ĐỊNH ở suy gan nặng."
            },
            "overdose_management": {
                "symptoms": [
                    "Rối loạn nhận thức nặng, mê sảng",
                    "Bí tiểu nặng",
                    "Táo bón nặng",
                    "Mờ mắt nặng",
                    "Nhịp tim nhanh",
                    "Khô miệng nặng"
                ],
                "antidote": "Physostigmine (anticholinesterase) - có thể dùng trong trường hợp nặng",
                "treatment": [
                    "Ngừng ngay tolterodine",
                    "Rửa dạ dày nếu mới uống <1 giờ",
                    "Than hoạt tính",
                    "Nếu rối loạn nhận thức nặng: Physostigmine 1-2mg IV (thận trọng)",
                    "Điều trị bí tiểu: Đặt ống thông tiểu nếu cần",
                    "Điều trị táo bón: Thuốc nhuận tràng, thụt tháo nếu cần",
                    "Theo dõi: Dấu hiệu sinh tồn, dấu hiệu rối loạn nhận thức"
                ],
                "monitoring": "Theo dõi dấu hiệu sinh tồn, dấu hiệu rối loạn nhận thức, bí tiểu, táo bón cho đến khi hồi phục."
            },
            "reversal_agents": {
                "available": True,
                "agents": ["Physostigmine (anticholinesterase) - có thể dùng trong trường hợp nặng"]
            },
            "administration_instructions": {
                "oral": {
                    "with_food": "Uống với hoặc không thức ăn. Có thể uống với thức ăn để giảm tác dụng phụ tiêu hóa.",
                    "timing": "Immediate-release: 2mg PO x 2 lần/ngày. Extended-release: 4mg PO x 1 lần/ngày. Giảm liều xuống 1mg x 2 lần/ngày nếu dùng với CYP3A4 inhibitors.",
                    "notes": "QUAN TRỌNG: 1) Chọn lọc hơn oxybutynin, ít tác dụng phụ hơn, 2) Extended-release ít tác dụng phụ hơn immediate-release, 3) Theo dõi rối loạn nhận thức (ít hơn oxybutynin), 4) CHỐNG CHỈ ĐỊNH ở bí tiểu và tăng nhãn áp góc đóng, 5) Giảm liều khi dùng với CYP3A4 inhibitors."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Tolterodine (Detrol)",
                    "AUA Guidelines - Overactive Bladder",
                    "UpToDate - Tolterodine: Drug Information",
                    "Medscape - Tolterodine Drug Reference"
                ],
                "last_updated": "2025-02-18",
                "evidence_level": "A - Dựa trên FDA drug labels, AUA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
            },
            "black_box_warnings": "Cần xem xét black box warnings",
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": [],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [],
            },
            "guideline_tags": [
                "FDA Drug Information",
                "UpToDate Drug Information",
            ]
        },

}

__all__ = ['OVERACTIVE_BLADDER_DRUGS']
