# -*- coding: utf-8 -*-
"""
    myip.factory
    ~~~~~~~~~~~~~~~

    Contains create_app method for instantiating applications.
"""

from flask import Flask
from myip import config
from myip.views import bp as main_views


def create_app():
    """Returns a :class:`Flask` application instance configured with common
    functionality for the myip platform.

    :param package_name: application package name
    :param settings_override: a dictionary of setings to override
    """
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(config)
    app.register_blueprint(main_views)

    return app
