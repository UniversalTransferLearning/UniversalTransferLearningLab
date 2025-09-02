---
title: "UTL Lab - News"
layout: gridlay
excerpt: "UTL Lab: News"
sitemap: false
permalink: /utlnews/
---

# News

{% assign sorted_news = site.data.news | sort: 'date' | reverse %}
{% assign number_printed = 0 %}

{% for article in sorted_news %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-12" style="margin-bottom: 20px;">
  <div class="news-card" style="border-left: 4px solid #007acc; padding: 20px; background-color: #f8f9fa; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
    <div class="news-date" style="color: #007acc; font-weight: bold; font-size: 0.9em; margin-bottom: 10px;">
      {{ article.date }}
    </div>
    <div class="news-headline" style="line-height: 1.6; color: #333; font-size: 1.1em;">
      {{ article.headline }}
    </div>
  </div>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}
