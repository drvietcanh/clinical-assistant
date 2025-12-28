"""
Script nhanh để cập nhật ngày review cho tất cả các bài viết

Sử dụng:
    python scripts/update_guideline_dates.py [--dry-run]
"""

import re
from pathlib import Path
from datetime import datetime

ARTICLES_DIR = Path("content/articles")
CURRENT_DATE = datetime.now()
CURRENT_MONTH = CURRENT_DATE.month
CURRENT_YEAR = CURRENT_DATE.year
CURRENT_DATE_STR = f"{CURRENT_YEAR}-{CURRENT_MONTH:02d}"


def update_file_dates(file_path: Path, dry_run: bool = True):
    """Cập nhật ngày trong một file"""
    try:
        content = file_path.read_text(encoding='utf-8')
        original_content = content
        updated = False
        
        # Cập nhật last_reviewed trong frontmatter
        if re.search(r'last_reviewed:\s*\d{4}-\d{2}', content):
            content = re.sub(
                r'last_reviewed:\s*\d{4}-\d{2}',
                f'last_reviewed: {CURRENT_DATE_STR}',
                content
            )
            updated = True
        
        # Cập nhật "Cập nhật:" trong header
        if re.search(r'\*\*Cập nhật:\*\*\s*Tháng\s+\d{1,2}/\d{4}', content):
            content = re.sub(
                r'\*\*Cập nhật:\*\*\s*Tháng\s+\d{1,2}/\d{4}',
                f'**Cập nhật:** Tháng {CURRENT_MONTH}/{CURRENT_YEAR}',
                content
            )
            updated = True
        
        if updated:
            if not dry_run:
                file_path.write_text(content, encoding='utf-8')
                print(f"✅ {file_path.name}")
                return True
            else:
                print(f"📝 {file_path.name} (sẽ cập nhật)")
                return True
        
        return False
    
    except Exception as e:
        print(f"❌ {file_path.name}: {e}")
        return False


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Cập nhật ngày review cho tất cả bài viết")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Chỉ hiển thị những file sẽ được cập nhật, không thực sự cập nhật"
    )
    
    args = parser.parse_args()
    
    md_files = list(ARTICLES_DIR.glob("*.md"))
    print(f"Tìm thấy {len(md_files)} file markdown")
    print(f"Ngày cập nhật: {CURRENT_DATE_STR} ({CURRENT_MONTH}/{CURRENT_YEAR})")
    print()
    
    if args.dry_run:
        print("🔍 DRY-RUN MODE: Chỉ hiển thị, không cập nhật file")
        print()
    
    updated_count = 0
    for file_path in sorted(md_files):
        if update_file_dates(file_path, dry_run=args.dry_run):
            updated_count += 1
    
    print()
    if args.dry_run:
        print(f"📊 Sẽ cập nhật {updated_count} file")
        print("   Chạy lại không có --dry-run để thực sự cập nhật")
    else:
        print(f"✅ Đã cập nhật {updated_count} file")


if __name__ == "__main__":
    main()

