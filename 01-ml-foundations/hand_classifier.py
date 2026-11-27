"""Phase 1: classify poker hands with machine learning.

The baseline (raw card columns) already works. Your job is to implement
`engineer_features` and see how much better the model gets.

Usage:
    python 01-ml-foundations/hand_classifier.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, f1_score

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
TRAIN_FILE = DATA_DIR / "poker-hand-training-true.data"
TEST_FILE = DATA_DIR / "poker-hand-testing.data"

COLUMNS = ["S1", "C1", "S2", "C2", "S3", "C3", "S4", "C4", "S5", "C5", "label"]
SUIT_COLS = ["S1", "S2", "S3", "S4", "S5"]
RANK_COLS = ["C1", "C2", "C3", "C4", "C5"]

LABEL_NAMES = [
    "nothing", "one pair", "two pairs", "three of a kind", "straight",
    "flush", "full house", "four of a kind", "straight flush", "royal flush",
]


def load(path: Path, max_rows: int | None = None) -> pd.DataFrame:
    if not path.exists():
        sys.exit(
            f"Missing {path}.\n"
            "Download the Poker Hand dataset from the UCI Machine Learning "
            "Repository and put the .data files in the data/ folder."
        )
    return pd.read_csv(path, header=None, names=COLUMNS, nrows=max_rows)


def raw_features(df: pd.DataFrame) -> pd.DataFrame:
    """Baseline: just the 10 raw columns. The model has to discover everything itself."""
    return df[SUIT_COLS + RANK_COLS]


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """YOUR TASK: build features that make hand types easy to spot.

    Ideas (try them one at a time and see which helps most):
      - how many times each rank appears (13 columns), or just the sorted
        counts, e.g. a full house is always [3, 2]
      - the number of distinct ranks and distinct suits
      - is_flush: all 5 suits the same
      - the gap between the highest and lowest rank (watch out: Ace is 1 here)
      - is_straight: 5 distinct ranks with max - min == 4, plus the A-10-J-Q-K case

    Return a DataFrame with one row per hand (same order as df).
    """
    # TODO: replace this with your implementation
    raise NotImplementedError


def train_and_report(name: str, X_train, y_train, X_test, y_test) -> None:
    model = RandomForestClassifier(n_estimators=100, random_state=0, n_jobs=-1)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    print(f"\n=== {name} ===")
    print(f"Accuracy: {accuracy_score(y_test, preds):.3f}")
    print(f"Macro F1: {f1_score(y_test, preds, average='macro'):.3f}")
    present = sorted(set(y_test) | set(preds))
    print(classification_report(
        y_test, preds, labels=present,
        target_names=[LABEL_NAMES[i] for i in present], zero_division=0,
    ))


def main() -> None:
    train = load(TRAIN_FILE)
    # The test file has 1,000,000 rows; 100k is plenty and much faster.
    test = load(TEST_FILE, max_rows=100_000)
    y_train, y_test = train["label"], test["label"]

    train_and_report("Baseline: raw cards", raw_features(train), y_train, raw_features(test), y_test)

    try:
        X_train, X_test = engineer_features(train), engineer_features(test)
    except NotImplementedError:
        print("\nengineer_features isn't implemented yet. That's your next step!")
        return
    train_and_report("Engineered features", X_train, y_train, X_test, y_test)


if __name__ == "__main__":
    main()
