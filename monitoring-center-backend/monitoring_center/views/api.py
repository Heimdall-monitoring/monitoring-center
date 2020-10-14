"""
Views relative to the API
"""

from datetime import datetime

from flask import (
    Blueprint,
    jsonify,
    request,
)

from ..models import (
    DB,
    Stats,
)
from ..services import ProbeService


API_VIEWS = Blueprint('api_views', __name__)


@API_VIEWS.route('/probes')
def get_probes():
    service = ProbeService(DB.session)
    return jsonify([probe.to_dict() for probe in service.get_all_probes()])


@API_VIEWS.route('/stats', methods=['POST'])
def add_stats():
    service = ProbeService(DB.session)
    data = request.json
    new_stats = Stats(data['uuid'], datetime.fromisoformat(data['datetime']))
    if 'ram-usage' in data:
        new_stats.set_ram(data['ram-usage']['available'], data['ram-usage']['free'])
    if 'system-info' in data:
        system_info = data['system-info']
        new_stats.set_os_info(
            system_info['operating-system'], system_info['kernel'],
            system_info['distro'], system_info['name'], system_info['machine'],
        )
    if 'uptime' in data:
        new_stats.set_uptime(data['uptime'])
    service.save_new_stats(new_stats)
    return "ok"
