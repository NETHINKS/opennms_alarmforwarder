{% include 'include/header.html.tpl' %}

<!-- page navigation -->
<ul class="nav nav-pills">
    <li role="presentation">
        <a href="{{ baseurl }}/targets"><span class="glyphicon glyphicon-list"></span>List Targets</a>
    </li>
    <li role="presentation"><a href="{{ baseurl }}/docs#_targets" target="_blank">
                                <span class="glyphicon glyphicon-question-sign"></span>Help
                            </a>
    </li>
</ul>

<h1><span class="glyphicon glyphicon-log-out"></span>Target {{ target.target_name }}</h1>

<div class="container">
    <form method="POST" action="{{ baseurl }}/targets/{{ target.target_name }}/edit">
        <div class="form-group">
            <label for="inputClass">Class</label>
            <input type="text" class="form-control" id="inputClass" name="class" value="{{ target.target_class }}" disabled="disabled" />
        </div>
        {% for parameter in target.target_parms %}
            <div class="form-group">
                <label for="input{{parameter.parameter_name}}">{{parameter.parameter_name}}</label>
                <input type="text" class="form-control" id="input{{parameter.parameter_name}}" 
                       name="{{parameter.parameter_name}}" value="{{ parameter.parameter_value }}" />
            </div>
        {% endfor %}
        <button type="submit" class="btn btn-primary">Save</button>
    </form>
</div>

{% include 'include/footer.html.tpl' %}
