"""Neurological Medications - Migraine CGRP Monoclonal Antibodies
Active module - contains CGRP receptor and ligand monoclonal antibodies for migraine prevention"""

# CGRP Monoclonal Antibodies for Migraine Prevention

MIGRAINE_CGRP_DRUGS = {
    "Erenumab": {
        "group": "Neurology - Anti-CGRP Receptor Monoclonal Antibody",
        "vietnamese_name": "Erenumab, Aimovig",
        "administration": ["SC"],
        "indications": [
            "Phòng ngừa migraine (episodic và chronic migraine) ở người lớn"
        ],
        "contraindications": [
            "Dị ứng erenumab hoặc bất kỳ thành phần nào"
        ],
        "dosage": {
            "adult_standard": "70mg SC mỗi tháng (có thể tăng đến 140mg SC mỗi tháng nếu cần)",
            "notes": "Tiêm dưới da (SC) ở vùng bụng, đùi, hoặc cánh tay. Có thể tự tiêm sau khi được hướng dẫn."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều",
            "under_30": "Không cần chỉnh liều"
        },
        "side_effects": [
            "Táo bón (phổ biến, có thể nghiêm trọng)",
            "Phản ứng tại chỗ tiêm (đau, đỏ, ngứa)",
            "Co thắt cơ (muscle cramps)",
            "Dị ứng (hiếm)"
        ],
        "interactions": [
            "Không có tương tác thuốc đáng kể đã được báo cáo"
        ],
        "pregnancy": "C",
        "mechanism_of_action": (
            "Erenumab là kháng thể đơn dòng kháng thụ thể CGRP (calcitonin gene-related peptide receptor, human monoclonal antibody). "
            "CGRP là một neuropeptide được giải phóng từ các terminal thần kinh trigeminal trong cơn migraine, "
            "gây giãn mạch máu não và kích hoạt quá trình viêm thần kinh, dẫn đến đau migraine. "
            "Erenumab gắn với thụ thể CGRP → ngăn chặn CGRP gắn với thụ thể → ức chế tác dụng giãn mạch và viêm của CGRP. "
            "Dẫn đến: giảm tần suất và mức độ nghiêm trọng của cơn migraine. "
            "Erenumab được dùng để phòng ngừa migraine (không phải điều trị cấp tính), "
            "đặc biệt hiệu quả ở bệnh nhân có migraine thường xuyên hoặc không đáp ứng với các thuốc phòng ngừa khác."
        ),
        "monitoring": [
            "Tần suất và mức độ nghiêm trọng của cơn migraine (theo dõi nhật ký migraine)",
            "Táo bón - theo dõi chặt chẽ, có thể nghiêm trọng và cần điều trị",
            "Phản ứng tại chỗ tiêm",
            "Dấu hiệu dị ứng (phát ban, khó thở, phù mạch)"
        ],
        "precautions": [
            "TÁO BÓN - phổ biến và có thể nghiêm trọng, cần theo dõi và điều trị sớm",
            "Có thể tự tiêm sau khi được hướng dẫn đúng cách",
            "Thận trọng ở bệnh nhân có tiền sử dị ứng với kháng thể đơn dòng",
            "Không dùng để điều trị cấp tính cơn migraine (chỉ dùng để phòng ngừa)",
            "Có thể mất vài tuần đến vài tháng để thấy hiệu quả đầy đủ"
        ],
        "pharmacokinetics": {
            "half_life": "~28 ngày (rất dài, cho phép dùng 1 lần/tháng)",
            "onset": "Vài tuần đến vài tháng (tác dụng chậm)",
            "duration": "Dài (do half-life rất dài)",
            "protein_binding": "IgG2 monoclonal antibody",
            "metabolism": "Chuyển hóa qua hệ thống reticuloendothelial (RES)",
            "clearance": "Không phụ thuộc gan thận đáng kể"
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Có thể để ở nhiệt độ phòng (≤25°C) tối đa 7 ngày. Không làm nóng hoặc lắc mạnh.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, táo bón có thể nghiêm trọng và cần điều trị.",
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng erenumab hoặc bất kỳ thành phần nào"
            ],
            "tương_đối": [
                "Tiền sử dị ứng với kháng thể đơn dòng",
                "Bệnh nhân có táo bón mạn tính hoặc rối loạn tiêu hóa nặng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu hạn chế. Có thể dùng trong thai kỳ khi lợi ích vượt trội nguy cơ. Theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Unknown",
                "details": "Chưa rõ bài tiết vào sữa mẹ. Kháng thể lớn, hấp thu qua đường tiêu hóa trẻ có thể hạn chế.",
                "recommendation": "Cân nhắc ngừng cho bú hoặc không dùng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều",
            "severe": "Không cần chỉnh liều",
            "notes": "Erenumab chuyển hóa qua RES, không phụ thuộc gan đáng kể."
        },
        "overdose_management": {
            "symptoms": [
                "Tăng nguy cơ táo bón",
                "Phản ứng tại chỗ tiêm nặng hơn",
                "Dị ứng (hiếm)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Theo dõi triệu chứng",
                "Điều trị táo bón nếu có",
                "Xử trí phản ứng dị ứng nếu có (antihistamine, corticosteroid, epinephrine nếu cần)"
            ],
            "monitoring": "Triệu chứng tiêu hóa, phản ứng tại chỗ tiêm, dấu hiệu dị ứng"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "sc": {
                "reconstitution": "Dùng trực tiếp từ bút tiêm hoặc ống tiêm đã pha sẵn.",
                "injection_site": "Vùng bụng, đùi, hoặc cánh tay. Thay đổi vị trí tiêm mỗi lần.",
                "injection_technique": "Tiêm dưới da (SC), không tiêm vào cơ hoặc tĩnh mạch.",
                "notes": "Có thể tự tiêm sau khi được hướng dẫn. Lưu trữ trong tủ lạnh, để ở nhiệt độ phòng 30 phút trước khi tiêm."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Erenumab (Aimovig)",
                "UpToDate - Erenumab: Drug information",
                "Lexicomp - Erenumab monograph",
                "AHS Guidelines - Migraine Prevention"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, large RCTs showing benefit in migraine prevention"
        }
    },

    "Fremanezumab": {
        "group": "Neurology - Anti-CGRP Monoclonal Antibody",
        "vietnamese_name": "Fremanezumab, Ajovy",
        "administration": ["SC"],
        "indications": [
            "Phòng ngừa migraine (episodic và chronic migraine) ở người lớn"
        ],
        "contraindications": [
            "Dị ứng fremanezumab hoặc bất kỳ thành phần nào"
        ],
        "dosage": {
            "adult_monthly": "225mg SC mỗi tháng",
            "adult_quarterly": "675mg SC mỗi 3 tháng (liều tương đương)",
            "notes": "Tiêm dưới da (SC) ở vùng bụng, đùi, hoặc cánh tay. Có thể tự tiêm sau khi được hướng dẫn."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều",
            "under_30": "Không cần chỉnh liều"
        },
        "side_effects": [
            "Phản ứng tại chỗ tiêm (đau, đỏ, ngứa) - phổ biến",
            "Dị ứng (hiếm)",
            "Buồn nôn (hiếm)"
        ],
        "interactions": [
            "Không có tương tác thuốc đáng kể đã được báo cáo"
        ],
        "pregnancy": "C",
        "mechanism_of_action": (
            "Fremanezumab là kháng thể đơn dòng kháng CGRP (calcitonin gene-related peptide, humanized monoclonal antibody). "
            "CGRP là một neuropeptide được giải phóng từ các terminal thần kinh trigeminal trong cơn migraine, "
            "gây giãn mạch máu não và kích hoạt quá trình viêm thần kinh, dẫn đến đau migraine. "
            "Fremanezumab gắn trực tiếp với CGRP ligand → ngăn chặn CGRP gắn với thụ thể CGRP → ức chế tác dụng giãn mạch và viêm của CGRP. "
            "Dẫn đến: giảm tần suất và mức độ nghiêm trọng của cơn migraine. "
            "Fremanezumab được dùng để phòng ngừa migraine (không phải điều trị cấp tính), "
            "có thể dùng hàng tháng hoặc hàng quý (3 tháng một lần). "
            "Đặc biệt hiệu quả ở bệnh nhân có migraine thường xuyên hoặc không đáp ứng với các thuốc phòng ngừa khác."
        ),
        "monitoring": [
            "Tần suất và mức độ nghiêm trọng của cơn migraine (theo dõi nhật ký migraine)",
            "Phản ứng tại chỗ tiêm",
            "Dấu hiệu dị ứng (phát ban, khó thở, phù mạch)"
        ],
        "precautions": [
            "Có thể tự tiêm sau khi được hướng dẫn đúng cách",
            "Thận trọng ở bệnh nhân có tiền sử dị ứng với kháng thể đơn dòng",
            "Không dùng để điều trị cấp tính cơn migraine (chỉ dùng để phòng ngừa)",
            "Có thể mất vài tuần đến vài tháng để thấy hiệu quả đầy đủ",
            "Có thể dùng hàng tháng hoặc hàng quý (tùy chọn liều)"
        ],
        "pharmacokinetics": {
            "half_life": "~31 ngày (rất dài, cho phép dùng 1 lần/tháng hoặc 1 lần/3 tháng)",
            "onset": "Vài tuần đến vài tháng (tác dụng chậm)",
            "duration": "Dài (do half-life rất dài)",
            "protein_binding": "IgG2 monoclonal antibody",
            "metabolism": "Chuyển hóa qua hệ thống reticuloendothelial (RES)",
            "clearance": "Không phụ thuộc gan thận đáng kể"
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Có thể để ở nhiệt độ phòng (≤25°C) tối đa 7 ngày. Không làm nóng hoặc lắc mạnh.",
        "black_box_warnings": "Không có black box warning.",
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng fremanezumab hoặc bất kỳ thành phần nào"
            ],
            "tương_đối": [
                "Tiền sử dị ứng với kháng thể đơn dòng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu hạn chế. Có thể dùng trong thai kỳ khi lợi ích vượt trội nguy cơ. Theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Unknown",
                "details": "Chưa rõ bài tiết vào sữa mẹ. Kháng thể lớn, hấp thu qua đường tiêu hóa trẻ có thể hạn chế.",
                "recommendation": "Cân nhắc ngừng cho bú hoặc không dùng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều",
            "severe": "Không cần chỉnh liều",
            "notes": "Fremanezumab chuyển hóa qua RES, không phụ thuộc gan đáng kể."
        },
        "overdose_management": {
            "symptoms": [
                "Phản ứng tại chỗ tiêm nặng hơn",
                "Dị ứng (hiếm)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Theo dõi triệu chứng",
                "Xử trí phản ứng dị ứng nếu có (antihistamine, corticosteroid, epinephrine nếu cần)"
            ],
            "monitoring": "Phản ứng tại chỗ tiêm, dấu hiệu dị ứng"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "sc": {
                "reconstitution": "Dùng trực tiếp từ bút tiêm hoặc ống tiêm đã pha sẵn.",
                "injection_site": "Vùng bụng, đùi, hoặc cánh tay. Thay đổi vị trí tiêm mỗi lần.",
                "injection_technique": "Tiêm dưới da (SC), không tiêm vào cơ hoặc tĩnh mạch.",
                "notes": "Có thể tự tiêm sau khi được hướng dẫn. Lưu trữ trong tủ lạnh, để ở nhiệt độ phòng 30 phút trước khi tiêm. Có thể dùng hàng tháng (225mg) hoặc hàng quý (675mg)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Fremanezumab (Ajovy)",
                "UpToDate - Fremanezumab: Drug information",
                "Lexicomp - Fremanezumab monograph",
                "AHS Guidelines - Migraine Prevention"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, large RCTs showing benefit in migraine prevention"
        }
    },

    "Galcanezumab": {
        "group": "Neurology - Anti-CGRP Monoclonal Antibody",
        "vietnamese_name": "Galcanezumab, Emgality",
        "administration": ["SC"],
        "indications": [
            "Phòng ngừa migraine (episodic và chronic migraine) ở người lớn",
            "Phòng ngừa cluster headache ở người lớn"
        ],
        "contraindications": [
            "Dị ứng galcanezumab hoặc bất kỳ thành phần nào"
        ],
        "dosage": {
            "adult_migraine": "240mg SC liều đầu (2 lần tiêm 120mg), sau đó 120mg SC mỗi tháng",
            "adult_cluster": "300mg SC liều đầu (3 lần tiêm 100mg), sau đó 300mg SC mỗi tháng trong thời gian cluster period",
            "notes": "Tiêm dưới da (SC) ở vùng bụng, đùi, hoặc cánh tay. Có thể tự tiêm sau khi được hướng dẫn."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều",
            "under_30": "Không cần chỉnh liều"
        },
        "side_effects": [
            "Phản ứng tại chỗ tiêm (đau, đỏ, ngứa) - phổ biến",
            "Dị ứng (hiếm)"
        ],
        "interactions": [
            "Không có tương tác thuốc đáng kể đã được báo cáo"
        ],
        "pregnancy": "C",
        "mechanism_of_action": (
            "Galcanezumab là kháng thể đơn dòng kháng CGRP (calcitonin gene-related peptide, humanized monoclonal antibody). "
            "CGRP là một neuropeptide được giải phóng từ các terminal thần kinh trigeminal trong cơn migraine và cluster headache, "
            "gây giãn mạch máu não và kích hoạt quá trình viêm thần kinh, dẫn đến đau. "
            "Galcanezumab gắn trực tiếp với CGRP ligand → ngăn chặn CGRP gắn với thụ thể CGRP → ức chế tác dụng giãn mạch và viêm của CGRP. "
            "Dẫn đến: giảm tần suất và mức độ nghiêm trọng của cơn migraine và cluster headache. "
            "Galcanezumab được dùng để phòng ngừa migraine và cluster headache (không phải điều trị cấp tính), "
            "là thuốc CGRP mAb đầu tiên được FDA phê duyệt cho cluster headache. "
            "Đặc biệt hiệu quả ở bệnh nhân có migraine hoặc cluster headache thường xuyên hoặc không đáp ứng với các thuốc phòng ngừa khác."
        ),
        "monitoring": [
            "Tần suất và mức độ nghiêm trọng của cơn migraine/cluster headache (theo dõi nhật ký)",
            "Phản ứng tại chỗ tiêm",
            "Dấu hiệu dị ứng (phát ban, khó thở, phù mạch)"
        ],
        "precautions": [
            "Có thể tự tiêm sau khi được hướng dẫn đúng cách",
            "Thận trọng ở bệnh nhân có tiền sử dị ứng với kháng thể đơn dòng",
            "Không dùng để điều trị cấp tính cơn migraine/cluster headache (chỉ dùng để phòng ngừa)",
            "Có thể mất vài tuần đến vài tháng để thấy hiệu quả đầy đủ",
            "Liều đầu cho migraine: 240mg (2 lần tiêm 120mg), sau đó 120mg/tháng"
        ],
        "pharmacokinetics": {
            "half_life": "~27 ngày (rất dài, cho phép dùng 1 lần/tháng)",
            "onset": "Vài tuần đến vài tháng (tác dụng chậm)",
            "duration": "Dài (do half-life rất dài)",
            "protein_binding": "IgG4 monoclonal antibody",
            "metabolism": "Chuyển hóa qua hệ thống reticuloendothelial (RES)",
            "clearance": "Không phụ thuộc gan thận đáng kể"
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Có thể để ở nhiệt độ phòng (≤25°C) tối đa 7 ngày. Không làm nóng hoặc lắc mạnh.",
        "black_box_warnings": "Không có black box warning.",
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng galcanezumab hoặc bất kỳ thành phần nào"
            ],
            "tương_đối": [
                "Tiền sử dị ứng với kháng thể đơn dòng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu hạn chế. Có thể dùng trong thai kỳ khi lợi ích vượt trội nguy cơ. Theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Unknown",
                "details": "Chưa rõ bài tiết vào sữa mẹ. Kháng thể lớn, hấp thu qua đường tiêu hóa trẻ có thể hạn chế.",
                "recommendation": "Cân nhắc ngừng cho bú hoặc không dùng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều",
            "severe": "Không cần chỉnh liều",
            "notes": "Galcanezumab chuyển hóa qua RES, không phụ thuộc gan đáng kể."
        },
        "overdose_management": {
            "symptoms": [
                "Phản ứng tại chỗ tiêm nặng hơn",
                "Dị ứng (hiếm)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Theo dõi triệu chứng",
                "Xử trí phản ứng dị ứng nếu có (antihistamine, corticosteroid, epinephrine nếu cần)"
            ],
            "monitoring": "Phản ứng tại chỗ tiêm, dấu hiệu dị ứng"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "sc": {
                "reconstitution": "Dùng trực tiếp từ bút tiêm hoặc ống tiêm đã pha sẵn.",
                "injection_site": "Vùng bụng, đùi, hoặc cánh tay. Thay đổi vị trí tiêm mỗi lần.",
                "injection_technique": "Tiêm dưới da (SC), không tiêm vào cơ hoặc tĩnh mạch.",
                "notes": "Có thể tự tiêm sau khi được hướng dẫn. Lưu trữ trong tủ lạnh, để ở nhiệt độ phòng 30 phút trước khi tiêm. Liều đầu cho migraine: 240mg (2 lần tiêm 120mg), sau đó 120mg/tháng."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Galcanezumab (Emgality)",
                "UpToDate - Galcanezumab: Drug information",
                "Lexicomp - Galcanezumab monograph",
                "AHS Guidelines - Migraine Prevention"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, large RCTs showing benefit in migraine and cluster headache prevention"
        }
    },

    "Eptinezumab": {
        "group": "Neurology - Anti-CGRP Monoclonal Antibody",
        "vietnamese_name": "Eptinezumab, Vyepti",
        "administration": ["IV"],
        "indications": [
            "Phòng ngừa migraine (episodic và chronic migraine) ở người lớn"
        ],
        "contraindications": [
            "Dị ứng eptinezumab hoặc bất kỳ thành phần nào"
        ],
        "dosage": {
            "adult_standard": "100mg IV mỗi 3 tháng (có thể tăng đến 300mg IV mỗi 3 tháng nếu cần)",
            "notes": "Truyền tĩnh mạch trong khoảng 30 phút. Cần được thực hiện bởi nhân viên y tế."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều",
            "under_30": "Không cần chỉnh liều"
        },
        "side_effects": [
            "Phản ứng truyền (infusion-related reactions) - phổ biến",
            "Buồn nôn",
            "Mệt mỏi",
            "Dị ứng (hiếm)"
        ],
        "interactions": [
            "Không có tương tác thuốc đáng kể đã được báo cáo"
        ],
        "pregnancy": "C",
        "mechanism_of_action": (
            "Eptinezumab là kháng thể đơn dòng kháng CGRP (calcitonin gene-related peptide, humanized monoclonal antibody). "
            "CGRP là một neuropeptide được giải phóng từ các terminal thần kinh trigeminal trong cơn migraine, "
            "gây giãn mạch máu não và kích hoạt quá trình viêm thần kinh, dẫn đến đau migraine. "
            "Eptinezumab gắn trực tiếp với CGRP ligand → ngăn chặn CGRP gắn với thụ thể CGRP → ức chế tác dụng giãn mạch và viêm của CGRP. "
            "Dẫn đến: giảm tần suất và mức độ nghiêm trọng của cơn migraine. "
            "Eptinezumab được dùng để phòng ngừa migraine (không phải điều trị cấp tính), "
            "là thuốc CGRP mAb duy nhất được dùng qua đường tĩnh mạch (IV), cho phép dùng 1 lần/3 tháng. "
            "Đặc biệt hiệu quả ở bệnh nhân có migraine thường xuyên hoặc không đáp ứng với các thuốc phòng ngừa khác."
        ),
        "monitoring": [
            "Tần suất và mức độ nghiêm trọng của cơn migraine (theo dõi nhật ký migraine)",
            "Phản ứng truyền (infusion-related reactions) - theo dõi trong và sau truyền",
            "Dấu hiệu dị ứng (phát ban, khó thở, phù mạch)"
        ],
        "precautions": [
            "Phản ứng truyền: có thể cần premedication (antihistamine, corticosteroid, acetaminophen)",
            "Thận trọng ở bệnh nhân có tiền sử dị ứng với kháng thể đơn dòng",
            "Không dùng để điều trị cấp tính cơn migraine (chỉ dùng để phòng ngừa)",
            "Có thể mất vài tuần đến vài tháng để thấy hiệu quả đầy đủ",
            "Cần được thực hiện bởi nhân viên y tế (không tự tiêm như các CGRP mAb khác)"
        ],
        "pharmacokinetics": {
            "half_life": "~27 ngày (rất dài, cho phép dùng 1 lần/3 tháng)",
            "onset": "Vài tuần đến vài tháng (tác dụng chậm)",
            "duration": "Dài (do half-life rất dài)",
            "protein_binding": "IgG1 monoclonal antibody",
            "metabolism": "Chuyển hóa qua hệ thống reticuloendothelial (RES)",
            "clearance": "Không phụ thuộc gan thận đáng kể"
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Dung dịch pha loãng: dùng trong 8 giờ ở nhiệt độ phòng hoặc 24 giờ ở 2-8°C.",
        "black_box_warnings": "Không có black box warning.",
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng eptinezumab hoặc bất kỳ thành phần nào"
            ],
            "tương_đối": [
                "Tiền sử dị ứng với kháng thể đơn dòng",
                "Tiền sử phản ứng truyền nặng với các thuốc IV khác"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu hạn chế. Có thể dùng trong thai kỳ khi lợi ích vượt trội nguy cơ. Theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Unknown",
                "details": "Chưa rõ bài tiết vào sữa mẹ. Kháng thể lớn, hấp thu qua đường tiêu hóa trẻ có thể hạn chế.",
                "recommendation": "Cân nhắc ngừng cho bú hoặc không dùng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều",
            "severe": "Không cần chỉnh liều",
            "notes": "Eptinezumab chuyển hóa qua RES, không phụ thuộc gan đáng kể."
        },
        "overdose_management": {
            "symptoms": [
                "Phản ứng truyền nặng",
                "Dị ứng (hiếm)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng truyền ngay nếu có phản ứng nặng",
                "Điều trị phản ứng truyền: corticosteroid, antihistamine, epinephrine nếu cần",
                "Theo dõi dấu hiệu sinh tồn"
            ],
            "monitoring": "Phản ứng truyền, dấu hiệu dị ứng, dấu hiệu sinh tồn"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha loãng trong 100ml NaCl 0.9%.",
                "infusion_rate": "Truyền tĩnh mạch trong khoảng 30 phút.",
                "compatibility": ["NaCl 0.9%"],
                "incompatibility": ["Dextrose solutions", "Không pha với các thuốc khác."],
                "notes": "Cần premedication (antihistamine, corticosteroid, acetaminophen) cho các liều đầu để giảm phản ứng truyền. Theo dõi chặt chẽ trong và sau truyền."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Eptinezumab (Vyepti)",
                "UpToDate - Eptinezumab: Drug information",
                "Lexicomp - Eptinezumab monograph",
                "AHS Guidelines - Migraine Prevention"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, large RCTs showing benefit in migraine prevention"
        }
    }
}

__all__ = ['MIGRAINE_CGRP_DRUGS']

