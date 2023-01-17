---
layout: post
title:  "Length contraction for light pulses"
categories: SR
date: 2023-01-16 17:54:00
usemathjax: true
---
# Introduction

I recently published a video, see below.

{% include youtube.html id='XkoZ9oq06fM' %}
&nbsp;

The video shows a light pulse propagating inside a special glass pipe.
The video is subdivided in two parts, which show the same scene from two different points of view.
In the first part of the video, the scene is observed from the ground and the light guide
is not moving. In the second part, the scene is observed from a train that moves in the same
direction of the propagating light. Interestingly, the light pulse appears much wider in the second
case. In this article we understand why this is the case.
$$
\newcommand{\vT}{v_{\mathrm{T}}}
\newcommand{\vP}{v_{\mathrm{P}}}
\newcommand{\betaT}{\beta_{\mathrm{T}}}
\newcommand{\betaP}{\beta_{\mathrm{P}}}
$$

# Intuitive explanation

The "expansion" of the pulse in the second case can be understood intuitively. Imagine
the pulse was not made of light but instead some fluid moving at a lower speed, $$\vP < c$$.
A train moving in the same direction with speed, $$\vT < \vP$$, would see the fluid moving slower
than what seen from the ground.
Consequently, the pulse would appear less Lorentz-contracted and hence wider.

Admittedly, Lorentz contraction doesn't quite work for objects that go exactly at the speed
of light. The contraction factor,

$$
\begin{equation}
F(\vP) = \sqrt{1 - \frac{\vP^2}{c^2}},
\label{eq:contract_factor}
\end{equation}
$$

becomes zero when $$\vP$$ approaches the speed of light, $$c$$:
photons are infinitely contracted along their direction of travel.

Still, it is reasonable to expect that a fluid moving at speeds close to the speed of light
would well approximate the behaviour of a light pulse, at least when seen from a train that moves
slowly compared to the pulse.

# Derivation

The contraction of the light pulse can be easily calculated by transforming the trajectories
of the light pulse boundaries via the
[Lorentz transformation](https://en.wikipedia.org/wiki/Lorentz_transformation).
Here we follow a perhaps more interesting approach. We continue riding the idea that the pulse
is travelling at a speed $$\vP$$, lower than the speed of light. We find what happens in this case.
Then, we increase the speed of the pulse, $$\vP \rightarrow c$$.

We start from the relativistic
[velocity addition formula](https://en.wikipedia.org/wiki/Velocity-addition_formula)
and calculate the speed of the pulse seen from the train's reference frame, $$\vP'$$:

$$
\begin{equation}
\betaP' = \frac{\betaP - \betaT}{1 - \betaP \betaT},
\label{eq:composition}
\end{equation}
$$

where we introduced $$\betaP' = \vP'/c$$, $$\betaP = \vP/c$$, $$\betaT = \vT/c$$.
Note that, from the formula above, $$\betaP'$$ is zero when the train moves as fast as the pulse
($$\vT = \vP$$). This is how it should be, although here we assume $$\vP \gg \vT$$.

The contraction factor, C, is the ratio between the pulse's Lorentz contraction as seen
from the moving reference frame and the one as seen from the ground.
Both factors are given by \eqref{eq:contract_factor}:

$$
C(\vT,\,\vP) = \frac{F(\vP')}{F(\vP)} = \sqrt{\frac{1 - (\betaP')^2}{1 - \betaP^2}}.
$$

Substituting $$\betaP'$$ from \eqref{eq:composition}, we rewrite this as follows:

$$
\sqrt{\frac{(1 - \betaP \betaT)^2 - (\betaP - \betaT)^2}{(1 - \betaP \betaT)^2 (1 - \betaP^2)}},
$$

which can be simplified to:

$$
C(\vT,\,\vP) = \frac{\sqrt{1 - \betaT^2}}{1 - \betaP \betaT}.
$$

For $$\vP \rightarrow c$$, we get $$\betaP \rightarrow 1$$ and
thus $$C = \sqrt{1 - \betaT^2}/(1 - \betaT)$$, or, equivalently:

$$
\bbox[lightyellow, 10px, border: 2px solid orange]{
\begin{equation*}
C = \sqrt{\frac{1 + \betaT}{1 - \betaT}}.
\end{equation*}
}
$$

In the video I posted, the train is travelling at 94% the speed of light, or, more precisely,
the speed at which the train contracts to 1/3 of its rest length.
At this speed, the factor $$C$$ is calculated as $$C \approx 5.83$$.

It is interesting that this factor, $$C$$, is considerably larger than the train contraction
factor, 3. In fact, for $$\betaT \rightarrow 1$$, we have

$$
C \approx \frac{\sqrt{2}}{\sqrt{1 - \betaT}},
$$

and

$$
\gamma_{\mathrm{T}} \equiv \frac{1}{F}
= \frac{1}{\sqrt{1 - \betaT^2}} \approx \frac{1}{\sqrt{2}\sqrt{1 - \betaT}},
$$

which gives:

$$
C \approx 2 \gamma_{\mathrm{T}} \quad (\mathrm{for\,}\betaT \approx 1)
$$

# Conclusion

In agreement to what is shown in the video, the width of a light pulse dilates more and more
as the observer increases its velocity in the direction of the pulse.
For the conditions chosen in the video, the dilation should be roughly a factor 6.

The dilation shown in the video is clearly larger than that. Counting the pixels
in the two scenes I get $$C \approx 15.6$$. I believe this discrepancy comes from the way
the pulse is triggered. As can be spotted by looking at the video, the collision mechanism I
implemented in the game is currently not very accurate and not perfectly covariant, meaning that
it depends on the particular choice of reference frame.
I plan to improve this aspect of the game. I will then rerun the simulation and compare
the measured value for $$C$$ with the expected value, 5.83.
The two should match closely, I believe.
I'll update this post when this happens, so watch this space!
