"""Test Salbutamol enhancement status"""
import sys
from pathlib import Path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from drugs.drug_database import DRUG_DATABASE
from drugs.drug_utils.enhanced_fields_template import check_drug_enhancement_status

s = DRUG_DATABASE.get('Salbutamol')
if s:
    status = check_drug_enhancement_status(s)
    print(f"Salbutamol completeness: {status['completeness_percent']:.1f}%")
    print(f"Present fields: {status['present_fields']}/{status['total_fields']}")
    print(f"Missing fields: {len(status['missing_fields'])}")
    if status['missing_fields']:
        print(f"Missing: {', '.join(status['missing_fields'])}")
else:
    print("Salbutamol not found")

