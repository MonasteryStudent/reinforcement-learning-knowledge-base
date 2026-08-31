## Definition

An **agent** is the decision-making entity in a [[Reinforcement Learning|reinforcement-learning]] problem.

At each time step, the agent receives the current [[State|state]] from the [[Environment|environment]] and selects an available [[Action|action]] according to its [[Policy|policy]]. The agent's objective is to learn a policy that produces a high expected [[Return|return]].

## Mathematical Formulation

At time step $t$, the agent receives state

$$
s_t\in\mathcal{S}
$$

and selects an action

$$
a_t\in\mathcal{A}(s_t).
$$

The probability that the agent selects action $a_t$ in state $s_t$ is determined by its policy:

$$
\pi(a_t\mid s_t).
$$

For every state, the action probabilities satisfy

$$
\sum_{a\in\mathcal{A}(s_t)}
\pi(a\mid s_t)=1.
$$