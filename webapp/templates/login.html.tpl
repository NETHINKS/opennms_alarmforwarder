{% include 'include/header.html.tpl' %}

<div id="custom-logincontainer" class="container">
        <div class="row">
            <div class="col-md-6 col-md-offset-3">
                <div class="panel panel-default" id="custom-loginpanel">
                    <div class="panel-heading">
                        <h3 class="panel-title">AlarmForwarder Login</h3>
                    </div>
                    <div class="panel-body">
                    <img class="center-block" src="{{ baseurl }}/static/img/logo.png" alt="AlarmForwarder Logo" />
                        {% include 'include/messagebar.html.tpl' %}

                        <form method="post" action="{{ baseurl }}/login" class="form-horizontal">
                            <!-- login form field: username -->
                            <div class="form-group">
                                <div class="input-group col-xs-10 col-xs-offset-1">
                                    <div class="input-group-addon"><i class="fa fa-user" aria-hidden="true"></i></div>
                                    <input type="text" class="form-control" placeholder="username" name="username"/>
                                </div>
                            </div>
                            <!-- login form field: password -->
                            <div class="form-group">
                                <div class="input-group col-xs-10 col-xs-offset-1">
                                    <div class="input-group-addon"><i class="fa fa-lock" aria-hidden="true"></i></div>
                                    <input type="password" data-toggle="password" class="form-control" placeholder="password" name="password"/>
                                </div>
                            </div>
                            <!-- login form: login button -->
                            <div class="form-group">
                                <div class="input-group col-xs-10 col-xs-offset-1">
                                <button type="submit" class="btn btn-primary btn-block">Login</button>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
</div>

{% include 'include/footer.html.tpl' %}
