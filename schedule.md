---
layout: page
title: The VerifAI Workshop
subtitle: "VerifAI: AI Verification in the Wild @ ICLR 2025"
use-site-title: true
---
<div class="venue" style="font-size: 27px; display: block; font-family: 'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif; font-weight: 300; color: #404040; text-align: center;">
  (Singapore, April 27, 2025)
</div>


#### (All times are in Singapore Time)


#### Location: Garnet 218-219, Singapore EXPO
<!-- #### Live video stream: [Link](https://neurips.cc/virtual/2022/workshop/50015) -->


<div class="container">
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
            <i>{{ s[1].title }}</i>
            <a href="{{speaker.url}}">{{ speaker.name }}</a>
            {% if speaker.title == "TBA" %}
            {% else %}
            <br><i><b>{{ speaker.title }}</b></i>
            {% endif %}
          </td>

        {% elsif s[1].type == "Contributed" %}
          <td >Contributed Talk</td>
          {% assign speaker = s[1] %}
          <td >
            <i>{{ speaker.name }}</i><br>
          </td>

        {% elsif s[1].type == "Spotlights" %}
          <td>Spotlights</td>
          {% assign speaker_id = s[1].event %}
          {% assign speaker = site.data.speakers[speaker_id] %}
          <td >
            <i>{{ s[1].title }}</i><br>
            <a href="{{speaker.url}}">{{ speaker.name }}</a>
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
</div>