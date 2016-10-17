{% include 'include/header.html.tpl' %}

<h1>Source {{ source.source_name }}</h1>

<form method="POST" action="/sources/{{ source.source_name }}/edit">
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
        <input type="text" class="form-control" id="inputPassword" name="password" value="{{ source.source_password }}" />
    </div>
    <div class="form-group">
        <label for="inputUrl">Filter</label>
        <input type="text" class="form-control" id="inputFilter" name="filter" value="{{ source.source_filter }}" />
    </div>
    <button type="submit" class="btn btn-default">Change</button>
</form>

{% include 'include/footer.html.tpl' %}
