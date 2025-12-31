"""
CMV Antivirals
Ganciclovir for cytomegalovirus infections
"""

CMV_ANTIVIRALS = {
    "Ganciclovir": {
        "group": "Infectious Disease - Antiviral",
        "vietnamese_name": "Ganciclovir, Cytovene",
        "administration": ["IV", "PO"],
        "indications": [
            "Nhiễm CMV ở người suy giảm miễn dịch",
            "Phòng ngừa CMV sau ghép tạng",
            "Viêm võng mạc do CMV",
            "CMV bẩm sinh"
        ],
        "contraindications": [
            "Dị ứng",
            "Suy thận nặng",
            "Có thai",
            "Giảm bạch cầu <500",
            "Giảm tiểu cầu <25,000"
        ],
        "dosage": {
            "adult_iv_induction": "5mg/kg IV mỗi 12 giờ x 14-21 ngày",
            "adult_iv_maintenance": "5mg/kg IV x 1 lần/ngày hoặc 6mg/kg x 5 lần/tuần",
            "adult_po": "1g x 3 lần/ngày (sau IV induction)",
            "notes": "Theo dõi bạch cầu, tiểu cầu, chức năng thận. Rất độc với tủy xương"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "50_80": "Giảm liều 50%",
            "25_50": "Giảm liều 75%",
            "under_25": "Giảm liều 90%"
        },
        "side_effects": [
            "Giảm bạch cầu (phổ biến, nặng)",
            "Giảm tiểu cầu",
            "Giảm hồng cầu",
            "Độc thận",
            "Độc thần kinh",
            "Sốt",
            "Ban da",
            "Rất độc - chỉ dùng khi cần thiết"
        ],
        "interactions": [
            "Probenecid: tăng nồng độ ganciclovir",
            "Zidovudine: tăng độc tính tủy xương",
            "Mycophenolate: tăng nồng độ ganciclovir"
        ],
        "pregnancy": "C - D (với CMV)",
        "mechanism_of_action": "Ganciclovir là thuốc kháng virus, là nucleotide analog của guanosine, tương tự acyclovir nhưng có hiệu quả mạnh hơn với cytomegalovirus (CMV). Sau khi vào tế bào nhiễm CMV, ganciclovir được phosphoryl hóa bởi virus UL97 kinase thành ganciclovir monophosphate, sau đó được phosphoryl hóa tiếp bởi enzyme tế bào thành ganciclovir triphosphate (GCV-TP). GCV-TP ức chế cạnh tranh DNA polymerase của CMV, gây chấm dứt chuỗi DNA và ngăn chặn sự nhân lên của virus. Ganciclovir có hiệu quả với CMV (acyclovir không hiệu quả) và HSV, VZV. Tuy nhiên, ganciclovir cũng được phosphoryl hóa ở tế bào người (ở mức độ thấp hơn), dẫn đến độc tính cao hơn acyclovir, đặc biệt độc với tủy xương (giảm bạch cầu, tiểu cầu, hồng cầu nghiêm trọng). Ganciclovir chỉ dùng khi thực sự cần thiết (CMV nặng ở người suy giảm miễn dịch).",
        "monitoring": [
            "Công thức máu (CBC) - QUAN TRỌNG: giảm bạch cầu, tiểu cầu, hồng cầu là tác dụng phụ phổ biến và nghiêm trọng (2-3 lần/tuần khi dùng IV)",
            "Bạch cầu - giảm bạch cầu nặng phổ biến, ngừng nếu <500/mm³",
            "Tiểu cầu - giảm tiểu cầu phổ biến, ngừng nếu <25,000/mm³",
            "Hồng cầu - thiếu máu có thể xảy ra",
            "Chức năng thận (creatinine, BUN) - độc thận có thể xảy ra, điều chỉnh liều ở suy thận",
            "Dấu hiệu độc thần kinh (lú lẫn, co giật, ảo giác, rối loạn tâm thần) - hiếm nhưng có thể nghiêm trọng",
            "Dấu hiệu nhiễm trùng (sốt, nhiễm trùng) - do giảm bạch cầu",
            "Dấu hiệu chảy máu (chảy máu, bầm tím) - do giảm tiểu cầu",
            "Tương tác với probenecid (tăng nồng độ), zidovudine (tăng độc tính tủy xương), mycophenolate (tăng nồng độ ganciclovir)"
        ],
        "precautions": [
            "RẤT ĐỘC - chỉ dùng khi thực sự cần thiết (CMV nặng ở người suy giảm miễn dịch)",
            "CHỐNG CHỈ ĐỊNH nếu bạch cầu <500/mm³ hoặc tiểu cầu <25,000/mm³",
            "Giảm bạch cầu, tiểu cầu, hồng cầu - tác dụng phụ phổ biến và nghiêm trọng, cần theo dõi chặt chẽ CBC (2-3 lần/tuần khi dùng IV)",
            "Ngừng ngay nếu bạch cầu <500/mm³ hoặc tiểu cầu <25,000/mm³",
            "Có thể cần dùng G-CSF (filgrastim) để tăng bạch cầu, hoặc truyền tiểu cầu",
            "Điều chỉnh liều ở suy thận QUAN TRỌNG: CrCl 50-80: giảm liều 50%; CrCl 25-50: giảm liều 75%; CrCl <25: giảm liều 90%",
            "CHỐNG CHỈ ĐỊNH trong thai kỳ - gây dị tật thai nhi, ung thư ở động vật (category D với CMV)",
            "Độc thần kinh - hiếm nhưng có thể nghiêm trọng (lú lẫn, co giật, ảo giác), cần theo dõi",
            "Độc thận - theo dõi chức năng thận, điều chỉnh liều",
            "Tránh dùng với zidovudine (tăng độc tính tủy xương)",
            "Thận trọng với probenecid (tăng nồng độ ganciclovir), mycophenolate (tăng nồng độ ganciclovir)",
            "Truyền IV chậm (trong 1 giờ) để giảm độc tính",
            "Duy trì đủ dịch để giảm độc thận",
            "Dùng đủ liều và đủ thời gian (induction 14-21 ngày, sau đó maintenance)"
        ],
        "pharmacokinetics": {
            "half_life": "2.5-3.5 giờ (IV), 3-4 giờ (PO)",
            "onset": "Nhanh sau khi vào tế bào",
            "duration": "Ngắn (cần dùng nhiều lần/ngày)",
            "protein_binding": "1-2% (không gắn protein)",
            "clearance": "Thận: bài tiết chủ yếu qua thận (90% nguyên dạng, không chuyển hóa). Hấp thu PO kém (6-9% bioavailability). Cần điều chỉnh liều ở suy thận (tỷ lệ với CrCl)."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Dung dịch IV: bảo quản ở 2-8°C, pha xong dùng trong 24 giờ. Viên nén: bảo quản trong bao bì kín.",
        "black_box_warnings": "RẤT ĐỘC với tủy xương - giảm bạch cầu, tiểu cầu, hồng cầu nghiêm trọng phổ biến. CHỐNG CHỈ ĐỊNH nếu bạch cầu <500/mm³ hoặc tiểu cầu <25,000/mm³. Theo dõi CBC 2-3 lần/tuần khi dùng IV. CHỐNG CHỈ ĐỊNH trong thai kỳ - gây dị tật thai nhi, ung thư ở động vật (category D với CMV). Chỉ dùng khi thực sự cần thiết. Nguy cơ độc thần kinh (lú lẫn, co giật, ảo giác).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Zidovudine (AZT)",
                    "mechanism": "Cả hai đều độc với tủy xương, tác dụng cộng dồn.",
                    "effect": "Tăng độc tính tủy xương nghiêm trọng, tăng nguy cơ giảm bạch cầu, tiểu cầu, hồng cầu",
                    "management": "TRÁNH dùng đồng thời nếu có thể. Nếu phải dùng, theo dõi CBC chặt chẽ (2-3 lần/tuần). Có thể cần giảm liều hoặc ngừng một trong hai thuốc."
                }
            ],
            "moderate": [
                {
                    "drug": "Probenecid",
                    "mechanism": "Probenecid ức chế bài tiết ganciclovir qua thận, tăng nồng độ ganciclovir.",
                    "effect": "Tăng nồng độ ganciclovir, tăng độc tính",
                    "management": "Thận trọng. Có thể cần giảm liều ganciclovir. Theo dõi CBC và chức năng thận chặt chẽ."
                },
                {
                    "drug": "Mycophenolate mofetil",
                    "mechanism": "Mycophenolate ức chế bài tiết ganciclovir qua thận, tăng nồng độ ganciclovir.",
                    "effect": "Tăng nồng độ ganciclovir, tăng độc tính",
                    "management": "Thận trọng. Có thể cần giảm liều ganciclovir. Theo dõi CBC và chức năng thận chặt chẽ."
                },
                {
                    "drug": "Imipenem-cilastatin",
                    "mechanism": "Có thể tăng nguy cơ co giật khi dùng với ganciclovir.",
                    "effect": "Tăng nguy cơ co giật",
                    "management": "Thận trọng. Tránh dùng đồng thời nếu có thể. Theo dõi dấu hiệu co giật."
                }
            ],
            "minor": [
                {
                    "drug": "Didanosine",
                    "mechanism": "Có thể tăng độc tính tủy xương.",
                    "effect": "Tăng độc tính tủy xương",
                    "management": "Thận trọng. Theo dõi CBC chặt chẽ."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng ganciclovir",
                "Bạch cầu <500/mm³ - chống chỉ định tuyệt đối",
                "Tiểu cầu <25,000/mm³ - chống chỉ định tuyệt đối",
                "Có thai - chống chỉ định tuyệt đối (category D với CMV, gây dị tật thai nhi, ung thư ở động vật)"
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <25) - cần điều chỉnh liều nghiêm ngặt (giảm 90%)",
                "Suy thận (CrCl 25-50) - cần điều chỉnh liều (giảm 75%)",
                "Suy thận (CrCl 50-80) - cần điều chỉnh liều (giảm 50%)",
                "Giảm bạch cầu, tiểu cầu, hồng cầu - thận trọng, theo dõi chặt chẽ",
                "Độc thần kinh (tiền sử) - thận trọng",
                "Độc thận (tiền sử) - thận trọng, theo dõi chức năng thận"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C - D (với CMV)",
            "pregnancy_details": "Ganciclovir là category C (thường) hoặc D (với CMV). CHỐNG CHỈ ĐỊNH trong thai kỳ. Ganciclovir gây dị tật thai nhi, ung thư, và các tác dụng phụ nghiêm trọng khác ở động vật. Không có dữ liệu an toàn ở phụ nữ có thai. Phụ nữ trong độ tuổi sinh đẻ phải dùng biện pháp tránh thai hiệu quả trong và sau khi dùng ganciclovir (ít nhất 30 ngày sau khi ngừng).",
            "lactation": {
                "safety": "Contraindicated",
                "details": "Ganciclovir bài tiết vào sữa mẹ. Không có dữ liệu an toàn ở trẻ bú mẹ. Ganciclovir có thể gây độc tính nghiêm trọng ở trẻ sơ sinh.",
                "recommendation": "KHÔNG dùng khi cho con bú. Ngừng cho con bú hoặc ngừng ganciclovir. Nếu phải dùng ganciclovir, không cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Ganciclovir chủ yếu thải trừ qua thận, không chuyển hóa ở gan.",
            "moderate": "Không cần điều chỉnh liều. Ganciclovir chủ yếu thải trừ qua thận, không chuyển hóa ở gan.",
            "severe": "Không cần điều chỉnh liều. Ganciclovir chủ yếu thải trừ qua thận, không chuyển hóa ở gan. Tuy nhiên, suy gan nặng có thể ảnh hưởng đến protein binding (nhưng ganciclovir không gắn protein đáng kể).",
            "notes": "Ganciclovir chủ yếu thải trừ qua thận (90% nguyên dạng, không chuyển hóa ở gan). Suy gan không ảnh hưởng đáng kể đến nồng độ ganciclovir. Tuy nhiên, suy gan có thể ảnh hưởng đến chức năng thận, gián tiếp ảnh hưởng đến thải trừ ganciclovir."
        },
        "overdose_management": {
            "symptoms": [
                "Giảm bạch cầu, tiểu cầu, hồng cầu nghiêm trọng (tăng so với liều điều trị)",
                "Độc thận (suy thận cấp)",
                "Độc thần kinh (lú lẫn, co giật, ảo giác, rối loạn tâm thần)",
                "Nhiễm trùng nặng (do giảm bạch cầu)",
                "Chảy máu nặng (do giảm tiểu cầu)",
                "Thiếu máu nặng (do giảm hồng cầu)",
                "Tử vong (trong trường hợp quá liều nghiêm trọng)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.",
            "treatment": [
                "Ngừng ganciclovir ngay lập tức",
                "Theo dõi CBC chặt chẽ (mỗi ngày hoặc 2 lần/ngày)",
                "Điều trị giảm bạch cầu:",
                "  - G-CSF (filgrastim) để tăng bạch cầu",
                "  - Kháng sinh phổ rộng nếu có nhiễm trùng",
                "  - Cách ly nếu bạch cầu rất thấp",
                "Điều trị giảm tiểu cầu:",
                "  - Truyền tiểu cầu nếu <10,000/mm³ hoặc có chảy máu",
                "  - Tránh thuốc chống đông, NSAID",
                "Điều trị thiếu máu:",
                "  - Truyền hồng cầu nếu cần",
                "  - Erythropoietin nếu cần",
                "Điều trị độc thận:",
                "  - Truyền dịch, điều chỉnh điện giải",
                "  - Hemodialysis nếu suy thận nặng (ganciclovir có thể được lọc qua thận nhân tạo)",
                "Điều trị độc thần kinh:",
                "  - An thần nếu co giật, kích động",
                "  - Anticonvulsant nếu co giật",
                "  - Theo dõi thần kinh chặt chẽ",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2",
                "Theo dõi chức năng thận: Creatinine, BUN, eGFR",
                "Theo dõi ít nhất 1-2 tuần sau khi ngừng ganciclovir"
            ],
            "monitoring": "CBC (bạch cầu, tiểu cầu, hồng cầu) mỗi ngày hoặc 2 lần/ngày, chức năng thận (creatinine, BUN, eGFR), dấu hiệu nhiễm trùng, dấu hiệu chảy máu, dấu hiệu độc thần kinh, dấu hiệu sinh tồn. Theo dõi ít nhất 1-2 tuần sau khi ngừng ganciclovir."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Hấp thu kém (6-9% bioavailability), nhưng thức ăn không ảnh hưởng đáng kể.",
                "timing": "Uống 3 lần/ngày (1g mỗi lần) sau khi hoàn thành IV induction. Uống cùng thời điểm mỗi ngày để duy trì nồng độ ổn định."
            },
            "iv": {
                "reconstitution": "Pha với nước muối đẳng trương (0.9% NaCl) hoặc D5W. Nồng độ pha: 10 mg/ml (tối đa). Pha 500mg trong 50ml = 10 mg/ml. Lắc kỹ để hòa tan hoàn toàn.",
                "infusion_rate": "Truyền chậm trong ít nhất 1 giờ. Không truyền nhanh (tăng nguy cơ độc tính).",
                "compatibility": ["Normal saline (0.9% NaCl)", "D5W (5% Dextrose)"],
                "incompatibility": ["Không trộn với các thuốc khác"],
                "notes": "Truyền IV chậm trong ít nhất 1 giờ. Duy trì đủ dịch để giảm độc thận. Theo dõi CBC 2-3 lần/tuần khi dùng IV. Điều chỉnh liều ở suy thận: CrCl 50-80: giảm liều 50%; CrCl 25-50: giảm liều 75%; CrCl <25: giảm liều 90%."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Ganciclovir (Cytovene)",
                "IDSA Guidelines - Cytomegalovirus Infection",
                "UpToDate - Ganciclovir: Drug Information",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
            ],
            "last_updated": "2025-02-04",
            "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "bleeding_risk": False,
            "organ_toxicity": ["Bone marrow suppression (severe neutropenia, thrombocytopenia, anemia) - CRITICAL", "Nephrotoxicity", "Neurotoxicity (confusion, seizures, hallucinations)"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": True,
            "requires_monitoring": ["CBC (neutrophils, platelets, hemoglobin) - CRITICAL (2-3 times/week when IV)", "Renal function (creatinine, BUN) - for dose adjustment", "Neurological status (confusion, seizures)", "Signs of infection (due to neutropenia)", "Signs of bleeding (due to thrombocytopenia)"]
        },
        "guideline_tags": [
            "IDSA Guidelines - Cytomegalovirus Infection",
            "FDA Black Box Warning - Ganciclovir and Bone Marrow Suppression",
            "FDA Black Box Warning - Ganciclovir and Pregnancy (Category D)",
            "FDA Black Box Warning - Ganciclovir and Neurotoxicity"
        ]
    },
}

__all__ = ['CMV_ANTIVIRALS']
