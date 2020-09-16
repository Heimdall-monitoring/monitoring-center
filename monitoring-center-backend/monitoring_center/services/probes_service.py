"""
Handle database access for the Probes object
"""

from typing import (
    List,
    cast,
)

from flask_sqlalchemy import SessionBase

from ..models import Probe


class ProbeService:
    def __init__(self, db_session: SessionBase):
        self._db_session = db_session

    def get_all_probes(self) -> List[Probe]:
        return cast(List[Probe], self._db_session.query(Probe).all())
