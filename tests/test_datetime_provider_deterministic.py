from datetime import datetime

from datetime_provider.datetime_provider_deterministic import DateTimeProviderDeterministic


def test_give_fed_datetime_when_now() -> None:
    datetime_provider = DateTimeProviderDeterministic()
    datetime_provider.feed(now=datetime(2023, 7, 17))
    assert datetime_provider.now() == datetime(2023, 7, 17)