"""
Represent the returned data from a monitoring probe
"""

from datetime import datetime
from typing import Optional
from uuid import uuid1

from . import DB


class Stats(DB.Model):

    __tablename__ = 'Stats'

    uuid = DB.Column(DB.String(64), nullable=False, primary_key=True)
    probe_uuid = DB.Column(DB.String(64), nullable=False)
    date = DB.Column(DB.DateTime, nullable=False)

    os = DB.Column(DB.String(32))
    kernel = DB.Column(DB.String(32))
    distro = DB.Column(DB.String(32))
    machine_name = DB.Column(DB.String(64))
    machine = DB.Column(DB.String(64))

    ram_available = DB.Column(DB.Integer)
    ram_free = DB.Column(DB.Integer)
    uptime_seconds = DB.Column(DB.Integer)

    def __init__(self, probe_uuid: str, date: datetime):
        probe_uuid_int = int(probe_uuid, 16)
        self.uuid = uuid1(probe_uuid_int).hex
        self.probe_uuid = probe_uuid
        self.date = date

    def __repr__(self) -> str:
        return f'Stats: (uuid: {self.uuid}, probe: {self.probe_uuid}, date: {self.date}) - '

    def set_os_info(
            self, os: Optional[str] = None,
            kernel: Optional[str] = None, distro: Optional[str] = None,
            machine_name: Optional[str] = None, machine: Optional[str] = None,
    ):
        self.os = os
        self.kernel = kernel
        self.distro = distro
        self.machine_name = machine_name
        self.machine = machine

    def set_ram(self, ram_avaible: int, ram_free: int):
        self.ram_available = ram_avaible
        self.ram_free = ram_free

    def set_uptime(self, uptime: int):
        self.uptime_seconds = uptime
