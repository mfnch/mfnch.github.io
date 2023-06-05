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
\DeclareMathOperator{\sinhc}{sinhc}
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
\newcommand{\uuai}{\hat{\mathbf{a}}_{\mathrm{i}}}
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
\newcommand{\vvAf}{\mathbf{A}_{\mathrm{f}}}
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
    \vvr' & = & \uuai'\,\frac{c^2}{a}\left(\cosh \frac{a\tau}{c} - 1 \right) \\
    \frac{\vvu'}{c} & = & \uuai'\,\tanh \frac{a\tau}{c}\\
    t' & = & \frac{c}{a} \sinh \frac{a\tau}{c}
  \end{array}
\right.
\label{eq:start_frame}
\end{equation}
$$

The acceleration $$a$$ is the norm of the proper acceleration:
$$a = \|\vvai'\| = \sqrt{-\vvAi^2} = \sqrt{\vvai^2 - \aiz^2}$$.
Note that $$\uuai' = \vvai' / a$$.

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
      \uuai'\,  + \frac{\gammai - 1}{\beta^2} \betaa\,\frac{\vvui}{c} \\
  \end{array}
\right.
\label{eq:preliminary_3d_hypmot}
\end{equation}
$$

where we have introduced $$\betaa = \uuai' \cdot \frac{\vvui}{c}$$
and the constant vector $$\vvq$$.

Let us now try to simplify Eq. \eqref{eq:preliminary_3d_hypmot}.
We first multiply Eq. \eqref{eq:a} by $$\vvui$$:

$$
\vvui \cdot \vvai' = \vvai \cdot \vvui +
  \frac{1 - \gammai}{\gammai} \, \vvai \cdot \vvui
  = \frac{1}{\gammai} \, \vvai \cdot \vvui.
$$

We now remember that $$\betaa = \uuai' \cdot \vvui / c$$, where
$$\uuai' = \vvai' / \|\vvai'\| = \vvai' / a$$. We therefore
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
      \frac{\gammai \vvui}{c} \, \sinh \frac{a\tau}{c} +
      \frac{\vvai}{a} \, \left(\cosh \frac{a\tau}{c} - 1\right)
    \right]\\
    t(\tau) & = \frac{c}{a} \left[
      \gammai \, \sinh \frac{a\tau}{c} +
      \frac{\aiz}{a} \, \left(  \cosh \frac{a\tau}{c} - 1\right)
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
  \gammai^2 \cosh^2 \frac{a\tau}{c} +
  \frac{\aiz^2}{a^2} \sinh^2 \frac{a\tau}{c} +
  2 \frac{\gammai \aiz}{a} \, \cosh \frac{a\tau}{c} \sinh \frac{a\tau}{c}
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
  \gammai \cosh \frac{a\tau}{c} + \frac{\aiz}{a} \sinh \frac{a\tau}{c}
\end{aligned}
}
\label{eq:u_and_gamma_of_tau}
\end{equation}
$$

We can also easily obtain the spatial and temporal parts of the four-acceleration,
by deriving $$\gamma \vvu$$ and $$\gamma$$ by the proper time $$\tau$$:

$$
\begin{equation*}
\bbox[lightyellow, 10px, border: 2px solid orange]{
\begin{aligned}
\vva(\tau) & =
  \vvai \, \cosh \frac{a\tau}{c} + \frac{a \gammai \vvui}{c} \, \sinh \frac{a\tau}{c}\\
a_0(\tau) & = \aiz \, \cosh \frac{a\tau}{c} + a \gammai \, \sinh \frac{a\tau}{c}
\end{aligned}
}
\end{equation*}
$$

# Alternative velocity formula

Eqs. \eqref{eq:u_and_gamma_of_tau} can be reworked as follows:

$$
\begin{equation}
\vvu(\tau) =
  \vvui
+ \frac{c \vvai - \vvui \aiz}{a} \, \frac{\sinh \frac{a\tau}{c}}{\gamma(\tau)}.
\label{eq:u_of_tau_alt}
\end{equation}
$$

This equation shows that **the velocity changes within a straight line**.
This can be seen better by rewriting the equation above as follows:

$$
\vvu(\tau) = \vvui + \vvu_{\mathrm{if}} \, f(\tau),
$$

where $$\vvu_{\mathrm{if}} = (c \vvai - \vvui \aiz)/a$$ is a constant vector and
$$f(\tau) = (\sinh a\tau/c)/\gamma(\tau)$$ is a function with the property
$$f(0) = 0$$.

# Four-vector equations

In this section we are going to rewrite the formulas derived in the previous
sections in terms of the four-vectors $$\vvX = (\vvr,\,ct)$$,
$$\vvU = (\gamma \vvu,\,\gamma c)$$, $$\vvA = (\vva,\,a_0)$$:

$$
\begin{equation}
\bbox[lightyellow, 10px, border: 2px solid orange]{
\begin{aligned}
\vvX(\tau) & =
  \vvXi +
  \frac{c\vvUi}{a} \, \sinh \frac{a\tau}{c} +
  \frac{c^2 \vvAi}{a^2} \, \left(\cosh \frac{a\tau}{c} - 1\right),\\
\vvU(\tau) & = \vvUi \cosh \frac{a\tau}{c} + \frac{c\vvAi}{a} \sinh \frac{a\tau}{c},\\
\vvA(\tau) & = \vvAi \, \cosh \frac{a\tau}{c} + \frac{a \vvUi}{c} \, \sinh \frac{a\tau}{c},\\
\end{aligned}
}
\label{eq:hyperbolic_fvec}
\end{equation}
$$

where $$a = \sqrt{-\vvAi^2} = \sqrt{\vvai^2 - \aiz^2}$$.

The formulas above are more elegant and compact than the ones we derived earlier.
Also, they express all quantities in terms of two vectors that are Minkowski-orthogonal
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

Our start point is the equation for $$t(\tau)$$ in \eqref{eq:second_preliminary_3d_hypmot}:

$$
t(\tau) = \frac{c}{a^2} \left[ a \gammai \, \sinh w + \aiz \cosh w - \aiz \right]
$$

where we introduced the shorthand $$w \equiv a\tau/c$$.

We need to invert this equation and write $$\tau$$ as a function of $$t$$.
We note that, if we manage to rewrite the equation above as:

$$
t = \frac{c}{a^2} \, \left[
  Q \left( \cosh w_0 \, \sinh w + \sinh w_0 \, \cosh w \right) - \aiz
  \right],
$$

for some suitable choice of $$w_0$$ and $$Q$$, then we can further simplify this to:

$$
t = \frac{c}{a^2} \, \left[ Q \sinh (w + w_0) - \aiz \right],
$$

and from this we can easily proceed with the inversion.
We therefore need to find $$Q$$ and $$w_0$$ such that:

$$
\begin{equation}
\left\{
\begin{aligned}
  a \gammai & = Q\,\cosh w_0 \\
  \aiz & = Q\,\sinh w_0 \\
\end{aligned}
\right.
\label{eq:w0_and_Q}
\end{equation}
$$

which gives $$\tanh w_0 = \aiz/(a \gammai)$$ and $$Q^2 = a^2 \gammai^2 -  \aiz^2$$.
We can write:

\begin{equation}
t = \frac{c}{a^2} \, \left[ \sqrt{a^2 \gammai^2 - \aiz^2} \, \sinh (w + w_0) - \aiz \right],
\label{eq:t_from_tau}
\end{equation}

We can finally express $$\tau$$ as a function of $$t$$:


$$
\frac{1}{\sqrt{a^2 \gammai^2 - \aiz^2}} \left(\frac{a^2 t}{c} + \aiz \right) = \sinh (w + w_0),
$$

\begin{equation}
\bbox[lightyellow, 10px, border: 2px solid orange]{
\tau(t) = \frac{c}{a} \left[
\asinh \left(\betaa \gammaa + \frac{\gammaa at}{\gammai c} \right) - \asinh \betaa \gammaa
\right]
\label{eq:tau_from_t}
}
\end{equation}

Note that $$\sinh w_0 = \betaa / Q = \betaa \gammaa$$ and
$$\cosh w_0 = 1/Q = \gammaa$$, therefore we can express $$w_0$$ in multiple ways:
$$w_0 = \atanh \betaa = \asinh \betaa \gammaa = \acosh \gammaa$$.

Note also that Eq. \eqref{eq:tau_from_t} is already sufficient to calculate position, velocity
and acceleration as a function of $$t$$, but in the next section we will attempt to obtain
simpler expressions, not requiring the inverse hyperbolic functions.

# Coordinate-time parametrization

This section's first goal is to express $$\cosh w$$ and $$\sinh w$$ in terms of t.
We start again from the equation for $$t(\tau)$$ in \eqref{eq:preliminary_3d_hypmot}:

$$
\begin{equation}
\sinh w + \betaa \, \cosh w = \frac{a t}{c \gammai} + \betaa \equiv \frac{D}{\gammaa},
\label{eq:coshw_of_D}
\end{equation}
$$

where we defined the shorthand quantity $$D = \gammaa(a t/(c \gammai) + \betaa)$$.
Let's first solve for $$\cosh w$$. This can be done by isolating the term in $$\sinh w$$
on one side of the equation, squaring it side-by-side and replacing
$$\sinh^2 w = \cosh^2 w - 1$$:

$$
\cosh^2 w + 2 D \betaa \gammaa \, \cosh w - \gammaa^2 - D^2 = 0,
$$

We can now use the much loved [quadratic formula](https://en.wikipedia.org/wiki/Quadratic_formula)
to find $$\cosh w$$. Once this is known, we can go back Eq. \eqref{eq:coshw_of_D} to
also easily obtain $$\sinh w$$. The results are all collected below:

$$
\begin{equation}
\bbox[lightyellow, 10px, border: 2px solid orange]{
\begin{aligned}
D(t) & = \frac{\gammaa}{\gammai} \frac{a t}{c} + \gammaa \betaa,\\
\cosh \frac{a\tau}{c} & = \gammaa \left(\sqrt{1 + D^2} - D \betaa \right),\\
\sinh \frac{a\tau}{c} & = \gammaa \left(D - \betaa \sqrt{1 + D^2}\right).
\end{aligned}
}
\label{eq:coshw_and_sinhw_of_t}
\end{equation}
$$

Problem solved! We can now use these formulas with Eqs. \eqref{eq:hyperbolic_fvec}
to numerically compute four-position, four-velocity and four-acceleration given $$t$$,
without having to compute any hyperbolic function.

There are, however, a couple of observations worth making before jumping
straight into computing these formulas.

First, the four-position formula in Eqs. \eqref{eq:hyperbolic_fvec}
has a removable singularity in $$a = 0$$ coming from the term $$\sinh w / a$$
and the term $$(\cosh w - 1) / a^2$$.
The issue can be solved by expressing the four-position in terms of the $$\sinhc$$
function:

$$
\vvX(\tau) =
  \vvXi +
  \vvUi \, \tau \sinhc \frac{a\tau}{c} +
  \vvAi \, \tau^2 \frac{\sinhc^2 \frac{a\tau}{c}}{\cosh \frac{a\tau}{c} + 1}.
$$

$$\tau \, \sinhc w$$ can then be calculated as:

$$
\begin{equation*}
\tau \, \sinhc w =
\frac{c \sinh w}{a} = \frac{\gammaa}{c\gammai^2}
  \frac{a t^2 + 2\betaa \gammai ct}{D + \betaa \sqrt{1 + D^2}}.
\end{equation*}
$$

A second point to make is that $$\gamma(t)$$ can be calculated more easily by going back
to Eq. \eqref{eq:u_and_gamma_of_tau} and rewriting it using the definition of $$w_0$$
from Eqs. \eqref{eq:w0_and_Q}:

$$
\begin{equation}
\begin{aligned}
\gamma(\tau) & = \gammai Q \left( \cosh w_0 \cosh w + \sinh w_0 \sinh w \right)\nonumber\\
 & = \frac{\gammai}{\gammaa} \cosh (w + w_0).
\end{aligned}
\label{eq:gamma_of_tau}
\end{equation}
$$

$$\cosh (w + w_0)$$ can be expressed as a function of $$t$$.
First, we obtain $$\sinh (w + w_0)$$ from Eq. \eqref{eq:t_from_tau}
and then we use the identity $$\cosh^2 x - \sinh^2 x = 1$$:

$$
\begin{equation}
\begin{aligned}
\sinh (w + w_0) & = \frac{\gammaa}{\gammai} \frac{at}{c} + \betaa \gammaa,\\
\cosh (w + w_0) & = \sqrt{1 +
  \left(\frac{\gammaa}{\gammai} \frac{at}{c} + \betaa \gammaa\right)^2}.
\end{aligned}
\label{eq:sinh_cosh_wp}
\end{equation}
$$

Eq. \eqref{eq:gamma_of_tau} can then be written as a function of $$t$$:

$$
\begin{equation}
\gamma(t) =
  \sqrt{\left(\frac{\gammai}{\gammaa}\right)^2 +
        \left(\frac{at}{c} + \betaa \gammai\right)^2}.
\nonumber
\end{equation}
$$

$$
\newcommand{\tauf}{\mathbf{\tau}_{\mathrm{f}}}
\newcommand{\vvXf}{\mathbf{X}_{\mathrm{f}}}
\newcommand{\vvUf}{\mathbf{U}_{\mathrm{f}}}
\newcommand{\vvuf}{\mathbf{u}_{\mathrm{f}}}
\newcommand{\gammaf}{\gamma_{\mathrm{f}}}
\newcommand{\vvUo}{\mathbf{U}_{\perp}}
$$

# Final velocity as a boundary condition

Similarly to what done in the one-dimensional case, we can rewrite the equations
of hyperbolic motion in terms of a final velocity, rather than using the initial acceleration.
In this section, we thus introduce $$\vvUf$$, the four-velocity at a time $$\tauf$$.
We aim to replace $$\vvAi$$ with $$\vvUf$$ in Eqs. \eqref{eq:hyperbolic_fvec}.

We start by rewriting the velocity equation \eqref{eq:hyperbolic_fvec} at time $$\tauf$$:

$$
\begin{equation}
\vvUf = \vvUi \cosh \frac{a\tauf}{c} + \frac{c\vvAi}{a} \sinh \frac{a\tauf}{c}.
\label{eq:uf_from_ui_and_ai}
\end{equation}
$$

$$\vvUf$$ is the final velocity, which we assume is given as a boundary condition.
We can use this equation to express $$\vvAi$$ in terms of $$\vvUf$$ and $$\vvUi$$:

$$
\begin{equation}
\frac{c\vvAi}{a} = \frac{\vvUf - \vvUi \cosh \frac{a\tauf}{c}}{\sinh \frac{a\tauf}{c}}.
\label{eq:ai_from_uf}
\end{equation}
$$

We can now replace this expression into Eqs. \eqref{eq:hyperbolic_fvec}:

$$
\begin{equation}
\bbox[lightyellow, 10px, border: 2px solid orange]{
\begin{aligned}
\vvX(\tau) & = \vvXi
  + \frac{c}{a} \frac{\vvUf \left( \cosh \frac{a\tau}{c} - 1\right) +
                      \vvUi \left( \cosh \frac{a\tauf}{c} - \cosh \frac{a(\tau - \tauf)}{c}\right)}
                     {\sinh \frac{a\tauf}{c}},\\
\vvU(\tau) & =
  \frac{\vvUf \sinh \frac{a\tau}{c} - \vvUi \sinh \frac{a(\tau - \tauf)}{c}}
       {\sinh \frac{a\tauf}{c}},\\
\vvA(\tau) & = \frac{a}{c}
  \frac{\vvUf \cosh \frac{a\tau}{c} - \vvUi \cosh \frac{a(\tau - \tauf)}{c}}
       {\sinh \frac{a\tauf}{c}},
\end{aligned}
}
\label{hyp3dwithuf}
\end{equation}
$$

These equations, however, have still traces of the initial acceleration, as they contain
terms in $$a$$. We can tackle this issue multiplying \eqref{eq:uf_from_ui_and_ai}
side-by-side by $$\vvUi$$ and obtain:

$$
\begin{equation}
\bbox[lightyellow, 10px, border: 2px solid orange]{
\vvUi \cdot \vvUf = c^2 \, \cosh \frac{a\tauf}{c},
}
\label{eq:a_from_ui_and_uf}
\end{equation}
$$

where we used the orthogonality of velocity and acceleration, $$\vvUi \cdot \vvAi = 0$$.
This expression, allows us to obtain $$a$$ from $$\vvUi$$ and $$\vvUf$$. It also allows us
to express $$\vvAi$$ purely in terms of $$\vvUi$$ and $$\vvUf$$:

$$
\vvUo = \frac{c\vvAi}{a} = s(\tauf)\,
\frac{\vvUf - \frac{\vvUi}{c^2} \, \vvUi \cdot \vvUf}
     {\sqrt{1 - \left(\frac{\vvUi \cdot \vvUf}{c^2}\right)^2}},
$$

where $$s(\tauf)$$ is the sign of $$\tauf$$.

Note that $$\vvUo$$ is a velocity. It has norm $$c$$ and is orthogonal to $$\vvUi$$.
That's not too suprising: the acceleration $$\vvAi$$ must be orthogonal to $$\vvUi$$
and must also be a linear combination of $$\vvUi$$ and $$\vvUf$$, as hyperbolic motion
takes place in a plane.

Similarly, we can also rewrite Eq. \eqref{eq:u_of_tau_alt} in terms of
the final velocity, $$\vvuf$$.

$$
\vvu(\tau) = \vvui +
  \left(\vvuf - \vvui\right) \, \frac{\gammaf}{\gamma(\tau)} \,
  \frac{\sinh \frac{a \tau}{c}}{\sinh \frac{a \tauf}{c}}.
$$

We conclude the section by noting that the position and acceleration at time $$\tau=\tauf$$
can be calculated to be:

$$
\begin{equation}
\bbox[lightyellow, 10px, border: 2px solid orange]{
\begin{aligned}
\vvXf & = \vvXi +
  \frac{c}{a} \frac{\cosh \frac{a\tauf}{c} - 1}{\sinh \frac{a\tauf}{c}}
    \left(\vvUi + \vvUf\right),\\
\vvAf & = \frac{a}{c} \frac{\vvUf \cosh \frac{a\tauf}{c} - \vvUi}{\sinh \frac{a\tauf}{c}},
\end{aligned}
}
\end{equation}
$$

or, taking advantage of Eq. \eqref{eq:a_from_ui_and_uf}:

$$
\begin{equation}
\bbox[lightyellow, 10px, border: 2px solid orange]{
\begin{aligned}
\vvXf & = \vvXi +
  \frac{\tauf}{\acosh \frac{\vvUi \cdot \vvUf}{c^2}}
    \sqrt{\frac{\vvUi \cdot \vvUf - c^2}{\vvUi \cdot \vvUf + c^2}}
    \left(\vvUi + \vvUf\right),\\
\vvAf & = \frac{\acosh \frac{\vvUi \cdot \vvUf}{c^2}}{\tauf}
 \frac{\vvUf \, (\vvUi \cdot \vvUf) - c^2 \vvUi}{\sqrt{(\vvUi \cdot \vvUf)^2 - c^4}}.
\end{aligned}
}
\end{equation}
$$
