"""
Script để tìm và sửa các file thiếu dấu } cuối
"""
import sys
from pathlib import Path
import ast

def check_file(file_path):
    """Kiểm tra file có lỗi syntax không"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        ast.parse(content)
        return True, None
    except SyntaxError as e:
        return False, str(e)
    except Exception as e:
        return False, str(e)

def fix_file(file_path):
    """Sửa file thiếu dấu } cuối"""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Kiểm tra dòng cuối
    if lines and not lines[-1].strip().endswith('}'):
        # Tìm dòng cuối có }
        last_brace_line = None
        for i in range(len(lines) - 1, -1, -1):
            if '}' in lines[i]:
                last_brace_line = i
                break
        
        if last_brace_line is not None:
            # Kiểm tra xem có thiếu } không
            content = ''.join(lines)
            open_count = content.count('{')
            close_count = content.count('}')
            
            if open_count > close_count:
                # Thêm }
                if lines[-1].strip().endswith(','):
                    lines[-1] = lines[-1].rstrip().rstrip(',') + '\n'
                lines.append('}\n')
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.writelines(lines)
                return True
    
    return False

def main():
    base_path = Path("drugs/drug_modules")
    fixed_files = []
    
    for py_file in base_path.rglob("*.py"):
        if py_file.name == '__init__.py' or py_file.name.endswith('.backup'):
            continue
        
        is_valid, error = check_file(py_file)
        if not is_valid and "'{' was never closed" in error:
            print(f"Fixing: {py_file}")
            if fix_file(py_file):
                # Kiểm tra lại
                is_valid_after, _ = check_file(py_file)
                if is_valid_after:
                    fixed_files.append(str(py_file))
                    print(f"  [OK] Fixed")
                else:
                    print(f"  [ERROR] Still has errors")
    
    print(f"\nFixed {len(fixed_files)} files")
    for f in fixed_files:
        print(f"  - {f}")

if __name__ == "__main__":
    main()

