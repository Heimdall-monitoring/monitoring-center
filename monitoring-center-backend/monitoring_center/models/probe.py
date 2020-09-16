"""
Represent the configuration for a monitoring probe
"""

from typing import (
    Any,
    Dict,
    Optional,
)

from . import DB


class Probe(DB.Model):

    __tablename__ = 'Probes'

    uuid = DB.Column(DB.String(64), primary_key=True, nullable=False)
    name = DB.Column(DB.String(64), nullable=False)
    description = DB.Column(DB.String(64), nullable=True)

    def __init__(self, uuid: str, name: str, description: Optional[str] = None):
        self.uuid = uuid
        self.name = name
        self.description = description

    def __repr__(self) -> str:
        return f'Probe: (uuid: {self.uuid}, name: {self.name}, description: {self.description}'

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Probe):
            return False
        return self.to_dict() == other.to_dict()

    def to_dict(self) -> Dict[str, Any]:
        return {
            'uuid': self.uuid,
            'name': self.name,
            'description': self.description
        }
