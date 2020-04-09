import os
import json
import ccpncdb


class Config(object):
    """"Configuration file"""

    _default_path = os.path.abspath(os.path.join(
        ccpncdb.__path__[0],
        '../config/config.json'))

    def __init__(self, path=_default_path):
        try:
            with open(path) as f:
                self.data = json.load(f)
        except IOError:
            self.data = {}

    @property
    def db_url(self):
        return self.data.get('db_url', 'localhost')

    @property
    def db_port(self):
        return self.data.get('db_port', 27017)
