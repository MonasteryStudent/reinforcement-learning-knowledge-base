## Definition

The **Robbins-Monro algorithm** is a [[Stochastic Approximation|stochastic-approximation]] algorithm for finding the root of an unknown function from noisy observations.

Unlike many conventional root-finding methods, it does not require the mathematical expression of the function or its derivative. It only requires an input and the corresponding noisy output of the function.

The algorithm repeatedly adjusts its current root estimate according to the sign and magnitude of the observed function value.

## Mathematical Formulation

The objective is to find a root $w^*$ satisfying

$$
g(w^*)=0.
$$

The function $g$ is unknown. For an input $w$, only a noisy observation is available:

$$
\widetilde{g}(w,\eta)=g(w)+\eta,
$$

where $\eta$ is the observation error.

Starting from an initial estimate $w_1$, the Robbins-Monro update is

$$
w_{k+1}=w_k-a_k\widetilde{g}(w_k,\eta_k),
$$

where:

- $w_k$ is the current estimate of the root,
- $\widetilde{g}(w_k,\eta_k)$ is the noisy observation,
- $a_k>0$ is the step size,
- $w_{k+1}$ is the updated estimate.

If $g$ is monotonically increasing, the update moves the estimate toward the root:

- If $w_k>w^*$, then $g(w_k)>0$ and the update decreases $w_k$.
- If $w_k<w^*$, then $g(w_k)<0$ and the update increases $w_k$.

Because the observation contains noise, individual updates may move irregularly. Under appropriate conditions on the function, observation noise, and [[Step-Size Conditions|step sizes]], the estimates converge almost surely to $w^*$.

## Convergence Conditions

The Robbins-Monro theorem guarantees almost-sure convergence to the root $w^*$ under three main conditions.

First, the function must be monotonically increasing with a bounded derivative:

$$
0<c_1\leq\nabla_wg(w)\leq c_2.
$$

Second, the step sizes must satisfy the [[Step-Size Conditions|step-size conditions]]

$$
\sum_{k=1}^{\infty}a_k=\infty
$$

and

$$
\sum_{k=1}^{\infty}a_k^2<\infty.
$$

Third, the observation noise must have a conditional mean of zero and a finite conditional second moment:

$$
\mathbb{E}[\eta_k\mid H_k]=0
$$

and

$$
\mathbb{E}[\eta_k^2\mid H_k]<\infty.
$$

Under these conditions,

$$
w_k\rightarrow w^*
$$

almost surely.

## Algorithm

1. Select an initial root estimate $w_1$.
2. Evaluate the system at $w_k$ and obtain the noisy observation $\widetilde{g}(w_k,\eta_k)$.
3. Update the estimate using

   $$
   w_{k+1}=w_k-a_k\widetilde{g}(w_k,\eta_k).
   $$

4. Repeat the observation and update steps.

[[Stochastic Gradient Descent]] is a special form of the Robbins-Monro algorithm.