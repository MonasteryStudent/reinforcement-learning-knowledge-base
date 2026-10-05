## Definition

The **step size** determines how strongly a new observation changes the current estimate in a stochastic iterative algorithm.

Large step sizes produce greater changes and allow the estimate to move quickly. Small step sizes reduce the influence of observation noise and stabilize the estimate.

For the [[Robbins-Monro Algorithm]] to converge from an arbitrary initial estimate, the step sizes must decrease over time, but they must not decrease too quickly.

## Mathematical Formulation

The Robbins-Monro update is

$$
w_{k+1}=w_k-a_k\widetilde{g}(w_k,\eta_k),
$$

where $a_k>0$ is the step size at iteration $k$.

The Robbins-Monro theorem requires the step-size sequence to satisfy

$$
\sum_{k=1}^{\infty}a_k=\infty
$$

and

$$
\sum_{k=1}^{\infty}a_k^2<\infty.
$$

The condition

$$
\sum_{k=1}^{\infty}a_k^2<\infty
$$

implies that $a_k$ approaches zero. Consequently, the individual updates become smaller and the estimate does not continue fluctuating because of observation noise.

The condition

$$
\sum_{k=1}^{\infty}a_k=\infty
$$

ensures that the step sizes do not approach zero too quickly. Their cumulative magnitude remains large enough for the algorithm to reach the root even when the initial estimate is far away.

A common step-size sequence satisfying both conditions is

$$
a_k=\frac{1}{k}.
$$

For this sequence,

$$
\sum_{k=1}^{\infty}\frac{1}{k}=\infty
$$

while

$$
\sum_{k=1}^{\infty}\frac{1}{k^2}=\frac{\pi^2}{6}<\infty.
$$

A constant step size does not satisfy these conditions because its squared sum is infinite. Nevertheless, sufficiently small constant step sizes are often used in practical stochastic-approximation and reinforcement-learning algorithms.