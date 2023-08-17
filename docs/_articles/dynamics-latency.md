---
layout: post
title:  "Latency of relativistic dynamics"
categories: SR
date: 2023-08-16 10:00:00
usemathjax: true
---

# Introduction

Contrary to classical mechanics, Special Relativity is very much a theory of particles and fields
rather than a theory of rigid bodies. So why am I talking so much about rigid bodies on this site
and on my videos? Well, one reason is that I am making a game and I want characters in the game to
have spatial extension rather than being point-like particles moving in a field. But that's not the
only reason. I believe **rigidity is a key mental tool for Special Relativity**. Consider my
[video on the train in a tunnel paradox](https://youtu.be/vnWNKdY8JtQ), for example.
I find it incredibly helpful to know that the train is rigid and that passengers on the train don't
see any deformation. It allows us to know for certain that the contraction we see when the train
moves is due to space-time effects, e.g. Lorentz contraction, rather than to a confusing mixture of
different phenomena.

If rigidity is part of the deal, however, we have a bunch of other problems to solve.
How do rigid bodies interact with each other? How does the player of the game move them?

# The quirks of relativistic rigidity

In this section I will try to explain one of the main features of rigidity in Special Relativity.
**A moving Born-rigid body has some of its history already written in the future**.
Take the picture below:

![moving rigid square](/assets/dynamics-latency-1.svg)

It shows a [Born-rigid body](https://en.wikipedia.org/wiki/Born_rigidity) that so-far has been
moving with constant velocity to the right.
The body has the shape of a square, but we see it squashed because it is moving and is thus
affected by Lorentz contraction. We know, however, that an observer moving with the object would see
an uncontracted square. (Objects appear Lorentz-contracted only when they move.
Oh, and by "see" I really mean "measure".)

Now, say you want the body to stop while still maintaining its rigidity. How can this happen?
Well, stopping means that the body's velocity decreases and becomes zero, therefore the body must
de-contract back to a square.
If you think about it, there is only one way this can happen. The left part of the object must
slow down more than the right part. The left part should budge first!

I recommend trying to visualize the scene in your head.
If you suddenly accelerate the body to the left, the front of the body (its right part),
must initially continue to go to the right to allow the body to de-contract.
And this is indeed what the rigidity constraint imposes. If you assume the body is rigid,
then the front of the body has its immediate future trajectory pre-determined. There is nothing
you can do to change it. The future of the body's front is already written.
The faster the body goes and the longer this unchangeable destiny is.
The back of the body, on the other hand, immediately reacts to the attempt to slow down the body.
It is as if the back of the body is in your present, but the front lives in your future.

The practical consequence of these effects is that a Born-rigid body is more and more
**difficult to steer** as it goes closer and closer to the speed of light. It just wants to go
straight, no matter how much you accelerate it... well, if you could increase the acceleration
arbitrarily you would manage to steer it, but it turns out there is a maximum acceleration that the
body can withstand before the rigidity constraint is broken. This maximum acceleration is smaller
for wider bodies. So... yeah, Born-rigid bodies want to go straight when they move fast. This is a
problem my game needs to be aware of. I cannot allow the body to accelerate too much otherwise it
becomes very difficult to steer.

This is the very first point I wanted to make when talking about "relativistic dynamics latency".

# Plausible collision models

When talking about latency of relativistic dynamics there is another important aspect
to consider: how does a rigid body interact with its environment?

Take the picture below:

![relativistic body colliding](/assets/dynamics-latency-2.svg)

It shows a rigid-body that collides in a particular point of space-time, marked with a red cross.
Say the collision happens at a certain time $$t_0$$. Clearly at this instant in time the other parts
of the body are unaware that the collision took place: information takes time to propagate and
cannot travel faster than the speed of light!
However, the body is rigid and must react as a whole. Information about the collision
**must propagate to a part of the body before that part can respond to it in any way**. Why?
Well, if a part of the body reacted before light had time to propagate to it from the collision
point, then the two "events" would have a space-like separation, which means there would
be observers reporting that the reaction of the body occurred before the collision.
For my game, I am trying to avoid causality inconsistencies like these, if possible.

"What's the problem?" -- you may argue -- "the part that collides reacts first and the rest
of the body follows...". Well... no. Because of what we have found in the previous section,
not even the front of the body can react immediately to the collision. Remember, the trajectory
of the front of the body is determined by the rigidity constraint. the back of the body must budge
first. We thus have a quite unaesthetic feature for collisions in our game: a collision cannot
alter the trajectory of the body for quite a bit of time after happening.
**Collision information must spread "enough" across the body before any reaction can occur**.

It then becomes interesting to find out how long it takes for information
(or, equivalently, light) to propagate across a moving body.
This provides further information about collision latency, i.e. the time it takes for
a rigid body to respond to a collision event.

In the remaining parts of the article we assume the body is hitting an obstacle (e.g. a potential
field) at its front and calculate the time it takes for the information to propagate to various
points of the body. These calculations give a rough estimate of how long the body will continue
to move before it reacts at all to the collision.

Note that the scenario where the collision happens at the front of the body is the most
interesting, as moving objects tend to collide with stuff in front of them. It is also the
scenario that gives smaller propagation times as most of the body moves towards
the collision propagation front.

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

**Propagation to the back-center**

Here we do a quick calculation to figure out how long it takes for light to propagate from
the collision point, at the center of the front of the body, to the back of the body,
as shown in the figure below:

![propagation to back](/assets/dynamics-latency-3.svg)

The problem is effectively a one-dimensional problem. We assume the collision happens at
time $$t=0$$ and position $$x=0$$. The destination point has the following coordinate:

$$
x_{\mathrm{B}}(t) = -\frac{L}{\gamma} + vt,
$$

where $$L$$ is the length of the sides of the square rigid body, $$\gamma$$ is the usual
relativistic factor $$\gamma = (1 - v^2/c^2)^{-1/2}$$, $$v$$ is the speed of the body,
$$c$$ is the speed of light and $$t$$ is time. The collision information leaves at the origin
and goes towards the destination point with constant speed $$c$$:

$$
x_{\mathrm{C}}(t) = -c t.
$$

The collision time can be found by equating $$x_{\mathrm{B}}$$ and $$x_{\mathrm{C}}$$.
This gives:

$$
t_{\mathrm{CB}} = \frac{L}{\gamma \left(c + v\right)} =
\frac{L}{c} \sqrt{\frac{1 - \beta}{1 + \beta}},
$$

where $$\beta = v/c$$.

The good news is that the time required for the collision information to reach the back of the body
becomes smaller and smaller as the body's velocity becomes closer and closer to the speed of light
($$\beta \approx 1$$.) This happens because, as $$\beta \rightarrow 1$$, the body contracts more
and more and there is less distance between the collision and the destination points.
At the same time $$x_{\mathrm{B}}$$ and $$x_{\mathrm{C}}$$ are both moving towards each other
at roughly the speed of light, giving a relative speed of $$2c$$.

**Propagation to a front corner**

We now consider a different part of the body that the collision information needs to reach:
the top corner at the front of the body.

![propagation to front/top corner](/assets/dynamics-latency-4.svg)

We again assume the collision happens in the origin of our inertial reference frame
$$(t,\,x,\,y) = (0,\,0,\,0)$$, where the $$x$$ axis is the horizontal direction
in the picture and the $$y$$ axis is the vertical one.

The coordinates of the front corner can be written as follows:

$$
\begin{equation*}
\begin{aligned}
x_{\mathrm{F}}(t) & = vt\\
y_{\mathrm{F}}(t) & = L
\end{aligned}
\end{equation*}
$$

The collision information leaves at the origin and propagates towards all directions
with speed $$c$$, meeting the destination when
$$x_{\mathrm{F}}^2 + y_{\mathrm{F}}^2 = (ct)^2$$:

$$
(vt)^2 + L^2 = (ct)^2.
$$

This equation can be easily solved in $$t$$:

$$
t_{\mathrm{CF}} = \frac{L}{c} \gamma.
$$

This is **not** great news. The time it takes for the collision information to reach the top-front
corner increases as the body's velocity gets closer and closer to the speed of light.
This happens because the front corner is escaping from the propagating front. You can indeed easily
prove that the corner would be unreachable if it was travelling exactly at the speed of light.

Said that, it could be argued that a rigid body can start to react to a collision before information
has spread to all the parts of the body. From the reasonings we made in this article, we must wait
for the whole back side of the body to receive the information before the body can start to slow
down. There is no need to wait that information about the collision reaches the top-front corner.

# Recap

This article has gone very quickly through some findings and observations I made while studying
and implementing rigidity and dynamics in my relativistic game.
It should give an idea of what it takes to have relativistic rigid bodies interact in some
(physically correct) ways with the environment, although things get considerably more complicated
in a real implementation: collisions can happen continuously (e.g. for a player standing on
a platform, for example) and from multiple points. Aggregating collisions from multiple points and
reacting to them consistently is also a bit of a challenge.

A key takeaway is that there is no way a relativistic rigid body can just bounce instantaneously
against a wall/potential. Unless a velocity limiting mechanism is introduced in the game, it is
hard to prevent objects from going through walls, for example. Even with such a mechanism in place,
physical interactions feel soft and long-range rather than sharp and short-range.

From what I have seen so far, this is not a huge problem for a platformer-style game, where
the player is pulled towards the ground (or platforms) by a gravity-like force. In this case,
friction can be used as a velocity-limiting mechanism. The feel of the dynamics is still "soft",
rather than "sharp", but it kinda works.

More problematic is the case I have been dealing with recently: the flying robot shown
in [this video](https://youtube.com/shorts/LujkEuEgZmg?feature=share). Being able to fly allows
the player to explore more extreme relativistic conditions (higher velocities).
However, it is then problematic to contain the robot inside walls.

Is this the end of the little robot? Absolutely no. Velocity-limitation is one option, but I
think there is an alternative way to achieve neat collisions and contain the motion of the robot:
collision avoidance!
The idea is to do something completely different to what described in this article.
The robot does not interact with the room's walls anymore. Instead, it features a state-of-the art
navigation system that automatically brakes when getting too close to walls and other parts of the
environment. To be honest, this solution is maybe more realistic than the one described in this
article: a real robot moving at relativistic speed should do its utmost to avoid relativistic
collisions as there is now way it can survive them.
I have been experimenting a bit with this approach and I think it can work, although
it will require some time to get right.