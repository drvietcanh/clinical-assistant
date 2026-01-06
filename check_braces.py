import sys

def check_braces(filename):
    with open(filename, encoding='utf-8') as f:
        lines = f.readlines()
    
    brace_count = 0
    for i, line in enumerate(lines, 1):
        open_braces = line.count('{')
        close_braces = line.count('}')
        brace_count += open_braces - close_braces
        
        if i >= len(lines) - 10 or brace_count < 0:
            print(f'Line {i}: brace_count={brace_count}, line={repr(line[:60].rstrip())}')
    
    print(f'\nFinal brace_count: {brace_count}')

if __name__ == '__main__':
    check_braces(sys.argv[1])
