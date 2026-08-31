## Definition

A **reward** is numerical feedback received by the [[Agent|agent]] after taking an [[Action|action]] in a [[State|state]]. It indicates the immediate desirability of the outcome of the agent's interaction with the [[Environment|environment]].

A reward can be positive, negative, or zero. The set of possible rewards associated with a state-action pair is called the **reward set**.

## Mathematical Formulation

An individual reward is denoted by $r$. The reward set associated with state $s$ and action $a$ is denoted by $\mathcal{R}(s,a)$. Therefore,

$$
r \in \mathcal{R}(s,a).
$$

In a deterministic model, the reward produced by a state-action pair can be written as

$$
r=r(s,a).
$$

In a stochastic model, the reward probability is denoted by

$$
p(r \mid s,a),
$$

which represents the probability of receiving reward $r$ after taking action $a$ in state $s$.

For every state-action pair, the probabilities of all possible rewards must sum to one:

$$
\sum_{r \in \mathcal{R}(s,a)}p(r \mid s,a)=1.
$$

In addition,

$$
p(r \mid s,a)\geq 0
$$

for every $r \in \mathcal{R}(s,a)$.