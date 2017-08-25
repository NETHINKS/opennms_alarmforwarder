{% include 'include/header.html.tpl' %}

<!-- page navigation -->
<ul class="breadcrumb pull-right">
    <li role="presentation">
        <a href="{{ baseurl }}/rules"><i class="fa fa-list" aria-hidden="true"></i> List Forwarding Rules</a>
    </li>
    <li role="presentation"><a href="{{ baseurl }}/docs#_forwarding_rules" target="_blank">
                                <i class="fa fa-question-circle" aria-hidden="true"></i> Help
                            </a>
    </li>
</ul>

<h1 class="page-header"><i class="fa fa-random" aria-hidden="true"></i> Rule: {{ rule.rule_id }}</h1>

    <form method="POST" action="{{ baseurl }}/rules/{{ rule.rule_id }}/edit">
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
        <button type="reset" class="btn btn-default">Reset</button>
    </form>

{% include 'include/footer.html.tpl' %}
