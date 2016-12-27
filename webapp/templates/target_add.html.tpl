{% include 'include/header.html.tpl' %}

<h1>Add new target</h1>

<div class="container">
    <form method="POST" action="{{ baseurl }}/targets/add">
        <input type="hidden" name="action" value="add">
        <div class="form-group">
            <label for="inputName">Name</label>
            <input type="text" class="form-control" id="inputName" name="name" value="{{ target_name }}">
        </div>
        <div class="form-group">
            <label for="inputClass">Class</label>
            <input type="text" class="form-control" id="inputClass" name="class" value="{{ target_class }}">
        </div>
        {% for parm_name in target_parameters %}
        <div class="form-group">
            <label for="input{{ parm_name }}">{{ parm_name }}</label>
            <input type="text" class="form-control" id="input{{ parm_name }}" name="{{ parm_name }}" value="{{ target_parameters[parm_name] }}">
        </div>
        {% endfor %}
        <button type="submit" class="btn btn-default">Submit</button>
    </form>
</div>

{% include 'include/footer.html.tpl' %}
