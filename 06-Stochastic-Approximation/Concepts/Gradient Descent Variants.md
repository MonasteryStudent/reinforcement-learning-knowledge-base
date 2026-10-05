## Definition

**Batch gradient descent (BGD)**, **mini-batch gradient descent (MBGD)**, and [[Stochastic Gradient Descent|stochastic gradient descent (SGD)]] differ in the number of samples used to calculate each parameter update.

- BGD uses all available samples.
- MBGD uses a subset of the available samples.
- SGD uses a single sample.

Using more samples reduces the randomness of the gradient estimate but increases the computational cost of an individual update.

## Mathematical Formulation

Suppose that the objective is to minimize a function using the samples

$$
\{x_i\}_{i=1}^{n}.
$$

### Batch Gradient Descent

BGD calculates the average gradient using all $n$ samples:

$$
w_{k+1}
=
w_k
-
\alpha_k
\frac{1}{n}
\sum_{i=1}^{n}
\nabla_w f(w_k,x_i).
$$

Because every sample is used, the update has little sampling randomness. However, each update can be computationally expensive when the dataset is large.

### Mini-Batch Gradient Descent

MBGD uses a subset $I_k$ containing $m$ sampled indices:

$$
w_{k+1}
=
w_k
-
\alpha_k
\frac{1}{m}
\sum_{j\in I_k}
\nabla_w f(w_k,x_j).
$$

The mini-batch average reduces some of the randomness of individual sample gradients without requiring all samples in every update.

### Stochastic Gradient Descent

SGD uses a single sample $x_k$:

$$
w_{k+1}
=
w_k
-
\alpha_k
\nabla_w f(w_k,x_k).
$$

It can update the parameter immediately after receiving a sample, but its updates contain more randomness.

## Comparison

| Method | Samples per update | Randomness | Cost per update |
|---|---:|---:|---:|
| BGD | All $n$ samples | Low | High |
| MBGD | $m$ samples | Medium | Medium |
| SGD | One sample | High | Low |

MBGD can be viewed as an intermediate method between BGD and SGD:

- When $m=1$, MBGD becomes SGD.
- When $m=n$, MBGD does not necessarily become BGD if the samples are drawn randomly with replacement.

In the latter case, the mini-batch may contain repeated samples and may not contain every sample in the dataset.