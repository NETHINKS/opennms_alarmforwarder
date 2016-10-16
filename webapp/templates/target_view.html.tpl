{% include 'include/header.html.tpl' %}

<h1>Target {{ target.target_name }}</h1>

<table>
    <tr>
        <td>class</td>
        <td>{{ target.target_class }}</td>
    </tr>
    {% for parameter in parameters %}
    <tr>
        <td>{{ parameter.parameter_name }}</td>
        <td>{{ parameter.parameter_value }}</td>
    </tr>
    {% endfor %}
</table>

{% include 'include/footer.html.tpl' %}
