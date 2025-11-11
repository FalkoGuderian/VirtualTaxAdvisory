#!/usr/bin/env python3
import PyPDF2
import sys

def extract_pdf_text(pdf_path):
    """Extract text from PDF file"""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)

            print(f"PDF has {len(pdf_reader.pages)} pages")

            # Extract text from all pages
            full_text = ""
            for page_num, page in enumerate(pdf_reader.pages):
                try:
                    page_text = page.extract_text()
                    full_text += f"\n=== PAGE {page_num + 1} ===\n{page_text}\n"
                except Exception as e:
                    print(f"Error extracting page {page_num + 1}: {e}")
                    continue

            return full_text

    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None

if __name__ == "__main__":
    pdf_file = "steuern-von-a-z.pdf"

    print(f"Extracting text from {pdf_file}...")
    text = extract_pdf_text(pdf_file)

    if text:
        print("Text extracted successfully!")
        print(f"Total text length: {len(text)} characters")

        # Look for table of contents or index
        toc_keywords = ["inhaltsverzeichnis", "inhalt", "verzeichnis", "index", "übersicht"]
        lines = text.lower().split('\n')

        print("\n=== LOOKING FOR TABLE OF CONTENTS ===")
        toc_found = False
        for i, line in enumerate(lines):
            if any(keyword in line for keyword in toc_keywords):
                print(f"Found potential TOC at line {i}: {line.strip()}")
                # Print surrounding context
                start = max(0, i-5)
                end = min(len(lines), i+20)
                print("Context:")
                for j in range(start, end):
                    marker = ">>> " if j == i else "    "
                    print(f"{marker}{lines[j]}")
                print("-" * 50)
                toc_found = True

        # Also look for specific tax law abbreviations
        tax_laws = ["estg", "ao", "ustg", "gewstg", "grstg", "erbstg", "kfstg", "solzg", "bewg", "einkommensteuer", "umsatzsteuer", "gewerbesteuer", "grundsteuer", "erbschaftsteuer", "kirchensteuer", "solidaritätszuschlag"]

        print("\n=== TAX LAWS MENTIONED IN THE DOCUMENT ===")
        found_laws = set()
        for line in lines:
            line_lower = line.lower()
            for law in tax_laws:
                if law in line_lower:
                    found_laws.add(law)

        if found_laws:
            print("Found tax laws:")
            for law in sorted(found_laws):
                print(f"  - {law}")
        else:
            print("No specific tax laws found in automated search")

        # Print first few pages to see structure
        print("\n=== FIRST 2000 CHARACTERS ===")
        print(text[:2000])
        print("\n... (truncated)")

    else:
        print("Failed to extract text from PDF")
