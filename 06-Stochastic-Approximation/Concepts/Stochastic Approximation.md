## Definition

**Stochastic approximation** refers to a broad class of stochastic iterative algorithms for solving root-finding and optimization problems.

Instead of requiring the exact expression of a function or its derivative, stochastic-approximation algorithms can update an estimate using noisy observations or random samples.

Each new observation is processed immediately. The current estimate is corrected by a small step instead of collecting all samples before performing a calculation. Stochastic approximation therefore provides a transition from non-incremental algorithms to incremental algorithms.

In reinforcement learning, this idea provides an important foundation for temporal-difference learning, where value estimates are updated after individual interactions with the environment.

## Mathematical Formulation

Consider the problem of estimating the expected value $\mathbb{E}[X]$ from a sequence of samples.

Let $w_k$ be the current estimate of the expected value $\mathbb{E}[X]$, and let $x_k$ be the newly observed sample. The estimate is updated according to

$$
w_{k+1}=w_k-\alpha_k(w_k-x_k),
$$

where $\alpha_k>0$ is the step size.

The difference $x_k-w_k$ determines the direction of the update:

- If $x_k>w_k$, the estimate increases.
- If $x_k<w_k$, the estimate decreases.
- If $x_k=w_k$, the estimate remains unchanged.

When

$$
\alpha_k=\frac{1}{k},
$$

the update calculates the running mean of the first $k$ samples:

$$
w_{k+1}=\frac{1}{k}\sum_{i=1}^{k}x_i.
$$

Stochastic approximation generalizes this incremental idea to root-finding and optimization problems.

For a root-finding problem, the objective is to find $w^*$ satisfying

$$
g(w^*)=0.
$$

If only a noisy observation

$$
\widetilde{g}(w,\eta)=g(w)+\eta
$$

is available, the [[Robbins-Monro Algorithm]] uses the update

$$
w_{k+1}=w_k-a_k\widetilde{g}(w_k,\eta_k).
$$