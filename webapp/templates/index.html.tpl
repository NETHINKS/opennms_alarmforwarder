{% include 'include/header.html.tpl' %}

<h1>Dashboard</h1>

<div class="container">
    <h2><span class="glyphicon glyphicon-log-in"></span>Sources</h2>
    <table class="table table-default">
        <tr>
                <th>Status</th>
                <th>Name</th>
                <th>URL</th>
                <th>Username</th>
                <th>Filter</th>
        </tr>

        {% for source in sources %}
            {% if source.source_status == 2 %}
                <tr class="danger">
                    <td><span class="glyphicon glyphicon-remove-sign"></span></td>
            {% elif source.source_status == 1 %}
                <tr class="success">
                    <td><span class="glyphicon glyphicon-ok-sign"></span></td>
            {% else %}
                <tr>
                    <td><span class="glyphicon glyphicon-question-sign"></span></td>
            {% endif %}
                    <td>{{ source.source_name }}</td>
                    <td>{{ source.source_url }}</td>
                    <td>{{ source.source_user }}</td>
                    <td>{{ source.source_filter }}</td>
                </tr>
        {% endfor %}
    </table>

    <h2><span class="glyphicon glyphicon-random"></span>Forwarding Rules</h2>
    <table class="table table-default">
        <tr>
                <th>Rule</th>
                <th>Delay [sec]</th>
                <th>max forwarded active Alarms</th>
                <th>Target</th>
        </tr>
        {% for rule in rules %}
            <tr>
                <td>{{ rule.rule_match }}</td>
                <td>{{ rule.rule_delay }}</td>
                <td>{{ rule.rule_maxforwardings }}</td>
                <td>{{ rule.rule_target }}</td>
            </tr>
        {% endfor %}
    </table>

</div>

{% include 'include/footer.html.tpl' %}
