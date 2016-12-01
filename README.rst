===============
Flask-WebSocket
===============

WebSocket for Flask apps.

Usage
-----

.. code-block:: python

    ws = WebSocket(app, prefix='/ws')

    @ws.on_message
    def on_message(msg):
        # echo message
        ws.send(msg)

    @ws.on_open
    def on_open():
        logger.info('connection is opend')

    @ws.on_close
    def on_close():
        logger.info('connection is closed')

    @ws.on_error
    def on_error(err):
        logger.info('error_code[%s], msg[%s]' % (err.code, err.msg))

Licence
-------

`BSD <https://github.com/bulbulpaul/flask-websocket/blob/master/LICENCE>`_ 

Author
------

'bulbulpaul <https://github.com/bulbulpaul>`_ 
