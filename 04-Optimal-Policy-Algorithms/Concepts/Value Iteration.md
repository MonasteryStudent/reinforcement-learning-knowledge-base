## Definition

**Value iteration** is a [[Dynamic Programming|dynamic-programming]] algorithm for finding optimal state values and an [[Optimal Policy]].

Starting from an arbitrary initial estimate, the algorithm repeatedly applies the [[Bellman Optimality Equation]]. Each update considers every available action and assigns the greatest resulting [[Action Value]] to the state.

For a finite discounted [[Markov Decision Process]] with $\gamma\in(0,1)$, the value estimates converge to the optimal state values.

## Mathematical Formulation

Let $v_k(s)$ be the estimated value of state $s$ at iteration $k$. The estimated action value is

$$
q_k(s,a)
=
r(s,a)
+
\gamma
\sum_{s'\in\mathcal{S}}
p(s'\mid s,a)v_k(s').
$$

The next state-value estimate is obtained by selecting the greatest action value:

$$
v_{k+1}(s)
=
\max_{a\in\mathcal{A}(s)}
q_k(s,a).
$$

A greedy deterministic policy can be selected such that

$$
q_k(s,\pi_{k+1}(s))
=
\max_{a\in\mathcal{A}(s)}
q_k(s,a).
$$

As the number of iterations increases,

$$
\mathbf{v}_k
\rightarrow
\mathbf{v}^*.
$$

A practical stopping condition is

$$
\left\|
\mathbf{v}_{k+1}
-
\mathbf{v}_k
\right\|_\infty
\leq
\varepsilon,
$$

where $\varepsilon>0$ is a chosen tolerance and the infinity norm is the greatest absolute change among all state values.

## Algorithm

1. Initialize $\mathbf{v}_0$ with an arbitrary value for every state.
2. For every state-action pair, calculate $q_k(s,a)$ using the values from iteration $k$.
3. For every state, set $v_{k+1}(s)$ to the greatest available action value.
4. Select a greedy action for every state.
5. Stop when the state values change by no more than the chosen tolerance; otherwise, continue with the next iteration.

During one iteration, the new value $v_{k+1}(s)$ of every state is calculated using only the old value vector $\mathbf{v}_k$. Newly calculated values are stored separately and are not used until all states have been updated. This is called a **synchronous update**.

After convergence, the resulting state values approximate $\mathbf{v}^*$ and the greedy policy approximates an optimal policy.