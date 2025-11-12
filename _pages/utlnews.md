---
title: "UTL Lab - News"
layout: gridlay
excerpt: "UTL Lab: News"
sitemap: false
permalink: /utlnews/
---

# News

{% assign all_years = "" | split: "," %}
{% for article in site.data.news %}
  {% assign article_year = article.date | split: ' ' | last %}
  {% unless all_years contains article_year %}
    {% assign all_years = all_years | push: article_year %}
  {% endunless %}
{% endfor %}

{% assign sorted_years = all_years | sort | reverse %}

{% for year in sorted_years %}
## {{ year }}

  {% assign months = "Dec.,Nov.,Oct.,Sep.,Aug.,Jul.,Jun.,May,Apr.,Mar.,Feb.,Jan.,December,November,October,September,August,July,June,April,March,February,January" | split: "," %}
  
  {% for month in months %}
    {% for article in site.data.news %}
      {% assign article_year = article.date | split: ' ' | last %}
      {% if article_year == year and article.date contains month %}
{{ article.date }}: {{ article.headline }}
      {% endif %}
    {% endfor %}
  {% endfor %}

{% endfor %}
