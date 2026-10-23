## Definition

**Value function approximation** represents [[State Value|state values]] or [[Action Value|action values]] with a parameterized function instead of storing every value separately in a table.

For a given policy $\pi$, the state value $v_\pi(s)$ is approximated by

$$
\hat{v}(s,\mathbf{w}),
$$

where $\mathbf{w}$ is a parameter vector. A value is retrieved by evaluating the function for a particular state. To change the approximated values, the parameters $\mathbf{w}$ are updated.

The parameter vector can be considerably smaller than a table containing one entry for every state. This makes function approximation suitable for large or continuous state spaces.

Updating $\mathbf{w}$ for an experience associated with one state may also change the approximated values of other states. Function approximation can therefore generalize information from visited states to states that have not been visited.

This increased storage efficiency and generalization ability come at the cost of a possible approximation error: the selected function may not be able to represent the true value function exactly.

## Mathematical Formulation

For a given policy $\pi$, the true state value is approximated as

$$
v_\pi(s)\approx\hat{v}(s,\mathbf{w}).
$$

The approximated value depends on both the state $s$ and the parameter vector $\mathbf{w}$.

A common example is a linear function approximator:

$$
\hat{v}(s,\mathbf{w})
=
\boldsymbol{\phi}^{T}(s)\mathbf{w},
$$

where $\boldsymbol{\phi}(s)$ is a feature vector describing state $s$.

Similarly, an action value can be approximated by

$$
q_\pi(s,a)\approx\hat{q}(s,a,\mathbf{w}).
$$

The parameters are selected so that the approximated values are close to the true values. For state values, this can be expressed through the objective function

$$
J(\mathbf{w})
=
\mathbb{E}
\left[
\left(
v_\pi(S)-\hat{v}(S,\mathbf{w})
\right)^2
\right].
$$

The probability distribution of the random state $S$ determines how strongly the approximation error of each state contributes to the objective. A common choice is the [[Stationary Distribution]] of the Markov process under policy $\pi$, which gives greater weight to states that are visited more frequently.