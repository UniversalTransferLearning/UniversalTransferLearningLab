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
<div class="news-card" style="margin:16px 0; border-left:4px solid #8B0000; padding:16px; background:#f8f9fa; border-radius:8px;">
<div class="news-date" style="color:#8B0000; font-weight:700; font-size:0.95em; margin-bottom:6px;">
  {{ article.date }}
</div>
<div class="news-headline" style="line-height:1.6; color:#333; font-size:1.05em;">
  {{ article.headline }}
</div>
</div>
{% endfor %}
</div>
