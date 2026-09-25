from pd import Action
from strategies import always_coop, always_defect, tit_for_tat, grudger, pavlov

def test_always_coop() -> None:
    assert always_coop(history=[]) == Action.COOPERATE

    assert always_coop(
            history=[
                (Action.COOPERATE, Action.COOPERATE),
                (Action.DEFECT, Action.DEFECT),
            ]
        ) == Action.COOPERATE

def test_always_defect() -> None:
    assert always_defect(history=[]) == Action.DEFECT

    assert always_defect(
        history=[
            (Action.COOPERATE, Action.COOPERATE),
            (Action.DEFECT, Action.COOPERATE),
        ]
    ) == Action.DEFECT

def test_tit_for_tat_no_history() -> None:
    move_no_history = tit_for_tat(history=[])
    assert move_no_history == Action.COOPERATE

def test_tit_for_tat_with_history() -> None:
    move_depending_on_history = tit_for_tat(history=[(Action.COOPERATE, Action.COOPERATE),
                                                     (Action.COOPERATE, Action.DEFECT)])
    assert move_depending_on_history == Action.DEFECT

    move_depending_on_history = tit_for_tat(history=[(Action.COOPERATE, Action.COOPERATE),
                                                    (Action.COOPERATE, Action.COOPERATE)])
    assert move_depending_on_history == Action.COOPERATE

def test_grudger() -> None:
    assert grudger(history=[]) == Action.COOPERATE

    assert grudger(history= [
    (Action.COOPERATE, Action.COOPERATE),
    (Action.COOPERATE, Action.COOPERATE),
    ]) == Action.COOPERATE

    assert grudger(history= [
    (Action.COOPERATE, Action.DEFECT),
    (Action.COOPERATE, Action.COOPERATE),
    ]) == Action.DEFECT

def test_pavlov() -> None:
    assert pavlov(history=[]) == Action.COOPERATE
    assert pavlov(history=[(Action.COOPERATE, Action.COOPERATE)]) == Action.COOPERATE
    assert pavlov(history=[(Action.COOPERATE, Action.DEFECT)]) == Action.DEFECT
    assert pavlov(history=[(Action.DEFECT, Action.COOPERATE)]) == Action.DEFECT
    assert pavlov(history=[(Action.DEFECT, Action.DEFECT)]) == Action.COOPERATE

