# Contributing to Virtual Tax Advisory

Thank you for your interest in contributing to the Virtual Tax Advisory project! We welcome contributions from the community.

## Code of Conduct

This project follows a code of conduct to ensure a welcoming environment for all contributors. Please read our [Code of Conduct](CODE_OF_CONDUCT.md) before participating.

## How to Contribute

### Reporting Issues

- Use GitHub Issues to report bugs or request features
- Provide detailed information including steps to reproduce
- Include relevant system information and error messages
- Use issue templates when available

### Contributing Code

1. **Fork the repository** on GitHub
2. **Create a feature branch** from `main`
3. **Make your changes** following our coding standards
4. **Write tests** for new functionality
5. **Update documentation** as needed
6. **Submit a pull request**

### Pull Request Process

1. Ensure your PR description clearly describes the changes
2. Reference any related issues
3. Ensure all tests pass
4. Update documentation if needed
5. Wait for review and address feedback

## Development Setup

### Prerequisites

- Python 3.6+
- Git
- Open Notebook instance (for full functionality)

### Local Development

```bash
# Clone the repository
git clone https://github.com/FalkoGuderian/virtual-tax-advisory.git
cd virtual-tax-advisory

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r OpenNotebookAPIToolkit/requirements.txt

# Run tests
python -m pytest
```

## Coding Standards

### Python Code

- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Write docstrings for all public functions
- Keep functions small and focused
- Use meaningful variable names

### Commit Messages

- Use clear, descriptive commit messages
- Start with a verb (Add, Fix, Update, etc.)
- Keep the first line under 50 characters
- Add detailed description if needed

Example:
```
Add tax calculation validation

- Add input validation for tax calculation parameters
- Improve error messages for invalid inputs
- Add unit tests for validation functions
```

## Testing

- Write unit tests for all new functionality
- Ensure all tests pass before submitting PR
- Test edge cases and error conditions
- Maintain or improve code coverage

## Documentation

- Update README.md for significant changes
- Add docstrings to new functions
- Update inline comments as needed
- Keep documentation current with code changes

## Legal and Compliance

⚠️ **Important**: This project deals with tax and financial data. Contributors must ensure:

- No sensitive personal data is committed
- Compliance with data protection regulations (GDPR, etc.)
- Proper handling of tax law information
- Clear disclaimers about professional tax advice

## Areas for Contribution

### High Priority
- Bug fixes and stability improvements
- Performance optimizations
- Enhanced error handling

### Medium Priority
- Additional tax law integrations
- UI/UX improvements
- Documentation improvements

### Future Enhancements
- Multi-language support
- Integration with tax filing systems
- Advanced AI features
- Mobile application

## Getting Help

- Check existing issues and documentation first
- Join our community discussions
- Contact maintainers for guidance

## Recognition

Contributors will be recognized in our README and release notes. Thank you for helping make Virtual Tax Advisory better!
