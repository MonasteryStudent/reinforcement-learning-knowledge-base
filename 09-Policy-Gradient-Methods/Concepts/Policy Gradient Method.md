## Definition

A **policy gradient method** directly optimizes a [[Parameterized Policy]] by changing its parameter vector $\boldsymbol{\theta}$.

The quality of the policy is measured by a scalar objective function

$$
J(\boldsymbol{\theta}).
$$

The gradient of this objective indicates the direction in parameter space in which the objective increases most strongly. The policy parameters are therefore moved in the direction of the gradient.

Policy gradient methods are **policy-based** because they directly optimize the policy. In contrast, value-based methods first estimate state or action values and derive a policy from these estimates.

Different scalar objectives can be used to evaluate a policy, including the [[Average State Value]] and the [[Average Reward]].

## Mathematical Formulation

The gradient of the objective with respect to the parameter vector is

$$
\nabla_{\boldsymbol{\theta}}J(\boldsymbol{\theta})
=
\begin{bmatrix}
\dfrac{\partial J}{\partial\theta_1}\\
\dfrac{\partial J}{\partial\theta_2}\\
\vdots\\
\dfrac{\partial J}{\partial\theta_m}
\end{bmatrix}.
$$

The policy parameters are updated through gradient ascent:

$$
\boldsymbol{\theta}_{t+1}
=
\boldsymbol{\theta}_t
+
\alpha
\nabla_{\boldsymbol{\theta}}
J(\boldsymbol{\theta}_t),
$$

where $\alpha>0$ is the optimization step size.

The addition of the gradient distinguishes gradient ascent from gradient descent. Gradient ascent seeks to maximize the objective, whereas gradient descent seeks to minimize it.

The desired parameter vector is

$$
\boldsymbol{\theta}^*
=
\underset{\boldsymbol{\theta}}{\arg\max}
\ J(\boldsymbol{\theta}).
$$

The corresponding policy

$$
\pi(a\mid s,\boldsymbol{\theta}^*)
$$

is optimal with respect to the selected objective.

The [[Policy Gradient Theorem]] provides an expression for the gradient that can be estimated from experience samples.

## Algorithm

1. Initialize the policy parameters $\boldsymbol{\theta}_0$.
2. Repeat until a stopping condition is satisfied:
   - Use the current policy to collect experience samples.
   - Use the samples to estimate the policy gradient.
   - Update the policy parameters in the direction of the estimated gradient.

The stopping condition may be a fixed number of parameter updates or a sufficiently small change in the policy parameters or objective value.