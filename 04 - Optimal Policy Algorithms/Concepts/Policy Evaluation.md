## Definition

**Policy evaluation** determines the [[State Value]] of every state under a fixed [[Policy]] $\pi$.

The resulting value $v_\pi(s)$ is the expected return obtained when the agent starts in state $s$ and follows policy $\pi$ thereafter. During policy evaluation, the policy remains unchanged.

Policy evaluation can be performed by solving the [[Bellman Equation]] directly or by applying iterative Bellman updates until the state values converge.

## Mathematical Formulation

For a fixed policy $\pi$, the expected immediate reward is

$$
r_\pi(s)
=
\sum_{a\in\mathcal{A}(s)}
\pi(a\mid s)r(s,a),
$$

and the corresponding state-transition probability is

$$
p_\pi(s'\mid s)
=
\sum_{a\in\mathcal{A}(s)}
\pi(a\mid s)p(s'\mid s,a).
$$

The state values satisfy the Bellman equation

$$
v_\pi(s)
=
r_\pi(s)
+
\gamma
\sum_{s'\in\mathcal{S}}
p_\pi(s'\mid s)v_\pi(s').
$$

In matrix-vector form,

$$
\mathbf{v}_\pi
=
\mathbf{r}_\pi
+
\gamma
\mathbf{P}_\pi
\mathbf{v}_\pi.
$$

The exact solution is therefore

$$
\mathbf{v}_\pi
=
\left(
\mathbf{I}
-
\gamma\mathbf{P}_\pi
\right)^{-1}
\mathbf{r}_\pi.
$$

Instead of solving the equation directly, the values can be calculated iteratively:

$$
\mathbf{v}_{j+1}
=
\mathbf{r}_\pi
+
\gamma
\mathbf{P}_\pi
\mathbf{v}_j.
$$

For $\gamma\in(0,1)$, these estimates converge to $\mathbf{v}_\pi$.

[[Policy Iteration]] evaluates the current policy completely before improving it. [[Truncated Policy Iteration]] performs only a fixed number of these iterative evaluation updates.