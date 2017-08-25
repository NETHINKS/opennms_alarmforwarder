<nav class="navbar navbar-fixed-top navbar-default">
    <div class="container">
        <div class="navbar-header">
            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar-collapse-1" aria-expanded="false">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>

                <a class="navbar-brand" href="{{ baseurl }}/">
                    <span class="nt-brand" data-char="AF"></span>AlarmForwarder
                </a>

        </div>

        <div class="collapse navbar-collapse navbar-right" id="navbar-collapse-1">
            <ul class="nav navbar-nav">
                <li class="{% if not current_path %} active{% endif %}"><a href="{{ baseurl }}/"><i class="fa fa-tachometer" aria-hidden="true"></i> Dashboard</a></li>

                <!-- Dropdown: forwarding configuration -->
                {% set forwarding_items = ["sources", "targets", "rules"] %}
                <li class="dropdown{% if current_path in forwarding_items %} active{% endif %}">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button">
                        <i class="fa fa-refresh" aria-hidden="true"></i> Forwarding <span class="caret"></span>
                    </a>
                    <ul class="dropdown-menu">
                        <li>
                            <a href="{{ baseurl }}/sources" ><i class="fa fa-sign-out" aria-hidden="true"></i> Sources</a>
                        </li>
                        <li>
                            <a href="{{ baseurl }}/targets"><i class="fa fa-sign-in" aria-hidden="true"></i> Targets</a>
                        </li>
                        <li>
                            <a href="{{ baseurl }}/rules"><i class="fa fa-random" aria-hidden="true"></i> Forwarding Rules</a>
                        </li>
                    </ul>
                </li>

                <!-- Dropdown: admin -->
                {% set admin_items = ["admin"] %}
                <li class="dropdown {% if current_path in admin_items %} active{% endif %}">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button">
                        <i class="fa fa-cog" aria-hidden="true"></i> Admin<span class="caret"></span>
                    </a>
                    <ul class="dropdown-menu">
                        <li><a href="{{ baseurl }}/admin/users"><i class="fa fa-user" aria-hidden="true"></i> Local Users</a></li>
                    </ul>
                </li>

                <!-- Dropdown: user menu -->
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button">
                        <i class="fa fa-user" aria-hidden="true"></i> User: {{ session.username }}<span class="caret"></span>
                    </a>
                    <ul class="dropdown-menu">
                        <li><a href="{{ baseurl }}/password-change"><i class="fa fa-exchange" aria-hidden="true"></i> Change Password</a></li>
                        <li><a href="{{ baseurl }}/logout"><i class="fa fa-times" aria-hidden="true"></i> Logout</a></li>
                    </ul>
                </li>
            </ul>
        </div>
    </div>
</nav>
