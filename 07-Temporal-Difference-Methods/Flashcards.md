## Card 07-001

**Front**

What is temporal-difference learning?

**Back**

Temporal-difference learning is a model-free approach that learns value estimates from sampled transitions.

It updates an estimate after every transition by combining the observed immediate reward with the current value estimate of the next state.

**Tags**

07-Temporal-Difference-Methods

## Card 07-002

**Front**

Write the temporal-difference update for the state value of the visited state.

**Back**

For the observed transition from $s_t$ to $s_{t+1}$ with reward $r_{t+1}$, the update is

$$
v_{t+1}(s_t)=v_t(s_t)-\alpha_t(s_t)\left[v_t(s_t)-\left(r_{t+1}+\gamma v_t(s_{t+1})\right)\right].
$$

The estimates of all other states remain unchanged.

**Tags**

07-Temporal-Difference-Methods

## Card 07-003

**Front**

What is the TD target for state-value learning?

**Back**

The TD target is

$$
\bar{v}_t=r_{t+1}+\gamma v_t(s_{t+1}).
$$

It consists of the observed immediate reward and the discounted current estimate of the next state's value.

**Tags**

07-Temporal-Difference-Methods

## Card 07-004

**Front**

How does Zhao define the TD error?

**Back**

Zhao defines the TD error as the current state-value estimate minus the TD target:

$$
\delta_t=v_t(s_t)-\bar{v}_t.
$$

Therefore,

$$
\delta_t=v_t(s_t)-\left[r_{t+1}+\gamma v_t(s_{t+1})\right].
$$

**Tags**

07-Temporal-Difference-Methods

## Card 07-005

**Front**

How does the sign of the TD error affect the state-value update?

**Back**

Following Zhao's definition:

- If $\delta_t>0$, the current estimate is greater than the TD target and is decreased.
- If $\delta_t<0$, the current estimate is smaller than the TD target and is increased.
- If $\delta_t=0$, the current estimate agrees with the TD target and remains unchanged.

As the estimates approach the true state values, the expected TD error approaches zero.

**Tags**

07-Temporal-Difference-Methods

## Card 07-006

**Front**

What is bootstrapping in reinforcement learning?

**Back**

Bootstrapping means updating an estimate using another existing estimate.

TD learning uses bootstrapping because the update of $v_t(s_t)$ uses the current estimate of the next state's value:

$$
v_t(s_{t+1}).
$$

**Tags**

07-Temporal-Difference-Methods

## Card 07-007

**Front**

What are the main differences between temporal-difference learning and Monte Carlo methods?

**Back**

Temporal-difference learning:

- updates after every transition,
- uses bootstrapping,
- can learn from incomplete episodes,
- can be applied to episodic and continuing tasks.

Monte Carlo methods:

- update after a complete episode,
- use the complete sampled return,
- do not use bootstrapping,
- require episodic experience.

**Tags**

07-Temporal-Difference-Methods

## Card 07-008

**Front**

Under what conditions do TD state-value estimates converge to the true state values of a fixed policy?

**Back**

Every state must be visited sufficiently often, and the step sizes must satisfy

$$
\sum_{t=0}^{\infty}\alpha_t(s)=\infty
$$

and

$$
\sum_{t=0}^{\infty}\alpha_t^2(s)<\infty
$$

for every state $s$.

The first condition ensures that learning continues. The second ensures that the updates eventually become sufficiently small.

**Tags**

07-Temporal-Difference-Methods

## Card 07-009

**Front**

What is Sarsa?

**Back**

Sarsa is a model-free temporal-difference algorithm that directly estimates the action values $q_\pi(s,a)$ of a policy from experience.

By combining action-value estimation with policy improvement, Sarsa can also be used to learn an optimal policy.

**Tags**

07-Temporal-Difference-Methods

## Card 07-010

**Front**

Why is the algorithm called Sarsa?

**Back**

Each Sarsa update uses the experience tuple

$$
(s_t,a_t,r_{t+1},s_{t+1},a_{t+1}).
$$

Sarsa is an abbreviation for state-action-reward-state-action.

**Tags**

07-Temporal-Difference-Methods

## Card 07-011

**Front**

What is the Sarsa action-value update?

**Back**

For the visited state-action pair $(s_t,a_t)$, the update is

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

The action values of all other state-action pairs remain unchanged.

**Tags**

07-Temporal-Difference-Methods

## Card 07-012

**Front**

What are the TD target and TD error of Sarsa?

**Back**

The Sarsa TD target is

$$
r_{t+1}
+
\gamma q_t(s_{t+1},a_{t+1}).
$$

Using Zhao's sign convention, the TD error is

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

**Tags**

07-Temporal-Difference-Methods

## Card 07-013

**Front**

Which equation does Sarsa solve when evaluating a fixed policy?

**Back**

Sarsa is a stochastic-approximation method for solving the action-value form of the Bellman equation:

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

**Tags**

07-Temporal-Difference-Methods

## Card 07-014

**Front**

How can Sarsa be extended from policy evaluation to optimal policy learning?

**Back**

The basic Sarsa update estimates the action values of a fixed policy.

To learn an optimal policy, action-value estimation is combined with policy improvement. After updating an action value, the policy for the visited state is made $\varepsilon$-greedy with respect to the new estimates.

**Tags**

07-Temporal-Difference-Methods

## Card 07-015

**Front**

Why is optimal policy learning with Sarsa an example of generalized policy iteration?

**Back**

After updating the action value of the visited state-action pair, Sarsa immediately improves the policy for the visited state.

The current policy is therefore not evaluated completely before it is improved. Policy evaluation and policy improvement proceed together.

**Tags**

07-Temporal-Difference-Methods

## Card 07-016

**Front**

How is the policy updated during optimal policy learning with Sarsa?

**Back**

Let

$$
a^*
=
\underset{a\in\mathcal{A}(s)}{\arg\max}
\ q(s,a)
$$

be a greedy action. The policy is updated to

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

The $\varepsilon$-greedy policy continues to explore while usually selecting a greedy action.

**Tags**

07-Temporal-Difference-Methods

## Card 07-017

**Front**

Under which conditions does Sarsa converge when evaluating a fixed policy?

**Back**

For every state-action pair $(s,a)$, the learning rates must satisfy

$$
\sum_{t=0}^{\infty}\alpha_t(s,a)=\infty
$$

and

$$
\sum_{t=0}^{\infty}\alpha_t^2(s,a)<\infty.
$$

The first condition requires every state-action pair to be visited sufficiently often. The second ensures that the learning rates eventually become small enough for the estimates to stabilize.

**Tags**

07-Temporal-Difference-Methods

## Card 07-018

**Front**

What is Expected Sarsa?

**Back**

Expected Sarsa is a variant of Sarsa that uses the policy-weighted mean of all action values in the next state.

Instead of using the value of one sampled next action, it considers every possible next action and its selection probability.

**Tags**

07-Temporal-Difference-Methods

## Card 07-019

**Front**

What is the TD target of Expected Sarsa?

**Back**

The Expected Sarsa TD target is

$$
r_{t+1}
+
\gamma
\sum_{a\in\mathcal{A}(s_{t+1})}
\pi_t(a\mid s_{t+1})
q_t(s_{t+1},a).
$$

The sum is the policy-weighted mean of the action values available in the next state.

**Tags**

07-Temporal-Difference-Methods

## Card 07-020

**Front**

What is the difference between the TD targets of Sarsa and Expected Sarsa?

**Back**

Sarsa uses the value of one sampled next action:

$$
r_{t+1}
+
\gamma q_t(s_{t+1},a_{t+1}).
$$

Expected Sarsa uses the policy-weighted mean of all next-action values:

$$
r_{t+1}
+
\gamma
\sum_{a\in\mathcal{A}(s_{t+1})}
\pi_t(a\mid s_{t+1})
q_t(s_{t+1},a).
$$

Expected Sarsa requires slightly more computation but generally has lower estimation variance.

**Tags**

07-Temporal-Difference-Methods