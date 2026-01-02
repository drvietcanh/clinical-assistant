"""
Biological Drugs - Other Biological
"""
from typing import Dict, Any


OTHER_BIOLOGICAL_DRUGS: Dict[str, Dict[str, Any]] = {
        "Caplacizumab": {
            "group": "Biological - Nanobody (anti-vWF)",
            "vietnamese_name": "Caplacizumab, Cablivi",
            "administration": ["SC"],
            "indications": [
                "TTP (thrombotic thrombocytopenic purpura) - acquired, kết hợp với plasma exchange và immunosuppression"
            ],
            "contraindications": [
                "Dị ứng caplacizumab hoặc bất kỳ thành phần nào",
                "Chảy máu nặng đang hoạt động"
            ],
            "dosage": {
                "adult_loading": "11mg SC ngày 1 (trước plasma exchange đầu tiên), sau đó 11mg SC mỗi ngày",
                "adult_maintenance": "11mg SC mỗi ngày trong ít nhất 30 ngày sau plasma exchange cuối cùng",
                "notes": "Tiêm dưới da. Dùng kết hợp với plasma exchange và immunosuppression (corticosteroid, rituximab). Tiếp tục ít nhất 30 ngày sau plasma exchange cuối cùng hoặc cho đến khi ADAMTS13 activity bình thường."
            },
            "renal_adjustment": {
                "normal": "Không đổi",
                "30_60": "Không đổi",
                "under_30": "Thận trọng, không cần điều chỉnh liều"
            },
            "side_effects": [
                "Chảy máu - phổ biến (chảy máu mũi, chảy máu nướu, chảy máu đường tiêu hóa)",
                "Phản ứng tại chỗ tiêm (đau, đỏ, sưng) - phổ biến",
                "Đau đầu",
                "Mệt mỏi",
                "Chảy máu nặng - có thể nghiêm trọng",
                "Thiếu máu"
            ],
            "interactions": [
                "Không có tương tác dược động học quan trọng",
                "Thuốc chống đông (warfarin, heparin): tăng nguy cơ chảy máu - TRÁNH hoặc thận trọng",
                "Thuốc chống kết tập tiểu cầu (aspirin, clopidogrel): tăng nguy cơ chảy máu - TRÁNH hoặc thận trọng"
            ],
            "pregnancy": "C",
            "mechanism_of_action": "Caplacizumab là nanobody (single-domain antibody) kháng vWF (von Willebrand factor). vWF là protein quan trọng cho quá trình kết tập tiểu cầu và đông máu. Trong TTP, thiếu ADAMTS13 (enzyme phân hủy vWF) → vWF không được phân hủy → tăng vWF → tăng kết tập tiểu cầu → hình thành huyết khối → tổn thương vi mạch → TTP. Caplacizumab gắn với vWF → ngăn chặn vWF gắn với platelet receptor (GPIb) → ức chế kết tập tiểu cầu → giảm hình thành huyết khối. Dẫn đến: giảm tổn thương vi mạch và cải thiện triệu chứng trong TTP. Caplacizumab được dùng để điều trị TTP kết hợp với plasma exchange và immunosuppression.",
            "monitoring": [
                "Chảy máu - QUAN TRỌNG: theo dõi chặt chẽ, đặc biệt chảy máu nặng",
                "Platelet - đánh giá hiệu quả điều trị, tăng platelet cho thấy đáp ứng",
                "LDH - giảm LDH cho thấy đáp ứng",
                "Creatinine - cải thiện chức năng thận",
                "ADAMTS13 activity - đánh giá đáp ứng, tiếp tục điều trị cho đến khi bình thường",
                "Hemoglobin - thiếu máu do chảy máu",
                "Phản ứng tại chỗ tiêm"
            ],
            "precautions": [
                "THEO DÕI CHẢY MÁU CHẶT CHẼ - tăng nguy cơ chảy máu, đặc biệt chảy máu nặng",
                "TRÁNH dùng với thuốc chống đông và thuốc chống kết tập tiểu cầu - tăng nguy cơ chảy máu",
                "Ngừng caplacizumab nếu có chảy máu nặng",
                "Dùng kết hợp với plasma exchange và immunosuppression - không dùng đơn độc",
                "Tiếp tục ít nhất 30 ngày sau plasma exchange cuối cùng hoặc cho đến khi ADAMTS13 activity bình thường",
                "Theo dõi platelet, LDH, creatinine để đánh giá đáp ứng",
                "Theo dõi ADAMTS13 activity - tiếp tục cho đến khi bình thường"
            ],
            "pharmacokinetics": {
                "half_life": "Không rõ chính xác, khoảng vài giờ",
                "onset": "Nhanh (vài giờ)",
                "duration": "24 giờ (liều mỗi ngày)",
                "protein_binding": "Gắn với vWF",
                "metabolism": "Chuyển hóa qua hệ thống RES, tương tự các immunoglobulin khác",
                "clearance": "Chuyển hóa qua RES, thải trừ qua thận một phần. Half-life ngắn."
            },
            "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Không để ở nhiệt độ phòng quá 14 ngày. Để nhiệt độ phòng 30 phút trước khi tiêm.",
            "black_box_warnings": "CHẢY MÁU NẶNG - tăng nguy cơ chảy máu nghiêm trọng. Theo dõi chặt chẽ. Ngừng ngay nếu có chảy máu nặng. TRÁNH dùng với thuốc chống đông và thuốc chống kết tập tiểu cầu.",
            "drug_interactions": {
                "major": [
                    {
                        "drug": "Thuốc chống đông (warfarin, heparin, DOACs)",
                        "mechanism": "Tác dụng cộng dồn chống đông",
                        "effect": "Tăng nguy cơ chảy máu nặng (nguy hiểm)",
                        "management": "TRÁNH dùng cùng. Nếu bắt buộc, theo dõi chặt chẽ và giảm liều thuốc chống đông."
                    },
                    {
                        "drug": "Thuốc chống kết tập tiểu cầu (aspirin, clopidogrel, ticagrelor)",
                        "mechanism": "Tác dụng cộng dồn ức chế kết tập tiểu cầu",
                        "effect": "Tăng nguy cơ chảy máu nặng (nguy hiểm)",
                        "management": "TRÁNH dùng cùng. Nếu bắt buộc, theo dõi chặt chẽ và cân nhắc ngừng thuốc chống kết tập tiểu cầu."
                    }
                ],
                "moderate": [],
                "minor": []
            },
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng caplacizumab hoặc bất kỳ thành phần nào",
                    "Chảy máu nặng đang hoạt động"
                ],
                "tương_đối": [
                    "Chảy máu nhẹ - tăng nguy cơ",
                    "Tiền sử chảy máu nặng - tăng nguy cơ",
                    "Có thai (category C) - thận trọng"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Caplacizumab là FDA category C. Có thể dùng trong thai kỳ khi cần thiết (TTP nặng). Một số nghiên cứu cho thấy an toàn trong thai kỳ, nhưng cần theo dõi chặt chẽ.",
                "lactation": {
                    "safety": "Compatible with caution",
                    "details": "Caplacizumab bài tiết vào sữa mẹ ở nồng độ thấp. Có thể dùng khi cho con bú với theo dõi trẻ.",
                    "recommendation": "Có thể dùng khi cho con bú với thận trọng. Theo dõi trẻ về dấu hiệu chảy máu."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không đổi",
                "moderate": "Không đổi",
                "severe": "Thận trọng, không cần điều chỉnh liều",
                "notes": "Caplacizumab không chuyển hóa ở gan. Không cần điều chỉnh liều ở suy gan."
            },
            "overdose_management": {
                "symptoms": [
                    "Chảy máu nặng",
                    "Thiếu máu do chảy máu"
                ],
                "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
                "treatment": [
                    "Ngừng caplacizumab ngay",
                    "Điều trị chảy máu: truyền máu, huyết tương, tiểu cầu nếu cần",
                    "Theo dõi hemoglobin, platelet",
                    "Theo dõi chặt chẽ trong ít nhất 24-48 giờ"
                ],
                "monitoring": "Dấu hiệu sinh tồn, dấu hiệu chảy máu, hemoglobin, platelet trong ít nhất 24-48 giờ."
            },
            "reversal_agents": {
                "available": False,
                "agents": []
            },
            "administration_instructions": {
                "sc": {
                    "reconstitution": "Dạng SC: 11mg/ml, tiêm dưới da",
                    "injection_site": "Vùng đùi, bụng (tránh vùng quanh rốn 5cm), cánh tay",
                    "notes": "Để nhiệt độ phòng 30 phút trước khi tiêm. Tiêm dưới da, không tiêm vào cơ hoặc mạch máu. Thay đổi vị trí tiêm mỗi lần. Tiêm trước plasma exchange đầu tiên. Tiếp tục ít nhất 30 ngày sau plasma exchange cuối cùng."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Caplacizumab (Cablivi)",
                    "UpToDate - Caplacizumab: Drug information",
                    "Lexicomp - Caplacizumab monograph",
                    "ASH Guidelines - Thrombotic Thrombocytopenic Purpura"
                ],
                "last_updated": "2025-02-18",
                "evidence_level": "A - FDA-approved, clinical trial data, widely used"
            }
        },

        "Efgartigimod": {
            "group": "Biological - FcRn Blocker (anti-FcRn)",
            "vietnamese_name": "Efgartigimod, Vyvgart",
            "administration": ["IV"],
            "indications": [
                "Nhược cơ (myasthenia gravis) - kháng acetylcholine receptor (AChR) dương tính, generalized"
            ],
            "contraindications": [
                "Dị ứng efgartigimod hoặc bất kỳ thành phần nào",
                "Nhiễm trùng nặng chưa điều trị"
            ],
            "dosage": {
                "adult": "10mg/kg IV mỗi tuần x 4 tuần, sau đó điều chỉnh theo đáp ứng",
                "notes": "Truyền trong 1 giờ. Có thể lặp lại đợt điều trị nếu triệu chứng tái phát."
            },
            "renal_adjustment": {
                "normal": "Không đổi",
                "30_60": "Không đổi",
                "under_30": "Thận trọng, không cần điều chỉnh liều"
            },
            "side_effects": [
                "Nhiễm trùng - phổ biến (nhiễm trùng đường hô hấp trên, nhiễm trùng đường tiết niệu)",
                "Phản ứng truyền (infusion reaction) - phổ biến lần đầu: sốt, ớn lạnh, đau đầu, buồn nôn",
                "Đau đầu",
                "Buồn nôn",
                "Nhiễm trùng nặng - có thể nghiêm trọng",
                "Giảm IgG - có thể xảy ra do cơ chế tác dụng"
            ],
            "interactions": [
                "Không có tương tác dược động học quan trọng",
                "Có thể làm giảm đáp ứng vaccine (sống)",
                "Có thể làm giảm hiệu quả immunoglobulin therapy"
            ],
            "pregnancy": "C",
            "mechanism_of_action": "Efgartigimod là kháng thể đơn dòng kháng FcRn (neonatal Fc receptor, humanized monoclonal antibody). FcRn là receptor quan trọng cho sự sống của IgG trong cơ thể. FcRn bảo vệ IgG khỏi bị phân hủy → kéo dài half-life của IgG. Trong myasthenia gravis, autoantibodies (IgG) tấn công acetylcholine receptor → gây yếu cơ. Efgartigimod gắn với FcRn → ngăn chặn FcRn bảo vệ IgG → tăng phân hủy IgG (bao gồm cả autoantibodies) → giảm nồng độ autoantibodies → giảm tấn công acetylcholine receptor → cải thiện yếu cơ. Dẫn đến: giảm triệu chứng và cải thiện chức năng trong myasthenia gravis. Efgartigimod được dùng để điều trị myasthenia gravis generalized, kháng AChR dương tính.",
            "monitoring": [
                "Nhiễm trùng - theo dõi dấu hiệu nhiễm trùng trong và sau điều trị",
                "Phản ứng truyền - QUAN TRỌNG: theo dõi trong và sau truyền, đặc biệt lần đầu",
                "Triệu chứng myasthenia gravis (yếu cơ, mệt mỏi) - đánh giá hiệu quả điều trị",
                "IgG máu - có thể giảm do cơ chế tác dụng",
                "Tự kháng thể AChR - có thể giảm",
                "Dấu hiệu nhiễm trùng nặng"
            ],
            "precautions": [
                "THEO DÕI NHIỄM TRÙNG CHẶT CHẼ - tăng nguy cơ nhiễm trùng do giảm IgG",
                "Ngừng efgartigimod nếu có nhiễm trùng nặng",
                "Theo dõi phản ứng truyền chặt chẽ, đặc biệt lần đầu",
                "IgG có thể giảm - theo dõi, có thể cần bổ sung immunoglobulin nếu giảm quá mức",
                "Không dùng vaccine sống trong và sau điều trị",
                "Thận trọng ở bệnh nhân có nhiễm trùng đang hoạt động",
                "Có thể cần lặp lại đợt điều trị nếu triệu chứng tái phát"
            ],
            "pharmacokinetics": {
                "half_life": "Không rõ chính xác, khoảng vài ngày",
                "onset": "Vài tuần",
                "duration": "1 tuần (liều mỗi tuần), tác dụng có thể kéo dài vài tuần sau đợt điều trị",
                "protein_binding": "Không rõ",
                "metabolism": "Chuyển hóa qua hệ thống RES, tương tự các immunoglobulin khác",
                "clearance": "Chuyển hóa qua RES, thải trừ qua thận một phần."
            },
            "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Dung dịch pha loãng: bảo quản ở nhiệt độ phòng (15-30°C) hoặc tủ lạnh (2-8°C), dùng trong 24 giờ.",
            "black_box_warnings": "NHIỄM TRÙNG NẶNG - tăng nguy cơ nhiễm trùng nghiêm trọng do giảm IgG. Ngừng nếu có nhiễm trùng nặng. Giảm IgG có thể làm tăng nguy cơ nhiễm trùng.",
            "drug_interactions": {
                "major": [],
                "moderate": [
                    {
                        "drug": "Vaccines (sống)",
                        "mechanism": "Efgartigimod làm giảm IgG, giảm đáp ứng miễn dịch",
                        "effect": "Giảm hiệu quả vaccine, tăng nguy cơ nhiễm trùng từ vaccine sống",
                        "management": "Không dùng vaccine sống trong và sau điều trị efgartigimod. Hoãn vaccine sống ít nhất 3-6 tháng sau liều cuối."
                    },
                    {
                        "drug": "Immunoglobulin therapy (IVIG)",
                        "mechanism": "Efgartigimod làm giảm IgG, có thể làm giảm hiệu quả IVIG",
                        "effect": "Giảm hiệu quả IVIG",
                        "management": "Thận trọng. Có thể cần điều chỉnh liều IVIG hoặc thời gian dùng."
                    }
                ],
                "minor": []
            },
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng efgartigimod hoặc bất kỳ thành phần nào",
                    "Nhiễm trùng nặng chưa điều trị"
                ],
                "tương_đối": [
                    "Nhiễm trùng đang hoạt động - tăng nguy cơ",
                    "Giảm IgG nặng - tăng nguy cơ nhiễm trùng",
                    "Có thai (category C) - thận trọng"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Efgartigimod là FDA category C. Có thể dùng trong thai kỳ khi cần thiết. Một số nghiên cứu cho thấy an toàn trong thai kỳ, nhưng cần theo dõi chặt chẽ.",
                "lactation": {
                    "safety": "Compatible with caution",
                    "details": "Efgartigimod bài tiết vào sữa mẹ ở nồng độ thấp. Có thể dùng khi cho con bú với theo dõi trẻ.",
                    "recommendation": "Có thể dùng khi cho con bú với thận trọng. Theo dõi trẻ về dấu hiệu nhiễm trùng."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không đổi",
                "moderate": "Không đổi",
                "severe": "Thận trọng, không cần điều chỉnh liều",
                "notes": "Efgartigimod không chuyển hóa ở gan. Không cần điều chỉnh liều ở suy gan."
            },
            "overdose_management": {
                "symptoms": [
                    "Nhiễm trùng nặng",
                    "Phản ứng truyền nặng (sốt cao, ớn lạnh, khó thở)",
                    "Giảm IgG nặng"
                ],
                "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
                "treatment": [
                    "Ngừng truyền ngay",
                    "Điều trị phản ứng truyền: corticosteroid IV, antihistamine, epinephrine nếu cần",
                    "Điều trị nhiễm trùng nếu có",
                    "Bổ sung immunoglobulin (IVIG) nếu giảm IgG nặng",
                    "Theo dõi chặt chẽ trong ít nhất 24-48 giờ"
                ],
                "monitoring": "Dấu hiệu sinh tồn, dấu hiệu nhiễm trùng, phản ứng truyền, IgG máu trong ít nhất 24-48 giờ."
            },
            "reversal_agents": {
                "available": False,
                "agents": []
            },
            "administration_instructions": {
                "iv": {
                    "reconstitution": "Pha với NS hoặc D5W. Pha loãng đến nồng độ 0.5-2mg/ml. Lọc qua filter 0.2-0.22 micron.",
                    "infusion_rate": "Truyền trong 1 giờ.",
                    "compatibility": ["NS", "D5W"],
                    "incompatibility": ["Không pha với các thuốc khác"],
                    "notes": "Theo dõi chặt chẽ trong và sau truyền, đặc biệt lần đầu. Ngừng ngay nếu có phản ứng nặng."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Efgartigimod (Vyvgart)",
                    "UpToDate - Efgartigimod: Drug information",
                    "Lexicomp - Efgartigimod monograph",
                    "AAN Guidelines - Myasthenia Gravis"
                ],
                "last_updated": "2025-02-18",
                "evidence_level": "A - FDA-approved, clinical trial data, widely used"
            }
        },

}

__all__ = ['{category.upper()}_DRUGS']
