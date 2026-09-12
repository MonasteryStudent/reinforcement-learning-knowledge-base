## Definition

The **optimal state value** of a [[State|state]] is the greatest [[State Value|state value]] that can be achieved among all possible [[Policy|policies]].

It represents the greatest expected [[Return|return]] that the [[Agent|agent]] can obtain when starting from a state and following an optimal policy.

The optimal state value is unique, even though multiple optimal policies may produce it.

## Mathematical Formulation

The optimal state value of state $s$ is

$$
v^*(s)=\max_{\pi\in\Pi}v_\pi(s),
$$

where $\Pi$ is the set of all possible policies.

If $\pi^*$ is an [[Optimal Policy|optimal policy]], then

$$
v^*(s)=v_{\pi^*}(s).
$$

For every state $s$ and every policy $\pi$,

$$
v^*(s)\geq v_\pi(s).
$$

For the complete state-value vectors, this relationship is written as

$$
\mathbf{v}^*=\mathbf{v}_{\pi^*}\geq\mathbf{v}_\pi,
$$

where the inequality is applied elementwise.