## Definition

The **advantage function** measures how much better or worse an action is than the average action selected by a [[Policy]] in the same state.

It is defined as the difference between the [[Action Value]] of a particular action and the [[State Value]]:

$$
\delta_\pi(s,a)
=
q_\pi(s,a)
-
v_\pi(s).
$$

The state value is the policy-weighted mean of the available action values. The advantage therefore evaluates an action relative to the policy's usual behavior in that state rather than according to its absolute action value.

The advantage has the following interpretation:

- If $\delta_\pi(s,a)>0$, action $a$ is better than the policy's average action in state $s$.
- If $\delta_\pi(s,a)<0$, action $a$ is worse than the policy's average action in state $s$.
- If $\delta_\pi(s,a)=0$, the action value equals the state value.

Zhao denotes the advantage function by $\delta_\pi(s,a)$. The same symbol is also commonly used for the TD error because the TD error can be used to approximate the advantage.

## Mathematical Formulation

The state value under policy $\pi$ is the policy-weighted mean of the action values:

$$
v_\pi(s)
=
\sum_{a\in\mathcal{A}(s)}
\pi(a\mid s)q_\pi(s,a).
$$

The advantage function is

$$
\delta_\pi(s,a)
=
q_\pi(s,a)-v_\pi(s).
$$

The expected advantage of actions sampled from the policy is zero:

$$
\mathbb{E}_{A\sim\pi(\cdot\mid s)}
\left[
\delta_\pi(s,A)
\right]
=
0.
$$

This follows from

$$
\sum_{a\in\mathcal{A}(s)}
\pi(a\mid s)
\left[
q_\pi(s,a)-v_\pi(s)
\right]
=
v_\pi(s)-v_\pi(s)
=
0.
$$

When the state value is used as a [[Policy Gradient Baseline]], the policy gradient becomes

$$
\nabla_{\boldsymbol{\theta}}
J(\boldsymbol{\theta})
=
\mathbb{E}
\left[
\nabla_{\boldsymbol{\theta}}
\ln\pi(A\mid S,\boldsymbol{\theta})
\delta_\pi(S,A)
\right].
$$

In practice, the exact action and state values are usually unknown. [[Advantage Actor-Critic]] therefore approximates the advantage using a one-step TD error:

$$
\delta_\pi(s_t,a_t)
\approx
r_{t+1}
+
\gamma v(s_{t+1},\mathbf{w}_t)
-
v(s_t,\mathbf{w}_t).
$$