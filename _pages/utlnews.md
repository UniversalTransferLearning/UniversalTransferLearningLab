---
title: "UTL Lab - News"
layout: gridlay
excerpt: "UTL Lab: News"
sitemap: false
permalink: /utlnews/
---

# News

<div class="news-list">
{% for article in site.data.news %}
<div class="news-card">
<div class="news-date">
  {{ article.date }}
</div>
<div class="news-headline">
  {{ article.headline }}
</div>
</div>
{% endfor %}
</div>
