## Definition

A **softmax policy** converts numerical action preferences into a probability distribution over the available actions.

The preference function

$$
h(s,a,\boldsymbol{\theta})
$$

indicates how strongly the policy favors action $a$ in state $s$. A larger preference produces a larger action probability, but the preference itself is not a probability and may take any real value.

The softmax function transforms these preferences into strictly positive probabilities whose sum equals one. The resulting policy is stochastic and therefore continues to explore every available action.

A softmax policy does not directly specify a single action. Instead, the agent samples an action from the probability distribution produced by the policy.

## Mathematical Formulation

The probability of selecting action $a$ in state $s$ is

$$
\pi(a\mid s,\boldsymbol{\theta})
=
\frac{
\exp\left(h(s,a,\boldsymbol{\theta})\right)
}{
\displaystyle
\sum_{a'\in\mathcal{A}(s)}
\exp\left(h(s,a',\boldsymbol{\theta})\right)
}.
$$

The action $a'$ in the denominator is a summation variable. The denominator includes the exponentiated preferences of all actions available in state $s$.

Because the exponential function is always positive,

$$
\pi(a\mid s,\boldsymbol{\theta})>0
$$

for every available action. The probabilities are normalized because

$$
\sum_{a\in\mathcal{A}(s)}
\pi(a\mid s,\boldsymbol{\theta})
=
1.
$$

An action is sampled according to this distribution:

$$
A_t
\sim
\pi(\cdot\mid s_t,\boldsymbol{\theta}).
$$

The strict positivity of the action probabilities also ensures that

$$
\ln\pi(a\mid s,\boldsymbol{\theta})
$$

is defined for every available action. This property is required by the expectation form of the [[Policy Gradient Theorem]].

A softmax policy can be represented by a neural network. The state is provided as the network input, and a softmax output layer produces one probability for every available action.