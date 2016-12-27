{% include 'include/header.html.tpl' %}

<!-- page navigation -->
<ul class="nav nav-pills">
    <li role="presentation">
        <a href="{{ baseurl }}/admin/users"><span class="glyphicon glyphicon-list"></span>List Users</a>
    </li>
</ul>

<h1><span class="glyphicon glyphicon-user"></span>User {{ user.user_name }}</h1>

<div class="container">
    <form method="POST" action="{{ baseurl }}/admin/users/{{ user.user_name }}/edit">
        <div class="form-group">
            <label for="inputName">Name</label>
            <input type="text" class="form-control" id="inputName" name="name" value="{{ user.user_name }}" disabled="disabled" />
        </div>
        <div class="form-group">
            <label for="inputPassword">New Password</label>
            <input type="password" class="form-control" id="inputPassword" name="password" />
        </div>
        <button type="submit" class="btn btn-primary">Save</button>
    </form>
</div>

{% include 'include/footer.html.tpl' %}
