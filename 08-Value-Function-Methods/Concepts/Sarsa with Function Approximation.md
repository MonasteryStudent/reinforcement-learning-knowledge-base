## Definition

**Sarsa with function approximation** extends [[Sarsa]] by representing the action-value function with a parameterized function

$$
\hat{q}(s,a,\mathbf{w})
$$

instead of a table containing a separate value for every state-action pair.

The algorithm remains [[On-Policy and Off-Policy Learning|on-policy]]: the next action $a_{t+1}$ is selected according to the same policy that is evaluated and improved. Each experience sample

$$
(s_t,a_t,r_{t+1},s_{t+1},a_{t+1})
$$

is used to update the parameter vector $\mathbf{w}_t$.

Because multiple action-value estimates can depend on the same parameters, updating $\mathbf{w}$ for one state-action pair may also change the estimates of other state-action pairs.

After the action-value update, the policy is improved toward an [[Epsilon-Greedy Policy]] with respect to the updated action-value approximation.

## Mathematical Formulation

For a given policy $\pi$, the true action value is approximated by

$$
q_\pi(s,a)
\approx
\hat{q}(s,a,\mathbf{w}).
$$

The one-step Sarsa [[TD Target and TD Error|TD target]] is

$$
r_{t+1}
+
\gamma\hat{q}(s_{t+1},a_{t+1},\mathbf{w}_t).
$$

The parameter update is

$$
\mathbf{w}_{t+1}
=
\mathbf{w}_t
+
\alpha_t
\left[
r_{t+1}
+
\gamma\hat{q}(s_{t+1},a_{t+1},\mathbf{w}_t)
-
\hat{q}(s_t,a_t,\mathbf{w}_t)
\right]
\nabla_{\mathbf{w}}
\hat{q}(s_t,a_t,\mathbf{w}_t).
$$

For [[Linear Function Approximation]], the action-value estimate is

$$
\hat{q}(s,a,\mathbf{w})
=
\boldsymbol{\phi}^{T}(s,a)\mathbf{w},
$$

and its gradient is

$$
\nabla_{\mathbf{w}}
\hat{q}(s,a,\mathbf{w})
=
\boldsymbol{\phi}(s,a).
$$

The parameter update therefore becomes

$$
\mathbf{w}_{t+1}
=
\mathbf{w}_t
+
\alpha_t
\left[
r_{t+1}
+
\gamma
\boldsymbol{\phi}^{T}(s_{t+1},a_{t+1})\mathbf{w}_t
-
\boldsymbol{\phi}^{T}(s_t,a_t)\mathbf{w}_t
\right]
\boldsymbol{\phi}(s_t,a_t).
$$

After the parameter update, a greedy action for the current state is

$$
a^*
=
\underset{a\in\mathcal{A}(s_t)}
{\arg\max}
\ \hat{q}(s_t,a,\mathbf{w}_{t+1}).
$$

The policy for the current state is updated according to

$$
\pi_{t+1}(a\mid s_t)
=
\begin{cases}
1-\varepsilon+\dfrac{\varepsilon}{|\mathcal{A}(s_t)|},
& a=a^*,\\
\dfrac{\varepsilon}{|\mathcal{A}(s_t)|},
& a\neq a^*.
\end{cases}
$$

## Algorithm

Initialize the parameter vector $\mathbf{w}_0$ and an initial policy $\pi_0$.

For every episode:

1. Select the initial action $a_0$ according to $\pi_0(\cdot\mid s_0)$.
2. For every transition until the target state is reached:

   - Execute $a_t$ and observe $r_{t+1}$ and $s_{t+1}$.
   - Select $a_{t+1}$ according to $\pi_t(\cdot\mid s_{t+1})$.
   - Update the parameter vector $\mathbf{w}_{t+1}$.
   - Make the policy for $s_t$ $\varepsilon$-greedy with respect to $\hat{q}(s_t,a,\mathbf{w}_{t+1})$.
   - Set $s_t\leftarrow s_{t+1}$ and $a_t\leftarrow a_{t+1}$.

The action values are represented by a function, but the policy may still be represented as a table. In that case, the method continues to require a finite state and action space for its policy representation.