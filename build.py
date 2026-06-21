import json

def build_site():
    # 1. Load the data
    with open('data/papers.json', 'r', encoding='utf-8') as f:
        papers = json.load(f)
    
    # 2. Generate the HTML for the papers
    papers_html = ""
    for paper in papers:
        # print(paper)
        bg_style = 'bgcolor="#ffffd0"' if paper.get('highlight') else ''
        
        # Format the links
        links_html = ' / '.join([f'<a href="{link["url"]}">{link["label"]}</a>' for link in paper.get('links', [])])
        
        # Format the video block if a video exists
        video_html = ""
        if paper.get('videoSrc'):
            video_html = f"""
                <video width="100%" height="100%" muted autoplay loop playsinline>
                  <source src="{paper['videoSrc']}" type="video/mp4">
                </video>
            """
            
        # Format the optional paper_type parameter
        paper_type_html = f" (<i>{paper.get('paperType')}</i>)" if paper.get('paperType') else ""

        # Append the specific paper HTML
        papers_html += f"""
        <tr {bg_style}>
          <td style="padding:16px;width:20%;vertical-align:middle">
            <div class="one paper-preview">
              <div class="two">
                {video_html}
              </div>
              <img src="{paper['imageSrc']}" width="160">
            </div>
          </td>
          <td style="padding:20px;width:75%;vertical-align:middle">
            <a href="{paper['titleUrl']}">
              <span class="papertitle">{paper['title']}</span>
            </a>
            <br>
            {paper['authors']}
            <br>
            <em>{paper['venue']}</em>, {paper['year']}{paper_type_html}
            <br>
            {links_html}
            <p></p>
            <p>{paper['description']}</p>
          </td>
        </tr>
        """

    # 3. Read the template
    with open('template.html', 'r', encoding='utf-8') as f:
        template = f.read()

    # 4. Inject the generated HTML into the template
    final_html = template.replace('{paper-build}', papers_html)

    # 5. Write the final static index.html
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(final_html)
        
    print("Successfully built index.html!")

if __name__ == "__main__":
    build_site()