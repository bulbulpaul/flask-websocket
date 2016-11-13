# coding: utf-8
#!/usr/bin/env python

"""
Flask-WebSocket
-------------

WebSocket for Flask apps.
"""
from setuptools import setup


setup(
    name='Flask-WebSocket',
    version='0.0.1',
    url='https://github.com/bulbulpaul/flask-websocket',
    license='See License',
    author='Nobuo Okada',
    author_email='bulbulpaul0325@gmail.com',
    description='WebSocket for Flask apps.',
    long_description=__doc__,
    py_modules=['flask_websocket'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    extras_require={
        ':python_version=="3.3"': ['asyncio'],
    },
)