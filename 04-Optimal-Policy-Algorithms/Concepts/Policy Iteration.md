## Definition

**Policy iteration** is a [[Dynamic Programming|dynamic-programming]] algorithm that alternates between [[Policy Evaluation]] and [[Policy Improvement]].

Policy evaluation calculates the state values of the current policy. Policy improvement then constructs a greedy deterministic policy from those values.

These two steps are repeated until policy improvement no longer changes the policy. At that point, the current policy is an [[Optimal Policy]].

## Mathematical Formulation

Let $\pi_k$ be the policy at iteration $k$.

During policy evaluation, the state values of $\pi_k$ are calculated from the [[Bellman Equation]]:

$$
\mathbf{v}_{\pi_k}
=
\mathbf{r}_{\pi_k}
+
\gamma
\mathbf{P}_{\pi_k}
\mathbf{v}_{\pi_k}.
$$

The exact state values can be obtained from

$$
\mathbf{v}_{\pi_k}
=
\left(
\mathbf{I}
-
\gamma\mathbf{P}_{\pi_k}
\right)^{-1}
\mathbf{r}_{\pi_k}.
$$

During policy improvement, the action values are calculated using $\mathbf{v}_{\pi_k}$:

$$
q_{\pi_k}(s,a)
=
r(s,a)
+
\gamma
\sum_{s'\in\mathcal{S}}
p(s'\mid s,a)v_{\pi_k}(s').
$$

The improved deterministic policy $\pi_{k+1}$ selects an action satisfying

$$
q_{\pi_k}(s,\pi_{k+1}(s))
=
\max_{a\in\mathcal{A}(s)}
q_{\pi_k}(s,a).
$$

The improvement theorem guarantees that

$$
v_{\pi_{k+1}}(s)
\geq
v_{\pi_k}(s)
$$

for every state $s$.

If

$$
\pi_{k+1}=\pi_k,
$$

the current policy cannot be improved further and is therefore optimal.

## Algorithm

1. Initialize an arbitrary deterministic policy $\pi_0$.
2. Evaluate the current policy $\pi_k$ by solving its Bellman equation.
3. Calculate the action values using $\mathbf{v}_{\pi_k}$.
4. Construct a greedy deterministic policy $\pi_{k+1}$ by selecting an action with the greatest action value in every state.
5. If $\pi_{k+1}=\pi_k$, return the current state values and policy.
6. Otherwise, replace the current policy with the improved policy and repeat the process.

Unlike [[Value Iteration]], policy iteration separates policy evaluation from policy improvement. Each policy is evaluated completely before the next policy is constructed.