"""Card basics.

Ranks are integers 2..14 (11 = Jack, 12 = Queen, 13 = King, 14 = Ace).
Suits are single letters: s (spades), h (hearts), d (diamonds), c (clubs).
Cards are written as two characters, e.g. "As" (ace of spades), "Td" (ten of diamonds).
"""

from __future__ import annotations

import random
from dataclasses import dataclass

RANK_CHARS = "23456789TJQKA"
SUITS = "shdc"


@dataclass(frozen=True, order=True)
class Card:
    rank: int  # 2..14
    suit: str  # one of "shdc"

    def __post_init__(self) -> None:
        if not 2 <= self.rank <= 14:
            raise ValueError(f"rank must be 2..14, got {self.rank}")
        if self.suit not in SUITS:
            raise ValueError(f"suit must be one of {SUITS!r}, got {self.suit!r}")

    @classmethod
    def from_str(cls, text: str) -> "Card":
        """Parse a card like "As" or "Td"."""
        if len(text) != 2:
            raise ValueError(f"cards are two characters, e.g. 'As', got {text!r}")
        rank_char, suit = text[0].upper(), text[1].lower()
        if rank_char not in RANK_CHARS:
            raise ValueError(f"unknown rank {rank_char!r}")
        return cls(RANK_CHARS.index(rank_char) + 2, suit)

    def __str__(self) -> str:
        return RANK_CHARS[self.rank - 2] + self.suit


def parse_hand(text: str) -> list[Card]:
    """Parse a space-separated hand like "As Kd 7c 7h 2s"."""
    return [Card.from_str(part) for part in text.split()]


def full_deck() -> list[Card]:
    """All 52 cards."""
    return [Card(rank, suit) for suit in SUITS for rank in range(2, 15)]


def deal(n: int, rng: random.Random | None = None) -> list[Card]:
    """Deal n distinct random cards from a fresh deck."""
    rng = rng or random.Random()
    return rng.sample(full_deck(), n)
