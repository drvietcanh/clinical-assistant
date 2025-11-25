"""Test Salbutamol enhancement"""
import sys
from pathlib import Path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from drugs.drug_database import DRUG_DATABASE
from drugs.drug_utils.enhanced_fields_template import check_drug_enhancement_status

s = DRUG_DATABASE.get('Salbutamol')
if s:
    status = check_drug_enhancement_status(s)
    print('Salbutamol Enhancement Status:')
    print(f'  Completeness: {status["completeness_percent"]:.1f}%')
    print(f'  Present fields: {len(status["present_field_names"])}')
    print(f'  Missing fields: {len(status["missing_fields"])}')
    print(f'  Present: {", ".join(status["present_field_names"][:5])}...')
    if status["missing_fields"]:
        print(f'  Missing: {", ".join(status["missing_fields"][:5])}...')
    else:
        print('  Missing: None ✅')
else:
    print('Salbutamol not found in database')

