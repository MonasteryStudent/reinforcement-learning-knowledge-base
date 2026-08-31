## Definition

A **state transition** is the change from the [[Agent|agent]]'s current [[State|state]] to a next state after the agent takes an [[Action|action]].

A state transition can be deterministic or stochastic. In a deterministic transition, a state-action pair always produces the same next state. In a stochastic transition, multiple next states may occur with different probabilities.

Remaining in the same state is also considered a state transition.

## Mathematical Formulation

If the agent is in state $s_t$ at time step $t$ and takes action $a_t$, the resulting next state is denoted by $s_{t+1}$:

$$
s_t \xrightarrow{a_t} s_{t+1}.
$$

The state-transition probability is denoted by

$$
p(s' \mid s,a),
$$

which represents the probability of transitioning to next state $s'$ after taking action $a$ in state $s$:

$$
p(s' \mid s,a)
=
P(S_{t+1}=s' \mid S_t=s,A_t=a).
$$

For every valid state-action pair, the probabilities of all possible next states must sum to one:

$$
\sum_{s' \in \mathcal{S}}p(s' \mid s,a)=1.
$$

In addition,

$$
p(s' \mid s,a)\geq 0
$$

for every $s' \in \mathcal{S}$.

In a deterministic transition, there is one next state $s^*$ for which

$$
p(s^* \mid s,a)=1,
$$

while all other next states have probability zero.