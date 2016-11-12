#! /usr/bin/python3
"""Main module
"""
from multiprocessing import Process
import os
import logging
import logging.config
import model
from receiver import OpennmsReceiver
from scheduler import Scheduler
from config import Config
from gunicorn_integration import WebApplication
from webapp.dispatcher import app as wsgi_app

def main():
    # get directory name
    basedir = os.path.dirname(__file__)

    # configure logging
    logging.basedir = basedir + "/logs"
    logging.config.fileConfig(basedir + "/etc/logging.conf")

    # init
    config = Config()
    scheduler = Scheduler(config)
    webapp_conf = {
        "bind": "0.0.0.0:5000"
    }
    webapp = WebApplication(wsgi_app, webapp_conf)

    # run scheduler
    print("Starting opennms_alarmforwarder...")
    proc_webapp = Process(target=webapp.run)
    proc_scheduler = Process(target=scheduler.run)
    proc_webapp.start()
    proc_scheduler.start()

    try:
        proc_scheduler.join()
        proc_webapp.join()
    except KeyboardInterrupt:
        print("Stopping opennms_alarmforwarder...")
        proc_scheduler.terminate()
        proc_webapp.terminate()
        print("...exited")



if __name__ == "__main__":
    main()
