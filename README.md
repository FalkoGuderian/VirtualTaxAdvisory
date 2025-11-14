# Virtual Tax Advisory with Open Notebook

[![Open Notebook](https://img.shields.io/badge/Open%20Notebook-Knowledge%20Base-blue)](https://github.com/lfnovo/open-notebook)
[![Python](https://img.shields.io/badge/Python-3.6+-green)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

An AI-supported virtual tax advisory for creating income tax declarations for Germany using Open Notebook as a knowledge base for German tax laws.

## ⚠️ Important Disclaimer

**This is not legal advice and should not be used as such.** This project is for informational and educational purposes only. It does not replace professional consultation with a certified tax advisor or lawyer. Always consult qualified professionals for your specific tax situation. We assume no liability for the accuracy of tax calculations, declarations, or any consequences arising from the use of this information.

## 📋 Overview

This project demonstrates how Open Notebook can be used as an AI-supported knowledge base for creating tax declarations. Based on uploaded tax laws, questions about calculations can be asked and complete tax declarations can be created.

<img width="1371" height="708" alt="image" src="https://github.com/user-attachments/assets/bc2b1a79-1065-4774-96d0-d32f7c77ce78" />

### ✨ Main Features

- **Intelligent Question Answering**: Ask and validate questions about tax laws
- **Automatic Calculations**: Calculate tax burden based on current laws
- **Documentation**: Generate complete tax declarations
- **Legal Compliance**: Based on official German tax laws

## 🏗️ Architecture

The Virtual Tax Advisory system is built around Open Notebook as its core knowledge base for German tax laws. The architecture consists of the following components:

- **Open Notebook**: Serves as the AI-powered knowledge base containing uploaded German tax laws
- **API Toolkit**: Python scripts that interface with the Open Notebook API for querying tax information
- **Data Ingestion**: Scripts for downloading and processing German tax laws into the knowledge base
- **Tax Calculation Engine**: Logic for performing tax calculations based on retrieved information
- **Documentation Generation**: Tools for creating complete tax declarations

The system follows a client-server architecture where the local Open Notebook instance provides the backend knowledge service, and Python scripts act as clients for querying and processing tax-related information.

## 📖 Key Documentation Files

This project includes detailed guides for working with German tax laws and creating tax declarations:

### Tax Declaration Process
**[Create_Tax_Declaration_OpenNotebook.md](Create_Tax_Declaration_OpenNotebook.md)** provides a comprehensive step-by-step guide for:
- Collecting personal tax data (income, marital status, deductions)
- Asking targeted questions to Open Notebook about tax laws
- Performing tax calculations based on retrieved information
- Creating complete income tax declarations with examples

The guide includes troubleshooting tips for common API issues and references to official German tax sources.

### Tax Laws Ingestion
**[Injest_German_Tax_Laws_OpenNotebook.md](Injest_German_Tax_Laws_OpenNotebook.md)** details the collection and upload process of German tax laws to Open Notebook:
- **Coverage**: 31 documents covering 25 out of 42 tax types (59.5% coverage)
- **Major Laws**: Includes EStG, KStG, UStG, GewStG, and other federal tax laws
- **Consumption Taxes**: Complete coverage of alcohol, beer, tobacco, energy, and other consumption taxes
- **AI Features**: Automatic summarization and analysis for all sources
- **TaxAgent Notebook**: Dedicated research environment with your notebook ID

This guide serves as the foundation for accurate tax research and AI-powered legal analysis.

## 📋 Prerequisites

### System Requirements
- **Python 3.6+**
- **Open Notebook Instance** (local on `http://localhost:8502`)
- **German Tax Laws** (already uploaded)
- **OpenNotebookAPIToolkit**: The repository `https://github.com/FalkoGuderian/OpenNotebookAPIToolkit` is currently private and will be provided on request. Clone it with `git clone https://github.com/FalkoGuderian/OpenNotebookAPIToolkit.git` once access is granted.

### Required Laws
- Income Tax Act (EStG)
- Solidarity Surcharge Act (SolzG)
- Fiscal Code (AO)
- Income Tax Implementation Ordinance (EStDV)

## 🚀 Quick Start

### 1. Start Open Notebook
```bash
# Start local instance (see OpenNotebookAPIToolkit/README.md)
# Typically available at: http://localhost:8502
```
### 2. Determine Notebook ID
```bash
# List current notebooks
python OpenNotebookAPIToolkit/scripts/check_notebook.py http://localhost:8502
```

### 3. Ask First Question
```bash
# Check basic tax-free amount
python OpenNotebookAPIToolkit/scripts/ask_notebook.py http://localhost:8502 notebook:<your-notebook-id> \
  "What is the basic tax-free amount for income tax in Germany 2024?" --simple
```

## 📖 Usage

### Collect Personal Data

Collect all relevant tax data:
- **Marital Status** (single, married, children)
- **Income** (gross, self-employed/freelance)
- **Deductions** (business expenses, special expenses)
- **Tax Classes**
- **Residence and Workplace**

### Ask Tax-Relevant Questions

#### Basic Tax Questions
```bash
# Basic tax-free amount
python OpenNotebookAPIToolkit/scripts/ask_notebook.py http://localhost:8502 notebook:<your-notebook-id> \
  "What is the basic tax-free amount for income tax in Germany 2024?" --simple

# Child tax credit vs. child benefit
python OpenNotebookAPIToolkit/scripts/ask_notebook.py http://localhost:8502 notebook:<your-notebook-id> \
  "What is the child tax credit for the tax year 2024 in Germany?" --simple

python OpenNotebookAPIToolkit/scripts/ask_notebook.py http://localhost:8502 notebook:<your-notebook-id> \
  "What is the child benefit for 2024 in Germany?" --simple
```

#### Business Expenses and Deductions
```bash
# Commuter allowance
python OpenNotebookAPIToolkit/scripts/ask_notebook.py http://localhost:8502 notebook:<your-notebook-id> \
  "What is the commuter allowance?" --simple

# Home office
python OpenNotebookAPIToolkit/scripts/ask_notebook.py http://localhost:8502 notebook:<your-notebook-id> \
  "What requirements apply for deducting home office costs?" --simple

# Special expenses
python OpenNotebookAPIToolkit/scripts/ask_notebook.py http://localhost:8502 notebook:<your-notebook-id> \
  "Which special expenses are tax deductible?" --simple
```

#### Special Cases
```bash
# Extraordinary burdens
python OpenNotebookAPIToolkit/scripts/ask_notebook.py http://localhost:8502 notebook:<your-notebook-id> \
  "What counts as an extraordinary burden?" --simple

# Household-related services
python OpenNotebookAPIToolkit/scripts/ask_notebook.py http://localhost:8502 notebook:<your-notebook-id> \
  "What is the tax bonus for handicraft services?" --simple
```

### Perform Tax Calculation

Based on the answers:

1. **Determine Income**: Gross minus business expenses
2. **Calculate Taxable Income**: Consider deductions
3. **Apply Tax Rate**: Basic rate or splitting for married couples
4. **Calculate Solidarity Surcharge**: 5.5% of income tax

### Create Tax Declaration

Use the collected data to create a complete tax declaration (see `Result_Steuererklaerung_2024.md` as an example).

## 📊 Example Scenario

### Input Data
- **Family**: Married, 2 children (under 6 years old)
- **Husband**: Employee, [REDACTED] € gross, tax class 3, commuter [REDACTED] km
- **Wife**: Freelancer, [REDACTED] € profit, tax class 5
- **Deductions**: Home office, childcare costs, social security contributions

### Calculation Result
- **Taxable Income**: [REDACTED] €
- **Income Tax**: [REDACTED] €
- **Solidarity Surcharge**: [REDACTED] €
- **Total Tax**: [REDACTED] €
- **Refund**: [REDACTED] €

## 🛠️ API Reference

### ask_notebook.py Parameters

| Parameter | Description | Example |
|-----------|-------------|----------|
| `url` | Open Notebook URL | `http://localhost:8502` |
| `notebook_id` | Notebook ID | `notebook:<your-notebook-id>` |
| `question` | Question to the knowledge base | `"What is the basic tax-free amount?"` |
| `--simple` | Simple answer (not streaming) | |
| `--no-save-note` | Do not save answer as note | |

### Frequently Asked Questions

#### What is the difference between child tax credit and child benefit?
- **Child Tax Credit**: Tax advantage directly in the tax declaration
- **Child Benefit**: Separate monthly transfer from the state
- **Choice**: Choose the more favorable option

#### How is the commuter allowance calculated?
- **Distance**: Kilometers between home and workplace
- **Allowance**: 0.30 € per kilometer (from 21 km)
- **Days**: Number of trips per year

## 🔧 Troubleshooting

### API Error 422 (Unprocessable Entity)
**Cause**: Missing model parameters
**Solution**: Use corrected scripts with default models

### API Error 500 (Internal Server Error)
**Cause**: Complex questions or missing embeddings
**Solution**:
- Ask simpler questions
- Wait until embeddings are ready
- Restart notebook

### Notebook not available
**Cause**: Open Notebook server not started
**Solution**: Start local instance (see OpenNotebookAPIToolkit/README.md)

### Inaccuracies in answers
**Cause**: Missing or outdated laws
**Solution**:
- Upload additional laws
- Formulate questions more specifically
- Check multiple sources

## 📁 Project Structure

```
VirtualTaxAdvisory/
├── .gitignore                  # Git ignore file
├── CHANGELOG.md                # Project changelog
├── CITATION.cff                # Citation file
├── CODE_OF_CONDUCT.md          # Code of conduct
├── CONTRIBUTING.md             # Contributing guidelines
├── Create_Tax_Declaration_OpenNotebook.md  # Tax declaration guide
├── Injest_German_Tax_Laws_OpenNotebook.md   # Tax law ingestion guide
├── LICENSE                     # Project license
├── README.md                   # This file
├── SECURITY.md                 # Security policy
├── docs/                       # Additional documentation (gitignored)
├── json/                       # JSON data files (gitignored)
├── laws/                       # German tax laws (gitignored)
├── results/                    # Generated results (gitignored)
└── scripts/                    # Automation scripts
    ├── analyze_missing_taxes.py
    ├── collect_all_insights.py
    ├── download_laws.py
    ├── download_missing_laws.py
    └── extract_pdf_text.py
```

### Git Ignore

The following directories are excluded from version control via `.gitignore`:
- `docs/` - Additional documentation files
- `json/` - JSON data files
- `laws/` - German tax law files (HTML/PDF)
- `results/` - Generated result files

These directories contain large files or generated content that should not be committed to the repository.

## 📚 Sources and References

### Official Sources
- **ELSTER**: Electronic tax declaration
  - https://www.elster.de/
- **Federal Ministry of Finance**: Tax laws
  - https://www.bundesfinanzministerium.de/
- **Finanztip**: Tax advisor
  - https://www.finanztip.de/steuererklaerung/

### Laws and Ordinances
- Income Tax Act (EStG)
- Solidarity Surcharge Act (SolzG)
- Fiscal Code (AO)
- Income Tax Implementation Ordinance (EStDV)

## 🚀 Advanced Use Cases

### Batch Processing
```bash
# Process multiple questions from file
python OpenNotebookAPIToolkit/scripts/ask_notebook.py http://localhost:8502 notebook:<your-notebook-id> \
  --batch-file tax_questions.txt
```

### Automated Workflows
- Integration with ELSTER interface
- Upload more laws (UStG, GewStG)
- Batch questions for complex cases

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create feature branch
3. Commit changes
4. Create pull request

### Improvement Opportunities
- Implement automated tax calculation
- Integrate more tax laws
- Develop ELSTER interface
- Add multilingual support

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## 📞 Support

For questions or problems:
1. Check the [troubleshooting](#-troubleshooting)
2. Consult the [Open Notebook documentation](OpenNotebookAPIToolkit/README.md)
3. Create an [issue](<your-repo-url>/issues) in the repository

---

**Note**: Ensure that all laws used are up to date. Tax laws change annually.
