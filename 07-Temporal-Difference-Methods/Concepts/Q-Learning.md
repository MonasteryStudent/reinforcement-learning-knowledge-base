## Definition

**Q-learning** is a model-free [[Temporal-Difference Learning|temporal-difference learning]] algorithm for estimating the optimal [[Action Value|action values]].

Unlike [[Sarsa]], Q-learning does not use the action that is actually selected in the next state for its update. Instead, it uses the greatest estimated action value available in the next state.

Therefore, Q-learning directly approximates the solution of the [[Bellman Optimality Equation]] and learns an [[Optimal Policy]].

Q-learning is an [[On-Policy and Off-Policy Learning|off-policy]] algorithm because the policy used to generate experience may differ from the greedy policy represented by the update target.

## Mathematical Formulation

The Q-learning target is

$$
\bar{q}_t=r_{t+1}+\gamma\max_{a\in\mathcal{A}(s_{t+1})}q_t(s_{t+1},a).
$$

The action value of the visited state-action pair is updated according to

$$
q_{t+1}(s_t,a_t)=q_t(s_t,a_t)-\alpha_t(s_t,a_t)\left[q_t(s_t,a_t)-\bar{q}_t\right].
$$

Substituting the target gives

$$
q_{t+1}(s_t,a_t)=q_t(s_t,a_t)-\alpha_t(s_t,a_t)\left[q_t(s_t,a_t)-\left(r_{t+1}+\gamma\max_{a\in\mathcal{A}(s_{t+1})}q_t(s_{t+1},a)\right)\right].
$$

The action values of all other state-action pairs remain unchanged:

$$
q_{t+1}(s,a)=q_t(s,a)
$$

for every $(s,a)\neq(s_t,a_t)$.

Q-learning approximates the optimal action values satisfying

$$
q^*(s,a)=\mathbb{E}\left[R_{t+1}+\gamma\max_{a'\in\mathcal{A}(S_{t+1})}q^*(S_{t+1},a')\mid S_t=s,A_t=a\right].
$$

Once the action values have converged, an optimal deterministic policy can be obtained through

$$
\pi^*(s)=\underset{a\in\mathcal{A}(s)}{\arg\max}\ q^*(s,a).
$$

## Algorithm

1. Initialize the action-value estimates $q_0(s,a)$.
2. Observe the current state $s_t$.
3. Select an action $a_t$ using the behavior policy.
4. Execute the action and observe the reward $r_{t+1}$ and next state $s_{t+1}$.
5. Determine the greatest estimated action value in the next state:

   $$
   \max_{a\in\mathcal{A}(s_{t+1})}q_t(s_{t+1},a).
   $$

6. Update $q_t(s_t,a_t)$ using the Q-learning update.
7. Repeat the process with the next state.

The behavior policy should continue to explore the available state-action pairs. However, the Q-learning target always assumes that an action with the greatest estimated action value is selected in the next state.