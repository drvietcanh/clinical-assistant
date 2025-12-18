"""
Generate EXTRA_ENHANCED_FIELDS overrides for risk_flags

Script này sử dụng cùng heuristic với check_high_alert_and_nti.py để:
- Duyệt DRUG_DATABASE
- Tìm các thuốc nên gắn:
    * risk_flags.high_alert = True
    * risk_flags.narrow_therapeutic_index = True
- Bỏ qua thuốc đã có risk_flags.high_alert / narrow_therapeutic_index trong data hiện tại
- Sinh ra đoạn code Python (dict) có thể copy vào EXTRA_ENHANCED_FIELDS
  trong enhanced_fields_overrides.py, ví dụ:

EXTRA_ENHANCED_FIELDS.update({
    "Heparin": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            ...
        }
    },
    ...
})

LƯU Ý:
- Script KHÔNG tự động ghi file; chỉ in ra gợi ý để bác sĩ/dev review.
"""

from drugs.drug_database import DRUG_DATABASE
from drugs.check_high_alert_and_nti import (
    is_high_alert,
    is_narrow_therapeutic_index,
)


def generate_risk_flags_overrides():
    """
    Sinh ra đoạn code EXTRA_ENHANCED_FIELDS.update({...}) cho các thuốc
    được heuristic gợi ý là high-alert / NTI nhưng chưa có flag tương ứng.
    """
    overrides = {}

    for name, data in DRUG_DATABASE.items():
        risk_flags = data.get("risk_flags", {}) or {}
        already_high_alert = bool(risk_flags.get("high_alert"))
        already_nti = bool(risk_flags.get("narrow_therapeutic_index"))

        suggested_high_alert = is_high_alert(name, data)
        suggested_nti = is_narrow_therapeutic_index(name, data)

        # Nếu không có gợi ý nào mới thì bỏ qua
        if not suggested_high_alert and not suggested_nti:
            continue

        # Nếu đã được gắn flag rồi thì cũng bỏ qua
        if (suggested_high_alert and already_high_alert) and (
            suggested_nti and already_nti
        ):
            continue

        # Chuẩn bị risk_flags mới, giữ lại flag đã có nếu có
        new_risk_flags = {
            "high_alert": already_high_alert or bool(suggested_high_alert),
            "narrow_therapeutic_index": already_nti or bool(suggested_nti),
            "look_alike_sound_alike": risk_flags.get(
                "look_alike_sound_alike", []
            ),
            "organ_toxicity": risk_flags.get(
                "organ_toxicity",
                {
                    "hepatic": "unknown",
                    "renal": "unknown",
                    "cardiac": "unknown",
                    "hematologic": "unknown",
                },
            ),
            "requires_double_check": risk_flags.get(
                "requires_double_check", bool(suggested_high_alert)
            ),
            "icu_critical_care_only": risk_flags.get(
                "icu_critical_care_only", False
            ),
        }

        overrides[name] = {
            "risk_flags": new_risk_flags,
        }

    # In dưới dạng code Python có thể copy vào enhanced_fields_overrides.py
    print("# Dán khối dưới đây vào enhanced_fields_overrides.py,")
    print("# ví dụ ngay trước dòng kết thúc EXTRA_ENHANCED_FIELDS.\n")
    print("EXTRA_ENHANCED_FIELDS.update({")

    for drug_name in sorted(overrides.keys(), key=lambda x: x.lower()):
        rf = overrides[drug_name]["risk_flags"]
        print(f'    "{drug_name}": {{')
        print("        \"risk_flags\": {")
        print(f"            \"high_alert\": {str(rf['high_alert'])},")
        print(
            f"            \"narrow_therapeutic_index\": {str(rf['narrow_therapeutic_index'])},"
        )
        print(
            f"            \"look_alike_sound_alike\": {rf['look_alike_sound_alike']!r},"
        )
        print(
            f"            \"organ_toxicity\": {rf['organ_toxicity']!r},"
        )
        print(
            f"            \"requires_double_check\": {str(rf['requires_double_check'])},"
        )
        print(
            f"            \"icu_critical_care_only\": {str(rf['icu_critical_care_only'])},"
        )
        print("        },")
        print("    },")

    print("})")


if __name__ == "__main__":
    generate_risk_flags_overrides()


