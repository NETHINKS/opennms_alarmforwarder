{% include 'include/header.html.tpl' %}

<h1>Target {{ target.target_name }}</h1>

<form method="POST" action="/targets/{{ target.target_name }}/edit">
    <div class="form-group">
        <label for="inputClass">Class</label>
        <input type="text" class="form-control" id="inputClass" name="class" value="{{ target.target_class }}" disabled="disabled" />
    </div>
    {% for parameter in parameters %}
        <div class="form-group">
            <label for="input{{parameter.parameter_name}}">{{parameter.parameter_name}}</label>
            <input type="text" class="form-control" id="input{{parameter.parameter_name}}" 
                   name="{{parameter.parameter_name}}" value="{{ parameter.parameter_value }}" />
        </div>
    {% endfor %}
    <button type="submit" class="btn btn-default">Change</button>
</form>

{% include 'include/footer.html.tpl' %}
