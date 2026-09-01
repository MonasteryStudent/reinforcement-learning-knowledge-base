## Card 001

**Front**

What is a policy?

**Back**

A policy is a strategy that tells the agent how to select an action in every state.

**Tags**

01-Basics

## Card 002

**Front**

Write the normalization condition for the state-transition probability.

**Back**

For every state-action pair $(s,a)$,

$$
\sum_{s' \in \mathcal{S}} p(s' \mid s,a)=1.
$$

**Tags**

01-Basics

## Card 003

**Front**

What is reinforcement learning?

**Back**

Reinforcement learning is a learning approach in which an agent learns by interacting with an environment. Its objective is to learn a policy that maximizes the expected return.

**Tags**

01-Basics

## Card 004

**Front**

What is an agent?

**Back**

An agent is the decision-making entity in a reinforcement-learning problem. It selects actions according to its policy with the objective of producing a high expected return.

**Tags**

01-Basics

## Card 005

**Front**

What is the environment?

**Back**

The environment represents everything outside the agent that is relevant to the reinforcement-learning problem. It transitions to a next state and produces a reward in response to the agent's action.

**Tags**

01-Basics

## Card 006

**Front**

What is a state?

**Back**

A state describes the agent's current situation with respect to the environment. The information included in a state depends on how the reinforcement-learning problem is modelled.

**Tags**

01-Basics

## Card 007

**Front**

What is an action?

**Back**

An action represents a choice available to the agent in a particular state. By taking an action, the agent interacts with the environment.

**Tags**

01-Basics

## Card 008

**Front**

What is a reward?

**Back**

A reward is numerical feedback received by the agent after taking an action in a state. It indicates the immediate desirability of the outcome.

**Tags**

01-Basics

## Card 009

**Front**

What is a state transition?

**Back**

A state transition is the change from the agent's current state to a next state after the agent takes an action. Remaining in the same state also counts as a state transition.

**Tags**

01-Basics

## Card 010

**Front**

What is a trajectory?

**Back**

A trajectory is a sequence of states, actions, and rewards generated while the agent interacts with the environment according to a policy.

**Tags**

01-Basics

## Card 011

**Front**

What is the return?

**Back**

The return is the cumulative reward obtained from a particular time step onward along a trajectory.

**Tags**

01-Basics

## Card 012

**Front**

What is an episode?

**Back**

An episode is a trajectory that ends when the agent reaches a terminal state. It represents one complete trial of an episodic task and is usually assumed to be finite.

**Tags**

01-Basics

## Card 013

**Front**

What is a Markov decision process?

**Back**

A Markov decision process is a mathematical framework for describing sequential decision-making in a stochastic environment. It satisfies the Markov property.

**Tags**

01-Basics

## Card 014

**Front**

What is a Markov process?

**Back**

A Markov process describes the evolution of states where the probability of the next state depends only on the current state and not on the preceding state history.

**Tags**

01-Basics

## Card 015

**Front**

How is the reinforcement-learning objective expressed mathematically?

**Back**

The objective is

$$
\pi^* = \underset{\pi}{\arg\max} \mathbb{E}_{\pi}[G_t].
$$

It asks which policy $\pi$ maximizes the expected return.

**Tags**

01-Basics

## Card 016

**Front**

What conditions must the action probabilities of a stochastic policy satisfy?

**Back**

For every state $s$,

$$
\sum_{a \in \mathcal{A}(s)} \pi(a \mid s)=1
$$

and

$$
\pi(a \mid s)\geq 0
$$

for every available action $a$.

**Tags**

01-Basics

## Card 017

**Front**

How are the reward probabilities for a state-action pair normalized?

**Back**

For every state-action pair $(s,a)$,

$$
\sum_{r \in \mathcal{R}(s,a)} p(r \mid s,a)=1.
$$

Every reward probability must also be non-negative.

**Tags**

01-Basics

## Card 018

**Front**

How is the infinite-horizon discounted return defined?

**Back**

For a particular trajectory,

$$
g_t = \sum_{k=0}^{\infty}\gamma^k r_{t+k+1},
$$

where $\gamma \in (0,1)$ is the discount rate.

**Tags**

01-Basics

## Card 019

**Front**

How is the Markov property for state transitions in an MDP expressed?

**Back**

The Markov property is

$$
p(s_{t+1}\mid s_t,a_t,s_{t-1},a_{t-1},\ldots,s_0,a_0) = p(s_{t+1}\mid s_t,a_t).
$$

Once the current state and action are known, the preceding history provides no additional information about the next-state probability.

**Tags**

01-Basics

## Card 020

**Front**

How does a fixed policy determine the state-transition probability of the resulting Markov process?

**Back**

The transition probability is

$$
p_\pi(s' \mid s) = \sum_{a \in \mathcal{A}(s)} \pi(a \mid s)\,p(s' \mid s,a).
$$

It averages the MDP transition probabilities over the actions according to their probabilities under the fixed policy.

**Tags**

01-Basics

## Card 021

**Front**

What is the Markov Property?

**Back**

The Markov property refers to the memoryless property of a stochastic process. In an MDP, the Markov property means that, given the current state and action, the probabilities of the next state and reward are independent of the preceding interaction history.

**Tags**

01-Basics