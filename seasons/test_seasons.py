from seasons import seasons
import pytest

def test_default():
    assert seasons("2023-01-17") == "One million, fifty-two thousand, six hundred forty minutes"

def test_exit():
    with pytest.raises(SystemExit):
        seasons("January 1, 1999")

