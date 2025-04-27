from datetime import datetime

from datetime_provider.primary_port import DateTimeProviderPrimaryPort


class DateTimeProvider(DateTimeProviderPrimaryPort):
    def now(self) -> datetime:
        return datetime.now()
