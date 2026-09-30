## Card 05-001

**Front**

What is Monte Carlo estimation?

**Back**

Monte Carlo estimation refers to a broad class of methods that use stochastic samples to estimate expected values.

If the probability distribution of a random variable is unknown, its expected value can be approximated by averaging observed samples.

**Tags**

05-Monte-Carlo-Methods

## Card 05-002

**Front**

What conditions should samples satisfy for Monte Carlo mean estimation?

**Back**

The samples should be independent and identically distributed (i.i.d.):

- Independent means that one sample does not influence another.
- Identically distributed means that all samples come from the same probability distribution.

For the sample mean

$$\overline{X}_n=\frac{1}{n}\sum_{i=1}^{n}X_i,$$

the law of large numbers states that it approaches $\mathbb{E}[X]$ as the number of samples increases.

**Tags**

05-Monte-Carlo-Methods

## Card 05-003

**Front**

Why is mean estimation important in reinforcement learning?

**Back**

State values and action values are expected values of returns. Estimating them from sampled returns is therefore a mean-estimation problem.

For example,

$$q_\pi(s,a)=\mathbb{E}_\pi[G_t\mid S_t=s,A_t=a].$$

Monte Carlo methods approximate this expectation by averaging returns observed after starting from $(s,a)$ and following policy $\pi$.

**Tags**

05-Monte-Carlo-Methods

## Card 05-004

**Front**

What is MC Basic?

**Back**

MC Basic is a model-free variant of policy iteration.

It repeatedly alternates between:

1. Estimating the action values of the current policy from sampled episodes.
2. Improving the policy by selecting an action with the greatest estimated action value in every state.

**Tags**

05-Monte-Carlo-Methods

## Card 05-005

**Front**

How does MC Basic estimate the action value of a state-action pair?

**Back**

For a state-action pair $(s,a)$, MC Basic generates $n$ episodes that begin with $(s,a)$ and then follow the current policy $\pi_k$.

If $g_{\pi_k}^{(i)}(s,a)$ is the return of episode $i$, then

$$q_{\pi_k}(s,a)\approx\widehat{q}_{\pi_k}(s,a)=\frac{1}{n}\sum_{i=1}^{n}g_{\pi_k}^{(i)}(s,a).$$

**Tags**

05-Monte-Carlo-Methods

## Card 05-006

**Front**

What is the main difference between policy iteration and MC Basic?

**Back**

Policy iteration calculates values from a known system model containing the reward and state-transition probabilities.

MC Basic does not require this model. It estimates action values directly from sampled returns.

Action values are estimated directly because calculating them from state values would still require the unknown system model.

**Tags**

05-Monte-Carlo-Methods

## Card 05-007

**Front**

What are the initial-visit, first-visit, and every-visit strategies?

**Back**

They determine how visits within an episode are used:

- **Initial visit:** Use the episode only for its initial state-action pair.
- **First visit:** Use only the first occurrence of each state-action pair.
- **Every visit:** Use every occurrence of each state-action pair.

MC Basic uses the initial-visit strategy.

**Tags**

05-Monte-Carlo-Methods

## Card 05-008

**Front**

Why is the every-visit strategy more sample-efficient than the initial-visit strategy?

**Back**

The every-visit strategy uses the return following every visited state-action pair.

A single episode can therefore provide samples for many action values, including multiple samples for a pair visited repeatedly.

However, returns from repeated visits in the same episode may be correlated because their remaining trajectories overlap.

**Tags**

05-Monte-Carlo-Methods

## Card 05-009

**Front**

What is the exploring-starts condition, and why is it important?

**Back**

Exploring starts requires every state-action pair to have a positive probability of being selected as the initial pair of an episode:

$$P(S_0=s,A_0=a)>0.$$

This allows every action value to be estimated from sufficiently many samples. Otherwise, an action may appear inferior merely because it has not been explored adequately.

**Tags**

05-Monte-Carlo-Methods

## Card 05-010

**Front**

How does MC Exploring Starts improve the efficiency of MC Basic?

**Back**

MC Exploring Starts introduces two main changes:

1. It uses the every-visit strategy to update every state-action pair visited in an episode.
2. It updates the action values and improves the policy after each episode instead of waiting for a complete policy-evaluation stage.

It still requires the exploring-starts condition.

**Tags**

05-Monte-Carlo-Methods

## Card 05-011

**Front**

How does MC Exploring Starts calculate returns and update action values?

**Back**

The episode is processed backwards. Starting with $g=0$, the return is updated by

$$g\leftarrow\gamma g+r_{t+1}.$$

For every visit, the algorithm performs

$$\mathrm{Returns}(s_t,a_t)\leftarrow\mathrm{Returns}(s_t,a_t)+g,$$

$$\mathrm{Num}(s_t,a_t)\leftarrow\mathrm{Num}(s_t,a_t)+1,$$

and

$$q(s_t,a_t)=\frac{\mathrm{Returns}(s_t,a_t)}{\mathrm{Num}(s_t,a_t)}.$$

**Tags**

05-Monte-Carlo-Methods

## Card 05-012

**Front**

Why can an MC algorithm improve its policy after only one episode?

**Back**

The return of one episode provides only a rough estimate of an action value, but policy evaluation does not have to be complete before policy improvement begins.

This follows the idea of generalized policy iteration: approximate value estimation and policy improvement can interact while both continue to develop.

**Tags**

05-Monte-Carlo-Methods

## Card 05-013

**Front**

What is a soft policy?

**Back**

A soft policy is a stochastic policy that assigns a positive probability to every action available in every state:

$$\pi(a\mid s)>0$$

for every $a\in\mathcal{A}(s)$.

It continues exploring different actions and can therefore remove the need to start episodes from every state-action pair.

**Tags**

05-Monte-Carlo-Methods

## Card 05-014

**Front**

How does an $\varepsilon$-greedy policy select an action?

**Back**

An $\varepsilon$-greedy policy uses one of two selection branches:

1. With probability $1-\varepsilon$, select a greedy action.
2. With probability $\varepsilon$, select uniformly from all available actions, including the greedy action.

A greedy action is an action with the greatest currently estimated action value.

**Tags**

05-Monte-Carlo-Methods

## Card 05-015

**Front**

Write the action probabilities of an $\varepsilon$-greedy policy.

**Back**

Let $a^*$ be a greedy action. Then

$$\pi(a\mid s)=\begin{cases}1-\varepsilon+\dfrac{\varepsilon}{|\mathcal{A}(s)|}, & a=a^*,\\ \dfrac{\varepsilon}{|\mathcal{A}(s)|}, & a\neq a^*.\end{cases}$$

The greedy action receives an additional probability of $\varepsilon/|\mathcal{A}(s)|$ because it can also be selected during uniform random selection.

**Tags**

05-Monte-Carlo-Methods

## Card 05-016

**Front**

What happens to an $\varepsilon$-greedy policy when $\varepsilon=0$ or $\varepsilon=1$?

**Back**

When $\varepsilon=0$, the policy always selects a greedy action and performs no deliberate exploration.

When $\varepsilon=1$, the policy selects uniformly from all available actions:

$$\pi(a\mid s)=\frac{1}{|\mathcal{A}(s)|}.$$

**Tags**

05-Monte-Carlo-Methods

## Card 05-017

**Front**

What is MC $\varepsilon$-Greedy, and how does it differ from MC Exploring Starts?

**Back**

MC $\varepsilon$-Greedy replaces the greedy policy-improvement step of MC Exploring Starts with an $\varepsilon$-greedy policy-improvement step.

Because the resulting soft policy retains a positive probability of selecting every action, the exploring-starts condition is no longer required.

The algorithm still uses the every-visit strategy.

**Tags**

05-Monte-Carlo-Methods

## Card 05-018

**Front**

Can MC $\varepsilon$-Greedy find an optimal policy?

**Back**

Given sufficient samples, it can find a policy that is optimal among all $\varepsilon$-greedy policies with the same value of $\varepsilon$.

This policy is not necessarily optimal among all possible policies because it must continue selecting non-greedy actions with positive probability.

For a sufficiently small $\varepsilon$, it can be close to a greedy optimal policy.

**Tags**

05-Monte-Carlo-Methods

## Card 05-019

**Front**

What is the trade-off between exploration and exploitation?

**Back**

**Exploration** means trying different actions so that their action values can be evaluated.

**Exploitation** means selecting an action that currently has the greatest estimated action value.

Increasing $\varepsilon$ produces more exploration but less exploitation. Decreasing $\varepsilon$ produces more exploitation but increases the risk of overlooking insufficiently explored actions.

**Tags**

05-Monte-Carlo-Methods

## Card 05-020

**Front**

What is the relationship between MC Basic, MC Exploring Starts, and MC $\varepsilon$-Greedy?

**Back**

The algorithms extend one another:

- **MC Basic** introduces model-free policy evaluation using sampled returns.
- **MC Exploring Starts** improves sample usage through the every-visit strategy and episode-by-episode policy updates.
- **MC $\varepsilon$-Greedy** replaces greedy improvement with $\varepsilon$-greedy improvement, removing the exploring-starts requirement.

**Tags**

05-Monte-Carlo-Methods