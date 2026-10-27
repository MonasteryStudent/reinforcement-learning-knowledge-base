## Definition

A **parameterized policy** represents a [[Policy]] as a function

$$
\pi(a\mid s,\boldsymbol{\theta}),
$$

where $\boldsymbol{\theta}\in\mathbb{R}^m$ is a parameter vector.

In a tabular policy, the action probabilities are stored separately for every state. In a parameterized policy, the probability of selecting action $a$ in state $s$ is calculated by evaluating the policy function.

Depending on its structure, the function may receive a state-action pair $(s,a)$ and return the corresponding action probability, or receive a state $s$ and return the probabilities of all available actions.

The policy is updated by changing the parameter vector $\boldsymbol{\theta}$ rather than individual table entries. Because the parameters can be shared across states and actions, a parameterized policy can generalize and is better suited to large or continuous state and action spaces.

## Mathematical Formulation

For every state $s$, a parameterized stochastic policy must satisfy

$$
\pi(a\mid s,\boldsymbol{\theta})\geq 0
$$

for every available action $a\in\mathcal{A}(s)$, and

$$
\sum_{a\in\mathcal{A}(s)}
\pi(a\mid s,\boldsymbol{\theta})
=
1.
$$

A scalar metric

$$
J(\boldsymbol{\theta})
$$

is used to evaluate the policy represented by $\boldsymbol{\theta}$. The parameters can be updated through gradient ascent:

$$
\boldsymbol{\theta}_{t+1}
=
\boldsymbol{\theta}_t
+
\alpha
\nabla_{\boldsymbol{\theta}}
J(\boldsymbol{\theta}_t),
$$

where $\alpha>0$ is the optimization step size and

$$
\nabla_{\boldsymbol{\theta}}J(\boldsymbol{\theta}_t)
$$

is the gradient of the metric with respect to the policy parameters.

The objective is to find parameters $\boldsymbol{\theta}^*$ that maximize the selected metric:

$$
\boldsymbol{\theta}^*
=
\underset{\boldsymbol{\theta}}{\arg\max}
\ J(\boldsymbol{\theta}).
$$