import numpy as np
import pytest

from kuhn_cfr import BET, InfoSetNode, KuhnTrainer, terminal_utility


# --- Game rules (already implemented) ---------------------------------------

def test_terminal_utility_showdown():
    # Player 0 has K (2), player 1 has J (0). After "pp" it's player 0's turn.
    assert terminal_utility([2, 0], "pp") == 1
    assert terminal_utility([2, 0], "bb") == 2


def test_terminal_utility_fold():
    # "bp": player 0 bet, player 1 folded. It's player 0's "turn", and they win 1.
    assert terminal_utility([0, 2], "bp") == 1


# --- TODO 1: regret matching -------------------------------------------------

@pytest.mark.parametrize("regrets, expected", [
    ([2.0, -1.0], [1.0, 0.0]),   # negative regret counts as 0
    ([1.0, 3.0], [0.25, 0.75]),  # proportional to positive regret
    ([0.0, 0.0], [0.5, 0.5]),    # no regret yet: play uniformly
    ([-1.0, -2.0], [0.5, 0.5]),  # all negative: also uniform
])
def test_regret_matching(regrets, expected):
    node = InfoSetNode("0")
    node.regret_sum = np.array(regrets)
    assert np.allclose(node.get_strategy(1.0), expected)


def test_get_strategy_accumulates_strategy_sum():
    node = InfoSetNode("0")
    node.regret_sum = np.array([1.0, 3.0])
    node.get_strategy(0.5)
    assert np.allclose(node.strategy_sum, [0.125, 0.375])


# --- TODO 2: average strategy -------------------------------------------------

def test_average_strategy_normalises():
    node = InfoSetNode("0")
    node.strategy_sum = np.array([3.0, 1.0])
    assert np.allclose(node.get_average_strategy(), [0.75, 0.25])


def test_average_strategy_uniform_when_empty():
    assert np.allclose(InfoSetNode("0").get_average_strategy(), [0.5, 0.5])


# --- TODO 3: CFR finds the equilibrium ---------------------------------------
# Info set keys are card + history: "0" = Jack at the start, "1b" = Queen facing a bet.

@pytest.fixture(scope="module")
def trained():
    trainer = KuhnTrainer()
    try:
        value = trainer.train(50_000, seed=0)
    except NotImplementedError:
        pytest.skip("not implemented yet")
    strategies = {key: s[BET] for key, s in trainer.average_strategies().items()}
    return value, strategies


def test_game_value_is_minus_one_eighteenth(trained):
    value, _ = trained
    assert value == pytest.approx(-1 / 18, abs=0.01)


def test_all_twelve_info_sets_visited(trained):
    _, bet = trained
    assert len(bet) == 12


def test_player0_bluffs_jack_and_values_king_three_times_as_often(trained):
    _, bet = trained
    alpha = bet["0"]
    assert 0 <= alpha <= 1 / 3 + 0.03
    assert bet["2"] == pytest.approx(3 * alpha, abs=0.1)


def test_player0_never_opens_queen(trained):
    _, bet = trained
    assert bet["1"] < 0.05


def test_player1_responses(trained):
    _, bet = trained
    assert bet["0b"] < 0.05                              # Jack folds to a bet
    assert bet["2b"] > 0.95                              # King always calls
    assert bet["1b"] == pytest.approx(1 / 3, abs=0.05)   # Queen calls a third of the time
    assert bet["0p"] == pytest.approx(1 / 3, abs=0.05)   # Jack bluffs a third of the time
    assert bet["2p"] > 0.95                              # King always bets
