import pandas as pd

import indicators as ind


def f_score(data, year):
    # Empty data frame with the same indices (firms) as data
    scores = pd.DataFrame(index=data.index)

    # Profitability indicators
    scores["F_ROA"] = ind.roa_score(data, year)
    scores["F_CFO"] = ind.cfo_score(data, year)
    scores["F_D_ROA"] = ind.delta_roa_score(data, year)
    scores["F_ACC"] = ind.accrual_score(data, year)

    # Capital structure indicators
    scores["F_D_LEV"] = ind.delta_leverage_score(data, year)
    scores["F_D_LIQ"] = ind.delta_liquidity_score(data, year)
    scores["F_EQ_OFFER"] = ind.eq_offer_score(data, year)

    # Efficiency indicators
    scores["F_D_MARGIN"] = ind.delta_margin_score(data, year)
    scores["F_D_TURN"] = ind.delta_turnover_score(data, year)

    # Aggregate the scores
    total_score = scores.sum(axis=1)

    return total_score
