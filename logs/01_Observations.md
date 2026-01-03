# 1/3/26

## Summary of Current Project

This model makes no claims about realism or psychology; it only explores informational constraints on aggregate predictability.

## Initial Observations

With the individual rule currently being used, I expected the mean to shift between every discrete time-step. Interestingly, the agent's movement towards the mean is symmetric, therefore the mean is conserved. No matter how fast the convergence rate is, the mean is always conserved. I assumed that if individuals change, the aggregate must change. But this proves on a baseline level the premise that individual volatility can coexist with macrowide stability.

## Current Model

A synchronous, deterministic, mean consensus system over scalar agent states.

## Hypothesis

The most glaring assumption with the current working model is the agent's information state. Currently, every agent has perfect and readily instantaneous knowledge of the entire population. I will split the agent list into (10) segments and calculate the mean for each, creating a local mean that its neighbors will converge towards. I predict that every group will now abandon the notion of the global mean, and each will converge towards their local mean. Variance within groups will most likely shrink, but variance between groups will most likely persist if not increase. If implemented correctly, this will also radically now alter the future long-term structure.

## Implementation

New grouping method established, where a list of initial agents is split into groups using split_agents(number_of_groups, group_size). Between every time step now, group average is calculated and used as the mean grouped neighbors now align towards.

## Results

Groups now completely ignore other group's states as reference for local means. Groups now are extremely precise and rapidly converge to intra-group means but inter-group means now differ wildly.

