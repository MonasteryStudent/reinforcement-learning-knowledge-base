## Definition

**Deterministic actor-critic** combines a deterministic target policy with an action-value critic.

The actor directly produces an action:

$$
a
=
\mu(s,\boldsymbol{\theta}).
$$

The critic approximates the action-value function as

$$
q(s,a,\mathbf{w}).
$$

An exploratory behavior policy $\beta$ generates the actions used to interact with the environment. The deterministic policy $\mu$ is the target policy being evaluated and improved.

The critic estimates how the action value changes with respect to the action. The actor uses this gradient to change its parameters in a direction that increases the critic's estimated action value.

## Mathematical Formulation

The behavior action is sampled according to

$$
a_t
\sim
\beta(\cdot\mid s_t).
$$

After observing $r_{t+1}$ and $s_{t+1}$, the target policy produces the next target action

$$
\tilde{a}_{t+1}
=
\mu(s_{t+1},\boldsymbol{\theta}_t).
$$

This target action is used to calculate the TD target but is not necessarily executed in the environment.

The critic calculates the TD error

$$
\delta_t
=
r_{t+1}
+
\gamma
q\left(
s_{t+1},
\mu(s_{t+1},\boldsymbol{\theta}_t),
\mathbf{w}_t
\right)
-
q(s_t,a_t,\mathbf{w}_t).
$$

The actor update is

$$
\boldsymbol{\theta}_{t+1}
=
\boldsymbol{\theta}_t
+
\alpha_\theta
\nabla_{\boldsymbol{\theta}}
\mu(s_t,\boldsymbol{\theta}_t)
\nabla_a q(s_t,a,\mathbf{w}_t)
\big|_{a=\mu(s_t,\boldsymbol{\theta}_t)}.
$$

The critic update is

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

The actor is off-policy because its gradient does not require actions sampled from the deterministic target policy.

The critic is also off-policy:

- The behavior policy generates the action $a_t$ used to interact with the environment.
- The target policy generates the next action used in the TD target.
- The target action is not used to interact with the environment at the next time step.

No importance weight is required for these updates.

## Algorithm

Initialize an exploratory behavior policy $\beta$, deterministic target-policy parameters $\boldsymbol{\theta}_0$, action-value parameters $\mathbf{w}_0$, and step sizes $\alpha_\theta,\alpha_w>0$.

At every time step:

1. Generate $a_t$ according to the behavior policy $\beta$.
2. Execute $a_t$ and observe $r_{t+1}$ and $s_{t+1}$.
3. Calculate the TD error:

   $$
   \delta_t
   =
   r_{t+1}
   +
   \gamma
   q\left(
   s_{t+1},
   \mu(s_{t+1},\boldsymbol{\theta}_t),
   \mathbf{w}_t
   \right)
   -
   q(s_t,a_t,\mathbf{w}_t).
   $$

4. Update the actor using the deterministic policy gradient.
5. Update the critic using the TD error.
6. Continue with state $s_{t+1}$.

The behavior policy may be any exploratory policy. A common approach is to construct it by adding exploration noise to the action produced by the deterministic policy.

When neural networks are used to represent the actor and critic, this general approach leads to methods such as **deep deterministic policy gradient (DDPG)**.