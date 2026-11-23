import math
import pytest
from robomentor.kinematics import forward_kinematics, inverse_kinematics, interpolate_path

def test_forward_kinematics_straight():
    x, y = forward_kinematics(2, 3, 0, 0)
    assert x == pytest.approx(5)
    assert y == pytest.approx(0)

@pytest.mark.parametrize("elbow", ["up", "down"])
def test_inverse_round_trip(elbow):
    target = (3.0, 2.0)
    angles = inverse_kinematics(3, 2, *target, elbow=elbow)
    assert angles is not None
    actual = forward_kinematics(3, 2, *angles)
    assert actual[0] == pytest.approx(target[0])
    assert actual[1] == pytest.approx(target[1])

def test_unreachable_target():
    assert inverse_kinematics(1, 1, 5, 5) is None

def test_interpolation_includes_endpoints():
    points = interpolate_path((0,0), (2,4), 5)
    assert points[0] == (0.0, 0.0)
    assert points[-1] == (2.0, 4.0)
    assert len(points) == 5
