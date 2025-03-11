# Contributing to Investment Analyst Agent

Thank you for considering contributing to the Investment Analyst Agent! This document provides guidelines and instructions for contributing to this project.

## Code of Conduct

Please be respectful and considerate of others when contributing to this project. We aim to foster an inclusive and collaborative environment.

## How Can I Contribute?

### Reporting Bugs

If you find a bug, please create an issue with the following information:
- A clear, descriptive title
- Steps to reproduce the bug
- Expected behavior
- Actual behavior
- Screenshots if applicable
- Environment details (OS, Python version, etc.)

### Suggesting Enhancements

For feature requests or enhancements:
- Use a clear, descriptive title
- Provide a detailed description of the proposed feature
- Explain why this enhancement would be useful
- Suggest an implementation approach if possible

### Pull Requests

1. Fork the repository
2. Create a new branch from `main` for your feature (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests to ensure your changes don't break existing functionality
5. Commit your changes with clear, descriptive commit messages
6. Push to your branch (`git push origin feature/amazing-feature`)
7. Create a pull request to the `main` branch

## Development Workflow

### Setting Up Development Environment

1. Clone the repository
```bash
git clone https://github.com/yourusername/investment-analyst.git
cd investment-analyst
```

2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install development dependencies
```bash
pip install -r requirements-dev.txt
```

### Code Style

We follow [PEP 8](https://peps.python.org/pep-0008/) style guidelines. Please ensure your code complies with these standards.

- Use 4 spaces for indentation
- Use docstrings for all public functions, classes, and methods
- Keep line length to a maximum of 100 characters

We recommend using tools such as `flake8`, `black`, and `isort` to maintain code quality.

### Testing

- Write unit tests for all new functionality
- Ensure all tests pass before submitting a pull request
- Run tests using pytest:

```bash
pytest
```

### Documentation

- Update documentation for any changes to functionality
- Use clear, concise language
- Include examples where appropriate

## Project Structure

```
investment-analyst/
│
├── app/                           # Main application code
│   ├── data/                      # Data retrieval modules
│   ├── analysis/                  # Analysis modules
│   ├── reporting/                 # Reporting modules
│   └── mcp/                       # MCP integration
│
├── tests/                         # Test suite
└── docs/                          # Documentation
```

## Adding New Features

### Data Sources

When adding a new data source:
1. Create a new module in the `app/data/` directory
2. Implement the required interface
3. Update the configuration to include any necessary API keys
4. Add appropriate error handling and fallback mechanisms

### Analysis Methods

When adding new analysis methods:
1. Create or update modules in the `app/analysis/` directory
2. Update the weighting system in `app/analysis/weights.py` if necessary
3. Ensure the new methods are integrated into the overall analysis flow

## Review Process

Pull requests will be reviewed by the project maintainers. We aim to review pull requests within a week. The review process includes:

- Code review for quality and style
- Testing to ensure functionality
- Documentation review

## Questions?

If you have any questions or need help, please create an issue labeled "question" or contact the maintainers directly.

Thank you for contributing to the Investment Analyst Agent!