## Definition

An **optimal policy** is a [[Policy|policy]] whose [[State Value|state values]] are greater than or equal to those of every other policy for all states.

An optimal policy therefore maximizes the expected [[Return|return]], regardless of the state from which the [[Agent|agent]] starts.

Optimal policies always exist in the tabular setting considered in Zhao's book. They are not necessarily unique, and they can be deterministic or stochastic. However, there always exists a deterministic greedy optimal policy.

A greedy optimal policy selects an [[Action|action]] with the greatest optimal [[Action Value|action value]] in each state.

## Mathematical Formulation

A policy $\pi^*$ is optimal if

$$
v_{\pi^*}(s)\geq v_\pi(s)
$$

for every state $s\in\mathcal{S}$ and every policy $\pi\in\Pi$.

The optimal action value is

$$
q^*(s,a)=\sum_{r\in\mathcal{R}(s,a)}p(r\mid s,a)r+\gamma\sum_{s'\in\mathcal{S}}p(s'\mid s,a)v^*(s').
$$

A greedy optimal action is selected according to

$$
a^*(s)=\underset{a\in\mathcal{A}(s)}{\arg\max}\ q^*(s,a).
$$

A deterministic greedy optimal policy can then be expressed as

$$
\pi^*(a\mid s)=
\begin{cases}
1, & a=a^*(s),\\
0, & a\neq a^*(s).
\end{cases}
$$

If multiple actions have the same greatest action value, different optimal policies can select different maximizing actions. This explains why the optimal state value is unique while an optimal policy may not be unique.