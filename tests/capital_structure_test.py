import random
from capital_structure import (
    delta_leverage_score,
    delta_liquidity_score,
    eq_offer_score,
)


def test_delta_leverage_score():
    assert delta_leverage_score(random.uniform(0.01, 1)) == 0
    assert delta_leverage_score(random.uniform(-1, -0.01)) == 1
    assert delta_leverage_score(0.0) == 0


def test_delta_liquidity_score():
    assert delta_liquidity_score(random.uniform(0.01, 1)) == 1
    assert delta_liquidity_score(random.uniform(-1, -0.01)) == 0
    assert delta_liquidity_score(0.0) == 0


def test_eq_offer_scoree():
    assert eq_offer_score(True) == 1
    assert eq_offer_score(False) == 0
