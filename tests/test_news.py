import os
import re
import sys
import json

def test_news_date_format():
    # Resolve index.html path relative to the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    index_path = os.path.join(repo_root, 'index.html')

    if not os.path.exists(index_path):
        print(f"Error: Could not locate index.html at {index_path}")
        return False

    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Locate the News Section content block
    news_match = re.search(r'<!-- News Section -->.*?<\/details>', content, re.DOTALL)
    if not news_match:
        print("Error: Could not locate '<!-- News Section -->' block in index.html")
        return False

    news_block = news_match.group(0)
    
    # Find all date strings enclosed in <strong>[...]</strong> inside the News block
    dates = re.findall(r'<strong>\[(.*?)\]</strong>', news_block)
    if not dates:
        print("Error: No news dates found in index.html (expected dates in format <strong>[Date]</strong>)")
        return False

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
        print("Unit Test Failed! News date format violations found:")
        for err in errors:
            print(f"  - {err}")
        return False

    print(f"Unit Test Passed! Verified {len(dates)} news dates in 'MMM YYYY' format.")
    return True


def test_papers_links():
    # Resolve papers.js path relative to the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    papers_path = os.path.join(repo_root, 'data', 'papers.js')

    if not os.path.exists(papers_path):
        print(f"Error: Could not locate papers.js at {papers_path}")
        return False

    with open(papers_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Strip variable declaration to extract clean JSON block
    match = re.match(r'^\s*const\s+papersData\s*=\s*(.*?);\s*$', content, re.DOTALL)
    if not match:
        print("Error: Could not extract papersData JSON from data/papers.js")
        return False

    json_str = match.group(1)
    try:
        papers = json.loads(json_str)
    except Exception as e:
        print(f"Error: Failed to parse papers JSON: {e}")
        return False

    errors = []
    for paper in papers:
        title = paper.get('title', 'Unknown Title')
        
        # 1. Verify it has an arXiv link in the links array
        links = paper.get('links', [])
        has_arxiv = any(link.get('label') == 'arXiv' for link in links)
        if not has_arxiv:
            errors.append(f"Paper '{title}' is missing an 'arXiv' link.")
            
        # 2. Verify it has a bibtex string (which generates the 'cite' link)
        has_cite = bool(paper.get('bibtex'))
        if not has_cite:
            errors.append(f"Paper '{title}' is missing a 'bibtex' string (required for the 'cite' toggle).")

    if errors:
        print("Unit Test Failed! Papers validation errors found:")
        for err in errors:
            print(f"  - {err}")
        return False

    print(f"Unit Test Passed! Verified all {len(papers)} papers contain 'arXiv' and 'cite' (bibtex) details.")
    return True


if __name__ == '__main__':
    print("Running website validation test suite...")
    
    news_ok = test_news_date_format()
    papers_ok = test_papers_links()
    
    if not (news_ok and papers_ok):
        print("\nOverall Status: FAILED")
        sys.exit(1)
        
    print("\nOverall Status: PASSED")
    sys.exit(0)
