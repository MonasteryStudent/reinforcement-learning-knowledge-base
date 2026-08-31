## Definition

A **state** describes the [[Agent|agent]]'s current situation with respect to the [[Environment|environment]]. What information is included in a state depends on how the [[Reinforcement Learning|reinforcement-learning]] problem is modelled.

The set of all possible states is called the **state space**.

## Mathematical Formulation

An individual state is denoted by $s$, and the state space is denoted by $\mathcal{S}$. Therefore,

$$
s \in \mathcal{S}.
$$

If the state space contains $n$ states, it can be written as

$$
\mathcal{S}=\{s_1,s_2,\ldots,s_n\}.
$$

The state occupied by the agent at time step $t$ is denoted by

$$
s_t \in \mathcal{S}.
$$