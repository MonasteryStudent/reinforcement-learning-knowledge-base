## Definition

A **policy gradient baseline** is a state-dependent scalar function

$$
b(s)
$$

that is subtracted from an action value in a policy-gradient update.

Introducing a baseline does not change the expected policy gradient, provided that the baseline depends on the state but not on the selected action. This property is called **baseline invariance**.

Although the expected gradient remains unchanged, the baseline can reduce the variance of the stochastic gradient estimate. Individual experience samples can then provide more reliable approximations of the true gradient.

Algorithms such as [[REINFORCE]] and [[Q Actor-Critic]] implicitly use the baseline

$$
b(s)=0.
$$

A more useful practical choice is often the [[State Value]]

$$
b(s)=v_\pi(s).
$$

This choice leads to the [[Advantage Function]].

## Mathematical Formulation

According to the [[Policy Gradient Theorem]], the policy gradient can be written as

$$
\nabla_{\boldsymbol{\theta}}J(\boldsymbol{\theta})
=
\mathbb{E}
\left[
\nabla_{\boldsymbol{\theta}}
\ln\pi(A\mid S,\boldsymbol{\theta})
q_\pi(S,A)
\right].
$$

A state-dependent baseline can be subtracted without changing the expected gradient:

$$
\nabla_{\boldsymbol{\theta}}J(\boldsymbol{\theta})
=
\mathbb{E}
\left[
\nabla_{\boldsymbol{\theta}}
\ln\pi(A\mid S,\boldsymbol{\theta})
\left(
q_\pi(S,A)-b(S)
\right)
\right].
$$

This equality holds because the expected contribution of the baseline is zero. For a fixed state $s$,

$$
\mathbb{E}_{A\sim\pi}
\left[
\nabla_{\boldsymbol{\theta}}
\ln\pi(A\mid s,\boldsymbol{\theta})
b(s)
\right]
=
0.
$$

This can be shown by expanding the expectation:

$$
\sum_{a\in\mathcal{A}(s)}
\pi(a\mid s,\boldsymbol{\theta})
\nabla_{\boldsymbol{\theta}}
\ln\pi(a\mid s,\boldsymbol{\theta})
b(s).
$$

Using

$$
\pi(a\mid s,\boldsymbol{\theta})
\nabla_{\boldsymbol{\theta}}
\ln\pi(a\mid s,\boldsymbol{\theta})
=
\nabla_{\boldsymbol{\theta}}
\pi(a\mid s,\boldsymbol{\theta}),
$$

the expression becomes

$$
b(s)
\nabla_{\boldsymbol{\theta}}
\sum_{a\in\mathcal{A}(s)}
\pi(a\mid s,\boldsymbol{\theta}).
$$

Because the action probabilities sum to one,

$$
b(s)\nabla_{\boldsymbol{\theta}}1
=
0.
$$

Therefore, the baseline changes the stochastic gradient obtained from an individual sample but not its expected value.

The variance-minimizing baseline is

$$
b^*(s)
=
\frac{
\mathbb{E}_{A\sim\pi}
\left[
\left\|
\nabla_{\boldsymbol{\theta}}
\ln\pi(A\mid s,\boldsymbol{\theta})
\right\|^2
q_\pi(s,A)
\right]
}{
\mathbb{E}_{A\sim\pi}
\left[
\left\|
\nabla_{\boldsymbol{\theta}}
\ln\pi(A\mid s,\boldsymbol{\theta})
\right\|^2
\right]
}.
$$

Because this expression is difficult to calculate in practice, the state value is commonly used as a simpler baseline:

$$
b(s)
=
v_\pi(s)
=
\mathbb{E}_{A\sim\pi}
\left[
q_\pi(s,A)
\right].
$$