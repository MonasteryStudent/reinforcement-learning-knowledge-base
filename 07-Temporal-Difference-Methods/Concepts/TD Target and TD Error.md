## Definition

The **TD target** is the value toward which the current [[State Value|state-value estimate]] is moved after observing a transition.

The **TD error** measures the difference between the current state-value estimate and the TD target. It represents the new information obtained from the observed transition.

## Mathematical Formulation

Suppose the agent observes the transition

$$
s_t
\xrightarrow{a_t,\ r_{t+1}}
s_{t+1}.
$$

The TD target is

$$
\bar{v}_t
=
r_{t+1}
+
\gamma v_t(s_{t+1}).
$$

It consists of the observed immediate reward $r_{t+1}$ and the discounted estimate of the next state's value $v_t(s_{t+1})$.

Following Zhao's sign convention, the TD error is

$$
\delta_t
=
v_t(s_t)-\bar{v}_t.
$$

Substituting the TD target gives

$$
\delta_t
=
v_t(s_t)
-
\left[
r_{t+1}
+
\gamma v_t(s_{t+1})
\right].
$$

The [[Temporal-Difference Learning|TD update]] can therefore be written as

$$
v_{t+1}(s_t)
=
v_t(s_t)
-
\alpha_t(s_t)\delta_t.
$$

## Interpretation

The sign of the TD error determines how the current estimate is updated:

- If $\delta_t>0$, the current estimate is greater than the TD target and is decreased.
- If $\delta_t<0$, the current estimate is smaller than the TD target and is increased.
- If $\delta_t=0$, the current estimate already agrees with the TD target and remains unchanged.

The TD target contains the estimated value $v_t(s_{t+1})$. The update therefore uses [[Bootstrapping]].

As the value estimates approach the true state values, the expected TD error approaches zero.