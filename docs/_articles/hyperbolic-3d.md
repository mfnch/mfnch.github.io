---
layout: post
title:  "Derivation of hyperbolic motion in three spatial dimensions"
categories: SR
date: 2023-02-13 10:40:00
usemathjax: true
---

$$
\DeclareMathOperator{\acosh}{acosh}
\DeclareMathOperator{\asinh}{asinh}
\DeclareMathOperator{\atanh}{atanh}
\newcommand{\insR}{\mathbb{R}}
\newcommand{\vvn}{\mathbf{n}}
\newcommand{\vvr}{\mathbf{r}}
\newcommand{\vvx}{\mathbf{x}}
\newcommand{\vvv}{\mathbf{v}}
\newcommand{\vvu}{\mathbf{u}}
\newcommand{\vvU}{\mathbf{U}}
\newcommand{\vva}{\mathbf{a}}
\newcommand{\vvA}{\mathbf{A}}
\newcommand{\vvq}{\mathbf{q}}
\newcommand{\vvc}{\mathbf{c}}
\newcommand{\vvalpha}{\boldsymbol{\alpha}}
\newcommand{\vvbeta}{\boldsymbol{\beta}}
\newcommand{\uua}{\hat{\mathbf{a}}}
\newcommand{\betaa}{\beta_{\mathrm{a}}}
\newcommand{\gammaa}{\gamma_{\mathrm{a}}}
\newcommand{\deriv} [2]{\frac{\mathrm{d} #1}{\mathrm{d} #2}}
\newcommand{\gammai}{\gamma_{\mathrm{i}}}
\newcommand{\vvX}{\mathbf{X}}
\newcommand{\vvXi}{\mathbf{X}_{\mathrm{i}}}
\newcommand{\vvUi}{\mathbf{U}_{\mathrm{i}}}
\newcommand{\vvui}{\mathbf{u}_{\mathrm{i}}}
\newcommand{\ui}{u_{\mathrm{i}}}
\newcommand{\vvAi}{\mathbf{A}_{\mathrm{i}}}
\newcommand{\vvai}{\mathbf{a}_{\mathrm{i}}}
\newcommand{\aiz}{a_{\mathrm{i0}}}
$$

# Introduction

In a [previous post](hyperbolic-1d) we derived the equations for hyperbolic
motion in one spatial dimension. This could seem a rather special case.
In fact, the one dimensional case is enough to characterize hyperbolic motion
in the most general case.
Indeed, for any point of an hyperbolic motion we can choose an inertial
frame which is tangent to the trajectory in that point.
We can also choose this frame such that the acceleration in the point
of tangency lies along the $$x$$ axis of the frame.
In that frame, the hyperbolic motion will take clearly the one dimensional
form which we derived and studied earlier.
This reasoning also lies down the path to obtain more generic
expressions of hyperbolic motion.

# Proper-time parametrization

So let us assume we are given the initial four-velocity,
$$\vvUi = \gammai\,(\vvui,\,c)$$, and four-acceleration,
$$\vvAi = (\vvai,\,\aiz)$$, of the particle at time $$t = 0$$
with respect to an original reference frame, $$\mathcal{R}$$.
Let us take the inertial frame, $$\mathcal{R}'$$, which sees the particle
at rest at $$t' = 0$$. We can now write down the transformation which
maps quantities from $$\mathcal{R}$$ to $$\mathcal{R}'$$, following
[this post](boosts-3d):

$$
\begin{equation}
\left\{
  \begin{array}{rcl}
    \vvv' & = & \vvv +
      (\vvv \cdot \vvui)\,\frac{\gammai - 1}{\ui^2}\,\vvui -
      v_0\,\gammai\,\frac{\vvui}{c}\\
    v_0' & = & \gammai \left(v_0 - \vvv \cdot \frac{\vvui}{c} \right)\\
  \end{array}
\right.
\label{eq:boost_to_zerov}
\end{equation}
$$

We can verify this is the correct transformation by applying it to
$$\vvUi$$. This corresponds to $$\vvv = \gammai \vvui$$,
$$v_0 = \gammai c$$:

$$
\left\{
  \begin{array}{rcl}
    \vvv' & = & \gammai \vvui +
      (\vvui \cdot \vvui) \, \frac{\gammai - 1}{\ui^2}\gammai \,\vvui -
      \gammai^2 \, \vvui\\
    v_0' & = & c \, \gammai^2 \left(1 - \vvui \cdot \frac{\vvui}{c^2} \right)\\
  \end{array}
\right.
$$

which becomes:

$$
\left\{
  \begin{array}{rcl}
    \vvv' & = & \gammai \vvui + (\gammai^2 - \gammai) \,\vvui - \gammai^2 \vvui
    = 0\\
    v_0' & = & c \, \gammai^2 \left(1 - \frac{\ui^2}{c^2} \right) = c\\
  \end{array}
\right.
$$

On the other hand, the acceleration $$\vvAi$$ transforms to the proper
acceleration $$\vvAi' = (\vvai', 0)$$, as follows:

$$
\left\{
  \begin{array}{rcl}
    \vvai' & = & \vvai +
      \frac{\gammai - 1}{\ui^2}(\vvai \cdot \vvui)\,\vvui -
      \gammai \aiz\,\frac{\vvui}{c}\\
    0 & = & \gammai \left(\aiz - \vvai \cdot \frac{\vvui}{c} \right)\\
  \end{array}
\right.
$$

The second equation gives $$c \aiz = \vvai \cdot \vvui$$, which can
be substituted into the first equation:

$$
\vvai' = \vvai +
      (\vvai \cdot \vvui)\,\vvui \, \left[
      \frac{\gammai - 1}{\ui^2} - \frac{\gammai}{c^2} \right]
$$

which gives:

\begin{equation}
\vvai' = \vvai +
  \frac{1 - \gammai}{\ui^2 \gammai} \,
  \left(\vvai \cdot \vvui\right) \, \vvui.
\label{eq:a}
\end{equation}

In the reference frame $$\mathcal{R}'$$ we are now able to write down
the equations of motion for hyperbolic motion. Indeed, the initial
velocity is zero in this frame. This causes the motion to happen
entirely in the direction $$\vvai'$$. In particular,

$$
\begin{equation}
\left\{
  \begin{array}{rcl}
    \vvr' & = & \uua_0'\,\frac{c^2}{a}\left(\cosh \frac{a\tau}{c} - 1 \right) \\
    \frac{\vvu'}{c} & = & \uua_0'\,\tanh \frac{a\tau}{c}\\
    t' & = & \frac{c}{a} \sinh \frac{a\tau}{c}
  \end{array}
\right.
\label{eq:start_frame}
\end{equation}
$$

The acceleration $$a$$ is the norm of the proper acceleration:
$$a = \|\vvai'\| = \sqrt{\vvAi^2} = \sqrt{\vvai^2 - \aiz^2}$$.
Note that $$\uua_0' = \vvai' / a$$.

To obtain the expression of hyperbolic motion in the original frame
we just have to apply the inverse of Eq. \eqref{eq:boost_to_zerov}
to the equations above. The former can be obtained by changing
$$\vvui \rightarrow -\vvui$$:

$$
\begin{equation}
\left\{
  \begin{array}{rcl}
    \vvv & = & \vvv' +
      (\vvv' \cdot \vvui) \, \frac{\gammai - 1}{\ui^2}\,\vvui +
      v_0'\,\gammai \frac{\vvui}{c}\\
    v_0 & = & \gammai \left(v_0' + \vvv' \cdot \frac{\vvui}{c} \right)\\
  \end{array}
\right.
\label{eq:boost_to_zerov_inv}
\end{equation}
$$

Substituting $$\vvr'$$ and $$t'$$ of Eq. \eqref{eq:start_frame} into
Eq. \eqref{eq:boost_to_zerov_inv} we get:

$$
\begin{equation}
\left\{
  \begin{array}{rcl}
    \vvr  & = & \frac{c^2}{a} \left[ \vvq \, (\cosh \frac{a\tau}{c} - 1) +
      \frac{\vvui}{c} \, \gammai \sinh w \right]\\
    t & = & \frac{c}{a} \left[
      \gammai \, \sinh \frac{a\tau}{c} +
      \betaa \gammai \, \cosh \frac{a\tau}{c} - \betaa \gammai\right]\\
    \vvq & = &
      \uua_0'\,  + \frac{\gammai - 1}{\beta^2} \betaa\,\frac{\vvui}{c} \\
  \end{array}
\right.
\label{eq:preliminary_3d_hypmot}
\end{equation}
$$

where we have introduced $$\betaa = \uua_0' \cdot \frac{\vvui}{c}$$
and the constant vector $$\vvq$$.

Let us now try to simplify Eq. \eqref{eq:preliminary_3d_hypmot}.
We first multiply Eq. \eqref{eq:a} by $$\vvui$$:

$$
\vvui \cdot \vvai' = \vvai \cdot \vvui +
  \frac{1 - \gammai}{\gammai} \, \vvai \cdot \vvui
  = \frac{1}{\gammai} \, \vvai \cdot \vvui.
$$

We now remember that $$\betaa = \uua_0' \cdot \vvui / c$$, where
$$\uua_0' = \vvai' / \|\vvai'\| = \vvai' / a$$. We therefore
conclude:

\begin{equation}
\betaa = \frac{1}{c \gammai a} \, \vvai \cdot \vvui = \frac{\aiz}{\gammai a}.
\label{eq:betaa}
\end{equation}

We now rewrite $$\vvq$$ by substituting Eq. \eqref{eq:a} into
the expression for $$\vvq$$ in Eq. \eqref{eq:preliminary_3d_hypmot}:

$$
\vvq = \frac{\vvai}{a} +
  \frac{1 - \gammai}{\gammai \ui^2 a} \,
  \left(\vvai \cdot \vvui\right) \, \vvui +
  \frac{\gammai - 1}{\ui^2} c\betaa\,\vvui \\
$$

Substituting Eq. \eqref{eq:betaa} in the expression above, we
simply get $$\vvq = \vvai/a$$.
We can thus rewrite Eq. \eqref{eq:preliminary_3d_hypmot} as:

$$
\begin{equation}
\bbox[lightyellow, 10px, border: 2px solid orange]{
\begin{aligned}
    \vvr(\tau) & =
    \frac{c^2}{a} \left[
      \frac{\vvai}{a} \, \left(\cosh \frac{a\tau}{c} - 1\right) +
      \frac{\gammai \vvui}{c} \, \sinh \frac{a\tau}{c}
    \right]\\
    t(\tau) & = \frac{c}{a} \left[
      \betaa \gammai \, \left(  \cosh \frac{a\tau}{c} - 1\right) +
      \gammai \, \sinh \frac{a\tau}{c}
    \right]
\end{aligned}
\label{eq:second_preliminary_3d_hypmot}
}
\end{equation}
$$

The velocity can be obtained by deriving $$\vvr$$ with respect to $$t$$:

$$
\vvu \equiv \deriv{\vvr}{t} =
    c \left[
      \frac{\vvai}{a} \, \sinh \frac{a\tau}{c} +
      \frac{\gammai \vvui}{c} \, \cosh \frac{a\tau}{c}
    \right] \deriv{\tau}{t}.
$$

$$\deriv{\tau}{t}$$ is simply $$\gamma^{-1}$$, therefore we can rewrite
this equation as:

$$
\gamma \vvu =
  \gammai \vvui \, \cosh \frac{a\tau}{c} +
    \vvai \, \frac{c}{a} \, \sinh \frac{a\tau}{c}.
$$

This, toghether with the identity $$\gamma^2 = 1 + (\gamma \vvu)^2 / c^2$$,
allows to find $$\gamma$$:

$$
\gamma^2 =
  1 +
  \gammai^2 \frac{\ui^2}{c^2} \, \cosh^2 \frac{a\tau}{c} +
  \vvai^2 \, \frac{1}{a^2} \, \sinh^2 \frac{a\tau}{c} +
  2 \gammai \vvui \cdot \vvai \, \frac{1}{ca} \, \cosh \frac{a\tau}{c} \, \sinh \frac{a\tau}{c}.
$$

This can be simplified to:

$$
\gamma^2 =
  \gammai^2 \left[
    \cosh^2 \frac{a\tau}{c} +
    \betaa^2  \sinh^2 \frac{a\tau}{c} +
    2 \cosh \frac{a\tau}{c} \, \betaa \sinh \frac{a\tau}{c}
  \right]
$$

Finally,

$$
\begin{equation}
\bbox[lightyellow, 10px, border: 2px solid orange]{
\begin{aligned}
\frac{\vvu(\tau)}{c} & =
  \frac{\frac{\gammai \vvui}{c} \, \cosh \frac{a\tau}{c} +
        \frac{\vvai}{a} \, \sinh \frac{a\tau}{c}}{\gamma(\tau)}\\
\gamma(\tau) & =
  \gammai \cosh \frac{a\tau}{c} + \gammai \betaa \sinh \frac{a\tau}{c}
\end{aligned}
}
\label{eq:u_and_gamma_of_tau}
\end{equation}
$$

We can also easily obtain the spatial part of the four-acceleration, by deriving
$$\gamma \vvu$$ by the proper time $$\tau$$:

$$
\begin{equation*}
\bbox[lightyellow, 10px, border: 2px solid orange]{
\begin{aligned}
\vva(\tau) & =
  \vvai \, \cosh \frac{a\tau}{c} + \frac{a \gammai \vvui}{c} \, \sinh \frac{a\tau}{c}\\
a_0(\tau) & =
  a \gammai \betaa \, \cosh \frac{a\tau}{c} +
  a \gammai \, \sinh \frac{a\tau}{c}
\end{aligned}
}
\end{equation*}
$$

# Four-vectors equations

In this section we are going to rewrite the formulas derived in the previous
sections in terms of the four-vectors $$\vvX = (\vvr,\,ct)$$,
$$\vvU = (\gamma \vvu,\,\gamma c)$$, $$\vvA = (\vva,\,a_0)$$:

$$
\begin{equation}
\bbox[lightyellow, 10px, border: 2px solid orange]{
\begin{aligned}
\vvX(\tau) & =
  \vvXi +
  \frac{c^2 \vvAi}{a^2} \, \left(\cosh \frac{a\tau}{c} - 1\right) +
  \frac{c\vvUi}{a} \, \sinh \frac{a\tau}{c},\\
\vvU(\tau) & = \vvUi \cosh \frac{a\tau}{c} + \frac{c\vvAi}{a} \sinh \frac{a\tau}{c},\\
\vvA(\tau) & = \vvAi \, \cosh \frac{a\tau}{c} + \frac{a \vvUi}{c} \, \sinh \frac{a\tau}{c},\\
\end{aligned}
}
\end{equation}
$$

where $$a = \sqrt{\vvAi^2} = \sqrt{\vvai^2 - \aiz^2}$$.

The formulas above are more elegant and compact than the ones we derived earlier.
Also, they express all quantities in terms of two vectors that are Minkowsky-orthogonal
between each other: the initial four-velocity, $$\vvUi$$, and initial four-acceleration,
$$\vvAi$$. This is very useful to further manipulate these expressions, as we are going
to see in the next sections.

# Proper-time from coordinate-time

In the previous section we have derived a number of formulas expressing
various quantities, such as position and velocity, as functions
of the proper-time, $$\tau$$. The objective of this section and the next one
is to express the same quantities as functions of the coordinate-time, instead.

One way of achieving this objective, is to express the proper-time as a function
of the coordinate-time, $$t$$. We can then plug this expression in the
equations we derived earlier to replace the dependency on $$\tau$$
with a dependency on $$t$$.

Our start point is the equation for $$t(\tau)$$ in \eqref{eq:preliminary_3d_hypmot}:

$$
t(\tau) = \frac{c \gammai}{a} \left(\sinh w + \betaa \, \cosh w - \betaa \right),
$$

where we introduced the shorthand $$w \equiv a\tau/c$$.

We need to invert this equation and write $$\tau$$ as a function of $$t$$.
We note that, if we manage to rewrite the equation above as:

$$
t = \frac{c \gammai}{a} \, \left[
  Q \left( \cosh w_0 \, \sinh w + \sinh w_0 \, \cosh w \right) - \betaa
  \right],
$$

for some suitable choice of $$w_0$$ and $$Q$$, then we can further simplify this to:

$$
t = \frac{c \gammai}{a} \, \left[ Q \sinh (w + w_0) - \betaa \right],
$$

and from this we can easily proceed with the inversion.
We therefore need to find $$Q$$ and $$w_0$$ such that:

$$
\begin{equation}
\left\{
\begin{aligned}
  1 & = Q\,\cosh w_0 \\
  \betaa & = Q\,\sinh w_0 \\
\end{aligned}
\right.
\label{eq:w0_and_Q}
\end{equation}
$$

which gives $$\tanh w_0 = \betaa$$ and $$Q^2 = 1 -  \betaa^2$$.
We can write:

\begin{equation}
t = \frac{c \gammai}{a} \, \left[ \frac{1}{\gammaa} \, \sinh (w + w_0) - \betaa \right],
\label{eq:t_from_tau}
\end{equation}

where we introduced, $$\gammaa = 1/Q = 1/\sqrt{1 - \betaa^2}$$.

We can finally express $$\tau$$ as a function of $$t$$:

\begin{equation}
\bbox[lightyellow, 10px, border: 2px solid orange]{
\tau(t) = \frac{c}{a} \left[
\asinh \left(\betaa \gammaa + \frac{\gammaa at}{\gamma c} \right) - \atanh \betaa
\right]
\label{eq:tau_from_t}
}
\end{equation}

Note that $$\sinh w_0 = \betaa / Q = \betaa \gammaa$$ and
$$\cosh w_0 = 1/Q = \gammaa$$, therefore we can express $$w_0$$ in multiple ways:
$$w_0 = \atanh \betaa = \asinh \betaa \gammaa = \acosh \gammaa$$.

These expressions help to verify that $$\tau(t=0)$$ is zero,
as also implied by Eq. \eqref{eq:preliminary_3d_hypmot}.

We conclude this section by rewriting Eq. \eqref{eq:t_from_tau} in a way that
is convenient for what we are going to do in the next section:

\begin{equation}
\sinh (w + w_0) = \frac{\gammaa}{\gammai} \frac{at}{c} + \betaa \gammaa.
\label{eq:sinhwp}
\end{equation}

From the identity $$\cosh^2 x - \sinh^2 x = 1$$, we obtain:

\begin{equation}
\cosh (w + w_0) = \sqrt{1 +
  \left(\frac{\gammaa}{\gammai} \frac{at}{c} + \betaa \gammaa\right)^2}.
\label{eq:coshwp}
\end{equation}

# Coordinate-time parametrization

The next easiest quantity to express in terms of $$t$$, after $$\tau(t)$$,
is $$\gamma$$.

We start from Eq. \eqref{eq:u_and_gamma_of_tau} and recall the definition of
$$w_0$$ from Eqs. \eqref{eq:w0_and_Q}:

$$
\begin{eqnarray}
\gamma(\tau) & = & \gammai Q \left( \cosh w_0 \cosh w + \sinh w_0 \sinh w \right)\nonumber\\
 & = & \frac{\gammai}{\gammaa} \cosh (w + w_0).
\label{eq:gamma_of_tau}
\end{eqnarray}
$$

Using Eq. \eqref{eq:coshwp}:

$$
\begin{equation}
\gamma(\tau) =
  \sqrt{\left(\frac{\gammai}{\gammaa}\right)^2 +
        \left(\frac{at}{c} + \betaa \gammai\right)^2}.
\nonumber
\end{equation}
$$
