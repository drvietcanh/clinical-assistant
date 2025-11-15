"""
Cephalosporins - Generation 1
"""

GENERATION_1 = {
    "Cefazolin": {
        "group": "Beta-lactam - Cephalosporin thế hệ 1",
        "vietnamese_name": "Cefazolin, Kefzol, Cephazolin",
        "administration": ["IV", "IM"],
        "indications": [
            "Dự phòng phẫu thuật",
            "Nhiễm khuẩn da và mô mềm",
            "Nhiễm khuẩn đường tiết niệu",
            "Nhiễm khuẩn đường hô hấp"
        ],
        "contraindications": [
            "Dị ứng cephalosporin (phản vệ)",
            "Dị ứng penicillin nặng (phản ứng chéo 10%)"
        ],
        "dosage": {
            "adult_iv": "1-2g IV mỗi 8 giờ",
            "adult_im": "500mg-1g IM mỗi 8 giờ",
            "prophylaxis_iv": "1-2g IV trước mổ (lặp lại nếu mổ >4 giờ)",
            "pediatric_iv": "25-100mg/kg/ngày chia 3-4 lần",
            "notes": "Thời gian bán thải dài (1.8h) nên dùng mỗi 8h"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "15_30": "Giảm liều 50% hoặc tăng khoảng cách",
            "under_15": "500mg-1g mỗi 24-48 giờ"
        },
        "side_effects": [
            "Phát ban",
            "Viêm tĩnh mạch (IV)",
            "Đau tại chỗ tiêm (IM)",
            "Tiêu chảy"
        ],
        "interactions": [
            "Probenecid: tăng nồng độ",
            "Warfarin: tăng nguy cơ chảy máu"
        ],
        "aware_classification": "ACCESS",
        "pregnancy": "B"
    },

    "Cephalexin": {
        "group": "Beta-lactam - Cephalosporin thế hệ 1",
        "vietnamese_name": "Cephalexin, Keflex, Cephalexin",
        "administration": ["PO"],
        "indications": [
            "Nhiễm khuẩn đường tiết niệu",
            "Nhiễm khuẩn da và mô mềm",
            "Nhiễm khuẩn đường hô hấp",
            "Nhiễm khuẩn răng miệng"
        ],
        "contraindications": [
            "Dị ứng cephalosporin (phản ứng chéo với penicillin)",
            "Sốc phản vệ với beta-lactam"
        ],
        "dosage": {
            "adult_po": "250-500mg PO x 4 lần/ngày",
            "adult_severe": "500mg-1g PO x 4 lần/ngày",
            "pediatric_po": "25-50mg/kg/ngày chia 4 lần",
            "notes": "Cephalosporin PO thông dụng nhất. Không có dạng IV"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "15_30": "Giảm liều 50%",
            "under_15": "Giảm liều mạnh hoặc tránh"
        },
        "side_effects": [
            "Tiêu chảy",
            "Phát ban",
            "Buồn nôn",
            "Nhiễm nấm Candida"
        ],
        "interactions": [
            "Probenecid: tăng nồng độ",
            "Warfarin: tăng nguy cơ chảy máu"
        ],
        "aware_classification": "ACCESS",
        "pregnancy": "B"
    },

    "Cefadroxil": {
        "group": "Beta-lactam - Cephalosporin thế hệ 1",
        "vietnamese_name": "Cefadroxil, Cefadroxil, Duricef",
        "administration": ["PO"],
        "indications": [
            "Nhiễm khuẩn đường tiết niệu",
            "Nhiễm khuẩn da và mô mềm",
            "Nhiễm khuẩn đường hô hấp"
        ],
        "contraindications": [
            "Dị ứng cephalosporin",
            "Sốc phản vệ với beta-lactam"
        ],
        "dosage": {
            "adult_po": "1-2g PO x 1-2 lần/ngày",
            "pediatric_po": "30mg/kg/ngày chia 2 lần",
            "notes": "Dùng 1-2 lần/ngày (thuận tiện hơn Cephalexin)"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "15_30": "Giảm liều 50%",
            "under_15": "Giảm liều mạnh"
        },
        "side_effects": [
            "Tiêu chảy",
            "Phát ban",
            "Buồn nôn"
        ],
        "interactions": [
            "Probenecid: tăng nồng độ"
        ],
        "aware_classification": "ACCESS",
        "pregnancy": "B"
    },
}

