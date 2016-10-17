{% include 'include/header.html.tpl' %}

<h1>Rule {{ rule.rule_id }}</h1>

<form method="POST" action="/rules/{{ rule.rule_id }}/edit">
    <div class="form-group">
        <label for="inputMatch">Rule</label>
        <input type="text" class="form-control" id="inputMatch" name="match" value="{{ rule.rule_match }}" />
    </div>
    <div class="form-group">
        <label for="inputTarget">Target</label>
        <select class="form-control" name="target" id="inputTarget">
            {% for target in targets %}
                <option{% if target.target_name==rule.rule_target %} selected="true"{% endif %}>{{ target.target_name }}</option>
            {% endfor %}
        </select>
    </div>
    <button type="submit" class="btn btn-default">Change</button>
</form>

{% include 'include/footer.html.tpl' %}
