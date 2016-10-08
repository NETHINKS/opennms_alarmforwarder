#! /usr/bin/python3
"""Main module
"""
import model
from receiver import OpennmsReceiver
from scheduler import Scheduler
from config import Config

def main():
    # init
    config = Config()
    receiver = OpennmsReceiver(config)
    scheduler = Scheduler(config, receiver)

    # start scheduler
    scheduler.run()


if __name__ == "__main__":
    main()
