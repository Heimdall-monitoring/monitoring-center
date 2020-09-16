from pathlib import Path

from flask_sqlalchemy import SQLAlchemy

from monitoring_center import create_app
from monitoring_center.config import SQLiteDatabaseConfig


# @APP.shell_context_processor
# def make_shell_context():
#     """Create the base shell context for Flask CLI."""
#     return dict(app=APP, db=db, User=User)


if __name__ == '__main__':

    app = create_app(debug=True)
    app.run(port=5000, host='0.0.0.0')
