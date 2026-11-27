# Phase 1: Machine learning foundations

Running alongside the Warwick AI Society's 5-workshop course. After each workshop, apply what I learned to poker.

## The main project: poker hand classifier

Train a model to look at 5 cards and say what hand it is (pair, flush, straight...), using the **Poker Hand** dataset from the UCI Machine Learning Repository.

This sounds easy, but it's a classic lesson: a model given the raw cards does badly, because "pair" isn't visible in any single column. Once you engineer the right features, accuracy jumps. The point of this phase is to *see that happen*.

### Setup

1. Download the Poker Hand dataset from the UCI Machine Learning Repository.
2. Put `poker-hand-training-true.data` and `poker-hand-testing.data` in a `data/` folder at the repo root (it's git-ignored).
3. Run:
   ```bash
   python 01-ml-foundations/hand_classifier.py
   ```

**Data format:** each row has 10 numbers then a label. Pairs of (suit 1-4, rank 1-13) for each of 5 cards, where rank 1 = Ace and 13 = King. The label is 0-9: nothing, one pair, two pairs, three of a kind, straight, flush, full house, four of a kind, straight flush, royal flush.

### Steps

1. **Run the baseline** as it is. Note the accuracy in the learning log. Look at the per-class report: which hands does it get wrong?
2. **Implement `engineer_features`** in `hand_classifier.py`. Rerun and compare.
3. **Stretch:** try different models (logistic regression, a decision tree, a small neural network with `MLPClassifier`). Which benefit most from good features? Why?
4. **Stretch:** the classes are hugely imbalanced (almost half the hands are "nothing"). Why does that make plain accuracy misleading? Look up macro-F1.

## Workshop log

Fill in after each workshop: what it covered and how I applied it to poker.

| # | Workshop topic | Applied to poker | Notes |
| --- | --- | --- | --- |
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
