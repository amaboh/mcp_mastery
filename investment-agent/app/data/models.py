"""
Data models for the Investment Analyst Agent.
Defines the structure for stocks, financial data, and analysis results.
"""

from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Dict, List, Optional, Any, Union


@dataclass
class Stock:
    """Represents a stock with basic information."""
    
    ticker: str
    name: str
    exchange: str
    sector: Optional[str] = None
    industry: Optional[str] = None
    market_cap: Optional[float] = None
    price: Optional[float] = None
    currency: str = "USD"
    daily_change: Optional[float] = None  # Percentage change
    daily_change_value: Optional[float] = None  # Absolute change
    volume: Optional[int] = None
    avg_volume: Optional[int] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    @property
    def is_large_cap(self) -> bool:
        """Return True if the stock is considered large cap (>$10B)."""
        if self.market_cap is None:
            return False
        return self.market_cap > 10000


@dataclass
class FinancialStatement:
    """Base class for financial statements."""
    
    ticker: str
    period: str  # "annual" or "quarterly"
    currency: str
    statement_date: date
    items: Dict[str, float] = field(default_factory=dict)


@dataclass
class BalanceSheet(FinancialStatement):
    """Represents a balance sheet for a company."""
    pass


@dataclass
class IncomeStatement(FinancialStatement):
    """Represents an income statement for a company."""
    pass


@dataclass
class CashFlowStatement(FinancialStatement):
    """Represents a cash flow statement for a company."""
    pass


@dataclass
class FinancialRatios:
    """Collection of financial ratios for a company."""
    
    ticker: str
    date: date
    
    # Liquidity Ratios
    current_ratio: Optional[float] = None
    quick_ratio: Optional[float] = None
    cash_ratio: Optional[float] = None
    
    # Solvency Ratios
    debt_to_equity: Optional[float] = None
    debt_to_assets: Optional[float] = None
    interest_coverage: Optional[float] = None
    
    # Profitability Ratios
    gross_margin: Optional[float] = None
    operating_margin: Optional[float] = None
    net_margin: Optional[float] = None
    return_on_assets: Optional[float] = None
    return_on_equity: Optional[float] = None
    
    # Valuation Ratios
    pe_ratio: Optional[float] = None
    pb_ratio: Optional[float] = None
    ps_ratio: Optional[float] = None
    ev_ebitda: Optional[float] = None
    
    # Efficiency Ratios
    asset_turnover: Optional[float] = None
    inventory_turnover: Optional[float] = None
    receivables_turnover: Optional[float] = None
    
    # Additional Ratios
    payout_ratio: Optional[float] = None
    dividend_yield: Optional[float] = None


@dataclass
class DividendInfo:
    """Information about dividends for a stock."""
    
    ticker: str
    has_dividend: bool
    dividend_yield: Optional[float] = None
    annual_dividend: Optional[float] = None
    payout_ratio: Optional[float] = None
    dividend_history: List[Dict[str, Union[date, float]]] = field(default_factory=list)
    dividend_growth_rates: Dict[str, float] = field(default_factory=dict)  # "1y", "3y", "5y", "10y"


@dataclass
class GrowthMetrics:
    """Growth metrics for a company."""
    
    ticker: str
    
    # Revenue Growth
    revenue_growth_yoy: Optional[float] = None
    revenue_growth_3yr: Optional[float] = None
    revenue_growth_5yr: Optional[float] = None
    
    # Earnings Growth
    earnings_growth_yoy: Optional[float] = None
    earnings_growth_3yr: Optional[float] = None
    earnings_growth_5yr: Optional[float] = None
    
    # Cash Flow Growth
    operating_cf_growth_yoy: Optional[float] = None
    operating_cf_growth_3yr: Optional[float] = None
    free_cf_growth_yoy: Optional[float] = None
    free_cf_growth_3yr: Optional[float] = None


@dataclass
class QualitativeAnalysis:
    """Qualitative analysis for a company."""
    
    ticker: str
    
    # Management Quality (1-10 scale)
    management_quality: Optional[int] = None
    management_notes: Optional[str] = None
    
    # Competitive Position (1-10 scale)
    competitive_position: Optional[int] = None
    competitive_notes: Optional[str] = None
    
    # Industry Analysis
    industry_trend: Optional[str] = None  # "positive", "neutral", "negative"
    industry_notes: Optional[str] = None
    
    # Additional Factors
    swot: Dict[str, List[str]] = field(default_factory=dict)  # strengths, weaknesses, opportunities, threats
    esg_rating: Optional[str] = None
    esg_notes: Optional[str] = None


@dataclass
class ValuationResults:
    """Results from various valuation methods."""
    
    ticker: str
    current_price: float
    valuation_date: date
    
    # DCF Valuation
    dcf_fair_value: Optional[float] = None
    dcf_upside: Optional[float] = None  # percentage
    
    # Ratio-based Valuations
    pe_based_value: Optional[float] = None
    pb_based_value: Optional[float] = None
    ps_based_value: Optional[float] = None
    ev_ebitda_based_value: Optional[float] = None
    
    # Dividend Discount Model
    ddm_value: Optional[float] = None
    
    # Average Fair Value
    average_fair_value: Optional[float] = None
    average_upside: Optional[float] = None  # percentage
    
    # Valuation Rating (1-10 scale)
    valuation_rating: Optional[int] = None


@dataclass
class AnalysisResult:
    """Comprehensive analysis result for a stock."""
    
    stock: Stock
    financial_health_score: float
    growth_score: float
    valuation_score: float
    dividend_score: float
    qualitative_score: float
    overall_score: float
    investment_recommendation: str  # "strong_buy", "buy", "hold", "sell", "strong_sell"
    analysis_summary: str
    strengths: List[str]
    weaknesses: List[str]
    analysis_date: datetime = field(default_factory=datetime.now)
    detailed_metrics: Dict[str, Any] = field(default_factory=dict)
    
    @property
    def formatted_recommendation(self) -> str:
        """Return a formatted version of the investment recommendation."""
        rec_map = {
            "strong_buy": "Strong Buy",
            "buy": "Buy",
            "hold": "Hold",
            "sell": "Sell",
            "strong_sell": "Strong Sell"
        }
        return rec_map.get(self.investment_recommendation, self.investment_recommendation)