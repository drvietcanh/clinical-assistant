#!/usr/bin/env python3
"""
Test script for Scores Optimization Phases
Tests Phase 1, Phase 2, and all integrations
"""

import sys
sys.path.insert(0, '.')

def test_phase1():
    """Test Phase 1: Research & Foundation"""
    print("\n" + "="*60)
    print("PHASE 1: Research & Foundation")
    print("="*60)
    
    errors = []
    
    # 1.1 UI/UX Research
    try:
        import os
        if os.path.exists('docs/SCORES_UI_UX_RESEARCH.md'):
            print("✅ UI/UX Research documentation exists")
        else:
            errors.append("❌ UI/UX Research documentation missing")
    except Exception as e:
        errors.append(f"❌ UI/UX Research check failed: {e}")
    
    # 1.2 Information Architecture
    try:
        from scores.specialty_groups import get_all_groups, get_specialties_in_group
        groups = get_all_groups()
        print(f"✅ Specialty groups: {len(groups)} groups")
        
        expected_groups = ['critical_care_emergency', 'organ_systems', 'special_populations', 'specialized_fields']
        for gid in expected_groups:
            if gid in groups:
                specialties = get_specialties_in_group(gid)
                print(f"  ✅ {gid}: {len(specialties)} specialties")
            else:
                errors.append(f"❌ Missing group: {gid}")
    except Exception as e:
        errors.append(f"❌ Information Architecture test failed: {e}")
    
    # 1.3 UI Components
    try:
        from scores.ui_scores_view import (
            is_daily_use,
            render_calculator_card,
            render_specialty_group,
            render_quick_access_section,
            render_filters_sidebar,
            filter_calculators
        )
        print("✅ UI Components: All functions import OK")
        
        # Test is_daily_use
        test_info = {'desc': 'Test calculator DÙNG HÀNG NGÀY'}
        result = is_daily_use(test_info)
        if result:
            print("  ✅ is_daily_use function works")
        else:
            errors.append("❌ is_daily_use function failed")
    except Exception as e:
        errors.append(f"❌ UI Components test failed: {e}")
    
    # 1.4 Geriatrics Module
    try:
        from scores import geriatrics
        from scores.geriatrics import (
            render_cfs,
            render_morse_fall,
            render_mmse,
            render_moca,
            render_beers,
            render_stopp_start
        )
        print("✅ Geriatrics Module: All functions import OK")
        
        # Check config
        from scores.config import SCORES_BY_SPECIALTY
        geriatrics_scores = SCORES_BY_SPECIALTY.get('👴 Lão khoa (Geriatrics)', {})
        if len(geriatrics_scores) == 6:
            print(f"  ✅ Geriatrics config: {len(geriatrics_scores)} calculators")
            print(f"  ✅ Calculator IDs: {list(geriatrics_scores.keys())}")
        else:
            errors.append(f"❌ Geriatrics config: Expected 6, got {len(geriatrics_scores)}")
    except Exception as e:
        errors.append(f"❌ Geriatrics Module test failed: {e}")
    
    return errors

def test_phase2():
    """Test Phase 2: Integration & Optimization"""
    print("\n" + "="*60)
    print("PHASE 2: Integration & Optimization")
    print("="*60)
    
    errors = []
    
    # 2.1 Modern View Integration
    try:
        # Check main page has modern view code
        with open('pages/01_📊_Scores.py', 'r', encoding='utf-8') as f:
            content = f.read()
            if 'Modern View' in content and 'modern_view' in content:
                print("✅ Modern View integration code exists")
            else:
                errors.append("❌ Modern View integration missing")
    except Exception as e:
        errors.append(f"❌ Modern View check failed: {e}")
    
    # 2.2 Recent Tracking
    try:
        from components.scores_recent import (
            add_to_recent,
            get_recent_calculators,
            clear_recent,
            render_recent_list
        )
        print("✅ Recent Tracking: All functions import OK")
        
        # Test functionality
        add_to_recent('Test Specialty', 'TEST_ID', 'Test Calculator')
        recent = get_recent_calculators(5)
        if len(recent) > 0 and recent[0]['name'] == 'Test Calculator':
            print("  ✅ Recent tracking functionality works")
        else:
            errors.append("❌ Recent tracking functionality failed")
    except Exception as e:
        errors.append(f"❌ Recent Tracking test failed: {e}")
    
    # 2.3 Mobile Optimization
    try:
        from scores.ui_scores_view import render_calculator_card
        # Check if mobile CSS is in the function
        import inspect
        source = inspect.getsource(render_calculator_card)
        if '@media' in source or 'mobile' in source.lower():
            print("✅ Mobile optimization CSS exists")
        else:
            errors.append("❌ Mobile optimization CSS missing")
    except Exception as e:
        errors.append(f"❌ Mobile Optimization test failed: {e}")
    
    # 2.4 Calculator Routing
    try:
        with open('pages/01_📊_Scores.py', 'r', encoding='utf-8') as f:
            content = f.read()
            if 'GERIATRICS_AVAILABLE' in content and 'geriatrics.render_geriatrics_calculator' in content:
                print("✅ Calculator routing includes Geriatrics")
            else:
                errors.append("❌ Geriatrics routing missing")
            
            # Check modern view routing
            if 'modern_view_calculator_selected' in content:
                print("✅ Modern View routing exists")
            else:
                errors.append("❌ Modern View routing missing")
    except Exception as e:
        errors.append(f"❌ Calculator Routing test failed: {e}")
    
    return errors

def test_integration():
    """Test Integration Points"""
    print("\n" + "="*60)
    print("INTEGRATION TESTING")
    print("="*60)
    
    errors = []
    
    # Config vs Groups Consistency
    try:
        from scores.config import SCORES_BY_SPECIALTY
        from scores.specialty_groups import get_all_groups, get_specialties_in_group
        
        groups = get_all_groups()
        all_specialties_in_groups = []
        for gid in groups.keys():
            specialties = get_specialties_in_group(gid)
            all_specialties_in_groups.extend(specialties)
        
        config_specialties = set(SCORES_BY_SPECIALTY.keys())
        group_specialties = set(all_specialties_in_groups)
        
        missing = config_specialties - group_specialties
        extra = group_specialties - config_specialties
        
        print(f"✅ Config specialties: {len(config_specialties)}")
        print(f"✅ Group specialties: {len(group_specialties)}")
        
        if missing:
            errors.append(f"❌ Missing in groups: {list(missing)[:3]}")
            print(f"⚠️ Missing in groups: {len(missing)}")
        else:
            print("✅ No missing specialties in groups")
        
        if extra:
            errors.append(f"❌ Extra in groups: {list(extra)[:3]}")
            print(f"⚠️ Extra in groups: {len(extra)}")
        else:
            print("✅ No extra specialties in groups")
    except Exception as e:
        errors.append(f"❌ Config vs Groups test failed: {e}")
    
    # Module Imports
    try:
        from scores import geriatrics
        from scores.specialty_groups import get_all_groups
        from scores.ui_scores_view import render_calculator_card
        from components.scores_recent import add_to_recent
        print("✅ All module imports successful")
    except Exception as e:
        errors.append(f"❌ Module imports failed: {e}")
    
    # Function Signatures
    try:
        import inspect
        from scores.ui_scores_view import render_calculator_card, render_specialty_group
        
        sig1 = inspect.signature(render_calculator_card)
        sig2 = inspect.signature(render_specialty_group)
        
        print(f"✅ render_calculator_card signature: {sig1}")
        print(f"✅ render_specialty_group signature: {sig2}")
    except Exception as e:
        errors.append(f"❌ Function signatures test failed: {e}")
    
    return errors

def main():
    """Run all tests"""
    print("\n" + "="*60)
    print("SCORES OPTIMIZATION - PHASE TESTING")
    print("="*60)
    
    all_errors = []
    
    # Phase 1
    phase1_errors = test_phase1()
    all_errors.extend(phase1_errors)
    
    # Phase 2
    phase2_errors = test_phase2()
    all_errors.extend(phase2_errors)
    
    # Integration
    integration_errors = test_integration()
    all_errors.extend(integration_errors)
    
    # Summary
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    
    if all_errors:
        print(f"\n❌ Found {len(all_errors)} errors:")
        for error in all_errors:
            print(f"  {error}")
        return 1
    else:
        print("\n✅ ALL TESTS PASSED!")
        print("\nPhase 1: ✅ PASS")
        print("Phase 2: ✅ PASS")
        print("Integration: ✅ PASS")
        return 0

if __name__ == '__main__':
    sys.exit(main())
