"""
Respiratory Medications
Active module - contains all respiratory drug data
"""

RESPIRATORY_DRUGS = {
"Salbutamol": {
        "group": "Respiratory - Short-acting Beta-2 Agonist (SABA)",
        "vietnamese_name": "Salbutamol, Ventolin",
        "administration": ["Inhalation", "IV", "PO"],
        "indications": [
            "Hen phế quản (cắt cơn)",
            "COPD (cắt cơn)",
            "Co thắt phế quản cấp",
            "Dự phòng co thắt do vận động"
        ],
        "contraindications": [
            "Dị ứng",
            "Nhịp tim nhanh nặng"
        ],
        "dosage": {
            "adult_inhalation": "1-2 puffs (100-200mcg) mỗi 4-6 giờ khi cần",
            "adult_nebulizer": "2.5-5mg mỗi 4-6 giờ",
            "adult_iv": "0.5mg IV, sau đó 5-20mcg/phút truyền liên tục",
            "notes": "Dùng khi cần (PRN) cho cắt cơn, không dùng thường xuyên"
        },
        "side_effects": [
            "Tim đập nhanh",
            "Run cơ",
            "Đau đầu",
            "Hạ kali máu (liều cao)",
            "Loạn nhịp tim (hiếm)"
        ],
        "interactions": [
            "Beta-blocker: đối kháng tác dụng (tránh dùng)"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Kích thích beta-2 adrenergic receptors ở cơ trơn phế quản, kích hoạt adenylate cyclase → tăng cAMP → giãn cơ trơn phế quản. Tác dụng nhanh, ngắn (4-6 giờ). Chọn lọc beta-2 hơn beta-1 nhưng vẫn có tác dụng tim mạch ở liều cao. Giảm phóng thích chất trung gian gây viêm từ mast cells.",
        "monitoring": [
            "Nhịp tim, huyết áp (đặc biệt khi dùng IV hoặc liều cao)",
            "Kali máu nếu dùng liều cao hoặc kéo dài",
            "Đáp ứng phế quản (peak flow, FEV1)",
            "Dấu hiệu quá liều: nhịp tim nhanh >120 bpm, run cơ nặng, loạn nhịp",
            "Dấu hiệu nghịch lý: co thắt phế quản nặng hơn (hiếm nhưng nguy hiểm)"
        ],
        "precautions": [
            "Chỉ dùng khi cần (PRN) cho cắt cơn - không dùng thường xuyên",
            "Nếu cần dùng >4 lần/ngày → cần đánh giá lại điều trị và tăng ICS",
            "Tránh dùng với beta-blocker (đối kháng tác dụng)",
            "Thận trọng ở bệnh nhân tim mạch, tăng huyết áp, loạn nhịp (tăng nguy cơ tác dụng tim mạch)",
            "Dùng liều thấp nhất hiệu quả để giảm tác dụng phụ",
            "Rửa miệng sau khi dùng dạng hít để giảm kích ứng và nấm miệng",
            "Nếu không đáp ứng → cần đánh giá lại chẩn đoán và điều trị"
        ],
        "pharmacokinetics": {
            "half_life": "2-7 giờ (hít), 2-4 giờ (IV)",
            "onset": "5-15 phút (hít), 2-5 phút (IV)",
            "duration": "4-6 giờ",
            "protein_binding": "10%",
            "clearance": "Gan (chuyển hóa qua sulfation, một phần qua CYP450), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh nhiệt độ cao, tránh ánh sáng trực tiếp. Không làm lạnh. Kiểm tra hạn sử dụng định kỳ.",
        "black_box_warnings": "Không dùng đơn độc cho hen phế quản mạn tính - phải kết hợp với corticosteroid dạng hít. Dùng quá mức (>4 lần/ngày) có thể gây tăng nguy cơ tử vong do hen. Nếu cần dùng thường xuyên → cần đánh giá lại và tăng điều trị kiểm soát."
    },
    "Salmeterol": {
        "group": "Respiratory - Long-acting Beta-2 Agonist (LABA)",
        "vietnamese_name": "Salmeterol, Serevent",
        "administration": ["Inhalation"],
        "indications": [
            "Hen phế quản (phòng ngừa, phải dùng với ICS)",
            "COPD (phòng ngừa)",
            "Co thắt phế quản ban đêm",
            "Dự phòng co thắt do vận động"
        ],
        "contraindications": [
            "Dị ứng",
            "Nhịp tim nhanh nặng",
            "Hen phế quản cấp (không dùng đơn độc)"
        ],
        "dosage": {
            "adult_inhalation": "50mcg x 2 lần/ngày (sáng và tối)",
            "notes": "PHẢI dùng kết hợp với ICS. Không dùng đơn độc cho hen. Tác dụng kéo dài 12 giờ"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Tim đập nhanh",
            "Run cơ",
            "Đau đầu",
            "Co thắt phế quản nghịch lý (hiếm)",
            "Loạn nhịp tim (hiếm)"
        ],
        "interactions": [
            "Beta-blocker: đối kháng tác dụng",
            "Theophylline: tăng tác dụng phụ"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Kích thích beta-2 adrenergic receptors ở cơ trơn phế quản, kích hoạt adenylate cyclase → tăng cAMP → giãn cơ trơn phế quản. Tác dụng dài (12 giờ) do liên kết chặt với receptor, giải phóng chậm. Chọn lọc beta-2 hơn beta-1 nhưng vẫn có tác dụng tim mạch. Giảm phóng thích chất trung gian gây viêm từ mast cells. Dùng để phòng ngừa, không dùng để cắt cơn (tác dụng chậm).",
        "monitoring": [
            "Nhịp tim, huyết áp (đặc biệt khi bắt đầu điều trị)",
            "Đáp ứng phế quản (peak flow, FEV1) - đánh giá hiệu quả phòng ngừa",
            "Dấu hiệu quá liều: nhịp tim nhanh >120 bpm, run cơ nặng, loạn nhịp",
            "Dấu hiệu nghịch lý: co thắt phế quản nặng hơn (hiếm nhưng nguy hiểm)",
            "Tần suất dùng SABA (nếu tăng → cần đánh giá lại điều trị)"
        ],
        "precautions": [
            "PHẢI dùng kết hợp với ICS (inhaled corticosteroid) - không bao giờ dùng đơn độc cho hen phế quản",
            "Không dùng để cắt cơn (tác dụng chậm, không hiệu quả) - cần có SABA để cắt cơn",
            "Không dùng đơn độc cho hen phế quản cấp - nguy cơ tăng tử vong",
            "Tránh dùng với beta-blocker (đối kháng tác dụng)",
            "Thận trọng ở bệnh nhân tim mạch, tăng huyết áp, loạn nhịp (tăng nguy cơ tác dụng tim mạch)",
            "Dùng đều đặn 2 lần/ngày (sáng và tối) để phòng ngừa",
            "Rửa miệng sau khi dùng dạng hít để giảm kích ứng và nấm miệng",
            "Nếu cần dùng SABA thường xuyên → cần đánh giá lại điều trị và tăng ICS",
            "Nếu không đáp ứng → cần đánh giá lại chẩn đoán và điều trị"
        ],
        "pharmacokinetics": {
            "half_life": "5.5 giờ (dài hơn salbutamol)",
            "onset": "15-30 phút (chậm hơn SABA)",
            "duration": "12 giờ (dài)",
            "protein_binding": "96%",
            "clearance": "Gan (chuyển hóa qua CYP3A4), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh nhiệt độ cao, tránh ánh sáng trực tiếp. Không làm lạnh. Kiểm tra hạn sử dụng định kỳ.",
        "black_box_warnings": "KHÔNG BAO GIỜ dùng đơn độc cho hen phế quản - phải dùng kết hợp với ICS. Dùng đơn độc LABA có thể tăng nguy cơ tử vong do hen. Không dùng để cắt cơn hen cấp (tác dụng chậm). Chỉ dùng để phòng ngừa và phải luôn có SABA để cắt cơn.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Beta-blockers (không chọn lọc: Propranolol, Nadolol)",
                    "mechanism": "Đối kháng tác dụng beta-2, chặn tác dụng giãn phế quản của salmeterol",
                    "effect": "Đối kháng tác dụng giãn phế quản, có thể gây co thắt phế quản nặng, suy hô hấp",
                    "management": "TRÁNH DÙNG với beta-blocker không chọn lọc. Nếu bệnh nhân cần beta-blocker, dùng beta-blocker chọn lọc beta-1 (atenolol, metoprolol) với thận trọng. Theo dõi chặt chẽ đáp ứng phế quản."
                }
            ],
            "moderate": [
                {
                    "drug": "Theophylline",
                    "mechanism": "Cả hai đều kích thích beta-adrenergic, có thể tăng tác dụng phụ và độc tính",
                    "effect": "Tăng tác dụng phụ (run, tim đập nhanh, loạn nhịp), tăng nguy cơ độc tính theophylline",
                    "management": "Theo dõi nồng độ theophylline. Theo dõi nhịp tim và triệu chứng. Có thể cần giảm liều theophylline."
                },
                {
                    "drug": "Digoxin",
                    "mechanism": "Salmeterol có thể gây hạ kali máu và tăng nhịp tim, tăng nguy cơ độc tính digoxin",
                    "effect": "Tăng nguy cơ loạn nhịp tim, tăng độc tính digoxin (đặc biệt khi hạ kali máu)",
                    "management": "Theo dõi nồng độ digoxin và kali máu. Theo dõi ECG nếu có triệu chứng. Có thể cần điều chỉnh liều digoxin."
                },
                {
                    "drug": "Diuretics (Furosemide, Thiazide)",
                    "mechanism": "Cả hai đều có thể gây hạ kali máu, tăng nguy cơ hạ kali máu nghiêm trọng",
                    "effect": "Tăng nguy cơ hạ kali máu nghiêm trọng, loạn nhịp tim, yếu cơ",
                    "management": "Theo dõi kali máu thường xuyên. Bổ sung kali nếu cần. Có thể cần điều chỉnh liều diuretic."
                }
            ],
            "minor": [
                {
                    "drug": "Tricyclic Antidepressants (TCA)",
                    "mechanism": "TCA tăng nhạy cảm với catecholamine, có thể tăng tác dụng tim mạch",
                    "effect": "Tăng nhịp tim, tăng huyết áp (nhẹ)",
                    "management": "Theo dõi nhịp tim và huyết áp. Không cần điều chỉnh liều thường quy."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Dị ứng với salmeterol hoặc các thành phần khác",
                "Nhịp tim nhanh nặng không kiểm soát (>120 bpm)",
                "Rối loạn nhịp tim nặng (rung nhĩ, rung thất không kiểm soát)",
                "Hen phế quản cấp (không dùng đơn độc, không dùng để cắt cơn)"
            ],
            "relative": [
                "Bệnh tim mạch (suy tim, bệnh mạch vành) - thận trọng, theo dõi chặt chẽ",
                "Tăng huyết áp không kiểm soát - có thể tăng huyết áp",
                "Loạn nhịp tim nhẹ - có thể làm nặng",
                "Đái tháo đường - có thể tăng đường huyết",
                "Hạ kali máu - có thể làm nặng",
                "Cường giáp - tăng nhạy cảm với catecholamine",
                "Dùng với digoxin - tăng nguy cơ loạn nhịp",
                "Dùng với theophylline - tăng tác dụng phụ"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Salmeterol là thuốc phân loại C. Các nghiên cứu trên động vật cho thấy có thể có tác dụng phụ trên thai nhi, nhưng không có nghiên cứu đầy đủ trên người. Salmeterol được sử dụng trong thai kỳ để điều trị hen và có vẻ an toàn. Hen phế quản không kiểm soát có thể gây nguy hiểm cho cả mẹ và thai nhi (thiếu oxy, suy thai). Salmeterol có thể được dùng khi lợi ích vượt quá nguy cơ, nhưng PHẢI dùng kết hợp với ICS. Dạng hít được ưu tiên để giảm tác dụng toàn thân.",
            "lactation": {
                "safety": "Compatible",
                "details": "Salmeterol bài tiết ít vào sữa mẹ. Nồng độ trong sữa mẹ rất thấp do hấp thu toàn thân ít từ dạng hít. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng an toàn khi cho con bú. Dạng hít được ưu tiên để giảm tác dụng toàn thân."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng - salmeterol chuyển hóa qua gan (CYP3A4), có thể tích lũy ở suy gan nặng",
            "notes": "Salmeterol chuyển hóa qua CYP3A4 ở gan. Ở suy gan nặng, có thể tích lũy và tăng tác dụng phụ. Theo dõi chặt chẽ nhịp tim và tác dụng phụ. Có thể cần giảm liều hoặc tăng khoảng cách giữa các liều."
        },
        "overdose_management": {
            "symptoms": [
                "Nhịp tim nhanh nghiêm trọng (>150 bpm)",
                "Run cơ nặng",
                "Loạn nhịp tim (rung nhĩ, rung thất)",
                "Đau ngực",
                "Khó thở nặng",
                "Co thắt phế quản nghịch lý",
                "Hạ kali máu nghiêm trọng",
                "Tăng đường huyết",
                "Kích động, lo âu",
                "Đau đầu nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Beta-blocker chọn lọc beta-1 (atenolol, metoprolol) có thể được dùng để đối kháng tác dụng tim mạch, nhưng thận trọng vì có thể làm nặng co thắt phế quản.",
            "treatment": [
                "Ngừng ngay salmeterol",
                "Hỗ trợ hô hấp nếu cần (oxy, thở máy nếu suy hô hấp)",
                "Theo dõi nhịp tim, huyết áp, ECG liên tục",
                "Điều trị loạn nhịp tim nếu có (theo protocol)",
                "Bổ sung kali nếu hạ kali máu",
                "Điều trị tăng đường huyết nếu cần",
                "Nếu có co thắt phế quản nghịch lý: dùng ipratropium hoặc corticosteroid, tránh dùng SABA",
                "Hỗ trợ tim mạch nếu cần (IV fluids, vasopressors nếu hạ huyết áp)",
                "Theo dõi và điều trị triệu chứng"
            ],
            "monitoring": "Theo dõi liên tục: nhịp tim, huyết áp, ECG, SpO2, kali máu, đường huyết, đáp ứng phế quản. Theo dõi ít nhất 12-24 giờ do thời gian bán thải dài (5.5 giờ)."
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "agent": "Beta-blocker chọn lọc beta-1 (Atenolol, Metoprolol)",
                    "mechanism": "Đối kháng tác dụng beta-adrenergic, giảm tác dụng tim mạch",
                    "indication": "Quá liều gây nhịp tim nhanh nghiêm trọng, loạn nhịp tim",
                    "caution": "Thận trọng vì có thể làm nặng co thắt phế quản. Chỉ dùng khi tác dụng tim mạch nghiêm trọng và có hỗ trợ hô hấp sẵn sàng."
                }
            ],
            "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Beta-blocker chọn lọc beta-1 có thể được dùng để đối kháng tác dụng tim mạch nhưng thận trọng."
        },
        "administration_instructions": {
            "oral": None,
            "iv": None,
            "inhalation": {
                "technique": "Dùng dạng hít (MDI hoặc DPI). Lắc kỹ trước khi dùng (nếu MDI). Hít sâu và giữ hơi thở 10 giây. Đợi 30-60 giây trước khi dùng liều thứ hai (nếu cần).",
                "timing": "Dùng 2 lần/ngày (sáng và tối), cách nhau khoảng 12 giờ. Dùng đều đặn hàng ngày, không phải khi cần.",
                "with_ics": "PHẢI dùng kết hợp với ICS (inhaled corticosteroid). Có thể dùng riêng hoặc dùng dạng fixed-dose combination (Seretide/Advair: fluticasone + salmeterol).",
                "after_use": "Súc miệng và súc họng sau mỗi lần dùng để giảm kích ứng và tránh nấm miệng (đặc biệt nếu dùng với ICS).",
                "notes": "Không dùng để cắt cơn (tác dụng chậm). Luôn có SABA (salbutamol) sẵn sàng để cắt cơn. Nếu cần dùng SABA thường xuyên → cần đánh giá lại điều trị."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Label: Serevent (Salmeterol)",
                "UpToDate: Long-acting beta-2 agonists in asthma",
                "GINA Guidelines 2024: Asthma Management",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
                "Micromedex: Salmeterol"
            ],
            "last_updated": "2025-02-03",
            "evidence_level": "High - FDA approved, multiple RCTs, clinical guidelines"
        }
    },
    "Ipratropium": {
        "group": "Respiratory - Anticholinergic (Short-acting)",
        "vietnamese_name": "Ipratropium, Atrovent",
        "administration": ["Inhalation", "Nebulizer"],
        "indications": [
            "COPD (cắt cơn và phòng ngừa)",
            "Hen phế quản (kết hợp với SABA)",
            "Co thắt phế quản",
            "Chảy nước mũi (dạng xịt mũi)"
        ],
        "contraindications": [
            "Dị ứng atropine/ipratropium",
            "Glaucoma góc đóng",
            "Tăng nhãn áp"
        ],
        "dosage": {
            "adult_inhalation": "1-2 puffs (20-40mcg) mỗi 6-8 giờ",
            "adult_nebulizer": "250-500mcg mỗi 6-8 giờ",
            "adult_max": "12 puffs/ngày hoặc 3 lần nebulizer/ngày",
            "notes": "Tác dụng sau 15-30 phút, kéo dài 4-6 giờ. An toàn hơn beta-agonist cho bệnh nhân tim mạch"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Khô miệng",
            "Đắng miệng",
            "Ho",
            "Kích ứng mắt (nếu vào mắt)",
            "Tăng nhãn áp (nếu vào mắt)",
            "Bí tiểu (hiếm)"
        ],
        "interactions": [
            "Anticholinergic khác: tăng tác dụng phụ",
            "Beta-agonist: hiệp đồng tốt"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Anticholinergic - ức chế muscarinic receptors (M1, M2, M3) ở cơ trơn phế quản, giảm acetylcholine-mediated co thắt phế quản. Giãn cơ trơn phế quản, giảm tiết dịch đường hô hấp. Không hấp thu hệ thống đáng kể khi dùng dạng hít (do ion hóa) → ít tác dụng phụ hệ thống hơn atropine. Tác dụng ngắn (4-6 giờ). An toàn hơn beta-agonist cho bệnh nhân tim mạch (không kích thích beta-1 receptors).",
        "monitoring": [
            "Đáp ứng phế quản (peak flow, FEV1)",
            "Nhịp tim, huyết áp (ít tác dụng tim mạch hơn beta-agonist)",
            "Dấu hiệu kích ứng mắt (nếu vào mắt - tăng nhãn áp, đỏ mắt)",
            "Dấu hiệu tăng nhãn áp (đau mắt, nhìn mờ) - đặc biệt ở bệnh nhân glaucoma",
            "Dấu hiệu bí tiểu (khó tiểu, đầy bụng) - hiếm nhưng cần chú ý",
            "Dấu hiệu khô miệng nặng (có thể ảnh hưởng sức khỏe răng miệng)"
        ],
        "precautions": [
            "Rửa miệng sau khi dùng để giảm kích ứng và tránh thuốc vào mắt",
            "Tránh để thuốc vào mắt (có thể gây tăng nhãn áp, đặc biệt ở bệnh nhân glaucoma)",
            "Thận trọng ở bệnh nhân glaucoma góc đóng (chống chỉ định) hoặc tăng nhãn áp",
            "Thận trọng ở bệnh nhân phì đại tuyến tiền liệt (có thể gây bí tiểu)",
            "Kết hợp với beta-agonist (SABA) cho hiệu quả tốt hơn - hiệp đồng tác dụng",
            "Dùng đều đặn cho COPD, dùng khi cần cho hen (kết hợp với SABA)",
            "Dạng hít: sử dụng đúng kỹ thuật để đạt hiệu quả tối đa",
            "Dạng nebulizer: phù hợp cho bệnh nhân không thể dùng dạng hít",
            "An toàn hơn beta-agonist cho bệnh nhân tim mạch (không kích thích tim)"
        ],
        "pharmacokinetics": {
            "half_life": "2 giờ",
            "onset": "15-30 phút (chậm hơn SABA)",
            "duration": "4-6 giờ",
            "protein_binding": "Không đáng kể (ion hóa, không hấp thu hệ thống)",
            "clearance": "Chủ yếu tại chỗ (phế quản), không chuyển hóa đáng kể"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh nhiệt độ cao, tránh ánh sáng trực tiếp. Không làm lạnh. Kiểm tra hạn sử dụng định kỳ.",
        "black_box_warnings": "Tránh để thuốc vào mắt - có thể gây tăng nhãn áp, đặc biệt nguy hiểm ở bệnh nhân glaucoma góc đóng. Rửa miệng sau khi dùng để tránh thuốc vào mắt.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Anticholinergic khác (Atropine, Scopolamine, Benztropine, Oxybutynin)",
                    "mechanism": "Tăng tác dụng anticholinergic, tăng tác dụng phụ anticholinergic",
                    "effect": "Tăng khô miệng, bí tiểu, táo bón, tăng nhãn áp, nhìn mờ, nhịp tim nhanh",
                    "management": "Thận trọng khi dùng cùng. Theo dõi tác dụng phụ anticholinergic. Có thể cần giảm liều hoặc tránh dùng cùng."
                }
            ],
            "minor": [
                {
                    "drug": "Beta-agonist (Salbutamol, Salmeterol)",
                    "mechanism": "Hiệp đồng tác dụng giãn phế quản",
                    "effect": "Tăng hiệu quả giãn phế quản (tác dụng tích cực)",
                    "management": "Có thể dùng kết hợp để tăng hiệu quả. Không cần điều chỉnh liều."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Dị ứng với ipratropium, atropine hoặc các thành phần khác",
                "Glaucoma góc đóng (chống chỉ định tuyệt đối)",
                "Tăng nhãn áp nặng không kiểm soát"
            ],
            "relative": [
                "Glaucoma góc mở - thận trọng, theo dõi nhãn áp",
                "Tăng nhãn áp nhẹ - thận trọng, tránh để thuốc vào mắt",
                "Phì đại tuyến tiền liệt - có thể gây bí tiểu",
                "Bí tiểu - có thể làm nặng",
                "Táo bón nặng - có thể làm nặng",
                "Nhược cơ - có thể làm nặng",
                "Dùng với anticholinergic khác - tăng tác dụng phụ"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Ipratropium là thuốc phân loại B. Các nghiên cứu trên động vật không cho thấy nguy cơ cho thai nhi, nhưng không có nghiên cứu đầy đủ trên người. Ipratropium được sử dụng rộng rãi trong thai kỳ để điều trị COPD và hen, và có vẻ an toàn. Hấp thu toàn thân rất ít từ dạng hít (do ion hóa), nên tác dụng toàn thân tối thiểu. Có thể được dùng khi lợi ích vượt quá nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Ipratropium bài tiết rất ít vào sữa mẹ do hấp thu toàn thân tối thiểu từ dạng hít. Nồng độ trong sữa mẹ rất thấp, không đáng kể. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng an toàn khi cho con bú. Dạng hít được ưu tiên để giảm tác dụng toàn thân."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi",
            "notes": "Ipratropium không chuyển hóa đáng kể ở gan. Hấp thu toàn thân tối thiểu từ dạng hít. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Khô miệng nặng",
                "Bí tiểu",
                "Táo bón nặng",
                "Tăng nhãn áp (nếu vào mắt)",
                "Nhìn mờ",
                "Đỏ mắt, đau mắt",
                "Nhịp tim nhanh (hiếm, nếu hấp thu toàn thân)",
                "Kích động, lú lẫn (hiếm)",
                "Co giật (rất hiếm, chỉ khi hấp thu toàn thân lớn)"
            ],
            "antidote": "Không có antidote đặc hiệu. Physostigmine (cholinergic) có thể được dùng trong trường hợp quá liều nghiêm trọng với tác dụng toàn thân, nhưng thận trọng và chỉ dùng trong môi trường có hỗ trợ hô hấp.",
            "treatment": [
                "Ngừng ngay ipratropium",
                "Rửa mắt ngay nếu thuốc vào mắt (dùng nước sạch hoặc nước muối sinh lý)",
                "Điều trị tăng nhãn áp nếu có (dùng thuốc nhỏ mắt chống tăng nhãn áp, khám bác sĩ mắt)",
                "Hỗ trợ bí tiểu nếu cần (đặt ống thông tiểu)",
                "Điều trị táo bón nếu cần (thuốc nhuận tràng, thụt tháo)",
                "Theo dõi nhãn áp nếu có triệu chứng mắt",
                "Theo dõi nhịp tim, huyết áp nếu có triệu chứng toàn thân",
                "Hỗ trợ hô hấp nếu cần (hiếm)",
                "Physostigmine chỉ dùng trong trường hợp quá liều nghiêm trọng với tác dụng toàn thân (thận trọng, có hỗ trợ hô hấp)"
            ],
            "monitoring": "Theo dõi: nhãn áp (nếu có triệu chứng mắt), nhịp tim, huyết áp, tình trạng bí tiểu, táo bón. Theo dõi ít nhất 4-6 giờ do thời gian tác dụng (4-6 giờ)."
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "agent": "Physostigmine",
                    "mechanism": "Ức chế acetylcholinesterase, tăng acetylcholine, đối kháng tác dụng anticholinergic",
                    "indication": "Quá liều nghiêm trọng với tác dụng toàn thân (hiếm với ipratropium dạng hít)",
                    "caution": "Thận trọng, chỉ dùng trong môi trường có hỗ trợ hô hấp. Có thể gây co thắt phế quản, tăng tiết dịch, co giật. Chỉ dùng khi quá liều nghiêm trọng với tác dụng toàn thân."
                }
            ],
            "notes": "Không có antidote đặc hiệu cho ipratropium. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Physostigmine chỉ dùng trong trường hợp quá liều nghiêm trọng với tác dụng toàn thân (rất hiếm với dạng hít)."
        },
        "administration_instructions": {
            "oral": None,
            "iv": None,
            "inhalation": {
                "technique": "Dạng hít (MDI): Lắc kỹ trước khi dùng. Hít sâu và giữ hơi thở 10 giây. Đợi 30-60 giây trước khi dùng liều thứ hai (nếu cần).",
                "timing": "Dùng mỗi 6-8 giờ khi cần (PRN) hoặc đều đặn cho COPD. Tối đa 12 puffs/ngày.",
                "after_use": "Súc miệng và súc họng sau mỗi lần dùng để giảm kích ứng và QUAN TRỌNG: tránh thuốc vào mắt (có thể gây tăng nhãn áp).",
                "with_saba": "Có thể dùng kết hợp với beta-agonist (SABA) cho hiệu quả tốt hơn - hiệp đồng tác dụng.",
                "notes": "Tránh để thuốc vào mắt - rửa tay sau khi dùng. Nếu thuốc vào mắt, rửa ngay bằng nước sạch. Dạng nebulizer: phù hợp cho bệnh nhân không thể dùng dạng hít."
            },
            "nebulizer": {
                "reconstitution": "Dùng dung dịch ipratropium 0.025% (250mcg/ml). Liều thường: 0.5-1ml (125-250mcg) pha với 2-4ml nước muối sinh lý.",
                "administration": "Dùng qua nebulizer, thở bình thường trong 10-15 phút cho đến khi hết thuốc.",
                "timing": "Mỗi 6-8 giờ khi cần hoặc đều đặn cho COPD. Tối đa 3 lần/ngày.",
                "after_use": "Súc miệng sau khi dùng. Rửa tay để tránh thuốc vào mắt."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Label: Atrovent (Ipratropium)",
                "UpToDate: Anticholinergic bronchodilators in COPD",
                "GOLD Guidelines 2024: COPD Management",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
                "Micromedex: Ipratropium"
            ],
            "last_updated": "2025-02-03",
            "evidence_level": "High - FDA approved, multiple RCTs, clinical guidelines"
        }
    },
    "Tiotropium": {
        "group": "Respiratory - Anticholinergic (Long-acting)",
        "vietnamese_name": "Tiotropium, Spiriva",
        "administration": ["Inhalation (HandiHaler hoặc Respimat)"],
        "indications": [
            "COPD (phòng ngừa)",
            "Hen phế quản (kết hợp với ICS, nếu không kiểm soát)"
        ],
        "contraindications": [
            "Dị ứng atropine/tiotropium",
            "Glaucoma góc đóng",
            "Tăng nhãn áp",
            "Phì đại tuyến tiền liệt nặng"
        ],
        "dosage": {
            "adult_handihaler": "18mcg x 1 lần/ngày",
            "adult_respimat": "5mcg x 2 lần/ngày (sáng và tối)",
            "notes": "Tác dụng kéo dài 24 giờ. Dùng 1 lần/ngày với HandiHaler"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng",
            "under_30": "Tránh dùng (thải qua thận)"
        },
        "side_effects": [
            "Khô miệng (thường gặp)",
            "Ho",
            "Nhiễm trùng đường hô hấp trên",
            "Táo bón",
            "Bí tiểu",
            "Kích ứng mắt (nếu vào mắt)"
        ],
        "interactions": [
            "Anticholinergic khác: tăng tác dụng phụ",
            "Beta-agonist: hiệp đồng"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Anticholinergic dài tác dụng - ức chế muscarinic receptors (M1, M2, M3) ở cơ trơn phế quản, giảm acetylcholine-mediated co thắt phế quản. Giãn cơ trơn phế quản, giảm tiết dịch đường hô hấp. Liên kết chặt với M3 receptors (chủ yếu) và M1 receptors, giải phóng chậm → tác dụng kéo dài 24 giờ. Không hấp thu hệ thống đáng kể khi dùng dạng hít (do ion hóa) → ít tác dụng phụ hệ thống. Tác dụng dài hơn ipratropium (4-6 giờ so với 24 giờ). An toàn hơn beta-agonist cho bệnh nhân tim mạch.",
        "monitoring": [
            "Đáp ứng phế quản (peak flow, FEV1) - đánh giá hiệu quả phòng ngừa",
            "Nhịp tim, huyết áp (ít tác dụng tim mạch hơn beta-agonist)",
            "Dấu hiệu kích ứng mắt (nếu vào mắt - tăng nhãn áp, đỏ mắt)",
            "Dấu hiệu tăng nhãn áp (đau mắt, nhìn mờ) - đặc biệt ở bệnh nhân glaucoma",
            "Dấu hiệu bí tiểu (khó tiểu, đầy bụng) - đặc biệt ở bệnh nhân phì đại tuyến tiền liệt",
            "Dấu hiệu khô miệng nặng (có thể ảnh hưởng sức khỏe răng miệng)",
            "Chức năng thận (thải qua thận, tích lũy ở suy thận)"
        ],
        "precautions": [
            "Rửa miệng sau khi dùng để giảm kích ứng và tránh thuốc vào mắt",
            "Tránh để thuốc vào mắt (có thể gây tăng nhãn áp, đặc biệt ở bệnh nhân glaucoma)",
            "Thận trọng ở bệnh nhân glaucoma góc đóng (chống chỉ định) hoặc tăng nhãn áp",
            "Thận trọng ở bệnh nhân phì đại tuyến tiền liệt nặng (có thể gây bí tiểu)",
            "Thận trọng ở suy thận (thải qua thận, tích lũy) - tránh dùng nếu CrCl <30",
            "Dùng 1 lần/ngày với HandiHaler (18mcg) hoặc 2 lần/ngày với Respimat (5mcg)",
            "Kết hợp với ICS cho hen phế quản nếu không kiểm soát",
            "Dạng hít: sử dụng đúng kỹ thuật để đạt hiệu quả tối đa",
            "An toàn hơn beta-agonist cho bệnh nhân tim mạch (không kích thích tim)",
            "Không dùng để cắt cơn (tác dụng chậm) - cần có SABA để cắt cơn"
        ],
        "pharmacokinetics": {
            "half_life": "5-6 ngày (rất dài, do liên kết chặt với receptor)",
            "onset": "30-60 phút",
            "duration": "24 giờ (dài)",
            "protein_binding": "72%",
            "clearance": "Thận (thải qua thận, tích lũy ở suy thận)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh nhiệt độ cao, tránh ánh sáng trực tiếp. Không làm lạnh. HandiHaler: bảo quản trong bao bì gốc. Kiểm tra hạn sử dụng định kỳ.",
        "black_box_warnings": "Tránh để thuốc vào mắt - có thể gây tăng nhãn áp, đặc biệt nguy hiểm ở bệnh nhân glaucoma góc đóng. Rửa miệng sau khi dùng để tránh thuốc vào mắt. Thận trọng ở suy thận - tích lũy có thể gây tăng tác dụng phụ.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Anticholinergic khác (Atropine, Scopolamine, Benztropine, Oxybutynin, Ipratropium)",
                    "mechanism": "Tăng tác dụng anticholinergic, tăng tác dụng phụ anticholinergic",
                    "effect": "Tăng khô miệng, bí tiểu, táo bón, tăng nhãn áp, nhìn mờ",
                    "management": "Thận trọng khi dùng cùng. Theo dõi tác dụng phụ anticholinergic. Có thể cần giảm liều hoặc tránh dùng cùng."
                }
            ],
            "minor": [
                {
                    "drug": "Beta-agonist (Salbutamol, Salmeterol)",
                    "mechanism": "Hiệp đồng tác dụng giãn phế quản",
                    "effect": "Tăng hiệu quả giãn phế quản (tác dụng tích cực)",
                    "management": "Có thể dùng kết hợp để tăng hiệu quả. Không cần điều chỉnh liều."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Dị ứng với tiotropium, atropine hoặc các thành phần khác",
                "Glaucoma góc đóng (chống chỉ định tuyệt đối)",
                "Tăng nhãn áp nặng không kiểm soát",
                "Suy thận nặng (CrCl <30 ml/min) - tích lũy, tăng tác dụng phụ"
            ],
            "relative": [
                "Glaucoma góc mở - thận trọng, theo dõi nhãn áp",
                "Tăng nhãn áp nhẹ - thận trọng, tránh để thuốc vào mắt",
                "Phì đại tuyến tiền liệt nặng - có thể gây bí tiểu",
                "Bí tiểu - có thể làm nặng",
                "Táo bón nặng - có thể làm nặng",
                "Suy thận trung bình (CrCl 30-60 ml/min) - thận trọng, theo dõi tác dụng phụ",
                "Nhược cơ - có thể làm nặng",
                "Dùng với anticholinergic khác - tăng tác dụng phụ"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Tiotropium là thuốc phân loại C. Các nghiên cứu trên động vật cho thấy có thể có tác dụng phụ trên thai nhi, nhưng không có nghiên cứu đầy đủ trên người. Tiotropium được sử dụng trong thai kỳ để điều trị COPD và có vẻ an toàn. Hấp thu toàn thân ít từ dạng hít (do ion hóa), nên tác dụng toàn thân tối thiểu. Tuy nhiên, tiotropium thải qua thận và có thời gian bán thải rất dài (5-6 ngày), nên có thể tích lũy. Có thể được dùng khi lợi ích vượt quá nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Tiotropium bài tiết ít vào sữa mẹ do hấp thu toàn thân tối thiểu từ dạng hít. Nồng độ trong sữa mẹ rất thấp, không đáng kể. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng an toàn khi cho con bú. Dạng hít được ưu tiên để giảm tác dụng toàn thân."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi",
            "notes": "Tiotropium không chuyển hóa đáng kể ở gan. Hấp thu toàn thân tối thiểu từ dạng hít. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Khô miệng nặng",
                "Bí tiểu",
                "Táo bón nặng",
                "Tăng nhãn áp (nếu vào mắt)",
                "Nhìn mờ",
                "Đỏ mắt, đau mắt",
                "Nhịp tim nhanh (hiếm, nếu hấp thu toàn thân)",
                "Kích động, lú lẫn (hiếm)",
                "Co giật (rất hiếm, chỉ khi hấp thu toàn thân lớn)"
            ],
            "antidote": "Không có antidote đặc hiệu. Physostigmine (cholinergic) có thể được dùng trong trường hợp quá liều nghiêm trọng với tác dụng toàn thân, nhưng thận trọng và chỉ dùng trong môi trường có hỗ trợ hô hấp.",
            "treatment": [
                "Ngừng ngay tiotropium",
                "Rửa mắt ngay nếu thuốc vào mắt (dùng nước sạch hoặc nước muối sinh lý)",
                "Điều trị tăng nhãn áp nếu có (dùng thuốc nhỏ mắt chống tăng nhãn áp, khám bác sĩ mắt)",
                "Hỗ trợ bí tiểu nếu cần (đặt ống thông tiểu)",
                "Điều trị táo bón nếu cần (thuốc nhuận tràng, thụt tháo)",
                "Theo dõi nhãn áp nếu có triệu chứng mắt",
                "Theo dõi nhịp tim, huyết áp nếu có triệu chứng toàn thân",
                "Hỗ trợ hô hấp nếu cần (hiếm)",
                "Physostigmine chỉ dùng trong trường hợp quá liều nghiêm trọng với tác dụng toàn thân (thận trọng, có hỗ trợ hô hấp)",
                "Lưu ý: Thời gian bán thải rất dài (5-6 ngày) → theo dõi kéo dài"
            ],
            "monitoring": "Theo dõi: nhãn áp (nếu có triệu chứng mắt), nhịp tim, huyết áp, tình trạng bí tiểu, táo bón, chức năng thận. Theo dõi ít nhất 24 giờ, nhưng có thể cần theo dõi lâu hơn do thời gian bán thải rất dài (5-6 ngày)."
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "agent": "Physostigmine",
                    "mechanism": "Ức chế acetylcholinesterase, tăng acetylcholine, đối kháng tác dụng anticholinergic",
                    "indication": "Quá liều nghiêm trọng với tác dụng toàn thân (hiếm với tiotropium dạng hít)",
                    "caution": "Thận trọng, chỉ dùng trong môi trường có hỗ trợ hô hấp. Có thể gây co thắt phế quản, tăng tiết dịch, co giật. Chỉ dùng khi quá liều nghiêm trọng với tác dụng toàn thân."
                }
            ],
            "notes": "Không có antidote đặc hiệu cho tiotropium. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Physostigmine chỉ dùng trong trường hợp quá liều nghiêm trọng với tác dụng toàn thân (rất hiếm với dạng hít). Lưu ý: Thời gian bán thải rất dài (5-6 ngày) → tác dụng có thể kéo dài."
        },
        "administration_instructions": {
            "oral": None,
            "iv": None,
            "inhalation": {
                "handihaler": {
                    "technique": "HandiHaler: Mở nắp, đặt capsule vào buồng, đóng nắp, nhấn nút để đâm thủng capsule, hít sâu và giữ hơi thở 10 giây. Dùng 1 lần/ngày (18mcg).",
                    "timing": "Dùng 1 lần/ngày, tốt nhất vào buổi sáng, cách nhau 24 giờ.",
                    "after_use": "Súc miệng và súc họng sau mỗi lần dùng để giảm kích ứng và QUAN TRỌNG: tránh thuốc vào mắt (có thể gây tăng nhãn áp)."
                },
                "respimat": {
                    "technique": "Respimat: Xoay nắp để mở, xoay base để nạp thuốc, nhấn nút để phun thuốc, hít sâu và giữ hơi thở 10 giây. Dùng 2 lần/ngày (5mcg mỗi lần).",
                    "timing": "Dùng 2 lần/ngày (sáng và tối), cách nhau khoảng 12 giờ.",
                    "after_use": "Súc miệng và súc họng sau mỗi lần dùng để giảm kích ứng và QUAN TRỌNG: tránh thuốc vào mắt (có thể gây tăng nhãn áp)."
                },
                "notes": "Tránh để thuốc vào mắt - rửa tay sau khi dùng. Nếu thuốc vào mắt, rửa ngay bằng nước sạch. Không dùng để cắt cơn (tác dụng chậm) - cần có SABA để cắt cơn. Thận trọng ở suy thận (CrCl <30) - tránh dùng hoặc giảm liều."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Label: Spiriva (Tiotropium)",
                "UpToDate: Long-acting anticholinergic bronchodilators in COPD",
                "GOLD Guidelines 2024: COPD Management",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
                "Micromedex: Tiotropium"
            ],
            "last_updated": "2025-02-03",
            "evidence_level": "High - FDA approved, multiple RCTs, clinical guidelines"
        }
    },
    "Budesonide inhaled": {
        "group": "Respiratory - Inhaled Corticosteroid (ICS)",
        "vietnamese_name": "Budesonide, Pulmicort",
        "administration": ["Inhalation", "Nebulizer"],
        "indications": [
            "Hen phế quản (kiểm soát, phòng ngừa)",
            "COPD (nếu có nhiều đợt cấp)",
            "Viêm phế quản co thắt"
        ],
        "contraindications": [
            "Nhiễm trùng đường hô hấp nặng chưa điều trị",
            "Dị ứng"
        ],
        "dosage": {
            "adult_inhalation_low": "200-400mcg x 2 lần/ngày",
            "adult_inhalation_medium": "400-800mcg x 2 lần/ngày",
            "adult_inhalation_high": "800-1600mcg x 2 lần/ngày",
            "adult_nebulizer": "0.5-1mg x 2 lần/ngày",
            "notes": "Súc miệng sau khi dùng để tránh nấm miệng. Không dùng cho cắt cơn cấp"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Nấm miệng (candidiasis)",
            "Khàn tiếng",
            "Ho",
            "Khô miệng",
            "Tác dụng toàn thân (liều cao)",
            "Ức chế trục hạ đồi-tuyến yên-thượng thận (liều cao)"
        ],
        "interactions": [
            "Ritonavir: tăng nồng độ budesonide (tránh dùng)",
            "Ketoconazole/Itraconazole: tăng nồng độ"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Budesonide là corticosteroid hít (inhaled corticosteroid, ICS) có tác dụng kháng viêm mạnh tại chỗ. Budesonide gắn vào glucocorticoid receptor trong tế bào, sau đó di chuyển vào nhân và gắn vào glucocorticoid response elements (GRE) trên DNA, kích hoạt hoặc ức chế biểu hiện gen. Dẫn đến: ức chế tổng hợp các cytokine gây viêm (IL-1, IL-2, IL-4, IL-5, TNF-α), giảm phóng thích các chất trung gian gây viêm từ mast cells và eosinophils, giảm thâm nhập tế bào viêm, giảm phù nề niêm mạc phế quản, và tăng số lượng beta-2 receptors. Budesonide có tác dụng chủ yếu tại chỗ (phế quản), ít hấp thu toàn thân nên ít tác dụng phụ toàn thân. Tuy nhiên, một phần nhỏ vẫn được hấp thu và có thể gây tác dụng toàn thân ở liều cao. Budesonide được chuyển hóa nhanh ở gan (first-pass metabolism cao) nên tác dụng toàn thân ít hơn so với corticosteroid uống.",
        "monitoring": [
            "Đáp ứng điều trị (giảm triệu chứng hen, tần suất cơn cấp, nhu cầu dùng SABA)",
            "Nấm miệng (candidiasis) - kiểm tra lưỡi, miệng, đặc biệt nếu không súc miệng sau khi dùng",
            "Khàn tiếng, ho, kích ứng họng - tác dụng phụ tại chỗ phổ biến",
            "Tác dụng toàn thân (chỉ ở liều cao): ức chế trục HPA, chậm phát triển ở trẻ em, loãng xương, tăng huyết áp",
            "Chức năng gan nếu có triệu chứng (hiếm)",
            "Tương tác với ritonavir, ketoconazole, itraconazole (tăng nồng độ budesonide)"
        ],
        "precautions": [
            "Súc miệng và súc họng sau mỗi lần dùng để tránh nấm miệng (candidiasis) - QUAN TRỌNG",
            "Không dùng cho cắt cơn cấp - cần SABA (salbutamol) cho cơn cấp, budesonide là thuốc duy trì",
            "Tác dụng phát huy sau vài ngày đến vài tuần - không mong đợi tác dụng tức thì",
            "Không ngừng đột ngột - giảm liều dần dần",
            "Tác dụng toàn thân hiếm với liều thường nhưng có thể xảy ra ở liều cao (>1600mcg/ngày)",
            "Thận trọng với bệnh nhân lao phổi, nhiễm trùng đường hô hấp - cần điều trị nhiễm trùng trước",
            "Tránh dùng với ritonavir (tăng đáng kể nồng độ budesonide, tăng nguy cơ ức chế HPA)",
            "Thận trọng với ketoconazole, itraconazole (tăng nồng độ budesonide)",
            "Theo dõi chậm phát triển ở trẻ em nếu dùng liều cao",
            "Có thể dùng cho trẻ em (có dạng nebulizer)",
            "Dùng đều đặn hàng ngày, không phải khi cần"
        ],
        "pharmacokinetics": {
            "half_life": "2-3 giờ (trong phổi), 4-6 giờ (toàn thân sau hấp thu)",
            "onset": "Vài giờ đến vài ngày (tác dụng kháng viêm)",
            "duration": "12-24 giờ (dùng 2 lần/ngày)",
            "protein_binding": "88-90%",
            "clearance": "Gan: chuyển hóa nhanh qua CYP3A4 (first-pass metabolism cao, ~85-90% bị chuyển hóa). Thận: bài tiết một phần metabolites. Hấp thu toàn thân ít do chuyển hóa nhanh ở gan. Phần lớn tác dụng tại chỗ (phế quản)."
        },
        "storage": "Dạng hít (MDI/DPI): bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng trực tiếp. Không đông lạnh. Nebulizer suspension: bảo quản ở nhiệt độ phòng, lắc kỹ trước khi dùng, dùng trong vòng 2 giờ sau khi mở gói. Bảo quản trong tủ lạnh nếu không dùng ngay (2-8°C), để nhiệt độ phòng trước khi dùng.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "Ritonavir",
                    "mechanism": "Ức chế CYP3A4, tăng đáng kể nồng độ budesonide",
                    "effect": "Tăng nguy cơ ức chế trục HPA, hội chứng Cushing, suy thượng thận",
                    "management": "TRÁNH DÙNG với ritonavir. Nếu cần dùng, giảm liều budesonide đáng kể và theo dõi chặt chẽ."
                }
            ],
            "moderate": [
                {
                    "drug": "Ketoconazole, Itraconazole",
                    "mechanism": "Ức chế CYP3A4, tăng nồng độ budesonide",
                    "effect": "Tăng nguy cơ tác dụng toàn thân, ức chế HPA",
                    "management": "Thận trọng, theo dõi tác dụng toàn thân. Có thể cần giảm liều budesonide."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "absolute": [
                "Dị ứng với budesonide hoặc các thành phần khác",
                "Nhiễm trùng đường hô hấp nặng chưa điều trị (lao phổi, nấm)"
            ],
            "relative": [
                "Lao phổi - cần điều trị lao trước, thận trọng",
                "Nhiễm trùng đường hô hấp - cần điều trị nhiễm trùng trước",
                "Dùng với ritonavir - tránh dùng",
                "Dùng với ketoconazole, itraconazole - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Budesonide là thuốc phân loại C. Các nghiên cứu trên động vật cho thấy có thể có tác dụng phụ trên thai nhi, nhưng không có nghiên cứu đầy đủ trên người. Budesonide được sử dụng trong thai kỳ để điều trị hen và có vẻ an toàn. Hấp thu toàn thân ít từ dạng hít (do chuyển hóa nhanh ở gan), nên tác dụng toàn thân tối thiểu. Có thể được dùng khi lợi ích vượt quá nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Budesonide bài tiết ít vào sữa mẹ do hấp thu toàn thân tối thiểu từ dạng hít. Nồng độ trong sữa mẹ rất thấp, không đáng kể. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng an toàn khi cho con bú. Dạng hít được ưu tiên để giảm tác dụng toàn thân."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng - budesonide chuyển hóa qua CYP3A4 ở gan, có thể tích lũy ở suy gan nặng",
            "notes": "Budesonide chuyển hóa nhanh qua CYP3A4 ở gan. Ở suy gan nặng, có thể tích lũy và tăng tác dụng toàn thân. Theo dõi chặt chẽ tác dụng toàn thân. Có thể cần giảm liều."
        },
        "overdose_management": {
            "symptoms": [
                "Ức chế trục HPA (mệt mỏi, yếu, hạ huyết áp)",
                "Hội chứng Cushing (tăng cân, mặt tròn, tăng huyết áp)",
                "Tăng đường huyết",
                "Loãng xương (liều cao kéo dài)",
                "Chậm phát triển ở trẻ em (liều cao)",
                "Nấm miệng nặng",
                "Khàn tiếng nặng"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay budesonide hoặc giảm liều đáng kể",
                "Theo dõi chức năng trục HPA (cortisol, ACTH)",
                "Bổ sung corticosteroid nếu có suy thượng thận",
                "Điều trị tăng đường huyết nếu cần",
                "Theo dõi và điều trị triệu chứng"
            ],
            "monitoring": "Theo dõi: chức năng trục HPA (cortisol, ACTH), đường huyết, huyết áp, cân nặng, chiều cao (ở trẻ em). Theo dõi ít nhất vài tuần do tác dụng kéo dài."
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là ngừng thuốc, giảm liều, và hỗ trợ. Có thể cần bổ sung corticosteroid nếu có suy thượng thận."
        },
        "administration_instructions": {
            "oral": None,
            "iv": None,
            "inhalation": {
                "technique": "Dạng hít (MDI/DPI): Lắc kỹ trước khi dùng (nếu MDI). Hít sâu và giữ hơi thở 10 giây. Đợi 30-60 giây trước khi dùng liều thứ hai (nếu cần).",
                "timing": "Dùng 2 lần/ngày (sáng và tối), đều đặn hàng ngày, không phải khi cần.",
                "after_use": "Súc miệng và súc họng sau mỗi lần dùng để tránh nấm miệng (candidiasis) - QUAN TRỌNG.",
                "notes": "Không dùng cho cắt cơn cấp - cần SABA (salbutamol) cho cơn cấp. Tác dụng phát huy sau vài ngày đến vài tuần."
            },
            "nebulizer": {
                "reconstitution": "Dùng budesonide nebulizer suspension. Lắc kỹ trước khi dùng.",
                "administration": "Dùng qua nebulizer, thở bình thường trong 10-15 phút.",
                "timing": "Dùng 2 lần/ngày (sáng và tối). Dùng trong vòng 2 giờ sau khi mở gói.",
                "after_use": "Súc miệng sau khi dùng."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Label: Pulmicort (Budesonide)",
                "UpToDate: Inhaled corticosteroids in asthma",
                "GINA Guidelines 2024: Asthma Management",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
                "Micromedex: Budesonide"
            ],
            "last_updated": "2025-02-03",
            "evidence_level": "High - FDA approved, multiple RCTs, clinical guidelines"
        }
    },
    "Fluticasone inhaled": {
        "group": "Respiratory - Inhaled Corticosteroid (ICS)",
        "vietnamese_name": "Fluticasone, Flixotide",
        "administration": ["Inhalation"],
        "indications": [
            "Hen phế quản (kiểm soát, phòng ngừa)",
            "COPD (kết hợp với LABA nếu nhiều đợt cấp)"
        ],
        "contraindications": [
            "Nhiễm trùng đường hô hấp nặng",
            "Dị ứng"
        ],
        "dosage": {
            "adult_inhalation_low": "100-250mcg x 2 lần/ngày",
            "adult_inhalation_medium": "250-500mcg x 2 lần/ngày",
            "adult_inhalation_high": "500-1000mcg x 2 lần/ngày",
            "notes": "Súc miệng sau khi dùng. Thường dùng kết hợp với LABA (Salmeterol)"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Nấm miệng",
            "Khàn tiếng",
            "Ho",
            "Kích ứng cổ họng",
            "Tác dụng toàn thân (liều cao)",
            "Chậm phát triển ở trẻ em (liều cao)"
        ],
        "interactions": [
            "Ritonavir: tăng đáng kể nồng độ fluticasone - tránh dùng",
            "Ketoconazole: tăng nồng độ"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Fluticasone là corticosteroid hít (inhaled corticosteroid, ICS) có tác dụng kháng viêm mạnh tại chỗ. Fluticasone gắn vào glucocorticoid receptor trong tế bào, sau đó di chuyển vào nhân và gắn vào glucocorticoid response elements (GRE) trên DNA, kích hoạt hoặc ức chế biểu hiện gen. Dẫn đến: ức chế tổng hợp các cytokine gây viêm (IL-1, IL-2, IL-4, IL-5, TNF-α), giảm phóng thích các chất trung gian gây viêm từ mast cells và eosinophils, giảm thâm nhập tế bào viêm, giảm phù nề niêm mạc phế quản, và tăng số lượng beta-2 receptors. Fluticasone có tác dụng chủ yếu tại chỗ (phế quản), ít hấp thu toàn thân nên ít tác dụng phụ toàn thân. Tuy nhiên, một phần nhỏ vẫn được hấp thu và có thể gây tác dụng toàn thân ở liều cao. Fluticasone được chuyển hóa nhanh ở gan (first-pass metabolism cao) nhưng thời gian bán thải dài hơn budesonide. Thường dùng kết hợp với LABA (long-acting beta-2 agonist) như salmeterol trong dạng fixed-dose combination.",
        "monitoring": [
            "Đáp ứng điều trị (giảm triệu chứng hen, tần suất cơn cấp, nhu cầu dùng SABA)",
            "Nấm miệng (candidiasis) - kiểm tra lưỡi, miệng, đặc biệt nếu không súc miệng sau khi dùng",
            "Khàn tiếng, ho, kích ứng cổ họng - tác dụng phụ tại chỗ phổ biến",
            "Tác dụng toàn thân (chỉ ở liều cao): ức chế trục HPA, chậm phát triển ở trẻ em, loãng xương, tăng huyết áp",
            "Chức năng gan nếu có triệu chứng (hiếm)",
            "Tương tác với ritonavir (tăng đáng kể nồng độ), ketoconazole (tăng nồng độ)"
        ],
        "precautions": [
            "Súc miệng và súc họng sau mỗi lần dùng để tránh nấm miệng (candidiasis) - QUAN TRỌNG",
            "Không dùng cho cắt cơn cấp - cần SABA (salbutamol) cho cơn cấp, fluticasone là thuốc duy trì",
            "Tác dụng phát huy sau vài ngày đến vài tuần - không mong đợi tác dụng tức thì",
            "Không ngừng đột ngột - giảm liều dần dần",
            "Tác dụng toàn thân hiếm với liều thường nhưng có thể xảy ra ở liều cao (>1000mcg/ngày)",
            "Thận trọng với bệnh nhân lao phổi, nhiễm trùng đường hô hấp - cần điều trị nhiễm trùng trước",
            "TRÁNH DÙNG với ritonavir (tăng đáng kể nồng độ fluticasone, tăng nguy cơ ức chế HPA nghiêm trọng, có thể gây hội chứng Cushing)",
            "Thận trọng với ketoconazole, itraconazole (tăng nồng độ fluticasone)",
            "Theo dõi chậm phát triển ở trẻ em nếu dùng liều cao",
            "Thường dùng kết hợp với LABA (salmeterol) trong dạng fixed-dose combination (Seretide/Advair)",
            "Dùng đều đặn hàng ngày, không phải khi cần"
        ],
        "pharmacokinetics": {
            "half_life": "7-8 giờ (trong phổi), 13-17 giờ (toàn thân sau hấp thu)",
            "onset": "Vài giờ đến vài ngày (tác dụng kháng viêm)",
            "duration": "12-24 giờ (dùng 2 lần/ngày)",
            "protein_binding": "91%",
            "clearance": "Gan: chuyển hóa nhanh qua CYP3A4 (first-pass metabolism cao, ~99% bị chuyển hóa). Thận: bài tiết một phần metabolites. Hấp thu toàn thân ít do chuyển hóa nhanh ở gan. Phần lớn tác dụng tại chỗ (phế quản). Thời gian bán thải dài hơn budesonide."
        },
        "storage": "Dạng hít (MDI/DPI): bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng trực tiếp. Không đông lạnh. Kiểm tra xem có còn thuốc (lắc, nghe tiếng). Dạng fixed-dose combination với salmeterol: bảo quản tương tự.",
        "black_box_warnings": "TRÁNH DÙNG với ritonavir (tăng đáng kể nồng độ fluticasone, tăng nguy cơ ức chế trục HPA nghiêm trọng, có thể gây hội chứng Cushing, suy thượng thận). Nguy cơ chậm phát triển ở trẻ em với liều cao.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Ritonavir",
                    "mechanism": "Ức chế CYP3A4, tăng đáng kể nồng độ fluticasone",
                    "effect": "Tăng nguy cơ ức chế trục HPA nghiêm trọng, hội chứng Cushing, suy thượng thận",
                    "management": "TRÁNH DÙNG với ritonavir. Nếu cần dùng, giảm liều fluticasone đáng kể hoặc xem xét thuốc thay thế (budesonide). Theo dõi chặt chẽ."
                }
            ],
            "moderate": [
                {
                    "drug": "Ketoconazole, Itraconazole",
                    "mechanism": "Ức chế CYP3A4, tăng nồng độ fluticasone",
                    "effect": "Tăng nguy cơ tác dụng toàn thân, ức chế HPA",
                    "management": "Thận trọng, theo dõi tác dụng toàn thân. Có thể cần giảm liều fluticasone."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "absolute": [
                "Dị ứng với fluticasone hoặc các thành phần khác",
                "Nhiễm trùng đường hô hấp nặng chưa điều trị (lao phổi, nấm)",
                "Dùng với ritonavir - chống chỉ định tuyệt đối"
            ],
            "relative": [
                "Lao phổi - cần điều trị lao trước, thận trọng",
                "Nhiễm trùng đường hô hấp - cần điều trị nhiễm trùng trước",
                "Dùng với ketoconazole, itraconazole - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Fluticasone là thuốc phân loại C. Các nghiên cứu trên động vật cho thấy có thể có tác dụng phụ trên thai nhi, nhưng không có nghiên cứu đầy đủ trên người. Fluticasone được sử dụng trong thai kỳ để điều trị hen và có vẻ an toàn. Hấp thu toàn thân ít từ dạng hít (do chuyển hóa nhanh ở gan), nên tác dụng toàn thân tối thiểu. Có thể được dùng khi lợi ích vượt quá nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Fluticasone bài tiết ít vào sữa mẹ do hấp thu toàn thân tối thiểu từ dạng hít. Nồng độ trong sữa mẹ rất thấp, không đáng kể. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng an toàn khi cho con bú. Dạng hít được ưu tiên để giảm tác dụng toàn thân."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng - fluticasone chuyển hóa qua CYP3A4 ở gan, có thể tích lũy ở suy gan nặng",
            "notes": "Fluticasone chuyển hóa nhanh qua CYP3A4 ở gan. Ở suy gan nặng, có thể tích lũy và tăng tác dụng toàn thân. Theo dõi chặt chẽ tác dụng toàn thân. Có thể cần giảm liều."
        },
        "overdose_management": {
            "symptoms": [
                "Ức chế trục HPA (mệt mỏi, yếu, hạ huyết áp)",
                "Hội chứng Cushing (tăng cân, mặt tròn, tăng huyết áp)",
                "Tăng đường huyết",
                "Loãng xương (liều cao kéo dài)",
                "Chậm phát triển ở trẻ em (liều cao)",
                "Nấm miệng nặng",
                "Khàn tiếng nặng"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay fluticasone hoặc giảm liều đáng kể",
                "Theo dõi chức năng trục HPA (cortisol, ACTH)",
                "Bổ sung corticosteroid nếu có suy thượng thận",
                "Điều trị tăng đường huyết nếu cần",
                "Theo dõi và điều trị triệu chứng"
            ],
            "monitoring": "Theo dõi: chức năng trục HPA (cortisol, ACTH), đường huyết, huyết áp, cân nặng, chiều cao (ở trẻ em). Theo dõi ít nhất vài tuần do tác dụng kéo dài."
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là ngừng thuốc, giảm liều, và hỗ trợ. Có thể cần bổ sung corticosteroid nếu có suy thượng thận."
        },
        "administration_instructions": {
            "oral": None,
            "iv": None,
            "inhalation": {
                "technique": "Dạng hít (MDI/DPI): Lắc kỹ trước khi dùng (nếu MDI). Hít sâu và giữ hơi thở 10 giây. Đợi 30-60 giây trước khi dùng liều thứ hai (nếu cần).",
                "timing": "Dùng 2 lần/ngày (sáng và tối), đều đặn hàng ngày, không phải khi cần.",
                "after_use": "Súc miệng và súc họng sau mỗi lần dùng để tránh nấm miệng (candidiasis) - QUAN TRỌNG.",
                "with_laba": "Thường dùng kết hợp với LABA (salmeterol) trong dạng fixed-dose combination (Seretide/Advair).",
                "notes": "Không dùng cho cắt cơn cấp - cần SABA (salbutamol) cho cơn cấp. Tác dụng phát huy sau vài ngày đến vài tuần. TRÁNH DÙNG với ritonavir."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Label: Flixotide (Fluticasone)",
                "UpToDate: Inhaled corticosteroids in asthma",
                "GINA Guidelines 2024: Asthma Management",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
                "Micromedex: Fluticasone"
            ],
            "last_updated": "2025-02-03",
            "evidence_level": "High - FDA approved, multiple RCTs, clinical guidelines"
        }
    },

"Montelukast": {
    "group": "Respiratory - Leukotriene Receptor Antagonist",
    "vietnamese_name": "Montelukast, Singulair",
    "administration": ["PO"],
    "indications": [
        "Hen phế quản (phòng ngừa)",
        "Viêm mũi dị ứng",
        "Co thắt phế quản do gắng sức"
    ],
    "contraindications": [
        "Dị ứng montelukast"
    ],
    "dosage": {
        "adult": "10mg x 1 lần/ngày (buổi tối)",
        "pediatric_6_14": "5mg x 1 lần/ngày",
        "pediatric_2_5": "4mg x 1 lần/ngày",
        "notes": "Uống buổi tối, có thể uống với hoặc không thức ăn"
    },
    "side_effects": [
        "Nhức đầu",
        "Buồn nôn",
        "Tiêu chảy",
        "Rối loạn giấc ngủ",
        "Thay đổi tâm trạng (hiếm)",
        "Phản ứng tâm thần (rất hiếm)"
    ],
    "interactions": [
        "Phenobarbital: giảm nồng độ montelukast",
        "Rifampin: giảm nồng độ montelukast"
    ],
    "pregnancy": "B",
    "mechanism_of_action": "Montelukast là chất đối kháng chọn lọc thụ thể leukotriene D4 (LTD4), thuộc nhóm leukotriene receptor antagonist (LTRA). Leukotriene là các chất trung gian gây viêm được tổng hợp từ acid arachidonic qua con đường 5-lipoxygenase. Leukotriene D4 gắn vào CysLT1 receptor trên cơ trơn phế quản, mạch máu, và các tế bào viêm, gây co thắt phế quản, tăng tính thấm mạch máu, phù nề, và tăng tiết chất nhầy. Montelukast ức chế LTD4 gắn vào CysLT1 receptor, ngăn chặn các tác dụng này, từ đó giảm co thắt phế quản, giảm viêm, và giảm triệu chứng hen. Montelukast có tác dụng phòng ngừa hen, đặc biệt hen do dị ứng và hen do gắng sức. Không dùng cho cắt cơn cấp. Tác dụng phát huy sau vài giờ đến vài ngày, dùng hàng ngày để duy trì.",
    "monitoring": [
        "Đáp ứng điều trị (giảm triệu chứng hen, giảm tần suất cơn cấp, giảm nhu cầu dùng SABA)",
        "Rối loạn tâm thần (thay đổi tâm trạng, lo âu, trầm cảm, hành vi bất thường, ý nghĩ tự sát) - hiếm nhưng nghiêm trọng, đặc biệt ở trẻ em và thanh thiếu niên",
        "Rối loạn giấc ngủ (mất ngủ, ác mộng)",
        "Nhức đầu, buồn nôn, tiêu chảy - tác dụng phụ phổ biến nhưng thường nhẹ",
        "Chức năng gan nếu có triệu chứng (hiếm)",
        "Tương tác với phenobarbital, rifampin (giảm nồng độ montelukast)"
    ],
    "precautions": [
        "Rối loạn tâm thần - nguy cơ thay đổi tâm trạng, lo âu, trầm cảm, hành vi bất thường, ý nghĩ tự sát, đặc biệt ở trẻ em và thanh thiếu niên",
        "NGỪNG NGAY và liên hệ bác sĩ nếu có thay đổi tâm trạng, hành vi bất thường, ý nghĩ tự sát",
        "Không dùng cho cắt cơn cấp - cần SABA (salbutamol) cho cơn cấp, montelukast là thuốc phòng ngừa",
        "Tác dụng phát huy sau vài giờ đến vài ngày - không mong đợi tác dụng tức thì",
        "Dùng hàng ngày, tốt nhất vào buổi tối, có thể uống với hoặc không thức ăn",
        "Không thay thế ICS (inhaled corticosteroid) - có thể dùng kết hợp với ICS",
        "Hiệu quả với hen do dị ứng và hen do gắng sức",
        "Thận trọng với phenobarbital, rifampin (giảm nồng độ montelukast, có thể giảm hiệu quả)",
        "An toàn trong thai kỳ (category B)",
        "Có thể dùng cho trẻ em từ 2 tuổi trở lên (liều điều chỉnh theo tuổi)",
        "Theo dõi chặt chẽ ở trẻ em và thanh thiếu niên về rối loạn tâm thần"
    ],
    "pharmacokinetics": {
        "half_life": "2.7-5.5 giờ",
        "onset": "Vài giờ đến vài ngày (tác dụng phòng ngừa)",
        "duration": "24 giờ (dùng 1 lần/ngày)",
        "protein_binding": ">99%",
        "clearance": "Gan: chuyển hóa qua CYP2C8, CYP3A4, và CYP2C9 thành metabolites không hoạt động. Thận: bài tiết một phần nguyên dạng và metabolites. Tương tác với CYP inducers (phenobarbital, rifampin) có thể giảm nồng độ."
    },
    "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén/capsule: bảo quản trong bao bì kín. Dạng nhai: bảo quản ở nhiệt độ phòng, tránh ẩm. Dạng bột: bảo quản ở nhiệt độ phòng, pha với nước, thức ăn mềm, hoặc sữa công thức trước khi dùng.",
    "black_box_warnings": "Nguy cơ rối loạn tâm thần nghiêm trọng, bao gồm thay đổi tâm trạng, lo âu, trầm cảm, hành vi bất thường, và ý nghĩ tự sát. Nguy cơ tăng ở trẻ em và thanh thiếu niên. Ngừng ngay và liên hệ bác sĩ nếu có thay đổi tâm trạng, hành vi bất thường, hoặc ý nghĩ tự sát.",
    "drug_interactions": {
        "major": [],
        "moderate": [
            {
                "drug": "Phenobarbital",
                "mechanism": "Cảm ứng CYP2C8, CYP3A4, giảm nồng độ montelukast",
                "effect": "Giảm hiệu quả montelukast, có thể không kiểm soát được hen",
                "management": "Theo dõi đáp ứng điều trị. Có thể cần tăng liều montelukast hoặc xem xét thuốc thay thế."
            },
            {
                "drug": "Rifampin",
                "mechanism": "Cảm ứng CYP2C8, CYP3A4, giảm nồng độ montelukast",
                "effect": "Giảm hiệu quả montelukast, có thể không kiểm soát được hen",
                "management": "Theo dõi đáp ứng điều trị. Có thể cần tăng liều montelukast hoặc xem xét thuốc thay thế."
            }
        ],
        "minor": []
    },
    "contraindications": {
        "absolute": [
            "Dị ứng với montelukast hoặc các thành phần khác"
        ],
        "relative": [
            "Rối loạn tâm thần (trầm cảm, lo âu, rối loạn hành vi) - thận trọng, theo dõi chặt chẽ",
            "Tiền sử tự sát - thận trọng, theo dõi chặt chẽ",
            "Dùng với phenobarbital, rifampin - có thể giảm hiệu quả"
        ]
    },
    "pregnancy_lactation": {
        "fda_category": "B",
        "pregnancy_details": "Montelukast là thuốc phân loại B. Các nghiên cứu trên động vật không cho thấy nguy cơ cho thai nhi, nhưng không có nghiên cứu đầy đủ trên người. Montelukast được sử dụng trong thai kỳ để điều trị hen và có vẻ an toàn. Có thể được dùng khi lợi ích vượt quá nguy cơ.",
        "lactation": {
            "safety": "Compatible",
            "details": "Montelukast bài tiết vào sữa mẹ với nồng độ thấp. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ.",
            "recommendation": "Có thể dùng an toàn khi cho con bú."
        }
    },
    "hepatic_adjustment": {
        "mild": "Không đổi",
        "moderate": "Không đổi",
        "severe": "Không đổi",
        "notes": "Montelukast chuyển hóa qua gan (CYP2C8, CYP3A4, CYP2C9) nhưng không tích lũy ở suy gan. Không cần điều chỉnh liều ở suy gan."
    },
    "overdose_management": {
        "symptoms": [
            "Nhức đầu",
            "Buồn nôn, nôn",
            "Tiêu chảy",
            "Rối loạn giấc ngủ",
            "Thay đổi tâm trạng, kích động",
            "Rối loạn tâm thần (hiếm)"
        ],
        "antidote": "Không có antidote đặc hiệu",
        "treatment": [
            "Ngừng ngay montelukast",
            "Hỗ trợ và điều trị triệu chứng",
            "Theo dõi rối loạn tâm thần (đặc biệt ở trẻ em và thanh thiếu niên)",
            "Theo dõi chức năng gan nếu có triệu chứng"
        ],
        "monitoring": "Theo dõi: tâm trạng, hành vi, ý nghĩ tự sát (đặc biệt ở trẻ em và thanh thiếu niên), nhức đầu, buồn nôn, tiêu chảy, chức năng gan. Theo dõi ít nhất 24 giờ."
    },
    "reversal_agents": {
        "available": False,
        "agents": [],
        "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng."
    },
    "administration_instructions": {
        "oral": {
            "with_food": "Có thể uống với hoặc không thức ăn",
            "timing": "Uống 1 lần/ngày, tốt nhất vào buổi tối",
            "pediatric": "Trẻ em 6-14 tuổi: 5mg/ngày. Trẻ em 2-5 tuổi: 4mg/ngày. Dạng nhai hoặc bột."
        },
        "iv": None
    },
    "references": {
        "primary_sources": [
            "FDA Label: Singulair (Montelukast)",
            "UpToDate: Leukotriene receptor antagonists in asthma",
            "GINA Guidelines 2024: Asthma Management",
            "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
            "Micromedex: Montelukast"
        ],
        "last_updated": "2025-02-03",
        "evidence_level": "High - FDA approved, multiple RCTs, clinical guidelines"
    }
}
}

__all__ = ['RESPIRATORY_DRUGS']
