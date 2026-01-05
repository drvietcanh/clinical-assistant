"""Tìm các thuốc thiếu field bổ sung"""
import sys
import json
from pathlib import Path
sys.path.insert(0, str(Path.cwd()))

from drugs.drug_database import DRUG_DATABASE
from drugs.drug_manager_tool import get_drug_manager
from drugs.field_validator import get_field_validator

manager = get_drug_manager()
validator = get_field_validator()

drugs_to_update = []

for drug_name, drug_data in DRUG_DATABASE.items():
    result = validator.validate_all_fields(drug_data)
    
    if len(result.get('missing_standard_fields', [])) == 0:
        missing_additional = result.get('missing_additional_fields', [])
        if missing_additional:
            files = manager.find_drug_file(drug_name)
            if files:
                drugs_to_update.append({
                    'name': drug_name,
                    'file': files[0],
                    'missing': missing_additional
                })

print(f"Found {len(drugs_to_update)} drugs missing additional fields")
for i, drug in enumerate(drugs_to_update[:20], 1):
    print(f"{i}. {drug['name']}: missing {len(drug['missing'])} fields - {', '.join(drug['missing'][:3])}")

