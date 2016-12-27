{% include 'include/header.html.tpl' %}


<h1><span class="glyphicon glyphicon-user"></span>Change Password</h1>


<!-- password change form -->
<div class="container">
    <form method="POST" action="{{ baseurl }}/password-change">
        <div class="form-group">
            <label for="inputPasswordOld">Old Password</label>
            <input type="password" class="form-control" id="inputPasswordOld" name="password-old" />
        </div>
        <div class="form-group">
            <label for="inputPasswordNew">New Password</label>
            <input type="password" class="form-control" id="inputPasswordNew" name="password-new" />
        </div>
        <div class="form-group">
            <label for="inputPasswordNew2">Repeat new Password</label>
            <input type="password" class="form-control" id="inputPasswordNew2" name="password-new2" />
        </div>
        <button type="submit" class="btn btn-primary">Save</button>
    </form>
</div>

{% include 'include/footer.html.tpl' %}
