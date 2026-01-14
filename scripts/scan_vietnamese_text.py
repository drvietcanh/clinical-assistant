"""
Script to scan and categorize all Vietnamese text in the codebase
Phân loại và thu thập tất cả chuỗi tiếng Việt trong codebase
"""

import re
import os
from pathlib import Path
from typing import Dict, List, Tuple
from collections import defaultdict
import json

# Pattern to find Vietnamese text in strings
VIETNAMESE_PATTERN = re.compile(
    r'["\']([^"\']*[àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđĐ][^"\']*)["\']',
    re.IGNORECASE
)

# Pattern to find Vietnamese in markdown/html
VIETNAMESE_MARKDOWN_PATTERN = re.compile(
    r'[àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđĐ]+',
    re.IGNORECASE
)

# Medical abbreviations that should be checked
MEDICAL_ABBREVIATIONS = {
    'ICU', 'TDM', 'eGFR', 'CrCl', 'CAP', 'HAP', 'VAP', 'UTI', 'SSTI', 
    'CNS', 'IAI', 'BACTEREMIA', 'SEPSIS', 'OSTEOMYELITIS', 'ENDOCARDITIS',
    'CHADS2', 'VASc', 'HAS-BLED', 'SOFA', 'APACHE', 'NEWS2', 'QSOFA',
    'SIRS', 'GCS', 'NIHSS', 'MRS', 'NYHA', 'TIMI', 'GRACE', 'WELLS',
    'PERC', 'BMI', 'BSA', 'FDA', 'IV', 'PO', 'IM', 'SC', 'TID', 'BID',
    'QD', 'QID', 'PRN', 'STAT', 'CKD', 'ESRD', 'AKI', 'CKD-EPI', 'MDRD',
    'FENa', 'COPD', 'ARDS', 'DVT', 'PE', 'ACS', 'STEMI', 'NSTEMI',
    'AFib', 'VT', 'VF', 'SVT', 'AVB', 'CHF', 'HF', 'MI', 'CAD', 'PAD',
    'TIA', 'CVA', 'ICH', 'SAH', 'SDH', 'EDH', 'ICP', 'CPP', 'MAP',
    'CVP', 'PAWP', 'SVR', 'PVR', 'CO', 'CI', 'SV', 'EF', 'LVEF', 'RVEF',
    'BNP', 'NT-proBNP', 'Troponin', 'CK-MB', 'LDH', 'AST', 'ALT', 'ALP',
    'Bilirubin', 'PT', 'INR', 'PTT', 'aPTT', 'D-dimer', 'Fibrinogen',
    'Platelets', 'WBC', 'RBC', 'Hgb', 'Hct', 'MCV', 'MCH', 'MCHC',
    'RDW', 'ESR', 'CRP', 'PCT', 'Procalcitonin', 'Lactate', 'ABG',
    'pH', 'pCO2', 'pO2', 'HCO3', 'BE', 'SaO2', 'SpO2', 'FiO2', 'PEEP',
    'RR', 'TV', 'MV', 'I:E', 'PIP', 'Plateau', 'Compliance', 'Resistance'
}

# Medical specialties in Vietnamese
MEDICAL_SPECIALTIES = {
    'Tim mạch', 'Thần kinh', 'Hồi sức', 'Thận học', 'Huyết học',
    'Nội tiết', 'Tiêu hóa', 'Hô hấp', 'Da liễu', 'Nhi khoa',
    'Sản phụ khoa', 'Cấp cứu', 'Ung bướu', 'Tâm thần', 'Chuyển hóa'
}

# Drug class terms
DRUG_CLASS_TERMS = {
    'Beta-lactam', 'Fluoroquinolone', 'Macrolide', 'Glycopeptide',
    'Aminoglycoside', 'Lincosamide', 'Tetracycline', 'Sulfonamide',
    'Penicillin', 'Cephalosporin', 'Carbapenem', 'Monobactam'
}

# Procedure terms
PROCEDURE_TERMS = {
    'Thở máy', 'Lọc máu', 'Chọc dò', 'Nội soi', 'Siêu âm',
    'X-quang', 'CT scan', 'MRI', 'ECG', 'EKG', 'EEG', 'EMG'
}

def scan_file(file_path: Path) -> List[Tuple[int, str, str]]:
    """
    Scan a single file for Vietnamese text
    
    Returns:
        List of tuples: (line_number, matched_text, context)
    """
    matches = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line_num, line in enumerate(lines, 1):
                # Find Vietnamese in string literals
                for match in VIETNAMESE_PATTERN.finditer(line):
                    matches.append((line_num, match.group(1), line.strip()[:100]))
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return matches

def categorize_text(text: str) -> Dict[str, bool]:
    """
    Categorize Vietnamese text into different types
    
    Returns:
        Dict with category flags
    """
    categories = {
        'is_medical_term': False,
        'is_abbreviation': False,
        'is_ui_text': False,
        'is_drug_name': False,
        'is_procedure': False,
        'needs_annotation': False
    }
    
    text_upper = text.upper()
    
    # Check for medical abbreviations
    for abbrev in MEDICAL_ABBREVIATIONS:
        if abbrev in text_upper:
            categories['is_abbreviation'] = True
            categories['is_medical_term'] = True
            categories['needs_annotation'] = True
    
    # Check for medical specialties
    for specialty in MEDICAL_SPECIALTIES:
        if specialty in text:
            categories['is_medical_term'] = True
    
    # Check for drug class terms
    for drug_class in DRUG_CLASS_TERMS:
        if drug_class in text:
            categories['is_drug_name'] = True
            categories['is_medical_term'] = True
    
    # Check for procedure terms
    for procedure in PROCEDURE_TERMS:
        if procedure in text:
            categories['is_procedure'] = True
            categories['is_medical_term'] = True
    
    # UI-related keywords
    ui_keywords = ['nút', 'button', 'menu', 'trang', 'màn hình', 'thông báo', 
                   'cảnh báo', 'lưu', 'hủy', 'gửi', 'tìm kiếm', 'lọc']
    if any(keyword in text.lower() for keyword in ui_keywords):
        categories['is_ui_text'] = True
    
    return categories

def scan_codebase(root_dir: Path = Path('.')) -> Dict:
    """
    Scan entire codebase for Vietnamese text
    
    Returns:
        Dictionary with categorized results
    """
    results = {
        'total_files_scanned': 0,
        'total_matches': 0,
        'by_file': {},
        'by_category': defaultdict(list),
        'medical_terms': [],
        'abbreviations': [],
        'ui_texts': [],
        'needs_review': []
    }
    
    # Directories to scan
    scan_dirs = ['components', 'pages', 'drugs', 'protocols', 'config', 
                 'utils', 'diagnosis', 'antibiotics', 'scores']
    
    # File extensions to scan
    extensions = ['.py']
    
    for scan_dir in scan_dirs:
        dir_path = root_dir / scan_dir
        if not dir_path.exists():
            continue
            
        for file_path in dir_path.rglob('*.py'):
            if '__pycache__' in str(file_path) or '.pyc' in str(file_path):
                continue
                
            results['total_files_scanned'] += 1
            matches = scan_file(file_path)
            
            if matches:
                relative_path = str(file_path.relative_to(root_dir))
                results['by_file'][relative_path] = {
                    'matches': len(matches),
                    'details': []
                }
                
                for line_num, text, context in matches:
                    results['total_matches'] += 1
                    categories = categorize_text(text)
                    
                    match_info = {
                        'line': line_num,
                        'text': text,
                        'context': context,
                        'categories': categories
                    }
                    
                    results['by_file'][relative_path]['details'].append(match_info)
                    
                    # Add to category lists
                    if categories['is_medical_term']:
                        results['medical_terms'].append({
                            'file': relative_path,
                            'line': line_num,
                            'text': text
                        })
                    
                    if categories['is_abbreviation']:
                        results['abbreviations'].append({
                            'file': relative_path,
                            'line': line_num,
                            'text': text
                        })
                    
                    if categories['is_ui_text']:
                        results['ui_texts'].append({
                            'file': relative_path,
                            'line': line_num,
                            'text': text
                        })
                    
                    if categories['needs_annotation']:
                        results['needs_review'].append({
                            'file': relative_path,
                            'line': line_num,
                            'text': text,
                            'reason': 'Contains medical abbreviation'
                        })

    return results

def main():
    """Main execution"""
    print("Scanning codebase for Vietnamese text...")
    print("=" * 60)
    
    root_dir = Path(__file__).parent.parent
    results = scan_codebase(root_dir)
    
    # Print summary
    print(f"\nSummary:")
    print(f"  Files scanned: {results['total_files_scanned']}")
    print(f"  Total Vietnamese strings found: {results['total_matches']}")
    print(f"  Files with Vietnamese text: {len(results['by_file'])}")
    print(f"  Medical terms found: {len(results['medical_terms'])}")
    print(f"  Abbreviations found: {len(results['abbreviations'])}")
    print(f"  UI texts found: {len(results['ui_texts'])}")
    print(f"  Items needing review: {len(results['needs_review'])}")
    
    # Save results to JSON
    output_file = root_dir / 'docs' / 'vietnamese_text_scan_results.json'
    output_file.parent.mkdir(exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f"\nResults saved to: {output_file}")
    
    # Print top files with most Vietnamese text
    print("\nTop 10 files with most Vietnamese text:")
    sorted_files = sorted(
        results['by_file'].items(),
        key=lambda x: x[1]['matches'],
        reverse=True
    )[:10]
    
    for file_path, data in sorted_files:
        print(f"  {file_path}: {data['matches']} matches")

if __name__ == '__main__':
    main()
