{% include 'include/header.html.tpl' %}

<!-- page navigation -->
<ul class="breadcrumb pull-right">
    <li role="presentation">
        <a href="{{ baseurl }}/targets"><span class="glyphicon glyphicon-list"></span>List Targets</a>
    </li>
    <li role="presentation"><a href="{{ baseurl }}/docs#_targets" target="_blank">
                                <span class="glyphicon glyphicon-question-sign"></span>Help
                            </a>
    </li>
</ul>

<h1 class="page-header"><i class="fa fa-sign-in" aria-hidden="true"></i> Target: <small>{{ target.target_name }}</small></h1>

    <form id="target_view_form" method="POST" action="{{ baseurl }}/targets/{{ target.target_name }}/edit">
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
        <button form="target_view_form" type="reset" class="btn btn-default">Reset</button>
    </form>

{% include 'include/footer.html.tpl' %}
