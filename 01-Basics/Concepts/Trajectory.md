## Definition

A **trajectory** is a sequence (or chain) of [[State|states]], [[Action|actions]], and [[Reward|rewards]] generated while the [[Agent|agent]] interacts with the [[Environment|environment]] according to a [[Policy|policy]].

A trajectory can be finite or infinite. Its exact sequence may vary between interactions if the policy or the environment is stochastic.

## Mathematical Formulation

A particular trajectory beginning at time step $0$ can be represented as

$$
\tau=
(s_0,a_0,r_1,s_1,a_1,r_2,s_2,\ldots).
$$

Here, $s_t$ is the state occupied by the agent at time step $t$, $a_t$ is the action taken at that time step, and $r_{t+1}$ is the resulting reward.

At every time step $t$, the values satisfy

$$
s_t\in\mathcal{S},
$$

$$
a_t\in\mathcal{A}(s_t),
$$

and

$$
r_{t+1}\in\mathcal{R}(s_t,a_t).
$$

A single step of the interaction can be represented as

$$
s_t
\xrightarrow{a_t,\;r_{t+1}}
s_{t+1}.
$$