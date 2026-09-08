## Definition

The **action value** of a state-action pair describes the expected [[Return|return]] obtained when the [[Agent|agent]] takes a particular [[Action|action]] in a particular [[State|state]] and then follows a given [[Policy|policy]].

Although it is conventionally called an action value, it depends on both the state and the action. It can therefore also be called a **state-action value**.

An action value consists of the expected immediate [[Reward|reward]] produced by the action and the discounted expected [[State Value|value]] of the next state.

Action values are closely related to state values. A state value is the mean of the action values available in that state, weighted by the probabilities with which the policy selects those actions.

## Mathematical Formulation

The action-value function under policy $\pi$ is defined as

$$
q_\pi(s,a) = \mathbb{E}_\pi[G_t\mid S_t=s,A_t=a].
$$

Here, the first action $a$ is fixed by the condition $A_t=a$. After this action, the agent continues to follow policy $\pi$.

The action value can be calculated from the expected immediate reward and the values of the possible next states:

$$
q_\pi(s,a) = \sum_{r\in\mathcal{R}(s,a)}p(r\mid s,a)r+\gamma\sum_{s'\in\mathcal{S}}p(s'\mid s,a)v_\pi(s').
$$

The first term is the expected immediate reward:

$$
\sum_{r\in\mathcal{R}(s,a)}p(r\mid s,a)r.
$$

The second term is the discounted expected value of the next state:

$$
\gamma\sum_{s'\in\mathcal{S}}p(s'\mid s,a)v_\pi(s').
$$

The state value can be obtained from the action values as

$$
v_\pi(s) = \sum_{a\in\mathcal{A}(s)}\pi(a\mid s)q_\pi(s,a).
$$

Thus, the relationship works in both directions:

- The action value $q_\pi(s,a)$ can be calculated from the values of the possible next states.
- The state value $v_\pi(s)$ can be calculated as the policy-weighted mean of the available action values.