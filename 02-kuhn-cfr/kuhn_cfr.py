"""Phase 2: solve Kuhn poker with Counterfactual Regret Minimization (CFR).

Kuhn poker rules:
  - 3 cards: Jack, Queen, King (stored as 0, 1, 2). Each player gets one; one is unused.
  - Both players put 1 chip in the pot (the ante).
  - Player 0 acts first: pass (check) or bet 1 chip.
  - Actions are written as a history string of "p" (pass) and "b" (bet):
      "pp"   both check            -> showdown, higher card wins 1
      "bb"   bet, call             -> showdown, higher card wins 2
      "bp"   bet, fold             -> player 0 wins 1
      "pbb"  check, bet, call      -> showdown, higher card wins 2
      "pbp"  check, bet, fold      -> player 1 wins 1

The game rules and training loop are written for you.
YOUR TASKS are the three TODOs:
  1. InfoSetNode.get_strategy        (regret matching)
  2. InfoSetNode.get_average_strategy
  3. KuhnTrainer.cfr                  (the CFR recursion)

Guide: Neller & Lanctot, "An Introduction to Counterfactual Regret Minimization".
Check your work with: pytest tests/test_kuhn_cfr.py -v

Known answer: player 0's expected value at equilibrium is -1/18 (about -0.056).
"""

from __future__ import annotations

import random

import numpy as np

PASS, BET = 0, 1
NUM_ACTIONS = 2
ACTION_CHARS = "pb"
CARD_NAMES = "JQK"
TERMINAL_HISTORIES = {"pp", "bb", "bp", "pbb", "pbp"}


def is_terminal(history: str) -> bool:
    return history in TERMINAL_HISTORIES


def terminal_utility(cards: list[int], history: str) -> float:
    """Payoff at the end of the game, for the player whose turn it *would* be.

    The player to act is len(history) % 2. This matches how cfr() works:
    it always returns utility from the point of view of the player to act.
    """
    player = len(history) % 2
    opponent = 1 - player
    player_has_higher_card = cards[player] > cards[opponent]

    if history[-1] == "p":
        if history == "pp":
            return 1.0 if player_has_higher_card else -1.0
        # A bet was followed by a pass: the opponent (who just acted) folded.
        return 1.0
    # Ends in "bb": bet was called, showdown for 2.
    return 2.0 if player_has_higher_card else -2.0


class InfoSetNode:
    """Everything a player knows at one decision point: their card + the history.

    regret_sum[a]:   total regret for not having picked action a
    strategy_sum[a]: total probability of picking a, weighted by how often we got here
    """

    def __init__(self, info_set: str) -> None:
        self.info_set = info_set
        self.regret_sum = np.zeros(NUM_ACTIONS)
        self.strategy_sum = np.zeros(NUM_ACTIONS)

    def get_strategy(self, realization_weight: float) -> np.ndarray:
        """Regret matching: turn regrets into a probability distribution.

        1. Take the positive part of each regret (negative regrets count as 0).
        2. If the total is > 0, normalise so the probabilities sum to 1.
           Otherwise, play uniformly at random (0.5, 0.5).
        3. Add realization_weight * strategy to self.strategy_sum
           (this is what get_average_strategy uses later).
        4. Return the strategy.
        """
        # TODO
        raise NotImplementedError

    def get_average_strategy(self) -> np.ndarray:
        """The average strategy over all training iterations.

        This, not the current strategy, is what converges to equilibrium.
        Normalise self.strategy_sum to sum to 1 (uniform if it's all zero).
        """
        # TODO
        raise NotImplementedError

    def __repr__(self) -> str:
        card = CARD_NAMES[int(self.info_set[0])]
        history = self.info_set[1:] or "(start)"
        bet = self.get_average_strategy()[BET]
        return f"{card} {history:>7}: bet/call {bet:5.1%}"


class KuhnTrainer:
    def __init__(self) -> None:
        self.nodes: dict[str, InfoSetNode] = {}

    def get_node(self, info_set: str) -> InfoSetNode:
        if info_set not in self.nodes:
            self.nodes[info_set] = InfoSetNode(info_set)
        return self.nodes[info_set]

    def cfr(self, cards: list[int], history: str, p0: float, p1: float) -> float:
        """Run one pass of CFR from this point in the game.

        cards:   cards[0] is player 0's card, cards[1] is player 1's
        history: actions so far, e.g. "pb"
        p0, p1:  probability that each player played to reach this point

        Returns the expected utility for the player to act.

        Steps:
          1. If the history is terminal, return terminal_utility(cards, history).
          2. player = len(history) % 2. Build the info set key: str(cards[player]) + history.
          3. Get the node's strategy (realization weight = this player's reach probability).
          4. For each action, recurse into history + "p" or "b", updating the acting
             player's reach probability. The child returns utility for the *other*
             player, so negate it.
          5. Node utility = sum over actions of strategy[a] * util[a].
          6. Regret for each action = util[a] - node utility. Add it to regret_sum,
             weighted by the OPPONENT's reach probability.
          7. Return the node utility.
        """
        # TODO
        raise NotImplementedError

    def train(self, iterations: int, seed: int = 0) -> float:
        """Self-play training. Returns player 0's average utility."""
        rng = random.Random(seed)
        cards = [0, 1, 2]
        total = 0.0
        for _ in range(iterations):
            rng.shuffle(cards)
            total += self.cfr(cards, "", 1.0, 1.0)
        return total / iterations

    def average_strategies(self) -> dict[str, np.ndarray]:
        return {key: node.get_average_strategy() for key, node in sorted(self.nodes.items())}


def main() -> None:
    trainer = KuhnTrainer()
    value = trainer.train(100_000)
    print(f"Player 0 average game value: {value:.4f}  (theory: {-1/18:.4f})\n")
    for key in sorted(trainer.nodes, key=lambda k: (len(k), k)):
        print(trainer.nodes[key])


if __name__ == "__main__":
    main()
