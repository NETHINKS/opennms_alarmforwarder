{% include 'include/header.html.tpl' %}

<!-- page navigation -->
<ul class="breadcrumb pull-right">
    <li><a href="#" data-toggle="modal" data-target="#modalAddSource">
                                <i class="fa fa-plus-circle" aria-hidden="true"></i> Add Source
                            </a>
    </li>
    <li>
        <a href="{{ baseurl }}/docs#_sources" target="_blank">
            <i class="fa fa-question-circle" aria-hidden="true"></i> Help
        </a>
    </li>
</ul>


<!-- modal: add new target -->
<div class="modal fade" id="modalAddSource" tabindex="-1" role="dialog">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Add new Source...</h4>
            </div>

            <div class="modal-body">
                <form method="POST" action="{{ baseurl }}/sources/add">
                    <div class="form-group">
                        <label for="inputName">Name</label>
                        <input type="text" class="form-control" id="inputName" name="name" placeholder="Name">
                    </div>
                    <div class="form-group">
                        <label for="inputUrl">URL</label>
                        <input type="text" class="form-control" id="inputUrl" name="url" placeholder="http://demo.opennms.org/opennms/rest">
                    </div>
                    <div class="form-group">
                        <label for="inputUser">Username</label>
                        <input type="text" class="form-control" id="inputUser" name="user" placeholder="admin">
                    </div>
                    <div class="form-group">
                        <label for="inputPassword">Password</label>
                        <input type="password" data-toggle="password" class="form-control" id="inputPassword" name="password" placeholder="admin">
                    </div>
                    <div class="form-group">
                        <label for="inputFilter">Filter</label>
                        <input type="text" class="form-control" id="inputFilter" name="filter" placeholder="alarmAckUser=NULL&stickyMemo=NULL&severity=CLEARED&comperator=gt">
                    </div>
                    <button type="submit" class="btn btn-primary">Submit</button>
                    <button type="reset" class="btn btn-default">Reset</button>
                </form>
            </div>
        </div>
    </div>
</div>


<!-- table with all sources -->
    <h1 class="page-header"><i class="fa fa-sign-out" aria-hidden="true"></i> Sources</h1>
    <table class="table table-default table-striped table-hover">
        <tr>
                <th>Status</th>
                <th>Name</th>
                <th>URL</th>
                <th>Username</th>
                <th>Filter</th>
                <th>Action</th>
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
                    <td><i class="fa fa-question-circle" aria-hidden="true"></i></td>
            {% endif %}
                    <td>{{ source.source_name }}</td>
                    <td><a href="{{ source.source_url }}" target="_blank">{{ source.source_url }}</a></td>
                    <td>{{ source.source_user }}</td>
                    <td>{{ source.source_filter }}</td>
                    <td>
                        <a href="{{ baseurl }}/sources/{{ source.source_name }}/test" title="test source"><i class="fa fa-check-square" aria-hidden="true"></i></a>
                        <a href="{{ baseurl }}/sources/{{ source.source_name }}" title="edit source"><i class="fa fa-pencil-square" aria-hidden="true"></i></a>
                        <a href="{{ baseurl }}/sources/{{ source.source_name }}/delete" title="delete source"><i class="fa fa-times" aria-hidden="true"></i></a>
                    </td>
                </tr>
        {% endfor %}

    </table>

{% include 'include/footer.html.tpl' %}
