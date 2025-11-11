#!/usr/bin/env python3
"""
Analyze which taxes from the comprehensive "Steuern von A-Z" list are missing from our current collection
"""

# Current sources we have uploaded (from PDF/HTML files)
current_sources = {
    'alkopopstg': 'Alkopopsteuer',
    'alkstg': 'Alkoholsteuer',
    'ao_1977': 'Abgabenordnung (Tax Code)',
    'bewg': 'Bewertungsgesetz (Assessment Act)',
    'bierstg_2009': 'Biersteuer',
    'energiestg': 'Energiesteuer',
    'erbstg_1974': 'Erbschaftsteuer/Schenkungsteuer',
    'estdv_1955': 'Einkommensteuer-Durchführungsverordnung',
    'estg': 'Einkommensteuer',
    'gewstg': 'Gewerbesteuer',
    'grestg_1983': 'Grunderwerbsteuer',
    'grstg_1973': 'Grundsteuer',
    'kaffeestg_2009': 'Kaffeesteuer',
    'kraftstg': 'Kraftfahrzeugsteuer',
    'kstg_1977': 'Körperschaftsteuer',
    'lstdv': 'Lohnsteuer-Durchführungsverordnung',
    'luftvstg': 'Luftverkehrsteuer',
    'minstg': 'Mindeststeuer',
    'rennwlottg_2021': 'Rennwett- und Lotteriesteuer',
    'schaumwzwstg_2009': 'Schaumweinsteuer',
    'solzg_1995': 'Solidaritätszuschlag',
    'stromstg': 'Stromsteuer',
    'tabstg_2009': 'Tabaksteuer',
    'ustdv_1980': 'Umsatzsteuer-Durchführungsverordnung',
    'ustg_1980': 'Umsatzsteuer',
    'versstg': 'Versicherungsteuer'
}

# Also have the comprehensive reference guide and newly added federal laws
current_sources['steuern-von-a-z'] = 'Steuern von A-Z (Comprehensive Reference)'
current_sources['feuerschstg_1979'] = 'Feuerschutzsteuergesetz (FeuerschStG) 1979'
current_sources['zollvg'] = 'Zollverwaltungsgesetz (ZollVG)'
current_sources['spielbkv'] = 'SpielbkV - Verordnung über öffentliche Spielbanken'

# Complete list from "Steuern von A-Z" with page numbers
complete_tax_list = {
    'Abgeltungsteuer': 29,
    'Abzugsteuern bei beschränkt Steuerpflichtigen': 32,
    'Alkoholsteuer': 34,
    'Alkopopsteuer': 36,
    'Besitz- und Verkehrsteuern': 37,
    'Biersteuer': 38,
    'Einfuhrumsatzsteuer': 40,
    'Einkommensteuer': 42,
    'Energiesteuer': 54,
    'Erbschaftsteuer/Schenkungsteuer': 58,
    'Feuerschutzsteuer': 66,
    'Getränkesteuer': 67,
    'Gewerbesteuer': 68,
    'Grunderwerbsteuer': 70,
    'Grundsteuer': 72,
    'Hundesteuer': 76,
    'Jagd- und Fischereisteuer': 77,
    'Kaffeesteuer': 78,
    'Kapitalertragsteuer': 79,
    'Kirchensteuer': 81,
    'Körperschaftsteuer': 83,
    'Kraftfahrzeugsteuer': 86,
    'Lohnsteuer': 90,
    'Luftverkehrsteuer': 97,
    'Mindeststeuer': 99,
    'Örtliche Steuern': 100,
    'Rennwett- und Lotteriesteuer': 101,
    'Schankerlaubnissteuer': 103,
    'Schaumweinsteuer': 104,
    'Solidaritätszuschlag': 105,
    'Spielbankabgabe': 107,
    'Steuerabzug bei Bauleistungen': 108,
    'Steueridentifikationsnummer': 110,
    'Stromsteuer': 111,
    'Tabaksteuer': 114,
    'Umsatzsteuer': 119,
    'Verbrauchsteuern (besondere)': 127,
    'Vergnügungsteuer': 128,
    'Versicherungsteuer': 129,
    'Zölle': 131,
    'Zweitwohnungsteuer': 134,
    'Zwischenerzeugnissteuer': 135
}

def analyze_coverage():
    """Analyze which taxes are covered and which are missing"""

    # Map our current sources to tax names
    covered_taxes = set()
    for source_key, description in current_sources.items():
        # Extract the main tax name from description
        if 'Alkopopsteuer' in description:
            covered_taxes.add('Alkopopsteuer')
        elif 'Alkoholsteuer' in description:
            covered_taxes.add('Alkoholsteuer')
        elif 'Biersteuer' in description:
            covered_taxes.add('Biersteuer')
        elif 'Energiesteuer' in description:
            covered_taxes.add('Energiesteuer')
        elif 'Erbschaftsteuer' in description:
            covered_taxes.add('Erbschaftsteuer/Schenkungsteuer')
        elif 'Einkommensteuer' in description and 'Durchführungsverordnung' not in description:
            covered_taxes.add('Einkommensteuer')
        elif 'Gewerbesteuer' in description:
            covered_taxes.add('Gewerbesteuer')
        elif 'Grunderwerbsteuer' in description:
            covered_taxes.add('Grunderwerbsteuer')
        elif 'Grundsteuer' in description:
            covered_taxes.add('Grundsteuer')
        elif 'Kaffeesteuer' in description:
            covered_taxes.add('Kaffeesteuer')
        elif 'Körperschaftsteuer' in description:
            covered_taxes.add('Körperschaftsteuer')
        elif 'Kraftfahrzeugsteuer' in description:
            covered_taxes.add('Kraftfahrzeugsteuer')
        elif 'Luftverkehrsteuer' in description:
            covered_taxes.add('Luftverkehrsteuer')
        elif 'Mindeststeuer' in description:
            covered_taxes.add('Mindeststeuer')
        elif 'Rennwett' in description:
            covered_taxes.add('Rennwett- und Lotteriesteuer')
        elif 'Schaumweinsteuer' in description:
            covered_taxes.add('Schaumweinsteuer')
        elif 'Solidaritätszuschlag' in description:
            covered_taxes.add('Solidaritätszuschlag')
        elif 'Stromsteuer' in description:
            covered_taxes.add('Stromsteuer')
        elif 'Tabaksteuer' in description:
            covered_taxes.add('Tabaksteuer')
        elif 'Umsatzsteuer' in description and 'Durchführungsverordnung' not in description:
            covered_taxes.add('Umsatzsteuer')
        elif 'Versicherungsteuer' in description:
            covered_taxes.add('Versicherungsteuer')
        elif 'Feuerschutzsteuergesetz' in description:
            covered_taxes.add('Feuerschutzsteuer')
        elif 'Zollverwaltungsgesetz' in description:
            covered_taxes.add('Zölle')
        elif 'SpielbkV' in description:
            covered_taxes.add('Spielbankabgabe')
        elif 'Steuern von A-Z' in description:
            # This covers many taxes as a reference
            pass

    # Also add Einfuhrumsatzsteuer as it's covered in UStG
    covered_taxes.add('Einfuhrumsatzsteuer')

    # Find missing taxes
    missing_taxes = {}
    for tax_name, page in complete_tax_list.items():
        if tax_name not in covered_taxes:
            missing_taxes[tax_name] = page

    return covered_taxes, missing_taxes

if __name__ == "__main__":
    covered, missing = analyze_coverage()

    print("=== GERMAN TAX LAW COVERAGE ANALYSIS ===")
    print(f"Total taxes in 'Steuern von A-Z': {len(complete_tax_list)}")
    print(f"Taxes covered by current sources: {len(covered)}")
    print(f"Taxes missing: {len(missing)}")
    print()

    print("✅ COVERED TAXES:")
    for tax in sorted(covered):
        print(f"  ✓ {tax}")
    print()

    print("❌ MISSING TAXES:")
    for tax, page in sorted(missing.items(), key=lambda x: x[1]):
        print(f"  ✗ {tax} (Page {page})")
    print()

    print("📊 COVERAGE SUMMARY:")
    coverage_percentage = (len(covered) / len(complete_tax_list)) * 100
    print(".1f")
    print()

    print("📝 ANALYSIS:")
    print("- Most missing taxes are local/state taxes without federal laws")
    print("- Many subtopics (withholding taxes, tax IDs) are covered in major laws like EStG")
    print("- Categories like 'Besitz- und Verkehrsteuern' are not specific laws")
    print("- The comprehensive 'Steuern von A-Z' guide covers all topics as reference")
    print()
    print("🔍 FEDERAL LAWS FOUND FOR MISSING TAXES:")
    print("✅ Feuerschutzsteuer → Feuerschutzsteuergesetz (FeuerschStG) 1979")
    print("✅ Zölle → Zollverwaltungsgesetz (ZollVG)")
    print("✅ Spielbankabgabe → SpielbkV (Verordnung über öffentliche Spielbanken)")
    print()
    print("💡 RECOMMENDATION: Download and add these 3 federal laws to complete the collection")
