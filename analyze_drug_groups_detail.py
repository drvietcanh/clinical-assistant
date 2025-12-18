"""
Analyze drug groups in DRUG_DATABASE and suggest missing high-priority drugs.

Usage:
    python analyze_drug_groups_detail.py
"""

from collections import defaultdict

from drugs.drug_database import DRUG_DATABASE


def normalize_name(name: str) -> str:
    """Simple normalization to compare drug names."""
    return name.strip().lower()


def main() -> None:
    # Build group → list of drug names
    groups: dict[str, list[str]] = defaultdict(list)
    for name, info in DRUG_DATABASE.items():
        group = info.get("group", "Unknown")
        if " - " in group:
            group = group.split(" - ")[0]
        groups[group].append(name)

    print("=== CHI TIẾT NHÓM THUỐC HIỆN TẠI ===\n")
    for group, names in sorted(groups.items(), key=lambda x: -len(x[1])):
        print(f"[{group}] - {len(names)} thuoc")
        for n in sorted(names, key=str.lower):
            print(f"  - {n}")
        print()

    # High-priority suggestions (taken from DRUG_DATABASE_EXPANSION_STATUS.md)
    priority_targets = {
        "Antibiotic": [
            "Azithromycin",
            "Clarithromycin",
            "Amoxicillin-clavulanate",
            "Ampicillin-sulbactam",
            "Cefazolin",
            "Cefuroxime",
            "Ceftriaxone",
            "Ceftazidime",
            "Cefepime",
            "Vancomycin",
            "Linezolid",
            "Clindamycin",
            "Metronidazole",
            "Doxycycline",
            "Minocycline",
            "Gentamicin",
            "Amikacin",
            "Tobramycin",
            "Meropenem",
            "Imipenem-cilastatin",
            "Ertapenem",
        ],
        "Cardiovascular": [
            "Amlodipine",
            "Nifedipine",
            "Diltiazem",
            "Verapamil",
            "Metoprolol",
            "Propranolol",
            "Atenolol",
            "Bisoprolol",
            "Carvedilol",
            "Losartan",
            "Valsartan",
            "Telmisartan",
            "Olmesartan",
            "Candesartan",
            "Irbesartan",
            "Ticagrelor",
            "Prasugrel",
            "Clopidogrel",
            "Aspirin",
            "Atorvastatin",
            "Rosuvastatin",
            "Simvastatin",
            "Pravastatin",
        ],
        "Emergency": [
            "Epinephrine",
            "Norepinephrine",
            "Dopamine",
            "Dobutamine",
            "Amiodarone",
            "Lidocaine",
            "Atropine",
            "Naloxone",
            "Flumazenil",
        ],
        "Neurology": [
            "Phenytoin",
            "Carbamazepine",
            "Valproate",
            "Levetiracetam",
            "Lamotrigine",
            "Topiramate",
            "Gabapentin",
            "Pregabalin",
            "Donepezil",
            "Rivastigmine",
            "Memantine",
            "Sumatriptan",
            "Rizatriptan",
        ],
        "Psychiatry": [
            "Fluoxetine",
            "Sertraline",
            "Citalopram",
            "Escitalopram",
            "Paroxetine",
            "Venlafaxine",
            "Duloxetine",
            "Amitriptyline",
            "Quetiapine",
        ],
        "Gastrointestinal": [
            "Lansoprazole",
            "Esomeprazole",
            "Pantoprazole",
            "Rabeprazole",
            "Ranitidine",
            "Famotidine",
            "Domperidone",
            "Metoclopramide",
            "Loperamide",
            "Bismuth subsalicylate",
        ],
        "Respiratory": [
            "Salmeterol",
            "Formoterol",
            "Ipratropium",
            "Tiotropium",
            "Montelukast",
            "Budesonide inhaled",
            "Fluticasone inhaled",
            "Beclomethasone inhaled",
        ],
        "Oncology": [
            "Oxaliplatin",
            "5-Fluorouracil",
            "Ifosfamide",
            "Doxorubicin",
            "Paclitaxel",
            "Docetaxel",
            "Gemcitabine",
            "Irinotecan",
            "Granisetron",
            "Palonosetron",
        ],
    }

    all_names_normalized = {normalize_name(n): n for n in DRUG_DATABASE.keys()}

    print("=== GOI Y THUOC UU TIEN CAN KIEM TRA/BO SUNG THEM ===\n")
    for group, targets in priority_targets.items():
        missing: list[str] = []
        present: list[str] = []
        for t in targets:
            if normalize_name(t) in all_names_normalized:
                present.append(t)
            else:
                missing.append(t)

        print(f"[{group}]")
        if present:
            print("  Da co trong database:")
            for p in present:
                print(f"    - {p}")
        if missing:
            print("  Chua tim thay (de xuat xem xet bo sung):")
            for m in missing:
                print(f"    - {m}")
        print()


if __name__ == "__main__":
    main()


