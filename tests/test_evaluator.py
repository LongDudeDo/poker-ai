import pytest

from poker.cards import parse_hand
from poker.evaluator import HandCategory as H, best_of_7, compare, evaluate_5


def category(text):
    return evaluate_5(parse_hand(text))[0]


@pytest.mark.parametrize("hand, expected", [
    ("As Kd 9c 6h 3s", H.HIGH_CARD),
    ("As Ad 9c 6h 3s", H.PAIR),
    ("Ks Kd 7c 7h 2s", H.TWO_PAIR),
    ("9s 9d 9c 6h 3s", H.THREE_OF_A_KIND),
    ("9s 8d 7c 6h 5s", H.STRAIGHT),
    ("Ah Kh 9h 6h 3h", H.FLUSH),
    ("9s 9d 9c 4h 4s", H.FULL_HOUSE),
    ("9s 9d 9c 9h 3s", H.FOUR_OF_A_KIND),
    ("9h 8h 7h 6h 5h", H.STRAIGHT_FLUSH),
    ("Ah Kh Qh Jh Th", H.STRAIGHT_FLUSH),
])
def test_categories(hand, expected):
    assert category(hand) == expected


def test_wheel_is_five_high_straight():
    assert evaluate_5(parse_hand("5s 4d 3c 2h As")) == (H.STRAIGHT, (5,))


def test_wheel_loses_to_six_high_straight():
    assert compare(parse_hand("6s 5d 4c 3h 2s"), parse_hand("5s 4d 3c 2h As")) == 1


def test_ace_high_straight():
    assert evaluate_5(parse_hand("As Kd Qc Jh Ts")) == (H.STRAIGHT, (14,))


def test_not_a_straight_when_wrapping_around():
    assert category("Qs Kd Ac 2h 3s") == H.HIGH_CARD


def test_two_pair_tiebreakers():
    assert evaluate_5(parse_hand("Ks Kd 7c 7h 2s")) == (H.TWO_PAIR, (13, 7, 2))


def test_full_house_tiebreakers():
    assert evaluate_5(parse_hand("4s 4d 9c 9h 9s")) == (H.FULL_HOUSE, (9, 4))


def test_kicker_decides():
    assert compare(parse_hand("As Ad Kc 6h 3s"), parse_hand("Ac Ah Qc 6d 3c")) == 1


def test_split_pot():
    assert compare(parse_hand("As Kd 9c 6h 3s"), parse_hand("Ac Kh 9d 6s 3c")) == 0


def test_flush_beats_straight():
    assert compare(parse_hand("2h 5h 7h 9h Jh"), parse_hand("As Kd Qc Jh Ts")) == 1


def test_best_of_7_finds_hidden_flush():
    seven = parse_hand("Ah 2h Kc Kd 7h 9h Jh")
    assert best_of_7(seven)[0] == H.FLUSH
