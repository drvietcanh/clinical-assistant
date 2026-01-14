"""Oncology Medications
Active module - contains all oncology drug data"""

# Topoisomerase Inhibitors

TOPOISOMERASE_INHIBITORS_DRUGS = {
    "Etoposide": {
        "group": "Oncology - Topoisomerase II Inhibitor",
        "vietnamese_name": "Etoposide, VP-16, Etopophos",
        "administration": ["IV", "PO"],
        "indications": [
            "Ung thư tế bào nhỏ phổi (small cell lung cancer - SCLC)",
            "Ung thư tinh hoàn (testicular cancer)",
            "U lympho (lymphoma)",
            "Bệnh bạch cầu cấp (acute leukemia)",
            "Ung thư buồng trứng",
            "Sarcoma mô mềm"
        ],
        "contraindications": [
            "Dị ứng etoposide hoặc bất kỳ thành phần nào",
            "Giảm bạch cầu nặng (ANC <1000)",
            "Giảm tiểu cầu nặng (<50,000)",
            "Có thai",
            "Đang cho con bú"
        ],
        "dosage": {
            "adult_iv_standard": "100-120mg/m² IV ngày 1-3 (mỗi 3-4 tuần)",
            "adult_iv_high": "500mg/m² IV ngày 1, 3, 5 (mỗi 3-4 tuần)",
            "adult_po": "50mg/m² PO x 21 ngày (mỗi 28 ngày) hoặc 100mg/m² PO ngày 1-5 (mỗi 3-4 tuần)",
            "notes": "Truyền IV trong 30-60 phút. Etoposide có cả dạng IV và PO. Dạng PO có sinh khả dụng thấp (50%), cần liều cao hơn."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25%",
            "under_30": "Giảm liều 50%"
        },
        "side_effects": [
            "Giảm bạch cầu, tiểu cầu (myelosuppression - RẤT PHỔ BIẾN, nặng)",
            "Thiếu máu - phổ biến",
            "Buồn nôn, nôn - phổ biến",
            "Rụng tóc - phổ biến",
            "Mệt mỏi - phổ biến",
            "Độc gan (tăng transaminase) - hiếm",
            "Ung thư thứ phát (acute myeloid leukemia - AML) - hiếm nhưng nghiêm trọng, với liều cao",
            "Phản ứng quá mẫn (hypersensitivity) - hiếm"
        ],
        "interactions": [
            "Cisplatin: tăng độc tính tủy xương",
            "Warfarin: tăng nguy cơ chảy máu",
            "CYP3A4 inhibitors: tăng nồng độ etoposide",
            "CYP3A4 inducers: giảm nồng độ etoposide"
        ],
        "pregnancy": "D - Chống chỉ định",
        "mechanism_of_action": "Etoposide là topoisomerase II inhibitor (epipodophyllotoxin derivative). Topoisomerase II là enzyme quan trọng để tháo xoắn DNA trong quá trình sao chép và phân chia tế bào. Etoposide gắn với topoisomerase II-DNA complex → ức chế enzyme → ngăn cản quá trình sửa chữa DNA sau khi tháo xoắn → gây đứt gãy DNA và chết tế bào. Etoposide tác động chủ yếu lên tế bào đang phân chia nhanh (ung thư), gây độc tế bào. Khác với topoisomerase I inhibitors (irinotecan, topotecan), etoposide ức chế topoisomerase II. Hiệu quả với ung thư tế bào nhỏ phổi, tinh hoàn, u lympho. Độc tính chính: myelosuppression (RẤT PHỔ BIẾN, nặng).",
        "monitoring": [
            "Công thức máu toàn phần (CBC) trước mỗi chu kỳ và giữa các chu kỳ - QUAN TRỌNG (myelosuppression RẤT PHỔ BIẾN, nặng)",
            "Dấu hiệu nhiễm trùng (sốt, ớn lạnh) do giảm bạch cầu",
            "Dấu hiệu chảy máu (do giảm tiểu cầu)",
            "Chức năng gan (ALT, AST, bilirubin) trước và trong điều trị (độc gan hiếm)",
            "Dấu hiệu phản ứng quá mẫn (hypersensitivity) - hiếm",
            "Dấu hiệu ung thư thứ phát (AML) - hiếm nhưng nghiêm trọng, với liều cao"
        ],
        "precautions": [
            "MYELOSUPPRESSION - RẤT PHỔ BIẾN, NẶNG - theo dõi CBC chặt chẽ trước mỗi chu kỳ",
            "Trì hoãn điều trị nếu giảm bạch cầu nặng (ANC <1000) hoặc giảm tiểu cầu nặng (<50,000)",
            "Có thể cần hỗ trợ G-CSF hoặc truyền máu/tiểu cầu",
            "Tương tác với cisplatin (tăng độc tính tủy xương)",
            "Tương tác với warfarin (tăng nguy cơ chảy máu - theo dõi INR)",
            "Tương tác với CYP3A4 inhibitors/inducers (ảnh hưởng nồng độ etoposide)",
            "Nguy cơ ung thư thứ phát (AML) - hiếm nhưng nghiêm trọng, với liều cao",
            "Dạng PO: sinh khả dụng thấp (50%), cần liều cao hơn dạng IV"
        ],
        "pharmacokinetics": {
            "half_life": "4-11 giờ",
            "onset": "1-2 tuần (tác dụng lâm sàng)",
            "duration": "24-48 giờ (tác dụng sinh học)",
            "protein_binding": "97%",
            "metabolism": "Gan (CYP3A4, glucuronidation)",
            "clearance": "Gan (chủ yếu), thận (một phần)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Bảo quản ở tủ lạnh (2-8°C) nếu yêu cầu. Pha với NS hoặc D5W.",
        "black_box_warnings": "MYELOSUPPRESSION (giảm bạch cầu, tiểu cầu, thiếu máu) RẤT PHỔ BIẾN VÀ NẶNG. Theo dõi CBC trước mỗi chu kỳ. Trì hoãn điều trị nếu giảm bạch cầu nặng (ANC <1000) hoặc giảm tiểu cầu nặng (<50,000). Nguy cơ ung thư thứ phát (acute myeloid leukemia - AML) - hiếm nhưng nghiêm trọng, với liều cao.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Cisplatin, Carboplatin",
                    "mechanism": "Cả hai đều gây myelosuppression, tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ giảm bạch cầu, tiểu cầu nghiêm trọng",
                    "management": "Theo dõi CBC chặt chẽ. Có thể cần giảm liều hoặc trì hoãn điều trị."
                }
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Etoposide có thể tăng tác dụng chống đông",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Thận trọng. Theo dõi INR chặt chẽ. Có thể cần giảm liều warfarin."
                },
                {
                    "drug": "CYP3A4 Inhibitors (Ketoconazole, Itraconazole, Ritonavir)",
                    "mechanism": "Ức chế CYP3A4, tăng nồng độ etoposide",
                    "effect": "Tăng nồng độ etoposide, tăng độc tính",
                    "management": "Thận trọng. Có thể cần giảm liều etoposide."
                },
                {
                    "drug": "CYP3A4 Inducers (Rifampin, Carbamazepine, Phenytoin)",
                    "mechanism": "Cảm ứng CYP3A4, giảm nồng độ etoposide",
                    "effect": "Giảm nồng độ etoposide, giảm hiệu quả",
                    "management": "Thận trọng. Có thể cần tăng liều etoposide."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng etoposide hoặc bất kỳ thành phần nào",
                "Có thai - CHỐNG CHỈ ĐỊNH (category D)",
                "Đang cho con bú - CHỐNG CHỈ ĐỊNH",
                "Giảm bạch cầu nặng (ANC <1000) - trì hoãn điều trị",
                "Giảm tiểu cầu nặng (<50,000) - trì hoãn điều trị"
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - giảm liều 50%",
                "Suy gan nặng - thận trọng (chuyển hóa qua gan)",
                "Bệnh nhân cao tuổi - tăng nguy cơ độc tính"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Etoposide phân loại D - chống chỉ định trong thai kỳ. Etoposide gây dị tật thai nhi, sẩy thai, và tử vong thai nhi. Không dùng trong thai kỳ trừ khi lợi ích vượt trội rõ ràng so với nguy cơ.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Etoposide bài tiết vào sữa mẹ. Thuốc có thể gây độc tính nghiêm trọng cho trẻ sơ sinh.",
                "recommendation": "Không cho con bú khi dùng etoposide. Ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, có thể cần giảm liều",
            "severe": "Thận trọng, giảm liều 25-50%",
            "notes": "Etoposide chuyển hóa qua gan (CYP3A4, glucuronidation). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và độc tính. Theo dõi chức năng gan và độc tính chặt chẽ."
        },
        "overdose_management": {
            "symptoms": [
                "Giảm bạch cầu, tiểu cầu nặng (nhiễm trùng, chảy máu)",
                "Thiếu máu nặng",
                "Buồn nôn, nôn nặng",
                "Độc gan (tăng transaminase)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ngay etoposide",
                "Supportive care: bù dịch, điều trị nhiễm trùng, truyền máu/tiểu cầu nếu cần",
                "Hỗ trợ G-CSF nếu giảm bạch cầu nặng",
                "Theo dõi CBC, chức năng gan, chức năng thận",
                "Theo dõi và điều trị triệu chứng"
            ],
            "monitoring": "CBC mỗi ngày, chức năng gan, chức năng thận, dấu hiệu nhiễm trùng, dấu hiệu chảy máu"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với hoặc không thức ăn. Có thể uống với thức ăn để giảm kích ứng dạ dày.",
                "timing": "50mg/m² PO x 21 ngày (mỗi 28 ngày) hoặc 100mg/m² PO ngày 1-5 (mỗi 3-4 tuần). Uống đều đặn cùng một thời điểm mỗi ngày.",
                "notes": "QUAN TRỌNG: 1) Sinh khả dụng thấp (50%), cần liều cao hơn dạng IV, 2) MYELOSUPPRESSION - RẤT PHỔ BIẾN, NẶNG, 3) Theo dõi CBC chặt chẽ."
            },
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W. Nồng độ cuối: 0.2-0.4mg/ml. Không lọc.",
                "infusion_rate": "Truyền tĩnh mạch trong 30-60 phút.",
                "compatibility": ["NS", "D5W"],
                "incompatibility": ["Không pha với các thuốc khác"],
                "notes": "100-120mg/m² IV ngày 1-3 (mỗi 3-4 tuần). Truyền trong 30-60 phút. QUAN TRỌNG: 1) MYELOSUPPRESSION - RẤT PHỔ BIẾN, NẶNG, 2) Theo dõi CBC chặt chẽ, 3) Tương tác với cisplatin và warfarin."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Etoposide (VP-16, Etopophos)",
                "UpToDate - Etoposide: Drug Information",
                "NCCN Guidelines - Small Cell Lung Cancer, Testicular Cancer",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, extensive clinical data, widely used"
        }
    },
    "Irinotecan": {'group': 'Oncology - Topoisomerase Inhibitor',vietnamese_name':
        'Irinotecan, Camptosar, CPT-11', 'administration': ['IV'],
        'indications': [
        'Ung thư đại trực tràng (metastatic)', 'Ung thư phổi không tế bào nhỏ (NSCLC)',
        'Ung thư tụy', 'Ung thư cổ tử cung'],
        'contraindications': [
        'Dị ứng irinotecan', 'Giảm bạch cầu nặng (ANC <1500)',
        'Tiêu chảy nặng đang diễn ra', 'Có thai', 'Đang cho con bú'],
        'dosage': {
        'adult_standard': '125mg/m² IV ngày 1, 8, 15, 22 (mỗi 6 tuần) hoặc 350mg/m² IV mỗi 3 tuần',
        'adult_folfiri': '180mg/m² IV ngày 1 (mỗi 2 tuần, với 5-FU và leucovorin)',
        'notes':
        'Cần premedication với atropine để giảm cholinergic syndrome. Theo dõi sát tiêu chảy'
        },renal_adjustment': {'normal': 'Không đổi', '30_60': 'Thận trọng',
        'under_30': 'Thận trọng, có thể giảm liều'},side_effects': [
        'Tiêu chảy (phổ biến, có thể nặng và nguy hiểm) - sớm (cholinergic) và muộn (độc tính)'
        , 'Giảm bạch cầu, tiểu cầu (myelosuppression - phổ biến)',
        'Buồn nôn, nôn (phổ biến)', 'Cholinergic syndrome (đổ mồ hôi, chảy nước mũi, tăng tiết nước bọt - sớm)'
        , 'Rụng tóc (phổ biến)', 'Mệt mỏi',
        'Độc gan (tăng transaminase - hiếm)'],interactions': [
        '5-Fluorouracil: tăng độc tính tủy xương và tiêu chảy',
        'Ketoconazole: tăng nồng độ irinotecan (tránh dùng)',
        'CYP3A4 inhibitors: tăng nồng độ irinotecan',
        'CYP3A4 inducers: giảm nồng độ irinotecan',
        'Atropine: giảm cholinergic syndrome (dùng kèm)'],pregnancy':
        'D - Chống chỉ định', 'mechanism_of_action':
        'Irinotecan là topoisomerase I inhibitor (camptothecin derivative). Irinotecan là prodrug, được chuyển hóa ở gan thành SN-38 (chất hoạt động). SN-38 ức chế enzyme topoisomerase I, ngăn cản quá trình sửa chữa DNA sau khi sao chép. Topoisomerase I là enzyme quan trọng để tháo xoắn DNA trong quá trình sao chép và phiên mã. Bằng cách ức chế topoisomerase I, SN-38 gây đứt gãy DNA và chết tế bào. Irinotecan tác động chủ yếu lên tế bào đang phân chia nhanh (ung thư), gây độc tế bào. Hiệu quả với ung thư đại trực tràng, phổi, tụy. Độc tính chính: tiêu chảy (sớm - cholinergic, muộn - độc tính) và myelosuppression.'
        , 'monitoring': [
        'Tiêu chảy - theo dõi sát (phổ biến, có thể nặng và nguy hiểm) - sớm (cholinergic, trong 24h) và muộn (độc tính, sau 24h)'
        , 'Công thức máu toàn phần (CBC) trước mỗi chu kỳ (theo dõi giảm bạch cầu, tiểu cầu - phổ biến)'
        , 'Cholinergic syndrome (đổ mồ hôi, chảy nước mũi, tăng tiết nước bọt, co thắt bụng) - sớm, trong 24h sau truyền'
        , 'Dấu hiệu nhiễm trùng (sốt, ớn lạnh) do giảm bạch cầu',
        'Chức năng gan (ALT, AST) trước và trong điều trị (độc gan hiếm)',
        'Dấu hiệu mất nước do tiêu chảy'],precautions': [
        'CẦN PREMEDICATION với atropine (0.25-1mg IV/SC) trước truyền để giảm cholinergic syndrome - QUAN TRỌNG'
        , 'Theo dõi sát tiêu chảy - phổ biến, có thể nặng và nguy hiểm, cần điều trị sớm'
        , 'Tiêu chảy sớm (cholinergic, trong 24h) - điều trị với atropine, loperamide'
        , 'Tiêu chảy muộn (độc tính, sau 24h) - điều trị với loperamide (4mg sau mỗi lần đi ngoài, tối đa 16mg/ngày), bù dịch'
        , 'Giảm liều hoặc trì hoãn điều trị nếu giảm bạch cầu nặng (ANC <1500)',
        'Giảm liều 25-50% nếu có tiêu chảy nặng ở chu kỳ trước',
        'Tương tác với 5-FU (tăng độc tính tủy xương và tiêu chảy)',
        'Tránh dùng với ketoconazole (tăng nồng độ irinotecan)',
        'Tương tác với CYP3A4 inhibitors/inducers (ảnh hưởng nồng độ irinotecan)'],pharmacokinetics': {
        'half_life': '6-12 giờ (irinotecan), 10-20 giờ (SN-38)', 'onset':
        '1-2 tuần (tác dụng lâm sàng)', 'duration': '24-48 giờ (tác dụng sinh học)',
        'protein_binding': '30-68% (irinotecan), 95% (SN-38)', 'clearance':
        'Gan (chuyển hóa irinotecan thành SN-38 qua CYP3A4, UGT1A1), thận (thải trừ - ít)'},storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Bảo quản ở tủ lạnh (2-8°C) nếu yêu cầu. Pha với NS hoặc D5W.'
        , 'black_box_warnings':
        'Tiêu chảy phổ biến và có thể nặng, có thể tử vong. Theo dõi sát tiêu chảy và điều trị sớm. Tiêu chảy sớm (cholinergic, trong 24h) - điều trị với atropine. Tiêu chảy muộn (độc tính, sau 24h) - điều trị với loperamide, bù dịch. Giảm bạch cầu, tiểu cầu phổ biến. Thiếu hụt UGT1A1 (UGT1A1*28) tăng độc tính - nên test trước điều trị nếu có thể.'
        , 'drug_interactions': {'major': [{'drug': '5-Fluorouracil', 'mechanism':
        'Cả hai đều gây độc tính, tác dụng cộng dồn', 'effect':
        'Tăng độc tính tủy xương và tiêu chảy nghiêm trọng', 'management':
        'Theo dõi CBC và tiêu chảy chặt chẽ. Có thể cần giảm liều hoặc trì hoãn điều trị.'}, {
        'drug': 'Ketoconazole, Itraconazole', 'mechanism':
        'Ức chế CYP3A4, tăng nồng độ irinotecan và SN-38', 'effect':
        'Tăng nồng độ irinotecan, tăng độc tính', 'management':
        'Tránh dùng với ketoconazole, itraconazole. Nếu phải dùng, giảm liều irinotecan 50%.'}],moderate': [{'drug': 'CYP3A4 inducers (Rifampin, Carbamazepine)', 'mechanism':
        'Cảm ứng CYP3A4, giảm nồng độ irinotecan', 'effect':
        'Giảm nồng độ irinotecan, giảm hiệu quả', 'management':
        'Theo dõi đáp ứng điều trị. Có thể cần tăng liều irinotecan.'}, {'drug':
        'UGT1A1 inhibitors', 'mechanism':
        'Ức chế chuyển hóa SN-38, tăng nồng độ SN-38', 'effect':
        'Tăng nồng độ SN-38, tăng độc tính', 'management':
        'Thận trọng, có thể cần giảm liều irinotecan.'}],minor': []},contraindications': {'tuyệt_đối': [
        'Dị ứng irinotecan hoặc các thành phần khác',
        'Tiêu chảy nặng đang diễn ra - chống chỉ định cho đến khi hồi phục',
        'Có thai - chống chỉ định tuyệt đối, gây dị tật thai nhi (category D)',
        'Đang cho con bú - chống chỉ định'],tương_đối': [
        'Giảm bạch cầu nặng (ANC <1500) - trì hoãn điều trị cho đến khi hồi phục',
        'Thiếu hụt UGT1A1 (UGT1A1*28) - tăng độc tính, giảm liều 25-50%',
        'Suy gan - thận trọng, có thể cần giảm liều (irinotecan chuyển hóa qua gan)',
        'Suy thận - thận trọng, có thể cần giảm liều',
        'Bệnh nhân cao tuổi - tăng nguy cơ độc tính']},pregnancy_lactation': {
        'fda_category': 'D', 'pregnancy_details':
        'Chống chỉ định trong thai kỳ. Irinotecan gây dị tật thai nhi, sẩy thai, và tử vong thai nhi. Không dùng trong thai kỳ trừ khi lợi ích vượt trội rõ ràng so với nguy cơ.'
        , 'lactation': {'safety': 'Incompatible', 'details':
        'Irinotecan và SN-38 bài tiết vào sữa mẹ. Thuốc có thể gây độc tính nghiêm trọng cho trẻ sơ sinh.'
        , 'recommendation':
        'Không cho con bú khi dùng irinotecan. Ngừng cho con bú hoặc ngừng thuốc.'}},hepatic_adjustment': {'mild': 'Không đổi', 'moderate':
        'Thận trọng, có thể cần giảm liều 25%', 'severe':
        'Thận trọng, giảm liều 25-50%', 'notes':
        'Irinotecan chuyển hóa chủ yếu qua gan (CYP3A4, UGT1A1). Suy gan làm giảm chuyển hóa, tăng nồng độ và độc tính. Theo dõi chức năng gan và độc tính chặt chẽ.'},overdose_management': {'symptoms': [
        'Tiêu chảy nặng, mất nước (nguy hiểm tính mạng)',
        'Giảm bạch cầu, tiểu cầu nặng (nhiễm trùng, chảy máu)',
        'Cholinergic syndrome nặng (đổ mồ hôi, chảy nước mũi, co thắt bụng)',
        'Buồn nôn, nôn nặng', 'Độc gan (tăng transaminase)'],antidote':
        'Atropine cho cholinergic syndrome. Không có antidote đặc hiệu cho độc tính tổng thể.',
        'treatment': [
        'Ngừng ngay irinotecan',
        'Xử trí tiêu chảy: loperamide (4mg sau mỗi lần đi ngoài, tối đa 16mg/ngày), bù dịch, điện giải'
        , 'Xử trí cholinergic syndrome: atropine (0.25-1mg IV/SC)',
        'Supportive care: bù dịch, điều trị nhiễm trùng, truyền máu nếu cần',
        'Theo dõi CBC, chức năng gan, chức năng thận',
        'Theo dõi và điều trị triệu chứng'],monitoring':
        'CBC mỗi ngày, chức năng gan, chức năng thận, dấu hiệu nhiễm trùng, dấu hiệu chảy máu, dấu hiệu mất nước, dấu hiệu cholinergic syndrome'},reversal_agents': {'available': True, 'agents': [{'name': 'Atropine',
        'indication': 'Cholinergic syndrome (đổ mồ hôi, chảy nước mũi, co thắt bụng)',
        'dose': '0.25-1mg IV/SC, có thể lặp lại', 'notes':
        'Điều trị cholinergic syndrome sớm (trong 24h sau truyền)'}]},administration_instructions': {'oral': None, 'iv': {'reconstitution':
        'Pha với NS hoặc D5W theo hướng dẫn nhà sản xuất. Nồng độ cuối: 0.12-2.8mg/ml.',
        'infusion_rate':
        'Truyền trong 30-90 phút. Theo dõi sát trong và sau truyền.',
        'premedication':
        'CẦN PREMEDICATION: Atropine 0.25-1mg IV/SC trước truyền để giảm cholinergic syndrome.',
        'compatibility': ['NS', 'D5W'],incompatibility': [],notes':
        'Theo dõi sát tiêu chảy (phổ biến, có thể nặng). Có thể phối hợp với 5-FU và leucovorin (FOLFIRI regimen).'}},references': {'primary_sources': ['FDA Drug Label - Irinotecan (Camptosar)',
        'UpToDate - Irinotecan Drug Information',
        "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"],last_updated': '2025-02-05', 'evidence_level':
        'High (FDA-approved, extensive clinical data)'}},
    "Topotecan": {
        "group": "Oncology - Topoisomerase Inhibitor",
        "vietnamese_name": "Topotecan, Hycamtin",
        "administration": ["IV", "PO"],
        "indications": [
            "Ung thư buồng trứng (relapsed/refractory)",
            "Ung thư phổi tế bào nhỏ (SCLC - relapsed/refractory)",
            "Ung thư cổ tử cung (relapsed/refractory)"
        ],
        "contraindications": [
            "Dị ứng topotecan",
            "Giảm bạch cầu nặng (ANC <1000)",
            "Giảm tiểu cầu nặng (<25,000)",
            "Có thai",
            "Đang cho con bú"
        ],
        "dosage": {
            "adult_iv": "1.5mg/m² IV ngày 1-5 (mỗi 21 ngày)",
            "adult_po": "2.3mg/m² PO ngày 1-5 (mỗi 21 ngày)",
            "notes": "Truyền IV trong 30 phút. Topotecan có cả dạng IV và PO. Dạng PO tiện lợi hơn nhưng có thể có độc tính tiêu hóa nhiều hơn."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 50% (CrCl 30-49)",
            "under_30": "CHỐNG CHỈ ĐỊNH (CrCl <30)"
        },
        "side_effects": [
            "Giảm bạch cầu, tiểu cầu (myelosuppression - RẤT PHỔ BIẾN, nặng)",
            "Thiếu máu (phổ biến)",
            "Buồn nôn, nôn (phổ biến)",
            "Tiêu chảy (phổ biến)",
            "Mệt mỏi",
            "Rụng tóc (phổ biến)",
            "Đau đầu",
            "Độc gan (hiếm)"
        ],
        "interactions": [
            "Cisplatin: tăng độc tính tủy xương",
            "Carboplatin: tăng độc tính tủy xương",
            "CYP3A4 inhibitors: tăng nồng độ topotecan (dạng PO)"
        ],
        "pregnancy": "D - Chống chỉ định",
        "mechanism_of_action": "Topotecan là topoisomerase I inhibitor (camptothecin derivative), tương tự irinotecan. Topotecan ức chế enzyme topoisomerase I, ngăn cản quá trình sửa chữa DNA sau khi sao chép. Topoisomerase I là enzyme quan trọng để tháo xoắn DNA trong quá trình sao chép và phiên mã. Bằng cách ức chế topoisomerase I, topotecan gây đứt gãy DNA và chết tế bào. Topotecan tác động chủ yếu lên tế bào đang phân chia nhanh (ung thư), gây độc tế bào. Khác với irinotecan (prodrug, chuyển hóa thành SN-38), topotecan là chất hoạt động trực tiếp. Hiệu quả với ung thư buồng trứng, phổi tế bào nhỏ, cổ tử cung. Độc tính chính: myelosuppression (RẤT PHỔ BIẾN, nặng) - giảm bạch cầu, tiểu cầu, thiếu máu.",
        "monitoring": [
            "Công thức máu toàn phần (CBC) trước mỗi chu kỳ và giữa các chu kỳ - QUAN TRỌNG (myelosuppression RẤT PHỔ BIẾN, nặng)",
            "Dấu hiệu nhiễm trùng (sốt, ớn lạnh) do giảm bạch cầu",
            "Dấu hiệu chảy máu (do giảm tiểu cầu)",
            "Chức năng thận (creatinine, eGFR) - QUAN TRỌNG (topotecan thải trừ qua thận, CHỐNG CHỈ ĐỊNH ở CrCl <30)",
            "Chức năng gan (ALT, AST) trước và trong điều trị (độc gan hiếm)",
            "Dấu hiệu buồn nôn, nôn, tiêu chảy"
        ],
        "precautions": [
            "MYELOSUPPRESSION - RẤT PHỔ BIẾN, NẶNG - theo dõi CBC chặt chẽ trước mỗi chu kỳ",
            "CHỐNG CHỈ ĐỊNH ở suy thận nặng (CrCl <30) - topotecan thải trừ qua thận",
            "Giảm liều 50% nếu suy thận (CrCl 30-49)",
            "Trì hoãn điều trị nếu giảm bạch cầu nặng (ANC <1000) hoặc giảm tiểu cầu nặng (<25,000)",
            "Tương tác với cisplatin/carboplatin (tăng độc tính tủy xương)",
            "Dạng PO: tương tác với CYP3A4 inhibitors (tăng nồng độ topotecan)",
            "Có thể cần hỗ trợ G-CSF hoặc truyền máu/tiểu cầu"
        ],
        "pharmacokinetics": {
            "half_life": "2-3 giờ",
            "onset": "1-2 tuần (tác dụng lâm sàng)",
            "duration": "24-48 giờ (tác dụng sinh học)",
            "protein_binding": "35%",
            "metabolism": "Gan (một phần), thận (thải trừ - chủ yếu, 50-70% nguyên dạng)",
            "clearance": "Thận (chủ yếu), gan (một phần)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Bảo quản ở tủ lạnh (2-8°C) nếu yêu cầu. Pha với NS hoặc D5W.",
        "black_box_warnings": "MYELOSUPPRESSION (giảm bạch cầu, tiểu cầu, thiếu máu) RẤT PHỔ BIẾN VÀ NẶNG. Theo dõi CBC trước mỗi chu kỳ. Trì hoãn điều trị nếu giảm bạch cầu nặng (ANC <1000) hoặc giảm tiểu cầu nặng (<25,000). CHỐNG CHỈ ĐỊNH ở suy thận nặng (CrCl <30).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Cisplatin, Carboplatin",
                    "mechanism": "Cả hai đều gây myelosuppression, tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ giảm bạch cầu, tiểu cầu nghiêm trọng",
                    "management": "Theo dõi CBC chặt chẽ. Có thể cần giảm liều hoặc trì hoãn điều trị."
                }
            ],
            "moderate": [
                {
                    "drug": "CYP3A4 Inhibitors (Ketoconazole, Itraconazole, Ritonavir) - dạng PO",
                    "mechanism": "Ức chế CYP3A4, tăng nồng độ topotecan (dạng PO)",
                    "effect": "Tăng nồng độ topotecan, tăng độc tính",
                    "management": "Thận trọng khi dùng dạng PO với CYP3A4 inhibitors. Có thể cần giảm liều topotecan."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng topotecan",
                "Có thai - CHỐNG CHỈ ĐỊNH (category D)",
                "Đang cho con bú - CHỐNG CHỈ ĐỊNH",
                "Suy thận nặng (CrCl <30) - CHỐNG CHỈ ĐỊNH",
                "Giảm bạch cầu nặng (ANC <1000) - trì hoãn điều trị",
                "Giảm tiểu cầu nặng (<25,000) - trì hoãn điều trị"
            ],
            "tương_đối": [
                "Suy thận (CrCl 30-49) - giảm liều 50%",
                "Giảm bạch cầu/tiểu cầu trung bình - theo dõi chặt chẽ",
                "Suy gan - thận trọng",
                "Bệnh nhân cao tuổi - tăng nguy cơ độc tính"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Chống chỉ định trong thai kỳ. Topotecan gây dị tật thai nhi, sẩy thai, và tử vong thai nhi. Không dùng trong thai kỳ trừ khi lợi ích vượt trội rõ ràng so với nguy cơ.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Topotecan bài tiết vào sữa mẹ. Thuốc có thể gây độc tính nghiêm trọng cho trẻ sơ sinh.",
                "recommendation": "Không cho con bú khi dùng topotecan. Ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, có thể cần giảm liều",
            "severe": "Thận trọng, giảm liều 25-50%",
            "notes": "Topotecan chuyển hóa một phần qua gan. Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và độc tính. Tuy nhiên, thải trừ chủ yếu qua thận, nên suy gan ít ảnh hưởng hơn suy thận."
        },
        "overdose_management": {
            "symptoms": [
                "Giảm bạch cầu, tiểu cầu nặng (nhiễm trùng, chảy máu)",
                "Thiếu máu nặng",
                "Buồn nôn, nôn nặng",
                "Tiêu chảy nặng",
                "Độc gan (tăng transaminase)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ngay topotecan",
                "Supportive care: bù dịch, điều trị nhiễm trùng, truyền máu/tiểu cầu nếu cần",
                "Hỗ trợ G-CSF nếu giảm bạch cầu nặng",
                "Theo dõi CBC, chức năng gan, chức năng thận",
                "Theo dõi và điều trị triệu chứng"
            ],
            "monitoring": "CBC mỗi ngày, chức năng gan, chức năng thận, dấu hiệu nhiễm trùng, dấu hiệu chảy máu"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với hoặc không thức ăn. Có thể uống với thức ăn để giảm kích ứng dạ dày.",
                "timing": "2.3mg/m² PO ngày 1-5 (mỗi 21 ngày). Uống đều đặn cùng một thời điểm mỗi ngày.",
                "notes": "QUAN TRỌNG: 1) MYELOSUPPRESSION RẤT PHỔ BIẾN, NẶNG, 2) CHỐNG CHỈ ĐỊNH ở suy thận nặng (CrCl <30), 3) Giảm liều 50% nếu suy thận (CrCl 30-49), 4) Theo dõi CBC chặt chẽ."
            },
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W theo hướng dẫn nhà sản xuất. Nồng độ cuối: 0.25-0.5mg/ml.",
                "infusion_rate": "Truyền trong 30 phút.",
                "compatibility": ["NS", "D5W"],
                "incompatibility": [],
                "notes": "1.5mg/m² IV ngày 1-5 (mỗi 21 ngày). Truyền trong 30 phút. QUAN TRỌNG: 1) MYELOSUPPRESSION RẤT PHỔ BIẾN, NẶNG, 2) CHỐNG CHỈ ĐỊNH ở suy thận nặng (CrCl <30), 3) Theo dõi CBC chặt chẽ."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Topotecan (Hycamtin)",
                "UpToDate - Topotecan: Drug Information",
                "NCCN Guidelines - Ovarian Cancer, Small Cell Lung Cancer",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, extensive clinical data"
        }
    },

}

__all__ = ['TOPOISOMERASE_INHIBITORS_DRUGS']

























