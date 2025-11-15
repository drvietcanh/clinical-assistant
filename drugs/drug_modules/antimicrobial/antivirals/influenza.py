"""
Influenza Antivirals
Neuraminidase inhibitors for influenza treatment
"""

INFLUENZA_ANTIVIRALS = {
    "Oseltamivir": {
        "group": "Infectious Disease - Antiviral (Neuraminidase Inhibitor)",
        "vietnamese_name": "Oseltamivir, Tamiflu",
        "administration": ["PO"],
        "indications": [
            "Cúm A và B (treatment)",
            "Phòng ngừa cúm",
            "Cúm ở người suy giảm miễn dịch"
        ],
        "contraindications": [
            "Dị ứng",
            "Suy thận nặng (thận trọng)"
        ],
        "dosage": {
            "adult_treatment": "75mg x 2 lần/ngày x 5 ngày",
            "adult_prophylaxis": "75mg x 1 lần/ngày x 10 ngày (sau tiếp xúc) hoặc x 6 tuần (mùa cúm)",
            "adult_max": "150mg x 2 lần/ngày (suy giảm miễn dịch)",
            "notes": "Bắt đầu trong 48 giờ đầu triệu chứng. Hiệu quả nhất trong 24 giờ đầu"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "75mg x 1 lần/ngày (treatment), 75mg cách ngày (prophylaxis)",
            "under_30": "75mg x 1 lần/ngày (treatment), 75mg cách 2 ngày (prophylaxis)"
        },
        "side_effects": [
            "Buồn nôn, nôn",
            "Đau đầu",
            "Tiêu chảy",
            "Rối loạn tâm thần (hiếm, ở trẻ em)",
            "Co giật (hiếm)"
        ],
        "interactions": [
            "Probenecid: tăng nồng độ oseltamivir",
            "Ít tương tác khác"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Oseltamivir là thuốc kháng virus cúm, thuộc nhóm chất ức chế neuraminidase. Oseltamivir phosphate là tiền thuốc (prodrug), được chuyển hóa trong gan thành oseltamivir carboxylate (chất hoạt động). Oseltamivir carboxylate ức chế enzyme neuraminidase của virus cúm A và B, enzyme này có vai trò quan trọng trong việc giải phóng các hạt virus mới từ tế bào chủ và lan truyền virus trong đường hô hấp. Bằng cách ức chế neuraminidase, oseltamivir ngăn chặn sự giải phóng virus, làm giảm lan truyền virus và giảm thời gian bệnh. Oseltamivir hiệu quả với cả cúm A và cúm B, nhưng hiệu quả nhất khi bắt đầu điều trị trong vòng 48 giờ đầu (tốt nhất là 24 giờ đầu) sau khi xuất hiện triệu chứng.",
        "monitoring": [
            "Triệu chứng cúm (sốt, ho, đau họng, đau cơ) - đánh giá đáp ứng điều trị",
            "Dấu hiệu biến chứng (viêm phổi, suy hô hấp, nhiễm trùng thứ phát)",
            "Tác dụng phụ (buồn nôn, nôn, đau đầu, tiêu chảy) - thường nhẹ",
            "Rối loạn tâm thần ở trẻ em (kích động, lú lẫn, hành vi bất thường) - hiếm nhưng cần theo dõi",
            "Co giật - hiếm, đặc biệt ở trẻ em",
            "Chức năng thận (creatinine) - điều chỉnh liều ở suy thận",
            "Tương tác với probenecid (tăng nồng độ oseltamivir)"
        ],
        "precautions": [
            "Bắt đầu điều trị càng sớm càng tốt - hiệu quả nhất trong vòng 48 giờ đầu (tốt nhất là 24 giờ đầu) sau khi xuất hiện triệu chứng",
            "Điều chỉnh liều ở suy thận: CrCl 30-60: 75mg x 1 lần/ngày (treatment), 75mg cách ngày (prophylaxis); CrCl <30: 75mg x 1 lần/ngày (treatment), 75mg cách 2 ngày (prophylaxis)",
            "Uống với thức ăn để giảm buồn nôn, nôn",
            "Rối loạn tâm thần ở trẻ em - hiếm nhưng có thể nghiêm trọng, cần theo dõi chặt chẽ",
            "Thận trọng ở bệnh nhân suy thận nặng - cần điều chỉnh liều",
            "Probenecid tăng nồng độ oseltamivir - có thể cần điều chỉnh liều",
            "Hiệu quả phòng ngừa: dùng 75mg x 1 lần/ngày x 10 ngày sau tiếp xúc hoặc x 6 tuần trong mùa cúm",
            "Liều cao hơn (150mg x 2 lần/ngày) có thể cần ở bệnh nhân suy giảm miễn dịch",
            "Không thay thế vaccine cúm - vaccine vẫn là biện pháp phòng ngừa chính",
            "Kháng thuốc có thể xảy ra - theo dõi đáp ứng điều trị"
        ],
        "pharmacokinetics": {
            "half_life": "1-3 giờ (oseltamivir), 6-10 giờ (oseltamivir carboxylate - chất hoạt động)",
            "onset": "24-48 giờ (giảm triệu chứng)",
            "duration": "5 ngày (treatment), 10 ngày - 6 tuần (prophylaxis)",
            "protein_binding": "3% (oseltamivir carboxylate)",
            "clearance": "Gan: chuyển hóa oseltamivir thành oseltamivir carboxylate (chất hoạt động) qua esterase. Thận: bài tiết chủ yếu qua thận (oseltamivir carboxylate bài tiết nguyên dạng). Cần điều chỉnh liều ở suy thận."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín. Dạng suspension: bảo quản ở nhiệt độ phòng, lắc kỹ trước khi dùng, dùng trong vòng 10 ngày sau khi pha hoặc 17 ngày nếu bảo quản trong tủ lạnh.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Probenecid",
                    "mechanism": "Probenecid ức chế bài tiết oseltamivir carboxylate qua thận, tăng nồng độ oseltamivir.",
                    "effect": "Tăng nồng độ oseltamivir carboxylate, tăng tác dụng và tác dụng phụ",
                    "management": "Thận trọng. Có thể cần giảm liều oseltamivir khi dùng với probenecid. Theo dõi tác dụng phụ."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng oseltamivir hoặc các thành phần khác"
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - cần điều chỉnh liều nghiêm ngặt",
                "Có thai - category C, thận trọng",
                "Trẻ em <1 tuổi - không khuyến cáo"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Oseltamivir là category C. Không có nghiên cứu đầy đủ ở phụ nữ có thai. Dùng được nếu lợi ích > nguy cơ. Cúm trong thai kỳ có thể gây biến chứng nghiêm trọng (viêm phổi, suy hô hấp, tử vong). Oseltamivir được khuyến cáo để điều trị cúm trong thai kỳ nếu có chỉ định.",
            "lactation": {
                "safety": "Compatible",
                "details": "Oseltamivir và oseltamivir carboxylate bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ sơ sinh nếu có dấu hiệu bất thường (hiếm)."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Oseltamivir chuyển hóa ở gan thành oseltamivir carboxylate, nhưng suy gan nhẹ không ảnh hưởng đáng kể.",
            "moderate": "Không cần điều chỉnh liều thường quy. Theo dõi tác dụng phụ. Chuyển hóa có thể giảm nhẹ ở suy gan trung bình.",
            "severe": "Thận trọng, theo dõi tác dụng phụ. Chuyển hóa có thể giảm ở suy gan nặng, nhưng thường không cần điều chỉnh liều.",
            "notes": "Oseltamivir chuyển hóa ở gan thành oseltamivir carboxylate (chất hoạt động) qua esterase. Suy gan có thể làm giảm chuyển hóa, nhưng thường không ảnh hưởng đáng kể đến nồng độ oseltamivir carboxylate."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn (tăng so với liều điều trị)",
                "Đau đầu",
                "Tiêu chảy",
                "Rối loạn tâm thần (hiếm)",
                "Co giật (hiếm)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng oseltamivir nếu có thể",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính nếu uống trong vòng 1-2 giờ",
                "Theo dõi dấu hiệu sinh tồn",
                "Điều trị hỗ trợ: truyền dịch nếu cần, điều trị triệu chứng",
                "Theo dõi ít nhất 4-6 giờ"
            ],
            "monitoring": "Dấu hiệu sinh tồn, dấu hiệu rối loạn tâm thần, co giật"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Nên uống với thức ăn để giảm buồn nôn, nôn. Có thể uống với hoặc không thức ăn, nhưng uống với thức ăn giúp giảm tác dụng phụ.",
                "timing": "Uống 2 lần/ngày (treatment) hoặc 1 lần/ngày (prophylaxis). Uống cùng thời điểm mỗi ngày để dễ nhớ. Điều chỉnh liều ở suy thận: CrCl 30-60: 75mg x 1 lần/ngày (treatment), 75mg cách ngày (prophylaxis); CrCl <30: 75mg x 1 lần/ngày (treatment), 75mg cách 2 ngày (prophylaxis)."
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
                "FDA Drug Label - Oseltamivir (Tamiflu)",
                "CDC Guidelines - Influenza Antiviral Medications",
                "WHO Guidelines - Antiviral Treatment for Influenza",
                "UpToDate - Oseltamivir: Drug Information",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
            ],
            "last_updated": "2025-02-04",
            "evidence_level": "A - Dựa trên FDA drug labels, CDC/WHO guidelines, và dữ liệu lâm sàng"
        }
    }
}

__all__ = ['INFLUENZA_ANTIVIRALS']
