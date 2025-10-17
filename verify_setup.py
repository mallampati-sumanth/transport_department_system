#!/usr/bin/env python3
"""
Verification script to check the Transport Department System setup.
This script verifies that all files are in place and syntax is correct.
"""

import os
import sys
import ast

def check_file(filepath):
    """Check if file exists and has valid Python syntax."""
    if not os.path.exists(filepath):
        print(f"❌ Missing: {filepath}")
        return False
    
    # Check syntax for Python files
    if filepath.endswith('.py'):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                ast.parse(f.read())
            print(f"✅ Valid: {filepath}")
        except SyntaxError as e:
            print(f"❌ Syntax Error in {filepath}: {e}")
            return False
    else:
        print(f"✅ Exists: {filepath}")
    
    return True

def main():
    """Main verification function."""
    print("=" * 60)
    print("Transport Department System - Verification")
    print("=" * 60)
    print()
    
    files_to_check = [
        # Core application files
        'app.py',
        'models.py',
        'config.py',
        'requirements.txt',
        'sample_data.py',
        'init_db.py',
        'setup.sh',
        'verify_setup.py',
        'README.md',
        '.gitignore',
        
        # Documentation
        'docs/API_DOCUMENTATION.md',
        'docs/PRODUCT_BACKLOG.md',
        'docs/SPRINT_PLANNING.md',
        'docs/SCRUM_TEAM.md',
        'docs/SCRUM_CEREMONIES.md',
        'docs/DEVELOPMENT_GUIDE.md',
        'docs/QUICK_START.md',
        
        # Tests
        'tests/__init__.py',
        'tests/test_models.py',
    ]
    
    all_ok = True
    
    print("Checking core files...")
    print("-" * 60)
    for filepath in files_to_check:
        if not check_file(filepath):
            all_ok = False
    
    print()
    print("-" * 60)
    
    if all_ok:
        print("✅ All files present and valid!")
        print()
        print("Project Structure:")
        print("  ✅ Core application modules (app.py, models.py, config.py)")
        print("  ✅ Database models (Vehicle, Driver, Route, License)")
        print("  ✅ Scrum documentation (Product Backlog, Sprint Planning, Team)")
        print("  ✅ API documentation")
        print("  ✅ Development guide")
        print("  ✅ Unit tests")
        print("  ✅ Setup scripts")
        print()
        print("Next Steps:")
        print("  1. Run setup script: ./setup.sh")
        print("  2. Or manually install: pip install -r requirements.txt")
        print("  3. Run the application: python app.py")
        print("  4. Run tests: pytest tests/")
        print()
        print("The Transport Department System is ready for development!")
        return 0
    else:
        print("❌ Some files are missing or have errors")
        print("Please check the errors above and fix them.")
        return 1

if __name__ == '__main__':
    sys.exit(main())
