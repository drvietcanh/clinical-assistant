"""
Antiarrhythmics - Antiarrhythmic Agents
"""

ANTIARRHYTHMICS = {
    "Amiodarone": {
        "group": "Cardiovascular - Antiarrhythmic (Class III)",
        "vietnamese_name": "Amiodarone, Cordarone",
        "administration": ["PO", "IV"],
        "indications": [
            "Rối loạn nhịp thất",
            "Rung nhĩ",
            "Nhịp nhanh trên thất",
            "Rối loạn nhịp kháng trị"
        ],
        "contraindications": [
            "Block nhĩ thất độ 2-3 không có máy tạo nhịp",
            "Rối loạn chức năng tuyến giáp",
            "Bệnh phổi mạn tính",
            "Bệnh gan nặng"
        ],
        "dosage": {
            "adult_po_loading": "800-1600mg/ngày chia 2 lần x 1-2 tuần",
            "adult_po_maintenance": "200-400mg x 1 lần/ngày",
            "adult_iv_loading": "150mg IV trong 10 phút, sau đó 1mg/phút x 6 giờ, 0.5mg/phút x 18 giờ",
            "notes": "Theo dõi chức năng gan, phổi, tuyến giáp định kỳ"
        },
        "side_effects": [
            "Bệnh phổi do amiodarone (nguy hiểm)",
            "Rối loạn chức năng tuyến giáp",
            "Bệnh gan",
            "Tích tụ ở da (màu xanh xám)",
            "Nhạy cảm với ánh sáng",
            "Corneal deposits",
            "Block nhĩ thất"
        ],
        "interactions": [
            "Digoxin: tăng nồng độ digoxin (giảm liều digoxin 50%)",
            "Warfarin: tăng tác dụng chống đông",
            "Statins: tăng nguy cơ tiêu cơ vân"
        ],
        "pregnancy": "D",
        "mechanism_of_action": "Class III antiarrhythmic (chủ yếu) với tác dụng bổ sung class I, II, IV. Chủ yếu ức chế kênh K+ (delayed rectifier), kéo dài phase 3 của action potential, kéo dài QT interval. Cũng có tác dụng ức chế Na+ channels (class I), chẹn beta (class II), và chẹn Ca2+ (class IV). Rất hiệu quả cho rối loạn nhịp nhưng có nhiều tác dụng phụ.",
        "monitoring": [
            "ECG: QT interval (kéo dài QT là bình thường, nhưng QT >500ms hoặc tăng >60ms nguy hiểm)",
            "Chức năng phổi: X-quang phổi, PFT (6 tháng/lần), đặc biệt chú ý dấu hiệu viêm phổi mô kẽ",
            "Chức năng gan: ALT, AST, bilirubin (mỗi 3-6 tháng)",
            "Chức năng tuyến giáp: TSH, FT4, FT3 (mỗi 6 tháng) - có thể gây cường giáp hoặc suy giáp",
            "Khám mắt: Soi đáy mắt (mỗi 6-12 tháng) - có thể gây viêm giác mạc, đục thủy tinh thể",
            "Da: Dấu hiệu nhạy cảm ánh sáng, xám da (blue-gray discoloration)",
            "Electrolytes: K+, Mg2+ (phải đảm bảo bình thường trước khi dùng)"
        ],
        "precautions": [
            "CẦN LOADING DOSE (thường 800-1600mg/ngày trong 1-2 tuần) trước khi dùng liều duy trì",
            "Tác dụng phụ nhiều và nghiêm trọng - chỉ dùng cho rối loạn nhịp đe dọa tính mạng hoặc không đáp ứng với thuốc khác",
            "Bắt buộc monitor chức năng phổi, gan, tuyến giáp, mắt định kỳ",
            "Tương tác thuốc rất nhiều - kiểm tra kỹ trước khi dùng",
            "Tránh dùng ở phụ nữ có thai (category D)",
            "Thời gian bán hủy rất dài (50-60 ngày) - tác dụng phụ có thể kéo dài sau khi ngừng",
            "Phải đảm bảo K+ và Mg2+ bình thường (giảm K+/Mg2+ tăng nguy cơ torsades de pointes)",
            "Tránh ánh nắng mặt trời (nhạy cảm ánh sáng nặng)"
        ],
        "pharmacokinetics": {
            "half_life": "50-60 ngày (RẤT DÀI - do tích lũy trong mô mỡ)",
            "onset": "1-3 tuần (do loading period)",
            "duration": "Rất lâu sau khi ngừng (do half-life dài)",
            "protein_binding": "96%",
            "clearance": "Gan (CYP3A4, CYP2C8), thải qua phân và nước tiểu (chậm)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Có thể gây tử vong do viêm phổi mô kẽ, suy gan, rối loạn nhịp tim nặng. Chỉ dùng cho rối loạn nhịp đe dọa tính mạng không đáp ứng với thuốc khác. Phải monitor chức năng phổi, gan, tuyến giáp định kỳ. Chống chỉ định trong thai kỳ",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Digoxin",
                    "mechanism": "Amiodarone ức chế P-glycoprotein và giảm thải trừ digoxin, tăng nồng độ digoxin",
                    "effect": "Tăng nồng độ digoxin 50-100%, tăng nguy cơ ngộ độc digoxin (rối loạn nhịp, block AV, buồn nôn)",
                    "management": "GIẢM LIỀU DIGOXIN 50% ngay khi bắt đầu amiodarone. Theo dõi nồng độ digoxin chặt chẽ. Có thể cần giảm liều digoxin thêm."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Amiodarone ức chế CYP2C9 (chuyển hóa warfarin), tăng nồng độ warfarin",
                    "effect": "Tăng tác dụng chống đông mạnh, tăng INR, tăng nguy cơ chảy máu nặng",
                    "management": "GIẢM LIỀU WARFARIN 30-50% ngay khi bắt đầu amiodarone. Theo dõi INR thường xuyên (mỗi 1-2 tuần đầu). Có thể cần giảm liều warfarin thêm khi tác dụng amiodarone ổn định."
                },
                {
                    "drug": "Quinidine, Procainamide, Disopyramide",
                    "mechanism": "Tác dụng hiệp đồng kéo dài QT interval",
                    "effect": "Tăng nguy cơ torsades de pointes, rối loạn nhịp tim đe dọa tính mạng",
                    "management": "TRÁNH DÙNG CHUNG. Nếu bắt buộc: theo dõi ECG sát, đảm bảo K+ và Mg2+ bình thường."
                }
            ],
            "moderate": [
                {
                    "drug": "Statins (simvastatin, atorvastatin, lovastatin)",
                    "mechanism": "Amiodarone ức chế CYP3A4, tăng nồng độ statin",
                    "effect": "Tăng nguy cơ tiêu cơ vân (rhabdomyolysis), suy thận cấp",
                    "management": "Giảm liều statin 50% hoặc tránh dùng simvastatin/atorvastatin. Ưu tiên pravastatin, rosuvastatin (ít chuyển hóa qua CYP3A4). Theo dõi CK, triệu chứng đau cơ."
                },
                {
                    "drug": "Beta-blockers (metoprolol, propranolol)",
                    "mechanism": "Tác dụng hiệp đồng ức chế dẫn truyền nhĩ thất",
                    "effect": "Tăng nguy cơ block nhĩ thất, nhịp tim chậm nặng",
                    "management": "Thận trọng. Giảm liều beta-blocker. Theo dõi ECG, nhịp tim."
                },
                {
                    "drug": "Verapamil, Diltiazem",
                    "mechanism": "Tác dụng hiệp đồng ức chế dẫn truyền nhĩ thất và kéo dài QT",
                    "effect": "Tăng nguy cơ block nhĩ thất, nhịp tim chậm nặng",
                    "management": "Thận trọng. Giảm liều verapamil/diltiazem. Theo dõi ECG sát."
                },
                {
                    "drug": "Phenytoin",
                    "mechanism": "Amiodarone ức chế chuyển hóa phenytoin, phenytoin tăng chuyển hóa amiodarone",
                    "effect": "Tăng nồng độ phenytoin (ngộ độc), giảm nồng độ amiodarone (mất hiệu quả)",
                    "management": "Theo dõi nồng độ cả hai thuốc. Có thể cần điều chỉnh liều."
                },
                {
                    "drug": "Fentanyl",
                    "mechanism": "Amiodarone ức chế CYP3A4, tăng nồng độ fentanyl",
                    "effect": "Tăng nguy cơ ức chế hô hấp, ngừng thở",
                    "management": "Thận trọng. Giảm liều fentanyl. Theo dõi hô hấp sát."
                }
            ],
            "minor": [
                {
                    "drug": "Cyclosporine, Tacrolimus",
                    "mechanism": "Amiodarone ức chế CYP3A4, tăng nồng độ cyclosporine/tacrolimus",
                    "effect": "Tăng nguy cơ độc tính",
                    "management": "Theo dõi nồng độ. Có thể cần giảm liều."
                },
                {
                    "drug": "Theophylline",
                    "mechanism": "Amiodarone ức chế chuyển hóa theophylline",
                    "effect": "Tăng nồng độ theophylline",
                    "management": "Theo dõi nồng độ theophylline. Có thể cần giảm liều."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Block nhĩ thất độ 2-3 không có máy tạo nhịp",
                "Rối loạn chức năng tuyến giáp không kiểm soát được",
                "Bệnh phổi mạn tính nặng (COPD, ILD)",
                "Bệnh gan nặng (Child-Pugh C)",
                "Có thai (category D)",
                "Hạ K+ hoặc Mg2+ nặng (tăng nguy cơ torsades de pointes)"
            ],
            "tương_đối": [
                "Suy thận nặng (thận trọng, theo dõi chức năng thận)",
                "Nhịp tim chậm (tăng nguy cơ block AV)",
                "Bệnh phổi nhẹ (theo dõi chức năng phổi chặt chẽ)",
                "Rối loạn chức năng tuyến giáp nhẹ (theo dõi TSH chặt chẽ)",
                "Đang dùng warfarin hoặc digoxin (cần giảm liều)"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI trong thai kỳ. Amiodarone có thể gây dị tật thai nhi (hypothyroidism, goiter, bất thường tim mạch, chậm phát triển), chậm phát triển thai nhi, và tử vong thai nhi. Nguy cơ cao nhất trong 3 tháng đầu. Chỉ dùng trong trường hợp đe dọa tính mạng của mẹ và không có lựa chọn khác.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Amiodarone bài tiết vào sữa mẹ ở nồng độ cao. Nồng độ trong máu trẻ bú mẹ có thể đạt 25% nồng độ mẹ. Có thể gây rối loạn chức năng tuyến giáp, nhịp tim chậm ở trẻ bú mẹ.",
                "recommendation": "KHÔNG KHUYẾN NGHỊ dùng khi cho con bú. Nếu bắt buộc: ngừng cho con bú hoặc ngừng amiodarone."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Giảm liều 25-50% (chuyển hóa qua gan)",
            "severe": "TRÁNH DÙNG (Child-Pugh C) hoặc giảm liều 50% (nếu bắt buộc), theo dõi chức năng gan chặt chẽ",
            "notes": "Amiodarone chuyển hóa qua gan (CYP3A4, CYP2C8). Suy gan làm giảm chuyển hóa, tăng nồng độ và tác dụng phụ. Bắt buộc theo dõi ALT, AST, bilirubin định kỳ."
        },
        "overdose_management": {
            "symptoms": [
                "Block nhĩ thất độ 2-3",
                "Nhịp tim chậm nặng",
                "Torsades de pointes (do QT kéo dài)",
                "Hạ huyết áp nặng",
                "Suy tim cấp",
                "Rối loạn nhịp tim đe dọa tính mạng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ: máy tạo nhịp, hỗ trợ tuần hoàn",
            "treatment": [
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ (nhưng thận trọng - có thể gây block AV)",
                "Than hoạt tính",
                "Điều trị block AV/nhịp tim chậm: Atropine 0.5-1mg IV, máy tạo nhịp tạm thời nếu cần",
                "Điều trị torsades de pointes: Magnesium sulfate 1-2g IV, nếu cần: pacing, isoproterenol",
                "Điều trị hạ huyết áp: Truyền dịch, nếu cần: dopamine, norepinephrine",
                "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "Theo dõi ECG liên tục (block AV, QT interval, rối loạn nhịp)",
                "Theo dõi ít nhất 24-48 giờ (do half-life rất dài 50-60 ngày)"
            ],
            "monitoring": "ECG liên tục (block AV, QT interval, rối loạn nhịp), huyết áp, nhịp tim, chức năng hô hấp, ý thức, điện giải (K+, Mg2+)"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Nên uống với thức ăn để giảm kích ứng dạ dày và tăng hấp thu.",
                "timing": "Loading dose: 800-1600mg/ngày chia 2 lần trong 1-2 tuần. Maintenance: 200-400mg x 1 lần/ngày. Uống cùng giờ mỗi ngày. KHÔNG ngừng đột ngột (half-life dài, nhưng có thể gây rối loạn nhịp)."
            },
            "iv": {
                "reconstitution": "Amiodarone IV: Dùng trực tiếp từ lọ. KHÔNG pha với các dung dịch khác trong cùng bơm tiêm (kết tủa).",
                "infusion_rate": "Loading: 150mg IV trong 10 phút, sau đó 1mg/phút x 6 giờ, 0.5mg/phút x 18 giờ. Maintenance: 0.5mg/phút. Theo dõi ECG và huyết áp liên tục. Chuyển sang PO càng sớm càng tốt.",
                "compatibility": ["D5W", "Normal saline"],
                "incompatibility": ["KHÔNG trộn với các thuốc khác trong cùng bơm tiêm (kết tủa)"],
                "notes": "Dùng cho cấp cứu rối loạn nhịp. Theo dõi ECG và huyết áp liên tục. Chuyển sang PO càng sớm càng tốt (trong vòng 24-48 giờ)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Cordarone (amiodarone)",
                "UpToDate - Amiodarone: Drug information",
                "EMERALD Study - Circulation",
                "ARREST Study - New England Journal of Medicine",
                "American Heart Association/American College of Cardiology guidelines - Arrhythmias"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Multiple RCTs (EMERALD, ARREST) and extensive clinical experience in life-threatening arrhythmias"
        }
      },
    "Flecainide": {
        "group": "Cardiovascular - Antiarrhythmic (Class IC)",
        "vietnamese_name": "Flecainide, Tambocor",
        "administration": ["PO"],
        "indications": [
            "Rung nhĩ (chuyển nhịp, duy trì nhịp xoang)",
            "Nhịp nhanh trên thất (SVT)",
            "Rối loạn nhịp thất (nếu không có bệnh tim cấu trúc)"
        ],
        "contraindications": [
            "Bệnh tim cấu trúc (suy tim, bệnh mạch vành, bệnh van tim)",
            "Block nhĩ thất độ 2-3",
            "Hội chứng Brugada",
            "QT kéo dài",
            "Suy thận nặng (CrCl <50)"
        ],
        "dosage": {
            "adult_po_loading": "200-300mg PO (chuyển nhịp AF)",
            "adult_po_maintenance": "100-200mg x 2 lần/ngày",
            "adult_max": "400mg/ngày",
            "notes": "CHỈ dùng nếu KHÔNG có bệnh tim cấu trúc. Theo dõi ECG trước và sau khi bắt đầu."
        },
        "side_effects": [
            "Rối loạn nhịp tim nặng (proarrhythmia)",
            "Block nhĩ thất",
            "Suy tim (nếu có bệnh tim)",
            "Chóng mặt",
            "Nhìn mờ",
            "Khó thở"
        ],
        "interactions": [
            "Amiodarone: tăng nồng độ flecainide",
            "Digoxin: tăng nồng độ digoxin",
            "Beta-blockers: tăng nguy cơ block nhĩ thất",
            "Verapamil, Diltiazem: tăng nguy cơ block nhĩ thất"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Class IC antiarrhythmic. Ức chế mạnh kênh Na+ voltage-gated, giảm tốc độ khử cực (phase 0), giảm dẫn truyền trong tim. Không ảnh hưởng đáng kể đến thời gian khử cực (QT interval). Hiệu quả cao cho rung nhĩ và SVT, nhưng có nguy cơ proarrhythmia cao, đặc biệt ở bệnh nhân có bệnh tim cấu trúc. CHỈ dùng nếu KHÔNG có bệnh tim cấu trúc (suy tim, bệnh mạch vành, bệnh van tim).",
        "monitoring": [
            "ECG: trước và sau khi bắt đầu, định kỳ (theo dõi QRS width, block AV)",
            "QRS width: tăng >25% hoặc QRS >150ms → giảm liều hoặc ngừng",
            "Block nhĩ thất: theo dõi dấu hiệu block AV",
            "Chức năng tim: siêu âm tim nếu có triệu chứng suy tim",
            "Nồng độ flecainide trong máu (nếu có thể, mục tiêu 0.2-1.0 mcg/mL)",
            "Chức năng thận (creatinine, eGFR) - điều chỉnh liều ở suy thận"
        ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI nếu có bệnh tim cấu trúc (suy tim, bệnh mạch vành, bệnh van tim) - nguy cơ proarrhythmia và suy tim cao",
            "CHỐNG CHỈ ĐỊNH nếu có hội chứng Brugada - nguy cơ rung thất",
            "CHỈ dùng nếu KHÔNG có bệnh tim cấu trúc - đánh giá siêu âm tim trước khi dùng",
            "Theo dõi ECG trước và sau khi bắt đầu - tăng QRS >25% hoặc QRS >150ms → giảm liều hoặc ngừng",
            "Theo dõi block nhĩ thất - có thể gây block AV độ 2-3",
            "Điều chỉnh liều ở suy thận (CrCl 30-50: giảm liều 25-50%; CrCl <30: tránh dùng)",
            "Tránh dùng với amiodarone (tăng nồng độ flecainide)",
            "Tránh dùng với beta-blockers, verapamil, diltiazem (tăng nguy cơ block AV)",
            "Theo dõi nồng độ digoxin nếu dùng cùng (flecainide tăng nồng độ digoxin)"
        ],
        "pharmacokinetics": {
            "half_life": "12-27 giờ",
            "onset": "1-6 giờ",
            "duration": "Dài (do half-life dài)",
            "protein_binding": "40-50%",
            "clearance": "Thận (thải trừ chủ yếu nguyên dạng 30-50%), gan (chuyển hóa một phần)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Có thể gây rối loạn nhịp tim nặng (proarrhythmia) và tử vong, đặc biệt ở bệnh nhân có bệnh tim cấu trúc. CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI nếu có suy tim, bệnh mạch vành, hoặc bệnh van tim. CHỈ dùng nếu KHÔNG có bệnh tim cấu trúc. Theo dõi ECG trước và sau khi bắt đầu.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Amiodarone",
                    "mechanism": "Amiodarone ức chế chuyển hóa flecainide, tăng nồng độ flecainide",
                    "effect": "Tăng nồng độ flecainide, tăng nguy cơ proarrhythmia và độc tính",
                    "management": "TRÁNH dùng chung. Nếu bắt buộc: giảm liều flecainide 50%. Theo dõi ECG và nồng độ flecainide chặt chẽ."
                },
                {
                    "drug": "Beta-blockers, Verapamil, Diltiazem",
                    "mechanism": "Tác dụng hiệp đồng ức chế dẫn truyền AV",
                    "effect": "Tăng nguy cơ block nhĩ thất độ 2-3",
                    "management": "Thận trọng. Theo dõi ECG chặt chẽ. Có thể cần giảm liều một trong hai thuốc."
                }
            ],
            "moderate": [
                {
                    "drug": "Digoxin",
                    "mechanism": "Flecainide tăng nồng độ digoxin (ức chế P-glycoprotein)",
                    "effect": "Tăng nồng độ digoxin, tăng nguy cơ ngộ độc digoxin",
                    "management": "Theo dõi nồng độ digoxin. Có thể cần giảm liều digoxin."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Bệnh tim cấu trúc (suy tim, bệnh mạch vành, bệnh van tim)",
                "Block nhĩ thất độ 2-3",
                "Hội chứng Brugada",
                "QT kéo dài",
                "Suy thận nặng (CrCl <30)"
            ],
            "tương_đối": [
                "Suy thận (CrCl 30-50) - giảm liều 25-50%",
                "Block nhĩ thất độ 1 - có thể làm nặng block",
                "Dùng với amiodarone - tăng nồng độ flecainide",
                "Dùng với beta-blockers, verapamil, diltiazem - tăng nguy cơ block AV"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Chứng cứ về an toàn trong thai kỳ còn hạn chế. Có thể dùng nếu lợi ích vượt quá nguy cơ. Thận trọng.",
            "lactation": {
                "safety": "Unknown",
                "details": "Không có dữ liệu về bài tiết flecainide vào sữa mẹ. Thận trọng khi dùng khi cho con bú.",
                "recommendation": "Tránh dùng khi cho con bú nếu có thể. Nếu phải dùng, theo dõi trẻ sát."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, có thể giảm liều nhẹ",
            "severe": "Thận trọng, giảm liều hoặc tránh dùng",
            "notes": "Flecainide chuyển hóa một phần ở gan. Suy gan có thể làm giảm chuyển hóa, tăng nguy cơ tích lũy."
        },
        "overdose_management": {
            "symptoms": [
                "Rối loạn nhịp tim nặng (proarrhythmia, rung thất)",
                "Block nhĩ thất độ 2-3",
                "Suy tim cấp",
                "Chóng mặt, lú lẫn",
                "Co giật (hiếm)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị rối loạn nhịp.",
            "treatment": [
                "Theo dõi ECG liên tục",
                "Hỗ trợ hô hấp nếu cần",
                "Điều trị rối loạn nhịp tim (theo protocol ACLS)",
                "Pacemaker nếu block AV nặng",
                "Hỗ trợ tim mạch (IV fluids, vasopressors nếu hạ huyết áp)",
                "Than hoạt tính nếu uống trong vòng 1-2 giờ",
                "Theo dõi ít nhất 24-48 giờ (half-life 12-27 giờ)"
            ],
            "monitoring": "ECG liên tục, huyết áp, nhịp tim, hô hấp, ý thức"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể dùng với hoặc không có thức ăn.",
                "timing": "Chia 2 lần/ngày (sáng, tối). Bắt đầu với liều thấp (100mg x 2 lần/ngày), tăng dần nếu dung nạp."
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
                "FDA Drug Label - Tambocor (flecainide)",
                "UpToDate - Flecainide: Drug information",
                "ACC/AHA/ESC Guidelines for Atrial Fibrillation"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - Multiple RCTs and clinical guidelines"
        }
    },
    "Propafenone": {
        "group": "Cardiovascular - Antiarrhythmic (Class IC)",
        "vietnamese_name": "Propafenone, Rythmol",
        "administration": ["PO"],
        "indications": [
            "Rung nhĩ (chuyển nhịp, duy trì nhịp xoang)",
            "Nhịp nhanh trên thất (SVT)",
            "Rối loạn nhịp thất (nếu không có bệnh tim cấu trúc)"
        ],
        "contraindications": [
            "Bệnh tim cấu trúc (suy tim, bệnh mạch vành, bệnh van tim)",
            "Block nhĩ thất độ 2-3",
            "Hội chứng Brugada",
            "QT kéo dài",
            "Suy gan nặng",
            "Suy thận nặng (CrCl <30)"
        ],
        "dosage": {
            "adult_po_loading": "450-600mg PO (chuyển nhịp AF)",
            "adult_po_maintenance": "150-300mg x 3 lần/ngày",
            "adult_max": "900mg/ngày",
            "notes": "CHỈ dùng nếu KHÔNG có bệnh tim cấu trúc. Theo dõi ECG trước và sau khi bắt đầu."
        },
        "side_effects": [
            "Rối loạn nhịp tim nặng (proarrhythmia)",
            "Block nhĩ thất",
            "Suy tim (nếu có bệnh tim)",
            "Chóng mặt",
            "Vị kim loại",
            "Buồn nôn"
        ],
        "interactions": [
            "Amiodarone: tăng nồng độ propafenone",
            "Digoxin: tăng nồng độ digoxin",
            "Beta-blockers: tăng nguy cơ block nhĩ thất (propafenone có tác dụng beta-blocker)",
            "Warfarin: tăng INR"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Class IC antiarrhythmic với tác dụng beta-blocker bổ sung. Ức chế mạnh kênh Na+ voltage-gated, giảm tốc độ khử cực (phase 0), giảm dẫn truyền trong tim. Cũng có tác dụng chẹn beta (nhẹ), có thể gây block nhĩ thất. Không ảnh hưởng đáng kể đến thời gian khử cực (QT interval). Hiệu quả cao cho rung nhĩ và SVT, nhưng có nguy cơ proarrhythmia cao, đặc biệt ở bệnh nhân có bệnh tim cấu trúc. CHỈ dùng nếu KHÔNG có bệnh tim cấu trúc.",
        "monitoring": [
            "ECG: trước và sau khi bắt đầu, định kỳ (theo dõi QRS width, block AV)",
            "QRS width: tăng >25% hoặc QRS >150ms → giảm liều hoặc ngừng",
            "Block nhĩ thất: theo dõi dấu hiệu block AV",
            "Chức năng tim: siêu âm tim nếu có triệu chứng suy tim",
            "Nồng độ propafenone trong máu (nếu có thể)",
            "Chức năng gan (ALT, AST) - điều chỉnh liều ở suy gan",
            "Chức năng thận (creatinine, eGFR) - điều chỉnh liều ở suy thận"
        ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI nếu có bệnh tim cấu trúc (suy tim, bệnh mạch vành, bệnh van tim) - nguy cơ proarrhythmia và suy tim cao",
            "CHỐNG CHỈ ĐỊNH nếu có hội chứng Brugada - nguy cơ rung thất",
            "CHỈ dùng nếu KHÔNG có bệnh tim cấu trúc - đánh giá siêu âm tim trước khi dùng",
            "Theo dõi ECG trước và sau khi bắt đầu - tăng QRS >25% hoặc QRS >150ms → giảm liều hoặc ngừng",
            "Theo dõi block nhĩ thất - có thể gây block AV độ 2-3 (do tác dụng beta-blocker)",
            "Điều chỉnh liều ở suy gan (giảm liều 25-50%)",
            "Điều chỉnh liều ở suy thận (CrCl 30-50: giảm liều 25-50%; CrCl <30: tránh dùng)",
            "Tránh dùng với amiodarone (tăng nồng độ propafenone)",
            "Tránh dùng với beta-blockers (tăng nguy cơ block AV do tác dụng hiệp đồng)",
            "Theo dõi nồng độ digoxin nếu dùng cùng (propafenone tăng nồng độ digoxin)",
            "Theo dõi INR nếu dùng với warfarin (propafenone tăng INR)"
        ],
        "pharmacokinetics": {
            "half_life": "2-10 giờ (ngắn hơn flecainide)",
            "onset": "1-3 giờ",
            "duration": "Ngắn hơn flecainide (do half-life ngắn hơn)",
            "protein_binding": ">95%",
            "clearance": "Gan (chuyển hóa qua CYP2D6, CYP3A4), thận (thải trừ một phần)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Có thể gây rối loạn nhịp tim nặng (proarrhythmia) và tử vong, đặc biệt ở bệnh nhân có bệnh tim cấu trúc. CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI nếu có suy tim, bệnh mạch vành, hoặc bệnh van tim. CHỈ dùng nếu KHÔNG có bệnh tim cấu trúc. Theo dõi ECG trước và sau khi bắt đầu.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Amiodarone",
                    "mechanism": "Amiodarone ức chế chuyển hóa propafenone, tăng nồng độ propafenone",
                    "effect": "Tăng nồng độ propafenone, tăng nguy cơ proarrhythmia và độc tính",
                    "management": "TRÁNH dùng chung. Nếu bắt buộc: giảm liều propafenone 50%. Theo dõi ECG chặt chẽ."
                },
                {
                    "drug": "Beta-blockers",
                    "mechanism": "Tác dụng hiệp đồng chẹn beta (propafenone có tác dụng beta-blocker)",
                    "effect": "Tăng nguy cơ block nhĩ thất độ 2-3, nhịp tim chậm",
                    "management": "Thận trọng. Theo dõi ECG chặt chẽ. Có thể cần giảm liều một trong hai thuốc."
                }
            ],
            "moderate": [
                {
                    "drug": "Digoxin",
                    "mechanism": "Propafenone tăng nồng độ digoxin (ức chế P-glycoprotein)",
                    "effect": "Tăng nồng độ digoxin, tăng nguy cơ ngộ độc digoxin",
                    "management": "Theo dõi nồng độ digoxin. Có thể cần giảm liều digoxin."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Propafenone ức chế chuyển hóa warfarin (CYP2C9)",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên. Có thể cần giảm liều warfarin."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Bệnh tim cấu trúc (suy tim, bệnh mạch vành, bệnh van tim)",
                "Block nhĩ thất độ 2-3",
                "Hội chứng Brugada",
                "QT kéo dài",
                "Suy gan nặng",
                "Suy thận nặng (CrCl <30)"
            ],
            "tương_đối": [
                "Suy gan - giảm liều 25-50%",
                "Suy thận (CrCl 30-50) - giảm liều 25-50%",
                "Block nhĩ thất độ 1 - có thể làm nặng block",
                "Dùng với amiodarone - tăng nồng độ propafenone",
                "Dùng với beta-blockers - tăng nguy cơ block AV"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Chứng cứ về an toàn trong thai kỳ còn hạn chế. Có thể dùng nếu lợi ích vượt quá nguy cơ. Thận trọng.",
            "lactation": {
                "safety": "Unknown",
                "details": "Không có dữ liệu về bài tiết propafenone vào sữa mẹ. Thận trọng khi dùng khi cho con bú.",
                "recommendation": "Tránh dùng khi cho con bú nếu có thể. Nếu phải dùng, theo dõi trẻ sát."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Giảm liều 25-50%. Theo dõi chức năng gan",
            "severe": "Tránh dùng. Theo dõi chức năng gan chặt chẽ",
            "notes": "Propafenone chuyển hóa mạnh ở gan qua CYP2D6, CYP3A4. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy và tác dụng phụ."
        },
        "overdose_management": {
            "symptoms": [
                "Rối loạn nhịp tim nặng (proarrhythmia, rung thất)",
                "Block nhĩ thất độ 2-3",
                "Suy tim cấp",
                "Chóng mặt, lú lẫn",
                "Co giật (hiếm)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị rối loạn nhịp.",
            "treatment": [
                "Theo dõi ECG liên tục",
                "Hỗ trợ hô hấp nếu cần",
                "Điều trị rối loạn nhịp tim (theo protocol ACLS)",
                "Pacemaker nếu block AV nặng",
                "Hỗ trợ tim mạch (IV fluids, vasopressors nếu hạ huyết áp)",
                "Than hoạt tính nếu uống trong vòng 1-2 giờ",
                "Theo dõi ít nhất 12-24 giờ (half-life 2-10 giờ)"
            ],
            "monitoring": "ECG liên tục, huyết áp, nhịp tim, hô hấp, ý thức"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể dùng với hoặc không có thức ăn.",
                "timing": "Chia 3 lần/ngày (sáng, trưa, tối). Bắt đầu với liều thấp (150mg x 3 lần/ngày), tăng dần nếu dung nạp."
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
                "FDA Drug Label - Rythmol (propafenone)",
                "UpToDate - Propafenone: Drug information",
                "ACC/AHA/ESC Guidelines for Atrial Fibrillation"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - Multiple RCTs and clinical guidelines"
        }
    },

    "Dronedarone": {
        "group": "Cardiovascular - Antiarrhythmic (Class III)",
        "vietnamese_name": "Dronedarone, Multaq",
        "administration": ["PO"],
        "indications": [
            "Rung nhĩ",
            "Cuồng nhĩ"
        ],
        "contraindications": [
            "Suy tim nặng (NYHA class IV) hoặc suy tim không ổn định",
            "Block nhĩ thất độ 2-3 không có máy tạo nhịp",
            "Nhịp chậm <50 bpm",
            "QT prolongation nặng",
            "Bệnh gan nặng"
        ],
        "dosage": {
            "adult_standard": "400mg x 2 lần/ngày (sáng và tối)",
            "adult_max": "800mg/ngày",
            "notes": "Dẫn xuất của amiodarone nhưng ít tác dụng phụ hơn. CHỐNG CHỈ ĐỊNH trong suy tim nặng."
        },
        "side_effects": [
            "Bệnh gan (hiếm nhưng nguy hiểm)",
            "QT prolongation",
            "Nhịp chậm",
            "Suy tim (CHỐNG CHỈ ĐỊNH trong suy tim nặng)",
            "Phổi (ít hơn amiodarone)",
            "Tăng creatinine (do ức chế creatinine transporter, không phải suy thận thực sự)"
        ],
        "interactions": [
            "Digoxin: tăng nồng độ digoxin (giảm liều digoxin 50%)",
            "Warfarin: tăng tác dụng chống đông",
            "Statins: tăng nguy cơ tiêu cơ vân",
            "CYP3A4 inhibitors: tăng nồng độ dronedarone"
        ],
        "pregnancy": "X",
        "mechanism_of_action": "Class III antiarrhythmic, dẫn xuất của amiodarone nhưng đã loại bỏ iodine và thêm nhóm methanesulfonyl. Ức chế kênh K+ (delayed rectifier), kéo dài phase 3 của action potential, kéo dài QT interval. Cũng có tác dụng ức chế Na+ channels (class I), chẹn beta (class II), và chẹn Ca2+ (class IV). Ít tác dụng phụ hơn amiodarone (ít bệnh phổi, ít rối loạn tuyến giáp) nhưng CHỐNG CHỈ ĐỊNH trong suy tim nặng (tăng nguy cơ tử vong).",
        "monitoring": [
            "ECG: QT interval, nhịp tim",
            "Chức năng gan: ALT, AST, bilirubin (mỗi 3 tháng) - nguy cơ bệnh gan hiếm nhưng nguy hiểm",
            "Creatinine - có thể tăng do ức chế creatinine transporter (không phải suy thận thực sự)",
            "Dấu hiệu suy tim - CHỐNG CHỈ ĐỊNH trong suy tim nặng",
            "Chức năng phổi (ít hơn amiodarone nhưng vẫn cần theo dõi)"
        ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH trong suy tim nặng (NYHA class IV) hoặc suy tim không ổn định - tăng nguy cơ tử vong",
            "CHỐNG CHỈ ĐỊNH trong bệnh gan nặng - nguy cơ bệnh gan hiếm nhưng nguy hiểm",
            "Theo dõi chức năng gan mỗi 3 tháng - ngừng ngay nếu có dấu hiệu bệnh gan",
            "Tăng creatinine - do ức chế creatinine transporter, không phải suy thận thực sự, không cần điều chỉnh liều",
            "Giảm liều digoxin 50% khi dùng với dronedarone",
            "Theo dõi INR nếu dùng với warfarin",
            "Ít tác dụng phụ hơn amiodarone nhưng vẫn cần theo dõi chặt chẽ"
        ],
        "pharmacokinetics": {
            "half_life": "13-19 giờ",
            "onset": "Vài ngày",
            "duration": "12 giờ (dùng 2 lần/ngày)",
            "protein_binding": ">98%",
            "clearance": "Gan: chuyển hóa qua CYP3A4. Thận: bài tiết một phần."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH trong suy tim nặng (NYHA class IV) hoặc suy tim không ổn định - tăng nguy cơ tử vong. Nguy cơ bệnh gan hiếm nhưng nguy hiểm - theo dõi chức năng gan mỗi 3 tháng, ngừng ngay nếu có dấu hiệu bệnh gan.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Digoxin",
                    "mechanism": "Giảm thải trừ digoxin qua thận",
                    "effect": "Tăng nồng độ digoxin, tăng độc tính",
                    "management": "Giảm liều digoxin 50%. Theo dõi nồng độ digoxin."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Ức chế chuyển hóa warfarin",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên. Có thể cần giảm liều warfarin."
                },
                {
                    "drug": "CYP3A4 inhibitors (ketoconazole, clarithromycin)",
                    "mechanism": "Ức chế chuyển hóa dronedarone",
                    "effect": "Tăng nồng độ dronedarone, tăng tác dụng phụ",
                    "management": "Tránh dùng chung. Nếu phải dùng, giảm liều dronedarone."
                }
            ],
            "moderate": [
                {
                    "drug": "Statins (simvastatin, atorvastatin)",
                    "mechanism": "Cả hai đều chuyển hóa qua CYP3A4",
                    "effect": "Tăng nguy cơ tiêu cơ vân",
                    "management": "Thận trọng. Theo dõi CK, triệu chứng tiêu cơ vân."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Suy tim nặng (NYHA class IV) hoặc suy tim không ổn định - CHỐNG CHỈ ĐỊNH (tăng nguy cơ tử vong)",
                "Bệnh gan nặng - CHỐNG CHỈ ĐỊNH",
                "Block nhĩ thất độ 2-3 không có máy tạo nhịp",
                "Nhịp chậm <50 bpm",
                "QT prolongation nặng",
                "Dùng với CYP3A4 inhibitors mạnh"
            ],
            "tương_đối": [
                "Suy tim nhẹ đến trung bình (NYHA class I-III) - thận trọng",
                "Suy gan nhẹ đến trung bình - thận trọng, theo dõi chặt chẽ",
                "Suy thận - tăng creatinine có thể xảy ra (không phải suy thận thực sự)",
                "Dùng với digoxin - giảm liều digoxin 50%",
                "Dùng với warfarin - theo dõi INR"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": "Category X - chống chỉ định trong thai kỳ. Có thể gây dị tật thai nhi.",
            "lactation": {
                "safety": "Not recommended",
                "details": "Bài tiết vào sữa mẹ. Không nên dùng khi cho con bú.",
                "recommendation": "Tránh dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, theo dõi chặt chẽ",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Chuyển hóa qua gan (CYP3A4). Suy gan nặng là chống chỉ định. Nguy cơ bệnh gan hiếm nhưng nguy hiểm - theo dõi chức năng gan mỗi 3 tháng."
        },
        "overdose_management": {
            "symptoms": [
                "QT prolongation nặng, rối loạn nhịp tim",
                "Nhịp chậm nặng",
                "Suy tim nặng",
                "Bệnh gan",
                "Ức chế CNS"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Theo dõi ECG liên tục (quan trọng - nguy cơ QT prolongation, rối loạn nhịp tim)",
                "Điều trị rối loạn nhịp tim nếu có",
                "Theo dõi chức năng gan (nguy cơ bệnh gan)",
                "Hỗ trợ tim mạch nếu có suy tim",
                "Lọc máu: ít hiệu quả (protein binding >98%)"
            ],
            "monitoring": "Theo dõi liên tục ECG, huyết áp, nhịp tim, chức năng gan trong ít nhất 24-48 giờ"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn để tăng hấp thu.",
                "timing": "Dùng 2 lần/ngày (sáng và tối), cách nhau 12 giờ. Uống với bữa ăn."
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
                "FDA Drug Label - Multaq (Dronedarone)",
                "UpToDate - Dronedarone: Drug information",
                "ACC/AHA/ESC Guidelines for Atrial Fibrillation"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - FDA approved, clinical guidelines"
        }
    },

    "Procainamide": {
        "group": "Cardiovascular - Antiarrhythmic (Class IA)",
        "vietnamese_name": "Procainamide, Pronestyl",
        "administration": ["PO", "IV"],
        "indications": [
            "Rối loạn nhịp thất",
            "Rung nhĩ",
            "Nhịp nhanh trên thất"
        ],
        "contraindications": [
            "Block nhĩ thất độ 2-3 không có máy tạo nhịp",
            "Suy tim nặng",
            "Lupus ban đỏ hệ thống",
            "Dị ứng procainamide"
        ],
        "dosage": {
            "adult_po": "250-500mg mỗi 3-6 giờ (tối đa 4g/ngày)",
            "adult_iv_loading": "15-17mg/kg IV trong 30-60 phút",
            "adult_iv_maintenance": "2-6mg/phút",
            "adult_max": "4g/ngày (PO), 2g/ngày (IV)",
            "notes": "Class IA antiarrhythmic. Nguy cơ lupus ban đỏ hệ thống khi dùng lâu dài (>6 tháng)."
        },
        "side_effects": [
            "Lupus ban đỏ hệ thống (khi dùng lâu dài >6 tháng)",
            "QT prolongation, rối loạn nhịp tim",
            "Hạ huyết áp (IV)",
            "Block nhĩ thất",
            "Giảm bạch cầu (hiếm)",
            "Buồn nôn, nôn"
        ],
        "interactions": [
            "Cimetidine: tăng nồng độ procainamide",
            "Quinidine: tăng tác dụng phụ",
            "QT prolonging drugs: tăng nguy cơ rối loạn nhịp"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Class IA antiarrhythmic. Ức chế kênh Na+ (phase 0), làm chậm dẫn truyền và kéo dài repolarization (phase 3). Kéo dài QT interval và PR interval. Hiệu quả cho rối loạn nhịp thất và trên thất. Nguy cơ lupus ban đỏ hệ thống khi dùng lâu dài (>6 tháng) do tạo autoantibodies. Active metabolite N-acetylprocainamide (NAPA) cũng có tác dụng antiarrhythmic.",
        "monitoring": [
            "ECG: QT interval, PR interval, QRS duration - nguy cơ QT prolongation, block nhĩ thất",
            "Dấu hiệu lupus ban đỏ hệ thống (khi dùng lâu dài >6 tháng): đau khớp, ban da, sốt, mệt mỏi",
            "Công thức máu - hiếm giảm bạch cầu",
            "Huyết áp (đặc biệt khi dùng IV)",
            "Nồng độ procainamide và NAPA (therapeutic range: procainamide 4-10mcg/ml, NAPA 10-30mcg/ml)"
        ],
        "precautions": [
            "Nguy cơ lupus ban đỏ hệ thống khi dùng lâu dài (>6 tháng) - cần đánh giá định kỳ, cân nhắc chuyển thuốc khác",
            "QT prolongation - nguy cơ rối loạn nhịp tim, cần theo dõi ECG",
            "Hạ huyết áp - đặc biệt khi dùng IV, truyền chậm",
            "Block nhĩ thất - thận trọng ở bệnh nhân có block nhĩ thất",
            "Giảm bạch cầu - hiếm nhưng nguy hiểm, theo dõi công thức máu",
            "Theo dõi nồng độ procainamide và NAPA nếu dùng lâu dài",
            "Giảm liều ở suy thận (NAPA tích lũy)"
        ],
        "pharmacokinetics": {
            "half_life": "3-4 giờ (procainamide), 6-8 giờ (NAPA metabolite)",
            "onset": "30-60 phút (PO), 5-10 phút (IV)",
            "duration": "3-6 giờ",
            "protein_binding": "15-20%",
            "clearance": "Gan: chuyển hóa thành NAPA (active metabolite). Thận: bài tiết chủ yếu (50-60% nguyên dạng, 10-30% NAPA)."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Dạng IV: bảo quản ở nhiệt độ phòng, không đông lạnh.",
        "black_box_warnings": "Nguy cơ lupus ban đỏ hệ thống khi dùng lâu dài (>6 tháng). QT prolongation có thể gây rối loạn nhịp tim nghiêm trọng.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "QT prolonging drugs",
                    "mechanism": "Cả hai đều kéo dài QT",
                    "effect": "Tăng nguy cơ rối loạn nhịp tim",
                    "management": "Tránh dùng chung nếu có thể. Theo dõi ECG chặt chẽ."
                }
            ],
            "moderate": [
                {
                    "drug": "Cimetidine",
                    "mechanism": "Giảm thải trừ procainamide qua thận",
                    "effect": "Tăng nồng độ procainamide, tăng tác dụng phụ",
                    "management": "Giảm liều procainamide 25-50%. Theo dõi nồng độ."
                },
                {
                    "drug": "Quinidine",
                    "mechanism": "Cả hai đều là class IA, tác dụng hiệp đồng",
                    "effect": "Tăng tác dụng phụ, tăng nguy cơ QT prolongation",
                    "management": "Tránh dùng chung."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng procainamide",
                "Block nhĩ thất độ 2-3 không có máy tạo nhịp",
                "Suy tim nặng",
                "Lupus ban đỏ hệ thống đang hoạt động"
            ],
            "tương_đối": [
                "Suy thận nặng - NAPA tích lũy, giảm liều",
                "Suy gan nặng - thận trọng",
                "Block nhĩ thất độ 1 - thận trọng",
                "QT prolongation - tăng nguy cơ rối loạn nhịp tim"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C. Có thể dùng khi cần thiết.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Bài tiết vào sữa mẹ ở nồng độ thấp.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng, giảm liều",
            "notes": "Chuyển hóa qua gan thành NAPA. Suy gan có thể ảnh hưởng chuyển hóa."
        },
        "overdose_management": {
            "symptoms": [
                "QT prolongation nặng, rối loạn nhịp tim",
                "Block nhĩ thất nặng",
                "Hạ huyết áp nặng",
                "Ức chế CNS"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Theo dõi ECG liên tục (quan trọng - nguy cơ QT prolongation, rối loạn nhịp tim)",
                "Điều trị rối loạn nhịp tim nếu có",
                "Điều trị hạ huyết áp: truyền dịch, vasopressors nếu cần",
                "Lọc máu: có thể hiệu quả (protein binding thấp 15-20%)"
            ],
            "monitoring": "Theo dõi liên tục ECG, huyết áp, nhịp tim trong ít nhất 6-12 giờ"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với thức ăn hoặc không.",
                "timing": "Mỗi 3-6 giờ. Liều tối đa: 4g/ngày."
            },
            "iv": {
                "reconstitution": "Pha trong 0.9% NaCl hoặc D5W. Nồng độ: 100mg/ml.",
                "infusion_rate": "Loading: 15-17mg/kg trong 30-60 phút. Maintenance: 2-6mg/phút.",
                "compatibility": ["0.9% NaCl", "D5W"],
                "incompatibility": [],
                "notes": "Truyền chậm để tránh hạ huyết áp. Theo dõi ECG liên tục."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Pronestyl (Procainamide)",
                "UpToDate - Procainamide: Drug information",
                "ACC/AHA/ESC Guidelines for Atrial Fibrillation"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - FDA approved, clinical guidelines"
        }
    },
    
    "Sotalol": {
        "group": "Cardiovascular - Antiarrhythmic (Class III)",
        "vietnamese_name": "Sotalol, Betapace",
        "administration": ["PO", "IV"],
        "indications": [
            "Rung nhĩ (atrial fibrillation) - duy trì nhịp xoang",
            "Cuồng nhĩ (atrial flutter) - duy trì nhịp xoang",
            "Nhịp nhanh trên thất (SVT)",
            "Rối loạn nhịp thất (ventricular arrhythmias)",
            "Rung thất (ventricular fibrillation) - dự phòng",
            "Nhịp nhanh thất (ventricular tachycardia) - dự phòng"
        ],
        "contraindications": [
            "Dị ứng sotalol",
            "QT kéo dài (QTc >450ms) - CHỐNG CHỈ ĐỊNH",
            "Torsades de pointes - CHỐNG CHỈ ĐỊNH",
            "Suy tim nặng (NYHA class IV) - CHỐNG CHỈ ĐỊNH",
            "Block nhĩ thất độ 2-3 không có máy tạo nhịp - CHỐNG CHỈ ĐỊNH",
            "Hạ kali máu, hạ magie máu - CHỐNG CHỈ ĐỊNH (phải điều chỉnh trước)",
            "Hạ huyết áp nặng",
            "Hen phế quản nặng (do tác dụng chẹn beta)"
        ],
        "dosage": {
            "adult_po_loading": "80mg PO x 2 lần/ngày, tăng dần mỗi 3 ngày",
            "adult_po_maintenance": "80-160mg PO x 2 lần/ngày (tối đa 320mg/ngày)",
            "adult_po_max": "320mg/ngày (160mg x 2 lần/ngày)",
            "adult_iv": "75-150mg IV trong 5 phút, sau đó 10mg/phút IV infusion",
            "pediatric_po": "2mg/kg/ngày PO chia 2 lần (tối đa 160mg/ngày)",
            "notes": "PHẢI bắt đầu trong bệnh viện với monitoring ECG 3 ngày (nguy cơ torsades de pointes). Điều chỉnh liều theo QTc và chức năng thận. Phải đảm bảo K+ và Mg2+ bình thường trước khi dùng."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 50% hoặc tăng khoảng cách (q12h → q24h)",
            "under_30": "Giảm liều 75% hoặc tăng khoảng cách đáng kể (q24-48h)",
            "hemodialysis": "Liều sau lọc máu, cần điều chỉnh theo QTc"
        },
        "side_effects": [
            "Torsades de pointes (nguy hiểm tính mạng) - nguy cơ cao trong 3 ngày đầu",
            "Kéo dài QT interval (QTc >500ms nguy hiểm)",
            "Nhịp chậm (bradycardia) - do tác dụng chẹn beta",
            "Block nhĩ thất (AV block)",
            "Suy tim (heart failure) - do tác dụng chẹn beta",
            "Hạ huyết áp",
            "Mệt mỏi, yếu cơ",
            "Khó thở (do chẹn beta)",
            "Co thắt phế quản (ở bệnh nhân hen)"
        ],
        "interactions": [
            "Thuốc kéo dài QT: tăng nguy cơ torsades de pointes",
            "Digoxin: tăng nguy cơ block AV",
            "Calcium channel blockers (verapamil, diltiazem): tăng nguy cơ block AV, nhịp chậm",
            "Thuốc lợi tiểu: tăng nguy cơ hạ K+/Mg2+, tăng nguy cơ torsades"
        ],
        "pregnancy": "B - Thận trọng trong thai kỳ",
        "mechanism_of_action": "Sotalol là class III antiarrhythmic với tác dụng chẹn beta (non-selective beta-blocker). Có hai tác dụng chính: (1) Class III: ức chế kênh K+ (delayed rectifier IKr), kéo dài phase 3 của action potential, kéo dài QT interval và effective refractory period (ERP), (2) Chẹn beta: ức chế beta-1 và beta-2 receptors, giảm nhịp tim, giảm co bóp cơ tim. Kết quả: giảm nhịp tim, kéo dài QT interval, tăng nguy cơ torsades de pointes (đặc biệt trong 3 ngày đầu). Phổ: hiệu quả với rung nhĩ, cuồng nhĩ, rối loạn nhịp thất. ĐẶC ĐIỂM: PHẢI bắt đầu trong bệnh viện với monitoring ECG 3 ngày (nguy cơ torsades de pointes cao trong 3 ngày đầu).",
        "monitoring": [
            "ECG liên tục trong 3 ngày đầu (BẮT BUỘC) - theo dõi QTc, torsades de pointes",
            "QTc interval - MỤC TIÊU: <450ms, NGUY HIỂM: >500ms hoặc tăng >60ms",
            "Nhịp tim và huyết áp - theo dõi nhịp chậm, hạ huyết áp",
            "Điện giải (K+, Mg2+) - PHẢI bình thường trước khi dùng, theo dõi định kỳ",
            "Chức năng thận (creatinine, eGFR) - điều chỉnh liều theo thận",
            "Dấu hiệu suy tim (khó thở, phù, tăng cân) - do tác dụng chẹn beta",
            "Dấu hiệu block AV (nhịp chậm, block nhĩ thất)",
            "Dấu hiệu torsades de pointes (ngất, rối loạn nhịp) - NGỪNG NGAY nếu có"
        ],
        "precautions": [
            "PHẢI bắt đầu trong bệnh viện với monitoring ECG 3 ngày (nguy cơ torsades de pointes cao trong 3 ngày đầu)",
            "CHỐNG CHỈ ĐỊNH nếu QTc >450ms hoặc có tiền sử torsades de pointes",
            "PHẢI đảm bảo K+ và Mg2+ bình thường trước khi dùng (giảm K+/Mg2+ tăng nguy cơ torsades)",
            "Điều chỉnh liều theo chức năng thận (eGFR) - QUAN TRỌNG",
            "NGỪNG NGAY nếu QTc >500ms hoặc tăng >60ms",
            "NGỪNG NGAY nếu có torsades de pointes",
            "CHỐNG CHỈ ĐỊNH trong suy tim nặng (NYHA class IV) - do tác dụng chẹn beta",
            "CHỐNG CHỈ ĐỊNH trong block AV độ 2-3 không có máy tạo nhịp",
            "Thận trọng ở bệnh nhân hen phế quản (chẹn beta có thể gây co thắt phế quản)",
            "Tránh dùng với thuốc kéo dài QT khác",
            "Tránh dùng với thuốc lợi tiểu (tăng nguy cơ hạ K+/Mg2+)",
            "Theo dõi chức năng thận định kỳ (thải trừ qua thận)"
        ],
        "pharmacokinetics": {
            "half_life": "12 giờ",
            "onset": "1-2 giờ (PO), ngay lập tức (IV)",
            "duration": "12 giờ (liều q12h)",
            "protein_binding": "Không đáng kể",
            "clearance": "Thận (80-90% bài tiết nguyên dạng qua nước tiểu), cần điều chỉnh thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": "Nguy cơ torsades de pointes (rối loạn nhịp tim đe dọa tính mạng), đặc biệt trong 3 ngày đầu. PHẢI bắt đầu trong bệnh viện với monitoring ECG 3 ngày. CHỐNG CHỈ ĐỊNH nếu QTc >450ms, có tiền sử torsades de pointes, suy tim nặng (NYHA class IV), hoặc block AV độ 2-3. PHẢI đảm bảo K+ và Mg2+ bình thường trước khi dùng.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Thuốc kéo dài QT (Quinidine, Procainamide, Disopyramide, Amiodarone, Ibutilide, Dofetilide, Haloperidol, Chlorpromazine, Methadone, Macrolides, Fluoroquinolones)",
                    "mechanism": "Tác dụng hiệp đồng kéo dài QT interval",
                    "effect": "Tăng nguy cơ torsades de pointes, rối loạn nhịp tim đe dọa tính mạng",
                    "management": "TRÁNH DÙNG CHUNG. Nếu bắt buộc: theo dõi ECG sát, đảm bảo K+ và Mg2+ bình thường, theo dõi QTc chặt chẽ."
                },
                {
                    "drug": "Digoxin",
                    "mechanism": "Sotalol (chẹn beta) và digoxin đều làm chậm nhịp tim, tăng block AV",
                    "effect": "Tăng nguy cơ block AV, nhịp chậm nặng",
                    "management": "Thận trọng. Theo dõi ECG chặt chẽ. Có thể cần giảm liều digoxin hoặc sotalol."
                },
                {
                    "drug": "Calcium Channel Blockers (Verapamil, Diltiazem)",
                    "mechanism": "Cả hai đều làm chậm nhịp tim và dẫn truyền AV",
                    "effect": "Tăng nguy cơ block AV, nhịp chậm nặng, suy tim",
                    "management": "TRÁNH DÙNG CHUNG. Nếu bắt buộc: theo dõi ECG và huyết động chặt chẽ."
                }
            ],
            "moderate": [
                {
                    "drug": "Thuốc lợi tiểu (Furosemide, Thiazide)",
                    "mechanism": "Thuốc lợi tiểu gây hạ K+ và Mg2+, tăng nguy cơ torsades de pointes khi dùng với sotalol",
                    "effect": "Tăng nguy cơ torsades de pointes",
                    "management": "Theo dõi K+ và Mg2+ chặt chẽ. Bổ sung K+ và Mg2+ nếu cần. Có thể cần giảm liều thuốc lợi tiểu."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng sotalol",
                "QT kéo dài (QTc >450ms) - CHỐNG CHỈ ĐỊNH",
                "Torsades de pointes - CHỐNG CHỈ ĐỊNH",
                "Suy tim nặng (NYHA class IV) - CHỐNG CHỈ ĐỊNH (do tác dụng chẹn beta)",
                "Block nhĩ thất độ 2-3 không có máy tạo nhịp - CHỐNG CHỈ ĐỊNH",
                "Hạ kali máu, hạ magie máu - CHỐNG CHỈ ĐỊNH (phải điều chỉnh trước)",
                "Hạ huyết áp nặng"
            ],
            "tương_đối": [
                "Suy tim (NYHA class I-III) - thận trọng, có thể làm nặng",
                "Hen phế quản - thận trọng (chẹn beta có thể gây co thắt phế quản)",
                "Bệnh phổi tắc nghẽn mạn tính (COPD) - thận trọng",
                "Suy thận nặng (CrCl <30) - giảm liều 75%",
                "Bệnh nhân cao tuổi - tăng nhạy cảm, tăng nguy cơ tác dụng phụ",
                "Dùng với digoxin - tăng nguy cơ block AV",
                "Dùng với calcium channel blockers - tăng nguy cơ block AV"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Sotalol là thuốc phân loại B. Không có bằng chứng về nguy cơ dị tật thai nhi trong các nghiên cứu trên động vật. Các nghiên cứu trên người không cho thấy nguy cơ tăng dị tật bẩm sinh rõ ràng. Tuy nhiên, sotalol có thể qua nhau thai và có thể gây nhịp chậm ở thai nhi. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt trong điều trị rối loạn nhịp đe dọa tính mạng.",
            "lactation": {
                "safety": "Compatible with Caution",
                "details": "Sotalol bài tiết vào sữa mẹ ở nồng độ thấp. Không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ, nhưng có thể gây nhịp chậm nhẹ.",
                "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng. Theo dõi trẻ bú mẹ về dấu hiệu nhịp chậm."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Không cần điều chỉnh liều (thải trừ chủ yếu qua thận)",
            "notes": "Sotalol thải trừ chủ yếu qua thận (80-90% bài tiết nguyên dạng). Không cần điều chỉnh liều ở bệnh nhân suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Torsades de pointes (rối loạn nhịp tim đe dọa tính mạng)",
                "Nhịp chậm nặng (<40 bpm)",
                "Block AV độ 2-3",
                "Suy tim cấp",
                "Hạ huyết áp nặng",
                "Ngất, rối loạn ý thức"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ. Magnesium có thể giúp điều trị torsades de pointes.",
            "treatment": [
                "Ngừng ngay sotalol",
                "Theo dõi ECG liên tục",
                "Nếu torsades de pointes:",
                "  - Magnesium sulfate 1-2g IV bolus, sau đó 1-2g/giờ IV infusion",
                "  - Overdrive pacing nếu cần",
                "  - Isoproterenol IV nếu cần (tăng nhịp tim)",
                "Nếu nhịp chậm nặng hoặc block AV:",
                "  - Atropine 0.5-1mg IV (có thể không hiệu quả do chẹn beta)",
                "  - Isoproterenol IV (đối kháng chẹn beta)",
                "  - Glucagon 1-5mg IV (đối kháng chẹn beta)",
                "  - Máy tạo nhịp tạm thời nếu cần",
                "Nếu suy tim cấp:",
                "  - Inotrope (dobutamine, milrinone)",
                "  - Hỗ trợ hô hấp",
                "Nếu hạ huyết áp nặng:",
                "  - Bù dịch (NS, LR)",
                "  - Vasopressor (norepinephrine, epinephrine)",
                "Lọc máu (hemodialysis) - sotalol có thể được loại bỏ một phần",
                "Theo dõi: ECG, huyết áp, nhịp tim, QTc liên tục"
            ],
            "monitoring": "Theo dõi ECG, huyết áp, nhịp tim, QTc liên tục cho đến khi hồi phục. Theo dõi lâu hơn nếu có biến chứng (torsades de pointes, block AV, suy tim)."
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "agent": "Isoproterenol",
                    "mechanism": "Beta-agonist, đối kháng tác dụng chẹn beta của sotalol",
                    "indication": "Nhịp chậm nặng, block AV do sotalol",
                    "dose": "1-5 mcg/phút IV infusion, tăng dần đến khi đạt nhịp tim mục tiêu",
                    "caution": "Có thể gây tăng nhịp tim, rối loạn nhịp. Theo dõi ECG chặt chẽ."
                },
                {
                    "agent": "Glucagon",
                    "mechanism": "Đối kháng tác dụng chẹn beta (cơ chế không rõ ràng)",
                    "indication": "Nhịp chậm nặng, block AV do sotalol",
                    "dose": "1-5mg IV bolus, sau đó 1-5mg/giờ IV infusion",
                    "caution": "Có thể gây buồn nôn, nôn. Theo dõi đường huyết."
                },
                {
                    "agent": "Magnesium sulfate",
                    "mechanism": "Điều trị torsades de pointes",
                    "indication": "Torsades de pointes do sotalol",
                    "dose": "1-2g IV bolus, sau đó 1-2g/giờ IV infusion",
                    "caution": "Điều trị hỗ trợ cho torsades de pointes."
                }
            ],
            "notes": "Isoproterenol và glucagon có thể đối kháng tác dụng chẹn beta. Magnesium điều trị torsades de pointes."
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với hoặc không thức ăn. Có thể uống không thức ăn nếu cần.",
                "timing": "80-160mg PO x 2 lần/ngày (q12h). Bắt đầu với 80mg x 2 lần/ngày, tăng dần mỗi 3 ngày nếu cần. Tối đa: 320mg/ngày (160mg x 2 lần/ngày).",
                "notes": "QUAN TRỌNG: 1) PHẢI bắt đầu trong bệnh viện với monitoring ECG 3 ngày, 2) Điều chỉnh liều theo chức năng thận (CrCl <30: giảm liều 75%), 3) PHẢI đảm bảo K+ và Mg2+ bình thường trước khi dùng, 4) NGỪNG NGAY nếu QTc >500ms hoặc có torsades de pointes, 5) Theo dõi QTc định kỳ."
            },
            "iv": {
                "reconstitution": "Pha trong NS hoặc D5W.",
                "infusion_rate": "Loading: 75-150mg IV trong 5 phút. Maintenance: 10mg/phút IV infusion. Điều chỉnh theo đáp ứng và QTc.",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
                "incompatibility": [
                    "Không trộn với các thuốc khác. Dùng đường truyền riêng."
                ],
                "notes": "QUAN TRỌNG: 1) PHẢI monitoring ECG liên tục, 2) Theo dõi QTc chặt chẽ, 3) PHẢI đảm bảo K+ và Mg2+ bình thường, 4) NGỪNG NGAY nếu QTc >500ms hoặc có torsades de pointes."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Sotalol (Betapace)",
                "ACC/AHA/ESC Guidelines for Atrial Fibrillation",
                "UpToDate - Sotalol: Drug Information",
                "Medscape - Sotalol Drug Reference"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, ACC/AHA/ESC guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },
    
    "Dofetilide": {
        "group": "Cardiovascular - Antiarrhythmic (Class III)",
        "vietnamese_name": "Dofetilide, Tikosyn",
        "administration": ["PO"],
        "indications": [
            "Rung nhĩ (atrial fibrillation) - chuyển nhịp và duy trì nhịp xoang",
            "Cuồng nhĩ (atrial flutter) - chuyển nhịp và duy trì nhịp xoang"
        ],
        "contraindications": [
            "Dị ứng dofetilide",
            "QT kéo dài (QTc >440ms) - CHỐNG CHỈ ĐỊNH",
            "Torsades de pointes - CHỐNG CHỈ ĐỊNH",
            "Suy thận nặng (CrCl <20) - CHỐNG CHỈ ĐỊNH",
            "Dùng với thuốc kéo dài QT - CHỐNG CHỈ ĐỊNH",
            "Dùng với cimetidine, verapamil, ketoconazole, trimethoprim - CHỐNG CHỈ ĐỊNH"
        ],
        "dosage": {
            "adult_po_crcl_>60": "500mcg PO x 2 lần/ngày",
            "adult_po_crcl_40_60": "250mcg PO x 2 lần/ngày",
            "adult_po_crcl_20_40": "125mcg PO x 2 lần/ngày",
            "adult_po_crcl_<20": "CHỐNG CHỈ ĐỊNH",
            "notes": "PHẢI bắt đầu trong bệnh viện với monitoring ECG 3 ngày (nguy cơ torsades de pointes). Điều chỉnh liều theo chức năng thận (CrCl). PHẢI đảm bảo K+ và Mg2+ bình thường trước khi dùng. CHỈ được kê đơn bởi bác sĩ đã được đào tạo về dofetilide."
        },
        "renal_adjustment": {
            "normal": "Không đổi (CrCl >60: 500mcg x 2 lần/ngày)",
            "30_60": "Giảm liều 50% (CrCl 40-60: 250mcg x 2 lần/ngày)",
            "under_30": "Giảm liều 75% (CrCl 20-40: 125mcg x 2 lần/ngày), CHỐNG CHỈ ĐỊNH nếu CrCl <20"
        },
        "side_effects": [
            "Torsades de pointes (nguy hiểm tính mạng) - nguy cơ cao trong 3 ngày đầu",
            "Kéo dài QT interval (QTc >500ms nguy hiểm)",
            "Nhịp chậm (bradycardia)",
            "Đau đầu",
            "Chóng mặt",
            "Đau ngực",
            "Khó thở"
        ],
        "interactions": [
            "Cimetidine: tăng nồng độ dofetilide (CHỐNG CHỈ ĐỊNH)",
            "Verapamil: tăng nồng độ dofetilide (CHỐNG CHỈ ĐỊNH)",
            "Ketoconazole: tăng nồng độ dofetilide (CHỐNG CHỈ ĐỊNH)",
            "Trimethoprim: tăng nồng độ dofetilide (CHỐNG CHỈ ĐỊNH)",
            "Thuốc kéo dài QT: tăng nguy cơ torsades de pointes (CHỐNG CHỈ ĐỊNH)",
            "Thuốc lợi tiểu: tăng nguy cơ hạ K+/Mg2+, tăng nguy cơ torsades"
        ],
        "pregnancy": "C - Thận trọng trong thai kỳ",
        "mechanism_of_action": "Dofetilide là class III antiarrhythmic thuần túy. Ức chế kênh K+ (delayed rectifier IKr), kéo dài phase 3 của action potential, kéo dài QT interval và effective refractory period (ERP). Khác với sotalol (có tác dụng chẹn beta), dofetilide chỉ có tác dụng class III. Phổ: hiệu quả với rung nhĩ và cuồng nhĩ (chuyển nhịp và duy trì nhịp xoang). ĐẶC ĐIỂM: (1) PHẢI bắt đầu trong bệnh viện với monitoring ECG 3 ngày (nguy cơ torsades de pointes cao trong 3 ngày đầu), (2) CHỈ được kê đơn bởi bác sĩ đã được đào tạo về dofetilide, (3) Điều chỉnh liều theo chức năng thận (CrCl) - QUAN TRỌNG, (4) CHỐNG CHỈ ĐỊNH nếu CrCl <20, (5) CHỐNG CHỈ ĐỊNH với nhiều thuốc (cimetidine, verapamil, ketoconazole, trimethoprim), (6) PHẢI đảm bảo K+ và Mg2+ bình thường trước khi dùng.",
        "monitoring": [
            "ECG liên tục trong 3 ngày đầu (BẮT BUỘC) - theo dõi QTc, torsades de pointes",
            "QTc interval - MỤC TIÊU: <440ms, NGUY HIỂM: >500ms hoặc tăng >15%",
            "Nhịp tim và huyết áp - theo dõi nhịp chậm",
            "Điện giải (K+, Mg2+) - PHẢI bình thường trước khi dùng, theo dõi định kỳ",
            "Chức năng thận (creatinine, CrCl) - điều chỉnh liều theo thận, QUAN TRỌNG",
            "Dấu hiệu torsades de pointes (ngất, rối loạn nhịp) - NGỪNG NGAY nếu có"
        ],
        "precautions": [
            "PHẢI bắt đầu trong bệnh viện với monitoring ECG 3 ngày (nguy cơ torsades de pointes cao trong 3 ngày đầu)",
            "CHỈ được kê đơn bởi bác sĩ đã được đào tạo về dofetilide",
            "CHỐNG CHỈ ĐỊNH nếu QTc >440ms hoặc có tiền sử torsades de pointes",
            "CHỐNG CHỈ ĐỊNH nếu CrCl <20",
            "PHẢI đảm bảo K+ và Mg2+ bình thường trước khi dùng (giảm K+/Mg2+ tăng nguy cơ torsades)",
            "Điều chỉnh liều theo chức năng thận (CrCl) - QUAN TRỌNG",
            "NGỪNG NGAY nếu QTc >500ms hoặc tăng >15%",
            "NGỪNG NGAY nếu có torsades de pointes",
            "CHỐNG CHỈ ĐỊNH với cimetidine, verapamil, ketoconazole, trimethoprim (tăng nồng độ dofetilide)",
            "CHỐNG CHỈ ĐỊNH với thuốc kéo dài QT khác",
            "Tránh dùng với thuốc lợi tiểu (tăng nguy cơ hạ K+/Mg2+)",
            "Theo dõi chức năng thận định kỳ (thải trừ qua thận)"
        ],
        "pharmacokinetics": {
            "half_life": "10 giờ",
            "onset": "2-3 giờ",
            "duration": "12 giờ (liều q12h)",
            "protein_binding": "60-70%",
            "clearance": "Thận (80% bài tiết nguyên dạng qua nước tiểu), cần điều chỉnh thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": "Nguy cơ torsades de pointes (rối loạn nhịp tim đe dọa tính mạng), đặc biệt trong 3 ngày đầu. PHẢI bắt đầu trong bệnh viện với monitoring ECG 3 ngày. CHỐNG CHỈ ĐỊNH nếu QTc >440ms, có tiền sử torsades de pointes, hoặc CrCl <20. CHỈ được kê đơn bởi bác sĩ đã được đào tạo về dofetilide. PHẢI đảm bảo K+ và Mg2+ bình thường trước khi dùng.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Cimetidine, Verapamil, Ketoconazole, Trimethoprim",
                    "mechanism": "Ức chế CYP3A4 và P-gp, tăng nồng độ dofetilide",
                    "effect": "Tăng nồng độ dofetilide đáng kể, tăng nguy cơ torsades de pointes, nguy hiểm tính mạng",
                    "management": "CHỐNG CHỈ ĐỊNH tuyệt đối. KHÔNG được dùng đồng thời với dofetilide."
                },
                {
                    "drug": "Thuốc kéo dài QT (Quinidine, Procainamide, Disopyramide, Amiodarone, Sotalol, Ibutilide, Haloperidol, Chlorpromazine, Methadone, Macrolides, Fluoroquinolones)",
                    "mechanism": "Tác dụng hiệp đồng kéo dài QT interval",
                    "effect": "Tăng nguy cơ torsades de pointes, rối loạn nhịp tim đe dọa tính mạng",
                    "management": "CHỐNG CHỈ ĐỊNH. KHÔNG được dùng đồng thời với dofetilide."
                }
            ],
            "moderate": [
                {
                    "drug": "Thuốc lợi tiểu (Furosemide, Thiazide)",
                    "mechanism": "Thuốc lợi tiểu gây hạ K+ và Mg2+, tăng nguy cơ torsades de pointes khi dùng với dofetilide",
                    "effect": "Tăng nguy cơ torsades de pointes",
                    "management": "Theo dõi K+ và Mg2+ chặt chẽ. Bổ sung K+ và Mg2+ nếu cần. Có thể cần giảm liều thuốc lợi tiểu hoặc ngừng tạm thời."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng dofetilide",
                "QT kéo dài (QTc >440ms) - CHỐNG CHỈ ĐỊNH",
                "Torsades de pointes - CHỐNG CHỈ ĐỊNH",
                "Suy thận nặng (CrCl <20) - CHỐNG CHỈ ĐỊNH",
                "Dùng với cimetidine, verapamil, ketoconazole, trimethoprim - CHỐNG CHỈ ĐỊNH",
                "Dùng với thuốc kéo dài QT - CHỐNG CHỈ ĐỊNH",
                "Hạ kali máu, hạ magie máu - CHỐNG CHỈ ĐỊNH (phải điều chỉnh trước)"
            ],
            "tương_đối": [
                "Suy thận (CrCl 20-40) - giảm liều 75%",
                "Bệnh nhân cao tuổi - tăng nhạy cảm, tăng nguy cơ tác dụng phụ",
                "Dùng với thuốc lợi tiểu - tăng nguy cơ hạ K+/Mg2+"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dofetilide là thuốc phân loại C. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Dofetilide có thể qua nhau thai. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt trong điều trị rối loạn nhịp đe dọa tính mạng.",
            "lactation": {
                "safety": "Unknown",
                "details": "Không biết dofetilide có bài tiết vào sữa mẹ hay không. Thời gian bán thải 10 giờ, protein binding 60-70%. Có thể bài tiết vào sữa mẹ ở nồng độ thấp.",
                "recommendation": "Thận trọng khi cho con bú. Nếu cần, ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Không cần điều chỉnh liều (thải trừ chủ yếu qua thận)",
            "notes": "Dofetilide thải trừ chủ yếu qua thận (80% bài tiết nguyên dạng). Không cần điều chỉnh liều ở bệnh nhân suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Torsades de pointes (rối loạn nhịp tim đe dọa tính mạng)",
                "Kéo dài QT interval nặng (QTc >500ms)",
                "Nhịp chậm nặng",
                "Ngất, rối loạn ý thức"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ. Magnesium có thể giúp điều trị torsades de pointes.",
            "treatment": [
                "Ngừng ngay dofetilide",
                "Theo dõi ECG liên tục",
                "Nếu torsades de pointes:",
                "  - Magnesium sulfate 1-2g IV bolus, sau đó 1-2g/giờ IV infusion",
                "  - Overdrive pacing nếu cần",
                "  - Isoproterenol IV nếu cần (tăng nhịp tim)",
                "Lọc máu (hemodialysis) - dofetilide có thể được loại bỏ một phần",
                "Theo dõi: ECG, QTc liên tục"
            ],
            "monitoring": "Theo dõi ECG, QTc liên tục cho đến khi hồi phục. Theo dõi lâu hơn nếu có biến chứng (torsades de pointes)."
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "agent": "Magnesium sulfate",
                    "mechanism": "Điều trị torsades de pointes",
                    "indication": "Torsades de pointes do dofetilide",
                    "dose": "1-2g IV bolus, sau đó 1-2g/giờ IV infusion",
                    "caution": "Điều trị hỗ trợ cho torsades de pointes."
                }
            ],
            "notes": "Magnesium điều trị torsades de pointes. Lọc máu có thể giúp loại bỏ dofetilide."
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với hoặc không thức ăn. Có thể uống không thức ăn nếu cần.",
                "timing": "Điều chỉnh liều theo CrCl: CrCl >60: 500mcg x 2 lần/ngày, CrCl 40-60: 250mcg x 2 lần/ngày, CrCl 20-40: 125mcg x 2 lần/ngày. Uống đều đặn, cách đều nhau trong ngày (q12h).",
                "notes": "QUAN TRỌNG: 1) PHẢI bắt đầu trong bệnh viện với monitoring ECG 3 ngày, 2) CHỈ được kê đơn bởi bác sĩ đã được đào tạo về dofetilide, 3) Điều chỉnh liều theo chức năng thận (CrCl) - QUAN TRỌNG, 4) CHỐNG CHỈ ĐỊNH nếu CrCl <20, 5) PHẢI đảm bảo K+ và Mg2+ bình thường trước khi dùng, 6) NGỪNG NGAY nếu QTc >500ms hoặc có torsades de pointes, 7) CHỐNG CHỈ ĐỊNH với cimetidine, verapamil, ketoconazole, trimethoprim."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Dofetilide (Tikosyn)",
                "ACC/AHA/ESC Guidelines for Atrial Fibrillation",
                "UpToDate - Dofetilide: Drug Information",
                "Medscape - Dofetilide Drug Reference"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, ACC/AHA/ESC guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },

    "Adenosine": {
        "group": "Cardiovascular - Antiarrhythmic (Class V - Purinergic Agonist)",
        "vietnamese_name": "Adenosine, Adenocard",
        "administration": ["IV"],
        "indications": [
            "Nhịp nhanh trên thất (SVT) - chuyển nhịp cấp tính",
            "Chẩn đoán rối loạn nhịp tim (unmasking underlying rhythm)",
            "Stress test (pharmacologic stress testing)"
        ],
        "contraindications": [
            "Dị ứng adenosine",
            "Block nhĩ thất độ 2-3 (trừ khi có máy tạo nhịp)",
            "Hội chứng sick sinus (trừ khi có máy tạo nhịp)",
            "Hen phế quản nặng",
            "COPD nặng",
            "Dùng với dipyridamole (tăng tác dụng adenosine)"
        ],
        "dosage": {
            "adult_svt_initial": "6mg IV bolus nhanh (trong 1-2 giây)",
            "adult_svt_repeat": "12mg IV bolus nhanh (nếu không đáp ứng sau 1-2 phút), có thể lặp lại 12mg thêm 1 lần",
            "adult_max": "12mg x 2 lần (tổng 30mg)",
            "adult_stress_test": "140 mcg/kg/phút IV infusion trong 6 phút",
            "notes": "Tiêm IV bolus NHANH (trong 1-2 giây) vào tĩnh mạch lớn (antecubital), sau đó rửa ngay bằng 10-20ml NS. Tác dụng rất ngắn (half-life <10 giây)."
        },
        "side_effects": [
            "Nhịp tim chậm thoáng qua (phổ biến, thường tự hết trong vài giây)",
            "Block nhĩ thất thoáng qua (phổ biến, thường tự hết)",
            "Khó thở, cảm giác nghẹt thở (phổ biến, thường tự hết)",
            "Đau ngực (phổ biến, thường tự hết)",
            "Đỏ mặt",
            "Chóng mặt",
            "Rối loạn nhịp tim (hiếm)",
            "Co thắt phế quản (ở bệnh nhân hen)"
        ],
        "interactions": [
            "Dipyridamole: tăng tác dụng adenosine (giảm liều adenosine 50-75%)",
            "Theophylline, Caffeine: giảm tác dụng adenosine (có thể cần tăng liều)",
            "Carbamazepine: tăng tác dụng adenosine",
            "Digoxin: tăng nguy cơ block nhĩ thất"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Adenosine là purine nucleoside, gắn với thụ thể A1 adenosine receptor trên tế bào nút nhĩ thất (AV node) và tế bào cơ tim. Kích hoạt thụ thể A1 → hoạt hóa kênh K+ (IKACh) → tăng dòng K+ ra ngoài → tăng phân cực màng tế bào → ức chế dẫn truyền qua nút nhĩ thất. Kết quả: (1) Block nhĩ thất thoáng qua (transient AV block), (2) Chuyển nhịp SVT về nhịp xoang (do ức chế reentry pathway qua AV node), (3) Unmasking underlying rhythm (chẩn đoán). ĐẶC ĐIỂM: (1) Tác dụng cực nhanh (khởi phát trong vài giây), (2) Thời gian tác dụng cực ngắn (half-life <10 giây, tác dụng kéo dài 10-20 giây), (3) Tiêm IV bolus NHANH (trong 1-2 giây) vào tĩnh mạch lớn, (4) Rửa ngay bằng NS sau khi tiêm, (5) Tác dụng phụ thoáng qua (thường tự hết trong vài giây), (6) An toàn và hiệu quả cao cho SVT.",
        "monitoring": [
            "ECG liên tục - QUAN TRỌNG, theo dõi chuyển nhịp, block AV",
            "Nhịp tim - nhịp tim chậm thoáng qua phổ biến",
            "Huyết áp - hạ huyết áp thoáng qua có thể xảy ra",
            "Dấu hiệu khó thở, co thắt phế quản (ở bệnh nhân hen)",
            "Dấu hiệu đau ngực (thường tự hết)"
        ],
        "precautions": [
            "Tiêm IV bolus NHANH (trong 1-2 giây) vào tĩnh mạch lớn (antecubital) - QUAN TRỌNG",
            "Rửa ngay bằng 10-20ml NS sau khi tiêm - QUAN TRỌNG (đảm bảo thuốc vào tim)",
            "CHỐNG CHỈ ĐỊNH nếu block AV độ 2-3 không có máy tạo nhịp",
            "CHỐNG CHỈ ĐỊNH nếu hội chứng sick sinus không có máy tạo nhịp",
            "Thận trọng ở bệnh nhân hen phế quản - có thể gây co thắt phế quản",
            "Thận trọng ở bệnh nhân COPD nặng - có thể gây co thắt phế quản",
            "Giảm liều 50-75% nếu dùng với dipyridamole (tăng tác dụng adenosine)",
            "Có thể cần tăng liều nếu dùng với theophylline, caffeine (giảm tác dụng adenosine)",
            "Tác dụng phụ thoáng qua - thường tự hết trong vài giây đến vài phút",
            "Theo dõi ECG liên tục - QUAN TRỌNG"
        ],
        "pharmacokinetics": {
            "half_life": "<10 giây (cực ngắn)",
            "onset": "Vài giây",
            "duration": "10-20 giây (cực ngắn)",
            "protein_binding": "Không đáng kể",
            "clearance": "Tế bào: chuyển hóa nhanh thành inosine và adenosine monophosphate (AMP) bởi adenosine deaminase. Thời gian bán thải cực ngắn."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh đông lạnh. Dung dịch: ổn định ở nhiệt độ phòng.",
        "black_box_warnings": "Có thể gây block nhĩ thất nặng, nhịp tim chậm nặng, và rối loạn nhịp tim. CHỐNG CHỈ ĐỊNH nếu block AV độ 2-3 hoặc hội chứng sick sinus không có máy tạo nhịp. Có thể gây co thắt phế quản ở bệnh nhân hen.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Dipyridamole",
                    "mechanism": "Dipyridamole ức chế adenosine deaminase và tái hấp thu adenosine, tăng nồng độ và tác dụng adenosine",
                    "effect": "Tăng tác dụng adenosine đáng kể, tăng nguy cơ block AV, nhịp tim chậm",
                    "management": "GIẢM LIỀU ADENOSINE 50-75% nếu dùng với dipyridamole. Hoặc ngừng dipyridamole 24 giờ trước khi dùng adenosine."
                },
                {
                    "drug": "Theophylline, Caffeine",
                    "mechanism": "Theophylline và caffeine đối kháng thụ thể adenosine, giảm tác dụng adenosine",
                    "effect": "Giảm tác dụng adenosine, có thể không chuyển nhịp SVT",
                    "management": "Có thể cần tăng liều adenosine hoặc dùng thuốc khác. Ngừng caffeine trước khi dùng adenosine nếu có thể."
                }
            ],
            "moderate": [
                {
                    "drug": "Carbamazepine",
                    "mechanism": "Carbamazepine có thể tăng tác dụng adenosine",
                    "effect": "Tăng nguy cơ block AV, nhịp tim chậm",
                    "management": "Thận trọng. Theo dõi ECG chặt chẽ."
                },
                {
                    "drug": "Digoxin",
                    "mechanism": "Digoxin và adenosine đều ức chế dẫn truyền AV",
                    "effect": "Tăng nguy cơ block nhĩ thất",
                    "management": "Thận trọng. Theo dõi ECG chặt chẽ."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng adenosine",
                "Block nhĩ thất độ 2-3 không có máy tạo nhịp - CHỐNG CHỈ ĐỊNH",
                "Hội chứng sick sinus không có máy tạo nhịp - CHỐNG CHỈ ĐỊNH",
                "Hen phế quản nặng - CHỐNG CHỈ ĐỊNH (có thể gây co thắt phế quản nặng)",
                "COPD nặng - CHỐNG CHỈ ĐỊNH (có thể gây co thắt phế quản nặng)"
            ],
            "tương_đối": [
                "Hen phế quản nhẹ - thận trọng, có thể gây co thắt phế quản",
                "COPD nhẹ - thận trọng",
                "Dùng với dipyridamole - giảm liều adenosine 50-75%",
                "Dùng với theophylline, caffeine - có thể cần tăng liều adenosine"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Adenosine là category C. Không có nghiên cứu đầy đủ ở phụ nữ có thai. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt trong SVT đe dọa tính mạng.",
            "lactation": {
                "safety": "Unknown",
                "details": "Không biết adenosine có bài tiết vào sữa mẹ hay không. Thời gian bán thải cực ngắn (<10 giây).",
                "recommendation": "Có thể dùng khi cho con bú do thời gian bán thải cực ngắn."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Không cần điều chỉnh liều (chuyển hóa nhanh, không phụ thuộc gan)",
            "notes": "Adenosine chuyển hóa nhanh bởi adenosine deaminase trong tế bào. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Block nhĩ thất nặng",
                "Nhịp tim chậm nặng",
                "Rối loạn nhịp tim",
                "Co thắt phế quản nặng (ở bệnh nhân hen)",
                "Hạ huyết áp nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ. Theophylline có thể đối kháng tác dụng adenosine.",
            "treatment": [
                "Ngừng adenosine ngay (nếu đang truyền)",
                "Theo dõi ECG liên tục",
                "Nếu block AV nặng hoặc nhịp tim chậm nặng:",
                "  - Atropine 0.5-1mg IV (có thể không hiệu quả do cơ chế khác)",
                "  - Máy tạo nhịp tạm thời nếu cần",
                "Nếu co thắt phế quản:",
                "  - Albuterol nebulizer",
                "  - Epinephrine IM nếu nặng",
                "  - Hỗ trợ hô hấp nếu cần",
                "Nếu hạ huyết áp nặng:",
                "  - Truyền dịch (NS, LR)",
                "  - Vasopressor (norepinephrine) nếu cần",
                "Theo dõi: ECG, huyết áp, nhịp tim, hô hấp liên tục",
                "Lưu ý: Half-life cực ngắn (<10 giây), tác dụng thường tự hết trong vài phút"
            ],
            "monitoring": "Theo dõi ECG, huyết áp, nhịp tim, hô hấp liên tục cho đến khi hồi phục. Theo dõi lâu hơn nếu có biến chứng (block AV, co thắt phế quản)."
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "agent": "Theophylline",
                    "mechanism": "Đối kháng thụ thể adenosine",
                    "indication": "Block AV nặng, nhịp tim chậm nặng do adenosine",
                    "dose": "100-200mg IV (nếu có)",
                    "caution": "Có thể đối kháng tác dụng adenosine."
                }
            ],
            "notes": "Theophylline có thể đối kháng tác dụng adenosine. Tuy nhiên, do half-life cực ngắn của adenosine (<10 giây), tác dụng thường tự hết trong vài phút."
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Dung dịch sẵn sàng sử dụng: 3mg/ml. Không cần pha loãng.",
                "infusion_rate": "Tiêm IV bolus NHANH (trong 1-2 giây) vào tĩnh mạch lớn (antecubital). Sau đó rửa ngay bằng 10-20ml NS.",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
                "incompatibility": [
                    "Không trộn với các thuốc khác. Dùng đường truyền riêng."
                ],
                "notes": "QUAN TRỌNG: 1) Tiêm IV bolus NHANH (trong 1-2 giây) vào tĩnh mạch lớn (antecubital), 2) Rửa ngay bằng 10-20ml NS sau khi tiêm, 3) Theo dõi ECG liên tục, 4) Liều: 6mg lần đầu, 12mg lần 2 (nếu không đáp ứng), 12mg lần 3 (nếu cần)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Adenosine (Adenocard)",
                "ACC/AHA/ESC Guidelines for Supraventricular Tachycardia",
                "UpToDate - Adenosine: Drug Information",
                "Medscape - Adenosine Drug Reference"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, ACC/AHA/ESC guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },

    "Quinidine": {
        "group": "Cardiovascular - Antiarrhythmic (Class IA)",
        "vietnamese_name": "Quinidine, Quinaglute, Cardioquin",
        "administration": ["PO", "IV"],
        "indications": [
            "Rung nhĩ (atrial fibrillation) - chuyển nhịp và duy trì nhịp xoang",
            "Cuồng nhĩ (atrial flutter) - chuyển nhịp và duy trì nhịp xoang",
            "Nhịp nhanh trên thất (SVT)",
            "Rối loạn nhịp thất (ventricular arrhythmias)",
            "Sốt rét (malaria) - ít dùng hiện nay"
        ],
        "contraindications": [
            "Dị ứng quinidine",
            "QT kéo dài (QTc >500ms) - CHỐNG CHỈ ĐỊNH",
            "Torsades de pointes - CHỐNG CHỈ ĐỊNH",
            "Block nhĩ thất độ 2-3 không có máy tạo nhịp - CHỐNG CHỈ ĐỊNH",
            "Suy tim nặng",
            "Bệnh gan nặng",
            "Hạ kali máu, hạ magie máu - CHỐNG CHỈ ĐỊNH (phải điều chỉnh trước)",
            "Myasthenia gravis - CHỐNG CHỈ ĐỊNH"
        ],
        "dosage": {
            "adult_po_immediate": "200-400mg PO mỗi 6 giờ",
            "adult_po_extended": "300-600mg PO mỗi 8-12 giờ (dạng extended release)",
            "adult_po_loading": "200-400mg PO mỗi 2 giờ x 3-5 lần (chuyển nhịp AF)",
            "adult_iv": "6-10mg/kg IV trong 30 phút, sau đó 0.5-1mg/kg/phút IV infusion",
            "adult_max": "3-4g/ngày (PO)",
            "notes": "Class IA antiarrhythmic. PHẢI đảm bảo K+ và Mg2+ bình thường trước khi dùng. Theo dõi QTc chặt chẽ. Nguy cơ torsades de pointes."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, có thể giảm liều",
            "under_30": "Giảm liều 25-50%, theo dõi chặt chẽ"
        },
        "side_effects": [
            "Torsades de pointes (nguy hiểm tính mạng) - nguy cơ cao",
            "Kéo dài QT interval (QTc >500ms nguy hiểm)",
            "Rối loạn nhịp tim (proarrhythmia)",
            "Block nhĩ thất",
            "Hạ huyết áp (đặc biệt IV)",
            "Rối loạn tiêu hóa (tiêu chảy, buồn nôn, nôn) - phổ biến",
            "Nhức đầu, chóng mặt",
            "Ù tai, mất thính giác (cinchonism)",
            "Thị lực mờ",
            "Giảm tiểu cầu (thrombocytopenia) - hiếm",
            "Ban da, sốt (hypersensitivity)"
        ],
        "interactions": [
            "Thuốc kéo dài QT: tăng nguy cơ torsades de pointes",
            "Digoxin: tăng nồng độ digoxin (giảm liều digoxin 50%)",
            "Warfarin: tăng tác dụng chống đông",
            "Amiodarone: tăng nguy cơ torsades de pointes",
            "Verapamil, Diltiazem: tăng nguy cơ block AV",
            "CYP3A4 inhibitors: tăng nồng độ quinidine"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Quinidine là class IA antiarrhythmic. Ức chế kênh Na+ voltage-gated (phase 0), làm chậm dẫn truyền và kéo dài repolarization (phase 3). Kéo dài QT interval và PR interval. Quinidine cũng có tác dụng chẹn alpha-adrenergic (gây hạ huyết áp) và chẹn muscarinic (gây nhịp tim nhanh phản ứng). Hiệu quả cho rối loạn nhịp thất và trên thất. ĐẶC ĐIỂM: (1) Nguy cơ torsades de pointes cao (do kéo dài QT), (2) PHẢI đảm bảo K+ và Mg2+ bình thường trước khi dùng, (3) Theo dõi QTc chặt chẽ, (4) Rối loạn tiêu hóa phổ biến (tiêu chảy), (5) Cinchonism (ù tai, mất thính giác) với liều cao, (6) Tăng nồng độ digoxin (giảm liều digoxin 50%), (7) Ít dùng hiện nay do tác dụng phụ và nguy cơ torsades de pointes.",
        "monitoring": [
            "ECG liên tục khi bắt đầu - theo dõi QTc, torsades de pointes",
            "QTc interval - MỤC TIÊU: <450ms, NGUY HIỂM: >500ms hoặc tăng >60ms",
            "Nhịp tim và huyết áp - theo dõi nhịp tim nhanh phản ứng, hạ huyết áp",
            "Điện giải (K+, Mg2+) - PHẢI bình thường trước khi dùng, theo dõi định kỳ",
            "Nồng độ quinidine trong máu (nếu có thể, therapeutic range: 2-5 mcg/ml)",
            "Nồng độ digoxin nếu dùng cùng (quinidine tăng nồng độ digoxin)",
            "INR nếu dùng với warfarin (quinidine tăng tác dụng warfarin)",
            "Công thức máu - hiếm giảm tiểu cầu",
            "Dấu hiệu cinchonism (ù tai, mất thính giác) - với liều cao",
            "Dấu hiệu torsades de pointes (ngất, rối loạn nhịp) - NGỪNG NGAY nếu có"
        ],
        "precautions": [
            "PHẢI đảm bảo K+ và Mg2+ bình thường trước khi dùng (giảm K+/Mg2+ tăng nguy cơ torsades)",
            "CHỐNG CHỈ ĐỊNH nếu QTc >500ms hoặc có tiền sử torsades de pointes",
            "Theo dõi QTc chặt chẽ - NGỪNG NGAY nếu QTc >500ms hoặc tăng >60ms",
            "NGỪNG NGAY nếu có torsades de pointes",
            "Rối loạn tiêu hóa phổ biến (tiêu chảy) - có thể cần giảm liều hoặc ngừng",
            "Giảm liều digoxin 50% khi dùng với quinidine (quinidine tăng nồng độ digoxin)",
            "Theo dõi INR nếu dùng với warfarin (quinidine tăng tác dụng warfarin)",
            "CHỐNG CHỈ ĐỊNH trong myasthenia gravis - có thể làm nặng bệnh",
            "CHỐNG CHỈ ĐỊNH trong block AV độ 2-3 không có máy tạo nhịp",
            "Thận trọng ở bệnh nhân suy tim nặng - có thể làm nặng",
            "Thận trọng ở bệnh nhân suy gan nặng - tăng nguy cơ tích lũy",
            "Tránh dùng với thuốc kéo dài QT khác",
            "Tránh dùng với thuốc lợi tiểu (tăng nguy cơ hạ K+/Mg2+)",
            "Ít dùng hiện nay do tác dụng phụ và nguy cơ torsades de pointes"
        ],
        "pharmacokinetics": {
            "half_life": "6-8 giờ",
            "onset": "1-3 giờ (PO), 5-10 phút (IV)",
            "duration": "6-8 giờ",
            "protein_binding": "80-90%",
            "clearance": "Gan: chuyển hóa qua CYP3A4, CYP2D6. Thận: bài tiết một phần nguyên dạng (20-50%)."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín.",
        "black_box_warnings": "Nguy cơ torsades de pointes (rối loạn nhịp tim đe dọa tính mạng), đặc biệt ở bệnh nhân có QT kéo dài, hạ K+/Mg2+, hoặc dùng với thuốc kéo dài QT khác. PHẢI đảm bảo K+ và Mg2+ bình thường trước khi dùng. Theo dõi QTc chặt chẽ. NGỪNG NGAY nếu QTc >500ms hoặc có torsades de pointes.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Thuốc kéo dài QT (Amiodarone, Sotalol, Dofetilide, Procainamide, Disopyramide, Haloperidol, Chlorpromazine, Methadone, Macrolides, Fluoroquinolones)",
                    "mechanism": "Tác dụng hiệp đồng kéo dài QT interval",
                    "effect": "Tăng nguy cơ torsades de pointes, rối loạn nhịp tim đe dọa tính mạng",
                    "management": "TRÁNH DÙNG CHUNG. Nếu bắt buộc: theo dõi ECG sát, đảm bảo K+ và Mg2+ bình thường, theo dõi QTc chặt chẽ."
                },
                {
                    "drug": "Digoxin",
                    "mechanism": "Quinidine ức chế P-glycoprotein, giảm thải trừ digoxin, tăng nồng độ digoxin",
                    "effect": "Tăng nồng độ digoxin 50-100%, tăng nguy cơ ngộ độc digoxin",
                    "management": "GIẢM LIỀU DIGOXIN 50% ngay khi bắt đầu quinidine. Theo dõi nồng độ digoxin chặt chẽ. Có thể cần giảm liều digoxin thêm."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Quinidine ức chế chuyển hóa warfarin (CYP2C9), tăng nồng độ warfarin",
                    "effect": "Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên khi bắt đầu quinidine. Có thể cần giảm liều warfarin."
                }
            ],
            "moderate": [
                {
                    "drug": "Amiodarone",
                    "mechanism": "Cả hai đều kéo dài QT và ức chế CYP3A4",
                    "effect": "Tăng nguy cơ torsades de pointes, tăng nồng độ quinidine",
                    "management": "TRÁNH DÙNG CHUNG. Nếu bắt buộc: theo dõi ECG sát, đảm bảo K+ và Mg2+ bình thường."
                },
                {
                    "drug": "Verapamil, Diltiazem",
                    "mechanism": "Cả hai đều làm chậm dẫn truyền AV",
                    "effect": "Tăng nguy cơ block nhĩ thất",
                    "management": "Thận trọng. Theo dõi ECG chặt chẽ. Có thể cần giảm liều một trong hai thuốc."
                },
                {
                    "drug": "CYP3A4 inhibitors (Ketoconazole, Clarithromycin, Erythromycin)",
                    "mechanism": "Ức chế chuyển hóa quinidine, tăng nồng độ quinidine",
                    "effect": "Tăng nồng độ quinidine, tăng tác dụng phụ",
                    "management": "Thận trọng. Theo dõi nồng độ quinidine. Có thể cần giảm liều quinidine."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng quinidine",
                "QT kéo dài (QTc >500ms) - CHỐNG CHỈ ĐỊNH",
                "Torsades de pointes - CHỐNG CHỈ ĐỊNH",
                "Block nhĩ thất độ 2-3 không có máy tạo nhịp - CHỐNG CHỈ ĐỊNH",
                "Suy tim nặng",
                "Bệnh gan nặng",
                "Hạ kali máu, hạ magie máu - CHỐNG CHỈ ĐỊNH (phải điều chỉnh trước)",
                "Myasthenia gravis - CHỐNG CHỈ ĐỊNH"
            ],
            "tương_đối": [
                "Suy tim (nhẹ đến trung bình) - thận trọng, có thể làm nặng",
                "Suy gan (nhẹ đến trung bình) - thận trọng, tăng nguy cơ tích lũy",
                "Suy thận nặng - giảm liều 25-50%",
                "Dùng với digoxin - giảm liều digoxin 50%",
                "Dùng với warfarin - theo dõi INR",
                "Dùng với thuốc kéo dài QT - tránh dùng chung"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Quinidine là category C. Không có nghiên cứu đầy đủ ở phụ nữ có thai. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt trong điều trị rối loạn nhịp đe dọa tính mạng.",
            "lactation": {
                "safety": "Compatible with Caution",
                "details": "Quinidine bài tiết vào sữa mẹ ở nồng độ thấp. Không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng. Theo dõi trẻ bú mẹ về dấu hiệu rối loạn nhịp tim hoặc rối loạn tiêu hóa."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Thận trọng, có thể cần giảm liều",
            "severe": "CHỐNG CHỈ ĐỊNH hoặc dùng rất thận trọng, giảm liều đáng kể",
            "notes": "Quinidine chuyển hóa ở gan qua CYP3A4, CYP2D6. Suy gan làm giảm chuyển hóa, tăng nồng độ và tác dụng phụ."
        },
        "overdose_management": {
            "symptoms": [
                "Torsades de pointes (rối loạn nhịp tim đe dọa tính mạng)",
                "Kéo dài QT interval nặng (QTc >500ms)",
                "Block nhĩ thất nặng",
                "Hạ huyết áp nặng",
                "Rối loạn tiêu hóa nặng (tiêu chảy, nôn)",
                "Cinchonism (ù tai, mất thính giác, thị lực mờ)",
                "Co giật (hiếm)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ. Magnesium có thể giúp điều trị torsades de pointes.",
            "treatment": [
                "Ngừng ngay quinidine",
                "Theo dõi ECG liên tục",
                "Nếu torsades de pointes:",
                "  - Magnesium sulfate 1-2g IV bolus, sau đó 1-2g/giờ IV infusion",
                "  - Overdrive pacing nếu cần",
                "  - Isoproterenol IV nếu cần (tăng nhịp tim)",
                "Nếu block AV nặng:",
                "  - Atropine 0.5-1mg IV",
                "  - Máy tạo nhịp tạm thời nếu cần",
                "Nếu hạ huyết áp nặng:",
                "  - Truyền dịch (NS, LR)",
                "  - Vasopressor (norepinephrine) nếu cần",
                "Điều trị rối loạn tiêu hóa:",
                "  - Bù dịch nếu tiêu chảy nặng",
                "  - Chống nôn nếu nôn nặng",
                "Lọc máu (hemodialysis) - ít hiệu quả (protein binding 80-90%)",
                "Theo dõi: ECG, huyết áp, nhịp tim, QTc liên tục"
            ],
            "monitoring": "Theo dõi ECG, huyết áp, nhịp tim, QTc liên tục cho đến khi hồi phục. Theo dõi lâu hơn nếu có biến chứng (torsades de pointes, block AV)."
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "agent": "Magnesium sulfate",
                    "mechanism": "Điều trị torsades de pointes",
                    "indication": "Torsades de pointes do quinidine",
                    "dose": "1-2g IV bolus, sau đó 1-2g/giờ IV infusion",
                    "caution": "Điều trị hỗ trợ cho torsades de pointes."
                }
            ],
            "notes": "Magnesium điều trị torsades de pointes. Lọc máu ít hiệu quả do protein binding cao."
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với thức ăn hoặc không. Uống với thức ăn có thể giảm rối loạn tiêu hóa.",
                "timing": "Dạng immediate release: 200-400mg PO mỗi 6 giờ. Dạng extended release: 300-600mg PO mỗi 8-12 giờ. Loading dose: 200-400mg PO mỗi 2 giờ x 3-5 lần (chuyển nhịp AF)."
            },
            "iv": {
                "reconstitution": "Pha trong NS hoặc D5W. Nồng độ: 16mg/ml.",
                "infusion_rate": "Loading: 6-10mg/kg IV trong 30 phút. Maintenance: 0.5-1mg/kg/phút IV infusion. Theo dõi ECG và huyết áp liên tục.",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
                "incompatibility": [
                    "Không trộn với các thuốc khác. Dùng đường truyền riêng."
                ],
                "notes": "QUAN TRỌNG: 1) PHẢI đảm bảo K+ và Mg2+ bình thường trước khi dùng, 2) Theo dõi ECG và QTc chặt chẽ, 3) NGỪNG NGAY nếu QTc >500ms hoặc có torsades de pointes, 4) Theo dõi huyết áp (hạ huyết áp phổ biến với IV)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Quinidine (Quinaglute, Cardioquin)",
                "ACC/AHA/ESC Guidelines for Atrial Fibrillation",
                "UpToDate - Quinidine: Drug Information",
                "Medscape - Quinidine Drug Reference"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, ACC/AHA/ESC guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },

    "Ibutilide": {
        "group": "Cardiovascular - Antiarrhythmic (Class III)",
        "vietnamese_name": "Ibutilide, Corvert",
        "administration": ["IV"],
        "indications": [
            "Rung nhĩ (atrial fibrillation) - chuyển nhịp cấp tính",
            "Cuồng nhĩ (atrial flutter) - chuyển nhịp cấp tính"
        ],
        "contraindications": [
            "Dị ứng ibutilide",
            "QT kéo dài (QTc >440ms) - CHỐNG CHỈ ĐỊNH",
            "Torsades de pointes - CHỐNG CHỈ ĐỊNH",
            "Hạ kali máu, hạ magie máu - CHỐNG CHỈ ĐỊNH (phải điều chỉnh trước)",
            "Dùng với thuốc kéo dài QT - CHỐNG CHỈ ĐỊNH"
        ],
        "dosage": {
            "adult_iv_weight_>60kg": "1mg IV trong 10 phút",
            "adult_iv_weight_<60kg": "0.01mg/kg IV trong 10 phút",
            "adult_iv_repeat": "Có thể lặp lại 1 lần sau 10 phút nếu không chuyển nhịp",
            "adult_max": "2mg (tổng)",
            "notes": "PHẢI bắt đầu trong bệnh viện với monitoring ECG 4 giờ (nguy cơ torsades de pointes). PHẢI đảm bảo K+ và Mg2+ bình thường trước khi dùng. Chỉ dùng IV, không có dạng PO."
        },
        "side_effects": [
            "Torsades de pointes (nguy hiểm tính mạng) - nguy cơ cao (3-5%)",
            "Kéo dài QT interval (QTc >500ms nguy hiểm)",
            "Rối loạn nhịp tim (proarrhythmia)",
            "Nhịp tim chậm",
            "Hạ huyết áp",
            "Đau đầu",
            "Buồn nôn"
        ],
        "interactions": [
            "Thuốc kéo dài QT: tăng nguy cơ torsades de pointes (CHỐNG CHỈ ĐỊNH)",
            "Digoxin: tăng nguy cơ rối loạn nhịp tim",
            "Beta-blockers: tăng nguy cơ nhịp tim chậm"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Ibutilide là class III antiarrhythmic. Ức chế kênh K+ (delayed rectifier IKr), kéo dài phase 3 của action potential, kéo dài QT interval và effective refractory period (ERP). Kết quả: chuyển nhịp rung nhĩ/cuồng nhĩ về nhịp xoang. ĐẶC ĐIỂM: (1) PHẢI bắt đầu trong bệnh viện với monitoring ECG 4 giờ (nguy cơ torsades de pointes cao), (2) Chỉ dùng IV, không có dạng PO, (3) PHẢI đảm bảo K+ và Mg2+ bình thường trước khi dùng, (4) Nguy cơ torsades de pointes cao (3-5%), (5) Hiệu quả cao cho chuyển nhịp AF/AFL cấp tính (60-70%).",
        "monitoring": [
            "ECG liên tục trong 4 giờ sau khi tiêm (BẮT BUỘC) - theo dõi QTc, torsades de pointes",
            "QTc interval - MỤC TIÊU: <440ms, NGUY HIỂM: >500ms hoặc tăng >60ms",
            "Nhịp tim và huyết áp",
            "Điện giải (K+, Mg2+) - PHẢI bình thường trước khi dùng",
            "Dấu hiệu torsades de pointes (ngất, rối loạn nhịp) - NGỪNG NGAY nếu có"
        ],
        "precautions": [
            "PHẢI bắt đầu trong bệnh viện với monitoring ECG 4 giờ (nguy cơ torsades de pointes cao)",
            "CHỐNG CHỈ ĐỊNH nếu QTc >440ms hoặc có tiền sử torsades de pointes",
            "PHẢI đảm bảo K+ và Mg2+ bình thường trước khi dùng (giảm K+/Mg2+ tăng nguy cơ torsades)",
            "CHỐNG CHỈ ĐỊNH với thuốc kéo dài QT khác",
            "NGỪNG NGAY nếu QTc >500ms hoặc có torsades de pointes",
            "Chỉ dùng IV, không có dạng PO",
            "Hiệu quả cao cho chuyển nhịp AF/AFL cấp tính (60-70%)"
        ],
        "pharmacokinetics": {
            "half_life": "6 giờ",
            "onset": "Vài phút (IV)",
            "duration": "Ngắn (do half-life ngắn)",
            "protein_binding": "40%",
            "clearance": "Gan (chuyển hóa), thận (bài tiết một phần)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh đông lạnh. Dung dịch: ổn định.",
        "black_box_warnings": "Nguy cơ torsades de pointes (rối loạn nhịp tim đe dọa tính mạng), nguy cơ cao (3-5%). PHẢI bắt đầu trong bệnh viện với monitoring ECG 4 giờ. CHỐNG CHỈ ĐỊNH nếu QTc >440ms, có tiền sử torsades de pointes, hoặc dùng với thuốc kéo dài QT. PHẢI đảm bảo K+ và Mg2+ bình thường trước khi dùng.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Thuốc kéo dài QT (Quinidine, Procainamide, Disopyramide, Amiodarone, Sotalol, Dofetilide, Haloperidol, Chlorpromazine, Methadone, Macrolides, Fluoroquinolones)",
                    "mechanism": "Tác dụng hiệp đồng kéo dài QT interval",
                    "effect": "Tăng nguy cơ torsades de pointes, rối loạn nhịp tim đe dọa tính mạng",
                    "management": "CHỐNG CHỈ ĐỊNH. KHÔNG được dùng đồng thời với ibutilide."
                }
            ],
            "moderate": [
                {
                    "drug": "Digoxin",
                    "mechanism": "Cả hai đều có thể gây rối loạn nhịp tim",
                    "effect": "Tăng nguy cơ rối loạn nhịp tim",
                    "management": "Thận trọng. Theo dõi ECG chặt chẽ."
                },
                {
                    "drug": "Beta-blockers",
                    "mechanism": "Cả hai đều làm chậm nhịp tim",
                    "effect": "Tăng nguy cơ nhịp tim chậm",
                    "management": "Thận trọng. Theo dõi ECG chặt chẽ."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng ibutilide",
                "QT kéo dài (QTc >440ms) - CHỐNG CHỈ ĐỊNH",
                "Torsades de pointes - CHỐNG CHỈ ĐỊNH",
                "Hạ kali máu, hạ magie máu - CHỐNG CHỈ ĐỊNH (phải điều chỉnh trước)",
                "Dùng với thuốc kéo dài QT - CHỐNG CHỈ ĐỊNH"
            ],
            "tương_đối": [
                "Suy tim nặng - thận trọng",
                "Dùng với digoxin - tăng nguy cơ rối loạn nhịp tim",
                "Dùng với beta-blockers - tăng nguy cơ nhịp tim chậm"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Ibutilide là category C. Không có nghiên cứu đầy đủ ở phụ nữ có thai. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt trong chuyển nhịp AF/AFL đe dọa tính mạng.",
            "lactation": {
                "safety": "Unknown",
                "details": "Không biết ibutilide có bài tiết vào sữa mẹ hay không. Thời gian bán thải 6 giờ.",
                "recommendation": "Thận trọng khi cho con bú. Nếu cần, ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Thận trọng",
            "severe": "Thận trọng, có thể cần giảm liều",
            "notes": "Ibutilide chuyển hóa ở gan. Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và tác dụng phụ."
        },
        "overdose_management": {
            "symptoms": [
                "Torsades de pointes (rối loạn nhịp tim đe dọa tính mạng)",
                "Kéo dài QT interval nặng (QTc >500ms)",
                "Nhịp tim chậm nặng",
                "Hạ huyết áp nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ. Magnesium có thể giúp điều trị torsades de pointes.",
            "treatment": [
                "Ngừng ngay ibutilide nếu đang truyền",
                "Theo dõi ECG liên tục",
                "Nếu torsades de pointes:",
                "  - Magnesium sulfate 1-2g IV bolus, sau đó 1-2g/giờ IV infusion",
                "  - Overdrive pacing nếu cần",
                "  - Isoproterenol IV nếu cần (tăng nhịp tim)",
                "Nếu nhịp tim chậm nặng:",
                "  - Atropine 0.5-1mg IV",
                "  - Máy tạo nhịp tạm thời nếu cần",
                "Nếu hạ huyết áp nặng:",
                "  - Truyền dịch (NS, LR)",
                "  - Vasopressor (norepinephrine) nếu cần",
                "Theo dõi: ECG, huyết áp, nhịp tim, QTc liên tục"
            ],
            "monitoring": "Theo dõi ECG, huyết áp, nhịp tim, QTc liên tục cho đến khi hồi phục. Theo dõi lâu hơn nếu có biến chứng (torsades de pointes)."
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "agent": "Magnesium sulfate",
                    "mechanism": "Điều trị torsades de pointes",
                    "indication": "Torsades de pointes do ibutilide",
                    "dose": "1-2g IV bolus, sau đó 1-2g/giờ IV infusion",
                    "caution": "Điều trị hỗ trợ cho torsades de pointes."
                }
            ],
            "notes": "Magnesium điều trị torsades de pointes."
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Dung dịch sẵn sàng sử dụng: 0.1mg/ml. Không cần pha loãng.",
                "infusion_rate": "Truyền IV trong 10 phút. Cân nặng >60kg: 1mg. Cân nặng <60kg: 0.01mg/kg. Có thể lặp lại 1 lần sau 10 phút nếu không chuyển nhịp.",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
                "incompatibility": [
                    "Không trộn với các thuốc khác. Dùng đường truyền riêng."
                ],
                "notes": "QUAN TRỌNG: 1) PHẢI bắt đầu trong bệnh viện với monitoring ECG 4 giờ, 2) PHẢI đảm bảo K+ và Mg2+ bình thường trước khi dùng, 3) Theo dõi QTc chặt chẽ, 4) NGỪNG NGAY nếu QTc >500ms hoặc có torsades de pointes."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Ibutilide (Corvert)",
                "ACC/AHA/ESC Guidelines for Atrial Fibrillation",
                "UpToDate - Ibutilide: Drug Information",
                "Medscape - Ibutilide Drug Reference"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, ACC/AHA/ESC guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },

    "Disopyramide": {
        "group": "Cardiovascular - Antiarrhythmic (Class IA)",
        "vietnamese_name": "Disopyramide, Norpace",
        "administration": ["PO"],
        "indications": [
            "Rung nhĩ (atrial fibrillation) - duy trì nhịp xoang",
            "Cuồng nhĩ (atrial flutter) - duy trì nhịp xoang",
            "Nhịp nhanh trên thất (SVT)",
            "Rối loạn nhịp thất (ventricular arrhythmias)"
        ],
        "contraindications": [
            "Dị ứng disopyramide",
            "QT kéo dài (QTc >500ms) - CHỐNG CHỈ ĐỊNH",
            "Torsades de pointes - CHỐNG CHỈ ĐỊNH",
            "Block nhĩ thất độ 2-3 không có máy tạo nhịp - CHỐNG CHỈ ĐỊNH",
            "Suy tim nặng - CHỐNG CHỈ ĐỊNH",
            "Hạ kali máu, hạ magie máu - CHỐNG CHỈ ĐỊNH (phải điều chỉnh trước)",
            "Myasthenia gravis - CHỐNG CHỈ ĐỊNH",
            "Glaucoma góc đóng - CHỐNG CHỈ ĐỊNH"
        ],
        "dosage": {
            "adult_po_immediate": "150-200mg PO mỗi 6 giờ",
            "adult_po_extended": "200-300mg PO mỗi 12 giờ (dạng extended release)",
            "adult_po_loading": "300mg PO, sau đó 150-200mg mỗi 6 giờ",
            "adult_max": "800mg/ngày",
            "notes": "Class IA antiarrhythmic. PHẢI đảm bảo K+ và Mg2+ bình thường trước khi dùng. Theo dõi QTc chặt chẽ. Nguy cơ torsades de pointes. Có tác dụng chống muscarinic (khô miệng, táo bón, bí tiểu)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "under_30": "Giảm liều 50-75%, theo dõi chặt chẽ"
        },
        "side_effects": [
            "Torsades de pointes (nguy hiểm tính mạng) - nguy cơ cao",
            "Kéo dài QT interval (QTc >500ms nguy hiểm)",
            "Rối loạn nhịp tim (proarrhythmia)",
            "Block nhĩ thất",
            "Suy tim (do tác dụng ức chế co bóp cơ tim - negative inotropy)",
            "Hạ huyết áp",
            "Khô miệng (do chống muscarinic)",
            "Táo bón (do chống muscarinic)",
            "Bí tiểu (do chống muscarinic)",
            "Nhìn mờ (do chống muscarinic)",
            "Glaucoma góc đóng (do chống muscarinic)"
        ],
        "interactions": [
            "Thuốc kéo dài QT: tăng nguy cơ torsades de pointes",
            "Digoxin: tăng nồng độ digoxin",
            "Warfarin: tăng tác dụng chống đông",
            "Beta-blockers: tăng nguy cơ suy tim (cả hai đều ức chế co bóp cơ tim)"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Disopyramide là class IA antiarrhythmic. Ức chế kênh Na+ voltage-gated (phase 0), làm chậm dẫn truyền và kéo dài repolarization (phase 3). Kéo dài QT interval và PR interval. Disopyramide cũng có tác dụng chống muscarinic (anticholinergic) mạnh → khô miệng, táo bón, bí tiểu, nhìn mờ, và có thể gây glaucoma góc đóng. Disopyramide cũng có tác dụng ức chế co bóp cơ tim (negative inotropy) → có thể làm nặng suy tim. Hiệu quả cho rối loạn nhịp thất và trên thất. ĐẶC ĐIỂM: (1) Nguy cơ torsades de pointes cao (do kéo dài QT), (2) PHẢI đảm bảo K+ và Mg2+ bình thường trước khi dùng, (3) Theo dõi QTc chặt chẽ, (4) Tác dụng chống muscarinic mạnh (khô miệng, táo bón, bí tiểu), (5) CHỐNG CHỈ ĐỊNH trong suy tim nặng (do negative inotropy), (6) CHỐNG CHỈ ĐỊNH trong glaucoma góc đóng (do chống muscarinic), (7) Ít dùng hiện nay do tác dụng phụ.",
        "monitoring": [
            "ECG liên tục khi bắt đầu - theo dõi QTc, torsades de pointes",
            "QTc interval - MỤC TIÊU: <450ms, NGUY HIỂM: >500ms hoặc tăng >60ms",
            "Nhịp tim và huyết áp - theo dõi nhịp tim chậm, hạ huyết áp",
            "Điện giải (K+, Mg2+) - PHẢI bình thường trước khi dùng, theo dõi định kỳ",
            "Chức năng tim (siêu âm tim nếu có triệu chứng suy tim) - disopyramide có thể làm nặng suy tim",
            "Nồng độ disopyramide trong máu (nếu có thể, therapeutic range: 2-5 mcg/ml)",
            "Nồng độ digoxin nếu dùng cùng (disopyramide tăng nồng độ digoxin)",
            "Dấu hiệu chống muscarinic (khô miệng, táo bón, bí tiểu, nhìn mờ)",
            "Dấu hiệu glaucoma góc đóng (đau mắt, nhìn mờ, đỏ mắt)",
            "Dấu hiệu torsades de pointes (ngất, rối loạn nhịp) - NGỪNG NGAY nếu có"
        ],
        "precautions": [
            "PHẢI đảm bảo K+ và Mg2+ bình thường trước khi dùng (giảm K+/Mg2+ tăng nguy cơ torsades)",
            "CHỐNG CHỈ ĐỊNH nếu QTc >500ms hoặc có tiền sử torsades de pointes",
            "Theo dõi QTc chặt chẽ - NGỪNG NGAY nếu QTc >500ms hoặc tăng >60ms",
            "NGỪNG NGAY nếu có torsades de pointes",
            "CHỐNG CHỈ ĐỊNH trong suy tim nặng - disopyramide có thể làm nặng suy tim (negative inotropy)",
            "CHỐNG CHỈ ĐỊNH trong glaucoma góc đóng - disopyramide có thể gây glaucoma góc đóng (chống muscarinic)",
            "Tác dụng chống muscarinic mạnh - khô miệng, táo bón, bí tiểu, nhìn mờ phổ biến",
            "Giảm liều digoxin 50% khi dùng với disopyramide (disopyramide tăng nồng độ digoxin)",
            "Theo dõi INR nếu dùng với warfarin (disopyramide tăng tác dụng warfarin)",
            "Tránh dùng với thuốc kéo dài QT khác",
            "Tránh dùng với thuốc lợi tiểu (tăng nguy cơ hạ K+/Mg2+)",
            "Điều chỉnh liều theo chức năng thận - QUAN TRỌNG",
            "Ít dùng hiện nay do tác dụng phụ và nguy cơ torsades de pointes"
        ],
        "pharmacokinetics": {
            "half_life": "4-10 giờ",
            "onset": "30-60 phút (PO)",
            "duration": "6-8 giờ",
            "protein_binding": "50-65%",
            "clearance": "Gan: chuyển hóa một phần. Thận: bài tiết chủ yếu nguyên dạng (50-60%). Cần điều chỉnh liều ở suy thận."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén/nang: bảo quản trong bao bì kín.",
        "black_box_warnings": "Nguy cơ torsades de pointes (rối loạn nhịp tim đe dọa tính mạng), đặc biệt ở bệnh nhân có QT kéo dài, hạ K+/Mg2+, hoặc dùng với thuốc kéo dài QT khác. PHẢI đảm bảo K+ và Mg2+ bình thường trước khi dùng. Theo dõi QTc chặt chẽ. NGỪNG NGAY nếu QTc >500ms hoặc có torsades de pointes. CHỐNG CHỈ ĐỊNH trong suy tim nặng và glaucoma góc đóng.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Thuốc kéo dài QT (Quinidine, Procainamide, Amiodarone, Sotalol, Dofetilide, Haloperidol, Chlorpromazine, Methadone, Macrolides, Fluoroquinolones)",
                    "mechanism": "Tác dụng hiệp đồng kéo dài QT interval",
                    "effect": "Tăng nguy cơ torsades de pointes, rối loạn nhịp tim đe dọa tính mạng",
                    "management": "TRÁNH DÙNG CHUNG. Nếu bắt buộc: theo dõi ECG sát, đảm bảo K+ và Mg2+ bình thường, theo dõi QTc chặt chẽ."
                },
                {
                    "drug": "Digoxin",
                    "mechanism": "Disopyramide ức chế P-glycoprotein, giảm thải trừ digoxin, tăng nồng độ digoxin",
                    "effect": "Tăng nồng độ digoxin, tăng nguy cơ ngộ độc digoxin",
                    "management": "GIẢM LIỀU DIGOXIN 50% ngay khi bắt đầu disopyramide. Theo dõi nồng độ digoxin chặt chẽ."
                },
                {
                    "drug": "Beta-blockers",
                    "mechanism": "Cả hai đều ức chế co bóp cơ tim (negative inotropy)",
                    "effect": "Tăng nguy cơ suy tim, hạ huyết áp",
                    "management": "TRÁNH DÙNG CHUNG. Nếu bắt buộc: theo dõi chức năng tim chặt chẽ."
                }
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Disopyramide có thể tăng tác dụng warfarin",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên. Có thể cần giảm liều warfarin."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng disopyramide",
                "QT kéo dài (QTc >500ms) - CHỐNG CHỈ ĐỊNH",
                "Torsades de pointes - CHỐNG CHỈ ĐỊNH",
                "Block nhĩ thất độ 2-3 không có máy tạo nhịp - CHỐNG CHỈ ĐỊNH",
                "Suy tim nặng - CHỐNG CHỈ ĐỊNH (do negative inotropy)",
                "Hạ kali máu, hạ magie máu - CHỐNG CHỈ ĐỊNH (phải điều chỉnh trước)",
                "Myasthenia gravis - CHỐNG CHỈ ĐỊNH (do chống muscarinic)",
                "Glaucoma góc đóng - CHỐNG CHỈ ĐỊNH (do chống muscarinic)"
            ],
            "tương_đối": [
                "Suy tim (nhẹ đến trung bình) - thận trọng, có thể làm nặng",
                "Suy thận nặng - giảm liều 50-75%",
                "Dùng với digoxin - giảm liều digoxin 50%",
                "Dùng với beta-blockers - tránh dùng chung",
                "Dùng với thuốc kéo dài QT - tránh dùng chung"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Disopyramide là category C. Không có nghiên cứu đầy đủ ở phụ nữ có thai. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt trong điều trị rối loạn nhịp đe dọa tính mạng.",
            "lactation": {
                "safety": "Compatible with Caution",
                "details": "Disopyramide bài tiết vào sữa mẹ ở nồng độ thấp. Không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng. Theo dõi trẻ bú mẹ về dấu hiệu chống muscarinic (khô miệng, táo bón)."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Thận trọng, có thể cần giảm liều",
            "severe": "Thận trọng, giảm liều",
            "notes": "Disopyramide chuyển hóa một phần ở gan. Suy gan có thể ảnh hưởng đến chuyển hóa, nhưng thải trừ chủ yếu qua thận."
        },
        "overdose_management": {
            "symptoms": [
                "Torsades de pointes (rối loạn nhịp tim đe dọa tính mạng)",
                "Kéo dài QT interval nặng (QTc >500ms)",
                "Block nhĩ thất nặng",
                "Suy tim cấp (do negative inotropy)",
                "Hạ huyết áp nặng",
                "Tác dụng chống muscarinic nặng (khô miệng, táo bón, bí tiểu, nhìn mờ)",
                "Glaucoma góc đóng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ. Magnesium có thể giúp điều trị torsades de pointes.",
            "treatment": [
                "Ngừng ngay disopyramide",
                "Theo dõi ECG liên tục",
                "Nếu torsades de pointes:",
                "  - Magnesium sulfate 1-2g IV bolus, sau đó 1-2g/giờ IV infusion",
                "  - Overdrive pacing nếu cần",
                "  - Isoproterenol IV nếu cần (tăng nhịp tim)",
                "Nếu block AV nặng:",
                "  - Atropine 0.5-1mg IV",
                "  - Máy tạo nhịp tạm thời nếu cần",
                "Nếu suy tim cấp:",
                "  - Inotrope (dobutamine, milrinone)",
                "  - Hỗ trợ hô hấp",
                "Nếu hạ huyết áp nặng:",
                "  - Truyền dịch (NS, LR)",
                "  - Vasopressor (norepinephrine) nếu cần",
                "Nếu glaucoma góc đóng:",
                "  - Pilocarpine mắt",
                "  - Tư vấn bác sĩ mắt ngay",
                "Lọc máu (hemodialysis) - có thể hiệu quả (protein binding 50-65%)",
                "Theo dõi: ECG, huyết áp, nhịp tim, QTc liên tục"
            ],
            "monitoring": "Theo dõi ECG, huyết áp, nhịp tim, QTc liên tục cho đến khi hồi phục. Theo dõi lâu hơn nếu có biến chứng (torsades de pointes, block AV, suy tim)."
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "agent": "Magnesium sulfate",
                    "mechanism": "Điều trị torsades de pointes",
                    "indication": "Torsades de pointes do disopyramide",
                    "dose": "1-2g IV bolus, sau đó 1-2g/giờ IV infusion",
                    "caution": "Điều trị hỗ trợ cho torsades de pointes."
                }
            ],
            "notes": "Magnesium điều trị torsades de pointes. Lọc máu có thể giúp loại bỏ disopyramide."
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với thức ăn hoặc không. Uống với thức ăn có thể giảm rối loạn tiêu hóa.",
                "timing": "Dạng immediate release: 150-200mg PO mỗi 6 giờ. Dạng extended release: 200-300mg PO mỗi 12 giờ. Loading dose: 300mg PO, sau đó 150-200mg mỗi 6 giờ."
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
                "FDA Drug Label - Disopyramide (Norpace)",
                "ACC/AHA/ESC Guidelines for Atrial Fibrillation",
                "UpToDate - Disopyramide: Drug Information",
                "Medscape - Disopyramide Drug Reference"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, ACC/AHA/ESC guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    }
}

__all__ = ['ANTIARRHYTHMICS']
