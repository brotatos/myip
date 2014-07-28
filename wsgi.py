# -*- coding: utf-8 -*-
"""
    wsgi
    ~~~~

    ieee wsgi module
"""

from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware

from myip.factory import create_app

application = create_app(__name__)

if __name__ == "__main__":
    run_simple('localhost', 5000, application, use_reloader=True,
               use_debugger=True, use_evalex=True)
