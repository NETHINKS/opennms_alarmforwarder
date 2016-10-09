import os
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
import model

basedir = os.path.dirname(__file__)
app = Flask("opennms_alarmforwarder", template_folder=basedir+"/templates",
            static_folder=basedir+"/static")

@app.route("/")
def index():
    return render_template("index.html.tpl")



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
    orm_session.close()
    if target is None:
        error_msg = "Target " + name + " not found!"
        return render_template("error.html.tpl", message=error_msg)
    else:
        return render_template("target_view.html.tpl", target=target)

@app.route("/targets/add", methods=['POST'])
def add_target():
    action = request.form["action"]
    target_name = request.form["name"]
    target_class = request.form["class"]
    parameters = {}
    if action == "show_form":
        return render_template("target_add.html.tpl", target_name=target_name,
                               target_class=target_class, target_parameters=parameters)
    if action == "add":
        orm_session = model.Session()
        target = model.Target(target_name=target_name, target_class=target_class)
        orm_session.add(target)
        orm_session.commit()
        orm_session.close()
        return render_template("index.html.tpl")



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
        return render_template("index.html.tpl")

@app.route("/rules/<rule_id>/delete")
def delete_rule(rule_id):
    orm_session = model.Session()
    rule = orm_session.query(model.ForwardingRule).filter(model.ForwardingRule.rule_id==rule_id).\
                      first()
    if rule is None:
        orm_sesion.close()
        error_msg = "Rule " + rule_id + "not found!"
        return render_template("error.html.tpl", message=error_msg)
    else:
        orm_session.delete(rule)
        orm_session.commit()
        orm_session.close()
        return render_template("index.html.tpl")
