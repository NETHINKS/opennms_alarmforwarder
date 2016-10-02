#! /usr/bin/python3
"""Main module
"""
import model
from receiver import OpennmsReceiver
from scheduler import Scheduler

def main():
    # init
    config = None
    receiver = OpennmsReceiver(config)
    scheduler = Scheduler(config, receiver)
    scheduler.run()


if __name__ == "__main__":
    main()
