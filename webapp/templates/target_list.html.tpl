{% include 'include/header.html.tpl' %}

<!-- page navigation -->
<ul class="breadcrumb pull-right">
    <li role="presentation"><a href="#" data-toggle="modal" data-target="#modalAddTarget">
                                <i class="fa fa-plus-circle" aria-hidden="true"></i> Add Target
                            </a>
    </li>
    <li role="presentation"><a href="{{ baseurl }}/docs#_targets" target="_blank">
                                <i class="fa fa-question-circle" aria-hidden="true"></i> Help
                            </a>
    </li>
</ul>


<h1 class="page-header"><i class="fa fa-sign-in" aria-hidden="true"></i> Targets</h1>

<!-- modal: add new target -->
<div class="modal fade" id="modalAddTarget" tabindex="-1" role="dialog">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Add new target...</h4>
            </div>

            <div class="modal-body">
                <form method="POST" action="{{ baseurl }}/targets/add">
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
                    <button type="submit" class="btn btn-primary">Submit</button>
                    <button type="reset" class="btn btn-default">Reset</button>
                </form>
            </div>
        </div>
    </div>
</div>


<!-- table with all targets -->
    <table class="table table-default table-striped table-hover">
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
                    <a href="{{ baseurl }}/targets/{{ target.target_name }}/test" title="test target"><i class="fa fa-check-square" aria-hidden="true"></i></a>
                    <a href="{{ baseurl }}/targets/{{ target.target_name }}" title="edit target"><i class="fa fa-pencil-square" aria-hidden="true"></i></a>
                    <a href="{{ baseurl }}/targets/{{ target.target_name }}/delete" title="delete target"><i class="fa fa-times" aria-hidden="true"></i></a>
                </td>
            </tr>
        {% endfor %}

    </table>

{% include 'include/footer.html.tpl' %}
