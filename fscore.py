import pandas as pd

import calculators as cal
import indicators as ind


def get_scores(data, year, indicator, calculator):
    return [indicator(value) for value in calculator(data, year)]


def f_score(data, year):
    # Empty data frame with the same indices (companies) as data
    scores = pd.DataFrame(index=data.index)

    # Profitability indicators
    scores["F_ROA"] = get_scores(data, year, ind.roa_score, cal.roa)
    scores["F_CFO"] = get_scores(data, year, ind.cfo_score, cal.cfo)
    scores["F_D_ROA"] = get_scores(data, year, ind.delta_roa_score, cal.delta_roa)
    scores["F_ACC"] = get_scores(data, year, ind.accrual_score, cal.accrual)

    # Capital structure indicators
    scores["F_D_LEV"] = get_scores(data, year, ind.delta_leverage_score, cal.delta_leverage)
    scores["F_D_LIQ"] = get_scores(data, year, ind.delta_liquidity_score, cal.delta_liquidity)
    scores["F_EQ_OFFER"] = get_scores(data, year, ind.eq_offer_score, cal.eq_offer)

    # Efficiency indicators
    scores["F_D_MARGIN"] = get_scores(data, year, ind.delta_margin_score, cal.delta_margin)
    scores["F_D_TURN"] = get_scores(data, year, ind.delta_turnover_score, cal.delta_turnover)

    # Aggregate the scores
    total_score = scores.sum(axis=1)

    return total_score
