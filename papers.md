---
layout: page
title: The VerifAI Workshop
subtitle: "VerifAI: AI Verification in the Wild @ ICLR 2026"
use-site-title: true
---
<div class="venue" style="font-size: 27px; display: block; font-family: 'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif; font-weight: 300; color: #404040; text-align: center;">
  (Rio, April 26/27, 2026)
</div>

# Accepted Papers

<div class="container">
  <ol>
    {% for p in site.data.papers %}
    <li style="margin-bottom: 12px;">
      <b>{{ p[1].title }}</b><br>
      <i>{{ p[1].authors }}</i>
    </li>
    {% endfor %}
  </ol>
</div>

<!-- # Reviewers

We are grateful to our fantastic reviewers for making our workshop reviewing process run smoothly:

<div class="reviewers">
<ul>
{% for reviewer in site.data.pc.people %}
    <li>{{ reviewer }}</li>
{% endfor %}
</ul>
</div>

<style>
.reviewers ul {
    columns: 4;
    -webkit-columns: 4;
    -moz-columns: 4;
    list-style-position: inside;
    padding-left: 0;
}
.reviewers li {
    break-inside: avoid;
    page-break-inside: avoid;
    padding: 2px 0;
}
</style> -->