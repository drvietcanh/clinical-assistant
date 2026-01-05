"""
Ophthalmology Drugs - Mydriatics
"""
from typing import Dict, Any


MYDRIATICS_DRUGS: Dict[str, Dict[str, Any]] = {
        "Atropine eye drops": {
            "group": "Ophthalmology - Cycloplegic/Mydriatic (Long-acting)",
            "vietnamese_name": "Atropine, Atropisol",
            "administration": ["Ophthalmic"],
            "indications": [
                "Giãn đồng tử (mydriasis) và liệt điều tiết (cycloplegia) cho khám mắt",
                "Điều trị viêm màng bồ đào (uveitis) - giảm đau, giảm dính mống mắt",
                "Điều trị viêm mống mắt (iritis)",
                "Điều trị viêm màng bồ đào trước (anterior uveitis)",
                "Dự phòng dính mống mắt (posterior synechiae) trong viêm màng bồ đào",
                "Điều trị nhược thị (amblyopia) ở trẻ em - bịt mắt tốt",
                "Điều trị co thắt điều tiết (accommodative spasm)"
            ],
            "contraindications": [
                "Dị ứng atropine hoặc anticholinergic",
                "Glaucoma góc đóng (narrow-angle glaucoma) - CHỐNG CHỈ ĐỊNH",
                "Glaucoma góc mở với góc hẹp - CHỐNG CHỈ ĐỊNH",
                "Trẻ em <3 tháng tuổi - thận trọng (tăng nhạy cảm)",
                "Bệnh nhược cơ (myasthenia gravis) - thận trọng",
                "Bệnh đường tiêu hóa nặng (tắc nghẽn) - thận trọng"
            ],
            "dosage": {
                "adult_mydriasis_cycloplegia": "1 giọt vào mắt bị ảnh hưởng x 1-3 lần/ngày tùy chỉ định",
                "adult_uveitis": "1 giọt vào mắt bị ảnh hưởng x 2-3 lần/ngày",
                "pediatric_amblyopia": "1 giọt vào mắt tốt x 1 lần/ngày để làm mờ mắt tốt, buộc mắt yếu phải làm việc",
                "notes": "Atropine là anticholinergic, gây giãn đồng tử (mydriasis) và liệt điều tiết (cycloplegia) kéo dài (7-14 ngày). CHỐNG CHỈ ĐỊNH ở glaucoma góc đóng. Có thể hấp thu toàn thân và gây tác dụng phụ hệ thống (khô miệng, nhịp nhanh, bí tiểu, lú lẫn ở người cao tuổi)."
            },
            "renal_adjustment": {
                "normal": "Không đổi",
                "30_60": "Không cần điều chỉnh đáng kể",
                "under_30": "Không cần điều chỉnh đáng kể"
            },
            "side_effects": [
                "Nhìn mờ kéo dài (7-14 ngày) - phổ biến",
                "Nhạy cảm với ánh sáng (photophobia) - phổ biến",
                "Kích ứng mắt (đỏ, rát) - phổ biến",
                "Hấp thu toàn thân: khô miệng - phổ biến",
                "Hấp thu toàn thân: nhịp tim nhanh - phổ biến",
                "Hấp thu toàn thân: bí tiểu - hiếm nhưng nghiêm trọng",
                "Hấp thu toàn thân: lú lẫn, mê sảng (ở người cao tuổi) - hiếm nhưng nghiêm trọng",
                "Hấp thu toàn thân: sốt (ở trẻ em) - hiếm nhưng nghiêm trọng",
                "Hấp thu toàn thân: co thắt phế quản (hen) - hiếm",
                "Tăng nhãn áp (nếu có glaucoma góc đóng) - NGUY HIỂM"
            ],
            "interactions": [
                "Thuốc kháng cholinergic khác: tăng nguy cơ tác dụng phụ",
                "Thuốc gây QT kéo dài: tăng nguy cơ rối loạn nhịp tim",
                "Thuốc ức chế acetylcholinesterase (neostigmine, pyridostigmine): đối kháng tác dụng"
            ],
            "pregnancy": "C - Thận trọng",
            "mechanism_of_action": "Atropine là anticholinergic (muscarinic receptor antagonist). Ức chế muscarinic receptors trong cơ trơn mống mắt (iris sphincter) và cơ thể mi (ciliary muscle), dẫn đến: (1) Giãn đồng tử (mydriasis) - ức chế cơ co đồng tử, (2) Liệt điều tiết (cycloplegia) - ức chế cơ thể mi, mất khả năng điều tiết, (3) Giảm đau trong viêm màng bồ đào (giảm co thắt cơ), (4) Dự phòng dính mống mắt (giữ đồng tử giãn). Atropine có tác dụng kéo dài (7-14 ngày) do thời gian bán thải dài. ĐẶC ĐIỂM: (1) Tác dụng kéo dài (7-14 ngày), (2) CHỐNG CHỈ ĐỊNH ở glaucoma góc đóng, (3) Có thể hấp thu toàn thân và gây tác dụng phụ hệ thống, (4) Nhìn mờ kéo dài - bệnh nhân không nên lái xe, (5) Nhạy cảm với ánh sáng - cần đeo kính râm, (6) Lú lẫn, mê sảng ở người cao tuổi - cần theo dõi sát.",
            "monitoring": [
                "Nhãn áp (intraocular pressure - IOP) - QUAN TRỌNG (nguy cơ tăng nhãn áp nếu có glaucoma góc đóng)",
                "Thị lực (nhìn mờ kéo dài)",
                "Dấu hiệu kích ứng mắt (đỏ, rát)",
                "Dấu hiệu hấp thu toàn thân: khô miệng, nhịp tim nhanh, bí tiểu, lú lẫn",
                "Ở trẻ em: dấu hiệu sốt, khô miệng nặng - NGUY HIỂM",
                "Ở người cao tuổi: dấu hiệu lú lẫn, mê sảng - NGUY HIỂM"
            ],
            "precautions": [
                "CHỐNG CHỈ ĐỊNH ở glaucoma góc đóng - nguy cơ tăng nhãn áp nặng, mất thị lực",
                "Nhìn mờ kéo dài (7-14 ngày) - bệnh nhân không nên lái xe hoặc vận hành máy móc",
                "Nhạy cảm với ánh sáng - cần đeo kính râm, tránh ánh nắng mặt trời",
                "Hấp thu toàn thân - có thể gây khô miệng, nhịp tim nhanh, bí tiểu, lú lẫn",
                "Lú lẫn, mê sảng ở người cao tuổi - cần theo dõi sát, có thể cần ngừng thuốc",
                "Sốt ở trẻ em - hiếm nhưng nghiêm trọng, cần ngừng thuốc",
                "Thận trọng ở trẻ em <3 tháng tuổi - tăng nhạy cảm",
                "Thận trọng ở bệnh nhân dùng thuốc kháng cholinergic khác",
                "Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào (nguy cơ nhiễm trùng)",
                "Nhấn nhẹ vào góc trong mắt (lacrimal sac) trong 1-2 phút để giảm hấp thu toàn thân"
            ],
            "pharmacokinetics": {
                "half_life": "2-4 giờ (huyết tương), nhưng tác dụng tại mắt kéo dài 7-14 ngày",
                "onset": "30-60 phút",
                "duration": "7-14 ngày (tác dụng kéo dài)",
                "protein_binding": "14-22%",
                "metabolism": "Chuyển hóa tại mắt và gan (nếu hấp thu toàn thân)",
                "clearance": "Thải trừ tại chỗ, hấp thu toàn thân tối thiểu"
            },
            "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Đóng nắp kín sau khi dùng. Dùng trong 4 tuần sau khi mở.",
            "black_box_warnings": "CHỐNG CHỈ ĐỊNH ở glaucoma góc đóng. Nguy cơ tăng nhãn áp nặng, mất thị lực. Nhìn mờ kéo dài 7-14 ngày. Lú lẫn, mê sảng ở người cao tuổi. Sốt ở trẻ em.",
            "drug_interactions": {
                "major": [
                    {
                        "drug": "Thuốc kháng cholinergic khác (Oxybutynin, Tolterodine, Scopolamine)",
                        "mechanism": "Tác dụng kháng cholinergic cộng dồn",
                        "effect": "Tăng nguy cơ tác dụng phụ (khô miệng, nhịp tim nhanh, bí tiểu, lú lẫn)",
                        "management": "Thận trọng. Theo dõi tác dụng phụ sát."
                    }
                ],
                "moderate": [
                    {
                        "drug": "Thuốc gây QT kéo dài (Quinidine, Sotalol, Amiodarone)",
                        "mechanism": "Cả hai đều có thể gây QT kéo dài, tác dụng cộng dồn",
                        "effect": "Tăng nguy cơ rối loạn nhịp tim (torsades de pointes)",
                        "management": "Thận trọng. Theo dõi ECG nếu có nguy cơ."
                    }
                ],
                "minor": []
            },
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng atropine hoặc anticholinergic",
                    "Glaucoma góc đóng (narrow-angle glaucoma) - CHỐNG CHỈ ĐỊNH (nguy cơ tăng nhãn áp nặng, mất thị lực)",
                    "Glaucoma góc mở với góc hẹp - CHỐNG CHỈ ĐỊNH"
                ],
                "tương_đối": [
                    "Trẻ em <3 tháng tuổi - thận trọng (tăng nhạy cảm)",
                    "Bệnh nhược cơ (myasthenia gravis) - thận trọng",
                    "Bệnh đường tiêu hóa nặng (tắc nghẽn) - thận trọng",
                    "Người cao tuổi - tăng nguy cơ lú lẫn, mê sảng",
                    "Bệnh nhân dùng thuốc kháng cholinergic khác - tăng nguy cơ tác dụng phụ"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Atropine là thuốc phân loại C. Atropine có thể hấp thu toàn thân và qua nhau thai. Anticholinergic có thể gây tác dụng phụ ở thai nhi. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt khi không có lựa chọn khác.",
                "lactation": {
                    "safety": "Compatible with Caution",
                    "details": "Atropine có thể hấp thu toàn thân và bài tiết vào sữa mẹ ở nồng độ thấp. Tuy nhiên, nồng độ trong sữa mẹ thấp khi dùng tại mắt và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ.",
                    "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng. Nồng độ trong sữa mẹ thấp."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh liều",
                "moderate": "Không cần điều chỉnh liều",
                "severe": "Không cần điều chỉnh liều (ophthalmic, hấp thu tối thiểu)",
                "notes": "Atropine dùng tại mắt, hấp thu toàn thân tối thiểu. Không cần điều chỉnh liều ở bệnh nhân suy gan."
            },
            "overdose_management": {
                "symptoms": [
                    "Nhìn mờ nặng",
                    "Kích ứng mắt nặng",
                    "Hấp thu toàn thân: khô miệng nặng, nhịp tim nhanh nặng",
                    "Hấp thu toàn thân: bí tiểu nặng - NGUY HIỂM",
                    "Hấp thu toàn thân: lú lẫn nặng, mê sảng - NGUY HIỂM",
                    "Hấp thu toàn thân: sốt cao (ở trẻ em) - NGUY HIỂM",
                    "Hấp thu toàn thân: co thắt phế quản nặng (hen) - NGUY HIỂM",
                    "Tăng nhãn áp nặng (nếu có glaucoma góc đóng) - NGUY HIỂM"
                ],
                "antidote": "Physostigmine (anticholinesterase) để đối kháng tác dụng anticholinergic.",
                "treatment": [
                    "Rửa mắt ngay với nước sạch hoặc nước muối sinh lý",
                    "Nếu tăng nhãn áp nặng:",
                    "  - Khám mắt ngay",
                    "  - Thuốc hạ nhãn áp (pilocarpine, timolol) nếu cần",
                    "Nếu hấp thu toàn thân nặng:",
                    "  - Physostigmine 1-2mg IV (đối kháng anticholinergic) nếu có lú lẫn nặng, mê sảng",
                    "  - Hỗ trợ hô hấp nếu có co thắt phế quản",
                    "  - Đặt ống thông tiểu nếu có bí tiểu",
                    "  - Hỗ trợ tuần hoàn nếu có nhịp tim nhanh nặng",
                    "  - Hạ sốt nếu có sốt cao",
                    "Theo dõi: Nhãn áp, thị lực, dấu hiệu sinh tồn, tình trạng thần kinh, lượng nước tiểu"
                ],
                "monitoring": "Theo dõi nhãn áp, thị lực, dấu hiệu sinh tồn, tình trạng thần kinh, lượng nước tiểu cho đến khi hồi phục. Theo dõi lâu hơn nếu có biến chứng (tăng nhãn áp, lú lẫn, bí tiểu)."
            },
            "reversal_agents": {
                "available": True,
                "agents": [
                    {
                        "agent": "Physostigmine",
                        "mechanism": "Anticholinesterase, ức chế acetylcholinesterase, tăng acetylcholine, đối kháng tác dụng anticholinergic của atropine",
                        "indication": "Tác dụng phụ toàn thân nặng do atropine (lú lẫn nặng, mê sảng)",
                        "dose": "1-2mg IV, lặp lại mỗi 30-60 phút nếu cần (tối đa 4mg)"
                    }
                ],
                "notes": "Physostigmine đối kháng tác dụng anticholinergic của atropine cho tác dụng phụ toàn thân nặng. CHỈ dùng khi có lú lẫn nặng, mê sảng. Thận trọng ở bệnh nhân có tiền sử rối loạn nhịp tim."
            },
            "administration_instructions": {
                "ophthalmic": {
                    "preparation": "Dạng dung dịch nhỏ mắt 0.5% hoặc 1%.",
                    "application": "1 giọt vào mắt bị ảnh hưởng x 1-3 lần/ngày tùy chỉ định. Nhắm mắt nhẹ 1-2 phút sau khi nhỏ. Nhấn nhẹ vào góc trong mắt (lacrimal sac) trong 1-2 phút để giảm hấp thu toàn thân.",
                    "timing": "1-3 lần/ngày tùy chỉ định. Cho viêm màng bồ đào: 2-3 lần/ngày.",
                    "contact_lenses": "Tháo kính áp tròng trước khi nhỏ. Đợi 15 phút trước khi đeo lại.",
                    "notes": "QUAN TRỌNG: 1) CHỐNG CHỈ ĐỊNH ở glaucoma góc đóng, 2) Nhìn mờ kéo dài 7-14 ngày - không lái xe, 3) Nhạy cảm với ánh sáng - đeo kính râm, 4) Lú lẫn, mê sảng ở người cao tuổi - theo dõi sát, 5) Sốt ở trẻ em - ngừng thuốc nếu có."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Atropine (Atropisol)",
                    "UpToDate - Atropine: Drug Information",
                    "Medscape - Atropine Drug Reference",
                    "AAO Guidelines - Uveitis, Cycloplegia"
                ],
                "last_updated": "2025-02-18",
                "evidence_level": "A - Dựa trên FDA drug labels, clinical guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
            },
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["Systemic anticholinergic effects (dry mouth, tachycardia, urinary retention, confusion)", "Increased intraocular pressure (if narrow-angle glaucoma)"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Intraocular pressure (IOP) - CRITICAL (contraindicated in narrow-angle glaucoma)", "Systemic anticholinergic effects (dry mouth, tachycardia, urinary retention, confusion)", "Signs of CNS depression in elderly/children"]
            },
            "guideline_tags": [
                "AAO Guidelines - Uveitis",
                "AAO Guidelines - Cycloplegia",
                "FDA Drug Information - Atropine Ophthalmic",
                "FDA Black Box Warning - Atropine and Narrow-Angle Glaucoma"
            ]
        },

        "Cyclopentolate eye drops": {
            "group": "Ophthalmology - Cycloplegic/Mydriatic (Short-acting)",
            "vietnamese_name": "Cyclopentolate, Cyclogyl",
            "administration": ["Ophthalmic"],
            "indications": [
                "Giãn đồng tử (mydriasis) và liệt điều tiết (cycloplegia) cho khám mắt",
                "Khám khúc xạ (refraction) ở trẻ em",
                "Điều trị viêm màng bồ đào (uveitis) - giảm đau, giảm dính mống mắt",
                "Điều trị viêm mống mắt (iritis)",
                "Dự phòng dính mống mắt (posterior synechiae) trong viêm màng bồ đào"
            ],
            "contraindications": [
                "Dị ứng cyclopentolate hoặc anticholinergic",
                "Glaucoma góc đóng (narrow-angle glaucoma) - CHỐNG CHỈ ĐỊNH",
                "Glaucoma góc mở với góc hẹp - CHỐNG CHỈ ĐỊNH",
                "Trẻ sơ sinh - thận trọng (tăng nhạy cảm)",
                "Bệnh nhược cơ (myasthenia gravis) - thận trọng",
                "Bệnh đường tiêu hóa nặng (tắc nghẽn) - thận trọng"
            ],
            "dosage": {
                "adult_mydriasis_cycloplegia": "1 giọt vào mắt bị ảnh hưởng x 1-2 lần (cách nhau 5-10 phút) trước khám mắt",
                "pediatric_refraction": "1 giọt vào mắt bị ảnh hưởng x 1-2 lần (cách nhau 5-10 phút) trước khám khúc xạ",
                "adult_uveitis": "1 giọt vào mắt bị ảnh hưởng x 2-3 lần/ngày",
                "notes": "Cyclopentolate là anticholinergic, gây giãn đồng tử (mydriasis) và liệt điều tiết (cycloplegia) tác dụng ngắn (6-24 giờ). Phù hợp cho khám mắt và khám khúc xạ. CHỐNG CHỈ ĐỊNH ở glaucoma góc đóng. Có thể hấp thu toàn thân và gây tác dụng phụ hệ thống (nhưng ít hơn atropine)."
            },
            "renal_adjustment": {
                "normal": "Không đổi",
                "30_60": "Không cần điều chỉnh đáng kể",
                "under_30": "Không cần điều chỉnh đáng kể"
            },
            "side_effects": [
                "Nhìn mờ (6-24 giờ) - phổ biến",
                "Nhạy cảm với ánh sáng (photophobia) - phổ biến",
                "Kích ứng mắt (đỏ, rát) - phổ biến",
                "Hấp thu toàn thân: khô miệng - phổ biến",
                "Hấp thu toàn thân: nhịp tim nhanh - phổ biến",
                "Hấp thu toàn thân: bí tiểu - hiếm",
                "Hấp thu toàn thân: lú lẫn, mê sảng (ở trẻ em, người cao tuổi) - hiếm nhưng nghiêm trọng",
                "Hấp thu toàn thân: sốt (ở trẻ em) - hiếm nhưng nghiêm trọng",
                "Hấp thu toàn thân: co thắt phế quản (hen) - hiếm",
                "Tăng nhãn áp (nếu có glaucoma góc đóng) - NGUY HIỂM"
            ],
            "interactions": [
                "Thuốc kháng cholinergic khác: tăng nguy cơ tác dụng phụ",
                "Thuốc gây QT kéo dài: tăng nguy cơ rối loạn nhịp tim",
                "Thuốc ức chế acetylcholinesterase (neostigmine, pyridostigmine): đối kháng tác dụng"
            ],
            "pregnancy": "C - Thận trọng",
            "mechanism_of_action": "Cyclopentolate là anticholinergic (muscarinic receptor antagonist). Ức chế muscarinic receptors trong cơ trơn mống mắt (iris sphincter) và cơ thể mi (ciliary muscle), dẫn đến: (1) Giãn đồng tử (mydriasis) - ức chế cơ co đồng tử, (2) Liệt điều tiết (cycloplegia) - ức chế cơ thể mi, mất khả năng điều tiết, (3) Giảm đau trong viêm màng bồ đào (giảm co thắt cơ), (4) Dự phòng dính mống mắt (giữ đồng tử giãn). Cyclopentolate có tác dụng ngắn (6-24 giờ) so với atropine (7-14 ngày), phù hợp cho khám mắt và khám khúc xạ. ĐẶC ĐIỂM: (1) Tác dụng ngắn (6-24 giờ), (2) CHỐNG CHỈ ĐỊNH ở glaucoma góc đóng, (3) Có thể hấp thu toàn thân nhưng ít hơn atropine, (4) Nhìn mờ 6-24 giờ - bệnh nhân không nên lái xe, (5) Nhạy cảm với ánh sáng - cần đeo kính râm, (6) Lú lẫn, mê sảng ở trẻ em, người cao tuổi - cần theo dõi sát.",
            "monitoring": [
                "Nhãn áp (intraocular pressure - IOP) - QUAN TRỌNG (nguy cơ tăng nhãn áp nếu có glaucoma góc đóng)",
                "Thị lực (nhìn mờ 6-24 giờ)",
                "Dấu hiệu kích ứng mắt (đỏ, rát)",
                "Dấu hiệu hấp thu toàn thân: khô miệng, nhịp tim nhanh, bí tiểu, lú lẫn",
                "Ở trẻ em: dấu hiệu sốt, lú lẫn, mê sảng - NGUY HIỂM",
                "Ở người cao tuổi: dấu hiệu lú lẫn, mê sảng - NGUY HIỂM"
            ],
            "precautions": [
                "CHỐNG CHỈ ĐỊNH ở glaucoma góc đóng - nguy cơ tăng nhãn áp nặng, mất thị lực",
                "Nhìn mờ (6-24 giờ) - bệnh nhân không nên lái xe hoặc vận hành máy móc",
                "Nhạy cảm với ánh sáng - cần đeo kính râm, tránh ánh nắng mặt trời",
                "Hấp thu toàn thân - có thể gây khô miệng, nhịp tim nhanh, bí tiểu, lú lẫn",
                "Lú lẫn, mê sảng ở trẻ em, người cao tuổi - cần theo dõi sát, có thể cần ngừng thuốc",
                "Sốt ở trẻ em - hiếm nhưng nghiêm trọng, cần ngừng thuốc",
                "Thận trọng ở trẻ sơ sinh - tăng nhạy cảm",
                "Thận trọng ở bệnh nhân dùng thuốc kháng cholinergic khác",
                "Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào (nguy cơ nhiễm trùng)",
                "Nhấn nhẹ vào góc trong mắt (lacrimal sac) trong 1-2 phút để giảm hấp thu toàn thân"
            ],
            "pharmacokinetics": {
                "half_life": "Không áp dụng (ophthalmic)",
                "onset": "30-60 phút",
                "duration": "6-24 giờ (tác dụng ngắn hơn atropine)",
                "protein_binding": "Không áp dụng (ophthalmic)",
                "metabolism": "Chuyển hóa tại mắt và gan (nếu hấp thu toàn thân)",
                "clearance": "Thải trừ tại chỗ, hấp thu toàn thân tối thiểu"
            },
            "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Đóng nắp kín sau khi dùng. Dùng trong 4 tuần sau khi mở.",
            "black_box_warnings": "CHỐNG CHỈ ĐỊNH ở glaucoma góc đóng. Nguy cơ tăng nhãn áp nặng, mất thị lực. Lú lẫn, mê sảng ở trẻ em, người cao tuổi. Sốt ở trẻ em.",
            "drug_interactions": {
                "major": [
                    {
                        "drug": "Thuốc kháng cholinergic khác (Oxybutynin, Tolterodine, Atropine)",
                        "mechanism": "Tác dụng kháng cholinergic cộng dồn",
                        "effect": "Tăng nguy cơ tác dụng phụ (khô miệng, nhịp tim nhanh, bí tiểu, lú lẫn)",
                        "management": "Thận trọng. Theo dõi tác dụng phụ sát."
                    }
                ],
                "moderate": [
                    {
                        "drug": "Thuốc gây QT kéo dài (Quinidine, Sotalol, Amiodarone)",
                        "mechanism": "Cả hai đều có thể gây QT kéo dài, tác dụng cộng dồn",
                        "effect": "Tăng nguy cơ rối loạn nhịp tim (torsades de pointes)",
                        "management": "Thận trọng. Theo dõi ECG nếu có nguy cơ."
                    }
                ],
                "minor": []
            },
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng cyclopentolate hoặc anticholinergic",
                    "Glaucoma góc đóng (narrow-angle glaucoma) - CHỐNG CHỈ ĐỊNH (nguy cơ tăng nhãn áp nặng, mất thị lực)",
                    "Glaucoma góc mở với góc hẹp - CHỐNG CHỈ ĐỊNH"
                ],
                "tương_đối": [
                    "Trẻ sơ sinh - thận trọng (tăng nhạy cảm)",
                    "Bệnh nhược cơ (myasthenia gravis) - thận trọng",
                    "Bệnh đường tiêu hóa nặng (tắc nghẽn) - thận trọng",
                    "Người cao tuổi - tăng nguy cơ lú lẫn, mê sảng",
                    "Bệnh nhân dùng thuốc kháng cholinergic khác - tăng nguy cơ tác dụng phụ"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Cyclopentolate là thuốc phân loại C. Cyclopentolate có thể hấp thu toàn thân và qua nhau thai. Anticholinergic có thể gây tác dụng phụ ở thai nhi. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt khi không có lựa chọn khác.",
                "lactation": {
                    "safety": "Compatible with Caution",
                    "details": "Cyclopentolate có thể hấp thu toàn thân và bài tiết vào sữa mẹ ở nồng độ thấp. Tuy nhiên, nồng độ trong sữa mẹ thấp khi dùng tại mắt và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ.",
                    "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng. Nồng độ trong sữa mẹ thấp."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh liều",
                "moderate": "Không cần điều chỉnh liều",
                "severe": "Không cần điều chỉnh liều (ophthalmic, hấp thu tối thiểu)",
                "notes": "Cyclopentolate dùng tại mắt, hấp thu toàn thân tối thiểu. Không cần điều chỉnh liều ở bệnh nhân suy gan."
            },
            "overdose_management": {
                "symptoms": [
                    "Nhìn mờ nặng",
                    "Kích ứng mắt nặng",
                    "Hấp thu toàn thân: khô miệng nặng, nhịp tim nhanh nặng",
                    "Hấp thu toàn thân: bí tiểu nặng - NGUY HIỂM",
                    "Hấp thu toàn thân: lú lẫn nặng, mê sảng - NGUY HIỂM",
                    "Hấp thu toàn thân: sốt cao (ở trẻ em) - NGUY HIỂM",
                    "Hấp thu toàn thân: co thắt phế quản nặng (hen) - NGUY HIỂM",
                    "Tăng nhãn áp nặng (nếu có glaucoma góc đóng) - NGUY HIỂM"
                ],
                "antidote": "Physostigmine (anticholinesterase) để đối kháng tác dụng anticholinergic.",
                "treatment": [
                    "Rửa mắt ngay với nước sạch hoặc nước muối sinh lý",
                    "Nếu tăng nhãn áp nặng:",
                    "  - Khám mắt ngay",
                    "  - Thuốc hạ nhãn áp (pilocarpine, timolol) nếu cần",
                    "Nếu hấp thu toàn thân nặng:",
                    "  - Physostigmine 1-2mg IV (đối kháng anticholinergic) nếu có lú lẫn nặng, mê sảng",
                    "  - Hỗ trợ hô hấp nếu có co thắt phế quản",
                    "  - Đặt ống thông tiểu nếu có bí tiểu",
                    "  - Hỗ trợ tuần hoàn nếu có nhịp tim nhanh nặng",
                    "  - Hạ sốt nếu có sốt cao",
                    "Theo dõi: Nhãn áp, thị lực, dấu hiệu sinh tồn, tình trạng thần kinh, lượng nước tiểu"
                ],
                "monitoring": "Theo dõi nhãn áp, thị lực, dấu hiệu sinh tồn, tình trạng thần kinh, lượng nước tiểu cho đến khi hồi phục. Theo dõi lâu hơn nếu có biến chứng (tăng nhãn áp, lú lẫn, bí tiểu)."
            },
            "reversal_agents": {
                "available": True,
                "agents": [
                    {
                        "agent": "Physostigmine",
                        "mechanism": "Anticholinesterase, ức chế acetylcholinesterase, tăng acetylcholine, đối kháng tác dụng anticholinergic của cyclopentolate",
                        "indication": "Tác dụng phụ toàn thân nặng do cyclopentolate (lú lẫn nặng, mê sảng)",
                        "dose": "1-2mg IV, lặp lại mỗi 30-60 phút nếu cần (tối đa 4mg)"
                    }
                ],
                "notes": "Physostigmine đối kháng tác dụng anticholinergic của cyclopentolate cho tác dụng phụ toàn thân nặng. CHỈ dùng khi có lú lẫn nặng, mê sảng. Thận trọng ở bệnh nhân có tiền sử rối loạn nhịp tim."
            },
            "administration_instructions": {
                "ophthalmic": {
                    "preparation": "Dạng dung dịch nhỏ mắt 0.5% hoặc 1%.",
                    "application": "1 giọt vào mắt bị ảnh hưởng x 1-2 lần (cách nhau 5-10 phút) trước khám mắt hoặc khám khúc xạ. Nhắm mắt nhẹ 1-2 phút sau khi nhỏ. Nhấn nhẹ vào góc trong mắt (lacrimal sac) trong 1-2 phút để giảm hấp thu toàn thân.",
                    "timing": "1-2 lần (cách nhau 5-10 phút) trước khám mắt. Cho viêm màng bồ đào: 2-3 lần/ngày.",
                    "contact_lenses": "Tháo kính áp tròng trước khi nhỏ. Đợi 15 phút trước khi đeo lại.",
                    "notes": "QUAN TRỌNG: 1) CHỐNG CHỈ ĐỊNH ở glaucoma góc đóng, 2) Nhìn mờ 6-24 giờ - không lái xe, 3) Nhạy cảm với ánh sáng - đeo kính râm, 4) Lú lẫn, mê sảng ở trẻ em, người cao tuổi - theo dõi sát, 5) Sốt ở trẻ em - ngừng thuốc nếu có."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Cyclopentolate (Cyclogyl)",
                    "UpToDate - Cyclopentolate: Drug Information",
                    "Medscape - Cyclopentolate Drug Reference",
                    "AAO Guidelines - Cycloplegia, Refraction"
                ],
                "last_updated": "2025-02-18",
                "evidence_level": "A - Dựa trên FDA drug labels, clinical guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
            },
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["Systemic anticholinergic effects (dry mouth, tachycardia, urinary retention, confusion)", "Increased intraocular pressure (if narrow-angle glaucoma)"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Intraocular pressure (IOP) - CRITICAL (contraindicated in narrow-angle glaucoma)", "Systemic anticholinergic effects (dry mouth, tachycardia, urinary retention, confusion)", "Signs of CNS depression in elderly/children (confusion, delirium, fever)"]
            },
            "guideline_tags": [
                "AAO Guidelines - Cycloplegia",
                "AAO Guidelines - Refraction",
                "FDA Drug Information - Cyclopentolate Ophthalmic",
                "FDA Black Box Warning - Cyclopentolate and Narrow-Angle Glaucoma"
            ]
        },

        "Phenylephrine eye drops": {
            "group": "Ophthalmology - Alpha-1 Adrenergic Agonist (Mydriatic)",
            "vietnamese_name": "Phenylephrine, Neo-Synephrine",
            "administration": ["Ophthalmic"],
            "indications": [
                "Giãn đồng tử (mydriasis) cho khám mắt",
                "Giãn đồng tử trước phẫu thuật mắt",
                "Điều trị viêm màng bồ đào (uveitis) - giảm dính mống mắt",
                "Điều trị xuất huyết dưới kết mạc (subconjunctival hemorrhage) - giảm đỏ mắt",
                "Kết hợp với cycloplegic để tăng hiệu quả giãn đồng tử"
            ],
            "contraindications": [
                "Dị ứng phenylephrine hoặc alpha-1 agonist",
                "Glaucoma góc đóng (narrow-angle glaucoma) - CHỐNG CHỈ ĐỊNH",
                "Glaucoma góc mở với góc hẹp - CHỐNG CHỈ ĐỊNH",
                "Bệnh tim mạch nặng (bệnh mạch vành, đột quỵ, nhồi máu cơ tim gần đây) - CHỐNG CHỈ ĐỊNH",
                "Tăng huyết áp không kiểm soát - CHỐNG CHỈ ĐỊNH",
                "Phình động mạch chủ (aortic aneurysm) - CHỐNG CHỈ ĐỊNH",
                "Trẻ em <12 tuổi (nồng độ cao) - thận trọng"
            ],
            "dosage": {
                "adult_mydriasis_2.5%": "1 giọt vào mắt bị ảnh hưởng x 1 lần trước khám mắt (2.5% solution)",
                "adult_mydriasis_10%": "1 giọt vào mắt bị ảnh hưởng x 1 lần trước khám mắt hoặc phẫu thuật (10% solution)",
                "adult_uveitis": "1 giọt vào mắt bị ảnh hưởng x 2-3 lần/ngày",
                "pediatric_<12_years": "Chỉ dùng nồng độ thấp (2.5%), thận trọng",
                "notes": "Phenylephrine là alpha-1 adrenergic agonist, gây giãn đồng tử (mydriasis) tác dụng ngắn (2-6 giờ). KHÔNG gây liệt điều tiết (cycloplegia). Có thể hấp thu toàn thân và gây tác dụng phụ hệ thống (tăng huyết áp, nhịp tim nhanh, đau ngực). CHỐNG CHỈ ĐỊNH ở bệnh tim mạch nặng, tăng huyết áp không kiểm soát."
            },
            "renal_adjustment": {
                "normal": "Không đổi",
                "30_60": "Không cần điều chỉnh đáng kể",
                "under_30": "Không cần điều chỉnh đáng kể"
            },
            "side_effects": [
                "Nhìn mờ tạm thời (2-6 giờ) - phổ biến",
                "Nhạy cảm với ánh sáng (photophobia) - phổ biến",
                "Kích ứng mắt (đỏ, rát) - phổ biến",
                "Hấp thu toàn thân: tăng huyết áp - phổ biến, có thể nặng",
                "Hấp thu toàn thân: nhịp tim nhanh - phổ biến",
                "Hấp thu toàn thân: đau ngực, loạn nhịp tim - hiếm nhưng nghiêm trọng",
                "Hấp thu toàn thân: đột quỵ, nhồi máu cơ tim - hiếm nhưng nghiêm trọng",
                "Hấp thu toàn thân: đau đầu, chóng mặt - phổ biến",
                "Tăng nhãn áp (nếu có glaucoma góc đóng) - NGUY HIỂM"
            ],
            "interactions": [
                "MAO inhibitors: tăng nguy cơ tăng huyết áp nặng, đột quỵ, nhồi máu cơ tim",
                "Thuốc tăng huyết áp: tăng nguy cơ tăng huyết áp nặng",
                "Beta-blockers: tăng nguy cơ tăng huyết áp nặng (do ức chế beta, chỉ còn alpha)",
                "Tricyclic antidepressants: tăng nguy cơ tăng huyết áp nặng",
                "Cocaine: tăng nguy cơ tăng huyết áp nặng, loạn nhịp tim"
            ],
            "pregnancy": "C - Thận trọng",
            "mechanism_of_action": "Phenylephrine là alpha-1 adrenergic receptor agonist. Kích thích alpha-1 receptors trong cơ trơn mống mắt (iris dilator muscle), gây co cơ giãn đồng tử (dilator muscle contraction), dẫn đến giãn đồng tử (mydriasis). Phenylephrine KHÔNG ảnh hưởng đến cơ thể mi (ciliary muscle), do đó KHÔNG gây liệt điều tiết (cycloplegia). Phenylephrine cũng có tác dụng co mạch (vasoconstriction), giảm đỏ mắt. ĐẶC ĐIỂM: (1) Tác dụng ngắn (2-6 giờ), (2) CHỈ gây giãn đồng tử, KHÔNG gây liệt điều tiết, (3) CHỐNG CHỈ ĐỊNH ở glaucoma góc đóng, bệnh tim mạch nặng, tăng huyết áp không kiểm soát, (4) Có thể hấp thu toàn thân và gây tăng huyết áp, nhịp tim nhanh, đau ngực, (5) CHỐNG CHỈ ĐỊNH với MAO inhibitors, (6) Thường dùng kết hợp với cycloplegic để tăng hiệu quả giãn đồng tử.",
            "monitoring": [
                "Nhãn áp (intraocular pressure - IOP) - QUAN TRỌNG (nguy cơ tăng nhãn áp nếu có glaucoma góc đóng)",
                "Thị lực (nhìn mờ tạm thời 2-6 giờ)",
                "Dấu hiệu kích ứng mắt (đỏ, rát)",
                "Huyết áp - QUAN TRỌNG (nguy cơ tăng huyết áp)",
                "Nhịp tim - QUAN TRỌNG (nguy cơ nhịp tim nhanh)",
                "Dấu hiệu hấp thu toàn thân: đau ngực, khó thở, đau đầu nặng - NGUY HIỂM"
            ],
            "precautions": [
                "CHỐNG CHỈ ĐỊNH ở glaucoma góc đóng - nguy cơ tăng nhãn áp nặng, mất thị lực",
                "CHỐNG CHỈ ĐỊNH ở bệnh tim mạch nặng, tăng huyết áp không kiểm soát - nguy cơ đột quỵ, nhồi máu cơ tim",
                "CHỐNG CHỈ ĐỊNH với MAO inhibitors - nguy cơ tăng huyết áp nặng, đột quỵ, nhồi máu cơ tim",
                "Tăng huyết áp - phổ biến, có thể nặng, cần theo dõi huyết áp",
                "Nhịp tim nhanh - phổ biến, có thể nặng",
                "Đau ngực, loạn nhịp tim - hiếm nhưng nghiêm trọng, cần ngừng thuốc ngay",
                "Nhìn mờ tạm thời (2-6 giờ) - bệnh nhân không nên lái xe",
                "Nhạy cảm với ánh sáng - cần đeo kính râm",
                "Thận trọng ở trẻ em <12 tuổi - chỉ dùng nồng độ thấp (2.5%)",
                "Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào (nguy cơ nhiễm trùng)",
                "Nhấn nhẹ vào góc trong mắt (lacrimal sac) trong 1-2 phút để giảm hấp thu toàn thân"
            ],
            "pharmacokinetics": {
                "half_life": "2-3 giờ (huyết tương), nhưng tác dụng tại mắt kéo dài 2-6 giờ",
                "onset": "20-30 phút",
                "duration": "2-6 giờ (tác dụng ngắn)",
                "protein_binding": "Không đáng kể",
                "metabolism": "Chuyển hóa tại mắt và gan (nếu hấp thu toàn thân, MAO)",
                "clearance": "Thải trừ tại chỗ, hấp thu toàn thân tối thiểu"
            },
            "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Đóng nắp kín sau khi dùng. Dùng trong 4 tuần sau khi mở.",
            "black_box_warnings": "CHỐNG CHỈ ĐỊNH ở glaucoma góc đóng, bệnh tim mạch nặng, tăng huyết áp không kiểm soát. Nguy cơ tăng huyết áp nặng, đột quỵ, nhồi máu cơ tim nếu hấp thu toàn thân. CHỐNG CHỈ ĐỊNH với MAO inhibitors.",
            "drug_interactions": {
                "major": [
                    {
                        "drug": "MAO Inhibitors (Phenelzine, Tranylcypromine, Isocarboxazid, Selegiline)",
                        "mechanism": "Ức chế MAO, tăng nồng độ catecholamine, tác dụng cộng dồn với alpha-1 agonist",
                        "effect": "Tăng nguy cơ tăng huyết áp nặng, đột quỵ, nhồi máu cơ tim, tử vong",
                        "management": "CHỐNG CHỈ ĐỊNH tuyệt đối. KHÔNG được dùng đồng thời. Cách xa ít nhất 14 ngày sau khi ngừng MAO inhibitor."
                    },
                    {
                        "drug": "Beta-blockers (Propranolol, Metoprolol, Atenolol)",
                        "mechanism": "Ức chế beta, chỉ còn tác dụng alpha, tăng nguy cơ tăng huyết áp nặng",
                        "effect": "Tăng nguy cơ tăng huyết áp nặng, đột quỵ, nhồi máu cơ tim",
                        "management": "TRÁNH DÙNG CHUNG. Nếu bắt buộc, theo dõi huyết áp sát."
                    }
                ],
                "moderate": [
                    {
                        "drug": "Thuốc tăng huyết áp (Norepinephrine, Epinephrine, Dopamine)",
                        "mechanism": "Tác dụng tăng huyết áp cộng dồn",
                        "effect": "Tăng nguy cơ tăng huyết áp nặng, đột quỵ, nhồi máu cơ tim",
                        "management": "Thận trọng. Theo dõi huyết áp sát."
                    },
                    {
                        "drug": "Tricyclic Antidepressants (Amitriptyline, Imipramine)",
                        "mechanism": "Ức chế tái hấp thu norepinephrine, tác dụng cộng dồn với alpha-1 agonist",
                        "effect": "Tăng nguy cơ tăng huyết áp nặng",
                        "management": "Thận trọng. Theo dõi huyết áp sát."
                    }
                ],
                "minor": []
            },
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng phenylephrine hoặc alpha-1 agonist",
                    "Glaucoma góc đóng (narrow-angle glaucoma) - CHỐNG CHỈ ĐỊNH (nguy cơ tăng nhãn áp nặng, mất thị lực)",
                    "Glaucoma góc mở với góc hẹp - CHỐNG CHỈ ĐỊNH",
                    "Bệnh tim mạch nặng (bệnh mạch vành, đột quỵ, nhồi máu cơ tim gần đây) - CHỐNG CHỈ ĐỊNH",
                    "Tăng huyết áp không kiểm soát - CHỐNG CHỈ ĐỊNH",
                    "Phình động mạch chủ (aortic aneurysm) - CHỐNG CHỈ ĐỊNH",
                    "Dùng với MAO inhibitors - CHỐNG CHỈ ĐỊNH"
                ],
                "tương_đối": [
                    "Bệnh tim mạch ổn định - thận trọng",
                    "Tăng huyết áp kiểm soát tốt - thận trọng",
                    "Trẻ em <12 tuổi - chỉ dùng nồng độ thấp (2.5%), thận trọng",
                    "Dùng với beta-blockers - tăng nguy cơ tăng huyết áp",
                    "Dùng với thuốc tăng huyết áp - tăng nguy cơ tăng huyết áp"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Phenylephrine là thuốc phân loại C. Phenylephrine có thể hấp thu toàn thân và qua nhau thai. Alpha-1 agonist có thể gây tăng huyết áp ở thai nhi. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt khi không có lựa chọn khác.",
                "lactation": {
                    "safety": "Compatible with Caution",
                    "details": "Phenylephrine có thể hấp thu toàn thân và bài tiết vào sữa mẹ ở nồng độ thấp. Tuy nhiên, nồng độ trong sữa mẹ thấp khi dùng tại mắt và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ.",
                    "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng. Nồng độ trong sữa mẹ thấp."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh liều",
                "moderate": "Không cần điều chỉnh liều",
                "severe": "Không cần điều chỉnh liều (ophthalmic, hấp thu tối thiểu)",
                "notes": "Phenylephrine dùng tại mắt, hấp thu toàn thân tối thiểu. Không cần điều chỉnh liều ở bệnh nhân suy gan."
            },
            "overdose_management": {
                "symptoms": [
                    "Nhìn mờ nặng",
                    "Kích ứng mắt nặng",
                    "Hấp thu toàn thân: tăng huyết áp nặng (>200/120 mmHg) - NGUY HIỂM",
                    "Hấp thu toàn thân: nhịp tim nhanh nặng (>150 bpm) - NGUY HIỂM",
                    "Hấp thu toàn thân: đau ngực, loạn nhịp tim - NGUY HIỂM",
                    "Hấp thu toàn thân: đột quỵ, nhồi máu cơ tim - NGUY HIỂM",
                    "Tăng nhãn áp nặng (nếu có glaucoma góc đóng) - NGUY HIỂM"
                ],
                "antidote": "Phentolamine (alpha-blocker) để đối kháng tác dụng alpha-1. Nitroglycerin để giảm huyết áp.",
                "treatment": [
                    "Rửa mắt ngay với nước sạch hoặc nước muối sinh lý",
                    "Nếu tăng nhãn áp nặng:",
                    "  - Khám mắt ngay",
                    "  - Thuốc hạ nhãn áp (pilocarpine, timolol) nếu cần",
                    "Nếu hấp thu toàn thân nặng:",
                    "  - Theo dõi ECG và huyết áp liên tục",
                    "  - Nếu tăng huyết áp nặng:",
                    "    - Phentolamine 5-10mg IV (đối kháng alpha-1)",
                    "    - Hoặc Nitroglycerin IV (giãn mạch, giảm huyết áp)",
                    "  - Nếu đau ngực, loạn nhịp tim:",
                    "    - Điều trị theo protocol nhồi máu cơ tim",
                    "    - Theo dõi ECG liên tục",
                    "  - Nếu đột quỵ:",
                    "    - Điều trị theo protocol đột quỵ",
                    "Theo dõi: Nhãn áp, thị lực, huyết áp, nhịp tim, ECG, dấu hiệu sinh tồn"
                ],
                "monitoring": "Theo dõi nhãn áp, thị lực, huyết áp, nhịp tim, ECG, dấu hiệu sinh tồn cho đến khi hồi phục. Theo dõi lâu hơn nếu có biến chứng (tăng huyết áp nặng, đau ngực, đột quỵ)."
            },
            "reversal_agents": {
                "available": True,
                "agents": [
                    {
                        "agent": "Phentolamine",
                        "mechanism": "Alpha-blocker, đối kháng tác dụng alpha-1 của phenylephrine (co mạch, tăng huyết áp)",
                        "indication": "Tăng huyết áp nặng do quá liều phenylephrine",
                        "dose": "5-10mg IV"
                    },
                    {
                        "agent": "Nitroglycerin",
                        "mechanism": "Giãn mạch, giảm huyết áp",
                        "indication": "Tăng huyết áp nặng do quá liều phenylephrine",
                        "dose": "5-10mcg/phút IV, tăng dần đến khi đạt huyết áp mục tiêu"
                    }
                ],
                "notes": "Phentolamine và nitroglycerin điều trị tăng huyết áp nặng do quá liều phenylephrine."
            },
            "administration_instructions": {
                "ophthalmic": {
                    "preparation": "Dạng dung dịch nhỏ mắt 2.5% hoặc 10%.",
                    "application": "1 giọt vào mắt bị ảnh hưởng x 1 lần trước khám mắt hoặc phẫu thuật. Nhắm mắt nhẹ 1-2 phút sau khi nhỏ. Nhấn nhẹ vào góc trong mắt (lacrimal sac) trong 1-2 phút để giảm hấp thu toàn thân.",
                    "timing": "1 lần trước khám mắt hoặc phẫu thuật. Cho viêm màng bồ đào: 2-3 lần/ngày.",
                    "contact_lenses": "Tháo kính áp tròng trước khi nhỏ. Đợi 15 phút trước khi đeo lại.",
                    "notes": "QUAN TRỌNG: 1) CHỐNG CHỈ ĐỊNH ở glaucoma góc đóng, bệnh tim mạch nặng, tăng huyết áp không kiểm soát, 2) CHỐNG CHỈ ĐỊNH với MAO inhibitors, 3) Tăng huyết áp, nhịp tim nhanh phổ biến - theo dõi sát, 4) Đau ngực - ngừng thuốc ngay, 5) Nhìn mờ 2-6 giờ - không lái xe."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Phenylephrine (Neo-Synephrine)",
                    "UpToDate - Phenylephrine: Drug Information",
                    "Medscape - Phenylephrine Drug Reference",
                    "AAO Guidelines - Mydriasis, Uveitis"
                ],
                "last_updated": "2025-02-18",
                "evidence_level": "A - Dựa trên FDA drug labels, clinical guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
            },
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["Cardiovascular effects (hypertension, tachycardia, chest pain, arrhythmias)", "Increased intraocular pressure (if narrow-angle glaucoma)", "Cerebrovascular events (stroke, MI) with systemic absorption"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Intraocular pressure (IOP) - CRITICAL (contraindicated in narrow-angle glaucoma)", "Blood pressure - CRITICAL (hypertension risk)", "Heart rate - CRITICAL (tachycardia risk)", "Signs of cardiovascular events (chest pain, arrhythmias)"]
            },
            "guideline_tags": [
                "AAO Guidelines - Mydriasis",
                "AAO Guidelines - Uveitis",
                "FDA Drug Information - Phenylephrine Ophthalmic",
                "FDA Black Box Warning - Phenylephrine and Cardiovascular Risk",
                "FDA Black Box Warning - Phenylephrine and MAO Inhibitors"
            ]
        },

        "Tropicamide eye drops": {
            "group": "Ophthalmology - Mydriatic (Pupil Dilation)",
            "vietnamese_name": "Tropicamide nhỏ mắt, Mydriacyl",
            "administration": ["Ophthalmic"],
            "indications": [
                "Giãn đồng tử để khám mắt (pupil dilation for eye examination)",
                "Khám đáy mắt (fundoscopy)",
                "Khám thủy tinh thể (lens examination)",
                "Đo khúc xạ (refraction) - ở trẻ em"
            ],
            "contraindications": [
                "Dị ứng tropicamide hoặc anticholinergic",
                "Tăng nhãn áp góc đóng (angle-closure glaucoma) - CHỐNG CHỈ ĐỊNH",
                "Bệnh nhân có tiền sử tăng nhãn áp góc đóng - CHỐNG CHỈ ĐỊNH",
                "Trẻ em <3 tháng tuổi - thận trọng"
            ],
            "dosage": {
                "adult_ophthalmic_0.5%": "1-2 giọt vào mắt cần khám, lặp lại sau 5 phút nếu cần",
                "adult_ophthalmic_1%": "1-2 giọt vào mắt cần khám, lặp lại sau 5 phút nếu cần",
                "pediatric_ophthalmic": "1 giọt vào mắt cần khám, lặp lại sau 5 phút nếu cần (thận trọng ở trẻ nhỏ)",
                "notes": "Tropicamide là anticholinergic, giãn đồng tử và liệt điều tiết. Tác dụng nhanh (15-30 phút), kéo dài 4-6 giờ. CHỐNG CHỈ ĐỊNH ở tăng nhãn áp góc đóng (có thể gây tăng nhãn áp cấp tính)."
            },
            "renal_adjustment": {
                "normal": "Không đổi",
                "30_60": "Không đổi",
                "under_30": "Không đổi"
            },
            "side_effects": [
                "Nhìn mờ (do liệt điều tiết) - phổ biến, kéo dài 4-6 giờ",
                "Nhạy cảm với ánh sáng (do giãn đồng tử) - phổ biến, kéo dài 4-6 giờ",
                "Kích ứng mắt (đỏ, rát) - phổ biến",
                "Tăng nhãn áp (ở bệnh nhân tăng nhãn áp góc đóng) - NGUY HIỂM",
                "Tăng nhãn áp cấp tính (angle-closure glaucoma) - NGUY HIỂM",
                "Hấp thu toàn thân: khô miệng, nhịp nhanh - hiếm",
                "Phản ứng dị ứng - hiếm"
            ],
            "interactions": [
                "Anticholinergic đường uống: tăng nguy cơ tác dụng phụ toàn thân",
                "Thuốc chống trầm cảm ba vòng: tăng nguy cơ tác dụng phụ toàn thân"
            ],
            "pregnancy": "C - Thận trọng",
            "mechanism_of_action": "Tropicamide là anticholinergic (muscarinic receptor antagonist). Ức chế muscarinic receptors trên cơ vòng mống mắt (sphincter pupillae) và cơ thể mi (ciliary muscle), dẫn đến: (1) Giãn đồng tử (mydriasis) - cơ vòng mống mắt giãn, cơ giãn mống mắt co, (2) Liệt điều tiết (cycloplegia) - cơ thể mi giãn, thủy tinh thể phẳng, không thể điều tiết. Dẫn đến: giãn đồng tử và liệt điều tiết, cho phép khám mắt tốt hơn. Tropicamide tác dụng nhanh (15-30 phút), kéo dài 4-6 giờ. ĐẶC ĐIỂM: (1) Anticholinergic, giãn đồng tử và liệt điều tiết, (2) Tác dụng nhanh (15-30 phút), kéo dài 4-6 giờ, (3) CHỐNG CHỈ ĐỊNH ở tăng nhãn áp góc đóng (có thể gây tăng nhãn áp cấp tính), (4) Nhìn mờ và nhạy cảm với ánh sáng kéo dài 4-6 giờ, (5) Có thể hấp thu toàn thân và gây tác dụng phụ (khô miệng, nhịp nhanh).",
            "monitoring": [
                "Nhãn áp (intraocular pressure - IOP) - QUAN TRỌNG: kiểm tra trước và sau khi dùng, đặc biệt ở bệnh nhân có nguy cơ",
                "Dấu hiệu tăng nhãn áp cấp tính (đau mắt nặng, đau đầu, buồn nôn, nhìn mờ) - NGUY HIỂM",
                "Thị lực - nhìn mờ kéo dài 4-6 giờ là bình thường",
                "Dấu hiệu nhạy cảm với ánh sáng - kéo dài 4-6 giờ là bình thường",
                "Dấu hiệu kích ứng mắt (đỏ, rát)"
            ],
            "precautions": [
                "CHỐNG CHỈ ĐỊNH ở tăng nhãn áp góc đóng (có thể gây tăng nhãn áp cấp tính) - NGUY HIỂM",
                "CHỐNG CHỈ ĐỊNH ở bệnh nhân có tiền sử tăng nhãn áp góc đóng",
                "Kiểm tra nhãn áp trước khi dùng ở bệnh nhân có nguy cơ",
                "Nhìn mờ kéo dài 4-6 giờ - bệnh nhân không nên lái xe hoặc vận hành máy móc",
                "Nhạy cảm với ánh sáng kéo dài 4-6 giờ - bệnh nhân nên đeo kính râm",
                "Có thể hấp thu toàn thân và gây tác dụng phụ (khô miệng, nhịp nhanh) - hiếm",
                "Thận trọng ở trẻ em <3 tháng tuổi",
                "Thận trọng ở bệnh nhân đeo kính áp tròng (benzalkonium chloride có thể làm hỏng kính)",
                "Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào (nguy cơ nhiễm trùng)"
            ],
            "pharmacokinetics": {
                "half_life": "2-4 giờ (huyết tương, nếu hấp thu toàn thân), nhưng tác dụng tại mắt kéo dài",
                "onset": "15-30 phút",
                "duration": "4-6 giờ",
                "protein_binding": "Không rõ",
                "metabolism": "Chuyển hóa tại mắt và gan (nếu hấp thu toàn thân)",
                "clearance": "Thải trừ qua thận (nếu hấp thu toàn thân)"
            },
            "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Đóng nắp kín sau khi dùng. Dùng trong 4 tuần sau khi mở.",
            "black_box_warnings": "NGUY CƠ TĂNG NHÃN ÁP CẤP TÍNH (angle-closure glaucoma) ở bệnh nhân tăng nhãn áp góc đóng. CHỐNG CHỈ ĐỊNH ở tăng nhãn áp góc đóng và bệnh nhân có tiền sử tăng nhãn áp góc đóng. Phải kiểm tra nhãn áp trước khi dùng ở bệnh nhân có nguy cơ.",
            "drug_interactions": {
                "major": [
                    {
                        "drug": "Anticholinergic đường uống (Atropine, Scopolamine, Oxybutynin)",
                        "mechanism": "Tác dụng hiệp đồng ức chế muscarinic receptors",
                        "effect": "Tăng nguy cơ tác dụng phụ toàn thân (khô miệng, nhịp nhanh, táo bón, bí tiểu)",
                        "management": "Thận trọng. Theo dõi dấu hiệu tác dụng phụ toàn thân."
                    },
                    {
                        "drug": "Thuốc chống trầm cảm ba vòng (Amitriptyline, Imipramine)",
                        "mechanism": "Có tác dụng anticholinergic, tác dụng hiệp đồng",
                        "effect": "Tăng nguy cơ tác dụng phụ toàn thân",
                        "management": "Thận trọng. Theo dõi dấu hiệu tác dụng phụ toàn thân."
                    }
                ],
                "moderate": [],
                "minor": []
            },
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng tropicamide hoặc anticholinergic",
                    "Tăng nhãn áp góc đóng (angle-closure glaucoma) - CHỐNG CHỈ ĐỊNH (nguy cơ tăng nhãn áp cấp tính)",
                    "Bệnh nhân có tiền sử tăng nhãn áp góc đóng - CHỐNG CHỈ ĐỊNH"
                ],
                "tương_đối": [
                    "Trẻ em <3 tháng tuổi - thận trọng",
                    "Bệnh nhân có nguy cơ tăng nhãn áp góc đóng - kiểm tra nhãn áp trước khi dùng",
                    "Bệnh nhân đeo kính áp tròng - thận trọng (benzalkonium chloride)",
                    "Có thai (category C) - thận trọng"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Tropicamide là thuốc phân loại C. Tropicamide có thể hấp thu toàn thân và qua nhau thai. Anticholinergic có thể gây tác dụng phụ ở thai nhi. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt khi không có lựa chọn khác.",
                "lactation": {
                    "safety": "Compatible with Caution",
                    "details": "Tropicamide có thể hấp thu toàn thân và bài tiết vào sữa mẹ. Tuy nhiên, nồng độ trong sữa mẹ thấp khi dùng tại mắt và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ.",
                    "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng. Nồng độ trong sữa mẹ thấp."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh liều",
                "moderate": "Không cần điều chỉnh liều",
                "severe": "Không cần điều chỉnh liều (ophthalmic, hấp thu tối thiểu)",
                "notes": "Tropicamide dùng tại mắt, hấp thu toàn thân tối thiểu. Không cần điều chỉnh liều ở bệnh nhân suy gan."
            },
            "overdose_management": {
                "symptoms": [
                    "Tăng nhãn áp cấp tính (angle-closure glaucoma) - NGUY HIỂM",
                    "Nhìn mờ nặng",
                    "Nhạy cảm với ánh sáng nặng",
                    "Hấp thu toàn thân: khô miệng nặng, nhịp nhanh, táo bón, bí tiểu"
                ],
                "antidote": "Pilocarpine (cholinergic) để co đồng tử và giảm nhãn áp. Physostigmine cho tác dụng phụ toàn thân.",
                "treatment": [
                    "Nếu tăng nhãn áp cấp tính:",
                    "  - Pilocarpine 1-2% nhỏ mắt để co đồng tử",
                    "  - Thuốc giảm nhãn áp (timolol, dorzolamide)",
                    "  - Acetazolamide uống hoặc IV nếu cần",
                    "  - Khám mắt ngay",
                    "Nếu hấp thu toàn thân nặng:",
                    "  - Physostigmine 1-2mg IV (đối kháng anticholinergic)",
                    "  - Hỗ trợ hô hấp nếu cần",
                    "Theo dõi: Thị lực, nhãn áp, nhịp tim, huyết áp, hô hấp"
                ],
                "monitoring": "Theo dõi thị lực, nhãn áp, nhịp tim, huyết áp, hô hấp cho đến khi hồi phục. Theo dõi lâu hơn nếu có biến chứng (tăng nhãn áp cấp tính)."
            },
            "reversal_agents": {
                "available": True,
                "agents": [
                    {
                        "agent": "Pilocarpine",
                        "mechanism": "Cholinergic (muscarinic agonist), co đồng tử và giảm nhãn áp",
                        "indication": "Tăng nhãn áp cấp tính do tropicamide",
                        "dose": "1-2% nhỏ mắt, 1 giọt mỗi 15 phút cho đến khi co đồng tử"
                    },
                    {
                        "agent": "Physostigmine",
                        "mechanism": "Cholinesterase inhibitor, đối kháng tác dụng anticholinergic",
                        "indication": "Tác dụng phụ toàn thân nặng do tropicamide",
                        "dose": "1-2mg IV, lặp lại mỗi 30-60 phút nếu cần"
                    }
                ],
                "notes": "Pilocarpine co đồng tử và giảm nhãn áp cho tăng nhãn áp cấp tính. Physostigmine đối kháng tác dụng anticholinergic cho tác dụng phụ toàn thân."
            },
            "administration_instructions": {
                "oral": None,
                "ophthalmic": {
                    "preparation": "Dạng dung dịch nhỏ mắt 0.5% hoặc 1%.",
                    "application": "1-2 giọt vào mắt cần khám, lặp lại sau 5 phút nếu cần. Nhắm mắt nhẹ 1-2 phút sau khi nhỏ. Nhấn nhẹ vào góc trong mắt (lacrimal sac) trong 1-2 phút để giảm hấp thu toàn thân.",
                    "timing": "Trước khi khám mắt. Tác dụng sau 15-30 phút, kéo dài 4-6 giờ.",
                    "contact_lenses": "Tháo kính áp tròng trước khi nhỏ. Đợi 15 phút trước khi đeo lại.",
                    "notes": "QUAN TRỌNG: 1) CHỐNG CHỈ ĐỊNH ở tăng nhãn áp góc đóng, 2) Nhìn mờ và nhạy cảm với ánh sáng kéo dài 4-6 giờ, 3) Bệnh nhân không nên lái xe hoặc vận hành máy móc, 4) Bệnh nhân nên đeo kính râm, 5) Tránh chạm đầu lọ vào mắt hoặc bất kỳ bề mặt nào."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Tropicamide (Mydriacyl)",
                    "UpToDate - Tropicamide: Drug Information",
                    "Medscape - Tropicamide Drug Reference",
                    "AAO Guidelines - Eye Examination"
                ],
                "last_updated": "2025-02-18",
                "evidence_level": "A - Dựa trên FDA drug labels, clinical guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
            },
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["Acute angle-closure glaucoma (if narrow-angle glaucoma)", "Systemic anticholinergic effects (dry mouth, tachycardia) with systemic absorption"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Intraocular pressure (IOP) - CRITICAL (check before and after use, especially in at-risk patients)", "Signs of acute angle-closure glaucoma (severe eye pain, headache, nausea, blurred vision)", "Visual acuity (blurred vision lasting 4-6 hours is normal)"]
            },
            "guideline_tags": [
                "AAO Guidelines - Eye Examination",
                "AAO Guidelines - Mydriasis",
                "FDA Drug Information - Tropicamide Ophthalmic",
                "FDA Black Box Warning - Tropicamide and Angle-Closure Glaucoma"
            ]
        },

}

__all__ = ['MYDRIATICS_DRUGS']
