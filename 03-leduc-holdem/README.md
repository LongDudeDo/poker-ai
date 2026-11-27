# Phase 3: Leduc hold'em + neural hand strength

Leduc hold'em is a bigger poker game used in research: 6 cards (two each of J, Q, K), two betting rounds and a shared board card. It's too big to solve by hand but small enough for CFR on a laptop.

## Plan

1. **Monte Carlo CFR on Leduc.** Use the [RLCard](https://github.com/datamllab/rlcard) environment (`pip install rlcard`). Adapt your Kuhn CFR: same idea, but sample chance outcomes instead of visiting every one.
2. **Evaluate the bot** against a random agent and a simple rule-based agent. Track win rate in big blinds per 100 hands.
3. **Neural hand-strength estimator.** Use the phase 0 evaluator to simulate thousands of random hold'em showdowns, recording (hole cards, board) → win probability. Train a small neural network to predict win probability without simulating. This is where phase 1's ML comes back in.

## Questions to answer in the learning log

- Why does vanilla CFR get slow here, and how does sampling fix it?
- How accurate is the neural estimator vs simulation, and how much faster is it?
