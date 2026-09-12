## Definition

A **fixed point** of a function is a value that remains unchanged when the function is applied to it.

A **contraction mapping** is a function that brings any two input vectors closer together. The distance between their outputs is smaller than the distance between their inputs by at least a constant factor.

The contraction mapping theorem states that a contraction mapping has exactly one fixed point. Repeatedly applying the function from any initial value converges to that fixed point.

In Chapter 3, this theorem is used to establish the existence and uniqueness of the solution of the [[Bellman Optimality Equation|Bellman optimality equation]] and the convergence of its iterative solution.

## Mathematical Formulation

A vector $\mathbf{x}^*$ is a fixed point of a function $f$ if

$$
f(\mathbf{x}^*)=\mathbf{x}^*.
$$

A function $f:\mathbb{R}^d\rightarrow\mathbb{R}^d$ is a contraction mapping if there exists a constant $\gamma\in(0,1)$ such that

$$
\lVert f(\mathbf{x}_1)-f(\mathbf{x}_2)\rVert\leq\gamma\lVert\mathbf{x}_1-\mathbf{x}_2\rVert
$$

for any vectors $\mathbf{x}_1,\mathbf{x}_2\in\mathbb{R}^d$.

If $f$ is a contraction mapping, then:

1. A fixed point $\mathbf{x}^*$ exists.
2. The fixed point is unique.
3. The iteration

$$
\mathbf{x}_{k+1}=f(\mathbf{x}_k)
$$

converges to $\mathbf{x}^*$ for any initial guess $\mathbf{x}_0$.

For the Bellman optimality operator,

$$
f(\mathbf{v})=\max_{\pi\in\Pi}\left(\mathbf{r}_\pi+\gamma\mathbf{P}_\pi\mathbf{v}\right),
$$

Zhao proves the contraction property using the maximum norm:

$$
\lVert f(\mathbf{v}_1)-f(\mathbf{v}_2)\rVert_\infty\leq\gamma\lVert\mathbf{v}_1-\mathbf{v}_2\rVert_\infty.
$$

The central idea is that the discount rate $\gamma<1$ reduces the difference between successive value estimates. Consequently, repeated application of the Bellman optimality operator converges to its unique fixed point $\mathbf{v}^*$.