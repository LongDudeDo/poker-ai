# Phase 0: Poker engine

The shared code every later phase uses.

- `cards.py`: card representation, parsing ("As Kd 7c"), dealing. **Done, no changes needed.**
- `evaluator.py`: decides which hand wins. **Your job: implement `evaluate_5`.**

## Steps

1. Read the docstring in `evaluator.py`, it explains the return format with examples.
2. Implement `evaluate_5`.
3. Run `pytest tests/test_evaluator.py -v` until everything passes.
4. Stretch: time how long `best_of_7` takes on 100,000 random hands. Later phases call it a lot, so speed will matter.

## Things to think about

- Why return a tuple instead of a single number?
- How many 5-card hands are there in total? (Hint: 52 choose 5.) How often does each category come up?
