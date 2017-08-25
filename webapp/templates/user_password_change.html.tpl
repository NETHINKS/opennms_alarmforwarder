{% include 'include/header.html.tpl' %}


<h1 class="page-header"><i class="fa fa-exchange" aria-hidden="true"></i> Change Password</h1>


<!-- password change form -->
    <form method="POST" action="{{ baseurl }}/password-change">
        <div class="form-group">
            <label for="inputPasswordOld">Old Password</label>
            <input type="password" data-toggle="password" data-placement="before" class="form-control" id="inputPasswordOld" name="password-old" />
        </div>
        <div class="form-group">
            <label for="inputPasswordNew">New Password</label>
            <input type="password" data-toggle="password" data-placement="before" class="form-control" id="inputPasswordNew" name="password-new" />
        </div>
        <div class="form-group">
            <label for="inputPasswordNew2">Repeat new Password</label>
            <input type="password" data-toggle="password" data-placement="before" class="form-control" id="inputPasswordNew2" name="password-new2" />
        </div>
        <button type="submit" class="btn btn-primary">Save</button>
        <button type="reset" class="btn btn-default">Reset</button>
    </form>

{% include 'include/footer.html.tpl' %}
