{% include 'include/header.html.tpl' %}

<!-- page navigation -->
<ul class="breadcrumb pull-right">
    <li role="presentation"><a href="#" data-toggle="modal" data-target="#modalAddUser">
                                <i class="fa fa-plus-circle" aria-hidden="true"></i> Add User
                            </a>
    </li>
</ul>



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
                        <input type="password" data-toggle="password" class="form-control" id="inputPassword" name="password" placeholder="secret1234">
                    </div>
                    <button type="submit" class="btn btn-primary">Submit</button>
                    <button type="reset" class="btn btn-default">Reset</button>
                </form>
            </div>
        </div>
    </div>
</div>


<h1 class="page-header"><i class="fa fa-user" aria-hidden="true"></i> Local Users</h1>
<!-- table with all users -->
    <table class="table table-default table-striped table-hover">
        <tr>
                <th>Username</th>
                <th>Action</th>
        </tr>

        {% for user in users %}
                <tr>
                    <td>{{ user.user_name }}</td>
                    <td>
                        <a href="{{ baseurl }}/admin/users/{{ user.user_name }}" title="edit user"><i class="fa fa-pencil-square" aria-hidden="true"></i></a>
                        <a href="{{ baseurl }}/admin/users/{{ user.user_name }}delete" title="delete user"><i class="fa fa-times" aria-hidden="true"></i></a>
                    </td>
                </tr>
        {% endfor %}

    </table>

{% include 'include/footer.html.tpl' %}
