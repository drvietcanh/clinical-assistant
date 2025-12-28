#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to list all drugs missing both risk_flags and guideline_tags
and organize them into sessions for batch processing
"""

from drugs.drug_database import DRUG_DATABASE
from collections import defaultdict

def get_drug_module(drug_name, drug_data):
    """Try to determine which module a drug belongs to"""
    group = drug_data.get('group', 'Unknown')
    
    # Extract module from group
    if 'Antibiotic' in group or 'Antimicrobial' in group:
        return 'Antimicrobial'
    elif 'Cardiovascular' in group or 'CV' in group:
        return 'Cardiovascular'
    elif 'Diabetes' in group:
        return 'Diabetes'
    elif 'Analgesic' in group or 'Pain' in group:
        return 'Analgesics'
    elif 'Neurological' in group or 'Neurology' in group:
        return 'Neurological'
    elif 'Gastrointestinal' in group or 'GI' in group:
        return 'Gastrointestinal'
    elif 'Respiratory' in group:
        return 'Respiratory'
    elif 'Psychiatry' in group or 'Psychiatric' in group:
        return 'Psychiatry'
    elif 'Oncology' in group or 'Cancer' in group:
        return 'Oncology'
    elif 'Endocrinology' in group or 'Hormone' in group:
        return 'Endocrinology'
    elif 'Emergency' in group:
        return 'Emergency'
    elif 'Supportive' in group:
        return 'Supportive'
    else:
        return 'Other'

def list_missing_drugs():
    """List all drugs missing both risk_flags and guideline_tags"""
    
    missing_both = []
    drugs_by_module = defaultdict(list)
    
    for drug_name, drug_data in DRUG_DATABASE.items():
        has_risk_flags = 'risk_flags' in drug_data and drug_data.get('risk_flags') is not None
        has_guideline_tags = 'guideline_tags' in drug_data and drug_data.get('guideline_tags') is not None
        
        if not has_risk_flags and not has_guideline_tags:
            missing_both.append(drug_name)
            module = get_drug_module(drug_name, drug_data)
            drugs_by_module[module].append(drug_name)
    
    # Sort drugs within each module
    for module in drugs_by_module:
        drugs_by_module[module].sort()
    
    # Sort modules by number of drugs (descending)
    sorted_modules = sorted(drugs_by_module.items(), key=lambda x: len(x[1]), reverse=True)
    
    print("=" * 80)
    print("DANH SÁCH THUỐC THIẾU CẢ HAI FIELD: risk_flags + guideline_tags")
    print("=" * 80)
    print(f"\nTổng số: {len(missing_both)} thuốc\n")
    
    # Print by module
    print("PHÂN LOẠI THEO MODULE:")
    print("-" * 80)
    total = 0
    for module, drugs in sorted_modules:
        print(f"\n{module}: {len(drugs)} thuốc")
        print(f"  {', '.join(drugs[:10])}" + ("..." if len(drugs) > 10 else ""))
        total += len(drugs)
    
    print(f"\n{'='*80}")
    print(f"TỔNG: {total} thuốc")
    print(f"{'='*80}\n")
    
    # Divide into sessions (20-30 drugs per session)
    SESSION_SIZE = 25
    sessions = []
    current_session = []
    current_count = 0
    
    # Group by module first, then split large modules
    for module, drugs in sorted_modules:
        if len(drugs) <= SESSION_SIZE:
            # Small module - can fit in one session
            if current_count + len(drugs) <= SESSION_SIZE:
                current_session.append((module, drugs))
                current_count += len(drugs)
            else:
                # Start new session
                if current_session:
                    sessions.append(current_session)
                current_session = [(module, drugs)]
                current_count = len(drugs)
        else:
            # Large module - split into multiple sessions
            if current_session:
                sessions.append(current_session)
                current_session = []
                current_count = 0
            
            # Split large module
            for i in range(0, len(drugs), SESSION_SIZE):
                chunk = drugs[i:i+SESSION_SIZE]
                sessions.append([(module, chunk)])
    
    # Add last session if exists
    if current_session:
        sessions.append(current_session)
    
    # Print sessions
    print("\n" + "=" * 80)
    print("CHIA THÀNH CÁC PHIÊN XỬ LÝ (25 thuốc/phiên)")
    print("=" * 80)
    
    for i, session in enumerate(sessions, 1):
        session_drugs = []
        for module, drugs in session:
            session_drugs.extend(drugs)
        
        print(f"\nPHIÊN {i}: {len(session_drugs)} thuốc")
        print("-" * 80)
        for module, drugs in session:
            print(f"  [{module}] {len(drugs)} thuốc: {', '.join(drugs)}")
    
    print(f"\n{'='*80}")
    print(f"TỔNG CỘNG: {len(sessions)} phiên")
    print(f"{'='*80}\n")
    
    # Export to file
    with open('missing_risk_guideline_list.txt', 'w', encoding='utf-8') as f:
        f.write("DANH SÁCH THUỐC THIẾU CẢ HAI FIELD: risk_flags + guideline_tags\n")
        f.write("=" * 80 + "\n")
        f.write(f"Tổng số: {len(missing_both)} thuốc\n\n")
        
        f.write("PHÂN LOẠI THEO MODULE:\n")
        f.write("-" * 80 + "\n")
        for module, drugs in sorted_modules:
            f.write(f"\n{module}: {len(drugs)} thuốc\n")
            for drug in drugs:
                f.write(f"  - {drug}\n")
        
        f.write(f"\n{'='*80}\n")
        f.write("CHIA THÀNH CÁC PHIÊN XỬ LÝ:\n")
        f.write("=" * 80 + "\n")
        for i, session in enumerate(sessions, 1):
            session_drugs = []
            for module, drugs in session:
                session_drugs.extend(drugs)
            f.write(f"\nPHIÊN {i}: {len(session_drugs)} thuốc\n")
            f.write("-" * 80 + "\n")
            for module, drugs in session:
                f.write(f"  [{module}] {len(drugs)} thuốc:\n")
                for drug in drugs:
                    f.write(f"    - {drug}\n")
    
    print("Đã xuất danh sách vào file: missing_risk_guideline_list.txt")
    
    return missing_both, drugs_by_module, sessions

if __name__ == '__main__':
    try:
        missing_both, drugs_by_module, sessions = list_missing_drugs()
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

