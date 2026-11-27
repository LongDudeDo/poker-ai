import pytest

from poker.cards import Card, deal, full_deck, parse_hand


def test_parse_card():
    card = Card.from_str("As")
    assert card.rank == 14 and card.suit == "s"
    assert str(Card.from_str("td")) == "Td"


def test_parse_hand():
    assert [str(c) for c in parse_hand("As Kd 7c")] == ["As", "Kd", "7c"]


def test_invalid_cards():
    with pytest.raises(ValueError):
        Card.from_str("1s")
    with pytest.raises(ValueError):
        Card.from_str("Ax")


def test_deck_has_52_unique_cards():
    deck = full_deck()
    assert len(deck) == 52 and len(set(deck)) == 52


def test_deal_is_distinct():
    hand = deal(7)
    assert len(set(hand)) == 7
