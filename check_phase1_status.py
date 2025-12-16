"""
Script để kiểm tra và liệt kê tất cả các calculator đã có Phase 1
"""

import os
from pathlib import Path

def check_phase1_status(file_path):
    """Kiểm tra xem file có Phase 1 không"""
    try:
        content = Path(file_path).read_text(encoding='utf-8')
        
        # Check for Phase 1 imports
        has_phase1_imports = (
            'PHASE 1 IMPORTS' in content or
            'from scores.references_config import get_references' in content
        )
        
        if not has_phase1_imports:
            return False, {}
        
        # Check for Phase 1 features
        features = {
            'load_shared_result': 'load_shared_result_from_url' in content,
            'render_suggestions': 'render_suggestions(' in content,
            'save_calculation': 'save_calculation_to_history(' in content,
            'render_share_section': 'render_share_section(' in content,
            'render_export_section': 'render_export_section(' in content,
            'render_history_ui': 'render_history_ui(' in content,
            'render_references_section': 'render_references_section(' in content,
        }
        
        all_features = all(features.values())
        
        return True, features
    except Exception as e:
        return False, {'error': str(e)}

def main():
    """Main function"""
    print("="*70)
    print("🔍 KIỂM TRA TRẠNG THÁI PHASE 1 CỦA TẤT CẢ CALCULATORS")
    print("="*70)
    
    # Find all calculator files
    calculator_files = []
    scores_dir = Path('scores')
    
    for root, dirs, files in os.walk(scores_dir):
        for file in files:
            if file.endswith('.py') and '__init__' not in file:
                file_path = Path(root) / file
                calculator_files.append(file_path)
    
    print(f"\n📊 Tổng số calculator files: {len(calculator_files)}")
    print("\n" + "="*70)
    
    # Check each calculator
    phase1_calculators = []
    no_phase1_calculators = []
    
    for file_path in sorted(calculator_files):
        has_phase1, features = check_phase1_status(file_path)
        
        # Get category and name
        parts = file_path.parts
        if len(parts) >= 3:
            category = parts[1]  # scores/category/file.py
            name = parts[2].replace('.py', '')
        else:
            category = "unknown"
            name = file_path.stem
        
        if has_phase1:
            phase1_calculators.append({
                'path': str(file_path),
                'category': category,
                'name': name,
                'features': features
            })
        else:
            no_phase1_calculators.append({
                'path': str(file_path),
                'category': category,
                'name': name
            })
    
    # Print results
    print(f"\n✅ Calculators ĐÃ CÓ Phase 1: {len(phase1_calculators)}/{len(calculator_files)}")
    print(f"❌ Calculators CHƯA CÓ Phase 1: {len(no_phase1_calculators)}/{len(calculator_files)}")
    print(f"📈 Tỷ lệ: {len(phase1_calculators)/len(calculator_files)*100:.1f}%")
    
    # Group by category
    print("\n" + "="*70)
    print("📋 PHÂN LOẠI THEO CATEGORY")
    print("="*70)
    
    categories = {}
    for calc in phase1_calculators:
        cat = calc['category']
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(calc['name'])
    
    for cat in sorted(categories.keys()):
        calcs = categories[cat]
        print(f"\n✅ {cat.upper()}: {len(calcs)} calculators")
        for calc_name in sorted(calcs):
            print(f"   - {calc_name}")
    
    # Show calculators without Phase 1 (first 20)
    if no_phase1_calculators:
        print("\n" + "="*70)
        print(f"❌ CALCULATORS CHƯA CÓ PHASE 1 (hiển thị 20 đầu tiên)")
        print("="*70)
        
        no_phase1_by_category = {}
        for calc in no_phase1_calculators:
            cat = calc['category']
            if cat not in no_phase1_by_category:
                no_phase1_by_category[cat] = []
            no_phase1_by_category[cat].append(calc['name'])
        
        count = 0
        for cat in sorted(no_phase1_by_category.keys()):
            if count >= 20:
                break
            calcs = no_phase1_by_category[cat]
            print(f"\n❌ {cat.upper()}: {len(calcs)} calculators")
            for calc_name in sorted(calcs)[:5]:  # Show first 5 per category
                if count >= 20:
                    break
                print(f"   - {calc_name}")
                count += 1
        
        if len(no_phase1_calculators) > 20:
            print(f"\n   ... và {len(no_phase1_calculators) - 20} calculators khác")
    
    # Summary
    print("\n" + "="*70)
    print("📊 TỔNG KẾT")
    print("="*70)
    print(f"✅ Đã có Phase 1: {len(phase1_calculators)} calculators")
    print(f"❌ Chưa có Phase 1: {len(no_phase1_calculators)} calculators")
    print(f"📈 Tỷ lệ hoàn thành: {len(phase1_calculators)/len(calculator_files)*100:.1f}%")
    print("="*70)
    
    return phase1_calculators, no_phase1_calculators

if __name__ == "__main__":
    phase1_calcs, no_phase1_calcs = main()

