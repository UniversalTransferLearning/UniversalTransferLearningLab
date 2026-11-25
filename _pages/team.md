---
title: "UTL Lab - Team"
layout: gridlay
excerpt: "UTL Lab: Team members"
sitemap: false
permalink: /team/
---

[//]: # (# Group Members)




[//]: # (Jump to [staff]&#40;#staff&#41;, [master and bachelor students]&#40;#master-and-bachelor-students&#41;, [alumni]&#40;#alumni&#41;, [administrative support]&#40;#administrative-support&#41;, [lab visitors]&#40;#lab-visitors&#41;.)

## Professor
{% for member in site.data.team_members %}
<div class="pi-card" markdown="0">
  <div class="pi-photo">
    {% assign portrait = member.photo | prepend: '/images/teampic/' %}
    <img {% include display_src.html photo=portrait %} alt="{{ member.name | escape }}" decoding="async" />
  </div>
  <div class="pi-info">
    <h4>{{ member.name }}</h4>
    <p class="pi-meta">
    {{ member.info }} <br />
    {{ member.dept }}  <br />
    {{ member.school }}
    </p>
    {% if member.number_educ and member.number_educ > 0 %}
    <ul class="pi-cv">
    {% for i in (1..member.number_educ) %}{% assign key = 'education' | append: i %}
    <li> {{ member[key] }} </li>
    {% endfor %}
    </ul>
    {% endif %}
  </div>
</div>
{% endfor %}

<div class="pi-bio">

I joined the Department of Artificial Intelligence at Korea University in Fall 2023.

I was a research staff member at MIT-IBM Watson AI Lab. I obtained my PhD in the Image and Video Computing Group at Boston University, advised by Prof. Stan Sclaroff and Prof. Kate Saenko. I received my Master's degree in Computer Science from University of Southern California. I had been working on 3D face modeling and recognition with Prof. Gerard Medioni and Dr. Jongmoo Choi in Computer Vision Group. My research interests focus on representation learning in Computer Vision and Deep Learning. Here is my <a href="https://scholar.google.com/citations?user=UsqNPH4AAAAJ&hl">Google Scholar</a>.

</div>

<div class="cta-box">

**We are  looking for new MS/PhD, PhD, and Postdocs to join the team** [(see openings)]({{ site.url }}{{ site.baseurl }}/openings) **!**

</div>

<div class="embed-responsive embed-responsive-16by9 video-frame" markdown="0">
  <a class="video-preview" href="https://www.youtube.com/watch?v=UFckOenT790" aria-label="Play KTN's Korea University AI Department video">
    <img src="{{ '/images/teampic/ktn-video-preview.jpg' | relative_url }}" alt="" loading="lazy" decoding="async">
  </a>
  <template>
    <iframe class="embed-responsive-item" src="https://www.youtube.com/embed/UFckOenT790?autoplay=1"
      title="KTN – Korea University AI Department"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
      referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
  </template>
</div>
<script defer src="{{ '/js/team-video.js' | relative_url }}"></script>

##  Students

<!-- [//]: # (Sojung Ahn <br>)

[//]: # (Jung Myung Wi <br>)

[//]: # (Dujin Lee <br>)

[//]: # (Yongwoo Kim <br>)

[//]: # (Hyunsoo Kim <br>) -->

<div class="people-grid" markdown="0">
{% for member in site.data.students %}
<div class="person-card">
  <div class="person-photo">
    {% assign portrait = member.photo | prepend: '/images/teampic/' %}
    <img {% include display_src.html photo=portrait %} alt="{{ member.name | escape }}" loading="lazy" decoding="async" />
  </div>
  <div class="person-body">
    <h4>{{ member.name }}</h4>
    <p class="person-role">{{ member.info }}</p>
    <p class="person-email">
      <span class="email-label">Email:</span> <a href="mailto:{{ member.email }}">{{ member.email }}</a>
    </p>
    {% if member.website %}
    <p class="person-link">
      <a href="{{ member.website }}" target="_blank" rel="noopener noreferrer">🔗 Website</a>
    </p>
    {% endif %}
    {% if member.number_educ and member.number_educ > 0 %}
    <ul class="person-cv">
    {% for i in (1..member.number_educ) %}{% assign key = 'education' | append: i %}
    <li> {{ member[key] }} </li>
    {% endfor %}
    </ul>
    {% endif %}
  </div>
</div>
{% endfor %}
</div>

## Visitors

<div class="people-list" markdown="0">
{% for member in site.data.ug_students %}
<div class="person-row">
  <!-- <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" /> -->
  <h4>{{ member.name }}</h4>
  <p class="person-role">{{ member.info }}</p> <!-- <br>email: <{{ member.email }}></i> -->
  {% if member.number_educ and member.number_educ > 0 %}
  <ul class="person-cv">
  {% for i in (1..member.number_educ) %}{% assign key = 'education' | append: i %}
  <li> {{ member[key] }} </li>
  {% endfor %}
  </ul>
  {% endif %}
</div>
{% endfor %}
</div>

## Alumni

<div class="people-list" markdown="0">
{% for member in site.data.alumni_members %}
<div class="person-row">
  <h4>{{ member.name }}</h4>
  <p class="person-role">{{ member.info }}</p>
  {% if member.website %}<p class="person-link"><a href="{{ member.website }}" target="_blank" rel="noopener noreferrer">🔗 Website</a></p>{% endif %}
</div>
{% endfor %}
</div>

<!-- ## Former students -->

[//]: # (<br />)
[//]: # (<div class="row">)

[//]: # ()
[//]: # (<div class="col-sm-4 clearfix">)

[//]: # (<h4>Visitors</h4>)

[//]: # ({% for member in site.data.alumni_visitors %})

[//]: # ({{ member.name }})

[//]: # ({% endfor %})

[//]: # (</div>)

[//]: # ()
[//]: # (<div class="col-sm-4 clearfix">)

[//]: # (<h4>Graduate students</h4>)


[//]: # ({% for member in site.data.alumni_msc %})

[//]: # ({{ member.name }})

[//]: # ({% endfor %})

[//]: # (</div>)

[//]: # ()
[//]: # (<div class="col-sm-4 clearfix">)

[//]: # (<h4>Bachelor Students</h4>)

[//]: # ({% for member in site.data.alumni_bsc %})

[//]: # ({{ member.name }})

[//]: # ({% endfor %})

[//]: # (</div>)

[//]: # ()
[//]: # (</div>)


[//]: # (## Administrative Support)

[//]: # (<a href="mailto:Rijsewijk@Physics.LeidenUniv.nl">Ellie van Rijsewijk</a> is helping us &#40;and other groups&#41; with administration.)
