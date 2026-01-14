"""
Biological Drugs - Fusion Proteins
"""
from typing import Dict, Any


FUSION_PROTEINS_DRUGS: Dict[str, Dict[str, Any]] = {
        "Etanercept": {
            "group": "Biological - Fusion Protein (TNF receptor)",
            "vietnamese_name": "Etanercept, Enbrel",
            "administration": ["SC"],
            "indications": [
                "Viêm khớp dạng thấp (RA)",
                "Viêm cột sống dính khớp (AS)",
                "Vảy nến (psoriasis)",
                "Viêm khớp vảy nến (PsA)",
                "Viêm khớp vị thành niên (JIA)"
            ],
            "contraindications": [
                "Dị ứng etanercept hoặc bất kỳ thành phần nào",
                "Nhiễm trùng nặng chưa điều trị",
                "Suy tim nặng (NYHA class III-IV)",
                "Bệnh lao đang hoạt động"
            ],
            "dosage": {
                "adult_ra": "50mg SC mỗi tuần (hoặc 25mg SC 2 lần/tuần)",
                "adult_psoriasis": "50mg SC 2 lần/tuần x 3 tháng, sau đó 50mg SC mỗi tuần",
                "adult_as": "50mg SC mỗi tuần",
                "adult_psa": "50mg SC mỗi tuần",
                "pediatric_jia": "0.8mg/kg SC mỗi tuần (tối đa 50mg/tuần)",
                "notes": "Tiêm dưới da. Có thể tự tiêm sau khi được hướng dẫn. Test lao trước khi dùng."
            },
            "renal_adjustment": {
                "normal": "Không đổi",
                "30_60": "Không đổi",
                "under_30": "Thận trọng, không cần điều chỉnh liều"
            },
            "side_effects": [
                "Phản ứng tại chỗ tiêm (đau, đỏ, sưng) - phổ biến",
                "Nhiễm trùng - phổ biến, có thể nghiêm trọng (nhiễm trùng cơ hội, lao)",
                "Phản ứng dị ứng (rash, urticaria)",
                "Tăng nguy cơ ung thư (lymphoma, ung thư da)",
                "Suy tim - có thể làm nặng",
                "Bệnh lý thần kinh (demyelinating disease) - hiếm",
                "Giảm bạch cầu, tiểu cầu - hiếm",
                "Tăng men gan",
                "Buồn nôn, đau đầu",
                "Mệt mỏi"
            ],
            "interactions": [
                "Không có tương tác dược động học quan trọng",
                "Có thể làm giảm đáp ứng vaccine (sống)",
                "Tăng nguy cơ nhiễm trùng khi dùng với các thuốc ức chế miễn dịch khác"
            ],
        "pregnancy": "B",
            "mechanism_of_action": "Etanercept là fusion protein gồm thụ thể TNF-α (p75) gắn với Fc của IgG1. TNF-α là cytokine tiền viêm quan trọng, được sản xuất bởi đại thực bào và tế bào T, đóng vai trò trong quá trình viêm. Trong các bệnh tự miễn (RA, AS, psoriasis), TNF-α tăng cao → gây viêm mạn tính → tổn thương mô. Etanercept gắn với TNF-α (cả TNF-α và lymphotoxin-α) → ngăn chặn TNF-α gắn với thụ thể trên tế bào → ức chế tín hiệu viêm → giảm viêm và tổn thương mô. Dẫn đến: giảm triệu chứng và làm chậm tiến triển bệnh. Etanercept được dùng để điều trị nhiều bệnh tự miễn qua trung gian TNF-α, đặc biệt hiệu quả trong RA và AS.",
            "monitoring": [
                "Phản ứng tại chỗ tiêm",
                "Nhiễm trùng - theo dõi dấu hiệu nhiễm trùng trong và sau điều trị",
                "Lao (tuberculosis) - test PPD hoặc IGRA trước khi dùng, theo dõi trong điều trị",
                "Dấu hiệu nhiễm trùng cơ hội (PCP, CMV, herpes, fungal)",
                "Chức năng gan: ALT, AST - mỗi 3-6 tháng",
                "Công thức máu: CBC - mỗi 3-6 tháng",
                "Dấu hiệu suy tim (nếu có tiền sử)",
                "Dấu hiệu bệnh lý thần kinh (nếu có triệu chứng)"
            ],
            "precautions": [
                "TEST LAO TRƯỚC KHI DÙNG (PPD hoặc IGRA) - lao có thể tái hoạt và nghiêm trọng",
                "Điều trị dự phòng lao nếu có tiền sử lao hoặc test dương tính",
                "Theo dõi dấu hiệu nhiễm trùng chặt chẽ - tăng nguy cơ nhiễm trùng, đặc biệt nhiễm trùng cơ hội",
                "Ngừng etanercept nếu có nhiễm trùng nặng",
                "Thận trọng ở bệnh nhân suy tim - có thể làm nặng",
                "Thận trọng ở bệnh nhân có tiền sử ung thư - tăng nguy cơ ung thư",
                "Không dùng vaccine sống trong và sau điều trị",
                "Thận trọng ở bệnh nhân có bệnh lý thần kinh demyelinating",
                "Theo dõi chức năng gan - có thể tăng men gan"
            ],
            "pharmacokinetics": {
                "half_life": "102 giờ (khoảng 4 ngày)",
                "onset": "Vài tuần",
                "duration": "1 tuần (liều mỗi tuần)",
                "protein_binding": "Không rõ",
                "metabolism": "Chuyển hóa qua hệ thống RES, tương tự các immunoglobulin khác",
                "clearance": "Chuyển hóa qua RES, thải trừ qua thận một phần. Half-life trung bình."
            },
            "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Không để ở nhiệt độ phòng quá 14 ngày. Để nhiệt độ phòng 15-30 phút trước khi tiêm.",
            "black_box_warnings": "NHIỄM TRÙNG NẶNG - tăng nguy cơ nhiễm trùng nghiêm trọng, đặc biệt lao và nhiễm trùng cơ hội. Test lao trước khi dùng. Điều trị dự phòng lao nếu cần. Ngừng nếu có nhiễm trùng nặng. Tăng nguy cơ ung thư (lymphoma, ung thư da). Suy tim - có thể làm nặng, ngừng nếu suy tim mới hoặc nặng hơn.",
            "drug_interactions": {
                "major": [],
                "moderate": [
                    {
                        "drug": "Các thuốc ức chế miễn dịch khác (methotrexate, azathioprine, 6-mercaptopurine)",
                        "mechanism": "Tác dụng cộng dồn ức chế miễn dịch",
                        "effect": "Tăng nguy cơ nhiễm trùng, đặc biệt nhiễm trùng cơ hội",
                        "management": "Thận trọng. Cần phòng ngừa nhiễm trùng chặt chẽ (PCP prophylaxis, v.v.)."
                    },
                    {
                        "drug": "Vaccines (sống)",
                        "mechanism": "Etanercept làm giảm đáp ứng miễn dịch",
                        "effect": "Giảm hiệu quả vaccine, tăng nguy cơ nhiễm trùng từ vaccine sống",
                        "management": "Không dùng vaccine sống trong và sau điều trị etanercept. Hoãn vaccine sống ít nhất 3-6 tháng sau liều cuối."
                    }
                ],
                "minor": []
            },
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng etanercept hoặc bất kỳ thành phần nào",
                    "Nhiễm trùng nặng chưa điều trị",
                    "Bệnh lao đang hoạt động",
                    "Suy tim nặng (NYHA class III-IV)"
                ],
                "tương_đối": [
                    "Nhiễm trùng đang hoạt động - tăng nguy cơ",
                    "Suy tim nhẹ đến trung bình (NYHA class I-II) - có thể làm nặng",
                    "Tiền sử lao - cần điều trị dự phòng",
                    "Tiền sử ung thư - tăng nguy cơ",
                    "Bệnh lý thần kinh demyelinating - có thể làm nặng",
                    "Có thai (category B) - thận trọng"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "B",
                "pregnancy_details": "Etanercept là FDA category B. Có thể dùng trong thai kỳ khi cần thiết. Một số nghiên cứu cho thấy an toàn trong thai kỳ, nhưng cần theo dõi chặt chẽ.",
                "lactation": {
                    "safety": "Compatible with caution",
                    "details": "Etanercept bài tiết vào sữa mẹ ở nồng độ thấp. Có thể dùng khi cho con bú với theo dõi trẻ.",
                    "recommendation": "Có thể dùng khi cho con bú với thận trọng. Theo dõi trẻ về dấu hiệu nhiễm trùng."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không đổi",
                "moderate": "Không đổi",
                "severe": "Thận trọng, không cần điều chỉnh liều",
                "notes": "Etanercept không chuyển hóa ở gan. Không cần điều chỉnh liều ở suy gan. Tuy nhiên, cần theo dõi chức năng gan (có thể tăng men gan)."
            },
            "overdose_management": {
                "symptoms": [
                    "Nhiễm trùng nặng",
                    "Phản ứng dị ứng nặng",
                    "Giảm bạch cầu nặng"
                ],
                "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
                "treatment": [
                    "Ngừng etanercept",
                    "Điều trị nhiễm trùng nếu có",
                    "Điều trị phản ứng dị ứng: corticosteroid, antihistamine nếu cần",
                    "Theo dõi công thức máu",
                    "Theo dõi chặt chẽ trong ít nhất 24-48 giờ"
                ],
                "monitoring": "Dấu hiệu sinh tồn, dấu hiệu nhiễm trùng, công thức máu trong ít nhất 24-48 giờ."
            },
            "reversal_agents": {
                "available": False,
                "agents": []
            },
            "administration_instructions": {
                "sc": {
                    "reconstitution": "Dạng SC: 25mg/0.5ml hoặc 50mg/ml, tiêm dưới da",
                    "injection_site": "Vùng đùi, bụng (tránh vùng quanh rốn 5cm), cánh tay",
                    "notes": "Để nhiệt độ phòng 15-30 phút trước khi tiêm. Tiêm dưới da, không tiêm vào cơ hoặc mạch máu. Thay đổi vị trí tiêm mỗi lần. Có thể tự tiêm sau khi được hướng dẫn."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Etanercept (Enbrel)",
                    "UpToDate - Etanercept: Drug information",
                    "Lexicomp - Etanercept monograph",
                    "ACR Guidelines - Rheumatoid Arthritis"
                ],
                "last_updated": "2025-02-18",
                "evidence_level": "A - FDA-approved, extensive clinical data, widely used"
            },
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["Serious infections (especially TB and opportunistic infections)", "Malignancy (lymphoma, skin cancer)", "Heart failure exacerbation", "Demyelinating disease"],
                "qt_prolongation": False,
                "hepatotoxicity": True,
                "nephrotoxicity": False,
                "requires_monitoring": ["Signs of infection - CRITICAL", "TB screening (PPD or IGRA) before treatment - CRITICAL", "CBC", "Hepatic function (ALT, AST)", "Symptoms of heart failure", "Neurological symptoms"]
            },
            "guideline_tags": [
                "ACR Guidelines - Rheumatoid Arthritis",
                "ACR Guidelines - Psoriatic Arthritis",
                "AAD Guidelines - Psoriasis",
                "FDA Black Box Warning - Etanercept and Serious Infections",
                "FDA Black Box Warning - Etanercept and TB",
                "FDA Black Box Warning - Etanercept and Malignancy"
            ]
        },

}

__all__ = ['{category.upper()}_DRUGS']
