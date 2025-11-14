"""
Template Script để Thêm Thuốc Mới vào Database
Hướng dẫn sử dụng và template cho thuốc mới
"""

# ============================================================================
# TEMPLATE THÊM THUỐC MỚI
# ============================================================================

NEW_DRUG_TEMPLATE = {
    "name": "Tên Thuốc",
    "generic_name": "Tên chung (generic name)",
    "brand_names": ["Biệt dược 1", "Biệt dược 2", "Biệt dược 3"],
    "group": "Nhóm thuốc (Cardiovascular, Diabetes, etc.)",
    "category": "Phân loại chi tiết (ACE Inhibitor, SSRI, etc.)",
    "indications": [
        "Chỉ định 1",
        "Chỉ định 2",
        "Chỉ định 3"
    ],
    "contraindications": [
        "Chống chỉ định 1",
        "Chống chỉ định 2"
    ],
    "dosage": {
        "adult": {
            "oral": "Liều uống: X mg/lần, Y lần/ngày",
            "iv": "Liều tiêm tĩnh mạch: X mg/lần",
            "im": "Liều tiêm bắp: X mg/lần"
        },
        "pediatric": {
            "oral": "Liều uống trẻ em: X mg/kg/lần",
            "iv": "Liều tiêm tĩnh mạch trẻ em: X mg/kg/lần"
        },
        "elderly": "Điều chỉnh liều cho người cao tuổi",
        "notes": "Ghi chú về liều dùng"
    },
    "renal_adjustment": {
        "crcl_30_50": "Điều chỉnh CrCl 30-50: Giảm 25-50%",
        "crcl_10_30": "Điều chỉnh CrCl 10-30: Giảm 50%",
        "crcl_<10": "Điều chỉnh CrCl <10: Giảm 75% hoặc tránh dùng",
        "hd": "Hemodialysis: Bổ sung sau lọc máu",
        "pd": "Peritoneal dialysis: Điều chỉnh liều"
    },
    "hepatic_adjustment": {
        "mild": "Suy gan nhẹ: Không cần điều chỉnh",
        "moderate": "Suy gan trung bình: Giảm 50%",
        "severe": "Suy gan nặng: Tránh dùng hoặc giảm 75%"
    },
    "side_effects": [
        "Tác dụng phụ thường gặp 1",
        "Tác dụng phụ thường gặp 2",
        "Tác dụng phụ hiếm gặp nhưng nghiêm trọng"
    ],
    "interactions": [
        "Tương tác với thuốc X: Tăng nguy cơ...",
        "Tương tác với thuốc Y: Giảm hiệu quả..."
    ],
    "pregnancy_lactation": {
        "pregnancy_category": "Category X (hoặc A, B, C, D)",
        "pregnancy_notes": "Ghi chú về sử dụng trong thai kỳ",
        "lactation": "An toàn/không an toàn khi cho con bú"
    },
    "notes": "Ghi chú quan trọng khác",
    "enhanced_fields": {
        "mechanism_of_action": "Cơ chế tác dụng chi tiết. Ví dụ: Ức chế enzyme X, dẫn đến...",
        "monitoring": "Các thông số cần theo dõi: Chức năng gan, thận, điện giải, huyết áp, nhịp tim, etc.",
        "precautions": "Lưu ý và thận trọng: Suy gan, suy thận, người cao tuổi, trẻ em, etc.",
        "pharmacokinetics": "Dược động học: T1/2 = X giờ, protein binding = Y%, metabolism = gan, excretion = thận",
        "storage": "Điều kiện bảo quản: Nhiệt độ phòng, tránh ánh sáng, độ ẩm, etc.",
        "black_box_warnings": "Cảnh báo hộp đen (nếu có): Nguy cơ X, Y, Z",
        # 8 fields tùy chọn (Phase 2)
        "drug_interactions": "Tương tác thuốc chi tiết với cơ chế",
        "contraindications_detailed": "Chống chỉ định phân loại chi tiết",
        "pregnancy_lactation_detailed": "Thai kỳ và cho con bú chi tiết",
        "hepatic_adjustment_detailed": "Điều chỉnh liều suy gan chi tiết",
        "overdose_management": "Xử trí quá liều: Triệu chứng, điều trị, chất đối kháng",
        "reversal_agents": "Chất đối kháng (nếu có): Naloxone, Flumazenil, etc.",
        "administration_instructions": "Hướng dẫn dùng chi tiết: Cách pha, tốc độ truyền, tương thích",
        "references": "Tài liệu tham khảo: FDA Label, UpToDate, Guidelines"
    }
}

# ============================================================================
# HƯỚNG DẪN SỬ DỤNG
# ============================================================================

USAGE_INSTRUCTIONS = """
# HƯỚNG DẪN THÊM THUỐC MỚI

## Bước 1: Chuẩn bị thông tin
1. Thu thập thông tin từ:
   - FDA Drug Labels (https://www.fda.gov/drugs)
   - UpToDate, Medscape
   - Goodman & Gilman, Katzung
   - Clinical guidelines
   - Vietnamese drug database

## Bước 2: Xác định file module
- Xem danh sách modules trong `drugs/drug_modules/`
- Xác định nhóm thuốc phù hợp
- Mở file module tương ứng

## Bước 3: Thêm thuốc
1. Copy template trên
2. Điền thông tin đầy đủ
3. Thêm vào dictionary trong file module
4. Đảm bảo format đúng (dấu phẩy, ngoặc, etc.)

## Bước 4: Cập nhật DRUG_GROUPS
- Mở `drugs/drug_utils/groups.py`
- Thêm tên thuốc vào nhóm tương ứng

## Bước 5: Validate
```bash
python check_enhanced_fields.py
python -c "from drugs.drug_database import DRUG_DATABASE; print(len(DRUG_DATABASE))"
```

## Bước 6: Test
- Test search: Tìm kiếm thuốc mới
- Test display: Hiển thị thông tin thuốc
- Test enhanced fields: Kiểm tra các fields hiển thị đúng

## Bước 7: Commit
- Commit với message rõ ràng
- Cập nhật documentation
"""

# ============================================================================
# VÍ DỤ CỤ THỂ
# ============================================================================

EXAMPLE_DRUG = {
    "Paracetamol": {
        "name": "Paracetamol",
        "generic_name": "Acetaminophen",
        "brand_names": ["Panadol", "Tylenol", "Efferalgan"],
        "group": "Analgesics",
        "category": "Analgesic/Antipyretic",
        "indications": [
            "Giảm đau nhẹ đến trung bình",
            "Hạ sốt",
            "Đau đầu, đau răng, đau cơ"
        ],
        "contraindications": [
            "Quá mẫn với paracetamol",
            "Suy gan nặng"
        ],
        "dosage": {
            "adult": {
                "oral": "500-1000 mg/lần, tối đa 4g/ngày",
                "iv": "1000 mg/lần, mỗi 6-8 giờ"
            },
            "pediatric": {
                "oral": "10-15 mg/kg/lần, mỗi 4-6 giờ"
            },
            "notes": "Không vượt quá 4g/ngày ở người lớn"
        },
        "renal_adjustment": {
            "crcl_30_50": "Không cần điều chỉnh",
            "crcl_10_30": "Giảm liều 25%",
            "crcl_<10": "Giảm liều 50%"
        },
        "side_effects": [
            "Hiếm: Phát ban, mày đay",
            "Quá liều: Độc tính gan"
        ],
        "interactions": [
            "Warfarin: Tăng nguy cơ chảy máu",
            "Rượu: Tăng nguy cơ độc tính gan"
        ],
        "pregnancy_lactation": {
            "pregnancy_category": "B",
            "pregnancy_notes": "An toàn trong thai kỳ",
            "lactation": "An toàn khi cho con bú"
        },
        "notes": "Thuốc giảm đau/hạ sốt phổ biến nhất. Cẩn thận quá liều gây độc tính gan.",
        "enhanced_fields": {
            "mechanism_of_action": "Ức chế enzyme cyclooxygenase (COX) trong hệ thần kinh trung ương, dẫn đến giảm tổng hợp prostaglandin và giảm cảm giác đau, hạ sốt.",
            "monitoring": "Chức năng gan (ALT, AST) nếu dùng kéo dài hoặc liều cao. Dấu hiệu quá liều: buồn nôn, nôn, đau bụng.",
            "precautions": "Suy gan, nghiện rượu, suy dinh dưỡng. Không vượt quá 4g/ngày. Cẩn thận với các sản phẩm kết hợp chứa paracetamol.",
            "pharmacokinetics": "T1/2 = 1-3 giờ. Protein binding = 10-25%. Metabolism = gan (CYP2E1). Excretion = thận (90% dạng glucuronide và sulfate).",
            "storage": "Nhiệt độ phòng, tránh ẩm. Bảo quản ở 15-30°C.",
            "black_box_warnings": "Quá liều có thể gây suy gan cấp, tử vong. Điều trị: N-acetylcysteine (NAC).",
            "drug_interactions": "Warfarin: Tăng INR, nguy cơ chảy máu. Rượu: Tăng nguy cơ độc tính gan. Phenytoin, Carbamazepine: Tăng chuyển hóa paracetamol.",
            "overdose_management": "Triệu chứng: Buồn nôn, nôn, đau bụng, vàng da, suy gan. Điều trị: N-acetylcysteine (NAC) trong vòng 8-10 giờ đầu. Liều: 150 mg/kg IV trong 15 phút, sau đó 50 mg/kg trong 4 giờ, sau đó 100 mg/kg trong 16 giờ.",
            "reversal_agents": "N-acetylcysteine (NAC) - chất giải độc cho quá liều paracetamol",
            "administration_instructions": "Uống với nước. Có thể uống trước hoặc sau ăn. IV: Pha trong 100ml NaCl 0.9%, truyền trong 15 phút.",
            "references": "FDA Label, UpToDate - Acetaminophen, WHO Essential Medicines List"
        }
    }
}

# ============================================================================
# DANH SÁCH THUỐC CẦN BỔ SUNG (Từ checklist)
# ============================================================================

DRUGS_TO_ADD = [
    # Giai đoạn 1 - Ưu tiên cao nhất (10 thuốc)
    "Paracetamol",
    "Salbutamol",
    "Acyclovir",
    "Valacyclovir",
    "Fluconazole",
    "Levofloxacin",
    "Fluoxetine",
    "Loratadine",
    "Cetirizine",
    "Fexofenadine",
    
    # Giai đoạn 2 - Ưu tiên cao (7 thuốc)
    "Trimethoprim-sulfamethoxazole",
    "Oseltamivir",
    "Ganciclovir",
    "Itraconazole",
    "Voriconazole",
    "Nystatin",
    "Ribavirin",
    
    # Giai đoạn 2 - Ưu tiên trung bình (18 thuốc)
    "Isosorbide mononitrate",
    "Gabapentin",
    "Pregabalin",
    "Desloratadine",
    "Levocetirizine",
    "Salmeterol",
    "Ipratropium",
    "Tiotropium",
    "Budesonide inhaled",
    "Fluticasone inhaled",
    "Lansoprazole",
    "Esomeprazole",
    "Domperidone",
    "Granisetron",
    "Palonosetron",
    "Methotrexate",
    "Budesonide",
    "Sumatriptan",
]

# ============================================================================
# FILE MODULES TƯƠNG ỨNG
# ============================================================================

MODULE_MAPPING = {
    "Paracetamol": "analgesics/analgesicantipyretic.py",
    "Salbutamol": "respiratory/short_acting_beta_2_agonist_sabas.py",
    "Acyclovir": "antimicrobial/antivirals.py",
    "Valacyclovir": "antimicrobial/antivirals.py",
    "Fluconazole": "antimicrobial/antifungals.py",
    "Levofloxacin": "infectious_other/fluoroquinolones.py",
    "Fluoxetine": "neurological/ssri_selective_serotonin_reuptake_inhibitors.py",
    "Loratadine": "supportive/antihistamine_h1_antagonist_2nd_generations.py",
    "Cetirizine": "supportive/antihistamine_h1_antagonist_2nd_generations.py",
    "Fexofenadine": "supportive/antihistamine_h1_antagonist_2nd_generations.py",
    # ... thêm các mapping khác
}

if __name__ == "__main__":
    print("=" * 60)
    print("📋 TEMPLATE THÊM THUỐC MỚI")
    print("=" * 60)
    print()
    print("Sử dụng template này để thêm thuốc mới vào database.")
    print()
    print(f"Tổng số thuốc cần bổ sung: {len(DRUGS_TO_ADD)}")
    print()
    print("Danh sách thuốc:")
    for i, drug in enumerate(DRUGS_TO_ADD, 1):
        print(f"  {i}. {drug}")
    print()
    print("Xem chi tiết trong:")
    print("  - drugs/DRUG_EXPANSION_PLAN.md")
    print("  - drugs/DRUG_EXPANSION_CHECKLIST.md")

