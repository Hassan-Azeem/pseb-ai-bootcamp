import pytest

from adult import is_adult


def test_is_adult_below_threshold():
    assert is_adult(17) is False


def test_is_adult_at_threshold():
    assert is_adult(18) is True


def test_is_adult_rejects_negative_age():
    with pytest.raises(ValueError):
        is_adult(-1)
