# coding: utf-8

from flask import request


class WebSockets(object):

    def __init__(self, app=None):
        self.app = app

    def init_app(self, app):
        pass