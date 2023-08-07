def delta_leverage_score(delta_leverage):
    return 1 if delta_leverage < 0.0 else 0


def delta_liquidity_score(delta_current_ratio):
    return 1 if delta_current_ratio > 0.0 else 0


def eq_offer_score(eq_offer):
    return 1 if eq_offer else 0
