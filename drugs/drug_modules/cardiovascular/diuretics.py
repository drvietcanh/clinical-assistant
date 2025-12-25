"""
Diuretics - Water Pills
"""

DIURETICS = {
    "Furosemide": {
        "group": "Cardiovascular - Loop Diuretic",
        "vietnamese_name": "Furosemide, Lasix",
        "administration": ["PO", "IV", "IM"],
        "indications": [
            "Phù (suy tim, xơ gan, suy thận)",
            "Tăng huyết áp",
            "Suy tim cấp",
            "Tăng kali máu"
        ],
        "contraindications": [
            "Vô niệu",
            "Mất nước nặng",
            "Hạ kali máu nặng",
            "Dị ứng sulfonamide"
        ],
        "dosage": {
            "adult_po": "20-80mg x 1-2 lần/ngày",
            "adult_iv": "20-80mg IV (có thể lặp lại)",
            "adult_iv_continuous": "5-40mg/giờ truyền liên tục",
            "heart_failure_acute": "20-40mg IV, có thể lặp lại",
            "notes": "Theo dõi cân bằng dịch, điện giải"
        },
        "side_effects": [
            "Hạ kali máu",
            "Hạ natri máu",
            "Mất nước",
            "Tăng acid uric",
            "Điếc tạm thời (IV liều cao)",
            "Tăng đường huyết"
        ],
        "interactions": [
            "Digoxin: tăng nguy cơ ngộ độc digoxin (hạ kali)",
            "Aminoglycosides: tăng độc tính thính giác",
            "NSAID: giảm hiệu quả",
            "Lithium: tăng nồng độ lithium"
        ],
        "pregnancy": "C",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": ["renal_hypoperfusion", "ototoxicity", "electrolyte_disturbance"]
        },
        "guideline_tags": [
            "ACC/AHA/HFSA HFrEF diuretic",
            "ESC HFrEF diuretic"
        ],
        "mechanism_of_action": "Ức chế đồng vận chuyển Na-K-2Cl ở quai Henle, tăng thải natri, kali, clo, và nước",
        "monitoring": [
            "Điện giải (K, Na, Cl) trước điều trị và định kỳ",
            "Cân bằng dịch vào-ra, cân nặng",
            "Creatinine, BUN",
            "Acid uric nếu dùng lâu dài",
            "Thính giác nếu IV liều cao hoặc suy thận"
        ],
        "precautions": [
            "Theo dõi sát điện giải, đặc biệt kali",
            "Bù kali nếu cần",
            "Tránh dùng quá liều (gây mất nước, suy thận)",
            "Thận trọng với bệnh nhân suy thận (có thể cần liều cao hơn)",
            "Tránh dùng IV liều cao ở bệnh nhân suy thận (nguy cơ điếc)"
        ],
        "pharmacokinetics": {
            "half_life": "2 giờ (PO), 1 giờ (IV)",
            "onset": "30-60 phút (PO), 5 phút (IV)",
            "duration": "6-8 giờ",
            "protein_binding": ">98%",
            "clearance": "Thận (50%) và gan"
                },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng",
        "black_box_warnings": "Có thể gây mất nước và rối loạn điện giải nghiêm trọng. Điếc có thể xảy ra với liều IV cao hoặc dùng nhanh. Hạ kali máu có thể làm tăng nguy cơ ngộ độc digoxin và rối loạn nhịp tim",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Digoxin",
                    "mechanism": "Furosemide gây hạ kali máu, tăng nguy cơ ngộ độc digoxin",
                    "effect": "Tăng nguy cơ ngộ độc digoxin (nhịp tim chậm, block AV, rối loạn nhịp tim)",
                    "management": "Theo dõi kali máu thường xuyên. Bù kali nếu cần. Theo dõi nồng độ digoxin. Theo dõi ECG."
                },
                {
                    "drug": "Aminoglycosides (gentamicin, tobramycin, amikacin)",
                    "mechanism": "Cả hai đều gây độc tính thính giác, tác dụng hiệp đồng",
                    "effect": "Tăng nguy cơ điếc vĩnh viễn, đặc biệt với furosemide IV liều cao",
                    "management": "Thận trọng. Tránh dùng furosemide IV liều cao cùng aminoglycosides. Theo dõi thính giác nếu cần dùng cùng."
                },
                {
                    "drug": "Lithium",
                    "mechanism": "Furosemide giảm thải trừ lithium qua thận (do giảm thể tích máu), tăng nồng độ lithium",
                    "effect": "Tăng nồng độ lithium, tăng nguy cơ độc tính lithium",
                    "management": "Theo dõi nồng độ lithium. Có thể cần giảm liều lithium. Theo dõi dấu hiệu độc tính lithium."
                }
            ],
            "moderate": [
                {
                    "drug": "NSAIDs (ibuprofen, naproxen, diclofenac, indomethacin)",
                    "mechanism": "NSAID giảm tác dụng lợi tiểu của furosemide (do giảm prostaglandin, giảm lưu lượng máu thận)",
                    "effect": "Giảm hiệu quả lợi tiểu, giảm hạ huyết áp",
                    "management": "Thận trọng. Theo dõi đáp ứng lợi tiểu. Có thể cần tăng liều furosemide. Tránh dùng lâu dài cùng."
                },
                {
                    "drug": "ACE inhibitors, ARBs",
                    "mechanism": "Tác dụng hiệp đồng hạ huyết áp, tăng nguy cơ hạ huyết áp quá mức",
                    "effect": "Tăng nguy cơ hạ huyết áp, suy thận cấp",
                    "management": "Thận trọng khi bắt đầu. Có thể cần giảm liều furosemide hoặc ACE inhibitor. Theo dõi huyết áp, chức năng thận."
                },
                {
                    "drug": "Corticosteroids",
                    "mechanism": "Corticosteroid gây giữ natri, giảm hiệu quả lợi tiểu",
                    "effect": "Giảm hiệu quả lợi tiểu",
                    "management": "Theo dõi đáp ứng lợi tiểu. Có thể cần tăng liều furosemide."
                }
            ],
            "minor": [
                {
                    "drug": "Probenecid",
                    "mechanism": "Probenecid ức chế bài tiết furosemide qua thận",
                    "effect": "Giảm hiệu quả lợi tiểu",
                    "management": "Có thể cần tăng liều furosemide."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Vô niệu",
                "Mất nước nặng",
                "Hạ kali máu nặng",
                "Dị ứng sulfonamide",
                "Dị ứng furosemide"
            ],
            "tương_đối": [
                "Suy thận nặng - có thể cần liều cao hơn (nhưng thận trọng với IV liều cao - nguy cơ điếc)",
                "Suy gan nặng - thận trọng (thải một phần qua gan)",
                "Hạ natri máu - điều chỉnh trước khi dùng",
                "Hạ magie máu - bù magie trước khi dùng",
                "Dùng với digoxin - tăng nguy cơ ngộ độc digoxin",
                "Dùng với aminoglycosides - tăng nguy cơ điếc",
                "Dùng với lithium - tăng nồng độ lithium"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Có thể gây giảm thể tích máu, giảm tưới máu nhau thai. Có thể gây giảm nước ối, thiếu máu thai nhi. Cân nhắc lợi ích/nguy cơ. Thường dùng được trong suy tim thai kỳ hoặc phù nếu lợi ích vượt trội nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Furosemide bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp. Không có báo cáo về tác dụng phụ nghiêm trọng ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có dấu hiệu mất nước, rối loạn điện giải."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng (thải một phần qua gan)",
            "severe": "Thận trọng (thải một phần qua gan)",
            "notes": "Furosemide thải qua cả thận (50%) và gan (50%). Suy gan có thể ảnh hưởng một phần đến dược động học nhưng thường không cần điều chỉnh liều đáng kể."
        },
        "overdose_management": {
            "symptoms": [
                "Mất nước nặng",
                "Hạ kali máu nặng (yếu cơ, rối loạn nhịp tim)",
                "Hạ natri máu nặng (lú lẫn, co giật)",
                "Hạ magie máu",
                "Hạ canxi máu",
                "Suy thận cấp (do mất nước)",
                "Điếc (với IV liều cao)",
                "Hạ huyết áp"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ: bù dịch, điện giải",
            "treatment": [
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Bù dịch: Truyền normal saline hoặc lactated Ringer's để bù mất nước",
                "Bù điện giải: Kali chloride (nếu hạ kali máu), Magie sulfate (nếu hạ magie máu), Calcium (nếu hạ canxi máu)",
                "Theo dõi điện giải thường xuyên (K, Na, Mg, Ca, Cl)",
                "Theo dõi chức năng thận (creatinine, BUN, nước tiểu)",
                "Theo dõi huyết áp, nhịp tim, ECG",
                "Nếu có điếc (với IV): Ngừng ngay, phần lớn hồi phục nhưng có thể không hoàn toàn ở liều rất cao",
                "Theo dõi ít nhất 12-24 giờ"
            ],
            "monitoring": "Điện giải (K, Na, Mg, Ca, Cl), chức năng thận (creatinine, BUN, nước tiểu), huyết áp, nhịp tim, ECG, cân bằng dịch, thính giác (nếu IV liều cao)"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Uống với thức ăn có thể giảm kích ứng dạ dày.",
                "timing": "Uống 1-2 lần/ngày (sáng và chiều). Uống buổi sáng để tránh đi tiểu đêm. Theo dõi cân bằng dịch, cân nặng."
            },
            "iv": {
                "reconstitution": "Furosemide IV: Pha với D5W hoặc normal saline. Nồng độ: 10mg/ml. KHÔNG pha với các dung dịch có pH <5.5 (kết tủa).",
                "infusion_rate": "Bolus: 20-80mg IV qua 1-2 phút. Có thể lặp lại mỗi 2 giờ nếu cần. Continuous infusion: 5-40mg/giờ, điều chỉnh theo đáp ứng. KHÔNG truyền quá nhanh (nguy cơ điếc).",
                "compatibility": ["D5W", "Normal saline", "Lactated Ringer's"],
                "incompatibility": ["Không trộn với các thuốc khác (pH <5.5 gây kết tủa)"],
                "notes": "Furosemide IV dùng cho suy tim cấp, phù nặng. Theo dõi điện giải, cân bằng dịch sát. KHÔNG truyền quá nhanh (nguy cơ điếc). Thận trọng ở suy thận (có thể cần liều cao nhưng tránh tốc độ cao - nguy cơ điếc)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Lasix (furosemide)",
                "UpToDate - Furosemide: Drug information",
                "DOSE Study - New England Journal of Medicine (2011) - Furosemide trong suy tim cấp",
                "American Heart Association/American College of Cardiology guidelines - Heart failure"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - Extensive clinical experience and RCTs (DOSE study) in acute heart failure"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"renal": "Moderate (hypoperfusion)", "ototoxicity": "Moderate (high dose IV)", "metabolic": "High (electrolyte disturbances)"}
        },
        "guideline_tags": [
            "ACC/AHA/HFSA Guidelines - Heart Failure",
            "ESC Guidelines - Heart Failure",
            "DOSE Study - Acute Heart Failure",
            "KDIGO Guidelines - Acute Kidney Injury",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18",
    },

    "Hydrochlorothiazide": {
        "group": "Cardiovascular - Thiazide Diuretic",
        "vietnamese_name": "Hydrochlorothiazide, HCTZ",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp",
            "Phù (suy tim nhẹ)",
            "Sỏi thận canxi"
        ],
        "contraindications": [
            "Dị ứng sulfonamide",
            "Vô niệu",
            "Hạ kali máu nặng"
        ],
        "dosage": {
            "adult_htn": "12.5-50mg x 1 lần/ngày",
            "adult_edema": "25-100mg x 1-2 lần/ngày",
            "notes": "Liều thấp (12.5-25mg) đủ cho tăng huyết áp"
        },
        "side_effects": [
            "Hạ kali máu",
            "Hạ natri máu",
            "Tăng đường huyết",
            "Tăng acid uric",
            "Tăng cholesterol"
        ],
                  "interactions": [
              "Digoxin: tăng nguy cơ ngộ độc digoxin",
              "Lithium: tăng nồng độ lithium",
              "NSAID: giảm hiệu quả"
          ],
          "pregnancy": "C",
          "mechanism_of_action": "Thiazide diuretic. Ức chế Na+/Cl- cotransporter ở đoạn xa của ống thận (distal convoluted tubule), tăng bài tiết Na+, Cl-, và nước, gây lợi tiểu. Giảm thể tích máu và giảm huyết áp. Tăng bài tiết K+, Mg2+, nhưng giữ lại Ca2+ (khác với loop diuretics).",
          "monitoring": [
              "Kali máu (mỗi 1-3 tháng, đặc biệt khi bắt đầu) - HCTZ gây hạ kali máu",
              "Natri máu - có thể gây hạ natri máu, đặc biệt ở người già",
              "Creatinine, BUN - có thể tăng nhẹ (không phải suy thận thật)",
              "Đường huyết - có thể tăng đường huyết, đặc biệt ở bệnh nhân đái tháo đường",
              "Acid uric - HCTZ gây tăng acid uric, có thể gây gout",
              "Lipid máu - có thể tăng cholesterol, triglycerides nhẹ",
              "Canxi máu - HCTZ có thể gây tăng canxi máu nhẹ (do giữ lại Ca2+)"
          ],
          "precautions": [
              "Liều thấp (12.5-25mg/ngày) đủ cho tăng huyết áp, ít tác dụng phụ hơn liều cao",
              "Thường cần bổ sung kali hoặc dùng với kali-sparing diuretic (spironolactone, amiloride)",
              "Thận trọng ở người già (tăng nguy cơ hạ natri máu)",
              "Thận trọng ở bệnh nhân đái tháo đường (tăng đường huyết)",
              "Thận trọng ở bệnh nhân gout (tăng acid uric)",
              "Tránh dùng với lithium (tăng nguy cơ độc tính lithium)",
              "Dị ứng sulfonamide - không dùng nếu dị ứng"
          ],
          "pharmacokinetics": {
              "half_life": "6-15 giờ",
              "onset": "2 giờ (PO)",
              "duration": "6-12 giờ",
              "protein_binding": "40-70%",
              "clearance": "Thận (không chuyển hóa, thải nguyên dạng)"
          },
          "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
          "black_box_warnings": "",
          "drug_interactions": {
              "major": [
                  {
                      "drug": "Lithium",
                      "mechanism": "HCTZ làm giảm thải trừ lithium qua thận",
                      "effect": "Tăng nồng độ lithium trong máu, tăng nguy cơ độc tính lithium (buồn nôn, run, lú lẫn, co giật)",
                      "management": "TRÁNH DÙNG CHUNG. Nếu bắt buộc: giảm liều lithium 50%, theo dõi nồng độ lithium chặt chẽ, bổ sung kali."
                  },
                  {
                      "drug": "Digoxin",
                      "mechanism": "HCTZ gây hạ kali máu, tăng độc tính digoxin",
                      "effect": "Tăng nguy cơ ngộ độc digoxin (rối loạn nhịp, block AV)",
                      "management": "Theo dõi kali máu chặt chẽ, duy trì kali >4.0 mEq/L. Theo dõi nồng độ digoxin. Cân nhắc dùng kali-sparing diuretic."
                  }
              ],
              "moderate": [
                  {
                      "drug": "NSAIDs (ibuprofen, naproxen, indomethacin)",
                      "mechanism": "NSAIDs giảm tác dụng lợi tiểu và hạ huyết áp của HCTZ, có thể gây suy thận",
                      "effect": "Giảm hiệu quả hạ huyết áp, tăng nguy cơ suy thận cấp",
                      "management": "Thận trọng. Theo dõi huyết áp, chức năng thận. Tránh dùng lâu dài cùng."
                  },
                  {
                      "drug": "Corticosteroids (prednisone, hydrocortisone)",
                      "mechanism": "Corticosteroids gây giữ natri, giảm kali (tương tự HCTZ)",
                      "effect": "Tăng nguy cơ hạ kali máu nặng",
                      "management": "Bổ sung kali. Theo dõi kali máu thường xuyên."
                  },
                  {
                      "drug": "ACE inhibitors, ARBs",
                      "mechanism": "Tác dụng hiệp đồng hạ huyết áp, tăng nguy cơ hạ kali máu (với ACE/ARB) hoặc tăng kali máu (ít gặp)",
                      "effect": "Tăng nguy cơ hạ huyết áp quá mức, tăng kali máu (hiếm)",
                      "management": "Theo dõi huyết áp khi bắt đầu. Theo dõi kali máu định kỳ."
                  },
                  {
                      "drug": "Insulin, các thuốc hạ đường huyết",
                      "mechanism": "HCTZ có thể tăng đường huyết",
                      "effect": "Có thể cần tăng liều insulin hoặc thuốc hạ đường huyết",
                      "management": "Theo dõi đường huyết. Có thể cần điều chỉnh liều thuốc đái tháo đường."
                  }
              ],
              "minor": [
                  {
                      "drug": "Cholestyramine, colestipol",
                      "mechanism": "Giảm hấp thu HCTZ",
                      "effect": "Giảm hiệu quả HCTZ",
                      "management": "Dùng HCTZ ít nhất 2 giờ trước hoặc sau các thuốc này."
                  },
                  {
                      "drug": "Allopurinol",
                      "mechanism": "Tăng nguy cơ phản ứng dị ứng (hiếm)",
                      "effect": "Tăng nguy cơ phản ứng dị ứng",
                      "management": "Thận trọng. Theo dõi dấu hiệu dị ứng."
                  }
              ]
          },
          "contraindications": {
              "tuyệt_đối": [
                  "Dị ứng sulfonamide (phản ứng nghiêm trọng)",
                  "Vô niệu (không có nước tiểu)",
                  "Hạ kali máu nặng không kiểm soát được"
              ],
              "tương_đối": [
                  "Suy thận nặng (eGFR <30 ml/min/1.73m²) - kém hiệu quả",
                  "Suy gan nặng (tăng nguy cơ hạ natri máu)",
                  "Bệnh gout (tăng acid uric)",
                  "Đái tháo đường (tăng đường huyết)",
                  "Lupus ban đỏ hệ thống (có thể làm nặng)",
                  "Đang dùng lithium (tăng nồng độ lithium nguy hiểm)"
              ]
          },
          "pregnancy_lactation": {
              "fda_category": "C",
              "pregnancy_details": "HCTZ có thể gây giảm thể tích máu, giảm tưới máu nhau thai, giảm nước ối. Có thể gây giảm cân nặng thai nhi, thiếu máu thai nhi. Cân nhắc lợi ích/nguy cơ. Thường dùng được trong tăng huyết áp thai kỳ nếu lợi ích vượt trội nguy cơ. Tránh dùng trong 3 tháng đầu nếu có thể.",
              "lactation": {
                  "safety": "Compatible",
                  "details": "HCTZ bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp. Không có báo cáo về tác dụng phụ nghiêm trọng ở trẻ bú mẹ.",
                  "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có dấu hiệu mất nước, rối loạn điện giải."
              }
          },
          "hepatic_adjustment": {
              "mild": "Không đổi",
              "moderate": "Thận trọng (tăng nguy cơ hạ natri máu)",
              "severe": "Thận trọng, có thể tránh dùng (tăng nguy cơ hạ natri máu, giữ natri)",
              "notes": "HCTZ thải qua thận, không chuyển hóa qua gan. Tuy nhiên, suy gan có thể gây giữ natri, tăng nguy cơ hạ natri máu khi dùng HCTZ. Thận trọng ở bệnh nhân suy gan."
          },
          "overdose_management": {
              "symptoms": [
                  "Mất nước nặng",
                  "Hạ kali máu nặng (yếu cơ, rối loạn nhịp tim, có thể gây tử vong)",
                  "Hạ natri máu nặng (lú lẫn, co giật, hôn mê)",
                  "Hạ magie máu",
                  "Hạ huyết áp nặng",
                  "Suy thận cấp (do mất nước)",
                  "Rối loạn nhịp tim (do hạ kali máu)"
              ],
              "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ: bù dịch, điện giải",
              "treatment": [
                  "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                  "Than hoạt tính",
                  "Bù dịch: Truyền normal saline hoặc lactated Ringer's để bù mất nước",
                  "Bù điện giải: Kali chloride (nếu hạ kali máu nặng - cần truyền IV), Magie sulfate (nếu hạ magie máu)",
                  "Điều trị hạ natri máu: Nếu nặng và có triệu chứng thần kinh: Sodium chloride 3% IV (thận trọng, từ từ)",
                  "Theo dõi điện giải thường xuyên (K, Na, Mg, Cl)",
                  "Theo dõi chức năng thận (creatinine, BUN, nước tiểu)",
                  "Theo dõi huyết áp, nhịp tim, ECG",
                  "Theo dõi ít nhất 12-24 giờ"
              ],
              "monitoring": "Điện giải (K, Na, Mg, Cl), chức năng thận (creatinine, BUN, nước tiểu), huyết áp, nhịp tim, ECG, cân bằng dịch, ý thức"
          },
          "reversal_agents": {
              "available": False,
              "agents": []
          },
          "administration_instructions": {
              "oral": {
                  "with_food": "Có thể uống với hoặc không có thức ăn. Uống với thức ăn có thể giảm kích ứng dạ dày.",
                  "timing": "Uống 1 lần/ngày vào buổi sáng (để tránh đi tiểu đêm). Liều thấp (12.5-25mg) đủ cho tăng huyết áp. Uống cùng giờ mỗi ngày. Theo dõi cân bằng dịch, cân nặng."
              },
              "iv": {
                  "reconstitution": "Không có dạng IV",
                  "infusion_rate": "N/A",
                  "compatibility": [],
                  "incompatibility": [],
                  "notes": "Chỉ có dạng uống"
              }
          },
          "references": {
              "primary_sources": [
                  "FDA Drug Label - Hydrochlorothiazide",
                  "UpToDate - Hydrochlorothiazide: Drug information",
                  "ALLHAT Study - JAMA (2002) - Thiazide trong tăng huyết áp",
                  "American Heart Association/American College of Cardiology guidelines - Hypertension"
              ],
              "last_updated": "2025-02-18",
              "evidence_level": "High - Extensive clinical experience and large RCTs (ALLHAT) in hypertension"
          },
          "risk_flags": {
              "high_alert": False,
              "narrow_therapeutic_index": False,
              "icu_critical_care_only": False,
              "bleeding_risk": "Low",
              "organ_toxicity": {"metabolic": "Moderate (electrolyte disturbances, hyperglycemia, hyperuricemia)"}
          },
          "guideline_tags": [
              "ACC/AHA Guidelines - Hypertension",
              "ALLHAT Study - Hypertension",
              "ESC/ESH Guidelines - Hypertension",
              "WHO Essential Medicines List"
          ],
          "last_updated": "2025-02-18",
      },

    "Spironolactone": {
    "group": "Cardiovascular - Aldosterone Antagonist (Potassium-sparing Diuretic)",
    "vietnamese_name": "Spironolactone, Aldactone",
    "administration": ["PO"],
    "indications": [
        "Suy tim (NYHA class II-IV)",
        "Xơ gan với cổ trướng",
        "Hội chứng Conn (tăng aldosterone)",
        "Tăng huyết áp (liều thấp)"
    ],
    "contraindications": [
        "Tăng kali máu",
        "Suy thận nặng (CrCl <30)",
        "Vô niệu",
        "Bệnh Addison"
    ],
    "dosage": {
        "adult_heart_failure": "12.5-25mg x 1 lần/ngày, tăng đến 25-50mg x 1 lần/ngày",
        "adult_ascites": "100-400mg/ngày chia 1-2 lần",
        "adult_htn": "25-100mg/ngày chia 1-2 lần",
        "notes": "Khởi đầu với liều thấp. Theo dõi kali máu"
    },
    "renal_adjustment": {
        "normal": "Không đổi",
        "30_60": "Thận trọng",
        "under_30": "Chống chỉ định"
    },
    "side_effects": [
        "Tăng kali máu",
        "Vú to ở nam (gynecomastia)",
        "Rối loạn kinh nguyệt",
        "Buồn nôn",
        "Chóng mặt"
    ],
    "interactions": [
        "ACE inhibitor/ARB: tăng kali máu đáng kể",
        "Kali bổ sung: tăng kali máu",
        "Digoxin: tăng nồng độ digoxin"
    ],
    "pregnancy": "D",
    "risk_flags": {
        "high_alert": False,
        "narrow_therapeutic_index": False,
        "icu_critical_care_only": False,
        "bleeding_risk": "Low",
        "organ_toxicity": ["hyperkalemia", "endocrine_gynecomastia"]
    },
    "guideline_tags": [
        "ACC/AHA/HFSA HFrEF MRA Class I",
        "ESC HFrEF MRA Class I"
    ],
        "mechanism_of_action": "Potassium-sparing diuretic, aldosterone antagonist. Đối kháng cạnh tranh với aldosterone tại mineralocorticoid receptor trong ống lượn xa và ống góp. Ngăn cản tác dụng của aldosterone (tái hấp thu natri, bài tiết kali). Dẫn đến tăng bài tiết natri và nước, giữ kali (không gây hạ kali). Có tác dụng chống androgen nhẹ (gây tác dụng phụ ở nam giới). Được dùng trong suy tim (giảm tử vong), xơ gan với cổ trướng, hội chứng Conn (cường aldosterone nguyên phát), và tăng huyết áp. Thường dùng kết hợp với loop diuretic hoặc thiazide để tránh hạ kali.",
        "monitoring": [
            "Điện giải (natri, kali) - tăng kali máu là tác dụng phụ chính (nguy hiểm)",
            "Chức năng thận (creatinine, eGFR) - không dùng nếu eGFR < 30",
            "Huyết áp",
            "Cân nặng và dấu hiệu phù",
            "Tác dụng phụ nội tiết (ở nam: vú to, rối loạn cương dương; ở nữ: rối loạn kinh nguyệt)",
            "Dấu hiệu quá liều (tăng kali nặng: yếu cơ, rối loạn nhịp tim)"
        ],
        "precautions": [
            "Tăng kali MÁU là tác dụng phụ chính - KHÔNG dùng nếu kali > 5 mEq/L hoặc eGFR < 30",
            "KHÔNG dùng với kali bổ sung hoặc các thuốc tăng kali khác (ACE inhibitor, ARB, trimethoprim) trừ khi được giám sát chặt chẽ",
            "Theo dõi kali thường xuyên, đặc biệt khi bắt đầu điều trị và tăng liều",
            "Tác dụng phụ nội tiết: vú to ở nam giới (gynecomastia), rối loạn cương dương, rối loạn kinh nguyệt ở nữ",
            "Liều thường: 25-100mg/ngày (PO), liều cao hơn cho hội chứng Conn",
            "Tác dụng chậm (vài ngày đến vài tuần)",
            "Không dùng ở suy thận nặng (eGFR < 30) hoặc tăng kali máu",
            "Thận trọng ở người cao tuổi (tăng nguy cơ tăng kali)",
            "Uống với thức ăn để tăng hấp thu"
        ],
        "pharmacokinetics": {
            "half_life": "10-35 giờ (dài)",
            "onset": "Vài ngày",
            "duration": "2-3 ngày sau khi ngừng",
            "protein_binding": "> 90%",
            "metabolism": "Gan (chuyển đổi thành active metabolites: canrenone)",
            "clearance": "Chủ yếu qua thận và gan"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng. Viên nén: tránh ẩm.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, tăng kali máu có thể gây rối loạn nhịp tim nghiêm trọng, có thể tử vong, đặc biệt ở bệnh nhân suy thận hoặc dùng với các thuốc tăng kali khác. Phải theo dõi kali thường xuyên.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "ACE inhibitors (captopril, enalapril, lisinopril), ARB (losartan, valsartan)",
                    "mechanism": "Cả hai đều làm giảm bài tiết kali qua thận, tác dụng hiệp đồng gây tăng kali máu",
                    "effect": "Tăng kali máu nặng (hyperkalemia), có thể gây rối loạn nhịp tim, ngừng tim",
                    "management": "Thận trọng. Theo dõi kali máu thường xuyên (1-2 tuần sau khi bắt đầu, sau đó mỗi 1-3 tháng). KHÔNG dùng cùng nếu kali > 5 mEq/L hoặc eGFR < 30. Cân nhắc giảm liều hoặc ngừng một trong hai thuốc nếu kali tăng."
                },
                {
                    "drug": "Kali bổ sung (potassium supplements), muối kali (potassium chloride)",
                    "mechanism": "Spironolactone giữ kali, kali bổ sung tăng kali máu",
                    "effect": "Tăng kali máu nặng, nguy hiểm",
                    "management": "CHỐNG CHỈ ĐỊNH dùng cùng. KHÔNG dùng kali bổ sung khi đang dùng spironolactone trừ khi được giám sát chặt chẽ và có chỉ định đặc biệt."
                },
                {
                    "drug": "Trimethoprim, Trimethoprim-sulfamethoxazole",
                    "mechanism": "Trimethoprim ức chế bài tiết kali ở ống lượn xa, tương tự spironolactone",
                    "effect": "Tăng kali máu nặng, đặc biệt ở người cao tuổi, suy thận",
                    "management": "Thận trọng. Theo dõi kali máu thường xuyên. Cân nhắc tránh dùng cùng, đặc biệt ở người cao tuổi hoặc suy thận."
                }
            ],
            "moderate": [
                {
                    "drug": "Digoxin",
                    "mechanism": "Spironolactone ức chế thải trừ digoxin qua thận, tăng nồng độ digoxin trong máu",
                    "effect": "Tăng nồng độ digoxin, tăng nguy cơ ngộ độc digoxin (buồn nôn, rối loạn nhịp tim, block AV)",
                    "management": "Theo dõi nồng độ digoxin trong máu. Có thể cần giảm liều digoxin. Theo dõi dấu hiệu ngộ độc digoxin."
                },
                {
                    "drug": "NSAIDs (ibuprofen, naproxen, diclofenac)",
                    "mechanism": "NSAID làm giảm lưu lượng máu thận, giảm bài tiết natri và kali",
                    "effect": "Tăng nguy cơ tăng kali máu, suy thận cấp",
                    "management": "Thận trọng, đặc biệt ở người cao tuổi hoặc suy thận. Theo dõi kali máu và chức năng thận. Tránh dùng lâu dài cùng."
                },
                {
                    "drug": "Amiloride, Triamterene (các kali-sparing diuretics khác)",
                    "mechanism": "Tác dụng hiệp đồng giữ kali",
                    "effect": "Tăng kali máu nặng",
                    "management": "KHÔNG dùng cùng. Chọn một trong các kali-sparing diuretics."
                },
                {
                    "drug": "Heparin (liều cao)",
                    "mechanism": "Heparin ức chế sản xuất aldosterone, có thể làm giảm bài tiết kali",
                    "effect": "Tăng nguy cơ tăng kali máu",
                    "management": "Theo dõi kali máu khi dùng heparin liều cao cùng spironolactone."
                }
            ],
            "minor": [
                {
                    "drug": "Aspirin liều thấp",
                    "mechanism": "Có thể làm giảm tác dụng lợi tiểu của spironolactone",
                    "effect": "Giảm nhẹ hiệu quả lợi tiểu",
                    "management": "Thường không cần điều chỉnh. Theo dõi đáp ứng điều trị."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Tăng kali máu (hyperkalemia) - kali > 5 mEq/L",
                "Suy thận nặng (CrCl < 30 mL/min, eGFR < 30)",
                "Vô niệu (anuria)",
                "Bệnh Addison (suy thượng thận nguyên phát)",
                "Dùng cùng kali bổ sung hoặc kali-sparing diuretics khác (amiloride, triamterene)"
            ],
            "tương_đối": [
                "Suy thận trung bình (CrCl 30-60) - thận trọng, theo dõi kali thường xuyên",
                "Dùng cùng ACE inhibitor/ARB - thận trọng, theo dõi kali thường xuyên",
                "Người cao tuổi - tăng nguy cơ tăng kali máu",
                "Suy gan - thận trọng (chuyển hóa qua gan)",
                "Tiểu đường - thận trọng (tăng nguy cơ tăng kali máu ở bệnh nhân đái tháo đường type 4)",
                "Thai kỳ - FDA category D, cân nhắc lợi ích/nguy cơ"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Spironolactone có thể gây tác dụng phụ trên thai nhi. Có thể gây tác dụng chống androgen (anti-androgen) trên thai nhi nam, dẫn đến dị tật bộ phận sinh dục. Có thể gây tác dụng phụ trên thai nhi nữ. Cân nhắc lợi ích/nguy cơ. Chỉ dùng khi lợi ích rõ ràng vượt trội nguy cơ. Tránh dùng trong tam cá nguyệt đầu tiên nếu có thể.",
            "lactation": {
                "safety": "Caution",
                "details": "Spironolactone và các metabolites bài tiết vào sữa mẹ. Nồng độ trong sữa mẹ thấp nhưng có thể gây tác dụng phụ trên trẻ bú mẹ. Có thể gây tác dụng chống androgen nhẹ. Có thể gây tăng kali máu ở trẻ bú mẹ (hiếm).",
                "recommendation": "Thận trọng khi dùng khi cho con bú. Cân nhắc lợi ích/nguy cơ. Theo dõi trẻ bú mẹ nếu có dấu hiệu bất thường. Có thể cân nhắc ngừng cho con bú hoặc dùng thuốc thay thế nếu có thể."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi liều",
            "moderate": "Thận trọng, có thể cần giảm liều do chuyển hóa qua gan",
            "severe": "Thận trọng, giảm liều hoặc tránh dùng. Spironolactone chuyển hóa qua gan thành canrenone (active metabolite). Suy gan nặng có thể làm tăng nồng độ spironolactone.",
            "notes": "Spironolactone chuyển hóa qua gan (chuyển đổi thành canrenone). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ spironolactone và tăng tác dụng phụ. Tuy nhiên, spironolactone thường được dùng trong xơ gan với cổ trướng, nên cần cân nhắc lợi ích/nguy cơ."
        },
        "overdose_management": {
            "symptoms": [
                "Tăng kali máu nặng (hyperkalemia) - triệu chứng chính và nguy hiểm nhất",
                "Yếu cơ, liệt cơ",
                "Rối loạn nhịp tim (arrhythmias), đặc biệt là rối loạn nhịp chậm",
                "Block nhĩ thất",
                "Ngừng tim (cardiac arrest)",
                "Rối loạn điện giải (hạ natri máu có thể xảy ra)",
                "Mất nước (dehydration) do lợi tiểu quá mức",
                "Hạ huyết áp",
                "Buồn nôn, nôn",
                "Chóng mặt, mệt mỏi"
            ],
            "antidote": "Không có antidote đặc hiệu. Xử trí tăng kali máu: Calcium gluconate/calcium chloride (bảo vệ tim), Insulin + glucose (chuyển kali vào tế bào), Sodium bicarbonate (nếu có nhiễm toan), Beta-2 agonist (salbutamol) - chuyển kali vào tế bào, Furosemide (tăng bài tiết kali) nếu chức năng thận bình thường, Hemodialysis nếu tăng kali nặng không đáp ứng",
            "treatment": [
                "Ngừng spironolactone ngay lập tức",
                "Đo kali máu ngay (ECG nếu có thể)",
                "Xử trí tăng kali máu:",
                "  - Nếu kali > 6.5 mEq/L hoặc có dấu hiệu tim mạch: Calcium gluconate 1-3g IV (bảo vệ tim, tác dụng nhanh)",
                "  - Insulin regular 10 đơn vị + Dextrose 50% 50ml IV (chuyển kali vào tế bào, tác dụng trong 15-30 phút)",
                "  - Sodium bicarbonate 50-100 mEq IV nếu có nhiễm toan (pH < 7.35)",
                "  - Salbutamol nebulizer 10-20mg (beta-2 agonist, chuyển kali vào tế bào)",
                "  - Furosemide 40-80mg IV nếu chức năng thận bình thường (tăng bài tiết kali)",
                "  - Hemodialysis nếu kali > 6.5 mEq/L và không đáp ứng với điều trị trên",
                "Theo dõi ECG liên tục (tăng kali gây thay đổi ECG: sóng T cao nhọn, kéo dài PR, mất sóng P, giãn QRS, rối loạn nhịp)",
                "Theo dõi kali máu thường xuyên (mỗi 1-2 giờ cho đến khi ổn định)",
                "Điều chỉnh các rối loạn điện giải khác (natri, canxi, magie)",
                "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "Rửa dạ dày và than hoạt tính nếu uống quá liều trong vòng 1-2 giờ (tuy nhiên spironolactone hấp thu chậm)",
                "Theo dõi ít nhất 24-48 giờ do half-life dài (10-35 giờ)"
            ],
            "monitoring": "ECG liên tục, kali máu (mỗi 1-2 giờ), natri máu, chức năng thận (creatinine, BUN), huyết áp, nhịp tim, dấu hiệu rối loạn nhịp tim, dấu hiệu suy hô hấp, dấu hiệu yếu cơ"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Nên uống với thức ăn để tăng hấp thu và giảm kích ứng dạ dày",
                "timing": "Uống 1-2 lần/ngày vào cùng một giờ mỗi ngày. Có thể uống vào buổi sáng hoặc chia 2 lần (sáng và trưa). Tránh uống vào buổi tối muộn để tránh đi tiểu đêm. Tác dụng chậm (vài ngày đến vài tuần), cần kiên nhẫn."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "Không áp dụng",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Spironolactone chỉ có dạng uống (PO)."
            }
        },
        "pediatric_dosing": {
            "neonates": "Không khuyến cáo cho trẻ sơ sinh <1 tháng tuổi (dữ liệu hạn chế). Nếu cần: 1-3mg/kg/ngày PO chia 1-2 lần. Theo dõi kali máu chặt chẽ.",
            "infants": "1 tháng - 2 tuổi: 1-3mg/kg/ngày PO chia 1-2 lần. Theo dõi kali máu chặt chẽ. Thận trọng ở suy thận.",
            "children": "2-12 tuổi: 1-3mg/kg/ngày PO chia 1-2 lần (tối đa 100mg/ngày). Suy tim: 1-2mg/kg/ngày. Theo dõi kali máu chặt chẽ. Thận trọng ở suy thận.",
            "adolescents": "≥12 tuổi: Liều người lớn. Suy tim: 12.5-25mg x 1 lần/ngày, tăng đến 25-50mg x 1 lần/ngày. Cổ trướng: 100-400mg/ngày chia 1-2 lần. Theo dõi kali máu chặt chẽ.",
            "notes": "Theo dõi kali máu chặt chẽ (tăng kali máu là tác dụng phụ nghiêm trọng). Thận trọng ở suy thận (CrCl <30: chống chỉ định). Không dùng với ACE inhibitor/ARB ở trẻ em nếu có suy thận. Theo dõi chức năng thận định kỳ."
        },
        "geriatric_dosing": {
            "considerations": "Người cao tuổi có nguy cơ tăng kali máu cao hơn do: suy thận phổ biến hơn, dùng nhiều thuốc (ACE inhibitor, ARB, kali bổ sung), giảm chức năng thận. Tăng nguy cơ vú to ở nam (gynecomastia).",
            "dose_adjustment": "Khởi đầu với liều thấp hơn (12.5mg x 1 lần/ngày). Tăng dần chậm hơn. Điều chỉnh liều theo chức năng thận: CrCl 30-60 → thận trọng, theo dõi sát, CrCl <30 → chống chỉ định. Thận trọng khi dùng với ACE inhibitor/ARB.",
            "monitoring": "Theo dõi kali máu chặt chẽ (mỗi 1-2 tuần khi bắt đầu, sau đó mỗi 1-3 tháng). Theo dõi chức năng thận (creatinine, CrCl) định kỳ. Theo dõi dấu hiệu tăng kali máu (yếu cơ, rối loạn nhịp tim). Theo dõi dấu hiệu vú to ở nam (gynecomastia). Theo dõi triệu chứng suy tim (khó thở, phù)."
        },
        "brand_names": {
            "vietnam": ["Spironolactone", "Aldactone", "Spironolactone Stada", "Spiro"],
            "common": ["Aldactone", "Spironolactone"]
        },
        "cost_estimate": {
            "unit": "VND",
            "range": "3,000 - 15,000 VND/viên (tùy hàm lượng và thương hiệu)",
            "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Spironolactone generic thường rẻ hơn (3,000-8,000 VND/viên 25mg). Aldactone (brand) thường đắt hơn (8,000-15,000 VND/viên 25mg)."
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Aldactone (spironolactone)",
                "UpToDate - Spironolactone: Drug information",
                "RALES Study - New England Journal of Medicine (1999) - Spironolactone trong suy tim",
                "EPHESUS Study - New England Journal of Medicine (2003) - Eplerenone sau nhồi máu cơ tim",
                "American Heart Association/American College of Cardiology guidelines - Heart failure management",
                "Goodman & Gilman's Pharmacological Basis of Therapeutics - Diuretics"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - Multiple large RCTs (RALES, EPHESUS) showing mortality benefit in heart failure"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"metabolic": "High (hyperkalemia)", "endocrine": "Moderate (gynecomastia, menstrual irregularities)"}
        },
        "guideline_tags": [
            "ACC/AHA/HFSA Guidelines - Heart Failure with Reduced Ejection Fraction",
            "ESC Guidelines - Heart Failure",
            "RALES Study - Heart Failure",
            "KDIGO Guidelines - Chronic Kidney Disease",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18",
    },

    "Bumetanide": {
        "group": "Cardiovascular - Loop Diuretic",
        "vietnamese_name": "Bumetanide, Burinex",
        "administration": ["PO", "IV", "IM"],
        "indications": [
            "Phù (suy tim, xơ gan, suy thận)",
            "Tăng huyết áp",
            "Suy tim cấp",
            "Tăng kali máu"
        ],
        "contraindications": [
            "Vô niệu",
            "Mất nước nặng",
            "Hạ kali máu nặng",
            "Dị ứng sulfonamide"
        ],
        "dosage": {
            "adult_po": "0.5-2mg x 1-2 lần/ngày",
            "adult_iv": "0.5-1mg IV (có thể lặp lại mỗi 2-3 giờ)",
            "adult_iv_continuous": "0.1-0.2mg/giờ truyền liên tục",
            "heart_failure_acute": "0.5-1mg IV, có thể lặp lại",
            "notes": "1mg bumetanide ≈ 40mg furosemide. Theo dõi cân bằng dịch, điện giải"
        },
        "side_effects": [
            "Hạ kali máu",
            "Hạ natri máu",
            "Mất nước",
            "Tăng acid uric",
            "Điếc tạm thời (IV liều cao)",
            "Tăng đường huyết"
        ],
        "interactions": [
            "Digoxin: tăng nguy cơ ngộ độc digoxin (hạ kali)",
            "Aminoglycosides: tăng độc tính thính giác",
            "NSAID: giảm hiệu quả",
            "Lithium: tăng nồng độ lithium"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Loop diuretic. Ức chế đồng vận chuyển Na-K-2Cl ở quai Henle, tăng thải natri, kali, clo, và nước. Mạnh hơn furosemide (1mg bumetanide ≈ 40mg furosemide).",
        "monitoring": [
            "Điện giải (K, Na, Cl) trước điều trị và định kỳ",
            "Cân bằng dịch vào-ra, cân nặng",
            "Creatinine, BUN",
            "Acid uric nếu dùng lâu dài",
            "Thính giác nếu IV liều cao hoặc suy thận"
        ],
        "precautions": [
            "Theo dõi sát điện giải, đặc biệt kali",
            "Bù kali nếu cần",
            "Tránh dùng quá liều (gây mất nước, suy thận)",
            "Thận trọng với bệnh nhân suy thận (có thể cần liều cao hơn)",
            "Tránh dùng IV liều cao ở bệnh nhân suy thận (nguy cơ điếc)"
        ],
        "pharmacokinetics": {
            "half_life": "1-1.5 giờ (PO), 1 giờ (IV)",
            "onset": "30-60 phút (PO), 2-3 phút (IV)",
            "duration": "4-6 giờ",
            "protein_binding": "94-96%",
            "clearance": "Thận (50%) và gan"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng",
        "black_box_warnings": "Có thể gây mất nước và rối loạn điện giải nghiêm trọng. Điếc có thể xảy ra với liều IV cao hoặc dùng nhanh. Hạ kali máu có thể làm tăng nguy cơ ngộ độc digoxin và rối loạn nhịp tim",
        "references": {
            "primary_sources": [
                "FDA Drug Label - Bumetanide",
                "UpToDate - Bumetanide: Drug information"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - Extensive clinical experience"
        }
    },

    "Torsemide": {
        "group": "Cardiovascular - Loop Diuretic",
        "vietnamese_name": "Torsemide, Demadex",
        "administration": ["PO", "IV"],
        "indications": [
            "Phù (suy tim, xơ gan, suy thận)",
            "Tăng huyết áp",
            "Suy tim cấp",
            "Tăng kali máu"
        ],
        "contraindications": [
            "Vô niệu",
            "Mất nước nặng",
            "Hạ kali máu nặng",
            "Dị ứng sulfonamide"
        ],
        "dosage": {
            "adult_po": "5-20mg x 1 lần/ngày",
            "adult_iv": "10-20mg IV (có thể lặp lại)",
            "adult_iv_continuous": "0.2-0.4mg/giờ truyền liên tục",
            "heart_failure_acute": "10-20mg IV, có thể lặp lại",
            "notes": "10mg torsemide ≈ 40mg furosemide. Thời gian bán hủy dài hơn furosemide. Theo dõi cân bằng dịch, điện giải"
        },
        "side_effects": [
            "Hạ kali máu",
            "Hạ natri máu",
            "Mất nước",
            "Tăng acid uric",
            "Điếc tạm thời (IV liều cao)",
            "Tăng đường huyết"
        ],
        "interactions": [
            "Digoxin: tăng nguy cơ ngộ độc digoxin (hạ kali)",
            "Aminoglycosides: tăng độc tính thính giác",
            "NSAID: giảm hiệu quả",
            "Lithium: tăng nồng độ lithium"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Loop diuretic. Ức chế đồng vận chuyển Na-K-2Cl ở quai Henle, tăng thải natri, kali, clo, và nước. 10mg torsemide ≈ 40mg furosemide. Thời gian bán hủy dài hơn furosemide (3-4 giờ vs 2 giờ), có thể dùng 1 lần/ngày.",
        "monitoring": [
            "Điện giải (K, Na, Cl) trước điều trị và định kỳ",
            "Cân bằng dịch vào-ra, cân nặng",
            "Creatinine, BUN",
            "Acid uric nếu dùng lâu dài",
            "Thính giác nếu IV liều cao hoặc suy thận"
        ],
        "precautions": [
            "Theo dõi sát điện giải, đặc biệt kali",
            "Bù kali nếu cần",
            "Tránh dùng quá liều (gây mất nước, suy thận)",
            "Thận trọng với bệnh nhân suy thận (có thể cần liều cao hơn)",
            "Tránh dùng IV liều cao ở bệnh nhân suy thận (nguy cơ điếc)",
            "Thời gian bán hủy dài hơn furosemide - có thể dùng 1 lần/ngày"
        ],
        "pharmacokinetics": {
            "half_life": "3-4 giờ (PO), 3 giờ (IV)",
            "onset": "60 phút (PO), 10 phút (IV)",
            "duration": "6-8 giờ",
            "protein_binding": "97-99%",
            "clearance": "Thận (80%) và gan (20%)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng",
        "black_box_warnings": "Có thể gây mất nước và rối loạn điện giải nghiêm trọng. Điếc có thể xảy ra với liều IV cao hoặc dùng nhanh. Hạ kali máu có thể làm tăng nguy cơ ngộ độc digoxin và rối loạn nhịp tim",
        "references": {
            "primary_sources": [
                "FDA Drug Label - Torsemide",
                "UpToDate - Torsemide: Drug information"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - Extensive clinical experience"
        }
    },

    "Indapamide": {
        "group": "Cardiovascular - Thiazide-like Diuretic",
        "vietnamese_name": "Indapamide, Natrilix",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp",
            "Phù (suy tim nhẹ)"
        ],
        "contraindications": [
            "Dị ứng sulfonamide",
            "Vô niệu",
            "Hạ kali máu nặng",
            "Suy gan nặng"
        ],
        "dosage": {
            "adult_htn": "1.25-2.5mg x 1 lần/ngày",
            "adult_edema": "2.5-5mg x 1 lần/ngày",
            "notes": "Thiazide-like diuretic, tác dụng dài, uống 1 lần/ngày. Ít gây hạ kali máu hơn thiazide truyền thống"
        },
        "side_effects": [
            "Hạ kali máu (ít hơn thiazide)",
            "Hạ natri máu",
            "Tăng đường huyết",
            "Tăng acid uric",
            "Chóng mặt",
            "Mệt mỏi"
        ],
        "interactions": [
            "Digoxin: tăng nguy cơ ngộ độc digoxin (hạ kali)",
            "Lithium: tăng nồng độ lithium",
            "NSAID: giảm hiệu quả"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Thiazide-like diuretic. Ức chế Na+/Cl- cotransporter ở đoạn xa của ống thận, tăng bài tiết Na+, Cl-, và nước. Có tác dụng giãn mạch trực tiếp (khác với thiazide truyền thống). Ít gây hạ kali máu hơn hydrochlorothiazide. Tác dụng dài, cho phép dùng 1 lần/ngày.",
        "monitoring": [
            "Kali máu (mỗi 1-3 tháng) - ít gây hạ kali hơn thiazide",
            "Natri máu - có thể gây hạ natri máu",
            "Creatinine, BUN",
            "Đường huyết - có thể tăng đường huyết",
            "Acid uric - có thể tăng acid uric"
        ],
        "precautions": [
            "Ít gây hạ kali máu hơn hydrochlorothiazide nhưng vẫn cần theo dõi",
            "Thận trọng ở người già (tăng nguy cơ hạ natri máu)",
            "Thận trọng ở bệnh nhân đái tháo đường (tăng đường huyết)",
            "Thận trọng ở bệnh nhân gout (tăng acid uric)",
            "Tránh dùng với lithium (tăng nguy cơ độc tính lithium)",
            "Dị ứng sulfonamide - không dùng nếu dị ứng"
        ],
        "pharmacokinetics": {
            "half_life": "14-18 giờ (dài)",
            "onset": "1-2 giờ (PO)",
            "duration": "24 giờ (cho phép dùng 1 lần/ngày)",
            "protein_binding": "71-79%",
            "clearance": "Thận (70%) và gan (30%)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Lithium",
                    "mechanism": "Indapamide làm giảm thải trừ lithium qua thận",
                    "effect": "Tăng nồng độ lithium, tăng nguy cơ độc tính",
                    "management": "TRÁNH DÙNG CHUNG. Nếu bắt buộc: giảm liều lithium 50%, theo dõi nồng độ lithium chặt chẽ."
                },
                {
                    "drug": "Digoxin",
                    "mechanism": "Indapamide gây hạ kali máu, tăng độc tính digoxin",
                    "effect": "Tăng nguy cơ ngộ độc digoxin",
                    "management": "Theo dõi kali máu chặt chẽ. Theo dõi nồng độ digoxin."
                }
            ],
            "moderate": [
                {
                    "drug": "NSAIDs",
                    "mechanism": "NSAIDs giảm tác dụng lợi tiểu và hạ huyết áp",
                    "effect": "Giảm hiệu quả hạ huyết áp",
                    "management": "Thận trọng. Theo dõi huyết áp. Tránh dùng lâu dài cùng."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng sulfonamide",
                "Vô niệu",
                "Hạ kali máu nặng không kiểm soát được",
                "Suy gan nặng"
            ],
            "tương_đối": [
                "Suy thận nặng (eGFR <30) - kém hiệu quả",
                "Bệnh gout - tăng acid uric",
                "Đái tháo đường - tăng đường huyết",
                "Đang dùng lithium - tăng nồng độ lithium nguy hiểm"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Có thể dùng khi cần thiết. Ít dữ liệu hơn hydrochlorothiazide. Cân nhắc lợi ích/nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Indapamide bài tiết vào sữa mẹ ở nồng độ thấp. An toàn cho trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng (thải một phần qua gan)",
            "severe": "Chống chỉ định (thải một phần qua gan)",
            "notes": "Indapamide thải qua cả thận (70%) và gan (30%). Suy gan nặng là chống chỉ định."
        },
        "overdose_management": {
            "symptoms": [
                "Mất nước nặng",
                "Hạ kali máu nặng",
                "Hạ natri máu nặng",
                "Hạ huyết áp nặng",
                "Suy thận cấp"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ: bù dịch, điện giải",
            "treatment": [
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Bù dịch: Truyền normal saline",
                "Bù điện giải: Kali chloride nếu hạ kali máu",
                "Theo dõi điện giải, chức năng thận",
                "Theo dõi ít nhất 12-24 giờ"
            ],
            "monitoring": "Điện giải (K, Na), chức năng thận, huyết áp, nhịp tim"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn.",
                "timing": "Uống 1 lần/ngày vào buổi sáng. Uống cùng giờ mỗi ngày."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống"
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Indapamide",
                "UpToDate - Indapamide: Drug information"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - Extensive clinical experience"
        }
    },

    "Eplerenone": {
        "group": "Cardiovascular - Aldosterone Antagonist (Potassium-sparing Diuretic)",
        "vietnamese_name": "Eplerenone, Inspra",
        "administration": ["PO"],
        "indications": [
            "Suy tim (NYHA class II-IV) sau nhồi máu cơ tim",
            "Suy tim với giảm phân suất tống máu (HFrEF)",
            "Tăng huyết áp (liều thấp)"
        ],
        "contraindications": [
            "Tăng kali máu (>5.5 mEq/L)",
            "Suy thận nặng (CrCl <30)",
            "Vô niệu",
            "Dùng với kali-sparing diuretics hoặc kali bổ sung",
            "Dùng với CYP3A4 inhibitors mạnh"
        ],
        "dosage": {
            "adult_heart_failure_post_mi": "25mg x 1 lần/ngày, tăng đến 50mg x 1 lần/ngày sau 4 tuần",
            "adult_heart_failure": "25mg x 1 lần/ngày, tăng đến 50mg x 1 lần/ngày",
            "adult_htn": "50mg x 1-2 lần/ngày",
            "notes": "Khởi đầu với liều thấp. Theo dõi kali máu. Có bằng chứng giảm tỷ lệ tử vong sau nhồi máu cơ tim (EPHESUS study)"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, theo dõi kali sát",
            "under_30": "Chống chỉ định"
        },
        "side_effects": [
            "Tăng kali máu (tác dụng phụ chính)",
            "Chóng mặt",
            "Mệt mỏi",
            "Ho",
            "Ít tác dụng phụ nội tiết hơn spironolactone (không gây vú to)"
        ],
        "interactions": [
            "ACE inhibitor/ARB: tăng kali máu đáng kể",
            "Kali bổ sung: tăng kali máu",
            "CYP3A4 inhibitors: tăng nồng độ eplerenone",
            "NSAID: tăng nguy cơ tăng kali máu"
        ],
        "pregnancy": "B",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": ["hyperkalemia"]
        },
        "guideline_tags": [
            "ACC/AHA/HFSA HFrEF MRA Class I",
            "ESC HFrEF MRA Class I"
        ],
        "mechanism_of_action": "Potassium-sparing diuretic, selective aldosterone antagonist. Đối kháng với aldosterone tại mineralocorticoid receptor trong ống lượn xa và ống góp. Khác với spironolactone: eplerenone chọn lọc hơn, ít tác dụng trên androgen và progesterone receptors, do đó ít gây tác dụng phụ nội tiết (không gây vú to ở nam, rối loạn kinh nguyệt ở nữ). Có bằng chứng mạnh làm giảm tỷ lệ tử vong và nhập viện trong suy tim sau nhồi máu cơ tim (EPHESUS study) và suy tim mạn tính (EMPHASIS-HF study).",
        "monitoring": [
            "Điện giải (natri, kali) - tăng kali máu là tác dụng phụ chính (nguy hiểm)",
            "Chức năng thận (creatinine, eGFR) - không dùng nếu eGFR < 30",
            "Huyết áp",
            "Cân nặng và dấu hiệu phù",
            "Dấu hiệu quá liều (tăng kali nặng: yếu cơ, rối loạn nhịp tim)"
        ],
        "precautions": [
            "Tăng kali MÁU là tác dụng phụ chính - KHÔNG dùng nếu kali > 5.5 mEq/L hoặc eGFR < 30",
            "KHÔNG dùng với kali bổ sung hoặc các thuốc tăng kali khác (ACE inhibitor, ARB, trimethoprim) trừ khi được giám sát chặt chẽ",
            "Theo dõi kali thường xuyên, đặc biệt khi bắt đầu điều trị và tăng liều (1-2 tuần sau khi bắt đầu, sau đó mỗi 1-3 tháng)",
            "Ít tác dụng phụ nội tiết hơn spironolactone (không gây vú to, rối loạn kinh nguyệt)",
            "Liều thường: 25-50mg/ngày (PO)",
            "Tác dụng chậm (vài ngày đến vài tuần)",
            "Không dùng ở suy thận nặng (eGFR < 30) hoặc tăng kali máu",
            "Thận trọng ở người cao tuổi (tăng nguy cơ tăng kali)",
            "Tránh dùng với CYP3A4 inhibitors mạnh (ketoconazole, itraconazole, clarithromycin)"
        ],
        "pharmacokinetics": {
            "half_life": "3-6 giờ (ngắn hơn spironolactone)",
            "onset": "Vài ngày",
            "duration": "12-24 giờ",
            "protein_binding": "50%",
            "metabolism": "Gan (CYP3A4) - chuyển hóa mạnh",
            "clearance": "Chủ yếu qua gan (metabolism), một phần qua thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, tăng kali máu có thể gây rối loạn nhịp tim nghiêm trọng, có thể tử vong, đặc biệt ở bệnh nhân suy thận hoặc dùng với các thuốc tăng kali khác. Phải theo dõi kali thường xuyên.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "ACE inhibitors (captopril, enalapril, lisinopril), ARB (losartan, valsartan)",
                    "mechanism": "Cả hai đều làm giảm bài tiết kali qua thận, tác dụng hiệp đồng gây tăng kali máu",
                    "effect": "Tăng kali máu nặng (hyperkalemia), có thể gây rối loạn nhịp tim, ngừng tim",
                    "management": "Thận trọng. Theo dõi kali máu thường xuyên (1-2 tuần sau khi bắt đầu, sau đó mỗi 1-3 tháng). KHÔNG dùng cùng nếu kali > 5.5 mEq/L hoặc eGFR < 30. Cân nhắc giảm liều hoặc ngừng một trong hai thuốc nếu kali tăng."
                },
                {
                    "drug": "Kali bổ sung (potassium supplements), muối kali (potassium chloride)",
                    "mechanism": "Eplerenone giữ kali, kali bổ sung tăng kali máu",
                    "effect": "Tăng kali máu nặng, nguy hiểm",
                    "management": "CHỐNG CHỈ ĐỊNH dùng cùng. KHÔNG dùng kali bổ sung khi đang dùng eplerenone trừ khi được giám sát chặt chẽ và có chỉ định đặc biệt."
                },
                {
                    "drug": "CYP3A4 inhibitors mạnh (ketoconazole, itraconazole, clarithromycin, ritonavir)",
                    "mechanism": "Ức chế chuyển hóa eplerenone qua CYP3A4",
                    "effect": "Tăng nồng độ eplerenone đáng kể, tăng tác dụng phụ (tăng kali máu)",
                    "management": "CHỐNG CHỈ ĐỊNH dùng cùng với CYP3A4 inhibitors mạnh."
                }
            ],
            "moderate": [
                {
                    "drug": "Trimethoprim, Trimethoprim-sulfamethoxazole",
                    "mechanism": "Trimethoprim ức chế bài tiết kali ở ống lượn xa",
                    "effect": "Tăng kali máu nặng, đặc biệt ở người cao tuổi, suy thận",
                    "management": "Thận trọng. Theo dõi kali máu thường xuyên. Cân nhắc tránh dùng cùng."
                },
                {
                    "drug": "NSAIDs (ibuprofen, naproxen, diclofenac)",
                    "mechanism": "NSAID làm giảm lưu lượng máu thận, giảm bài tiết kali",
                    "effect": "Tăng nguy cơ tăng kali máu, suy thận cấp",
                    "management": "Thận trọng, đặc biệt ở người cao tuổi hoặc suy thận. Theo dõi kali máu và chức năng thận."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Tăng kali máu (hyperkalemia) - kali > 5.5 mEq/L",
                "Suy thận nặng (CrCl < 30 mL/min, eGFR < 30)",
                "Vô niệu (anuria)",
                "Dùng cùng kali bổ sung hoặc kali-sparing diuretics khác (spironolactone, amiloride, triamterene)",
                "Dùng với CYP3A4 inhibitors mạnh (ketoconazole, itraconazole, clarithromycin, ritonavir)"
            ],
            "tương_đối": [
                "Suy thận trung bình (CrCl 30-60) - thận trọng, theo dõi kali thường xuyên",
                "Dùng cùng ACE inhibitor/ARB - thận trọng, theo dõi kali thường xuyên",
                "Người cao tuổi - tăng nguy cơ tăng kali máu",
                "Suy gan - thận trọng (chuyển hóa qua gan CYP3A4)"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Eplerenone phân loại B - an toàn hơn spironolactone (category D). Có thể dùng khi cần thiết. Ít tác dụng phụ trên thai nhi hơn spironolactone. Cân nhắc lợi ích/nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Eplerenone bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp. An toàn cho trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có dấu hiệu bất thường."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng (chuyển hóa qua CYP3A4)",
            "severe": "Thận trọng, có thể cần giảm liều (chuyển hóa qua CYP3A4)",
            "notes": "Eplerenone chuyển hóa qua gan (CYP3A4). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ eplerenone. Thận trọng ở bệnh nhân suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Tăng kali máu nặng (hyperkalemia) - triệu chứng chính và nguy hiểm nhất",
                "Yếu cơ, liệt cơ",
                "Rối loạn nhịp tim (arrhythmias), đặc biệt là rối loạn nhịp chậm",
                "Block nhĩ thất",
                "Ngừng tim (cardiac arrest)",
                "Hạ huyết áp",
                "Buồn nôn, nôn",
                "Chóng mặt, mệt mỏi"
            ],
            "antidote": "Không có antidote đặc hiệu. Xử trí tăng kali máu: Calcium gluconate/calcium chloride (bảo vệ tim), Insulin + glucose (chuyển kali vào tế bào), Sodium bicarbonate (nếu có nhiễm toan), Beta-2 agonist (salbutamol), Furosemide (tăng bài tiết kali) nếu chức năng thận bình thường, Hemodialysis nếu tăng kali nặng không đáp ứng",
            "treatment": [
                "Ngừng eplerenone ngay lập tức",
                "Đo kali máu ngay (ECG nếu có thể)",
                "Xử trí tăng kali máu:",
                "  - Nếu kali > 6.5 mEq/L hoặc có dấu hiệu tim mạch: Calcium gluconate 1-3g IV (bảo vệ tim, tác dụng nhanh)",
                "  - Insulin regular 10 đơn vị + Dextrose 50% 50ml IV (chuyển kali vào tế bào, tác dụng trong 15-30 phút)",
                "  - Sodium bicarbonate 50-100 mEq IV nếu có nhiễm toan (pH < 7.35)",
                "  - Salbutamol nebulizer 10-20mg (beta-2 agonist, chuyển kali vào tế bào)",
                "  - Furosemide 40-80mg IV nếu chức năng thận bình thường (tăng bài tiết kali)",
                "  - Hemodialysis nếu kali > 6.5 mEq/L và không đáp ứng với điều trị trên",
                "Theo dõi ECG liên tục (tăng kali gây thay đổi ECG: sóng T cao nhọn, kéo dài PR, mất sóng P, giãn QRS, rối loạn nhịp)",
                "Theo dõi kali máu thường xuyên (mỗi 1-2 giờ cho đến khi ổn định)",
                "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "Rửa dạ dày và than hoạt tính nếu uống quá liều trong vòng 1-2 giờ",
                "Theo dõi ít nhất 12-24 giờ do half-life 3-6 giờ"
            ],
            "monitoring": "ECG liên tục, kali máu (mỗi 1-2 giờ), natri máu, chức năng thận (creatinine, BUN), huyết áp, nhịp tim, dấu hiệu rối loạn nhịp tim"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Không ảnh hưởng đáng kể đến hấp thu.",
                "timing": "Uống 1 lần/ngày vào cùng một giờ mỗi ngày. Khởi đầu với liều thấp (25mg/ngày), tăng dần sau 4 tuần nếu cần. Tác dụng chậm (vài ngày đến vài tuần), cần kiên nhẫn."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Eplerenone chỉ có dạng uống (PO)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Inspra (eplerenone)",
                "UpToDate - Eplerenone: Drug information",
                "EPHESUS Study - New England Journal of Medicine (2003) - Eplerenone sau nhồi máu cơ tim",
                "EMPHASIS-HF Study - New England Journal of Medicine (2011) - Eplerenone trong suy tim",
                "American Heart Association/American College of Cardiology guidelines - Heart failure management"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - Multiple large RCTs (EPHESUS, EMPHASIS-HF) showing mortality benefit in heart failure"
        }
    },
    "Chlorthalidone": {
        "group": "Cardiovascular - Thiazide-like Diuretic",
        "vietnamese_name": "Chlorthalidone, Hygroton",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp",
            "Phù (suy tim nhẹ)"
        ],
        "contraindications": [
            "Dị ứng sulfonamide",
            "Vô niệu",
            "Hạ kali máu nặng",
            "Suy gan nặng"
        ],
        "dosage": {
            "adult_htn": "12.5-25mg x 1 lần/ngày",
            "adult_edema": "25-100mg x 1 lần/ngày",
            "adult_max": "100mg/ngày",
            "notes": "Thiazide-like diuretic, tác dụng rất dài (48-72 giờ), uống 1 lần/ngày. Ưu tiên hơn HCTZ theo ESC/ESH 2023. Hiệu quả hạ huyết áp tốt hơn HCTZ."
        },
        "side_effects": [
            "Hạ kali máu",
            "Hạ natri máu",
            "Tăng đường huyết",
            "Tăng acid uric",
            "Tăng cholesterol, triglyceride",
            "Chóng mặt",
            "Mệt mỏi",
            "Rối loạn cương dương"
        ],
        "interactions": [
            "Digoxin: tăng nguy cơ ngộ độc digoxin (hạ kali)",
            "Lithium: tăng nồng độ lithium",
            "NSAID: giảm hiệu quả",
            "Corticosteroid: tăng hạ kali máu"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Thiazide-like diuretic. Ức chế Na+/Cl- cotransporter ở đoạn xa của ống thận, tăng bài tiết Na+, Cl-, và nước. Có tác dụng giãn mạch trực tiếp. Tác dụng rất dài (48-72 giờ) do half-life dài, cho phép dùng 1 lần/ngày. Hiệu quả hạ huyết áp tốt hơn hydrochlorothiazide (HCTZ) ở liều tương đương. Theo ESC/ESH 2023 và ACC/AHA 2024, chlorthalidone được ưu tiên hơn HCTZ cho điều trị tăng huyết áp do hiệu quả tốt hơn và bằng chứng lâm sàng mạnh hơn.",
        "monitoring": [
            "Kali máu (mỗi 1-3 tháng) - hạ kali máu phổ biến",
            "Natri máu - có thể gây hạ natri máu, đặc biệt ở người già",
            "Creatinine, BUN - có thể tăng nhẹ",
            "Đường huyết - có thể tăng đường huyết",
            "Acid uric - có thể tăng acid uric, gây gout",
            "Lipid máu - có thể tăng cholesterol, triglyceride nhẹ"
        ],
        "precautions": [
            "Ưu tiên hơn hydrochlorothiazide (HCTZ) theo ESC/ESH 2023 và ACC/AHA 2024 - hiệu quả hạ huyết áp tốt hơn",
            "Tác dụng rất dài (48-72 giờ) - dùng 1 lần/ngày, thuận tiện",
            "Hạ kali máu phổ biến - theo dõi kali máu thường xuyên, bổ sung kali nếu cần",
            "Thận trọng ở người già - tăng nguy cơ hạ natri máu, té ngã",
            "Thận trọng ở bệnh nhân đái tháo đường (tăng đường huyết)",
            "Thận trọng ở bệnh nhân gout (tăng acid uric)",
            "Tránh dùng với lithium (tăng nguy cơ độc tính lithium)",
            "Theo dõi chức năng thận - có thể tăng creatinine nhẹ",
            "Bắt đầu với liều thấp (12.5mg/ngày) để giảm tác dụng phụ"
        ],
        "pharmacokinetics": {
            "half_life": "40-60 giờ (rất dài)",
            "onset": "2-3 giờ",
            "duration": "48-72 giờ (rất dài)",
            "protein_binding": "75%",
            "clearance": "Thận (thải trừ chủ yếu nguyên dạng), gan (chuyển hóa một phần)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Có thể gây hạ kali máu nghiêm trọng, hạ natri máu, và rối loạn điện giải. Hạ kali máu có thể làm tăng nguy cơ ngộ độc digoxin và rối loạn nhịp tim. Hạ natri máu có thể gây lú lẫn, co giật, hôn mê, đặc biệt ở người già.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Digoxin",
                    "mechanism": "Chlorthalidone gây hạ kali máu, tăng nguy cơ ngộ độc digoxin",
                    "effect": "Tăng nguy cơ ngộ độc digoxin (nhịp tim chậm, block AV, rối loạn nhịp tim)",
                    "management": "Theo dõi kali máu thường xuyên. Bù kali nếu cần. Theo dõi nồng độ digoxin. Theo dõi ECG."
                },
                {
                    "drug": "Lithium",
                    "mechanism": "Chlorthalidone giảm thải trừ lithium qua thận (do giảm thể tích máu), tăng nồng độ lithium",
                    "effect": "Tăng nồng độ lithium, tăng nguy cơ độc tính lithium",
                    "management": "TRÁNH dùng chung. Nếu bắt buộc: theo dõi nồng độ lithium chặt chẽ. Có thể cần giảm liều lithium."
                }
            ],
            "moderate": [
                {
                    "drug": "NSAIDs (ibuprofen, naproxen, diclofenac)",
                    "mechanism": "NSAID giảm tác dụng lợi tiểu của chlorthalidone (do giảm prostaglandin, giảm lưu lượng máu thận)",
                    "effect": "Giảm hiệu quả lợi tiểu, giảm hạ huyết áp",
                    "management": "Thận trọng. Theo dõi đáp ứng hạ huyết áp. Có thể cần tăng liều chlorthalidone."
                },
                {
                    "drug": "Corticosteroid",
                    "mechanism": "Corticosteroid gây hạ kali máu, tác dụng hiệp đồng với chlorthalidone",
                    "effect": "Tăng nguy cơ hạ kali máu nghiêm trọng",
                    "management": "Theo dõi kali máu thường xuyên. Bù kali nếu cần."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng chlorthalidone hoặc sulfonamide",
                "Vô niệu",
                "Hạ kali máu nặng không kiểm soát",
                "Suy gan nặng"
            ],
            "tương_đối": [
                "Suy thận (CrCl <30) - giảm hiệu quả, tăng nguy cơ tác dụng phụ",
                "Hạ kali máu - có thể làm nặng",
                "Hạ natri máu - có thể làm nặng",
                "Đái tháo đường - có thể tăng đường huyết",
                "Gout - có thể tăng acid uric, gây cơn gout",
                "Người cao tuổi - tăng nguy cơ hạ natri máu, té ngã",
                "Dùng với digoxin - tăng nguy cơ ngộ độc digoxin",
                "Dùng với lithium - tăng nguy cơ độc tính lithium"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "An toàn trong thai kỳ. Không có bằng chứng về dị tật bẩm sinh. Có thể dùng nếu cần thiết. Tuy nhiên, có thể gây giảm thể tích máu và giảm tưới máu nhau thai.",
            "lactation": {
                "safety": "Compatible",
                "details": "Chlorthalidone bài tiết vào sữa mẹ ở nồng độ thấp. Có thể gây giảm tiết sữa nhẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi lượng sữa."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, có thể giảm liều nhẹ",
            "severe": "Tránh dùng",
            "notes": "Chlorthalidone chuyển hóa một phần ở gan. Suy gan nặng có thể làm giảm chuyển hóa, tăng nguy cơ tích lũy."
        },
        "overdose_management": {
            "symptoms": [
                "Hạ kali máu nghiêm trọng (yếu cơ, rối loạn nhịp tim)",
                "Hạ natri máu nghiêm trọng (lú lẫn, co giật, hôn mê)",
                "Mất nước",
                "Hạ huyết áp",
                "Suy thận cấp"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều chỉnh điện giải.",
            "treatment": [
                "Ngừng chlorthalidone ngay lập tức",
                "Đo điện giải ngay (K+, Na+, Cl-)",
                "Bù kali nếu hạ kali máu (K+ <3.5 mEq/L)",
                "Điều chỉnh natri máu nếu hạ natri máu (Na+ <135 mEq/L) - bù dịch nước muối sinh lý hoặc nước muối 3% nếu nặng",
                "Truyền dịch nếu mất nước hoặc hạ huyết áp",
                "Theo dõi chức năng thận (creatinine, BUN)",
                "Theo dõi ECG nếu có rối loạn nhịp tim",
                "Rửa dạ dày và than hoạt tính nếu uống quá liều trong vòng 1-2 giờ",
                "Theo dõi ít nhất 48-72 giờ do half-life rất dài (40-60 giờ)"
            ],
            "monitoring": "Điện giải (K+, Na+, Cl-), chức năng thận (creatinine, BUN), huyết áp, nhịp tim, ECG, cân bằng dịch vào-ra"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể dùng với hoặc không có thức ăn. Dùng với thức ăn có thể giảm kích ứng dạ dày.",
                "timing": "Uống 1 lần/ngày vào buổi sáng. Tác dụng rất dài (48-72 giờ) nên chỉ cần dùng 1 lần/ngày. Bắt đầu với liều thấp (12.5mg/ngày), tăng dần nếu dung nạp."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống"
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Hygroton (chlorthalidone)",
                "UpToDate - Chlorthalidone: Drug information",
                "ESC/ESH Guidelines for the management of arterial hypertension, 2023",
                "ACC/AHA 2024 Hypertension guidance",
                "ALLHAT Study - JAMA (2002) - Chlorthalidone vs other antihypertensives"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - Multiple large RCTs (ALLHAT) and clinical guidelines (ESC/ESH 2023, ACC/AHA 2024)"
        }
    }

}

__all__ = ['DIURETICS']
