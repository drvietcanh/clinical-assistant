"""Gastrointestinal Drugs - Antispasmodics for Colon and IBS
Mebeverine, Trimebutine, Hyoscine butylbromide"""

ANTISPASMODICS_DRUGS = {
    "Hyoscine butylbromide": {
        "group": "Gastrointestinal - Antispasmodic (Anticholinergic)",
        "vietnamese_name": "Hyoscine butylbromide, Buscopan",
        "administration": ["PO", "IV", "IM"],
        "indications": [
            "Co thắt cơ trơn đường tiêu hóa (dạ dày, ruột, đại tràng) gây đau quặn",
            "Co thắt đường mật, tiết niệu (hỗ trợ giảm đau)",
            "Đau bụng quặn do IBS hoặc co thắt đại tràng",
        ],
        "contraindications": [
            "Glaucoma góc đóng",
            "Phì đại tuyến tiền liệt có bí tiểu",
            "Tắc ruột cơ học, liệt ruột",
            "Nhịp tim nhanh chưa kiểm soát",
        ],
        "dosage": {
            "adult_po": "10–20mg PO x 3–5 lần/ngày (tối đa ~100mg/ngày tùy hướng dẫn quốc gia)",
            "adult_iv_im": "20mg IV/IM, có thể lặp lại sau 30 phút nếu cần (tối đa 100mg/ngày)",
            "notes": "Dùng ngắn hạn cho cơn đau quặn; PO hoặc IV/IM tùy mức độ.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều, nhưng thận trọng nếu dùng IV/IM nhiều lần",
            "under_30": "Thận trọng, dữ liệu hạn chế",
        },
        "side_effects": [
            "Khô miệng",
            "Nhìn mờ",
            "Táo bón",
            "Giữ tiểu, bí tiểu (đặc biệt ở nam lớn tuổi có BPH)",
            "Tim nhanh, đánh trống ngực",
            "Lú lẫn (nhạy cảm ở người già, hiếm với dạng butylbromide do ít qua BBB)",
        ],
        "interactions": [
            "Thuốc kháng cholinergic khác (TCAs, thuốc kháng H1 thế hệ 1): tăng tác dụng phụ kháng cholinergic",
            "Thuốc tăng nhịp tim (β-agonists): có thể tăng nhịp tim nhiều hơn",
        ],
        "pregnancy": "B/C – thường dùng ngắn hạn, lợi ích > nguy cơ",
        "mechanism_of_action": (
            "Hyoscine butylbromide là dẫn xuất ammonium bậc 4 của scopolamine, "
            "tác dụng kháng muscarinic (anticholinergic) chủ yếu ở ngoại vi trên cơ trơn "
            "dạ dày-ruột, đường mật, tiết niệu. Giảm co thắt cơ trơn và giảm đau quặn. "
            "Do là ammonium bậc 4 nên hầu như không qua hàng rào máu não → ít tác dụng trung ương hơn atropine/scopolamine.",
        ),
        "monitoring": [
            "Triệu chứng đau bụng quặn",
            "Mạch, huyết áp (IV/IM)",
            "Dấu hiệu bí tiểu ở bệnh nhân BPH",
            "Dấu hiệu khô miệng, nhìn mờ, táo bón nặng",
        ],
        "precautions": [
            "Tránh dùng kéo dài ở người già do nhạy cảm với anticholinergic (lú lẫn, té ngã)",
            "Không dùng nếu nghi ngờ bụng cấp ngoại khoa chưa rõ chẩn đoán (có thể che lấp triệu chứng)",
            "Thận trọng ở bệnh nhân BPH, glaucoma góc đóng, nhịp nhanh",
        ],
        "pharmacokinetics": {
            "half_life": "4–6 giờ",
            "onset": "15–30 phút (PO), nhanh hơn với IV/IM",
            "duration": "3–6 giờ",
            "protein_binding": "Cao",
            "clearance": "Chuyển hóa qua gan và thải qua mật/thận; hấp thu đường uống không hoàn toàn",
        },
        "storage": "Bảo quản ở nhiệt độ phòng, tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Thuốc kháng cholinergic khác (TCAs, kháng H1 thế hệ 1, antipsychotics cổ điển)",
                    "mechanism": "Tác dụng cộng dồn kháng cholinergic",
                    "effect": "Tăng nguy cơ bí tiểu, táo bón nặng, nhìn mờ, lú lẫn",
                    "management": "Thận trọng, tránh phối hợp nếu có thể, đặc biệt ở người già.",
                },
                {
                    "drug": "Thuốc tăng nhịp tim (β-agonists)",
                    "mechanism": "Tác dụng cộng dồn tăng nhịp tim",
                    "effect": "Tăng nhịp tim nhiều hơn",
                    "management": "Thận trọng, theo dõi mạch."
                }
            ],
            "minor": [],
        },
        "drug_interactions_detail": {
            "major": [],
            "moderate": [
                {
                    "drug": "Thuốc kháng cholinergic khác (TCAs, kháng H1 thế hệ 1, antipsychotics cổ điển)",
                    "mechanism": "Tác dụng cộng dồn kháng cholinergic",
                    "effect": "Tăng nguy cơ bí tiểu, táo bón nặng, nhìn mờ, lú lẫn",
                    "management": "Thận trọng, tránh phối hợp nếu có thể, đặc biệt ở người già.",
                }
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Glaucoma góc đóng",
                "Bí tiểu do BPH",
                "Tắc ruột cơ học, liệt ruột",
                "Nhịp nhanh chưa kiểm soát nặng",
            ],
            "tương_đối": [
                "BPH không bí tiểu (nguy cơ bí tiểu)",
                "Bệnh tim mạch (nhịp nhanh, thiếu máu cơ tim)",
                "Người cao tuổi (nguy cơ lú lẫn, té ngã)",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu hạn chế; thường dùng ngắn hạn dưới giám sát bác sĩ khi lợi ích rõ ràng.",
            "lactation": {
                "safety": "Caution",
                "details": "Chưa rõ bài tiết vào sữa; nguy cơ lý thuyết gây khô miệng, bí tiểu ở trẻ.",
                "recommendation": "Dùng thận trọng, tránh kéo dài; theo dõi trẻ nếu dùng.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng, không nhất thiết chỉnh liều",
            "moderate": "Thận trọng, tránh liều cao lặp lại IV/IM",
            "severe": "Tránh dùng lặp lại, cân nhắc thuốc khác",
            "notes": "Chuyển hóa qua gan; suy gan có thể tăng phơi nhiễm.",
        },
        "overdose_management": {
            "symptoms": [
                "Khô miệng rất nhiều, nhìn mờ",
                "Tim nhanh, sốt nhẹ",
                "Bí tiểu, táo bón nặng",
                "Trong quá liều rất cao: lú lẫn, kích động (hiếm do ít qua BBB)",
            ],
            "antidote": "Không có antidote đặc hiệu; trong ngộ độc anticholinergic nặng có thể cân nhắc physostigmine (chuyên khoa).",
            "treatment": [
                "Ngừng thuốc",
                "Hỗ trợ: bù dịch, làm mát nếu sốt, điều trị bí tiểu (đặt sonde nếu cần)",
                "Theo dõi mạch, huyết áp, ý thức",
            ],
            "monitoring": "Mạch, huyết áp, ý thức, lượng nước tiểu.",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống cùng hoặc không với thức ăn.",
                "timing": "Thường 3–5 lần/ngày khi có cơn đau quặn; không nên dùng kéo dài liều cao.",
            },
            "iv": {
                "reconstitution": "Dùng dung dịch tiêm sẵn; có thể tiêm chậm trực tiếp hoặc pha loãng trong NaCl 0,9%.",
                "infusion_rate": "Tiêm tĩnh mạch chậm trong vài phút để tránh tụt huyết áp hoặc tim nhanh quá mức.",
                "compatibility": ["NaCl 0,9%", "D5W"],
                "incompatibility": [],
                "notes": "Chỉ dùng IV/IM trong cơn đau quặn nặng; chuyển sang PO khi ổn định.",
            },
        },
        "references": {
            "primary_sources": [
                "BNF – Hyoscine butylbromide monograph",
                "ESNM guidelines – Management of IBS and functional abdominal pain",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "Moderate – rộng rãi trong thực hành lâm sàng",
        },
              "black_box_warnings": None,
          "black_box_warnings": None,
          "black_box_warnings": None,
          "black_box_warnings": None,
          "black_box_warnings": None,
          "black_box_warnings": None,
          "black_box_warnings": None,
          "black_box_warnings": None,
          "black_box_warnings": None,
          "black_box_warnings": None,
          "black_box_warnings": None,
          "black_box_warnings": None,
          "black_box_warnings": None,
          "black_box_warnings": None,
          "black_box_warnings": None,
          "black_box_warnings": None,
          "black_box_warnings": None,
          "black_box_warnings": "Không có",
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
    "Mebeverine": {
        "group": "Gastrointestinal - Antispasmodic (Direct smooth muscle relaxant)",
        "vietnamese_name": "Mebeverine, Duspatalin",
        "administration": ["PO"],
        "indications": [
            "Hội chứng ruột kích thích (IBS) với đau quặn bụng, đầy hơi",
            "Co thắt đại tràng, dạ dày-ruột chức năng",
        ],
        "contraindications": [
            "Dị ứng mebeverine",
            "Liệt ruột mạn (hiếm, thận trọng)",
        ],
        "dosage": {
            "adult_standard": "135mg PO x 3 lần/ngày trước bữa ăn, hoặc 200mg viên giải phóng chậm x 2 lần/ngày",
            "notes": "Nuốt nguyên viên, không nghiền/nhai; dùng trước bữa ăn khoảng 20 phút.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều",
            "under_30": "Thận trọng, dữ liệu hạn chế nhưng không cần chỉnh liều thường quy",
        },
        "side_effects": [
            "Buồn nôn nhẹ",
            "Đau đầu, chóng mặt (hiếm)",
            "Phản ứng quá mẫn da (phát ban, ngứa – rất hiếm)",
        ],
        "interactions": [
            "Ít tương tác lâm sàng có ý nghĩa; không có tương tác CYP đáng kể được ghi nhận",
        ],
        "pregnancy": "C – dùng khi lợi ích > nguy cơ; thường tránh trong 3 tháng đầu",
        "mechanism_of_action": (
            "Mebeverine là thuốc giãn cơ trơn chọn lọc đường tiêu hóa, có tác dụng trực tiếp trên cơ trơn ruột "
            "thông qua điều hòa kênh ion (Na+, Ca2+), giảm co thắt mà không gây liệt ruột và không có tác dụng kháng cholinergic "
            "(không gây khô miệng, bí tiểu...). Không ảnh hưởng nhu động sinh lý, chủ yếu giảm co thắt bất thường."
        ),
        "monitoring": [
            "Triệu chứng IBS: đau bụng, đầy hơi, rối loạn phân",
            "Dấu hiệu dị ứng da hiếm gặp",
        ],
        "precautions": [
            "Nếu đau bụng mới xuất hiện, nặng dần, sụt cân, sốt, thiếu máu… cần loại trừ nguyên nhân thực thể trước khi dùng lâu dài",
            "Không dùng thay thế đánh giá chẩn đoán (nội soi, siêu âm…) khi có dấu hiệu báo động",
        ],
        "pharmacokinetics": {
            "half_life": "2–5 giờ (dạng thường), dài hơn với dạng giải phóng chậm",
            "onset": "Trong vòng 1–2 giờ",
            "duration": "Vài giờ; dạng retard duy trì cả ngày với liều 2 lần/ngày",
            "protein_binding": "Cao, gắn đáng kể vào protein huyết tương",
            "clearance": "Chuyển hóa qua gan thành chất không hoạt tính, thải qua thận",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15–30°C), tránh ẩm.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "drug_interactions_detail": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": ["Dị ứng mebeverine hoặc tá dược"],
            "tương_đối": [
                "Nghi ngờ tắc ruột cơ học hoặc liệt ruột (cần loại trừ trước)",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu người còn hạn chế; dùng khi lợi ích lâm sàng rõ ràng, tránh nếu có lựa chọn an toàn hơn.",
            "lactation": {
                "safety": "Caution",
                "details": "Lượng bài tiết vào sữa không rõ; chưa ghi nhận tác dụng phụ rõ ràng ở trẻ.",
                "recommendation": "Có thể dùng nếu cần, theo dõi trẻ về thay đổi phân hoặc kích thích.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều, nhưng thận trọng",
            "moderate": "Thận trọng, cân nhắc liều thấp",
            "severe": "Tránh dùng nếu không theo dõi chặt",
            "notes": "Chuyển hóa qua gan; chưa có khuyến cáo liều cụ thể nhưng nên thận trọng.",
        },
        "overdose_management": {
            "symptoms": [
                "Chủ yếu là tăng tác dụng phụ tiêu hóa (buồn nôn, chóng mặt)",
            ],
            "antidote": "Không có; điều trị hỗ trợ",
            "treatment": [
                "Điều trị triệu chứng, theo dõi",
            ],
            "monitoring": "Dấu hiệu sinh tồn, triệu chứng thần kinh nếu có.",
        },
        "reversal_agents": {"available": False, "agents": [], "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay. Physostigmine có thể đối kháng tác dụng anticholinergic nhưng thận trọng."},
        "administration_instructions": {
            "oral": {
                "with_food": "Dùng trước bữa ăn khoảng 20 phút để giảm co thắt sau ăn.",
                "timing": "2–3 lần/ngày tùy chế phẩm (thường sáng–trưa–tối hoặc 2 lần/ngày với dạng retard).",
            }
        },
        "references": {
            "primary_sources": [
                "NICE IBS guideline – antispasmodic therapy",
                "BNF – Mebeverine monograph",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "Moderate – thường dùng, dữ liệu thực hành phong phú",
        },
             "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": "Không có",
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

    "Trimebutine": {
        "group": "Gastrointestinal - Antispasmodic & Motility Modulator",
        "vietnamese_name": "Trimebutine, Debridat",
        "administration": ["PO"],
        "indications": [
            "Hội chứng ruột kích thích (IBS) với tiêu chảy hoặc táo bón kèm đau quặn bụng",
            "Rối loạn nhu động ruột chức năng, đau quặn đại tràng",
        ],
        "contraindications": [
            "Dị ứng trimebutine",
            "Trẻ <2–3 tuổi (tùy khuyến cáo quốc gia)",
        ],
        "dosage": {
            "adult_standard": "100–200mg PO x 3 lần/ngày (tối đa ~600mg/ngày), dùng trước bữa ăn",
            "notes": "Có dạng siro cho trẻ em; điều chỉnh liều theo cân nặng theo hướng dẫn sản phẩm.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, có thể cân nhắc giảm liều nếu dùng kéo dài",
            "under_30": "Thận trọng, dữ liệu hạn chế",
        },
        "side_effects": [
            "Buồn nôn, khô miệng nhẹ",
            "Buồn ngủ, chóng mặt (hiếm, liên quan hoạt tính opioid ngoại biên nhẹ)",
            "Táo bón hoặc tiêu chảy (thường thoáng qua)",
        ],
        "interactions": [
            "Ít tương tác CYP đáng kể; thận trọng khi phối hợp với thuốc ức chế thần kinh trung ương do tác dụng an thần nhẹ.",
        ],
        "pregnancy": "C – dùng khi lợi ích > nguy cơ",
        "mechanism_of_action": (
            "Trimebutine là chất điều hòa nhu động ruột và chống co thắt thông qua tác động lên thụ thể opioid ngoại biên "
            "(µ, κ, δ) ở thành ruột, điều chỉnh phóng thích acetylcholine và các chất dẫn truyền khác. "
            "Nó có thể ức chế hoặc kích thích nhu động tùy theo tình trạng nền (bình thường hóa nhu động), "
            "hữu ích trong IBS cả thể táo bón và tiêu chảy."
        ),
        "monitoring": [
            "Triệu chứng đau bụng, số lần đi ngoài, tính chất phân",
        ],
        "precautions": [
            "Nếu có triệu chứng báo động (sụt cân, chảy máu tiêu hóa, thiếu máu, sốt, tiêu chảy đêm) cần loại trừ nguyên nhân thực thể trước dùng lâu dài",
            "Thận trọng khi lái xe/vận hành máy móc nếu có buồn ngủ, chóng mặt",
        ],
        "pharmacokinetics": {
            "half_life": "1–5 giờ (tùy chất chuyển hóa)",
            "onset": "Trong vài giờ đầu",
            "duration": "Cần dùng 2–3 lần/ngày để duy trì",
            "protein_binding": "Cao (trên 90%)",
            "clearance": "Chuyển hóa qua gan, thải qua thận và mật",
        },
        "storage": "Bảo quản ở nhiệt độ phòng, tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Thuốc ức chế thần kinh trung ương",
                    "mechanism": "Tác dụng cộng dồn an thần",
                    "effect": "Tăng buồn ngủ, chóng mặt",
                    "management": "Thận trọng khi phối hợp, đặc biệt khi lái xe/vận hành máy móc."
                }
            ],
            "minor": [],
        },
        "drug_interactions_detail": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": ["Dị ứng trimebutine hoặc tá dược"],
            "tương_đối": [
                "Suy gan hoặc thận trung bình–nặng (thận trọng)",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu hạn chế; chỉ dùng khi thật sự cần thiết.",
            "lactation": {
                "safety": "Caution",
                "details": "Chưa rõ bài tiết vào sữa; ưu tiên thuốc khác nếu có.",
                "recommendation": "Nếu dùng, theo dõi trẻ về thay đổi phân hoặc an thần bất thường.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều rõ ràng, nhưng thận trọng",
            "moderate": "Xem xét giảm liều hoặc kéo dài khoảng cách",
            "severe": "Tránh dùng nếu có thể",
            "notes": "Chuyển hóa qua gan; suy gan có thể tăng phơi nhiễm.",
        },
        "overdose_management": {
            "symptoms": [
                "Tăng buồn ngủ, chóng mặt, rối loạn tiêu hóa",
            ],
            "antidote": "Không có; điều trị hỗ trợ",
            "treatment": [
                "Theo dõi dấu hiệu sinh tồn",
                "Điều trị triệu chứng (bù dịch nếu tiêu chảy nhiều)",
            ],
            "monitoring": "Ý thức, huyết áp, mạch, hô hấp.",
        },
        "reversal_agents": {"available": False, "agents": [], "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay. Physostigmine có thể đối kháng tác dụng anticholinergic nhưng thận trọng."},
        "administration_instructions": {
            "oral": {
                "with_food": "Dùng trước bữa ăn để giảm đau quặn sau ăn.",
                "timing": "Thường 3 lần/ngày (sáng–trưa–tối).",
            }
        },
        "references": {
            "primary_sources": [
                "NICE IBS guideline – antispasmodic options",
                "BNF – Trimebutine monograph",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "Moderate – sử dụng rộng rãi trong IBS tại nhiều quốc gia",
        },
              "black_box_warnings": None,
          "black_box_warnings": None,
          "black_box_warnings": None,
          "black_box_warnings": None,
          "black_box_warnings": None,
          "black_box_warnings": None,
          "black_box_warnings": None,
          "black_box_warnings": None,
          "black_box_warnings": None,
          "black_box_warnings": None,
          "black_box_warnings": None,
          "black_box_warnings": None,
          "black_box_warnings": None,
          "black_box_warnings": None,
          "black_box_warnings": "Không có",
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

__all__ = ["ANTISPASMODICS_DRUGS"]


