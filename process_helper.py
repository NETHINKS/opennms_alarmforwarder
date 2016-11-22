"""
multiprocess handling helper module

:license: MIT, see LICENSE for more details
:copyright: (c) 2016 by NETHINKS GmbH, see AUTORS for more details
"""

class GracefulShutdown(Exception):
    """define the GracefulShutdown Exception"""
    pass

def shutdown_handler(signum, frame):
    """Shutdown Handler. Creates a GracefulShutdown Exception"""
    raise GracefulShutdown("shudown received")


