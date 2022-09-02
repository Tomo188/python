from test import square
import pytest


def testPositive():
    assert square(3) == 9
    assert square(2) == 4


def testNegative():
    assert square(-2) == 4
    assert square(-3) == 9


def testNull():
    assert square(0) == 0


def test_str():
    with pytest.raises(TypeError):
        square("str")
