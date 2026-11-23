import pytest
from robomentor.safety import point_is_clear, path_is_clear

def test_point_clear_and_inside():
    assert point_is_clear((2,0), (0,0), 1)
    assert not point_is_clear((0.5,0), (0,0), 1)

def test_path_blocked():
    assert not path_is_clear((0,0), (4,0), (2,0), 0.5)

def test_path_clear():
    assert path_is_clear((0,0), (4,0), (2,2), 0.5)

def test_touching_counts_as_collision():
    assert not path_is_clear((0,0), (4,0), (2,1), 1)

def test_negative_radius_rejected():
    with pytest.raises(ValueError):
        point_is_clear((0,0), (1,1), -1)
