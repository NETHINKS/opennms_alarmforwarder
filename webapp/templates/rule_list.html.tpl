{% include 'include/header.html.tpl' %}

<ul class="nav nav-pills">
    <li role="presentation"><a href="/rules/add">Add new Rule</a></li>
</ul>

<h1>Forwarding Rules</h1>

<table class="table table-default">
    <tr>
            <th>Rule</th>
            <th>Target</th>
            <th>Action</th>
    </tr>
    {% for rule in rules %}
        <tr>
            <td>{{ rule.rule_match }}</td>
            <td>{{ rule.rule_target }}</td>
            <td><a href="/rules/{{ rule.rule_id }}/delete"><span class="glyphicon glyphicon-remove"></span></a></td>
        </tr>
    {% endfor %}

</table>

{% include 'include/footer.html.tpl' %}
