## Definition

The **state value** of a [[State|state]] is the expected [[Return|return]] obtained when the [[Agent|agent]] starts from that state and follows a given [[Policy|policy]].

The state value depends on both the state and the policy. Consequently, the same state can have different values under different policies.

If the policy and the [[Environment|environment]] are deterministic, starting from a state always generates the same [[Trajectory|trajectory]]. In this case, the state value equals the return of that trajectory.

If either the policy or the environment is stochastic, starting from the same state may generate different trajectories and returns. The state value is then the mean of these possible returns.

State values can therefore be used to evaluate a policy: a policy that produces greater state values is considered better.

## Mathematical Formulation

The state-value function under policy $\pi$ is defined as

$$
v_\pi(s) = \mathbb{E}_\pi[G_t \mid S_t=s].
$$

Here,

- $S_t$ is the state random variable at time step $t$,
- $s$ is a particular state,
- $G_t$ is the return random variable,
- $\pi$ is the policy being followed,
- $\mathbb{E}_\pi$ denotes the expectation under policy $\pi$.

The discounted return is

$$
G_t = R_{t+1}+\gamma R_{t+2}+\gamma^2R_{t+3}+\cdots,
$$

where $\gamma\in(0,1)$ is the discount rate.

Although the notation contains the time step $t$, the value $v_\pi(s)$ does not depend on time. Once the policy and system model are fixed, each state has a corresponding state value.