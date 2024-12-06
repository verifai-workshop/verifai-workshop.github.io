---
layout: page
title: MATH-AI
subtitle: "The 4th Workshop on Mathematical Reasoning and AI"
use-site-title: true
---
<div class="venue" style="font-size: 27px; display: block; font-family: 'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif; font-weight: 300; color: #404040; text-align: center;">
  (Vancouver, December 14, 2024, <a href="https://mathai2024.github.io/" target="_blank">Website</a>)
</div>

# Schedule

<!-- #### Friday, December 14th, 2023
#### All times are in Central Standard Time (CST) ([Check local time](https://www.google.com/search?q=time+for+local+new+orleans))


#### Location: Room 217-219, New Orleans Convention Center ([Map](https://goo.gl/maps/8WXJ8h4Svng793Cc8))
#### Live video stream: [Link](https://neurips.cc/virtual/2022/workshop/50015) -->

TBD

<!-- <div class="container">
  <div class="row">
    <table class="table">
        {% for s in site.data.schedule %}
        <tr>
        <td>{{ s[1].start }}</td>
        {% if s[1].type == "General" %}
          <td>{{ s[1].event }}</td>
          <td></td>

        {% elsif s[1].type == "Invited" %}
          <td >Invited Talk</td>
          {% assign speaker_id = s[1].event %}
          {% assign speaker = site.data.speakers[speaker_id] %}
          <td >
            <i>{{ s[1].title }}</i><br>
            <a href="{{speaker.url}}">{{ speaker.name }}</a>, {{speaker.affiliation}}
            {% if speaker.title == "TBA" %}
            {% else %}
            <br><i><b>{{ speaker.title }}</b></i>
            {% endif %}
          </td>

        {% elsif s[1].type == "Contributed" %}
          <td >Contributed Talk</td>
          {% assign speaker = s[1] %}
          <td >
            <i>{{ speaker.title }}</i><br>
            <a href="{{speaker.url}}">{{ speaker.name }}</a>, {{speaker.affiliation}}
          </td>

        {% elsif s[1].type == "Spotlights" %}
          <td>Spotlights</td>
          {% assign speaker_id = s[1].event %}
          {% assign speaker = site.data.speakers[speaker_id] %}
          <td >
            <i>{{ s[1].title }}</i><br>
            <a href="{{speaker.url}}">{{ speaker.name }}</a>, {{speaker.affiliation}}
            {% if speaker.title == "TBA" %}
            {% else %}
            <br><i><b>{{ speaker.title }}</b></i>
            {% endif %}
          </td>

        {% elsif s[1].type == "Break" %}
          <td class="info">{{ s[1].event }}</td>
          <td class="info"></td>

        {% elsif s[1].type == "Session" %}
          <td><b>{{ s[1].event }}</b></td>
          <td></td>

        {% elsif s[1].type == "None" %}
          <td ></td>
          <td >{{ s[1].event }}</td>
          
        {% elsif s[1].type == "Panel" %}
          <td >Panel Discussion</td>
          <td>
            {% for speaker_id in s[1].speakers %}
              {% assign speaker = site.data.speakers[speaker_id] %}
              {% if speaker_id != s[1].speakers[-1] %}
                <a href="{{speaker.url}}">{{ speaker.name }}</a> ({{speaker.affiliation}}),
              {% else %}
                <a href="{{speaker.url}}">{{ speaker.name }}</a> ({{speaker.affiliation}})
              {% endif %}
              {% if forloop.index == 5 %}
                  <br>
              {% endif %}
            {% endfor %}
          </td>
        {% endif %}

        </tr>
        {% endfor %}
    </table>
  </div>
</div> -->