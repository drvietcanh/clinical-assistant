"""Test Paracetamol enhancement"""
import sys
from pathlib import Path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from drugs.drug_database import DRUG_DATABASE
from drugs.drug_utils.enhanced_fields_template import check_drug_enhancement_status

p = DRUG_DATABASE.get('Paracetamol')
if p:
    status = check_drug_enhancement_status(p)
    print('Paracetamol Enhancement Status:')
    print(f'  Completeness: {status["completeness_percent"]:.1f}%')
    print(f'  Present fields: {len(status["present_field_names"])}')
    print(f'  Missing fields: {len(status["missing_fields"])}')
    print(f'  Present: {", ".join(status["present_field_names"][:5])}...')
    print(f'  Missing: {", ".join(status["missing_fields"][:5])}...')
else:
    print('Paracetamol not found in database')

