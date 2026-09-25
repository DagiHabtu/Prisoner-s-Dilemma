from pd import Action, History, payoff

def always_coop(history: History) -> int:
    return Action.COOPERATE

def always_defect(history: History) -> int:
    return Action.DEFECT

def tit_for_tat(history: History) -> int:
    if history == []:
        return Action.COOPERATE
        
    else:
        return history[-1][1]

def grudger(history: History) -> int:
    for my_action, opponent_action in history:
        if opponent_action == Action.DEFECT:
            return Action.DEFECT
        
    return Action.COOPERATE

def pavlov(history: History) -> int:
    if history == []:
        return Action.COOPERATE
    else:
        my_action, opponent_action = history[-1]
        my_payoff, _ = payoff(my_action, opponent_action)
        if my_payoff == 5 or my_payoff == 3:
            return my_action
        else:
            return -my_action