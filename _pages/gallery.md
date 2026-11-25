---
title: "UTL Lab - Gallery"
layout: gridlay
excerpt: "UTL Lab Gallery"
sitemap: false
permalink: /gallery/
---

<div class="gallery-archive" markdown="0">
  <header class="gallery-header">
    <h1>Gallery</h1>
  </header>

  {% for group in site.data.gallery %}
  <section class="gallery-year" aria-labelledby="gallery-{{ group.year }}">
    <h2 id="gallery-{{ group.year }}">{{ group.year }}</h2>
    <div class="gallery-grid">
      {% for activity in group.activities %}
      {% include gallery_card.html activity=activity %}
      {% endfor %}
    </div>
  </section>
  {% endfor %}

</div>
<script src="{{ '/js/gallery.js' | relative_url }}" defer></script>
