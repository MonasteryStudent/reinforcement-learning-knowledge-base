## Definition

**Linear function approximation** is a form of [[Value Function Approximation]] in which an approximated value is expressed as a linear function of a parameter vector.

For a state $s$, the approximation is based on a feature vector $\boldsymbol{\phi}(s)$ that describes relevant properties of the state. The parameter vector $\mathbf{w}$ determines how strongly the individual features contribute to the approximated value.

Although the approximation is linear in $\mathbf{w}$, it does not have to be linear in the state $s$. The feature vector may contain nonlinear transformations such as polynomial or trigonometric features.

The selection of suitable features determines which value functions can be represented. More features can increase the approximation ability but also require additional storage and computation.

## Mathematical Formulation

The approximated state value is

$$
\hat{v}(s,\mathbf{w})
=
\boldsymbol{\phi}^{T}(s)\mathbf{w},
$$

where

$$
\boldsymbol{\phi}(s)
=
\begin{bmatrix}
\phi_1(s)\\
\phi_2(s)\\
\vdots\\
\phi_m(s)
\end{bmatrix}
$$

is the feature vector and

$$
\mathbf{w}
=
\begin{bmatrix}
w_1\\
w_2\\
\vdots\\
w_m
\end{bmatrix}
$$

is the parameter vector. Written as a sum, the approximation is

$$
\hat{v}(s,\mathbf{w})
=
\sum_{i=1}^{m}\phi_i(s)w_i.
$$

Because the function is linear in its parameters, its gradient with respect to $\mathbf{w}$ is

$$
\nabla_{\mathbf{w}}\hat{v}(s,\mathbf{w})
=
\boldsymbol{\phi}(s).
$$

The same representation can be applied to [[Action Value|action values]]:

$$
\hat{q}(s,a,\mathbf{w})
=
\boldsymbol{\phi}^{T}(s,a)\mathbf{w}.
$$

The tabular representation is a special case of linear function approximation. For a finite state space containing $n$ states, let

$$
\boldsymbol{\phi}(s)=\mathbf{e}_s\in\mathbb{R}^{n},
$$

where $\mathbf{e}_s$ contains a one at the position corresponding to state $s$ and zeros at all other positions. The approximated state value then becomes

$$
\hat{v}(s,\mathbf{w})
=
\mathbf{e}_s^T\mathbf{w}
=
w(s).
$$

Each component of $\mathbf{w}$ therefore represents the value of one state, as it would in a value table.