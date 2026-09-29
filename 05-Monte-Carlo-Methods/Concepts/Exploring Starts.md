## Definition

**Exploring starts** is a condition requiring every state-action pair to have a positive probability of being selected as the initial pair of an [[Episode|episode]].

This condition ensures that every state-action pair can be visited sufficiently many times. Its [[Action Value|action value]] can therefore be estimated from sampled [[Return|returns]].

Both [[MC Basic]] and [[MC Exploring Starts]] rely on this condition. However, it can be difficult to satisfy in practical applications because an agent may not be able to begin an episode in every possible state while executing every possible action.

## Mathematical Formulation

The exploring-starts condition requires

$$
P(S_0=s,A_0=a)>0
$$

for every state $s$ and every available action $a\in\mathcal{A}(s)$.

The starting pairs do not have to be selected uniformly. They must only have nonzero selection probabilities.

If all possible state-action pairs are selected uniformly, then

$$
P(S_0=s,A_0=a)=\frac{1}{\sum_{s'\in\mathcal{S}}|\mathcal{A}(s')|}.
$$

Given sufficiently many episodes, every state-action pair can then be selected repeatedly and its action value can be estimated using [[Monte Carlo Estimation]].