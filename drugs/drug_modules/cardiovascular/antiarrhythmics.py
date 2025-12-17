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
    }

}

__all__ = ['ANTIARRHYTHMICS']
