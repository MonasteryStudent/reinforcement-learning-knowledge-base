## Definition

**Sarsa** is a model-free [[Temporal-Difference Learning|temporal-difference learning]] algorithm that directly estimates the [[Action Value|action values]] of a policy.

The name Sarsa refers to the five elements required for an update:

$$
(s_t,a_t,r_{t+1},s_{t+1},a_{t+1}),
$$

which represent state, action, reward, next state, and next action.

For a fixed policy $\pi$, Sarsa estimates the action value $q_\pi(s,a)$. By combining action-value estimation with policy improvement, Sarsa can also be used to learn an [[Optimal Policy|optimal policy]].

## Mathematical Formulation

At time step $t$, Sarsa updates the action-value estimate of the visited state-action pair according to

$$
q_{t+1}(s_t,a_t)
=
q_t(s_t,a_t)
-
\alpha_t(s_t,a_t)
\left[
q_t(s_t,a_t)
-
\left(
r_{t+1}
+
\gamma q_t(s_{t+1},a_{t+1})
\right)
\right].
$$

The action values of all other state-action pairs remain unchanged:

$$
q_{t+1}(s,a)=q_t(s,a),
\qquad
(s,a)\neq(s_t,a_t).
$$

The Sarsa TD target is

$$
r_{t+1}+\gamma q_t(s_{t+1},a_{t+1}).
$$

Using the sign convention from [[TD Target and TD Error]], the corresponding TD error is

$$
\delta_t
=
q_t(s_t,a_t)
-
\left[
r_{t+1}
+
\gamma q_t(s_{t+1},a_{t+1})
\right].
$$

Therefore, the update can be written as

$$
q_{t+1}(s_t,a_t)
=
q_t(s_t,a_t)
-
\alpha_t(s_t,a_t)\delta_t.
$$

Sarsa is a stochastic-approximation method for solving the action-value form of the [[Bellman Equation]]:

$$
q_\pi(s,a)
=
\mathbb{E}_\pi
\left[
R_{t+1}
+
\gamma q_\pi(S_{t+1},A_{t+1})
\mid
S_t=s,A_t=a
\right].
$$

## Algorithm

To learn an optimal policy, Sarsa combines action-value estimation with $\varepsilon$-greedy policy improvement.

1. Initialize the action-value estimates $q_0(s,a)$.
2. Derive an initial [[Epsilon-Greedy Policy]] from these estimates.
3. At the beginning of an episode, select an initial action $a_0$ according to the current policy.
4. For every time step:
   - Execute $a_t$ in $s_t$.
   - Observe the reward $r_{t+1}$ and next state $s_{t+1}$.
   - Select $a_{t+1}$ according to the current policy.
   - Update $q_t(s_t,a_t)$ using the Sarsa update.
   - Update the policy at $s_t$ so that it is $\varepsilon$-greedy with respect to the new action-value estimates.
   - Continue with $s_{t+1}$ and $a_{t+1}$.

If $a^*$ is a greedy action,

$$
a^*
=
\underset{a\in\mathcal{A}(s)}{\arg\max}\ q(s,a),
$$

then the $\varepsilon$-greedy policy is

$$
\pi(a\mid s)
=
\begin{cases}
1-\varepsilon+\dfrac{\varepsilon}{|\mathcal{A}(s)|},
& a=a^*,\\
\dfrac{\varepsilon}{|\mathcal{A}(s)|},
& a\neq a^*.
\end{cases}
$$

The policy is improved immediately after updating a visited state-action pair. It is therefore not necessary to evaluate the current policy completely before improving it. This follows the idea of generalized policy iteration.

## Convergence

For a fixed policy $\pi$, the Sarsa estimates converge almost surely to $q_\pi(s,a)$ if the learning rates satisfy

$$
\sum_{t=0}^{\infty}\alpha_t(s,a)=\infty
$$

and

$$
\sum_{t=0}^{\infty}\alpha_t^2(s,a)<\infty
$$

for every state-action pair $(s,a)$.

The first condition requires every state-action pair to be visited sufficiently often. The second condition ensures that the learning rates eventually become small enough for the estimates to stabilize.