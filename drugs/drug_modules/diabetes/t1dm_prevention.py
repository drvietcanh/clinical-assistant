"""
Type 1 Diabetes Prevention Drugs
Drugs that delay or prevent type 1 diabetes mellitus
Teplizumab - anti-CD3 monoclonal antibody
"""

T1DM_PREVENTION_DRUGS = {
    "Teplizumab": {
        "group": "Diabetes - T1DM Prevention (anti-CD3 Monoclonal Antibody)",
        "vietnamese_name": "Teplizumab, Tzield",
        "administration": ["IV"],
        "indications": [
            "Trì hoãn khởi phát đái tháo đường type 1 (T1DM) ở bệnh nhân ≥8 tuổi có nguy cơ cao (stage 2 T1DM)",
            "Bệnh nhân có tự kháng thể dương tính (autoantibodies) và rối loạn dung nạp glucose nhưng chưa có triệu chứng lâm sàng"
        ],
        "contraindications": [
            "Dị ứng teplizumab hoặc bất kỳ thành phần nào",
            "Nhiễm trùng nặng chưa điều trị",
            "Bệnh nhân đã có T1DM lâm sàng (stage 3)"
        ],
        "dosage": {
            "adult_pediatric_8_17": "850mcg/m² IV ngày 1, sau đó 425mcg/m² IV ngày 2-14 (tổng 14 ngày)",
            "notes": "Truyền trong 30 phút. Chỉ dùng cho bệnh nhân stage 2 T1DM (có tự kháng thể và rối loạn dung nạp glucose nhưng chưa có triệu chứng lâm sàng). Premedication với antihistamine và acetaminophen để giảm phản ứng truyền."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng, không cần điều chỉnh liều"
        },
        "side_effects": [
            "Phản ứng truyền (infusion reaction) - phổ biến: sốt, ớn lạnh, đau đầu, buồn nôn, phát ban, mệt mỏi",
            "Giảm bạch cầu lympho (lymphopenia) - phổ biến, thường tự hồi phục",
            "Nhiễm trùng - phổ biến (nhiễm trùng đường hô hấp trên, nhiễm trùng đường tiết niệu)",
            "Phát ban",
            "Đau đầu",
            "Buồn nôn, nôn",
            "Mệt mỏi",
            "Nhiễm trùng nặng - hiếm",
            "Phản ứng dị ứng nặng - hiếm"
        ],
        "interactions": [
            "Không có tương tác dược động học quan trọng",
            "Có thể làm giảm đáp ứng vaccine (sống)",
            "Tăng nguy cơ nhiễm trùng khi dùng với các thuốc ức chế miễn dịch khác"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Teplizumab là kháng thể đơn dòng kháng CD3 (humanized monoclonal antibody). CD3 là phức hợp protein trên bề mặt tế bào T, quan trọng cho hoạt động của tế bào T. Trong T1DM, tế bào T tự phản ứng (autoreactive T cells) tấn công và phá hủy tế bào beta đảo tụy → giảm sản xuất insulin → T1DM. Teplizumab gắn với CD3 trên tế bào T → điều chỉnh hoạt động tế bào T → giảm hoạt động tế bào T tự phản ứng → bảo vệ tế bào beta đảo tụy. Dẫn đến: trì hoãn khởi phát T1DM ở bệnh nhân có nguy cơ cao. Teplizumab được dùng để trì hoãn khởi phát T1DM ở bệnh nhân stage 2 (có tự kháng thể và rối loạn dung nạp glucose nhưng chưa có triệu chứng lâm sàng).",
        "monitoring": [
            "Phản ứng truyền - QUAN TRỌNG: theo dõi trong và sau truyền mỗi ngày",
            "Công thức máu (WBC, lymphocyte) - giảm bạch cầu lympho phổ biến, thường tự hồi phục",
            "Nhiễm trùng - theo dõi dấu hiệu nhiễm trùng trong và sau điều trị",
            "Đường huyết (glucose, HbA1c) - đánh giá hiệu quả trì hoãn T1DM",
            "C-peptide - đánh giá chức năng tế bào beta",
            "Tự kháng thể (autoantibodies) - có thể giảm",
            "Dấu hiệu T1DM lâm sàng (đa niệu, khát nhiều, sụt cân) - đánh giá khởi phát T1DM"
        ],
        "precautions": [
            "CHỈ DÙNG CHO BỆNH NHÂN STAGE 2 T1DM - có tự kháng thể và rối loạn dung nạp glucose nhưng chưa có triệu chứng lâm sàng",
            "KHÔNG DÙNG CHO BỆNH NHÂN ĐÃ CÓ T1DM LÂM SÀNG (stage 3) - không hiệu quả",
            "THEO DÕI PHẢN ỨNG TRUYỀN CHẶT CHẼ - phổ biến, đặc biệt lần đầu",
            "Premedication với antihistamine và acetaminophen để giảm phản ứng truyền",
            "Truyền chậm lần đầu - theo dõi chặt chẽ",
            "Giảm bạch cầu lympho phổ biến - thường tự hồi phục, theo dõi công thức máu",
            "Ngừng teplizumab nếu có nhiễm trùng nặng",
            "Không dùng vaccine sống trong và sau điều trị",
            "Thận trọng ở bệnh nhân có nhiễm trùng đang hoạt động",
            "Theo dõi dấu hiệu khởi phát T1DM lâm sàng - điều trị ngay nếu có"
        ],
        "pharmacokinetics": {
            "half_life": "Không rõ chính xác, khoảng vài ngày",
            "onset": "Tác dụng trì hoãn T1DM: vài tháng đến vài năm",
            "duration": "Một đợt điều trị: 14 ngày. Tác dụng trì hoãn: có thể kéo dài vài năm.",
            "protein_binding": "Không rõ",
            "metabolism": "Chuyển hóa qua hệ thống RES, tương tự các immunoglobulin khác",
            "clearance": "Chuyển hóa qua RES, thải trừ qua thận một phần."
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Dung dịch pha loãng: bảo quản ở nhiệt độ phòng (15-30°C) hoặc tủ lạnh (2-8°C), dùng trong 24 giờ.",
        "black_box_warnings": "PHẢN ỨNG TRUYỀN NẶNG - có thể gây tử vong. Theo dõi chặt chẽ trong và sau truyền. Ngừng ngay nếu có phản ứng nặng. Tăng nguy cơ nhiễm trùng. Giảm bạch cầu lympho phổ biến.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Các thuốc ức chế miễn dịch khác",
                    "mechanism": "Tác dụng cộng dồn ức chế miễn dịch",
                    "effect": "Tăng nguy cơ nhiễm trùng",
                    "management": "Thận trọng. Cần phòng ngừa nhiễm trùng chặt chẽ."
                },
                {
                    "drug": "Vaccines (sống)",
                    "mechanism": "Teplizumab làm giảm đáp ứng miễn dịch",
                    "effect": "Giảm hiệu quả vaccine, tăng nguy cơ nhiễm trùng từ vaccine sống",
                    "management": "Không dùng vaccine sống trong và sau điều trị teplizumab. Hoãn vaccine sống ít nhất 3-6 tháng sau liều cuối."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng teplizumab hoặc bất kỳ thành phần nào",
                "Nhiễm trùng nặng chưa điều trị",
                "Bệnh nhân đã có T1DM lâm sàng (stage 3)"
            ],
            "tương_đối": [
                "Nhiễm trùng đang hoạt động - tăng nguy cơ",
                "Giảm bạch cầu nặng - tăng nguy cơ nhiễm trùng",
                "Có thai (category C) - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Teplizumab là FDA category C. Có thể dùng trong thai kỳ khi cần thiết. Một số nghiên cứu cho thấy an toàn trong thai kỳ, nhưng cần theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Compatible with caution",
                "details": "Teplizumab bài tiết vào sữa mẹ ở nồng độ thấp. Có thể dùng khi cho con bú với theo dõi trẻ.",
                "recommendation": "Có thể dùng khi cho con bú với thận trọng. Theo dõi trẻ về dấu hiệu nhiễm trùng."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng, không cần điều chỉnh liều",
            "notes": "Teplizumab không chuyển hóa ở gan. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Phản ứng truyền nặng (sốt cao, ớn lạnh, khó thở, phù, sốc)",
                "Giảm bạch cầu lympho nặng",
                "Nhiễm trùng nặng",
                "Phản ứng dị ứng nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng truyền ngay",
                "Điều trị phản ứng truyền: corticosteroid IV, antihistamine, epinephrine nếu cần",
                "Điều trị sốc: dịch, vận mạch nếu cần",
                "Theo dõi công thức máu",
                "Điều trị nhiễm trùng nếu có",
                "Theo dõi chặt chẽ trong ít nhất 24-48 giờ"
            ],
            "monitoring": "Dấu hiệu sinh tồn, phản ứng truyền, công thức máu, dấu hiệu nhiễm trùng trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W. Pha loãng đến nồng độ 0.01-0.1mg/ml. Lọc qua filter 0.2-0.22 micron.",
                "infusion_rate": "Truyền trong 30 phút.",
                "compatibility": ["NS", "D5W"],
                "incompatibility": ["Không pha với các thuốc khác"],
                "notes": "Premedication: diphenhydramine 50mg IV/PO, acetaminophen 650-1000mg PO, 30-60 phút trước truyền. Theo dõi chặt chẽ trong và sau truyền mỗi ngày. Ngừng ngay nếu có phản ứng nặng."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Teplizumab (Tzield)",
                "UpToDate - Teplizumab: Drug information",
                "Lexicomp - Teplizumab monograph",
                "ADA Guidelines - Type 1 Diabetes Prevention"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved (2022), clinical trial data",
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": [],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [],
            },
            "guideline_tags": [
                "FDA Drug Information",
                "UpToDate Drug Information",
            ] 

        }
    },
}

__all__ = ["T1DM_PREVENTION_DRUGS"]

