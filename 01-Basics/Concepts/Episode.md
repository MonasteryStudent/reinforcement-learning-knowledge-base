## Definition

An **episode** is a [[Trajectory|trajectory]] that ends when the [[Agent|agent]] reaches a terminal [[State|state]]. It represents one complete trial of an episodic task and is usually assumed to be finite.

A **continuing task** has no terminal state, so the interaction continues indefinitely. Strictly speaking, this produces an infinite trajectory rather than a continuing episode.

Zhao treats episodic and continuing tasks within a unified mathematical framework by defining what happens after the terminal state is reached. The finite episode can then be extended into an infinite trajectory.

He describes two possible treatments of the terminal state:

1. The terminal state can be treated as an **absorbing state**. Once reached, the agent remains there forever, regardless of which available [[Action|action]] it selects.
2. The terminal state can be treated as a normal state. The agent may leave it and return later.

If an infinite trajectory produces positive [[Reward|rewards]] indefinitely, a discount rate is required to prevent the [[Return|return]] from growing without bound.

## Mathematical Formulation

A particular episode beginning at time step $0$ and terminating at time step $T$ can be represented as

$$
\tau_{\mathrm{episode}} = (s_0,a_0,r_1,s_1,a_1,r_2,\ldots,a_{T-1},r_T,s_T),
$$

where $s_T$ is the terminal state.

A continuing trajectory has no terminal time and can be represented as

$$
\tau_{\mathrm{continuing}}
=
(s_0,a_0,r_1,s_1,a_1,r_2,s_2,\ldots).
$$

To convert an episodic task into a continuing one, the terminal state can be made absorbing. One option is to give it only a stay action:

$$
\mathcal{A}(s_T)=\{a_{\mathrm{stay}}\},
$$

with

$$
p(s_T\mid s_T,a_{\mathrm{stay}})=1.
$$

Alternatively, the terminal state can retain the full action space,

$$
\mathcal{A}(s_T)=\mathcal{A},
$$

while every action produces a self-transition:

$$
p(s_T\mid s_T,a)=1
\qquad
\text{for every }a\in\mathcal{A}.
$$

The original episode is then followed by an infinite sequence of transitions within the absorbing state:

$$
\ldots,a_{T-1},r_T,s_T,
a_T,r_{T+1},s_T,
a_{T+1},r_{T+2},s_T,\ldots
$$

If the terminal state is instead treated as a normal state, transitions to other states remain possible:

$$
p(s'\mid s_T,a)>0
$$

may hold for some $s'\neq s_T$ and some $a\in\mathcal{A}(s_T)$.