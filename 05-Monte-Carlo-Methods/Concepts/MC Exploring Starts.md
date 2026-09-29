## Definition

**MC Exploring Starts** is a model-free algorithm that improves the sample efficiency of [[MC Basic]].

It introduces two main changes:

1. It uses the [[Visit Strategies|every-visit strategy]] to update the [[Action Value|action value]] of every state-action pair visited in an episode.
2. It updates the action values and improves the [[Policy|policy]] after each episode instead of waiting for a complete policy-evaluation stage.

The algorithm still requires the [[Exploring Starts|exploring-starts condition]] so that every state-action pair can be selected as the initial pair of an episode.

## Mathematical Formulation

For every state-action pair, the algorithm maintains the accumulated return

$$
\operatorname{Returns}(s,a)
$$

and the number of visits

$$
\operatorname{Num}(s,a).
$$

After generating an episode of length $T$, the returns are calculated backwards. Starting with $g=0$, the update at time step $t$ is

$$
g\leftarrow \gamma g+r_{t+1}.
$$

The accumulated return and visit count are then updated:

$$
\operatorname{Returns}(s_t,a_t)\leftarrow\operatorname{Returns}(s_t,a_t)+g,
$$

$$
\operatorname{Num}(s_t,a_t)\leftarrow\operatorname{Num}(s_t,a_t)+1.
$$

The action-value estimate becomes

$$
q(s_t,a_t)=\frac{\operatorname{Returns}(s_t,a_t)}{\operatorname{Num}(s_t,a_t)}.
$$

The policy is improved greedily for the visited state:

$$
a^*=\underset{a\in\mathcal{A}(s_t)}{\arg\max}\ q(s_t,a).
$$

For a deterministic policy,

$$
\pi(a\mid s_t)=
\begin{cases}
1, & a=a^*,\\
0, & a\neq a^*.
\end{cases}
$$

## Algorithm

1. Initialize a policy $\pi_0$, action values $q(s,a)$, accumulated returns, and visit counts.
2. Select an initial state-action pair satisfying the exploring-starts condition.
3. Generate an episode by taking the selected initial action and then following the current policy.
4. Traverse the episode backwards.
5. Calculate the return following every visited state-action pair.
6. Update its accumulated return, visit count, and action-value estimate.
7. Improve the policy greedily for each visited state.
8. Repeat the procedure for additional episodes.