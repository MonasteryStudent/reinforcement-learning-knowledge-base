## Definition

**Dvoretzky's convergence theorem** provides sufficient conditions under which the error of a stochastic iterative algorithm converges to zero.

The theorem separates an update into two components:

- a contracting component that reduces the current error,
- a stochastic component caused by observation noise.

It can be used to prove the convergence of incremental mean estimation, the [[Robbins-Monro Algorithm]], and other stochastic algorithms.

## Mathematical Formulation

Consider the stochastic error process

$$
\Delta_{k+1}=(1-\alpha_k)\Delta_k+\beta_k\eta_k,
$$

where:

- $\Delta_k$ is the current estimation error,
- $\alpha_k\geq 0$ controls the reduction of the current error,
- $\beta_k\geq 0$ controls the influence of the noise,
- $\eta_k$ is the stochastic observation error.

The term

$$
(1-\alpha_k)\Delta_k
$$

reduces the existing error, whereas

$$
\beta_k\eta_k
$$

introduces a stochastic disturbance.

The error $\Delta_k$ converges to zero almost surely if the coefficient sequences satisfy

$$
\sum_{k=1}^{\infty}\alpha_k=\infty,
$$

$$
\sum_{k=1}^{\infty}\alpha_k^2<\infty,
$$

and

$$
\sum_{k=1}^{\infty}\beta_k^2<\infty.
$$

The observation noise must also satisfy

$$
\mathbb{E}[\eta_k\mid H_k]=0
$$

and

$$
\mathbb{E}[\eta_k^2\mid H_k]\leq C,
$$

where $H_k$ represents the information available before observing $\eta_k$, and $C$ is a finite constant.

Consequently,

$$
\Delta_k\rightarrow 0
$$

almost surely.

Almost-sure convergence means that the probability of the error converging to zero is one, although exceptional sample sequences may still exist.