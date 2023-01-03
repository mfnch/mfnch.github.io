---
layout: page
title: Articles
permalink: /articles/
---

This page collects articles I wrote while working on my relativistic platformer video game.
They are grouped by topic.

# Special Relativity

The articles in this section collect results that I find useful for the development of my
relativistic video game. They are quite dense with formulas and probably not of much use outside
the narrow context of Special Relativity. I used to collect these results in a private
[Latex](https://en.wikipedia.org/wiki/LaTeX) document. I decided to move them to this site.
At the very least, they provide documentation for the work I am doing and give external people
a chance of checking that what I am doing is correct, following the scientific spirit :)

{% for article in site.articles %}
  {% if article.categories contains "SR" %}
  <p>
    <a href="{{ article.url }}">
      {{ article.title }}
    </a>
  </p>
  {% endif %}
{% endfor %}

# Games

Here are some posts about video games and game programming:

{% for article in site.articles %}
  {% if article.categories contains "Games" %}
  <p>
    <a href="{{ article.url }}">
      {{ article.title }}
    </a>
  </p>
  {% endif %}
{% endfor %}
