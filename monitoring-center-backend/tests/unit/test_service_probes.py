"""
Test the methods related to probes service
"""

from monitoring_center.models import Probe
from monitoring_center.services import probes_service


def test_get_all_probes_1(db_session):
    service = probes_service.ProbeService(db_session)
    assert service.get_all_probes() == []


def test_get_all_probes_2(db_session):
    db_session.add(Probe('1234', 'test1', 'description test'))
    db_session.add(Probe('5678', 'test2'))
    db_session.commit()
    service = probes_service.ProbeService(db_session)
    assert service.get_all_probes() == [
        Probe('1234', 'test1', 'description test'),
        Probe('5678', 'test2'),
    ]
