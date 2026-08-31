## Definition

The **environment** represents everything outside the [[Agent|agent]] that is relevant to the [[Reinforcement Learning|reinforcement-learning]] problem.

At each time step, the current situation is represented by a [[State|state]]. When the agent applies an [[Action|action]], the environment [[State Transition|transitions]] to a next state and produces a [[Reward|reward]]. This behaviour is described by the model, also called the dynamics, of the reinforcement-learning problem.

## Mathematical Formulation

When action $a_t$ is applied in state $s_t$, the environment produces reward $r_{t+1}$ and transitions to state $s_{t+1}$:

$$
s_t
\xrightarrow{a_t}
(r_{t+1},s_{t+1}).
$$

The probability of transitioning to next state $s_{t+1}$ is described by

$$
p(s_{t+1}\mid s_t,a_t),
$$

and the probability of receiving reward $r_{t+1}$ is described by

$$
p(r_{t+1}\mid s_t,a_t).
$$

For every valid state-action pair, the probabilities of all possible next states satisfy

$$
\sum_{s'\in\mathcal{S}}
p(s'\mid s_t,a_t)=1,
$$

and the probabilities of all possible rewards satisfy

$$
\sum_{r\in\mathcal{R}(s_t,a_t)}
p(r\mid s_t,a_t)=1.
$$