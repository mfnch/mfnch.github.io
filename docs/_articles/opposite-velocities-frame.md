---
layout: post
title:  "Frame where two velocities are the opposite of each other"
categories: SR
date: 2022-12-19 16:03:00
usemathjax: true
---

$$
\newcommand{\vini}[1]{\mathbf{#1}_{\mathrm{I}}}
\newcommand{\vmid}[1]{\mathbf{#1}_{\mathrm{M}}}
\newcommand{\vfin}[1]{\mathbf{#1}_{\mathrm{F}}}
\newcommand{\ini}[1]{#1_{\mathrm{I}}}
\newcommand{\fin}[1]{#1_{\mathrm{F}}}
\newcommand{\vvr}{\mathbf{r}}
\newcommand{\vvr}{\mathbf{r}}
\newcommand{\vvv}{\mathbf{v}}
\newcommand{\vva}{\mathbf{a}}
\newcommand{\vvu}{\mathbf{u}}
\newcommand{\vvw}{\mathbf{w}}
$$

# Introduction

Consider one point-like particle. The particle has position $$\vvr_1$$ and velocity $$\vvv_1$$ at
time $$t_1$$. It has position $$\vvr_2$$ and velocity $$\vvv_2$$ at time $$t_2$$. In classical
mechanics, it is possible to choose an intertial reference system so that $$\vvr_2' = -\vvr_1'$$
and $$\vvv_2' = -\vvv_1'$$. What about Special Relativity?

# Motivation

Even simple calculations get pretty messy in Special Relativity.
Being able to choose a reference frame where formulas are mathematically simpler can help a great
deal with the caculations. It also gives a big help to the poor human mind that is trying to
understand what is going on behind all the math.

This simplification helps solving the [analytical positioning problem](analytical-positioning).

# Classical case

Let's first take a look at the classical case. The following reference frame transformation:

$$
\begin{equation}
\mathbf{r}' =
  \mathbf{r}
  - \frac{\vvr_1 + \vvr_2}{2}
  - \frac{\vvv_1 + \vvv_2}{2} \,
    \left(t - \frac{t_1 + t_2}{2}\right),
\label{eq:classical}
\end{equation}
$$

brings us in the reference frame where the positions and the velocities of the particle at the two
instants $$t_1$$ and $$t_2$$ are the opposite of each other. In particular, applying this
transformation to $$\vvr_1$$, $$\vvv_1$$, $$\vvr_2$$, and $$\vvv_2$$, we get:

$$
\begin{eqnarray*}
\vvr_1' & = & \frac{\vvr_1 - \vvr_2}{2} - \frac{\vvv_1 + \vvv_2}{2} \,
  \frac{t_1 - t_2}{2}, \\
\vvr_2' & = & \frac{\vvr_2 - \vvr_1}{2} - \frac{\vvv_1 + \vvv_2}{2} \,
  \frac{t_2 - t_1}{2} = -\vvr_1', \\
\vvv_1' & = & \frac{\vvv_1 - \vvv_2}{2}, \\
\vvv_2' & = & \frac{\vvv_2 - \vvv_1}{2} = -\vvv_1'.
\end{eqnarray*}
$$

# Relativistic case

Let's now try to find a reference frame transformation analogous to Eq. \eqref{eq:classical}, but
within the framework of Special Relativity.

As derived in [this other post](boosts-3d), a four-vector $$(\vvw,\,w_0)$$ seen from a reference
frame that moves with speed $$\vvv$$ can be written as follows:

$$
\begin{equation}
\vvw' = P_\perp \vvw + \gamma P_\parallel \vvw - \gamma \frac{\vvv}{c} \, w_0.
\label{eq:boost}
\end{equation}
$$

Let's see whether we can find a velocity $$\vvv$$ which transforms $$\vvv_1$$ and $$\vvv_2$$ so
that $$\vvv_2' = -\vvv_1'$$.
We then use Eq. \eqref{eq:boost} with $$\vvw = \gamma_1 \vvv_1$$, $$w_0 = \gamma_1 c$$
and with $$\vvw = \gamma_2 \vvv_2$$, $$w_0 = \gamma_2 c$$:

$$
\begin{eqnarray*}
\gamma_1' \vvv_1' & = &
  P_\perp \gamma_1 \vvv_1 + \gamma P_\parallel \gamma_1 \vvv_1
- \frac{\vvv}{c} \, \gamma \gamma_1 c, \\
\gamma_2' \vvv_2' & = &
  P_\perp \gamma_2 \vvv_2 + \gamma P_\parallel \gamma_2 \vvv_2
- \frac{\vvv}{c} \, \gamma \gamma_2 c. \\
\end{eqnarray*}
$$

We, however, have $$\gamma_2' \vvv_2' = -\gamma_1' \vvv_1'$$, because $$\vvv_2' = -\vvv_1'$$ and
thus $$\gamma_1' = \gamma_2'$$. Therefore we can combine the two equations above, obtaining:

$$
\begin{equation}
P_\perp (\gamma_1 \vvv_1 + \gamma_2 \vvv_2)
  + \gamma P_\parallel (\gamma_1 \vvv_1 + \gamma_2 \vvv_2)
  - \vvv \, \gamma(\gamma_1 + \gamma_2) = 0. \\
\label{eq:projs}
\end{equation}
$$

This equation can be projected into the direction parallel to $$\vvv$$ (via $$P_\parallel$$) and
the orthogonal directions (via $$P_\perp$$), obtaining two independent equations.  In particular,
for the orthogonal directions we have $$P_\perp (\gamma_1 \vvv_1 + \gamma_2 \vvv_2) = 0$$, which
implies that $$\vvv$$ is parrallel to $$\gamma_1 \vvv_1 + \gamma_2 \vvv_2$$,
i.e. $$P_\parallel (\gamma_1 \vvv_1 + \gamma_2 \vvv_2) = \gamma_1 \vvv_1 + \gamma_2 \vvv_2$$.
Eq. \eqref{eq:projs} can thus be rewritten as:

$$
\gamma (\gamma_1 \vvv_1 + \gamma_2 \vvv_2) - \vvv \, \gamma (\gamma_1 + \gamma_2) = 0.
$$

Finally, we have:

$$
\bbox[lightyellow, 10px, border: 2px solid orange]{
\begin{equation*}
\vvv = \frac{\gamma_1 \vvv_1 + \gamma_2 \vvv_2}{\gamma_1 + \gamma_2}.
\end{equation*}
}
$$

A Lorentz boost with this velocity transforms the two velocities $$\vvv_1$$ and $$\vvv_2$$ so that
they are the opposite of each other, i.e. $$\vvv_2' = -\vvv_1'$$.

After the boost is applied, the reference frame can be translated by a four-vector
$$(\vvr_1 + \vvr_2, t_1 + t_2)/2$$ to ensure that $$\vvr_2' = -\vvr_1'$$ and $$t_2 = -t_1$$,
similarly to the classical case.
