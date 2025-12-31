"""
Vasodilators - Vasodilating Agents
"""

VASODILATORS = {
    "Hydralazine": {
        "group": "Cardiovascular - Direct Vasodilator",
        "vietnamese_name": "Hydralazine, Apresoline",
        "administration": ["PO", "IV", "IM"],
        "indications": [
            "Tăng huyết áp",
            "Suy tim (kết hợp với nitrate)",
            "Cơn tăng huyết áp",
            "Tiền sản giật/sản giật"
        ],
        "contraindications": [
            "Dị ứng hydralazine",
            "Bệnh động mạch vành nặng",
            "Bệnh van tim (hẹp động mạch chủ, hẹp động mạch phổi)",
            "Lupus ban đỏ hệ thống (SLE)"
        ],
        "dosage": {
            "adult_po": "10-25mg x 2-4 lần/ngày, tăng dần đến 200mg/ngày",
            "adult_iv_im": "10-20mg IV/IM mỗi 4-6 giờ (cơn tăng huyết áp)",
            "adult_heart_failure": "25-50mg x 3-4 lần/ngày (kết hợp với isosorbide dinitrate)",
            "notes": "Khởi đầu với liều thấp, tăng dần. Có thể gây lupus-like syndrome với liều cao kéo dài"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng, có thể cần giảm liều"
        },
        "side_effects": [
            "Nhức đầu (phổ biến)",
            "Nhịp tim nhanh phản ứng (tachycardia)",
            "Đỏ mặt, đỏ bừng",
            "Chóng mặt",
            "Hạ huyết áp",
            "Lupus-like syndrome (liều cao, dùng lâu dài)",
            "Viêm đa khớp",
            "Sốt",
            "Phát ban"
        ],
        "interactions": [
            "Thuốc hạ huyết áp khác: tăng tác dụng",
            "MAO inhibitors: tăng tác dụng hạ huyết áp",
            "NSAIDs: giảm hiệu quả hydralazine"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Hydralazine là direct-acting vasodilator, giãn trực tiếp cơ trơn động mạch (chủ yếu arterioles) bằng cách mở kênh K+ và ức chế IP3 (inositol triphosphate) pathway, dẫn đến giảm Ca2+ nội bào và thư giãn cơ trơn mạch máu. Hydralazine chủ yếu giãn động mạch (giảm hậu gánh), ít ảnh hưởng đến tĩnh mạch (không giảm tiền gánh). Kết quả: giảm huyết áp, giảm hậu gánh tim, tăng cung lượng tim. Hydralazine gây nhịp tim nhanh phản ứng (do hạ huyết áp kích thích baroreceptor reflex) và tăng renin-angiotensin-aldosterone system (RAAS), nên thường dùng kết hợp với beta-blocker hoặc diuretic. Trong suy tim, hydralazine kết hợp với isosorbide dinitrate (BiDil) đã được chứng minh giảm tử vong ở bệnh nhân suy tim người Mỹ gốc Phi.",
        "monitoring": [
            "Huyết áp - hạ huyết áp là tác dụng mong muốn nhưng cần tránh hạ quá mức",
            "Nhịp tim - nhịp tim nhanh phản ứng phổ biến, có thể cần beta-blocker",
            "Dấu hiệu lupus-like syndrome: sốt, đau khớp, phát ban, viêm màng phổi (nếu dùng liều cao >200mg/ngày, kéo dài >6 tháng)",
            "ANA (antinuclear antibody) - kiểm tra nếu có triệu chứng lupus-like",
            "Chức năng thận - hydralazine có thể gây viêm thận kẽ (hiếm)",
            "Triệu chứng suy tim - đánh giá hiệu quả khi dùng kết hợp với nitrate"
        ],
        "precautions": [
            "Nhịp tim nhanh phản ứng - phổ biến, có thể cần beta-blocker để chống lại",
            "Lupus-like syndrome - nguy cơ tăng với liều cao (>200mg/ngày) và dùng lâu dài (>6 tháng), đặc biệt ở người chậm acetylator",
            "CHỐNG CHỈ ĐỊNH trong bệnh động mạch vành nặng - nhịp tim nhanh có thể làm nặng thiếu máu cơ tim",
            "CHỐNG CHỈ ĐỊNH trong hẹp động mạch chủ/phổi nặng - giảm hậu gánh có thể làm nặng hẹp",
            "Khởi đầu với liều thấp, tăng dần để tránh hạ huyết áp quá mức",
            "Thận trọng ở bệnh nhân có tiền sử SLE - có thể làm nặng bệnh",
            "Trong suy tim: dùng kết hợp với isosorbide dinitrate (BiDil) - đã được chứng minh giảm tử vong",
            "NSAIDs có thể giảm hiệu quả - tránh dùng cùng nếu có thể",
            "Uống với thức ăn hoặc không (không ảnh hưởng hấp thu đáng kể)"
        ],
        "pharmacokinetics": {
            "half_life": "2-8 giờ (thay đổi theo acetylator status)",
            "onset": "20-30 phút (PO), 5-20 phút (IV)",
            "duration": "2-6 giờ",
            "protein_binding": "85-90%",
            "clearance": "Gan: chuyển hóa qua N-acetylation (phụ thuộc vào acetylator status - fast vs slow acetylator). Thận: bài tiết một phần. Slow acetylators có half-life dài hơn và nguy cơ lupus-like syndrome cao hơn."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín. Dạng tiêm: bảo quản ở nhiệt độ phòng, tránh đông lạnh.",
        "black_box_warnings": "Có thể gây lupus-like syndrome với liều cao (>200mg/ngày) và dùng lâu dài (>6 tháng), đặc biệt ở người chậm acetylator. Nguy cơ tăng ở phụ nữ và người Mỹ gốc Phi. Ngừng ngay nếu có triệu chứng lupus-like (sốt, đau khớp, phát ban, viêm màng phổi).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "MAO inhibitors (phenelzine, tranylcypromine)",
                    "mechanism": "MAO inhibitors ức chế chuyển hóa catecholamines, tác dụng cộng dồn với hydralazine",
                    "effect": "Tăng tác dụng hạ huyết áp, có thể gây hạ huyết áp nghiêm trọng",
                    "management": "Tránh dùng cùng. Nếu cần, thận trọng và theo dõi huyết áp chặt chẽ."
                }
            ],
            "moderate": [
                {
                    "drug": "Thuốc hạ huyết áp khác (ACE inhibitors, ARBs, Beta-blockers, Diuretics)",
                    "mechanism": "Tác dụng cộng dồn hạ huyết áp",
                    "effect": "Tăng nguy cơ hạ huyết áp quá mức",
                    "management": "Thận trọng. Theo dõi huyết áp chặt chẽ. Có thể cần giảm liều các thuốc hạ huyết áp khác."
                },
                {
                    "drug": "NSAIDs (ibuprofen, naproxen, indomethacin)",
                    "mechanism": "NSAIDs ức chế prostaglandin, làm giảm tác dụng giãn mạch của hydralazine",
                    "effect": "Giảm hiệu quả hạ huyết áp của hydralazine",
                    "management": "Tránh dùng cùng nếu có thể. Theo dõi huyết áp. Có thể cần tăng liều hydralazine."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng hydralazine",
                "Bệnh động mạch vành nặng - nhịp tim nhanh có thể làm nặng thiếu máu cơ tim",
                "Hẹp động mạch chủ nặng - giảm hậu gánh có thể làm nặng hẹp",
                "Hẹp động mạch phổi nặng - giảm hậu gánh có thể làm nặng hẹp",
                "Lupus ban đỏ hệ thống (SLE) - có thể làm nặng bệnh"
            ],
            "tương_đối": [
                "Suy tim nặng - thận trọng, có thể cần dùng kết hợp với nitrate",
                "Bệnh thận - thận trọng, có thể gây viêm thận kẽ (hiếm)",
                "Có thai - category C, thận trọng",
                "Người chậm acetylator - tăng nguy cơ lupus-like syndrome"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Hydralazine là category C. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ. Thường dùng trong tiền sản giật/sản giật. Thận trọng, đặc biệt trong tam cá nguyệt thứ ba (có thể gây hạ huyết áp ở mẹ và thai nhi).",
            "lactation": {
                "safety": "Compatible",
                "details": "Hydralazine bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Dùng liều thấp nhất hiệu quả."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Hydralazine chuyển hóa ở gan nhưng suy gan nhẹ không ảnh hưởng đáng kể.",
            "moderate": "Thận trọng, có thể cần giảm liều. Chuyển hóa có thể giảm ở suy gan trung bình.",
            "severe": "Thận trọng, giảm liều. Chuyển hóa giảm ở suy gan nặng, tăng nguy cơ tích lũy.",
            "notes": "Hydralazine chuyển hóa ở gan qua N-acetylation. Suy gan có thể ảnh hưởng đến chuyển hóa, đặc biệt ở người chậm acetylator."
        },
        "overdose_management": {
            "symptoms": [
                "Hạ huyết áp nghiêm trọng, ngất",
                "Nhịp tim nhanh",
                "Nhức đầu nặng",
                "Chóng mặt, buồn nôn, nôn",
                "Shock, tử vong"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ cho hạ huyết áp.",
            "treatment": [
                "Ngừng hydralazine ngay lập tức",
                "Đặt bệnh nhân nằm ngửa, nâng chân cao",
                "Truyền dịch nếu cần (normal saline)",
                "Nếu hạ huyết áp nặng: thuốc vận mạch (norepinephrine, phenylephrine)",
                "Theo dõi huyết áp, nhịp tim liên tục",
                "Hỗ trợ hô hấp nếu cần"
            ],
            "monitoring": "Huyết áp, nhịp tim, dấu hiệu sinh tồn"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Không ảnh hưởng hấp thu đáng kể.",
                "timing": "Uống 2-4 lần/ngày tùy liều. Khởi đầu với liều thấp (10-25mg x 2 lần/ngày), tăng dần đến liều hiệu quả."
            },
            "iv": {
                "reconstitution": "Hydralazine IV: 20mg pha với 10ml NaCl 0.9% hoặc D5W",
                "infusion_rate": "Tiêm tĩnh mạch chậm trong 1-2 phút hoặc truyền trong 10-20 phút",
                "compatibility": ["NaCl 0.9%", "D5W"],
                "incompatibility": [],
                "notes": "Dùng cho cơn tăng huyết áp. Chuyển sang PO sớm nhất có thể."
            },
            "im": {
                "reconstitution": "Hydralazine IM: 10-20mg tiêm bắp",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Có thể tiêm bắp nếu không có đường tĩnh mạch."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Hydralazine (Apresoline)",
                "UpToDate - Hydralazine: Drug Information",
                "A-HeFT Trial - New England Journal of Medicine (BiDil in heart failure)",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A - FDA approved, large RCT (A-HeFT trial for heart failure)"
        }
    },
    
    "Isosorbide mononitrate": {
        "group": "Cardiovascular - Nitrate",
        "vietnamese_name": "Isosorbide mononitrate, Imdur",
        "administration": ["PO"],
        "indications": [
            "Đau thắt ngực (phòng ngừa)",
            "Suy tim (giảm tiền gánh)",
            "Đau thắt ngực ổn định"
        ],
        "contraindications": [
            "Dị ứng nitrate",
            "Hạ huyết áp nặng",
            "Shock",
            "Dùng sildenafil/tadalafil/vardenafil (trong 24-48h)",
            "Tăng áp lực nội sọ",
            "Thiếu máu nặng"
        ],
        "dosage": {
            "adult_angina_immediate": "10-20mg x 2-3 lần/ngày",
            "adult_angina_extended": "30-120mg x 1 lần/ngày (buổi sáng)",
            "adult_heart_failure": "10-40mg x 2-3 lần/ngày",
            "notes": "Tolerance với nitrate nếu dùng liên tục. Cần khoảng nghỉ nitrate-free 10-14h mỗi ngày"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Nhức đầu (thường gặp, giảm sau vài ngày)",
            "Hạ huyết áp",
            "Chóng mặt",
            "Đỏ mặt",
            "Nhịp tim nhanh phản ứng",
            "Ngất (hiếm)"
        ],
        "interactions": [
            "Sildenafil/Tadalafil/Vardenafil: hạ huyết áp nguy hiểm - chống chỉ định",
            "Rượu: tăng tác dụng hạ huyết áp",
            "Thuốc hạ huyết áp khác: tăng tác dụng"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Isosorbide mononitrate là thuốc nitrate, được chuyển hóa thành nitric oxide (NO) trong tế bào cơ trơn mạch máu. NO kích hoạt guanylate cyclase, làm tăng cGMP (cyclic guanosine monophosphate), dẫn đến thư giãn cơ trơn mạch máu. Isosorbide mononitrate chủ yếu giãn tĩnh mạch (giảm tiền gánh), giảm áp lực đổ đầy thất trái, giảm thể tích tâm thất, và giảm nhu cầu oxy của cơ tim. Giãn động mạch nhẹ (giảm hậu gánh) cũng xảy ra. Kết quả: giảm đau thắt ngực, giảm triệu chứng suy tim, và cải thiện khả năng gắng sức. Isosorbide mononitrate là dẫn xuất mononitrate của isosorbide dinitrate, có thời gian bán thải dài hơn và ít tolerance hơn. Tuy nhiên, tolerance với nitrate vẫn xảy ra nếu dùng liên tục, cần khoảng nghỉ nitrate-free 10-14 giờ mỗi ngày.",
        "monitoring": [
            "Huyết áp - hạ huyết áp là tác dụng phụ phổ biến, đặc biệt khi đứng (hạ huyết áp tư thế)",
            "Nhịp tim - nhịp tim nhanh phản ứng có thể xảy ra (do hạ huyết áp)",
            "Triệu chứng đau thắt ngực - đánh giá hiệu quả phòng ngừa",
            "Triệu chứng suy tim - đánh giá hiệu quả giảm tiền gánh",
            "Nhức đầu - tác dụng phụ phổ biến nhất, thường giảm sau vài ngày",
            "Dấu hiệu tolerance - giảm hiệu quả sau vài tuần dùng liên tục (cần khoảng nghỉ nitrate-free)",
            "Tương tác với sildenafil, tadalafil, vardenafil (chống chỉ định - hạ huyết áp nguy hiểm)"
        ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH với sildenafil, tadalafil, vardenafil trong 24-48 giờ - hạ huyết áp nguy hiểm, có thể gây tử vong",
            "Tolerance với nitrate - nếu dùng liên tục, hiệu quả giảm sau vài tuần, cần khoảng nghỉ nitrate-free 10-14 giờ mỗi ngày",
            "Dạng extended release - dùng 1 lần/ngày vào buổi sáng để có khoảng nghỉ nitrate-free tự nhiên",
            "Dạng immediate release - dùng 2-3 lần/ngày, đảm bảo khoảng nghỉ 10-14 giờ giữa các liều cuối và liều đầu ngày hôm sau",
            "Hạ huyết áp - phổ biến, đặc biệt khi đứng (hạ huyết áp tư thế), tránh đứng dậy đột ngột",
            "Nhức đầu - tác dụng phụ phổ biến nhất, thường tự khỏi sau vài ngày, có thể dùng acetaminophen",
            "Không dùng nếu hạ huyết áp nặng, shock, tăng áp lực nội sọ, thiếu máu nặng",
            "Tránh rượu - tăng tác dụng hạ huyết áp",
            "Thận trọng khi dùng với các thuốc hạ huyết áp khác (tăng tác dụng)",
            "Ngừng đột ngột - có thể gây rebound angina (tăng nguy cơ đau thắt ngực), giảm liều dần dần",
            "Dùng với thức ăn hoặc không (không ảnh hưởng hấp thu)",
            "Không nghiền hoặc nhai dạng extended release (phải uống nguyên viên)"
        ],
        "pharmacokinetics": {
            "half_life": "4-5 giờ (immediate release), 8-10 giờ (extended release)",
            "onset": "15-30 phút (immediate release), 30-60 phút (extended release)",
            "duration": "6-8 giờ (immediate release), 12-24 giờ (extended release)",
            "protein_binding": "<5%",
            "clearance": "Gan: chuyển hóa thành isosorbide và các metabolites không hoạt động. Thận: bài tiết một phần metabolites. Không cần điều chỉnh liều ở suy thận hoặc suy gan."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín. Dạng extended release: bảo quản tương tự, không nghiền hoặc nhai.",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH với sildenafil, tadalafil, vardenafil trong 24-48 giờ. Kết hợp có thể gây hạ huyết áp nghiêm trọng, có thể gây tử vong. Nguy cơ hạ huyết áp nặng, ngất, nhồi máu cơ tim, đột quỵ.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Sildenafil, Tadalafil, Vardenafil (PDE-5 inhibitors)",
                    "mechanism": "Cả hai đều tăng cGMP, tác dụng cộng dồn giãn mạch.",
                    "effect": "Hạ huyết áp nghiêm trọng, có thể gây tử vong, ngất, nhồi máu cơ tim, đột quỵ",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI trong 24-48 giờ. Không dùng cùng."
                }
            ],
            "moderate": [
                {
                    "drug": "Rượu",
                    "mechanism": "Rượu gây giãn mạch, tác dụng cộng dồn với nitrate.",
                    "effect": "Tăng tác dụng hạ huyết áp, tăng nguy cơ ngất",
                    "management": "Tránh rượu khi dùng nitrate."
                },
                {
                    "drug": "Thuốc hạ huyết áp khác (ACE inhibitors, ARBs, Beta-blockers, Diuretics)",
                    "mechanism": "Tác dụng cộng dồn hạ huyết áp.",
                    "effect": "Tăng nguy cơ hạ huyết áp quá mức",
                    "management": "Thận trọng. Theo dõi huyết áp chặt chẽ. Có thể cần giảm liều các thuốc hạ huyết áp khác."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dùng sildenafil, tadalafil, vardenafil trong 24-48 giờ - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI",
                "Hạ huyết áp nặng (systolic <90 mmHg)",
                "Shock",
                "Tăng áp lực nội sọ",
                "Thiếu máu nặng",
                "Dị ứng nitrate"
            ],
            "tương_đối": [
                "Suy tim nặng - thận trọng, có thể cần giảm liều",
                "Hẹp động mạch chủ nặng - thận trọng",
                "Hẹp động mạch phổi nặng - thận trọng",
                "Có thai - category C, thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Isosorbide mononitrate là category C. Không có nghiên cứu đầy đủ ở phụ nữ có thai. Dùng được nếu lợi ích > nguy cơ. Thận trọng, đặc biệt trong tam cá nguyệt thứ ba (có thể gây hạ huyết áp ở mẹ và thai nhi).",
            "lactation": {
                "safety": "Unknown",
                "details": "Không biết isosorbide mononitrate có bài tiết vào sữa mẹ hay không. Thận trọng khi dùng khi cho con bú.",
                "recommendation": "Thận trọng khi dùng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Isosorbide mononitrate chuyển hóa ở gan nhưng suy gan nhẹ không ảnh hưởng đáng kể.",
            "moderate": "Không cần điều chỉnh liều thường quy. Theo dõi đáp ứng điều trị.",
            "severe": "Không cần điều chỉnh liều thường quy. Theo dõi đáp ứng điều trị.",
            "notes": "Isosorbide mononitrate chuyển hóa ở gan thành isosorbide và các metabolites không hoạt động. Suy gan thường không ảnh hưởng đáng kể đến nồng độ."
        },
        "overdose_management": {
            "symptoms": [
                "Hạ huyết áp nghiêm trọng, ngất",
                "Nhức đầu nặng",
                "Chóng mặt, buồn nôn, nôn",
                "Nhịp tim nhanh phản ứng",
                "Methemoglobinemia (hiếm, với liều rất cao)",
                "Shock, tử vong"
            ],
            "antidote": "Methylene blue cho methemoglobinemia nếu có. Điều trị hỗ trợ cho hạ huyết áp.",
            "treatment": [
                "Ngừng isosorbide mononitrate ngay lập tức",
                "Đặt bệnh nhân nằm ngửa, nâng chân cao",
                "Truyền dịch nếu cần (normal saline)",
                "Nếu hạ huyết áp nặng: thuốc vận mạch (norepinephrine, phenylephrine)",
                "Nếu methemoglobinemia: methylene blue 1-2 mg/kg IV",
                "Theo dõi huyết áp, nhịp tim, SpO2 liên tục",
                "Hỗ trợ hô hấp nếu cần"
            ],
            "monitoring": "Huyết áp, nhịp tim, SpO2, dấu hiệu sinh tồn, methemoglobin nếu nghi ngờ methemoglobinemia"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Không ảnh hưởng hấp thu.",
                "timing": "Dạng immediate release: 2-3 lần/ngày, đảm bảo khoảng nghỉ nitrate-free 10-14 giờ. Dạng extended release: 1 lần/ngày vào buổi sáng. KHÔNG nghiền hoặc nhai dạng extended release."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống"
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Isosorbide Mononitrate (Imdur)",
                "UpToDate - Isosorbide Mononitrate: Drug Information",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
            ],
            "last_updated": "2025-02-04",
            "evidence_level": "A - Dựa trên FDA drug labels và dữ liệu lâm sàng"
        }
    },
    
    "Nesiritide": {
        "group": "Cardiovascular - Natriuretic Peptide (Vasodilator)",
        "vietnamese_name": "Nesiritide, Natrecor",
        "administration": ["IV"],
        "indications": [
            "Suy tim cấp mất bù (acute decompensated heart failure) - giảm khó thở",
            "Suy tim với sung huyết phổi nặng"
        ],
        "contraindications": [
            "Dị ứng nesiritide",
            "Hạ huyết áp nặng (systolic BP <90 mmHg)",
            "Sốc tim",
            "Bệnh van tim nặng (hẹp van động mạch chủ, hẹp van hai lá)"
        ],
        "dosage": {
            "adult_loading": "2 mcg/kg IV bolus",
            "adult_maintenance": "0.01 mcg/kg/phút IV infusion",
            "notes": "Truyền liên tục. Theo dõi huyết áp sát. Có thể tăng liều đến 0.03 mcg/kg/phút nếu cần và huyết áp cho phép."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, có thể cần giảm liều",
            "under_30": "Thận trọng, có thể cần giảm liều",
            "hemodialysis": "Thận trọng"
        },
        "side_effects": [
            "Hạ huyết áp (phổ biến, có thể nặng)",
            "Nhịp tim nhanh phản xạ",
            "Nhức đầu",
            "Chóng mặt",
            "Buồn nôn",
            "Rối loạn nhịp tim (hiếm)"
        ],
        "interactions": [
            "Thuốc hạ huyết áp khác: tăng nguy cơ hạ huyết áp",
            "ACE inhibitors: tăng nguy cơ hạ huyết áp"
        ],
        "pregnancy": "C - Thận trọng trong thai kỳ",
        "mechanism_of_action": "Nesiritide là B-type natriuretic peptide (BNP) tái tổ hợp. BNP là hormone được tiết ra từ tâm thất khi có căng thẳng (stretch). Nesiritide gắn với thụ thể natriuretic peptide (NPR-A), kích hoạt guanylate cyclase, làm tăng cGMP, dẫn đến: (1) Giãn tĩnh mạch và động mạch (giảm tiền gánh và hậu gánh), (2) Tăng bài tiết natri qua thận (lợi tiểu), (3) Ức chế hệ renin-angiotensin-aldosterone (RAAS), (4) Ức chế hệ thần kinh giao cảm. Kết quả: giảm áp lực đổ đầy tim, giảm khó thở, cải thiện huyết động trong suy tim cấp. Tác dụng nhanh (khởi phát trong vài phút), thời gian tác dụng ngắn (half-life 18 phút).",
        "monitoring": [
            "Huyết áp liên tục (arterial line nếu có thể) - QUAN TRỌNG",
            "Nhịp tim và ECG",
            "Dấu hiệu cải thiện khó thở",
            "Cân bằng dịch (nước tiểu giờ, cân nặng)",
            "Điện giải (Na+, K+)",
            "Chức năng thận (creatinine, eGFR)"
        ],
        "precautions": [
            "Hạ huyết áp - phổ biến, cần theo dõi sát",
            "CHỐNG CHỈ ĐỊNH nếu hạ huyết áp nặng (systolic BP <90 mmHg)",
            "Thận trọng ở bệnh nhân bệnh van tim nặng (hẹp van động mạch chủ, hẹp van hai lá)",
            "Bù dịch đầy đủ trước khi dùng (trừ sốc tim)",
            "Giảm liều hoặc ngừng nếu hạ huyết áp nặng",
            "Pha trong NS hoặc D5W, truyền qua đường truyền riêng"
        ],
        "pharmacokinetics": {
            "half_life": "18 phút",
            "onset": "Vài phút",
            "duration": "Ngắn (cần truyền liên tục)",
            "protein_binding": "Không đáng kể",
            "clearance": "Thận (thải trừ qua nước tiểu), thời gian bán thải ngắn"
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh. Dung dịch đã pha: dùng trong 24 giờ.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "Thuốc hạ huyết áp khác (ACE inhibitors, ARBs, Nitroglycerin, Hydralazine)",
                    "mechanism": "Tác dụng hạ huyết áp cộng dồn",
                    "effect": "Tăng nguy cơ hạ huyết áp nặng, sốc",
                    "management": "Theo dõi huyết áp sát. Giảm liều các thuốc hạ huyết áp khác nếu cần."
                }
            ],
            "moderate": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng nesiritide",
                "Hạ huyết áp nặng (systolic BP <90 mmHg) - CHỐNG CHỈ ĐỊNH",
                "Sốc tim - CHỐNG CHỈ ĐỊNH",
                "Bệnh van tim nặng (hẹp van động mạch chủ nặng, hẹp van hai lá nặng) - CHỐNG CHỈ ĐỊNH"
            ],
            "tương_đối": [
                "Suy thận nặng - thận trọng, có thể cần giảm liều",
                "Bệnh nhân cao tuổi - tăng nhạy cảm với hạ huyết áp",
                "Dùng với thuốc hạ huyết áp khác - tăng nguy cơ hạ huyết áp"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Nesiritide là thuốc phân loại C. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt trong suy tim cấp nặng.",
            "lactation": {
                "safety": "Unknown",
                "details": "Không biết nesiritide có bài tiết vào sữa mẹ hay không. Thời gian bán thải ngắn (18 phút).",
                "recommendation": "Thận trọng khi cho con bú. Nếu cần, ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Không cần điều chỉnh liều (thải trừ chủ yếu qua thận)",
            "notes": "Nesiritide thải trừ chủ yếu qua thận. Không cần điều chỉnh liều ở bệnh nhân suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Hạ huyết áp nặng, sốc",
                "Nhịp tim nhanh",
                "Rối loạn nhịp tim"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ngay nesiritide nếu đang truyền",
                "Hỗ trợ huyết động: Truyền dịch bolus (NS, LR), thuốc vận mạch (norepinephrine, dopamine) nếu cần",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, ECG liên tục",
                "Hỗ trợ hô hấp nếu cần"
            ],
            "monitoring": "Theo dõi huyết áp, nhịp tim, ECG liên tục cho đến khi hồi phục."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": None,
            "iv": {
                "reconstitution": "Pha trong NS hoặc D5W. Nồng độ thường dùng: 0.01-0.03 mcg/kg/phút.",
                "infusion_rate": "Loading: 2 mcg/kg IV bolus. Maintenance: 0.01 mcg/kg/phút IV infusion. Có thể tăng đến 0.03 mcg/kg/phút nếu cần và huyết áp cho phép.",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
                "incompatibility": [
                    "Không trộn với các thuốc khác. Dùng đường truyền riêng."
                ],
                "notes": "QUAN TRỌNG: 1) Theo dõi huyết áp sát, 2) CHỐNG CHỈ ĐỊNH nếu hạ huyết áp nặng, 3) Bù dịch đầy đủ trước khi dùng."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Nesiritide (Natrecor)",
                "ACC/AHA Guidelines for Heart Failure",
                "UpToDate - Nesiritide: Drug Information",
                "Medscape - Nesiritide Drug Reference"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, ACC/AHA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },
    
    "Nitroglycerin": {
        "group": "Cardiovascular - Nitrate",
        "vietnamese_name": "Nitroglycerin, Nitrostat, Nitro-Bid, Nitro-Dur",
        "administration": ["SL", "IV", "TD", "PO"],
        "indications": [
            "Đau thắt ngực cấp tính (sublingual)",
            "Phòng ngừa đau thắt ngực (topical, oral)",
            "Suy tim cấp với sung huyết phổi (IV)",
            "Cơn tăng huyết áp (IV)",
            "Đau thắt ngực không ổn định (IV)",
            "Nhồi máu cơ tim cấp (IV)"
        ],
        "contraindications": [
            "Dị ứng nitrate",
            "Hạ huyết áp nặng (systolic BP <90 mmHg)",
            "Shock",
            "Dùng sildenafil/tadalafil/vardenafil (trong 24-48h) - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI",
            "Tăng áp lực nội sọ",
            "Thiếu máu nặng",
            "Hẹp động mạch chủ nặng",
            "Hẹp động mạch phổi nặng"
        ],
        "dosage": {
            "adult_sl_acute": "0.3-0.6mg SL, lặp lại mỗi 5 phút tối đa 3 lần",
            "adult_iv_initial": "5-10 mcg/phút IV infusion, tăng dần 5-10 mcg/phút mỗi 3-5 phút",
            "adult_iv_maintenance": "10-200 mcg/phút IV infusion (tối đa 400 mcg/phút)",
            "adult_td_patch": "0.2-0.4mg/giờ, áp 12-14 giờ, nghỉ 10-12 giờ",
            "adult_td_ointment": "0.5-2 inch (1.25-5cm) mỗi 8 giờ",
            "adult_po": "2.5-6.5mg x 3-4 lần/ngày",
            "notes": "Sublingual: dùng cho đau thắt ngực cấp. IV: dùng trong ICU với monitoring. Topical: phòng ngừa đau thắt ngực. Tolerance nếu dùng liên tục - cần khoảng nghỉ nitrate-free 10-14h mỗi ngày."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Nhức đầu (rất phổ biến, đặc biệt với liều đầu tiên)",
            "Hạ huyết áp (phổ biến, có thể nặng)",
            "Chóng mặt, ngất",
            "Đỏ mặt, đỏ bừng",
            "Nhịp tim nhanh phản ứng",
            "Methemoglobinemia (hiếm, với liều rất cao IV)"
        ],
        "interactions": [
            "Sildenafil/Tadalafil/Vardenafil: hạ huyết áp nguy hiểm - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI",
            "Rượu: tăng tác dụng hạ huyết áp",
            "Thuốc hạ huyết áp khác: tăng tác dụng",
            "Heparin: có thể giảm hiệu quả heparin (IV)"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Nitroglycerin là thuốc nitrate, được chuyển hóa thành nitric oxide (NO) trong tế bào cơ trơn mạch máu. NO kích hoạt guanylate cyclase, làm tăng cGMP (cyclic guanosine monophosphate), dẫn đến thư giãn cơ trơn mạch máu. Nitroglycerin chủ yếu giãn tĩnh mạch (giảm tiền gánh), giảm áp lực đổ đầy thất trái, giảm thể tích tâm thất, và giảm nhu cầu oxy của cơ tim. Giãn động mạch nhẹ (giảm hậu gánh) cũng xảy ra. Kết quả: giảm đau thắt ngực, giảm triệu chứng suy tim, và cải thiện khả năng gắng sức. Nitroglycerin có nhiều dạng: (1) Sublingual: tác dụng nhanh (1-3 phút) cho đau thắt ngực cấp, (2) IV: tác dụng nhanh, điều chỉnh liều dễ dàng, dùng trong ICU, (3) Topical (patch, ointment): tác dụng kéo dài, phòng ngừa đau thắt ngực, (4) Oral: tác dụng kéo dài. Tolerance với nitrate xảy ra nếu dùng liên tục, cần khoảng nghỉ nitrate-free 10-14 giờ mỗi ngày.",
        "monitoring": [
            "Huyết áp - hạ huyết áp là tác dụng phụ phổ biến, đặc biệt khi đứng (hạ huyết áp tư thế)",
            "Nhịp tim - nhịp tim nhanh phản ứng có thể xảy ra (do hạ huyết áp)",
            "Triệu chứng đau thắt ngực - đánh giá hiệu quả (sublingual)",
            "Triệu chứng suy tim - đánh giá hiệu quả (IV)",
            "Nhức đầu - tác dụng phụ phổ biến nhất, thường giảm sau vài ngày",
            "Dấu hiệu tolerance - giảm hiệu quả sau vài tuần dùng liên tục (cần khoảng nghỉ nitrate-free)",
            "Methemoglobin nếu dùng IV liều cao kéo dài",
            "Tương tác với sildenafil, tadalafil, vardenafil (chống chỉ định - hạ huyết áp nguy hiểm)"
        ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI với sildenafil, tadalafil, vardenafil trong 24-48 giờ - hạ huyết áp nguy hiểm, có thể gây tử vong",
            "Tolerance với nitrate - nếu dùng liên tục, hiệu quả giảm sau vài tuần, cần khoảng nghỉ nitrate-free 10-14 giờ mỗi ngày",
            "Dạng topical (patch, ointment) - dùng 12-14 giờ, nghỉ 10-12 giờ để tránh tolerance",
            "Dạng IV - CHỈ dùng trong ICU với monitoring huyết động liên tục",
            "Hạ huyết áp - phổ biến, đặc biệt khi đứng (hạ huyết áp tư thế), tránh đứng dậy đột ngột",
            "Nhức đầu - tác dụng phụ phổ biến nhất, thường tự khỏi sau vài ngày, có thể dùng acetaminophen",
            "Sublingual - đặt dưới lưỡi, không nuốt, tác dụng trong 1-3 phút",
            "Không dùng nếu hạ huyết áp nặng, shock, tăng áp lực nội sọ, thiếu máu nặng",
            "Tránh rượu - tăng tác dụng hạ huyết áp",
            "Thận trọng khi dùng với các thuốc hạ huyết áp khác (tăng tác dụng)",
            "Ngừng đột ngột - có thể gây rebound angina (tăng nguy cơ đau thắt ngực), giảm liều dần dần",
            "Bảo quản sublingual: tránh ánh sáng, nhiệt độ, ẩm (mất hiệu quả)"
        ],
        "pharmacokinetics": {
            "half_life": "1-4 phút (sublingual, IV), 1-4 giờ (topical, oral)",
            "onset": "1-3 phút (sublingual), ngay lập tức (IV), 30-60 phút (topical, oral)",
            "duration": "10-30 phút (sublingual), ngắn (IV, cần truyền liên tục), 8-12 giờ (topical), 4-8 giờ (oral)",
            "protein_binding": "60%",
            "clearance": "Gan: chuyển hóa nhanh thành dinitrate và mononitrate (hoạt tính thấp hơn). Thận: bài tiết một phần metabolites. Không cần điều chỉnh liều ở suy thận hoặc suy gan."
        },
        "storage": "Bảo quản sublingual: tránh ánh sáng, nhiệt độ, ẩm (mất hiệu quả). Bảo quản ở nhiệt độ phòng (15-30°C), trong bao bì kín. Dạng IV: bảo vệ khỏi ánh sáng (dùng bọc tối màu). Dạng topical: bảo quản ở nhiệt độ phòng.",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI với sildenafil, tadalafil, vardenafil trong 24-48 giờ. Kết hợp có thể gây hạ huyết áp nghiêm trọng, có thể gây tử vong. Nguy cơ hạ huyết áp nặng, ngất, nhồi máu cơ tim, đột quỵ.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Sildenafil, Tadalafil, Vardenafil (PDE-5 inhibitors)",
                    "mechanism": "Cả hai đều tăng cGMP, tác dụng cộng dồn giãn mạch.",
                    "effect": "Hạ huyết áp nghiêm trọng, có thể gây tử vong, ngất, nhồi máu cơ tim, đột quỵ",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI trong 24-48 giờ. Không dùng cùng."
                }
            ],
            "moderate": [
                {
                    "drug": "Rượu",
                    "mechanism": "Rượu gây giãn mạch, tác dụng cộng dồn với nitrate.",
                    "effect": "Tăng tác dụng hạ huyết áp, tăng nguy cơ ngất",
                    "management": "Tránh rượu khi dùng nitrate."
                },
                {
                    "drug": "Thuốc hạ huyết áp khác (ACE inhibitors, ARBs, Beta-blockers, Diuretics)",
                    "mechanism": "Tác dụng cộng dồn hạ huyết áp.",
                    "effect": "Tăng nguy cơ hạ huyết áp quá mức",
                    "management": "Thận trọng. Theo dõi huyết áp chặt chẽ. Có thể cần giảm liều các thuốc hạ huyết áp khác."
                },
                {
                    "drug": "Heparin",
                    "mechanism": "Nitroglycerin IV có thể giảm hiệu quả heparin (cơ chế không rõ ràng).",
                    "effect": "Giảm hiệu quả chống đông của heparin",
                    "management": "Thận trọng khi dùng cùng. Theo dõi aPTT nếu dùng heparin. Có thể cần tăng liều heparin."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dùng sildenafil, tadalafil, vardenafil trong 24-48 giờ - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI",
                "Hạ huyết áp nặng (systolic <90 mmHg)",
                "Shock",
                "Tăng áp lực nội sọ",
                "Thiếu máu nặng",
                "Hẹp động mạch chủ nặng",
                "Hẹp động mạch phổi nặng",
                "Dị ứng nitrate"
            ],
            "tương_đối": [
                "Suy tim nặng - thận trọng, có thể cần giảm liều",
                "Bệnh mạch vành nặng - thận trọng",
                "Có thai - category C, thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Nitroglycerin là category C. Không có nghiên cứu đầy đủ ở phụ nữ có thai. Dùng được nếu lợi ích > nguy cơ. Thận trọng, đặc biệt trong tam cá nguyệt thứ ba (có thể gây hạ huyết áp ở mẹ và thai nhi).",
            "lactation": {
                "safety": "Unknown",
                "details": "Không biết nitroglycerin có bài tiết vào sữa mẹ hay không. Thận trọng khi dùng khi cho con bú.",
                "recommendation": "Thận trọng khi dùng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Nitroglycerin chuyển hóa ở gan nhưng suy gan nhẹ không ảnh hưởng đáng kể.",
            "moderate": "Không cần điều chỉnh liều thường quy. Theo dõi đáp ứng điều trị.",
            "severe": "Không cần điều chỉnh liều thường quy. Theo dõi đáp ứng điều trị.",
            "notes": "Nitroglycerin chuyển hóa ở gan thành dinitrate và mononitrate. Suy gan thường không ảnh hưởng đáng kể đến nồng độ."
        },
        "overdose_management": {
            "symptoms": [
                "Hạ huyết áp nghiêm trọng, ngất",
                "Nhức đầu nặng",
                "Chóng mặt, buồn nôn, nôn",
                "Nhịp tim nhanh phản ứng",
                "Methemoglobinemia (hiếm, với liều rất cao IV)",
                "Shock, tử vong"
            ],
            "antidote": "Methylene blue cho methemoglobinemia nếu có. Điều trị hỗ trợ cho hạ huyết áp.",
            "treatment": [
                "Ngừng nitroglycerin ngay lập tức",
                "Đặt bệnh nhân nằm ngửa, nâng chân cao",
                "Truyền dịch nếu cần (normal saline)",
                "Nếu hạ huyết áp nặng: thuốc vận mạch (norepinephrine, phenylephrine)",
                "Nếu methemoglobinemia: methylene blue 1-2 mg/kg IV",
                "Theo dõi huyết áp, nhịp tim, SpO2 liên tục",
                "Hỗ trợ hô hấp nếu cần"
            ],
            "monitoring": "Huyết áp, nhịp tim, SpO2, dấu hiệu sinh tồn, methemoglobin nếu nghi ngờ methemoglobinemia"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "sublingual": {
                "technique": "Đặt viên dưới lưỡi, không nuốt. Để tan tự nhiên. Tác dụng trong 1-3 phút.",
                "timing": "Khi có đau thắt ngực: 0.3-0.6mg SL, lặp lại mỗi 5 phút tối đa 3 lần. Nếu không đỡ sau 3 lần: gọi cấp cứu.",
                "notes": "Bảo quản: tránh ánh sáng, nhiệt độ, ẩm (mất hiệu quả). Kiểm tra hạn sử dụng thường xuyên."
            },
            "iv": {
                "reconstitution": "Pha trong D5W hoặc NS. Nồng độ thường dùng: 50-200 mcg/ml. Bảo vệ khỏi ánh sáng (dùng bọc tối màu).",
                "infusion_rate": "Khởi đầu: 5-10 mcg/phút IV infusion. Tăng dần 5-10 mcg/phút mỗi 3-5 phút theo đáp ứng huyết áp. Tối đa: 400 mcg/phút. CHỈ dùng trong ICU với monitoring huyết động liên tục.",
                "compatibility": ["D5W (5% Dextrose)", "NS (0.9% NaCl)"],
                "incompatibility": [
                    "Không trộn với các thuốc khác. Dùng đường truyền riêng."
                ],
                "notes": "QUAN TRỌNG: 1) CHỈ dùng trong ICU với monitoring huyết động liên tục, 2) Bảo vệ khỏi ánh sáng, 3) Chỉnh liều theo huyết áp mục tiêu, 4) Theo dõi methemoglobin nếu dùng liều cao kéo dài."
            },
            "topical": {
                "patch": "Áp patch lên da sạch, khô (ngực, cánh tay). Dùng 12-14 giờ, nghỉ 10-12 giờ để tránh tolerance. Thay đổi vị trí mỗi ngày.",
                "ointment": "Bôi 0.5-2 inch (1.25-5cm) lên da sạch, khô (ngực, cánh tay). Dùng mỗi 8 giờ. Dùng giấy bọc để tránh dính quần áo.",
                "notes": "Dùng 12-14 giờ, nghỉ 10-12 giờ để tránh tolerance với nitrate."
            },
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn.",
                "timing": "Uống 3-4 lần/ngày. Đảm bảo khoảng nghỉ nitrate-free 10-14 giờ mỗi ngày."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Nitroglycerin (Nitrostat, Nitro-Bid, Nitro-Dur)",
                "UpToDate - Nitroglycerin: Drug Information",
                "ACC/AHA Guidelines for Stable Ischemic Heart Disease",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, ACC/AHA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },
    "Nitroprusside": {
        "group": "Cardiovascular - Vasodilator (Hypertensive Emergency)",
        "vietnamese_name": "Nitroprusside, Nipride",
        "administration": ["IV"],
        "indications": [
            "Cơn tăng huyết áp (hypertensive emergency) - cấp cứu",
            "Suy tim cấp với tăng hậu gánh",
            "Phẫu thuật tim (giảm hậu gánh)",
            "Dissection động mạch chủ (aortic dissection)"
        ],
        "contraindications": [
            "Dị ứng nitroprusside",
            "Thiếu máu cục bộ cơ tim cấp (acute coronary syndrome) - thận trọng",
            "Suy thận nặng (nguy cơ thiocyanate độc)",
            "Thiếu cơ sở theo dõi huyết động liên tục - CHỐNG CHỈ ĐỊNH"
        ],
        "dosage": {
            "adult_initial": "0.25-0.5 mcg/kg/phút IV infusion",
            "adult_maintenance": "0.5-10 mcg/kg/phút IV infusion (tối đa 10 mcg/kg/phút)",
            "notes": "CHỈ dùng trong ICU với monitoring huyết động liên tục (arterial line). Chỉnh liều theo huyết áp mục tiêu. Thời gian dùng tối đa 24-48 giờ (nguy cơ thiocyanate độc)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, giảm liều, theo dõi thiocyanate",
            "under_30": "CHỐNG CHỈ ĐỊNH hoặc dùng rất thận trọng, giảm liều, theo dõi thiocyanate sát",
            "hemodialysis": "CHỐNG CHỈ ĐỊNH hoặc dùng rất thận trọng"
        },
        "side_effects": [
            "Hạ huyết áp nặng (phổ biến, có thể gây sốc)",
            "Thiocyanate độc (cyanide toxicity) - nguy hiểm tính mạng nếu dùng kéo dài hoặc liều cao",
            "Nhịp tim nhanh phản xạ",
            "Đau đầu",
            "Chóng mặt",
            "Buồn nôn, nôn",
            "Rối loạn ý thức (do thiocyanate độc)",
            "Co giật (do thiocyanate độc)"
        ],
        "interactions": [
            "Thuốc hạ huyết áp khác: tăng nguy cơ hạ huyết áp",
            "Thuốc gây mê: tăng nguy cơ hạ huyết áp"
        ],
        "pregnancy": "C - Thận trọng trong thai kỳ",
        "mechanism_of_action": "Nitroprusside là thuốc giãn mạch mạnh, tác dụng nhanh. Sau khi vào cơ thể, nitroprusside giải phóng nitric oxide (NO) và cyanide. NO kích hoạt guanylate cyclase, làm tăng cGMP, dẫn đến thư giãn cơ trơn mạch máu. Nitroprusside giãn cả tĩnh mạch (giảm tiền gánh) và động mạch (giảm hậu gánh) mạnh. Kết quả: giảm huyết áp nhanh, giảm áp lực đổ đầy tim, cải thiện huyết động trong suy tim cấp. ĐẶC ĐIỂM: (1) Tác dụng cực nhanh (khởi phát trong vài giây), (2) Thời gian tác dụng ngắn (half-life vài phút), (3) CHỈ dùng trong ICU với monitoring huyết động liên tục, (4) Nguy cơ thiocyanate độc nếu dùng kéo dài (>24-48 giờ) hoặc liều cao (>10 mcg/kg/phút), (5) Cyanide được chuyển hóa thành thiocyanate ở gan (cần thiosulfate), thiocyanate thải trừ qua thận (nguy cơ tích lũy ở suy thận).",
        "monitoring": [
            "Huyết áp động mạch liên tục (arterial line - BẮT BUỘC) - QUAN TRỌNG",
            "Nhịp tim và ECG",
            "Nồng độ thiocyanate trong máu (nếu dùng >24 giờ hoặc liều cao) - MỤC TIÊU: <10 mg/dL, NGUY HIỂM: >20 mg/dL",
            "Dấu hiệu thiocyanate độc (rối loạn ý thức, co giật, buồn nôn, nôn)",
            "Chức năng thận (creatinine, eGFR) - thiocyanate thải trừ qua thận",
            "Acid-base balance (lactate, pH) - thiocyanate độc có thể gây toan lactic"
        ],
        "precautions": [
            "CHỈ dùng trong ICU với monitoring huyết động liên tục (arterial line) - BẮT BUỘC",
            "Hạ huyết áp nặng - phổ biến, cần theo dõi sát",
            "Nguy cơ thiocyanate độc nếu dùng kéo dài (>24-48 giờ) hoặc liều cao (>10 mcg/kg/phút)",
            "CHỐNG CHỈ ĐỊNH hoặc dùng rất thận trọng ở suy thận nặng (thiocyanate tích lũy)",
            "Thời gian dùng tối đa 24-48 giờ (tránh thiocyanate độc)",
            "Pha trong D5W (KHÔNG dùng NS - không ổn định), bảo vệ khỏi ánh sáng (dùng bọc tối màu)",
            "Bù dịch đầy đủ trước khi dùng (trừ sốc tim)",
            "Giảm liều hoặc ngừng nếu hạ huyết áp nặng",
            "Theo dõi nồng độ thiocyanate nếu dùng >24 giờ hoặc liều cao"
        ],
        "pharmacokinetics": {
            "half_life": "Vài phút (nitroprusside), 2-7 ngày (thiocyanate)",
            "onset": "Vài giây",
            "duration": "Ngắn (cần truyền liên tục)",
            "protein_binding": "Không đáng kể",
            "metabolism": "Chuyển hóa thành cyanide và NO. Cyanide chuyển hóa thành thiocyanate ở gan (cần thiosulfate).",
            "clearance": "Thiocyanate thải trừ qua thận (nguy cơ tích lũy ở suy thận)"
        },
        "storage": "Bảo quản bột khô ở nhiệt độ phòng (20-25°C), tránh ánh sáng. Sau khi pha: bảo vệ khỏi ánh sáng (dùng bọc tối màu), dùng trong 24 giờ.",
        "black_box_warnings": "Nguy cơ thiocyanate độc (cyanide toxicity) nếu dùng kéo dài (>24-48 giờ) hoặc liều cao (>10 mcg/kg/phút), có thể gây tử vong. CHỈ dùng trong ICU với monitoring huyết động liên tục (arterial line). CHỐNG CHỈ ĐỊNH hoặc dùng rất thận trọng ở suy thận nặng. Phải theo dõi nồng độ thiocyanate nếu dùng >24 giờ hoặc liều cao.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Thuốc hạ huyết áp khác (ACE inhibitors, ARBs, Nitroglycerin, Hydralazine)",
                    "mechanism": "Tác dụng hạ huyết áp cộng dồn",
                    "effect": "Tăng nguy cơ hạ huyết áp nặng, sốc",
                    "management": "Theo dõi huyết áp sát. Giảm liều các thuốc hạ huyết áp khác nếu cần."
                }
            ],
            "moderate": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng nitroprusside",
                "Thiếu cơ sở theo dõi huyết động liên tục (arterial line) - CHỐNG CHỈ ĐỊNH",
                "Suy thận nặng (CrCl <30) với nguy cơ thiocyanate độc - CHỐNG CHỈ ĐỊNH hoặc dùng rất thận trọng"
            ],
            "tương_đối": [
                "Thiếu máu cục bộ cơ tim cấp (acute coronary syndrome) - thận trọng, có thể làm nặng",
                "Suy thận (CrCl 30-60) - thận trọng, giảm liều, theo dõi thiocyanate",
                "Bệnh nhân cao tuổi - tăng nhạy cảm với hạ huyết áp",
                "Dùng với thuốc hạ huyết áp khác - tăng nguy cơ hạ huyết áp"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Nitroprusside là thuốc phân loại C. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Nitroprusside có thể qua nhau thai và có thể gây thiocyanate độc ở thai nhi. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt trong cơn tăng huyết áp đe dọa tính mạng.",
            "lactation": {
                "safety": "Not Recommended",
                "details": "Nitroprusside và thiocyanate có thể bài tiết vào sữa mẹ. Nguy cơ thiocyanate độc ở trẻ bú mẹ.",
                "recommendation": "Không khuyến cáo cho con bú khi đang dùng nitroprusside. Cân nhắc ngừng cho con bú hoặc dùng thuốc thay thế."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Thận trọng. Chuyển hóa cyanide thành thiocyanate có thể giảm, tăng nguy cơ cyanide độc.",
            "severe": "Thận trọng. Chuyển hóa cyanide thành thiocyanate giảm đáng kể, tăng nguy cơ cyanide độc. Có thể cần thiosulfate.",
            "notes": "Nitroprusside chuyển hóa thành cyanide và NO. Cyanide chuyển hóa thành thiocyanate ở gan (cần thiosulfate). Suy gan có thể làm giảm chuyển hóa cyanide, tăng nguy cơ cyanide độc. Có thể cần thiosulfate để điều trị cyanide độc."
        },
        "overdose_management": {
            "symptoms": [
                "Hạ huyết áp nặng, sốc",
                "Thiocyanate độc: rối loạn ý thức, co giật, buồn nôn, nôn, toan lactic",
                "Cyanide độc: rối loạn ý thức, co giật, toan lactic nặng, ngừng tim",
                "Nhịp tim nhanh"
            ],
            "antidote": "Thiosulfate cho cyanide độc. Lọc máu cho thiocyanate độc.",
            "treatment": [
                "Ngừng ngay nitroprusside nếu đang truyền",
                "Nếu hạ huyết áp nặng:",
                "  - Truyền dịch bolus (NS, LR)",
                "  - Thuốc vận mạch (norepinephrine, dopamine) nếu cần",
                "Nếu thiocyanate độc (nồng độ >20 mg/dL hoặc triệu chứng):",
                "  - Lọc máu (hemodialysis) - thiocyanate có thể được loại bỏ",
                "  - Hỗ trợ hô hấp nếu cần",
                "Nếu cyanide độc (nghi ngờ nếu dùng liều cao, suy gan):",
                "  - Sodium thiosulfate 12.5g IV (chuyển hóa cyanide thành thiocyanate)",
                "  - Hydroxocobalamin 5g IV (nếu có) - đối kháng cyanide",
                "  - Hỗ trợ hô hấp, thở oxy",
                "Theo dõi: Huyết áp, nhịp tim, ECG, nồng độ thiocyanate, acid-base balance liên tục"
            ],
            "monitoring": "Theo dõi huyết áp, nhịp tim, ECG, nồng độ thiocyanate, acid-base balance liên tục cho đến khi hồi phục. Theo dõi lâu hơn nếu có biến chứng (thiocyanate độc, cyanide độc)."
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "agent": "Sodium thiosulfate",
                    "mechanism": "Chuyển hóa cyanide thành thiocyanate (ít độc hơn)",
                    "indication": "Cyanide độc do nitroprusside",
                    "dose": "12.5g IV (150mg/kg)"
                },
                {
                    "agent": "Hydroxocobalamin",
                    "mechanism": "Đối kháng cyanide, tạo cyanocobalamin",
                    "indication": "Cyanide độc do nitroprusside",
                    "dose": "5g IV (70mg/kg)"
                }
            ],
            "notes": "Sodium thiosulfate và hydroxocobalamin điều trị cyanide độc. Lọc máu điều trị thiocyanate độc."
        },
        "administration_instructions": {
            "oral": None,
            "iv": {
                "reconstitution": "Pha trong D5W (KHÔNG dùng NS - không ổn định). Nồng độ thường dùng: 50-200 mcg/ml. Bảo vệ khỏi ánh sáng (dùng bọc tối màu).",
                "infusion_rate": "Khởi đầu: 0.25-0.5 mcg/kg/phút IV infusion. Chỉnh liều theo huyết áp mục tiêu. Tối đa: 10 mcg/kg/phút. Thời gian dùng tối đa 24-48 giờ.",
                "compatibility": ["D5W (5% Dextrose)"],
                "incompatibility": [
                    "NS (0.9% NaCl) - không ổn định",
                    "Không trộn với các thuốc khác. Dùng đường truyền riêng."
                ],
                "notes": "QUAN TRỌNG: 1) CHỈ dùng trong ICU với monitoring huyết động liên tục (arterial line), 2) Pha trong D5W (KHÔNG dùng NS), 3) Bảo vệ khỏi ánh sáng, 4) Thời gian dùng tối đa 24-48 giờ, 5) Theo dõi nồng độ thiocyanate nếu dùng >24 giờ hoặc liều cao."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Nitroprusside (Nipride)",
                "ACC/AHA Guidelines for Hypertension",
                "UpToDate - Nitroprusside: Drug Information",
                "Medscape - Nitroprusside Drug Reference"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, ACC/AHA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },

}

__all__ = ['VASODILATORS']
