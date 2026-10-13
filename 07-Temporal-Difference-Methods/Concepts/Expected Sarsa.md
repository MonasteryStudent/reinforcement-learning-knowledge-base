## Definition

**Expected Sarsa** is a variant of [[Sarsa]] that estimates [[Action Value|action values]] using the expected action value of the next state.

Sarsa uses the value of a single next action selected according to the current [[Policy|policy]]. Expected Sarsa instead calculates the policy-weighted mean of the action values available in the next state.

This reduces the variance of the estimate because the update does not depend on a randomly sampled next action.

## Mathematical Formulation

The Expected Sarsa update is

$$
q_{t+1}(s_t,a_t)
=
q_t(s_t,a_t)
-
\alpha_t(s_t,a_t)
\left[
q_t(s_t,a_t)
-
\left(
r_{t+1}
+
\gamma
\mathbb{E}
\left[
q_t(s_{t+1},A)
\right]
\right)
\right].
$$

The action values of all other state-action pairs remain unchanged:

$$
q_{t+1}(s,a)=q_t(s,a),
\qquad
(s,a)\neq(s_t,a_t).
$$

The expected action value in the next state is

$$
\mathbb{E}
\left[
q_t(s_{t+1},A)
\right]
=
\sum_{a\in\mathcal{A}(s_{t+1})}
\pi_t(a\mid s_{t+1})
q_t(s_{t+1},a).
$$

This policy-weighted mean is the estimated [[State Value|state value]] of the next state:

$$
\mathbb{E}
\left[
q_t(s_{t+1},A)
\right]
=
v_t(s_{t+1}).
$$

The Expected Sarsa TD target is therefore

$$
r_{t+1}
+
\gamma
\sum_{a\in\mathcal{A}(s_{t+1})}
\pi_t(a\mid s_{t+1})
q_t(s_{t+1},a).
$$

Expected Sarsa can be viewed as a stochastic-approximation method for solving the action-value form of the [[Bellman Equation]]:

$$
q_\pi(s,a)
=
\mathbb{E}_\pi
\left[
R_{t+1}
+
\gamma
\mathbb{E}_\pi
\left[
q_\pi(S_{t+1},A_{t+1})
\mid
S_{t+1}
\right]
\middle|
S_t=s,A_t=a
\right].
$$

## Comparison with Sarsa

The TD target used by [[Sarsa]] is

$$
r_{t+1}
+
\gamma q_t(s_{t+1},a_{t+1}),
$$

where $a_{t+1}$ is sampled according to the current policy.

Expected Sarsa instead uses

$$
r_{t+1}
+
\gamma
\sum_{a\in\mathcal{A}(s_{t+1})}
\pi_t(a\mid s_{t+1})
q_t(s_{t+1},a).
$$

Expected Sarsa therefore considers every possible next action instead of relying on one sampled next action. Calculating this expected value requires slightly more computation but usually produces an estimate with lower variance.