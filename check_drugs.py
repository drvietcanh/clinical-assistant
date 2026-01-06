from drugs.drug_database import DRUG_DATABASE

drugs_to_check = [
    'Azelastine/Fluticasone nasal spray',
    'Cetirizine/Pseudoephedrine',
    'Fexofenadine/Pseudoephedrine',
    'Folic acid',
    'Hydrocortisone topical',
    'Insulin',
    'Iron',
    'Loratadine/Pseudoephedrine'
]

for drug_name in drugs_to_check:
    if drug_name in DRUG_DATABASE:
        drug_data = DRUG_DATABASE[drug_name]
        has_rf = 'risk_flags' in drug_data and drug_data.get('risk_flags') is not None
        has_gt = 'guideline_tags' in drug_data and drug_data.get('guideline_tags') is not None
        print(f"{drug_name}:")
        print(f"  risk_flags: {has_rf}")
        print(f"  guideline_tags: {has_gt}")
        if has_rf:
            print(f"  risk_flags value: {drug_data.get('risk_flags')}")
        if has_gt:
            print(f"  guideline_tags value: {drug_data.get('guideline_tags')}")
        print()
    else:
        print(f"{drug_name}: NOT FOUND IN DATABASE")
        print()
