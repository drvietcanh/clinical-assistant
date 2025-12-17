"""
Polymyxin Antibiotics
Colistin (Polymyxin E)
Kháng sinh cuối cùng cho MDR Gram-âm
"""

POLYMYXIN_ANTIBIOTICS = {
    "Colistin": {
        "group": "Antibiotic - Polymyxin",
        "vietnamese_name": "Colistin, Colistimethate sodium, Coly-Mycin",
        "administration": ["IV", "IM", "Inhaled", "Intrathecal"],
        "indications": [
            "Nhiễm khuẩn do vi khuẩn kháng đa thuốc (MDR) Gram-âm",
            "Pseudomonas aeruginosa kháng đa thuốc",
            "Acinetobacter baumannii kháng đa thuốc",
            "Klebsiella pneumoniae kháng carbapenem (CRE)",
            "E. coli kháng carbapenem",
            "Nhiễm khuẩn huyết do MDR Gram-âm",
            "Viêm phổi bệnh viện do MDR Gram-âm",
            "Nhiễm khuẩn đường tiết niệu do MDR Gram-âm",
            "Viêm màng não do MDR Gram-âm (intrathecal)",
            "Nhiễm khuẩn phổi mãn tính ở bệnh nhân xơ nang (CF) - dạng hít"
        ],
        "contraindications": [
            "Dị ứng colistin hoặc polymyxin",
            "Myasthenia gravis - CHỐNG CHỈ ĐỊNH",
            "Suy thận nặng (CrCl <30) - thận trọng, cần điều chỉnh liều",
            "Suy thận cấp - thận trọng"
        ],
        "dosage": {
            "adult_iv_standard": "2.5-5 mg/kg/ngày IV (tính theo colistin base), chia 2-3 lần",
            "adult_iv_severe": "5-6 mg/kg/ngày IV, chia 2-3 lần",
            "adult_iv_meningitis": "5-6 mg/kg/ngày IV, chia 2-3 lần + intrathecal",
            "adult_inhaled_cf": "75-150mg x 2 lần/ngày (dạng hít)",
            "adult_intrathecal": "5-10mg intrathecal x 1 lần/ngày (viêm màng não)",
            "notes": "Liều tính theo colistin base. Colistimethate sodium (CMS) chuyển thành colistin trong cơ thể. Cần điều chỉnh liều theo chức năng thận. Độc thận và độc thần kinh cao."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50% hoặc tăng khoảng cách",
            "under_30": "Giảm liều 50-75% hoặc tăng khoảng cách đáng kể",
            "hemodialysis": "Liều sau lọc máu, cần TDM nếu có thể"
        },
        "side_effects": [
            "Độc thận (nephrotoxicity) - tăng creatinine, suy thận cấp, có thể không hồi phục",
            "Độc thần kinh (neurotoxicity) - tê bì, yếu cơ, rối loạn cảm giác, co giật, suy hô hấp (neuromuscular blockade)",
            "Block thần kinh-cơ (neuromuscular blockade) - suy hô hấp, nguy hiểm tính mạng",
            "Phát ban",
            "Sốt",
            "Ho, khó thở (dạng hít)",
            "Đau tại chỗ tiêm"
        ],
        "interactions": [
            "Aminoglycosides: tăng độc thận và độc thần kinh",
            "Thuốc giãn cơ (neuromuscular blocking agents): tăng nguy cơ suy hô hấp",
            "Vancomycin: có thể tăng độc thận",
            "Furosemide: có thể tăng độc thận",
            "Cisplatin: tăng độc thận"
        ],
        "pregnancy": "C - Sử dụng nếu lợi ích > nguy cơ (độc thận, độc thần kinh)",
        "mechanism_of_action": "Colistin là polymyxin kháng sinh, gắn với lipopolysaccharide (LPS) của màng ngoài vi khuẩn Gram-âm, phá vỡ tính toàn vẹn màng và gây chết tế bào. Tác động như một chất tẩy rửa (detergent), làm rò rỉ nội dung tế bào. Phổ kháng khuẩn: Gram-âm mạnh (Pseudomonas aeruginosa, Acinetobacter baumannii, Klebsiella pneumoniae, E. coli - kể cả các chủng kháng carbapenem CRE), không có hoạt tính với Gram-dương hoặc kỵ khí. Đặc điểm: kháng sinh cuối cùng cho MDR Gram-âm, độc thận và độc thần kinh cao, cần điều chỉnh liều theo chức năng thận. CHỐNG CHỈ ĐỊNH trong myasthenia gravis (nguy cơ neuromuscular blockade).",
        "monitoring": [
            "Chức năng thận (creatinine, eGFR, BUN) - BẮT BUỘC: hàng ngày, đặc biệt quan trọng vì độc thận cao",
            "Dấu hiệu độc thần kinh: tê bì, yếu cơ, rối loạn cảm giác, co giật, suy hô hấp",
            "Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Điện giải (natri, kali, magie) - có thể gây hạ natri, hạ kali",
            "Chức năng hô hấp (nếu có dấu hiệu neuromuscular blockade)",
            "Dấu hiệu suy hô hấp (neuromuscular blockade) - nguy hiểm tính mạng",
            "TDM (nếu có thể) - nồng độ colistin trong huyết thanh"
        ],
        "precautions": [
            "Độc thận và độc thần kinh - RẤT CAO, có thể không hồi phục",
            "CHỐNG CHỈ ĐỊNH trong myasthenia gravis - nguy cơ neuromuscular blockade, suy hô hấp",
            "Điều chỉnh liều theo chức năng thận (eGFR) - QUAN TRỌNG",
            "Theo dõi chức năng thận hàng ngày - bắt buộc",
            "Theo dõi dấu hiệu độc thần kinh (tê bì, yếu cơ, suy hô hấp) - nguy hiểm tính mạng",
            "Tránh dùng với aminoglycosides - tăng độc thận và độc thần kinh",
            "Tránh dùng với thuốc giãn cơ - tăng nguy cơ suy hô hấp",
            "Tránh dùng với thuốc độc thận khác (vancomycin, furosemide, cisplatin)",
            "Thận trọng ở người cao tuổi, suy thận, có tiền sử bệnh thần kinh",
            "Dạng hít: dùng cho bệnh nhân xơ nang (CF) để điều trị nhiễm Pseudomonas mãn tính, ít độc tính toàn thân hơn",
            "Intrathecal: chỉ dùng cho viêm màng não do MDR Gram-âm, cần thận trọng",
            "Pha trong NS hoặc D5W, truyền IV trong 30-60 phút"
        ],
        "pharmacokinetics": {
            "half_life": "2-3 giờ (bình thường), 10-20 giờ (suy thận nặng)",
            "onset": "Ngay lập tức sau khi truyền IV",
            "duration": "Liều q8-12h (bình thường), q24-48h (suy thận)",
            "protein_binding": "50%",
            "metabolism": "Chuyển hóa một phần (colistimethate → colistin)",
            "clearance": "Chủ yếu qua thận (70-80% bài tiết nguyên dạng), cần điều chỉnh thận",
            "volume_of_distribution": "0.2-0.3 L/kg"
        },
        "storage": "Bảo quản bột khô ở nhiệt độ phòng (20-25°C). Sau khi pha: bảo quản ở nhiệt độ phòng 24 giờ, hoặc trong tủ lạnh 7 ngày. Không đông lạnh.",
        "black_box_warnings": "Độc thận và độc thần kinh - RẤT CAO, có thể không hồi phục. CHỐNG CHỈ ĐỊNH trong myasthenia gravis (nguy cơ neuromuscular blockade, suy hô hấp). Chỉ dùng khi không còn lựa chọn khác (MDR Gram-âm). Cần điều chỉnh liều theo chức năng thận và theo dõi sát.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Aminoglycosides (Gentamicin, Amikacin, Tobramycin)",
                    "mechanism": "Cả hai đều độc thận và độc thần kinh, tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ độc thận và độc thần kinh nặng, có thể không hồi phục",
                    "management": "TRÁNH dùng đồng thời. Nếu bắt buộc, theo dõi chức năng thận và thần kinh sát, giảm liều nếu cần."
                },
                {
                    "drug": "Thuốc giãn cơ (Neuromuscular Blocking Agents: Succinylcholine, Rocuronium, Vecuronium)",
                    "mechanism": "Colistin tăng tác dụng thuốc giãn cơ, gây neuromuscular blockade",
                    "effect": "Tăng nguy cơ suy hô hấp, nguy hiểm tính mạng",
                    "management": "TRÁNH dùng đồng thời. Nếu bắt buộc (phẫu thuật), theo dõi hô hấp sát, có thể cần giảm liều thuốc giãn cơ."
                },
                {
                    "drug": "Vancomycin",
                    "mechanism": "Cả hai đều độc thận, tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ độc thận nặng",
                    "management": "Theo dõi chức năng thận sát nếu dùng đồng thời."
                },
                {
                    "drug": "Furosemide",
                    "mechanism": "Furosemide có thể tăng độc thận của colistin",
                    "effect": "Tăng nguy cơ độc thận",
                    "management": "Theo dõi chức năng thận sát nếu dùng đồng thời."
                }
            ]
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Colistin (Coly-Mycin)",
                "IDSA Guidelines - Antimicrobial Therapy, MDR Gram-negative",
                "UpToDate - Colistin: Drug Information",
                "Medscape - Colistin Drug Reference",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
                "Lexicomp Online - Colistin Monograph",
                "Micromedex - Colistin Drug Information"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    }
}

__all__ = ['POLYMYXIN_ANTIBIOTICS']























