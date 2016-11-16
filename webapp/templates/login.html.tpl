{% include 'include/header.html.tpl' %}

<div id="custom-logincontainer">
    <div class="container">
        <div class="row">
            <div class="col-md-6 col-md-offset-3">
                <div class="panel panel-default" id="custom-loginpanel">
                    <div class="panel-heading">
                        <h3 class="panel-title">AlarmForwarder Login</h3>
                    </div>
                    <div class="panel-body">
                        {% include 'include/messagebar.html.tpl' %}
                        <img class="center-block" src="/static/images/logo.png" alt="AlarmForwarder Logo" />
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
                                <button type="submit" class="btn btn-primary col-xs-offset-1">Login</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

{% include 'include/footer.html.tpl' %}
