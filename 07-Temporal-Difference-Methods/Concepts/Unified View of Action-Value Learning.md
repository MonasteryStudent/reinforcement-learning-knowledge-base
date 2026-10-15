## Definition

The principal model-free action-value learning algorithms share a common update structure. They differ primarily in how they construct the target toward which the current action-value estimate is updated.

This unified view connects [[Monte Carlo Estimation]], [[Sarsa]], [[Expected Sarsa]], [[n-step Sarsa]], and [[Q-Learning]].

Monte Carlo methods use a complete observed return as their target. Temporal-difference methods combine observed rewards with current value estimates through [[Bootstrapping]].

## Mathematical Formulation

A general action-value update can be written as

$$
q_{t+1}(s_t,a_t)
=
q_t(s_t,a_t)
-
\alpha_t(s_t,a_t)
\left[
q_t(s_t,a_t)-\bar{q}_t
\right],
$$

where $\bar{q}_t$ denotes the learning target.

Equivalently, the current estimate is moved toward the target:

$$
q_{t+1}(s_t,a_t)
=
q_t(s_t,a_t)
+
\alpha_t(s_t,a_t)
\left[
\bar{q}_t-q_t(s_t,a_t)
\right].
$$

The term

$$
\bar{q}_t-q_t(s_t,a_t)
$$

is the error between the target and the current estimate. The different algorithms are obtained by using different targets.

### Monte Carlo

Monte Carlo learning uses the complete return observed from time step $t$ until the end of the episode:

$$
\bar{q}_t
=
g_t
=
\sum_{i=t}^{T-1}\gamma^{i-t}r_{i+1}.
$$

It does not bootstrap from another action-value estimate.

### Sarsa

[[Sarsa]] uses the reward and the estimated value of the action actually selected in the next state:

$$
\bar{q}_t
=
r_{t+1}
+
\gamma q_t(s_{t+1},a_{t+1}).
$$

### Expected Sarsa

[[Expected Sarsa]] replaces the value of one sampled next action with the policy-weighted mean of all available next-action values:

$$
\bar{q}_t
=
r_{t+1}
+
\gamma
\sum_{a\in\mathcal{A}(s_{t+1})}
\pi_t(a\mid s_{t+1})
q_t(s_{t+1},a).
$$

### n-step Sarsa

[[n-step Sarsa]] uses $n$ observed rewards before bootstrapping from a later action-value estimate:

$$
\bar{q}_t
=
\sum_{i=0}^{n-1}\gamma^i r_{t+i+1}
+
\gamma^n q_t(s_{t+n},a_{t+n}).
$$

The parameter $n$ determines the position between one-step Sarsa and Monte Carlo learning.

### Q-Learning

[[Q-Learning]] uses the greatest estimated action value available in the next state:

$$
\bar{q}_t
=
r_{t+1}
+
\gamma
\max_{a\in\mathcal{A}(s_{t+1})}
q_t(s_{t+1},a).
$$

Its target is independent of the action actually selected by the behavior policy.

## Comparison

| Algorithm | Observed rewards before bootstrapping | Bootstrap value | Policy relationship |
|---|---:|---|---|
| Monte Carlo | All remaining rewards | None | On-policy as introduced |
| Sarsa | One | Selected next-action value | On-policy |
| Expected Sarsa | One | Expected next-action value | On-policy as introduced |
| n-step Sarsa | $n$ | Selected action value after $n$ steps | On-policy |
| Q-Learning | One | Greatest next-action value | Off-policy |

Monte Carlo learning, Sarsa, Expected Sarsa, and n-step Sarsa estimate action values associated with a policy and are connected to the [[Bellman Equation]].

Q-learning instead directly estimates optimal action values and is connected to the [[Bellman Optimality Equation]].

The choice of target therefore determines how much observed experience is used, where bootstrapping occurs, and whether the algorithm learns about the behavior policy or a different target policy. These distinctions are also related to [[On-Policy and Off-Policy Learning]] and [[Online and Offline Learning]].