from drugs.drug_modules import ALL_DRUGS

REQUIRED_FIELDS = ['group', 'vietnamese_name', 'administration', 'indications', 'contraindications']
OPTIONAL_FIELDS = ['side_effects', 'precautions', 'dosing', 'interactions']

missing_stats = {field: 0 for field in REQUIRED_FIELDS}
total_drugs = len(ALL_DRUGS)

print(f"Checking {total_drugs} drugs for missing fields...")
print("-" * 50)

for drug_name, drug_data in ALL_DRUGS.items():
    if not isinstance(drug_data, dict):
        continue
    
    for field in REQUIRED_FIELDS:
        if field not in drug_data:
            missing_stats[field] += 1
            # print(f"Drug '{drug_name}' missing '{field}'")

print("Missing Fields Statistics:")
for field, count in missing_stats.items():
    if count > 0:
        print(f"{field:<20}: {count} drugs ({count/total_drugs*100:.1f}%)")

if all(count == 0 for count in missing_stats.values()):
    print("All drugs have required fields!")
