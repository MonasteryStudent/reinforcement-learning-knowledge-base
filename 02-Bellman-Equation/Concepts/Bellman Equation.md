## Definition

The **Bellman equation** is a set of linear equations describing the relationships between the [[State Value|values]] of all states under a given [[Policy|policy]].

It decomposes the value of a state into two parts:

1. the expected immediate [[Reward|reward]];
2. the discounted expected value of the next state.

Solving the Bellman equation gives the state values of a fixed policy. This process is called **policy evaluation**.

The Bellman equation introduced here evaluates a given policy. The Bellman optimality equation introduced in the following chapter is used to find optimal policies.

## Mathematical Formulation

The [[Return|return]] random variable can be decomposed recursively as

$$
G_t = R_{t+1}+\gamma G_{t+1}.
$$

Substituting this relationship into the definition of the state value gives

$$
v_\pi(s) = \mathbb{E}_\pi[R_{t+1}+\gamma G_{t+1}\mid S_t=s].
$$

Therefore,

$$
v_\pi(s) = \mathbb{E}_\pi[R_{t+1}\mid S_t=s]+\gamma\mathbb{E}_\pi[G_{t+1}\mid S_t=s].
$$

Using the [[Policy|policy]], [[Reward|reward]] probability and [[State Transition|state-transition probability]], the Bellman equation can be written as

$$
v_\pi(s) = \sum_{a\in\mathcal{A}(s)}\pi(a\mid s)\left[\sum_{r\in\mathcal{R}(s,a)}p(r\mid s,a)r+\gamma\sum_{s'\in\mathcal{S}}p(s'\mid s,a)v_\pi(s')\right].
$$

The first inner sum is the expected immediate reward:

$$
\sum_{r\in\mathcal{R}(s,a)}p(r\mid s,a)r.
$$

The second inner sum is the expected value of the next state:

$$
\sum_{s'\in\mathcal{S}}p(s'\mid s,a)v_\pi(s').
$$

For a fixed policy, define the expected immediate reward as

$$
r_\pi(s) = \sum_{a\in\mathcal{A}(s)}\pi(a\mid s)\sum_{r\in\mathcal{R}(s,a)}p(r\mid s,a)r,
$$

and the state-transition probability under that policy as

$$
p_\pi(s'\mid s) = \sum_{a\in\mathcal{A}(s)}\pi(a\mid s)p(s'\mid s,a).
$$

The Bellman equation can then be written more concisely as

$$
v_\pi(s) = r_\pi(s)+\gamma\sum_{s'\in\mathcal{S}}p_\pi(s'\mid s)v_\pi(s').
$$

For a finite state space, the equations for all states can be combined into the matrix-vector form

$$
\mathbf{v}_\pi = \mathbf{r}_\pi+\gamma\mathbf{P}_\pi\mathbf{v}_\pi.
$$

Its closed-form solution is

$$
\mathbf{v}_\pi = (\mathbf{I}-\gamma\mathbf{P}_\pi)^{-1}\mathbf{r}_\pi.
$$

The state values can alternatively be calculated iteratively:

$$
\mathbf{v}_{k+1} = \mathbf{r}_\pi+\gamma\mathbf{P}_\pi\mathbf{v}_k,
$$

where $\mathbf{v}_0$ is an initial guess. For $\gamma\in(0,1)$, the sequence converges to $\mathbf{v}_\pi$ as $k$ approaches infinity.