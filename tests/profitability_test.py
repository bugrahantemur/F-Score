import random
from profitability import roa_score, cfo_score, delta_roa_score, accrual_score


def test_roa_score():
    assert roa_score(random.uniform(0.01, 1)) == 1
    assert roa_score(random.uniform(-1, -0.01)) == 0
    assert roa_score(0.0) == 0


def test_cfo_score():
    assert cfo_score(random.uniform(0.01, 1)) == 1
    assert cfo_score(random.uniform(-1, -0.01)) == 0
    assert cfo_score(0.0) == 0


def test_delta_roa_score():
    assert delta_roa_score(random.uniform(0.01, 1)) == 1
    assert delta_roa_score(random.uniform(-1, -0.01)) == 0
    assert delta_roa_score(0.0) == 0


def test_accrual_score():
    assert accrual_score(random.uniform(0.01, 1)) == 0
    assert accrual_score(random.uniform(-1, -0.01)) == 1
    assert accrual_score(0.0) == 0
