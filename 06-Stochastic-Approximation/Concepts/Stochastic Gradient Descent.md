## Definition

**Stochastic gradient descent (SGD)** is an incremental optimization algorithm that updates a parameter using the gradient obtained from a single stochastic sample.

It is used when the objective function contains an expectation that cannot be calculated directly because the probability distribution of the random variable is unknown.

Instead of calculating the true gradient, SGD uses a stochastic gradient based on the sample observed in the current iteration.

SGD is a special form of the [[Robbins-Monro Algorithm]].

## Mathematical Formulation

Consider the optimization problem

$$
\min_w J(w)=\mathbb{E}[f(w,X)],
$$

where $w$ is the parameter to be optimized and $X$ is a random variable.

The true gradient is

$$
\nabla_wJ(w)=\mathbb{E}[\nabla_wf(w,X)].
$$

Gradient descent would therefore use the update

$$
w_{k+1}=w_k-\alpha_k\mathbb{E}[\nabla_wf(w_k,X)].
$$

If the probability distribution of $X$ is unknown, this expected gradient cannot be calculated directly.

SGD replaces it with the stochastic gradient obtained from the current sample $x_k$:

$$
w_{k+1}=w_k-\alpha_k\nabla_wf(w_k,x_k).
$$

If the samples are independent and identically distributed, the stochastic gradient is an unbiased estimate of the true gradient:

$$
\mathbb{E}_{x_k}[\nabla_wf(w_k,x_k)]
=
\mathbb{E}[\nabla_wf(w_k,X)].
$$

Consequently, the stochastic gradient can be written as the true gradient plus a zero-mean observation error:

$$
\nabla_wf(w_k,x_k)
=
\mathbb{E}[\nabla_wf(w_k,X)]
+
\eta_k.
$$

## Application to Mean Estimation

Mean estimation can be formulated as the optimization problem

$$
\min_w J(w)=\frac{1}{2}\mathbb{E}\left[\|w-X\|^2\right].
$$

For

$$
f(w,X)=\frac{1}{2}\|w-X\|^2,
$$

the stochastic gradient is

$$
\nabla_wf(w,x_k)=w-x_k.
$$

The SGD update therefore becomes

$$
w_{k+1}=w_k-\alpha_k(w_k-x_k),
$$

which is the incremental mean-estimation update.

## Algorithm

1. Select an initial parameter estimate $w_1$.
2. Obtain a sample $x_k$.
3. Calculate the stochastic gradient $\nabla_wf(w_k,x_k)$.
4. Update the parameter using

   $$
   w_{k+1}=w_k-\alpha_k\nabla_wf(w_k,x_k).
   $$

5. Repeat the sampling and update steps.

When the estimate is far from the optimal solution, SGD generally behaves similarly to gradient descent. Near the solution, the randomness of the stochastic gradient becomes more influential and the estimates may fluctuate.