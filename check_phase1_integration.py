"""
Check which calculators have Phase 1 features integrated
Phase 1 features: References, History, Share, Suggestions, Flowcharts
"""
import os
from pathlib import Path

def check_phase1_features(file_path):
    """Check if a calculator file has Phase 1 features"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        has_references = 'render_references' in content or 'get_references' in content
        has_history = 'render_history' in content or 'save_calculation_to_history' in content
        has_share = 'render_share' in content or 'load_shared_result_from_url' in content
        has_suggestions = 'render_suggestions' in content
        has_flowchart = 'render_flowchart' in content or 'flowchart' in content.lower()
        
        # Count how many features are present
        features_count = sum([has_references, has_history, has_share, has_suggestions, has_flowchart])
        
        return {
            'has_references': has_references,
            'has_history': has_history,
            'has_share': has_share,
            'has_suggestions': has_suggestions,
            'has_flowchart': has_flowchart,
            'features_count': features_count,
            'has_all': features_count >= 4  # At least 4 out of 5 (flowchart is optional)
        }
    except Exception as e:
        return None

def main():
    """Check all calculator files"""
    scores_dir = Path("scores")
    
    calculator_files = []
    for file_path in scores_dir.rglob("*.py"):
        if file_path.name == "__init__.py" or file_path.name.endswith(".bak") or "ui_" in file_path.name or "reference" in file_path.name:
            continue
        calculator_files.append(file_path)
    
    print(f"Checking {len(calculator_files)} calculator files...\n")
    
    has_all_features = []
    has_partial_features = []
    has_no_features = []
    
    for file_path in sorted(calculator_files):
        result = check_phase1_features(file_path)
        if result is None:
            continue
        
        rel_path = str(file_path.relative_to(scores_dir))
        
        if result['has_all']:
            has_all_features.append((rel_path, result))
        elif result['features_count'] > 0:
            has_partial_features.append((rel_path, result))
        else:
            has_no_features.append(rel_path)
    
    print("="*80)
    print("SUMMARY")
    print("="*80)
    print(f"Total calculators: {len(calculator_files)}")
    print(f"Has all Phase 1 features (4+): {len(has_all_features)} ({len(has_all_features)/len(calculator_files)*100:.1f}%)")
    print(f"Has partial features (1-3): {len(has_partial_features)} ({len(has_partial_features)/len(calculator_files)*100:.1f}%)")
    print(f"Has no features: {len(has_no_features)} ({len(has_no_features)/len(calculator_files)*100:.1f}%)")
    
    print("\n" + "="*80)
    print("CALCULATORS WITH ALL PHASE 1 FEATURES")
    print("="*80)
    for file_path, result in has_all_features[:30]:
        features = []
        if result['has_references']: features.append("References")
        if result['has_history']: features.append("History")
        if result['has_share']: features.append("Share")
        if result['has_suggestions']: features.append("Suggestions")
        if result['has_flowchart']: features.append("Flowchart")
        print(f"✅ {file_path} - {', '.join(features)}")
    if len(has_all_features) > 30:
        print(f"... and {len(has_all_features) - 30} more")
    
    print("\n" + "="*80)
    print("CALCULATORS WITH PARTIAL FEATURES")
    print("="*80)
    for file_path, result in has_partial_features[:20]:
        features = []
        if result['has_references']: features.append("Ref")
        if result['has_history']: features.append("Hist")
        if result['has_share']: features.append("Share")
        if result['has_suggestions']: features.append("Sugg")
        if result['has_flowchart']: features.append("Flow")
        print(f"🟡 {file_path} - {result['features_count']}/5 features ({', '.join(features)})")
    if len(has_partial_features) > 20:
        print(f"... and {len(has_partial_features) - 20} more")
    
    print("\n" + "="*80)
    print("CALCULATORS WITH NO PHASE 1 FEATURES")
    print("="*80)
    for file_path in has_no_features[:30]:
        print(f"❌ {file_path}")
    if len(has_no_features) > 30:
        print(f"... and {len(has_no_features) - 30} more")
    
    # Save to file
    with open("phase1_integration_report.txt", "w", encoding="utf-8") as f:
        f.write("CALCULATORS WITH ALL PHASE 1 FEATURES\n")
        f.write("="*80 + "\n")
        for file_path, result in has_all_features:
            f.write(f"{file_path}\n")
        
        f.write("\n\nCALCULATORS WITH PARTIAL FEATURES\n")
        f.write("="*80 + "\n")
        for file_path, result in has_partial_features:
            f.write(f"{file_path} - {result['features_count']}/5 features\n")
        
        f.write("\n\nCALCULATORS WITH NO PHASE 1 FEATURES\n")
        f.write("="*80 + "\n")
        for file_path in has_no_features:
            f.write(f"{file_path}\n")
    
    print(f"\nReport saved to: phase1_integration_report.txt")
    print(f"\nRemaining calculators to integrate: {len(has_no_features) + len(has_partial_features)}")

if __name__ == "__main__":
    main()

