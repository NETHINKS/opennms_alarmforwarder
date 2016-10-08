{% include 'include/header.html.tpl' %}

<h1>Targets</h1>

<table class="table table-default">
    {% for target in targets %}
        <tr>
            <td>{{ target.target_name }}</td>
            <td>{{ target.target_class }}</td>
            <td><a href="/targets/{{ target.target_name }}"><span class="glyphicon glyphicon-eye-open"></span></a></td>
        </tr>
    {% endfor %}

</table>

{% include 'include/footer.html.tpl' %}
