"""
List summary of risk_flags (high_alert & narrow_therapeutic_index) for all drugs

Mục tiêu:
- Sau khi đã gắn risk_flags qua enhanced_fields_overrides,
  script này sẽ in ra:
  * Danh sách tất cả thuốc high-alert
  * Danh sách tất cả thuốc NTI (narrow therapeutic index)
  * Một bảng tổng hợp (có thể copy sang Markdown/Excel) để review.
"""

from drugs.drug_database import DRUG_DATABASE


def list_risk_flags_summary():
    high_alert = []
    nti = []

    for name, data in DRUG_DATABASE.items():
        rf = data.get("risk_flags") or {}
        if rf.get("high_alert"):
            high_alert.append(
                {
                    "name": name,
                    "group": data.get("group", ""),
                    "routes": ", ".join(data.get("administration", [])),
                }
            )
        if rf.get("narrow_therapeutic_index"):
            nti.append(
                {
                    "name": name,
                    "group": data.get("group", ""),
                    "routes": ", ".join(data.get("administration", [])),
                }
            )

    print("# Thuốc high-alert (risk_flags.high_alert = True)\n")
    print(f"Tổng số: {len(high_alert)}\n")
    print("| Tên thuốc | Nhóm | Đường dùng |")
    print("|-----------|------|------------|")
    for item in sorted(high_alert, key=lambda x: x["name"].lower()):
        print(
            f"| {item['name']} | {item['group']} | {item['routes'] or '-'} |"
        )

    print("\n\n# Thuốc narrow therapeutic index (risk_flags.narrow_therapeutic_index = True)\n")
    print(f"Tổng số: {len(nti)}\n")
    print("| Tên thuốc | Nhóm | Đường dùng |")
    print("|-----------|------|------------|")
    for item in sorted(nti, key=lambda x: x["name"].lower()):
        print(
            f"| {item['name']} | {item['group']} | {item['routes'] or '-'} |"
        )


if __name__ == "__main__":
    list_risk_flags_summary()


