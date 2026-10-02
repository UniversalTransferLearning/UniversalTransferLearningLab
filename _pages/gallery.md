---
title: "UTL Lab - Gallery"
layout: gridlay
excerpt: "UTL Lab Gallery"
sitemap: false
permalink: /gallery/
---

<h1>Gallery</h1>

{% for group in site.data.gallery %}

<div class="gallery-year">
<h2>{{ group.year }}</h2>

<div class="row">
{% for activity in group.activities %}

<div class="col-sm-6">
{% include gallery_card.html activity=activity %}
</div>

{% endfor %}
</div>

</div>

{% endfor %}