## Definition

A **soft policy** is a stochastic [[Policy]] that assigns a positive probability to every action available in every state.

Because every action can be selected, a soft policy continues to explore the [[Environment]]. If an episode is sufficiently long and the state-action pairs are reachable, they may be visited repeatedly without requiring [[Exploring Starts]].

A soft policy therefore provides a way to estimate action values even when the agent cannot begin episodes from arbitrary state-action pairs.

## Mathematical Formulation

A policy $\pi$ is soft if

$$
\pi(a\mid s)>0
$$

for every state $s$ and every action $a\in\mathcal{A}(s)$.

As with every stochastic policy, its action probabilities must satisfy

$$
\sum_{a\in\mathcal{A}(s)}\pi(a\mid s)=1.
$$

A deterministic greedy policy is generally not soft because it assigns probability one to a greedy action and probability zero to all other actions.

An [[Epsilon-Greedy Policy]] is a commonly used soft policy because it assigns a nonzero probability to every available action.