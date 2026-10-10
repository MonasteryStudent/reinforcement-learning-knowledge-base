## Definition

**Temporal-difference learning**, or **TD learning**, is a model-free approach for estimating the [[State Value|state values]] of a fixed [[Policy|policy]] from sampled transitions.

TD learning updates the value estimate immediately after each transition. It therefore does not require a model of the [[Environment]] or a complete [[Episode|episode]].

The update uses the observed immediate reward together with the current estimate of the next state's value. Since one estimate is updated using another estimate, TD learning uses [[Bootstrapping]].

## Mathematical Formulation

For a fixed policy $\pi$, the state value satisfies the [[Bellman Equation|Bellman expectation equation]]

$$
v_\pi(s)
=
\mathbb{E}_\pi
\left[
R_{t+1}
+
\gamma v_\pi(S_{t+1})
\mid S_t=s
\right].
$$

Suppose the agent observes the transition

$$
s_t
\xrightarrow{a_t,\ r_{t+1}}
s_{t+1}.
$$

The **TD target** is

$$
\bar{v}_t
=
r_{t+1}
+
\gamma v_t(s_{t+1}).
$$

Following Zhao's sign convention, the [[TD Error|TD error]] is

$$
\delta_t
=
v_t(s_t)-\bar{v}_t
=
v_t(s_t)
-
\left[
r_{t+1}
+
\gamma v_t(s_{t+1})
\right].
$$

The value estimate of the visited state is updated according to

$$
v_{t+1}(s_t)
=
v_t(s_t)
-
\alpha_t(s_t)\delta_t.
$$

Equivalently,

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

The estimates of all other states remain unchanged:

$$
v_{t+1}(s)=v_t(s),
\qquad s\neq s_t.
$$

## Properties

TD learning has the following properties:

- It is **model-free** because it learns from sampled transitions.
- It is **incremental** because an update is performed after every transition.
- It can be applied to both episodic and continuing tasks.
- It uses bootstrapping because the TD target contains the current estimate $v_t(s_{t+1})$.
- It generally has lower variance than Monte Carlo estimation because its target depends on fewer random variables.

## Convergence

For a fixed policy $\pi$, the estimates converge to the true state values $v_\pi(s)$ if every state is visited sufficiently often and the step sizes satisfy

$$
\sum_{t=0}^{\infty}\alpha_t(s)=\infty
$$

and

$$
\sum_{t=0}^{\infty}\alpha_t^2(s)<\infty
$$

for every state $s$.

The first condition ensures that learning continues, while the second condition ensures that the updates become sufficiently small for the estimates to stabilize.

## Comparison with Monte Carlo Methods

Both temporal-difference learning and Monte Carlo Methods learn value estimates from experience without requiring a model of the environment. However, they differ in how and when the estimates are updated.

| Temporal-Difference Learning | Monte Carlo Methods |
|---|---|
| Updates value estimates after every transition. | Updates value estimates after a complete episode. |
| Can be applied to episodic and continuing tasks. | Requires complete episodes. |
| Uses the immediate reward and the estimated value of the next state. | Uses the complete sampled return. |
| Uses [[Bootstrapping]]. | Does not use bootstrapping. |
| Requires initial value estimates. | Does not rely on estimates of subsequent state values. |
| Usually has lower variance because the update target contains fewer random variables. | Usually has higher variance because the return contains rewards from the entire remaining episode. |

The TD target is

$$
r_{t+1}+\gamma v_t(s_{t+1}),
$$

whereas the Monte Carlo target is the complete return

$$
g_t
=
r_{t+1}
+
\gamma r_{t+2}
+
\gamma^2r_{t+3}
+\cdots.
$$

TD learning can therefore update its estimate before the final outcome of an episode is known. The cost of this earlier update is that the TD target depends partly on the current value estimate rather than only on observed rewards.