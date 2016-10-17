import os
from flask import Flask
from flask import flash
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
import model
import forwarder

basedir = os.path.dirname(__file__)
app = Flask("opennms_alarmforwarder", template_folder=basedir+"/templates",
            static_folder=basedir+"/static")
app.secret_key = 'msdniuf7go832gfvzuztcur65'

@app.route("/")
def index():
    return render_template("index.html.tpl")



@app.route("/sources")
def get_source_list():
    orm_session = model.Session()
    sources = orm_session.query(model.Source).all()
    orm_session.close()
    return render_template("source_list.html.tpl", sources=sources)

@app.route("/sources/add", methods=['POST'])
def add_source():
    source_name = request.form["name"]
    source_url = request.form["url"]
    source_user = request.form["user"]
    source_password = request.form["password"]
    source_filter = request.form["filter"]
    orm_session = model.Session()
    # add source
    source = model.Source(source_name=source_name, source_url=source_url, source_user=source_user,
                          source_password=source_password, source_filter=source_filter)
    orm_session.add(source)
    orm_session.commit()
    orm_session.close()
    flash("Source " + source_name + " successfully added", "alert-success")
    return redirect("/sources")

@app.route("/sources/<name>/delete")
def delete_source(name):
    orm_session = model.Session()
    source = orm_session.query(model.Source).filter(model.Source.source_name==name).first()
    if source is None:
        orm_session.close()
        flash("Source " + name + " not found!", "alert-danger")
        return redirect("/sources")
    else:
        orm_session.delete(source)
        orm_session.commit()
        orm_session.close()
        flash("Source " + name + " successfully deleted", "alert-success")
        return redirect("/sources")



@app.route("/targets")
def get_target_list():
    orm_session = model.Session()
    targets = orm_session.query(model.Target).all()
    forwarder_classes = ['StdoutForwarder']
    orm_session.close()
    return render_template("target_list.html.tpl", targets=targets,
                           forwarder_classes=forwarder_classes)

@app.route("/targets/<name>")
def get_target(name):
    orm_session = model.Session()
    target = orm_session.query(model.Target).filter(model.Target.target_name==name).first()
    if target is None:
        orm_session.close()
        flash("Target " + name + " not found!", "alert-danger")
        return redirect("/targets")
    else:
        parameters = target.target_parms
        orm_session.close()
        return render_template("target_view.html.tpl", target=target, parameters=parameters)

@app.route("/targets/<name>/delete")
def delete_target(name):
    orm_session = model.Session()
    target = orm_session.query(model.Target).filter(model.Target.target_name==name).first()
    if target is None:
        orm_session.close()
        flash("Target " + name + " not found!", "alert-danger")
        return redirect("/targets")
    else:
        orm_session.delete(target)
        orm_session.commit()
        orm_session.close()
        flash("Target " + name + " successfully deleted", "alert-success")
        return redirect("/targets")

@app.route("/targets/add", methods=['POST'])
def add_target():
    action = request.form["action"]
    target_name = request.form["name"]
    target_class = request.form["class"]
    default_parameters = forwarder.Forwarder.get_default_parameters(target_class)
    parameters = {}
    for request_parm in request.form:
        if request_parm != "action" and request_parm != "class" and request_parm != "name":
            parameters[request_parm] = request.form[request_parm]
    if action == "show_form":
        return render_template("target_add.html.tpl", target_name=target_name,
                               target_class=target_class, target_parameters=default_parameters)
    if action == "add":
        orm_session = model.Session()
        # add target
        target = model.Target(target_name=target_name, target_class=target_class)
        orm_session.add(target)
        # add target parameters
        for parameter in parameters:
            parameter_obj = model.TargetParameter(target_name=target_name, parameter_name=parameter,
                                                  parameter_value=parameters[parameter])
            orm_session.add(parameter_obj)
        orm_session.commit()
        orm_session.close()
        flash("Target " + target_name + " successfully added", "alert-success")
        return redirect("/targets")



@app.route("/rules")
def get_rule_list():
    orm_session = model.Session()
    rules = orm_session.query(model.ForwardingRule).all()
    orm_session.close()
    return render_template("rule_list.html.tpl", rules=rules)

@app.route("/rules/add", methods=['GET', 'POST'])
def add_rule():
    if request.method == 'GET':
        orm_session = model.Session()
        targets = orm_session.query(model.Target).all()
        orm_session.close()
        return render_template("rule_add.html.tpl", targets=targets)
    else:
        orm_session = model.Session()
        rule_match = request.form['rule']
        rule_target = request.form['target']
        rule = model.ForwardingRule(rule_match=rule_match, rule_target=rule_target)
        orm_session.add(rule)
        orm_session.commit()
        orm_session.close()
        flash("Rule successfully added", "alert-success")
        return redirect("/rules")

@app.route("/rules/<rule_id>/delete")
def delete_rule(rule_id):
    orm_session = model.Session()
    rule = orm_session.query(model.ForwardingRule).filter(model.ForwardingRule.rule_id==rule_id).\
                      first()
    if rule is None:
        orm_session.close()
        flash("Rule " + rule_id + " not found!", "alert-danger")
        return redirect("/rules")
    else:
        orm_session.delete(rule)
        orm_session.commit()
        orm_session.close()
        flash("Rule successfully deleted", "alert-success")
        return redirect("/rules")
