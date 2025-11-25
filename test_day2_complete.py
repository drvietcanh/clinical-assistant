"""Test Day 2 completion - Paracetamol and Salbutamol"""
import sys
from pathlib import Path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from drugs.drug_database import DRUG_DATABASE
from drugs.drug_utils.enhanced_fields_template import check_drug_enhancement_status

print("=" * 80)
print("🧪 DAY 2: PARACETAMOL & SALBUTAMOL ENHANCEMENT TEST")
print("=" * 80)
print()

# Test Paracetamol
p = DRUG_DATABASE.get('Paracetamol')
if p:
    p_status = check_drug_enhancement_status(p)
    print(f"✅ Paracetamol:")
    print(f"   Completeness: {p_status['completeness_percent']:.1f}%")
    print(f"   Fields: {p_status['present_fields']}/{p_status['total_fields']}")
    if p_status['missing_fields']:
        print(f"   ⚠️  Missing: {', '.join(p_status['missing_fields'])}")
    else:
        print(f"   ✅ All fields present!")
else:
    print("❌ Paracetamol not found")

print()

# Test Salbutamol
s = DRUG_DATABASE.get('Salbutamol')
if s:
    s_status = check_drug_enhancement_status(s)
    print(f"✅ Salbutamol:")
    print(f"   Completeness: {s_status['completeness_percent']:.1f}%")
    print(f"   Fields: {s_status['present_fields']}/{s_status['total_fields']}")
    if s_status['missing_fields']:
        print(f"   ⚠️  Missing: {', '.join(s_status['missing_fields'])}")
    else:
        print(f"   ✅ All fields present!")
else:
    print("❌ Salbutamol not found")

print()
print("=" * 80)
if p and s:
    p_complete = len(p_status['missing_fields']) == 0
    s_complete = len(s_status['missing_fields']) == 0
    if p_complete and s_complete:
        print("✅ DAY 2 COMPLETE: Both drugs fully enhanced!")
    else:
        print("⚠️  DAY 2 IN PROGRESS: Some fields still missing")
print("=" * 80)

