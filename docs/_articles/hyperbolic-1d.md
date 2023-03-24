---
layout: post
title:  "Derivation of hyperbolic motion in one spatial dimension"
categories: SR
date: 2023-02-13 10:40:00
usemathjax: true
---

$$
\DeclareMathOperator{\asinh}{asinh}
\DeclareMathOperator{\atanh}{atanh}
\DeclareMathOperator{\sinhc}{sinhc}
\newcommand{\insR}{\mathbb{R}}
\newcommand{\deriv} [2]{\frac{\mathrm{d} #1}{\mathrm{d} #2}}
\newcommand{\gammai}{\gamma_{\mathrm{i}}}
\newcommand{\thetai}{\theta_{\mathrm{i}}}
\newcommand{\tf}{t_{\mathrm{f}}}
\newcommand{\Ti}{T_{\mathrm{i}}}
\newcommand{\Tf}{T_{\mathrm{f}}}
\newcommand{\omegai}{\omega_{\mathrm{i}}}
\newcommand{\ui}{u_{\mathrm{i}}}
\newcommand{\gammaf}{\gamma_{\mathrm{f}}}
\newcommand{\omegaf}{\omega_{\mathrm{f}}}
\newcommand{\uf}{u_{\mathrm{f}}}
$$

# Derivation

In this article we derive the formulas for hyperbolic motion in one dimension.
Let's start by considering a point-like particle and choose an inertial frame $$\mathcal{R}$$
such that the trajectory of the particle passes through the origin.
We here assume that both the velocity and the acceleration of the particle
are directed along the $$x$$ axis.
It is reasonable to expect that the trajectory of such a particle
can written as $$(x(t),\,0,\,0,\,t)$$.

When we say that the particle is uniformly accelerated, we mean that
the particle accelerates uniformly from one inertial frame to the next.
This means that, if we consider an arbitrary point $$\mathrm{Q}\in\insR^4$$
of the particle trajectory and we express the trajectory in an intertial
frame tangent to the trajectory in $$\mathrm{Q}$$ we expect to always get the
same expression, independently from the choice of $$\mathrm{Q}$$.

So let us return to the reference frame $$\mathcal{R}$$ and let us choose
a time $$t_1$$. The particle will be at $$x_1 \equiv x(t=t_1)$$
on the $$x$$ axis and have a velocity $$u_1 \equiv u(t=t_1)$$ also directed
along the $$x$$ direction.
At a subsequent time $$t_2 = t_1 + \Delta t$$ the particle will be at
position $$x_2$$ with velocity $$u_2$$.
Let us consider the inertial reference frame, $$\mathcal{R}'$$,
where $$x_1'$$ and $$u_1'$$ are both zero. This frame moves with velocity
$$u_1$$ with respect to $$\mathcal{R}$$.
In this frame the particle is seen accelerating from standstill
between time $$t_1'$$ and time $$t_2'$$.
If $$t_2'$$ is sufficiently close to $$t_1'$$, then
the classical limit must hold and the velocity must be well approximated
by $$u' = a \, \Delta t' = a \, (t_2' - t_1')$$, where $$a$$ is the proper
acceleration. We can now compute the velocity in the reference frame
$$\mathcal{R}$$ using the relativistic law of composition of velocities:

$$
u = \frac{u_1 + a \, \Delta t'}{1 + (u_1 a\, \Delta t')/c^2},
$$

and

$$
\Delta u = u - u_1 =
\frac{1 - u_1^2/c^2}{1 + (u_1 a\, \Delta t')/c^2} \, a \, \Delta t'.
$$

The limit $$\Delta t' \rightarrow 0$$ gives:

$$
\Delta u = u - u_1 =
\left(1 - u_1^2/c^2\right) \, a \, \Delta t'.
$$

$$\Delta t'$$ is the proper time, i.e. an interval of time measured
from the reference frame which moves with the particle. This is
related to the time seen from $$\mathcal{R}$$ as follows:
$$\Delta t = \gamma_1 \Delta t'$$, where $$\gamma_1 = 1/\sqrt{1 - u_1^2/c^2}$$.
Substituting this into the previous equation we get:

$$
\deriv{u}{t} = a \, \gamma^{-3} = \left(1 - u^2/c^2 \right)^{3/2},
$$

where the index 1 was omitted as this derivation can be done
for any value of the time $$t_1$$.

This equation can be solved doing the substitutions
$$\sin \theta = u/c$$ and $$T = at/c$$:

$$
\deriv{\theta}{T} = \cos^2 \theta.
$$

which is easily integrated to:

$$
\int_{\thetai}^{\theta}
  \frac{\mathrm{d}\Theta}{\cos^2 \Theta} =
\tan \theta - \tan \thetai = T.
$$

Substituting $$\sin \theta = u/c$$, we have:

$$
\begin{equation}
\sin \theta = \frac{u}{c} = \frac{T + \Ti}{\sqrt{1 + (T + \Ti)^2}},
\label{eq:sin_theta}
\end{equation}
$$

where we introduced $$\Ti \equiv \tan \thetai$$.
Note that, taking $$T = 0$$ (i.e., $$t = 0$$) in the equation above, we get to:

$$
\frac{\ui}{c} = \frac{\Ti}{\sqrt{1 + \Ti^2}}
\Rightarrow
\Ti = \frac{\gammai \ui}{c}.
$$

From \eqref{eq:sin_theta} we can compute $$\gamma = (1 - (u/c)^2)^{-1/2}$$:

$$
\gamma = \left[1 - \frac{(T + \Ti)^2}{1 + (T + \Ti)^2} \right]^{-1/2}
= \sqrt{1 + (T + \Ti)^2}
$$

We can integrate the velocity formula \eqref{eq:sin_theta} to obtain the position:

$$
x = \int_0^{\tf} u \, \mathrm{d}t =
\frac{c^2}{a} \int_0^{\Tf} \frac{u}{c} \, \mathrm{d}T
$$

Changing variable of integration to $$\Theta$$ as above:

$$
x =
\frac{c^2}{a} \int_{\thetai}^{\theta}
  \frac{\sin \Theta}{\cos^2 \Theta} \, \mathrm{d}\Theta =
-\frac{c^2}{a} \int_{\cos \thetai}^{\cos \theta}
  \frac{\mathrm{d}\cos \Theta}{\cos^2 \Theta}
$$

which gives:

$$
x =
\frac{c^2}{a} \left( \frac{1}{\cos \theta} - \frac{1}{\cos \thetai} \right).
$$

From Eq. \eqref{eq:sin_theta} we deduce that
$$\cos^{-1} \theta = \sqrt{1 + (T + \Ti)^2} = \gamma$$
and $$\cos^{-1} \thetai = \sqrt{1 + \Ti^2} = \gammai$$. We thus have:

$$
\begin{equation*}
x = \frac{c^2}{a} \left( \gamma - \gammai \right)
\end{equation*}
$$

and,

$$
\bbox[lightyellow, 10px, border: 2px solid orange]{
\begin{equation*}
x(t) = \frac{c^2}{a} \left(
  \sqrt{1 + \left(\frac{at}{c} + \frac{\gammai \ui}{c}\right)^2} - \gammai \right).
\end{equation*}
}
$$

This expression has a removable singularity in $$a = 0$$, which isn't well suited for numerical
computation. We can solve the issue by multiplying the right hand side by
$$(\gamma + \gammai)/(\gamma + \gammai)$$:

$$
\begin{eqnarray*}
x & = & \frac{c^2}{a} \frac{\gamma^2 - \gammai^2}{\gamma + \gammai} \\
& = & \frac{c^2}{a(\gamma + \gammai)}
  \left[1 + \left(\frac{at}{c} + \frac{\gammai \ui}{c}\right)^2 - \gammai^2\right]\\
& = & \frac{a t^2 + 2 \gammai \ui \, t}{\gamma + \gammai}.
\end{eqnarray*}
$$

Above, we used the identity: $$1 + \frac{\gammai^2 \ui^2}{c^2} - \gammai^2 = 0$$.

In summary:

$$
\begin{equation}
\bbox[lightyellow, 10px, border: 2px solid orange]{
\begin{aligned}
\gamma(t) & = \sqrt{1 + \left( \frac{at}{c} + \frac{\gammai \ui}{c} \right)^2}, \\
u(t) & = \frac{at + \gammai \ui}{\gamma(t)}, \\
x(t) & = \frac{a t^2 + 2 \gammai \ui \, t}{\gamma(t) + \gammai}.
\end{aligned}
}
\label{eq:gamma_u_x_of_t}
\end{equation}
$$

Note that $$\gamma(t = 0) = \gammai$$. Also, the formula for $$x(t)$$ reduces to
$$x(t) = \ui t$$ when $$a = 0$$ and to $$x(t) = a t^2 /2 + \ui t$$ when $$\gamma(t) \approx 1$$.

# Proper time parametrization

If we call $$\tau(t)$$ the proper time, we have:

$$
\deriv{\tau}{t} = \frac{1}{\gamma} = \frac{1}{\sqrt{1 + (T + \Ti)^2}},
$$

which can be integrated as follows:

$$
\tau = \int_0^{t} \frac{\mathrm{d}t}{\sqrt{1 + (T + \Ti)^2}} =
\frac{c}{a} \, \int_{\Ti}^{T + \Ti} \frac{\mathrm{d}W}{\sqrt{1 + W^2}},
$$

We now change variable of integration to $$W = \sinh \phi$$:

$$
\frac{a \tau}{c} =
\int_{\asinh \Ti}^{\asinh (T + \Ti)} \mathrm{d} w =
\asinh (T + \Ti) - \asinh \Ti,
$$

Which gives:

$$
T + \Ti = \sinh \left( \frac{a \tau}{c} + \asinh \Ti \right).
$$

We now introduce the quantity $$w$$ defined as:

$$
w = \frac{a \tau}{c} + \asinh \Ti =
\frac{a \tau}{c} + \atanh \frac{\ui}{c},
$$

where we have used the identity
$$\asinh \frac{\gammai \ui}{c} = \atanh \frac{\ui}{c}$$.
We have $$T + \Ti = \sinh w$$ and $$\sqrt{1 + (T + \Ti)^2} = \cosh w$$.
We can thus write:

$$
\begin{equation}
\bbox[lightyellow, 10px, border: 2px solid orange]{
\begin{aligned}
w(\tau) & = \frac{a \tau}{c} + \atanh \frac{\ui}{c}, \\
\gamma(\tau) & = \cosh w(\tau), \\
\frac{u(\tau)}{c} & = \tanh w(\tau) \\
x(\tau) & = \frac{c^2}{a} \left[ \cosh w(\tau) - \gammai \right], \\
t(\tau) & = \frac{1}{a} \left[c \, \sinh w(\tau) - \gammai \ui\right].
\end{aligned}
}
\label{eq:gamma_u_x_of_tau}
\end{equation}
$$

The formulas for $$x(t)$$ and $$u(t)$$ have a removable singularity
at $$a = 0$$.
I doubt this singularity can be removed as easily as done in the previous section.
Take the case $$\ui = 0$$, for example.
We get $$t(\tau) = c \, \sinh (a \tau / c) / a$$. This can be rewritten as:
$$t(\tau) = \tau \, \sinhc (a \tau/c)$$,
where $$\sinhc$$ is the
[hyperbolic sinc function](https://mathworld.wolfram.com/SinhcFunction.html).
The problem of removing the singularity from $$t(\tau)$$ is thus transformed to the problem
of removing the singularity from $$\sinhc$$.

We thus have to be a bit careful when numerically computing $$x(\tau)$$ and $$t(\tau)$$.
For example, we could use a Taylor expansion in the vicinity of $$a = 0$$.

# Final velocity as a boundary condition

So far, we have written down the equations for hyperbolic motion assuming the position, velocity,
and acceleration are known at an initial time $$t = 0$$ (or $$\tau = 0$$.)
In certain cases, it is desirable to use a different set of boundary conditions.

In this section we rewrite the formulas for hyperbolic motion in terms of a desired final velocity.
In other words, we assume we are given the position and velocity at time $$t = 0$$ and
the velocity at a later time $$t = T$$.

We start from the velocity as in Eqs. \eqref{eq:gamma_u_x_of_t} and rewrite it as follows:

$$
\gamma(t) u(t) = \gammai \ui + at.
$$

This equation shows very clearly that the spatial component of the four-velocity, $$\gamma u$$,
increases linearly with time. This allows to express the acceleration, $$a$$, in terms
of the initial and final velocities:

$$
a = \frac{\gammaf \uf - \gammai \ui}{T}.
$$

In some cases, it may be a good idea to go a step further and introduce a new variable as follows:

$$
\omega(t) = \frac{\gamma(t) u(t)}{c}.
$$

The formulas for hyperbolic motion can now be reparametrised on $$\omega$$:

$$
\begin{equation*}
\begin{aligned}
\gamma(\omega) & = \sqrt{1 + \omega^2}, \\
u(\omega) & = \frac{c\omega}{\gamma(\omega)}, \\
x(\omega) & = cT \, \frac{\gamma(\omega) - \gammai}{\omegaf - \omegai}.
\end{aligned}
\end{equation*}
$$

This parametrisation can be useful to join two pieces of hyperbolic trajectory, for example.
