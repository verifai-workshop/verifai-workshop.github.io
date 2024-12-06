---
layout: page
title: MATH-AI
subtitle: "The 4th Workshop on Mathematical Reasoning and AI"
use-site-title: true
---
<div class="venue" style="font-size: 27px; display: block; font-family: 'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif; font-weight: 300; color: #404040; text-align: center;">
  (Vancouver, December 14, 2024, <a href="https://mathai2024.github.io/" target="_blank">Website</a>)
</div>

# Accepted Papers

The list of accepted papers can be found on OpenReview <a href="https://openreview.net/group?id=NeurIPS.cc/2024/Workshop/MATH-AI#tab-accept">here</a>.

# Reviewers

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
</style>