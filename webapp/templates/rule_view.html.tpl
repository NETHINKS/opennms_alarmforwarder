{% include 'include/header.html.tpl' %}

<!-- page navigation -->
<ul class="nav nav-pills">
    <li role="presentation">
        <a href="/rules"><span class="glyphicon glyphicon-list"></span>List Forwarding Rules</a>
    </li>
</ul>

<h1><span class="glyphicon glyphicon-random"></span>Rule {{ rule.rule_id }}</h1>

<div class="container">
    <form method="POST" action="/rules/{{ rule.rule_id }}/edit">
        <div class="form-group">
            <label for="inputMatch">Rule</label>
            <input type="text" class="form-control" id="inputMatch" name="match" value="{{ rule.rule_match }}" />
        </div>
        <div class="form-group">
            <label for="inputDelay">Delay [sec]</label>
            <input type="number" class="form-control" id="inputDelay" name="delay" value="{{ rule.rule_delay }}" />
        </div>
        <div class="form-group">
            <label for="inputMaxforwardings">max forwarded active Alarms</label>
            <input type="number" class="form-control" id="inputMaxforwardings" name="maxforwardings" value="{{ rule.rule_maxforwardings }}" />
        </div>
        <div class="form-group">
            <label for="inputTarget">Target</label>
            <select class="form-control" name="target" id="inputTarget">
                {% for target in targets %}
                    <option{% if target.target_name==rule.rule_target %} selected="true"{% endif %}>{{ target.target_name }}</option>
                {% endfor %}
            </select>
        </div>
        <button type="submit" class="btn btn-primary">Save</button>
    </form>
</div>

{% include 'include/footer.html.tpl' %}
