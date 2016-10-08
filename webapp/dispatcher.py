import os
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
import model

basedir = os.path.dirname(__file__)
app = Flask("opennms_alarmforwarder", template_folder=basedir+"/templates")

@app.route("/")
def index():
    return render_template("index.html.tpl")

@app.route("/targets")
def targets():
    orm_session = model.Session()
    targets = orm_session.query(model.Target).all()
    orm_session.close()
    return render_template("targets.html.tpl", targets=targets)
