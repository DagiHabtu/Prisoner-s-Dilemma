from pd import History, Strategy, payoff


def play_match(strategy_a: Strategy, strategy_b: Strategy, rounds: int = 100) -> tuple[int, int]:
    history: History = []
    score_a = 0
    score_b = 0

    for _ in range(rounds):
        history_a = history
        history_b = [(b, a) for a, b in history]

        action_a = strategy_a(history_a)
        action_b = strategy_b(history_b)

        payoff_result = payoff(action_a, action_b)
        round_score_a, round_score_b = payoff_result

        score_a += round_score_a
        score_b += round_score_b

        history.append((action_a, action_b))

    return score_a, score_b


def match_outcome(score_a: int, score_b: int) -> str:
    if score_a > score_b:
        return "win"
    elif score_a < score_b:
        return "loss"
    else:
        return "tie"


def tournament(
    strategies: list[Strategy], rounds: int = 100
) -> tuple[list[tuple[Strategy, int]], dict[Strategy, dict[str, int]]]:
    scores: dict[Strategy, int] = {strategy: 0 for strategy in strategies}
    outcomes: dict[Strategy, dict[str, int]] = {
        strategy: {"wins": 0, "losses": 0, "ties": 0}
        for strategy in strategies
    }

    for i, strategy_a in enumerate(strategies):
        for strategy_b in strategies[i:]:
            score_a, score_b = play_match(strategy_a, strategy_b, rounds)

            result = match_outcome(score_a, score_b)

            if strategy_a is not strategy_b:
                if result == "win":
                    outcomes[strategy_a]["wins"] += 1
                    outcomes[strategy_b]["losses"] += 1
                elif result == "loss":
                    outcomes[strategy_a]["losses"] += 1
                    outcomes[strategy_b]["wins"] += 1
                else:
                    outcomes[strategy_a]["ties"] += 1
                    outcomes[strategy_b]["ties"] += 1

                scores[strategy_a] += score_a
                scores[strategy_b] += score_b

            else:
                # Self play is counted once
                scores[strategy_a] += score_a
                outcomes[strategy_a]["ties"] += 1

    ranking = sorted(
        scores.items(),
        key=lambda item: item[1],
        reverse=True
    )

    return ranking, outcomes

