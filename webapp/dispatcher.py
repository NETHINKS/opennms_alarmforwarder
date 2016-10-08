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
    orm_session.close()
    return render_template("target_list.html.tpl", targets=targets)

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



@app.route("/rules")
def get_rule_list():
    orm_session = model.Session()
    rules = orm_session.query(model.ForwardingRule).all()
    orm_session.close()
    return render_template("rule_list.html.tpl", rules=rules)
