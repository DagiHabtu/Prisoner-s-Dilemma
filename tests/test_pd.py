import pytest
from pd import Action, payoff 

def test_payoff() -> None:
    assert payoff(Action.COOPERATE, Action.COOPERATE) == (3, 3)
    assert payoff(Action.DEFECT, Action.DEFECT) == (1, 1)
    assert payoff(Action.DEFECT, Action.COOPERATE) == (5, 0)
    assert payoff(Action.COOPERATE, Action.DEFECT) == (0, 5)
    with pytest.raises(ValueError):
        payoff(2, 1)




