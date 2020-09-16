"""
Main package for the application
"""
from pathlib import Path

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from .config import SQLiteDatabaseConfig
from .models import (
    DB,
    Probe,
)
from .views import (
    API_VIEWS,
    MAIN_VIEWS,
)


def create_app(debug=False):
    db_file = Path('/tmp/test.db')
    db_config = SQLiteDatabaseConfig(db_file)
    print(f'Connecting to database {db_config.database_uri}')

    app = Flask(__name__)
    app.debug = debug
    app.config['SQLALCHEMY_DATABASE_URI'] = db_config.database_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.register_blueprint(MAIN_VIEWS)
    app.register_blueprint(API_VIEWS, url_prefix='/api')
    DB.init_app(app)
    Migrate(app, DB)

    @app.after_request
    def add_header(response):
        response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
        return response

    return app
