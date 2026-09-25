from typing import Callable

class Action:
    COOPERATE = 1
    DEFECT = -1

History = list[tuple[int, int]]
Strategy = Callable[[History], int]

def payoff(a: int, b: int) -> tuple[int, int]:
    # Reward/Punishment for Action pairs 
    if a == Action.COOPERATE and b == Action.COOPERATE:
        return (3, 3)
    elif a == Action.DEFECT and b == Action.DEFECT:
        return (1, 1)
    elif a == Action.DEFECT and b == Action.COOPERATE:
        return (5, 0)
    elif a == Action.COOPERATE and b == Action.DEFECT:
        return (0, 5)
    else:
        raise ValueError(f"Invalid action: {a!r}, {b!r}")
    


