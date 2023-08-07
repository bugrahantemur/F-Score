import random
import indicators

# Profitability indicators


def test_roa_score():
    assert indicators.roa_score(random.uniform(0.01, 1)) == 1
    assert indicators.roa_score(random.uniform(-1, -0.01)) == 0
    assert indicators.roa_score(0.0) == 0


def test_cfo_score():
    assert indicators.cfo_score(random.uniform(0.01, 1)) == 1
    assert indicators.cfo_score(random.uniform(-1, -0.01)) == 0
    assert indicators.cfo_score(0.0) == 0


def test_delta_roa_score():
    assert indicators.delta_roa_score(random.uniform(0.01, 1)) == 1
    assert indicators.delta_roa_score(random.uniform(-1, -0.01)) == 0
    assert indicators.delta_roa_score(0.0) == 0


def test_accrual_score():
    assert indicators.accrual_score(random.uniform(0.01, 1)) == 0
    assert indicators.accrual_score(random.uniform(-1, -0.01)) == 1
    assert indicators.accrual_score(0.0) == 0


# Capital structure indicators


def test_delta_leverage_score():
    assert indicators.delta_leverage_score(random.uniform(0.01, 1)) == 0
    assert indicators.delta_leverage_score(random.uniform(-1, -0.01)) == 1
    assert indicators.delta_leverage_score(0.0) == 0


def test_delta_liquidity_score():
    assert indicators.delta_liquidity_score(random.uniform(0.01, 1)) == 1
    assert indicators.delta_liquidity_score(random.uniform(-1, -0.01)) == 0
    assert indicators.delta_liquidity_score(0.0) == 0


def test_eq_offer_scoree():
    assert indicators.eq_offer_score(True) == 1
    assert indicators.eq_offer_score(False) == 0


# Efficiency indicators


def test_delta_margin_score():
    assert indicators.delta_margin_score(random.uniform(0.01, 1)) == 1
    assert indicators.delta_margin_score(random.uniform(-1, -0.01)) == 0
    assert indicators.delta_margin_score(0.0) == 0


def test_delta_turnover_score():
    assert indicators.delta_turnover_score(random.uniform(0.01, 1)) == 1
    assert indicators.delta_turnover_score(random.uniform(-1, -0.01)) == 0
    assert indicators.delta_turnover_score(0.0) == 0
