def roa_score(roa):
    return 1 if roa > 0.0 else 0


def cfo_score(cfo):
    return 1 if cfo > 0.0 else 0


def delta_roa_score(delta_roa):
    return 1 if delta_roa > 0.0 else 0


def accrual_score(accrual):
    return 1 if accrual < 0.0 else 0
