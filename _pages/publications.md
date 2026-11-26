---
title: "UTL Lab - Publications"
layout: gridlay
excerpt: "UTL Lab -- Publications."
sitemap: false
permalink: /publications/
---

 

<h1> Publications </h1>
<p class="page-intro">Here is the <a href="https://scholar.google.com/citations?user=UsqNPH4AAAAJ&hl=en"> full list of publications.</a></p>


[//]: # (## Group highlights)


[//]: # ({% assign number_printed = 0 %})

[//]: # ({% for publi in site.data.publist %})

[//]: # ()
[//]: # ({% assign even_odd = number_printed | modulo: 2 %})

[//]: # ({% if publi.highlight == 1 %})

[//]: # ()
[//]: # ({% if even_odd == 0 %})

[//]: # (<div class="row">)

[//]: # ({% endif %})

[//]: # ()
[//]: # (<div class="col-sm-6 clearfix">)

[//]: # ( <div class="well">)

[//]: # (  <pubtit>{{ publi.title }}</pubtit>)

[//]: # (  <img src="{{ site.url }}{{ site.baseurl }}/images/pubpic/{{ publi.image }}" class="img-responsive" width="33%" style="float: left" />)

[//]: # (  <p>{{ publi.description }}</p>)

[//]: # (  <p><em>{{ publi.authors }}</em></p>)

[//]: # (  <p><strong><a href="{{ publi.link.url }}" style="font-size: 14px;">{{ publi.link.display | markdownify | remove: '<p>' | remove: '</p>' | strip }}</a></strong></p>)

[//]: # (  <p class="text-danger"><strong> {{ publi.news1 }}</strong></p>)

[//]: # (  <p> {{ publi.news2 }}</p>)

[//]: # ( </div>)

[//]: # (</div>)

[//]: # ()
[//]: # ({% assign number_printed = number_printed | plus: 1 %})

[//]: # ()
[//]: # ({% if even_odd == 1 %})

[//]: # (</div>)

[//]: # ({% endif %})

[//]: # ()
[//]: # ({% endif %})

[//]: # ({% endfor %})

[//]: # ()
[//]: # ({% assign even_odd = number_printed | modulo: 2 %})

[//]: # ({% if even_odd == 1 %})

[//]: # (</div>)

[//]: # ({% endif %})

[//]: # ()
[//]: # (<p> &nbsp; </p>)


[//]: # (## Patents)

[//]: # (<em>Milan P Allan, S Gröblacher, RA Norte, M Leeuwenhoek</em><br />Novel atomic force microscopy probes with phononic crystals<br /> PCT/NL20-20/050797 &#40;2020&#41;)

[//]: # ()
[//]: # (<em>Milan P Allan</em><br /> Methods of manufacturing superconductor and phononic elements <br /> <a href="https://patents.google.com/patent/US10439125B2/en?inventor=Milan+ALLAN&oq=inventor:&#40;Milan+ALLAN&#41;">US10439125B2 &#40;2016&#41;</a>)


<div class="pub-list" markdown="0">
{% assign year_last = 0 %}
{% for publi in site.data.publist %}
{% if year_last != publi.year %}{% assign year_last = publi.year %}
<h3 class="pub-year">{{ publi.year }}</h3>
{% endif %}
{% assign formatted_authors = publi.authors %}
{% for author in site.data.utl_authors %}
  {% capture bold_author %}<span class="utl-author">{{ author }}</span>{% endcapture %}
  {% assign formatted_authors = formatted_authors | replace: author, bold_author %}
{% endfor %}
{% assign paper_title = publi.title | markdownify | remove: '<p>' | remove: '</p>' | strip %}
{% assign paper_url = publi.link.url | strip %}
<div class="pub-item">
<div class="pub-title">
{% if paper_url != empty %}
  <a href="{{ paper_url | escape }}">{{ paper_title }}&nbsp;<span class="glyphicon glyphicon-link pub-link-mark" aria-hidden="true"></span></a>
{% else %}
  {{ paper_title }}
{% endif %}
</div>
<div class="pub-authors">{{ formatted_authors | markdownify | remove: '<p>' | remove: '</p>' | strip }}</div>
{% if publi.affiliations %}<div class="pub-affiliations">{{ publi.affiliations }}</div>{% endif %}
<div class="pub-venue">{{ publi.link.display | markdownify | remove: '<p>' | remove: '</p>' | strip }}</div>
</div>
{% endfor %}
</div>
