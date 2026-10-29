## Definition

**Q Actor-Critic (QAC)** is the simplest [[Actor-Critic Methods|actor-critic method]]. It combines a [[Policy Gradient Method|policy-gradient]] actor with a critic that estimates [[Action Value|action values]] using [[Temporal-Difference Learning]] and [[Value Function Approximation]].

The actor represents a [[Parameterized Policy]]

$$
\pi(a\mid s,\boldsymbol{\theta}),
$$

while the critic represents the action-value function as

$$
q(s,a,\mathbf{w}).
$$

The actor uses the critic's current action-value estimate to update the policy. The critic updates its parameters using the one-step [[Sarsa]] [[TD Target and TD Error|TD error]].

QAC is an [[On-Policy and Off-Policy Learning|on-policy]] algorithm because both the current action $a_t$ and the next action $a_{t+1}$ are sampled from the policy that is being evaluated and improved.

The main difference from [[REINFORCE]] is how the action value is estimated. REINFORCE uses [[Monte Carlo Estimation]] based on a complete [[Return|return]], whereas QAC uses a [[Bootstrapping|bootstrapped]] one-step TD estimate.

## Mathematical Formulation

At time step $t$, the actor samples an action according to

$$
a_t
\sim
\pi(\cdot\mid s_t,\boldsymbol{\theta}_t).
$$

After executing $a_t$, the agent observes $r_{t+1}$ and $s_{t+1}$. The next action is also sampled from the current policy:

$$
a_{t+1}
\sim
\pi(\cdot\mid s_{t+1},\boldsymbol{\theta}_t).
$$

The critic calculates the Sarsa TD error

$$
\delta_t
=
r_{t+1}
+
\gamma q(s_{t+1},a_{t+1},\mathbf{w}_t)
-
q(s_t,a_t,\mathbf{w}_t).
$$

The actor updates the policy parameters according to

$$
\boldsymbol{\theta}_{t+1}
=
\boldsymbol{\theta}_t
+
\alpha_\theta
\nabla_{\boldsymbol{\theta}}
\ln\pi(a_t\mid s_t,\boldsymbol{\theta}_t)
q(s_t,a_t,\mathbf{w}_t).
$$

The critic updates the action-value parameters according to

$$
\mathbf{w}_{t+1}
=
\mathbf{w}_t
+
\alpha_w
\delta_t
\nabla_{\mathbf{w}}
q(s_t,a_t,\mathbf{w}_t).
$$

The actor and critic are updated with separate step sizes:

$$
\alpha_\theta>0
\qquad\text{and}\qquad
\alpha_w>0.
$$

## Algorithm

Initialize the policy parameters $\boldsymbol{\theta}_0$ and action-value parameters $\mathbf{w}_0$.

At every time step in each episode:

1. Generate $a_t$ according to the current policy:

   $$
   a_t
   \sim
   \pi(\cdot\mid s_t,\boldsymbol{\theta}_t).
   $$

2. Execute $a_t$ and observe $r_{t+1}$ and $s_{t+1}$.
3. Generate $a_{t+1}$ according to the current policy.
4. Calculate the TD error:

   $$
   \delta_t
   =
   r_{t+1}
   +
   \gamma q(s_{t+1},a_{t+1},\mathbf{w}_t)
   -
   q(s_t,a_t,\mathbf{w}_t).
   $$

5. Update the actor:

   $$
   \boldsymbol{\theta}_{t+1}
   =
   \boldsymbol{\theta}_t
   +
   \alpha_\theta
   \nabla_{\boldsymbol{\theta}}
   \ln\pi(a_t\mid s_t,\boldsymbol{\theta}_t)
   q(s_t,a_t,\mathbf{w}_t).
   $$

6. Update the critic:

   $$
   \mathbf{w}_{t+1}
   =
   \mathbf{w}_t
   +
   \alpha_w
   \delta_t
   \nabla_{\mathbf{w}}
   q(s_t,a_t,\mathbf{w}_t).
   $$

7. Continue with $s_{t+1}$ and $a_{t+1}$.