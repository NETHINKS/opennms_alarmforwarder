import os
from flask import Flask
from flask import flash
from flask import jsonify
from flask import render_template
from flask import request
from flask import redirect
from flask import session
from flask import url_for
from sqlalchemy.orm import joinedload
import model
import forwarder
import receiver
import security
from webapp.auth import AuthenticationHandler
from webapp.json_helper import json_check
from webapp.json_helper import json_result
from webapp.json_helper import json_error

basedir = os.path.dirname(__file__)
app = Flask("opennms_alarmforwarder", template_folder=basedir+"/templates",
            static_folder=basedir+"/static")
app.secret_key = 'msdniuf7go832gfvzuztcur65'

@app.route("/")
@AuthenticationHandler.login_required
def index():
    return render_template("index.html.tpl")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if AuthenticationHandler.login(username, password):
            redirect_path = "/"
            try:
                redirect_path = session["redirect"]
                del session["redirect"]
            except:
                pass
            return redirect(redirect_path)
        else:
            error_msg = "Sorry, username or password wrong."
            flash(error_msg, "alert-danger")
    return render_template("login.html.tpl")

@app.route("/logout")
@AuthenticationHandler.login_required
def logout():
    AuthenticationHandler.logout()
    return redirect("/")



@app.route("/admin/users")
@AuthenticationHandler.login_required
def get_user_list():
    local_auth_provider = security.LocalUserAuthenticationProvider()
    users = local_auth_provider.list_users()
    if json_check():
        return jsonify(items=[user.dict_repr() for user in users])
    return render_template("user_list.html.tpl", users=users)

@app.route("/admin/users/add", methods=['POST'])
@AuthenticationHandler.login_required
def add_user():
    # check, if data are form data or json
    if request.get_json(silent=True) is not None:
        # add source from json data
        user_name = request.json["user_name"]
        user_password = request.json["user_password"]
    else:
        # add source from form data
        user_name = request.form["name"]
        user_password = request.form["password"]
    # add user
    local_auth_provider = security.LocalUserAuthenticationProvider()
    result = local_auth_provider.create_user(user_name, user_password)
    if not result:
        message = "Error adding user " + user_name
        if json_check():
            return json_error(message, 500)
        flash(message, "alert-danger")
    else:
        message = "User " + user_name + " successfully added."
        if json_check():
            return json_result(message, 200)
        flash(message, "alert-success")
    return redirect("/admin/users")

@app.route("/admin/users/<name>/delete")
@AuthenticationHandler.login_required
def delete_user(name):
    if name == session["username"]:
        message = "You cannot delete your own user account, please do not bite the hand that feeds you :-)"
        if json_check():
            return json_error(message, 500)
        flash(message, "alert-danger")
        return redirect("/admin/users")
    local_auth_provider = security.LocalUserAuthenticationProvider()
    result = local_auth_provider.delete_user(name)
    if not result:
        message = "User " + name + " not found!"
        if json_check():
            return json_error(message, 404)
        flash(message, "alert-danger")
        return redirect("/admin/users")
    else:
        message = "User " + name + " successfully deleted"
        if json_check():
            return json_result(message, 200)
        flash(message, "alert-success")
        return redirect("/admin/users")





@app.route("/sources")
@AuthenticationHandler.login_required
def get_source_list():
    orm_session = model.Session()
    sources = orm_session.query(model.Source).all()
    orm_session.close()
    if json_check():
        return jsonify(items=[source.dict_repr() for source in sources])
    return render_template("source_list.html.tpl", sources=sources)

@app.route("/sources/<name>")
@AuthenticationHandler.login_required
def get_source(name):
    orm_session = model.Session()
    source = orm_session.query(model.Source).filter(model.Source.source_name==name).first()
    orm_session.close()
    if source is None:
        error_msg = "Source " + name + " not found!"
        if json_check():
            return json_error(error_msg, 404)
        flash(error_msg, "alert-danger")
        return redirect("/sources")
    if json_check():
        return jsonify(source.dict_repr())
    return render_template("source_view.html.tpl", source=source)

@app.route("/sources/<name>/test")
@AuthenticationHandler.login_required
def test_source(name):
    orm_session = model.Session()
    source = orm_session.query(model.Source).filter(model.Source.source_name==name).first()
    orm_session.close()
    if source is None:
        error_msg = "Source " + name + " not found!"
        if json_check():
            return json_error(error_msg, 404)
        flash(error_msg, "alert-danger")
        return redirect("/sources")
    recv = receiver.OpennmsReceiver(source)
    test_result = recv.test_connection()
    result = {}
    result["result_state"] = "failed"
    result["result_msg"] = ""
    if test_result == 200:
        result["result_state"] = "success"
        result["result_msg"] = "Test of source " + name + " successful: HTTP/" + str(test_result)
        flash(result["result_msg"], "alert-success")
    elif test_result == -1:
        result["result_msg"] = "Test of source " + name + " failed: Error connecting to server"
        flash(result["result_msg"], "alert-danger")
    else:
        result["result_msg"] = "Test of source " + name + " failed: HTTP/" + str(test_result)
        flash(result["result_msg"], "alert-danger")
    if json_check():
        return jsonify(result)
    return redirect("/sources")

@app.route("/sources/<name>/edit", methods=['POST'])
@AuthenticationHandler.login_required
def edit_source(name):
    orm_session = model.Session()
    source = orm_session.query(model.Source).filter(model.Source.source_name==name).first()
    if source is None:
        orm_session.close()
        error_msg = "Source " + name + " not found!"
        if json_check():
            return json_error(error_msg, 404)
        flash(error_msg, "alert-danger")
        return redirect("/sources")
    else:
        # check, if data are form data or json
        if request.get_json(silent=True) is not None:
            # update source from json data
            source.source_url = request.json["source_url"]
            source.source_user = request.json["source_user"]
            source.source_password = request.json["source_password"]
            source.source_filter = request.json["source_filter"]
            orm_session.commit()
            orm_session.close()
            result_msg = "Source " + name + " successfully changed"
            return json_result(result_msg, 200)
        else:
            # update source from form data
            source.source_url = request.form["url"]
            source.source_user = request.form["user"]
            source.source_password = request.form["password"]
            source.source_filter = request.form["filter"]
            orm_session.commit()
            orm_session.close()
            flash("Source " + name + " successfully changed", "alert-success")
            return redirect("/sources")

@app.route("/sources/add", methods=['POST'])
@AuthenticationHandler.login_required
def add_source():
    # check, if data are form data or json
    if request.get_json(silent=True) is not None:
        # add source from json data
        source_name = request.json["source_name"]
        source_url = request.json["source_url"]
        source_user = request.json["source_user"]
        source_password = request.json["source_password"]
        source_filter = request.json["source_filter"]
    else:
        # add source from form data
        source_name = request.form["name"]
        source_url = request.form["url"]
        source_user = request.form["user"]
        source_password = request.form["password"]
        source_filter = request.form["filter"]
    # add source
    orm_session = model.Session()
    source = model.Source(source_name=source_name, source_url=source_url, source_user=source_user,
                          source_password=source_password, source_filter=source_filter,
                          source_status=model.Source.source_status_unknown)
    orm_session.add(source)
    orm_session.commit()
    orm_session.close()
    message = "Source " + source_name + " successfully added"
    if json_check():
        return json_result(message, 200)
    flash(message, "alert-success")
    return redirect("/sources")

@app.route("/sources/<name>/delete")
@AuthenticationHandler.login_required
def delete_source(name):
    orm_session = model.Session()
    source = orm_session.query(model.Source).filter(model.Source.source_name==name).first()
    if source is None:
        orm_session.close()
        message = "Source " + name + " not found!"
        if json_check():
            return json_error(message, 404)
        flash(message, "alert-danger")
        return redirect("/sources")
    else:
        orm_session.delete(source)
        orm_session.commit()
        orm_session.close()
        message = "Source " + name + " successfully deleted"
        if json_check():
            return json_result(message, 200)
        flash(message, "alert-success")
        return redirect("/sources")



@app.route("/targets")
@AuthenticationHandler.login_required
def get_target_list():
    orm_session = model.Session()
    targets = orm_session.query(model.Target).options(joinedload("target_parms")).all()
    forwarder_classes = forwarder.Forwarder.get_forwarder_classnames()
    orm_session.close()
    if json_check():
        return jsonify(items=[target.dict_repr() for target in targets])
    return render_template("target_list.html.tpl", targets=targets,
                           forwarder_classes=forwarder_classes)

@app.route("/targets/<name>")
@AuthenticationHandler.login_required
def get_target(name):
    orm_session = model.Session()
    target = orm_session.query(model.Target).options(joinedload("target_parms")).filter(model.Target.target_name==name).first()
    orm_session.close()
    if target is None:
        error_msg = "Target " + name + " not found!"
        if json_check():
            return json_error(error_msg, 404)
        flash(error_msg, "alert-danger")
        return redirect("/targets")
    else:
        if json_check():
            return jsonify(target.dict_repr())
        return render_template("target_view.html.tpl", target=target)

@app.route("/targets/<name>/test", methods=["GET", "POST"])
@AuthenticationHandler.login_required
def test_target(name):
    # check if message parameter is set
    message = None
    try:
        message = request.json["message"]
    except:
        pass
    try:
        message = request.form["message"]
    except:
        pass
    orm_session = model.Session()
    target = orm_session.query(model.Target).options(joinedload("target_parms")).filter(model.Target.target_name==name).first()
    orm_session.close()
    if target is None:
        error_msg = "Target " + name + " not found!"
        if json_check():
            return json_error(error_msg, 404)
        flash(error_msg, "alert-danger")
        return redirect("/targets")
    else:
        forwarder_obj = forwarder.Forwarder.create_forwarder(target.target_name, target.target_class, target.target_parms)
        forwarder_obj.test_forwarder(message)
        result_msg = "Target " + name + " tested"
        if json_check():
            return json_result(result_msg, 200)
        flash(result_msg, "alert-info")
        return redirect("/targets")

@app.route("/targets/<name>/delete")
@AuthenticationHandler.login_required
def delete_target(name):
    orm_session = model.Session()
    target = orm_session.query(model.Target).filter(model.Target.target_name==name).first()
    if target is None:
        orm_session.close()
        error_msg = "Target " + name + " not found!"
        if json_check():
            return json_error(error_msg, 404)
        flash(error_msg, "alert-danger")
        return redirect("/targets")
    else:
        orm_session.delete(target)
        orm_session.commit()
        orm_session.close()
        result_msg = "Target " + name + " successfully deleted"
        if json_check():
            return json_result(result_msg, 200)
        flash(result_msg, "alert-success")
        return redirect("/targets")

@app.route("/targets/add", methods=['POST'])
@AuthenticationHandler.login_required
def add_target():
    parameters = {}
    # check, if data are form data or json
    if request.get_json(silent=True) is not None:
        action = "add"
        target_name = request.json["target_name"]
        target_class = request.json["target_class"]
        target_delay = request.json["target_delay"]
        for request_parm in request.json["target_parms"]:
            parameters[request_parm] = request.json["target_parms"][request_parm]
    else:
        action = request.form["action"]
        target_name = request.form["name"]
        target_class = request.form["class"]
        target_delay = request.form["delay"]
        default_parameters = forwarder.Forwarder.get_default_parameters(target_class)
        for request_parm in request.form:
            if request_parm not in ["action", "class", "name", "delay"]:
                parameters[request_parm] = request.form[request_parm]
    if action == "show_form":
        return render_template("target_add.html.tpl", target_name=target_name,
                               target_class=target_class, target_delay=target_delay,
                               target_parameters=default_parameters)
    if action == "add":
        orm_session = model.Session()
        # add target
        target = model.Target(target_name=target_name, target_class=target_class,
                              target_delay=target_delay)
        orm_session.add(target)
        # add target parameters
        for parameter in parameters:
            parameter_obj = model.TargetParameter(target_name=target_name, parameter_name=parameter,
                                                  parameter_value=parameters[parameter])
            orm_session.add(parameter_obj)
        orm_session.commit()
        orm_session.close()
        result_msg = "Target " + target_name + " successfully added"
        if json_check():
            return json_result(result_msg, 200)
        flash(result_msg, "alert-success")
        return redirect("/targets")

@app.route("/targets/<name>/edit", methods=['POST'])
@AuthenticationHandler.login_required
def edit_target(name):
    orm_session = model.Session()
    target = orm_session.query(model.Target).filter(model.Target.target_name==name).first()
    if target is None:
        orm_session.close()
        error_msg = "Target " + name + " not found!"
        if json_check():
            return json_error(error_msg, 404)
        flash(error_msg, "alert-danger")
        return redirect("/targets")
    else:
        #update target parameters
        # check, if data are form data or json
        if request.get_json(silent=True) is not None:
            # update source from json data
            for request_parm in request.json["target_parms"]:
                for target_parm in target.target_parms:
                    if target_parm.parameter_name == request_parm:
                        target_parm.parameter_value = request.json["target_parms"][request_parm]
        else:
            # update source from form data
            for request_parm in request.form:
                if request_parm != "action" and request_parm != "class" and request_parm != "name":
                    for target_parm in target.target_parms:
                        if target_parm.parameter_name == request_parm:
                            target_parm.parameter_value = request.form[request_parm]
        orm_session.commit()
        orm_session.close()
        result_msg = "Target " + name + " successfully changed"
        if json_check():
            return json_result(result_msg, 200)
        flash(result_msg, "alert-success")
        return redirect("/targets")




@app.route("/rules")
@AuthenticationHandler.login_required
def get_rule_list():
    orm_session = model.Session()
    rules = orm_session.query(model.ForwardingRule).all()
    orm_session.close()
    if json_check():
        return jsonify(items=[rule.dict_repr() for rule in rules])
    return render_template("rule_list.html.tpl", rules=rules)

@app.route("/rules/<rule_id>")
@AuthenticationHandler.login_required
def get_rule(rule_id):
    orm_session = model.Session()
    targets = orm_session.query(model.Target).all()
    rule = orm_session.query(model.ForwardingRule).filter(model.ForwardingRule.rule_id==rule_id).\
                      first()
    if rule is None:
        orm_session.close()
        error_msg = "Rule " + rule_id + " not found!"
        if json_check():
            return json_error(error_msg, 404)
        flash(error_msg, "alert-danger")
        return redirect("/rules")
    if json_check():
        return jsonify(rule.dict_repr())
    return render_template("rule_view.html.tpl", rule=rule, targets=targets)

@app.route("/rules/add", methods=['GET', 'POST'])
@AuthenticationHandler.login_required
def add_rule():
    if request.method == 'GET':
        orm_session = model.Session()
        targets = orm_session.query(model.Target).all()
        orm_session.close()
        return render_template("rule_add.html.tpl", targets=targets)
    else:
        # check, if data are form data or json
        if request.get_json(silent=True) is not None:
            rule_match = request.json["rule_match"]
            rule_target = request.json["rule_target"]
        else:
            rule_match = request.form['rule']
            rule_target = request.form['target']
        orm_session = model.Session()
        rule = model.ForwardingRule(rule_match=rule_match, rule_target=rule_target)
        orm_session.add(rule)
        orm_session.commit()
        orm_session.close()
        result_msg = "Rule successfully added"
        if json_check():
            return json_result(result_msg, 200)
        flash("Rule successfully added", "alert-success")
        return redirect("/rules")

@app.route("/rules/<rule_id>/edit", methods=['POST'])
@AuthenticationHandler.login_required
def edit_rule(rule_id):
    orm_session = model.Session()
    rule = orm_session.query(model.ForwardingRule).filter(model.ForwardingRule.rule_id==rule_id).\
                      first()
    if rule is None:
        orm_session.close()
        error_msg = "Rule " + rule_id + " not found!"
        if json_check():
            return json_error(error_msg, 404)
        flash(error_msg, "alert-danger")
        return redirect("/rules")
    else:
        # check, if data are form data or json
        if request.get_json(silent=True) is not None:
            rule.rule_target = request.json["rule_target"]
            rule.rule_match = request.json["rule_match"]
        else:
            rule.rule_target = request.form["target"]
            rule.rule_match = request.form["match"]
        orm_session.commit()
        orm_session.close()
        result_msg = "Rule successfully changed"
        if json_check():
            return json_result(result_msg, 200)
        flash(result_msg, "alert-success")
        return redirect("/rules")

@app.route("/rules/<rule_id>/delete")
@AuthenticationHandler.login_required
def delete_rule(rule_id):
    orm_session = model.Session()
    rule = orm_session.query(model.ForwardingRule).filter(model.ForwardingRule.rule_id==rule_id).\
                      first()
    if rule is None:
        orm_session.close()
        error_msg = "Rule " + rule_id + " not found!"
        if json_check():
            return json_error(error_msg, 404)
        flash(error_msg, "alert-danger")
        return redirect("/rules")
    else:
        orm_session.delete(rule)
        orm_session.commit()
        orm_session.close()
        result_msg = "Rule successfully deleted"
        if json_check():
            return json_result(result_msg, 200)
        flash(result_msg, "alert-success")
        return redirect("/rules")

