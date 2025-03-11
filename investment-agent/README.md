# Investment Analyst Agent

An intelligent agent that identifies the top 10 worst-performing stocks of the day and performs comprehensive fundamental analysis to provide actionable investment insights.

## Overview

This project implements an investment analysis agent using Anthropic's MCP (Model-Controlled Processes) protocol, integrated with Claude Desktop. The agent automates the daily workflow of identifying underperforming stocks and conducting bottom-up fundamental analysis to determine investment potential.

### Key Features

- Automated retrieval of worst-performing stocks using yfinance
- Comprehensive fundamental analysis including:
  - Financial statement analysis
  - Key financial ratios
  - Dividend analysis
  - Qualitative factors
  - Macroeconomic context
  - Comparative analysis
- Weighted scoring system for investment recommendations
- Detailed reporting and visualization

## Getting Started

### Prerequisites

- Python 3.9+
- API keys for additional data sources (if applicable)
- Claude API access for MCP integration

### Installation

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

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up configuration
```bash
cp .env.template .env
# Edit .env with your API keys and configuration
```

### Usage

Run the main application:

```bash
python -m app.main
```

## Development Roadmap

- [x] Project initialization and setup
- [ ] Data fetching implementation
- [ ] Analysis engine development
- [ ] Reporting and integration
- [ ] Testing and refinement

## Architecture

The application follows a modular architecture:

- **Data Module**: Retrieves market data, financial statements, and other relevant information
- **Analysis Module**: Processes data and applies the weighting system for fundamental analysis
- **Reporting Module**: Generates reports and visualizations
- **MCP Module**: Handles tool calling and prompt chaining for Claude integration

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [yfinance](https://github.com/ranaroussi/yfinance) for market data access
- Anthropic for Claude and MCP capabilities