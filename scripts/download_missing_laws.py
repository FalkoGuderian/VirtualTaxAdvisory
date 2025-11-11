#!/usr/bin/env python3
"""
Download the missing German tax laws found on gesetze-im-internet.de
"""

import requests
import time
from pathlib import Path

def download_law(url, filename):
    """Download a law from gesetze-im-internet.de"""
    try:
        print(f"Downloading {filename} from {url}...")
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        # Handle both text (HTML) and binary (PDF) files
        if filename.endswith('.pdf'):
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f"✅ Successfully downloaded {filename} ({len(response.content)} bytes)")
        else:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(response.text)
            print(f"✅ Successfully downloaded {filename} ({len(response.text)} characters)")

        return True

    except Exception as e:
        print(f"❌ Failed to download {filename}: {e}")
        return False

def main():
    """Download the three missing federal tax laws"""

    laws_to_download = [
        {
            'url': 'https://www.gesetze-im-internet.de/feuerschstg_1979/FeuerschStG.pdf',
            'filename': 'feuerschstg_1979.pdf',
            'name': 'Feuerschutzsteuergesetz (FeuerschStG) 1979'
        },
        {
            'url': 'https://www.gesetze-im-internet.de/zollvg/ZollVG.pdf',
            'filename': 'zollvg.pdf',
            'name': 'Zollverwaltungsgesetz (ZollVG)'
        },
        {
            'url': 'https://www.gesetze-im-internet.de/spielbkv/SpielbkV.pdf',
            'filename': 'spielbkv.pdf',
            'name': 'SpielbkV - Verordnung über öffentliche Spielbanken'
        }
    ]

    print("=== DOWNLOADING MISSING GERMAN TAX LAWS ===")
    print()

    downloaded_files = []

    for law in laws_to_download:
        success = download_law(law['url'], law['filename'])
        if success:
            downloaded_files.append(law['filename'])

        # Be polite and wait between downloads
        time.sleep(2)

    print()
    print("=== DOWNLOAD SUMMARY ===")
    print(f"Successfully downloaded: {len(downloaded_files)}/{len(laws_to_download)} laws")
    print()
    print("Downloaded files:")
    for filename in downloaded_files:
        print(f"  📄 {filename}")

    if downloaded_files:
        print()
        print("Next steps:")
        print("1. Review the downloaded HTML files")
        print("2. Upload them to Open Notebook using the upload_sources.py script")
        print("3. Update the tax coverage analysis")

if __name__ == "__main__":
    main()
