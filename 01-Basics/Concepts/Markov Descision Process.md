## Definition

A **Markov decision process (MDP)** is a mathematical framework for describing sequential decision-making in a stochastic [[Environment|environment]].

At each time step, the [[Agent|agent]] observes the current [[State|state]], selects an available [[Action|action]] according to a [[Policy|policy]], receives a [[Reward|reward]], and [[State Transition|transitions]] to a next state.

An MDP satisfies the **Markov property**: given the current state and action, the probabilities of the next state and reward are independent of all previous states, actions, and rewards. The current state therefore contains the information required by the model to describe the next step of the interaction.

The **model**, also called the **dynamics**, describes how the environment responds to the agent through [[State Transition|state-transition]] and reward probabilities. Within the MDP framework, the policy describes how the agent selects actions. The **policy** is therefore part of the overall framework, but it is distinct from the environment model.

## Mathematical Formulation

An MDP contains the following sets:

* A state space $\mathcal{S}$ containing all possible states: 

$$
s\in\mathcal{S}.
$$

* An action space $\mathcal{A}(s)$ containing the actions available in state $s$: 

$$
a\in\mathcal{A}(s).
$$

* A reward set $\mathcal{R}(s,a)$ containing the possible rewards associated with state-action pair $(s,a)$:

$$
r\in\mathcal{R}(s,a).
$$

The state-transition probability is

$$
p(s'\mid s,a),
$$

where $s'$ is a possible next state. For every valid state-action pair,

$$
\sum_{s'\in\mathcal{S}}p(s'\mid s,a)=1.
$$

The reward probability is

$$
p(r\mid s,a).
$$

For every valid state-action pair,

$$
\sum_{r\in\mathcal{R}(s,a)}p(r\mid s,a)=1.
$$

A policy used within the MDP is denoted by

$$
\pi(a\mid s).
$$

For every state, the probabilities of all available actions sum to one:

$$
\sum_{a\in\mathcal{A}(s)}\pi(a\mid s)=1.
$$

The Markov property for the state transition is expressed as

$$
p(s_{t+1}\mid s_t,a_t,s_{t-1},a_{t-1},\ldots,s_0,a_0)=p(s_{t+1}\mid s_t,a_t).
$$

Similarly, the Markov property for the reward is

$$
p(r_{t+1}\mid s_t,a_t,s_{t-1},a_{t-1},\ldots,s_0,a_0)=p(r_{t+1}\mid s_t,a_t).
$$

These equations state that once the current state $s_t$ and action $a_t$ are known, the earlier interaction history provides no additional information about the probabilities of the next state or reward.