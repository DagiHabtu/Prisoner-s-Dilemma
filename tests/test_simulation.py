from simulation import play_match, tournament, match_outcome
from strategies import always_coop, always_defect, tit_for_tat, grudger, pavlov

def test_simulation_coop_vs_defect() -> None:
    assert play_match(always_coop, always_defect, rounds=3) == (0, 15)

def test_simulation_defect_vs_coop() -> None:
    assert play_match(always_defect, always_coop, rounds=3) == (15, 0)

def test_simulation_tit_for_tat() -> None:
    assert play_match(always_coop, tit_for_tat, rounds=3) == (9, 9)
    assert play_match(tit_for_tat, always_coop, rounds=3) == (9, 9)
    assert play_match(always_defect, tit_for_tat, rounds=3) == (7, 2)
    assert play_match(tit_for_tat, always_defect, rounds=3) == (2, 7)
    assert play_match(tit_for_tat, tit_for_tat, rounds=3) == (9, 9)

def test_simulation_grudger() -> None:
    assert play_match(grudger, grudger, rounds=3) == (9, 9)

def test_simulation_tournament() -> None:
    ranking, outcomes = tournament([always_coop, always_defect], rounds=3)
    assert ranking == [
        (always_defect, 18),
        (always_coop, 9)
        ]
    assert outcomes == {
        always_coop: {"wins": 0, "losses": 1, "ties": 1},
        always_defect: {"wins": 1, "losses": 0, "ties": 1}
    }
        
    
    

def test_simulation_tournament_one_round() -> None:
    ranking, outcomes = tournament([always_coop, always_defect], rounds=1)

    assert ranking == [
        (always_defect, 6),
        (always_coop, 3)
    ]

    assert outcomes == {
        always_coop: {"wins": 0, "losses": 1, "ties": 1},
        always_defect: {"wins": 1, "losses": 0, "ties": 1}
    }

def test_simulation_ranking() -> None:
    ranking, outcomes = tournament([always_coop, always_defect], rounds=3)

    assert ranking == [
        (always_defect, 18),
        (always_coop, 9)
    ]

    assert outcomes == {
        always_coop: {"wins": 0, "losses": 1, "ties": 1},
        always_defect: {"wins": 1, "losses": 0, "ties": 1}
    }

def test_simulation_tournament_all_strategies() -> None:
    ranking, outcomes = tournament(
        [always_coop, always_defect, tit_for_tat, grudger, pavlov],
        rounds=100
    )

    assert ranking == [
        (tit_for_tat, 1299),
        (grudger, 1299),
        (pavlov, 1250),
        (always_coop, 1200),
        (always_defect, 1108)
    ]

def test_simulation_match_outcome() -> None:
    assert match_outcome(15, 0) == "win"
    assert match_outcome(0, 15) == "loss"
    assert match_outcome(9, 9) == "tie"