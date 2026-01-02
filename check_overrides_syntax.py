
import sys

try:
    with open(r"d:\1 medical\drugs\enhanced_fields_overrides.py", "r", encoding="utf-8") as f:
        content = f.read()
        compile(content, "enhanced_fields_overrides.py", "exec")
    print("SUCCESS: Syntax check passed for enhanced_fields_overrides.py")
except SyntaxError as e:
    print(f"FAILED: SyntaxError: {e}")
except Exception as e:
    print(f"FAILED: Generic Error: {e}")
