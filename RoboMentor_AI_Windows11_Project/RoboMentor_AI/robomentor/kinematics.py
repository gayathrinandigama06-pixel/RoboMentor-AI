"""Planar two-link robot kinematics."""
import math
import numpy as np

def forward_kinematics(l1: float, l2: float, theta1: float, theta2: float):
    """Return end-effector (x, y) for angles in radians."""
    x = l1 * math.cos(theta1) + l2 * math.cos(theta1 + theta2)
    y = l1 * math.sin(theta1) + l2 * math.sin(theta1 + theta2)
    return (x, y)

def inverse_kinematics(l1: float, l2: float, x: float, y: float, elbow: str = "down"):
    """Return (theta1, theta2) in radians, or None if unreachable."""
    if l1 <= 0 or l2 <= 0:
        raise ValueError("Link lengths must be positive.")
    r2 = x*x + y*y
    c2 = (r2 - l1*l1 - l2*l2) / (2*l1*l2)
    if c2 < -1.0 - 1e-9 or c2 > 1.0 + 1e-9:
        return None
    c2 = max(-1.0, min(1.0, c2))
    sign = -1.0 if elbow == "down" else 1.0
    s2 = sign * math.sqrt(max(0.0, 1.0-c2*c2))
    theta2 = math.atan2(s2, c2)
    theta1 = math.atan2(y, x) - math.atan2(l2*s2, l1+l2*c2)
    return (theta1, theta2)

def interpolate_path(start, goal, steps=50):
    """Generate evenly spaced 2D points, including start and goal."""
    if steps < 2:
        raise ValueError("steps must be at least 2")
    return [tuple(map(float, p)) for p in np.linspace(start, goal, steps)]
