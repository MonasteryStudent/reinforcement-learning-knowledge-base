## Card 06-001

**Front**

What is stochastic approximation?

**Back**

Stochastic approximation refers to a broad class of stochastic iterative algorithms for solving root-finding and optimization problems.

These algorithms update their estimates incrementally using noisy observations or random samples.

Stochastic approximation is important in reinforcement learning because temporal-difference algorithms can be viewed as stochastic-approximation algorithms.

**Tags**

06-Stochastic-Approximation

## Card 06-002

**Front**

What is the difference between non-incremental and incremental mean estimation?

**Back**

Non-incremental mean estimation first collects all samples and then calculates their average.

Incremental mean estimation updates the current estimate whenever a new sample is observed. It does not require storing and recalculating the mean from all previous samples.

**Tags**

06-Stochastic-Approximation

## Card 06-003

**Front**

Write the incremental mean-estimation update.

**Back**

Let $w_k$ be the current estimate and $x_k$ the new sample. The update is

$$
w_{k+1}=w_k-\alpha_k(w_k-x_k),
$$

where $\alpha_k>0$ is the step size.

If the sample is greater than the current estimate, the estimate increases. If the sample is smaller, the estimate decreases.

**Tags**

06-Stochastic-Approximation

## Card 06-004

**Front**

What happens when incremental mean estimation uses $\alpha_k=1/k$?

**Back**

The estimate becomes the exact running mean of the first $k$ samples:

$$
w_{k+1}=\frac{1}{k}\sum_{i=1}^{k}x_i.
$$

The average can therefore be updated whenever a new sample is observed.

**Tags**

06-Stochastic-Approximation

## Card 06-005

**Front**

What is the Robbins-Monro algorithm?

**Back**

The Robbins-Monro algorithm is a stochastic-approximation algorithm that finds the root of an unknown function using noisy observations.

It does not require the mathematical expression of the function or its derivative. It only requires inputs and their corresponding noisy outputs.

**Tags**

06-Stochastic-Approximation

## Card 06-006

**Front**

What problem and observation model are considered by the Robbins-Monro algorithm?

**Back**

The objective is to find a root $w^*$ satisfying

$$
g(w^*)=0.
$$

The exact function value cannot be observed. Instead, the algorithm receives

$$
\widetilde{g}(w,\eta)=g(w)+\eta,
$$

where $\eta$ is the observation error.

**Tags**

06-Stochastic-Approximation

## Card 06-007

**Front**

Write the Robbins-Monro update.

**Back**

The Robbins-Monro update is

$$
w_{k+1}=w_k-a_k\widetilde{g}(w_k,\eta_k),
$$

where:

- $w_k$ is the current root estimate,
- $\widetilde{g}(w_k,\eta_k)$ is the noisy observation,
- $a_k>0$ is the step size.

**Tags**

06-Stochastic-Approximation

## Card 06-008

**Front**

Why does the Robbins-Monro update tend to move toward the root of an increasing function?

**Back**

Ignoring observation noise, the update is

$$
w_{k+1}=w_k-a_kg(w_k).
$$

For an increasing function with root $w^*$:

- If $w_k>w^*$, then $g(w_k)>0$, so the estimate decreases.
- If $w_k<w^*$, then $g(w_k)<0$, so the estimate increases.

With a sufficiently small step, the estimate moves closer to the root. With observation noise, individual updates may move away from it.

**Tags**

06-Stochastic-Approximation

## Card 06-009

**Front**

What are the three main assumptions of the Robbins-Monro convergence theorem?

**Back**

First, the function has a positive, bounded derivative:

$$
0<c_1\leq\nabla_w g(w)\leq c_2.
$$

Second, the positive step sizes satisfy

$$
\sum_{k=1}^{\infty}a_k=\infty,
\qquad
\sum_{k=1}^{\infty}a_k^2<\infty.
$$

Third, the observation noise satisfies

$$
\mathbb{E}[\eta_k\mid H_k]=0,
\qquad
\mathbb{E}[\eta_k^2\mid H_k]<\infty,
$$

where $H_k$ represents the history available before the new observation.

Under these assumptions, the estimates converge almost surely to the root.

**Tags**

06-Stochastic-Approximation

## Card 06-010

**Front**

Why must the step sizes have an infinite sum but a finite sum of squares?

**Back**

The condition

$$
\sum_{k=1}^{\infty}a_k=\infty
$$

prevents the steps from decreasing too quickly. It avoids exhausting a finite total step-size budget before reaching the root.

The condition

$$
\sum_{k=1}^{\infty}a_k^2<\infty
$$

limits the accumulated effect of noise and implies $a_k\rightarrow0$.

Individual step sizes can therefore approach zero even though their sum grows without bound.

**Tags**

06-Stochastic-Approximation

## Card 06-011

**Front**

Why is $a_k=1/k$ a suitable step-size sequence?

**Back**

The individual step sizes approach zero, while

$$
\sum_{k=1}^{\infty}\frac{1}{k}=\infty
$$

and

$$
\sum_{k=1}^{\infty}\frac{1}{k^2}
=
\frac{\pi^2}{6}
<
\infty.
$$

The sequence decreases slowly enough to retain unlimited cumulative movement but quickly enough to reduce fluctuations caused by noise.

**Tags**

06-Stochastic-Approximation

## Card 06-012

**Front**

What is the purpose of Dvoretzky's convergence theorem?

**Back**

Dvoretzky's theorem provides sufficient conditions under which the error of a stochastic iterative algorithm converges to zero almost surely.

It can be used to prove the convergence of incremental mean estimation, the Robbins-Monro algorithm, and other stochastic algorithms.

**Tags**

06-Stochastic-Approximation

## Card 06-013

**Front**

What do the two terms in Dvoretzky's stochastic error process represent?

**Back**

The error process is

$$
\Delta_{k+1}=(1-\alpha_k)\Delta_k+\beta_k\eta_k.
$$

The term $(1-\alpha_k)\Delta_k$ reduces the existing error when $0<\alpha_k<1$.

The term $\beta_k\eta_k$ introduces observation noise scaled by $\beta_k$.

The theorem gives conditions under which the error converges to zero despite these stochastic disturbances.

**Tags**

06-Stochastic-Approximation

## Card 06-014

**Front**

What does almost-sure convergence mean?

**Back**

Almost-sure convergence means that the probability of a stochastic sequence converging to its target is one.

Exceptional sample sequences for which convergence does not occur may exist, but the set of such sequences has probability zero.

**Tags**

06-Stochastic-Approximation

## Card 06-015

**Front**

What is stochastic gradient descent?

**Back**

Stochastic gradient descent is an incremental optimization algorithm that updates a parameter using the gradient obtained from a single stochastic sample.

It replaces a true expected gradient that cannot be calculated directly with a sample-based stochastic gradient.

SGD is a special form of the Robbins-Monro algorithm.

**Tags**

06-Stochastic-Approximation

## Card 06-016

**Front**

How does the SGD update differ from the gradient-descent update?

**Back**

Gradient descent uses the true expected gradient:

$$
w_{k+1}
=
w_k
-
\alpha_k
\mathbb{E}[\nabla_w f(w_k,X)].
$$

SGD replaces it with the gradient obtained from the current sample:

$$
w_{k+1}
=
w_k
-
\alpha_k
\nabla_w f(w_k,x_k).
$$

**Tags**

06-Stochastic-Approximation

## Card 06-017

**Front**

What does it mean that a stochastic gradient is an unbiased estimate of the true gradient?

**Back**

Hold the current parameter $w_k$ fixed and average over independently drawn samples from the distribution of $X$.

The expected sample gradient equals the true gradient:

$$
\mathbb{E}_{x_k}[\nabla_w f(w_k,x_k)]
=
\nabla_w J(w_k).
$$

A single sample gradient may differ from the true gradient, but its expected deviation is zero.

“Unbiased” does not mean that every sample gradient is accurate.

**Tags**

06-Stochastic-Approximation

## Card 06-018

**Front**

How is incremental mean estimation a special SGD algorithm?

**Back**

Mean estimation can be formulated as

$$
\min_w
\frac{1}{2}
\mathbb{E}\left[\|w-X\|^2\right].
$$

The stochastic gradient for a sample $x_k$ is

$$
\nabla_w f(w_k,x_k)=w_k-x_k.
$$

The SGD update therefore becomes

$$
w_{k+1}=w_k-\alpha_k(w_k-x_k),
$$

which is the incremental mean-estimation update.

**Tags**

06-Stochastic-Approximation

## Card 06-019

**Front**

What convergence pattern does SGD typically exhibit?

**Back**

When the estimate is far from the optimal solution, the true gradient is large relative to the sampling error. SGD therefore behaves similarly to gradient descent and can approach the solution quickly.

Near the optimal solution, the true gradient becomes small and the randomness of the stochastic gradient becomes more influential. The estimates may therefore fluctuate and convergence becomes less direct.

**Tags**

06-Stochastic-Approximation

## Card 06-020

**Front**

How do BGD, MBGD, and SGD differ?

**Back**

They differ in the number of samples used per update:

- **Batch gradient descent:** uses all available samples.
- **Mini-batch gradient descent:** uses a subset of $m$ samples.
- **Stochastic gradient descent:** uses one sample.

Using more samples reduces the randomness of the gradient estimate but increases the cost of an individual update.

When $m=1$, MBGD becomes SGD. When $m=n$, randomly sampled MBGD does not necessarily become BGD because samples may be repeated and others omitted.

**Tags**

06-Stochastic-Approximation