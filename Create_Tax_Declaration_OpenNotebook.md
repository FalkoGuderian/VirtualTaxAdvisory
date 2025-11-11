# Tax Declaration with Open Notebook

This README describes how to use Open Notebook to create an income tax declaration for Germany. Based on the uploaded tax laws, questions can be asked to validate calculations and create a complete tax declaration.

## Overview

The Open Notebook serves as an AI-supported knowledge base for German tax laws. It enables:
- Asking questions about tax laws
- Validating calculations
- Generating automatic summaries
- Creating tax declarations

## Prerequisites

- **Open Notebook Installation**: Local instance on `http://localhost:8502`
- **Tax Laws**: Uploaded German tax laws (EStG, SolzG, etc.)
- **Python Toolkit**: `OpenNotebookAPIToolkit/scripts/ask_notebook.py`
- **Notebook ID**: `notebook:<your-notebook-id>` (Open Notebook)

## Steps for Tax Declaration

### 1. Upload Laws (already completed)
The relevant tax laws have already been uploaded:
- Income Tax Act (EStG)
- Solidarity Surcharge Act (SolzG)
- Fiscal Code (AO)
- Income Tax Implementation Ordinance (EStDV)

### 2. Collect Personal Data
Collect all necessary data:
- Marital status (married, children)
- Income (gross, self-employed/freelance)
- Deductions (business expenses, special expenses)
- Tax classes
- Residence/workplace

### 3. Ask Questions to Open Notebook

Use the ask_notebook.py script to ask specific questions:

#### Check Basic Tax-Free Amount
```bash
python OpenNotebookAPIToolkit/scripts/ask_notebook.py http://localhost:8502 notebook:<your-notebook-id> "What is the basic tax-free amount for income tax in Germany 2024?" --simple
```

#### Child Tax Credit/Child Benefit
```bash
python OpenNotebookAPIToolkit/scripts/ask_notebook.py http://localhost:8502 notebook:<your-notebook-id> "What is the child tax credit for the tax year 2024 in Germany?" --simple
python OpenNotebookAPIToolkit/scripts/ask_notebook.py http://localhost:8502 notebook:<your-notebook-id> "What is the child benefit for 2024 in Germany?" --simple
```

#### Commuter Allowance
```bash
python OpenNotebookAPIToolkit/scripts/ask_notebook.py http://localhost:8502 notebook:<your-notebook-id> "What is the commuter allowance?" --simple
```

### 4. Perform Tax Calculation

Based on the answers:
- Calculate income (gross minus business expenses)
- Determine taxable income
- Apply tax rate (splitting for married couples)
- Calculate solidarity surcharge

### 5. Create Tax Declaration

Use the collected data to create a complete tax declaration (see `Steuererklaerung_2024.md` as an example).

## Example Session

### Input Data
- **Family**: Married, 2 children (6 years)
- **Husband**: Employee, [REDACTED] € gross, tax class 3, commuter
- **Wife**: Freelancer, [REDACTED] € profit, tax class 5
- **Deductions**: Home office, childcare costs, social security contributions

### Open Notebook Questions
1. Basic tax-free amount: [REDACTED] € (single) / [REDACTED] € (married)
2. Child tax credit: [REDACTED] € per parent per child
3. Child benefit: [REDACTED] €/month per child
4. Commuter allowance: [REDACTED] € (1-20 km) / [REDACTED] € (from 21 km)

### Result
- Taxable income: [REDACTED] €
- Income tax: [REDACTED] €
- Solidarity surcharge: [REDACTED] €
- Total tax: [REDACTED] €
- Refund: [REDACTED] €

## Troubleshooting

### API Error 422
- **Cause**: Missing model parameters
- **Solution**: Use the corrected scripts with default models

### API Error 500
- **Cause**: Complex questions or missing embeddings
- **Solution**: Ask simpler questions or wait until embeddings are ready

### Notebook not available
- **Cause**: Open Notebook server not started
- **Solution**: Start local instance (see OpenNotebookAPIToolkit/README.md)

## Files

- `Steuererklaerung_2024.md`: Example tax declaration
- `Familie_Steuer_2024.md`: Summary of calculations
- `OpenNotebookAPIToolkit/scripts/ask_notebook.py`: Question script (corrected)

## Sources

- German tax laws (gesetze-im-internet.de)
- ELSTER online help
- Finanztip tax advisor
- Open Notebook API documentation

## Next Steps

- Implement automated tax calculation
- Upload more laws (UStG, GewStG)
- Batch questions for complex cases
- Integration with ELSTER interface
