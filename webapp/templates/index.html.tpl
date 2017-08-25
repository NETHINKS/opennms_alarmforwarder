{% include 'include/header.html.tpl' %}

    <h1 class="page-header">Dashboard</h1>
    <h2><i class="fa fa-sign-out" aria-hidden="true"></i> Sources</h2>
    <table class="table table-default table-striped table-hover">
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
                    <td><i class="fa fa-ban" aria-hidden="true"></i></td>
            {% elif source.source_status == 1 %}
                <tr class="success">
                    <td><i class="fa fa-check-circle" aria-hidden="true"></i></td>
            {% else %}
                <tr>
                    <td><span class="glyphicon glyphicon-question-sign"></span></td>
            {% endif %}
                    <td>{{ source.source_name }}</td>
                    <td><a href="{{ source.source_url }}" target="_blank">{{ source.source_url }}</a></td>
                    <td>{{ source.source_user }}</td>
                    <td>{{ source.source_filter }}</td>
                </tr>
        {% endfor %}
    </table>

    <h2><i class="fa fa-random" aria-hidden="true"></i> Forwarding Rules</h2>
    <table class="table table-default table-striped table-hover">
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


{% include 'include/footer.html.tpl' %}
