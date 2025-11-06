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

}

__all__ = ['VASODILATORS']
