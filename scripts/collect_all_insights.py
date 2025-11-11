#!/usr/bin/env python3
"""
Collect all insights from sources in the TaxAgent notebook
"""

import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_sources_for_notebook(base_url, notebook_id):
    """Get all sources for a specific notebook"""
    url = f"{base_url}/api/sources?notebook_id={notebook_id}"

    try:
        response = requests.get(url, verify=False)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"❌ Failed to get sources: HTTP {response.status_code}")
            return []
    except Exception as e:
        print(f"❌ Error getting sources: {e}")
        return []

def get_source_insights(base_url, source_id):
    """Get all insights for a source"""
    url = f"{base_url}/api/sources/{source_id}/insights"

    try:
        response = requests.get(url, verify=False)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"❌ Failed to get insights for {source_id}: HTTP {response.status_code}")
            return []
    except Exception as e:
        print(f"❌ Error getting insights for {source_id}: {e}")
        return []

def main():
    base_url = "http://localhost:8502"
    notebook_id = "notebook:vyeb7xi6hpixkfqnekdf"

    print(f"Collecting insights from all sources in notebook: {notebook_id}")

    # Get all sources for the notebook
    sources = get_sources_for_notebook(base_url, notebook_id)
    if not sources:
        print("No sources found for the notebook")
        return

    print(f"Found {len(sources)} sources")

    # Collect all insights
    all_insights = []

    for source in sources:
        source_id = source['id']
        title = source.get('title', 'Unknown')

        insights = get_source_insights(base_url, source_id)

        for insight in insights:
            all_insights.append({
                'source_id': source_id,
                'source_title': title,
                'insight_type': insight.get('insight_type', ''),
                'content': insight.get('content', ''),
                'created': insight.get('created', '')
            })

    print(f"Collected {len(all_insights)} insights total")

    # Save to JSON file for processing
    with open('tax_laws_insights.json', 'w', encoding='utf-8') as f:
        json.dump(all_insights, f, ensure_ascii=False, indent=2)

    print("Saved insights to tax_laws_insights.json")

    # Print summary
    insight_types = {}
    for insight in all_insights:
        itype = insight['insight_type']
        insight_types[itype] = insight_types.get(itype, 0) + 1

    print("\nInsight types summary:")
    for itype, count in insight_types.items():
        print(f"  {itype}: {count}")

if __name__ == '__main__':
    main()
