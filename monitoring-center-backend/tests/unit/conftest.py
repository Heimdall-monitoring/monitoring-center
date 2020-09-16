from pathlib import Path

import pytest

from alembic.command import upgrade as alembic_upgrade
from alembic.config import Config as AlembicConfig
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from monitoring_center.config import SQLiteDatabaseConfig


@pytest.fixture(name='app', scope="session")
def fixture_app(request):
    config = SQLiteDatabaseConfig(Path('/tmp/test_db.db'))
    flask_app = Flask(__name__)
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = config.database_uri
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    @request.addfinalizer
    def drop_database():
        Path('/tmp/test_db.db').unlink()

    return flask_app


@pytest.fixture(scope='session')
def _db(app):
    db = SQLAlchemy(app)
    with app.app_context():
        Migrate(app, db)
        alembic_config = AlembicConfig('migrations/alembic.ini')
        alembic_config.set_main_option('sqlalchemy.url', app.config['SQLALCHEMY_DATABASE_URI'])
        alembic_upgrade(alembic_config, 'head')
    return db
