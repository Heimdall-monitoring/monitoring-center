"""
Test the probe model
"""

from monitoring_center import Probe


def test_equality_1():
    assert Probe('1234', 'name1') == Probe('1234', 'name1')
    assert Probe('1234', 'name2', 'description') == Probe('1234', 'name2', 'description')


def test_equality_2():
    assert Probe('1234', 'name2') != Probe('1234', 'name3')
    assert Probe('1234', 'name2') != Probe('12344', 'name2')
    assert Probe('1234', 'name2', 'description') != Probe('1234', 'name2', 'description2')
    assert Probe('1234', 'name2', 'description') != Probe('1234', 'name2')


def test_equality_3():
    assert Probe('1234', 'name') != {'uuid': '1234', 'name': 'name'}
