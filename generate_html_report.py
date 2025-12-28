#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script tạo báo cáo HTML đẹp từ kết quả validation
"""

import json
from datetime import datetime

def load_validation_report():
    """Đọc báo cáo validation"""
    try:
        with open('drug_validation_report.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("❌ Không tìm thấy drug_validation_report.json")
        print("   Vui lòng chạy comprehensive_drug_validation.py trước")
        return None

def generate_html_report(report):
    """Tạo báo cáo HTML"""
    
    stats = report["summary"]
    field_completion = report["field_completion"]
    
    html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Báo Cáo Kiểm Tra Dữ Liệu Thuốc</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            min-height: 100vh;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 10px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            overflow: hidden;
        }}
        
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }}
        
        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        
        .header .date {{
            opacity: 0.9;
            font-size: 1.1em;
        }}
        
        .content {{
            padding: 30px;
        }}
        
        .section {{
            margin-bottom: 40px;
        }}
        
        .section h2 {{
            color: #667eea;
            font-size: 1.8em;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 3px solid #667eea;
        }}
        
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}
        
        .stat-card {{
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        
        .stat-card .number {{
            font-size: 2.5em;
            font-weight: bold;
            color: #667eea;
            margin-bottom: 10px;
        }}
        
        .stat-card .label {{
            font-size: 1.1em;
            color: #555;
        }}
        
        .stat-card.success {{
            background: linear-gradient(135deg, #84fab0 0%, #8fd3f4 100%);
        }}
        
        .stat-card.warning {{
            background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
        }}
        
        .stat-card.error {{
            background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%);
        }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        
        th {{
            background: #667eea;
            color: white;
            padding: 15px;
            text-align: left;
            font-weight: 600;
        }}
        
        td {{
            padding: 12px 15px;
            border-bottom: 1px solid #eee;
        }}
        
        tr:hover {{
            background: #f5f7fa;
        }}
        
        .badge {{
            display: inline-block;
            padding: 5px 10px;
            border-radius: 20px;
            font-size: 0.9em;
            font-weight: 600;
        }}
        
        .badge-success {{
            background: #84fab0;
            color: #2d5016;
        }}
        
        .badge-warning {{
            background: #ffecd2;
            color: #8b4513;
        }}
        
        .badge-error {{
            background: #ff9a9e;
            color: #8b0000;
        }}
        
        .progress-bar {{
            width: 100%;
            height: 25px;
            background: #e0e0e0;
            border-radius: 15px;
            overflow: hidden;
            margin-top: 5px;
        }}
        
        .progress-fill {{
            height: 100%;
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            transition: width 0.3s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: 600;
            font-size: 0.9em;
        }}
        
        .error-list {{
            background: #fff5f5;
            border-left: 4px solid #ff6b6b;
            padding: 15px;
            margin: 10px 0;
            border-radius: 5px;
        }}
        
        .error-list h3 {{
            color: #c92a2a;
            margin-bottom: 10px;
        }}
        
        .error-item {{
            margin: 8px 0;
            padding: 8px;
            background: white;
            border-radius: 5px;
        }}
        
        .drug-name {{
            font-weight: 600;
            color: #667eea;
        }}
        
        @media (max-width: 768px) {{
            .stats-grid {{
                grid-template-columns: 1fr;
            }}
            
            table {{
                font-size: 0.9em;
            }}
            
            th, td {{
                padding: 8px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📊 Báo Cáo Kiểm Tra Dữ Liệu Thuốc</h1>
            <div class="date">Ngày tạo: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}</div>
        </div>
        
        <div class="content">
            <!-- Thống kê tổng quan -->
            <div class="section">
                <h2>📈 Thống Kê Tổng Quan</h2>
                <div class="stats-grid">
                    <div class="stat-card">
                        <div class="number">{stats['total_drugs']}</div>
                        <div class="label">Tổng Số Thuốc</div>
                    </div>
                    <div class="stat-card success">
                        <div class="number">{stats['complete_drugs']}</div>
                        <div class="label">Thuốc Hoàn Chỉnh</div>
                        <div style="margin-top: 10px; font-size: 0.9em;">
                            ({stats['complete_drugs']/stats['total_drugs']*100:.1f}%)
                        </div>
                    </div>
                    <div class="stat-card warning">
                        <div class="number">{stats['incomplete_drugs']}</div>
                        <div class="label">Thuốc Chưa Hoàn Chỉnh</div>
                        <div style="margin-top: 10px; font-size: 0.9em;">
                            ({stats['incomplete_drugs']/stats['total_drugs']*100:.1f}%)
                        </div>
                    </div>
                    <div class="stat-card error">
                        <div class="number">{stats['error_count']}</div>
                        <div class="label">Tổng Số Lỗi</div>
                    </div>
                    <div class="stat-card warning">
                        <div class="number">{stats['warning_count']}</div>
                        <div class="label">Tổng Số Cảnh Báo</div>
                    </div>
                </div>
            </div>
            
            <!-- Hoàn thành Enhanced Fields -->
            <div class="section">
                <h2>📋 Hoàn Thành Enhanced Fields</h2>
                <table>
                    <thead>
                        <tr>
                            <th>Field</th>
                            <th>Hoàn Thành</th>
                            <th>Tỷ Lệ</th>
                            <th>Thiếu</th>
                            <th>Trạng Thái</th>
                        </tr>
                    </thead>
                    <tbody>
"""
    
    # Sắp xếp fields theo tỷ lệ hoàn thành
    sorted_fields = sorted(
        field_completion.items(),
        key=lambda x: x[1]['percentage'],
        reverse=True
    )
    
    for field, data in sorted_fields:
        percentage = data['percentage']
        count = data['count']
        missing = data['missing']
        total = stats['total_drugs']
        
        if percentage == 100:
            status_badge = '<span class="badge badge-success">✅ Hoàn thành</span>'
            status_class = "success"
        elif percentage >= 80:
            status_badge = '<span class="badge badge-warning">⚠️ Tốt</span>'
            status_class = "warning"
        else:
            status_badge = '<span class="badge badge-error">❌ Cần cải thiện</span>'
            status_class = "error"
        
        html += f"""
                        <tr>
                            <td><strong>{field}</strong></td>
                            <td>{count}/{total}</td>
                            <td>
                                <div class="progress-bar">
                                    <div class="progress-fill" style="width: {percentage}%">
                                        {percentage:.1f}%
                                    </div>
                                </div>
                            </td>
                            <td>{missing}</td>
                            <td>{status_badge}</td>
                        </tr>
"""
    
    html += """
                    </tbody>
                </table>
            </div>
            
            <!-- Thuốc có lỗi -->
"""
    
    if report["drugs_with_errors"]:
        html += """
            <div class="section">
                <h2>❌ Thuốc Có Lỗi</h2>
"""
        for drug in sorted(report["drugs_with_errors"])[:30]:  # Hiển thị 30 đầu tiên
            html += f"""
                <div class="error-list">
                    <h3><span class="drug-name">{drug}</span></h3>
"""
            for error in report["errors_by_drug"][drug][:5]:  # 5 lỗi đầu
                html += f"""
                    <div class="error-item">{error}</div>
"""
            if len(report["errors_by_drug"][drug]) > 5:
                html += f"""
                    <div class="error-item" style="opacity: 0.7;">
                        ... và {len(report['errors_by_drug'][drug]) - 5} lỗi khác
                    </div>
"""
            html += """
                </div>
"""
        
        if len(report["drugs_with_errors"]) > 30:
            html += f"""
                <div style="text-align: center; margin-top: 20px; color: #666;">
                    ... và {len(report['drugs_with_errors']) - 30} thuốc khác
                </div>
"""
        html += """
            </div>
"""
    
    html += """
        </div>
    </div>
</body>
</html>
"""
    
    return html

def main():
    """Hàm chính"""
    print("Đang tạo báo cáo HTML...")
    
    report = load_validation_report()
    if not report:
        return
    
    html = generate_html_report(report)
    
    output_file = "drug_validation_report.html"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ Đã tạo báo cáo HTML: {output_file}")
    print(f"   Mở file trong trình duyệt để xem")

if __name__ == '__main__':
    main()

