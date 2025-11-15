"""
Thyroid Hormones - Metabolic and Endocrine Medications
"""

THYROID_HORMONES_DRUGS = {
    "Levothyroxine": {
        "group": "Endocrinology - Thyroid Hormone",
        "vietnamese_name": "Levothyroxine, Synthroid, Euthyrox, Thyroxine",
        "administration": ["PO", "IV"],
        "indications": [
            "Suy giáp (hypothyroidism)",
            "Suy giáp bẩm sinh",
            "Bướu cổ (goiter)",
            "Myxedema coma (IV)",
            "Ức chế TSH sau điều trị ung thư tuyến giáp"
        ],
        "contraindications": [
            "Cường giáp không điều trị",
            "Nhồi máu cơ tim cấp",
            "Viêm cơ tim cấp",
            "Dị ứng levothyroxine"
        ],
        "dosage": {
            "adult_start": "25-50mcg x 1 lần/ngày (sáng đói, trước ăn 30-60 phút)",
            "adult_usual": "75-150mcg x 1 lần/ngày",
            "adult_elderly": "Bắt đầu 12.5-25mcg/ngày, tăng dần",
            "adult_cardiac": "Bắt đầu 12.5-25mcg/ngày",
            "adult_myxedema_coma": "200-500mcg IV x 1 lần, sau đó 50-100mcg/ngày",
            "notes": "Uống sáng đói, cách xa thức ăn, thuốc khác ít nhất 30-60 phút"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Dấu hiệu cường giáp (quá liều): tim đập nhanh, lo âu, mất ngủ, đổ mồ hôi",
            "Đau ngực",
            "Nhức đầu",
            "Rối loạn kinh nguyệt",
            "Rụng tóc (tạm thời)",
            "Loạn nhịp tim (quá liều)"
        ],
        "interactions": [
            "Calcium/Sắt/Antacid: giảm hấp thu - cách 4 giờ",
            "Cholestyramine: giảm hấp thu - cách 4 giờ",
            "Warfarin: tăng tác dụng chống đông (điều chỉnh liều warfarin)",
            "Digoxin: có thể cần tăng liều digoxin",
            "Insulin/Oral hypoglycemics: có thể cần điều chỉnh liều",
            "Estrogen: có thể cần tăng liều levothyroxine"
        ],
        "pregnancy": "A - An toàn, cần thiết cho thai kỳ",
        "mechanism_of_action": "Hormone tuyến giáp tổng hợp (T4, thyroxine). Bổ sung hoặc thay thế hormone tuyến giáp thiếu hụt. Trong tế bào, T4 được chuyển đổi thành T3 (triiodothyronine) - dạng hoạt động. T3 gắn với thyroid hormone receptor trong nhân tế bào, điều hòa biểu hiện gen, tăng chuyển hóa cơ bản, tăng nhịp tim, tăng nhiệt độ cơ thể, tăng nhu động ruột, và tăng phát triển tế bào. Được dùng trong suy giáp (hypothyroidism), bướu cổ, và sau phẫu thuật cắt tuyến giáp.",
        "monitoring": [
            "TSH (thyroid stimulating hormone) - mục tiêu: bình thường hóa TSH, kiểm tra mỗi 6-8 tuần khi điều chỉnh liều",
            "Free T4 (FT4) - mục tiêu: trong khoảng bình thường",
            "T3 (nếu cần, trong một số trường hợp)",
            "Nhịp tim và huyết áp (tăng ở quá liều)",
            "Dấu hiệu cường giáp (run, đổ mồ hôi, mất ngủ, nhịp tim nhanh, sụt cân) - dấu hiệu quá liều",
            "Dấu hiệu suy giáp (mệt mỏi, tăng cân, nhịp tim chậm, táo bón, lạnh) - dấu hiệu thiếu liều",
            "Xương (loãng xương nếu quá liều kéo dài)",
            "Tim mạch (rối loạn nhịp tim, đau thắt ngực ở bệnh nhân bệnh mạch vành nếu quá liều)"
        ],
        "precautions": [
            "PHẢI uống vào buổi sáng, khi đói, 30-60 phút trước khi ăn (thức ăn giảm hấp thu 40-60%)",
            "KHÔNG uống cùng với: sắt, canxi, antacid, sucralfate, cholestyramine (cách ít nhất 4 giờ)",
            "Bắt đầu với liều thấp, tăng dần dựa trên TSH",
            "Ở bệnh nhân bệnh mạch vành hoặc người cao tuổi: bắt đầu với liều rất thấp, tăng chậm",
            "Không được ngừng đột ngột (trừ khi có chỉ định)",
            "Liều thay thế: 1.6-1.8 mcg/kg/ngày",
            "TSH mục tiêu: 0.5-2.5 mIU/L (tùy tuổi và tình trạng)",
            "Khi điều chỉnh liều: kiểm tra TSH sau 6-8 tuần (TSH thay đổi chậm)",
            "Quá liều có thể gây cường giáp, rối loạn nhịp tim, đau thắt ngực ở bệnh nhân bệnh mạch vành",
            "Thận trọng ở phụ nữ có thai (nhu cầu tăng 25-50%)",
            "Không dùng để giảm cân (nguy hiểm)"
        ],
        "pharmacokinetics": {
            "half_life": "7 ngày (rất dài)",
            "onset": "3-5 ngày",
            "duration": "Dài (nhiều ngày)",
            "protein_binding": "99.97% (rất cao, gắn với TBG, transthyretin, albumin)",
            "metabolism": "Gan và các mô ngoại vi (deiodination thành T3)",
            "clearance": "Chủ yếu qua gan, một phần qua thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng. Viên nén: tránh ẩm.",
        "black_box_warnings": "Không được dùng để giảm cân ở bệnh nhân bình giáp. Quá liều có thể gây cường giáp, rối loạn nhịp tim, và đau thắt ngực ở bệnh nhân bệnh mạch vành. Ở bệnh nhân bệnh mạch vành, phải bắt đầu với liều thấp và tăng chậm.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Cholestyramine, Colestipol, Colesevelam",
                    "mechanism": "Các resin gắn acid mật gắn với levothyroxine trong ruột, giảm hấp thu đáng kể.",
                    "effect": "Giảm hấp thu levothyroxine 40-60%, giảm hiệu quả điều trị",
                    "management": "Cách ít nhất 4 giờ giữa levothyroxine và resin. Uống levothyroxine trước, resin sau. Theo dõi TSH và điều chỉnh liều nếu cần."
                },
                {
                    "drug": "Calcium carbonate, Sắt, Antacid (Aluminum, Magnesium)",
                    "mechanism": "Các cation (Ca2+, Fe2+, Al3+, Mg2+) gắn với levothyroxine trong ruột, tạo phức hợp không hấp thu được.",
                    "effect": "Giảm hấp thu levothyroxine 30-50%, giảm hiệu quả điều trị",
                    "management": "Cách ít nhất 4 giờ giữa levothyroxine và các thuốc này. Uống levothyroxine sáng đói, các thuốc khác sau bữa ăn. Theo dõi TSH."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Levothyroxine tăng chuyển hóa các yếu tố đông máu phụ thuộc vitamin K, tăng tác dụng chống đông của warfarin.",
                    "effect": "Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR chặt chẽ khi bắt đầu, thay đổi liều, hoặc ngừng levothyroxine. Điều chỉnh liều warfarin nếu cần. INR có thể thay đổi trong 1-2 tuần sau khi điều chỉnh liều levothyroxine."
                }
            ],
            "moderate": [
                {
                    "drug": "Estrogen (Oral contraceptives, Hormone replacement therapy)",
                    "mechanism": "Estrogen tăng nồng độ thyroxine-binding globulin (TBG), tăng gắn T4 với protein, giảm T4 tự do.",
                    "effect": "Tăng nhu cầu levothyroxine, có thể cần tăng liều 25-50%",
                    "management": "Theo dõi TSH sau 6-8 tuần khi bắt đầu hoặc ngừng estrogen. Điều chỉnh liều levothyroxine nếu TSH tăng."
                },
                {
                    "drug": "Rifampin, Carbamazepine, Phenytoin, Phenobarbital",
                    "mechanism": "Cảm ứng enzyme chuyển hóa, tăng chuyển hóa levothyroxine.",
                    "effect": "Giảm nồng độ levothyroxine, tăng nhu cầu liều",
                    "management": "Theo dõi TSH và điều chỉnh liều levothyroxine. Có thể cần tăng liều 25-50%."
                },
                {
                    "drug": "Sucralfate",
                    "mechanism": "Sucralfate gắn với levothyroxine trong ruột, giảm hấp thu.",
                    "effect": "Giảm hấp thu levothyroxine",
                    "management": "Cách ít nhất 4 giờ. Uống levothyroxine sáng đói, sucralfate sau bữa ăn."
                }
            ],
            "minor": [
                {
                    "drug": "Digoxin",
                    "mechanism": "Levothyroxine có thể tăng chuyển hóa digoxin, giảm nồng độ digoxin.",
                    "effect": "Giảm nồng độ digoxin, có thể cần tăng liều digoxin",
                    "management": "Theo dõi nồng độ digoxin và điều chỉnh liều nếu cần."
                },
                {
                    "drug": "Insulin, Oral hypoglycemics",
                    "mechanism": "Levothyroxine tăng chuyển hóa glucose, có thể ảnh hưởng đến kiểm soát đường huyết.",
                    "effect": "Có thể cần điều chỉnh liều insulin hoặc thuốc hạ đường huyết",
                    "management": "Theo dõi đường huyết khi bắt đầu hoặc điều chỉnh liều levothyroxine."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Cường giáp không điều trị (có thể làm nặng thêm triệu chứng)",
                "Nhồi máu cơ tim cấp (có thể làm nặng thêm, tăng nguy cơ rối loạn nhịp tim)",
                "Viêm cơ tim cấp (có thể làm nặng thêm)",
                "Dị ứng levothyroxine hoặc các thành phần khác"
            ],
            "tương_đối": [
                "Bệnh mạch vành (bắt đầu với liều rất thấp, tăng chậm)",
                "Rối loạn nhịp tim (thận trọng, theo dõi sát)",
                "Suy tim (thận trọng, bắt đầu với liều thấp)",
                "Loãng xương (theo dõi mật độ xương nếu dùng liều cao kéo dài)"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "A",
            "pregnancy_details": "Levothyroxine là hormone tuyến giáp tự nhiên, an toàn và cần thiết trong thai kỳ. Suy giáp không điều trị trong thai kỳ có thể gây chậm phát triển thần kinh ở thai nhi, sảy thai, sinh non, và các biến chứng khác. Nhu cầu levothyroxine tăng 25-50% trong thai kỳ, đặc biệt trong tam cá nguyệt đầu và thứ hai. Phải theo dõi TSH mỗi 4-6 tuần trong thai kỳ và điều chỉnh liều để duy trì TSH trong khoảng bình thường (mục tiêu: 0.5-2.5 mIU/L trong tam cá nguyệt đầu, <3.0 mIU/L trong tam cá nguyệt thứ hai và thứ ba).",
            "lactation": {
                "safety": "Compatible",
                "details": "Levothyroxine bài tiết vào sữa mẹ ở nồng độ rất thấp, không ảnh hưởng đến chức năng tuyến giáp của trẻ bú mẹ. An toàn cho trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Không cần điều chỉnh liều. Theo dõi chức năng tuyến giáp của mẹ và trẻ nếu cần."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Levothyroxine chủ yếu chuyển hóa qua gan (deiodination), nhưng suy gan nhẹ không ảnh hưởng đáng kể.",
            "moderate": "Không cần điều chỉnh liều thường quy. Theo dõi TSH và điều chỉnh nếu cần. Chuyển hóa có thể giảm nhẹ ở suy gan trung bình.",
            "severe": "Không cần điều chỉnh liều thường quy. Theo dõi TSH chặt chẽ. Có thể cần giảm liều nhẹ nếu có dấu hiệu quá liều (tăng TSH không phản ánh đúng nhu cầu).",
            "notes": "Levothyroxine chủ yếu chuyển hóa qua gan, nhưng suy gan thường không ảnh hưởng đáng kể đến nồng độ T4. Tuy nhiên, suy gan nặng có thể ảnh hưởng đến chuyển đổi T4 thành T3. Theo dõi TSH và FT4, không chỉ dựa vào T4 toàn phần."
        },
        "overdose_management": {
            "symptoms": [
                "Dấu hiệu cường giáp: tim đập nhanh, lo âu, mất ngủ, đổ mồ hôi, run tay",
                "Rối loạn nhịp tim: nhịp nhanh xoang, rung nhĩ, rung thất (hiếm)",
                "Đau thắt ngực, nhồi máu cơ tim (ở bệnh nhân bệnh mạch vành)",
                "Sụt cân không giải thích được",
                "Tiêu chảy, tăng nhu động ruột",
                "Yếu cơ, run cơ",
                "Loãng xương (nếu quá liều kéo dài)"
            ],
            "antidote": "Không có antidote đặc hiệu. Ngừng levothyroxine và điều trị hỗ trợ.",
            "treatment": [
                "Ngừng levothyroxine ngay lập tức",
                "Theo dõi dấu hiệu sinh tồn: nhịp tim, huyết áp, ECG",
                "Điều trị rối loạn nhịp tim nếu có (beta-blockers như propranolol để giảm nhịp tim)",
                "Điều trị đau thắt ngực nếu có (nitroglycerin, beta-blockers)",
                "Theo dõi TSH, FT4, FT3 sau 2-4 tuần",
                "Khởi động lại với liều thấp hơn sau khi TSH tăng lên",
                "Ở bệnh nhân bệnh mạch vành: điều trị tích cực rối loạn nhịp tim và đau thắt ngực"
            ],
            "monitoring": "Nhịp tim, huyết áp, ECG, TSH, FT4, FT3, dấu hiệu cường giáp. Theo dõi ít nhất 2-4 tuần sau khi ngừng thuốc."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "PHẢI uống khi đói, 30-60 phút trước khi ăn sáng. Thức ăn giảm hấp thu 40-60%. Có thể uống với nước đầy đủ.",
                "timing": "Uống vào buổi sáng, khi đói, 30-60 phút trước khi ăn. Cách xa các thuốc khác ít nhất 4 giờ (sắt, canxi, antacid, cholestyramine, sucralfate). Uống cùng thời điểm mỗi ngày để duy trì nồng độ ổn định."
            },
            "iv": {
                "reconstitution": "Pha với nước cất hoặc dung dịch muối đẳng trương. Không pha với các dung dịch khác.",
                "infusion_rate": "Truyền chậm trong 2-5 phút. Không truyền nhanh.",
                "compatibility": ["D5W", "Normal saline"],
                "incompatibility": ["Không trộn với các thuốc khác"],
                "notes": "Chỉ dùng IV trong myxedema coma hoặc khi không thể dùng PO. Chuyển sang PO ngay khi có thể. Liều IV thường bằng 50-75% liều PO."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Levothyroxine (Synthroid, Levoxyl, Tirosint)",
                "American Thyroid Association Guidelines - Hypothyroidism in Pregnancy",
                "Endocrine Society Clinical Practice Guidelines - Thyroid Hormone Replacement",
                "UpToDate - Hypothyroidism treatment",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "A - Dựa trên FDA drug labels, ATA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },
}

__all__ = ['THYROID_HORMONES_DRUGS']

