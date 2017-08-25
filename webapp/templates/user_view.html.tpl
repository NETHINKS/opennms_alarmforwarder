{% include 'include/header.html.tpl' %}

<!-- page navigation -->
<ul class="breadcrumb pull-right">
    <li role="presentation">
        <a href="{{ baseurl }}/admin/users"><i class="fa fa-list" aria-hidden="true"></i> List Users</a>
    </li>
</ul>

<h1><i class="fa fa-user" aria-hidden="true"></i> User: <small>{{ user.user_name }}</small></h1>

    <form method="POST" action="{{ baseurl }}/admin/users/{{ user.user_name }}/edit">
        <div class="form-group">
            <label for="inputName">Name</label>
            <input type="text" class="form-control" id="inputName" name="name" value="{{ user.user_name }}" disabled="disabled" />
        </div>
        <div class="form-group">
            <label for="inputPassword">New Password</label>
            <input type="password" class="form-control" id="inputPassword" name="password" data-toggle="password"/>
        </div>
        <button type="submit" class="btn btn-primary">Save</button>
        <button type="reset" class="btn btn-default">Reset</button>
    </form>

{% include 'include/footer.html.tpl' %}
