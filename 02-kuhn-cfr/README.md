# Phase 2: Solving Kuhn poker with CFR

Kuhn poker is the smallest "real" poker game: 3 cards, 2 players, one betting round. It's small enough to solve exactly, but it still has bluffing, which makes it the perfect first test for CFR.

## What is CFR?

Counterfactual Regret Minimization trains a strategy by playing against itself millions of times. At each decision, it asks: *"How much better would I have done if I'd always picked action X here?"* That's the **regret**. Over time, the bot picks actions it regrets *not* taking more often. The **average** strategy across all iterations converges to a Nash equilibrium: a strategy no opponent can exploit.

## Steps

1. Read sections 1-3 of Neller & Lanctot, *An Introduction to Counterfactual Regret Minimization*. It walks through exactly this game.
2. Implement the three TODOs in `kuhn_cfr.py`, in order. Run the tests after each one:
   ```bash
   pytest tests/test_kuhn_cfr.py -v
   ```
3. Run the trainer and look at the strategy it learned:
   ```bash
   python 02-kuhn-cfr/kuhn_cfr.py
   ```

## What you should see (and why it's cool)

Nobody tells the bot to bluff, but it learns to:
- **Bet with a Jack sometimes** (the worst card). That's a bluff.
- **Never bet first with a Queen**: it can't win against a King and only gets called by one.
- **Bet a King about 3x as often as it bluffs with a Jack**. That exact ratio comes out of the maths.
- Player 0's average result converges to **-1/18**: going first is a slight disadvantage.

## Stretch goals

- Plot the game value against iterations. How fast does it converge?
- Implement **CFR+** (clip regrets at zero after each update). How much faster is it?
- Write a `play.py` so you can play against your bot in the terminal.
