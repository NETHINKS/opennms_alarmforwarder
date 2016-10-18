{% include 'include/header.html.tpl' %}

<!-- page navigation -->
<ul class="nav nav-pills">
    <li role="presentation">
        <button type="button" class="btn btn-primary btn-lg" data-toggle="modal" data-target="#modalAddTarget">
            Add new Target...
        </button>
    </li>
</ul>


<h1>Targets</h1>

<!-- modal: add new target -->
<div class="modal fade" id="modalAddTarget" role="dialog">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Add new target...</h4>
            </div>

            <div class="modal-body">
                <form method="POST" action="/targets/add">
                    <input type="hidden" name="action" value="show_form">
                    <div class="form-group">
                        <label for="inputName">Target Name</label>
                        <input type="text" class="form-control" id="inputName" name="name" placeholder="Name">
                    </div>
                    <div class="form-group">
                        <label for="inputClass">Forwarding Class</label>
                        <select class="form-control" name="class" id="inputClass">
                        {% for forwarder_class in forwarder_classes %}
                            <option>{{ forwarder_class  }}</option>
                        {% endfor %}
                        </select>
                    </div>
                    <button type="submit" class="btn btn-default">Submit</button>
                </form>
            </div>
        </div>
    </div>
</div>


<!-- table with all targets -->
<table class="table table-default">
    <tr>
            <th>Name</th>
            <th>Class</th>
            <th>Action</th>
    </tr>
    {% for target in targets %}
        <tr>
            <td>{{ target.target_name }}</td>
            <td>{{ target.target_class }}</td>
            <td>
                <a href="/targets/{{ target.target_name }}/test"><span class="glyphicon glyphicon-ok"></span></a>
                <a href="/targets/{{ target.target_name }}"><span class="glyphicon glyphicon-edit"></span></a>
                <a href="/targets/{{ target.target_name }}/delete"><span class="glyphicon glyphicon-remove"></span></a>
            </td>
        </tr>
    {% endfor %}

</table>

{% include 'include/footer.html.tpl' %}
