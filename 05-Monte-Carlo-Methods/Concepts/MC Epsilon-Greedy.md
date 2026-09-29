## Definition

**MC $\varepsilon$-Greedy** is a model-free algorithm obtained by replacing the greedy policy-improvement step of [[MC Exploring Starts]] with an [[Epsilon-Greedy Policy]].

Because an $\varepsilon$-greedy policy can select every action with positive probability, the algorithm does not require the [[Exploring Starts|exploring-starts condition]].

The algorithm uses the [[Visit Strategies|every-visit strategy]] and improves the policy after each episode. Given sufficient samples, it can find a policy that is optimal within the set of $\varepsilon$-greedy policies.

This policy is not necessarily an [[Optimal Policy|optimal policy]] among all possible policies. However, for a sufficiently small $\varepsilon$, it can be close to a greedy optimal policy.

## Mathematical Formulation

After an episode has been generated, its returns are calculated backwards. Starting with $g=0$, the return update is

$$
g\leftarrow\gamma g+r_{t+1}.
$$

For every visited state-action pair, the algorithm updates

$$
\operatorname{Returns}(s_t,a_t)\leftarrow\operatorname{Returns}(s_t,a_t)+g,
$$

$$
\operatorname{Num}(s_t,a_t)\leftarrow\operatorname{Num}(s_t,a_t)+1,
$$

and

$$
q(s_t,a_t)=\frac{\operatorname{Returns}(s_t,a_t)}{\operatorname{Num}(s_t,a_t)}.
$$

A greedy action for the visited state is

$$
a^*=\underset{a\in\mathcal{A}(s_t)}{\arg\max}\ q(s_t,a).
$$

The improved policy is

$$
\pi(a\mid s_t)=
\begin{cases}
1-\varepsilon+\dfrac{\varepsilon}{|\mathcal{A}(s_t)|}, & a=a^*,\\
\dfrac{\varepsilon}{|\mathcal{A}(s_t)|}, & a\neq a^*.
\end{cases}
$$

## Algorithm

1. Initialize a policy $\pi_0$, action values $q(s,a)$, accumulated returns, and visit counts.
2. Choose $\varepsilon\in(0,1]$.
3. Generate an episode by following the current policy. The exploring-starts condition is not required.
4. Traverse the episode backwards and calculate the return following each visit.
5. Update the accumulated return, visit count, and action value of every visited state-action pair.
6. Improve the policy to be $\varepsilon$-greedy with respect to the current action-value estimates.
7. Repeat the procedure for additional episodes.