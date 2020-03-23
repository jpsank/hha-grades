import os

import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

from flask import Flask, render_template, request
import logging
from logging.handlers import RotatingFileHandler

from config import Config, basedir


if Config.SENTRY_DSN:
    sentry_sdk.init(
        dsn=Config.SENTRY_DSN,
        integrations=[FlaskIntegration()]
    )


app = Flask(__name__, static_url_path="/hha-grades/app/static")
app.config.from_object(Config)

if not app.debug and not app.testing:
    logs_path = os.path.join(basedir, 'logs')
    if not os.path.exists(logs_path):
        os.mkdir(logs_path)
    handler = RotatingFileHandler(os.path.join(logs_path, 'grades.log'), maxBytes=10240, backupCount=1)
    app.logger.addHandler(handler)

    app.logger.setLevel(logging.WARNING)
    app.logger.info('HHA Grades startup')


from app import routes
