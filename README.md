# Poker AI 🃏

![tests](https://github.com/LongDudeDo/poker-ai/actions/workflows/tests.yml/badge.svg)

Building a poker-playing AI from scratch, one stage at a time: starting with machine learning fundamentals and ending with the game-theory techniques behind superhuman poker bots like Libratus and Pluribus.

I'm a first-year Computer Science student at the University of Warwick, and this repo is my learning log as much as a codebase. Each phase builds on the last.

## Roadmap

| Phase | Goal | Key idea | Status |
| --- | --- | --- | --- |
| [0. Poker engine](poker/) | Card representation and a 5/7-card hand evaluator | Turning poker rules into code | ⬜ Not started |
| [1. ML foundations](01-ml-foundations/) | Classify poker hands with machine learning | Feature engineering matters more than the model | ⬜ Not started |
| [2. Kuhn poker CFR](02-kuhn-cfr/) | Solve a 3-card poker game with Counterfactual Regret Minimization | Learning strategies through self-play and regret | ⬜ Not started |
| [3. Leduc hold'em](03-leduc-holdem/) | Scale CFR up and add a neural hand-strength estimator | Combining ML with game theory | ⬜ Not started |
| [4. Deep CFR](04-deep-cfr/) | Replace CFR's tables with neural networks | How modern poker AIs scale | ⬜ Not started |

Update the status column as you go: ⬜ Not started · 🚧 In progress · ✅ Done

## Why poker is hard for AI

In chess, both players see the whole board. In poker, you can't see your opponent's cards, so the best move depends on what they *might* have, and on what they think *you* might have. You also have to bluff sometimes, or you become predictable. That's why the strongest poker bots use game theory (CFR) rather than standard machine learning alone.

## Running it

```bash
git clone https://github.com/LongDudeDo/poker-ai.git
cd poker-ai
pip install -r requirements.txt
pytest
```

Tests for parts that aren't implemented yet are **skipped**, not failed, so the test suite becomes a progress tracker: the more you build, the more tests turn green.

## Structure

```
poker/              # shared poker engine (cards, hand evaluator)
01-ml-foundations/  # phase 1: ML hand classifier
02-kuhn-cfr/        # phase 2: CFR on Kuhn poker
03-leduc-holdem/    # phase 3: Leduc hold'em + neural hand strength
04-deep-cfr/        # phase 4: Deep CFR
tests/              # tests for every phase
LEARNING_LOG.md     # what I learned at each step
```

## Resources

- Neller & Lanctot, *An Introduction to Counterfactual Regret Minimization* (the main guide for phase 2)
- Brown et al., *Deep Counterfactual Regret Minimization* (2019) (phase 4)
- Brown & Sandholm, *Superhuman AI for multiplayer poker* (Pluribus, 2019)
- [RLCard](https://github.com/datamllab/rlcard) and [OpenSpiel](https://github.com/google-deepmind/open_spiel): ready-made poker environments
- UCI Machine Learning Repository, *Poker Hand* dataset (phase 1)
