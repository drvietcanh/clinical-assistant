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

}

__all__ = ['ANTIARRHYTHMICS']
