---
layout: post
title:  "Analytical positioning of bodies (WIP)"
categories: SR
usemathjax: true
---

# Introduction

In the relativistic game I am writing every physical object is a
[Born-rigid body](http://en.wikipedia.org/wiki/Born_rigidity) which moves along a piece-wise
[hyperbolic trajectory](https://en.wikipedia.org/wiki/Hyperbolic_trajectory).
More could be said about this choice. I will reserve this for a different post.
Let's continue and say that hyperbolic trajectories arise when a particle (or body)
experiences anacceleration which is constant in time. This is different than what happens
for a classical particle, whose trajectory is a parabola rather than an hyperbola.

In games it is often necessary to move objects to a desired position. Imagine a ghost chasing
Pacman or wanting to return to the ghosts' home. One way this can be achieved is by changing
the velocity or applied force frame by frame, so that it points toward the destination at all
times. A possibility that provides more flexibility is using Bezier curves or splines for the
trajectories.

In the case of Special Relativity, it is desirable to move the bodies "physically", i.e.
applying forces rather than directly changing the velocities. Moving bodies "physically" is
less likely to lead to physics that violates causality or depends on the choosen reference frame.
The problem of how to move a particle by applying successive constant forces is therefore
an interesting problem to solve. In this article, I am going to pose the problem more rigorously
and provide a classical solution to it. The relativistic case is considerably more complicated,
but I hope that the classical solution can guide me towards the relativistic solution.

# Problem statement
We have a point-like particle in 3D space with known position, $$\mathbf{r}_{\mathrm{I}}$$, and
velocity, $$\mathbf{v}_{\mathrm{I}}$$, at an initial time, $$t_{\mathrm{I}}$$.  We want to move the
particle so that it has a different position, $$\mathbf{r}_{\mathrm{F}}$$, and a different
velocity, $$\mathbf{v}_{\mathrm{F}}$$, at a later time $$t_{\mathrm{F}} > t_{\mathrm{I}}$$.

The problem is sketched in the figure below:

![sketch of the analytical positioning problem](/assets/analytical-positioning-figure-1.svg)

We want to move the particle in the "simplest possible" way...
For example, we could apply just a constant force (uniform acceleration) between time
$$t_{\mathrm{I}}$$ and $$t_{\mathrm{F}}$$. Alternatively, if applying a single constant force
is not enough to solve the problem generally, we could subdivide the time
interval [$$t_{\mathrm{I}}$$, $$t_{\mathrm{F}}$$] in two or more intervals and apply a different
constant force in each subsequent interval.

# Classical case

Clearly, it is not possible to solve the problem generally by applying one single force.
Take the case where the initial and final velocities are both zero but the initial and final
positions are distinct. We must apply a force to move the particle away from its initial position,
but a constant force would then only keep increasing the particle's velocity, which we want to
be again zero at the destination point.

Let's try, instead, to subdivide the trajectory in two pieces.
From time $$t_{\mathrm{I}}$$ to $$t_{\mathrm{M}}$$ a uniform acceleration
$$\mathbf{a}_{\mathrm{I}}$$ is applied.
From time $$t_{\mathrm{M}}$$ to $$t_{\mathrm{F}}$$ a different uniform acceleration
$$\mathbf{a}_{\mathrm{F}}$$ is applied.

![sketch with two subdivisions](/assets/analytical-positioning-figure-2.svg)

Before we write down any equations, we apply the following coordinate transformation:

$$
\newcommand{\vini}[1]{\mathbf{#1}_{\mathrm{I}}}
\newcommand{\vmid}[1]{\mathbf{#1}_{\mathrm{M}}}
\newcommand{\vfin}[1]{\mathbf{#1}_{\mathrm{F}}}
\newcommand{\ini}[1]{#1_{\mathrm{I}}}
\newcommand{\fin}[1]{#1_{\mathrm{F}}}
\newcommand{\vvr}{\mathbf{r}}
\newcommand{\vvv}{\mathbf{v}}
\newcommand{\vva}{\mathbf{a}}
\begin{equation}
\mathbf{r}' =
  \mathbf{r}
  - \frac{\vini{r} + \vfin{r}}{2}
  - \frac{\vini{v} + \vfin{v}}{2} \,
    \left(t - \frac{\ini{t} + \fin{t}}{2}\right).
\label{eq:transf_r}
\end{equation}
$$

Deriving with respect to time, we obtain the transformation equation for velocities:

$$
\begin{equation}
\mathbf{v}' =  \mathbf{v} - \frac{\vini{v} + \vfin{v}}{2}.
\label{eq:transf_v}
\end{equation}
$$

In this reference frame, final position and velocity are just the opposite
of the initial position and velocity, respectively.
This can be seen by inserting $$\vvr = \vini{r},\, \vfin{r}$$ in Eq. $$\eqref{eq:transf_r}$$
and $$\vvv = \vini{v},\, \vfin{v}$$ in Eq. $$\eqref{eq:transf_v}$$:

$$
\begin{eqnarray}
\vini{r}' & = & \frac{\vini{r} - \vfin{r}}{2} - \frac{\vini{v} + \vfin{v}}{2} \,
  \frac{\ini{t} - \fin{t}}{2}, \nonumber\\
\vfin{r}' & = & \frac{\vfin{r} - \vini{r}}{2} - \frac{\vini{v} + \vfin{v}}{2} \,
  \frac{\fin{t} - \ini{t}}{2} = -\vini{r}', \nonumber\\
\vini{v}' & = & \frac{\vini{v} - \vfin{v}}{2}, \nonumber\\
\vfin{v}' & = & \frac{\vfin{v} - \vini{v}}{2} = -\vini{v}',\nonumber
\end{eqnarray}
$$

Let us now write down the trajectory of the particle for the two parts:

$$
\begin{eqnarray}
\vvr'(t) & = &
  -\mathbf{R} - \mathbf{V} \, (t - \ini{t}) + \frac{1}{2} \vini{a} \, (t - \ini{t})^2
\nonumber\\
\vvr'(t) & = &
   \mathbf{R} + \mathbf{V} \, (t - \fin{t}) + \frac{1}{2} \vfin{a} \, (t - \fin{t})^2
\nonumber
\end{eqnarray}
$$

Above, we renamed the quantities as follows:
$$\mathbf{R} = \vfin{r}'$$, $$\mathbf{V} = \vfin{v}'$$.

These two trajectories have to join up at a time $$t_M$$, with $$\ini{t} < t_M < \fin{t}$$.
In particular, positions and velocities of these two trajectories must match at time $$t_M$$.
The constraint on matching positions is easily written as:

$$
\vini{a} \, \ini{T}^2 - \vfin{a} \, \fin{T}^2
= 4 \mathbf{R} + 2 \mathbf{V} \, (\ini{T} - \fin{T})
$$

where we have introduced $$\ini{T} = t_M - \ini{t}$$ and $$\fin{T} = \fin{t} - t_M$$.
The constraints on matching velocities at time $$t_M$$ gives:

$$
\vini{a} \, \ini{T} + \vfin{a} \, \fin{T} = 2\mathbf{V}
$$

This is solved to:

$$
\begin{eqnarray*}
\vini{a} & = & \frac{2 \mathbf{V}}{T} + \frac{4 \mathbf{R}}{\ini{T} T},\\
\vfin{a} & = & \frac{2 \mathbf{V}}{T} - \frac{4 \mathbf{R}}{\fin{T} T},
\end{eqnarray*}
$$

where we have introduced $$T = \ini{T} + \fin{T} = \fin{t} - \ini{t}$$.

We found a different solution for each different choice of $$t_M$$.
One possible choice of $$t_M$$ is $$(\ini{t} + \fin{t})/2$$,
i.e. the mid-point between $$\ini{t}$$ and $$\fin{t}$$,
which corresponds to $$\ini{T} = \fin{T} = T/2$$.
This is probably the simplest choice of $$t_M$$ and makes the trajectory
construction "time-symmetrical". In other words, the trajectory constructed
by flipping $$\mathbf{R} \rightarrow -\mathbf{R}$$ goes from $$-\mathbf{R}$$
to $$\mathbf{R}$$, following exactly the reversed path.
This would not be the case, if we choose -- say -- $$t_M = (\ini{t} + \fin{t})/3$$.
It should be noted, however, that there may be other ways of choosing $$t_M$$,
based on the initial conditions of the problem, that have the same time-reversal property.

Let's conclude this section by rewriting the result in the case $$\ini{T} = \fin{T} = T/2$$.
We get $$\vini{a} = \frac{\mathbf{2V}}{T} + 8\frac{\mathbf{R}}{T^2}$$
and $$\vfin{a} = \frac{\mathbf{2V}}{T} - 8\frac{\mathbf{R}}{T^2}$$, or, in terms
of the original positions and velocities,

$$
\bbox[lightyellow, 10px, border: 2px solid orange]{
\begin{eqnarray*}
  \vini{a} & = &  -\frac{3\vini{v} + \vfin{v}}{\fin{t} - \ini{t}}
             - 4 \frac{\vini{r} - \vfin{r}}{(\fin{t} - \ini{t})^2} \\
  \vfin{a} & = &  \frac{\vini{v} + 3\vfin{v}}{\fin{t} - \ini{t}}
             + 4 \frac{\vini{r} - \vfin{r}}{(\fin{t} - \ini{t})^2}
\end{eqnarray*}
}
$$
