## Definition

**Reinforcement learning** is a learning approach in which an [[Agent|agent]] learns by interacting with an [[Environment|environment]].

At each time step, the agent selects an [[Action|action]], receives a [[Reward|reward]], and undergoes a [[State Transition|state transition]] to a next [[State|state]]. The agent uses this experience to improve its [[Policy|policy]].

The objective is to learn a policy that maximizes the expected [[Return|return]] rather than merely the immediate reward.

## Mathematical Formulation

The interaction between the agent and environment generates a [[Trajectory|trajectory]]:

$$
\tau=
(s_0,a_0,r_1,s_1,a_1,r_2,s_2,\ldots).
$$

A particular trajectory produces a return value $g_t$. Because different trajectories may produce different return values, the corresponding return random variable is denoted by $G_t$.

The reinforcement-learning objective can be expressed as

$$
\pi^*
=
\underset{\pi}{\operatorname{arg\,max}}
\ \mathbb{E}_{\pi}[G_t],
$$

where $\pi^*$ is an optimal policy and $\mathbb{E}_{\pi}[G_t]$ is the expected return when the agent follows policy $\pi$.