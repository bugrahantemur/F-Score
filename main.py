import pandas as pd

import calculators as cal
import indicators as ind

data = pd.read_csv("./data/company_data.csv", index_col=0)
year = 2022

#
# Profitability indicators
#
data["F_ROA"] = [ind.roa_score(roa) for roa in cal.roa(data, year)]
data["F_CFO"] = [ind.cfo_score(cfo) for cfo in cal.cfo(data, year)]
data["F_D_ROA"] = [ind.delta_roa_score(d_roa) for d_roa in cal.delta_roa(data, year)]
data["F_ACC"] = [ind.accrual_score(acc) for acc in cal.accrual(data, year)]
#
# Capital structure indicators
#
data["F_D_LEV"] = [ind.delta_leverage_score(d_lev) for d_lev in cal.delta_leverage(data, year)]
data["F_D_LIQ"] = [ind.delta_liquidity_score(d_liq) for d_liq in cal.delta_liquidity(data, year)]
data["F_EQ_OFFER"] = [ind.eq_offer_score(eq_offer) for eq_offer in cal.eq_offer(data, year)]
#
# Efficiency indicators
#
data["F_D_MARGIN"] = [ind.delta_margin_score(d_margin) for d_margin in cal.delta_margin(data, year)]
data["F_D_TURN"] = [ind.delta_turnover_score(d_turn) for d_turn in cal.delta_turnover(data, year)]


data["F-SCORE"] = data.loc[:, ind.IDS].sum(axis=1)

print(data["F-SCORE"])
