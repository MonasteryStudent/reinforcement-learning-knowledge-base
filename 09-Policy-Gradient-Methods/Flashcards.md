## Card 09-001

**Front**

What is a parameterized policy?

**Back**

A parameterized policy represents a policy as a function

$$
\pi(a\mid s,\boldsymbol{\theta}),
$$

where $\boldsymbol{\theta}$ is a parameter vector. The function calculates the probability of selecting action $a$ in state $s$.

**Tags**

09-Policy-Gradient-Methods

## Card 09-002

**Front**

How does a parameterized policy differ from a tabular policy?

**Back**

A tabular policy stores the action probabilities separately for every state.

A parameterized policy calculates the action probabilities using a function. It is updated by changing its parameter vector $\boldsymbol{\theta}$ rather than individual table entries.

**Tags**

09-Policy-Gradient-Methods

## Card 09-003

**Front**

What is a policy gradient method?

**Back**

A policy gradient method directly optimizes a parameterized policy by changing its parameter vector in order to maximize a scalar objective.

It is policy-based because it directly improves the policy instead of deriving it from separately estimated values.

**Tags**

09-Policy-Gradient-Methods

## Card 09-004

**Front**

What is the basic idea of a policy gradient method?

**Back**

The basic procedure is:

1. Define a scalar policy objective $J(\boldsymbol{\theta})$.
2. Calculate or estimate its gradient.
3. Update the policy parameters through gradient ascent.

The parameter update is

$$
\boldsymbol{\theta}_{t+1}
=
\boldsymbol{\theta}_t
+
\alpha
\nabla_{\boldsymbol{\theta}}
J(\boldsymbol{\theta}_t).
$$

**Tags**

09-Policy-Gradient-Methods

## Card 09-005

**Front**

Which scalar metrics can be used to evaluate a parameterized policy?

**Back**

Two important types of metrics are:

- the average state value $\bar{v}_\pi$,
- the average reward $\bar{r}_\pi$.

The average state value can use either a policy-independent state distribution $d_0$ or the stationary distribution $d_\pi$.

**Tags**

09-Policy-Gradient-Methods

## Card 09-006

**Front**

How is the average state value defined?

**Back**

The average state value is the weighted mean of the state values:

$$
\bar{v}_\pi
=
\sum_{s\in\mathcal{S}}
d(s)v_\pi(s).
$$

Equivalently,

$$
\bar{v}_\pi
=
\mathbb{E}_{S\sim d}
\left[
v_\pi(S)
\right].
$$

**Tags**

09-Policy-Gradient-Methods

## Card 09-007

**Front**

What does the distribution $d$ determine in the average state value?

**Back**

The distribution $d$ determines how strongly the value of each state contributes to the average state value.

States with larger probabilities $d(s)$ receive greater weight in the objective.

**Tags**

09-Policy-Gradient-Methods

## Card 09-008

**Front**

How can the state distribution for the average state value be selected?

**Back**

A policy-independent distribution $d_0$ may assign equal importance to all states or focus on a particular starting state.

Alternatively, the stationary distribution $d_\pi$ can be used. It assigns larger weights to states that are visited more frequently in the long term under policy $\pi$.

**Tags**

09-Policy-Gradient-Methods

## Card 09-009

**Front**

How is the average state value related to the expected discounted return?

**Back**

If the initial state is distributed according to $d$, then

$$
\bar{v}_\pi
=
\mathbb{E}_\pi
\left[
\sum_{t=0}^{\infty}
\gamma^tR_{t+1}
\right].
$$

The average state value is therefore the expected discounted return averaged over the initial-state distribution.

**Tags**

09-Policy-Gradient-Methods

## Card 09-010

**Front**

What is the average reward?

**Back**

The average reward is the expected immediate reward obtained in the long run under a policy:

$$
\bar{r}_\pi
=
\sum_{s\in\mathcal{S}}
d_\pi(s)r_\pi(s),
$$

where $d_\pi$ is the stationary distribution and $r_\pi(s)$ is the expected immediate reward in state $s$.

**Tags**

09-Policy-Gradient-Methods

## Card 09-011

**Front**

How is the expected immediate reward $r_\pi(s)$ calculated?

**Back**

The expected immediate reward in state $s$ is the policy-weighted mean of the expected rewards of the available actions:

$$
r_\pi(s)
=
\sum_{a\in\mathcal{A}(s)}
\pi(a\mid s,\boldsymbol{\theta})r(s,a).
$$

Equivalently,

$$
r_\pi(s)
=
\mathbb{E}_{A\sim\pi(\cdot\mid s,\boldsymbol{\theta})}
\left[
r(s,A)
\right].
$$

**Tags**

09-Policy-Gradient-Methods

## Card 09-012

**Front**

How can the average reward be expressed using a long sequence of rewards?

**Back**

The average reward is the expected long-run average of the collected rewards:

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

**Tags**

09-Policy-Gradient-Methods

## Card 09-013

**Front**

How are the average reward and average state value related in the discounted case?

**Back**

When $\gamma<1$ and the stationary distribution is used,

$$
\bar{r}_\pi
=
(1-\gamma)\bar{v}_\pi.
$$

Because $1-\gamma$ is positive and independent of the policy, both metrics are maximized by the same policies.

**Tags**

09-Policy-Gradient-Methods

## Card 09-014

**Front**

What is a softmax policy?

**Back**

A softmax policy converts action preferences into action probabilities:

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

The function $h(s,a,\boldsymbol{\theta})$ represents the preference for selecting action $a$ in state $s$.

**Tags**

09-Policy-Gradient-Methods

## Card 09-015

**Front**

Why is the softmax function suitable for representing a stochastic policy?

**Back**

The softmax function produces action probabilities that satisfy

$$
\pi(a\mid s,\boldsymbol{\theta})>0
$$

and

$$
\sum_{a\in\mathcal{A}(s)}
\pi(a\mid s,\boldsymbol{\theta})
=
1.
$$

Every available action therefore retains a nonzero probability of being selected.

**Tags**

09-Policy-Gradient-Methods

## Card 09-016

**Front**

What is the summation form of the policy gradient theorem?

**Back**

The policy gradient theorem states that

$$
\nabla_{\boldsymbol{\theta}}J(\boldsymbol{\theta})
=
\sum_{s\in\mathcal{S}}
\eta(s)
\sum_{a\in\mathcal{A}(s)}
\nabla_{\boldsymbol{\theta}}
\pi(a\mid s,\boldsymbol{\theta})
q_\pi(s,a).
$$

The exact objective $J(\boldsymbol{\theta})$ and state weighting $\eta$ depend on the selected metric and setting.

**Tags**

09-Policy-Gradient-Methods

## Card 09-017

**Front**

What is the expectation form of the policy gradient theorem?

**Back**

The policy gradient can be expressed as

$$
\nabla_{\boldsymbol{\theta}}J(\boldsymbol{\theta})
=
\mathbb{E}_{S\sim\eta,\ A\sim\pi(\cdot\mid S,\boldsymbol{\theta})}
\left[
\nabla_{\boldsymbol{\theta}}
\ln\pi(A\mid S,\boldsymbol{\theta})
q_\pi(S,A)
\right].
$$

This form allows the true gradient to be approximated using experience samples.

**Tags**

09-Policy-Gradient-Methods

## Card 09-018

**Front**

Why does the natural logarithm appear in the policy gradient theorem?

**Back**

The logarithmic derivative identity is

$$
\nabla_{\boldsymbol{\theta}}
\ln\pi(a\mid s,\boldsymbol{\theta})
=
\frac{
\nabla_{\boldsymbol{\theta}}
\pi(a\mid s,\boldsymbol{\theta})
}{
\pi(a\mid s,\boldsymbol{\theta})
}.
$$

Therefore,

$$
\nabla_{\boldsymbol{\theta}}
\pi(a\mid s,\boldsymbol{\theta})
=
\pi(a\mid s,\boldsymbol{\theta})
\nabla_{\boldsymbol{\theta}}
\ln\pi(a\mid s,\boldsymbol{\theta}).
$$

This identity allows the policy gradient to be written as an expectation and estimated from samples.

**Tags**

09-Policy-Gradient-Methods

## Card 09-019

**Front**

What is REINFORCE?

**Back**

REINFORCE is an episodic Monte Carlo policy gradient algorithm.

It generates complete episodes with the current policy and uses the observed returns as estimates of the action values required for the policy-gradient update.

REINFORCE is on-policy because the policy being optimized also generates the experience samples.

**Tags**

09-Policy-Gradient-Methods

## Card 09-020

**Front**

How does REINFORCE update the policy parameters?

**Back**

For an episode terminating at time step $T$, the Monte Carlo action-value estimate is

$$
q_t(s_t,a_t)
=
G_t
=
\sum_{k=t+1}^{T}
\gamma^{k-t-1}r_k.
$$

The policy parameters are updated according to

$$
\boldsymbol{\theta}
\leftarrow
\boldsymbol{\theta}
+
\alpha
\nabla_{\boldsymbol{\theta}}
\ln\pi(a_t\mid s_t,\boldsymbol{\theta})
G_t.
$$

The update is performed for every state-action pair in the generated episode.

**Tags**

09-Policy-Gradient-Methods