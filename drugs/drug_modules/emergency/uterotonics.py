"""
Emergency Obstetric Uterotonics
Includes Oxytocin for postpartum hemorrhage prevention and treatment
"""

UTEROTONICS_DRUGS = {
    "Oxytocin": {
        "group": "Emergency - Obstetric uterotonic (PPH prevention/treatment)",
        "vietnamese_name": "Oxytocin (Ocytocin)",
        "administration": ["IV", "IM"],
        "indications": [
            "Dự phòng băng huyết sau sinh (PPH) ngay sau sổ thai.",
            "Điều trị băng huyết sau sinh do đờ tử cung.",
            "Kích thích hoặc tăng co chuyển dạ (trong môi trường sản khoa có theo dõi sát).",
        ],
        "contraindications": [
            "Bất tương xứng đầu chậu, ngôi bất thường chưa xử trí.",
            "Sẹo mổ cũ tử cung có nguy cơ vỡ (mổ lấy thai dọc thân, nhiều lần).",
            "Suy thai, nhau tiền đạo trung tâm, nhau bong non chưa xử trí.",
            "Dị ứng với oxytocin.",
        ],
        "dosage": {
            "pph_prophylaxis_im": "10 đơn vị (IU) tiêm bắp ngay sau sổ thai.",
            "pph_prophylaxis_iv": "5–10 IU tiêm tĩnh mạch chậm (trong ít nhất 1 phút).",
            "pph_treatment_infusion": (
                "20–40 IU pha trong 1.000mL NaCl 0,9% hoặc Ringer lactate, "
                "truyền 60–120 giọt/phút (≈ 3–6 IU/giờ), chỉnh theo co tử cung và huyết động."
            ),
            "labor_induction_augmentation": (
                "Pha 5 IU trong 500mL dung dịch đẳng trương (10 mU/mL). "
                "Bắt đầu 1–2 mU/phút, tăng 1–2 mU/phút mỗi 30 phút đến khi đạt co tử cung hiệu quả "
                "(tối đa thường 20 mU/phút, theo phác đồ đơn vị)."
            ),
            "notes": "KHÔNG tiêm tĩnh mạch bolus nhanh liều cao (nguy cơ tụt huyết áp, nhịp nhanh).",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều riêng.",
            "30_60": "Không cần chỉnh liều; chú ý phù, quá tải dịch do kèm truyền dịch.",
            "under_30": "Thận trọng nguy cơ quá tải dịch/hạ natri máu nếu truyền kéo dài.",
        },
        "side_effects": [
            "Buồn nôn, nôn, đỏ bừng.",
            "Hạ huyết áp thoáng qua (nhất là khi tiêm IV nhanh), nhịp tim nhanh phản xạ.",
            "Tăng co tử cung quá mức → đau, vỡ tử cung (hiếm nhưng nguy hiểm).",
            "Nước nhiều, hạ natri máu, co giật (khi truyền kéo dài liều rất cao với dung dịch nhược trương).",
        ],
        "interactions": [
            "Thuốc gây mê, thuốc giãn cơ trơn tử cung (magnesium sulfate liều cao): có thể giảm đáp ứng co tử cung.",
            "Thuốc co mạch/thuốc gây mê hít: phối hợp có thể ảnh hưởng huyết động.",
        ],
        "pregnancy": "Dùng trong thai kỳ chỉ trong bệnh viện với chỉ định rõ ràng (khởi phát/tăng co chuyển dạ).",
        "mechanism_of_action": (
            "Oxytocin là peptide hormone gắn vào thụ thể oxytocin trên cơ tử cung, "
            "hoạt hóa đường tín hiệu phospholipase C–IP3–Ca2+, làm tăng Ca2+ nội bào và gây co cơ tử cung nhịp nhàng. "
            "Ở vú, kích thích tiết sữa bằng cách co cơ biểu mô quanh nang tuyến sữa."
        ),
        "monitoring": [
            "Mức độ co tử cung (tần số, biên độ, thời gian co) và đau bụng.",
            "Mạch, huyết áp, tình trạng mất máu mẹ (PPH).",
            "Tình trạng thai (monitoring tim thai) khi dùng trong chuyển dạ.",
            "Lượng dịch vào/ra nếu truyền kéo dài, dấu hiệu quá tải dịch/hạ natri máu.",
        ],
        "precautions": [
            "Chỉ dùng tại cơ sở y tế có khả năng phẫu thuật cấp cứu và hồi sức mẹ/trẻ.",
            "Tránh truyền nhanh hoặc bolus liều cao IV (nguy cơ hạ huyết áp, loạn nhịp).",
            "Theo dõi sát co tử cung để tránh tăng co/hyperstimulation (nguy cơ vỡ tử cung, suy thai).",
            "Thận trọng ở tiền sử mổ lấy thai, sẹo tử cung, đa thai, đa ối.",
        ],
        "pharmacokinetics": {
            "half_life": "3–5 phút (ngắn).",
            "onset": "Ngay sau khi tiêm IV; 3–5 phút sau IM.",
            "duration": "Khoảng 30–60 phút sau IM; tác dụng IV phụ thuộc tốc độ truyền.",
            "protein_binding": "Thấp; bị phân hủy nhanh bởi oxytocinase.",
            "clearance": "Bị giáng hóa ở gan, thận và bởi oxytocinase nhau thai.",
        },
        "storage": (
            "Bảo quản 2–8°C (tủ lạnh), tránh ánh sáng. "
            "Một số chế phẩm ổn định ở nhiệt độ phòng trong thời gian ngắn theo hướng dẫn nhà sản xuất."
        ),
        "black_box_warnings": (
            "Nguy cơ tăng co tử cung quá mức, vỡ tử cung, rối loạn huyết động nếu dùng sai chỉ định hoặc liều. "
            "Chỉ sử dụng bởi bác sĩ có kinh nghiệm sản khoa trong môi trường bệnh viện có phương tiện hồi sức."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Prostaglandin uterotonic mạnh (ví dụ carboprost)",
                    "mechanism": "Tác dụng cộng dồn tăng co tử cung.",
                    "effect": "Nguy cơ tăng co, vỡ tử cung.",
                    "management": "Dùng tuần tự, theo dõi rất sát co tử cung và huyết động.",
                }
            ],
            "moderate": [
                {
                    "drug": "Magnesium sulfate liều cao",
                    "mechanism": "Giảm co cơ tử cung, đối kháng một phần tác dụng oxytocin.",
                    "effect": "Có thể cần liều oxytocin cao hơn để đạt co hiệu quả.",
                    "management": "Điều chỉnh liều dựa trên co tử cung; không vượt liều khuyến cáo.",
                }
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Bất tương xứng đầu chậu chưa xử trí.",
                "Ngôi ngang, ngôi bất thường chưa cho phép sinh đường âm đạo.",
                "Nhau tiền đạo trung tâm, nhau bong non nặng chưa xử trí.",
            ],
            "tương_đối": [
                "Sẹo mổ lấy thai dọc thân tử cung hoặc nhiều lần.",
                "Đa thai, đa ối.",
                "Tiền sản giật nặng/tăng huyết áp chưa kiểm soát.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "Không phân loại – dùng có kiểm soát trong thai kỳ và sau sinh.",
            "pregnancy_details": (
                "Được dùng rộng rãi để khởi phát/tăng co chuyển dạ và dự phòng/điều trị băng huyết sau sinh, "
                "nhưng phải theo dõi sát tại bệnh viện."
            ),
            "lactation": {
                "safety": "Compatible",
                "details": "Oxytocin nội sinh là hormone tiết sữa; liều dùng sản khoa không gây hại cho trẻ bú.",
                "recommendation": "Có thể cho bú bình thường sau dùng oxytocin.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Không cần chỉnh liều; theo dõi huyết động.",
            "severe": "Dữ liệu hạn chế; dùng liều thấp nhất hiệu quả, theo dõi sát.",
            "notes": "Giáng hóa nhanh bởi oxytocinase; suy gan ít ảnh hưởng đáng kể đến thời gian bán thải.",
        },
        "overdose_management": {
            "symptoms": [
                "Tăng co tử cung kéo dài, đau dữ dội.",
                "Dấu hiệu suy thai (nếu đang chuyển dạ): bất thường tim thai.",
                "Hạ huyết áp, nhịp nhanh, quá tải dịch, hạ natri máu (truyền kéo dài liều cao).",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Ngừng ngay oxytocin, cho sản phụ nằm nghiêng trái.",
                "Hỗ trợ hô hấp, huyết động; điều chỉnh dịch và điện giải.",
                "Nếu co tử cung quá mức, có thể dùng thuốc giảm co (tocolytic) theo phác đồ (ví dụ salbutamol, nitroglycerin).",
                "Xử trí sản khoa nếu nghi vỡ tử cung hoặc suy thai.",
            ],
            "monitoring": (
                "Theo dõi liên tục co tử cung, huyết áp, mạch, tình trạng thai (nếu còn thai), "
                "và điện giải/natri nếu truyền kéo dài với lượng dịch lớn."
            ),
        },
        "reversal_agents": None,
        "administration_instructions": {
            "iv": {
                "reconstitution": (
                    "Pha 5–10 IU oxytocin trong 500–1000mL NaCl 0,9% hoặc Ringer lactate. "
                    "KHÔNG pha với dung dịch nhược trương quá mức để tránh hạ natri máu."
                ),
                "infusion_rate": (
                    "PPH: truyền nhanh hơn ban đầu (ví dụ 120 giọt/phút) rồi giảm khi tử cung co tốt; "
                    "khởi phát chuyển dạ: bắt đầu 1–2 mU/phút, tăng dần mỗi 30 phút đến khi đạt co hiệu quả."
                ),
                "compatibility": ["NaCl 0,9%", "Ringer lactate"],
                "incompatibility": [
                    "Không pha chung với thuốc khác trong cùng dây truyền nếu chưa có dữ liệu tương hợp.",
                ],
                "notes": "Luôn dùng bơm tiêm điện hoặc dây truyền giọt đếm để kiểm soát tốc độ.",
            },
            "im": {
                "reconstitution": "Dùng dung dịch oxytocin sẵn có, không cần pha loãng.",
                "notes": "Tiêm bắp sâu 10 IU ngay sau sổ thai để dự phòng PPH khi không có đường truyền.",
            },
        },
        "references": {
            "primary_sources": [
                "WHO Recommendations for the Prevention and Treatment of Postpartum Haemorrhage",
                "FIGO/ICM guidelines on active management of third stage of labour",
                "Textbook of Obstetrics and Gynecology",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – guideline-based",
        },
    },
}

__all__ = ["UTEROTONICS_DRUGS"]

