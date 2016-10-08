<h1>Targets</h1>

<table>
    {% for target in targets %}
        <tr>
            <td>{{ target.target_name }}</td>
            <td>{{ target.target_class }}</td>
        </tr>
    {% endfor %}

</table>
