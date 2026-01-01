import sys
import os

# Add the project root to the python path
sys.path.append(r'd:\1 medical')

from drugs.drug_modules.cardiovascular.statins import STATINS_DRUGS
from drugs.drug_modules.cardiovascular.calcium_blockers.non_dihydropyridines import NON_DIHYDROPYRIDINE_CCB
from drugs.drug_modules.cardiovascular.calcium_blockers.dihydropyridines import DIHYDROPYRIDINE_CCB
from drugs.drug_modules.cardiovascular.beta_blockers.selective import SELECTIVE_BETA_BLOCKERS
from drugs.drug_modules.cardiovascular.beta_blockers.non_selective import NON_SELECTIVE_BETA_BLOCKERS
from drugs.drug_modules.cardiovascular.diuretics import DIURETICS

def check_drug(name, data):
    missing = []
    if "risk_flags" not in data:
        missing.append("risk_flags")
    if "guideline_tags" not in data:
        missing.append("guideline_tags")
    
    if missing:
        print(f"[FAIL] {name}: Missing {', '.join(missing)}")
    else:
        print(f"[PASS] {name}")

print("--- Verifying Statins ---")
for drug, data in STATINS_DRUGS.items():
    check_drug(drug, data)

print("\n--- Verifying Non-Dihydropyridine CCBs ---")
for drug, data in NON_DIHYDROPYRIDINE_CCB.items():
    check_drug(drug, data)

print("\n--- Verifying Dihydropyridine CCBs ---")
for drug, data in DIHYDROPYRIDINE_CCB.items():
    check_drug(drug, data)

print("\n--- Verifying Selective Beta Blockers ---")
for drug, data in SELECTIVE_BETA_BLOCKERS.items():
    check_drug(drug, data)

print("\n--- Verifying Non-Selective Beta Blockers ---")
for drug, data in NON_SELECTIVE_BETA_BLOCKERS.items():
    check_drug(drug, data)

print("\n--- Verifying Diuretics ---")
for drug, data in DIURETICS.items():
    check_drug(drug, data)
