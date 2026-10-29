## Definition

A **deterministic policy gradient** directly optimizes a deterministic policy

$$
a
=
\mu(s,\boldsymbol{\theta}).
$$

Unlike a stochastic policy, which produces a probability distribution over actions, the deterministic policy directly maps each state to a single action.

Deterministic policies are particularly useful for continuous action spaces because the actor can directly produce a continuous action without calculating probabilities for every possible action.

The deterministic policy gradient describes how the policy parameters should change to increase the [[Action Value]] of the action produced by the policy.

## Mathematical Formulation

A deterministic policy is represented as

$$
\mu:\mathcal{S}\rightarrow\mathcal{A}
$$

with

$$
a
=
\mu(s,\boldsymbol{\theta}).
$$

The deterministic policy gradient theorem states that

$$
\nabla_{\boldsymbol{\theta}}J(\boldsymbol{\theta})
=
\sum_{s\in\mathcal{S}}
\eta(s)
\nabla_{\boldsymbol{\theta}}
\mu(s,\boldsymbol{\theta})
\nabla_a q_\mu(s,a)
\big|_{a=\mu(s,\boldsymbol{\theta})},
$$

where $\eta$ is a state distribution.

Equivalently,

$$
\nabla_{\boldsymbol{\theta}}J(\boldsymbol{\theta})
=
\mathbb{E}_{S\sim\eta}
\left[
\nabla_{\boldsymbol{\theta}}
\mu(S,\boldsymbol{\theta})
\nabla_a q_\mu(S,a)
\big|_{a=\mu(S,\boldsymbol{\theta})}
\right].
$$

The two gradient terms have different roles:

- $\nabla_{\boldsymbol{\theta}}\mu(s,\boldsymbol{\theta})$ describes how the policy parameters change the selected action.
- $\nabla_a q_\mu(s,a)$ describes how a change in the action changes its expected return.

Their product applies the chain rule to determine how the policy parameters should change to increase the action value.

A stochastic gradient update using a sampled state $s_t$ is

$$
\boldsymbol{\theta}_{t+1}
=
\boldsymbol{\theta}_t
+
\alpha_\theta
\nabla_{\boldsymbol{\theta}}
\mu(s_t,\boldsymbol{\theta}_t)
\nabla_a q_\mu(s_t,a)
\big|_{a=\mu(s_t,\boldsymbol{\theta}_t)}.
$$

Unlike the stochastic [[Policy Gradient Theorem]], the deterministic gradient contains no action random variable and no logarithm of an action probability. Actions therefore do not have to be sampled from the target policy to estimate this gradient.

As a result, deterministic policy-gradient methods are naturally [[On-Policy and Off-Policy Learning|off-policy]] and can learn from states visited by a different behavior policy.