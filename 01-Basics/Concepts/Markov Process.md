## Definition

A **Markov process (MP)** describes the evolution of [[State|states]] where the probability of the next state depends only on the current state and not on the preceding state history.

A Markov process can be obtained from a [[Markov Descision Process|Markov decision process]] by fixing its [[Policy|policy]].

## Mathematical Formulation

Given the state-transition probability $p(s'\mid s,a)$ and a fixed policy $\pi(a\mid s)$, the transition probability of the resulting Markov process is

$$
p_\pi(s'\mid s)=\sum_{a\in\mathcal{A}(s)}\pi(a\mid s)\,p(s'\mid s,a).
$$

The resulting state process satisfies the Markov property:

$$
p_\pi(s_{t+1}\mid s_t,s_{t-1},\ldots,s_0)=p_\pi(s_{t+1}\mid s_t).
$$

For every state $s$, the transition probabilities satisfy

$$
\sum_{s'\in\mathcal{S}}
p_\pi(s'\mid s)=1.
$$