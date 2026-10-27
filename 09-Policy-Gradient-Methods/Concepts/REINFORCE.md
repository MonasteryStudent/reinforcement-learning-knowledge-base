## Definition

**REINFORCE**, also called **Monte Carlo policy gradient**, is an episodic [[Policy Gradient Method]] that estimates the policy gradient from complete episodes.

The agent generates an episode by following its current [[Parameterized Policy]]. The [[Return|return]] observed after each state-action pair is then used as a Monte Carlo estimate of its [[Action Value]].

REINFORCE is an **on-policy** algorithm because the same policy is used to generate the experience samples and to perform the parameter updates.

The algorithm does not require a model of the environment. However, the complete episode must be generated before the returns can be calculated.

## Mathematical Formulation

Gradient ascent using the true policy gradient would update the parameters according to

$$
\boldsymbol{\theta}_{t+1}
=
\boldsymbol{\theta}_t
+
\alpha
\nabla_{\boldsymbol{\theta}}
J(\boldsymbol{\theta}_t).
$$

According to the [[Policy Gradient Theorem]], the gradient can be expressed as an expectation:

$$
\nabla_{\boldsymbol{\theta}}
J(\boldsymbol{\theta})
=
\mathbb{E}
\left[
\nabla_{\boldsymbol{\theta}}
\ln\pi(A\mid S,\boldsymbol{\theta})
q_\pi(S,A)
\right].
$$

REINFORCE replaces this expectation with a sampled state-action pair and replaces the unknown action value with a Monte Carlo return:

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

For an episode terminating at time step $T$, the return following $(s_t,a_t)$ is

$$
G_t
=
\sum_{k=t+1}^{T}
\gamma^{k-t-1}r_k.
$$

This return serves as the action-value estimate:

$$
q_t(s_t,a_t)
=
G_t.
$$

The parameter update can therefore also be written as

$$
\boldsymbol{\theta}
\leftarrow
\boldsymbol{\theta}
+
\alpha
\nabla_{\boldsymbol{\theta}}
\ln\pi(a_t\mid s_t,\boldsymbol{\theta})
q_t(s_t,a_t).
$$

The sampled return determines how strongly the probability of the sampled action is changed. A positive return moves the parameters in a direction that increases the probability of the action, whereas a negative return moves them in a direction that decreases its probability.

## Algorithm

Initialize the policy parameters $\boldsymbol{\theta}$, the discount rate $\gamma\in(0,1)$, and the step size $\alpha>0$.

For every episode:

1. Generate an episode by following the current policy:

   $$
   (s_0,a_0,r_1,\ldots,s_{T-1},a_{T-1},r_T).
   $$

2. For every time step $t=0,1,\ldots,T-1$:

   - Calculate the return:

     $$
     G_t
     =
     \sum_{k=t+1}^{T}
     \gamma^{k-t-1}r_k.
     $$

   - Update the policy parameters:

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

3. Repeat until a stopping condition is satisfied.

A stopping condition may be a fixed number of episodes or a sufficiently small change in the policy parameters or objective value.