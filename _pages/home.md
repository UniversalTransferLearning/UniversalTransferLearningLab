---
title: "Universal Transfer Learning Lab - Home"
layout: homelay
excerpt: "Universal Transfer Learning Lab at Korea University."
sitemap: false
permalink: /
---
<div class="home-logo">
  <img src="../images/logopic/logo_UTL.png" alt="UTL Lab Logo">
</div>
<p class="lead-text">We are <strong>Universal Transfer Learning (UTL)</strong> lab at Korea University with <strong>Prof. Donghyun Kim.</strong> Our research pursuits are situated under the expansive umbrella of transfer learning, with a particular emphasis on investigating the transferability, generalization, and adaptability of robust artificial intelligence (AI) models across a wide array of AI domains and disciplines.</p>
<h2 id="research-area">Research Area</h2>
<p>Our overarching objective is to pioneer the creation of highly effective transfer learning algorithms that can seamlessly transcend the boundaries of disparate domains and modalities found within a multitude of fields. These algorithms will be specifically tailored to cater to a wide spectrum of real-world applications, thus driving innovation and advancements in various industries and sectors. </p>

{% comment %}
<h3 class="research-poster-title" id="transferable-intelligence">Transferable Intelligence</h3>
<p>Across domains, modalities, and tasks</p>
<div class="research-fields" markdown="0">
  <section>
    <h4>Embodied AI &amp; Robotics</h4>
    <figure>
      {% include research/robotics.html %}
      <figcaption>Grounding “Make a cup of coffee” in a sequence of physical actions.</figcaption>
    </figure>
    <details>
      <summary>Planning and grasping</summary>
      <p>We study how robots connect instructions to the objects they see and the actions they can take.</p>
      <p>In the kitchen, the robot must grasp the mug, place it under the spout, and press the brew button. We study how vision-language-action models grasp objects from different viewpoints and how these skills transfer between kitchens, living rooms, and workshops.</p>
    </details>
  </section>
  <section>
    <h4>Multimodal &amp; Vision-Language Learning</h4>
    <figure>
      {% include research/vision-language.html %}
      <figcaption>“Find the small red mug left of the machine.”</figcaption>
    </figure>
    <details>
      <summary>Retrieval and scene understanding</summary>
      <p>We study how models connect words to objects and relationships in images, and how they follow events in video.</p>
      <p>In composed image retrieval, a reference photo of a dog and the instruction “Add a red hat” together specify the image to find. In scene graph generation, the model describes relationships: the mug is left of the machine, and both are on the table.</p>
      <p>For video understanding and movie retrieval-augmented generation (Movie RAG), the evidence unfolds over time. To answer “What did she take from the fridge?”, a model must find the moment she takes out a bottle.</p>
    </details>
  </section>
  <section>
    <h4>Foundation Model Learning &amp; Adaptation</h4>
    <figure>
      {% include research/adaptation.html %}
      <figcaption>Two small trainable matrices adapt a model while its pretrained weights stay frozen.</figcaption>
    </figure>
    <details>
      <summary>Adaptation methods and examples</summary>
      <p>We study how to adapt large language models, vision-language models, and diffusion models for vision, language, reasoning, and generation while retaining existing skills.</p>
      <p>For efficient adaptation, we keep the original weights frozen and learn a low-rank update (W = W₀ + BA). For continual learning, we adapt a generator, select examples to replay, and distill that knowledge into a vision-language model.</p>
      <p>We study how to erase a selected visual style using paired images, and how to assess multimodal safety in Korean cultural contexts. We also examine whether a model can generate exactly “three guitars and two pillows,” or use diffusion to recognize three differently shaped objects as soap dispensers.</p>
    </details>
  </section>
  <section>
    <h4>Transfer &amp; Generalizable AI</h4>
    <figure>
      {% include research/transfer.html %}
      <figcaption>Can a model trained on simulated streets recognize what it sees on a real road?</figcaption>
    </figure>
    <details>
      <summary>Adaptation and generalization</summary>
      <p>We study how to pretrain representations that preserve class identity when the data source or viewing conditions change.</p>
      <p>In domain adaptation, the model has access to data from the target domain during training. In domain generalization, it first encounters that domain at test time. In both cases, we want examples of the same class to remain recognizable across domains.</p>
      <p>We explore transfer across synthetic data, adverse weather, microscopy images, diverse objects, and event-camera data. Cross-domain retrieval poses a related question: can a drawing of a bird retrieve a photograph of its counterpart?</p>
    </details>
  </section>
</div>
{% endcomment %}

<p>Our main research interests include but not limited to the following: </p>
<ul class="interest-grid">
  <li>Domain Transfer (Domain Adaptation/Generalization) </li>
  <li>Task Transfer</li>
  <li>Pre-training for Transfer Learning</li>
  <li>Foundation Model Adaptation</li>
  <li>Efficient Adaptation</li>
  <li>Multimodal Representation Learning</li>
  <li>Transferable Representation Learning</li>
  <li>Un/self-supervised Learning</li>
  <li>Learning From Synthetic Data</li>
  <li>Learning Compositionality</li>
  <li>Embodied AI</li>
  <li>Etc…</li>
</ul>

{% assign research_poster = '/images/picpic/UTL-Research-Poster-Square.png' | relative_url %}
<a id="research-poster" class="research-poster" href="{{ research_poster }}" aria-label="View the full-size Transferable Intelligence research poster">
  <img {% include display_src.html photo='/images/picpic/UTL-Research-Poster-Square.png' %} width="1440" height="1440" loading="lazy" decoding="async" alt="Transferable Intelligence: Embodied AI &amp; Robotics, Multimodal &amp; Vision-Language Learning, Foundation Model Learning &amp; Adaptation, and Transfer &amp; Generalizable AI.">
</a>

<div class="cta-box">

**We are  looking for passionate new MS, MS/PhD, PhD students or Postdocs to join the team** [(more info)]({{ site.url }}{{ site.baseurl }}/openings) **!**

</div>
