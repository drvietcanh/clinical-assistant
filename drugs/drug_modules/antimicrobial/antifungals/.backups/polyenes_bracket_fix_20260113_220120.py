"""
Polyene Antifungals - Antifungal Medications
"""

POLYENES_DRUGS = {
    "Amphotericin B":     {
        "group": "Infectious Disease - Antifungal (Polyene)",
        "vietnamese_name": "Amphotericin B, Fungizone, AmBisome",
        "administration": [
            "IV",
            "Topical",
            "Intrathecal"
    ],
        "indications": [
            "Nhiễm nấm hệ thống nặng (invasive fungal infections)",
            "Nhiễm nấm Candida hệ thống (candidemia, endocarditis)",
            "Nhiễm nấm Aspergillus (invasive aspergillosis)",
            "Nhiễm nấm Cryptococcus (viêm màng não, nhiễm khuẩn huyết)",
            "Nhiễm nấm Mucor (mucormycosis)",
            "Nhiễm nấm Histoplasma (histoplasmosis)",
            "Nhiễm nấm Coccidioides (coccidioidomycosis)",
            "Nhiễm nấm Blastomyces (blastomycosis)",
            "Nhiễm nấm Sporothrix (sporotrichosis)"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng amphotericin B (phản ứng nghiêm trọng)"
    ],
            "tương_đối": [
                "Suy thận nặng (cân nhắc lợi ích/nguy cơ, có thể dùng liposomal - AmBisome)",
                "Suy gan nặng (hiếm độc tính gan)",
                "Rối loạn điện giải nặng (hạ kali, hạ magie)",
                "Thiếu máu nặng"
    ],
        },
        "dosage": {
            "adult_standard": "0.5-1.0 mg/kg/ngày IV",
            "adult_severe": "1.0-1.5 mg/kg/ngày IV",
            "adult_loading": "1 mg/kg x 1 liều (ngày đầu), sau đó 0.5-1 mg/kg/ngày",
            "adult_liposomal": "3-5 mg/kg/ngày IV (AmBisome - ít độc tính thận hơn)",
            "adult_intrathecal": "0.1-0.5 mg mỗi 48-72 giờ (cho viêm màng não do nấm)",
            "notes": """Truyền IV trong 2-6 giờ. Bắt đầu với liều thấp (0.25 mg/kg), tăng dần. Premedication với diphenhydramine, acetaminophen, hydrocortisone để giảm phản ứng truyền.""",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, theo dõi chức năng thận chặt chẽ",
            "under_30": "Thận trọng, cân nhắc dùng liposomal (AmBisome) - ít độc tính thận hơn",
            "hemodialysis": "Không bị lọc qua lọc máu, không cần bổ sung liều",
        },
        "side_effects": [
            "Độc tính thận (tăng creatinine, suy thận cấp) - phổ biến",
            "Hạ kali máu (do tăng thải kali qua thận)",
            "Hạ magie máu",
            "Sốt, ớn lạnh, run (infusion-related reactions) - phổ biến",
            "Buồn nôn, nôn",
            "Thiếu máu",
            "Viêm tĩnh mạch tại vị trí tiêm",
            "Độc tính tim (rối loạn nhịp tim, suy tim) - hiếm",
            "Độc tính gan (tăng men gan) - hiếm"
    ],
        "interactions": [
            "Aminoglycosides: tăng độc tính thận",
            "Cyclosporine: tăng độc tính thận",
            "Tacrolimus: tăng độc tính thận",
            "Furosemide: tăng độc tính thận",
            "Corticosteroids: tăng hạ kali máu",
            "Digoxin: tăng nguy cơ ngộ độc digoxin (hạ kali máu)",
            "Flucytosine: tác dụng hiệp đồng (dùng cùng trong điều trị cryptococcal meningitis)"
    ],
        "pregnancy": "B",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": None,
            "organ_toxicity": {"renal": "Black Box Warning - Nephrotoxicity (may be irreversible, dose-dependent)", "hepatic": "Hepatotoxicity (rare)", "cardiovascular": "Cardiac toxicity (arrhythmias, heart failure - rare)", "hematologic": "Anemia", "metabolic": "Hypokalemia, hypomagnesemia (very common)", "dermatologic": "Infusion-related reactions (fever, chills, rigors - Black Box Warning)"},
            "qt_prolongation": False,
            "hepatotoxicity": "Rare",
            "nephrotoxicity": True,
            "requires_monitoring": ["Renal function (creatinine, BUN, CrCl - Black Box Warning for nephrotoxicity, daily monitoring)", "Serum potassium (hypokalemia - very common, frequent replacement needed)", "Serum magnesium (hypomagnesemia - very common, frequent replacement needed)", "CBC (anemia risk)", "Infusion-related reactions (Black Box Warning - premedication required)", "Hepatic function (hepatotoxicity risk - rare)", "ECG (cardiac toxicity risk - rare)", "Fluid balance (dehydration risk)"],
            "look_alike_sound_alike": ["Amphotericin B", "Amphotericin B deoxycholate"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Nephrotoxicity (may be irreversible)",
            "FDA Black Box Warning - Infusion-Related Reactions",
            "IDSA Guidelines - Antifungal Therapy",
            "IDSA Guidelines - Invasive Aspergillosis",
            "IDSA Guidelines - Candidiasis",
            "IDSA Guidelines - Cryptococcosis",
            "ESCMID-ECMM-ERS Guidelines - Aspergillosis",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18",
        "mechanism_of_action": """Amphotericin B là polyene antifungal, gắn với ergosterol trong màng tế bào nấm, tạo lỗ thủng trong màng, làm rò rỉ các ion và chất dinh dưỡng, dẫn đến chết tế bào nấm. Thuốc có ái lực cao với ergosterol (có trong nấm) nhưng cũng gắn một phần với cholesterol (có trong tế bào người), gây độc tính. Phổ kháng nấm rất rộng: Candida, Aspergillus, Cryptococcus, Mucor, Histoplasma, Coccidioides, Blastomyces, Sporothrix. Đây là thuốc tiêu chuẩn vàng (gold standard) cho nhiễm nấm hệ thống nặng, nhưng có độc tính thận đáng kể. Liposomal formulation (AmBisome) có ít độc tính thận hơn nhưng đắt hơn.""",
        "monitoring": [
            "Chức năng thận (creatinine, BUN, CrCl) - TRƯỚC, TRONG, và SAU điều trị - đặc biệt quan trọng",
            "Điện giải (K, Mg) - hạ kali và hạ magie rất phổ biến, cần bù",
            "Công thức máu (Hgb, Hct) - thiếu máu có thể xảy ra",
            "Dấu hiệu nhiễm trùng (sốt, WBC, CRP)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Chức năng gan (ALT, AST) - hiếm nhưng có thể xảy ra",
            "ECG (nếu có triệu chứng tim) - hiếm",
            "Cân bằng dịch vào-ra",
            "Dấu hiệu phản ứng truyền (sốt, ớn lạnh, run)"
    ],
        "precautions": [
            "Độc tính thận là tác dụng phụ phổ biến nhất - theo dõi chặt chẽ creatinine, BUN",
            "Premedication: Diphenhydramine 25-50mg IV, Acetaminophen 650mg PO, Hydrocortisone 25-50mg IV (trước truyền) để giảm phản ứng truyền",
            "Bắt đầu với liều thấp (0.25 mg/kg), tăng dần đến liều đích (0.5-1 mg/kg/ngày)",
            "Truyền IV trong 2-6 giờ (truyền chậm giảm phản ứng truyền)",
            "Bù kali và magie thường xuyên (hạ kali và hạ magie rất phổ biến)",
            "Theo dõi cân bằng dịch (có thể gây mất nước)",
            "Liposomal formulation (AmBisome) ít độc tính thận hơn nhưng đắt hơn - cân nhắc ở bệnh nhân suy thận",
            "Tránh dùng cùng aminoglycosides, cyclosporine, tacrolimus (tăng độc tính thận)",
            "Theo dõi thiếu máu (có thể cần truyền máu)",
            "Không pha chung với các thuốc khác (truyền riêng biệt)",
            "Bảo vệ khỏi ánh sáng (bọc bọc ngoài bằng giấy bạc hoặc túi tối màu)"
    ],
        "pharmacokinetics": {
            "half_life": "15 ngày (rất dài - tích lũy trong mô)",
            "onset": "Tác dụng kháng nấm bắt đầu trong 24-48 giờ",
            "duration": "Liều 0.5-1 mg/kg/ngày, điều trị thường 2-6 tuần (tùy loại nhiễm nấm)",
            "protein_binding": ">90%",
            "clearance": "Chậm, tích lũy trong mô (gan, thận, phổi). Thải trừ rất chậm qua thận và phân.",
        },
        "storage": """Bảo quản bột khô ở nhiệt độ phòng (20-25°C), tránh ánh sáng. Sau khi pha: bảo quản ở nhiệt độ phòng 24 giờ, tránh ánh sáng. Không đông lạnh. Bảo vệ khỏi ánh sáng khi truyền (bọc bọc ngoài bằng giấy bạc).""",
        "black_box_warnings": """Có thể gây suy thận cấp nghiêm trọng, đặc biệt ở liều cao, dùng kéo dài, hoặc dùng cùng các thuốc độc thận khác. Độc tính thận có thể không hồi phục. Theo dõi chức năng thận chặt chẽ. Hạ kali máu và hạ magie máu rất phổ biến và có thể nghiêm trọng.""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Aminoglycosides (Gentamicin, Tobramycin, Amikacin)",
                    "mechanism": "Cả hai đều có độc tính thận, tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ suy thận cấp nghiêm trọng",
                    "management": """TRÁNH DÙNG CHUNG nếu có thể. Nếu bắt buộc, theo dõi chức năng thận chặt chẽ (creatinine, BUN mỗi ngày). Cân nhắc dùng liposomal (AmBisome).""",
                },
    {
                    "drug": "Cyclosporine, Tacrolimus",
                    "mechanism": "Cả hai đều có độc tính thận, tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ suy thận cấp nghiêm trọng",
                    "management": """TRÁNH DÙNG CHUNG nếu có thể. Nếu bắt buộc, theo dõi chức năng thận chặt chẽ. Cân nhắc dùng liposomal (AmBisome). Có thể cần giảm liều cyclosporine/tacrolimus.""",
                },
    {
                    "drug": "Furosemide, các loop diuretics",
                    "mechanism": "Cả hai đều có độc tính thận, tác dụng cộng dồn. Furosemide cũng gây hạ kali máu.",
                    "effect": "Tăng nguy cơ suy thận cấp, tăng hạ kali máu",
                    "management": "Thận trọng. Theo dõi chức năng thận chặt chẽ. Bù kali và magie thường xuyên.",
                }
                ],
            "moderate": [
    {
                    "drug": "Digoxin",
                    "mechanism": "Amphotericin B gây hạ kali máu, tăng độc tính digoxin",
                    "effect": "Tăng nguy cơ ngộ độc digoxin (rối loạn nhịp, block AV)",
                    "management": "Theo dõi kali máu chặt chẽ, duy trì kali >4.0 mEq/L. Theo dõi nồng độ digoxin. Bù kali thường xuyên.",
                },
    {
                    "drug": "Corticosteroids (Prednisone, Hydrocortisone)",
                    "mechanism": "Corticosteroids cũng gây hạ kali máu",
                    "effect": "Tăng nguy cơ hạ kali máu nặng",
                    "management": "Bù kali và magie thường xuyên. Theo dõi kali máu chặt chẽ.",
                },
    {
                    "drug": "Flucytosine",
                    "mechanism": "Tác dụng hiệp đồng kháng nấm (dùng cùng trong điều trị cryptococcal meningitis)",
                    "effect": "Tăng hiệu quả kháng nấm, nhưng flucytosine cũng có độc tính thận và tủy xương",
                    "management": """Dùng cùng để tăng hiệu quả (ví dụ: cryptococcal meningitis). Theo dõi chức năng thận, công thức máu chặt chẽ. Điều chỉnh liều flucytosine theo chức năng thận.""",
                }
                ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng amphotericin B (phản ứng nghiêm trọng)"
    ],
            "tương_đối": [
                "Suy thận nặng (cân nhắc lợi ích/nguy cơ, có thể dùng liposomal - AmBisome)",
                "Suy gan nặng (hiếm độc tính gan)",
                "Rối loạn điện giải nặng (hạ kali, hạ magie)",
                "Thiếu máu nặng"
    ],
        },
        "reversal_agents": None,
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": """Amphotericin B được coi là tương đối an toàn trong thai kỳ. Đã được sử dụng trong thai kỳ cho nhiễm nấm hệ thống nặng. Cân nhắc lợi ích/nguy cơ. Lựa chọn đầu tay cho nhiễm nấm hệ thống nặng trong thai kỳ.""",
            "lactation": {
                "safety": "Compatible",
                "details": """Amphotericin B bài tiết vào sữa mẹ ở nồng độ rất thấp. Nồng độ trong máu trẻ bú mẹ thường không phát hiện được. Không có báo cáo về tác dụng phụ nghiêm trọng ở trẻ bú mẹ.""",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có dấu hiệu bất thường.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng (hiếm độc tính gan)",
            "notes": """Amphotericin B không chuyển hóa qua gan đáng kể. Tuy nhiên, có thể gây độc tính gan hiếm. Không cần điều chỉnh liều ở suy gan, nhưng theo dõi men gan.""",
        },
        "overdose_management": {
            "symptoms": [
                "Suy thận cấp nặng (tăng creatinine, giảm nước tiểu)",
                "Hạ kali máu nặng (yếu cơ, rối loạn nhịp tim)",
                "Hạ magie máu nặng",
                "Thiếu máu nặng",
                "Rối loạn nhịp tim (do hạ kali máu)",
                "Sốc (hiếm)"
    ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ: bù điện giải, điều chỉnh chức năng thận",
            "treatment": [
                "Ngừng thuốc ngay lập tức",
                "Bù kali: Kali chloride IV (nếu hạ kali máu nặng - cần truyền IV, thận trọng)",
                "Bù magie: Magie sulfate IV (nếu hạ magie máu nặng)",
                "Điều chỉnh chức năng thận: Truyền dịch, theo dõi cân bằng dịch vào-ra",
                "Truyền máu nếu thiếu máu nặng",
                "Theo dõi chức năng thận, điện giải thường xuyên",
                "Theo dõi ít nhất 24-48 giờ",
                "Có thể cần lọc máu nếu suy thận nặng"
    ],
            "monitoring": """Chức năng thận (creatinine, BUN, CrCl, nước tiểu), điện giải (K, Mg, Na), công thức máu (Hgb, Hct), huyết áp, nhịp tim, ECG, cân bằng dịch vào-ra""",
        },
        "administration_instructions": {
            "oral": {
                "with_food": "N/A - chỉ có dạng IV, topical, intrathecal",
                "timing": "N/A - chỉ có dạng IV, topical, intrathecal",
            },
            "iv": {
                "reconstitution": """Pha với D5W (5% Dextrose) - KHÔNG dùng NS (tạo kết tủa). Thể tích pha: 500ml D5W cho liều 50mg. Nồng độ pha: 0.1 mg/ml (50mg/500ml). Lắc kỹ để hòa tan hoàn toàn. Bảo vệ khỏi ánh sáng (bọc bọc ngoài bằng giấy bạc hoặc túi tối màu).""",
                "infusion_rate": """Truyền IV trong 2-6 giờ (truyền chậm giảm phản ứng truyền). Tốc độ: 500ml/2-6 giờ = ~83-250ml/giờ. Premedication: Diphenhydramine 25-50mg IV, Acetaminophen 650mg PO, Hydrocortisone 25-50mg IV (trước truyền).""",
                "compatibility": [
                    "D5W (5% Dextrose) - CHỈ DÙNG D5W"
    ],
                "incompatibility": [
                    "NS (0.9% NaCl) - TẠO KẾT TỦA, KHÔNG DÙNG",
                    "Tất cả các thuốc khác - không pha chung, truyền riêng biệt",
                    "Các dung dịch có muối"
    ],
                "notes": """QUAN TRỌNG: 1) CHỈ PHA VỚI D5W (không dùng NS - tạo kết tủa), 2) Bảo vệ khỏi ánh sáng (bọc bọc ngoài), 3) Truyền chậm (2-6 giờ) để giảm phản ứng truyền, 4) Premedication trước truyền, 5) Không pha chung với bất kỳ thuốc nào, 6) Theo dõi chức năng thận chặt chẽ.""",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Amphotericin B (Fungizone, AmBisome)",
                "IDSA Guidelines - Antifungal Therapy",
                "UpToDate - Amphotericin B: Drug Information",
                "Medscape - Amphotericin B Drug Reference",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": """A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều thập kỷ (gold standard cho nhiễm nấm hệ thống)""",
        },
    },
    "Nystatin": {
        "group": "Infectious Disease - Antifungal (Polyene)",
        "vietnamese_name": "Nystatin, Mycostatin",
        "administration": ["PO (suspension, tablet)", "Topical"],
        "indications": [
            "Nhiễm nấm Candida miệng (oral candidiasis/thrush)",
            "Nhiễm nấm Candida thực quản",
            "Nhiễm nấm Candida da (topical)",
            "Nhiễm nấm Candida âm đạo (topical)"
        ],
        "contraindications": [
            "Dị ứng nystatin"
        ],
        "dosage": {
            "adult_oral_suspension": "400,000-600,000 đơn vị x 4 lần/ngày",
            "adult_oral_tablet": "500,000-1,000,000 đơn vị x 4 lần/ngày",
            "adult_topical": "Bôi 2-3 lần/ngày",
            "notes": "Không hấp thu qua đường tiêu hóa. Chỉ tác dụng tại chỗ. Súc miệng và nuốt (suspension)"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Buồn nôn, nôn (hiếm, PO)",
            "Tiêu chảy (hiếm, PO)",
            "Kích ứng da (hiếm, topical)",
            "Dị ứng (hiếm)"
        ],
        "interactions": [
            "Rất ít tương tác (không hấp thu hệ thống)"
        ],',
"pregnancy": "C - An toàn (không hấp thu)",
        "mechanism_of_action": "Nystatin là polyene antifungal, gắn với ergosterol trong màng tế bào nấm, tạo lỗ thủng trong màng, làm rò rỉ các ion và chất dinh dưỡng, dẫn đến chết tế bào nấm. Thuốc có ái lực cao với ergosterol (có trong nấm) nhưng không gắn với cholesterol (có trong tế bào người), nên an toàn cho tế bào người. Nystatin không hấp thu qua đường tiêu hóa hoặc qua da, nên chỉ tác dụng tại chỗ. Thuốc hiệu quả trên Candida species, đặc biệt Candida albicans, thường dùng cho nhiễm nấm miệng, thực quản, và da.",
        "monitoring": [
            "Đáp ứng điều trị (giảm triệu chứng, giảm mảng trắng trong miệng)",
            "Dấu hiệu dị ứng (ban da, kích ứng)",
            "Triệu chứng tiêu hóa (buồn nôn, tiêu chảy) - hiếm",
            "Tái nhiễm (nếu điều trị không đủ hoặc yếu tố nguy cơ vẫn còn)"
        ],
        "precautions": [
            "Suspension: súc miệng kỹ, giữ trong miệng vài phút, sau đó nuốt (cho nhiễm nấm thực quản)",
            "Tablet: ngậm trong miệng cho tan (cho nhiễm nấm miệng)",
            "Topical: bôi đều, rửa sạch tay sau khi bôi",
            "Tiếp tục điều trị 48 giờ sau khi hết triệu chứng",
            "Với nhiễm nấm miệng: điều trị 7-14 ngày",
            "Với nhiễm nấm thực quản: điều trị 14-21 ngày",
            "An toàn trong thai kỳ và cho con bú (không hấp thu)",
            "Rất ít tác dụng phụ do không hấp thu hệ thống",
            "Thận trọng ở bệnh nhân có vết thương mở rộng (topical)"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (không hấp thu)",
            "onset": "Tác dụng tại chỗ ngay lập tức",
            "duration": "Tác dụng tại chỗ trong vài giờ",
            "protein_binding": "Không áp dụng (không vào máu)",
            "clearance": "Không hấp thu, thải trừ qua phân (PO) hoặc rửa trôi (topical)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh đông lạnh, lắc kỹ trước khi dùng (suspension)",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications": [
            "Dị ứng nystatin"
        ],
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng nystatin"
            ],
            "tương_đối": []
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "An toàn trong thai kỳ. Nystatin không hấp thu qua đường tiêu hóa hoặc qua da, nên không vào máu và không ảnh hưởng đến thai nhi.",
            "lactation": {
                "safety": "Compatible",
                "details": "Nystatin không hấp thu hệ thống, không bài tiết vào sữa mẹ. An toàn khi cho con bú.",
                "recommendation": "Có thể dùng an toàn khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi",
            "notes": "Nystatin không hấp thu hệ thống, không chuyển hóa qua gan. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn (hiếm)",
                "Tiêu chảy (hiếm)",
                "Kích ứng da (topical)"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng thuốc",
                "Rửa miệng/da nếu cần",
                "Supportive care",
                "Theo dõi triệu chứng"
            ],
            "monitoring": "Triệu chứng lâm sàng"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn",
                "timing": "Suspension: súc miệng kỹ, giữ trong miệng vài phút, sau đó nuốt (cho nhiễm nấm thực quản). Tablet: ngậm trong miệng cho tan (cho nhiễm nấm miệng)."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "Không áp dụng",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Nystatin chỉ có dạng PO và topical, không có dạng IV."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Nystatin (Mycostatin)",
                "UpToDate - Nystatin Drug Information",
                "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"
            ],
            "last_updated": "2025-01-15",
            "evidence_level": "High (FDA-approved, extensive clinical data)"
        },
        "black_box_warnings": None,
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": [],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Clinical response"]
        },
        "guideline_tags": [
            "IDSA Candidiasis Guidelines 2024",
            "WHO Essential Medicines List"
        ],
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
    },

}

__all__ = ['POLYENES_DRUGS']
