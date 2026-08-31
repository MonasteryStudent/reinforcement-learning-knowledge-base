## Definition

A **policy** describes the [[Agent|agent]]'s behaviour by specifying how it selects [[Action|actions]] in each [[State|state]]. It therefore represents a strategy that tells the agent which action to take at every state.

A policy can be deterministic or stochastic. A deterministic policy selects one particular action in each state, whereas a stochastic policy assigns probabilities to the available actions.

## Mathematical Formulation

A policy is denoted by $\pi(a \mid s)$ and represents the probability of selecting action $a$ in state $s$:

$$
\pi(a \mid s)=P(A_t=a \mid S_t=s).
$$

For every state $s$, the probabilities of all available actions must sum to one:

$$
\sum_{a \in \mathcal{A}(s)} \pi(a \mid s)=1.
$$

In addition,

$$
\pi(a \mid s) \geq 0
$$

for every $a \in \mathcal{A}(s)$.

For a deterministic policy, there is one action $a^*$ in each state for which

$$
\pi(a^* \mid s)=1,
$$

while all other available actions have probability zero.