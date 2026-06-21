import os
import re
import sys

def test_section_redirects():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    
    # Path to main index.html
    index_path = os.path.join(repo_root, 'index.html')
    if not os.path.exists(index_path):
        print(f"Error: Could not locate index.html at {index_path}")
        sys.exit(1)

    with open(index_path, 'r', encoding='utf-8') as f:
        index_content = f.read()

    sections = ['publications', 'news', 'misc']
    errors = []

    for section in sections:
        # 1. Verify index.html has the section ID anchor
        if f'id="{section}"' not in index_content and f"id='{section}'" not in index_content:
            errors.append(f"index.html is missing an anchor element with id='{section}'")

        # 2. Verify redirect index.html exists in the section directory
        redirect_dir = os.path.join(repo_root, section)
        redirect_file = os.path.join(redirect_dir, 'index.html')
        
        if not os.path.exists(redirect_file):
            errors.append(f"Missing redirect directory or file: {section}/index.html")
            continue

        with open(redirect_file, 'r', encoding='utf-8') as f:
            redirect_content = f.read()

        # 3. Verify it contains redirects to ../#{section}
        expected_anchor = f'../#{section}'
        if expected_anchor not in redirect_content:
            errors.append(f"{section}/index.html does not redirect to the correct relative path '{expected_anchor}'")

        # Basic check for meta refresh and JavaScript location replace
        if 'http-equiv="refresh"' not in redirect_content and "http-equiv='refresh'" not in redirect_content:
            errors.append(f"{section}/index.html is missing the meta http-equiv refresh redirect")

        if 'window.location.replace' not in redirect_content:
            errors.append(f"{section}/index.html is missing the window.location.replace JavaScript redirect")

    if errors:
        print("Unit Test Failed! Redirect validation errors found:")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)

    print(f"Unit Test Passed! Verified relative redirects for all {len(sections)} sections: {sections}")
    sys.exit(0)

if __name__ == '__main__':
    test_section_redirects()
