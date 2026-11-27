# Phase 4: Deep CFR

In full poker there are far too many situations to store a regret table for each one. Deep CFR replaces the tables with neural networks that *predict* regrets, so similar situations share what they've learned.

## Plan

1. Read Brown et al., *Deep Counterfactual Regret Minimization* (2019).
2. Re-implement Leduc hold'em with Deep CFR (PyTorch). Compare against your phase 3 tabular bot.
3. Stretch: heads-up limit Texas hold'em with card abstraction.

## Reading

- Brown, Lerer, Gross & Sandholm, *Deep Counterfactual Regret Minimization* (2019)
- Brown & Sandholm, *Superhuman AI for heads-up no-limit poker: Libratus beats top professionals* (2018)
- Brown & Sandholm, *Superhuman AI for multiplayer poker* (Pluribus, 2019)
