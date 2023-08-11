import json

import calculators
import indicators

with open("./data/company_data.json") as file:
    data = json.load(file)

    for company in data:
        company_data = data[company]
        year = 2022

        scores = [
            #
            # Profitability indicators
            #
            indicators.roa_score(calculators.roa(company_data, year)),
            indicators.cfo_score(calculators.cfo(company_data, year)),
            indicators.delta_roa_score(calculators.delta_roa(company_data, year)),
            indicators.accrual_score(calculators.accrual(company_data, year)),
            #
            # Capital structure indicators
            #
            indicators.delta_leverage_score(calculators.delta_leverage(company_data, year)),
            indicators.delta_liquidity_score(calculators.delta_liquidity(company_data, year)),
            indicators.eq_offer_score(calculators.eq_offer(company_data, year)),
            #
            # Efficiency indicators
            #
            indicators.delta_margin_score(calculators.delta_margin(company_data, year)),
            indicators.delta_turnover_score(calculators.delta_turnover(company_data, year)),
        ]

        print(f"{company} ({year}) - Piotroski F-Score: {sum(scores)}")
        print("  Scores: ", scores)
