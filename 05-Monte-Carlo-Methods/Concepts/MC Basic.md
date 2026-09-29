## Definition

**MC Basic** is a model-free algorithm for finding an approximately [[Optimal Policy]] from sampled [[Episode|episodes]].

The algorithm alternates between two steps:

1. **Policy evaluation:** The [[Action Value|action values]] of the current [[Policy]] are estimated by averaging sampled returns.
2. **Policy improvement:** A new greedy policy is obtained by selecting an action with the greatest estimated action value in every state.

Unlike dynamic-programming algorithms, MC Basic does not require the state-transition or reward probabilities of the [[Environment]]. It learns entirely from episodes generated through interaction.

## Mathematical Formulation

Let $\pi_k$ be the policy in iteration $k$. For every state-action pair $(s,a)$, the algorithm generates $n$ episodes that begin with $(s,a)$ and then follow $\pi_k$.

Let

$$
g_{\pi_k}^{(i)}(s,a)
$$

denote the observed [[Return|return]] of the $i$th episode. The corresponding action value is estimated by

$$
\widehat{q}_{\pi_k}(s,a)
=
\frac{1}{n}
\sum_{i=1}^{n}
g_{\pi_k}^{(i)}(s,a).
$$

This sample mean approximates the expected return:

$$
\widehat{q}_{\pi_k}(s,a)
\approx
q_{\pi_k}(s,a).
$$

The policy is then improved greedily:

$$
\pi_{k+1}(s)
=
\underset{a\in\mathcal{A}(s)}{\arg\max}
\ \widehat{q}_{\pi_k}(s,a).
$$

If the improved policy is identical to the current policy, the algorithm terminates:

$$
\pi_{k+1}=\pi_k.
$$

## Algorithm

1. Initialize an arbitrary deterministic policy $\pi_0$.
2. For every state-action pair $(s,a)$:
   - Generate multiple episodes that begin with $(s,a)$.
   - Follow the current policy for the remaining steps of each episode.
   - Calculate the return produced by each episode.
   - Estimate $q_{\pi_k}(s,a)$ by averaging these returns.
3. Improve the policy by selecting an action with the greatest estimated action value in every state.
4. Repeat policy evaluation and policy improvement until the policy no longer changes.