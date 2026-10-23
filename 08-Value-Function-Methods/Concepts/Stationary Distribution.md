## Definition

A **stationary distribution** describes the long-term probabilities of an agent being in the different states of a [[Markov Process]].

For a fixed [[Policy]] $\pi$, let $d_\pi(s)$ denote the long-term probability of the agent being in state $s$. States that are visited more frequently under the policy have larger values of $d_\pi(s)$.

The distribution is called stationary because applying the state-transition probabilities does not change it. Under appropriate conditions, the state distribution converges to $d_\pi$ as the process continues, independently of its initial distribution.

In [[Value Function Approximation]], the stationary distribution can be used to give greater importance to states that are encountered more frequently under the policy.

## Mathematical Formulation

Let $P_\pi$ be the state-transition matrix of the [[Markov Process]] induced by policy $\pi$. Its entries are

$$
[P_\pi]_{ij}
=
p_\pi(s_j\mid s_i).
$$

If $\mathbf{d}_0$ is the initial state distribution, the state distribution after $k$ transitions is

$$
\mathbf{d}_k^T
=
\mathbf{d}_0^T P_\pi^k.
$$

Under appropriate conditions, this distribution converges to the stationary distribution:

$$
\lim_{k\to\infty}\mathbf{d}_k^T
=
\mathbf{d}_\pi^T.
$$

The stationary distribution satisfies

$$
\mathbf{d}_\pi^T
=
\mathbf{d}_\pi^T P_\pi.
$$

Its entries are non-negative and sum to one:

$$
d_\pi(s)\geq 0,
$$

$$
\sum_{s\in\mathcal{S}}d_\pi(s)=1.
$$

Using the stationary distribution, the objective for state-value approximation can be written as

$$
J(\mathbf{w})
=
\sum_{s\in\mathcal{S}}
d_\pi(s)
\left(
v_\pi(s)-\hat{v}(s,\mathbf{w})
\right)^2.
$$

The approximation errors of states with larger stationary probabilities therefore contribute more strongly to the objective.