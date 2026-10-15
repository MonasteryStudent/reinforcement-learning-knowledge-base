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

## Card 07-021

**Front**

What is n-step Sarsa?

**Back**

n-step Sarsa is a generalization of Sarsa that uses $n$ observed rewards before bootstrapping from an estimated action value.

The algorithm evaluates the action values of a given policy. It must be combined with policy improvement to learn an optimal policy.

**Tags**

07-Temporal-Difference-Methods

## Card 07-022

**Front**

What is the n-step target used by n-step Sarsa?

**Back**

The sampled n-step target is

$$
g_t^{(n)}
=
\sum_{i=0}^{n-1}
\gamma^i r_{t+i+1}
+
\gamma^n q_t(s_{t+n},a_{t+n}).
$$

It contains $n$ observed rewards and then bootstraps from the estimated action value of the state-action pair reached after $n$ steps.

**Tags**

07-Temporal-Difference-Methods

## Card 07-023

**Front**

Why must the update of $(s_t,a_t)$ in n-step Sarsa be delayed?

**Back**

The n-step target requires the experience sequence up to

$$
r_{t+n},s_{t+n},a_{t+n}.
$$

This information is not yet available at time step $t$. The algorithm must therefore wait until time step $t+n$ before updating the action value of $(s_t,a_t)$.

**Tags**

07-Temporal-Difference-Methods

## Card 07-024

**Front**

How are ordinary Sarsa and Monte Carlo learning special cases of n-step Sarsa?

**Back**

When $n=1$, the target is

$$
g_t^{(1)}
=
r_{t+1}
+
\gamma q_t(s_{t+1},a_{t+1}),
$$

which is the ordinary Sarsa target.

When $n$ extends to the end of the episode, the target becomes the complete discounted return. With $n=\infty$ and $\alpha=1$, the algorithm becomes Monte Carlo learning.

**Tags**

07-Temporal-Difference-Methods

## Card 07-025

**Front**

How does the choice of $n$ affect the bias and variance of n-step Sarsa?

**Back**

A small $n$ causes early bootstrapping from current action-value estimates. This generally produces greater bias but lower variance.

A large $n$ uses more observed rewards and bootstraps later. This generally produces lower bias but greater variance.

The increase in variance occurs when the generated rewards, transitions, or actions are stochastic.

**Tags**

07-Temporal-Difference-Methods

## Card 07-026

**Front**

What is Q-learning?

**Back**

Q-learning is a model-free temporal-difference algorithm that directly estimates the optimal action values.

It updates the visited state-action pair toward the immediate reward plus the greatest estimated action value in the next state.

**Tags**

07-Temporal-Difference-Learning

## Card 07-027

**Front**

What is the Q-learning target?

**Back**

The Q-learning target is

$$
\bar{q}_t
=
r_{t+1}
+
\gamma
\max_{a\in\mathcal{A}(s_{t+1})}
q_t(s_{t+1},a).
$$

It uses the greatest estimated action value in the next state, independently of the action actually selected there.

**Tags**

07-Temporal-Difference-Learning

## Card 07-028

**Front**

Write the Q-learning update for the visited state-action pair.

**Back**

The Q-learning update is

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
\gamma
\max_{a\in\mathcal{A}(s_{t+1})}
q_t(s_{t+1},a)
\right)
\right].
$$

All other action-value estimates remain unchanged.

**Tags**

07-Temporal-Difference-Learning

## Card 07-029

**Front**

What is the main difference between the Sarsa and Q-learning targets?

**Back**

Sarsa uses the action value of the action actually selected in the next state:

$$
r_{t+1}+\gamma q_t(s_{t+1},a_{t+1}).
$$

Q-learning instead uses the greatest estimated action value in the next state:

$$
r_{t+1}
+
\gamma
\max_{a\in\mathcal{A}(s_{t+1})}
q_t(s_{t+1},a).
$$

Sarsa learns from the next action selected by the current policy, whereas Q-learning learns from a greedy next action.

**Tags**

07-Temporal-Difference-Learning

## Card 07-030

**Front**

How is an optimal policy obtained from the action values learned by Q-learning?

**Back**

After the action values have converged, an optimal action is selected greedily in every state:

$$
\pi^*(s)
=
\underset{a\in\mathcal{A}(s)}{\arg\max}
\ q^*(s,a).
$$

If several actions have the same greatest action value, any of them can be selected as an optimal action.

**Tags**

07-Temporal-Difference-Learning

## Card 07-031

**Front**

What is a behavior policy?

**Back**

A behavior policy is the policy used to select actions and generate experience through interaction with the environment.

It determines which state-action pairs are visited during learning.

**Tags**

07-Temporal-Difference-Learning

## Card 07-032

**Front**

What is a target policy?

**Back**

A target policy is the policy being evaluated or improved by a learning algorithm.

It does not necessarily have to be the same policy that generated the experience.

**Tags**

07-Temporal-Difference-Learning

## Card 07-033

**Front**

What is the difference between on-policy and off-policy learning?

**Back**

In on-policy learning, the behavior policy and target policy are the same:

$$
\pi_b=\pi_T.
$$

In off-policy learning, the behavior policy and target policy may differ:

$$
\pi_b\neq\pi_T.
$$

Therefore, off-policy learning can use experience generated by one policy to learn about another policy.

**Tags**

07-Temporal-Difference-Learning

## Card 07-034

**Front**

Why is Sarsa an on-policy algorithm?

**Back**

Sarsa uses the next action actually selected by the current behavior policy in its target:

$$
r_{t+1}+\gamma q_t(s_{t+1},a_{t+1}).
$$

The policy generating the experience is therefore also the policy whose action values are being learned.

**Tags**

07-Temporal-Difference-Learning

## Card 07-035

**Front**

Why is Q-learning generally classified as an off-policy algorithm?

**Back**

The Q-learning target uses

$$
\max_{a\in\mathcal{A}(s_{t+1})}q_t(s_{t+1},a)
$$

instead of the value of the action actually selected by the behavior policy.

Its update therefore learns about a greedy target policy independently of how the experience was generated.

**Tags**

07-Temporal-Difference-Learning

## Card 07-036

**Front**

How can Q-learning have both on-policy and off-policy implementations?

**Back**

In an on-policy implementation, the policy being updated is also used to generate the experience.

In an off-policy implementation, a separate behavior policy generates the experience.

The Q-learning target remains the same in both cases:

$$
r_{t+1}
+
\gamma
\max_{a\in\mathcal{A}(s_{t+1})}
q_t(s_{t+1},a).
$$

Q-learning is nevertheless generally classified as off-policy because this target is independent of the next action selected by the behavior policy.

**Tags**

07-Temporal-Difference-Learning

## Card 07-037

**Front**

What is the difference between online and offline learning?

**Back**

In online learning, the agent generates experience through interaction with the environment and updates its estimates during this interaction.

In offline learning, the algorithm learns from previously collected experience without interacting with the environment during learning.

**Tags**

07-Temporal-Difference-Learning

## Card 07-038

**Front**

How do the on-policy–off-policy and online–offline distinctions differ?

**Back**

On-policy versus off-policy describes the relationship between the behavior policy and target policy.

Online versus offline describes whether experience is generated during learning or was collected beforehand.

The two distinctions describe different properties of a learning process.

**Tags**

07-Temporal-Difference-Learning

## Card 07-039

**Front**

Why is off-policy learning suitable for offline learning?

**Back**

An offline dataset may have been generated by a policy that differs from the policy currently being learned.

An off-policy algorithm can use this experience to learn about another target policy, provided that the dataset contains sufficient experience of the relevant state-action pairs.

**Tags**

07-Temporal-Difference-Learning

## Card 07-040

**Front**

What common update structure connects model-free action-value learning algorithms?

**Back**

Their updates can be written as

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

where $\bar{q}_t$ is the learning target.

The algorithms differ primarily in how they construct this target.

**Tags**

07-Temporal-Difference-Learning

## Card 07-041

**Front**

How do the targets of Monte Carlo learning, Sarsa, n-step Sarsa, and Q-learning differ?

**Back**

Monte Carlo learning uses the complete observed return.

Sarsa uses one observed reward and the value of the selected next action.

n-step Sarsa uses $n$ observed rewards before bootstrapping from a later action value.

Q-learning uses one observed reward and the greatest estimated action value in the next state.

**Tags**

07-Temporal-Difference-Learning