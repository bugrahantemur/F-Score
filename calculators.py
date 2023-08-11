def roa(company_data, year):
    return (
        company_data["Net income from continuing operations"][str(year)]
        - company_data["Total assets"][str(year - 1)]
    )


def cfo(company_data, year):
    return (
        company_data["Net cash from operating activities"][str(year)]
        / company_data["Total assets"][str(year - 1)]
    )


def delta_roa(company_data, year):
    roa_current = roa(company_data, year)

    roa_prev = roa(company_data, year - 1)

    return roa_current - roa_prev


def accrual(company_data, year):
    return roa(company_data, year) - cfo(company_data, year)


def average_total_assets(company_data, year):
    return 0.5 * (
        company_data["Total assets"][str(year)] + company_data["Total assets"][str(year - 1)]
    )


def leverage(company_data, year, average_total_assets_in_year):
    return company_data["Long-term debt"][str(year)] / average_total_assets_in_year


def delta_leverage(company_data, year):
    leverage_current = leverage_current = leverage(
        company_data, year, average_total_assets(company_data, year)
    )

    leverage_prev = leverage_current = leverage(
        company_data, year - 1, average_total_assets(company_data, year - 1)
    )

    return leverage_current - leverage_prev


def current_ratio(company_data, year):
    return company_data["Current assets"][str(year)] / company_data["Current liabilites"][str(year)]


def delta_liquidity(company_data, year):
    current_ratio_current = current_ratio(company_data, year)

    current_ratio_prev = current_ratio(company_data, year - 1)

    return current_ratio_current - current_ratio_prev


def eq_offer(company_data, year):
    return (
        company_data["Shares outstanding"][str(year)]
        - company_data["Shares outstanding"][str(year - 1)]
    )


def margin_ratio(company_data, year):
    return company_data["Gross margin"][str(year)] / company_data["Total assets"][str(year - 1)]


def delta_margin(company_data, year):
    margin_ratio_current = margin_ratio(company_data, year)

    margin_ratio_prev = margin_ratio(company_data, year - 1)

    return margin_ratio_current - margin_ratio_prev


def turnover(company_data, year):
    return company_data["Gross margin"][str(year)] / company_data["Total assets"][str(year - 1)]


def delta_turnover(company_data, year):
    turnover_current = turnover(company_data, year)

    turnover_prev = turnover(company_data, year - 1)

    return turnover_current - turnover_prev
