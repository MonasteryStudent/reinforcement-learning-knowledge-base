## Card 08-001

**Front**

What is value function approximation?

**Back**

Value function approximation represents state values or action values with a parameterized function instead of storing every value separately in a table.

For example,

$$
v_\pi(s)\approx\hat{v}(s,\mathbf{w}),
$$

where $\mathbf{w}$ is the parameter vector.

**Tags**

08-Value-Function-Methods

## Card 08-002

**Front**

What is a stationary distribution?

**Back**

A stationary distribution describes the long-term probabilities of an agent being in the different states of a Markov process under a fixed policy.

It remains unchanged when the state-transition matrix is applied:

$$
\mathbf{d}_\pi^T=\mathbf{d}_\pi^T P_\pi.
$$

**Tags**

08-Value-Function-Methods

## Card 08-003

**Front**

What is linear function approximation?

**Back**

Linear function approximation represents a value as a linear function of a parameter vector:

$$
\hat{v}(s,\mathbf{w})=\boldsymbol{\phi}^T(s)\mathbf{w}.
$$

Here, $\boldsymbol{\phi}(s)$ is the feature vector of state $s$.

**Tags**

08-Value-Function-Methods

## Card 08-004

**Front**

What is TD learning with function approximation?

**Back**

TD learning with function approximation estimates the state values of a fixed policy by updating the parameters of a function

$$
\hat{v}(s,\mathbf{w})
$$

from observed transitions and one-step TD targets.

**Tags**

08-Value-Function-Methods

## Card 08-005

**Front**

What is Sarsa with function approximation?

**Back**

Sarsa with function approximation is an on-policy method that represents action values with a parameterized function

$$
\hat{q}(s,a,\mathbf{w}).
$$

It updates the parameters using the next action selected by the current policy.

**Tags**

08-Value-Function-Methods

## Card 08-006

**Front**

What is Q-learning with function approximation?

**Back**

Q-learning with function approximation represents action values with a parameterized function and updates its parameters using the greatest approximated action value in the next state.

It can be implemented in an on-policy or off-policy manner.

**Tags**

08-Value-Function-Methods

## Card 08-007

**Front**

What is deep Q-learning?

**Back**

Deep Q-learning, also called a deep Q-network, uses an artificial neural network to approximate the action-value function.

It commonly combines Q-learning with a main network, a target network, and experience replay.

**Tags**

08-Value-Function-Methods

## Card 08-008

**Front**

What is experience replay?

**Back**

Experience replay stores experience samples

$$
(s,a,r,s')
$$

in a replay buffer and uniformly draws mini-batches from the stored samples during training.

This changes the order in which the samples are used and allows them to be reused.

**Tags**

08-Value-Function-Methods

## Card 08-009

**Front**

How do tabular representation and function approximation differ when values are retrieved and updated?

**Back**

With a table, a value is retrieved or updated directly through its corresponding table entry.

With function approximation, a value is retrieved by evaluating the function. Values are updated indirectly by changing the parameter vector $\mathbf{w}$.

**Tags**

08-Value-Function-Methods

## Card 08-010

**Front**

What are the main advantages and disadvantage of value function approximation?

**Back**

Its main advantages are:

- reduced storage requirements,
- generalization from visited to unvisited states,
- applicability to large or continuous state spaces.

Its disadvantage is that the selected function may not represent the true value function exactly, resulting in approximation error.

**Tags**

08-Value-Function-Methods

## Card 08-011

**Front**

What role does the stationary distribution play in value function approximation?

**Back**

The stationary distribution determines how strongly each state's approximation error contributes to the objective:

$$
J(\mathbf{w})=\sum_{s\in\mathcal{S}}d_\pi(s)\left(v_\pi(s)-\hat{v}(s,\mathbf{w})\right)^2.
$$

States visited more frequently under policy $\pi$ receive greater weight.

**Tags**

08-Value-Function-Methods

## Card 08-012

**Front**

Why can a linear function approximator be nonlinear in the state?

**Back**

The term linear refers to the dependence on the parameter vector $\mathbf{w}$, not necessarily to the dependence on the state.

The feature vector may contain nonlinear state features such as

$$
1,\quad s,\quad s^2,\quad s^3.
$$

The approximation remains linear in $\mathbf{w}$.

**Tags**

08-Value-Function-Methods

## Card 08-013

**Front**

Why is tabular value representation a special case of linear function approximation?

**Back**

For every state $s$, select a one-hot feature vector

$$
\boldsymbol{\phi}(s)=\mathbf{e}_s.
$$

Then,

$$
\hat{v}(s,\mathbf{w})=\mathbf{e}_s^T\mathbf{w}=w(s).
$$

Each parameter represents the value of one state, as in a value table.

**Tags**

08-Value-Function-Methods

## Card 08-014

**Front**

What objective is used to approximate the state values of a policy?

**Back**

The parameter vector is selected to minimize the expected squared difference between the true and approximated state values:

$$
J(\mathbf{w})=\mathbb{E}\left[\left(v_\pi(S)-\hat{v}(S,\mathbf{w})\right)^2\right].
$$

**Tags**

08-Value-Function-Methods

## Card 08-015

**Front**

Write the TD state-value update with function approximation.

**Back**

$$
\mathbf{w}_{t+1}=\mathbf{w}_t+\alpha_t\left[r_{t+1}+\gamma\hat{v}(s_{t+1},\mathbf{w}_t)-\hat{v}(s_t,\mathbf{w}_t)\right]\nabla_{\mathbf{w}}\hat{v}(s_t,\mathbf{w}_t).
$$

The expression in square brackets is the TD target minus the current estimate.

**Tags**

08-Value-Function-Methods

## Card 08-016

**Front**

Write the Sarsa update with function approximation.

**Back**

$$
\mathbf{w}_{t+1}=\mathbf{w}_t+\alpha_t\left[r_{t+1}+\gamma\hat{q}(s_{t+1},a_{t+1},\mathbf{w}_t)-\hat{q}(s_t,a_t,\mathbf{w}_t)\right]\nabla_{\mathbf{w}}\hat{q}(s_t,a_t,\mathbf{w}_t).
$$

The next action $a_{t+1}$ is selected according to the current policy.

**Tags**

08-Value-Function-Methods

## Card 08-017

**Front**

Write the Q-learning update with function approximation.

**Back**

$$
\mathbf{w}_{t+1}=\mathbf{w}_t+\alpha_t\left[r_{t+1}+\gamma\max_{a\in\mathcal{A}(s_{t+1})}\hat{q}(s_{t+1},a,\mathbf{w}_t)-\hat{q}(s_t,a_t,\mathbf{w}_t)\right]\nabla_{\mathbf{w}}\hat{q}(s_t,a_t,\mathbf{w}_t).
$$

**Tags**

08-Value-Function-Methods

## Card 08-018

**Front**

How do the targets of Sarsa and Q-learning with function approximation differ?

**Back**

Sarsa uses the action actually selected in the next state:

$$
r_{t+1}+\gamma\hat{q}(s_{t+1},a_{t+1},\mathbf{w}_t).
$$

Q-learning uses the greatest approximated action value in the next state:

$$
r_{t+1}+\gamma\max_{a\in\mathcal{A}(s_{t+1})}\hat{q}(s_{t+1},a,\mathbf{w}_t).
$$

**Tags**

08-Value-Function-Methods

## Card 08-019

**Front**

Why does deep Q-learning use a target network in addition to the main network?

**Back**

Without a separate target network, the parameter vector $\mathbf{w}$ would appear in both the current estimate

$$
\hat{q}(s,a,\mathbf{w})
$$

and the target

$$
r+\gamma\max_{a\in\mathcal{A}(s')}\hat{q}(s',a,\mathbf{w}).
$$

This makes the gradient more difficult to calculate because the target would also change whenever $\mathbf{w}$ is updated.

Deep Q-learning therefore calculates the target with temporarily fixed parameters $\mathbf{w}_T$:

$$
y_T=r+\gamma\max_{a\in\mathcal{A}(s')}\hat{q}(s',a,\mathbf{w}_T).
$$

The main network parameters $\mathbf{w}$ are updated while $\mathbf{w}_T$ remains fixed. After every $C$ iterations, the target network is synchronized:

$$
\mathbf{w}_T\leftarrow\mathbf{w}.
$$

**Tags**

08-Value-Function-Methods

## Card 08-020

**Front**

Why is experience replay used in deep Q-learning?

**Back**

Uniformly sampling from a replay buffer reduces the temporal correlations between consecutive experience samples.

It also allows stored samples to be used multiple times, which increases data efficiency.

**Tags**

08-Value-Function-Methods