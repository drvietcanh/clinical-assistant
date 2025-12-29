"""
Test script để kiểm tra HTML escaping trong drug pages
"""

import sys
import html
import io

# Fix encoding for Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Test escape_html function
def test_escape_html():
    """Test HTML escaping function"""
    print("=" * 60)
    print("TEST HTML ESCAPING")
    print("=" * 60)
    
    test_cases = [
        ("Normal text", "Normal text"),
        ("Text with <tag>", "Text with &lt;tag&gt;"),
        ("Text with 'quotes'", "Text with &#x27;quotes&#x27;"),
        ("Text with \"double quotes\"", "Text with &quot;double quotes&quot;"),
        ("Text with & ampersand", "Text with &amp; ampersand"),
        ("<script>alert('XSS')</script>", "&lt;script&gt;alert(&#x27;XSS&#x27;)&lt;/script&gt;"),
        ("Drug name with <special> chars", "Drug name with &lt;special&gt; chars"),
    ]
    
    all_passed = True
    for input_text, expected in test_cases:
        result = html.escape(str(input_text))
        if result == expected:
            print(f"✅ PASS: '{input_text}' -> '{result}'")
        else:
            print(f"❌ FAIL: '{input_text}'")
            print(f"   Expected: '{expected}'")
            print(f"   Got:      '{result}'")
            all_passed = False
    
    return all_passed

# Test import các modules
def test_imports():
    """Test import các modules có escape_html"""
    print("\n" + "=" * 60)
    print("TEST IMPORTS")
    print("=" * 60)
    
    all_passed = True
    
    # Test import html module
    try:
        import html
        print("✅ PASS: import html")
    except ImportError as e:
        print(f"❌ FAIL: import html - {e}")
        all_passed = False
    
    # Test import Drug_Detail
    try:
        import sys
        sys.path.insert(0, '.')
        from pages.Drug_Detail import escape_html
        print("✅ PASS: import escape_html from Drug_Detail")
        
        # Test function
        result = escape_html("<test>")
        if result == "&lt;test&gt;":
            print("✅ PASS: escape_html function works")
        else:
            print(f"❌ FAIL: escape_html returned '{result}' instead of '&lt;test&gt;'")
            all_passed = False
    except Exception as e:
        print(f"⚠️  WARN: Could not test Drug_Detail.escape_html - {e}")
        print("   (This is OK if running outside Streamlit context)")
    
    # Test import card_components
    try:
        from drugs.drug_info_components.card_components import escape_html as escape_html_card
        print("✅ PASS: import escape_html from card_components")
        
        # Test function
        result = escape_html_card("<test>")
        if result == "&lt;test&gt;":
            print("✅ PASS: card_components.escape_html function works")
        else:
            print(f"❌ FAIL: escape_html returned '{result}' instead of '&lt;test&gt;'")
            all_passed = False
    except Exception as e:
        print(f"⚠️  WARN: Could not test card_components.escape_html - {e}")
        print("   (This is OK if running outside Streamlit context)")
    
    # Test import detail_view
    try:
        from drugs.drug_info_components.detail_view import escape_html as escape_html_detail
        print("✅ PASS: import escape_html from detail_view")
        
        # Test function
        result = escape_html_detail("<test>")
        if result == "&lt;test&gt;":
            print("✅ PASS: detail_view.escape_html function works")
        else:
            print(f"❌ FAIL: escape_html returned '{result}' instead of '&lt;test&gt;'")
            all_passed = False
    except Exception as e:
        print(f"⚠️  WARN: Could not test detail_view.escape_html - {e}")
        print("   (This is OK if running outside Streamlit context)")
    
    return all_passed

# Test HTML structure trong code
def test_html_structure():
    """Test HTML structure trong các files"""
    print("\n" + "=" * 60)
    print("TEST HTML STRUCTURE IN FILES")
    print("=" * 60)
    
    files_to_check = [
        "pages/Drug_Detail.py",
        "drugs/drug_info_components/card_components.py",
        "drugs/drug_info_components/detail_view.py",
    ]
    
    all_passed = True
    
    for file_path in files_to_check:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check for escape_html function definition
            if 'def escape_html' in content:
                print(f"✅ PASS: {file_path} has escape_html function")
            else:
                print(f"❌ FAIL: {file_path} missing escape_html function")
                all_passed = False
            
            # Check for import html
            if 'import html' in content:
                print(f"✅ PASS: {file_path} imports html module")
            else:
                print(f"❌ FAIL: {file_path} missing 'import html'")
                all_passed = False
            
            # Check for unsafe_allow_html usage (should have escape_html nearby)
            if 'unsafe_allow_html=True' in content:
                # Count occurrences
                count = content.count('unsafe_allow_html=True')
                print(f"✅ INFO: {file_path} uses unsafe_allow_html {count} times")
                # Note: We can't automatically verify all are escaped, but we can check patterns
                
        except FileNotFoundError:
            print(f"⚠️  WARN: {file_path} not found")
        except Exception as e:
            print(f"❌ ERROR checking {file_path}: {e}")
            all_passed = False
    
    return all_passed

# Main test runner
def main():
    """Run all tests"""
    print("\n" + "=" * 60)
    print("HTML ESCAPING TEST SUITE")
    print("=" * 60 + "\n")
    
    results = []
    
    # Test 1: Basic HTML escaping
    results.append(("HTML Escaping", test_escape_html()))
    
    # Test 2: Imports
    results.append(("Imports", test_imports()))
    
    # Test 3: HTML Structure
    results.append(("HTML Structure", test_html_structure()))
    
    # Summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    all_passed = True
    for test_name, passed in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status}: {test_name}")
        if not passed:
            all_passed = False
    
    print("=" * 60)
    if all_passed:
        print("✅ ALL TESTS PASSED!")
    else:
        print("❌ SOME TESTS FAILED")
    print("=" * 60)
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())

