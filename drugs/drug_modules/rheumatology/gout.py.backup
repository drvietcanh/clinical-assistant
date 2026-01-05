"""
Gout & Hyperuricemia Drugs (Thuốc điều trị Gout & Tăng acid uric)
"""

GOUT_DRUGS = {
    "Allopurinol": {
        "group": "Rheumatology - Gout (Xanthine Oxidase Inhibitor)",
        "vietnamese_name": "Allopurinol, Zyloric",
        "brand_names": {
            "common": ["Zyloprim"],
            "vietnam": ["Allopurinol 100/300mg", "Zyloric", "Sadapron"]
        },
        "administration": ["PO"],
        "indications": [
            "Gout mạn tính (hạ acid uric máu)",
            "Tăng acid uric do hóa trị ung thư",
            "Sỏi thận do acid uric"
        ],
        "contraindications": [
            "Quá mẫn với Allopurinol (đặc biệt: người mang gen HLA-B*5801)",
            "Cơn Gout cấp đang diễn tiến (không khởi trị lúc này, nhưng nếu đang dùng thì tiếp tục)"
        ],
        "dosage": {
            "gout_maintenance": "Khởi đầu 100 mg/ngày. Tăng dần mỗi 2-4 tuần đến 300 mg/ngày (max 800 mg).",
            "renal_impairment_crcl_10_20": "200 mg/ngày.",
            "renal_impairment_crcl_under_10": "100 mg/ngày.",
            "notes": "Quan trọng: Cần sàng lọc gen HLA-B*5801 ở người Việt Nam/Á Đông trước khi dùng để tránh hội chứng Steven-Johnson."
        },
        "side_effects": [
            "Dị ứng da (nhẹ đến nghiêm trọng - SJS/TEN)",
            "Khởi phát cơn Gout cấp khi mới bắt đầu điều trị (nên phối hợp Colchicine/NSAID trong 3-6 tháng đầu)"
        ],
        "mechanism_of_action": "Ức chế Xanthine Oxidase, enzyme chuyển hóa Hypoxanthine -> Xanthine -> Acid Uric.",
        "monitoring": ["Acid uric máu (Target <6 mg/dL)", "Chức năng thận", "Dấu hiệu dị ứng da"]
    },

    "Colchicine": {
        "group": "Rheumatology - Gout (Anti-inflammatory)",
        "vietnamese_name": "Colchicine",
        "brand_names": {
            "common": ["Colcrys"],
            "vietnam": ["Colchicine 1mg", "Colgout"]
        },
        "administration": ["PO"],
        "indications": [
            "Cơn Gout cấp (Acute Gout)",
            "Dự phòng cơn Gout cấp khi bắt đầu dùng Allopurinol/Febuxostat",
            "Sốt Địa Trung Hải (Familial Mediterranean Fever)"
        ],
        "contraindications": [
            "Suy thận nặng + Suy gan nặng (CCĐ tuyệt đối)",
            "Dùng chung chất ức chế P-gp/CYP3A4 mạnh (Clarithromycin, Ketoconazole) ở người suy thận/gan"
        ],
        "dosage": {
            "acute_gout": "1.2 mg (ưu tiên) hoặc 1 mg ngay khi có triệu chứng, sau đó 0.6 mg (hoặc 0.5mg) sau 1 giờ. Tổng liều ngày đầu không quá 1.8 mg.",
            "prophylaxis": "0.5-0.6 mg x 1-2 lần/ngày.",
            "notes": "Liều cao (Uống mỗi 2h đến khi tiêu chảy) KHÔNG CÒN ĐƯỢC KHUYẾN CÁO do độc tính cao."
        },
        "side_effects": ["Tiêu chảy (chắc chắn xảy ra nếu liều cao)", "Suy tủy (hiếm, dùng lâu dài)", "Độc tính cơ"],
        "mechanism_of_action": "Ức chế sự di cư của bạch cầu trung tính vào ổ viêm bằng cách gắn vào tubulin.",
        "monitoring": ["Công thức máu, CK (nếu đau cơ)", "Chức năng thận"]
    },

    "Febuxostat": {
        "group": "Rheumatology - Gout (Xanthine Oxidase Inhibitor)",
        "vietnamese_name": "Febuxostat, Feburic",
        "brand_names": {
            "common": ["Uloric"],
            "vietnam": ["Feburic 80mg", "Febus"]
        },
        "administration": ["PO"],
        "indications": [
            "Gout mạn tính (Khi không dung nạp hoặc không đáp ứng Allopurinol)",
            "Không cần chỉnh liều ở suy thận nhẹ-trung bình"
        ],
        "contraindications": ["Dùng chung với Azathioprine hoặc Mercaptopurine (CCĐ tuyệt đối)"],
        "dosage": {
            "maintenance": "40 mg hoặc 80 mg x 1 lần/ngày.",
            "notes": "Cảnh báo an toàn về tim mạch (Cardiovascular death risk) cao hơn Allopurinol (FDA Boxed Warning cũ - nay đã giảm nhẹ nhưng vẫn cần thận trọng)."
        },
        "mechanism_of_action": "Ức chế chọn lọc Xanthine Oxidase (Mạnh hơn Allopurinol).",
        "monitoring": ["Men gan", "Acid uric máu"]
    }
}
