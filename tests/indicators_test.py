import indicators as ind
import pandas as pd

#
# Profitability indicators
#


def test_roa_score():
    df = pd.DataFrame()

    df[ind.cols["IO"] + "2022"] = [10, -10]
    df[ind.cols["TA"] + "2021"] = [1_000, 1_000]

    # Positive ROA -- negative ROA
    assert ind.roa_score(df, 2022) == [1, 0]


def test_cfo_score():
    df = pd.DataFrame()

    df[ind.cols["CO"] + "2022"] = [10, -10]
    df[ind.cols["TA"] + "2021"] = [1_000, 1_000]

    # Positive CFO -- negative CFO
    assert ind.cfo_score(df, 2022) == [1, 0]


def test_delta_roa_score():
    df = pd.DataFrame()

    df[ind.cols["IO"] + "2022"] = [15, 5]
    df[ind.cols["IO"] + "2021"] = [10, 10]

    df[ind.cols["TA"] + "2021"] = [1_000, 1_000]
    df[ind.cols["TA"] + "2020"] = [1_000, 1_000]

    # Increasing ROA -- decreasing ROA
    assert ind.delta_roa_score(df, 2022) == [1, 0]


def test_accrual_score():
    df = pd.DataFrame()

    df[ind.cols["IO"] + "2022"] = [10, 10]
    df[ind.cols["CO"] + "2022"] = [15, 5]
    df[ind.cols["TA"] + "2021"] = [1_000, 1_000]

    # Negative accruals -- positive accruals
    assert ind.accrual_score(df, 2022) == [1, 0]


#
# Capital structure indicators
#


def test_delta_leverage_score():
    df = pd.DataFrame()

    df[ind.cols["LD"] + "2022"] = [500, 2_000]
    df[ind.cols["LD"] + "2021"] = [1_000, 1_000]

    df[ind.cols["TA"] + "2022"] = [1_000, 1_000]
    df[ind.cols["TA"] + "2021"] = [1_000, 1_000]
    df[ind.cols["TA"] + "2020"] = [1_000, 1_000]

    # Increasing leverage -- decreasing leverage
    assert ind.delta_leverage_score(df, 2022) == [1, 0]


def test_delta_liquidity_score():
    df = pd.DataFrame()

    df[ind.cols["CA"] + "2022"] = [2_000, 500]
    df[ind.cols["CA"] + "2021"] = [1_000, 1_000]

    df[ind.cols["CL"] + "2022"] = [1_000, 1_000]
    df[ind.cols["CL"] + "2021"] = [1_000, 1_000]

    # Increasing liquidity -- decreasing liquidity
    assert ind.delta_liquidity_score(df, 2022) == [1, 0]


def test_eq_offer_scoree():
    df = pd.DataFrame()

    df[ind.cols["SO"] + "2022"] = [1_000, 1_200]
    df[ind.cols["SO"] + "2021"] = [1_000, 1_000]

    # No new equity offered -- new equity offered
    assert ind.eq_offer_score(df, 2022) == [1, 0]


#
# Efficiency indicators
#


def test_delta_margin_score():
    df = pd.DataFrame()

    df[ind.cols["GM"] + "2022"] = [2_000, 500]
    df[ind.cols["GM"] + "2021"] = [1_000, 1_000]

    df[ind.cols["TA"] + "2021"] = [1_000, 1_000]
    df[ind.cols["TA"] + "2020"] = [1_000, 1_000]

    # Increasing margin ration -- decreasing margin ratio
    assert ind.delta_margin_score(df, 2022) == [1, 0]


def test_delta_turnover_score():
    df = pd.DataFrame()

    df[ind.cols["NS"] + "2022"] = [2_000, 500]
    df[ind.cols["NS"] + "2021"] = [1_000, 1_000]

    df[ind.cols["TA"] + "2021"] = [1_000, 1_000]
    df[ind.cols["TA"] + "2020"] = [1_000, 1_000]

    # Increasing turnover -- decreasing turnover
    assert ind.delta_turnover_score(df, 2022) == [1, 0]
