## Definition

An **actor-critic method** combines a policy-based component with a value-based component.

The **actor** represents and updates a [[Parameterized Policy]]. It is called the actor because the agent selects its actions according to this policy.

The **critic** estimates the values associated with the actor's policy. It evaluates the actions taken by the actor and provides a learning signal for the policy update. The critic may estimate [[State Value|state values]] or [[Action Value|action values]] using [[Temporal-Difference Learning]] and [[Value Function Approximation]].

Actor-critic methods are still [[Policy Gradient Method|policy gradient methods]]. Their distinguishing feature is that the value required by the policy-gradient update is estimated through TD learning.

If the action value is estimated from complete returns using Monte Carlo learning, the resulting algorithm is [[REINFORCE]]. If it is estimated using TD learning, the resulting method is generally called actor-critic.

## Mathematical Formulation

The actor represents a stochastic policy as

$$
\pi(a\mid s,\boldsymbol{\theta}),
$$

where $\boldsymbol{\theta}$ is the actor parameter vector.

The critic represents a value function using a separate parameter vector $\mathbf{w}$. Depending on the algorithm, this may be an action-value approximation

$$
q(s,a,\mathbf{w})
$$

or a state-value approximation

$$
v(s,\mathbf{w}).
$$

A general stochastic policy-gradient update has the form

$$
\boldsymbol{\theta}_{t+1}
=
\boldsymbol{\theta}_t
+
\alpha_\theta
\nabla_{\boldsymbol{\theta}}
\ln\pi(a_t\mid s_t,\boldsymbol{\theta}_t)
q_t(s_t,a_t),
$$

where $q_t(s_t,a_t)$ is an estimate of the action value supplied by the critic.

The actor and critic therefore have different roles and parameters:

- $\boldsymbol{\theta}$ determines the policy used to select actions.
- $\mathbf{w}$ determines the value approximation used to evaluate the policy.
- $\alpha_\theta$ is the actor step size.
- $\alpha_w$ is the critic step size.

The critic uses observed transitions to update its value estimate through a TD error. The resulting estimate is then used by the actor to update the policy parameters.

## Algorithm

Initialize the actor parameters $\boldsymbol{\theta}_0$ and critic parameters $\mathbf{w}_0$.

At every time step:

1. The actor selects action $a_t$ according to

   $$
   a_t
   \sim
   \pi(\cdot\mid s_t,\boldsymbol{\theta}_t).
   $$

2. The agent executes the action and observes reward $r_{t+1}$ and next state $s_{t+1}$.
3. The critic calculates a TD error and updates the value parameters $\mathbf{w}$.
4. The actor uses the critic's value estimate or TD error to update the policy parameters $\boldsymbol{\theta}$.
5. Continue until a stopping condition is satisfied.

The particular value representation and update signal distinguish algorithms such as [[Q Actor-Critic]] and [[Advantage Actor-Critic]].