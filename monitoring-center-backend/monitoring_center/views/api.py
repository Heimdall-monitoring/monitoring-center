"""
Views relative to the API
"""

from flask import (
    Blueprint,
    jsonify,
)

from ..models import DB
from ..services import ProbeService


API_VIEWS = Blueprint('api_views', __name__)


@API_VIEWS.route('/probes')
def get_probes():
    service = ProbeService(DB.session)
    return jsonify([probe.to_dict() for probe in service.get_all_probes()])
