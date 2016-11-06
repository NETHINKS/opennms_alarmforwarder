{% include 'include/header.html.tpl' %}

<!-- page navigation -->
<ul class="nav nav-pills">
    <li role="presentation">
        <button type="button" class="btn btn-primary btn-lg" data-toggle="modal" data-target="#modalAddUser">
            Add new User...
        </button>
    </li>
</ul>


<h1><span class="glyphicon glyphicon-user"></span>Local Users</h1>

<!-- modal: add new user -->
<div class="modal fade" id="modalAddUser" role="dialog">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Add new User...</h4>
            </div>

            <div class="modal-body">
                <form method="POST" action="/admin/users/add">
                    <div class="form-group">
                        <label for="inputName">Username</label>
                        <input type="text" class="form-control" id="inputName" name="name" placeholder="Name">
                    </div>
                    <div class="form-group">
                        <label for="inputPassword">Password</label>
                        <input type="password" class="form-control" id="inputPassword" name="password" placeholder="secret1234">
                    </div>
                    <button type="submit" class="btn btn-default">Submit</button>
                </form>
            </div>
        </div>
    </div>
</div>


<!-- table with all users -->
<table class="table table-default">
    <tr>
            <th>Username</th>
            <th>Action</th>
    </tr>

    {% for user in users %}
            <tr>
                <td>{{ user.user_name }}</td>
                <td>
                    <a href="/admin/users/{{ user.user_name }}/delete"><span class="glyphicon glyphicon-remove"></span></a>
                </td>
            </tr>
    {% endfor %}

</table>

{% include 'include/footer.html.tpl' %}
