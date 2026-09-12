## Definition

The **Bellman optimality equation** describes the relationships between [[Optimal State Value|optimal state values]].

It expresses the optimal value of a state as the greatest value obtainable among the available actions. This value consists of the expected immediate [[Reward|reward]] and the discounted expected optimal value of the next state.

The Bellman optimality equation is a special [[Bellman Equation|Bellman equation]] whose corresponding policy is optimal. Solving it produces the unique optimal state-value vector and at least one [[Optimal Policy|optimal policy]].

Unlike the Bellman equation of a fixed policy, the Bellman optimality equation contains a maximization operation and is therefore nonlinear.

## Mathematical Formulation

For every state $s$, the Bellman optimality equation can be written as

$$
v^*(s)=\max_{a\in\mathcal{A}(s)}\left[\sum_{r\in\mathcal{R}(s,a)}p(r\mid s,a)r+\gamma\sum_{s'\in\mathcal{S}}p(s'\mid s,a)v^*(s')\right].
$$

Using the optimal [[Action Value|action value]], it can be written more concisely as

$$
v^*(s)=\max_{a\in\mathcal{A}(s)}q^*(s,a).
$$

Before its solution is known, Zhao expresses the equation as a maximization over policies:

$$
v(s)=\max_{\pi(s)\in\Pi(s)}\sum_{a\in\mathcal{A}(s)}\pi(a\mid s)q(s,a).
$$

The matrix-vector form is

$$
\mathbf{v}=\max_{\pi\in\Pi}\left(\mathbf{r}_\pi+\gamma\mathbf{P}_\pi\mathbf{v}\right),
$$

where the maximization is performed elementwise.

Define the Bellman optimality operator as

$$
f(\mathbf{v})=\max_{\pi\in\Pi}\left(\mathbf{r}_\pi+\gamma\mathbf{P}_\pi\mathbf{v}\right).
$$

The Bellman optimality equation then has the fixed-point form

$$
\mathbf{v}=f(\mathbf{v}).
$$

Its unique solution is the optimal state-value vector:

$$
\mathbf{v}^*=f(\mathbf{v}^*).
$$

Because $f$ is a [[Contraction Mapping|contraction mapping]], the solution can be calculated iteratively:

$$
\mathbf{v}_{k+1}=f(\mathbf{v}_k)=\max_{\pi\in\Pi}\left(\mathbf{r}_\pi+\gamma\mathbf{P}_\pi\mathbf{v}_k\right).
$$

Starting from any initial guess $\mathbf{v}_0$, the sequence converges to $\mathbf{v}^*$.