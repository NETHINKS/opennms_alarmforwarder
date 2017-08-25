{% include 'include/header.html.tpl' %}

<!-- page navigation -->
<ul class="breadcrumb pull-right">
    <li role="presentation">
        <a href="{{ baseurl }}/sources"><i class="fa fa-list" aria-hidden="true"></i> List Sources</a>
    </li>
    <li role="presentation"><a href="{{ baseurl }}/docs#_sources" target="_blank">
                                <i class="fa fa-question-circle" aria-hidden="true"></i> Help
                            </a>
    </li>
</ul>


<h1 class="page-header"><i class="fa fa-sign-out" aria-hidden="true"></i> Source: <small>{{ source.source_name }}</small></h1>

    <form method="POST" action="{{ baseurl }}/sources/{{ source.source_name }}/edit">
        <div class="form-group">
            <label for="inputUrl">URL</label>
            <input type="text" class="form-control" id="inputUrl" name="url" value="{{ source.source_url }}" />
        </div>
        <div class="form-group">
            <label for="inputUrl">User</label>
            <input type="text" class="form-control" id="inputUser" name="user" value="{{ source.source_user }}" />
        </div>
        <div class="form-group">
            <label for="inputUrl">Password</label>
            <input type="password" data-toggle="password" class="form-control" id="inputPassword" name="password" value="{{ source.source_password }}" />
        </div>
        <div class="form-group">
            <label for="inputUrl">Filter</label>
            <input type="text" class="form-control" id="inputFilter" name="filter" value="{{ source.source_filter }}" />
        </div>
        <button type="submit" class="btn btn-primary">Save</button>
        <button type="reset" class="btn btn-default">Reset</button>
    </form>


{% include 'include/footer.html.tpl' %}
