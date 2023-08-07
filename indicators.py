# Profitability indicators


def roa_score(roa):
    return 1 if roa > 0.0 else 0


def cfo_score(cfo):
    return 1 if cfo > 0.0 else 0


def delta_roa_score(delta_roa):
    return 1 if delta_roa > 0.0 else 0


def accrual_score(accrual):
    return 1 if accrual < 0.0 else 0


# Capital structure indicators


def delta_leverage_score(delta_leverage):
    return 1 if delta_leverage < 0.0 else 0


def delta_liquidity_score(delta_current_ratio):
    return 1 if delta_current_ratio > 0.0 else 0


def eq_offer_score(eq_offer):
    return 1 if eq_offer else 0


# Efficiency indicators


def delta_margin_score(delta_margin):
    return 1 if delta_margin > 0.0 else 0


def delta_turnover_score(delta_turnover):
    return 1 if delta_turnover > 0.0 else 0
