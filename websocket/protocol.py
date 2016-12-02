# coding:utf-8

import base64
import hashlib

GUID = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"

class WebSocketProtocol(object):

    def __init__(self, secure=None, timeout=10):
        self.secure = secure
        self.timeout = timeout
        self.key = None

    @staticmethod
    def valid_request(req):
        try:
            assert req.headers['Upgrade'].lower() == 'websocket'
            assert any([param.strip() == 'upgrade' for param in req.headers['Connection'].lower().split(',')])
            key = req.headers['Sec-WebSocket-Key']
            assert req.headers['Sec-WebSocket-Version'] == '13'
        except Exception as e:
            raise e
        else:
            return key

    @staticmethod
    def build_response(res, key):
        res.headers['Upgrade'] = 'WebSocket'
        res.headers['Connection'] = 'Upgrade'
        res.headers['Sec-WebSocket-Accept'] = generate_accept_key(key)
        return res

    @staticmethod
    def generate_accept_key(key):
        sha1 = hashlib.sha1((key + GUID).encode()).digest()
        return base64.b64encode(sha1).decode()