import pytest
from rmr.ratings import get_ucs_rating, get_rqd_rating, get_spacing_rating

def test_ucs_ratings():
    assert get_ucs_rating(300) == 15
    assert get_ucs_rating(150) == 12
    assert get_ucs_rating(75) == 7
    assert get_ucs_rating(35) == 4
    assert get_ucs_rating(15) == 2
    assert get_ucs_rating(3) == 1
    assert get_ucs_rating(0.5) == 0

def test_rqd_ratings():
    assert get_rqd_rating(95) == 20
    assert get_rqd_rating(80) == 17
    assert get_rqd_rating(60) == 13
    assert get_rqd_rating(30) == 8
    assert get_rqd_rating(10) == 3
    
    with pytest.raises(ValueError):
        get_rqd_rating(105)

def test_spacing_ratings():
    assert get_spacing_rating(2.5) == 20
    assert get_spacing_rating(1.0) == 15
    assert get_spacing_rating(0.4) == 10
    assert get_spacing_rating(0.1) == 8
    assert get_spacing_rating(0.02) == 5