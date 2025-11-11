# German Tax Law Collection - Open Notebook

This repository contains a comprehensive collection of German tax laws and regulations uploaded to Open Notebook for AI-powered research and analysis.

## 📊 Coverage Overview

### Statistics
- **Total Sources**: 31 documents
- **Tax Types Covered**: 25 out of 42 (59.5% coverage)
- **Major Federal Laws**: ✅ Complete
- **Consumption Taxes**: ✅ Complete
- **Reference Materials**: ✅ Complete
- **AI Summaries**: ✅ Generated for all sources
- **TaxAgent Notebook**: ✅ Organized research environment

### Coverage Breakdown
- **✅ Covered**: 25 tax types
- **❌ Missing**: 17 tax types (mostly local/state taxes or subtopics)
- **🤖 AI Features**: Automatic summarization and analysis available

## 📋 Covered Tax Laws

### Major Federal Tax Laws
| Tax Type | German Name | Law/Regulation | Status |
|----------|-------------|----------------|--------|
| Income Tax | Einkommensteuer | EStG (Einkommensteuergesetz) | ✅ |
| Corporate Tax | Körperschaftsteuer | KStG (Körperschaftsteuergesetz) | ✅ |
| Sales Tax | Umsatzsteuer | UStG (Umsatzsteuergesetz) | ✅ |
| Trade Tax | Gewerbesteuer | GewStG (Gewerbesteuergesetz) | ✅ |
| Property Tax | Grundsteuer | GrStG (Grundsteuergesetz) | ✅ |
| Inheritance Tax | Erbschaftsteuer | ErbStG (Erbschaftsteuergesetz) | ✅ |
| Solidarity Surcharge | Solidaritätszuschlag | SolZG (Solidaritätszuschlagsgesetz) | ✅ |
| Tax Code | Abgabenordnung | AO (Abgabenordnung) | ✅ |

### Consumption Taxes
| Tax Type | German Name | Law/Regulation | Status |
|----------|-------------|----------------|--------|
| Alcohol Tax | Alkoholsteuer | AlkStG (Alkoholsteuergesetz) | ✅ |
| Alcopop Tax | Alkopopsteuer | AlkPopStG (Alkopopsteuergesetz) | ✅ |
| Beer Tax | Biersteuer | BierStG (Biersteuergesetz) | ✅ |
| Coffee Tax | Kaffeesteuer | KaffeeStG (Kaffeesteuergesetz) | ✅ |
| Tobacco Tax | Tabaksteuer | TabStG (Tabaksteuergesetz) | ✅ |
| Energy Tax | Energiesteuer | EnergieStG (Energiesteuergesetz) | ✅ |
| Electricity Tax | Stromsteuer | StromStG (Stromsteuergesetz) | ✅ |
| Sparkling Wine Tax | Schaumweinsteuer | SchaumwZwStG (Schaumweinsteuergesetz) | ✅ |
| Insurance Tax | Versicherungsteuer | VersStG (Versicherungsteuergesetz) | ✅ |

### Special and Transaction Taxes
| Tax Type | German Name | Law/Regulation | Status |
|----------|-------------|----------------|--------|
| Vehicle Tax | Kraftfahrzeugsteuer | KraftStG (Kraftfahrzeugsteuergesetz) | ✅ |
| Air Traffic Tax | Luftverkehrsteuer | LuftVStG (Luftverkehrsteuergesetz) | ✅ |
| Real Estate Transfer Tax | Grunderwerbsteuer | GrEStG (Grunderwerbsteuergesetz) | ✅ |
| Minimum Tax | Mindeststeuer | MinStG (Mindeststeuergesetz) | ✅ |
| Racing/Lottery Tax | Rennwett- und Lotteriesteuer | RennwLottG (Rennwett- und Lotteriesteuergesetz) | ✅ |
| Import Sales Tax | Einfuhrumsatzsteuer | Covered in UStG | ✅ |

### Additional Federal Laws
| Tax Type | German Name | Law/Regulation | Status |
|----------|-------------|----------------|--------|
| Fire Protection Tax | Feuerschutzsteuer | FeuerschStG (Feuerschutzsteuergesetz) | ✅ |
| Customs Duties | Zölle | ZollVG (Zollverwaltungsgesetz) | ✅ |
| Casino Tax | Spielbankabgabe | SpielbkV (Verordnung über öffentliche Spielbanken) | ✅ |

## 📚 Reference Materials

### Comprehensive Guides
- **"Steuern von A-Z"** - Complete alphabetical reference guide covering all German taxes (2025 edition)
- **Assessment Act** - BewG (Bewertungsgesetz) - Property valuation regulations

### Implementation Regulations
- **EStDV** - Einkommensteuer-Durchführungsverordnung (Income Tax Implementation Ordinance)
- **UStDV** - Umsatzsteuer-Durchführungsverordnung (Sales Tax Implementation Ordinance)
- **LStDV** - Lohnsteuer-Durchführungsverordnung (Wage Tax Implementation Ordinance)

## ❌ Missing Tax Types

The following tax types are **not covered** in the current collection:

### Local/State Taxes (No Federal Laws)
- Getränkesteuer (Beverage Tax)
- Hundesteuer (Dog Tax)
- Jagd- und Fischereisteuer (Hunting/Fishing Tax)
- Kirchensteuer (Church Tax)
- Schankerlaubnissteuer (Tavern License Tax)
- Vergnügungsteuer (Entertainment Tax)
- Zweitwohnungsteuer (Second Home Tax)

### Subtopics Covered in Major Laws
These are already covered in the major tax laws:
- Abgeltungsteuer (Withholding Tax) → Covered in EStG
- Kapitalertragsteuer (Capital Gains Tax) → Covered in EStG
- Lohnsteuer (Wage Tax) → Covered in EStG
- Steuerabzug bei Bauleistungen (Construction Withholding) → Covered in EStG/UStG
- Abzugsteuern bei beschränkt Steuerpflichtigen → Covered in AO/EStG

### Categories and Administrative Topics
- Besitz- und Verkehrsteuern (Property/Transaction Taxes) - Category
- Örtliche Steuern (Local Taxes) - Category
- Steueridentifikationsnummer (Tax ID Number) - Administrative
- Verbrauchsteuern (besondere) (Special Consumption Taxes) - Category
- Zwischenerzeugnissteuer (Intermediate Product Tax) - Covered in Schaumweinsteuer

## 🚀 Usage

### TaxAgent Notebook
All tax laws have been organized in a dedicated "TaxAgent" notebook for streamlined research:

- **Notebook ID**: `notebook:<your-notebook-id>`
- **Sources**: 31 German tax law documents
- **AI Summaries**: Automatic simple summaries generated for all sources
- **Comprehensive Overview**: German Markdown overview available (`steuergesetze_uebersicht.md`)

### Open Notebook Integration
All laws are uploaded to Open Notebook and available for:
- AI-powered legal research
- Tax compliance analysis
- Cross-referencing between laws
- Question answering about German tax law
- Automatic summarization and analysis

### Research Workflow
```bash
# Ask questions about German tax law using TaxAgent notebook
python OpenNotebookAPIToolkit/scripts/ask_notebook.py http://localhost:8502 notebook:<your-notebook-id> "What is the German corporate tax rate?" --simple

# Extract research results from TaxAgent notebook
python OpenNotebookAPIToolkit/scripts/extract_notes.py http://localhost:8502 -n notebook:<your-notebook-id>

# Generate AI summaries for all sources
python generate_source_summaries.py

# Collect all insights/summaries
python collect_all_insights.py
```

### Source Management
```bash
# Check available sources
python OpenNotebookAPIToolkit/scripts/check_sources.py http://localhost:8502

# Clear all sources
python OpenNotebookAPIToolkit/scripts/clear_all.py http://localhost:8502

# Add existing sources to TaxAgent notebook
python add_sources_to_notebook.py http://localhost:8502 notebook:<your-notebook-id>
```

### AI-Powered Features
```bash
# Generate simple summaries for all sources
python generate_source_summaries.py

# Collect and analyze all insights
python collect_all_insights.py

# View comprehensive German overview
cat steuergesetze_uebersicht.md
```

## 📖 Source Documents

### File Structure
```
laws/
├── pdf/           # PDF versions of all laws
├── html/          # HTML versions of all laws
├── steuern-von-a-z.pdf    # Comprehensive reference guide
├── feuerschstg_1979.pdf  # Fire protection tax law
├── zollvg.pdf            # Customs administration law
└── spielbkv.pdf          # Casino tax regulation
```

### Document Types
- **Primary Laws**: Federal tax legislation (Gesetze)
- **Regulations**: Implementation ordinances (Verordnungen)
- **Reference**: Comprehensive tax guides and manuals

## 🔍 Research Capabilities

With this collection, Open Notebook can provide:

### AI-Powered Analysis
- **Automatic Summarization**: AI-generated simple summaries for all 31 tax laws
- **Intelligent Question Answering**: Ask complex questions about German tax law
- **Cross-Reference Analysis**: AI-powered connections between related laws
- **Comprehensive Overviews**: Structured German-language summaries

### Tax Law Analysis
- Detailed explanations of German tax regulations
- Cross-references between related laws
- Historical context and amendments
- Regulatory compliance guidance

### Compliance Research
- Tax calculation methodologies
- Filing requirements and deadlines
- Exemption rules and special cases
- Audit preparation support

### Comparative Analysis
- Differences between tax types
- International tax implications
- EU harmonization effects
- Tax optimization strategies

### Practical Applications
- Tax planning strategies
- Legal research assistance
- Educational resources
- Professional consultation support

## 📈 Future Enhancements

Potential additions to complete the collection:
- Local tax laws from major German states (Bundesländer)
- EU tax directives and regulations
- Tax court decisions and precedents
- Updated versions of existing laws

## 📋 Technical Notes

- **Language**: All documents are in German
- **Format**: PDF and HTML versions available
- **Source**: Official German legal database (gesetze-im-internet.de)
- **Updates**: Laws reflect 2024-2025 versions
- **Processing**: All documents are fully indexed and searchable in Open Notebook

## 🤝 Contributing

To add more tax laws to the collection:
1. Research official sources on gesetze-im-internet.de
2. Download PDF versions of federal laws
3. Upload using the Open Notebook toolkit
4. Update this README with coverage changes

---

**Last Updated**: November 2025
**Coverage**: 59.5% of all German tax types
**Sources**: 31 documents
**Status**: Complete for federal tax research
