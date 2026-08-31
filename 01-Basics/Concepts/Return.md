## Definition

The **return** is the cumulative [[Reward|reward]] obtained from a particular time step onward along a [[Trajectory|trajectory]].

If a trajectory is infinitely long, simply adding all future rewards may produce a sum that grows without bound or does not converge. The **discounted return** addresses this problem by assigning progressively smaller weights to rewards received further in the future.

The discount rate also determines the relative importance of immediate and future rewards. A small discount rate emphasizes near-future rewards, while a discount rate close to one gives greater importance to rewards received further in the future.

## Mathematical Formulation

For a particular trajectory, the discounted return from time step $t$ is denoted by $g_t$ and defined as

$$
g_t
=
r_{t+1}
+\gamma r_{t+2}
+\gamma^2r_{t+3}
+\cdots,
$$

where

$$
\gamma\in(0,1)
$$

is the discount rate.

The same expression can be written as

$$
g_t
=
\sum_{k=0}^{\infty}
\gamma^kr_{t+k+1}.
$$

Because the weights $\gamma^k$ approach zero as $k$ increases, the discounted sum remains finite for an infinitely long trajectory if the rewards are bounded.

For example, if the [[Agent|agent]] receives a reward of $1$ at every time step, the undiscounted return is

$$
1+1+1+\cdots,
$$

which grows without bound. The discounted return is

$$
1+\gamma+\gamma^2+\cdots
=
\frac{1}{1-\gamma},
$$

which is finite for $\gamma\in(0,1)$.

For a finite trajectory that terminates at time step $T$, the return is

$$
g_t
=
\sum_{k=0}^{T-t-1}
\gamma^kr_{t+k+1}.
$$

The lowercase $g_t$ denotes the return value obtained along one particular trajectory. The corresponding random variable over all possible trajectories is denoted by $G_t$.