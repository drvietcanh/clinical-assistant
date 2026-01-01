"""
Common Anticoagulants (Thuốc chống đông phổ biến)
Bao gồm: Warfarin, Rivaroxaban, Enoxaparin
"""

ANTICOAGULANTS_COMMON = {
    "Warfarin": {
        "group": "Hematology - Anticoagulant (Vitamin K Antagonist)",
        "vietnamese_name": "Warfarin, Coumadin",
        "brand_names": {
            "common": ["Coumadin", "Jantoven"],
            "vietnam": ["Warfarin 2mg/5mg", "Marevan"]
        },
        "administration": ["PO"],
        "indications": [
            "Phòng ngừa đột quỵ trong rung nhĩ (Atrial Fibrillation)",
            "Điều trị và phòng ngừa huyết khối tĩnh mạch sâu (DVT) và thuyên tắc phổi (PE)",
            "Phòng ngừa huyết khối sau thay van tim cơ học",
            "Hội chứng kháng phospholipid (APS)"
        ],
        "contraindications": [
            "Chảy máu đang hoạt động",
            "Có thai (Đặc biệt tam cá nguyệt 1 - gây quái thai)",
            "Không thể theo dõi INR thường xuyên",
            "Suy gan nặng"
        ],
        "dosage": {
            "initial": "Khởi đầu 2-5 mg/ngày, điều chỉnh theo INR.",
            "target_inr_afib_dvt": "INR 2-3 (Rung nhĩ, DVT/PE).",
            "target_inr_mechanical_valve": "INR 2.5-3.5 (Van tim cơ học).",
            "notes": "Khoảng điều trị hẹp. Cần theo dõi INR thường xuyên (mỗi 1-4 tuần). Tương tác thuốc và thức ăn rất nhiều."
        },
        "side_effects": [
            "Chảy máu (phổ biến nhất)",
            "Hoại tử da (Warfarin-induced skin necrosis) - Hiếm, nguy hiểm",
            "Hội chứng ngón chân tím (Purple toe syndrome)"
        ],
        "interactions": [
            "RẤT NHIỀU tương tác thuốc (Kháng sinh, NSAID, Amiodarone, Azole antifungals, v.v.)",
            "Thức ăn giàu Vitamin K (Rau xanh đậm) làm giảm hiệu quả",
            "Rượu làm tăng nguy cơ chảy máu"
        ],
        "mechanism_of_action": "Ức chế Vitamin K epoxide reductase, ngăn cản tái tạo Vitamin K, làm giảm tổng hợp các yếu tố đông máu phụ thuộc Vitamin K (II, VII, IX, X) và Protein C, S.",
        "monitoring": [
            "INR (International Normalized Ratio) - Mỗi 1-4 tuần",
            "Dấu hiệu chảy máu (phân đen, nôn ra máu, chảy máu cam, bầm tím)"
        ],
        "reversal_agents": {
            "vitamin_k": "Vitamin K1 (Phytomenadione) 2.5-10mg PO/IV - đảo ngược trong 12-24h.",
            "pcc": "PCC (Prothrombin Complex Concentrate) - đảo ngược nhanh trong trường hợp cấp cứu.",
            "ffp": "FFP (Fresh Frozen Plasma) - nếu không có PCC."
        }
    },

    "Rivaroxaban": {
        "group": "Hematology - Anticoagulant (Direct Factor Xa Inhibitor, DOAC)",
        "vietnamese_name": "Rivaroxaban, Xarelto",
        "brand_names": {
            "common": ["Xarelto"],
            "vietnam": ["Xarelto 10/15/20mg"]
        },
        "administration": ["PO"],
        "indications": [
            "Phòng ngừa đột quỵ trong rung nhĩ không do van tim",
            "Điều trị DVT/PE",
            "Phòng ngừa DVT sau phẫu thuật thay khớp háng/gối",
            "Phòng ngừa huyết khối sau hội chứng mạch vành cấp (với aspirin)"
        ],
        "contraindications": [
            "Chảy máu đang hoạt động",
            "Suy thận nặng (CrCl <15)",
            "Có thai",
            "Suy gan nặng (Child-Pugh C)"
        ],
        "dosage": {
            "afib": "20mg x 1 lần/ngày (15mg nếu CrCl 15-50). Uống cùng bữa tối.",
            "dvt_pe_treatment": "15mg x 2 lần/ngày x 21 ngày, sau đó 20mg x 1 lần/ngày.",
            "prophylaxis": "10mg x 1 lần/ngày.",
            "notes": "Liều ≥15mg phải uống cùng thức ăn để tăng hấp thu. Liều 10mg có thể uống đói."
        },
        "side_effects": [
            "Chảy máu (phổ biến)",
            "Rối loạn tiêu hóa"
        ],
        "interactions": [
            "CYP3A4 và P-gp inhibitors mạnh (Ketoconazole, Ritonavir): Tăng nồng độ - Tránh dùng.",
            "CYP3A4 và P-gp inducers (Rifampin, Carbamazepine): Giảm nồng độ - Tránh dùng.",
            "Aspirin/NSAID: Tăng nguy cơ chảy máu."
        ],
        "mechanism_of_action": "Ức chế trực tiếp Factor Xa, ngăn chặn chuyển đổi prothrombin thành thrombin. Là DOAC, không cần theo dõi INR thường xuyên.",
        "monitoring": [
            "Dấu hiệu chảy máu",
            "Chức năng thận (CrCl) - mỗi 3-6 tháng",
            "Không cần theo dõi INR/aPTT thường xuyên"
        ],
        "reversal_agents": {
            "andexanet_alfa": "Andexanet alfa (Andexxa) - Antidote đặc hiệu cho Rivaroxaban và Apixaban."
        }
    },

    "Enoxaparin": {
        "group": "Hematology - Anticoagulant (Low Molecular Weight Heparin, LMWH)",
        "vietnamese_name": "Enoxaparin, Lovenox, Clexane",
        "brand_names": {
            "common": ["Lovenox", "Clexane"],
            "vietnam": ["Clexane 40mg/0.4ml, 60mg/0.6ml"]
        },
        "administration": ["SC (Tiêm dưới da)"],
        "indications": [
            "Phòng ngừa DVT sau phẫu thuật",
            "Điều trị DVT/PE (cầu nối sang Warfarin hoặc điều trị dài hạn)",
            "Hội chứng mạch vành cấp (ACS) - STEMI, NSTEMI",
            "Chống đông trong lọc máu"
        ],
        "contraindications": [
            "Chảy máu đang hoạt động",
            "Tiền sử giảm tiểu cầu do Heparin (HIT)",
            "Suy thận nặng (CrCl <30) - Cần giảm liều hoặc tránh dùng"
        ],
        "dosage": {
            "prophylaxis": "40mg SC x 1 lần/ngày (phẫu thuật).",
            "dvt_pe_treatment": "1mg/kg SC x 2 lần/ngày hoặc 1.5mg/kg x 1 lần/ngày.",
            "acs": "1mg/kg SC x 2 lần/ngày.",
            "notes": "Không cần theo dõi aPTT thường xuyên (khác Heparin không phân đoạn). Cần giảm liều ở suy thận."
        },
        "side_effects": [
            "Chảy máu (ít hơn Heparin không phân đoạn)",
            "Giảm tiểu cầu do Heparin (HIT) - Hiếm hơn Heparin không phân đoạn",
            "Loãng xương (nếu dùng lâu dài >3 tháng)",
            "Tăng men gan"
        ],
        "mechanism_of_action": "Heparin trọng lượng phân tử thấp (LMWH) gắn với Antithrombin III, ức chế chủ yếu Factor Xa (và ít Factor IIa hơn Heparin không phân đoạn). Tác dụng chống đông có thể dự đoán hơn, không cần theo dõi aPTT thường xuyên.",
        "monitoring": [
            "Dấu hiệu chảy máu",
            "Tiểu cầu (ngày 3-5 để phát hiện HIT)",
            "Chức năng thận (CrCl) - đặc biệt quan trọng",
            "Anti-Xa levels (chỉ ở một số trường hợp đặc biệt: béo phì, suy thận, thai kỳ)"
        ],
        "reversal_agents": {
            "protamine": "Protamine sulfate - Đảo ngược một phần (khoảng 60%). Liều: 1mg protamine cho mỗi 1mg enoxaparin (trong 8h gần nhất)."
        }
    }
}
