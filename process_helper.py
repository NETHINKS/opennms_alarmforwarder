"""helper for multiprocess handling"""

class GracefulShutdown(Exception):
    pass

def shutdown_handler(signum, frame):
    raise GracefulShutdown("shudown received")


