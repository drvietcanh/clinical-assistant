#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Check existing data for drugs"""

from drugs.drug_database import DRUG_DATABASE
import json

drugs_to_check = ["Ramipril", "Metoprolol", "Atorvastatin", "Warfarin"]

for drug_name in drugs_to_check:
    drug_data = DRUG_DATABASE.get(drug_name, {})
    print(f"\n{'='*60}")
    print(f"{drug_name}:")
    print(f"{'='*60}")
    
    # Check contraindications
    if 'contraindications' in drug_data:
        print(f"Has 'contraindications': {type(drug_data['contraindications'])}")
        if isinstance(drug_data['contraindications'], dict):
            print(f"  Structure: {list(drug_data['contraindications'].keys())}")
    else:
        print("No 'contraindications' field")
    
    # Check other relevant fields
    for field in ['renal_adjustment', 'reversal_agents', 'black_box_warnings']:
        if field in drug_data:
            print(f"Has '{field}': {type(drug_data[field])}")
        else:
            print(f"No '{field}' field")


