## Definition

The **average reward** is a scalar metric that evaluates a [[Policy]] through the expected immediate reward obtained in the long run.

It weights the expected immediate reward of every state by the [[Stationary Distribution]] $d_\pi$ under policy $\pi$. States that are visited more frequently in the long term therefore contribute more strongly to the metric.

Unlike the discounted return, the long-run average reward does not discount rewards according to when they occur. It is particularly suitable for continuing tasks in which the interaction between the agent and the environment does not terminate.

## Mathematical Formulation

The expected immediate reward in state $s$ under policy $\pi$ is

$$
r_\pi(s)
=
\sum_{a\in\mathcal{A}(s)}
\pi(a\mid s,\boldsymbol{\theta})r(s,a),
$$

where

$$
r(s,a)
=
\mathbb{E}[R\mid s,a]
$$

is the expected immediate reward for state-action pair $(s,a)$.

Equivalently,

$$
r_\pi(s)
=
\mathbb{E}_{A\sim\pi(\cdot\mid s,\boldsymbol{\theta})}
\left[
r(s,A)
\right].
$$

The average reward is defined as

$$
\bar{r}_\pi
=
\sum_{s\in\mathcal{S}}
d_\pi(s)r_\pi(s),
$$

where $d_\pi$ is the stationary distribution under policy $\pi$.

Using a random state $S$ distributed according to $d_\pi$, this can be written as

$$
\bar{r}_\pi
=
\mathbb{E}_{S\sim d_\pi}
\left[
r_\pi(S)
\right].
$$

The average reward is also equivalent to the expected long-run average of the collected rewards:

$$
\bar{r}_\pi
=
\lim_{n\to\infty}
\frac{1}{n}
\mathbb{E}_\pi
\left[
\sum_{t=0}^{n-1}
R_{t+1}
\right].
$$

For a [[Parameterized Policy]], the average reward can be used as the objective

$$
J(\boldsymbol{\theta})
=
\bar{r}_{\pi_{\boldsymbol{\theta}}}.
$$

The objective is to find parameters that maximize the long-run average reward:

$$
\boldsymbol{\theta}^*
=
\underset{\boldsymbol{\theta}}{\arg\max}
\ \bar{r}_{\pi_{\boldsymbol{\theta}}}.
$$

In the discounted case with $\gamma<1$, the average reward and the [[Average State Value]] under the stationary distribution satisfy

$$
\bar{r}_\pi
=
(1-\gamma)\bar{v}_\pi.
$$

Because the factor $1-\gamma$ is positive and independent of the policy, maximizing either metric produces the same optimal policy.