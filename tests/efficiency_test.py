import random
from efficiency import delta_margin_score, delta_turnover_score


def test_delta_margin_score():
    assert delta_margin_score(random.uniform(0.01, 1)) == 1
    assert delta_margin_score(random.uniform(-1, -0.01)) == 0
    assert delta_margin_score(0.0) == 0


def test_delta_turnover_score():
    assert delta_turnover_score(random.uniform(0.01, 1)) == 1
    assert delta_turnover_score(random.uniform(-1, -0.01)) == 0
    assert delta_turnover_score(0.0) == 0
