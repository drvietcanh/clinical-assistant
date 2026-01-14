"""
Hematology Drugs - Hemostatics
"""
from typing import Dict, Any


HEMOSTATICS_DRUGS: Dict[str, Dict[str, Any]] = {
        "Tranexamic acid": {
            "group": "Hematology - Antifibrinolytic Agent",
            "vietnamese_name": "Tranexamic acid, Acid tranexamic",
            "administration": ["PO", "IV"],
            "indications": [
                "Chảy máu nặng (trauma, phẫu thuật)",
                "Chảy máu kinh nguyệt nặng",
                "Chảy máu do rối loạn đông máu",
                "Chảy máu do thuốc chống đông",
                "Phẫu thuật tim mạch (giảm chảy máu)",
                "Chảy máu do fibrinogen thấp"
            ],
            "contraindications": [
                "Huyết khối đang hoạt động",
                "Tiền sử huyết khối",
                "Suy thận nặng (CrCl <30) - thận trọng",
                "Dị ứng tranexamic acid"
            ],
            "dosage": {
                "adult_iv_loading": "1g IV trong 10 phút",
                "adult_iv_maintenance": "1g IV mỗi 8 giờ",
                "adult_po": "1-1.5g PO x 3-4 lần/ngày",
                "adult_menorrhagia": "1g PO x 3 lần/ngày trong 3-5 ngày",
                "pediatric": "10mg/kg IV mỗi 8 giờ",
                "notes": "Điều chỉnh liều theo suy thận. Tối đa 4g/ngày."
            },
            "side_effects": [
                "Huyết khối (nguy cơ cao)",
                "Co giật (liều cao IV)",
                "Buồn nôn, nôn",
                "Tiêu chảy",
                "Nhìn mờ (hiếm)",
                "Phản ứng dị ứng (hiếm)"
            ],
            "interactions": [
                "Thuốc chống đông: tăng nguy cơ huyết khối",
                "Estrogen: tăng nguy cơ huyết khối",
                "Factor IX concentrates: tăng nguy cơ huyết khối"
            ],
        "pregnancy": "B",
            "mechanism_of_action": "Tranexamic acid là chất ức chế plasmin (antifibrinolytic), ngăn chặn quá trình tiêu sợi huyết (fibrinolysis). Tranexamic acid gắn với plasminogen và plasmin, ngăn chặn plasmin gắn với fibrin, do đó ức chế sự phân hủy fibrin và cục máu đông. Tranexamic acid được sử dụng để giảm chảy máu trong các tình huống chảy máu nặng, đặc biệt khi có tăng tiêu sợi huyết (hyperfibrinolysis). Thuốc có hiệu quả trong chảy máu kinh nguyệt nặng, chảy máu do trauma, và chảy máu trong phẫu thuật. Tuy nhiên, tranexamic acid làm tăng nguy cơ huyết khối do ức chế tiêu sợi huyết, nên không dùng ở bệnh nhân có nguy cơ huyết khối.",
            "monitoring": [
                "Dấu hiệu chảy máu (xem có giảm chảy máu)",
                "Dấu hiệu huyết khối (đau ngực, khó thở, đau chân, sưng chân) - NGUY CƠ CAO",
                "Chức năng thận (creatinine, eGFR) - cần điều chỉnh liều ở suy thận",
                "Dấu hiệu co giật (với liều cao IV)",
                "Thị lực (nhìn mờ, hiếm)"
            ],
            "precautions": [
                "NGUY CƠ HUYẾT KHỐI CAO - không dùng ở bệnh nhân có huyết khối đang hoạt động hoặc tiền sử huyết khối",
                "Điều chỉnh liều ở suy thận: CrCl 30-60 → giảm liều 50%, CrCl <30 → giảm liều 75%",
                "Thận trọng với bệnh nhân có nguy cơ huyết khối (ung thư, bất động, suy tim)",
                "Liều cao IV có thể gây co giật - không vượt quá 4g/ngày",
                "Không dùng quá 5 ngày liên tục (tăng nguy cơ huyết khối)",
                "Theo dõi sát dấu hiệu huyết khối",
                "Có thể dùng trong thai kỳ nếu cần thiết (category B)"
            ],
            "pharmacokinetics": {
                "half_life": "2-3 giờ",
                "onset": "Ngay lập tức (IV), 1-2 giờ (PO)",
                "duration": "6-8 giờ",
                "protein_binding": "3%",
                "clearance": "Thận: bài tiết chủ yếu qua thận (90% nguyên dạng). Cần điều chỉnh liều ở suy thận."
            },
            "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Dung dịch IV: bảo quản ở nhiệt độ phòng, tránh đông lạnh.",
            "black_box_warnings": "Nguy cơ huyết khối nghiêm trọng, có thể gây tử vong. Không dùng ở bệnh nhân có huyết khối đang hoạt động hoặc tiền sử huyết khối. Theo dõi sát dấu hiệu huyết khối.",
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["cardiovascular", "neurological"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Signs of thrombosis (CRITICAL - Black Box Warning)", "Renal function (CrCl - dose adjustment required)", "Seizure signs (high dose IV)", "Vision (rare)"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Thrombosis Risk (can be fatal)",
                "WHO Essential Medicines List",
                "CRASH-2 Trial - Trauma Bleeding",
                "WOMAN Trial - Postpartum Hemorrhage"
            ],
            "drug_interactions": {
                "major": [
                    {
                        "drug": "Thuốc chống đông (warfarin, heparin, DOACs)",
                        "mechanism": "Tác dụng đối kháng - tranexamic acid ức chế tiêu sợi huyết, làm tăng nguy cơ huyết khối",
                        "effect": "Tăng nguy cơ huyết khối nghiêm trọng",
                        "management": "Thận trọng. Thường tránh dùng cùng. Nếu cần thiết, theo dõi sát dấu hiệu huyết khối."
                    },
                    {
                        "drug": "Estrogen, Combined oral contraceptives",
                        "mechanism": "Cả hai đều tăng nguy cơ huyết khối",
                        "effect": "Tăng nguy cơ huyết khối nghiêm trọng",
                        "management": "Thận trọng. Thường tránh dùng cùng."
                    }
                ],
                "moderate": [
                    {
                        "drug": "Factor IX concentrates",
                        "mechanism": "Tăng nguy cơ huyết khối",
                        "effect": "Tăng nguy cơ huyết khối",
                        "management": "Thận trọng. Theo dõi sát."
                    }
                ],
                "minor": []
            },
            "contraindications": {
                "tuyệt_đối": [
                    "Huyết khối đang hoạt động",
                    "Tiền sử huyết khối",
                    "Dị ứng tranexamic acid"
                ],
                "tương_đối": [
                    "Suy thận nặng (CrCl <30) - thận trọng, giảm liều 75%",
                    "Bệnh nhân có nguy cơ huyết khối (ung thư, bất động, suy tim) - thận trọng",
                    "Liều cao IV - tăng nguy cơ co giật"
                ]
            },
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Huyết khối đang hoạt động",
                    "Tiền sử huyết khối",
                    "Dị ứng tranexamic acid"
                ],
                "tương_đối": [
                    "Suy thận nặng (CrCl <30) - thận trọng, giảm liều 75%",
                    "Bệnh nhân có nguy cơ huyết khối (ung thư, bất động, suy tim) - thận trọng",
                    "Liều cao IV - tăng nguy cơ co giật"
                ]
            },
            "renal_adjustment": {
                "normal": "Không cần chỉnh liều",
                "30_60": "Giảm liều 50%",
                "under_30": "Giảm liều 75%",
                "dialysis": "Giảm liều 75%. Tranexamic acid được lọc sạch qua thẩm phân máu, bổ sung liều sau lọc.",
                "notes": "Tranexamic acid thải trừ chủ yếu qua thận (90% nguyên dạng). Suy thận cần điều chỉnh liều rõ ràng."
            },
            "pregnancy_lactation": {
                "fda_category": "B",
                "pregnancy_details": "Có thể dùng trong thai kỳ nếu cần thiết. Tranexamic acid được sử dụng để điều trị chảy máu nặng trong thai kỳ.",
                "lactation": {
                    "safety": "Compatible",
                    "details": "Tranexamic acid bài tiết vào sữa mẹ ở nồng độ thấp. An toàn cho trẻ bú mẹ.",
                    "recommendation": "Có thể dùng khi cho con bú."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không đổi",
                "moderate": "Không đổi",
                "severe": "Không đổi",
                "notes": "Tranexamic acid không chuyển hóa ở gan. Suy gan không ảnh hưởng đến tranexamic acid."
            },
            "overdose_management": {
                "symptoms": [
                    "Co giật (liều cao IV)",
                    "Huyết khối (nguy cơ cao)",
                    "Buồn nôn, nôn nặng",
                    "Nhìn mờ"
                ],
                "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
                "treatment": [
                    "Ngừng tranexamic acid ngay lập tức",
                    "Điều trị co giật nếu có (benzodiazepines)",
                    "Theo dõi dấu hiệu huyết khối",
                    "Điều trị huyết khối nếu có",
                    "Theo dõi ít nhất 24 giờ"
                ],
                "monitoring": "Dấu hiệu huyết khối, co giật, thị lực"
            },
            "reversal_agents": {
                "available": False,
                "agents": []
            },
            "administration_instructions": {
                "oral": {
                    "with_food": "Có thể uống với hoặc không có thức ăn. Uống với thức ăn có thể giảm buồn nôn.",
                    "timing": "Dùng 3-4 lần/ngày. Tối đa 4g/ngày. Không dùng quá 5 ngày liên tục."
                },
                "iv": {
                    "reconstitution": "Pha loãng trong NS hoặc D5W (10mg/ml)",
                    "infusion_rate": "Tiêm IV trong 10 phút (loading), sau đó truyền chậm (maintenance)",
                    "compatibility": ["NS", "D5W"],
                    "incompatibility": [],
                    "notes": "Loading: 1g IV trong 10 phút. Maintenance: 1g IV mỗi 8 giờ. Tối đa 4g/ngày. Điều chỉnh liều ở suy thận."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Tranexamic acid",
                    "UpToDate - Tranexamic acid: Drug information",
                    "CRASH-2 Trial - Lancet (trauma bleeding)",
                    "WHO Guidelines - Postpartum hemorrhage"
                ],
                "last_updated": "2025-02-05",
                "evidence_level": "High - FDA-approved, large RCTs (CRASH-2, WOMAN trial)"
            }
        },

}

__all__ = ['HEMOSTATICS_DRUGS']
