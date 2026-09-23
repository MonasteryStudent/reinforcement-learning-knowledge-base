## Definition

**Truncated policy iteration** is a [[Dynamic Programming|dynamic-programming]] algorithm that combines elements of [[Value Iteration]] and [[Policy Iteration]].

Like policy iteration, it alternates between [[Policy Evaluation]] and [[Policy Improvement]]. However, the current policy is not evaluated completely. Instead, only a fixed number of iterative Bellman updates is performed before the policy is improved.

The resulting values are therefore approximations of the state values of the current policy.

## Mathematical Formulation

Let $\pi_k$ be the current policy and let $\mathbf{v}_k$ be the current value estimate.

The truncated policy-evaluation phase starts from the current value estimate:

$$
\mathbf{v}^{(0)}
=
\mathbf{v}_k.
$$

While policy $\pi_k$ remains fixed, the Bellman update is applied $m$ times:

$$
\mathbf{v}^{(j+1)}
=
\mathbf{r}_{\pi_k}
+
\gamma
\mathbf{P}_{\pi_k}
\mathbf{v}^{(j)},
\qquad
j=0,\ldots,m-1.
$$

After $m$ evaluation updates, the result becomes the next value estimate:

$$
\mathbf{v}_{k+1}
=
\mathbf{v}^{(m)}.
$$
These values are then used to calculate the action values

$$
q_k(s,a)
=
r(s,a)
+
\gamma
\sum_{s'\in\mathcal{S}}
p(s'\mid s,a)v_{k+1}(s').
$$

The improved deterministic policy selects an action satisfying

$$
q_k(s,\pi_{k+1}(s))
=
\max_{a\in\mathcal{A}(s)}
q_k(s,a).
$$

A practical stopping condition requires both the value estimates and the policy to be stable:

$$
\left\|
\mathbf{v}_{k+1}
-
\mathbf{v}_k
\right\|_\infty
\leq
\varepsilon
$$

and

$$
\pi_{k+1}
=
\pi_k.
$$

## Algorithm

1. Initialize an arbitrary deterministic policy $\pi_0$ and an arbitrary value estimate $\mathbf{v}_0$.
2. Keep the current policy fixed.
3. Perform $m$ iterative policy-evaluation updates, starting from the current value estimate.
4. Use the resulting approximate values to calculate the action values.
5. Construct a greedy deterministic policy by selecting an action with the greatest action value in every state.
6. Stop when the value estimates have converged and policy improvement no longer changes the policy.
7. Otherwise, continue with the improved policy and the latest value estimate.

The parameter $m$ determines how extensively the current policy is evaluated before it is improved:

- With a small $m$, policy improvement is performed frequently.
- With a large $m$, the evaluation approaches complete policy evaluation.
- With $m=1$, the algorithm is closely related to [[Value Iteration]].
- If policy evaluation is continued until convergence, the algorithm becomes [[Policy Iteration]].