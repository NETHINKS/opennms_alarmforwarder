{% include 'include/header.html.tpl' %}

<!-- page navigation -->
<ul class="nav nav-pills">
    <li role="presentation">
        <button type="button" class="btn btn-primary btn-lg" data-toggle="modal" data-target="#modalAddSource">
            Add new Source...
        </button>
    </li>
</ul>


<h1>Sources</h1>

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
                        <input type="text" class="form-control" id="inputFilter" name="filter" placeholder="">
                    </div>
                    <button type="submit" class="btn btn-default">Submit</button>
                </form>
            </div>
        </div>
    </div>
</div>


<!-- table with all sources -->
<table class="table table-default">
    <tr>
            <th>Name</th>
            <th>URL</th>
            <th>Username</th>
            <th>Filter</th>
            <th>Action</th>
    </tr>

    {% for source in sources %}
        <tr>
            <td>{{ source.source_name }}</td>
            <td>{{ source.source_url }}</td>
            <td>{{ source.source_user }}</td>
            <td>{{ source.source_filter }}</td>
            <td>
                <a href="/sources/{{ source.source_name }}/delete"><span class="glyphicon glyphicon-remove"></span></a>
            </td>
        </tr>
    {% endfor %}

</table>

{% include 'include/footer.html.tpl' %}
