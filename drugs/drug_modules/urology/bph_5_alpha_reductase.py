"""
Urology Drugs - Bph 5 Alpha Reductase
"""
from typing import Dict, Any


BPH_5_ALPHA_REDUCTASE_DRUGS: Dict[str, Dict[str, Any]] = {
        "Dutasteride": {
            "group": "Urology - 5-alpha Reductase Inhibitor (BPH)",
            "vietnamese_name": "Dutasteride, Avodart",
            "administration": ["PO"],
            "indications": [
                "Phì đại tuyến tiền liệt lành tính (BPH) - giảm kích thước tuyến tiền liệt",
                "Kết hợp với tamsulosin (Jalyn) để tăng hiệu quả"
            ],
            "contraindications": [
                "Dị ứng dutasteride",
                "Phụ nữ có thai - CHỐNG CHỈ ĐỊNH (nguy cơ dị tật thai nhi nam)",
                "Phụ nữ có thể mang thai - CHỐNG CHỈ ĐỊNH (phải dùng biện pháp tránh thai)"
            ],
            "dosage": {
                "adult_bph": "0.5mg PO x 1 lần/ngày",
                "adult_with_tamsulosin": "Jalyn: Dutasteride 0.5mg + Tamsulosin 0.4mg PO x 1 lần/ngày",
                "notes": "Tác dụng chậm (3-6 tháng). Cần dùng liên tục để duy trì hiệu quả. Dutasteride ức chế cả type I và type II 5-alpha reductase (mạnh hơn finasteride chỉ ức chế type II)."
            },
            "renal_adjustment": {
                "normal": "Không đổi",
                "30_60": "Không cần điều chỉnh đáng kể",
                "under_30": "Không cần điều chỉnh đáng kể"
            },
            "side_effects": [
                "Rối loạn chức năng tình dục (giảm ham muốn, rối loạn cương dương, giảm thể tích tinh dịch) - phổ biến",
                "Trầm cảm, lo âu",
                "Ung thư tuyến tiền liệt thể xâm lấn cao (high-grade) - nguy cơ tăng nhẹ",
                "Phát ban",
                "Đau vú, phì đại vú (gynecomastia)"
            ],
            "interactions": [
                "Không có tương tác đáng kể"
            ],
            "pregnancy": "X - Chống chỉ định trong thai kỳ",
            "mechanism_of_action": "Dutasteride là 5-alpha reductase inhibitor (ức chế cả type I và type II). Ức chế enzyme 5-alpha reductase, ngăn chặn chuyển đổi testosterone thành dihydrotestosterone (DHT). DHT là hormone chính kích thích phì đại tuyến tiền liệt. Giảm DHT dẫn đến: (1) Giảm kích thước tuyến tiền liệt (giảm 20-30% sau 6-12 tháng), (2) Cải thiện triệu chứng BPH, (3) Giảm nguy cơ cấp cứu tiết niệu và phẫu thuật BPH. ĐẶC ĐIỂM: (1) Ức chế cả type I và type II 5-alpha reductase (mạnh hơn finasteride chỉ ức chế type II), (2) Tác dụng chậm (3-6 tháng), (3) Cần dùng liên tục để duy trì hiệu quả, (4) Nguy cơ rối loạn chức năng tình dục, (5) CHỐNG CHỈ ĐỊNH ở phụ nữ có thai (nguy cơ dị tật thai nhi nam), (6) Nguy cơ ung thư tuyến tiền liệt thể xâm lấn cao tăng nhẹ.",
            "monitoring": [
                "Triệu chứng BPH (tiểu khó, tiểu yếu, tiểu đêm, tiểu gấp)",
                "Kích thước tuyến tiền liệt (siêu âm, khám trực tràng)",
                "PSA (Prostate-Specific Antigen) - giảm 50% khi dùng dutasteride, cần điều chỉnh khi đánh giá",
                "Dấu hiệu rối loạn chức năng tình dục",
                "Dấu hiệu trầm cảm, lo âu",
                "Dấu hiệu ung thư tuyến tiền liệt (PSA tăng, khám trực tràng bất thường)"
            ],
            "precautions": [
                "CHỐNG CHỈ ĐỊNH ở phụ nữ có thai hoặc có thể mang thai (nguy cơ dị tật thai nhi nam)",
                "Phụ nữ không được xử lý viên nang vỡ (nguy cơ hấp thu qua da)",
                "Tác dụng chậm (3-6 tháng) - cần kiên nhẫn",
                "Cần dùng liên tục để duy trì hiệu quả (ngừng thuốc sẽ mất tác dụng)",
                "Nguy cơ rối loạn chức năng tình dục - tư vấn bệnh nhân trước khi dùng",
                "PSA giảm 50% khi dùng dutasteride - cần điều chỉnh khi đánh giá nguy cơ ung thư tuyến tiền liệt",
                "Nguy cơ ung thư tuyến tiền liệt thể xâm lấn cao tăng nhẹ - theo dõi PSA và khám trực tràng định kỳ",
                "Nguy cơ trầm cảm, lo âu - theo dõi tâm trạng",
                "Dutasteride mạnh hơn finasteride (ức chế cả type I và type II)"
            ],
            "pharmacokinetics": {
                "half_life": "5 tuần (rất dài)",
                "onset": "3-6 tháng (tác dụng lâm sàng)",
                "duration": "Dài (cần dùng liên tục, half-life rất dài)",
                "protein_binding": "99%",
                "metabolism": "Gan (CYP3A4)",
                "clearance": "Gan, thận (bài tiết qua nước tiểu và phân)"
            },
            "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
            "black_box_warnings": "Nguy cơ ung thư tuyến tiền liệt thể xâm lấn cao (high-grade) tăng nhẹ. CHỐNG CHỈ ĐỊNH ở phụ nữ có thai hoặc có thể mang thai (nguy cơ dị tật thai nhi nam). Phụ nữ không được xử lý viên nang vỡ.",
            "drug_interactions": {
                "major": [],
                "moderate": [],
                "minor": []
            },
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng dutasteride",
                    "Phụ nữ có thai - CHỐNG CHỈ ĐỊNH (nguy cơ dị tật thai nhi nam)",
                    "Phụ nữ có thể mang thai - CHỐNG CHỈ ĐỊNH (phải dùng biện pháp tránh thai)"
                ],
                "tương_đối": [
                    "Suy gan nặng - thận trọng (chuyển hóa qua gan)",
                    "Tiền sử ung thư tuyến tiền liệt - thận trọng (nguy cơ ung thư thể xâm lấn cao tăng nhẹ)"
                ]
            },
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng dutasteride",
                    "Phụ nữ có thai - CHỐNG CHỈ ĐỊNH (nguy cơ dị tật thai nhi nam)",
                    "Phụ nữ có thể mang thai - CHỐNG CHỈ ĐỊNH (phải dùng biện pháp tránh thai)"
                ],
                "tương_đối": [
                    "Suy gan nặng - thận trọng (chuyển hóa qua gan)",
                    "Tiền sử ung thư tuyến tiền liệt - thận trọng (nguy cơ ung thư thể xâm lấn cao tăng nhẹ)"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "X",
                "pregnancy_details": "Dutasteride là thuốc phân loại X - CHỐNG CHỈ ĐỊNH trong thai kỳ. Dutasteride có thể gây dị tật thai nhi nam (bất thường cơ quan sinh dục ngoài). Phụ nữ có thai hoặc có thể mang thai KHÔNG được dùng hoặc xử lý viên nang vỡ.",
                "lactation": {
                    "safety": "Not Recommended",
                    "details": "Dutasteride bài tiết vào sữa mẹ. Không khuyến cáo cho con bú khi đang dùng dutasteride.",
                    "recommendation": "Không khuyến cáo cho con bú khi đang dùng dutasteride. Cân nhắc ngừng cho con bú hoặc ngừng thuốc."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh liều",
                "moderate": "Thận trọng. Chuyển hóa qua gan có thể giảm, nhưng thường không cần điều chỉnh liều.",
                "severe": "Thận trọng. Chuyển hóa qua gan giảm, nhưng thường không cần điều chỉnh liều. Theo dõi tác dụng phụ.",
                "notes": "Dutasteride chuyển hóa qua gan (CYP3A4). Suy gan có thể ảnh hưởng chuyển hóa, nhưng thường không cần điều chỉnh liều do phạm vi điều trị rộng và half-life rất dài."
            },
            "overdose_management": {
                "symptoms": [
                    "Rối loạn chức năng tình dục nặng",
                    "Trầm cảm, lo âu nặng"
                ],
                "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
                "treatment": [
                    "Ngừng ngay dutasteride",
                    "Điều trị hỗ trợ: Theo dõi tâm trạng, hỗ trợ tâm lý nếu cần",
                    "Theo dõi: Dấu hiệu rối loạn chức năng tình dục, trầm cảm",
                    "Lưu ý: Half-life rất dài (5 tuần), tác dụng có thể kéo dài"
                ],
                "monitoring": "Theo dõi dấu hiệu rối loạn chức năng tình dục, trầm cảm, lo âu cho đến khi hồi phục. Half-life rất dài, cần theo dõi lâu hơn."
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ. Tác dụng của dutasteride có thể kéo dài rất lâu do half-life rất dài (5 tuần)."
            },
            "administration_instructions": {
                "oral": {
                    "with_food": "Uống với hoặc không thức ăn. Có thể uống không thức ăn nếu cần.",
                    "timing": "0.5mg PO x 1 lần/ngày. Uống đều đặn cùng một thời điểm mỗi ngày.",
                    "notes": "QUAN TRỌNG: 1) Tác dụng chậm (3-6 tháng), cần kiên nhẫn, 2) Cần dùng liên tục để duy trì hiệu quả, 3) CHỐNG CHỈ ĐỊNH ở phụ nữ có thai, 4) Tư vấn bệnh nhân về nguy cơ rối loạn chức năng tình dục, 5) PSA giảm 50% khi dùng dutasteride, 6) Half-life rất dài (5 tuần)."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Dutasteride (Avodart)",
                    "AUA Guidelines - Benign Prostatic Hyperplasia",
                    "UpToDate - Dutasteride: Drug Information",
                    "Medscape - Dutasteride Drug Reference"
                ],
                "last_updated": "2025-02-18",
                "evidence_level": "A - Dựa trên FDA drug labels, AUA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
            }
        },

        "Finasteride": {
            "group": "Urology - 5-alpha Reductase Inhibitor (BPH)",
            "vietnamese_name": "Finasteride, Proscar, Propecia",
            "administration": ["PO"],
            "indications": [
                "Phì đại tuyến tiền liệt lành tính (BPH) - giảm kích thước tuyến tiền liệt",
                "Rụng tóc kiểu nam (male pattern hair loss) - liều thấp hơn"
            ],
            "contraindications": [
                "Dị ứng finasteride",
                "Phụ nữ có thai - CHỐNG CHỈ ĐỊNH (nguy cơ dị tật thai nhi nam)",
                "Phụ nữ có thể mang thai - CHỐNG CHỈ ĐỊNH (phải dùng biện pháp tránh thai)"
            ],
            "dosage": {
                "adult_bph": "5mg PO x 1 lần/ngày",
                "adult_hair_loss": "1mg PO x 1 lần/ngày",
                "notes": "Tác dụng chậm (3-6 tháng). Cần dùng liên tục để duy trì hiệu quả. Ngừng thuốc sẽ mất tác dụng."
            },
            "renal_adjustment": {
                "normal": "Không đổi",
                "30_60": "Không cần điều chỉnh đáng kể",
                "under_30": "Không cần điều chỉnh đáng kể"
            },
            "side_effects": [
                "Rối loạn chức năng tình dục (giảm ham muốn, rối loạn cương dương, giảm thể tích tinh dịch) - phổ biến",
                "Trầm cảm, lo âu",
                "Ung thư tuyến tiền liệt thể xâm lấn cao (high-grade) - nguy cơ tăng nhẹ",
                "Phát ban",
                "Đau vú, phì đại vú (gynecomastia)"
            ],
            "interactions": [
                "Không có tương tác đáng kể"
            ],
            "pregnancy": "X - Chống chỉ định trong thai kỳ",
            "mechanism_of_action": "Finasteride là 5-alpha reductase inhibitor (type II). Ức chế enzyme 5-alpha reductase, ngăn chặn chuyển đổi testosterone thành dihydrotestosterone (DHT). DHT là hormone chính kích thích phì đại tuyến tiền liệt. Giảm DHT dẫn đến: (1) Giảm kích thước tuyến tiền liệt (giảm 20-30% sau 6-12 tháng), (2) Cải thiện triệu chứng BPH, (3) Giảm nguy cơ cấp cứu tiết niệu và phẫu thuật BPH. ĐẶC ĐIỂM: (1) Tác dụng chậm (3-6 tháng), (2) Cần dùng liên tục để duy trì hiệu quả, (3) Nguy cơ rối loạn chức năng tình dục, (4) CHỐNG CHỈ ĐỊNH ở phụ nữ có thai (nguy cơ dị tật thai nhi nam), (5) Nguy cơ ung thư tuyến tiền liệt thể xâm lấn cao tăng nhẹ.",
            "monitoring": [
                "Triệu chứng BPH (tiểu khó, tiểu yếu, tiểu đêm, tiểu gấp)",
                "Kích thước tuyến tiền liệt (siêu âm, khám trực tràng)",
                "PSA (Prostate-Specific Antigen) - giảm 50% khi dùng finasteride, cần điều chỉnh khi đánh giá",
                "Dấu hiệu rối loạn chức năng tình dục",
                "Dấu hiệu trầm cảm, lo âu",
                "Dấu hiệu ung thư tuyến tiền liệt (PSA tăng, khám trực tràng bất thường)"
            ],
            "precautions": [
                "CHỐNG CHỈ ĐỊNH ở phụ nữ có thai hoặc có thể mang thai (nguy cơ dị tật thai nhi nam)",
                "Phụ nữ không được xử lý viên nang vỡ (nguy cơ hấp thu qua da)",
                "Tác dụng chậm (3-6 tháng) - cần kiên nhẫn",
                "Cần dùng liên tục để duy trì hiệu quả (ngừng thuốc sẽ mất tác dụng)",
                "Nguy cơ rối loạn chức năng tình dục - tư vấn bệnh nhân trước khi dùng",
                "PSA giảm 50% khi dùng finasteride - cần điều chỉnh khi đánh giá nguy cơ ung thư tuyến tiền liệt",
                "Nguy cơ ung thư tuyến tiền liệt thể xâm lấn cao tăng nhẹ - theo dõi PSA và khám trực tràng định kỳ",
                "Nguy cơ trầm cảm, lo âu - theo dõi tâm trạng"
            ],
            "pharmacokinetics": {
                "half_life": "6-8 giờ",
                "onset": "3-6 tháng (tác dụng lâm sàng)",
                "duration": "Dài (cần dùng liên tục)",
                "protein_binding": "90%",
                "metabolism": "Gan (CYP3A4)",
                "clearance": "Gan, thận (bài tiết qua nước tiểu và phân)"
            },
            "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
            "black_box_warnings": "Nguy cơ ung thư tuyến tiền liệt thể xâm lấn cao (high-grade) tăng nhẹ. CHỐNG CHỈ ĐỊNH ở phụ nữ có thai hoặc có thể mang thai (nguy cơ dị tật thai nhi nam). Phụ nữ không được xử lý viên nang vỡ.",
            "drug_interactions": {
                "major": [],
                "moderate": [],
                "minor": []
            },
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng finasteride",
                    "Phụ nữ có thai - CHỐNG CHỈ ĐỊNH (nguy cơ dị tật thai nhi nam)",
                    "Phụ nữ có thể mang thai - CHỐNG CHỈ ĐỊNH (phải dùng biện pháp tránh thai)"
                ],
                "tương_đối": [
                    "Suy gan nặng - thận trọng (chuyển hóa qua gan)",
                    "Tiền sử ung thư tuyến tiền liệt - thận trọng (nguy cơ ung thư thể xâm lấn cao tăng nhẹ)"
                ]
            },
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng finasteride",
                    "Phụ nữ có thai - CHỐNG CHỈ ĐỊNH (nguy cơ dị tật thai nhi nam)",
                    "Phụ nữ có thể mang thai - CHỐNG CHỈ ĐỊNH (phải dùng biện pháp tránh thai)"
                ],
                "tương_đối": [
                    "Suy gan nặng - thận trọng (chuyển hóa qua gan)",
                    "Tiền sử ung thư tuyến tiền liệt - thận trọng (nguy cơ ung thư thể xâm lấn cao tăng nhẹ)"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "X",
                "pregnancy_details": "Finasteride là thuốc phân loại X - CHỐNG CHỈ ĐỊNH trong thai kỳ. Finasteride có thể gây dị tật thai nhi nam (bất thường cơ quan sinh dục ngoài). Phụ nữ có thai hoặc có thể mang thai KHÔNG được dùng hoặc xử lý viên nang vỡ.",
                "lactation": {
                    "safety": "Not Recommended",
                    "details": "Finasteride bài tiết vào sữa mẹ. Không khuyến cáo cho con bú khi đang dùng finasteride.",
                    "recommendation": "Không khuyến cáo cho con bú khi đang dùng finasteride. Cân nhắc ngừng cho con bú hoặc ngừng thuốc."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh liều",
                "moderate": "Thận trọng. Chuyển hóa qua gan có thể giảm, nhưng thường không cần điều chỉnh liều.",
                "severe": "Thận trọng. Chuyển hóa qua gan giảm, nhưng thường không cần điều chỉnh liều. Theo dõi tác dụng phụ.",
                "notes": "Finasteride chuyển hóa qua gan (CYP3A4). Suy gan có thể ảnh hưởng chuyển hóa, nhưng thường không cần điều chỉnh liều do phạm vi điều trị rộng."
            },
            "overdose_management": {
                "symptoms": [
                    "Rối loạn chức năng tình dục nặng",
                    "Trầm cảm, lo âu nặng"
                ],
                "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
                "treatment": [
                    "Ngừng ngay finasteride",
                    "Điều trị hỗ trợ: Theo dõi tâm trạng, hỗ trợ tâm lý nếu cần",
                    "Theo dõi: Dấu hiệu rối loạn chức năng tình dục, trầm cảm"
                ],
                "monitoring": "Theo dõi dấu hiệu rối loạn chức năng tình dục, trầm cảm, lo âu cho đến khi hồi phục."
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ. Tác dụng của finasteride có thể kéo dài sau khi ngừng do thời gian bán thải dài."
            },
            "administration_instructions": {
                "oral": {
                    "with_food": "Uống với hoặc không thức ăn. Có thể uống không thức ăn nếu cần.",
                    "timing": "BPH: 5mg PO x 1 lần/ngày. Rụng tóc: 1mg PO x 1 lần/ngày. Uống đều đặn cùng một thời điểm mỗi ngày.",
                    "notes": "QUAN TRỌNG: 1) Tác dụng chậm (3-6 tháng), cần kiên nhẫn, 2) Cần dùng liên tục để duy trì hiệu quả, 3) CHỐNG CHỈ ĐỊNH ở phụ nữ có thai, 4) Tư vấn bệnh nhân về nguy cơ rối loạn chức năng tình dục, 5) PSA giảm 50% khi dùng finasteride."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Finasteride (Proscar, Propecia)",
                    "AUA Guidelines - Benign Prostatic Hyperplasia",
                    "UpToDate - Finasteride: Drug Information",
                    "Medscape - Finasteride Drug Reference"
                ],
                "last_updated": "2025-02-18",
                "evidence_level": "A - Dựa trên FDA drug labels, AUA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
            },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["High-grade prostate cancer (slight increase)", "Sexual dysfunction (decreased libido, erectile dysfunction, decreased ejaculate volume)"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["PSA (decreases by 50% - need to adjust interpretation)", "Prostate size (ultrasound, DRE)", "BPH symptoms", "Sexual function", "Depression/anxiety symptoms"]
            },
            "guideline_tags": [
                "AUA Guidelines - Benign Prostatic Hyperplasia",
                "FDA Black Box Warning - Finasteride and High-Grade Prostate Cancer",
                "FDA Black Box Warning - Finasteride and Pregnancy (Category X)",
                "UpToDate - Finasteride Drug Information"
            ]
        },

}

__all__ = ['BPH_5_ALPHA_REDUCTASE_DRUGS']
