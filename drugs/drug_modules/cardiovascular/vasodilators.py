"""
Vasodilators - Vasodilating Agents
"""

VASODILATORS = {
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
    }

}

__all__ = ['VASODILATORS']
