---
layout: post
title:  "Derivation of hyperbolic motion in one spatial dimension"
categories: SR
date: 2023-01-03 10:40:00
usemathjax: true
---

$$
\DeclareMathOperator{\asinh}{asinh}
\DeclareMathOperator{\atanh}{atanh}
\DeclareMathOperator{\sinhc}{sinhc}
\newcommand{\insR}{\mathbb{R}}
\newcommand{\deriv} [2]{\frac{\mathrm{d} #1}{\mathrm{d} #2}}
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
frame tangent to $$\mathrm{Q}\in\insR^4$$ we expect to always get the
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
\int_{\theta_0}^{\theta}
  \frac{\mathrm{d}\Theta}{\cos^2 \Theta} =
\tan \theta - \tan \theta_0 = T.
$$

Substituting $$\sin \theta = u/c$$, we have:

$$
\begin{equation}
\sin \theta = \frac{u}{c} = \frac{T + T_0}{\sqrt{1 + (T + T_0)^2}},
\label{eq:sin_theta}
\end{equation}
$$

where $$T_0 = \tan \theta_0$$ and hence:

$$
\frac{u_0}{c} = \frac{T_0}{\sqrt{1 + T_0^2}}
\Rightarrow
T_0 = \frac{\gamma_0 u_0}{c}.
$$

From \eqref{eq:sin_theta} we can compute $$\gamma = (1 - (u_0/c)^2)^{-1/2}$$:

$$
\gamma = \left[1 - \frac{(T + T_0)^2}{1 + (T + T_0)^2} \right]^{-1/2}
= \sqrt{1 + (T + T_0)^2}
$$

We can integrate the velocity formula \eqref{eq:sin_theta} to obtain the position:

$$
x = \int_0^{t_0} u \, \mathrm{d}t =
\frac{c^2}{a} \int_0^{T_0} \frac{u}{c} \, \mathrm{d}T
$$

Changing variable of integration to $$\Theta$$ as above:

$$
x =
\frac{c^2}{a} \int_{\theta_0}^{\theta}
  \frac{\sin \Theta}{\cos^2 \Theta} \, \mathrm{d}\Theta =
-\frac{c^2}{a} \int_{\cos \theta_0}^{\cos \theta}
  \frac{\mathrm{d}\cos \Theta}{\cos^2 \Theta}
$$

which gives:

$$
x =
\frac{c^2}{a} \left( \frac{1}{\cos \theta} - \frac{1}{\cos \theta_0} \right).
$$

From Eq. \eqref{eq:sin_theta} we deduce that
$$\cos^{-1} \theta = \sqrt{1 + (T + T_0)^2} = \gamma$$
and $$\cos^{-1} \theta_0 = \sqrt{1 + T_0^2} = \gamma_0$$. We thus have:

$$
\begin{equation*}
x = \frac{c^2}{a} \left( \gamma - \gamma_0 \right)
\end{equation*}
$$

and,

$$
\bbox[lightyellow, 10px, border: 2px solid orange]{
\begin{equation*}
x(t) = \frac{c^2}{a} \left(
  \sqrt{1 + \left(\frac{at}{c} + \frac{\gamma_0 u_0}{c}\right)^2} - \gamma_0 \right).
\end{equation*}
}
$$

This expression has a removable singularity in $$a = 0$$, which isn't well suited for numerical
computation. We can solve the issue by multiplying the right hand side by
$$(\gamma + \gamma_0)/(\gamma + \gamma_0)$$:

$$
\begin{eqnarray*}
x & = & \frac{c^2}{a} \frac{\gamma^2 - \gamma_0^2}{\gamma + \gamma_0} \\
& = & \frac{c^2}{a(\gamma + \gamma_0)}
  \left[1 + \left(\frac{at}{c} + \frac{\gamma_0 u_0}{c}\right)^2 - \gamma_0^2\right]\\
& = & \frac{a t^2 + 2 \gamma_0 u_0 \, t}{\gamma + \gamma_0}.
\end{eqnarray*}
$$

Above, we used the identity: $$1 + \frac{\gamma_0^2 u_0^2}{c^2} - \gamma_0^2 = 0$$.

In summary:

$$
\bbox[lightyellow, 10px, border: 2px solid orange]{
\begin{eqnarray*}
\gamma(t) & = & \sqrt{1 + \left( \frac{at}{c} + \frac{\gamma_0 u_0}{c} \right)^2}, \\
u(t) & = & \frac{at + \gamma_0 u_0}{\gamma(t)}, \\
x(t) & = & \frac{a t^2 + 2 \gamma_0 u_0 \, t}{\gamma(t) + \gamma_0}.
\end{eqnarray*}
}
$$

Note that $$\gamma(t = 0) = \gamma_0$$. Also, the formula for $$x(t)$$ reduces to
$$x(t) = u_0 t$$ when $$a = 0$$ and to $$x(t) = a t^2 /2 + u_0 t$$ when $$\gamma(t) \approx 1$$.

# Proper time parametrization

If we call $$\tau(t)$$ the proper time, we have:

$$
\deriv{\tau}{t} = \frac{1}{\gamma} = \frac{1}{\sqrt{1 + (T + T_0)^2}},
$$

which can be integrated as follows:

$$
\tau = \int_0^{t} \frac{\mathrm{d}t}{\sqrt{1 + (T + T_0)^2}} =
\frac{c}{a} \, \int_{T_0}^{T + T_0} \frac{\mathrm{d}W}{\sqrt{1 + W^2}},
$$

We now change variable of integration to $$W = \sinh \phi$$:

$$
\frac{a \tau}{c} =
\int_{\asinh T_0}^{\asinh (T + T_0)} \mathrm{d} w =
\asinh (T + T_0) - \asinh T_0,
$$

Which gives:

$$
T + T_0 = \sinh \left( \frac{a \tau}{c} + \asinh T_0 \right).
$$

We now introduce the quantity $$w$$ defined as:

$$
w = \frac{a \tau}{c} + \asinh T_0 =
\frac{a \tau}{c} + \atanh \frac{u_0}{c},
$$

where we have used the identity
$$\asinh \frac{\gamma_0 u_0}{c} = \atanh \frac{u_0}{c}$$.
We have $$T + T_0 = \sinh w$$ and $$\sqrt{1 + (T + T_0)^2} = \cosh w$$.
We can thus write:

$$
\bbox[lightyellow, 10px, border: 2px solid orange]{
\begin{eqnarray*}
w(\tau) & = & \frac{a \tau}{c} + \atanh \frac{u_0}{c}, \\
\gamma(\tau) & = & \cosh w(\tau), \\
\frac{u(\tau)}{c} & = & \tanh w(\tau) \\
x(\tau) & = & \frac{c^2}{a} \left[ \cosh w(\tau) - \gamma_0 \right], \\
t(\tau) & = & \frac{1}{a} \left[c \, \sinh w(\tau) - \gamma_0 u_0\right]. \\
\end{eqnarray*}
}
$$

The formulas for $$x(t)$$ and $$u(t)$$ have a removable singularity
at $$a = 0$$.
I doubt this singularity can be removed as easily as done in the previous section.
Take the case $$u_0 = 0$$, for example.
We get $$t(\tau) = c \, \sinh (a \tau / c) / a$$. This can be rewritten as:
$$t(\tau) = \tau \, \sinhc (a \tau/c)$$,
where $$\sinhc$$ is the
[hyperbolic sinc function](https://mathworld.wolfram.com/SinhcFunction.html).
The problem of removing the singularity from $$t(\tau)$$ is thus transformed to the problem
of removing the singularity from $$\sinhc$$.

We thus have to be a bit careful when numerically computing $$x(\tau)$$ and $$t(\tau)$$.
For example, we could use a Taylor expansion in the vicinity of $$a = 0$$.