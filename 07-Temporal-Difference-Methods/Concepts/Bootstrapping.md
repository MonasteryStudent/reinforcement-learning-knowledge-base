## Definition

**Bootstrapping** means updating an estimate using another existing estimate instead of waiting until the complete outcome is known.

In [[Temporal-Difference Learning]], the estimated [[State Value|state value]] of the current state is updated using the current estimate of the next state's value. The algorithm therefore learns partly from observed experience and partly from its own previous estimates.

Bootstrapping enables value estimates to be updated after every transition and makes learning possible in both episodic and continuing tasks.

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

The estimate $v_t(s_{t+1})$ is used to update the estimate $v_t(s_t)$. The TD update is

$$
v_{t+1}(s_t)
=
v_t(s_t)
-
\alpha_t(s_t)
\left[
v_t(s_t)
-
\left(
r_{t+1}
+
\gamma v_t(s_{t+1})
\right)
\right].
$$

This update uses bootstrapping because the target contains the current estimate

$$
v_t(s_{t+1}).
$$

By contrast, Monte Carlo methods use the complete sampled [[Return|return]]

$$
g_t
=
r_{t+1}
+
\gamma r_{t+2}
+
\gamma^2r_{t+3}
+\cdots
$$

as their target. Since this target contains only observed rewards and no estimated state value, Monte Carlo methods do not use bootstrapping.

Iterative methods based on the [[Bellman Equation]] also use bootstrapping because a new value estimate is calculated from previous value estimates.