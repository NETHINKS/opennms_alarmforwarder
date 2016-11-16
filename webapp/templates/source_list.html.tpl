{% include 'include/header.html.tpl' %}

<!-- page navigation -->
<ul class="nav nav-pills">
    <li role="presentation"><a href="#" data-toggle="modal" data-target="#modalAddSource">
                                <span class="glyphicon glyphicon-plus"></span>Add Source
                            </a>
    </li>
</ul>



<!-- modal: add new target -->
<div class="modal fade" id="modalAddSource" role="dialog">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Add new Source...</h4>
            </div>

            <div class="modal-body">
                <form method="POST" action="/sources/add">
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
                        <input type="text" class="form-control" id="inputPassword" name="password" placeholder="admin">
                    </div>
                    <div class="form-group">
                        <label for="inputFilter">Filter</label>
                        <input type="text" class="form-control" id="inputFilter" name="filter" placeholder="alarmAckUser IS NULL AND stickyMemo is NULL">
                    </div>
                    <button type="submit" class="btn btn-primary">Submit</button>
                </form>
            </div>
        </div>
    </div>
</div>


<!-- table with all sources -->
<div class="container">
    <h1><span class="glyphicon glyphicon-log-in"></span>Sources</h1>
    <table class="table table-default">
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
                    <td><span class="glyphicon glyphicon-remove-sign"></span></td>
            {% elif source.source_status == 1 %}
                <tr class="success">
                    <td><span class="glyphicon glyphicon-ok-sign"></span></td>
            {% else %}
                <tr>
                    <td><span class="glyphicon glyphicon-question-sign"></span></td>
            {% endif %}
                    <td>{{ source.source_name }}</td>
                    <td>{{ source.source_url }}</td>
                    <td>{{ source.source_user }}</td>
                    <td>{{ source.source_filter }}</td>
                    <td>
                        <a href="/sources/{{ source.source_name }}/test"><span class="glyphicon glyphicon-ok"></span></a>
                        <a href="/sources/{{ source.source_name }}"><span class="glyphicon glyphicon-edit"></span></a>
                        <a href="/sources/{{ source.source_name }}/delete"><span class="glyphicon glyphicon-remove"></span></a>
                    </td>
                </tr>
        {% endfor %}

    </table>
</div>

{% include 'include/footer.html.tpl' %}
