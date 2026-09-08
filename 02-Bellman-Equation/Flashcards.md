## Card 02-001

**Front**

What is a state value?

**Back**

The state value of a state is the expected return obtained when the agent starts from that state and follows a given policy.

**Tags**

02-Bellman-Equation

## Card 02-002

**Front**

What is the relationship between a return and a state value?

**Back**

A return is associated with a particular trajectory, whereas a state value is the expected return over the possible trajectories that can begin in a state under a given policy.

If the policy and system model are deterministic, the state value equals the return of the resulting trajectory.

**Tags**

02-Bellman-Equation

## Card 02-003

**Front**

How is the state value under policy $\pi$ defined mathematically?

**Back**

$$
v_\pi(s)=\mathbb{E}_\pi[G_t\mid S_t=s].
$$

It is the expected return given that the agent is in state $s$ at time step $t$ and follows policy $\pi$.

**Tags**

02-Bellman-Equation

## Card 02-004

**Front**

What is the Bellman equation?

**Back**

The Bellman equation is a set of linear equations that describes the relationships between the values of all states under a given policy.

It expresses a state value as the expected immediate reward plus the discounted expected value of the next state.

**Tags**

02-Bellman-Equation

## Card 02-005

**Front**

How can the return random variable $G_t$ be expressed recursively?

**Back**

$$
G_t=R_{t+1}+\gamma G_{t+1}.
$$

The return from time step $t$ consists of the immediate reward $R_{t+1}$ and the discounted return from the next time step.

**Tags**

02-Bellman-Equation

## Card 02-006

**Front**

Write the Bellman equation for the state value $v_\pi(s)$.

**Back**

$$
v_\pi(s)=\sum_{a\in\mathcal{A}(s)}\pi(a\mid s)\left[\sum_{r\in\mathcal{R}(s,a)}p(r\mid s,a)r+\gamma\sum_{s'\in\mathcal{S}}p(s'\mid s,a)v_\pi(s')\right].
$$

The first inner sum represents the expected immediate reward. The second inner sum represents the expected value of the next state.

**Tags**

02-Bellman-Equation

## Card 02-007

**Front**

Why is solving the Bellman equation called policy evaluation?

**Back**

Solving the Bellman equation gives the state values produced by a given policy.

Because state values can be used to assess how good a policy is, calculating them can be interpreted as evaluating the policy.

**Tags**

02-Bellman-Equation

## Card 02-008

**Front**

Consider a two-state system under a fixed policy $\pi$:

- In state $s_1$, the expected immediate reward is $1$. The next state is $s_1$ with probability $0.5$ and $s_2$ with probability $0.5$.
- In state $s_2$, the expected immediate reward is $0$. The system remains in $s_2$ with probability $1$.

Write the corresponding Bellman equation in matrix-vector form.

**Back**

The general matrix-vector form of the Bellman equation is

$$
\mathbf{v}_\pi=\mathbf{r}_\pi+\gamma\mathbf{P}_\pi\mathbf{v}_\pi.
$$

For the given system,

$$
\mathbf{r}_\pi=\begin{bmatrix}1\\0\end{bmatrix}
$$

and

$$
\mathbf{P}_\pi=\begin{bmatrix}0.5&0.5\\0&1\end{bmatrix}.
$$

Therefore,

$$
\begin{bmatrix}v_\pi(s_1)\\v_\pi(s_2)\end{bmatrix}=\begin{bmatrix}1\\0\end{bmatrix}+\gamma\begin{bmatrix}0.5&0.5\\0&1\end{bmatrix}\begin{bmatrix}v_\pi(s_1)\\v_\pi(s_2)\end{bmatrix}.
$$

This represents the two equations

$$
v_\pi(s_1)=1+\gamma\left[0.5v_\pi(s_1)+0.5v_\pi(s_2)\right]
$$

and

$$
v_\pi(s_2)=\gamma v_\pi(s_2).
$$

**Tags**

02-Bellman-Equation

## Card 02-009

**Front**

Which two approaches can be used to calculate state values from the Bellman equation?

**Back**

State values can be calculated using a **closed-form solution** or an **iterative solution**.

The closed-form solution is

$$
\mathbf{v}_\pi=(\mathbf{I}-\gamma\mathbf{P}_\pi)^{-1}\mathbf{r}_\pi.
$$

It expresses the state values directly but requires the inverse of the matrix $\mathbf{I}-\gamma\mathbf{P}_\pi$.

The iterative solution starts from an initial guess $\mathbf{v}_0$ and repeatedly applies

$$
\mathbf{v}_{k+1}=\mathbf{r}_\pi+\gamma\mathbf{P}_\pi\mathbf{v}_k.
$$

The resulting sequence converges to the state-value vector $\mathbf{v}_\pi$.

**Tags**

02-Bellman-Equation

## Card 02-010

**Front**

How does the iterative solution of the Bellman equation work, and why does it require an initial guess?

**Back**

The iterative solution begins with an initial state-value vector $\mathbf{v}_0$ and repeatedly applies the Bellman update

$$
\mathbf{v}_{k+1}=\mathbf{r}_\pi+\gamma\mathbf{P}_\pi\mathbf{v}_k.
$$

During each iteration, the current estimates in $\mathbf{v}_k$ are used to calculate improved estimates in $\mathbf{v}_{k+1}$.

This update uses **bootstrapping**: the new state-value estimates in $\mathbf{v}_{k+1}$ are calculated from the previous estimates in $\mathbf{v}_k$.

The initial guess $\mathbf{v}_0$ provides the values needed to perform the first update. It does not have to be accurate and is often chosen as the zero vector.

For $\gamma\in(0,1)$, the sequence converges to the true state-value vector:

$$
\mathbf{v}_k\rightarrow\mathbf{v}_\pi\quad\text{as}\quad k\rightarrow\infty.
$$

**Tags**

02-Bellman-Equation

## Card 02-011

**Front**

What is an action value?

**Back**

The action value of a state-action pair is the expected return obtained after taking a particular action in a particular state and then following a given policy.

Although it is called an action value, it depends on both the state and the action.

**Tags**

02-Bellman-Equation

## Card 02-012

**Front**

How is the action value under policy $\pi$ defined mathematically?

**Back**

$$
q_\pi(s,a)=\mathbb{E}_\pi[G_t\mid S_t=s,A_t=a].
$$

The condition fixes the current state and action. After taking action $a$, the agent continues to follow policy $\pi$.

**Tags**

02-Bellman-Equation

## Card 02-013

**Front**

How can an action value be calculated from state values?

**Back**

$$
q_\pi(s,a)=\sum_{r\in\mathcal{R}(s,a)}p(r\mid s,a)r+\gamma\sum_{s'\in\mathcal{S}}p(s'\mid s,a)v_\pi(s').
$$

The action value is the expected immediate reward plus the discounted expected value of the next state.

**Tags**

02-Bellman-Equation

## Card 02-014

**Front**

How can a state value be calculated from action values?

**Back**

$$
v_\pi(s)=\sum_{a\in\mathcal{A}(s)}\pi(a\mid s)q_\pi(s,a).
$$

The state value is the policy-weighted mean of the action values available in that state.

**Tags**

02-Bellman-Equation