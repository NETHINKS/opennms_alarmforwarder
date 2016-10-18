#! /usr/bin/python3
"""Main module
"""
import os
import logging
import logging.config
import model
from receiver import OpennmsReceiver
from scheduler import Scheduler
from config import Config

def main():
    # get directory name
    basedir = os.path.dirname(__file__)

    # configure logging
    logging.basedir = basedir + "/logs"
    logging.config.fileConfig(basedir + "/etc/logging.conf")

    # init
    config = Config()
    scheduler = Scheduler(config)

    # run scheduler
    try:
        scheduler.run()
    except KeyboardInterrupt:
        print("Shutting down...")


if __name__ == "__main__":
    main()
