## Definition

A **visit** occurs whenever a state-action pair $(s,a)$ appears in an [[Episode|episode]].

Different visit strategies determine which parts of an episode are used for [[Monte Carlo Estimation]]:

- The **initial-visit strategy** uses an episode only to estimate the [[Action Value|action value]] of its initial state-action pair. This strategy is used by [[MC Basic]].
- The **first-visit strategy** uses only the first occurrence of each state-action pair in an episode.
- The **every-visit strategy** uses every occurrence of each state-action pair in an episode.

The first-visit and every-visit strategies use an episode more efficiently because the trajectory following each visit can be treated as a subepisode.

The every-visit strategy uses the greatest number of samples. However, returns obtained from repeated visits within the same episode may be correlated because their subepisodes overlap.

## Mathematical Formulation

Consider an episode

$$
S_0,A_0,R_1,S_1,A_1,\ldots,S_{T-1},A_{T-1},R_T,S_T.
$$

The set of time steps at which $(s,a)$ is visited is

$$
\mathcal{V}(s,a)=\{t\mid S_t=s,\ A_t=a\}.
$$

The observed [[Return|return]] following a visit at time step $t$ is

$$
g_t=\sum_{k=0}^{T-t-1}\gamma^k r_{t+k+1}.
$$

The strategies use these returns differently:

- **Initial visit:** Use only $g_0$ for the initial pair $(S_0,A_0)$.
- **First visit:** Use $g_t$ for $t=\min\mathcal{V}(s,a)$.
- **Every visit:** Use $g_t$ for every $t\in\mathcal{V}(s,a)$.

If $N(s,a)$ returns have been collected for a state-action pair, its action value is estimated as

$$
\widehat{q}(s,a)=\frac{1}{N(s,a)}\sum_{i=1}^{N(s,a)}g^{(i)}(s,a).
$$