IDS = [
    "F_ROA",
    "F_CFO",
    "F_D_ROA",
    "F_ACC",
    "F_D_LEV",
    "F_D_LIQ",
    "F_EQ_OFFER",
    "F_D_MARGIN",
    "F_D_TURN",
]


# Profitability indicators

# These indicator provide information about a firm's ability to generate earnings from operations.


def roa_score(roa):
    """
    Returns the F-score contribution of the return on assets (roa) indicator.

    roa is defined as the net income before extraordinary items scaled by beginning-of-the-year
    total assets.

    A positive roa is considered a positive signal for a firm's profitability.

    Args:
        roa (float): Return on assets.

    Returns:
        int: Acquired score (1 or 0).
    """
    return 1 if roa > 0.0 else 0


def cfo_score(cfo):
    """
    Returns the F-score contribution of the cash-flow from operations (cfo) indicator.

    cfo is defined as the cash flow from operations items scaled by beginning-of-the-year
    total assets.

    A positive cfo is considered a positive signal for a firm's profitability.

    Args:
        cfo (float): Cash-flow from operations.

    Returns:
        int: Acquired score (1 or 0).
    """
    return 1 if cfo > 0.0 else 0


def delta_roa_score(delta_roa):
    """
    Returns the F-score contribution of the change in return on assets (delta_roa) indicator.

    delta_roa is defined as the current year's roa less the previous year's roa.

    A increase in roa, i.e. a positive delta_roa, is considered a positive signal for a firm's
    profitability.

    Args:
        delta_roa (float): Change in return on assets.

    Returns:
        int: Acquired score (1 or 0).
    """
    return 1 if delta_roa > 0.0 else 0


def accrual_score(accrual):
    """
    Returns the F-score contribution of the accrual indicator.

    Accrual is defined as the current year's net income before extraordinary items less cash-flow
    from operations, scaled by beginng-of-the-year assets. So, `accrual = roa - cfo`.

    A positive accrual is considered a bad signal about a firm's future profitability and returns
    (Sloan,1996).

    Args:
        accrual (float): Accrual value.

    Returns:
        int: Acquired score (1 or 0).
    """
    return 1 if accrual < 0.0 else 0


# Capital structure indicators

# These indicators provide information about a firm's changes in capital structure and its ability
# to meet future debt service obligations.


def delta_leverage_score(delta_leverage):
    """
    Returns the F-score contribution of the delta_leverage indicator.

    delta_leverage is the measure of how the long-term debt levels of a firm changes. It is defined
    as the change in the ratio between long-term debt and average total assets.

    For a distressed firm, raising external debt signals an inability to generate funds internally.
    So, a positive delta_leverage is considered a bad signal for the firm.

    Args:
        delta_leverage (float): Change in the debt-to-assets ratio.

    Returns:
        int: Acquired score (1 or 0).
    """
    return 1 if delta_leverage < 0.0 else 0


def delta_liquidity_score(delta_current_ratio):
    """
    Returns the F-score contribution of the delta_current_ratio (a.k.a. delta_liquid) indicator.

    delta_current_ratio captures the change in a firm's current ratio between the current year
    and the previous year.

    Current ratio is defined as the ratio of a firm's current assets to its current liabilities.

    An increase of the current ratio, i.e. a positive delta_current_ratio, constitutes an
    improvement in liquidity and a positive signal about a firm's ability to meet short-term
    obligations.

    Args:
        delta_current_ratio (float): Change in the current ratio.

    Returns:
        int: Acquired score (1 or 0).
    """
    return 1 if delta_current_ratio > 0.0 else 0


def eq_offer_score(eq_offer):
    """
    Returns the F-score contribution of the eq_offer indicator.

    The boolean eq_offer is a variable capturing if a firm issued common
    equity in the year until portfolio formation.

    For a distressed firm, just like raising long-term debt, raising external capital from
    investors signals an inability to generate funds internally. So, eq_offer == True is considered
    a bad signal for the firm.

    Args:
        eq_offer (bool): Boolean indicating if common equity was offered.

    Returns:
        int: Acquired score (1 or 0).
    """
    return 1 if eq_offer else 0


# Efficiency indicators

# These indicators measure the changes in the efficiency of a firm's operations.


def delta_margin_score(delta_margin):
    """
    Returns the F-score contribution of the delta_margin indicator.

    delta_margin is defined as the current year's gross margin ratio (gross margin scaled by
    beginning-of-the-year total assets) less the previous year's gross margin ratio. An increase of
    the gross margin ratio, i.e. a positive delta_margin, represents an increase of efficiency of a
    firm's operations, hence considered a good signal.

    Args:
        delta_margin (bool): Change in the gross margin ratio.

    Returns:
        int: Acquired score (1 or 0).
    """
    return 1 if delta_margin > 0.0 else 0


def delta_turnover_score(delta_turnover):
    """
    Returns the F-score contribution of the delta_turnover indicator.

    delta_turnover is defined as the current year's asset turnover (total sales scaled by
    beginning-of-the-year total assets) less the previous year's asset turnover. An increase of
    the asset turnover, i.e. a positive delta_turnover, represents an improvement of productivity
    from a firm's asset base, hence considered a good signal.

    Args:
        delta_turnover (bool): Change in the gross margin ratio.

    Returns:
        int: Acquired score (1 or 0).
    """
    return 1 if delta_turnover > 0.0 else 0
