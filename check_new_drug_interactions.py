"""Script to check interactions for newly added drugs"""
from drugs.interactions_data import get_interaction

new_drugs = ['Cefoperazone', 'Cefpirome', 'Aripiprazole', 'Chlorpromazine', 'Nicardipine', 'Nisoldipine']
common_drugs = ['Warfarin', 'Aspirin', 'Digoxin', 'Metformin', 'Omeprazole', 'Ciprofloxacin', 'Ketoconazole', 'Clarithromycin']

print("Kiem tra interactions cho cac thuoc moi:")
print()

for drug in new_drugs:
    found = False
    interactions = []
    for common in common_drugs:
        interaction = get_interaction(drug, common)
        if interaction:
            interactions.append(f"{drug} <-> {common}: CO (Severity: {interaction.get('severity', 'Unknown')})")
            found = True
    
    if found:
        for inter in interactions:
            print(f"  {inter}")
    else:
        print(f"  {drug}: Chua co interactions trong database")
