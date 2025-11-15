"""
Non-selective Beta-blockers
Non-selective beta-adrenergic blocking agents
"""
NON_SELECTIVE_BETA_BLOCKERS = {
    "Propranolol": {
        "group": "Cardiovascular - Beta-blocker (non-selective)",
        "vietnamese_name": "Propranolol, Inderal",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp",
            "Đau thắt ngực",
            "Rối loạn nhịp tim",
            "Migraine phòng ngừa",
            "Run cơ",
            "Lo âu"
        ],
        "contraindications": [
            "Hen phế quản",
            "Suy tim cấp",
            "Block nhĩ thất độ 2-3",
            "Nhịp tim chậm nặng"
        ],
        "dosage": {
            "adult_htn": "40-160mg x 2 lần/ngày",
            "adult_angina": "80-320mg x 2-3 lần/ngày",
            "adult_migraine": "20-40mg x 2-3 lần/ngày",
            "notes": "Non-selective, ức chế cả beta1 và beta2"
        },
        "side_effects": [
            "Mệt mỏi",
            "Lạnh tay chân",
            "Nhịp tim chậm",
            "Co thắt phế quản",
            "Giảm libido"
        ],
                  "interactions": [
              "Verapamil: tăng nguy cơ block nhĩ thất",
              "Insulin: che dấu triệu chứng hạ đường huyết"
          ],
          "pregnancy": "C",
          "mechanism_of_action": "Non-selective beta-adrenergic receptor blocker (beta1 và beta2). Ức chế tác dụng của catecholamines (epinephrine, norepinephrine), giảm nhịp tim, giảm co bóp cơ tim, giảm huyết áp, giảm nhu cầu oxy cơ tim. Ức chế renin-angiotensin system. Có tác dụng chống loạn nhịp (class II antiarrhythmic).",
          "monitoring": [
              "Nhịp tim và huyết áp (trước và sau khi bắt đầu)",
              "Dấu hiệu suy tim (khó thở, phù, tăng cân)",
              "Chức năng phổi (nếu có bệnh phổi tắc nghẽn)",
              "Đường huyết (đặc biệt ở bệnh nhân đái tháo đường - che dấu triệu chứng hạ đường huyết)",
              "Triệu chứng mệt mỏi, lạnh tay chân, rối loạn cương dương"
          ],
          "precautions": [
              "KHÔNG được ngừng đột ngột (có thể gây rebound hypertension, đau thắt ngực nặng, nhồi máu cơ tim). Phải giảm liều dần trong 1-2 tuần",
              "Thận trọng ở bệnh nhân hen phế quản/COPD (có thể gây co thắt phế quản nặng)",
              "Tránh dùng trong suy tim cấp, block AV độ 2-3, nhịp tim chậm <50 bpm",
              "Thận trọng ở bệnh nhân đái tháo đường (che dấu triệu chứng hạ đường huyết)",
              "Có thể gây mệt mỏi, giảm khả năng tập luyện",
              "Thận trọng khi dùng với verapamil/diltiazem (tăng nguy cơ block AV, suy tim)"
          ],
          "pharmacokinetics": {
              "half_life": "3-5 giờ (ngắn), nhưng tác dụng kéo dài hơn do tác dụng trên receptor",
              "onset": "1-2 giờ (PO)",
              "duration": "6-12 giờ",
              "protein_binding": "90-95%",
              "clearance": "Gan (extensive first-pass metabolism), CYP2D6, CYP1A2"
          },
          "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
          "black_box_warnings": "KHÔNG được ngừng đột ngột ở bệnh nhân đau thắt ngực - có thể gây đau thắt ngực nặng, nhồi máu cơ tim, rối loạn nhịp tim nặng. Phải giảm liều dần dần trong 1-2 tuần",
          "drug_interactions": {
              "major": [
                  {
                      "drug": "Verapamil, Diltiazem",
                      "mechanism": "Tác dụng hiệp đồng ức chế dẫn truyền nhĩ thất và co bóp tim",
                      "effect": "Tăng nguy cơ block nhĩ thất độ 2-3, nhịp tim chậm nặng, suy tim",
                      "management": "Thận trọng. Tránh dùng cùng nếu có thể. Nếu cần, dùng liều thấp và theo dõi ECG sát."
                  }
              ],
              "moderate": [
                  {
                      "drug": "Insulin, các thuốc hạ đường huyết",
                      "mechanism": "Che dấu triệu chứng hạ đường huyết (nhịp tim nhanh, run rẩy)",
                      "effect": "Tăng nguy cơ hạ đường huyết không được phát hiện, nguy hiểm",
                      "management": "Theo dõi đường huyết thường xuyên. Bệnh nhân đái tháo đường nên biết các triệu chứng khác của hạ đường huyết."
                  },
                  {
                      "drug": "NSAIDs (ibuprofen, naproxen)",
                      "mechanism": "Giảm tác dụng hạ huyết áp",
                      "effect": "Giảm hiệu quả điều trị tăng huyết áp",
                      "management": "Thận trọng. Theo dõi huyết áp. Tránh dùng lâu dài cùng."
                  },
                  {
                      "drug": "CYP2D6, CYP1A2 inhibitors (fluoxetine, cimetidine, ciprofloxacin)",
                      "mechanism": "Ức chế chuyển hóa propranolol",
                      "effect": "Tăng nồng độ propranolol, tăng tác dụng phụ",
                      "management": "Theo dõi nhịp tim, huyết áp. Có thể cần giảm liều propranolol."
                  }
              ],
              "minor": [
                  {
                      "drug": "Chlorpromazine",
                      "mechanism": "Tăng nguy cơ an thần",
                      "effect": "Tăng tác dụng an thần",
                      "management": "Thận trọng. Tránh lái xe hoặc vận hành máy móc."
                  }
              ]
          },
          "contraindications": {
              "tuyệt_đối": [
                  "Hen phế quản",
                  "Suy tim cấp",
                  "Block nhĩ thất độ 2-3",
                  "Nhịp tim chậm nặng (<50 bpm)",
                  "Sốc tim",
                  "Hội chứng sick sinus (trừ khi có máy tạo nhịp)"
              ],
              "tương_đối": [
                  "COPD (thận trọng, có thể dùng liều thấp nhưng nguy cơ co thắt phế quản cao hơn)",
                  "Đái tháo đường (che dấu triệu chứng hạ đường huyết)",
                  "Bệnh mạch máu ngoại biên (có thể làm nặng)",
                  "Suy gan (giảm chuyển hóa, extensive first-pass)",
                  "Dùng với verapamil/diltiazem (tăng nguy cơ block AV)"
              ]
          },
          "pregnancy_lactation": {
              "fda_category": "C",
              "pregnancy_details": "Có thể dùng khi cần thiết. Có thể gây nhịp tim chậm thai nhi, hạ đường huyết, giảm thông khí. Theo dõi sát thai nhi. Ưu tiên dùng trong 3 tháng cuối nếu có thể.",
              "lactation": {
                  "safety": "Compatible",
                  "details": "Propranolol bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp. Không có báo cáo về tác dụng phụ nghiêm trọng ở trẻ bú mẹ.",
                  "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có dấu hiệu nhịp tim chậm hoặc hạ đường huyết."
              }
          },
          "hepatic_adjustment": {
              "mild": "Không đổi",
              "moderate": "Thận trọng, có thể giảm liều (extensive first-pass metabolism)",
              "severe": "Giảm liều 50% (extensive first-pass metabolism qua gan)",
              "notes": "Propranolol có extensive first-pass metabolism qua gan (CYP2D6, CYP1A2). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và tác dụng phụ."
          },
          "overdose_management": {
              "symptoms": [
                  "Nhịp tim chậm nặng (<40 bpm)",
                  "Block nhĩ thất độ 2-3",
                  "Hạ huyết áp nặng",
                  "Suy tim cấp",
                  "Co thắt phế quản nặng",
                  "Hạ đường huyết",
                  "Ngất",
                  "Sốc tim"
              ],
              "antidote": "Atropine (cho nhịp tim chậm), Glucagon (cho suy tim), Epinephrine (cho hạ huyết áp nặng)",
              "treatment": [
                  "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                  "Than hoạt tính",
                  "Điều trị nhịp tim chậm: Atropine 0.5-1mg IV, có thể lặp lại",
                  "Nếu atropine không hiệu quả: Glucagon 1-5mg IV (kích thích tim qua cơ chế không phụ thuộc beta-receptor)",
                  "Điều trị hạ huyết áp: Truyền dịch, nâng chân, nếu cần: dopamine, norepinephrine",
                  "Điều trị block AV: Atropine, nếu cần: máy tạo nhịp tạm thời",
                  "Điều trị co thắt phế quản: Albuterol, ipratropium (quan trọng vì non-selective)",
                  "Điều trị hạ đường huyết: Glucose IV",
                  "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                  "Theo dõi ít nhất 12-24 giờ (do half-life 3-5 giờ nhưng tác dụng kéo dài)"
              ],
              "monitoring": "Nhịp tim, huyết áp, ECG (block AV, rối loạn nhịp), đường huyết, chức năng hô hấp (đặc biệt quan trọng), ý thức"
          },
          "reversal_agents": {
              "available": True,
              "agents": [
                  {
                      "name": "Glucagon",
                      "mechanism": "Kích thích tim qua cơ chế không phụ thuộc beta-receptor (tăng cAMP)",
                      "indication": "Suy tim, nhịp tim chậm nặng do beta-blocker",
                      "dose": "1-5mg IV, có thể lặp lại"
                  },
                  {
                      "name": "Atropine",
                      "mechanism": "Ức chế phó giao cảm, tăng nhịp tim",
                      "indication": "Nhịp tim chậm, block nhĩ thất",
                      "dose": "0.5-1mg IV, có thể lặp lại"
                  }
              ]
          },
          "administration_instructions": {
              "oral": {
                  "with_food": "Uống với thức ăn để giảm tác dụng phụ và tăng hấp thu (giảm first-pass metabolism).",
                  "timing": "Uống 2-3 lần/ngày (do half-life ngắn). Uống cùng giờ mỗi ngày. KHÔNG ngừng đột ngột - giảm liều dần dần trong 1-2 tuần."
              },
              "iv": {
                  "reconstitution": "Không có dạng IV thường dùng",
                  "infusion_rate": "N/A",
                  "compatibility": [],
                  "incompatibility": [],
                  "notes": "Chỉ có dạng uống thường dùng"
              }
          },
          "references": {
              "primary_sources": [
                  "FDA Drug Label - Inderal (propranolol)",
                  "UpToDate - Propranolol: Drug information",
                  "Beta-Blocker Heart Attack Trial - JAMA",
                  "ISIS-1 Study - The Lancet",
                  "American Heart Association/American College of Cardiology guidelines"
              ],
              "last_updated": "2024-12-19",
              "evidence_level": "High - Multiple large RCTs (BHAT, ISIS-1) and extensive clinical experience"
          }    },

    "Carvedilol": {
    "group": "Cardiovascular - Beta-blocker (Non-selective with Alpha-blocking)",
    "vietnamese_name": "Carvedilol, Dilatrend",
    "administration": ["PO"],
    "indications": [
        "Suy tim (NYHA class II-IV)",
        "Tăng huyết áp",
        "Sau nhồi máu cơ tim"
    ],
    "contraindications": [
        "Hen phế quản nặng",
        "Block nhĩ thất độ 2-3",
        "Suy tim cấp không bù",
        "Nhịp tim chậm nặng",
        "Suy gan nặng"
    ],
    "dosage": {
        "adult_heart_failure": "3.125mg x 2 lần/ngày, tăng dần mỗi 2 tuần đến 25mg x 2 lần/ngày",
        "adult_htn": "6.25-25mg x 2 lần/ngày",
        "adult_post_mi": "6.25-25mg x 2 lần/ngày",
        "notes": "Có bằng chứng giảm tỷ lệ tử vong trong suy tim. Có tác dụng giãn mạch"
    },
    "renal_adjustment": {
        "normal": "Không đổi",
        "30_60": "Thận trọng",
        "under_30": "Thận trọng"
    },
    "side_effects": [
        "Mệt mỏi",
        "Chóng mặt",
        "Hạ huyết áp",
        "Nhịp tim chậm",
        "Phù chân (ít)"
    ],
          "interactions": [
          "Digoxin: tăng nồng độ digoxin",
          "Insulin: che dấu triệu chứng hạ đường huyết",
          "CYP2D6 inhibitors: tăng nồng độ carvedilol"
      ],
      "pregnancy": "C",
      "mechanism_of_action": "Non-selective beta-adrenergic receptor blocker (beta1 và beta2) kết hợp với alpha-1 adrenergic receptor blocker. Ức chế beta receptors làm giảm nhịp tim, giảm co bóp cơ tim, giảm huyết áp. Block alpha-1 receptors gây giãn mạch, giảm hậu gánh, cải thiện tuần hoàn. Có bằng chứng mạnh làm giảm tỷ lệ tử vong và nhập viện trong suy tim mạn tính (NYHA class II-IV).",
      "monitoring": [
          "Nhịp tim và huyết áp (trước và sau khi bắt đầu, đặc biệt ở bệnh nhân suy tim - có thể gây hạ huyết áp)",
          "Dấu hiệu suy tim: khó thở, phù, tăng cân, giảm khả năng gắng sức",
          "Chức năng gan (chống chỉ định trong suy gan nặng)",
          "Đường huyết (ở bệnh nhân đái tháo đường)",
          "Triệu chứng mệt mỏi, chóng mặt, hạ huyết áp, phù chân"
      ],
      "precautions": [
          "KHÔNG được ngừng đột ngột (có thể gây rebound hypertension, đau thắt ngực nặng, suy tim nặng). Phải giảm liều dần trong 1-2 tuần",
          "Khởi đầu với liều rất thấp (3.125mg x 2 lần/ngày) ở bệnh nhân suy tim, tăng dần mỗi 2 tuần",
          "CHỐNG CHỈ ĐỊNH trong suy gan nặng",
          "Thận trọng ở bệnh nhân hen phế quản/COPD (non-selective, có thể gây co thắt phế quản nặng)",
          "Tránh dùng trong suy tim cấp không bù, block AV độ 2-3, nhịp tim chậm <60 bpm",
          "Có thể gây hạ huyết áp nặng (do tác dụng alpha-blocking) - theo dõi sát khi bắt đầu",
          "Thận trọng khi dùng với digoxin (tăng nồng độ digoxin)",
          "Thận trọng với CYP2D6 inhibitors (tăng nồng độ carvedilol)"
      ],
      "pharmacokinetics": {
          "half_life": "7-10 giờ",
          "onset": "1-2 giờ (PO)",
          "duration": "12-24 giờ (uống 2 lần/ngày)",
          "protein_binding": "98% (rất cao)",
          "clearance": "Gan (chủ yếu, chuyển hóa qua CYP2D6, CYP2C9, CYP3A4). Thải qua phân và nước tiểu"
      },
      "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
      "black_box_warnings": "KHÔNG được ngừng đột ngột ở bệnh nhân đau thắt ngực hoặc suy tim - có thể gây đau thắt ngực nặng, nhồi máu cơ tim, suy tim nặng. Phải giảm liều dần dần trong 1-2 tuần",
      "drug_interactions": {
          "major": [
              {
                  "drug": "Verapamil, Diltiazem",
                  "mechanism": "Tác dụng hiệp đồng ức chế dẫn truyền nhĩ thất",
                  "effect": "Tăng nguy cơ block nhĩ thất độ 2-3, suy tim, nhịp tim chậm nặng",
                  "management": "Thận trọng. Theo dõi ECG, nhịp tim, huyết áp. Tránh dùng cùng nếu có thể."
              },
              {
                  "drug": "CYP2D6 inhibitors (fluoxetine, paroxetine, quinidine)",
                  "mechanism": "Ức chế chuyển hóa carvedilol qua CYP2D6",
                  "effect": "Tăng nồng độ carvedilol đáng kể, tăng tác dụng phụ (hạ huyết áp, nhịp tim chậm)",
                  "management": "Thận trọng. Giảm liều carvedilol. Theo dõi nhịp tim, huyết áp sát."
              }
          ],
          "moderate": [
              {
                  "drug": "Digoxin",
                  "mechanism": "Carvedilol tăng nồng độ digoxin",
                  "effect": "Tăng nguy cơ ngộ độc digoxin (nhịp tim chậm, block AV, rối loạn nhịp)",
                  "management": "Theo dõi nồng độ digoxin. Có thể cần giảm liều digoxin."
              },
              {
                  "drug": "CYP3A4 inhibitors (ketoconazole, itraconazole, clarithromycin)",
                  "mechanism": "Ức chế chuyển hóa carvedilol qua CYP3A4",
                  "effect": "Tăng nồng độ carvedilol, tăng tác dụng phụ",
                  "management": "Thận trọng. Theo dõi nhịp tim, huyết áp. Có thể cần giảm liều carvedilol."
              },
              {
                  "drug": "Insulin, Sulfonylureas",
                  "mechanism": "Che dấu triệu chứng hạ đường huyết",
                  "effect": "Hạ đường huyết nặng, khó nhận biết triệu chứng",
                  "management": "Theo dõi đường huyết thường xuyên."
              }
          ],
          "minor": [
              {
                  "drug": "NSAIDs",
                  "mechanism": "Giảm tác dụng hạ huyết áp",
                  "effect": "Giảm hiệu quả hạ huyết áp",
                  "management": "Theo dõi huyết áp."
              }
          ]
      },
      "contraindications": {
          "tuyệt_đối": [
              "Hen phế quản nặng",
              "Block nhĩ thất độ 2-3 không có máy tạo nhịp",
              "Suy tim cấp không bù",
              "Nhịp tim chậm nặng (<60 bpm)",
              "Suy gan nặng",
              "Sốc tim"
          ],
          "tương_đối": [
              "COPD - thận trọng (non-selective beta-blocker, có thể gây co thắt phế quản nặng)",
              "Suy gan trung bình - thận trọng, giảm liều (thải chủ yếu qua gan)",
              "Suy thận nặng - thận trọng",
              "Đái tháo đường - thận trọng (che dấu triệu chứng hạ đường huyết)",
              "Dùng với verapamil/diltiazem - tăng nguy cơ block AV",
              "Dùng với CYP2D6 inhibitors - tăng nồng độ carvedilol đáng kể"
          ]
      },
      "pregnancy_lactation": {
          "fda_category": "C",
          "pregnancy_details": "Có thể gây hạ huyết áp, nhịp tim chậm ở thai nhi. Có thể gây chậm phát triển thai nhi, nhịp tim chậm ở trẻ sơ sinh. Cân nhắc lợi ích/nguy cơ. Thường dùng được nếu lợi ích vượt trội nguy cơ, đặc biệt trong suy tim.",
          "lactation": {
              "safety": "Compatible",
              "details": "Carvedilol bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp. Có thể gây nhịp tim chậm nhẹ ở trẻ bú mẹ nhưng hiếm.",
              "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có nhịp tim chậm, mệt mỏi, tăng cân kém."
          }
      },
      "hepatic_adjustment": {
          "mild": "Không đổi",
          "moderate": "Thận trọng, giảm liều (thải chủ yếu qua gan)",
          "severe": "CHỐNG CHỈ ĐỊNH (thải chủ yếu qua gan, chuyển hóa qua CYP2D6, CYP2C9, CYP3A4)",
          "notes": "Carvedilol thải chủ yếu qua gan (chuyển hóa qua CYP2D6, CYP2C9, CYP3A4). Suy gan nặng là chống chỉ định tuyệt đối. Suy gan trung bình cần giảm liều và theo dõi sát."
      },
      "overdose_management": {
          "symptoms": [
              "Nhịp tim chậm nặng (<40 bpm)",
              "Block nhĩ thất độ 2-3",
              "Hạ huyết áp nặng (do cả beta và alpha-blocking)",
              "Suy tim cấp",
              "Co giật",
              "Hôn mê",
              "Suy hô hấp"
          ],
          "antidote": "Glucagon (có thể đảo ngược tác dụng beta-blocker), Atropine (cho nhịp tim chậm), Epinephrine (cho hạ huyết áp nặng)",
          "treatment": [
              "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
              "Than hoạt tính",
              "Điều trị nhịp tim chậm: Atropine 0.5-1mg IV, có thể lặp lại. Nếu không hiệu quả: Glucagon 1-5mg IV, Isoproterenol, hoặc máy tạo nhịp tạm thời",
              "Điều trị hạ huyết áp: Truyền dịch (normal saline), nâng chân, Glucagon 1-5mg IV, Epinephrine (thận trọng - có thể gây tăng huyết áp quá mức)",
              "Theo dõi ECG liên tục",
              "Theo dõi huyết áp, nhịp tim, ý thức",
              "Hỗ trợ hô hấp nếu cần",
              "Theo dõi ít nhất 24-48 giờ (do half-life 7-10 giờ)"
          ],
          "monitoring": "ECG liên tục, huyết áp, nhịp tim, ý thức, dấu hiệu suy tim, dấu hiệu suy hô hấp"
      },
      "reversal_agents": {
          "available": True,
          "agents": [
              {
                  "name": "Glucagon",
                  "mechanism": "Kích thích cAMP, đảo ngược tác dụng beta-blocker",
                  "dose": "1-5mg IV, có thể lặp lại",
                  "indication": "Nhịp tim chậm, hạ huyết áp do quá liều beta-blocker"
              },
              {
                  "name": "Atropine",
                  "mechanism": "Chẹn muscarinic, tăng nhịp tim",
                  "dose": "0.5-1mg IV, có thể lặp lại",
                  "indication": "Nhịp tim chậm, block AV"
              },
              {
                  "name": "Epinephrine",
                  "mechanism": "Agonist alpha và beta, tăng nhịp tim và huyết áp",
                  "dose": "Theo protocol ACLS",
                  "indication": "Hạ huyết áp nặng không đáp ứng với glucagon"
              }
          ]
      },
      "administration_instructions": {
          "oral": {
              "with_food": "Nên uống với thức ăn để giảm nguy cơ hạ huyết áp và tăng hấp thu.",
              "timing": "Uống 2 lần/ngày (sáng và tối). Ở bệnh nhân suy tim: khởi đầu với liều rất thấp (3.125mg x 2 lần/ngày), tăng dần mỗi 2 tuần. KHÔNG ngừng đột ngột - phải giảm liều dần trong 1-2 tuần."
          },
          "iv": {
              "reconstitution": "Không có dạng IV",
              "infusion_rate": "Không áp dụng",
              "compatibility": [],
              "incompatibility": [],
              "notes": "Carvedilol chỉ có dạng uống (PO)."
          }
      },
      "references": {
          "primary_sources": [
              "FDA Drug Label - Coreg (carvedilol)",
              "UpToDate - Carvedilol: Drug information",
              "COPERNICUS Study - New England Journal of Medicine (2001) - Carvedilol trong suy tim nặng",
              "CAPRICORN Study - Lancet (2001) - Carvedilol sau nhồi máu cơ tim",
              "American Heart Association/American College of Cardiology guidelines - Beta-blockers in heart failure"
          ],
          "last_updated": "2024-12-19",
          "evidence_level": "High - Multiple large RCTs (COPERNICUS, CAPRICORN) showing mortality benefit in heart failure and extensive clinical experience"
      }    }
}

__all__ = ['NON_SELECTIVE_BETA_BLOCKERS']
