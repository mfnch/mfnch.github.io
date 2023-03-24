---
layout: post
title:  "Why you need to pre-multiply textures"
categories: Games
date: 2023-03-24 10:41:00
usemathjax: true
---

**TL;DR** *textures with transparency are going to be incorrectly rendered in a GPU shader
unless they are pre-multiplied. This applies to textures containing color (RGB data),
but also textures containing other stuff (normals, depth, ...)*

I will be brief in this post. My aim is to make one main point:
**pre-multiplication is not only for color textures**.
You must pre-multiply your texture before loading it in the GPU memory if:

- you are using one channel in the texture to signal that the information
  in the other channels is absent and should be ignored when interpolating
  across the texture or when computing mipmaps.
- you are doing any kind of linear filtering on the texture, such as interpolating or scaling.
  If you are probing the textures only at the texel centers, then you are likely to have
  no troubles at all.

# What's the problem?

Suppose you have two adjacent pixels and you are probing in between them, exactly in the
middle between them. Suppose one pixel is red and almost fully opaque, say
(red=1, green=0, blue=0, alpha=0.8), and the other is green and almost fully transparent,
say (red=0, green=1, blue=0, alpha=0.1).

<figure>
  <img src="{{site.url}}/assets/premultiplication.svg"
       alt="blending between two pixels with and without premultiplication"/>
  <figcaption><strong>Figure:</strong> the circles show the resulting of blending two pixels
    with and without premultiplying the RGB in the OpenGL texture. The green color is almost
    transparent and is not expected to affect much the final color.</figcaption>
</figure>

You'd expect the interpolated value to be more
red than green, right? Well, in GPU textures all channels are independent.
If you load a texture with these pixel values and probe in between them, you'll get the
unweighted average between the pixel values, that is (red=0.5, green=0.5, blue=0, alpha=0.45),
which corresponds to a yellow with some amount of trasparency. The resulting RGB values do
not depend at all on the transparencies of the adjacent pixels, which is clearly wrong.

<figure>
  <img src="{{site.url}}/assets/premul_black_borders.png"
       alt="black borders without premultiplication"/>
  <figcaption><strong>Figure:</strong> Non-premultiplied textures tend to be excessively dark
  around borders between full opacity and full transparency.</figcaption>
</figure>

# What's the solution?

The alpha channel in most textures represents the presence/absence of color or other
information. For a pixel with components $$(r,\,g,\,b,\,a)$$,
$$(r,\,g,\,b)$$ is the color of the pixel, while $$(ra,\,ga,\,ba)$$ can be seen as
the amount of that color contained in it.
We should sum the amounts of colors, rather than the colors themselves.
This can be achieved using a weighted sum. For the red-green pixels example
we considered before, we should do something like:

$$
(r_{12},\,g_{12},\,b_{12}) =
  \frac{(r_1,\,g_1,\,b_1)\,a_1 + (r_2,\,g_2,\,b_2)\,a_2}
       {a_1 + a_2},
$$

to obtain the color of the pixel in the middle.

Note that this is just a weighted sum, *it is not a color blending operation*.
Indeed, the equation above is symmetric in the two color values, while blending in general
is an asymmetric operation, meaning that blending color A on top of B is not the same as
blending B on top of A. As mentioned earlier, the reasonings we are doing here hold in general,
for more than just color values!

Luckily for us, we can rewrite the equation above as follows:

$$
(r_{12} a_{12},\,g_{12} a_{12},\,b_{12} a_{12}) =
  \frac{(r_1 a_1,\,g_1 a_1,\,b_1 a_1) + (r_2 a_2,\,g_2 a_2,\,b_2 a_2)}{2},
$$

where we introduced $$a_{12} = (a_1 + a_2)/2$$, which is the alpha channel linearly
interpolated between the two pixels.

This is cool! The weighted sum becomes a simple linear interpolation if rather
than dealing with raw colors we deal with the color amounts, i.e. the colors multiplied
by the corresponding alpha values.

But how do we use this in practice? Well, we add a fourth component to make
the equation above a bit more useful:

$$
(r_{12} a_{12},\,g_{12} a_{12},\,b_{12} a_{12},\,a_{12}) =
  \frac{(r_1 a_1,\,g_1 a_1,\,b_1 a_1,\,a_1) + (r_2 a_2,\,g_2 a_2,\,b_2 a_2,\,a_2)}{2}.
$$

This shows us that, if we load the textures replacing the pixels
$$(r,\,g,\,b,\,a)$$ with the premultiplied values $$(ra,\,ga,\,ba,\,a)$$,
then the texture unit in the GPU will simply interpolate between
the premultiplied values, giving again a premultiplied color value.

All we need to do then, is to undo the premultiplication in the shader,
to obtain the correctly weighted color channels, or normals or whatever else we
stored in the texture. The GLSL code would look as follows:

{% highlight glsl %}
  vec4 c = texture(t, uv);
  c.rgb /= (c.a > 0) ? c.a : 1.0;
{% endhighlight %}

For normal maps:

{% highlight glsl %}
  vec4 normal_raw = texture(t, uv);
  normal_raw.rgb /= (normal_raw.a > 0.0) ? normal_raw.a : 1.0;
  vec3 normal = 2.0 * normal_raw.rgb - 1.0;
  normal /= max(0.01, length(normal));
{% endhighlight %}

Not premultiplying normal maps leads to artefacts at borders between opaque and transparent regions,
where the normals end up receiving contributions from pixels where normal information is absent.
In my experience, this leads to artefacts if the normals are defined as pointing
in the z direction in the regions of transparency.

An alternative, albeit less accurate, way to mitigate these issues, is to define
the normals to (0, 0, 0) in the areas of transparency. This reduces the lengths
of the normals at borders (similar to the darkening of the pixels for diffuse maps),
but the direction can be recovered when readjusting the length of the normals,
as done in the code fragment above.

A more thorough discussion can be found
[here](https://www.realtimerendering.com/blog/gpus-prefer-premultiplication/).
