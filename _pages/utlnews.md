---
title: "UTL Lab - News"
layout: gridlay
excerpt: "UTL Lab: News"
sitemap: false
permalink: /utlnews/
---

# News

{% assign sorted_news = site.data.news | sort: 'date_iso' %}

<div class="news-list">
{% for article in sorted_news %}
<div class="news-card" style="margin:16px 0; border-left:4px solid #007acc; padding:16px; background:#f8f9fa; border-radius:8px;">
<div class="news-date" style="color:#007acc; font-weight:700; font-size:0.95em; margin-bottom:6px;">
  {{ article.date }}
</div>
<div class="news-headline" style="line-height:1.6; color:#333; font-size:1.05em;">
  {{ article.headline }}
</div>
</div>
{% endfor %}
</div>