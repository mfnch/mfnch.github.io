---
layout: page
title: Articles
permalink: /articles/
---

Here is a list of articles I wrote while working on my relativistic platformer video game.
They are grouped by topic.

# Special Relativity
{% for article in site.articles %}
  <p>
    <a href="{{ article.url }}">
      {{ article.title }}
    </a>
  </p>
{% endfor %}
