"""
Infectious Disease & Antibiotic Drugs (Other) - Macrolides, Fluoroquinolones, Antimalarials, etc.
"""

INFECTIOUS_OTHER_DRUGS = {
    "Azithromycin": {
        "group": "Infectious Disease - Macrolide Antibiotic",
        "vietnamese_name": "Azithromycin, Zithromax",
        "administration": ["PO", "IV"],
        "indications": [
            "Nhiễm trùng đường hô hấp trên (viêm họng, viêm xoang)",
            "Nhiễm trùng đường hô hấp dưới (viêm phổi, viêm phế quản)",
            "Nhiễm trùng da và mô mềm",
            "Chlamydia",
            "Nhiễm trùng đường tiết niệu không biến chứng"
        ],
        "contraindications": [
            "Dị ứng azithromycin/macrolide",
            "QT kéo dài",
            "Rối loạn nhịp tim"
        ],
        "dosage": {
            "adult_respiratory": "500mg x 1 lần/ngày x 3 ngày hoặc 500mg ngày đầu, sau đó 250mg x 1 lần/ngày x 4 ngày",
            "adult_chlamydia": "1g x 1 lần (đơn liều)",
            "adult_iv": "500mg x 1 lần/ngày IV",
            "notes": "Tác dụng kéo dài, uống ít lần hơn erythromycin"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng"
        },
        "side_effects": [
            "Buồn nôn, nôn, tiêu chảy",
            "Đau bụng",
            "QT kéo dài",
            "Loạn nhịp tim (torsades de pointes)",
            "Rối loạn thính giác (hiếm)"
        ],
                  "interactions": [
              "Warfarin: tăng nguy cơ chảy máu",
              "Digoxin: tăng nồng độ digoxin",
              "Cyclosporine: tăng nồng độ cyclosporine",
              "Thuốc QT kéo dài: tăng nguy cơ loạn nhịp"
          ],
          "pregnancy": "B",
          "mechanism_of_action": "Macrolide antibiotic. Ức chế tổng hợp protein vi khuẩn bằng cách gắn vào 50S ribosomal subunit, ức chế peptide chain elongation. Phổ tác dụng: Gram-positive (Streptococcus, Staphylococcus), một số Gram-negative (Haemophilus influenzae), atypical pathogens (Mycoplasma, Chlamydia, Legionella). Có tác dụng kéo dài do thời gian bán hủy dài (68 giờ), cho phép phác đồ ngắn (3-5 ngày).",
          "monitoring": [
              "ECG: QT interval (có thể gây QT kéo dài, đặc biệt ở bệnh nhân có yếu tố nguy cơ)",
              "Triệu chứng rối loạn nhịp tim (torsades de pointes - hiếm nhưng nguy hiểm)",
              "Chức năng gan: ALT, AST (hiếm gây độc gan)",
              "Triệu chứng tiêu hóa: buồn nôn, nôn, tiêu chảy (phổ biến)",
              "Rối loạn thính giác (hiếm, thường ở liều cao hoặc dùng lâu dài)"
          ],
          "precautions": [
              "Tránh dùng ở bệnh nhân QT kéo dài hoặc có yếu tố nguy cơ (suy tim, hạ kali máu, hạ magie máu, dùng thuốc QT kéo dài khác)",
              "Thận trọng khi dùng với warfarin (tăng nguy cơ chảy máu - theo dõi INR)",
              "Thận trọng khi dùng với digoxin (tăng nồng độ digoxin - theo dõi nồng độ)",
              "Thận trọng khi dùng với cyclosporine (tăng nồng độ cyclosporine)",
              "Có thể gây tiêu chảy (phổ biến) - có thể dẫn đến C. difficile colitis nếu nặng",
              "Thận trọng ở bệnh nhân suy gan nặng"
          ],
          "pharmacokinetics": {
              "half_life": "68 giờ (RẤT DÀI - cho phép phác đồ ngắn 3-5 ngày)",
              "onset": "2-3 giờ (PO), 1 giờ (IV)",
              "duration": "5-7 ngày sau liều cuối (do half-life dài)",
              "protein_binding": "7-50% (thay đổi theo nồng độ)",
              "clearance": "Chủ yếu qua phân (không đổi), một phần qua gan. Không phụ thuộc vào chức năng thận (không cần điều chỉnh liều ở suy thận)"
          },
          "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Bảo quản suspension trong tủ lạnh sau khi pha",
          "black_box_warnings": "Có thể gây QT kéo dài và torsades de pointes, đặc biệt ở bệnh nhân có yếu tố nguy cơ (suy tim, hạ kali máu, hạ magie máu, nhịp tim chậm, dùng thuốc QT kéo dài khác). Tránh dùng ở bệnh nhân QT kéo dài",
          "drug_interactions": {
              "major": [
                  {
                      "drug": "Warfarin",
                      "mechanism": "Azithromycin có thể ảnh hưởng đến hệ vi khuẩn đường ruột, làm giảm tổng hợp vitamin K, tăng tác dụng warfarin. Cũng có thể ức chế nhẹ CYP450.",
                      "effect": "Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu",
                      "management": "Theo dõi INR chặt chẽ khi bắt đầu, thay đổi liều, hoặc ngừng azithromycin. Điều chỉnh liều warfarin nếu cần."
                  },
                  {
                      "drug": "Digoxin",
                      "mechanism": "Azithromycin có thể ảnh hưởng đến hệ vi khuẩn đường ruột, làm giảm chuyển hóa digoxin, tăng hấp thu digoxin.",
                      "effect": "Tăng nồng độ digoxin, tăng độc tính (buồn nôn, nôn, rối loạn nhịp tim, block AV)",
                      "management": "Theo dõi nồng độ digoxin và dấu hiệu độc tính. Giảm liều digoxin nếu cần. Theo dõi ECG."
                  }
              ],
              "moderate": [
                  {
                      "drug": "Cyclosporine, Tacrolimus",
                      "mechanism": "Azithromycin có thể ức chế nhẹ CYP3A4, làm giảm chuyển hóa cyclosporine và tacrolimus.",
                      "effect": "Tăng nồng độ cyclosporine/tacrolimus, tăng độc tính (độc thận, tăng huyết áp, độc thần kinh)",
                      "management": "Theo dõi nồng độ cyclosporine/tacrolimus, chức năng thận. Điều chỉnh liều nếu cần."
                  },
                  {
                      "drug": "Thuốc kéo dài QT (Amiodarone, Sotalol, Antipsychotics)",
                      "mechanism": "Cả hai đều kéo dài QT interval, tác dụng cộng dồn.",
                      "effect": "Tăng nguy cơ QT kéo dài, torsades de pointes, rối loạn nhịp tim nghiêm trọng",
                      "management": "TRÁNH DÙNG đồng thời nếu có thể. Nếu bắt buộc, theo dõi ECG chặt chẽ. Đảm bảo kali, magie bình thường. Ngừng ngay nếu QT >500ms hoặc có triệu chứng."
                  }
              ],
              "minor": [
                  {
                      "drug": "Antacids (Aluminum, Magnesium)",
                      "mechanism": "Antacids có thể giảm nhẹ hấp thu azithromycin.",
                      "effect": "Giảm nhẹ hấp thu azithromycin",
                      "management": "Cách 2 giờ nếu có thể. Không ảnh hưởng đáng kể ở liều điều trị thông thường."
                  }
              ]
          },
          "contraindications": {
              "tuyệt_đối": [
                  "Dị ứng azithromycin hoặc các macrolide khác (erythromycin, clarithromycin)",
                  "QT kéo dài hoặc rối loạn nhịp tim nặng - tăng nguy cơ torsades de pointes",
                  "Dùng với pimozide, terfenadine, astemizole - tăng nguy cơ loạn nhịp tim nghiêm trọng"
              ],
              "tương_đối": [
                  "Suy tim - tăng nguy cơ QT kéo dài, torsades de pointes",
                  "Hạ kali máu, hạ magie máu - tăng nguy cơ QT kéo dài, torsades de pointes",
                  "Nhịp tim chậm - tăng nguy cơ QT kéo dài",
                  "Dùng với thuốc kéo dài QT khác - tác dụng cộng dồn",
                  "Suy gan nặng - thận trọng, có thể giảm chuyển hóa",
                  "Suy thận nặng - thận trọng, mặc dù không cần điều chỉnh liều thường quy"
              ]
          },
          "pregnancy_lactation": {
              "fda_category": "B",
              "pregnancy_details": "Azithromycin phân loại B - an toàn trong thai kỳ. Các nghiên cứu trên động vật không cho thấy nguy cơ gây dị tật thai nhi. Các nghiên cứu trên người không cho thấy nguy cơ tăng dị tật bẩm sinh. Macrolide là một trong những kháng sinh an toàn nhất trong thai kỳ (sau penicillin). Được sử dụng rộng rãi trong thai kỳ để điều trị nhiễm trùng, đặc biệt Chlamydia. Tuy nhiên, nên dùng liều thấp nhất hiệu quả và tránh dùng không cần thiết.",
              "lactation": {
                  "safety": "Compatible",
                  "details": "Azithromycin bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ. Macrolide là một trong những kháng sinh an toàn nhất khi cho con bú.",
                  "recommendation": "Có thể dùng khi cho con bú. Dùng liều thấp nhất hiệu quả. Theo dõi trẻ sơ sinh nếu dùng liều cao hoặc kéo dài (tiêu chảy, phát ban)."
              }
          },
          "hepatic_adjustment": {
              "mild": "Không cần điều chỉnh liều. Azithromycin chuyển hóa một phần qua gan nhưng không đáng kể.",
              "moderate": "Thận trọng, có thể cần giảm liều nhẹ. Chuyển hóa có thể giảm ở suy gan trung bình, nhưng thải trừ chủ yếu qua phân nên ít ảnh hưởng.",
              "severe": "Thận trọng, có thể cần giảm liều. Chuyển hóa có thể giảm ở suy gan nặng, nhưng thải trừ chủ yếu qua phân nên ít ảnh hưởng. Tuy nhiên, suy gan nặng có thể kèm theo suy thận, nên cần theo dõi chặt chẽ.",
              "notes": "Azithromycin chuyển hóa một phần qua gan nhưng thải trừ chủ yếu qua phân (không đổi), một phần qua gan. Suy gan có thể giảm chuyển hóa nhẹ nhưng không đáng kể do thải trừ chủ yếu qua phân. Không cần điều chỉnh liều thường quy ở suy gan."
          },
          "overdose_management": {
              "symptoms": [
                  "Triệu chứng tiêu hóa: Buồn nôn, nôn, tiêu chảy, đau bụng",
                  "Triệu chứng tim mạch: QT kéo dài, torsades de pointes, rối loạn nhịp tim (hiếm nhưng nguy hiểm)",
                  "Triệu chứng thần kinh: Đau đầu, chóng mặt, mệt mỏi",
                  "Triệu chứng thính giác: Giảm thính lực, ù tai (hiếm, thường ở liều cao hoặc dùng lâu dài)",
                  "Triệu chứng nghiêm trọng: Torsades de pointes, rối loạn nhịp tim nghiêm trọng, mất thính lực"
              ],
              "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.",
              "treatment": [
                  "Ngừng ngay azithromycin",
                  "Rửa dạ dày hoặc than hoạt nếu uống trong vòng 1-2 giờ (nếu không có chống chỉ định)",
                  "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2, ECG",
                  "Điều trị triệu chứng tiêu hóa:",
                  "  - Chống nôn nếu cần",
                  "  - Truyền dịch nếu mất nước",
                  "  - Theo dõi điện giải",
                  "Điều trị QT kéo dài/torsades de pointes nếu có:",
                  "  - Theo dõi ECG liên tục",
                  "  - Đảm bảo kali, magie bình thường",
                  "  - Điều trị torsades de pointes: Magnesium sulfate IV, pacing nếu cần",
                  "  - Tránh các thuốc kéo dài QT khác",
                  "Điều trị rối loạn thính giác nếu có:",
                  "  - Ngừng ngay azithromycin",
                  "  - Điều trị hỗ trợ",
                  "  - Có thể không hồi phục",
                  "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2, ECG"
              ],
              "monitoring": "Theo dõi dấu hiệu sinh tồn, ECG (QT interval), điện giải (kali, magie), dấu hiệu thính giác trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có biến chứng (QT kéo dài, torsades de pointes, rối loạn thính giác)."
          },
          "reversal_agents": None,
          "administration_instructions": {
              "oral": {
                  "with_food": "Có thể uống với hoặc không thức ăn. Uống với thức ăn có thể giảm kích ứng dạ dày và buồn nôn. Có thể uống không thức ăn nếu cần.",
                  "timing": "Uống 1 lần/ngày (phác đồ 3-5 ngày) hoặc theo chỉ định. Uống đều đặn, cách đều nhau trong ngày. Không bỏ liều. Có thể uống trước hoặc sau bữa ăn."
              },
              "iv": {
                  "reconstitution": "Pha theo hướng dẫn nhà sản xuất. Thường pha với nước cất vô trùng hoặc NaCl 0.9%. Lắc kỹ để hòa tan hoàn toàn.",
                  "infusion_rate": "Truyền IV trong 60 phút (không truyền nhanh hơn). Có thể truyền trong 30 phút nếu cần nhưng không khuyến nghị.",
                  "compatibility": [
                      "NaCl 0.9%",
                      "D5W (Dextrose 5%)",
                      "Nước cất vô trùng"
                  ],
                  "incompatibility": [
                      "Không trộn với các thuốc khác trong cùng một bơm tiêm hoặc chai truyền",
                      "Lactated Ringer's (LR) - không tương thích",
                      "Các dung dịch có cation (Al3+, Mg2+) - có thể tạo phức hợp"
                  ],
                  "notes": "Truyền IV trong 60 phút. Không truyền nhanh hơn. Theo dõi phản ứng tại chỗ tiêm (viêm tĩnh mạch). Dùng ngay sau khi pha. Không bảo quản lâu sau khi pha."
              }
          },
          "references": {
              "primary_sources": [
                  "FDA Label: Zithromax (azithromycin)",
                  "UpToDate: Azithromycin drug information",
                  "Lexicomp: Azithromycin monograph",
                  "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
                  "Sanford Guide to Antimicrobial Therapy"
              ],
              "last_updated": "2025-02-03",
              "evidence_level": "Level 1 - FDA approved, multiple clinical trials, extensive clinical experience"
          }
      },

      "Clarithromycin": {
        "group": "Infectious Disease - Macrolide Antibiotic",
        "vietnamese_name": "Clarithromycin, Klacid",
        "administration": ["PO", "IV"],
        "indications": [
            "Nhiễm trùng đường hô hấp (viêm phổi, viêm phế quản)",
            "Nhiễm trùng da và mô mềm",
            "Tiệt trừ H. pylori (kết hợp)",
            "Mycobacterium avium complex (MAC)"
        ],
        "contraindications": [
            "Dị ứng clarithromycin/macrolide",
            "QT kéo dài",
            "Dùng pimozide, terfenadine, astemizole"
        ],
        "dosage": {
            "adult_respiratory": "250-500mg x 2 lần/ngày x 7-14 ngày",
            "adult_h_pylori": "500mg x 2 lần/ngày (với amoxicillin + PPI)",
            "adult_mac": "500mg x 2 lần/ngày",
            "notes": "Mạnh hơn azithromycin nhưng nhiều tương tác hơn"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 50%",
            "under_30": "Giảm liều 50-75%"
        },
        "side_effects": [
            "Buồn nôn, nôn",
            "Tiêu chảy",
            "Vị kim loại trong miệng",
            "QT kéo dài",
            "Rối loạn thính giác (hiếm)"
        ],
        "interactions": [
            "CYP3A4 substrates: tăng đáng kể nồng độ (simvastatin, lovastatin, midazolam)",
            "Warfarin: tăng tác dụng chống đông",
            "Digoxin: tăng nồng độ digoxin",
            "Theophylline: tăng nồng độ theophylline"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Clarithromycin là kháng sinh macrolide bán tổng hợp, thuộc nhóm azalide. Ức chế tổng hợp protein của vi khuẩn bằng cách gắn vào tiểu đơn vị 50S của ribosome vi khuẩn, ngăn chặn quá trình dịch mã (translocation) và kéo dài chuỗi peptide. Dẫn đến ngừng tổng hợp protein và ức chế sự phát triển của vi khuẩn. Clarithromycin có phổ kháng khuẩn rộng: Gram-dương (Streptococcus pneumoniae, Staphylococcus aureus - không phải MRSA), một số Gram-âm (H. influenzae, Moraxella catarrhalis), và vi khuẩn không điển hình (Mycoplasma pneumoniae, Chlamydia pneumoniae, Legionella pneumophila). Clarithromycin cũng có tác dụng với Helicobacter pylori và một số vi khuẩn không điển hình khác. Mạnh hơn azithromycin nhưng có nhiều tương tác thuốc hơn do ức chế CYP3A4.",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng) để đánh giá đáp ứng điều trị",
            "Cấy máu và cấy từ vị trí nhiễm trùng (nếu có) để xác định vi khuẩn và độ nhạy cảm",
            "ECG - QT kéo dài (đặc biệt ở bệnh nhân có nguy cơ, dùng với thuốc kéo dài QT khác)",
            "Rối loạn thính giác (giảm thính lực, ù tai) - hiếm nhưng có thể không hồi phục",
            "Chức năng gan (ALT, AST) nếu dùng lâu dài hoặc có triệu chứng",
            "Chức năng thận (creatinine) - điều chỉnh liều ở suy thận",
            "Tương tác với CYP3A4 substrates (simvastatin, lovastatin, midazolam, warfarin, digoxin, theophylline) - theo dõi tác dụng phụ và nồng độ nếu có"
        ],
        "precautions": [
            "QT kéo dài - không dùng với các thuốc kéo dài QT khác (amiodarone, sotalol, antipsychotics), bệnh nhân có tiền sử rối loạn nhịp",
            "Không dùng với pimozide, terfenadine, astemizole (tăng nguy cơ loạn nhịp nghiêm trọng)",
            "Nhiều tương tác thuốc do ức chế CYP3A4 - tăng nồng độ simvastatin, lovastatin (nguy cơ tiêu cơ vân), midazolam, warfarin (tăng INR), digoxin (tăng nồng độ), theophylline (tăng nồng độ)",
            "Giảm liều ở suy thận (CrCl <30: giảm 50-75%)",
            "Uống với thức ăn để giảm buồn nôn, nôn",
            "Rối loạn thính giác - ngừng ngay nếu có giảm thính lực, ù tai (có thể không hồi phục)",
            "Vị kim loại trong miệng - tác dụng phụ phổ biến, thường tự khỏi",
            "Thận trọng ở bệnh nhân có bệnh gan (metabolite qua gan)",
            "Dùng đủ liều và đủ thời gian để tránh kháng thuốc"
        ],
        "pharmacokinetics": {
            "half_life": "3-7 giờ (tăng ở suy thận)",
            "onset": "2-4 giờ",
            "duration": "q12h (dùng 2 lần/ngày)",
            "protein_binding": "70%",
            "clearance": "Gan: chuyển hóa qua CYP3A4 thành 14-hydroxyclarithromycin (metabolite hoạt động, mạnh hơn với H. influenzae). Thận: bài tiết một phần nguyên dạng và metabolites. Cần điều chỉnh liều ở suy thận (CrCl <30)."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín. Dạng suspension: bảo quản ở nhiệt độ phòng, lắc kỹ trước khi dùng, dùng trong vòng 14 ngày sau khi pha. IV: bảo quản trong tủ lạnh, để nhiệt độ phòng trước khi pha.",
        "black_box_warnings": "Tăng nguy cơ tử vong do tim mạch ở bệnh nhân có bệnh tim mạch. Không dùng ở bệnh nhân có QT kéo dài, loạn nhịp tim, hoặc dùng với các thuốc kéo dài QT. Tăng nguy cơ tiêu cơ vân khi dùng với simvastatin, lovastatin.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Simvastatin, Lovastatin",
                    "mechanism": "Clarithromycin ức chế mạnh CYP3A4, làm giảm chuyển hóa simvastatin và lovastatin.",
                    "effect": "Tăng nồng độ statin, tăng nguy cơ tiêu cơ vân (myopathy, rhabdomyolysis), suy thận cấp",
                    "management": "TRÁNH DÙNG đồng thời nếu có thể. Nếu bắt buộc, giảm liều statin hoặc tạm ngừng. Dùng pravastatin hoặc rosuvastatin (ít chuyển hóa qua CYP3A4) nếu có thể. Theo dõi CK, dấu hiệu đau cơ."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Clarithromycin ức chế CYP2C9 và CYP3A4, làm giảm chuyển hóa warfarin.",
                    "effect": "Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu nghiêm trọng",
                    "management": "Theo dõi INR chặt chẽ khi bắt đầu, thay đổi liều, hoặc ngừng clarithromycin. Giảm liều warfarin 25-50% khi bắt đầu clarithromycin. Điều chỉnh liều warfarin theo INR."
                },
                {
                    "drug": "Digoxin",
                    "mechanism": "Clarithromycin ức chế P-glycoprotein và ảnh hưởng đến hệ vi khuẩn đường ruột, làm tăng hấp thu và giảm thải trừ digoxin.",
                    "effect": "Tăng nồng độ digoxin, tăng độc tính (buồn nôn, nôn, rối loạn nhịp tim, block AV)",
                    "management": "Theo dõi nồng độ digoxin và dấu hiệu độc tính. Giảm liều digoxin 25-50% khi bắt đầu clarithromycin. Theo dõi ECG."
                },
                {
                    "drug": "Pimozide, Terfenadine, Astemizole",
                    "mechanism": "Clarithromycin ức chế CYP3A4, làm giảm chuyển hóa pimozide, terfenadine, astemizole. Cả hai đều kéo dài QT interval.",
                    "effect": "Tăng nồng độ thuốc, tăng nguy cơ QT kéo dài, torsades de pointes, rối loạn nhịp tim nghiêm trọng, tử vong",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI. Không dùng đồng thời."
                }
            ],
            "moderate": [
                {
                    "drug": "Midazolam, Triazolam",
                    "mechanism": "Clarithromycin ức chế CYP3A4, làm giảm chuyển hóa benzodiazepine.",
                    "effect": "Tăng nồng độ benzodiazepine, tăng tác dụng an thần, kéo dài thời gian tác dụng",
                    "management": "Giảm liều benzodiazepine 50-75%. Theo dõi dấu hiệu an thần quá mức, suy hô hấp."
                },
                {
                    "drug": "Theophylline",
                    "mechanism": "Clarithromycin có thể ảnh hưởng đến chuyển hóa theophylline.",
                    "effect": "Tăng nồng độ theophylline, tăng độc tính (buồn nôn, nôn, co giật, rối loạn nhịp tim)",
                    "management": "Theo dõi nồng độ theophylline. Giảm liều theophylline nếu cần. Theo dõi dấu hiệu độc tính."
                },
                {
                    "drug": "Cyclosporine, Tacrolimus",
                    "mechanism": "Clarithromycin ức chế CYP3A4, làm giảm chuyển hóa cyclosporine và tacrolimus.",
                    "effect": "Tăng nồng độ cyclosporine/tacrolimus, tăng độc tính (độc thận, tăng huyết áp, độc thần kinh)",
                    "management": "Giảm liều cyclosporine/tacrolimus 25-50% khi bắt đầu clarithromycin. Theo dõi nồng độ, chức năng thận. Điều chỉnh liều theo nồng độ."
                },
                {
                    "drug": "Thuốc kéo dài QT (Amiodarone, Sotalol, Antipsychotics)",
                    "mechanism": "Cả hai đều kéo dài QT interval, tác dụng cộng dồn.",
                    "effect": "Tăng nguy cơ QT kéo dài, torsades de pointes, rối loạn nhịp tim nghiêm trọng",
                    "management": "TRÁNH DÙNG đồng thời nếu có thể. Nếu bắt buộc, theo dõi ECG chặt chẽ. Đảm bảo kali, magie bình thường. Ngừng ngay nếu QT >500ms hoặc có triệu chứng."
                }
            ],
            "minor": [
                {
                    "drug": "Rifampin",
                    "mechanism": "Rifampin cảm ứng CYP3A4, làm tăng chuyển hóa clarithromycin.",
                    "effect": "Giảm nồng độ clarithromycin, giảm hiệu quả điều trị",
                    "management": "Tăng liều clarithromycin nếu cần. Theo dõi đáp ứng điều trị."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng clarithromycin hoặc các macrolide khác (erythromycin, azithromycin)",
                "QT kéo dài hoặc rối loạn nhịp tim nặng - tăng nguy cơ tử vong do tim mạch",
                "Dùng với pimozide, terfenadine, astemizole - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI, tăng nguy cơ loạn nhịp tim nghiêm trọng, tử vong",
                "Bệnh tim mạch nặng - tăng nguy cơ tử vong do tim mạch"
            ],
            "tương_đối": [
                "Suy tim - tăng nguy cơ QT kéo dài, tử vong do tim mạch",
                "Hạ kali máu, hạ magie máu - tăng nguy cơ QT kéo dài, torsades de pointes",
                "Dùng với thuốc kéo dài QT khác - tác dụng cộng dồn",
                "Dùng với simvastatin, lovastatin - tăng nguy cơ tiêu cơ vân",
                "Dùng với warfarin - tăng nguy cơ chảy máu",
                "Dùng với digoxin - tăng độc tính digoxin",
                "Suy thận nặng (CrCl <30) - cần giảm liều 50-75%",
                "Suy gan - thận trọng, có thể giảm chuyển hóa"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Clarithromycin phân loại C - thận trọng trong thai kỳ. Các nghiên cứu trên động vật cho thấy một số nguy cơ (giảm cân, chậm phát triển xương). Các nghiên cứu trên người không cho thấy nguy cơ tăng dị tật bẩm sinh rõ ràng, nhưng dữ liệu còn hạn chế. Macrolide nói chung an toàn hơn nhiều kháng sinh khác trong thai kỳ. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt trong điều trị H. pylori hoặc nhiễm trùng nặng. Tuy nhiên, nên dùng liều thấp nhất hiệu quả và tránh dùng không cần thiết. Azithromycin có thể là lựa chọn an toàn hơn trong thai kỳ (phân loại B).",
            "lactation": {
                "safety": "Compatible",
                "details": "Clarithromycin bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ. Macrolide là một trong những kháng sinh an toàn nhất khi cho con bú.",
                "recommendation": "Có thể dùng khi cho con bú. Dùng liều thấp nhất hiệu quả. Theo dõi trẻ sơ sinh nếu dùng liều cao hoặc kéo dài (tiêu chảy, phát ban)."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Clarithromycin chuyển hóa qua gan nhưng không đáng kể ở suy gan nhẹ.",
            "moderate": "Thận trọng, có thể cần giảm liều nhẹ. Chuyển hóa có thể giảm ở suy gan trung bình.",
            "severe": "Thận trọng, có thể cần giảm liều. Chuyển hóa có thể giảm đáng kể ở suy gan nặng, tăng nồng độ clarithromycin và nguy cơ tác dụng phụ.",
            "notes": "Clarithromycin chuyển hóa qua CYP3A4 thành 14-hydroxyclarithromycin (metabolite hoạt động). Suy gan có thể giảm chuyển hóa, tăng nồng độ clarithromycin. Tuy nhiên, thải trừ một phần qua thận nên cần điều chỉnh liều theo cả chức năng gan và thận. Theo dõi chặt chẽ tác dụng phụ ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng tiêu hóa: Buồn nôn, nôn, tiêu chảy, đau bụng, vị kim loại trong miệng",
                "Triệu chứng tim mạch: QT kéo dài, torsades de pointes, rối loạn nhịp tim, tử vong do tim mạch (hiếm nhưng nguy hiểm)",
                "Triệu chứng thần kinh: Đau đầu, chóng mặt, mệt mỏi",
                "Triệu chứng thính giác: Giảm thính lực, ù tai (hiếm, có thể không hồi phục)",
                "Triệu chứng nghiêm trọng: Torsades de pointes, rối loạn nhịp tim nghiêm trọng, tử vong do tim mạch, mất thính lực"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.",
            "treatment": [
                "Ngừng ngay clarithromycin",
                "Rửa dạ dày hoặc than hoạt nếu uống trong vòng 1-2 giờ (nếu không có chống chỉ định)",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2, ECG",
                "Điều trị triệu chứng tiêu hóa:",
                "  - Chống nôn nếu cần",
                "  - Truyền dịch nếu mất nước",
                "  - Theo dõi điện giải",
                "Điều trị QT kéo dài/torsades de pointes nếu có:",
                "  - Theo dõi ECG liên tục",
                "  - Đảm bảo kali, magie bình thường",
                "  - Điều trị torsades de pointes: Magnesium sulfate IV, pacing nếu cần",
                "  - Tránh các thuốc kéo dài QT khác",
                "Điều trị rối loạn thính giác nếu có:",
                "  - Ngừng ngay clarithromycin",
                "  - Điều trị hỗ trợ",
                "  - Có thể không hồi phục",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2, ECG"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, ECG (QT interval), điện giải (kali, magie), dấu hiệu thính giác trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có biến chứng (QT kéo dài, torsades de pointes, rối loạn thính giác)."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn để giảm kích ứng dạ dày, giảm buồn nôn, nôn. Có thể uống không thức ăn nếu cần nhưng không khuyến nghị.",
                "timing": "Uống 2 lần/ngày (q12h), thường 250-500mg x 2 lần/ngày. Uống đều đặn, cách đều nhau trong ngày (12 giờ). Không bỏ liều."
            },
            "iv": {
                "reconstitution": "Pha theo hướng dẫn nhà sản xuất. Thường pha với nước cất vô trùng hoặc NaCl 0.9%. Lắc kỹ để hòa tan hoàn toàn.",
                "infusion_rate": "Truyền IV trong 60 phút (không truyền nhanh hơn). Có thể truyền trong 30 phút nếu cần nhưng không khuyến nghị.",
                "compatibility": [
                    "NaCl 0.9%",
                    "D5W (Dextrose 5%)",
                    "Nước cất vô trùng"
                ],
                "incompatibility": [
                    "Không trộn với các thuốc khác trong cùng một bơm tiêm hoặc chai truyền",
                    "Lactated Ringer's (LR) - không tương thích",
                    "Các dung dịch có cation (Al3+, Mg2+) - có thể tạo phức hợp"
                ],
                "notes": "Truyền IV trong 60 phút. Không truyền nhanh hơn. Theo dõi phản ứng tại chỗ tiêm (viêm tĩnh mạch). Dùng ngay sau khi pha. Không bảo quản lâu sau khi pha."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Label: Klacid (clarithromycin)",
                "UpToDate: Clarithromycin drug information",
                "Lexicomp: Clarithromycin monograph",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
                "Sanford Guide to Antimicrobial Therapy"
            ],
            "last_updated": "2025-02-03",
            "evidence_level": "Level 1 - FDA approved, multiple clinical trials, extensive clinical experience"
        }
    },

    "Ciprofloxacin": {
        "group": "Antibiotic - Fluoroquinolone",
        "vietnamese_name": "Ciprofloxacin, Cipro",
        "administration": ["PO", "IV"],
        "indications": [
            "Nhiễm khuẩn đường tiết niệu",
            "Nhiễm khuẩn đường tiêu hóa",
            "Nhiễm khuẩn da mô mềm",
            "Nhiễm khuẩn xương khớp",
            "Viêm phổi (một số loại)"
        ],
        "contraindications": [
            "Dị ứng fluoroquinolone",
            "Có thai",
            "Trẻ em <18 tuổi (trừ trường hợp đặc biệt)",
            "QT kéo dài"
        ],
        "dosage": {
            "adult_uti": "250-500mg PO x 2 lần/ngày",
            "adult_uti_complicated": "500-750mg PO x 2 lần/ngày",
            "adult_iv": "200-400mg IV mỗi 12 giờ",
            "adult_severe": "400mg IV mỗi 8 giờ",
            "notes": "Uống cách xa antacid 2 giờ. Không dùng với sữa"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "under_30": "Giảm liều 50-75%"
        },
        "side_effects": [
            "Rối loạn tiêu hóa",
            "Đau gân, viêm gân (có thể đứt gân)",
            "QT kéo dài",
            "Co giật (hiếm)",
            "Nhạy cảm ánh sáng",
            "Rối loạn tâm thần (hiếm)"
        ],
        "interactions": [
            "Antacid: giảm hấp thu",
            "Warfarin: tăng INR",
            "Theophylline: tăng nồng độ theophylline",
            "Probenecid: tăng nồng độ ciprofloxacin"
        ],
        "pregnancy": "C - Tránh dùng",
        "mechanism_of_action": "Ciprofloxacin là fluoroquinolone kháng sinh phổ rộng thuộc thế hệ thứ hai. Ức chế DNA gyrase (topoisomerase II) ở vi khuẩn Gram-âm và topoisomerase IV ở vi khuẩn Gram-dương, các enzyme cần thiết cho quá trình sao chép, phiên mã, sửa chữa, và tái tổ hợp DNA. Dẫn đến tổn thương DNA không thể sửa chữa và chết tế bào vi khuẩn. Phổ kháng khuẩn: Gram-âm mạnh (Enterobacteriaceae, Pseudomonas aeruginosa, H. influenzae, Neisseria, Moraxella), một số Gram-dương (không phải MRSA), và một số vi khuẩn không điển hình (Legionella, Mycoplasma, Chlamydia). Kháng thuốc phát triển nhanh nếu dùng không đúng hoặc không đủ liều.",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng) để đánh giá đáp ứng điều trị",
            "Cấy máu và cấy từ vị trí nhiễm trùng (nếu có) để xác định vi khuẩn và độ nhạy cảm",
            "Tendon (gân) - đau, sưng, đứt gân (đặc biệt gân Achilles) - có thể xảy ra bất cứ lúc nào, kể cả sau khi ngừng thuốc",
            "Thần kinh trung ương (co giật, kích động, mất ngủ, lo âu, trầm cảm, rối loạn tâm thần)",
            "Tim mạch (ECG - QT kéo dài, rối loạn nhịp tim) - đặc biệt ở bệnh nhân có nguy cơ",
            "Đường huyết (tăng hoặc hạ đường huyết - đặc biệt với sulfonylurea)",
            "Chức năng thận (creatinine, BUN) - điều chỉnh liều ở suy thận",
            "Chức năng gan (ALT, AST) - hiếm viêm gan nặng"
        ],
        "precautions": [
            "Nguy cơ đứt gân, viêm gân (đặc biệt gân Achilles) - có thể xảy ra bất cứ lúc nào, kể cả sau khi ngừng thuốc",
            "Nguy cơ tăng ở: > 60 tuổi, dùng corticosteroid, ghép thận, ghép tim, ghép phổi, hoạt động thể lực",
            "NGỪNG NGAY nếu có đau, sưng gân - nghỉ ngơi, không vận động",
            "QT kéo dài → không dùng với các thuốc kéo dài QT khác (amiodarone, sotalol, antipsychotics), bệnh nhân có tiền sử rối loạn nhịp",
            "Co giật → không dùng ở bệnh nhân có tiền sử co giật, tránh dùng với NSAID (tăng nguy cơ)",
            "Tăng độ nhạy cảm với ánh sáng → tránh ánh nắng trực tiếp, dùng kem chống nắng, mặc quần áo che",
            "Tương tác với nhiều thuốc: giảm hấp thu với antacid, sucralfate, sắt, kẽm, canxi (cách ít nhất 2 giờ)",
            "Hạ đường huyết → thận trọng với sulfonylurea (glibenclamide, gliclazide)",
            "Không dùng cho trẻ em < 18 tuổi (trừ trường hợp đặc biệt như nhiễm trùng nặng không có lựa chọn khác) - nguy cơ tổn thương sụn, viêm khớp",
            "Tránh dùng với sữa, sản phẩm sữa (giảm hấp thu)",
            "Uống nhiều nước để tránh kết tinh trong nước tiểu",
            "Không dùng trong thai kỳ (nguy cơ tổn thương sụn thai nhi)"
        ],
        "pharmacokinetics": {
            "half_life": "4 giờ (bình thường), 5-7 giờ (suy thận nặng)",
            "onset": "1-2 giờ (PO), ngay lập tức (IV)",
            "duration": "q12h (PO/IV), q8h cho Pseudomonas hoặc nhiễm trùng nặng",
            "protein_binding": "20-40%",
            "clearance": "Chủ yếu qua thận (40-60% bài tiết nguyên dạng), một phần qua gan (CYP1A2). Cần điều chỉnh liều ở suy thận (CrCl <30)."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín, tránh ẩm. IV: bảo quản trong tủ lạnh (2-8°C), để nhiệt độ phòng trước khi pha. Dung dịch đã pha: bảo quản ở nhiệt độ phòng, dùng trong vòng 24 giờ.",
        "black_box_warnings": "Tăng nguy cơ viêm gân và đứt gân ở mọi lứa tuổi. Nguy cơ tăng ở bệnh nhân > 60 tuổi, dùng corticosteroid, ghép cơ quan. Nguy cơ tổn thương thần kinh ngoại biên không hồi phục. Nguy cơ tác dụng phụ nghiêm trọng về gân, cơ, khớp, và thần kinh có thể xảy ra cùng lúc. Nguy cơ làm nặng bệnh nhược cơ. Tăng nguy cơ rối loạn tâm thần và hành vi tự sát. Chỉ dùng khi không có lựa chọn khác.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Antacids (Aluminum, Magnesium), Sucralfate, Sắt, Kẽm, Canxi",
                    "mechanism": "Cation (Al3+, Mg2+, Fe2+, Zn2+, Ca2+) tạo phức hợp không hòa tan với ciprofloxacin, giảm hấp thu.",
                    "effect": "Giảm hấp thu ciprofloxacin, giảm nồng độ trong máu, giảm hiệu quả điều trị",
                    "management": "Cách ít nhất 2 giờ (tốt nhất 4 giờ) trước hoặc sau khi uống ciprofloxacin. Không uống cùng lúc."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Ciprofloxacin ức chế CYP2C9, làm giảm chuyển hóa warfarin, tăng nồng độ warfarin.",
                    "effect": "Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu nghiêm trọng",
                    "management": "Theo dõi INR chặt chẽ khi bắt đầu, thay đổi liều, hoặc ngừng ciprofloxacin. Giảm liều warfarin khi bắt đầu ciprofloxacin. Điều chỉnh liều warfarin theo INR."
                },
                {
                    "drug": "Theophylline",
                    "mechanism": "Ciprofloxacin ức chế CYP1A2, làm giảm chuyển hóa theophylline, tăng nồng độ theophylline.",
                    "effect": "Tăng nồng độ theophylline, tăng độc tính theophylline (buồn nôn, nôn, co giật, rối loạn nhịp tim)",
                    "management": "Giảm liều theophylline 25-50% khi bắt đầu ciprofloxacin. Theo dõi nồng độ theophylline. Theo dõi dấu hiệu độc tính."
                }
            ],
            "moderate": [
                {
                    "drug": "Probenecid",
                    "mechanism": "Probenecid ức chế bài tiết ống thận của ciprofloxacin, tăng nồng độ.",
                    "effect": "Tăng nồng độ ciprofloxacin, tăng tác dụng phụ",
                    "management": "Theo dõi tác dụng phụ. Có thể cần giảm liều ciprofloxacin."
                },
                {
                    "drug": "NSAID (Ibuprofen, Naproxen)",
                    "mechanism": "Cả hai đều có thể gây co giật, tác dụng cộng dồn.",
                    "effect": "Tăng nguy cơ co giật",
                    "management": "Tránh dùng đồng thời nếu có thể. Thận trọng ở bệnh nhân có tiền sử co giật."
                },
                {
                    "drug": "Corticosteroid",
                    "mechanism": "Cả hai đều tăng nguy cơ đứt gân, tác dụng cộng dồn.",
                    "effect": "Tăng nguy cơ viêm gân, đứt gân",
                    "management": "TRÁNH DÙNG đồng thời nếu có thể. Nếu bắt buộc, theo dõi chặt chẽ dấu hiệu đau, sưng gân. Ngừng ngay nếu có đau gân."
                }
            ],
            "minor": [
                {
                    "drug": "Sulfonylurea (Glibenclamide, Gliclazide)",
                    "mechanism": "Ciprofloxacin có thể gây hạ đường huyết.",
                    "effect": "Tăng nguy cơ hạ đường huyết",
                    "management": "Theo dõi đường huyết. Điều chỉnh liều sulfonylurea nếu cần."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng ciprofloxacin hoặc các fluoroquinolone khác",
                "Có thai - chống chỉ định tuyệt đối, nguy cơ tổn thương sụn thai nhi",
                "Trẻ em < 18 tuổi (trừ trường hợp đặc biệt như nhiễm trùng nặng không có lựa chọn khác) - nguy cơ tổn thương sụn, viêm khớp",
                "QT kéo dài hoặc rối loạn nhịp tim nặng - tăng nguy cơ loạn nhịp tim nghiêm trọng",
                "Bệnh nhược cơ nặng - có thể làm nặng bệnh"
            ],
            "tương_đối": [
                "Bệnh nhân > 60 tuổi - tăng nguy cơ đứt gân, viêm gân",
                "Dùng corticosteroid - tăng nguy cơ đứt gân",
                "Ghép cơ quan - tăng nguy cơ đứt gân",
                "Tiền sử co giật - tăng nguy cơ co giật",
                "Suy thận nặng (CrCl <30) - giảm liều đáng kể",
                "Suy gan - thận trọng, có thể giảm chuyển hóa",
                "Dùng với warfarin - tăng nguy cơ chảy máu",
                "Dùng với theophylline - tăng độc tính theophylline",
                "Hoạt động thể lực nặng - tăng nguy cơ đứt gân"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Ciprofloxacin là thuốc phân loại C. Các nghiên cứu trên động vật cho thấy có thể gây tổn thương sụn ở khớp ở thai nhi. Có báo cáo về tổn thương sụn ở trẻ em khi dùng trong thai kỳ. CHỐNG CHỈ ĐỊNH trong thai kỳ trừ khi lợi ích vượt quá nguy cơ rõ ràng và không có lựa chọn khác. Nhiễm trùng nặng có thể gây nguy hiểm cho thai nhi, nhưng nên dùng kháng sinh khác nếu có thể.",
            "lactation": {
                "safety": "Compatible (với thận trọng)",
                "details": "Ciprofloxacin bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ. Tuy nhiên, fluoroquinolone có thể gây tổn thương sụn ở trẻ sơ sinh.",
                "recommendation": "Có thể dùng khi cho con bú với thận trọng. Dùng liều thấp nhất hiệu quả. Theo dõi trẻ sơ sinh. Tránh dùng nếu có lựa chọn khác."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Ciprofloxacin chuyển hóa một phần qua gan nhưng không phụ thuộc nhiều vào chức năng gan.",
            "moderate": "Không cần điều chỉnh liều. Thận trọng nếu có suy thận kèm theo.",
            "severe": "Thận trọng, có thể cần giảm liều nhẹ. Chuyển hóa có thể giảm ở suy gan nặng, nhưng thải trừ chủ yếu qua thận nên ít ảnh hưởng.",
            "notes": "Ciprofloxacin chuyển hóa một phần qua gan (CYP1A2), thải trừ chủ yếu qua thận (40-60% nguyên dạng). Suy gan có thể giảm chuyển hóa nhẹ nhưng không đáng kể. Tuy nhiên, suy gan có thể kèm theo suy thận, nên cần điều chỉnh liều theo chức năng thận."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng tiêu hóa: Buồn nôn, nôn, tiêu chảy, đau bụng",
                "Triệu chứng thần kinh: Co giật, kích động, lo âu, mất ngủ, trầm cảm, rối loạn tâm thần, hành vi tự sát",
                "Triệu chứng gân: Đau gân, viêm gân, đứt gân (đặc biệt gân Achilles)",
                "Triệu chứng tim mạch: QT kéo dài, rối loạn nhịp tim, có thể gây tử vong",
                "Triệu chứng chuyển hóa: Hạ hoặc tăng đường huyết",
                "Triệu chứng nghiêm trọng: Tổn thương thần kinh ngoại biên không hồi phục, rối loạn nhịp tim nghiêm trọng, đứt gân"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.",
            "treatment": [
                "Ngừng ngay ciprofloxacin",
                "Rửa dạ dày hoặc than hoạt nếu uống trong vòng 1-2 giờ (nếu không có chống chỉ định)",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2, ECG",
                "Điều trị co giật nếu có:",
                "  - Benzodiazepine (diazepam, lorazepam)",
                "  - Theo dõi thần kinh chặt chẽ",
                "Điều trị rối loạn nhịp tim nếu có:",
                "  - Theo dõi ECG liên tục",
                "  - Điều trị loạn nhịp nếu cần",
                "Điều trị đau gân nếu có:",
                "  - Ngừng ngay ciprofloxacin",
                "  - Nghỉ ngơi, không vận động",
                "  - Chườm lạnh",
                "  - Thuốc giảm đau nếu cần",
                "Điều trị hạ đường huyết nếu có:",
                "  - Truyền glucose",
                "  - Theo dõi đường huyết",
                "Điều trị triệu chứng tiêu hóa:",
                "  - Chống nôn nếu cần",
                "  - Truyền dịch nếu mất nước",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, ECG, dấu hiệu thần kinh, dấu hiệu gân, đường huyết trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có biến chứng (loạn nhịp, co giật, đứt gân)."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Uống với nước đầy đủ (ít nhất 1-2 ly nước) để tránh kết tinh trong nước tiểu. KHÔNG uống với sữa hoặc sản phẩm sữa (giảm hấp thu).",
                "timing": "Uống 2 lần/ngày (q12h), cách đều 12 giờ. Cách ít nhất 2 giờ (tốt nhất 4 giờ) trước hoặc sau khi uống antacid, sucralfate, sắt, kẽm, canxi. Không uống cùng lúc với các cation này."
            },
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W. Nồng độ pha: 1-2mg/ml (tối đa). Pha 200mg trong 100ml dịch = 2mg/ml. Pha 400mg trong 200ml dịch = 2mg/ml.",
                "infusion_rate": "Truyền trong 60 phút (ít nhất 60 phút). Không truyền quá nhanh. Tốc độ: 100ml/60 phút = ~1.7ml/phút. 200ml/60 phút = ~3.3ml/phút.",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
                "incompatibility": ["Không trộn với các thuốc khác trong cùng một ống truyền. Kiểm tra tương thích trước khi pha. Tránh pha với cation (Al3+, Mg2+, Ca2+)."],
                "notes": "Theo dõi chức năng thận, dấu hiệu gân, thần kinh trong quá trình truyền. Có thể gây kích ứng tĩnh mạch - thay đổi vị trí tiêm nếu cần. Liều: 200-400mg mỗi 12 giờ (q12h), hoặc 400mg mỗi 8 giờ (q8h) cho Pseudomonas hoặc nhiễm trùng nặng."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Ciprofloxacin (Cipro)",
                "UpToDate - Ciprofloxacin: Drug Information",
                "Medscape - Ciprofloxacin Drug Reference",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
                "Lexicomp Online - Ciprofloxacin Monograph",
                "Micromedex - Ciprofloxacin Drug Information",
                "IDSA Guidelines - Antimicrobial Therapy"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },

    "Doxycycline": {
        "group": "Infectious Disease - Tetracycline Antibiotic",
        "vietnamese_name": "Doxycycline, Vibramycin",
        "administration": ["PO", "IV"],
        "indications": [
            "Nhiễm trùng đường hô hấp",
            "Nhiễm trùng da (mụn trứng cá)",
            "Chlamydia",
            "Lyme disease",
            "Sốt rét phòng ngừa",
            "Rickettsia",
            "Mycoplasma"
        ],
        "contraindications": [
            "Dị ứng doxycycline/tetracycline",
            "Có thai (3 tháng cuối)",
            "Trẻ em <8 tuổi (gây vàng răng)"
        ],
        "dosage": {
            "adult_respiratory": "100mg x 2 lần/ngày x 7-14 ngày",
            "adult_chlamydia": "100mg x 2 lần/ngày x 7 ngày",
            "adult_acne": "50-100mg x 1-2 lần/ngày",
            "adult_malaria_prophylaxis": "100mg x 1 lần/ngày",
            "notes": "Uống với nhiều nước, tránh nằm ngay sau khi uống. Tránh nắng"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Buồn nôn, nôn",
            "Loét thực quản (nếu không uống đủ nước)",
            "Phản ứng quang hóa (nhạy cảm ánh sáng)",
            "Vàng răng (trẻ em, có thai)",
            "Tăng áp lực nội sọ (hiếm)",
            "Độc gan (liều cao)"
        ],
        "interactions": [
            "Antacid/Sắt/Calcium: giảm hấp thu - cách 2 giờ",
            "Warfarin: tăng tác dụng chống đông",
            "Digoxin: tăng nồng độ digoxin",
            "Phenytoin/Carbamazepine: giảm nồng độ doxycycline"
        ],
        "pregnancy": "D - Chống chỉ định trong 3 tháng cuối",
        "mechanism_of_action": "Tetracycline kháng sinh phổ rộng. Ức chế tổng hợp protein vi khuẩn bằng cách gắn với tiểu phần 30S của ribosome, ngăn cản gắn aminoacyl-tRNA. Phổ kháng khuẩn: Gram-dương, Gram-âm, vi khuẩn không điển hình (Chlamydia, Mycoplasma, Rickettsia, Borrelia), và một số ký sinh trùng (Plasmodium). Không hiệu quả với Pseudomonas hoặc Proteus. Đặc biệt hiệu quả với vi khuẩn không điển hình và được dùng trong nhiễm trùng đường hô hấp, Lyme disease, và sốt rét.",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, WBC)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Dạ dày-ruột (buồn nôn, nôn, tiêu chảy, viêm thực quản)",
            "Da (tăng độ nhạy cảm với ánh sáng, phát ban)",
            "Răng và xương (ở trẻ em < 8 tuổi: ố vàng răng vĩnh viễn, chậm phát triển xương)",
            "Chức năng gan (ALT, AST) - hiếm viêm gan, tăng áp lực nội sọ giả (ở phụ nữ)",
            "Thận (không tích lũy ở suy thận, nhưng theo dõi)"
        ],
        "precautions": [
            "KHÔNG dùng cho trẻ em < 8 tuổi (trừ trường hợp đe dọa tính mạng) - gây ố vàng răng vĩnh viễn, chậm phát triển xương",
            "Tăng độ nhạy cảm với ánh sáng → tránh ánh nắng trực tiếp, dùng kem chống nắng, mặc quần áo che phủ",
            "Uống với nhiều nước (ít nhất 200ml) và ở tư thế đứng để tránh viêm thực quản (đau khi nuốt, khó nuốt)",
            "KHÔNG uống nằm ngửa hoặc trước khi ngủ",
            "Tương tác với nhiều thuốc và thực phẩm: giảm hấp thu với antacid, sắt, canxi, magie, kẽm, sữa (cách 2 giờ)",
            "Tương tác với warfarin → tăng nguy cơ chảy máu (theo dõi INR)",
            "Tương tác với thuốc tránh thai → giảm hiệu quả (dùng biện pháp tránh thai khác)",
            "Tăng áp lực nội sọ giả (đau đầu, nhìn mờ, phù gai thị) - đặc biệt ở phụ nữ, ngừng nếu có",
            "Không dùng trong 3 tháng cuối thai kỳ (nguy cơ ố vàng răng, chậm phát triển xương ở trẻ)",
            "Uống với thức ăn để giảm kích ứng dạ dày (nhưng giảm hấp thu một phần)"
        ],
        "pharmacokinetics": {
            "half_life": "18-22 giờ (dài)",
            "onset": "1-2 giờ (PO), ngay lập tức (IV)",
            "duration": "q12h hoặc q24h (PO/IV)",
            "protein_binding": "80-90%",
            "metabolism": "Gan (một phần), bài tiết một phần nguyên dạng",
            "clearance": "Gan và thận, KHÔNG tích lũy ở suy thận (khác với tetracycline cũ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng. Viên nang: tránh ẩm. Bảo quản tốt hơn các tetracycline cũ (ít bị hỏng).",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, ố vàng răng vĩnh viễn ở trẻ em < 8 tuổi là không hồi phục. Tăng áp lực nội sọ giả có thể gây mù. Viêm thực quản có thể nghiêm trọng.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Antacid, Sắt, Calcium, Magnesium, Kẽm, Bismuth",
                    "mechanism": "Các cation hóa trị 2+ (Ca²⁺, Mg²⁺, Fe²⁺, Zn²⁺) tạo phức hợp không hòa tan với doxycycline, làm giảm hấp thu doxycycline.",
                    "effect": "Giảm hấp thu doxycycline đáng kể (50-90%), giảm hiệu quả kháng khuẩn",
                    "management": "Cách ít nhất 2 giờ giữa doxycycline và các thuốc/thực phẩm chứa cation (antacid, sắt, canxi, magie, kẽm, sữa, bismuth). Uống doxycycline trước bữa ăn hoặc 2 giờ sau bữa ăn nếu bữa ăn chứa nhiều sữa hoặc thực phẩm giàu canxi."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Doxycycline có thể ức chế tổng hợp vitamin K phụ thuộc vào hệ vi khuẩn đường ruột, làm giảm sản xuất các yếu tố đông máu phụ thuộc vitamin K. Ngoài ra, có thể đẩy warfarin khỏi albumin (protein binding cao).",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên (ít nhất 2-3 lần/tuần khi bắt đầu dùng doxycycline). Có thể cần giảm liều warfarin. Đặc biệt thận trọng ở bệnh nhân dùng kéo dài (>7 ngày)."
                }
            ],
            "moderate": [
                {
                    "drug": "Digoxin",
                    "mechanism": "Doxycycline có thể làm tăng hấp thu digoxin bằng cách thay đổi hệ vi khuẩn đường ruột, làm tăng nồng độ digoxin.",
                    "effect": "Tăng nồng độ digoxin, tăng nguy cơ độc tính digoxin (buồn nôn, rối loạn nhịp tim)",
                    "management": "Theo dõi nồng độ digoxin. Có thể cần giảm liều digoxin. Theo dõi dấu hiệu độc tính digoxin."
                },
                {
                    "drug": "Phenytoin, Carbamazepine",
                    "mechanism": "Phenytoin và carbamazepine cảm ứng enzyme chuyển hóa doxycycline, làm giảm nồng độ doxycycline.",
                    "effect": "Giảm nồng độ doxycycline, giảm hiệu quả kháng khuẩn",
                    "management": "Có thể cần tăng liều doxycycline. Theo dõi đáp ứng điều trị."
                },
                {
                    "drug": "Thuốc tránh thai đường uống",
                    "mechanism": "Kháng sinh phổ rộng có thể làm giảm hệ vi khuẩn đường ruột, làm giảm tái hấp thu estrogen từ đường ruột. Ngoài ra, doxycycline có thể cảm ứng enzyme chuyển hóa estrogen.",
                    "effect": "Giảm hiệu quả thuốc tránh thai (hiếm, nhưng có thể xảy ra)",
                    "management": "Khuyến cáo sử dụng biện pháp tránh thai bổ sung (bao cao su) trong khi dùng kháng sinh và 7 ngày sau khi ngừng."
                }
            ],
            "minor": [
                {
                    "drug": "Penicillin",
                    "mechanism": "Doxycycline có thể đối kháng với penicillin trong một số trường hợp (ức chế tổng hợp protein vs ức chế tổng hợp thành tế bào).",
                    "effect": "Giảm hiệu quả kháng khuẩn của penicillin (hiếm)",
                    "management": "Tránh dùng đồng thời nếu có thể. Chọn một trong hai thuốc tùy theo chỉ định."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng doxycycline hoặc tetracycline",
                "Có thai (3 tháng cuối) - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI (nguy cơ ố vàng răng, chậm phát triển xương ở trẻ)",
                "Trẻ em < 8 tuổi - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI (trừ trường hợp đe dọa tính mạng như sốt rét, rickettsia) - nguy cơ ố vàng răng vĩnh viễn, chậm phát triển xương"
            ],
            "tương_đối": [
                "Có thai (3 tháng đầu và giữa) - nguy cơ ố vàng răng, chậm phát triển xương ở trẻ, chỉ dùng khi thực sự cần thiết",
                "Suy gan nặng - tăng nguy cơ độc gan",
                "Tăng áp lực nội sọ giả - có thể làm nặng thêm",
                "Bệnh nhân đang dùng warfarin - tăng nguy cơ chảy máu",
                "Bệnh nhân đang dùng digoxin - tăng nguy cơ độc tính digoxin",
                "Nhạy cảm với ánh sáng - tăng nguy cơ phản ứng quang hóa"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Doxycycline là thuốc phân loại D. Các nghiên cứu trên động vật và người cho thấy nguy cơ ố vàng răng vĩnh viễn và chậm phát triển xương ở trẻ khi dùng trong thai kỳ, đặc biệt trong tam cá nguyệt thứ hai và thứ ba. Chống chỉ định trong tam cá nguyệt thứ hai và thứ ba. Tránh dùng trong tam cá nguyệt đầu tiên nếu có thể. Chỉ dùng khi lợi ích vượt quá nguy cơ, đặc biệt trong các trường hợp đe dọa tính mạng như sốt rét, rickettsia.",
            "lactation": {
                "safety": "Compatible",
                "details": "Doxycycline bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ. Tuy nhiên, có thể gây ố vàng răng ở trẻ sơ sinh nếu dùng kéo dài.",
                "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng. Tránh dùng kéo dài. Theo dõi trẻ sơ sinh về dấu hiệu tiêu chảy, phát ban, hoặc các tác dụng phụ khác. Dùng liều thấp nhất hiệu quả."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Doxycycline chuyển hóa một phần qua gan, nhưng không tích lũy đáng kể ở suy gan nhẹ.",
            "moderate": "Thận trọng, có thể cần giảm liều. Theo dõi chức năng gan và dấu hiệu độc gan.",
            "severe": "Giảm liều 25-50% hoặc tăng khoảng cách giữa các liều. Theo dõi chức năng gan chặt chẽ. Có thể cần tránh dùng nếu suy gan rất nặng.",
            "notes": "Doxycycline chuyển hóa một phần qua gan, nhưng thải trừ chủ yếu qua gan và thận. Không tích lũy đáng kể ở suy gan nhẹ, nhưng có thể tích lũy ở suy gan nặng. Cần điều chỉnh liều ở suy gan nặng. Khác với tetracycline cũ, doxycycline không tích lũy ở suy thận."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng tiêu hóa: Buồn nôn, nôn, tiêu chảy, viêm thực quản (đau khi nuốt, khó nuốt)",
                "Triệu chứng gan: Tăng men gan, viêm gan (đặc biệt ở liều cao, suy gan)",
                "Triệu chứng thần kinh: Tăng áp lực nội sọ giả (đau đầu, nhìn mờ, phù gai thị) - đặc biệt ở phụ nữ, có thể gây mù",
                "Triệu chứng da: Phản ứng quang hóa nặng (phát ban, bỏng da khi tiếp xúc với ánh sáng)",
                "Triệu chứng chảy máu: Chảy máu kéo dài, tăng INR (khi dùng với warfarin)",
                "Triệu chứng dị ứng: Phát ban, phù mạch, sốc phản vệ (nếu dị ứng)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.",
            "treatment": [
                "Ngừng ngay doxycycline",
                "Điều trị viêm thực quản nếu có:",
                "  - Uống nhiều nước",
                "  - Tránh nằm ngửa",
                "  - Điều trị giảm đau nếu cần",
                "  - Có thể cần nội soi nếu nghiêm trọng",
                "Điều trị tăng áp lực nội sọ giả nếu có:",
                "  - Ngừng ngay doxycycline",
                "  - Điều trị bằng acetazolamide hoặc mannitol nếu cần",
                "  - Theo dõi thị lực và dấu hiệu thần kinh",
                "  - Có thể cần chọc dò tủy sống để giảm áp lực",
                "Điều trị phản ứng quang hóa nếu có:",
                "  - Tránh ánh nắng trực tiếp",
                "  - Dùng kem chống nắng",
                "  - Điều trị phát ban/bỏng da",
                "Điều trị chảy máu nếu có:",
                "  - Bổ sung vitamin K nếu giảm prothrombin",
                "  - Truyền huyết tương tươi đông lạnh (FFP) nếu chảy máu nặng",
                "  - Điều chỉnh liều warfarin nếu đang dùng",
                "Điều trị độc gan nếu có:",
                "  - Ngừng ngay doxycycline",
                "  - Điều trị hỗ trợ gan",
                "  - Theo dõi chức năng gan",
                "Điều trị dị ứng nếu có:",
                "  - Epinephrine nếu sốc phản vệ",
                "  - Antihistamine, corticosteroid",
                "  - Hỗ trợ hô hấp nếu cần",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2",
                "Lọc máu: Hemodialysis không hiệu quả do protein binding cao (80-90%)"
            ],
            "monitoring": "Theo dõi dấu hiệu tiêu hóa (buồn nôn, nôn, viêm thực quản), dấu hiệu tăng áp lực nội sọ giả (đau đầu, nhìn mờ, phù gai thị), dấu hiệu phản ứng quang hóa (phát ban, bỏng da), chức năng gan (ALT, AST), PT/INR (nếu dùng với warfarin), dấu hiệu chảy máu, dấu hiệu sinh tồn trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có tăng áp lực nội sọ giả hoặc độc gan."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Uống với thức ăn có thể giảm kích ứng dạ dày nhưng giảm hấp thu một phần. Tránh uống với sữa hoặc thực phẩm giàu canxi (giảm hấp thu đáng kể).",
                "timing": "Uống 1-2 lần/ngày tùy chỉ định (respiratory: 2 lần/ngày, chlamydia: 2 lần/ngày, acne: 1-2 lần/ngày, malaria prophylaxis: 1 lần/ngày). Cách đều trong ngày. Uống với nhiều nước (ít nhất 200ml) và ở tư thế đứng để tránh viêm thực quản. KHÔNG uống nằm ngửa hoặc trước khi ngủ. Cách ít nhất 2 giờ với antacid, sắt, canxi, magie, kẽm, sữa."
            },
            "iv": {
                "reconstitution": "Pha với NS (0.9% NaCl) hoặc D5W (5% Dextrose). Nồng độ pha: 0.1-1mg/ml. Pha 100mg trong 100ml = 1mg/ml. Pha 200mg trong 200ml = 1mg/ml. Lắc kỹ để hòa tan hoàn toàn. Bảo quản tránh ánh sáng.",
                "infusion_rate": "Truyền IV trong 1-4 giờ. Tốc độ: 100ml/1 giờ = ~1.7ml/phút, 200ml/4 giờ = ~0.83ml/phút. KHÔNG truyền nhanh (bolus) - tăng nguy cơ tác dụng phụ.",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
                "incompatibility": [
                    "Ringer's Lactate - có thể tạo kết tủa với canxi",
                    "Các dung dịch chứa canxi, magie, sắt - tạo kết tủa",
                    "Các thuốc có tính kiềm hoặc acid mạnh"
                ],
                "notes": "QUAN TRỌNG: 1) Uống với nhiều nước và ở tư thế đứng để tránh viêm thực quản, 2) Tránh ánh nắng trực tiếp, dùng kem chống nắng, 3) Cách ít nhất 2 giờ với antacid, sắt, canxi, magie, kẽm, sữa, 4) KHÔNG dùng cho trẻ em < 8 tuổi (trừ trường hợp đe dọa tính mạng), 5) KHÔNG dùng trong 3 tháng cuối thai kỳ, 6) Theo dõi dấu hiệu tăng áp lực nội sọ giả."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Doxycycline (Vibramycin)",
                "UpToDate - Doxycycline: Drug Information",
                "Medscape - Doxycycline Drug Reference",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
                "Lexicomp Online - Doxycycline Monograph",
                "Micromedex - Doxycycline Drug Information",
                "IDSA Guidelines - Community-Acquired Pneumonia, Tick-Borne Infections"
            ],
            "last_updated": "2025-02-03",
            "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },

    "Metronidazole": {
        "group": "Infectious Disease - Nitroimidazole Antibiotic",
        "vietnamese_name": "Metronidazole, Flagyl",
        "administration": ["PO", "IV"],
        "indications": [
            "Nhiễm khuẩn kỵ khí",
            "Giardia",
            "Trichomonas",
            "Amebiasis",
            "Bacterial vaginosis",
            "H. pylori (kết hợp)",
            "C. difficile colitis"
        ],
        "contraindications": [
            "Dị ứng metronidazole",
            "Có thai (3 tháng đầu)",
            "Dùng disulfiram trong 14 ngày"
        ],
        "dosage": {
            "adult_anaerobic": "500mg x 3 lần/ngày PO hoặc 500mg mỗi 6-8 giờ IV",
            "adult_giardia": "250mg x 3 lần/ngày x 7 ngày",
            "adult_trichomonas": "2g x 1 lần hoặc 500mg x 2 lần/ngày x 7 ngày",
            "adult_c_diff": "500mg x 3 lần/ngày x 10-14 ngày",
            "adult_h_pylori": "500mg x 2 lần/ngày (với amoxicillin + PPI)",
            "notes": "TRÁNH RƯỢU (phản ứng disulfiram-like). Uống với thức ăn"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Giảm liều 50%"
        },
        "side_effects": [
            "Vị kim loại trong miệng",
            "Buồn nôn, nôn",
            "Đau đầu",
            "Phản ứng với rượu (nôn, đỏ mặt, nhịp tim nhanh)",
            "Co giật (liều cao)",
            "Bệnh thần kinh ngoại biên (dùng lâu dài)",
            "Ban da"
        ],
        "interactions": [
            "Rượu: phản ứng disulfiram-like (nôn, đỏ mặt) - TRÁNH",
            "Warfarin: tăng tác dụng chống đông",
            "Lithium: tăng nồng độ lithium",
            "Phenytoin: tăng nồng độ phenytoin",
            "Disulfiram: chống chỉ định"
        ],
        "pregnancy": "B - D trong 3 tháng đầu",
        "mechanism_of_action": "Nitroimidazole kháng sinh/kháng ký sinh trùng. Sau khi vào tế bào vi khuẩn/ký sinh trùng, bị khử bởi ferredoxin (có trong vi khuẩn kỵ khí và ký sinh trùng) → tạo ra các gốc tự do độc hại phá hủy DNA. Chỉ hoạt động với vi khuẩn kỵ khí (Bacteroides, Clostridium, giardia) và ký sinh trùng (Trichomonas, Giardia, Entamoeba). KHÔNG hoạt động với vi khuẩn hiếu khí. Đặc biệt hiệu quả với kỵ khí và được dùng trong nhiễm trùng bụng, nhiễm trùng phụ khoa, và nhiễm C. difficile.",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, WBC)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Thần kinh (dị cảm, co giật, viêm dây thần kinh ngoại biên, chóng mặt, mất điều hòa)",
            "Dạ dày-ruột (buồn nôn, nôn, tiêu chảy, vị kim loại)",
            "Chức năng gan (ALT, AST) - hiếm viêm gan",
            "Số lượng bạch cầu (hiếm giảm bạch cầu)",
            "Phản ứng Disulfiram-like nếu uống rượu (buồn nôn, nôn, đỏ bừng, nhịp tim nhanh)"
        ],
        "precautions": [
            "TUYỆT ĐỐI KHÔNG uống rượu trong và ít nhất 3 ngày sau khi ngừng thuốc - gây phản ứng Disulfiram-like nặng (buồn nôn, nôn, đỏ bừng, nhịp tim nhanh, hạ huyết áp)",
            "Nguy cơ tổn thương thần kinh ngoại biên và trung ương (dị cảm, co giật, viêm dây thần kinh) - tăng ở dùng kéo dài, liều cao, suy gan",
            "Ngừng nếu có dấu hiệu tổn thương thần kinh",
            "Không dùng cho nhiễm trùng do vi khuẩn hiếu khí (không hiệu quả)",
            "Uống với thức ăn để giảm kích ứng dạ dày",
            "Vị kim loại rất thường gặp - không phải tác dụng phụ nghiêm trọng nhưng khó chịu",
            "Có thể làm nước tiểu sẫm màu (vô hại)",
            "Thận trọng ở suy gan (giảm chuyển hóa → tăng nguy cơ tác dụng phụ thần kinh)",
            "Không dùng trong 3 tháng đầu thai kỳ (nguy cơ dị tật) - chỉ dùng khi thực sự cần thiết",
            "Pha trong NS, D5W, hoặc LR, truyền IV trong 30-60 phút"
        ],
        "pharmacokinetics": {
            "half_life": "6-8 giờ (bình thường), 9-15 giờ (suy gan)",
            "onset": "1-2 giờ (PO), ngay lập tức (IV)",
            "duration": "q8h (PO/IV), q12h cho C. difficile (PO)",
            "protein_binding": "< 20%",
            "metabolism": "Gan (CYP450) - chuyển hóa mạnh",
            "clearance": "Chủ yếu qua gan (60-80%), cần điều chỉnh ở suy gan nặng"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ánh sáng. Viên nén: tránh ẩm. Dung dịch pha tiêm: sau khi pha, bảo quản ở nhiệt độ phòng 24 giờ, tránh ánh sáng.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, phản ứng Disulfiram-like với rượu có thể nặng. Tổn thương thần kinh có thể không hồi phục. Nguy cơ dị tật thai nhi nếu dùng trong 3 tháng đầu thai kỳ.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Rượu (Ethanol)",
                    "mechanism": "Metronidazole ức chế aldehyde dehydrogenase, enzyme chuyển hóa acetaldehyde (sản phẩm chuyển hóa của ethanol) thành acetate. Kết quả là tích lũy acetaldehyde, gây phản ứng Disulfiram-like.",
                    "effect": "Phản ứng Disulfiram-like nặng: buồn nôn, nôn, đỏ bừng mặt, nhịp tim nhanh, hạ huyết áp, khó thở, có thể đe dọa tính mạng",
                    "management": "TUYỆT ĐỐI KHÔNG uống rượu trong và ít nhất 3 ngày sau khi ngừng metronidazole. Tránh tất cả các sản phẩm chứa rượu (thuốc ho, nước súc miệng, thực phẩm có rượu). Nếu uống rượu, ngừng ngay metronidazole và điều trị hỗ trợ."
                },
                {
                    "drug": "Disulfiram",
                    "mechanism": "Cả hai đều ức chế aldehyde dehydrogenase, tác dụng cộng dồn làm tăng nguy cơ phản ứng Disulfiram-like và tổn thương thần kinh.",
                    "effect": "Tăng nguy cơ phản ứng Disulfiram-like nặng, tăng nguy cơ tổn thương thần kinh",
                    "management": "CHỐNG CHỈ ĐỊNH: Không dùng metronidazole trong vòng 14 ngày sau khi ngừng disulfiram. Nếu đang dùng disulfiram, không dùng metronidazole."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Metronidazole ức chế chuyển hóa warfarin qua CYP2C9, làm tăng nồng độ warfarin và tăng tác dụng chống đông.",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu nghiêm trọng",
                    "management": "Theo dõi INR thường xuyên (ít nhất 2-3 lần/tuần khi bắt đầu dùng metronidazole). Giảm liều warfarin 30-50%. Đặc biệt thận trọng ở bệnh nhân suy gan, dùng kéo dài (>7 ngày)."
                }
            ],
            "moderate": [
                {
                    "drug": "Lithium",
                    "mechanism": "Metronidazole có thể làm giảm thải trừ lithium, làm tăng nồng độ lithium trong máu.",
                    "effect": "Tăng nồng độ lithium, tăng nguy cơ độc tính lithium (buồn nôn, run, lú lẫn, suy thận)",
                    "management": "Theo dõi nồng độ lithium thường xuyên. Có thể cần giảm liều lithium. Theo dõi dấu hiệu độc tính lithium."
                },
                {
                    "drug": "Phenytoin",
                    "mechanism": "Metronidazole ức chế chuyển hóa phenytoin qua CYP2C9, làm tăng nồng độ phenytoin.",
                    "effect": "Tăng nồng độ phenytoin, tăng nguy cơ độc tính (chóng mặt, rung giật nhãn cầu, lú lẫn, co giật)",
                    "management": "Theo dõi nồng độ phenytoin. Có thể cần giảm liều phenytoin. Theo dõi dấu hiệu độc tính phenytoin."
                },
                {
                    "drug": "Phenobarbital",
                    "mechanism": "Phenobarbital có thể cảm ứng enzyme chuyển hóa metronidazole, làm giảm nồng độ metronidazole.",
                    "effect": "Giảm nồng độ metronidazole, giảm hiệu quả kháng khuẩn",
                    "management": "Có thể cần tăng liều metronidazole. Theo dõi đáp ứng điều trị."
                }
            ],
            "minor": [
                {
                    "drug": "Cimetidine",
                    "mechanism": "Cimetidine có thể ức chế chuyển hóa metronidazole, làm tăng nhẹ nồng độ metronidazole.",
                    "effect": "Tăng nhẹ nồng độ metronidazole",
                    "management": "Theo dõi dấu hiệu tác dụng phụ. Thường không cần điều chỉnh liều."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng metronidazole hoặc nitroimidazole",
                "Đang dùng disulfiram hoặc đã dùng disulfiram trong vòng 14 ngày - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI"
            ],
            "tương_đối": [
                "Có thai (3 tháng đầu) - nguy cơ dị tật thai nhi, chỉ dùng khi thực sự cần thiết",
                "Suy gan nặng - giảm chuyển hóa, tăng nguy cơ tác dụng phụ thần kinh",
                "Bệnh thần kinh ngoại biên - tăng nguy cơ tổn thương thần kinh",
                "Bệnh nhân đang dùng warfarin - tăng nguy cơ chảy máu",
                "Bệnh nhân đang dùng lithium - tăng nguy cơ độc tính lithium",
                "Nhiễm trùng do vi khuẩn hiếu khí - không hiệu quả"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B (D trong 3 tháng đầu)",
            "pregnancy_details": "Metronidazole là thuốc phân loại B trong tam cá nguyệt thứ hai và thứ ba, nhưng phân loại D trong tam cá nguyệt đầu tiên. Các nghiên cứu trên động vật cho thấy nguy cơ dị tật bẩm sinh khi dùng trong tam cá nguyệt đầu tiên. Các nghiên cứu trên người cho thấy nguy cơ dị tật tăng nhẹ khi dùng trong tam cá nguyệt đầu tiên. Tránh dùng trong tam cá nguyệt đầu tiên nếu có thể. Nếu cần thiết, chỉ dùng khi lợi ích vượt quá nguy cơ. Có thể dùng trong tam cá nguyệt thứ hai và thứ ba khi cần thiết.",
            "lactation": {
                "safety": "Compatible",
                "details": "Metronidazole bài tiết vào sữa mẹ ở nồng độ tương đương nồng độ trong máu mẹ. Nồng độ trong sữa mẹ cao và có thể gây vị đắng cho trẻ sơ sinh. Tuy nhiên, không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ khi dùng liều thông thường.",
                "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng. Có thể gây vị đắng cho trẻ sơ sinh. Theo dõi trẻ sơ sinh về dấu hiệu tiêu chảy, phát ban, hoặc các tác dụng phụ khác. Dùng liều thấp nhất hiệu quả. Có thể cân nhắc ngừng cho con bú trong thời gian ngắn nếu dùng liều cao."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Metronidazole chuyển hóa qua gan (CYP450), nhưng không tích lũy đáng kể ở suy gan nhẹ.",
            "moderate": "Thận trọng, có thể cần giảm liều 25-50%. Theo dõi chức năng gan và dấu hiệu tác dụng phụ thần kinh.",
            "severe": "Giảm liều 50% hoặc tăng khoảng cách giữa các liều (q12h thay vì q8h). Theo dõi chức năng gan chặt chẽ. Theo dõi dấu hiệu tác dụng phụ thần kinh (dị cảm, co giật). Có thể cần tránh dùng nếu suy gan rất nặng.",
            "notes": "Metronidazole chuyển hóa mạnh qua gan (CYP450), thải trừ chủ yếu qua gan (60-80%). Half-life tăng từ 6-8 giờ (bình thường) lên 9-15 giờ (suy gan). Tích lũy ở suy gan nặng, làm tăng nguy cơ tác dụng phụ thần kinh. Cần điều chỉnh liều ở suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng thần kinh: Co giật, rối loạn ý thức, dị cảm, viêm dây thần kinh ngoại biên, chóng mặt, mất điều hòa (đặc biệt ở suy gan, liều cao)",
                "Triệu chứng tiêu hóa: Buồn nôn, nôn, tiêu chảy, vị kim loại",
                "Triệu chứng Disulfiram-like: Buồn nôn, nôn, đỏ bừng mặt, nhịp tim nhanh, hạ huyết áp, khó thở (nếu uống rượu)",
                "Triệu chứng chảy máu: Chảy máu kéo dài, tăng INR (khi dùng với warfarin)",
                "Triệu chứng gan: Tăng men gan, viêm gan (hiếm)",
                "Triệu chứng dị ứng: Phát ban, phù mạch, sốc phản vệ (nếu dị ứng)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.",
            "treatment": [
                "Ngừng ngay metronidazole",
                "Điều trị co giật nếu có: Benzodiazepine (diazepam, lorazepam), phenobarbital",
                "Điều trị phản ứng Disulfiram-like nếu có (nếu uống rượu):",
                "  - Ngừng ngay metronidazole",
                "  - Bù dịch đầy đủ",
                "  - Hỗ trợ hô hấp nếu cần",
                "  - Điều trị hạ huyết áp nếu cần",
                "  - Theo dõi dấu hiệu sinh tồn",
                "Điều trị tổn thương thần kinh ngoại biên:",
                "  - Ngừng ngay metronidazole",
                "  - Điều trị hỗ trợ (vật lý trị liệu)",
                "  - Tổn thương có thể không hồi phục hoàn toàn",
                "Điều trị chảy máu nếu có:",
                "  - Bổ sung vitamin K nếu giảm prothrombin",
                "  - Truyền huyết tương tươi đông lạnh (FFP) nếu chảy máu nặng",
                "  - Điều chỉnh liều warfarin nếu đang dùng",
                "Điều trị dị ứng nếu có:",
                "  - Epinephrine nếu sốc phản vệ",
                "  - Antihistamine, corticosteroid",
                "  - Hỗ trợ hô hấp nếu cần",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2",
                "Lọc máu: Hemodialysis có thể loại bỏ metronidazole một phần (protein binding <20%), nhưng không hiệu quả lắm do chuyển hóa chủ yếu qua gan."
            ],
            "monitoring": "Theo dõi dấu hiệu thần kinh (co giật, ý thức, dị cảm, viêm dây thần kinh), dấu hiệu Disulfiram-like (nếu uống rượu), PT/INR (nếu dùng với warfarin), chức năng gan (ALT, AST), dấu hiệu chảy máu, dấu hiệu sinh tồn trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có tổn thương thần kinh hoặc suy gan."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Nên uống với thức ăn để giảm kích ứng dạ dày và vị kim loại. Uống với thức ăn không ảnh hưởng đáng kể đến hấp thu.",
                "timing": "Uống 2-3 lần/ngày tùy chỉ định (anaerobic: 3 lần/ngày, C. difficile: 3 lần/ngày, H. pylori: 2 lần/ngày). Cách đều trong ngày. TUYỆT ĐỐI KHÔNG uống rượu trong và ít nhất 3 ngày sau khi ngừng."
            },
            "iv": {
                "reconstitution": "Pha với NS (0.9% NaCl), D5W (5% Dextrose), hoặc Ringer's Lactate. Nồng độ pha: 5mg/ml (tối đa). Pha 500mg trong 100ml = 5mg/ml. Pha 1g trong 200ml = 5mg/ml. Lắc kỹ để hòa tan hoàn toàn. Bảo quản tránh ánh sáng.",
                "infusion_rate": "Truyền IV trong 30-60 phút. Tốc độ: 100ml/30 phút = ~3.3ml/phút, 100ml/60 phút = ~1.7ml/phút. KHÔNG truyền nhanh (bolus) - tăng nguy cơ tác dụng phụ.",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)", "Ringer's Lactate"],
                "incompatibility": [
                    "Aminophylline - tạo kết tủa, không pha chung",
                    "Phenytoin - có thể tạo kết tủa, không pha chung",
                    "Các thuốc có tính kiềm hoặc acid mạnh"
                ],
                "notes": "QUAN TRỌNG: 1) TUYỆT ĐỐI KHÔNG uống rượu trong và ít nhất 3 ngày sau khi ngừng, 2) Truyền chậm (30-60 phút) để giảm tác dụng phụ, 3) Bảo quản tránh ánh sáng, 4) Theo dõi dấu hiệu tổn thương thần kinh, 5) Điều chỉnh liều ở suy gan nặng."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Metronidazole (Flagyl)",
                "UpToDate - Metronidazole: Drug Information",
                "Medscape - Metronidazole Drug Reference",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
                "Lexicomp Online - Metronidazole Monograph",
                "Micromedex - Metronidazole Drug Information",
                "IDSA Guidelines - Anaerobic Infections, C. difficile Infection"
            ],
            "last_updated": "2025-02-03",
            "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },

    "Chloroquine": {
        "group": "Infectious Disease - Antimalarial",
        "vietnamese_name": "Chloroquine, Aralen",
        "administration": ["PO"],
        "indications": [
            "Sốt rét (phòng ngừa và điều trị)",
            "Amebiasis ngoài gan",
            "Lupus ban đỏ hệ thống",
            "Viêm khớp dạng thấp"
        ],
        "contraindications": [
            "Dị ứng chloroquine/4-aminoquinoline",
            "Bệnh võng mạc",
            "Bệnh gan nặng",
            "Bệnh thận nặng",
            "Rối loạn tạo máu"
        ],
        "dosage": {
            "adult_malaria_treatment": "600mg base (1g phosphate) ngày đầu, sau đó 300mg base (500mg phosphate) sau 6-8 giờ, sau đó 300mg base/ngày x 2 ngày",
            "adult_malaria_prophylaxis": "300mg base (500mg phosphate) x 1 lần/tuần, bắt đầu 1-2 tuần trước khi đi, tiếp tục trong khi ở và 4 tuần sau khi về",
            "adult_lupus": "200-400mg base/ngày",
            "notes": "Rất độc cho võng mạc nếu dùng lâu dài. Theo dõi mắt định kỳ"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 50%",
            "under_30": "Tránh dùng"
        },
        "side_effects": [
            "Độc võng mạc (dùng lâu dài, không hồi phục)",
            "Rối loạn thị giác",
            "Ban da, rụng tóc",
            "Rối loạn tạo máu",
            "Rối loạn tim mạc (liều cao)",
            "Co giật (quá liều)",
            "Độc gan"
        ],
        "interactions": [
            "Digoxin: tăng nồng độ digoxin",
            "Cimetidine: tăng nồng độ chloroquine",
            "Ampicillin: giảm hấp thu ampicillin",
            "Kaolin: giảm hấp thu chloroquine"
        ],
        "pregnancy": "C - Thận trọng, nhưng có thể dùng cho sốt rét",
        "mechanism_of_action": "Chloroquine là 4-aminoquinoline, ức chế polymerase của ký sinh trùng sốt rét, ngăn cản tổng hợp DNA và RNA. Thuốc tích lũy trong lysosome của ký sinh trùng, tăng pH và ức chế tiêu hóa hemoglobin. Đối với sốt rét, chloroquine diệt thể vô tính trong hồng cầu. Đối với bệnh tự miễn (lupus, RA), chloroquine ức chế hoạt động của tế bào miễn dịch và giảm sản xuất cytokine viêm",
        "monitoring": [
            "Khám mắt định kỳ mỗi 6-12 tháng nếu dùng lâu dài (theo dõi độc võng mạc)",
            "Thị trường (visual field) mỗi 6-12 tháng nếu dùng lâu dài",
            "Chức năng gan (ALT, AST) định kỳ",
            "Công thức máu toàn phần (CBC) định kỳ",
            "Điện tâm đồ nếu dùng liều cao (theo dõi rối loạn nhịp)",
            "Dấu hiệu rối loạn thị giác (nhìn mờ, ám điểm)",
            "Dấu hiệu độc võng mạc (không hồi phục nếu phát hiện muộn)"
        ],
        "precautions": [
            "Rất độc cho võng mạc nếu dùng lâu dài - cần khám mắt định kỳ",
            "Ngừng ngay nếu có dấu hiệu độc võng mạc (nhìn mờ, ám điểm)",
            "Giảm liều 50% nếu suy thận (CrCl 30-60)",
            "Tránh dùng nếu suy thận nặng (CrCl <30)",
            "Có thể dùng trong thai kỳ cho sốt rét (category C)",
            "Tránh dùng với kaolin (giảm hấp thu)",
            "Tương tác với digoxin (tăng nồng độ digoxin)",
            "Có thể gây rối loạn nhịp tim nếu dùng liều cao (cần theo dõi ECG)"
        ],
        "pharmacokinetics": {
            "half_life": "20-60 ngày (rất dài, tích lũy)",
            "onset": "2-3 giờ (sốt rét), 4-8 tuần (lupus/RA)",
            "duration": "7-14 ngày (sốt rét), kéo dài (lupus/RA)",
            "protein_binding": "55%",
            "clearance": "Gan (chuyển hóa), thận (thải trừ - chậm)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Có thể gây độc võng mạc nặng và không hồi phục nếu dùng lâu dài. Cần khám mắt định kỳ mỗi 6-12 tháng khi dùng lâu dài. Ngừng ngay nếu có dấu hiệu độc võng mạc",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Digoxin",
                    "mechanism": "Chloroquine tăng nồng độ digoxin (cơ chế chưa rõ)",
                    "effect": "Tăng nồng độ digoxin, tăng nguy cơ độc tính digoxin (rối loạn nhịp, buồn nôn)",
                    "management": "Theo dõi nồng độ digoxin, giảm liều digoxin nếu cần. Theo dõi ECG và triệu chứng độc tính digoxin"
                }
            ],
            "moderate": [
                {
                    "drug": "Cimetidine",
                    "mechanism": "Ức chế chuyển hóa chloroquine",
                    "effect": "Tăng nồng độ chloroquine, tăng độc tính",
                    "management": "Theo dõi độc tính chloroquine (võng mạc, gan, máu)"
                },
                {
                    "drug": "Ampicillin",
                    "mechanism": "Chloroquine giảm hấp thu ampicillin",
                    "effect": "Giảm hiệu quả ampicillin",
                    "management": "Tách thời gian dùng (cách nhau ít nhất 2 giờ)"
                },
                {
                    "drug": "Kaolin",
                    "mechanism": "Kaolin giảm hấp thu chloroquine",
                    "effect": "Giảm hiệu quả chloroquine",
                    "management": "Tách thời gian dùng (cách nhau ít nhất 2 giờ)"
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng chloroquine hoặc 4-aminoquinoline",
                "Bệnh võng mạc (retinopathy) - đặc biệt nếu dùng lâu dài",
                "Suy gan nặng",
                "Suy thận nặng (CrCl <30)"
            ],
            "tương_đối": [
                "Rối loạn tạo máu - thận trọng, theo dõi công thức máu",
                "Bệnh tim mạch - thận trọng với liều cao (có thể gây rối loạn nhịp)",
                "Bệnh võng mạc nhẹ - thận trọng, khám mắt thường xuyên"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Có thể dùng trong thai kỳ cho sốt rét (category C). Sốt rét có thể đe dọa tính mạng mẹ và thai nhi, nên điều trị vẫn cần thiết. Tuy nhiên, thận trọng với liều cao và dùng lâu dài (lupus, RA) do nguy cơ độc võng mạc. Cân nhắc lợi ích/nguy cơ.",
            "lactation": {
                "safety": "Unknown",
                "details": "Chloroquine bài tiết vào sữa mẹ. Không có dữ liệu đầy đủ về an toàn cho trẻ bú mẹ.",
                "recommendation": "Thận trọng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc tùy theo tình trạng lâm sàng. Sốt rét có thể đe dọa tính mạng, nên điều trị vẫn cần thiết"
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi liều",
            "moderate": "Không đổi liều, nhưng theo dõi chức năng gan",
            "severe": "Tránh dùng hoặc dùng liều thấp dưới sự giám sát chặt chẽ. Theo dõi ALT/AST, bilirubin thường xuyên",
            "notes": "Chloroquine chuyển hóa ở gan. Suy gan có thể làm giảm chuyển hóa và tăng tích lũy, tăng nguy cơ độc tính gan"
        },
        "overdose_management": {
            "symptoms": [
                "Rối loạn thị giác (nhìn mờ, ám điểm)",
                "Độc võng mạc (không hồi phục nếu phát hiện muộn)",
                "Rối loạn nhịp tim (liều cao)",
                "Co giật (quá liều)",
                "Rối loạn tạo máu (giảm bạch cầu, giảm tiểu cầu)",
                "Độc gan",
                "Ban da, rụng tóc"
            ],
            "antidote": "Không có thuốc giải độc đặc hiệu",
            "treatment": [
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính nếu uống trong vòng 1 giờ",
                "Điều trị hỗ trợ: Truyền dịch, điều chỉnh điện giải",
                "Theo dõi ECG nếu có triệu chứng rối loạn nhịp",
                "Điều trị co giật nếu có (benzodiazepine)",
                "Theo dõi chức năng gan (ALT, AST, bilirubin)",
                "Theo dõi công thức máu (CBC) - theo dõi rối loạn tạo máu",
                "Khám mắt ngay (theo dõi độc võng mạc)",
                "Điều trị triệu chứng: Thuốc chống nôn, giảm đau nếu cần"
            ],
            "monitoring": "ECG (nếu có triệu chứng rối loạn nhịp), chức năng gan (ALT, AST, bilirubin), công thức máu (CBC), khám mắt (theo dõi độc võng mạc), triệu chứng lâm sàng"
        },
        "reversal_agents": {
            "available": False,
            "agents": None,
            "notes": "Không có thuốc giải độc đặc hiệu. Điều trị hỗ trợ và theo dõi. Quan trọng: khám mắt ngay để phát hiện độc võng mạc sớm"
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với thức ăn hoặc không. Uống với thức ăn có thể giảm kích ứng dạ dày nhẹ",
                "timing": "Với sốt rét: 600mg base (1g phosphate) ngày đầu, sau đó 300mg base (500mg phosphate) sau 6-8 giờ, sau đó 300mg base/ngày x 2 ngày. Với phòng ngừa: 300mg base (500mg phosphate) x 1 lần/tuần. Với lupus/RA: 200-400mg base/ngày",
                "notes": "Rất độc cho võng mạc nếu dùng lâu dài (lupus, RA). Cần khám mắt định kỳ mỗi 6-12 tháng. Ngừng ngay nếu có dấu hiệu độc võng mạc. Tránh dùng với kaolin (giảm hấp thu)"
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Chloroquine (Aralen)",
                "UpToDate - Chloroquine drug information",
                "WHO Guidelines for the treatment of malaria",
                "American Academy of Ophthalmology Guidelines for chloroquine retinopathy screening",
                "Goodman & Gilman's Pharmacological Basis of Therapeutics"
            ],
            "last_updated": "2025-02-04",
            "evidence_level": "High - Guidelines dựa trên chứng cứ từ WHO, FDA và AAO"
        }
    },

    "Artesunate": {
        "group": "Infectious Disease - Antimalarial (Artemisinin)",
        "vietnamese_name": "Artesunate",
        "administration": ["PO", "IV", "IM", "Rectal"],
        "indications": [
            "Sốt rét nặng (severe malaria)",
            "Sốt rét kháng chloroquine",
            "Sốt rét sốt rét P. falciparum",
            "Điều trị kết hợp sốt rét (ACT)"
        ],
        "contraindications": [
            "Dị ứng artesunate/artemisinin",
            "3 tháng đầu thai kỳ (trừ sốt rét nặng)",
            "Dùng đơn độc (phải dùng kết hợp)"
        ],
        "dosage": {
            "adult_severe_iv": "2.4mg/kg IV ngay, sau đó 1.2mg/kg sau 12 và 24 giờ, sau đó mỗi ngày",
            "adult_po": "200mg ngày đầu, sau đó 100mg x 1 lần/ngày x 5 ngày (với artemether-lumefantrine)",
            "adult_act": "Theo phác đồ ACT (artesunate + amodiaquine/ mefloquine/piperaquine)",
            "notes": "PHẢI dùng kết hợp với thuốc sốt rét khác (ACT). Không dùng đơn độc"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng"
        },
        "side_effects": [
            "Nhức đầu",
            "Chóng mặt",
            "Buồn nôn",
            "Rối loạn tiêu hóa",
            "Nhịp tim chậm (hiếm)",
            "Độc tính thần kinh (dùng lâu dài, liều cao - hiếm)"
        ],
        "interactions": [
            "Thuốc sốt rét khác: dùng kết hợp (ACT protocol)",
            "Warfarin: có thể tăng tác dụng chống đông",
            "CYP2A6 substrates: có thể tăng nồng độ"
        ],
        "pregnancy": "D - Tránh trong 3 tháng đầu (trừ sốt rét nặng)",
        "mechanism_of_action": "Artesunate là dẫn xuất artemisinin (sesquiterpene lactone), chuyển hóa thành dihydroartemisinin (hoạt chất). Tác động nhanh và mạnh lên ký sinh trùng sốt rét bằng cách tạo ra các gốc tự do (free radicals) trong hồng cầu bị nhiễm, gây stress oxy hóa và phá vỡ màng tế bào ký sinh trùng. Artesunate diệt cả thể vô tính và thể giao tử (gametocyte), đặc biệt hiệu quả với P. falciparum kháng chloroquine. Thuốc có tác dụng nhanh (fast-acting), giảm số lượng ký sinh trùng trong 24-48 giờ",
        "monitoring": [
            "Theo dõi sốt và triệu chứng sốt rét (giảm nhanh trong 24-48 giờ)",
            "Ký sinh trùng trong máu (parasitemia) mỗi 6-12 giờ trong sốt rét nặng",
            "Chức năng gan (ALT, AST) nếu dùng lâu dài",
            "Dấu hiệu rối loạn nhịp tim (nhịp chậm - hiếm)",
            "Dấu hiệu độc tính thần kinh nếu dùng lâu dài, liều cao (hiếm)",
            "Đường huyết nếu dùng IV (có thể gây hạ đường huyết)"
        ],
        "precautions": [
            "PHẢI dùng kết hợp với thuốc sốt rét khác (ACT protocol) - không dùng đơn độc",
            "Tránh dùng trong 3 tháng đầu thai kỳ (trừ sốt rét nặng - cân nhắc lợi ích/nguy cơ)",
            "Dùng đúng phác đồ ACT để tránh kháng thuốc",
            "Không dùng đơn độc (dễ gây kháng thuốc)",
            "Có thể gây hạ đường huyết nếu dùng IV (theo dõi)",
            "Có thể gây nhịp tim chậm (hiếm - theo dõi ECG nếu có triệu chứng)",
            "Có thể tương tác với warfarin (tăng tác dụng chống đông)",
            "Dùng kết hợp với amodiaquine, mefloquine, hoặc piperaquine theo phác đồ ACT"
        ],
        "pharmacokinetics": {
            "half_life": "45 phút (artesunate), 1-2 giờ (dihydroartemisinin)",
            "onset": "1-2 giờ (giảm sốt, triệu chứng)",
            "duration": "4-6 giờ (ngắn)",
            "protein_binding": "Moderate",
            "clearance": "Gan (chuyển hóa nhanh qua CYP2A6, esterase), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Để tủ lạnh (2-8°C) nếu yêu cầu",
        "black_box_warnings": "KHÔNG được dùng đơn độc - phải dùng kết hợp với thuốc sốt rét khác theo phác đồ ACT để tránh kháng thuốc. Tránh dùng trong 3 tháng đầu thai kỳ trừ sốt rét nặng (cân nhắc lợi ích/nguy cơ)",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Dùng đơn độc (không kết hợp)",
                    "mechanism": "Dùng artesunate đơn độc dễ gây kháng thuốc",
                    "effect": "Kháng thuốc sốt rét, thất bại điều trị",
                    "management": "PHẢI dùng kết hợp với thuốc sốt rét khác theo phác đồ ACT (artesunate + amodiaquine/mefloquine/piperaquine)"
                }
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Có thể tăng tác dụng chống đông",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên, điều chỉnh liều warfarin nếu cần"
                },
                {
                    "drug": "CYP2A6 substrates",
                    "mechanism": "Artesunate chuyển hóa qua CYP2A6, có thể ức chế hoặc cảm ứng",
                    "effect": "Có thể tăng hoặc giảm nồng độ các thuốc chuyển hóa qua CYP2A6",
                    "management": "Thận trọng, theo dõi tác dụng phụ"
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dùng đơn độc (phải dùng kết hợp với thuốc sốt rét khác)",
                "Dị ứng artesunate hoặc artemisinin"
            ],
            "tương_đối": [
                "3 tháng đầu thai kỳ - tránh trừ sốt rét nặng (cân nhắc lợi ích/nguy cơ)",
                "Suy thận nặng (CrCl <30) - thận trọng",
                "Suy gan nặng - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Tránh dùng trong 3 tháng đầu thai kỳ trừ sốt rét nặng (cân nhắc lợi ích/nguy cơ). Sốt rét nặng có thể đe dọa tính mạng mẹ và thai nhi, nên điều trị vẫn cần thiết. Có thể dùng trong tam cá nguyệt 2 và 3 nếu cần. Phải dùng kết hợp với thuốc sốt rét khác theo phác đồ ACT.",
            "lactation": {
                "safety": "Unknown",
                "details": "Artesunate bài tiết vào sữa mẹ. Không có dữ liệu đầy đủ về an toàn cho trẻ bú mẹ.",
                "recommendation": "Thận trọng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc tùy theo tình trạng lâm sàng. Sốt rét nặng có thể đe dọa tính mạng, nên điều trị vẫn cần thiết"
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi liều",
            "moderate": "Không đổi liều, nhưng theo dõi chức năng gan",
            "severe": "Thận trọng, theo dõi chức năng gan thường xuyên",
            "notes": "Artesunate chuyển hóa nhanh ở gan qua CYP2A6 và esterase. Suy gan có thể làm giảm chuyển hóa, nhưng ít tích lũy do half-life ngắn"
        },
        "overdose_management": {
            "symptoms": [
                "Nhức đầu, chóng mặt",
                "Buồn nôn, nôn",
                "Rối loạn tiêu hóa",
                "Nhịp tim chậm (hiếm)",
                "Hạ đường huyết (nếu dùng IV)",
                "Độc tính thần kinh (nếu dùng lâu dài, liều cao - hiếm)"
            ],
            "antidote": "Không có thuốc giải độc đặc hiệu",
            "treatment": [
                "Ngừng thuốc ngay",
                "Điều trị hỗ trợ: Truyền dịch, điều chỉnh điện giải",
                "Theo dõi đường huyết nếu dùng IV (có thể gây hạ đường huyết)",
                "Theo dõi nhịp tim (ECG) nếu có triệu chứng nhịp chậm",
                "Điều trị triệu chứng: Thuốc chống nôn, giảm đau nếu cần",
                "Theo dõi chức năng gan nếu dùng lâu dài"
            ],
            "monitoring": "Triệu chứng lâm sàng, đường huyết (nếu dùng IV), nhịp tim (ECG nếu có triệu chứng), chức năng gan (nếu dùng lâu dài)"
        },
        "reversal_agents": {
            "available": False,
            "agents": None,
            "notes": "Không có thuốc giải độc đặc hiệu. Điều trị hỗ trợ và theo dõi"
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với thức ăn hoặc không",
                "timing": "Theo phác đồ ACT. Thường: 200mg ngày đầu, sau đó 100mg x 1 lần/ngày x 5 ngày (với artemether-lumefantrine hoặc các phác đồ ACT khác)",
                "notes": "PHẢI dùng kết hợp với thuốc sốt rét khác (amodiaquine, mefloquine, piperaquine) theo phác đồ ACT. Không dùng đơn độc"
            },
            "iv": {
                "reconstitution": "Pha trong D5W hoặc NS. Dùng ngay sau khi pha",
                "infusion_rate": "Truyền trong 5-10 phút",
                "compatibility": ["D5W", "NS"],
                "incompatibility": ["Không pha trộn với các thuốc khác"],
                "notes": "Dùng cho sốt rét nặng. Liều: 2.4mg/kg IV ngay, sau đó 1.2mg/kg sau 12 và 24 giờ, sau đó mỗi ngày. Theo dõi đường huyết (có thể gây hạ đường huyết)"
            },
            "im": {
                "notes": "Có thể dùng IM cho sốt rét nặng nếu không có IV. Liều tương tự IV"
            },
            "rectal": {
                "notes": "Có thể dùng đường trực tràng cho trẻ em hoặc khi không có đường uống/IV. Liều theo cân nặng"
            }
        },
        "references": {
            "primary_sources": [
                "WHO Guidelines for the treatment of malaria",
                "WHO Guidelines for ACT (Artemisinin-based Combination Therapy)",
                "UpToDate - Artesunate drug information",
                "CDC Guidelines for treatment of malaria",
                "Goodman & Gilman's Pharmacological Basis of Therapeutics"
            ],
            "last_updated": "2025-02-04",
            "evidence_level": "High - Guidelines dựa trên chứng cứ từ WHO và CDC"
        }
    },

    "Albendazole": {
        "group": "Infectious Disease - Anthelmintic",
        "vietnamese_name": "Albendazole, Albenza",
        "administration": ["PO"],
        "indications": [
            "Giun sán (giun đũa, giun móc, giun tóc, giun kim)",
            "Sán dây",
            "Sán lá gan",
            "Hydatid disease (Echinococcus)",
            "Neurocysticercosis"
        ],
        "contraindications": [
            "Dị ứng albendazole/benzimidazole",
            "Có thai",
            "Suy gan nặng",
            "Giảm bạch cầu"
        ],
        "dosage": {
            "adult_intestinal_worms": "400mg x 1 lần (đơn liều) hoặc 400mg x 2 lần/ngày x 3 ngày",
            "adult_echinococcus": "400mg x 2 lần/ngày x 28 ngày (có thể lặp lại)",
            "adult_neurocysticercosis": "400mg x 2 lần/ngày x 8-30 ngày",
            "adult_hydatid": "10-15mg/kg/ngày x 28 ngày",
            "notes": "Uống với thức ăn béo để tăng hấp thu. Uống kèm corticosteroid cho neurocysticercosis"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng"
        },
        "side_effects": [
            "Đau đầu",
            "Buồn nôn, nôn",
            "Đau bụng",
            "Tiêu chảy",
            "Giảm bạch cầu",
            "Tăng men gan",
            "Ban da",
            "Rụng tóc (dùng lâu dài)"
        ],
        "interactions": [
            "Dexamethasone: tăng nồng độ albendazole",
            "Praziquantel: tăng nồng độ albendazole",
            "Cimetidine: tăng nồng độ albendazole",
            "Phenytoin/Carbamazepine: giảm nồng độ albendazole"
        ],
        "pregnancy": "D - Chống chỉ định",
        "mechanism_of_action": "Albendazole là benzimidazole carbamate, ức chế tubulin polymerization trong tế bào ký sinh trùng, gây mất microtubule, phá vỡ cấu trúc tế bào và chức năng của ký sinh trùng. Thuốc ngăn chặn vận chuyển glucose và các chất dinh dưỡng khác trong tế bào ký sinh trùng, dẫn đến mất năng lượng và chết. Albendazole có tác dụng phổ rộng trên nhiều loại giun sán, bao gồm giun đũa, giun móc, giun tóc, giun kim, sán dây, và sán lá gan. Đặc biệt hiệu quả trong điều trị hydatid disease và neurocysticercosis do tác dụng hệ thống tốt hơn mebendazole.",
        "monitoring": [
            "Công thức máu (CBC) - theo dõi giảm bạch cầu, đặc biệt khi dùng lâu dài",
            "Chức năng gan (ALT, AST, bilirubin) - theo dõi độc tính gan",
            "Triệu chứng lâm sàng (đau đầu, buồn nôn, đau bụng)",
            "Đáp ứng điều trị (xét nghiệm phân sau điều trị)",
            "Dấu hiệu nhiễm độc (rụng tóc, ban da) khi dùng lâu dài"
        ],
        "precautions": [
            "Uống với thức ăn béo để tăng hấp thu (tăng nồng độ trong máu 5 lần)",
            "Dùng kèm corticosteroid (dexamethasone) cho neurocysticercosis để giảm phản ứng viêm",
            "Theo dõi chức năng gan thường xuyên khi dùng lâu dài (hydatid disease, neurocysticercosis)",
            "Tránh dùng trong thai kỳ (gây dị tật thai nhi)",
            "Kiểm tra thai trước khi bắt đầu điều trị",
            "Dùng biện pháp tránh thai hiệu quả trong và sau điều trị",
            "Thận trọng ở bệnh nhân suy gan",
            "Theo dõi công thức máu khi dùng lâu dài (nguy cơ giảm bạch cầu)"
        ],
        "pharmacokinetics": {
            "half_life": "8-12 giờ (albendazole sulfoxide - chất chuyển hóa hoạt động)",
            "onset": "2-4 giờ",
            "duration": "24-48 giờ",
            "protein_binding": "70%",
            "clearance": "Gan (chuyển hóa thành albendazole sulfoxide), thải trừ qua mật và nước tiểu"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Chống chỉ định trong thai kỳ - có thể gây dị tật thai nhi và tử vong thai nhi. Cần kiểm tra thai trước khi bắt đầu điều trị",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Dexamethasone",
                    "mechanism": "Tăng nồng độ albendazole sulfoxide (chất chuyển hóa hoạt động) qua ức chế CYP3A4",
                    "effect": "Tăng nồng độ albendazole, tăng hiệu quả và độc tính",
                    "management": "Theo dõi chức năng gan và công thức máu. Có thể cần giảm liều albendazole"
                },
                {
                    "drug": "Praziquantel",
                    "mechanism": "Tăng nồng độ albendazole sulfoxide",
                    "effect": "Tăng hiệu quả điều trị, nhưng cũng tăng độc tính",
                    "management": "Theo dõi chức năng gan và công thức máu"
                }
            ],
            "moderate": [
                {
                    "drug": "Cimetidine",
                    "mechanism": "Ức chế CYP3A4, tăng nồng độ albendazole sulfoxide",
                    "effect": "Tăng nồng độ albendazole",
                    "management": "Theo dõi chức năng gan"
                },
                {
                    "drug": "Phenytoin, Carbamazepine",
                    "mechanism": "Cảm ứng CYP3A4, tăng chuyển hóa albendazole",
                    "effect": "Giảm nồng độ albendazole, giảm hiệu quả",
                    "management": "Có thể cần tăng liều albendazole hoặc dùng thuốc khác"
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Có thai (category D - gây dị tật thai nhi)",
                "Dị ứng albendazole hoặc benzimidazole",
                "Suy gan nặng (Child-Pugh C)"
            ],
            "tương_đối": [
                "Suy gan nhẹ đến trung bình (Child-Pugh A-B) - thận trọng, theo dõi chức năng gan",
                "Giảm bạch cầu - thận trọng, theo dõi công thức máu",
                "Suy thận nặng (CrCl <30) - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Chống chỉ định trong thai kỳ. Albendazole có thể gây dị tật thai nhi và tử vong thai nhi. Cần kiểm tra thai trước khi bắt đầu điều trị. Phụ nữ trong độ tuổi sinh đẻ phải dùng biện pháp tránh thai hiệu quả trong và sau điều trị ít nhất 1 tháng.",
            "lactation": {
                "safety": "Unknown",
                "details": "Albendazole bài tiết vào sữa mẹ. Không có dữ liệu đầy đủ về an toàn cho trẻ bú mẹ.",
                "recommendation": "Thận trọng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc tùy theo tình trạng lâm sàng"
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi liều, nhưng theo dõi chức năng gan",
            "moderate": "Thận trọng, theo dõi chức năng gan thường xuyên",
            "severe": "Tránh dùng hoặc dùng liều thấp dưới sự giám sát chặt chẽ. Theo dõi ALT/AST, bilirubin thường xuyên",
            "notes": "Albendazole chuyển hóa ở gan thành albendazole sulfoxide (hoạt chất). Suy gan có thể làm giảm chuyển hóa và tăng tích lũy, tăng nguy cơ độc tính gan"
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn, đau bụng",
                "Đau đầu, chóng mặt",
                "Tăng men gan (ALT, AST)",
                "Giảm bạch cầu",
                "Ban da, rụng tóc"
            ],
            "antidote": "Không có thuốc giải độc đặc hiệu",
            "treatment": [
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính nếu uống trong vòng 1 giờ",
                "Điều trị hỗ trợ: Truyền dịch, điều chỉnh điện giải",
                "Theo dõi chức năng gan (ALT, AST, bilirubin) thường xuyên",
                "Theo dõi công thức máu (CBC) - theo dõi giảm bạch cầu",
                "Điều trị triệu chứng: Thuốc chống nôn, giảm đau nếu cần"
            ],
            "monitoring": "Chức năng gan (ALT, AST, bilirubin), công thức máu (CBC), triệu chứng lâm sàng"
        },
        "reversal_agents": {
            "available": False,
            "agents": None,
            "notes": "Không có thuốc giải độc đặc hiệu. Điều trị hỗ trợ và theo dõi"
        },
        "administration_instructions": {
            "oral": {
                "with_food": "BẮT BUỘC uống với thức ăn béo (bữa ăn có chất béo) để tăng hấp thu. Uống với thức ăn béo tăng nồng độ trong máu lên 5 lần so với uống khi đói",
                "timing": "Uống với bữa ăn chính (sáng, trưa, tối). Với hydatid disease và neurocysticercosis: 400mg x 2 lần/ngày với bữa ăn",
                "notes": "Với neurocysticercosis: dùng kèm corticosteroid (dexamethasone) để giảm phản ứng viêm. Với hydatid disease: có thể cần lặp lại chu kỳ 28 ngày"
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Albendazole (Albenza)",
                "UpToDate - Albendazole drug information",
                "WHO Guidelines for treatment of echinococcosis",
                "WHO Guidelines for treatment of neurocysticercosis",
                "Goodman & Gilman's Pharmacological Basis of Therapeutics"
            ],
            "last_updated": "2025-02-04",
            "evidence_level": "High - Guidelines dựa trên chứng cứ từ WHO và FDA"
        }
    },

    "Mebendazole": {
        "group": "Infectious Disease - Anthelmintic",
        "vietnamese_name": "Mebendazole, Vermox",
        "administration": ["PO"],
        "indications": [
            "Giun sán (giun đũa, giun móc, giun tóc, giun kim)",
            "Sán dây",
            "Trichinosis"
        ],
        "contraindications": [
            "Dị ứng mebendazole/benzimidazole",
            "Có thai",
            "Trẻ em <1 tuổi"
        ],
        "dosage": {
            "adult_intestinal_worms": "100mg x 2 lần/ngày x 3 ngày",
            "adult_pinworm": "100mg x 1 lần (đơn liều), lặp lại sau 2-3 tuần",
            "adult_whipworm": "100mg x 2 lần/ngày x 3 ngày",
            "adult_tapeworm": "100mg x 2 lần/ngày x 3 ngày",
            "notes": "Uống với thức ăn hoặc không đều được. Không hấp thu tốt nên ít tác dụng phụ hệ thống"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Đau bụng",
            "Tiêu chảy",
            "Buồn nôn",
            "Ban da",
            "Giảm bạch cầu (dùng lâu dài, liều cao)",
            "Độc gan (hiếm)"
        ],
        "interactions": [
            "Cimetidine: có thể tăng nồng độ mebendazole",
            "Carbamazepine/Phenytoin: có thể giảm nồng độ mebendazole"
        ],
        "pregnancy": "D - Chống chỉ định",
        "mechanism_of_action": "Mebendazole là benzimidazole carbamate, ức chế tubulin polymerization trong tế bào ký sinh trùng, gây mất microtubule và phá vỡ cấu trúc tế bào. Thuốc ngăn chặn vận chuyển glucose và các chất dinh dưỡng trong tế bào ký sinh trùng, dẫn đến mất năng lượng và chết. Khác với albendazole, mebendazole hấp thu kém qua đường tiêu hóa (<5%), nên chủ yếu tác dụng tại chỗ trong ruột, ít tác dụng phụ hệ thống. Thuốc hiệu quả trên giun đũa, giun móc, giun tóc, giun kim, và sán dây. Thường dùng cho nhiễm giun đường ruột đơn giản, ít dùng cho nhiễm nấm hệ thống.",
        "monitoring": [
            "Triệu chứng lâm sàng (đau bụng, tiêu chảy, buồn nôn)",
            "Đáp ứng điều trị (xét nghiệm phân sau 2-3 tuần)",
            "Công thức máu (nếu dùng lâu dài, liều cao) - theo dõi giảm bạch cầu",
            "Chức năng gan (nếu dùng lâu dài, liều cao)",
            "Dấu hiệu dị ứng (ban da)"
        ],
        "precautions": [
            "Có thể uống với thức ăn hoặc không (không ảnh hưởng nhiều do hấp thu kém)",
            "Không hấp thu tốt nên ít tác dụng phụ hệ thống (ưu điểm so với albendazole)",
            "Phù hợp cho nhiễm giun đường ruột đơn giản",
            "Lặp lại liều sau 2-3 tuần cho giun kim (để diệt ấu trùng mới nở)",
            "Tránh dùng trong thai kỳ (gây dị tật thai nhi)",
            "Không dùng cho trẻ em <1 tuổi",
            "Thận trọng ở bệnh nhân suy gan nặng",
            "Theo dõi công thức máu nếu dùng lâu dài hoặc liều cao"
        ],
        "pharmacokinetics": {
            "half_life": "2-9 giờ (rất thay đổi do hấp thu kém)",
            "onset": "2-4 giờ",
            "duration": "24-48 giờ",
            "protein_binding": "90-95%",
            "clearance": "Hấp thu kém (<5%), chủ yếu thải trừ qua phân, một phần qua nước tiểu"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Chống chỉ định trong thai kỳ - có thể gây dị tật thai nhi",
        "drug_interactions": {
            "moderate": [
                {
                    "drug": "Cimetidine",
                    "mechanism": "Có thể ức chế chuyển hóa mebendazole, tăng nồng độ",
                    "effect": "Tăng nồng độ mebendazole (nhưng ít ảnh hưởng do hấp thu kém)",
                    "management": "Theo dõi tác dụng phụ"
                },
                {
                    "drug": "Carbamazepine, Phenytoin",
                    "mechanism": "Cảm ứng enzyme chuyển hóa",
                    "effect": "Có thể giảm nồng độ mebendazole (nhưng ít ảnh hưởng do hấp thu kém)",
                    "management": "Theo dõi đáp ứng điều trị"
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Có thai (category D - gây dị tật thai nhi)",
                "Dị ứng mebendazole hoặc benzimidazole",
                "Trẻ em <1 tuổi"
            ],
            "tương_đối": [
                "Suy gan nặng - thận trọng",
                "Giảm bạch cầu - thận trọng khi dùng lâu dài"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Chống chỉ định trong thai kỳ. Mebendazole có thể gây dị tật thai nhi. Phụ nữ trong độ tuổi sinh đẻ phải dùng biện pháp tránh thai hiệu quả trong và sau điều trị.",
            "lactation": {
                "safety": "Unknown",
                "details": "Mebendazole hấp thu kém (<5%) nên ít bài tiết vào sữa mẹ. Tuy nhiên, không có dữ liệu đầy đủ về an toàn cho trẻ bú mẹ.",
                "recommendation": "Thận trọng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc tùy theo tình trạng lâm sàng"
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi liều",
            "moderate": "Không đổi liều",
            "severe": "Thận trọng, theo dõi chức năng gan",
            "notes": "Mebendazole hấp thu kém qua đường tiêu hóa (<5%), chủ yếu tác dụng tại chỗ trong ruột, ít tác dụng phụ hệ thống. Suy gan ít ảnh hưởng do hấp thu kém"
        },
        "overdose_management": {
            "symptoms": [
                "Đau bụng, tiêu chảy",
                "Buồn nôn, nôn",
                "Ban da",
                "Giảm bạch cầu (nếu dùng liều cao, lâu dài)",
                "Độc gan (hiếm)"
            ],
            "antidote": "Không có thuốc giải độc đặc hiệu",
            "treatment": [
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính nếu uống trong vòng 1 giờ",
                "Điều trị hỗ trợ: Truyền dịch, điều chỉnh điện giải",
                "Điều trị triệu chứng: Thuốc chống nôn, giảm đau nếu cần",
                "Theo dõi công thức máu nếu dùng liều cao, lâu dài",
                "Theo dõi chức năng gan nếu có triệu chứng"
            ],
            "monitoring": "Triệu chứng lâm sàng, công thức máu (nếu dùng liều cao), chức năng gan (nếu có triệu chứng)"
        },
        "reversal_agents": {
            "available": False,
            "agents": None,
            "notes": "Không có thuốc giải độc đặc hiệu. Điều trị hỗ trợ và theo dõi"
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với thức ăn hoặc không (không ảnh hưởng nhiều do hấp thu kém). Uống với thức ăn có thể giảm kích ứng dạ dày nhẹ",
                "timing": "Uống với bữa ăn hoặc không. Với giun đũa, giun móc, giun tóc, sán dây: 100mg x 2 lần/ngày x 3 ngày. Với giun kim: 100mg x 1 lần (đơn liều), lặp lại sau 2-3 tuần",
                "notes": "Lặp lại liều sau 2-3 tuần cho giun kim để diệt ấu trùng mới nở. Không hấp thu tốt nên ít tác dụng phụ hệ thống (ưu điểm so với albendazole)"
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Mebendazole (Vermox)",
                "UpToDate - Mebendazole drug information",
                "WHO Guidelines for treatment of soil-transmitted helminthiasis",
                "Goodman & Gilman's Pharmacological Basis of Therapeutics"
            ],
            "last_updated": "2025-02-04",
            "evidence_level": "High - Guidelines dựa trên chứng cứ từ WHO và FDA"
        }
    },

    "Amoxicillin-clavulanate": {
        "group": "Antibiotic - Beta-lactam (Penicillin + Beta-lactamase inhibitor)",
        "vietnamese_name": "Amoxicillin-clavulanate, Augmentin, Amoclav",
        "administration": ["PO", "IV"],
        "indications": [
            "Nhiễm khuẩn đường hô hấp trên/dưới",
            "Nhiễm khuẩn đường tiết niệu",
            "Nhiễm khuẩn da mô mềm",
            "Nhiễm khuẩn răng miệng",
            "Nhiễm khuẩn tai mũi họng (trẻ em)"
        ],
        "contraindications": [
            "Dị ứng penicillin",
            "Viêm gan do amoxicillin-clavulanate trước đây",
            "Dị ứng beta-lactam"
        ],
        "dosage": {
            "adult_po": "875/125mg x 2 lần/ngày hoặc 500/125mg x 3 lần/ngày",
            "pediatric_po_suspension": "20-40mg amoxicillin/kg/ngày chia 2-3 lần (tối đa 875mg/125mg)",
            "pediatric_po_tablet": "25-45mg amoxicillin/kg/ngày chia 2 lần (trên 40kg: dùng liều người lớn)",
            "adult_iv": "1000/200mg IV mỗi 8 giờ",
            "pediatric_iv": "90mg amoxicillin/kg/ngày chia 3 lần (tối đa 1000/200mg mỗi 8 giờ)",
            "notes": "Có dạng suspension cho trẻ em. Uống với thức ăn để giảm tiêu chảy"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều hoặc tăng khoảng cách",
            "under_30": "Liều thấp hơn, khoảng cách dài hơn"
        },
        "side_effects": [
            "Tiêu chảy (phổ biến)",
            "Buồn nôn",
            "Phát ban",
            "Viêm gan (hiếm nhưng nguy hiểm)",
            "Nhiễm trùng nấm Candida"
        ],
        "interactions": [
            "Warfarin: tăng INR",
            "Methotrexate: tăng độc tính methotrexate",
            "Allopurinol: tăng nguy cơ phát ban",
            "Thuốc tránh thai: có thể giảm hiệu quả"
        ],
        "pregnancy": "B - An toàn",
        "mechanism_of_action": "Amoxicillin: aminopenicillin phổ rộng, ức chế tổng hợp thành tế bào vi khuẩn bằng cách gắn với penicillin-binding proteins (PBPs). Clavulanate: beta-lactamase inhibitor, bảo vệ amoxicillin khỏi bị phân hủy bởi beta-lactamase. Kết hợp này mở rộng phổ kháng khuẩn, đặc biệt hiệu quả với H. influenzae, E. coli, và một số kỵ khí. Clavulanate không có hoạt tính kháng khuẩn riêng. Được dùng rộng rãi trong nhiễm trùng đường hô hấp, tiết niệu, da và mô mềm.",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, WBC)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Chức năng gan (ALT, AST) - tăng men gan (thường nhất thời), hiếm viêm gan (đặc biệt với clavulanate)",
            "Dấu hiệu nhiễm C. difficile",
            "Phát ban (đặc biệt ở bệnh nhân nhiễm virus như EBV)",
            "Chức năng thận (creatinine) - hiếm viêm thận kẽ"
        ],
        "precautions": [
            "Không dùng ở bệnh nhân dị ứng penicillins (phản ứng chéo cao)",
            "Nguy cơ viêm gan (đặc biệt do clavulanate) - thường nhất thời, hiếm nặng, tăng ở nam giới, dùng kéo dài",
            "Theo dõi men gan, ngừng nếu tăng nặng",
            "Phát ban thường gặp, đặc biệt ở bệnh nhân nhiễm virus (EBV, CMV) - không phải dị ứng thật",
            "Nguy cơ nhiễm C. difficile - theo dõi tiêu chảy",
            "Uống với thức ăn để giảm kích ứng dạ dày và tăng hấp thu",
            "Dùng đúng liều và đủ thời gian để tránh kháng thuốc",
            "Không dùng cho nhiễm trùng do Pseudomonas hoặc Enterococcus kháng"
        ],
        "pharmacokinetics": {
            "half_life": "1 giờ (amoxicillin và clavulanate)",
            "onset": "1-2 giờ (PO)",
            "duration": "q8h hoặc q12h tùy công thức",
            "protein_binding": "17-20% (amoxicillin), 22-30% (clavulanate)",
            "metabolism": "Một phần trong gan",
            "clearance": "Chủ yếu qua thận, cần điều chỉnh thận ở suy thận nặng"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm. Sau khi pha (suspension): bảo quản trong tủ lạnh 10 ngày, sau đó vứt bỏ.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, nguy cơ viêm gan (đặc biệt do clavulanate) có thể nặng, đặc biệt ở nam giới và dùng kéo dài. Phát ban thường gặp và có thể nhầm với dị ứng.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Amoxicillin-clavulanate có thể ảnh hưởng đến hệ vi khuẩn đường ruột, làm giảm tổng hợp vitamin K, tăng tác dụng warfarin.",
                    "effect": "Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR chặt chẽ khi bắt đầu, thay đổi liều, hoặc ngừng amoxicillin-clavulanate. Điều chỉnh liều warfarin nếu cần."
                },
                {
                    "drug": "Methotrexate",
                    "mechanism": "Amoxicillin-clavulanate ức chế bài tiết methotrexate ở ống thận, làm giảm thải trừ methotrexate.",
                    "effect": "Tăng nồng độ methotrexate, tăng độc tính (giảm bạch cầu, thiếu máu, độc gan, độc thận)",
                    "management": "TRÁNH DÙNG đồng thời nếu có thể. Nếu bắt buộc, giảm liều methotrexate, theo dõi chặt chẽ công thức máu, chức năng gan, thận. Ngừng methotrexate nếu có dấu hiệu độc tính."
                }
            ],
            "moderate": [
                {
                    "drug": "Allopurinol",
                    "mechanism": "Cơ chế chưa rõ ràng, có thể liên quan đến phản ứng miễn dịch.",
                    "effect": "Tăng nguy cơ phát ban, phản ứng dị ứng (đặc biệt phát ban maculopapular)",
                    "management": "Thận trọng khi dùng đồng thời. Theo dõi dấu hiệu phát ban. Ngừng ngay nếu có phát ban nặng hoặc phản ứng dị ứng."
                },
                {
                    "drug": "Thuốc tránh thai nội tiết",
                    "mechanism": "Amoxicillin-clavulanate có thể ảnh hưởng đến hệ vi khuẩn đường ruột, làm giảm tái hấp thu estrogen, giảm nồng độ estrogen.",
                    "effect": "Có thể giảm hiệu quả thuốc tránh thai, tăng nguy cơ mang thai",
                    "management": "Khuyến nghị sử dụng biện pháp tránh thai bổ sung (bao cao su) trong khi dùng amoxicillin-clavulanate và 7 ngày sau khi ngừng thuốc."
                },
                {
                    "drug": "Probenecid",
                    "mechanism": "Probenecid ức chế bài tiết amoxicillin ở ống thận, làm tăng nồng độ amoxicillin.",
                    "effect": "Tăng nồng độ amoxicillin, tăng tác dụng phụ",
                    "management": "Có thể dùng để tăng nồng độ amoxicillin nếu cần. Theo dõi tác dụng phụ. Giảm liều amoxicillin nếu cần."
                }
            ],
            "minor": [
                {
                    "drug": "Antacids",
                    "mechanism": "Antacids có thể giảm nhẹ hấp thu amoxicillin.",
                    "effect": "Giảm nhẹ hấp thu amoxicillin",
                    "management": "Cách 2 giờ nếu có thể. Không ảnh hưởng đáng kể ở liều điều trị thông thường."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng amoxicillin, clavulanate, hoặc các penicillin khác - phản ứng chéo cao với tất cả beta-lactam",
                "Dị ứng beta-lactam (penicillin, cephalosporin, carbapenem) - phản ứng chéo cao",
                "Viêm gan do amoxicillin-clavulanate trước đây - nguy cơ tái phát cao, có thể nặng hơn"
            ],
            "tương_đối": [
                "Dị ứng cephalosporin - phản ứng chéo 5-10%, thận trọng",
                "Suy thận nặng (CrCl <30) - cần điều chỉnh liều, tăng khoảng cách",
                "Suy gan - thận trọng, có thể giảm chuyển hóa",
                "Nhiễm virus (EBV, CMV) - tăng nguy cơ phát ban (không phải dị ứng thật)",
                "Tiền sử nhiễm C. difficile - tăng nguy cơ tái phát",
                "Dùng với methotrexate - tăng độc tính methotrexate",
                "Dùng với allopurinol - tăng nguy cơ phát ban"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Amoxicillin-clavulanate phân loại B - an toàn trong thai kỳ. Các nghiên cứu trên động vật không cho thấy nguy cơ gây dị tật thai nhi. Các nghiên cứu trên người không cho thấy nguy cơ tăng dị tật bẩm sinh. Penicillin là một trong những kháng sinh an toàn nhất trong thai kỳ. Được sử dụng rộng rãi trong thai kỳ để điều trị nhiễm trùng. Tuy nhiên, nên dùng liều thấp nhất hiệu quả và tránh dùng không cần thiết.",
            "lactation": {
                "safety": "Compatible",
                "details": "Amoxicillin và clavulanate bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ. Penicillin là một trong những kháng sinh an toàn nhất khi cho con bú.",
                "recommendation": "Có thể dùng khi cho con bú. Dùng liều thấp nhất hiệu quả. Theo dõi trẻ sơ sinh nếu dùng liều cao hoặc kéo dài (tiêu chảy, phát ban)."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Amoxicillin và clavulanate chuyển hóa một phần qua gan nhưng không đáng kể.",
            "moderate": "Thận trọng, có thể cần giảm liều nhẹ. Chuyển hóa có thể giảm ở suy gan trung bình, nhưng thải trừ chủ yếu qua thận nên ít ảnh hưởng.",
            "severe": "Thận trọng, có thể cần giảm liều. Chuyển hóa có thể giảm ở suy gan nặng, nhưng thải trừ chủ yếu qua thận nên ít ảnh hưởng. Tuy nhiên, suy gan nặng có thể kèm theo suy thận, nên cần điều chỉnh liều theo chức năng thận.",
            "notes": "Amoxicillin và clavulanate chuyển hóa một phần qua gan nhưng thải trừ chủ yếu qua thận (60-70% bài tiết nguyên dạng qua nước tiểu). Suy gan có thể giảm chuyển hóa nhẹ nhưng không đáng kể. Tuy nhiên, nguy cơ viêm gan do clavulanate tăng ở bệnh nhân có bệnh gan, đặc biệt nam giới và dùng kéo dài. Theo dõi chặt chẽ chức năng gan."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng tiêu hóa: Buồn nôn, nôn, tiêu chảy, đau bụng",
                "Triệu chứng thần kinh: Kích động, co giật (hiếm, thường ở liều rất cao)",
                "Triệu chứng thận: Tăng creatinine, suy thận cấp (hiếm)",
                "Triệu chứng da: Phát ban, mày đay",
                "Triệu chứng gan: Tăng men gan, viêm gan (đặc biệt với clavulanate)",
                "Triệu chứng nghiêm trọng: Co giật, suy thận cấp, viêm gan nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.",
            "treatment": [
                "Ngừng ngay amoxicillin-clavulanate",
                "Rửa dạ dày hoặc than hoạt nếu uống trong vòng 1-2 giờ (nếu không có chống chỉ định)",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2",
                "Điều trị triệu chứng tiêu hóa:",
                "  - Chống nôn nếu cần",
                "  - Truyền dịch nếu mất nước",
                "  - Theo dõi điện giải",
                "Điều trị co giật nếu có:",
                "  - Benzodiazepine (diazepam, lorazepam)",
                "  - Theo dõi hô hấp",
                "Điều trị tăng men gan/viêm gan nếu có:",
                "  - Theo dõi ALT, AST, bilirubin",
                "  - Điều trị hỗ trợ gan",
                "  - Nếu viêm gan nặng: điều trị suy gan",
                "Điều trị suy thận cấp nếu có:",
                "  - Theo dõi creatinine, BUN, lượng nước tiểu",
                "  - Điều trị suy thận cấp",
                "Lọc máu (hemodialysis) có thể loại bỏ một phần amoxicillin nhưng không được khuyến nghị thường quy",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, chức năng gan (ALT, AST, bilirubin), chức năng thận (creatinine, BUN, lượng nước tiểu), dấu hiệu da trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có biến chứng (suy gan, suy thận, co giật)."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn để giảm kích ứng dạ dày, giảm tiêu chảy, và tăng hấp thu. Có thể uống không thức ăn nếu cần nhưng không khuyến nghị.",
                "timing": "Uống 2-3 lần/ngày tùy công thức (875/125mg x 2 lần/ngày hoặc 500/125mg x 3 lần/ngày). Uống đều đặn, cách đều nhau trong ngày. Không bỏ liều."
            },
            "iv": {
                "reconstitution": "Pha theo hướng dẫn nhà sản xuất. Thường pha với nước cất vô trùng hoặc NaCl 0.9%. Lắc kỹ để hòa tan hoàn toàn.",
                "infusion_rate": "Truyền IV trong 30 phút (không truyền nhanh hơn). Có thể truyền trong 15-20 phút nếu cần nhưng không khuyến nghị.",
                "compatibility": [
                    "NaCl 0.9%",
                    "D5W (Dextrose 5%)",
                    "Lactated Ringer's (LR) - thận trọng, kiểm tra tương thích",
                    "Nước cất vô trùng"
                ],
                "incompatibility": [
                    "Không trộn với các thuốc khác trong cùng một bơm tiêm hoặc chai truyền",
                    "Aminoglycosides (mất hoạt tính nếu trộn trực tiếp)",
                    "Probenecid (không trộn, dùng riêng)"
                ],
                "notes": "Truyền IV trong 30 phút. Không truyền nhanh hơn. Theo dõi phản ứng tại chỗ tiêm (viêm tĩnh mạch). Dùng ngay sau khi pha. Không bảo quản lâu sau khi pha."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Label: Augmentin (amoxicillin-clavulanate)",
                "UpToDate: Amoxicillin-clavulanate drug information",
                "Lexicomp: Amoxicillin-clavulanate monograph",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
                "Sanford Guide to Antimicrobial Therapy"
            ],
            "last_updated": "2025-02-03",
            "evidence_level": "Level 1 - FDA approved, multiple clinical trials, extensive clinical experience"
        }
    },

    "Amoxicillin suspension": {
        "group": "Antibiotic - Beta-lactam (Penicillin)",
        "vietnamese_name": "Amoxicillin suspension, Amoxicillin sirô",
        "administration": ["PO"],
        "indications": [
            "Nhiễm khuẩn đường hô hấp",
            "Nhiễm khuẩn tai mũi họng",
            "Nhiễm khuẩn đường tiết niệu",
            "Nhiễm khuẩn da mô mềm",
            "Helicobacter pylori (phối hợp)"
        ],
        "contraindications": [
            "Dị ứng penicillin",
            "Dị ứng beta-lactam"
        ],
        "dosage": {
            "pediatric_otitis": "80-90mg/kg/ngày chia 2 lần (10 ngày)",
            "pediatric_pneumonia": "80-100mg/kg/ngày chia 3-4 lần",
            "pediatric_uti": "25-50mg/kg/ngày chia 3 lần",
            "pediatric_suspension_common": "20-40mg/kg/ngày chia 2-3 lần",
            "notes": "Có dạng suspension 125mg/5ml, 250mg/5ml cho trẻ em. Uống với hoặc không thức ăn"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều hoặc tăng khoảng cách",
            "under_30": "Liều thấp hơn, khoảng cách dài hơn"
        },
        "side_effects": [
            "Tiêu chảy",
            "Buồn nôn",
            "Phát ban",
            "Nhiễm trùng nấm Candida",
            "Giảm bạch cầu (hiếm)"
        ],
        "interactions": [
            "Warfarin: tăng INR",
            "Methotrexate: tăng độc tính",
            "Allopurinol: tăng nguy cơ phát ban",
            "Thuốc tránh thai: có thể giảm hiệu quả"
        ],
        "pregnancy": "B - An toàn",
        "mechanism_of_action": "Amoxicillin là aminopenicillin (beta-lactam antibiotic), ức chế tổng hợp thành tế bào vi khuẩn bằng cách gắn với penicillin-binding proteins (PBPs) trên màng tế bào vi khuẩn. Amoxicillin là chất tương tự penicillin nhưng có nhóm amin, giúp tăng khả năng xuyên qua màng ngoài của vi khuẩn Gram-âm và tăng phổ kháng khuẩn. Amoxicillin ức chế enzyme transpeptidase, ngăn chặn liên kết chéo giữa các chuỗi peptidoglycan trong thành tế bào vi khuẩn, dẫn đến làm suy yếu và vỡ thành tế bào khi vi khuẩn phân chia. Amoxicillin có phổ kháng khuẩn rộng: Gram-dương (Streptococcus, Enterococcus, một số Staphylococcus không kháng penicillinase), Gram-âm (H. influenzae, E. coli, Proteus mirabilis, Salmonella, Shigella), và một số kỵ khí. Không hiệu quả với vi khuẩn tiết beta-lactamase (cần kết hợp với clavulanate). Dạng suspension phù hợp cho trẻ em, dễ uống và hấp thu tốt.",
        "monitoring": [
            "Dấu hiệu nhiễm trùng: sốt, WBC, CRP (theo dõi đáp ứng điều trị)",
            "Cấy máu và cấy từ vị trí nhiễm trùng (nếu có) để đánh giá hiệu quả",
            "Dấu hiệu dị ứng: phát ban, mề đay, khó thở, sốc phản vệ (đặc biệt ở lần đầu tiên dùng)",
            "Tiêu chảy (phổ biến, có thể là nhiễm C. difficile nếu nặng)",
            "Chức năng thận (creatinine) nếu dùng liều cao hoặc suy thận",
            "Dấu hiệu nhiễm C. difficile: tiêu chảy nặng, đau bụng, sốt (cần ngừng và điều trị)",
            "Chức năng gan (ALT, AST) nếu có triệu chứng (hiếm)",
            "Công thức máu (giảm bạch cầu, thiếu máu hiếm)",
            "INR nếu dùng với warfarin (tăng nguy cơ chảy máu)"
        ],
        "precautions": [
            "Không dùng ở bệnh nhân dị ứng penicillin hoặc beta-lactam (phản ứng chéo với cephalosporin ~5-10%)",
            "Lắc kỹ suspension trước khi dùng (thuốc lắng xuống đáy)",
            "Có thể uống với hoặc không thức ăn (hấp thu tốt)",
            "Dùng đủ liều và đủ thời gian (thường 7-10 ngày) để tránh kháng thuốc",
            "Thận trọng ở bệnh nhân suy thận (giảm liều hoặc tăng khoảng cách)",
            "Thận trọng ở bệnh nhân có tiền sử nhiễm C. difficile (tăng nguy cơ tái phát)",
            "Thận trọng với allopurinol (tăng nguy cơ phát ban)",
            "Thận trọng với methotrexate (amoxicillin làm giảm thải trừ methotrexate, tăng độc tính)",
            "Có thể giảm hiệu quả thuốc tránh thai (dùng biện pháp dự phòng)",
            "Theo dõi tiêu chảy - nếu nặng hoặc kéo dài, có thể là nhiễm C. difficile",
            "Dùng đúng liều theo cân nặng ở trẻ em (tính theo mg/kg)"
        ],
        "pharmacokinetics": {
            "half_life": "1-1.5 giờ",
            "onset": "1-2 giờ (đạt nồng độ đỉnh trong máu)",
            "duration": "6-8 giờ (dùng 2-3 lần/ngày)",
            "protein_binding": "20%",
            "clearance": "Thận: bài tiết chủ yếu qua nước tiểu (không thay đổi, 60-70% trong 6-8 giờ). Một phần nhỏ qua mật. Hấp thu tốt qua đường uống (75-90%), không bị ảnh hưởng bởi thức ăn. Dạng suspension hấp thu tương tự viên nén."
        },
        "storage": "Bảo quản suspension ở nhiệt độ phòng (15-30°C) hoặc trong tủ lạnh (2-8°C) - theo hướng dẫn trên nhãn. Lắc kỹ trước khi dùng. Sau khi pha (nếu là bột pha nước): bảo quản trong tủ lạnh (2-8°C), dùng trong vòng 7-14 ngày (theo hướng dẫn). Tránh đông lạnh. Để nơi khô ráo, tránh ánh sáng trực tiếp, tránh xa tầm tay trẻ em.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "Methotrexate",
                    "mechanism": "Amoxicillin làm giảm thải trừ methotrexate qua thận, tăng nồng độ methotrexate.",
                    "effect": "Tăng độc tính methotrexate (giảm bạch cầu, độc gan, độc thận, viêm niêm mạc)",
                    "management": "Tránh dùng cùng nếu có thể. Nếu bắt buộc, theo dõi công thức máu, chức năng gan, thận chặt chẽ. Có thể cần giảm liều methotrexate."
                },
                {
                    "drug": "Allopurinol",
                    "mechanism": "Cơ chế chưa rõ ràng, nhưng allopurinol làm tăng nguy cơ phản ứng da nghiêm trọng với amoxicillin.",
                    "effect": "Tăng nguy cơ phát ban nghiêm trọng, SJS, TEN (đe dọa tính mạng)",
                    "management": "Tránh dùng cùng nếu có thể. Nếu bắt buộc, theo dõi sát dấu hiệu phát ban. Ngừng ngay nếu có phát ban."
                }
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Amoxicillin có thể ảnh hưởng đến hệ vi khuẩn đường ruột, ảnh hưởng đến chuyển hóa vitamin K, tăng tác dụng warfarin.",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên khi dùng amoxicillin. Điều chỉnh liều warfarin nếu cần."
                },
                {
                    "drug": "Thuốc tránh thai (estrogen)",
                    "mechanism": "Amoxicillin có thể ảnh hưởng đến hệ vi khuẩn đường ruột, giảm tái hấp thu estrogen, giảm hiệu quả thuốc tránh thai.",
                    "effect": "Giảm hiệu quả thuốc tránh thai, tăng nguy cơ có thai",
                    "management": "Dùng biện pháp tránh thai dự phòng (bao cao su) trong thời gian dùng amoxicillin và 7 ngày sau."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng penicillin - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI (phản ứng chéo với cephalosporin ~5-10%)",
                "Dị ứng beta-lactam",
                "Sốc phản vệ với penicillin trước đây"
            ],
            "tương_đối": [
                "Dị ứng cephalosporin - thận trọng (phản ứng chéo ~5-10%)",
                "Nhiễm C. difficile trước đây - tăng nguy cơ tái phát",
                "Suy thận nặng - giảm liều hoặc tăng khoảng cách",
                "Đang dùng methotrexate - tăng độc tính methotrexate",
                "Đang dùng allopurinol - tăng nguy cơ phát ban"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Amoxicillin là category B - an toàn trong thai kỳ. Penicillin là một trong những kháng sinh an toàn nhất trong thai kỳ. Không có bằng chứng về dị tật thai nhi. Có thể dùng trong tất cả các tam cá nguyệt.",
            "lactation": {
                "safety": "Compatible",
                "details": "Amoxicillin bài tiết vào sữa mẹ ở nồng độ thấp. An toàn cho trẻ bú mẹ. Có thể gây tiêu chảy nhẹ hoặc phát ban ở trẻ, nhưng hiếm.",
                "recommendation": "Có thể dùng khi cho con bú. An toàn cho trẻ bú mẹ. Theo dõi dấu hiệu tiêu chảy hoặc phát ban ở trẻ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Amoxicillin chủ yếu thải qua thận, không chuyển hóa ở gan.",
            "moderate": "Không cần điều chỉnh liều. Amoxicillin chủ yếu thải qua thận.",
            "severe": "Không cần điều chỉnh liều. Amoxicillin chủ yếu thải qua thận.",
            "notes": "Amoxicillin chủ yếu thải qua thận (60-70% trong 6-8 giờ), không chuyển hóa ở gan. Suy gan không ảnh hưởng đến nồng độ amoxicillin."
        },
        "overdose_management": {
            "symptoms": [
                "Tiêu chảy nặng (có thể là nhiễm C. difficile)",
                "Buồn nôn, nôn",
                "Phát ban, mề đay",
                "Sốc phản vệ (hiếm nhưng nguy hiểm)",
                "Co giật (với liều rất cao, suy thận)",
                "Rối loạn điện giải (natri cao nếu dùng liều lớn)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng amoxicillin ngay lập tức",
                "Nếu sốc phản vệ: epinephrine, corticosteroids, antihistamines, hỗ trợ hô hấp",
                "Nếu tiêu chảy nặng: điều trị C. difficile nếu xác định (metronidazole, vancomycin)",
                "Nếu co giật: benzodiazepines (diazepam, lorazepam)",
                "Điều chỉnh điện giải nếu cần",
                "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "Theo dõi dấu hiệu sinh tồn"
            ],
            "monitoring": "Dấu hiệu sinh tồn, dấu hiệu dị ứng, tiêu chảy, điện giải, dấu hiệu nhiễm C. difficile"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Hấp thu tốt, không bị ảnh hưởng bởi thức ăn. Uống với thức ăn có thể giảm kích ứng dạ dày.",
                "timing": "Uống 2-3 lần/ngày tùy chỉ định, cách đều. Lắc kỹ suspension trước khi dùng (thuốc lắng xuống đáy). Dùng đúng liều theo cân nặng ở trẻ em (tính theo mg/kg)."
            },
            "iv": {
                "reconstitution": "N/A - chỉ có dạng uống",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống (suspension)"
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Amoxicillin",
                "UpToDate - Amoxicillin: Drug Information",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
            ],
            "last_updated": "2025-02-04",
            "evidence_level": "A - Dựa trên FDA drug labels và dữ liệu lâm sàng"
        }
    },

    "Ceftriaxone": {
        "group": "Antibiotic - Cephalosporin (3rd Generation)",
        "vietnamese_name": "Ceftriaxone, Rocephin",
        "administration": ["IV", "IM"],
        "indications": [
            "Nhiễm khuẩn nặng",
            "Viêm màng não",
            "Nhiễm khuẩn bệnh viện",
            "Nhiễm khuẩn đường tiết niệu",
            "Viêm phổi"
        ],
        "contraindications": [
            "Dị ứng cephalosporin hoặc penicillin (thận trọng)",
            "Trẻ sơ sinh <28 ngày với Ca IV"
        ],
        "dosage": {
            "adult_standard": "1-2g IV/IM mỗi 24 giờ",
            "adult_severe": "2-4g IV mỗi 24 giờ",
            "adult_meningitis": "2g IV mỗi 12 giờ",
            "pediatric_standard": "50-75mg/kg IV/IM mỗi 24 giờ (tối đa 2g)",
            "pediatric_meningitis": "80-100mg/kg IV mỗi 12-24 giờ (tối đa 4g/ngày)",
            "notes": "Thời gian bán hủy dài, dùng 1 lần/ngày. Có thể gây kết tủa với Ca ở trẻ sơ sinh"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi (thải qua mật)",
            "under_30": "Giảm liều nếu CrCl <10 và suy gan"
        },
        "side_effects": [
            "Tiêu chảy",
            "Phát ban",
            "Tăng transaminase",
            "Viêm túi mật (hiếm)",
            "Giảm bạch cầu (hiếm)",
            "Sỏi mật (với liều cao dài ngày)"
        ],
        "interactions": [
            "Warfarin: tăng INR",
            "Calcium IV: kết tủa (trẻ sơ sinh)",
            "Probenecid: tăng nồng độ ceftriaxone"
        ],
        "pregnancy": "B - An toàn",
        "mechanism_of_action": "Cephalosporin thế hệ 3, phổ rộng. Ức chế tổng hợp thành tế bào vi khuẩn bằng cách gắn với penicillin-binding proteins (PBPs). Phổ kháng khuẩn: Gram-dương (một số), Gram-âm mạnh (Enterobacteriaceae, Neisseria, H. influenzae), và một số kỵ khí. Kháng được nhiều beta-lactamase do có cấu trúc vòng beta-lactam bền vững. Không hiệu quả với Pseudomonas aeruginosa, Enterococcus, hoặc MRSA. Thời gian bán thải dài (6-9 giờ) → chỉ cần tiêm 1 lần/ngày.",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, WBC, CRP)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Chức năng gan (ALT, AST, bilirubin) - có thể tăng, hiếm sỏi mật",
            "Sỏi mật (ceftriaxone-calcium complex) - đặc biệt ở trẻ em, dùng liều cao",
            "Chức năng thận (creatinine) - không cần điều chỉnh thận nhưng theo dõi",
            "Dấu hiệu nhiễm C. difficile",
            "Co giật (hiếm, nhưng có thể ở suy thận nặng)",
            "Phản ứng tại chỗ tiêm (đau, viêm tĩnh mạch)"
        ],
        "precautions": [
            "KHÔNG dùng ở trẻ sơ sinh < 28 ngày tuổi nếu đang dùng calci IV (nguy cơ kết tủa ceftriaxone-calcium trong phổi, thận) - có thể tử vong",
            "Nguy cơ sỏi mật (ceftriaxone-calcium complex) - đặc biệt ở trẻ em, dùng liều cao, dùng kéo dài",
            "Không dùng ở bệnh nhân dị ứng penicillins hoặc cephalosporins (phản ứng chéo ~5-10%)",
            "Nguy cơ nhiễm C. difficile - theo dõi tiêu chảy",
            "Có thể gây tăng bilirubin (nhất thời, do đẩy bilirubin khỏi albumin)",
            "Pha trong NS, D5W, hoặc LR, tiêm IV hoặc IM",
            "Tiêm IM: pha với lidocaine 1% để giảm đau",
            "Không pha trộn với các thuốc khác (tương kỵ với nhiều thuốc, đặc biệt vancomycin, calcium)",
            "Thời gian bán thải dài → chỉ cần 1 lần/ngày (trừ viêm màng não: q12h)"
        ],
        "pharmacokinetics": {
            "half_life": "6-9 giờ (rất dài cho cephalosporin)",
            "onset": "Ngay lập tức sau khi tiêm IV",
            "duration": "24 giờ (liều 1-2g q24h), 12 giờ (viêm màng não: 2g q12h)",
            "protein_binding": "85-95% (rất cao)",
            "metabolism": "Không chuyển hóa, bài tiết nguyên dạng",
            "clearance": "40% qua thận, 60% qua mật (độc nhất trong cephalosporin) → không cần điều chỉnh thận"
        },
        "storage": "Bảo quản bột khô ở nhiệt độ phòng (20-25°C). Sau khi pha: bảo quản ở nhiệt độ phòng 24 giờ, hoặc trong tủ lạnh 10 ngày. Không đông lạnh.",
        "black_box_warnings": "KHÔNG dùng ở trẻ sơ sinh < 28 ngày tuổi nếu đang dùng calci IV - có thể gây kết tủa ceftriaxone-calcium trong phổi, thận, có thể tử vong. Tránh dùng calci IV trong 48 giờ sau liều ceftriaxone cuối cùng ở trẻ sơ sinh.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Calcium IV (đặc biệt ở trẻ sơ sinh < 28 ngày)",
                    "mechanism": "Ceftriaxone tạo phức hợp không hòa tan với calci, gây kết tủa ceftriaxone-calcium trong phổi, thận, có thể tử vong.",
                    "effect": "Kết tủa ceftriaxone-calcium trong phổi, thận, có thể tử vong (đặc biệt ở trẻ sơ sinh)",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI: Không dùng ceftriaxone ở trẻ sơ sinh < 28 ngày nếu đang dùng calci IV. Tránh dùng calci IV trong 48 giờ sau liều ceftriaxone cuối cùng ở trẻ sơ sinh. Ở người lớn, tránh pha chung trong cùng một ống truyền, truyền riêng biệt."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Ceftriaxone có thể ức chế tổng hợp vitamin K phụ thuộc vào hệ vi khuẩn đường ruột, làm giảm sản xuất các yếu tố đông máu phụ thuộc vitamin K. Ngoài ra, có thể đẩy warfarin khỏi albumin (protein binding cao).",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên (ít nhất 2-3 lần/tuần khi bắt đầu dùng ceftriaxone). Có thể cần giảm liều warfarin. Đặc biệt thận trọng ở bệnh nhân suy gan, dùng kéo dài (>7 ngày)."
                }
            ],
            "moderate": [
                {
                    "drug": "Probenecid",
                    "mechanism": "Probenecid ức chế bài tiết ống thận của ceftriaxone, làm giảm thải trừ và tăng nồng độ ceftriaxone.",
                    "effect": "Tăng nồng độ ceftriaxone, tăng thời gian bán thải",
                    "management": "Có thể cần giảm liều ceftriaxone. Theo dõi chức năng thận. Thường không cần điều chỉnh liều thường quy do ceftriaxone thải trừ chủ yếu qua mật."
                },
                {
                    "drug": "Vancomycin",
                    "mechanism": "Có thể tạo kết tủa khi pha chung. Cả hai đều có thể gây độc thận, tác dụng cộng dồn.",
                    "effect": "Kết tủa khi pha chung, tăng nguy cơ độc thận",
                    "management": "Không pha chung. Truyền riêng biệt. Theo dõi chức năng thận chặt chẽ. Theo dõi nồng độ vancomycin nếu có thể."
                },
                {
                    "drug": "Aminoglycosides (Gentamicin, Tobramycin, Amikacin)",
                    "mechanism": "Có thể tạo kết tủa khi pha chung. Cả hai đều có thể gây độc thận, tác dụng cộng dồn.",
                    "effect": "Kết tủa khi pha chung, tăng nguy cơ độc thận",
                    "management": "Không pha chung. Truyền riêng biệt. Theo dõi chức năng thận chặt chẽ."
                }
            ],
            "minor": [
                {
                    "drug": "Thuốc tránh thai đường uống",
                    "mechanism": "Kháng sinh phổ rộng có thể làm giảm hệ vi khuẩn đường ruột, làm giảm tái hấp thu estrogen từ đường ruột.",
                    "effect": "Giảm hiệu quả thuốc tránh thai (hiếm, nhưng có thể xảy ra)",
                    "management": "Khuyến cáo sử dụng biện pháp tránh thai bổ sung (bao cao su) trong khi dùng kháng sinh và 7 ngày sau khi ngừng."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng cephalosporin hoặc beta-lactam (phản ứng type I - sốc phản vệ, phù mạch, phát ban nặng)",
                "Trẻ sơ sinh < 28 ngày tuổi đang dùng calci IV - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI (nguy cơ kết tủa tử vong)"
            ],
            "tương_đối": [
                "Dị ứng penicillin (phản ứng chéo ~5-10%) - thận trọng, có thể dùng nếu phản ứng nhẹ",
                "Suy gan nặng kèm suy thận (CrCl <10) - cần giảm liều",
                "Tiền sử nhiễm C. difficile - tăng nguy cơ tái phát",
                "Rối loạn đông máu - tăng nguy cơ chảy máu khi dùng với warfarin",
                "Sỏi mật - tăng nguy cơ sỏi mật (ceftriaxone-calcium complex), đặc biệt ở trẻ em, dùng liều cao"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Ceftriaxone là thuốc phân loại B. Các nghiên cứu trên động vật không cho thấy nguy cơ dị tật bẩm sinh, nhưng không có nghiên cứu đầy đủ trên phụ nữ có thai. Cephalosporins nói chung được coi là an toàn trong thai kỳ và được sử dụng rộng rãi. Ceftriaxone có thể được dùng khi lợi ích vượt quá nguy cơ, đặc biệt trong nhiễm khuẩn nặng như viêm màng não. Tuy nhiên, cần thận trọng với nguy cơ sỏi mật và tương tác với calci. Nên tránh dùng kéo dài nếu có thể.",
            "lactation": {
                "safety": "Compatible",
                "details": "Ceftriaxone bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ. Cephalosporins nói chung được coi là an toàn khi cho con bú.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ sơ sinh về dấu hiệu tiêu chảy, phát ban, hoặc các tác dụng phụ khác. Dùng liều thấp nhất hiệu quả."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Ceftriaxone thải trừ 40% qua thận, 60% qua mật, không chuyển hóa qua gan.",
            "moderate": "Không cần điều chỉnh liều. Tuy nhiên, cần thận trọng với nguy cơ tăng bilirubin (nhất thời, do đẩy bilirubin khỏi albumin).",
            "severe": "Không cần điều chỉnh liều. Tuy nhiên, nếu kèm theo suy thận nặng (CrCl <10), có thể cần giảm liều. Theo dõi bilirubin và chức năng gan.",
            "notes": "Ceftriaxone không chuyển hóa qua gan, thải trừ 40% qua thận và 60% qua mật (độc nhất trong cephalosporin). Không cần điều chỉnh liều ở bệnh nhân suy gan. Tuy nhiên, suy gan nặng có thể kèm theo suy thận, nên cần điều chỉnh liều theo chức năng thận nếu CrCl <10. Ngoài ra, ceftriaxone có protein binding cao (85-95%), có thể đẩy bilirubin khỏi albumin, gây tăng bilirubin nhất thời."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng thần kinh: Co giật, rối loạn ý thức (hiếm, thường chỉ với liều rất cao hoặc suy thận nặng)",
                "Triệu chứng gan: Tăng bilirubin, tăng transaminase (nhất thời)",
                "Triệu chứng sỏi mật: Đau bụng, buồn nôn, nôn (do kết tủa ceftriaxone-calcium)",
                "Triệu chứng thận: Suy thận cấp (hiếm với liều thông thường)",
                "Triệu chứng tiêu hóa: Tiêu chảy nặng, buồn nôn, nôn",
                "Triệu chứng dị ứng: Phát ban, phù mạch, sốc phản vệ (nếu dị ứng)",
                "Triệu chứng chảy máu: Chảy máu kéo dài, tăng INR (khi dùng với warfarin)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.",
            "treatment": [
                "Ngừng ngay ceftriaxone",
                "Điều trị co giật nếu có: Benzodiazepine (diazepam, lorazepam), phenobarbital",
                "Điều trị sỏi mật nếu có:",
                "  - Giảm đau: NSAID hoặc opioid",
                "  - Bù dịch đầy đủ",
                "  - Theo dõi siêu âm bụng",
                "  - Có thể cần can thiệp nếu tắc nghẽn",
                "Điều trị chảy máu nếu có:",
                "  - Bổ sung vitamin K nếu giảm prothrombin",
                "  - Truyền huyết tương tươi đông lạnh (FFP) nếu chảy máu nặng",
                "  - Điều chỉnh liều warfarin nếu đang dùng",
                "Điều trị suy thận cấp nếu có:",
                "  - Bù dịch đầy đủ",
                "  - Điều chỉnh điện giải",
                "  - Lọc máu nếu cần (hemodialysis có thể loại bỏ ceftriaxone một phần)",
                "Điều trị dị ứng nếu có:",
                "  - Epinephrine nếu sốc phản vệ",
                "  - Antihistamine, corticosteroid",
                "  - Hỗ trợ hô hấp nếu cần",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2",
                "Lọc máu: Hemodialysis có thể loại bỏ ceftriaxone một phần (40% thải qua thận), nhưng không hiệu quả bằng các cephalosporin khác do thải trừ chủ yếu qua mật."
            ],
            "monitoring": "Theo dõi dấu hiệu thần kinh (co giật, ý thức), chức năng gan (bilirubin, ALT, AST), dấu hiệu sỏi mật (đau bụng), chức năng thận (creatinine, BUN, lượng nước tiểu), PT/INR (nếu dùng với warfarin), dấu hiệu chảy máu, dấu hiệu sinh tồn trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có suy thận cấp hoặc sỏi mật."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Không áp dụng - chỉ có dạng IV và IM",
                "timing": "Không áp dụng - chỉ có dạng IV và IM"
            },
            "iv": {
                "reconstitution": "Pha với NS (0.9% NaCl), D5W (5% Dextrose), hoặc Ringer's Lactate. Nồng độ pha: 10-40mg/ml. Pha 1g trong 10ml = 100mg/ml (quá đậm, không dùng). Pha 1g trong 50ml = 20mg/ml. Pha 2g trong 50ml = 40mg/ml. Lắc kỹ để hòa tan hoàn toàn. KHÔNG pha với calci IV.",
                "infusion_rate": "Truyền IV trong 30 phút. Tốc độ: 50ml/30 phút = ~1.7ml/phút. Có thể truyền nhanh hơn (bolus) nếu cần, nhưng thường truyền trong 30 phút để giảm đau tại chỗ.",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)", "Ringer's Lactate"],
                "incompatibility": [
                    "Calcium IV - KHÔNG pha chung, nguy cơ kết tủa tử vong (đặc biệt ở trẻ sơ sinh)",
                    "Vancomycin - tạo kết tủa, không pha chung",
                    "Aminoglycosides - có thể tạo kết tủa, truyền riêng biệt",
                    "Amphotericin B - không tương thích",
                    "Các thuốc có tính kiềm hoặc acid mạnh"
                ],
                "notes": "QUAN TRỌNG: 1) KHÔNG pha chung với calci IV (nguy cơ kết tủa tử vong ở trẻ sơ sinh), 2) Không pha chung với vancomycin hoặc aminoglycosides, 3) Thời gian bán thải dài (6-9 giờ) → chỉ cần 1 lần/ngày (trừ viêm màng não: q12h), 4) Tiêm IM: pha với lidocaine 1% để giảm đau, 5) Theo dõi sỏi mật ở trẻ em, dùng liều cao, dùng kéo dài."
            },
            "im": {
                "reconstitution": "Pha với lidocaine 1% (không có epinephrine) để giảm đau. Nồng độ pha: 250mg/ml (1g trong 3.5ml lidocaine 1%). Pha 1g trong 3.5ml lidocaine 1% = 250mg/ml. Lắc kỹ để hòa tan hoàn toàn.",
                "injection_site": "Tiêm sâu vào cơ (gluteus maximus hoặc vastus lateralis). Tránh tiêm vào mạch máu.",
                "notes": "Pha với lidocaine 1% để giảm đau tại chỗ. Tiêm sâu vào cơ. Có thể gây đau tại chỗ, nhưng thường nhẹ khi pha với lidocaine."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Ceftriaxone (Rocephin)",
                "UpToDate - Ceftriaxone: Drug Information",
                "Medscape - Ceftriaxone Drug Reference",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
                "Lexicomp Online - Ceftriaxone Monograph",
                "Micromedex - Ceftriaxone Drug Information",
                "IDSA Guidelines - Community-Acquired Pneumonia, Meningitis"
            ],
            "last_updated": "2025-02-03",
            "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },

}

__all__ = ['INFECTIOUS_OTHER_DRUGS']
