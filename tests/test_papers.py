import os
import re
import sys
import json

def test_papers_links():
    # Resolve papers.js path relative to the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    papers_path = os.path.join(repo_root, 'data', 'papers.js')

    if not os.path.exists(papers_path):
        print(f"Error: Could not locate papers.js at {papers_path}")
        sys.exit(1)

    with open(papers_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Strip variable declaration to extract clean JSON block
    match = re.match(r'^\s*const\s+papersData\s*=\s*(.*?);\s*$', content, re.DOTALL)
    if not match:
        print("Error: Could not extract papersData JSON from data/papers.js")
        sys.exit(1)

    json_str = match.group(1)
    try:
        papers = json.loads(json_str)
    except Exception as e:
        print(f"Error: Failed to parse papers JSON: {e}")
        sys.exit(1)

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
        sys.exit(1)

    print(f"Unit Test Passed! Verified all {len(papers)} papers contain 'arXiv' and 'cite' (bibtex) details.")
    sys.exit(0)

if __name__ == '__main__':
    test_papers_links()
