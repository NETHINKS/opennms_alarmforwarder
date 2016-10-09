{% include 'include/header.html.tpl' %}

<h1>Add new rule</h1>

<form method="POST" action="/rules/add">
    <div class="form-group">
        <label for="inputRule">Rule</label>
        <input type="text" class="form-control" id="inputRule" name="rule" placeholder="Rule">
    </div>
    <div class="form-group">
        <label for="inputTarget">Target</label>
        <select class="form-control" name="target" id="inputTarget">
        {% for target in targets %}
            <option>{{ target.target_name  }}</option>
        {% endfor %}
        </select>
    </div>
    <button type="submit" class="btn btn-default">Submit</button>
</form>
</table>

{% include 'include/footer.html.tpl' %}
