"""
Miscellaneous Drugs - Other
FDA Approved Drugs 2022-2026
"""

from typing import Dict, Any


OTHER_MISCELLANEOUS_DRUGS: Dict[str, Dict[str, Any]] = {
    "Amvuttra": {
                "group": "FDA Approved 2022",
                "vietnamese_name": "Vutrisiran, Amvuttra",
                "administration": [
                        "SC",
                ],
                "indications": [
                        "To treat polyneuropathy of hereditary transthyretin-mediated amyloidosis",
                ],
                "contraindications": [
                        "Dị ứng vutrisiran hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "25mg SC mỗi 3 tháng một lần",
                        "adult_loading": "25mg SC, sau đó 25mg SC mỗi 3 tháng",
                        "notes": "FDA phê duyệt 2022. To treat polyneuropathy of hereditary transthyretin-mediated amyloidosis. Tiêm dưới da (SC) mỗi 3 tháng. Bổ sung vitamin A hàng ngày được khuyến cáo.",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Phản ứng tại chỗ tiêm (injection site reactions) - phổ biến (đau, đỏ, sưng, ngứa)",
                        "Đau khớp (arthralgia) - phổ biến",
                        "Mệt mỏi - phổ biến",
                        "Đau cơ (myalgia) - phổ biến",
                        "Buồn nôn - phổ biến",
                        "Đau đầu - phổ biến",
                        "Chóng mặt - phổ biến",
                        "Giảm vitamin A - có thể xảy ra (cần bổ sung vitamin A)",
                        "Giảm thị lực do thiếu vitamin A - hiếm nhưng nghiêm trọng",
                ],
                "interactions": [
                        "Vitamin A supplements: vutrisiran làm giảm nồng độ vitamin A, cần bổ sung vitamin A",
                        "Thuốc chống đông: có thể tăng nguy cơ chảy máu (theo dõi)",
                        "Thuốc ức chế miễn dịch: có thể ảnh hưởng đến đáp ứng vaccine",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Vutrisiran là một small interfering RNA (siRNA) được FDA phê duyệt 2022 để điều trị polyneuropathy của bệnh amyloidosis di truyền qua trung gian transthyretin (hATTR). Cơ chế: Vutrisiran nhắm mục tiêu và làm giảm sản xuất transthyretin (TTR) protein trong gan thông qua RNA interference (RNAi). TTR là protein vận chuyển thyroxine và retinol-binding protein. Trong hATTR, đột biến TTR dẫn đến sự lắng đọng amyloid trong các mô, đặc biệt là thần kinh ngoại biên và tim, gây ra polyneuropathy và các triệu chứng khác. Vutrisiran sử dụng công nghệ GalNAc-conjugate để nhắm mục tiêu gan, nơi TTR được sản xuất. Khi vào tế bào gan, vutrisiran được xử lý và tích hợp vào RNA-induced silencing complex (RISC), sau đó gắn với mRNA của TTR và gây ra sự phân hủy mRNA, dẫn đến giảm sản xuất TTR protein. Giảm TTR protein làm giảm sự lắng đọng amyloid, cải thiện triệu chứng polyneuropathy và làm chậm tiến triển bệnh. Vutrisiran được tiêm dưới da (SC) mỗi 3 tháng một lần, thuận tiện hơn so với patisiran (tiêm mỗi 3 tuần).",
                "monitoring": [
                        "Nồng độ vitamin A - QUAN TRỌNG: trước điều trị và định kỳ trong điều trị, bổ sung vitamin A nếu cần",
                        "Đáp ứng điều trị: cải thiện triệu chứng polyneuropathy, đánh giá chức năng thần kinh",
                        "Phản ứng tại chỗ tiêm - phổ biến, thường nhẹ",
                        "Chức năng gan - định kỳ",
                        "Chức năng thận - định kỳ",
                        "Thị lực - đặc biệt quan trọng do nguy cơ thiếu vitamin A",
                ],
                "precautions": [
                        "Dị ứng vutrisiran hoặc bất kỳ thành phần nào",
                        "GIẢM VITAMIN A - vutrisiran làm giảm nồng độ vitamin A, cần bổ sung vitamin A hàng ngày để tránh thiếu vitamin A và giảm thị lực",
                        "Theo dõi nồng độ vitamin A trước và trong điều trị",
                        "Phản ứng tại chỗ tiêm - phổ biến, thường nhẹ đến trung bình",
                        "Thận trọng ở bệnh nhân suy gan nặng",
                        "Thận trọng ở bệnh nhân suy thận nặng",
                        "Có thể ảnh hưởng đến đáp ứng vaccine - tham khảo ý kiến bác sĩ về lịch tiêm chủng",
                ],
                "pharmacokinetics": {
                        "half_life": "Khoảng 3-4 tháng (do cơ chế RNAi kéo dài)",
                        "onset": "2-4 tuần sau liều đầu tiên (giảm TTR protein)",
                        "duration": "Kéo dài (tiêm mỗi 3 tháng)",
                        "protein_binding": "Không áp dụng (siRNA)",
                        "metabolism": "Phân hủy bởi endonucleases và exonucleases trong tế bào",
                        "clearance": "Thải trừ qua thận và hệ thống reticuloendothelial"
                },
                "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh. Để nhiệt độ phòng 30 phút trước khi tiêm. Không lắc.",
                "black_box_warnings": "GIẢM VITAMIN A - vutrisiran làm giảm nồng độ vitamin A. Thiếu vitamin A có thể dẫn đến giảm thị lực nghiêm trọng. Bổ sung vitamin A hàng ngày được khuyến cáo để duy trì nồng độ vitamin A bình thường.",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng vutrisiran hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Vutrisiran (Amvuttra)",
                                "FDA Approval Date: 2022",
                                "FDA-approved use: To treat polyneuropathy of hereditary transthyretin-mediated amyloidosis",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2022",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Vutrisiran (Amvuttra)",
                ],
                "last_updated": "2026-01-15",
        },
    "Relyvrio": {
                "group": "FDA Approved 2022",
                "vietnamese_name": "Sodium phenylbutyrate/taurursodiol, Relyvrio",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat amyotrophic lateral sclerosis (ALS)",
                ],
                "contraindications": [
                        "Dị ứng sodium phenylbutyrate, taurursodiol hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "1 gói (3g sodium phenylbutyrate + 1g taurursodiol) PO x 2 lần/ngày",
                        "adult_loading": "Bắt đầu với 1 gói x 2 lần/ngày, có thể tăng lên 2 gói x 2 lần/ngày nếu dung nạp tốt",
                        "notes": "FDA phê duyệt 2022. To treat amyotrophic lateral sclerosis (ALS). Mỗi gói chứa 3g sodium phenylbutyrate và 1g taurursodiol. Hòa tan gói bột trong 8 oz (240ml) nước lạnh hoặc nước ở nhiệt độ phòng, khuấy đều và uống ngay. Uống với thức ăn để giảm tác dụng phụ đường tiêu hóa.",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng, có thể cần giảm liều",
                        "under_30": "Thận trọng, dữ liệu hạn chế, có thể cần giảm liều",
                },
                "side_effects": [
                        "Tiêu chảy - phổ biến (có thể nặng)",
                        "Buồn nôn - phổ biến",
                        "Đau bụng - phổ biến",
                        "Mệt mỏi - phổ biến",
                        "Đau đầu - phổ biến",
                        "Chóng mặt - phổ biến",
                        "Đầy hơi - phổ biến",
                        "Tăng men gan (ALT, AST) - phổ biến",
                        "Giảm cân - có thể xảy ra",
                        "Mất nước do tiêu chảy - có thể nghiêm trọng",
                ],
                "interactions": [
                        "Thuốc lợi tiểu: có thể tăng nguy cơ mất nước và rối loạn điện giải",
                        "Thuốc ảnh hưởng đến chức năng gan: có thể tăng nguy cơ tăng men gan",
                        "Thuốc chống đông: sodium phenylbutyrate có thể ảnh hưởng đến đông máu (theo dõi)",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Relyvrio là sự kết hợp của sodium phenylbutyrate và taurursodiol được FDA phê duyệt 2022 để điều trị amyotrophic lateral sclerosis (ALS). Cơ chế: (1) Sodium phenylbutyrate: là một histone deacetylase inhibitor (HDACi) và cũng là một chất giải độc. Nó hoạt động như một chất thay thế cho phenylacetate, giúp loại bỏ ammonia và các chất độc khác. Trong ALS, nó có thể giúp giảm stress endoplasmic reticulum (ER stress) và giảm viêm thần kinh. (2) Taurursodiol (tauroursodeoxycholic acid - TUDCA): là một acid mật taurine-conjugated có tác dụng bảo vệ tế bào thần kinh. Nó giúp giảm ER stress, giảm apoptosis (chết tế bào), và có tác dụng chống viêm. Trong ALS, sự kết hợp này giúp bảo vệ tế bào thần kinh vận động, làm chậm tiến triển bệnh và kéo dài thời gian sống. Cơ chế chính xác chưa được hiểu đầy đủ, nhưng cả hai thành phần đều có tác dụng bảo vệ thần kinh thông qua giảm ER stress và viêm.",
                "monitoring": [
                        "Chức năng gan (ALT, AST, bilirubin) - trước điều trị và định kỳ trong điều trị",
                        "Triệu chứng tiêu chảy - theo dõi chặt chẽ, có thể cần giảm liều hoặc ngừng thuốc",
                        "Dấu hiệu mất nước - đặc biệt quan trọng do tiêu chảy",
                        "Đáp ứng điều trị: đánh giá chức năng vận động, thời gian sống",
                        "Cân nặng - theo dõi giảm cân",
                        "Điện giải - nếu có tiêu chảy nặng",
                ],
                "precautions": [
                        "Dị ứng sodium phenylbutyrate, taurursodiol hoặc bất kỳ thành phần nào",
                        "TIÊU CHẢY - phổ biến và có thể nặng, có thể dẫn đến mất nước và rối loạn điện giải. Ngừng thuốc nếu tiêu chảy nặng.",
                        "Tăng men gan - phổ biến, theo dõi chức năng gan định kỳ",
                        "Mất nước - đặc biệt quan trọng do tiêu chảy, cần bù nước đầy đủ",
                        "Thận trọng ở bệnh nhân suy gan nặng",
                        "Thận trọng ở bệnh nhân suy thận nặng",
                        "Uống với thức ăn để giảm tác dụng phụ đường tiêu hóa",
                ],
                "pharmacokinetics": {
                        "half_life": "Sodium phenylbutyrate: khoảng 0.8-1 giờ; Taurursodiol: khoảng 3-4 giờ",
                        "onset": "Vài tuần đến vài tháng (tác dụng lâm sàng trên ALS)",
                        "duration": "Dài (dùng hàng ngày)",
                        "protein_binding": "Thấp đến trung bình",
                        "metabolism": "Sodium phenylbutyrate: chuyển hóa thành phenylacetate trong gan; Taurursodiol: chuyển hóa trong gan",
                        "clearance": "Thải trừ qua thận và gan"
                },
                "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm. Bảo quản trong bao bì gốc. Hòa tan gói bột trong nước ngay trước khi dùng.",
                "black_box_warnings": "Không có black box warning. Tuy nhiên, cần theo dõi chặt chẽ tiêu chảy và tăng men gan.",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng sodium hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Sodium (Relyvrio)",
                                "FDA Approval Date: 2022",
                                "FDA-approved use: To treat amyotrophic lateral sclerosis (ALS)",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2022",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Sodium (Relyvrio)",
                ],
                "last_updated": "2026-01-15",
        },
    "Fabhalta": {
                "group": "FDA Approved 2023",
                "vietnamese_name": "Iptacopan, Fabhalta",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat paroxysmal nocturnal hemoglobinuria",
                ],
                "contraindications": [
                        "Dị ứng iptacopan hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2023. To treat paroxysmal nocturnal hemoglobinuria",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Iptacopan được FDA phê duyệt 2023 để to treat paroxysmal nocturnal hemoglobinuria. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng iptacopan",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng iptacopan hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Iptacopan (Fabhalta)",
                                "FDA Approval Date: 2023",
                                "FDA-approved use: To treat paroxysmal nocturnal hemoglobinuria",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2023",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Iptacopan (Fabhalta)",
                ],
                "last_updated": "2026-01-15",
        },
    "Filsuvez": {
                "group": "FDA Approved 2023",
                "vietnamese_name": "Birch, Filsuvez",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat wounds associated with dystrophic and junctional epidermolysis bullosa",
                ],
                "contraindications": [
                        "Dị ứng birch hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2023. To treat wounds associated with dystrophic and junctional epidermolysis bullosa",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Birch được FDA phê duyệt 2023 để to treat wounds associated with dystrophic and junctional epidermolysis bullosa. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng birch",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng birch hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Birch (Filsuvez)",
                                "FDA Approval Date: 2023",
                                "FDA-approved use: To treat wounds associated with dystrophic and junctional epidermolysis bullosa",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2023",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Birch (Filsuvez)",
                ],
                "last_updated": "2026-01-15",
        },
    "Litfulo": {
                "group": "FDA Approved 2023",
                "vietnamese_name": "Ritlecitinib, Litfulo",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat severely patchy hair loss",
                ],
                "contraindications": [
                        "Dị ứng ritlecitinib hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2023. To treat severely patchy hair loss",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Ritlecitinib được FDA phê duyệt 2023 để to treat severely patchy hair loss. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng ritlecitinib",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng ritlecitinib hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Ritlecitinib (Litfulo)",
                                "FDA Approval Date: 2023",
                                "FDA-approved use: To treat severely patchy hair loss",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2023",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Ritlecitinib (Litfulo)",
                ],
                "last_updated": "2026-01-15",
        },
    "Qalsody": {
                "group": "FDA Approved 2023",
                "vietnamese_name": "Tofersen, Qalsody",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat amyotrophic lateral sclerosis in adults who have a SOD1 gene mutation",
                ],
                "contraindications": [
                        "Dị ứng tofersen hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2023. To treat amyotrophic lateral sclerosis in adults who have a SOD1 gene mutation",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Tofersen được FDA phê duyệt 2023 để to treat amyotrophic lateral sclerosis in adults who have a sod1 gene mutation. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng tofersen",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng tofersen hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Tofersen (Qalsody)",
                                "FDA Approval Date: 2023",
                                "FDA-approved use: To treat amyotrophic lateral sclerosis in adults who have a SOD1 gene mutation",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2023",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Tofersen (Qalsody)",
                ],
                "last_updated": "2026-01-15",
        },
    "Skyclarys": {
                "group": "FDA Approved 2023",
                "vietnamese_name": "Omaveloxolone, Skyclarys",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat Friedrich’s ataxia",
                ],
                "contraindications": [
                        "Dị ứng omaveloxolone hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2023. To treat Friedrich’s ataxia",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Omaveloxolone được FDA phê duyệt 2023 để to treat friedrich’s ataxia. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng omaveloxolone",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng omaveloxolone hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Omaveloxolone (Skyclarys)",
                                "FDA Approval Date: 2023",
                                "FDA-approved use: To treat Friedrich’s ataxia",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2023",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Omaveloxolone (Skyclarys)",
                ],
                "last_updated": "2026-01-15",
        },
    "Sohonos": {
                "group": "FDA Approved 2023",
                "vietnamese_name": "Palovarotene, Sohonos",
                "administration": [
                        "IV",
                        "SC",
                ],
                "indications": [
                        "To reduce the volume of new heterotopic ossification in adults and pediatric patients (aged 8 years and older for females and 10 years and older for males) with fibrodysplasia ossificans progressiva",
                ],
                "contraindications": [
                        "Dị ứng palovarotene hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2023. To reduce the volume of new heterotopic ossification in adults and pediatric patients (aged 8 years and older for females and 10 years and older for males) with fibrodysplasia ossificans progressiva",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Palovarotene được FDA phê duyệt 2023 để to reduce the volume of new heterotopic ossification in adults and pediatric patients (aged 8 years and older for females and 10 years and older for males) with fibrodysplasia ossificans progressiva. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng palovarotene",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng palovarotene hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Palovarotene (Sohonos)",
                                "FDA Approval Date: 2023",
                                "FDA-approved use: To reduce the volume of new heterotopic ossification in adults and pediatric patients (aged 8 years and older for females and 10 years and older for males) with fibrodysplasia ossificans progressiva",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2023",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Palovarotene (Sohonos)",
                ],
                "last_updated": "2026-01-15",
        },
    "Wainua": {
                "group": "FDA Approved 2023",
                "vietnamese_name": "Eplontersen, Wainua",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat polyneuropathy of hereditary transthyretin-mediated amyloidosis",
                ],
                "contraindications": [
                        "Dị ứng eplontersen hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2023. To treat polyneuropathy of hereditary transthyretin-mediated amyloidosis",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Eplontersen được FDA phê duyệt 2023 để to treat polyneuropathy of hereditary transthyretin-mediated amyloidosis. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng eplontersen",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng eplontersen hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Eplontersen (Wainua)",
                                "FDA Approval Date: 2023",
                                "FDA-approved use: To treat polyneuropathy of hereditary transthyretin-mediated amyloidosis",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2023",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Eplontersen (Wainua)",
                ],
                "last_updated": "2026-01-15",
        },
    "Xdemvy": {
                "group": "FDA Approved 2023",
                "vietnamese_name": "Lotilaner, Xdemvy",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat Demodex blepharitis",
                ],
                "contraindications": [
                        "Dị ứng lotilaner hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2023. To treat Demodex blepharitis",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Lotilaner được FDA phê duyệt 2023 để to treat demodex blepharitis. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng lotilaner",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng lotilaner hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Lotilaner (Xdemvy)",
                                "FDA Approval Date: 2023",
                                "FDA-approved use: To treat Demodex blepharitis",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2023",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Lotilaner (Xdemvy)",
                ],
                "last_updated": "2026-01-15",
        },
    "Alyftrek": {
                "group": "FDA Approved 2024",
                "vietnamese_name": "Vanzacaftor, Alyftrek",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "For the treatment of cystic fibrosis (CF) in patients 6 years of age and older",
                ],
                "contraindications": [
                        "Dị ứng vanzacaftor hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2024. For the treatment of cystic fibrosis (CF) in patients 6 years of age and older",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Vanzacaftor được FDA phê duyệt 2024 để for the treatment of cystic fibrosis (cf) in patients 6 years of age and older. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng vanzacaftor",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng vanzacaftor hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Vanzacaftor (Alyftrek)",
                                "FDA Approval Date: 2024",
                                "FDA-approved use: For the treatment of cystic fibrosis (CF) in patients 6 years of age and older",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2024",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Vanzacaftor (Alyftrek)",
                ],
                "last_updated": "2026-01-15",
        },
    "Aqneursa": {
                "group": "FDA Approved 2024",
                "vietnamese_name": "Levacetylleucine, Aqneursa",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat Niemann-Pick disease type C",
                ],
                "contraindications": [
                        "Dị ứng levacetylleucine hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2024. To treat Niemann-Pick disease type C",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Levacetylleucine được FDA phê duyệt 2024 để to treat niemann-pick disease type c. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng levacetylleucine",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng levacetylleucine hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Levacetylleucine (Aqneursa)",
                                "FDA Approval Date: 2024",
                                "FDA-approved use: To treat Niemann-Pick disease type C",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2024",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Levacetylleucine (Aqneursa)",
                ],
                "last_updated": "2026-01-15",
        },
    "Iqirvo": {
                "group": "FDA Approved 2024",
                "vietnamese_name": "Elafibranor, Iqirvo",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat primary biliary cholangitis in combination with ursodeoxycholic acid",
                ],
                "contraindications": [
                        "Dị ứng elafibranor hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2024. To treat primary biliary cholangitis in combination with ursodeoxycholic acid",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Elafibranor được FDA phê duyệt 2024 để to treat primary biliary cholangitis in combination with ursodeoxycholic acid. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng elafibranor",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng elafibranor hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Elafibranor (Iqirvo)",
                                "FDA Approval Date: 2024",
                                "FDA-approved use: To treat primary biliary cholangitis in combination with ursodeoxycholic acid",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2024",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Elafibranor (Iqirvo)",
                ],
                "last_updated": "2026-01-15",
        },
    "Leqselvi": {
                "group": "FDA Approved 2024",
                "vietnamese_name": "Deuruxolitinib, Leqselvi",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat severe alopecia areata",
                ],
                "contraindications": [
                        "Dị ứng deuruxolitinib hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2024. To treat severe alopecia areata",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Deuruxolitinib được FDA phê duyệt 2024 để to treat severe alopecia areata. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng deuruxolitinib",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng deuruxolitinib hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Deuruxolitinib (Leqselvi)",
                                "FDA Approval Date: 2024",
                                "FDA-approved use: To treat severe alopecia areata",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2024",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Deuruxolitinib (Leqselvi)",
                ],
                "last_updated": "2026-01-15",
        },
    "Livdelzi": {
                "group": "FDA Approved 2024",
                "vietnamese_name": "Seladelpar, Livdelzi",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat primary biliary cholangitis (PBC)",
                ],
                "contraindications": [
                        "Dị ứng seladelpar hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2024. To treat primary biliary cholangitis (PBC)",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Seladelpar được FDA phê duyệt 2024 để to treat primary biliary cholangitis (pbc). Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng seladelpar",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng seladelpar hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Seladelpar (Livdelzi)",
                                "FDA Approval Date: 2024",
                                "FDA-approved use: To treat primary biliary cholangitis (PBC)",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2024",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Seladelpar (Livdelzi)",
                ],
                "last_updated": "2026-01-15",
        },
    "Miplyffa": {
                "group": "FDA Approved 2024",
                "vietnamese_name": "Arimoclomol, Miplyffa",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat Niemann-Pick disease type C",
                ],
                "contraindications": [
                        "Dị ứng arimoclomol hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2024. To treat Niemann-Pick disease type C",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Arimoclomol được FDA phê duyệt 2024 để to treat niemann-pick disease type c. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng arimoclomol",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng arimoclomol hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Arimoclomol (Miplyffa)",
                                "FDA Approval Date: 2024",
                                "FDA-approved use: To treat Niemann-Pick disease type C",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2024",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Arimoclomol (Miplyffa)",
                ],
                "last_updated": "2026-01-15",
        },
    "Rapiblyk": {
                "group": "FDA Approved 2024",
                "vietnamese_name": "Landiolol, Rapiblyk",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat supraventricular tachycardia",
                ],
                "contraindications": [
                        "Dị ứng landiolol hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2024. To treat supraventricular tachycardia",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Landiolol được FDA phê duyệt 2024 để to treat supraventricular tachycardia. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng landiolol",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng landiolol hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Landiolol (Rapiblyk)",
                                "FDA Approval Date: 2024",
                                "FDA-approved use: To treat supraventricular tachycardia",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2024",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Landiolol (Rapiblyk)",
                ],
                "last_updated": "2026-01-15",
        },
    "Sofdra": {
                "group": "FDA Approved 2024",
                "vietnamese_name": "Sofpironium, Sofdra",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat primary axillary hyperhidrosis",
                ],
                "contraindications": [
                        "Dị ứng sofpironium hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2024. To treat primary axillary hyperhidrosis",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Sofpironium được FDA phê duyệt 2024 để to treat primary axillary hyperhidrosis. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng sofpironium",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng sofpironium hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Sofpironium (Sofdra)",
                                "FDA Approval Date: 2024",
                                "FDA-approved use: To treat primary axillary hyperhidrosis",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2024",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Sofpironium (Sofdra)",
                ],
                "last_updated": "2026-01-15",
        },
    "Yorvipath": {
                "group": "FDA Approved 2024",
                "vietnamese_name": "Palopegteriparatide, Yorvipath",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat hypoparathyroidism",
                ],
                "contraindications": [
                        "Dị ứng palopegteriparatide hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2024. To treat hypoparathyroidism",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Palopegteriparatide được FDA phê duyệt 2024 để to treat hypoparathyroidism. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng palopegteriparatide",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng palopegteriparatide hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Palopegteriparatide (Yorvipath)",
                                "FDA Approval Date: 2024",
                                "FDA-approved use: To treat hypoparathyroidism",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2024",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Palopegteriparatide (Yorvipath)",
                ],
                "last_updated": "2026-01-15",
        },
    "Zelsuvmi": {
                "group": "FDA Approved 2024",
                "vietnamese_name": "Berdazimer, Zelsuvmi",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat molluscum contagiosum",
                ],
                "contraindications": [
                        "Dị ứng berdazimer hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2024. To treat molluscum contagiosum",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Berdazimer được FDA phê duyệt 2024 để to treat molluscum contagiosum. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng berdazimer",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng berdazimer hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Berdazimer (Zelsuvmi)",
                                "FDA Approval Date: 2024",
                                "FDA-approved use: To treat molluscum contagiosum",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2024",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Berdazimer (Zelsuvmi)",
                ],
                "last_updated": "2026-01-15",
        },
    "Cardamyst": {
                "group": "FDA Approved 2025",
                "vietnamese_name": "Etripamil, Cardamyst",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat episodes of paroxysmal supraventricular tachycardia",
                ],
                "contraindications": [
                        "Dị ứng etripamil hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2025. To treat episodes of paroxysmal supraventricular tachycardia",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Etripamil được FDA phê duyệt 2025 để to treat episodes of paroxysmal supraventricular tachycardia. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng etripamil",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng etripamil hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Etripamil (Cardamyst)",
                                "FDA Approval Date: 2025",
                                "FDA-approved use: To treat episodes of paroxysmal supraventricular tachycardia",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2025",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Etripamil (Cardamyst)",
                ],
                "last_updated": "2026-01-15",
        },
    "Dawnzera": {
                "group": "FDA Approved 2025",
                "vietnamese_name": "Donidalorsen, Dawnzera",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To prevent attacks of hereditary angioedema",
                ],
                "contraindications": [
                        "Dị ứng donidalorsen hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2025. To prevent attacks of hereditary angioedema",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Donidalorsen được FDA phê duyệt 2025 để to prevent attacks of hereditary angioedema. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng donidalorsen",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng donidalorsen hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Donidalorsen (Dawnzera)",
                                "FDA Approval Date: 2025",
                                "FDA-approved use: To prevent attacks of hereditary angioedema",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2025",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Donidalorsen (Dawnzera)",
                ],
                "last_updated": "2026-01-15",
        },
    "Ekterly": {
                "group": "FDA Approved 2025",
                "vietnamese_name": "Sebetralstat, Ekterly",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat acute attacks of hereditary angioedema",
                ],
                "contraindications": [
                        "Dị ứng sebetralstat hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2025. To treat acute attacks of hereditary angioedema",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Sebetralstat được FDA phê duyệt 2025 để to treat acute attacks of hereditary angioedema. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng sebetralstat",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng sebetralstat hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Sebetralstat (Ekterly)",
                                "FDA Approval Date: 2025",
                                "FDA-approved use: To treat acute attacks of hereditary angioedema",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2025",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Sebetralstat (Ekterly)",
                ],
                "last_updated": "2026-01-15",
        },
    "Gomekli": {
                "group": "FDA Approved 2025",
                "vietnamese_name": "Mirdametinib, Gomekli",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat neurofibromatosis type 1 who have symptomatic plexiform neurofibromas not amenable to complete resection",
                ],
                "contraindications": [
                        "Dị ứng mirdametinib hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2025. To treat neurofibromatosis type 1 who have symptomatic plexiform neurofibromas not amenable to complete resection",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Mirdametinib được FDA phê duyệt 2025 để to treat neurofibromatosis type 1 who have symptomatic plexiform neurofibromas not amenable to complete resection. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng mirdametinib",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng mirdametinib hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Mirdametinib (Gomekli)",
                                "FDA Approval Date: 2025",
                                "FDA-approved use: To treat neurofibromatosis type 1 who have symptomatic plexiform neurofibromas not amenable to complete resection",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2025",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Mirdametinib (Gomekli)",
                ],
                "last_updated": "2026-01-15",
        },
    "Nereus": {
                "group": "FDA Approved 2025",
                "vietnamese_name": "Tradipitant, Nereus",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat vomiting associated with motion",
                ],
                "contraindications": [
                        "Dị ứng tradipitant hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2025. To treat vomiting associated with motion",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Tradipitant được FDA phê duyệt 2025 để to treat vomiting associated with motion. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng tradipitant",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng tradipitant hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Tradipitant (Nereus)",
                                "FDA Approval Date: 2025",
                                "FDA-approved use: To treat vomiting associated with motion",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2025",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Tradipitant (Nereus)",
                ],
                "last_updated": "2026-01-15",
        },
    "Palsonify": {
                "group": "FDA Approved 2025",
                "vietnamese_name": "Paltusotine, Palsonify",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat acromegaly in adults who had an inadequate response to surgery and/or for whom surgery is not an option",
                ],
                "contraindications": [
                        "Dị ứng paltusotine hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2025. To treat acromegaly in adults who had an inadequate response to surgery and/or for whom surgery is not an option",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Paltusotine được FDA phê duyệt 2025 để to treat acromegaly in adults who had an inadequate response to surgery and/or for whom surgery is not an option. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng paltusotine",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng paltusotine hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Paltusotine (Palsonify)",
                                "FDA Approval Date: 2025",
                                "FDA-approved use: To treat acromegaly in adults who had an inadequate response to surgery and/or for whom surgery is not an option",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2025",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Paltusotine (Palsonify)",
                ],
                "last_updated": "2026-01-15",
        },
    "Sephience": {
                "group": "FDA Approved 2025",
                "vietnamese_name": "Sepiapterin, Sephience",
                "administration": [
                        "IV",
                        "SC",
                ],
                "indications": [
                        "To treat hyperphenylalaninemia in patients with sepiapterin-responsive phenylketonuria, in conjunction with a phenylalanine-restricted diet",
                ],
                "contraindications": [
                        "Dị ứng sepiapterin hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2025. To treat hyperphenylalaninemia in patients with sepiapterin-responsive phenylketonuria, in conjunction with a phenylalanine-restricted diet",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Sepiapterin được FDA phê duyệt 2025 để to treat hyperphenylalaninemia in patients with sepiapterin-responsive phenylketonuria, in conjunction with a phenylalanine-restricted diet. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng sepiapterin",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng sepiapterin hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Sepiapterin (Sephience)",
                                "FDA Approval Date: 2025",
                                "FDA-approved use: To treat hyperphenylalaninemia in patients with sepiapterin-responsive phenylketonuria, in conjunction with a phenylalanine-restricted diet",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2025",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Sepiapterin (Sephience)",
                ],
                "last_updated": "2026-01-15",
        },
    "Vizz": {
                "group": "FDA Approved 2025",
                "vietnamese_name": "Aceclidine, Vizz",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat presbyopia",
                ],
                "contraindications": [
                        "Dị ứng aceclidine hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2025. To treat presbyopia",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Aceclidine được FDA phê duyệt 2025 để to treat presbyopia. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng aceclidine",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng aceclidine hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Aceclidine (Vizz)",
                                "FDA Approval Date: 2025",
                                "FDA-approved use: To treat presbyopia",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2025",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Aceclidine (Vizz)",
                ],
                "last_updated": "2026-01-15",
        },
    "Zycubo": {
                "group": "FDA Approved 2026",
                "vietnamese_name": "Copper, Zycubo",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat Menkes disease",
                ],
                "contraindications": [
                        "Dị ứng copper hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2026. To treat Menkes disease",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Copper được FDA phê duyệt 2026 để to treat menkes disease. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng copper",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng copper hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Copper (Zycubo)",
                                "FDA Approval Date: 2026",
                                "FDA-approved use: To treat Menkes disease",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2026",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Copper (Zycubo)",
                ],
                "last_updated": "2026-01-15",
        }
}

__all__ = ['OTHER_MISCELLANEOUS_DRUGS']
