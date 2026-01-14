"""
Hematology Drugs - Other Hematology
"""
from typing import Dict, Any


OTHER_HEMATOLOGY_DRUGS: Dict[str, Dict[str, Any]] = {
        "Emicizumab": {
            "group": "Hematology - Bispecific Monoclonal Antibody",
            "vietnamese_name": "Emicizumab, Hemlibra",
            "administration": ["SC"],
            "indications": [
                "Hemophilia A (với hoặc không có chất ức chế factor VIII)",
                "Phòng ngừa chảy máu ở bệnh nhân hemophilia A"
            ],
            "contraindications": [
                "Dị ứng emicizumab hoặc bất kỳ thành phần nào",
                "Đang có huyết khối đang hoạt động"
            ],
            "dosage": {
                "adult_loading": "3mg/kg SC tuần 1, 2, 4",
                "adult_maintenance": "1.5mg/kg SC mỗi tuần, hoặc 3mg/kg SC mỗi 2 tuần, hoặc 6mg/kg SC mỗi 4 tuần",
                "notes": "Tiêm dưới da (SC) ở vùng bụng, đùi, hoặc cánh tay. Có thể tự tiêm sau khi được hướng dẫn."
            },
            "renal_adjustment": {
                "normal": "Không cần chỉnh liều",
                "30_60": "Không cần chỉnh liều",
                "under_30": "Không cần chỉnh liều"
            },
            "side_effects": [
                "Phản ứng tại chỗ tiêm (đau, đỏ, ngứa) - phổ biến",
                "Nhức đầu",
                "Mệt mỏi",
                "Buồn nôn",
                "Tăng nguy cơ huyết khối (thrombosis) - hiếm nhưng nghiêm trọng, đặc biệt khi dùng với activated prothrombin complex concentrate (aPCC)",
                "Dị ứng (hiếm)"
            ],
            "interactions": [
                "Activated prothrombin complex concentrate (aPCC): tăng nguy cơ huyết khối nghiêm trọng",
                "Recombinant factor VIIa: có thể tăng nguy cơ huyết khối"
            ],
        "pregnancy": "C",
            "mechanism_of_action": (
                "Emicizumab là bispecific monoclonal antibody (humanized) gắn đồng thời với factor IXa và factor X. "
                "Trong hemophilia A, thiếu factor VIII dẫn đến không thể hình thành phức hợp tenase (factor VIIIa/factor IXa) "
                "cần thiết để kích hoạt factor X thành factor Xa, dẫn đến rối loạn đông máu và chảy máu. "
                "Emicizumab bắt chước chức năng của factor VIIIa bằng cách gắn với factor IXa và factor X, "
                "tạo thành phức hợp tương tự tenase mà không cần factor VIII. "
                "Dẫn đến: kích hoạt factor X thành factor Xa, hình thành thrombin, và đông máu bình thường. "
                "Emicizumab được dùng để phòng ngừa chảy máu ở bệnh nhân hemophilia A, "
                "đặc biệt hiệu quả ở bệnh nhân có chất ức chế factor VIII (kháng thể kháng factor VIII) "
                "vì các thuốc thay thế factor VIII truyền thống không hiệu quả ở những bệnh nhân này. "
                "Emicizumab có half-life dài, cho phép dùng 1-4 tuần một lần (tùy phác đồ)."
            ),
            "monitoring": [
                "Tần suất và mức độ nghiêm trọng của chảy máu (theo dõi nhật ký chảy máu)",
                "Phản ứng tại chỗ tiêm",
                "Dấu hiệu huyết khối (đau ngực, khó thở, đau chân, sưng chân) - đặc biệt khi dùng với aPCC",
                "Dấu hiệu dị ứng (phát ban, khó thở, phù mạch)",
                "Chức năng gan (ALT, AST) - theo dõi định kỳ"
            ],
            "precautions": [
                "NGUY CƠ HUYẾT KHỐI - đặc biệt khi dùng với activated prothrombin complex concentrate (aPCC), "
                "cần theo dõi chặt chẽ dấu hiệu huyết khối",
                "Tránh dùng aPCC với emicizumab nếu có thể - nếu cần dùng, dùng liều thấp nhất và theo dõi chặt chẽ",
                "Có thể tự tiêm sau khi được hướng dẫn đúng cách",
                "Không dùng để điều trị cấp tính chảy máu nặng (cần dùng factor VIII hoặc bypassing agents)",
                "Thận trọng ở bệnh nhân có tiền sử huyết khối",
                "Có thể mất vài tuần để đạt hiệu quả đầy đủ"
            ],
            "pharmacokinetics": {
                "half_life": "~4-5 tuần (rất dài, cho phép dùng 1-4 tuần một lần)",
                "onset": "Vài tuần (tác dụng chậm)",
                "duration": "Dài (do half-life rất dài)",
                "protein_binding": "IgG4 bispecific monoclonal antibody",
                "metabolism": "Chuyển hóa qua hệ thống reticuloendothelial (RES)",
                "clearance": "Không phụ thuộc gan thận đáng kể"
            },
            "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Có thể để ở nhiệt độ phòng (≤25°C) tối đa 7 ngày. Không làm nóng hoặc lắc mạnh.",
            "black_box_warnings": (
                "NGUY CƠ HUYẾT KHỐI - đặc biệt khi dùng với activated prothrombin complex concentrate (aPCC). "
                "Có báo cáo huyết khối tĩnh mạch sâu (DVT), thuyên tắc phổi (PE), và huyết khối động mạch. "
                "Tránh dùng aPCC với emicizumab nếu có thể. Nếu cần dùng, dùng liều thấp nhất và theo dõi chặt chẽ dấu hiệu huyết khối."
            ),
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["cardiovascular"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Signs of thrombosis (Black Box Warning - especially with aPCC)", "Injection site reactions", "Allergic reactions", "Liver function (ALT, AST)"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Thrombosis Risk (especially with aPCC)",
                "ASH Guidelines - Hemophilia A Treatment",
                "WHO Essential Medicines List"
            ],
            "drug_interactions": {
                "major": [
                    {
                        "drug": "Activated prothrombin complex concentrate (aPCC, FEIBA)",
                        "mechanism": "Tăng nguy cơ huyết khối khi dùng với emicizumab",
                        "effect": "Tăng nguy cơ huyết khối nghiêm trọng (DVT, PE, huyết khối động mạch)",
                        "management": "Tránh dùng nếu có thể. Nếu cần dùng, dùng liều thấp nhất (≤50 U/kg/24h) và theo dõi chặt chẽ dấu hiệu huyết khối."
                    },
                    {
                        "drug": "Recombinant factor VIIa (rFVIIa)",
                        "mechanism": "Có thể tăng nguy cơ huyết khối",
                        "effect": "Tăng nguy cơ huyết khối",
                        "management": "Thận trọng. Theo dõi chặt chẽ dấu hiệu huyết khối."
                    }
                ],
                "moderate": [],
                "minor": []
            },
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng emicizumab hoặc bất kỳ thành phần nào",
                    "Đang có huyết khối đang hoạt động"
                ],
                "tương_đối": [
                    "Tiền sử huyết khối - tăng nguy cơ huyết khối",
                    "Đang dùng aPCC - tăng nguy cơ huyết khối nghiêm trọng"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Dữ liệu hạn chế. Có thể dùng trong thai kỳ khi lợi ích vượt trội nguy cơ. Theo dõi chặt chẽ.",
                "lactation": {
                    "safety": "Unknown",
                    "details": "Chưa rõ bài tiết vào sữa mẹ. Kháng thể lớn, hấp thu qua đường tiêu hóa trẻ có thể hạn chế.",
                    "recommendation": "Cân nhắc ngừng cho bú hoặc không dùng thuốc."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh liều",
                "moderate": "Không cần chỉnh liều",
                "severe": "Không cần chỉnh liều",
                "notes": "Emicizumab chuyển hóa qua RES, không phụ thuộc gan đáng kể."
            },
            "overdose_management": {
                "symptoms": [
                    "Tăng nguy cơ huyết khối",
                    "Phản ứng tại chỗ tiêm nặng hơn",
                    "Dị ứng (hiếm)"
                ],
                "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
                "treatment": [
                    "Theo dõi dấu hiệu huyết khối chặt chẽ",
                    "Xử trí huyết khối nếu có (anticoagulation, thrombectomy nếu cần)",
                    "Xử trí phản ứng dị ứng nếu có (antihistamine, corticosteroid, epinephrine nếu cần)"
                ],
                "monitoring": "Dấu hiệu huyết khối, phản ứng tại chỗ tiêm, dấu hiệu dị ứng"
            },
            "reversal_agents": {
                "available": False,
                "agents": []
            },
            "administration_instructions": {
                "sc": {
                    "reconstitution": "Dùng trực tiếp từ bút tiêm hoặc ống tiêm đã pha sẵn.",
                    "injection_site": "Vùng bụng, đùi, hoặc cánh tay. Thay đổi vị trí tiêm mỗi lần.",
                    "injection_technique": "Tiêm dưới da (SC), không tiêm vào cơ hoặc tĩnh mạch.",
                    "notes": "Có thể tự tiêm sau khi được hướng dẫn. Lưu trữ trong tủ lạnh, để ở nhiệt độ phòng 30 phút trước khi tiêm. Phác đồ: 3mg/kg tuần 1, 2, 4 (loading), sau đó 1.5mg/kg/tuần, 3mg/kg/2 tuần, hoặc 6mg/kg/4 tuần (maintenance)."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Emicizumab (Hemlibra)",
                    "UpToDate - Emicizumab: Drug information",
                    "Lexicomp - Emicizumab monograph",
                    "ASH Guidelines - Hemophilia A"
                ],
                "last_updated": "2025-02-18",
                "evidence_level": "A - FDA-approved, large RCTs showing benefit in hemophilia A prevention"
            }
        },

}

__all__ = ['OTHER_HEMATOLOGY_DRUGS']
