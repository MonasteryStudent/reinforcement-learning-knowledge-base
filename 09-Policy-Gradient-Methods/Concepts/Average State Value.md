## Definition

The **average state value**, also called the **average value**, is a scalar metric that evaluates a [[Policy]] by calculating a weighted average of its [[State Value|state values]].

Each state $s$ is assigned a weight $d(s)$. States with larger weights contribute more strongly to the resulting metric.

The weights may be independent of the policy or determined by the [[Stationary Distribution]] under the policy. The choice of weights therefore determines which states are considered particularly important when optimizing a [[Parameterized Policy]].

## Mathematical Formulation

The average state value of policy $\pi$ is defined as

$$
\bar{v}_\pi
=
\sum_{s\in\mathcal{S}}
d(s)v_\pi(s),
$$

where $d$ is a probability distribution over the state space and therefore satisfies

$$
d(s)\geq 0
$$

for every state $s$, and

$$
\sum_{s\in\mathcal{S}}d(s)=1.
$$

Using a random state $S$ distributed according to $d$, the average state value can equivalently be written as

$$
\bar{v}_\pi
=
\mathbb{E}_{S\sim d}
\left[
v_\pi(S)
\right].
$$

### Policy-independent distribution

The distribution may be selected independently of the policy and denoted by $d_0$.

If all states are considered equally important, a uniform distribution can be used:

$$
d_0(s)
=
\frac{1}{|\mathcal{S}|}.
$$

If the agent always starts from a particular state $s_0$, the distribution can instead be defined as

$$
d_0(s_0)=1
$$

and

$$
d_0(s)=0
\qquad
\text{for }s\neq s_0.
$$

In this case, the average state value reduces to

$$
\bar{v}_\pi
=
v_\pi(s_0).
$$

### Policy-dependent distribution

The distribution may also be selected as the stationary distribution $d_\pi$ under policy $\pi$:

$$
\bar{v}_\pi
=
\sum_{s\in\mathcal{S}}
d_\pi(s)v_\pi(s).
$$

States that are frequently visited in the long term receive larger weights, while rarely visited states receive smaller weights.

### Relation to the expected return

If the initial state is distributed according to $d$, the average state value is equivalent to the expected discounted return:

$$
\bar{v}_\pi
=
\mathbb{E}_\pi
\left[
\sum_{t=0}^{\infty}
\gamma^tR_{t+1}
\right].
$$

For a parameterized policy, this quantity can therefore be used as the objective

$$
J(\boldsymbol{\theta})
=
\bar{v}_{\pi_{\boldsymbol{\theta}}}.
$$

The policy parameters are selected to maximize the average state value:

$$
\boldsymbol{\theta}^*
=
\underset{\boldsymbol{\theta}}{\arg\max}
\ \bar{v}_{\pi_{\boldsymbol{\theta}}}.
$$