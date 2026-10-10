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