"""Test Paracetamol enhancement status"""
import sys
from pathlib import Path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from drugs.drug_database import DRUG_DATABASE
from drugs.drug_utils.enhanced_fields_template import check_drug_enhancement_status

p = DRUG_DATABASE.get('Paracetamol')
if p:
    s = check_drug_enhancement_status(p)
    print(f"Paracetamol completeness: {s['completeness_percent']:.1f}%")
    print(f"Present fields: {s['present_fields']}/{s['total_fields']}")
    print(f"Missing fields: {len(s['missing_fields'])}")
    if s['missing_fields']:
        print(f"Missing: {', '.join(s['missing_fields'][:5])}")
else:
    print("Paracetamol not found")

