"""
Enhanced Fields Schema - Data
Schema definitions and examples for enhanced drug fields
"""

"""
Enhanced Fields Schema - Data
Schema definitions and examples for enhanced drug fields
"""

ENHANCED_FIELDS_SCHEMA = {
    "mechanism_of_action": {
        "type": "string",
        "required": True,
        "description": "Cơ chế tác dụng của thuốc",
        "format": "Mô tả chi tiết cách thuốc hoạt động ở cấp độ phân tử, tế bào, hoặc cơ quan",
        "guidelines": [
            "Bắt đầu với thuốc tác động lên receptor/enzyme/target nào",
            "Mô tả chuỗi phản ứng dẫn đến hiệu quả điều trị",
            "Nếu là prodrug, mô tả quá trình chuyển hóa thành chất hoạt động",
            "Độ dài: 50-200 từ (đủ chi tiết nhưng không quá dài)",
            "Ngôn ngữ: Tiếng Việt, dễ hiểu cho bác sĩ lâm sàng"
        ],
        "examples": [
            "Ức chế angiotensin converting enzyme (ACE), giảm chuyển angiotensin I thành angiotensin II, giảm aldosterone, gây giãn mạch và giảm huyết áp",
            "Ức chế sản xuất glucose ở gan, tăng nhạy cảm với insulin ở mô ngoại vi, giảm hấp thu glucose ở ruột",
            "Ức chế enzyme cyclooxygenase (COX-1 và COX-2), giảm sản xuất prostaglandin, dẫn đến giảm đau, hạ sốt, chống viêm"
        ]
    },
    
    "monitoring": {
        "type": "list of strings",
        "required": True,
        "description": "Các thông số cần theo dõi khi dùng thuốc",
        "format": "Danh sách các xét nghiệm, dấu hiệu lâm sàng cần monitor",
        "guidelines": [
            "Liệt kê theo tần suất và mức độ quan trọng",
            "Bao gồm: xét nghiệm lab, dấu hiệu lâm sàng, tác dụng phụ cần theo dõi",
            "Có thể có 3-10 mục tùy thuộc vào độ phức tạp của thuốc",
            "Sắp xếp: quan trọng nhất → ít quan trọng hơn",
            "Định dạng: \"Tên xét nghiệm/chỉ số - tần suất - mục đích\""
        ],
        "examples": [
            [
                "Creatinine, BUN sau 1-2 tuần khi bắt đầu",
                "Kali máu định kỳ",
                "Huyết áp",
                "Ho khan (tác dụng phụ thường gặp)",
                "Dấu hiệu phù mạch (sưng mặt, lưỡi, họng - cấp cứu)"
            ],
            [
                "HbA1c mỗi 3 tháng",
                "Đường huyết đói và sau ăn",
                "Creatinine, eGFR mỗi 3-6 tháng",
                "Vitamin B12 mỗi 1-2 năm",
                "Lactate nếu nghi ngờ nhiễm toan lactic (đau cơ, khó thở, đau bụng)"
            ],
            [
                "INR mỗi 1-2 ngày khi bắt đầu, sau đó mỗi 1-4 tuần",
                "Dấu hiệu chảy máu (chảy máu cam, xuất huyết dưới da, nôn ra máu, phân đen)",
                "Chức năng gan (ALT, AST) định kỳ"
            ]
        ]
    },
    
    "precautions": {
        "type": "list of strings",
        "required": True,
        "description": "Các lưu ý và thận trọng khi sử dụng thuốc",
        "format": "Danh sách các điểm cần lưu ý khi kê đơn, sử dụng, hoặc theo dõi",
        "guidelines": [
            "Bao gồm: cách dùng, liều khởi đầu, điều kiện đặc biệt, tương tác quan trọng",
            "Tập trung vào các điểm thực hành lâm sàng",
            "Có thể có 4-8 mục",
            "Sắp xếp: quan trọng nhất → ít quan trọng hơn",
            "Định dạng: \"Hành động cụ thể - lý do hoặc hậu quả\""
        ],
        "examples": [
            [
                "Khởi đầu với liều thấp (5-10mg), tăng dần",
                "Ưu điểm: dùng 1 lần/ngày (compliance tốt hơn)",
                "Theo dõi sát creatinine khi bắt đầu (có thể tăng nhẹ)",
                "Tránh dùng với NSAID (giảm hiệu quả, tăng nguy cơ suy thận)",
                "Ngừng ngay nếu có phù mạch (có thể nguy hiểm tính mạng)"
            ],
            [
                "Ngừng 48h trước và sau khi dùng thuốc cản quang",
                "Theo dõi nhiễm toan lactic ở bệnh nhân suy tim, suy gan, suy thận",
                "Bổ sung vitamin B12 nếu dùng lâu dài",
                "Tránh rượu (tăng nguy cơ nhiễm toan lactic)"
            ],
            [
                "Khởi đầu với liều thấp, tăng dần theo INR",
                "Tương tác với nhiều thuốc và thức ăn (vitamin K)",
                "Cần giáo dục bệnh nhân về chế độ ăn và dấu hiệu chảy máu",
                "Không ngừng đột ngột (tăng nguy cơ huyết khối)"
            ]
        ]
    },
    
    "pharmacokinetics": {
        "type": "dict",
        "required": True,
        "description": "Thông tin dược động học của thuốc",
        "format": "Dictionary với các key chuẩn",
        "structure": {
            "half_life": "string - Thời gian bán thải (vd: '6.2 giờ', '12 giờ (dài)')",
            "onset": "string - Thời gian bắt đầu tác dụng (vd: '1 giờ', '15-30 phút')",
            "duration": "string - Thời gian tác dụng (vd: '10-12 giờ', '24 giờ')",
            "protein_binding": "string - Tỷ lệ gắn protein (vd: '25-30%', 'Minimal', '>95%')",
            "clearance": "string - Đường thải trừ (vd: 'Thận (chủ yếu)', 'Gan qua CYP3A4', 'Thận 60%, gan 40%')"
        },
        "guidelines": [
            "Các key có thể có: half_life, onset, duration, protein_binding, clearance",
            "Có thể thêm các key khác nếu cần: metabolism, distribution, bioavailability",
            "Nếu không có thông tin chính xác, dùng \"Không rõ\" hoặc ước lượng",
            "Định dạng: string ngắn gọn, dễ hiểu"
        ],
        "examples": [
            {
                "half_life": "6.2 giờ",
                "onset": "1-2 giờ",
                "duration": "10-12 giờ",
                "protein_binding": "Minimal",
                "clearance": "Thận (chủ yếu)"
            },
            {
                "half_life": "12 giờ (dài)",
                "onset": "1 giờ",
                "duration": "24 giờ (dài nhất trong các ACE inhibitor)",
                "protein_binding": "25%",
                "clearance": "Thận (100%), không chuyển hóa qua gan"
            },
            {
                "half_life": "36 giờ (rất dài)",
                "onset": "2-4 giờ",
                "duration": "72 giờ",
                "protein_binding": ">99%",
                "clearance": "Gan qua CYP2C9, CYP3A4"
            }
        ]
    },
    
    "storage": {
        "type": "string",
        "required": True,
        "description": "Điều kiện bảo quản thuốc",
        "format": "Mô tả ngắn gọn điều kiện bảo quản",
        "guidelines": [
            "Bao gồm: nhiệt độ, ánh sáng, độ ẩm, các điều kiện đặc biệt",
            "Độ dài: 1-2 câu ngắn gọn",
            "Định dạng chuẩn: \"Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng\""
        ],
        "examples": [
            "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
            "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
            "Bảo quản ở nhiệt độ 2-8°C (tủ lạnh), không đông lạnh",
            "Bảo quản ở nhiệt độ phòng, bảo vệ khỏi ánh sáng, đóng chặt nắp"
        ]
    },
    
    "black_box_warnings": {
        "type": "string or None",
        "required": True,
        "description": "Cảnh báo hộp đen (Black Box Warning) - cảnh báo nghiêm trọng nhất",
        "format": "String mô tả cảnh báo hoặc None nếu không có",
        "guidelines": [
            "Chỉ điền nếu thuốc có Black Box Warning chính thức (FDA)",
            "Nếu không có Black Box Warning nhưng có cảnh báo quan trọng, mô tả ngắn gọn",
            "Nếu không có cảnh báo nghiêm trọng, dùng None",
            "Độ dài: 1-2 câu, ngắn gọn và rõ ràng",
            "Bắt đầu với vấn đề nghiêm trọng nhất"
        ],
        "examples": [
            "Nhiễm toan lactic - có thể tử vong. Nguy cơ cao ở suy thận, suy tim, suy gan, nhiễm trùng nặng",
            "Chống chỉ định trong thai kỳ - có thể gây dị tật thai nhi và tử vong thai nhi. Phù mạch có thể đe dọa tính mạng",
            None,
            "Tăng nguy cơ nhiễm trùng nghiêm trọng, ung thư hạch, và các tác dụng phụ nghiêm trọng khác. Cần theo dõi chặt chẽ"
        ]
    },
    
    # === 8 FIELDS BỔ SUNG ===
    
    "drug_interactions": {
        "type": "dict",
        "required": False,  # Optional field
        "description": "Tương tác thuốc chi tiết với mức độ và cơ chế",
        "format": "Dictionary với các key: major, moderate, minor",
        "structure": {
            "major": "List of dict - Tương tác nghiêm trọng (cần tránh hoặc điều chỉnh)",
            "moderate": "List of dict - Tương tác trung bình (cần theo dõi)",
            "minor": "List of dict - Tương tác nhẹ (ít quan trọng)"
        },
        "item_structure": {
            "drug": "Tên thuốc tương tác",
            "mechanism": "Cơ chế tương tác",
            "effect": "Hậu quả của tương tác",
            "management": "Cách xử trí"
        },
        "examples": [
            {
                "major": [
                    {
                        "drug": "Warfarin",
                        "mechanism": "Ức chế chuyển hóa warfarin qua CYP2C9",
                        "effect": "Tăng nguy cơ chảy máu, tăng INR",
                        "management": "Giảm liều warfarin, theo dõi INR thường xuyên"
                    }
                ],
                "moderate": [],
                "minor": []
            }
        ]
    },
    
    "contraindications": {
        "type": "dict",
        "required": False,
        "description": "Chống chỉ định phân loại thành tuyệt đối và tương đối",
        "format": "Dictionary với absolute và relative",
        "guidelines": [
            "Absolute: Chống chỉ định tuyệt đối (không được dùng)",
            "Relative: Chống chỉ định tương đối (dùng với thận trọng)",
            "Nếu không có, có thể để None hoặc rỗng"
        ],
        "examples": [
            {
                "absolute": [
                    "Dị ứng với thuốc (phản vệ)",
                    "Tam cá nguyệt 2-3 thai kỳ",
                    "Suy thận nặng (CrCl <15)"
                ],
                "relative": [
                    "Suy thận trung bình (CrCl 15-30) - giảm liều",
                    "Suy gan - dùng với thận trọng"
                ]
            }
        ]
    },
    
    "pregnancy_lactation": {
        "type": "dict",
        "required": False,
        "description": "Thông tin về thai kỳ và cho con bú",
        "structure": {
            "fda_category": "A/B/C/D/X - FDA Pregnancy Category",
            "pregnancy_details": "Chi tiết về sử dụng trong thai kỳ",
            "lactation": {
                "safety": "Compatible/Incompatible/Caution",
                "details": "Chi tiết về bài tiết vào sữa mẹ",
                "recommendation": "Khuyến nghị sử dụng"
            }
        },
        "examples": [
            {
                "fda_category": "B",
                "pregnancy_details": "An toàn trong thai kỳ, không có bằng chứng dị tật thai nhi",
                "lactation": {
                    "safety": "Compatible",
                    "details": "Thuốc bài tiết ít vào sữa mẹ, nồng độ thấp",
                    "recommendation": "Có thể dùng an toàn khi cho con bú"
                }
            }
        ]
    },
    
    "hepatic_adjustment": {
        "type": "dict",
        "required": False,
        "description": "Điều chỉnh liều cho bệnh nhân suy gan",
        "structure": {
            "mild": "Điều chỉnh cho suy gan nhẹ (Child-Pugh A)",
            "moderate": "Điều chỉnh cho suy gan trung bình (Child-Pugh B)",
            "severe": "Điều chỉnh cho suy gan nặng (Child-Pugh C)",
            "notes": "Ghi chú thêm về chuyển hóa qua gan"
        },
        "examples": [
            {
                "mild": "Không đổi",
                "moderate": "Giảm liều 25-50%",
                "severe": "Tránh hoặc giảm liều mạnh",
                "notes": "Thuốc chuyển hóa chủ yếu qua gan (CYP3A4)"
            }
        ]
    },
    
    "overdose_management": {
        "type": "dict",
        "required": False,
        "description": "Xử trí quá liều",
        "structure": {
            "symptoms": "List các triệu chứng quá liều",
            "antidote": "Antidote nếu có (hoặc 'Không có')",
            "treatment": "List các bước xử trí",
            "monitoring": "Theo dõi cần thiết"
        },
        "examples": [
            {
                "symptoms": [
                    "Buồn nôn, nôn",
                    "Chóng mặt",
                    "Hạ huyết áp",
                    "Nhịp tim chậm"
                ],
                "antidote": "Không có antidote đặc hiệu",
                "treatment": [
                    "Rửa dạ dày nếu mới uống <1 giờ",
                    "Supportive care",
                    "Theo dõi ECG, huyết áp",
                    "Dopamine/norepinephrine nếu hạ huyết áp"
                ],
                "monitoring": "ECG, huyết áp, nhịp tim liên tục"
            }
        ]
    },
    
    "reversal_agents": {
        "type": "dict or None",
        "required": False,
        "description": "Chất đối kháng/antidote cho thuốc (nếu có)",
        "format": "None nếu không có, hoặc dict với available và agents",
        "structure": {
            "available": "True/False",
            "agents": "List of dict với name, indication, dose, notes"
        },
        "examples": [
            {
                "available": True,
                "agents": [
                    {
                        "name": "Vitamin K",
                        "indication": "Đảo ngược tác dụng chống đông",
                        "dose": "1-10mg PO/IV tùy mức độ",
                        "notes": "PO tác dụng chậm hơn IV (12-24h vs 6-12h)"
                    },
                    {
                        "name": "Prothrombin Complex Concentrate (PCC)",
                        "indication": "Chảy máu nặng, cấp cứu",
                        "dose": "25-50 IU/kg IV"
                    }
                ]
            },
            None  # Nếu không có antidote
        ]
    },
    
    "administration_instructions": {
        "type": "dict",
        "required": False,
        "description": "Hướng dẫn dùng thuốc chi tiết",
        "structure": {
            "oral": {
                "with_food": "Uống với/không thức ăn",
                "timing": "Thời điểm uống (trước/sau ăn)"
            },
            "iv": {
                "reconstitution": "Cách pha",
                "infusion_rate": "Tốc độ truyền",
                "compatibility": "List dịch tương thích",
                "incompatibility": "List dịch không tương thích",
                "notes": "Ghi chú"
            }
        },
        "examples": [
            {
                "oral": {
                    "with_food": "Uống với thức ăn để giảm kích ứng dạ dày",
                    "timing": "Trước ăn 30 phút để hấp thu tốt nhất"
                },
                "iv": {
                    "reconstitution": "Pha với 50-100ml NS hoặc D5W",
                    "infusion_rate": "Truyền trong 30-60 phút",
                    "compatibility": ["NS", "D5W", "Ringer's Lactate"],
                    "incompatibility": ["Amphotericin B", "Vancomycin"],
                    "notes": "Không pha cùng aminoglycoside"
                }
            }
        ]
    },
    
    "references": {
        "type": "dict",
        "required": False,
        "description": "Tài liệu tham khảo và nguồn thông tin",
        "structure": {
            "primary_sources": "List các nguồn chính",
            "last_updated": "Ngày cập nhật (YYYY-MM-DD)",
            "evidence_level": "Mức độ chứng cứ"
        },
        "examples": [
            {
                "primary_sources": [
                    "FDA Drug Label - Metformin",
                    "UpToDate - Metformin Drug Information",
                    "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"
                ],
                "last_updated": "2024-01-15",
                "evidence_level": "High (FDA-approved, extensive clinical data)"
            }
        ]
    }
}


# ============================================================================
# TEMPLATE FUNCTION - Tạo Enhanced Fields Mẫu
# ============================================================================

def create_enhanced_fields_template():
    """
    Trả về template rỗng cho enhanced fields
    Sử dụng để copy-paste khi thêm enhanced fields cho thuốc mới
    """
    return {
        # === 6 FIELDS CƠ BẢN ===
        "mechanism_of_action": "",  # Mô tả cơ chế tác dụng (50-200 từ)
        "monitoring": [],  # List các thông số cần monitor
        "precautions": [],  # List các lưu ý và thận trọng
        "pharmacokinetics": {
            "half_life": "",  # Thời gian bán thải
            "onset": "",  # Thời gian bắt đầu tác dụng
            "duration": "",  # Thời gian tác dụng
            "protein_binding": "",  # Tỷ lệ gắn protein
            "clearance": ""  # Đường thải trừ
        },
        "storage": "",  # Điều kiện bảo quản
        "black_box_warnings": None,  # Cảnh báo hộp đen hoặc None
        
        # === 8 FIELDS BỔ SUNG ===
        "drug_interactions": {
            "major": [],  # List dict: {"drug": "...", "mechanism": "...", "effect": "...", "management": "..."}
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "absolute": [],  # List chống chỉ định tuyệt đối
            "relative": []  # List chống chỉ định tương đối
        },
        "pregnancy_lactation": {
            "fda_category": "",  # A/B/C/D/X
            "pregnancy_details": "",  # Chi tiết về thai kỳ
            "lactation": {
                "safety": "",  # Compatible/Incompatible/Caution
                "details": "",  # Chi tiết
                "recommendation": ""  # Khuyến nghị
            }
        },
        "hepatic_adjustment": {
            "mild": "",  # Điều chỉnh cho suy gan nhẹ
            "moderate": "",  # Điều chỉnh cho suy gan trung bình
            "severe": "",  # Điều chỉnh cho suy gan nặng
            "notes": ""  # Ghi chú thêm
        },
        "overdose_management": {
            "symptoms": [],  # List triệu chứng quá liều
            "antidote": "",  # Antidote nếu có (hoặc "Không có")
            "treatment": [],  # List các bước xử trí
            "monitoring": ""  # Theo dõi cần thiết
        },
        "reversal_agents": None,  # None nếu không có, hoặc dict với "available": True và "agents": []
        "administration_instructions": {
            "oral": {
                "with_food": "",  # Uống với/không thức ăn
                "timing": ""  # Thời điểm uống
            },
            "iv": {
                "reconstitution": "",  # Cách pha
                "infusion_rate": "",  # Tốc độ truyền
                "compatibility": [],  # Dịch tương thích
                "incompatibility": [],  # Dịch không tương thích
                "notes": ""  # Ghi chú
            }
        },
        "references": {
            "primary_sources": [],  # List nguồn chính
            "last_updated": "",  # Ngày cập nhật (YYYY-MM-DD)
            "evidence_level": ""  # Mức độ chứng cứ
        }
    }


# ============================================================================
# VALIDATION FUNCTION - Kiểm Tra Tính Hợp Lệ
# ============================================================================

def validate_enhanced_fields(drug_name, enhanced_fields):
    """
    Kiểm tra tính hợp lệ của enhanced fields
    
    Args:
        drug_name: Tên thuốc
        enhanced_fields: Dictionary chứa enhanced fields
    
    Returns:
        tuple: (is_valid: bool, errors: list of strings)
    """
    errors = []
    
    # Kiểm tra tất cả các field bắt buộc
    required_fields = ["mechanism_of_action", "monitoring", "precautions", 
                      "pharmacokinetics", "storage", "black_box_warnings"]
    
    for field in required_fields:
        if field not in enhanced_fields:
            errors.append(f"{drug_name}: Thiếu field '{field}'")
    
    # Kiểm tra kiểu dữ liệu
    if "mechanism_of_action" in enhanced_fields:
        if not isinstance(enhanced_fields["mechanism_of_action"], str):
            errors.append(f"{drug_name}: 'mechanism_of_action' phải là string")
        elif len(enhanced_fields["mechanism_of_action"]) < 50:
            errors.append(f"{drug_name}: 'mechanism_of_action' quá ngắn (<50 ký tự)")
    
    if "monitoring" in enhanced_fields:
        if not isinstance(enhanced_fields["monitoring"], list):
            errors.append(f"{drug_name}: 'monitoring' phải là list")
        elif len(enhanced_fields["monitoring"]) == 0:
            errors.append(f"{drug_name}: 'monitoring' không được rỗng")
    
    if "precautions" in enhanced_fields:
        if not isinstance(enhanced_fields["precautions"], list):
            errors.append(f"{drug_name}: 'precautions' phải là list")
        elif len(enhanced_fields["precautions"]) == 0:
            errors.append(f"{drug_name}: 'precautions' không được rỗng")
    
    if "pharmacokinetics" in enhanced_fields:
        if not isinstance(enhanced_fields["pharmacokinetics"], dict):
            errors.append(f"{drug_name}: 'pharmacokinetics' phải là dict")
        else:
            pk = enhanced_fields["pharmacokinetics"]
            required_pk_fields = ["half_life", "onset", "duration", 
                                 "protein_binding", "clearance"]
            for pk_field in required_pk_fields:
                if pk_field not in pk:
                    errors.append(f"{drug_name}: 'pharmacokinetics' thiếu '{pk_field}'")
    
    if "storage" in enhanced_fields:
        if not isinstance(enhanced_fields["storage"], str):
            errors.append(f"{drug_name}: 'storage' phải là string")
        elif len(enhanced_fields["storage"]) < 10:
            errors.append(f"{drug_name}: 'storage' quá ngắn (<10 ký tự)")
    
    if "black_box_warnings" in enhanced_fields:
        value = enhanced_fields["black_box_warnings"]
        if value is not None and not isinstance(value, str):
            errors.append(f"{drug_name}: 'black_box_warnings' phải là string hoặc None")
    
    # === VALIDATION CHO 8 FIELDS BỔ SUNG (Optional) ===
    
    # drug_interactions
    if "drug_interactions" in enhanced_fields and enhanced_fields["drug_interactions"] is not None:
        if not isinstance(enhanced_fields["drug_interactions"], dict):
            errors.append(f"{drug_name}: 'drug_interactions' phải là dict hoặc None")
        else:
            di = enhanced_fields["drug_interactions"]
            for severity in ["major", "moderate", "minor"]:
                if severity in di:
                    if not isinstance(di[severity], list):
                        errors.append(f"{drug_name}: 'drug_interactions.{severity}' phải là list")
                    else:
                        for item in di[severity]:
                            if not isinstance(item, dict):
                                errors.append(f"{drug_name}: 'drug_interactions.{severity}' items phải là dict")
                            else:
                                required_keys = ["drug", "mechanism", "effect", "management"]
                                for key in required_keys:
                                    if key not in item:
                                        errors.append(f"{drug_name}: 'drug_interactions.{severity}' item thiếu key '{key}'")
    
    # contraindications
    if "contraindications" in enhanced_fields and enhanced_fields["contraindications"] is not None:
        if not isinstance(enhanced_fields["contraindications"], dict):
            errors.append(f"{drug_name}: 'contraindications' phải là dict hoặc None")
        else:
            ci = enhanced_fields["contraindications"]
            for ci_type in ["absolute", "relative"]:
                if ci_type in ci and not isinstance(ci[ci_type], list):
                    errors.append(f"{drug_name}: 'contraindications.{ci_type}' phải là list")
    
    # pregnancy_lactation
    if "pregnancy_lactation" in enhanced_fields and enhanced_fields["pregnancy_lactation"] is not None:
        if not isinstance(enhanced_fields["pregnancy_lactation"], dict):
            errors.append(f"{drug_name}: 'pregnancy_lactation' phải là dict hoặc None")
        else:
            pl = enhanced_fields["pregnancy_lactation"]
            if "lactation" in pl and not isinstance(pl["lactation"], dict):
                errors.append(f"{drug_name}: 'pregnancy_lactation.lactation' phải là dict")
    
    # hepatic_adjustment
    if "hepatic_adjustment" in enhanced_fields and enhanced_fields["hepatic_adjustment"] is not None:
        if not isinstance(enhanced_fields["hepatic_adjustment"], dict):
            errors.append(f"{drug_name}: 'hepatic_adjustment' phải là dict hoặc None")
    
    # overdose_management
    if "overdose_management" in enhanced_fields and enhanced_fields["overdose_management"] is not None:
        if not isinstance(enhanced_fields["overdose_management"], dict):
            errors.append(f"{drug_name}: 'overdose_management' phải là dict hoặc None")
        else:
            od = enhanced_fields["overdose_management"]
            if "symptoms" in od and not isinstance(od["symptoms"], list):
                errors.append(f"{drug_name}: 'overdose_management.symptoms' phải là list")
            if "treatment" in od and not isinstance(od["treatment"], list):
                errors.append(f"{drug_name}: 'overdose_management.treatment' phải là list")
    
    # reversal_agents
    if "reversal_agents" in enhanced_fields:
        ra = enhanced_fields["reversal_agents"]
        if ra is not None:
            if not isinstance(ra, dict):
                errors.append(f"{drug_name}: 'reversal_agents' phải là dict hoặc None")
            else:
                if "available" in ra and not isinstance(ra["available"], bool):
                    errors.append(f"{drug_name}: 'reversal_agents.available' phải là bool")
                if "agents" in ra and not isinstance(ra["agents"], list):
                    errors.append(f"{drug_name}: 'reversal_agents.agents' phải là list")
    
    # administration_instructions
    if "administration_instructions" in enhanced_fields and enhanced_fields["administration_instructions"] is not None:
        if not isinstance(enhanced_fields["administration_instructions"], dict):
            errors.append(f"{drug_name}: 'administration_instructions' phải là dict hoặc None")
    
    # references
    if "references" in enhanced_fields and enhanced_fields["references"] is not None:
        if not isinstance(enhanced_fields["references"], dict):
            errors.append(f"{drug_name}: 'references' phải là dict hoặc None")
        else:
            ref = enhanced_fields["references"]
            if "primary_sources" in ref and not isinstance(ref["primary_sources"], list):
                errors.append(f"{drug_name}: 'references.primary_sources' phải là list")
    
    return len(errors) == 0, errors


# ============================================================================
# HELPER FUNCTION - Tạo Enhanced Fields từ Thông Tin Thuốc
# ============================================================================

def generate_enhanced_fields_guidelines():
    """
    Trả về hướng dẫn chi tiết cách tạo enhanced fields
    """
    return """
# ============================================================================
# HƯỚNG DẪN TẠO ENHANCED FIELDS CHO THUỐC
# ============================================================================

## BƯỚC 1: Thu thập thông tin
- Xem lại thông tin hiện có trong drug database (dosage, indications, side_effects)
- Tìm kiếm thông tin từ:
  * FDA Drug Labels
  * UpToDate, Medscape
  * Goodman & Gilman, Katzung
  * Nhà sản xuất thuốc
  * Clinical guidelines

## BƯỚC 2: Điền từng field

### 1. mechanism_of_action
- Mô tả cách thuốc hoạt động
- Bắt đầu với target/receptor/enzyme
- Giải thích chuỗi phản ứng
- Độ dài: 50-200 từ

### 2. monitoring
- Liệt kê xét nghiệm lab, dấu hiệu lâm sàng cần theo dõi
- Bao gồm tần suất (nếu có)
- Sắp xếp từ quan trọng nhất → ít quan trọng
- 3-10 mục

### 3. precautions
- Các lưu ý thực hành lâm sàng
- Cách dùng, liều khởi đầu
- Điều kiện đặc biệt
- 4-8 mục

### 4. pharmacokinetics
- half_life: Thời gian bán thải
- onset: Thời gian bắt đầu tác dụng
- duration: Thời gian tác dụng
- protein_binding: % gắn protein
- clearance: Đường thải trừ (thận/gan)

### 5. storage
- Nhiệt độ bảo quản
- Ánh sáng, độ ẩm
- Điều kiện đặc biệt

### 6. black_box_warnings
- Chỉ điền nếu có Black Box Warning
- Hoặc cảnh báo nghiêm trọng quan trọng
- None nếu không có

## BƯỚC 3: Kiểm tra
- Chạy validate_enhanced_fields() để kiểm tra
- Đảm bảo tất cả field đều có giá trị hợp lệ
- Kiểm tra chính tả và ngữ pháp

## BƯỚC 4: Thêm vào database
- Mở file drugs/drug_database.py
- Tìm thuốc cần enhance
- Thêm enhanced fields vào dictionary của thuốc đó
- Kiểm tra lại bằng check_enhanced_fields.py
"""


# ============================================================================
# EXAMPLE - Ví Dụ Hoàn Chỉnh
# ============================================================================

EXAMPLE_ENHANCED_FIELDS = {
    "Metformin": {
        "mechanism_of_action": "Ức chế sản xuất glucose ở gan, tăng nhạy cảm với insulin ở mô ngoại vi, giảm hấp thu glucose ở ruột",
        "monitoring": [
            "HbA1c mỗi 3 tháng",
            "Đường huyết đói và sau ăn",
            "Creatinine, eGFR mỗi 3-6 tháng",
            "Vitamin B12 mỗi 1-2 năm",
            "Lactate nếu nghi ngờ nhiễm toan lactic (đau cơ, khó thở, đau bụng)"
        ],
        "precautions": [
            "Ngừng 48h trước và sau khi dùng thuốc cản quang",
            "Theo dõi nhiễm toan lactic ở bệnh nhân suy tim, suy gan, suy thận",
            "Bổ sung vitamin B12 nếu dùng lâu dài",
            "Tránh rượu (tăng nguy cơ nhiễm toan lactic)"
        ],
        "pharmacokinetics": {
            "half_life": "6.2 giờ",
            "onset": "1-2 giờ",
            "duration": "10-12 giờ",
            "protein_binding": "Minimal",
            "clearance": "Thận (chủ yếu)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Nhiễm toan lactic - có thể tử vong. Nguy cơ cao ở suy thận, suy tim, suy gan, nhiễm trùng nặng"
    },
    
    "Lisinopril": {
        "mechanism_of_action": "Ức chế angiotensin converting enzyme (ACE), giảm chuyển angiotensin I thành angiotensin II, giảm aldosterone, gây giãn mạch và giảm huyết áp. Không phải prodrug (khác với enalapril), tác dụng trực tiếp",
        "monitoring": [
            "Creatinine, BUN sau 1-2 tuần khi bắt đầu",
            "Kali máu định kỳ",
            "Huyết áp",
            "Ho khan (tác dụng phụ thường gặp)",
            "Dấu hiệu phù mạch (sưng mặt, lưỡi, họng - cấp cứu)"
        ],
        "precautions": [
            "Khởi đầu với liều thấp (5-10mg), tăng dần",
            "Ưu điểm: dùng 1 lần/ngày (compliance tốt hơn)",
            "Không phải prodrug nên tác dụng nhanh hơn enalapril",
            "Theo dõi sát creatinine khi bắt đầu (có thể tăng nhẹ)",
            "Tránh dùng với NSAID (giảm hiệu quả, tăng nguy cơ suy thận)",
            "Ngừng ngay nếu có phù mạch (có thể nguy hiểm tính mạng)"
        ],
        "pharmacokinetics": {
            "half_life": "12 giờ (dài)",
            "onset": "1 giờ",
            "duration": "24 giờ (dài nhất trong các ACE inhibitor)",
            "protein_binding": "25%",
            "clearance": "Thận (100%), không chuyển hóa qua gan"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Chống chỉ định trong thai kỳ - có thể gây dị tật thai nhi và tử vong thai nhi. Phù mạch có thể đe dọa tính mạng"
    }
}


# ============================================================================
# EXPORT
# ============================================================================

EXAMPLE_ENHANCED_FIELDS = {
    "Metformin": {
        "mechanism_of_action": "Ức chế sản xuất glucose ở gan, tăng nhạy cảm với insulin ở mô ngoại vi, giảm hấp thu glucose ở ruột",
        "monitoring": [
            "HbA1c mỗi 3 tháng",
            "Đường huyết đói và sau ăn",
            "Creatinine, eGFR mỗi 3-6 tháng",
            "Vitamin B12 mỗi 1-2 năm",
            "Lactate nếu nghi ngờ nhiễm toan lactic (đau cơ, khó thở, đau bụng)"
        ],
        "precautions": [
            "Ngừng 48h trước và sau khi dùng thuốc cản quang",
            "Theo dõi nhiễm toan lactic ở bệnh nhân suy tim, suy gan, suy thận",
            "Bổ sung vitamin B12 nếu dùng lâu dài",
            "Tránh rượu (tăng nguy cơ nhiễm toan lactic)"
        ],
        "pharmacokinetics": {
            "half_life": "6.2 giờ",
            "onset": "1-2 giờ",
            "duration": "10-12 giờ",
            "protein_binding": "Minimal",
            "clearance": "Thận (chủ yếu)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Nhiễm toan lactic - có thể tử vong. Nguy cơ cao ở suy thận, suy tim, suy gan, nhiễm trùng nặng"
    },
    
    "Lisinopril": {
        "mechanism_of_action": "Ức chế angiotensin converting enzyme (ACE), giảm chuyển angiotensin I thành angiotensin II, giảm aldosterone, gây giãn mạch và giảm huyết áp. Không phải prodrug (khác với enalapril), tác dụng trực tiếp",
        "monitoring": [
            "Creatinine, BUN sau 1-2 tuần khi bắt đầu",
            "Kali máu định kỳ",
            "Huyết áp",
            "Ho khan (tác dụng phụ thường gặp)",
            "Dấu hiệu phù mạch (sưng mặt, lưỡi, họng - cấp cứu)"
        ],
        "precautions": [
            "Khởi đầu với liều thấp (5-10mg), tăng dần",
            "Ưu điểm: dùng 1 lần/ngày (compliance tốt hơn)",
            "Không phải prodrug nên tác dụng nhanh hơn enalapril",
            "Theo dõi sát creatinine khi bắt đầu (có thể tăng nhẹ)",
            "Tránh dùng với NSAID (giảm hiệu quả, tăng nguy cơ suy thận)",
            "Ngừng ngay nếu có phù mạch (có thể nguy hiểm tính mạng)"
        ],
        "pharmacokinetics": {
            "half_life": "12 giờ (dài)",
            "onset": "1 giờ",
            "duration": "24 giờ (dài nhất trong các ACE inhibitor)",
            "protein_binding": "25%",
            "clearance": "Thận (100%), không chuyển hóa qua gan"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Chống chỉ định trong thai kỳ - có thể gây dị tật thai nhi và tử vong thai nhi. Phù mạch có thể đe dọa tính mạng"
    }
}

# ============================================================================
# EXAMPLE - Ví Dụ Hoàn Chỉnh
# ============================================================================

EXAMPLE_ENHANCED_FIELDS = {
    "Metformin": {
        "mechanism_of_action": "Ức chế sản xuất glucose ở gan, tăng nhạy cảm với insulin ở mô ngoại vi, giảm hấp thu glucose ở ruột",
        "monitoring": [
            "HbA1c mỗi 3 tháng",
            "Đường huyết đói và sau ăn",
            "Creatinine, eGFR mỗi 3-6 tháng",
            "Vitamin B12 mỗi 1-2 năm",
            "Lactate nếu nghi ngờ nhiễm toan lactic (đau cơ, khó thở, đau bụng)"
        ],
        "precautions": [
            "Ngừng 48h trước và sau khi dùng thuốc cản quang",
            "Theo dõi nhiễm toan lactic ở bệnh nhân suy tim, suy gan, suy thận",
            "Bổ sung vitamin B12 nếu dùng lâu dài",
            "Tránh rượu (tăng nguy cơ nhiễm toan lactic)"
        ],
        "pharmacokinetics": {
            "half_life": "6.2 giờ",
            "onset": "1-2 giờ",
            "duration": "10-12 giờ",
            "protein_binding": "Minimal",
            "clearance": "Thận (chủ yếu)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Nhiễm toan lactic - có thể tử vong. Nguy cơ cao ở suy thận, suy tim, suy gan, nhiễm trùng nặng"
    },
    
    "Lisinopril": {
        "mechanism_of_action": "Ức chế angiotensin converting enzyme (ACE), giảm chuyển angiotensin I thành angiotensin II, giảm aldosterone, gây giãn mạch và giảm huyết áp. Không phải prodrug (khác với enalapril), tác dụng trực tiếp",
        "monitoring": [
            "Creatinine, BUN sau 1-2 tuần khi bắt đầu",
            "Kali máu định kỳ",
            "Huyết áp",
            "Ho khan (tác dụng phụ thường gặp)",
            "Dấu hiệu phù mạch (sưng mặt, lưỡi, họng - cấp cứu)"
        ],
        "precautions": [
            "Khởi đầu với liều thấp (5-10mg), tăng dần",
            "Ưu điểm: dùng 1 lần/ngày (compliance tốt hơn)",
            "Không phải prodrug nên tác dụng nhanh hơn enalapril",
            "Theo dõi sát creatinine khi bắt đầu (có thể tăng nhẹ)",
            "Tránh dùng với NSAID (giảm hiệu quả, tăng nguy cơ suy thận)",
            "Ngừng ngay nếu có phù mạch (có thể nguy hiểm tính mạng)"
        ],
        "pharmacokinetics": {
            "half_life": "12 giờ (dài)",
            "onset": "1 giờ",
            "duration": "24 giờ (dài nhất trong các ACE inhibitor)",
            "protein_binding": "25%",
            "clearance": "Thận (100%), không chuyển hóa qua gan"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Chống chỉ định trong thai kỳ - có thể gây dị tật thai nhi và tử vong thai nhi. Phù mạch có thể đe dọa tính mạng"
    }
}

