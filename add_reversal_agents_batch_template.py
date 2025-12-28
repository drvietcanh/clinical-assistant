#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Template script bổ sung reversal_agents cho nhiều thuốc trong một batch.

Mục tiêu:
- Chuẩn hóa format field reversal_agents
- Giảm thao tác lặp lại khi nhập cho nhiều thuốc (đặc biệt ICU/emergency)

Workflow gợi ý:
1. Chạy: python generate_missing_lists.py
2. Mở:  missing_lists.json → xem key "reversal_agents"
3. Chọn 10–20 thuốc ưu tiên (ICU/emergency, high-risk) cho batch
4. Điền dữ liệu vào REVERSAL_AGENTS_DATA theo format bên dưới
5. Chạy: python add_reversal_agents_batch_template.py
6. Copy block EXTRA_ENHANCED_FIELDS.update({...}) in ra → dán cuối drugs/enhanced_fields_overrides.py
7. Kiểm tra: python quick_validation_check.py --fields reversal_agents --top 5
"""

from __future__ import annotations

from typing import Dict, List, Any

from drugs.drug_database import DRUG_DATABASE


# TODO: Điền dữ liệu cho từng thuốc theo format dưới đây.
# GỢI Ý:
# - Nếu thuốc KHÔNG có antidote đặc hiệu → available=False, agents=[]
# - Nếu CÓ antidote → available=True, điền danh sách "agents"
REVERSAL_AGENTS_DATA: Dict[str, Dict[str, Any]] = {
    # Ví dụ cấu trúc (hãy sửa/ghi đè cho thuốc thật):
    #
    # "Alteplase": {
    #     "reversal_agents": {
    #         "available": False,
    #         "agents": [],
    #         "notes": "Không có thuốc giải độc đặc hiệu; xử trí chủ yếu là ngừng thuốc, hỗ trợ và đảo ngược chảy máu nếu cần.",
    #     },
    # },
    #
    # "Andexanet alfa": {
    #     "reversal_agents": {
    #         "available": True,
    #         "agents": [
    #             {
    #                 "name": "Andexanet alfa",
    #                 "dose": "Theo protocol tuỳ NOAC và thời điểm liều cuối",
    #                 "route": "IV",
    #                 "notes": "Thuốc giải độc cho rivaroxaban/apixaban; dùng theo guideline chuyên ngành.",
    #             }
    #         ],
    #         "notes": "CẦN XÁC MINH protocol liều chuẩn theo guideline hiện hành.",
    #     },
    # },
}


def generate_code() -> str:
    """Sinh block code EXTRA_ENHANCED_FIELDS.update(...) để dán vào overrides."""
    lines: List[str] = []
    lines.append(
        "\n# ======================== BATCH: REVERSAL AGENTS ===============================\n"
    )
    lines.append("# Bổ sung reversal_agents cho một số thuốc ưu tiên\n\n")
    lines.append("EXTRA_ENHANCED_FIELDS.update({\n")

    for drug_name, data in REVERSAL_AGENTS_DATA.items():
        field = data.get("reversal_agents", {})
        available = field.get("available", False)
        agents = field.get("agents", [])
        notes = field.get("notes", "")

        lines.append(f'    "{drug_name}": {{\n')
        lines.append('        "reversal_agents": {\n')

        # available
        lines.append(f"            \"available\": {str(bool(available))},\n")

        # agents
        lines.append('            "agents": [\n')
        for agent in agents:
            name = agent.get("name", "")
            dose = agent.get("dose", "")
            route = agent.get("route", "")
            agent_notes = agent.get("notes", "")
            lines.append("                {\n")
            lines.append(f'                    "name": "{name}",\n')
            lines.append(f'                    "dose": "{dose}",\n')
            lines.append(f'                    "route": "{route}",\n')
            lines.append(f'                    "notes": "{agent_notes}",\n')
            lines.append("                },\n")
        lines.append("            ],\n")

        # notes
        lines.append(f'            "notes": "{notes}",\n')

        lines.append("        },\n")
        lines.append("    },\n")

    lines.append("})\n")
    lines.append(
        "# ======================== END BATCH: REVERSAL AGENTS ==========================\n"
    )

    return "".join(lines)


def main() -> None:
    print("Kiểm tra các thuốc trong REVERSAL_AGENTS_DATA có nằm trong DRUG_DATABASE không:")
    for drug_name in REVERSAL_AGENTS_DATA.keys():
        if drug_name in DRUG_DATABASE:
            has_field = "reversal_agents" in DRUG_DATABASE[drug_name]
            status = "ĐÃ CÓ" if has_field else "THIẾU"
            print(f"  ✅ {drug_name}: {status} trong DRUG_DATABASE gốc")
        else:
            print(f"  ❌ {drug_name}: KHÔNG TÌM THẤY trong DRUG_DATABASE")

    print("\n" + "=" * 80)
    print("Code để thêm vào drugs/enhanced_fields_overrides.py:")
    print("=" * 80)
    print(generate_code())


if __name__ == "__main__":
    main()


