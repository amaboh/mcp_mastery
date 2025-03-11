"""
Configuration settings for the Investment Analyst Agent.
"""

import os
from pathlib import Path
from typing import Dict, Any, Optional

import dotenv

# Load environment variables from .env file
dotenv.load_dotenv()

# Base paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
REPORTS_DIR = BASE_DIR / "reports"

# Ensure directories exist
DATA_DIR.mkdir(exist_ok=True)
REPORTS_DIR.mkdir(exist_ok=True)

# API Keys
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
FINANCIAL_MODELING_PREP_API_KEY = os.getenv("FINANCIAL_MODELING_PREP_API_KEY")

# Application settings
NUM_STOCKS = int(os.getenv("NUM_STOCKS", "10"))
MARKET_SCOPE = os.getenv("MARKET_SCOPE", "us")
MIN_MARKET_CAP = float(os.getenv("MIN_MARKET_CAP", "100"))  # in millions
STOCK_EXCHANGE = os.getenv("STOCK_EXCHANGE", "ALL")

# Financial API endpoints
API_ENDPOINTS = {
    "alpha_vantage_base": "https://www.alphavantage.co/query",
    "fmp_base": "https://financialmodelingprep.com/api/v3",
}

# Analysis weights configuration
ANALYSIS_WEIGHTS = {
    "financial_health": {
        "weight": 0.30,
        "components": {
            "liquidity": {
                "weight": 0.10,
                "metrics": {
                    "current_ratio": 0.05,
                    "quick_ratio": 0.05,
                }
            },
            "solvency": {
                "weight": 0.10,
                "metrics": {
                    "debt_to_equity": 0.05,
                    "interest_coverage": 0.05,
                }
            },
            "profitability": {
                "weight": 0.10,
                "metrics": {
                    "net_margin": 0.03,
                    "return_on_equity": 0.04,
                    "return_on_assets": 0.03,
                }
            }
        }
    },
    "growth_metrics": {
        "weight": 0.25,
        "components": {
            "revenue_growth": {
                "weight": 0.10,
                "metrics": {
                    "yoy_growth": 0.04,
                    "three_year_cagr": 0.03,
                    "five_year_cagr": 0.03,
                }
            },
            "earnings_growth": {
                "weight": 0.10,
                "metrics": {
                    "yoy_growth": 0.04,
                    "three_year_cagr": 0.03,
                    "five_year_cagr": 0.03,
                }
            },
            "cash_flow_growth": {
                "weight": 0.05,
                "metrics": {
                    "operating_cf_growth": 0.03,
                    "free_cf_growth": 0.02,
                }
            }
        }
    },
    "valuation_metrics": {
        "weight": 0.20,
        "metrics": {
            "pe_ratio": 0.05,
            "ps_ratio": 0.05,
            "pb_ratio": 0.05,
            "ev_ebitda": 0.05,
        }
    },
    "dividend_analysis": {
        "weight": 0.10,
        "metrics": {
            "dividend_yield": 0.04,
            "dividend_growth_rate": 0.03,
            "payout_ratio": 0.03,
        }
    },
    "qualitative_factors": {
        "weight": 0.15,
        "metrics": {
            "management_quality": 0.05,
            "competitive_positioning": 0.05,
            "industry_trends": 0.05,
        }
    }
}

# Investment recommendation thresholds
INVESTMENT_THRESHOLDS = {
    "strong_buy": 0.80,
    "buy": 0.65,
    "hold": 0.45,
    "sell": 0.30,
    "strong_sell": 0.0
}

def get_config() -> Dict[str, Any]:
    """Return the complete configuration as a dictionary."""
    return {
        "api_keys": {
            "anthropic": ANTHROPIC_API_KEY,
            "alpha_vantage": ALPHA_VANTAGE_API_KEY,
            "financial_modeling_prep": FINANCIAL_MODELING_PREP_API_KEY,
        },
        "settings": {
            "num_stocks": NUM_STOCKS,
            "market_scope": MARKET_SCOPE,
            "min_market_cap": MIN_MARKET_CAP,
            "stock_exchange": STOCK_EXCHANGE,
        },
        "api_endpoints": API_ENDPOINTS,
        "analysis_weights": ANALYSIS_WEIGHTS,
        "investment_thresholds": INVESTMENT_THRESHOLDS,
    }

def validate_config() -> bool:
    """
    Validate that the configuration has all required values.
    Returns True if valid, False otherwise.
    """
    # Check required API keys based on which services we're using
    if not ANTHROPIC_API_KEY:
        print("Error: ANTHROPIC_API_KEY not set in .env file")
        return False
        
    # Additional validations can be added here
    
    return True