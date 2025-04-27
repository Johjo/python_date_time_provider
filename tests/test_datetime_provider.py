from datetime_provider import DateTimeProvider


def test_give_real_datetime_when_now() -> None:
    datetime_provider = sDateTimeProvider()
    first = datetime_provider.now()
    second = datetime_provider.now()
    assert first != second
