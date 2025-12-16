"""
Script tự động kiểm tra và sửa số thập phân dư không có ý nghĩa lâm sàng

Usage:
    python utils/fix_decimal_precision.py --check    # Chỉ kiểm tra và báo cáo
    python utils/fix_decimal_precision.py --fix       # Tự động sửa
    python utils/fix_decimal_precision.py --fix --dry-run  # Xem sẽ sửa gì nhưng không sửa thật
"""

import re
import os
from pathlib import Path
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
from enum import Enum


class PrecisionLevel(Enum):
    """Mức độ chính xác cho các loại giá trị lâm sàng"""
    INTEGER = 0      # Số nguyên (0 chữ số thập phân)
    ONE_DECIMAL = 1  # 1 chữ số thập phân
    TWO_DECIMAL = 2  # 2 chữ số thập phân
    THREE_DECIMAL = 3  # 3 chữ số thập phân (hiếm khi cần)


@dataclass
class DecimalIssue:
    """Thông tin về một lỗi số thập phân"""
    file_path: str
    line_number: int
    line_content: str
    current_precision: int
    recommended_precision: int
    context: str
    value_type: str


class DecimalPrecisionFixer:
    """Class để kiểm tra và sửa số thập phân dư"""
    
    # Các pattern để nhận diện giá trị lâm sàng
    CLINICAL_PATTERNS = {
        # Vital signs - số nguyên
        r'(mmHg|bpm|beats/min|breaths/min|°C|°F)': PrecisionLevel.INTEGER,
        
        # Weight, height - 1 chữ số
        r'(kg|g|lb|pounds?|cm|m|inches?)': PrecisionLevel.ONE_DECIMAL,
        
        # Lab values - 1-2 chữ số
        r'(mg/dL|mmol/L|mEq/L|µmol/L|ng/mL|µg/mL|IU/L|U/L|g/L|g/dL)': PrecisionLevel.TWO_DECIMAL,
        
        # Medication doses - 1-2 chữ số
        r'(mg|mcg|µg|units?|IU)/': PrecisionLevel.TWO_DECIMAL,
        r'(mg/kg|mcg/kg|µg/kg|units/kg)': PrecisionLevel.TWO_DECIMAL,
        r'(mg/h|mcg/h|µg/h|units/h)': PrecisionLevel.TWO_DECIMAL,
        r'(mg/ngày|mcg/ngày|µg/ngày|units/ngày)': PrecisionLevel.TWO_DECIMAL,
        
        # Volumes - 1-2 chữ số
        r'(mL|ml|L|l|liters?)': PrecisionLevel.TWO_DECIMAL,
        
        # Scores - 1-2 chữ số
        r'(score|điểm|points?|RTS|SOFA|APACHE|GCS|NIHSS)': PrecisionLevel.TWO_DECIMAL,
        
        # Percentages - 1 chữ số
        r'(%|percent|phần trăm)': PrecisionLevel.ONE_DECIMAL,
        
        # Time intervals - 2 chữ số
        r'(s|seconds?|giây|h|hours?|giờ|min|minutes?|phút)': PrecisionLevel.TWO_DECIMAL,
        
        # Pressure - 1 chữ số
        r'(cmH2O|cm H2O|cmH₂O)': PrecisionLevel.ONE_DECIMAL,
        
        # BSA, ratios - 2 chữ số
        r'(m²|BSA|ratio|tỷ lệ)': PrecisionLevel.TWO_DECIMAL,
    }
    
    # Các file/thư mục bỏ qua (test, debug, logging)
    IGNORE_PATTERNS = [
        r'test_.*\.py$',
        r'.*_test\.py$',
        r'utils/performance_monitor\.py$',
        r'utils/logger.*\.py$',
        r'__pycache__',
        r'\.pyc$',
    ]
    
    # Các pattern format string cần kiểm tra
    FORMAT_PATTERNS = [
        r'f"[^"]*\{[^}]*:\.([3-9]|\d{2,})f[^}]*\}[^"]*"',  # f-string với .3f trở lên
        r'f\'[^\']*\{[^}]*:\.([3-9]|\d{2,})f[^}]*\}[^\']*\'',  # f-string với single quotes
        r'format\([^,]+,\s*[\'"]\.([3-9]|\d{2,})f[\'"]',  # .format() với .3f trở lên
        r'\.format\([^)]*\.([3-9]|\d{2,})f',  # .format() khác
    ]
    
    def __init__(self, root_dir: str = "."):
        self.root_dir = Path(root_dir)
        self.issues: List[DecimalIssue] = []
        
    def should_ignore_file(self, file_path: Path) -> bool:
        """Kiểm tra xem file có nên bỏ qua không"""
        file_str = str(file_path)
        for pattern in self.IGNORE_PATTERNS:
            if re.search(pattern, file_str):
                return True
        return False
    
    def is_clinical_value(self, line: str, match: re.Match) -> bool:
        """Kiểm tra xem giá trị có phải là giá trị lâm sàng không"""
        # Kiểm tra xem có chứa các từ khóa lâm sàng không
        line_lower = line.lower()
        
        # Bỏ qua nếu là logging/debug (logger.info, logger.error, print, etc.)
        # nhưng không phải Streamlit (st.info, st.metric, etc.)
        if any(keyword in line_lower for keyword in ['logger.', 'logger.info', 'logger.error', 
                                                      'logger.warning', 'logger.debug', 
                                                      'print(', 'debug(', 'log(']):
            # Chỉ giữ lại nếu có từ khóa Streamlit (st.metric, st.info, etc.)
            if not any(keyword in line_lower for keyword in ['st.metric', 'st.info', 'st.success', 
                                                              'st.warning', 'st.error', 'st.caption', 
                                                              'st.markdown', 'render_result']):
                return False
        
        # Kiểm tra các pattern lâm sàng
        for pattern, precision in self.CLINICAL_PATTERNS.items():
            if re.search(pattern, line, re.IGNORECASE):
                return True
        
        # Kiểm tra xem có trong context Streamlit không (thường là hiển thị cho user)
        if any(keyword in line for keyword in ['st.metric', 'st.info', 'st.success', 'st.warning', 
                                                'st.error', 'st.caption', 'st.markdown', 'render_result']):
            return True
            
        return False
    
    def get_recommended_precision(self, line: str) -> PrecisionLevel:
        """Xác định độ chính xác khuyến nghị dựa trên context"""
        line_lower = line.lower()
        
        # Kiểm tra các pattern cụ thể
        for pattern, precision in self.CLINICAL_PATTERNS.items():
            if re.search(pattern, line, re.IGNORECASE):
                return precision
        
        # Mặc định: 2 chữ số cho các giá trị lâm sàng không xác định
        return PrecisionLevel.TWO_DECIMAL
    
    def find_decimal_issues(self) -> List[DecimalIssue]:
        """Tìm tất cả các lỗi số thập phân"""
        self.issues = []
        
        # Tìm tất cả file Python
        python_files = list(self.root_dir.rglob("*.py"))
        
        for file_path in python_files:
            if self.should_ignore_file(file_path):
                continue
                
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    
                for line_num, line in enumerate(lines, 1):
                    # Tìm các format string với precision >= 3
                    for pattern in self.FORMAT_PATTERNS:
                        matches = re.finditer(pattern, line)
                        for match in matches:
                            precision_str = match.group(1)
                            try:
                                precision = int(precision_str)
                            except ValueError:
                                continue
                                
                            if precision >= 3:
                                # Kiểm tra xem có phải giá trị lâm sàng không
                                if self.is_clinical_value(line, match):
                                    recommended = self.get_recommended_precision(line)
                                    
                                    # Xác định loại giá trị
                                    value_type = "Unknown"
                                    for pat, prec in self.CLINICAL_PATTERNS.items():
                                        if re.search(pat, line, re.IGNORECASE):
                                            value_type = pat
                                            break
                                    
                                    issue = DecimalIssue(
                                        file_path=str(file_path.relative_to(self.root_dir)),
                                        line_number=line_num,
                                        line_content=line.strip(),
                                        current_precision=precision,
                                        recommended_precision=recommended.value,
                                        context=line.strip()[:100],
                                        value_type=value_type
                                    )
                                    self.issues.append(issue)
            except Exception as e:
                print(f"⚠️  Lỗi khi đọc {file_path}: {e}")
                
        return self.issues
    
    def fix_issue(self, issue: DecimalIssue, dry_run: bool = False) -> bool:
        """Sửa một lỗi cụ thể"""
        file_path = self.root_dir / issue.file_path
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            line = lines[issue.line_number - 1]
            original_line = line
            
            # Thay thế precision
            # Tìm và thay thế .3f, .4f, etc. thành .{recommended}f
            new_line = re.sub(
                rf':\.([3-9]|\d{{2,}})f',
                f':.{issue.recommended_precision}f',
                line
            )
            
            if new_line != original_line:
                if not dry_run:
                    lines[issue.line_number - 1] = new_line
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.writelines(lines)
                return True
        except Exception as e:
            print(f"❌ Lỗi khi sửa {file_path}:{issue.line_number}: {e}")
            return False
            
        return False
    
    def generate_report(self, output_file: Optional[str] = None) -> str:
        """Tạo báo cáo chi tiết"""
        report_lines = [
            "# BÁO CÁO KIỂM TRA SỐ THẬP PHÂN DƯ",
            "",
            f"**Tổng số lỗi tìm thấy:** {len(self.issues)}",
            "",
            "## Chi tiết các lỗi:",
            ""
        ]
        
        # Nhóm theo file
        issues_by_file = {}
        for issue in self.issues:
            if issue.file_path not in issues_by_file:
                issues_by_file[issue.file_path] = []
            issues_by_file[issue.file_path].append(issue)
        
        for file_path, file_issues in sorted(issues_by_file.items()):
            report_lines.append(f"### {file_path}")
            report_lines.append(f"**Số lỗi:** {len(file_issues)}")
            report_lines.append("")
            
            for issue in file_issues:
                report_lines.append(f"- **Dòng {issue.line_number}:** `.{issue.current_precision}f` → `.{issue.recommended_precision}f`")
                report_lines.append(f"  ```python")
                report_lines.append(f"  {issue.line_content}")
                report_lines.append(f"  ```")
                report_lines.append(f"  *Loại giá trị:* {issue.value_type}")
                report_lines.append("")
        
        report = "\n".join(report_lines)
        
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(report)
            print(f"✅ Báo cáo đã lưu vào: {output_file}")
        
        return report


def main():
    """Main function"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Kiểm tra và sửa số thập phân dư không có ý nghĩa lâm sàng"
    )
    parser.add_argument(
        '--check',
        action='store_true',
        help='Chỉ kiểm tra và tạo báo cáo, không sửa'
    )
    parser.add_argument(
        '--fix',
        action='store_true',
        help='Tự động sửa các lỗi tìm thấy'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Xem sẽ sửa gì nhưng không sửa thật (chỉ dùng với --fix)'
    )
    parser.add_argument(
        '--report',
        type=str,
        default='DECIMAL_PRECISION_REPORT.md',
        help='File để lưu báo cáo (mặc định: DECIMAL_PRECISION_REPORT.md)'
    )
    parser.add_argument(
        '--root',
        type=str,
        default='.',
        help='Thư mục gốc để quét (mặc định: thư mục hiện tại)'
    )
    
    args = parser.parse_args()
    
    if not args.check and not args.fix:
        parser.print_help()
        return
    
    print("🔍 Đang quét codebase để tìm số thập phân dư...")
    fixer = DecimalPrecisionFixer(root_dir=args.root)
    issues = fixer.find_decimal_issues()
    
    print(f"\n📊 Tìm thấy {len(issues)} lỗi số thập phân dư")
    
    if len(issues) == 0:
        print("✅ Không có lỗi nào!")
        return
    
    # Hiển thị tóm tắt
    print("\n📋 Tóm tắt:")
    issues_by_file = {}
    for issue in issues:
        if issue.file_path not in issues_by_file:
            issues_by_file[issue.file_path] = 0
        issues_by_file[issue.file_path] += 1
    
    for file_path, count in sorted(issues_by_file.items()):
        print(f"  - {file_path}: {count} lỗi")
    
    # Tạo báo cáo
    if args.check or args.fix:
        report = fixer.generate_report(args.report)
        print(f"\n📄 Báo cáo chi tiết đã được tạo: {args.report}")
    
    # Sửa nếu được yêu cầu
    if args.fix:
        print(f"\n🔧 Đang sửa các lỗi...")
        fixed_count = 0
        for issue in issues:
            if fixer.fix_issue(issue, dry_run=args.dry_run):
                fixed_count += 1
                if args.dry_run:
                    print(f"  [DRY-RUN] Sẽ sửa: {issue.file_path}:{issue.line_number}")
                else:
                    print(f"  ✅ Đã sửa: {issue.file_path}:{issue.line_number}")
        
        if args.dry_run:
            print(f"\n⚠️  DRY-RUN: Sẽ sửa {fixed_count}/{len(issues)} lỗi")
        else:
            print(f"\n✅ Đã sửa {fixed_count}/{len(issues)} lỗi")


if __name__ == "__main__":
    main()

