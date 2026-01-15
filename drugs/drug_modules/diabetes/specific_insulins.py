"""Specific Insulin Types
Rapid-acting, Short-acting, Intermediate-acting, Long-acting, Ultra-long-acting insulins"""

SPECIFIC_INSULINS_DRUGS = {
    "Insulin Aspart": {
        "group": "Diabetes - Rapid-Acting Insulin",
        "vietnamese_name": "Insulin Aspart, Novolog, Fiasp",
        "administration": ["SC", "IV"],
        "indications": [
            "Đái tháo đường type 1 (bolus insulin)",
            "Đái tháo đường type 2 (bolus insulin)",
            "Điều trị tăng đường huyết sau ăn"
        ],
        "contraindications": [
            "Hạ đường huyết",
            "Dị ứng insulin aspart"
        ],
        "contraindications_detail": {
            "tuyệt_đối": [
                "Hạ đường huyết đang diễn ra (hypoglycemia)",
                "Dị ứng với insulin aspart hoặc bất kỳ thành phần nào",
                "Dị ứng với insulin nói chung"
            ],
            "tương_đối": [
                "Suy thận - cần giảm liều insulin do giảm thải trừ, tăng nguy cơ hạ đường huyết",
                "Suy gan - cần giảm liều insulin do giảm chuyển hóa glucose",
                "Bệnh nhân cao tuổi - tăng nguy cơ hạ đường huyết, cần theo dõi chặt chẽ",
                "Bệnh nhân có bệnh tim mạch - thận trọng với hạ đường huyết",
                "Phụ nữ có thai - cần điều chỉnh liều theo nhu cầu tăng lên trong thai kỳ"
            ]
        },
        "dosage": {
            "adult_start": "0.1-0.15 đơn vị/kg trước mỗi bữa ăn (bolus insulin)",
            "adult_bolus": "0.1-0.15 đơn vị/kg trước mỗi bữa ăn. Điều chỉnh theo carbohydrate (thường 1 đơn vị/10-15g carbohydrate) và đường huyết trước ăn.",
            "adult_usual": "0.5-1 đơn vị/kg/ngày (tổng liều bolus, thường chia 3 bữa). Ví dụ: 70kg → 35-70 đơn vị/ngày bolus, chia 3 bữa = 12-23 đơn vị/bữa.",
            "adult_max": "Điều chỉnh theo đường huyết, không có liều tối đa cố định. Một số bệnh nhân kháng insulin có thể cần >1 đơn vị/kg/ngày.",
            "dm_t1": "0.5-1 đơn vị/kg/ngày chia trước bữa ăn (bolus insulin). Thường dùng kết hợp với basal insulin (glargine, detemir, degludec).",
            "dm_t2": "0.1-0.15 đơn vị/kg trước mỗi bữa ăn. Thường dùng khi không kiểm soát được đường huyết sau ăn bằng thuốc uống hoặc basal insulin.",
            "elderly": "Khởi đầu liều thấp hơn (0.05-0.1 đơn vị/kg/bữa), tăng dần chậm. Người cao tuổi nhạy cảm hơn với hạ đường huyết.",
            "pregnancy": "Nhu cầu insulin tăng trong thai kỳ, đặc biệt tam cá nguyệt thứ 2 và 3. Có thể tăng 50-100% so với trước thai kỳ. Điều chỉnh liều thường xuyên.",
            "renal_adjustment_dosage": {
                "normal": "0.1-0.15 đơn vị/kg/bữa (CrCl ≥60)",
                "30_60": "Giảm liều 20-30% do giảm chuyển hóa insulin. Ví dụ: nếu liều bình thường 15 đơn vị/bữa → giảm xuống 10-12 đơn vị/bữa (CrCl 30-60)",
                "under_30": "Giảm liều 30-50% do giảm chuyển hóa insulin đáng kể. Ví dụ: nếu liều bình thường 15 đơn vị/bữa → giảm xuống 7.5-10 đơn vị/bữa (CrCl <30)",
                "dialysis": "Giảm liều 30-50%. Điều chỉnh liều sau mỗi lần lọc máu. Theo dõi đường huyết chặt chẽ."
            },
            "hepatic_adjustment_dosage": {
                "mild": "0.1-0.15 đơn vị/kg/bữa. Không cần điều chỉnh đặc biệt.",
                "moderate": "Có thể cần giảm liều 20-30% do giảm chuyển hóa glucose. Suy gan có thể gây hạ đường huyết.",
                "severe": "Có thể cần giảm liều 30-50%. Suy gan nặng có thể gây hạ đường huyết nghiêm trọng."
            },
            "administration_route": "SC (tiêm dưới da) - thường dùng. IV (tĩnh mạch) - chỉ dùng trong bệnh viện cho DKA, HHNK.",
            "frequency": "3-4 lần/ngày (trước mỗi bữa ăn chính)",
            "with_food": "Tiêm 15 phút TRƯỚC bữa ăn (Novolog). Fiasp: có thể tiêm ngay trước ăn hoặc sau ăn 20 phút. Điều chỉnh liều theo carbohydrate trong bữa ăn.",
            "timing": "Tiêm 15 phút TRƯỚC bữa ăn (Novolog). Fiasp: có thể tiêm ngay trước ăn hoặc sau ăn 20 phút. Điều chỉnh liều theo đường huyết trước ăn và carbohydrate.",
            "titration": "Tăng liều từ từ: Mỗi 2-3 ngày tăng 1-2 đơn vị/bữa nếu đường huyết sau ăn vẫn cao (>180 mg/dL). Giảm liều nếu có hạ đường huyết. Đánh giá hiệu quả sau mỗi 3-7 ngày.",
            "notes": "Rapid-acting insulin, tác dụng nhanh (onset 15 phút). Tiêm 15 phút TRƯỚC bữa ăn (Novolog). Fiasp: có thể tiêm ngay trước ăn hoặc sau ăn 20 phút. Điều chỉnh liều theo carbohydrate (insulin-to-carbohydrate ratio) và đường huyết trước ăn (correction factor). LUÔN có glucagon và glucose sẵn để điều trị hạ đường huyết."
        },
        "side_effects": [
            "Hạ đường huyết",
            "Tăng cân",
            "Phản ứng tại chỗ tiêm"
        ],
        "interactions": [
            "Beta-blocker: che dấu triệu chứng hạ đường huyết",
            "Corticosteroid: tăng đường huyết"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Insulin aspart là insulin analog rapid-acting, được tạo ra bằng cách thay proline bằng aspartic acid ở vị trí B28. Thay đổi này làm giảm khả năng tự kết hợp → hấp thu nhanh → tác dụng nhanh. Tương tự insulin lispro, có thời gian bán thải ~1 giờ, onset 15 phút, duration 3-5 giờ.",
        "monitoring": [
            "Đường huyết trước và sau bữa ăn",
            "HbA1c mỗi 3 tháng",
            "Dấu hiệu hạ đường huyết"
        ],
        "precautions": [
            "Tiêm 15 phút TRƯỚC bữa ăn",
            "LUÔN có glucagon và glucose sẵn",
            "Điều chỉnh liều theo carbohydrate và đường huyết"
        ],
        "pharmacokinetics": {
            "half_life": "~1 giờ",
            "onset": "15 phút",
            "duration": "3-5 giờ",
            "peak": "30-90 phút"
        },
        "storage": "Chưa mở: Tủ lạnh (2-8°C). Đang dùng: Nhiệt độ phòng (<30°C), dùng trong 28 ngày.",
        "black_box_warnings": "Nguy cơ hạ đường huyết nghiêm trọng có thể gây hôn mê, co giật, tử vong. Phải theo dõi đường huyết thường xuyên và có glucagon sẵn.",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "organ_toxicity": {},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "ADA Guidelines (American Diabetes Association)",
            "AACE/ACE Guidelines (American Association of Clinical Endocrinologists)"
        ],
        "references": {
            "primary_sources": [
                "FDA Drug Label - Novolog (insulin aspart), Fiasp",
                "ADA Guidelines"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA approved"
        },
        "drug_interactions": {
              "major": [],
              "moderate": [],
              "minor": [
                  {
                      "drug": "Beta-blocker: che dấu triệu chứng hạ đường huyết",
                      "mechanism": "Tương tác lâm sàng"
                  },
                  {
                      "drug": "Corticosteroid: tăng đường huyết",
                      "mechanism": "Tương tác lâm sàng"
                  }
              ]
          },
          "pregnancy_lactation": {
              "fda_category": "B",
              "pregnancy_details": "Insulin là lựa chọn an toàn trong thai kỳ. Cần điều chỉnh liều theo nhu cầu tăng lên trong thai kỳ.",
              "lactation": {
                  "safety": "Compatible",
                  "details": "Insulin không bài tiết vào sữa mẹ với lượng đáng kể.",
                  "recommendation": "An toàn khi cho con bú."
              }
          },
          "hepatic_adjustment": {
              "mild": "Không đổi",
              "moderate": "Không đổi",
              "severe": "Không đổi",
              "notes": "Insulin không chuyển hóa qua gan, không cần điều chỉnh liều ở suy gan."
          },
          "renal_adjustment": {
              "normal": "Không cần chỉnh liều",
              "30_60": "Giảm liều 25-50%. Suy thận làm giảm thải trừ insulin, tăng nguy cơ hạ đường huyết.",
              "under_30": "Giảm liều 50% hoặc hơn. Theo dõi đường huyết chặt chẽ. Tăng nguy cơ hạ đường huyết.",
              "dialysis": "Giảm liều đáng kể. Insulin được lọc một phần qua thẩm phân máu. Theo dõi đường huyết chặt chẽ trước và sau lọc máu.",
              "notes": "Insulin thải trừ qua thận. Suy thận làm giảm thải trừ insulin, tăng thời gian bán thải, tăng nguy cơ hạ đường huyết. Cần giảm liều và theo dõi đường huyết chặt chẽ."
          },
          "overdose_management": {
              "symptoms": [
                  "Hạ đường huyết nặng",
                  "Đổ mồ hôi, run, lo âu",
                  "Lú lẫn, co giật",
                  "Hôn mê"
              ],
              "antidote": "Glucagon 1mg IM/SC hoặc Dextrose 50% IV",
              "treatment": [
                  "Nếu tỉnh: uống glucose 15-20g",
                  "Nếu không tỉnh: Glucagon 1mg IM/SC hoặc Dextrose 50% 50ml IV",
                  "Theo dõi đường huyết mỗi 15-30 phút",
                  "Có thể cần truyền Dextrose 10% liên tục"
              ],
              "monitoring": "Theo dõi đường huyết liên tục, dấu hiệu sinh tồn"
          },
          "reversal_agents": {
              "available": True,
              "agents": [
                  {
                      "agent": "Glucagon",
                      "dose": "1mg IM/SC",
                      "indication": "Hạ đường huyết do insulin"
                  },
                  {
                      "agent": "Dextrose 50%",
                      "dose": "50ml IV",
                      "indication": "Hạ đường huyết nặng"
                  }
              ]
          },
          "administration_instructions": {
              "iv": {
                  "reconstitution": "Dùng insulin regular, không cần pha loãng",
                  "infusion_rate": "Theo chỉ định (ví dụ: 0.1 đơn vị/kg/giờ trong DKA)",
                  "compatibility": [
                      "Normal saline",
                      "Dextrose 5%"
                  ],
                  "incompatibility": [],
                  "notes": "Chỉ dùng trong bệnh viện với theo dõi chặt chẽ. Theo dõi đường huyết mỗi 1-2 giờ."
              },
              "sc": {
                  "technique": "Tiêm dưới da, luân phiên vị trí tiêm",
                  "timing": "30-60 phút trước bữa ăn (regular), ngay trước bữa ăn (rapid-acting), hoặc theo chỉ định (basal)",
                  "notes": "Tránh tiêm vào vùng có lipodystrophy. Luân phiên vị trí tiêm."
              }
          },
},

    "Insulin Degludec": {
        "group": "Diabetes - Ultra-Long-Acting Insulin",
        "vietnamese_name": "Insulin Degludec, Tresiba",
        "administration": ["SC"],
        "indications": [
            "Đái tháo đường type 1 (basal insulin)",
            "Đái tháo đường type 2 (basal insulin)"
        ],
        "contraindications": [
            "Hạ đường huyết",
            "Dị ứng insulin degludec"
        ],
        "contraindications_detail": {
            "tuyệt_đối": [
                "Hạ đường huyết đang diễn ra (hypoglycemia)",
                "Dị ứng với degludec hoặc bất kỳ thành phần nào",
                "Dị ứng với insulin nói chung"
            ],
            "tương_đối": [
                "Suy thận - cần giảm liều insulin do giảm thải trừ, tăng nguy cơ hạ đường huyết",
                "Suy gan - cần giảm liều insulin do giảm chuyển hóa glucose",
                "Bệnh nhân cao tuổi - tăng nguy cơ hạ đường huyết, cần theo dõi chặt chẽ",
                "Bệnh nhân có bệnh tim mạch - thận trọng với hạ đường huyết",
                "Phụ nữ có thai - cần điều chỉnh liều theo nhu cầu tăng lên trong thai kỳ"
            ]
        },
        "dosage": {
            "adult_start": "0.2-0.4 đơn vị/kg/ngày x 1 lần/ngày (basal insulin)",
            "adult_basal": "0.2-0.4 đơn vị/kg/ngày x 1 lần/ngày. Ví dụ: 70kg → 14-28 đơn vị/ngày.",
            "adult_usual": "0.2-0.4 đơn vị/kg/ngày x 1 lần/ngày. Type 1: thường 0.2-0.4 đơn vị/kg/ngày. Type 2: thường 0.1-0.3 đơn vị/kg/ngày.",
            "adult_max": "Điều chỉnh theo đường huyết, không có liều tối đa cố định.",
            "dm_t1": "0.2-0.4 đơn vị/kg/ngày x 1 lần/ngày (basal insulin). Thường dùng kết hợp với bolus insulin (rapid-acting) trước bữa ăn.",
            "dm_t2": "0.1-0.3 đơn vị/kg/ngày x 1 lần/ngày (basal insulin). Khởi đầu 0.1-0.2 đơn vị/kg/ngày, tăng dần.",
            "elderly": "Khởi đầu liều thấp hơn (0.1-0.2 đơn vị/kg/ngày), tăng dần chậm. Người cao tuổi nhạy cảm hơn với hạ đường huyết.",
            "pregnancy": "Nhu cầu insulin tăng trong thai kỳ. Có thể tăng 50-100% so với trước thai kỳ. Điều chỉnh liều thường xuyên.",
            "renal_adjustment_dosage": {
                "normal": "0.2-0.4 đơn vị/kg/ngày (CrCl ≥60)",
                "30_60": "Giảm liều 20-30% do giảm chuyển hóa insulin (CrCl 30-60)",
                "under_30": "Giảm liều 30-50% do giảm chuyển hóa insulin đáng kể (CrCl <30)",
                "dialysis": "Giảm liều 30-50%. Điều chỉnh liều sau mỗi lần lọc máu."
            },
            "hepatic_adjustment_dosage": {
                "mild": "0.2-0.4 đơn vị/kg/ngày. Không cần điều chỉnh đặc biệt.",
                "moderate": "Có thể cần giảm liều 20-30% do giảm chuyển hóa glucose.",
                "severe": "Có thể cần giảm liều 30-50%. Suy gan nặng có thể gây hạ đường huyết nghiêm trọng."
            },
            "administration_route": "SC (tiêm dưới da)",
            "frequency": "1 lần/ngày",
            "with_food": "Không phụ thuộc bữa ăn. Tiêm bất kỳ giờ nào trong ngày (linh hoạt về thời gian), nhưng nên tiêm cùng giờ mỗi ngày để duy trì nồng độ ổn định.",
            "timing": "Tiêm 1 lần/ngày, bất kỳ giờ nào trong ngày (linh hoạt về thời gian). Có thể tiêm buổi sáng, buổi tối, hoặc bất kỳ giờ nào phù hợp. Nên tiêm cùng giờ mỗi ngày để duy trì nồng độ ổn định.",
            "titration": "Tăng liều từ từ: Mỗi 3-5 ngày tăng 2-4 đơn vị nếu đường huyết trước ăn vẫn cao (>130 mg/dL). Giảm liều nếu có hạ đường huyết. Đánh giá hiệu quả sau mỗi 1-2 tuần.",
            "notes": "Ultra-long-acting insulin, tác dụng kéo dài >42 giờ → ít nguy cơ hạ đường huyết nhất trong các insulin. KHÔNG có peak tác dụng (flat profile). Tiêm 1 lần/ngày, bất kỳ giờ nào trong ngày (linh hoạt về thời gian). Có thể bỏ lỡ liều và tiêm muộn hơn (trong vòng 8 giờ) mà không ảnh hưởng nhiều. LUÔN có glucagon và glucose sẵn để điều trị hạ đường huyết."
        },
        "side_effects": [
            "Hạ đường huyết (ít nhất trong các insulin)",
            "Tăng cân",
            "Phản ứng tại chỗ tiêm"
        ],
        "interactions": [
            "Beta-blocker: che dấu triệu chứng hạ đường huyết",
            "Corticosteroid: tăng đường huyết"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Insulin degludec là insulin analog siêu dài tác dụng (ultra-long-acting), được tạo ra bằng cách loại bỏ threonine ở vị trí B30 và gắn một chuỗi acid béo (hexadecanedioic acid) vào lysine ở vị trí B29. Thay đổi này tạo ra các multihexamer ở mô dưới da → hấp thu rất chậm và đều → tác dụng kéo dài >42 giờ. KHÔNG có peak tác dụng → ít nguy cơ hạ đường huyết nhất trong các insulin. Có thể tiêm bất kỳ giờ nào trong ngày (linh hoạt về thời gian).",
        "monitoring": [
            "Đường huyết trước bữa ăn và trước khi ngủ",
            "HbA1c mỗi 3 tháng",
            "Dấu hiệu hạ đường huyết",
            "Cân nặng"
        ],
        "precautions": [
            "Tiêm 1 lần/ngày, bất kỳ giờ nào (linh hoạt)",
            "Tác dụng kéo dài >42 giờ → ít nguy cơ hạ đường huyết nhất",
            "LUÔN có glucagon và glucose sẵn",
            "Xoay vị trí tiêm"
        ],
        "pharmacokinetics": {
            "half_life": "~42 giờ",
            "onset": "1-2 giờ",
            "duration": ">42 giờ",
            "peak": "KHÔNG có peak (flat profile)"
        },
        "storage": "Chưa mở: Tủ lạnh (2-8°C). Đang dùng: Nhiệt độ phòng (<30°C), dùng trong 56 ngày.",
        "black_box_warnings": "Nguy cơ hạ đường huyết nghiêm trọng có thể gây hôn mê, co giật, tử vong. Phải theo dõi đường huyết thường xuyên và có glucagon sẵn.",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "organ_toxicity": {},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "ADA Guidelines (American Diabetes Association)",
            "AACE/ACE Guidelines (American Association of Clinical Endocrinologists)"
        ],
        "references": {
            "primary_sources": [
                "FDA Drug Label - Tresiba (insulin degludec)",
                "ADA Guidelines"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA approved"
        },
        "drug_interactions": {
              "major": [],
              "moderate": [],
              "minor": [
                  {
                      "drug": "Beta-blocker: che dấu triệu chứng hạ đường huyết",
                      "mechanism": "Tương tác lâm sàng"
                  },
                  {
                      "drug": "Corticosteroid: tăng đường huyết",
                      "mechanism": "Tương tác lâm sàng"
                  }
              ]
          },
          "pregnancy_lactation": {
              "fda_category": "B",
              "pregnancy_details": "Insulin là lựa chọn an toàn trong thai kỳ. Cần điều chỉnh liều theo nhu cầu tăng lên trong thai kỳ.",
              "lactation": {
                  "safety": "Compatible",
                  "details": "Insulin không bài tiết vào sữa mẹ với lượng đáng kể.",
                  "recommendation": "An toàn khi cho con bú."
              }
          },
          "hepatic_adjustment": {
              "mild": "Không đổi",
              "moderate": "Không đổi",
              "severe": "Không đổi",
              "notes": "Insulin không chuyển hóa qua gan, không cần điều chỉnh liều ở suy gan."
          },
          "renal_adjustment": {
              "normal": "Không cần chỉnh liều",
              "30_60": "Giảm liều 25-50%. Suy thận làm giảm thải trừ insulin, tăng nguy cơ hạ đường huyết.",
              "under_30": "Giảm liều 50% hoặc hơn. Theo dõi đường huyết chặt chẽ. Tăng nguy cơ hạ đường huyết.",
              "dialysis": "Giảm liều đáng kể. Insulin được lọc một phần qua thẩm phân máu. Theo dõi đường huyết chặt chẽ trước và sau lọc máu.",
              "notes": "Insulin thải trừ qua thận. Suy thận làm giảm thải trừ insulin, tăng thời gian bán thải, tăng nguy cơ hạ đường huyết. Cần giảm liều và theo dõi đường huyết chặt chẽ."
          },
          "overdose_management": {
              "symptoms": [
                  "Hạ đường huyết nặng",
                  "Đổ mồ hôi, run, lo âu",
                  "Lú lẫn, co giật",
                  "Hôn mê"
              ],
              "antidote": "Glucagon 1mg IM/SC hoặc Dextrose 50% IV",
              "treatment": [
                  "Nếu tỉnh: uống glucose 15-20g",
                  "Nếu không tỉnh: Glucagon 1mg IM/SC hoặc Dextrose 50% 50ml IV",
                  "Theo dõi đường huyết mỗi 15-30 phút",
                  "Có thể cần truyền Dextrose 10% liên tục"
              ],
              "monitoring": "Theo dõi đường huyết liên tục, dấu hiệu sinh tồn"
          },
          "reversal_agents": {
              "available": True,
              "agents": [
                  {
                      "agent": "Glucagon",
                      "dose": "1mg IM/SC",
                      "indication": "Hạ đường huyết do insulin"
                  },
                  {
                      "agent": "Dextrose 50%",
                      "dose": "50ml IV",
                      "indication": "Hạ đường huyết nặng"
                  }
              ]
          },
          "administration_instructions": {
              "sc": {
                  "technique": "Tiêm dưới da, luân phiên vị trí tiêm",
                  "timing": "30-60 phút trước bữa ăn (regular), ngay trước bữa ăn (rapid-acting), hoặc theo chỉ định (basal)",
                  "notes": "Tránh tiêm vào vùng có lipodystrophy. Luân phiên vị trí tiêm."
              }
          },
},
    "Insulin Detemir": {
        "group": "Diabetes - Long-Acting Insulin",
        "vietnamese_name": "Insulin Detemir, Levemir",
        "administration": ["SC"],
        "indications": [
            "Đái tháo đường type 1 (basal insulin)",
            "Đái tháo đường type 2 (basal insulin)"
        ],
        "contraindications": [
            "Hạ đường huyết",
            "Dị ứng insulin detemir"
        ],
        "contraindications_detail": {
            "tuyệt_đối": [
                "Hạ đường huyết đang diễn ra (hypoglycemia)",
                "Dị ứng với detemir hoặc bất kỳ thành phần nào",
                "Dị ứng với insulin nói chung"
            ],
            "tương_đối": [
                "Suy thận - cần giảm liều insulin do giảm thải trừ, tăng nguy cơ hạ đường huyết",
                "Suy gan - cần giảm liều insulin do giảm chuyển hóa glucose",
                "Bệnh nhân cao tuổi - tăng nguy cơ hạ đường huyết, cần theo dõi chặt chẽ",
                "Bệnh nhân có bệnh tim mạch - thận trọng với hạ đường huyết",
                "Phụ nữ có thai - cần điều chỉnh liều theo nhu cầu tăng lên trong thai kỳ"
            ]
        },
        "dosage": {
            "adult_start": "0.2-0.4 đơn vị/kg/ngày, chia 1-2 lần (basal insulin)",
            "adult_basal": "0.2-0.4 đơn vị/kg/ngày, chia 1-2 lần. Thường 1 lần/ngày, nhưng có thể cần 2 lần/ngày ở một số bệnh nhân. Ví dụ: 70kg → 14-28 đơn vị/ngày.",
            "adult_usual": "0.2-0.4 đơn vị/kg/ngày, chia 1-2 lần. Type 1: thường 0.2-0.4 đơn vị/kg/ngày. Type 2: thường 0.1-0.3 đơn vị/kg/ngày.",
            "adult_max": "Điều chỉnh theo đường huyết, không có liều tối đa cố định.",
            "dm_t1": "0.2-0.4 đơn vị/kg/ngày, chia 1-2 lần (basal insulin). Thường dùng kết hợp với bolus insulin (rapid-acting) trước bữa ăn.",
            "dm_t2": "0.1-0.3 đơn vị/kg/ngày, chia 1-2 lần (basal insulin). Khởi đầu 0.1-0.2 đơn vị/kg/ngày, tăng dần.",
            "elderly": "Khởi đầu liều thấp hơn (0.1-0.2 đơn vị/kg/ngày), tăng dần chậm. Người cao tuổi nhạy cảm hơn với hạ đường huyết.",
            "pregnancy": "Nhu cầu insulin tăng trong thai kỳ. Có thể tăng 50-100% so với trước thai kỳ. Điều chỉnh liều thường xuyên.",
            "renal_adjustment_dosage": {
                "normal": "0.2-0.4 đơn vị/kg/ngày, chia 1-2 lần (CrCl ≥60)",
                "30_60": "Giảm liều 20-30% do giảm chuyển hóa insulin (CrCl 30-60)",
                "under_30": "Giảm liều 30-50% do giảm chuyển hóa insulin đáng kể (CrCl <30)",
                "dialysis": "Giảm liều 30-50%. Điều chỉnh liều sau mỗi lần lọc máu."
            },
            "hepatic_adjustment_dosage": {
                "mild": "0.2-0.4 đơn vị/kg/ngày, chia 1-2 lần. Không cần điều chỉnh đặc biệt.",
                "moderate": "Có thể cần giảm liều 20-30% do giảm chuyển hóa glucose.",
                "severe": "Có thể cần giảm liều 30-50%. Suy gan nặng có thể gây hạ đường huyết nghiêm trọng."
            },
            "administration_route": "SC (tiêm dưới da)",
            "frequency": "1-2 lần/ngày (thường 1 lần/ngày, có thể cần 2 lần/ngày)",
            "with_food": "Không phụ thuộc bữa ăn. Tiêm cùng giờ mỗi ngày (thường buổi tối hoặc buổi sáng).",
            "timing": "Tiêm 1-2 lần/ngày. Thường 1 lần/ngày (buổi tối hoặc buổi sáng). Một số bệnh nhân có thể cần 2 lần/ngày (buổi sáng và buổi tối) để kiểm soát đường huyết tốt hơn. Tiêm cùng giờ mỗi ngày.",
            "titration": "Tăng liều từ từ: Mỗi 3-5 ngày tăng 2-4 đơn vị nếu đường huyết trước ăn vẫn cao (>130 mg/dL). Giảm liều nếu có hạ đường huyết. Đánh giá hiệu quả sau mỗi 1-2 tuần.",
            "notes": "Long-acting insulin, tác dụng kéo dài 18-24 giờ. KHÔNG có peak tác dụng (flat profile) → ít nguy cơ hạ đường huyết hơn NPH. Tiêm 1-2 lần/ngày. Có thể cần 2 lần/ngày ở một số bệnh nhân để kiểm soát đường huyết tốt hơn. LUÔN có glucagon và glucose sẵn để điều trị hạ đường huyết."
        },
        "side_effects": [
            "Hạ đường huyết (ít hơn NPH)",
            "Tăng cân",
            "Phản ứng tại chỗ tiêm"
        ],
        "interactions": [
            "Beta-blocker: che dấu triệu chứng hạ đường huyết",
            "Corticosteroid: tăng đường huyết"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Insulin detemir là insulin analog dài tác dụng (long-acting), được tạo ra bằng cách gắn một chuỗi acid béo (myristic acid) vào lysine ở vị trí B29. Chuỗi acid béo gắn với albumin trong máu → làm chậm hấp thu và kéo dài tác dụng. KHÔNG có peak tác dụng → ít nguy cơ hạ đường huyết hơn NPH. Thời gian bán thải ~12 giờ, có thể cần tiêm 2 lần/ngày ở một số bệnh nhân.",
        "monitoring": [
            "Đường huyết trước bữa ăn và trước khi ngủ",
            "HbA1c mỗi 3 tháng",
            "Dấu hiệu hạ đường huyết",
            "Cân nặng"
        ],
        "precautions": [
            "Tiêm 1-2 lần/ngày",
            "KHÔNG có peak tác dụng → ít nguy cơ hạ đường huyết hơn NPH",
            "LUÔN có glucagon và glucose sẵn",
            "Xoay vị trí tiêm"
        ],
        "pharmacokinetics": {
            "half_life": "~12 giờ",
            "onset": "1-2 giờ",
            "duration": "18-24 giờ",
            "peak": "KHÔNG có peak (flat profile)"
        },
        "storage": "Chưa mở: Tủ lạnh (2-8°C). Đang dùng: Nhiệt độ phòng (<30°C), dùng trong 42 ngày.",
        "black_box_warnings": "Nguy cơ hạ đường huyết nghiêm trọng có thể gây hôn mê, co giật, tử vong. Phải theo dõi đường huyết thường xuyên và có glucagon sẵn.",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "organ_toxicity": {},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "ADA Guidelines (American Diabetes Association)",
            "AACE/ACE Guidelines (American Association of Clinical Endocrinologists)"
        ],
        "references": {
            "primary_sources": [
                "FDA Drug Label - Levemir (insulin detemir)",
                "ADA Guidelines"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA approved"
        },
        "drug_interactions": {
              "major": [],
              "moderate": [],
              "minor": [
                  {
                      "drug": "Beta-blocker: che dấu triệu chứng hạ đường huyết",
                      "mechanism": "Tương tác lâm sàng"
                  },
                  {
                      "drug": "Corticosteroid: tăng đường huyết",
                      "mechanism": "Tương tác lâm sàng"
                  }
              ]
          },
          "pregnancy_lactation": {
              "fda_category": "B",
              "pregnancy_details": "Insulin là lựa chọn an toàn trong thai kỳ. Cần điều chỉnh liều theo nhu cầu tăng lên trong thai kỳ.",
              "lactation": {
                  "safety": "Compatible",
                  "details": "Insulin không bài tiết vào sữa mẹ với lượng đáng kể.",
                  "recommendation": "An toàn khi cho con bú."
              }
          },
          "hepatic_adjustment": {
              "mild": "Không đổi",
              "moderate": "Không đổi",
              "severe": "Không đổi",
              "notes": "Insulin không chuyển hóa qua gan, không cần điều chỉnh liều ở suy gan."
          },
          "renal_adjustment": {
              "normal": "Không cần chỉnh liều",
              "30_60": "Giảm liều 25-50%. Suy thận làm giảm thải trừ insulin, tăng nguy cơ hạ đường huyết.",
              "under_30": "Giảm liều 50% hoặc hơn. Theo dõi đường huyết chặt chẽ. Tăng nguy cơ hạ đường huyết.",
              "dialysis": "Giảm liều đáng kể. Insulin được lọc một phần qua thẩm phân máu. Theo dõi đường huyết chặt chẽ trước và sau lọc máu.",
              "notes": "Insulin thải trừ qua thận. Suy thận làm giảm thải trừ insulin, tăng thời gian bán thải, tăng nguy cơ hạ đường huyết. Cần giảm liều và theo dõi đường huyết chặt chẽ."
          },
          "overdose_management": {
              "symptoms": [
                  "Hạ đường huyết nặng",
                  "Đổ mồ hôi, run, lo âu",
                  "Lú lẫn, co giật",
                  "Hôn mê"
              ],
              "antidote": "Glucagon 1mg IM/SC hoặc Dextrose 50% IV",
              "treatment": [
                  "Nếu tỉnh: uống glucose 15-20g",
                  "Nếu không tỉnh: Glucagon 1mg IM/SC hoặc Dextrose 50% 50ml IV",
                  "Theo dõi đường huyết mỗi 15-30 phút",
                  "Có thể cần truyền Dextrose 10% liên tục"
              ],
              "monitoring": "Theo dõi đường huyết liên tục, dấu hiệu sinh tồn"
          },
          "reversal_agents": {
              "available": True,
              "agents": [
                  {
                      "agent": "Glucagon",
                      "dose": "1mg IM/SC",
                      "indication": "Hạ đường huyết do insulin"
                  },
                  {
                      "agent": "Dextrose 50%",
                      "dose": "50ml IV",
                      "indication": "Hạ đường huyết nặng"
                  }
              ]
          },
          "administration_instructions": {
              "sc": {
                  "technique": "Tiêm dưới da, luân phiên vị trí tiêm",
                  "timing": "30-60 phút trước bữa ăn (regular), ngay trước bữa ăn (rapid-acting), hoặc theo chỉ định (basal)",
                  "notes": "Tránh tiêm vào vùng có lipodystrophy. Luân phiên vị trí tiêm."
              }
          },
},

    "Insulin Glargine": {
        "group": "Diabetes - Long-Acting Insulin",
        "vietnamese_name": "Insulin Glargine, Lantus, Basaglar, Toujeo",
        "administration": ["SC"],
        "indications": [
            "Đái tháo đường type 1 (basal insulin)",
            "Đái tháo đường type 2 (basal insulin)"
        ],
        "contraindications": [
            "Hạ đường huyết",
            "Dị ứng insulin glargine"
        ],
        "contraindications_detail": {
            "tuyệt_đối": [
                "Hạ đường huyết đang diễn ra (hypoglycemia)",
                "Dị ứng với glargine hoặc bất kỳ thành phần nào",
                "Dị ứng với insulin nói chung"
            ],
            "tương_đối": [
                "Suy thận - cần giảm liều insulin do giảm thải trừ, tăng nguy cơ hạ đường huyết",
                "Suy gan - cần giảm liều insulin do giảm chuyển hóa glucose",
                "Bệnh nhân cao tuổi - tăng nguy cơ hạ đường huyết, cần theo dõi chặt chẽ",
                "Bệnh nhân có bệnh tim mạch - thận trọng với hạ đường huyết",
                "Phụ nữ có thai - cần điều chỉnh liều theo nhu cầu tăng lên trong thai kỳ"
            ]
        },
        "dosage": {
            "adult_start": "0.2-0.4 đơn vị/kg/ngày x 1 lần/ngày (basal insulin)",
            "adult_basal": "0.2-0.4 đơn vị/kg/ngày x 1 lần/ngày. Ví dụ: 70kg → 14-28 đơn vị/ngày.",
            "adult_usual": "0.2-0.4 đơn vị/kg/ngày x 1 lần/ngày. Type 1: thường 0.2-0.4 đơn vị/kg/ngày. Type 2: thường 0.1-0.3 đơn vị/kg/ngày.",
            "adult_max": "Điều chỉnh theo đường huyết, không có liều tối đa cố định.",
            "toujeo": "Toujeo (U-300, nồng độ cao hơn): liều cao hơn 20-30% so với Lantus (U-100). Ví dụ: nếu Lantus 20 đơn vị/ngày → Toujeo 24-26 đơn vị/ngày. Tác dụng kéo dài hơn Lantus.",
            "dm_t1": "0.2-0.4 đơn vị/kg/ngày x 1 lần/ngày (basal insulin). Thường dùng kết hợp với bolus insulin (rapid-acting) trước bữa ăn.",
            "dm_t2": "0.1-0.3 đơn vị/kg/ngày x 1 lần/ngày (basal insulin). Khởi đầu 0.1-0.2 đơn vị/kg/ngày, tăng dần.",
            "elderly": "Khởi đầu liều thấp hơn (0.1-0.2 đơn vị/kg/ngày), tăng dần chậm. Người cao tuổi nhạy cảm hơn với hạ đường huyết.",
            "pregnancy": "Nhu cầu insulin tăng trong thai kỳ. Có thể tăng 50-100% so với trước thai kỳ. Điều chỉnh liều thường xuyên.",
            "renal_adjustment_dosage": {
                "normal": "0.2-0.4 đơn vị/kg/ngày x 1 lần/ngày (CrCl ≥60)",
                "30_60": "Giảm liều 20-30% do giảm chuyển hóa insulin (CrCl 30-60)",
                "under_30": "Giảm liều 30-50% do giảm chuyển hóa insulin đáng kể (CrCl <30)",
                "dialysis": "Giảm liều 30-50%. Điều chỉnh liều sau mỗi lần lọc máu."
            },
            "hepatic_adjustment_dosage": {
                "mild": "0.2-0.4 đơn vị/kg/ngày x 1 lần/ngày. Không cần điều chỉnh đặc biệt.",
                "moderate": "Có thể cần giảm liều 20-30% do giảm chuyển hóa glucose.",
                "severe": "Có thể cần giảm liều 30-50%. Suy gan nặng có thể gây hạ đường huyết nghiêm trọng."
            },
            "administration_route": "SC (tiêm dưới da)",
            "frequency": "1 lần/ngày",
            "with_food": "Không phụ thuộc bữa ăn. Tiêm cùng giờ mỗi ngày (thường buổi tối).",
            "timing": "Tiêm 1 lần/ngày, cùng giờ mỗi ngày (thường buổi tối). Có thể tiêm buổi sáng nếu phù hợp hơn. Tiêm cùng giờ mỗi ngày để duy trì nồng độ ổn định.",
            "titration": "Tăng liều từ từ: Mỗi 3-5 ngày tăng 2-4 đơn vị nếu đường huyết trước ăn vẫn cao (>130 mg/dL). Giảm liều nếu có hạ đường huyết. Đánh giá hiệu quả sau mỗi 1-2 tuần.",
            "notes": "Long-acting insulin, tác dụng kéo dài 18-24 giờ. KHÔNG có peak tác dụng (flat profile) → ít nguy cơ hạ đường huyết hơn NPH. Tiêm 1 lần/ngày, cùng giờ mỗi ngày (thường buổi tối). Toujeo (U-300): liều cao hơn 20-30% so với Lantus, tác dụng kéo dài hơn. KHÔNG được trộn với insulin khác trong cùng ống tiêm. LUÔN có glucagon và glucose sẵn để điều trị hạ đường huyết."
        },
        "side_effects": [
            "Hạ đường huyết (ít hơn NPH)",
            "Tăng cân",
            "Phản ứng tại chỗ tiêm",
            "Đau tại chỗ tiêm (nhẹ)"
        ],
        "interactions": [
            "Beta-blocker: che dấu triệu chứng hạ đường huyết",
            "Corticosteroid: tăng đường huyết"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Insulin glargine là insulin analog dài tác dụng (long-acting), được tạo ra bằng cách thay asparagine bằng glycine ở vị trí A21 và thêm 2 arginine ở vị trí B30. Thay đổi này làm insulin kết tủa ở pH trung tính → hấp thu chậm và đều → tác dụng kéo dài 24 giờ. KHÔNG có peak tác dụng → ít nguy cơ hạ đường huyết hơn NPH. Toujeo là dạng U-300 (nồng độ cao hơn) → tác dụng kéo dài hơn.",
        "monitoring": [
            "Đường huyết trước bữa ăn và trước khi ngủ",
            "HbA1c mỗi 3 tháng",
            "Dấu hiệu hạ đường huyết",
            "Cân nặng"
        ],
        "precautions": [
            "Tiêm 1 lần/ngày, cùng giờ mỗi ngày",
            "KHÔNG có peak tác dụng → ít nguy cơ hạ đường huyết hơn NPH",
            "LUÔN có glucagon và glucose sẵn",
            "Xoay vị trí tiêm",
            "KHÔNG được trộn với insulin khác trong cùng ống tiêm"
        ],
        "pharmacokinetics": {
            "half_life": "12-24 giờ",
            "onset": "1-2 giờ",
            "duration": "18-24 giờ",
            "peak": "KHÔNG có peak (flat profile)"
        },
        "storage": "Chưa mở: Tủ lạnh (2-8°C). Đang dùng: Nhiệt độ phòng (<30°C), dùng trong 28 ngày.",
        "black_box_warnings": "Nguy cơ hạ đường huyết nghiêm trọng có thể gây hôn mê, co giật, tử vong. Phải theo dõi đường huyết thường xuyên và có glucagon sẵn.",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "organ_toxicity": {},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "ADA Guidelines (American Diabetes Association)",
            "AACE/ACE Guidelines (American Association of Clinical Endocrinologists)"
        ],
        "references": {
            "primary_sources": [
                "FDA Drug Label - Lantus (insulin glargine), Basaglar, Toujeo",
                "ADA Guidelines"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA approved, extensive clinical use"
        },
        "drug_interactions": {
              "major": [],
              "moderate": [],
              "minor": [
                  {
                      "drug": "Beta-blocker: che dấu triệu chứng hạ đường huyết",
                      "mechanism": "Tương tác lâm sàng"
                  },
                  {
                      "drug": "Corticosteroid: tăng đường huyết",
                      "mechanism": "Tương tác lâm sàng"
                  }
              ]
          },
          "pregnancy_lactation": {
              "fda_category": "B",
              "pregnancy_details": "Insulin là lựa chọn an toàn trong thai kỳ. Cần điều chỉnh liều theo nhu cầu tăng lên trong thai kỳ.",
              "lactation": {
                  "safety": "Compatible",
                  "details": "Insulin không bài tiết vào sữa mẹ với lượng đáng kể.",
                  "recommendation": "An toàn khi cho con bú."
              }
          },
          "hepatic_adjustment": {
              "mild": "Không đổi",
              "moderate": "Không đổi",
              "severe": "Không đổi",
              "notes": "Insulin không chuyển hóa qua gan, không cần điều chỉnh liều ở suy gan."
          },
          "renal_adjustment": {
              "normal": "Không cần chỉnh liều",
              "30_60": "Giảm liều 25-50%. Suy thận làm giảm thải trừ insulin, tăng nguy cơ hạ đường huyết.",
              "under_30": "Giảm liều 50% hoặc hơn. Theo dõi đường huyết chặt chẽ. Tăng nguy cơ hạ đường huyết.",
              "dialysis": "Giảm liều đáng kể. Insulin được lọc một phần qua thẩm phân máu. Theo dõi đường huyết chặt chẽ trước và sau lọc máu.",
              "notes": "Insulin thải trừ qua thận. Suy thận làm giảm thải trừ insulin, tăng thời gian bán thải, tăng nguy cơ hạ đường huyết. Cần giảm liều và theo dõi đường huyết chặt chẽ."
          },
          "overdose_management": {
              "symptoms": [
                  "Hạ đường huyết nặng",
                  "Đổ mồ hôi, run, lo âu",
                  "Lú lẫn, co giật",
                  "Hôn mê"
              ],
              "antidote": "Glucagon 1mg IM/SC hoặc Dextrose 50% IV",
              "treatment": [
                  "Nếu tỉnh: uống glucose 15-20g",
                  "Nếu không tỉnh: Glucagon 1mg IM/SC hoặc Dextrose 50% 50ml IV",
                  "Theo dõi đường huyết mỗi 15-30 phút",
                  "Có thể cần truyền Dextrose 10% liên tục"
              ],
              "monitoring": "Theo dõi đường huyết liên tục, dấu hiệu sinh tồn"
          },
          "reversal_agents": {
              "available": True,
              "agents": [
                  {
                      "agent": "Glucagon",
                      "dose": "1mg IM/SC",
                      "indication": "Hạ đường huyết do insulin"
                  },
                  {
                      "agent": "Dextrose 50%",
                      "dose": "50ml IV",
                      "indication": "Hạ đường huyết nặng"
                  }
              ]
          },
          "administration_instructions": {
              "sc": {
                  "technique": "Tiêm dưới da, luân phiên vị trí tiêm",
                  "timing": "30-60 phút trước bữa ăn (regular), ngay trước bữa ăn (rapid-acting), hoặc theo chỉ định (basal)",
                  "notes": "Tránh tiêm vào vùng có lipodystrophy. Luân phiên vị trí tiêm."
              }
          },
},

    "Insulin Glulisine": {
        "group": "Diabetes - Rapid-Acting Insulin",
        "vietnamese_name": "Insulin Glulisine, Apidra",
        "administration": ["SC", "IV"],
        "indications": [
            "Đái tháo đường type 1 (bolus insulin)",
            "Đái tháo đường type 2 (bolus insulin)"
        ],
        "contraindications": [
            "Hạ đường huyết",
            "Dị ứng insulin glulisine"
        ],
        "contraindications_detail": {
            "tuyệt_đối": [
                "Hạ đường huyết đang diễn ra (hypoglycemia)",
                "Dị ứng với glulisine hoặc bất kỳ thành phần nào",
                "Dị ứng với insulin nói chung"
            ],
            "tương_đối": [
                "Suy thận - cần giảm liều insulin do giảm thải trừ, tăng nguy cơ hạ đường huyết",
                "Suy gan - cần giảm liều insulin do giảm chuyển hóa glucose",
                "Bệnh nhân cao tuổi - tăng nguy cơ hạ đường huyết, cần theo dõi chặt chẽ",
                "Bệnh nhân có bệnh tim mạch - thận trọng với hạ đường huyết",
                "Phụ nữ có thai - cần điều chỉnh liều theo nhu cầu tăng lên trong thai kỳ"
            ]
        },
        "dosage": {
            "adult_start": "0.1-0.15 đơn vị/kg trước mỗi bữa ăn (bolus insulin)",
            "adult_bolus": "0.1-0.15 đơn vị/kg trước mỗi bữa ăn. Điều chỉnh theo carbohydrate (thường 1 đơn vị/10-15g carbohydrate) và đường huyết trước ăn.",
            "adult_usual": "0.5-1 đơn vị/kg/ngày (tổng liều bolus, thường chia 3 bữa). Ví dụ: 70kg → 35-70 đơn vị/ngày bolus, chia 3 bữa = 12-23 đơn vị/bữa.",
            "adult_max": "Điều chỉnh theo đường huyết, không có liều tối đa cố định.",
            "dm_t1": "0.5-1 đơn vị/kg/ngày chia trước bữa ăn (bolus insulin). Thường dùng kết hợp với basal insulin.",
            "dm_t2": "0.1-0.15 đơn vị/kg trước mỗi bữa ăn. Thường dùng khi không kiểm soát được đường huyết sau ăn.",
            "elderly": "Khởi đầu liều thấp hơn (0.05-0.1 đơn vị/kg/bữa), tăng dần chậm. Người cao tuổi nhạy cảm hơn với hạ đường huyết.",
            "pregnancy": "Nhu cầu insulin tăng trong thai kỳ. Có thể tăng 50-100% so với trước thai kỳ. Điều chỉnh liều thường xuyên.",
            "renal_adjustment_dosage": {
                "normal": "0.1-0.15 đơn vị/kg/bữa (CrCl ≥60)",
                "30_60": "Giảm liều 20-30% do giảm chuyển hóa insulin (CrCl 30-60)",
                "under_30": "Giảm liều 30-50% do giảm chuyển hóa insulin đáng kể (CrCl <30)",
                "dialysis": "Giảm liều 30-50%. Điều chỉnh liều sau mỗi lần lọc máu."
            },
            "hepatic_adjustment_dosage": {
                "mild": "0.1-0.15 đơn vị/kg/bữa. Không cần điều chỉnh đặc biệt.",
                "moderate": "Có thể cần giảm liều 20-30% do giảm chuyển hóa glucose.",
                "severe": "Có thể cần giảm liều 30-50%. Suy gan nặng có thể gây hạ đường huyết nghiêm trọng."
            },
            "administration_route": "SC (tiêm dưới da) - thường dùng. IV (tĩnh mạch) - chỉ dùng trong bệnh viện cho DKA, HHNK.",
            "frequency": "3-4 lần/ngày (trước mỗi bữa ăn chính)",
            "with_food": "Tiêm 15 phút TRƯỚC bữa ăn hoặc ngay sau khi bắt đầu ăn. Điều chỉnh liều theo carbohydrate trong bữa ăn.",
            "timing": "Tiêm 15 phút TRƯỚC bữa ăn hoặc ngay sau khi bắt đầu ăn. Điều chỉnh liều theo đường huyết trước ăn và carbohydrate.",
            "titration": "Tăng liều từ từ: Mỗi 2-3 ngày tăng 1-2 đơn vị/bữa nếu đường huyết sau ăn vẫn cao (>180 mg/dL). Giảm liều nếu có hạ đường huyết. Đánh giá hiệu quả sau mỗi 3-7 ngày.",
            "notes": "Rapid-acting insulin, tác dụng nhanh (onset 15 phút). Tiêm 15 phút TRƯỚC bữa ăn hoặc ngay sau khi bắt đầu ăn. Điều chỉnh liều theo carbohydrate (insulin-to-carbohydrate ratio) và đường huyết trước ăn (correction factor). LUÔN có glucagon và glucose sẵn để điều trị hạ đường huyết."
        },
        "side_effects": [
            "Hạ đường huyết",
            "Tăng cân",
            "Phản ứng tại chỗ tiêm"
        ],
        "interactions": [
            "Beta-blocker: che dấu triệu chứng hạ đường huyết",
            "Corticosteroid: tăng đường huyết"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Insulin glulisine là insulin analog rapid-acting, được tạo ra bằng cách thay asparagine bằng lysine ở vị trí B3 và glutamic acid bằng lysine ở vị trí B29. Tương tự insulin lispro và aspart, có tác dụng nhanh, onset 15 phút, duration 3-5 giờ.",
        "monitoring": [
            "Đường huyết trước và sau bữa ăn",
            "HbA1c mỗi 3 tháng",
            "Dấu hiệu hạ đường huyết"
        ],
        "precautions": [
            "Tiêm 15 phút TRƯỚC bữa ăn hoặc ngay sau khi bắt đầu ăn",
            "LUÔN có glucagon và glucose sẵn"
        ],
        "pharmacokinetics": {
            "half_life": "~1 giờ",
            "onset": "15 phút",
            "duration": "3-5 giờ",
            "peak": "30-90 phút"
        },
        "storage": "Chưa mở: Tủ lạnh (2-8°C). Đang dùng: Nhiệt độ phòng (<30°C), dùng trong 28 ngày.",
        "black_box_warnings": "Nguy cơ hạ đường huyết nghiêm trọng có thể gây hôn mê, co giật, tử vong. Phải theo dõi đường huyết thường xuyên và có glucagon sẵn.",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "organ_toxicity": {},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "ADA Guidelines (American Diabetes Association)",
            "AACE/ACE Guidelines (American Association of Clinical Endocrinologists)"
        ],
        "references": {
            "primary_sources": [
                "FDA Drug Label - Apidra (insulin glulisine)",
                "ADA Guidelines"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA approved"
        },
        "drug_interactions": {
              "major": [],
              "moderate": [],
              "minor": [
                  {
                      "drug": "Beta-blocker: che dấu triệu chứng hạ đường huyết",
                      "mechanism": "Tương tác lâm sàng"
                  },
                  {
                      "drug": "Corticosteroid: tăng đường huyết",
                      "mechanism": "Tương tác lâm sàng"
                  }
              ]
          },
          "pregnancy_lactation": {
              "fda_category": "B",
              "pregnancy_details": "Insulin là lựa chọn an toàn trong thai kỳ. Cần điều chỉnh liều theo nhu cầu tăng lên trong thai kỳ.",
              "lactation": {
                  "safety": "Compatible",
                  "details": "Insulin không bài tiết vào sữa mẹ với lượng đáng kể.",
                  "recommendation": "An toàn khi cho con bú."
              }
          },
          "hepatic_adjustment": {
              "mild": "Không đổi",
              "moderate": "Không đổi",
              "severe": "Không đổi",
              "notes": "Insulin không chuyển hóa qua gan, không cần điều chỉnh liều ở suy gan."
          },
          "renal_adjustment": {
              "normal": "Không cần chỉnh liều",
              "30_60": "Giảm liều 25-50%. Suy thận làm giảm thải trừ insulin, tăng nguy cơ hạ đường huyết.",
              "under_30": "Giảm liều 50% hoặc hơn. Theo dõi đường huyết chặt chẽ. Tăng nguy cơ hạ đường huyết.",
              "dialysis": "Giảm liều đáng kể. Insulin được lọc một phần qua thẩm phân máu. Theo dõi đường huyết chặt chẽ trước và sau lọc máu.",
              "notes": "Insulin thải trừ qua thận. Suy thận làm giảm thải trừ insulin, tăng thời gian bán thải, tăng nguy cơ hạ đường huyết. Cần giảm liều và theo dõi đường huyết chặt chẽ."
          },
          "overdose_management": {
              "symptoms": [
                  "Hạ đường huyết nặng",
                  "Đổ mồ hôi, run, lo âu",
                  "Lú lẫn, co giật",
                  "Hôn mê"
              ],
              "antidote": "Glucagon 1mg IM/SC hoặc Dextrose 50% IV",
              "treatment": [
                  "Nếu tỉnh: uống glucose 15-20g",
                  "Nếu không tỉnh: Glucagon 1mg IM/SC hoặc Dextrose 50% 50ml IV",
                  "Theo dõi đường huyết mỗi 15-30 phút",
                  "Có thể cần truyền Dextrose 10% liên tục"
              ],
              "monitoring": "Theo dõi đường huyết liên tục, dấu hiệu sinh tồn"
          },
          "reversal_agents": {
              "available": True,
              "agents": [
                  {
                      "agent": "Glucagon",
                      "dose": "1mg IM/SC",
                      "indication": "Hạ đường huyết do insulin"
                  },
                  {
                      "agent": "Dextrose 50%",
                      "dose": "50ml IV",
                      "indication": "Hạ đường huyết nặng"
                  }
              ]
          },
          "administration_instructions": {
              "iv": {
                  "reconstitution": "Dùng insulin regular, không cần pha loãng",
                  "infusion_rate": "Theo chỉ định (ví dụ: 0.1 đơn vị/kg/giờ trong DKA)",
                  "compatibility": [
                      "Normal saline",
                      "Dextrose 5%"
                  ],
                  "incompatibility": [],
                  "notes": "Chỉ dùng trong bệnh viện với theo dõi chặt chẽ. Theo dõi đường huyết mỗi 1-2 giờ."
              },
              "sc": {
                  "technique": "Tiêm dưới da, luân phiên vị trí tiêm",
                  "timing": "30-60 phút trước bữa ăn (regular), ngay trước bữa ăn (rapid-acting), hoặc theo chỉ định (basal)",
                  "notes": "Tránh tiêm vào vùng có lipodystrophy. Luân phiên vị trí tiêm."
              }
          },
},

    "Insulin Lispro": {
        "group": "Diabetes - Rapid-Acting Insulin",
        "vietnamese_name": "Insulin Lispro, Humalog",
        "administration": ["SC", "IV"],
        "indications": [
            "Đái tháo đường type 1 (bolus insulin)",
            "Đái tháo đường type 2 (bolus insulin)",
            "Điều trị tăng đường huyết sau ăn"
        ],
        "contraindications": [
            "Hạ đường huyết",
            "Dị ứng insulin lispro"
        ],
        "contraindications_detail": {
            "tuyệt_đối": [
                "Hạ đường huyết đang diễn ra (hypoglycemia)",
                "Dị ứng với lispro hoặc bất kỳ thành phần nào",
                "Dị ứng với insulin nói chung"
            ],
            "tương_đối": [
                "Suy thận - cần giảm liều insulin do giảm thải trừ, tăng nguy cơ hạ đường huyết",
                "Suy gan - cần giảm liều insulin do giảm chuyển hóa glucose",
                "Bệnh nhân cao tuổi - tăng nguy cơ hạ đường huyết, cần theo dõi chặt chẽ",
                "Bệnh nhân có bệnh tim mạch - thận trọng với hạ đường huyết",
                "Phụ nữ có thai - cần điều chỉnh liều theo nhu cầu tăng lên trong thai kỳ"
            ]
        },
        "dosage": {
            "adult_start": "0.1-0.15 đơn vị/kg trước mỗi bữa ăn (bolus insulin)",
            "adult_bolus": "0.1-0.15 đơn vị/kg trước mỗi bữa ăn. Điều chỉnh theo carbohydrate (thường 1 đơn vị/10-15g carbohydrate) và đường huyết trước ăn.",
            "adult_correction": "Điều chỉnh theo sliding scale hoặc insulin-to-carbohydrate ratio. Correction factor: thường 1 đơn vị giảm đường huyết 30-50 mg/dL (tùy độ nhạy cảm insulin).",
            "adult_usual": "0.5-1 đơn vị/kg/ngày (tổng liều bolus, thường chia 3 bữa). Ví dụ: 70kg → 35-70 đơn vị/ngày bolus, chia 3 bữa = 12-23 đơn vị/bữa.",
            "adult_max": "Điều chỉnh theo đường huyết, không có liều tối đa cố định.",
            "dm_t1": "0.5-1 đơn vị/kg/ngày chia trước bữa ăn (bolus insulin). Thường dùng kết hợp với basal insulin.",
            "dm_t2": "0.1-0.15 đơn vị/kg trước mỗi bữa ăn. Thường dùng khi không kiểm soát được đường huyết sau ăn.",
            "elderly": "Khởi đầu liều thấp hơn (0.05-0.1 đơn vị/kg/bữa), tăng dần chậm. Người cao tuổi nhạy cảm hơn với hạ đường huyết.",
            "pregnancy": "Nhu cầu insulin tăng trong thai kỳ. Có thể tăng 50-100% so với trước thai kỳ. Điều chỉnh liều thường xuyên.",
            "renal_adjustment_dosage": {
                "normal": "0.1-0.15 đơn vị/kg/bữa (CrCl ≥60)",
                "30_60": "Giảm liều 20-30% do giảm chuyển hóa insulin (CrCl 30-60)",
                "under_30": "Giảm liều 30-50% do giảm chuyển hóa insulin đáng kể (CrCl <30)",
                "dialysis": "Giảm liều 30-50%. Điều chỉnh liều sau mỗi lần lọc máu."
            },
            "hepatic_adjustment_dosage": {
                "mild": "0.1-0.15 đơn vị/kg/bữa. Không cần điều chỉnh đặc biệt.",
                "moderate": "Có thể cần giảm liều 20-30% do giảm chuyển hóa glucose.",
                "severe": "Có thể cần giảm liều 30-50%. Suy gan nặng có thể gây hạ đường huyết nghiêm trọng."
            },
            "administration_route": "SC (tiêm dưới da) - thường dùng. IV (tĩnh mạch) - chỉ dùng trong bệnh viện cho DKA, HHNK.",
            "frequency": "3-4 lần/ngày (trước mỗi bữa ăn chính)",
            "with_food": "Tiêm 15 phút TRƯỚC bữa ăn (hoặc ngay trước ăn). Điều chỉnh liều theo carbohydrate trong bữa ăn.",
            "timing": "Tiêm 15 phút TRƯỚC bữa ăn (hoặc ngay trước ăn). Tác dụng nhanh nhất trong các insulin. Điều chỉnh liều theo đường huyết trước ăn và carbohydrate.",
            "titration": "Tăng liều từ từ: Mỗi 2-3 ngày tăng 1-2 đơn vị/bữa nếu đường huyết sau ăn vẫn cao (>180 mg/dL). Giảm liều nếu có hạ đường huyết. Đánh giá hiệu quả sau mỗi 3-7 ngày.",
            "notes": "Rapid-acting insulin, tác dụng nhanh nhất trong các insulin (onset 15 phút). Tiêm 15 phút TRƯỚC bữa ăn (hoặc ngay trước ăn). Điều chỉnh liều theo carbohydrate (insulin-to-carbohydrate ratio) và đường huyết trước ăn (correction factor). LUÔN có glucagon và glucose sẵn để điều trị hạ đường huyết."
        },
        "side_effects": [
            "Hạ đường huyết (nguy hiểm)",
            "Tăng cân",
            "Phản ứng tại chỗ tiêm",
            "Lipodystrophy (hiếm)"
        ],
        "interactions": [
            "Beta-blocker: che dấu triệu chứng hạ đường huyết",
            "Corticosteroid: tăng đường huyết",
            "Rượu: tăng nguy cơ hạ đường huyết"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Insulin lispro là insulin analog rapid-acting, được tạo ra bằng cách đổi vị trí proline và lysine ở vị trí B28 và B29. Thay đổi này làm giảm khả năng tự kết hợp của insulin → hấp thu nhanh hơn từ mô dưới da → tác dụng nhanh hơn insulin regular. Insulin lispro có thời gian bán thải ~1 giờ, onset 15 phút, duration 3-5 giờ. Phù hợp cho bolus insulin (trước bữa ăn) để kiểm soát đường huyết sau ăn.",
        "monitoring": [
            "Đường huyết trước và sau bữa ăn",
            "HbA1c mỗi 3 tháng",
            "Dấu hiệu hạ đường huyết",
            "Cân nặng"
        ],
        "precautions": [
            "Tiêm 15 phút TRƯỚC bữa ăn (hoặc ngay trước ăn)",
            "LUÔN có glucagon và glucose sẵn",
            "Điều chỉnh liều theo carbohydrate và đường huyết",
            "Xoay vị trí tiêm",
            "Bảo quản trong tủ lạnh trước khi mở"
        ],
        "pharmacokinetics": {
            "half_life": "~1 giờ",
            "onset": "15 phút",
            "duration": "3-5 giờ",
            "peak": "30-90 phút"
        },
        "storage": "Chưa mở: Tủ lạnh (2-8°C). Đang dùng: Nhiệt độ phòng (<30°C), dùng trong 28 ngày.",
        "black_box_warnings": "Nguy cơ hạ đường huyết nghiêm trọng có thể gây hôn mê, co giật, tử vong. Phải theo dõi đường huyết thường xuyên và có glucagon sẵn.",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "organ_toxicity": {},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "ADA Guidelines (American Diabetes Association)",
            "AACE/ACE Guidelines (American Association of Clinical Endocrinologists)"
        ],
        "references": {
            "primary_sources": [
                "FDA Drug Label - Humalog (insulin lispro)",
                "ADA Guidelines - Insulin therapy"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA approved, extensive clinical use"
        },
        "drug_interactions": {
             "major": [],
             "moderate": [],
             "minor": [
                 {
                     "drug": "Beta-blocker: che dấu triệu chứng hạ đường huyết",
                     "mechanism": "Tương tác lâm sàng"
                 },
                 {
                     "drug": "Corticosteroid: tăng đường huyết",
                     "mechanism": "Tương tác lâm sàng"
                 },
                 {
                     "drug": "Rượu: tăng nguy cơ hạ đường huyết",
                     "mechanism": "Tương tác lâm sàng"
                 }
             ]
         },
         "pregnancy_lactation": {
             "fda_category": "B",
             "pregnancy_details": "Insulin là lựa chọn an toàn trong thai kỳ. Cần điều chỉnh liều theo nhu cầu tăng lên trong thai kỳ.",
             "lactation": {
                 "safety": "Compatible",
                 "details": "Insulin không bài tiết vào sữa mẹ với lượng đáng kể.",
                 "recommendation": "An toàn khi cho con bú."
             }
         },
         "hepatic_adjustment": {
             "mild": "Không đổi",
             "moderate": "Không đổi",
             "severe": "Không đổi",
             "notes": "Insulin không chuyển hóa qua gan, không cần điều chỉnh liều ở suy gan."
         },
          "renal_adjustment": {
              "normal": "Không cần chỉnh liều",
              "30_60": "Giảm liều 25-50%. Suy thận làm giảm thải trừ insulin, tăng nguy cơ hạ đường huyết.",
              "under_30": "Giảm liều 50% hoặc hơn. Theo dõi đường huyết chặt chẽ. Tăng nguy cơ hạ đường huyết.",
              "dialysis": "Giảm liều đáng kể. Insulin được lọc một phần qua thẩm phân máu. Theo dõi đường huyết chặt chẽ trước và sau lọc máu.",
              "notes": "Insulin thải trừ qua thận. Suy thận làm giảm thải trừ insulin, tăng thời gian bán thải, tăng nguy cơ hạ đường huyết. Cần giảm liều và theo dõi đường huyết chặt chẽ."
          },
         "overdose_management": {
             "symptoms": [
                 "Hạ đường huyết nặng",
                 "Đổ mồ hôi, run, lo âu",
                 "Lú lẫn, co giật",
                 "Hôn mê"
             ],
             "antidote": "Glucagon 1mg IM/SC hoặc Dextrose 50% IV",
             "treatment": [
                 "Nếu tỉnh: uống glucose 15-20g",
                 "Nếu không tỉnh: Glucagon 1mg IM/SC hoặc Dextrose 50% 50ml IV",
                 "Theo dõi đường huyết mỗi 15-30 phút",
                 "Có thể cần truyền Dextrose 10% liên tục"
             ],
             "monitoring": "Theo dõi đường huyết liên tục, dấu hiệu sinh tồn"
         },
         "reversal_agents": {
             "available": True,
             "agents": [
                 {
                     "agent": "Glucagon",
                     "dose": "1mg IM/SC",
                     "indication": "Hạ đường huyết do insulin"
                 },
                 {
                     "agent": "Dextrose 50%",
                     "dose": "50ml IV",
                     "indication": "Hạ đường huyết nặng"
                 }
             ]
         },
         "administration_instructions": {
             "iv": {
                 "reconstitution": "Dùng insulin regular, không cần pha loãng",
                 "infusion_rate": "Theo chỉ định (ví dụ: 0.1 đơn vị/kg/giờ trong DKA)",
                 "compatibility": [
                     "Normal saline",
                     "Dextrose 5%"
                 ],
                 "incompatibility": [],
                 "notes": "Chỉ dùng trong bệnh viện với theo dõi chặt chẽ. Theo dõi đường huyết mỗi 1-2 giờ."
             },
             "sc": {
                 "technique": "Tiêm dưới da, luân phiên vị trí tiêm",
                 "timing": "30-60 phút trước bữa ăn (regular), ngay trước bữa ăn (rapid-acting), hoặc theo chỉ định (basal)",
                 "notes": "Tránh tiêm vào vùng có lipodystrophy. Luân phiên vị trí tiêm."
             }
         },
},

    "Insulin NPH": {
        "group": "Diabetes - Intermediate-Acting Insulin",
        "vietnamese_name": "Insulin NPH, Humulin N, Novolin N",
        "administration": ["SC"],
        "indications": [
            "Đái tháo đường type 1 (basal insulin)",
            "Đái tháo đường type 2 (basal insulin)"
        ],
        "contraindications": [
            "Hạ đường huyết",
            "Dị ứng insulin"
        ],
        "contraindications_detail": {
            "tuyệt_đối": [
                "Hạ đường huyết đang diễn ra (hypoglycemia)",
                "Dị ứng với nph hoặc bất kỳ thành phần nào",
                "Dị ứng với insulin nói chung"
            ],
            "tương_đối": [
                "Suy thận - cần giảm liều insulin do giảm thải trừ, tăng nguy cơ hạ đường huyết",
                "Suy gan - cần giảm liều insulin do giảm chuyển hóa glucose",
                "Bệnh nhân cao tuổi - tăng nguy cơ hạ đường huyết, cần theo dõi chặt chẽ",
                "Bệnh nhân có bệnh tim mạch - thận trọng với hạ đường huyết",
                "Phụ nữ có thai - cần điều chỉnh liều theo nhu cầu tăng lên trong thai kỳ"
            ]
        },
        "dosage": {
            "adult_start": "0.2-0.4 đơn vị/kg/ngày, chia 1-2 lần (basal insulin)",
            "adult_basal": "0.2-0.4 đơn vị/kg/ngày, chia 1-2 lần. Thường 1-2 lần/ngày. Ví dụ: 70kg → 14-28 đơn vị/ngày.",
            "adult_usual": "0.2-0.4 đơn vị/kg/ngày, chia 1-2 lần. Type 1: thường 0.2-0.4 đơn vị/kg/ngày. Type 2: thường 0.1-0.3 đơn vị/kg/ngày.",
            "adult_max": "Điều chỉnh theo đường huyết, không có liều tối đa cố định.",
            "dm_t1": "0.2-0.4 đơn vị/kg/ngày, chia 1-2 lần (basal insulin). Thường dùng kết hợp với bolus insulin (rapid-acting) trước bữa ăn.",
            "dm_t2": "0.1-0.3 đơn vị/kg/ngày, chia 1-2 lần (basal insulin). Khởi đầu 0.1-0.2 đơn vị/kg/ngày, tăng dần.",
            "elderly": "Khởi đầu liều thấp hơn (0.1-0.2 đơn vị/kg/ngày), tăng dần chậm. Người cao tuổi nhạy cảm hơn với hạ đường huyết, đặc biệt vào giờ peak.",
            "pregnancy": "Nhu cầu insulin tăng trong thai kỳ. Có thể tăng 50-100% so với trước thai kỳ. Điều chỉnh liều thường xuyên. Cẩn thận với peak tác dụng.",
            "renal_adjustment_dosage": {
                "normal": "0.2-0.4 đơn vị/kg/ngày, chia 1-2 lần (CrCl ≥60)",
                "30_60": "Giảm liều 20-30% do giảm chuyển hóa insulin. Cẩn thận với peak tác dụng (CrCl 30-60)",
                "under_30": "Giảm liều 30-50% do giảm chuyển hóa insulin đáng kể. Cẩn thận với peak tác dụng (CrCl <30)",
                "dialysis": "Giảm liều 30-50%. Điều chỉnh liều sau mỗi lần lọc máu. Cẩn thận với peak tác dụng."
            },
            "hepatic_adjustment_dosage": {
                "mild": "0.2-0.4 đơn vị/kg/ngày, chia 1-2 lần. Không cần điều chỉnh đặc biệt.",
                "moderate": "Có thể cần giảm liều 20-30% do giảm chuyển hóa glucose. Cẩn thận với peak tác dụng.",
                "severe": "Có thể cần giảm liều 30-50%. Suy gan nặng có thể gây hạ đường huyết nghiêm trọng, đặc biệt vào giờ peak."
            },
            "administration_route": "SC (tiêm dưới da)",
            "frequency": "1-2 lần/ngày (thường 1-2 lần/ngày)",
            "with_food": "Không phụ thuộc bữa ăn. Tiêm cùng giờ mỗi ngày. Cẩn thận với peak tác dụng (2-8 giờ sau tiêm) → có thể cần ăn nhẹ vào giờ peak.",
            "timing": "Tiêm 1-2 lần/ngày, cùng giờ mỗi ngày (thường buổi sáng và/hoặc buổi tối). Có peak tác dụng (2-8 giờ sau tiêm) → nguy cơ hạ đường huyết giữa các bữa ăn. Có thể cần ăn nhẹ vào giờ peak.",
            "titration": "Tăng liều từ từ: Mỗi 3-5 ngày tăng 2-4 đơn vị nếu đường huyết trước ăn vẫn cao (>130 mg/dL). Giảm liều nếu có hạ đường huyết, đặc biệt vào giờ peak. Đánh giá hiệu quả sau mỗi 1-2 tuần.",
            "notes": "Intermediate-acting insulin, tác dụng kéo dài 12-16 giờ. Có peak tác dụng (2-8 giờ sau tiêm) → nguy cơ hạ đường huyết giữa các bữa ăn cao hơn long-acting insulin không có peak. Tiêm 1-2 lần/ngày. Cẩn thận với hạ đường huyết vào giờ peak. Có thể cần ăn nhẹ vào giờ peak. LUÔN có glucagon và glucose sẵn để điều trị hạ đường huyết."
        },
        "side_effects": [
            "Hạ đường huyết (đặc biệt vào giờ peak)",
            "Tăng cân",
            "Phản ứng tại chỗ tiêm"
        ],
        "interactions": [
            "Beta-blocker: che dấu triệu chứng hạ đường huyết",
            "Corticosteroid: tăng đường huyết"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Insulin NPH (Neutral Protamine Hagedorn) là insulin trung tác dụng (intermediate-acting), được tạo ra bằng cách thêm protamine và zinc vào insulin regular → làm chậm hấp thu → tác dụng kéo dài. Có thời gian bán thải 8-12 giờ, onset 1-3 giờ, duration 12-16 giờ. Có peak tác dụng (2-8 giờ sau tiêm) → nguy cơ hạ đường huyết cao hơn so với long-acting insulin không có peak.",
        "monitoring": [
            "Đường huyết trước bữa ăn và trước khi ngủ",
            "HbA1c mỗi 3 tháng",
            "Dấu hiệu hạ đường huyết (đặc biệt vào giờ peak)",
            "Cân nặng"
        ],
        "precautions": [
            "Có peak tác dụng → nguy cơ hạ đường huyết cao hơn long-acting insulin",
            "Tiêm 1-2 lần/ngày",
            "LUÔN có glucagon và glucose sẵn",
            "Xoay vị trí tiêm"
        ],
        "pharmacokinetics": {
            "half_life": "8-12 giờ",
            "onset": "1-3 giờ",
            "duration": "12-16 giờ",
            "peak": "2-8 giờ sau tiêm"
        },
        "storage": "Chưa mở: Tủ lạnh (2-8°C). Đang dùng: Nhiệt độ phòng (<30°C), dùng trong 28 ngày.",
        "black_box_warnings": "Nguy cơ hạ đường huyết nghiêm trọng có thể gây hôn mê, co giật, tử vong. Phải theo dõi đường huyết thường xuyên và có glucagon sẵn.",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "organ_toxicity": {},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "ADA Guidelines (American Diabetes Association)",
            "AACE/ACE Guidelines (American Association of Clinical Endocrinologists)"
        ],
        "references": {
            "primary_sources": [
                "FDA Drug Label - Humulin N, Novolin N",
                "ADA Guidelines"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA approved, extensive clinical use"
        },
        "drug_interactions": {
              "major": [],
              "moderate": [],
              "minor": [
                  {
                      "drug": "Beta-blocker: che dấu triệu chứng hạ đường huyết",
                      "mechanism": "Tương tác lâm sàng"
                  },
                  {
                      "drug": "Corticosteroid: tăng đường huyết",
                      "mechanism": "Tương tác lâm sàng"
                  }
              ]
          },
          "pregnancy_lactation": {
              "fda_category": "B",
              "pregnancy_details": "Insulin là lựa chọn an toàn trong thai kỳ. Cần điều chỉnh liều theo nhu cầu tăng lên trong thai kỳ.",
              "lactation": {
                  "safety": "Compatible",
                  "details": "Insulin không bài tiết vào sữa mẹ với lượng đáng kể.",
                  "recommendation": "An toàn khi cho con bú."
              }
          },
          "hepatic_adjustment": {
              "mild": "Không đổi",
              "moderate": "Không đổi",
              "severe": "Không đổi",
              "notes": "Insulin không chuyển hóa qua gan, không cần điều chỉnh liều ở suy gan."
          },
          "renal_adjustment": {
              "normal": "Không cần chỉnh liều",
              "30_60": "Giảm liều 25-50%. Suy thận làm giảm thải trừ insulin, tăng nguy cơ hạ đường huyết.",
              "under_30": "Giảm liều 50% hoặc hơn. Theo dõi đường huyết chặt chẽ. Tăng nguy cơ hạ đường huyết.",
              "dialysis": "Giảm liều đáng kể. Insulin được lọc một phần qua thẩm phân máu. Theo dõi đường huyết chặt chẽ trước và sau lọc máu.",
              "notes": "Insulin thải trừ qua thận. Suy thận làm giảm thải trừ insulin, tăng thời gian bán thải, tăng nguy cơ hạ đường huyết. Cần giảm liều và theo dõi đường huyết chặt chẽ."
          },
          "overdose_management": {
              "symptoms": [
                  "Hạ đường huyết nặng",
                  "Đổ mồ hôi, run, lo âu",
                  "Lú lẫn, co giật",
                  "Hôn mê"
              ],
              "antidote": "Glucagon 1mg IM/SC hoặc Dextrose 50% IV",
              "treatment": [
                  "Nếu tỉnh: uống glucose 15-20g",
                  "Nếu không tỉnh: Glucagon 1mg IM/SC hoặc Dextrose 50% 50ml IV",
                  "Theo dõi đường huyết mỗi 15-30 phút",
                  "Có thể cần truyền Dextrose 10% liên tục"
              ],
              "monitoring": "Theo dõi đường huyết liên tục, dấu hiệu sinh tồn"
          },
          "reversal_agents": {
              "available": True,
              "agents": [
                  {
                      "agent": "Glucagon",
                      "dose": "1mg IM/SC",
                      "indication": "Hạ đường huyết do insulin"
                  },
                  {
                      "agent": "Dextrose 50%",
                      "dose": "50ml IV",
                      "indication": "Hạ đường huyết nặng"
                  }
              ]
          },
          "administration_instructions": {
              "sc": {
                  "technique": "Tiêm dưới da, luân phiên vị trí tiêm",
                  "timing": "30-60 phút trước bữa ăn (regular), ngay trước bữa ăn (rapid-acting), hoặc theo chỉ định (basal)",
                  "notes": "Tránh tiêm vào vùng có lipodystrophy. Luân phiên vị trí tiêm."
              }
          },
},

    "Insulin Regular": {
        "group": "Diabetes - Short-Acting Insulin",
        "vietnamese_name": "Insulin Regular, Humulin R, Novolin R",
        "administration": ["SC", "IV"],
        "indications": [
            "Đái tháo đường type 1 (bolus insulin)",
            "Đái tháo đường type 2 (bolus insulin)",
            "Nhiễm toan ceton do đái tháo đường (IV)",
            "Tăng đường huyết trong bệnh viện (IV)"
        ],
        "contraindications": [
            "Hạ đường huyết",
            "Dị ứng insulin"
        ],
        "contraindications_detail": {
            "tuyệt_đối": [
                "Hạ đường huyết đang diễn ra (hypoglycemia)",
                "Dị ứng với regular hoặc bất kỳ thành phần nào",
                "Dị ứng với insulin nói chung"
            ],
            "tương_đối": [
                "Suy thận - cần giảm liều insulin do giảm thải trừ, tăng nguy cơ hạ đường huyết",
                "Suy gan - cần giảm liều insulin do giảm chuyển hóa glucose",
                "Bệnh nhân cao tuổi - tăng nguy cơ hạ đường huyết, cần theo dõi chặt chẽ",
                "Bệnh nhân có bệnh tim mạch - thận trọng với hạ đường huyết",
                "Phụ nữ có thai - cần điều chỉnh liều theo nhu cầu tăng lên trong thai kỳ"
            ]
        },
        "dosage": {
            "adult_start": "0.1-0.15 đơn vị/kg trước mỗi bữa ăn (SC bolus insulin)",
            "sc_bolus": "0.1-0.15 đơn vị/kg trước mỗi bữa ăn. Điều chỉnh theo carbohydrate và đường huyết trước ăn.",
            "adult_usual": "0.5-1 đơn vị/kg/ngày (tổng liều bolus, thường chia 3 bữa). Ví dụ: 70kg → 35-70 đơn vị/ngày bolus, chia 3 bữa = 12-23 đơn vị/bữa.",
            "adult_max": "Điều chỉnh theo đường huyết, không có liều tối đa cố định.",
            "dm_t1": "0.5-1 đơn vị/kg/ngày chia trước bữa ăn (bolus insulin). Thường dùng kết hợp với basal insulin.",
            "dm_t2": "0.1-0.15 đơn vị/kg trước mỗi bữa ăn. Thường dùng khi không kiểm soát được đường huyết sau ăn.",
            "dka_iv": "0.1 đơn vị/kg/giờ IV truyền liên tục (sau khi bù dịch và điện giải). Ví dụ: 70kg → 7 đơn vị/giờ. Mục tiêu: giảm đường huyết 50-75 mg/dL/giờ. Khi đường huyết <200 mg/dL, giảm tốc độ truyền xuống 0.05-0.1 đơn vị/kg/giờ và thêm dextrose vào dịch truyền.",
            "dka_initial_bolus": "0.1 đơn vị/kg IV bolus (tùy chọn, không bắt buộc) trước khi truyền liên tục. Ví dụ: 70kg → 7 đơn vị IV bolus.",
            "hospital_hyperglycemia_iv": "0.05-0.1 đơn vị/kg/giờ IV truyền liên tục. Mục tiêu đường huyết: 140-180 mg/dL. Điều chỉnh tốc độ truyền theo đường huyết mỗi 1-2 giờ.",
            "elderly": "Khởi đầu liều thấp hơn (0.05-0.1 đơn vị/kg/bữa), tăng dần chậm. Người cao tuổi nhạy cảm hơn với hạ đường huyết.",
            "pregnancy": "Nhu cầu insulin tăng trong thai kỳ. Có thể tăng 50-100% so với trước thai kỳ. Điều chỉnh liều thường xuyên.",
            "renal_adjustment_dosage": {
                "normal": "0.1-0.15 đơn vị/kg/bữa (SC) hoặc 0.05-0.1 đơn vị/kg/giờ (IV) (CrCl ≥60)",
                "30_60": "Giảm liều 20-30% do giảm chuyển hóa insulin (CrCl 30-60)",
                "under_30": "Giảm liều 30-50% do giảm chuyển hóa insulin đáng kể (CrCl <30)",
                "dialysis": "Giảm liều 30-50%. Điều chỉnh liều sau mỗi lần lọc máu."
            },
            "hepatic_adjustment_dosage": {
                "mild": "0.1-0.15 đơn vị/kg/bữa (SC) hoặc 0.05-0.1 đơn vị/kg/giờ (IV). Không cần điều chỉnh đặc biệt.",
                "moderate": "Có thể cần giảm liều 20-30% do giảm chuyển hóa glucose.",
                "severe": "Có thể cần giảm liều 30-50%. Suy gan nặng có thể gây hạ đường huyết nghiêm trọng."
            },
            "administration_route": "SC (tiêm dưới da) - thường dùng. IV (tĩnh mạch) - chỉ dùng trong bệnh viện cho DKA, HHNK, tăng đường huyết nặng.",
            "frequency": "3-4 lần/ngày (SC, trước mỗi bữa ăn chính) hoặc truyền liên tục (IV)",
            "with_food": "SC: Tiêm 30-60 phút TRƯỚC bữa ăn. Điều chỉnh liều theo carbohydrate trong bữa ăn. IV: Không phụ thuộc bữa ăn.",
            "timing": "SC: Tiêm 30-60 phút TRƯỚC bữa ăn (sớm hơn rapid-acting insulin). IV: Truyền liên tục với tốc độ 0.05-0.1 đơn vị/kg/giờ, điều chỉnh theo đường huyết mỗi 1-2 giờ.",
            "titration": "SC: Tăng liều từ từ: Mỗi 2-3 ngày tăng 1-2 đơn vị/bữa nếu đường huyết sau ăn vẫn cao (>180 mg/dL). IV: Điều chỉnh tốc độ truyền theo đường huyết mỗi 1-2 giờ.",
            "notes": "Short-acting insulin, tác dụng chậm hơn rapid-acting (onset 30-60 phút). Tiêm 30-60 phút TRƯỚC bữa ăn (sớm hơn rapid-acting insulin). Có thể dùng IV trong DKA hoặc tăng đường huyết nặng trong bệnh viện (0.05-0.1 đơn vị/kg/giờ truyền liên tục). Điều chỉnh liều theo carbohydrate và đường huyết trước ăn. LUÔN có glucagon và glucose sẵn để điều trị hạ đường huyết."
        },
        "side_effects": [
            "Hạ đường huyết",
            "Tăng cân",
            "Phản ứng tại chỗ tiêm"
        ],
        "interactions": [
            "Beta-blocker: che dấu triệu chứng hạ đường huyết",
            "Corticosteroid: tăng đường huyết"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Insulin regular là insulin ngắn tác dụng (short-acting), là insulin tự nhiên. Có thời gian bán thải 2-4 giờ, onset 30-60 phút, duration 6-8 giờ. Phù hợp cho bolus insulin nhưng cần tiêm sớm hơn so với rapid-acting insulin. Có thể dùng IV trong DKA hoặc tăng đường huyết nặng.",
        "monitoring": [
            "Đường huyết trước và sau bữa ăn",
            "HbA1c mỗi 3 tháng",
            "Dấu hiệu hạ đường huyết",
            "Nếu IV: đường huyết mỗi 1-2 giờ"
        ],
        "precautions": [
            "Tiêm 30-60 phút TRƯỚC bữa ăn",
            "LUÔN có glucagon và glucose sẵn",
            "IV chỉ dùng trong bệnh viện với theo dõi chặt chẽ"
        ],
        "pharmacokinetics": {
            "half_life": "2-4 giờ",
            "onset": "30-60 phút",
            "duration": "6-8 giờ",
            "peak": "2-4 giờ"
        },
        "storage": "Chưa mở: Tủ lạnh (2-8°C). Đang dùng: Nhiệt độ phòng (<30°C), dùng trong 28 ngày.",
        "black_box_warnings": "Nguy cơ hạ đường huyết nghiêm trọng có thể gây hôn mê, co giật, tử vong. Phải theo dõi đường huyết thường xuyên và có glucagon sẵn.",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "organ_toxicity": {},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "ADA Guidelines (American Diabetes Association)",
            "AACE/ACE Guidelines (American Association of Clinical Endocrinologists)"
        ],
        "references": {
            "primary_sources": [
                "FDA Drug Label - Humulin R, Novolin R",
                "ADA Guidelines"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA approved, extensive clinical use"
        },
        "drug_interactions": {
              "major": [],
              "moderate": [],
              "minor": [
                  {
                      "drug": "Beta-blocker: che dấu triệu chứng hạ đường huyết",
                      "mechanism": "Tương tác lâm sàng"
                  },
                  {
                      "drug": "Corticosteroid: tăng đường huyết",
                      "mechanism": "Tương tác lâm sàng"
                  }
              ]
          },
          "pregnancy_lactation": {
              "fda_category": "B",
              "pregnancy_details": "Insulin là lựa chọn an toàn trong thai kỳ. Cần điều chỉnh liều theo nhu cầu tăng lên trong thai kỳ.",
              "lactation": {
                  "safety": "Compatible",
                  "details": "Insulin không bài tiết vào sữa mẹ với lượng đáng kể.",
                  "recommendation": "An toàn khi cho con bú."
              }
          },
          "hepatic_adjustment": {
              "mild": "Không đổi",
              "moderate": "Không đổi",
              "severe": "Không đổi",
              "notes": "Insulin không chuyển hóa qua gan, không cần điều chỉnh liều ở suy gan."
          },
          "renal_adjustment": {
              "normal": "Không cần chỉnh liều",
              "30_60": "Giảm liều 25-50%. Suy thận làm giảm thải trừ insulin, tăng nguy cơ hạ đường huyết.",
              "under_30": "Giảm liều 50% hoặc hơn. Theo dõi đường huyết chặt chẽ. Tăng nguy cơ hạ đường huyết.",
              "dialysis": "Giảm liều đáng kể. Insulin được lọc một phần qua thẩm phân máu. Theo dõi đường huyết chặt chẽ trước và sau lọc máu.",
              "notes": "Insulin thải trừ qua thận. Suy thận làm giảm thải trừ insulin, tăng thời gian bán thải, tăng nguy cơ hạ đường huyết. Cần giảm liều và theo dõi đường huyết chặt chẽ."
          },
          "overdose_management": {
              "symptoms": [
                  "Hạ đường huyết nặng",
                  "Đổ mồ hôi, run, lo âu",
                  "Lú lẫn, co giật",
                  "Hôn mê"
              ],
              "antidote": "Glucagon 1mg IM/SC hoặc Dextrose 50% IV",
              "treatment": [
                  "Nếu tỉnh: uống glucose 15-20g",
                  "Nếu không tỉnh: Glucagon 1mg IM/SC hoặc Dextrose 50% 50ml IV",
                  "Theo dõi đường huyết mỗi 15-30 phút",
                  "Có thể cần truyền Dextrose 10% liên tục"
              ],
              "monitoring": "Theo dõi đường huyết liên tục, dấu hiệu sinh tồn"
          },
          "reversal_agents": {
              "available": True,
              "agents": [
                  {
                      "agent": "Glucagon",
                      "dose": "1mg IM/SC",
                      "indication": "Hạ đường huyết do insulin"
                  },
                  {
                      "agent": "Dextrose 50%",
                      "dose": "50ml IV",
                      "indication": "Hạ đường huyết nặng"
                  }
              ]
          },
          "administration_instructions": {
              "iv": {
                  "reconstitution": "Dùng insulin regular, không cần pha loãng",
                  "infusion_rate": "Theo chỉ định (ví dụ: 0.1 đơn vị/kg/giờ trong DKA)",
                  "compatibility": [
                      "Normal saline",
                      "Dextrose 5%"
                  ],
                  "incompatibility": [],
                  "notes": "Chỉ dùng trong bệnh viện với theo dõi chặt chẽ. Theo dõi đường huyết mỗi 1-2 giờ."
              },
              "sc": {
                  "technique": "Tiêm dưới da, luân phiên vị trí tiêm",
                  "timing": "30-60 phút trước bữa ăn (regular), ngay trước bữa ăn (rapid-acting), hoặc theo chỉ định (basal)",
                  "notes": "Tránh tiêm vào vùng có lipodystrophy. Luân phiên vị trí tiêm."
              }
          },
},

}

__all__ = ['SPECIFIC_INSULINS_DRUGS']

