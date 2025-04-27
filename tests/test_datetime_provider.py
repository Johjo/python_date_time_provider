from datetime import datetime

from datetime_provider.primary_port import DateTimeProviderPrimaryPort


class DateTimeProvider(DateTimeProviderPrimaryPort):
    def now(self) -> datetime:
        return datetime.now()


def test_give_real_datetime_when_now() -> None:
    datetime_provider = DateTimeProvider()
    first = datetime_provider.now()
    second = datetime_provider.now()
    assert first != second
