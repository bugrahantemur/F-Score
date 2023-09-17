import indicators as ind
import pandas as pd

#
# Profitability indicators
#


def test_roa_score():
    df = pd.DataFrame()

    df["NetIncomeFromContinuingOps_2022"] = [10, -10]
    df["TotalAssets_2021"] = [1_000, 1_000]

    # Positive ROA -- negative ROA
    assert ind.roa_score(df, 2022) == [1, 0]


def test_cfo_score():
    df = pd.DataFrame()

    df["NetCashFromOperatingActivities_2022"] = [10, -10]
    df["TotalAssets_2021"] = [1_000, 1_000]

    # Positive CFO -- negative CFO
    assert ind.cfo_score(df, 2022) == [1, 0]


def test_delta_roa_score():
    df = pd.DataFrame()

    df["NetIncomeFromContinuingOps_2022"] = [15, 5]
    df["NetIncomeFromContinuingOps_2021"] = [10, 10]

    df["TotalAssets_2021"] = [1_000, 1_000]
    df["TotalAssets_2020"] = [1_000, 1_000]

    # Increasing ROA -- decreasing ROA
    assert ind.delta_roa_score(df, 2022) == [1, 0]


def test_accrual_score():
    df = pd.DataFrame()

    df["NetIncomeFromContinuingOps_2022"] = [10, 10]
    df["NetCashFromOperatingActivities_2022"] = [15, 5]
    df["TotalAssets_2021"] = [1_000, 1_000]

    # Negative accruals -- positive accruals
    assert ind.accrual_score(df, 2022) == [1, 0]


#
# Capital structure indicators
#


def test_delta_leverage_score():
    df = pd.DataFrame()

    df["LongTermDebt_2022"] = [500, 2_000]
    df["LongTermDebt_2021"] = [1_000, 1_000]

    df["TotalAssets_2022"] = [1_000, 1_000]
    df["TotalAssets_2021"] = [1_000, 1_000]
    df["TotalAssets_2020"] = [1_000, 1_000]

    # Increasing leverage -- decreasing leverage
    assert ind.delta_leverage_score(df, 2022) == [1, 0]


def test_delta_liquidity_score():
    df = pd.DataFrame()

    df["CurrentAssets_2022"] = [2_000, 500]
    df["CurrentAssets_2021"] = [1_000, 1_000]

    df["CurrentLiabilities_2022"] = [1_000, 1_000]
    df["CurrentLiabilities_2021"] = [1_000, 1_000]

    # Increasing liquidity -- decreasing liquidity
    assert ind.delta_liquidity_score(df, 2022) == [1, 0]


def test_eq_offer_scoree():
    df = pd.DataFrame()

    df["SharesOutstanding_2022"] = [1_000, 1_200]
    df["SharesOutstanding_2021"] = [1_000, 1_000]

    # No new equity offered -- new equity offered
    assert ind.eq_offer_score(df, 2022) == [1, 0]


#
# Efficiency indicators
#


def test_delta_margin_score():
    df = pd.DataFrame()

    df["GrossMargin_2022"] = [2_000, 500]
    df["GrossMargin_2021"] = [1_000, 1_000]

    df["TotalAssets_2021"] = [1_000, 1_000]
    df["TotalAssets_2020"] = [1_000, 1_000]

    # Increasing margin ration -- decreasing margin ratio
    assert ind.delta_margin_score(df, 2022) == [1, 0]


def test_delta_turnover_score():
    df = pd.DataFrame()

    df["NetSales_2022"] = [2_000, 500]
    df["NetSales_2021"] = [1_000, 1_000]

    df["TotalAssets_2021"] = [1_000, 1_000]
    df["TotalAssets_2020"] = [1_000, 1_000]

    # Increasing turnover -- decreasing turnover
    assert ind.delta_turnover_score(df, 2022) == [1, 0]
