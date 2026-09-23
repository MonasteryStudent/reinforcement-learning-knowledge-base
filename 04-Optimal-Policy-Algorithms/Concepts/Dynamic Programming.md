## Definition

**Dynamic programming (DP)** refers to a collection of model-based methods for solving a [[Markov Decision Process]].

These methods assume that the state-transition probabilities and expected immediate rewards of the environment are known. They use the recursive structure expressed by the [[Bellman Equation]] and reuse the values of possible next states instead of evaluating every complete trajectory separately.

In reinforcement learning, dynamic programming can be used to evaluate a fixed [[Policy]] or to find an [[Optimal Policy]].

## Mathematical Formulation

Suppose that $v_k(s)$ is the current estimate of the value of state $s$. A one-step lookahead gives the estimated [[Action Value]]

$$
q_k(s,a)
=
r(s,a)
+
\gamma
\sum_{s'\in\mathcal{S}}
p(s'\mid s,a)v_k(s'),
$$

where $r(s,a)$ is the expected immediate reward.

For a fixed policy $\pi$, a dynamic-programming update calculates

$$
v_{k+1}(s)
=
\sum_{a\in\mathcal{A}(s)}
\pi(a\mid s)q_k(s,a).
$$

This update is based on the [[Bellman Equation]] and is used for policy evaluation.

To search for an optimal policy, the policy-weighted mean is replaced by a maximization:

$$
v_{k+1}(s)
=
\max_{a\in\mathcal{A}(s)}
q_k(s,a).
$$

This update is based on the [[Bellman Optimality Equation]].

[[Value Iteration]], [[Policy Iteration]], and [[Truncated Policy Iteration]] differ primarily in how they combine these value updates with policy improvement.