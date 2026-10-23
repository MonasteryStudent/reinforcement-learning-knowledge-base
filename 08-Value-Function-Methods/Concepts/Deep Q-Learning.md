## Definition

**Deep Q-learning**, also called a **deep Q-network (DQN)**, extends [[Q-Learning with Function Approximation]] by using an artificial neural network to approximate the action-value function.

The network represents

$$
\hat{q}(s,a,\mathbf{w}),
$$

where $\mathbf{w}$ contains the network parameters. Despite the name, the neural network does not necessarily have to contain many hidden layers.

Deep Q-learning commonly uses two networks:

- A **main network** that is updated during every training iteration.
- A **target network** that remains fixed for a certain number of iterations.

Experience samples are stored in a replay buffer and drawn uniformly in mini-batches using [[Experience Replay]]. These techniques make the training process more stable and allow experience samples to be reused.

The algorithm can be implemented [[On-Policy and Off-Policy Learning|off-policy]]: a behavior policy generates the experience samples, while the network learns action values associated with greedy action selection.

## Mathematical Formulation

The main network approximates the optimal action values as

$$
q^*(s,a)
\approx
\hat{q}(s,a,\mathbf{w}).
$$

A direct objective for Q-learning with function approximation is

$$
J(\mathbf{w})
=
\mathbb{E}
\left[
\left(
R
+
\gamma
\max_{a\in\mathcal{A}(S')}
\hat{q}(S',a,\mathbf{w})
-
\hat{q}(S,A,\mathbf{w})
\right)^2
\right].
$$

In this objective, $\mathbf{w}$ appears in both the current estimate and the TD target. Deep Q-learning therefore introduces a separate target network with parameters $\mathbf{w}_T$:

$$
J(\mathbf{w})
=
\mathbb{E}
\left[
\left(
R
+
\gamma
\max_{a\in\mathcal{A}(S')}
\hat{q}(S',a,\mathbf{w}_T)
-
\hat{q}(S,A,\mathbf{w})
\right)^2
\right].
$$

For an experience sample $(s,a,r,s')$, the output of the main network is

$$
y
=
\hat{q}(s,a,\mathbf{w}).
$$

The target value is

$$
y_T
=
r
+
\gamma
\max_{a\in\mathcal{A}(s')}
\hat{q}(s',a,\mathbf{w}_T).
$$

The main network is trained to minimize the squared difference

$$
\left(
y_T-y
\right)^2.
$$

For a mini-batch $\mathcal{M}$, the loss can be written as

$$
L(\mathbf{w})
=
\frac{1}{|\mathcal{M}|}
\sum_{(s,a,r,s')\in\mathcal{M}}
\left[
y_T-\hat{q}(s,a,\mathbf{w})
\right]^2.
$$

The target network is periodically synchronized with the main network:

$$
\mathbf{w}_T
\leftarrow
\mathbf{w}.
$$

Once the action values have been learned, a greedy policy can be obtained from

$$
\pi(s)
=
\underset{a\in\mathcal{A}(s)}
{\arg\max}
\ \hat{q}(s,a,\mathbf{w}).
$$

## Algorithm

Initialize a main network and a target network with identical parameters.

1. Generate experience samples using a behavior policy.
2. Store the samples $(s,a,r,s')$ in the replay buffer $\mathcal{B}$.
3. For every training iteration:

   - Uniformly draw a mini-batch of samples from $\mathcal{B}$.
   - For every sample, calculate the target value:

     $$
     y_T
     =
     r
     +
     \gamma
     \max_{a\in\mathcal{A}(s')}
     \hat{q}(s',a,\mathbf{w}_T).
     $$

   - Update the main network parameters $\mathbf{w}$ by minimizing

     $$
     \frac{1}{|\mathcal{M}|}
     \sum_{(s,a,r,s')\in\mathcal{M}}
     \left[
     y_T-\hat{q}(s,a,\mathbf{w})
     \right]^2.
     $$

   - After every $C$ iterations, copy the main network parameters to the target network:

     $$
     \mathbf{w}_T
     \leftarrow
     \mathbf{w}.
     $$

The main network changes during every training iteration, whereas the target network remains fixed between two synchronization steps.