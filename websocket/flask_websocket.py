# coding: utf-8

from flask import request


class WebSocket(object):

    def __init__(self, app=None, prefix='/ws'):
        self.app = app
        self.init_app(app)

    def init_app(self, app):
        app.add_url_rule(self.prefix, 'ws', self._handler)

    def on_message(self, msg):
        def decorator(fn):
            pass
            return f
        return 

    def on_open(self):
        def decorator(fn):
            pass
            return f
        return 

    def on_close(self):
        def decorator(fn):
            pass
            return f
        return 

    def on_error(self):
        def decorator(fn):
            pass
            return f
        return 

    def send(self):
        pass

    def _handler(self):
        pass