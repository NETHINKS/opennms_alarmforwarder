{% include 'include/header.html.tpl' %}

<h1>Login</h1>

<form method="post" action="/login" class="form-horizontal">
    <!-- login form field: username -->
    <div class="form-group">
        <div class="input-group col-xs-10 col-xs-offset-1">
            <div class="input-group-addon"><span class="glyphicon glyphicon-user" aria-hidden="true"></span></div>
            <input type="text" class="form-control" placeholder="username" name="username"/>
        </div>
    </div>
    <!-- login form field: password -->
    <div class="form-group">
        <div class="input-group col-xs-10 col-xs-offset-1">
            <div class="input-group-addon"><span class="glyphicon glyphicon-option-horizontal" aria-hidden="true"></span></div>
            <input type="password" class="form-control" placeholder="password" name="password"/>
        </div>
    </div>
    <!-- login form: login button -->
    <div class="form-group">
        <button type="submit" class="btn btn-default col-xs-offset-1">Login</button>
    </div>
</form>

{% include 'include/footer.html.tpl' %}
