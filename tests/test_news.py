import os
import re
import sys

def test_news_date_format():
    # Resolve index.html path relative to the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    index_path = os.path.join(repo_root, 'index.html')

    if not os.path.exists(index_path):
        print(f"Error: Could not locate index.html at {index_path}")
        sys.exit(1)

    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Locate the News Section content block
    news_match = re.search(r'<!-- News Section -->.*?<\/details>', content, re.DOTALL)
    if not news_match:
        print("Error: Could not locate '<!-- News Section -->' block in index.html")
        sys.exit(1)

    news_block = news_match.group(0)
    
    # Find all date strings enclosed in <strong>[...]</strong> inside the News block
    dates = re.findall(r'<strong>\[(.*?)\]</strong>', news_block)
    if not dates:
        print("Error: No news dates found in index.html (expected dates in format <strong>[Date]</strong>)")
        sys.exit(1)

    valid_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    pattern = re.compile(r'^([A-Z][a-z]{2}) \d{4}$')

    errors = []
    for date in dates:
        match = pattern.match(date)
        if not match:
            errors.append(f"'{date}' does not match format 'MMM YYYY' (e.g. 'Jun 2026')")
            continue
        
        month = match.group(1)
        if month not in valid_months:
            errors.append(f"'{date}' has an invalid month abbreviation '{month}' (must be one of {valid_months})")

    if errors:
        print("Unit Test Failed! Format violations found:")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)

    print(f"Unit Test Passed! Verified {len(dates)} news dates in 'MMM YYYY' format.")
    sys.exit(0)

if __name__ == '__main__':
    test_news_date_format()
