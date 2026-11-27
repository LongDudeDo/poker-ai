"""Hand evaluator: which poker hand wins?

YOUR TASK (Phase 0): implement `evaluate_5`.

Everything else in this file already works once `evaluate_5` does:
`best_of_7` finds the best 5-card hand out of 7 (as in Texas hold'em),
and `compare` tells you which of two hands wins.

Run `pytest tests/test_evaluator.py -v` to check your work.
"""

from __future__ import annotations

from enum import IntEnum
from itertools import combinations

from poker.cards import Card


class HandCategory(IntEnum):
    HIGH_CARD = 0
    PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8


HandValue = tuple[int, tuple[int, ...]]


def evaluate_5(cards: list[Card]) -> HandValue:
    """Score exactly 5 cards.

    Return a tuple (category, tiebreakers) where:
      - category is a HandCategory
      - tiebreakers is a tuple of ranks, most important first

    The key property: comparing two return values with > must give the
    right winner. Python compares tuples left to right, so the category
    decides first and the tiebreakers settle ties.

    Examples:
      K K 7 7 2  ->  (TWO_PAIR, (13, 7, 2))        pairs high to low, then kicker
      9 9 9 4 4  ->  (FULL_HOUSE, (9, 4))
      A K 9 6 3 (all hearts)  ->  (FLUSH, (14, 13, 9, 6, 3))
      5 4 3 2 A  ->  (STRAIGHT, (5,))               the "wheel": ace plays low

    Hints:
      - collections.Counter on the ranks tells you about pairs, trips and quads
      - sorting the (count, rank) pairs gives you the tiebreak order almost for free
      - a flush is when all 5 suits are the same
      - a straight is 5 consecutive distinct ranks; handle A-2-3-4-5 as a special case
    """
    if len(cards) != 5:
        raise ValueError(f"evaluate_5 needs exactly 5 cards, got {len(cards)}")

    # TODO: replace this with your implementation
    raise NotImplementedError


def best_of_7(cards: list[Card]) -> HandValue:
    """Best 5-card hand out of 7 cards (2 hole cards + 5 board cards)."""
    if len(cards) != 7:
        raise ValueError(f"best_of_7 needs exactly 7 cards, got {len(cards)}")
    return max(evaluate_5(list(combo)) for combo in combinations(cards, 5))


def compare(hand_a: list[Card], hand_b: list[Card]) -> int:
    """Return 1 if hand_a wins, -1 if hand_b wins, 0 for a split pot."""
    score = best_of_7 if len(hand_a) == 7 else evaluate_5
    a, b = score(hand_a), score(hand_b)
    return (a > b) - (a < b)
