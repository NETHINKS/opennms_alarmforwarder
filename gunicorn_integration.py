import multiprocessing
import gunicorn.app.base
from gunicorn.six import iteritems

class WebApplication(gunicorn.app.base.BaseApplication):

    def __init__(self, application, options):
        self.options = options
        self.application = application
        super(WebApplication, self).__init__()

    def load_config(self):
        config = dict([(key, value) for key, value in iteritems(self.options)
                       if key in self.cfg.settings and value is not None])
        for key, value in iteritems(config):
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application
