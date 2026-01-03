# 1/2/26

## State

Each agent has a scalar state [0, 1]

## Initialization 

States sampled from random(0, 1)

## Time

Discrete timesteps t = 0, 1, 2, ...

## Update Rule

At each timestep, synchronously compute population average u(t)
Each agent updates values:

a(t+1) = a(t) + (u(t) - a(t))/k

## Parameters 

Population size N
Convergence rate K