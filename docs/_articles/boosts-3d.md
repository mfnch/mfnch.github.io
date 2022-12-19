---
layout: post
title:  "Lorentz boost in three dimensions"
categories: SR
usemathjax: true
---

$$
\newcommand{\vini}[1]{\mathbf{#1}_{\mathrm{I}}}
\newcommand{\vmid}[1]{\mathbf{#1}_{\mathrm{M}}}
\newcommand{\vfin}[1]{\mathbf{#1}_{\mathrm{F}}}
\newcommand{\ini}[1]{#1_{\mathrm{I}}}
\newcommand{\fin}[1]{#1_{\mathrm{F}}}
\newcommand{\vvr}{\mathbf{r}}
\newcommand{\vvv}{\mathbf{v}}
\newcommand{\vva}{\mathbf{a}}
\newcommand{\vvu}{\mathbf{u}}
\newcommand{\vvw}{\mathbf{w}}
$$

In this short post I am going to derive the relativistic formulas to transform between two
intertial refererence frames, $$\mathcal{R}$$ and $$\mathcal{R}'$$, translating with constant
velocity with respect to each other. In this scenario, the axes of one reference frame remain
parallel to the corresponding axes of the other reference frame, while the origin of the two
reference frames move with constant velocity, $$\vvv$$, with respect to each other.

We are going to derive the 3D formulas from the 1D ones:

$$
\begin{eqnarray}
x' = \gamma (x - \beta ct),\nonumber\\
ct' = \gamma (ct - \beta x),\nonumber
\end{eqnarray}
$$

where, as usual, $$c$$ is the speed of light, $$\beta = v/c$$ and
$$\gamma = (1 - \beta^2)^{-1/2}$$.

The idea behind this simple derivation is to look at what happens in the direction parallel to
the velocity $$\vvv$$ and the directions orthogonal to it. A Lorentz boost along $$\vvv$$ is going
to only affect the "parallel direction", as described by the one-dimensional formulas above.

Let's then start by introducing two projection functions, $$P_\perp$$ and $$P_\parallel$$.
Given an arbitrary vector $$\vvw$$, $$P_\perp \vvw$$ is the component of the vector orthogonal to
$$\vvv$$, while $$P_\parallel \vvw$$ is the component parallel to it. We thus have
$$\vvv \cdot P_\perp \vvw = 0$$ and $$\vvw = P_\perp \vvw + P_\parallel \vvw$$.
We can easily write down $$P_\perp$$ and $$P_\parallel$$ as follows:

$$
\begin{equation}
\begin{aligned}
P_\parallel & =  \frac{\vvw \cdot \vvv}{v^2}\,\vvv, \\
P_\perp & = \vvw  - P_\parallel \vvw.
\end{aligned}
\label{eq:proj}
\end{equation}
$$

A Lorentz Boost along $$\vvv$$ can then be expressed along these directions as follows:

$$
\begin{eqnarray*}
P_\perp \vvw' & = & P_\perp \vvw, \\
P_\parallel \vvw' & = & \gamma \left(P_\parallel \vvw - \frac{\vvv}{c} \, w_0\right), \\
w_0' & = & \gamma \left(w_0 - \frac{\vvv}{c} \cdot P_\parallel \vvw\right).
\end{eqnarray*}
$$

Where the boost is applied to the four-vector $$(\vvw,\,w_0)$$.
Summing $$P_\perp \vvw'$$ and $$P_\parallel \vvw'$$ we get $$\vvw'$$:

$$
\begin{equation*}
\vvw' = P_\perp \vvw + \gamma P_\parallel \vvw - \gamma \frac{\vvv}{c} \, w_0.
\end{equation*}
$$

We can finally use Eq. $$\eqref{eq:proj}$$ to write:

$$
\bbox[lightyellow, 10px, border: 2px solid orange]{
\begin{eqnarray*}
\vvw' & = & \vvw
  + \vvv \, \frac{\gamma - 1}{c^2\beta^2} \left(\vvv \cdot \vvw\right)
  - \gamma \frac{\vvv}{c} \, w_0, \\
w_0' & = & \gamma \left(w_0 - \frac{\vvv}{c} \cdot \vvw \right).
\end{eqnarray*}
}
$$

The formulas above apply a Lorentz boost to the four-vector $$(\vvw,\,w_0)$$, transforming it to
$$(\vvw',\,w_0')$$, the four-vector "seen" by a reference frame moving with velocity $$\vvv$$.

It can be easily seen that choosing $$\vvw = 0$$, $$w_0 = c$$ leads to
$$\vvw' = \gamma \vvv$$ and $$w_0' = \gamma c$$, as expected.
Also, choosing $$\vvw = \gamma \vvv$$, $$w_0 = \gamma c$$, gives $$\vvw' = 0$$ and $$w_0' = c$$.

Note also that the inverse Boost can be obtained simply by substituting $$\vvv \rightarrow -\vvv$$.