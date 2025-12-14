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
        "pediatric_dosing": {
            "neonates": "10-15mcg/kg/ngày chia 2 lần (PO) hoặc 15-25mcg/kg/ngày (IV). Loading: 20-30mcg/kg chia 3 lần trong 24h. Theo dõi nồng độ digoxin chặt chẽ",
            "infants": "10-15mcg/kg/ngày chia 2 lần (PO) hoặc 15-25mcg/kg/ngày (IV). Loading: 20-30mcg/kg chia 3 lần trong 24h. Theo dõi nồng độ digoxin chặt chẽ",
            "children": "10-15mcg/kg/ngày chia 2 lần (PO) hoặc 15-25mcg/kg/ngày (IV). Loading: 20-30mcg/kg chia 3 lần trong 24h. Theo dõi nồng độ digoxin, K+, Mg2+ chặt chẽ",
            "adolescents": "0.125-0.25mg x 1 lần/ngày (PO) hoặc 0.25-0.5mg IV. Liều người lớn. Theo dõi nồng độ digoxin",
            "notes": "Dùng cho suy tim và rối loạn nhịp ở trẻ em. Liều tính theo cân nặng. BẮT BUỘC theo dõi nồng độ digoxin trong máu (mục tiêu 0.8-2 ng/mL). Theo dõi K+, Mg2+ (hạ K+, hạ Mg2+ → tăng nguy cơ ngộ độc). Giảm liều ở suy thận"
        },
        "geriatric_dosing": {
            "considerations": "Người cao tuổi nhạy cảm hơn với ngộ độc digoxin. Suy thận phổ biến hơn → half-life tăng (4-6 ngày). Cần liều thấp hơn",
            "dose_adjustment": "Khởi đầu với liều thấp (0.0625-0.125mg/ngày). Điều chỉnh theo CrCl. Tránh loading dose nhanh. Theo dõi nồng độ digoxin chặt chẽ hơn",
            "monitoring": "Theo dõi nồng độ digoxin thường xuyên hơn (mỗi 1-2 tuần khi bắt đầu). Theo dõi K+, Mg2+, creatinine. Cảnh báo về triệu chứng ngộ độc (buồn nôn, rối loạn thị giác, rối loạn nhịp)"
        },
        "brand_names": {
            "vietnam": ["Lanoxin", "Digoxin Stada", "Digoxin", "Cardiox"],
            "common": ["Lanoxin", "Digoxin"]
        },
        "cost_estimate": {
            "unit": "VND",
            "range": "3,000 - 12,000 VND/viên (tùy hàm lượng và thương hiệu)",
            "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Digoxin generic thường rẻ hơn (3,000-8,000 VND/viên 0.25mg)."
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

    "Clonidine": {
        "group": "Cardiovascular - Central Alpha-2 Agonist",
        "vietnamese_name": "Clonidine, Catapres",
        "administration": ["PO", "Transdermal"],
        "indications": [
            "Tăng huyết áp",
            "Cai nghiện opioid",
            "Cai nghiện rượu",
            "Rối loạn tăng động giảm chú ý (ADHD)",
            "Đau dây thần kinh",
            "Đổ mồ hôi quá mức"
        ],
        "contraindications": [
            "Dị ứng clonidine",
            "Block nhĩ thất độ 2-3",
            "Sick sinus syndrome"
        ],
        "dosage": {
            "adult_htn": "0.1-0.3mg x 2-3 lần/ngày, tăng dần đến 0.6-2.4mg/ngày",
            "adult_htn_transdermal": "Patch 0.1-0.3mg/ngày, thay mỗi 7 ngày",
            "adult_opioid_withdrawal": "0.1-0.3mg x 3 lần/ngày",
            "notes": "KHÔNG ngừng đột ngột (rebound hypertension). Giảm liều dần trong 2-4 ngày."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, có thể giảm liều",
            "under_30": "Thận trọng, giảm liều 25-50%"
        },
        "side_effects": [
            "Khô miệng (thường gặp)",
            "Buồn ngủ, mệt mỏi",
            "Chóng mặt",
            "Táo bón",
            "Rebound hypertension (nếu ngừng đột ngột)",
            "Nhịp tim chậm",
            "Hạ huyết áp tư thế"
        ],
        "interactions": [
            "Beta-blocker: tăng nguy cơ nhịp tim chậm, block AV khi ngừng clonidine",
            "Tricyclic antidepressants: giảm hiệu quả clonidine",
            "Alcohol, sedatives: tăng tác dụng an thần"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Central alpha-2 adrenergic agonist. Kích thích thụ thể alpha-2 ở hành não (nucleus tractus solitarius), làm giảm hoạt động giao cảm, giảm giải phóng norepinephrine từ các neuron giao cảm trung ương. Kết quả: giảm nhịp tim, giảm sức cản mạch máu ngoại vi, giảm huyết áp. Cũng có tác dụng giảm đau và giảm triệu chứng cai nghiện opioid/rượu. Clonidine cũng có tác dụng ngoại vi nhẹ (alpha-2 agonist ngoại vi).",
        "monitoring": [
            "Huyết áp và nhịp tim (đặc biệt khi bắt đầu và khi ngừng)",
            "Dấu hiệu rebound hypertension (nếu ngừng đột ngột)",
            "Dấu hiệu quá liều (hạ huyết áp nặng, nhịp tim chậm, buồn ngủ nặng)",
            "Chức năng thận (creatinine, eGFR)"
        ],
        "precautions": [
            "KHÔNG ngừng đột ngột - phải giảm liều dần trong 2-4 ngày (nguy cơ rebound hypertension nặng)",
            "Thận trọng ở suy thận (giảm thải trừ)",
            "Thận trọng ở bệnh nhân có block AV hoặc nhịp tim chậm",
            "Tăng tác dụng an thần với alcohol, sedatives",
            "Dạng transdermal: có thể gây kích ứng da, thay vị trí mỗi tuần",
            "Tương tác với beta-blockers: không ngừng clonidine đột ngột khi đang dùng beta-blocker"
        ],
        "pharmacokinetics": {
            "half_life": "12-16 giờ",
            "onset": "30-60 phút (PO), 2-3 ngày (transdermal)",
            "duration": "6-8 giờ (PO), 7 ngày (transdermal patch)",
            "protein_binding": "20-40%",
            "metabolism": "Gan (50%), thận (50% bài tiết không đổi)",
            "clearance": "Gan và thận, cần điều chỉnh ở suy thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng. Patch: bảo quản trong túi kín, tránh nhiệt độ cao.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, ngừng đột ngột clonidine có thể gây rebound hypertension nặng, đe dọa tính mạng. PHẢI giảm liều dần trong 2-4 ngày.",
        "references": {
            "primary_sources": [
                "FDA Drug Label - Catapres (clonidine)",
                "UpToDate - Clonidine: Drug information",
                "American Heart Association/American College of Cardiology guidelines - Hypertension"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - Extensive clinical experience in hypertension and opioid withdrawal"
        }
    },

    "Methyldopa": {
        "group": "Cardiovascular - Central Alpha-2 Agonist",
        "vietnamese_name": "Methyldopa, Aldomet",
        "administration": ["PO", "IV"],
        "indications": [
            "Tăng huyết áp thai kỳ (ưu tiên)",
            "Tăng huyết áp",
            "Tăng huyết áp ở bệnh nhân suy thận"
        ],
        "contraindications": [
            "Dị ứng methyldopa",
            "Bệnh gan hoạt động",
            "Pheochromocytoma",
            "Dùng MAO inhibitors"
        ],
        "dosage": {
            "adult_htn": "250mg x 2-3 lần/ngày, tăng dần đến 500-2000mg/ngày chia 2-4 lần",
            "adult_htn_max": "Tối đa 3000mg/ngày",
            "adult_pregnancy": "250mg x 2-3 lần/ngày, tăng dần đến 500-2000mg/ngày",
            "adult_iv": "250-500mg IV mỗi 6 giờ",
            "notes": "Thuốc lựa chọn cho tăng huyết áp thai kỳ"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, giảm liều 25-50%",
            "under_30": "Giảm liều 50%"
        },
        "side_effects": [
            "Buồn ngủ, mệt mỏi (thường gặp khi bắt đầu)",
            "Khô miệng",
            "Chóng mặt",
            "Hạ huyết áp tư thế",
            "Rối loạn chức năng gan (hiếm nhưng nguy hiểm)",
            "Hemolytic anemia (hiếm)",
            "Dương tính Coombs test (không có triệu chứng)",
            "Tăng prolactin"
        ],
        "interactions": [
            "MAO inhibitors: tăng tác dụng, nguy hiểm",
            "Lithium: tăng nguy cơ độc tính lithium",
            "Iron: giảm hấp thu methyldopa",
            "Antidepressants: có thể giảm hiệu quả"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Central alpha-2 adrenergic agonist (tương tự clonidine). Methyldopa được chuyển hóa thành alpha-methylnorepinephrine trong não, kích thích thụ thể alpha-2 ở hành não, làm giảm hoạt động giao cảm trung ương, giảm giải phóng norepinephrine. Kết quả: giảm nhịp tim, giảm sức cản mạch máu ngoại vi, giảm huyết áp. Methyldopa là thuốc lựa chọn cho tăng huyết áp thai kỳ vì an toàn cho thai nhi (category B).",
        "monitoring": [
            "Huyết áp và nhịp tim",
            "Chức năng gan (ALT, AST, bilirubin) - QUAN TRỌNG (có thể gây viêm gan)",
            "Công thức máu (hemolytic anemia hiếm)",
            "Coombs test (dương tính nhưng thường không có triệu chứng)",
            "Dấu hiệu quá liều (hạ huyết áp nặng, buồn ngủ nặng)"
        ],
        "precautions": [
            "Theo dõi chức năng gan định kỳ (có thể gây viêm gan, ngừng ngay nếu có)",
            "Thận trọng ở suy thận (giảm thải trừ)",
            "Thận trọng ở bệnh nhân có bệnh gan (chống chỉ định nếu bệnh gan hoạt động)",
            "Dương tính Coombs test thường gặp nhưng không có triệu chứng",
            "Hemolytic anemia hiếm nhưng cần theo dõi",
            "Tăng prolactin có thể gây vú to, tiết sữa",
            "Buồn ngủ thường gặp khi bắt đầu, thường giảm sau vài tuần",
            "KHÔNG dùng với MAO inhibitors",
            "Dùng cách xa bữa ăn với iron (giảm hấp thu)"
        ],
        "pharmacokinetics": {
            "half_life": "1.5-2 giờ",
            "onset": "2-4 giờ (PO), 4-6 giờ (IV)",
            "duration": "12-24 giờ",
            "protein_binding": "Thấp",
            "metabolism": "Gan (chuyển hóa thành alpha-methylnorepinephrine)",
            "clearance": "Thận (70%), cần điều chỉnh ở suy thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng. Viên nén: ổn định.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, methyldopa có thể gây rối loạn chức năng gan nặng (viêm gan, hoại tử gan) - ngừng ngay nếu có dấu hiệu viêm gan.",
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Methyldopa là thuốc lựa chọn cho tăng huyết áp thai kỳ. An toàn cho thai nhi (category B). Đã được sử dụng rộng rãi trong thai kỳ với dữ liệu an toàn tốt. Có thể dùng trong cả 3 tam cá nguyệt.",
            "lactation": {
                "safety": "Compatible",
                "details": "Methyldopa bài tiết vào sữa mẹ ở nồng độ thấp. Không có báo cáo về tác dụng phụ nghiêm trọng ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có dấu hiệu hạ huyết áp hoặc buồn ngủ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng (methyldopa chuyển hóa ở gan)",
            "moderate": "Thận trọng, giảm liều 25-50%",
            "severe": "CHỐNG CHỈ ĐỊNH nếu bệnh gan hoạt động",
            "notes": "Methyldopa chuyển hóa ở gan. Có thể gây viêm gan, hoại tử gan. CHỐNG CHỈ ĐỊNH ở bệnh nhân có bệnh gan hoạt động. Theo dõi chức năng gan định kỳ. Ngừng ngay nếu có dấu hiệu viêm gan."
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Aldomet (methyldopa)",
                "UpToDate - Methyldopa: Drug information",
                "ACOG Practice Bulletin - Hypertension in Pregnancy",
                "American Heart Association/American College of Cardiology guidelines - Hypertension"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - Extensive clinical experience, especially in pregnancy (category B, preferred for pregnancy hypertension)"
        }
    },

    "Labetalol": {
        "group": "Cardiovascular - Alpha-Beta Blocker",
        "vietnamese_name": "Labetalol, Normodyne, Trandate",
        "administration": ["PO", "IV"],
        "indications": [
            "Tăng huyết áp",
            "Tăng huyết áp cấp cứu",
            "Tăng huyết áp thai kỳ",
            "Pheochromocytoma (preoperative)"
        ],
        "contraindications": [
            "Hen phế quản nặng",
            "Block nhĩ thất độ 2-3",
            "Suy tim cấp không bù",
            "Nhịp tim chậm nặng (<60 bpm)",
            "Sốc tim"
        ],
        "dosage": {
            "adult_po": "100mg x 2 lần/ngày, tăng dần đến 200-400mg x 2 lần/ngày (tối đa 2400mg/ngày)",
            "adult_iv_bolus": "20mg IV, sau đó 40-80mg mỗi 10 phút (tối đa 300mg)",
            "adult_iv_infusion": "2mg/phút, tăng dần đến 5-10mg/phút",
            "pregnancy_htn": "100mg x 2 lần/ngày, tăng dần đến 200-400mg x 2 lần/ngày",
            "notes": "Có cả dạng PO và IV. Dạng IV dùng cho tăng huyết áp cấp cứu. An toàn trong thai kỳ."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, có thể giảm liều",
            "under_30": "Giảm liều 50%"
        },
        "side_effects": [
            "Mệt mỏi",
            "Chóng mặt",
            "Nhịp tim chậm",
            "Hạ huyết áp tư thế đứng",
            "Khó thở ở bệnh nhân hen/COPD (ít hơn beta-blocker thuần túy)",
            "Rối loạn cương dương",
            "Rối loạn giấc ngủ"
        ],
        "interactions": [
            "Verapamil/Diltiazem: tăng nguy cơ block nhĩ thất",
            "Insulin: che dấu triệu chứng hạ đường huyết",
            "Halothane: tăng nguy cơ hạ huyết áp"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Labetalol là alpha-1 và beta (beta-1 và beta-2) adrenergic receptor blocker. Ức chế alpha-1 → giãn mạch ngoại vi → giảm sức cản mạch máu. Ức chế beta-1 → giảm nhịp tim, giảm co bóp cơ tim. Ức chế beta-2 → có thể gây co thắt phế quản (nhưng ít hơn beta-blocker thuần túy). Tỷ lệ alpha:beta = 1:3 (PO) và 1:7 (IV). Đặc điểm: hạ huyết áp hiệu quả mà không làm giảm nhịp tim nhiều (do alpha-blockade bù trừ). An toàn trong thai kỳ.",
        "monitoring": [
            "Huyết áp và nhịp tim (theo dõi chặt chẽ khi bắt đầu, đặc biệt dạng IV)",
            "Dấu hiệu hạ huyết áp tư thế đứng",
            "Dấu hiệu suy tim: khó thở, phù, tăng cân",
            "Chức năng thận (thải một phần qua thận)",
            "Đường huyết (ở bệnh nhân đái tháo đường)",
            "Triệu chứng mệt mỏi, chóng mặt"
        ],
        "precautions": [
            "KHÔNG được ngừng đột ngột (có thể gây rebound hypertension). Phải giảm liều dần trong 1-2 tuần",
            "Dạng IV: theo dõi huyết áp liên tục, có thể gây hạ huyết áp nhanh",
            "Thận trọng ở bệnh nhân hen phế quản/COPD (mặc dù ít gây co thắt phế quản hơn beta-blocker thuần túy)",
            "Tránh dùng trong suy tim cấp không bù, block AV độ 2-3, nhịp tim chậm <60 bpm",
            "Thận trọng ở bệnh nhân suy thận (giảm liều 50% nếu CrCl <30)",
            "Thận trọng khi dùng với verapamil/diltiazem (tăng nguy cơ block AV, suy tim)",
            "Che dấu triệu chứng hạ đường huyết ở bệnh nhân đái tháo đường",
            "An toàn trong thai kỳ - được dùng cho tăng huyết áp thai kỳ"
        ],
        "pharmacokinetics": {
            "half_life": "6-8 giờ (PO), 5.5 giờ (IV)",
            "onset": "2-4 giờ (PO), 5-10 phút (IV)",
            "duration": "8-12 giờ (PO), 2-4 giờ (IV)",
            "protein_binding": "50%",
            "clearance": "Gan (chuyển hóa) và thận (một phần)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Dạng IV: bảo quản ở nhiệt độ phòng, tránh đông lạnh.",
        "black_box_warnings": "KHÔNG được ngừng đột ngột - có thể gây tăng huyết áp phản hồi, đau thắt ngực, nhồi máu cơ tim. Giảm liều từ từ trong 1-2 tuần.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Verapamil, Diltiazem",
                    "mechanism": "Tác dụng hiệp đồng ức chế dẫn truyền nhĩ thất và co bóp tim",
                    "effect": "Tăng nguy cơ block nhĩ thất độ 2-3, nhịp tim chậm nặng, suy tim",
                    "management": "Thận trọng. Tránh dùng cùng nếu có thể. Nếu cần, dùng liều thấp và theo dõi ECG sát."
                }
            ],
            "moderate": [
                {
                    "drug": "Insulin, các thuốc hạ đường huyết",
                    "mechanism": "Che dấu triệu chứng hạ đường huyết (nhịp tim nhanh, run rẩy)",
                    "effect": "Tăng nguy cơ hạ đường huyết không được phát hiện",
                    "management": "Theo dõi đường huyết thường xuyên. Bệnh nhân đái tháo đường nên biết các triệu chứng khác của hạ đường huyết."
                },
                {
                    "drug": "Halothane, các thuốc mê",
                    "mechanism": "Tác dụng hiệp đồng hạ huyết áp",
                    "effect": "Tăng nguy cơ hạ huyết áp nặng trong phẫu thuật",
                    "management": "Thận trọng trong phẫu thuật. Theo dõi huyết áp sát. Có thể cần giảm liều labetalol."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Hen phế quản nặng",
                "Block nhĩ thất độ 2-3 không có máy tạo nhịp",
                "Suy tim cấp không bù",
                "Nhịp tim chậm nặng (<60 bpm)",
                "Sốc tim"
            ],
            "tương_đối": [
                "COPD - thận trọng (ít gây co thắt phế quản hơn beta-blocker thuần túy)",
                "Suy thận nặng (CrCl <30) - giảm liều 50%",
                "Suy thận trung bình (CrCl 30-60) - thận trọng",
                "Đái tháo đường - che dấu triệu chứng hạ đường huyết",
                "Dùng với verapamil/diltiazem - tăng nguy cơ block AV"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Labetalol được dùng rộng rãi cho tăng huyết áp thai kỳ. An toàn tương đối cho thai nhi. Có thể gây nhịp tim chậm thai nhi, hạ đường huyết. Theo dõi sát thai nhi. Ưu tiên dùng trong 3 tháng cuối nếu có thể.",
            "lactation": {
                "safety": "Compatible",
                "details": "Labetalol bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp. Không có báo cáo về tác dụng phụ nghiêm trọng ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có nhịp tim chậm, mệt mỏi."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, có thể giảm liều (chuyển hóa qua gan)",
            "severe": "Giảm liều 50% (chuyển hóa qua gan)",
            "notes": "Labetalol chuyển hóa qua gan. Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và tác dụng phụ."
        },
        "overdose_management": {
            "symptoms": [
                "Nhịp tim chậm nặng",
                "Block nhĩ thất",
                "Hạ huyết áp nặng",
                "Suy tim cấp",
                "Co thắt phế quản",
                "Hạ đường huyết"
            ],
            "antidote": "Glucagon (có thể đảo ngược tác dụng beta-blocker), Atropine (cho nhịp tim chậm)",
            "treatment": [
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị nhịp tim chậm: Atropine 0.5-1mg IV, có thể lặp lại",
                "Nếu atropine không hiệu quả: Glucagon 1-5mg IV",
                "Điều trị hạ huyết áp: Truyền dịch, nâng chân, nếu cần: dopamine, norepinephrine",
                "Điều trị co thắt phế quản: Albuterol, ipratropium",
                "Điều trị hạ đường huyết: Glucose IV",
                "Theo dõi ít nhất 12-24 giờ"
            ],
            "monitoring": "ECG, huyết áp, nhịp tim, ý thức, đường huyết, chức năng hô hấp"
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Glucagon",
                    "mechanism": "Kích thích cAMP, đảo ngược tác dụng beta-blocker",
                    "dose": "1-5mg IV, có thể lặp lại",
                    "indication": "Nhịp tim chậm, hạ huyết áp do quá liều beta-blocker"
                },
                {
                    "name": "Atropine",
                    "mechanism": "Chẹn muscarinic, tăng nhịp tim",
                    "dose": "0.5-1mg IV, có thể lặp lại",
                    "indication": "Nhịp tim chậm, block AV"
                }
            ]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Không ảnh hưởng đáng kể đến hấp thu.",
                "timing": "Uống 2 lần/ngày vào cùng giờ mỗi ngày. KHÔNG ngừng đột ngột - phải giảm liều dần trong 1-2 tuần."
            },
            "iv": {
                "reconstitution": "Dùng trực tiếp từ lọ. Có thể pha loãng trong D5W hoặc normal saline.",
                "infusion_rate": "Bolus: 20mg IV, sau đó 40-80mg mỗi 10 phút (tối đa 300mg). Infusion: 2mg/phút, tăng dần đến 5-10mg/phút. Theo dõi huyết áp liên tục.",
                "compatibility": ["D5W", "Normal saline"],
                "incompatibility": [],
                "notes": "Dùng cho tăng huyết áp cấp cứu. Theo dõi huyết áp liên tục. Chuyển sang PO càng sớm càng tốt."
            }
        },
        "pediatric_dosing": {
            "neonates": "Không khuyến cáo cho trẻ <18 tuổi (dữ liệu hạn chế)",
            "infants": "Không khuyến cáo cho trẻ <18 tuổi (dữ liệu hạn chế)",
            "children": "Không khuyến cáo cho trẻ <18 tuổi (dữ liệu hạn chế). Nếu cần, 2-4mg/kg/ngày chia 2 lần, tối đa 1200mg/ngày",
            "adolescents": "100mg x 2 lần/ngày, tăng dần đến 200-400mg x 2 lần/ngày nếu cần. Liều người lớn",
            "notes": "Dữ liệu hạn chế ở trẻ em. Chỉ dùng khi thực sự cần thiết. Theo dõi nhịp tim, huyết áp chặt chẽ"
        },
        "geriatric_dosing": {
            "considerations": "Người cao tuổi nhạy cảm hơn với tác dụng phụ (nhịp tim chậm, hạ huyết áp, mệt mỏi). Suy gan và suy thận phổ biến hơn",
            "dose_adjustment": "Khởi đầu với liều thấp hơn (50-100mg x 2 lần/ngày). Tăng dần chậm hơn. Điều chỉnh theo chức năng thận và gan",
            "monitoring": "Theo dõi nhịp tim, huyết áp sát hơn. Theo dõi chức năng thận và gan. Cảnh báo về không ngừng đột ngột"
        },
        "brand_names": {
            "vietnam": ["Normodyne", "Trandate", "Labetalol Stada", "Labetalol"],
            "common": ["Normodyne", "Trandate", "Labetalol"]
        },
        "cost_estimate": {
            "unit": "VND",
            "range": "10,000 - 30,000 VND/viên (PO), 50,000 - 150,000 VND/lọ (IV) (tùy hàm lượng và thương hiệu)",
            "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Labetalol generic thường rẻ hơn."
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Normodyne (labetalol), Trandate (labetalol)",
                "UpToDate - Labetalol: Drug information",
                "ACOG Practice Bulletin - Hypertension in Pregnancy",
                "American Heart Association/American College of Cardiology guidelines - Hypertension"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - Extensive clinical experience, especially in pregnancy and hypertensive emergencies"
        }
    },

    "Ivabradine": {
        "group": "Cardiovascular - If Channel Inhibitor",
        "vietnamese_name": "Ivabradine, Corlanor, Procoralan",
        "administration": ["PO"],
        "indications": [
            "Suy tim mạn tính (NYHA class II-IV) với nhịp xoang ≥70 bpm",
            "Đau thắt ngực ổn định với nhịp xoang ≥70 bpm (không dùng với beta-blocker)"
        ],
        "contraindications": [
            "Nhịp tim chậm (<60 bpm trước điều trị)",
            "Block nhĩ thất độ 2-3",
            "Suy tim cấp",
            "Huyết áp thấp (<90/50 mmHg)",
            "Rung nhĩ hoặc rối loạn nhịp tim khác",
            "Dùng với CYP3A4 inhibitors mạnh"
        ],
        "dosage": {
            "adult_heart_failure": "5mg x 2 lần/ngày, tăng đến 7.5mg x 2 lần/ngày nếu nhịp tim vẫn ≥60 bpm sau 2 tuần",
            "adult_angina": "5mg x 2 lần/ngày, tăng đến 7.5mg x 2 lần/ngày nếu nhịp tim vẫn ≥60 bpm",
            "elderly": "Khởi đầu 2.5mg x 2 lần/ngày",
            "notes": "Chỉ dùng cho bệnh nhân có nhịp xoang ≥70 bpm. Theo dõi nhịp tim, ngừng nếu <50 bpm."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng, khởi đầu 2.5mg x 2 lần/ngày"
        },
        "side_effects": [
            "Nhịp tim chậm (thường gặp)",
            "Rối loạn thị giác (phosphenes - nhìn thấy ánh sáng nhấp nháy, thường tạm thời)",
            "Chóng mặt",
            "Mệt mỏi",
            "Hạ huyết áp",
            "Rối loạn nhịp tim (ngoại tâm thu nhĩ, rung nhĩ)"
        ],
        "interactions": [
            "CYP3A4 inhibitors mạnh: CHỐNG CHỈ ĐỊNH (ketoconazole, itraconazole, clarithromycin, ritonavir)",
            "CYP3A4 inhibitors vừa: giảm liều 50% (diltiazem, verapamil, fluconazole)",
            "Grapefruit juice: tránh dùng"
        ],
        "pregnancy": "N/A",
        "mechanism_of_action": "Ivabradine ức chế kênh If (funny current) trong nút xoang, làm giảm nhịp tim mà không ảnh hưởng đến lực co bóp cơ tim, dẫn truyền nhĩ thất, hoặc huyết áp. Khác với beta-blocker: ivabradine chỉ làm chậm nhịp tim, không ảnh hưởng đến co bóp tim. Có bằng chứng giảm tỷ lệ tử vong và nhập viện trong suy tim mạn tính (SHIFT study). Chuyển hóa qua CYP3A4.",
        "monitoring": [
            "Nhịp tim (BẮT BUỘC): đo trước mỗi liều, ngừng nếu <50 bpm hoặc có triệu chứng nhịp tim chậm",
            "ECG: nhịp tim, block nhĩ thất, rối loạn nhịp",
            "Dấu hiệu suy tim: khó thở, phù, tăng cân",
            "Huyết áp (có thể gây hạ huyết áp)",
            "Rối loạn thị giác (phosphenes - thường tạm thời, không nguy hiểm)",
            "Chức năng thận (thải một phần qua thận)"
        ],
        "precautions": [
            "CHỈ dùng cho bệnh nhân có nhịp xoang ≥70 bpm",
            "Ngừng ngay nếu nhịp tim <50 bpm hoặc có triệu chứng nhịp tim chậm",
            "CHỐNG CHỈ ĐỊNH với CYP3A4 inhibitors mạnh (ketoconazole, itraconazole, clarithromycin, ritonavir)",
            "Giảm liều 50% với CYP3A4 inhibitors vừa (diltiazem, verapamil, fluconazole)",
            "Tránh grapefruit juice (ức chế CYP3A4)",
            "Thận trọng ở suy thận nặng (CrCl <30) - khởi đầu 2.5mg x 2 lần/ngày",
            "Rối loạn thị giác (phosphenes) thường tạm thời, không nguy hiểm, thường tự hết",
            "Có thể dùng cùng với beta-blocker trong suy tim (nhưng thận trọng - tăng nguy cơ nhịp tim chậm)",
            "Không dùng trong suy tim cấp"
        ],
        "pharmacokinetics": {
            "half_life": "2 giờ (nhưng tác dụng kéo dài do tác dụng trên kênh If)",
            "onset": "1 giờ",
            "duration": "12 giờ (uống 2 lần/ngày)",
            "protein_binding": "70%",
            "clearance": "Gan (CYP3A4) và thận (một phần)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH với CYP3A4 inhibitors mạnh (ketoconazole, itraconazole, clarithromycin, ritonavir) - có thể tăng nồng độ ivabradine đáng kể, tăng nguy cơ nhịp tim chậm nặng.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "CYP3A4 inhibitors mạnh (ketoconazole, itraconazole, clarithromycin, erythromycin, ritonavir, cobicistat)",
                    "mechanism": "Ức chế chuyển hóa ivabradine qua CYP3A4",
                    "effect": "Tăng nồng độ ivabradine đáng kể (có thể tăng 7-8 lần), tăng nguy cơ nhịp tim chậm nặng, block AV",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI. Không dùng cùng."
                }
            ],
            "moderate": [
                {
                    "drug": "CYP3A4 inhibitors vừa (diltiazem, verapamil, fluconazole)",
                    "mechanism": "Ức chế chuyển hóa ivabradine qua CYP3A4",
                    "effect": "Tăng nồng độ ivabradine, tăng nguy cơ nhịp tim chậm",
                    "management": "Giảm liều ivabradine 50% (2.5mg x 2 lần/ngày). Theo dõi nhịp tim chặt chẽ."
                },
                {
                    "drug": "Grapefruit juice",
                    "mechanism": "Ức chế CYP3A4",
                    "effect": "Tăng nồng độ ivabradine, tăng nguy cơ nhịp tim chậm",
                    "management": "TRÁNH hoàn toàn grapefruit juice khi dùng ivabradine."
                },
                {
                    "drug": "Beta-blockers",
                    "mechanism": "Tác dụng hiệp đồng làm chậm nhịp tim",
                    "effect": "Tăng nguy cơ nhịp tim chậm nặng",
                    "management": "Thận trọng. Có thể dùng cùng trong suy tim nhưng theo dõi nhịp tim chặt chẽ. Có thể cần giảm liều một trong hai thuốc."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Nhịp tim chậm (<60 bpm trước điều trị)",
                "Block nhĩ thất độ 2-3 không có máy tạo nhịp",
                "Suy tim cấp",
                "Huyết áp thấp (<90/50 mmHg)",
                "Rung nhĩ hoặc rối loạn nhịp tim khác (chỉ dùng cho nhịp xoang)",
                "Dùng với CYP3A4 inhibitors mạnh (ketoconazole, itraconazole, clarithromycin, ritonavir)"
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - thận trọng, khởi đầu 2.5mg x 2 lần/ngày",
                "Dùng với CYP3A4 inhibitors vừa (diltiazem, verapamil, fluconazole) - giảm liều 50%",
                "Dùng với beta-blockers - tăng nguy cơ nhịp tim chậm"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "N/A",
            "pregnancy_details": "Không có dữ liệu đầy đủ trên phụ nữ có thai. Không khuyến cáo dùng trong thai kỳ trừ khi lợi ích vượt trội nguy cơ.",
            "lactation": {
                "safety": "Unknown",
                "details": "Không biết ivabradine có bài tiết vào sữa mẹ hay không. Không khuyến cáo dùng khi cho con bú.",
                "recommendation": "Tránh dùng khi cho con bú. Nếu cần, ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, có thể giảm liều (chuyển hóa qua gan)",
            "severe": "Thận trọng, giảm liều 50% (chuyển hóa qua gan CYP3A4)",
            "notes": "Ivabradine chuyển hóa qua gan (CYP3A4). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và tác dụng phụ."
        },
        "overdose_management": {
            "symptoms": [
                "Nhịp tim chậm nặng (<40 bpm)",
                "Block nhĩ thất",
                "Hạ huyết áp nặng",
                "Chóng mặt, ngất",
                "Mệt mỏi nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Atropine (cho nhịp tim chậm)",
            "treatment": [
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị nhịp tim chậm: Atropine 0.5-1mg IV, có thể lặp lại",
                "Nếu atropine không hiệu quả: Isoproterenol hoặc máy tạo nhịp tạm thời",
                "Điều trị hạ huyết áp: Truyền dịch, nâng chân, nếu cần: dopamine, norepinephrine",
                "Theo dõi ECG liên tục",
                "Theo dõi ít nhất 12-24 giờ"
            ],
            "monitoring": "ECG liên tục, huyết áp, nhịp tim, ý thức"
        },
        "reversal_agents": {
            "available": False,
            "agents": [
                {
                    "name": "Atropine",
                    "mechanism": "Chẹn muscarinic, tăng nhịp tim",
                    "dose": "0.5-1mg IV, có thể lặp lại",
                    "indication": "Nhịp tim chậm do quá liều ivabradine"
                }
            ],
            "notes": "Không có antidote đặc hiệu. Điều trị hỗ trợ. Atropine có thể giúp tăng nhịp tim."
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn để tăng hấp thu và giảm tác dụng phụ.",
                "timing": "Uống 2 lần/ngày (sáng và tối) vào cùng giờ mỗi ngày. Đo nhịp tim trước mỗi liều. Ngừng nếu nhịp tim <50 bpm hoặc có triệu chứng nhịp tim chậm."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Ivabradine chỉ có dạng uống (PO)."
            }
        },
        "pediatric_dosing": {
            "neonates": "Không khuyến cáo cho trẻ <18 tuổi (dữ liệu hạn chế)",
            "infants": "Không khuyến cáo cho trẻ <18 tuổi (dữ liệu hạn chế)",
            "children": "Không khuyến cáo cho trẻ <18 tuổi (dữ liệu hạn chế)",
            "adolescents": "Không khuyến cáo cho trẻ <18 tuổi (dữ liệu hạn chế)",
            "notes": "Dữ liệu hạn chế ở trẻ em. Chỉ dùng khi thực sự cần thiết và có chỉ định đặc biệt."
        },
        "geriatric_dosing": {
            "considerations": "Người cao tuổi nhạy cảm hơn với tác dụng phụ (nhịp tim chậm, hạ huyết áp). Suy gan và suy thận phổ biến hơn",
            "dose_adjustment": "Khởi đầu với liều thấp hơn (2.5mg x 2 lần/ngày). Tăng dần chậm hơn. Điều chỉnh theo chức năng thận và gan",
            "monitoring": "Theo dõi nhịp tim sát hơn. Đo nhịp tim trước mỗi liều. Theo dõi chức năng thận và gan"
        },
        "brand_names": {
            "vietnam": ["Corlanor", "Procoralan", "Ivabradine"],
            "common": ["Corlanor", "Procoralan", "Ivabradine"]
        },
        "cost_estimate": {
            "unit": "VND",
            "range": "50,000 - 150,000 VND/viên (tùy hàm lượng và thương hiệu)",
            "note": "Giá cao hơn các thuốc tim mạch khác do là thuốc mới. Giá thay đổi theo thương hiệu và nhà thuốc."
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Corlanor (ivabradine)",
                "UpToDate - Ivabradine: Drug information",
                "SHIFT Study - The Lancet (2010) - Ivabradine trong suy tim",
                "American Heart Association/American College of Cardiology guidelines - Heart failure"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - Large RCT (SHIFT) showing mortality and hospitalization benefit in heart failure"
        }
    },

    "Sacubitril-valsartan": {
        "group": "Cardiovascular - ARNI (Angiotensin Receptor-Neprilysin Inhibitor)",
        "vietnamese_name": "Sacubitril-valsartan, Entresto",
        "administration": ["PO"],
        "indications": [
            "Suy tim mạn tính (NYHA class II-IV) với EF giảm (≤40%)",
            "Thay thế ACE inhibitor hoặc ARB trong suy tim"
        ],
        "contraindications": [
            "Dị ứng sacubitril-valsartan hoặc bất kỳ thành phần nào",
            "Dị ứng với ACE inhibitor hoặc ARB (phù mạch)",
            "Dùng với ACE inhibitor (phải ngừng ACE inhibitor 36 giờ trước)",
            "Phụ nữ có thai",
            "Bệnh thận đái tháo đường (type 1 hoặc type 2) với protein niệu >300mg/ngày",
            "Suy thận nặng (eGFR <30 mL/min/1.73m²)"
        ],
        "dosage": {
            "adult_initial": "49/51mg (sacubitril/valsartan) x 2 lần/ngày",
            "adult_target": "97/103mg x 2 lần/ngày sau 2-4 tuần",
            "adult_elderly_or_renal": "Khởi đầu 24/26mg x 2 lần/ngày",
            "adult_switching_from_acei": "Ngừng ACE inhibitor 36 giờ, sau đó khởi đầu 49/51mg x 2 lần/ngày",
            "notes": "Phải ngừng ACE inhibitor 36 giờ trước khi bắt đầu. Có bằng chứng giảm tỷ lệ tử vong và nhập viện (PARADIGM-HF study)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Khởi đầu 24/26mg x 2 lần/ngày, tăng dần",
            "under_30": "CHỐNG CHỈ ĐỊNH (eGFR <30)"
        },
        "side_effects": [
            "Hạ huyết áp (thường gặp)",
            "Tăng kali máu",
            "Ho (ít hơn ACE inhibitor)",
            "Chóng mặt",
            "Mệt mỏi",
            "Suy thận (hiếm)",
            "Phù mạch (hiếm nhưng nguy hiểm)"
        ],
        "interactions": [
            "ACE inhibitor: CHỐNG CHỈ ĐỊNH (phải ngừng 36 giờ trước)",
            "Kali-sparing diuretics: tăng nguy cơ tăng kali máu",
            "Kali bổ sung: tăng nguy cơ tăng kali máu",
            "NSAIDs: tăng nguy cơ suy thận",
            "Lithium: tăng nồng độ lithium"
        ],
        "pregnancy": "D",
        "mechanism_of_action": "Sacubitril-valsartan là phối hợp của sacubitril (ức chế neprilysin) và valsartan (ức chế thụ thể angiotensin II). Sacubitril ức chế neprilysin → tăng nồng độ natriuretic peptides (ANP, BNP) → giãn mạch, lợi tiểu, giảm tái hấp thu natri. Valsartan ức chế thụ thể angiotensin II → giảm tác dụng của angiotensin II (co mạch, giữ natri). Kết hợp: giảm tiền tải và hậu tải, cải thiện chức năng tim. Có bằng chứng mạnh giảm tỷ lệ tử vong và nhập viện trong suy tim (PARADIGM-HF study) - tốt hơn enalapril.",
        "monitoring": [
            "Huyết áp (theo dõi chặt chẽ khi bắt đầu, đặc biệt 2 tuần đầu)",
            "Creatinine, eGFR (theo dõi suy thận)",
            "Kali máu (theo dõi tăng kali máu)",
            "Dấu hiệu suy tim: khó thở, phù, tăng cân",
            "Dấu hiệu phù mạch: sưng mặt, môi, lưỡi, họng (nguy hiểm, cần điều trị ngay)",
            "Triệu chứng hạ huyết áp: chóng mặt, ngất"
        ],
        "precautions": [
            "PHẢI ngừng ACE inhibitor 36 giờ trước khi bắt đầu sacubitril-valsartan (nguy cơ phù mạch)",
            "CHỐNG CHỈ ĐỊNH trong thai kỳ (category D - gây hại cho thai nhi)",
            "CHỐNG CHỈ ĐỊNH ở bệnh nhân đái tháo đường với protein niệu >300mg/ngày",
            "CHỐNG CHỈ ĐỊNH ở suy thận nặng (eGFR <30)",
            "Thận trọng ở suy thận trung bình (eGFR 30-60) - khởi đầu liều thấp",
            "Theo dõi kali máu (tăng kali máu có thể xảy ra)",
            "Theo dõi creatinine (suy thận có thể xảy ra, đặc biệt khi dùng với NSAIDs)",
            "Tránh dùng với kali-sparing diuretics hoặc kali bổ sung (trừ khi được giám sát chặt chẽ)",
            "Có bằng chứng mạnh giảm tỷ lệ tử vong và nhập viện trong suy tim - tốt hơn ACE inhibitor"
        ],
        "pharmacokinetics": {
            "half_life": "Sacubitril: 1.4 giờ, Valsartan: 9.9 giờ",
            "onset": "1-2 giờ",
            "duration": "12 giờ (uống 2 lần/ngày)",
            "protein_binding": "Sacubitril: 97%, Valsartan: 94-97%",
            "clearance": "Gan (chuyển hóa) và thận (một phần)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm. Viên nén: ổn định.",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH trong thai kỳ - có thể gây hại hoặc tử vong cho thai nhi. Phụ nữ trong độ tuổi sinh đẻ phải sử dụng biện pháp tránh thai hiệu quả. Ngừng ngay nếu có thai.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "ACE inhibitors (enalapril, lisinopril, ramipril, etc.)",
                    "mechanism": "Cả hai đều ức chế hệ renin-angiotensin, tăng nguy cơ phù mạch",
                    "effect": "Tăng nguy cơ phù mạch đe dọa tính mạng, suy thận, hạ huyết áp nặng",
                    "management": "CHỐNG CHỈ ĐỊNH. PHẢI ngừng ACE inhibitor 36 giờ trước khi bắt đầu sacubitril-valsartan."
                },
                {
                    "drug": "Kali-sparing diuretics (spironolactone, eplerenone, amiloride, triamterene)",
                    "mechanism": "Cả hai đều có thể tăng kali máu",
                    "effect": "Tăng nguy cơ tăng kali máu nặng (>5.5 mEq/L), có thể đe dọa tính mạng",
                    "management": "Thận trọng. Theo dõi kali máu chặt chẽ. Có thể cần giảm liều một trong hai thuốc hoặc ngừng kali-sparing diuretic."
                },
                {
                    "drug": "Kali bổ sung",
                    "mechanism": "Sacubitril-valsartan có thể tăng kali máu, kali bổ sung làm tăng thêm",
                    "effect": "Tăng nguy cơ tăng kali máu nặng",
                    "management": "Thận trọng. CHỐNG CHỈ ĐỊNH dùng kali bổ sung trừ khi được giám sát chặt chẽ và có chỉ định đặc biệt."
                }
            ],
            "moderate": [
                {
                    "drug": "NSAIDs (ibuprofen, naproxen, diclofenac)",
                    "mechanism": "NSAIDs làm giảm tưới máu thận, sacubitril-valsartan cũng ảnh hưởng đến thận",
                    "effect": "Tăng nguy cơ suy thận cấp, tăng creatinine",
                    "management": "Thận trọng. Theo dõi creatinine, eGFR. Tránh dùng lâu dài cùng."
                },
                {
                    "drug": "Lithium",
                    "mechanism": "Sacubitril-valsartan có thể giảm thải trừ lithium",
                    "effect": "Tăng nồng độ lithium, tăng nguy cơ ngộ độc lithium",
                    "management": "Thận trọng. Theo dõi nồng độ lithium. Có thể cần giảm liều lithium."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng sacubitril-valsartan hoặc bất kỳ thành phần nào",
                "Dị ứng với ACE inhibitor hoặc ARB (phù mạch)",
                "Dùng với ACE inhibitor (phải ngừng 36 giờ trước)",
                "Phụ nữ có thai - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI",
                "Bệnh thận đái tháo đường (type 1 hoặc type 2) với protein niệu >300mg/ngày",
                "Suy thận nặng (eGFR <30 mL/min/1.73m²)"
            ],
            "tương_đối": [
                "Suy thận trung bình (eGFR 30-60) - thận trọng, khởi đầu liều thấp (24/26mg x 2 lần/ngày)",
                "Dùng với kali-sparing diuretics - tăng nguy cơ tăng kali máu",
                "Dùng với NSAIDs - tăng nguy cơ suy thận"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI trong thai kỳ. Có thể gây hại hoặc tử vong cho thai nhi. Có thể gây chậm phát triển thai nhi, giảm nước ối, suy thận thai nhi, dị tật bẩm sinh. Phụ nữ trong độ tuổi sinh đẻ phải sử dụng biện pháp tránh thai hiệu quả. Ngừng ngay nếu có thai.",
            "lactation": {
                "safety": "Unknown",
                "details": "Không biết sacubitril-valsartan có bài tiết vào sữa mẹ hay không. Không khuyến cáo dùng khi cho con bú.",
                "recommendation": "Tránh dùng khi cho con bú. Nếu cần, ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, có thể giảm liều (chuyển hóa qua gan)",
            "severe": "Thận trọng, giảm liều 50% (chuyển hóa qua gan)",
            "notes": "Sacubitril-valsartan chuyển hóa qua gan. Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và tác dụng phụ."
        },
        "overdose_management": {
            "symptoms": [
                "Hạ huyết áp nặng",
                "Tăng kali máu",
                "Suy thận cấp",
                "Chóng mặt, ngất",
                "Mệt mỏi nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị hạ huyết áp: Truyền dịch (normal saline), nâng chân, nếu cần: dopamine, norepinephrine",
                "Điều trị tăng kali máu: Calcium gluconate (nếu có ECG changes), Insulin + glucose, Sodium bicarbonate, Kayexalate",
                "Theo dõi creatinine, eGFR",
                "Theo dõi ECG (nếu tăng kali máu)",
                "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "Theo dõi ít nhất 24-48 giờ"
            ],
            "monitoring": "Huyết áp, nhịp tim, ECG, creatinine, eGFR, kali máu, ý thức"
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị hỗ trợ. Điều trị hạ huyết áp và tăng kali máu nếu có."
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Không ảnh hưởng đáng kể đến hấp thu.",
                "timing": "Uống 2 lần/ngày (sáng và tối) vào cùng giờ mỗi ngày. PHẢI ngừng ACE inhibitor 36 giờ trước khi bắt đầu. Khởi đầu với liều thấp (49/51mg x 2 lần/ngày), tăng dần đến liều đích (97/103mg x 2 lần/ngày) sau 2-4 tuần."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Sacubitril-valsartan chỉ có dạng uống (PO)."
            }
        },
        "pediatric_dosing": {
            "neonates": "Không khuyến cáo cho trẻ <18 tuổi (dữ liệu hạn chế)",
            "infants": "Không khuyến cáo cho trẻ <18 tuổi (dữ liệu hạn chế)",
            "children": "Không khuyến cáo cho trẻ <18 tuổi (dữ liệu hạn chế)",
            "adolescents": "Không khuyến cáo cho trẻ <18 tuổi (dữ liệu hạn chế)",
            "notes": "Dữ liệu hạn chế ở trẻ em. Chỉ dùng khi thực sự cần thiết và có chỉ định đặc biệt."
        },
        "geriatric_dosing": {
            "considerations": "Người cao tuổi nhạy cảm hơn với tác dụng phụ (hạ huyết áp, suy thận). Suy gan và suy thận phổ biến hơn",
            "dose_adjustment": "Khởi đầu với liều thấp hơn (24/26mg x 2 lần/ngày nếu eGFR 30-60, hoặc 49/51mg x 2 lần/ngày nếu eGFR >60). Tăng dần chậm hơn. Điều chỉnh theo chức năng thận",
            "monitoring": "Theo dõi huyết áp sát hơn. Theo dõi creatinine, eGFR, kali máu thường xuyên hơn. Cảnh báo về không dùng với ACE inhibitor"
        },
        "brand_names": {
            "vietnam": ["Entresto", "Sacubitril-valsartan"],
            "common": ["Entresto", "Sacubitril-valsartan"]
        },
        "cost_estimate": {
            "unit": "VND",
            "range": "100,000 - 300,000 VND/viên (tùy hàm lượng và thương hiệu)",
            "note": "Giá cao do là thuốc mới và có bằng chứng mạnh. Giá thay đổi theo thương hiệu và nhà thuốc."
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Entresto (sacubitril-valsartan)",
                "UpToDate - Sacubitril-valsartan: Drug information",
                "PARADIGM-HF Study - New England Journal of Medicine (2014) - Sacubitril-valsartan trong suy tim",
                "American Heart Association/American College of Cardiology guidelines - Heart failure (Class I recommendation)"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - Large RCT (PARADIGM-HF) showing significant mortality and hospitalization benefit compared to enalapril in heart failure"
        }
    }

}

__all__ = ['OTHER_CV_DRUGS']
