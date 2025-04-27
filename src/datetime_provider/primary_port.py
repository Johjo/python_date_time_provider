from abc import ABC, abstractmethod
from datetime import datetime


class DateTimeProviderPrimaryPort(ABC):
    @abstractmethod
    def now(self) -> datetime:
        pass
