import urllib.request
import os
import re

# List of unique URLs from the markdown file, corrected
urls = [
    "https://www.gesetze-im-internet.de/ao_1977/",
    "https://www.gesetze-im-internet.de/estg/",
    "https://www.gesetze-im-internet.de/alkstg/",
    "https://www.gesetze-im-internet.de/alkopopstg/",
    "https://www.gesetze-im-internet.de/bewg/",
    "https://www.gesetze-im-internet.de/bierstg_2009/",  # corrected
    "https://www.gesetze-im-internet.de/ustg_1980/",
    "https://www.gesetze-im-internet.de/estdv_1955/",  # corrected
    "https://www.gesetze-im-internet.de/energiestg/",
    "https://www.gesetze-im-internet.de/erbstg_1974/",
    "https://www.gesetze-im-internet.de/versstg/",
    # "https://www.gesetze-im-internet.de/kag_nrw/",  # state law, skip
    "https://www.gesetze-im-internet.de/gewstg/",  # corrected
    "https://www.gesetze-im-internet.de/grestg_1983/",
    "https://www.gesetze-im-internet.de/grstg_1973/",
    # "https://www.gesetze-im-internet.de/hundestg/",  # state law, skip
    "https://www.gesetze-im-internet.de/kaffeestg_2009/",  # corrected
    # "https://www.gesetze-im-internet.de/kirchstg_bay/",  # state law, skip
    # "https://www.gesetze-im-internet.de/kirchstg_1993/",  # state law, skip
    "https://www.gesetze-im-internet.de/kstg_1977/",
    "https://www.gesetze-im-internet.de/kraftstg/",
    "https://www.gesetze-im-internet.de/lstdv/",  # corrected
    "https://www.gesetze-im-internet.de/luftvstg/",
    "https://www.gesetze-im-internet.de/minstg/",
    "https://www.gesetze-im-internet.de/rennwlottg_2021/",  # corrected
    "https://www.gesetze-im-internet.de/schaumwzwstg_2009/",  # corrected
    "https://www.gesetze-im-internet.de/solzg_1995/",
    # "https://www.gesetze-im-internet.de/spielbankg_nrw/",  # state law, skip
    "https://www.gesetze-im-internet.de/stromstg/",
    "https://www.gesetze-im-internet.de/tabstg_2009/",
    "https://www.gesetze-im-internet.de/ustdv_1980/",
    # "https://www.gesetze-im-internet.de/vergn_stg/",  # state law, skip
]

# Create directories for downloads
os.makedirs('laws/html', exist_ok=True)
os.makedirs('laws/pdf', exist_ok=True)

for url in urls:
    # Extract the law code, e.g., ao_1977
    law_code = url.rstrip('/').split('/')[-1]
    # HTML URL (the main page)
    html_url = url

    filename_pdf = f"laws/pdf/{law_code}.pdf"
    filename_html = f"laws/html/{law_code}.html"

    # Download HTML first
    html_content = None
    try:
        with urllib.request.urlopen(html_url, timeout=10) as response:
            if response.status == 200:
                html_content = response.read()
                with open(filename_html, 'wb') as f:
                    f.write(html_content)
                print(f"Downloaded HTML: {law_code}")
            else:
                print(f"Failed to download HTML for {law_code}: Status {response.status}")
                continue
    except Exception as e:
        print(f"Failed to download HTML for {law_code}: {e}")
        continue

    # Parse HTML for PDF link
    html_str = html_content.decode('utf-8', errors='ignore')
    pdf_match = re.search(r'href="([^"]*\.pdf)"', html_str)
    if pdf_match:
        pdf_relative = pdf_match.group(1)
        if pdf_relative.startswith('/'):
            pdf_url = f"https://www.gesetze-im-internet.de{pdf_relative}"
        elif pdf_relative.startswith('http'):
            pdf_url = pdf_relative
        else:
            pdf_url = f"{url.rstrip('/')}/{pdf_relative}"
        try:
            with urllib.request.urlopen(pdf_url, timeout=10) as response:
                if response.status == 200:
                    with open(filename_pdf, 'wb') as f:
                        f.write(response.read())
                    print(f"Downloaded PDF: {law_code}")
                else:
                    print(f"Failed to download PDF for {law_code}: Status {response.status}")
        except Exception as e:
            print(f"Failed to download PDF for {law_code}: {e}")
    else:
        print(f"No PDF link found for {law_code}")

print("Download complete.")
