# -*- coding: utf-8 -*-
"""
    myip.factory
    ~~~~~~~~~~~~~~~

    Contains create_app method for instantiating applications.
"""

from flask import Flask
from myip.views import bp as main_views


def create_app(package_name, settings_override=None):
    """Returns a :class:`Flask` application instance configured with common
    functionality for the myip platform.

    :param package_name: application package name
    :param package_path: application package path
    :param settings_override: a dictionary of setings to override
    """
    app = Flask(package_name, instance_relative_config=True)
    app.register_blueprint(main_views)
    return app
