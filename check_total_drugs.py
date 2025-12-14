"""Script to check total number of drugs in database"""
from drugs.drug_database import DRUG_DATABASE, TOTAL_DRUGS

print(f"Tong so thuoc trong database: {TOTAL_DRUGS}")
print(f"Muc tieu: 300+")
print(f"Trang thai: {'Da dat muc tieu' if TOTAL_DRUGS >= 300 else 'Chua dat muc tieu'}")
print()

# Phân bổ theo nhóm
groups = {}
for drug, info in DRUG_DATABASE.items():
    group = info.get('group', 'Unknown')
    if ' - ' in group:
        group = group.split(' - ')[0]
    groups[group] = groups.get(group, 0) + 1

print("Phan bo theo nhom:")
for group, count in sorted(groups.items(), key=lambda x: -x[1]):
    print(f"  {group}: {count} thuoc")
