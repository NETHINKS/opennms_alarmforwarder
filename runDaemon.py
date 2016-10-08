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

    # run scheduler
    try:
        scheduler.run()
    except KeyboardInterrupt:
        print("Shutting down...")


if __name__ == "__main__":
    main()
