## Definition

**Policy improvement** constructs a new [[Policy]] by selecting actions greedily with respect to the [[State Value|state values]] of the current policy.

After [[Policy Evaluation]] has calculated $v_\pi(s)$, the [[Action Value]] of every available action is determined using a one-step lookahead. The improved policy selects an action with the greatest action value in each state.

The policy improvement theorem states that the resulting policy $\pi'$ is at least as good as the original policy $\pi$.

## Mathematical Formulation

Given the state values of policy $\pi$, the action values are

$$
q_\pi(s,a)
=
r(s,a)
+
\gamma
\sum_{s'\in\mathcal{S}}
p(s'\mid s,a)v_\pi(s').
$$

The original state value is the policy-weighted mean of these action values:

$$
v_\pi(s)
=
\sum_{a\in\mathcal{A}(s)}
\pi(a\mid s)q_\pi(s,a).
$$

A greedy deterministic policy $\pi'$ selects an action satisfying

$$
q_\pi(s,\pi'(s))
=
\max_{a\in\mathcal{A}(s)}
q_\pi(s,a).
$$

Because the maximum action value cannot be smaller than the policy-weighted mean,

$$
q_\pi(s,\pi'(s))
\geq
v_\pi(s).
$$

The policy improvement theorem therefore gives

$$
v_{\pi'}(s)
\geq
v_\pi(s)
$$

for every state $s$.

If policy evaluation is exact and policy improvement does not change the selected action in any state, the current policy already selects an action with the greatest action value everywhere. Its state values therefore satisfy the [[Bellman Optimality Equation]], and the policy is an [[Optimal Policy]].

If several actions share the greatest action value, any of them may be selected by the improved deterministic policy.