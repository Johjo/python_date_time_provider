from datetime import datetime

from datetime_provider.primary_port import DateTimeProviderPrimaryPort


class DateTimeProviderDeterministic(DateTimeProviderPrimaryPort):
    def __init__(self) -> None:
        self._now : datetime | None = None

    def now(self) -> datetime:
        if self._now is None:
            raise RuntimeError("DateTimeProviderFixed.now() called before feed()")
        return self._now

    def feed(self, now: datetime) -> None:
        self._now = now
