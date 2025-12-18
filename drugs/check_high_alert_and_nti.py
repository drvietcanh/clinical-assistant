"""
Check High-Alert and Narrow Therapeutic Index (NTI) Drug Candidates

Script này duyệt toàn bộ DRUG_DATABASE và gợi ý thuốc nào nên:
- gắn risk_flags.high_alert = True
- gắn risk_flags.narrow_therapeutic_index = True

TIÊU CHÍ (tham khảo ISMP, ICU practice, các database như UpToDate/DrugBank):
- High-alert:
  * Thuốc vận mạch / catecholamine (epinephrine, norepinephrine, dopamine, dobutamine...)
  * Thuốc chống đông (heparin, enoxaparin, fondaparinux, warfarin, DOACs)
  * Insulin
  * Opioids mạnh (morphine, fentanyl, hydromorphone, oxycodone...)
  * Thuốc chống loạn nhịp (amiodarone, lidocaine tiêm...)
  * Một số thuốc gây mê/an thần mạnh (propofol, ketamine, midazolam IV...)
  * Hóa trị/oncology agents

- NTI (narrow therapeutic index):
  * Digoxin, theophylline
  * Aminoglycosides (gentamicin, amikacin, tobramycin...)
  * Vancomycin
  * Carbamazepine, phenytoin, valproate, lithium
  * Warfarin và một số thuốc chống đông khác
  * Một số thuốc chống loạn nhịp

LƯU Ý:
- Script CHỈ GỢI Ý, KHÔNG tự động chỉnh sửa database.
- Output dưới dạng bảng text/markdown để bác sĩ review rồi mới cập nhật vào risk_flags.
"""

from drugs.drug_database import DRUG_DATABASE


# Các danh sách tên thuốc/ngữ cảnh dùng để nhận diện
HIGH_ALERT_NAME_KEYWORDS = {
    # Anticoagulants / antiplatelets
    "Warfarin",
    "Heparin",
    "Enoxaparin",
    "Fondaparinux",
    "Rivaroxaban",
    "Apixaban",
    "Dabigatran",
    "Edoxaban",
    # Insulin
    "Insulin",
    # Vasopressors / inotropes / antiarrhythmics
    "Epinephrine",
    "Adrenaline",
    "Norepinephrine",
    "Noradrenaline",
    "Dopamine",
    "Dobutamine",
    "Amiodarone",
    "Lidocaine",
    # Opioids (đặc biệt đường IV / mạnh)
    "Morphine",
    "Fentanyl",
    "Hydromorphone",
    "Oxycodone",
    "Methadone",
    "Buprenorphine",
    # Chemo / oncology (nhiều thuốc nguy cơ cao)
    "Cisplatin",
    "Carboplatin",
    "Oxaliplatin",
    "Cyclophosphamide",
    "Ifosfamide",
    "Doxorubicin",
    "Paclitaxel",
    "Docetaxel",
    "Methotrexate",
}

NTI_NAME_KEYWORDS = {
    "Digoxin",
    "Theophylline",
    "Carbamazepine",
    "Phenytoin",
    "Valproate",
    "Valproic acid",
    "Lithium",
    # Aminoglycosides
    "Gentamicin",
    "Amikacin",
    "Tobramycin",
    # Vancomycin / một số kháng sinh cần TDM
    "Vancomycin",
}


def is_high_alert(drug_name: str, drug_data: dict) -> bool:
    """Heuristic xác định thuốc high-alert dựa trên tên và group."""
    name = drug_name.lower()
    group = str(drug_data.get("group", "")).lower()

    # 1) Match theo tên cụ thể
    for key in HIGH_ALERT_NAME_KEYWORDS:
        if key.lower() in name:
            return True

    # 2) Theo group/chuyên khoa
    high_risk_group_keywords = [
        "anticoagulant",
        "antiplatelet",
        "thrombolytic",
        "vasopressor",
        "inotrope",
        "antiarrhythmic",
        "opioid",
        "chemotherapy",
        "oncology",
        "immunosuppressant",
    ]
    if any(kw in group for kw in high_risk_group_keywords):
        return True

    # 3) Theo đường dùng + nhóm đặc biệt (ví dụ insulin tiêm, opioid tiêm)
    routes = [r.lower() for r in drug_data.get("administration", [])]
    if "iv" in routes:
        if "insulin" in name or "morphine" in name or "fentanyl" in name:
            return True

    return False


def is_narrow_therapeutic_index(drug_name: str, drug_data: dict) -> bool:
    """Heuristic xác định thuốc NTI dựa trên tên và group."""
    name = drug_name.lower()
    group = str(drug_data.get("group", "")).lower()

    for key in NTI_NAME_KEYWORDS:
        if key.lower() in name:
            return True

    nti_group_keywords = [
        "aminoglycoside",
        "antiarrhythmic",
        "anticonvulsant",
        "antiepileptic",
        "tdm",  # các thuốc được đánh dấu trong modules TDM
    ]
    if any(kw in group for kw in nti_group_keywords):
        return True

    return False


def analyze_high_alert_and_nti():
    """
    Duyệt toàn bộ DRUG_DATABASE và in báo cáo:
    - Gợi ý high-alert
    - Gợi ý NTI
    Đồng thời cho biết thuốc đã có risk_flags trước đó để tránh trùng.
    """
    high_alert_candidates = []
    nti_candidates = []

    for name, data in DRUG_DATABASE.items():
        risk_flags = data.get("risk_flags", {}) or {}
        already_high_alert = bool(risk_flags.get("high_alert"))
        already_nti = bool(risk_flags.get("narrow_therapeutic_index"))

        suggested_high_alert = is_high_alert(name, data)
        suggested_nti = is_narrow_therapeutic_index(name, data)

        if suggested_high_alert and not already_high_alert:
            high_alert_candidates.append(
                {
                    "name": name,
                    "group": data.get("group", ""),
                    "routes": ", ".join(data.get("administration", [])),
                }
            )

        if suggested_nti and not already_nti:
            nti_candidates.append(
                {
                    "name": name,
                    "group": data.get("group", ""),
                    "routes": ", ".join(data.get("administration", [])),
                }
            )

    # In kết quả dưới dạng bảng đơn giản (có thể copy sang markdown)
    print("# Gợi ý gắn risk_flags.high_alert\n")
    print(f"Tổng số gợi ý mới: {len(high_alert_candidates)}\n")
    print("| Tên thuốc | Nhóm | Đường dùng |")
    print("|-----------|------|------------|")
    for item in sorted(high_alert_candidates, key=lambda x: x["name"].lower()):
        print(
            f"| {item['name']} | {item['group']} | {item['routes'] or '-'} |"
        )

    print("\n\n# Gợi ý gắn risk_flags.narrow_therapeutic_index\n")
    print(f"Tổng số gợi ý mới: {len(nti_candidates)}\n")
    print("| Tên thuốc | Nhóm | Đường dùng |")
    print("|-----------|------|------------|")
    for item in sorted(nti_candidates, key=lambda x: x["name"].lower()):
        print(
            f"| {item['name']} | {item['group']} | {item['routes'] or '-'} |"
        )


if __name__ == "__main__":
    analyze_high_alert_and_nti()


