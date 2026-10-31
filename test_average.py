import pytest

from average import avg


def test_avg_returns_average():
    assert avg([1, 2, 3]) == 2


def test_avg_rejects_empty_list():
    with pytest.raises(ValueError, match="at least one number"):
        avg([])
