## Definition

**n-step Sarsa** is a generalization of [[Sarsa]] that uses $n$ observed rewards before [[Bootstrapping|bootstrapping]] from an estimated action value.

Ordinary Sarsa uses one observed reward and the estimated action value of the next state-action pair. In contrast, n-step Sarsa waits for $n$ transitions and includes all rewards observed during these transitions in its update target.

The parameter $n$ therefore determines how many actual rewards are used before the algorithm bootstraps.

## Mathematical Formulation

The n-step return is

$$
G_t^{(n)}
=
\sum_{i=0}^{n-1}
\gamma^i R_{t+i+1}
+
\gamma^n q_\pi(S_{t+n},A_{t+n}).
$$

A sampled n-step target is

$$
g_t^{(n)}
=
r_{t+1}
+
\gamma r_{t+2}
+
\cdots
+
\gamma^{n-1}r_{t+n}
+
\gamma^n q_t(s_{t+n},a_{t+n}).
$$

The corresponding action-value update is

$$
q(s_t,a_t)
\leftarrow
q(s_t,a_t)
-
\alpha
\left[
q(s_t,a_t)-g_t^{(n)}
\right].
$$

For example, the two-step target is

$$
g_t^{(2)}
=
r_{t+1}
+
\gamma r_{t+2}
+
\gamma^2 q_t(s_{t+2},a_{t+2}).
$$

## Algorithm

To update the action value of $(s_t,a_t)$, the algorithm requires the experience sequence

$$
(
s_t,a_t,r_{t+1},
s_{t+1},a_{t+1},
\ldots,
r_{t+n},s_{t+n},a_{t+n}
).
$$

At time step $t$, the complete sequence is not yet available. The algorithm must therefore wait until time step $t+n$ before updating the action value of $(s_t,a_t)$.

The n-step Sarsa algorithm described here evaluates the action values of a given [[Policy|policy]]. To learn an [[Optimal Policy|optimal policy]], it must be combined with a policy-improvement step.

## Special Cases

When $n=1$, the target becomes

$$
g_t^{(1)}
=
r_{t+1}
+
\gamma q_t(s_{t+1},a_{t+1}),
$$

which is the ordinary [[Sarsa]] target.

When $n$ extends to the end of the episode, no estimated action value is needed after the final reward. The target becomes the complete discounted return:

$$
g_t
=
r_{t+1}
+
\gamma r_{t+2}
+
\gamma^2 r_{t+3}
+
\cdots.
$$

With $n=\infty$ and $\alpha=1$, n-step Sarsa therefore becomes [[Monte Carlo Estimation|Monte Carlo learning]].

## Bias-Variance Tradeoff

A small value of $n$ makes n-step Sarsa similar to ordinary Sarsa. It bootstraps early and generally has lower variance but greater bias.

A large value of $n$ makes the algorithm closer to Monte Carlo learning. It uses more observed rewards and generally has lower bias but greater variance.

The parameter $n$ therefore controls the balance between bootstrapping from current estimates and learning from observed rewards.