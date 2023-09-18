#
# Abbreviations for the column names that should be found in the data
#

cols = {
    "IO": "NetIncomeFromContinuingOps_",
    "TA": "TotalAssets_",
    "CO": "NetCashFromOperatingActivities_",
    "CA": "CurrentAssets_",
    "CL": "CurrentLiabilities_",
    "GM": "GrossMargin_",
    "NS": "NetSales_",
    "LD": "LongTermDebt_",
    "SO": "SharesOutstanding_",
}

#
# Some calculation routines used in more than one place in the indicator functions
#


def calculate_roa(data, year):
    return data[cols["IO"] + str(year)] / data[cols["TA"] + str(year - 1)]


def calculate_cfo(data, year):
    return data[cols["CO"] + str(year)] / data[cols["TA"] + str(year - 1)]


def calculate_current_ratio(data, year):
    return data[cols["CA"] + str(year)] / data[cols["CL"] + str(year)]


def calculate_margin_ratio(data, year):
    return data[cols["GM"] + str(year)] / data[cols["TA"] + str(year - 1)]


def calculate_turnover(data, year):
    return data[cols["NS"] + str(year)] / data[cols["TA"] + str(year - 1)]


def calculate_leverage(data, year):
    average_total_assets = 0.5 * (data[cols["TA"] + str(year)] + data[cols["TA"] + str(year - 1)])
    return data[cols["LD"] + str(year)] / average_total_assets


def calculate_shares_outstanding(data, year):
    return data[cols["SO"] + str(year)]


# Profitability indicators
#
# These indicator provide information about a firm's ability to generate earnings from operations.


def roa_score(data, year):
    """
    Returns the F-score contribution of the return on assets (roa) indicator.

    roa is defined as the net income before extraordinary items scaled by beginning-of-the-year
    total assets.

    A positive roa is considered a positive signal for a firm's profitability.

    Args:
        data (Series): Data frame with fundamental information of companies.
        year (int): Year to calculate the indicator.

    Returns:
        list[int]: Acquired score for every firm (1 or 0).
    """
    roas = calculate_roa(data, year)

    return [1 if roa > 0.0 else 0 for roa in roas]


def cfo_score(data, year):
    """
    Returns the F-score contribution of the cash-flow from operations (cfo) indicator.

    cfo is defined as the cash flow from operations items scaled by beginning-of-the-year
    total assets.

    A positive cfo is considered a positive signal for a firm's profitability.

    Args:
        data (Series): Data frame with fundamental information of firms.
        year (int): Year to calculate the indicator.

    Returns:
        list[int]: Acquired score for every firm (1 or 0).
    """
    cfos = calculate_cfo(data, year)

    return [1 if cfo > 0.0 else 0 for cfo in cfos]


def delta_roa_score(data, year):
    """
    Returns the F-score contribution of the change in return on assets (delta_roa) indicator.

    delta_roa is defined as the current year's roa less the previous year's roa.

    A increase in roa, i.e. a positive delta_roa, is considered a positive signal for a firm's
    profitability.

    Args:
        data (Series): Data frame with fundamental information of companies.
        year (int): Year to calculate the indicator.

    Returns:
        list[int]: Acquired score for every firm (1 or 0).
    """
    roas_current = calculate_roa(data, year)
    roas_prev = calculate_roa(data, year - 1)
    delta_roas = roas_current - roas_prev

    return [1 if delta_roa > 0.0 else 0 for delta_roa in delta_roas]


def accrual_score(data, year):
    """
    Returns the F-score contribution of the accrual indicator.

    Accrual is defined as the current year's net income before extraordinary items less cash-flow
    from operations, scaled by beginng-of-the-year assets. So, `accrual = roa - cfo`.

    A positive accrual is considered a bad signal about a firm's future profitability and returns
    (Sloan,1996).

     Args:
        data (Series): Data frame with fundamental information of companies.
        year (int): Year to calculate the indicator.

    Returns:
        list[int]: Acquired score for every firm (1 or 0).
    """
    roas = calculate_roa(data, year)
    cfos = calculate_cfo(data, year)
    accruals = roas - cfos

    return [1 if accrual < 0.0 else 0 for accrual in accruals]


# Capital structure indicators
#
# These indicators provide information about a firm's changes in capital structure and its ability
# to meet future debt service obligations.


def delta_leverage_score(data, year):
    """
    Returns the F-score contribution of the delta_leverage indicator.

    delta_leverage is the measure of how the long-term debt levels of a firm changes. It is defined
    as the change in the ratio between long-term debt and average total assets.

    For a distressed firm, raising external debt signals an inability to generate funds internally.
    So, a positive delta_leverage is considered a bad signal for the firm.

     Args:
        data (Series): Data frame with fundamental information of companies.
        year (int): Year to calculate the indicator.

    Returns:
        list[int]: Acquired score for every firm (1 or 0).
    """
    leverages_current = calculate_leverage(data, year)
    leverages_prev = calculate_leverage(data, year - 1)
    delta_leverages = leverages_current - leverages_prev

    return [1 if delta_leverage < 0.0 else 0 for delta_leverage in delta_leverages]


def delta_liquidity_score(data, year):
    """
    Returns the F-score contribution of the delta_current_ratio (a.k.a. delta_liquid) indicator.

    delta_current_ratio captures the change in a firm's current ratio between the current year
    and the previous year.

    Current ratio is defined as the ratio of a firm's current assets to its current liabilities.

    An increase of the current ratio, i.e. a positive delta_current_ratio, constitutes an
    improvement in liquidity and a positive signal about a firm's ability to meet short-term
    obligations.

     Args:
        data (Series): Data frame with fundamental information of companies.
        year (int): Year to calculate the indicator.

    Returns:
        list[int]: Acquired score for every firm (1 or 0).
    """
    current_ratios_current = calculate_current_ratio(data, year)
    current_ratios_prev = calculate_current_ratio(data, year - 1)
    delta_current_ratios = current_ratios_current - current_ratios_prev

    return [1 if delta_current_ratio > 0.0 else 0 for delta_current_ratio in delta_current_ratios]


def eq_offer_score(data, year):
    """
    Returns the F-score contribution of the eq_offer indicator.

    eq_offer is a variable capturing if a firm issued common equity. It is calculated as the
    difference in the number of shares outstanding of the firm (i.e. delta_shares_outstanding).

    For a distressed firm, just like raising long-term debt, raising external capital from
    investors signals an inability to generate funds internally. So, a positive eq_offer is
    considered a bad signal for the firm.

    Args:
        data (Series): Data frame with fundamental information of companies.
        year (int): Year to calculate the indicator.

    Returns:
        list[int]: Acquired score for every firm (1 or 0).
    """
    shares_outstanding_current = calculate_shares_outstanding(data, year)
    shares_outstanding_prev = calculate_shares_outstanding(data, year - 1)
    eq_offers = shares_outstanding_current - shares_outstanding_prev

    return [0 if eq_offer > 0 else 1 for eq_offer in eq_offers]


# Efficiency indicators
#
# These indicators measure the changes in the efficiency of a firm's operations.


def delta_margin_score(data, year):
    """
    Returns the F-score contribution of the delta_margin indicator.

    delta_margin is defined as the current year's gross margin ratio (gross margin scaled by
    beginning-of-the-year total assets) less the previous year's gross margin ratio. An increase of
    the gross margin ratio, i.e. a positive delta_margin, represents an increase of efficiency of a
    firm's operations, hence considered a good signal.

    Args:
        data (Series): Data frame with fundamental information of companies.
        year (int): Year to calculate the indicator.

    Returns:
        list[int]: Acquired score for every firm (1 or 0).
    """
    margins_current = calculate_margin_ratio(data, year)
    margins_prev = calculate_margin_ratio(data, year - 1)
    delta_margins = margins_current - margins_prev

    return [1 if delta_margin > 0.0 else 0 for delta_margin in delta_margins]


def delta_turnover_score(data, year):
    """
    Returns the F-score contribution of the delta_turnover indicator.

    delta_turnover is defined as the current year's asset turnover (total sales scaled by
    beginning-of-the-year total assets) less the previous year's asset turnover. An increase of
    the asset turnover, i.e. a positive delta_turnover, represents an improvement of productivity
    from a firm's asset base, hence considered a good signal.

    Args:
        data (Series): Data frame with fundamental information of companies.
        year (int): Year to calculate the indicator.

    Returns:
        list[int]: Acquired score for every firm (1 or 0).
    """
    turnovers_current = calculate_turnover(data, year)
    turnovers_prev = calculate_turnover(data, year - 1)
    delta_turnovers = turnovers_current - turnovers_prev

    return [1 if delta_turnover > 0.0 else 0 for delta_turnover in delta_turnovers]
