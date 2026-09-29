## Definition

An **$\varepsilon$-greedy policy** is a [[Soft Policy|soft policy]] that selects actions based on their estimated [[Action Value|action values]].

In each state, an action with the greatest estimated action value is called a **greedy action**. It represents the action that currently appears to be the best, although its estimated value may still be inaccurate.

To select one action, the policy uses the following random procedure:

1. With probability $1-\varepsilon$, select the greedy action.
2. With probability $\varepsilon$, select uniformly from all available actions, including the greedy action.

As a result, the greedy action has the highest selection probability, while every other action retains a nonzero probability of being selected.

The parameter $\varepsilon\in[0,1]$ controls the balance between [[Exploration and Exploitation|exploration and exploitation]].

## Mathematical Formulation

Let

$$
a^*=\underset{a\in\mathcal{A}(s)}{\arg\max}\ q(s,a)
$$

be a greedy action and let $|\mathcal{A}(s)|$ be the number of actions available in state $s$.

The $\varepsilon$-greedy policy is

$$
\pi(a\mid s)=
\begin{cases}
1-\varepsilon+\dfrac{\varepsilon}{|\mathcal{A}(s)|}, & a=a^*,\\
\dfrac{\varepsilon}{|\mathcal{A}(s)|}, & a\neq a^*.
\end{cases}
$$

Equivalently, the probability of the greedy action can be written as

$$
1-\frac{|\mathcal{A}(s)|-1}{|\mathcal{A}(s)|}\varepsilon.
$$

When $\varepsilon=0$, the policy is greedy:

$$
\pi(a^*\mid s)=1.
$$

When $\varepsilon=1$, all available actions are selected uniformly:

$$
\pi(a\mid s)=\frac{1}{|\mathcal{A}(s)|}.
$$