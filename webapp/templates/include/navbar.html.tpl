<nav class="navbar navbar-inverse">
    <div class="container-fluid">
        <div class="navbar-header">
            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar-collapse-1" aria-expanded="false">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <h1>
                <a class="navbar-brand" href="/">
                    <img src="/static/images/logo-small.png" alt="AlarmForwarder Logo" />
                    AlarmForwarder
                </a>
            </h1>
        </div>

        <div class="collapse navbar-collapse navbar-right" id="navbar-collapse-1">
            <ul class="nav navbar-nav">
                <li><a href="/"><span class="glyphicon glyphicon-dashboard"></span>Overview</a></li>

                <!-- Dropdown: forwarding configuration -->
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button">
                        <span class="glyphicon glyphicon-log-out"></span>Forwarding Configuration<span class="caret"></span>
                    </a>
                    <ul class="dropdown-menu">
                        <li><a href="/sources"><span class="glyphicon glyphicon-log-in"></span>Sources</a></li>
                        <li><a href="/targets"><span class="glyphicon glyphicon-log-out"></span>Targets</a></li>
                        <li><a href="/rules"><span class="glyphicon glyphicon-random"></span>Forwarding Rules</a></li>
                    </ul>
                </li>

                <!-- Dropdown: admin -->
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button">
                        <span class="glyphicon glyphicon-wrench"></span>Admin<span class="caret"></span>
                    </a>
                    <ul class="dropdown-menu">
                        <li><a href="/admin/users"><span class="glyphicon glyphicon-user"></span>Local Users</a></li>
                    </ul>
                </li>

                <!-- Dropdown: help menu -->
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button">
                        <span class="glyphicon glyphicon-question-sign"></span>Help<span class="caret"></span>
                    </a>
                    <ul class="dropdown-menu">
                        <li><a href="/docs" target="_blank"><span class="glyphicon glyphicon-book"></span>Documentation</a></li>
                        <li><a href="https://github.com/NETHINKS/opennms_alarmforwarder" target="_blank"><span class="glyphicon glyphicon-globe"></span>GitHub Project</a></li>
                    </ul>
                </li>

                <!-- Dropdown: user menu -->
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button">
                        <span class="glyphicon glyphicon-user"></span>User: {{ session.username }}<span class="caret"></span>
                    </a>
                    <ul class="dropdown-menu">
                        <li><a href="/password-change"><span class="glyphicon glyphicon-cog"></span>Change Password</a></li>
                        <li><a href="/logout"><span class="glyphicon glyphicon-off"></span>Logout</a></li>
                    </ul>
                </li>
            </ul>
        </div>
    </div>
</nav>

