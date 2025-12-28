"""
Script tạo HTML dashboard từ báo cáo guideline

Sử dụng:
    python scripts/create_guideline_dashboard.py
    python scripts/create_guideline_dashboard.py --input reports/guideline_check_*.md
"""

import re
from pathlib import Path
from datetime import datetime
import json
import sys

sys.path.insert(0, str(Path(__file__).parent))
from check_guideline_updates import GuidelineChecker, ARTICLES_DIR

def parse_markdown_report(report_path: Path):
    """Parse markdown report để lấy thông tin"""
    content = report_path.read_text(encoding='utf-8')
    
    # Extract tổng quan
    total_match = re.search(r'Tổng số file:\s*(\d+)', content)
    needs_check_match = re.search(r'Cần kiểm tra:\s*(\d+)', content)
    
    # Extract files cần kiểm tra
    files_needs_check = []
    sections = re.split(r'### ', content)
    
    for section in sections[1:]:  # Skip phần đầu
        if 'Các file cần kiểm tra guideline' in section:
            file_sections = section.split('\n\n')
            for file_section in file_sections[1:]:  # Skip header
                if not file_section.strip():
                    continue
                
                lines = file_section.split('\n')
                if not lines:
                    continue
                
                file_name = lines[0].strip()
                if not file_name.endswith('.md'):
                    continue
                
                file_info = {
                    "file": file_name,
                    "guidelines": [],
                    "reasons": []
                }
                
                for line in lines:
                    if line.startswith('- '):
                        if 'Guideline' in line or any(g in line for g in ['ESC', 'ACC', 'ADA', 'KDIGO', 'GOLD', 'GINA']):
                            file_info["guidelines"].append(line.replace('- ', '').strip())
                    elif 'Lý do' in line:
                        continue
                    elif line.startswith('  - '):
                        file_info["reasons"].append(line.replace('  - ', '').strip())
                
                if file_info["guidelines"] or file_info["reasons"]:
                    files_needs_check.append(file_info)
    
    return {
        "total": int(total_match.group(1)) if total_match else 0,
        "needs_check": int(needs_check_match.group(1)) if needs_check_match else 0,
        "files": files_needs_check
    }

def create_html_dashboard(data, output_path: Path):
    """Tạo HTML dashboard"""
    
    total = data.get("total", 0)
    needs_check = data.get("needs_check", 0)
    no_check = total - needs_check
    needs_check_pct = (needs_check / total * 100) if total > 0 else 0
    
    html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Guideline Checker Dashboard</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: #f5f5f5;
            padding: 20px;
            color: #333;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            padding: 30px;
        }}
        
        h1 {{
            color: #2c3e50;
            margin-bottom: 10px;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
        }}
        
        .meta {{
            color: #7f8c8d;
            margin-bottom: 30px;
            font-size: 14px;
        }}
        
        .stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}
        
        .stat-card {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 8px;
            text-align: center;
        }}
        
        .stat-card.warning {{
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        }}
        
        .stat-card.success {{
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        }}
        
        .stat-card .number {{
            font-size: 36px;
            font-weight: bold;
            margin-bottom: 5px;
        }}
        
        .stat-card .label {{
            font-size: 14px;
            opacity: 0.9;
        }}
        
        .progress-bar {{
            width: 100%;
            height: 30px;
            background: #ecf0f1;
            border-radius: 15px;
            overflow: hidden;
            margin: 20px 0;
        }}
        
        .progress-fill {{
            height: 100%;
            background: linear-gradient(90deg, #f093fb 0%, #f5576c 100%);
            transition: width 0.3s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: bold;
            font-size: 14px;
        }}
        
        .files-list {{
            margin-top: 30px;
        }}
        
        .file-item {{
            background: #fff;
            border: 1px solid #e0e0e0;
            border-left: 4px solid #e74c3c;
            padding: 15px;
            margin-bottom: 15px;
            border-radius: 4px;
            transition: box-shadow 0.2s;
        }}
        
        .file-item:hover {{
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}
        
        .file-name {{
            font-weight: bold;
            color: #2c3e50;
            margin-bottom: 10px;
            font-size: 16px;
        }}
        
        .guidelines {{
            margin: 10px 0;
        }}
        
        .guideline-tag {{
            display: inline-block;
            background: #3498db;
            color: white;
            padding: 4px 10px;
            border-radius: 12px;
            font-size: 12px;
            margin: 2px;
        }}
        
        .reasons {{
            margin-top: 10px;
            padding-left: 20px;
        }}
        
        .reason-item {{
            color: #e74c3c;
            font-size: 13px;
            margin: 5px 0;
        }}
        
        .no-files {{
            text-align: center;
            padding: 40px;
            color: #95a5a6;
            font-size: 18px;
        }}
        
        .footer {{
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #e0e0e0;
            text-align: center;
            color: #7f8c8d;
            font-size: 12px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 Guideline Checker Dashboard</h1>
        <div class="meta">
            Cập nhật: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
        </div>
        
        <div class="stats">
            <div class="stat-card">
                <div class="number">{total}</div>
                <div class="label">Tổng số file</div>
            </div>
            <div class="stat-card warning">
                <div class="number">{needs_check}</div>
                <div class="label">Cần kiểm tra</div>
            </div>
            <div class="stat-card success">
                <div class="number">{no_check}</div>
                <div class="label">Không cần kiểm tra</div>
            </div>
        </div>
        
        <div class="progress-bar">
            <div class="progress-fill" style="width: {needs_check_pct}%">
                {needs_check_pct:.1f}% cần kiểm tra
            </div>
        </div>
        
        <div class="files-list">
            <h2>📋 Files cần kiểm tra guideline</h2>
"""
    
    if data.get("files"):
        for file_info in data["files"][:50]:  # Limit 50 files
            file_name = file_info.get("file", "")
            guidelines = file_info.get("guidelines", [])
            reasons = file_info.get("reasons", [])
            
            html += f"""
            <div class="file-item">
                <div class="file-name">📄 {file_name}</div>
"""
            if guidelines:
                html += '<div class="guidelines">'
                for guideline in guidelines[:5]:  # Limit 5 guidelines
                    html += f'<span class="guideline-tag">{guideline}</span>'
                html += '</div>'
            
            if reasons:
                html += '<div class="reasons">'
                for reason in reasons[:3]:  # Limit 3 reasons
                    html += f'<div class="reason-item">⚠️ {reason}</div>'
                html += '</div>'
            
            html += '</div>'
    else:
        html += '<div class="no-files">✅ Không có file nào cần kiểm tra</div>'
    
    html += """
        </div>
        
        <div class="footer">
            <p>Generated by Guideline Checker Scripts</p>
            <p>Chạy: <code>python scripts/check_guideline_updates.py</code> để cập nhật</p>
        </div>
    </div>
</body>
</html>
"""
    
    output_path.write_text(html, encoding='utf-8')
    print(f"✅ Đã tạo dashboard: {output_path}")

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Tạo HTML dashboard từ báo cáo guideline")
    parser.add_argument(
        "--input",
        type=str,
        help="File markdown report (mặc định: báo cáo mới nhất trong reports/)"
    )
    parser.add_argument(
        "--output",
        type=str,
        help="File HTML output (mặc định: reports/dashboard.html)"
    )
    
    args = parser.parse_args()
    
    # Xác định input
    if args.input:
        input_path = Path(args.input)
    else:
        # Tìm báo cáo mới nhất
        reports_dir = Path("reports")
        if reports_dir.exists():
            md_files = list(reports_dir.glob("guideline_check_*.md"))
            if md_files:
                input_path = max(md_files, key=lambda p: p.stat().st_mtime)
            else:
                print("⚠️  Không tìm thấy báo cáo. Đang tạo báo cáo mới...")
                from check_guideline_updates import main as check_main
                import sys
                sys.argv = ["check_guideline_updates.py", "--report-only"]
                check_main()
                md_files = list(reports_dir.glob("guideline_check_*.md"))
                if md_files:
                    input_path = max(md_files, key=lambda p: p.stat().st_mtime)
                else:
                    print("❌ Không thể tạo báo cáo")
                    return
        else:
            print("❌ Thư mục reports/ không tồn tại")
            return
    
    # Parse báo cáo
    print(f"Đang đọc báo cáo: {input_path}")
    data = parse_markdown_report(input_path)
    
    # Xác định output
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = Path("reports/dashboard.html")
    
    # Tạo dashboard
    output_path.parent.mkdir(parents=True, exist_ok=True)
    create_html_dashboard(data, output_path)

if __name__ == "__main__":
    main()

