{% include 'include/header.html.tpl' %}

<!-- page navigation -->
<ul class="nav nav-pills">
    <li role="presentation"><a href="#" data-toggle="modal" data-target="#modalAddRule">
                                <span class="glyphicon glyphicon-plus"></span>Add Rule
                            </a>
    </li>
</ul>

<!-- modal: add new rule -->
<div class="modal fade" id="modalAddRule" role="dialog">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Add new Rule...</h4>
            </div>

            <div class="modal-body">
                <form method="POST" action="/rules/add">
                    <div class="form-group">
                        <label for="inputRule">Rule</label>
                        <input type="text" class="form-control" id="inputRule" name="rule" placeholder="alarm_uei~.*nodeDown.*">
                    </div>
                    <div class="form-group">
                        <label for="inputTarget">Target</label>
                        <select class="form-control" name="target" id="inputTarget">
                        {% for target in targets %}
                            <option>{{ target.target_name  }}</option>
                        {% endfor %}
                        </select>
                    </div>
                    <button type="submit" class="btn btn-primary">Submit</button>
                </form>
            </div>
        </div>
    </div>
</div>

<div class="container">
    <h1><span class="glyphicon glyphicon-random"></span>Forwarding Rules</h1>
    <table class="table table-default">
        <tr>
                <th>Rule</th>
                <th>Target</th>
                <th>Action</th>
        </tr>
        {% for rule in rules %}
            <tr>
                <td>{{ rule.rule_match }}</td>
                <td>{{ rule.rule_target }}</td>
                <td>
                    <a href="/rules/{{ rule.rule_id }}"><span class="glyphicon glyphicon-edit"></span></a>
                    <a href="/rules/{{ rule.rule_id }}/delete"><span class="glyphicon glyphicon-remove"></span></a>
                </td>
            </tr>
        {% endfor %}
    </table>
</div>

{% include 'include/footer.html.tpl' %}
