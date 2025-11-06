"""
Emergency and ACLS Medications
Generated from drug_database_data.py
"""

EMERGENCY_DRUGS = {
"Epinephrine": {
        "group": "Emergency - Catecholamine (Alpha & Beta Agonist)",
        "vietnamese_name": "Epinephrine, Adrenaline",
        "administration": ["IV", "IM", "SC", "INH", "IT"],
        "indications": [
            "Ngừng tim (cardiac arrest)",
            "Sốc phản vệ (anaphylaxis)",
            "Sốc (shock)",
            "Cơn hen nặng (IV/nebulizer)",
            "Co thắt thanh quản"
        ],
        "contraindications": [
            "Không có trong cấp cứu ngừng tim",
            "Sốc phản vệ: không có chống chỉ định tuyệt đối"
        ],
        "dosage": {
            "adult_cardiac_arrest_iv": "1mg IV mỗi 3-5 phút (hoặc 0.1mg/kg)",
            "adult_cardiac_arrest_it": "2-2.5mg IT",
            "adult_anaphylaxis_im": "0.3-0.5mg IM (0.3-0.5ml 1:1000) ở đùi ngoài",
            "adult_anaphylaxis_iv": "0.1-0.25mg IV bolus (pha 1mg trong 10ml = 0.1mg/ml)",
            "adult_shock": "0.1-2mcg/kg/phút IV infusion",
            "pediatric_cardiac_arrest": "0.01mg/kg (0.1ml/kg 1:10000) IV/IT mỗi 3-5 phút",
            "pediatric_anaphylaxis_im": "0.01mg/kg IM (0.01ml/kg 1:1000) ở đùi ngoài (tối đa 0.5mg)",
            "notes": "1:1000 = 1mg/ml (dùng IM/SC), 1:10000 = 0.1mg/ml (dùng IV). Đùi ngoài cho anaphylaxis"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Tim đập nhanh",
            "Tăng huyết áp",
            "Lo lắng, run tay",
            "Đau đầu",
            "Nhồi máu cơ tim (với liều cao)",
            "Rối loạn nhịp tim",
            "Hoại tử (nếu tiêm ngoài mạch)"
        ],
        "interactions": [
            "Beta-blockers: đối kháng tác dụng",
            "MAOIs: tăng tác dụng",
            "Tricyclic antidepressants: tăng tác dụng",
            "Digoxin: tăng nguy cơ loạn nhịp"
        ],
        "pregnancy": "C - An toàn trong cấp cứu",
        "mechanism_of_action": "Non-selective alpha và beta-adrenergic receptor agonist. Kích thích alpha-1 receptors → co mạch ngoại vi, tăng huyết áp. Kích thích beta-1 receptors → tăng nhịp tim, tăng co bóp cơ tim, tăng cung lượng tim. Kích thích beta-2 receptors → giãn phế quản, giãn mạch cơ xương. Trong ngừng tim: tăng áp lực tưới máu vành, tăng khả năng khử rung thành công.",
        "monitoring": [
            "Nhịp tim và huyết áp liên tục",
            "Điện tâm đồ (ECG) - theo dõi rối loạn nhịp",
            "Lactate máu (trong shock)",
            "Đường huyết (tăng đường huyết)",
            "Dấu hiệu thiếu máu cục bộ (đau ngực, thay đổi ST)",
            "Tổn thương mô tại chỗ tiêm (hoại tử nếu tiêm ngoài mạch)"
        ],
        "precautions": [
            "TUYỆT ĐỐI KHÔNG tiêm ngoài mạch (có thể gây hoại tử)",
            "Pha loãng đúng nồng độ: 1:1000 (1mg/ml) cho IM/SC, 1:10000 (0.1mg/ml) cho IV",
            "Trong anaphylaxis: tiêm IM ở đùi ngoài (hấp thu nhanh hơn cánh tay)",
            "Theo dõi sát trong 20 phút đầu (nguy cơ rối loạn nhịp, tăng huyết áp)",
            "Thận trọng ở bệnh nhân bệnh mạch vành (có thể gây nhồi máu cơ tim)",
            "Tránh dùng với thuốc chẹn beta (có thể gây tăng huyết áp nặng do không đối kháng alpha)",
            "Tiêm IV chậm, pha loãng để tránh tăng huyết áp đột ngột"
        ],
        "pharmacokinetics": {
            "half_life": "2-3 phút (rất ngắn)",
            "onset": "IV: ngay lập tức; IM: 5-10 phút",
            "duration": "3-10 phút (IV), 10-30 phút (IM)",
            "protein_binding": "Không đáng kể (catecholamine)",
            "clearance": "Rất nhanh, bị bất hoạt bởi enzyme (MAO và COMT trong gan và mô)"
        },
        "storage": "Bảo quản ở nhiệt độ 2-8°C, tránh ánh sáng, tránh đông lạnh. Kiểm tra màu sắc trước dùng (hóa nâu = hỏng).",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, tiêm ngoài mạch có thể gây hoại tử mô. Liều cao có thể gây nhồi máu cơ tim, đột quỵ, hoặc tử vong."
    },
    "Atropine": {
        "group": "Emergency - Anticholinergic",
        "vietnamese_name": "Atropine",
        "administration": ["IV", "IM", "IO", "IT"],
        "indications": [
            "Nhịp tim chậm có triệu chứng",
            "Block nhĩ thất",
            "Quá liều organophosphate",
            "Chuẩn bị phẫu thuật (giảm tiết)",
            "Ngừng tim với nhịp chậm/PEA"
        ],
        "contraindications": [
            "Glaucoma góc đóng",
            "Tắc nghẽn đường tiểu",
            "Nhịp tim nhanh",
            "Sốt"
        ],
        "dosage": {
            "adult_bradycardia": "0.5-1mg IV mỗi 3-5 phút (tối đa 3mg)",
            "adult_cardiac_arrest": "1mg IV/IT, lặp lại mỗi 3-5 phút",
            "adult_organophosphate": "2-5mg IV, lặp lại đến khi đạt tác dụng",
            "pediatric_bradycardia": "0.02mg/kg IV (tối thiểu 0.1mg, tối đa 0.5mg)",
            "pediatric_cardiac_arrest": "0.02mg/kg IV/IT (tối thiểu 0.1mg)",
            "notes": "Liều tối thiểu người lớn 0.5mg để tránh nhịp tim chậm nghịch lý"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Nhịp tim nhanh",
            "Khô miệng",
            "Giãn đồng tử",
            "Táo bón",
            "Bí tiểu",
            "Lú lẫn (người già)",
            "Tăng nhãn áp"
        ],
        "interactions": [
            "Các anticholinergics khác: tăng tác dụng",
            "Digoxin: có thể tăng nồng độ digoxin"
        ],
        "pregnancy": "C - An toàn",
        "mechanism_of_action": "Anticholinergic (antimuscarinic). Kháng chọn lọc thụ thể muscarinic acetylcholine (M1-M5), ức chế tác dụng của acetylcholine. Tăng nhịp tim (ức chế vagal tone), giảm tiết (nước bọt, mồ hôi, dịch tiêu hóa, phế quản), giãn đồng tử và giảm co thắt cơ trơn (phế quản, ruột, bàng quang). Được dùng trong emergency để điều trị nhịp tim chậm có triệu chứng, block nhĩ thất, và như một chất giải độc trong quá liều organophosphate.",
        "monitoring": [
            "Nhịp tim (ECG monitoring - mục tiêu tăng nhịp tim)",
            "Dấu hiệu kháng cholinergic quá mức: khô miệng nặng, giãn đồng tử, bí tiểu, lú lẫn",
            "Nhãn áp (nếu có nguy cơ glaucoma)",
            "Triệu chứng nhịp tim chậm nghịch lý (paradoxical bradycardia) - có thể xảy ra với liều <0.5mg ở người lớn",
            "Phản ứng quá mức (nhịp tim nhanh, đánh trống ngực)"
        ],
        "precautions": [
            "QUAN TRỌNG: Liều tối thiểu người lớn 0.5mg để tránh nhịp tim chậm nghịch lý (liều thấp có thể kích thích trung tâm vagal)",
            "CHỐNG CHỈ ĐỊNH tuyệt đối: Glaucoma góc đóng (có thể gây tăng nhãn áp đe dọa thị giác)",
            "CHỐNG CHỈ ĐỊNH: Tắc nghẽn đường tiểu (có thể làm nặng thêm bí tiểu)",
            "CHỐNG CHỈ ĐỊNH: Nhịp tim nhanh (có thể làm tăng nhịp tim hơn nữa)",
            "Thận trọng ở người già (tăng nguy cơ lú lẫn, bí tiểu)",
            "Thận trọng ở bệnh nhân sốt (có thể làm tăng nhiệt độ do giảm tiết mồ hôi)",
            "Thận trọng khi dùng với các anticholinergics khác (tăng tác dụng phụ)",
            "Trong quá liều organophosphate: dùng liều cao hơn nhiều (2-5mg), có thể cần lặp lại nhiều lần cho đến khi đạt tác dụng (đồng tử co lại, giảm tiết)"
        ],
        "pharmacokinetics": {
            "half_life": "2-4 giờ (người lớn), 10-20 giờ (trẻ em)",
            "onset": "Vài phút (IV), 15-30 phút (IM)",
            "duration": "4-6 giờ (tác dụng lâm sàng)",
            "protein_binding": "50%",
            "clearance": "Thận (50-90% thải qua nước tiểu dưới dạng không đổi), gan (metabolite). Thời gian bán hủy dài hơn ở trẻ em"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Dung dịch tiêm: bảo quản trong tủ mát (2-8°C) nếu có chỉ định, nhưng thường ổn định ở nhiệt độ phòng",
        "black_box_warnings": None
    },
    "Lidocaine": {
        "group": "Emergency - Local Anesthetic / Antiarrhythmic (Class IB)",
        "vietnamese_name": "Lidocaine, Xylocaine",
        "administration": ["IV", "IO", "IT"],
        "indications": [
            "Rung thất / Nhịp nhanh thất không có mạch (khi không có amiodarone)",
            "Rối loạn nhịp thất",
            "Gây tê tại chỗ",
            "Gây tê vùng"
        ],
        "contraindications": [
            "Dị ứng lidocaine",
            "Block nhĩ thất độ 2-3 (không có máy tạo nhịp)",
            "Hội chứng Adams-Stokes",
            "Rối loạn nhịp nặng"
        ],
        "dosage": {
            "adult_cardiac_arrest": "1-1.5mg/kg IV bolus, lặp lại 0.5-0.75mg/kg mỗi 5-10 phút (tối đa 3mg/kg)",
            "adult_vt_with_pulse": "1-1.5mg/kg IV bolus, sau đó 1-4mg/phút IV infusion",
            "pediatric_arrest": "1mg/kg IV/IO bolus",
            "pediatric_infusion": "20-50mcg/kg/phút IV",
            "notes": "Giảm liều ở suy tim, suy gan, người già. Theo dõi co giật, độc thần kinh"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Độc thần kinh trung ương (co giật, lú lẫn, ngừng thở - với liều cao)",
            "Rối loạn nhịp tim",
            "Hạ huyết áp",
            "Phản ứng dị ứng (hiếm)"
        ],
        "interactions": [
            "Beta-blockers: giảm chuyển hóa lidocaine",
            "Cimetidine: tăng nồng độ lidocaine",
            "Phenytoin: tăng độc tính"
        ],
        "pregnancy": "B - An toàn",
        "mechanism_of_action": "Thuốc gây tê tại chỗ nhóm amide và thuốc chống loạn nhịp class IB. Ức chế kênh natri voltage-gated trong màng tế bào thần kinh và tế bào cơ tim, ngăn cản khử cực và dẫn truyền xung động thần kinh. Ở tim: ức chế dẫn truyền trong các tế bào có thời gian khử cực dài (tâm thất), giảm tự động tính, giảm nguy cơ rối loạn nhịp thất. Tác dụng nhanh, thời gian bán thải ngắn. Được dùng trong gây tê tại chỗ, giảm đau tại chỗ, và điều trị rối loạn nhịp thất.",
        "monitoring": [
            "ECG liên tục (theo dõi rối loạn nhịp)",
            "Huyết áp và nhịp tim",
            "Dấu hiệu độc tính thần kinh trung ương (chóng mặt, ù tai, co giật, mất ý thức) - dấu hiệu đầu tiên của quá liều",
            "Dấu hiệu độc tính tim mạch (block nhĩ thất, nhịp tim chậm, rung thất) - dấu hiệu muộn, nguy hiểm",
            "Nồng độ lidocaine trong máu (nếu dùng kéo dài hoặc liều cao)",
            "Chức năng gan (lidocaine chuyển hóa mạnh ở gan)",
            "Dấu hiệu phản ứng dị ứng (hiếm)"
        ],
        "precautions": [
            "Độc tính thần kinh trung ương là dấu hiệu CẢNH BÁO SỚM - ngừng ngay nếu có chóng mặt, ù tai, co giật",
            "Độc tính tim mạch có thể xảy ra sau độc tính thần kinh - nguy hiểm tính mạng",
            "PHẢI điều chỉnh liều ở suy gan (giảm chuyển hóa → tích lũy → độc tính)",
            "Thận trọng ở suy tim (giảm phân bố → tăng nồng độ)",
            "Không dùng ở block nhĩ thất độ 2-3 hoặc block nhánh nếu không có máy tạo nhịp",
            "Liều gây tê tại chỗ: tuân thủ liều tối đa (không quá 4.5mg/kg không có epinephrine, 7mg/kg có epinephrine)",
            "Tiêm IV chậm (không quá 25-50mg/phút) để tránh độc tính",
            "Cần có sẵn thuốc chống co giật (benzodiazepine) và thiết bị hồi sức",
            "Giảm liều ở người cao tuổi (giảm chuyển hóa)"
        ],
        "pharmacokinetics": {
            "half_life": "1.5-2 giờ (bình thường), 3-5 giờ (suy gan)",
            "onset": "Ngay lập tức (IV), 2-5 phút (gây tê tại chỗ)",
            "duration": "10-20 phút (IV), 1-3 giờ (gây tê tại chỗ)",
            "protein_binding": "60-80%",
            "metabolism": "Gan (CYP3A4, CYP1A2) - chuyển hóa mạnh thành active metabolites",
            "clearance": "Chủ yếu qua gan, cần điều chỉnh ở suy gan"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Dung dịch: tránh đông lạnh.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, độc tính tim mạch có thể gây block nhĩ thất, rung thất, và tử vong, đặc biệt ở suy gan hoặc quá liều. Độc tính thần kinh trung ương (co giật) là dấu hiệu cảnh báo sớm."
    },
    "Adenosine": {
        "group": "Emergency - Antiarrhythmic",
        "vietnamese_name": "Adenosine",
        "administration": ["IV", "IO"],
        "indications": [
            "Nhịp nhanh trên thất (SVT) - cấp cứu",
            "Chẩn đoán rối loạn nhịp",
            "Cuồng nhĩ"
        ],
        "contraindications": [
            "Block nhĩ thất độ 2-3 (không có máy tạo nhịp)",
            "Hội chứng sick sinus",
            "Hen phế quản nặng",
            "Dị ứng adenosine"
        ],
        "dosage": {
            "adult_svt_first": "6mg IV bolus nhanh (1-2 giây) + flush nhanh 20ml NS",
            "adult_svt_second": "12mg IV nếu không đáp ứng (có thể lặp lại 1 lần)",
            "adult_max": "12mg (tối đa)",
            "pediatric_svt_first": "0.1mg/kg IV (tối đa 6mg)",
            "pediatric_svt_second": "0.2mg/kg IV nếu không đáp ứng (tối đa 12mg)",
            "notes": "Phải tiêm bolus nhanh (1-2 giây) và flush ngay 20ml. Có thể gây ngừng tim tạm thời"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Ngừng tim tạm thời (thường <10 giây - bình thường)",
            "Cảm giác khó chịu ở ngực",
            "Khó thở",
            "Đỏ mặt",
            "Chóng mặt",
            "Loạn nhịp (thoáng qua)"
        ],
        "interactions": [
            "Theophylline/Caffeine: đối kháng tác dụng",
            "Dipyridamole: tăng tác dụng",
            "Carbamazepine: tăng tác dụng"
        ],
        "pregnancy": "C - An toàn",
        "mechanism_of_action": "Adenosine là một nucleoside nội sinh kích hoạt các thụ thể A1 adenosine ở nút nhĩ-thất (AV node), làm tăng thời gian dẫn truyền và kéo dài thời gian refrac của nút AV. Tác dụng này chặn tạm thời dẫn truyền qua nút AV, phá vỡ vòng re-entry trong SVT và chuyển nhịp về xoang. Có thời gian bán thải cực ngắn (<10 giây) do bị bắt giữ nhanh bởi tế bào hồng cầu và nội mô, nên tác dụng thoáng qua và an toàn",
        "monitoring": [
            "ECG liên tục trong và sau khi tiêm (ngừng tim tạm thời có thể xảy ra)",
            "Nhịp tim, huyết áp trong và sau khi tiêm (1-2 phút)",
            "Dấu hiệu sốc phản vệ (hiếm nhưng nguy hiểm)",
            "Dấu hiệu co thắt phế quản (đặc biệt ở bệnh nhân hen)",
            "Đáp ứng điều trị (chuyển về nhịp xoang)"
        ],
        "precautions": [
            "PHẢI tiêm bolus nhanh (1-2 giây) và flush ngay 20ml NS để đảm bảo thuốc vào tim trước khi bị bắt giữ",
            "Nếu tiêm chậm → thuốc bị bắt giữ bởi tế bào máu → không hiệu quả",
            "Chuẩn bị sẵn thiết bị hồi sức tim phổi (CPR, defibrillator) vì có thể gây ngừng tim tạm thời",
            "Tránh dùng ở bệnh nhân hen phế quản nặng (có thể gây co thắt phế quản)",
            "Tránh dùng ở block AV độ 2-3 hoặc sick sinus syndrome (trừ khi có máy tạo nhịp)",
            "Có thể gây ngừng tim tạm thời <10 giây (bình thường, không cần điều trị)",
            "Nếu không đáp ứng với 6mg, có thể tăng lên 12mg (tối đa)",
            "Tránh dùng với theophylline hoặc caffeine (đối kháng tác dụng)"
        ],
        "pharmacokinetics": {
            "half_life": "<10 giây (cực ngắn)",
            "onset": "Ngay lập tức (vài giây)",
            "duration": "10-30 giây (tạm thời)",
            "protein_binding": "Không đáng kể",
            "clearance": "Bắt giữ nhanh bởi tế bào hồng cầu và nội mô, chuyển hóa thành inosine và adenosine monophosphate"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh đông lạnh. Bảo vệ khỏi ánh sáng",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "Theophylline, Caffeine",
                    "mechanism": "Theophylline và caffeine là chất đối kháng adenosine receptor, ức chế tác dụng của adenosine.",
                    "effect": "Giảm hoặc mất hiệu quả điều trị SVT, có thể cần liều cao hơn hoặc không đáp ứng",
                    "management": "Tránh dùng adenosine nếu bệnh nhân đang dùng theophylline hoặc uống caffeine gần đây. Nếu cần, có thể cần liều cao hơn (12mg) hoặc dùng phương pháp khác (adenosine không hiệu quả)."
                },
                {
                    "drug": "Dipyridamole",
                    "mechanism": "Dipyridamole ức chế bắt giữ adenosine bởi tế bào, tăng nồng độ và thời gian tác dụng của adenosine.",
                    "effect": "Tăng tác dụng và thời gian tác dụng của adenosine, tăng nguy cơ tác dụng phụ (ngừng tim kéo dài, block AV)",
                    "management": "GIẢM LIỀU adenosine xuống 50-75% (1.5-3mg thay vì 6mg). Theo dõi chặt chẽ ECG. Chuẩn bị sẵn thiết bị hồi sức."
                }
            ],
            "moderate": [
                {
                    "drug": "Carbamazepine",
                    "mechanism": "Carbamazepine có thể tăng tác dụng của adenosine (cơ chế không rõ ràng, có thể liên quan đến bắt giữ adenosine).",
                    "effect": "Tăng tác dụng và thời gian tác dụng của adenosine, tăng nguy cơ tác dụng phụ",
                    "management": "Thận trọng, có thể cần giảm liều adenosine. Theo dõi chặt chẽ ECG."
                },
                {
                    "drug": "Digoxin",
                    "mechanism": "Digoxin có thể tăng độ nhạy cảm của nút AV với adenosine.",
                    "effect": "Tăng nguy cơ block AV, ngừng tim kéo dài",
                    "management": "Thận trọng, theo dõi ECG chặt chẽ. Có thể cần giảm liều adenosine."
                }
            ],
            "minor": [
                {
                    "drug": "Beta-blockers",
                    "mechanism": "Beta-blockers có thể tăng độ nhạy cảm của nút AV với adenosine.",
                    "effect": "Tăng nguy cơ block AV (nhẹ)",
                    "management": "Theo dõi ECG. Không cần điều chỉnh liều thường quy."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Block nhĩ thất độ 2-3 (AV block) không có máy tạo nhịp",
                "Hội chứng sick sinus (sick sinus syndrome) không có máy tạo nhịp",
                "Hen phế quản nặng hoặc co thắt phế quản nặng",
                "Dị ứng adenosine",
                "Rung nhĩ/rung thất (không phải chỉ định)"
            ],
            "relative": [
                "Block AV độ 1 - thận trọng, có thể làm nặng",
                "Hen phế quản nhẹ đến trung bình - thận trọng, có thể gây co thắt phế quản",
                "Suy tim - thận trọng, có thể gây ngừng tim kéo dài",
                "Suy thận nặng - không cần điều chỉnh liều nhưng thận trọng",
                "Dùng với dipyridamole - giảm liều 50-75%",
                "Dùng với theophylline/caffeine - có thể không hiệu quả",
                "Nhịp tim chậm (<50 bpm) - thận trọng, có thể gây ngừng tim"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Adenosine là thuốc phân loại C. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Adenosine có thời gian bán thải cực ngắn (<10 giây) và tác dụng thoáng qua, nên ít có khả năng ảnh hưởng đến thai nhi. Được sử dụng trong cấp cứu để điều trị SVT ở phụ nữ có thai và có vẻ an toàn. SVT có thể gây nguy hiểm cho cả mẹ và thai nhi (giảm tưới máu, thiếu oxy). Adenosine có thể được dùng khi lợi ích vượt quá nguy cơ, đặc biệt trong cấp cứu.",
            "lactation": {
                "safety": "Compatible",
                "details": "Adenosine có thời gian bán thải cực ngắn (<10 giây), nên không có khả năng bài tiết vào sữa mẹ ở nồng độ đáng kể. Tác dụng thoáng qua và bị bắt giữ nhanh bởi tế bào. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Adenosine có tác dụng cực ngắn và không bài tiết vào sữa mẹ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Adenosine không chuyển hóa qua gan, bị bắt giữ bởi tế bào máu.",
            "moderate": "Không cần điều chỉnh liều.",
            "severe": "Không cần điều chỉnh liều. Adenosine không chuyển hóa qua gan.",
            "notes": "Adenosine không chuyển hóa qua gan, bị bắt giữ nhanh bởi tế bào hồng cầu và nội mô, chuyển hóa thành inosine. Không cần điều chỉnh liều ở bệnh nhân suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Ngừng tim tạm thời kéo dài (>10-30 giây) - có thể tiến triển thành ngừng tim thực sự",
                "Block AV độ 2-3 kéo dài - có thể gây nhịp chậm nặng, suy tim",
                "Rung nhĩ/rung thất - hiếm nhưng nguy hiểm",
                "Co thắt phế quản nặng - khó thở, suy hô hấp",
                "Sốc phản vệ - phát ban, phù mạch, sốc (hiếm)",
                "Tụt huyết áp nặng",
                "Nhịp chậm nặng (<30-40 bpm)"
            ],
            "antidote": "Không có antidote đặc hiệu. Theophylline hoặc aminophylline có thể đối kháng tác dụng adenosine (nếu có block AV kéo dài).",
            "treatment": [
                "Ngừng ngay adenosine nếu đang truyền (nếu có)",
                "Hỗ trợ hô hấp: Thở oxy, nếu cần hỗ trợ thông khí cơ học",
                "Theo dõi ECG liên tục: Nhịp tim, block AV, loạn nhịp",
                "Nếu ngừng tim tạm thời <10 giây: Quan sát, thường tự hồi phục",
                "Nếu ngừng tim kéo dài >10-30 giây hoặc block AV độ 2-3:",
                "  - Hỗ trợ hô hấp, thở oxy",
                "  - Nếu nhịp chậm nặng: Atropine 0.5-1mg IV (nếu không có block AV)",
                "  - Nếu block AV kéo dài: Theophylline 100-200mg IV hoặc aminophylline (đối kháng adenosine)",
                "  - Nếu ngừng tim thực sự: CPR, defibrillation nếu cần",
                "Nếu co thắt phế quản: Salbutamol dạng hít hoặc IV, corticosteroid nếu cần",
                "Nếu sốc phản vệ: Epinephrine, diphenhydramine, corticosteroid",
                "Hỗ trợ huyết động: Truyền dịch, thuốc vận mạch nếu cần",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2 trong ít nhất 30-60 phút"
            ],
            "monitoring": "Theo dõi ECG liên tục, dấu hiệu sinh tồn trong ít nhất 30-60 phút sau khi dùng. Theo dõi lâu hơn nếu có biến chứng (block AV, ngừng tim, co thắt phế quản)."
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "agent": "Theophylline / Aminophylline",
                    "mechanism": "Đối kháng adenosine receptors, đảo ngược tác dụng block AV của adenosine",
                    "indication": "Block AV kéo dài sau khi dùng adenosine",
                    "dose": "Theophylline 100-200mg IV hoặc Aminophylline 5-6mg/kg IV"
                }
            ]
        },
        "administration_instructions": {
            "oral": None,
            "iv": {
                "reconstitution": "Dùng trực tiếp từ lọ, không cần pha. Có thể pha trong NS nếu cần nhưng thường dùng trực tiếp.",
                "infusion_rate": "BOLUS NHANH: Tiêm trực tiếp vào tĩnh mạch lớn (tĩnh mạch ngoại biên lớn hoặc tĩnh mạch trung tâm) trong 1-2 giây. SAU ĐÓ NGAY LẬP TỨC flush 20ml NS nhanh để đẩy thuốc vào tim trước khi bị bắt giữ bởi tế bào máu. KHÔNG được tiêm chậm hoặc truyền - sẽ không hiệu quả.",
                "compatibility": ["NS (0.9% NaCl) - để flush"],
                "incompatibility": ["Không trộn với các thuốc khác. Tiêm bolus riêng biệt."],
                "notes": "QUAN TRỌNG: 1) Tiêm bolus NHANH (1-2 giây) vào tĩnh mạch lớn, 2) Flush NGAY 20ml NS nhanh, 3) Theo dõi ECG liên tục, 4) Chuẩn bị sẵn thiết bị hồi sức. Nếu tiêm chậm → thuốc bị bắt giữ → không hiệu quả. Liều đầu: 6mg, nếu không đáp ứng: 12mg (tối đa)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Adenosine",
                "ACLS Guidelines 2020 - American Heart Association",
                "UpToDate - Adenosine: Drug Information",
                "Medscape - Adenosine Drug Reference",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
                "Lexicomp Online - Adenosine Monograph",
                "Micromedex - Adenosine Drug Information"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "A - Dựa trên FDA drug labels, ACLS guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },
    "Naloxone": {
        "group": "Emergency - Opioid Antagonist",
        "vietnamese_name": "Naloxone, Narcan",
        "administration": ["IV", "IM", "SC", "INH", "IO"],
        "indications": [
            "Quá liều opioid (nghiện)",
            "Ngộ độc opioid",
            "Đảo ngược tác dụng opioid sau phẫu thuật",
            "Đảo ngược tác dụng opioid trong ICU"
        ],
        "contraindications": [
            "Dị ứng naloxone"
        ],
        "dosage": {
            "adult_overdose": "0.4-2mg IV/IM/SC, lặp lại mỗi 2-3 phút đến khi đáp ứng",
            "adult_reversal": "0.04-0.4mg IV titrate đến khi đáp ứng",
            "adult_infusion": "0.25-6.25mcg/kg/giờ IV (nếu cần duy trì)",
            "pediatric_overdose": "0.01mg/kg IV/IM/IO, lặp lại đến khi đáp ứng",
            "pediatric_infusion": "2.5-10mcg/kg/giờ IV",
            "notes": "Tác dụng ngắn (20-90 phút), có thể cần lặp lại hoặc infusion. Theo dõi hội chứng cai"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Hội chứng cai opioid (nếu bệnh nhân nghiện)",
            "Hạ huyết áp",
            "Rối loạn nhịp tim",
            "Co giật (hiếm)",
            "Phù phổi (hiếm)"
        ],
        "interactions": [
            "Opioids: đảo ngược tác dụng"
        ],
        "pregnancy": "C - An toàn",
        "mechanism_of_action": "Opioid receptor antagonist cạnh tranh. Gắn với ái lực cao vào mu-opioid receptor (và kappa, delta receptors), đẩy opioid ra khỏi receptor, đảo ngược hoàn toàn tác dụng của opioid (ức chế hô hấp, an thần, giảm đau, miosis). Tác dụng rất nhanh (1-2 phút IV), nhưng thời gian tác dụng ngắn (30-90 phút) do bị chuyển hóa nhanh, trong khi nhiều opioid có thời gian tác dụng dài hơn → cần lặp lại liều hoặc dùng infusion.",
        "monitoring": [
            "Độ bão hòa oxy (SpO2) và nhịp thở liên tục",
            "Mức độ ý thức (GCS)",
            "Dấu hiệu hội chứng cai opioid (kích động, vã mồ hôi, tăng huyết áp, nhịp tim nhanh)",
            "Huyết áp và nhịp tim",
            "Dấu hiệu tái ngộ độc opioid (thở chậm lại, giảm ý thức) - đặc biệt quan trọng nếu opioid có thời gian tác dụng dài hơn naloxone",
            "Co giật (hiếm nhưng nguy hiểm)"
        ],
        "precautions": [
            "Thời gian tác dụng NGẮN (30-90 phút) - opioid có thể tác dụng trở lại sau khi naloxone hết tác dụng",
            "Theo dõi sát ít nhất 2-4 giờ sau khi dùng naloxone (nguy cơ tái ngộ độc)",
            "Ở bệnh nhân nghiện opioid: naloxone có thể gây hội chứng cai nặng (kích động, nôn, tăng huyết áp) - cần chuẩn bị xử trí",
            "Không dùng quá liều (tăng nguy cơ hội chứng cai nặng, không tăng hiệu quả)",
            "Nếu cần duy trì: dùng infusion thay vì bolus lặp lại",
            "Thận trọng ở bệnh nhân có tiền sử co giật (có thể gây co giật)",
            "Dùng liều thấp (0.04-0.4mg) khi đảo ngược tác dụng opioid sau phẫu thuật để tránh đảo ngược hoàn toàn giảm đau"
        ],
        "pharmacokinetics": {
            "half_life": "30-90 phút (ngắn)",
            "onset": "1-2 phút (IV), 2-5 phút (IM)",
            "duration": "30-90 phút (tùy liều)",
            "protein_binding": "45%",
            "clearance": "Gan (glucuronidation), thời gian bán thải ngắn hơn nhiều so với hầu hết opioid"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Có thể bảo quản ở nhiệt độ 2-8°C.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, thời gian tác dụng ngắn có thể dẫn đến tái ngộ độc opioid nếu không theo dõi đúng. Hội chứng cai opioid có thể nguy hiểm ở bệnh nhân nghiện."
    },
    "Flumazenil": {
        "group": "Emergency - Benzodiazepine Antagonist",
        "vietnamese_name": "Flumazenil, Anexate",
        "administration": ["IV"],
        "indications": [
            "Quá liều benzodiazepine",
            "Đảo ngược tác dụng benzodiazepine sau phẫu thuật",
            "Quá liều zolpidem/zopiclone"
        ],
        "contraindications": [
            "Dị ứng flumazenil",
            "Động kinh (đang điều trị với benzodiazepine)",
            "Quá liều tricyclic antidepressants",
            "Phụ thuộc benzodiazepine lâu dài"
        ],
        "dosage": {
            "adult_overdose": "0.2mg IV, lặp lại 0.2mg mỗi 1 phút đến khi đáp ứng (tối đa 1mg)",
            "adult_reversal": "0.1-0.2mg IV titrate đến khi đáp ứng",
            "pediatric": "0.01mg/kg IV (tối đa 0.2mg), lặp lại đến khi đáp ứng",
            "notes": "Tác dụng ngắn (30-60 phút), có thể cần lặp lại. Nguy cơ co giật ở bệnh nhân động kinh"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Co giật (nguy hiểm ở bệnh nhân động kinh)",
            "Hội chứng cai benzodiazepine",
            "Buồn nôn, nôn",
            "Chóng mặt",
            "Lo lắng",
            "Rối loạn nhịp tim"
        ],
        "interactions": [
            "Benzodiazepines: đảo ngược tác dụng",
            "Tricyclic antidepressants: tăng nguy cơ co giật"
        ],
        "pregnancy": "C - Thận trọng",
        "mechanism_of_action": "Benzodiazepine receptor antagonist cạnh tranh. Gắn với ái lực cao vào benzodiazepine receptor (một phần của GABA-A receptor complex), đẩy benzodiazepine ra khỏi receptor, đảo ngược tác dụng của benzodiazepine (an thần, ức chế hô hấp, giảm trương lực cơ, mất trí nhớ). Tác dụng rất nhanh (1-2 phút IV), nhưng thời gian tác dụng ngắn (45-90 phút) do bị chuyển hóa nhanh, trong khi nhiều benzodiazepine có thời gian tác dụng dài hơn → cần theo dõi sát, có thể cần lặp lại liều.",
        "monitoring": [
            "Mức độ ý thức (GCS) liên tục",
            "Nhịp thở và độ bão hòa oxy (SpO2)",
            "Dấu hiệu tái an thần/tái ức chế hô hấp (quan trọng - flumazenil hết tác dụng trước benzodiazepine)",
            "Dấu hiệu hội chứng cai benzodiazepine (kích động, run, co giật) - đặc biệt ở bệnh nhân nghiện",
            "Huyết áp và nhịp tim",
            "Co giật (nguy cơ ở bệnh nhân có tiền sử co giật, dùng benzodiazepine để chống co giật)",
            "Rối loạn nhịp tim (hiếm)"
        ],
        "precautions": [
            "Thời gian tác dụng NGẮN (45-90 phút) - benzodiazepine có thể tác dụng trở lại sau khi flumazenil hết",
            "Theo dõi sát ít nhất 2-4 giờ sau khi dùng (nguy cơ tái an thần, tái ức chế hô hấp)",
            "Ở bệnh nhân nghiện benzodiazepine: có thể gây hội chứng cai nặng (kích động, run, co giật) - cần chuẩn bị xử trí",
            "KHÔNG dùng ở bệnh nhân dùng benzodiazepine để chống co giật (có thể gây co giật nặng)",
            "KHÔNG dùng ở ngộ độc tricyclic antidepressant (có thể gây co giật, rối loạn nhịp)",
            "Khởi đầu với liều thấp (0.2mg), tăng dần nếu cần",
            "Không dùng quá liều (không tăng hiệu quả, tăng nguy cơ tác dụng phụ)",
            "Nếu cần duy trì: có thể dùng infusion, nhưng thường không khuyến cáo",
            "Thận trọng ở bệnh nhân có tiền sử co giật"
        ],
        "pharmacokinetics": {
            "half_life": "41-79 phút (ngắn)",
            "onset": "1-2 phút (IV)",
            "duration": "45-90 phút (tùy liều)",
            "protein_binding": "50%",
            "metabolism": "Gan (glucuronidation)",
            "clearance": "Gan, thời gian bán thải ngắn hơn nhiều so với hầu hết benzodiazepine"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Sau khi pha: bảo quản ở nhiệt độ phòng 24 giờ.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, thời gian tác dụng ngắn có thể dẫn đến tái an thần và tái ức chế hô hấp nếu không theo dõi đúng. Hội chứng cai benzodiazepine có thể nguy hiểm ở bệnh nhân nghiện. Nguy cơ co giật ở bệnh nhân có tiền sử co giật hoặc ngộ độc tricyclic antidepressant."
    },
}

__all__ = ['EMERGENCY_DRUGS']
