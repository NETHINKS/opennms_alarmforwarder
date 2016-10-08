{% include 'include/header.html.tpl' %}

<h1>Forwarding Rules</h1>

<table class="table table-default">
    <th>
        <tr>
            <td>Rule</td>
            <td>Target</td>
        </tr>
    </th>
    {% for rule in rules %}
        <tr>
            <td>{{ rule.rule_match }}</td>
            <td>{{ rule.rule_target }}</td>
        </tr>
    {% endfor %}

</table>

{% include 'include/footer.html.tpl' %}
