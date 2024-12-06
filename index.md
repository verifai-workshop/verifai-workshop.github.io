---
layout: page
title: The VerifAI Workshop
subtitle: "VerifAI: AI Verification in the Wild @ ICLR 2025"
use-site-title: true
---
<div class="venue" style="font-size: 27px; display: block; font-family: 'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif; font-weight: 300; color: #404040; text-align: center;">
  (Singapore, April 27/28, 2025)
</div>



<div class="sharethis-inline-share-buttons"></div>
<meta name="thumbnail" content="./img/iclr-logo.jpg" />

# Reviewer Nomination

If you'd like to become a reviewer for the workshop, or recommend someone, [please use this form](404.html).

# Overview
This workshop explores the intersection of scale-driven generative artificial intelligence (AI) and the correctness-focused principles of verification. Formal analysis tools such as theorem provers, satisfiability solvers, and execution monitoring have demonstrated success in ensuring properties of interest across a range of tasks in software development and mathematics where precise reasoning is necessary. However, these methods face scaling challenges. Recently, generative AI such as large language models (LLMs) has been explored as a scalable and adaptable option to create solutions in these settings. The effectiveness of AI in these settings increases with more compute and data, but unlike traditional formalisms, they are built around probabilistic methods – not correctness by construction. In the VerifAI: AI Verification in the Wild workshop we invite papers and discussions that discuss how to bridge these two fields. Potential angles include, but are not limited to the following: generative AI for formal methods, formal methods for generative AI, AI as verifiers, datasets and benchmarks, and a special theme: LLMs for code generation. We welcome novel methodologies, analytic contributions, works in progress, negative results, and review and positional papers that will foster discussion. We will also have a track for tiny or short papers.

<hr>

# Speakers & Panelists
<div class="container" style="margin-top: 20px;margin-bottom: 0px;">
  <div class="row">
    {% for p in site.data.speakers %}
    {% if forloop.index<=5 %}
    {% capture id %}{{ p[0] }}{% endcapture %}
    {% include profile.html p=p %}
    {% endif %}
    {% endfor %}
  </div>
  <div class="row">
    {% for p in site.data.speakers %}
    {% capture id %}{{ p[0] }}{% endcapture %}
    {% if forloop.index>5 and forloop.index<=10%}
    {% include profile.html p=p %}
    {% endif %}
    {% endfor %}
  </div>
  <div class="row">
    {% for p in site.data.speakers %}
    {% capture id %}{{ p[0] }}{% endcapture %}
    {% if forloop.index>10%}
    {% include profile.html p=p %}
    {% endif %}
    {% endfor %}
  </div>
<a href="speakers">More Info</a>
</div>

<hr>

# Organizers
<!-- # Organizers -->

<!-- prettier-ignore -->
<div class="container" style="margin-top: 25px;margin-bottom: 40px;">
  <!-- <br> 
  <div class="row" style="margin: -30px;"> -->
  <div class="row">
    {% for p in site.data.organizers %}
    {% if forloop.index<=4 %}
    {% capture id %}{{ p[0] }}{% endcapture %}
    {% include profile.html p=p %}
    {% endif %}
    {% endfor %}
  </div>
  <div class="row">
    {% for p in site.data.organizers %}
    {% capture id %}{{ p[0] }}{% endcapture %}
    {% if forloop.index>4 and forloop.index<=8%}
    {% include profile.html p=p %}
    {% endif %}
    {% endfor %}
  </div>
</div>
<hr>

<!-- # Program Committee
<div class="container">
  <ul class="list-group list-group-flush">
    {% for p in site.data.pc.people %}
      <li class="list-group-item col-xs-6 col-sm-4 col-md-3">{{ p }}</li>
    {% endfor %}
  </ul>
</div>
<hr> -->

# Related Venues

<div class="container" style="margin-bottom: 10px;"></div>
- [NeurIPS'24 Workshop on Formal Verification and Machine Learning (WFVML 2024)](https://www.ml-verification.com/) 

<div class="container" style="margin-bottom: 10px;"></div>

<hr>

<!-- Contact: <mathai.neurips2024@gmail.com>. -->
Website template from https://mathai2024.github.io/.
