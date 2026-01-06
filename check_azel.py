import importlib
import sys

# Clear cache
if 'drugs.drug_database' in sys.modules:
    del sys.modules['drugs.drug_database']
if 'drugs.drug_modules.ent_oral_nasal_combinations' in sys.modules:
    del sys.modules['drugs.drug_modules.ent_oral_nasal_combinations']
if 'drugs.drug_modules' in sys.modules:
    del sys.modules['drugs.drug_modules']
if 'drugs.drug_modules.supportive' in sys.modules:
    del sys.modules['drugs.drug_modules.supportive']
if 'drugs.drug_modules.supportive.folates' in sys.modules:
    del sys.modules['drugs.drug_modules.supportive.folates']
if 'drugs.drug_modules.supportive.irons' in sys.modules:
    del sys.modules['drugs.drug_modules.supportive.irons']

from drugs.drug_database import DRUG_DATABASE

azel = DRUG_DATABASE.get('Azelastine/Fluticasone nasal spray', {})
print('Azelastine/Fluticasone nasal spray:')
print('  Has risk_flags:', 'risk_flags' in azel)
print('  Has guideline_tags:', 'guideline_tags' in azel)
if 'risk_flags' in azel:
    print('  risk_flags:', azel['risk_flags'])
if 'guideline_tags' in azel:
    print('  guideline_tags:', azel['guideline_tags'])

fol = DRUG_DATABASE.get('Folic acid', {})
print('\nFolic acid:')
print('  Has risk_flags:', 'risk_flags' in fol)
print('  Has guideline_tags:', 'guideline_tags' in fol)
if 'risk_flags' in fol:
    print('  risk_flags:', fol['risk_flags'])
if 'guideline_tags' in fol:
    print('  guideline_tags:', fol['guideline_tags'])

iron = DRUG_DATABASE.get('Iron', {})
print('\nIron:')
print('  Has risk_flags:', 'risk_flags' in iron)
print('  Has guideline_tags:', 'guideline_tags' in iron)
if 'risk_flags' in iron:
    print('  risk_flags:', iron['risk_flags'])
if 'guideline_tags' in iron:
    print('  guideline_tags:', iron['guideline_tags'])
