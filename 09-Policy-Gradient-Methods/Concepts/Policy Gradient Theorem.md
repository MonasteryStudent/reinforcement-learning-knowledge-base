## Definition

The **policy gradient theorem** provides an expression for the gradient of a scalar policy objective

$$
J(\boldsymbol{\theta})
$$

with respect to the parameters of a [[Parameterized Policy]].

The theorem expresses the gradient using the policy gradient at each state-action pair and the corresponding [[Action Value]]. It therefore connects changes in the policy parameters with the expected returns produced by the actions.

This expression is important because it allows the policy gradient to be estimated from experience samples without explicitly differentiating the state distribution.

## Mathematical Formulation

The policy gradient theorem can be written as

$$
\nabla_{\boldsymbol{\theta}}J(\boldsymbol{\theta})
=
\sum_{s\in\mathcal{S}}
\eta(s)
\sum_{a\in\mathcal{A}(s)}
\nabla_{\boldsymbol{\theta}}
\pi(a\mid s,\boldsymbol{\theta})
q_\pi(s,a),
$$

where:

- $J(\boldsymbol{\theta})$ is the scalar policy objective,
- $\eta(s)$ is a state distribution or state-weighting function,
- $\nabla_{\boldsymbol{\theta}}\pi(a\mid s,\boldsymbol{\theta})$ describes how the action probability changes with the policy parameters,
- $q_\pi(s,a)$ is the expected return obtained by taking action $a$ in state $s$ and subsequently following policy $\pi$.

The exact definitions of $J(\boldsymbol{\theta})$ and $\eta$ depend on the selected objective and whether the problem is treated in the discounted or undiscounted setting.

Using the logarithmic derivative identity

$$
\nabla_{\boldsymbol{\theta}}
\ln\pi(a\mid s,\boldsymbol{\theta})
=
\frac{
\nabla_{\boldsymbol{\theta}}
\pi(a\mid s,\boldsymbol{\theta})
}{
\pi(a\mid s,\boldsymbol{\theta})
},
$$

we obtain

$$
\nabla_{\boldsymbol{\theta}}
\pi(a\mid s,\boldsymbol{\theta})
=
\pi(a\mid s,\boldsymbol{\theta})
\nabla_{\boldsymbol{\theta}}
\ln\pi(a\mid s,\boldsymbol{\theta}).
$$

The policy gradient can therefore be expressed as an expectation:

$$
\nabla_{\boldsymbol{\theta}}J(\boldsymbol{\theta})
=
\mathbb{E}_{\substack{
S\sim\eta\\
A\sim\pi(\cdot\mid S,\boldsymbol{\theta})
}}
\left[
\nabla_{\boldsymbol{\theta}}
\ln\pi(A\mid S,\boldsymbol{\theta})
q_\pi(S,A)
\right].
$$

The term

$$
\nabla_{\boldsymbol{\theta}}
\ln\pi(A\mid S,\boldsymbol{\theta})
$$

describes how the parameters must change to alter the probability of the sampled action. The action value

$$
q_\pi(S,A)
$$

weights this change according to the expected return of that action.

Because the logarithm is used, the policy must satisfy

$$
\pi(a\mid s,\boldsymbol{\theta})>0.
$$

This condition can be ensured by using a [[Softmax Policy]].

The expectation form makes it possible to approximate the true gradient using experience samples. This provides the basis for the [[REINFORCE]] algorithm.