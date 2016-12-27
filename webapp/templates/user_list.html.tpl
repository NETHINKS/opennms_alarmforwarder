{% include 'include/header.html.tpl' %}

<!-- page navigation -->
<ul class="nav nav-pills">
    <li role="presentation"><a href="#" data-toggle="modal" data-target="#modalAddUser">
                                <span class="glyphicon glyphicon-plus"></span>Add User
                            </a>
    </li>
</ul>


<h1><span class="glyphicon glyphicon-user"></span>Local Users</h1>

<!-- modal: add new user -->
<div class="modal fade" id="modalAddUser" tabindex="-1" role="dialog">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Add new User...</h4>
            </div>

            <div class="modal-body">
                <form method="POST" action="{{ baseurl }}/admin/users/add">
                    <div class="form-group">
                        <label for="inputName">Username</label>
                        <input type="text" class="form-control" id="inputName" name="name" placeholder="Name">
                    </div>
                    <div class="form-group">
                        <label for="inputPassword">Password</label>
                        <input type="password" class="form-control" id="inputPassword" name="password" placeholder="secret1234">
                    </div>
                    <button type="submit" class="btn btn-primary">Submit</button>
                </form>
            </div>
        </div>
    </div>
</div>


<!-- table with all users -->
<div class="container">
    <table class="table table-default">
        <tr>
                <th>Username</th>
                <th>Action</th>
        </tr>

        {% for user in users %}
                <tr>
                    <td>{{ user.user_name }}</td>
                    <td>
                        <a href="{{ baseurl }}/admin/users/{{ user.user_name }}" title="edit user"><span class="glyphicon glyphicon-edit"></span></a>
                        <a href="{{ baseurl }}/admin/users/{{ user.user_name }}/delete" title="delete user"><span class="glyphicon glyphicon-remove"></span></a>
                    </td>
                </tr>
        {% endfor %}

    </table>
</div>

{% include 'include/footer.html.tpl' %}
