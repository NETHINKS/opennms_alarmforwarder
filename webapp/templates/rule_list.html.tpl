{% include 'include/header.html.tpl' %}

<!-- page navigation -->
<ul class="breadcrumb pull-right">
    <li role="presentation"><a href="#" data-toggle="modal" data-target="#modalAddRule">
                                <i class="fa fa-plus-circle" aria-hidden="true"></i> Add Rule
                            </a>
    </li>
    <li role="presentation"><a href="{{ baseurl }}/docs#_forwarding_rules" target="_blank">
                                <i class="fa fa-question-circle" aria-hidden="true"></i> Help
                            </a>
    </li>
</ul>

<!-- modal: add new rule -->
<div class="modal fade" id="modalAddRule" tabindex="-1" role="dialog">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Add new Rule...</h4>
            </div>

            <div class="modal-body">
                <form method="POST" action="{{ baseurl }}/rules/add">
                    <div class="form-group">
                        <label for="inputRule">Rule</label>
                        <input type="text" class="form-control" id="inputRule" name="rule" placeholder="alarm_uei~.*nodeDown.*">
                    </div>
                    <div class="form-group">
                        <label for="inputDelay">Delay [sec]</label>
                        <input type="number" class="form-control" id="inputDelay" name="delay" value="0">
                    </div>
                    <div class="form-group">
                        <label for="inputMaxforwardings">max forwarded active Alarms</label>
                        <input type="number" class="form-control" id="inputMaxForwardings" name="maxforwardings" value="0">
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
                    <button type="reset" class="btn btn-default">Reset</button>
                </form>
            </div>
        </div>
    </div>
</div>

    <h1 class="page-header"><i class="fa fa-random" aria-hidden="true"></i> Forwarding Rules</h1>
    <table class="table table-default table-striped table-hover">
        <tr>
                <th>Rule</th>
                <th>Delay [sec]</th>
                <th>max forwarded active Alarms</th>
                <th>Target</th>
                <th>Action</th>
        </tr>
        {% for rule in rules %}
            <tr>
                <td>{{ rule.rule_match }}</td>
                <td>{{ rule.rule_delay }}</td>
                <td>{{ rule.rule_maxforwardings }}</td>
                <td>{{ rule.rule_target }}</td>
                <td>
                    <a href="{{ baseurl }}/rules/{{ rule.rule_id }}" title="edit rule"><i class="fa fa-pencil-square" aria-hidden="true"></i></span></a>
                    <a href="{{ baseurl }}/rules/{{ rule.rule_id }}/delete" title="delete rule"><i class="fa fa-times" aria-hidden="true"></i></a>
                </td>
            </tr>
        {% endfor %}
    </table>

{% include 'include/footer.html.tpl' %}
