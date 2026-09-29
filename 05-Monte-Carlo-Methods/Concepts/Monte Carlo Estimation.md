## Definition

**Monte Carlo estimation** is a model-free method for estimating the expected value of a random variable from observed samples.

Instead of calculating the expectation from a known probability distribution, Monte Carlo estimation uses the average of independent and identically distributed (i.i.d.) samples. According to the law of large numbers, the sample mean approaches the expected value as the number of samples increases.

In [[Reinforcement Learning]], complete [[Episode|episodes]] provide return samples that can be used to estimate [[Action Value|action values]] without knowing the state-transition and reward probabilities of the [[Environment]].

## Mathematical Formulation

Let $X$ be a random variable and let

$$
X_1,X_2,\ldots,X_n
$$

be independent and identically distributed samples of $X$. Their sample mean is

$$
\overline{X}_n=\frac{1}{n}\sum_{i=1}^{n}X_i.
$$

The sample mean is an unbiased estimator of the expected value:

$$
\mathbb{E}[\overline{X}_n]=\mathbb{E}[X].
$$

Its variance decreases as the number of samples increases:

$$
\operatorname{Var}(\overline{X}_n)=\frac{\operatorname{Var}(X)}{n}.
$$

Therefore, the sample mean approaches the expected value as $n$ increases:

$$
\overline{X}_n\rightarrow\mathbb{E}[X].
$$

In reinforcement learning, the [[Action Value|action value]] of a state-action pair under a [[Policy]] $\pi$ is

$$
q_\pi(s,a)=\mathbb{E}_\pi[G_t\mid S_t=s,A_t=a].
$$

Suppose that $n$ episodes start with the state-action pair $(s,a)$ and then follow policy $\pi$. If the observed return from episode $i$ is denoted by $g_\pi^{(i)}(s,a)$, the action value can be estimated by

$$
q_\pi(s,a)\approx\widehat{q}_\pi(s,a)=\frac{1}{n}\sum_{i=1}^{n}g_\pi^{(i)}(s,a).
$$

The estimate generally becomes more accurate as more return samples are collected.