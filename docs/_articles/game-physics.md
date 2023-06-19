---
layout: post
title:  "Relativistic dynamics in the game"
categories: SR
date: 2023-06-19 10:40:00
usemathjax: true
---

$$
\newcommand{\gammaB}{\gamma_{\mathrm{B}}}
\newcommand{\vF}{\mathbf{F}}
\newcommand{\va}{\mathbf{a}}
\newcommand{\vr}{\mathbf{r}}
\newcommand{\vvB}{\mathbf{v}}
\newcommand{\vvB}{\mathbf{v}_{\mathrm{B}}}
\newcommand{\uy}{\hat{\mathbf{y}}}
\newcommand{\uv}{\hat{\mathbf{v}}}
\newcommand{\uvB}{\hat{\mathbf{v}}_{\mathrm{B}}}
\newcommand{\vnabla}{\mathbf{\nabla}}
\newcommand{\deriv} [2]{\frac{\mathrm{d} #1}{\mathrm{d} #2}}
\newcommand{\ui}{u_{\mathrm{i}}}
\newcommand{\uf}{u_{\mathrm{f}}}
$$

# Introduction

What kind of Physics do games typically implement? Well, I guess the most used equation must be
Newton's second law of motion, $$\vF = m\va$$. This equation, however, is never the full
story. For example, to describe how two particles interact you need to define precisely the force,
$$\vF$$, that the particles exert on each other. And here is where a big problem arises for our
relativistic game.

You see, while Special Relativity offers its own version of Newton's second law,
most - if not all - of the force expressions that you can pick from a Classical Mechanics textbook
are pretty much useless in Special Relativity. Take Newton's law of gravitation or the
Coulomb law. These laws both assume "action at a distance", i.e. that the two particles interact
without any delay: if one particle moves, the other particle immediately "feels it", no matter
whether the particle is nearby or in a distant galaxy.

It could be argued that action at a distance is weird even from a classical standpoint. Indeed, it
is not very clear how two events that occur exactly at the same time, i.e. the movement of the first
particle and the change of force acting on the second particle, can be causally linked. In classical
mechanics, however, it is easy to close one eye, then close the other eye and forget about it. The
maths works well and the issue is kind-of a philosophical/metaphysical one.

That's different in Special Relativity. According to this theory, action at a distance is
unphysical, unacceptable. Information cannot propagate faster than the speed of light. There must
thus be a delay between the movement of a particle and the ability of the other particle to "sense"
the change.

So... how do particles interact in Special Relativity? Well, they rely on the mediation of a
"field". For example, two electrically charged particles interact thanks to the mediation of the
electromagnetic field. When one particle moves, the field changes through space and time. The change
propagates at the speed of light from the first particle towards the second particle. Only once it
reaches the second particle, can it know that the first particle moved.

The "right" thing to do in Special Relativity would be to model interactions between objects via
fields. This, however, would require keeping track of the value of the field for every point in
space (and time, possibly.) This approach quickly becomes unmanageable, especially for 2 and 3
spatial dimensions. It requires too much memory and computational power.

Are there any shortcuts we could take and avoid keeping track of the entire field, while maintaining
consistency with respect to Special Relativity? Well, this is what this article is about. I'll be
documenting the key ideas behind the implementation of physical interactions in my game.  This will
be an open article, like others in this site: I'll keep updating it as I go along with the
development.

# What is necessary and what is sufficient

The aim for the game is to come up with interactions that can be made-up, but must be physically
correct.

- By made-up I mean that the interactions do not need to closely mimic any real phenomena.
  For example, the interaction of the player with another object may be a short range interaction
  that vanishes when the distance between the two objects grows above a certain threshold. In a way,
  this isn't much different than what happens in ordinary games. Maybe the biggest difference is
  that ordinary games tend to reproduce, albeit in an exaggerated fashion, mechanisms that their
  players experience in the real world, like the parabolic trajectory that an object follows when
  it is thrown in the air. Players of a relativistic game completely lack an everyday intuition
  of relativistic Physics, so there isn't much of a constraint between reality and game fiction.

- By physically correct I mean that all physics must respect causality and must be consistently
  describable in any intertial reference frame.

The other point to clarify is what is interacting with what. Are we talking about extended bodies
interacting with each other. Or are we talking about particles?

The general case of two extended bodies, say Born-rigid, interacting with each other is somewhat
difficult to deal with. I'd say even difficult to make sense of. In particular, it is unclear how
the spatial extent of two Born-rigid bodies may factor into the interaction.
Instead, we will start considering the player interacting with - say - floor, walls, doors and
other objects. In this situation, we have:

- one object, "the player", that is Born-rigid and can accelerate, Lorentz-contract, Wigner-rotate.
  This object is affected by the iteraction with other objects, such as walls, doors, etc.

- another object, we call it "the block", that is typically stationary. It may accelerate, but
  we don't necessarily require it to be affected by the interaction with the other object.
  A bit like the Earth is not affected by people jumping on it.

Initially, we will consider the player as point-like and we will try to model the block with a
known "force field", a bit how you'd model the interaction of a ball in Earth's gravity within
the framework of classical mechanics. In particular, we assume we are given a
[Signed Distance Function (SDF)](https://en.wikipedia.org/wiki/Signed_distance_function)
(find some [here](https://iquilezles.org/articles/distfunctions/)) that models the shape
of the block, $$s(\vr)$$. It would be tempting to adopt the reference frame of the block,
and in that reference frame, write the acceleration of the player as:

$$
\begin{equation}
\va = C \, f(s) \mathbf{\nabla} s,
\label{eq:naive_proposal}
\end{equation}
$$

where $$C$$ is a constant and $$f(s)$$ is a function that determines how the strength of the force
field depends on the distance from the surface of the block.

For example, for a sphere of radius $$R_0$$, we have $$s(\vr) = \|\vr\| - R_0$$
and $$\vnabla s = \vr/\|\vr\|$$ points radially outwards from the center of the sphere.
$$f(s)$$ then controls the strength of the interaction based on the distance of the player
from the sphere's surface.
For example, a choice for $$f$$ may be $$f(s) = \min(0, s).$$ This gives zero acceleration if
the player is outside the sphere ($$s \ge 0$$) and an acceleration pointing out of the sphere's
center more and more as the player enters deeper and deeper into the sphere, thus getting
close to its center ($$s < 0$$).

The problem with Eq. \eqref{eq:naive_proposal} is that it complely forgets that we are doing
relativistic Physics, beside not dealing with the issue that the reference frame of the block
may not be intertial. Despite all the flaws, the core idea is interesting. We just need to
develop it a bit and make it more solid.

Eq. \eqref{eq:naive_proposal} would actually work in classical non-relativistic Physics.
One idea is then to search a rewriting that is invariant with respect to Lorentz transformations.
That's not hard. $$\vnabla s$$ transforms as a covariant vector, so we can make it
contravariant by multiplying it by the Minkowsky metric,
e.g. $$\eta = \mathrm{diag}(-1,\,-1,\,-1,\,1)$$:

$$
\begin{equation}
A^{\mu} = -C \, f(s) \, \eta^{\mu\nu} \partial_{\nu} s.
\label{eq:better_proposal}
\end{equation}
$$

The minus sign ensures this expression reduces to Eq. \eqref{eq:naive_proposal} in the classical
limit. This approach, however, requires us to extend the definition of $$s$$ and make it an
invariant function of both time and space: $$s(\vr,\,t)$$. That requires a bit of thought.
We'll tackle this problem in the next section. Let's continue assuming we have solved this problem
and have obtained a "suitable" function $$s(\vr,\,t)$$.

Another problem with Eq. \eqref{eq:better_proposal} is that it gives a four-vector that is not
a four-acceleration. Indeed, the four-acceleration must be orthogonal to the four-velocity.
This property emerges from the constancy of the norm of the four-velocity.
One way we can deal with this problem is to project the expression in Eq. \eqref{eq:better_proposal}
as follows:

$$
\begin{equation}
A^{\mu} \longrightarrow A^{\mu} - \frac{A^{\nu} U_{\nu}}{c^2} \, U^{\mu}.
\label{eq:projection}
\end{equation}
$$

This is a invariant expression, so the overall expression for $$A^{\mu}$$ continues to be invariant.

# Invariant extension of the SDF function

First, let's cosider the case when the block moves with constant velocity.
It makes sense to assume that the reference frame moving with the block sees the regular,
spatial SDF, $$S(\vr')$$. Any other reference frames will then see this scalar function contracted
and moving: $$s(\vr,\,t) = S(\vr'(\vr, t))$$. $$\vr'(\vr, t)$$ is just a Lorentz transformation
mapping the coordinates $$(\vr,\,t)$$ to the coordinates in the reference frame moving
with the block, $$(\vr',\,t')$$. $$t'$$ doesn't matter, as $$S$$ does not change in time.
Using the result from [this post](boosts-3d), we can write:

$$
\begin{equation}
s(\vr,\,t) = S(\vr - \vr_0
               + (\gammaB - 1) \uvB \, \left[\uvB \cdot (\vr - \vr_0) \right]
               - \gammaB \vvB\,t),
\label{eq:sdf_const_speed}
\end{equation}
$$

where $$\vr_0$$ is the position of the block at time $$t=0$$.

Note how substituting $$\vr = \vr_0 + \vvB\,t$$, gives: $$s(\vr_0 + \vvB\,t,\,t) = S(0)$$,
as expected.

# Example: plane moving with constant velocity

Let's take the SDF of the $$x$$-$$z$$ plane, $$S(\vr) = \vr \cdot \uy$$.
This could be used to model the interaction of the player with the floor, for example.
If we take $$\vr_0 = 0$$, we can write Eq. \eqref{eq:sdf_const_speed} as follows:

$$
\begin{equation}
s(\vr,\,t) = \vr \cdot \uy + (\gammaB - 1) (\uvB \cdot \uy) \, (\uvB \cdot \vr )
           - \gammaB (\uvB \cdot \uy)\,t,
\label{eq:s_example}
\end{equation}
$$

This expression is not immediately recogniseable as an invariant scalar.
However, if we go back to the expression for $$S,$$ we can easily rewrite $$S = R^{\mu} Y_{\mu}$$,
where $$R$$ is the four-position and $$Y$$ is a four-vector whose components --
seen from the reference frame moving with the block -- are all zero, except for the
$$y$$-component which is one.
This expression for $$S$$ is invariant for Lorentz transformations and coincides with $$s$$
in the reference frame travelling with the block.
It follows, that it must be identical to Eq. \eqref{eq:s_example}. This can be easily verified
by transforming $$Y$$ according to [this post](boosts-3d).

Eq. \eqref{eq:better_proposal} becomes:

$$
A^{\mu} = C \, f(s) \, Y^{\mu}.
$$

We now apply Eq. \eqref{eq:projection} and obtain:

$$
A^{\mu} = C \, f(s) \, \left( Y^{\mu} - \frac{Y^{\nu}U_{\nu}}{c^2} U^{\mu} \right),
$$

and, for example, $$f(s) = \min(0,\,R^{\nu}Y_{\nu})$$.

# To be continued...
