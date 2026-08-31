## Definition

An **action** represents a choice available to the [[Agent|agent]] in a particular [[State|state]]. By taking an action, the agent interacts with the [[Environment|environment]] and may cause a [[State Transition|state transition]] and receive a [[Reward|reward]].

The set of actions available in a state is called the **action space**. Different states may have different action spaces.

## Mathematical Formulation

An individual action is denoted by $a$. The action space associated with state $s$ is denoted by $\mathcal{A}(s)$. Therefore,

$$
a \in \mathcal{A}(s).
$$

If $m$ actions are available in state $s$, the action space can be written as

$$
\mathcal{A}(s)=\{a_1,a_2,\ldots,a_m\}.
$$

If every state has the same action space, it can be denoted by $\mathcal{A}$, such that

$$
\mathcal{A}(s)=\mathcal{A}
$$

for every $s \in \mathcal{S}$.