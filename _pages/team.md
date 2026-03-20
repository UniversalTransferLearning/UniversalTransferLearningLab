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
{% assign number_printed = 0 %}
{% for member in site.data.team_members %}

{% assign even_odd = number_printed | modulo: 1 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-12">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  <h4>{{ member.name }}</h4>

[//]: # (  <i>{{ member.info }} <!--<br>email: <{{ member.email }}></i> -->)
  {{ member.info }} <!--<br>email: <{{ member.email }}> --> <br />
  {{ member.dept }}  <br />
  {{ member.school }}
  <ul style="overflow: hidden">

  {% if member.number_educ == 1 %}
  <li> {{ member.education1 }} </li>
  {% endif %}

  {% if member.number_educ == 2 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  {% endif %}

  {% if member.number_educ == 3 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  {% endif %}

  {% if member.number_educ == 4 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  <li> {{ member.education4 }} </li>
  {% endif %}

  {% if member.number_educ == 5 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  <li> {{ member.education4 }} </li>
  <li> {{ member.education5 }} </li>
  {% endif %}

  </ul>
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


I joined the Department of Artificial Intelligence at Korea University in Fall 2023. Please send an <a href = "mailto: d_kim@korea.ac.kr">email</a> if you are interested in our lab and in working with me.

I was a research staff member at MIT-IBM Watson AI Lab. I obtained my PhD in the Image and Video Computing Group at Boston University, advised by Prof. Stan Sclaroff and Prof. Kate Saenko. I received my Master's degree in Computer Science from University of Southern California. I had been working on 3D face modeling and recognition with Prof. Gerard Medioni and Dr. Jongmoo Choi in Computer Vision Group. My research interests focus on representation learning in Computer Vision and Deep Learning. Here is my <a href="https://scholar.google.com/citations?user=UsqNPH4AAAAJ&hl">Google Scholar</a>.

**We are  looking for new MS/PhD, PhD, and Postdocs to join the team** [(see openings)]({{ site.url }}{{ site.baseurl }}/openings) **!** <br>

##  Students

<!-- [//]: # (Sojung Ahn <br>)

[//]: # (Jung Myung Wi <br>)

[//]: # (Dujin Lee <br>)

[//]: # (Yongwoo Kim <br>)

[//]: # (Hyunsoo Kim <br>) -->


{% assign number_printed = 0 %}
{% for member in site.data.students %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  <h4>{{ member.name }}</h4>
  <p><i>{{ member.info }}</i></p>
  <p>Email: <a href="mailto:{{ member.email }}">{{ member.email }}</a></p>
  <ul style="overflow: hidden">

  {% if member.number_educ == 1 %}
  <li> {{ member.education1 }} </li>
  {% endif %}

  {% if member.number_educ == 2 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  {% endif %}

  {% if member.number_educ == 3 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  {% endif %}

  {% if member.number_educ == 4 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  <li> {{ member.education4 }} </li>
  {% endif %}

  </ul>
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
<br />

## Visitors

{% assign number_printed = 0 %}
{% for member in site.data.ug_students %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <!-- <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" /> -->
  <h4>{{ member.name }}</h4>
  <i>{{ member.info }} <!-- <br>email: <{{ member.email }}></i> -->
  <ul style="overflow: hidden">

  {% if member.number_educ == 1 %}
  <li> {{ member.education1 }} </li>
  {% endif %}

  {% if member.number_educ == 2 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  {% endif %}

  {% if member.number_educ == 3 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  {% endif %}

  {% if member.number_educ == 4 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  <li> {{ member.education4 }} </li>
  {% endif %}

  </ul>
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
<br />

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
