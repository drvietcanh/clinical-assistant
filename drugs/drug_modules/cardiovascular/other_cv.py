"""
Other Cardiovascular Drugs
"""

OTHER_CV_DRUGS = {
      "Digoxin": {
        "group": "Cardiovascular - Cardiac Glycoside",
        "vietnamese_name": "Digoxin, Lanoxin",
        "administration": ["PO", "IV"],
        "indications": [
            "Suy tim với rung nhĩ",
            "Rung nhĩ kiểm soát tần số",
            "Suy tim không rung nhĩ (ít dùng)"
        ],
        "contraindications": [
            "Block nhĩ thất độ 2-3",
            "Nhịp tim chậm nặng",
            "Hội chứng Wolff-Parkinson-White",
            "Ngộ độc digoxin"
        ],
        "dosage": {
            "adult_po_loading": "0.5-1mg chia 2-3 lần/ngày x 1 ngày",
            "adult_po_maintenance": "0.125-0.25mg x 1 lần/ngày",
            "adult_iv": "0.25-0.5mg IV x 1 lần",
            "elderly": "Liều thấp hơn (0.0625-0.125mg/ngày)",
            "notes": "Theo dõi nồng độ digoxin (mục tiêu 0.8-2 ng/mL)"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "under_30": "Giảm liều 50-75%",
            "hemodialysis": "Bổ sung sau lọc máu"
        },
        "side_effects": [
            "Ngộ độc digoxin (buồn nôn, rối loạn nhịp, rối loạn thị giác)",
            "Nhịp tim chậm",
            "Block nhĩ thất",
            "Rối loạn nhịp (ngoại tâm thu, nhịp nhanh thất)"
        ],
        "interactions": [
            "Amiodarone: tăng nồng độ digoxin (giảm liều 50%)",
            "Furosemide: tăng nguy cơ ngộ độc (hạ kali)",
            "Verapamil: tăng nồng độ digoxin",
            "Quinine: tăng nồng độ digoxin"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Ức chế Na+/K+-ATPase ở màng tế bào cơ tim, tăng nồng độ Na+ nội bào, kích thích Na+/Ca2+ exchanger, tăng Ca2+ nội bào → tăng lực co bóp cơ tim (inotropy dương). Ở nút AV: tăng trương lực phế vị, giảm dẫn truyền AV (làm chậm tần số thất trong AF)",
        "monitoring": [
            "Nồng độ digoxin trong máu (BẮT BUỘC): Mục tiêu 0.8-2 ng/mL (1.0-2.6 nmol/L)",
            "Đo nồng độ ít nhất 6-8 giờ sau liều (sau khi phân bố)",
            "Điện giải: K+, Mg2+ (quan trọng - hạ K+, hạ Mg2+ → tăng nguy cơ ngộ độc)",
            "Creatinine, eGFR (digoxin thải qua thận)",
            "ECG: nhịp tim, block AV, rối loạn nhịp",
            "Triệu chứng ngộ độc: buồn nôn, nôn, rối loạn thị giác (nhìn vàng xanh), rối loạn nhịp"
        ],
        "precautions": [
            "LUÔN theo dõi nồng độ trong máu (therapeutic window hẹp)",
            "Hạ K+ và hạ Mg2+ làm tăng nguy cơ ngộ độc mạnh → phải bù điện giải trước",
            "Giảm liều ở suy thận (half-life tăng từ 36h lên 4-6 ngày)",
            "Ở người già: dùng liều thấp hơn (0.0625-0.125mg/ngày)",
            "Tránh loading dose nhanh ở suy thận (nguy cơ ngộ độc)",
            "Nhiều thuốc tương tác làm tăng nồng độ: amiodarone, verapamil, diltiazem, quinidine, macrolides, cyclosporine",
            "Ngộ độc digoxin có thể đe dọa tính mạng → cần điều trị ngay (Digibind/digoxin immune fab)"
        ],
        "pharmacokinetics": {
            "half_life": "36-48 giờ (bình thường), 4-6 ngày (suy thận)",
            "onset": "1-2 giờ (PO), 5-30 phút (IV)",
            "duration": "3-4 ngày (vì half-life dài)",
            "protein_binding": "20-25%",
            "clearance": "Thận (75-80%), không chuyển hóa"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: ổn định",
        "black_box_warnings": "Không dùng trong WPW với AF (có thể gây nhịp nhanh thất nguy hiểm). Ngộ độc digoxin có thể gây rối loạn nhịp đe dọa tính mạng và tử vong",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Amiodarone",
                    "mechanism": "Amiodarone ức chế P-glycoprotein và giảm thải trừ digoxin, tăng nồng độ digoxin",
                    "effect": "Tăng nồng độ digoxin 50-100%, tăng nguy cơ ngộ độc digoxin (rối loạn nhịp, block AV, buồn nôn)",
                    "management": "GIẢM LIỀU DIGOXIN 50% ngay khi bắt đầu amiodarone. Theo dõi nồng độ digoxin chặt chẽ. Có thể cần giảm liều digoxin thêm."
                },
                {
                    "drug": "Verapamil, Diltiazem",
                    "mechanism": "Verapamil/diltiazem ức chế P-glycoprotein, giảm thải trừ digoxin",
                    "effect": "Tăng nồng độ digoxin 50-70%, tăng nguy cơ ngộ độc",
                    "management": "Giảm liều digoxin 25-50%. Theo dõi nồng độ digoxin. Theo dõi ECG."
                },
                {
                    "drug": "Quinidine, Quinine",
                    "mechanism": "Quinidine/quinine ức chế P-glycoprotein, giảm thải trừ digoxin",
                    "effect": "Tăng nồng độ digoxin 50-100%, tăng nguy cơ ngộ độc",
                    "management": "Giảm liều digoxin 50%. Theo dõi nồng độ digoxin chặt chẽ."
                },
                {
                    "drug": "Macrolides (clarithromycin, erythromycin)",
                    "mechanism": "Macrolides ức chế P-glycoprotein và có thể giảm chuyển hóa digoxin bởi vi khuẩn ruột",
                    "effect": "Tăng nồng độ digoxin, tăng nguy cơ ngộ độc",
                    "management": "Thận trọng. Theo dõi nồng độ digoxin. Có thể cần giảm liều digoxin."
                },
                {
                    "drug": "Diuretics (furosemide, hydrochlorothiazide)",
                    "mechanism": "Diuretics gây hạ kali máu, tăng độc tính digoxin",
                    "effect": "Tăng nguy cơ ngộ độc digoxin mạnh (rối loạn nhịp, block AV) ngay cả khi nồng độ digoxin bình thường",
                    "management": "Duy trì kali máu >4.0 mEq/L. Theo dõi kali máu thường xuyên. Cân nhắc dùng kali-sparing diuretic hoặc bổ sung kali."
                }
            ],
            "moderate": [
                {
                    "drug": "Cyclosporine, Tacrolimus",
                    "mechanism": "Cyclosporine/tacrolimus ức chế P-glycoprotein",
                    "effect": "Tăng nồng độ digoxin",
                    "management": "Theo dõi nồng độ digoxin. Có thể cần giảm liều digoxin."
                },
                {
                    "drug": "Propafenone, Flecainide",
                    "mechanism": "Propafenone/flecainide có thể tăng nồng độ digoxin",
                    "effect": "Tăng nguy cơ ngộ độc digoxin",
                    "management": "Theo dõi nồng độ digoxin. Có thể cần giảm liều digoxin."
                },
                {
                    "drug": "Spironolactone, Eplerenone",
                    "mechanism": "Spironolactone/eplerenone ức chế thải trừ digoxin, có thể tăng kali máu",
                    "effect": "Tăng nồng độ digoxin (nhẹ), có thể tăng kali máu",
                    "management": "Theo dõi nồng độ digoxin và kali máu. Thường không cần giảm liều digoxin."
                },
                {
                    "drug": "Cholestyramine, Colestipol",
                    "mechanism": "Giảm hấp thu digoxin",
                    "effect": "Giảm nồng độ digoxin, giảm hiệu quả",
                    "management": "Dùng digoxin ít nhất 2 giờ trước hoặc sau các thuốc này."
                },
                {
                    "drug": "Rifampin",
                    "mechanism": "Rifampin tăng chuyển hóa digoxin (hiếm)",
                    "effect": "Giảm nồng độ digoxin",
                    "management": "Theo dõi nồng độ digoxin. Có thể cần tăng liều digoxin."
                }
            ],
            "minor": [
                {
                    "drug": "NSAIDs",
                    "mechanism": "Có thể giảm thải trừ digoxin nhẹ",
                    "effect": "Tăng nồng độ digoxin nhẹ",
                    "management": "Thận trọng. Theo dõi nồng độ digoxin."
                },
                {
                    "drug": "Calcium",
                    "mechanism": "Tăng Ca2+ nội bào (tương tự digoxin)",
                    "effect": "Tăng nguy cơ ngộ độc digoxin (tăng lực co bóp tim quá mức)",
                    "management": "Thận trọng khi dùng calcium IV. Theo dõi ECG."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Block nhĩ thất độ 2-3",
                "Nhịp tim chậm nặng (<50 bpm)",
                "Hội chứng Wolff-Parkinson-White với rung nhĩ (tăng nguy cơ nhịp nhanh thất nguy hiểm)",
                "Ngộ độc digoxin đang hoạt động",
                "Hạ kali máu nặng không kiểm soát được",
                "Hạ magie máu nặng không kiểm soát được"
            ],
            "tương_đối": [
                "Suy thận nặng (half-life tăng lên 4-6 ngày, tăng nguy cơ tích lũy)",
                "Suy gan (thận trọng, theo dõi chức năng gan)",
                "Người già (tăng nhạy cảm, giảm chức năng thận)",
                "Bệnh phổi nặng (tăng nhạy cảm)",
                "Rối loạn điện giải (hạ K+, hạ Mg2+)"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Có thể dùng khi cần thiết. Digoxin đi qua nhau thai. Nồng độ trong máu thai nhi thường thấp hơn mẹ. Có thể gây nhịp tim chậm thai nhi, nhưng thường an toàn. Theo dõi sát thai nhi. Cân nhắc lợi ích/nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Digoxin bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp (<1 ng/mL). Không có báo cáo về tác dụng phụ nghiêm trọng ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có dấu hiệu nhịp tim chậm hoặc triệu chứng ngộ độc digoxin."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng (digoxin không chuyển hóa qua gan, nhưng suy gan có thể ảnh hưởng đến protein binding)",
            "severe": "Thận trọng, có thể giảm liều nhẹ",
            "notes": "Digoxin thải chủ yếu qua thận (75-80%), không chuyển hóa qua gan. Tuy nhiên, suy gan có thể ảnh hưởng đến protein binding và có thể tăng nhạy cảm. Thận trọng ở bệnh nhân suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn",
                "Rối loạn thị giác (nhìn vàng xanh, halos, blur)",
                "Nhịp tim chậm nặng",
                "Block nhĩ thất độ 2-3",
                "Rối loạn nhịp tim (ngoại tâm thu, nhịp nhanh thất, VT, VF)",
                "Hạ kali máu (do ngộ độc digoxin)",
                "Tử vong"
            ],
            "antidote": "Digoxin Immune Fab (Digibind, DigiFab) - ANTIDOTE ĐẶC HIỆU",
            "treatment": [
                "NGỪNG DIGOXIN NGAY LẬP TỨC",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị ngộ độc nặng: Digoxin Immune Fab (Digibind/DigiFab) - liều theo nồng độ digoxin hoặc liều uống",
                "Công thức: Số lọ Digibind = (nồng độ digoxin ng/mL × cân nặng kg) / 100 (hoặc liều uống mg / 0.6)",
                "Điều trị hạ kali máu: Kali chloride IV (THẬN TRỌNG - có thể làm nặng block AV nếu ngộ độc nặng)",
                "Điều trị block AV/nhịp tim chậm: Atropine 0.5-1mg IV, máy tạo nhịp tạm thời nếu cần",
                "Điều trị rối loạn nhịp: Phenytoin, lidocaine (tránh dùng quinidine, procainamide - có thể làm nặng)",
                "Điều trị hạ magie máu: Magie sulfate IV",
                "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "Theo dõi ít nhất 24-48 giờ (do half-life dài 36-48 giờ)"
            ],
            "monitoring": "Nồng độ digoxin (trước và sau Digibind), ECG liên tục (block AV, rối loạn nhịp), huyết áp, nhịp tim, điện giải (K+, Mg2+), chức năng thận, ý thức"
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Digoxin Immune Fab (Digibind, DigiFab)",
                    "mechanism": "Kháng thể đặc hiệu gắn với digoxin, tạo phức hợp không hoạt động, tăng thải trừ qua thận",
                    "indication": "Ngộ độc digoxin nặng (rối loạn nhịp đe dọa tính mạng, block AV, nồng độ >2 ng/mL với triệu chứng)",
                    "dose": "Liều tính theo: (nồng độ digoxin ng/mL × cân nặng kg) / 100, HOẶC (liều uống mg) / 0.6. Thường 10-20 lọ (380mg/lọ). Tiêm IV từ từ."
                }
            ]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Không ảnh hưởng đáng kể đến hấp thu.",
                "timing": "Uống 1 lần/ngày, cùng giờ mỗi ngày. Uống cùng thời điểm để duy trì nồng độ ổn định. KHÔNG bỏ liều. Nếu quên: uống ngay khi nhớ, nhưng không uống gấp đôi."
            },
            "iv": {
                "reconstitution": "Digoxin IV: Pha với D5W hoặc normal saline. Nồng độ: 0.25mg/ml. KHÔNG pha với các thuốc khác.",
                "infusion_rate": "Bolus: 0.25-0.5mg IV qua 5-10 phút. KHÔNG tiêm trực tiếp (nguy cơ block AV). Theo dõi ECG và huyết áp liên tục trong khi tiêm.",
                "compatibility": ["D5W", "Normal saline"],
                "incompatibility": ["KHÔNG trộn với các thuốc khác"],
                "notes": "Dùng cho cấp cứu. Tiêm CHẬM qua 5-10 phút. Theo dõi ECG và huyết áp liên tục. Chuyển sang PO càng sớm càng tốt."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Lanoxin (digoxin)",
                "UpToDate - Digoxin: Drug information",
                "DIG Study - New England Journal of Medicine (1997) - Digoxin trong suy tim",
                "AFFIRM Study - New England Journal of Medicine (2002) - Digoxin trong rung nhĩ",
                "American Heart Association/American College of Cardiology guidelines - Heart failure, Atrial fibrillation"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Multiple large RCTs (DIG, AFFIRM) and extensive clinical experience"
        }
    },

}

__all__ = ['OTHER_CV_DRUGS']
