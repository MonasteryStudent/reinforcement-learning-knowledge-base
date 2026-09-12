## Card 03-001

**Front**

What is an optimal state value?

**Back**

The optimal state value of a state is the greatest state value that can be achieved among all possible policies:

$$
v^*(s)=\max_{\pi\in\Pi}v_\pi(s).
$$

It represents the greatest expected return that the agent can obtain when starting from state $s$.

**Tags**

03-Bellman-Optimality-Equation

## Card 03-002

**Front**

What is an optimal policy?

**Back**

A policy $\pi^*$ is optimal if its state value is greater than or equal to that of every other policy for every state:

$$
v_{\pi^*}(s)\geq v_\pi(s)
$$

for every state $s\in\mathcal{S}$ and every policy $\pi\in\Pi$.

**Tags**

03-Bellman-Optimality-Equation

## Card 03-003

**Front**

Do optimal policies always exist, and must they be deterministic?

**Back**

In the tabular setting considered in the book, an optimal policy always exists.

An optimal policy can be deterministic or stochastic. However, there always exists at least one deterministic greedy optimal policy.

**Tags**

03-Bellman-Optimality-Equation

## Card 03-004

**Front**

Are the optimal state value and optimal policy unique?

**Back**

The optimal state-value vector $\mathbf{v}^*$ is unique.

An optimal policy $\pi^*$ is not necessarily unique. Multiple policies can produce the same optimal state values, for example when several actions have the same greatest action value.

**Tags**

03-Bellman-Optimality-Equation

## Card 03-005

**Front**

What is the optimal action value $q^*(s,a)$?

**Back**

The optimal action value is the expected return obtained after taking action $a$ in state $s$ and behaving optimally afterward.

It can be calculated as

$$
q^*(s,a)=\sum_{r\in\mathcal{R}(s,a)}p(r\mid s,a)r+\gamma\sum_{s'\in\mathcal{S}}p(s'\mid s,a)v^*(s').
$$

It consists of the expected immediate reward and the discounted expected optimal value of the next state.

**Tags**

03-Bellman-Optimality-Equation

## Card 03-006

**Front**

What is a deterministic greedy optimal policy?

**Back**

A deterministic greedy optimal policy always selects an action with the greatest optimal action value:

$$
a^*(s)=\underset{a\in\mathcal{A}(s)}{\arg\max}\ q^*(s,a).
$$

The corresponding policy is

$$
\pi^*(a\mid s)=
\begin{cases}
1, & a=a^*(s),\\
0, & a\neq a^*(s).
\end{cases}
$$

If several actions have the same greatest action value, any of them can be selected by a deterministic greedy optimal policy.

**Tags**

03-Bellman-Optimality-Equation

## Card 03-007

**Front**

What is the Bellman optimality equation, and why is it important?

**Back**

The Bellman optimality equation describes the relationships between optimal state values.

It expresses the optimal value of a state as the greatest value obtainable among the available actions.

Solving the equation produces the unique optimal state-value vector and at least one optimal policy.

**Tags**

03-Bellman-Optimality-Equation

## Card 03-008

**Front**

How does the Bellman optimality equation differ from the Bellman equation?

**Back**

The Bellman equation evaluates a given, fixed policy and produces its state values.

The Bellman optimality equation maximizes over possible policies or actions and produces the optimal state values and an optimal policy.

The Bellman optimality equation is therefore a special Bellman equation whose corresponding policy is optimal.

**Tags**

03-Bellman-Optimality-Equation

## Card 03-009

**Front**

Write the elementwise Bellman optimality equation.

**Back**

For every state $s$,

$$
v^*(s)=\max_{a\in\mathcal{A}(s)}\left[\sum_{r\in\mathcal{R}(s,a)}p(r\mid s,a)r+\gamma\sum_{s'\in\mathcal{S}}p(s'\mid s,a)v^*(s')\right].
$$

Equivalently,

$$
v^*(s)=\max_{a\in\mathcal{A}(s)}q^*(s,a).
$$

**Tags**

03-Bellman-Optimality-Equation

## Card 03-010

**Front**

Why can the maximization over policies in the Bellman optimality equation be replaced by a maximization over actions?

**Back**

For a state $s$, a policy assigns probabilities to the available actions. Therefore,

$$
\sum_{a\in\mathcal{A}(s)}\pi(a\mid s)q(s,a)
$$

is the policy-weighted mean of their action values.

This mean is maximized by assigning probability $1$ to an action with the greatest action value and probability $0$ to the other actions.

Therefore,

$$
\max_{\pi(s)\in\Pi(s)}\sum_{a\in\mathcal{A}(s)}\pi(a\mid s)q(s,a)=\max_{a\in\mathcal{A}(s)}q(s,a).
$$

The maximizing policy can consequently be chosen as a deterministic greedy policy.

**Tags**

03-Bellman-Optimality-Equation

## Card 03-011

**Front**

Write the matrix-vector and fixed-point forms of the Bellman optimality equation.

**Back**

The matrix-vector form is

$$
\mathbf{v}=\max_{\pi\in\Pi}\left(\mathbf{r}_\pi+\gamma\mathbf{P}_\pi\mathbf{v}\right),
$$

where the maximization is performed elementwise.

Define the Bellman optimality operator as

$$
f(\mathbf{v})=\max_{\pi\in\Pi}\left(\mathbf{r}_\pi+\gamma\mathbf{P}_\pi\mathbf{v}\right).
$$

The fixed-point form is then

$$
\mathbf{v}=f(\mathbf{v}).
$$

Its unique solution is the optimal state-value vector $\mathbf{v}^*$.

**Tags**

03-Bellman-Optimality-Equation

## Card 03-012

**Front**

What is a fixed point of a function?

**Back**

A fixed point is a value that remains unchanged when the function is applied to it.

A vector $\mathbf{x}^*$ is a fixed point of $f$ if

$$
f(\mathbf{x}^*)=\mathbf{x}^*.
$$

The optimal state-value vector is a fixed point of the Bellman optimality operator:

$$
f(\mathbf{v}^*)=\mathbf{v}^*.
$$

**Tags**

03-Bellman-Optimality-Equation

## Card 03-013

**Front**

What is a contraction mapping?

**Back**

A contraction mapping is a function that brings any two input vectors closer together.

A function $f$ is a contraction mapping if there is a constant $\gamma\in(0,1)$ such that

$$
\lVert f(\mathbf{x}_1)-f(\mathbf{x}_2)\rVert\leq\gamma\lVert\mathbf{x}_1-\mathbf{x}_2\rVert
$$

for any vectors $\mathbf{x}_1$ and $\mathbf{x}_2$.

**Tags**

03-Bellman-Optimality-Equation

## Card 03-014

**Front**

What does the contraction mapping theorem establish?

**Back**

If a function $f$ is a contraction mapping, then:

1. A fixed point $\mathbf{x}^*$ exists.
2. The fixed point is unique.
3. Starting from any initial guess $\mathbf{x}_0$, the iteration

$$
\mathbf{x}_{k+1}=f(\mathbf{x}_k)
$$

converges to $\mathbf{x}^*$.

**Tags**

03-Bellman-Optimality-Equation

## Card 03-015

**Front**

Why is the contraction property important for the Bellman optimality equation?

**Back**

The Bellman optimality operator satisfies

$$
\lVert f(\mathbf{v}_1)-f(\mathbf{v}_2)\rVert_\infty\leq\gamma\lVert\mathbf{v}_1-\mathbf{v}_2\rVert_\infty,
$$

where $\gamma\in(0,1)$.

Therefore, the contraction mapping theorem establishes that the Bellman optimality equation has a unique value solution $\mathbf{v}^*$ and that repeated application of the operator converges to it from any initial guess.

**Tags**

03-Bellman-Optimality-Equation

## Card 03-016

**Front**

How can the optimal state values and an optimal policy be obtained from the Bellman optimality equation?

**Back**

Starting from any initial guess $\mathbf{v}_0$, repeatedly apply

$$
\mathbf{v}_{k+1}=\max_{\pi\in\Pi}\left(\mathbf{r}_\pi+\gamma\mathbf{P}_\pi\mathbf{v}_k\right).
$$

The sequence converges to the optimal state-value vector $\mathbf{v}^*$.

An optimal policy can then be obtained from

$$
\pi^*=\underset{\pi\in\Pi}{\arg\max}\left(\mathbf{r}_\pi+\gamma\mathbf{P}_\pi\mathbf{v}^*\right).
$$

This iterative approach forms the basis of the value iteration algorithm introduced in Chapter 4.

**Tags**

03-Bellman-Optimality-Equation

## Card 03-017

**Front**

Which factors determine optimal state values and optimal policies?

**Back**

The optimal state values and optimal policies are determined by:

1. The immediate reward values $r$
2. The discount rate $\gamma$
3. The system model, consisting of $p(s'\mid s,a)$ and $p(r\mid s,a)$

Changing one of these factors can change the optimal state values and the optimal policy.

**Tags**

03-Bellman-Optimality-Equation

## Card 03-018

**Front**

How does the discount rate influence an optimal policy?

**Back**

A relatively large discount rate gives future rewards greater importance and produces a more far-sighted optimal policy.

Reducing the discount rate makes the optimal policy more short-sighted because future rewards contribute less to the return.

When $\gamma=0$, the agent considers only immediate rewards.

**Tags**

03-Bellman-Optimality-Equation

## Card 03-019

**Front**

What does optimal policy invariance under an affine transformation of the rewards mean?

**Back**

**Optimal policy invariance** means that an affine transformation of all rewards does not change the optimal policy.

Suppose every reward is transformed according to

$$
r'=\alpha r+\beta,
$$

where $\alpha>0$.

The optimal policy remains unchanged, while the optimal state-value vector becomes

$$
\mathbf{v}'=\alpha\mathbf{v}^*+\frac{\beta}{1-\gamma}\mathbf{1}.
$$

Therefore, multiplying all rewards by the same positive factor or adding the same value to all rewards changes the optimal state values but preserves the optimal policy.

**Tags**

03-Bellman-Optimality-Equation

## Card 03-020

**Front**

Why does an optimal policy avoid meaningless detours even when movement has a reward of zero?

**Back**

A detour delays the future rewards associated with reaching the target.

Because future rewards are discounted, reaching the same target through a longer trajectory produces a smaller return than reaching it through a shorter trajectory.

Therefore, the discount rate already encourages the agent to reach the target without meaningless detours.

**Tags**

03-Bellman-Optimality-Equation