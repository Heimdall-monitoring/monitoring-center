"""
Handle the configuration for the database
"""
import abc
import tempfile

from pathlib import Path


class BaseDatabaseConfig(abc.ABC):
    """Represent the base configuration for a database connection
    """

    @property
    @abc.abstractmethod
    def database_uri(self) -> str:
        raise NotImplementedError()

    @abc.abstractmethod
    def is_valid(self) -> bool:
        raise NotImplementedError()


class SQLiteDatabaseConfig(BaseDatabaseConfig):
    """Represent the configuration for a sqlite database connection
    """

    def __init__(self, filepath: Path):
        self._path = filepath

    @property
    def database_uri(self) -> str:
        return f'sqlite:///{self._path}'

    def is_valid(self) -> bool:
        # If the file exists, it should be ok
        if self._path.exists():
            return True

        # If the file does not exist, check that it's at least possible to write in this directory
        try:
            testfile = tempfile.TemporaryFile(dir=self._path.parent)
            testfile.close()
            return True
        except OSError:
            return False
