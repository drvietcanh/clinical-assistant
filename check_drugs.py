"""Check if drugs are in all_drugs"""
import sys
sys.path.insert(0, '.')
from check_missing_fields_final import load_all_drugs, check_drug_fields

all_drugs = load_all_drugs()
drugs = ['Bumetanide', 'Torsemide', 'Simvastatin', 'Norepinephrine', 'Dopamine', 'Dobutamine']

for d in drugs:
    if d in all_drugs:
        print(f"{d}: FOUND - fields: {all_drugs[d]}")
        result = check_drug_fields(d, all_drugs[d])
        print(f"  Missing enhanced: {result['missing_enhanced']}")
    else:
        print(f"{d}: NOT FOUND")

