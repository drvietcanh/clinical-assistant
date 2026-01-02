"""
Phân tích kích thước file và đề xuất chia nhỏ
"""
import os
from pathlib import Path
from collections import defaultdict

def analyze_file(file_path):
    """Phân tích một file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        total_lines = len(lines)
        empty_lines = sum(1 for l in lines if not l.strip())
        comment_lines = sum(1 for l in lines if l.strip().startswith('#'))
        data_lines = sum(1 for l in lines if '{' in l or '[' in l or '=' in l and ('{' in l or '[' in l))
        code_lines = total_lines - empty_lines - comment_lines
        
        return {
            'total': total_lines,
            'empty': empty_lines,
            'comments': comment_lines,
            'data': data_lines,
            'code': code_lines,
            'is_data_file': data_lines > total_lines * 0.5
        }
    except Exception as e:
        return {'error': str(e)}

def main():
    base_path = Path('.')
    files_info = []
    
    # Tìm tất cả file Python
    for py_file in base_path.rglob('*.py'):
        if any(skip in str(py_file) for skip in ['__pycache__', '.pyc', 'backup', '.bak', 'venv', '.git']):
            continue
        
        rel_path = str(py_file.relative_to(base_path))
        info = analyze_file(py_file)
        if 'error' not in info:
            info['path'] = rel_path
            files_info.append(info)
    
    # Sắp xếp theo số dòng
    files_info.sort(key=lambda x: x['total'], reverse=True)
    
    # In top 30 file dài nhất
    print("=" * 80)
    print("TOP 30 FILE DAI NHAT")
    print("=" * 80)
    print(f"{'File':<60} {'Total':<8} {'Code':<8} {'Data':<8} {'Type':<10}")
    print("-" * 80)
    
    for info in files_info[:30]:
        file_type = "DATA" if info['is_data_file'] else "CODE"
        print(f"{info['path']:<60} {info['total']:<8} {info['code']:<8} {info['data']:<8} {file_type:<10}")
    
    # Phân tích theo loại
    print("\n" + "=" * 80)
    print("PHAN TICH THEO LOAI FILE")
    print("=" * 80)
    
    code_files = [f for f in files_info if not f['is_data_file'] and f['total'] > 1000]
    data_files = [f for f in files_info if f['is_data_file'] and f['total'] > 1000]
    
    print(f"\nCODE FILES (>1000 dong): {len(code_files)}")
    for f in code_files[:10]:
        print(f"  - {f['path']}: {f['total']} dong (code: {f['code']})")
    
    print(f"\nDATA FILES (>1000 dong): {len(data_files)}")
    for f in data_files[:10]:
        print(f"  - {f['path']}: {f['total']} dong (data: {f['data']})")
    
    # Đề xuất chia nhỏ
    print("\n" + "=" * 80)
    print("DE XUAT CHIA NHO FILE")
    print("=" * 80)
    
    threshold = 2000
    large_files = [f for f in files_info if f['total'] > threshold]
    
    print(f"\nFiles > {threshold} dong can xem xet chia nho:\n")
    for f in large_files:
        print(f"{f['path']}")
        print(f"   - Tong: {f['total']} dong")
        print(f"   - Code: {f['code']} dong")
        print(f"   - Data: {f['data']} dong")
        print(f"   - Loai: {'DATA FILE' if f['is_data_file'] else 'CODE FILE'}")
        
        if f['is_data_file']:
            print(f"   De xuat: Chia theo category hoac nhom thuoc/benh")
        else:
            print(f"   De xuat: Tach thanh modules nho hon, moi module < 1000 dong")
        print()

if __name__ == '__main__':
    main()

