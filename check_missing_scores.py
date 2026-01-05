"""
Check which scores are missing based on the documentation list
"""
from pathlib import Path

# List of scores mentioned in documentation as missing
MISSING_SCORES_LIST = {
    # Emergency/Critical Care
    "NEWS2": "emergency/news2.py",
    "MEWS": "emergency/mews.py",
    "PRISM III": "pediatrics/prism3.py",
    "PIM2": "pediatrics/pim2.py",
    "PELOD-2": "pediatrics/pelod2.py",
    "APACHE IV": "emergency/apache4.py",
    
    # Gastroenterology
    "GI Bleed Blatchford Enhanced": "gi/glasgow_blatchford.py",
    "AIMS65": "gi/aims65.py",
    "Rockall Enhanced": "gi/rockall.py",
    "Lactulose Calculator": None,  # Need to check
    
    # Nephrology
    "CKD-EPI Enhanced": "nephrology/egfr.py",  # Need to check if enhanced
    "4-variable MDRD": "nephrology/egfr.py",  # Need to check
    "AKI Staging Enhanced": "nephrology/akin.py",  # Need to check if enhanced
    "Dialysis Adequacy": None,  # Need to check
    
    # Hematology
    "HAS-BLED Enhanced": "cardiology/hasbled.py",  # Need to check if enhanced
    "Warfarin Dosing": None,  # Need to check
    "INR Target Calculator": None,  # Need to check
    "Bleeding Risk": None,  # Need to check
    
    # Neurology
    "ASPECTS Score": "neurology/aspects.py",
    "ABCD2 Score": "neurology/abcd2.py",
    "CT Head Rules": "neurology/canadian_ct_head.py",
    "Canadian Stroke Scale": None,  # Need to check
    "Modified Rankin Scale details": "neurology/mrs.py",  # Need to check if has details
}

def check_scores():
    """Check which scores exist and which are missing"""
    scores_dir = Path("scores")
    
    existing_scores = []
    missing_scores = []
    needs_enhancement = []
    
    for score_name, expected_path in MISSING_SCORES_LIST.items():
        if expected_path is None:
            # Need manual check
            missing_scores.append((score_name, "Need to check manually"))
            continue
        
        file_path = scores_dir / expected_path
        if file_path.exists():
            existing_scores.append((score_name, str(file_path)))
            
            # Check if it says "Enhanced" in the name
            if "Enhanced" in score_name:
                # Read file to check if it's actually enhanced
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if 'enhanced' not in content.lower() and 'Enhanced' not in content:
                            needs_enhancement.append((score_name, str(file_path)))
                except:
                    pass
        else:
            missing_scores.append((score_name, f"Expected: {expected_path}"))
    
    # Check for additional scores that might exist
    print("="*80)
    print("SCORE STATUS CHECK")
    print("="*80)
    
    print(f"\n✅ Existing Scores: {len(existing_scores)}")
    for score_name, path in existing_scores:
        print(f"  ✅ {score_name}: {path}")
    
    if needs_enhancement:
        print(f"\n⚠️ Needs Enhancement: {len(needs_enhancement)}")
        for score_name, path in needs_enhancement:
            print(f"  ⚠️ {score_name}: {path}")
    
    if missing_scores:
        print(f"\n❌ Missing Scores: {len(missing_scores)}")
        for score_name, reason in missing_scores:
            print(f"  ❌ {score_name}: {reason}")
    
    # Check for scores that might exist but not in the list
    print("\n" + "="*80)
    print("ADDITIONAL SCORES TO VERIFY")
    print("="*80)
    
    additional_checks = [
        ("Canadian Stroke Scale", "neurology", "canadian_stroke"),
        ("Warfarin Dosing", "hematology", "warfarin"),
        ("INR Target", "hematology", "inr"),
        ("Dialysis Adequacy", "nephrology", "dialysis"),
        ("Lactulose Calculator", "gi", "lactulose"),
        ("Bleeding Risk", "hematology", "bleeding"),
    ]
    
    for score_name, category, keyword in additional_checks:
        category_dir = scores_dir / category
        if category_dir.exists():
            found = False
            for file_path in category_dir.glob("*.py"):
                if keyword.lower() in file_path.stem.lower():
                    print(f"  ✅ Found: {score_name} - {file_path}")
                    found = True
                    break
            if not found:
                print(f"  ❌ Not found: {score_name}")
    
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print(f"Total scores to check: {len(MISSING_SCORES_LIST)}")
    print(f"✅ Existing: {len(existing_scores)}")
    print(f"⚠️ Needs Enhancement: {len(needs_enhancement)}")
    print(f"❌ Missing: {len(missing_scores)}")
    print(f"📊 Completion: {len(existing_scores)/len(MISSING_SCORES_LIST)*100:.1f}%")

if __name__ == "__main__":
    check_scores()

