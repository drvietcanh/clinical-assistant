"""
Script to check Vietnamese localization issues
Kiểm tra và báo cáo các vấn đề về việt hóa
"""

import re
import os
from pathlib import Path
from typing import Dict, List, Set, Tuple
from collections import defaultdict
import json

# Import translation dictionaries
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from utils.i18n import TRANSLATIONS
from utils.term_annotations import MEDICAL_TERM_ANNOTATIONS, check_term_needs_annotation

# Patterns
VIETNAMESE_PATTERN = re.compile(
    r'["\']([^"\']*[àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđĐ][^"\']*)["\']',
    re.IGNORECASE
)

# Medical abbreviations that should have annotations
MEDICAL_ABBREVIATIONS = {
    'CAP', 'HAP', 'VAP', 'UTI', 'SSTI', 'CNS', 'IAI', 'SEPSIS', 'BACTEREMIA',
    'OSTEOMYELITIS', 'ENDOCARDITIS', 'CHADS2', 'VASc', 'HAS-BLED', 'SOFA',
    'APACHE', 'NEWS2', 'QSOFA', 'SIRS', 'GCS', 'NIHSS', 'MRS', 'NYHA',
    'TIMI', 'GRACE', 'WELLS', 'PERC', 'CKD', 'ESRD', 'AKI', 'CKD-EPI',
    'MDRD', 'FENa', 'COPD', 'ARDS', 'DVT', 'PE', 'ACS', 'STEMI', 'NSTEMI',
    'AFib', 'VT', 'VF', 'SVT', 'AVB', 'CHF', 'HF', 'MI', 'CAD', 'PAD',
    'TIA', 'CVA', 'ICH', 'SAH', 'SDH', 'EDH', 'ICP', 'CPP', 'MAP',
    'CVP', 'PAWP', 'SVR', 'PVR', 'CO', 'CI', 'SV', 'EF', 'LVEF', 'RVEF',
    'BNP', 'NT-proBNP', 'Troponin', 'CK-MB', 'LDH', 'AST', 'ALT', 'ALP',
    'Bilirubin', 'PT', 'INR', 'PTT', 'aPTT', 'D-dimer', 'Fibrinogen',
    'CRP', 'ESR', 'PCT', 'Procalcitonin', 'Lactate', 'ABG', 'pCO2', 'pO2',
    'HCO3', 'BE', 'SaO2', 'SpO2', 'FiO2', 'PEEP', 'RR', 'TV', 'MV', 'I:E',
    'PIP', 'Plateau', 'Compliance', 'Resistance', 'CRRT', 'CT scan', 'MRI',
    'ECG', 'EKG', 'EEG', 'EMG', 'ITP', 'DIC', 'TTP', 'HUS'
}

# Terms that should use i18n keys instead of hardcoded
COMMON_UI_TERMS = {
    'Trang chủ': 'home',
    'Tìm kiếm': 'search',
    'Cài đặt': 'settings',
    'Giới thiệu': 'about',
    'Đóng': 'close',
    'Lưu': 'save',
    'Hủy': 'cancel',
    'Gửi': 'submit',
    'Quay lại': 'back',
    'Tiếp theo': 'next',
    'Trước': 'previous',
    'Xóa': 'delete',
    'Chỉnh sửa': 'edit',
    'Xem': 'view',
    'Tải xuống': 'download',
    'Xuất': 'export',
    'Thuốc': 'drugs',
    'Liều dùng': 'dosage',
    'Chỉ định': 'indication',
    'Chống chỉ định': 'contraindication',
    'Tác dụng phụ': 'side_effect',
    'Tương tác': 'interaction',
    'Phác đồ': 'protocols',
    'Hướng dẫn': 'guideline',
    'Khuyến cáo': 'recommendation',
    'Bằng chứng': 'evidence',
    'Bệnh nhân': 'patient',
    'Chẩn đoán': 'diagnosis',
    'Điều trị': 'treatment',
    'Theo dõi': 'monitoring',
    'Cảnh báo': 'warning',
}

# Inconsistent term mappings (found issues)
INCONSISTENT_TERMS = {
    'ICU': ['ICU', 'Đơn vị hồi sức tích cực', 'Hồi sức'],
    'TDM': ['TDM', 'Theo dõi nồng độ thuốc'],
    'eGFR': ['eGFR', 'Độ lọc cầu thận ước tính'],
    'CrCl': ['CrCl', 'Độ thanh thải Creatinine'],
}

class LocalizationChecker:
    """Check Vietnamese localization issues"""
    
    def __init__(self, root_dir: Path = None):
        self.root_dir = root_dir or Path(__file__).parent.parent
        self.issues = {
            'hardcoded_strings': [],
            'missing_annotations': [],
            'inconsistent_terms': [],
            'not_using_i18n': [],
            'medical_terms_without_glossary': [],
        }
        self.stats = {
            'files_checked': 0,
            'total_vietnamese_strings': 0,
            'hardcoded_count': 0,
            'missing_annotation_count': 0,
            'inconsistent_count': 0,
            'not_using_i18n_count': 0,
        }
    
    def check_file(self, file_path: Path) -> None:
        """Check a single file for localization issues"""
        if '__pycache__' in str(file_path):
            return
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.split('\n')
        except Exception as e:
            return
        
        self.stats['files_checked'] += 1
        
        # Skip if it's a translation file itself
        if 'vietnamese_translations.py' in str(file_path) or 'vietnamese_terms.py' in str(file_path):
            return
        
        # Check for Vietnamese strings
        for line_num, line in enumerate(lines, 1):
            # Find Vietnamese text in string literals
            for match in VIETNAMESE_PATTERN.finditer(line):
                vietnamese_text = match.group(1)
                self.stats['total_vietnamese_strings'] += 1
                
                relative_path = str(file_path.relative_to(self.root_dir))
                
                # Check 1: Hardcoded strings (should use i18n)
                if self._should_use_i18n(vietnamese_text):
                    self.stats['not_using_i18n_count'] += 1
                    self.issues['not_using_i18n'].append({
                        'file': relative_path,
                        'line': line_num,
                        'text': vietnamese_text,
                        'suggested_key': self._get_i18n_key(vietnamese_text),
                        'context': line.strip()[:100]
                    })
                
                # Check 2: Medical abbreviations without annotation
                abbrev_found = self._find_medical_abbreviation(vietnamese_text)
                if abbrev_found and check_term_needs_annotation(abbrev_found):
                    self.stats['missing_annotation_count'] += 1
                    self.issues['missing_annotations'].append({
                        'file': relative_path,
                        'line': line_num,
                        'text': vietnamese_text,
                        'abbreviation': abbrev_found,
                        'context': line.strip()[:100]
                    })
                
                # Check 3: Inconsistent medical terms
                inconsistent = self._check_inconsistent_term(vietnamese_text)
                if inconsistent:
                    self.stats['inconsistent_count'] += 1
                    self.issues['inconsistent_terms'].append({
                        'file': relative_path,
                        'line': line_num,
                        'text': vietnamese_text,
                        'term': inconsistent,
                        'context': line.strip()[:100]
                    })
                
                # Check 4: Medical terms not in glossary
                medical_term = self._find_medical_term(vietnamese_text)
                if medical_term and medical_term not in MEDICAL_TERM_ANNOTATIONS:
                    self.issues['medical_terms_without_glossary'].append({
                        'file': relative_path,
                        'line': line_num,
                        'text': vietnamese_text,
                        'term': medical_term,
                        'context': line.strip()[:100]
                    })
    
    def _should_use_i18n(self, text: str) -> bool:
        """Check if text should use i18n key instead of hardcoded"""
        text_clean = text.strip()
        return text_clean in COMMON_UI_TERMS
    
    def _get_i18n_key(self, text: str) -> str:
        """Get suggested i18n key for text"""
        return COMMON_UI_TERMS.get(text.strip(), '')
    
    def _find_medical_abbreviation(self, text: str) -> str:
        """Find medical abbreviation in text"""
        text_upper = text.upper()
        for abbrev in MEDICAL_ABBREVIATIONS:
            if abbrev in text_upper:
                return abbrev
        return None
    
    def _check_inconsistent_term(self, text: str) -> str:
        """Check for inconsistent term usage"""
        text_upper = text.upper()
        for term, variants in INCONSISTENT_TERMS.items():
            if term in text_upper:
                # Check if using non-standard variant
                for variant in variants[1:]:  # Skip first (standard)
                    if variant.lower() in text.lower():
                        return term
        return None
    
    def _find_medical_term(self, text: str) -> str:
        """Find medical term that might need glossary entry"""
        # Simple heuristic: check for common medical patterns
        medical_keywords = [
            'viêm', 'nhiễm', 'suy', 'hội chứng', 'bệnh', 'thang điểm',
            'độ lọc', 'thanh thải', 'nồng độ', 'liều', 'kháng sinh'
        ]
        for keyword in medical_keywords:
            if keyword in text.lower():
                # Extract potential term (first few words)
                words = text.split()[:3]
                return ' '.join(words)
        return None
    
    def scan_codebase(self, directories: List[str] = None) -> None:
        """Scan codebase for issues"""
        if directories is None:
            directories = ['components', 'pages', 'drugs', 'protocols', 'config', 'utils']
        
        for directory in directories:
            dir_path = self.root_dir / directory
            if not dir_path.exists():
                continue
            
            for file_path in dir_path.rglob('*.py'):
                self.check_file(file_path)
    
    def generate_report(self) -> Dict:
        """Generate report of all issues"""
        return {
            'stats': self.stats,
            'issues': self.issues,
            'summary': {
                'total_files_checked': self.stats['files_checked'],
                'total_vietnamese_strings': self.stats['total_vietnamese_strings'],
                'hardcoded_strings_found': len(self.issues['not_using_i18n']),
                'missing_annotations_found': len(self.issues['missing_annotations']),
                'inconsistent_terms_found': len(self.issues['inconsistent_terms']),
                'medical_terms_needing_glossary': len(self.issues['medical_terms_without_glossary']),
            }
        }
    
    def print_summary(self) -> None:
        """Print summary of findings"""
        print("=" * 70)
        print("VIETNAMESE LOCALIZATION CHECK SUMMARY")
        print("=" * 70)
        print(f"\nFiles checked: {self.stats['files_checked']}")
        print(f"Total Vietnamese strings found: {self.stats['total_vietnamese_strings']}")
        print(f"\nIssues found:")
        print(f"  - Hardcoded strings (should use i18n): {len(self.issues['not_using_i18n'])}")
        print(f"  - Missing annotations: {len(self.issues['missing_annotations'])}")
        print(f"  - Inconsistent terms: {len(self.issues['inconsistent_terms'])}")
        print(f"  - Medical terms needing glossary: {len(self.issues['medical_terms_without_glossary'])}")
        
        # Print top issues
        if self.issues['not_using_i18n']:
            print("\nTop 10 hardcoded strings (should use i18n):")
            for issue in self.issues['not_using_i18n'][:10]:
                print(f"  {issue['file']}:{issue['line']} - '{issue['text']}' → use '{issue['suggested_key']}'")
        
        if self.issues['missing_annotations']:
            print("\nTop 10 missing annotations:")
            seen = set()
            for issue in self.issues['missing_annotations']:
                abbrev = issue['abbreviation']
                if abbrev not in seen:
                    print(f"  '{abbrev}' found in {issue['file']}:{issue['line']}")
                    seen.add(abbrev)
                    if len(seen) >= 10:
                        break


def main():
    """Main execution"""
    print("Checking Vietnamese localization...")
    print("=" * 70)
    
    checker = LocalizationChecker()
    checker.scan_codebase()
    
    checker.print_summary()
    
    # Save detailed report
    report = checker.generate_report()
    output_file = checker.root_dir / 'docs' / 'localization_check_report.json'
    output_file.parent.mkdir(exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    
    print(f"\nDetailed report saved to: {output_file}")


if __name__ == '__main__':
    main()
